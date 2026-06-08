# HC01 TravelAgent Full-Text Adjudication

Date: 2026-04-27

Purpose: close the HC01 acquisition blocker and decide whether the newly archived full text supports stable Core evidence-map coding.

## Acquisition Result

- Source file supplied by user: `/Users/mac/Documents/6-Research/2412.18985v1 (1).pdf`
- Archived file: `assets/survey_paper/pdfs/phase1_core/00_HC01_TravelAgent_Noyman2025.pdf`
- File check: valid PDF header, 20 MB, 21 pages
- Local extraction: `pdfplumber` text extraction succeeded

The archived PDF is the arXiv preprint version dated 2024-12-30. It matches the HC01 title and author team:

- Title: `TravelAgent: Generative agents in the built environment`
- Authors: Ariel Noyman, Kai Hu, Kent Larson

## Full-Text Evidence

### Spatial Representation

TravelAgent is a strong spatial-interface case.

The method section describes:

- a rudimentary 3D environment
- pedestrian-level visual observations generated from 3D models
- image segmentation and object detection
- depth and collision information from ray casting
- a discovery map showing current location, orientation, and previously explored areas
- a compass-like cue in some scenarios
- compressed textual spatial memory containing visited locations, observed objects, and navigational cues

Coding implication:

- `environment_side_representation = 3D_engine`
- `agent_accessible_representation = L5`

Reason:

The agent-facing interface goes beyond place labels or local adjacency. It includes first-person visual input plus metric depth/collision constraints and map/orientation aids. This meets the manual threshold for geometry- or physical-constraint-bearing information.

### Behavioral Evidence

The paper reports observed spatial behavior:

- 100 simulations
- 1,898 agent steps
- about 76% task completion
- navigation, wayfinding, free exploration, and commute-style tasks
- spatial path analysis, term/topic analysis of observation and planning streams, and sentiment analysis

Coding implication:

- `behavioral_scale = local_action`
- `behavior_type = mobility; other`
- `evidence_status = observed_effect`
- `spatial_behavior_coupling = explicit`
- `evaluation_method = mixed`

Reason:

The reported outcomes directly connect spatial cues, visibility, obstacles, routes, and agent navigation decisions. The evidence is stronger than designed affordance only.

### Core Boundary Problem

The full text does not support stable Core social-behavior coding under the current manual.

Key boundary facts:

- The current experiments simulate one agent per run rather than simultaneous multi-agent interaction.
- The analyzed behavior is primarily pedestrian navigation, wayfinding, search, and local spatial adaptation.
- Agent-to-agent communication, group dynamics, crowd movement, and social dynamics are presented as future work rather than current evidence.

Coding implication:

- Do not use HC01 to support strong Core claims about spatial representation shaping multi-agent social behavior.
- Treat HC01 as Adjacent/boundary evidence unless the review scope is explicitly broadened to include single-agent spatially aware systems as Core.

## Final Ruling

Recommended tier after full-text review:

- `Adjacent`

Recommended use:

- Keep as a high-value built-environment boundary case.
- Use it in feasibility and representation-interface discussion.
- Do not count it as stable Core evidence for social emergence, cooperation, norm formation, or multi-agent interaction.

## Suggested Coding Row

```csv
system_name,environment_configuration,system_family,paper_refs,year,agent_count,environment_side_representation,agent_accessible_representation,representation_gap_note,behavioral_scale,behavior_type,evidence_status,spatial_behavior_coupling,evaluation_method,space_syntax_construct,notes
TravelAgent: Generative agents in the built environment,built-environment pedestrian navigation and wayfinding,TravelAgent,Noyman2025,2025,1,3D_engine,L5,The backend 3D environment is converted into first-person visual observations plus segmentation depth collision discovery-map compass and textual spatial memory; this is rich spatial input but not multi-agent social evidence.,local_action,mobility; other,observed_effect,explicit,mixed,none,Full-text reviewed on 2026-04-27. Use as adjacent boundary evidence because current experiments are single-agent navigation rather than multi-agent social simulation.
```

## Follow-Up

- HC01 acquisition blocker is closed.
- HC13 and HC14 were subsequently resolved by local full-text extraction and conservative first-pass coding on 2026-04-27.
- If the paper later has a journal version with materially different multi-agent experiments, reopen adjudication against that version.
