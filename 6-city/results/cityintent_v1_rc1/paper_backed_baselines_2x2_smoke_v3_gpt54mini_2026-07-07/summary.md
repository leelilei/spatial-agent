# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 0.8 | 0.2 | 0.2 | 0.5 | 0.675 | 0.654 | 0.715 |  | 0.2 |  | 1.0 | 1.0 | 0.605 | 0.75 | 0.0 | 0.0 |
| api_llm_react_tool_policy | 1.0 | 0.45 | 0.55 | 0.55 | 0.5 | 0.275 | 0.154 | 0.414 |  | 0.55 |  | 1.0 | 1.0 | 0.158 | 0.25 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 2 | 14.514 | 12964 | 458 | 13422 | True |
| api_llm_react_tool_policy | 18 | 106.057 | 141329 | 1248 | 142577 | True |
