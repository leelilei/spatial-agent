# CityIntent v1.0-rc1 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | task_completion | constraint_satisfaction | process_success | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.627 | 0.373 | 0.373 | 0.417 | 0.613 | 0.528 | 0.894 | 0.0 | 0.373 | 0.0 | 0.807 | 1.0 | 0.451 | 0.333 | 0.083 | 0.0 |
| gatsim_official_planner | 1.0 | 0.943 | 0.057 | 0.057 | 0.083 | 0.862 | 0.84 | 0.952 | 0.667 | 0.057 | 1.0 | 0.727 | 1.0 | 0.845 | 0.583 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.691 | 0.309 | 0.309 | 0.75 | 0.613 | 0.537 | 0.894 | 0.0 | 0.309 | 0.0 | 0.899 | 1.0 | 0.444 | 0.417 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.838 | 0.163 | 0.163 | 0.0 | 0.438 | 0.098 | 1.0 | 0.333 | 0.163 | 0.5 | 0.955 | 1.0 | 0.372 | 0.417 | 0.083 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 82 | 510.837 | 569185 | 12952 | 582137 | True |
| gatsim_official_planner | 23 | 246.76 | 208151 | 6631 | 214782 | True |
| generative_agents_official_planner | 58 | 330.291 | 341387 | 8376 | 349763 | True |
| sotopia_official_llm_agent | 56 | 232.974 | 383467 | 1685 | 385152 | True |
