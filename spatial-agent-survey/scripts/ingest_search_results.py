#!/usr/bin/env python3
"""Import raw JSONL search results into a normalized papers master table."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.ingest import ingest_search_results, papers_to_rows, write_csv
from spatial_agent_survey.schemas import paper_fieldnames


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=PROJECT_ROOT / "data" / "raw",
        help="Directory containing raw JSONL search results.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PROJECT_ROOT / "data" / "processed" / "papers_master_raw.csv",
        help="Output CSV path for normalized paper rows.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw_dir = args.raw_dir
    output_path = args.output
    papers = ingest_search_results(raw_dir)
    write_csv(output_path, papers_to_rows(papers), paper_fieldnames())
    print(f"Ingested {len(papers)} papers into {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
