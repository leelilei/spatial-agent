# AIPR/SPIE build QA

Checked on 2026-08-06 (updated 2026-08-06 after PAT-K-260806-010 additions).

## Template

- Source page: https://www.aipr.net/pages/sub.html
- Download: https://www.aipr.net/spie-proceedings-style.zip
- Class: SPIE Proceedings `spie.cls` v3.4 (2015-08-14)
- Bibliography style: official `spiebib.bst`
- Layout: default US Letter, one column, 10pt, no headers, footers, or page
  numbers

## Manuscript

- Final length: 14 pages
- Extracted PDF words: approximately 6,742
- Abstract: 187 words (template maximum: 250)
- Keywords: 5 (template maximum: 8)
- Figures: 6, including one real official-training image plate, one
  feature-grounded prototype-refinement diagnostic, and one new per-class
  transfer and paired significance figure (PAT-K-260806-010)
- Tables: 5 — component analysis, matched comparison, robustness panels (a+b),
  configuration/reproducibility, per-class transfer and paired tests
- References: 22 (AIPR minimum: 10); added BDCSPN, PADDLE, UNEM

## Additions since v1 (2026-08-06)

1. **Per-class transfer analysis** (§ Class-level transfer and paired
   significance): post-hoc breakdown of 6 dev episodes showing 152/99 positive
   and 28/19 negative transfer classes (CUB/Dogs); McNemar rotation-level
   significance; error-overlap Jaccard 0.78 on both datasets.
2. **Per-class transfer figure** (`fig_per_class_transfer`): 4-panel sorted
   bar chart and rotation-level significance plot from
   `analyze_per_class_transfer.py` / PAT-K-260806-010.
3. **Reproducibility section** (§ Reproducibility): consolidated hyperparameter
   table covering DCTPR and all matched baselines, environment, episode
   determinism, and code/data availability statement.
4. **Related work expansion**: added BDCSPN (Liu et al., ECCV 2020) to
   position cheap prototype rectification; PADDLE (Martin et al., NeurIPS 2022)
   and UNEM (Zhou et al., CVPR 2025) to cover hyper-parameter-free and unrolled
   imbalanced-TFSL methods; extended imbalanced subsection with explicit
   protocol boundary.
5. **Discussion update**: added sentence noting Dogs gap is statistically
   unresolved (3/30 rotations significant) and per-class characterisation of
   the 1-in-7 degradation rate.

## Automated checks

- `make all`: pass
- Undefined citations or references: none
- Overfull or underfull boxes: none
- Final LaTeX warnings: none
- Fonts: embedded
- Page size: 612 x 792 pt (US Letter)

## Visual checks

Pages 1–11 previously verified. Pages 12–14 (new content) require visual
inspection before submission; no build errors were observed.

## Page-charge note

AIPR regular registration covers up to 10 pages. This version is 14 pages;
four extra-page charges apply. The author has confirmed 14 pages is acceptable.

## Submission blocker

The author block is intentionally a visible placeholder. AIPR requires full
author names, affiliations, mailing addresses, e-mail addresses, and one
identified corresponding author. These fields must be supplied before
submission.
