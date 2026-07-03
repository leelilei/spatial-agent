---
title: "TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation"
source_pdf: "08_route_planning_agents\\03_TrajGenAgent_Li2026.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-07-03T12:08:25+00:00
page_count: 14
status: ok
text_char_count: 73959
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\08_route_planning_agents\03_TrajGenAgent_Li2026.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-07-03T12:08:25+00:00
- Page count: 14
- Status: ok
- Text chars: 73959
- Quality flags: none

## Metadata

- Title: TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation
- Author: Siyu Li; Toan Tran; Lingyi Zhao; Khurram Shafique; Li Xiong
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

—Human mobility data is essential for transportation urban planning, and epidemic control. Yet large-scale trajectory collection is often costly and restricted by privacy concerns motivating the need for realistic synthetic mobility trajectory generation. Recent LLM-based generators typically follow two paradigms: (i) prompt engineering, which provides efficient zero shot generation with general prior knowledge but lacks fine grained spatiotemporal grounding; and (ii) fine-tuning with structured trajectories, which achieves strong spatiotempora precision but incurs substantial computational cost and may weaken general reasoning. Tool-augmented agents are emerging but remain at an early stage and still lack effective coordination between high-level planning and low-level realization. To address these limitations, we propose TrajGenAgent, a semantic-aware hierarchical LLM-agent framework for trajectory generation without model fine-tuning. TrajGenAgent adopts a two-stage orchestrator–worker design that decouples macro-level activity structure from micro-level spatiotemporal dynamics. In the first stage, an LLM synthesizes an activity chain for a given individual and day of the week via in-context learning over historic examples. In the second stage, a deterministic workflow instantiates each activity visit with distance-aware rule-based lo cation retrieval and LLM augmented kinematics-aware tempora generation. Traditional evaluation metrics for synthetic mobility data primarily assess aggregate spatiotemporal statistics, which do not capture behavioral fidelity or realism of individual trajec tories. To address this limitation, we introduce an anomaly detection-based evaluation framework with two complementary anomaly detectors that provide behavior & semantic feedback beyond macro-level statistical consistency. Experiments on both benchmark and large-scale simulation datasets show that TrajGe nAgent outperforms baselines in both spatiotemporal statistica metrics while also improving semantic coherence and individual specific behavior fidelity, all without parameter updates.

## Outline

- Introduction (page 1)
- Related Work (page 3)
- TrajGenAgent Framework (page 4)
  - Trajectory Representation and Problem Setup (page 4)
  - TrajGenAgent Overview (page 4)
  - Stage 1: Orchestrator for Activity-Chain Generation (page 5)
    - Evidence construction from individual history (page 6)
    - Evidence-based activity chain generation with verification (page 6)
    - Why evidence-based activity chain generation outperforms fine-tuning for personalization (page 6)
  - Stage 2: Workflow-based Spatiotemporal Grounding (page 6)
    - Location Grounding (page 6)
    - Travel Time (page 7)
    - Duration estimation (page 7)
- Experiments (page 7)
  - Datasets & Preprocessing (page 7)
  - Baselines (page 8)
  - Evaluation Metrics (page 8)
    - Aggregation-level Spatiotemporal Statistics Metrics (page 8)
    - Anomaly-Detection Evaluation (page 8)
  - Implementation Details (page 9)
  - Aggregation-level Spatiotemporal Statistics (page 9)
  - Anomaly-Detection Evaluation (page 9)
  - Computational Efficiency (page 10)
  - Tool-Invocation Stability: Deterministic Workflow vs. Free-form Tool Calling (page 10)
  - Ablation Study: Kinematics-aware Grounding (page 11)
  - Parameter Study: LLM Sampling Temperature Impacts (page 11)
- Conclusion (page 11)
- References (page 13)

## Markdown Content

TrajGenAgent: A Hier
Human Mobility T
Siyu Li†, Toan Tran†, Lingyi Zh
† Dept. of Computer Science, E
‡ Novateur Research So
{siyu.li, viet.toan.tran, lxiong}@em
Abstract—Human mobility data is essential for transportation
urban planning, and epidemic control. Yet large-scale trajectory
collection is often costly and restricted by privacy concerns
motivating the need for realistic synthetic mobility trajectory
generation. Recent LLM-based generators typically follow two
paradigms: (i) prompt engineering, which provides efficient zero
shot generation with general prior knowledge but lacks fine
grained spatiotemporal grounding; and (ii) fine-tuning with
structured trajectories, which achieves strong spatiotempora
precision but incurs substantial computational cost and may
weaken general reasoning. Tool-augmented agents are emerging
but remain at an early stage and still lack effective coordination
between high-level planning and low-level realization. To address
these limitations, we propose TrajGenAgent, a semantic-aware
hierarchical LLM-agent framework for trajectory generation
without model fine-tuning. TrajGenAgent adopts a two-stage
orchestrator–worker design that decouples macro-level activity
structure from micro-level spatiotemporal dynamics. In the
first stage, an LLM synthesizes an activity chain for a given
individual and day of the week via in-context learning over
historic examples. In the second stage, a deterministic workflow
instantiates each activity visit with distance-aware rule-based lo
cation retrieval and LLM augmented kinematics-aware tempora
generation.
Traditional evaluation metrics for synthetic mobility data
primarily assess aggregate spatiotemporal statistics, which do
not capture behavioral fidelity or realism of individual trajec
tories. To address this limitation, we introduce an anomaly
detection-based evaluation framework with two complementary
anomaly detectors that provide behavior & semantic feedback
beyond macro-level statistical consistency. Experiments on both
benchmark and large-scale simulation datasets show that TrajGe
nAgent outperforms baselines in both spatiotemporal statistica
metrics while also improving semantic coherence and individual
specific behavior fidelity, all without parameter updates.
Index Terms—Human Mobility Trajectory Generation, LLM
Agent, Orchestrator–Worker Architecture, Zero-Shot Reasoning
Workflow-Based Tool Integration
I. INTRODUCTION
Human mobility data, represented as trajectories or sequences of visits, is essential for advancing research and
applications in transportation, urban planning, social dynamics, and epidemiology [1]–[3]. However, collecting largescale trajectory data is often constrained by high costs and
privacy concerns, making real-world mobility datasets difficul
to access [4]. This has motivated the development of synthetic
yet realistic trajectory generation methods.
Existing Approaches and Limitations. Early approaches
relied on micro-simulators calibrated using sensor data, traf6202
nuJ
01
]IA.sc[
1v75621.6062:viXra

rchical LLM Agent for
ajectory Generation
, Khurram Shafique‡, Li Xiong†
y University, Atlanta, GA, USA
ons, Ashburn, VA, USA
edu, {lzhao, kshafique}@novateur.ai
fic statistics, and handcrafted behavioral rules [5]. Such
simulation-based methods require careful parameter tuning
and often fail to capture complex mobility patterns due to
over-simplified heuristics [6]. More recent data-driven models, including Generative Adversarial Networks (GAN) and
spatiotemporal point processes, learn mobility distributions
directly from data to generate large-scale trajectories [7]–[10].
However, they often suffer from training instability, scalability
imitations, remain limited in modeling long-range and complex dependencies, and lack explicit semantic understanding
of human routines.
With the emergence of Large Language Models (LLMs)
[11], recent studies have begun to leverage their powerful
sequence modeling and reasoning capabilities for trajectory
generation [12]–[14]. Existing LLM-based methods can be
categorized by how spatiotemporal knowledge is integrated:
(1) language-level approaches, including pure prompting that
relies on semantic priors [15] and lightweight text-based fineuning that inject global spatiotemporal knowledge in natural
anguage form [13]; (2) trajectory-level fine-tuning that encodes structured trajectories as token sequences [12]; and (3)
ool-augmented agent paradigms that externalizes spatiotemporal grounding by invoking dedicated tools or knowledge
sources during inference time [14], [16].
Language-level approaches preserve an LLM’s general
knowledge and adaptability, but offer limited capability of finegrained spatiotemporal pattern injection, often yielding trajecories that are semantically plausible yet poorly calibrated in
ime and space. In contrast, trajectory-level fine-tuning methods such as Geo-Llama [12] represent trajectories as sequences
of visits and adapt pretrained LLMs via parameter-efficient
fine-tuning (e.g., LoRA [17]). While achieving strong spaiotemporal fidelity, they introduce substantial computational
overhead and tightly entangle semantic reasoning with lowevel statistical pattern fitting, over-specializing the model and
reducing general reasoning capacity and control of individualevel semantic behaviors.
These observations reveal a fundamental tension: realistic
mobility generation requires both semantic coherence and finegrained spatiotemporal grounding. Here, semantic coherence
refers to the consistency of a generated trajectory with human activity logic, individual- and day-specific routines, and
activity–POI–time compatibility, while fine-grained groundng concerns the accurate reflection of location preferences,

Fig. 1: The TrajGenAgent framework. A hierarchical orches
synthesizes individual- and day-controlled activity-chain sc
deterministic LangGraph worker loop grounds each activity
/kinematics-aware travel-time propagation, and a context-awa
transition patterns, and temporal regularities. The above two
approaches struggle to achieve both simultaneously. Toolaugmented agent paradigms, while promising, remain at an
early stage and still lack effective coordination between highlevel behavioral planning and low-level spatiotemporal realization.
Challenges in LLM Agent based Mobility Generation
LLM agent based paradigm offers a principled solution to the
previously observed tension: the LLM serves as a semantic
reasoning and planning core, while external tools can injec
precise spatiotemporal evidence at inference time withou
requiring all domain knowledge to be encoded into mode
parameters [18], [19]. However, effectively leveraging LLM
agents for trajectory generation presents several challenges.
General LLM agent frameworks primarily differ in how they
structure and enforce tool invocation: 1) schema-registered
prompt-based calling, 2) supervised fine-tuning on functioncall traces for higher reliability (e.g., tool-calling specialized
models) [20], and 3) workflow-managed agents that organize
tool execution as a state machine to guarantee stable contro
flow and termination while reserving the LLM for steps
requiring semantic generalization [21].
A natural agent design for trajectory generation is to finetune or prompt an LLM to autonomously invoke tools via
structured function-call schemas [20]. However, trajectory
generation requires repeated, deterministic decisions for every
visit (location choice, travel-time propagation, duration estimation), which makes end-to-end autonomous tool calling fragile

or–worker LLM agent workflow, where a LLM orchestrator
lds via in-context learning over historical evidence, and a
o complete visits by peer-augmented POI retrieval, distanceconstraint-guided LLM duration module.
Schema compliance cannot be guaranteed at 100% for longhorizon trajectories; a single malformed or missed tool call
can leave missing fields (e.g., POI or time) and break visito-visit dependencies, trigger cascading errors that corrupt
subsequent steps and the overall daily schedule. Moreover,
supervised fine-tuning for tool-calling behavior introduces
additional training cost and may compromise generalization
capability due to catastrophic forgetting [16].
Workflow-managed orchestration offers a promising alternaive for stable and deterministic tool execution in long-horizon
rajectory generation. However, designing such workflows is
nontrivial: it requires structuring control flow, enforcing visitevel dependencies, and balancing deterministic execution with
semantic flexibility. To our knowledge, prior work has not
explored workflow design for trajectory generation.
Evaluation Gap in Mobility Generation. Beyond agent
design, a complementary challenge lies in how generated
rajectories are evaluated. Most trajectory-generation evaluaions rely on aggregate distributional distance metrics (e.g.,
Jensen–Shannon divergence (JSD) between real training data
and generated trajectories over travel distance, visit frequency,
or transition matrices) [8], [12]. These metrics quantify
population-level statistical similarity but often miss individualevel semantic defects—e.g., a location–time pattern that is
normal for one may be anomalous for another, even if global
statistics match.
Contributions. We propose TrajGenAgent, a zero-shot hierarchical agent framework that orchestrates heterogeneous

reasoning components within a deterministic workflow implemented using LangGraph [21]. By integrating LLM-based
reasoning with rule-based retrieval and explicit physical calculations, it ensures semantic-aware planning and physicsaware fine-grained spatiotemporal knowledge injection without costly model updates. As shown in Fig. 1, TrajGenAgen
decomposes generation into a macro-to-micro pipeline. In
Stage 1, an orchestrator LLM produces an activity-chain
scaffold (a semantic skeleton) via in-context learning over an
individual’s historical daily chains and contextual information
(personal attributes and day context). In Stage 2, specialized
worker modules transform each activity into a complete visi
through a predefined workflow that injects fine-grained spatiotemporal knowledge.
Concretely, Stage 2 consists of two specialized workers
a spatial worker and a temporal worker. The spatial worker
performs rule-based location retrieval using personal statistica
priors from a peer-augmented candidate pool constructed by
similarity matching across individuals. This enables controlled
exploration while restricting locations within a personalized
feasible set. A distance-aware mechanism further enforces
transition plausibility by aligning candidate locations with the
user’s historical activity-pair moving modalities, ensuring consistency with observed velocity and movement distributions
The temporal worker advances time by jointly inferring arriva
timestamps and stay durations. Specifically, it combines (i) a
kinematics-aware travel-time estimator that leverages movingmodality priors with (ii) an LLM-based duration module tha
respects time budget constraints. Given the generated history
and the remaining itinerary, the workflow iteratively calibrates
each visit’s arrival time and dwell time to maintain loca
transition plausibility and day-level schedule consistency. To
ensure robustness, lightweight verifiers supervise both workers
through schema-enforced fallbacks and feasibility constraints
which ensure both structural format and time validity.
Finally, to better evaluate behavior-level plausibility beyond
traditional aggregate statistical metrics, we propose a nove
anomaly-detection based evaluation framework. We use two
detectors with complementary emphases: ICAD which identifies local visit-wise inconsistencies [22] and BeSTAD which
captures user-level behavioral shifts [23]. Both are applied pos
hoc to assess the semantic coherence of generated trajectories
Our contributions are summarized as follows:
• Hierarchical LLM-Agent Framework. We propose TrajGenAgent, a zero-shot hierarchical LLM-agent framework that injects spatiotemporal knowledge at inference
time via a deterministic, verifier-guarded orchestrator–
worker workflow. By separating macro-level activitychain planning from visit-level grounding, TrajGenAgen
enables high-fidelity trajectory generation without costly
fine-tuning or fragile autonomous tool calling.
• Personalized and Physics-Aware Control. We enable
fine-grained personalized control over user- and dayspecific routines by constraining generation with historical evidence and configurable tool scopes, while enforcing time budgets and physics-aware mobility during

spatiotemporal grounding. This yields trajectories that are
both semantically coherent and faithful to fine-grained
spatiotemporal statistics.
• Behavior-Aware Evaluation Framework. We introduce
a novel evaluation framework that augments traditional
statistical metrics with two complementary anomaly detectors (ICAD and BeSTAD), trained to distinguish real
from abnormal or implausible trajectories, to assess the
semantic coherence of the generated trajectories.
• Comprehensive Experimental Evaluation. Experiments
on large scale datasets show that TrajGenAgent outperforms baselines on spatiotemporal statistical alignment and semantic coherence, without expensive parameter updates. Anomaly-detection results suggest that our
inference-time grounding with individualized evidence
and kinematics-aware priors preserves semantic plausibility and avoids detectable artifacts, while baselines
can still exhibit anomalous trajectory patterns despite
matching aggregate statistics, especially on behaviorally
diverse datasets.
II. RELATED WORK
Mobility Trajectory Generation without LLMs. Prior
o LLM-based approaches, mobility generation was dominated by simulation and neural-based generative modeling.
Simulation-based methods synthesize trajectories using handcrafted behavioral rules and physically motivated estimations
calibrated from sensors or surveys [24], [25]. They are often
brittle due to over-simplified heuristics. Data-driven models instead learn trajectory distributions directly from historical data.
A common formulation encodes mobility as a fixed-interval
spatiotemporal sequence, and learns next-step transitions with
recurrent backbones (e.g., RNN/LSTM variants) [26], [27].
Beyond one-step predictors, GAN-based generators improve
distribution matching by adversarial training [28], with representative variants including adversarial trajectory synthesis [9]
and reinforcement-learning-based sequence generation [6], [8],
[29]. Despite progress, fixed-interval representations produce
unnecessarily long sequences with repeated location states
and implicit time encoding, resulting in ambiguous temporal representation and degrades trajectory generation quality.
To address these limitations, recent work adopts visit-wise
rajectory and continuous-spatiotemporal formulations based
on deep spatiotemporal point processes (DeepSTPP) [10],
[30], which model trajectories as irregular visit sequences and
ointly capture where and when visits occur. However, these
generators remain limited in modeling long-range, complex
dependencies and lack explicit semantic understanding of
human routines and behavioral logic.
LLM-based Mobility Trajectory Generation. Recent studies
everage LLMs for mobility generation by exploiting their
strong sequence modeling and semantic reasoning capabiliies. They mainly differ in how fine-grained spatiotemporal
knowledge is incorporated.
a) Pure prompting-based generation: A representative
ine of work relies on pure prompt engineering to generate

plausible trajectories in a zero-shot manner [15]. For example, [13] crafts prompts using statistical summaries (e.g.
demographics, event types, and event–temporal correlations)
to emulate travel-diary-style generation without additiona
training. [31] further improves prompting via self-consisten
activity pattern identification and retrieval-augmented generation (RAG), using LLM priors to evaluate candidate promp
combinations conditioned on individual profiles and POI
background information. While prompting can exploit rich
contextual cues to produce semantically coherent, narrativelevel mobility routines, it typically lacks explicit injections of
fine-grained spatiotemporal information, which limits precise
micro-level spatiotemporal grounding.
b) Trajectory-level fine-tuning: In contrast, trajectorylevel fine-tuning injects spatiotemporal knowledge into mode
parameters by encoding structured trajectories as visit sequence prompts and fine-tuning pretrained LLMs with
parameter-efficient adapters such as LoRA [17]. Geo-Llama
[12] exemplifies this paradigm by optimizing a next-token prediction objective over discretized spatiotemporal visit tokens
and further introducing visit-wise permutation so the mode
learns temporal regularities from time features within visits
rather than from the original sequence order, yielding strong
micro-level spatiotemporal fidelity without external semantic
annotations. However, heavy adaptation on structured tokens
can introduce substantial computational overhead and entangle
semantic reasoning with low-level spatiotemporal statistics
reducing the general semantic capabilities and flexibility of
foundation models.
c) LLM agents and tool-augmented workflows: The
above limitations motivate an emerging paradigm that reframes LLMs as tool-augmented agents rather than monolithic
generators, enabling inference-time spatiotemporal knowledge
injection through modular interfaces without costly fine-tuning
or parameter updates [14], [18], [19]. Beyond domain knowledge, robust agentic generation often requires procedura
control over structured reasoning (e.g., CoT-style traces [32])
and tool usage (e.g., schema-registered function calls [19])
Existing agent frameworks typically enforce tool use via
three strategies: (i) supervised fine-tuning on tool-call traces
with explicit JSON/function-call schemas to improve invocation reliability (e.g., tool-calling specialized models such
as xLAM [20]); (ii) zero-shot prompting with schema/too
registration, leveraging strong foundation models that can
follow JSON-style interfaces (e.g., GPT4-OSS-120B [33])
and (iii) workflow-managed orchestration that encodes too
execution as an explicit state machine to guarantee stable
control flow and termination (e.g., LangGraph [21]). Such
workflow-managed agents can flexibly compose heterogeneous tools to inject spatiotemporal evidence at inference time
while preserving the LLM as a semantic planner. However
systematically designing reliable, long-horizon workflows for
mobility generation remains relatively under-explored [14].
GPS Trajectory Generation and POI Recommendation
Apart from human mobility trajectory generation, two closely
related topics study synthetic movement data under differen

objectives and representations.
GPS trajectory generation targets dense coordinate streams
at very fine-grained spatial and temporal resolution (e.g., persecond), instead of visit-wise trajectories that encode discrete
activities and human behavioral semantics. Early works synhesize GPS traces by perturbing real trajectories or recombinng trajectory segments [34], [35], which can distort spatiotemporal characteristics and reduce utility. Data-driven approaches
have also been explored, including GAN-based approaches
[36], [37] and diffusion-based models such as DiffTraj [38],
which learn fine-grained spatiotemporal dynamics from raw
GPS sequences. Due to this distinct granularity and goal, we
do not include GPS-trajectory generators in our comparisons.
Next point-of-interest (POI) recommendation predicts an
ndividual’s next POI conditioned on historical mobility and
context, typically framed as a sequential recommendation
problem, with limited or coarse temporal modeling. Prior work
spans probabilistic, deep learning, graph-based, and LLMbased recommenders [39]–[46]. In contrast, our task is traectory generation: synthesizing full-day visit sequences with
both visit-specific spatiotemporal fidelity and realistic global
dynamics, rather than focusing on one-step recommendation
accuracy. Although recommenders can be rolled out autoregressively, they often lack explicit mechanisms to maintain
ong-horizon coherence. Given these fundamental differences,
we do not treat POI recommendation methods as baselines for
our work.
III. TRAJGENAGENT FRAMEWORK
A. Trajectory Representation and Problem Setup
We represent a daily trajectory as a sequence of visits rather
han a fixed-interval time series. For an individual u on date
d, a trajectory is a sequence of visits:
T = [(a , p , ts, te)] Nu,d , (1)
u,d i i i i i=1
where a ∈ A is the activity type, p ∈ P is a POI identifier
i i
(with associated latitude/longitude), and ts, te are the start/end
i i
imestamps of the visit. The number of visits N varies by
u,d
ndividual and day, and we further define the visit duration as:
δ = te − ts. (2)
i i i
Given a historical trajectory dataset, an individual u and
arget date d, our goal is to generate a visit sequence T that
u,d
s realistic, reflecting both the individual’s historical mobility
and population-level behavioral patterns.
B. TrajGenAgent Overview
TrajGenAgent adopts a hierarchical orchestrator–worker
agent architecture implemented as a deterministic workflow
n LangGraph [21]. Given an individual u and target date d,
generation is decomposed into two stages:
Stage 1: Orchestrator Stage 2: Worker Workflow
(u, d, H ) −−−−−−−−−−−→ C −−−−−−−−−−−−−−→ T ,
u u,d u,d
(3)

where H is the historical repository, C = [a , . . . , N ] is
u u,d 1 u,d
an activity-chain semantic skeleton, and T is the final visi
u,d
trajectory.
Stage 1 (Orchestrator) performs semantic planning: i
prompts an LLM with individual-conditioned historical evidence (exemplar daily chains and compact statistical summaries) and synthesizes a plausible activity chain under hard
lexical and structural constraints. Stage 2 (Worker Workflow) performs spatiotemporal grounding: it deterministically
instantiates each activity into (p , ts, te) by executing a fixed
i i i
sequence of modules (POI retrieval, travel-time propagation
and duration estimation) until completion. In our implementation, both stages share the same instruction-tuned backbone
Qwen2.5-32B-Instruct [47], served via a vLLM [48] inference
server exposing an OpenAI API–compatible interface for highthroughput generation in the deterministic workflow.
a) Why deterministic workflow instead of free-form
tool calling: A natural alternative is to fine-tune an LLM
to autonomously invoke MCP-style tools through schemaconstrained outputs. We avoid this design for three reasons
(i) reliability—schema fine-tuning still cannot guarantee 100%
valid calls, while mobility generation repeatedly makes structured decisions at every visit; (ii) efficiency—tool-calling finetuning is compute-intensive and may weaken instructionfollowing robustness, whereas TrajGenAgent leverages strong
off-the-shelf instruction models at inference time; and (iii)
control/termination—free-form autonomous calling can drif
from global constraints, repeat locally, or loop, which is
especially harmful for long-horizon daily sequences. Encoding
the procedure as an explicit state machine yields bounded
execution, predictable control flow, and reproducibility.
b) Activity chain as a stabilizing intermediate: Introducing C decouples semantic planning from spatiotemu,d
poral realization, which simplifies long-horizon generation
and reduces error accumulation across visits. As a high-leve
scaffold, C anchors global day structure while allowing the
u,d
worker to inject deterministic mobility priors (e.g., distanceand speed-based feasibility) without requiring the LLM to
directly rank or search over large POI candidate sets.
c) Evidence-driven decisions with lightweight verifiers:
Across both stages, TrajGenAgent follows an evidence-todecision pattern: historical observations provide evidence (activity and transition tendencies, POI preferences, duration
statistics, and mobility priors), and workflow modules translate
this evidence into constrained decisions. Lightweight verifiers
enforce strict output schemas and feasibility bounds through
bounded checks and clipping; upon violations, the workflow
triggers deterministic repair or fallback to preserve structura
validity and schedule feasibility.
Overall, TrajGenAgent balances foundation-model semantic
generalization with deterministic spatiotemporal grounding
enabling reliable large-scale trajectory generation without finetuning while remaining extensible to richer semantic controls
and evaluator-in-the-loop feedback.

Fig. 2: The illustration of Stage 1 LLM semantic planning for
activity-chain generation.
C. Stage 1: Orchestrator for Activity-Chain Generation
Stage 1 generates a daily activity chain C =
u,d
a , . . . , a ] as a semantic plan for individual u on date
1 Nu,d
d. Rather than training a dedicated generator, the orchesrator leverages in-context learning (ICL) over individualconditioned evidence at inference time, enabling fine-grained
personalization even in narrow regimes (e.g., conditioning on a
specific weekday or day type). Figure 2 illustrates the promptevel semantic planning process used by the orchestrator.
From each individual’s historical trajectories, we construct
an evidence profile Π that characterizes individual prefu
erences and mobility regularities. In addition to activityand POI-level statistics, Π includes transition-level mobility
u
priors derived from consecutive visits using the great-circle
distance ℓ = dist(p , p ) and the observed inter-visit
i−1,i i−1 i
gap ts − te .
i i−1
(cid:110)
Π = π (a), π (a′ | a), π (p | a), µ (δ | a),
u u u u u
(4)
µ (cid:0) ℓ | a → a′(cid:1) , µ (cid:0) v | a → a′(cid:1) , µ (ts | w, a) (cid:111) ,
u u u 1
where π (a) is the activity occurrence likelihood, π (a′ | a)
u u
s the activity transition tendency, and π (p | a) is the activityu
conditioned POI preference. Here, π (·) denotes empirical
u
categorical distributions over discrete choices, while µ (·)
u
denotes empirical priors over continuous-valued quantities.
The remaining terms characterize empirical priors of visit
duration, transition distance, transition speed, and weekday-

conditioned first-start-time patterns (with w denoting the day
type or day-of-week).
1) Evidence construction from individual history: We construct daily activity chains from the individual-specific historical repository H by extracting each day’s visit sequence
u
in temporal order. For a target date d, we retrieve a datespecific evidence subset E ⊂ H using a prioritized policy
u,d u
(i) same weekday, (ii) same day type (weekday/weekend), and
(iii) fallback to all available days. From E we construct two
u,d
complementary evidence views:
• Exemplar evidence (ICL anchors): a small set of
historical chains presented verbatim as strong references
allowing the LLM to induce day structure via in-contex
pattern learning.
• Summary evidence (compact priors): compact activityfrequency and transition-tendency summaries derived
from the evidence profile Π in Eq. (4), which regularize
u
generation and reduce implausible chains.
2) Evidence-based activity chain generation with verification: The orchestrator LLM is prompted with (1) day-leve
controllable signals (e.g., day-of-week and day type), (2)
historical evidence in the form of exemplar activity chains
and compact statistical priors (e.g., activity frequencies and
transition tendencies), and (3) hard constraints, including a
fixed activity vocabulary and a no-adjacent-duplicate rule (with
an optional soft home-start/end prior). The output is restricted
to a Python list of activity strings. To ensure robustness, we
apply a bounded generate–verify loop:
• Schema check: parse the output as a list and rejec
malformed generations.
• Constraint check: enforce vocabulary membership, and
no-adjacent-duplicate constraints.
• Repair/fallback: retry briefly; if still invalid, fall back
to an evidence-derived default (e.g., a sampled historica
chain) to prevent error propagation to Stage 2.
3) Why evidence-based activity chain generation outperforms fine-tuning for personalization: Compared to fine-tuned
generators, this orchestrator is data-adaptive—it can specialize to a single individual or a weekday-specific routine
simply by adjusting the evidence scope—and offers finegrained controllability through the evidence selection policy
Moreover, by leveraging prompting-based in-context learning
it preserves the backbone model’s semantic generalization and
requires only inference-time compute (no parameter updates)
yielding a personalized and semantically coherent scaffold for
Stage 2 grounding.
D. Stage 2: Workflow-based Spatiotemporal Grounding
Given the semantic skeleton C = [a , . . . , a ], Traju,d 1 Nu,d
GenAgent finalizes a complete visit trajectory by executing a
deterministic state-machine workflow (implemented in LangGraph) over i = 1 . . . N . The worker workflow maintains
u,d
a shared state (e.g., visit index, previous POI, current time
and partial trajectory) that each module reads and updates to

propagate visit-to-visit dependencies, and then applies a fixed
module order for each visit:
location_node → travel_time_node
(5)
→ duration_node.
This ordering is deliberate: location grounding provides
he spatial context required for travel-time propagation and
duration scheduling, while each module reads and writes wellscoped state fields, preventing tool-call drift and ensuring
reproducible long-horizon generation.
1) Location Grounding : For each activity visit a , we
i
ground a location in two steps: (1) construct a feasible
candidate POI set P (a ), and (2) score candidates by combini
ng their likelihood under user/similar-user preferences with
distance-compatibility, then sample accordingly.
a) Candidate construction with feasible set and conrolled exploration: For each activity a , we retrieve a cani
didate POI set rather than sampling from the full location
space. We first build an individual-specific feasible set P (a )
u i
from historical visits. To enable controlled exploration beyond personal history, we augment candidates using a topK similar-individual pool obtained via similarity matching
over mobility signatures (e.g., spatial scale, temporal rhythm,
and activity/transition distributions, optionally with co-location
signals).
This yields an augmented location memory P (a ) from
sim i
similar individuals, and we take P(a ) = P (a ) ∪ P (a ).
i u i sim i
If P(a ) is empty, we emit an explicit invalid marker (rather
i
han silently sampling) to avoid cascading errors.
b) Distance-aware scoring and stochastic selection: To
choose a plausible next POI, we score each candidate by combining likelihood (how likely the user or similar users visits it
for this activity) with distance based feasibility (how consistent
he travel distance is with the user’s typical transitions). For
each candidate p ∈ P(a ), we compute a composite score:
i
S(p) = λ · s (p) + λ · s (p), (6)
f freq d dist
where the frequency prior mixes individual and neighbor
preferences with exploration gate α:
s (p) = (1 − α) P (p | a ) + α P (p | a ). (7)
freq u i sim i
The exploration gate α balances individual fidelity and conrolled diversity. Moderate changes in α have limited impact
on our statistical or anomaly metrics, but α = 0 can yield
near-copy trajectories with lower downstream utility, while excessive peer weighting may drift beyond the target individual’s
mobility scope.
To enforce physically plausible transitions, distance compatibility is measured against the previous grounded POI p
i−1
and the individual’s historical transition-distance regime for
(a , a ):
i−1 i
s dist (p) = exp (cid:0) −β · (cid:12) (cid:12)dist(p i−1 , p) − ℓ¯ u (a i−1 , a i ) (cid:12) (cid:12) (cid:1) , (8)
where dist(·, ·) is the Haversine distance and ℓ¯ (a , a )
u i−1 i
s the individual-specific mean transition distance (with robust defaults if unavailable). Finally, we sample p from the
i
normalized {S(p)}, yielding stochastic yet profile-constrained

location grounding with built-in personalization and controlled
exploration, without any model fine-tuning.
2) Travel Time: Given the grounded POIs {p }
Nu,d
and aci i=1
tivities {a }
Nu,d,
the temporal worker constructs an irregular
i i=1
daily timeline by iteratively producing each visit’s start time
ts and duration δ (thus end time te). Time is treated as a firsti i i
class continuous variable, avoiding the granularity loss from
fixed-bin discretization and enabling explicit feasibility contro
through budget and kinematic priors.
a) Cold-start initialization for the first visit: For i = 1
we initialize ts from an individual- and weekday-conditioned
1
prior of the first-visit start time estimated from history. If
unavailable, we fall back to a conservative default (e.g., morning start) and add a small random offset to avoid degenerate
identical schedules across days.
b) Distance- and kinematics-aware travel-time propagation: For i > 1, the workflow advances time using a traveltime estimate driven by (i) the geographic distance between
consecutive POIs and (ii) an individual-specific kinematic
prior captured by historical transition speeds:
ts = te + ∆ttravel,
i i−1 i
(cid:18) dist(p , p ) (cid:19) (9)
∆ttravel = clip i−1 i · 60, ∆ , ∆ .
i v (a , a ) min max
u i−1 i
Here dist(·, ·) is the Haversine distance, v (a , a ) is the
u i−1 i
historical mean speed for transition (a → a ), and clip(·)
i−1 i
enforces pre-defined time feasibility bounds (e.g., ∆ = 5
min
min, ∆ = 180 min). When v is missing or unreliable, we
max u
use robust defaults based on distance regime (e.g., walk vs
drive), preserving kinematic plausibility without requiring the
LLM to reason over high-dimensional mobility dynamics.
3) Duration estimation: Unlike travel time, activity duration is highly context-dependent (e.g., Work vs. EatOut)
and may adapt under schedule pressure. We therefore delegate
duration estimation to an LLM worker that conditions on
retrieved evidence and the current generation state:
• current start time ts i and remaining daily time budget,
• current activity a i and its historical duration prior,
• remaining activities [a i+1 , . . . , a Nu,d ] and their expected
total time,
• optional individual-specific duration tendencies.
The LLM outputs a strict JSON object (e.g.
{"duration_minutes": 45}). A lightweigh
verifier enforces schema validity and feasibility
δ ∈ [δ , min(δ , budget left)], with retry-on-violation
i min max
and deterministic fallback to the historical prior if parsing or
validation fails. This evidence-to-decision design preserves
semantic flexibility in duration choices while guaranteeing
coherent and time-feasible execution. Finally, we update the
end time as te = ts + δ , and proceed to the next visit
i i i
cumulatively generating a full-day irregular timeline that is
semantically coherent and physically feasible.
IV. EXPERIMENTS
In this section, we evaluate TrajGenAgent for human mobility trajectory generation on two large-scale synthetic datasets

We compare it against two prevailing paradigms: (i) trajectoryevel fine-tuned LLM generators, represented by Geo-Llama
[12], and (ii) state-of-the-art non-LLM neural generators (see
Section IV-B). This setup tests whether a zero-shot, workflowmanaged agent can match or surpass both fine-tuning-based
LLM generators and state-of-the-art non-LLM continuousime neural baselines in spatiotemporal fidelity and semantic
coherence, while avoiding costly parameter updates.
Beyond conventional aggregate spatiotemporal statistics, we
ntroduce an anomaly detection-based evaluation framework to
probe semantic coherence and behavioral plausibility. Specifcally, we incorporate two complementary anomaly detectors,
ICAD [22] and BeSTAD [23], which capture different abnormal patterns and provide diagnostic signals that aggregationevel metrics can miss. Overall, our experiments ask whether
TrajGenAgent (1) preserves basic spatiotemporal statistics
fidelity, (2) improves semantic and behavioral plausibility
under anomaly-based scrutiny, and (3) achieves these gains
with lower computational overhead by avoiding fine-tuning.
Our code can be accessed at: https://github.com/
Emory-AIMS/TrajGenAgent.
Statistic NumoSim MobilitySyn
Total daily trajectories used 34,000 34,000
Avg. stay points per trajectory 7.2 8.7
# Individuals 1,200 1,200
# Activity types 16 6
TABLE I: Training Dataset Statistics
A. Datasets & Preprocessing
We conduct experiments on two synthetic mobility datasets:
he open-source benchmark NumoSim and our simulated
MobilitySyn dataset.
• NumoSim. NumoSim [49] is a large-scale synthetic
mobility benchmark for anomaly detection, providing 8
weeks of stay-point trajectories for 200,000 individuals
in Los Angeles.
• MobilitySyn. We create MobilitySyn by following the
simulation framework in [50] to generate a realistic
week-long mobility trace for 5,000 individuals over a
metropolitan area. The simulator produces second-bysecond GPS records, which we convert into visit-wise
(stay-point) trajectories for evaluation.
Trajectory Representations. Our baselines cover two trajecory representations: (i) fixed-interval sequences with 96 steps
per day (15-minute bins), and (ii) visit-wise sequences with
variable length. TrajGenAgent, Geo-Llama [12], and GeoCETRA [51] (see details in Section IV-B) operate on visit-wise
rajectories. Geo-Llama represents each visit by a POI ID and
a discretized timestamp, whereas TrajGenAgent uses POI IDs
with continuous timestamps and an intermediate activity type.
Geo-CETRA generates continuous locations and times; for fair
comparison, we discretize its outputs to the same evaluation
grid/time bins. Specifically, we use 15-minute intervals and
grid sizes of 0.5 km for NumoSim and 0.7 km for MobilitySyn.

B. Baselines
We evaluate the performance of our model against the
following six state-of-the-art baselines:
• GRU [52] and LSTM [53]: Recurrent neural networks
that are efficient for sequential data generation. These
models are able to predict the next location based on
historically visited locations.
• Transformer [54]: A powerful deep learning mode
used in various natural language processing (NLP) and
computer vision tasks that leverages self-attention mechanisms. A multi-layer Transformer decoder is utilized for
trajectory generation.
• SeqGAN [29]: A sequence GAN that introduces a discriminator as a reward signal to guide the gradient policy
update of the generator, which performs the next location
prediction task based on the past states.
• Geo-CETRA [51]: A spatiotemporal point process-based
framework for trajectory generation that incorporates
constraint factorization and beam decoding to produce
realistic trajectories.
• Geo-Llama [12]: An LLM-based generator that encodes
daily trajectories as structured visit sequences and learns
spatiotemporal dependencies via parameter-efficient finetuning (e.g., LoRA). It applies visit-wise permutation to
encourage learning temporal regularities from visit-leve
time attributes rather than sequence order.
C. Evaluation Metrics
Our primary intended use case is providing synthetic trajectory data for counterfactual analysis of urban mobility
patterns, rather than optimizing a specific downstream task
such as next-POI recommendation. We therefore evaluate
generated trajectories from two complementary perspectives
(1) spatiotemporal statistics fidelity under aggregated mobility
statistics, and (2) behavioral semantics under downstream
anomaly detection models.
1) Aggregation-level Spatiotemporal Statistics Metrics:
Following prior mobility-generation evaluations [6], [8], we
compare generated and real trajectories through populationand trajectory-level mobility distributions.
Distance is the distribution of cumulative travel distance
per user per day. G-radius (radius of gyration) measures the
distribution of daily spatial movement range. Duration is the
distribution of dwell time per visited location. DailyLoc is the
distribution of the number of visited locations per user per day
G-rank is the global visit-frequency distribution over top-100
visited locations. I-rank is the per-user counterpart of G-rank
For these distributional properties, we compute Jensen–
(cid:16) (cid:17)
Shannon divergence (JSD): JSD (D, D′) = h D+D′ −
2
h(D)+h(D′) where D and D′ denote real and generated dis2
tributions, and h(·) is Shannon entropy. Lower JSD indicates
better agreement with real mobility statistics.
We additionally compare transition dynamics
Transition is the location-to-location transition
probability matrix over discretized locations G

Its discrepancy is measured by Frobenius norm:
(cid:113)
∥PD − PD′ ∥
F
= (cid:80)|
l
G
1=
|
1
(cid:80)|
l
G
2=
|
1
|PD(l
1
, l
2
) − PD′ (l
1
, l
2
)|2.
Lower values indicate better preservation of transition
structure. We note that G-rank and Transition correspond
o global-level while others correspond to trajectory-level
patterns.
2) Anomaly-Detection Evaluation: Aggregate spatiotemporal fidelity can be achieved even when trajectories are
behaviorally implausible at the visit or individual level. To
assess behavioral realism beyond population-level metrics,
we evaluate generated trajectories with two complementary
anomaly detectors: ICAD and BeSTAD. Since human mobilty realism is inherently multi-faceted and partly subjective, we
use these detectors as behavior-aware diagnostic proxies rather
han exhaustive measures of semantic coherence. Intuitively,
rajectories that are both statistically realistic and semantically
coherent in individual behavior should be harder for these
detectors to distinguish from trajectories in the training set.
a) ICAD (visit-level multi-context detector): ICAD is
a self-supervised autoregressive framework that decomposes
each visit into location, arrival time, and departure time,
and learns next-visit regularities under normal mobility paterns [22]. For anomaly scoring, it uses top-k deviation for
discrete spatial prediction and a mode-margin density score
(GMM-based) for continuous temporal components, then fuses
component-wise deviations into a final anomaly score. A key
property is interpretability: ICAD can attribute abnormality to
spatial, temporal, or compound deviations. This makes ICAD
suitable for testing whether generated visits preserve finegrained spatiotemporal consistency.
b) BeSTAD (individual-level behavioral shift detector):
BeSTAD targets individual-level anomalies by modeling individualized behavior clusters in a past “normal” period
and comparing cluster alignment in a future period [23].
It integrates temporal behavior signals with multi-scale spaial semantics (including point/line/polygon context, e.g.,
from OpenStreetMap (OSM), via the Hexagonal Hierarchical
Geospatial Indexing System (H3)-based indexing) to capture
richer behavioral context. Its anomaly score emphasizes crossperiod behavioral shifts and emerging routine changes rather
han isolated single-visit outliers. Therefore, BeSTAD complements ICAD by stressing high-level behavioral coherence at
ndividual level.
c) Metrics: We report anomaly-detection outputs, AUROC and average precision (AP), by applying detectors with
dentical settings to distinguish real trajectories (normal) from
generated ones (treated as anomalies). Unless otherwise specfied, we use a balanced split with equal positive and negative
samples, for which random guessing yields AUROC ≈ 0.5
and AP ≈ 0.5. This conservative setting avoids inflated
performance due to class imbalance. From a generationquality perspective, scores closer to chance indicate lower
separability—i.e., the generated data is harder to distinguish
from real mobility data under the detector—and therefore
exhibit higher behavioral semantic fidelity.

Tra
Dataset Model
Distance G-radius
GRU 0.0111 0.2557
LSTM 0.0146 0.3113
Transformer 0.0082 0.2945
NumoSim SeqGAN 0.0085 0.0998
Geo-CETRA 0.0093 0.3337
Geo-Llama 0.0075 0.2361
TrajGenAgent 0.0006 0.0993
GRU 0.0116 0.1859
LSTM 0.0131 0.2823
Transformer 0.0085 0.3760
MobilitySyn SeqGAN 0.0089 0.0738
Geo-CETRA 0.0276 0.5784
Geo-Llama 0.0268 0.5528
TrajGenAgent 0.0000 0.0051
TABLE II: Aggregation-level spatiotempora
D. Implementation Details
• GRU, LSTM, and Transformer are trained for 200
epochs using the Adam optimizer with a learning rate
of 0.001. Models share an embedding size of 256, with
GRU and LSTM using 6 layers of 512 hidden units, while
Transformer adopts a decoder-only architecture with 4
layers and 4 attention heads.
• SeqGAN includes an LSTM-based generator trained with
16-dimensional embeddings and 16 hidden units. Discriminator employs diverse filter sizes and counts, and
rollout number of 8. The entire pipeline carries 40 epochs
of pre-training and 20 epochs of adversarial training.
• Geo-CETRA employs a conditional Gaussian Mixture
Model with 8 spatial and temporal mixture components
and a beam search strategy with a beam size 10 and top
k=3. Optimization is performed with the Adam optimizer
a learning rate of 0.01, a scheduler with a decay factor
of 0.99, and z-score normalization for input data.
• Geo-Llama fine-tunes the Llama-2-7b-chat-hf
model using LoRA with a batch size of 48, a learning rate
of 0.00001, LoRA alpha32, LoRA dropout 0.02, LoRA r
16, and 20 epochs. Sampling uses temperature 1.2.
• TrajGenAgent performs zero-shot generation withou
model fine-tuning, using Qwen2.5-32B-Instruct as
the backbone LLM. Both workflow stages are served with
vLLM for high-throughput inference (temperature 0.90
top-p 0.95, max tokens 1024, max context length 8192)
E. Aggregation-level Spatiotemporal Statistics
Table II reports the trajectory generation performance under
aggregation-level spatiotemporal statistical metrics. Overall
TrajGenAgent achieves the strongest spatial alignment across
both datasets: it consistently attains the lowest divergence
on distance-based metrics (Distance, G-radius) and improves
global transition realism (Transition), highlighting the benefit of inference-time spatiotemporal grounding with peeraugmented individualized evidence and distance-/kinematicsaware priors. On MobilitySyn, TrajGenAgent is near-perfec
on most location- and transition-related metrics (Distance, Gradius, DailyLoc, I-rank/G-rank, and Transition), indicating

ory-level (↓) Global-level (↓)
uration DailyLoc I-rank G-rank Transition
0.2145 0.1561 0.0137 0.0159 0.0156
0.3013 0.1981 0.0893 0.0134 0.0150
0.2150 0.1620 0.0079 0.0112 0.0118
0.2410 0.1585 0.0082 0.0107 0.0120
0.0060 0.1128 0.0002 0.0002 0.0088
0.0028 0.0128 0.0001 0.0001 0.0087
0.0155 0.2117 0.0002 0.0002 0.0075
0.1747 0.3368 0.0082 0.0097 0.0132
0.1680 0.3046 0.0044 0.0078 0.0135
0.1510 0.2810 0.0047 0.0065 0.0115
0.1344 0.2437 0.0035 0.0062 0.0108
0.0319 0.1573 0.0006 0.0006 0.0083
0.0241 0.1209 0.0005 0.0005 0.0078
0.1308 0.0000 0.0003 0.0003 0.0000
atistical metrics of the trajectory generation.
hat the workflow can robustly reconstruct visit-wise spatial
statistics and movement structure without parameter updates.
On NumoSim, TrajGenAgent remains highly competitive on
spatial and transition metrics, while Geo-Llama is stronger
on time-centric statistics (notably Duration and DailyLoc).
This gap likely arises because duration grounding is sensiive to accumulated state errors and conflicts between the
sampled activity scaffold, remaining time budget, and sparse
ndividual temporal evidence. We attribute this to the increased behavioral complexity of NumoSim (more activity
ypes and richer daily schedules), where fine-tuning on strucured visit tokens can more precisely fit dwell-time and visitcount distributions; in contrast, our budget-aware duration
module prioritizes schedule feasibility and semantic plausibility; since it is not directly optimized to match aggregate
duration distributions, it can be less calibrated on micro-level
duration statistics on more behaviorally complex datasets. A
key factor across baselines is trajectory representation. The
fixed-interval generators (GRU/LSTM/Transformer/SeqGAN)
operate on 96-step sequences per day with implicit time
encoded through discretized bins, which produces long sequences with repeated states (stay points) and can obscure finegrained temporal patterns. In contrast, visit-wise generators
(Geo-CETRA, Geo-Llama, and TrajGenAgent) model daily
rajectories as variable-length visit sequences, which better
matches the underlying event structure and generally improves
ransition- and rank-related statistics. Among the fixed-interval
baselines, GRU/LSTM/Transformer capture some locationfrequency patterns reasonably well, whereas adversarial trainng (SeqGAN) is more sensitive to optimization instability and
can degrade fidelity on both spatial and temporal metrics.
F. Anomaly-Detection Evaluation
Table III reports anomaly-detection results under a balanced generated-vs-real split, where AUROC/AP closer to 0.5
ndicates lower separability and thus better semantic coherence. Since ICAD is prediction-based, it naturally supports
evaluation at both the visit-level and the individual-level,
whereas BeSTAD is designed for individual-level behavioral
shift detection and is therefore reported at the individual-level
only. Because anomaly detectors operate on POIs and activity

types, we focus on the three strongest visit-wise trajectory
generators without location grids, which means they can be
directly mapped to POI/GPS coordinates without introducing
coarse grid inversion artifacts: Geo-CETRA, Geo-Llama, and
TrajGenAgent.
On NumoSim, which has richer underlying spatiotempora
dynamics and a stronger activity type diversity, TrajGenAgen
consistently yields AUROC/AP values closest to 0.5 across
both detectors, indicating that its generated trajectories are the
hardest to distinguish from real ones. Geo-Llama is generally
stronger than Geo-CETRA, but both remain substantially more
separable than TrajGenAgent under ICAD’s fine-grained spatiotemporal scrutiny and BeSTAD’s individual-level behaviora
shift detection. These results align with our design goal
inference-time spatiotemporal grounding with individualized
evidence and kinematics-aware priors can preserve semantic
plausibility while avoiding systematic artifacts detectable by
anomaly models.
On MobilitySyn, which has simpler underlying mobility
patterns and fewer activity types, results are more mixed. GeoLlama is closest to chance under BeSTAD, while Geo-CETRA
attains the best (closest-to-0.5) ICAD visit-level scores; TrajGenAgent remains competitive and achieves the stronges
ICAD individual-level AP, suggesting improved individuallevel behavioral stability under ICAD. We conjecture tha
on simpler simulation dynamics, direct fine-tuning on structured tokens (Geo-Llama) or end-to-end neural approach with
rule-based decomposition of visit-wise movement constraints
as priors (Geo-CETRA) can already obscure many detector
cues, while the strength of TrajGenAgent in evidence-driven
semantic planning and kinematics-aware grounding are more
pronounced on richer, behaviorally more diverse datasets.
BeSTAD ICAD (Visit-level) ICAD (Individual-lev
Dataset Model (→ 0.5) (→ 0.5) (→ 0.5)
AUROC AP AUROC AP AUROC
Geo-CETRA 0.5767 0.7234 0.6414 0.7806 0.8821
NumoSim Geo-Llama 0.3375 0.7046 0.6057 0.7888 0.8962
TrajGenAgent 0.5008 0.5255 0.5368 0.5690 0.6398
Geo-CETRA 0.8192 0.4668 0.5435 0.7934 0.7314
MobilitySyn Geo-Llama 0.5025 0.5885 0.5969 0.7283 0.6629
TrajGenAgent 0.6817 0.6318 0.6761 0.6342 0.7194
TABLE III: Trajectory generation performance under
BeSTAD and ICAD anomaly detection. With balanced spli
(pos/neg=0.5), AP and AUROC closer to 0.5 is better.
G. Computational Efficiency
Table IV summarizes the end-to-end computational cos
under a unified setting, with all timings measured on a single
NVIDIA H100 GPU with maximized memory utilization
For parameter-updated baselines, the reported cost includes
training plus inference; for TrajGenAgent, which performs
zero-shot generation without parameter updates, it includes
only inference-time generation. In both cases, the workload
uses the same scale: 34,000 historical daily trajectories from
1,200 individuals are used as the training set or historica
evidence, and each method generates 34,000 daily trajectories
Overall, TrajGenAgent offers a strong cost–quality tradeoff: it matches or slightly exceeds Geo-Llama in generation

quality while avoiding costly parameter updates by injectng fine-grained spatiotemporal evidence at inference time
hrough a deterministic, verifier-guarded workflow. Such transferability is particularly valuable for transfer to new cities
or mobility regimes, where patterns shift and repeated fineuning is impractical under limited budgets. Among advanced
baselines, Geo-CETRA is relatively efficient by combining
rule-based decomposition of visit-wise movement constraints
with an efficient Transformer backbone, yielding moderate
GPU hours with competitive quality. In contrast, Geo-Llama
attains strong spatiotemporal fidelity via fine-tuning-driven sequence modeling over structured tokens, incurring the highest
compute among the strong baselines. SeqGAN is the least
cost-effective: adversarial training and Monte-Carlo rolloutbased reward feedback dominate runtime, leading to very
high GPU hours despite a lightweight generator and weaker
performance. For naive baselines, GRU/LSTM are the most
compute-efficient but deliver weaker fidelity, while the vanilla
Transformer improves fidelity at a higher training cost, reflectng the standard capacity–efficiency trade-off. Taken together,
hese results highlight that TrajGenAgent achieves comparable
or better quality than fine-tuned LLMs with substantially lower
end-to-end compute, narrowing the apparent gap between low
compute cost and high generation fidelity.
Model GRU TrajGenAgent LSTM Transformer
GPU Hours (↓) 1.25 1.67 1.83 3.17
Model Geo-CETRA SeqGAN Geo-Llama
GPU Hours (↓) 3.38 20.62 24.77
TABLE IV: Average computational cost per dataset on a
single NVIDIA H100 GPU, including generating 34,000 daily
rajectories and training with the same number if required.
H. Tool-Invocation Stability: Deterministic Workflow vs. Freeorm Tool Calling
We further evaluate tool-invocation stability with a simplified spatiotemporal grounding setting to justify our use of
deterministic workflow execution instead of zero-shot freeform tool calling. Specifically, we fix the activity chains
and evaluate only Stage-2 spatiotemporal grounding, where
each daily trajectory contains seven activities. This grounding
process is sequentially dependent: the POI selected for the
current visit affects travel-time estimation, the resulting end
ime determines the next visit’s start time, and both variables
condition subsequent POI and time decisions. Therefore, a
single missing or malformed tool call can break downstream
state variables and cause cascading failures. Both variants
use the same Qwen2.5-32B-Instruct backbone and a
simplified two-tool interface, location and time, which
gives the free-form variant a favorable setting by minimizing
ool-selection complexity. The free-form variant receives the
activity chain, tool schemas, and a semantic instruction to
convert the chain into a complete trajectory, and the LLM
autonomously decides when and how to invoke tools. In
contrast, our workflow-managed variant executes the same
grounding task under a fixed state-machine order. Although

Tool-calling strategy Traj.-level success ↑ Visit-level success ↑
Free-form tool calling 9.8% 59.3%
Deterministic workflow 100.0% 100.0%
TABLE V: Tool-invocation stability comparison between freeform tool calling and deterministic workflow execution under
fallback-enabled setting.
tool-call fine-tuning with scenario–tool–JSON traces can improve autonomous invocation, it introduces additional data and
training costs and may require a smaller backbone under the
same hardware budget. We therefore compare against zeroshot free-form tool calling using the same backbone withou
fine-tuning.
To avoid early termination after a failed call, the tools include default-value fallbacks that allow the grounding process
to continue. These fallbacks only keep later visits executable
but may still introduce inaccurate state variables that propagate
through subsequent grounding steps. Table V therefore reports invocation success under this fallback-enabled execution
setting. Trajectory-level success requires that all visits in
a daily trajectory complete the required location and time
calls without fallback-induced substitution. Visit-level success
measures the fraction of visits in which the required calls
are completed. Even under this simplified setting, zero-sho
free-form tool calling falls short of a practically usable leve
of tool-invocation stability for sequential grounding, whereas
deterministic workflow achieves perfect invocation with explicitly predefined control flow and state dependencies.
NumoSim MobilitySyn
Metric (↓)
TrajGenAgent w/o kin. TrajGenAgent w/o kin.
Distance 0.0006 0.0028 0.0000 0.0000
G-radius 0.0993 0.1508 0.0051 0.0004
Duration 0.0155 0.0198 0.1308 0.3732
DailyLoc 0.2117 0.2476 0.0000 0.0000
I-rank 0.0002 0.0006 0.0003 0.0001
G-rank 0.0002 0.0006 0.0003 0.0001
Transition 0.0075 0.0077 0.0000 0.0000
TABLE VI: Ablation study of TrajGenAgent on kinematics
design with aggregation-level spatiotemporal statistical metrics.
NumoSim MobilitySyn
Metric
TrajGenAgent w/o kin. TrajGenAgent w/o kin.
BeSTAD
AUROC (→ 0.5) 0.5008 0.5104 0.6817 0.7400
ICAD (Visit-level)
AP (→ 0.5) 0.5255 0.6692 0.6318 0.7143
AUROC (→ 0.5) 0.5368 0.6483 0.6761 0.6827
ICAD (Agent-level)
AP (→ 0.5) 0.5690 0.9034 0.6342 0.9922
AUROC (→ 0.5) 0.6398 0.9143 0.7194 0.9925
TABLE VII: The Kinematics Ablation study of TrajGenAgen
under BeSTAD and ICAD anomaly detection.
I. Ablation Study: Kinematics-aware Grounding
Tables VI and VII show that the kinematics-aware module is a key contributor to TrajGenAgent: removing it degrades mobility pattern fidelity especially under the scrutiny

T = 0.5 T = 0.9 T = 1.5
Total↓ Schema↓ Constr.↓ Total↓ Schema↓ Constr.↓ Total↓ Schema↓ Constr.↓
Avg. FR(%) 14.3% 1.8% 12.5% 9.1% 3.6% 5.5% 28.3% 15.2% 13.1%
TABLE VIII: LLM verifier-triggered failure rates (FR) under
different sampling temperatures T (averaged across datasets).
of ICAD/BeSTAD. This confirms that physics-/kinematicsnformed travel-time propagation helps maintain coherent temporal progression and behavior-level plausibility beyond what
aggregate metrics alone reveal. More broadly, the ablation
highlights a core advantage of our workflow-managed agent
design: specialized constraints and domain modules can be
plugged in or removed flexibly, which is challenging for endo-end approaches.
J. Parameter Study: LLM Sampling Temperature Impacts
Table VIII reports verifier-triggered failure rates under three
sampling temperatures (averaged across datasets). We mark a
daily run as failed if either Stage 1 (activity chain) or Stage 2
(duration) LLM output violates the required schema or basic
feasibility constraints (e.g., chain length/duration bounds).
Schema failures increase monotonically with temperature,
as higher T flattens the token distribution and destabilizes
structured outputs. Constraint failures are non-monotonic: very
ow T is mode-seeking and can repeat typical but infeasible
values under budget/bound checks, while very high T induces
out-of-bound or implausible samples; T = 0.9 provides the
best balance and the lowest overall failure rate.
V. CONCLUSION
We presented TrajGenAgent, a zero-shot, semantic-aware
hierarchical LLM-agent framework for human mobility trajecory generation. It couples an orchestrator LLM for individualand weekday-conditioned activity chain planning with a deerministic, verifier-guarded worker workflow for kinematicsaware spatiotemporal grounding via inference-time tool inegration (without fine-tuning or parameter updates). Across
both large-scale simulation datasets, TrajGenAgent consisently outperforms baselines under complementary evaluations, including traditional spatiotemporal statistical metrics and our anomaly-detection-based semantic-aware metrics
(ICAD/BeSTAD).
Despite the promising results, several limitations suggest
directions for future work. Our temporal grounding relies
on retrieval-driven priors and bounded constraints; even augmented with LLMs, achieving highly accurate, individualspecific temporal modeling remains challenging and motivates
stronger constraint-aware neural temporal modules. In addiion, our verifiers mainly enforce structural validity and feasibility, offering limited semantic-quality feedback for iterative
refinement; incorporating evaluator-in-the-loop signals could
better guide the refinement of activity chains and temporal
schedules. We hope these directions will further strengthen
workflow-based LLM agents for semantically coherent and
physically plausible human mobility trajectory generation at
scale.

ACKNOWLEDGMENTS produce and distribute reprints for Governmental purposes,
notwithstanding any copyright annotation thereon. Disclaimer:
Research supported by the Intelligence Advanced ReThe views and conclusions contained herein are those of the
search Projects Activity (IARPA) via the Department of Inauthors and should not be interpreted as necessarily representterior/Interior Business Center (DOI/IBC) contract number
ing the official policies or endorsements, either expressed or
140D0423C0033. The U.S. Government is authorized to reimplied, of IARPA or the U.S. Government.

REFERENCES
[1] T. Hu, S. Wang, B. She, M. Zhang, X. Huang, Y. Cui, J. Khuri, Y. Hu
X. Fu, X. Wang et al., “Human mobility data in the covid-19 pandemic
characteristics, applications, and challenges,” International Journal o
Digital Earth, vol. 14, no. 9, pp. 1126–1147, 2021.
[2] R. A. Becker, R. Caceres, K. Hanson, J. M. Loh, S. Urbanek, A. Var
shavsky, and C. Volinsky, “A tale of one city: Using cellular network
data for urban planning,” IEEE Pervasive Computing, vol. 10, no. 4, pp
18–26, 2011.
[3] Y. Chen, C. Hu, and J. Wang, “Human-centered trajectory tracking
control for autonomous vehicles with driver cut-in behavior prediction,”
IEEE Transactions on Vehicular Technology, vol. 68, no. 9, pp. 8461–
8471, 2019.
[4] M. e. a. Mokbel, “Mobility data science: Perspectives and challenges,”
ACM Trans. Spatial Algorithms Syst., vol. 10, no. 2, jul 2024. [Online]
Available: https://doi.org/10.1145/3652158
[5] D.-T. Le, G. Cernicchiaro, C. Zegras, and J. Ferreira
“Constructing a synthetic population of establishments for the
simmobility microsimulation platform,” Transportation Research
Procedia, vol. 19, pp. 81–93, 2016, transforming Urban
Mobility. mobil.TUM 2016. International Scientific Conference on
Mobility and Transport. Conference Proceedings. [Online]. Available
https://www.sciencedirect.com/science/article/pii/S2352146516308560
[6] J. Feng, Z. Yang, F. Xu, H. Yu, M. Wang, and Y. Li, “Learning to
simulate human mobility,” in Proceedings of the 26th ACM SIGKDD
international conference on knowledge discovery & data mining, 2020
pp. 3426–3433.
[7] H. Lin, S. Shaham, Y.-Y. Chiang, and C. Shahabi, “Generating realistic
and representative trajectories with mobility behavior clustering,” in
Proceedings of the 31st ACM International Conference on Advance
in Geographic Information Systems, 2023, pp. 1–4.
[8] M. Zhang, H. Lin, S. Takagi, Y. Cao, C. Shahabi, and L. Xiong, “Cs
gan: Modality-aware trajectory generation via clustering-based sequence
gan,” in 2023 24th IEEE International Conference on Mobile Data
Management (MDM). IEEE, 2023, pp. 148–157.
[9] K. Ouyang, R. Shokri, D. S. Rosenblum, and W. Yang, “A non
parametric generative model for human trajectories.” in IJCAI, vol. 18
2018, pp. 3812–3817.
[10] Q. Long, H. Wang, T. Li, L. Huang, K. Wang, Q. Wu, G. Li, Y. Liang
L. Yu, and Y. Li, “Practical synthetic human trajectories generation
based on variational point processes,” in Proceedings of the 29th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining, 2023
pp. 4561–4571.
[11] W. X. Zhao, K. Zhang, J. Xie, J. Liu, Z. Li, Y. Shan, G. Yang, S. He
Z. Wang, Z. Liu et al., “A survey of large language models,” arXiv
preprint arXiv:2303.18223, 2023.
[12] S. Li, T. Tran, H. Lin, J. Krumm, C. Shahabi, L. Zhao, K. Shafique, and
L. Xiong, “Geo-llama: Leveraging llms for human mobility trajectory
generation with constraints,” in 2025 26th IEEE International Confer
ence on Mobile Data Management (MDM). IEEE, 2025, pp. 20–31.
[13] P. Bhandari, A. Anastasopoulos, and D. Pfoser, “Urban mobility as
sessment using llms,” in Proceedings of the 32nd ACM Internationa
Conference on Advances in Geographic Information Systems, 2024, pp
67–79.
[14] Y. Zhang, Y. Hu, and D. Wang, “A study on individual spatiotempora
activity generation method using mcp-enhanced chain-of-thought large
language models,” arXiv preprint arXiv:2506.10853, 2025.
[15] W. JIAWEI, R. Jiang, C. Yang, Z. Wu, R. Shibasaki, N. Koshizuka
C. Xiao et al., “Large language models as urban residents: An llm
agent framework for personal mobility generation,” Advances in Neura
Information Processing Systems, vol. 37, pp. 124 547–124 574, 2024.
[16] S. Li, T. Tran, L. Zhao, K. Shafique, and L. Xiong, “Towards foun
dation model-based generation of human mobility trajectories,” in The
inaugural ACM SIGSPATIAL International Workshop on Urban Mobility
Foundation, 2025, p. 22.
[17] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, L. Wang, and W. Chen
“Lora: Low-rank adaptation of large language models,” in Internationa
Conference on Learning Representations (ICLR), 2022.
[18] S. Yao, J. Yu, J. Zhao, K. Narasimhan, O. Etzioni, and Y. Choi, “React
Synergizing reasoning and acting in language models,” arXiv preprin
arXiv:2210.03629, 2022.
[19] T. Schick, J. Dwivedi-Yu, R. Dess`ı, R. Raileanu, M. Lomeli, L. Zettle
moyer, N. Cancedda, and T. Scialom, “Toolformer: Language model

can teach themselves to use tools,” in Advances in Neural Information
Processing Systems, 2023.
20] J. Zhang, T. Lan, M. Zhu, Z. Liu, and C. Xiong, “xLAM: A family
of large action models to empower ai agent systems,” 2024, https://
huggingface.co/Salesforce/Llama-xLAM-2-8b-fc-r.
21] J. Wang and Z. Duan, “Agent ai with langgraph: A modular framework
for enhancing machine translation using large language models,” 2024,
arXiv preprint; LangGraph framework for modular agent orchestration.
22] B. Azarijoo, M. D. Siampou, J. Krumm, and C. Shahabi, “Icad: A selfsupervised autoregressive approach for multi-context anomaly detection
in human mobility data,” in Proceedings of the 33rd ACM International
Conference on Advances in Geographic Information Systems, 2025, pp.
595–606.
23] J. Xie, J. Kim, Y.-Y. Chiang, L. Zhao, and K. Shafique, “Bestad:
Behavior-aware spatio-temporal anomaly detection for human mobility
data,” in Proceedings of the 2nd ACM SIGSPATIAL International
Workshop on Geospatial Anomaly Detection, 2025, pp. 56–59.
24] N. Pelekis, C. Ntrigkogias, P. Tampakis, S. Sideridis, and Y. Theodoridis,
“Hermoupolis: a trajectory generator for simulating generalized mobility
patterns,” in Machine Learning and Knowledge Discovery in Databases:
European Conference, ECML PKDD 2013, Prague, Czech Republic,
September 23-27, 2013, Proceedings, Part III 13. Springer, 2013, pp.
659–662.
25] S. Jiang, Y. Yang, S. Gupta, D. Veneziano, S. Athavale, and M. C.
Gonza´lez, “The timegeo modeling framework for urban mobility without
travel surveys,” Proceedings of the National Academy of Sciences, vol.
113, no. 37, pp. E5370–E5378, 2016.
26] Q. Liu, S. Wu, L. Wang, and T. Tan, “Predicting the next location: A
recurrent model with spatial and temporal contexts,” in Proceedings of
the AAAI conference on artificial intelligence, vol. 30, no. 1, 2016.
27] J. Feng, Y. Li, C. Zhang, F. Sun, F. Meng, A. Guo, and D. Jin, “Deepmove: Predicting human mobility with attentional recurrent networks,”
in Proceedings of the 2018 world wide web conference, 2018, pp. 1459–
1468.
28] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial networks,”
Communications of the ACM, vol. 63, no. 11, pp. 139–144, 2020.
29] L. Yu, W. Zhang, J. Wang, and Y. Yu, “Seqgan: Sequence generative
adversarial nets with policy gradient,” in Proceedings of the AAAI
conference on artificial intelligence, vol. 31, no. 1, 2017.
30] Z. Zhou, X. Yang, R. Rossi, H. Zhao, and R. Yu, “Neural point process
for learning spatiotemporal event dynamics,” in Learning for Dynamics
and Control Conference. PMLR, 2022, pp. 777–789.
31] J. Wang, R. Jiang, C. Yang, Z. Wu, M. Onizuka, R. Shibasaki,
N. Koshizuka, and C. Xiao, “Large language models as urban residents:
An llm agent framework for personal mobility generation,” arXiv
preprint arXiv:2402.14744, 2024.
32] J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, and
D. Zhou, “Chain of thought prompting elicits reasoning in large
language models,” in Advances in Neural Information Processing
Systems, 2022. [Online]. Available: https://arxiv.org/abs/2201.11903
33] O. S. Community, “Gpt-4-oss: Open-source 120b parameter llm,” https:
//huggingface.co/TheBloke/GPT4-OSS-120B, 2024, accessed August
2025.
34] M. P. Armstrong, G. Rushton, and D. L. Zimmerman, “Geographically
masking health data to preserve confidentiality,” Statistics in medicine,
vol. 18, no. 5, pp. 497–525, 1999.
35] P. A. Zandbergen, “Ensuring confidentiality of geocoded health data:
Assessing geographic masking strategies for individual-level data,” Advances in medicine, vol. 2014, no. 1, p. 567049, 2014.
36] X. Wang, X. Liu, Z. Lu, and H. Yang, “Large scale gps trajectory
generation using map based on two stage gan,” Journal of Data Science,
vol. 19, no. 1, pp. 126–141, 2021.
37] C. Cao and M. Li, “Generating mobility trajectories with retained
data utility,” in Proceedings of the 27th ACM SIGKDD Conference on
Knowledge Discovery & data Mining, 2021, pp. 2610–2620.
38] Y. Zhu, Y. Ye, S. Zhang, X. Zhao, and J. Yu, “Difftraj: Generating
gps trajectory with diffusion probabilistic model,” Advances in Neural
Information Processing Systems, vol. 36, pp. 65 168–65 188, 2023.
39] C. Cheng, H. Yang, M. R. Lyu, and I. King, “Where you like to
go next: Successive point-of-interest recommendation,” in Twenty-Third
international joint conference on Artificial Intelligence, 2013.
40] D. Kong and F. Wu, “Hst-lstm: A hierarchical spatial-temporal longshort term memory network for location prediction.” in Ijcai, vol. 18,
no. 7, 2018, pp. 2341–2347.

[41] K. Sun, T. Qian, T. Chen, Y. Liang, Q. V. H. Nguyen, and H. Yin, “Where
to go next: Modeling long-and short-term user preferences for point-of
interest recommendation,” in Proceedings of the AAAI conference on
artificial intelligence, vol. 34, no. 01, 2020, pp. 214–221.
[42] Y. Luo, Q. Liu, and Z. Liu, “Stan: Spatio-temporal attention network fo
next location recommendation,” in Proceedings of the web conference
2021, 2021, pp. 2177–2185.
[43] L. Zhang, Z. Sun, Z. Wu, J. Zhang, Y. S. Ong, and X. Qu, “Next point
of-interest recommendation with inferring multi-step future preferences.”
in IJCAI, 2022, pp. 3751–3757.
[44] N. Lim, B. Hooi, S.-K. Ng, X. Wang, Y. L. Goh, R. Weng, and
J. Varadarajan, “Stp-udgat: Spatial-temporal-preference user dimensiona
graph attention network for next poi recommendation,” in Proceeding
of the 29th ACM International conference on information & knowledge
management, 2020, pp. 845–854.
[45] S. Yang, J. Liu, and K. Zhao, “Getnext: trajectory flow map enhanced
transformer for next poi recommendation,” in Proceedings of the 45th
International ACM SIGIR Conference on research and development in
information retrieval, 2022, pp. 1144–1153.
[46] P. Li, M. de Rijke, H. Xue, S. Ao, Y. Song, and F. D. Salim
“Large language models for next point-of-interest recommendation,”
in Proceedings of the 47th International ACM SIGIR Conference on
Research and Development in Information Retrieval, 2024, pp. 1463–
1472.
[47] A. Yang, A. Li, B. Yang, B. Zhang, B. Hui, B. Zheng, B. Yu, C. Gao
C. Huang, C. Lv et al., “Qwen3 technical report,” arXiv preprin
arXiv:2505.09388, 2025.

48] W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. Gonzalez,
H. Zhang, and I. Stoica, “Efficient memory management for large
language model serving with pagedattention,” in Proceedings of the 29th
symposium on operating systems principles, 2023, pp. 611–626.
49] C. Stanford, S. Adari, X. Liao, Y. He, Q. Jiang, C. Kuai, J. Ma,
E. Tung, Y. Qian, L. Zhao et al., “Numosim: A synthetic mobility dataset
with anomaly detection benchmarks,” in Proceedings of the 1st ACM
SIGSPATIAL International Workshop on Geospatial Anomaly Detection,
2024, pp. 68–78.
50] S. B. Yoginath, N. Ahmad, C. Gunaratne, L. Amichi, J.-S. Kim,
A. Burger, H. Xu, B. Bishnoi, S. C. Christopher, and G. M. Thakur,
“A scalable multi-modal framework for high-fidelity distributed human
mobility simulations,” in Proceedings of the 8th ACM SIGSPATIAL
International Workshop on Geospatial Simulation, 2025, pp. 1–11.
51] H. Lin, J. Krumm, C. Shahabi, and L. Xiong, “Controllable visit
trajectory generation with spatiotemporal constraints,” in Proceedings
of the 2024 IEEE International Conference on Data Mining (ICDM).
IEEE, 2024.
52] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, “Gradient-based learning
applied to document recognition,” Proceedings of the IEEE, vol. 86,
no. 11, pp. 2278–2324, 1998.
53] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
computation, vol. 9, no. 8, pp. 1735–1780, 1997.
54] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez,
Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in
Neural Information Processing Systems, vol. 30, 2017.
