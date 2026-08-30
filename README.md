# Greyshore Product Partners

Greyshore Product Partners is an AI-native digital-product consultancy with one
human Chief Product Officer and a 30-role AI organization assembled by
engagement.

The firm handles websites, mobile applications, SaaS products, platforms, and
internal tools. Its operating model covers opportunity development, product
strategy, research, design, engineering, quality, market readiness, and
engagement closeout. AI engineers can deliver locally runnable MVPs; the human
CPO leads product and never writes code.

> **Independent speculative work:** A real organization named in an engagement
> is a target account, not a Greyshore client. It did not request, review, or
> endorse the work. No outreach or external representation is permitted.

## Open the company

Open this repository in Codex and use:

```text
CEO, begin company operations. Have Sales identify three target-account
opportunities from current public market signals. Qualify them with Revenue,
Finance, Technology, and Legal, select the strongest opportunity, create its
isolated account workspace, and staff the smallest team required. Brief me as
the CPO when a product decision is ready. Route every non-product task to the
accountable executive or specialist. Do not perform outreach or imply that the
target organization is a client.
```

Codex reads [`AGENTS.md`](AGENTS.md) before working. That file defines company
authority, Board oversight, product decision rights, delegation, evidence,
external-action limits, and account isolation.

## Governance

The Board oversees the CEO. An Independent Board Director for Product and
Strategy serves as a seasoned product advisor to the CPO at major portfolio and
governance decisions. The director does not manage routine product work or sit
between the CEO and CPO.

The AI CEO manages the company. The human CPO and AI CTO are peer executives who
report to the CEO. The CPO owns product vision, users, problems, outcomes,
strategy, priorities, experience direction, requirements, roadmap, metrics, and
product acceptance. AI executives own the remaining company functions.

- [`company/ORG_CHART.md`](company/ORG_CHART.md) — reporting lines, Board role,
  and executive accountability
- [`company/ROLE_CATALOG.md`](company/ROLE_CATALOG.md) — all 30 AI roles and
  activation criteria
- [`.codex/agents/`](.codex/agents/) — Codex custom-agent profiles

## How an engagement runs

1. Sales identifies target accounts from current public evidence.
2. The CRO, CFO, CTO, and Legal and Risk Advisor qualify the opportunity.
3. The CEO selects an account and assembles a small cross-functional team.
4. The CPO makes product decisions; specialists supply evidence, alternatives,
   recommendations, and execution.
5. Product Operations records decisions and keeps product artifacts aligned.
6. After the CPO and CTO approve the plan, AI engineers build the MVP.
7. The CPO accepts product behavior; the CTO accepts technical readiness.
8. Revenue and Operations prepare internal market-readiness and closeout
   materials. Nothing is published or represented as client work.

The Board product advisor participates only when the CPO requests counsel or a
major product, portfolio, conflict, or governance matter reaches the Board.

## Account workspace

Every engagement is isolated under `clients/<engagement-slug>/`. Copy
[`clients/_template/`](clients/_template/) to begin. Each workspace contains:

- the internal opportunity brief and source log;
- team assignments and executive accountability;
- research, strategy, PRD, roadmap, and metrics;
- product and executive decision records;
- design and engineering workspaces;
- optional Board product-advisory memoranda; and
- engagement closeout and company-level implications.

The repository remains the source of truth when a team uses external tools.
Export or summarize material Figma, Jira, or analytics work into the account
workspace.

## Free-only operating stack

The firm uses product tools requested in current PM roles without paid seats:

- GitHub Issues/Projects and Markdown for durable planning and documentation;
- Figma Starter and FigJam, with Penpot as the open-source design alternative;
- Jira, Jira Product Discovery, and Confluence free plans, with Plane and
  repository artifacts as alternatives;
- Dovetail Free or repository templates for research synthesis;
- PostHog's free tier for analytics;
- DuckDB and Metabase Open Source for SQL and dashboards;
- Hoppscotch for API exploration;
- Formbricks for surveys; and
- Excalidraw and Mermaid for whiteboards and diagrams.

See [`playbooks/TOOLS.md`](playbooks/TOOLS.md) for current plan limits and
substitutions. No engagement may depend on a paid plan or expiring trial.

## Operating references

- [`playbooks/OPERATING_GUIDE.md`](playbooks/OPERATING_GUIDE.md) — start and run
  the company
- [`playbooks/ENGAGEMENT_LIFECYCLE.md`](playbooks/ENGAGEMENT_LIFECYCLE.md) —
  qualification, delivery, acceptance, and closeout gates
- [`playbooks/BOARD_GOVERNANCE.md`](playbooks/BOARD_GOVERNANCE.md) — Board
  oversight and product-advisor protocol
- [`playbooks/PORTFOLIO_STRATEGY.md`](playbooks/PORTFOLIO_STRATEGY.md) — the
  firm's account and product-portfolio progression
- [`docs/USING_CODEX.md`](docs/USING_CODEX.md) — company-role delegation in Codex

## Validate the repository

```bash
python3 scripts/validate_repo.py
```

The validator checks required operating files, agent-profile count and schema,
account-template structure, disclosure language, internal links, and prohibited
company framing.

## Public-repository note

This repository is public but has no license. Public visibility does not grant
permission to copy, modify, or redistribute its contents. Never commit private
information, real credentials, or claims that a target account is a client.
