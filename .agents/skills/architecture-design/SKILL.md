---
name: architecture-design
description: "Design or assess a system architecture by clarifying constraints, mapping boundaries and data flows, comparing options, and recording reversible decisions and operational risks."
license: MIT
---

# Architecture design workflow

1. Establish functional requirements, quality attributes, scale assumptions, deployment constraints, existing components, and non-goals.
2. Record unknowns and identify which ones materially affect the decision. Research version-sensitive APIs or technologies before relying on them.
3. Map the current or proposed system: actors, entry points, components, state, data flow, trust boundaries, and external dependencies.
4. Compare at least two plausible options when the decision is consequential. Include a simple baseline when appropriate.
5. Evaluate correctness, complexity, reliability, security/privacy, latency, cost, team operability, migration, and reversibility.
6. Define API/data contracts, failure modes, retries/idempotency, authorization, observability, migration, backup, and rollback where relevant.
7. Prefer the least complex option that meets requirements. Distinguish measured constraints from guessed future scale.
8. Record the decision using the repository's ADR convention. If none exists, propose an ADR in `docs/decisions/` rather than inventing a large documentation framework.

## Output

- Context, requirements, and constraints
- Current/proposed architecture diagram or text flow
- Options and trade-off matrix
- Recommended option with rationale
- Interfaces and failure semantics
- Security, operations, migration, and rollback risks
- Revisit triggers / decision owner

## Guardrails

Avoid architecture astronautics and premature scaling. Do not assert system capacity without measurements. Keep implementation decisions distinct from user/product decisions.
