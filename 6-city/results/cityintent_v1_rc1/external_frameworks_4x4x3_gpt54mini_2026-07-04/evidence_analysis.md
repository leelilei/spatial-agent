# CityIntent Evidence Reliability And Dissociation

A trace is face-plausible when judge score >= 0.70; full task success and full feasibility require score >= 0.999.

## Architecture Table

| Agent | n | Full task | Fully feasible | Plausible | Plausible task failure | Plausible infeasible | pass^k task | pass^k feasible |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 12 | 0.583 | 0.250 | 1.000 | 0.417 | 0.750 | 0.250 | 0.250 |
| GATSim | 12 | 0.667 | 0.583 | 0.583 | 0.167 | 0.333 | 0.500 | 0.250 |
| Generative Agents | 12 | 0.417 | 0.000 | 0.667 | 0.500 | 0.667 | 0.250 | 0.000 |
| SOTOPIA | 12 | 0.000 | 0.750 | 0.833 | 0.833 | 0.250 | 0.000 | 0.500 |

`pass^k` uses all available repeats for each scenario-agent cell.

## Metric Dissociation

| Comparison | n | Pooled Pearson | Pooled Spearman | Within-cell Pearson | Within-cell Spearman |
|---|---:|---:|---:|---:|---:|
| `face_vs_task` | 48 | -0.041 | 0.055 | -0.048 | 0.005 |
| `face_vs_feasibility` | 48 | -0.262 | -0.277 | -0.341 | -0.238 |
| `trace_believability_vs_task` | 48 | 0.223 | 0.217 | 0.138 | 0.17 |
| `trace_believability_vs_feasibility` | 48 | -0.341 | -0.408 | -0.451 | -0.304 |

## Reading

- No architecture dominates all proof obligations: task completion, feasibility, face plausibility, and repeated reliability rank systems differently.
- Face plausibility is not a valid substitute for environment-owned task or feasibility evidence in this sample.
- These are architecture-by-scenario pilot estimates, not human behavioral realism claims; human construct validation remains a separate release gate.
