# PAT-D-260728-009 result report

## Decision

**The preregistered episode-reliability gates passed, but the result is not
causal evidence for sparse keypoint value because the Global and PrPool arms
use different pooling architectures.**

Across three independently sampled CUB official-train 10-shot episodes,
Random-K1 achieved 69.30–70.05% OOF balanced accuracy and Full Oracle achieved
69.70–70.85%. Both were stable. Official CUB test images were not decoded or
encoded.

## Results

| Episode | Global | Random-K1 | Full Oracle | K1 − Global | Oracle − Global | K1 negative class rate |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 60.00% | 69.85% | 70.75% | +9.85pp | +10.75pp | 11.5% |
| 2 | 61.95% | 70.05% | 70.85% | +8.10pp | +8.90pp | 15.5% |
| 3 | 61.25% | 69.30% | 69.70% | +8.05pp | +8.45pp | 16.0% |
| **Mean** | **61.07%** | **69.73%** | **70.43%** | **+8.67pp** | **+9.37pp** | **14.33%** |

The pooled Random-K1 class-bootstrap 95% interval versus Global was +7.30 to
+10.07pp. The negative-transfer-rate range was 4.5pp, so all three frozen
reliability conditions passed.

## Critical interpretation

The result uncovered a missing control in `PAT-D-260728-004`: Global uses
global average pooling and a 2,048-dimensional classifier, whereas Random-K1
uses sixteen learned attention maps, concatenated pooled features, and a
different classifier. Therefore, `K1 − Global` combines:

1. the effect of the PrPool architecture and optimization;
2. the effect of sparse keypoint loss.

Moreover, the Global model's median best epoch in `PAT-D-260728-001` was 18,
whereas this audit froze every arm at epoch 9. The experiment validly
demonstrates repeatability of the complete arms under a common budget, but it
does not identify the keypoint contribution.

This result triggered the preregistered-after-observation
`PAT-D-260728-010` architecture-matched K0 control. No CCT or final-test gate
was unlocked from `PAT-D-260728-009`.

## Traceability

- Protocol SHA256:
  `03141dbb4bdf080769912758ccc246c58605890235cea1cdfca30c86a81827c2`
- Unique official-train images across episodes: 4,181
- Pairwise episode overlap: 34.1–35.45%
- Official-test images decoded or encoded: `0`

