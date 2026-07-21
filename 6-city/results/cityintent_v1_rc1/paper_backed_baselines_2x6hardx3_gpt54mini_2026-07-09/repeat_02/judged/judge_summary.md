# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.858 | 0.937 | 0.009 | 0.547 | 0.312 | 0.642 | 0.838 | 0.702 |
| api_llm_react_tool_policy | 0.857 | 0.967 | 0.0 | 0.563 | 0.293 | 0.758 | 0.817 | 0.71 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
