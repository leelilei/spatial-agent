#!/usr/bin/env python3
"""Generate screening sheets, exclusion recheck samples, and PRISMA summaries."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.export import export_json
from spatial_agent_survey.ingest import write_csv
from spatial_agent_survey.schemas import paper_from_row
from spatial_agent_survey.screening import build_screening_sheet, sample_exclusion_recheck, summarize_prisma


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--papers",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "papers_master.csv",
        help="Deduplicated papers master CSV path.",
    )
    parser.add_argument(
        "--screening-output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "screening_sheet.csv",
        help="Screening sheet output path.",
    )
    parser.add_argument(
        "--recheck-output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "exclusion_recheck_sample.csv",
        help="Exclusion recheck sample output path.",
    )
    parser.add_argument(
        "--prisma-output",
        type=Path,
        default=PROJECT_ROOT / "results" / "logs" / "prisma_summary.json",
        help="PRISMA summary output path.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    papers_path = args.papers
    screening_path = args.screening_output
    recheck_path = args.recheck_output
    prisma_path = args.prisma_output

    paper_rows = read_rows(papers_path)
    papers = [paper_from_row(row) for row in paper_rows]

    existing_screening = read_rows(screening_path)
    if existing_screening:
        screening_rows = existing_screening
    else:
        screening_rows = build_screening_sheet(papers)
        write_csv(
            screening_path,
            screening_rows,
            ["paper_id", "title", "year", "venue", "source_families", "final_status", "corpus_tier", "exclusion_reason", "notes"],
        )

    recheck_rows = sample_exclusion_recheck(screening_rows)
    write_csv(
        recheck_path,
        recheck_rows,
        ["paper_id", "title", "year", "venue", "source_families", "final_status", "corpus_tier", "exclusion_reason", "notes", "recheck_required"],
    )
    export_json(prisma_path, summarize_prisma(screening_rows))
    print(f"Wrote screening inputs to {screening_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
