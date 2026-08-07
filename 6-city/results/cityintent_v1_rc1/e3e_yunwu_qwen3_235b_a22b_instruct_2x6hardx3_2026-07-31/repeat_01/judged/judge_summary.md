# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.855 | 0.965 | 0.0 | 0.533 | 0.322 | 0.85 | 0.805 | 0.75 |
| api_llm_react_tool_policy | 0.918 | 0.888 | 0.079 | 0.647 | 0.272 | 0.717 | 0.89 | 0.827 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
