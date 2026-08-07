# PAT-D-260728-010 result report

## Decision

**NO-GO: after architecture matching, neither sparse nor full keypoint
supervision passed its isolated-value gate. Stop the CUB sparse-keypoint
direction.**

The large gains previously reported against Global are mainly attributable to
the PrPool architecture and its optimization, not to keypoint annotations.
CUB official test and all CCT final splits remain unopened.

## Architecture-matched results

`PRPOOL_K0` is identical to Random-K1 in architecture, augmentation, optimizer,
complement regularizer, fold seeds, and fixed nine-epoch budget. Its only
difference is that no image receives keypoint loss.

| Episode | PrPool K0 | Random-K1 | Full Oracle | K1 − K0 | Oracle − K0 | K1 negative class rate vs K0 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 69.10% | 69.85% | 70.75% | +0.75pp | +1.65pp | 21.5% |
| 2 | 69.60% | 70.05% | 70.85% | +0.45pp | +1.25pp | 27.0% |
| 3 | 69.30% | 69.30% | 69.70% | +0.00pp | +0.40pp | 23.0% |
| **Mean** | **69.33%** | **69.73%** | **70.43%** | **+0.40pp** | **+1.10pp** | — |

The pooled K1−K0 class-bootstrap 95% interval was −0.28 to +1.10pp. The pooled
negative-transfer class rate was 32.0%, and the pooled worst-class delta was
−13.33pp.

## Frozen gates

The sparse-value gate required:

1. mean K1−K0 gain at least +1.0pp; and
2. at least two of three episode gains at least +0.5pp.

Observed values were +0.40pp and one of three. The gate failed.

The full-keypoint gate required:

1. mean Full−K0 gain at least +2.0pp; and
2. at least two of three episode gains at least +1.0pp.

Observed values were +1.10pp and two of three. The mean-effect condition
failed. The overall gate therefore failed.

## Consequence

1. retract the interpretation that K1 retains 71.8% of a causal keypoint
   Oracle gain; that ratio used an architecture-mismatched denominator;
2. retain `PAT-D-260728-004` only as a response curve within PrPool plus an
   unmatched Global reference;
3. do not continue CUB active selection, class-safety, CCT confirmation, or
   final evaluation under the current proposal;
4. retain the reproducible result that a PrPool-style architecture reaches
   about 69.3% BA without keypoints, but treat this as architecture evidence,
   not a new keypoint-annotation contribution.

## Traceability

- Protocol SHA256:
  `0eb290cb6d3e7735a608af6d251572b0162fac1f0cccad1e9aa9b4951af66e04`
- Formal training: 3 episodes × 5 folds × 9 epochs
- Every training log reported `annotated_seen = 0`
- Official-test images decoded or encoded: `0`

