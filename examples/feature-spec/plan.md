# Implementation plan — Invitation-based sign-up

| Slice | Deliverable | Depends on | Acceptance evidence |
|---|---|---|---|
| S-001 | Schema/model and expiry/status definitions | None | Unit tests cover status transitions and uniqueness |
| S-002 | Authorized invitation creation endpoint/service | S-001 | Admin success and unauthorized denial tests |
| S-003 | Token acceptance with atomic consumption | S-001 | Success, expired, revoked, repeated, and concurrent use tests |
| S-004 | Audit event and redaction | S-002, S-003 | Event assertions and no-token-in-logs check |
| S-005 | UI, email delivery, and integrated verification | S-002, S-003, S-004 | End-to-end journey with provider test mode |

Before implementation, verify database and identity constraints in the target repository. Do not copy this plan literally if the project already has an invitation subsystem.
