# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | judge_plan_plausibility | trace_feasibility | judge_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.34 | 0.75 | 0.0 | 0.85 | 0.72 | 0.46 |
| utility_planner | 0.55 | 1.0 | 0.0 | 1.0 | 0.72 | 0.78 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
