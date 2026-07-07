# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.902 | 0.976 | 0.0 | 0.695 | 0.207 | 0.917 | 0.928 | 0.853 |
| api_llm_react_tool_policy | 0.84 | 0.958 | 0.0 | 0.663 | 0.177 | 0.933 | 0.863 | 0.743 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
