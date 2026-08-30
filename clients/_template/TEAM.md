# Engagement team

Activate only the roles required for the current stage. The human CPO is the
product decision owner but is not an AI agent.

| Role | Active? | Current assignment | Output path | Decision owner | Release condition |
|---|---|---|---|---|---|
| AI CEO | yes | Lead the engagement | `README.md` | AI CEO | Engagement closed |
| Human CPO | yes | Lead product | `DECISION_LOG.md` | Human CPO | Engagement closed |
| Product Operations Manager | yes | Maintain product operating record | `DECISION_LOG.md` | Human CPO | Product closeout complete |
| [AI role] | [yes/no] | [bounded assignment] | [file] | [owner] | [completion test] |

## Optional Board role

| Role | Active? | Governance trigger | Output path | Authority boundary | Release condition |
|---|---|---|---|---|---|
| Independent Board Director, Product and Strategy | no | [trigger or none] | `BOARD_ADVISORY.md` | Advisory only; no line authority over CPO | Memorandum accepted into Board record |

## Coordination rules

- One agent owns each output file at a time.
- Independent read-only research can run in parallel.
- Product decisions cannot be delegated.
- The Board advisor is not part of routine staffing.
- Update this table when a role joins or leaves.
