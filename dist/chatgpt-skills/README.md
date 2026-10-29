# LaunchCrew — ChatGPT skill uploads

This folder contains one ZIP per LaunchCrew skill. Upload **one skill ZIP at a time** in the ChatGPT Skills interface when that feature is available on your account/workspace.

## Suggested starting set

1. `specify.zip` — turn a feature request into requirements, design, and a plan.
2. `validate.zip` — catch missing, contradictory, or untestable requirements.
3. `implement.zip` — deliver small, verifiable implementation slices.
4. `test.zip` — prove behavior and report actual test evidence.
5. `review.zip` — independently inspect changes for correctness and risk.

Add the rest as relevant; enabling every workflow at once is not required. These ZIPs contain portable instructions only. They do not grant repository access or tools, install Codex-specific agent configurations, or override account/workspace policy.

To regenerate from the source skills, run `python3 scripts/package_chatgpt_skills.py` from the repository root. To check the current archives, run `python3 scripts/package_chatgpt_skills.py --check`.

See [`../../docs/chatgpt.md`](../../docs/chatgpt.md) for setup and the Projects fallback.
