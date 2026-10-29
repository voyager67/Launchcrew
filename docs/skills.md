# LaunchCrew Skill Catalog

Each skill has one job, a specific trigger, a step-by-step procedure, guardrails, and an expected output. Load skills on demand; do not attach all skill files to every task.

| Skill | Best used when | Typical output |
|---|---|---|
| `constitution` | Create or refine project-wide principles, non-negotiable constraints, quality bars, and decision rules | Project charter |
| `specify` | Turn a feature, bug fix, refactor, or product idea into testable requirements, a technical design, a dependency-aware implementation plan, and acceptance scenarios before substantial coding | Requirements + design + plan |
| `validate` | Review requirements, designs, plans, or implementation artifacts for completeness, consistency, feasibility, testability, risk, scope drift, and readiness before proceeding | Readiness verdict |
| `implement` | Execute an approved spec or bounded engineering task in small slices, coordinate independent subagent work when available, verify each slice, detect drift, and preserve resumable progress | Tested slices + progress |
| `test` | Build and execute a risk-appropriate verification plan, reproduce failures, add regression coverage, and report trustworthy evidence for a change | Verification evidence |
| `review` | Independently review a diff or proposed implementation for correctness, security, regressions, performance, accessibility, and missing tests; return prioritized findings with evidence | Prioritized findings |
| `document` | Create or update accurate project documentation from actual code, tests, interfaces, and decisions; keep onboarding, API behavior, examples, and release notes synchronized | Accurate docs |
| `analyze` | Explain an unfamiliar repository or feature by mapping entry points, execution paths, data flow, dependencies, conventions, and unknowns before recommending changes | Evidence-backed code map |
| `refactor` | Improve code structure, duplication, naming, boundaries, or maintainability while preserving externally observable behavior and verifying equivalence | Behavior-preserving change |
| `debug` | Investigate a bug using reproducible evidence, competing root-cause hypotheses, narrow experiments, and a regression test before implementing the smallest reliable fix | Root cause + regression test |
| `product-discovery` | Clarify a product opportunity by identifying users, jobs-to-be-done, pain severity, current alternatives, constraints, scope, and measurable outcomes before committing to a build | Problem and validation brief |
| `research-brief` | Produce a source-backed technical or market research brief when the question requires current information, niche facts, comparisons, or decisions based on external evidence | Sourced research |
| `architecture-design` | Design or assess a system architecture by clarifying constraints, mapping boundaries and data flows, comparing options, and recording reversible decisions and operational risks | Options + decision |
| `security-audit` | Perform a practical security review of code or architecture, focusing on trust boundaries, authn/authz, secrets, injection, sensitive data, dependencies, and risk-ranked remediation | Risk-ranked findings |
| `performance-audit` | Investigate latency, throughput, memory, startup time, bundle size, query cost, or resource usage using measurements and bottleneck analysis before proposing optimizations | Measured bottlenecks |
| `accessibility-audit` | Review a product interface or user journey for accessibility barriers and provide specific, testable fixes covering keyboard, semantics, names, contrast, focus, motion, and assistive technology | Accessibility findings |
| `ui-ux` | Turn product requirements into understandable interface flows and interaction criteria, accounting for loading, empty, error, success, responsive, and accessible states | Flows + state criteria |
| `data-science` | Plan or execute a reproducible data analysis or machine-learning experiment with data provenance, leakage checks, baselines, metrics, uncertainty, and reproducible outputs | Reproducible experiment plan |
| `eval-design` | Design an evaluation strategy for an AI model, agent, prompt, or workflow, including representative cases, holdouts, rubrics, graders, failure taxonomy, and regression gates | Evaluation set + rubric |
| `incident-response` | Guide an incident investigation through scope confirmation, timeline, evidence preservation, safe containment, communication, recovery verification, and a blameless follow-up | Incident timeline + recovery |
| `release-manager` | Prepare a dependable software release by checking scope, versioning, tests, migrations, compatibility, release notes, rollout, monitoring, and rollback readiness | Release readiness |
| `growth-launch` | Prepare a credible open-source or product launch with a clear audience, differentiated promise, concise README/message, channel-specific drafts, and an ethical feedback loop | Launch and feedback plan |
| `startup-operations` | Help a founder or small team connect product priorities to measurable outcomes, operating cadence, resource constraints, risks, and evidence-based decisions | Operating metrics + decisions |

## Usage rules

- Pick the skill based on the job, not its name alone.
- Use one primary workflow and a specialist audit only when it adds value.
- Skills are instructions, not a guarantee that tools, files, tests, or external access exist.
- Preserve uncertainty and cite evidence for claims that materially affect the decision.


## Optional working styles

Communication profiles are separate from workflow skills: [The Sprint](../styles/the-sprint.md) for concise execution and [The Craft](../styles/the-craft.md) for explanatory engineering. They do not replace verification, approvals, or project policy.
