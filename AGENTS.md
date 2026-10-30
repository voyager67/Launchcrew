# LaunchCrew repository guidance

## Project goal

Maintain a practical, portable set of reusable skills and Codex project-scoped agents for evidence-first product and software delivery. Keep ChatGPT compatibility explicit and honest; do not claim Codex-only configuration is directly importable into ChatGPT.

## Working principles

- Read only the files relevant to the requested change. Do not load the whole repository for a narrow edit.
- For new workflows, use `$specify` when the change has multiple requirements, components, or meaningful risks. Use direct implementation for small changes.
- Use `$validate` before implementing a complex spec; use `$test` for changes to scripts, validation, packaging, metadata, or workflow behavior; use `$review` before release-quality changes.
- Keep skill names and directory names aligned. Each skill must have a valid `SKILL.md` with concise YAML frontmatter (`name`, `description`) and a narrowly scoped trigger.
- Keep skills procedural, evidence-based, and progressive-disclosure friendly. Move long reference material to `references/` instead of bloating `SKILL.md`.
- Use `$research-brief` for current or version-sensitive claims. Prefer official documentation and date the verification.
- Prefer deterministic checks for things that can be validated mechanically; do not imply a check was run if it was not.
- Do not fabricate sources, results, test runs, benchmark numbers, customer feedback, or claims of adoption.
- Avoid overwriting a user's existing skill, config, or project instructions. Installer operations must fail safely on collisions.
- Do not introduce provider-specific API assumptions into portable skills unless clearly labeled and documented.

## Change safety

- Avoid unrequested dependencies and generated binary artifacts unless they improve the release experience.
- Before changing release, installer, security, or packaging behavior, inspect its callers and tests.
- Never store API keys, tokens, personal data, or actual customer secrets in this repository.
- Ask for explicit approval before destructive operations, deployment, external messages, permission changes, or material cost-incurring actions.

## Validation commands

```bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/package_chatgpt_skills.py --check
```

## Review expectations

Prioritize broken skill metadata, invalid TOML, unsafe install behavior, broken links, mismatched claims in docs, misleading compatibility statements, and missing test coverage. Report concrete findings with file paths and reproduction steps.
