# Extracted fulltext (pdfplumber)

Source: https://arxiv.org/abs/2606.12657
<!-- page 1 -->

TrajGenAgent: A Hierarchical LLM Agent for
Human Mobility Trajectory Generation
Siyu Li†, Toan Tran†, Lingyi Zhao‡, Khurram Shafique‡, Li Xiong†
† Dept. of Computer Science, Emory University, Atlanta, GA, USA
‡ Novateur Research Solutions, Ashburn, VA, USA
{siyu.li, viet.toan.tran, lxiong}@emory.edu, {lzhao, kshafique}@novateur.ai
Abstract—Humanmobilitydataisessentialfortransportation, fic statistics, and handcrafted behavioral rules [5]. Such
urban planning, and epidemic control. Yet large-scale trajectory simulation-based methods require careful parameter tuning
collection is often costly and restricted by privacy concerns,
and often fail to capture complex mobility patterns due to
motivating the need for realistic synthetic mobility trajectory
over-simplified heuristics [6]. More recent data-driven mod-
generation. Recent LLM-based generators typically follow two
paradigms:(i)promptengineering,whichprovidesefficientzero- els, including Generative Adversarial Networks (GAN) and
shot generation with general prior knowledge but lacks fine- spatiotemporal point processes, learn mobility distributions
grained spatiotemporal grounding; and (ii) fine-tuning with directlyfromdatatogeneratelarge-scaletrajectories[7]–[10].
structured trajectories, which achieves strong spatiotemporal
However,theyoftensufferfromtraininginstability,scalability
precision but incurs substantial computational cost and may
limitations, remain limited in modeling long-range and com-
weaken general reasoning. Tool-augmented agents are emerging
but remain at an early stage and still lack effective coordination plex dependencies, and lack explicit semantic understanding
betweenhigh-levelplanningandlow-levelrealization.Toaddress of human routines.
these limitations, we propose TrajGenAgent, a semantic-aware With the emergence of Large Language Models (LLMs)
hierarchical LLM-agent framework for trajectory generation
[11], recent studies have begun to leverage their powerful
without model fine-tuning. TrajGenAgent adopts a two-stage
sequence modeling and reasoning capabilities for trajectory
orchestrator–worker design that decouples macro-level activity
structure from micro-level spatiotemporal dynamics. In the generation [12]–[14]. Existing LLM-based methods can be
first stage, an LLM synthesizes an activity chain for a given categorized by how spatiotemporal knowledge is integrated:
individual and day of the week via in-context learning over (1) language-level approaches, including pure prompting that
historic examples. In the second stage, a deterministic workflow
relies on semantic priors [15] and lightweight text-based fine-
instantiateseachactivityvisitwithdistance-awarerule-basedlo-
tuning that inject global spatiotemporal knowledge in natural
cationretrievalandLLMaugmentedkinematics-awaretemporal
generation. language form [13]; (2) trajectory-level fine-tuning that en-
Traditional evaluation metrics for synthetic mobility data codes structured trajectories as token sequences [12]; and (3)
primarily assess aggregate spatiotemporal statistics, which do tool-augmented agent paradigms that externalizes spatiotem-
not capture behavioral fidelity or realism of individual trajec-
poral grounding by invoking dedicated tools or knowledge
tories. To address this limitation, we introduce an anomaly-
sources during inference time [14], [16].
detection-based evaluation framework with two complementary
anomaly detectors that provide behavior & semantic feedback Language-level approaches preserve an LLM’s general
beyond macro-level statistical consistency. Experiments on both knowledgeandadaptability,butofferlimitedcapabilityoffine-
benchmarkandlarge-scalesimulationdatasetsshowthatTrajGe- grained spatiotemporal pattern injection, often yielding trajec-
nAgent outperforms baselines in both spatiotemporal statistical
tories that are semantically plausible yet poorly calibrated in
metricswhilealsoimprovingsemanticcoherenceandindividual-
time and space. In contrast, trajectory-level fine-tuning meth-
specific behavior fidelity, all without parameter updates.
Index Terms—Human Mobility Trajectory Generation, LLM odssuchasGeo-Llama[12]representtrajectoriesassequences
Agent,Orchestrator–WorkerArchitecture,Zero-ShotReasoning, of visits and adapt pretrained LLMs via parameter-efficient
Workflow-Based Tool Integration fine-tuning (e.g., LoRA [17]). While achieving strong spa-
tiotemporal fidelity, they introduce substantial computational
I. INTRODUCTION
overhead and tightly entangle semantic reasoning with low-
Human mobility data, represented as trajectories or se- levelstatisticalpatternfitting,over-specializingthemodeland
quences of visits, is essential for advancing research and reducinggeneralreasoningcapacityandcontrolofindividual-
applications in transportation, urban planning, social dynam- level semantic behaviors.
ics, and epidemiology [1]–[3]. However, collecting large- These observations reveal a fundamental tension: realistic
scale trajectory data is often constrained by high costs and mobilitygenerationrequiresbothsemanticcoherenceandfine-
privacyconcerns,makingreal-worldmobilitydatasetsdifficult grained spatiotemporal grounding. Here, semantic coherence
toaccess[4].Thishasmotivatedthedevelopmentofsynthetic refers to the consistency of a generated trajectory with hu-
yet realistic trajectory generation methods. man activity logic, individual- and day-specific routines, and
Existing Approaches and Limitations. Early approaches activity–POI–time compatibility, while fine-grained ground-
relied on micro-simulators calibrated using sensor data, traf- ing concerns the accurate reflection of location preferences,
6202
nuJ
01
]IA.sc[
1v75621.6062:viXra

<!-- page 2 -->

Fig. 1: The TrajGenAgent framework. A hierarchical orchestrator–worker LLM agent workflow, where a LLM orchestrator
synthesizes individual- and day-controlled activity-chain scaffolds via in-context learning over historical evidence, and a
deterministic LangGraph worker loop grounds each activity into complete visits by peer-augmented POI retrieval, distance-
/kinematics-aware travel-time propagation, and a context-aware, constraint-guided LLM duration module.
transition patterns, and temporal regularities. The above two Schema compliance cannot be guaranteed at 100% for long-
approaches struggle to achieve both simultaneously. Tool- horizon trajectories; a single malformed or missed tool call
augmented agent paradigms, while promising, remain at an can leave missing fields (e.g., POI or time) and break visit-
early stage and still lack effective coordination between high- to-visit dependencies, trigger cascading errors that corrupt
level behavioral planning and low-level spatiotemporal real- subsequent steps and the overall daily schedule. Moreover,
ization. supervised fine-tuning for tool-calling behavior introduces
additional training cost and may compromise generalization
Challenges in LLM Agent based Mobility Generation.
capability due to catastrophic forgetting [16].
LLM agent based paradigm offers a principled solution to the
Workflow-managedorchestrationoffersapromisingalterna-
previously observed tension: the LLM serves as a semantic
tiveforstableanddeterministictoolexecutioninlong-horizon
reasoning and planning core, while external tools can inject
trajectory generation. However, designing such workflows is
precise spatiotemporal evidence at inference time without
nontrivial: it requires structuring control flow, enforcing visit-
requiring all domain knowledge to be encoded into model
leveldependencies,andbalancingdeterministicexecutionwith
parameters [18], [19]. However, effectively leveraging LLM
semantic flexibility. To our knowledge, prior work has not
agents for trajectory generation presents several challenges.
explored workflow design for trajectory generation.
GeneralLLMagentframeworksprimarilydifferinhowthey
Evaluation Gap in Mobility Generation. Beyond agent
structure and enforce tool invocation: 1) schema-registered
design, a complementary challenge lies in how generated
prompt-based calling, 2) supervised fine-tuning on function-
trajectories are evaluated. Most trajectory-generation evalua-
call traces for higher reliability (e.g., tool-calling specialized
tions rely on aggregate distributional distance metrics (e.g.,
models) [20], and 3) workflow-managed agents that organize
Jensen–Shannon divergence (JSD) between real training data
tool execution as a state machine to guarantee stable control
andgeneratedtrajectoriesovertraveldistance,visitfrequency,
flow and termination while reserving the LLM for steps
or transition matrices) [8], [12]. These metrics quantify
requiring semantic generalization [21].
population-levelstatisticalsimilaritybutoftenmissindividual-
A natural agent design for trajectory generation is to fine-
level semantic defects—e.g., a location–time pattern that is
tune or prompt an LLM to autonomously invoke tools via
normal for one may be anomalous for another, even if global
structured function-call schemas [20]. However, trajectory
statistics match.
generation requires repeated, deterministic decisions for every
visit(locationchoice,travel-timepropagation,durationestima- Contributions. We propose TrajGenAgent, a zero-shot hi-
tion),whichmakesend-to-endautonomoustoolcallingfragile. erarchical agent framework that orchestrates heterogeneous

<!-- page 3 -->

reasoning components within a deterministic workflow im- spatiotemporalgrounding.Thisyieldstrajectoriesthatare
plemented using LangGraph [21]. By integrating LLM-based both semantically coherent and faithful to fine-grained
reasoning with rule-based retrieval and explicit physical cal- spatiotemporal statistics.
culations, it ensures semantic-aware planning and physics- • Behavior-Aware Evaluation Framework. We introduce
aware fine-grained spatiotemporal knowledge injection with- a novel evaluation framework that augments traditional
out costly model updates. As shown in Fig. 1, TrajGenAgent statistical metrics with two complementary anomaly de-
decomposes generation into a macro-to-micro pipeline. In tectors (ICAD and BeSTAD), trained to distinguish real
Stage 1, an orchestrator LLM produces an activity-chain from abnormal or implausible trajectories, to assess the
scaffold (a semantic skeleton) via in-context learning over an semantic coherence of the generated trajectories.
individual’s historical daily chains and contextual information • ComprehensiveExperimentalEvaluation.Experiments
(personal attributes and day context). In Stage 2, specialized on large scale datasets show that TrajGenAgent out-
worker modules transform each activity into a complete visit performs baselines on spatiotemporal statistical align-
through a predefined workflow that injects fine-grained spa- ment and semantic coherence, without expensive param-
tiotemporal knowledge. eter updates. Anomaly-detection results suggest that our
Concretely, Stage 2 consists of two specialized workers: inference-time grounding with individualized evidence
a spatial worker and a temporal worker. The spatial worker and kinematics-aware priors preserves semantic plau-
performsrule-basedlocationretrievalusingpersonalstatistical sibility and avoids detectable artifacts, while baselines
priors from a peer-augmented candidate pool constructed by can still exhibit anomalous trajectory patterns despite
similaritymatchingacrossindividuals.Thisenablescontrolled matching aggregate statistics, especially on behaviorally
exploration while restricting locations within a personalized diverse datasets.
feasible set. A distance-aware mechanism further enforces
II. RELATEDWORK
transition plausibility by aligning candidate locations with the
user’shistoricalactivity-pairmovingmodalities,ensuringcon- Mobility Trajectory Generation without LLMs. Prior
sistency with observed velocity and movement distributions. to LLM-based approaches, mobility generation was domi-
Thetemporalworkeradvancestimebyjointlyinferringarrival nated by simulation and neural-based generative modeling.
timestamps and stay durations. Specifically, it combines (i) a Simulation-based methods synthesize trajectories using hand-
kinematics-awaretravel-timeestimatorthatleveragesmoving- crafted behavioral rules and physically motivated estimations
modality priors with (ii) an LLM-based duration module that calibrated from sensors or surveys [24], [25]. They are often
respects time budget constraints. Given the generated history brittleduetoover-simplifiedheuristics.Data-drivenmodelsin-
andtheremainingitinerary,theworkflowiterativelycalibrates steadlearntrajectorydistributionsdirectlyfromhistoricaldata.
each visit’s arrival time and dwell time to maintain local A common formulation encodes mobility as a fixed-interval
transition plausibility and day-level schedule consistency. To spatiotemporal sequence, and learns next-step transitions with
ensurerobustness,lightweightverifierssupervisebothworkers recurrent backbones (e.g., RNN/LSTM variants) [26], [27].
through schema-enforced fallbacks and feasibility constraints, Beyond one-step predictors, GAN-based generators improve
which ensure both structural format and time validity. distribution matching by adversarial training [28], with repre-
Finally,tobetterevaluatebehavior-levelplausibilitybeyond sentativevariantsincludingadversarialtrajectorysynthesis[9]
traditional aggregate statistical metrics, we propose a novel andreinforcement-learning-basedsequencegeneration[6],[8],
anomaly-detection based evaluation framework. We use two [29]. Despite progress, fixed-interval representations produce
detectors with complementary emphases: ICAD which identi- unnecessarily long sequences with repeated location states
fies local visit-wise inconsistencies [22] and BeSTAD which and implicit time encoding, resulting in ambiguous tempo-
capturesuser-levelbehavioralshifts[23].Bothareappliedpost ral representation and degrades trajectory generation quality.
hoctoassessthesemanticcoherenceofgeneratedtrajectories. To address these limitations, recent work adopts visit-wise
Our contributions are summarized as follows: trajectory and continuous-spatiotemporal formulations based
• HierarchicalLLM-AgentFramework.WeproposeTra- on deep spatiotemporal point processes (DeepSTPP) [10],
jGenAgent, a zero-shot hierarchical LLM-agent frame- [30], which model trajectories asirregular visit sequences and
work that injects spatiotemporal knowledge at inference jointly capture where and when visits occur. However, these
time via a deterministic, verifier-guarded orchestrator– generators remain limited in modeling long-range, complex
worker workflow. By separating macro-level activity- dependencies and lack explicit semantic understanding of
chain planning from visit-level grounding, TrajGenAgent human routines and behavioral logic.
enables high-fidelity trajectory generation without costly LLM-basedMobilityTrajectoryGeneration.Recentstudies
fine-tuning or fragile autonomous tool calling. leverage LLMs for mobility generation by exploiting their
• Personalized and Physics-Aware Control. We enable strong sequence modeling and semantic reasoning capabili-
fine-grained personalized control over user- and day- ties. They mainly differ in how fine-grained spatiotemporal
specific routines by constraining generation with histor- knowledge is incorporated.
ical evidence and configurable tool scopes, while en- a) Pure prompting-based generation: A representative
forcing time budgets and physics-aware mobility during line of work relies on pure prompt engineering to generate

<!-- page 4 -->

plausible trajectories in a zero-shot manner [15]. For ex- objectives and representations.
ample, [13] crafts prompts using statistical summaries (e.g., GPS trajectory generation targets dense coordinate streams
demographics, event types, and event–temporal correlations) at very fine-grained spatial and temporal resolution (e.g., per-
to emulate travel-diary-style generation without additional second), instead of visit-wise trajectories that encode discrete
training. [31] further improves prompting via self-consistent activities and human behavioral semantics. Early works syn-
activity pattern identification and retrieval-augmented genera- thesizeGPStracesbyperturbingrealtrajectoriesorrecombin-
tion (RAG), using LLM priors to evaluate candidate prompt ingtrajectorysegments[34],[35],whichcandistortspatiotem-
combinations conditioned on individual profiles and POI poralcharacteristicsandreduceutility.Data-drivenapproaches
background information. While prompting can exploit rich have also been explored, including GAN-based approaches
contextual cues to produce semantically coherent, narrative- [36], [37] and diffusion-based models such as DiffTraj [38],
level mobility routines, it typically lacks explicit injections of which learn fine-grained spatiotemporal dynamics from raw
fine-grained spatiotemporal information, which limits precise GPS sequences. Due to this distinct granularity and goal, we
micro-level spatiotemporal grounding. do not include GPS-trajectory generators in our comparisons.
b) Trajectory-level fine-tuning: In contrast, trajectory- Next point-of-interest (POI) recommendation predicts an
level fine-tuning injects spatiotemporal knowledge into model individual’s next POI conditioned on historical mobility and
parameters by encoding structured trajectories as visit se- context, typically framed as a sequential recommendation
quence prompts and fine-tuning pretrained LLMs with problem,withlimitedorcoarsetemporalmodeling.Priorwork
parameter-efficient adapters such as LoRA [17]. Geo-Llama spans probabilistic, deep learning, graph-based, and LLM-
[12]exemplifiesthisparadigmbyoptimizinganext-tokenpre- based recommenders [39]–[46]. In contrast, our task is tra-
diction objective over discretized spatiotemporal visit tokens, jectory generation: synthesizing full-day visit sequences with
and further introducing visit-wise permutation so the model both visit-specific spatiotemporal fidelity and realistic global
learns temporal regularities from time features within visits dynamics, rather than focusing on one-step recommendation
rather than from the original sequence order, yielding strong accuracy. Although recommenders can be rolled out autore-
micro-level spatiotemporal fidelity without external semantic gressively, they often lack explicit mechanisms to maintain
annotations. However, heavy adaptation on structured tokens long-horizon coherence. Given these fundamental differences,
canintroducesubstantialcomputationaloverheadandentangle wedonottreatPOIrecommendationmethodsasbaselinesfor
semantic reasoning with low-level spatiotemporal statistics, our work.
reducing the general semantic capabilities and flexibility of
foundation models. III. TRAJGENAGENTFRAMEWORK
c) LLM agents and tool-augmented workflows: The
A. Trajectory Representation and Problem Setup
above limitations motivate an emerging paradigm that re-
framesLLMsastool-augmentedagentsratherthanmonolithic Werepresentadailytrajectoryasasequenceofvisitsrather
generators,enablinginference-timespatiotemporalknowledge than a fixed-interval time series. For an individual u on date
injectionthroughmodularinterfaceswithoutcostlyfine-tuning d, a trajectory is a sequence of visits:
orparameterupdates[14],[18],[19].Beyonddomainknowl-
T =[(a ,p ,ts,te)] Nu,d, (1)
edge, robust agentic generation often requires procedural u,d i i i i i=1
control over structured reasoning (e.g., CoT-style traces [32])
where a ∈ A is the activity type, p ∈ P is a POI identifier
and tool usage (e.g., schema-registered function calls [19]). i i
(withassociatedlatitude/longitude),andts,te arethestart/end
Existing agent frameworks typically enforce tool use via i i
timestamps of the visit. The number of visits N varies by
three strategies: (i) supervised fine-tuning on tool-call traces u,d
individualandday,andwefurtherdefinethevisitdurationas:
with explicit JSON/function-call schemas to improve invo-
cation reliability (e.g., tool-calling specialized models such δ =te−ts. (2)
i i i
as xLAM [20]); (ii) zero-shot prompting with schema/tool
registration, leveraging strong foundation models that can Given a historical trajectory dataset, an individual u and
follow JSON-style interfaces (e.g., GPT4-OSS-120B [33]); targetdated,ourgoalistogenerateavisitsequenceT that
u,d
and (iii) workflow-managed orchestration that encodes tool is realistic, reflecting both the individual’s historical mobility
execution as an explicit state machine to guarantee stable and population-level behavioral patterns.
control flow and termination (e.g., LangGraph [21]). Such
workflow-managed agents can flexibly compose heteroge- B. TrajGenAgent Overview
neoustoolstoinjectspatiotemporalevidenceatinferencetime TrajGenAgent adopts a hierarchical orchestrator–worker
while preserving the LLM as a semantic planner. However, agent architecture implemented as a deterministic workflow
systematically designing reliable, long-horizon workflows for in LangGraph [21]. Given an individual u and target date d,
mobility generation remains relatively under-explored [14]. generation is decomposed into two stages:
GPS Trajectory Generation and POI Recommendation.
Stage1:Orchestrator Stage2:WorkerWorkflow
Apart from human mobility trajectory generation, two closely (u,d,H )−−−−−−−−−−−→C −−−−−−−−−−−−−−→T ,
u u,d u,d
related topics study synthetic movement data under different (3)

<!-- page 5 -->

whereH isthehistoricalrepository,C =[a ,...,N ]is
u u,d 1 u,d
an activity-chain semantic skeleton, and T is the final visit
u,d
trajectory.
Stage 1 (Orchestrator) performs semantic planning: it
prompts an LLM with individual-conditioned historical ev-
idence (exemplar daily chains and compact statistical sum-
maries) and synthesizes a plausible activity chain under hard
lexical and structural constraints. Stage 2 (Worker Work-
flow) performs spatiotemporal grounding: it deterministically
instantiates each activity into (p ,ts,te) by executing a fixed
i i i
sequence of modules (POI retrieval, travel-time propagation,
and duration estimation) until completion. In our implemen-
tation, both stages share the same instruction-tuned backbone
Qwen2.5-32B-Instruct[47],servedviaavLLM[48]inference
serverexposinganOpenAIAPI–compatibleinterfaceforhigh-
throughput generation in the deterministic workflow.
a) Why deterministic workflow instead of free-form
tool calling: A natural alternative is to fine-tune an LLM
to autonomously invoke MCP-style tools through schema-
constrained outputs. We avoid this design for three reasons:
(i)reliability—schemafine-tuningstillcannotguarantee100%
valid calls, while mobility generation repeatedly makes struc-
tureddecisionsateveryvisit;(ii)efficiency—tool-callingfine-
tuning is compute-intensive and may weaken instruction-
following robustness, whereas TrajGenAgent leverages strong
Fig. 2: The illustration of Stage 1 LLM semantic planning for
off-the-shelf instruction models at inference time; and (iii)
activity-chain generation.
control/termination—free-form autonomous calling can drift
from global constraints, repeat locally, or loop, which is C. Stage 1: Orchestrator for Activity-Chain Generation
especiallyharmfulforlong-horizondailysequences.Encoding
Stage 1 generates a daily activity chain C =
the procedure as an explicit state machine yields bounded u,d
[a ,...,a ] as a semantic plan for individual u on date
execution, predictable control flow, and reproducibility. 1 Nu,d
d. Rather than training a dedicated generator, the orches-
b) Activity chain as a stabilizing intermediate: Intro- trator leverages in-context learning (ICL) over individual-
ducing C u,d decouples semantic planning from spatiotem- conditioned evidence at inference time, enabling fine-grained
poral realization, which simplifies long-horizon generation personalizationeveninnarrowregimes(e.g.,conditioningona
and reduces error accumulation across visits. As a high-level specificweekdayordaytype).Figure2illustratestheprompt-
scaffold, C u,d anchors global day structure while allowing the level semantic planning process used by the orchestrator.
worker to inject deterministic mobility priors (e.g., distance- From each individual’s historical trajectories, we construct
and speed-based feasibility) without requiring the LLM to an evidence profile Π that characterizes individual pref-
u
directly rank or search over large POI candidate sets. erences and mobility regularities. In addition to activity-
c) Evidence-driven decisions with lightweight verifiers: and POI-level statistics, Π u includes transition-level mobility
Across both stages, TrajGenAgent follows an evidence-to- priors derived from consecutive visits using the great-circle
decision pattern: historical observations provide evidence (ac- distance ℓ i−1,i = dist(p i−1 ,p i ) and the observed inter-visit
tivity and transition tendencies, POI preferences, duration gap ts i −te i−1 .
statistics,andmobilitypriors),andworkflowmodulestranslate (cid:110)
Π = π (a), π (a′|a), π (p|a), µ (δ|a),
this evidence into constrained decisions. Lightweight verifiers u u u u u
(4)
enforce strict output schemas and feasibility bounds through µ (cid:0) ℓ|a→a′(cid:1) , µ (cid:0) v |a→a′(cid:1) , µ (ts|w,a) (cid:111) ,
bounded checks and clipping; upon violations, the workflow u u u 1
triggers deterministic repair or fallback to preserve structural where π (a) is the activity occurrence likelihood, π (a′| a)
u u
validity and schedule feasibility.
istheactivitytransitiontendency,andπ (p|a)istheactivity-
u
Overall,TrajGenAgentbalancesfoundation-modelsemantic conditioned POI preference. Here, π (·) denotes empirical
u
generalization with deterministic spatiotemporal grounding, categorical distributions over discrete choices, while µ (·)
u
enablingreliablelarge-scaletrajectorygenerationwithoutfine- denotes empirical priors over continuous-valued quantities.
tuning while remaining extensible to richer semantic controls The remaining terms characterize empirical priors of visit
and evaluator-in-the-loop feedback. duration, transition distance, transition speed, and weekday-

<!-- page 6 -->

conditioned first-start-time patterns (with w denoting the day propagate visit-to-visit dependencies, and then applies a fixed
type or day-of-week). module order for each visit:
1) Evidence construction from individual history: We con- location_node→travel_time_node
(5)
struct daily activity chains from the individual-specific his-
→duration_node.
torical repository H by extracting each day’s visit sequence
u
This ordering is deliberate: location grounding provides
in temporal order. For a target date d, we retrieve a date-
the spatial context required for travel-time propagation and
specific evidence subset E ⊂H using a prioritized policy:
u,d u
durationscheduling,whileeachmodulereadsandwriteswell-
(i)sameweekday,(ii)samedaytype(weekday/weekend),and
scoped state fields, preventing tool-call drift and ensuring
(iii)fallbacktoallavailabledays.FromE weconstructtwo
u,d
reproducible long-horizon generation.
complementary evidence views:
1) Location Grounding : For each activity visit a , we
i
• Exemplar evidence (ICL anchors): a small set of ground a location in two steps: (1) construct a feasible
historical chains presented verbatim as strong references,
candidatePOIsetP(a ),and(2)scorecandidatesbycombin-
i
allowing the LLM to induce day structure via in-context
ing their likelihood under user/similar-user preferences with
pattern learning.
distance-compatibility, then sample accordingly.
• Summaryevidence(compactpriors):compactactivity- a) Candidate construction with feasible set and con-
frequency and transition-tendency summaries derived
trolled exploration: For each activity a , we retrieve a can-
i
fromtheevidenceprofileΠ inEq.(4),whichregularize
u didate POI set rather than sampling from the full location
generation and reduce implausible chains.
space.Wefirstbuildanindividual-specificfeasiblesetP (a )
u i
2) Evidence-based activity chain generation with verifica- from historical visits. To enable controlled exploration be-
tion: The orchestrator LLM is prompted with (1) day-level yond personal history, we augment candidates using a top-
controllable signals (e.g., day-of-week and day type), (2) K similar-individual pool obtained via similarity matching
historical evidence in the form of exemplar activity chains over mobility signatures (e.g., spatial scale, temporal rhythm,
and compact statistical priors (e.g., activity frequencies and andactivity/transitiondistributions,optionallywithco-location
transition tendencies), and (3) hard constraints, including a signals).
fixedactivityvocabularyandano-adjacent-duplicaterule(with This yields an augmented location memory P (a ) from
sim i
an optional soft home-start/end prior). The output is restricted similar individuals, and we take P(a ) = P (a )∪P (a ).
i u i sim i
to a Python list of activity strings. To ensure robustness, we If P(a ) is empty, we emit an explicit invalid marker (rather
i
apply a bounded generate–verify loop: than silently sampling) to avoid cascading errors.
b) Distance-aware scoring and stochastic selection: To
• Schema check: parse the output as a list and reject
chooseaplausiblenextPOI,wescoreeachcandidatebycom-
malformed generations.
bining likelihood (how likely the user or similar users visits it
• Constraint check: enforce vocabulary membership, and
forthisactivity)withdistancebasedfeasibility(howconsistent
no-adjacent-duplicate constraints.
the travel distance is with the user’s typical transitions). For
• Repair/fallback: retry briefly; if still invalid, fall back
each candidate p∈P(a ), we compute a composite score:
to an evidence-derived default (e.g., a sampled historical i
chain) to prevent error propagation to Stage 2. S(p)=λ f ·s freq (p)+λ d ·s dist (p), (6)
3) Why evidence-based activity chain generation outper- where the frequency prior mixes individual and neighbor
formsfine-tuningforpersonalization: Comparedtofine-tuned preferences with exploration gate α:
generators, this orchestrator is data-adaptive—it can spe-
s (p)=(1−α)P (p|a )+αP (p|a ). (7)
freq u i sim i
cialize to a single individual or a weekday-specific routine
simply by adjusting the evidence scope—and offers fine- The exploration gate α balances individual fidelity and con-
grained controllabilitythroughtheevidenceselectionpolicy. trolled diversity. Moderate changes in α have limited impact
Moreover, by leveraging prompting-based in-context learning, on our statistical or anomaly metrics, but α = 0 can yield
itpreservesthebackbonemodel’ssemanticgeneralizationand near-copytrajectorieswithlowerdownstreamutility,whileex-
requires only inference-time compute (no parameter updates), cessivepeerweightingmaydriftbeyondthetargetindividual’s
yielding a personalized and semantically coherent scaffold for mobility scope.
Stage 2 grounding. To enforce physically plausible transitions, distance com-
patibilityismeasuredagainstthepreviousgroundedPOIp
i−1
D. Stage 2: Workflow-based Spatiotemporal Grounding and the individual’s historical transition-distance regime for
(a ,a ):
i−1 i
Ge G nA iv g e e n n t t h fi e n s a e li m ze a s nt a ic co sk m e p le le to te n v C is u i , t d tr = aje [ c a t 1 o , r . y .. b , y a N ex u e ,d c ] u , ti T n r g aj a - s dist (p)=exp (cid:0) −β· (cid:12) (cid:12)dist(p i−1 ,p)−ℓ¯ u (a i−1 ,a i ) (cid:12) (cid:12) (cid:1) , (8)
deterministic state-machine workflow (implemented in Lang- where dist(·,·) is the Haversine distance and ℓ¯ (a ,a )
u i−1 i
Graph) over i = 1...N . The worker workflow maintains is the individual-specific mean transition distance (with ro-
u,d
a shared state (e.g., visit index, previous POI, current time, bust defaults if unavailable). Finally, we sample p from the
i
and partial trajectory) that each module reads and updates to normalized{S(p)},yieldingstochasticyetprofile-constrained

<!-- page 7 -->

locationgroundingwithbuilt-inpersonalizationandcontrolled Wecompareitagainsttwoprevailingparadigms:(i)trajectory-
exploration, without any model fine-tuning. level fine-tuned LLM generators, represented by Geo-Llama
2) TravelTime: GiventhegroundedPOIs{p }
Nu,d
andac- [12], and (ii) state-of-the-art non-LLM neural generators (see
i i=1
tivities {a } Nu,d, the temporal worker constructs an irregular SectionIV-B).Thissetuptestswhetherazero-shot,workflow-
i i=1
daily timeline by iteratively producing each visit’s start time managed agent can match or surpass both fine-tuning-based
ts anddurationδ (thusendtimete).Timeistreatedasafirst- LLM generators and state-of-the-art non-LLM continuous-
i i i
class continuous variable, avoiding the granularity loss from time neural baselines in spatiotemporal fidelity and semantic
fixed-bindiscretizationandenablingexplicitfeasibilitycontrol coherence, while avoiding costly parameter updates.
through budget and kinematic priors. Beyondconventionalaggregatespatiotemporalstatistics,we
a) Cold-start initialization for the first visit: For i = 1, introduceananomalydetection-basedevaluationframeworkto
we initialize ts from an individual- and weekday-conditioned probe semantic coherence and behavioral plausibility. Specif-
1
prior of the first-visit start time estimated from history. If ically, we incorporate two complementary anomaly detectors,
unavailable,wefallbacktoaconservativedefault(e.g.,morn- ICAD [22] and BeSTAD [23], which capture different abnor-
ing start) and add a small random offset to avoid degenerate mal patterns and provide diagnostic signals that aggregation-
identical schedules across days. level metrics can miss. Overall, our experiments ask whether
b) Distance- and kinematics-aware travel-time propaga- TrajGenAgent (1) preserves basic spatiotemporal statistics
tion: For i > 1, the workflow advances time using a travel- fidelity, (2) improves semantic and behavioral plausibility
time estimate driven by (i) the geographic distance between under anomaly-based scrutiny, and (3) achieves these gains
consecutive POIs and (ii) an individual-specific kinematic with lower computational overhead by avoiding fine-tuning.
prior captured by historical transition speeds: Our code can be accessed at: https://github.com/
ts =te +∆ttravel, Emory-AIMS/TrajGenAgent.
i i−1 i
(cid:18) dist(p ,p ) (cid:19) (9)
∆ttravel =clip i−1 i ·60, ∆ , ∆ . Statistic NumoSim MobilitySyn
i v (a ,a ) min max Totaldailytrajectoriesused 34,000 34,000
u i−1 i
Avg.staypointspertrajectory 7.2 8.7
Here dist(·,·) is the Haversine distance, v u (a i−1 ,a i ) is the #Individuals 1,200 1,200
historical mean speed for transition (a →a ), and clip(·) #Activitytypes 16 6
i−1 i
enforces pre-defined time feasibility bounds (e.g., ∆ min = 5 TABLE I: Training Dataset Statistics
min,∆ =180min).Whenv ismissingorunreliable,we
max u
use robust defaults based on distance regime (e.g., walk vs.
A. Datasets & Preprocessing
drive), preserving kinematic plausibility without requiring the
LLM to reason over high-dimensional mobility dynamics.
Weconductexperimentsontwosyntheticmobilitydatasets:
3) Duration estimation: Unlike travel time, activity dura-
the open-source benchmark NumoSim and our simulated
tion is highly context-dependent (e.g., Work vs. EatOut)
MobilitySyn dataset.
andmayadaptunderschedulepressure.Wethereforedelegate
duration estimation to an LLM worker that conditions on • NumoSim. NumoSim [49] is a large-scale synthetic
mobility benchmark for anomaly detection, providing 8
retrieved evidence and the current generation state:
weeks of stay-point trajectories for 200,000 individuals
• current start time ts i and remaining daily time budget, in Los Angeles.
• current activity a i and its historical duration prior, • MobilitySyn. We create MobilitySyn by following the
• remaining activities [a i+1 ,...,a Nu,d ] and their expected simulation framework in [50] to generate a realistic
total time,
week-long mobility trace for 5,000 individuals over a
• optional individual-specific duration tendencies.
metropolitan area. The simulator produces second-by-
The LLM outputs a strict JSON object (e.g.,
second GPS records, which we convert into visit-wise
{"duration_minutes": 45}). A lightweight
(stay-point) trajectories for evaluation.
verifier enforces schema validity and feasibility:
δ ∈ [δ , min(δ , budget left)], with retry-on-violation Trajectory Representations. Our baselines cover two trajec-
i min max
and deterministic fallback to the historical prior if parsing or tory representations: (i) fixed-interval sequences with 96 steps
validation fails. This evidence-to-decision design preserves per day (15-minute bins), and (ii) visit-wise sequences with
semantic flexibility in duration choices while guaranteeing variable length. TrajGenAgent, Geo-Llama [12], and Geo-
coherent and time-feasible execution. Finally, we update the CETRA[51](seedetailsinSectionIV-B)operateonvisit-wise
end time as te = ts + δ , and proceed to the next visit, trajectories. Geo-Llama represents each visit by a POI ID and
i i i
cumulatively generating a full-day irregular timeline that is a discretized timestamp, whereas TrajGenAgent uses POI IDs
semantically coherent and physically feasible. with continuous timestamps and an intermediate activity type.
Geo-CETRAgeneratescontinuouslocationsandtimes;forfair
IV. EXPERIMENTS
comparison, we discretize its outputs to the same evaluation
Inthissection,weevaluateTrajGenAgentforhumanmobil- grid/time bins. Specifically, we use 15-minute intervals and
ity trajectory generation on two large-scale synthetic datasets. gridsizesof0.5kmforNumoSimand0.7kmforMobilitySyn.

<!-- page 8 -->

B. Baselines Its discrepancy is measured by Frobenius norm:
(cid:113)
We evaluate the performance of our model against the ∥PD − PD′ ∥
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
,l
2
)−PD′ (l
1
,l
2
)|2.
following six state-of-the-art baselines: Lower values indicate better preservation of transition
• GRU [52] and LSTM [53]: Recurrent neural networks structure. We note that G-rank and Transition correspond
that are efficient for sequential data generation. These to global-level while others correspond to trajectory-level
models are able to predict the next location based on patterns.
historically visited locations. 2) Anomaly-Detection Evaluation: Aggregate spatiotem-
• Transformer [54]: A powerful deep learning model poral fidelity can be achieved even when trajectories are
used in various natural language processing (NLP) and behaviorally implausible at the visit or individual level. To
computer vision tasks that leverages self-attention mech- assess behavioral realism beyond population-level metrics,
anisms.Amulti-layerTransformerdecoderisutilizedfor we evaluate generated trajectories with two complementary
trajectory generation. anomaly detectors: ICAD and BeSTAD. Since human mobil-
• SeqGAN [29]: A sequence GAN that introduces a dis- ityrealismisinherentlymulti-facetedandpartlysubjective,we
criminatorasarewardsignaltoguidethegradientpolicy usethesedetectorsasbehavior-awarediagnosticproxiesrather
updateofthegenerator,whichperformsthenextlocation than exhaustive measures of semantic coherence. Intuitively,
prediction task based on the past states. trajectoriesthatarebothstatisticallyrealisticandsemantically
• Geo-CETRA[51]:Aspatiotemporalpointprocess-based coherent in individual behavior should be harder for these
framework for trajectory generation that incorporates detectors to distinguish from trajectories in the training set.
constraint factorization and beam decoding to produce a) ICAD (visit-level multi-context detector): ICAD is
realistic trajectories. a self-supervised autoregressive framework that decomposes
• Geo-Llama [12]: An LLM-based generator that encodes each visit into location, arrival time, and departure time,
daily trajectories as structured visit sequences and learns and learns next-visit regularities under normal mobility pat-
spatiotemporal dependencies via parameter-efficient fine- terns [22]. For anomaly scoring, it uses top-k deviation for
tuning (e.g., LoRA). It applies visit-wise permutation to discrete spatial prediction and a mode-margin density score
encourage learning temporal regularities from visit-level (GMM-based)forcontinuoustemporalcomponents,thenfuses
time attributes rather than sequence order. component-wise deviations into a final anomaly score. A key
property is interpretability: ICAD can attribute abnormality to
C. Evaluation Metrics
spatial, temporal, or compound deviations. This makes ICAD
Our primary intended use case is providing synthetic tra- suitable for testing whether generated visits preserve fine-
jectory data for counterfactual analysis of urban mobility grained spatiotemporal consistency.
patterns, rather than optimizing a specific downstream task
b) BeSTAD (individual-level behavioral shift detector):
such as next-POI recommendation. We therefore evaluate
BeSTAD targets individual-level anomalies by modeling in-
generated trajectories from two complementary perspectives:
dividualized behavior clusters in a past “normal” period
(1)spatiotemporalstatisticsfidelityunderaggregatedmobility
and comparing cluster alignment in a future period [23].
statistics, and (2) behavioral semantics under downstream
It integrates temporal behavior signals with multi-scale spa-
anomaly detection models.
tial semantics (including point/line/polygon context, e.g.,
1) Aggregation-level Spatiotemporal Statistics Metrics:
from OpenStreetMap (OSM), via the Hexagonal Hierarchical
Following prior mobility-generation evaluations [6], [8], we
Geospatial Indexing System (H3)-based indexing) to capture
compare generated and real trajectories through population-
richerbehavioralcontext.Itsanomalyscoreemphasizescross-
and trajectory-level mobility distributions.
period behavioral shifts and emerging routine changes rather
Distance is the distribution of cumulative travel distance
thanisolatedsingle-visitoutliers.Therefore,BeSTADcomple-
per user per day. G-radius (radius of gyration) measures the
ments ICAD by stressing high-level behavioral coherence at
distribution of daily spatial movement range. Duration is the
individual level.
distributionofdwelltimepervisitedlocation.DailyLocisthe
c) Metrics: We report anomaly-detection outputs, AU-
distributionofthenumberofvisitedlocationsperuserperday.
ROC and average precision (AP), by applying detectors with
G-rank is the global visit-frequency distribution over top-100
identical settings to distinguish real trajectories (normal) from
visitedlocations.I-rankistheper-usercounterpartofG-rank.
generated ones (treated as anomalies). Unless otherwise spec-
For these distributional properties, we compute Jensen–
(cid:16) (cid:17) ified, we use a balanced split with equal positive and negative
Shannon divergence (JSD): JSD(D,D′) = h D+D′ −
2 samples, for which random guessing yields AUROC ≈ 0.5
h(D)+h(D′) where D and D′ denote real and generated dis- and AP ≈ 0.5. This conservative setting avoids inflated
2
tributions, and h(·) is Shannon entropy. Lower JSD indicates performance due to class imbalance. From a generation-
better agreement with real mobility statistics. quality perspective, scores closer to chance indicate lower
We additionally compare transition dynamics. separability—i.e., the generated data is harder to distinguish
Transition is the location-to-location transition from real mobility data under the detector—and therefore
probability matrix over discretized locations G. exhibit higher behavioral semantic fidelity.

<!-- page 9 -->

Trajectory-level(↓) Global-level(↓)
Dataset Model
Distance G-radius Duration DailyLoc I-rank G-rank Transition
GRU 0.0111 0.2557 0.2145 0.1561 0.0137 0.0159 0.0156
LSTM 0.0146 0.3113 0.3013 0.1981 0.0893 0.0134 0.0150
Transformer 0.0082 0.2945 0.2150 0.1620 0.0079 0.0112 0.0118
NumoSim SeqGAN 0.0085 0.0998 0.2410 0.1585 0.0082 0.0107 0.0120
Geo-CETRA 0.0093 0.3337 0.0060 0.1128 0.0002 0.0002 0.0088
Geo-Llama 0.0075 0.2361 0.0028 0.0128 0.0001 0.0001 0.0087
TrajGenAgent 0.0006 0.0993 0.0155 0.2117 0.0002 0.0002 0.0075
GRU 0.0116 0.1859 0.1747 0.3368 0.0082 0.0097 0.0132
LSTM 0.0131 0.2823 0.1680 0.3046 0.0044 0.0078 0.0135
Transformer 0.0085 0.3760 0.1510 0.2810 0.0047 0.0065 0.0115
MobilitySyn SeqGAN 0.0089 0.0738 0.1344 0.2437 0.0035 0.0062 0.0108
Geo-CETRA 0.0276 0.5784 0.0319 0.1573 0.0006 0.0006 0.0083
Geo-Llama 0.0268 0.5528 0.0241 0.1209 0.0005 0.0005 0.0078
TrajGenAgent 0.0000 0.0051 0.1308 0.0000 0.0003 0.0003 0.0000
TABLE II: Aggregation-level spatiotemporal statistical metrics of the trajectory generation.
D. Implementation Details that the workflow can robustly reconstruct visit-wise spatial
statistics and movement structure without parameter updates.
• GRU, LSTM, and Transformer are trained for 200
On NumoSim, TrajGenAgent remains highly competitive on
epochs using the Adam optimizer with a learning rate
spatial and transition metrics, while Geo-Llama is stronger
of 0.001. Models share an embedding size of 256, with
on time-centric statistics (notably Duration and DailyLoc).
GRUandLSTMusing6layersof512hiddenunits,while
This gap likely arises because duration grounding is sensi-
Transformer adopts a decoder-only architecture with 4
tive to accumulated state errors and conflicts between the
layers and 4 attention heads.
sampled activity scaffold, remaining time budget, and sparse
• SeqGANincludesanLSTM-basedgeneratortrainedwith
individual temporal evidence. We attribute this to the in-
16-dimensional embeddings and 16 hidden units. Dis-
creased behavioral complexity of NumoSim (more activity
criminator employs diverse filter sizes and counts, and
types and richer daily schedules), where fine-tuning on struc-
rolloutnumberof8.Theentirepipelinecarries40epochs
tured visit tokens can more precisely fit dwell-time and visit-
of pre-training and 20 epochs of adversarial training.
count distributions; in contrast, our budget-aware duration
• Geo-CETRA employs a conditional Gaussian Mixture
module prioritizes schedule feasibility and semantic plausi-
Model with 8 spatial and temporal mixture components
bility; since it is not directly optimized to match aggregate
and a beam search strategy with a beam size 10 and top
duration distributions, it can be less calibrated on micro-level
k=3.OptimizationisperformedwiththeAdamoptimizer,
duration statistics on more behaviorally complex datasets. A
a learning rate of 0.01, a scheduler with a decay factor
key factor across baselines is trajectory representation. The
of 0.99, and z-score normalization for input data.
fixed-interval generators (GRU/LSTM/Transformer/SeqGAN)
• Geo-Llama fine-tunes the Llama-2-7b-chat-hf
operate on 96-step sequences per day with implicit time
modelusingLoRAwithabatchsizeof48,alearningrate
encoded through discretized bins, which produces long se-
of 0.00001, LoRA alpha32, LoRA dropout 0.02, LoRA r
quenceswithrepeatedstates(staypoints)andcanobscurefine-
16, and 20 epochs. Sampling uses temperature 1.2.
grained temporal patterns. In contrast, visit-wise generators
• TrajGenAgent performs zero-shot generation without
(Geo-CETRA, Geo-Llama, and TrajGenAgent) model daily
modelfine-tuning,usingQwen2.5-32B-Instructas
trajectories as variable-length visit sequences, which better
thebackboneLLM.Bothworkflowstagesareservedwith
matchestheunderlyingeventstructureandgenerallyimproves
vLLM for high-throughput inference (temperature 0.90,
transition-andrank-relatedstatistics.Amongthefixed-interval
top-p 0.95, max tokens 1024, max context length 8192).
baselines, GRU/LSTM/Transformer capture some location-
frequency patterns reasonably well, whereas adversarial train-
E. Aggregation-level Spatiotemporal Statistics
ing(SeqGAN)ismoresensitivetooptimizationinstabilityand
TableIIreportsthetrajectorygenerationperformanceunder can degrade fidelity on both spatial and temporal metrics.
aggregation-level spatiotemporal statistical metrics. Overall,
F. Anomaly-Detection Evaluation
TrajGenAgent achieves the strongest spatial alignment across
both datasets: it consistently attains the lowest divergence Table III reports anomaly-detection results under a bal-
on distance-based metrics (Distance, G-radius) and improves ancedgenerated-vs-realsplit,whereAUROC/APcloserto0.5
global transition realism (Transition), highlighting the ben- indicates lower separability and thus better semantic coher-
efit of inference-time spatiotemporal grounding with peer- ence. Since ICAD is prediction-based, it naturally supports
augmented individualized evidence and distance-/kinematics- evaluation at both the visit-level and the individual-level,
aware priors. On MobilitySyn, TrajGenAgent is near-perfect whereas BeSTAD is designed for individual-level behavioral
on most location- and transition-related metrics (Distance, G- shift detection and is therefore reported at the individual-level
radius, DailyLoc, I-rank/G-rank, and Transition), indicating only. Because anomaly detectors operate on POIs and activity

<!-- page 10 -->

types, we focus on the three strongest visit-wise trajectory quality while avoiding costly parameter updates by inject-
generators without location grids, which means they can be ing fine-grained spatiotemporal evidence at inference time
directly mapped to POI/GPS coordinates without introducing throughadeterministic,verifier-guardedworkflow.Suchtrans-
coarse grid inversion artifacts: Geo-CETRA, Geo-Llama, and ferability is particularly valuable for transfer to new cities
TrajGenAgent. or mobility regimes, where patterns shift and repeated fine-
On NumoSim, which has richer underlying spatiotemporal tuning is impractical under limited budgets. Among advanced
dynamics and a stronger activity type diversity, TrajGenAgent baselines, Geo-CETRA is relatively efficient by combining
consistently yields AUROC/AP values closest to 0.5 across rule-based decomposition of visit-wise movement constraints
bothdetectors,indicatingthatitsgeneratedtrajectoriesarethe with an efficient Transformer backbone, yielding moderate
hardest to distinguish from real ones. Geo-Llama is generally GPU hours with competitive quality. In contrast, Geo-Llama
strongerthanGeo-CETRA,butbothremainsubstantiallymore attainsstrongspatiotemporalfidelityviafine-tuning-drivense-
separable than TrajGenAgent under ICAD’s fine-grained spa- quence modeling over structured tokens, incurring the highest
tiotemporalscrutinyandBeSTAD’sindividual-levelbehavioral compute among the strong baselines. SeqGAN is the least
shift detection. These results align with our design goal: cost-effective: adversarial training and Monte-Carlo rollout-
inference-time spatiotemporal grounding with individualized based reward feedback dominate runtime, leading to very
evidence and kinematics-aware priors can preserve semantic high GPU hours despite a lightweight generator and weaker
plausibility while avoiding systematic artifacts detectable by performance. For naive baselines, GRU/LSTM are the most
anomaly models. compute-efficient but deliver weaker fidelity, while the vanilla
On MobilitySyn, which has simpler underlying mobility Transformerimprovesfidelityatahighertrainingcost,reflect-
patternsandfeweractivitytypes,resultsaremoremixed.Geo- ing the standard capacity–efficiency trade-off. Taken together,
LlamaisclosesttochanceunderBeSTAD,whileGeo-CETRA theseresultshighlightthatTrajGenAgentachievescomparable
attains the best (closest-to-0.5) ICAD visit-level scores; Tra- orbetterqualitythanfine-tunedLLMswithsubstantiallylower
jGenAgent remains competitive and achieves the strongest end-to-end compute, narrowing the apparent gap between low
ICAD individual-level AP, suggesting improved individual- compute cost and high generation fidelity.
level behavioral stability under ICAD. We conjecture that
on simpler simulation dynamics, direct fine-tuning on struc- Model GRU TrajGenAgent LSTM Transformer
GPUHours(↓) 1.25 1.67 1.83 3.17
tured tokens (Geo-Llama) or end-to-end neural approach with
Model Geo-CETRA SeqGAN Geo-Llama
rule-based decomposition of visit-wise movement constraints
GPUHours(↓) 3.38 20.62 24.77
as priors (Geo-CETRA) can already obscure many detector
TABLE IV: Average computational cost per dataset on a
cues, while the strength of TrajGenAgent in evidence-driven
singleNVIDIAH100GPU,includinggenerating34,000daily
semantic planning and kinematics-aware grounding are more
trajectories and training with the same number if required.
pronounced on richer, behaviorally more diverse datasets.
BeSTAD ICAD(Visit-level) ICAD(Individual-level) H. Tool-InvocationStability:DeterministicWorkflowvs.Free-
Dataset Model (→0.5) (→0.5) (→0.5)
AUROC AP AUROC AP AUROC form Tool Calling
Geo-CETRA 0.5767 0.7234 0.6414 0.7806 0.8821
NumoSim Geo-Llama 0.3375 0.7046 0.6057 0.7888 0.8962 We further evaluate tool-invocation stability with a simpli-
TrajGenAgent 0.5008 0.5255 0.5368 0.5690 0.6398 fied spatiotemporal grounding setting to justify our use of
Geo-CETRA 0.8192 0.4668 0.5435 0.7934 0.7314
MobilitySyn Geo-Llama 0.5025 0.5885 0.5969 0.7283 0.6629 deterministic workflow execution instead of zero-shot free-
TrajGenAgent 0.6817 0.6318 0.6761 0.6342 0.7194 form tool calling. Specifically, we fix the activity chains
TABLE III: Trajectory generation performance under and evaluate only Stage-2 spatiotemporal grounding, where
BeSTAD and ICAD anomaly detection. With balanced split each daily trajectory contains seven activities. This grounding
(pos/neg=0.5), AP and AUROC closer to 0.5 is better. process is sequentially dependent: the POI selected for the
current visit affects travel-time estimation, the resulting end
G. Computational Efficiency time determines the next visit’s start time, and both variables
Table IV summarizes the end-to-end computational cost condition subsequent POI and time decisions. Therefore, a
under a unified setting, with all timings measured on a single single missing or malformed tool call can break downstream
NVIDIA H100 GPU with maximized memory utilization. state variables and cause cascading failures. Both variants
For parameter-updated baselines, the reported cost includes use the same Qwen2.5-32B-Instruct backbone and a
training plus inference; for TrajGenAgent, which performs simplified two-tool interface, location and time, which
zero-shot generation without parameter updates, it includes gives the free-form variant a favorable setting by minimizing
only inference-time generation. In both cases, the workload tool-selection complexity. The free-form variant receives the
uses the same scale: 34,000 historical daily trajectories from activity chain, tool schemas, and a semantic instruction to
1,200 individuals are used as the training set or historical convert the chain into a complete trajectory, and the LLM
evidence,andeachmethodgenerates34,000dailytrajectories. autonomously decides when and how to invoke tools. In
Overall, TrajGenAgent offers a strong cost–quality trade- contrast, our workflow-managed variant executes the same
off: it matches or slightly exceeds Geo-Llama in generation grounding task under a fixed state-machine order. Although

<!-- page 11 -->

Tool-calling strategy Traj.-level success↑ Visit-level success↑ T=0.5 T=0.9 T=1.5
Total↓ Schema↓ Constr.↓ Total↓ Schema↓ Constr.↓ Total↓ Schema↓ Constr.↓
Free-formtoolcalling 9.8% 59.3% Avg.FR(%) 14.3% 1.8% 12.5% 9.1% 3.6% 5.5% 28.3% 15.2% 13.1%
Deterministicworkflow 100.0% 100.0% TABLE VIII: LLM verifier-triggered failure rates (FR) under
different sampling temperatures T (averaged across datasets).
TABLEV:Tool-invocationstabilitycomparisonbetweenfree-
form tool calling and deterministic workflow execution under
of ICAD/BeSTAD. This confirms that physics-/kinematics-
fallback-enabled setting.
informedtravel-timepropagationhelpsmaintaincoherenttem-
poral progression and behavior-level plausibility beyond what
tool-call fine-tuning with scenario–tool–JSON traces can im-
aggregate metrics alone reveal. More broadly, the ablation
proveautonomousinvocation,itintroducesadditionaldataand
highlights a core advantage of our workflow-managed agent
training costs and may require a smaller backbone under the
design: specialized constraints and domain modules can be
same hardware budget. We therefore compare against zero-
plugged in or removed flexibly, which is challenging for end-
shot free-form tool calling using the same backbone without
to-end approaches.
fine-tuning.
To avoid early termination after a failed call, the tools in-
J. Parameter Study: LLM Sampling Temperature Impacts
clude default-value fallbacks that allow the grounding process
to continue. These fallbacks only keep later visits executable, TableVIIIreportsverifier-triggeredfailureratesunderthree
butmaystillintroduceinaccuratestatevariablesthatpropagate sampling temperatures (averaged across datasets). We mark a
through subsequent grounding steps. Table V therefore re- daily run as failed if either Stage 1 (activity chain) or Stage 2
portsinvocationsuccessunderthisfallback-enabledexecution (duration) LLM output violates the required schema or basic
setting. Trajectory-level success requires that all visits in feasibility constraints (e.g., chain length/duration bounds).
a daily trajectory complete the required location and time Schema failures increase monotonically with temperature,
calls without fallback-induced substitution. Visit-level success as higher T flattens the token distribution and destabilizes
measures the fraction of visits in which the required calls structuredoutputs.Constraintfailuresarenon-monotonic:very
are completed. Even under this simplified setting, zero-shot low T is mode-seeking and can repeat typical but infeasible
free-form tool calling falls short of a practically usable level valuesunderbudget/boundchecks,whileveryhighT induces
of tool-invocation stability for sequential grounding, whereas out-of-bound or implausible samples; T = 0.9 provides the
deterministic workflow achieves perfect invocation with ex- best balance and the lowest overall failure rate.
plicitly predefined control flow and state dependencies.
V. CONCLUSION
NumoSim MobilitySyn
Metric(↓)
TrajGenAgent w/okin. TrajGenAgent w/okin.
We presented TrajGenAgent, a zero-shot, semantic-aware
Distance 0.0006 0.0028 0.0000 0.0000
G-radius 0.0993 0.1508 0.0051 0.0004 hierarchicalLLM-agentframeworkforhumanmobilitytrajec-
Duration 0.0155 0.0198 0.1308 0.3732 torygeneration.ItcouplesanorchestratorLLMforindividual-
DailyLoc 0.2117 0.2476 0.0000 0.0000
and weekday-conditioned activity chain planning with a de-
I-rank 0.0002 0.0006 0.0003 0.0001
G-rank 0.0002 0.0006 0.0003 0.0001 terministic, verifier-guarded worker workflow for kinematics-
Transition 0.0075 0.0077 0.0000 0.0000 aware spatiotemporal grounding via inference-time tool in-
TABLE VI: Ablation study of TrajGenAgent on kinematics tegration (without fine-tuning or parameter updates). Across
design with aggregation-level spatiotemporal statistical met- both large-scale simulation datasets, TrajGenAgent consis-
rics. tently outperforms baselines under complementary evalu-
ations, including traditional spatiotemporal statistical met-
rics and our anomaly-detection-based semantic-aware metrics
Metric NumoSim MobilitySyn (ICAD/BeSTAD).
TrajGenAgent w/okin. TrajGenAgent w/okin.
BeSTAD Despite the promising results, several limitations suggest
AUROC(→0.5) 0.5008 0.5104 0.6817 0.7400 directions for future work. Our temporal grounding relies
ICAD(Visit-level)
AP(→0.5) 0.5255 0.6692 0.6318 0.7143 on retrieval-driven priors and bounded constraints; even aug-
AUROC(→0.5) 0.5368 0.6483 0.6761 0.6827 mented with LLMs, achieving highly accurate, individual-
ICAD(Agent-level)
specifictemporalmodelingremainschallengingandmotivates
AP(→0.5) 0.5690 0.9034 0.6342 0.9922
AUROC(→0.5) 0.6398 0.9143 0.7194 0.9925 stronger constraint-aware neural temporal modules. In addi-
tion, our verifiers mainly enforce structural validity and feasi-
TABLEVII:TheKinematicsAblationstudyofTrajGenAgent
bility, offering limited semantic-quality feedback for iterative
under BeSTAD and ICAD anomaly detection.
refinement; incorporating evaluator-in-the-loop signals could
better guide the refinement of activity chains and temporal
I. Ablation Study: Kinematics-aware Grounding
schedules. We hope these directions will further strengthen
Tables VI and VII show that the kinematics-aware mod- workflow-based LLM agents for semantically coherent and
ule is a key contributor to TrajGenAgent: removing it de- physically plausible human mobility trajectory generation at
grades mobility pattern fidelity especially under the scrutiny scale.

<!-- page 12 -->

ACKNOWLEDGMENTS produce and distribute reprints for Governmental purposes,
notwithstandinganycopyrightannotationthereon.Disclaimer:
Research supported by the Intelligence Advanced Re-
The views and conclusions contained herein are those of the
search Projects Activity (IARPA) via the Department of In-
authorsandshouldnotbeinterpretedasnecessarilyrepresent-
terior/Interior Business Center (DOI/IBC) contract number
ing the official policies or endorsements, either expressed or
140D0423C0033. The U.S. Government is authorized to re-
implied, of IARPA or the U.S. Government.

<!-- page 13 -->

REFERENCES canteachthemselvestousetools,”inAdvancesinNeuralInformation
ProcessingSystems,2023.
[1] T.Hu,S.Wang,B.She,M.Zhang,X.Huang,Y.Cui,J.Khuri,Y.Hu,
[20] J. Zhang, T. Lan, M. Zhu, Z. Liu, and C. Xiong, “xLAM: A family
X.Fu,X.Wangetal.,“Humanmobilitydatainthecovid-19pandemic:
of large action models to empower ai agent systems,” 2024, https://
characteristics, applications, and challenges,” International Journal of
huggingface.co/Salesforce/Llama-xLAM-2-8b-fc-r.
DigitalEarth,vol.14,no.9,pp.1126–1147,2021.
[21] J.WangandZ.Duan,“Agentaiwithlanggraph:Amodularframework
[2] R.A.Becker,R.Caceres,K.Hanson,J.M.Loh,S.Urbanek,A.Var-
forenhancingmachinetranslationusinglargelanguagemodels,”2024,
shavsky, and C. Volinsky, “A tale of one city: Using cellular network
arXivpreprint;LangGraphframeworkformodularagentorchestration.
dataforurbanplanning,”IEEEPervasiveComputing,vol.10,no.4,pp.
[22] B.Azarijoo,M.D.Siampou,J.Krumm,andC.Shahabi,“Icad:Aself-
18–26,2011.
supervisedautoregressiveapproachformulti-contextanomalydetection
[3] Y. Chen, C. Hu, and J. Wang, “Human-centered trajectory tracking inhumanmobilitydata,”inProceedingsofthe33rdACMInternational
controlforautonomousvehicleswithdrivercut-inbehaviorprediction,” ConferenceonAdvancesinGeographicInformationSystems,2025,pp.
IEEETransactionsonVehicularTechnology,vol.68,no.9,pp.8461–
595–606.
8471,2019.
[23] J. Xie, J. Kim, Y.-Y. Chiang, L. Zhao, and K. Shafique, “Bestad:
[4] M.e.a.Mokbel,“Mobilitydatascience:Perspectivesandchallenges,”
Behavior-awarespatio-temporalanomalydetectionforhumanmobility
ACMTrans.SpatialAlgorithmsSyst.,vol.10,no.2,jul2024.[Online].
data,” in Proceedings of the 2nd ACM SIGSPATIAL International
Available:https://doi.org/10.1145/3652158 WorkshoponGeospatialAnomalyDetection,2025,pp.56–59.
[5] D.-T. Le, G. Cernicchiaro, C. Zegras, and J. Ferreira,
[24] N.Pelekis,C.Ntrigkogias,P.Tampakis,S.Sideridis,andY.Theodoridis,
“Constructing a synthetic population of establishments for the
“Hermoupolis:atrajectorygeneratorforsimulatinggeneralizedmobility
simmobility microsimulation platform,” Transportation Research patterns,”inMachineLearningandKnowledgeDiscoveryinDatabases:
Procedia, vol. 19, pp. 81–93, 2016, transforming Urban European Conference, ECML PKDD 2013, Prague, Czech Republic,
Mobility. mobil.TUM 2016. International Scientific Conference on September23-27,2013,Proceedings,PartIII13. Springer,2013,pp.
Mobility and Transport. Conference Proceedings. [Online]. Available:
659–662.
https://www.sciencedirect.com/science/article/pii/S2352146516308560
[25] S. Jiang, Y. Yang, S. Gupta, D. Veneziano, S. Athavale, and M. C.
[6] J. Feng, Z. Yang, F. Xu, H. Yu, M. Wang, and Y. Li, “Learning to
Gonza´lez,“Thetimegeomodelingframeworkforurbanmobilitywithout
simulate human mobility,” in Proceedings of the 26th ACM SIGKDD travelsurveys,”ProceedingsoftheNationalAcademyofSciences,vol.
internationalconferenceonknowledgediscovery&datamining,2020,
113,no.37,pp.E5370–E5378,2016.
pp.3426–3433.
[26] Q. Liu, S. Wu, L. Wang, and T. Tan, “Predicting the next location: A
[7] H.Lin,S.Shaham,Y.-Y.Chiang,andC.Shahabi,“Generatingrealistic recurrentmodelwithspatialandtemporalcontexts,”inProceedingsof
and representative trajectories with mobility behavior clustering,” in theAAAIconferenceonartificialintelligence,vol.30,no.1,2016.
Proceedings of the 31st ACM International Conference on Advances
[27] J.Feng,Y.Li,C.Zhang,F.Sun,F.Meng,A.Guo,andD.Jin,“Deep-
inGeographicInformationSystems,2023,pp.1–4.
move:Predictinghumanmobilitywithattentionalrecurrentnetworks,”
[8] M. Zhang, H. Lin, S. Takagi, Y. Cao, C. Shahabi, and L. Xiong, “Cs- inProceedingsofthe2018worldwidewebconference,2018,pp.1459–
gan:Modality-awaretrajectorygenerationviaclustering-basedsequence
1468.
gan,” in 2023 24th IEEE International Conference on Mobile Data
[28] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley,
Management(MDM). IEEE,2023,pp.148–157.
S.Ozair,A.Courville,andY.Bengio,“Generativeadversarialnetworks,”
[9] K. Ouyang, R. Shokri, D. S. Rosenblum, and W. Yang, “A non- CommunicationsoftheACM,vol.63,no.11,pp.139–144,2020.
parametricgenerativemodelforhumantrajectories.”inIJCAI,vol.18,
[29] L. Yu, W. Zhang, J. Wang, and Y. Yu, “Seqgan: Sequence generative
2018,pp.3812–3817. adversarial nets with policy gradient,” in Proceedings of the AAAI
[10] Q.Long,H.Wang,T.Li,L.Huang,K.Wang,Q.Wu,G.Li,Y.Liang, conferenceonartificialintelligence,vol.31,no.1,2017.
L. Yu, and Y. Li, “Practical synthetic human trajectories generation
[30] Z.Zhou,X.Yang,R.Rossi,H.Zhao,andR.Yu,“Neuralpointprocess
basedonvariationalpointprocesses,”inProceedingsofthe29thACM
forlearningspatiotemporaleventdynamics,”inLearningforDynamics
SIGKDDConferenceonKnowledgeDiscoveryandDataMining,2023,
andControlConference. PMLR,2022,pp.777–789.
pp.4561–4571.
[31] J. Wang, R. Jiang, C. Yang, Z. Wu, M. Onizuka, R. Shibasaki,
[11] W.X.Zhao,K.Zhang,J.Xie,J.Liu,Z.Li,Y.Shan,G.Yang,S.He,
N.Koshizuka,andC.Xiao,“Largelanguagemodelsasurbanresidents:
Z. Wang, Z. Liu et al., “A survey of large language models,” arXiv An llm agent framework for personal mobility generation,” arXiv
preprintarXiv:2303.18223,2023.
preprintarXiv:2402.14744,2024.
[12] S.Li,T.Tran,H.Lin,J.Krumm,C.Shahabi,L.Zhao,K.Shafique,and
[32] J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, and
L. Xiong, “Geo-llama: Leveraging llms for human mobility trajectory
D. Zhou, “Chain of thought prompting elicits reasoning in large
generation with constraints,” in 2025 26th IEEE International Confer- language models,” in Advances in Neural Information Processing
enceonMobileDataManagement(MDM). IEEE,2025,pp.20–31. Systems,2022.[Online].Available:https://arxiv.org/abs/2201.11903
[13] P. Bhandari, A. Anastasopoulos, and D. Pfoser, “Urban mobility as-
[33] O.S.Community,“Gpt-4-oss:Open-source120bparameterllm,”https:
sessment using llms,” in Proceedings of the 32nd ACM International
//huggingface.co/TheBloke/GPT4-OSS-120B, 2024, accessed August
ConferenceonAdvancesinGeographicInformationSystems,2024,pp.
2025.
67–79.
[34] M.P.Armstrong,G.Rushton,andD.L.Zimmerman,“Geographically
[14] Y.Zhang,Y.Hu,andD.Wang,“Astudyonindividualspatiotemporal maskinghealthdatatopreserveconfidentiality,”Statisticsinmedicine,
activity generation method using mcp-enhanced chain-of-thought large
vol.18,no.5,pp.497–525,1999.
languagemodels,”arXivpreprintarXiv:2506.10853,2025.
[35] P. A. Zandbergen, “Ensuring confidentiality of geocoded health data:
[15] W. JIAWEI, R. Jiang, C. Yang, Z. Wu, R. Shibasaki, N. Koshizuka, Assessinggeographicmaskingstrategiesforindividual-leveldata,”Ad-
C. Xiao et al., “Large language models as urban residents: An llm vancesinmedicine,vol.2014,no.1,p.567049,2014.
agentframeworkforpersonalmobilitygeneration,”AdvancesinNeural
[36] X. Wang, X. Liu, Z. Lu, and H. Yang, “Large scale gps trajectory
InformationProcessingSystems,vol.37,pp.124547–124574,2024.
generationusingmapbasedontwostagegan,”JournalofDataScience,
[16] S. Li, T. Tran, L. Zhao, K. Shafique, and L. Xiong, “Towards foun-
vol.19,no.1,pp.126–141,2021.
dation model-based generation of human mobility trajectories,” in The
[37] C. Cao and M. Li, “Generating mobility trajectories with retained
inauguralACMSIGSPATIALInternationalWorkshoponUrbanMobility
datautility,” inProceedings ofthe27th ACMSIGKDD Conferenceon
Foundation,2025,p.22.
KnowledgeDiscovery&dataMining,2021,pp.2610–2620.
[17] E.J.Hu,Y.Shen,P.Wallis,Z.Allen-Zhu,Y.Li,L.Wang,andW.Chen,
[38] Y. Zhu, Y. Ye, S. Zhang, X. Zhao, and J. Yu, “Difftraj: Generating
“Lora:Low-rankadaptationoflargelanguagemodels,”inInternational
gps trajectory with diffusion probabilistic model,” Advances in Neural
ConferenceonLearningRepresentations(ICLR),2022.
InformationProcessingSystems,vol.36,pp.65168–65188,2023.
[18] S.Yao,J.Yu,J.Zhao,K.Narasimhan,O.Etzioni,andY.Choi,“React:
[39] C. Cheng, H. Yang, M. R. Lyu, and I. King, “Where you like to
Synergizing reasoning and acting in language models,” arXiv preprint gonext:Successivepoint-of-interestrecommendation,”inTwenty-Third
arXiv:2210.03629,2022.
internationaljointconferenceonArtificialIntelligence,2013.
[19] T.Schick,J.Dwivedi-Yu,R.Dess`ı,R.Raileanu,M.Lomeli,L.Zettle-
[40] D. Kong and F. Wu, “Hst-lstm: A hierarchical spatial-temporal long-
moyer, N. Cancedda, and T. Scialom, “Toolformer: Language models short term memory network for location prediction.” in Ijcai, vol. 18,
no.7,2018,pp.2341–2347.

<!-- page 14 -->

[41] K.Sun,T.Qian,T.Chen,Y.Liang,Q.V.H.Nguyen,andH.Yin,“Where [48] W.Kwon,Z.Li,S.Zhuang,Y.Sheng,L.Zheng,C.H.Yu,J.Gonzalez,
togonext:Modelinglong-andshort-termuserpreferencesforpoint-of- H. Zhang, and I. Stoica, “Efficient memory management for large
interest recommendation,” in Proceedings of the AAAI conference on languagemodelservingwithpagedattention,”inProceedingsofthe29th
artificialintelligence,vol.34,no.01,2020,pp.214–221. symposiumonoperatingsystemsprinciples,2023,pp.611–626.
[42] Y.Luo,Q.Liu,andZ.Liu,“Stan:Spatio-temporalattentionnetworkfor [49] C. Stanford, S. Adari, X. Liao, Y. He, Q. Jiang, C. Kuai, J. Ma,
next location recommendation,” in Proceedings of the web conference E.Tung,Y.Qian,L.Zhaoetal.,“Numosim:Asyntheticmobilitydataset
2021,2021,pp.2177–2185. with anomaly detection benchmarks,” in Proceedings of the 1st ACM
[43] L.Zhang,Z.Sun,Z.Wu,J.Zhang,Y.S.Ong,andX.Qu,“Nextpoint- SIGSPATIALInternationalWorkshoponGeospatialAnomalyDetection,
of-interestrecommendationwithinferringmulti-stepfuturepreferences.” 2024,pp.68–78.
inIJCAI,2022,pp.3751–3757. [50] S. B. Yoginath, N. Ahmad, C. Gunaratne, L. Amichi, J.-S. Kim,
[44] N. Lim, B. Hooi, S.-K. Ng, X. Wang, Y. L. Goh, R. Weng, and A. Burger, H. Xu, B. Bishnoi, S. C. Christopher, and G. M. Thakur,
J.Varadarajan,“Stp-udgat:Spatial-temporal-preferenceuserdimensional “Ascalablemulti-modalframeworkforhigh-fidelitydistributedhuman
graphattentionnetworkfornextpoirecommendation,”inProceedings mobility simulations,” in Proceedings of the 8th ACM SIGSPATIAL
ofthe29thACMInternationalconferenceoninformation&knowledge InternationalWorkshoponGeospatialSimulation,2025,pp.1–11.
management,2020,pp.845–854. [51] H. Lin, J. Krumm, C. Shahabi, and L. Xiong, “Controllable visit
[45] S.Yang,J.Liu,andK.Zhao,“Getnext:trajectoryflowmapenhanced trajectory generation with spatiotemporal constraints,” in Proceedings
transformer for next poi recommendation,” in Proceedings of the 45th of the 2024 IEEE International Conference on Data Mining (ICDM).
International ACM SIGIR Conference on research and development in IEEE,2024.
informationretrieval,2022,pp.1144–1153. [52] Y.LeCun,L.Bottou,Y.Bengio,andP.Haffner,“Gradient-basedlearning
[46] P. Li, M. de Rijke, H. Xue, S. Ao, Y. Song, and F. D. Salim, applied to document recognition,” Proceedings of the IEEE, vol. 86,
“Large language models for next point-of-interest recommendation,” no.11,pp.2278–2324,1998.
in Proceedings of the 47th International ACM SIGIR Conference on [53] S. Hochreiter and J. Schmidhuber, “Long short-term memory,” Neural
Research and Development in Information Retrieval, 2024, pp. 1463– computation,vol.9,no.8,pp.1735–1780,1997.
1472. [54] A.Vaswani,N.Shazeer,N.Parmar,J.Uszkoreit,L.Jones,A.N.Gomez,
[47] A.Yang,A.Li,B.Yang,B.Zhang,B.Hui,B.Zheng,B.Yu,C.Gao, Ł. Kaiser, and I. Polosukhin, “Attention is all you need,” Advances in
C. Huang, C. Lv et al., “Qwen3 technical report,” arXiv preprint NeuralInformationProcessingSystems,vol.30,2017.
arXiv:2505.09388,2025.
