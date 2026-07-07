# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 0.976 | 0.024 | 0.024 | 0.167 | 0.917 | 0.917 | 0.917 |  | 0.024 |  | 1.0 | 1.0 | 0.898 | 0.917 | 0.0 | 0.167 |
| api_llm_react_tool_policy | 1.0 | 0.958 | 0.042 | 0.042 | 0.167 | 0.933 | 1.0 | 0.833 |  | 0.042 |  | 1.0 | 0.833 | 0.908 | 1.0 | 0.167 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 6 | 63.58 | 41338 | 1698 | 43036 | True |
| api_llm_react_tool_policy | 44 | 198.657 | 356961 | 2972 | 359933 | True |
