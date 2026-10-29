---
name: refactor
description: "Improve code structure, duplication, naming, boundaries, or maintainability while preserving externally observable behavior and verifying equivalence."
license: MIT
---

# Refactor workflow

1. State the desired structural improvement and the behavior that must not change.
2. Inspect callers, interfaces, tests, error semantics, data shape, timing, logging, and configuration around the target.
3. Establish a baseline: relevant tests and, where meaningful, benchmark or behavior snapshots.
4. Choose the smallest refactor that yields the intended design benefit. Avoid bundling feature work, dependency upgrades, or broad formatting.
5. Make one coherent structural change at a time and keep public behavior stable.
6. Run tests after each meaningful step. Add characterization tests if important behavior lacks coverage before moving code.
7. Compare before/after behavior and performance where relevant. Call out any behavior changes instead of labelling the whole patch a refactor.
8. Update docs only where structure affects a developer-facing contract or architecture guide.

## Output

- Targeted design smell and rationale
- Behavior invariants
- Changes and trade-offs
- Verification evidence
- Remaining coupling / follow-up candidates

## Guardrails

Do not refactor merely for personal style. Preserve compatibility unless a breaking change is explicitly authorized. If tests are insufficient to establish preservation, state the uncertainty and add tests before making high-risk moves.
