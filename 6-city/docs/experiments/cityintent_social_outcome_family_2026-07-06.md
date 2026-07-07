# CityIntent Social-Outcome Scenario Family

Date: 2026-07-06

## Motivation

The rc1 headline — "legal but ineffective": frameworks stay feasible
(SOTOPIA trace_feasibility 1.0) yet fail the co-presence outcome
(task_completion 0.077; 0/4 accepted meetings) — currently rests on a single
meeting scenario at one repeat. That is too thin to carry Claim A. This adds a
dedicated `social_outcome` family that varies the co-presence outcome along
several axes, so the headline can be reported as a family effect rather than an
anecdote, and makes the checkout-machine framework runs turnkey.

## What was added

Six new scenarios under `benchmarks/cityintent_v0/scenarios/`
(family `social_outcome`), each centered on an environment-accepted co-presence
outcome:

| Scenario | Axis it stresses |
|---|---|
| `social_copresence_open_meet` | baseline co-presence, free location, no coordination gate |
| `social_copresence_message_gated` | interaction requires a prior confirming message |
| `social_copresence_event_window` | tight, opportunity-bound window (miss it and it's gone) |
| `social_copresence_two_party` | two sequential meetings with ordering (double co-presence) |
| `social_copresence_with_errand` | competing errand vs meeting — both outcomes required |
| `social_copresence_decoy_location` | discriminate the correct venue from a closer decoy |

## Fairness guarantee (oracle-winnability)

Every scenario is proven a *fair* test — winnable by a correct agent — before use.
`tools/verify_social_outcome_family.py` holds an oracle winning plan per scenario
and drives it through the real `execute_action` + `score_trace`.

Result — ALL PASS: task_completion == 1.0, trace_feasibility == 1.0, zero
violations, and an accepted co-presence interaction for every co_presence outcome
(the two-party scenario yields two accepted interactions). Schema validation
passes (18 scenarios total; `social_outcome` = 6). Guarded by
`tests/test_social_outcome_family.py`.

Archived: `results/cityintent_v1_rc1/social_outcome_family_oracle/`.

## Design notes (contract mechanics confirmed while authoring)

- `interaction_target_available` only grants a co_presence target via
  `location_any_of` (not a bare `location`), and — when the scenario has any
  `send_message` outcome to that counterpart — requires a prior message. Both are
  respected by the message-gated variants.
- Interacting before the window opens raises `interaction_target_unavailable`; the
  oracles cross into the window with a paid `buy` (cost>0 venues) or a free
  `dwell` (park), confirming the "arrive early, wait correctly" path is legal.
- A first draft used a `plaza-library` route block, but the natural shortest path
  (office→coworking→bookstore→library) avoids that edge, so the block never bit
  and no replan was scored. Replanning is already covered by the v0.3
  interruptible-movement runs; scenario #5 was reframed to the errand-vs-meeting
  trade-off to keep this family cleanly about the *social outcome*.

## Framework Run Completed

The four official decision-layer adapters were run over all six scenarios for
three repeats on the checkout machine (72 real provider-backed traces). GATSim
accepts 15/21 co-presence outcomes; AgentSociety 4/21; Generative Agents 2/21;
the SOTOPIA-style `LLMAgent` adapter 0/21 despite 61.1% fully feasible traces.
The full result is archived at
`results/cityintent_v1_rc1/external_frameworks_4x6socialx1_gpt54mini_2026-07-06/`
and interpreted in
`docs/experiments/cityintent_v1_rc1_social_outcome_4x6x3_2026-07-06.md`.
