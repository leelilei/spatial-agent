# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | judge_plan_plausibility | trace_feasibility | judge_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.629 | 0.92 | 0.0 | 0.912 | 0.7 | 0.664 |
| api_llm_plan_then_act | 0.919 | 1.0 | 0.0 | 0.944 | 0.954 | 0.925 |
| api_llm_reactive_replanner | 0.828 | 1.0 | 0.0 | 1.0 | 0.845 | 0.851 |
| utility_planner | 0.748 | 0.875 | 0.102 | 0.906 | 0.807 | 0.784 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
