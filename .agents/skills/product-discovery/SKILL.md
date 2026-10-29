---
name: product-discovery
description: "Clarify a product opportunity by identifying users, jobs-to-be-done, pain severity, current alternatives, constraints, scope, and measurable outcomes before committing to a build."
license: MIT
---

# Product discovery workflow

1. Summarize the opportunity in one sentence without naming the solution as the problem.
2. Identify primary user segments, context, trigger, job-to-be-done, current workaround, and consequence of failure.
3. Separate evidence (interviews, analytics, support tickets, observed behavior) from assumptions and anecdotes. Cite sources supplied or researched.
4. Map alternatives, including doing nothing, existing tools, manual process, and adjacent competitors. Compare user outcomes, not only feature lists.
5. Assess pain frequency, severity, urgency, willingness/ability to adopt, and affected population where evidence permits. Do not invent market sizes.
6. Propose the smallest test that could falsify the most important assumption: interview, landing-page test, prototype, data query, or manual concierge run.
7. Define success metrics with a baseline, target, measurement window, and owner. Include guardrail metrics that catch harm or degraded experience.
8. Define an MVP scope and non-goals. Label risks and assumptions needing validation before implementation.

## Output

- Problem statement and target segment
- Evidence table (source, finding, confidence, caveat)
- Jobs, alternatives, and differentiation hypothesis
- Assumptions ranked by risk
- MVP and explicit non-goals
- Success/guardrail metrics
- Low-cost validation plan and decision threshold

## Guardrails

Do not mistake a compelling narrative for evidence. Avoid false precision, invented customer quotes, and unsupported competitive claims. Recommend not building when evidence favors a different next step.
