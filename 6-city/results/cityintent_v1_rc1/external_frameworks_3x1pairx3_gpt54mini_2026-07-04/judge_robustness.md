# CityIntent Plausibility-Judge Robustness

Judges: `gpt54mini` and `gpt54`. Binary agreement uses threshold >= 0.70.

| Metric | n | Baseline mean | Candidate mean | MAE | Pearson | Spearman | Threshold agreement | Kappa |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `face_plausibility` | 18 | 0.844 | 0.842 | 0.099 | 0.354 | 0.676 | 0.722 | -0.154 |
| `trace_believability` | 18 | 0.638 | 0.721 | 0.207 | 0.426 | 0.581 | 0.667 | 0.333 |
| `rationale_alignment` | 18 | 0.651 | 0.642 | 0.217 | 0.634 | 0.749 | 0.722 | 0.458 |
| `urban_common_sense` | 18 | 0.750 | 0.821 | 0.164 | 0.278 | 0.615 | 0.611 | -0.033 |

## Interpretation

- Cross-judge agreement is only moderate, so soft plausibility scores must be reported with evaluator identity and sensitivity analysis.
- Deterministic task, feasibility, resource, and state-transition scores remain unchanged across judges.
- This robustness check strengthens the case for the two-person human audit; it does not replace that release gate.
