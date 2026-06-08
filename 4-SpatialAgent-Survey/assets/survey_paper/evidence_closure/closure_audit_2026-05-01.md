# Evidence Closure Audit

Date: 2026-05-01

Scope: stable widened-Core evidence map used by the current manuscript draft.

Source table: `spatial-agent-survey/paper/appendix/appendix_evidence_table.csv`

Markdown bundle: `assets/survey_paper/pdfs/phase1_stable_widened_core_markdown/`

Archive manifest: `assets/survey_paper/evidence_closure/pdf_markdown_archive_manifest_2026-05-01.md`

PDF acquisition log: `assets/survey_paper/evidence_closure/core_pdf_acquisition_log_2026-05-01.md`

Remaining route check: `assets/survey_paper/evidence_closure/pdf_gap_route_check_2026-05-01.md`

## Current Gate Result

The manuscript body can remain as a paragraph-level scaffold, but it should not be treated as final until the evidence closure gate is resolved.

- Stable widened-Core rows: `34`
- `anchor_core`: `19` rows
- `bridge_core`: `15` rows
- Rows with local PDF as primary artifact: `33 / 34`
- Rows with markdown/source-note primary artifact: `1 / 34`
- Rows with PDF-derived or archived full-text markdown available: `33 / 34`
- Local PDF library conversion: `62 / 62` PDFs have paired `.fulltext.md` and `.meta.json`
- Legacy PDF library conversion: `32 / 33` PDFs have paired `.fulltext.md` and `.meta.json`; the remaining file is an HTML download challenge saved with a `.pdf` extension.
- Rows with a markdown dossier in the stable widened-Core bundle: `34 / 34`
- Closure-card status after bridge batch: `33 / 34` rows are `C3 closed_card_done`.
- Remaining unresolved Core row: `BK02` remains `C0 acquire_or_downgrade` until a full text is acquired or the row is downgraded.
- Important caveat: the markdown dossier is not always a full-text conversion. Files ending in `.source.md` are source notes, not full-text transcriptions.

## Closure Status Legend

| Status | Meaning | Required before final manuscript |
|---|---|---|
| `C0 acquire_or_downgrade` | No local PDF or full-text artifact sufficient for final Core use. Usually source-note-only, missing PDF, or not acquired. | Acquire PDF/full text, or downgrade/exclude/mark as lower-confidence bridge evidence. |
| `C1 needs_fulltext_card` | Local PDF or full-text markdown exists, but no standardized closure card has yet verified representation, behavior, evidence status, and claim boundary. | Read/verify and write a closure card. |
| `C2 provisionally_closed` | Full-text or adjudication basis is already strong enough for the current coding, though a short card may still be useful for traceability. | Optional card or final spot-check. |
| `C3 closed_card_done` | Standardized closure card exists and the row is ready for manuscript use, subject to later global consistency checks. | No immediate action. |

## Row-by-Row Audit

| ID | Layer | Current artifact | Source basis | Closure status | Next action |
|---|---|---|---|---|---|
| `HC02` | anchor | PDF + full-text markdown bundle | `local_pdf_and_reading_note` | `C3 closed_card_done` | Done in `cards/HC02_Generative_Agents.md`; keep as `L3 / designed_affordance_only` for spatial-effect claim. |
| `HC03A` | anchor | PDF + OCR/adjudication | `local_pdf_ocr_and_adjudication_memo` | `C3 closed_card_done` | Done in `cards/HC03A_HC03B_Concordia.md`; keep Riverbend split as `L3`. |
| `HC03B` | anchor | PDF + OCR/adjudication | `local_pdf_ocr_and_adjudication_memo` | `C3 closed_card_done` | Done in `cards/HC03A_HC03B_Concordia.md`; keep phone-calendar split as `L1`. |
| `HC04` | anchor | PDF + full-text markdown bundle | `local_pdf_and_reading_note` | `C3 closed_card_done` | Done in `cards/HC04_Affordable_Generative_Agents.md`; keep social-simulation row as inherited `L3` town interface. |
| `HC05` | anchor | PDF + full-text markdown bundle | `local_pdf_and_reading_note` | `C3 closed_card_done` | Done in `cards/HC05_Artificial_Leviathan.md`; likely recode from `L3` to `L2` or mark as weak/boundary spatial environment. |
| `HC06` | anchor | PDF + OCR/read note | `local_pdf_ocr_and_reading_note` | `C3 closed_card_done` | Done in `cards/HC06_Project_Sid.md`; keep `L5`, but consider upgrading evidence status to limited `observed_effect`. |
| `HC07` | anchor | PDF + boundary note | `local_pdf_and_boundary_note` | `C3 closed_card_done` | Done in `cards/HC07_OASIS.md`; keep `L3 / observed_effect`, not `L4`. |
| `HC08` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC08_Lyfe_Agents.md`; keep `3D_engine / L3 / designed_affordance_only` because the agent-facing interface is local/proximity/language-mediated. |
| `HC09` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC09_Spontaneous_Emergence.md`; keep `2D_grid / L3 / observed_effect` for local-neighborhood message-range effects. |
| `HC10` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC10_Real_World_Community_Oriented.md`; keep `3D_engine / L3 / observed_effect`, separating Unreal backend from categorical agent observations. |
| `HC12A` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC12A_HC12B_SimWorld.md`; keep split row as `3D_engine / L5` for visual-GPS embodied interface. |
| `HC12B` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC12A_HC12B_SimWorld.md`; keep split row as `3D_engine / L3` for scene-graph/abstract-layout interface. |
| `HC13` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC13_Fire_Evacuation_CA.md`; keep `2D_grid / L3 / observed_effect`, not direct-geometry `L5`. |
| `HC14` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC14_Crowd_Evacuation_Disaster.md`; keep `graph_based / L3 / observed_effect` for GIS road-network evacuation. |
| `HC15` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC15_CitySim.md`; keep `graph_based / L3 / observed_effect` for POI/place-level urban simulation. |
| `R3-01` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/R3-01_MineLand.md`; keep `3D_engine / L5 / observed_effect` for embodied multimodal Minecraft interface. |
| `R3-02` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/R3-02_GATSim.md`; keep `graph_based / L3 / observed_effect` for transport network and spatial-temporal memory. |
| `R3-04` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/R3-04_LLM_Epidemic_Economic_Dynamics.md`; keep `2D_grid / L3 / observed_effect` for local contact/proximity ABM. |
| `BK01` | anchor | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/BK01_AgentSociety.md`; keep `graph_based / L3`, with observed simulator outcomes but conservative spatial-representation claims. |
| `HC11` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/HC11_Environment_Aware_VR_Roleplay.md`; keep `3D_engine / L2`, with coordinate fields treated as structured text-schema evidence rather than embodied geometry. |
| `BK02` | bridge | source note + local note | `local_note_reviewed` | `C0 acquire_or_downgrade` | Acquire full text if retained as bridge evidence; otherwise keep only as Adjacent motivation. |
| `BK03` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/BK03_Context_Aware_Onboarding_Metaverse.md`; keep `3D_engine / L2 / observed_effect` for context-aware onboarding assistance. |
| `BK04` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/BK04_NPC_Interaction.md`; keep `3D_engine / L2` because the LLM maps speech to predefined dialogue options. |
| `BK05` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/BK05_Forum_Theatre_Training.md`; keep `3D_engine / L2` for VR training dialogue state, not spatial representation. |
| `BK06` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/BK06_TongSIM.md`; keep `3D_engine / L5` but retain bridge/platform caveat. |
| `BK07` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/BK07_S3_Social_Network_Simulation.md`; keep `graph_based / L3`, not `L4`, because global graph metrics are not agent-facing. |
| `BK08` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/BK08_Chirper_Online_Community.md`; keep `graph_based / L3`, separating Chirper platform interactions from researcher-side SNA. |
| `R3-03` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/R3-03_Cognitive_Agents_Urban_Mobility.md`; keep `graph_based / L3 / observed_effect` for urban mobility adaptation. |
| `R3-05` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/R3-05_CoELA.md`; keep `3D_engine / L5 / observed_effect` with the paper's own limitation about incomplete 3D spatial reasoning. |
| `L4R-01` | bridge | PDF + full-text from legacy archive | `local_pdf_and_fulltext_from_legacy_archive` | `C3 closed_card_done` | Done in `cards/L4R-01_Network_Formation_Multi_LLMs.md`; keep as the only widened-bridge `L4` row, not an anchor-core spatial case. |
| `TW-09` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/TW-09_ELLMA-T_Social_VR.md`; keep `3D_engine / L2` for role-play scene/context prompting in VRChat. |
| `TW-11` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/TW-11_Office_Whispers_GenAI_NPCs.md`; keep `3D_engine / L2 / observed_effect`, noting participant-reported context-awareness limits. |
| `TW-13` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/TW-13_TUMSphere.md`; keep `3D_engine / L5 / observed_effect` for NavMesh/object-location integrated VR guidance. |
| `TW-12` | bridge | PDF + PDF-derived full text | `local_pdf_fulltext_closure_card` | `C3 closed_card_done` | Done in `cards/TW-12_Virtual_Tutoring_System.md`; keep `3D_engine / L2 / observed_effect` for situated educational NPC interaction. |

## Immediate Work Order

1. Resolve the remaining PDF gap through institutional access or author-copy request: `BK02`.
2. Use `assets/survey_paper/evidence_closure/global_consistency_check_2026-05-01.md` as the global claim-boundary checkpoint.
3. Resume manuscript drafting with closure cards and the global consistency memo as the source of truth.
