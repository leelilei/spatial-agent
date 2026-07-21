# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.883 | 0.893 | 0.039 | 0.54 | 0.343 | 0.575 | 0.917 | 0.75 |
| api_llm_react_tool_policy | 0.742 | 0.83 | 0.077 | 0.403 | 0.338 | 0.692 | 0.725 | 0.615 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
