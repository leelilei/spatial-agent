#!/usr/bin/env python3
"""Build a leak-checked public CityIntent v1.1 candidate archive."""

from __future__ import annotations

import argparse
import json
import shutil
import tarfile
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
V0_ROOT = ROOT.parent


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def copy_file(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def private_tokens() -> set[str]:
    tokens = set()
    for path in (ROOT / "worlds" / "private").glob("*.json"):
        world = load_json(path)
        tokens.add(world["world_id"])
        tokens.update(location["id"] for location in world["locations"])
    internal = ROOT / "internal" / "private_world_specs.json"
    if internal.exists():
        for item in load_json(internal):
            tokens.update((item["world_id"], str(item["seed"])))
    return {token for token in tokens if token}


def build_archive(output: Path) -> Path:
    with tempfile.TemporaryDirectory(prefix="cityintent-public-") as temp_dir:
        package = Path(temp_dir) / "cityintent-1.1.0-candidate"
        for filename in ("README.md", "release_spec.json", "BENCHMARK_CARD.md", "CHANGELOG.md", "generate_worlds.py", "generate_scenarios.py"):
            copy_file(ROOT / filename, package / filename)
        copy_file(ROOT / "benchmark_config.public.json", package / "benchmark_config.json")
        for path in (ROOT / "worlds" / "public").glob("*.json"):
            copy_file(path, package / "worlds" / "public" / path.name)
        for split in ("examples", "development", "public_test"):
            for path in (ROOT / "scenarios" / split).glob("*.json"):
                copy_file(path, package / "scenarios" / split / path.name)
        for path in (ROOT / "submission").glob("*.json"):
            copy_file(path, package / "submission" / path.name)
        copy_file(ROOT / "submission" / "score_submission.py", package / "submission" / "score_submission.py")
        copy_file(V0_ROOT / "tools" / "run_baseline_traces.py", package / "submission" / "_runtime" / "run_baseline_traces.py")
        copy_file(V0_ROOT / "tools" / "validate_cityintent_v0.py", package / "tools" / "validate_cityintent_v0.py")
        copy_file(V0_ROOT / "worlds" / "micro_city.json", package / "templates" / "worlds" / "micro_city.json")
        for path in (V0_ROOT / "scenarios").glob("*.json"):
            copy_file(path, package / "templates" / "scenarios" / path.name)

        world_manifest = load_json(ROOT / "manifests" / "worlds_manifest.json")
        world_manifest["worlds"] = [item for item in world_manifest["worlds"] if item["visibility"] == "public"]
        world_manifest["world_count"] = len(world_manifest["worlds"])
        scenario_manifest = load_json(ROOT / "manifests" / "scenarios_manifest.json")
        scenario_manifest["scenarios"] = [item for item in scenario_manifest["scenarios"] if item["split"] != "private_test"]
        scenario_manifest["candidate_count"] = len(scenario_manifest["scenarios"])
        scenario_manifest["split_counts"].pop("private_test", None)
        scenario_manifest["split_hashes"].pop("private_test", None)
        scenario_manifest["construct_counts"] = dict(sorted(Counter(item["construct_family"] for item in scenario_manifest["scenarios"]).items()))
        scenario_manifest["difficulty_counts"] = dict(sorted(Counter(item["difficulty_tier"] for item in scenario_manifest["scenarios"]).items()))
        (package / "manifests").mkdir(parents=True, exist_ok=True)
        (package / "manifests" / "worlds_manifest.json").write_text(json.dumps(world_manifest, indent=2) + "\n", encoding="utf-8")
        (package / "manifests" / "scenarios_manifest.json").write_text(json.dumps(scenario_manifest, indent=2) + "\n", encoding="utf-8")

        forbidden = private_tokens()
        leaks = []
        for path in package.rglob("*"):
            if path.is_file():
                text = path.read_text(encoding="utf-8")
                hits = sorted(token for token in forbidden if token in text)
                if hits:
                    leaks.append({"path": str(path.relative_to(package)), "tokens": hits})
        if leaks:
            raise RuntimeError(f"private asset leak detected: {leaks}")

        output.parent.mkdir(parents=True, exist_ok=True)
        with tarfile.open(output, "w:gz") as archive:
            archive.add(package, arcname=package.name)
    return output


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=V0_ROOT.parents[2] / "dist" / "cityintent-1.1.0-candidate-public.tar.gz")
    args = parser.parse_args()
    output = build_archive(args.output.resolve())
    print(json.dumps({"archive": str(output), "bytes": output.stat().st_size}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
