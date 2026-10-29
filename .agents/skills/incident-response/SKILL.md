---
name: incident-response
description: "Guide an incident investigation through scope confirmation, timeline, evidence preservation, safe containment, communication, recovery verification, and a blameless follow-up."
license: MIT
---

# Incident response workflow

## First: protect people and systems

1. Confirm the incident, affected service/assets, severity, impact window, and who has authority to make changes.
2. Preserve relevant logs/metrics/events and a timestamped timeline. Avoid exposing secrets or personal data in shared channels.
3. Start with reversible, least-risk containment. Ask before production changes, data deletion, account suspension, or other material side effects unless an established emergency policy explicitly authorizes them.
4. Identify symptoms, blast radius, recent changes, dependency health, and known mitigations. Keep observations separate from hypotheses.
5. Delegate independent investigations only when the incident commander and ownership are clear; do not let responders make conflicting changes to shared systems.
6. Communicate status with known impact, current action, owner, and next update time. Do not speculate publicly or overstate recovery.
7. Verify recovery against user-visible indicators and error rates, then monitor for recurrence.
8. Run a blameless review: detection gaps, contributing conditions, effective mitigations, and prioritized follow-ups with owners/dates.

## Output

- Current status and severity rationale
- Scope / impact and timeline
- Confirmed facts vs hypotheses
- Actions taken, approvals, and evidence
- Recovery checks and residual risk
- Blameless follow-up items

## Guardrails

Do not invent an incident timeline, claim systems recovered without metrics, destroy evidence, or execute unapproved changes. Follow the organization's runbooks and escalation paths.
