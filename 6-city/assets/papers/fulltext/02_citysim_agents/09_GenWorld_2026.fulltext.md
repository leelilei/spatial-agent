# Extracted fulltext (pdfplumber)

Source: https://arxiv.org/abs/2606.27650
<!-- page 1 -->

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
1.1 Grounded and Scalable LLM-
LLM-agent simulation faces a joint grounding and
Agent Simulation
scaling problem: agents should act in environments
that reflect real urban constraints, yet direct online
Large Language Models (LLMs) have motivated a
LLMcallsforcity-scalepopulationsarecomputation-
new generation of agent simulations in which agents
ally prohibitive. We present GenWorld, an empir-
can use language-like observations, reason over con-
ically grounded urban simulation infrastructure that
text, and emit structured decisions [32, 39, 42, 15].
combines a building-level synthetic city, a structured
For urban research, this direction is attractive be-
agent–environment interface, and offline compilation
causecitiesarespatiallyconstrained, sociallyhetero-
of LLM-derived decision signals into lookup policies
geneous, and temporally dynamic. A useful urban
for scalable rollout. In a reference instantiation for
agentenvironmentshouldthereforeexposemorethan
Higashihiroshima,Japan,GenWorldgrounds196,608
a list of points of interest: it should ground agents in
syntheticresidentsincensusandgeospatialdata,val-
realistic homes, schools, workplaces, activity oppor-
idates demographic consistency against census tabu-
tunities,infrastructure,anddemographicheterogene-
lations, and uses YJMob100K mobile-phone data as
ity.
a commuting-distance diagnostic. We demonstrate
At the same time, city-scale LLM-agent simula-
the infrastructure through three reproducible cases:
tion faces a joint grounding–scaling problem. On the
a full-city weekday rollout, a weekday–weekend be-
grounding side, agents should operate under empiri-
havioral contrast, and a warning-response perturba-
calurbanconstraintsratherthaninabstracttexten-
tion with auditable replanning traces. These cases
vironments or coarse POI lists. On the scaling side,
support GenWorld as a reproducible platform for
directly querying an LLM for every decision of ev-
grounded and scalable LLM-agent studies, while cal-
ery agent is impractical for hundreds of thousands
ibrated forecasting for traffic, evacuation, or policy
of residents and many decision points per day. For
outcomes remains future work.Project page: https:
example, 200,000 agents over a 24-hour day with 15-
//genworld1993.netlify.app/.
minute decision intervals would require 19.2 million
Keywords: LLM agents, Urban simulation infras- online LLM calls if every decision were delegated to
tructure,Syntheticpopulation,Building-levelassign- a teacher model. This scale mismatch motivates the
ment, Multi-agent systems, Policy compilation, Em- central question of this paper:
pirical validation
How can LLM-agent simulations be
grounded in real urban constraints
∗Correspondingauthor: taofeng@hiroshima-u.ac.jp and scaled to city-level populations
1
6202
nuJ
62
]AM.sc[
1v05672.6062:viXra

<!-- page 2 -->

Figure 1: Multi-scale spatial granularity of GenWorld’s empirically grounded urban world in Higashihi-
roshima,Hiroshima,Japan. (A)City-levelviewshowing196,608individualsdistributedacrossgeoreferenced
buildings, validated against census data. (B) District-level view near Hiroshima University, revealing di-
versebuildingtypes(residential,commercial,educational)withtopographiccontextandelevationdata. (C)
Building-levelviewofaYoumeTownsupermarketareawith47employeesspatiallyassignedtoacorrespond-
ing commercial land-use parcel; residential buildings are rendered in red with color intensity proportional to
resident counts (darker indicates more residents). (D) Individual-level details showing employee household
origins, occupations, commuting distances, and residential neighborhoods (cho/town). This fine-grained
spatial allocation supports environment-aware agent simulation, which is typically difficult to capture in
TAZ-based or POI-list approaches.
without online LLM calls for every 1.2 Why Urban Grounding Matters
agent decision?
Urban environments are demanding testbeds for
agent simulation. Physical distance and infrastruc-
ture topology shape feasible actions; schools, work-
We answer this question with GenWorld, an em- places, and services create institutional constraints;
piricallygroundedurbansimulationinfrastructurefor households and neighborhoods create social and spa-
scalable LLM-agent studies. The key design is a sys- tial context; and individual routines aggregate into
tem chain rather than a single isolated algorithm: a city-levelpatterns. Thesecharacteristicsmakeurban
building-level synthetic urban world provides realis- simulationwellsuitedforstudyingsituatedagentbe-
tic constraints; a structured agent–environment in- havior, butonlyiftheenvironmentitselfisgrounded
terface makes LLM-style decisions executable, vali- in realistic population and spatial structure.
datable, and traceable; and offline compilation shifts RecentLLM-agentenvironmentsoftenfallshorton
LLM-derived decision signals out of the simulation this point. Abstract text-based benchmarks support
loop into lightweight lookup policies. controlled reasoning tasks but lack real spatial con-
2

<!-- page 3 -->

straints[28]. POI-basedurbansimulationsandlarge- validation targets, while geospatial sources pro-
scale agent platforms [32, 33, 38] have made progress vide buildings, land use, POIs, roads, elevation,
inagentcognitionandinteraction,buttheyoftenrely schools, and workplaces. We validate census
oncoarsespatialunits,POIlists,orweaklyvalidated consistency and use anonymized YJMob100K
population foundations. For city-scale urban stud- mobile-phonedata[40]asacommuting-distance
ies, such abstractions make it difficult to represent diagnostic.
building-level exposure, home–work–school anchor-
2. Structured agent interface and trace con-
ing, commute-distance structure, and land-use fea-
tract. We define a query-conditioned interface
sibility.
inwhichrawcityandpersonastatesaremapped
GenWorld therefore treats synthetic population
into binned observations, actions are selected
and spatial assignment as a grounding layer. We
from finite candidate sets, outputs are JSON-
use established population synthesis and spatial
validated, and execution traces are recorded in
allocation techniques, including census-constrained
machine-readable form. This contract makes
synthesis, building-level household placement, and
LLM-style decisions executable in a simulator
school/workplace assignment. The contribution is
and suitable for later analysis or policy compila-
not IPF in isolation. Rather, the contribution is in-
tion.
tegrating these standard ingredients into an LLM-
ready urban world that can be used by structured
3. Offline policy compilation for city-scale
agent policies and reproduced through documented
rollout. We compile repeated teacher-model
data-preparation stages.
responses under discretized context keys into
simulation-time lookup policies. This shifts ex-
1.3 Why Offline Compilation Matters pensive LLM calls out of the rollout loop and
enables city-scale execution through lightweight
LLM-agent behavior also raises a scalability prob-
sampling over validated action candidates.
lem. Online LLM inference can be useful for small
numbersofagentsordiagnostictraces, butcity-scale 4. Reproducible evaluation cases. We evalu-
rollout requires a different execution model. Gen- ate GenWorld through three cases: a full-city
World separates teacher inference from simulation- weekday baseline, a weekday–weekend behav-
time execution. A teacher LLM is queried offline ioral contrast, and a warning-response pertur-
under discretized context keys and finite candidate bation. These cases demonstrate city-scale roll-
sets; the resulting score distributions are compiled out,controlledtemporal-regimechanges,andau-
intolookuppolicies;andsimulation-timeagentssam- ditable replanning under an exogenous event.
plefromthesecompiledpolicieswhileusingthesame They are infrastructure diagnostics rather than
validators and deterministic execution semantics. calibratedforecastsoftraffic,evacuation,orpol-
Thisdesigntradesopen-endedonlinereasoningfor icy outcomes.
tractable, auditable rollout. It should be understood
as compiled stochastic policy execution rather than
1.5 Paper Organization
as fully adaptive online LLM reasoning. The benefit
isthateverysimulatedactionremainstiedtoastruc- Section 2 reviews related work in LLM-agent simu-
turedinterface,afinitecandidateset,andatraceable lation,urbansimulationplatforms,syntheticpopula-
context key, enabling large-scale execution and post- tiongeneration, anddistillationforagentsimulation.
hoc analysis. Section 3 presents the structured agent interface and
tracecontract. Section4describesofflinepolicycom-
1.4 Contributions pilationforscalablerollout. Section5detailstheem-
pirically grounded urban world construction and val-
This paper presents GenWorld as a reproducible in- idation. Section 6 presents the platform architecture
frastructure for grounded and scalable LLM-agent and simulation engine. Section 7 reports the evalua-
simulation. Thecontributionsareorganizedasacon- tion cases and scalability analysis. Sections 8 and 9
nected system: discuss limitations and conclude.
1. Empirically grounded urban world for
LLM-agent simulation. We instantiate a 2 Related Work
building-levelurbanworldforHigashihiroshima,
Japan, with 196,608 synthetic residents. Census Table 1 provides an overview of how GenWorld com-
tabulationsprovidedemographicconstraintsand pares to existing platforms across three categories:
3

<!-- page 4 -->

LLM agent simulation platforms, LLM-based urban reasoning patterns, achieving 600× acceleration in
mobility platforms, and population synthesis plat- simulation time; however, it focuses on prompt-level
forms. We detail these comparisons in the following efficiency rather than building-level spatial ground-
subsections. ing. Overall, these efforts primarily emphasize indi-
vidualtrajectorygenerationorengineeringefficiency.
They often do not provide city-scale population syn-
2.1 LLM Agents and Simulation Plat-
thesiswithjointlyvalidateddemographicsandspatial
forms
assignments (e.g., building-level placement) or thor-
TheemergenceofLargeLanguageModelshasdriven ough empirical validation.
rapid progress in autonomous agent systems. Recent Existing platforms often do not jointly provide
worksdemonstrateLLMagentsacrossarangeofset- realistic population foundations supported by em-
tings, from social simulation [32] to tool use [34] and pirical data, spatial complexity with infrastructure
multi-agent collaboration [15]. This progress moti- constraints, computational scalability to city-scale
vates the need for realistic simulation environments (100,000+ agents), and LLM-compatible interfaces.
that can support LLM agent research under real- GenWorld provides an empirically grounded urban
world constraints. environment with 200,000-agent scalability based on
Existing Agent Platforms. Existing platforms data from Higashihiroshima, Hiroshima, Japan.
and benchmarks span multiple levels of realism.
Abstract environments (e.g.,
GridWorld/TextWorld-style tasks) [28] are use-
ful for isolating reasoning and planning, but they 2.2 Urban Simulation Platforms
abstract away geography, resource constraints, and
social interactions.
Agent-basedmodelinghasarichhistoryinurbanand
Task-specificplatformssuchasSWE-bench[19]
transportation research [6, 23], with several estab-
(software engineering) and WebArena [46] (web nav-
lished platforms:
igation)providegroundedobjectivesandmeasurable
success criteria, but they typically focus on single- TraditionalABMPlatforms. GAMA[35],MA-
agent, non-spatial settings. SON [29], and NetLogo [37] are widely used for
Social simulation platforms such as Genera- urban simulation. These platforms provide powerful
tive Agents [32] explore emergent interactions, yet modeling capabilities but were designed for domain
the environments are simplified and the scale (e.g., experts rather than AI researchers, and they do not
25 agents) is insufficient for studying city-scale phe- provide standardized LLM integration interfaces or
nomenaandcomputationalscalability. CityBench[8] natural language observation spaces.
evaluatesLLMworld-modelingcapabilitiesforurban
Transportation SimulationTools. MATSim[16],
tasks but does not provide building-level population
SUMO [22], and similar tools focus on traffic simu-
grounding.
lation with detailed traffic modeling. However, they
LLM Agents in Transportation and Mobil-
typicallyusesimplifiedbehavioralmodelsanddonot
ity. Beyond interactive simulacra, LLMs have
incorporate the cognitive realism enabled by LLM-
been explored as simulated economic agents [17]
driven agents.
and integrated into mobility and transportation set-
Commercial Platforms. AnyLogic, Citilabs, and
tings. LLMob[38]usesself-consistencyandretrieval-
other commercial tools offer sophisticated urban
augmented strategies for individual mobility genera-
modeling but are closed-source, expensive, and not
tionwithGPS-basedvalidation. Liuetal.[27]outline
designed for AI research integration.
anLLM-agent-basedtransportationmodelingframe-
work with a small proof-of-concept. TrajLLM [20] Recent open-source efforts such as VoxCity [9]
combinesLLM-basedpersonagenerationwithhybrid provide seamless 3D urban environment generation,
destination choice (LLM + physical models), but fo- while Biljecki and Chow [3] establish global building
cuses on POI-level trajectories. GATSim [26] and morphology indicators for standardized urban anal-
MobileCity [43] target larger-scale mobility simula- ysis. However, existing platforms were not designed
tion; MobileCity achieves efficiency partly by dis- with LLM agents in mind. GenWorld aims to ad-
abling LLM modules at scale, trading behavioral fi- dressthesegapsbyprovidingnaturallanguageobser-
delity for speed. OpenCity [41] proposes a “group- vation spaces, flexible actionspecifications, validated
and-distill” prompt optimization strategy that clus- population foundations, and computational scalabil-
ters agents with similar attributes and distills shared ity through knowledge distillation.
4

<!-- page 5 -->

Table 1: Comparison of GenWorld with Related Platforms
Platform Population Empirical Scale Real Spatial Social
Realism Validation (Agents) Geography Detail Networks
LLM Agent Simulation Platforms
GridWorld/TextWorld Low No <100 No No No
Generative Agents [32] Low No <100 No Limited Limited
WebArena [46] N/A N/A Individual No No No
LLM-Based Urban Mobility Platforms
LLM-ABM Framework [27] Low No <100 No Low No
LLMob [38] Medium GPS Individual Yes POI-level No
TrajLLM [20] Medium Qualitative <100 No POI-level No
MobAgent [24] Medium Survey Individual Yes POI-level No
GATSim [26] Medium No 1K–10K No Medium Limited
MobileCity [43] Medium No 1K–10K No Medium Limited
OpenCity [41] Low GPS 1K–10K Yes POI-level No
Population Synthesis Platforms
Jiang et al. [18] High Census 100K+ Yes Road-based Multi-layer
Pseudo-PFLOW [21] High Census 100K+ Yes Building No
GenWorld (Ours) High Multi-source 100K+ Yes Building Multi-layer†
† Socialnetworksaregeneratedfromspatialco-locationbutnotusedincurrentexperiments.
2.3 Synthetic Population Generation is important for spatial realism. Common ap-
proaches include: gravity models [1] for work-
Generating realistic synthetic populations is funda-
place assignment, distance-based allocation for
mental to valid agent-based modeling [25].
household placement, and constraint satisfaction
Population Synthesis Methods. Iterative Pro- for student-to-school assignment. Jiang et al. [18]
portional Fitting (IPF) [5] and its variants are developed a large-scale method generating 23 mil-
commonly used methods, adjusting cell weights to lion geographically-explicit individuals for New York
match marginal distributions from census data. Be- Metro Area with multi-layer social networks (house-
yondIPF,priorworkalsoexploresalternativeformu- hold, work, school, daycare) emergent from spatial
lations such as combinatorial optimization, Bayesian co-location,highlightingtheimportanceofsocialnet-
approaches, and deep generative models (DGMs). works for urban simulations. Kashiyama et al. [21]
While DGMs can generate diverse populations be- developed Pseudo-PFLOW, an agent-based frame-
yondobservedsamples,theyoftenstruggletobalance work that downscales census data to building-level
sampling zeros (valid but unobserved combinations) assignments using Markov chain models for activ-
withstructuralzeros (implausiblecombinations)[25]. ity generation, covering Japan’s 130 million pop-
Recent work explores LLM-based approaches: Li et ulation. While achieving strong validation results
al. [24] proposed MobAgent, using LLMs to extract (R2=0.61–0.98forpopulationdistribution),theseap-
fine-grained mobility patterns from individual pro- proaches rely on traditional statistical models rather
files through self-evaluation and recursive reasoning, than LLM-driven behavioral realism and lack inte-
validated on 0.2M travel surveys. Ma et al. [30] de- gration with modern LLM agent frameworks.
velopedafoundationmodelusingLLMsforsemantic
enrichmentofGPStrajectories,demonstratingtrans- Validation Approaches. Traditional validation
ferlearningacrossregions(LAtoEgypt)formobility relies primarily on census data comparison. Re-
pattern synthesis. While these LLM-based methods cent work has begun incorporating mobile phone
have been explored for individual trajectory genera- data [40] for validating commuting patterns, build-
tion,theyfocusonpersonalmobilitymodelingrather ing on foundational studies of human mobility pat-
than city-scale population synthesis with validated terns [11, 31, 13]. Ma et al. [30] demonstrated multi-
demographic distributions and spatial assignments. level validation through traffic simulation, achieving
Spatial Assignment and Social Networks. As- MAPE < 6% for traffic volumes. However, system-
signing synthetic individuals to geographic locations atic validation combining demographic distributions,
5

<!-- page 6 -->

spatial assignments, and mobility patterns against enabling large speedups in typical settings for large-
real-world data remains rare. scale simulations.
Most synthetic population studies focus on de- As summarized in Table 1, GenWorld com-
mographic accuracy but neglect spatial validation bines building-level population grounding with
with real mobility data, social network construction, census-validated demographics, city-scale scala-
daily activity schedules, and integration with LLM bility via offline knowledge distillation (200,000+
agentframeworks. GenWorldprovidesanend-to-end agents), multi-layer social networks derived from
pipeline that covers these aspects. spatial co-location, and schema-validated LLM-
readyinterfacesthatproducemachine-readablebe-
havioral traces in a real-city instantiation.
2.4 Knowledge Distillation for Agent
Simulation
3 Agent Interface
Knowledge distillation [14] has been widely applied
GenWorldexposesalightweightdecisioninterfacefor
in machine learning to compress large models into
LLM agents and records each decision as a struc-
efficient ones. Recent applications include:
tured log entry. This interface is designed to en-
Beyond model compression, recent work explores
able post-hoc qualitative inspection of agent rou-
abstraction and software architecture to scale LLM-
tinesandfailuremodesandprovidemachine-readable
agent simulations. Chopra et al. [4] introduce LLM
decision traces for offline distillation. Concretely,
archetypes, where many agents share an archetypal
each decision consumes a binned observation o˜
LLM policy to increase throughput at scale, but this i,t
and a finite candidate set A , and produces a
can reduce individual-level heterogeneity and online i,t
schema-conformant JSON action, a validator bit,
adaptivity. SocioVerse [45] targets population-scale
and (if needed) a deterministic fallback outcome, all
social simulation by aligning LLM agents to a large
recorded as a log entry.
pool of real users and standardizing simulation pro-
cedures; however, it relies on large external datasets
Observation and Action Schema At each de-
anditsalignmentpipelinecanbecostlytoreproduce
cision point for agent i at time t, the simulator con-
ortransfer. Forinfluencediffusioninsocialnetworks,
structsadecisioncontextfromthecitystatex (time,
LLM-AIDSim [44] integrates LLM-enhanced agents t
environment signals, and infrastructure states), a
into classical diffusion simulation pipelines, but the
synthesized persona u produced by the population
approach is task-specific and may not directly gen- i
instantiation pipeline (core demographics and spa-
eralize to open-ended urban decision spaces. From a
tial anchors such as home/work/school when avail-
systemsperspective, SALLMA[2]proposesalayered
able, with optional household and social features),
multi-agent architecture with orchestration and con-
and optionally short-term memory summaries m
tainerized deployment; while improving modularity i,t
distilled from recent logs. This context is denoted as
and scalability, it does not inherently remove per-
c = (x ,u ,m ). Given a decision query q , the
decision LLM inference costs and can require sub- i,t t i i,t t
environment deterministically produces a binned ob-
stantial engineering infrastructure.
servation and a finite candidate action set:
LLM Distillation. Distillinglargelanguagemodels
into smaller, faster models while maintaining perfor-
o˜ =ϕ(c ;q ),
i,t i,t t
mance is an active area of research. However, most
A =κ(q ,o˜ ).
work focuses on natural language tasks, not agent i,t t i,t
decision-making in complex environments. The function ϕ is implemented as a deterministic en-
Agent Behavior Cloning. Imitation learning and coder stack that includes coarse binning and query-
behavior cloning train efficient policies from expert specificformatting. Apromptcomposerg(o˜ ,q )as-
i,t t
demonstrations. GenWorldextendsthisparadigmby semblesastabletemplatewithquestion-specificslots.
using LLMs as ”expert demonstrators” to generate The agent then outputs a structured JSON action
training data for efficient student models. a ∈ A following a fixed schema (e.g., activity
i,t i,t
Weapplyknowledgedistillationtoenablecity-scale type). A deterministic validator v(o˜ ,a ) ∈ {0,1}
i,t i,t
LLM agent simulation. Our approach estimates the enforces schema and feasibility constraints; invalid
teacher’s discrete decision distribution via repeated actions trigger a deterministic safe fallback before
Monte Carlo sampling and compiles the resulting execution, and all artifacts are logged. Figure 2
probabilistic policy into efficient lookup tables, shift- illustrates a representative query where raw per-
ingexpensiveinferenceoutofthesimulationloopand sona/state fields are deterministically mapped into
6

<!-- page 7 -->

coarsebinsbeforebeingpassedtotheLLM.Figure3 Inbothcases,adeterministicreturn-homefallbackis
summarizeshowtheresultingstructuredoutputsare applied and the agent stays at home until the next
executed into full-day trajectories by lightweight de- plan sampling time (day-start or checkpoint). Sec-
terministic rules. In this implementation, persona tion 4 describes how decision traces are collected un-
slices are intentionally sparse, while richer prefer- der binned contexts and compiled into scalable stu-
ence/trait slices can be added as optional extensions dent policies.
ortreatedaslatentvariablesdependingonthetarget
application.
FormalContractSummary Theformalcontract
(Figure 2) is summarized as follows. The simulator
Two-Tier Decision Queries for Long-Horizon deterministically maps raw persona and state fields
Rollout Decision-making is separated into two into coarse bins via encoders b and b :
u x
structured outputs with different time scales.
ActivityPreference is a per-agent, persona- I ={home,duty,leisure,maintenance},
conditioned preference profile that is initialized once u˜ =b (u ), x˜ =b (x ),
i u i k x k
(and optionally refreshed) and defines propensities
τ ∈{weekday,weekend},
over activity types for each high-level intention.
C ⊆I∗.
DayPlan is a per-day (or per-checkpoint) plan that τ
specifiesasmallmixtureofintention-chaintemplates
where τ is a coarse day-type label and C is a small
together with discretized POI-selection weights. The τ
predefinedcandidatesetofintention-chaintemplates.
plan sampling index is denoted by k (day-start or
Theper-agentquerydefinesaconditionalcategorical
checkpoint), which is much sparser than the simu-
distribution over activity types given intention z:
lator time step t used for execution, and the city
state at plan sampling time is written as x . The
k A (z):=ActivityPreference (z),
intention space is fixed to {home, duty, leisure, i i
maintenance}. A i (z)={(a,p(a|z))} a∈Az , z ∈I,
This two-tier abstraction is grounded in time- (cid:88)
a∈A , p(a|z)=1,
z
geography theory [12]: daily mobility is con-
a∈Az
strained by capability (physical limits), coupling
(coordination with others), and authority (in- where A is a small predefined set of activity types
z
stitutional schedules). Our intention hierar- allowed under intention z (Appendix A.3). The per-
chy(home/duty/leisure/maintenance)capturesthese day (or per-checkpoint) query returns:
canonicalconstraintclasses,whiletheactivityvocab-
ulary covers the primary purposes observed in na- D i,k =DayPlan i,k (x˜ k ,u˜ i ,C τ ),
tional time-use surveys. The fixed ontology trades
D =(r ,C ,w ),
i,k i,k i,k i,k
open-ended expressiveness for tractability and re-
peatability; extending the vocabulary is straightfor- C i,k ={(c j ,π j )}| j C = τ 1 |,
ward within the same interface contract.
(cid:88)
|Cτ|
Critically, the day-level query is not conditioned r ∈{0,1}, π =1,
i,k j
on a single intention; instead, the simulator provides
j=1
a small, day-type-specific candidate set of intention- c ∈C ⊆I∗,
j τ
chain templates (e.g., weekday vs. weekend vari-
w (z)=(ℓnear(z),ℓpref(z),ℓcost(z)),
ants) and includes this candidate set as part of the i,k i,k i,k i,k
binned context. During rollout, agents sample a ℓ∗ (z)∈{0,...,10}, z ∈I,
i,k
DayPlan at day start, and the simulator consumes
it through a lightweight executor (as shown in Fig- where C is a small predefined candidate set
τ
ure 3) to produce an explicit trajectory of simu- of intention-chain templates (in our instantiation,
lator actions. Concretely, an intention-chain tem- |C | = 6 per day type). Here r is an override re-
τ i,k
plate is sampled from the day-type-specific candi- questflag,eachc isanintention-chaintemplate,and
j
date set, expanded into activity types by sampling w (z) specifiesdiscretized POI-selection weights for
i,k
ActivityPreference, and grounded into concrete intention z. Here k denotes the plan sampling index
destinationsviaafixedactivity-to-placeontologyand (day-startorcheckpoint),whichismuchsparserthan
feasibility checks. Overrides may be requested by theexecutiontimestep. Overridesmayalsobeforced
the agent or forced by the simulator when feasibility bythesimulatorwhenfeasibilitychecksfail;ineither
checks fail or exogenous events invalidate the plan. case, a deterministic return-home fallback is applied.
7

<!-- page 8 -->

Figure 2: Query-conditioned prompt construction for our structured decision interface. Raw persona/state
fieldsaredeterministicallymappedintocoarsebinsandarenotincludedverbatimintheprompt. Thefigure
schematically illustrates promptvariantsused in thisinstantiation: a per-agentActivityPreference query
overafixedcandidatesetunderagivenintention,andday-levelpromptsthatscorePOI-selectionpreferences
over near/pref/cost weights and intention-chain templates over a predefined chain candidate set. In this
default instantiation, POI-weight scoring and intention-chain scoring are issued jointly as a single DayPlan
query, but they can also be queried separately. Input features are represented using coarse discrete bins,
while candidate scores returned by the teacher are integers in [0,10] over a predefined option set. Section 4
describes how these structured traces are aggregated and compiled for scalable rollout.
schema, a discrete and bounded action space with
strict validation, and deterministic execution seman-
tics are enforced. At city scale, even rare formatting
or parsing failures can derail long simulations. LLM
decisionsarethereforeconstrainedtoasmalldiscrete
action set with a fixed schema, and strict validation
and deterministic fallback rules are enforced in the
decisionlogger. Thisdesignmakesdecisiontracesdi-
rectlymachine-readableandsuitablefordownstream
analysis and policy compilation (Section 4).
Figure 3: Plan-to-trajectory execution with a two-
tier decision structure. ActivityPreference pro-
4 Distillation and Scaling
videspersona-conditionedactivitypropensities,while
DayPlanspecifiesintention-chaintemplatesandPOI-
To scale LLM-driven decision-making to city-scale
selection weights. A lightweight executor produces
simulations, the teacher’s stochastic decision behav-
explicit trajectories through fixed ontologies and fea-
ior is distilled into empirical score vectors and sam-
sibility checks.
pling distributions under discretized contexts by re-
peatedly querying the LLM under identical context
keys and aggregating its scores over a fixed candi-
Tool-Oriented Interface, Robustness, and date set (e.g., intention-chain templates or intention-
Traceability The interface is realized as stable conditioned activity templates). Because the inter-
prompt templates with strict JSON schemas that facebinsrawcontextsintodiscretekeysandrestricts
are validated and logged by the simulator, and each query to a finite candidate set with strict val-
can be wrapped by standard tool-calling middleware idation, the teacher can be repeatedly queried un-
whenneeded. Afixed,query-conditionedobservation der identical keys and its scores can be aggregated.
8

<!-- page 9 -->

The key idea is to shift expensive inference out of query returns an integer score r(k)(a) ∈ [0,10] for
the simulation loop: a one-time offline cost is paid to every candidate a ∈ A . The mean score and con-
qt
estimate these distributions, and the resulting com- sistency statistics are aggregated:
piledtablesareexecutedviaamortizedconstant-time
lookup and sampling given bounded candidate sets 1 (cid:88) K
µ(a|s)= r(k)(a), (1)
per query, with respect to the number of agents and
K
decision steps. k=1
(cid:118)
In a micro-benchmark on the compiled (cid:117) K
(cid:117) (cid:88)(cid:0) (cid:1)2
ActivityPreference table, Python lookup achieves σ(a|s)=(cid:116)K−1 r(k)(a)−µ(a|s) . (2)
1.85M queries/s (0.54µs per query) over 200,000 k=1
randomizedcontextkeys. Whileabsolutethroughput
depends on hardware and implementation details, The aggregated mean scores are normalized across
this benchmark highlights the potential for large candidates into a categorical sampling distribution
speedups relative to online LLM inference in typical π(· | s), which is used for simulation-time sampling.
settings. End-to-end wall-clock time per simulator Since scores are in [0,10], an executable sampling
step also includes environment updates, routing, and distribution is constructed by normalizing the mean
execution overheads. Prompt templates used for scores:
distillation are listed in Appendix A.4.
π(a|s)=Normalize(µ(a|s)), a∈A . (3)
qt
Action Primitives and Context Discretiza-
The score variability σ(a | s) is reported to quantify
tion Repeated sampling requires that the teacher
teacher consistency across repeated queries (and to
be queried under identical contexts. Following the
diagnose context regions with high variability).
interface contract in Section 3, raw persona and
state are discretized into bins (e.g., u˜ = b (u ),
i u i
x˜ = b (x)) and each decision query q is treated Policy Compilation and Simulation-Time In-
x t
as defining its own finite action space. Concretely, ference The aggregated scores and sampling dis-
for each query type q (e.g., ActivityPreference tributions (e.g., µ(· | s) and π(· | s)) are compiled
t
or DayPlan), an executable discrete action set A intoper-querylookuptableskeyedbydiscretizedcon-
qt
is defined that matches the simulator’s structured text features (persona bins, time bins, coarse loca-
schema and validation rules. A finite context key tion types, scenario indicators, and day-type indica-
s = (u˜ ,x˜,q ,τ) is then formed, where τ indexes tors). Duringsimulation,agentssampleanintention-
i t
the day-type-specific candidate template set used by chain template or activity template according to the
DayPlan. This makes repeated offline teacher ag- distilled distribution rather than querying the LLM,
gregation well-defined and enables compilation into and execute the sampled schema through the same
amortized constant-time lookup policies. The day- validator/executor as the teacher outputs. Scoring
type indicator τ is included explicitly because the and sampling over intention-chain templates enables
DayPlan candidate set differs across day types (e.g., long-horizondiversitywhilekeepingtheexecutionin-
weekday vs. weekend). terface lightweight. This compilation separates two
concerns:
Computational Motivation At city scale, a di-
rect teacher-driven simulation requires O(NT) LLM • Teacher inference (offline): generate multi-
calls, where N is the number of agents and T is the ple samples per context to estimate µ(·|s) (and
number of decision points per simulated day. For ex- σ(·|s)), then derive π(·|s).
ample,N =200,000agentswith15-minutetimesteps
over 24 hours yields T =96 and thus 1.92×107 calls • Agent rollout (online): execute a lightweight
stochasticdecisionrulebytablelookupandsam-
for a single day, which is computationally expensive
pling.
in practice. Distillation reduces simulation-time in-
ference to amortized constant-time table lookup and
sampling with respect to the number of agents and Context Design and Coverage To make compi-
decision steps. lation feasible, contexts are discretized into a finite
key space (e.g., persona bins, coarse location types,
Repeated Teacher Query Aggregation For a and time bins) and representative contexts are sam-
fixed candidate set A and context key s, K teacher pled according to the instantiated population dis-
qt
score vectors {r(k)(·)}K are sampled, where each tribution. This allows the offline sampling budget
k=1
9

<!-- page 10 -->

Figure 4: Teacher preference scores (0–10) for ActivityPreference across persona categories (rows) and
candidate activity types (columns), shown separately for maintenance (left) and leisure (right). The scores
define the simulation-time sampling distribution used by the compiled policy.
(a) Weekday intention-chain template preference. (b) Weekend intention-chain template preference.
Figure 5: Distilled teacher scores for DayPlan intention-chain templates, shown separately for weekday and
weekend candidate sets.
to be allocated where it matters most while keep- road network with elevation, and anonymized mo-
ing simulation-time inference amortized constant- bility data for commuting diagnostics. These inputs
time with respect to the number of agents and de- provideconstraintsforpopulationsynthesisandspa-
cision steps. This discretization trades off fidelity for tial grounding, and also provide independent signals
tractability: behavior matching depends on context for validation.
keydesignandcoverage,andunseenkeysmayrequire Detaileddatasourcesandprocessingstepsarepro-
backingofftocoarserkeysoraconservativedefault. vided in Appendix A.2 (Table 3).
5 Empirical Grounding of the 5.1 Population and Environment
Foundation
Urban World
This section describes the empirically-grounded pop-
Our reference instantiation integrates multi-source ulation and environment foundation used in our Hi-
empirical datasets, including official census statistics gashihiroshima reference instantiation, grounded in
and administrative boundaries, building footprints publicly available census tabulations and geospatial
and POIs, parcel-level land-use labels, a complete layers (buildings, land use parcels, school districts,
10

<!-- page 11 -->

POIs, and roads), synthesizing 196,608 individuals Eq. (6)–(7) are realized via seeded sampling: an em-
across 89,988 private households, with 5,641 addi- ployed subset of size E′ is drawn and an occupation
t
tionalgroup-quarterrecordsretainedseparately. The multiset with counts C′ is assigned, followed by a
t,o
formulation combines demographic micro-synthesis tract-seeded random permutation.
under tract-level census constraints with spatial
grounding of home, school, and work locations un- 5.1.2 Spatial Grounding of Home, School,
der capacity and distance constraints. and Work
Households are assigned to residential buildings
5.1.1 Tract-Level Micro-Synthesis and At- within each tract using a capacity-aware alloca-
tribute Assignment tion; students are assigned to schools using dis-
trict polygons when available with nearest-school
Foreachtractt,thetotalpopulationN istreatedas
t fallback; university assignment uses a distance-
a hard constraint and an age–gender joint distribu-
based stochastic choice with weights proportional to
tion is estimated whose marginals match census age
1/d2. For workplace allocation, employed individ-
counts and gender totals. A 2D IPF procedure is
uals are mapped to landuse parcels (not building
adopted on an age×gender matrix M(t):
IDs) using an occupation-conditioned landuse prior
M a (k ,g + 2 1) =M a (k ,g )· (cid:80) n t M ,a (k) (4) ( g o e c th cu er pa w t i i t o h n→ am la a n x d i u m s u e m m c a o p m p m in u g te w -d it i h sta r n at c i e o c s o r n o s , t l ) ra t in o t -
g′ a,g′ d .
M a (k ,g +1) =M a (k ,g +1 2 ) · (cid:80) n t,g (k+1) (5) m C ax apacity inference by area (quotas). For occupa-
M 2 tion o, let total employees be N , eligible landuse
a′ a′,g o
categoriesbeL , andtheconfiguredlanduseratiobe
o
(cid:80)
where n is the census count of age bin a in r for l ∈L with r =1. For each landuse
t,a o,l o l∈Lo o,l
tract t, and n is the census total of gender g ∈ parcel j of category l with area A , an occupation-
t,g j
{male,female}. M(t) isinitializedwithastrictlypos- specific quota is defined:
itive prior (e.g., uniform or tract-independent) and
N r A
Eq. (5) is iterated until marginal errors fall below ϵ q = o o,l j , j ∈P , l∈L (8)
j,o (cid:80) A l o
or for a fixed number of rounds. Individuals are then k∈Pl k
sampled from the normalized joint distribution, and
where P is the set of parcels with landuse category
l
a concrete integer age is sampled uniformly within
l. Fractionalquotasareconvertedintointegercapac-
the selected age bin.
itiesqˆ (e.g.,viafloorwithremainderredistribution
j,o
Given the sampled individuals, households are
orstochasticrounding)topreservetotalcapacityper
formed using the tract household-size histogram
occupation.
(1,2,3,4,5,6+)withalightweightplausibilityheuristic
Gravity-based allocation. We employ a gravity
(e.g.,cappinghouseholdsizeat6). Thecensushouse-
model to assign workplaces, balancing employment
hold count target H is enforced and household sizes
t opportunities with distance decay. Let d be the
ij
are sampled to match the tract histogram. Employ-
haversine distance between employed individual i’s
ment status and occupation categories are then as-
home and landuse parcel j. The probability P of
ij
signed for working-age individuals so that tract-level
individual i choosing workplace j is proportional to
employed totals and occupational marginals match
theparcel’sdestinationattractiveness(capacity)and
the census. Let I be individuals in tract t, and
t inversely proportional to commute distance:
W ⊂ I be working-age individuals. Denote the
t t
census employed target as E and the census occu- P ∝Aα·f(d )·M (9)
t ij j ij ij
pation target counts as C for occupation category
t,o
where A is the capacity (attractiveness) of parcel
o ∈ O. Let E′ = min(E , |W |) and let C′ be ad- j
t t t t,o j, f(d) = d−β is the distance decay function with
justed occupation targets derived from {C } by
t,o o∈O
padding/truncation so that (cid:80) C′ = E′. The friction parameter β, and M ij is a binary mask en-
o∈O t,o t forcing occupation compatibility (M = 1 if parcel
following constraints are enforced: ij
j supports individual i’s occupation o and j has re-
i
(cid:88) mainingcapacity,else0). Wesetα=1andcalibrate
I[employed ]=E′ (6)
i t β againstempiricalmobilitydata. Theassignmentis
i∈Wt
performed stochastically:
(cid:88)
I[employed ∧occ =o]=C′ , ∀o∈O (7)
i i t,o
j∗ ∼Categorical({P } ) (10)
i∈Wt ij j
11

<!-- page 12 -->

This probabilistic approach allows for a realistic dis- 5.2 Activity Generation and Tempo-
tribution of commute distances, including long-tail ral Grounding
commutes, unlike strict distance minimization.
Weimplementahybridgenerativemechanismto
ensurebothbehavioralrealismandtemporalfidelity.
5.1.3 Derived Social Networks While the sequence and semantics of daily activ-
ities (e.g., the decision to visit a gym after work) are
Multi-layer networks are a deterministic byproduct
generatedbytheLLM-distilledpolicytocapturehet-
of the assigned home/school/work locations and in-
erogeneous preferences, the temporal attributes
stitutionalmembership. Whilenotusedbytheagent
(start time and duration) are grounded in the Na-
interfaceortheexperimentsinthispaper,theyarere-
tional Time Use Survey. Specifically, once an
tainedasanoptionalartifactforinternalconsistency
activity type is selected by the agent, its timing is
checks and future extensions:
sampled from the corresponding empirical distribu-
tion (e.g., ’Sports’ duration distribution for a ’Gym’
G=(V,E), (11) visit), thereby preventing unrealistic hallucinations
E =E ∪E ∪E ∪E common in pure LLM scheduling.
household home school work
∪E (12) We utilize the action initialization probabil-
neighborhood
ity(derivedfromactivitystart-timestatistics)rather
than the raw action participation rate (occu-
where edges represent interaction opportunities in-
pancy). Usingrawoccupancyratesassamplingprob-
ducedbysharedhouseholds,sharedresidentialbuild-
abilities—a common pitfall—would incorrectly bias
ings, shared schools, shared workplace landuse, and
the duration of activities. Our pipeline explicitly
neighborhood proximity. To keep graphs sparse at
separates the decision to start an activity from the
scale,degreesarecappedoredgesaresampledwithin
duration of the activity, ensuring that the generated
large buildings/institutions and edges can optionally
temporaldynamicsmathematicallyalignwiththeag-
be weighted by co-location frequency.
gregate census observations.
5.1.4 Urban Environment Integration
5.3 Population Distribution Valida-
The platform integrates multiple layers of urban in- tion
frastructure:
We validate our synthetic population against census
data at the tract level to ensure demographic accu-
E ={P,R,B,A} (13)
racy.
where:
5.3.1 Census Data Validation
• P: POI catalog with categorical attributes P =
{(p ,type ,capacity ,hours )} Our population synthesis method generates 196,608
i i i i
individuals across 89,988 private households in Hi-
• R: Road network graph R = (V ,E ,w ) with gashihiroshima, with 5,641 additional group-quarter
r r r
recordsretainedseparatelyfromprivate-homeassign-
edge weights (distance, speed, capacity)
ment. We validate the synthetic population against
2020 Japanese Census tabulations at census-tract
• B: Building set with spatial footprints and land
granularity across multiple demographic dimensions.
use B ={(b ,geom ,use ,C )}
i i i i For household size statistics, the census reports
general household counts, while some tracts include
• A: Administrativehierarchy(censusblocks, dis-
non-household residents (e.g., dormitories or institu-
tricts, city) for spatial aggregation
tional facilities). We therefore evaluate household
size distributions on tracts where total population
When explicit capacities, opening hours, or road-
equalsgeneral-householdpersons(seeAppendixAfor
capacity attributes are missing in the source layers,
details).
theimplementationusesconservativedefaultsorsim-
ple rule-based proxies (e.g., POI-type-specific heuris-
tics and road-class-based speed/capacity settings) to Distributional Fit Metrics We distinguish hard
support feasibility checks. constraints from soft-fit metrics. Tract-level total
12

<!-- page 13 -->

population is constrained to match census totals ex- than silently assigned through unconstrained fall-
actly, yielding very close agreement with census to- backrules;747school-agegroup-quarterresidentsare
tals by construction. We therefore emphasize distri- treatedasoutofscopeforprivatehome-basedschool
butionalsimilarityforvariablesnotenforcedasexact assignment. We report the assigned school enroll-
constraints. ment distribution in Figure A2.
After restricting census tabulations to the instan-
tiated study area, we obtain 198 finest-resolution
5.4 Mobility Pattern Validation
census units (HYOSYO=2/4). We evaluate de-
mographic fit on 185 tracts; 13 census units with We compare commuting statistics against
zero population and zero households (e.g., industrial anonymized mobile phone mobility data from
parks) are excluded. Gender ratios are well matched Yahoo Japan Mobility (YJMob100K) [40]. The
(male ratio MAE < 0.02). Age distributions achieve dataset discretizes location pings into 500m × 500m
meanL1=0.1229(median0.10,max0.31),meanKS grid cells and timestamps into 30-minute bins, with
= 0.0299 (max 0.12), and mean JS = 0.0047 (max the metropolitan area undisclosed for privacy. For
0.02), with 95% of tracts having L1 < 0.20. House- our case study, we extract a subregion consistent
hold size distributions achieve mean L1 = 0.0547, with the Higashihiroshima area by registering the
mean KS = 0.0269, and mean JS = 0.0075. Em- released mesh grid via manual rigid alignment. The
ployment counts (15+) show high tract-level agree- registration uses coastline landmarks and major
ment (R2 > 0.99). Occupation distributions achieve terrain features as control points, with an estimated
mean L1 = 0.1945, mean KS = 0.0972, and mean JS alignment error of <500m (one grid cell). A sen-
= 0.0382. The tight distribution of per-tract errors sitivity analysis indicates that commute distance
reflects the effectiveness of the IPF constraints. distributions are robust to registration errors within
this range. The extraction workflow is documented
in the repository at data_prepare/mobility_
5.3.2 Spatial Distribution Validation
validation/README.md, with comparison scripts
Unlike TAZ-based methods that assign residents to under data_prepare/mobility_validation/ and
abstract zones, our building-level approach assigns data_prepare/step3_assignment/work/; the
households to specific georeferenced buildings under comparison is treated as a commuting-distance
tract-level and capacity constraints. Because build- diagnostic rather than an OD-flow benchmark.
ingfootprintsandland-uselabelsmaybeincomplete We infer each user’s home mesh from nighttime
in a small number of tracts (e.g., industrial parks), records and work mesh from daytime records (fixed
wereportexplicitassignmentdiagnosticsratherthan timewindows),thenderiveacommutingdistancedis-
silently forcing fallback placements. tributioninthemeshspace. Figure6summarizesthe
In our reference instantiation, all 89,988 private extractedcommutingpatternsfortheselectedsubre-
census-target households are successfully assigned to gion.
residentialbuildings. The5,641unmappedhousehold The released validation artifact extracts 7,525
records are group-quarter records and are intention- YJM-derivedcommutersfromtheselectedsubregion,
ally excluded from private-home placement rather with a mean commute distance of 7.45 km, me-
than treated as failed residential assignments. dian of 5.00 km, and 90th percentile of 19.24 km.
Against this reference, the 90,744 synthetic workers
assigned to workplaces have a mean commute dis-
5.3.3 School Assignment Validation
tance of 10.81 km, median of 10.09 km, and 90th
Schoolassignmentusesbuilding-levelhomelocations. percentile of 19.15 km. The resulting KS distance is
Elementary and junior-high students are assigned by 0.359 (0.399 when restricted to commutes ≤20 km).
school-district polygons with nearest-school fallback. This diagnostic indicates that the current workplace
High-school assignment is nearest-school based with assignment captures the upper-tail scale but under-
limited randomness among candidates within a dis- representsveryshortcommutesandoverrepresents5–
tance threshold, and university assignment uses a 15 km trips. We therefore use YJM as a commuting-
gravity-style stochastic choice with weights propor- distance diagnostic and not as evidence of calibrated
tional to 1/d2. OD-flow prediction.
In our reference instantiation, 42,376 out of 42,584 Figure A4 compares the resulting distributions.
in-scope students are assigned to a school (99.51%). We treat this comparison as a commuting-distance
The remaining 208 in-scope records are flagged as diagnostic rather than a strict OD-flow correlation,
too far stay home by the diagnostic pipeline rather because the observed mesh space is anonymized and
13

<!-- page 14 -->

requires manual registration. Layer 1: Population and Environment Foun-
dation Instantiates the georeferenced urban world
and synthetic population under census constraints
and reports validation diagnostics; see Section 5.
Layer 2: Agent Decision Framework Ex-
poses a structured agent–environment interface with
binnedobservationsandfiniteJSON-validatedaction
candidates, enabling rule-based, teacher-LLM, and
distilled-student policies; see Sections 3 and 4.
Layer 3: Simulation Engine Orchestrates time-
steppedmulti-agentexecutionwithfeasibilitychecks,
system-level consistency updates, and detailed log-
ging; see Section 6.2.
Thefollowingsubsectionsdetailthesimulationen-
gine.
Figure 6: Commuting pattern extraction from YJ-
Mob100Kafterregisteringtheanonymizedmeshgrid
to our study area. The figure visualizes inferred 6.2 Simulation Engine
home/workpointsandcommutingdistancestatistics
The simulation engine orchestrates time-stepped
for the extracted subregion.
multi-agent execution, managing time progression,
spatial dynamics, and system-level feasibility con-
straints. The engine is designed to support both
small-scaleLLMexperimentsandlarge-scaledistilled
simulations.
Time-stepped Execution (Pseudo-code) The
simulator advances in discrete time steps (typically
15-minute intervals) and executes validated actions
under feasibility constraints, while recording struc-
Figure 7: Commuting distance distributions under
tureddecisiontracesforanalysisandofflinecompila-
building-levelgroundingversusatract-centroidbase-
tion.
line. The baseline collapses within-tract heterogene-
This modular architecture supports repeatability
ity by placing all households at tract centroids, il-
through deterministic execution and configuration-
lustrating how coarse spatial grounding can distort
based parameters, while enabling extensibility for
short-range commuting structure even when work-
new agent models, additional cities, and integration
place assignments are held fixed.
with external frameworks.
7 Evaluation Cases and Scala-
6 Platform Architecture
bility
GenWorld emphasizes modularity (independent
componentsforflexibility),scalability(efficienthan- 7.1 Evaluation Cases
dling of 200,000+ agents in our reference instan-
tiation), and accessibility (LLM-compatible inter- We report three simulation cases selected according
faces for AI researchers). Figure 8 illustrates the de- to three criteria: (i) the case is generated by the
tailed system architecture. Platform UI screenshots public pipeline or the paper-figure reproduction con-
(Streamlit-basedinterface)areprovidedinAppendix tract,(ii)ithasquantitativechecksforschedulecom-
Figure A5. pleteness and spatial feasibility, and (iii) it supports
a specific claim about GenWorld rather than only
serving as a visual showcase. Table 2 summarizes
6.1 System Overview
the cases. In all reported runs, each person has a
The platform is organized into three layers: complete 1,440-minute daily schedule with no gaps
14

<!-- page 15 -->

Figure 8: GenWorld System Architecture. The platform is organized into three layers: Population & Envi-
ronment Foundation, Agent Decision Framework, and Simulation Engine. The architecture supports LLM
integration and knowledge distillation for city-scale scalability.
or overlaps, and the activity-to-land-use compatibil-
ity checker reports zero violations.
Algorithm 1 Time-stepped simulation engine with 7.1.1 Case 1: Full-City Weekday Baseline
structured decision interface
The full-city baseline simulates 196,608 agents dis-
1: for each simulation step t do
tributed across 89,988 private households, with addi-
2: determine active agents S t from schedules tionalgroup-quarterrecordsretainedseparatelyfrom
3: for each agent i∈S t do private-home assignment. Building-level home as-
4: constructcontextc i,t fromworldstateand signment, home/school/work anchors, and daily ac-
persona
tivityschedulesareexecutedunderthestructuredin-
5: o˜ i,t ←ϕ(c i,t ;q t ) ▷ binned observation terface. The run produces 947,233 activity records.
6: A i,t ←κ(q t ,o˜ i,t ) ▷ finite candidates Each agent receives a complete daily schedule from
7: a i,t ←π(o˜ i,t ,A i,t ) ▷ rule/teacher/student midnighttomidnight. Aggregatedbyduration,home
8: if v(o˜ i,t ,a i,t )=0 then activitiesaccountfor79.25%ofperson-minutes,duty
9: a i,t ←f(o˜ i,t ) ▷ deterministic fallback activities (work and study) for 16.22%, leisure for
10: end if
2.43%, and maintenance activities for 2.11%. The
11: executea i,t andupdateagent/worldstates median nonzero movement distance is 5.59 km, the
12: append decision record and trajectory log
95th percentile is 17.26 km, and no movement ex-
13: end for
ceeds 50 km.
14: apply system-level consistency updates (e.g.,
We visualize the spatial distribution of agents and
travel-time feedback and POI capacity)
their daily commuting flows. The 3D visualization
15: recordaggregatemetrics(e.g., utilizationand
supports qualitative inspection of residential den-
travel-time indicators)
sitygradients,commutingcorridors,activityhotspots
16: end for
around commercial and institutional areas, and day–
nightpopulationshifts. Figure9showstwosnapshots
of the visualized resident locations: during worktime
thedistributionexhibitsstrongclusteringaroundac-
15

<!-- page 16 -->

Table 2: Evaluation cases included in the paper. Duration shares are computed over total person-minutes.
Movement statistics use nonzero movement records between consecutive activity locations.
Case Scope Key evidence Supported claim
Full-city weekday 196,608 agents, Home 79.25%, duty 16.22%, non- City-scale rollout over
baseline weekday normal home20.75%;movementp95=17.26 an empirically grounded
km; no trips over 50 km synthetic population
Weekday–weekend 1,000-agent Dutydecreasesfrom15.68%onweek- The same population
contrast paired diagnos- day to 0% on weekend; leisure in- can express different
tic creases from 3.81% to 37.92%; no temporal regimes under
land-use violations controlled day-type
constraints
Warning-response 1,000 agents, After the warning, all agents are Scenario perturbations
perturbation weekday alarm at home at 15:00, 16:00, and can trigger schedule
at 15:00 18:00; emergency-return-home occu- replanning and pro-
pies 37.5% of person-minutes duce auditable response
traces
tivity centers (e.g., the Hiroshima University area), results do not validate weekend behavior against in-
while at nighttime these daytime hotspots become dependentobservations;instead,theyshowthatGen-
sparse as residents return to their home neighbor- Worldcanapplydifferentday-typeconstraintstothe
hoods. same synthetic population while preserving schedule
Additionalweekdayspatialheatmapsforrepresen- and land-use consistency.
tativeactivitytypes(shopping,socializing,andchild-
care) at multiple time windows are provided in the
7.1.3 Case 3: Warning-Response Perturba-
appendix (Figure A6).
tion
We also summarize the city-scale diurnal rhythm
by aggregating simulated activity occupancy over We include a warning-response case as a controlled
time. Figure 10 visualizes the 24-hour distribution perturbation test rather than as a calibrated dis-
ofactivitycategoriesasaradialstackedplot, provid- aster model. Starting from a weekday setting, an
ing a compact view of time-of-day regularities in the alarm is introduced at 15:00. The policy then re-
baseline rollout. plans subsequent activity segments under a rule-
constrained emergency response, producing explicit
emergency return home records and preserving the
7.1.2 Case 2: Weekday–Weekend Behavioral
same schedule-completeness constraints.
Contrast
In the 1,000-agent alarm run, the simulator pro-
To test whether the same population foundation can duces6,000activityrecords. Therunpassestheland-
support different temporal regimes, we compare two use compatibility checker with zero violations. At
1,000-agentdiagnosticrunsunderweekdayandweek- 15:00, 16:00, and 18:00, all 1,000 agents are at home
end settings. Both runs pass the same schedule- according to the diagnostic evaluator. Emergency-
completenessandland-usecompatibilitychecks. The return-home records account for 37.5% of total
weekday run contains 5,016 records and includes person-minutes. This case demonstrates that Gen-
work/study duty activities, while the weekend run World can inject a scenario perturbation, replan
contains5,000recordsandremovesdutyactivitiesby schedules, and produce auditable response traces.
construction. It should be interpreted as an illustrative warning-
The contrast is clear at the duration level. In the response stress test, not as evidence that the current
weekday run, duty activities account for 15.68% of implementation predicts real evacuation behavior or
person-minutes, while leisure activities account for fully implements a psychological theory of disaster
3.81%. In the weekend run, duty falls to 0% and response.
leisure rises to 37.92%. The spatial pattern also
changes: the weekend movement-distance distribu-
7.1.4 Road-Flow Visualization
tion is shorter (p95 = 5.67 km) than the weekday
distribution (p95 = 13.85 km), reflecting more local We further visualize aggregate road-network traffic
discretionaryactivityinthediagnosticsample. These flow by routing simulated trips between consecutive
16

<!-- page 17 -->

Figure 10: 24-hour activity occupancy distribution
in the baseline rollout, shown as a radial stacked
plot (outer radius indicates more people). The vi-
sualization highlights the expected day–night cycle:
home/sleep dominates overnight, work and study in-
(a) Worktime resident-location heatmap.
crease during daytime hours, and leisure and other
discretionary activities rise in the evening.
activity locations. Figure 11 shows the all-day flow
map computed from a 50,000-resident sample, where
edgecolorintensityindicateshigheraccumulatedvol-
umes. Note that this is a static shortest-path visu-
alization without dynamic congestion feedback; val-
idating against real-time traffic counts and incorpo-
ratingequilibriumassignmentareleftforfuturework.
7.1.5 Scalability Analysis
Through offline compilation, simulation-time
decision-making can be implemented as amor-
tized constant-time table lookup and sampling
under bounded candidate sets. The computational
(b) Nighttime resident-location heatmap. complexity comparison is as follows:
Figure 9: Day–night contrast of visualized resident • Online LLM: O(N ·T ·C ) per simulated
LLM
locationsinthebaselinerollout. Theworktimesnap- day, where N is agent count, T is decision steps
shot highlights dense daytime clustering around ma- per day, and C is per-query LLM inference
LLM
jor institutional and employment centers (e.g., the cost (typically 0.5–2s for local 7B models).
Hiroshima University area), whereas the nighttime
snapshotshowstheseareasbecomingnearlyemptyas • Distilled policy: O(N · T · C lookup ), where
the population shifts back toward residential neigh- C lookup ≈ 1µs (hash table lookup + categorical
borhoods. sampling).
For N = 200,000 agents with T = 96 decision
pointsperday(15-minutesteps),onlineLLMsimula-
tionwouldrequire∼19Minferencecallspersimulated
day, which is computationally expensive in practice.
Our distilled policy replaces these calls with table
17

<!-- page 18 -->

tances against YJMob100K mobile phone data, and
activity schedules against the Japanese National
Time Use Survey (e-Stat). Our activity schedule
validation shows good agreement for diurnal pat-
terns (average correlation r > 0.86, RMSE < 3%),
thoughpeak-timeshiftsforwork/studyactivitiessug-
gestlunch-breakmodelingneedsrefinement. Broader
validation, such as link-level traffic counts and full
OD-flow correlation, would require additional cali-
brated datasets and is left for future work.
Distillation Fidelity Our distillation pipeline ag-
gregates teacher-model responses into lookup tables,
but the fidelity of this compilation is not fully vali-
dated. We use K = 10–30 samples per context key
withasingleteachermodel(Gemma327B);ablation
Figure 11: All-day road-network traffic flow aggre-
of sampling count, temperature, and teacher model
gatedfroma50,000-residentsample. Tripsarerouted
choice is needed. We also do not quantitatively com-
via static shortest paths (no congestion feedback);
pare distilled outputs against fresh teacher queries
edge intensity indicates accumulated volume. This
(e.g., via KL divergence or decision agreement rate).
is intended as a visualization of spatial demand pat-
terns rather than a validated traffic simulation.
Behavioral Modeling The structured interface
enablesloggingandanalysisofLLM-drivendecisions,
lookups, allowing city-scale rollout in our reference but connecting these to human decision processes is
setup. not addressed here. Possible extensions include com-
In a micro-test, Python lookup achieves 1.85M parisonsagainsthumansubjectsorstated-preference
queries/s (0.54µs per query) over 200,000 random- surveys, sensitivity analyses of prompt design, and
ized context keys on an Intel Core i5-14600K CPU. evaluation of emergent behaviors under scenario per-
End-to-endwall-clocktimepersimulatorstepalsoin- turbations.
cludes environment updates, spatial queries, and ac-
tivityexecution;profilingundervaryingagentcounts
Case-Study Boundaries The three cases in Sec-
is ongoing work.
tion 7 are intended to demonstrate infrastructure
capabilities under controlled settings. The full-
7.2 Summary city weekday case supports scalability and schedule-
generation claims, while the weekday–weekend com-
These cases show three aspects of GenWorld: city-
parison demonstrates that the same population can
scale rollout over an empirically grounded popula-
be simulated under different temporal constraints.
tion, controlled behavioral contrast across day types,
The alarm case is more limited: it is a warning-
and auditable replanning under a warning perturba-
response perturbation with rule-constrained replan-
tion. TheresultssupportGenWorldasareproducible
ning and should not be interpreted as a calibrated
simulationinfrastructure. Theydonotbythemselves
evacuation model, a validated disaster-response fore-
establish calibrated forecasting performance for traf-
cast, or a full implementation of Protection Motiva-
fic, evacuation, or policy outcomes; broader valida-
tionTheory. ItsroleistoshowthatGenWorldcanin-
tion would require additional external observations
ject a scenario event and produce auditable response
and scenario-specific calibration.
traces for later behavioral calibration.
8 Discussion
Generalizability The current implementation
is instantiated in Higashihiroshima, a mid-sized
Limitations and Future Work Several limita- Japanese city with approximately 200,000 residents.
tions remain in the current reference instantiation. Higashihiroshima has a relatively dispersed urban
formcenteredaroundHiroshimaUniversity; scalabil-
Validation Scope We validate synthetic popu- itytodensermetropolitanareas(Tokyo,Osaka)with
lations against census tabulations, commuting dis- more complex transit networks remains untested,
18

<!-- page 19 -->

and computational challenges may arise at 10× census tabulations, commuting-distance diagnostics
population scales. against YJMob100K, and reproducible evaluation
Our data pipeline relies on Japan-specific sources cases covering full-city weekday rollout, weekday–
(e-Stat census, YJMob100K mobility, Hiroshima weekend contrast, and warning-response perturba-
DoBOX land use). Replication elsewhere requires tion. These results support GenWorld as a platform
equivalent data sources and adapted preprocessing; for grounded and scalable LLM-agent experimenta-
availability and format consistency vary across re- tion. They do not establish calibrated forecasting
gions. Activity patterns and commuting behav- performance for transportation, evacuation, or pol-
iors also differ across urban contexts—US suburban icy analysis; such applications require additional be-
sprawl, European compact cities, and Asian high- havioral calibration, external validation data, and
density development each have distinct characteris- scenario-specific evaluation metrics. Code, configu-
tics. The distilled decision distributions may not rations, documentation, and a deterministic public
transfer without local calibration. demo are available in the project repository, follow-
ingtheprinciplesofreproducibleurbanresearch[7].
Potential Application Scenarios Although the
results reported in this paper focus on empirical Code and Data Availability
grounding, scalable rollout, and controlled scenario
diagnostics,thesameinstantiationandstructuredde- Code, configuration files, documentation, and a de-
cisiontracescansupportqualitativewhat-ifanalyses. terministic public demo are available at https://
Example extensions include transportation-demand github.com/Perseus1993/genworld. The reposi-
inspection under hypothetical transit or land-use tory includes the staged data-preparation pipeline,
changes, warning-response experiments with richer the public demo for tract 34212058004, and a paper-
behavioral models, and urban policy diagnostics un- figure reproduction manifest. Large source datasets
der routine or capacity modifications. Such uses re- and generated outputs are not redistributed in the
quire scenario-specific assumptions, calibration data, repository. Open or registration-based inputs should
and validation metrics before they can be treated as be obtained from their original providers and placed
forecasts or decision-support evidence. accordingtothepathsdocumentedintherepository.
YJMob100K-derived inputs are non-redistributable
and are used only as local validation inputs. The
9 Conclusion
arXiv source package contains only the manuscript
sources and figures needed to reproduce the paper
This paper introduced GenWorld as an empirically
PDF.
groundedurbansimulationinfrastructureforscalable
LLM-agent studies. The central problem is not pop-
ulationsynthesisaloneorLLMdistillationalone,but Acknowledgments
the connection between the two: LLM-agent simu-
lations need realistic urban constraints, while city- WethankXuesong(Simon)Zhouforhisvaluablesug-
scalerolloutcannotrelyononlineLLMcallsforevery gestions.
agent decision.
GenWorld addresses this grounding–scaling gap
References
through a connected system design. A building-level
synthetic urban world provides census-consistent
[1] James E Anderson. The gravity model. Annu.
population structure, spatial anchors, and land-use
Rev. Econ., 3(1):133–160, 2011.
constraints. A structured agent interface maps city
and persona states into binned observations, finite
[2] Marco Becattini, Roberto Verdecchia, and En-
candidate sets, JSON-valid actions, deterministic ex-
rico Vicario. Sallma: A software architec-
ecution semantics, and machine-readable traces. Of-
ture for llm-based multi-agent systems. In
fline policy compilation then shifts repeated teacher-
2025 IEEE/ACM International Workshop New
model queries out of the rollout loop and exe-
Trends in Software Architecture (SATrends),
cutescompiledstochasticpoliciesthroughlightweight
pages 5–8. IEEE, 2025.
lookup and sampling.
The Higashihiroshima instantiation demonstrates [3] Filip Biljecki and Yoong Shin Chow. Global
the feasibility of this infrastructure for 196,608 syn- buildingmorphologyindicators.Computers,En-
theticresidents,withdemographicvalidationagainst vironment and Urban Systems, 95:101809, 2022.
19

<!-- page 20 -->

[4] Ayush Chopra, Shashank Kumar, Nurullah [14] Geoffrey Hinton, Oriol Vinyals, and Jeff Dean.
Giray-Kuru, RameshRaskar,andArnauQuera- Distilling the knowledge in a neural network.
Bofarull. On the limits of agency in agent-based arXiv preprint arXiv:1503.02531, 2015.
models. arXiv preprint arXiv:2409.10568, 2024.
[15] Sirui Hong, Mingchen Zhuge, Jonathan Chen,
[5] Abdoul-Ahad Choupani and Amir Reza Mam- Xiawu Zheng, Yuheng Cheng, Jinlin Wang,
doohi. Population synthesis using iterative pro- Ceyao Zhang, Zili Wang, Steven Ka Shing Yau,
portional fitting (ipf): A review and future Zijuan Lin, et al. Metagpt: Meta programming
research. Transportation Research Procedia, for a multi-agent collaborative framework. In
17:223–233, 2016. The twelfth international conference on learning
representations, 2023.
[6] Joshua M Epstein and Robert Axtell. Growing
artificial societies: social science from the bot-
[16] Andreas Horni, Kai Nagel, and Kay W Ax-
tom up. Brookings Institution Press, 1996.
hausen. Introducing matsim. In Multi-Agent
[7] Rosa F´elix, Filipe Moura, and Robin Lovelace. Transport Simulation MATSim. Ubiquity Press,
Reproducible methods for modeling combined 2016.
public transport and cycling trips and associ-
[17] John J Horton. Large language models as simu-
ated benefits: Evidence from the biclar tool.
lated economic agents: What can we learn from
Computers, Environment and Urban Systems,
homosilicus? Technicalreport,NationalBureau
117:102230, 2025.
of Economic Research, 2023.
[8] Jie Feng, Jun Zhang, Tianhui Liu, Xin Zhang,
Tianjian Ouyang, Junbo Yan, Yuwei Du, Siqi [18] Na Jiang, Andrew T Crooks, Hamdi Kavak,
Guo, and Yong Li. Citybench: Evaluating the Annetta Burger, and William G Kennedy. A
capabilities of large language models for urban method to create a synthetic population with
tasks. arXiv preprint arXiv:2406.13945, 2024. socialnetworksforgeographically-explicitagent-
Accepted by KDD 2025 D&B Track. based models. Computational Urban Science,
2(1):7, 2022.
[9] Kunihiko Fujiwara, Ryuta Tsurumi, Tomoki
Kiyono, Zicheng Fan, Xiucheng Liang, Binyu [19] CarlosEJimenez,JohnYang,AlexanderWettig,
Lei, WinstonYap, KoichiIto, andFilipBiljecki. Shunyu Yao, Kexin Pei, Ofir Press, and Karthik
Voxcity: Aseamlessframeworkforopengeospa- Narasimhan. Swe-bench: Can language models
tialdataintegration,grid-basedsemantic3dcity resolve real-world github issues? arXiv preprint
modelgeneration, andurbanenvironmentsimu- arXiv:2310.06770, 2023.
lation. Computers,EnvironmentandUrbanSys-
tems, 123:102366, 2026. [20] Chenlu Ju, Jiaxin Liu, Shobhit Sinha, Hao Xue,
and Flora Salim. Trajllm: A modular llm-
[10] Dawei Gao, Zitao Li, Xuchen Pan, Weirui enhancedagent-basedframeworkforrealistichu-
Kuang, Zhijian Ma, Bingchen Qian, Fei Wei, man trajectory simulation. In Companion Pro-
Wenhao Zhang, Yuexiang Xie, Daoyuan Chen, ceedings of the ACM on Web Conference 2025,
et al. Agentscope: A flexible yet ro- pages 2847–2850, 2025.
bust multi-agent platform. arXiv preprint
arXiv:2402.14034, 2024. [21] Takehiro Kashiyama, Yanbo Pang, Yuya
Shibuya, Takahiro Yabe, and Yoshihide Seki-
[11] MartaCGonzalez,CesarAHidalgo,andAlbert-
moto. Nationwide synthetic human mobility
Laszlo Barabasi. Understanding individual hu-
dataset construction from limited travel sur-
man mobility patterns. nature, 453(7196):779–
veys and open data. Computer-Aided Civil
782, 2008.
and Infrastructure Engineering, 39(21):3337–
[12] Torsten H¨agerstrand. What about people in re- 3353, 2024.
gional science. Transport Sociology: Social as-
[22] Daniel Krajzewicz, Jakob Erdmann, Michael
pectsoftransportplanning,pages143–158,1970.
Behrisch, Laura Bieker, et al. Recent develop-
[13] Samiul Hasan, Christian M Schneider, Satish V ment and applications of sumo-simulation of ur-
Ukkusuri,andMartaCGonza´lez. Spatiotempo- ban mobility. International journal on advances
ral patterns of urban human mobility. Journal in systems and measurements, 5(3&4):128–138,
of Statistical Physics, 151(1):304–318, 2013. 2012.
20

<!-- page 21 -->

[23] David Lazer, Alex Pentland, Lada Adamic, [33] Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li,
Sinan Aral, Albert-L´aszl´o Barab´asi, Devon Junbo Yan, Xiaochong Lan, Zhihong Lu, Zhi-
Brewer, Nicholas Christakis, Noshir Contractor, heng Zheng, Jing Yi Wang, Di Zhou, et al.
James Fowler, Myron Gutmann, et al. Compu- Agentsociety: Large-scale simulation of llm-
tational social science. Science, 323(5915):721– drivengenerativeagentsadvancesunderstanding
723, 2009. of human behaviors and society. arXiv preprint
arXiv:2502.08691, 2025.
[24] Xuchuan Li, Fei Huang, Jianrong Lv, Zhix-
iong Xiao, Guolong Li, and Yang Yue. Be [34] Timo Schick, Jane Dwivedi-Yu, Roberto Dess`ı,
more real: Travel diary generation using llm Roberta Raileanu, Maria Lomeli, Eric Ham-
agents and individual profiles. arXiv preprint bro, Luke Zettlemoyer, Nicola Cancedda, and
arXiv:2407.18932, 2024. Thomas Scialom. Toolformer: Language mod-
els can teach themselves to use tools. Ad-
[25] Sung Yoo Lim, Hyunsoo Yun, Prateek Bansal,
vances in Neural Information Processing Sys-
Dong-Kyu Kim, and Eui-Jin Kim. A large lan-
tems, 36:68539–68551, 2023.
guage model for feasible and diverse popula-
tionsynthesis. arXivpreprintarXiv:2505.04196, [35] Patrick Taillandier, Benoit Gaudou, Arnaud
2025. Grignard, Quang-Nghi Huynh, Nicolas Maril-
leau, Philippe Caillou, Damien Philippon, and
[26] Qi Liu, Can Li, and Wanjing Ma. Gatsim: Ur-
AlexisDrogoul. Building, composingandexper-
ban mobility simulation with generative agents.
imenting complex spatial models with the gama
arXiv preprint arXiv:2506.23306, 2025.
platform. GeoInformatica, 23(2):299–322, 2019.
[27] Tianming Liu, Jirong Yang, and Yafeng Yin.
[36] Gemma Team, Aishwarya Kamath, Johan Fer-
Towardllm-agent-basedmodelingoftransporta-
ret, Shreya Pathak, Nino Vieillard, Ramona
tionsystems: Aconceptualframework.Artificial
Merhej, Sarah Perrin, Tatiana Matejovicova,
Intelligence for Transportation, 1:100001, 2025.
Alexandre Ram´e, Morgane Rivi`ere, et al.
[28] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Gemma 3 technical report. arXiv preprint
Xuanyu Lei, Hanyu Lai, Yu Gu, Hangliang arXiv:2503.19786, 2025.
Ding, Kaiwen Men, Kejuan Yang, et al. Agent-
[37] SethTisue,UriWilensky,etal. Netlogo: Asim-
bench: Evaluatingllmsasagents. arXivpreprint
pleenvironmentfor modeling complexity. In In-
arXiv:2308.03688, 2023.
ternational conference on complex systems, vol-
[29] Sean Luke, Claudio Cioffi-Revilla, Liviu Panait, ume 21, pages 16–21. Boston, MA, 2004.
Keith Sullivan, and Gabriel Balan. Mason: A
[38] Jiawei Wang, Renhe Jiang, Chuang Yang,
multiagent simulation environment. Simulation,
Zengqing Wu, Makoto Onizuka, Ryosuke
81(7):517–527, 2005.
Shibasaki, Noboru Koshizuka, and Chuan Xiao.
[30] Haoxuan Ma, Xishun Liao, Yifan Liu, Qinhua Large language models as urban residents: An
Jiang,ChrisStanford,ShangqingCao,andJiaqi llm agent framework for personal mobility gen-
Ma. Learninguniversalhumanmobilitypatterns eration. Advances in Neural Information Pro-
with a foundation model for cross-domain data cessing Systems, 37:124547–124574, 2024.
fusion. Transportation Research Part C: Emerg-
[39] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He,
ing Technologies, 180:105311, 2025.
YiwenDing,BoyangHong,MingZhang,Junzhe
[31] Luca Pappalardo and Filippo Simini. Data- Wang,SenjieJin,EnyuZhou,etal. Theriseand
driven generation of spatio-temporal routines in potential of large language model based agents:
human mobility. Data Mining and Knowledge A survey. Science China Information Sciences,
Discovery, 32(3):787–829, 2018. 68(2):121101, 2025.
[32] Joon Sung Park, Joseph O’Brien, Carrie Jun [40] Takahiro Yabe, Kota Tsubouchi, Toru Shimizu,
Cai, Meredith Ringel Morris, Percy Liang, and Yoshihide Sekimoto, Kaoru Sezaki, Esteban
MichaelSBernstein.Generativeagents: Interac- Moro, and Alex Pentland. Yjmob100k: City-
tivesimulacraofhumanbehavior.InProceedings scale and longitudinal dataset of anonymized
ofthe36thannualacmsymposiumonuserinter- human mobility trajectories. Scientific Data,
face software and technology, pages 1–22, 2023. 11(1):397, 2024.
21

<!-- page 22 -->

[41] Yuwei Yan, Qingbin Zeng, Zhiheng Zheng,
Jingzhe Yuan, Jie Feng, Jun Zhang, Fengli Xu,
and Yong Li. Opencity: A scalable platform
to simulate urban activities with massive llm
agents. arXiv preprint arXiv:2410.21286, 2024.
[42] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du,
Izhak Shafran, Karthik R Narasimhan, and
Yuan Cao. React: Synergizing reasoning and
actinginlanguagemodels.InTheeleventhinter-
national conference on learning representations,
2022.
[43] Xiaotong Ye, Nicolas Bougie, Toshihiko Ya-
masaki, and Narimasa Watanabe. Mo-
bilecity: An efficient framework for large-scale
urban behavior simulation. arXiv preprint
arXiv:2504.16946, 2025.
[44] Lan Zhang, Yuxuan Hu, Weihua Li, Quan Bai, Figure A1: Census data summary showing age-
and Parma Nand. Llm-aidsim: Llm-enhanced gender-occupation distributions across the finest-
agent-based influence diffusion simulation in so- resolutioncensusunits(level2+level4)inHigashihi-
cial networks. Systems, 13(1):29, 2025. roshima. The tabulations are used as a reference
forevaluatingdemographicaccuracyofthesynthetic
[45] Xinnong Zhang, Jiayu Lin, Xinyi Mou, Shiyue
population.
Yang,XiaweiLiu,LiboSun,HanjiaLyu,Yihang
Yang, Weihong Qi, Yue Chen, et al. Socioverse:
A world model for social simulation powered by
llm agents and a pool of 10 million real-world
users. arXiv preprint arXiv:2504.10157, 2025.
[46] Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui
Zhou, Robert Lo, Abishek Sridhar, Xianyi
Cheng,TianyueOu,YonatanBisk,DanielFried,
et al. Webarena: A realistic web environment
for building autonomous agents. arXiv preprint
arXiv:2307.13854, 2023.
A Supplementary Materials
A.1 Additional Figures
A.2 Data Sources
Figure A2: School enrollment distribution across 85
schools in Higashihiroshima, showing the number of
students assigned to each educational level. The dis-
tribution is consistent with official enrollment statis-
tics.
22

<!-- page 23 -->

Table 3: Data sources used to instantiate and validate GenWorld in Higashihiroshima. Access column
indicates availability: Open = publicly available for automatic download; Reg = requires free registration;
NR = non-redistributable (requires user to obtain from original source).
Data Type Source Access Description
Census Data e-Stat Open Age-gender, household, occupation statistics (198 census
units)
Time Use Survey e-Stat Open National time-use survey tabulations for activity distribu-
tions
Admin Bound- e-Stat Open Census tract boundaries for spatial aggregation
aries
Buildings OpenStreetMap Open Buildingfootprintswithheightandarea(45,000+buildings)
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
Figure A3: Example of YJMob100K data show-
ing aggregated commuting flows after registering the
Figure A4: Commute distance distribution compari-
anonymizedmeshgridtoourHigashihiroshimastudy
sonbetweenthesyntheticpopulationandYJMdata,
area. Thedataprovidesmesh-levelorigin-destination
used as a diagnostic for commuting-distance scale.
patternsderivedfromanonymizedmobilephoneGPS
trajectories, and is used as an external mobility ref-
erence.
23

<!-- page 24 -->

(b) Interactive building-level map view for inspect-
ingtheinstantiatedurbanworld(e.g.,landuseand
assignedhouseholds). Residentialbuildingsareren-
(a) Simulation dashboard and real-time activity deredinredwithcolorintensityproportionaltores-
statistics in the Streamlit-based UI. ident counts (darker indicates more residents).
FigureA5: PlatformUIscreenshotsofGenWorld,implementedwithStreamlitforinteractiveinspectionand
monitoring of the simulation and instantiated urban world.
Figure A6: Weekday spatial heatmaps for three representative activity types (shopping, socializing, and
childcare) at five time windows. Each row corresponds to an activity type and each column corresponds to
a time window; color intensity indicates higher occupancy.
24

<!-- page 25 -->

A.3 Intention and Activity-Type Tax-
onomy
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
I = {home,duty,leisure,maintenance},
weekday/weekend intention-chain candi-
dates (with_duty_intention_chain and
without_duty_intention_chain), and the
legal mappings activity→intention and
activity→landuse. These candidate sets de-
fine the finite action space used by offline distillation
and simulation-time lookup.
25

<!-- page 26 -->

Table 4: Reference intention set and allowed activity types used in our instantiation. For each intention
z ∈ I, the teacher scores the predefined candidate set A and we normalize the aggregated scores into a
z
categorical distribution for simulation-time sampling.
Intention z Semantics Allowed activity types A
z
home Stay at residence / rest sleep_rest
duty Obligations (work/school) work_task,study_class
maintenance Daily necessities and errands daily_shopping,personal_service,medical_care,admin_
errand
leisure Discretionary activities solo_meal,social_meal,social_visit,entertainment_
activity,structured_exercise,casual_walk,outdoor_
leisure
A.4 Distillation Prompt Templates • Age bins (3 categories): child (0–17), adult
(18–64), elderly (65+)
Belowarerepresentativeprompttemplatesforoffline
distillation. Each query type uses a fixed template
• Occupation bins (9 categories):
thatincludesresidentprofilefieldsandoutputsstruc-
agriculture worker, industrial worker,
tured JSON scores.
service worker, office worker,
professional,public sector,self employed,
Chain Scores Prompt non employed, college student
Role-play as a resident and score behavior preferences.
• Day type (2 categories): weekday, weekend
Resident: age_bin=<age>, occupation=<occ>
Scenario: typical <day_type>
Candidates: [<chain_1>, <chain_2>, ...] Activity–Intention Mapping Eachactivitytype
(H=home, D=duty, L=leisure, M=maintenance) maps to exactly one intention category:
Task: Score each chain [0-10]. Output JSON only: Activity Intention
{"scores": {"<chain_1>": 5, "<chain_2>": 5}}
sleep rest home
work task, study class duty
Activity Scores Prompt daily shopping, maint.
personal service,
Role-play as a resident and score activity preferences. medical care, admin errand
solo meal, social meal, leisure
Resident: age_bin=<age>, occupation=<occ> social visit,
Scenario: pursuing intention='<intention>' entertainment activity,
Candidates: [<activity_1>, <activity_2>, ...] structured exercise,
casual walk, outdoor leisure
Task: Score each activity [0-10]. Output JSON only:
{"scores": {"<activity_1>": 5, "<activity_2>": 5}}
Activity–Landuse Mapping Each activity
Full templates and configuration type is constrained to specific landuse categories
files are available in the repository at (abbreviations: C=commercial, I=industrial,
data prepare/step4 activity/. P=public facility, T=transport, O=open space,
R=residential, A=agriculture, N=nature):
A.5 LLM Interface Schema Activity Landuse
sleep rest R
This section provides detailed repeatability notes
work task C,I,P,T,O,A
for the LLM-ready interface, including discretization study class P
bins, activity–landuse mappings, and missing value daily shopping, personal service C
medical care, admin errand P
handling.
solo meal C,P,T,O
social meal, entertainment C,O
social visit R,O
Context Discretization Bins Agent context is
structured exercise O,P
discretizedintocoarsebinstoenableefficientlookup-
casual walk O,road
table compilation: outdoor leisure O,N
26

<!-- page 27 -->

Missing Value Handling When agent attributes 1. Coarse-bin fallback: Map the unseen key
are incomplete, the following defaults apply: to a coarser bin (e.g., specific occupation →
non employed)
• Missing occupation: Mapped to
non employed bin 2. Defaultdistribution: Ifnomatchingcompiled
distribution exists, use a uniform distribution
• Missingage: Mappedtoadultbin(modalcat- over the candidate action set
egory)
In practice, our discretization yields 3×9×2 = 54
• Missing home location: Agent excluded unique context keys for activity preference queries,
from spatial activity generation; flagged as which are enumerated during offline compilation.
no location
• No valid POI for activity: Fallback to near-
est POI of any compatible landuse type; if none
available within search radius, activity skipped
The complete schema files are
available in the repository at
data prepare/step4 activity/bins *.json.
A.6 Distillation Setup
Weperformofflinedistillationbyrepeatedlyquerying
a teacher model under identical discretized context
keyss(Section4)andestimatingempiricalactiondis-
tributionsforeachdecisionquerytype. Prompttem-
platesusedfordistillationarelistedinAppendixA.4.
Sampling Hyperparameters Inourreferencein-
stantiation, we use the following configuration:
• Repetitionspercontextkey(K): 10samples
per unique (age bin,occupation bin,day type)
tuple
• Teacher model: Gemma 3 27B [36] served lo-
cally via Ollama
• Temperature: 0.7 for score generation (en-
abling diverse but coherent responses)
• Sampling: No adaptive sampling; uniform K
across all context keys
Hardware Distillation was performed on a work-
station equipped with an RTX 4090 GPU (24GB
VRAM), 96GB RAM, and an Intel Core i5-14600K
CPU. The teacher model was queried through
AgentScope [10].
Unseen Key Handling At simulation time, if a
contextkeyswasnotencounteredduringdistillation
(due to rare demographic combinations), we apply a
fallback strategy:
27
