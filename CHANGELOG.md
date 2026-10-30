# Changelog

All notable changes are documented here. This project follows a lightweight Keep a Changelog format and uses semantic versioning where releases are tagged.

## [Unreleased]

### Fixed
- Restored release and repository-maintainer reference documents that were present in the original project package.
- Removed duplicate legacy copies of styles, spec templates, and tests from under `scripts/`, plus an obsolete self-removing repair helper.
- Added layout regression checks so the duplicate paths cannot silently return.

### Changed
- Clarified that ChatGPT Skills upload access depends on account/workspace enablement and current rollout.
- Added a downloadable source snapshot to successful main-branch CI runs.

### Added
- Dedicated Codex / ChatGPT compatibility issue form and issue chooser.
- Community label catalog and automated GitHub label synchronization, including good first issue and help wanted.
- Contributor guidance for reproduction, local validation, and evidence-backed pull requests.

### Changed
- Expanded bug and feature report forms to collect reproducible evidence.
- Pull request template now requests exact test output and product-environment details.
- CI runs on pull requests with repository validation, unit tests, installer smoke tests, and bundle verification.

## [0.1.0] - 2026-10-29

### Added
- Initial LaunchCrew skill library with 23 portable `SKILL.md` workflows.
- Ten project-scoped Codex specialist agents and example multi-agent configuration.
- Codex installation and ChatGPT skill-bundle packaging scripts.
- Validator, unit tests, CI workflow, setup guides, governance docs, and launch assets.
- Spec-first workflow artifacts, starter templates, and safety boundaries.
