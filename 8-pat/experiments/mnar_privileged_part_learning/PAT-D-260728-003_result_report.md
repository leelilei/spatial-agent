# PAT-D-260728-003 result report

## Decision

**NO-GO: the severe 12.5%-annotation stress test does not establish harmful
selective missingness for the frozen CUB PrPool stack.**

The most adverse arm, one-sided pose support isolation, was only 0.55pp below
equal-budget MCAR. This misses the pre-registered −2pp gate, and its
negative-transfer class-rate gap was only +2.5 percentage points rather than
the required +10 points. The official CUB test split was not decoded or
encoded.

Per protocol, the project must stop constructing progressively stronger
synthetic harm for this mechanism. Correction-method development remains
blocked.

## Five-fold OOF results

| Fold | Global | Full Oracle | MCAR-1 | Atypical MAR-X | Incomplete MNAR-Z | SI-Pose |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 65.75% | 70.50% | 70.50% | 69.75% | 68.50% | 69.25% |
| 1 | 67.25% | 70.75% | 69.00% | 69.50% | 69.50% | 69.00% |
| 2 | 65.50% | 72.25% | 71.00% | 71.25% | 72.00% | 70.25% |
| 3 | 66.00% | 71.50% | 70.25% | 71.00% | 71.00% | 69.75% |
| 4 | 62.75% | 69.75% | 67.50% | 66.25% | 68.25% | 67.25% |
| **OOF total** | **65.45%** | **70.95%** | **69.65%** | **69.55%** | **69.85%** | **69.10%** |

Every partial-annotation arm used exactly one annotated image per class in
each fold-training set (200 of 1,600 images, 12.5%). All arms used the same
fold seeds and fixed nine-epoch training budget.

## Pre-registered gate

| Arm | Δ vs Global | Δ vs MCAR-1 | Negative class rate vs Global | Gap vs MCAR-1 | Worst class Δ |
|---|---:|---:|---:|---:|---:|
| MCAR-1 | +4.20pp | 0.00pp | 22.0% | — | −30pp |
| Atypical MAR-X | +4.10pp | −0.10pp | 23.5% | +1.5pp | −30pp |
| Incomplete MNAR-Z | +4.40pp | +0.20pp | 22.0% | 0.0pp | −30pp |
| SI-Pose | +3.65pp | −0.55pp | 24.5% | +2.5pp | −40pp |

No biased arm passed either harm criterion.

## Manipulation check

The severe mechanisms created large, intended support differences:

- selected/unselected typicality was 0.652/0.792 for Atypical MAR-X;
- selected/unselected completeness was 0.124/0.554 for Incomplete MNAR-Z;
- selected/unselected pose score was 0.858/−0.089 for SI-Pose.

Therefore the No-Go cannot be attributed to weak or identical selection
masks. Even one keypoint-annotated image per class retained most of the full
Oracle benefit, and the identity of that image had limited influence.

## Scientific consequence

Two independently frozen diagnostics now fail to support the proposed H1:

1. at 25% annotations, biased arms were 0.15–0.75pp above MCAR;
2. at 12.5% annotations with adverse and support-isolated selection, biased
   arms ranged from −0.55 to +0.20pp relative to MCAR.

The defensible result is robustness/sample efficiency of sparse CUB keypoint
supervision, not a demonstrated MNAR correction problem. A continued paper
should pivot to annotation-value or sample-selection efficiency, or seek a
different real benchmark where selection harm exists independently. It
should not add a correction method to the current synthetic setup.

## Traceability

- Protocol SHA256:
  `a92d9ab6227b56ff15fcb42d2d5644d4c1163c7565956d83423f7be2f56f5e59`
- Selection SHA256:
  `f76e209488396cab3e4a557e37d8b59ec39ff57bf21debab607a63b6ae9c4dd2`
- Manifest SHA256:
  `53cb7db2360556453d0868d7fcf59328cfd8ed5065cacf35c719c1030e14dded`
- Official-test images decoded or encoded: `0`

