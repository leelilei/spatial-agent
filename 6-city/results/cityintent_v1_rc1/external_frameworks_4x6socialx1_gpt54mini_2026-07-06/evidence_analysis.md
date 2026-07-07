# CityIntent Evidence Reliability And Dissociation

A trace is face-plausible when judge score >= 0.70; full task success and full feasibility require score >= 0.999.

## Architecture Table

| Agent | n | Full task | Fully feasible | Plausible | Plausible task failure | Plausible infeasible | pass^k task | pass^k feasible |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| AgentSociety | 18 | 0.222 | 0.278 | 1.000 | 0.778 | 0.722 | 0.167 | 0.167 |
| GATSim | 18 | 0.667 | 0.500 | 0.833 | 0.278 | 0.333 | 0.667 | 0.500 |
| Generative Agents | 18 | 0.056 | 0.056 | 0.778 | 0.722 | 0.722 | 0.000 | 0.000 |
| SOTOPIA | 18 | 0.000 | 0.611 | 0.889 | 0.889 | 0.389 | 0.000 | 0.500 |

`pass^k` uses all available repeats for each scenario-agent cell.

## Metric Dissociation

| Comparison | n | Pooled Pearson | Pooled Spearman | Within-cell Pearson | Within-cell Spearman |
|---|---:|---:|---:|---:|---:|
| `face_vs_task` | 72 | 0.141 | 0.16 | -0.077 | -0.116 |
| `face_vs_feasibility` | 72 | -0.057 | 0.01 | -0.176 | -0.029 |
| `trace_believability_vs_task` | 72 | 0.207 | 0.288 | -0.183 | -0.193 |
| `trace_believability_vs_feasibility` | 72 | 0.106 | 0.094 | 0.009 | -0.118 |

## Reading

- No architecture dominates all proof obligations: task completion, feasibility, face plausibility, and repeated reliability rank systems differently.
- Face plausibility is not a valid substitute for environment-owned task or feasibility evidence in this sample.
- These are architecture-by-scenario pilot estimates, not human behavioral realism claims; human construct validation remains a separate release gate.
