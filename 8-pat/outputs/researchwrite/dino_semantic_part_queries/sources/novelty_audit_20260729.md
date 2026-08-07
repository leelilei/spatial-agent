# Targeted novelty audit: DINO semantic part queries

## Search scope

Search blocks covered keypoint-guided fine-grained classification, training-only privileged keypoints, semantic part discovery, transformer part selection, DINO-assisted keypoint localization, and pose-normalized few-shot recognition. OpenAlex was used as a discovery layer over Crossref and arXiv metadata. The academic-search MCP, Semantic Scholar, Scopus, and Web of Science were unavailable in this environment, so this is a targeted audit rather than an exhaustive review.

## Closest work

| Work | Direct overlap | Remaining distinction |
|---|---|---|
| Rodriguez et al., *Fine-Grained Species Recognition With Privileged Pooling* (TPAMI 2023), doi:10.1109/TPAMI.2023.3316718 | Training-only keypoints supervise attention for species recognition | Current gate freezes DINO tokens and learns a cross-class token detector rather than adapting a CNN attention pooler |
| Tang et al., *Revisiting Pose-Normalization for Fine-Grained Few-Shot Recognition* (CVPR 2020), doi:10.1109/CVPR42600.2020.01436 | Semantic parts form pose-normalized few-shot representations | Current detector is fitted directly in frozen DINO token space and is evaluated against a same-pipeline uniform control |
| van der Klis et al., *PDiscoNet* (ICCV 2023), doi:10.1109/ICCV51070.2023.00179 | Consistent discriminative part discovery for FG recognition | PDiscoNet is label-only discovery; current candidate uses named training keypoints as privileged supervision |
| Aniraj et al., *PDiscoFormer* (ECCV 2024), doi:10.1007/978-3-031-73013-9_15 | Transformer-based part discovery | Generic transformer part queries are not claimable as novel |
| He et al., *TransFG* (AAAI 2022), doi:10.1609/aaai.v36i1.19967 | Transformer attention selects discriminative patches | Current part identities are semantic and cross-class rather than attention-ranked only |
| Lu et al., *From Saliency to DINO* (2023), arXiv:2304.03140 | DINO-assisted few-shot keypoint detection | DINO plus keypoint localization is established; classification-oriented training-only use is the narrower boundary |

## Internal overlap

PAT-H-260729-001 already used DINO patch tokens sampled at one keypoint-annotated image per class and propagated class-specific anchors. The new gate is permissible only because it changes the causal question: it fits one cross-class semantic detector per named part from Full fold-training keypoints, evaluates held-out localization, and compares an identical part-pooling representation with and without detector supervision. Reusing class-specific anchor reranking would be a duplicate failed arm.

## Permitted novelty statement

Before any positive result, no novelty claim is permitted. If Full and later K1 gates pass, the narrow provisional statement is:

> training-only semantic keypoints calibrate cross-class queries in a frozen foundation-model token space, producing a keypoint-free part representation whose incremental value is isolated against uniform pooling and a strong CLS classifier.

This statement still requires a deeper 2024--2026 full-text audit before manuscript use.
