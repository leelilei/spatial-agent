from spatial_agent_survey.coding import (
    merge_or_split_recommendation,
    pilot_system_examples,
    system_records_to_rows,
)
from spatial_agent_survey.schemas import AgentAccessibleRepresentation, EnvironmentSideRepresentation


def test_merge_or_split_recommendation_splits_on_representation_change():
    existing = {
        "agent_accessible_representation": "L2",
        "environment_side_representation": "text-only",
        "environment_configuration": "town",
        "behavioral_scale": "interaction",
        "agent_count": "2-10",
    }
    new = dict(existing)
    new["agent_accessible_representation"] = "L3"
    decision, reasons = merge_or_split_recommendation(existing, new)
    assert decision == "split"
    assert "agent_accessible_representation_changed" in reasons


def test_pilot_examples_cover_planned_scenarios():
    pilots = pilot_system_examples()
    assert len(pilots) == 3
    sarah = [row for row in pilots if row.system_name == "SARAH"][0]
    assert sarah.environment_side_representation == EnvironmentSideRepresentation.ENGINE_3D
    assert sarah.agent_accessible_representation != AgentAccessibleRepresentation.L5
    rows = system_records_to_rows(pilots)
    assert rows[0]["paper_refs"]
