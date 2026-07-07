# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.883 | 0.517 | 0.378 | 0.547 | 0.337 | 0.467 | 0.902 | 0.705 |
| gatsim_official_planner | 0.795 | 0.829 | 0.077 | 0.363 | 0.432 | 0.65 | 0.605 | 0.452 |
| generative_agents_official_planner | 0.847 | 0.674 | 0.237 | 0.455 | 0.392 | 0.325 | 0.552 | 0.658 |
| sotopia_official_llm_agent | 0.853 | 0.925 | 0.03 | 0.438 | 0.415 | 0.4 | 0.74 | 0.623 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
