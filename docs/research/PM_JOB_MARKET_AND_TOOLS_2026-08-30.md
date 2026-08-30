# PM job-market and tool research — 2026-08-30

## Research question

Which practical tools and adjacent skills appear in current product-management
job postings, and which free or open-source tools can this studio use to teach
those competencies?

This is a directional snapshot, not a statistically representative labor-market
study. Postings can change or expire. Sources were accessed on 2026-08-30.

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

Atlassian's Associate Product Manager program also emphasizes mentorship,
shipping, problem-solving, empathy, and communication rather than a list of
tools: [Atlassian APM](https://www.atlassian.com/company/careers/graduates/apm).

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

The curriculum should teach the competency rather than train button-clicking in
one vendor. Tool fluency matters, but the transferable product decision and
artifact matter more.

## Resulting curriculum choices

- Practice Figma and FigJam because design collaboration appears repeatedly,
  but provide Penpot and repo-native flows so a paid plan is never required.
- Practice Jira/Jira Product Discovery/Confluence concepts on free plans when
  useful, while keeping GitHub and Markdown as the durable source of truth.
- Teach SQL with DuckDB and dashboards with Metabase Open Source. This builds
  the data fluency postings ask for without needing a commercial BI license.
- Teach product instrumentation and experimentation with PostHog's free tier or
  synthetic event data.
- Teach API literacy with Hoppscotch and plain-language architecture artifacts;
  the human CPO is not expected to code.
- Teach research planning and synthesis with Dovetail Free or repository
  templates, and use Formbricks only for labeled synthetic survey practice.
- Assess communication, prioritization, judgment, and evidence use in every
  case; those skills cannot be replaced by software.

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

Recheck the posting sample and free-plan limits every six months or before a
case relies on an external feature. Update the access date and describe what
changed; do not silently overwrite the historical snapshot.
