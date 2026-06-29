#!/usr/bin/env python3
"""Validate provenance and official prompt surfaces for all external adapters."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


BENCHMARK_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = BENCHMARK_ROOT.parents[1]
if str(BENCHMARK_ROOT) not in sys.path:
    sys.path.insert(0, str(BENCHMARK_ROOT))

from external_adapters.adapter_common import (  # noqa: E402
    compile_named_function,
    extract_assigned_string,
    extract_function_string,
    load_json,
    render_official_file_prompt,
    verify_official_checkout,
)


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


def validate_prompt_surface(framework: str, root: Path) -> list[str]:
    checked: list[str] = []
    if framework == "gatsim":
        source = root / "gatsim" / "agent" / "llm_modules" / "llm.py"
        renderer = compile_named_function(source, "generate_prompt")
        template = (
            root
            / "gatsim"
            / "agent"
            / "llm_modules"
            / "prompt_templates"
            / "generate_daily_activity_plan_v1.txt"
        )
        prompt = render_official_file_prompt(renderer, ["x"] * 9, template)
        if not prompt:
            raise RuntimeError("empty GATSim official prompt")
        checked.extend(["generate_prompt", "generate_daily_activity_plan_v1"])
    elif framework == "sotopia":
        source = root / "sotopia" / "generation_utils" / "generate.py"
        fill_template = compile_named_function(source, "fill_template")
        template = extract_function_string(source, "agenerate_action", "Imagine you are {agent}")
        prompt = fill_template(
            template,
            agent="test_agent",
            history="test history",
            turn_number="1",
            action_list="action none leave",
            goal="test goal",
            format_instructions="json",
        )
        if "test_agent" not in prompt or "test history" not in prompt:
            raise RuntimeError("SOTOPIA official action template did not render")
        checked.extend(["LLMAgent.aact", "agenerate_action", "AgentAction"])
    elif framework == "generative-agents":
        prompt_root = root / "reverie" / "backend_server" / "persona" / "prompt_template"
        renderer = compile_named_function(prompt_root / "gpt_structure.py", "generate_prompt")
        prompt = render_official_file_prompt(
            renderer,
            ["identity", "lifestyle", "date", "name", "08:00"],
            prompt_root / "v2" / "daily_planning_v6.txt",
        )
        if "identity" not in prompt or "name" not in prompt:
            raise RuntimeError("Generative Agents official daily prompt did not render")
        checked.extend(["generate_prompt", "daily_planning_v6", "new_decomp_schedule_v1"])
    elif framework == "agentsociety":
        block_root = (
            root
            / "packages"
            / "agentsociety"
            / "agentsociety"
            / "cityagent"
            / "blocks"
        )
        for source_name, variable in [
            ("plan_block.py", "GUIDANCE_SELECTION_PROMPT"),
            ("plan_block.py", "DETAILED_PLAN_PROMPT"),
            ("mobility_block.py", "PLACE_ANALYSIS_PROMPT"),
        ]:
            if not extract_assigned_string(block_root / source_name, variable):
                raise RuntimeError(f"empty AgentSociety prompt: {variable}")
            checked.append(variable)
    return checked


def validate_framework(framework: str, config: dict[str, Any]) -> dict[str, Any]:
    manifest_path = MANIFESTS[framework]
    manifest = load_json(manifest_path)
    root = PROJECT_ROOT / "tmp" / "external" / manifest["checkout_dir"]
    provenance = verify_official_checkout(root, manifest_path)
    config_entry = next(
        (
            item
            for item in config["agents_under_test"]
            if item["id"] == manifest["framework_id"]
        ),
        None,
    )
    if config_entry is None:
        raise RuntimeError(f"missing benchmark config entry for {manifest['framework_id']}")
    expected = {
        "implementation": manifest["integration_level"],
        "source_repo": manifest["source_repo"],
        "source_commit": manifest["source_commit"],
    }
    mismatches = {
        key: {"config": config_entry.get(key), "manifest": value}
        for key, value in expected.items()
        if config_entry.get(key) != value
    }
    if mismatches:
        raise RuntimeError(f"config/manifest mismatch for {framework}: {mismatches}")
    return {
        "framework": manifest["framework_name"],
        "agent_id": manifest["framework_id"],
        "source_commit": provenance["source_commit"],
        "integration_level": provenance["integration_level"],
        "native_backend": provenance["native_backend"],
        "verified_files": len(provenance["verified_files"]),
        "prompt_surfaces": validate_prompt_surface(framework, root),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--framework", choices=["all", *MANIFESTS], default="all")
    args = parser.parse_args()
    requested = list(MANIFESTS) if args.framework == "all" else [args.framework]
    config = load_json(BENCHMARK_ROOT / "benchmark_config.json")
    results = [validate_framework(framework, config) for framework in requested]
    print(json.dumps({"status": "passed", "adapters": results}, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
