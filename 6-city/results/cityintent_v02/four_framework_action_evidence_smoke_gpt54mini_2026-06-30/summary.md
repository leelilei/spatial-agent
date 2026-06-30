# CityIntent v0.2 Trace Results

This run includes verified external-framework adapters: `agentsociety_official_plan_blocks`, `gatsim_official_planner`, `generative_agents_official_planner`, `sotopia_official_llm_agent`.

Controlled agents without `model_info` remain offline architecture proxies, not real model or external-framework results.

## Aggregate Metrics

| agent_type | plan_plausibility | trace_feasibility | plausibility_feasibility_gap | impossible_trace_rate | city_false_continue | goal_completion | feasibility_violation | replanning_success | travel_efficiency | budget_consistency | intention_consistency | social_appropriateness | done_state_loop_rate | social_derailment_rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 1.0 | 0.8 | 0.2 | 0.2 | 0.0 | 0.5 | 0.2 |  | 1.0 | 1.0 | 0.4 |  | 0.0 | 0.0 |
| gatsim_official_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 |  | 1.0 | 1.0 | 1.0 |  | 0.0 | 0.0 |
| generative_agents_official_planner | 1.0 | 1.0 | 0.0 | 0.0 | 0.0 | 0.55 | 0.0 |  | 1.0 | 1.0 | 0.55 |  | 0.0 | 0.0 |
| sotopia_official_llm_agent | 1.0 | 0.6 | 0.4 | 0.4 | 0.0 | 0.55 | 0.2 |  | 1.0 | 1.0 | 0.44 |  | 1.0 | 0.0 |

## Scenario-Level Rows

See `summary.csv` and `traces.jsonl` in this directory.

## LLM Telemetry

| agent_type | calls | latency_seconds | input_tokens | output_tokens | total_tokens | provider_usage_complete |
|---|---:|---:|---:|---:|---:|---|
| agentsociety_official_plan_blocks | 4 | 24.858 | 26476 | 919 | 27395 | True |
| gatsim_official_planner | 1 | 9.404 | 8545 | 441 | 8986 | True |
| generative_agents_official_planner | 1 | 19.036 | 6292 | 431 | 6723 | True |
| sotopia_official_llm_agent | 6 | 18.814 | 39618 | 139 | 39757 | True |
