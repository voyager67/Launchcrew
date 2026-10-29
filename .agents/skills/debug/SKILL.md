---
name: debug
description: "Investigate a bug using reproducible evidence, competing root-cause hypotheses, narrow experiments, and a regression test before implementing the smallest reliable fix."
license: MIT
---

# Debug workflow

1. Capture the exact symptom, reproduction steps, expected behavior, actual behavior, environment, and recent relevant changes.
2. Reproduce before changing code. If reproduction is impossible, record what evidence is missing.
3. Trace the execution path and inspect logs, tests, inputs, state transitions, and error boundaries.
4. Generate at least two plausible hypotheses for non-trivial failures. For each, list confirming and disconfirming evidence.
5. Choose the smallest experiment that distinguishes hypotheses. Change one variable at a time and avoid modifying unrelated files.
6. Identify root cause, not just the visible symptom. Verify how the failure propagates and what recovery behavior is expected.
7. Add a regression test before or alongside the fix. Implement the narrowest change that resolves the root cause.
8. Run targeted tests and relevant integration checks. Revisit other hypotheses if evidence disagrees.
9. Summarize the cause, fix, verification, and any residual uncertainty.

## Output

- Reproduction and evidence
- Hypotheses considered and experiments
- Confirmed root cause
- Minimal fix and regression test
- Commands/results and remaining risk

## Guardrails

Do not randomly patch multiple locations, suppress errors, weaken tests, or claim causality based solely on correlation. Ask before destructive data repair or actions that affect shared/prod systems.
