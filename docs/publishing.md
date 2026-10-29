# Publishing LaunchCrew to GitHub

The source package is ready to review and publish, but local preparation does not create or push a remote GitHub repository. Use this guide after reviewing the release checklist.

## Option A — GitHub CLI

Prerequisites: Git installed, GitHub CLI installed, and `gh auth login` completed. From the extracted `launchcrew/` directory:

```bash
git init -b main
git add .
git commit -m "feat: launchcrew v0.1.0"
gh repo create launchcrew --public --source=. --remote=origin --push
```

If you want a private rehearsal first, replace `--public` with `--private`; you can change visibility later. This command creates a new `launchcrew` repository under the authenticated GitHub account and pushes the current local commit. Check the target account before running it.

## Option B — GitHub website

1. Create a repository named `launchcrew` under the intended account.
2. Do **not** initialize it with a README, license, or `.gitignore`, because this package already contains them.
3. In the extracted package directory, run:

   ```bash
   git init -b main
   git add .
   git commit -m "feat: launchcrew v0.1.0"
   git remote add origin https://github.com/ACCOUNT/launchcrew.git
   git push -u origin main
   ```

4. Replace `ACCOUNT` with the account that owns the new repository.
5. Verify the Actions run and the badge in `README.md`. The included CI checks this repository's package; it does not validate your application code.

## After the first push

- Add topics from `REPOSITORY-METADATA.md` and paste its description into the About panel.
- Review branch protections and enable secret scanning/dependency alerts where appropriate.
- Check the open issue templates render correctly.
- Use the [`RELEASE-CHECKLIST.md`](../RELEASE-CHECKLIST.md) before tagging a release.
- Don't claim ChatGPT skill upload was tested unless you test it in an account where the Skills UI is available.
