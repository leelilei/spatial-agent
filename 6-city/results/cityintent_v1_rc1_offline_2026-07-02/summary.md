# CityIntent v1.0-rc1 Trace Results

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| llm_direct_actor | 1.0 | 0.604 | 0.396 | 0.396 | 0.333 | 0.471 | 0.382 | 0.686 | 0.0 | 0.396 | 0.0 | 0.86 | 1.0 | 0.375 | 0.417 | 0.0 | 0.0 |
| memory_reflection | 1.0 | 0.976 | 0.024 | 0.024 | 0.0 | 1.0 | 1.0 | 1.0 | 1.0 | 0.024 | 1.0 | 0.905 | 1.0 | 0.976 | 1.0 | 0.0 | 0.0 |
| reactive_replanner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.946 | 0.956 | 1.0 | 0.667 | 0.0 | 1.0 | 0.936 | 1.0 | 0.946 | 0.833 | 0.0 | 0.0 |
| utility_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.979 | 1.0 | 1.0 | 0.667 | 0.0 | 1.0 | 0.936 | 1.0 | 0.979 | 0.833 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
