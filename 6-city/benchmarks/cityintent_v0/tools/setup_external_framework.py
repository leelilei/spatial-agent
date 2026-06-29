#!/usr/bin/env python3
"""Create and verify pinned sparse checkouts for external agent frameworks."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any


BENCHMARK_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = BENCHMARK_ROOT.parents[1]
MANIFESTS = {
    "gatsim": BENCHMARK_ROOT / "external_adapters" / "gatsim_manifest.json",
    "sotopia": BENCHMARK_ROOT / "external_adapters" / "sotopia_manifest.json",
    "generative-agents": BENCHMARK_ROOT
    / "external_adapters"
    / "generative_agents_manifest.json",
    "agentsociety": BENCHMARK_ROOT
    / "external_adapters"
    / "agentsociety_manifest.json",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def run(*args: str, cwd: Path | None = None) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def output(*args: str, cwd: Path | None = None) -> str:
    return subprocess.check_output(args, cwd=cwd, text=True, encoding="utf-8").strip()


def setup_framework(
    framework: str, target: Path, verify_only: bool = False
) -> dict[str, Any]:
    manifest_path = MANIFESTS[framework]
    manifest = load_json(manifest_path)
    if not (target / ".git").exists():
        if verify_only:
            raise SystemExit(f"missing {manifest['framework_name']} checkout: {target}")
        target.mkdir(parents=True, exist_ok=True)
        run("git", "init", cwd=target)
        run("git", "remote", "add", "origin", manifest["source_repo"], cwd=target)
        run("git", "config", "core.sparseCheckout", "true", cwd=target)
        sparse_file = target / ".git" / "info" / "sparse-checkout"
        sparse_file.write_text(
            "\n".join(f"/{path}" for path in manifest["sparse_paths"]) + "\n",
            encoding="ascii",
        )
        run(
            "git",
            "fetch",
            "--depth",
            "1",
            "--filter=blob:none",
            "origin",
            manifest["source_commit"],
            cwd=target,
        )
        run("git", "checkout", "--detach", "FETCH_HEAD", cwd=target)

    if str(BENCHMARK_ROOT) not in __import__("sys").path:
        __import__("sys").path.insert(0, str(BENCHMARK_ROOT))
    from external_adapters.adapter_common import verify_official_checkout

    verified = verify_official_checkout(target, manifest_path)
    return {
        "framework": manifest["framework_name"],
        "target": str(target.resolve()),
        **verified,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--framework", choices=sorted(MANIFESTS), required=True)
    parser.add_argument("--target", type=Path, default=None)
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    manifest = load_json(MANIFESTS[args.framework])
    target = args.target or (
        PROJECT_ROOT / "tmp" / "external" / manifest["checkout_dir"]
    )
    result = setup_framework(args.framework, target, verify_only=args.verify_only)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
