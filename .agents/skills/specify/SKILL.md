---
name: specify
description: "Turn a feature, bug fix, refactor, or product idea into testable requirements, a technical design, a dependency-aware implementation plan, and acceptance scenarios before substantial coding."
license: MIT
---

# Specify workflow

## Choose the right depth

- **Direct:** a tiny fix with one obvious behavior change; write a short intent and test note only.
- **Incremental:** a feature spanning a few components; create requirements, design, and an ordered phase plan.
- **Factory:** broad work with independent deliverables; create a manifest, isolated units, explicit dependencies, and holdout acceptance scenarios.

Do not over-specify a small change.

## Procedure

1. Inspect relevant source, tests, existing conventions, and related issues/docs. Identify what already exists.
2. State the problem, primary user, current behavior, desired outcome, and why it matters. Keep solution ideas separate from requirements.
3. Define scope, non-goals, assumptions, constraints, compatibility promises, risks, and measurable success conditions.
4. Write requirements as observable behavior. Use unique IDs (`REQ-001`) and concrete acceptance criteria. Include negative paths and edge cases.
5. Propose the smallest defensible architecture: components, responsibilities, data flow, interfaces, persistence, errors, security boundaries, and migration needs where relevant.
6. Split work into small slices. Each slice must have one owner, bounded files/interfaces, dependencies, acceptance evidence, and a verification command where possible.
7. Add acceptance scenarios that are not simply copied from implementation instructions. Cover success, validation failures, permission boundaries, and regression risks.
8. Check feasibility against the actual repository and note external dependencies or unknown API behavior.
9. Save artifacts under the repository's existing spec convention. If there is no convention, use `.launchcrew/specs/NNN-short-name/` with `requirements.md`, `design.md`, `plan.md`, and `acceptance.md`. Find the next available ID; never overwrite an existing spec.
10. Run `$validate` or explicitly identify why it is unnecessary for a Direct-tier change.

## Required output

- One-paragraph outcome and scope
- Requirements and acceptance criteria
- Non-goals / assumptions / open questions
- Design and alternatives considered
- Ordered slices with dependencies and verification
- Risks, rollout/rollback notes, and acceptance scenarios

## Guardrails

Do not start implementation merely because the spec exists. A spec is a decision aid, not authorization for irreversible actions. Mark guessed facts as assumptions. Do not claim user or stakeholder alignment without evidence.
