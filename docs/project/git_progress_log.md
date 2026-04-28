# Git Progress Log

## Scope

This log captures project progress from `2026-04-28` to `2026-04-29`, focused on the survey pipeline, widened-Core evidence map, and local archival status.

## 2026-04-28

### `690d842` - `2026-04-28 01:17:19 +0800`
`Sync phase1 survey artifacts and abstract backfill`

- Synchronized a large Phase 1 survey artifact batch covering widened-core reclassification, representation-balance rechecks, targeted `L4` robustness search, and widened evidence-map execution memos.
- Added or refreshed local full-text support for key core papers, including `HC13` and `HC14`, plus PDF-to-text utilities under `spatial-agent-survey`.
- Backfilled missing abstracts and proxy summaries, expanding Phase 1 screening coverage and reducing metadata-only rows.
- Updated coding support assets, including `coding_schema.yaml`, `pdf.py`, `pdf2text.py`, `test_pdf.py`, and related export helpers, so later evidence-map generation could rely on local text extraction rather than scattered manual notes.

### `15230c5` - `2026-04-28 16:53:10 +0800`
`Update survey evidence map and exemplar references`

- Added six method or exemplar references to `assets/survey_paper/pdfs/review_library`, including scoping-review reporting or methodology papers and exemplar review material for drafting guidance.
- Added `docs/guides/survey_exemplar_usage_guide.md` and `docs/guides/survey_reference_gap_memo_2026-04-28.md` to lock the writing strategy toward evidence-map-first drafting rather than additional broad search.
- Updated `docs/guides/survey_research_guide.md` and the then-current widened-Core materials to reflect the exemplar-guided drafting plan.
- At this stage, the widened evidence map was expanded and stabilized for drafting use, before the later `HC01` exclusion and final local archival pass on `2026-04-29`.

## 2026-04-29

### `7e27418` - `2026-04-29 00:36:50 +0800`
`Sync widened-core survey scaffolds and markdown bundle`

- Reworked `docs/guides/todolist.md` into a current execution-oriented survey plan, shifting the main line from corpus expansion to `evidence map -> claim check -> drafting scaffold`.
- Updated `docs/plans/claim_matrix.md` to the current widened-Core baseline and tightened the claim discipline for `anchor_core`, `bridge_core`, `L4`, and boundary cases such as `TW-02`.
- Scaffolded the main survey sections:
  - `spatial-agent-survey/paper/sections/03_evidence_map.md`
  - `spatial-agent-survey/paper/sections/04_feasibility.md`
  - `spatial-agent-survey/paper/sections/05_social_simulation.md`
  - `spatial-agent-survey/paper/sections/06_evaluation_dimensions.md`
- Resolved the `HC01` inconsistency by aligning the stable widened-Core working baseline to exclude it, which settled the corpus at:
  - `34 rows / 32 papers`
  - `anchor_core = 19`
  - `bridge_core = 15`
  - `L1/L2/L3/L4/L5 = 1 / 8 / 18 / 1 / 6`
- Switched `spatial-agent-survey/scripts/export_evidence_assets.py` to use the widened-Core source table by default and regenerated:
  - `spatial-agent-survey/paper/appendix/appendix_evidence_table.csv`
  - `spatial-agent-survey/results/tables/evidence_map.csv`
  - `spatial-agent-survey/results/tables/evidence_map.md`
  - `spatial-agent-survey/results/tables/representation_gap_examples.csv`
  - `spatial-agent-survey/results/logs/l4_gap_summary.json`
- Added `spatial-agent-survey/scripts/build_stable_widened_core_markdown_bundle.py` and created `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown` as a unified local dossier directory for the stable widened-Core corpus.
- Built local Markdown coverage for all stable widened-Core rows, including row-level source notes for the previously weakly archived bridge cases such as `HC11`, `BK02`, `BK03`, `BK08`, `R3-05`, `L4R-01`, `TW-09`, `TW-11`, `TW-12`, and `TW-13`.
- After the archival pass, the stable widened-Core local artifact status became:
  - `22` local PDFs
  - `2` local full-text Markdown files
  - `10` local source-note Markdown files
  - `0` remote-only or missing artifacts in the stable widened-Core working set

## Current Status As Of `2026-04-29`

- The survey workflow is now in a drafting-ready state rather than a search-expansion state.
- The main bottleneck has shifted from corpus discovery to turning the stabilized evidence base into polished section prose, beginning with `Section 3 Evidence Map`.
- The widened-Core bundle, appendix, and exported evidence tables are now synchronized to one local baseline, which should reduce future drift between guide text, claim discipline, and paper assets.
