from __future__ import annotations

import importlib.util
from pathlib import Path

from spatial_agent_survey.ingest import dedupe_papers
from spatial_agent_survey.schemas import FinalStatus


def load_phase0_script():
    project_root = Path(__file__).resolve().parents[1]
    script_path = project_root / "scripts" / "ingest_phase0_seed_corpus.py"
    spec = importlib.util.spec_from_file_location("ingest_phase0_seed_corpus", script_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_phase0_seed_corpus_stays_above_readiness_threshold():
    module = load_phase0_script()
    paper_list_path = module.PROJECT_ROOT.parent / "assets" / "papers" / "generated" / "paper_list.md"
    background_path = module.PROJECT_ROOT.parent / "docs" / "background" / "spatial_agent_survey.md"

    records = module.parse_paper_list(paper_list_path) + module.parse_background_references(background_path)
    deduped, _ = dedupe_papers(records)
    classified = [module.classify_record(record) for record in deduped]

    assert len(classified) >= 80
    assert sum(record.final_status == FinalStatus.CORE for record in classified) >= 5
    assert sum(record.final_status == FinalStatus.FOUNDATIONAL for record in classified) >= 20
