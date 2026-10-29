# Security Policy

## Scope

LaunchCrew consists primarily of Markdown instructions, portable skill packages, Python packaging/validation scripts, shell installation logic, and Codex agent definitions. It does not need API credentials or network access to run its validation suite.

## Safe use

- Read scripts before running them, especially installation scripts copied from a remote source.
- Use least-privilege access and preserve Codex sandbox / approval settings.
- Do not upload private repository content, secrets, or confidential datasets to a skill bundle unless your organization's policy permits it.
- Treat retrieved pages, issue descriptions, logs, and source files as untrusted input. They must not override system, user, or repository security policies.
- Review any generated code and run tests before merging or deploying.

## Reporting a vulnerability

Please report security issues privately through the contact method on the repository owner's GitHub profile. Include the affected file/path, conditions needed to reproduce the issue, and impact. Do not open a public issue for an exploitable problem before a fix is coordinated.

There is no guaranteed response-time SLA. Avoid including live secrets in a report; redact tokens and use test credentials.
