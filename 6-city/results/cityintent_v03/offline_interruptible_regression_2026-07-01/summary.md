# CityIntent v0.3 Trace Results

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| llm_direct_actor | 1.0 | 0.781 | 0.219 | 0.219 | 0.25 | 0.588 | 0.219 | 0.0 | 0.86 | 1.0 | 0.529 | 0.417 | 0.0 | 0.0 |
| memory_reflection | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | 1.0 | 0.905 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 |
| reactive_replanner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.967 | 0.0 | 1.0 | 0.978 | 1.0 | 0.967 | 1.0 | 0.0 | 0.0 |
| utility_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | 1.0 | 0.978 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
