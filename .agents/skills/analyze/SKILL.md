---
name: analyze
description: "Explain an unfamiliar repository or feature by mapping entry points, execution paths, data flow, dependencies, conventions, and unknowns before recommending changes."
license: MIT
---

# Analyze workflow

1. Clarify the question and requested depth: quick orientation, focused bug path, architecture map, or change-impact analysis.
2. Inspect repository structure and relevant instruction files, then trace from a real entry point to the behavior in question.
3. Follow data and control flow across calls, persistence, queues, UI state, permissions, and error handling as applicable.
4. Identify module responsibilities, public contracts, external dependencies, and tests that exercise the path.
5. Search for existing patterns before recommending a new abstraction. Note duplicated or legacy paths only when relevant.
6. Separate observed facts, strong inferences, hypotheses, and unknowns. Cite file paths, symbols, and line numbers when available.
7. Explain what would change if the user modifies the target, including likely callers/tests/docs/configuration.

## Output

- Plain-English summary
- Relevant execution path (ordered)
- Components and contracts
- Evidence: file/symbol references
- Risks / unknowns
- Minimal safe next step

## Guardrails

Do not edit code during an analysis-only request. Do not claim complete architectural understanding from a partial scan. Prefer targeted evidence over a massive file inventory.
