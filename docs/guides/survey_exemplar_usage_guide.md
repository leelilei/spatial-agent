# Survey Exemplar Usage Guide

Date: 2026-04-28

Purpose: explain how to use the local review-library papers and a small set of added method references when drafting the SpatialAgent survey. This is a writing, figure, and structure guide, not a new Phase 1 screening protocol.

Primary local source folder:

- `assets/survey_paper/pdfs/review_library/`

Current decision:

- The topic-review library is sufficient for drafting.
- Supplement the library with method/reporting references and two computing/AI/HCI-style scoping review exemplars.
- Do not start another broad background-survey search unless a specific manuscript section lacks support.

## 1. Minimal Reference Supplement

Add these references to the bibliography or review-library README. They are method/reporting references and writing exemplars; they do not enter Phase 1 article screening.

| Priority | Reference | Use in this survey | Archive status |
|---|---|---|---|
| P0 | Tricco et al. (2018), `PRISMA Extension for Scoping Reviews (PRISMA-ScR): Checklist and Explanation`, DOI `10.7326/M18-0850` | Reporting checklist, methods wording, PRISMA-ScR compliance | local PDF |
| P0 | Peters et al. (2024), JBI Manual chapter `Scoping Reviews`, DOI `10.46658/JBIMES-24-09` | Protocol design, PCC framing, charting, reporting evidence | local PDF |
| P0 | Arksey and O'Malley (2005), `Scoping studies: towards a methodological framework`, DOI `10.1080/1364557032000119616` | Classical rationale for mapping an emerging field | local PDF |
| P0 | Levac, Colquhoun, and O'Brien (2010), `Scoping studies: advancing the methodology`, DOI `10.1186/1748-5908-5-69` | Iterative review logic, numerical summary plus thematic analysis | local PDF |
| P1 | Bevilacqua et al. (2025), `Framing the Human-Centered Artificial Intelligence Concepts and Methods: Scoping Review`, DOI `10.2196/67350` | Computing/HCI-style scoping-review exemplar; useful for PRISMA-ScR, OSF protocol, IEEE Xplore search, and design-method charting | local PMC HTML |
| P1 | Feliciani et al. (2019), `A scoping review of simulation models of peer review`, DOI `10.1007/s11192-019-03205-w` | Computational social-science exemplar for heterogeneous simulation/ABM model taxonomy and charting | local PDF |

Downloaded local files:

- `14_Tricco2018_PRISMA_ScR.pdf`
- `15_Peters2024_JBI_Scoping_Reviews.pdf`
- `16_Arksey2005_Scoping_Studies_Framework.pdf`
- `17_Levac2010_Scoping_Studies_Advancing_Methodology.pdf`
- `18_Bevilacqua2025_Human_Centered_AI_Scoping_Review.html` (PMC open full-text HTML; JMIR PDF direct link returned `403`)
- `19_Feliciani2019_Simulation_Models_Peer_Review_Scoping_Review.pdf`

Reserve references only if methods or taxonomy writing still needs more support:

- Peters et al. (2015), `Guidance for conducting systematic scoping reviews`, DOI `10.1097/XEB.0000000000000050`
- Wohlgemut et al. (2024), `A scoping review, novel taxonomy and catalogue of implementation frameworks for clinical decision support systems`, DOI `10.1186/s12911-024-02739-1`
- Sousa et al. (2026), `The landscape of artificial intelligence tools and platforms for evidence synthesis: a scoping review`, DOI `10.1186/s13643-025-02842-y`

## 2. Local Review Library Roles

| Local file | Primary use | Avoid using it for |
|---|---|---|
| `01_Feng2025_Spatial_Intelligence_Across_Scales.pdf` | Spatial-intelligence positioning, scale framing, smart-city and embodied-agent context | Direct social-effect evidence |
| `02_Guo2024_LLM_Multi_Agents_Survey.pdf` | LLM multi-agent landscape, architecture, collaboration context | Spatial representation taxonomy |
| `03_Hu2024_LLM_Game_Agents_Survey.pdf` | Game agents, NPCs, sandbox environments, perception-action interfaces | PRISMA/scoping method claims |
| `04_Gao2024_LLM_ABM_Simulation_Survey.pdf` | LLM-ABM bridge, simulation domains, perception/action/evaluation challenges | Fine-grained spatial taxonomy |
| `05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf` | Individual/scenario/society social-simulation framing | Space Syntax claims |
| `06_Feng2024_Social_Agents_Game_Theory_Survey.pdf` | Social-agent evaluation and game-theoretic interaction settings | Open spatial-environment evidence |
| `07_Luo2025_LLM_Agent_Methodology_Survey.pdf` | Agent methodology, collaboration, evolution, evaluation ecosystem | Scoping-review reporting style |
| `08_Gu2022_VLN_Survey.pdf` | Classical VLN tasks and benchmark background | Social behavior effects |
| `09_Zhang2024_VLN_Foundation_Models_Survey.pdf` | Foundation-model era navigation and world-model framing | Corpus method claims |
| `10_Ma2024_VLA_Embodied_AI_Survey.pdf` | Embodied action interfaces and VLA architecture | Social emergence claims |
| `11_Silacci2026_LLM_Agents_Scoping_Review.pdf` | Scoping-review rhetoric for weak/heterogeneous LLM-agent evidence; outcomes tables | Spatial theory |
| `12_Leiser2025_LLM_Architectures_Scoping_Review.pdf` | Coding dimensions, PRISMA-ScR flow, heterogeneous LLM literature reporting | Domain theory |
| `13_TudorCar2020_Conversational_Agents_Scoping_Review.pdf` | Conceptual analysis, historical figure, distribution/bubble plot, topic/design mapping | LLM architecture claims |

## 3. Article Structure

Use `survey_plan_v4.md` as the base structure, but draft with the current widened evidence-map interpretation.

| Section | Main job | Core references | Method support |
|---|---|---|---|
| `1. Introduction` | Define the WHERE gap, position against existing surveys, state scoping-review design | `01`, `02`, `03`, `04`, `05` | Tricco 2018 |
| `2. Space Syntax Primer` | Provide only the theory needed for configuration, encounter, and movement claims | Foundational Space Syntax sources; `01` only for AI bridge framing | `claim_matrix.md` |
| `3. Evidence Map` | Present corpus tiers, L0-L5 taxonomy, anchor/bridge split, and counts | `12`, `13`; local widened-core tables | JBI; Tricco 2018 |
| `4. Feasibility` | Discuss whether LLM/VLM agents can consume richer spatial information | `01`, `08`, `09`, `10` | Adjacent evidence rules |
| `5. Space in LLM Social Simulation` | Explain how current social-simulation systems use space | `03`, `04`, `05`, `06` | Levac 2010 |
| `6. Evaluation` | Define what future spatial-behavior evaluations must measure | `06`, `07`, `11`, `12` | `claim_matrix.md` |
| `7. Research Agenda` | Convert gaps into concrete research directions | all topic surveys selectively | Arksey/O'Malley; Levac 2010 |
| `8. Conclusion` | Restate findings and limits | no new references | no new evidence |

Recommended writing order:

1. `§3 Evidence Map`
2. `§5 Space in LLM Social Simulation`
3. `§4 Feasibility`
4. `§2 Space Syntax Primer`
5. `§6 Evaluation`
6. `§7 Research Agenda`
7. `§1 Introduction`
8. `§8 Conclusion`

## 4. Figure and Table Plan

The manuscript should be evidence-map centered. Each figure or table must either explain method, position the survey, or report coded evidence.

| Item | Type | Section | Purpose | Best exemplar |
|---|---|---|---|---|
| `Table 1` | Multi-survey positioning matrix | `§1` | Show how this survey differs from spatial intelligence, LLM multi-agent, game-agent, ABM, social-simulation, VLN, and VLA surveys | local README positioning table; `01` |
| `Figure 1` | Corpus/evidence-role diagram | `§1` or `§3` | Show `anchor_core`, `bridge_core`, `Adjacent`, and `Foundational` as distinct evidence roles | `13` conceptual figure style; JBI PCC logic |
| `Figure 2` | PRISMA-ScR flowchart | `§3` or Appendix | Report identification, screening, exclusion reasons, full-text checks, and final rows | `11` Figure 1; `12` Figure 1; PRISMA-ScR |
| `Table 2` | Review protocol summary | `§3` | Summarize databases, time windows, search families, inclusion/exclusion criteria, unit of analysis | `12` Table 1 |
| `Figure 3` | L0-L5 taxonomy diagram | `§3` | Explain agent-accessible spatial representation levels and backend/agent-input distinction | `01` Figure 2; `07` taxonomy overview |
| `Table 3` | Core evidence map | `§3` | Report system/configuration rows by layer, representation, behavioral scale, and evidence status | `12` Tables 2-5; `11` Tables 1-4 |
| `Figure 4` | Representation distribution chart | `§3` | Show `L1/L2/L3/L4/L5`, split by `anchor_core` and `bridge_core` | `13` Figure 3 distribution/bubble plot concept |
| `Table 4` | Environment-side vs agent-accessible examples | `§3` | Show why 3D backend does not automatically mean `L5` | local widened-core table |
| `Table 5` | Space Syntax measure primer | `§2` | Define `integration`, `depth`, `control`, `choice` with intuition and survey use | Foundational Space Syntax sources |
| `Figure 5` | Worked example graph | `§2` | Show how configurational information differs from local adjacency | original figure based on Space Syntax logic |
| `Table 6` | Space Syntax proposition transfer table | `§5` | Mark physical-space propositions as transferable hypotheses, not LLM-agent findings | `04`, `05` |
| `Table 7` | Evaluation dimension table | `§6` | Map candidate measures to representation level, behavioral scale, and evidence requirement | `06`, `07` |
| `Figure 6` | Research agenda map | `§7` | Organize future work by representation, mechanism, emergence, generalization, and applications | `05`, `07` |

Minimum required set for a full draft:

- `Table 1`: multi-survey positioning matrix
- `Figure 1`: corpus/evidence-role diagram
- `Figure 2`: PRISMA-ScR flowchart
- `Figure 3`: L0-L5 taxonomy
- `Table 3`: evidence map
- `Table 4`: environment-side vs agent-accessible examples
- `Table 6`: proposition transfer table
- `Table 7`: evaluation dimensions

Optional after the text stabilizes:

- worked example graph for `§2`
- research agenda map for `§7`
- bubble/distribution plot for representation by evidence status

## 5. Chapter Notes

### Section 1: Introduction

Use `01-05` to show that neighboring survey space is already crowded. The gap is not "no one has reviewed LLM agents"; the gap is that existing surveys do not center agent-accessible spatial representation as a route to social behavior generation.

Use `Table 1` here. Keep protocol details short and move full methods to `§3` and Appendix.

### Section 2: Space Syntax Primer

Use foundational Space Syntax sources, not the LLM surveys, as the main basis. This section should be short and functional:

- core claim: configuration shapes encounter and movement;
- four measures: integration, depth, control, choice;
- one small worked example;
- boundary paragraph: physical-space evidence motivates hypotheses but does not directly prove LLM-agent effects.

### Section 3: Evidence Map

Model the reporting style on `Leiser 2025` and `Tudor Car 2020`.

Required local evidence:

- widened-core evidence map;
- P0/P1 optimistic recheck memos;
- TW-02 scope decision;
- proxy abstract recheck audit.

Keep these counts visible:

- strict `anchor_core`: `19` rows, `17` papers;
- stable widened Core: `35` rows, `33` papers;
- representation distribution: `L1 = 1 / L2 = 8 / L3 = 18 / L4 = 1 / L5 = 7`.

### Section 4: Feasibility

Use `01`, `08`, `09`, and `10`. This section argues feasibility of richer spatial input, not social-effect evidence. It should end with a caution that navigation success and embodied planning do not prove spatially mediated social behavior.

### Section 5: Space in LLM Social Simulation

Use `03`, `04`, `05`, and `06`. The main synthesis should explain that current systems mostly use:

- place labels;
- semantic scene descriptions;
- local co-presence;
- graph/feed structures;
- occasional embodied geometry;
- very little agent-facing configurational or global abstract structure.

### Section 6: Evaluation

Use `06`, `07`, `11`, and `12`. The central artifact should be `Table 7`, not a long narrative. Each evaluation dimension should specify:

- behavior measured;
- spatial representation required;
- control or baseline;
- evidence status it can support.

### Section 7: Research Agenda

Recommended agenda headings:

- representation: how to expose configuration to agents;
- mechanism: structural reasoning vs. spatial-language association;
- emergence: micro-level spatial bias to macro-level social structure;
- generalization: models, languages, and environment types;
- applications: game NPCs, urban simulation, evacuation, metaverse training.

Do not introduce new literature in this section unless it already supports an earlier section.

## 6. Decision

Current reference-gap decision:

- Add the six minimal method/structure/exemplar references listed in Section 1.
- Use the local 13 PDFs as the topic and writing exemplar library.
- Do not add more generic LLM-agent surveys now.
- Generate figure/table assets only after the `§3 Evidence Map` draft outline is frozen.
