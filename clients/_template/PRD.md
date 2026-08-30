# Product requirements document

## Approval

- **Product owner:** Human CPO
- **Product status:** [draft | approved | revise]
- **Product approval date:** [date]
- **Technical owner:** AI CTO
- **Technical status:** [draft | approved | revise]
- **Technical approval date:** [date]

Engineering must not begin until both statuses are `approved`.

## Product outcome

[What user outcome should this MVP create or test?]

## Target user and problem

[Link to the approved strategy decision.]

## MVP hypothesis

We believe [capability] for [target user] will produce [outcome]. We will gain
confidence when [observable threshold], while [guardrail] does not worsen.

## In scope

1. [User-visible behavior and why it is needed]

## Out of scope

1. [Explicit deferral and why]

## User flow

[Link to or describe the approved flow.]

## Requirements and acceptance criteria

| ID | User need | Requirement | Acceptance criterion | Priority | Evidence / rationale |
|---|---|---|---|---|---|
| R-001 | [need] | [behavior, not implementation] | Given / When / Then | [must/should/could] | [source or decision] |

## Experience requirements

- **Accessibility:** [requirements]
- **Content:** [requirements]
- **Error and empty states:** [requirements]
- **Privacy and trust:** [requirements]

## Measurement

[Events, properties, outcome metric, guardrails, and link to `METRICS.md`.]

## Product risks and open questions

| Question or risk | Owner | Must resolve before | Status |
|---|---|---|---|
| [item] | [role] | [gate] | [open/closed] |

## Product review protocol

The engineering team should demo working behavior. The CPO evaluates the
approved outcomes and acceptance criteria, not code implementation details.
