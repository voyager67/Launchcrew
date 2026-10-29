---
name: release-manager
description: "Prepare a dependable software release by checking scope, versioning, tests, migrations, compatibility, release notes, rollout, monitoring, and rollback readiness."
license: MIT
---

# Release management workflow

1. Identify release type, current version, intended audience, release branch/tag conventions, freeze rules, and owner.
2. Inspect the full diff since the previous release and map user-visible changes, API/schema changes, dependency updates, deprecations, and security fixes.
3. Verify required tests, builds, lint/type checks, signing/artifact steps, and release automation. Report checks that cannot run.
4. Check migrations, feature flags, data backfills, compatibility windows, config changes, secrets, and operational runbooks.
5. Draft release notes with features, fixes, breaking changes, security notes, migration steps, and known limitations. Never invent resolved issues.
6. Decide rollout strategy based on risk: staged rollout, canary, feature flag, migration order, health metrics, and rollback path.
7. Validate monitoring and the person/role responsible for halting rollout. Confirm rollback is technically possible and does not corrupt forward-only data migrations.
8. Prepare the exact proposed commands/actions and request approval before creating tags, publishing artifacts, releasing, or deploying when not explicitly authorized.
9. After release, verify artifact identity, deployed version, health signals, and user-visible behavior. Record outcome and follow-ups.

## Output

- Release readiness verdict
- Version/scope and changelog
- Test and artifact evidence
- Compatibility / migration assessment
- Rollout, monitoring, rollback plan
- Explicit approval items

## Guardrails

A release checklist is not proof of a successful deployment. Do not publish, tag, or deploy without authorization. Never hide a known critical issue in release notes.
