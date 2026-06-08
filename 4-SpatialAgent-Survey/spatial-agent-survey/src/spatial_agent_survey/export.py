"""Export helpers for CSV, Markdown, and JSON artifacts."""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Dict, Iterable, List

import pandas as pd

from .analysis import compute_evidence_map, compute_l4_gap_summary, select_representation_gap_examples


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def export_csv(path: Path, rows: Iterable[Dict], fieldnames: List[str] | None = None) -> None:
    rows = list(rows)
    ensure_parent(path)
    if fieldnames is None:
        fieldnames = list(rows[0].keys()) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        if fieldnames:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)


def export_markdown_table(path: Path, frame: pd.DataFrame, title: str = "") -> None:
    ensure_parent(path)
    lines: List[str] = []
    if title:
        lines.extend([f"# {title}", ""])
    if frame.empty:
        lines.append("No rows available.")
    else:
        columns = list(frame.columns)
        lines.append("| " + " | ".join(columns) + " |")
        lines.append("|" + "|".join(["---"] * len(columns)) + "|")
        for _, row in frame.iterrows():
            lines.append("| " + " | ".join(str(row[col]) for col in columns) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def export_json(path: Path, payload: Dict) -> None:
    ensure_parent(path)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def export_evidence_assets(core_frame: pd.DataFrame, output_dir: Path) -> Dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    tables_dir = output_dir / "tables"
    logs_dir = output_dir / "logs"
    tables_dir.mkdir(parents=True, exist_ok=True)
    logs_dir.mkdir(parents=True, exist_ok=True)
    evidence_map = compute_evidence_map(core_frame)
    l4_summary = compute_l4_gap_summary(core_frame)
    gap_examples = select_representation_gap_examples(core_frame)

    evidence_map_csv = tables_dir / "evidence_map.csv"
    evidence_map_md = tables_dir / "evidence_map.md"
    gap_examples_csv = tables_dir / "representation_gap_examples.csv"
    l4_summary_json = logs_dir / "l4_gap_summary.json"

    evidence_map.to_csv(evidence_map_csv, index=False)
    export_markdown_table(evidence_map_md, evidence_map, title="Evidence Map")
    gap_examples.to_csv(gap_examples_csv, index=False)
    export_json(l4_summary_json, l4_summary)

    return {
        "evidence_map_csv": evidence_map_csv,
        "evidence_map_md": evidence_map_md,
        "representation_gap_examples_csv": gap_examples_csv,
        "l4_gap_summary_json": l4_summary_json,
    }
