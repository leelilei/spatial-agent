#!/usr/bin/env python3
"""Prepare system-level coding templates, pilot records, and appendix stubs."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.coding import (
    build_system_templates,
    pilot_system_examples,
    system_records_to_rows,
)
from spatial_agent_survey.export import export_csv
from spatial_agent_survey.schemas import system_fieldnames


ADJUDICATION_TEMPLATE = """# Adjudication Memo

Use this file for ambiguous coding cases.

## Case Template

1. System / family:
2. Contested field:
3. Candidate coding A:
4. Candidate coding B:
5. Evidence:
6. Final ruling:
7. Triggered taxonomy update:
"""

TAXONOMY_LOG_TEMPLATE = """# Taxonomy Change Log

| old_rule | new_rule | trigger_case | reason | downstream_impact |
|---|---|---|---|---|
"""


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    screening_path = PROJECT_ROOT / "data" / "processed" / "screening_sheet.csv"
    systems_template_path = PROJECT_ROOT / "data" / "processed" / "systems_master_template.csv"
    core_template_path = PROJECT_ROOT / "data" / "processed" / "core_evidence_template.csv"
    adjacent_template_path = PROJECT_ROOT / "data" / "processed" / "adjacent_evidence_template.csv"
    pilot_path = PROJECT_ROOT / "data" / "processed" / "pilot_systems.csv"
    appendix_dir = PROJECT_ROOT / "paper" / "appendix"

    screening_rows = read_rows(screening_path)
    system_templates = build_system_templates(screening_rows)
    pilot_rows = system_records_to_rows(pilot_system_examples())

    export_csv(systems_template_path, system_templates, system_fieldnames())
    export_csv(core_template_path, system_templates, system_fieldnames())
    export_csv(adjacent_template_path, [], system_fieldnames())
    export_csv(pilot_path, pilot_rows, system_fieldnames())

    appendix_dir.mkdir(parents=True, exist_ok=True)
    (appendix_dir / "adjudication_memo_template.md").write_text(ADJUDICATION_TEMPLATE, encoding="utf-8")
    (appendix_dir / "taxonomy_change_log.md").write_text(TAXONOMY_LOG_TEMPLATE, encoding="utf-8")
    print(f"Wrote pilot coding assets to {PROJECT_ROOT / 'data' / 'processed'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
