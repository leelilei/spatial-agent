---
title: "GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies"
source_pdf: "07_large_scale_urban_sim\\01_GenWorld_Li2026.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-07-03T12:08:10+00:00
page_count: 27
status: ok
text_char_count: 87668
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\07_large_scale_urban_sim\01_GenWorld_Li2026.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-07-03T12:08:10+00:00
- Page count: 27
- Status: ok
- Text chars: 87668
- Quality flags: none

## Metadata

- Title: GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies
- Author: Gen Li; Jieyuan Lan; Pengcheng Xu; Zongyuan Wu; Masaki Ogura; Tao Feng
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

1 Introduction

## Outline

- Introduction (page 1)
  - Grounded and Scalable LLM-Agent Simulation (page 1)
  - Why Urban Grounding Matters (page 2)
  - Why Offline Compilation Matters (page 3)
  - Contributions (page 3)
  - Paper Organization (page 3)
- Related Work (page 3)
  - LLM Agents and Simulation Platforms (page 4)
  - Urban Simulation Platforms (page 4)
  - Synthetic Population Generation (page 5)
  - Knowledge Distillation for Agent Simulation (page 6)
- Agent Interface (page 6)
- Distillation and Scaling (page 8)
- Empirical Grounding of the Urban World (page 10)
  - Population and Environment Foundation (page 10)
    - Tract-Level Micro-Synthesis and Attribute Assignment (page 11)
    - Spatial Grounding of Home, School, and Work (page 11)
    - Derived Social Networks (page 12)
    - Urban Environment Integration (page 12)
  - Activity Generation and Temporal Grounding (page 12)
  - Population Distribution Validation (page 12)
    - Census Data Validation (page 12)
    - Spatial Distribution Validation (page 13)
    - School Assignment Validation (page 13)
  - Mobility Pattern Validation (page 13)
- Platform Architecture (page 14)
  - System Overview (page 14)
  - Simulation Engine (page 14)
- Evaluation Cases and Scalability (page 14)
  - Evaluation Cases (page 14)
    - Case 1: Full-City Weekday Baseline (page 15)
    - Case 2: Weekday–Weekend Behavioral Contrast (page 16)
    - Case 3: Warning-Response Perturbation (page 16)
    - Road-Flow Visualization (page 16)
    - Scalability Analysis (page 17)
  - Summary (page 18)
- Discussion (page 18)
- Conclusion (page 19)
- Supplementary Materials (page 22)
  - Additional Figures (page 22)
  - Data Sources (page 22)
  - Intention and Activity-Type Taxonomy (page 25)
  - Distillation Prompt Templates (page 26)
  - LLM Interface Schema (page 26)
  - Distillation Setup (page 27)

## Markdown Content

GenWorld: Empirically Grounded Urban Simulation Infrastructure
for Scalable LLM-Agent Studies
Gen Li1, Jieyuan Lan1,2, Pengcheng Xu3, Zongyuan Wu4, Masaki Ogura1, and Tao Feng∗1
1Graduate School of Advanced Science and Engineering, Hiroshima University,
Higashi-Hiroshima, Japan
2Jiangxi Polytechnic University, Jiangxi, China
3College of Urban Development and Modern Transportation, Xi’an University of
Architecture and Technology, Xi’an, China
4North China University of Water Resources and Electric Power, China
June 29, 2026
Abstract 1 Introduction
1.1 Grounded and Scalable LLMLLM-agent simulation faces a joint grounding and
Agent Simulation
scaling problem: agents should act in environments
that reflect real urban constraints, yet direct online
Large Language Models (LLMs) have motivated a
LLM calls for city-scale populations are computationnew generation of agent simulations in which agents
ally prohibitive. We present GenWorld, an empircan use language-like observations, reason over conically grounded urban simulation infrastructure that
text, and emit structured decisions [32, 39, 42, 15].
combines a building-level synthetic city, a structured
For urban research, this direction is attractive beagent–environment interface, and offline compilation
cause cities are spatially constrained, socially heteroof LLM-derived decision signals into lookup policies
geneous, and temporally dynamic. A useful urban
for scalable rollout. In a reference instantiation for
agent environment should therefore expose more than
Higashihiroshima, Japan, GenWorld grounds 196,608
a list of points of interest: it should ground agents in
synthetic residents in census and geospatial data, valrealistic homes, schools, workplaces, activity opporidates demographic consistency against census tabutunities, infrastructure, and demographic heterogenelations, and uses YJMob100K mobile-phone data as
ity.
a commuting-distance diagnostic. We demonstrate
At the same time, city-scale LLM-agent simulathe infrastructure through three reproducible cases:
tion faces a joint grounding–scaling problem. On the
a full-city weekday rollout, a weekday–weekend begrounding side, agents should operate under empirihavioral contrast, and a warning-response perturbacal urban constraints rather than in abstract text ention with auditable replanning traces. These cases
vironments or coarse POI lists. On the scaling side,
support GenWorld as a reproducible platform for
directly querying an LLM for every decision of evgrounded and scalable LLM-agent studies, while calery agent is impractical for hundreds of thousands
ibrated forecasting for traffic, evacuation, or policy
of residents and many decision points per day. For
outcomes remains future work.Project page: https:
example, 200,000 agents over a 24-hour day with 15-
//genworld1993.netlify.app/.
minute decision intervals would require 19.2 million
Keywords: LLM agents, Urban simulation infras- online LLM calls if every decision were delegated to
tructure, Synthetic population, Building-level assign- a teacher model. This scale mismatch motivates the
ment, Multi-agent systems, Policy compilation, Em- central question of this paper:
pirical validation
How can LLM-agent simulations be
grounded in real urban constraints
∗Corresponding author: taofeng@hiroshima-u.ac.jp and scaled to city-level populations
1
6202
nuJ
62
]AM.sc[
1v05672.6062:viXra

Figure 1: Multi-scale spatial granularity of GenWorld’s empirically grounded urban world in Higashihiroshima, Hiroshima, Japan. (A) City-level view showing 196,608 individuals distributed across georeferenced
buildings, validated against census data. (B) District-level view near Hiroshima University, revealing diverse building types (residential, commercial, educational) with topographic context and elevation data. (C)
Building-level view of a Youme Town supermarket area with 47 employees spatially assigned to a corresponding commercial land-use parcel; residential buildings are rendered in red with color intensity proportional to
resident counts (darker indicates more residents). (D) Individual-level details showing employee household
origins, occupations, commuting distances, and residential neighborhoods (cho/town). This fine-grained
spatial allocation supports environment-aware agent simulation, which is typically difficult to capture in
TAZ-based or POI-list approaches.
without online LLM calls for every 1.2 Why Urban Grounding Matters
agent decision?
Urban environments are demanding testbeds for
agent simulation. Physical distance and infrastructure topology shape feasible actions; schools, workWe answer this question with GenWorld, an em- places, and services create institutional constraints;
pirically grounded urban simulation infrastructure for households and neighborhoods create social and spascalable LLM-agent studies. The key design is a sys- tial context; and individual routines aggregate into
tem chain rather than a single isolated algorithm: a city-level patterns. These characteristics make urban
building-level synthetic urban world provides realis- simulation well suited for studying situated agent betic constraints; a structured agent–environment in- havior, but only if the environment itself is grounded
terface makes LLM-style decisions executable, vali- in realistic population and spatial structure.
datable, and traceable; and offline compilation shifts Recent LLM-agent environments often fall short on
LLM-derived decision signals out of the simulation this point. Abstract text-based benchmarks support
loop into lightweight lookup policies. controlled reasoning tasks but lack real spatial con2

straints [28]. POI-based urban simulations and large
scale agent platforms [32, 33, 38] have made progres
in agent cognition and interaction, but they often rely
on coarse spatial units, POI lists, or weakly validated
population foundations. For city-scale urban stud
ies, such abstractions make it difficult to represen
building-level exposure, home–work–school anchor
ing, commute-distance structure, and land-use fea
sibility.
GenWorld therefore treats synthetic population
and spatial assignment as a grounding layer. We
use established population synthesis and spatia
allocation techniques, including census-constrained
synthesis, building-level household placement, and
school/workplace assignment. The contribution i
not IPF in isolation. Rather, the contribution is in
tegrating these standard ingredients into an LLM
ready urban world that can be used by structured
agent policies and reproduced through documented
data-preparation stages.
1.3 Why Offline Compilation Matters
LLM-agent behavior also raises a scalability prob
lem. Online LLM inference can be useful for smal
numbers of agents or diagnostic traces, but city-scale
rollout requires a different execution model. Gen
World separates teacher inference from simulation
time execution. A teacher LLM is queried offline
under discretized context keys and finite candidate
sets; the resulting score distributions are compiled
into lookup policies; and simulation-time agents sam
ple from these compiled policies while using the same
validators and deterministic execution semantics.
This design trades open-ended online reasoning fo
tractable, auditable rollout. It should be understood
as compiled stochastic policy execution rather than
as fully adaptive online LLM reasoning. The benefi
is that every simulated action remains tied to a struc
tured interface, a finite candidate set, and a traceable
context key, enabling large-scale execution and post
hoc analysis.
1.4 Contributions
This paper presents GenWorld as a reproducible in
frastructure for grounded and scalable LLM-agen
simulation. The contributions are organized as a con
nected system:
1. Empirically grounded urban world for
LLM-agent simulation. We instantiate a
building-level urban world for Higashihiroshima
Japan, with 196,608 synthetic residents. Censu
tabulations provide demographic constraints and

validation targets, while geospatial sources provide buildings, land use, POIs, roads, elevation,
schools, and workplaces. We validate census
consistency and use anonymized YJMob100K
mobile-phone data [40] as a commuting-distance
diagnostic.
2. Structured agent interface and trace contract. We define a query-conditioned interface
in which raw city and persona states are mapped
into binned observations, actions are selected
from finite candidate sets, outputs are JSONvalidated, and execution traces are recorded in
machine-readable form. This contract makes
LLM-style decisions executable in a simulator
and suitable for later analysis or policy compilation.
3. Offline policy compilation for city-scale
rollout. We compile repeated teacher-model
responses under discretized context keys into
simulation-time lookup policies. This shifts expensive LLM calls out of the rollout loop and
enables city-scale execution through lightweight
sampling over validated action candidates.
4. Reproducible evaluation cases. We evaluate GenWorld through three cases: a full-city
weekday baseline, a weekday–weekend behavioral contrast, and a warning-response perturbation. These cases demonstrate city-scale rollout, controlled temporal-regime changes, and auditable replanning under an exogenous event.
They are infrastructure diagnostics rather than
calibrated forecasts of traffic, evacuation, or policy outcomes.
1.5 Paper Organization
Section 2 reviews related work in LLM-agent simuation, urban simulation platforms, synthetic populaion generation, and distillation for agent simulation.
Section 3 presents the structured agent interface and
race contract. Section 4 describes offline policy compilation for scalable rollout. Section 5 details the empirically grounded urban world construction and valdation. Section 6 presents the platform architecture
and simulation engine. Section 7 reports the evaluaion cases and scalability analysis. Sections 8 and 9
discuss limitations and conclude.
2 Related Work
Table 1 provides an overview of how GenWorld compares to existing platforms across three categories:

LLM agent simulation platforms, LLM-based urban
mobility platforms, and population synthesis plat
forms. We detail these comparisons in the following
subsections.
2.1 LLM Agents and Simulation Platforms
The emergence of Large Language Models has driven
rapid progress in autonomous agent systems. Recen
works demonstrate LLM agents across a range of set
tings, from social simulation [32] to tool use [34] and
multi-agent collaboration [15]. This progress moti
vates the need for realistic simulation environment
that can support LLM agent research under real
world constraints.
Existing Agent Platforms. Existing platform
and benchmarks span multiple levels of realism.
Abstract environments (e.g.
GridWorld/TextWorld-style tasks) [28] are use
ful for isolating reasoning and planning, but they
abstract away geography, resource constraints, and
social interactions.
Task-specific platforms such as SWE-bench [19
(software engineering) and WebArena [46] (web nav
igation) provide grounded objectives and measurable
success criteria, but they typically focus on single
agent, non-spatial settings.
Social simulation platforms such as Genera
tive Agents [32] explore emergent interactions, ye
the environments are simplified and the scale (e.g.
25 agents) is insufficient for studying city-scale phe
nomena and computational scalability. CityBench [8
evaluates LLM world-modeling capabilities for urban
tasks but does not provide building-level population
grounding.
LLM Agents in Transportation and Mobil
ity. Beyond interactive simulacra, LLMs have
been explored as simulated economic agents [17
and integrated into mobility and transportation set
tings. LLMob [38] uses self-consistency and retrieval
augmented strategies for individual mobility genera
tion with GPS-based validation. Liu et al. [27] outline
an LLM-agent-based transportation modeling frame
work with a small proof-of-concept. TrajLLM [20
combines LLM-based persona generation with hybrid
destination choice (LLM + physical models), but fo
cuses on POI-level trajectories. GATSim [26] and
MobileCity [43] target larger-scale mobility simula
tion; MobileCity achieves efficiency partly by dis
abling LLM modules at scale, trading behavioral fi
delity for speed. OpenCity [41] proposes a “group
and-distill” prompt optimization strategy that clus
ters agents with similar attributes and distills shared

easoning patterns, achieving 600× acceleration in
imulation time; however, it focuses on prompt-level
efficiency rather than building-level spatial groundng. Overall, these efforts primarily emphasize individual trajectory generation or engineering efficiency.
They often do not provide city-scale population synhesis with jointly validated demographics and spatial
assignments (e.g., building-level placement) or thorough empirical validation.
Existing platforms often do not jointly provide
ealistic population foundations supported by empirical data, spatial complexity with infrastructure
constraints, computational scalability to city-scale
100,000+ agents), and LLM-compatible interfaces.
GenWorld provides an empirically grounded urban
environment with 200,000-agent scalability based on
data from Higashihiroshima, Hiroshima, Japan.
2.2 Urban Simulation Platforms
Agent-based modeling has a rich history in urban and
ransportation research [6, 23], with several estabished platforms:
Traditional ABM Platforms. GAMA [35], MASON [29], and NetLogo [37] are widely used for
urban simulation. These platforms provide powerful
modeling capabilities but were designed for domain
experts rather than AI researchers, and they do not
provide standardized LLM integration interfaces or
natural language observation spaces.
Transportation Simulation Tools. MATSim [16],
SUMO [22], and similar tools focus on traffic simuation with detailed traffic modeling. However, they
ypically use simplified behavioral models and do not
ncorporate the cognitive realism enabled by LLMdriven agents.
Commercial Platforms. AnyLogic, Citilabs, and
other commercial tools offer sophisticated urban
modeling but are closed-source, expensive, and not
designed for AI research integration.
Recent open-source efforts such as VoxCity [9]
provide seamless 3D urban environment generation,
while Biljecki and Chow [3] establish global building
morphology indicators for standardized urban analysis. However, existing platforms were not designed
with LLM agents in mind. GenWorld aims to address these gaps by providing natural language observation spaces, flexible action specifications, validated
population foundations, and computational scalabilty through knowledge distillation.

Table 1: Comparison of Gen
Platform Population Empiric
Realism Validatio
LLM Agent Simulation Platforms
GridWorld/TextWorld Low No
Generative Agents [32] Low No
WebArena [46] N/A N/A
LLM-Based Urban Mobility Platforms
LLM-ABM Framework [27] Low No
LLMob [38] Medium GPS
TrajLLM [20] Medium Qualitati
MobAgent [24] Medium Survey
GATSim [26] Medium No
MobileCity [43] Medium No
OpenCity [41] Low GPS
Population Synthesis Platforms
Jiang et al. [18] High Census
Pseudo-PFLOW [21] High Census
GenWorld (Ours) High Multi-sou
† Social networks are generated from spatial co-location bu
2.3 Synthetic Population Generation
Generating realistic synthetic populations is funda
mental to valid agent-based modeling [25].
Population Synthesis Methods. Iterative Pro
portional Fitting (IPF) [5] and its variants are
commonly used methods, adjusting cell weights to
match marginal distributions from census data. Be
yond IPF, prior work also explores alternative formu
lations such as combinatorial optimization, Bayesian
approaches, and deep generative models (DGMs)
While DGMs can generate diverse populations be
yond observed samples, they often struggle to balance
sampling zeros (valid but unobserved combinations
with structural zeros (implausible combinations) [25]
Recent work explores LLM-based approaches: Li e
al. [24] proposed MobAgent, using LLMs to extrac
fine-grained mobility patterns from individual pro
files through self-evaluation and recursive reasoning
validated on 0.2M travel surveys. Ma et al. [30] de
veloped a foundation model using LLMs for semantic
enrichment of GPS trajectories, demonstrating trans
fer learning across regions (LA to Egypt) for mobility
pattern synthesis. While these LLM-based method
have been explored for individual trajectory genera
tion, they focus on personal mobility modeling rathe
than city-scale population synthesis with validated
demographic distributions and spatial assignments.
Spatial Assignment and Social Networks. As
signing synthetic individuals to geographic location

orld with Related Platforms
Scale Real Spatial Social
(Agents) Geography Detail Networks
< 100 No No No
< 100 No Limited Limited
Individual No No No
< 100 No Low No
Individual Yes POI-level No
< 100 No POI-level No
Individual Yes POI-level No
1K–10K No Medium Limited
1K–10K No Medium Limited
1K–10K Yes POI-level No
100K+ Yes Road-based Multi-layer
100K+ Yes Building No
100K+ Yes Building Multi-layer†
ot used in current experiments.
s important for spatial realism. Common approaches include: gravity models [1] for workplace assignment, distance-based allocation for
household placement, and constraint satisfaction
or student-to-school assignment. Jiang et al. [18]
developed a large-scale method generating 23 milion geographically-explicit individuals for New York
Metro Area with multi-layer social networks (household, work, school, daycare) emergent from spatial
co-location, highlighting the importance of social networks for urban simulations. Kashiyama et al. [21]
developed Pseudo-PFLOW, an agent-based framework that downscales census data to building-level
assignments using Markov chain models for activty generation, covering Japan’s 130 million population. While achieving strong validation results
R2=0.61–0.98 for population distribution), these approaches rely on traditional statistical models rather
han LLM-driven behavioral realism and lack integration with modern LLM agent frameworks.
Validation Approaches. Traditional validation
elies primarily on census data comparison. Recent work has begun incorporating mobile phone
data [40] for validating commuting patterns, buildng on foundational studies of human mobility paterns [11, 31, 13]. Ma et al. [30] demonstrated multievel validation through traffic simulation, achieving
MAPE < 6% for traffic volumes. However, systematic validation combining demographic distributions,

spatial assignments, and mobility patterns agains
real-world data remains rare.
Most synthetic population studies focus on de
mographic accuracy but neglect spatial validation
with real mobility data, social network construction
daily activity schedules, and integration with LLM
agent frameworks. GenWorld provides an end-to-end
pipeline that covers these aspects.
2.4 Knowledge Distillation for Agent
Simulation
Knowledge distillation [14] has been widely applied
in machine learning to compress large models into
efficient ones. Recent applications include:
Beyond model compression, recent work explore
abstraction and software architecture to scale LLM
agent simulations. Chopra et al. [4] introduce LLM
archetypes, where many agents share an archetypa
LLM policy to increase throughput at scale, but thi
can reduce individual-level heterogeneity and online
adaptivity. SocioVerse [45] targets population-scale
social simulation by aligning LLM agents to a large
pool of real users and standardizing simulation pro
cedures; however, it relies on large external dataset
and its alignment pipeline can be costly to reproduce
or transfer. For influence diffusion in social networks
LLM-AIDSim [44] integrates LLM-enhanced agent
into classical diffusion simulation pipelines, but the
approach is task-specific and may not directly gen
eralize to open-ended urban decision spaces. From a
systems perspective, SALLMA [2] proposes a layered
multi-agent architecture with orchestration and con
tainerized deployment; while improving modularity
and scalability, it does not inherently remove per
decision LLM inference costs and can require sub
stantial engineering infrastructure.
LLM Distillation. Distilling large language model
into smaller, faster models while maintaining perfor
mance is an active area of research. However, mos
work focuses on natural language tasks, not agen
decision-making in complex environments.
Agent Behavior Cloning. Imitation learning and
behavior cloning train efficient policies from exper
demonstrations. GenWorld extends this paradigm by
using LLMs as ”expert demonstrators” to generate
training data for efficient student models.
We apply knowledge distillation to enable city-scale
LLM agent simulation. Our approach estimates the
teacher’s discrete decision distribution via repeated
Monte Carlo sampling and compiles the resulting
probabilistic policy into efficient lookup tables, shift
ing expensive inference out of the simulation loop and

enabling large speedups in typical settings for largecale simulations.
As summarized in Table 1, GenWorld combines building-level population grounding with
census-validated demographics, city-scale scalability via offline knowledge distillation (200,000+
agents), multi-layer social networks derived from
patial co-location, and schema-validated LLMready interfaces that produce machine-readable behavioral traces in a real-city instantiation.
3 Agent Interface
GenWorld exposes a lightweight decision interface for
LLM agents and records each decision as a strucured log entry. This interface is designed to enable post-hoc qualitative inspection of agent rouines and failure modes and provide machine-readable
decision traces for offline distillation. Concretely,
each decision consumes a binned observation o˜
i,t
and a finite candidate set A , and produces a
i,t
chema-conformant JSON action, a validator bit,
and (if needed) a deterministic fallback outcome, all
ecorded as a log entry.
Observation and Action Schema At each decision point for agent i at time t, the simulator contructs a decision context from the city state x (time,
t
environment signals, and infrastructure states), a
ynthesized persona u produced by the population
i
nstantiation pipeline (core demographics and spaial anchors such as home/work/school when available, with optional household and social features),
and optionally short-term memory summaries m
i,t
distilled from recent logs. This context is denoted as
c = (x , u , m ). Given a decision query q , the
i,t t i i,t t
environment deterministically produces a binned obervation and a finite candidate action set:
o˜ = ϕ(c ; q ),
i,t i,t t
A = κ(q , o˜ ).
i,t t i,t
The function ϕ is implemented as a deterministic encoder stack that includes coarse binning and querypecific formatting. A prompt composer g(o˜ , q ) asi,t t
embles a stable template with question-specific slots.
The agent then outputs a structured JSON action
a ∈ A following a fixed schema (e.g., activity
i,t i,t
ype). A deterministic validator v(o˜ , a ) ∈ {0, 1}
i,t i,t
enforces schema and feasibility constraints; invalid
actions trigger a deterministic safe fallback before
execution, and all artifacts are logged. Figure 2
llustrates a representative query where raw perona/state fields are deterministically mapped into

coarse bins before being passed to the LLM. Figure 3
summarizes how the resulting structured outputs are
executed into full-day trajectories by lightweight de
terministic rules. In this implementation, persona
slices are intentionally sparse, while richer prefer
ence/trait slices can be added as optional extension
or treated as latent variables depending on the targe
application.
Two-Tier Decision Queries for Long-Horizon
Rollout Decision-making is separated into two
structured outputs with different time scales
ActivityPreference is a per-agent, persona
conditioned preference profile that is initialized once
(and optionally refreshed) and defines propensitie
over activity types for each high-level intention
DayPlan is a per-day (or per-checkpoint) plan tha
specifies a small mixture of intention-chain template
together with discretized POI-selection weights. The
plan sampling index is denoted by k (day-start o
checkpoint), which is much sparser than the simu
lator time step t used for execution, and the city
state at plan sampling time is written as x . The
k
intention space is fixed to {home, duty, leisure
maintenance}.
This two-tier abstraction is grounded in time
geography theory [12]: daily mobility is con
strained by capability (physical limits), coupling
(coordination with others), and authority (in
stitutional schedules). Our intention hierar
chy (home/duty/leisure/maintenance) captures these
canonical constraint classes, while the activity vocab
ulary covers the primary purposes observed in na
tional time-use surveys. The fixed ontology trade
open-ended expressiveness for tractability and re
peatability; extending the vocabulary is straightfor
ward within the same interface contract.
Critically, the day-level query is not conditioned
on a single intention; instead, the simulator provide
a small, day-type-specific candidate set of intention
chain templates (e.g., weekday vs. weekend vari
ants) and includes this candidate set as part of the
binned context. During rollout, agents sample a
DayPlan at day start, and the simulator consume
it through a lightweight executor (as shown in Fig
ure 3) to produce an explicit trajectory of simu
lator actions. Concretely, an intention-chain tem
plate is sampled from the day-type-specific candi
date set, expanded into activity types by sampling
ActivityPreference, and grounded into concrete
destinations via a fixed activity-to-place ontology and
feasibility checks. Overrides may be requested by
the agent or forced by the simulator when feasibility
checks fail or exogenous events invalidate the plan

n both cases, a deterministic return-home fallback is
applied and the agent stays at home until the next
plan sampling time (day-start or checkpoint). Secion 4 describes how decision traces are collected under binned contexts and compiled into scalable student policies.
Formal Contract Summary The formal contract
Figure 2) is summarized as follows. The simulator
deterministically maps raw persona and state fields
nto coarse bins via encoders b and b :
u x
I = {home, duty, leisure, maintenance},
u˜ = b (u ), x˜ = b (x ),
i u i k x k
τ ∈ {weekday, weekend},
C ⊆ I∗.
τ
where τ is a coarse day-type label and C is a small
τ
predefined candidate set of intention-chain templates.
The per-agent query defines a conditional categorical
distribution over activity types given intention z:
A (z) := ActivityPreference (z),
i i
A (z) = {(a, p(a | z))} , z ∈ I,
i a∈Az
(cid:88)
a ∈ A , p(a | z) = 1,
z
a∈Az
where A is a small predefined set of activity types
z
allowed under intention z (Appendix A.3). The perday (or per-checkpoint) query returns:
D = DayPlan (x˜ , u˜ , C ),
i,k i,k k i τ
D = (r , C , w ),
i,k i,k i,k i,k
C = {(c , π )}|Cτ |,
i,k j j j=1
(cid:88)
|Cτ |
r ∈ {0, 1}, π = 1,
i,k j
j=1
c ∈ C ⊆ I∗,
j τ
w (z) = (ℓnear(z), ℓpref(z), ℓcost(z)),
i,k i,k i,k i,k
ℓ∗ (z) ∈ {0, . . . , 10}, z ∈ I,
i,k
where C is a small predefined candidate set
τ
of intention-chain templates (in our instantiation,
C | = 6 per day type). Here r is an override reτ i,k
quest flag, each c is an intention-chain template, and
j
w (z) specifies discretized POI-selection weights for
i,k
ntention z. Here k denotes the plan sampling index
day-start or checkpoint), which is much sparser than
he execution time step. Overrides may also be forced
by the simulator when feasibility checks fail; in either
case, a deterministic return-home fallback is applied.

Figure 2: Query-conditioned prompt construction for our structured decision interface. Raw persona/state
fields are deterministically mapped into coarse bins and are not included verbatim in the prompt. The figure
schematically illustrates prompt variants used in this instantiation: a per-agent ActivityPreference query
over a fixed candidate set under a given intention, and day-level prompts that score POI-selection preferences
over near/pref/cost weights and intention-chain templates over a predefined chain candidate set. In this
default instantiation, POI-weight scoring and intention-chain scoring are issued jointly as a single DayPlan
query, but they can also be queried separately. Input features are represented using coarse discrete bins,
while candidate scores returned by the teacher are integers in [0, 10] over a predefined option set. Section 4
describes how these structured traces are aggregated and compiled for scalable rollout.
schema, a discrete and bounded action space with
strict validation, and deterministic execution semantics are enforced. At city scale, even rare formatting
or parsing failures can derail long simulations. LLM
decisions are therefore constrained to a small discrete
action set with a fixed schema, and strict validation
and deterministic fallback rules are enforced in the
decision logger. This design makes decision traces directly machine-readable and suitable for downstream
analysis and policy compilation (Section 4).
Figure 3: Plan-to-trajectory execution with a twotier decision structure. ActivityPreference pro4 Distillation and Scaling
vides persona-conditioned activity propensities, while
DayPlan specifies intention-chain templates and POITo scale LLM-driven decision-making to city-scale
selection weights. A lightweight executor produces
simulations, the teacher’s stochastic decision behavexplicit trajectories through fixed ontologies and feaior is distilled into empirical score vectors and samsibility checks.
pling distributions under discretized contexts by repeatedly querying the LLM under identical context
keys and aggregating its scores over a fixed candiTool-Oriented Interface, Robustness, and date set (e.g., intention-chain templates or intentionTraceability The interface is realized as stable conditioned activity templates). Because the interprompt templates with strict JSON schemas that face bins raw contexts into discrete keys and restricts
are validated and logged by the simulator, and each query to a finite candidate set with strict valcan be wrapped by standard tool-calling middleware idation, the teacher can be repeatedly queried unwhen needed. A fixed, query-conditioned observation der identical keys and its scores can be aggregated.
8

The key idea is to shift expensive inference out o
the simulation loop: a one-time offline cost is paid to
estimate these distributions, and the resulting com
piled tables are executed via amortized constant-time
lookup and sampling given bounded candidate set
per query, with respect to the number of agents and
decision steps.
In a micro-benchmark on the compiled
ActivityPreference table, Python lookup achieve
1.85M queries/s (0.54 µs per query) over 200,000
randomized context keys. While absolute throughpu
depends on hardware and implementation details
this benchmark highlights the potential for large
speedups relative to online LLM inference in typica
settings. End-to-end wall-clock time per simulato
step also includes environment updates, routing, and
execution overheads. Prompt templates used fo
distillation are listed in Appendix A.4.
Action Primitives and Context Discretiza
tion Repeated sampling requires that the teache
be queried under identical contexts. Following the
interface contract in Section 3, raw persona and
state are discretized into bins (e.g., u˜ = b (u )
i u i
x˜ = b (x)) and each decision query q is treated
x t
as defining its own finite action space. Concretely
for each query type q (e.g., ActivityPreference
t
or DayPlan), an executable discrete action set A
q
is defined that matches the simulator’s structured
schema and validation rules. A finite context key
s = (u˜ , x˜, q , τ ) is then formed, where τ indexe
i t
the day-type-specific candidate template set used by
DayPlan. This makes repeated offline teacher ag
gregation well-defined and enables compilation into
amortized constant-time lookup policies. The day
type indicator τ is included explicitly because the
DayPlan candidate set differs across day types (e.g.
weekday vs. weekend).
Computational Motivation At city scale, a di
rect teacher-driven simulation requires O(N T ) LLM
calls, where N is the number of agents and T is the
number of decision points per simulated day. For ex
ample, N = 200,000 agents with 15-minute time step
over 24 hours yields T = 96 and thus 1.92 × 107 call
for a single day, which is computationally expensive
in practice. Distillation reduces simulation-time in
ference to amortized constant-time table lookup and
sampling with respect to the number of agents and
decision steps.
Repeated Teacher Query Aggregation For a
fixed candidate set A and context key s, K teache
qt
score vectors {r(k)(·)}K are sampled, where each
k=1

query returns an integer score r(k)(a) ∈ [0, 10] for
every candidate a ∈ A . The mean score and conqt
istency statistics are aggregated:
K
1 (cid:88)
µ(a | s) = r(k)(a), (1)
K
k=1
(cid:118)
(cid:117) K
(cid:117) (cid:88)(cid:0) (cid:1)2
σ(a | s) = (cid:116)K−1 r(k)(a) − µ(a | s) . (2)
k=1
The aggregated mean scores are normalized across
candidates into a categorical sampling distribution
π(· | s), which is used for simulation-time sampling.
Since scores are in [0, 10], an executable sampling
distribution is constructed by normalizing the mean
cores:
π(a | s) = Normalize (µ(a | s)) , a ∈ A . (3)
qt
The score variability σ(a | s) is reported to quantify
eacher consistency across repeated queries (and to
diagnose context regions with high variability).
Policy Compilation and Simulation-Time Inerence The aggregated scores and sampling disributions (e.g., µ(· | s) and π(· | s)) are compiled
nto per-query lookup tables keyed by discretized conext features (persona bins, time bins, coarse locaion types, scenario indicators, and day-type indicaors). During simulation, agents sample an intentionchain template or activity template according to the
distilled distribution rather than querying the LLM,
and execute the sampled schema through the same
validator/executor as the teacher outputs. Scoring
and sampling over intention-chain templates enables
ong-horizon diversity while keeping the execution inerface lightweight. This compilation separates two
concerns:
• Teacher inference (offline): generate multiple samples per context to estimate µ(· | s) (and
σ(· | s)), then derive π(· | s).
• Agent rollout (online): execute a lightweight
stochastic decision rule by table lookup and sampling.
Context Design and Coverage To make compiation feasible, contexts are discretized into a finite
key space (e.g., persona bins, coarse location types,
and time bins) and representative contexts are sampled according to the instantiated population disribution. This allows the offline sampling budget

Figure 4: Teacher preference scores (0–10) for Acti
candidate activity types (columns), shown separatel
define the simulation-time sampling distribution use
(a) Weekday intention-chain template preference.
Figure 5: Distilled teacher scores for DayPlan intent
weekend candidate sets.
to be allocated where it matters most while keep
ing simulation-time inference amortized constant
time with respect to the number of agents and de
cision steps. This discretization trades off fidelity fo
tractability: behavior matching depends on contex
key design and coverage, and unseen keys may require
backing off to coarser keys or a conservative default.
5 Empirical Grounding of the
Urban World
Our reference instantiation integrates multi-source
empirical datasets, including official census statistic
and administrative boundaries, building footprint
and POIs, parcel-level land-use labels, a complete

tyPreference across persona categories (rows) and
or maintenance (left) and leisure (right). The scores
y the compiled policy.
(b) Weekend intention-chain template preference.
-chain templates, shown separately for weekday and
oad network with elevation, and anonymized mobility data for commuting diagnostics. These inputs
provide constraints for population synthesis and spaial grounding, and also provide independent signals
or validation.
Detailed data sources and processing steps are provided in Appendix A.2 (Table 3).
5.1 Population and Environment
Foundation
This section describes the empirically-grounded population and environment foundation used in our Higashihiroshima reference instantiation, grounded in
publicly available census tabulations and geospatial
ayers (buildings, land use parcels, school districts,

POIs, and roads), synthesizing 196,608 individual
across 89,988 private households, with 5,641 addi
tional group-quarter records retained separately. The
formulation combines demographic micro-synthesi
under tract-level census constraints with spatia
grounding of home, school, and work locations un
der capacity and distance constraints.
5.1.1 Tract-Level Micro-Synthesis and At
tribute Assignment
For each tract t, the total population N is treated a
t
a hard constraint and an age–gender joint distribu
tion is estimated whose marginals match census age
counts and gender totals. A 2D IPF procedure i
adopted on an age × gender matrix M (t):
M a (k ,g + 2 1 ) = M a (k ,g ) · (cid:80) n t M ,a (k) (4
g′ a,g′
M a (k ,g +1) = M a (k ,g + 1 2 ) · (cid:80) n t,g (k+ 1 ) (5
M 2
a′ a′,g
where n is the census count of age bin a in
t,a
tract t, and n is the census total of gender g ∈
t,g
{male, female}. M (t) is initialized with a strictly pos
itive prior (e.g., uniform or tract-independent) and
Eq. (5) is iterated until marginal errors fall below
or for a fixed number of rounds. Individuals are then
sampled from the normalized joint distribution, and
a concrete integer age is sampled uniformly within
the selected age bin.
Given the sampled individuals, households are
formed using the tract household-size histogram
(1,2,3,4,5,6+) with a lightweight plausibility heuristic
(e.g., capping household size at 6). The census house
hold count target H is enforced and household size
t
are sampled to match the tract histogram. Employ
ment status and occupation categories are then as
signed for working-age individuals so that tract-leve
employed totals and occupational marginals match
the census. Let I be individuals in tract t, and
t
W ⊂ I be working-age individuals. Denote the
t t
census employed target as E and the census occu
t
pation target counts as C for occupation category
t,o
o ∈ O. Let E′ = min(E , |W |) and let C′ be ad
t t t t,o
justed occupation targets derived from {C } by
t,o o∈O
padding/truncation so that (cid:80) C′ = E′. The
o∈O t,o t
following constraints are enforced:
(cid:88)
I[employed ] = E′ (6
i t
i∈Wt
(cid:88)
I[employed ∧ occ = o] = C′ , ∀o ∈ O (7
i i t,o
i∈Wt

Eq. (6)–(7) are realized via seeded sampling: an employed subset of size E′ is drawn and an occupation
t
multiset with counts C′ is assigned, followed by a
t,o
ract-seeded random permutation.
5.1.2 Spatial Grounding of Home, School,
and Work
Households are assigned to residential buildings
within each tract using a capacity-aware allocaion; students are assigned to schools using disrict polygons when available with nearest-school
allback; university assignment uses a distancebased stochastic choice with weights proportional to
1/d2. For workplace allocation, employed individuals are mapped to landuse parcels (not building
Ds) using an occupation-conditioned landuse prior
occupation→landuse mapping with ratios r ) too,l
gether with a maximum commute-distance constraint
d .
max
Capacity inference by area (quotas). For occupaion o, let total employees be N , eligible landuse
o
categories be L , and the configured landuse ratio be
o
(cid:80)
r for l ∈ L with r = 1. For each landuse
o,l o l∈Lo o,l
parcel j of category l with area A , an occupationj
pecific quota is defined:
N r A
q = o o,l j , j ∈ P , l ∈ L (8)
j,o (cid:80) A l o
k∈Pl k
where P is the set of parcels with landuse category
l
. Fractional quotas are converted into integer capacties qˆ (e.g., via floor with remainder redistribution
j,o
or stochastic rounding) to preserve total capacity per
occupation.
Gravity-based allocation. We employ a gravity
model to assign workplaces, balancing employment
opportunities with distance decay. Let d be the
ij
haversine distance between employed individual i’s
home and landuse parcel j. The probability P of
ij
ndividual i choosing workplace j is proportional to
he parcel’s destination attractiveness (capacity) and
nversely proportional to commute distance:
P ∝ Aα · f (d ) · M (9)
ij j ij ij
where A is the capacity (attractiveness) of parcel
j
, f (d) = d−β is the distance decay function with
riction parameter β, and M is a binary mask enij
orcing occupation compatibility (M = 1 if parcel
ij
supports individual i’s occupation o and j has rei
maining capacity, else 0). We set α = 1 and calibrate
β against empirical mobility data. The assignment is
performed stochastically:
j∗ ∼ Categorical({P } ) (10)
ij j

This probabilistic approach allows for a realistic dis
tribution of commute distances, including long-tai
commutes, unlike strict distance minimization.
5.1.3 Derived Social Networks
Multi-layer networks are a deterministic byproduc
of the assigned home/school/work locations and in
stitutional membership. While not used by the agen
interface or the experiments in this paper, they are re
tained as an optional artifact for internal consistency
checks and future extensions:
G = (V, E), (11
E = E ∪ E ∪ E ∪ E
household home school work
∪ E (12
neighborhood
where edges represent interaction opportunities in
duced by shared households, shared residential build
ings, shared schools, shared workplace landuse, and
neighborhood proximity. To keep graphs sparse a
scale, degrees are capped or edges are sampled within
large buildings/institutions and edges can optionally
be weighted by co-location frequency.
5.1.4 Urban Environment Integration
The platform integrates multiple layers of urban in
frastructure:
E = {P, R, B, A} (13
where:
• P: POI catalog with categorical attributes P =
{(p , type , capacity , hours )}
i i i i
• R: Road network graph R = (V , E , w ) with
r r r
edge weights (distance, speed, capacity)
• B: Building set with spatial footprints and land
use B = {(b , geom , use , C )}
i i i i
• A: Administrative hierarchy (census blocks, dis
tricts, city) for spatial aggregation
When explicit capacities, opening hours, or road
capacity attributes are missing in the source layers
the implementation uses conservative defaults or sim
ple rule-based proxies (e.g., POI-type-specific heuris
tics and road-class-based speed/capacity settings) to
support feasibility checks.

5.2 Activity Generation and Temporal Grounding
We implement a hybrid generative mechanism to
ensure both behavioral realism and temporal fidelity.
While the sequence and semantics of daily activties (e.g., the decision to visit a gym after work) are
generated by the LLM-distilled policy to capture heterogeneous preferences, the temporal attributes
start time and duration) are grounded in the National Time Use Survey. Specifically, once an
activity type is selected by the agent, its timing is
ampled from the corresponding empirical distribuion (e.g., ’Sports’ duration distribution for a ’Gym’
visit), thereby preventing unrealistic hallucinations
common in pure LLM scheduling.
We utilize the action initialization probabilty (derived from activity start-time statistics) rather
han the raw action participation rate (occupancy). Using raw occupancy rates as sampling probabilities—a common pitfall—would incorrectly bias
he duration of activities. Our pipeline explicitly
eparates the decision to start an activity from the
duration of the activity, ensuring that the generated
emporal dynamics mathematically align with the aggregate census observations.
5.3 Population Distribution Validation
We validate our synthetic population against census
data at the tract level to ensure demographic accuacy.
5.3.1 Census Data Validation
Our population synthesis method generates 196,608
ndividuals across 89,988 private households in Higashihiroshima, with 5,641 additional group-quarter
ecords retained separately from private-home assignment. We validate the synthetic population against
2020 Japanese Census tabulations at census-tract
granularity across multiple demographic dimensions.
For household size statistics, the census reports
general household counts, while some tracts include
non-household residents (e.g., dormitories or instituional facilities). We therefore evaluate household
ize distributions on tracts where total population
equals general-household persons (see Appendix A for
details).
Distributional Fit Metrics We distinguish hard
constraints from soft-fit metrics. Tract-level total

population is constrained to match census totals ex
actly, yielding very close agreement with census to
tals by construction. We therefore emphasize distri
butional similarity for variables not enforced as exac
constraints.
After restricting census tabulations to the instan
tiated study area, we obtain 198 finest-resolution
census units (HYOSYO=2/4). We evaluate de
mographic fit on 185 tracts; 13 census units with
zero population and zero households (e.g., industria
parks) are excluded. Gender ratios are well matched
(male ratio MAE < 0.02). Age distributions achieve
mean L1 = 0.1229 (median 0.10, max 0.31), mean KS
= 0.0299 (max 0.12), and mean JS = 0.0047 (max
0.02), with 95% of tracts having L1 < 0.20. House
hold size distributions achieve mean L1 = 0.0547
mean KS = 0.0269, and mean JS = 0.0075. Em
ployment counts (15+) show high tract-level agree
ment (R2 > 0.99). Occupation distributions achieve
mean L1 = 0.1945, mean KS = 0.0972, and mean JS
= 0.0382. The tight distribution of per-tract error
reflects the effectiveness of the IPF constraints.
5.3.2 Spatial Distribution Validation
Unlike TAZ-based methods that assign residents to
abstract zones, our building-level approach assign
households to specific georeferenced buildings unde
tract-level and capacity constraints. Because build
ing footprints and land-use labels may be incomplete
in a small number of tracts (e.g., industrial parks)
we report explicit assignment diagnostics rather than
silently forcing fallback placements.
In our reference instantiation, all 89,988 private
census-target households are successfully assigned to
residential buildings. The 5,641 unmapped household
records are group-quarter records and are intention
ally excluded from private-home placement rathe
than treated as failed residential assignments.
5.3.3 School Assignment Validation
School assignment uses building-level home locations
Elementary and junior-high students are assigned by
school-district polygons with nearest-school fallback
High-school assignment is nearest-school based with
limited randomness among candidates within a dis
tance threshold, and university assignment uses a
gravity-style stochastic choice with weights propor
tional to 1/d2.
In our reference instantiation, 42,376 out of 42,584
in-scope students are assigned to a school (99.51%)
The remaining 208 in-scope records are flagged a
too far stay home by the diagnostic pipeline rathe

han silently assigned through unconstrained fallback rules; 747 school-age group-quarter residents are
reated as out of scope for private home-based school
assignment. We report the assigned school enrollment distribution in Figure A2.
5.4 Mobility Pattern Validation
We compare commuting statistics against
anonymized mobile phone mobility data from
Yahoo Japan Mobility (YJMob100K) [40]. The
dataset discretizes location pings into 500m × 500m
grid cells and timestamps into 30-minute bins, with
he metropolitan area undisclosed for privacy. For
our case study, we extract a subregion consistent
with the Higashihiroshima area by registering the
eleased mesh grid via manual rigid alignment. The
egistration uses coastline landmarks and major
errain features as control points, with an estimated
alignment error of <500m (one grid cell). A senitivity analysis indicates that commute distance
distributions are robust to registration errors within
his range. The extraction workflow is documented
n the repository at data_prepare/mobility_
validation/README.md, with comparison scripts
under data_prepare/mobility_validation/ and
data_prepare/step3_assignment/work/; the
comparison is treated as a commuting-distance
diagnostic rather than an OD-flow benchmark.
We infer each user’s home mesh from nighttime
ecords and work mesh from daytime records (fixed
ime windows), then derive a commuting distance disribution in the mesh space. Figure 6 summarizes the
extracted commuting patterns for the selected subregion.
The released validation artifact extracts 7,525
YJM-derived commuters from the selected subregion,
with a mean commute distance of 7.45 km, median of 5.00 km, and 90th percentile of 19.24 km.
Against this reference, the 90,744 synthetic workers
assigned to workplaces have a mean commute disance of 10.81 km, median of 10.09 km, and 90th
percentile of 19.15 km. The resulting KS distance is
0.359 (0.399 when restricted to commutes ≤20 km).
This diagnostic indicates that the current workplace
assignment captures the upper-tail scale but underepresents very short commutes and overrepresents 5–
15 km trips. We therefore use YJM as a commutingdistance diagnostic and not as evidence of calibrated
OD-flow prediction.
Figure A4 compares the resulting distributions.
We treat this comparison as a commuting-distance
diagnostic rather than a strict OD-flow correlation,
because the observed mesh space is anonymized and

requires manual registration.
Figure 6: Commuting pattern extraction from YJ
Mob100K after registering the anonymized mesh grid
to our study area. The figure visualizes inferred
home/work points and commuting distance statistic
for the extracted subregion.
Figure 7: Commuting distance distributions unde
building-level grounding versus a tract-centroid base
line. The baseline collapses within-tract heterogene
ity by placing all households at tract centroids, il
lustrating how coarse spatial grounding can distor
short-range commuting structure even when work
place assignments are held fixed.
6 Platform Architecture
GenWorld emphasizes modularity (independen
components for flexibility), scalability (efficient han
dling of 200,000+ agents in our reference instan
tiation), and accessibility (LLM-compatible inter
faces for AI researchers). Figure 8 illustrates the de
tailed system architecture. Platform UI screenshot
(Streamlit-based interface) are provided in Appendix
Figure A5.
6.1 System Overview
The platform is organized into three layers:

Layer 1: Population and Environment Foundation Instantiates the georeferenced urban world
and synthetic population under census constraints
and reports validation diagnostics; see Section 5.
Layer 2: Agent Decision Framework Exposes a structured agent–environment interface with
binned observations and finite JSON-validated action
candidates, enabling rule-based, teacher-LLM, and
distilled-student policies; see Sections 3 and 4.
Layer 3: Simulation Engine Orchestrates timetepped multi-agent execution with feasibility checks,
ystem-level consistency updates, and detailed logging; see Section 6.2.
The following subsections detail the simulation engine.
6.2 Simulation Engine
The simulation engine orchestrates time-stepped
multi-agent execution, managing time progression,
patial dynamics, and system-level feasibility contraints. The engine is designed to support both
mall-scale LLM experiments and large-scale distilled
imulations.
Time-stepped Execution (Pseudo-code) The
imulator advances in discrete time steps (typically
15-minute intervals) and executes validated actions
under feasibility constraints, while recording strucured decision traces for analysis and offline compilaion.
This modular architecture supports repeatability
hrough deterministic execution and configurationbased parameters, while enabling extensibility for
new agent models, additional cities, and integration
with external frameworks.
7 Evaluation Cases and Scalability
7.1 Evaluation Cases
We report three simulation cases selected according
o three criteria: (i) the case is generated by the
public pipeline or the paper-figure reproduction conract, (ii) it has quantitative checks for schedule completeness and spatial feasibility, and (iii) it supports
a specific claim about GenWorld rather than only
erving as a visual showcase. Table 2 summarizes
he cases. In all reported runs, each person has a
complete 1,440-minute daily schedule with no gaps

Figure 8: GenWorld System Architecture. The plat
ronment Foundation, Agent Decision Framework, a
integration and knowledge distillation for city-scale
Algorithm 1 Time-stepped simulation engine with
structured decision interface
1: for each simulation step t do
2: determine active agents S t from schedules
3: for each agent i ∈ S t do
4: construct context c i,t from world state and
persona
5: o˜ i,t ← ϕ(c i,t ; q t ) ▷ binned observation
6: A i,t ← κ(q t , o˜ i,t ) ▷ finite candidate
7: a i,t ← π(o˜ i,t , A i,t ) ▷ rule/teacher/studen
8: if v(o˜ i,t , a i,t ) = 0 then
9: a i,t ← f (o˜ i,t ) ▷ deterministic fallback
10: end if
11: execute a i,t and update agent/world state
12: append decision record and trajectory log
13: end for
14: apply system-level consistency updates (e.g.
travel-time feedback and POI capacity)
15: record aggregate metrics (e.g., utilization and
travel-time indicators)
16: end for

m is organized into three layers: Population & EnviSimulation Engine. The architecture supports LLM
ability.
or overlaps, and the activity-to-land-use compatibilty checker reports zero violations.
7.1.1 Case 1: Full-City Weekday Baseline
The full-city baseline simulates 196,608 agents disributed across 89,988 private households, with addiional group-quarter records retained separately from
private-home assignment. Building-level home asignment, home/school/work anchors, and daily acivity schedules are executed under the structured inerface. The run produces 947,233 activity records.
Each agent receives a complete daily schedule from
midnight to midnight. Aggregated by duration, home
activities account for 79.25% of person-minutes, duty
activities (work and study) for 16.22%, leisure for
2.43%, and maintenance activities for 2.11%. The
median nonzero movement distance is 5.59 km, the
95th percentile is 17.26 km, and no movement exceeds 50 km.
We visualize the spatial distribution of agents and
heir daily commuting flows. The 3D visualization
upports qualitative inspection of residential denity gradients, commuting corridors, activity hotspots
around commercial and institutional areas, and day–
night population shifts. Figure 9 shows two snapshots
of the visualized resident locations: during worktime
he distribution exhibits strong clustering around ac-

Table 2: Evaluation cases included in the paper. Duration shares are computed over total person-minutes.
Movement statistics use nonzero movement records between consecutive activity locations.
Case Scope Key evidence Supported claim
Full-city weekday 196,608 agents, Home 79.25%, duty 16.22%, non- City-scale rollout over
baseline weekday normal home 20.75%; movement p95 = 17.26 an empirically grounded
km; no trips over 50 km synthetic population
Weekday–weekend 1,000-agent Duty decreases from 15.68% on week- The same population
contrast paired diagnos- day to 0% on weekend; leisure in- can express different
tic creases from 3.81% to 37.92%; no temporal regimes under
land-use violations controlled day-type
constraints
Warning-response 1,000 agents, After the warning, all agents are Scenario perturbations
perturbation weekday alarm at home at 15:00, 16:00, and can trigger schedule
at 15:00 18:00; emergency-return-home occu- replanning and propies 37.5% of person-minutes duce auditable response
traces
tivity centers (e.g., the Hiroshima University area), results do not validate weekend behavior against inwhile at nighttime these daytime hotspots become dependent observations; instead, they show that Gensparse as residents return to their home neighbor- World can apply different day-type constraints to the
hoods. same synthetic population while preserving schedule
Additional weekday spatial heatmaps for represen- and land-use consistency.
tative activity types (shopping, socializing, and childcare) at multiple time windows are provided in the
7.1.3 Case 3: Warning-Response Perturbaappendix (Figure A6).
tion
We also summarize the city-scale diurnal rhythm
by aggregating simulated activity occupancy over We include a warning-response case as a controlled
time. Figure 10 visualizes the 24-hour distribution perturbation test rather than as a calibrated disof activity categories as a radial stacked plot, provid- aster model. Starting from a weekday setting, an
ing a compact view of time-of-day regularities in the alarm is introduced at 15:00. The policy then rebaseline rollout. plans subsequent activity segments under a ruleconstrained emergency response, producing explicit
emergency return home records and preserving the
7.1.2 Case 2: Weekday–Weekend Behavioral
same schedule-completeness constraints.
Contrast
In the 1,000-agent alarm run, the simulator proTo test whether the same population foundation can duces 6,000 activity records. The run passes the landsupport different temporal regimes, we compare two use compatibility checker with zero violations. At
1,000-agent diagnostic runs under weekday and week- 15:00, 16:00, and 18:00, all 1,000 agents are at home
end settings. Both runs pass the same schedule- according to the diagnostic evaluator. Emergencycompleteness and land-use compatibility checks. The return-home records account for 37.5% of total
weekday run contains 5,016 records and includes person-minutes. This case demonstrates that Genwork/study duty activities, while the weekend run World can inject a scenario perturbation, replan
contains 5,000 records and removes duty activities by schedules, and produce auditable response traces.
construction. It should be interpreted as an illustrative warningThe contrast is clear at the duration level. In the response stress test, not as evidence that the current
weekday run, duty activities account for 15.68% of implementation predicts real evacuation behavior or
person-minutes, while leisure activities account for fully implements a psychological theory of disaster
3.81%. In the weekend run, duty falls to 0% and response.
leisure rises to 37.92%. The spatial pattern also
changes: the weekend movement-distance distribu7.1.4 Road-Flow Visualization
tion is shorter (p95 = 5.67 km) than the weekday
distribution (p95 = 13.85 km), reflecting more local We further visualize aggregate road-network traffic
discretionary activity in the diagnostic sample. These flow by routing simulated trips between consecutive
16

Figure 10: 24-hour activity occupancy distribution
in the baseline rollout, shown as a radial stacked
plot (outer radius indicates more people). The visualization highlights the expected day–night cycle:
home/sleep dominates overnight, work and study in-
(a) Worktime resident-location heatmap.
crease during daytime hours, and leisure and other
discretionary activities rise in the evening.
activity locations. Figure 11 shows the all-day flow
map computed from a 50,000-resident sample, where
edge color intensity indicates higher accumulated volumes. Note that this is a static shortest-path visualization without dynamic congestion feedback; validating against real-time traffic counts and incorporating equilibrium assignment are left for future work.
7.1.5 Scalability Analysis
Through offline compilation, simulation-time
decision-making can be implemented as amortized constant-time table lookup and sampling
under bounded candidate sets. The computational
(b) Nighttime resident-location heatmap. complexity comparison is as follows:
Figure 9: Day–night contrast of visualized resident • Online LLM: O(N · T · C ) per simulated
LLM
locations in the baseline rollout. The worktime snap- day, where N is agent count, T is decision steps
shot highlights dense daytime clustering around ma- per day, and C is per-query LLM inference
LLM
jor institutional and employment centers (e.g., the cost (typically 0.5–2s for local 7B models).
Hiroshima University area), whereas the nighttime
snapshot shows these areas becoming nearly empty as • Distilled policy: O(N · T · C lookup ), where
the population shifts back toward residential neigh- C lookup ≈ 1µs (hash table lookup + categorical
borhoods. sampling).
For N = 200,000 agents with T = 96 decision
points per day (15-minute steps), online LLM simulation would require ∼19M inference calls per simulated
day, which is computationally expensive in practice.
Our distilled policy replaces these calls with table
17

Figure 11: All-day road-network traffic flow aggre
gated from a 50,000-resident sample. Trips are routed
via static shortest paths (no congestion feedback)
edge intensity indicates accumulated volume. Thi
is intended as a visualization of spatial demand pat
terns rather than a validated traffic simulation.
lookups, allowing city-scale rollout in our reference
setup.
In a micro-test, Python lookup achieves 1.85M
queries/s (0.54µs per query) over 200,000 random
ized context keys on an Intel Core i5-14600K CPU
End-to-end wall-clock time per simulator step also in
cludes environment updates, spatial queries, and ac
tivity execution; profiling under varying agent count
is ongoing work.
7.2 Summary
These cases show three aspects of GenWorld: city
scale rollout over an empirically grounded popula
tion, controlled behavioral contrast across day types
and auditable replanning under a warning perturba
tion. The results support GenWorld as a reproducible
simulation infrastructure. They do not by themselve
establish calibrated forecasting performance for traf
fic, evacuation, or policy outcomes; broader valida
tion would require additional external observation
and scenario-specific calibration.
8 Discussion
Limitations and Future Work Several limita
tions remain in the current reference instantiation.
Validation Scope We validate synthetic popu
lations against census tabulations, commuting dis

ances against YJMob100K mobile phone data, and
activity schedules against the Japanese National
Time Use Survey (e-Stat). Our activity schedule
validation shows good agreement for diurnal paterns (average correlation r > 0.86, RMSE < 3%),
hough peak-time shifts for work/study activities suggest lunch-break modeling needs refinement. Broader
validation, such as link-level traffic counts and full
OD-flow correlation, would require additional calibrated datasets and is left for future work.
Distillation Fidelity Our distillation pipeline aggregates teacher-model responses into lookup tables,
but the fidelity of this compilation is not fully validated. We use K = 10–30 samples per context key
with a single teacher model (Gemma 3 27B); ablation
of sampling count, temperature, and teacher model
choice is needed. We also do not quantitatively compare distilled outputs against fresh teacher queries
e.g., via KL divergence or decision agreement rate).
Behavioral Modeling The structured interface
enables logging and analysis of LLM-driven decisions,
but connecting these to human decision processes is
not addressed here. Possible extensions include comparisons against human subjects or stated-preference
urveys, sensitivity analyses of prompt design, and
evaluation of emergent behaviors under scenario perurbations.
Case-Study Boundaries The three cases in Secion 7 are intended to demonstrate infrastructure
capabilities under controlled settings. The fullcity weekday case supports scalability and schedulegeneration claims, while the weekday–weekend comparison demonstrates that the same population can
be simulated under different temporal constraints.
The alarm case is more limited: it is a warningesponse perturbation with rule-constrained replanning and should not be interpreted as a calibrated
evacuation model, a validated disaster-response forecast, or a full implementation of Protection Motivaion Theory. Its role is to show that GenWorld can inect a scenario event and produce auditable response
races for later behavioral calibration.
Generalizability The current implementation
s instantiated in Higashihiroshima, a mid-sized
Japanese city with approximately 200,000 residents.
Higashihiroshima has a relatively dispersed urban
orm centered around Hiroshima University; scalabilty to denser metropolitan areas (Tokyo, Osaka) with
more complex transit networks remains untested,

and computational challenges may arise at 10×
population scales.
Our data pipeline relies on Japan-specific source
(e-Stat census, YJMob100K mobility, Hiroshima
DoBOX land use). Replication elsewhere require
equivalent data sources and adapted preprocessing
availability and format consistency vary across re
gions. Activity patterns and commuting behav
iors also differ across urban contexts—US suburban
sprawl, European compact cities, and Asian high
density development each have distinct characteris
tics. The distilled decision distributions may no
transfer without local calibration.
Potential Application Scenarios Although the
results reported in this paper focus on empirica
grounding, scalable rollout, and controlled scenario
diagnostics, the same instantiation and structured de
cision traces can support qualitative what-if analyses
Example extensions include transportation-demand
inspection under hypothetical transit or land-use
changes, warning-response experiments with riche
behavioral models, and urban policy diagnostics un
der routine or capacity modifications. Such uses re
quire scenario-specific assumptions, calibration data
and validation metrics before they can be treated a
forecasts or decision-support evidence.
9 Conclusion
This paper introduced GenWorld as an empirically
grounded urban simulation infrastructure for scalable
LLM-agent studies. The central problem is not pop
ulation synthesis alone or LLM distillation alone, bu
the connection between the two: LLM-agent simu
lations need realistic urban constraints, while city
scale rollout cannot rely on online LLM calls for every
agent decision.
GenWorld addresses this grounding–scaling gap
through a connected system design. A building-leve
synthetic urban world provides census-consisten
population structure, spatial anchors, and land-use
constraints. A structured agent interface maps city
and persona states into binned observations, finite
candidate sets, JSON-valid actions, deterministic ex
ecution semantics, and machine-readable traces. Of
fline policy compilation then shifts repeated teacher
model queries out of the rollout loop and exe
cutes compiled stochastic policies through lightweigh
lookup and sampling.
The Higashihiroshima instantiation demonstrate
the feasibility of this infrastructure for 196,608 syn
thetic residents, with demographic validation agains

census tabulations, commuting-distance diagnostics
against YJMob100K, and reproducible evaluation
cases covering full-city weekday rollout, weekday–
weekend contrast, and warning-response perturbaion. These results support GenWorld as a platform
or grounded and scalable LLM-agent experimentaion. They do not establish calibrated forecasting
performance for transportation, evacuation, or polcy analysis; such applications require additional behavioral calibration, external validation data, and
cenario-specific evaluation metrics. Code, configuations, documentation, and a deterministic public
demo are available in the project repository, followng the principles of reproducible urban research [7].
Code and Data Availability
Code, configuration files, documentation, and a deerministic public demo are available at https://
github.com/Perseus1993/genworld. The reposiory includes the staged data-preparation pipeline,
he public demo for tract 34212058004, and a paperfigure reproduction manifest. Large source datasets
and generated outputs are not redistributed in the
epository. Open or registration-based inputs should
be obtained from their original providers and placed
according to the paths documented in the repository.
YJMob100K-derived inputs are non-redistributable
and are used only as local validation inputs. The
arXiv source package contains only the manuscript
ources and figures needed to reproduce the paper
PDF.
Acknowledgments
We thank Xuesong (Simon) Zhou for his valuable suggestions.
References
[1] James E Anderson. The gravity model. Annu.
Rev. Econ., 3(1):133–160, 2011.
[2] Marco Becattini, Roberto Verdecchia, and Enrico Vicario. Sallma: A software architecture for llm-based multi-agent systems. In
2025 IEEE/ACM International Workshop New
Trends in Software Architecture (SATrends),
pages 5–8. IEEE, 2025.
[3] Filip Biljecki and Yoong Shin Chow. Global
building morphology indicators. Computers, Environment and Urban Systems, 95:101809, 2022.

[4] Ayush Chopra, Shashank Kumar, Nurullah
Giray-Kuru, Ramesh Raskar, and Arnau Quera
Bofarull. On the limits of agency in agent-based
models. arXiv preprint arXiv:2409.10568, 2024
[5] Abdoul-Ahad Choupani and Amir Reza Mam
doohi. Population synthesis using iterative pro
portional fitting (ipf): A review and future
research. Transportation Research Procedia
17:223–233, 2016.
[6] Joshua M Epstein and Robert Axtell. Growing
artificial societies: social science from the bot
tom up. Brookings Institution Press, 1996.
[7] Rosa F´elix, Filipe Moura, and Robin Lovelace
Reproducible methods for modeling combined
public transport and cycling trips and associ
ated benefits: Evidence from the biclar tool
Computers, Environment and Urban Systems
117:102230, 2025.
[8] Jie Feng, Jun Zhang, Tianhui Liu, Xin Zhang
Tianjian Ouyang, Junbo Yan, Yuwei Du, Siq
Guo, and Yong Li. Citybench: Evaluating the
capabilities of large language models for urban
tasks. arXiv preprint arXiv:2406.13945, 2024
Accepted by KDD 2025 D&B Track.
[9] Kunihiko Fujiwara, Ryuta Tsurumi, Tomok
Kiyono, Zicheng Fan, Xiucheng Liang, Binyu
Lei, Winston Yap, Koichi Ito, and Filip Biljecki
Voxcity: A seamless framework for open geospa
tial data integration, grid-based semantic 3d city
model generation, and urban environment simu
lation. Computers, Environment and Urban Sys
tems, 123:102366, 2026.
[10] Dawei Gao, Zitao Li, Xuchen Pan, Weiru
Kuang, Zhijian Ma, Bingchen Qian, Fei Wei
Wenhao Zhang, Yuexiang Xie, Daoyuan Chen
et al. Agentscope: A flexible yet ro
bust multi-agent platform. arXiv preprin
arXiv:2402.14034, 2024.
[11] Marta C Gonzalez, Cesar A Hidalgo, and Albert
Laszlo Barabasi. Understanding individual hu
man mobility patterns. nature, 453(7196):779–
782, 2008.
[12] Torsten H¨agerstrand. What about people in re
gional science. Transport Sociology: Social as
pects of transport planning, pages 143–158, 1970
[13] Samiul Hasan, Christian M Schneider, Satish V
Ukkusuri, and Marta C Gonza´lez. Spatiotempo
ral patterns of urban human mobility. Journa
of Statistical Physics, 151(1):304–318, 2013.

14] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean.
Distilling the knowledge in a neural network.
arXiv preprint arXiv:1503.02531, 2015.
15] Sirui Hong, Mingchen Zhuge, Jonathan Chen,
Xiawu Zheng, Yuheng Cheng, Jinlin Wang,
Ceyao Zhang, Zili Wang, Steven Ka Shing Yau,
Zijuan Lin, et al. Metagpt: Meta programming
for a multi-agent collaborative framework. In
The twelfth international conference on learning
representations, 2023.
16] Andreas Horni, Kai Nagel, and Kay W Axhausen. Introducing matsim. In Multi-Agent
Transport Simulation MATSim. Ubiquity Press,
2016.
17] John J Horton. Large language models as simulated economic agents: What can we learn from
homo silicus? Technical report, National Bureau
of Economic Research, 2023.
18] Na Jiang, Andrew T Crooks, Hamdi Kavak,
Annetta Burger, and William G Kennedy. A
method to create a synthetic population with
social networks for geographically-explicit agentbased models. Computational Urban Science,
2(1):7, 2022.
19] Carlos E Jimenez, John Yang, Alexander Wettig,
Shunyu Yao, Kexin Pei, Ofir Press, and Karthik
Narasimhan. Swe-bench: Can language models
resolve real-world github issues? arXiv preprint
arXiv:2310.06770, 2023.
20] Chenlu Ju, Jiaxin Liu, Shobhit Sinha, Hao Xue,
and Flora Salim. Trajllm: A modular llmenhanced agent-based framework for realistic human trajectory simulation. In Companion Proceedings of the ACM on Web Conference 2025,
pages 2847–2850, 2025.
21] Takehiro Kashiyama, Yanbo Pang, Yuya
Shibuya, Takahiro Yabe, and Yoshihide Sekimoto. Nationwide synthetic human mobility
dataset construction from limited travel surveys and open data. Computer-Aided Civil
and Infrastructure Engineering, 39(21):3337–
3353, 2024.
22] Daniel Krajzewicz, Jakob Erdmann, Michael
Behrisch, Laura Bieker, et al. Recent development and applications of sumo-simulation of urban mobility. International journal on advances
in systems and measurements, 5(3&4):128–138,
2012.

[23] David Lazer, Alex Pentland, Lada Adamic
Sinan Aral, Albert-L´aszl´o Barab´asi, Devon
Brewer, Nicholas Christakis, Noshir Contractor
James Fowler, Myron Gutmann, et al. Compu
tational social science. Science, 323(5915):721–
723, 2009.
[24] Xuchuan Li, Fei Huang, Jianrong Lv, Zhix
iong Xiao, Guolong Li, and Yang Yue. Be
more real: Travel diary generation using llm
agents and individual profiles. arXiv preprin
arXiv:2407.18932, 2024.
[25] Sung Yoo Lim, Hyunsoo Yun, Prateek Bansal
Dong-Kyu Kim, and Eui-Jin Kim. A large lan
guage model for feasible and diverse popula
tion synthesis. arXiv preprint arXiv:2505.04196
2025.
[26] Qi Liu, Can Li, and Wanjing Ma. Gatsim: Ur
ban mobility simulation with generative agents
arXiv preprint arXiv:2506.23306, 2025.
[27] Tianming Liu, Jirong Yang, and Yafeng Yin
Toward llm-agent-based modeling of transporta
tion systems: A conceptual framework. Artificia
Intelligence for Transportation, 1:100001, 2025.
[28] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu
Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang
Ding, Kaiwen Men, Kejuan Yang, et al. Agent
bench: Evaluating llms as agents. arXiv preprin
arXiv:2308.03688, 2023.
[29] Sean Luke, Claudio Cioffi-Revilla, Liviu Panait
Keith Sullivan, and Gabriel Balan. Mason: A
multiagent simulation environment. Simulation
81(7):517–527, 2005.
[30] Haoxuan Ma, Xishun Liao, Yifan Liu, Qinhua
Jiang, Chris Stanford, Shangqing Cao, and Jiaq
Ma. Learning universal human mobility pattern
with a foundation model for cross-domain data
fusion. Transportation Research Part C: Emerg
ing Technologies, 180:105311, 2025.
[31] Luca Pappalardo and Filippo Simini. Data
driven generation of spatio-temporal routines in
human mobility. Data Mining and Knowledge
Discovery, 32(3):787–829, 2018.
[32] Joon Sung Park, Joseph O’Brien, Carrie Jun
Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein. Generative agents: Interac
tive simulacra of human behavior. In Proceeding
of the 36th annual acm symposium on user inter
face software and technology, pages 1–22, 2023.

33] Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li,
Junbo Yan, Xiaochong Lan, Zhihong Lu, Zhiheng Zheng, Jing Yi Wang, Di Zhou, et al.
Agentsociety: Large-scale simulation of llmdriven generative agents advances understanding
of human behaviors and society. arXiv preprint
arXiv:2502.08691, 2025.
34] Timo Schick, Jane Dwivedi-Yu, Roberto Dess`ı,
Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and
Thomas Scialom. Toolformer: Language models can teach themselves to use tools. Advances in Neural Information Processing Systems, 36:68539–68551, 2023.
35] Patrick Taillandier, Benoit Gaudou, Arnaud
Grignard, Quang-Nghi Huynh, Nicolas Marilleau, Philippe Caillou, Damien Philippon, and
Alexis Drogoul. Building, composing and experimenting complex spatial models with the gama
platform. GeoInformatica, 23(2):299–322, 2019.
36] Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya Pathak, Nino Vieillard, Ramona
Merhej, Sarah Perrin, Tatiana Matejovicova,
Alexandre Ram´e, Morgane Rivi`ere, et al.
Gemma 3 technical report. arXiv preprint
arXiv:2503.19786, 2025.
37] Seth Tisue, Uri Wilensky, et al. Netlogo: A simple environment for modeling complexity. In International conference on complex systems, volume 21, pages 16–21. Boston, MA, 2004.
38] Jiawei Wang, Renhe Jiang, Chuang Yang,
Zengqing Wu, Makoto Onizuka, Ryosuke
Shibasaki, Noboru Koshizuka, and Chuan Xiao.
Large language models as urban residents: An
llm agent framework for personal mobility generation. Advances in Neural Information Processing Systems, 37:124547–124574, 2024.
39] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He,
Yiwen Ding, Boyang Hong, Ming Zhang, Junzhe
Wang, Senjie Jin, Enyu Zhou, et al. The rise and
potential of large language model based agents:
A survey. Science China Information Sciences,
68(2):121101, 2025.
40] Takahiro Yabe, Kota Tsubouchi, Toru Shimizu,
Yoshihide Sekimoto, Kaoru Sezaki, Esteban
Moro, and Alex Pentland. Yjmob100k: Cityscale and longitudinal dataset of anonymized
human mobility trajectories. Scientific Data,
11(1):397, 2024.

[41] Yuwei Yan, Qingbin Zeng, Zhiheng Zheng
Jingzhe Yuan, Jie Feng, Jun Zhang, Fengli Xu
and Yong Li. Opencity: A scalable platform
to simulate urban activities with massive llm
agents. arXiv preprint arXiv:2410.21286, 2024.
[42] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du
Izhak Shafran, Karthik R Narasimhan, and
Yuan Cao. React: Synergizing reasoning and
acting in language models. In The eleventh inter
national conference on learning representations
2022.
[43] Xiaotong Ye, Nicolas Bougie, Toshihiko Ya
masaki, and Narimasa Watanabe. Mo
bilecity: An efficient framework for large-scale
urban behavior simulation. arXiv preprin
arXiv:2504.16946, 2025.
[44] Lan Zhang, Yuxuan Hu, Weihua Li, Quan Bai
and Parma Nand. Llm-aidsim: Llm-enhanced
agent-based influence diffusion simulation in so
cial networks. Systems, 13(1):29, 2025.
[45] Xinnong Zhang, Jiayu Lin, Xinyi Mou, Shiyue
Yang, Xiawei Liu, Libo Sun, Hanjia Lyu, Yihang
Yang, Weihong Qi, Yue Chen, et al. Socioverse
A world model for social simulation powered by
llm agents and a pool of 10 million real-world
users. arXiv preprint arXiv:2504.10157, 2025.
[46] Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhu
Zhou, Robert Lo, Abishek Sridhar, Xiany
Cheng, Tianyue Ou, Yonatan Bisk, Daniel Fried
et al. Webarena: A realistic web environmen
for building autonomous agents. arXiv preprin
arXiv:2307.13854, 2023.
A Supplementary Materials
A.1 Additional Figures
A.2 Data Sources

Figure A1: Census data summary showing agegender-occupation distributions across the finestesolution census units (level 2 + level 4) in Higashihioshima. The tabulations are used as a reference
or evaluating demographic accuracy of the synthetic
population.
Figure A2: School enrollment distribution across 85
chools in Higashihiroshima, showing the number of
tudents assigned to each educational level. The disribution is consistent with official enrollment statisics.

Table 3: Data sources used to instantiate and validate GenWorld in Higashihiroshima. Access column
indicates availability: Open = publicly available for automatic download; Reg = requires free registration;
NR = non-redistributable (requires user to obtain from original source).
Data Type Source Access Description
Census Data e-Stat Open Age-gender, household, occupation statistics (198 census
units)
Time Use Survey e-Stat Open National time-use survey tabulations for activity distributions
Admin Bound- e-Stat Open Census tract boundaries for spatial aggregation
aries
Buildings OpenStreetMap Open Building footprints with height and area (45,000+ buildings)
POI Data OpenStreetMap Open Points of interest (57,000 POIs)
Manufacturing Hiroshima High- NR Company locations and employee counts (215 facilities)
POIs Tech Assoc.
Land Use Hiroshima Reg Parcel-level land use classification
DoBOX
Elevation GSI FGD Reg 1m-mesh digital elevation model
DEM1A
Road Network OpenStreetMap Open Road network with hierarchy (15,861 nodes)
School Districts e-Stat Open School district boundaries (85 schools)
Mobile Phone YJMob100K [40] NR Aggregated commuting patterns for validation
Data
Figure A3: Example of YJMob100K data showing aggregated commuting flows after registering the
Figure A4: Commute distance distribution comparianonymized mesh grid to our Higashihiroshima study
son between the synthetic population and YJM data,
area. The data provides mesh-level origin-destination
used as a diagnostic for commuting-distance scale.
patterns derived from anonymized mobile phone GPS
trajectories, and is used as an external mobility reference.
23

(b) Interactive building-level map view for inspecting the instantiated urban world (e.g., land use and
assigned households). Residential buildings are ren-
(a) Simulation dashboard and real-time activity dered in red with color intensity proportional to resstatistics in the Streamlit-based UI. ident counts (darker indicates more residents).
Figure A5: Platform UI screenshots of GenWorld, implemented with Streamlit for interactive inspection and
monitoring of the simulation and instantiated urban world.
Figure A6: Weekday spatial heatmaps for three representative activity types (shopping, socializing, and
childcare) at five time windows. Each row corresponds to an activity type and each column corresponds to
a time window; color intensity indicates higher occupancy.
24

A.3 Intention and Activity-Type Taxonomy
Activity Type Vocabulary We use a small,
discrete activity-template vocabulary (configured in
data_prepare/step4_activity/bins_activity_
preference.json) in our reference instantiation:
sleep_rest, work_task, study_class, daily_shopping,
(cid:44)→ personal_service, solo_meal, social_meal,
(cid:44)→ medical_care, admin_errand, social_visit,
(cid:44)→ entertainment_activity, structured_exercise,
(cid:44)→ casual_walk, outdoor_leisure
Distillation Candidate Sets The same
configuration file specifies the intention set
I = {home, duty, leisure, maintenance},
weekday/weekend intention-chain candidates (with_duty_intention_chain and
without_duty_intention_chain), and the
legal mappings activity→intention and
activity→landuse. These candidate sets define the finite action space used by offline distillation
and simulation-time lookup.
25

Table 4: Reference intention set and allowed activ
z ∈ I, the teacher scores the predefined candidate
categorical distribution for simulation-time sampling
Intention z Semantics A
home Stay at residence / rest s
duty Obligations (work/school) w
maintenance Daily necessities and errands d
e
leisure Discretionary activities s
a
l
A.4 Distillation Prompt Templates
Below are representative prompt templates for offline
distillation. Each query type uses a fixed template
that includes resident profile fields and outputs struc
tured JSON scores.
Chain Scores Prompt
Role-play as a resident and score behavior preferences
Resident: age_bin=<age>, occupation=<occ>
Scenario: typical <day_type>
Candidates: [<chain_1>, <chain_2>, ...]
(H=home, D=duty, L=leisure, M=maintenance)
Task: Score each chain [0-10]. Output JSON only:
{"scores": {"<chain_1>": 5, "<chain_2>": 5}}
Activity Scores Prompt
Role-play as a resident and score activity preferences
Resident: age_bin=<age>, occupation=<occ>
Scenario: pursuing intention='<intention>'
Candidates: [<activity_1>, <activity_2>, ...]
Task: Score each activity [0-10]. Output JSON only:
{"scores": {"<activity_1>": 5, "<activity_2>": 5}}
Full templates and configuration
files are available in the repository a
data prepare/step4 activity/.
A.5 LLM Interface Schema
This section provides detailed repeatability note
for the LLM-ready interface, including discretization
bins, activity–landuse mappings, and missing value
handling.
Context Discretization Bins Agent context i
discretized into coarse bins to enable efficient lookup
table compilation:

types used in our instantiation. For each intention
A and we normalize the aggregated scores into a
z
wed activity types A
z
p_rest
_task,study_class
y_shopping,personal_service,medical_care,admin_
nd
_meal,social_meal,social_visit,entertainment_
vity,structured_exercise,casual_walk,outdoor_
ure
• Age bins (3 categories): child (0–17), adult
(18–64), elderly (65+)
• Occupation bins (9 categories):
agriculture worker, industrial worker,
service worker, office worker,
professional, public sector, self employed,
non employed, college student
• Day type (2 categories): weekday, weekend
Activity–Intention Mapping Each activity type
maps to exactly one intention category:
Activity Intention
sleep rest home
work task, study class duty
daily shopping, maint.
personal service,
medical care, admin errand
solo meal, social meal, leisure
social visit,
entertainment activity,
structured exercise,
casual walk, outdoor leisure
Activity–Landuse Mapping Each activity
ype is constrained to specific landuse categories
abbreviations: C=commercial, I=industrial,
P=public facility, T=transport, O=open space,
R=residential, A=agriculture, N=nature):
Activity Landuse
sleep rest R
work task C, I, P, T, O, A
study class P
daily shopping, personal service C
medical care, admin errand P
solo meal C, P, T, O
social meal, entertainment C, O
social visit R, O
structured exercise O, P
casual walk O, road
outdoor leisure O, N

Missing Value Handling When agent attributes 1. Coarse-bin fallback: Map the unseen key
are incomplete, the following defaults apply: to a coarser bin (e.g., specific occupation →
non employed)
• Missing occupation: Mapped to
non employed bin 2. Default distribution: If no matching compiled
distribution exists, use a uniform distribution
• Missing age: Mapped to adult bin (modal cat- over the candidate action set
egory)
In practice, our discretization yields 3 × 9 × 2 = 54
• Missing home location: Agent excluded unique context keys for activity preference queries,
from spatial activity generation; flagged as which are enumerated during offline compilation.
no location
• No valid POI for activity: Fallback to nearest POI of any compatible landuse type; if none
available within search radius, activity skipped
The complete schema files are
available in the repository at
data prepare/step4 activity/bins *.json.
A.6 Distillation Setup
We perform offline distillation by repeatedly querying
a teacher model under identical discretized context
keys s (Section 4) and estimating empirical action distributions for each decision query type. Prompt templates used for distillation are listed in Appendix A.4.
Sampling Hyperparameters In our reference instantiation, we use the following configuration:
• Repetitions per context key (K): 10 samples
per unique (age bin, occupation bin, day type)
tuple
• Teacher model: Gemma 3 27B [36] served locally via Ollama
• Temperature: 0.7 for score generation (enabling diverse but coherent responses)
• Sampling: No adaptive sampling; uniform K
across all context keys
Hardware Distillation was performed on a workstation equipped with an RTX 4090 GPU (24GB
VRAM), 96GB RAM, and an Intel Core i5-14600K
CPU. The teacher model was queried through
AgentScope [10].
Unseen Key Handling At simulation time, if a
context key s was not encountered during distillation
(due to rare demographic combinations), we apply a
fallback strategy:
27
