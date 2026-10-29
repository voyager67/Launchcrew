## What changed?

<!-- Summarize the user-visible behavior or workflow improvement. -->

## Why?

<!-- Link the issue or concrete use case. -->

## Validation

- [ ] `python3 scripts/validate_project.py`
- [ ] `python3 -m unittest discover -s tests -v`
- [ ] `python3 scripts/package_chatgpt_skills.py --check`

## Safety / compatibility

- [ ] No credentials, private customer data, or unlicensed assets added.
- [ ] ChatGPT and Codex support claims are accurate and clearly separated.
- [ ] Existing user skill/config files will not be silently overwritten.
