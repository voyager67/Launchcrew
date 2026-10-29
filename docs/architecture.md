# Architecture and workflow model

## What LaunchCrew is

LaunchCrew is a content-first workflow system: portable skill instructions and project-specific context guide the model; Codex's own execution environment supplies file access, terminal tools, approvals, and optional subagent orchestration. ChatGPT can consume portable skills where supported and can use the Project instructions fallback.

It is not a replacement agent runtime, does not create hidden tool permissions, and does not guarantee multi-agent execution.

## Layers

1. **Project policy — `AGENTS.md`**: compact durable instructions, boundaries, and validation commands.
2. **Reusable workflows — `.agents/skills/*/SKILL.md`**: narrowly scoped procedures with triggers and expected outputs.
3. **Specialist profiles — `.codex/agents/*.toml`**: Codex-specific roles that can be delegated independent tasks.
4. **Durable work artifacts — `.launchcrew/specs/`**: optional requirements, design, plans, acceptance scenarios, and progress ledger.
5. **Packaging and validation — `scripts/`**: deterministic installation, archive creation, and metadata checks.

## Decomposition levels

### Direct

Use for very small changes. Inspect relevant code, make the change, run targeted checks, and summarize. No spec folder is required by default.

### Incremental

Use for features with multiple components or acceptance conditions. Create requirements, design, plan, and acceptance criteria; implement ordered slices with per-slice checks.

### Factory

Use for broad work with multiple independent units. Create a manifest, define ownership and dependency graph, and keep holdout acceptance scenarios separate from implementation directions where useful. Integrate after each unit is verified.

## Parallelization contract

Subagents are useful for independent exploration, research, test design, security review, and separately owned slices. They are not useful for short dependent work or when two agents must edit the same files. The coordinating agent owns the spec, assigns file ownership, resolves conflicts, verifies merged output, and reports actual evidence.

## Resumability

Keep active work in files rather than chat-only state. Recommended structure for a complex feature:

```text
.launchcrew/specs/001-feature-name/
├── requirements.md
├── design.md
├── plan.md
├── acceptance.md
└── progress.md
```

Treat this as a recommended convention, not a requirement for every repository.

## Compatibility boundary

- `AGENTS.md`, portable skills, and ChatGPT Project instructions are separate surfaces with overlapping intent but different loading behavior.
- Codex custom agents in `.codex/agents/*.toml` are Codex-specific.
- ChatGPT Skills installation is account/workspace dependent; the generated archives contain skill content, not native agents or tool permissions.
- Tool availability and exact skill invocation syntax can change. Keep docs linked to official references and re-check version-specific claims periodically.
