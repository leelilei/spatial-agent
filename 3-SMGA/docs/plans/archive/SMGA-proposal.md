# SMGA Proposal

## Situated Memory for Generative Agents

> Working title: **Situated Memory for Generative Agents: From Episodic Memory Streams to Actionable Social Context**  
> Short name: **SMGA**  
> Version: 0.1  
> Date: 2026-05-19  
> Status: independent research proposal  

---

## 0. One-Line Version

This project studies whether **Generative-Agent-style memory streams are sufficient for situated social behavior**, and proposes a structured memory framework that converts raw episodic experience into **entity-indexed, evidence-grounded, and planning-actionable social context**.

The central question is:

> Can LLM generative agents move beyond flat episodic memory streams and form structured situated memories about people, places, relationships, activities, and recurring social contexts that they can actually use in future planning and behavior?

---

## 1. Why This Project Exists

Generative Agents showed that LLM-based agents can simulate believable daily behavior by combining memory, retrieval, reflection, planning, and action. The key architectural move was to give each agent a memory stream: a natural-language record of observations, plans, conversations, and reflections that can be retrieved later to support future behavior.

That was a major step forward. But the memory stream is still mostly a **flat episodic record**. It can store that something happened, and it can retrieve relevant fragments, but it does not by itself guarantee that the agent will organize experience into reusable social knowledge.

For example, a GA-style agent may store:

```text
Maria talked with Klaus at the cafe about the party.
Klaus saw Maria again at the cafe the next morning.
Klaus heard event news from Isabella in the cafe.
```

But the architecture does not necessarily form or use the more actionable abstraction:

```text
The cafe is a place where Klaus often encounters Maria and hears social news.
If Klaus wants to find Maria or learn public information, the cafe is a reasonable place to visit.
```

This gap matters because believable simulation is not the same as situated social cognition. A believable agent may respond plausibly to the current prompt, but a socially situated agent should be able to:

```text
remember where social experiences occurred;
connect repeated experiences across people, places, and activities;
abstract place-, person-, and relationship-level meanings;
use those meanings in future planning;
update them when later experiences contradict earlier patterns.
```

SMGA proposes that the next step after GA is not merely a larger memory, a longer context window, or a better vector retriever. The next step is a **structured situated memory framework**.

---

## 2. Research Gap

### 2.1 What Generative Agents solved

Generative Agents introduced a practical architecture for believable LLM agents:

```text
observation
-> memory stream
-> retrieval
-> reflection
-> planning
-> action / reaction / dialogue
```

Its strengths are clear:

- agents maintain a record of experience;
- retrieval combines relevance, recency, and importance;
- reflection turns lower-level memories into higher-level thoughts;
- planning uses memory and current state to generate daily behavior;
- multi-agent simulation can produce emergent social events.

This made long-running LLM social simulation plausible.

### 2.2 What Generative Agents did not fully solve

GA-style memory is powerful, but it leaves several unresolved issues:

#### Gap 1: Flat memory is not structured social knowledge

A memory stream records experiences as natural-language items. It does not necessarily create durable, typed, queryable structures such as:

```text
person memory
place memory
relationship memory
activity memory
routine memory
social norm memory
```

As a result, the agent may remember many episodes without forming stable social context.

#### Gap 2: Place is usually a location field, not a memory object

In GA-like systems, a location often appears as metadata or narrative context:

```text
Klaus talked with Maria at the cafe.
```

But the location itself is rarely treated as an evolving social object:

```text
Cafe -> repeated encounters with Maria
Cafe -> public information exchange
Cafe -> good place for casual conversation
Cafe -> candidate place for finding Maria later
```

This matters because many forms of social intelligence are place-mediated. People do not only remember who they know; they also remember where interactions tend to happen.

#### Gap 3: Reflection is general, not systematically situated

GA-style reflection can synthesize higher-level thoughts, but it is not usually organized by explicit reflection targets such as:

```text
What kind of place is this becoming for me?
What pattern characterizes my relationship with this person?
Which activities repeatedly occur in this setting?
Which locations are associated with positive, negative, public, private, or information-rich interactions?
```

Without target-specific reflection, situated meanings may remain implicit, inconsistent, or unused.

#### Gap 4: Retrieval does not guarantee planning use

Even if the relevant memories exist, the agent may not retrieve them at the moment of planning. Even if they are retrieved, the agent may not use them as evidence for action.

The key missing link is:

```text
episodic memory
-> structured situated abstraction
-> planning-actionable recommendation
-> changed behavior
```

Most memory evaluations stop at recall or retrieval accuracy. SMGA evaluates whether memory changes future behavior.

#### Gap 5: Social simulation needs memory mechanisms, not only outcome networks

It is tempting to measure only the emergent dialogue network and ask whether the network looks plausible. But a plausible network does not reveal the mechanism. Did agents form situated memories, or were they simply colocated? Did they choose future locations based on remembered experience, or did the simulator route them there?

SMGA treats the memory mechanism itself as the research object.

---

## 3. Core Claim

The clean claim is not:

> We add more memory to agents.

Nor is it:

> We make agents better at social simulation.

The clean claim is:

> A flat GA-style memory stream is insufficient for robust situated social behavior. A structured situated memory framework can improve agents' ability to form, retrieve, abstract, and act on social memories tied to people, places, relationships, activities, and recurring contexts.

In shorter form:

> From memory stream to situated social memory.

---

## 4. Research Frame

SMGA reframes the problem from spatial structure to memory architecture.

### 4.1 Old frame to avoid

The earlier spatial framing asked:

```text
Does spatial structure shape emergent dialogue networks?
```

This is useful but limited. It risks collapsing into an encounter-opportunity claim:

```text
space changes who meets whom;
therefore space changes dialogue.
```

That is not deep enough as an agent-architecture contribution.

### 4.2 New frame

The new frame asks:

```text
Can agent memory transform situated experience into future-oriented social knowledge?
```

This shifts the causal chain:

```text
experience
-> memory organization
-> situated abstraction
-> planning use
-> behavior
-> social network
```

Space remains useful, but only as one domain in which situated memory can be tested. The paper is not about space syntax, and it does not require agents to receive space-syntax metrics.

### 4.3 Unit of contribution

The contribution is a **memory framework** and an **evaluation protocol**.

SMGA should be presented as:

```text
an architectural extension to GA-style agents
+
a controlled evaluation of whether structured situated memory changes recall, abstraction, planning, and behavior.
```

---

## 5. What SMGA Is and Is Not

### 5.1 SMGA is

SMGA is:

- a memory-architecture paper;
- a direct extension and critique of GA-style memory streams;
- a framework for turning episodes into structured social context;
- an evaluation of whether memory becomes behaviorally actionable;
- a bridge between social simulation, language-agent memory, and situated cognition.

### 5.2 SMGA is not

SMGA is not:

- a space-syntax paper;
- a generic vector-memory system;
- a long-context management paper;
- a new multi-agent simulator;
- a pure social-network paper;
- a claim that agents have human-like cognition;
- a claim that adding structure always improves believability.

---

## 6. Related-Work Positioning

### 6.1 Generative Agents

Generative Agents is the primary baseline. It demonstrates memory streams, reflection, and planning for believable multi-agent simulation. SMGA keeps this core loop but asks whether the memory stream is too flat to support situated social behavior.

SMGA's positioning:

```text
GA: believable agents through natural-language memory streams.
SMGA: structured situated memory for evidence-grounded and planning-actionable social context.
```

### 6.2 Cognitive architectures for language agents

Cognitive architecture work, especially CoALA, frames language agents as systems with modular memory, action spaces, and decision processes. SMGA can be positioned as a concrete memory architecture within this broader cognitive-architecture landscape.

SMGA's positioning:

```text
CoALA: high-level taxonomy of language-agent cognition.
SMGA: specific situated-memory design and evaluation for generative social agents.
```

### 6.3 Long-term memory systems

MemoryBank, MemGPT, and related systems address long-term memory, context management, memory updating, and extended interaction. These systems are important but usually focus on storing, recalling, compressing, or managing memory over time.

SMGA's distinction:

```text
Long-term memory systems: how to remember more over time.
SMGA: how to organize experience into social context that can guide future behavior.
```

### 6.4 Reflection and lifelong learning agents

Reflexion and Voyager show that agents can use verbal feedback, reflection, or skill libraries to improve future performance. They demonstrate that memory should not only store the past; it should support future action.

SMGA's distinction:

```text
Reflexion/Voyager: task feedback and skill learning.
SMGA: situated social memory over people, places, relationships, activities, and recurring contexts.
```

### 6.5 Structured and graph memory

HippoRAG, A-Mem, and graph-memory systems show a broader move from unstructured memory lists toward linked, structured, graph-like memory. SMGA should acknowledge this trend.

SMGA's distinction:

```text
Structured memory work: general memory organization and retrieval.
SMGA: socially situated schema + GA-style simulation + behavioral evaluation of planning use.
```

### 6.6 Social-intelligence benchmarks and simulators

SOTOPIA and Lifelong-SOTOPIA evaluate social intelligence and long-term social interaction. Concordia, AgentSims, AgentSociety, and Ella-like embodied social-agent systems show that agent environments and social simulations are becoming richer.

SMGA's distinction:

```text
Social benchmarks/simulators: evaluate or instantiate social behavior.
SMGA: tests what memory architecture is needed for situated social behavior to emerge and be used.
```

---

## 7. Proposed Framework

SMGA has four memory layers.

```text
Layer 1: Episodic Memory
Layer 2: Entity-Indexed Memory
Layer 3: Situated Abstraction
Layer 4: Actionable Memory for Planning
```

The framework can be implemented inside a GA-like agent loop.

---

## 8. Layer 1: Episodic Memory

This layer corresponds to the original GA-style memory stream.

It stores raw experiences:

```json
{
  "memory_id": "mem_00041",
  "agent_id": "klaus",
  "time": "day_1_15_30",
  "memory_type": "dialogue",
  "text": "Klaus talked with Maria at the cafe about the upcoming party.",
  "actors": ["klaus", "maria"],
  "location": "cafe",
  "topic_tags": ["party", "social_event"],
  "valence": "positive",
  "importance": 6,
  "source_event_id": "event_00122"
}
```

This layer answers:

> What happened?

It should preserve GA compatibility and serve as the evidence base for all higher layers.

---

## 9. Layer 2: Entity-Indexed Memory

This layer attaches each episode to typed entities.

Entity types:

```text
person
place
relationship
activity
topic
goal
routine
social_group
```

Example index records:

```json
{
  "entity_type": "place",
  "entity_id": "cafe",
  "linked_memory_ids": ["mem_00041", "mem_00057", "mem_00082"],
  "summary_hint": "dialogues and public social encounters"
}
```

```json
{
  "entity_type": "relationship",
  "entity_id": "klaus::maria",
  "linked_memory_ids": ["mem_00041", "mem_00057"],
  "summary_hint": "repeated friendly conversations"
}
```

This layer answers:

> Which experiences are associated with this person, place, relationship, activity, or topic?

Key design point:

> The system should not rely only on semantic vector similarity. It should support explicit typed retrieval.

---

## 10. Layer 3: Situated Abstraction

This layer periodically converts entity-indexed episodes into evidence-grounded situated memories.

The abstraction should be typed by target.

### 10.1 Person reflection

```json
{
  "reflection_id": "pref_00012",
  "target_type": "person",
  "target_id": "maria",
  "text": "Klaus sees Maria as a familiar and friendly social contact.",
  "evidence_ids": ["mem_00041", "mem_00057", "mem_00083"],
  "confidence": 0.78
}
```

### 10.2 Place reflection

```json
{
  "reflection_id": "plref_00007",
  "target_type": "place",
  "target_id": "cafe",
  "text": "The cafe has recently been a common place for Klaus to meet Maria and hear social news.",
  "evidence_ids": ["mem_00041", "mem_00057", "mem_00082"],
  "place_role_tags": ["social_hub", "information_exchange"],
  "confidence": 0.74
}
```

### 10.3 Relationship reflection

```json
{
  "reflection_id": "rref_00019",
  "target_type": "relationship",
  "target_id": "klaus::maria",
  "text": "Klaus and Maria's relationship has become more familiar through repeated informal conversations.",
  "evidence_ids": ["mem_00041", "mem_00057", "mem_00083"],
  "relationship_tags": ["friendly", "increasing_familiarity"],
  "confidence": 0.81
}
```

This layer answers:

> What do repeated experiences mean in context?

Important constraint:

> Every situated abstraction must cite evidence memories. Unsupported abstraction is a failure, not a feature.

---

## 11. Layer 4: Actionable Memory for Planning

This layer turns situated memories into planning-useful suggestions.

Example:

```json
{
  "suggestion_id": "actmem_00021",
  "agent_id": "klaus",
  "goal_type": "find_person",
  "goal_target": "maria",
  "suggested_action": "visit_place",
  "suggested_place": "cafe",
  "rationale": "Klaus has met Maria at the cafe several times recently.",
  "evidence_ids": ["mem_00041", "mem_00057", "plref_00007"],
  "confidence": 0.76
}
```

Other examples:

```text
Goal: hear public news
Suggestion: visit plaza, because recent information exchanges happened there.

Goal: avoid John
Suggestion: avoid studio, because the last interaction with John there was negative.

Goal: work quietly
Suggestion: go to library, because it is associated with solitary work and low social interruption.
```

This layer answers:

> Given the current goal, what past situated experience should shape the plan?

This is the central SMGA idea.

---

## 12. Runtime Loop

SMGA modifies the GA loop as follows:

```text
Perceive event
-> write episodic memory
-> update entity indexes
-> periodically generate situated abstractions
-> retrieve situated memories for current goal
-> produce actionable planning suggestions
-> generate plan using evidence-bounded memory context
-> execute action
-> log whether plan used situated memory
```

The LLM still generates natural-language decisions, but memory access is structured and auditable.

---

## 13. Research Questions

### RQ1: Formation

> Do SMGA agents form more accurate person-, place-, relationship-, and activity-linked memories than GA-style baseline agents?

### RQ2: Abstraction

> Do SMGA agents generate more evidence-supported situated abstractions than GA-style baseline agents?

### RQ3: Planning use

> Do SMGA agents actually use situated memories in future planning, rather than merely being able to report them in interviews?

### RQ4: Behavioral feedback

> Does situated memory change future movement, interaction, seeking, avoidance, and social decision behavior under matched conditions?

### RQ5: Social emergence

> Do situated memory mechanisms produce more interpretable and evidence-grounded emergent social networks, beyond simple co-presence or encounter opportunity?

---

## 14. Hypotheses

### H1: Entity-indexed recall

SMGA improves recall of who, where, with whom, and in what context events occurred.

Expected pattern:

```text
M1, M2, M3 > M0
```

### H2: Situated abstraction

SMGA improves evidence-supported abstraction over places, people, relationships, and recurring activities.

Expected pattern:

```text
M2, M3 > M1 > M0
```

### H3: Planning use

SMGA increases the rate at which future plans cite and use relevant situated memories.

Expected pattern:

```text
M3 > M2 > M1 > M0
```

### H4: Behavioral feedback

SMGA agents are more likely to choose locations, contacts, and activities consistent with prior situated social experience.

Expected pattern:

```text
M3 > M2 > M1 > M0
```

### H5: Network interpretability

SMGA produces dialogue ties and repeated interactions that are more traceable to prior memory evidence, without requiring the dialogue network to become larger or denser.

Expected pattern:

```text
M3 has higher evidence-supported tie formation than M0.
```

---

## 15. Experimental Conditions

The main experiment is a memory-architecture ablation.

| Condition | Name | Description | Role |
|---|---|---|---|
| M0 | GA-like baseline | Episodic memory stream + standard retrieval/reflection/planning | baseline |
| M1 | Entity-indexed memory | M0 + typed indexing by person, place, relationship, activity, topic | indexing ablation |
| M2 | Situated reflection | M1 + evidence-grounded target-specific abstractions | abstraction ablation |
| M3 | Actionable situated memory | M2 + planning-time memory suggestions and evidence citation | full SMGA |

Optional additional conditions:

| Condition | Name | Description |
|---|---|---|
| M1-vector-only | Unstructured retrieval | Uses vector retrieval without typed entity indexes |
| M2-no-evidence | Unconstrained abstraction | Allows reflections without evidence IDs; useful as a hallucination-risk control |
| M3-no-planning-citation | Hidden planning memory | Supplies memory but does not require plan evidence citation |

---

## 16. Experimental Design

### 16.1 Two-phase design

Use a two-phase experiment.

```text
Phase 1: controlled experience exposure
Phase 2: free planning and behavioral probes
```

This separates memory formation from future use.

### 16.2 Phase 1: Controlled experience exposure

All conditions receive the same scripted or semi-scripted experiences.

Example environment:

```text
agents: 6-8
locations: 6
simulation days: 1-2 controlled exposure days
```

Location roles should be induced by experience, not by obvious labels.

Example:

| Location | Induced experience |
|---|---|
| Room A | repeated casual conversations |
| Room B | repeated information exchange |
| Room C | one or more negative interactions |
| Room D | quiet work / low social activity |
| Room E | repeated encounters with a specific person |
| Room F | transit-only / high co-presence but little dialogue |

Important rule:

> Do not rely on names such as cafe, library, or plaza if those names leak social affordances. Use neutral labels in the cleanest version.

### 16.3 Phase 2: Free behavior and probes

After Phase 1, agents receive goals that require memory use.

Examples:

```text
Find Maria.
Hear the latest public news.
Avoid John after an awkward interaction.
Choose a quiet place to work.
Plan an afternoon with both work and social goals.
```

Then measure where they go, whom they contact, what they say, and whether their rationale cites prior situated memory.

### 16.4 Matched-seed design

Each seed should generate the same agents, goals, initial states, and Phase 1 events across conditions.

```text
seed_i under M0
seed_i under M1
seed_i under M2
seed_i under M3
```

This ensures that differences are attributable to memory architecture rather than different worlds.

---

## 17. Evaluation Metrics

SMGA should not rely on a single metric. The evaluation must show a chain from memory to behavior.

```text
recall
-> abstraction
-> planning use
-> behavior
-> network interpretability
```

---

## 18. Metric Family 1: Situated Recall

### 18.1 Place recall accuracy

Questions:

```text
What usually happens at Room A?
Who have you met at Room B?
Where did you previously hear important news?
Which place would you avoid, and why?
```

Metrics:

```text
place-recall precision
place-recall recall
unsupported place-claim rate
place-agent association accuracy
place-topic association accuracy
```

### 18.2 Person and relationship recall

Questions:

```text
Where have you met Maria recently?
What kinds of interactions have you had with John?
Which person is associated with Room E?
```

Metrics:

```text
person-place recall accuracy
relationship-event recall accuracy
relationship-valence accuracy
```

Expected result:

```text
M1/M2/M3 improve recall over M0.
```

---

## 19. Metric Family 2: Situated Abstraction

### 19.1 Place-role classification

Ground-truth roles are derived from logs.

Possible roles:

```text
social hub
information exchange place
avoidance place
quiet work place
person-specific encounter place
transit-only place
```

Metrics:

```text
place-role accuracy
place-role F1
ranking correlation between agent-rated sociality and log-derived sociality
```

### 19.2 Evidence-supported abstraction rate

For each generated abstraction:

```text
Is the claim supported by cited memories?
Does the evidence cover enough independent events?
Does the abstraction overgeneralize beyond evidence?
```

Metrics:

```text
supported-abstraction rate
unsupported-abstraction rate
reflection evidence diversity
reflection overgeneralization rate
```

Expected result:

```text
M2/M3 improve abstraction quality over M0/M1.
```

---

## 20. Metric Family 3: Planning Use

This is the central evaluation family.

For each plan, log:

```json
{
  "plan_id": "plan_00031",
  "agent_id": "klaus",
  "goal": "find Maria",
  "chosen_location": "Room E",
  "rationale": "I have met Maria at Room E several times recently.",
  "used_memory_ids": ["mem_00011", "mem_00036", "plref_00004"],
  "support_status": "supported"
}
```

Metrics:

```text
place-memory-used-in-plan rate
relationship-memory-used-in-plan rate
activity-memory-used-in-plan rate
evidence-supported planning rate
unsupported planning-rationale rate
planning citation completeness
```

Expected result:

```text
M3 should outperform M0/M1/M2.
```

Critical rule:

> A plan does not count as memory-guided unless its rationale is supported by logged memory evidence.

---

## 21. Metric Family 4: Behavioral Feedback

This family tests whether memory changes action.

### 21.1 Goal-consistent location choice

Example tasks:

| Goal | Relevant memory | Expected action |
|---|---|---|
| find Maria | Maria repeatedly appeared in Room E | visit Room E |
| hear news | Room B hosted information exchange | visit Room B |
| avoid John | negative interaction occurred in Room C | avoid Room C |
| work quietly | Room D had quiet work history | visit Room D |

Metrics:

```text
target-consistent location choice rate
relevant-place selection advantage
avoidance-after-negative-interaction rate
information-seeking location accuracy
quiet-work location accuracy
```

### 21.2 Behavioral model

A possible model:

```text
visit_relevant_location ~ memory_condition
                        + goal_type
                        + distance
                        + location_baseline_popularity
                        + agent_sociability
                        + seed
```

Expected result:

```text
M3 agents should be more likely to choose behavior consistent with situated memory.
```

---

## 22. Metric Family 5: Network Interpretability

Network metrics are secondary. They should not be the only evidence.

Primary network:

```text
dialogue network
```

Control network:

```text
co-presence network
```

Metrics:

```text
evidence-supported dialogue-tie rate
repeat-tie rate at memory-relevant places
goal-directed encounter success rate
dialogue beyond co-presence
relationship reinforcement after memory-guided revisits
```

Key comparison:

```text
Does SMGA produce dialogue ties that can be traced to prior situated memory evidence, beyond what co-presence alone explains?
```

Expected result:

```text
M3 improves traceability and interpretability of dialogue ties.
```

---

## 23. Minimum Viable Experiment

### 23.1 MVP scale

Recommended first experiment:

```text
agents: 6-8
locations: 6
conditions: M0, M1, M2, M3
seeds: 10-20
runs: 40-80
```

### 23.2 MVP outputs

Each run should produce:

```text
results/smga/{seed}/{condition}/metadata.json
results/smga/{seed}/{condition}/events.jsonl
results/smga/{seed}/{condition}/episodes.jsonl
results/smga/{seed}/{condition}/entity_index.jsonl
results/smga/{seed}/{condition}/situated_reflections.jsonl
results/smga/{seed}/{condition}/planning_suggestions.jsonl
results/smga/{seed}/{condition}/plans.jsonl
results/smga/{seed}/{condition}/actions.jsonl
results/smga/{seed}/{condition}/dialogues.jsonl
results/smga/{seed}/{condition}/network_dialogue.graphml
results/smga/{seed}/{condition}/network_copresence.graphml
results/smga/{seed}/{condition}/metrics_run.json
```

---

## 24. Required Data Schema

### 24.1 Episode memory

```text
memory_id
agent_id
time
memory_type
text
actors
location
activity
topic_tags
valence
importance
source_event_id
```

### 24.2 Entity index

```text
entity_index_id
agent_id
entity_type
entity_id
linked_memory_ids
last_updated
summary_hint
```

### 24.3 Situated reflection

```text
reflection_id
agent_id
target_type
target_id
text
evidence_ids
role_tags
confidence
support_status
created_at
used_later
```

### 24.4 Planning suggestion

```text
suggestion_id
agent_id
goal_type
goal_target
suggested_action
suggested_entity
rationale
evidence_ids
confidence
used_in_plan
```

### 24.5 Plan trace

```text
plan_id
agent_id
goal
chosen_action
chosen_location
chosen_target
rationale
used_memory_ids
support_status
execution_result
```

---

## 25. Statistical Analysis

### 25.1 Independent unit

The primary independent unit should be the run.

Agent-level, place-level, and dyad-level outcomes are nested within runs and should not be treated as fully independent without clustering or run-level aggregation.

### 25.2 Primary comparisons

Primary comparisons:

```text
M1 vs M0: effect of entity indexing
M2 vs M1: effect of situated abstraction
M3 vs M2: effect of planning-actionable memory
M3 vs M0: full SMGA effect
```

### 25.3 Primary endpoints

Recommended primary endpoints:

```text
place-role F1
evidence-supported planning rate
target-consistent location choice rate
unsupported situated-claim rate
```

### 25.4 Secondary endpoints

Secondary endpoints:

```text
network tie traceability
repeat-tie rate
dialogue beyond co-presence
believability rating
cost and latency
```

### 25.5 Multiple comparisons

Control FDR within the primary endpoint family.

---

## 26. Success Criteria

### Minimum success

The project is worth continuing if:

```text
M1/M2/M3 improve situated recall over M0
and unsupported memory claims do not increase sharply.
```

Interpretation:

> GA-style flat memory under-organizes situated experience; typed indexing helps.

### Strong success

The project becomes a strong memory-architecture paper if:

```text
M2 improves evidence-supported situated abstraction
and M3 improves planning evidence use.
```

Interpretation:

> Situated memory requires both entity indexing and target-specific abstraction.

### Best-case success

The strongest result is:

```text
M3 improves recall, abstraction, planning use, and behavior
while preserving believability and reducing unsupported claims.
```

Interpretation:

> Structured situated memory converts episodic experience into actionable social context.

---

## 27. Downgrade Rules

| Result pattern | Downgrade |
|---|---|
| Recall improves but planning does not | SMGA improves memory reporting, not behavior |
| Planning rationales improve but actions do not | SMGA improves explanation, not decision-making |
| Actions change but evidence support is weak | possible hallucinated rationale or prompt artifact |
| Network changes disappear after co-presence control | memory changed exposure, not social behavior beyond exposure |
| M0 already matches M3 | GA-style memory may be sufficient under this task |
| M1 matches M3 | indexing is enough; abstraction/planning modules unnecessary |
| M2 improves abstraction but M3 reduces believability | over-structured memory harms natural behavior |
| M3 requires highly leading prompts | result is prompt steering, not memory architecture |

---

## 28. Main Risks

### 28.1 Novelty risk

Risk:

```text
Reviewers say this is just graph memory or structured retrieval.
```

Control:

```text
Position SMGA as socially situated memory for GA-style agents, evaluated by planning use and behavior, not only retrieval QA.
```

### 28.2 Prompt artifact risk

Risk:

```text
Agents use place memories only because the prompt explicitly tells them to.
```

Control:

```text
Use both forced-choice probes and open-ended planning probes. Report whether memory use appears without overly leading prompts.
```

### 28.3 Hallucinated abstraction risk

Risk:

```text
The system generates plausible but unsupported place or relationship meanings.
```

Control:

```text
Require evidence IDs and score support status. Unsupported abstraction is a primary failure mode.
```

### 28.4 Over-structuring risk

Risk:

```text
Structured memory makes agents rigid, repetitive, or less believable.
```

Control:

```text
Believability preservation is a secondary endpoint. Planning suggestions should be optional evidence, not hard rules.
```

### 28.5 Evaluation leakage risk

Risk:

```text
Ground-truth roles leak into prompts or memory suggestions.
```

Control:

```text
Roles must be inferred from event evidence, not inserted as labels during exposure.
```

---

## 29. Relation to Previous Spatial Plans

SMGA does not discard the spatial insight. It reframes it.

Earlier spatial plans asked whether environment structure shapes emergent dialogue networks. SMGA asks what memory architecture is necessary for agents to convert environment-mediated experience into future-oriented social knowledge.

Space becomes a testbed, not the main theoretical object.

```text
Old frame:
spatial structure -> dialogue network

SMGA frame:
situated experience -> structured memory -> planning -> behavior -> dialogue network
```

Space syntax or graph metrics may still be used by the researcher as background analysis variables, but they should not be the agent's internal cognitive language.

---

## 30. Expected Contributions

### Contribution 1: Conceptual

SMGA defines **situated social memory** as a missing layer between episodic memory streams and believable long-run social behavior.

### Contribution 2: Architectural

SMGA proposes a four-layer memory framework:

```text
episodic memory
entity-indexed memory
situated abstraction
actionable planning memory
```

### Contribution 3: Evaluation

SMGA introduces an evaluation protocol that tests not only whether agents remember, but whether memory is evidence-supported, abstracted correctly, used in planning, and reflected in behavior.

### Contribution 4: Empirical

SMGA compares GA-like memory against structured situated-memory ablations under matched social experience conditions.

---

## 31. Paper Structure

```text
1. Introduction
   - GA made believable agents possible through memory streams.
   - But flat memory streams may under-support situated social behavior.
   - We introduce Situated Memory for Generative Agents.

2. Background and Related Work
   - Generative Agents
   - Cognitive architectures for language agents
   - Long-term memory systems
   - Structured/graph memory
   - Social intelligence benchmarks

3. Research Gap
   - episodic memory vs situated social memory
   - recall vs planning use
   - social network outcome vs memory mechanism

4. SMGA Framework
   - episodic memory
   - entity-indexed memory
   - situated abstraction
   - actionable planning memory

5. Experimental Design
   - memory architecture ablations
   - controlled exposure phase
   - free planning phase
   - matched-seed design

6. Metrics
   - situated recall
   - abstraction support
   - planning evidence use
   - behavioral feedback
   - network interpretability

7. Results
   - H1 recall
   - H2 abstraction
   - H3 planning use
   - H4 behavior
   - H5 network traceability

8. Discussion
   - what GA-style memory is sufficient for
   - when structured memory helps
   - trade-offs between structure and believability

9. Limitations
   - prompt sensitivity
   - evaluation domain limits
   - human-likeness claims

10. Conclusion
```

---

## 32. Implementation Plan

### Stage 0: Baseline audit

Tasks:

```text
reproduce or approximate GA-like memory loop
identify how memories are written, retrieved, reflected, and used in planning
create logging for memory usage in plans
```

Exit condition:

```text
M0 baseline can run controlled exposure and planning probes.
```

### Stage 1: Entity indexing

Tasks:

```text
add typed memory metadata
build entity indexes
support retrieval by person, place, relationship, activity, and topic
```

Exit condition:

```text
M1 improves entity-specific recall in pilot tests.
```

### Stage 2: Situated reflection

Tasks:

```text
generate target-specific abstractions
require evidence IDs
score support status
```

Exit condition:

```text
M2 produces evidence-supported place/person/relationship abstractions.
```

### Stage 3: Planning-actionable memory

Tasks:

```text
retrieve situated memories for goals
generate planning suggestions with evidence IDs
log whether suggestions are used
```

Exit condition:

```text
M3 changes planning decisions in controlled probes.
```

### Stage 4: Full evaluation

Tasks:

```text
run matched-seed experiments
compute primary metrics
run robustness checks
write paper
```

Exit condition:

```text
M3 improves planning use and behavior without major believability loss.
```

---

## 33. Minimal File/Code Structure

Proposed paths:

```text
smga/configs/conditions.yaml
smga/configs/experiment_main.yaml
smga/runtime/agent_loop.py
smga/memory/episodic_store.py
smga/memory/entity_index.py
smga/memory/situated_reflection.py
smga/memory/actionable_memory.py
smga/eval/recall_metrics.py
smga/eval/abstraction_metrics.py
smga/eval/planning_metrics.py
smga/eval/behavior_metrics.py
smga/eval/network_metrics.py
smga/experiments/run_smga.py
smga/docs/output_schema.md
smga/docs/evaluation_manual.md
smga/docs/preregistration.md
```

---

## 34. Recommended Title Options

### Option A

**Situated Memory for Generative Agents: From Episodic Memory Streams to Actionable Social Context**

Best if the paper is architecture-focused.

### Option B

**Beyond Memory Streams: Structured Situated Memory for Generative Social Agents**

Best if the paper directly critiques GA-style memory.

### Option C

**Can Generative Agents Form Place-Based Social Memory?**

Best if the first experiment uses place memory as the main testbed.

### Option D

**From Experience to Social Context: A Structured Memory Framework for LLM Agents**

Best if aiming for a broader language-agent venue.

Recommended title:

> **Situated Memory for Generative Agents: From Episodic Memory Streams to Actionable Social Context**

---

## 35. References to Ground the Proposal

- Park et al. 2023. **Generative Agents: Interactive Simulacra of Human Behavior.** https://arxiv.org/abs/2304.03442
- Sumers et al. 2023. **Cognitive Architectures for Language Agents.** https://arxiv.org/abs/2309.02427
- Zhong et al. 2023/2024. **MemoryBank: Enhancing Large Language Models with Long-Term Memory.** https://arxiv.org/abs/2305.10250
- Packer et al. 2023. **MemGPT: Towards LLMs as Operating Systems.** https://arxiv.org/abs/2310.08560
- Shinn et al. 2023. **Reflexion: Language Agents with Verbal Reinforcement Learning.** https://arxiv.org/abs/2303.11366
- Wang et al. 2023. **Voyager: An Open-Ended Embodied Agent with Large Language Models.** https://arxiv.org/abs/2305.16291
- Zhou et al. 2023/2024. **SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents.** https://arxiv.org/abs/2310.11667
- Goel et al. 2025. **Lifelong-SOTOPIA: Evaluating Social Intelligence of Language Agents over Lifelong Social Interactions.** https://arxiv.org/pdf/2506.12666
- Gutierrez et al. 2024. **HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models.** https://openreview.net/forum?id=hkujvAPVsg
- Xu et al. 2025. **A-Mem: Agentic Memory for LLM Agents.** https://openreview.net/forum?id=FiM0M8gcct
- Zhang et al. 2025. **Ella: Embodied Social Agents with Lifelong Memory.** https://arxiv.org/abs/2506.24019
- Zhang et al. 2024. **A Survey on the Memory Mechanism of Large Language Model based Agents.** https://arxiv.org/abs/2404.13501

---

## 36. Final Positioning Statement

SMGA should be positioned as follows:

> Generative Agents showed that memory streams can support believable long-running behavior. However, flat memory streams do not necessarily let agents organize experience into situated social knowledge. SMGA proposes a structured memory framework that transforms episodic experience into entity-indexed, evidence-grounded, and planning-actionable memories. Through controlled memory-architecture ablations, we test whether agents can form and use situated memories about people, places, relationships, activities, and recurring social contexts, and whether those memories affect future behavior rather than merely improving retrospective recall.

This is the core of the project.
