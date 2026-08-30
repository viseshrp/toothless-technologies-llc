# Engagement lifecycle and gates

Every practice case uses the same eleven stages. Stages can be shortened, but a
gate cannot be silently skipped. The CEO owns the engagement flow; the Product
Coach keeps the CPO learning; named decision owners approve their domains.

## Stage 1: Opportunity

**Purpose:** create a realistic learning problem without pretending there is a
real client.

**Active roles:** CEO, CRO, Sales Director, Market Researcher, Legal and Risk
Advisor.

**Required output:** three public-source opportunity cards, each with:

- named company and current signal;
- source links and access dates;
- fictional need and clearly labeled assumptions;
- possible digital-product type;
- likely product learning objectives; and
- required simulation disclaimer.

**Gate O — CEO:** select one case based on learning value, evidence quality,
scope, and safety. No CPO product decision is required yet.

## Stage 2: Kickoff

**Purpose:** turn the selected opportunity into a controlled engagement.

**Active roles:** CEO, COO, Product Coach, Product Operations Manager, Account
Executive.

**Required output:** a new `clients/<engagement-slug>/` copied from the template,
completed `README.md` and `BRIEF.md`, named team, assumptions, risks, stage plan,
and first product question.

**Gate K — CEO:** confirm the folder is isolated, disclaimers are present, and
staffing is minimal. The CEO then briefs the CPO.

## Stage 3: Discover

**Purpose:** learn enough about users, context, behavior, and alternatives to
frame a product problem responsibly.

**Active roles:** Product Coach, Market Researcher, User Researcher, Product
Analyst; add Solutions Consultant or CTO for material technical unknowns.

**CPO decisions:** research objective, riskiest assumptions, target segments to
study, evidence threshold, and interpretation of the evidence.

**Required output:** `RESEARCH.md` containing facts, inferences, assumptions,
unknowns, methods, limitations, and citations. Synthetic interviews and data
must be labeled at every use.

**Gate D — CPO:** approve that the evidence is sufficient to define a problem,
or choose more research.

## Stage 4: Define

**Purpose:** choose the problem and outcome before choosing a solution.

**Active roles:** Product Coach, Product Designer, Product Analyst, CFO when
business viability matters.

**CPO decisions:** target user, job or need, problem statement, desired outcome,
value proposition, product principles, success metric, guardrails, and explicit
non-goals.

**Required output:** the problem and strategy sections of `PRODUCT_STRATEGY.md`,
an updated `METRICS.md`, and decision-log entries.

**Gate P — CPO:** approve the problem, outcome, and measurement direction.

## Stage 5: Explore

**Purpose:** compare meaningfully different ways to create the desired outcome.

**Active roles:** Product Designer, Content Designer, Accessibility Specialist,
Solution Architect, CFO when cost materially differs.

**CPO decisions:** evaluation criteria, selected concept, experience direction,
and accepted tradeoffs.

**Required output:** at least three solution concepts, including a low-complexity
option; user flow; assumption map; feasibility notes; and a decision record.

**Gate E — CPO and CTO:** CPO selects the product direction. CTO confirms that
at least one implementation path is feasible within the fictional constraints.

## Stage 6: Validate

**Purpose:** test the riskiest product assumptions before committing to build.

**Active roles:** Product Designer, User Researcher, Content Designer,
Accessibility Specialist, Experimentation Analyst.

**CPO decisions:** hypothesis, prototype fidelity, participant profile or proxy,
success threshold, interpretation, and iteration choice.

**Required output:** prototype reference or repo-native flow, test plan, clearly
labeled synthetic/proxy findings, limitations, and resulting changes.

**Gate V — CPO:** persevere, pivot, narrow, or stop. Record why.

## Stage 7: Plan

**Purpose:** define the smallest valuable and testable MVP and align product and
technical execution.

**Active roles:** Product Operations Manager, CTO, Engineering Manager, Solution
Architect, Product Analyst, Security Engineer as needed.

**CPO decisions:** MVP goal, in-scope and out-of-scope behavior, priority,
acceptance criteria, roadmap order, success measures, and product risks.

**Required output:** approved `PRD.md`, `ROADMAP.md`, `METRICS.md`, experience
reference, and technical plan under `delivery/`.

**Gate B — dual approval:** the CPO signs off product scope and acceptance
criteria. The CTO signs off feasibility, security approach, and build plan.

## Stage 8: Build

**Purpose:** create a working local MVP that tests the approved product idea.

**Active roles:** CTO, Engineering Manager, only the engineers required, QA,
Security, Technical Writer.

**CPO decisions:** resolve product questions, review increments, accept or reject
scope changes, and decide whether behavior matches the intent.

**Required output:** working code under `delivery/`, tests, setup instructions,
and `delivery/BUILD_LOG.md` with commands and results.

**Gate I — Engineering Manager:** implementation is complete against the current
approved scope. Product deviations are logged and approved by the CPO.

## Stage 9: Assure

**Purpose:** determine whether the MVP is useful enough and safe enough for the
simulated next step.

**Active roles:** QA Engineer, Security Engineer, Accessibility Specialist,
Product Designer, Product Analyst, CTO.

**CPO decisions:** product acceptance, severity of experience gaps, metric
readiness, and which issues block a simulated release.

**Required output:** acceptance results, defect list, accessibility review,
security review, analytics plan, and known limitations.

**Gate A — dual approval:** the CPO approves product readiness. The CTO approves
technical readiness. Either may reject and return the case to Build.

## Stage 10: Launch simulation

**Purpose:** practice bringing a product to market without actually publishing
or contacting anyone.

**Active roles:** Product Marketing Manager, Customer Success Manager, Product
Analyst, CRO, Technical Writer, Legal and Risk Advisor.

**CPO decisions:** product narrative, product promises, rollout approach,
learning plan, and product-response thresholds.

**Required output:** internal launch brief, positioning, onboarding plan,
support assumptions, dashboard specification, rollout/rollback recommendation,
and explicit statement that no external launch occurred.

**Gate L — CEO:** accept the internal launch simulation. External deployment or
communication remains prohibited without separate human authorization.

## Stage 11: Review

**Purpose:** convert the work into better product judgment.

**Active roles:** CEO, Product Coach, Product Operations Manager.

**Required output:** `RETROSPECTIVE.md` with outcome review, decision evidence,
rubric scores, one demonstrated strength, one priority growth area, and a next
case recommendation.

**Gate R — CEO:** close the case and release its agents. Preserve all artifacts
in the engagement folder.

## Gate-status format

Record each gate in `DECISION_LOG.md`:

```markdown
## YYYY-MM-DD — Gate P: Problem definition

- Decision owner: Human CPO
- Status: approved | rejected | revise
- Decision:
- Evidence considered:
- Options rejected and why:
- Risks and unknowns:
- Downstream consequence:
```
