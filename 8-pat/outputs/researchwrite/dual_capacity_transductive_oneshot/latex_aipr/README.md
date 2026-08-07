# DCTPR AIPR/SPIE manuscript

This directory is the AIPR-specific manuscript prepared with the official
LaTeX template linked from:

https://www.aipr.net/pages/sub.html

The downloaded template is `spie-proceedings-style.zip`. Its official
`spie.cls` and `spiebib.bst` files are bundled here so the source is
self-contained.

## Build

```bash
make all
```

The build uses `pdflatex` and `bibtex`. The four external PDF figures are
already bundled under `figures/`.

## Verified AIPR requirements

- Full papers must contain at least 8 full pages.
- One regular registration covers up to 10 pages, including figures, tables,
  and references; extra pages are charged.
- The paper must be in English.
- References must number at least 10; recent references are preferred.
- Figures and tables must appear in their proper positions and be named
  clearly.
- The corresponding author must be identified.
- All author names, affiliations, mailing addresses, and e-mail addresses must
  be supplied.

The SPIE template further specifies a one-column US-letter layout by default,
no headers, footers, or page numbers, an abstract of at most 250 words, up to
eight keywords, and numbered references in citation order.

The generic draft's reproducibility statement was removed from the submission
body. The current mechanism-grounded version is 11 pages, one page above the
regular-registration allowance; AIPR therefore charges one extra page unless
content is moved to supplementary material. Its supporting evidence remains
in the project archive: immutable protocols, feature metadata, per-rotation
predictions, summary JSON files, source hashes, recomputation reports, figure
source data, split-verified training-image provenance, and the locked
official-test/sensitivity package under
`../supplementary_results/PAT-K-260805-009/`.

## Required author action

`main.tex` deliberately contains an anonymous author placeholder because no
author identity or affiliation was provided. Replace the `\author`, `\affil`,
and `\authorinfo` fields before submission.

## Provenance

- AIPR submission page checked: 2026-07-30
- Template URL:
  https://www.aipr.net/spie-proceedings-style.zip
- Template class: SPIE Proceedings class v3.4, dated 2015-08-14
- Original generic manuscript remains unchanged in the sibling `latex/`
  directory.
