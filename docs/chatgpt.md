# ChatGPT setup

LaunchCrew is built around portable Agent Skills, but ChatGPT feature access depends on account, plan, and workspace settings. The most direct path is to upload individual skill ZIPs where the Skills interface is available. The fallback is a ChatGPT Project with the master instructions and selected skill files attached.

## Option A — Upload individual Skills

1. From the repository root, generate packages:

   ```bash
   python3 scripts/package_chatgpt_skills.py
   ```

2. Open `dist/chatgpt-skills/`. Each archive contains exactly one skill folder with its `SKILL.md` and any optional support files.
3. In ChatGPT, open **Plugins → Skills → Create → Upload from your computer** if this feature is available to you.
4. Upload the skills most useful to your workflow. Start with `specify`, `validate`, `implement`, `test`, and `review` rather than enabling every possible workflow immediately.
5. Ask ChatGPT to use a skill by name if it does not select the skill automatically.

A skill archive is portable content, not a permission grant. It does not install Codex custom agents, turn on external tools, grant repository access, or bypass workspace policy.

## Option B — ChatGPT Projects fallback

If the Skills interface is not available:

1. Create a ChatGPT Project for the codebase or product.
2. Copy the contents of [`chatgpt-project-instructions.md`](chatgpt-project-instructions.md) into Project instructions.
3. Attach only the skill `SKILL.md` files needed for the current type of work, along with non-sensitive project docs.
4. For coding changes, provide the relevant repository files or use the connected/available coding surface. A Project instruction file alone cannot edit a local repository it cannot access.
5. Keep the spec, decisions, and progress record as files so future conversations can resume reliably.

## Important distinction

ChatGPT Projects and ChatGPT Skills are not the same as Codex CLI. Codex's `AGENTS.md`, `.codex/agents/*.toml`, terminal, and repository-local skill discovery are Codex-specific. ChatGPT can use portable skill content and Project instructions, but the exact tools available in a ChatGPT conversation depend on the current product surface and your connected apps.

## Optional response styles

Attach [`the-sprint.md`](../styles/the-sprint.md) or [`the-craft.md`](../styles/the-craft.md) to the Project and reference the desired style in Project instructions. They guide tone and explanation depth only; they do not enable tools or override safety boundaries.

## Recommended first five skills

- `product-discovery`: clarify the goal before building.
- `specify`: create requirements and a realistic plan.
- `validate`: find gaps before expensive implementation.
- `review`: independently check a proposal or change.
- `research-brief`: investigate current claims with sources.

## Official resources

- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)
- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects)
- [Skills concept for ChatGPT and Codex](https://developers.openai.com/plugins/concepts/skills)
- [Agent Skills standard](https://agentskills.io/)
