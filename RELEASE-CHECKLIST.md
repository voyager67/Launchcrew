# First public release checklist

- [ ] Confirm repository name and public URL (`voyager67/launchcrew` is used in badges/links).
- [ ] Confirm the default branch is `main`; update badge and workflow triggers otherwise.
- [ ] Review project name/trademark conflicts and choose a final GitHub description.
- [ ] Run `python3 scripts/validate_project.py`.
- [ ] Run `python3 -m unittest discover -s tests -v`.
- [ ] Run `python3 scripts/package_chatgpt_skills.py --check`.
- [ ] Inspect install script and generated ZIP contents.
- [ ] Test a clean clone in Codex CLI.
- [ ] Test uploading one generated skill ZIP in a ChatGPT account/workspace where Skills are available, and verify the Projects fallback.
- [ ] Ensure CI passes after pushing.
- [ ] Create the first release/tag only after all available checks pass.
- [ ] Verify README badges render and issue links work.
- [ ] Customize launch drafts and follow each target community's self-promotion policy.

The launch checklist intentionally distinguishes tasks that can be tested locally from tasks requiring an actual GitHub push or product-account UI. A local package cannot honestly claim those external checks already passed.
