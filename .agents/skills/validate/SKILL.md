---
name: validate
description: "Review requirements, designs, plans, or implementation artifacts for completeness, consistency, feasibility, testability, risk, scope drift, and readiness before proceeding."
license: MIT
---

# Validate workflow

## Procedure

1. Identify the artifact under review and the decision it must support (ready to plan, ready to implement, or implementation conforms).
2. Read only the linked requirements, design, plan, charter, and relevant code/tests.
3. Check completeness: every requirement has an owner or implementation mapping and measurable acceptance evidence.
4. Check consistency: names, interfaces, data shapes, error behavior, scope, and dependencies agree across documents.
5. Check feasibility: each task is bounded, dependencies are acyclic, tool/API assumptions are verified or flagged, and the plan fits repository conventions.
6. Check testability: include happy paths, edge cases, failure modes, security/privacy expectations, and regression conditions.
7. Check risk and operations: migration, rollout, observability, rollback, accessibility, performance, and data handling where relevant.
8. Detect scope drift: list requirements that are missing, changed, contradicted, or added without decision.
9. Assign findings by severity and cite exact file/section or symbol. Separate blockers from improvements.
10. Return **PASS**, **PASS WITH RISKS**, or **NOT READY** with concise rationale and the minimum fixes required.

## Output format

- Verdict and why
- Blockers (if any)
- Findings table: severity, evidence/location, impact, recommended fix
- Open assumptions / decisions
- Re-check criteria

## Guardrails

Validation is evidence-led, not ceremonial. Never label a plan “validated” if sections were not inspected. Do not block delivery on cosmetic preferences. Be explicit if code or external documentation was unavailable.
