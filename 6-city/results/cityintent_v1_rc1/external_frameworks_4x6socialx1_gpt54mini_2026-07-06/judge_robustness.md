# CityIntent Plausibility-Judge Robustness

Judges: `gpt54mini` and `gpt54`. Binary agreement uses threshold >= 0.70.

| Metric | n | Baseline mean | Candidate mean | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `face_plausibility` | 72 | 0.816 | 0.727 | 0.136 | 0.566 | 0.516 | 0.681 | 0.098 |
| `trace_believability` | 72 | 0.413 | 0.472 | 0.207 | 0.433 | 0.441 | 0.778 | 0.253 |
| `rationale_alignment` | 72 | 0.706 | 0.484 | 0.291 | 0.443 | 0.483 | 0.569 | 0.271 |
| `urban_common_sense` | 72 | 0.594 | 0.658 | 0.172 | 0.557 | 0.549 | 0.667 | 0.344 |

## Interpretation

- Cross-judge agreement is only moderate, so soft plausibility scores must be reported with evaluator identity and sensitivity analysis.
- Deterministic task, feasibility, resource, and state-transition scores remain unchanged across judges.
- This robustness check strengthens the case for the two-person human audit; it does not replace that release gate.
