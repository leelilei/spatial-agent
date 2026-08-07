# Result integration QA — round 4

## Decision integrity

- CUB protocol frozen before extraction and predictions: yes.
- Official archive byte count and MD5 verified: yes.
- Official train used for the development gate: yes.
- Official test images decoded or encoded: 0.
- Same backbone adaptation budget used in both arms: yes.
- Pre-registered +2 pp gate applied without relaxation: yes.
- Five-fold directions all positive: yes.

## Claim control

- Supported: full-keypoint PrPool raises train-only 10-shot OOF BA from 65.45%
  to 70.95%, a +5.50 pp gain.
- Supported: a positive privileged-part ceiling exists in this CUB setup.
- Supported: mean improvement coexists with class-level negative transfer.
- Prohibited: claiming the mechanism is safe; 23% of classes decline.
- Prohibited: claiming a missingness correction result; no MCAR/MAR/MNAR arm
  has yet been evaluated.
- Prohibited: reporting official CUB test performance.

## Next-round gate

Freeze the CUB mechanism and diagnostic budget. Compare equal-budget MCAR,
MAR-X, MNAR-Z, and support-isolation before implementing a new correction
method. Continue to keep official test unopened.

## Scores

| Dimension | Score / 10 |
|---|---:|
| Traceability | 9.7 |
| Protocol fidelity | 9.6 |
| Claim calibration | 9.6 |
| Negative-transfer reporting | 9.5 |
| Split protection | 9.8 |

Average: **9.64 / 10**.

