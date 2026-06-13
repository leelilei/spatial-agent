# SpatialAgent Research Plan v14-A

> 规范说明：本文件为当前 live 研究计划（proposal.md）。历史版本见 docs/plans/archive/。

## Environment Structure, Not Space Syntax as Agent Cognition

> Version: 14-A  
> Date: 2026-05-19  
> Lead author: Li  
> Target venue: AAAI main track / AAMAS main track, with ICWSM, CSCW, and network-science venues as alternatives  
> Status: standalone research plan, revised from v13-A after conceptual audit  
> Working title: **Identifying Environment-Structure Effects in LLM Multi-Agent Systems via Emergent Dialogue Networks**

---

## 0. One-Line Version

This paper tests whether LLM-based multi-agent systems transform **controlled environment structure** into measurable emergent dialogue networks, without treating space syntax metrics as the agents' own representation of space.

The core question is:

> When LLM agents interact in matched graph-based environments, do their movement, encounters, and dialogue networks align with externally measured spatial structure, and can this alignment be separated from prompt richness, semantic labels, co-location opportunity, and evaluator artifacts?

---

## 1. Major Change from v13-A

v13-A framed the work as:

```text
Do LLM agents use spatial configurational structure?
```

That framing was useful but too close to a conceptual trap:

```text
space syntax metric != space itself
```

Metrics such as `integration_z`, `depth_z`, and `control_z` are useful abstractions, but they are not the full lived, visual, semantic, embodied, or social experience of space. They should not be presented as the agent's natural cognitive representation of space.

v14-A therefore makes a decisive change:

> **Space syntax and graph metrics are researcher-side measurement and design instruments, not the primary agent-facing language.**

In v14-A, agents primarily see natural, local, action-oriented environment information:

```text
current location
neighboring locations
available actions
local objects
nearby agents
movement history
place affordances
optional natural spatial cues
```

Researchers separately compute spatial-configuration metrics in the background:

```text
graph accessibility / integration proxy
mean depth / average shortest path
betweenness / bridge score
local degree
control value
community / modularity position
optional space syntax measures if geometry supports them
```

The main paper no longer claims:

```text
LLM agents understand or use space syntax.
```

The main paper claims:

```text
LLM multi-agent behavior can be evaluated against controlled environment structure using external spatial metrics, matched controls, and dialogue-network outcomes.
```

---

## 2. Core Claim

The clean v14-A claim is:

> LLM multi-agent systems may convert controlled environment structure into emergent interaction networks through two separable channels: navigational exposure and representation-sensitive spatial cues. v14-A introduces a controlled protocol to identify which channel is active, using researcher-side spatial metrics, matched controls, dialogue-network construction, and null models.

This deliberately avoids saying:

> We put space syntax into agents.

Instead, the paper says:

> We use spatial metrics as an external scientific instrument for designing and analyzing environments, while agents receive only controlled environment information.

---

## 3. Why This Is Still a Real Problem

Generative-agent systems already include environments, maps, locations, objects, movement constraints, and local perception. The gap is not that prior systems lack space.

The gap is that prior systems rarely isolate whether environment structure becomes a measurable mechanism in multi-agent behavior.

The unresolved questions are:

1. Does graph-constrained navigation alone create spatially patterned interaction?
2. Do natural spatial cues add effects beyond mechanical co-location opportunity?
3. Do such effects aggregate into dialogue-network centrality and tie formation?
4. Can these effects be separated from prompt verbosity, semantic affordances, shuffled mappings, model artifacts, and evaluator bias?
5. Can we evaluate these questions without pretending that space syntax equals space?

This is the v14-A problem.

---

## 4. Positioning

### 4.1 What v14-A is

v14-A is:

- a controlled evaluation protocol for LLM multi-agent systems;
- a mechanism-identification study about environment structure;
- a dialogue-network analysis of emergent interaction;
- a design that separates environment mechanics from agent-facing representation;
- a paper that uses spatial metrics as external measurement, not agent cognition;
- a successor to v13-A with a stronger conceptual foundation.

### 4.2 What v14-A is not

v14-A is not:

- a paper claiming that space syntax fully represents space;
- a paper claiming that LLMs naturally reason in `integration_z`, `depth_z`, or `control_z`;
- a generic social simulation paper;
- a new generative-agent architecture paper;
- a pure map-design paper;
- a claim that any spatial effect must come from explicit prompt descriptors.

### 4.3 Relationship to v13-A

v13-A's useful elements remain:

```text
matched conditions
information-volume control
shuffled mapping control
co-occurrence exposure control
rule-based event extraction
QAP / run-level dyadic analysis
null models
downgrade rules
```

The main change is that direct metric descriptors are removed from the primary treatment.

Original v13-A:

```text
Configurational perception = agents receive explicit integration, depth, control descriptors.
```

Revised v14-A:

```text
Main treatment = agents receive local environment structure and/or natural spatial cues.
Researcher-side metrics are hidden and used for design, measurement, and hypothesis testing.
Direct metric descriptors are diagnostic only.
```

---

## 5. Conceptual Model

v14-A separates four layers that were partially conflated in earlier versions.

### 5.1 Environment structure

The actual substrate:

```text
locations
edges / adjacency
movement costs
objects
visibility or local perception
agent positions
interaction rules
```

### 5.2 Agent-facing environment information

What the agent is allowed to know:

```text
current location
neighboring locations
available movement options
nearby agents
local objects
natural place descriptions
optional natural spatial cues
```

### 5.3 Researcher-side spatial measurement

What the researcher computes but the agent does not necessarily see:

```text
accessibility / integration proxy
mean depth
betweenness
local degree
control value
community bridge position
space syntax metrics where appropriate
```

### 5.4 Emergent social outcome

What the system produces:

```text
visits
co-presence
dialogue events
dialogue network
agent centrality
dyadic ties
social-event locations
```

The key empirical question is not whether the agent can read a metric label. The key empirical question is whether outcomes in layer 5.4 align with structure in layer 5.1 and measurements in layer 5.3, under controlled variation in layer 5.2.

---

## 6. Primary Research Question

> Do LLM-based multi-agent systems transform controlled environment structure into emergent dialogue-network structure, and through which channel: mechanical exposure, natural spatial cues, or prompt/semantic artifacts?

Operational version:

> In matched graph environments with identical agents, goals, seeds, maps, and interaction rules, do researcher-measured structural properties of locations and paths predict visits, co-presence, dialogue events, agent-level dialogue centrality, and dyadic tie formation, after controlling for information volume, semantic labels, co-location exposure, and shuffled spatial mappings?

---

## 7. Research Questions

### RQ1: Environment exposure

> Does local graph-constrained navigation produce visit and co-presence patterns aligned with researcher-side spatial structure?

This tests whether environment mechanics alone generate spatial exposure effects.

### RQ2: Natural spatial cues

> Do natural spatial descriptions such as “many paths pass through here” or “this area is tucked away” change behavior beyond local topology alone?

This tests representation-sensitive use without using space syntax labels as agent language.

### RQ3: Dialogue-network aggregation

> Do local movement and encounter effects aggregate into agent-level dialogue centrality and non-degenerate dialogue networks?

This is the main AI-system question.

### RQ4: Dyadic tie formation

> Does topological distance or shared structural exposure predict dialogue tie formation after accounting for co-presence opportunity?

This tests whether spatial structure shapes pairwise social relations.

### RQ5: Identification and robustness

> Can observed effects be distinguished from information volume, prompt richness, semantic affordances, shuffled mappings, evaluator artifacts, and model-specific behavior?

---

## 8. Primary Hypotheses

v14-A keeps three confirmatory hypotheses, but reframes them around external structure and channel identification.

### H1: Local exposure alignment

Structurally accessible locations receive more visits, co-presence, and social-event opportunities.

| Field | Specification |
|---|---|
| Unit | run x location |
| Primary response | visit rate and co-presence rate |
| Primary predictor | researcher-side accessibility / integration proxy |
| Expected direction | positive |
| Main contrast | local topology and natural spatial cues vs non-spatial control |
| Interpretation | environment structure shapes exposure opportunity |

Important note:

> H1 is not yet a strong social-network claim. It shows spatial exposure alignment, not necessarily dialogue-network transformation.

### H2: Dialogue-network centrality

Agents exposed to structurally accessible locations become more central in the dialogue network.

| Field | Specification |
|---|---|
| Unit | run x agent |
| Primary response | dialogue-network weighted degree / strength |
| Primary predictor | exposure-weighted researcher-side accessibility |
| Required control | co-presence exposure / encounter opportunity |
| Expected direction | positive |
| Interpretation | local spatial exposure aggregates into system-level interaction structure |

H2 is the most important hypothesis for the main paper.

### H3: Dyadic tie formation

Dialogue tie probability decreases with topological distance and/or increases with shared structural exposure.

| Field | Specification |
|---|---|
| Unit | run x dyad |
| Primary response | dialogue tie present or dialogue edge weight |
| Primary predictor | topological distance between visited-location profiles; shared structural exposure |
| Required method | QAP, MRQAP, run-level coefficient aggregation, or permutation |
| Expected direction | distance negative; shared exposure positive |
| Interpretation | environment structure shapes pairwise social ties |

---

## 9. Experimental Conditions

### 9.1 Main condition ladder

The main conditions are redesigned so that direct space syntax metrics are not the primary agent-facing treatment.

| Paper-facing name | Internal key | Agent-facing information | Role |
|---|---|---|---|
| Flat semantic world | `V14_C0_flat` | locations and semantic labels, but no meaningful graph constraints | sanity baseline |
| Local topology | `V14_C1_local` | current location, neighbors, movement options, local objects, nearby agents | main environment-mechanics baseline |
| Non-spatial matched information | `V14_C2_nonspatial` | same amount/format of extra information, but non-spatial and behaviorally neutral | information-volume control |
| Natural spatial cues | `V14_C3_natural` | local topology plus natural spatial cues derived from hidden structure | main representation treatment |
| Shuffled natural cues | `V14_C4_shuffle` | same natural cues assigned to incorrect locations | mechanism control |

The decisive representation-sensitive contrast is:

```text
V14_C3_natural > V14_C2_nonspatial
and
V14_C3_natural > V14_C4_shuffle
```

The decisive environment-mechanics contrast is:

```text
V14_C1_local > V14_C0_flat
```

The most important network-level contrast is:

```text
H2 remains positive under V14_C3_natural after co-presence exposure control.
```

### 9.2 Diagnostic-only conditions

These conditions are useful but should not carry the main claim.

| Paper-facing name | Internal key | Purpose | Status |
|---|---|---|---|
| Direct metric descriptors | `V14_D1_metrics` | agents receive `integration`, `depth`, `control`, or normalized graph values | diagnostic / appendix |
| Neutral numeric descriptors | `V14_D2_numeric` | agents receive metric-like numbers without spatial vocabulary | semantic-leakage audit |
| Counter-semantic labels | `V14_D3_counter` | spatial cues conflict with semantic place labels | semantic dominance audit |
| Alternate LLM model | `V14_D4_model_alt` | tests model specificity | robustness |
| Judge-only spatial info | `V14_D5_judge_only` | tests evaluator artifact risk | robustness |

Rule:

> `V14_D1_metrics` can show that LLMs can respond to explicit spatial abstractions, but it cannot by itself prove that agents use space.

### 9.3 Preferred MVP design

Core MVP:

```text
3 maps x 10 seeds x 4 conditions = 120 runs
```

Recommended four conditions:

```text
V14_C1_local
V14_C2_nonspatial
V14_C3_natural
V14_C4_shuffle
```

Optional sanity baseline:

```text
3 maps x 10 seeds x V14_C0_flat = 30 runs
```

Optional diagnostic:

```text
3 maps x 10 seeds x V14_D1_metrics = 30 runs
```

Recommended full v14-A package:

```text
120 main runs
+ 30 flat/sanity runs
+ 30 diagnostic or robustness runs
= 180 runs
```

If resources are limited, run the 120-run MVP first.

---

## 10. Maps

The main paper uses three controlled maps, but their role is reframed.

| Map | Purpose |
|---|---|
| `Plaza` | high-accessibility convergence case |
| `Grid` | regular topology control |
| `Labyrinth` | high-depth / separation case |

Map inclusion requirements:

- connected graph;
- no isolated required location;
- enough variance in researcher-side accessibility, depth, and bridge measures;
- enough visits per location in pilot runs;
- lexical labels do not trivially imply centrality or social desirability;
- hidden metrics are frozen before confirmatory runs;
- map semantics are balanced across central and peripheral locations.

Deferred maps:

```text
Bridge
Irregular
Multi-level building
Visibility-heavy layout
```

These should remain appendix or follow-on unless the main design is stable.

---

## 11. Agent-Facing Environment Representation

### 11.1 Default local prompt representation

In `V14_C1_local`, the agent sees only local, action-relevant information:

```text
You are at: Cafe
Nearby places you can go next: Plaza, Market, Alley
Visible objects: counter, tables, bulletin board
Nearby agents: Maria, Klaus
Recent local events: Maria entered Cafe five minutes ago
Your current goal: buy coffee before meeting Sam
```

No hidden graph metrics are visible.

### 11.2 Natural spatial cue representation

In `V14_C3_natural`, the agent may see natural spatial cues:

```text
This place connects several routes and is often passed through.
This place is tucked away and usually reached after passing through other areas.
This place is a narrow connector between two parts of town.
```

Allowed natural cue principles:

- no metric names;
- no normalized scores;
- no direct claim that a place is socially important;
- no words such as “high integration” or “centrality”;
- cues should describe spatial experience, not expected social outcome.

### 11.3 Bad agent-facing representation

The main condition should not use:

```text
Cafe has integration_z = 1.42, depth_z = -0.73, control_z = 0.88.
```

This belongs only in diagnostic conditions.

---

## 12. Researcher-Side Metrics

v14-A allows spatial metrics, but places them on the researcher side.

### 12.1 Primary structural metric

Freeze one primary structural metric before confirmatory runs.

Recommended primary metric:

```text
accessibility_z = standardized inverse mean shortest-path distance
```

This is easier to explain to AI reviewers than a specialized space syntax term.

Optional equivalent:

```text
integration_z
```

Only use `integration_z` as the primary label if the paper has enough space to explain the space syntax abstraction carefully.

### 12.2 Secondary structural metrics

Secondary metrics:

```text
depth_z
betweenness_z
control_z
local_degree_z
bridge_score_z
community_boundary_score
```

These are used for robustness and interpretation, not for multiplying primary claims.

### 12.3 Metric policy

The paper must state:

> These metrics do not exhaust what space is. They operationalize selected structural properties of the environment graph for experimental control and analysis.

---

## 13. Primary Networks and Observables

### 13.1 Visit distribution

Definition:

```text
agent x round x location
```

Use:

- movement alignment;
- exposure computation;
- denominator for local social-event rates.

### 13.2 Co-presence network

Definition:

```text
nodes = agents
edge weight = number of rounds two agents share a location
```

Use:

- encounter opportunity control;
- mechanism check;
- not the primary social network.

### 13.3 Dialogue network

Definition:

```text
nodes = agents
edge = observed dialogue interaction
edge weight = number of dialogue events or turns
```

This remains the primary social network.

Why:

- dialogue is directly social;
- it is observable from logs;
- it avoids treating mere co-location as social tie;
- it supports centrality and dyadic tie analysis.

### 13.4 Spatial-exposure network

Definition:

```text
bipartite graph between agents and locations
edge weight = visits, dwell time, or actions
```

Use:

- computes exposure-weighted structural metrics;
- supports H2;
- supports null models.

### 13.5 Exploratory diffusion network

Optional only.

Use only if information tokens can be traced with strict evidence thresholds.

---

## 14. Event Coding

### 14.1 Primary social event definition

Primary social event should be rule-based:

```text
social_event = observed dialogue interaction between two agents in a recorded round and location
```

Required fields:

```text
round
agent_id
target_id
location
event_type
event_text
event_source
dialogue_id
```

Allowed primary event types:

```text
social
other
```

Secondary semantic labels such as privacy, gatekeeping, or information handoff are exploratory.

### 14.2 LLM judge policy

If an LLM judge is used:

- the judge must be blind to condition;
- hidden spatial metrics must be removed;
- natural spatial cues should be sanitized when judging social-event validity;
- judge model and prompt must be frozen;
- judge-only artifact checks should be reported if feasible.

### 14.3 Human validation subset

Recommended but not mandatory:

```text
sample across maps x conditions x seeds
validate dialogue tie presence
validate social-event location
compare rule extraction, LLM judge, and human labels
```

---

## 15. Statistical Plan

### 15.1 Independent unit

The primary independent unit is the run.

```text
run = map x seed x condition
```

Agents, dyads, locations, and time windows are nested within runs.

Do not treat raw dyads or events as independent samples without dependence-aware modeling.

### 15.2 H1 model: local exposure alignment

For each run and location:

```text
visit_rate = visits_to_location / total_visits_in_run
copresence_rate = copresence_rounds_at_location / visits_to_location
```

Primary run-level statistic:

```text
rho_visit_run = SpearmanCorr(visit_rate, accessibility_z)
rho_copresence_run = SpearmanCorr(copresence_rate, accessibility_z)
```

Transform:

```text
tar_h1_visit = FisherZ(rho_visit_run)
tar_h1_copresence = FisherZ(rho_copresence_run)
```

Primary model:

```r
tar_h1_visit ~ condition + map + condition:map + (1|seed)
```

Secondary:

```r
tar_h1_copresence ~ condition + map + condition:map + (1|seed)
```

### 15.3 H2 model: dialogue centrality

For each agent in each run:

```text
exposure_weighted_accessibility = weighted mean of visited-location accessibility_z
co_presence_exposure = number of co-presence opportunities
network_strength = weighted degree in dialogue network
```

Recommended model:

```text
network_strength ~ exposure_weighted_accessibility
                 + co_presence_exposure
                 + condition
                 + map
                 + nested run effects
```

Confirmatory inference should aggregate coefficients at the run level or use clustered uncertainty by run.

The strongest H2 result is:

```text
exposure_weighted_accessibility remains positive after co_presence_exposure control,
and the effect is stronger in V14_C3_natural than V14_C2_nonspatial and V14_C4_shuffle.
```

### 15.4 H3 model: dyadic tie formation

For each run, construct matrices:

```text
Y_dialogue_tie
X_topological_distance
X_shared_location_exposure
X_shared_accessibility_exposure
X_co_presence
```

Allowed methods:

- QAP;
- MRQAP;
- run-level dyadic coefficient aggregation;
- permutation at run or seed level.

Confirmatory interpretation requires dependence-aware inference.

### 15.5 Multiple comparisons

Confirmatory family:

```text
H1
H2
H3
```

Control:

```text
FDR within the confirmatory family
```

Exploratory analyses are reported separately.

---

## 16. Null Models

Every network claim requires a null model.

| Claim | Null model |
|---|---|
| H1 local exposure alignment | shuffled metric-location mapping |
| H2 centrality from exposure | permuted agent exposure profiles within run |
| H3 dyadic tie formation | shuffled location-pair distances or QAP permutations |
| dialogue-network structure | degree-preserving rewiring |
| natural cue mechanism | shuffled natural-cue mapping |
| information-volume control | non-spatial matched descriptors |
| co-location artifact | co-presence network as exposure baseline |

Main null-model question:

> Would the claimed effect remain if graph, agents, interaction volume, and network density were preserved, but the mapping between environment structure and social outcome were broken?

---

## 17. Power and SESOI

Power must be simulated before confirmatory runs.

### 17.1 Proposed SESOI

| Endpoint | SESOI |
|---|---|
| H1 visit alignment | Delta FisherZ >= 0.25 between `V14_C3_natural` and controls |
| H2 centrality | standardized slope >= 0.25 after co-presence control |
| H3 dyadic tie | odds ratio <= 0.80 per topological step, or equivalent negative coefficient |

### 17.2 Power target

Minimum:

```text
80% power for H1 and H2
```

Desired:

```text
80% power for H1, H2, and H3
```

If H2 is underpowered or unstable, the paper should not claim strong system-level dialogue-network transformation.

---

## 18. Success Criteria

### 18.1 Minimum publishable success

The project remains valuable if it shows:

```text
controlled protocol works
rule-based event extraction works
dialogue networks are non-degenerate
null models expose at least one real or absent mechanism
```

This can be framed as a diagnostic benchmark.

### 18.2 Strong AAAI/AAMAS success

Strong success requires:

1. H2 positive: structural exposure predicts dialogue-network centrality.
2. H2 survives co-presence exposure control.
3. `V14_C3_natural` beats both `V14_C2_nonspatial` and `V14_C4_shuffle`.
4. H3 is positive or partially positive under QAP/run-level aggregation.
5. At least one robustness condition succeeds.
6. Direct metric descriptors are not needed for the main effect.

### 18.3 Best-case success

Best case:

```text
local topology creates exposure alignment
natural spatial cues strengthen representation-sensitive effects
exposure alignment aggregates into dialogue-network centrality
dyadic tie formation shows distance decay
all effects survive shuffled mapping, non-spatial controls, and co-presence controls
```

---

## 19. Downgrade Rules

| Pattern | Downgrade |
|---|---|
| `V14_C3_natural` matches `V14_C2_nonspatial` | information-volume or format effect |
| `V14_C3_natural` matches `V14_C4_shuffle` | mapping-insensitive prompt effect |
| `V14_D1_metrics` works but natural cues fail | LLM responds to abstract labels, not natural environment structure |
| H1 positive but H2 negative | local exposure does not aggregate into dialogue-network structure |
| H2 disappears after co-presence control | encounter-opportunity effect, not dialogue-network transformation |
| H3 disappears under QAP or run-level aggregation | no confirmatory dyadic distance-decay claim |
| rule-based extraction fails but LLM judge succeeds | possible evaluator artifact |
| alternate model fails completely | model-specific result |
| effects depend on centrality-like words | semantic leakage |
| map labels predict outcome better than hidden structure | semantic-place effect, not structural effect |

---

## 20. Expected Result Tiers

| Tier | H1 | H2 | H3 | Interpretation |
|---|---|---|---|---|
| Tier 1 | positive | positive | positive | strong evidence that controlled environment structure transfers into emergent dialogue networks |
| Tier 2 | positive | positive | mixed | strong system-level evidence, dyadic mechanism weaker |
| Tier 3 | positive | negative | mixed | environment shapes exposure but not social-network structure |
| Tier 4 | weak | weak | weak | protocol identifies boundary condition or failure mode |
| Tier 5 | only direct metric condition works | weak | weak | do not claim spatial structure use; report prompt-label sensitivity only |

Tier 1 or Tier 2 is the target.

Tier 3 can still be useful if framed honestly as an exposure-network result.

Tier 5 should not be submitted as the main spatial-structure paper.

---

## 21. Implementation Binding

### 21.1 Configs

| Artifact | Proposed path |
|---|---|
| condition definitions | `spatial-agent-core/configs/experiments/planv14_A_conditions.yaml` |
| main experiment config | `spatial-agent-core/configs/experiments/exp_planv14_A_main.yaml` |
| robustness config | `spatial-agent-core/configs/experiments/exp_planv14_A_robustness.yaml` |
| map metric config | `spatial-agent-core/configs/experiments/planv14_A_map_metrics.yaml` |

### 21.2 Runners and analysis modules

| Artifact | Proposed path | Responsibility |
|---|---|---|
| run launcher | `spatial-agent-core/experiments/run_planv14_A.py` | execute map x seed x condition runs |
| condition renderer | `spatial-agent-core/src/env/condition_renderer_v14.py` | produce agent-visible environment information |
| map metrics | `spatial-agent-core/src/analysis/map_structure_metrics.py` | compute hidden graph/spatial metrics |
| leakage audit | `spatial-agent-core/src/analysis/spatial_leakage_audit.py` | detect metric leakage and semantic confounds |
| event extraction | `spatial-agent-core/src/analysis/event_extraction.py` | rule-based social-event extraction |
| network construction | `spatial-agent-core/src/analysis/network_construction.py` | dialogue, co-presence, and exposure networks |
| network metrics | `spatial-agent-core/src/analysis/network_metrics.py` | centrality and graph summaries |
| hypothesis tests | `spatial-agent-core/src/analysis/planv14_A_hypotheses.py` | H1, H2, H3 tests |
| null models | `spatial-agent-core/src/analysis/network_nulls.py` | rewiring, shuffling, exposure permutation |
| power simulation | `spatial-agent-core/src/analysis/planv14_A_power.py` | SESOI and power checks |

### 21.3 Documentation

| Document | Proposed path |
|---|---|
| benchmark card | `spatial-agent-core/docs/planv14_A_benchmark_card.md` |
| output schema | `spatial-agent-core/docs/planv14_A_output_schema.md` |
| condition manual | `spatial-agent-core/docs/planv14_A_condition_manual.md` |
| event coding manual | `spatial-agent-core/docs/planv14_A_event_coding.md` |
| spatial metric policy | `spatial-agent-core/docs/planv14_A_spatial_metric_policy.md` |
| preregistration draft | `spatial-agent-core/docs/planv14_A_preregistration.md` |

---

## 22. Required Output Schema

Each run should write:

```text
results/planv14-A/{map}/{seed}/{condition}/metadata.json
results/planv14-A/{map}/{seed}/{condition}/agent_visible_prompts.jsonl
results/planv14-A/{map}/{seed}/{condition}/hidden_map_metrics.csv
results/planv14-A/{map}/{seed}/{condition}/visits.csv
results/planv14-A/{map}/{seed}/{condition}/copresence.csv
results/planv14-A/{map}/{seed}/{condition}/events.csv
results/planv14-A/{map}/{seed}/{condition}/messages.jsonl
results/planv14-A/{map}/{seed}/{condition}/network_dialogue.graphml
results/planv14-A/{map}/{seed}/{condition}/network_copresence.graphml
results/planv14-A/{map}/{seed}/{condition}/network_spatial_exposure.graphml
results/planv14-A/{map}/{seed}/{condition}/network_metrics.json
results/planv14-A/{map}/{seed}/{condition}/nulls.json
results/planv14-A/{map}/{seed}/{condition}/leakage_audit.json
```

### 22.1 `hidden_map_metrics.csv`

Required columns:

```text
location_id
map
accessibility_z
mean_depth_z
betweenness_z
local_degree_z
control_z
bridge_score_z
community_id
is_agent_visible
```

`is_agent_visible` should be `false` for all hidden metric columns in main conditions.

### 22.2 `agent_visible_prompts.jsonl`

Required fields:

```text
round
agent_id
condition
current_location
visible_neighbors
visible_objects
visible_agents
visible_spatial_cues
full_prompt_hash
metric_leakage_flag
```

### 22.3 `events.csv`

Required fields:

```text
round
agent_id
target_id
location
event_type
event_text
event_source
dialogue_id
```

### 22.4 `leakage_audit.json`

Required fields:

```text
condition
metric_terms_present
centrality_synonyms_present
spatial_outcome_leakage_present
semantic_label_confounds
prompt_length_stats
verdict
```

---

## 23. Stages

### Stage 0: Conceptual and substrate preflight

Purpose:

```text
make sure v14-A is not a space-syntax-as-space paper
```

Required checks:

- freeze metric policy;
- decide primary hidden metric;
- verify no direct metric leakage in main prompts;
- verify maps have structural variance;
- verify map labels do not trivially encode central/peripheral status;
- verify rule-based dialogue event extraction works;
- verify dialogue networks are non-degenerate in pilots.

Exit rule:

```text
Do not run confirmatory Stage 2 until hidden metrics, visible prompts, and leakage audits are frozen.
```

### Stage 1: Micro-task validation

Purpose:

```text
test whether agents can respond to natural local spatial cues without direct metric labels
```

Example task:

```text
Given your goal and local environment, choose where to go next.
```

Required contrasts:

```text
V14_C3_natural > V14_C2_nonspatial
V14_C3_natural > V14_C4_shuffle
```

If Stage 1 fails, Stage 2 can still run, but the paper should frame natural-cue effects as exploratory.

### Stage 2: Long-run multi-agent evaluation

Purpose:

```text
test whether environment-structure alignment aggregates into dialogue networks
```

Outputs:

- H1 exposure alignment;
- H2 dialogue centrality;
- H3 dyadic tie formation;
- co-presence exposure controls;
- null-model comparisons.

### Stage 3: Robustness and diagnostic checks

Minimum robustness:

- non-spatial matched information;
- shuffled natural cues;
- rule-based event extraction;
- co-presence exposure control;
- run-level or QAP dyadic inference.

Recommended additional robustness:

- alternate LLM model;
- direct metric descriptor diagnostic;
- neutral numeric descriptors;
- counter-semantic labels;
- human validation subset.

---

## 24. Paper Structure

```text
1. Introduction
   - LLM multi-agent systems increasingly use environments.
   - The problem is not whether environments exist, but whether environment structure is an identifiable mechanism.
   - Space syntax metrics are useful abstractions, not the agent's cognition.
   - We introduce v14-A: a controlled evaluation protocol separating environment mechanics, agent-facing representation, and researcher-side measurement.

2. Background and Motivation
   - Generative agents and spatialized simulation environments
   - Environment representation in LLM agents
   - Spatial configuration and graph-based environmental measures
   - Network analysis of emergent interaction

3. Conceptual Framework
   - Four-layer distinction: environment structure, agent-facing information, researcher-side metrics, emergent social outcomes
   - Why direct metric prompting is diagnostic, not primary evidence

4. Evaluation Protocol
   - maps
   - conditions
   - agent-visible environment rendering
   - hidden map metrics
   - leakage audits
   - output schema

5. Identification Strategy
   - local topology vs flat world
   - natural spatial cues vs non-spatial matched information
   - natural cues vs shuffled natural cues
   - co-presence exposure control
   - null models
   - downgrade rules

6. Experiments
   - Stage 0 preflight
   - Stage 1 micro-task validation
   - Stage 2 long-run multi-agent evaluation
   - Stage 3 robustness and diagnostics

7. Results
   - H1 local exposure alignment
   - H2 dialogue-network centrality
   - H3 dyadic tie formation
   - robustness, null models, and diagnostics

8. Discussion
   - what it means for LLM agents to use environment structure
   - environment mechanics vs representation-sensitive behavior
   - limits of spatial metrics
   - implications for LLM multi-agent evaluation

9. Limitations
   - metrics abstract only part of space
   - simulated agents are not humans
   - map scale and task design matter
   - model-specific behavior
   - dialogue network is only one social outcome

10. Conclusion
```

---

## 25. Reviewer Concerns and Responses

### Concern 1: Space syntax is not space.

Response:

> Correct. v14-A does not treat space syntax as space. It uses selected spatial and graph metrics as external operational measures for experimental design and analysis.

### Concern 2: Why use spatial metrics at all?

Response:

> Because the paper needs pre-specified, reproducible, quantitative structure variables. The agents do not need to know these variables; researchers use them to test whether behavior aligns with controlled environment structure.

### Concern 3: Generative Agents already have environments.

Response:

> v14-A does not claim prior systems lack environments. It claims prior systems rarely isolate environment structure as an identifiable mechanism with matched controls, shuffled mappings, co-presence controls, and dialogue-network null models.

### Concern 4: The effect may be co-location only.

Response:

> Co-presence is explicitly modeled as an exposure network. H2 must survive co-presence exposure control to support a dialogue-network transformation claim.

### Concern 5: The natural spatial cues may contain semantic leakage.

Response:

> v14-A includes non-spatial matched information, shuffled natural cues, leakage audits, and optional counter-semantic conditions.

### Concern 6: Direct metric descriptors produce stronger effects.

Response:

> That is expected and diagnostic. It shows LLM sensitivity to explicit abstractions, not necessarily natural environment-structure use. It is not the main claim.

### Concern 7: Dyads are not independent.

Response:

> H3 uses QAP, MRQAP, run-level coefficient aggregation, or permutation-based inference.

### Concern 8: Event coding is judge-biased.

Response:

> Primary social events are rule-based dialogue interactions. LLM or human judges are secondary validation tools.

---

## 26. Execution Checklist

### Immediate

- [ ] Rename project from `planv13-A` to `planv14-A`.
- [ ] Rewrite title away from “Do LLM agents use spatial structure?” toward “environment-structure effects”.
- [ ] Freeze the four-layer conceptual model.
- [ ] Remove direct `integration_z/depth_z/control_z` from main agent prompts.
- [ ] Move direct metric descriptors to diagnostic condition only.
- [ ] Decide whether primary hidden metric is `accessibility_z` or `integration_z`.

### Before implementation

- [ ] Implement condition renderer for local topology, non-spatial control, natural cues, and shuffled natural cues.
- [ ] Implement hidden map metric computation.
- [ ] Implement prompt leakage audit.
- [ ] Implement rule-based dialogue event extraction.
- [ ] Implement network construction for dialogue, co-presence, and spatial exposure.

### Before Stage 1

- [ ] Freeze natural cue templates.
- [ ] Freeze non-spatial matched information templates.
- [ ] Freeze shuffled mapping procedure.
- [ ] Run prompt-length matching check.
- [ ] Run lexical leakage audit.

### Before Stage 2

- [ ] Freeze H1, H2, H3.
- [ ] Freeze maps and seed list.
- [ ] Run power simulation.
- [ ] Freeze SESOI.
- [ ] Freeze null models.
- [ ] Freeze downgrade rules.

### Before writing

- [ ] Report H1, H2, H3 before exploratory results.
- [ ] Report co-presence-controlled H2.
- [ ] Report shuffled natural cue results.
- [ ] Report non-spatial information control.
- [ ] Report leakage audit.
- [ ] Clearly state that spatial metrics are abstractions, not space itself.
- [ ] Keep direct metric descriptor condition out of the main claim.

---

## 27. Final Positioning

v14-A should be positioned as:

> A controlled evaluation protocol for identifying whether and how LLM multi-agent systems transform environment structure into emergent dialogue networks, using natural agent-facing environment information, researcher-side spatial metrics, matched controls, co-presence exposure controls, and network null models.

The strongest paper is not:

```text
LLM agents use space syntax.
```

The strongest paper is:

```text
We can identify when environment structure becomes a measurable mechanism in LLM multi-agent interaction, without confusing external spatial metrics with the agent's own representation of space.
```

