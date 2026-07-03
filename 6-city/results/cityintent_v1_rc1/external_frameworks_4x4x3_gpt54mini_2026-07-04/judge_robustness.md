# CityIntent Plausibility-Judge Robustness

Judges: `gpt54mini` and `gpt54`. Binary agreement uses threshold >= 0.70.

| Metric | n | Baseline mean | Candidate mean | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `face_plausibility` | 48 | 0.727 | 0.694 | 0.176 | 0.47 | 0.432 | 0.729 | 0.373 |
| `trace_believability` | 48 | 0.367 | 0.486 | 0.207 | 0.497 | 0.457 | 0.729 | 0.246 |
| `rationale_alignment` | 48 | 0.547 | 0.457 | 0.243 | 0.528 | 0.548 | 0.646 | 0.308 |
| `urban_common_sense` | 48 | 0.578 | 0.630 | 0.200 | 0.451 | 0.396 | 0.625 | 0.254 |

## Interpretation

- Cross-judge agreement is only moderate, so soft plausibility scores must be reported with evaluator identity and sensitivity analysis.
- Deterministic task, feasibility, resource, and state-transition scores remain unchanged across judges.
- This robustness check strengthens the case for the two-person human audit; it does not replace that release gate.
