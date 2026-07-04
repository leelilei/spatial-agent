# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.787 | 0.212 | 0.212 | 0.167 | 0.767 | 0.756 | 0.779 |  | 0.212 |  | 0.834 | 1.0 | 0.61 | 1.0 | 0.167 | 0.0 |
| gatsim_official_planner | 1.0 | 0.976 | 0.024 | 0.024 | 0.167 | 0.958 | 1.0 | 0.907 |  | 0.024 |  | 0.571 | 1.0 | 0.941 | 1.0 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.853 | 0.146 | 0.146 | 0.333 | 0.858 | 0.923 | 0.779 |  | 0.146 |  | 0.844 | 1.0 | 0.76 | 1.0 | 0.167 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.805 | 0.195 | 0.195 | 0.167 | 0.425 | 0.09 | 0.81 |  | 0.195 |  | 0.897 | 1.0 | 0.367 | 1.0 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 36 | 248.09 | 251966 | 4629 | 256595 | True |
| gatsim_official_planner | 10 | 317.372 | 90676 | 2898 | 93574 | True |
| generative_agents_official_planner | 22 | 188.301 | 132128 | 3050 | 135178 | True |
| sotopia_official_llm_agent | 24 | 152.483 | 165155 | 442 | 165597 | True |
