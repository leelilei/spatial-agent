# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.943 | 0.057 | 0.057 | 0.0 | 0.883 | 1.0 | 0.721 |  | 0.057 |  | 0.901 | 1.0 | 0.839 | 1.0 | 0.0 | 0.0 |
| api_llm_plan_and_execute | 1.0 | 0.982 | 0.018 | 0.018 | 0.0 | 0.933 | 1.0 | 0.833 |  | 0.018 |  | 1.0 | 0.833 | 0.922 | 1.0 | 0.0 | 0.0 |
| api_llm_react_tool_policy | 1.0 | 0.976 | 0.024 | 0.024 | 0.167 | 0.933 | 1.0 | 0.833 |  | 0.024 |  | 1.0 | 0.833 | 0.919 | 1.0 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 0.801 | 0.199 | 0.199 | 0.167 | 0.65 | 0.667 | 0.643 |  | 0.199 |  | 0.929 | 0.833 | 0.613 | 0.667 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.958 | 0.042 | 0.042 | 0.167 | 0.817 | 0.833 | 0.8 |  | 0.042 |  | 0.898 | 1.0 | 0.796 | 0.833 | 0.0 | 0.167 |
| sotopia_official_llm_agent | 1.0 | 0.811 | 0.19 | 0.19 | 0.5 | 0.558 | 0.635 | 0.443 |  | 0.19 |  | 0.817 | 1.0 | 0.457 | 0.667 | 0.167 | 0.167 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 18 | 295.131 | 121501 | 19989 | 141490 | True |
| api_llm_plan_and_execute | 6 | 97.064 | 41338 | 8115 | 49453 | True |
| api_llm_react_tool_policy | 41 | 390.253 | 326523 | 30548 | 357071 | True |
| gatsim_official_planner | 17 | 331.988 | 156549 | 23293 | 179842 | True |
| generative_agents_official_planner | 10 | 141.251 | 61370 | 12017 | 73387 | True |
| sotopia_official_llm_agent | 60 | 577.429 | 413332 | 55200 | 468532 | True |
