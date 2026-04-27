#!/usr/bin/env python3
"""Extract reusable Markdown full text and metadata from local PDFs."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.pdf import extract_pdf, write_fulltext_outputs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "inputs",
        nargs="+",
        type=Path,
        help="PDF files or directories to process.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Optional shared output directory. Defaults to each PDF's parent directory.",
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=None,
        help="Optional page limit for extraction.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow overwriting existing fulltext artifacts.",
    )
    parser.add_argument(
        "--emit-meta",
        action="store_true",
        help="Emit JSON sidecar files in addition to Markdown output.",
    )
    return parser


def resolve_pdf_paths(inputs: list[Path]) -> list[Path]:
    pdf_paths: list[Path] = []
    for input_path in inputs:
        if input_path.is_dir():
            pdf_paths.extend(sorted(input_path.rglob("*.pdf")))
        elif input_path.suffix.lower() == ".pdf":
            pdf_paths.append(input_path)
    seen: set[Path] = set()
    unique_paths: list[Path] = []
    for path in pdf_paths:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique_paths.append(resolved)
    return unique_paths


def main() -> int:
    args = build_parser().parse_args()
    pdf_paths = resolve_pdf_paths(args.inputs)
    if not pdf_paths:
        print("No PDF files found.", file=sys.stderr)
        return 1

    failures = 0
    for pdf_path in pdf_paths:
        output_dir = args.output_dir or pdf_path.parent
        markdown_path = output_dir / f"{pdf_path.stem}.fulltext.md"
        meta_path = output_dir / f"{pdf_path.stem}.meta.json"
        if not args.overwrite and (markdown_path.exists() or (args.emit_meta and meta_path.exists())):
            print(f"[skip] {pdf_path} -> output already exists")
            continue

        result = extract_pdf(pdf_path, max_pages=args.max_pages)
        markdown_out, meta_out = write_fulltext_outputs(result, output_dir=output_dir, emit_meta=args.emit_meta)
        print(
            f"[{result.status}] {pdf_path} -> {markdown_out}"
            + (f" | {meta_out}" if meta_out is not None else "")
            + f" | chars={result.text_char_count}"
        )
        if result.status == "failed":
            failures += 1

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
