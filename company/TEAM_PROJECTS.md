# Functional team projects

Toothless Technologies LLC runs 12 separate public GitHub Projects. There is
no master board. Each team controls its own commitments, while
`clients/<engagement-slug>/PROJECT_TRACKER.md` links the cards that together
serve one engagement.

The machine-readable assignment is in [`team_projects.toml`](team_projects.toml).
Every one of the 30 AI roles has exactly one primary project.

| Team project | Accountable leader | Primary roles | Scope |
|---|---|---|---|
| [Executive & Portfolio](https://github.com/users/viseshrp/projects/2) | CEO | CEO; Independent Board Director for Product and Strategy | Company priorities, portfolio allocation, executive decisions, governance, and closeout |
| [Product Management](https://github.com/users/viseshrp/projects/3) | Human CPO | Product Operations Manager; Product Analyst; Experimentation Analyst | Product decisions, strategy, requirements, roadmap, metrics, and product operations |
| [Research](https://github.com/users/viseshrp/projects/4) | Human CPO | Market Researcher; User Researcher | Market and user evidence, assumptions, unknowns, and synthesis |
| [Design & Accessibility](https://github.com/users/viseshrp/projects/5) | Human CPO | Product Designer; Content Designer; Accessibility Specialist | Experience direction, interaction and visual design, content, and accessibility |
| [Development & Architecture](https://github.com/users/viseshrp/projects/6) | CTO | CTO; Engineering Manager; Solution Architect; Frontend Engineer; Backend Engineer; Mobile Engineer; Data Engineer; Technical Writer | Architecture, implementation planning, software delivery, data, and technical documentation |
| [Reliability & Security](https://github.com/users/viseshrp/projects/7) | CTO | DevOps and SRE; Security Engineer | Infrastructure, delivery automation, reliability, security, and technical risk |
| [Testing & Quality](https://github.com/users/viseshrp/projects/8) | CTO | QA Engineer | Acceptance coverage, defect evidence, verification, and release quality |
| [Sales](https://github.com/users/viseshrp/projects/9) | CRO | CRO; Sales Director; Account Executive; Solutions Consultant | Public-signal opportunity discovery, qualification support, and internal account planning |
| [Marketing & Customer Success](https://github.com/users/viseshrp/projects/10) | CRO | Product Marketing Manager; Customer Success Manager | Positioning, internal market readiness, adoption planning, and support design |
| [Operations](https://github.com/users/viseshrp/projects/11) | COO | COO | Staffing, dependencies, cadence, risks, handoffs, and the company checkpoint |
| [Finance](https://github.com/users/viseshrp/projects/12) | CFO | CFO | Financial assumptions, scenarios, budgets, unit economics, and commercial analysis |
| [Legal & Risk](https://github.com/users/viseshrp/projects/13) | COO | Legal and Risk Advisor | Representation controls, legal assumptions, compliance questions, and enterprise risk |

The CPO directs Product Management, Research, and Design & Accessibility as a
product executive. Product Operations performs the board administration for
those functions; the CPO is never assigned issue routing or status collation.

## One-card ownership

One work item belongs to one team project. A second team receives its own card
only when it owns a distinct deliverable, review, risk, or decision. The two
cards link to one another through `Depends on`. Do not copy one card across
projects merely for visibility.

Every substantive work item is also a repository issue. This gives the card a
stable URL, written history, and a clear place for pause and handoff notes.
The full operating contract is in
[`playbooks/PROJECT_BOARDS.md`](../playbooks/PROJECT_BOARDS.md).
