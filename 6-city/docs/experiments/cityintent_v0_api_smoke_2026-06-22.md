# CityIntent v0 API Smoke Run

Date: 2026-06-22

## Setup

Benchmark: `benchmarks/cityintent_v0`

Model-backed agent:

- agent type: `api_llm_direct_actor`
- provider: `fhl`
- model: `gpt-5.4-mini`
- wire API: `responses`
- config: `benchmarks/cityintent_v0/configs/fhl_gpt54mini.json`

Comparison baseline:

- `utility_planner`

Run output:

- `results/cityintent_v0/api_all_gpt54mini/summary.md`
- `results/cityintent_v0/api_all_gpt54mini/summary.csv`
- `results/cityintent_v0/api_all_gpt54mini/traces.jsonl`

## Aggregate Result

| agent_type | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness |
|---|---:|---:|---:|---:|---:|---:|---:|
| `api_llm_direct_actor` | 0.869 | 0.078 | 0.0 | 0.848 | 1.0 | 0.822 | 0.75 |
| `utility_planner` | 0.906 | 0.125 | 0.0 | 1.0 | 1.0 | 0.844 | 0.75 |

## Main Takeaways

1. The API-backed CityIntent loop works end to end.

   The real model produced parseable typed actions, the environment executed
   them, and deterministic scoring generated trace-level and aggregate outputs.

2. Direct LLM action is strong on ordinary preference and memory cases.

   It completed `closed_poi_replacement`, `memory_dependent_place_choice`,
   `lunch_meeting_time_pressure`, `avoid_crowd_event`, and
   `conflicting_social_obligation` without feasibility violations.

3. The benchmark exposes failures that are easy to miss in plain text.

   In `commute_disruption`, the model chose a route that crossed the
   `transit_hub` to `office` edge during the blocked time interval. The action
   sounded plausible, but the environment trace marked the blocked-edge
   violation.

4. The benchmark exposes weak task-state control.

   In `unexpected_friend_encounter`, the model repeatedly interacted with Casey
   instead of completing the medicine errand. The repeated short chats sounded
   locally reasonable, but the trace failed the bounded-social-interaction goal
   and left the errand incomplete.

5. The prompt/action interface matters.

   Earlier smoke runs showed that if `dwell` is underspecified, the model keeps
   moving between plausible places. After clarifying that `dwell` is how agents
   work, wait, meet, eat, or complete time at a place, behavior became much more
   stable.

## Method Fixes From This Run

The run exposed three benchmark/scoring fixes that were applied before the final
`api_all_gpt54mini` result:

- blocked edges are checked over the whole traversal interval, not only at the
  departure time;
- actions that cross the episode end time now produce an `episode_overtime`
  violation;
- bounded social interaction now sums total interaction time with the target
  agent, instead of accepting any single short interaction;
- `budget_errand_chain.return_home` now ignores the initial home location when
  scoring whether the agent returned home.

## Interpretation

This is not yet a leaderboard result. It is a smoke run with one model, one
prompt/action interface, and eight toy scenarios.

The useful conclusion is methodological:

> CityIntent can turn plausible-sounding city-agent behavior into a verifiable
> action trace, and the trace reveals failures in temporal constraints,
> route validity, budget/task state, and bounded social behavior.

The next experiment should compare:

- `api_llm_direct_actor`
- `api_reactive_replanner`
- `api_memory_reflection`

on the same eight scenarios, using the same model and deterministic scorer.
