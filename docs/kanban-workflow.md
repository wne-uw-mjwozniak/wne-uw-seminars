# Weekly status and the kanban board

Every thesis project is run on a **GitHub Projects** board. The board is the single source of truth
for progress: the supervisor reads it before each weekly check-in, so the call can be about
decisions rather than reporting.

## Set-up (once)

1. Create your project repository on GitHub (private is fine) and add the supervisor as a collaborator.
2. In the repository, open **Projects**, create a new project with the **Board** layout, and link it
   to the repository.
3. Set the `Status` field to these five columns:

   | Column | Meaning |
   | --- | --- |
   | Backlog | Ideas and future work, roughly ordered. |
   | Ready | Defined well enough to start: has a definition of done. |
   | In progress | Being worked on now. **At most two cards per person.** |
   | In review | Pull request open, waiting for the supervisor or a teammate. |
   | Done | Merged or otherwise finished. |

4. Turn on the built-in workflows: *item closed* moves a card to Done; *pull request merged* moves it to Done.
5. Add the first cards: concept note, repository and environment, data acquisition, first baseline,
   thesis outline.

## Cards

One card is one GitHub issue and one piece of work that can be finished in days, not weeks.
Writing counts: chapters and sections are cards too. Use this shape:

```markdown
**Goal**: what this achieves for the thesis, in one sentence.

**Definition of done**
- [ ] a concrete output: a figure, a table, a section, a passing test
- [ ] results reproducible from a clean clone

**Notes**: links, papers, open questions.
```

If a card sits in *In progress* for more than two weeks, it was too big. Split it.

## Flow

1. Move a card from Ready to In progress and create a branch for it.
2. Commit small and often, with messages that say what changed and why.
3. Open a pull request that references the issue (`Closes #12`) and move the card to In review.
4. The supervisor or a teammate reviews. Merging closes the issue and moves the card to Done.

## The weekly status

Before the check-in, make sure the board reflects reality. In the call, three questions:

1. What moved since last week?
2. What is blocked, and what decision do you need?
3. What will be in *Done* by next week?

## Team projects

Larger projects use one board for the whole team, with an `Assignee` on every card and, if helpful,
a custom field for the thesis each card belongs to. Shared infrastructure (data pipeline, evaluation
protocol) gets its own cards and is reviewed by someone who did not write it.
