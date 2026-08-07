# PAT-D-260728-005 result report

## Decision

**NO-GO: none of the four image-only K1 selectors passed the preregistered
benefit or safety branch.**

The experiment therefore stops before `PAT-D-260728-006`, CCT20+ method
validation, and every official final split. The CUB official test decode/encode
count remains zero.

## Frozen comparison

All strategies selected exactly one official-train image per class and outer
fold. Selection used frozen ordinary-image ResNet-50 features, class labels,
and folds; the selector dataset received no keypoint field. All four arms used
the same five model/fold seeds (7901–7905) and fixed nine-epoch training.

| Strategy | OOF BA | vs Global | Negative-transfer class rate | Worst class delta | Benefit gate | Safety gate |
|---|---:|---:|---:|---:|---|---|
| Random K1, 3-seed mean | 69.40% | +3.95pp | 24.17% | −40 to −50pp | reference | reference |
| Medoid | 69.30% | +3.85pp | 25.00% | −40pp | fail | fail |
| Boundary | **69.65%** | **+4.20pp** | 24.50% | −40pp | fail | fail |
| Discriminative | 69.45% | +4.00pp | 25.50% | −40pp | fail | fail |
| Balanced Annotation Value | 69.50% | +4.05pp | **22.50%** | −40pp | fail | fail |

The benefit branch required BA ≥70.15% and negative-transfer rate ≤24.17%.
The safety branch required BA ≥69.15% and negative-transfer rate ≤19.17%.
No arm satisfied either conjunction.

## Interpretation

The simple geometry-based selectors did not create a robust improvement over
Random:

- Boundary had the highest BA, but improved only 0.25pp over the Random mean
  and slightly increased the negative-transfer rate.
- Balanced Annotation Value improved BA by 0.10pp and reduced the
  negative-transfer rate by 1.67pp relative to the Random mean, far below the
  preregistered 5pp safety improvement.
- Medoid and Discriminative did not improve both primary dimensions.

This is not caused by all policies choosing the same images. In a labeled
post-hoc overlap audit, pairwise selection overlap ranged from 0% to 20.4%;
each deterministic strategy overlapped a Random mask by only 11.9%–14.2% on
average. The result instead indicates that static ImageNet feature geometry is
not a sufficiently strong proxy for downstream keypoint annotation value at
K1.

## Stage-gate consequence

The frozen plan states that no passing strategy means:

1. do not name a winner;
2. do not run the paired multi-seed confirmation;
3. do not use CCT20+ as confirmatory method evidence;
4. do not create `FINAL_EVAL_LOCK.json`;
5. do not decode or encode CUB test or CCT Cis/Trans.

The later-stage code and guards are implemented, but remain locked.

## Traceability

- Feature SHA256:
  `c653df616b210d3f33559d727943db374ed911c35c87a00f0ec6e68dfad3c997`
- Selector-manifest SHA256:
  `3d2a30c347014a8edfbdb0cbaec23704dbebe520060775dbaa6d1e13f98234e8`
- Selection-mask SHA256:
  `7b1b6900c11b5fd069e9626ce9f174b60ad0854ef79ed213349bf07a34d15d09`
- Candidate-score SHA256:
  `65fb572ee4fa8aa80719b0a7431b5fdc9aa476b19ceff467dce22607d42fe23f`
- Official-test images decoded or encoded: `0`

