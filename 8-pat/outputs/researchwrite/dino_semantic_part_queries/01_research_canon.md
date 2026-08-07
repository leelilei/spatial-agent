# Research canon

## Literature facts

1. Privileged Pooling uses training-only keypoints to supervise visual attention and reports improved sample efficiency; it is the closest direct prior for the problem setting (Rodriguez et al., TPAMI 2023, doi:10.1109/TPAMI.2023.3316718).
2. Pose-normalized part representations can strongly improve few-shot fine-grained recognition, but require a semantic part localization stage (Tang et al., CVPR 2020, doi:10.1109/CVPR42600.2020.01436).
3. PDiscoNet and PDiscoFormer discover consistent parts without keypoints; therefore generic part discovery or semantic consistency is not a new contribution (van der Klis et al., ICCV 2023, doi:10.1109/ICCV51070.2023.00179; Aniraj et al., ECCV 2024, doi:10.1007/978-3-031-73013-9_15).
4. TransFG already uses transformer attention for discriminative patch selection; generic transformer part selection is not novel (He et al., AAAI 2022, doi:10.1609/aaai.v36i1.19967).
5. SalViT studies DINO-assisted few-shot keypoint detection; DINO plus keypoint localization is not by itself a new combination (Lu et al., arXiv:2304.03140).

## Experimental facts

1. Architecture-matched PrPool K1 improves over K0 by only +0.40pp on average; Full improves by +1.10pp. Both frozen keypoint-value gates failed in PAT-D-260728-010.
2. PASAC improved classification on one episode but failed its preregistered localization-mechanism gate; the Hungarian channel-identity route is closed.
3. Frozen DINOv2-B CLS + RBF SVC reaches 86.20%, 86.85%, and 85.90% on train-only episodes 1--3, mean 86.32%.
4. PAT-H-260729-001 already tested one-image-per-class class-specific DINO patch anchors; all sparse-anchor reranking arms remained below the strong global classifier.
5. Fusion, multi-view inference, residual adapters, local kernels, last-block LoRA, and class-safe post-hoc correction did not produce stable gains.
6. Official CUB test, CCT Cis, and CCT Trans access counts remain zero.

## Model facts

1. Episode 1 has cached frozen DINOv2 ViT-B/14 CLS features and 28x28 dense patch tokens for 2,000 official-train images.
2. The cache includes a 15-element semantic keypoint-to-patch index vector per image; invisible keypoints use -1.
3. The current feature extraction used deterministic direct resize to 392x392, so cached keypoint indices and patch tokens share one coordinate system.

## Supervisor constraints

1. Target is a defensible EI conference paper, not a top-journal claim.
2. A method must beat the 86.20% standard `SVC.predict` baseline, not only older weak models.
3. Every method must have an architecture-matched no-keypoint control.
4. New train-only episodes are generated only after the episode 1 mechanism gate passes.

## Terminology definitions

- Semantic part query: a cross-class detector over frozen patch tokens for one named CUB keypoint type.
- K0 query representation: the identical representation pipeline with zero detector scores, hence uniform spatial attention and no keypoint supervision.
- Full query representation: the detector is fitted from every visible fold-training keypoint.
- Oracle gate: a prerequisite test of whether full training keypoints create a useful upper bound; it is not a final method result.

## Forbidden claims

- First use of keypoints, DINO tokens, part queries, supervised attention, or pose normalization.
- Novel part discovery or novel few-shot keypoint detection.
- Guaranteed class safety, state of the art, or validated cross-dataset generalization.
- Any causal keypoint claim based on comparison with a different architecture or classifier.

## Unresolved claims

1. Whether a linear cross-class detector can localize held-out semantic parts in frozen DINO token space.
2. Whether semantic part pooling adds information beyond CLS and uniform mean-patch pooling.
3. Whether a positive Full oracle, if present, survives at K1 annotation budget.
4. Whether the narrow method combination remains distinct after a deeper 2024--2026 full-text search.
