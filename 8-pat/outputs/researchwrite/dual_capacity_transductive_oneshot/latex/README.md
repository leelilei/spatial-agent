# DCTPR LaTeX manuscript

This directory contains the expanded English manuscript in a portable,
two-column conference-like layout.

## Build

```bash
make
```

The build uses `pdflatex` and `bibtex`; `latexmk` and `IEEEtran.cls` are not
required. It first regenerates the training-example plate and both quantitative
figures, then writes `main.pdf`.

## Figure artifacts

The sibling `figures/` directory contains:

- the figure evidence contract;
- the Python generation script;
- the three archived summary JSON files required to rebuild the quantitative
  panels;
- source-data CSV files;
- six displayed training images with row/file provenance and SHA256 digests;
- editable PDF/SVG exports;
- 600-dpi TIFF and 300-dpi PNG exports.

The quantitative plots contain only archived experimental values. The image
plate contains real CUB and Stanford Dogs official-training images; no
generated-image model is used anywhere in the manuscript.

## Submission template migration

The current class is a generic two-column `article` because no target venue was
specified and the local TeX installation does not include `IEEEtran.cls`.
When a venue is selected, replace the document class and venue metadata first,
then recheck table widths, title spacing, page limits, and bibliography style.

`Anonymous Authors` is an intentional placeholder. No author identity or
affiliation has been inferred.
