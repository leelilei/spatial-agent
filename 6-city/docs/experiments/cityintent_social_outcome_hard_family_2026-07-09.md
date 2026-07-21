# CityIntent Social-Outcome HARD Family (E1: difficulty headroom)

Date: 2026-07-09

Status: verified 2026-07-09 — ALL PASS (6/6 two-sided).

## Motivation

The base `social_outcome` family saturates for a good execution scaffold: ReAct
accepts 21/21 required co-presence outcomes (unified six-policy table,
2026-07-08). Without headroom, the planned backbone sweep (E3) cannot
discriminate models — every backbone under ReAct would score ~100%. The hard
tier restores dynamic range while keeping the family strictly about
environment-accepted social outcomes.

## Design principle: difficulty must be *proven*, both ways

Every hard scenario ships with two hand-authored plans, both driven through the
real `execute_action` + `score_trace`:

- **Positive control (fairness)** — an oracle plan must reach
  `task_completion == 1.0`, `trace_feasibility == 1.0`, zero violations,
  accepted evidence for every outcome. No unwinnable scenarios.
- **Negative control (difficulty)** — the *natural greedy/reactive* play
  (nearest-first, salience-first, or stale-memory) must score
  `task_completion < 1.0`. Difficulty is demonstrated against a concrete
  plausible strategy, not asserted.

The pair also gives each scenario a measurable `headroom = 1 − greedy_task`.

## The six scenarios (family `social_outcome_hard`)

| Scenario | Difficulty mechanism | Why greedy fails |
|---|---|---|
| `hard_three_meeting_relay` | sequencing relay: 3 windows open in strict order | nearest counterpart (market, 17' via city_hall) is NOT the first window; going there first forfeits the park window (closes 12:40) |
| `hard_budget_entangled_meet` | irreversible budget entanglement | a routine grocery side-buy (14) starves the required medicine (9) + paid-wait tea (10) chain on a 20 budget |
| `hard_deadline_then_meet` | non-greedy ordering under a hard deadline | heading toward the (near, salient) meeting first makes the far 12:35 pharmacy deadline unreachable |
| `hard_stale_plan_override` | fresh public update must override remembered plan | executing the memorized "plaza 13:00" misses the real window (quiet cafe, closes 12:45) |
| `hard_full_evening_chain` | 4-outcome chain; the meal duration is the bridge into the social window | eat-first-leave-early exits the diner before Casey's 17:45 window opens |
| `hard_overlapping_windows` | overlapping windows, far-closes-first | taking the near, already-open cafe first + forced paid wait loses the park window to travel time |

Shared properties: all outcomes remain environment-evidence-based (accepted
`interaction` / `purchase` / `service` / `entry`); windows, travel times, and
budgets are tuned against the world graph so the oracle passes with small but
nonzero margin (1–4 credits / 2–5 minutes); `interaction_target_available`
mechanics (co-presence windows, message gating, paid-wait `buy`/`dwell` rules)
follow the base family conventions.

## Artifacts

- Scenarios: `benchmarks/cityintent_v0/scenarios/hard_*.json` (6 files)
- Two-sided verifier: `benchmarks/cityintent_v0/tools/verify_social_outcome_hard_family.py`
- Guard test: `benchmarks/cityintent_v0/tests/test_social_outcome_hard_family.py`
- Report archive: `results/cityintent_v1_rc1/social_outcome_hard_family_oracle/`

## Results (two-sided verification, run 2026-07-09)

ALL PASS — every scenario winnable by the oracle AND failed by the plausible
greedy play:

| Scenario | Oracle task / feas / viol | Greedy task | Headroom |
|---|---|---:|---:|
| `hard_three_meeting_relay` | 1.0 / 1.0 / 0 | 0.667 | 0.333 |
| `hard_budget_entangled_meet` | 1.0 / 1.0 / 0 | 0.769 | 0.231 |
| `hard_deadline_then_meet` | 1.0 / 1.0 / 0 | 0.000 | 1.000 |
| `hard_stale_plan_override` | 1.0 / 1.0 / 0 | 0.333 | 0.667 |
| `hard_full_evening_chain` | 1.0 / 1.0 / 0 | 0.643 | 0.357 |
| `hard_overlapping_windows` | 1.0 / 1.0 / 0 | 0.500 | 0.500 |

Mean greedy headroom ≈ 0.51. Every oracle ends with all outcomes evidenced and
a non-negative budget; greedy failures land exactly on the intended mechanism
(e.g. the budget-entangled greedy ends at −13 credits; the deadline greedy
misses the 12:35 cutoff entirely).

Schema validation: 30 scenarios total, `social_outcome_hard` = 6. Full test
suite: 41 passed (guarded by `tests/test_social_outcome_hard_family.py`).

## Authoring lesson (recorded for future scenario design)

The first relay oracle failed 2/6 because the hand-computed office→park route
missed the shorter `office→city_hall→market→park = 25'` path: the whole
timeline ran 2 minutes early and two interacts fired *before* their windows,
rejected as `interaction_target_unavailable`. Two takeaways: (a) the
environment's early-arrival rejection works as designed — arriving early and
interacting immediately is not a meeting; (b) never trust hand-computed
shortest paths — the two-sided verifier catches exactly this class of authoring
error, which is why it must gate every new scenario.

## Next

Run the 6 policies (2 paper-backed baselines + 4 official adapters) over
`social_outcome` + `social_outcome_hard` (12 scenarios) × 3 repeats — the
baselines run wherever a provider config exists; the official adapters need the
checkout machine. If ReAct drops below 1.0 on the hard tier while remaining
near-perfect on the base tier, the benchmark gains the model-discriminative
dynamic range E3 (backbone sweep) requires.
