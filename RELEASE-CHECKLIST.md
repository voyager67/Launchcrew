# LaunchCrew release checklist

Use this checklist before publishing a new release or creating a version tag.

## Repository and contents

- [ ] Confirm the release version and update `CHANGELOG.md`.
- [ ] Confirm `README.md`, `manifest.json`, the skill catalog, and agent count match the shipped files.
- [ ] Review the MIT license, contribution guide, security policy, and community templates.
- [ ] Confirm the repository banner, About description, topics, and CI badge point to the canonical repository.
- [ ] Inspect generated ChatGPT ZIPs; each archive should contain one top-level skill folder and one `SKILL.md`.

## Automated validation

Run from the repository root:

```bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/package_chatgpt_skills.py --check
```

- [ ] All three commands pass.
- [ ] The latest GitHub Actions validation run is green.
- [ ] Review the final diff and confirm there are no secrets, temporary files, duplicate legacy paths, or unrelated changes.

## Product-specific manual checks

- [ ] Test a clean clone with the supported Codex CLI version.
- [ ] Verify repository-local skill discovery and the optional custom-agent setup.
- [ ] Test the project/global installer in a disposable directory, including collision refusal.
- [ ] Where a ChatGPT Skills-enabled workspace is available, upload one ZIP and verify the skill can be selected.
- [ ] Verify the ChatGPT Projects fallback instructions independently.

Record the product versions, environment, commands, and observed results. Mark checks as not tested when the necessary product/account environment is unavailable; do not infer a successful UI test from passing CI.

## Publish

- [ ] Create or update the GitHub release notes from `CHANGELOG.md`.
- [ ] Attach the source archive or link to the corresponding GitHub source snapshot.
- [ ] Verify the release page, README badges, and issue links after publication.
- [ ] Prepare any launch messages for the target community and follow its self-promotion rules.
