# HC13 and HC14 Full-Text Adjudication

Date: 2026-04-27

Purpose: close the remaining Core acquisition blockers and record the most conservative stable reading supported by the newly archived PDFs and the new local `pdf2text` workflow.

## Acquisition Result

- Source files supplied by user:
  - `1-s2.0-S0925753525001602-main.pdf`
  - `1-s2.0-S0951832025012554-main.pdf`
- Archived files:
  - `assets/survey_paper/pdfs/phase1_core/14_HC13_Fire_Evacuation_CA.pdf`
  - `assets/survey_paper/pdfs/phase1_core/15_HC14_Crowd_Evacuation_Disaster.pdf`
- File check:
  - both files have valid PDF headers
  - `HC13` archive size: `7,115,767` bytes
  - `HC14` archive size: `27,875,701` bytes

## Full-Text Extraction Result

Local extraction now succeeds with:

- `spatial-agent-survey/scripts/pdf2text.py`
- backend: `pdfplumber` with `pypdf` metadata and outline support

Generated artifacts:

- `assets/survey_paper/pdfs/phase1_core/14_HC13_Fire_Evacuation_CA.fulltext.md`
- `assets/survey_paper/pdfs/phase1_core/14_HC13_Fire_Evacuation_CA.meta.json`
- `assets/survey_paper/pdfs/phase1_core/15_HC14_Crowd_Evacuation_Disaster.fulltext.md`
- `assets/survey_paper/pdfs/phase1_core/15_HC14_Crowd_Evacuation_Disaster.meta.json`

Extraction summary:

- `HC13`: `13` pages, about `70,097` extracted characters, status `ok`
- `HC14`: `17` pages, about `77,213` extracted characters, status `ok`

This is sufficient for conservative method-level adjudication and stable first-pass coding.

## HC13

Metadata confirmed from the archived PDF:

- Title: `Large-language-model-driven agents for fire evacuation simulation in a cellular automata environment`
- DOI: `10.1016/j.ssci.2025.106935`
- Journal: `Safety Science, 191 (2025) 106935`
- Author metadata: `Pei Dang`
- Keywords: `Large language model`, `Fire evacuation`, `Multi agent`, `Cellular automata`

Method and result evidence confirmed from local full text:

- the experiment uses `10` agents in a shopping-mall fire evacuation scenario
- the environment is represented through a spatial-semantic cellular approach with a `2D` automaton, height-aware cell semantics, and directional text prompts sent to the LLM
- the physical scene is built from LiDAR scans and `3D` reconstruction, then converted into a `502 x 206` cellular grid with manually added spatial semantics
- agents maintain short-term and long-term memory and can communicate with nearby agents within `3.6 m`
- the paper reports evacuation distance, evacuation time, decision changes, smoke-cell traversal, and communication behaviors rather than stopping at designed affordance only

Coding ruling:

- keep `HC13` in `Core`
- `agent_count = 2-10`
- `environment_side_representation = 2D_grid`
- `agent_accessible_representation = L3`
- `behavioral_scale = mixed`
- `evidence_status = observed_effect`

Reason:

The paper clearly combines a spatially explicit evacuation environment, LLM-driven decision-making, and observed multi-agent outcomes. But the agent-facing interface is still text rendered from the cellular model rather than direct geometry, so `L5` would overclaim the representation level.

## HC14

Metadata confirmed from the archived PDF:

- Title: `When agents learn to think: Large language model-enhanced agent-based modeling for crowd evacuation in disaster scenarios`
- DOI: `10.1016/j.ress.2025.112056`
- Journal: `Reliability Engineering and System Safety, 269 (2026) 112056`
- Author metadata: `Sen Yang`
- Keywords: `Large language models`, `Agent-based modeling`, `Crowd evacuation`, `Disaster response`, `Resilience`

Method and result evidence confirmed from local full text:

- the case study covers about `84%` of residential Arahama, with an estimated population of approximately `2271` residents
- each agent prompt includes personal attributes, current location, hazard conditions, nearby communications, road status, and memory of prior decisions
- the movement environment is a GIS-derived road network with road width, speed, intersection, pedestrian-density, and vehicle-dynamics logic
- the framework explicitly supports both pedestrian and vehicular evacuation, batch prompting, and parallel LLM requests
- the paper reports emergent information dissemination, spontaneous assistance, detouring around congestion, comparison with a conventional ABM baseline, and validation against reported casualty ranges

Coding ruling:

- keep `HC14` in `Core`
- `agent_count = 100+`
- `environment_side_representation = graph_based`
- `agent_accessible_representation = L3`
- `behavioral_scale = mixed`
- `evidence_status = observed_effect`

Reason:

The PDF confirms a substantive full methodology and evaluation pipeline, and the environment-side model is now clear enough to code conservatively as GIS road-network or graph-based. But the LLM still receives textualized state and communication context rather than direct geometry, so the stable reading remains `L3`, not `L5`.

## Final Ruling

- `HC13` and `HC14` are no longer acquisition blockers
- both papers remain stable `Core` items under the current review scope
- both can now be used in stable first-pass coding and evidence-completeness accounting
- neither paper should be used to strengthen `L5` or strong direct-geometry claims

## Follow-Through Completed

- the seed, coding-queue, sanity-check, and first-pass coding files were updated in this pass to reflect the new full-text status
- the stable Core first-pass table now contains `16` coded rows after adding `HC13` and `HC14`
- the local `pdf2text` workflow is now the default path for the next full-text acquisition pass instead of ad hoc PDF extraction
