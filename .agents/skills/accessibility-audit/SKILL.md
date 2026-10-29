---
name: accessibility-audit
description: "Review a product interface or user journey for accessibility barriers and provide specific, testable fixes covering keyboard, semantics, names, contrast, focus, motion, and assistive technology."
license: MIT
---

# Accessibility audit workflow

1. Identify the interface, target user journeys, supported platforms, and available source/runtime evidence.
2. Inspect semantic structure, accessible names, roles/states, keyboard navigation, visible focus, focus order, form labels/errors, headings/landmarks, status announcements, contrast, zoom/reflow, target sizes, and motion/animation behavior.
3. Cover key states: loading, empty, validation errors, dialogs, menus, disabled controls, dynamic updates, and success/failure feedback.
4. Use automated checks as a starting point, not a complete audit. Combine source review, keyboard-only walkthrough, browser/assistive-technology checks where available, and user-impact reasoning.
5. Map findings to WCAG concepts when confident. Note version/level and the limit of what was tested; do not claim certification.
6. Prioritize blockers that prevent task completion, then high-friction barriers. Include clear repro steps and recommended fixes.
7. Validate changed behavior in the same journey, including keyboard focus and error announcements.

## Output

- Coverage and limitations
- Findings by severity and user impact
- Steps to reproduce, affected state, criterion/concept, and fix
- Regression test ideas
- Items requiring manual assistive-technology validation

## Guardrails

Do not label a product “fully accessible” based on automated scans alone. Avoid making assumptions about a person's disability or preferred assistive technology.
