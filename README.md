# CPO Practice Studio

An AI-staffed, fictional digital-product consultancy where one human CPO learns
to lead product work from discovery through a working MVP.

> **Educational simulation:** No company named in this repository is a client.
> Scenarios may use real companies and public facts, but the work is fictional,
> was not requested by the named company, and does not imply affiliation.

## Who this is for

The human learner is the Chief Product Officer. She practices product judgment
and leadership; she does not code or run sales, finance, operations, legal, or
technical delivery. An AI CEO leads the simulated company. The human CPO and an
AI CTO are peer executives reporting to the CEO, supported by 28 additional AI
roles that are activated only when needed.

The studio supports websites, mobile apps, SaaS products, platforms, and
internal tools. A case can stop after strategy or continue through a locally
runnable MVP built and tested by AI engineers.

## Start here

Open this repository in Codex and use:

```text
CEO, start my first practice engagement. Have Sales create three fictional
opportunities involving real companies using current public evidence. Choose
the opportunity that will teach me the most, staff only the roles we need, and
brief me as the CPO. Coach me one product decision at a time. Do not ask me to
code or perform non-product company work.
```

Codex reads [`AGENTS.md`](AGENTS.md) before working. That file is the operating
contract for authority, coaching, evidence, delegation, safety, and client
isolation.

## What a practice engagement feels like

1. AI Sales finds public market signals and drafts fictional opportunities.
2. The AI CEO selects a case and assembles a small cross-functional team.
3. The Product Coach explains each stage and asks one focused question at a
   time.
4. The CPO makes product decisions: user, problem, outcomes, strategy,
   priorities, scope, experience, requirements, metrics, and readiness.
5. Specialists do the surrounding work and return evidence and options.
6. After the CPO approves the product plan, AI engineers can build the MVP.
7. The CPO reviews the product; the CTO owns technical quality.
8. A closing review shows what the CPO practiced and what to improve next.

## Company structure

- [`company/ORG_CHART.md`](company/ORG_CHART.md) — reporting lines and decision
  rights
- [`company/ROLE_CATALOG.md`](company/ROLE_CATALOG.md) — all 30 AI roles and when
  to activate them
- [`.codex/agents/`](.codex/agents/) — Codex custom-agent profiles

The entire AI workforce is not active at once. A typical discovery stage might
use the CEO, Product Coach, Market Researcher, and User Researcher. A build stage
might add the CTO, Engineering Manager, two engineers, QA, and Security.

## Engagement workspace

Every case is isolated under `clients/<engagement-slug>/`. Copy
[`clients/_template/`](clients/_template/) to begin. The template contains:

- the fictional brief and source log;
- a product decision log;
- discovery, strategy, PRD, roadmap, and metrics artifacts;
- design and delivery workspaces;
- a coaching log and end-of-case review.

The repository is the source of truth even when an exercise uses an external
tool. Export or summarize important Figma, Jira, or analytics work back into the
case folder.

## Free-only tool policy

The curriculum practices tools that appear in current PM job postings without
requiring paid seats. The default stack combines free plans with open-source
fallbacks:

- GitHub Issues/Projects and Markdown for durable planning and documentation;
- Figma Starter and FigJam, with Penpot as the open-source design fallback;
- Jira, Jira Product Discovery, and Confluence free plans, with Plane and repo
  artifacts as fallbacks;
- Dovetail Free or repository templates for research synthesis;
- PostHog's free tier for analytics practice;
- DuckDB and Metabase Open Source for SQL and dashboards;
- Hoppscotch for API exploration;
- Formbricks for surveys; and
- Excalidraw and Mermaid for whiteboards and diagrams.

See [`playbooks/TOOLS.md`](playbooks/TOOLS.md) for plan limits, substitutions,
and evidence. No exercise may depend on a paid plan or expiring trial.

## Practice sequence

Use [`playbooks/START_HERE.md`](playbooks/START_HERE.md) for the first case and
[`playbooks/ENGAGEMENT_LIFECYCLE.md`](playbooks/ENGAGEMENT_LIFECYCLE.md) for all
stage gates. [`playbooks/COACHING.md`](playbooks/COACHING.md) defines how agents
teach without taking product judgment away from the CPO.

## Validate the repository

```bash
python3 scripts/validate_repo.py
```

The validator checks the operating files, agent-profile count and schema,
template structure, and required simulation language.

## Public-repository note

This repository is public for educational viewing. It contains no license, so
public visibility alone does not grant permission to copy, modify, or
redistribute its contents. Never commit private information or real credentials.
