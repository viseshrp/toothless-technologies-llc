# Start the first practice engagement

This guide gets the human CPO from an empty studio to her first product decision
without tool setup or coding.

## 1. Open the studio

Open the repository in Codex and send:

```text
Act as the CEO of CPO Practice Studio. Read AGENTS.md and the company and
playbook files. Ask Sales to generate three current, fictional practice
opportunities involving real companies, using only public sources and the
required disclaimer. Choose the one with the clearest learning value, create
its isolated client folder from clients/_template, staff the smallest useful
team, and brief me as the CPO. Coach me one product decision at a time.
```

No Figma, Jira, or analytics account is required to begin. The agents should
create repository-native artifacts first.

## 2. Read the CEO brief

The CEO should tell the CPO:

- what the fictional company appears to need and which claims are sourced;
- what has been invented for the exercise;
- which digital-product category is in scope;
- why the case is useful for practice;
- which roles are active now; and
- the first product decision, explained in plain language.

If the brief suggests a real request, real contact, or affiliation, stop and
have the Legal and Risk Advisor correct it.

## 3. Make one decision at a time

The CPO should answer in her own words. A useful answer does not need product
jargon. The Product Coach should clarify, challenge, and then record the final
decision in `DECISION_LOG.md`.

At minimum, the first case should let her decide:

1. the target user;
2. the user problem;
3. the outcome worth creating;
4. the evidence needed before committing to a solution;
5. the MVP boundary;
6. the most important success metric; and
7. whether the working MVP meets the product acceptance criteria.

## 4. Let agents do their jobs

The CPO should not be asked to:

- write application code or tests;
- configure hosting, analytics, CI, or databases;
- collect real leads or contact research participants;
- administer Jira, create status reports, or coordinate agent schedules;
- calculate budgets or prepare legal language; or
- fix technical defects.

She should be asked to interpret evidence, resolve product ambiguity, explain
tradeoffs, communicate product direction, and accept or reject product work.

## 5. End with a learning review

At case close, ask:

```text
CEO, close the engagement. Have the Product Coach review my decisions against
the coaching rubric, cite examples from the decision log, identify one strength
and one growth area, and recommend the skill the next case should exercise.
```

The review belongs in `RETROSPECTIVE.md`. It should use evidence from her work,
not generic encouragement.

## If the interaction stops feeling educational

Use one of these corrections:

```text
Pause. Explain the product concept and why this decision matters, then ask me
one focused question.
```

```text
You are making a product decision for me. Give me the evidence, two or three
options, your recommendation, and the tradeoffs, then let me decide.
```

```text
This is not product work. Delegate it to the correct AI role and return when I
have a product decision to make.
```
