import importlib.util
import json
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "v1_1" / "build_calibration_registry.py"
SPEC = importlib.util.spec_from_file_location(
    "cityintent_v1_1_calibration_registry", MODULE_PATH
)
assert SPEC and SPEC.loader
registry_builder = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = registry_builder
SPEC.loader.exec_module(registry_builder)


def test_wave3_registry_separates_calibration_from_release_acceptance():
    registry = registry_builder.build_registry()
    assert registry["status"] == "calibration_template_pool_not_release"
    assert registry["calibration_template_count"] == 24
    assert registry["calibration_public_instance_count"] == 72
    assert registry["release_target"] == 144
    assert registry["release_accepted_count"] == 0
    assert set(
        registry["construction_gap"][
            "calibrated_public_templates_per_construct"
        ].values()
    ) == {3}
    assert set(
        registry["construction_gap"][
            "remaining_public_templates_per_construct"
        ].values()
    ) == {1}
    assert registry["construction_gap"]["next_required_waves"] == ["wave4"]
    assert all(
        len(template["public_instances"]) == 3
        for template in registry["templates"]
    )


def test_wave3_registry_rejects_scenario_hash_drift(tmp_path):
    source = registry_builder.DEFAULT_SOURCES[0][1]
    copied = tmp_path / "scenarios"
    copied.mkdir()
    for path in source.glob("*.json"):
        (copied / path.name).write_bytes(path.read_bytes())
    target = next(copied.glob("*.json"))
    scenario = json.loads(target.read_text(encoding="utf-8"))
    scenario["title"] += " drift"
    target.write_text(json.dumps(scenario), encoding="utf-8")

    with pytest.raises(ValueError, match="scenario hash drift"):
        registry_builder.build_registry(
            ((registry_builder.DEFAULT_SOURCES[0][0], copied),)
            + registry_builder.DEFAULT_SOURCES[1:],
        )
