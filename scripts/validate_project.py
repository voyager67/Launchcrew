#!/usr/bin/env python3
"""Validate LaunchCrew skills, Codex agents, release docs, and community configuration."""
from __future__ import annotations

from pathlib import Path
import json
import re
import sys
import tomllib
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
REQUIRED = [
    "README.md", "AGENTS.md", "LICENSE", "CONTRIBUTING.md", "SECURITY.md",
    "CODE_OF_CONDUCT.md", "CHANGELOG.md", "manifest.json",
    ".github/workflows/ci.yml", ".github/workflows/sync-labels.yml",
    ".github/labels.json",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/compatibility_report.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/pull_request_template.md",
    "docs/architecture.md", "docs/codex.md", "docs/chatgpt.md",
    "docs/publishing.md", "docs/skills.md",
    "scripts/install.sh", "scripts/package_chatgpt_skills.py",
    "tests/test_validate_project.py",
    "styles/the-sprint.md", "styles/the-craft.md",
]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MARKDOWN_LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")


def parse_frontmatter(text: str):
    """Parse the simple name/description YAML frontmatter used by LaunchCrew skills."""
    if not text.startswith("---\n"):
        raise ValueError("must start with YAML frontmatter")
    try:
        end = text.index("\n---\n", 4)
    except ValueError as exc:
        raise ValueError("missing closing frontmatter fence") from exc
    block = text[4:end]
    values = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line!r}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in values:
            raise ValueError(f"duplicate frontmatter key: {key}")
        values[key] = value
    return values


def manifest_errors(skill_names: list[str], agent_names: list[str]) -> list[str]:
    """Return inconsistencies between manifest.json and the files present in the repo."""
    path = ROOT / "manifest.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"manifest.json: unable to read valid JSON ({exc})"]

    errors = []
    for field, actual in (("skills", skill_names), ("codex_agents", agent_names)):
        declared = manifest.get(field)
        if not isinstance(declared, list) or not all(isinstance(item, str) for item in declared):
            errors.append(f"manifest.json: {field!r} must be a list of strings")
        elif sorted(declared) != sorted(actual):
            errors.append(
                f"manifest.json: {field!r} does not match repository files "
                f"(declared {len(declared)}, found {len(actual)})"
            )

    for field, actual in (("skill_count", len(skill_names)), ("agent_count", len(agent_names))):
        if type(manifest.get(field)) is not int or manifest[field] != actual:
            errors.append(f"manifest.json: {field!r} must equal the detected count ({actual})")

    declared_styles = manifest.get("working_styles")
    actual_styles = ["styles/the-craft.md", "styles/the-sprint.md"]
    if not isinstance(declared_styles, list) or sorted(declared_styles) != actual_styles:
        errors.append("manifest.json: 'working_styles' does not match the repository files")
    return errors


def community_config_errors() -> list[str]:
    """Check contributor labels and ensure CI is configured for pull requests."""
    labels_path = ROOT / ".github" / "labels.json"
    errors = []
    try:
        labels = json.loads(labels_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f".github/labels.json: unable to read valid JSON ({exc})"]

    if not isinstance(labels, list):
        return [".github/labels.json: expected a list of label objects"]

    names = []
    for item in labels:
        if not isinstance(item, dict):
            errors.append(".github/labels.json: each label must be an object")
            continue
        name, color, description = item.get("name"), item.get("color"), item.get("description")
        if not isinstance(name, str) or not name.strip():
            errors.append(".github/labels.json: label name must be a non-empty string")
            continue
        names.append(name)
        if not isinstance(color, str) or not re.fullmatch(r"[0-9a-fA-F]{6}", color):
            errors.append(f".github/labels.json: invalid hex color for {name!r}")
        if not isinstance(description, str) or not description.strip():
            errors.append(f".github/labels.json: missing description for {name!r}")

    if len(names) != len(set(names)):
        errors.append(".github/labels.json: label names must be unique")
    required_labels = {"bug", "enhancement", "compatibility", "good first issue", "help wanted"}
    missing = sorted(required_labels - set(names))
    if missing:
        errors.append(f".github/labels.json: missing community labels: {', '.join(missing)}")

    ci_path = ROOT / ".github" / "workflows" / "ci.yml"
    if ci_path.is_file():
        ci_text = ci_path.read_text(encoding="utf-8")
        if not re.search(r"(?m)^  pull_request:\s*(?:#.*)?$", ci_text):
            errors.append(".github/workflows/ci.yml: CI must run on pull_request events")
    return errors


def broken_local_markdown_links(markdown_paths: list[Path]) -> list[str]:
    """Find missing relative file/directory links in the user-facing Markdown docs."""
    errors = []
    root = ROOT.resolve()
    for source in markdown_paths:
        if not source.is_file():
            continue
        content = source.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(content):
            target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            destination = (source.parent / unquote(parsed.path)).resolve()
            try:
                destination.relative_to(root)
            except ValueError:
                errors.append(f"{source.relative_to(ROOT)}: local link escapes repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{source.relative_to(ROOT)}: broken local link: {target}")
    return errors


def layout_errors() -> list[str]:
    """Reject duplicate legacy content paths and one-off repair utilities."""
    obsolete = [
        "scripts/styles/the-sprint.md",
        "scripts/styles/the-craft.md",
        "scripts/templates/spec/requirements.md",
        "scripts/templates/spec/design.md",
        "scripts/templates/spec/plan.md",
        "scripts/templates/spec/acceptance.md",
        "scripts/tests/test_validate_project.py",
        "apply-update.ps1",
    ]
    return [
        f"obsolete or duplicate repository path: {relative}"
        for relative in obsolete
        if (ROOT / relative).exists()
    ]


def main() -> int:
    errors = []
    for item in REQUIRED:
        if not (ROOT / item).exists():
            errors.append(f"missing required project file: {item}")

    if not SKILLS.is_dir():
        errors.append("missing .agents/skills directory")
        skill_dirs = []
    else:
        skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())

    skill_names = []
    for folder in skill_dirs:
        manifest = folder / "SKILL.md"
        if not manifest.is_file():
            errors.append(f"{folder.relative_to(ROOT)} is missing SKILL.md")
            continue
        try:
            metadata = parse_frontmatter(manifest.read_text(encoding="utf-8"))
        except ValueError as exc:
            errors.append(f"{manifest.relative_to(ROOT)}: {exc}")
            continue
        name = metadata.get("name", "")
        desc = metadata.get("description", "")
        skill_names.append(folder.name)
        if not NAME_RE.fullmatch(name):
            errors.append(f"{manifest.relative_to(ROOT)}: invalid skill name {name!r}")
        if name != folder.name:
            errors.append(f"{manifest.relative_to(ROOT)}: name {name!r} does not match folder {folder.name!r}")
        if not desc or len(desc) > 1024:
            errors.append(f"{manifest.relative_to(ROOT)}: description must be 1-1024 characters")
        if len(manifest.read_text(encoding="utf-8").splitlines()) > 500:
            errors.append(f"{manifest.relative_to(ROOT)}: SKILL.md exceeds recommended 500-line limit")

    agents_dir = ROOT / ".codex" / "agents"
    agent_files = sorted(agents_dir.glob("*.toml")) if agents_dir.is_dir() else []
    agent_names = [path.stem for path in agent_files]
    if not agent_files:
        errors.append("no Codex custom agent TOML files found")
    for path in agent_files:
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid TOML ({exc})")
            continue
        for key in ("name", "description", "developer_instructions"):
            if not isinstance(data.get(key), str) or not data[key].strip():
                errors.append(f"{path.relative_to(ROOT)}: required field {key!r} missing/empty")
        if data.get("name") and data["name"] != path.stem:
            errors.append(f"{path.relative_to(ROOT)}: name does not match filename stem")
    if len(agent_files) < 5:
        errors.append(f"expected at least 5 specialist agents; found {len(agent_files)}")

    errors.extend(manifest_errors(skill_names, agent_names))
    errors.extend(community_config_errors())
    errors.extend(layout_errors())
    markdown_to_check = [
        ROOT / "README.md", ROOT / "CONTRIBUTING.md",
        *sorted((ROOT / "docs").glob("*.md"))
    ]
    errors.extend(broken_local_markdown_links(markdown_to_check))

    if errors:
        print("LaunchCrew validation FAILED:", file=sys.stderr)
        for error in errors:
            print(f"  - {error}", file=sys.stderr)
        return 1

    print(
        f"LaunchCrew validation passed: {len(skill_names)} skills, "
        f"{len(agent_files)} Codex agents, manifest, community configuration, and local links are consistent."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
