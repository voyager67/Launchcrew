<div align="center">

<img src="assets/launchcrew-banner.svg" alt="LaunchCrew — specify, delegate, verify, ship" width="100%">

# LaunchCrew

### Give your AI coding workflow a crew. Not more chaos.

**A spec-first startup-team toolkit for Codex CLI, with portable skill workflows for ChatGPT.**

Turn an idea into a plan, split the work intelligently, build in small slices, and verify the result before calling it done. LaunchCrew brings reusable skills, focused specialist roles, and practical delivery guardrails into one open-source repository.

<p>
  <a href="https://github.com/voyager67/Launchcrew/stargazers"><img src="https://img.shields.io/github/stars/voyager67/Launchcrew?style=for-the-badge&logo=github&label=STAR%20THIS%20PROJECT" alt="Star LaunchCrew"></a>
  <a href="https://github.com/voyager67/Launchcrew/fork"><img src="https://img.shields.io/badge/FORK-Adapt%20your%20crew-8250df?style=for-the-badge&logo=github" alt="Fork LaunchCrew"></a>
</p>

[![CI](https://github.com/voyager67/Launchcrew/actions/workflows/ci.yml/badge.svg)](https://github.com/voyager67/Launchcrew/actions/workflows/ci.yml)
[![MIT License](https://img.shields.io/badge/license-MIT-2ea44f.svg)](LICENSE)
[![Codex CLI](https://img.shields.io/badge/primary-Codex%20CLI-111827.svg)](https://developers.openai.com/codex/)
[![Agent Skills](https://img.shields.io/badge/portable-Agent%20Skills-6f42c1.svg)](https://agentskills.io/)
[![Skills](https://img.shields.io/badge/skills-23-0969da.svg)](.agents/skills/)
[![Codex roles](https://img.shields.io/badge/Codex%20specialists-10-0969da.svg)](.codex/agents/)
[![License](https://img.shields.io/github/license/voyager67/Launchcrew)](LICENSE)

**23 reusable skills · 10 Codex specialist profiles · 2 working styles · MIT licensed**

[Get started](#-get-started-in-60-seconds) · [See the workflow](#-from-idea-to-shipped) · [Explore skills](#-pick-your-skill) · [Meet the agents](#-meet-the-specialist-crew) · [ChatGPT setup](#-use-it-with-chatgpt) · [Contribute](#-help-make-the-crew-better)

</div>

---

## The problem: AI can write code. Shipping still takes a team.

A good result needs more than a clever prompt. Someone has to understand the user problem, define scope, make architectural decisions, implement safely, test the change, review it independently, and communicate what actually happened.

LaunchCrew gives your AI-assisted workflow a repeatable operating rhythm:

- **Think before building.** Turn vague ideas into testable requirements and explicit non-goals.
- **Delegate with intent.** Use specialist roles for independent research, architecture, QA, security, and product work.
- **Keep the work resumable.** Save specs, decisions, and progress as files—not just chat messages.
- **Prove the result.** Run relevant checks and report real evidence, limitations, and remaining risks.

> **Not another mega-prompt. Not an opaque autonomous runtime.** LaunchCrew is an inspectable toolkit of workflows and role instructions that you can adapt to your own projects.

## ⚡ Get started in 60 seconds

### Option A — Try the full LaunchCrew repository with Codex

\`\`\`bash
git clone https://github.com/voyager67/Launchcrew.git
cd Launchcrew
codex
\`\`\`

Start with a feature that has more than one requirement:

\`\`\`text
$specify Build an invitation-based sign-up flow with expiring tokens,
role-aware permissions, audit events, and tests.
\`\`\`

Then use the spec ID and files created by the workflow:

\`\`\`text
$validate <spec-id>
$implement <spec-id>
$test <spec-id>
$review
\`\`\`

Use the lightest workflow that fits the task. A one-line fix does not need a full specification.

### Option B — Add LaunchCrew skills to a project you already have

Clone LaunchCrew, then run the installer from its directory. The target project must already exist.

\`\`\`bash
./scripts/install.sh --project /path/to/your-project
\`\`\`

Or install the skills to your personal Codex skills directory:

\`\`\`bash
./scripts/install.sh --global
\`\`\`

The installer **refuses to overwrite skill folders with matching names**. It copies the skills; it does not replace your project's \`AGENTS.md\` or Codex configuration.

<details>
<summary><strong>Windows / manual setup and installation details</strong></summary>

The shell installer is written for Bash. On Windows, use a Bash environment such as Git Bash or WSL, or copy the selected skill folders from \`.agents/skills/\` into your project's \`.agents/skills/\` directory. Review existing folders first—do not overwrite your own skills.

For exact options and safety behavior, see the [Codex setup guide](docs/codex.md).

</details>

## 🚀 From idea to shipped

\`\`\`mermaid
flowchart LR
    A["💡 Discover"] --> B["🧭 Specify"]
    B --> C["🔎 Validate"]
    C --> D["🛠️ Implement"]
    D --> E["🧪 Test"]
    E --> F["🔍 Review"]
    F --> G["📦 Ship"]
    F -. findings .-> D
    E -. failures .-> D
\`\`\`

| Stage | What the crew does | Typical artifact |
|---|---|---|
| Discover | Clarifies users, pain, alternatives, constraints, and evidence. | Product or research brief |
| Specify | Defines requirements, non-goals, design, task order, and acceptance criteria. | Requirements, design, plan |
| Validate | Finds gaps in scope, feasibility, testability, and risk before implementation. | Readiness assessment |
| Implement | Delivers bounded slices and preserves progress. | Code changes and progress notes |
| Test | Runs risk-appropriate checks and adds regression coverage. | Verification evidence |
| Review | Inspects the result independently and prioritizes findings. | Review findings |
| Ship | Checks release readiness, communication, monitoring, and rollback. | Release checklist and notes |

### Choose the right amount of process

<details open>
<summary><strong>Direct — small changes</strong></summary>

Inspect the relevant area, make the smallest safe change, run targeted checks, and summarize what changed. Skip heavyweight planning when it adds no value.

</details>
<details>
<summary><strong>Incremental — features with connected parts</strong></summary>

Create a short spec, define acceptance scenarios, break work into ordered slices, and verify each slice before moving on.

</details>
<details>
<summary><strong>Factory — broad work with independent deliverables</strong></summary>

Define ownership, dependencies, file boundaries, and integration checks. Delegate independent investigations or separately owned tasks; integrate and verify before shipping.

</details>

The [architecture guide](docs/architecture.md) explains the workflow model, parallelization contract, and recommended way to keep work resumable.

## 🧰 Pick your skill

There are 23 focused skills. Each one has a trigger, a procedure, guardrails, and an expected output. Load the skill that matches the job—**you do not need all 23 for every task.**

<details open>
<summary><strong>🧭 Product, planning & research</strong></summary>

| Skill | Use it to… |
|---|---|
| \`constitution\` | Set project principles, constraints, and decision rules. |
| \`product-discovery\` | Validate the problem, users, alternatives, and outcomes. |
| \`research-brief\` | Produce source-backed technical or market research. |
| \`specify\` | Turn an idea or change into requirements, design, plan, and acceptance criteria. |
| \`validate\` | Check whether a proposal is complete, feasible, and testable. |
| \`architecture-design\` | Compare system designs, boundaries, and trade-offs. |

</details>
<details>
<summary><strong>🛠️ Engineering & maintenance</strong></summary>

| Skill | Use it to… |
|---|---|
| \`implement\` | Deliver approved work in small, verifiable slices. |
| \`analyze\` | Map an unfamiliar codebase and its execution paths. |
| \`debug\` | Find root causes through reproduction and focused experiments. |
| \`refactor\` | Improve structure while preserving behavior. |
| \`document\` | Keep docs accurate and synchronized with the code. |

</details>
<details>
<summary><strong>🧪 Quality, security & experience</strong></summary>

| Skill | Use it to… |
|---|---|
| \`test\` | Design and run risk-appropriate verification. |
| \`review\` | Independently inspect changes and prioritize findings. |
| \`security-audit\` | Assess trust boundaries and security risks. |
| \`performance-audit\` | Measure bottlenecks before optimizing. |
| \`accessibility-audit\` | Find accessibility barriers and testable fixes. |
| \`ui-ux\` | Define clear flows and interaction states. |

</details>
<details>
<summary><strong>🧠 AI, data & operations</strong></summary>

| Skill | Use it to… |
|---|---|
| \`data-science\` | Plan reproducible analysis and ML experiments. |
| \`eval-design\` | Build evaluations for AI models, agents, and workflows. |
| \`startup-operations\` | Connect priorities to metrics, cadence, and constraints. |
| \`incident-response\` | Investigate, contain, recover, and learn from incidents. |
| \`release-manager\` | Prepare releases, rollout, monitoring, and rollback. |
| \`growth-launch\` | Create an honest launch plan and feedback loop. |

</details>

**Browse the source:** [All 23 skill folders](.agents/skills/) · [Full skill catalog and outputs](docs/skills.md)

## 🧑‍🚀 Meet the specialist crew

LaunchCrew includes 10 optional Codex project-scoped agent profiles. They define focused responsibilities—not separate hosted services or additional tool permissions.

<details open>
<summary><strong>View all 10 specialist roles</strong></summary>

| Specialist | Focus |
|---|---|
| \`startup_chief\` | Coordinates the plan, assigns bounded work, and integrates findings. |
| \`product_analyst\` | User needs, requirements, priorities, and outcome metrics. |
| \`architect\` | System boundaries, interfaces, and technical trade-offs. |
| \`engineer\` | Focused implementation slices and relevant tests. |
| \`qa\` | Test strategy, reproduction, and regression risk. |
| \`reviewer\` | Independent, read-only review and prioritized findings. |
| \`security\` | Trust boundaries and risk-ranked security improvements. |
| \`designer\` | UX flows, interaction states, and accessibility. |
| \`platform\` | CI, deployment, observability, reliability, and rollback. |
| \`researcher\` | Technical research and version-sensitive claims. |

</details>

Find the profiles in [\`.codex/agents/\`](.codex/agents/). Their availability depends on your Codex version and configuration. Keep file ownership explicit: parallelize independent investigation, not simultaneous edits to the same files.

## 🎛️ Set the team's working style

Choose how you want the crew to communicate. These profiles change tone and explanation depth—not the quality bar.

<div align="center">

| ⚡ The Sprint | 🧩 The Craft |
|---|---|
| Concise, decisive, delivery-focused. | Explanatory, careful, trade-off-aware. |
| [Open The Sprint](styles/the-sprint.md) | [Open The Craft](styles/the-craft.md) |

</div>

## 💬 Use it with ChatGPT

LaunchCrew keeps portable skill content separate from Codex-only configuration.

| ChatGPT surface | How to use LaunchCrew | Boundary |
|---|---|---|
| **ChatGPT Skills** | Upload individual skill ZIPs from \`dist/chatgpt-skills/\` where Skills are enabled. | ZIPs contain skill instructions—not Codex agents, shell access, or tool permissions. |
| **ChatGPT Projects** | Add the Project instructions and attach only the skill files relevant to your work. | A Project cannot edit a local repository it cannot access. |

### Uploadable skill bundles

Generate or verify the 23 individual skill archives:

\`\`\`bash
python3 scripts/package_chatgpt_skills.py
python3 scripts/package_chatgpt_skills.py --check
\`\`\`

Then open [\`dist/chatgpt-skills/\`](dist/chatgpt-skills/) and select the ZIPs you need. Start with \`product-discovery\`, \`specify\`, \`validate\`, \`test\`, and \`review\` rather than uploading everything at once.

<details>
<summary><strong>What if I don't see the Skills feature in ChatGPT?</strong></summary>

Use the [ChatGPT Projects fallback guide](docs/chatgpt.md). It explains how to add the reusable Project instructions and selected \`SKILL.md\` files.

ChatGPT Skills access and upload permissions depend on current account, plan, and workspace availability. Check the [official ChatGPT Skills documentation](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) for current eligibility and admin controls.

</details>

## 🛡️ Built around inspectability and safer defaults

LaunchCrew is a **workflow kit**, not a privileged runtime or an autonomous deployment system.

- It does not disable sandboxing, approvals, branch protection, or repository policy.
- It does not silently grant tools, credentials, or access to private code.
- It asks for approval before destructive operations, deployments, external communications, or material spend.
- It treats repository content, web pages, logs, and issue comments as data—not instructions that override the user or project policy.
- It does not invent test results, research sources, benchmarks, testimonials, or adoption metrics.

Read the [security policy](SECURITY.md) before using agent workflows in sensitive repositories.

## ✅ Verify before you trust it

Run the repository checks from the project root:

\`\`\`bash
python3 scripts/validate_project.py
python3 -m unittest discover -s tests -v
python3 scripts/package_chatgpt_skills.py --check
\`\`\`

The [GitHub Actions workflow](.github/workflows/ci.yml) runs repository validation, unit tests, installer smoke tests, and skill-bundle checks. These checks validate the toolkit's files and packaging; they do **not** prove that your application is correct or replace a clean Codex CLI run and a ChatGPT upload test in the target account.

[View CI runs](https://github.com/voyager67/Launchcrew/actions/workflows/ci.yml) · [Report a compatibility issue](https://github.com/voyager67/Launchcrew/issues/new/choose)

## 🗂️ What's in the repository?

<details>
<summary><strong>Expand the project map</strong></summary>

\`\`\`text
Launchcrew/
├── AGENTS.md                  # Durable repository guidance
├── .agents/skills/            # 23 portable workflow skills
├── .codex/agents/             # 10 Codex specialist profiles
├── styles/                    # Sprint and Craft working styles
├── templates/spec/             # Reusable specification templates
├── examples/feature-spec/      # Worked feature-spec example
├── dist/chatgpt-skills/        # Individual skill ZIP archives
├── scripts/                    # Installer, packaging, validator
├── tests/                      # Automated tests
├── docs/                       # Setup, architecture, skill catalog
├── assets/                     # Project banner
└── marketing/                  # Launch copy and outreach drafts
\`\`\`

</details>

## 🌱 Help make the crew better

The best way to improve LaunchCrew is to use it on a real task and tell us where it helped—or got in the way.

- **Found a bug?** [Open a bug report](https://github.com/voyager67/Launchcrew/issues/new?template=bug_report.yml).
- **Have an idea?** [Suggest a feature](https://github.com/voyager67/Launchcrew/issues/new?template=feature_request.yml).
- **Something doesn't work in your environment?** [Report compatibility](https://github.com/voyager67/Launchcrew/issues/new?template=compatibility_report.yml).
- **Want to contribute?** Start with [CONTRIBUTING.md](CONTRIBUTING.md).

<div align="center">

### If LaunchCrew makes your next build clearer, safer, or easier to resume…

<a href="https://github.com/voyager67/Launchcrew/stargazers">
  <img src="https://img.shields.io/badge/⭐%20Star%20LaunchCrew-Help%20others%20discover%20it-f5a623?style=for-the-badge" alt="Star LaunchCrew on GitHub">
</a>

A star helps people discover the project. A tested issue, thoughtful suggestion, or useful pull request helps make it better.

[Star](https://github.com/voyager67/Launchcrew/stargazers) · [Fork](https://github.com/voyager67/Launchcrew/fork) · [Explore the code](https://github.com/voyager67/Launchcrew)

</div>

---

<div align="center">

**LaunchCrew** is an independent open-source project. It is not affiliated with or endorsed by OpenAI or the maintainers of similarly named projects. Product and organization names belong to their respective owners.

Released under the [MIT License](LICENSE).

<sub>Build with intent. Delegate with discipline. Ship with evidence.</sub>

</div>
