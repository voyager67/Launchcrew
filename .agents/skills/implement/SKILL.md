---
name: implement
description: "Execute an approved spec or bounded engineering task in small slices, coordinate independent subagent work when available, verify each slice, detect drift, and preserve resumable progress."
license: MIT
---

# Implement workflow

## Entry conditions

Find the applicable spec, acceptance criteria, project instructions, tests, and any in-progress ledger. If the spec is missing or contradictory, pause and report the smallest decisions needed before broad implementation.

## Procedure

1. Classify the work as Direct, Incremental, or Factory. Use the lowest process level that safely fits.
2. Inspect the relevant code path, tests, interfaces, and repository conventions. Avoid broad repository scans for narrow work.
3. Build a task graph. Keep dependencies explicit and identify independent slices that may be delegated. Assign a single owner to each edited file or interface.
4. Implement one slice at a time. Prefer small changes that can be verified independently. Do not combine unrelated cleanup with the requested behavior.
5. Add/update tests that express observable requirements. Run the narrowest relevant checks after each slice, then the broader suite at integration.
6. Compare behavior with the requirements. If the implementation or discovered constraints imply a spec change, stop that slice, record the conflict, and request or document an approved decision rather than silently drifting.
7. Record progress in the spec folder's ledger: completed slices, changed files, commands run, test outcomes, failures, and remaining risks. Never fabricate passing checks.
8. Integrate delegated work only after reviewing its diffs and evidence. Resolve conflicts centrally; never let agents edit the same files concurrently without coordination.
9. Run final verification, summarize user-visible changes, and list tests and limitations.

## Done means

- Every in-scope acceptance criterion is satisfied or explicitly unresolved.
- Relevant tests ran and outcomes are reported accurately.
- No known failures are hidden or dismissed as “pre-existing” without evidence.
- Docs/config/migrations are updated when behavior requires it.
- No unapproved destructive actions, dependency upgrades, commits, pushes, or deployments occurred.

## Guardrails

Respect sandbox and approval policies. Ask before destructive actions, external side effects, secrets access, cost-incurring services, or deployment. Do not claim to have used parallel agents if the environment did not provide them.
