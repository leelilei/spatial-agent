# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.92 | 0.966 | 0.006 | 0.617 | 0.303 | 0.85 | 0.93 | 0.752 |
| api_llm_react_tool_policy | 0.892 | 1.0 | 0.0 | 0.613 | 0.278 | 0.875 | 0.872 | 0.703 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
