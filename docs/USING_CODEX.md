# Running Toothless Technologies LLC with Codex

The repository configures a lead Codex agent to operate as Toothless
Technologies LLC's CEO and assemble specialist AI roles while the human CPO
remains in the main product conversation.

## Agent configuration

Codex reads the root `AGENTS.md` before working. The 30 project-specific profiles
in `.codex/agents/` define the remit and authority boundary of each Board,
executive, product, design, engineering, data, revenue, operations, and risk
role. The lead agent activates the smallest accountable team, gives each role a
bounded assignment, and returns its evidence or artifact to the engagement.

The project `.codex/config.toml` sets new lead sessions to `gpt-5.6-sol` with
`max` reasoning. Every role profile also sets an explicit model and `max`
reasoning: senior leadership uses Sol, direct reports to senior leadership use
Terra, and roles reporting to a manager or director use Luna. The lead session
routes substantive work through the exact role profile instead of performing
specialist work itself.

Project configuration applies when the repository is trusted. An explicit model
selection in the app or a command-line override has higher precedence, so do not
override the configured model for company work. Existing sessions do not change
models retroactively; start a new chat after model-routing configuration changes.

Official OpenAI documentation:

- [Open a folder and start a new Codex chat](https://learn.chatgpt.com/docs/app)
- [Codex project configuration basics](https://learn.chatgpt.com/docs/config-file/config-basic)
- [How Codex discovers `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex subagents and project agent profiles](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## First use

1. Open the ChatGPT desktop app and sign in.
2. Choose **Open folder** and select the cloned
   `toothless-technologies-llc` repository.
3. Read the root [`OPERATIONS.md`](../OPERATIONS.md) for the current company
   checkpoint.
4. Choose **Codex**, start a **New chat**, and paste the first-launch prompt from
   the root [`README.md`](../README.md).
5. Continue in the same chat until the engagement closes. Answer only the
   product decisions reserved for the CPO; direct other work back to the CEO.

The CPO does not need to choose or start individual agents. The CEO activates
the relevant project-scoped profiles and consolidates their work.

## CPO commands

The CPO speaks to the CEO and company roles in normal business language. She
does not need to manage agent concurrency.

```text
CEO, bring me the next product decision. Have the accountable teams complete
the non-product analysis and execution first.
```

```text
Product Analyst, give me the metric definitions, evidence, alternatives,
recommendation, and tradeoffs. I will make the product decision.
```

```text
CTO, direct Engineering to build the approved MVP. Return product ambiguity to
me, but make technical decisions within your authority.
```

```text
CEO, show me which company roles are active, what each owns, and which decision
is blocked on my product authority.
```

## Board product advisor

The Independent Board Director for Product and Strategy is not a default member
of an engagement. Use the role only under `playbooks/BOARD_GOVERNANCE.md`.

```text
CEO, refer this matter to the Independent Board Director for Product and
Strategy. The director should review the written record and issue an advisory
memorandum without managing my team or writing my product decision.
```

## Delegation rules

- Product decisions remain in the main conversation with the human CPO.
- Independent research and reviews can run in parallel.
- Each artifact has one writing owner at a time.
- Every specialist receives an engagement path, assignment, evidence boundary,
  output path, decision owner, and completion test.
- Before and after work, every specialist updates the appropriate functional
  project card under `playbooks/PROJECT_BOARDS.md`.
- The lead agent reviews delegated output before treating it as accepted.
- If the required custom role cannot run, pause that assignment and record the
  routing blocker. The lead agent does not emulate it under another model.
- Board involvement requires a documented governance trigger.

## Expected executive update

A well-formed update is concise and accountable:

```text
Market Research found two supported patterns and one material unknown. User
Research prepared a synthetic proxy analysis under the no-outreach policy. The CTO
confirmed that both options are feasible. The Product Designer recommends
Option A because it reduces abandonment with less scope. Your CPO decision is
which target user and product direction to approve.
```

The CPO should not receive raw agent chatter, conflicting files, administrative
assignments, or coding work.
