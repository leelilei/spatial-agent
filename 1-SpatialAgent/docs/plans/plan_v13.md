# SpatialAgent Research Plan v13

## Spatial-to-Social Network Mapping in LLM-Agent Populations

> Version: 13.0  
> Date: 2026-05-15  
> Lead author: Li  
> Target venue: AAMAS-27 main track, with ICWSM / CSCW / network-science venues as alternatives  
> Status: standalone main-paper plan

---

## 0. One-Line Version

This paper tests whether a controlled spatial topology shapes emergent social networks among LLM agents.

The central question is:

> Does spatial integration in a controlled environment produce more social interaction locally, and does that local exposure aggregate into centrality and tie formation in the emergent dialogue network?

The paper is intentionally scoped as a main-conference experiment, not a multi-paper research program.

---

## 1. Core Claim

LLM-agent systems often place agents in towns, maps, game worlds, simulated communities, and graph-based environments. The missing piece is not the presence of space, but the controlled measurement of how spatial topology becomes social structure.

This paper treats the environment as an experimental substrate:

```text
controlled spatial topology
-> agent-facing configurational representation
-> local social interaction
-> emergent dialogue network
```

The main measurable object is:

```text
F: spatial network -> dialogue network
```

The paper asks whether high-integration spaces become social hubs and whether agents exposed to those spaces become more central in the dialogue network.

---

## 2. Survey Anchor

The survey evidence base provides the empirical motivation:

```text
spatial-agent-survey/paper/appendix/appendix_evidence_table.csv
```

Current coded baseline:

- `35` coded rows
- `anchor_core = 19`
- `bridge_core = 16`
- representation distribution: `L1 = 1 / L2 = 8 / L3 = 19 / L4 = 1 / L5 = 6`
- strict `anchor_core` has `L4 = 0`
- the only admitted `L4` case is a widened digital-network bridge case rather than a physical or navigable spatial anchor case

The survey supports this gap statement:

> Existing LLM-agent systems often include spatial environments, but rarely manipulate computable spatial topology as an agent-facing treatment, and almost never test whether spatial topology maps into emergent social-network structure.

This paper fills that gap with a controlled experiment.

---

## 3. Main Research Question

### 3.1 Primary RQ

> Does a controlled spatial topology shape emergent social networks among LLM agents?

### 3.2 Operational version

> When matched LLM-agent populations run on the same graph under different representation conditions, do integrated locations produce more social interaction, do exposed agents become more central in the dialogue network, and does tie probability decay with topological distance?

### 3.3 Identification strategy

The central identification strategy is:

> We isolate spatial-to-social coupling by comparing matched agent populations across conditions that preserve agents, goals, initial states, graph connectivity, and information volume while varying whether spatial configurational structure is available, correctly mapped, or semantically neutralized.

This is the main defense against the concern that effects are caused by prompt richness, semantic labels, agent roles, movement policy, or evaluator bias.

---

## 4. Contribution Statement

### 4.1 Conceptual

We define spatial-to-social network mapping as a measurable object in LLM-agent populations.

### 4.2 Methodological

We introduce a controlled substrate that manipulates spatial topology and representation while measuring behavior and emergent dialogue networks under explicit null models.

### 4.3 Empirical

We test whether spatial integration, topological distance, and spatial exposure transfer into social interaction, dialogue-network centrality, and tie formation across matched multi-agent simulations.

---

## 5. Scope Control

### 5.1 Main-paper scope

The main paper focuses on:

- one spatial mechanism: `integration`
- one primary social network: `dialogue network`
- three primary hypotheses
- three MVP maps
- four main conditions
- two decisive robustness checks

### 5.2 Deferred or appendix-only topics

These are not primary claims:

- privacy and gatekeeping behavior
- diffusion-network analysis
- human evaluation
- economic-geography reanalysis
- internal spatial-representation probing
- additional layouts such as `Bridge` and `Irregular`

They may appear in appendix, exploratory analysis, or follow-on work after the main experiment is stable.

---

## 6. Primary Hypotheses

### H1: Behavior

High-integration locations produce more social interaction events.

| Field | Specification |
|---|---|
| Unit | run x location |
| Primary metric | social-event rate by location |
| Spatial predictor | `integration_z` |
| Expected direction | positive |
| Primary comparison | `Configurational perception > Topology-only` |

### H2: Network

Agents exposed to high-integration locations become more central in the dialogue network.

| Field | Specification |
|---|---|
| Unit | run x agent |
| Primary metric | dialogue-network weighted degree or strength |
| Spatial predictor | exposure-weighted mean `integration_z` |
| Expected direction | positive |
| Primary comparison | `Configurational perception > Topology-only` |

### H3: Dyadic

Dialogue tie probability decreases with topological distance.

| Field | Specification |
|---|---|
| Unit | run x dyad |
| Primary metric | probability of dialogue tie |
| Spatial predictor | mean or minimum topological distance between agents' visited locations |
| Expected direction | negative |
| Primary comparison | `Configurational perception > Shuffled mapping` |

### 6.1 Exploratory hypotheses

Exploratory only:

- privacy events by depth
- gatekeeping events by control value
- co-occurrence-network centrality
- diffusion-network propagation
- human preference for spatially appropriate trajectories

These cannot overturn failed primary hypotheses.

---

## 7. Experimental Conditions

### 7.1 Main conditions

| Paper-facing name | Internal key | Reviewer-facing meaning | Role |
|---|---|---|---|
| Topology-only | `C1` | agents move on the same graph but receive no explicit configurational metrics | baseline |
| Non-spatial control | `C2c` | same information volume and structure, but no spatial meaning | information-volume control |
| Configurational perception | `C6m` | agents receive explicit integration, depth, and control descriptors | main treatment |
| Shuffled mapping | `C_shuffle` | same descriptors, but assigned to wrong locations | mechanism control |

### 7.2 Demonstration condition

| Paper-facing name | Internal key | Role |
|---|---|---|
| Full SpatialAgent | `C4` | system demonstration and secondary analysis, not the primary causal claim |

`C4` is intentionally not the center of the confirmatory claim because it combines representation, movement metrics, and action sampling.

### 7.3 Optional audit conditions

| Paper-facing name | Internal key | Role |
|---|---|---|
| Neutral numeric descriptors | `C6m_neutral` | tests whether the effect depends on spatial vocabulary |
| Counter-semantic labels | `C_counter` | tests whether semantic labels override structure |
| Judge-only spatial information | `C_judge_only` | tests evaluator artifact risk |
| Rule scorer | `C_rule_scorer` | tests non-LLM scoring robustness |

These audits should be run if resources allow, but the main design remains readable without them.

---

## 8. Maps

The main paper uses exactly three maps:

| Map | Purpose |
|---|---|
| `Plaza` | high-integration public convergence case |
| `Grid` | regular control topology |
| `Labyrinth` | high-depth separation case |

Map-entry requirements:

- connected graph
- no isolated required location
- enough variance in `integration_z`
- enough visits per location in pilot runs
- labels pass lexical leakage checks

Deferred maps:

- `Bridge`
- `Irregular`

Deferred maps stay out of the main paper unless the core experiment is already successful and powered.

---

## 9. Primary Social Network

### 9.1 Primary network: dialogue network

All confirmatory social-network claims use the dialogue network unless explicitly marked otherwise.

Definition:

- node = agent
- edge = at least one dialogue interaction between two agents
- edge weight = number of dialogue turns or dialogue events
- default direction = undirected for main centrality analysis, directed in appendix if turn initiation is reliable

Why dialogue is primary:

- it is directly social
- it is observable in logs
- it avoids treating mere co-presence as a social tie
- it is easier to validate than semantic information diffusion

### 9.2 Secondary network: co-occurrence network

Definition:

- node = agent
- edge weight = number of rounds two agents share a location

Use:

- exposure baseline
- mechanism check
- not a confirmatory social tie by itself

### 9.3 Exploratory network: diffusion network

Definition:

- directed edge `A -> B` if information introduced by `A` later appears in `B`'s memory, speech, or decision rationale

Use:

- exploratory or appendix-only
- requires strict evidence threshold
- not part of the main confirmatory claim

### 9.4 Spatial-exposure network

Definition:

- agent-location bipartite graph
- optional projection based on shared location-visit profiles

Use:

- exposure control
- helps distinguish social interaction from shared spatial opportunity

---

## 10. Event Coding and Internal Validity

Event coding is the largest internal-validity risk, so it is a core method component rather than an appendix detail.

### 10.1 Primary observable event definitions

Primary social events should be defined as observably as possible:

- co-location plus dialogue turn
- direct message between two agents
- repeated contact across rounds
- explicit information handoff when available

Semantic labels such as `privacy` and `gatekeeping` are secondary.

### 10.2 Primary event coding policy

The primary `social` event should be rule-based where possible.

Recommended primary rule:

```text
social_event = same round dialogue interaction between two agents, with location recorded
```

This reduces dependence on an LLM judge.

### 10.3 Judge policy

When an LLM judge is used:

- the judge must be blind to condition
- location descriptors should be removed or sanitized from `event_text` where possible
- the judge prompt and model version must be frozen
- a `C_judge_only` audit should test whether evaluator access to spatial information can reproduce the main effect

### 10.4 Human validation subset

Use a small human-coded validation subset if feasible:

- sample across maps, conditions, and seeds
- code social-event presence and dialogue tie validity
- report agreement between rule-based coding, LLM judge, and human coding

---

## 11. Required Outputs

Each run must produce:

```text
results/v13/{map}/{seed}/{condition}/metadata.json
results/v13/{map}/{seed}/{condition}/visits.csv
results/v13/{map}/{seed}/{condition}/events.csv
results/v13/{map}/{seed}/{condition}/messages.jsonl
results/v13/{map}/{seed}/{condition}/metrics_run.json
results/v13/{map}/{seed}/{condition}/network_dialogue.graphml
results/v13/{map}/{seed}/{condition}/network_cooccurrence.graphml
results/v13/{map}/{seed}/{condition}/network_spatial_exposure.graphml
results/v13/{map}/{seed}/{condition}/network_metrics.json
```

Required `visits.csv` columns:

```text
round, agent_id, location
```

Required `events.csv` columns:

```text
round, agent_id, target_id, location, event_type, event_text, event_source
```

Allowed primary `event_type` values:

```text
social, other
```

Secondary semantic event types:

```text
privacy, gatekeeping
```

---

## 12. Stage Plan

### 12.1 Stage 0: preflight

Mandatory gates:

- spatial metric sanity
- model comprehension
- lexical leakage audit
- reverse-inference audit
- event-coding pilot
- matched-initial-condition pilot
- convergence pilot
- dialogue-network sanity pilot

Pass condition:

- all three MVP maps pass map checks
- the primary model understands the descriptor format
- rule-based social-event extraction works on pilot logs
- dialogue networks are non-degenerate under interaction-enabled conditions

### 12.2 Stage 1: micro-task validation

Purpose:

- verify that configurational information affects single-step behavioral choices before running long simulations

Minimum conditions:

```text
C1, C2c, C6m, C_shuffle
```

Optional audits:

```text
C6m_neutral, C_counter
```

Stage 2 remains confirmatory only if:

- `C6m > C1` on the preregistered social-location choice direction
- `C6m > C_shuffle`
- the effect is not fully explained by information volume or lexical leakage

### 12.3 Stage 2: main long-run simulation

Run definition:

```text
run = map x seed x condition
```

MVP design:

```text
3 maps x 10 seeds x 4 conditions = 120 runs
```

MVP conditions:

```text
C1, C2c, C6m, C_shuffle
```

Optional demonstration:

```text
3 maps x 10 seeds x C4 = 30 additional runs
```

Total with demonstration:

```text
150 runs
```

### 12.4 Stage 3: robustness

Minimum robustness checks:

- rule scorer for primary event extraction
- LLM judge blinded to condition
- co-occurrence network as secondary comparison
- run-level permutation tests

Optional robustness checks:

- `C6m_neutral`
- `C_counter`
- alternate model
- diffusion network

### 12.5 Stage 4: optional human evaluation

Human evaluation is not required for the main claim.

If run, it should test:

> Which trajectory is more spatially appropriate and socially plausible?

Primary comparison:

```text
C6m vs C1
```

Recommended target:

```text
N = 80
```

---

## 13. Statistical Analysis

### 13.1 Independent unit

The primary independent unit is the run.

Dyads, agents, locations, and time windows are nested within runs. They must not be treated as independent samples without a dependence-aware model or permutation scheme.

### 13.2 H1 behavior model

Primary endpoint:

```text
tar_h1_run_full
```

Early endpoint:

```text
tar_h1_run_early
```

Operational formula:

```text
For each location:
  social_event_rate = social events at location / visits to location

rho_run = SpearmanCorr(social_event_rate, integration_z)
tar_h1_run = FisherZ(rho_run)
```

Primary model:

```r
tar_h1_run_full ~ condition + map + condition:map + (1|seed)
```

Fallback if unstable:

```r
tar_h1_run_full ~ condition + (1|seed)
```

and report map-specific estimates descriptively.

### 13.3 H2 agent-network model

Primary network:

```text
dialogue network
```

Primary response:

```text
agent weighted degree / strength
```

Primary predictor:

```text
exposure-weighted mean integration_z
```

Recommended model:

```text
run-level aggregation first, then cross-run comparison
```

or:

```text
mixed model with agent nested in run and run clustered by map x seed
```

### 13.4 H3 dyadic model

Primary response:

```text
dialogue tie present / absent
```

Primary predictor:

```text
topological distance between agents' visited-location distributions
```

Dependence-aware analysis:

- QAP or MRQAP within run
- run-level coefficient aggregation across seeds and maps
- permutation at run or seed level for confirmatory inference

Dyads must not be treated as independent raw rows in a simple logistic regression.

### 13.5 Null models

| Claim | Primary null |
|---|---|
| H1 behavior alignment | shuffled metric-location mapping |
| H2 network centrality | permuted agent exposure profiles |
| H3 distance decay | shuffled location-pair distances |
| dialogue-network structure | degree-preserving rewiring |
| co-occurrence robustness | spatial-exposure baseline |

### 13.6 Multiple comparisons

Primary confirmatory family:

- H1
- H2
- H3

Control:

- FDR within the primary family
- exploratory analyses reported separately

---

## 14. Power and SESOI

Power analysis must be run before confirmatory Stage 2.

### 14.1 Smallest effect sizes of interest

Proposed SESOI:

| Endpoint | SESOI |
|---|---|
| H1 behavior | `Delta FisherZ >= 0.25` between `C6m` and `C1` |
| H2 network | `Delta standardized degree slope >= 0.25` for exposure-weighted integration |
| H3 dyadic | `OR <= 0.80` per additional topological step |

These values can be revised after Stage 0 pilots, but must be frozen before Stage 2.

### 14.2 Power target

Minimum:

```text
80% power for H1 and H2 at the frozen SESOI
```

Desired:

```text
80% power for all three primary hypotheses
```

If the MVP has less than `70%` power for H1 or H2, the experiment is written as pilot or boundary-condition evidence rather than confirmatory evidence.

---

## 15. Implementation Binding

### 15.1 Required configs and runners

| Need | Proposed file |
|---|---|
| condition definitions | `spatial-agent-core/configs/experiments/v13_conditions.yaml` |
| main experiment config | `spatial-agent-core/configs/experiments/exp_v13_main.yaml` |
| run launcher | `spatial-agent-core/experiments/run_v13.py` |
| metrics wrapper | `spatial-agent-core/src/analysis/v13_metrics.py` |
| power simulation | `spatial-agent-core/src/analysis/v13_power.py` |

### 15.2 Required analysis modules

| Module | Proposed path | Responsibility |
|---|---|---|
| event extraction | `spatial-agent-core/src/analysis/event_extraction.py` | rule-based social-event extraction |
| network construction | `spatial-agent-core/src/analysis/network_construction.py` | dialogue, co-occurrence, and exposure networks |
| network metrics | `spatial-agent-core/src/analysis/network_metrics.py` | degree, strength, centralization, distance decay |
| network hypotheses | `spatial-agent-core/src/analysis/network_hypotheses.py` | H2 and H3 tests |
| QAP utilities | `spatial-agent-core/src/analysis/qap.py` | dyadic dependence-aware inference |
| null models | `spatial-agent-core/src/analysis/network_nulls.py` | metric shuffling, rewiring, permutation nulls |

### 15.3 Required docs

| Document | Proposed path |
|---|---|
| output schema | `spatial-agent-core/docs/v13_output_schema.md` |
| condition manual | `spatial-agent-core/docs/v13_condition_manual.md` |
| event coding manual | `spatial-agent-core/docs/v13_event_coding.md` |
| preregistration draft | `spatial-agent-core/docs/v13_preregistration.md` |

---

## 16. Downgrade Rules

### 16.1 Main downgrades

- If `C_shuffle` matches `C6m`, downgrade to mapping-insensitive prompt effect.
- If `C2c` matches `C6m`, downgrade to information-volume or format effect.
- If social-event extraction depends on an unblinded LLM judge, downgrade internal-validity strength.
- If dyadic effects disappear under QAP or run-level aggregation, do not claim distance decay.
- If dialogue-network results are absent but co-occurrence results are positive, claim exposure structure rather than social-network structure.

### 16.2 Result tiers

| Tier | H1 behavior | H2 network | H3 dyadic | Claim |
|---|---|---|---|---|
| Tier 1 | positive | positive | positive | spatial integration shapes local interaction and emergent dialogue ties |
| Tier 2 | positive | positive | mixed | spatial integration shapes interaction and centrality, distance decay is weak |
| Tier 3 | positive | negative | mixed | local response does not aggregate into network structure |
| Tier 4 | negative | negative | negative | current substrate does not support robust spatial-to-social mapping |

---

## 17. Paper Structure

```text
1. Introduction
2. Survey-Derived Gap and Research Question
3. SpatialAgent Substrate and Conditions
4. Event Coding and Dialogue-Network Construction
5. Hypotheses and Identification Strategy
6. Stage 0 and Stage 1 Validation
7. Main Long-Run Results
8. Robustness and Null Models
9. Discussion
10. Limitations
11. Conclusion
```

Appendix:

```text
A. Survey evidence bridge
B. Layout metrics
C. Prompt templates
D. Event coding validation
E. Network construction details
F. Power simulation
G. Exploratory privacy/gatekeeping/diffusion analyses
H. Optional human evaluation
```

---

## 18. Main Risks

### 18.1 Scope creep

Risk:

- the work expands into a broad research program rather than a sharp main paper

Control:

- keep H1, H2, H3 as the only primary hypotheses
- keep dialogue network as the only primary social network
- keep Plaza, Grid, and Labyrinth as the only main maps

### 18.2 Semantic leakage

Risk:

- spatial labels or descriptors imply social affordances

Control:

- non-spatial control
- shuffled mapping
- lexical leakage audit
- neutral numeric descriptor audit if feasible

### 18.3 Event-coding artifact

Risk:

- measured social events reflect judge bias rather than agent behavior

Control:

- rule-based primary event definition
- blinded judge only for secondary labels
- sanitized event text
- human validation subset

### 18.4 Pseudo-replication

Risk:

- dyads and agents are treated as independent when they share the same run context

Control:

- run as primary independent unit
- QAP or MRQAP for dyads
- run-level coefficient aggregation
- permutation at run or seed level

---

## 19. Execution Checklist

### 19.1 Immediate planning

- [ ] Freeze the three primary hypotheses.
- [ ] Freeze the four main conditions.
- [ ] Freeze dialogue network as the primary network.
- [ ] Freeze the MVP map set: Plaza, Grid, Labyrinth.
- [ ] Freeze SESOI values after pilot calibration.

### 19.2 Before coding

- [ ] Create `v13_conditions.yaml`.
- [ ] Create `exp_v13_main.yaml`.
- [ ] Draft `v13_output_schema.md`.
- [ ] Draft `v13_event_coding.md`.
- [ ] Define rule-based social-event extraction.

### 19.3 Before Stage 1

- [ ] Implement micro-task validation.
- [ ] Run lexical leakage audit.
- [ ] Run reverse-inference audit.
- [ ] Confirm `C6m > C_shuffle` on the preregistered micro-task direction.

### 19.4 Before Stage 2

- [ ] Implement `run_v13.py`.
- [ ] Implement `v13_metrics.py`.
- [ ] Implement dialogue-network construction.
- [ ] Implement QAP or run-level dyadic coefficient aggregation.
- [ ] Run power simulation for H1, H2, and H3.
- [ ] Pass dialogue-network sanity pilot.

### 19.5 Before writing

- [ ] Report H1, H2, and H3 before exploratory analyses.
- [ ] Report null models for each network claim.
- [ ] Keep co-occurrence and diffusion separate from dialogue-network claims.
- [ ] Apply downgrade rules explicitly.

---

## 20. Final Positioning

The clean main-paper claim is:

> Controlled spatial topology can shape emergent dialogue networks in LLM-agent populations, and this coupling can be measured through preregistered behavior-level and network-level endpoints under explicit null models.

The paper is strongest when it stays narrow:

```text
integration -> social interaction -> dialogue centrality / distance decay
```

The goal is not to show every possible spatial-social regularity. The goal is to establish one carefully identified experimental pathway from spatial topology to emergent social structure.
