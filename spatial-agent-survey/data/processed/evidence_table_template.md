# Evidence Table Template

This markdown file is the human-readable contract for the CSV templates in this folder.

## Primary Files

- `systems_master_template.csv`
- `core_evidence_template.csv`
- `adjacent_evidence_template.csv`

## Required System-Level Fields

The following fields are mandatory for both `systems_master` and `core_evidence`:

- `system_name`
- `system_family`
- `paper_refs`
- `agent_count`
- `environment_side_representation`
- `agent_accessible_representation`
- `representation_gap_note`
- `behavioral_scale`
- `behavior_type`
- `evidence_status`
- `spatial_behavior_coupling`
- `evaluation_method`
- `space_syntax_construct`

## Encoding Rules

- Unit of analysis is `system / environment configuration`, not raw paper count.
- `paper_refs` may contain multiple citations for one `system_family`.
- `environment_side_representation` captures backend environment structure.
- `agent_accessible_representation` captures what the agent actually receives.
- `representation_gap_note` is required whenever backend structure is richer than agent input.
- `behavioral_scale` must distinguish `local_action`, `interaction`, and `emergent_social_structure`.
- `evidence_status` must follow `claim_matrix.md` language limits.

## Phase 0 Readiness Use

Phase 0 is considered ready only when:

- the CSV templates above exist and match the required schema,
- the coding rules are aligned with `docs/plans/coding_manual.md`,
- the pilot systems can be entered without adding ad hoc columns,
- the resulting evidence exports remain compatible with `scripts/export_evidence_assets.py`.
