# Product measurement plan

Use synthetic data under the current no-outreach boundary. Never imply that
synthetic events or results came from real users.

## Product outcome

[Approved outcome from `PRODUCT_STRATEGY.md`.]

## Metric tree

- **North-star candidate:** [metric and why]
  - **Leading indicator:** [metric]
  - **Leading indicator:** [metric]
- **User-value metric:** [metric]
- **Business-value metric:** [metric]
- **Guardrail:** [metric that must not worsen]
- **Diagnostic:** [metric that explains movement]

## Metric definitions

| Metric | Definition | Population | Window | Data source | Decision threshold | Limitation |
|---|---|---|---|---|---|---|
| [name] | [precise numerator/denominator] | [who] | [period] | [synthetic source] | [action threshold] | [caveat] |

## Instrumentation specification

| Event | Trigger | Required properties | Purpose | Privacy note |
|---|---|---|---|---|
| [event_name] | [behavior] | [properties] | [decision supported] | synthetic only |

## Decision rules

- If [metric] reaches [threshold], then [product response].
- If [guardrail] crosses [threshold], then [product response].
- If evidence is inconclusive, then [next evidence step].

## Analysis notes

- **Dataset:** [path]
- **Queries:** [path]
- **Dashboard or specification:** [path or free-tool link]
- **Synthetic-data label:** [where the label is displayed]
