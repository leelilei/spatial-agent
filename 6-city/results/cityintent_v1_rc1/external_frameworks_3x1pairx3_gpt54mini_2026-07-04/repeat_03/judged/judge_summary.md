# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.9 | 0.75 | 0.18 | 0.7 | 0.2 | 0.75 | 0.925 | 0.835 |
| gatsim_official_planner | 0.755 | 1.0 | 0.0 | 0.3 | 0.455 | 1.0 | 0.38 | 0.38 |
| generative_agents_official_planner | 0.905 | 0.834 | 0.082 | 0.795 | 0.11 | 0.75 | 0.6 | 0.85 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
