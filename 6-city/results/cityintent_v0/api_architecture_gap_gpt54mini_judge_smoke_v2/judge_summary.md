# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| api_llm_direct_actor | 0.68 | 0.75 | 0.0 | 0.34 | 0.34 | 0.85 | 0.74 | 0.52 |
| utility_planner | 0.66 | 1.0 | 0.0 | 0.38 | 0.28 | 1.0 | 0.72 | 0.54 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
