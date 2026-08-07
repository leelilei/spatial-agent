# PAT-K-260805-009 result report

## Locked official-test audit

All method and matched-baseline constants were frozen before official-test image
decoding. CUB uses one 200-way episode because the smallest test class has only
11 images. Stanford Dogs uses three disjoint 120-way episodes, selected from
`test_list.mat` with seed `47081`; each class contributes one support and nine
queries per rotation.

| Dataset | BL-NCC | DCTPR | Strongest matched solver | DCTPR gap | DCTPR gain over BL-NCC |
|---|---:|---:|---|---:|---:|
| CUB official test | 67.95% | 74.64% | TIM-ADM 76.18% | -1.53pp | +6.69pp |
| Dogs official test | 63.56% | 70.49% | MAP-RAW 71.48% | -0.99pp | +6.92pp |

Task-head latency was 34.4 ms per CUB rotation and 30.6 ms per Dogs rotation.
The shared B/L feature extraction cost was 42.2 s for CUB's 2,000 images and
24.7--25.1 s per 1,200-image Dogs episode. Peak allocated GPU memory was 0.44 GB
for ViT-B/14 and 1.34 GB for ViT-L/14 on one RTX 3080 Ti.

## Sensitivity

The scan uses only the six official-train episodes and is one-factor-at-a-time.
The frozen reference is `T=3`, `lambda=0.5`, `tau=0.05`.

- CUB pooled means for `T=1,2,3,5`: 74.59, 74.76, 74.85, 74.94%.
- Dogs pooled means for `T=1,2,3,5`: 69.13, 70.01, 70.36, 70.60%.
- CUB pooled means for `lambda=0.25,0.5,0.75,1.0`: 74.23, 74.85, 75.21, 73.95%.
- Dogs pooled means for `lambda=0.25,0.5,0.75,1.0`: 68.55, 70.36, 71.11, 70.92%.
- CUB pooled means for `tau=0.025,0.05,0.1`: 75.64, 74.85, 73.26%.
- Dogs pooled means for `tau=0.025,0.05,0.1`: 69.95, 70.36, 68.49%.

The sensitivity scan supports a short update schedule and the need for a
support anchor, but also shows that temperature is not universally insensitive.
No official-test result was used to select a new value.
