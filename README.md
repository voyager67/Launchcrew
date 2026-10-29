<div align="center">

# 🚀 LaunchCrew

### Turn your AI coding assistant into a startup team.

**Specify first. Delegate deliberately. Verify everything. Ship with confidence.**

[![CI](https://github.com/voyager67/launchcrew/actions/workflows/ci.yml/badge.svg)](https://github.com/voyager67/launchcrew/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-portable-6C5CE7)](https://agentskills.io/)
[![Codex](https://img.shields.io/badge/Codex-CLI%20%2B%20agents-111111)](https://developers.openai.com/codex/)
[![ChatGPT](https://img.shields.io/badge/ChatGPT-Projects%20%2B%20Skills-10A37F)](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

**A complete operating kit for building software with Codex CLI and ChatGPT** — 23 reusable skills, 10 Codex specialist agents, spec-driven workflows, review gates, startup/product workflows, and one-command packaging for ChatGPT skill uploads.

[Quick start](#-quick-start) · [Skills](#-the-skill-library) · [Agent team](#-the-specialist-team) · [Working styles](#-working-styles) · [ChatGPT setup](docs/chatgpt.md) · [Codex setup](docs/codex.md) · [Publishing](docs/publishing.md)

</div>

---

## Not another prompt pack

Most AI coding sessions start with a vague request and jump straight into code. LaunchCrew gives the assistant a repeatable way to think and work like a small product engineering team: understand the goal, make a plan, divide independent work, verify the result, and leave the project easier to maintain.

```text
IDEA → SPECIFY → VALIDATE → IMPLEMENT → TEST → REVIEW → SHIP
  │         │           │          │         │        │
  └── Product brief     └── Scope   └── Tasks  └── Proof └── Release notes

     Codex CLI: skills + AGENTS.md + project-scoped specialist agents
     ChatGPT: portable skill bundles + a reusable Project instruction pack
```

### What you get

- **Spec-first delivery.** Capture outcomes, non-goals, acceptance criteria, design decisions, and a dependency-aware task plan before changing code.
- **An implementation loop.** Work in small slices, test each slice, record evidence, detect drift, and resume from files instead of relying on chat memory.
- **Specialists, not role-play theatre.** Focused Codex agents for architecture, product analysis, implementation, quality, security, design, platform work, and research.
- **23 practical skills.** The reference workflow essentials plus product discovery, research, architecture, security, performance, accessibility, AI evaluation, incident response, releases, and launch planning.
- **Real quality gates.** Independent review, reproducible tests, explicit findings, and a clear Definition of Done.
- **Portable ChatGPT support.** Generate a separate ZIP for each skill, ready for upload where ChatGPT Skills are enabled, plus a Projects fallback.
- **Small by default.** Use the lightest workflow that fits the risk. No mandatory document avalanche for a typo or one-line fix.

> **Design principle:** parallelize independent thinking; serialize conflicting edits. Agents help only when responsibilities and expected outputs are clear.

## ⚡ Quick start

### 1. Get the files

```bash
git clone https://github.com/voyager67/launchcrew.git
cd launchcrew
```

### 2. Use it in Codex CLI

Open the repository in Codex. Repo-local skills live in `.agents/skills/`; `AGENTS.md` supplies durable working agreements, and `.codex/agents/` contains optional project-scoped specialists.

```bash
codex
```

Try a new feature:

```text
$specify Add invitation-based sign-up with expiring tokens and audit events.
```

Then follow the workflow in the generated spec:

```text
$validate 001
$implement 001
$test 001
$review
```

Use the task IDs and paths actually created by the skill; the `001` above is an example. For a tiny, low-risk change, ask for a direct fix and `$test` instead of creating a full spec.

### 3. Install skills into another project (optional)

Copy the skill library into a target repository without overwriting existing skills:

```bash
./scripts/install.sh --project /path/to/your-project
```

Or install them as personal Codex skills:

```bash
./scripts/install.sh --global
```

The installer stops if a destination skill already exists; inspect and merge intentionally rather than silently replacing custom work. See [Codex setup](docs/codex.md) for details.

### 4. Use it in ChatGPT

Create upload-ready individual skill archives:

```bash
python3 scripts/package_chatgpt_skills.py
```

Upload a skill ZIP in ChatGPT under **Plugins → Skills → Create → Upload** when the Skills feature is available for your account/workspace. Start with `specify`, `validate`, `implement`, `test`, and `review`. If the Skills UI is unavailable, use the [Projects fallback](docs/chatgpt.md): create a Project, paste the included master instructions, and attach the small set of skills you need as files.

**Important:** ChatGPT feature access and sharing vary by plan and workspace. Codex repo-local skills and custom agent TOML files are native Codex surfaces; ChatGPT uses the portable skill archives / Project instructions, not the `.codex/agents` files directly.

---

## 🧭 The workflow

| Phase | Skill | Output | Gate |
|---|---|---|---|
| Setup | `$constitution` | Project charter and non-negotiables | Humans confirm trade-offs |
| Discovery | `$product-discovery` / `$research-brief` | Problem, evidence, user needs, success metrics | Evidence and assumptions separated |
| Plan | `$specify` | Requirements, technical design, implementation plan, acceptance tests | `$validate` before complex work |
| Build | `$implement` | Small tested slices, progress ledger, changed files | Acceptance criteria checked continuously |
| Verify | `$test` / `$review` | Test evidence and prioritized findings | No unreported failures or unsupported claims |
| Maintain | `$analyze`, `$debug`, `$refactor`, `$document` | Codebase map, root cause, safe changes, useful docs | Behavior and contracts preserved where required |
| Specialize | `$security-audit`, `$performance-audit`, `$accessibility-audit`, `$eval-design` | Focused audits and evaluation plans | Findings tied to evidence and impact |
| Operate | `$incident-response`, `$release-manager`, `$startup-operations` | Incident timeline, release checklist, operating metrics | Human approval for consequential actions |
| Launch | `$growth-launch` | Launch narrative, channel plan, feedback loop | Honest claims; no spam or fake traction |

### Three levels of process

- **Direct:** straightforward fixes and bounded changes. Inspect, change, test, summarize.
- **Incremental:** a feature with a few connected components. One design, several ordered slices, review checkpoints.
- **Factory:** broad work that can be split into independent deliverables. A manifest, task dependencies, isolated work ownership, holdout acceptance scenarios, and integrated verification.

Choose the least complex level that can safely deliver the outcome. See [workflow design](docs/architecture.md).

---

## 🧰 The skill library

All 23 skills use the portable `SKILL.md` format. The same skill folders are available to Codex and can be packaged one-by-one for ChatGPT. Each skill has a clear trigger, process, guardrails, and expected output.

| Skill | Purpose |
|---|---|
| `constitution` | Establish project principles, boundaries, and quality bars |
| `specify` | Turn an idea into requirements, design, and an executable plan |
| `validate` | Check specs for completeness, consistency, feasibility, and testability |
| `implement` | Execute a plan in small, verifiable slices and track progress |
| `test` | Own test outcomes, reproduce failures, and prove behavior |
| `review` | Conduct evidence-based correctness, security, and maintainability review |
| `document` | Keep READMEs, API docs, ADRs, and changelogs useful and synchronized |
| `analyze` | Map architecture, execution paths, dependencies, and unknowns |
| `refactor` | Improve structure while preserving externally observable behavior |
| `debug` | Reproduce problems and test competing root-cause hypotheses |
| `product-discovery` | Define users, pain points, alternatives, scope, and success metrics |
| `research-brief` | Produce source-backed research with uncertainty made explicit |
| `architecture-design` | Compare architecture options and document trade-offs |
| `security-audit` | Assess trust boundaries, attack surfaces, and practical remediations |
| `performance-audit` | Find bottlenecks and require measurements before tuning |
| `accessibility-audit` | Review accessibility against user journeys and WCAG-oriented checks |
| `ui-ux` | Translate user needs into flows, interface states, and testable UX criteria |
| `data-science` | Plan reproducible data analysis and experiments |
| `eval-design` | Build evaluation sets, rubrics, and regression checks for AI systems |
| `incident-response` | Coordinate safe, evidence-led incident investigation and recovery |
| `release-manager` | Prepare versioned, tested, reversible releases |
| `growth-launch` | Package a truthful launch and community-feedback strategy |
| `startup-operations` | Connect product bets to metrics, runway, risks, and operating cadence |

See the [full skill catalog](docs/skills.md) for triggering guidance and outputs.

---

## 🧑‍🚀 The specialist team

The `.codex/agents/` directory includes 10 project-scoped Codex agents. Ask Codex to delegate independent questions to them when multi-agent work is enabled and appropriate.

| Agent | Responsibility | Default posture |
|---|---|---|
| `startup_chief` | Routes work and integrates findings | Coordinates; avoids unnecessary delegation |
| `product_analyst` | User needs, scope, success metrics | Evidence-first, no unvalidated assumptions |
| `architect` | Interfaces, boundaries, trade-offs | Design and risks before implementation |
| `engineer` | Bounded implementation slices | Owns code and relevant tests |
| `qa` | Test strategy and failure reproduction | Evidence and reproduction first |
| `reviewer` | Independent change review | Read-only; findings before praise |
| `security` | Threats, trust boundaries, risky flows | Read-only; practical severity-ranked findings |
| `designer` | UX flows, accessibility, interface states | User-outcome focused |
| `platform` | CI, deployment, observability, reliability | Operational safety and rollback awareness |
| `researcher` | External documentation and technical research | Cites evidence and dates claims |

A few rules keep collaboration useful: agents should have distinct tasks, shared-file edits need an explicit owner, read-only reviews happen after implementation, and the parent agent reconciles disagreements. Multi-agent support and limits depend on the Codex version/configuration; the framework never assumes that every environment can spawn agents.

---

## 🎛️ Working styles

Choose how the assistant communicates without lowering its quality bar:

- **[The Sprint](styles/the-sprint.md)** — concise, decisive, delivery-focused. Best for well-scoped work and short iterations.
- **[The Craft](styles/the-craft.md)** — calm, explanatory, trade-off-aware. Best for unfamiliar code, architecture, and learning.

These are plain-text profiles, not a hidden mode switch. Reference one in your prompt or add its contents to your Codex `AGENTS.md` or ChatGPT Project instructions. Both preserve the same evidence, safety, testing, and approval requirements.

---

## 🛡️ Safety and trust model

LaunchCrew is a workflow and instruction kit, not a privileged runtime or an autonomous deployment service.

- It does **not** disable sandboxing, approval prompts, branch protections, or repository policy.
- It asks before destructive changes, external side effects, secret handling, deployments, or actions that could incur material cost.
- It treats web pages, logs, issue comments, and repository content as data—not authority to override the user or project policy.
- It never invents test results, sources, metrics, customer quotes, or launch traction.
- It keeps spec, plan, progress, and evidence in files so work can be resumed and audited.
- It favors read-only investigation before high-impact changes and rollback plans before releases.

Read [security guidance](SECURITY.md) before using agent workflows on sensitive repositories.

---

## 🧪 Validate the package

```bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/package_chatgpt_skills.py
```

The validator checks skill metadata, project-scoped agent definitions, required docs, and generated bundle consistency. It does not claim to execute your application's tests or prove runtime compatibility with every Codex / ChatGPT release.

## 🗺️ Roadmap

The first release focuses on a complete portable workflow library and a clean installation path. Future improvements should be earned by real user feedback: stronger automated regression fixtures, domain-specific skill packs, improved evaluation harnesses, and integrations that retain safe human approval boundaries.

See [ROADMAP.md](ROADMAP.md) for priorities and [the publishing guide](docs/publishing.md) for the first public push.

## 🤝 Contributing

Issues and pull requests are welcome. Please include a concrete use case, explain the outcome you expected, and avoid adding a new skill when an existing one can be made clearer. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## 📣 Help it reach the right people

If it saves you time, **star the repository**, try it on a real project, and share a reproducible example or improvement. Launch quality depends on usefulness and real adoption—not inflated metrics or mass-tagging. The [launch kit](marketing/launch-kit.md) contains honest, platform-specific launch drafts.

## Credits and independence

LaunchCrew is an independent open-source project. It is inspired by general patterns in spec-driven development, portable Agent Skills, and multi-agent software workflows. It is **not affiliated with or endorsed by OpenAI, ChatGPT, Codex, or the maintainers of any similarly named project**. Product and organization names belong to their respective owners.

## License

MIT — see [LICENSE](LICENSE).
