# Engagement lifecycle and gates

Every account follows ten operating stages. A stage may be compressed, but its
decision owner and gate cannot be silently skipped. The CEO owns engagement
flow; named executives and specialists own their domains; the CPO owns all
product decisions.

## Stage 1: Opportunity

**Purpose:** identify product-consulting opportunities from current public
market signals.

**Active roles:** CRO, Sales Director, Market Researcher, Legal and Risk Advisor.

**Required output:** three internal opportunity cards, each with:

- target organization and public signal;
- source links and access dates;
- assumed need and commercial context;
- possible product category and mandate;
- strategic fit, revenue logic, and delivery implications;
- representation, data, regulatory, and reputation risk; and
- the required independent-work disclosure.

**Gate O — CEO:** select one opportunity based on evidence, strategy, commercial
logic, capacity, portfolio balance, and risk.

## Stage 2: Qualification

**Purpose:** determine whether Greyshore should allocate company capacity to the
selected opportunity.

**Active roles:** CEO, CRO, CFO, CTO, COO, Legal and Risk Advisor, Account
Executive.

**Required output:** `QUALIFICATION.md` covering:

- strategic and portfolio fit;
- assumed account and commercial context;
- product mandate and key unknowns;
- financial range and cost assumptions;
- technical feasibility and capability gaps;
- staffing and dependency impact;
- risk assessment and controls; and
- executive accept, reject, or condition recommendations.

**Gate Q — CEO:** accept, reject, or condition the opportunity. Material
portfolio or company-governance exposure goes to the Board.

## Stage 3: Kickoff

**Purpose:** establish an isolated engagement with explicit authority and
accountability.

**Active roles:** CEO, COO, CPO, Product Operations Manager, Account Executive.

**Required output:** a new `clients/<engagement-slug>/` copied from the template,
completed `README.md`, `BRIEF.md`, `QUALIFICATION.md`, `TEAM.md`, assumptions,
risks, stage plan, and first product decision.

**Gate K — CEO:** confirm account isolation, disclosure, qualification, staffing,
decision rights, and scope.

## Stage 4: Discovery

**Purpose:** gather enough evidence about users, context, behavior, alternatives,
and constraints to frame the product problem.

**Active roles:** Market Researcher, User Researcher, Product Analyst; add
Solutions Consultant or CTO for material technical unknowns.

**CPO decisions:** research objective, riskiest assumptions, segments to
investigate, evidence threshold, and interpretation of evidence.

**Required output:** `RESEARCH.md` containing facts, inferences, assumptions,
unknowns, methods, limitations, and citations. Synthetic interviews and data
must be labeled at every use.

**Gate D — CPO:** evidence is sufficient to define a problem, or additional
discovery is required.

## Stage 5: Strategy

**Purpose:** select the product problem, outcome, and strategic position before
committing to a solution.

**Active roles:** Product Designer, Product Analyst, CFO when viability matters,
Market Researcher when competitive context remains open.

**CPO decisions:** target user, problem statement, desired outcome, value
proposition, product principles, success metric, guardrails, and non-goals.

**Required output:** approved `PRODUCT_STRATEGY.md`, updated `METRICS.md`, and
decision-log entries.

**Gate S — CPO:** approve the user, problem, outcome, and strategic choices.

## Stage 6: Solution

**Purpose:** compare materially different ways to create the approved outcome.

**Active roles:** Product Designer, Content Designer, Accessibility Specialist,
Solution Architect, CFO when cost differs materially.

**CPO decisions:** evaluation criteria, selected concept, experience direction,
and accepted product tradeoffs.

**Required output:** at least three concepts including a low-complexity option,
user flow, assumption map, feasibility notes, and decision record.

**Gate C — CPO and CTO:** the CPO selects the product direction. The CTO confirms
at least one feasible implementation path.

## Stage 7: Validation

**Purpose:** reduce the riskiest product uncertainty before authorizing a build.

**Active roles:** Product Designer, User Researcher, Content Designer,
Accessibility Specialist, Experimentation Analyst.

**CPO decisions:** hypothesis, prototype fidelity, participant proxy, success
threshold, interpretation, and product response.

**Required output:** prototype reference or repository-native flow, validation
plan, clearly labeled synthetic or proxy findings, limitations, and resulting
product changes.

**Gate V — CPO:** proceed, redirect, narrow, or stop, with a recorded rationale.

## Stage 8: Plan

**Purpose:** define the smallest valuable MVP and align product and technical
execution.

**Active roles:** Product Operations Manager, CTO, Engineering Manager, Solution
Architect, Product Analyst, Security Engineer as required.

**CPO decisions:** MVP goal, in-scope and out-of-scope behavior, priority,
acceptance criteria, roadmap order, success measures, and product risks.

**Required output:** approved `PRD.md`, `ROADMAP.md`, `METRICS.md`, experience
reference, and technical plan under `delivery/`.

**Gate P — dual approval:** the CPO signs off product scope and acceptance
criteria. The CTO signs off feasibility, security approach, and build plan.

## Stage 9: Build and assure

**Purpose:** deliver a working local MVP and determine product and technical
readiness.

**Active roles:** CTO, Engineering Manager, required engineers, QA, Security,
Accessibility, Product Design, Product Analyst, Technical Writer.

**CPO decisions:** resolve product ambiguity, accept or reject scope changes,
evaluate working behavior, prioritize experience gaps, and approve product
readiness.

**Required output:** working code under `delivery/`, tests, setup instructions,
`delivery/BUILD_LOG.md`, acceptance results, defect list, accessibility and
security reviews, analytics plan, and known limitations.

**Gate A — dual approval:** the CPO approves product readiness. The CTO approves
technical readiness. Either may reject and return the engagement to build.

## Stage 10: Market readiness and closeout

**Purpose:** prepare an internal account and product recommendation, preserve the
delivery record, and return company capacity.

**Active roles:** CEO, COO, CRO, CPO, CTO, CFO, Product Marketing Manager,
Customer Success Manager, Product Analyst, Legal and Risk Advisor.

**CPO decisions:** product narrative, permitted product claims, internal rollout
recommendation, measurement response thresholds, and final product position.

**Required output:** internal market-readiness brief, positioning, adoption and
support model, dashboard specification, financial and delivery review, known
risks, `ENGAGEMENT_REVIEW.md`, and explicit confirmation that no external launch
or target-account representation occurred.

**Gate X — CEO:** accept the closeout, record company-level implications, and
release the team. Refer material portfolio or governance issues to the Board.

## Board involvement

The Independent Board Director for Product and Strategy is not a standing
engagement role. Activate the director only under
`playbooks/BOARD_GOVERNANCE.md`. Store any opinion in `BOARD_ADVISORY.md` without
changing the underlying executive or CPO decision record.

## Gate-status format

Record each gate in `DECISION_LOG.md`:

```markdown
## YYYY-MM-DD — Gate S: Product strategy

- Decision owner: Human CPO
- Status: approved | rejected | revise
- Decision:
- Evidence considered:
- Alternatives rejected and why:
- Risks and unknowns:
- Dissent:
- Downstream consequence:
```
