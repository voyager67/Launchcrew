#!/usr/bin/env python3
"""Validate LaunchCrew skill frontmatter, Codex agents, and release files."""
from __future__ import annotations
from pathlib import Path
import re
import sys
import tomllib

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents' / 'skills'
REQUIRED = [
    'README.md', 'AGENTS.md', 'LICENSE', 'CONTRIBUTING.md', 'SECURITY.md',
    'CODE_OF_CONDUCT.md', 'CHANGELOG.md', 'ROADMAP.md', 'docs/codex.md',
    'docs/chatgpt.md', 'docs/publishing.md', 'REPOSITORY-METADATA.md', 'scripts/install.sh', 'scripts/package_chatgpt_skills.py',
    'styles/the-sprint.md', 'styles/the-craft.md',
]
NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')


def parse_frontmatter(text: str):
    if not text.startswith('---\n'):
        raise ValueError('must start with YAML frontmatter')
    try:
        end = text.index('\n---\n', 4)
    except ValueError as exc:
        raise ValueError('missing closing frontmatter fence') from exc
    block = text[4:end]
    values = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if ':' not in line:
            raise ValueError(f'invalid frontmatter line: {line!r}')
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key in values:
            raise ValueError(f'duplicate frontmatter key: {key}')
        values[key] = value
    return values


def main() -> int:
    errors = []
    for item in REQUIRED:
        if not (ROOT / item).exists():
            errors.append(f'missing required release file: {item}')
    if not SKILLS.is_dir():
        errors.append('missing .agents/skills directory')
    else:
        skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
        for folder in skill_dirs:
            manifest = folder / 'SKILL.md'
            if not manifest.is_file():
                errors.append(f'{folder.relative_to(ROOT)} is missing SKILL.md')
                continue
            try:
                metadata = parse_frontmatter(manifest.read_text(encoding='utf-8'))
            except ValueError as exc:
                errors.append(f'{manifest.relative_to(ROOT)}: {exc}')
                continue
            name = metadata.get('name', '')
            desc = metadata.get('description', '')
            if not NAME_RE.fullmatch(name):
                errors.append(f'{manifest.relative_to(ROOT)}: invalid skill name {name!r}')
            if name != folder.name:
                errors.append(f'{manifest.relative_to(ROOT)}: name {name!r} does not match folder {folder.name!r}')
            if not desc or len(desc) > 1024:
                errors.append(f'{manifest.relative_to(ROOT)}: description must be 1-1024 characters')
            if len(manifest.read_text(encoding='utf-8').splitlines()) > 500:
                errors.append(f'{manifest.relative_to(ROOT)}: SKILL.md exceeds recommended 500-line limit')
    agents_dir = ROOT / '.codex' / 'agents'
    agent_files = sorted(agents_dir.glob('*.toml'))
    if not agent_files:
        errors.append('no Codex custom agent TOML files found')
    for path in agent_files:
        try:
            data = tomllib.loads(path.read_text(encoding='utf-8'))
        except Exception as exc:
            errors.append(f'{path.relative_to(ROOT)}: invalid TOML ({exc})')
            continue
        for key in ('name', 'description', 'developer_instructions'):
            if not isinstance(data.get(key), str) or not data[key].strip():
                errors.append(f'{path.relative_to(ROOT)}: required field {key!r} missing/empty')
        if data.get('name') and data['name'] != path.stem:
            errors.append(f'{path.relative_to(ROOT)}: name does not match filename stem')
    if len(agent_files) < 5:
        errors.append(f'expected at least 5 specialist agents; found {len(agent_files)}')
    if errors:
        print('LaunchCrew validation FAILED:', file=sys.stderr)
        for error in errors:
            print(f'  - {error}', file=sys.stderr)
        return 1
    print(f'LaunchCrew validation passed: {len(list(SKILLS.glob("*/SKILL.md")))} skills, {len(agent_files)} Codex agents, required docs present.')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
