# Result integration QA — round 5

## Decision integrity

- Selection protocol frozen before missingness-arm predictions: yes.
- Same 25% class-balanced annotation budget used in all four arms: yes.
- Same fixed nine-epoch training budget used in all four arms: yes.
- Hyperparameter search after observing results: no.
- Official test images decoded or encoded: 0.
- Pre-registered −2pp / +0.10 harm gate applied without relaxation: yes.
- Replication and correction arms stopped after the harm gate failed: yes.

## Claim control

- Supported: all four partial-keypoint arms improve over the stored Global
  reference by 4.40–5.15pp OOF balanced accuracy.
- Supported: under the current 25% regime, MAR-X, MNAR-Z, and SI-HARD do not
  underperform equal-budget MCAR.
- Supported: the manipulation changes image typicality or keypoint
  completeness, so the comparison is not based on identical selections.
- Prohibited: claiming that non-random missingness is harmless in general.
- Prohibited: claiming that a correction method works; none was run.
- Prohibited: tuning a correction method before a separately frozen stressor
  first establishes reproducible harm relative to MCAR.

## Next-round gate

Any continuation must modify and freeze the missingness stressor rather than
the correction. The clearest candidate is one annotated image per class with
pose/background support isolation and an explicit support-separation
manipulation check. If this also fails, H1 should be narrowed or abandoned.

## Scores

| Dimension | Score / 10 |
|---|---:|
| Traceability | 9.8 |
| Protocol fidelity | 9.8 |
| Claim calibration | 9.7 |
| Negative-result reporting | 9.7 |
| Stopping-rule compliance | 9.9 |

Average: **9.78 / 10**.
