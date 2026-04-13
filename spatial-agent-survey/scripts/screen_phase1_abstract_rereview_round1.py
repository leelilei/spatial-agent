#!/usr/bin/env python3
"""Generate a stricter abstract-based rereview for the Phase 1 117-paper keep pool."""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = PROJECT_ROOT.parent
SRC_ROOT = PROJECT_ROOT / "src"
import sys

if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.ingest import write_csv


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_manual_tier_review_sheet_2026-04-13.csv",
        help="Current manual tier review sheet.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_abstract_rereview_round1_2026-04-13.csv",
        help="Round-1 abstract rereview CSV.",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=REPO_ROOT / "assets" / "survey_paper" / "phase1" / "phase1_abstract_rereview_round1_summary.md",
        help="Round-1 abstract rereview summary.",
    )
    return parser.parse_args()


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


CORE_KEEP = {
    "Affordable Generative Agents": ("high", "摘要明确描述了 agent-environment 与 inter-agent interaction，并报告开放环境中的可信交互行为。"),
    "AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents Advances Understanding of Human Behaviors and Society": (
        "medium",
        "摘要明确是大规模 LLM 社会模拟，但空间环境如何表示仍不够具体；先保留为 core-candidate。",
    ),
    "Artificial Leviathan: Exploring Social Evolution of LLM Agents Through the Lens of Hobbesian Social Contract Theory": (
        "medium",
        "摘要明确是沙盒生存环境中的多智能体社会演化，具备环境与社会行为两个条件。",
    ),
    "Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia": (
        "high",
        "摘要明确强调 actions grounded in physical/social/digital space，可作为空间化 GABM 平台保留。",
    ),
    "Generative Agents: Interactive Simulacra of Human Behavior": (
        "high",
        "摘要直接报告 The Sims 风格沙盒城镇中的日常与社会行为，是核心 anchor 系统。",
    ),
    "Project Sid: Many-agent simulations toward AI civilization": (
        "medium",
        "摘要虽抽取不完整，但明确提到 Minecraft environment 与 many-agent civilizational simulation，先保留 core。",
    ),
    "TravelAgent: Generative agents in the built environment": (
        "high",
        "摘要明确位于 built environment，并报告导航、活动和人类式决策，保留为核心空间系统。",
    ),
}

CORE_DOWNGRADE_TO_ADJACENT = {
    "Exploring Large Language Model-Driven Agents for Environment-Aware Spatial Interactions and Conversations in Virtual Reality Role-Play Scenarios": (
        "high",
        "摘要更像单 agent + user 的 environment-aware VR interaction，不是多智能体社会模拟，先降到 adjacent。",
    ),
}

CORE_EXCLUDE_NO_SPACE = {
    "Can A Society of Generative Agents Simulate Human Behavior and Inform Public Health Policy? A Case Study on Vaccine Hesitancy": (
        "high",
        "摘要聚焦社交网络与健康决策，没有明确可识别空间环境，按 E1 先排除。",
    ),
    "Can Generative Agent-Based Modeling Replicate the Friendship Paradox in Social Media Simulations?": (
        "high",
        "摘要讨论社交网络结构与 friendship paradox，并非空间环境中的社会行为，按 E1 排除。",
    ),
    "CharacterEval: A Chinese Benchmark for Role-Playing Conversational Agent Evaluation": (
        "high",
        "这是角色扮演对话 benchmark，不含空间环境，按 E1 排除。",
    ),
    "Generative Agent Simulations of 1,000 People": (
        "high",
        "摘要是 interview-conditioned human behavior replication，没有明确空间环境，按 E1 排除。",
    ),
    "Harnessing Large Language Models to Simulate Realistic Human Responses to Social Engineering Attacks: A Case Study": (
        "high",
        "摘要聚焦 phishing/social engineering response simulation，不含空间环境，按 E1 排除。",
    ),
    "Psychologically-Valid Generative Agents: A Novel Approach to Agent-Based Modeling in Social Sciences": (
        "high",
        "摘要是通用 cognitive/stance framework，没有明确空间环境，按 E1 排除。",
    ),
    "Simulating Public Administration Crisis: A Novel Generative Agent-Based Simulation System to Lower Technology Barriers in Social Science Research": (
        "high",
        "摘要描述虚拟政府与公共事件仿真，但未给出明确空间环境，按 E1 排除。",
    ),
    "User Behavior Simulation with Large Language Model based Agents": (
        "high",
        "摘要聚焦 recommendation/social network 用户仿真，没有明确空间环境，按 E1 排除。",
    ),
    "User Behavior Simulation with Large Language Model-based Agents": (
        "high",
        "摘要聚焦 recommendation/social network 用户仿真，没有明确空间环境，按 E1 排除。",
    ),
}

CORE_HOLD_AMBIGUOUS_SPACE = {
    "OASIS: Open Agent Social Interaction Simulations with One Million Agents": (
        "medium",
        "摘要强调社交媒体平台环境，但是否可算作本文需要的空间环境仍需全文裁定；先 hold。",
    ),
    "Unveiling the Truth and Facilitating Change: Towards Agent-based Large-scale Social Movement Simulation": (
        "medium",
        "摘要是 Twitter-like 社交媒体仿真，空间维度不明确；先 hold，等待全文确认。",
    ),
    "Multimodal Safety Evaluation in Generative Agent Social Simulations": (
        "medium",
        "摘要提到 rich multimodal settings，但未说明空间结构输入如何进入 agent，先 hold。",
    ),
}

CORE_HOLD_MISSING_ABSTRACT = {
    "Agent-Based Modelling Meets Generative AI in Social Network Simulations": (
        "low",
        "当前缺英文摘要且无本地 PDF，暂不下结论；标题更像 social network simulation，后续优先补全文核实。",
    ),
}

ADJACENT_EXCLUDE_BACKGROUND = {
    "AgentSims: An Open-Source Sandbox for Large Language Model Evaluation": (
        "medium",
        "摘要聚焦通用 agent evaluation sandbox，空间目标不明确，先按 E1 排除出本轮空间相关语料。",
    ),
    "A survey on large language model based autonomous agents": (
        "high",
        "通用 agent survey，不是 spatial reasoning / spatially-aware corpus，按 E1 排除。",
    ),
    "A Survey on Large Language Model-Based Game Agents": (
        "medium",
        "综述范围过宽，未直接服务 spatial capability boundary，先按 E1 排除出正式 Phase 1 语料。",
    ),
    "Large language models empowered agent-based modeling and simulation: a survey and perspectives": (
        "medium",
        "这是 general LLM+ABM survey，不直接回答空间能力边界，先按 E1 排除出本轮正式语料。",
    ),
    "Methods That Support the Validation of Agent-Based Models: An Overview and Discussion": (
        "high",
        "传统 ABM validation overview，既非 LLM 也非空间能力论文，按 E3 排除。",
    ),
    "On The Planning Abilities of OpenAI's o1 Models: Feasibility, Optimality, and Generalizability": (
        "high",
        "标题与摘要不显示空间目标，属于一般 planning 能力，不纳入本轮空间语料。",
    ),
    "The Rise and Potential of Large Language Model Based Agents: A Survey": (
        "high",
        "通用 LLM agent survey，不直接服务 spatial boundary，按 E1 排除。",
    ),
    "Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling": (
        "medium",
        "聚焦 generative social simulation validation，而非空间能力边界，先按 E1 排除。",
    ),
}

FOUNDATIONAL_EXCLUDE_OVERBROAD = {
    "<b>Language and space.</b> Ed. By Paul Bloom, Mary A. Peterson, Lynn Nadel, and Merrill F. Garrett. Cambridge, MA &amp; London: MIT Press/Bradford, 1996. Pp. x, 597. $50.00.": (
        "high",
        "这是 broad book review，不是本综述需要的直接桥接证据，先排除。",
    ),
    "Building Problem Spaces for Deaf and Hard of Hearing Students’ Spatial Cognition in a Programming Language": (
        "high",
        "虽与 spatial cognition 相关，但与空间构型-社会行为桥接太远，先排除。",
    ),
    "Handbook of spatial cognition.": (
        "medium",
        "通用 handbook 过宽，不适合作为本轮 foundational 主体。",
    ),
    "LANGUAGE AND SPACE": (
        "medium",
        "通用语言与空间汇编过宽，先排除以收缩 foundational。",
    ),
    "Language, cognition, and space:the state of the art and new directions": (
        "medium",
        "广义 edited volume，当前超出本轮最小桥接集，先排除。",
    ),
    "Space in language and cognition explorations in cognitive diversity": (
        "medium",
        "通用认知多样性 volume，当前不直接服务本文的空间-社会桥接。",
    ),
    "Space in Languages": (
        "medium",
        "语言类型学范围过宽，当前先不进入正式 foundational 集。",
    ),
    "Spatial cognition : brain bases and development": (
        "medium",
        "这是广义空间认知基础书，不是最直接的社会/构型桥接证据，先排除。",
    ),
    "Thought Without Language": (
        "medium",
        "过于宽泛的语言-思维讨论，不作为当前 foundational 主集合。",
    ),
}


def default_keep_note(row: dict[str, str]) -> tuple[str, str]:
    tier = row["current_tier"]
    if tier == "core":
        return "medium", "摘要层面基本支持当前 core 判断，但后续仍需全文确认空间输入细节。"
    if tier == "adjacent":
        return "medium", "摘要明确属于 spatial reasoning / embodied / geospatial capability 边界，先维持 adjacent。"
    return "medium", "摘要与当前 foundational 定位基本一致，可暂作理论或桥接背景保留。"


def review_row(row: dict[str, str]) -> dict[str, str]:
    title = row["title"]
    abstract = row.get("abstract", "").strip()
    current_tier = row["current_tier"]

    result = dict(row)
    result["r1_decision"] = "keep"
    result["r1_recommended_tier"] = current_tier
    result["r1_exclusion_reason"] = ""
    result["r1_confidence"] = ""
    result["r1_note"] = ""

    if not abstract:
        result["r1_decision"] = "hold_missing_abstract"
        result["r1_recommended_tier"] = current_tier
        result["r1_confidence"] = "low"
        result["r1_note"] = "当前缺英文摘要，abstract-only 复核无法完成；需补全文或元数据。"
        return result

    if title in CORE_KEEP:
        confidence, note = CORE_KEEP[title]
        result["r1_confidence"] = confidence
        result["r1_note"] = note
        return result

    if title in CORE_DOWNGRADE_TO_ADJACENT:
        confidence, note = CORE_DOWNGRADE_TO_ADJACENT[title]
        result["r1_decision"] = "downgrade"
        result["r1_recommended_tier"] = "adjacent"
        result["r1_confidence"] = confidence
        result["r1_note"] = note
        return result

    if title in CORE_EXCLUDE_NO_SPACE:
        confidence, note = CORE_EXCLUDE_NO_SPACE[title]
        result["r1_decision"] = "exclude"
        result["r1_recommended_tier"] = "excluded"
        result["r1_exclusion_reason"] = "E1"
        result["r1_confidence"] = confidence
        result["r1_note"] = note
        return result

    if title in CORE_HOLD_AMBIGUOUS_SPACE:
        confidence, note = CORE_HOLD_AMBIGUOUS_SPACE[title]
        result["r1_decision"] = "hold_ambiguous_space"
        result["r1_recommended_tier"] = current_tier
        result["r1_confidence"] = confidence
        result["r1_note"] = note
        return result

    if title in CORE_HOLD_MISSING_ABSTRACT:
        confidence, note = CORE_HOLD_MISSING_ABSTRACT[title]
        result["r1_decision"] = "hold_missing_abstract"
        result["r1_recommended_tier"] = current_tier
        result["r1_confidence"] = confidence
        result["r1_note"] = note
        return result

    if title in ADJACENT_EXCLUDE_BACKGROUND:
        confidence, note = ADJACENT_EXCLUDE_BACKGROUND[title]
        result["r1_decision"] = "exclude"
        result["r1_recommended_tier"] = "excluded"
        result["r1_exclusion_reason"] = "E1" if "E3" not in note else "E3"
        result["r1_confidence"] = confidence
        result["r1_note"] = note
        return result

    if title in FOUNDATIONAL_EXCLUDE_OVERBROAD:
        confidence, note = FOUNDATIONAL_EXCLUDE_OVERBROAD[title]
        result["r1_decision"] = "exclude"
        result["r1_recommended_tier"] = "excluded"
        result["r1_exclusion_reason"] = "E2"
        result["r1_confidence"] = confidence
        result["r1_note"] = note
        return result

    confidence, note = default_keep_note(row)
    result["r1_confidence"] = confidence
    result["r1_note"] = note
    return result


def build_summary(rows: list[dict[str, str]]) -> str:
    decision_counter = Counter(row["r1_decision"] for row in rows)
    tier_counter = Counter(row["r1_recommended_tier"] for row in rows)

    changed_rows = [row for row in rows if row["r1_decision"] in {"downgrade", "exclude", "hold_ambiguous_space", "hold_missing_abstract"}]

    lines = [
        "# Phase 1 Abstract Rereview Round 1 Summary",
        "",
        "日期：2026-04-13",
        "",
        "## 决策统计",
        "",
        f"- `keep`: `{decision_counter.get('keep', 0)}`",
        f"- `downgrade`: `{decision_counter.get('downgrade', 0)}`",
        f"- `exclude`: `{decision_counter.get('exclude', 0)}`",
        f"- `hold_ambiguous_space`: `{decision_counter.get('hold_ambiguous_space', 0)}`",
        f"- `hold_missing_abstract`: `{decision_counter.get('hold_missing_abstract', 0)}`",
        "",
        "## R1 推荐层级",
        "",
        f"- `core`: `{tier_counter.get('core', 0)}`",
        f"- `adjacent`: `{tier_counter.get('adjacent', 0)}`",
        f"- `foundational`: `{tier_counter.get('foundational', 0)}`",
        f"- `excluded`: `{tier_counter.get('excluded', 0)}`",
        "",
        "## 说明",
        "",
        "- 这一版是 `abstract-only` 复核，不是最终定稿。",
        "- `hold_ambiguous_space` 表示摘要显示社会模拟存在，但空间环境是否满足本综述定义仍需全文确认。",
        "- `hold_missing_abstract` 表示当前缺英文摘要，不能只靠 abstract 做稳健判断。",
        "",
        "## 需要优先全文复核的变化项",
        "",
    ]

    for row in changed_rows[:30]:
        lines.append(
            f"- `{row['r1_decision']}` | `{row['current_tier']} -> {row['r1_recommended_tier']}` | {row['title']} | {row['r1_note']}"
        )

    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    rows = read_rows(args.input)
    reviewed_rows = [review_row(row) for row in rows]

    fieldnames = list(reviewed_rows[0].keys())
    write_csv(args.output, reviewed_rows, fieldnames, encoding="utf-8-sig")
    args.summary_output.parent.mkdir(parents=True, exist_ok=True)
    args.summary_output.write_text(build_summary(reviewed_rows), encoding="utf-8")
    print(f"Wrote {len(reviewed_rows)} rows to {args.output}")
    print(f"Wrote summary to {args.summary_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
