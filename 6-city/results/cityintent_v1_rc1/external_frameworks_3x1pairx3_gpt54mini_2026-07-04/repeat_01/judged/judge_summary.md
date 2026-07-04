# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.955 | 0.875 | 0.09 | 0.925 | 0.03 | 0.9 | 0.98 | 0.94 |
| gatsim_official_planner | 0.66 | 1.0 | 0.0 | 0.47 | 0.19 | 1.0 | 0.565 | 0.58 |
| generative_agents_official_planner | 0.925 | 0.75 | 0.19 | 0.755 | 0.17 | 0.75 | 0.6 | 0.84 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
