---
name: security-audit
description: "Perform a practical security review of code or architecture, focusing on trust boundaries, authn/authz, secrets, injection, sensitive data, dependencies, and risk-ranked remediation."
license: MIT
---

# Security audit workflow

1. Confirm scope, assets, threat actors, trust boundaries, data sensitivity, deployment context, and authorized testing boundaries.
2. Inspect changed code and adjacent paths for authentication, authorization, input validation, output encoding, injection, SSRF, path traversal, deserialization, insecure defaults, secrets, logging, cryptography, and dependency risk where relevant.
3. Trace permissions end-to-end: user → API → service → data store / tool → external side effect. Check deny-by-default behavior and object-level authorization.
4. Examine failure paths, retries, caches, uploads, webhooks, background jobs, and multi-tenant boundaries where applicable.
5. Distinguish confirmed exploit paths from hardening suggestions and speculative concerns. Never run destructive probes or test systems outside the approved scope.
6. Rank findings by impact, exploitability, affected assets, and confidence. Include a practical reproduction path that does not expose live secrets.
7. Recommend smallest safe mitigations and regression tests. Verify fixes against the original risk.

## Output

- Scope and limitations
- Threat model summary
- Findings: severity, evidence/location, attack preconditions, impact, remediation
- Positive controls / missing controls
- Prioritized fix plan and regression checks

## Guardrails

Do not print secrets into reports. Do not turn an audit request into unauthorized exploitation, credential harvesting, persistence, or destructive testing. Preserve evidence and request approval before active tests with material side effects.
