from pathlib import Path
import importlib.util
import unittest
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('validate_project', ROOT / 'scripts' / 'validate_project.py')
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class FrontmatterTests(unittest.TestCase):
    def test_valid_frontmatter(self):
        parsed = module.parse_frontmatter('---\nname: demo-skill\ndescription: "Do a useful thing."\n---\n\nInstructions\n')
        self.assertEqual(parsed['name'], 'demo-skill')
        self.assertEqual(parsed['description'], 'Do a useful thing.')

    def test_missing_closing_fence_fails(self):
        with self.assertRaises(ValueError):
            module.parse_frontmatter('---\nname: demo-skill\ndescription: "missing fence"\n')

    def test_missing_frontmatter_fails(self):
        with self.assertRaises(ValueError):
            module.parse_frontmatter('# No metadata')


class RepositoryAssetTests(unittest.TestCase):
    def test_skill_names_match_directories_and_are_unique(self):
        skill_files = sorted((ROOT / '.agents' / 'skills').glob('*/SKILL.md'))
        self.assertGreaterEqual(len(skill_files), 20)
        names = []
        for skill_file in skill_files:
            metadata = module.parse_frontmatter(skill_file.read_text(encoding='utf-8'))
            names.append(metadata['name'])
            self.assertEqual(metadata['name'], skill_file.parent.name)
            self.assertTrue(metadata.get('description'))
            self.assertLessEqual(len(metadata['description']), 1024)
            self.assertRegex(metadata['name'], r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
        self.assertEqual(len(names), len(set(names)))

    def test_working_style_profiles_exist_and_keep_quality_guardrails(self):
        for relative in ('styles/the-sprint.md', 'styles/the-craft.md'):
            content = (ROOT / relative).read_text(encoding='utf-8')
            self.assertIn('## Non-negotiables', content)
            self.assertIn('test', content.lower())
            self.assertIn('evidence', content.lower())

    def test_each_chatgpt_bundle_contains_one_skill_manifest(self):
        skills_dir = ROOT / '.agents' / 'skills'
        bundles = ROOT / 'dist' / 'chatgpt-skills'
        skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
        self.assertEqual({p.stem for p in bundles.glob('*.zip')}, {p.name for p in skill_dirs})
        for skill_dir in skill_dirs:
            archive = bundles / f'{skill_dir.name}.zip'
            with zipfile.ZipFile(archive) as zf:
                entries = zf.namelist()
                self.assertIn(f'{skill_dir.name}/SKILL.md', entries)
                manifests = [entry for entry in entries if entry.lower().endswith('skill.md')]
                self.assertEqual(len(manifests), 1)
                self.assertIsNone(zf.testzip())


if __name__ == '__main__':
    unittest.main()
