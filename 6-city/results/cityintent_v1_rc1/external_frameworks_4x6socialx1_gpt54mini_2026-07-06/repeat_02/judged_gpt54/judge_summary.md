# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.803 | 0.655 | 0.19 | 0.552 | 0.252 | 0.433 | 0.783 | 0.762 |
| gatsim_official_planner | 0.752 | 0.785 | 0.067 | 0.553 | 0.198 | 0.65 | 0.473 | 0.637 |
| generative_agents_official_planner | 0.653 | 0.602 | 0.143 | 0.418 | 0.235 | 0.308 | 0.298 | 0.615 |
| sotopia_official_llm_agent | 0.59 | 0.896 | 0.002 | 0.287 | 0.303 | 0.4 | 0.278 | 0.463 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
