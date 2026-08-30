# Using the studio with Codex

The repository is configured so a lead Codex agent can assemble specialist AI
roles for non-product work while the human CPO stays in the main conversation.

## How it works

Codex reads the root `AGENTS.md` before working. The 30 project-specific agent
profiles in `.codex/agents/` describe when and how to use each company role. The
lead agent should activate the smallest useful team, give each specialist a
bounded task, and return its evidence or artifact to the main engagement.

The role files deliberately omit a fixed model. They inherit the available
Codex configuration, which keeps the playbook portable as models change.

Official references:

- [How Codex discovers `AGENTS.md`](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex subagents and project agent profiles](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## What the CPO needs to do

The CPO can speak to the CEO in normal language. She does not need to name every
agent or manage parallel work.

Examples:

```text
CEO, bring me the next product decision. Staff any non-product work needed to
give me evidence and options.
```

```text
Coach, I do not understand this metric decision. Explain it with an example,
then ask me one question.
```

```text
CTO, have the engineering team build the approved MVP. Bring product ambiguity
back to me, but make technical decisions within your authority.
```

```text
CEO, show me which agents are active, what each owns, and which product decision
is waiting on me.
```

## Delegation rules

- Product decisions remain in the main conversation with the human CPO.
- Read-heavy independent research and reviews can happen in parallel.
- Each artifact has one writing owner at a time to prevent conflicting edits.
- Every specialist receives an engagement path, task, evidence boundary, output
  path, decision owner, and completion test.
- The lead agent reviews delegated output before treating it as accepted.
- If subagents are unavailable, the lead agent performs the roles sequentially
  under the same boundaries.

## Expected visible behavior

When delegation is working well, the CPO should see a concise synthesis such as:

```text
The Market Researcher found two supported patterns and one unresolved gap. The
User Researcher designed a synthetic proxy test, and the CTO found both options
feasible. Your decision is which target user to serve first. Here are the two
options and their tradeoffs.
```

She should not receive raw agent chatter, be asked to reconcile conflicting
files, or be handed coding work.
