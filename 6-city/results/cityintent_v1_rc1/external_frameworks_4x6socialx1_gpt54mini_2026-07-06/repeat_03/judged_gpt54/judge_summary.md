# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.788 | 0.517 | 0.292 | 0.508 | 0.28 | 0.467 | 0.69 | 0.73 |
| gatsim_official_planner | 0.75 | 0.829 | 0.057 | 0.567 | 0.183 | 0.65 | 0.558 | 0.647 |
| generative_agents_official_planner | 0.748 | 0.674 | 0.126 | 0.552 | 0.197 | 0.325 | 0.453 | 0.717 |
| sotopia_official_llm_agent | 0.743 | 0.925 | 0.012 | 0.363 | 0.38 | 0.4 | 0.373 | 0.685 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
