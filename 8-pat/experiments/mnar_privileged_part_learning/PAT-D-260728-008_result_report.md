# PAT-D-260728-008 result report

## Decision

**NO-GO: classification-protective projection detected frequent gradient
conflicts but did not pass the paired benefit or safety gate.**

The mechanism is stopped. CUB official test and CCT Cis/Trans remain unopened,
and no final-evaluation lock is generated.

## Frozen paired results

The three `PAT-D-260728-004` Random-K1 masks and model/fold seeds were reused.
The only change was the preregistered projection of an auxiliary keypoint
gradient when its global dot product with the classification gradient was
negative.

| Selection seed | Naive BA | Projected BA | Paired BA change | Naive negative rate | Projected negative rate | Rate change |
|---:|---:|---:|---:|---:|---:|---:|
| 8101 | 69.55% | 69.60% | +0.05pp | 24.0% | 23.0% | −1.0pp |
| 8102 | 69.65% | 69.30% | −0.35pp | 23.5% | 23.5% | 0.0pp |
| 8103 | 69.00% | 69.10% | +0.10pp | 25.0% | 25.5% | +0.5pp |
| **Mean** | **69.40%** | **69.33%** | **−0.07pp** | **24.17%** | **24.00%** | **−0.17pp** |

The benefit branch required a mean paired BA gain of at least 0.50pp, at
least two positive seeds, and no mean safety regression. Although two seeds
had a positive sign, the mean change was −0.07pp.

The safety branch required BA non-inferiority within 0.25pp, a mean
negative-transfer-rate reduction of at least 5pp, and at least two
safety-positive seeds. The observed reduction was only 0.17pp and only one
seed improved.

The aggregate class-bootstrap 95% interval for the paired BA change was
−0.37pp to +0.23pp and was not used to alter the frozen gate.

## Gradient diagnostics

Across the 15 formal fold runs, the batch-level conflict fraction ranged from
70.0% to 83.8%, with a mean of 76.9%. The mechanism was therefore active and
the No-Go is not explained by an absence of detected conflicts.

The result indicates that a negative global batch-gradient dot product is not
a sufficient proxy for class-level negative transfer. Projection can protect
the instantaneous aggregate classification direction while still changing
optimization trajectories and individual class recalls in inconsistent ways.

## Execution anomaly

The first complete formal computation reached summary serialization but failed
before writing predictions because NumPy boolean gate values were passed to
the standard JSON encoder. No result was used from that process. The code was
changed only to cast the three gate booleans to native Python `bool`, after
which the entire frozen experiment was rerun from the beginning.

The repeated training log matched the first run's deterministic epoch
diagnostics. Both logs are archived. This anomaly did not touch any test split
and did not change the protocol, masks, seeds, model, or gate.

## Consequence

1. do not continue this batch-global gradient-projection mechanism;
2. do not treat high conflict frequency as evidence of causal class harm;
3. do not unlock CCT20+ confirmatory method validation or final test;
4. retain `PAT-D-260728-004` only as evidence that random sparse keypoint
   supervision is valuable, not that the tested active/safety methods work.

## Traceability

- Official-test images decoded or encoded: `0`
- Formal mean gradient-conflict fraction: `0.7688888889`
- Formal output:
  `raw/experiments/2026.07.28_CUB_GradientSafety_PAT-D-260728-008/results/formal/`

