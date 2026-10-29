# Technical design — Invitation-based sign-up

## Proposed flow

1. An authorized admin requests an invite.
2. Server creates a cryptographically random token, stores only a verifier/hash where supported, expiry, workspace, intended recipient policy, status, and creator.
3. Delivery is queued only after the provider and send action are explicitly configured.
4. Invitee submits the token; server validates expiry, status, recipient binding, and workspace constraints.
5. Membership creation and token consumption happen atomically or with an equivalent idempotent transaction.
6. An audit event is written without the raw token or unnecessary personal data.

## Risks

- Race condition on concurrent acceptance.
- Token leakage via logs, referrers, analytics, or copied links.
- Cross-workspace authorization failures.
- Email delivery retries causing duplicate sends.

## Decisions to verify against the actual codebase

- Existing identity/session model.
- Database transaction support and membership uniqueness constraints.
- Existing mail queue, logging, and audit schema.
- Email case normalization and invitee changes.
