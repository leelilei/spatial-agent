# Result integration QA — round 2

## Decision integrity

- Pre-registered Oracle threshold applied without post-validation relaxation: yes.
- Validation opened after manifest/grid/hyperparameter freeze: yes.
- Validation reused for selection after failure: no.
- Test images decoded or encoded: 0.
- Failed Oracle gate reported as current-mechanism No-Go: yes.
- Research question distinguished from failed implementation: yes.

## Claim control

- Supported: the current frozen-CLIP linear part residual gives a small,
  directionally consistent mean benefit (+0.7407 pp).
- Supported: it fails the +2 pp Oracle threshold and causes −11.1111 pp
  worst-class harm in every validation seed.
- Prohibited: claiming MNAR correction works, because downstream missingness
  arms were correctly stopped.
- Prohibited: claiming the overall research direction is disproved.

## Next-round gate

The next experiment must change the mechanism family and establish a new
train-only development split. A canonical Privileged Pooling-style reference
with limited backbone adaptation must pass the full-part Oracle ceiling before
any MCAR/MAR/MNAR correction is run.

## Scores

| Dimension | Score / 10 |
|---|---:|
| Traceability | 9.2 |
| Protocol fidelity | 9.4 |
| Claim calibration | 9.1 |
| Negative-result reporting | 9.3 |
| Next-step falsifiability | 8.8 |

Average: **9.16 / 10**.

