# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 | 1.0 |  | 0.0 |  | 1.0 | 1.0 | 1.0 | 1.0 | 0.0 | 0.0 |
| api_llm_react_tool_policy | 1.0 | 0.111 | 0.889 | 0.889 | 1.0 | 0.2 | 0.0 | 0.4 |  | 0.889 |  | 1.0 | 1.0 | 0.022 | 0.0 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 1 | 7.561 | 6453 | 228 | 6681 | True |
| api_llm_react_tool_policy | 9 | 36.087 | 69992 | 509 | 70501 | True |
