# Stochastic known-inclusion-probability P/U diagnostic

## Boundary

- U is sampled with recorded independent Bernoulli probability q;
- IPW uses self-normalized 1/q on the sampled-U negative risk;
- FullPool-nnPU uses the candidate census as sampling-risk reference;
- FullPool is not label Oracle and U still has no human truth.

- Encoder: `ViT-B/16`
- Images: 50
- Official boxes: 237
- Candidate pool rows: 23371
- Unique encoded regions: 5599
- Sampled rows: 669
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.874 | 0.805–0.929 | 0.571 | 0.455–0.667 | 0.546 | 0.380 |
| Ignore | 0.875 | 0.816–0.921 | 0.551 | 0.449–0.650 | 0.539 | 0.447 |
| nnPU-sampled | 0.782 | 0.699–0.857 | 0.429 | 0.313–0.539 | 0.910 | 0.511 |
| IPW-nnPU | 0.795 | 0.712–0.866 | 0.445 | 0.327–0.555 | 0.924 | 0.543 |
| FullPool-nnPU | 0.789 | 0.696–0.867 | 0.454 | 0.340–0.561 | 0.912 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.016/0.033/0.082
- IPW ESS mean: 16.06

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.013 | +0.003–+0.024 | +0.016 | -0.004–+0.039 |
| IPW-nnPU − FullPool-nnPU | +0.006 | -0.006–+0.019 | -0.009 | -0.038–+0.019 |
| nnPU-sampled − FullPool-nnPU | -0.007 | -0.021–+0.009 | -0.025 | -0.063–+0.017 |
| IPW-nnPU − Ignore | -0.080 | -0.114–-0.046 | -0.106 | -0.164–-0.046 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.002 | -0.015–+0.014 | -0.014 | -0.033–+0.003 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
