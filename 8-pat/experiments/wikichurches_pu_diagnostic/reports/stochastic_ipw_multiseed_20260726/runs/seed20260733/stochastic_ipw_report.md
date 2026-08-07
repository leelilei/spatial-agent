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
- Sampled rows: 662
- Labels: 9
- Repeats: 30 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.868 | 0.795–0.926 | 0.558 | 0.435–0.660 | 0.545 | 0.369 |
| Ignore | 0.874 | 0.816–0.921 | 0.551 | 0.449–0.649 | 0.540 | 0.447 |
| nnPU-sampled | 0.762 | 0.654–0.857 | 0.429 | 0.295–0.554 | 0.903 | 0.481 |
| IPW-nnPU | 0.776 | 0.677–0.861 | 0.435 | 0.316–0.551 | 0.916 | 0.505 |
| FullPool-nnPU | 0.790 | 0.697–0.867 | 0.453 | 0.338–0.560 | 0.913 | 0.462 |

## Sampling diagnostics

- q min/median/max over split samples: 0.016/0.034/0.082
- IPW ESS mean: 20.29

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.014 | -0.000–+0.028 | +0.007 | -0.024–+0.036 |
| IPW-nnPU − FullPool-nnPU | -0.014 | -0.038–+0.003 | -0.017 | -0.045–+0.005 |
| nnPU-sampled − FullPool-nnPU | -0.028 | -0.058–-0.007 | -0.024 | -0.075–+0.019 |
| IPW-nnPU − Ignore | -0.098 | -0.153–-0.051 | -0.115 | -0.166–-0.065 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | -0.005 | -0.016–+0.005 | -0.007 | -0.030–+0.011 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
