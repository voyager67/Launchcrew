## Summary

<!-- What changed? Describe the user-visible behavior or workflow improvement. -->

## Related issue

<!-- Link the issue this addresses, e.g. Closes #123. For standalone maintenance work, explain why it is needed. -->

## Implementation

<!-- Describe the approach, important trade-offs, and any files or workflows affected. -->

## Verification evidence

List the exact commands you ran and paste the relevant output. Do not tick a check that you did not run.

- [ ] `python3 scripts/validate_project.py`
- [ ] `python3 -m unittest discover -s tests -v`
- [ ] `python3 scripts/package_chatgpt_skills.py --check`
- [ ] Installer smoke test (project/global, when installer behavior changed)
- [ ] Manual product test (when Codex / ChatGPT behavior changed)

**Commands and results**

```text
<!-- Exact command(s), pass/fail result, and relevant output. -->
```

**Environment**

<!-- OS, Python, Codex CLI / ChatGPT surface and version, where relevant. -->

## Risk and compatibility

- [ ] No credentials, private customer data, or confidential prompts added.
- [ ] Codex-specific and ChatGPT-compatible behavior are clearly distinguished.
- [ ] Existing user skill/config files are not silently overwritten.
- [ ] Documentation, examples, and changelog are updated where needed.
- [ ] Limitations and unverified product-specific behavior are stated honestly.

## Screenshots / additional context

<!-- Optional. Add before/after screenshots for UI changes; redact sensitive content. -->
