---
name: ui-ux
description: "Turn product requirements into understandable interface flows and interaction criteria, accounting for loading, empty, error, success, responsive, and accessible states."
license: MIT
---

# UI/UX workflow

1. Identify user, context, goal, existing workflow, constraints, and observable success.
2. Map the primary journey and important branches. Minimize steps without hiding critical choices or consequences.
3. Define information hierarchy, navigation, labels, affordances, and the primary action. Prefer familiar patterns unless a new pattern solves a clear problem.
4. Specify all meaningful states: initial, loading, empty, partial data, validation, permission denied, offline/failure, success, and recovery.
5. Include responsive behavior, keyboard/focus behavior, accessible labels, contrast, reduced motion, and clear error recovery.
6. Match designs to existing design tokens and components. If a visual direction is new, show a small number of alternatives and their trade-offs.
7. Define usability acceptance criteria and how to test them with representative tasks.
8. If implementing, keep semantics and visual styling aligned; run relevant browser or screenshot checks when available.

## Output

- User / context / goal
- Main flow and edge flows
- Content hierarchy and interaction rules
- State table
- Accessibility and responsive requirements
- Acceptance criteria and usability questions

## Guardrails

Do not optimize for novelty over clarity. Avoid unsupported statements about what “users want” without evidence. Don't use color alone to communicate status or turn destructive actions into easy-to-misclick primary actions.
