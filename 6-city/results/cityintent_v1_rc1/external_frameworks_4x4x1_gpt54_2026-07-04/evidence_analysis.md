# CityIntent Evidence Reliability And Dissociation

A trace is face-plausible when judge score >= 0.70; full task success and full feasibility require score >= 0.999.

## Architecture Table

| Agent | n | Full task | Fully feasible | Plausible | Plausible task failure | Plausible infeasible | pass^k task | pass^k feasible |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 4 | 0.500 | 0.500 | 0.750 | 0.250 | 0.500 | 0.500 | 0.500 |
| GATSim | 4 | 0.500 | 0.250 | 0.500 | 0.250 | 0.500 | 0.500 | 0.250 |
| Generative Agents | 4 | 0.750 | 0.750 | 1.000 | 0.250 | 0.250 | 0.750 | 0.750 |
| SOTOPIA | 4 | 0.250 | 0.500 | 0.750 | 0.500 | 0.500 | 0.250 | 0.500 |

`pass^k` uses all available repeats for each scenario-agent cell.

## Metric Dissociation

| Comparison | n | Pooled Pearson | Pooled Spearman | Within-cell Pearson | Within-cell Spearman |
|---|---:|---:|---:|---:|---:|
| `face_vs_task` | 16 | 0.274 | 0.271 | None | None |
| `face_vs_feasibility` | 16 | -0.235 | -0.108 | None | None |
| `trace_believability_vs_task` | 16 | 0.342 | 0.293 | None | None |
| `trace_believability_vs_feasibility` | 16 | -0.246 | -0.358 | None | None |

## Reading

- No architecture dominates all proof obligations: task completion, feasibility, face plausibility, and repeated reliability rank systems differently.
- Face plausibility is not a valid substitute for environment-owned task or feasibility evidence in this sample.
- These are architecture-by-scenario pilot estimates, not human behavioral realism claims; human construct validation remains a separate release gate.
