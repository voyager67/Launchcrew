# Publishing a LaunchCrew copy

The canonical LaunchCrew repository is already public at [github.com/voyager67/Launchcrew](https://github.com/voyager67/Launchcrew). Use this guide when publishing a fork, customized copy, or independent derivative under your own GitHub account.

## Before publishing

1. Review the project name, description, license, and any changes you made.
2. Keep the README's compatibility statements accurate; Codex-specific agents and configuration are not ChatGPT Skills.
3. Run the local validation commands from the repository root:

   ```bash
   python3 scripts/validate_project.py
   python3 -m unittest discover -s tests -v
   python3 scripts/package_chatgpt_skills.py --check
   ```

## Option A — GitHub CLI

Prerequisites: Git installed, GitHub CLI installed, and `gh auth login` completed. From your prepared copy:

```bash
git init -b main
git add .
git commit -m "feat: publish LaunchCrew-based workflow kit"
gh repo create launchcrew --public --source=. --remote=origin --push
```

The command creates a repository named `launchcrew` under the authenticated GitHub account. Change the repository name or visibility deliberately before running it.

## Option B — GitHub website

1. Create a repository under the intended account. Do not initialize it with a README, license, or `.gitignore`; this project already contains those files.
2. From the prepared copy, run:

   ```bash
   git init -b main
   git add .
   git commit -m "feat: publish LaunchCrew-based workflow kit"
   git remote add origin https://github.com/ACCOUNT/REPOSITORY.git
   git push -u origin main
   ```

3. Replace `ACCOUNT/REPOSITORY` with the new repository's owner and name.
4. Verify the Actions run and CI badge.

## After the first push

- Add a concise repository description, such as: "A startup-team workflow kit for Codex CLI and ChatGPT-compatible portable skills."
- Consider focused topics such as `codex`, `codex-cli`, `chatgpt`, `agent-skills`, `ai-agents`, `spec-driven-development`, `developer-tools`, and `open-source`.
- Review branch protection, issue templates, and available security settings.
- Update [`CHANGELOG.md`](../CHANGELOG.md) for user-visible changes before tagging a release.
- Do not claim Codex clean-clone validation or ChatGPT Skills upload was tested unless you perform those checks in the corresponding environments.

The included GitHub Actions workflow validates this repository's skill metadata, agent configuration, documentation links, tests, and generated skill bundles. It does not validate a target application's source code or grant ChatGPT/Codex features that are not enabled for the user.
