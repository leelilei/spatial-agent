# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.943 | 0.057 | 0.057 | 0.333 | 0.708 | 0.646 | 0.833 |  | 0.057 |  | 0.956 | 1.0 | 0.67 | 0.583 | 0.0 | 0.333 |
| gatsim_official_planner | 1.0 | 0.926 | 0.074 | 0.074 | 0.0 | 0.817 | 0.75 | 0.917 |  | 0.074 |  | 0.917 | 1.0 | 0.802 | 0.75 | 0.0 | 0.167 |
| generative_agents_official_planner | 1.0 | 0.907 | 0.093 | 0.093 | 0.333 | 0.667 | 0.612 | 0.762 |  | 0.093 |  | 1.0 | 1.0 | 0.618 | 0.528 | 0.0 | 0.333 |
| sotopia_official_llm_agent | 1.0 | 0.931 | 0.069 | 0.069 | 0.167 | 0.642 | 0.58 | 0.762 |  | 0.069 |  | 0.948 | 1.0 | 0.604 | 0.361 | 0.0 | 0.333 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 22 | 300.618 | 154957 | 32859 | 187816 | True |
| gatsim_official_planner | 11 | 181.711 | 101862 | 18839 | 120701 | True |
| generative_agents_official_planner | 16 | 233.147 | 99206 | 23134 | 122340 | True |
| sotopia_official_llm_agent | 64 | 563.509 | 450454 | 66484 | 516938 | True |
