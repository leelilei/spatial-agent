#!/usr/bin/env python3
"""Build a rough LaTeX manuscript draft from the current markdown assets.

The output is intentionally simple: it is meant for fast manuscript review,
not for final venue formatting.
"""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PAPER_DIR = REPO_ROOT / "spatial-agent-survey" / "paper"
SECTIONS_DIR = PAPER_DIR / "sections"
TABLES_DIR = PAPER_DIR / "tables"
FIGURES_DIR = PAPER_DIR / "figures"
OUT_DIR = PAPER_DIR / "latex"
OUT_MD = OUT_DIR / "draft_main.md"
OUT_TEX = OUT_DIR / "draft_main.tex"


SECTIONS = [
    "01_introduction.md",
    "02_space_syntax_primer.md",
    "03_evidence_map.md",
    "04_feasibility.md",
    "05_social_simulation.md",
    "06_evaluation_dimensions.md",
    "07_research_agenda.md",
    "08_conclusion.md",
]


TABLE_FILES = {
    1: "table_1_multi_survey_positioning_matrix.md",
    2: "table_2_review_protocol_summary.md",
    3: "table_3_core_evidence_map.md",
    4: "table_4_environment_side_vs_agent_accessible_examples.md",
    5: "table_5_space_syntax_measure_primer.md",
    6: "table_6_space_syntax_proposition_transfer.md",
    7: "table_7_evaluation_dimensions.md",
}


TABLE_NOTE_RE = re.compile(r"^(Baseline note|Caption):\s*(.+?)\s*$")


FIGURE_FILES = {
    1: (
        "gpt_image_2/figure_1_where_gap_claim_architecture_gpt_image_2_v3.png",
        "figure_1_corpus_evidence_roles_spec.md",
    ),
    2: (
        "gpt_image_2/figure_2_record_to_row_pipeline_gpt_image_2_v3.png",
        "figure_2_prisma_scr_flow_spec.md",
    ),
    3: (
        "gpt_image_2/figure_3_agent_interface_coding_system_gpt_image_2_v3.png",
        "figure_3_l0_l5_taxonomy_spec.md",
    ),
    4: (
        "gpt_image_2/figure_4_evidence_map_matrix_gpt_image_2_v3.png",
        "figure_4_representation_distribution_spec.md",
    ),
    5: (
        "gpt_image_2/figure_5_local_global_claim_boundary_gpt_image_2_v3.png",
        "figure_5_local_vs_global_configuration_spec.md",
    ),
    6: (
        "gpt_image_2/figure_6_research_agenda_evidence_ladder_gpt_image_2_v3.png",
        "figure_6_research_agenda_map_spec.md",
    ),
}


PLACEHOLDER_RE = re.compile(r"\[(Figure|Table) (\d+) about here:[^\]]+\]")


def clean_markdown_text(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def clean_section(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines():
        if line.startswith("Draft status:"):
            continue
        lines.append(line)
    return "\n".join(lines).strip() + "\n"


def table_block(number: int) -> str:
    path = TABLES_DIR / TABLE_FILES[number]
    text = path.read_text(encoding="utf-8")
    blocks: list[str] = []
    current_title = f"Table {number}"
    notes: list[str] = []
    table_lines: list[str] = []

    def flush_table() -> None:
        nonlocal table_lines
        if not table_lines:
            return
        blocks.append(markdown_table_to_latex(current_title, table_lines, notes))
        table_lines = []
        notes.clear()

    for line in text.splitlines():
        if line.startswith("Draft status:"):
            continue
        if line.startswith("# "):
            flush_table()
            current_title = line[2:].strip()
            continue
        if line.startswith("## "):
            flush_table()
            current_title = line[3:].strip()
            continue
        note_match = TABLE_NOTE_RE.match(line)
        if note_match:
            notes.append(clean_markdown_text(note_match.group(2)))
            continue
        if line.startswith("|"):
            table_lines.append(line)
            continue
        if table_lines and not line.strip():
            flush_table()
    flush_table()
    return "\n\n".join(blocks) + "\n\n"


def split_markdown_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def markdown_table_to_latex(title: str, table_lines: list[str], notes: list[str]) -> str:
    rows = [split_markdown_row(line) for line in table_lines]
    rows = [row for row in rows if not is_separator_row(row)]
    if not rows:
        return ""

    col_count = len(rows[0])
    col_width = {
        2: "0.45\\textwidth",
        3: "0.30\\textwidth",
        4: "0.22\\textwidth",
        5: "0.175\\textwidth",
        6: "0.145\\textwidth",
        7: "0.122\\textwidth",
        8: "0.103\\textwidth",
    }.get(col_count, "0.12\\textwidth")
    col_spec = "|".join([rf">{{\raggedright\arraybackslash}}p{{{col_width}}}" for _ in range(col_count)])
    header = " & ".join(latex_escape(clean_markdown_text(cell)) for cell in rows[0]) + r" \\"
    body_rows = [
        " & ".join(latex_escape(clean_markdown_text(cell)) for cell in row) + r" \\"
        for row in rows[1:]
    ]
    note_text = " ".join(notes).strip()
    note_block = rf"\vspace{{0.25em}}\par\footnotesize {latex_escape(note_text)}" if note_text else ""

    return rf"""
\begin{{table*}}[t]
\centering
\caption{{{latex_escape(clean_markdown_text(title))}}}
\scriptsize
\setlength{{\tabcolsep}}{{3pt}}
\renewcommand{{\arraystretch}}{{1.12}}
\begin{{tabular}}{{@{{}}{col_spec}@{{}}}}
\toprule
{header}
\midrule
{chr(10).join(body_rows)}
\bottomrule
\end{{tabular}}
{note_block}
\label{{tab:{title.lower().replace(" ", "-").replace(".", "").replace(":", "")}}}
\end{{table*}}
"""


def latex_escape(text: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def spec_caption(spec_text: str) -> str:
    match = re.search(r"## Caption\n\n(.+?)(?:\n\n## |\Z)", spec_text, re.S)
    if not match:
        return "Draft figure caption pending."
    caption = " ".join(line.strip() for line in match.group(1).splitlines() if line.strip())
    return caption


def figure_block(number: int) -> str:
    image_name, spec_name = FIGURE_FILES[number]
    image_path = FIGURES_DIR / image_name
    spec_path = FIGURES_DIR / spec_name
    spec_text = spec_path.read_text(encoding="utf-8")
    caption = spec_caption(spec_text)
    rel_image_from_latex = Path("..") / image_path.relative_to(PAPER_DIR)
    label = f"fig:{number}"
    return rf"""
\begin{{figure*}}[t]
\centering
\includegraphics[width=0.94\textwidth,height=0.62\textheight,keepaspectratio]{{{latex_escape(str(rel_image_from_latex))}}}
\caption{{{latex_escape(caption)}}}
\label{{{label}}}
\end{{figure*}}
"""


def replace_placeholders(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        kind = match.group(1)
        number = int(match.group(2))
        if kind == "Table" and number in TABLE_FILES:
            return table_block(number)
        if kind == "Figure" and number in FIGURE_FILES:
            return figure_block(number)
        return match.group(0)

    return PLACEHOLDER_RE.sub(repl, text)


def build_markdown() -> str:
    metadata = "\n".join(
        [
        "---",
        "title: \"Spatial Configuration and Social Behavior in LLM-Agent Systems\"",
        "subtitle: \"Compact Conference-Style Draft\"",
        "author: \"Anonymous Authors\"",
        "date: \"2026-05-01\"",
        "documentclass: article",
        "classoption:",
        "  - twocolumn",
        "geometry:",
        "  - top=1in",
        "  - bottom=1in",
        "  - left=0.75in",
        "  - right=0.75in",
        "toc: false",
        "numbersections: true",
        "header-includes:",
        "  - \\AtBeginDocument{\\fontsize{9}{10.5}\\selectfont}",
        "  - \\usepackage{graphicx}",
        "  - \\usepackage{booktabs}",
        "  - \\usepackage{array}",
        "  - \\usepackage{float}",
        "  - \\usepackage{xcolor}",
        "  - \\usepackage{caption}",
        "---",
        ]
    )

    parts = [
        metadata,
        "",
    ]

    for section_name in SECTIONS:
        section_text = (SECTIONS_DIR / section_name).read_text(encoding="utf-8")
        parts.append(replace_placeholders(clean_section(section_text)))

    return "\n\n".join(parts).strip() + "\n"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text(build_markdown(), encoding="utf-8")
    subprocess.run(
        [
            "pandoc",
            str(OUT_MD),
            "--from",
            "markdown+raw_tex+yaml_metadata_block",
            "--to",
            "latex",
            "--standalone",
            "--toc",
            "--number-sections",
            "--output",
            str(OUT_TEX),
        ],
        cwd=REPO_ROOT,
        check=True,
    )
    print(f"Wrote {OUT_MD.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUT_TEX.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
