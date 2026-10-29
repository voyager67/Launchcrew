#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/.agents/skills"
MODE="${1:-}"

if [[ ! -d "$SOURCE" ]]; then
  echo "Error: skill source directory not found: $SOURCE" >&2
  exit 1
fi

copy_skills() {
  local destination="$1"
  mkdir -p "$destination"
  local collisions=()
  while IFS= read -r -d '' skill_dir; do
    local name
    name="$(basename "$skill_dir")"
    if [[ -e "$destination/$name" ]]; then
      collisions+=("$name")
    fi
  done < <(find "$SOURCE" -mindepth 1 -maxdepth 1 -type d -print0)

  if (( ${#collisions[@]} > 0 )); then
    echo "Refusing to overwrite existing skill folder(s) in $destination:" >&2
    printf '  - %s\n' "${collisions[@]}" >&2
    echo "Review and merge collisions manually, or choose another destination." >&2
    return 2
  fi

  while IFS= read -r -d '' skill_dir; do
    cp -R "$skill_dir" "$destination/"
  done < <(find "$SOURCE" -mindepth 1 -maxdepth 1 -type d -print0)
  echo "Installed $(find "$SOURCE" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ') skills into $destination"
}

case "$MODE" in
  --project)
    if [[ $# -ne 2 || -z "${2:-}" ]]; then
      echo "Usage: $0 --project /path/to/project" >&2
      exit 2
    fi
    TARGET="$(cd "$2" 2>/dev/null && pwd)" || { echo "Project path must already exist: $2" >&2; exit 2; }
    copy_skills "$TARGET/.agents/skills"
    ;;
  --global)
    if [[ $# -ne 1 ]]; then
      echo "Usage: $0 --global" >&2
      exit 2
    fi
    CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
    copy_skills "$CODEX_HOME/skills"
    ;;
  --chatgpt)
    python3 "$ROOT/scripts/package_chatgpt_skills.py"
    ;;
  *)
    cat <<'USAGE'
LaunchCrew installer

Usage:
  ./scripts/install.sh --project /path/to/existing-project
  ./scripts/install.sh --global
  ./scripts/install.sh --chatgpt

The installer never overwrites an existing skill folder.
USAGE
    exit 2
    ;;
esac
