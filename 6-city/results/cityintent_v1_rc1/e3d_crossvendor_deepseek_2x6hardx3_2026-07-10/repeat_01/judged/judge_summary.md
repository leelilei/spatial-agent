# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.84 | 0.921 | 0.006 | 0.432 | 0.408 | 0.608 | 0.833 | 0.738 |
| api_llm_react_tool_policy | 0.82 | 0.957 | 0.0 | 0.52 | 0.3 | 0.842 | 0.793 | 0.678 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
