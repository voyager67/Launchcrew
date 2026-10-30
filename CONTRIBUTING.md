# Contributing to LaunchCrew

Thanks for helping make LaunchCrew more useful, compatible, and dependable. LaunchCrew is community-improvable: you can report a problem, reproduce it, propose a fix, improve documentation, or contribute a new workflow. You do not need maintainer permission to open an issue or submit a pull request.

## Where to start

- **Bug:** use the [Bug report form](https://github.com/voyager67/Launchcrew/issues/new?template=bug_report.yml).
- **Feature idea:** use the [Feature request form](https://github.com/voyager67/Launchcrew/issues/new?template=feature_request.yml).
- **Codex / ChatGPT compatibility:** use the [Compatibility report form](https://github.com/voyager67/Launchcrew/issues/new?template=compatibility_report.yml).
- **Security vulnerability:** follow [SECURITY.md](SECURITY.md). Do not publish exploitable details in a public issue.
- **Code or documentation fix:** open a pull request using the repository template.

Search [existing issues](https://github.com/voyager67/Launchcrew/issues) and pull requests before starting. Comment on the relevant issue so others know you are investigating it. For a substantial or behavior-changing contribution, discuss the approach first to avoid duplicated work.

## Reproducing an issue

A useful report lets another person reach the same result.

1. Record the LaunchCrew release or full commit SHA.
2. Identify the affected surface: Codex CLI, ChatGPT Skills, ChatGPT Projects fallback, installer, packaging, or documentation.
3. Record relevant environment details: operating system, shell, Python version, and product version/build.
4. Follow the shortest exact sequence that triggers the issue.
5. Capture the expected and actual behavior, including relevant error output.
6. Remove secrets, API keys, personal data, private paths, proprietary prompts, and customer information before sharing logs.

For compatibility problems, include the product surface and version separately. Do not assume that behavior in Codex CLI proves behavior in ChatGPT, or vice versa. A product limitation, workspace rollout, or unavailable feature may be distinct from a LaunchCrew defect.

## Setting up a local checkout

Requirements for the repository checks: Python 3.11 or newer and a POSIX-compatible shell for the installer smoke test.

```bash
git clone https://github.com/voyager67/Launchcrew.git
cd Launchcrew
python3 --version
```

Run the validation suite before changing anything:

```bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/package_chatgpt_skills.py --check
```

The installer can be tried safely against a temporary existing directory:

```bash
tmpdir="$(mktemp -d)"
mkdir "$tmpdir/project"
./scripts/install.sh --project "$tmpdir/project"
CODEX_HOME="$tmpdir/codex" ./scripts/install.sh --global
rm -rf "$tmpdir"
```

The installer refuses to overwrite existing skill folders. Do not test collision handling against a real personal Codex skills directory unless you have backed up the content and intend to inspect the result.

## Making a change

1. Choose one focused issue or improvement. Check the existing skill catalog in [docs/skills.md](docs/skills.md) before adding another skill.
2. Create a descriptive branch, for example `fix/installer-collision-message`, `docs/chatgpt-setup`, or `feat/compatibility-check`.
3. Keep the change narrow and preserve the project's existing conventions.
4. Add or update tests for behavior changes. Fix the cause rather than weakening a test to make CI green.
5. Update README, catalog, examples, or CHANGELOG when users need to know about the change.
6. Rebuild generated ChatGPT ZIPs after changing skill source:

   ```bash
   python3 scripts/package_chatgpt_skills.py
   python3 scripts/package_chatgpt_skills.py --check
   ```

7. Run the validation commands above and inspect `git diff` before submitting.

For new skills:

- The directory name and YAML frontmatter `name` must match and use lowercase letters, digits, and hyphens.
- Keep each `SKILL.md` focused, procedural, and progressive-disclosure friendly.
- Give the skill a clear trigger, expected output, safety boundaries, and verification approach.
- Avoid hidden assumptions about model, subscription, workspace, MCP server, shell access, or permissions.
- Put provider-specific instructions in clearly marked sections and keep cross-product claims accurate.

## Submitting a pull request

1. Push your branch and open a pull request against `main`.
2. Link the issue with `Closes #123` where applicable.
3. Explain the user problem, the fix, and any compatibility or security implications.
4. Include the exact commands you ran and their results. Mark checks as skipped when they were not run and explain why.
5. Include manual test details for Codex / ChatGPT behavior changes. Do not claim a product-specific behavior was verified if you could not test it.
6. Add screenshots for UI/documentation rendering changes when they materially help review.
7. Respond to review feedback with focused commits.

GitHub Actions runs automatically on pull requests and checks skill/agent metadata, repository consistency, unit tests, installer behavior, and generated ChatGPT skill bundles. A passing CI run validates the repository checks; it does not prove that every Codex version or ChatGPT workspace supports every feature.

## Labels and first contributions

Issues labeled **good first issue** are intended as approachable entry points. **help wanted** marks work where community contributions are especially useful. Compatibility reports should identify the exact product surface and version. If an issue is missing information, help reproduce it before proposing a fix.

Maintainers may add or adjust labels as an issue is triaged. A label is an invitation, not a guarantee that a task is trivial; ask questions in the issue before investing substantial time.

## Pull request quality checklist

- [ ] The change has a clear user problem or maintenance purpose.
- [ ] Relevant tests cover the behavior and important failure cases.
- [ ] `python3 scripts/validate_project.py` passes.
- [ ] `python3 -m unittest discover -s tests -v` passes.
- [ ] `python3 scripts/package_chatgpt_skills.py --check` passes when bundles are affected.
- [ ] Installer behavior is tested when installer code changes.
- [ ] Documentation and examples match actual behavior.
- [ ] No secrets, private customer content, or unlicensed assets are included.
- [ ] Codex-only and ChatGPT-supported behavior are not conflated.

Be respectful, constructive, and specific. Small evidence-backed contributions are easier to review and merge than broad rewrites.
