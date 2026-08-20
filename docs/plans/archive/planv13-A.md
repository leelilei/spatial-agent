# SpatialAgent Research Plan v13-A

## Do LLM Agents Use Spatial Structure? A Controlled Multi-Agent Evaluation via Emergent Dialogue Networks

> Version: 13-A  
> Date: 2026-05-15  
> Lead author: Li  
> Target venue: AAAI main track  
> Status: standalone AAAI-oriented research plan

---

## 0. One-Line Version

This paper introduces a controlled evaluation protocol for testing whether LLM-based multi-agent systems use spatial structure in ways that transfer into emergent dialogue networks.

The core AAAI-facing question is:

> Do LLM agents actually use environment structure, or do apparent spatial-social effects arise from prompt richness, semantic labels, encounter opportunity, or evaluator artifacts?

The paper is framed as an AI evaluation and mechanism-identification study for LLM multi-agent systems.

---

## 1. AAAI Framing

LLM-agent systems increasingly place agents in simulated environments, towns, maps, games, workflows, and graph-structured worlds. These systems often assume that agents can use environment structure, but the assumption is rarely tested under controlled conditions.

This paper asks whether LLM agents transform spatial representations into measurable multi-agent behavior:

```text
environment graph
-> agent-facing spatial representation
-> local interaction behavior
-> emergent dialogue network
```

The AI contribution is not that a particular map produces a particular social pattern. The contribution is a reusable protocol for evaluating whether LLM-based multi-agent systems are representation-sensitive, mechanism-identifiable, and robust to matched controls.

The central claim is:

> LLM-based multi-agent systems exhibit measurable representation-sensitive spatial-to-social coupling, and this coupling can be evaluated under matched controls, null models, and downgrade rules.

---

## 2. Research Gap

Most current LLM-agent studies treat spatial environments as simulation context, narrative scaffolding, or task background. They rarely isolate whether agents use spatial structure as an input to behavior.

This leaves three open AI-system questions:

1. Do LLM agents respond to configurational information when it is exposed in a controlled environment?
2. Do local responses aggregate into system-level interaction structure?
3. Can these effects be separated from prompt verbosity, semantic affordances, co-location exposure, and evaluation artifacts?

This plan turns those questions into a benchmarkable evaluation design.

---

## 3. Evaluation Object

The primary evaluation object is:

```text
F: spatial representation -> emergent dialogue network
```

The protocol measures whether a matched population of LLM agents produces different interaction networks when the underlying graph is held constant but the agent-facing representation changes.

The key distinction is:

```text
same agents
same goals
same initial states
same graph
same information volume
different availability or correctness of spatial configurational information
```

This design targets mechanism identification rather than only phenomenon description.

---

## 4. Contributions

### 4.1 Evaluation contribution

We introduce a controlled protocol for testing whether LLM agents use spatial configurational information in multi-agent environments.

The protocol specifies:

- matched graph-based environments
- representation conditions
- rule-based social-event extraction
- primary dialogue-network construction
- null models for network claims
- downgrade rules for ambiguous results
- reproducible run outputs

### 4.2 Causal-identification contribution

We separate spatial representation effects from confounds that commonly affect LLM-agent simulations:

- prompt richness
- semantic leakage
- information volume
- co-location exposure
- shuffled metric-location mappings
- evaluator access to spatial descriptors

The paper treats these as first-class identification threats rather than appendix-only concerns.

### 4.3 Empirical contribution

We test when and how spatial representation transfers into:

- local social interaction
- agent-level dialogue centrality
- dyadic tie formation

The strongest AAAI result requires network-level evidence, not only local behavior differences.

---

## 5. Primary Research Question

> Do LLM agents use spatial configurational structure in a way that measurably affects emergent multi-agent interaction networks?

Operationally:

> Under matched graph, agent, seed, task, and information-volume controls, does access to correctly mapped spatial configurational information increase local social interaction, predict dialogue-network centrality, and produce topological distance decay in tie formation?

---

## 6. Primary Hypotheses

The paper has exactly three confirmatory hypotheses.

### H1: Local interaction

High-integration locations produce more social interaction.

| Field | Specification |
|---|---|
| Unit | run x location |
| Primary response | social-event rate |
| Primary predictor | location `integration_z` |
| Expected direction | positive |
| Main contrast | configurational perception vs topology-only |

H1 is necessary but not sufficient for an AAAI-strength claim. If only H1 succeeds, the paper should be framed as a pilot evaluation rather than a strong systems result.

### H2: Agent centrality

Agents exposed to high-integration locations become more central in the dialogue network.

| Field | Specification |
|---|---|
| Unit | run x agent |
| Primary response | dialogue-network weighted degree or strength |
| Primary predictor | exposure-weighted mean `integration_z` |
| Required control | co-occurrence exposure |
| Expected direction | positive |

H2 is the most important AAAI hypothesis because it shows that representation-sensitive behavior aggregates into a system-level multi-agent property.

### H3: Dyadic tie formation

Dialogue tie probability decreases with topological distance.

| Field | Specification |
|---|---|
| Unit | run x dyad |
| Primary response | dialogue tie present or edge weight |
| Primary predictor | topological distance between visited-location profiles |
| Required method | QAP, MRQAP, or run-level coefficient aggregation |
| Expected direction | negative |

H3 tests whether spatial structure shapes pairwise interaction beyond individual centrality.

---

## 7. Experimental Conditions

### 7.1 Main condition ladder

| Paper-facing name | Internal key | Purpose | AAAI interpretation |
|---|---|---|---|
| Topology-only | `C1` | baseline | agents move on the graph but receive no explicit configurational descriptors |
| Non-spatial control | `C2c` | information-volume control | agents receive matched descriptor volume without spatial meaning |
| Configurational perception | `C6m` | main treatment | agents receive correctly mapped integration, depth, and control descriptors |
| Shuffled mapping | `C_shuffle` | mechanism control | agents receive the same spatial descriptors assigned to incorrect locations |

The decisive contrast is:

```text
C6m > C2c and C6m > C_shuffle
```

If this contrast fails, the paper cannot claim robust spatial-representation use.

### 7.2 Demonstration condition

| Paper-facing name | Internal key | Role |
|---|---|---|
| Full SpatialAgent | `C4` | secondary system demonstration, not the primary causal identification condition |

`C4` is intentionally not the main treatment because it combines multiple mechanisms. It can demonstrate the full system after the controlled evaluation has established what can and cannot be attributed to representation.

### 7.3 Robustness conditions

At least one robustness condition is required for an AAAI submission.

| Robustness condition | Internal key | Purpose |
|---|---|---|
| Neutral numeric descriptors | `C6m_neutral` | tests whether effects require spatial vocabulary |
| Alternate LLM model | `model_alt` | tests whether effects are model-specific |
| Counter-semantic labels | `C_counter` | tests whether semantic labels override structure |
| Judge-only access | `C_judge_only` | tests evaluator-artifact risk |
| Rule scorer | `C_rule_scorer` | tests non-LLM scoring robustness |

Minimum AAAI recommendation:

```text
Run either C6m_neutral or model_alt in addition to the four main conditions.
```

---

## 8. Maps

The main evaluation uses three controlled layouts.

| Map | Purpose |
|---|---|
| `Plaza` | high-integration convergence case |
| `Grid` | regular topology control |
| `Labyrinth` | high-depth separation case |

Map inclusion requirements:

- connected graph
- sufficient variance in integration, depth, and control
- no isolated required node
- enough visits per location in pilot runs
- labels pass lexical leakage checks
- spatial metrics are frozen before confirmatory runs

Additional maps should not be added to the main paper unless the three-map protocol is already powered and stable.

---

## 9. Primary Network and Observables

### 9.1 Primary social network: dialogue network

All confirmatory social-network claims use the dialogue network.

Definition:

- node = agent
- edge = observed dialogue interaction
- edge weight = number of dialogue turns or dialogue events
- default graph = undirected weighted graph
- optional appendix graph = directed graph by turn initiation

Why dialogue is primary:

- it is directly social
- it is observable from logs
- it avoids conflating co-presence with interaction
- it supports system-level network metrics

### 9.2 Required exposure control: co-occurrence network

The co-occurrence network is not the primary social network.

Definition:

- node = agent
- edge weight = number of rounds in which two agents share a location

Use:

- controls for encounter opportunity
- distinguishes dialogue effects from shared exposure
- helps answer the AAAI concern that results are only movement or collision artifacts

### 9.3 Spatial-exposure network

Definition:

- bipartite graph between agents and locations
- edge weight = visits, dwell time, or action count

Use:

- computes exposure-weighted integration
- supports H2
- supports null models that permute exposure profiles

### 9.4 Exploratory diffusion network

The diffusion network is optional and exploratory.

It should only be reported if information-token propagation can be detected with strict evidence thresholds. It is not needed for the AAAI main claim.

---

## 10. Event Coding

Event coding is treated as a core validity component.

### 10.1 Primary event definition

The primary social event should be rule-based:

```text
social_event = observed dialogue interaction between two agents in a recorded round and location
```

Required fields:

```text
round, agent_id, target_id, location, event_type, event_text, event_source
```

Allowed primary event types:

```text
social, other
```

Secondary semantic labels may include:

```text
privacy, gatekeeping
```

These secondary labels are not part of the primary AAAI claim.

### 10.2 LLM judge policy

If an LLM judge is used:

- the judge must be blind to condition
- location descriptors should be removed or sanitized where possible
- the judge prompt must be frozen
- the judge model and version must be recorded
- judge-only artifact checks should be reported if feasible

### 10.3 Human validation subset

A small validation subset is recommended:

- sample across maps, conditions, and seeds
- code whether dialogue ties and social events are valid
- compare rule-based coding, LLM judge coding, and human labels

This is a credibility enhancer, not a required primary endpoint.

---

## 11. Reusable Benchmark Protocol

The AAAI version should be packaged as a reusable evaluation protocol.

### 11.1 Protocol inputs

```text
graph layout
spatial metrics
agent profiles
task and goal templates
condition definitions
random seed
LLM model configuration
```

### 11.2 Protocol outputs

```text
visit logs
dialogue logs
event logs
network files
network metrics
run metadata
null-model outputs
analysis tables
```

### 11.3 Required output schema

Each run should write:

```text
results/planv13-A/{map}/{seed}/{condition}/metadata.json
results/planv13-A/{map}/{seed}/{condition}/visits.csv
results/planv13-A/{map}/{seed}/{condition}/events.csv
results/planv13-A/{map}/{seed}/{condition}/messages.jsonl
results/planv13-A/{map}/{seed}/{condition}/network_dialogue.graphml
results/planv13-A/{map}/{seed}/{condition}/network_cooccurrence.graphml
results/planv13-A/{map}/{seed}/{condition}/network_spatial_exposure.graphml
results/planv13-A/{map}/{seed}/{condition}/network_metrics.json
results/planv13-A/{map}/{seed}/{condition}/nulls.json
```

### 11.4 Reproducibility promise

The paper should release or document:

- condition templates
- map files
- spatial metric computation scripts
- event extraction rules
- network construction scripts
- analysis notebooks or scripts
- seed list
- downgrade-rule checklist

This is important for AAAI because reusable evaluation infrastructure is more compelling than a one-off social simulation.

---

## 12. Experimental Design

### 12.1 Run definition

```text
run = map x seed x condition
```

The run is the primary independent unit.

### 12.2 MVP design

```text
3 maps x 10 seeds x 4 main conditions = 120 runs
```

Main conditions:

```text
C1, C2c, C6m, C_shuffle
```

### 12.3 AAAI robustness extension

At least one extension should be included:

```text
3 maps x 10 seeds x 1 robustness condition = 30 additional runs
```

Preferred options:

```text
C6m_neutral
model_alt
```

Recommended total:

```text
150 runs
```

Optional system demonstration:

```text
3 maps x 10 seeds x C4 = 30 additional runs
```

The demonstration is useful only after the controlled protocol is complete.

---

## 13. Stages

### Stage 0: Preflight

Required checks:

- spatial metric sanity
- graph connectivity
- descriptor comprehension
- lexical leakage audit
- reverse-inference audit
- event extraction pilot
- dialogue-network non-degeneracy pilot
- matched-seed reproducibility check

Exit rule:

```text
Do not run confirmatory simulations until all required checks pass.
```

### Stage 1: Micro-task validation

Purpose:

```text
test whether agents can use configurational information in a controlled single-step task
```

Required contrast:

```text
C6m > C1
C6m > C2c
C6m > C_shuffle
```

If Stage 1 fails, Stage 2 should be reframed as exploratory debugging rather than confirmatory evaluation.

### Stage 2: Long-run multi-agent evaluation

Purpose:

```text
test whether local representation sensitivity aggregates into emergent dialogue networks
```

Primary outputs:

- H1 local interaction effect
- H2 dialogue centrality effect
- H3 dyadic tie effect
- co-occurrence exposure controls
- null-model comparisons

### Stage 3: Robustness and packaging

Purpose:

```text
show the result is not a one-off prompt, judge, or model artifact
```

Minimum:

- one robustness condition
- rule-based event extraction
- blinded judge or human validation subset
- reusable benchmark artifact list

---

## 14. Statistical Plan

### 14.1 Independence and pseudo-replication

The run is the primary independent unit.

Agents, locations, dyads, and time windows are nested within runs. Dyadic rows must not be treated as independent samples in a simple logistic model.

### 14.2 H1 model

For each run and location:

```text
social_event_rate = social events at location / visits to location
```

For each run:

```text
rho_run = SpearmanCorr(social_event_rate, integration_z)
tar_h1_run = FisherZ(rho_run)
```

Primary comparison:

```text
tar_h1_run ~ condition + map + condition:map + (1|seed)
```

### 14.3 H2 model

For each agent:

```text
exposure_weighted_integration =
  weighted mean of visited-location integration_z
```

Primary response:

```text
dialogue-network weighted degree or strength
```

Required control:

```text
co-occurrence exposure
```

Recommended model:

```text
network_centrality ~ exposure_weighted_integration + cooccurrence_exposure + condition + map + nested run effects
```

Confirmatory inference should aggregate effects at the run level or use clustered uncertainty.

### 14.4 H3 model

Primary response:

```text
dialogue tie present or dialogue edge weight
```

Primary predictor:

```text
topological distance between agents' visited-location profiles
```

Allowed methods:

- QAP
- MRQAP
- run-level dyadic coefficient aggregation
- permutation at run or seed level

The main text should explicitly state how dyadic dependence is handled.

### 14.5 Multiple comparisons

Confirmatory family:

```text
H1, H2, H3
```

Control:

```text
FDR within the confirmatory family
```

Exploratory analyses are reported separately.

---

## 15. Null Models

Every network claim requires a null model.

| Claim | Null model |
|---|---|
| H1 local interaction alignment | shuffled metric-location mapping |
| H2 centrality from exposure | permuted agent exposure profiles |
| H3 distance decay | shuffled location-pair distances |
| dialogue-network structure | degree-preserving rewiring |
| co-occurrence robustness | spatial-exposure baseline |
| semantic-label robustness | neutral numeric descriptors or counter-semantic labels |

The main null-model question is:

> Would the claimed effect remain if the same graph, agents, interaction volume, and network density were preserved but the spatial mapping were broken?

---

## 16. Power and SESOI

Power must be simulated before confirmatory Stage 2.

### 16.1 Smallest effect sizes of interest

Proposed SESOI:

| Endpoint | SESOI |
|---|---|
| H1 local interaction | `Delta FisherZ >= 0.25` between `C6m` and controls |
| H2 centrality | standardized slope `>= 0.25` for exposure-weighted integration after co-occurrence control |
| H3 dyadic tie formation | odds ratio `<= 0.80` per topological step |

### 16.2 Power target

Minimum:

```text
80% power for H1 and H2
```

Desired:

```text
80% power for H1, H2, and H3
```

If H2 is underpowered, the AAAI submission should not overclaim system-level evidence.

---

## 17. AAAI Minimum Success Criteria

The project should target AAAI only if these conditions are met:

1. H2 is positive: exposure-weighted integration predicts dialogue-network centrality.
2. H2 remains meaningful after controlling for co-occurrence exposure.
3. `C6m` is stronger than both `C2c` and `C_shuffle`.
4. At least one robustness check succeeds, preferably neutral descriptors or an alternate LLM.
5. The code, data schema, condition templates, and analysis scripts are packaged as a reusable evaluation protocol.

If these are not met, the paper may still be valuable, but the AAAI framing should be softened to a diagnostic benchmark or pilot study.

---

## 18. Downgrade Rules

| Pattern | Downgrade |
|---|---|
| `C2c` matches `C6m` | information-volume or descriptor-format effect |
| `C_shuffle` matches `C6m` | mapping-insensitive prompt effect |
| H1 positive but H2 negative | local behavior does not aggregate into system-level network structure |
| H2 disappears after co-occurrence control | encounter-opportunity effect |
| H3 disappears under QAP or run-level aggregation | no confirmatory dyadic distance-decay claim |
| rule-based extraction fails but LLM judge succeeds | possible evaluator artifact |
| alternate model fails completely | model-specific result, not general LLM-agent claim |
| neutral descriptors fail while spatial labels succeed | semantic-affordance effect |

These downgrade rules should be preregistered before the main run.

---

## 19. Expected Result Tiers

| Tier | H1 | H2 | H3 | AAAI-facing interpretation |
|---|---|---|---|---|
| Tier 1 | positive | positive | positive | strong evidence that LLM multi-agent systems use spatial structure in local and network-level interaction |
| Tier 2 | positive | positive | mixed | strong system-level evidence, with weaker dyadic mechanism |
| Tier 3 | positive | negative | mixed | agents show local sensitivity but not emergent network coupling |
| Tier 4 | negative | negative | negative | the protocol identifies a boundary condition for current LLM-agent spatial reasoning |

Tier 1 or Tier 2 is the target for AAAI.

Tier 3 can still be useful if framed as an evaluation protocol exposing a failure mode.

---

## 20. Implementation Binding

### 20.1 Configs

| Artifact | Proposed path |
|---|---|
| condition definitions | `spatial-agent-core/configs/experiments/planv13_A_conditions.yaml` |
| main experiment config | `spatial-agent-core/configs/experiments/exp_planv13_A_main.yaml` |
| robustness config | `spatial-agent-core/configs/experiments/exp_planv13_A_robustness.yaml` |

### 20.2 Runners and analysis modules

| Artifact | Proposed path | Responsibility |
|---|---|---|
| run launcher | `spatial-agent-core/experiments/run_planv13_A.py` | execute map x seed x condition runs |
| event extraction | `spatial-agent-core/src/analysis/event_extraction.py` | rule-based social-event extraction |
| network construction | `spatial-agent-core/src/analysis/network_construction.py` | dialogue, co-occurrence, and exposure networks |
| network metrics | `spatial-agent-core/src/analysis/network_metrics.py` | centrality and graph summaries |
| hypothesis tests | `spatial-agent-core/src/analysis/planv13_A_hypotheses.py` | H1, H2, H3 tests |
| null models | `spatial-agent-core/src/analysis/network_nulls.py` | rewiring, shuffling, exposure permutation |
| power simulation | `spatial-agent-core/src/analysis/planv13_A_power.py` | SESOI and power checks |

### 20.3 Documentation

| Document | Proposed path |
|---|---|
| benchmark card | `spatial-agent-core/docs/planv13_A_benchmark_card.md` |
| output schema | `spatial-agent-core/docs/planv13_A_output_schema.md` |
| condition manual | `spatial-agent-core/docs/planv13_A_condition_manual.md` |
| event coding manual | `spatial-agent-core/docs/planv13_A_event_coding.md` |
| preregistration draft | `spatial-agent-core/docs/planv13_A_preregistration.md` |

---

## 21. AAAI Paper Structure

```text
1. Introduction
   - LLM multi-agent systems assume agents use environment structure.
   - Existing evaluations rarely isolate representation-sensitive mechanism use.
   - This paper introduces a controlled protocol using emergent dialogue networks.

2. Related Work
   - LLM agents and multi-agent simulations
   - Environment representations in agents
   - Evaluation of LLM-agent behavior
   - Network-based analysis of multi-agent interaction

3. Evaluation Protocol
   - graph substrate
   - conditions
   - maps
   - run schema
   - event extraction
   - dialogue-network construction

4. Identification Strategy
   - matched controls
   - information-volume control
   - shuffled mapping
   - co-occurrence exposure control
   - null models
   - downgrade rules

5. Experiments
   - Stage 0 preflight
   - Stage 1 micro-task validation
   - Stage 2 long-run multi-agent evaluation
   - Stage 3 robustness

6. Results
   - H1 local interaction
   - H2 dialogue centrality
   - H3 dyadic ties
   - robustness and null models

7. Discussion
   - what the protocol reveals about LLM multi-agent systems
   - when spatial representation is used
   - failure modes and limits

8. Conclusion
```

Appendix:

```text
A. Survey-derived motivation
B. Map and metric details
C. Prompt templates
D. Event extraction rules
E. Network construction details
F. Power analysis
G. Robustness conditions
H. Full reproducibility checklist
```

---

## 22. Reviewer Concerns and Responses

### Concern 1: This is social simulation, not AI.

Response:

> The paper contributes an evaluation protocol for LLM multi-agent systems: it tests whether agents use environment representations under matched controls and null models.

### Concern 2: The effect may be prompt richness.

Response:

> `C2c` matches information volume without spatial meaning, and `C_shuffle` preserves descriptors while breaking the mapping.

### Concern 3: The network effect may be co-location exposure.

Response:

> Dialogue network is primary, co-occurrence is modeled separately, and H2 must survive co-occurrence exposure control.

### Concern 4: Event labels may come from judge bias.

Response:

> Primary social events are rule-based dialogue interactions; LLM judging is blinded and secondary.

### Concern 5: Dyads are not independent.

Response:

> H3 uses QAP, MRQAP, run-level coefficient aggregation, or permutation at the run or seed level.

### Concern 6: Results may be model-specific.

Response:

> At least one robustness check uses either neutral descriptors or an alternate LLM model.

---

## 23. Execution Checklist

### Before implementation

- [ ] Freeze H1, H2, and H3.
- [ ] Freeze the four main conditions.
- [ ] Select one required robustness extension.
- [ ] Freeze the three MVP maps.
- [ ] Freeze the primary dialogue-network definition.
- [ ] Write the benchmark card.
- [ ] Write the output schema.

### Before Stage 1

- [ ] Implement condition templates.
- [ ] Implement descriptor comprehension checks.
- [ ] Implement lexical leakage audit.
- [ ] Implement reverse-inference audit.
- [ ] Implement rule-based event extraction.

### Before Stage 2

- [ ] Implement the run launcher.
- [ ] Implement dialogue-network construction.
- [ ] Implement co-occurrence exposure controls.
- [ ] Implement QAP or run-level dyadic analysis.
- [ ] Run power simulation.
- [ ] Freeze SESOI.

### Before writing

- [ ] Report H1, H2, and H3 before exploratory results.
- [ ] Report `C6m` vs `C2c` and `C_shuffle`.
- [ ] Report co-occurrence-controlled H2.
- [ ] Report null models for every network claim.
- [ ] Apply downgrade rules explicitly.
- [ ] Package code, schemas, and templates as reusable evaluation artifacts.

---

## 24. Final Positioning

The AAAI version should be positioned as:

> A controlled benchmark-style evaluation of whether LLM-based multi-agent systems use spatial representations, measured through emergent dialogue networks and validated with matched controls, null models, and downgrade rules.

The strongest paper is not:

```text
space shapes social networks in agents
```

The strongest paper is:

```text
we can evaluate and identify when LLM multi-agent systems transform environment representations into system-level interaction structure
```

This keeps the contribution squarely in AI: evaluation, mechanism identification, multi-agent behavior, and reproducible benchmark design.
