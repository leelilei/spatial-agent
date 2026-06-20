#!/usr/bin/env python3
"""Scaffold a standard-compliant research project skeleton.

Usage:
    python3 scaffold.py <project-name> [--type empirical|survey] [--root PATH] [--force]

Creates the standard directory layout and fills templates from templates/,
substituting {{PROJECT_NAME}} and {{DATE}}. Existing files are never overwritten
unless --force is passed.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = SCRIPT_DIR / "templates"
DEFAULT_ROOT = Path("/Users/mac/Documents/6-Research")

# Directories to create for every project.
COMMON_DIRS = [
    "docs/guides",
    "docs/plans/archive",
    "docs/project",
    "docs/background",
    "docs/experiments",
    "docs/reviews",
    "assets/papers",
    "assets/papers/metadata",
    "assets/papers/pdf",
    "assets/papers/fulltext",
    "assets/papers/notes",
]

# (template_filename, destination_relative_path)
COMMON_FILES = [
    ("README.template.md", "README.md"),
    ("todolist.template.md", "docs/guides/todolist.md"),
    ("roadmap.template.yaml", "docs/guides/roadmap.yaml"),
    ("project_map.template.yaml", "docs/guides/project_map.yaml"),
    ("proposal.template.md", "docs/plans/proposal.md"),
    ("reference_sources.template.md", "docs/project/reference_sources.md"),
    ("decisions.template.md", "docs/project/decisions.md"),
]

EMPIRICAL_DIRS = ["src", "scripts", "configs", "data", "results", "tests"]


def render(template_name: str, project_name: str) -> str:
    text = (TEMPLATES_DIR / template_name).read_text(encoding="utf-8")
    return text.replace("{{PROJECT_NAME}}", project_name).replace(
        "{{DATE}}", date.today().isoformat()
    )


def write_file(path: Path, content: str, force: bool, created: list[str], skipped: list[str]) -> None:
    if path.exists() and not force:
        skipped.append(str(path))
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    created.append(str(path))


def scaffold(name: str, root: Path, project_type: str, force: bool) -> dict:
    project_dir = (root / name).expanduser().resolve()
    created: list[str] = []
    skipped: list[str] = []

    dirs = list(COMMON_DIRS)
    code_pkg = f"{name}-core"
    if project_type == "empirical":
        dirs += [f"{code_pkg}/{sub}" for sub in EMPIRICAL_DIRS]
        dirs += ["paper"]
    for rel in dirs:
        (project_dir / rel).mkdir(parents=True, exist_ok=True)

    for template_name, rel_dest in COMMON_FILES:
        write_file(project_dir / rel_dest, render(template_name, name), force, created, skipped)

    return {"projectDir": str(project_dir), "created": created, "skipped": skipped}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scaffold a standard research project.")
    parser.add_argument("name", help="Project directory name, e.g. 6-MyProject.")
    parser.add_argument("--type", choices=["empirical", "survey"], default="empirical")
    parser.add_argument("--root", default=str(DEFAULT_ROOT), help="Research root directory.")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    if not TEMPLATES_DIR.is_dir():
        sys.stderr.write(f"Templates directory not found: {TEMPLATES_DIR}\n")
        return 1
    result = scaffold(args.name, Path(args.root), args.type, args.force)
    print(f"Scaffolded at {result['projectDir']}")
    for path in result["created"]:
        print(f"  + {path}")
    for path in result["skipped"]:
        print(f"  · skipped (exists): {path}")
    print("\nNext: edit docs/guides/todolist.md and docs/plans/proposal.md, then run")
    print(f"  python3 {SCRIPT_DIR / 'check_compliance.py'} {result['projectDir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
