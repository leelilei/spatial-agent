# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.88 | 0.985 | 0.0 | 0.732 | 0.148 | 0.933 | 0.923 | 0.78 |
| api_llm_react_tool_policy | 0.907 | 0.983 | 0.0 | 0.702 | 0.205 | 0.808 | 0.902 | 0.768 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
