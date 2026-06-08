#!/usr/bin/env python3
"""Build a unified Markdown bundle for the stable widened-Core corpus."""

from __future__ import annotations

import csv
import re
import sys
from argparse import ArgumentParser
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = REPO_ROOT / "spatial-agent-survey"
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.pdf import extract_pdf, render_fulltext_markdown


DEFAULT_SOURCE_CSV = (
    REPO_ROOT
    / "assets"
    / "survey_paper"
    / "phase1"
    / "phase1_widened_core_evidence_map_2026-04-27.csv"
)
DEFAULT_OUTPUT_DIR = (
    REPO_ROOT / "assets" / "survey_paper" / "pdfs" / "phase1_stable_widened_core_markdown"
)


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--source-csv", type=Path, default=DEFAULT_SOURCE_CSV)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    return parser


def slugify(value: str, *, limit: int = 80) -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "_", value).strip("_")
    return slug[:limit] or "item"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def resolve_artifact(path_text: str) -> Path | None:
    if not path_text or path_text.startswith("http"):
        return None
    candidate = REPO_ROOT / Path(path_text)
    return candidate if candidate.exists() else None


def sibling_fulltext_markdown(pdf_path: Path) -> Path | None:
    candidate = pdf_path.with_suffix(".fulltext.md")
    return candidate if candidate.exists() else None


def classify_artifact(path_text: str, source_basis: str) -> str:
    if path_text.endswith(".pdf"):
        return "local_pdf"
    if path_text.endswith(".source.md"):
        return "local_markdown_source_note"
    if path_text.endswith(".md"):
        return "local_markdown_fulltext"
    if path_text.startswith("http"):
        return "remote_page_only"
    if source_basis in {"missing_pdf", "not_acquired_in_round3"}:
        return "missing_local_artifact"
    if not path_text:
        return "no_local_file_recorded"
    return "other"


def build_placeholder_body(row: dict[str, str], artifact_class: str) -> str:
    lines = [
        "## Source Content Status",
        "",
        f"- artifact_class: `{artifact_class}`",
        f"- source_basis: `{row.get('source_basis', '') or 'unknown'}`",
    ]
    artifact = row.get("local_artifact_path", "")
    if artifact:
        lines.append(f"- recorded_source: `{artifact}`")
    else:
        lines.append("- recorded_source: none")

    lines.extend(["", "## Placeholder Note", ""])
    if artifact_class == "remote_page_only":
        lines.append(
            "This row currently relies on a remote page reference rather than a locally archived PDF or full-text file."
        )
    elif artifact_class == "missing_local_artifact":
        lines.append(
            "This row is admitted in the current stable widened-Core table, but no local PDF/full-text artifact is currently archived."
        )
    elif artifact_class == "no_local_file_recorded":
        lines.append(
            "This row is represented by a local review note or memo basis, but the stable widened-Core CSV does not currently point to a local full-text artifact."
        )
    else:
        lines.append(
            "No extractable local full-text artifact was found for this row at bundle build time."
        )
    lines.append("")
    return "\n".join(lines)


def build_row_markdown(row: dict[str, str]) -> str:
    path_text = row.get("local_artifact_path", "")
    source_basis = row.get("source_basis", "")
    artifact_class = classify_artifact(path_text, source_basis)
    artifact_path = resolve_artifact(path_text)

    content_section = ""
    if artifact_path and artifact_path.suffix.lower() == ".md":
        content_section = artifact_path.read_text(encoding="utf-8")
    elif artifact_path and artifact_path.suffix.lower() == ".pdf":
        sibling = sibling_fulltext_markdown(artifact_path)
        if sibling is not None:
            content_section = sibling.read_text(encoding="utf-8")
        else:
            content_section = render_fulltext_markdown(extract_pdf(artifact_path))
    else:
        content_section = build_placeholder_body(row, artifact_class)

    lines = [
        f"# {row['shortlist_id']} - {row['system_name']}",
        "",
        "## Stable Widened-Core Snapshot",
        "",
        f"- core_layer: `{row.get('core_layer', '')}`",
        f"- admission_status: `{row.get('admission_status', '')}`",
        f"- corpus_tier: `{row.get('corpus_tier', '')}`",
        f"- system_family: `{row.get('system_family', '')}`",
        f"- paper_refs: `{row.get('paper_refs', '')}`",
        f"- year: `{row.get('year', '')}`",
        f"- agent_count: `{row.get('agent_count', '')}`",
        f"- environment_side_representation: `{row.get('environment_side_representation', '')}`",
        f"- agent_accessible_representation: `{row.get('agent_accessible_representation', '')}`",
        f"- behavioral_scale: `{row.get('behavioral_scale', '')}`",
        f"- behavior_type: `{row.get('behavior_type', '')}`",
        f"- evidence_status: `{row.get('evidence_status', '')}`",
        f"- spatial_behavior_coupling: `{row.get('spatial_behavior_coupling', '')}`",
        f"- evaluation_method: `{row.get('evaluation_method', '')}`",
        f"- space_syntax_construct: `{row.get('space_syntax_construct', '')}`",
        f"- source_basis: `{source_basis or 'unknown'}`",
        f"- artifact_class: `{artifact_class}`",
        "",
        "## Representation Gap Note",
        "",
        row.get("representation_gap_note", "") or "[no representation gap note recorded]",
        "",
        "## Original Artifact Pointer",
        "",
        f"- local_artifact_path: `{path_text or 'none'}`",
        "",
        "## Source Content",
        "",
    ]
    lines.append(content_section.rstrip())
    lines.append("")
    return "\n".join(lines)


def write_bundle(rows: list[dict[str, str]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    generated_files: list[str] = []
    for row in rows:
        filename = f"{row['shortlist_id']}_{slugify(row['system_name'])}.md"
        target = output_dir / filename
        target.write_text(build_row_markdown(row), encoding="utf-8")
        generated_files.append(filename)

    readme_lines = [
        "# Stable Widened-Core Markdown Bundle",
        "",
        f"- generated_at_utc: {datetime.now(timezone.utc).replace(microsecond=0).isoformat()}",
        f"- source_csv: `{DEFAULT_SOURCE_CSV.relative_to(REPO_ROOT)}`",
        f"- total_rows: `{len(rows)}`",
        "",
        "This folder groups the current stable widened-Core corpus into one Markdown directory.",
        "Each row receives one Markdown dossier with row-level coding metadata plus either extracted full text, a local source note, or a structured placeholder when no local text artifact is currently archived.",
        "Files ending in `.source.md` are row-level local source notes rather than full-text transcriptions.",
        "",
        "Generated files:",
        "",
    ]
    readme_lines.extend(f"- `{name}`" for name in generated_files)
    readme_lines.append("")
    (output_dir / "README.md").write_text("\n".join(readme_lines), encoding="utf-8")


def main() -> int:
    args = build_parser().parse_args()
    rows = read_rows(args.source_csv)
    write_bundle(rows, args.output_dir)
    print(f"Built Markdown bundle for {len(rows)} rows at: {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
