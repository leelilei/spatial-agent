# PAT-C-260728-002 result report

## Decision

**NO-GO for all frozen-CLIP patch-head mechanisms tested so far.**

The mechanism was changed from additive local logits to a
Privileged-Pooling-inspired architecture after checking the TPAMI paper and
official implementation:

- 3x3 convolutional sigmoid attention maps;
- four supervised maps plus one complementary map;
- per-map attention-weighted average pooling and L2 normalization;
- concatenated features with a single classifier;
- multi-scale part supervision and complementary-map variance regularization.

## Train-only OOF results

| Arm | Balanced accuracy | Gain vs strong reference | Worst-class delta |
|---|---:|---:|---:|
| CLIP CLS Global | 91.8125% | — | — |
| Patch Average | 85.0000% | −6.8125 pp | — |
| Best PrPool-inspired Oracle | 93.4375% | +1.6250 pp | −6.2500 pp |

No one of the six PrPool candidates met the −2 pp worst-class safety
constraint. The selected candidate used part-loss weight 1.0,
complementary-regularizer weight 0.1, learning rate 0.003, weight decay 0.001,
and 16 epochs.

The pre-registered gate required at least +2.5 pp with worst-class delta no
lower than −2 pp. It failed. Validation and test images read or encoded: **0**.

## Interpretation

Canonical attention pooling recovers more signal than additive local logits,
but a head trained on frozen CLIP patch tokens remains below the required
ceiling and continues to redistribute errors across classes. Further frozen
feature head variants are stopped. The only admissible technical escalation is
limited backbone adaptation, using a fresh train-only development protocol; if
that also fails, PartImageNet method development should stop.

