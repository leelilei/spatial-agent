# SpatialAgent Research Plan v12

## Spatial-to-Social Network Mapping in LLM-Agent Populations

> Version: 12.0  
> Date: 2026-05-15  
> Lead author: Li  
> Target venues: AAMAS-27 for the main systems paper, with possible follow-on papers in economic geography and network science  
> Status: standalone working plan

---

## 0. One-Line Version

This project measures how a controlled spatial substrate maps into an emergent social network in LLM-agent populations.

The central question is:

> When LLM agents move, meet, talk, and exchange information in a controlled spatial topology, how does the exogenous spatial network shape the endogenous social network that emerges?

The paper studies not only whether spatial information changes local behavior, but also whether local behavioral changes accumulate into measurable population-level social structure.

---

## 1. Core Thesis

LLM-agent systems increasingly place agents in maps, towns, games, simulated communities, social VR environments, and graph-based worlds. Yet in most systems, space remains a scene setting, a movement menu, or a semantic prompt ingredient.

SpatialAgent reframes space as a controlled experimental substrate:

```text
computable spatial topology
-> agent-facing spatial representation
-> local behavioral response
-> emergent social-network structure
-> spatial-to-social mapping
```

The main object of study is the mapping between:

- an `exogenous spatial network`: the layout, topology, distance, integration, depth, and control structure
- an `endogenous social network`: ties produced by co-location, dialogue, information flow, and repeated interaction

The project asks whether the social network inherits, transforms, or decouples from the spatial network.

---

## 2. Survey Anchor

The survey evidence base remains the empirical anchor for the research gap:

```text
spatial-agent-survey/paper/appendix/appendix_evidence_table.csv
```

Current coded baseline:

- `35` coded rows
- `anchor_core = 19`
- `bridge_core = 16`
- representation distribution: `L1 = 1 / L2 = 8 / L3 = 19 / L4 = 1 / L5 = 6`
- strict `anchor_core` has `L4 = 0`
- the only admitted `L4` case appears in a widened digital-network bridge case, not in a physical or navigable spatial anchor case

System-level interpretation:

- the appendix contains `35` coded rows
- the widened corpus corresponds to roughly `33` system-level items when dual-row systems are collapsed at the family level

The survey does not support a weak absence claim such as:

> LLM-agent systems do not use space.

It supports a sharper claim:

> Existing LLM-agent systems often include spatial environments, but rarely treat computable spatial structure as an experimentally controlled agent-facing variable, and almost never analyze the resulting population-level social network as the primary outcome.

---

## 3. Research Gap

### 3.1 The precise gap

The spatial-to-social network mapping in LLM-agent populations is currently unmeasured.

We do not know whether:

- high-integration locations become social hubs
- deeper or more segregated locations become privacy or withholding zones
- high-control locations produce brokerage or gatekeeping behavior
- distance decay appears in synthetic social ties
- different layouts leave distinguishable signatures on emergent communication networks
- social dynamics eventually override the spatial substrate

### 3.2 Why this gap matters

The gap is not just that one more metric has not been tested.

It defines a new measurable object:

```text
F: spatial network -> social network
```

That mapping function can produce several publishable outcomes:

- `inheritance`: social structure tracks spatial structure
- `transformation`: spatial structure matters, but agents reshape it
- `decoupling`: social dynamics override spatial constraint
- `no stable pattern`: current LLM-agent systems are weak substrates for network-level social science

All four outcomes are scientifically meaningful.

---

## 4. Positioning

### 4.1 What the paper claims

The paper claims that:

- spatial-to-social coupling can be operationalized in LLM-agent populations
- the coupling can be measured at both behavior and network levels
- controlled spatial substrates let us test network-science regularities under reduced confounding
- positive, mixed, and negative results each clarify what LLM-agent societies can and cannot model

### 4.2 What the paper does not claim

The paper does not claim that:

- LLM agents are equivalent to humans
- synthetic populations validate or falsify human social theory by themselves
- any observed network pattern implies human-like spatial cognition
- any failed transfer invalidates the corresponding human-population regularity
- Space Syntax is proven in artificial societies

### 4.3 Safest framing

The safest recurring sentence is:

> We use controlled spatial topology as a computable representation layer and measure how that layer shapes local behavior and emergent social-network structure in LLM-agent populations.

---

## 5. Adjacent Literatures

| Literature | What it already contributes | What remains missing |
|---|---|---|
| LLM-agent social simulation | agents, memory, dialogue, roles, group behavior | spatial topology is rarely treated as a controlled causal substrate |
| LLM multi-agent communication topology | task graphs, routing, coordination networks | topology is usually imposed rather than emergent, and rarely spatial |
| spatial network science | spatial-social regularities in human populations | observational confounds and limited experimental control |
| economic geography | distance decay, agglomeration, spatial homophily | limited ability to manipulate social and spatial structure independently |
| Space Syntax and ABM | computable configurational variables and movement behavior | reactive agents and limited endogenous social-network formation |

SpatialAgent combines:

- LLM-agent cognition and dialogue
- explicit spatial topology
- controlled experimental manipulation
- endogenous social ties
- network-level null models

That combination is the opening.

---

## 6. Contributions

### 6.1 Conceptual contribution

- Define `spatial-to-social network mapping` as a measurable property of LLM-agent populations.
- Provide a four-way outcome typology: inheritance, transformation, decoupling, no stable pattern.

### 6.2 Methodological contribution

- Build a controlled simulation substrate with preregistered spatial, behavioral, and network outputs.
- Define separate co-occurrence, dialogue, diffusion, and spatial-exposure networks.
- Pair every network metric with a stated null model.

### 6.3 Empirical contribution

- Measure spatial-to-social coupling across layouts, seeds, and representation conditions.
- Test distance decay, brokerage transfer, layout signatures, and coupling decay in a synthetic population.

### 6.4 Cross-disciplinary contribution

- Offer a reproducible testbed for questions in agent simulation, network science, spatial sociology, and economic geography.
- Clarify which human-population regularities transfer to LLM-agent substrates and which do not.

---

## 7. Hypothesis Architecture

The plan uses two coupled hypothesis layers.

### 7.1 Layer 1: behavior-level hypotheses

| ID | Direction | Unit | Primary metric | Main comparison | Status |
|---|---|---|---|---|---|
| H1a | Higher integration nodes have higher social-event rate. | run | `tar_h1_run_early`, `tar_h1_run_full` | `C4 > C1` | confirmatory |
| H1b | Explicit configurational perception increases social-event alignment beyond topology-only input. | run | `tar_h1_run_early`, `tar_h1_run_full` | `C6m > C1` | confirmatory |
| H1c | Explicit configurational perception exceeds non-spatial and semantic controls. | run | `tar_h1_run_full` | `C6m > C2`, `C6m > C2b`, `C6m > C2c` | confirmatory with FDR |
| H1d | Correct structure-location mapping matters. | run | `tar_h1_run_full` | `C6m > C_shuffle` | mechanism confirmatory |
| H1e | Neutral numeric descriptors preserve part of the configurational effect. | micro-task | `h1_micro_alignment` | `C6m_neutral > C1` | mechanism confirmatory |
| H2 | Higher mean-depth nodes have higher privacy-event rate. | run | `tar_h2_run` | directional test | secondary |
| H3 | Higher control-value nodes have higher gatekeeping-event rate. | run | `tar_h3_run` | directional test | conditional secondary |
| H4 | Human judges prefer spatially structured trajectories as more spatially appropriate. | participant | pairwise preference | `C4 > C1` | strong-version secondary |

### 7.2 Layer 2: network-level hypotheses

| ID | Direction | Unit | Primary metric | Null model | Status |
|---|---|---|---|---|---|
| H1n | Social-network centralization tracks spatial-network integration centralization. | map x seed | correlation or mixed-effects coefficient | rewired social-network null | confirmatory |
| H2n | Tie probability decreases with topological distance. | dyad | distance-decay coefficient | shuffled location-pair null | confirmatory |
| H3n | Exposure to high-control-value nodes predicts emergent brokerage. | agent | QAP or MRQAP coefficient | permuted trajectory-assignment null | confirmatory |
| H4n | Different layouts yield distinct social-network signatures. | layout | graph-distance or NetEMD-style comparison | configuration-model null per layout | confirmatory |
| H5n | Spatial-social coupling decays over interaction horizon. | population | half-life of coupling metric | constant-coupling null | secondary |

### 7.3 Two-layer interpretation matrix

| Layer 1 result | Layer 2 result | Interpretation |
|---|---|---|
| positive | positive | spatial structure shapes both local behavior and macro-structure |
| positive | negative | local spatial responsiveness does not accumulate into stable network structure |
| negative | positive | population-level coupling emerges through indirect or delayed dynamics |
| negative | negative | current substrate does not support robust spatial-to-social coupling |

---

## 8. Experimental Conditions

### 8.1 Main conditions

| Condition | Purpose | MVP status |
|---|---|---|
| `C1` | topology-only baseline | included |
| `C2c` | true non-spatial control | included |
| `C6m` | explicit configurational perception | included |
| `C6f` | movement-level spatial metrics | included |
| `C4` | full SpatialAgent condition | included |
| `C2` | implicit spatial-affordance baseline | strong version |
| `C2b` | structured non-spatial format control | strong version |
| `C6m_neutral` | neutral numeric descriptor audit | Stage 1 required, Stage 2 optional |

### 8.2 Audit conditions

| Condition | Purpose |
|---|---|
| `C_shuffle` | tests whether correct metric-location mapping matters |
| `C_counter` | tests structure versus semantic label conflict |
| `C_judge_only` | tests evaluator artifact risk |
| `C_rule_scorer` | tests non-LLM scoring robustness |
| `C_isolated` | blocks inter-agent interaction to isolate exposure-only structure |
| `C_random_layout` | compares real spatial layouts against matched random graph substrates |

### 8.3 Diagnostic contrasts

The contrasts are diagnostic rather than additive decompositions:

| Contrast | Interpretation |
|---|---|
| `C4 - C1` | full spatial-agent effect |
| `C6m - C1` | configurational perception effect |
| `C6m - C2c` | explicit spatial structure versus true non-spatial control |
| `C6m - C2` | explicit structure versus implicit spatial semantics |
| `C6m_neutral - C1` | neutral metric representation effect |
| `C6f - C6m` | movement-level metric contribution |
| `C4 - C6f` | action-sampling contribution |
| `C_isolated - C4` | interaction-mediated network formation |
| `C_random_layout - C4` | layout-specific structure versus generic graph substrate |

---

## 9. Experimental Materials

### 9.1 Maps

MVP maps:

- `Plaza`
- `Labyrinth`
- `Grid`

Strong-version or follow-on maps:

- `Bridge`
- `Irregular`

Map-entry rule:

- no map enters confirmatory analysis until it passes Stage 0 sanity checks
- new maps stay out of the formal design until their files exist and their spatial metrics are validated

### 9.2 Agents

Default population:

```text
10 agents per run
200 rounds per run
```

Pilot-based adjustment:

- increase to `300` rounds if behavior-level or network-level metrics do not stabilize at `200`

Agent traits should vary in:

- role
- public or private preference
- information sensitivity
- movement tendency
- social openness

Matched seeds must preserve initial locations, personas, goals, initial events, and non-spatial description mappings across comparable conditions.

### 9.3 Models

Before confirmatory execution, freeze:

- model endpoint name
- provider
- temperature
- top-p if available
- max tokens
- prompt template path
- prompt hash
- execution date

The primary and robustness models must pass the Stage 0 gates before they are used in confirmatory runs.

---

## 10. Required Outputs

Each run must produce the core behavioral artifacts:

```text
results/v12/{map}/{seed}/{condition}/metadata.json
results/v12/{map}/{seed}/{condition}/visits.csv
results/v12/{map}/{seed}/{condition}/events.csv
results/v12/{map}/{seed}/{condition}/messages.jsonl
results/v12/{map}/{seed}/{condition}/metrics_run.json
```

Required `visits.csv` columns:

```text
round, agent_id, location
```

Required `events.csv` columns:

```text
round, agent_id, target_id, location, event_type, event_text, judge_source
```

Allowed confirmatory `event_type` values:

```text
social, privacy, gatekeeping, other
```

Each run must also produce network artifacts:

```text
results/v12/{map}/{seed}/{condition}/network_social_cooccurrence.graphml
results/v12/{map}/{seed}/{condition}/network_social_dialogue.graphml
results/v12/{map}/{seed}/{condition}/network_social_diffusion.graphml
results/v12/{map}/{seed}/{condition}/network_spatial_exposure.graphml
results/v12/{map}/{seed}/{condition}/network_metrics.json
results/v12/{map}/{seed}/{condition}/coupling_timeseries.csv
```

---

## 11. Network Construction Protocols

### 11.1 Co-occurrence network

Definition:

- node = agent
- edge weight = number of rounds in which two agents occupy the same location

Frozen before Stage 2:

- threshold rule
- whether weights are raw counts, normalized rates, or both
- whether brief contacts count equally across all locations

### 11.2 Dialogue network

Definition:

- node = agent
- directed or undirected edge = dialogue turn between agents
- edge weight = number of dialogue turns or weighted interaction count

Frozen before Stage 2:

- directionality
- multi-party dialogue handling
- repeated-turn aggregation

### 11.3 Information-diffusion network

Definition:

- directed edge `A -> B` if information introduced by `A` appears in `B`'s memory, speech, decision rationale, or recorded knowledge state

Frozen before Stage 2:

- evidence threshold for information adoption
- whether semantic paraphrase counts
- whether source attribution is required

### 11.4 Spatial-exposure network

Definition:

- agent-location bipartite graph based on visits
- projected agent-agent graph based on shared spatial exposure

Use:

- distinguishes pure co-exposure from interaction-mediated social ties
- supports `C_isolated` interpretation

### 11.5 Anti-conflation rule

The paper must report the network types separately before making any aggregate "social network" claim.

---

## 12. Stage Plan

### 12.1 Stage 0: preflight gates

Mandatory gates:

- spatial metric sanity
- model comprehension
- reverse-inference audit
- lexical norming
- prompt-position audit
- event-coding pilot
- matched-initial-condition pilot
- convergence pilot
- network-sanity pilot

Network-sanity pass expectations:

- interaction-enabled runs produce non-degenerate networks
- mean degree exceeds a trivial isolated baseline
- network construction succeeds for all preregistered network types
- null-model generation works on pilot outputs

### 12.2 Stage 1: micro-task representation experiment

Purpose:

- test whether the representation layer changes single-step behavioral judgments before expensive long-run simulation

Minimum conditions:

```text
C1, C2c, C6m, C6m_neutral, C_shuffle
```

Stage 2 remains confirmatory only if the Stage 1 representation tests support the core configurational-response logic.

### 12.3 Stage 2: long-run multi-agent simulation

Run definition:

```text
run = map x seed x condition
```

MVP design:

```text
3 maps x 10 seeds x 5 conditions = 150 runs
```

MVP conditions:

```text
C1, C2c, C6m, C6f, C4
```

Strong design:

```text
3 maps x 15 seeds x 8 conditions = 360 runs
```

Expanded design:

```text
5 maps x 15 seeds x 8 conditions = 600 runs
```

The same Stage 2 run set feeds both behavior-level and network-level analyses.

### 12.4 Stage 3: mechanism and robustness

Mechanism checks:

- `C_shuffle`
- `C_counter`
- `C_judge_only`
- `C_rule_scorer`
- `C_isolated`
- `C_random_layout`

Robustness checks:

- alternate model where feasible
- alternate network thresholds
- alternate null models
- time-window sensitivity

### 12.5 Stage 4: human evaluation

Purpose:

- test whether trajectories are perceived as more spatially appropriate or socially plausible

Default comparison:

```text
C4 vs C1
```

Secondary comparisons:

```text
C6m vs C2c
C6m_neutral vs C1
```

Recommended target:

```text
N = 80 participants
```

### 12.6 Stage 5: cross-theory reanalysis

This is an analysis stage, not a new simulation stage.

Possible lenses:

- distance decay and spatial homophily
- brokerage and control-value transfer
- network signature comparison
- internal spatial-representation probes

---

## 13. Metrics

### 13.1 Behavior-level TAR metrics

For each run and hypothesis:

```text
For each location:
  event_rate_h = number of events of type h at location / visits to location

rho_h_run = SpearmanCorr(event_rate_h, spatial_metric_h)
tar_h_run = FisherZ(rho_h_run)
bsr_h_run = abs(tar_h_run)
```

Primary mapping:

| Hypothesis | Event type | Spatial metric | Expected direction |
|---|---|---|---|
| H1 | `social` | `integration_z` | positive |
| H2 | `privacy` | `mean_depth_z` | positive |
| H3 | `gatekeeping` | `control_value_z` | positive |

Primary endpoints:

- `tar_h1_run_early`
- `tar_h1_run_full`

### 13.2 Network metrics

Minimum network metrics:

- mean degree
- density
- degree centralization
- weighted strength distribution
- clustering
- betweenness
- brokerage score
- assortativity or homophily diagnostics
- layout-specific graph signature distance
- coupling-timeseries summary

### 13.3 Coupling metrics

Possible coupling metrics:

- correlation between spatial integration and social degree by location
- tie probability as a function of topological distance
- agent brokerage as a function of exposure to high-control nodes
- distance between social-network signatures across layouts
- time-windowed coupling strength

---

## 14. Statistical Analysis

### 14.1 Behavior-level model

Primary model:

```r
tar_h1_run_full ~ condition + map + condition:map + (1|seed)
```

Early endpoint model:

```r
tar_h1_run_early ~ condition + map + condition:map + (1|seed)
```

If map count makes the model unstable:

```r
tar_h1_run_full ~ condition + (1|seed)
```

and map-specific estimates are reported descriptively.

### 14.2 Network-level methods

| Hypothesis | Main method | Null model | Correction |
|---|---|---|---|
| H1n | run-level correlation or mixed model | rewired social-network null | FDR within network family |
| H2n | exponential or power-law distance-decay fit | shuffled location-pair null | FDR |
| H3n | QAP or MRQAP | permuted trajectory-assignment null | FDR |
| H4n | graph-signature distance | configuration-model null per layout | layout-pair correction |
| H5n | windowed coupling regression | constant-coupling null | descriptive unless powered |

### 14.3 Power analysis

Behavior-layer and network-layer power must be simulated separately.

Minimum behavior-layer power targets:

- `C4 vs C1`
- `C6m vs C2c`
- `C6f vs C6m`

Minimum network-layer power targets:

- `H1n`
- `H2n`
- `C_isolated` versus interaction-enabled reference
- `C_random_layout` versus matched structured-layout reference

Decision rule:

- if power is adequate for the primary behavior and network endpoints, the MVP can support confirmatory claims
- if power is weak, the same design becomes a pilot or boundary-condition study

---

## 15. Implementation Binding

### 15.1 Required configs and runners

| Need | Proposed file |
|---|---|
| condition definitions | `spatial-agent-core/configs/experiments/v12_conditions.yaml` |
| main experiment config | `spatial-agent-core/configs/experiments/exp_v12_main.yaml` |
| run launcher | `spatial-agent-core/experiments/run_v12.py` |
| metrics wrapper | `spatial-agent-core/src/analysis/v12_metrics.py` |
| power simulation | `spatial-agent-core/src/analysis/v12_power.py` |

### 15.2 Required analysis modules

| Module | Proposed path | Responsibility |
|---|---|---|
| network construction | `spatial-agent-core/src/analysis/network_construction.py` | build co-occurrence, dialogue, diffusion, and exposure networks |
| network metrics | `spatial-agent-core/src/analysis/network_metrics.py` | compute centralization, clustering, brokerage, and signature metrics |
| network hypotheses | `spatial-agent-core/src/analysis/network_hypotheses.py` | evaluate H1n-H5n |
| QAP utilities | `spatial-agent-core/src/analysis/qap.py` | QAP or MRQAP wrappers |
| null models | `spatial-agent-core/src/analysis/network_nulls.py` | rewiring, configuration-model, spatial-shuffle nulls |

### 15.3 Required docs

| Document | Proposed path |
|---|---|
| output schema | `spatial-agent-core/docs/v12_output_schema.md` |
| network schema | `spatial-agent-core/docs/v12_network_schema.md` |
| condition manual | `spatial-agent-core/docs/v12_condition_manual.md` |
| preregistration draft | `spatial-agent-core/docs/v12_preregistration.md` |

---

## 16. Downgrade Rules

### 16.1 Behavior-layer downgrades

- If `C_shuffle` is as strong as `C6m`, downgrade to mapping-insensitive prompt effect.
- If `C_counter` follows semantic labels over structure, downgrade to semantic-affordance effect.
- If `C_judge_only` reproduces the main effect, downgrade to evaluator artifact risk.
- If `C_rule_scorer` reverses direction, downgrade to scorer dependence.

### 16.2 Network-layer downgrades

- If a network metric lacks a null model, it cannot support a confirmatory claim.
- If `C_isolated` reproduces the main network result, downgrade to exposure-only structure.
- If `C_random_layout` matches structured layouts, downgrade to generic graph-substrate dependence.
- If only one network-construction protocol supports an effect, narrow the claim to that protocol.
- If the result appears only in one map, treat it as layout-specific rather than general.

### 16.3 Result tiers

| Tier | Behavior layer | Network layer | Claim |
|---|---|---|---|
| Tier 1 | positive | positive | spatial structure shapes both local and population-level outcomes |
| Tier 2 | positive | mixed | local response exists, network transfer is selective |
| Tier 3 | mixed | positive | indirect or delayed population-level coupling |
| Tier 4 | negative | negative | current substrate does not support robust coupling |

---

## 17. Paper Series

### 17.1 Paper 1: main systems paper

Working title:

> Spatial-to-Social Network Mapping in LLM-Agent Populations: A Controlled Substrate

Contribution:

- system substrate
- condition design
- behavior-level and network-level hypotheses
- main experimental results
- robustness and downgrade analysis

### 17.2 Paper 2: economic geography reanalysis

Working focus:

- distance decay
- spatial homophily
- agglomeration-style regularities
- confound-reduced synthetic population tests

### 17.3 Paper 3: network-science reanalysis

Working focus:

- layout signatures
- brokerage transfer
- communication-network formation
- scaling across additional layouts

### 17.4 Optional representation probe paper

Working focus:

- whether agent behavior reveals implicit spatial maps
- whether internal representations can be reconstructed from trajectories, messages, and tie formation

---

## 18. Collaboration Structure

If a network-science collaborator is involved, the clean division of labor is:

| Domain | Li | Collaborator |
|---|---|---|
| simulation infrastructure | lead | review |
| layout design and spatial metrics | lead | advise |
| prompt and condition design | lead | review |
| network construction protocols | review | lead |
| network metrics and null models | review | lead |
| QAP or MRQAP analysis | review | lead |
| behavior-level analysis | lead | advise |
| network-level analysis | joint | joint |
| paper 1 writing | lead | second author |
| paper 2 writing | second author | lead |
| paper 3 writing | joint | joint |

Decision rights:

- simulation design, prompt content, and condition definitions: Li final call
- network definitions, null models, and network statistics: collaborator final call if formally onboarded
- preregistered hypotheses and paper sequencing: joint sign-off

---

## 19. Main Risks and Anti-Patterns

Avoid:

- reporting network metrics without null models
- treating co-occurrence as intentional social tie without evidence
- aggregating all network types into one social network too early
- overclaiming from one layout
- treating path-dependent contrasts as additive causal decomposition
- claiming that macro-network structure proves internal spatial understanding
- mixing survey anchor evidence and widened bridge evidence without marking the difference

The paper should consistently say:

> We measure coupling between controlled spatial structure and emergent social structure. We do not claim direct validation of human theory in synthetic populations.

---

## 20. Open Design Questions

Freeze these before Stage 2:

1. What threshold defines a co-occurrence tie?
2. Are dialogue and diffusion networks directed, symmetrized, or both?
3. What is the primary null model for H1n?
4. Does H2n use topological distance, Euclidean distance, or both?
5. Do `Bridge` and `Irregular` enter paper 1 or remain follow-on layouts?
6. Does `C_isolated` block all inter-agent communication or only direct dialogue?
7. What Layer 2 power threshold is required for confirmatory language?
8. Which network-construction protocol is treated as primary if protocols disagree?

---

## 21. Execution Checklist

### 21.1 Immediate planning

- [ ] Freeze the research question wording.
- [ ] Freeze the interpretation boundary.
- [ ] Decide which strong-version conditions enter the MVP.
- [ ] Decide whether `C_isolated` and `C_random_layout` are Stage 2 or Stage 3 only.
- [ ] Decide the paper-series sequencing.

### 21.2 Before coding

- [ ] Create `v12_conditions.yaml`.
- [ ] Create `exp_v12_main.yaml`.
- [ ] Freeze `v12_output_schema.md`.
- [ ] Freeze `v12_network_schema.md`.
- [ ] Freeze co-occurrence, dialogue, diffusion, and exposure-network rules.

### 21.3 Before Stage 1

- [ ] Implement the micro-task generator.
- [ ] Include `C6m_neutral` in the minimum Stage 1 condition set.
- [ ] Run lexical leakage and reverse-inference audits.
- [ ] Define Stage 1 result tables.

### 21.4 Before Stage 2

- [ ] Implement `run_v12.py`.
- [ ] Implement `v12_metrics.py`.
- [ ] Implement network construction and null-model modules.
- [ ] Run behavior-layer power simulation.
- [ ] Run network-layer power simulation.
- [ ] Pass the network-sanity pilot.

### 21.5 Before results writing

- [ ] Separate behavior and network confirmatory families.
- [ ] Report null models for every network claim.
- [ ] Apply downgrade rules.
- [ ] Keep follow-on paper claims separate from paper 1 claims.

---

## 22. Final Positioning

The clean v12 claim is:

> Controlled spatial topology can be used as an experimental substrate for measuring how LLM-agent populations convert spatial structure into behavior and social-network structure.

The most important result is not simply whether space matters.

The important result is:

> which spatial representations matter, at which analytical layer, under which null models, and whether emergent social networks inherit, transform, or decouple from the structure of the spatial substrate.

This makes the project a controlled measurement program, not a one-effect demonstration.
