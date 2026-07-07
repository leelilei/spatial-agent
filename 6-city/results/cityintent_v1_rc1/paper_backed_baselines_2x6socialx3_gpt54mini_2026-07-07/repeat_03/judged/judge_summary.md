# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.923 | 0.939 | 0.028 | 0.665 | 0.258 | 0.883 | 0.933 | 0.802 |
| api_llm_react_tool_policy | 0.902 | 0.958 | 0.003 | 0.635 | 0.267 | 0.933 | 0.892 | 0.727 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
