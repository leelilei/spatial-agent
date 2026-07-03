# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.742 | 0.705 | 0.13 | 0.515 | 0.228 | 0.725 | 0.675 | 0.69 |
| gatsim_official_planner | 0.635 | 1.0 | 0.0 | 0.57 | 0.065 | 0.787 | 0.432 | 0.665 |
| generative_agents_official_planner | 0.67 | 0.701 | 0.108 | 0.44 | 0.23 | 0.637 | 0.307 | 0.635 |
| sotopia_official_llm_agent | 0.725 | 0.817 | 0.116 | 0.427 | 0.297 | 0.613 | 0.422 | 0.575 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
