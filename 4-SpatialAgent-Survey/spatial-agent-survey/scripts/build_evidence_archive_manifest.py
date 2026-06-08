#!/usr/bin/env python3
"""Build archive manifests for local survey PDF/fulltext assets."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SURVEY_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EVIDENCE_TABLE = SURVEY_ROOT / "paper" / "appendix" / "appendix_evidence_table.csv"
DEFAULT_PDF_ROOT = REPO_ROOT / "assets" / "survey_paper" / "pdfs"
DEFAULT_LEGACY_PDF_ROOT = REPO_ROOT / "assets" / "papers" / "pdfs"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "assets" / "survey_paper" / "evidence_closure"

STABLE_CORE_LAYERS = {"anchor_core", "bridge_core"}


@dataclass(frozen=True)
class PdfInventoryRow:
    pdf_path: str
    pdf_exists: bool
    fulltext_path: str
    fulltext_exists: bool
    meta_path: str
    meta_exists: bool
    page_count: str
    text_char_count: str
    source_group: str


@dataclass(frozen=True)
class EvidenceAuditRow:
    core_layer: str
    corpus_tier: str
    shortlist_id: str
    system_name: str
    paper_refs: str
    artifact_path: str
    artifact_kind: str
    artifact_exists: bool
    pdf_path: str
    pdf_exists: bool
    fulltext_path: str
    fulltext_exists: bool
    meta_path: str
    meta_exists: bool
    source_basis: str
    next_action: str


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def paired_paths(pdf_path: Path) -> tuple[Path, Path]:
    return pdf_path.with_suffix(".fulltext.md"), pdf_path.with_suffix(".meta.json")


def load_meta(meta_path: Path) -> dict:
    if not meta_path.exists():
        return {}
    try:
        return json.loads(meta_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}


def build_pdf_inventory(pdf_root: Path) -> list[PdfInventoryRow]:
    rows: list[PdfInventoryRow] = []
    for pdf_path in sorted(pdf_root.rglob("*.pdf")):
        fulltext_path, meta_path = paired_paths(pdf_path)
        meta = load_meta(meta_path)
        rows.append(
            PdfInventoryRow(
                pdf_path=rel(pdf_path),
                pdf_exists=pdf_path.exists(),
                fulltext_path=rel(fulltext_path),
                fulltext_exists=fulltext_path.exists(),
                meta_path=rel(meta_path),
                meta_exists=meta_path.exists(),
                page_count=str(meta.get("page_count", "")),
                text_char_count=str(meta.get("text_char_count", "")),
                source_group=pdf_path.parent.name,
            )
        )
    return rows


def evidence_rows(evidence_table: Path) -> list[dict[str, str]]:
    with evidence_table.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def infer_pdf_for_artifact(artifact_path: Path) -> tuple[Path, bool]:
    if artifact_path.suffix.lower() == ".pdf":
        return artifact_path, artifact_path.exists()
    if artifact_path.name.endswith(".fulltext.md"):
        pdf_path = artifact_path.with_name(artifact_path.name.removesuffix(".fulltext.md") + ".pdf")
        return pdf_path, pdf_path.exists()
    return artifact_path.with_suffix(".pdf"), False


def classify_next_action(
    artifact_path: Path,
    artifact_exists: bool,
    pdf_exists: bool,
    fulltext_exists: bool,
    source_basis: str,
) -> str:
    if artifact_path.suffix.lower() == ".pdf":
        if pdf_exists and fulltext_exists:
            return "ready_for_closure_card"
        if pdf_exists:
            return "convert_pdf_to_fulltext"
        return "acquire_pdf"
    if artifact_path.name.endswith(".fulltext.md") and artifact_exists:
        if pdf_exists:
            return "ready_for_closure_card"
        return "accept_fulltext_md_or_acquire_pdf"
    if "missing_pdf" in source_basis or "not_acquired" in source_basis:
        return "acquire_pdf_or_downgrade_candidate"
    if artifact_exists:
        return "source_note_only_verify_or_acquire_pdf"
    return "missing_artifact"


def build_evidence_audit(evidence_table: Path) -> list[EvidenceAuditRow]:
    audit_rows: list[EvidenceAuditRow] = []
    for row in evidence_rows(evidence_table):
        if row.get("core_layer") not in STABLE_CORE_LAYERS:
            continue
        artifact_path = REPO_ROOT / row["local_artifact_path"]
        artifact_exists = artifact_path.exists()
        pdf_path, pdf_exists = infer_pdf_for_artifact(artifact_path)
        fulltext_path, meta_path = paired_paths(pdf_path)
        if artifact_path.name.endswith(".fulltext.md") and not fulltext_path.exists():
            fulltext_path = artifact_path
        fulltext_exists = fulltext_path.exists()
        meta_exists = meta_path.exists()
        audit_rows.append(
            EvidenceAuditRow(
                core_layer=row["core_layer"],
                corpus_tier=row["corpus_tier"],
                shortlist_id=row["shortlist_id"],
                system_name=row["system_name"],
                paper_refs=row["paper_refs"],
                artifact_path=row["local_artifact_path"],
                artifact_kind=artifact_path.suffix.lower().lstrip(".") or "unknown",
                artifact_exists=artifact_exists,
                pdf_path=rel(pdf_path),
                pdf_exists=pdf_exists,
                fulltext_path=rel(fulltext_path),
                fulltext_exists=fulltext_exists,
                meta_path=rel(meta_path),
                meta_exists=meta_exists,
                source_basis=row["source_basis"],
                next_action=classify_next_action(
                    artifact_path=artifact_path,
                    artifact_exists=artifact_exists,
                    pdf_exists=pdf_exists,
                    fulltext_exists=fulltext_exists,
                    source_basis=row["source_basis"],
                ),
            )
        )
    return audit_rows


def write_csv(path: Path, rows: list[object]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].__dataclass_fields__)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: getattr(row, field) for field in fieldnames})


def bool_count(rows: list[object], field: str) -> int:
    return sum(1 for row in rows if bool(getattr(row, field)))


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        escaped = [cell.replace("|", "\\|").replace("\n", " ") for cell in row]
        lines.append("| " + " | ".join(escaped) + " |")
    return "\n".join(lines)


def write_markdown(
    path: Path,
    pdf_rows: list[PdfInventoryRow],
    evidence_rows_: list[EvidenceAuditRow],
    legacy_pdf_rows: list[PdfInventoryRow],
) -> None:
    pdf_by_group = Counter(row.source_group for row in pdf_rows)
    action_counts = Counter(row.next_action for row in evidence_rows_)
    core_rows_by_action: dict[str, list[EvidenceAuditRow]] = defaultdict(list)
    for row in evidence_rows_:
        core_rows_by_action[row.next_action].append(row)

    missing_or_nonready = [
        row
        for row in evidence_rows_
        if row.next_action != "ready_for_closure_card"
    ]
    duplicate_pdf_paths = Counter(row.pdf_path for row in evidence_rows_ if row.pdf_exists)
    duplicate_rows = [
        (path_, count)
        for path_, count in sorted(duplicate_pdf_paths.items())
        if count > 1
    ]

    lines = [
        "# Evidence PDF/Markdown Archive Manifest",
        "",
        f"- Generated: {date.today().isoformat()}",
        f"- PDF inventory root: `{rel(DEFAULT_PDF_ROOT)}`",
        f"- Local PDFs inventoried: {len(pdf_rows)}",
        f"- PDFs with fulltext markdown: {bool_count(pdf_rows, 'fulltext_exists')}/{len(pdf_rows)}",
        f"- PDFs with metadata JSON: {bool_count(pdf_rows, 'meta_exists')}/{len(pdf_rows)}",
        f"- Legacy PDF library inventoried: {len(legacy_pdf_rows)}",
        f"- Legacy PDFs with fulltext markdown: {bool_count(legacy_pdf_rows, 'fulltext_exists')}/{len(legacy_pdf_rows)}",
        f"- Legacy PDFs with metadata JSON: {bool_count(legacy_pdf_rows, 'meta_exists')}/{len(legacy_pdf_rows)}",
        f"- Stable widened-Core rows audited: {len(evidence_rows_)}",
        f"- Stable widened-Core rows with local PDF: {bool_count(evidence_rows_, 'pdf_exists')}/{len(evidence_rows_)}",
        f"- Stable widened-Core rows with fulltext markdown: {bool_count(evidence_rows_, 'fulltext_exists')}/{len(evidence_rows_)}",
        "",
        "## Local PDF Groups",
        "",
    ]
    lines.extend(f"- `{group}`: {count}" for group, count in sorted(pdf_by_group.items()))

    if legacy_pdf_rows:
        legacy_missing = [
            row for row in legacy_pdf_rows if not row.fulltext_exists or not row.meta_exists
        ]
        lines.extend(
            [
                "",
                "## Legacy PDF Library",
                "",
                f"- Root: `{rel(DEFAULT_LEGACY_PDF_ROOT)}`",
                f"- PDFs inventoried: {len(legacy_pdf_rows)}",
                f"- PDFs with fulltext markdown: {bool_count(legacy_pdf_rows, 'fulltext_exists')}/{len(legacy_pdf_rows)}",
                f"- PDFs with metadata JSON: {bool_count(legacy_pdf_rows, 'meta_exists')}/{len(legacy_pdf_rows)}",
            ]
        )
        if legacy_missing:
            lines.extend(["", "### Legacy PDFs Still Not Converted", ""])
            lines.append(
                markdown_table(
                    ["pdf_path", "fulltext_exists", "meta_exists"],
                    [
                        [row.pdf_path, str(row.fulltext_exists), str(row.meta_exists)]
                        for row in legacy_missing
                    ],
                )
            )
    lines.extend(
        [
            "",
            "## Stable Widened-Core Actions",
            "",
        ]
    )
    lines.extend(f"- `{action}`: {count}" for action, count in sorted(action_counts.items()))

    if duplicate_rows:
        lines.extend(["", "## Shared PDF Artifacts", ""])
        lines.append(
            markdown_table(
                ["pdf_path", "row_count"],
                [[path_, str(count)] for path_, count in duplicate_rows],
            )
        )

    if missing_or_nonready:
        lines.extend(["", "## Rows Not Yet PDF-Ready", ""])
        lines.append(
            markdown_table(
                [
                    "shortlist_id",
                    "paper_refs",
                    "artifact_path",
                    "pdf_exists",
                    "fulltext_exists",
                    "source_basis",
                    "next_action",
                ],
                [
                    [
                        row.shortlist_id,
                        row.paper_refs,
                        row.artifact_path,
                        str(row.pdf_exists),
                        str(row.fulltext_exists),
                        row.source_basis,
                        row.next_action,
                    ]
                    for row in missing_or_nonready
                ],
            )
        )

    lines.extend(
        [
            "",
            "## Closure-Ready Rows",
            "",
            markdown_table(
                ["shortlist_id", "paper_refs", "pdf_path", "fulltext_path"],
                [
                    [row.shortlist_id, row.paper_refs, row.pdf_path, row.fulltext_path]
                    for row in evidence_rows_
                    if row.next_action == "ready_for_closure_card"
                ],
            ),
            "",
            "## Companion CSV Files",
            "",
            "- `pdf_inventory_2026-05-01.csv`: every local PDF under `assets/survey_paper/pdfs` with paired fulltext/meta status.",
            "- `legacy_pdf_inventory_2026-05-01.csv`: every local PDF under `assets/papers/pdfs` with paired fulltext/meta status.",
            "- `evidence_row_asset_audit_2026-05-01.csv`: stable widened-Core rows aligned to artifact/PDF/fulltext status.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence-table", type=Path, default=DEFAULT_EVIDENCE_TABLE)
    parser.add_argument("--pdf-root", type=Path, default=DEFAULT_PDF_ROOT)
    parser.add_argument("--legacy-pdf-root", type=Path, default=DEFAULT_LEGACY_PDF_ROOT)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--date", default=date.today().isoformat())
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    pdf_rows = build_pdf_inventory(args.pdf_root)
    legacy_pdf_rows = build_pdf_inventory(args.legacy_pdf_root) if args.legacy_pdf_root.exists() else []
    evidence_audit_rows = build_evidence_audit(args.evidence_table)

    pdf_csv = args.output_dir / f"pdf_inventory_{args.date}.csv"
    legacy_pdf_csv = args.output_dir / f"legacy_pdf_inventory_{args.date}.csv"
    audit_csv = args.output_dir / f"evidence_row_asset_audit_{args.date}.csv"
    markdown_path = args.output_dir / f"pdf_markdown_archive_manifest_{args.date}.md"

    write_csv(pdf_csv, pdf_rows)
    write_csv(legacy_pdf_csv, legacy_pdf_rows)
    write_csv(audit_csv, evidence_audit_rows)
    write_markdown(markdown_path, pdf_rows, evidence_audit_rows, legacy_pdf_rows)

    print(f"wrote {pdf_csv}")
    print(f"wrote {legacy_pdf_csv}")
    print(f"wrote {audit_csv}")
    print(f"wrote {markdown_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
