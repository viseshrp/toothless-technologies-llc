# PM job-market and tool research — 2026-08-30

## Research question

Which practical tools and adjacent capabilities appear in current
product-management job postings, and which free or open-source tools can
Greyshore use to cover those operating needs?

This is a directional snapshot, not a statistically representative labor-market
analysis. Postings can change or expire. Sources were accessed on 2026-08-30.

## Current posting sample

| Employer / role | Evidence observed in the posting | Source |
|---|---|---|
| SAP — Senior Product Management Specialist | Jira, Confluence, Mural, Figma, Lucidchart; Tableau and analytics tools; Python, YAML, and SQL; validation and usability | [SAP Careers](https://jobs.sap.com/job/Palo-Alto-Senior-Product-Management-Specialist-CA-94304/1427137433/) |
| Karya — Associate Product Manager | Jira, Notion, Figma, SQL as a plus, APIs and data flows, Agile/Scrum, end-to-end lifecycle | [Karya on Greenhouse](https://job-boards.greenhouse.io/karya/jobs/5205891008) |
| ToolJet — Associate Product Manager, Technical | Jira, Confluence, Figma, Postman, SQL, REST APIs, product analytics; JavaScript/Python as a plus | [ToolJet on Wellfound](https://wellfound.com/jobs/4465216-associate-product-manager-technical) |
| Hop — Senior Product Manager | Jira, Confluence, Tableau, SQL | [Hop on Lever](https://jobs.lever.co/hophr/54b5cdd0-dc1b-43eb-b91f-79bcf5ee8e2f) |
| Fiserv — Product Management Associate | Jira, Confluence, Figma, Miro, SQL, and AI tools | [Fiserv listing on Indeed](https://www.indeed.com/viewjob?jk=daf260ef807f5d98) |
| Avida — Associate Product Manager | SQL, dashboards, Figma, APIs and architecture, discovery and user interviews | [Avida on Ashby](https://jobs.ashbyhq.com/avida/0b436257-9455-4e8f-a414-2b2b0425e85a) |
| SignalFire portfolio — Staff Product Manager | Jira/Asana/Trello/Notion; Amplitude/Mixpanel/Google Analytics; Figma; Slack/Confluence/Miro/Loom; SQL/Looker/Tableau | [SignalFire talent network](https://jobs.signalfire.com/companies/signalfire/jobs/88793548-staff-product-manager-vc-backed-startups) |
| DXC — Senior Product Manager, Knowledge & Data | Discover/Define/Design/Deliver; Confluence as system of record; Jira execution; AI-assisted prototyping | [DXC Careers](https://dxctechnology.wd1.myworkdayjobs.com/en-US/dxcjobs/job/USA---NY---NEW-YORK/Senior-Product-Manager-Knowledge-Data_51584348-1) |

Atlassian's Associate Product Manager program emphasizes shipping,
problem-solving, empathy, and communication rather than a list of tools:
[Atlassian APM](https://www.atlassian.com/company/careers/graduates/apm).

## Findings

Across this sample, the strongest recurring competency clusters were:

1. **Planning and product operations:** Jira, Confluence, backlog/roadmap
   management, Agile collaboration, and clear written artifacts.
2. **Design and discovery:** Figma, whiteboarding, user interviews, usability,
   prototyping, and close work with design.
3. **Data fluency:** SQL, dashboards, product analytics, experimentation, and
   turning evidence into decisions.
4. **Technical literacy:** APIs, data flows, architecture conversations, and
   tools such as Postman. Coding sometimes appears as a plus, not as the core PM
   responsibility.
5. **Leadership:** communication, stakeholder alignment, prioritization,
   lifecycle ownership, empathy, and judgment.

Greyshore should select tools for the underlying product capability rather than
vendor-specific button sequences. Tool fluency matters, but the transferable
product decision and operating artifact matter more.

## Operating implications

- Use Figma and FigJam because design collaboration appears repeatedly,
  but provide Penpot and repo-native flows so a paid plan is never required.
- Use Jira, Jira Product Discovery, and Confluence free plans when
  useful, while keeping GitHub and Markdown as the durable source of truth.
- Use DuckDB for SQL and Metabase Open Source for dashboards. This covers the
  data fluency postings request without a commercial BI license.
- Use PostHog's free tier or synthetic event data for product instrumentation
  and experimentation.
- Use Hoppscotch and plain-language architecture artifacts for API work;
  the human CPO does not code.
- Use Dovetail Free or repository templates for research planning and synthesis,
  and use Formbricks only with labeled synthetic survey data.
- Require clear communication, prioritization, judgment, and evidence in every
  engagement; software does not replace those responsibilities.

## Free and open-source verification sources

- [Figma pricing](https://www.figma.com/pricing/) and [Starter-plan details](https://help.figma.com/hc/en-us/articles/13838684089751-Starter-plan-overview)
- [Jira pricing](https://www.atlassian.com/software/jira/pricing), [Jira Product Discovery pricing](https://www.atlassian.com/software/jira/product-discovery/pricing), and [Confluence pricing](https://www.atlassian.com/software/confluence/pricing)
- [Dovetail pricing](https://dovetail.com/pricing/)
- [Penpot repository](https://github.com/penpot/penpot)
- [Plane open-source edition](https://plane.so/open-source)
- [PostHog](https://posthog.com/) and its [self-hosting caveat](https://posthog.com/docs/self-host/open-source/disclaimer)
- [DuckDB repository](https://github.com/duckdb/duckdb)
- [Metabase Open Source](https://www.metabase.com/start/oss/)
- [Hoppscotch repository](https://github.com/hoppscotch/hoppscotch)
- [Formbricks repository](https://github.com/formbricks/formbricks)
- [Excalidraw repository](https://github.com/excalidraw/excalidraw)
- [Mermaid repository](https://github.com/mermaid-js/mermaid)

## Review cadence

Recheck the posting sample and free-plan limits every six months or before an
engagement relies on an external feature. Update the access date, describe what
changed, and preserve the historical snapshot.
