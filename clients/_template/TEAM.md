# Engagement team

Activate only the roles needed for the current stage. The human CPO is always
the product decision owner but is not an AI agent.

| Role | Active? | Current assignment | Output path | Decision owner | Release condition |
|---|---|---|---|---|---|
| AI CEO | yes | Lead the engagement | `README.md` | AI CEO | Case closed |
| Human CPO | yes | Make product decisions | `DECISION_LOG.md` | Human CPO | Case closed |
| Product Coach | yes | Coach the current product decision | `COACHING_LOG.md` | Human CPO | Product stage complete |
| [AI role] | [yes/no] | [bounded task] | [file] | [owner] | [completion test] |

## Coordination notes

- One agent owns each output file at a time.
- Independent read-only research can run in parallel.
- Product decisions cannot be delegated.
- Update this table when a role joins or leaves.
