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
- Sampled rows: 692
- Labels: 9
- Repeats: 1 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.920 | 0.858–0.972 | 0.606 | 0.428–0.788 | 0.546 | 0.366 |
| Ignore | 0.916 | 0.850–0.969 | 0.629 | 0.463–0.796 | 0.545 | 0.445 |
| nnPU-sampled | 0.759 | 0.619–0.878 | 0.351 | 0.224–0.488 | 0.594 | 0.297 |
| IPW-nnPU | 0.772 | 0.628–0.891 | 0.335 | 0.215–0.454 | 0.545 | 0.258 |
| FullPool-nnPU | 0.770 | 0.649–0.879 | 0.361 | 0.228–0.512 | 0.603 | 0.263 |

## Sampling diagnostics

- q min/median/max over split samples: 0.017/0.036/0.076
- IPW ESS mean: 19.08

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.013 | -0.007–+0.038 | -0.016 | -0.093–+0.068 |
| IPW-nnPU − FullPool-nnPU | +0.002 | -0.051–+0.070 | -0.026 | -0.142–+0.102 |
| nnPU-sampled − FullPool-nnPU | -0.011 | -0.053–+0.046 | -0.010 | -0.104–+0.082 |
| IPW-nnPU − Ignore | -0.144 | -0.296–-0.010 | -0.294 | -0.485–-0.068 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | +0.009 | -0.004–+0.022 | +0.026 | -0.053–+0.109 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
