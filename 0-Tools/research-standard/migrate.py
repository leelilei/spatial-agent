#!/usr/bin/env python3
"""Migrate a project's V1 dashboard files to the V2 unified project.yaml.

Merges `docs/guides/roadmap.yaml` + `docs/guides/project_map.yaml` into a single
`docs/guides/project.yaml`, then moves the two V1 files into
`docs/guides/archive/`. The dashboard reads project.yaml in preference, so the
result renders identically.

Usage:
    python3 migrate.py <project-dir> [--dry-run]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


def phase_extras(project_map: dict) -> tuple[dict, dict]:
    """Map phase number -> completion date (from milestones) and -> next actions."""
    dates: dict[int, str] = {}
    for milestone in project_map.get("milestones", []) or []:
        n = milestone.get("phase")
        if n is not None and milestone.get("date"):
            dates[n] = milestone["date"]
    nexts: dict[int, list] = {}
    for node in project_map.get("mapNodes", []) or []:
        n = node.get("phase")
        if n is not None and node.get("nextActions"):
            nexts[n] = list(node["nextActions"])
    return dates, nexts


def build_project_yaml(roadmap: dict, project_map: dict) -> dict:
    dates, nexts = phase_extras(project_map)
    has_build = any(str(p.get("track")) == "build" for p in roadmap.get("phases", []) or [])
    out: dict = {
        "version": 2,
        "project": project_map.get("project") or roadmap.get("project") or "",
        "type": "empirical" if has_build else "survey",
        "title": project_map.get("title") or roadmap.get("project") or "",
        "researchQuestion": project_map.get("researchQuestion", ""),
        "currentFocus": project_map.get("currentFocus", ""),
        "phases": [],
    }
    for p in roadmap.get("phases", []) or []:
        n = p.get("number")
        # A recorded milestone (done + date) is authoritative: that phase is done,
        # even if a stale roadmap status said otherwise.
        status = "done" if n in dates else p.get("status", "planned")
        phase = {
            "n": n,
            "title": p.get("title"),
            "track": p.get("track", "untracked"),
            "status": status,
            "summary": p.get("summary", ""),
        }
        if n in dates:
            phase["date"] = dates[n]
        if p.get("outputs"):
            phase["outputs"] = list(p["outputs"])
        if n in nexts:
            phase["next"] = nexts[n]
        out["phases"].append(phase)
    if project_map.get("paper"):
        out["paper"] = project_map["paper"]
    return out


def migrate(project_dir: Path, dry_run: bool) -> int:
    guides = project_dir / "docs/guides"
    roadmap_path = guides / "roadmap.yaml"
    map_path = guides / "project_map.yaml"
    out_path = guides / "project.yaml"

    if yaml is None:
        sys.stderr.write("需要 PyYAML 才能迁移。\n")
        return 1
    if out_path.exists():
        sys.stderr.write(f"已存在 {out_path}，跳过。\n")
        return 1
    if not roadmap_path.exists():
        sys.stderr.write(f"找不到 {roadmap_path}，无可迁移内容。\n")
        return 1

    roadmap = yaml.safe_load(roadmap_path.read_text(encoding="utf-8")) or {}
    project_map = (
        yaml.safe_load(map_path.read_text(encoding="utf-8")) or {} if map_path.exists() else {}
    )
    merged = build_project_yaml(roadmap, project_map)
    rendered = yaml.safe_dump(merged, allow_unicode=True, sort_keys=False)

    if dry_run:
        print(f"# 将写入 {out_path}：\n")
        print(rendered)
        return 0

    out_path.write_text(rendered, encoding="utf-8")
    archive = guides / "archive"
    archive.mkdir(exist_ok=True)
    for src in (roadmap_path, map_path):
        if src.exists():
            src.rename(archive / src.name)
    print(f"已生成 {out_path}")
    print(f"已归档 roadmap.yaml / project_map.yaml 到 {archive}/")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Migrate V1 dashboard files to V2 project.yaml.")
    parser.add_argument("project", help="Project directory (containing docs/guides/).")
    parser.add_argument("--dry-run", action="store_true", help="Print the merged project.yaml without writing.")
    args = parser.parse_args(argv or sys.argv[1:])
    return migrate(Path(args.project).expanduser().resolve(), args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
