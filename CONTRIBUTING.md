# Contributing to LaunchCrew

Thanks for helping make repeatable AI workflows safer and more useful.

## Before opening an issue

Search existing issues and explain the concrete workflow, the current failure or friction, the expected result, and how to reproduce it. Avoid sharing credentials, private source, personal data, or proprietary prompts.

## Before proposing a new skill

1. Check `docs/skills.md` for an existing skill with the same job.
2. Define an unmistakable trigger and a single primary output.
3. Keep `SKILL.md` procedural and reasonably short; use `references/`, `scripts/`, and `assets/` only when they materially help.
4. Include boundaries, uncertainty handling, and a way to verify the result.
5. Ensure it works without hidden assumptions about a model, plan, MCP server, or shell tool.

## Pull request checklist

- [ ] The skill's `name` matches its folder and uses lowercase letters, digits, and hyphens.
- [ ] The description accurately explains what the skill does and when to use it.
- [ ] Provider-specific steps are clearly labeled.
- [ ] No secret, personal data, external customer content, or unlicensed asset is included.
- [ ] `python3 scripts/validate_project.py` passes.
- [ ] `python3 -m unittest discover -s tests -v` passes.
- [ ] README/catalog/launch docs reflect meaningful new skills or behavior.
- [ ] Claims are verifiable and do not inflate compatibility or test coverage.

## Review style

Small focused pull requests are easier to verify. Prefer specific edits and evidence over broad rewrites. Maintainers may request narrower scope or additional validation when a change affects installation, safety, or compatibility.
