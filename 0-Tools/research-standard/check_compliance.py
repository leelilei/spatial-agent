#!/usr/bin/env python3
"""Check a research project against RESEARCH-PROJECT-STANDARD.md.

Usage:
    python3 check_compliance.py                 # check all projects under research root
    python3 check_compliance.py <path> [<path>] # check specific project directories
    python3 check_compliance.py --json          # machine-readable output

Compliance levels (each level requires all lower levels to be fully satisfied):
    L0 Minimal      README.md + docs/guides/todolist.md
    L1 Tracked      + docs/guides/roadmap.yaml + docs/plans/proposal.md
    L2 Mapped       + docs/guides/project_map.yaml + docs/project/reference_sources.md
    L3 Paper-ready  + paper/ + docs/project/decisions.md

This module is import-safe: research-dashboard reuses `check_project` to render
the "规范健康度" view.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

DEFAULT_RESEARCH_ROOT = Path(
    os.environ.get("RESEARCH_DASHBOARD_ROOT", "/Users/mac/Documents/6-Research")
)

# Projects that are out of scope for the standard (learning / tooling).
# 2-GAME-AGENT is a beginner "做中学" demo per its own PRD, so treated as learning.
EXCLUDED_DIR_NAMES = {"0-Tools", "0-LLM-learning", "2-GAME-AGENT"}

# Ordered level definitions. Each requirement is (relative_path, is_dir).
LEVELS: list[tuple[str, str, list[tuple[str, bool]]]] = [
    ("L0", "Minimal", [
        ("README.md", False),
        ("docs/guides/todolist.md", False),
    ]),
    ("L1", "Tracked", [
        ("docs/guides/roadmap.yaml", False),
        ("docs/plans/proposal.md|docs/plans/survey_plan.md", False),
    ]),
    ("L2", "Mapped", [
        ("docs/guides/project_map.yaml", False),
        ("docs/project/reference_sources.md", False),
    ]),
    ("L3", "Paper-ready", [
        ("paper", True),
        ("docs/project/decisions.md", False),
    ]),
]


def requirement_met(project_dir: Path, rel_path: str, is_dir: bool) -> bool:
    # rel_path may list alternatives separated by "|" (any one satisfies it),
    # e.g. empirical projects use proposal.md, surveys use survey_plan.md.
    for candidate in rel_path.split("|"):
        target = project_dir / candidate
        if (target.is_dir() if is_dir else target.is_file()):
            return True
    return False


def check_project(project_dir: Path) -> dict:
    """Return a compliance report for a single project directory."""
    project_dir = project_dir.expanduser().resolve()
    levels = []
    achieved = None
    still_qualifies = True  # once a level fails, higher levels cannot be "achieved"

    for code, name, requirements in LEVELS:
        items = [
            {
                "path": rel_path,
                "isDir": is_dir,
                "present": requirement_met(project_dir, rel_path, is_dir),
            }
            for rel_path, is_dir in requirements
        ]
        complete = all(item["present"] for item in items)
        if complete and still_qualifies:
            achieved = code
        else:
            still_qualifies = False
        levels.append({
            "code": code,
            "name": name,
            "complete": complete,
            "items": items,
            "missing": [item["path"] for item in items if not item["present"]],
        })

    # Versioning hygiene: docs/plans should not have multiple loose proposal_v*.md.
    plans_dir = project_dir / "docs/plans"
    stray_versions = []
    if plans_dir.is_dir():
        stray_versions = sorted(
            p.name for p in plans_dir.glob("*.md")
            if p.name != "proposal.md" and "proposal" in p.name.lower()
        )

    return {
        "name": project_dir.name,
        "path": str(project_dir),
        "achievedLevel": achieved,           # None means below L0
        "levels": levels,
        "strayProposalVersions": stray_versions,
    }


def discover_projects(root: Path) -> list[Path]:
    root = root.expanduser().resolve()
    if not root.is_dir():
        return []
    return sorted(
        p for p in root.iterdir()
        if p.is_dir() and not p.name.startswith(".") and p.name not in EXCLUDED_DIR_NAMES
    )


def print_human(reports: list[dict]) -> None:
    for report in reports:
        level = report["achievedLevel"] or "—（未达 L0）"
        print(f"\n{report['name']}  →  {level}")
        for entry in report["levels"]:
            mark = "✓" if entry["complete"] else "✗"
            print(f"  {mark} {entry['code']} {entry['name']}")
            for missing in entry["missing"]:
                print(f"      缺：{missing}")
        if report["strayProposalVersions"]:
            print(f"  ⚠ 散落的 proposal 版本（应移入 archive/）："
                  f"{', '.join(report['strayProposalVersions'])}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check research projects against the standard.")
    parser.add_argument("paths", nargs="*", help="Project directories to check (default: discover all).")
    parser.add_argument("--root", default=str(DEFAULT_RESEARCH_ROOT), help="Research root for discovery.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of human-readable output.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if args.paths:
        projects = [Path(p) for p in args.paths]
    else:
        projects = discover_projects(Path(args.root))

    reports = [check_project(project) for project in projects]

    if args.json:
        print(json.dumps(reports, ensure_ascii=False, indent=2))
    else:
        print_human(reports)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
