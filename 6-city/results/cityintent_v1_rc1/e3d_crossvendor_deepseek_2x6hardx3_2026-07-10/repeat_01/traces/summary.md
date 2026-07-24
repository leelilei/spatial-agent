# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 0.921 | 0.079 | 0.079 | 0.0 | 0.608 | 0.564 | 0.678 |  | 0.079 |  | 0.988 | 1.0 | 0.571 | 0.444 | 0.0 | 0.5 |
| api_llm_react_tool_policy | 1.0 | 0.957 | 0.043 | 0.043 | 0.0 | 0.842 | 0.842 | 0.833 |  | 0.043 |  | 1.0 | 1.0 | 0.809 | 0.917 | 0.0 | 0.5 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 6 | 240.47 | 12970 | 11305 | 24275 | True |
| api_llm_react_tool_policy | 60 | 1306.042 | 224636 | 23425 | 248061 | True |
