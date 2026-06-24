# CityIntent v0 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Offline architecture proxies are still not real LLM results unless the agent type starts with `api_llm_`.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 1.0 | 0.975 | 0.025 | 0.025 | 0.0 | 0.969 | 0.0 | 1.0 | 0.896 | 1.0 | 0.969 | 0.75 | 0.125 | 0.0 |
| api_llm_plan_then_act | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.95 | 0.0 | 1.0 | 0.865 | 1.0 | 0.95 | 1.0 | 0.0 | 0.0 |
| api_llm_reactive_replanner | 1.0 | 0.875 | 0.125 | 0.125 | 0.0 | 0.938 | 0.125 | 0.0 | 0.911 | 1.0 | 0.875 | 1.0 | 0.0 | 0.0 |
| utility_planner | 1.0 | 0.875 | 0.125 | 0.125 | 0.0 | 0.906 | 0.125 | 0.0 | 1.0 | 1.0 | 0.844 | 0.75 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
