# CityIntent Evidence Reliability And Dissociation

A trace is face-plausible when judge score >= 0.70; full task success and full feasibility require score >= 0.999.

## Architecture Table

| Agent | n | Full task | Fully feasible | Plausible | Plausible task failure | Plausible infeasible | pass^k task | pass^k feasible |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 6 | 0.667 | 0.500 | 1.000 | 0.333 | 0.500 | 0.500 | 0.500 |
| GATSim | 6 | 1.000 | 1.000 | 0.500 | 0.000 | 0.000 | 1.000 | 1.000 |
| Generative Agents | 6 | 0.500 | 0.500 | 1.000 | 0.500 | 0.500 | 0.500 | 0.500 |

`pass^k` uses all available repeats for each scenario-agent cell.

## Metric Dissociation

| Comparison | n | Pooled Pearson | Pooled Spearman | Within-cell Pearson | Within-cell Spearman |
|---|---:|---:|---:|---:|---:|
| `face_vs_task` | 18 | 0.074 | 0.323 | 0.268 | 0.409 |
| `face_vs_feasibility` | 18 | 0.052 | 0.29 | 0.306 | 0.284 |
| `trace_believability_vs_task` | 18 | 0.177 | 0.216 | 0.463 | 0.407 |
| `trace_believability_vs_feasibility` | 18 | 0.155 | 0.191 | 0.621 | 0.527 |

## Reading

- No architecture dominates all proof obligations: task completion, feasibility, face plausibility, and repeated reliability rank systems differently.
- Face plausibility is not a valid substitute for environment-owned task or feasibility evidence in this sample.
- These are architecture-by-scenario pilot estimates, not human behavioral realism claims; human construct validation remains a separate release gate.
