# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.843 | 0.963 | 0.0 | 0.48 | 0.363 | 0.708 | 0.78 | 0.645 |
| api_llm_react_tool_policy | 0.935 | 1.0 | 0.0 | 0.662 | 0.273 | 0.925 | 0.952 | 0.803 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
