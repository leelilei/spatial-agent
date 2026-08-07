# Imbalanced transductive few-shot learning audit

## Decision relevance

Unknown query-class imbalance is a real method problem, not merely a survey
topic. However, it is already an active benchmark with strong specialized
methods. A new prior estimator cannot claim novelty or SOTA without running the
public standard protocol and its strongest baselines.

## Public protocol

Veilleux et al. define a 5-way transductive protocol with 75 total unlabeled
queries per task. Test query proportions are sampled from
`Dirichlet(2 * 1_K)`, and accuracy is averaged over 10,000 tasks. For CUB they
use the standard 100/50/50 base/validation/test class split and 84x84 images.

This is not the same as PAT-K-005/PAT-K-008, which use 200-way CUB official-train
episodes and deterministic mild 3/9 or severe 1--9 class counts. Results cannot
be compared numerically across these protocols.

## Verified competitive boundary

| Work | Relevant mechanism | Public CUB 1-shot result |
|---|---|---:|
| Veilleux et al., 2022, arXiv:2204.11181 | alpha-entropy TIM under Dirichlet imbalance | 75.7% (RN18) |
| Tian et al., ICCV 2023, arXiv:2308.03047 | conditional transport and EM prototype refinement | 78.9% RN18 / 86.9% WRN-SSL |
| Lazarou et al., WACV 2024, DOI 10.1109/WACV57701.2024.00229 | adaptive sparse manifold | 79.92% (RN18) |
| Zhou et al., arXiv:2412.16739 | learned unrolled generalized EM | no directly comparable 1-shot CUB cell; 5/10/20-shot results reported |

The paper tables were visually checked from rendered PDF pages. Backbone and
pretraining differences are material; the largest number is not automatically
the fairest comparator.

## Novelty boundary for DCPR-like methods

Already established:

- relaxing uniform query priors;
- alpha-divergence/alpha-entropy objectives;
- data-adaptive transport matrices;
- EM prototype refinement under unknown class proportions;
- learned class-balance hyperparameters;
- adaptive query manifolds and feature preprocessing.

A defensible future method would need a contribution beyond generic prior
estimation, such as independently verified cross-capacity uncertainty with a
mechanism ablation. It would still need the public 5-way Dirichlet protocol,
matched public backbones, alpha-TIM, PUTM, alpha-AM, and newer UNEM/PADDLE-family
comparators.

## Download and verification record

All four files are legitimate open-access PDFs and were verified with `file` and
`pdfinfo`; relevant table pages were rendered with Poppler and inspected.

- Veilleux PDF SHA-256: `1b2bca4bd9eb00f5b8b9f2d4a56b2246b1b8df019a45a155832b03fbff37a3b0`
- Tian PDF SHA-256: `76af847ff8833839945fa6f21f821580cd1617c830909abe0a01ea2b67786a5b`
- Lazarou PDF SHA-256: `0e647c14f3b7559d5c4826086e32e99054d680af2d2a0f5a748101024f452e4b`
- Zhou PDF SHA-256: `995d416c594b96de343043edcd3aa5e75d828005569c2fca2daac1b2764b5043`

