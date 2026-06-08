from __future__ import annotations

import json
from pathlib import Path

from spatial_agent_survey.pdf import extract_abstract_from_text, extract_pdf, write_fulltext_outputs


def test_extract_pdf_reads_text_and_metadata_from_minimal_pdf(tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    _write_minimal_pdf(
        pdf_path,
        text="Abstract This is a test abstract. Keywords alpha beta. 1 Introduction Body text.",
        title="Sample PDF",
        author="Ada Lovelace",
        subject="Testing PDF extraction",
        keywords="alpha,beta",
    )

    result = extract_pdf(pdf_path)

    assert result.status == "ok"
    assert result.title == "Sample PDF"
    assert result.author == "Ada Lovelace"
    assert result.subject == "Testing PDF extraction"
    assert result.keywords == ["alpha", "beta"]
    assert "This is a test abstract" in result.text
    assert result.text_char_count == len(result.text)


def test_write_fulltext_outputs_emits_markdown_and_meta(tmp_path):
    pdf_path = tmp_path / "sample.pdf"
    output_dir = tmp_path / "out"
    _write_minimal_pdf(
        pdf_path,
        text="Abstract This is a test abstract. 1 Introduction Body text.",
        title="Rendered PDF",
        author="Grace Hopper",
        subject="Rendering PDF extraction",
        keywords="render,test",
    )

    result = extract_pdf(pdf_path)
    markdown_path, meta_path = write_fulltext_outputs(result, output_dir=output_dir, emit_meta=True)

    markdown = markdown_path.read_text(encoding="utf-8")
    meta = json.loads(meta_path.read_text(encoding="utf-8"))

    assert markdown_path.exists()
    assert meta_path is not None and meta_path.exists()
    assert "Title: Rendered PDF" in markdown
    assert "Markdown Content:" in markdown
    assert "Body text." in markdown
    assert meta["title"] == "Rendered PDF"
    assert meta["author"] == "Grace Hopper"
    assert meta["status"] == "ok"


def test_extract_abstract_from_text_prefers_abstract_section():
    text = """Title line

Abstract
This paper presents a reusable extraction workflow for local PDFs.
Keywords: PDF, extraction
1 Introduction
Background text.
"""
    abstract = extract_abstract_from_text(text)
    assert abstract == "This paper presents a reusable extraction workflow for local PDFs."


def _write_minimal_pdf(
    path: Path,
    *,
    text: str,
    title: str,
    author: str,
    subject: str,
    keywords: str,
) -> None:
    text = text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")
    objects = [
        b"<< /Type /Catalog /Pages 2 0 R >>",
        b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
        b"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>",
        b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
        (
            f"<< /Length {len(f'BT /F1 12 Tf 72 720 Td ({text}) Tj ET'.encode('latin-1'))} >>\n"
            f"stream\nBT /F1 12 Tf 72 720 Td ({text}) Tj ET\nendstream"
        ).encode("latin-1"),
        (
            f"<< /Title ({title}) /Author ({author}) /Subject ({subject}) /Keywords ({keywords}) >>"
        ).encode("latin-1"),
    ]

    buffer = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for index, obj in enumerate(objects, start=1):
        offsets.append(len(buffer))
        buffer.extend(f"{index} 0 obj\n".encode("ascii"))
        buffer.extend(obj)
        buffer.extend(b"\nendobj\n")

    xref_offset = len(buffer)
    buffer.extend(f"xref\n0 {len(objects) + 1}\n".encode("ascii"))
    buffer.extend(b"0000000000 65535 f \n")
    for offset in offsets[1:]:
        buffer.extend(f"{offset:010d} 00000 n \n".encode("ascii"))
    buffer.extend(
        (
            f"trailer\n<< /Size {len(objects) + 1} /Root 1 0 R /Info 6 0 R >>\n"
            f"startxref\n{xref_offset}\n%%EOF\n"
        ).encode("ascii")
    )
    path.write_bytes(bytes(buffer))
