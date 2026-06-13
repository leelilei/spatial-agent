#!/usr/bin/env python3
"""Local read-only dashboard for research markdown todo files."""

from __future__ import annotations

import argparse
import importlib
import json
import os
import re
import sys
import webbrowser
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from functools import partial
from http import HTTPStatus
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:  # pragma: no cover - local environment includes PyYAML
    yaml = None


SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parents[1]
LEGACY_RESEARCH_ROOT = Path("/Users/mac/Documents/6-Research")
LEGACY_PERSONAL_TODO_DIR = Path("/Users/mac/Documents/1-ProjectRes/Personal Todo")


def import_yaml_from_workspace_venv():
    candidates = [
        *REPO_ROOT.glob(".venv/Lib/site-packages"),
        *REPO_ROOT.glob(".venv/lib/python*/site-packages"),
    ]
    for candidate in candidates:
        if not candidate.exists():
            continue
        sys.path.insert(0, str(candidate))
        try:
            return importlib.import_module("yaml")
        except ImportError:
            continue
    return None


if yaml is None:
    yaml = import_yaml_from_workspace_venv()


COMPLIANCE_DIR = SCRIPT_DIR.parent / "research-standard"
try:
    if str(COMPLIANCE_DIR) not in sys.path:
        sys.path.insert(0, str(COMPLIANCE_DIR))
    import check_compliance  # type: ignore
except Exception:  # noqa: BLE001 - compliance view is optional
    check_compliance = None


def configured_path(env_name: str) -> Path | None:
    value = os.environ.get(env_name)
    return Path(value).expanduser() if value else None


RESEARCH_ROOT = (
    configured_path("RESEARCH_DASHBOARD_ROOT")
    or (LEGACY_RESEARCH_ROOT if LEGACY_RESEARCH_ROOT.exists() else REPO_ROOT)
)
# Single source of truth lives inside the repo and is an OVERRIDE layer only:
# projects are auto-discovered from RESEARCH_ROOT/*/docs/guides/todolist.md, and
# sources.json may rename / recolor / disable them or add non-standard paths.
SOURCES_CONFIG_PATH = configured_path("RESEARCH_DASHBOARD_SOURCES") or (SCRIPT_DIR / "sources.json")

# Accent palette assigned by discovery order when no override sets a colour.
ACCENT_PALETTE = ["#0071e3", "#34c759", "#ff9500", "#af52de", "#ff2d55", "#5856d6", "#00c7be"]

# Directories that are not paper projects (learning / tooling). Mirrors the
# research-standard exclusion list so the dashboard and compliance agree.
if check_compliance is not None:
    EXCLUDED_DIR_NAMES = set(check_compliance.EXCLUDED_DIR_NAMES)
else:
    EXCLUDED_DIR_NAMES = {"0-Tools", "0-LLM-learning", "2-GAME-AGENT"}

# Staleness thresholds (days since 更新日期) for the "心里有底" freshness badge.
STALE_WARN_DAYS = 14
STALE_BLOCK_DAYS = 30

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
PHASE_RE = re.compile(r"(?:^|\s)Phase\s*(\d+)\s*(?:[-\u2013\u2014:：]\s*)?(.*)$", re.I)
TASK_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s+(.+?)\s*$")
PRIORITY_RE = re.compile(r"Priority\s*(\d+)", re.I)
PROJECT_MAP_STATUSES = {"done", "current", "next", "planned", "blocked", "draft", "ready", "missing"}
PROJECT_MAP_STATUS_ALIASES = {
    "complete": "done",
    "completed": "done",
    "finished": "done",
    "in_progress": "current",
    "active": "current",
    "todo": "planned",
    "not_started": "planned",
    "empty": "planned",
    "open": "planned",
}
PROJECT_MAP_LANES = {"done", "now", "next", "paper"}


@dataclass
class PhaseBuilder:
    number: int
    title: str
    tasks: list[dict]


def discover_source_configs() -> list[dict]:
    """Auto-discover paper projects from RESEARCH_ROOT/*/docs/guides/todolist.md."""
    configs: list[dict] = []
    index = 0
    for todo_path in sorted(RESEARCH_ROOT.glob("*/docs/guides/todolist.md")):
        project_dir = todo_path.parents[2]
        name = project_dir.name
        if name in EXCLUDED_DIR_NAMES or name.startswith("."):
            continue
        configs.append(
            {
                "id": name.lower(),
                "name": name,
                "path": str(todo_path),
                "accent": ACCENT_PALETTE[index % len(ACCENT_PALETTE)],
                "enabled": True,
            }
        )
        index += 1
    return configs


def apply_source_overrides(configs: list[dict], overrides: list[dict]) -> list[dict]:
    """Merge sources.json overrides onto discovered configs (matched by id)."""
    by_id = {config["id"]: config for config in configs}
    extra: list[dict] = []
    for index, override in enumerate(overrides):
        override_id = str(override.get("id") or "").strip()
        target = by_id.get(override_id)
        if target is None:
            # A manual entry for a non-standard path is only usable if it has one.
            if override.get("path"):
                extra.append(
                    {
                        "id": override_id or f"source-{index + 1}",
                        "name": str(override.get("name") or override_id or f"Source {index + 1}"),
                        "path": str(override["path"]),
                        "accent": str(override.get("accent") or ACCENT_PALETTE[0]),
                        "enabled": bool(override.get("enabled", True)),
                    }
                )
            continue
        if override.get("name"):
            target["name"] = str(override["name"])
        if override.get("accent"):
            target["accent"] = str(override["accent"])
        if override.get("path"):
            target["path"] = str(override["path"])
        if "enabled" in override:
            target["enabled"] = bool(override["enabled"])
    return configs + extra


def load_source_configs() -> tuple[list[dict], str | None]:
    configs = discover_source_configs()
    config_error: str | None = None

    if SOURCES_CONFIG_PATH.exists():
        try:
            payload = json.loads(SOURCES_CONFIG_PATH.read_text(encoding="utf-8"))
            configs = apply_source_overrides(configs, payload.get("sources", []))
        except Exception as exc:  # noqa: BLE001 - surface local config errors in UI
            config_error = f"无法读取覆盖配置 sources.json：{exc}"

    if not configs:
        config_error = config_error or (
            f"未在 {RESEARCH_ROOT} 下发现任何 docs/guides/todolist.md"
        )
    return configs, config_error


def dashboard_state() -> dict:
    configs, config_error = load_source_configs()
    sources = [parse_source(config) for config in configs]

    totals = {
        "sourceCount": len(sources),
        "readableCount": sum(1 for source in sources if source["readable"]),
        "errorCount": sum(1 for source in sources if source["error"]),
        "openTasks": sum(source["taskCounts"]["open"] for source in sources),
        "p0": sum(source["priorityCounts"].get("P0", 0) for source in sources),
        "p1": sum(source["priorityCounts"].get("P1", 0) for source in sources),
        "phaseCount": sum(len(source["phases"]) for source in sources),
        "progressCompleted": sum(source["progress"]["completed"] for source in sources),
        "progressTotal": sum(source["progress"]["total"] for source in sources),
        "activeCount": sum(1 for source in sources if source["readable"] and source["staleness"]["level"] in {"fresh", "warn"}),
        "staleCount": sum(1 for source in sources if source["readable"] and source["staleness"]["level"] == "stale"),
    }
    totals["progressFraction"] = fraction(totals["progressCompleted"], totals["progressTotal"])
    totals["weeklyCompletedDelta"] = weekly_completed_delta(totals["progressCompleted"])

    return {
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "configPath": str(SOURCES_CONFIG_PATH),
        "configError": config_error,
        "sources": sources,
        "totals": totals,
    }


def parse_source(config: dict) -> dict:
    base = {
        "id": config["id"],
        "name": config["name"],
        "path": config["path"],
        "accent": config["accent"],
        "enabled": config["enabled"],
        "readable": False,
        "error": None,
        "updateDate": None,
        "currentMainline": "",
        "priorityCounts": {"P0": 0, "P1": 0, "P2": 0, "P3": 0, "P4": 0},
        "taskCounts": {"open": 0, "completed": 0, "tracked": 0, "allOpen": 0},
        "tasks": [],
        "phases": [],
        "currentPhaseNumber": None,
        "nextActions": [],
        "progress": {"completed": 0, "open": 0, "total": 0, "fraction": 0, "mode": "none"},
        "staleness": {"days": None, "level": "unknown"},
        "compliance": None,
        "roadmap": {"mode": "none", "tracks": [], "phases": [], "error": None},
        "projectMap": {
            "mode": "none",
            "milestones": [],
            "mapNodes": [],
            "paper": {"sections": []},
            "history": [],
            "nextWork": [],
            "readinessSummary": {"total": 0, "ready": 0, "blocked": 0, "missing": 0, "planned": 0, "fraction": 0},
            "error": None,
        },
    }

    if not config["enabled"]:
        base["error"] = "项目源已停用"
        return base

    path = Path(config["path"]).expanduser()
    if not path.exists():
        base["error"] = f"找不到 todo 文件：{path}"
        return base

    try:
        content = path.read_text(encoding="utf-8")
    except Exception as exc:  # noqa: BLE001 - surface local file errors in UI
        base["error"] = f"无法读取 todo 文件：{exc}"
        return base

    parsed = parse_todo(content, config)
    roadmap = load_roadmap(path.with_name("roadmap.yaml"), parsed["phases"], parsed["currentPhaseNumber"], config)
    parsed["roadmap"] = roadmap
    parsed["phases"] = roadmap["phases"]
    parsed["nextActions"] = next_actions(parsed["tasks"], parsed["phases"])
    parsed["progress"] = progress_with_fallback(parsed["phases"], parsed["taskCounts"])
    parsed["staleness"] = staleness_info(parsed["updateDate"])
    parsed["compliance"] = compliance_info(path)
    parsed["projectMap"] = load_project_map(
        path.with_name("project_map.yaml"),
        path,
        config,
        roadmap,
        parsed["phases"],
        parsed["tasks"],
        parsed["nextActions"],
        parsed["progress"],
        parsed["currentMainline"],
    )
    parsed.update({"readable": True, "error": None})
    return {**base, **parsed}


def progress_with_fallback(phases: list[dict], task_counts: dict) -> dict:
    """Phase-based progress when phases exist; otherwise fall back to all checkboxes."""
    summary = progress_summary(phases)
    if summary["total"] > 0:
        summary["mode"] = "phase"
        return summary
    completed = task_counts.get("completed", 0)
    total = task_counts.get("tracked", 0)
    if total <= 0:
        return {"completed": 0, "open": 0, "total": 0, "fraction": 0, "mode": "none"}
    return {
        "completed": completed,
        "open": total - completed,
        "total": total,
        "fraction": fraction(completed, total),
        "mode": "checkbox",
    }


def staleness_info(update_date: str | None) -> dict:
    if not update_date:
        return {"days": None, "level": "unknown"}
    try:
        updated = datetime.strptime(update_date, "%Y-%m-%d").date()
    except ValueError:
        return {"days": None, "level": "unknown"}
    days = (datetime.now().date() - updated).days
    if days < 0:
        days = 0
    if days <= STALE_WARN_DAYS:
        level = "fresh"
    elif days <= STALE_BLOCK_DAYS:
        level = "warn"
    else:
        level = "stale"
    return {"days": days, "level": level}


def compliance_info(todo_path: Path) -> dict | None:
    if check_compliance is None:
        return None
    try:
        report = check_compliance.check_project(infer_project_root(todo_path))
    except Exception:  # noqa: BLE001 - compliance view must never break the board
        return None
    return {
        "achievedLevel": report.get("achievedLevel"),
        "levels": [
            {"code": level["code"], "name": level["name"], "complete": level["complete"], "missing": level["missing"]}
            for level in report.get("levels", [])
        ],
        "strayProposalVersions": report.get("strayProposalVersions", []),
    }


def weekly_completed_delta(current_completed: int) -> int:
    """Net completed tasks vs the snapshot closest to ~7 days ago (0 if no history)."""
    history_path = SCRIPT_DIR / "history.jsonl"
    if not history_path.exists():
        return 0
    totals_by_date: dict[str, int] = {}
    try:
        for line in history_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            entry = json.loads(line)
            date = entry.get("date")
            if not date:
                continue
            totals_by_date[date] = sum(int(s.get("completed", 0)) for s in entry.get("sources", []))
    except Exception:  # noqa: BLE001 - trend delta is best-effort
        return 0
    if not totals_by_date:
        return 0
    target = (datetime.now().date() - timedelta(days=7)).isoformat()
    on_or_before = [d for d in totals_by_date if d <= target]
    baseline_date = max(on_or_before) if on_or_before else min(totals_by_date)
    return current_completed - totals_by_date[baseline_date]


def parse_todo(content: str, config: dict) -> dict:
    headings: dict[int, str] = {}
    update_date = None
    current_mainline = ""
    current_phase_index: int | None = None
    phase_builders: list[PhaseBuilder] = []
    active_tasks: list[dict] = []
    fallback_tasks: list[dict] = []
    all_open_tasks: list[dict] = []
    completed_count = 0
    tracked_count = 0

    lines = content.splitlines()
    for line_number, line in enumerate(lines, start=1):
        if update_date is None and "更新日期" in line:
            update_date = first_date(line)

        if "当前主线" in line:
            current_mainline = clean_markdown(text_after_colon(line))

        heading = parse_heading(line)
        if heading:
            level, text = heading
            headings[level] = text
            for key in [key for key in headings if key > level]:
                del headings[key]

            phase = parse_phase_heading(text) if level <= 2 else None
            if phase:
                phase_builders.append(PhaseBuilder(number=phase[0], title=phase[1], tasks=[]))
                current_phase_index = len(phase_builders) - 1
            elif level <= 2:
                current_phase_index = None
            continue

        task_match = TASK_RE.match(line)
        if not task_match:
            continue

        heading_path = [headings[key] for key in sorted(headings)]
        if is_deferred_section(heading_path):
            continue

        checked = task_match.group(1).lower() == "x"
        title = clean_markdown(task_match.group(2))
        tracked_count += 1

        if current_phase_index is not None:
            phase_builders[current_phase_index].tasks.append(
                {
                    "title": title,
                    "completed": checked,
                    "lineNumber": line_number,
                    "sourceId": config["id"],
                    "sourceName": config["name"],
                    "sourceAccent": config["accent"],
                }
            )

        if checked:
            completed_count += 1
            continue

        priority = priority_info(heading_path)
        task = {
            "title": title,
            "priorityLabel": priority["label"],
            "priorityName": priority["name"],
            "priorityValue": priority["value"],
            "lineNumber": line_number,
            "sourceId": config["id"],
            "sourceName": config["name"],
            "sourceAccent": config["accent"],
        }
        all_open_tasks.append(task)

        if "执行优先级" in heading_path:
            active_tasks.append(task)
        else:
            fallback_tasks.append(task)

    current_phase_number = parse_phase_number(current_mainline)
    phases = [
        make_phase(builder, config, current_phase_number)
        for builder in phase_builders
    ]
    chosen_tasks = sorted(active_tasks or fallback_tasks, key=task_sort_key)
    priority_counts = {"P0": 0, "P1": 0, "P2": 0, "P3": 0, "P4": 0}
    for task in chosen_tasks:
        priority_counts[task["priorityLabel"]] = priority_counts.get(task["priorityLabel"], 0) + 1

    return {
        "updateDate": update_date,
        "currentMainline": current_mainline,
        "priorityCounts": priority_counts,
        "taskCounts": {
            "open": len(chosen_tasks),
            "completed": completed_count,
            "tracked": tracked_count,
            "allOpen": len(all_open_tasks),
        },
        "tasks": chosen_tasks,
        "phases": sorted(phases, key=lambda phase: phase["number"]),
        "currentPhaseNumber": current_phase_number,
        "nextActions": next_actions(chosen_tasks, phases),
        "progress": progress_summary(phases),
    }


def load_roadmap(roadmap_path: Path, md_phases: list[dict], current_phase_number: int | None, config: dict) -> dict:
    if not roadmap_path.exists():
        return {
            "mode": "derived",
            "path": str(roadmap_path),
            "project": config["name"],
            "currentPhase": current_phase_number,
            "tracks": [],
            "phases": sorted(md_phases, key=lambda phase: phase["number"]),
            "error": None,
        }

    if yaml is None:
        return {
            "mode": "derived",
            "path": str(roadmap_path),
            "project": config["name"],
            "currentPhase": current_phase_number,
            "tracks": [],
            "phases": sorted(md_phases, key=lambda phase: phase["number"]),
            "error": "当前环境没有 PyYAML，无法读取结构化路线图。",
        }

    try:
        payload = yaml.safe_load(roadmap_path.read_text(encoding="utf-8")) or {}
        return structured_roadmap(payload, roadmap_path, md_phases, current_phase_number, config)
    except Exception as exc:  # noqa: BLE001 - keep todo board usable
        return {
            "mode": "derived",
            "path": str(roadmap_path),
            "project": config["name"],
            "currentPhase": current_phase_number,
            "tracks": [],
            "phases": sorted(md_phases, key=lambda phase: phase["number"]),
            "error": f"路线图配置错误：{exc}",
        }


def structured_roadmap(
    payload: dict,
    roadmap_path: Path,
    md_phases: list[dict],
    current_phase_number: int | None,
    config: dict,
) -> dict:
    md_by_number = {phase["number"]: phase for phase in md_phases}
    roadmap_current = payload.get("currentPhase", current_phase_number)
    tracks = sorted(
        [normalize_track(track) for track in payload.get("tracks", [])],
        key=lambda track: track["order"],
    )
    track_ids = {track["id"] for track in tracks}
    phases = []

    for phase_config in payload.get("phases", []):
        number = int(phase_config["number"])
        md_phase = md_by_number.get(number, empty_phase(number, config, roadmap_current))
        track = str(phase_config.get("track", "untracked"))
        if track not in track_ids:
            tracks.append(
                {
                    "id": track,
                    "name": title_case(track),
                    "accent": config["accent"],
                    "order": 999,
                }
            )
            track_ids.add(track)

        phase = {
            **md_phase,
            "title": str(phase_config.get("title") or md_phase["title"]),
            "track": track,
            "summary": str(phase_config.get("summary") or ""),
            "outputs": [str(item) for item in phase_config.get("outputs", [])],
            "status": merged_status(str(phase_config.get("status") or md_phase["status"]), number, roadmap_current),
            "isCurrent": number == roadmap_current,
        }
        phases.append(phase)

    known_numbers = {phase["number"] for phase in phases}
    for md_phase in md_phases:
        if md_phase["number"] not in known_numbers:
            phases.append({**md_phase, "track": "untracked", "summary": "", "outputs": []})

    tracks = sorted(tracks, key=lambda track: track["order"])
    phases = sorted(phases, key=lambda phase: phase["number"])
    return {
        "mode": "structured",
        "path": str(roadmap_path),
        "version": payload.get("version", 1),
        "project": str(payload.get("project") or config["name"]),
        "currentPhase": roadmap_current,
        "tracks": tracks,
        "phases": phases,
        "error": None,
    }


def load_project_map(
    map_path: Path,
    todo_path: Path,
    config: dict,
    roadmap: dict,
    phases: list[dict],
    tasks: list[dict],
    next_actions_list: list[dict],
    progress: dict,
    current_mainline: str,
) -> dict:
    project_root = infer_project_root(todo_path)
    if not map_path.exists():
        return derived_project_map(
            map_path,
            config,
            roadmap,
            phases,
            tasks,
            next_actions_list,
            progress,
            current_mainline,
            None,
        )

    if yaml is None:
        return derived_project_map(
            map_path,
            config,
            roadmap,
            phases,
            tasks,
            next_actions_list,
            progress,
            current_mainline,
            "Current environment does not have PyYAML, so project_map.yaml could not be read.",
        )

    try:
        payload = yaml.safe_load(map_path.read_text(encoding="utf-8")) or {}
        if not isinstance(payload, dict):
            raise ValueError("project_map.yaml must contain a mapping at the top level")
        return normalize_project_map(
            payload,
            map_path,
            project_root,
            config,
            phases,
            tasks,
            next_actions_list,
            progress,
            current_mainline,
        )
    except Exception as exc:  # noqa: BLE001 - fallback keeps the dashboard usable
        return derived_project_map(
            map_path,
            config,
            roadmap,
            phases,
            tasks,
            next_actions_list,
            progress,
            current_mainline,
            f"Project map configuration error: {exc}",
        )


def normalize_project_map(
    payload: dict,
    map_path: Path,
    project_root: Path,
    config: dict,
    phases: list[dict],
    tasks: list[dict],
    next_actions_list: list[dict],
    progress: dict,
    current_mainline: str,
) -> dict:
    milestones = [
        normalize_milestone(item, project_root, index)
        for index, item in enumerate(ensure_list(payload.get("milestones")), start=1)
    ]
    map_nodes = [
        normalize_map_node(item, project_root, index)
        for index, item in enumerate(ensure_list(payload.get("mapNodes")), start=1)
    ]

    if not map_nodes:
        map_nodes = derived_map_nodes(phases, config, current_mainline)

    paper_payload = payload.get("paper") if isinstance(payload.get("paper"), dict) else {}
    paper_sections = [
        normalize_paper_section(item, project_root, index)
        for index, item in enumerate(ensure_list(paper_payload.get("sections")), start=1)
    ]

    next_work_payload = payload.get("nextWork") or payload.get("next_work")
    next_work = [
        normalize_work_item(item, index)
        for index, item in enumerate(ensure_list(next_work_payload), start=1)
    ] if next_work_payload else build_next_work(map_nodes, next_actions_list)

    return {
        "mode": "manifest",
        "path": str(map_path),
        "version": payload.get("version", 1),
        "project": str(payload.get("project") or config["name"]),
        "title": str(payload.get("title") or config["name"]),
        "currentFocus": str(payload.get("currentFocus") or current_mainline or ""),
        "researchQuestion": str(payload.get("researchQuestion") or ""),
        "milestones": milestones,
        "mapNodes": map_nodes,
        "paper": {"sections": paper_sections},
        "history": milestones or history_from_nodes(map_nodes),
        "nextWork": next_work,
        "readinessSummary": readiness_summary(paper_sections),
        "progress": progress,
        "taskCount": len(tasks),
        "error": None,
    }


def derived_project_map(
    map_path: Path,
    config: dict,
    roadmap: dict,
    phases: list[dict],
    tasks: list[dict],
    next_actions_list: list[dict],
    progress: dict,
    current_mainline: str,
    map_error: str | None,
) -> dict:
    map_nodes = derived_map_nodes(phases, config, current_mainline)
    if not map_nodes:
        map_nodes = [
            {
                "id": f"{config['id']}-research-thread",
                "title": current_mainline or config["name"],
                "lane": "now",
                "status": "current",
                "phase": None,
                "summary": "Simplified map generated from the active todo list.",
                "dependsOn": [],
                "outputs": [],
                "taskRefs": [],
                "nextActions": [str(task.get("title", "")) for task in next_actions_list[:4]],
            }
        ]

    paper_sections: list[dict] = []
    return {
        "mode": "derived",
        "path": str(map_path),
        "version": 1,
        "project": config["name"],
        "title": config["name"],
        "currentFocus": current_mainline or "",
        "researchQuestion": "",
        "milestones": history_from_nodes(map_nodes),
        "mapNodes": map_nodes,
        "paper": {"sections": paper_sections},
        "history": history_from_nodes(map_nodes),
        "nextWork": build_next_work(map_nodes, next_actions_list),
        "readinessSummary": readiness_summary(paper_sections),
        "progress": progress,
        "taskCount": len(tasks),
        "roadmapMode": roadmap.get("mode", "derived"),
        "error": map_error,
    }


def derived_map_nodes(phases: list[dict], config: dict, current_mainline: str) -> list[dict]:
    sorted_phases = sorted(phases, key=lambda phase: phase.get("number") or 0)
    current_phase = next((phase for phase in sorted_phases if phase.get("isCurrent")), None)
    current_number = current_phase.get("number") if current_phase else None
    first_future_number = next(
        (
            phase.get("number")
            for phase in sorted_phases
            if current_number is not None and (phase.get("number") or 0) > current_number
        ),
        None,
    )
    nodes = []

    for phase in sorted_phases:
        phase_number = phase.get("number")
        raw_status = str(phase.get("status") or "")
        status = normalize_project_status(raw_status, "planned")
        if phase.get("isCurrent"):
            lane = "now"
            status = "current"
        elif status == "done":
            lane = "done"
        elif current_number is not None and phase_number and phase_number > current_number:
            lane = "next"
            status = "next" if phase_number == first_future_number else "planned"
        elif raw_status == "in_progress":
            lane = "now"
            status = "current"
        else:
            lane = "done" if status == "done" else "next"

        open_tasks = [task for task in phase.get("tasks", []) if not task.get("completed")]
        outputs = [
            normalize_reference(item, infer_project_root(Path(config["path"])), "ready")
            for item in ensure_list(phase.get("outputs"))
        ]
        nodes.append(
            {
                "id": str(phase.get("id") or f"{config['id']}-phase-{phase_number or len(nodes) + 1}"),
                "title": f"Phase {phase_number}: {phase.get('title')}" if phase_number else str(phase.get("title") or config["name"]),
                "lane": lane,
                "status": status,
                "phase": phase_number,
                "summary": str(phase.get("summary") or current_mainline or "Generated from roadmap and todo progress."),
                "dependsOn": [],
                "outputs": outputs,
                "taskRefs": [
                    f"line-{task.get('lineNumber')}"
                    for task in phase.get("tasks", [])[:8]
                    if task.get("lineNumber")
                ],
                "nextActions": [str(task.get("title", "")) for task in open_tasks[:4]],
                "progress": {
                    "completed": phase.get("completedCount", 0),
                    "total": phase.get("totalCount", 0),
                    "fraction": phase.get("fraction", 0),
                },
            }
        )

    return nodes


def normalize_milestone(item: object, project_root: Path, index: int) -> dict:
    payload = item if isinstance(item, dict) else {"title": str(item)}
    title = str(payload.get("title") or f"Milestone {index}")
    return {
        "id": str(payload.get("id") or slugify(title, f"milestone-{index}")),
        "title": title,
        "status": normalize_project_status(payload.get("status"), "done"),
        "phase": optional_int(payload.get("phase")),
        "date": str(payload.get("date") or ""),
        "summary": str(payload.get("summary") or ""),
        "outputs": [
            normalize_reference(output, project_root, "ready")
            for output in ensure_list(payload.get("outputs"))
        ],
        "taskRefs": [str(item) for item in ensure_list(payload.get("taskRefs"))],
    }


def normalize_map_node(item: object, project_root: Path, index: int) -> dict:
    payload = item if isinstance(item, dict) else {"title": str(item)}
    title = str(payload.get("title") or f"Map node {index}")
    status = normalize_project_status(payload.get("status"), "planned")
    return {
        "id": str(payload.get("id") or slugify(title, f"node-{index}")),
        "title": title,
        "lane": normalize_map_lane(payload.get("lane"), status),
        "status": status,
        "phase": optional_int(payload.get("phase")),
        "summary": str(payload.get("summary") or ""),
        "dependsOn": [str(item) for item in ensure_list(payload.get("dependsOn"))],
        "outputs": [
            normalize_reference(output, project_root, "ready")
            for output in ensure_list(payload.get("outputs"))
        ],
        "taskRefs": [str(item) for item in ensure_list(payload.get("taskRefs"))],
        "nextActions": [str(item) for item in ensure_list(payload.get("nextActions"))],
    }


def normalize_paper_section(item: object, project_root: Path, index: int) -> dict:
    payload = item if isinstance(item, dict) else {"title": str(item)}
    title = str(payload.get("title") or f"Paper section {index}")
    return {
        "id": str(payload.get("id") or slugify(title, f"paper-section-{index}")),
        "title": title,
        "status": normalize_project_status(payload.get("status"), "planned"),
        "summary": str(payload.get("summary") or ""),
        "assets": [
            normalize_reference(asset, project_root, "missing")
            for asset in ensure_list(payload.get("assets"))
        ],
        "blockers": [str(item) for item in ensure_list(payload.get("blockers"))],
        "nextActions": [str(item) for item in ensure_list(payload.get("nextActions"))],
    }


def normalize_work_item(item: object, index: int) -> dict:
    if isinstance(item, dict):
        title = str(item.get("title") or item.get("summary") or f"Next work {index}")
        return {
            "id": str(item.get("id") or slugify(title, f"next-work-{index}")),
            "title": title,
            "status": normalize_project_status(item.get("status"), "next"),
            "summary": str(item.get("summary") or ""),
            "source": str(item.get("source") or "project_map"),
        }
    title = str(item)
    return {
        "id": slugify(title, f"next-work-{index}"),
        "title": title,
        "status": "next",
        "summary": "",
        "source": "project_map",
    }


def normalize_reference(item: object, project_root: Path, default_status: str) -> dict:
    if isinstance(item, dict):
        path_value = str(item.get("path") or "")
        label = str(item.get("label") or item.get("title") or path_value or "Asset")
        ref_type = str(item.get("type") or ("file" if path_value else "output"))
        status = normalize_project_status(item.get("status"), default_status)
    else:
        label = str(item)
        path_value = label if looks_like_path(label) else ""
        ref_type = "file" if path_value else "output"
        status = normalize_project_status(default_status, default_status)

    resolved = (project_root / path_value).resolve() if path_value else None
    return {
        "path": path_value,
        "label": label,
        "type": ref_type,
        "status": status,
        "exists": bool(resolved and resolved.exists()),
        "absolutePath": str(resolved) if resolved else "",
    }


def build_next_work(map_nodes: list[dict], next_actions_list: list[dict]) -> list[dict]:
    work = []
    focus_nodes = [
        node
        for node in map_nodes
        if node.get("lane") in {"now", "next"} or node.get("status") in {"current", "next"}
    ]
    for index, node in enumerate(focus_nodes[:4], start=1):
        work.append(
            {
                "id": f"node-{node.get('id')}",
                "title": str(node.get("title") or f"Map node {index}"),
                "status": normalize_project_status(node.get("status"), "next"),
                "summary": str(node.get("summary") or ""),
                "source": "map",
            }
        )

    for task in next_actions_list[:6]:
        title = str(task.get("title") or "")
        if not title:
            continue
        work.append(
            {
                "id": f"task-{task.get('lineNumber') or slugify(title, 'task')}",
                "title": title,
                "status": "next",
                "summary": f"Todo line {task.get('lineNumber')}" if task.get("lineNumber") else "",
                "source": "todo",
            }
        )
    return work


def history_from_nodes(map_nodes: list[dict]) -> list[dict]:
    history = []
    for node in map_nodes:
        if node.get("lane") != "done" and node.get("status") != "done":
            continue
        history.append(
            {
                "id": str(node.get("id") or ""),
                "title": str(node.get("title") or ""),
                "status": "done",
                "phase": node.get("phase"),
                "date": "",
                "summary": str(node.get("summary") or ""),
                "outputs": node.get("outputs", []),
                "taskRefs": node.get("taskRefs", []),
            }
        )
    return history


def readiness_summary(sections: list[dict]) -> dict:
    total = len(sections)
    ready = sum(1 for section in sections if section.get("status") in {"ready", "done", "draft"})
    blocked = sum(1 for section in sections if section.get("status") == "blocked")
    missing = sum(1 for section in sections if section.get("status") == "missing")
    planned = sum(1 for section in sections if section.get("status") == "planned")
    return {
        "total": total,
        "ready": ready,
        "blocked": blocked,
        "missing": missing,
        "planned": planned,
        "fraction": fraction(ready, total),
    }


def normalize_project_status(value: object, default: str) -> str:
    status = str(value or default).strip().lower().replace("-", "_").replace(" ", "_")
    status = PROJECT_MAP_STATUS_ALIASES.get(status, status)
    return status if status in PROJECT_MAP_STATUSES else default


def normalize_map_lane(value: object, status: str) -> str:
    lane = str(value or "").strip().lower().replace("-", "_").replace(" ", "_")
    if lane in PROJECT_MAP_LANES:
        return lane
    if status == "done":
        return "done"
    if status == "current":
        return "now"
    if status in {"draft", "ready", "missing"}:
        return "paper"
    return "next"


def infer_project_root(todo_path: Path) -> Path:
    try:
        return todo_path.expanduser().resolve().parents[2]
    except IndexError:
        return todo_path.expanduser().resolve().parent


def ensure_list(value: object) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def optional_int(value: object) -> int | None:
    if value in (None, ""):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def looks_like_path(value: str) -> bool:
    return "/" in value or "\\" in value or bool(re.search(r"\.[a-zA-Z0-9]{1,8}$", value))


def slugify(value: str, fallback: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or fallback


def normalize_track(track: dict) -> dict:
    track_id = str(track["id"])
    return {
        "id": track_id,
        "name": str(track.get("name") or title_case(track_id)),
        "accent": str(track.get("accent") or "#0071e3"),
        "order": int(track.get("order", 999)),
    }


def empty_phase(number: int, config: dict, current_phase_number: int | None) -> dict:
    is_current = number == current_phase_number
    return {
        "id": f"{config['id']}-phase-{number}",
        "sourceId": config["id"],
        "sourceName": config["name"],
        "sourceAccent": config["accent"],
        "number": number,
        "title": f"Phase {number}",
        "status": "current" if is_current else "empty",
        "isCurrent": is_current,
        "completedCount": 0,
        "openCount": 0,
        "totalCount": 0,
        "fraction": 0,
        "tasks": [],
    }


def merged_status(config_status: str, phase_number: int, current_phase_number: int | None) -> str:
    if phase_number == current_phase_number:
        return "current"
    if config_status == "planned":
        return "not_started"
    return config_status


def progress_summary(phases: list[dict]) -> dict:
    completed = sum(phase["completedCount"] for phase in phases)
    total = sum(phase["totalCount"] for phase in phases)
    open_count = sum(phase["openCount"] for phase in phases)
    return {
        "completed": completed,
        "open": open_count,
        "total": total,
        "fraction": fraction(completed, total),
    }


def title_case(value: str) -> str:
    return value.replace("_", " ").replace("-", " ").title()


def parse_heading(line: str) -> tuple[int, str] | None:
    match = HEADING_RE.match(line.strip())
    if not match:
        return None
    return len(match.group(1)), clean_markdown(match.group(2))


def parse_phase_heading(text: str) -> tuple[int, str] | None:
    match = PHASE_RE.search(text)
    if not match:
        return None
    number = int(match.group(1))
    title = clean_markdown(match.group(2)) or f"Phase {number}"
    return number, title


def parse_phase_number(text: str) -> int | None:
    match = re.search(r"Phase\s*(\d+)", text, re.I)
    return int(match.group(1)) if match else None


def make_phase(builder: PhaseBuilder, config: dict, current_phase_number: int | None) -> dict:
    completed = sum(1 for task in builder.tasks if task["completed"])
    total = len(builder.tasks)
    open_count = total - completed
    is_current = builder.number == current_phase_number
    if total == 0:
        status = "empty"
    elif completed == total:
        status = "complete"
    elif is_current:
        status = "current"
    elif completed > 0:
        status = "in_progress"
    else:
        status = "not_started"

    return {
        "id": f"{config['id']}-phase-{builder.number}",
        "sourceId": config["id"],
        "sourceName": config["name"],
        "sourceAccent": config["accent"],
        "number": builder.number,
        "title": builder.title,
        "status": status,
        "isCurrent": is_current,
        "completedCount": completed,
        "openCount": open_count,
        "totalCount": total,
        "fraction": fraction(completed, total),
        "tasks": builder.tasks,
    }


def next_actions(tasks: list[dict], phases: list[dict]) -> list[dict]:
    current_phase = next((phase for phase in phases if phase["isCurrent"]), None)
    if current_phase:
        phase_actions = [task for task in current_phase["tasks"] if not task["completed"]]
        if phase_actions:
            return phase_actions[:6]
    return tasks[:6]


def priority_info(heading_path: list[str]) -> dict:
    for heading in reversed(heading_path):
        if not heading.lower().startswith("priority"):
            continue
        match = PRIORITY_RE.search(heading)
        number = int(match.group(1)) if match else 4
        name = text_after_colon(heading) if ("：" in heading or ":" in heading) else heading
        return {"label": f"P{number}", "name": clean_markdown(name), "value": priority_value(number)}
    return {"label": "P4", "name": "一般任务", "value": priority_value(4)}


def priority_value(number: int) -> int:
    if number == 0:
        return 1
    if number == 1:
        return 5
    return 9 + number


def task_sort_key(task: dict) -> tuple[int, int, str]:
    return (task["priorityValue"], task["lineNumber"], task["title"])


def is_deferred_section(heading_path: list[str]) -> bool:
    return any("暂不做" in heading for heading in heading_path)


def first_date(text: str) -> str | None:
    match = DATE_RE.search(text)
    return match.group(1) if match else None


def text_after_colon(text: str) -> str:
    chinese = text.find("：")
    english = text.find(":")
    positions = [position for position in [chinese, english] if position >= 0]
    if not positions:
        return text
    position = min(positions)
    return text[position + 1 :]


def clean_markdown(text: str) -> str:
    cleaned = re.sub(r"^\s*>\s*", "", text)
    cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
    cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
    cleaned = re.sub(r"\*\*([^*]+)\*\*", r"\1", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def fraction(completed: int, total: int) -> float:
    return completed / total if total else 0


def record_snapshot(state: dict) -> None:
    """Record a daily snapshot of the dashboard state to history.jsonl."""
    history_path = SCRIPT_DIR / "history.jsonl"
    today = datetime.now().strftime("%Y-%m-%d")
    
    sources_data = []
    for s in state.get("sources", []):
        sources_data.append({
            "id": s.get("id"),
            "name": s.get("name"),
            "completed": s.get("progress", {}).get("completed", 0),
            "total": s.get("progress", {}).get("total", 0),
            "fraction": s.get("progress", {}).get("fraction", 0),
            "openTasks": s.get("taskCounts", {}).get("open", 0)
        })
    
    new_entry = {
        "date": today,
        "sources": sources_data
    }
    
    entries = []
    if history_path.exists():
        try:
            with open(history_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                        if entry.get("date") != today:
                            entries.append(entry)
                    except json.JSONDecodeError:
                        pass
        except Exception as exc:
            sys.stderr.write(f"Error reading history.jsonl: {exc}\n")
    
    entries.append(new_entry)
    entries = entries[-90:]
    
    try:
        with open(history_path, "w", encoding="utf-8") as f:
            for entry in entries:
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as exc:
        sys.stderr.write(f"Error writing to history.jsonl: {exc}\n")


class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - stdlib method name
        parsed = urlparse(self.path)
        if parsed.path == "/api/state":
            self.send_dashboard_state()
            return
        if parsed.path == "/api/history":
            self.send_history()
            return
        if parsed.path == "/":
            self.path = "/index.html"
        super().do_GET()

    def send_dashboard_state(self) -> None:
        try:
            state = dashboard_state()
            record_snapshot(state)
            payload = json.dumps(state, ensure_ascii=False).encode("utf-8")
            self.send_response(HTTPStatus.OK)
        except Exception as exc:  # noqa: BLE001 - return useful local error
            payload = json.dumps({"error": str(exc)}, ensure_ascii=False).encode("utf-8")
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)

        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def send_history(self) -> None:
        try:
            history_path = SCRIPT_DIR / "history.jsonl"
            entries = []
            if history_path.exists():
                with open(history_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line:
                            try:
                                entries.append(json.loads(line))
                            except json.JSONDecodeError:
                                pass
            payload = json.dumps(entries, ensure_ascii=False).encode("utf-8")
            self.send_response(HTTPStatus.OK)
        except Exception as exc:
            payload = json.dumps({"error": str(exc)}, ensure_ascii=False).encode("utf-8")
            self.send_response(HTTPStatus.INTERNAL_SERVER_ERROR)

        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, format: str, *args: object) -> None:
        sys.stderr.write("%s\n" % (format % args))


def run_server(port: int, should_open: bool) -> None:
    static_dir = Path(__file__).resolve().parent / "static"
    handler = partial(DashboardHandler, directory=str(static_dir))
    server = ThreadingHTTPServer(("127.0.0.1", port), handler)
    url = f"http://127.0.0.1:{port}"
    print(f"Research Dashboard running at {url}")
    if should_open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


def print_check() -> int:
    state = dashboard_state()
    print(json.dumps(state, ensure_ascii=False, indent=2))
    return 1 if state.get("configError") else 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve the local Research Dashboard.")
    parser.add_argument("--port", type=int, default=8765, help="Local port to bind.")
    parser.add_argument("--open", action="store_true", help="Open the dashboard in a browser.")
    parser.add_argument("--check", action="store_true", help="Print parsed state and exit.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.check:
        return print_check()
    run_server(args.port, args.open)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
