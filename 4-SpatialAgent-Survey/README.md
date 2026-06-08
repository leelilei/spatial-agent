# SpatialAgent Survey

This is the independent workspace for the SpatialAgent survey paper:

`Where Agents Dwell: A Scoping Review of Spatial Representation and Its Social Effects in LLM Multi-Agent Systems`

It was split out from `../1-SpatialAgent/` so the empirical SpatialAgent project and the survey project can evolve independently.

## Layout

```text
.
├── docs/
│   ├── background/
│   ├── guides/
│   ├── plans/
│   └── reviews/
├── assets/
│   ├── papers/generated/
│   └── survey_paper/
└── spatial-agent-survey/
    ├── configs/
    ├── data/
    ├── paper/
    ├── results/
    ├── scripts/
    ├── src/
    └── tests/
```

## Boundaries

- `docs/` stores survey plans, reviews, guides, and background notes.
- `assets/survey_paper/` stores the survey-specific paper set, reading notes, evidence closure materials, exemplar assets, and PDF working library.
- `assets/papers/generated/` stores copied reference indexes (`paper_list.md`, `papers.bib`) needed by the survey.
- `spatial-agent-survey/` is the runnable Python subproject for ingestion, screening, coding, QC, and paper assembly.

The empirical SpatialAgent code and experiments remain in `../1-SpatialAgent/spatial-agent-core/`.

## Core Documents

- `docs/plans/survey_plan_v4.md`: active survey plan.
- `docs/plans/coding_manual.md`: coding protocol.
- `docs/plans/claim_matrix.md`: claim-strength guardrails.
- `docs/guides/survey_research_guide.md`: day-to-day execution guide.
- `spatial-agent-survey/README.md`: runnable workflow and quick start.

## Quick Start

```bash
cd spatial-agent-survey
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Do not start large-scale coding until the Phase 0 gates in `docs/plans/survey_plan_v4.md` are satisfied.
