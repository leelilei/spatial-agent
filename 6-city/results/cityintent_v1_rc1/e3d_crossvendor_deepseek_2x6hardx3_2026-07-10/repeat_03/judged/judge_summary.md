# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_plan_and_execute | 0.797 | 0.937 | 0.012 | 0.457 | 0.34 | 0.642 | 0.727 | 0.648 |
| api_llm_react_tool_policy | 0.877 | 1.0 | 0.0 | 0.622 | 0.255 | 0.925 | 0.882 | 0.745 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
