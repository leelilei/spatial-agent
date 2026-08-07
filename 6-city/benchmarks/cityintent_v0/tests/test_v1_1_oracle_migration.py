import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "v1_1" / "verify_available_oracles.py"
SPEC = importlib.util.spec_from_file_location("cityintent_v1_1_verify_oracles", MODULE_PATH)
assert SPEC and SPEC.loader
oracles = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = oracles
SPEC.loader.exec_module(oracles)


def test_available_oracle_migration_produces_real_evidence():
    report = oracles.verify(ROOT / "v1_1")
    assert report["scenario_count"] > 0
    assert report["oracle_pass_count"] > 0
    assert report["negative_control_available_count"] > 0
