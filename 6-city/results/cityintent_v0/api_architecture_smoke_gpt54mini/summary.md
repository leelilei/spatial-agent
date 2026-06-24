# CityIntent v0 Trace Results

This run includes `api_llm_direct_actor`, which calls a configured real model provider.

Offline architecture proxies are still not real LLM results unless the agent type is `api_llm_direct_actor`.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 1.0 | 0.75 | 0.25 | 0.25 | 0.5 | 0.75 | 0.25 | 0.0 | 1.0 | 1.0 | 0.625 |  | 0.0 | 0.0 |
| api_llm_plan_then_act | 1.0 | 0.75 | 0.25 | 0.25 | 0.5 | 0.875 | 0.25 | 1.0 | 0.817 | 1.0 | 0.688 |  | 0.0 | 0.0 |
| api_llm_reactive_replanner | 1.0 | 0.5 | 0.5 | 0.5 | 0.0 | 0.75 | 0.5 | 0.0 | 1.0 | 1.0 | 0.5 |  | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
