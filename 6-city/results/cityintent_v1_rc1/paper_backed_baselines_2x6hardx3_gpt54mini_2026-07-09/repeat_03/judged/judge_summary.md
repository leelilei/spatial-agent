# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.927 | 0.897 | 0.051 | 0.547 | 0.38 | 0.592 | 0.92 | 0.81 |
| api_llm_react_tool_policy | 0.858 | 0.926 | 0.015 | 0.493 | 0.365 | 0.733 | 0.772 | 0.682 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
