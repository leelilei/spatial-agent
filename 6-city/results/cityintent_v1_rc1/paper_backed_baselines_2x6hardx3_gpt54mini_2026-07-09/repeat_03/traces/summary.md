# CityIntent v1.0-rc1 Trace Results

This run includes `api_llm_*` agents, which call a configured real model provider.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 1.0 | 0.897 | 0.102 | 0.102 | 0.167 | 0.592 | 0.529 | 0.678 |  | 0.102 |  | 1.0 | 1.0 | 0.538 | 0.444 | 0.0 | 0.667 |
| api_llm_react_tool_policy | 0.985 | 0.926 | 0.059 | 0.074 | 0.167 | 0.733 | 0.759 | 0.667 |  | 0.074 |  | 1.0 | 0.833 | 0.691 | 0.75 | 0.333 | 0.667 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| api_llm_plan_and_execute | 6 | 61.816 | 42836 | 2466 | 45302 | True |
| api_llm_react_tool_policy | 59 | 453.072 | 508774 | 4086 | 512860 | True |
