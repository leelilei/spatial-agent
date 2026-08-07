# DAI 2026 submission draft

This directory contains the independent, double-blind ACM `sigconf` submission source.
It does not replace the earlier AAAI-oriented source under `paper/latex/`.
The local `references.bib` and `figures/` copies make this folder self-contained for upload.

Build from this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The page-limit audit must count the last numbered content page before references. References are
excluded from DAI's eight-page research-track limit.

Current release audit (2026-07-23):

- ACM `sigconf`, anonymous/double-blind source
- 14 PDF pages total: eight content pages, references on pages 9--10, and appendix on pages 11--14
- 57 references are actually cited and rendered; appendix follows the bibliography as required
- no undefined citations, references, or overfull boxes
- conference metadata: Hong Kong, November 29--December 2, 2026
- main claim wording is conditional on provenance-preserving communication
- strict selector-only ablation, PROV-source replay, and GA-generated cross-source replay are reported
- seed-level SAID sensitivity and descriptive agent-level SAID--HELD alignment are reported
- appendix provides prompt contracts, memory semantics, reconstruction audits, per-seed paired
  results, robustness/channel diagnostics, attack details, and a claim-to-artifact map
- anonymous artifact build instructions are in `ARTIFACT_README.md`
