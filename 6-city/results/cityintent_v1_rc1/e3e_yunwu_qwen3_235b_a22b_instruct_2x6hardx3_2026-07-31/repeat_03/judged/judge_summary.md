# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.87 | 0.953 | 0.005 | 0.552 | 0.318 | 0.783 | 0.79 | 0.748 |
| api_llm_react_tool_policy | 0.86 | 0.965 | 0.0 | 0.572 | 0.288 | 0.825 | 0.855 | 0.738 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
