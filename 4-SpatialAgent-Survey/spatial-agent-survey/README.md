# Spatial Agent Survey

Survey execution workspace for:

`Where Agents Dwell: A Scoping Review of Spatial Representation and Its Social Effects in LLM Multi-Agent Systems`

## Purpose

This project is the runnable subproject inside the independent
`4-SpatialAgent-Survey/` workspace.

It exists to support the survey workflow with semi-automated tooling for:

- search-result ingestion
- paper deduplication
- screening sheet generation
- system-level evidence coding templates
- quality control and audit summaries
- evidence-map and appendix export

## Boundaries

- Survey plans, reviews, coding rules, and claim rules live in:
  - `../docs/plans/survey_plan_v4.md`
  - `../docs/plans/coding_manual.md`
  - `../docs/plans/claim_matrix.md`
- Survey-specific PDFs, reading notes, exemplar assets, and closure materials live in:
  - `../assets/survey_paper/`
- Shared reference indexes copied for this project live in:
  - `../assets/papers/generated/`
- Experimental code for the empirical paper remains in:
  - `../../1-SpatialAgent/spatial-agent-core/`

This subproject should not absorb empirical SpatialAgent experiment code.

## Layout

```text
spatial-agent-survey/
├── configs/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── paper/
│   ├── appendix/
│   ├── figures/
│   ├── sections/
│   └── tables/
├── results/
│   ├── figures/
│   ├── logs/
│   └── tables/
├── scripts/
├── src/spatial_agent_survey/
└── tests/
```

## Workflow

### Phase 0 Bootstrap

Use the local seed-corpus script to satisfy the readiness gate before large-scale coding:

```bash
python scripts/ingest_phase0_seed_corpus.py
```

This writes:

- `data/processed/papers_master.csv`
- `data/processed/screening_sheet.csv`
- `results/logs/prisma_summary.json`
- `results/logs/phase0_seed_corpus_summary.md`

### Standard Flow

1. Put raw search results in `data/raw/`.
2. Run `scripts/ingest_search_results.py`.
3. Run `scripts/dedupe_papers.py`.
4. Run `scripts/screen_prepare_inputs.py`.
5. Complete manual screening and coding.
6. Run `scripts/code_prepare_pilot.py` and `scripts/qc_validate_evidence.py`.
7. Run `scripts/export_evidence_assets.py`.

## Guardrails

- Do not start large-scale coding before Phase 0 gates in `survey_plan_v4.md` are met.
- `claim_matrix.md` is a formal check artifact, not an optional note.
- Short-paper outputs must be extracted from validated full-review assets.

## Quick Start

```bash
cd spatial-agent-survey
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```
