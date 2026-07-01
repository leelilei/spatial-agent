# CityIntent v0.3 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.661 | 0.339 | 0.339 | 0.5 | 0.625 | 0.339 | 0.0 | 0.845 | 1.0 | 0.384 | 0.75 | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.788 | 0.0 | 1.0 | 0.908 | 1.0 | 0.788 | 0.25 | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 0.819 | 0.181 | 0.181 | 0.5 | 0.7 | 0.181 | 0.0 | 0.905 | 1.0 | 0.586 | 0.75 | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.875 | 0.125 | 0.125 | 0.25 | 0.562 | 0.125 | 1.0 | 0.919 | 1.0 | 0.475 | 0.5 | 0.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 26 | 437.099 | 175151 | 4840 | 179991 | True |
| gatsim_official_planner | 7 | 66.5 | 61303 | 2440 | 63743 | True |
| generative_agents_official_planner | 16 | 154.46 | 91801 | 3089 | 94890 | True |
| sotopia_official_llm_agent | 21 | 81.402 | 139309 | 814 | 140123 | True |
