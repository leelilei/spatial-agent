"""Create separate blinded handoff archives for CityIntent human annotators."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path
from typing import Any


BENCHMARK_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = BENCHMARK_ROOT.parents[2]
DEFAULT_AUDIT_DIR = (
    REPO_ROOT
    / "6-city"
    / "annotation"
    / "cityintent_v1_rc1_blind_validation_2026-07-02"
)


COMMON_FILES = [
    "RUBRIC.md",
    "blinded/audit_items.jsonl",
    "blinded/audit_packet.md",
    "blinded/world_reference.json",
]


def binary_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(value, f, indent=2, ensure_ascii=False)
        f.write("\n")


def build_handoffs(audit_dir: Path, output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    archives = []
    for annotator in ("annotator_a", "annotator_b"):
        relative_files = [*COMMON_FILES, f"annotations/{annotator}.csv"]
        missing = [relative for relative in relative_files if not (audit_dir / relative).exists()]
        if missing:
            raise FileNotFoundError(f"missing handoff files for {annotator}: {missing}")
        archive = output_dir / f"{annotator}_blinded_handoff.zip"
        with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as zf:
            for relative in relative_files:
                zf.write(audit_dir / relative, arcname=relative)
        with zipfile.ZipFile(archive) as zf:
            members = set(zf.namelist())
        if any(member.startswith("sealed/") for member in members):
            raise RuntimeError(f"sealed material leaked into {archive}")
        other = "annotator_b.csv" if annotator == "annotator_a" else "annotator_a.csv"
        if any(member.endswith(other) for member in members):
            raise RuntimeError(f"other annotator file leaked into {archive}")
        archives.append(
            {
                "annotator": annotator,
                "archive": archive.name,
                "sha256": binary_sha256(archive),
                "members": sorted(members),
            }
        )
    manifest = {
        "schema_version": "cityintent_human_handoff_v1",
        "audit_dir": str(audit_dir),
        "archives": archives,
        "sealed_material_included": False,
    }
    write_json(output_dir / "handoff_manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--audit-dir", type=Path, default=DEFAULT_AUDIT_DIR)
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    output_dir = args.output_dir or args.audit_dir / "handoff"
    manifest = build_handoffs(args.audit_dir, output_dir)
    print(f"Wrote {len(manifest['archives'])} blinded handoff archives to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
