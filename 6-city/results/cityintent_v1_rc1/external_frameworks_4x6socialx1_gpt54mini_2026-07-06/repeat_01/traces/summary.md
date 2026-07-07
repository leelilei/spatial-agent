# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.673 | 0.327 | 0.327 | 0.5 | 0.417 | 0.269 | 0.622 |  | 0.327 |  | 0.944 | 1.0 | 0.344 | 0.333 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 0.843 | 0.157 | 0.157 | 0.333 | 0.65 | 0.667 | 0.643 |  | 0.157 |  | 0.77 | 0.833 | 0.62 | 0.667 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.723 | 0.277 | 0.277 | 1.0 | 0.333 | 0.288 | 0.36 |  | 0.277 |  | 0.94 | 0.833 | 0.246 | 0.25 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.919 | 0.081 | 0.081 | 0.0 | 0.35 | 0.103 | 0.717 |  | 0.081 |  | 0.813 | 1.0 | 0.334 | 0.167 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 38 | 236.377 | 264682 | 5443 | 270125 | True |
| gatsim_official_planner | 13 | 116.781 | 119391 | 3177 | 122568 | True |
| generative_agents_official_planner | 22 | 137.129 | 130539 | 3094 | 133633 | True |
| sotopia_official_llm_agent | 36 | 165.244 | 247574 | 924 | 248498 | True |
