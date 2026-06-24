# CityIntent v0 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Offline architecture proxies are still not real LLM results unless the agent type starts with `api_llm_`.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 1.0 | 0.842 | 0.158 | 0.158 | 0.25 | 0.796 | 0.111 | 0.5 | 0.823 | 0.917 | 0.737 | 0.667 | 0.167 | 0.083 |
| api_llm_plan_then_act | 1.0 | 0.896 | 0.104 | 0.104 | 0.083 | 0.933 | 0.104 | 1.0 | 0.868 | 0.917 | 0.849 | 0.833 | 0.0 | 0.0 |
| api_llm_reactive_replanner | 1.0 | 0.833 | 0.167 | 0.167 | 0.0 | 0.904 | 0.167 | 0.5 | 0.91 | 1.0 | 0.796 | 0.833 | 0.0 | 0.0 |
| utility_planner | 1.0 | 0.75 | 0.25 | 0.25 | 0.0 | 0.85 | 0.25 | 0.0 | 1.0 | 1.0 | 0.713 | 0.667 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
