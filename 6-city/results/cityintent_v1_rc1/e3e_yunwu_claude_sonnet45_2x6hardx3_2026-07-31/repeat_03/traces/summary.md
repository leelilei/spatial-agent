# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 0.963 | 0.037 | 0.037 | 0.0 | 0.708 | 0.631 | 0.833 |  | 0.037 |  | 0.951 | 1.0 | 0.689 | 0.611 | 0.0 | 0.667 |
| api_llm_react_tool_policy | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.925 | 0.878 | 1.0 |  | 0.0 |  | 1.0 | 1.0 | 0.925 | 0.917 | 0.0 | 0.333 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 6 | 80.205 | 14157 | 5039 | 19196 | True |
| api_llm_react_tool_policy | 57 | 343.474 | 225099 | 7764 | 232863 | True |
