# Requirements — Invitation-based sign-up

## Problem

A workspace administrator needs to invite a person to join a workspace without enabling open self-service registration.

## Scope

- Invitee receives a time-limited token.
- Token use is single-use and bound to the intended workspace/email policy.
- Acceptance records an audit event.
- Expired, revoked, malformed, and previously used invitations fail safely.

## Non-goals

- Designing the entire identity provider integration.
- Password policy changes unrelated to invitation acceptance.
- Sending real email until an authorized provider and sender are configured.

## Requirements

| ID | Requirement | Acceptance criteria |
|---|---|---|
| REQ-001 | Authorized administrators can create an invitation | Unauthorized users receive a safe denial and no invitation is created |
| REQ-002 | Invitation tokens expire | Expired token cannot create membership |
| REQ-003 | Token use is single-use | Concurrent/repeated use does not create duplicate membership |
| REQ-004 | Successful acceptance is auditable | Event contains actor/workspace/time and avoids storing the raw secret token |
| REQ-005 | Failures are safe | Error response does not disclose whether unrelated accounts exist |
