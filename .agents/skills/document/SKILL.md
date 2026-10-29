---
name: document
description: "Create or update accurate project documentation from actual code, tests, interfaces, and decisions; keep onboarding, API behavior, examples, and release notes synchronized."
license: MIT
---

# Documentation workflow

1. Identify the audience and job: setup, usage, contributor onboarding, API reference, architecture, operation, or release.
2. Inspect source and tests as the source of truth. For version-sensitive external behavior, verify against current official documentation and include links.
3. Write the shortest complete path to success first. Include prerequisites, copy-pasteable commands, expected output, and common failure recovery.
4. For APIs, document inputs, outputs, errors, auth, compatibility, limits, and example usage. Verify examples against code/tests where feasible.
5. For architecture, explain boundaries, data flow, decisions, and trade-offs rather than restating filenames.
6. Update only the relevant documents. Use relative links and check that referenced files/commands exist.
7. For changed behavior, add a changelog note or migration note if users need to act.
8. Report any example that could not be executed and any behavior that remains uncertain.

## Deliverables by document type

- README: problem, value, install, quick start, capabilities, limitations, contribution.
- API docs: real contract plus failure behavior and examples.
- ADR: context, decision, alternatives, consequences, revisit conditions.
- Changelog: user-visible changes grouped by type and release.
- Runbook: alert/trigger, checks, safe mitigation, escalation, recovery verification.

## Guardrails

Do not document intended behavior as implemented behavior without proof. Avoid absolute compatibility promises, unsupported performance claims, or hidden assumptions about credentials and tools.
