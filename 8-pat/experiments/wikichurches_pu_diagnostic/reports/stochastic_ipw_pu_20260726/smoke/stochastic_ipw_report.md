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
- Sampled rows: 690
- Labels: 9
- Repeats: 1 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.923 | 0.868–0.970 | 0.624 | 0.448–0.801 | 0.547 | 0.376 |
| Ignore | 0.916 | 0.850–0.969 | 0.629 | 0.463–0.796 | 0.545 | 0.445 |
| nnPU-sampled | 0.805 | 0.676–0.916 | 0.422 | 0.262–0.584 | 0.581 | 0.294 |
| IPW-nnPU | 0.810 | 0.696–0.907 | 0.410 | 0.247–0.570 | 0.553 | 0.281 |
| FullPool-nnPU | 0.770 | 0.649–0.879 | 0.361 | 0.228–0.512 | 0.603 | 0.263 |

## Sampling diagnostics

- q min/median/max over split samples: 0.015/0.035/0.081
- IPW ESS mean: 16.94

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.005 | -0.016–+0.026 | -0.012 | -0.105–+0.104 |
| IPW-nnPU − FullPool-nnPU | +0.040 | +0.002–+0.093 | +0.049 | -0.114–+0.217 |
| nnPU-sampled − FullPool-nnPU | +0.035 | -0.007–+0.095 | +0.060 | -0.067–+0.195 |
| IPW-nnPU − Ignore | -0.106 | -0.228–+0.007 | -0.219 | -0.427–+0.007 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | +0.003 | -0.013–+0.021 | +0.063 | -0.020–+0.164 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
