# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.627 | 0.83 | 0.041 | 0.408 | 0.218 | 0.475 | 0.738 | 0.543 |
| gatsim_official_planner | 0.787 | 0.905 | 0.052 | 0.568 | 0.218 | 0.817 | 0.633 | 0.648 |
| generative_agents_official_planner | 0.74 | 0.816 | 0.063 | 0.493 | 0.247 | 0.575 | 0.22 | 0.665 |
| sotopia_official_llm_agent | 0.66 | 0.834 | 0.02 | 0.368 | 0.292 | 0.35 | 0.452 | 0.492 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
