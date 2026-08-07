# PAT-C-260728-001 result report

## Decision

**NO-GO for the frozen CLIP linear privileged-part residual mechanism.**

This decision does not reject the research question. It rejects proceeding to
MCAR/MAR/MNAR correction with a local mechanism whose full-annotation Oracle
does not provide the pre-registered transferable-benefit ceiling.

## Audit boundary

- Official archive size: 3,124,435,169 bytes.
- Official/archive SHA256:
  `9719778db7a7f589af94de4d7e4a025b832835502df370154f7c0a8b35466090`.
- Train pilot: 20 Quadruped synsets × 80 images = 1,600 images.
- Validation: all 170 images from the frozen 20 synsets.
- Encoder: OpenAI CLIP ViT-B/16 QuickGELU, frozen.
- Train manifest SHA256:
  `e1ba76d350cb588a861c466b3f8bc750bb87e4acb02d9a2ace2559fe2c273be8`.
- Validation was opened only after train-only five-fold selection.
- Validation masks were not model inputs.
- Test images decoded or encoded: **0**.

## Train-only OOF selection

| Arm | Balanced accuracy | Gain vs Global | Worst-class delta |
|---|---:|---:|---:|
| Global | 91.8125% | — | — |
| Selected Full-Part Oracle | 93.8125% | +2.0000 pp | −1.2500 pp |

The selected Oracle used learning rate 0.003, weight decay 0.001,
part-loss weight 0.3, residual scale 0.25 and 29 epochs. It was the only one of
nine Oracle candidates satisfying the train-OOF worst-class constraint.

## One-shot validation gate

| Seed | Global BA | Oracle BA | Oracle gain | Worst-class delta |
|---:|---:|---:|---:|---:|
| 1307 | 91.5972% | 92.1528% | +0.5556 pp | −11.1111 pp |
| 2607 | 91.0417% | 91.5972% | +0.5556 pp | −11.1111 pp |
| 5207 | 91.0417% | 92.1528% | +1.1111 pp | −11.1111 pp |
| **Mean** | **91.2269%** | **91.9676%** | **+0.7407 pp** | — |

All three gains were positive, but the mean was below the pre-registered
+2 pp Oracle threshold and class-level harm was well outside the −2 pp safety
limit. The Oracle gate therefore failed.

## Interpretation

The result supports a narrower statement: part supervision contains a small,
directionally consistent signal, but the current frozen-CLIP linear attention
and additive local-logit residual cannot transfer it strongly or safely enough.
Running NAIVE, CLIPPED_IPW or SUPPORT_AWARE now would test corrections below an
insufficient upper bound and is therefore stopped.

The next admissible experiment is a **new mechanism family**, not a retuning of
this validation result: reproduce a canonical Privileged Pooling-style
train-time supervised-attention baseline with limited backbone adaptation and
discard additive local logits. Its protocol must be frozen before any new
validation access; PAT-C-260728-001 validation cannot be reused for selection.

