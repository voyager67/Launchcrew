#!/usr/bin/env python3
"""Create one upload-ready ZIP per portable LaunchCrew skill."""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents' / 'skills'
OUT = ROOT / 'dist' / 'chatgpt-skills'


def build(check: bool = False) -> int:
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not skill_dirs:
        print(f'No skills found under {SKILLS}', file=sys.stderr)
        return 2
    expected = set()
    if not check:
        OUT.mkdir(parents=True, exist_ok=True)
    for folder in skill_dirs:
        manifest = folder / 'SKILL.md'
        if not manifest.is_file():
            print(f'Missing SKILL.md: {folder}', file=sys.stderr)
            return 2
        archive = OUT / f'{folder.name}.zip'
        expected.add(archive.name)
        if check:
            if not archive.is_file():
                print(f'Missing generated archive: {archive.relative_to(ROOT)}', file=sys.stderr)
                return 1
            try:
                with zipfile.ZipFile(archive) as zf:
                    names = zf.namelist()
                    if f'{folder.name}/SKILL.md' not in names:
                        print(f'Invalid archive layout: {archive.name}', file=sys.stderr)
                        return 1
                    if zf.testzip() is not None:
                        print(f'Corrupt archive: {archive.name}', file=sys.stderr)
                        return 1
            except zipfile.BadZipFile:
                print(f'Invalid ZIP: {archive.name}', file=sys.stderr)
                return 1
            continue
        with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for path in sorted(folder.rglob('*')):
                if path.is_file() and path.name not in {'.DS_Store'}:
                    zf.write(path, path.relative_to(SKILLS).as_posix())
        print(f'created {archive.relative_to(ROOT)}')
    if check:
        current = {p.name for p in OUT.glob('*.zip')}
        if current != expected:
            print(f'Archive set mismatch. Expected {sorted(expected)}, found {sorted(current)}', file=sys.stderr)
            return 1
        print(f'Validated {len(expected)} ChatGPT skill archives.')
    else:
        print(f'Packaged {len(expected)} skills into {OUT.relative_to(ROOT)}/')
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='validate existing archives without modifying them')
    args = parser.parse_args()
    raise SystemExit(build(check=args.check))
