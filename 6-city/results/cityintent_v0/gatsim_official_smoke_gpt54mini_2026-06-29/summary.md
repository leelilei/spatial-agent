# CityIntent v0 Trace Results

This run includes verified external-framework adapters: `gatsim_official_planner`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| gatsim_official_planner | 1.0 | 0.556 | 0.444 | 0.444 | 0.333 | 0.75 | 0.444 | 0.0 | 0.833 | 1.0 | 0.5 |  | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
