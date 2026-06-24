# CityIntent v0 Trace Results

Offline architecture proxies are still not real LLM results unless the agent type is `api_llm_direct_actor`.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| llm_direct_actor | 1.0 | 0.75 | 0.25 | 0.438 | 0.125 | 0.456 | 0.25 | 0.0 | 0.807 | 0.875 | 0.35 | 0.125 | 0.0 | 0.0 |
| memory_reflection | 1.0 | 0.875 | 0.125 | 0.125 | 0.0 | 0.938 | 0.125 | 0.0 | 0.891 | 1.0 | 0.875 | 1.0 | 0.0 | 0.0 |
| reactive_replanner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.969 | 0.0 | 1.0 | 0.983 | 1.0 | 0.969 | 0.75 | 0.0 | 0.0 |
| utility_planner | 1.0 | 0.875 | 0.125 | 0.125 | 0.0 | 0.906 | 0.125 | 0.0 | 1.0 | 1.0 | 0.844 | 0.75 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
