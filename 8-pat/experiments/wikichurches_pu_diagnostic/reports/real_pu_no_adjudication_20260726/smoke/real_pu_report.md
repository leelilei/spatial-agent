# Real P/U diagnostic without adjudication

## Protocol boundary

- P: official WikiChurches element boxes;
- U: real candidate regions outside official boxes;
- reliable N: hierarchy-incompatible official boxes;
- evaluation: held-out official P versus held-out reliable N;
- Oracle: unavailable because both annotation CSV files are empty;
- nnPU is a prior-sensitivity diagnostic; candidate selection violates the usual SCAR assumption.

- Frozen encoder: OpenAI CLIP `ViT-B/16`
- Images: 50
- Official boxes: 237
- Unlabeled candidate boxes: 708
- Labels: 9
- Repeats: 1 / label
- Primary PU prior: 0.25; sensitivity priors: 0.10, 0.25, 0.50

## Held-out known-label performance

| Method | ROC-AUC | 95% CI | AP | 95% CI | P score | U score | U > RN95 |
|---|---:|---:|---:|---:|---:|---:|---:|
| PN | 0.903 | 0.822–0.967 | 0.568 | 0.399–0.735 | 0.537 | 0.394 | 0.126 |
| Ignore | 0.916 | 0.850–0.969 | 0.629 | 0.463–0.796 | 0.545 | 0.480 | 0.311 |
| nnPU(pi=0.10) | 0.517 | 0.366–0.675 | 0.201 | 0.093–0.354 | 0.236 | 0.044 | 0.000 |
| nnPU(pi=0.25) | 0.633 | 0.476–0.773 | 0.246 | 0.144–0.357 | 0.544 | 0.271 | 0.000 |
| nnPU(pi=0.50) | 0.740 | 0.563–0.900 | 0.447 | 0.251–0.641 | 0.896 | 0.738 | 0.006 |

## Paired differences for primary nnPU prior

| Contrast | ΔROC-AUC | 95% CI | ΔAP | 95% CI |
|---|---:|---:|---:|---:|
| nnPU(pi=0.25) − PN | -0.270 | -0.427–-0.151 | -0.322 | -0.470–-0.171 |
| nnPU(pi=0.25) − Ignore | -0.283 | -0.439–-0.159 | -0.383 | -0.548–-0.204 |

## Interpretation limit

`U > RN95` is a recovery-candidate rate, not precision: U has no human truth. The held-out metrics only test known official labels. This experiment can reject an unstable P/U formulation, but it cannot estimate the real missing-positive rate or an Oracle gap.
