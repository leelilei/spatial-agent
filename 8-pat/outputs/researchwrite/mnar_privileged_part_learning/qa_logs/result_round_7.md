# Result integration QA — round 7

## Decision integrity

- Budget-response protocol frozen before predictions: yes.
- Three independent selection seeds and nested K1/K2/K4 masks: yes.
- Same model/fold seeds across all nine partial-annotation arms: yes.
- Fixed nine epochs and no hyperparameter search: yes.
- Official test images decoded or encoded: 0.
- Sparse-value and selection-robustness gates applied without relaxation: yes.

## Claim control

- Supported: K1 mean OOF BA is 69.40%, +3.95pp over Global.
- Supported: K1 retains 71.8% of the stored Full-Oracle gain.
- Supported: K1 varies by only 0.65pp across three random selections.
- Supported: mean annotation returns diminish from K1 through K4.
- Prohibited: claiming class-uniform safety; 22–24% of classes decline.
- Prohibited: reviving the rejected synthetic-MNAR correction claim.
- Prohibited: reporting official CUB test performance.

## Direction decision

Proceed with sparse keypoint annotation value and image-only selection
policies at a fixed K1 budget. Preserve class-level harm as a co-primary
endpoint.

## Scores

| Dimension | Score / 10 |
|---|---:|
| Traceability | 9.9 |
| Protocol fidelity | 9.9 |
| Claim calibration | 9.8 |
| Positive-result reporting | 9.8 |
| Split protection | 10.0 |

Average: **9.88 / 10**.
