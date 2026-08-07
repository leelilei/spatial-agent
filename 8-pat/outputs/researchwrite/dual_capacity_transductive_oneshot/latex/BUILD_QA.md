# DCTPR LaTeX build QA

## Final artifact

- Source: `main.tex`
- Bibliography: `references.bib`
- PDF: `main.pdf`
- Pages: 8
- Extracted PDF word count: 5,204 (including bibliography)
- Cited references: 19
- Figures: 4 (one TikZ pipeline, one real training-image plate, and two
  quantitative result figures)
- Tables: 4
- Author metadata: anonymous placeholder

## Build verification

The final PDF was built with:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
pdflatex main.tex
```

Final-log checks:

- no undefined citations;
- no undefined cross-references;
- no overfull horizontal or vertical boxes;
- no oversized floats;
- no font-substitution warnings;
- all generated figure PDFs embed editable Arial text;
- the six training photos are embedded at 599 ppi in the plate PDF, with source
  dimensions sufficient for more than 300 effective ppi at final size;
- figure source data contain 12 Pareto records, 60 paired rotation gains, and
  12 prior-stress records;
- the three archived summary JSON files needed by the figure script are stored
  inside `figures/source_data/`, so the package rebuild is self-contained;
- the image-provenance CSV contains six records with source locators, split
  evidence, processing notes, and SHA256 digests.

## Visual verification

All eight pages were re-rendered at 115 dpi after the manuscript expansion and
inspected individually. Verified:

- no clipped or overlapping text;
- the TikZ method schematic is legible at full-page width;
- the page-4 training-image plate and its six class labels are legible;
- all tables remain inside their assigned columns or page width;
- the accuracy--runtime and prior-boundary plots remain legible at final size;
- direct labels, legends, annotations, and data points do not overlap;
- no stranded section headings or empty float pages;
- the 7.5-pt bibliography is complete and readable on the final page;
- method and dataset macros preserve following whitespace.

## Integrity

```text
main.tex       49dafb56602be4e5341a1837a69278ef18b33ec742d45b400055f7a9e15404c7
references.bib 3a1677f80a52de9a6c6eeeac97e3cc35a14c24d1cb939d5d95502431e9e31545
main.pdf       3b7a788723124db04a32ed18b3235f75a2db2d17e5df29b796990a7ed1a00213
figure script  8ac48692b99ced09ce72beb5202bca1b766d0f2fc24eac910016c3b75406047f
image plate    925d4b624de461cfa11012e0f720a1f80407c959f1657027aadde59f9b97b8ad
Pareto PDF     7584d5f599c769dbdee1a61fd1aceaba09d10d97537330e721adbde0c66b4b1c
robustness PDF 3d2703a5cfd24216d160317492c4296a32c7a7b0c3c99a4131300770b040fccd
provenance CSV 08464d8c66d381df295b0cf65a0113a275a76596e24c2c31dbbb745f99b6890a
```

## Submission boundary

This is a portable conference-like layout, not a venue-specific camera-ready
template. Once a venue is chosen, author metadata, document class, page limit,
bibliography style, and mandatory declarations still need to be adapted.
