# PAT-D-260728-002 result report

## Decision

**NO-GO for selection-bias correction under the frozen 25%-annotation
screening regime.**

The biased MAR-X, MNAR-Z, and support-isolation arms did not underperform the
equal-budget MCAR arm by the pre-registered 2 percentage points, and none
raised the negative-transfer class rate by 0.10. The official CUB test split
was not decoded or encoded.

This is a No-Go for inventing or tuning a correction method, not evidence that
non-randomly missing part annotations are harmless in general.

## Five-fold OOF results

| Fold | Global | Full Oracle | MCAR | MAR-X | MNAR-Z | SI-HARD |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 65.75% | 70.50% | 70.25% | 68.75% | 70.00% | 68.75% |
| 1 | 67.25% | 70.75% | 69.25% | 68.25% | 69.25% | 69.00% |
| 2 | 65.50% | 72.25% | 71.75% | 73.25% | 73.50% | 73.00% |
| 3 | 66.00% | 71.50% | 72.25% | 72.75% | 72.75% | 71.50% |
| 4 | 62.75% | 69.75% | 65.75% | 67.75% | 67.50% | 67.75% |
| **OOF total** | **65.45%** | **70.95%** | **69.85%** | **70.15%** | **70.60%** | **70.00%** |

All partial-annotation arms used exactly two annotated images per class in each
fold-training set (400 of 1,600 images, 25%) and the same fixed nine-epoch
training budget. Classification loss used all fold-training images; keypoint
loss used only the selected images.

## Pre-registered gate

| Arm | Δ vs Global | Δ vs MCAR | Negative class rate vs Global | Gap vs MCAR | Worst class Δ vs Global |
|---|---:|---:|---:|---:|---:|
| MCAR | +4.40pp | 0.00pp | 23.5% | — | −40pp |
| MAR-X | +4.70pp | +0.30pp | 21.5% | −2.0pp | −30pp |
| MNAR-Z | +5.15pp | +0.75pp | 20.0% | −3.5pp | −30pp |
| SI-HARD | +4.55pp | +0.15pp | 20.5% | −3.0pp | −40pp |

The gate required at least one biased arm to be at least 2pp below MCAR or to
increase the negative-class rate by at least 10 percentage points. Neither
condition occurred. Therefore the gate failed.

## Manipulation check

The selection mechanisms changed the intended covariates:

- MCAR selected and unselected keypoint-completeness means were 0.503 and
  0.499;
- MNAR-Z selected and unselected completeness means were 0.765 and 0.412;
- SI-HARD selected and unselected completeness means were 0.716 and 0.428;
- MAR-X selected and unselected typicality means were 0.832 and 0.755.

Thus the null gate is not explained by identical selection masks. Under this
model and budget, selecting more typical or more keypoint-complete examples
was at least as useful as random keypoint supervision.

## Interpretation and next action

H1 is not supported at this severity: non-random selection did not create the
required downstream harm. Repeating the same setup with more seeds or
developing IPW/support-aware correction would not answer the claimed problem.

The next admissible diagnostic must be frozen separately and change the
missingness stressor, not the correction method. A defensible candidate is an
equal-budget one-image-per-class regime with pose/background support
isolation, including a manipulation check that the annotated and unannotated
supports are separated. Correction baselines remain blocked until such a
diagnostic first shows reproducible harm relative to MCAR.

## Traceability

- Protocol SHA256:
  `1c09e806d1e61dd11f87e2476af8cc5db77487e9d58e0a51cb6bb4140637c3a9`
- Selection NPZ SHA256:
  `13d2b48fab274d0f6f87f332e923ef1859fc350d36acba778bb760233f880123`
- Manifest SHA256:
  `53cb7db2360556453d0868d7fcf59328cfd8ed5065cacf35c719c1030e14dded`
- Summary SHA256:
  `5f6ba822ba06e8825ef950aeb09fe82bb4ca89c46dd76cf326e6d5240552a818`
- Predictions SHA256:
  `34462cf5610ac78afd5115435ef049319c88992a5ef9c6d7ed872f46e0683c01`
- Official-test images decoded or encoded: `0`

