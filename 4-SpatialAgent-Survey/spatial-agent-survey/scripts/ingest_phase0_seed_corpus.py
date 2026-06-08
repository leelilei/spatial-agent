#!/usr/bin/env python3
"""Build a Phase 0 prescreened seed corpus from local survey assets."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = PROJECT_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from spatial_agent_survey.export import export_json
from spatial_agent_survey.ingest import dedupe_papers, make_paper_id, papers_to_rows, write_csv
from spatial_agent_survey.schemas import ExclusionReason, FinalStatus, PaperRecord, paper_fieldnames
from spatial_agent_survey.screening import sample_exclusion_recheck, summarize_prisma


PAPER_LIST_DEFAULTS = {
    "LLM-based game agents": FinalStatus.CORE,
    "Space Syntax theory and agent simulation": FinalStatus.FOUNDATIONAL,
    "Spatially-aware LLM agents": FinalStatus.ADJACENT,
    "NPC dialogue and behavior systems": FinalStatus.CORE,
    "Multi-agent social simulation and emergent behavior": FinalStatus.CORE,
    "Agent memory and cognitive architecture": FinalStatus.EXCLUDED,
    "Evaluation methodology": FinalStatus.EXCLUDED,
}

BACKGROUND_DEFAULTS = {
    "Space Syntax 经典文献": FinalStatus.FOUNDATIONAL,
    "Space Syntax 计算与应用": FinalStatus.FOUNDATIONAL,
    "LLM Agent 架构": FinalStatus.EXCLUDED,
    "LLM 推理与空间能力": FinalStatus.ADJACENT,
    "多智能体社会模拟": FinalStatus.CORE,
    "空间认知": FinalStatus.FOUNDATIONAL,
    "Embodied AI 与导航": FinalStatus.ADJACENT,
    "评估方法": FinalStatus.EXCLUDED,
    "ABM 经典": FinalStatus.FOUNDATIONAL,
}

SKIPPED_SECTIONS = {"Space Syntax computational tools"}


def normalize_title_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


CORE_OVERRIDES = {
    normalize_title_key("Generative Agents: Interactive Simulacra of Human Behavior"),
    normalize_title_key("Affordable Generative Agents"),
    normalize_title_key("Project Sid: Many-Agent Simulations Toward AI Civilization"),
    normalize_title_key("LIGS: Developing an LLM-Infused Game System for Emergent Narrative"),
    normalize_title_key("Artificial Leviathan: Exploring Social Evolution of LLM Agents Through the Lens of Hobbesian Social Contract Theory"),
    normalize_title_key("AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents"),
    normalize_title_key("LLM-Driven NPCs: Cross-Platform Dialogue System for Games and Social Platforms"),
    normalize_title_key("Generative agent-based modeling with actions grounded in physical, social, or digital space using Concordia"),
}

ADJACENT_OVERRIDES = {
    normalize_title_key("A Survey on Large Language Model-Based Game Agents"),
    normalize_title_key("When LLMs Recognize Your Space: Research on Experiences with Spatially Aware LLM Agents"),
    normalize_title_key("SARAH: Spatially Aware Real-time Agentic Humans"),
    normalize_title_key("Advancing Spatial Reasoning in Large Language Models: An In-Depth Evaluation and Enhancement Using the StepGame Benchmark"),
    normalize_title_key("SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities"),
    normalize_title_key("Reframing Spatial Reasoning Evaluation in Language Models: A Real-World Simulation Benchmark for Qualitative Reasoning"),
    normalize_title_key("ProAgent: Building Proactive Cooperative Agents with Large Language Models"),
    normalize_title_key("Voyager: An open-ended embodied agent with large language models"),
    normalize_title_key("AgentSims: An open-source sandbox for large language model evaluation"),
    normalize_title_key("Chain-of-thought prompting elicits reasoning in large language models"),
    normalize_title_key("ReAct: Synergizing reasoning and acting in language models"),
    normalize_title_key("Tree of thoughts: Deliberate problem solving with large language models"),
    normalize_title_key("SpartQA: A textual question answering benchmark for spatial reasoning"),
    normalize_title_key("StepGame: A new benchmark for robust multi-hop spatial reasoning in texts"),
    normalize_title_key("Language models represent space and time"),
    normalize_title_key("Habitat: A platform for embodied AI research"),
    normalize_title_key("ALFRED: A benchmark for interpreting grounded instructions for everyday tasks"),
    normalize_title_key("Beyond the nav-graph: Vision-and-language navigation in continuous environments"),
    normalize_title_key("SayNav: Grounding large language models for dynamic planning to navigation in new environments"),
}

FOUNDATIONAL_OVERRIDES = {
    normalize_title_key("The Social Logic of Space"),
    normalize_title_key("Space is the Machine: A Configurational Theory of Architecture"),
    normalize_title_key("From Isovists to Visibility Graphs: A Methodology for the Analysis of Architectural Space"),
    normalize_title_key("Space Syntax Based Agent Simulation"),
    normalize_title_key("Space Syntax Methodology (4th edition, draft)"),
    normalize_title_key("Agent-Based Analysis of Urban Spaces Using Space Syntax and Spatial Cognition Approaches: A Case Study in Bari, Italy"),
    normalize_title_key("Computational Analytical Methods for Buildings and Cities: Space Syntax and Shape Grammar"),
    normalize_title_key("Comparative Analysis of Pedestrian Volume Models: Agent-Based Models, Machine Learning Methods and Multiple Regression Analysis"),
    normalize_title_key("Evaluation of Spatial Visual Perception of Streets Based on Deep Learning and Spatial Syntax"),
    normalize_title_key("Visibility Graph Analysis vs. Human Mobility Patterns: An Empirical Validation of Simulation-Based Analysis Using Space Syntax in Public Squares"),
    normalize_title_key("Natural movement: or, configuration and attraction in urban pedestrian movement"),
    normalize_title_key("Crime and urban layout: The need for evidence"),
    normalize_title_key("Decoding Homes and Houses"),
    normalize_title_key("Depthmap: A program to perform visibility graph analysis"),
    normalize_title_key("Space Syntax: A brief introduction to its logic and analytical techniques"),
    normalize_title_key("The mathematics of spatial configuration: Revisiting, revising and critiquing justified plan graph theory"),
    normalize_title_key("Urban Network Analysis: A new toolbox for ArcGIS"),
    normalize_title_key("Is spatial intelligibility critical to the design of large-scale virtual environments?"),
    normalize_title_key("Space Syntax for modeling building evacuation"),
    normalize_title_key("The New Science of Cities"),
    normalize_title_key("Vector-Based Navigation Using Grid-Like Representations in Artificial Agents"),
    normalize_title_key("Place Cells, Grid Cells, and Memory"),
    normalize_title_key("A Non-Spatial Account of Place and Grid Cells Based on Clustering Models of Concept Learning"),
    normalize_title_key("Cognitive maps in rats and men"),
    normalize_title_key("The Hippocampus as a Cognitive Map"),
    normalize_title_key("Space in Language and Cognition"),
    normalize_title_key("\"What\" and \"where\" in spatial language and spatial cognition"),
    normalize_title_key("Navigates Like Me: Understanding How People Evaluate Human-Like AI in Video Games"),
    normalize_title_key("Turing's Test and Believable AI in Games"),
    normalize_title_key("Assessing Believability"),
    normalize_title_key("Dynamic models of segregation"),
    normalize_title_key("Growing Artificial Societies: Social Science from the Bottom Up"),
    normalize_title_key("The dissemination of culture: A model with local convergence and global polarization"),
}

EXCLUSION_OVERRIDES = {
    normalize_title_key("MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents"): (
        ExclusionReason.E1,
        "Collaboration topology benchmark without a persistent spatial environment.",
    ),
    normalize_title_key("Deflanderization for Game Dialogue: Balancing Character Authenticity with Task Execution in LLM-based NPCs"): (
        ExclusionReason.E1,
        "Dialogue-quality study without an analyzable spatial environment.",
    ),
    normalize_title_key("Tricking LLM-Based NPCs into Spilling Secrets"): (
        ExclusionReason.E1,
        "Security study for NPC prompting, not a spatial social simulation.",
    ),
    normalize_title_key("Ubisoft Project NEO NPC (Industry Prototype)"): (
        ExclusionReason.E5,
        "Industry news/prototype coverage rather than an accessible research paper.",
    ),
    normalize_title_key("Fixed-Persona SLMs with Modular Memory: Scalable NPC Dialogue on Consumer Hardware"): (
        ExclusionReason.E1,
        "Persona-memory study without a stable spatial environment.",
    ),
    normalize_title_key("Character-LLM: A Trainable Agent for Role-Playing"): (
        ExclusionReason.E1,
        "Role-playing agent work without an explicit spatial environment.",
    ),
    normalize_title_key("Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game"): (
        ExclusionReason.E1,
        "Strategic social game without a spatial environment.",
    ),
    normalize_title_key("Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization (LSPO)"): (
        ExclusionReason.E1,
        "Strategic social game without a spatial environment.",
    ),
    normalize_title_key("S³: Social-network Simulation System with Large Language Model-Empowered Agents"): (
        ExclusionReason.E1,
        "Social-network simulation without an embodied or navigable space.",
    ),
    normalize_title_key("SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents"): (
        ExclusionReason.E1,
        "Social interaction benchmark without a spatial environment.",
    ),
    normalize_title_key("Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents (AgeMem)"): (
        ExclusionReason.E1,
        "Agent memory infrastructure without spatial or social simulation focus.",
    ),
    normalize_title_key("MemGPT: Towards LLMs as Operating Systems"): (
        ExclusionReason.E1,
        "Memory/OS architecture paper without a spatial environment.",
    ),
    normalize_title_key("Reflexion: Language Agents with Verbal Reinforcement Learning"): (
        ExclusionReason.E1,
        "General agent improvement framework without spatial environment evidence.",
    ),
    normalize_title_key("A-MEM: Agentic Memory for LLM Agents"): (
        ExclusionReason.E1,
        "Memory module paper without spatial environment evidence.",
    ),
    normalize_title_key("GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games"): (
        ExclusionReason.E2,
        "Game benchmark emphasizes task performance rather than social behavior.",
    ),
    normalize_title_key("Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"): (
        ExclusionReason.E1,
        "Evaluation methodology paper without a spatial environment.",
    ),
    normalize_title_key("A Survey on LLM-as-a-Judge"): (
        ExclusionReason.E1,
        "Evaluation survey without a spatial environment.",
    ),
    normalize_title_key("Network Formation and Dynamics Among Multi-LLMs"): (
        ExclusionReason.E1,
        "Network dynamics study without a spatial environment.",
    ),
    normalize_title_key("Unveiling the Collective Behaviors of Large Language Model-Based Autonomous Agents in an Online Community"): (
        ExclusionReason.E1,
        "Online community study without a navigable spatial environment.",
    ),
    normalize_title_key("MetaGPT: Meta programming for a multi-agent collaborative framework"): (
        ExclusionReason.E1,
        "Software collaboration framework without a spatial environment.",
    ),
    normalize_title_key("AgentBench: Evaluating LLMs as agents"): (
        ExclusionReason.E1,
        "Agent benchmark without a stable spatial environment.",
    ),
    normalize_title_key("Toolformer: Language models can teach themselves to use tools"): (
        ExclusionReason.E1,
        "Tool-use model paper without a spatial environment.",
    ),
    normalize_title_key("HuggingGPT: Solving AI tasks with ChatGPT and its friends in Hugging Face"): (
        ExclusionReason.E1,
        "Task orchestration framework without a spatial environment.",
    ),
    normalize_title_key("Large language model-empowered agents for simulating macroeconomic activities"): (
        ExclusionReason.E1,
        "Macroeconomic simulation without a navigable spatial environment.",
    ),
    normalize_title_key("Out of one, many: Using language models to simulate human samples"): (
        ExclusionReason.E1,
        "Population sampling study without a spatial environment.",
    ),
    normalize_title_key("Playing repeated games with large language models"): (
        ExclusionReason.E1,
        "Repeated-game study without a spatial environment.",
    ),
    normalize_title_key("Lost in the middle: How language models use long contexts"): (
        ExclusionReason.E1,
        "Context-length paper without spatial or social simulation evidence.",
    ),
}


def split_authors(text: str) -> list[str]:
    cleaned = text.replace(" and ", ", ").replace("&", ",")
    parts = [part.strip() for part in cleaned.split(",") if part.strip()]
    return parts


def clean_title(text: str) -> str:
    title = text.strip().strip("*").strip()
    title = re.sub(r"\s+", " ", title)
    for suffix in (
        ". Cambridge University Press",
        ". MIT Press",
        ". Clarendon Press",
        ". International Journal of Design Computing",
    ):
        if title.endswith(suffix):
            title = title[: -len(suffix)].rstrip()
    return title


def section_slug(source_name: str, section_name: str) -> str:
    section = re.sub(r"[^a-z0-9]+", "_", section_name.lower()).strip("_")
    return f"{source_name}_{section}"


def parse_paper_list(path: Path) -> list[PaperRecord]:
    records: list[PaperRecord] = []
    current_section = ""
    lines = path.read_text(encoding="utf-8").splitlines()
    for line in lines:
        if line.startswith("### "):
            current_section = line[4:].strip()
            continue
        if current_section in SKIPPED_SECTIONS:
            continue
        if not line.startswith("|") or "[论文" in line or "---" in line:
            continue
        cells = [cell.strip() for cell in line.strip().split("|")[1:-1]]
        if len(cells) != 6 or cells[0] == "下载状态" or cells[0] == "---":
            continue
        match = re.search(r"\[([^\]]+)\]\(([^)]+)\)", cells[1])
        title = clean_title(match.group(1) if match else cells[1])
        url = match.group(2).strip() if match else ""
        authors = split_authors(cells[2])
        year_text = cells[3].strip()
        year = int(year_text) if year_text.isdigit() else None
        record = PaperRecord(
            paper_id=make_paper_id(title=title, year=year, url=url),
            title=title,
            abstract="",
            year=year,
            venue=current_section,
            url=url,
            doi="",
            authors=authors,
            source_families=[section_slug("paper_list", current_section)],
            notes="Seeded from local generated paper list for Phase 0 prescreening.",
        )
        records.append(record)
    return records


def parse_background_references(path: Path) -> list[PaperRecord]:
    records: list[PaperRecord] = []
    current_section = ""
    in_references = False
    pattern = re.compile(
        r"^(?P<authors>.+?)\s*\((?P<year>\d{4})\)\.\s*(?:(?:\*(?P<title1>[^*]+)\*)|(?P<title2>.*?))(?:\.\s*(?:\*|In\s+\*|$))"
    )
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("### Space Syntax 经典文献"):
            in_references = True
            current_section = line[4:].strip()
            continue
        if not in_references:
            continue
        if line.startswith("### "):
            current_section = line[4:].strip()
            continue
        if not line.startswith("- "):
            continue
        body = line[2:].strip()
        match = pattern.search(body)
        if not match:
            continue
        year = int(match.group("year"))
        title = clean_title(match.group("title1") or match.group("title2") or "")
        authors = split_authors(match.group("authors"))
        record = PaperRecord(
            paper_id=make_paper_id(title=title, year=year),
            title=title,
            abstract="",
            year=year,
            venue=current_section,
            url="",
            doi="",
            authors=authors,
            source_families=[section_slug("background_refs", current_section)],
            notes="Seeded from local background survey reference list for Phase 0 prescreening.",
        )
        records.append(record)
    return records


def classify_record(record: PaperRecord) -> PaperRecord:
    key = normalize_title_key(record.title)
    note_parts = [record.notes]

    if key in FOUNDATIONAL_OVERRIDES:
        record.final_status = FinalStatus.FOUNDATIONAL
        record.corpus_tier = FinalStatus.FOUNDATIONAL
        note_parts.append("Tagged as foundational corpus during Phase 0 prescreen.")
    elif key in ADJACENT_OVERRIDES:
        record.final_status = FinalStatus.ADJACENT
        record.corpus_tier = FinalStatus.ADJACENT
        note_parts.append("Tagged as adjacent corpus during Phase 0 prescreen.")
    elif key in CORE_OVERRIDES:
        record.final_status = FinalStatus.CORE
        record.corpus_tier = FinalStatus.CORE
        note_parts.append("Tagged as core corpus during Phase 0 prescreen.")
    elif key in EXCLUSION_OVERRIDES:
        exclusion_reason, explanation = EXCLUSION_OVERRIDES[key]
        record.final_status = FinalStatus.EXCLUDED
        record.corpus_tier = FinalStatus.EXCLUDED
        record.exclusion_reason = exclusion_reason
        note_parts.append(explanation)
    else:
        source_section = record.venue
        default_status = PAPER_LIST_DEFAULTS.get(source_section) or BACKGROUND_DEFAULTS.get(source_section)
        if default_status == FinalStatus.FOUNDATIONAL:
            record.final_status = FinalStatus.FOUNDATIONAL
            record.corpus_tier = FinalStatus.FOUNDATIONAL
            note_parts.append("Tagged as foundational by section-level Phase 0 rule.")
        elif default_status == FinalStatus.ADJACENT:
            record.final_status = FinalStatus.ADJACENT
            record.corpus_tier = FinalStatus.ADJACENT
            note_parts.append("Tagged as adjacent by section-level Phase 0 rule.")
        elif default_status == FinalStatus.CORE:
            record.final_status = FinalStatus.CORE
            record.corpus_tier = FinalStatus.CORE
            note_parts.append("Tagged as core by section-level Phase 0 rule.")
        else:
            record.final_status = FinalStatus.EXCLUDED
            record.corpus_tier = FinalStatus.EXCLUDED
            record.exclusion_reason = ExclusionReason.E1
            note_parts.append("Excluded by default because no stable spatial corpus tier was identified.")

    record.notes = " ".join(part for part in note_parts if part).strip()
    return record


def screening_rows(records: list[PaperRecord]) -> list[dict]:
    rows: list[dict] = []
    for record in records:
        rows.append(
            {
                "paper_id": record.paper_id,
                "title": record.title,
                "year": record.year or "",
                "venue": record.venue,
                "source_families": "; ".join(record.source_families),
                "final_status": record.final_status.value if record.final_status else "",
                "corpus_tier": record.corpus_tier.value if record.corpus_tier else "",
                "exclusion_reason": record.exclusion_reason.value if record.exclusion_reason else "",
                "notes": record.notes,
            }
        )
    return rows


def write_summary(path: Path, records: list[PaperRecord]) -> None:
    counts = Counter(record.final_status.value for record in records if record.final_status)
    section_counts = Counter()
    for record in records:
        for family in record.source_families:
            section_counts[family] += 1

    lines = [
        "# Phase 0 Seed Corpus Summary",
        "",
        "This local prescreen seed corpus was assembled from `assets/papers/generated/paper_list.md`",
        "and the reference appendix in `docs/background/spatial_agent_survey.md`.",
        "",
        f"- Total unique candidate papers: {len(records)}",
        f"- Core: {counts.get(FinalStatus.CORE.value, 0)}",
        f"- Adjacent: {counts.get(FinalStatus.ADJACENT.value, 0)}",
        f"- Foundational: {counts.get(FinalStatus.FOUNDATIONAL.value, 0)}",
        f"- Excluded: {counts.get(FinalStatus.EXCLUDED.value, 0)}",
        "",
        "## Notes",
        "",
        "- This is a Phase 0 prescreen asset, not the final PRISMA-ScR corpus.",
        "- Inclusion/exclusion decisions are quick-screen tags based on local metadata and existing notes.",
        "- Papers excluded at this stage still remain useful search traces for later corpus expansion.",
        "",
        "## Source Family Counts",
        "",
    ]
    for family, count in sorted(section_counts.items()):
        lines.append(f"- `{family}`: {count}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    paper_list_path = PROJECT_ROOT.parent / "assets" / "papers" / "generated" / "paper_list.md"
    background_path = PROJECT_ROOT.parent / "docs" / "background" / "spatial_agent_survey.md"

    parsed_records = parse_paper_list(paper_list_path) + parse_background_references(background_path)
    deduped, duplicates = dedupe_papers(parsed_records)
    classified = [classify_record(record) for record in deduped]

    if len(classified) < 80:
        raise SystemExit(f"Phase 0 seed corpus too small: expected >=80 unique papers, found {len(classified)}")

    processed_dir = PROJECT_ROOT / "data" / "processed"
    logs_dir = PROJECT_ROOT / "results" / "logs"

    papers_master_path = processed_dir / "papers_master.csv"
    dupes_path = processed_dir / "paper_duplicates.csv"
    screening_path = processed_dir / "screening_sheet.csv"
    recheck_path = processed_dir / "exclusion_recheck_sample.csv"
    prisma_path = logs_dir / "prisma_summary.json"
    summary_path = logs_dir / "phase0_seed_corpus_summary.md"

    rows = papers_to_rows(classified)
    write_csv(papers_master_path, rows, paper_fieldnames())
    write_csv(dupes_path, duplicates, ["kept_paper_id", "duplicate_paper_id", "reason"])

    screening = screening_rows(classified)
    write_csv(
        screening_path,
        screening,
        [
            "paper_id",
            "title",
            "year",
            "venue",
            "source_families",
            "final_status",
            "corpus_tier",
            "exclusion_reason",
            "notes",
        ],
    )
    write_csv(
        recheck_path,
        sample_exclusion_recheck(screening),
        [
            "paper_id",
            "title",
            "year",
            "venue",
            "source_families",
            "final_status",
            "corpus_tier",
            "exclusion_reason",
            "notes",
            "recheck_required",
        ],
    )
    export_json(prisma_path, summarize_prisma(screening))
    write_summary(summary_path, classified)

    counts = Counter(record.final_status.value for record in classified if record.final_status)
    print(
        "Phase 0 seed corpus ready:",
        f"total={len(classified)}",
        f"core={counts.get(FinalStatus.CORE.value, 0)}",
        f"adjacent={counts.get(FinalStatus.ADJACENT.value, 0)}",
        f"foundational={counts.get(FinalStatus.FOUNDATIONAL.value, 0)}",
        f"excluded={counts.get(FinalStatus.EXCLUDED.value, 0)}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
