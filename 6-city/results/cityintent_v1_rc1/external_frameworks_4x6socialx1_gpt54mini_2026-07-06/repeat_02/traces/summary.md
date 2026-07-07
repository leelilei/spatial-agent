# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.655 | 0.345 | 0.345 | 0.5 | 0.433 | 0.269 | 0.626 |  | 0.345 |  | 0.801 | 1.0 | 0.339 | 0.333 | 0.0 | 0.167 |
| gatsim_official_planner | 1.0 | 0.785 | 0.215 | 0.215 | 0.167 | 0.65 | 0.667 | 0.643 |  | 0.215 |  | 0.784 | 0.833 | 0.611 | 0.667 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.602 | 0.398 | 0.398 | 1.0 | 0.308 | 0.2 | 0.443 |  | 0.398 |  | 0.928 | 1.0 | 0.183 | 0.333 | 0.0 | 0.167 |
| sotopia_official_llm_agent | 1.0 | 0.896 | 0.104 | 0.104 | 0.0 | 0.4 | 0.103 | 0.817 |  | 0.104 |  | 0.825 | 1.0 | 0.379 | 0.167 | 0.167 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 38 | 250.121 | 264726 | 5868 | 270594 | True |
| gatsim_official_planner | 17 | 144.106 | 157963 | 3725 | 161688 | True |
| generative_agents_official_planner | 36 | 238.35 | 212684 | 5519 | 218203 | True |
| sotopia_official_llm_agent | 38 | 181.148 | 261217 | 977 | 262194 | True |
