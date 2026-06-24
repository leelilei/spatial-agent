# CityIntent v0 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Offline architecture proxies are still not real LLM results unless the agent type starts with `api_llm_`.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 1.0 | 0.892 | 0.108 | 0.108 | 0.083 | 0.871 | 0.038 | 1.0 | 0.784 | 1.0 | 0.838 | 0.667 | 0.25 | 0.083 |
| api_llm_plan_then_act | 1.0 | 0.883 | 0.117 | 0.117 | 0.25 | 0.913 | 0.117 | 1.0 | 0.878 | 0.917 | 0.82 | 0.833 | 0.0 | 0.0 |
| api_llm_reactive_replanner | 1.0 | 0.8 | 0.2 | 0.2 | 0.083 | 0.929 | 0.183 | 0.5 | 0.898 | 0.917 | 0.807 | 0.917 | 0.083 | 0.0 |
| utility_planner | 1.0 | 0.75 | 0.25 | 0.25 | 0.0 | 0.85 | 0.25 | 0.0 | 1.0 | 1.0 | 0.713 | 0.667 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.
