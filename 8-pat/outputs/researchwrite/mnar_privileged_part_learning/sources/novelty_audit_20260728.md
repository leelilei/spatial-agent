# Novelty audit — 2026-07-28

## Candidate problem

All training images have target class labels, while privileged part annotations are
observed only for a non-randomly selected subset. The target is safe transfer to
fine-grained classification rather than recovery of every missing part label.

## Closest work matrix

| Work | Covers | Does not directly cover |
|---|---|---|
| Hu et al., ICLR 2022, *On Non-Random Missing Labels in Semi-Supervised Learning* | MNAR class labels; class-aware propensity and imputation; doubly robust objective | target labels are missing; no privileged part annotations |
| Duan et al., ICCV 2023, *Towards Semi-supervised Learning with Non-random Missing Labels* | MNAR class imbalance and pseudo-label rectification | no complete target labels plus selectively missing local PI |
| Xie et al., AAAI 2023, *Semi-supervised Learning with Support Isolation* | deterministic filtering and disjoint labeled/unlabeled support | standard class labels; no part PI or fine-grained downstream safety |
| Rodríguez et al., TPAMI 2023, *Fine-Grained Species Recognition with Privileged Pooling* | train-only keypoints, fine-grained recognition, few-shot, biased camera-trap data, sparse keypoint subset | does not formulate annotation availability as MCAR/MAR/MNAR; no annotation-support diagnostic or explicit negative-transfer control |
| Sabeti et al., IEEE JBHI 2021, *Learning Using Partially Available Privileged Information...* | PI available for only a subset of training samples | medical SVM; no part selection mechanism or few-shot FGVC |
| Aslam et al., CVPRW 2023, *Privileged Knowledge Distillation...* | adaptive weighting to reduce negative transfer from an incorrect privileged teacher | privileged audio modality; no non-random annotation coverage |
| Zhang et al., CVPR 2015, *Weakly Supervised Fine-Grained Image Categorization* | part discovery with class labels only | does not use or audit selectively available part supervision |

## Current novelty statement

The defensible gap is not any individual component. It is the joint problem of:

1. complete target labels;
2. selectively observed privileged part annotations;
3. explicit MCAR/MAR/MNAR and support-violation protocols;
4. downstream negative-transfer measurement;
5. risk-controlled use of part knowledge with a non-trivial-use constraint.

## Risk

Medium-high. A paper that only combines propensity weighting, an OOD gate, and
distillation will look incremental. The experimental protocol and the distinction
between information, representativeness, and transferability must be a first-class
contribution, and the method must beat direct adaptations of the closest work.

## Sources

- https://iclr.cc/virtual/2022/poster/6177
- https://openaccess.thecvf.com/content/ICCV2023/html/Duan_Towards_Semi-supervised_Learning_with_Non-random_Missing_Labels_ICCV_2023_paper.html
- https://xie-zheng.cn/assets/pdf/aaai23-xiez.pdf
- https://arxiv.org/abs/2003.09168
- https://pmc.ncbi.nlm.nih.gov/articles/PMC7872470/
- https://openaccess.thecvf.com/content/CVPR2023W/FGAHI/papers/Aslam_Privileged_Knowledge_Distillation_for_Dimensional_Emotion_Recognition_in_the_Wild_CVPRW_2023_paper.pdf
- https://arxiv.org/abs/1504.04943
