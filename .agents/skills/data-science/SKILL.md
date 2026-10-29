---
name: data-science
description: "Plan or execute a reproducible data analysis or machine-learning experiment with data provenance, leakage checks, baselines, metrics, uncertainty, and reproducible outputs."
license: MIT
---

# Data science workflow

1. Translate the question into a measurable estimand, prediction target, or decision. Define the unit of analysis and time horizon.
2. Inspect data schema, provenance, rights, sensitive fields, missingness, duplicates, class balance, selection bias, and quality constraints before modeling.
3. Write a minimal data dictionary and reproducible preprocessing steps. Keep transformations fit only on training data where required.
4. Split data by the real deployment setting (time, entity, group, or random as justified). Check for label leakage, near-duplicates, contaminated evaluation data, and post-outcome features.
5. Establish a simple baseline before adding complexity. Select metrics aligned with business/user impact and compare against a credible threshold.
6. Track experiment parameters, data/model versions, seeds, environment, and outputs. Report variance and uncertainty where feasible.
7. Perform error analysis by meaningful slices. Inspect false positives/negatives and failure modes rather than relying only on one aggregate score.
8. Discuss deployment risks: drift, monitoring, retraining, latency, privacy, feedback loops, and rollback.

## Output

- Question and success metric
- Data provenance / quality summary
- Split and leakage-risk rationale
- Baseline and experimental method
- Results with uncertainty and error slices
- Reproducibility record
- Limitations and next experiment

## Guardrails

Do not fabricate results or run claims beyond the data. Never expose sensitive records. Distinguish correlation from causation and offline metrics from real-world impact.
