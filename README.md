# Toothless Technologies LLC

Toothless Technologies LLC is an AI-native digital-product consultancy with one
human Chief Product Officer and a 30-role AI organization assembled by
engagement.

The firm handles websites, mobile applications, SaaS products, platforms, and
internal tools. Its operating model covers opportunity development, product
strategy, research, design, engineering, quality, market readiness, and
engagement closeout. AI engineers can deliver locally runnable MVPs; the human
CPO leads product and never writes code.

> **Independent speculative work:** A real organization named in an engagement
> is a target account, not a client of Toothless Technologies LLC. It did not
> request, review, or endorse the work. No outreach or external representation
> is permitted.

> **Name and legal status:** Toothless Technologies LLC is the operating name
> selected for this repository. The repository does not claim that an LLC has
> been formed, registered, licensed, or is in good standing. Confirm name
> availability, trademark risk, and formation requirements in the relevant
> jurisdiction before using the name for real business.

## Start in three steps

1. Open the ChatGPT desktop app, choose **Open folder**, and select this cloned
   repository (`toothless-technologies-llc`).
2. Read [`OPERATIONS.md`](OPERATIONS.md) to see exactly where company work last
   stopped, then choose **Codex**, start a **New chat**, and paste the launch
   prompt below.
3. Stay in that chat for the engagement. The CEO will resume the recorded next
   action, assemble the AI team, and return when the CPO has a product decision
   to make.

No command line, coding, or manual agent setup is required for the CPO. Codex
reads [`AGENTS.md`](AGENTS.md) and the 30 project agent profiles automatically
when the repository is opened.

### First launch prompt

Paste this exactly:

```text
CEO, begin company operations. Have Sales identify three target-account
opportunities from current public market signals. Qualify them with Revenue,
Finance, Technology, and Legal, select the strongest opportunity, create its
isolated account workspace, and staff the smallest team required. Brief me as
the CPO when a product decision is ready. Route every non-product task to the
accountable executive or specialist. Read OPERATIONS.md first. Create or update
the appropriate functional project card before each team works, and update all
affected team projects before pausing. Run each assigned task through the exact
project-scoped role profile so its configured model is used; never emulate a
named role in the lead session. Do not perform outreach or imply that the target
organization is a client.
```

The first useful result should be a CEO brief containing the selected target
account, supporting public evidence, qualification, active roles, and exactly
one product decision for the CPO. If the CEO assigns non-product work to her,
reply: `This is not product work. Route it to the accountable company role and
return when product authority is required.`

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

## Functional Kanban projects

The company has 12 separate public GitHub Projects: Executive & Portfolio,
Product Management, Research, Design & Accessibility, Development &
Architecture, Reliability & Security, Testing & Quality, Sales, Marketing &
Customer Success, Operations, Finance, and Legal & Risk.

[`company/TEAM_PROJECTS.md`](company/TEAM_PROJECTS.md) contains every board link
and the complete 30-role assignment. Each work item has one owning team; linked
cards express cross-team dependencies. `OPERATIONS.md` records the company-wide
pause point, and each engagement's `PROJECT_TRACKER.md` indexes its cards across
the team projects. The CPO does not administer boards.

## Account workspace

Every engagement is isolated under `clients/<engagement-slug>/`. Copy
[`clients/_template/`](clients/_template/) to begin. Each workspace contains:

- the internal opportunity brief and source log;
- the cross-team project tracker and pause point;
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
- [`playbooks/PROJECT_BOARDS.md`](playbooks/PROJECT_BOARDS.md) — functional
  projects, card ownership, cross-team dependencies, and handoffs
- [`docs/USING_CODEX.md`](docs/USING_CODEX.md) — company-role delegation in Codex

## Validate the repository

```bash
python3 scripts/validate_repo.py
```

The validator checks required operating files, agent-profile count and schema,
functional-project count and one-project-per-agent assignment, account-template
structure, disclosure language, internal links, and prohibited company framing.

## Public-repository note

This repository is public but has no license. Public visibility does not grant
permission to copy, modify, or redistribute its contents. Never commit private
information, real credentials, or claims that a target account is a client.
