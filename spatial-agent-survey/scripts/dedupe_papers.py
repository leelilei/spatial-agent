#!/usr/bin/env python3
"""Deduplicate normalized paper records and emit a duplicate log."""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.ingest import dedupe_papers, papers_to_rows, write_csv
from spatial_agent_survey.schemas import paper_fieldnames, paper_from_row


def read_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "papers_master_raw.csv",
        help="Normalized input CSV path.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "papers_master.csv",
        help="Deduplicated output CSV path.",
    )
    parser.add_argument(
        "--dupes-output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "paper_duplicates.csv",
        help="Output CSV path for duplicate log.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    input_path = args.input
    output_path = args.output
    dupes_path = args.dupes_output
    papers = [paper_from_row(row) for row in read_rows(input_path)]
    deduped, duplicates = dedupe_papers(papers)
    write_csv(output_path, papers_to_rows(deduped), paper_fieldnames())
    write_csv(dupes_path, duplicates, ["kept_paper_id", "duplicate_paper_id", "reason"])
    print(f"Deduped {len(papers)} -> {len(deduped)} papers")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
