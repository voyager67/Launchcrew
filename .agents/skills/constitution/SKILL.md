---
name: constitution
description: "Create or refine project-wide principles, non-negotiable constraints, quality bars, and decision rules. Use at project kickoff or when inconsistent agent behavior needs durable guidance."
license: MIT
---

# Constitution workflow

## Outcome

Create a concise project charter that helps people and agents make consistent trade-offs. Do not turn preferences into rigid law without context.

## Procedure

1. Inspect the README, existing `AGENTS.md`, tests, architecture notes, and relevant product requirements. Read only the material needed to understand the project.
2. Identify the product outcome, users, constraints, quality requirements, compatibility commitments, and risks. Separate stated facts from inferred defaults.
3. Draft principles in priority order. Each principle must include a rule, why it matters, and an observable way to check it.
4. Include non-goals, decision ownership, security/privacy expectations, and when human approval is required.
5. Reconcile conflicts with existing repo instructions; do not silently erase or replace them.
6. Present material trade-offs and uncertain assumptions. Ask for approval only where a decision would change architecture, policy, or project direction.
7. Save to the repo's established governance location. If none exists, propose `docs/engineering-charter.md` and link it from `AGENTS.md` only with user approval.

## Output

- Purpose and scope
- 5–9 prioritized principles
- Explicit non-goals
- Quality and security bars
- Decision rights and escalation points
- Open questions / assumptions

## Guardrails

Keep this brief enough to remain useful. Do not duplicate every coding convention from `AGENTS.md`. A charter guides decisions; it does not replace tests, permissions, or human accountability.
