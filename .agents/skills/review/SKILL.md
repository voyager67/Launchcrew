---
name: review
description: "Independently review a diff or proposed implementation for correctness, security, regressions, performance, accessibility, and missing tests; return prioritized findings with evidence."
license: MIT
---

# Review workflow

## Mode

Default to read-only review. Do not edit files unless the user explicitly changes the task from review to remediation.

## Procedure

1. Establish the review base and inspect the complete diff plus the relevant surrounding code and tests.
2. Reconstruct the intended behavior from the spec/issue. If no acceptance criteria exist, state the inferred contract.
3. Prioritize: data loss/security boundary violations; correctness regressions; broken error handling; missing critical test coverage; performance/accessibility risks; maintainability concerns.
4. Trace effects across callers, interfaces, schemas, migrations, caches, retries, authorization, async behavior, and configuration as applicable.
5. Check whether tests can fail while implementation is broken. Look for false positives, missing negative cases, and untested error paths.
6. Use specialist perspectives only when the diff warrants them (e.g., security for auth changes; accessibility for UI changes; concurrency for async code).
7. Verify each finding against source and cite file/line or exact symbol. Distinguish confirmed bugs from hypotheses.
8. Do not spend findings budget on style-only preferences unless they obscure correctness or increase meaningful risk.

## Output format

Findings first, sorted by severity. Each finding includes severity, location, failure scenario, user/system impact, and concrete remediation. Then list questions, testing gaps, positive observations only when helpful, and an overall disposition: approve, approve with follow-up, or changes requested.

## Guardrails

A clean review means no material issues were found within the reviewed scope; it is not proof that the system is bug-free. State inaccessible areas and missing test/evidence limitations.
