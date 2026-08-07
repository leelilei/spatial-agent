# PAT-D-260728-004 result report

> **Superseded interpretation (PAT-D-260728-010):** the Global reference and
> K1/Full arms use different pooling architectures. An architecture-matched
> PrPool-K0 control later reached 69.33% mean BA; K1 improved it by only
> +0.40pp (95% class-bootstrap interval −0.28 to +1.10pp) and failed the
> frozen isolated-value gate. Therefore, the 71.8% retained-gain figure below
> is a historical arm-level comparison, not a causal keypoint-annotation
> effect. The CUB sparse-keypoint direction is stopped.

## Decision

**GO: sparse keypoint annotation value and random-selection robustness are
supported under the frozen CUB 10-shot PrPool protocol.**

With one randomly selected keypoint-annotated image per class (12.5% of each
fold-training set), three independent selections achieve 69.00–69.65% OOF
balanced accuracy. Their 69.40% mean is +3.95pp above the stored Global
reference and retains 71.8% of the stored Full-Oracle gain. Both
pre-registered gates pass. The official CUB test split was not decoded or
encoded.

## Budget-response results

| Annotated images/class | Annotation rate | Seed 8101 | Seed 8102 | Seed 8103 | Mean BA | Gain vs Global | Oracle gain retained | Range |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 (Global) | 0% | — | — | — | 65.45% | 0.00pp | 0% | — |
| 1 | 12.5% | 69.55% | 69.65% | 69.00% | **69.40%** | **+3.95pp** | **71.8%** | **0.65pp** |
| 2 | 25% | 70.35% | 69.30% | 69.40% | **69.68%** | **+4.23pp** | **77.0%** | 1.05pp |
| 4 | 50% | 69.95% | 69.85% | 70.20% | **70.00%** | **+4.55pp** | **82.7%** | 0.35pp |
| 8 (Full Oracle) | 100% | — | — | — | 70.95% | +5.50pp | 100% | — |

Within each selection seed, K1 was nested in K2 and K2 in K4. All nine
partial-annotation arms used the same five model/fold seeds and fixed
nine-epoch training budget.

## Pre-registered gates

The sparse-value gate required:

1. K1 mean retained Full-Oracle gain ≥60%;
2. every K1 selection was at least +2pp above Global;
3. official test access remained zero.

Observed values were 71.8%, +3.55 to +4.20pp, and zero. The gate passed.

The random-selection robustness gate required a K1 range ≤2pp. The observed
range was 0.65pp. This gate also passed.

## Interpretation

The response curve shows strong diminishing returns. Moving from no keypoint
annotations to one image per class recovers 3.95 of the available 5.50pp.
Increasing from one to four images per class quadruples annotation cost but
adds only 0.60pp mean BA. Full annotation adds another 0.95pp over K4.

This supports a new, narrower research direction: annotation-budget
allocation and sample-selection efficiency for privileged keypoint
supervision. It does not rescue the rejected claim that synthetic MNAR
selection causes large harm.

## Safety limitation

Average efficiency is not class-uniform:

- mean negative-transfer class rates were 24.2% for K1, 22.5% for K2, and
  22.0% for K4;
- the worst observed class delta was −50pp.

Each class has only ten OOF predictions, so these class deltas are discrete
and noisy. Nevertheless, a follow-up selection method should optimize both
mean annotation value and class-level harm, not BA alone.

## Next admissible experiment

At the fixed K1 budget, compare equal-cost image-only selection policies
(random, within-class medoid/typicality, uncertainty, and coverage-aware
selection) using the same OOF protocol. The selection policy may inspect
ordinary image features and class labels, but not hidden keypoints. Primary
endpoints should be BA gain per annotated image, K1 selection variance, and
negative-transfer class rate.

## Traceability

- Protocol SHA256:
  `8a3af98a62935c1c4ddd520c6e2ff63c44312b34c9cd85c32474c6f10eaa6386`
- Selection SHA256:
  `64c308a71737a395daf4aa18ded6a2c0d5a849297f86c3ac16670af44c1df0a4`
- Manifest SHA256:
  `53cb7db2360556453d0868d7fcf59328cfd8ed5065cacf35c719c1030e14dded`
- Official-test images decoded or encoded: `0`
