# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.833 | 0.951 | 0.049 | 0.049 | 0.0 | 0.758 | 0.736 | 0.817 |  | 0.049 |  | 0.82 | 1.0 | 0.729 | 0.667 | 0.0 | 0.0 |
| api_llm_plan_and_execute | 1.0 | 0.979 | 0.021 | 0.021 | 0.167 | 0.933 | 1.0 | 0.833 |  | 0.021 |  | 1.0 | 0.833 | 0.921 | 1.0 | 0.0 | 0.0 |
| api_llm_react_tool_policy | 1.0 | 0.976 | 0.024 | 0.024 | 0.0 | 0.933 | 1.0 | 0.833 |  | 0.024 |  | 1.0 | 0.833 | 0.919 | 1.0 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 0.783 | 0.217 | 0.217 | 0.167 | 0.592 | 0.57 | 0.643 |  | 0.217 |  | 0.917 | 0.833 | 0.557 | 0.5 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.958 | 0.042 | 0.042 | 0.0 | 0.792 | 0.718 | 0.9 |  | 0.042 |  | 0.942 | 1.0 | 0.783 | 0.75 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.839 | 0.161 | 0.161 | 0.333 | 0.633 | 0.648 | 0.622 |  | 0.161 |  | 0.906 | 1.0 | 0.565 | 0.75 | 0.0 | 0.167 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 16 | 183.786 | 110031 | 19271 | 129302 | True |
| api_llm_plan_and_execute | 6 | 91.121 | 41338 | 10324 | 51662 | True |
| api_llm_react_tool_policy | 41 | 341.815 | 330836 | 36275 | 367111 | True |
| gatsim_official_planner | 17 | 295.396 | 158627 | 23995 | 182622 | True |
| generative_agents_official_planner | 8 | 134.305 | 50688 | 10698 | 61386 | True |
| sotopia_official_llm_agent | 54 | 439.916 | 373139 | 54857 | 427996 | True |
