# CityIntent v0 Plausibility Judge Results

This is a second-pass LLM judge over existing traces. It does not replace deterministic validation.

## Aggregate

| agent_type | face_plausibility | trace_feasibility | face_feasibility_gap | trace_believability | face_believability_gap | goal_completion | rationale_alignment | urban_common_sense |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| agentsociety_official_plan_blocks | 0.71 | 0.792 | 0.069 | 0.428 | 0.282 | 0.408 | 0.745 | 0.508 |
| gatsim_official_planner | 0.692 | 0.905 | 0.058 | 0.387 | 0.305 | 0.817 | 0.462 | 0.472 |
| generative_agents_official_planner | 0.627 | 0.743 | 0.081 | 0.397 | 0.23 | 0.467 | 0.452 | 0.528 |
| sotopia_official_llm_agent | 0.617 | 0.869 | 0.0 | 0.337 | 0.28 | 0.317 | 0.568 | 0.467 |

## Scenario-Level Rows

See `judge_summary.csv` and `judged_traces.json` in this directory.
