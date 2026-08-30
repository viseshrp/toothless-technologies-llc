# Free and open-source product tool stack

This stack is designed for one human CPO and AI agents that work primarily in
the repository. It reflects tool categories repeatedly requested in current PM
job postings while avoiding paid plans.

Plan details change. The links and limits below were checked on 2026-08-30.
Before assigning an external tool, verify its current official plan page. If a
free feature disappears, use the listed fallback.

## Default stack

| Product job to practice | Recognized free tool | Free/open-source fallback | Repository artifact |
|---|---|---|---|
| Backlog and delivery | Jira Free | Plane Community Edition or GitHub Issues/Projects | `ROADMAP.md`, issues, decision log |
| Product discovery and prioritization | Jira Product Discovery Free | GitHub Projects plus Markdown | `PRODUCT_STRATEGY.md`, opportunity table |
| Team knowledge | Confluence Free | Markdown in this repository | All engagement documents |
| Interface design and whiteboarding | Figma Starter and FigJam | Penpot, Excalidraw, Mermaid | exported image/link plus design rationale |
| Research repository | Dovetail Free | `RESEARCH.md` and local evidence tables | `RESEARCH.md` |
| Product analytics and experiments | PostHog free tier | DuckDB plus Metabase Open Source | `METRICS.md`, queries, dashboard specification |
| API exploration | Hoppscotch | `curl` plus saved examples | API notes under `delivery/` |
| Surveys and feedback | Formbricks open-source core | Markdown/CSV synthetic responses | research plan and labeled synthetic dataset |

## Free-plan guardrails

### GitHub

Use the public repository, Issues, Projects, pull requests, and Actions as the
durable operating system. Agents do not need GitHub user accounts. Keep product
decisions in Markdown even when an issue tracks the work.

- Official plans: <https://github.com/pricing>

### Figma Starter and FigJam

Use the free Starter plan for basic design and whiteboarding practice. Only the
human CPO needs an account. Export a PNG/PDF or add a share link plus a written
design rationale to the engagement folder.

Do not depend on Dev Mode: Figma's Starter-plan documentation says it is not
included. If the Starter limits interrupt the exercise, use Penpot.

- Pricing: <https://www.figma.com/pricing/>
- Starter plan: <https://help.figma.com/hc/en-us/articles/13838684089751-Starter-plan-overview>
- Penpot, open source under MPL-2.0: <https://github.com/penpot/penpot>

### Jira, Jira Product Discovery, and Confluence

Use these only when the CPO is specifically practicing employer-recognized
workflows. As checked, Jira Free and Confluence Free support up to 10 users, and
Jira Product Discovery Free supports up to 3 creators. One human account fits
the exercise; agents should not consume seats.

- Jira pricing: <https://www.atlassian.com/software/jira/pricing>
- Jira Product Discovery pricing: <https://www.atlassian.com/software/jira/product-discovery/pricing>
- Confluence pricing: <https://www.atlassian.com/software/confluence/pricing>
- Plane open-source edition: <https://plane.so/open-source>

### Dovetail

The free plan is useful for learning research-repository concepts but is limited
to one project and one channel as checked. Work on one practice case at a time
or keep the full evidence trail in `RESEARCH.md`.

- Pricing: <https://dovetail.com/pricing/>

### PostHog

Use the cloud free tier for a small local practice product only if the CPO wants
hands-on analytics. Do not send real personal data. The open-source self-hosted
edition is possible, but PostHog recommends Cloud for most teams and warns that
self-hosting requires infrastructure and security expertise. The default
fallback is a synthetic local dataset analyzed with DuckDB.

- Product and pricing: <https://posthog.com/>
- Open-source self-hosting caveat: <https://posthog.com/docs/self-host/open-source/disclaimer>

### DuckDB and Metabase

DuckDB provides local SQL practice against CSV, JSON, and Parquet data without a
server. Metabase Open Source can turn a local dataset into a dashboard when the
visualization itself is part of the learning goal. Use synthetic data only.

- DuckDB, MIT licensed: <https://github.com/duckdb/duckdb>
- Metabase Open Source: <https://www.metabase.com/start/oss/>

### Hoppscotch

Use Hoppscotch's web, desktop, or local open-source tool to understand HTTP APIs
without requiring Postman. Save sanitized requests and explanations in the
engagement folder; never paste secrets.

- Hoppscotch, MIT licensed: <https://github.com/hoppscotch/hoppscotch>

### Formbricks

Use Formbricks only with synthetic respondents in this studio. Its fully
functional core is AGPLv3, while the same repository also contains separately
licensed enterprise features. The Markdown research templates remain the
zero-setup fallback.

- Formbricks repository and license explanation: <https://github.com/formbricks/formbricks>

### Excalidraw and Mermaid

Use Excalidraw for free-form diagrams and Mermaid for diagrams that should stay
reviewable as text in Git. Both are open-source and can work without a paid
workspace.

- Excalidraw, MIT licensed: <https://github.com/excalidraw/excalidraw>
- Mermaid, MIT licensed: <https://github.com/mermaid-js/mermaid>

## Tools seen in current PM postings but not required here

The research also found references to Notion, Miro, Asana, Trello, Tableau,
Looker, Mixpanel, Amplitude, Google Analytics, Celonis, Signavio, Adobe
Analytics, and Postman. They represent useful categories, not required
purchases. The studio practices the underlying competency with the free stack:

- collaboration and documentation;
- discovery and prioritization;
- wireframing and prototyping;
- product analytics, experimentation, SQL, and dashboards;
- API and technical literacy; and
- clear stakeholder communication.

Do not collect tools for their own sake. Choose a tool only when it makes the
current product decision, artifact, or learning objective better.
