# GitHub repository automation

This directory contains the issue forms, pull request template, label catalog, and GitHub Actions workflows used by LaunchCrew.

## Issue and pull request templates

- `ISSUE_TEMPLATE/bug_report.yml` collects reproducible defect reports.
- `ISSUE_TEMPLATE/feature_request.yml` focuses proposals on a user problem and desired outcome.
- `ISSUE_TEMPLATE/compatibility_report.yml` separates Codex CLI, ChatGPT Skills, and Projects compatibility reports.
- `ISSUE_TEMPLATE/config.yml` configures the issue chooser and private security-reporting guidance.
- `pull_request_template.md` asks contributors for implementation details, test evidence, and compatibility notes.

Never include credentials, private prompts, private repository contents, or customer data in public reports.

## Workflows

- `workflows/ci.yml` validates skill metadata, Codex agent TOML, docs and repository layout; runs unit tests; smoke-tests the installer; verifies generated ChatGPT skill ZIPs; and publishes a downloadable source snapshot for successful pushes to `main`.
- `workflows/sync-labels.yml` creates or updates the labels listed in `labels.json` when the catalog changes on `main`.

The label-sync workflow needs the repository's standard GitHub Actions token with `issues: write`. Keep workflow permissions scoped to the minimum required.

## Maintaining these files

Update the relevant validator and tests whenever repository structure or community automation changes. Run:

```bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/package_chatgpt_skills.py --check
```
