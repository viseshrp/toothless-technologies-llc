# Functional project operating contract

The 12 public projects in [`company/TEAM_PROJECTS.md`](../company/TEAM_PROJECTS.md)
are the live control surfaces for company work. Repository artifacts remain the
durable evidence and decision record. Cards state who owns the next result and
where that result lives.

## Shared Kanban workflow

Every project uses the same columns:

1. **Backlog** — valid work that is not committed next.
2. **Ready** — sufficiently defined and eligible to start.
3. **In progress** — actively owned now.
4. **Review** — the result exists and awaits its accountable reviewer.
5. **Blocked** — no safe progress is possible until a named dependency or
   decision is resolved.
6. **Done** — the acceptance condition, repository record, and required checks
   are complete.

Each card also maintains `Priority`, `Engagement`, `Stage`, `Work type`,
`Decision owner`, `Repository path`, `Depends on`, and `Last touched`.

`Workflow` is the detailed source of truth. Keep GitHub's built-in `Status`
field aligned for compatibility: `Backlog` and `Ready` map to `Todo`; `In
progress`, `Review`, and `Blocked` map to `In Progress`; `Done` maps to `Done`.

## Required work-item content

Use a repository issue for every substantive item and add it to exactly one
owning project. The issue states:

- the outcome and why it matters;
- the accountable team and working role;
- the engagement slug or `company`;
- the decision owner, including the CPO for reserved product decisions;
- dependencies and linked team cards;
- the repository artifact or expected path;
- the current state and next action; and
- the condition required to move to Done.

The issue form in `.github/ISSUE_TEMPLATE/team-work-item.yml` supplies this
structure.

## Update protocol

### Before work

1. Read [`OPERATIONS.md`](../OPERATIONS.md), then the active engagement's
   `PROJECT_TRACKER.md` when an engagement exists.
2. Identify the owning team through `company/team_projects.toml`.
3. Find the existing issue or create one, add it to that team's project, and
   fill every relevant field.
4. Move the card to **In progress** before substantive work starts.

### While work is active

- Update the owning card when scope, priority, owner, dependency, stage,
  decision owner, or expected artifact changes.
- When another team owns a separate result, create or update that team's card
  and link both cards through `Depends on`.
- Keep the engagement `PROJECT_TRACKER.md` aligned with every affected team
  project.
- Never ask the CPO to update cards, chase statuses, or administer projects.
  Product Operations owns that work for product functions; the accountable AI
  role owns it elsewhere; the COO audits the company checkpoint.

### Before any pause, handoff, or final response

Update every affected card with:

```text
Last completed:
Current state:
Next action:
Blocked by or waiting on:
Decision required and owner:
Repository artifacts:
Updated by and date:
```

Then set the truthful workflow column and update `Last touched`. Use
**Blocked** only when a named dependency prevents progress. Keep an item **In
progress** when an agent still owns the next action, and use **Review** when the
result awaits acceptance. Apply the corresponding built-in `Status` value at
the same time.

For a company-level pause, the COO also updates [`OPERATIONS.md`](../OPERATIONS.md)
and the standing checkpoint card in the Operations project. A new CEO or COO
agent resumes from that checkpoint before opening other cards.

### Completion

Move a card to **Done** only when:

1. its acceptance condition is satisfied;
2. the repository artifact and material evidence are linked;
3. applicable checks or reviews are recorded;
4. dependent cards and the engagement tracker reflect the result; and
5. no reserved CPO decision was silently made by an AI role.

Work is not complete merely because a file changed or an agent produced an
answer. The owning project must show the same current state.

## Cross-team rules

- One team owns each card; there is no shared master project.
- Create linked cards only for separately accountable outcomes.
- The requesting team's card records what it needs and by when. The delivering
  team's card records what it will produce.
- A product decision stays on Product Management even when a technical or
  commercial card depends on it.
- A technical review stays on Development, Reliability & Security, or Testing
  & Quality as appropriate; it is not reassigned to the CPO.
- The engagement tracker is an index, not another Kanban board.

## Resume order

When asked to continue company operations:

1. read `OPERATIONS.md`;
2. open the Operations checkpoint card;
3. read the active engagement's `PROJECT_TRACKER.md`;
4. inspect only the linked active or blocked cards on the relevant team
   projects; and
5. continue the recorded next action or return the recorded product decision to
   the CPO.

This order is the answer to “where did the company stop?” It avoids reconstructing
state from chat history.
