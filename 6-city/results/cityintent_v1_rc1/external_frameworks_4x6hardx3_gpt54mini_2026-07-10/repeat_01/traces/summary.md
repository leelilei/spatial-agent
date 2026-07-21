# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.792 | 0.208 | 0.208 | 0.333 | 0.408 | 0.247 | 0.667 |  | 0.208 |  | 0.975 | 1.0 | 0.352 | 0.139 | 0.0 | 0.167 |
| gatsim_official_planner | 1.0 | 0.905 | 0.095 | 0.095 | 0.0 | 0.817 | 0.75 | 0.917 |  | 0.095 |  | 0.942 | 1.0 | 0.798 | 0.75 | 0.0 | 0.167 |
| generative_agents_official_planner | 1.0 | 0.743 | 0.257 | 0.257 | 0.333 | 0.467 | 0.349 | 0.667 |  | 0.257 |  | 0.88 | 1.0 | 0.371 | 0.083 | 0.0 | 0.333 |
| sotopia_official_llm_agent | 1.0 | 0.869 | 0.131 | 0.131 | 0.0 | 0.317 | 0.091 | 0.678 |  | 0.131 |  | 0.809 | 1.0 | 0.286 | 0.083 | 0.333 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 32 | 401.369 | 208379 | 5389 | 213768 | True |
| gatsim_official_planner | 11 | 263.936 | 96368 | 3108 | 99476 | True |
| generative_agents_official_planner | 24 | 582.465 | 133707 | 3756 | 137463 | True |
| sotopia_official_llm_agent | 49 | 667.069 | 335243 | 1252 | 336495 | True |
