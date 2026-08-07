# Result integration QA — round 6

## Decision integrity

- Severe protocol frozen before new predictions: yes.
- One annotated image per class and fold-training set in every arm: yes.
- Same fold seeds and fixed nine-epoch budget in every arm: yes.
- Manipulation checks show strong covariate/support separation: yes.
- Official test images decoded or encoded: 0.
- Pre-registered −2pp / +0.10 gate applied without relaxation: yes.
- Further synthetic-harm and correction arms stopped after No-Go: yes.

## Claim control

- Supported: one random keypoint-annotated image per class improves OOF BA by
  4.20pp over Global and retains most of the +5.50pp Full-Oracle ceiling.
- Supported: strong atypicality, incompleteness, and pose selection change BA
  by only −0.55 to +0.20pp relative to MCAR-1 in this screen.
- Prohibited: claiming that selection never matters outside CUB/PrPool.
- Prohibited: claiming a successful MNAR correction method.
- Prohibited: creating progressively more adverse synthetic masks solely to
  force the original hypothesis to pass.

## Direction decision

Stop the current synthetic-MNAR correction route. The evidence supports a
pivot toward sparse keypoint annotation value and sample-selection robustness,
or requires a different benchmark with independently established real
selection harm.

## Scores

| Dimension | Score / 10 |
|---|---:|
| Traceability | 9.8 |
| Protocol fidelity | 9.9 |
| Claim calibration | 9.8 |
| Negative-result reporting | 9.8 |
| Stopping-rule compliance | 10.0 |

Average: **9.86 / 10**.
