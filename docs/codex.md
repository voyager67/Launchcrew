# Codex CLI setup

LaunchCrew uses Codex-native surfaces: repository instructions, portable skill folders, and project-scoped custom agent files. Use the repository-local setup when possible because it keeps the workflow versioned with the project.

## What is loaded where?

- `AGENTS.md` contains durable, repo-wide guidance.
- `.agents/skills/<skill>/SKILL.md` contains a portable workflow. Codex can discover repository-local skills from the standard skills directory.
- `.codex/agents/*.toml` defines optional project-scoped specialist agents. They are useful only when the running Codex environment supports subagents and the configuration is enabled.
- `.codex/config.example.toml` is an example only. Review the current configuration documentation before copying it to `.codex/config.toml`.

## Quick path

```bash
codex
```

In the session, try `$specify` for a feature with several requirements, then `$validate`, `$implement`, `$test`, and `$review` as appropriate. Skill invocation syntax can evolve; consult current Codex documentation if a skill is not discovered.

For use in an existing project:

```bash
/path/to/launchcrew/scripts/install.sh --project /path/to/your-project
```

This copies the skill library to `/path/to/your-project/.agents/skills/` and refuses to overwrite a skill folder that already exists. It does not modify the target project's `AGENTS.md` or Codex configuration. Review and link to the skills you want from your own project instructions.

To install skills as personal Codex skills:

```bash
/path/to/launchcrew/scripts/install.sh --global
```

The global installer uses `${CODEX_HOME:-$HOME/.codex}/skills/` and refuses name collisions. If you already have a skill with the same name, compare and merge manually rather than overwriting it.

## Working styles

Optional communication profiles live in [`styles/the-sprint.md`](../styles/the-sprint.md) and [`styles/the-craft.md`](../styles/the-craft.md). Reference one in your prompt or incorporate its principles into your repo-level `AGENTS.md`; these profiles do not replace project instructions or Codex security controls.

## Multi-agent use

Codex custom agents are defined in `.codex/agents/`. Use them when subtasks are genuinely independent, such as an architecture investigation and an independent test review. Do not delegate tightly coupled edits to several agents at once. Agent tools, concurrency, and availability depend on your Codex version and configuration.

A useful prompt is:

```text
Use startup_chief to coordinate. Have architect inspect component boundaries,
qa map the regression risks, and researcher verify any version-specific API
assumptions. Keep those tasks read-only. Integrate their findings before
assigning engineer a single bounded implementation slice. Review and test the
result before summarizing.
```

## Reference documentation

- [Codex](https://developers.openai.com/codex/)
- [Codex skills](https://developers.openai.com/codex/skills)
- [Codex subagents and custom agents](https://developers.openai.com/codex/subagents)
- [Codex configuration reference](https://developers.openai.com/codex/config-reference)
- [Agent Skills standard](https://agentskills.io/)

This documentation was checked during the initial package build on 2026-10-29. Because product capabilities can change, verify current official docs before relying on version-specific settings.
