# Acceptance scenarios — Invitation-based sign-up

| ID | Given | When | Then |
|---|---|---|---|
| ACC-001 | Admin has permission and recipient policy is valid | Admin creates invite | One active invite is created and no raw token is written to logs |
| ACC-002 | User lacks invite-management permission | User attempts to create invite | Request is denied and no invite is created |
| ACC-003 | Invitation has expired | Invitee accepts token | Membership is not created |
| ACC-004 | Invitation has already been consumed | Invitee reuses token | No duplicate membership is created |
| ACC-005 | Two requests race to consume one token | Both requests attempt acceptance | At most one request creates membership; the other fails safely or returns idempotent success |
| ACC-006 | Token belongs to a different workspace/recipient | Token is submitted outside policy | Acceptance is denied without disclosing unrelated account information |
