# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.795 | 0.75 | 0.06 | 0.615 | 0.18 | 0.75 | 0.7 | 0.75 |
| gatsim_official_planner | 0.815 | 1.0 | 0.0 | 0.7 | 0.115 | 1.0 | 0.57 | 0.825 |
| generative_agents_official_planner | 0.895 | 0.834 | 0.076 | 0.78 | 0.115 | 0.75 | 0.545 | 0.905 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
