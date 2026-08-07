import sys
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
import run_baseline_traces as runner  # noqa: E402


def state():
    return runner.TraceState(
        scenario_id="wave4_test", agent_id="aria", agent_type="oracle",
        time=600, end_time=900, location="home", budget=100,
    )


def test_dwell_within_window_counts_only_overlap():
    value = state()
    value.dwell_records = [
        {"location": "library", "start_time": 610, "end_time": 625, "minutes": 15},
    ]
    condition = {
        "type": "dwell_within_window", "location": "library",
        "time_window": ["10:15", "10:30"], "min_minutes": 10,
    }
    assert runner.condition_success(condition, value, {}) == 1.0
    condition["min_minutes"] = 11
    assert runner.condition_success(condition, value, {}) == 0.0


def test_ordered_service_chain_rejects_reverse_order():
    value = state()
    value.services = [
        {"location": "referral", "service": "referral", "time": 610},
        {"location": "provider", "service": "treatment", "time": 630},
    ]
    condition = {"type": "ordered_service_chain", "steps": [
        {"location": "referral", "service": "referral"},
        {"location": "provider", "service": "treatment"},
    ]}
    assert runner.condition_success(condition, value, {}) == 1.0
    value.services[0]["time"], value.services[1]["time"] = 640, 620
    assert runner.condition_success(condition, value, {}) == 0.0


def test_handoff_requires_purchase_before_interaction():
    value = state()
    value.purchases = [{"location": "market", "item": "parcel", "time": 620}]
    value.interactions = [{
        "with": "ben", "location": "station", "start_time": 640,
        "end_time": 645, "time": 640,
    }]
    condition = {
        "type": "handoff_evidence", "item_location": "market", "item": "parcel",
        "to": "ben", "interaction_location": "station",
    }
    assert runner.condition_success(condition, value, {}) == 1.0
    value.purchases[0]["time"] = 650
    assert runner.condition_success(condition, value, {}) == 0.0


def test_ordered_interaction_chain_rejects_reversed_relay():
    value = state()
    value.interactions = [
        {"with": "ben", "location": "library", "start_time": 620, "end_time": 625},
        {"with": "casey", "location": "office", "start_time": 650, "end_time": 655},
    ]
    condition = {"type": "ordered_interaction_chain", "steps": [
        {"to": "ben", "location": "library"},
        {"to": "casey", "location": "office"},
    ]}
    assert runner.condition_success(condition, value, {}) == 1.0
    value.interactions[0]["start_time"], value.interactions[0]["end_time"] = 660, 665
    value.interactions[1]["start_time"], value.interactions[1]["end_time"] = 640, 645
    assert runner.condition_success(condition, value, {}) == 0.0


def test_service_after_recovery_rejects_pre_recovery_and_late_evidence():
    condition = {
        "type": "service_after_recovery", "location": "clinic",
        "service": "appointment", "after": "10:40", "deadline": "11:30",
    }
    value = state()
    value.services = [{"location": "clinic", "service": "appointment", "time": 640}]
    assert runner.condition_success(condition, value, {}) == 1.0

    # Completed one minute before the outage recovers.
    value.services = [{"location": "clinic", "service": "appointment", "time": 639}]
    assert runner.condition_success(condition, value, {}) == 0.0

    # Recovered, but past the deadline.
    value.services = [{"location": "clinic", "service": "appointment", "time": 691}]
    assert runner.condition_success(condition, value, {}) == 0.0

    # Right service label is required.
    value.services = [{"location": "clinic", "service": "walk_in", "time": 650}]
    assert runner.condition_success(condition, value, {}) == 0.0


def test_service_after_recovery_reports_only_qualifying_evidence():
    condition = {
        "type": "service_after_recovery", "location": "clinic",
        "service": "appointment", "after": "10:40",
    }
    value = state()
    value.services = [
        {"location": "clinic", "service": "appointment", "time": 620},
        {"location": "clinic", "service": "appointment", "time": 660},
    ]
    evidence = runner.condition_evidence(condition, value)
    assert [record["time"] for record in evidence] == [660]


def test_ordered_evidence_chain_supports_mixed_action_types():
    value = state()
    value.services = [
        {"location": "civic", "service": "credential", "time": 610},
        {"location": "clinic", "service": "appointment", "time": 650},
    ]
    value.purchases = [{"location": "market", "item": "permit", "time": 630}]
    condition = {"type": "ordered_evidence_chain", "steps": [
        {"kind": "use_service", "location": "civic", "label": "credential"},
        {"kind": "buy", "location": "market", "label": "permit"},
        {"kind": "use_service", "location": "clinic", "label": "appointment"},
    ]}
    assert runner.condition_success(condition, value, {}) == 1.0
    value.purchases[0]["time"] = 600
    assert runner.condition_success(condition, value, {}) == 0.0
