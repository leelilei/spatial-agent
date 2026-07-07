# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.905 | 0.955 | 0.0 | 0.633 | 0.272 | 0.883 | 0.885 | 0.803 |
| api_llm_react_tool_policy | 0.885 | 0.958 | 0.0 | 0.69 | 0.195 | 0.933 | 0.898 | 0.773 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
