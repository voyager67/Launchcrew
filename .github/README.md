# GitHub automation

CI validates the skill metadata, TOML agent definitions, required documentation, unit tests, and generated ChatGPT ZIP archives. It does not execute an application test suite because LaunchCrew is primarily an instruction and tooling repository.

Before publishing the first release, push the repository to the expected `main` branch and check the CI badge in the README. If the repository's default branch differs, update the workflow trigger and badge URL accordingly.
