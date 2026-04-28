#!/usr/bin/env python3
"""Export evidence-map artifacts for manuscript and appendix use."""

from __future__ import annotations

import csv
import json
import sys
from argparse import ArgumentParser
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parent
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


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(
        "--core-path",
        type=Path,
        default=REPO_ROOT
        / "assets"
        / "survey_paper"
        / "phase1"
        / "phase1_widened_core_evidence_map_2026-04-27.csv",
        help="Stable widened-Core coding CSV to export from.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    core_path = args.core_path
    appendix_path = PROJECT_ROOT / "paper" / "appendix" / "appendix_evidence_table.csv"
    screening_path = PROJECT_ROOT / "data" / "processed" / "screening_sheet.csv"
    output_dir = PROJECT_ROOT / "results"

    if not core_path.exists():
        print(f"Missing Core evidence input: {core_path}", file=sys.stderr)
        return 1

    core_frame = pd.read_csv(core_path, dtype=str).fillna("")
    if "corpus_tier" in core_frame.columns:
        core_frame = core_frame[core_frame["corpus_tier"].str.casefold() == "core"].copy()
    if "shortlist_id" in core_frame.columns and (core_frame["shortlist_id"] == "HC01").any():
        print("HC01 is adjacent/boundary evidence and must not be exported as Core.", file=sys.stderr)
        return 1

    paths = export_evidence_assets(core_frame, output_dir=output_dir)
    appendix_path.parent.mkdir(parents=True, exist_ok=True)
    core_frame.to_csv(appendix_path, index=False)

    screening_rows = read_rows(screening_path)
    if screening_rows:
        prisma_path = output_dir / "logs" / "prisma_summary.json"
        prisma_path.write_text(
            json.dumps(summarize_prisma(screening_rows), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print("Exported evidence assets:")
    print(f"- core_input: {core_path}")
    print(f"- core_rows: {len(core_frame)}")
    for name, path in paths.items():
        print(f"- {name}: {path}")
    print(f"- appendix_evidence_csv: {appendix_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
