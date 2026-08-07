import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "v1_1" / "audit_candidates.py"
SPEC = importlib.util.spec_from_file_location("cityintent_v1_1_audit_candidates", MODULE_PATH)
assert SPEC and SPEC.loader
candidate_audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = candidate_audit
SPEC.loader.exec_module(candidate_audit)


def test_candidate_audit_detects_no_split_or_private_asset_leakage():
    report = candidate_audit.audit(ROOT / "v1_1")
    assert report["machine_audit_passed"] is True
    assert report["candidate_count"] == 144
    assert report["private_leakage_count"] == 0
    assert report["accepted_count"] == 0
    assert report["reason_counts"]["oracle_not_run"] == 144
