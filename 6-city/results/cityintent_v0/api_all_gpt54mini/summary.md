# CityIntent v0 Trace Results

This run includes `api_llm_direct_actor`, which calls a configured real model provider.

Offline architecture proxies are still not real LLM results unless the agent type is `api_llm_direct_actor`.

## Aggregate Metrics

| agent_type | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness |
|---|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.869 | 0.078 | 0.0 | 0.848 | 1.0 | 0.822 | 0.75 |
| utility_planner | 0.906 | 0.125 | 0.0 | 1.0 | 1.0 | 0.844 | 0.75 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
