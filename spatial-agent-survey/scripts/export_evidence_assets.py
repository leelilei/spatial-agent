#!/usr/bin/env python3
"""Export evidence-map artifacts for manuscript and appendix use."""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.export import export_evidence_assets
from spatial_agent_survey.screening import summarize_prisma


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    core_path = PROJECT_ROOT / "data" / "processed" / "core_evidence_template.csv"
    appendix_path = PROJECT_ROOT / "paper" / "appendix" / "appendix_evidence_table.csv"
    screening_path = PROJECT_ROOT / "data" / "processed" / "screening_sheet.csv"
    output_dir = PROJECT_ROOT / "results"

    core_frame = pd.read_csv(core_path) if core_path.exists() else pd.DataFrame()
    paths = export_evidence_assets(core_frame, output_dir=output_dir)
    appendix_path.parent.mkdir(parents=True, exist_ok=True)
    core_frame.to_csv(appendix_path, index=False)

    screening_rows = read_rows(screening_path)
    if screening_rows:
        prisma_path = output_dir / "logs" / "prisma_summary.json"
        prisma_path.write_text(
            pd.Series(summarize_prisma(screening_rows)).to_json(indent=2, force_ascii=False) + "\n",
            encoding="utf-8",
        )

    print("Exported evidence assets:")
    for name, path in paths.items():
        print(f"- {name}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
