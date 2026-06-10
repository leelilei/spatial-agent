#!/usr/bin/env python3
"""Local read-only dashboard for research markdown todo files."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import webbrowser
from dataclasses import dataclass
from datetime import datetime, timezone
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


def configured_path(env_name: str) -> Path | None:
    value = os.environ.get(env_name)
    return Path(value).expanduser() if value else None


RESEARCH_ROOT = (
    configured_path("RESEARCH_DASHBOARD_ROOT")
    or (LEGACY_RESEARCH_ROOT if LEGACY_RESEARCH_ROOT.exists() else REPO_ROOT)
)
PERSONAL_TODO_DIR = (
    configured_path("RESEARCH_DASHBOARD_CONFIG_DIR")
    or (LEGACY_PERSONAL_TODO_DIR if LEGACY_PERSONAL_TODO_DIR.exists() else SCRIPT_DIR)
)
SOURCES_CONFIG_PATH = configured_path("RESEARCH_DASHBOARD_SOURCES") or (PERSONAL_TODO_DIR / "sources.json")

DEFAULT_SOURCES = [
    {
        "id": "1-spatialagent",
        "name": "1-SpatialAgent",
        "path": str(RESEARCH_ROOT / "1-SpatialAgent/docs/guides/todolist.md"),
        "accent": "#0071e3",
        "enabled": True,
    },
    {
        "id": "2-game-agent",
        "name": "2-GAME-AGENT",
        "path": str(RESEARCH_ROOT / "2-GAME-AGENT/docs/guides/todolist.md"),
        "accent": "#34c759",
        "enabled": True,
    },
    {
        "id": "3-smga",
        "name": "3-SMGA",
        "path": str(RESEARCH_ROOT / "3-SMGA/docs/guides/todolist.md"),
        "accent": "#ff9500",
        "enabled": True,
    },
    {
        "id": "4-spatialagent-survey",
        "name": "4-SpatialAgent-Survey",
        "path": str(RESEARCH_ROOT / "4-SpatialAgent-Survey/docs/guides/todolist.md"),
        "accent": "#af52de",
        "enabled": True,
    },
]

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
PHASE_RE = re.compile(r"(?:^|\s)Phase\s*(\d+)\s*(?:[-\u2013\u2014:：]\s*)?(.*)$", re.I)
TASK_RE = re.compile(r"^\s*-\s*\[([ xX])\]\s+(.+?)\s*$")
PRIORITY_RE = re.compile(r"Priority\s*(\d+)", re.I)


@dataclass
class PhaseBuilder:
    number: int
    title: str
    tasks: list[dict]


def load_source_configs() -> tuple[list[dict], str | None]:
    if not SOURCES_CONFIG_PATH.exists():
        return DEFAULT_SOURCES, f"配置文件不存在：{SOURCES_CONFIG_PATH}"

    try:
        payload = json.loads(SOURCES_CONFIG_PATH.read_text(encoding="utf-8"))
        sources = payload.get("sources", [])
    except Exception as exc:  # noqa: BLE001 - surface local config errors in UI
        return DEFAULT_SOURCES, f"无法读取 sources.json：{exc}"

    normalized = []
    for index, source in enumerate(sources):
        normalized.append(
            {
                "id": str(source.get("id") or f"source-{index + 1}"),
                "name": str(source.get("name") or f"Source {index + 1}"),
                "path": str(source.get("path") or ""),
                "accent": str(source.get("accent") or "#0071e3"),
                "enabled": bool(source.get("enabled", True)),
            }
        )
    return normalized, None


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
    }
    totals["progressFraction"] = fraction(totals["progressCompleted"], totals["progressTotal"])

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
        "progress": {"completed": 0, "open": 0, "total": 0, "fraction": 0},
        "roadmap": {"mode": "none", "tracks": [], "phases": [], "error": None},
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
    parsed["progress"] = progress_summary(parsed["phases"])
    parsed.update({"readable": True, "error": None})
    return {**base, **parsed}


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


class DashboardHandler(SimpleHTTPRequestHandler):
    def do_GET(self) -> None:  # noqa: N802 - stdlib method name
        parsed = urlparse(self.path)
        if parsed.path == "/api/state":
            self.send_dashboard_state()
            return
        if parsed.path == "/":
            self.path = "/index.html"
        super().do_GET()

    def send_dashboard_state(self) -> None:
        try:
            payload = json.dumps(dashboard_state(), ensure_ascii=False).encode("utf-8")
            self.send_response(HTTPStatus.OK)
        except Exception as exc:  # noqa: BLE001 - return useful local error
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
