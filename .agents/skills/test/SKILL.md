---
name: test
description: "Build and execute a risk-appropriate verification plan, reproduce failures, add regression coverage, and report trustworthy evidence for a change."
license: MIT
---

# Test workflow

## Procedure

1. Inspect project instructions and identify the project's actual test, lint, type-check, build, and integration commands. Do not invent commands.
2. Map each changed behavior to an existing test or a new test. Prioritize user-visible contracts and historically fragile boundaries.
3. Run the narrowest relevant test first. On failure, preserve the complete error and identify the failing layer.
4. Reproduce a failure with the smallest reliable case. Distinguish code regressions from environment/configuration problems using evidence.
5. Add regression tests for fixed bugs. Prefer stable assertions over brittle implementation-detail checks.
6. Run required quality checks; broaden to the relevant suite when feasible. If a check is unavailable or too expensive, state why and what remains unverified.
7. Inspect for flakiness, hidden network dependence, time ordering, test isolation, and cleanup leaks where relevant.
8. Report exact commands, pass/fail counts if available, failures, skipped checks, and residual risk.

## Ownership rule

A failure discovered during your work must be investigated and reported. Do not dismiss it as pre-existing without comparing baseline evidence. Fix failures within the approved scope; ask before expanding scope into a risky or unrelated rewrite.

## Output

- Tests run (exact commands)
- Result and useful evidence
- Failures / environment blockers
- Coverage gaps and remaining risks
- Recommended next action

## Guardrails

Never say “all tests pass” unless the relevant checks actually completed successfully. Do not weaken assertions, skip tests, or alter production behavior merely to obtain a green run without explaining and justifying the change.
