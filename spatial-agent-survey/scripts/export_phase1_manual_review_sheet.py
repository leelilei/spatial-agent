#!/usr/bin/env python3
"""Export a manual review sheet for the Phase 1 117-paper keep pool."""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from PyPDF2 import PdfReader

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parent
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.ingest import write_csv
from spatial_agent_survey.screening import normalize_title_key

TIER_RANK = {"core": 0, "adjacent": 1, "foundational": 2}
PDF_STATUS_RANK = {"ready": 0, "metadata_only": 1, "missing": 2}

RULE_REASON_CN = {
    "seed_anchor": "这篇论文已经进入 Phase 1 的人工种子清单，当前 tier 判断来自前期手工确认，可直接作为优先复核对象。",
    "known_core_title": "标题直接对应已知的 LLM 多智能体社会模拟系统；若摘要也显示存在空间环境与社会行为，通常应归入 Core。",
    "llm_social_simulation": "摘要显示它更像 LLM/生成式 agent 的社会模拟或行为模拟工作；复核时重点确认是否真的存在可识别空间环境。",
    "survey_adjacent": "它属于 survey/review 背景文献，不是 evidence map 的系统对象；更适合放入 Adjacent 支持能力与领域背景边界。",
    "llm_spatial_reasoning": "它主要回答模型能否处理空间或结构输入，而不是直接报告社会行为效应，因此当前先归 Adjacent。",
    "space_syntax_bridge": "它提供空间构型、移动或社会互动的理论/实证桥梁，但不是 LLM system evidence，因此先归 Foundational。",
    "spatial_cognition_anchor": "它主要提供空间认知或空间语言背景，用于理论基础与桥接叙事，而不是 Core 系统证据。",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--keep-pool",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_prescreen_keep_pool_2026-04-13.csv",
        help="Phase 1 keep-pool CSV path.",
    )
    parser.add_argument(
        "--candidate-pool",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_candidate_pool_2026-04-13.csv",
        help="Phase 1 candidate-pool CSV path with abstracts and links.",
    )
    parser.add_argument(
        "--paper-list",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_paper_list.md",
        help="Markdown paper list with curated local PDF links.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_2026-04-13.csv",
        help="Output CSV path.",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_summary.md",
        help="Output Markdown summary path.",
    )
    parser.add_argument(
        "--zh-summary-map",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_zh_summary_2026-04-13.json",
        help="Optional JSON file mapping paper_id to Chinese abstract summary.",
    )
    parser.add_argument(
        "--translation-input-output",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_translation_input_2026-04-13.json",
        help="JSON file exported for downstream Chinese-summary generation.",
    )
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def normalize_abstract_text(text: str) -> str:
    normalized = html.unescape(str(text or ""))
    normalized = normalized.replace("&#13;", " ").replace("\r", "\n")
    normalized = re.sub(r"-\s*\n\s*", "", normalized)
    normalized = re.sub(r"\n+", "\n", normalized)
    normalized = re.sub(r"[ \t]+", " ", normalized)
    normalized = re.sub(r" ?\n ?", "\n", normalized)
    return normalized.strip()


def flatten_abstract_text(text: str) -> str:
    return re.sub(r"\s+", " ", normalize_abstract_text(text)).strip()


def extract_markdown_link_target(cell: str) -> str:
    match = re.search(r"\[[^\]]+\]\(([^)]+)\)", cell)
    return match.group(1).strip() if match else ""


def parse_phase1_paper_list_pdf_map(path: Path) -> dict[str, dict[str, str]]:
    pdf_map: dict[str, dict[str, str]] = {}
    if not path.exists():
        return pdf_map

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            continue
        if set(line.replace("|", "").replace("-", "").replace(" ", "")) == set():
            continue
        parts = [part.strip() for part in line.strip("|").split("|")]
        if len(parts) != 8 or parts[0] in {"ID", "用途"}:
            continue
        title = parts[4]
        local_pdf_cell = parts[7]
        status = "missing"
        local_pdf_path = ""
        if "Metadata only" in local_pdf_cell:
            status = "metadata_only"
        else:
            target = extract_markdown_link_target(local_pdf_cell)
            if target:
                status = "ready"
                local_pdf_path = str((path.parent / target).resolve())
        pdf_map[normalize_title_key(title)] = {
            "local_pdf_status": status,
            "local_pdf_path": local_pdf_path,
        }
    return pdf_map


def load_zh_summary_map(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return {
            str(item.get("paper_id") or "").strip(): str(item.get("abstract_zh_summary") or "").strip()
            for item in payload
            if str(item.get("paper_id") or "").strip()
        }
    if isinstance(payload, dict):
        return {str(key).strip(): str(value).strip() for key, value in payload.items() if str(key).strip()}
    return {}


def _extract_pdf_text(pdf_path: Path, max_pages: int = 2) -> str:
    try:
        reader = PdfReader(str(pdf_path))
    except Exception:
        return ""

    pages: list[str] = []
    for page in reader.pages[:max_pages]:
        try:
            pages.append(page.extract_text() or "")
        except Exception:
            continue
    return "\n\n".join(part for part in pages if part).strip()


def _slice_after_abstract_label(text: str) -> str:
    match = re.search(r"(?is)\babstract\b\s*[:\n ]*", text)
    if not match:
        return ""
    return text[match.end():].strip()


def _slice_until_section_boundary(text: str) -> str:
    boundary_patterns = [
        r"(?is)\n\s*keywords?\b",
        r"(?is)\n\s*index terms\b",
        r"(?is)\n\s*ccs concepts\b",
        r"(?is)\n\s*acm reference format\b",
        r"(?is)\n\s*1\s*\.?\s*introduction\b",
        r"(?is)\n\s*1\.1\b",
        r"(?is)\n\s*figure\s*1\b",
    ]
    end = len(text)
    for pattern in boundary_patterns:
        match = re.search(pattern, text)
        if match:
            end = min(end, match.start())
    return text[:end].strip()


def _fallback_preamble_abstract(text: str) -> str:
    first_page = text.split("\n\n", 1)[0] if "\n\n" in text else text
    intro_match = re.search(r"(?is)\n\s*1\s*\.?\s*introduction\b", first_page)
    figure_match = re.search(r"(?is)\n\s*figure\s*1\b", first_page)
    cutoffs = [m.start() for m in [intro_match, figure_match] if m]
    preamble = first_page[: min(cutoffs)] if cutoffs else first_page
    lines = [line.strip() for line in preamble.splitlines() if line.strip()]
    candidate_lines = [line for line in lines if len(line) >= 120]
    if not candidate_lines:
        candidate_lines = [line for line in lines if len(line) >= 80]
    return "\n".join(candidate_lines).strip()


def extract_pdf_abstract(pdf_path: str) -> str:
    if not pdf_path:
        return ""
    path = Path(pdf_path)
    if not path.exists():
        return ""

    raw_text = _extract_pdf_text(path)
    if not raw_text:
        return ""

    normalized = normalize_abstract_text(raw_text)
    after_abstract = _slice_after_abstract_label(normalized)
    abstract = _slice_until_section_boundary(after_abstract) if after_abstract else ""
    if not abstract:
        abstract = _slice_until_section_boundary(_fallback_preamble_abstract(normalized))
    return flatten_abstract_text(abstract)


def tier_role_cn(tier: str) -> str:
    if tier == "core":
        return "直接主编码对象：用于 evidence map 主表。"
    if tier == "adjacent":
        return "补充能力边界：用于说明 LLM/agent 是否能处理空间或结构输入。"
    if tier == "foundational":
        return "理论与桥接背景：用于 Space Syntax、物理空间实证与可迁移命题。"
    return ""


def review_focus_cn(tier: str) -> str:
    if tier == "core":
        return "确认它是否同时满足：LLM multi-agent + 可识别空间环境 + 社会行为。若缺少空间环境或社会行为，需要降级或排除。"
    if tier == "adjacent":
        return "确认它是否直接回答空间能力或结构输入处理边界；不要把 benchmark 或导航能力误写成社会行为证据。"
    if tier == "foundational":
        return "确认它是否提供理论、物理空间实证或经典 ABM 桥梁；正文引用时必须注明不是 LLM multi-agent 的直接证据。"
    return ""


def download_action(tier: str, local_pdf_status: str) -> str:
    if local_pdf_status == "ready":
        return "local_pdf_ready"
    if tier == "core":
        return "download_before_fulltext_screen"
    return "abstract_first_download_if_retained"


def download_note_cn(tier: str, local_pdf_status: str) -> str:
    if local_pdf_status == "ready":
        return "本地已有 PDF，可直接进入全文快速扫描。"
    if tier == "core":
        return "如果人工摘要复核后仍保留为 Core，应优先补全文 PDF。"
    return "先做 title/abstract 复核；只有保留进入下一轮时再下载全文。"


def build_manual_review_rows(
    keep_rows: list[dict[str, str]],
    candidate_rows: list[dict[str, str]],
    pdf_map: dict[str, dict[str, str]],
    zh_summary_map: dict[str, str],
) -> list[dict[str, str]]:
    candidate_by_id = {row["paper_id"]: row for row in candidate_rows}
    rows: list[dict[str, str]] = []
    for keep_row in keep_rows:
        candidate_row = candidate_by_id.get(keep_row["paper_id"], {})
        tier = str(keep_row.get("corpus_tier") or keep_row.get("assistant_corpus_tier") or "").strip().lower()
        title = str(keep_row.get("title") or candidate_row.get("title") or "").strip()
        pdf_info = pdf_map.get(
            normalize_title_key(title),
            {"local_pdf_status": "missing", "local_pdf_path": ""},
        )
        rule = str(keep_row.get("assistant_rule") or "").strip()
        abstract_from_metadata = flatten_abstract_text(candidate_row.get("abstract", ""))
        abstract_source = "candidate_pool" if abstract_from_metadata else ""
        abstract_text = abstract_from_metadata
        if not abstract_text and pdf_info["local_pdf_status"] == "ready":
            abstract_text = extract_pdf_abstract(pdf_info["local_pdf_path"])
            abstract_source = "local_pdf" if abstract_text else ""
        if not abstract_text:
            abstract_source = "missing"
        rows.append(
            {
                "paper_id": keep_row.get("paper_id", ""),
                "title": title,
                "year": str(candidate_row.get("year") or keep_row.get("year") or ""),
                "venue": str(candidate_row.get("venue") or keep_row.get("venue") or ""),
                "authors": str(candidate_row.get("authors") or ""),
                "url": str(candidate_row.get("url") or ""),
                "doi": str(candidate_row.get("doi") or ""),
                "source_families": str(candidate_row.get("source_families") or keep_row.get("source_families") or ""),
                "assistant_priority": str(keep_row.get("assistant_priority") or ""),
                "assistant_confidence": str(keep_row.get("assistant_confidence") or ""),
                "assistant_rule": rule,
                "assistant_rationale": str(keep_row.get("assistant_rationale") or ""),
                "current_tier": tier,
                "tier_role_cn": tier_role_cn(tier),
                "tier_reason_cn": RULE_REASON_CN.get(rule, "依据当前摘要与规则，它暂时被放入该层级；请人工复核是否符合该 tier 的证据角色。"),
                "review_focus_cn": review_focus_cn(tier),
                "local_pdf_status": pdf_info["local_pdf_status"],
                "local_pdf_path": pdf_info["local_pdf_path"],
                "download_action": download_action(tier, pdf_info["local_pdf_status"]),
                "download_note_cn": download_note_cn(tier, pdf_info["local_pdf_status"]),
                "abstract_source": abstract_source,
                "abstract": abstract_text,
                "abstract_zh_summary": zh_summary_map.get(keep_row.get("paper_id", ""), ""),
                "manual_final_status": "",
                "manual_corpus_tier": "",
                "manual_exclusion_reason": "",
                "manual_note": "",
            }
        )

    rows.sort(
        key=lambda row: (
            TIER_RANK.get(row["current_tier"], 9),
            PDF_STATUS_RANK.get(row["local_pdf_status"], 9),
            {"high": 0, "medium": 1, "low": 2}.get(row["assistant_priority"], 9),
            row["title"].lower(),
        )
    )

    for index, row in enumerate(rows, start=1):
        row["review_order"] = f"{index:03d}"
    return rows


def build_summary(rows: list[dict[str, str]]) -> str:
    tier_counter = Counter(row["current_tier"] for row in rows)
    pdf_counter_by_tier: dict[str, Counter[str]] = defaultdict(Counter)
    action_counter = Counter(row["download_action"] for row in rows)
    abstract_source_counter = Counter(row["abstract_source"] for row in rows)
    zh_counter = Counter("filled" if row["abstract_zh_summary"].strip() else "missing" for row in rows)
    for row in rows:
        pdf_counter_by_tier[row["current_tier"]][row["local_pdf_status"]] += 1

    lines = [
        "# Phase 1 Manual Tier Review Sheet Summary",
        "",
        "日期：2026-04-13",
        "",
        "## 总体情况",
        "",
        f"- 总保留池：`{len(rows)}` 篇",
        f"- `core`：`{tier_counter.get('core', 0)}`",
        f"- `adjacent`：`{tier_counter.get('adjacent', 0)}`",
        f"- `foundational`：`{tier_counter.get('foundational', 0)}`",
        "",
        "## 本地 PDF 覆盖情况",
        "",
    ]

    for tier in ["core", "adjacent", "foundational"]:
        counter = pdf_counter_by_tier.get(tier, Counter())
        lines.append(
            f"- `{tier}`: ready=`{counter.get('ready', 0)}`, metadata_only=`{counter.get('metadata_only', 0)}`, missing=`{counter.get('missing', 0)}`"
        )

    lines.extend(
        [
            "",
            "## 下载建议",
            "",
            f"- `local_pdf_ready`: `{action_counter.get('local_pdf_ready', 0)}` 篇，可直接全文复核",
            f"- `download_before_fulltext_screen`: `{action_counter.get('download_before_fulltext_screen', 0)}` 篇，若摘要复核后仍保留为 `Core`，建议优先下载",
            f"- `abstract_first_download_if_retained`: `{action_counter.get('abstract_first_download_if_retained', 0)}` 篇，先做摘要复核，不需要立即下载全文",
            "",
            "## 摘要字段覆盖情况",
            "",
            f"- 英文摘要来自 candidate pool：`{abstract_source_counter.get('candidate_pool', 0)}`",
            f"- 英文摘要来自 local PDF 抽取：`{abstract_source_counter.get('local_pdf', 0)}`",
            f"- 英文摘要仍缺失：`{abstract_source_counter.get('missing', 0)}`",
            f"- 中文摘要已填充：`{zh_counter.get('filled', 0)}`",
            f"- 中文摘要待填充：`{zh_counter.get('missing', 0)}`",
            "",
            "## 建议人工复核顺序",
            "",
            "1. 先看 `core + local_pdf_ready`",
            "2. 再看 `core + missing PDF`，确认值得保留后再补全文",
            "3. 然后处理 `adjacent`",
            "4. 最后收束 `foundational`，防止理论文献无限膨胀",
            "",
            "## 主文件",
            "",
            "- `phase1_manual_tier_review_sheet_2026-04-13.csv`",
            "- `phase1_manual_tier_review_sheet_translation_input_2026-04-13.json`",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    keep_rows = read_rows(args.keep_pool)
    candidate_rows = read_rows(args.candidate_pool)
    pdf_map = parse_phase1_paper_list_pdf_map(args.paper_list)
    zh_summary_map = load_zh_summary_map(args.zh_summary_map)
    manual_rows = build_manual_review_rows(keep_rows, candidate_rows, pdf_map, zh_summary_map)

    fieldnames = [
        "review_order",
        "paper_id",
        "title",
        "year",
        "venue",
        "authors",
        "url",
        "doi",
        "source_families",
        "assistant_priority",
        "assistant_confidence",
        "assistant_rule",
        "assistant_rationale",
        "current_tier",
        "tier_role_cn",
        "tier_reason_cn",
        "review_focus_cn",
        "local_pdf_status",
        "local_pdf_path",
        "download_action",
        "download_note_cn",
        "abstract_source",
        "abstract",
        "abstract_zh_summary",
        "manual_final_status",
        "manual_corpus_tier",
        "manual_exclusion_reason",
        "manual_note",
    ]
    # Use UTF-8 BOM so spreadsheet apps like Excel detect Chinese text correctly.
    write_csv(args.output, manual_rows, fieldnames, encoding="utf-8-sig")
    translation_payload = [
        {
            "paper_id": row["paper_id"],
            "title": row["title"],
            "current_tier": row["current_tier"],
            "abstract": row["abstract"],
        }
        for row in manual_rows
    ]
    args.translation_input_output.parent.mkdir(parents=True, exist_ok=True)
    args.translation_input_output.write_text(json.dumps(translation_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.write_text(build_summary(manual_rows), encoding="utf-8")
    print(f"Wrote {len(manual_rows)} rows to {args.output}")
    print(f"Wrote translation input to {args.translation_input_output}")
    print(f"Wrote summary to {args.summary_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
