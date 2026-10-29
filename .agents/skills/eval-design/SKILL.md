---
name: eval-design
description: "Design an evaluation strategy for an AI model, agent, prompt, or workflow, including representative cases, holdouts, rubrics, graders, failure taxonomy, and regression gates."
license: MIT
---

# AI evaluation design workflow

1. Define the system's intended use, excluded use, target users, and failure costs.
2. Translate requirements into observable dimensions (correctness, completeness, grounding, safety, tool use, latency, cost, usability). Avoid vague “quality” alone.
3. Build a small but representative dataset across common, boundary, adversarial, and high-impact cases. Separate development examples from held-out evaluation cases.
4. Record source, rights, expected behavior, rubric, labels, and version for each case. Remove sensitive data and check duplicates/contamination.
5. Define graders: deterministic checks for exact facts/structure when possible, rubric-based human review for nuanced quality, and model grading only with calibrated examples and bias checks.
6. Include negative and refusal cases where relevant, plus task-specific prompt injection or tool failure scenarios.
7. Set thresholds before looking at final results. Report sample size, uncertainty, per-slice performance, and disagreement between graders.
8. Compare a baseline and candidate using identical conditions. Inspect qualitative failures before claiming improvement.
9. Turn high-severity regressions into automated gates where stable; keep expert review for ambiguous high-impact decisions.

## Output

- Use case and failure taxonomy
- Evaluation dimensions / rubric
- Dataset design and holdout policy
- Example case schema
- Grader plan and calibration
- Baseline / threshold / reporting plan
- Known limitations and next iteration

## Guardrails

Do not use test data to tune and then report it as held out. Avoid one-number claims that hide important slices. Protect privacy and clearly label synthetic versus real examples.
