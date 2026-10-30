from pathlib import Path
import importlib.util
import json
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]

VALIDATOR_SPEC = importlib.util.spec_from_file_location(
    "validate_project", ROOT / "scripts" / "validate_project.py"
)
validator = importlib.util.module_from_spec(VALIDATOR_SPEC)
VALIDATOR_SPEC.loader.exec_module(validator)

PACKAGE_SPEC = importlib.util.spec_from_file_location(
    "package_chatgpt_skills", ROOT / "scripts" / "package_chatgpt_skills.py"
)
package = importlib.util.module_from_spec(PACKAGE_SPEC)
PACKAGE_SPEC.loader.exec_module(package)


class FrontmatterTests(unittest.TestCase):
    def test_valid_frontmatter(self):
        parsed = validator.parse_frontmatter(
            '---\nname: demo-skill\ndescription: "Do a useful thing."\n---\n\nInstructions\n'
        )
        self.assertEqual(parsed["name"], "demo-skill")
        self.assertEqual(parsed["description"], "Do a useful thing.")

    def test_missing_closing_fence_fails(self):
        with self.assertRaises(ValueError):
            validator.parse_frontmatter(
                '---\nname: demo-skill\ndescription: "missing fence"\n'
            )

    def test_missing_frontmatter_fails(self):
        with self.assertRaises(ValueError):
            validator.parse_frontmatter("# No metadata")


class RepositoryAssetTests(unittest.TestCase):
    def test_skill_names_match_directories_and_are_unique(self):
        skill_files = sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md"))
        self.assertGreaterEqual(len(skill_files), 20)
        names = []
        for skill_file in skill_files:
            metadata = validator.parse_frontmatter(skill_file.read_text(encoding="utf-8"))
            names.append(metadata["name"])
            self.assertEqual(metadata["name"], skill_file.parent.name)
            self.assertTrue(metadata.get("description"))
            self.assertLessEqual(len(metadata["description"]), 1024)
            self.assertRegex(metadata["name"], r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertEqual(len(names), len(set(names)))

    def test_manifest_matches_repository_assets(self):
        skill_names = sorted(path.name for path in (ROOT / ".agents" / "skills").iterdir() if path.is_dir())
        agent_names = sorted(path.stem for path in (ROOT / ".codex" / "agents").glob("*.toml"))
        self.assertEqual(validator.manifest_errors(skill_names, agent_names), [])

    def test_community_labels_and_pr_ci_are_configured(self):
        self.assertEqual(validator.community_config_errors(), [])
        labels = json.loads((ROOT / ".github" / "labels.json").read_text(encoding="utf-8"))
        names = {label["name"] for label in labels}
        self.assertIn("good first issue", names)
        self.assertIn("help wanted", names)
        self.assertIn("compatibility", names)

    def test_compatibility_issue_form_covers_both_product_surfaces(self):
        form = (ROOT / ".github" / "ISSUE_TEMPLATE" / "compatibility_report.yml").read_text(encoding="utf-8")
        self.assertIn("Codex CLI", form)
        self.assertIn("ChatGPT Skills", form)
        self.assertIn("product_version", form)
        self.assertIn("Exact steps to reproduce", form)

    def test_user_facing_markdown_has_no_broken_local_links(self):
        markdown_files = [
            ROOT / "README.md", ROOT / "CONTRIBUTING.md",
            *sorted((ROOT / "docs").glob("*.md"))
        ]
        self.assertEqual(validator.broken_local_markdown_links(markdown_files), [])

    def test_working_style_profiles_exist_and_keep_quality_guardrails(self):
        for relative in ("styles/the-sprint.md", "styles/the-craft.md"):
            content = (ROOT / relative).read_text(encoding="utf-8")
            self.assertIn("## Non-negotiables", content)
            self.assertIn("test", content.lower())
            self.assertIn("evidence", content.lower())

    def test_each_chatgpt_bundle_matches_its_source(self):
        skills_dir = ROOT / ".agents" / "skills"
        bundles = ROOT / "dist" / "chatgpt-skills"
        skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
        self.assertEqual({path.stem for path in bundles.glob("*.zip")}, {path.name for path in skill_dirs})
        for skill_dir in skill_dirs:
            archive = bundles / f"{skill_dir.name}.zip"
            valid, reason = package.validate_archive(skill_dir, archive)
            self.assertTrue(valid, reason)

    def test_stale_chatgpt_bundle_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            skill_dir = root / "demo-skill"
            skill_dir.mkdir()
            (skill_dir / "SKILL.md").write_text("current source", encoding="utf-8")
            archive = root / "demo-skill.zip"
            with zipfile.ZipFile(archive, "w") as zf:
                zf.writestr("demo-skill/SKILL.md", "outdated source")
            valid, reason = package.validate_archive(skill_dir, archive)
            self.assertFalse(valid)
            self.assertIn("Stale bundle", reason)


    def test_maintainer_and_release_documents_exist(self):
        for relative in (
            ".github/README.md",
            "RELEASE-CHECKLIST.md",
            "REPOSITORY-METADATA.md",
            "ROADMAP.md",
        ):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_legacy_duplicate_paths_are_absent(self):
        self.assertEqual(validator.layout_errors(), [])


if __name__ == "__main__":
    unittest.main()
