# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.795 | 0.875 | 0.0 | 0.645 | 0.15 | 0.9 | 0.855 | 0.69 |
| gatsim_official_planner | 0.885 | 1.0 | 0.0 | 0.82 | 0.065 | 1.0 | 0.68 | 0.885 |
| generative_agents_official_planner | 0.9 | 0.75 | 0.165 | 0.83 | 0.07 | 0.75 | 0.57 | 0.92 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
