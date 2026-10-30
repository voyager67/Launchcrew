#!/usr/bin/env python3
"""Create and verify one upload-ready ZIP per portable LaunchCrew skill."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
OUT = ROOT / "dist" / "chatgpt-skills"


def validate_archive(folder: Path, archive: Path) -> tuple[bool, str]:
    """Check archive integrity, layout, and byte-for-byte parity with the source skill."""
    expected = {
        (Path(folder.name) / path.relative_to(folder)).as_posix(): path
        for path in folder.rglob("*")
        if path.is_file() and path.name not in {".DS_Store"}
    }
    try:
        with zipfile.ZipFile(archive) as zf:
            names = [name for name in zf.namelist() if not name.endswith("/")]
            if len(names) != len(set(names)):
                return False, f"Duplicate entries in archive: {archive.name}"
            if set(names) != set(expected):
                return False, (
                    f"Archive file set mismatch in {archive.name}. "
                    f"Expected {sorted(expected)}, found {sorted(names)}"
                )
            corrupt_file = zf.testzip()
            if corrupt_file is not None:
                return False, f"Corrupt archive {archive.name}: {corrupt_file}"
            for name, source in expected.items():
                if zf.read(name) != source.read_bytes():
                    return False, f"Stale bundle: {archive.name} does not match {source.relative_to(folder.parent)}"
    except (OSError, zipfile.BadZipFile, KeyError) as exc:
        return False, f"Invalid ZIP {archive.name}: {exc}"
    return True, ""


def build(check: bool = False) -> int:
    if not SKILLS.is_dir():
        print(f"Skill source directory not found: {SKILLS}", file=sys.stderr)
        return 2
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not skill_dirs:
        print(f"No skills found under {SKILLS}", file=sys.stderr)
        return 2

    expected = set()
    if not check:
        OUT.mkdir(parents=True, exist_ok=True)

    for folder in skill_dirs:
        manifest = folder / "SKILL.md"
        if not manifest.is_file():
            print(f"Missing SKILL.md: {folder}", file=sys.stderr)
            return 2
        archive = OUT / f"{folder.name}.zip"
        expected.add(archive.name)
        if check:
            if not archive.is_file():
                print(f"Missing generated archive: {archive.relative_to(ROOT)}", file=sys.stderr)
                return 1
            valid, reason = validate_archive(folder, archive)
            if not valid:
                print(reason, file=sys.stderr)
                return 1
            continue

        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for path in sorted(folder.rglob("*")):
                if path.is_file() and path.name not in {".DS_Store"}:
                    zf.write(path, (Path(folder.name) / path.relative_to(folder)).as_posix())
        print(f"created {archive.relative_to(ROOT)}")

    if check:
        current = {p.name for p in OUT.glob("*.zip")}
        if current != expected:
            print(
                f"Archive set mismatch. Expected {sorted(expected)}, found {sorted(current)}",
                file=sys.stderr,
            )
            return 1
        print(f"Validated {len(expected)} ChatGPT skill archives against their source files.")
    else:
        print(f"Packaged {len(expected)} skills into {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="verify existing archives without modifying them")
    args = parser.parse_args()
    raise SystemExit(build(check=args.check))
