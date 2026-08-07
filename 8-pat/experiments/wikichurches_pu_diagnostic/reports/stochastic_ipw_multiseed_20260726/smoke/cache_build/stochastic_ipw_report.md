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
- Sampled rows: 700
- Labels: 9
- Repeats: 1 / label
- Class prior: 0.25

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | pool score |
|---|---:|---:|---:|---:|---:|---:|
| PN-sampled | 0.914 | 0.840–0.975 | 0.634 | 0.429–0.832 | 0.547 | 0.366 |
| Ignore | 0.916 | 0.850–0.969 | 0.629 | 0.463–0.796 | 0.545 | 0.445 |
| nnPU-sampled | 0.763 | 0.651–0.865 | 0.383 | 0.248–0.509 | 0.601 | 0.296 |
| IPW-nnPU | 0.763 | 0.663–0.855 | 0.327 | 0.211–0.454 | 0.523 | 0.255 |
| FullPool-nnPU | 0.770 | 0.649–0.879 | 0.361 | 0.228–0.512 | 0.603 | 0.263 |

## Sampling diagnostics

- q min/median/max over split samples: 0.015/0.034/0.088
- IPW ESS mean: 19.05

## Paired differences

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| IPW-nnPU − nnPU-sampled | +0.001 | -0.022–+0.024 | -0.056 | -0.138–+0.004 |
| IPW-nnPU − FullPool-nnPU | -0.007 | -0.054–+0.051 | -0.034 | -0.076–+0.008 |
| nnPU-sampled − FullPool-nnPU | -0.008 | -0.042–+0.033 | +0.022 | -0.046–+0.091 |
| IPW-nnPU − Ignore | -0.153 | -0.243–-0.077 | -0.302 | -0.404–-0.188 |

## FullPool approximation

Negative values mean IPW is closer to FullPool than unweighted sampled-U nnPU.

| Gap contrast | Δ absolute AUC gap | 95% CI | Δ absolute AP gap | 95% CI |
|---|---:|---:|---:|---:|
| IPW gap − unweighted gap | +0.016 | -0.001–+0.034 | -0.022 | -0.059–+0.010 |

This experiment identifies candidate-sampling correction only. It does not identify annotation propensity, missing-positive precision, or Oracle performance.
