# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.884 | 0.117 | 0.117 | 0.167 | 0.667 | 0.674 | 0.678 |  | 0.117 |  | 0.942 | 1.0 | 0.592 | 0.583 | 0.0 | 0.333 |
| gatsim_official_planner | 1.0 | 0.972 | 0.028 | 0.028 | 0.0 | 0.775 | 0.686 | 0.917 |  | 0.028 |  | 0.917 | 1.0 | 0.769 | 0.583 | 0.0 | 0.167 |
| generative_agents_official_planner | 1.0 | 0.915 | 0.085 | 0.085 | 0.333 | 0.675 | 0.636 | 0.762 |  | 0.085 |  | 0.986 | 1.0 | 0.612 | 0.417 | 0.0 | 0.167 |
| sotopia_official_llm_agent | 1.0 | 0.9 | 0.1 | 0.1 | 0.5 | 0.625 | 0.584 | 0.678 |  | 0.1 |  | 0.957 | 1.0 | 0.563 | 0.5 | 0.0 | 0.333 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 30 | 396.991 | 212090 | 49423 | 261513 | True |
| gatsim_official_planner | 8 | 125.964 | 72407 | 16187 | 88594 | True |
| generative_agents_official_planner | 16 | 179.469 | 99231 | 20488 | 119719 | True |
| sotopia_official_llm_agent | 67 | 450.925 | 470191 | 70054 | 540245 | True |
