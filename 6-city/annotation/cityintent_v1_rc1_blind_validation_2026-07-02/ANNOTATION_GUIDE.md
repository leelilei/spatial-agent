# CityIntent Annotation Calibration Guide

Companion to `RUBRIC.md`. This teaches how to **apply** the rubric's definitions
with worked examples. It does **not** give answers to the audit items — the mini
traces below are hypothetical. You still judge every item independently and may
still disagree with any automated verdict; the goal is to apply the *definitions*
correctly, not to match an answer key.

All examples use the same evidence discipline as the packet: judge by the
**"Accepted environment outcomes"** block (entries / services / purchases /
accepted_dwell / interactions), **not** by the `action` column, the `reason`
text, or the plan's stated intent.

---

## Two ideas that cause most disagreement

### A. Completion is judged on ACCEPTED EVIDENCE, not on "the spirit"

An agent that *looks like* it did the task, or *arrives near* the goal, has not
completed an outcome unless the environment recorded the required evidence.

### B. Feasibility and completion are SEPARATE axes

- **Completion** = did the intended `outcome` conditions get their evidence?
- **Feasibility** = were the executed steps all *valid*?

A trace can be **feasible but not complete** (every step legal, but the agent
stopped early). A trace can be **infeasible but partially complete** (it reached
some outcomes but also did an invalid step). **Not reaching the goal is NOT, by
itself, infeasibility.** Decide the two labels separately.

---

## Signature rules, with worked micro-examples

### 1. Arrival ≠ entry

A `move` that arrives at a place leaves the agent *outside*. An outcome that needs
the agent to *be at / inside* a place (visit, dwell, service, pickup) requires an
explicit `enter` record.

> **Example.** Goal: "reach the office before 09:15." Trace: `move office`
> arriving 08:44, then `finish`. Accepted outcomes show `entries: [home (start)]`
> — no office entry.
> → **completion = not_complete.** The agent stood outside the office; the
> entry-based outcome was never earned. (It arrived on time, but arriving is not
> being there.)

### 2. Feasibility = every executed step valid; one bad step → infeasible

If *any* executed transition was rejected or violated — a blocked edge, a closed
place, entering where you are not, spending below zero, a rejected interaction —
the trace is **infeasible**, and you record the first invalid step. This holds
**even if the agent still reached its goal by other steps.**

> **Example.** Trace completes the errand, but step 3 was `enter market` while the
> agent was still at `plaza` (an `enter_not_at_location` rejection), and later
> steps recovered.
> → **feasibility = infeasible, first_invalid_step = 3** — despite the goal being
> met. Completion is judged separately.

### 3. Goal-incompletion alone is NOT infeasibility

If the agent simply stopped early or missed the goal, but **every step it did take
was legal**, the trace is **feasible** (and `not_complete` or `partial`). Do not
mark infeasible just because the outcome failed.

> **Example.** Goal: meet a friend. Trace: legal moves, `enter cafe`, `finish` —
> never attempted the meeting. No invalid step anywhere.
> → **feasibility = feasible, completion = not_complete.** (This is the single
> most common mistake: "the task failed, so it's infeasible." No — feasibility is
> only about the validity of the steps that *were* executed.)

### 4. Paid places: consuming/dwelling needs prior payment

At a place with a cost, a `dwell` or the benefit only counts if a `buy` /
`use_service` (a payment record) came first. A `dwell` at a paid place with no
prior payment is an invalid step.

### 5. A meeting needs an ACCEPTED interaction

Co-presence is earned only by an accepted `interaction` naming the counterpart,
the location, and a time inside the window. Sending messages, arriving at the
venue, or waiting there is **not** a meeting. If the scenario requires a
coordinating message first, that message must precede the interaction.

### 6. Only "Accepted environment outcomes" count

The `action` column shows what the agent *attempted*. The environment may have
**rejected** it. Never credit a purchase, entry, service, meeting, or dwell that
does not appear in the accepted-outcomes block. A claimed action with no matching
accepted record earns nothing.

---

## Per-item procedure

1. Read the private intention and list the `outcome`-role conditions (ignore
   `constraint` / `process` for the completion label).
2. For **completion**: for each outcome, find its evidence in the accepted-outcomes
   block. All present → `complete`; some present → `partial`; ~none → `not_complete`.
   Remember arrival ≠ entry (rule 1) and accepted-only (rule 6).
3. For **feasibility**: scan the executed steps for *any* invalid/rejected
   transition. None → `feasible`. One or more → `infeasible` + first invalid step.
   Do **not** let goal failure push you to infeasible (rule 3).
4. Label the two axes independently; use `uncertain` only when the packet truly
   lacks the information.

## Common pitfalls checklist

- [ ] Marked `complete` because the agent *arrived* — but there was no `enter`. (rule 1)
- [ ] Marked `feasible` because the goal was reached — but a step was rejected. (rule 2)
- [ ] Marked `infeasible` because the goal *failed* — but every step was legal. (rule 3)
- [ ] Credited an action from the `action` column that the environment rejected. (rule 6)
- [ ] Counted arriving/messaging/waiting as a completed meeting. (rule 5)
