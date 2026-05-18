# TGA-PLAN.md

# Auditable Tool-Orchestrated Generative Agents

## Tool-Orchestrated Memory, Planning, Reflection, and Social Interaction for Believable Multi-Agent Simulation

> Version: 0.1  
> Date: 2026-05-18  
> Working name: **TGA / Tool-GA**  
> Recommended paper-facing name: **Auditable Generative Agents**  
> Status: research-gap and research-plan draft  
> Relation to SpatialAgent v13/v13-A: complementary runtime / possible follow-on paper

---

## 0. One-Line Version

This project studies whether the original **Generative Agents** architecture can be made more reliable, auditable, and reproducible by replacing monolithic prompt-chain cognition with explicit tools for memory retrieval, planning validation, reflection evidence, social-event logging, and optional spatial querying.

The central question is:

> Can tool-orchestrated cognitive modules improve the reliability and auditability of GA-style long-running social simulations without damaging believable individual behavior or emergent social interaction?

---

## 1. Motivation

The original Generative Agents framework demonstrated that LLM-based agents can simulate believable human-like daily behavior and emergent social dynamics by combining:

```text
memory stream
-> retrieval
-> reflection
-> planning
-> action / reaction / dialogue
```

This architecture is powerful because agents do not merely respond to the current prompt. They remember past experiences, retrieve relevant memories, synthesize reflections, plan over longer time horizons, and react to events.

However, the architecture is also mostly **prompt-chain driven**. Memory retrieval, reflection generation, planning, reaction, and dialogue rely heavily on natural-language prompts and untyped context assembly. This creates a gap between believable outputs and auditable mechanisms.

For scientific use, especially social simulation and multi-agent evaluation, this is a serious limitation. It is not enough for agents to produce plausible text. We need to know:

```text
Which memories were retrieved?
Which evidence supported a reflection?
Which constraints made a plan valid or invalid?
Which observed dialogue created a social edge?
Which spatial or social state was actually available to the agent?
```

TGA addresses this by treating Generative Agents not only as believable characters, but as **auditable computational systems**.

---

## 2. Research Gap

### 2.1 Gap in Generative Agents

Generative Agents established a cognitively inspired architecture, but several unresolved issues remain:

1. **Memory retrieval is imperfect.**  
   Agents can fail to retrieve relevant memories or retrieve incomplete fragments, causing incorrect answers or inconsistent behavior.

2. **Memory-based answers can contain embellishments.**  
   Agents may produce plausible but unsupported details when recalling past events.

3. **Reflection lacks fully structured evidence control.**  
   Reflections cite memories in the original design, but the end-to-end system does not enforce strong typed provenance for every downstream use of those reflections.

4. **Planning can be plausible but hard to validate.**  
   Plans are generated recursively in natural language. Without explicit validators, time conflicts, location errors, repeated activities, or impossible actions may be difficult to detect systematically.

5. **Social events are not first-class audit objects.**  
   Dialogue and interaction happen in the simulation, but social-event extraction and network construction are usually post hoc rather than part of the agent runtime.

6. **The system is costly and slow.**  
   The original 25-agent simulation required substantial token credits and time. Cost optimization has been studied by AGA, but auditability and reliability remain underexplored.

7. **Robustness is not well characterized.**  
   Prompt hacking, memory hacking, hallucinated events, and long-horizon drift remain important concerns for GA-style systems.

### 2.2 Gap after Affordable Generative Agents

Affordable Generative Agents reduces cost by:

```text
agent-environment side: Lifestyle Policy reuses repeated plan/action decompositions
inter-agent side: Social Memory compresses dialogue auxiliary information
```

AGA is important, but its primary target is **affordability**. It does not fully solve:

```text
memory faithfulness
reflection provenance
plan validation
social-event auditability
traceable network construction
robustness to corrupted memories or unsupported claims
```

It also notes that better evaluation mechanisms for believable behavior remain needed.

### 2.3 Gap in modern tool-using agent frameworks

Modern agent frameworks already support tools, traces, skills, handoffs, state, and external APIs. Related work includes general tool-using agents, cognitive architectures for language agents, AutoGen-style multi-agent frameworks, and newer agent SDKs.

Therefore, **tool use itself is not novel**.

The open research gap is narrower:

> Existing tool-using agent work rarely retrofits the specific Generative Agents cognitive loop and evaluates whether tool orchestration improves long-running social simulation reliability, memory faithfulness, plan validity, reflection evidence, and emergent social-network quality.

### 2.4 Gap relative to SpatialAgent v13/v13-A

SpatialAgent v13/v13-A asks whether LLM agents use controlled spatial structure in ways that transfer into emergent dialogue networks.

TGA asks a different but complementary question:

```text
SpatialAgent v13-A:
Do LLM agents use spatial structure?

TGA:
Can the GA cognitive architecture be made auditable and reliable enough to support such claims?
```

TGA can serve either as:

1. a **runtime layer** underneath v13-A, improving traceability and reproducibility; or
2. a **standalone follow-on paper** about auditable generative-agent architecture.

---

## 3. Core Claim

The clean claim is not:

> We make agents call tools.

That is too broad and already common.

The clean claim is:

> A GA-style cognitive loop can be reconstructed as an auditable tool-orchestrated architecture, improving memory faithfulness, plan validity, reflection evidence, and social-event traceability while preserving believable behavior and emergent interaction.

---

## 4. Positioning

### 4.1 What this project is

TGA is:

- a GA-specific architectural retrofit;
- an auditability and reliability study;
- a controlled evaluation of memory, planning, reflection, and interaction modules;
- a possible infrastructure layer for SpatialAgent v13-A;
- a bridge between believable social simulation and modern agent runtimes.

### 4.2 What this project is not

TGA is not:

- a generic tool-use paper;
- a new AutoGen / LangGraph / Agents SDK clone;
- a pure engineering reimplementation of Generative Agents;
- a cost-only optimization paper;
- a broad social-simulation platform paper;
- a replacement for SpatialAgent v13-A.

---

## 5. Research Questions

### RQ1: Memory faithfulness

> Does tool-mediated memory retrieval reduce unsupported recall and improve evidence-grounded answers compared with vanilla GA retrieval?

### RQ2: Retrieval quality

> Does an explicit retrieval tool with typed filters and provenance improve retrieval precision for agent interviews, dialogue generation, and reaction decisions?

### RQ3: Plan validity

> Does explicit plan validation reduce impossible, conflicting, repeated, or context-inconsistent plans without making behavior less believable?

### RQ4: Reflection provenance

> Does a tool-orchestrated reflection module increase the proportion of reflections that are supported by traceable evidence?

### RQ5: Social-event auditability

> Does making interactions and dialogue edges first-class logged events improve the reliability of emergent social-network construction?

### RQ6: Believability preservation

> Can TGA improve auditability and reliability while preserving the believable individual and social behavior demonstrated by the original GA architecture?

### RQ7: Optional spatial extension

> When integrated with SpatialAgent v13-A, does TGA preserve or improve measured spatial-to-social coupling while making the mechanism more auditable?

---

## 6. Hypotheses

### H1: Memory

TGA improves memory faithfulness compared with vanilla GA.

| Field | Specification |
|---|---|
| Unit | agent x interview question x run |
| Primary response | evidence-supported answer rate |
| Main contrast | TGA > Vanilla GA |
| Expected direction | positive |

### H2: Retrieval

TGA improves retrieval precision without reducing necessary recall.

| Field | Specification |
|---|---|
| Unit | retrieval call |
| Primary response | precision@k / evidence relevance |
| Main contrast | TGA retrieval tool > vanilla GA retrieval prompt/context assembly |
| Expected direction | positive |

### H3: Planning

TGA reduces invalid or inconsistent plans.

| Field | Specification |
|---|---|
| Unit | plan segment / action segment |
| Primary response | invalid-plan rate |
| Main contrast | TGA plan validator < Vanilla GA |
| Expected direction | negative |

### H4: Reflection

TGA increases reflection evidence traceability.

| Field | Specification |
|---|---|
| Unit | generated reflection |
| Primary response | supported-reflection rate |
| Main contrast | TGA > Vanilla GA |
| Expected direction | positive |

### H5: Social network

TGA improves social-event auditability while preserving non-degenerate emergent dialogue networks.

| Field | Specification |
|---|---|
| Unit | run |
| Primary response | valid dialogue-edge rate; network non-degeneracy |
| Main contrast | TGA >= Vanilla GA |
| Expected direction | positive for auditability; non-inferior for network richness |

### H6: Cost and latency

TGA reduces prompt bloat and repeated context injection, but may introduce tool-call overhead. Cost and latency are secondary outcomes.

| Field | Specification |
|---|---|
| Unit | run / agent turn |
| Primary response | tokens, wall-clock latency, tool calls |
| Main contrast | TGA vs Vanilla GA / AGA |
| Expected direction | lower input tokens; latency uncertain |

---

## 7. Proposed Architecture

### 7.1 High-level pipeline

```text
Perceive
-> Typed Event Logger
-> Memory Store
-> Retrieval Tool
-> Planning Tool / Plan Validator
-> Reflection Tool
-> Interaction Tool / Dialogue Logger
-> Optional Spatial Query Tool
-> Trace Store
-> Analysis Outputs
```

### 7.2 Key design principle

The LLM should not receive a large, loosely assembled prompt whenever possible. Instead, it should access structured state through explicit tools whose calls are logged.

```text
Vanilla GA:
assemble relevant text -> prompt LLM -> parse output

TGA:
call tools -> receive typed evidence -> prompt LLM with bounded evidence -> validate/log output
```

---

## 8. Modules

### 8.1 Typed Memory Store

Every memory is stored as a typed object rather than only a natural-language text entry.

Required fields:

```json
{
  "memory_id": "mem_000001",
  "agent_id": "agent_klaus",
  "created_at": "2026-05-18T09:00:00",
  "last_accessed_at": "2026-05-18T10:00:00",
  "memory_type": "observation | dialogue | reflection | plan | user_intervention | environment_event",
  "text": "Klaus talked with Maria about his research project at the cafe.",
  "actors": ["agent_klaus", "agent_maria"],
  "location": "cafe",
  "event_id": "event_000121",
  "importance": 7,
  "embedding_id": "emb_000001",
  "source": "perception | dialogue_logger | reflection_tool | user_input",
  "evidence_ids": [],
  "confidence": 1.0
}
```

### 8.2 Retrieval Tool

The retrieval tool returns memory IDs, scores, and reasons rather than raw unbounded context.

API sketch:

```python
def retrieve_memory(
    agent_id: str,
    query: str,
    k: int = 10,
    memory_types: list[str] | None = None,
    actors: list[str] | None = None,
    location: str | None = None,
    time_window: tuple[str, str] | None = None,
    require_evidence: bool = True
) -> list[RetrievedMemory]:
    ...
```

Returned object:

```json
{
  "memory_id": "mem_000121",
  "text": "Maria invited Klaus to the Valentine's Day party.",
  "score_total": 0.87,
  "score_recency": 0.76,
  "score_importance": 0.90,
  "score_semantic": 0.85,
  "score_spatial": 0.70,
  "reason": "Same interlocutor and party-related query."
}
```

### 8.3 Plan Generator and Plan Validator

Planning remains LLM-assisted, but validation is explicit.

API sketch:

```python
def generate_plan(agent_id, date, goals, constraints, retrieved_memory_ids):
    ...

def validate_plan(plan, calendar_state, location_graph, object_state, social_constraints):
    ...

def repair_plan(plan, validation_errors):
    ...
```

Validation categories:

```text
time conflict
location impossible
object unavailable
repeated mundane action
role inconsistency
social inconsistency
spatial impossibility
unsafe or policy-invalid action
```

### 8.4 Reflection Tool

Reflection should create evidence-grounded abstract memories.

API sketch:

```python
def should_reflect(agent_id, recent_event_ids, importance_sum, social_change=None, spatial_change=None):
    ...

def generate_reflection_questions(agent_id, memory_ids):
    ...

def write_reflection(agent_id, insight, evidence_ids):
    ...
```

Every reflection must include evidence IDs.

Example:

```json
{
  "reflection_id": "ref_000033",
  "agent_id": "agent_klaus",
  "text": "Klaus sees Maria as a close academic peer.",
  "evidence_ids": ["mem_000102", "mem_000118", "dialogue_000021"],
  "support_status": "supported"
}
```

### 8.5 Interaction Tool and Dialogue Logger

Social interactions should be logged as first-class events.

API sketch:

```python
def detect_encounter(agent_a, agent_b, location, time):
    ...

def decide_interaction_type(agent_a, agent_b, context):
    # skip | greet | short_chat | full_dialogue | information_handoff
    ...

def log_dialogue_event(agent_a, agent_b, location, round_id, utterances, topic_tags):
    ...
```

Output fields:

```json
{
  "event_id": "event_000201",
  "event_type": "social",
  "agent_id": "agent_klaus",
  "target_id": "agent_maria",
  "location": "cafe",
  "round": 42,
  "dialogue_id": "dialogue_000044",
  "edge_weight_increment": 1,
  "event_source": "dialogue_logger"
}
```

### 8.6 Optional Spatial Query Tool

This module should be included only if TGA is integrated with SpatialAgent v13-A.

API sketch:

```python
def query_location(location_id):
    return {
        "integration_z": 1.23,
        "depth_z": -0.44,
        "control_z": 0.70,
        "neighbors": ["cafe", "park", "market"]
    }

def query_path(source, target):
    ...

def query_nearby_agents(agent_id, radius=1):
    ...
```

Important rule:

> The spatial query tool should support controlled experimental conditions such as topology-only, configurational perception, non-spatial control, and shuffled mapping. It must not leak the correct spatial mechanism into control conditions.

---

## 9. Experimental Conditions

### 9.1 Minimal standalone TGA conditions

| Condition | Internal key | Description | Role |
|---|---|---|---|
| Vanilla GA | `GA` | Original prompt-chain memory/retrieval/reflection/planning | baseline |
| TGA-memory | `TGA_M` | Typed memory and retrieval tools only | memory ablation |
| TGA-memory-plan | `TGA_MP` | Typed memory + plan validation | planning ablation |
| Full TGA | `TGA_FULL` | Memory, planning, reflection, interaction logging | main treatment |
| AGA | `AGA` | Affordable Generative Agents-style cost baseline | optional baseline |

### 9.2 SpatialAgent-integrated conditions

If integrated with v13-A, preserve the v13-A condition ladder:

| Condition | Meaning |
|---|---|
| `C1` | topology-only |
| `C2c` | non-spatial information-volume control |
| `C6m` | correctly mapped configurational perception |
| `C_shuffle` | shuffled spatial descriptor mapping |

Then compare runtime variants:

```text
GA-runtime vs TGA-runtime
```

The full factorial design can become too large. Recommended first spatial integration:

```text
3 maps x 5 seeds x 4 spatial conditions x 2 runtimes = 120 runs
```

This is already comparable in scale to the v13-A MVP.

---

## 10. Evaluation Metrics

### 10.1 Memory metrics

| Metric | Definition |
|---|---|
| evidence-supported answer rate | fraction of interview answers supported by logged memories |
| unsupported recall rate | fraction of answers containing claims not supported by memory |
| memory hallucination rate | fraction of claims about events that never occurred |
| retrieval precision@k | fraction of top-k retrieved memories judged relevant |
| retrieval recall proxy | whether known seeded critical memories appear in retrieved set |
| source attribution completeness | fraction of answers citing sufficient memory IDs |

### 10.2 Planning metrics

| Metric | Definition |
|---|---|
| invalid-plan rate | fraction of plan segments failing validation |
| repair success rate | fraction of invalid plans repaired successfully |
| repeated-action rate | repeated mundane activities within implausible time windows |
| time-conflict rate | overlapping incompatible activities |
| location-validity rate | plan locations reachable and appropriate under current map state |
| object-validity rate | required object exists and is in usable state |

### 10.3 Reflection metrics

| Metric | Definition |
|---|---|
| supported-reflection rate | reflections with sufficient evidence IDs |
| unsupported-reflection rate | reflections with weak or missing evidence |
| evidence diversity | number of distinct memory sources supporting reflections |
| reflection usefulness | retrieval/use frequency of reflections in later behavior |
| reflection drift | degree to which reflections overgeneralize beyond evidence |

### 10.4 Social interaction metrics

| Metric | Definition |
|---|---|
| valid social-event rate | events supported by actual dialogue logs |
| dialogue-edge auditability | fraction of network edges traceable to event IDs |
| relationship-update support | relationship changes backed by dialogue evidence |
| information-handoff support | diffusion claims backed by utterance-level evidence |
| network non-degeneracy | dialogue network not empty, complete, or trivially structured |

### 10.5 Believability metrics

Use believability as a preservation endpoint, not the only success criterion.

| Metric | Definition |
|---|---|
| GA-style interview score | self-knowledge, memory, planning, reaction, reflection |
| human or LLM believability rating | blind rating of behavior traces |
| social plausibility | whether dialogues and relationships are consistent |
| role consistency | whether agent behavior remains compatible with profile |

### 10.6 Cost and runtime metrics

| Metric | Definition |
|---|---|
| total input tokens | prompt tokens consumed |
| total output tokens | generated tokens consumed |
| LLM calls | number of model calls |
| tool calls | number and type of tool calls |
| wall-clock latency | runtime per simulated day |
| trace storage size | log overhead |

---

## 11. Experimental Stages

### Stage 0: Literature and baseline audit

Purpose:

```text
confirm that the novelty is GA-specific auditability, not generic tool use
```

Tasks:

- review GA, AGA, CoALA, CoAG, AutoGen-like frameworks, Agents SDK, LangGraph, Concordia, AgentSociety;
- write a related-work matrix;
- freeze the paper claim;
- decide whether TGA is standalone or a v13-A runtime layer.

Exit condition:

```text
The gap statement does not claim generic tool use as novelty.
```

### Stage 1: Module-level tests

Purpose:

```text
test whether individual tools improve measurable reliability
```

Tests:

- memory retrieval benchmark;
- plan validation benchmark;
- reflection evidence benchmark;
- dialogue event logging benchmark.

Exit condition:

```text
At least two of memory, planning, reflection, or logging show measurable improvement over vanilla GA.
```

### Stage 2: Controlled interview evaluation

Purpose:

```text
test whether TGA improves GA-style agent interviews
```

Use interview categories similar to GA:

```text
self-knowledge
memory
planning
reaction
reflection
```

Primary comparison:

```text
GA vs TGA_FULL
```

Secondary ablations:

```text
TGA_M, TGA_MP
```

### Stage 3: Long-run multi-agent simulation

Purpose:

```text
test whether TGA preserves believable social emergence while improving auditability
```

Suggested MVP:

```text
3-agent environment x 10 seeds x 2 days x {GA, TGA_FULL}
```

Optional extended run:

```text
25-agent Smallville-like environment x fewer seeds
```

Outputs:

```text
memory logs
retrieval logs
plan logs
validation logs
reflection logs
dialogue logs
network files
trace files
metrics files
```

### Stage 4: Optional SpatialAgent integration

Purpose:

```text
test whether TGA supports v13-A claims with better auditability
```

Primary question:

> Does TGA preserve spatial-to-social coupling while improving traceability of the underlying mechanism?

Use v13-A H1/H2/H3 only if this becomes part of the SpatialAgent paper. Otherwise keep it as an appendix or follow-on experiment.

---

## 12. Statistical Analysis

### 12.1 Independent unit

The primary independent unit is the run.

Do not treat agents, memories, dyads, or dialogue turns as independent without clustering or run-level aggregation.

### 12.2 Paired-seed design

Prefer paired seeds across conditions:

```text
seed_i under GA
seed_i under TGA_FULL
```

This controls randomness in agent profiles, schedules, environmental events, and user-seeded events.

### 12.3 Primary tests

| Hypothesis | Recommended test |
|---|---|
| H1 memory | mixed model or paired run-level comparison of evidence-supported answer rate |
| H2 retrieval | retrieval-call-level model clustered by run and agent |
| H3 planning | invalid-plan rate aggregated per run |
| H4 reflection | supported-reflection rate aggregated per run |
| H5 social network | run-level valid-edge rate and network non-degeneracy comparison |
| H6 cost | paired comparison of tokens, calls, and latency |

### 12.4 Multiple comparisons

Primary family:

```text
H1 memory
H3 planning
H4 reflection
H5 social-event auditability
```

Secondary outcomes:

```text
cost
latency
believability
spatial H1/H2/H3
```

Use FDR control within the primary family.

---

## 13. Success Criteria

### Minimum success

The project is worth continuing if TGA shows:

```text
memory faithfulness improvement
or plan validity improvement
or social-event auditability improvement
```

without a major drop in believability.

### Strong success

The project becomes a strong standalone paper if TGA shows:

```text
memory faithfulness improvement
+ plan validity improvement
+ reflection evidence improvement
+ social-event auditability improvement
+ preserved believable behavior
```

### Best-case success

The strongest result is:

```text
TGA improves reliability and auditability
while reducing prompt tokens
and preserving emergent dialogue-network structure
under both Smallville-like and SpatialAgent-style environments.
```

---

## 14. Result Tiers

| Tier | Memory | Planning | Reflection | Social auditability | Believability | Interpretation |
|---|---|---|---|---|---|---|
| Tier 1 | positive | positive | positive | positive | preserved | strong TGA architecture paper |
| Tier 2 | positive | positive | mixed | positive | preserved | strong reliability paper |
| Tier 3 | positive | mixed | mixed | positive | preserved | audit/runtime contribution |
| Tier 4 | mixed | mixed | mixed | positive | preserved | engineering infrastructure only |
| Tier 5 | mixed | mixed | mixed | mixed | degraded | do not submit as main paper |

---

## 15. Downgrade Rules

| Pattern | Downgrade |
|---|---|
| TGA only reduces tokens | frame as cost engineering, not auditable cognition |
| TGA only improves trace logging | frame as infrastructure, not agent architecture |
| TGA improves module tests but not long-run behavior | frame as component benchmark |
| TGA reduces believability | do not claim improvement over GA |
| TGA depends on unblinded LLM judging | downgrade evaluation strength |
| TGA requires vendor-specific framework features | frame as implementation-specific, not general architecture |
| Spatial results disappear under TGA | do not combine with v13-A as main claim |
| Tool calls simply expose hidden gold labels | invalid mechanism; redesign controls |

---

## 16. Main Risks

### 16.1 Novelty risk

Risk:

```text
Reviewers say tool orchestration is already common.
```

Control:

```text
Position the novelty as GA-specific auditability and long-running social-simulation evaluation.
```

### 16.2 Scope creep

Risk:

```text
The project expands into a general agent platform.
```

Control:

```text
Keep only four primary modules: memory, planning, reflection, interaction logging.
```

### 16.3 Over-instrumentation

Risk:

```text
Too much validation makes behavior rigid and less believable.
```

Control:

```text
Believability preservation is a required endpoint.
```

### 16.4 Judge artifact

Risk:

```text
LLM evaluators reward structured traces rather than true behavior quality.
```

Control:

```text
Use rule-based metrics where possible and blind human or LLM judges to condition.
```

### 16.5 Tool leakage

Risk:

```text
Tools reveal information unavailable to the agent.
```

Control:

```text
Every tool must enforce condition-specific access rules.
```

### 16.6 Runtime overhead

Risk:

```text
Tool calls increase latency or engineering complexity.
```

Control:

```text
Measure latency separately from token cost and report trade-offs explicitly.
```

---

## 17. Required Outputs

Each run should produce:

```text
results/tga/{env}/{seed}/{condition}/metadata.json
results/tga/{env}/{seed}/{condition}/events.jsonl
results/tga/{env}/{seed}/{condition}/memories.jsonl
results/tga/{env}/{seed}/{condition}/retrieval_calls.jsonl
results/tga/{env}/{seed}/{condition}/plans.jsonl
results/tga/{env}/{seed}/{condition}/plan_validations.jsonl
results/tga/{env}/{seed}/{condition}/reflections.jsonl
results/tga/{env}/{seed}/{condition}/dialogues.jsonl
results/tga/{env}/{seed}/{condition}/tool_trace.jsonl
results/tga/{env}/{seed}/{condition}/network_dialogue.graphml
results/tga/{env}/{seed}/{condition}/metrics_run.json
```

Required `tool_trace.jsonl` fields:

```text
trace_id
timestamp
agent_id
tool_name
input_hash
output_hash
visible_to_agent
condition
source_event_id
latency_ms
status
```

Required `retrieval_calls.jsonl` fields:

```text
call_id
agent_id
query
k
filters
returned_memory_ids
score_components
used_in_prompt
downstream_decision_id
```

Required `plan_validations.jsonl` fields:

```text
validation_id
agent_id
plan_id
valid
error_types
error_messages
repair_attempted
repair_success
```

Required `reflections.jsonl` fields:

```text
reflection_id
agent_id
text
evidence_ids
support_status
created_at
used_later
```

---

## 18. Implementation Binding

### 18.1 Proposed files

| Need | Proposed path |
|---|---|
| TGA configs | `spatial-agent-core/configs/experiments/tga_conditions.yaml` |
| runtime config | `spatial-agent-core/configs/experiments/exp_tga_main.yaml` |
| run launcher | `spatial-agent-core/experiments/run_tga.py` |
| memory store | `spatial-agent-core/src/tga/memory_store.py` |
| retrieval tool | `spatial-agent-core/src/tga/tools/retrieval.py` |
| planning tool | `spatial-agent-core/src/tga/tools/planning.py` |
| plan validator | `spatial-agent-core/src/tga/tools/plan_validator.py` |
| reflection tool | `spatial-agent-core/src/tga/tools/reflection.py` |
| interaction logger | `spatial-agent-core/src/tga/tools/interaction_logger.py` |
| trace collector | `spatial-agent-core/src/tga/tracing.py` |
| evaluation metrics | `spatial-agent-core/src/analysis/tga_metrics.py` |
| hypothesis tests | `spatial-agent-core/src/analysis/tga_hypotheses.py` |

### 18.2 Required docs

| Document | Proposed path |
|---|---|
| output schema | `spatial-agent-core/docs/tga_output_schema.md` |
| tool access policy | `spatial-agent-core/docs/tga_tool_access_policy.md` |
| evaluation manual | `spatial-agent-core/docs/tga_evaluation_manual.md` |
| preregistration draft | `spatial-agent-core/docs/tga_preregistration.md` |
| relation to v13-A | `spatial-agent-core/docs/tga_v13a_integration.md` |

---

## 19. Paper Structure

```text
1. Introduction
   - Generative agents are believable but hard to audit.
   - Modern tool-using agents exist, but GA-specific social-simulation reliability remains underexplored.
   - We introduce Auditable Generative Agents.

2. Background and Gap
   - Generative Agents
   - Affordable Generative Agents
   - Tool-using language agents and cognitive architectures
   - Why social-simulation auditability is still open

3. TGA Architecture
   - Typed memory store
   - Retrieval tool
   - Planning and validation tools
   - Reflection evidence tool
   - Interaction and dialogue event logging
   - Optional spatial query tool

4. Evaluation Protocol
   - Conditions
   - Environments
   - Metrics
   - Believability preservation
   - Auditability endpoints

5. Experiments
   - Module-level tests
   - Interview evaluation
   - Long-run simulation
   - Optional SpatialAgent integration

6. Results
   - Memory faithfulness
   - Plan validity
   - Reflection evidence
   - Social-event auditability
   - Believability and cost

7. Discussion
   - What tool orchestration fixes
   - What remains prompt-dependent
   - Relationship to v13-A
   - Limits of auditability

8. Limitations and Ethics

9. Conclusion
```

---

## 20. Relationship to SpatialAgent v13/v13-A

### Option A: TGA as implementation layer for v13-A

Use TGA tools to make v13-A logs more reliable.

Main v13-A claim remains:

```text
Do LLM agents use spatial structure?
```

TGA is described as:

```text
an auditable runtime used to record memory retrieval, spatial exposure, dialogue events, and network construction.
```

This is safest for the current SpatialAgent paper.

### Option B: TGA as a standalone paper

Main TGA claim becomes:

```text
Can GA-style cognitive loops be made more auditable and reliable through tool orchestration?
```

SpatialAgent becomes one evaluation environment.

This is better for a second paper.

### Recommendation

Do not merge full TGA and v13-A as two equal main claims in one paper.

Recommended path:

```text
Current paper:
v13-A main claim + light TGA runtime for logging/auditability

Follow-on paper:
Auditable Generative Agents / full TGA architecture
```

---

## 21. Execution Checklist

### Immediate

- [ ] Decide whether TGA is a runtime layer or standalone paper.
- [ ] Freeze the name: `Auditable Generative Agents` vs `Tool-Orchestrated Generative Agents`.
- [ ] Build related-work matrix: GA, AGA, CoALA, CoAG, AutoGen-like frameworks, Agents SDK, Concordia, AgentSociety.
- [ ] Freeze four primary modules: memory, planning, reflection, interaction logging.

### Before coding

- [ ] Define typed memory schema.
- [ ] Define retrieval call schema.
- [ ] Define plan validation rules.
- [ ] Define reflection evidence rules.
- [ ] Define dialogue-event logging rules.
- [ ] Define tool access policy.

### Stage 1

- [ ] Implement memory store and retrieval tool.
- [ ] Implement plan validator.
- [ ] Implement reflection evidence writer.
- [ ] Implement dialogue event logger.
- [ ] Run module-level tests.

### Stage 2

- [ ] Run GA-style interview benchmark.
- [ ] Compare memory faithfulness and planning validity.
- [ ] Check believability preservation.

### Stage 3

- [ ] Run long-run simulation.
- [ ] Construct dialogue network from logged events.
- [ ] Compare auditability and social-network non-degeneracy.

### Optional Stage 4

- [ ] Integrate with v13-A spatial conditions.
- [ ] Confirm tool access policy respects each condition.
- [ ] Test whether spatial H1/H2/H3 are preserved under TGA runtime.

---

## 22. Final Positioning

The strongest positioning is:

> Generative Agents made LLM-based social simulation believable. Affordable Generative Agents made it cheaper. TGA asks whether it can be made auditable.

The key slogan:

```text
From believable outputs to auditable mechanisms.
```

The paper should avoid claiming that tool use is new. The contribution is the **GA-specific reconstruction and evaluation** of memory, planning, reflection, and social interaction as traceable tool-mediated mechanisms.
