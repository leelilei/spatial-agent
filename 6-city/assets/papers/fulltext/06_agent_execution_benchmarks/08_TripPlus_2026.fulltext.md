# Extracted fulltext (pdfplumber)

Source: https://arxiv.org/abs/2606.21169
<!-- page 1 -->

Trip+: Benchmarking Agents in Personalized
Interactive Travel Planning
(cid:0)
JunleChen1, WeiChen1,2 , YehongXu1, ZhengjunHuang1, YuqianWu3, ZhoujinTian1,
KaiWang2, LeiWang2, XiaofangZhou1
1HKUST, 2Tencent Hy, 3HKUST(GZ)
Interactive travel planning has become a popular use case for language models. Agents are deployed
to manage evolving preferences and unexpected disruptions over multiple turns. Such settings require
models to make complex, profile-conditioned planning decisions. However, existing benchmarks often
evaluatefeasibility,personalization,orinteractioninrelativelyisolatedsettings. Wethereforeintroduce
Trip+ to measure the ability of agents to plan travel holistically. In Trip+, given traveler profiles and
dynamic interactions, agents must generate and revise minute-level itineraries. End-to-end traveler
experiences are evaluated via an LLM-based simulator, enabling the assessment of subjective metrics
like fatigue. Our scenarios range from simple request resolutions to complex environment-driven
replanning. We evaluate 18 LMs and find a consistent gap in experiential quality. Models favor
technically feasible but exhausting itineraries that diverge sharply from profiled traveler preferences.
Correspondence: jchenkg@connect.ust.hk, onedeanxxx@gmail.com, zxf@cse.ust.hk
https://github.com/junle-chen/trip-plus
Repository:
https://junle-chen.github.io/trip-plus-site/
Website:
Date: June 23, 2026
1 Introduction
As language agents (Anthropic, 2026; OpenAI, 2026a; Google DeepMind, 2026a; Qwen Team, 2026a) move
toward real-world applications, travel planning (Xie et al., 2024) has emerged as a representative task that
goes beyond one-shot execution. Unlike simple question answering, itinerary design naturally unfolds through
multi-turn interactions: travelers refine preferences, introduce constraints, resolve conflicts, and react to
changing travel conditions. This makes travel planning an ideal testbed for personalized agents, requiring
them to maintain itineraries that are executable, profile-aligned, and consistent with accumulated user intents.
Constraints Profiles Experience
Personalization Richness
ssenhciR
noitcaretnI
Figure 1 illustrates the progressive evolution of exist-
ing travel-planning benchmarks along two dimensions:
and . Along Diverse
personalizationrichness interactionrichness
the personalization axis, early benchmarks emphasize
explicit hard requirements and generic itinerary feasibil-
Targeted ity(Xieetal.,2024;Shaoetal.,2024;Zhangetal.,2026),
while more recent work incorporates profile-conditioned
preferences or traveler-experience evaluation (Chaud- One-shot
huri et al., 2025; Cheng et al., 2025; Yang et al., 2025).
Along the interaction axis, benchmarks have progressed
from one-shot itinerary generation to more interactive
settings involving clarification, feedback incorporation,
Figure1 Positioning travel-planning benchmarks for
orreplanning(Chengetal.,2025;Shenetal.,2026;Kar-
agents by personalization and interaction richness.
makar et al., 2025). These advances have substantially
improved the realism of evaluating agents in travel-planning scenarios.
Despite this progress, as agents transition into real-world consumer products, an underexplored frontier
remains: the joint handling of rich personalization and diverse long-horizon interactions. As shown in Table 1,
1
6202
nuJ
91
]IA.sc[
1v96112.6062:viXra

<!-- page 2 -->

Table1 Comparisonoftravel-planningbenchmarksacrosstaskconstruction,evaluation,andresourcedimensions. Rows
are grouped by their primary emphasis. ✓, ✓✗ , and ✗ denote explicit, partial/indirect, and no support, respectively.
Grounding: environments integrated with a verifiable sandbox. Profile: inclusion of distinct user personas. Interaction:
support for multi-turn user engagement. Fine-grained: requires detailed itineraries comprising diverse activities and
transit, bounded by precise start/end timestamps. Feasibility: validates executability through structural completeness,
entity grounding, strict temporal coherence, and accurate budget calculation. StatefulEval.: tests the agent’s ability
to incorporate newly introduced constraints while strictly retaining prior user requirements across turns. UserSim.:
leverages an LLM to role-play the profiled traveler, sequentially experiencing and scoring the fine-grained itinerary
activities. OpenSource: indicates whether data and evaluation code are publicly available.
TaskConstruction Evaluation Resources
Benchmark Grounding Profile Interaction Fine-grained Feasibility StatefulEval. UserSim. OpenSource
Grounded feasibility
TravelPlanner(Xieetal.,2024) ✓ ✗ ✗ ✗ ✓ ✗ ✗ ✓
ChinaTravel(Shaoetal.,2024) ✓ ✗ ✗ ✓✗ ✓ ✗ ✗ ✓
DeepPlanning(Zhangetal.,2026) ✓ ✗ ✗ ✓ ✓ ✗ ✗ ✓
Profile-aware itinerary quality
TripCraft(Chaudhurietal.,2025) ✓ ✓ ✗ ✓ ✓ ✗ ✗ ✓✗
TripTailor(Wangetal.,2025) ✓ ✓✗ ✗ ✓✗ ✓ ✗ ✗ ✓
Travel-Sim(Yangetal.,2025) ✓ ✓ ✗ ✓✗ ✓✗ ✗ ✓ ✗
Interactive replanning
RETAIL(Dengetal.,2025) ✓ ✓✗ ✓ ✓✗ ✓ ✓✗ ✗ ✗
TravelBench(Chengetal.,2025) ✓ ✓ ✓ ✗ ✓ ✓✗ ✗ ✓
TripTide(Karmakaretal.,2025) ✓ ✓✗ ✓ ✓✗ ✓ ✓✗ ✗ ✗
TRIP-Bench(Shenetal.,2026) ✓ ✓✗ ✓ ✓✗ ✓ ✓✗ ✗ ✗
Trip+(ours) ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓
existingtravel-planningbenchmarksfallshortofcomprehensiveevaluation. Profile-aware benchmarks typically
evaluate static preference matching, often neglecting long-horizon interaction and stateful evaluation to test
how agents handle evolving user intents. Conversely, interactive replanning benchmarks frequently focus
on isolated interaction patterns (e.g., asking clarifying questions, incorporating feedback, or performing
isolated replanning), failing to comprehensively capture accumulated preference shifts, emerging conflicts,
environmental disruptions, and their downstream impact on the profiled traveler’s experience. This gap
naturally raises a critical question: How can we evaluate whether travel-planning agents maintain feasible,
traveler-suitable, and intent-consistent itineraries as user needs and travel conditions evolve across turns?
To answer this question, we introduce Trip+, a real-world travel-planning benchmark specifically designed to
evaluate language agents in personalized, multi-turn environments. Trip+ grounds 11 distinct traveler profiles
within a 40-city evidence sandbox, accessible via 11 domain-specific tools (covering attractions, restaurants,
hotels, mobility, intercitytransport, weather, andlocationevidence). Comprising153multi-turninstancesand
570 user turns, the benchmark captures four realistic interaction archetypes: User-State Evolution, Request
Resolution, Environment-Driven Replanning, and Long-Horizon Alignment. At each turn, an agent must
strategically navigate its action space—outputting a Plan, requesting Clarification for conflicting or
missing information, or returning NoSolution when tool evidence proves hard constraints are unsatisfiable.
To rigorously assess these actions, Trip+ employs a comprehensive four-layer evaluation protocol. It first
validates the correctness of the chosen response mode (gating), followed by deterministic checks for itinerary
executability. Stateful rule-based evaluators then verify adherence to requirement satisfaction and cross-turn
intent retention, while a profile-conditioned large language model simulator finally replays the minute-level
execution trace to score the holistic traveler experience (e.g., fatigue, pacing pressure, weather exposure,
budget stress, and preference mismatch). A sampled subset has been reviewed by human experts to ensure
the reliability of judgments. In summary, our contributions are threefold:
• Task Construction. We introduce Trip+, a personalized multi-turn travel-planning benchmark for frontier
language agent model, comprising 153 instances and 570 user turns. It is built from 11 traveler-profile
templates and a fixed 40-city evidence sandbox exposed through 11 domain-specific travel tools, covering
four realistic interaction archetypes.
• Evaluation Setup. We propose a profile- and interaction-aware evaluation protocol that assesses response
mode, feasibility, hard constraints, profile alignment, cross-turn retention, and simulated traveler experience.
2

<!-- page 3 -->

• Findings. Our studies indicate that mere feasibility is insufficient for travel-planning: current agents often
underperform in intention retention, profile matching, and traveler experience across diverse interactions.
2 Trip+: TowardsBenchmarkingProductAgentsforRealUsers
This section describes Trip+ in detail (Figure 2). We first formalize the task (section 2.1), then explain how
task instance is constructed through a sandbox, traveler profiles, and multi-turn interaction (section 2.2).
Besides, wereviewbenchmarkstatistics(section2.3). Finally, weintroduceourevaluationdesign(section2.4).
TaskConstruction Evaluation
Sandbox Environment Traveler Profile
Response Mode
11 diverse Traveler Profiles
Travel Data Sandbox Plan Clarification NoSolution
Backpacker Couples Senior Three-Generation
Intercity Transport Local Mobility POIs Environment Family
...
Three-Generation Family
Itinerary Feasibility
40 diverse cities & dates E Ø nv W iro e n a m th e e n r t a ri l s c k ontext Student Food-first Friends Businessman
Ø Crowd queue risk
... Ø POI Closure
Ø Heat / Cold… Structural Grounded C o h e r ent Transport Cost
Completeness Entities timing evidence consistency
Multi-Turn Interaction
Traveler Profiles Four Diverse Interactions Requirement Satisfaction
Ⅰ User-state evolution Ⅱ Request Resolution Hard constraints Soft Preferences
Base Query requirements evolve across turns o 5 n e P O Da Is y A Ø sk T S i f e r o e n r d io ! c r l C a p o r ro i n f f f i l i c i l c e a t s t i w o i n th b d u a d t g e e s, t , r o re u q te u , i r p e a d r t p y l a s c iz e e s , , , p (p a r c o in f g il , e w -c a o lk n in d g i t b io u n rd e e d n ) ,
We, family of five, 4- Ø Ambiguous (which date) dining… interest coverage…
day Hong Kong trip, Add budgetChange scheduleNew must-visit
must visit Disneyland. Ⅲ Environment-Driven Replanning Ⅲ Ⅳ Long-Horizon Alignment
Profile-Conditioned User Simulation
...
Simulate Experience ü
ü
T
V
r
i
a
si
n
t
sferMinute-Level
DestinationDate,duration New requirementsAmbiguous Disruptions ü Eat… Activities
Sandbox environment Turn 1 Turn 2 Turn 3
Physical Schedule Environmental Budget Preference
Agent Planning Comfort Comfort Comfort Comfort Comfort
Sandbox Interactions: new requirements, ü Sandbox 12345 12345 12345 12345 12345
disruptions, ambiguous … ü Profile-Derived Rules
üIntercity Transport Revision(turn-level) ü Turn state
Tool ü ü L P o O c I a s l Mobility Minute-Level Itinerary ü LLM-as-judge Stateful Multi-Turn Evaluation
üEnvironment 9:00-9:30 hotel->attraction taxi Every turn
Base Query Clarify/NoSolution 9 1 : 2 3 : 0 0 - 0 1 - 2 1 : 2 0 : 0 1 0 a a t t t t r r a a c c t t i i o o n n ->restaurant walk N R ew eq ly u a e d st d f e u d lf i o ll r m re e v n i t sed Int F e o n r t g p et r e o s r e n r o v t a ? tion
Decide Plan 1 … 2:30-13:30 meal Verifier requirement solved?
Figure2 The overall design of Trip+, used to evaluate language agents in complex travel planning scenarios.
2.1 TaskFormulation
Trip+ evaluates multi-turn travel-planning agents in a fixed travel sandbox. At each turn, the agent uses the
visible traveler profile, the dialogue prefix, and tool-retrieved sandbox evidence to choose one of three response
modes: generate a minute-level itinerary, ask for clarification, or return an evidence-backed no-solution
response. The benchmark also maintains hidden turn states only for evaluation.
We formalize each task instance as an agent-visible part and a hidden reference part:
Instance.
x=(xvis,xref),
xvis =(Dtool,pvis,I ),
1:T
xref =(Dref,s ).
1:T
Thevisiblepartxvis consistsofthetool-accessiblesandboxDtool,thevisibletravelerprofilepvis,andturn-level
interaction histories I =(I ,...,I ). Each I =(u ,rˆ ,...,u ,rˆ ,u ) is the dialogue prefix up to turn
1:T 1 T t 1 1 t−1 t−1 t
t, where u and rˆ denote the user utterance and agent response at turn i.
i i
The hidden reference part xref contains two evaluation resources: Dref, which grounds itinerary-feasibility
checks in the fixed sandbox evidence, and s =(s ,...,s ), a sequence of hidden states aligned with the
1:T 1 T
T-turn dialogue.
3

<!-- page 4 -->

Hiddenstate. Each turn t has a hidden state:
s =(m ,H ,Q ,E ),
t t t t t
where m is the expected response mode, H contains hard constraints that apply at turn t, Q contains
t t t
profile-derivedsoftpreferencesrelevanttoturnt,andE containsenvironmentalconditionsthataffectplanning.
t
These fields define the turn-level evaluation targets: response-mode correctness, hard-constraint satisfaction,
soft-preference satisfaction, and environment-aware planning.
Acrossturns,Trip+updatesthehardconstraints,profile-derivedsoftpreferences,andenvironmentalconditions
that remain relevant to the dialogue:
H =(H ∪∆H,+)\∆H,−,
t t−1 t t
Q =(Q ∪∆Q,+)\∆Q,−,
t t−1 t t
E =(E ∪∆E,+)\∆E,−.
t t−1 t t
Here, ∆·,+ denotes newly introduced items, while ∆·,− denotes items that are revised or canceled. Items not
t t
removed remain active in later turns, enabling evaluation of cross-turn retention.
Turn-levelagentbehavior. At turn t, the agent A θ observes the visible context, including the traveler profile
pvis, the interaction histories I , and sandbox evidence R retrieved through tool calls. It returns a response
≤t t
with two components: a response mode mˆ and mode-specific content zˆ:
t t
rˆ =(mˆ ,zˆ)=A (pvis,I ,R ), R ⊆Dtool,
t t t θ ≤t t t
(cid:40)
yˆ, mˆ =Plan,
zˆ = t t
t
η , mˆ ∈{Clar,NoSol}.
t t
Here, η denotes a non-plan response: a clarification question under Clar, or an infeasibility explanation under
t
NoSol. For plan responses, yˆ is an executable itinerary organized by day:
t
yˆ =(d ,...,d ,B), d =(c ,A ,h ),
t 1 D j j j j
A =(a ,...,a ), j =1,...,D.
j j1 jnj
Here, B is the itinerary-level budget summary; c , A , and h denote the city, ordered activities, and
j j j
accommodation for day j. Each activity a records its time interval, type, grounded place or transport item,
jk
movement context, and cost fields. The benchmark evaluates both the selected mode mˆ and the content zˆ
t t
against the hidden state s .
t
2.2 BenchmarkConstruction
Trip+ is constructed in three stages: building a fixed travel data sandbox, defining traveler profiles, and
generating multi-turn interactions, making travel planning realistic and verifiable.
We build a fixed travel sandbox over a diverse set of 40 Chinese cities, covering different
Sandboxconstruction.
destination types, seasons, and local travel conditions. The sandbox provides reproducible evidence for POIs,
hotels, restaurants, weather, local mobility, and intercity transport, together with city-level environmental
context for environment-aware scenarios. Agents access this evidence through 11 domain-specific travel tools,
while evaluators use the same fixed snapshot to verify grounding, feasibility, costs, and environment-aware
planning. Detailed evidence fields and coverage are reported in Appendix A.1, A.2 and A.3.
We construct 11 diverse traveler-profile templates to systematically vary long-
Travelerprofileconstruction.
term user context across planning instances. The templates are designed to cover heterogeneous traveler
needs, including party composition, budget sensitivity, mobility constraints, pace, interests, accommodation
preferences, and travel style. For each instance, we sample an observable profile pvis and provide it to the
agent as user memory. Each observable profile is also mapped to hidden profile-derived rules used only for
evaluation, allowing Trip+ to test whether agents produce plans that are not only feasible but also suitable
for the target traveler. Detailed profile fields and derived rules are provided in Appendix A.4.
4

<!-- page 5 -->

(a) Traveler profiles (b) 40-city sandbox evidence (c) Expected response modes by interaction type
Backpacker 23 In-city transport 7.2M
Family + child 22 Train rows 309K User-state 148
3-gen family 17
Flight rows 38K
Budget st S u e d n e io n r t 13 16 Local places 15K res R o e l q u u ti e o s n t 77 39 1 P Cl l a a r n ification
Cultural explorer 13 Subway stations 7K No-solution
Couple 11 Attractions 7K Environment 120
Friend group 11 replanning
Restaurants 4K
Business 10
Nature lover 9 Hotels 2K Long-horizon 167 14 4
Food-first 8 Weather days 647
0 10 20 103 104 105 106 107 0 25 50 75 100 125 150 175
Figure3 Dataset statistics of Trip+, covering traveler profiles, sandbox evidence, and multi-turn interactions.
We generate multi-turn interactions using a state-first pipeline. For each
Multi-turninteractionconstruction.
turn, we specify a structured hidden state (including state delta, response mode, and evaluation target) before
rendering it as a natural-language user utterance. Specifically:
• Sample a sandbox-grounded seed request. We first sample an executable trip frame from the fixed evidence
sandbox, including the route, dates, trip duration, party size, room count, and intercity transport mode.
We then sample two visible database-backed requirement categories from transport, lodging, dining, and
attractions, with budget added as an extra visible constraint when it fits the sampled traveler.
• Expand into a multi-turn scenario. We expand each seed request using one of four interaction archetypes: I.
User-state Evolution, where user needs (e.g., party composition, budget, schedule) change across turns; II.
Request Resolution, where the agent clarifies or resolves underspecified, conflicting, or infeasible requests;
III. Environment-driven Replanning, where external disruptions (e.g., weather, closures, traffic) require
itinerary revisions; IV. Long-horizon Alignment, where multiple updates are handled while preserving prior
commitments. For each turn, we maintain a hidden state s tracking the expected response mode, active
t
hard constraints, accumulated user updates, and active environment events. We also store the turn delta
and preservation targets to specify current turn changes and the prior commitments that must remain valid.
• Render and validate each turn. Once the hidden turn state and update are fixed, we convert them into the
actual user message shown to the agent. Here, we keep the required entities, numbers, constraints, and
response-mode cues unchanged, discarding any rendered message that omits key details or exposes hidden
reference fields.
2.3 DatasetStatistics
Trip+contains153multi-turninstancesand570userturns. Figure3summarizestheprofile,sandboxevidence,
and interaction coverage. The instances span all 11 traveler profiles (8–23 instances per profile), grounded
in a fixed 40-city sandbox containing 7.2M in-city transport records, 309K train rows, 38K flight rows, and
thousands of places, attractions, stations, restaurants, hotels, and weather records. The turns cover four
interaction archetypes and all three response modes; planning dominates, while clarification and no-solution
cases appear mainly in request-resolution and long-horizon interactions. More distributions of trip duration
and departure month are in Appendix A.1.
2.4 EvaluationProtocol
Each turn in Trip+ is evaluated against its hidden turn state s , which specifies the expected response mode
t
m , active hard requirements H , profile-derived expectations Q , environment conditions E , and items to
t t t t
preserve across turns. Evaluation proceeds in two stages: first, we check if the response follows the expected
mode; for planning turns that pass this mode gate, the remaining evaluation covers operational feasibility,
turn-state satisfaction, profile-conditioned user simulation, and stateful multi-turn evaluation. Specifically:
The mode gate determines whether an agent’s response is eligible for itinerary-level
Response-ModeGating.
evaluation. If the response mode mismatches m , we record a mode error and skip itinerary-level metrics.
t
Itinerary metrics are computed only when m = Plan and the response provides a concrete itinerary;
t
Clarification and NoSolution turns are evaluated by response-mode accuracy instead of itinerary quality.
5

<!-- page 6 -->

Itinerary feasibility measures whether a generated itinerary is executable under the
ItineraryFeasibility.
fixed travel sandbox. The evaluator checks structural completeness, grounded choices (hotels, restaurants,
attractions, transport), temporal coherence, venue opening hours, supported transfers, and cost arithmetic.
This part evaluates whether an executable itinerary satisfies the active user
Requirement Satisfaction.
state at turn t. We separately measure hard-constraint satisfaction and soft-preference satisfaction. Hard
constraintsinH correspondtoexplicituserrequirements(e.g.,dates,destinations,partysize,budget,required
t
lodging/dining/transport); violations indicate request failures. Soft preferences in Q capture profile-derived
t
expectations (e.g., pace, walking tolerance, budget sensitivity, comfort, interests). Both are evaluated by
deterministic rules, treating hard violations as request failures and soft violations as profile-alignment failures.
Profile-ConditionedUserSimulation . Rule-based checks verify whether the generated itinerary yˆ t is feasible,
satisfies hard constraints, and aligns with verifiable soft preferences. However, they cannot model how a
profiled traveler subjectively experiences an itinerary activity by activity, as an otherwise valid plan may
still feel tiring, rushed, or uncomfortable. To capture this, we feed the activity sequences {A }D in yˆ
j j=1 t
to an LLM simulator that evaluates each activity from the traveler’s perspective under active profile and
environmental conditions. It assigns 1–5 scores with brief rationales across applicable dimensions (physical,
schedule, environmental, budget comfort, and preference satisfaction), complementing rule-based metrics by
assessing subjective experiential suitability.
Multi-turn evaluation is stateful, judging each response against hidden turn
StatefulMulti-TurnEvaluation.
states rather than in isolation. The transition from s to s defines the current turn changes, while s
t−1 t t
specifies which hard constraints, soft preferences, and environment conditions remain active. We report two
signals: Request fulfillment verifieswhethertheresponseincorporatesnewturnchanges(addedorrevisedhard
constraints ∆H, soft preferences ∆Q, and environment conditions ∆E); Intent preservation checks whether
t t t
ongoing constraints, preferences, and environment conditions in H , Q , and E remain satisfied. Together,
t t t
they measure the agent’s ability to adapt to updates while retaining prior commitments.
Note, full metric definitions are in Appendix B.
3 Experiments
3.1 ExperimentalSetup
Models and Agent Scaffold. We evaluate 18 Agentic models across frontier families including Gemini, GPT,
Doubao, DeepSeek, MiniMax, Kimi, Hy, and GLM, as well as lightweight families including Gemma, Qwen,
and GLM. Exact model variants are reported in Appendix C.1 and C.2. To focus on the models’ own tool-use
and planning capabilities, all models use the same lightweight OpenAI-compatible function-calling scaffold.
Metrics. We report two groups of metrics. End-to-End Interaction measures turn-level reliability over all
interactions,includingresponse-modeaccuracy,requestfulfillment,andintentpreservation. Valid Plan Quality
evaluates plan outputs that pass the response-mode gate, covering operational feasibility, hard-constraint
satisfaction, profile-conditioned soft preferences and simulated traveler experience. For simulated traveler
experience, we use four fixed profile-conditioned judges from the Qwen, Claude, Gemini, and GPT families
to score each generated plan from the target traveler’s perspective, and take the median as the final value.
AppendixB.6liststheexactjudgeversionsandreportsreliabilityanalyses: pairwiseSpearmanrankalignment,
ensemble-level Cronbach’s α and human rationale verification over 50 sampled cases covering 1,825 activities.
3.2 MainResults
❶CurrentLLMagentsremainunreliableinrealisticmulti-turntravelplanning. Table2showsclearweaknesses
in the interaction: models still make mistakes in deciding whether to plan, ask for clarification, or report
infeasibility, and they often fail to preserve earlier user needs as the dialogue evolves. Gemma-4-31B achieves
the best response accuracy and request fulfillment, while Gemini-3.1-Pro-Preview performs best on intent
preservation. These results suggest that diverse user and environment changes expose interaction-level
failures that are not captured by static planning alone. ❷ Feasible itineraries are not necessarily user-aligned.
6

<!-- page 7 -->

Table2 Main results on Trip+. Models are grouped into frontier and lightweight models. Bold and underline denote
the best and second-best scores in each column. PlanAvg. averages the four valid-plan quality metrics. Win(%) reports
the percentage of non-aggregate metrics on which each model ranks first.
End-to-EndInteraction ValidPlanQuality Summary
Model Resp.Acc. Req.Fulfill IntentPres. Feas. HardCons. SoftPref. UserSim. PlanAvg. Win(%)
Frontier models
Gemini-3.1-Pro-Preview 0.8544 0.7382 0.7697 0.8812 0.9047 0.6389 0.5077 0.7331 42.9
Gemini-3-Flash-Preview 0.8667 0.6885 0.6532 0.7099 0.7179 0.6172 0.4862 0.6328 0.0
GPT-5.4 0.7544 0.5585 0.5489 0.7669 0.8110 0.5854 0.5184 0.6704 14.3
GPT-5.4-Mini 0.7807 0.4879 0.4221 0.6455 0.6126 0.6207 0.5085 0.5968 0.0
GLM-5.1 0.8702 0.7214 0.7301 0.8463 0.7973 0.6136 0.5014 0.6896 0.0
Kimi-K2.6 0.8439 0.6727 0.6811 0.7472 0.7984 0.6380 0.5164 0.6750 0.0
Doubao-Seed-2.0-Pro 0.8246 0.6811 0.6814 0.6731 0.8006 0.6031 0.5128 0.6474 0.0
DeepSeek-V4-Pro 0.7912 0.6657 0.7139 0.6755 0.8375 0.6258 0.5100 0.6622 0.0
DeepSeek-V3.2 0.7702 0.5418 0.5566 0.6461 0.7162 0.5842 0.4755 0.6055 0.0
Hy3-preview 0.8930 0.6708 0.7640 0.7223 0.6476 0.5957 0.4866 0.6130 0.0
MiniMax-M2.7 0.7772 0.5766 0.4921 0.5596 0.6326 0.6076 0.4992 0.5748 0.0
Lightweight models
Gemma-4-31B 0.9035 0.7465 0.7490 0.7427 0.7632 0.5731 0.4923 0.6428 28.6
Gemma-4-26B-A4B 0.8386 0.5989 0.5594 0.6761 0.6925 0.5940 0.4916 0.6136 0.0
Qwen3.5-27B 0.8491 0.6309 0.6218 0.7393 0.7256 0.6375 0.4821 0.6461 0.0
Qwen3.5-122B-A10B-FP8 0.3368 0.2033 0.1028 0.6935 0.7235 0.6319 0.5050 0.6385 0.0
Qwen3.6-27B 0.5649 0.4350 0.3756 0.7521 0.7225 0.6626 0.5167 0.6635 14.3
Qwen3.6-35B-A3B 0.6912 0.4554 0.2463 0.4292 0.4588 0.5839 0.5141 0.4965 0.0
GLM-4-32B 0.5053 0.4656 0.3155 0.5236 0.5605 0.6141 0.4791 0.5443 0.0
0.88
0.80
0.72
1 2 3 4
Turn
erocS
(a) User State (b) Request Resolution (c) Env. Replanning (d) Long Horizon
0.9 0.90
0.88
0.8 0.75
0.80 0.7 0.60
Resp. Acc.
Req. Fulfill
Intent Pres. 0.72 0.6 0.45
1 2 3 1 2 3 1 2 3 4 5
Turn Turn Turn
Figure4 Interaction reliability of Gemini-3.1-Pro-Preview across four multi-turn scenario types. Intent preservation is
omitted at Turn 1 because there is no previous commitment to preserve.
Gemini-3.1-Pro-Previewachievesthestrongestvalid-planquality,rankinghighestinfeasibility,hard-constraint
satisfaction and plan average score. However, softer alignment metrics remain weak: soft-preference scores
are lower, and the best user-simulation score achieved by GPT-5.4 is only 0.5184. This shows that satisfying
explicit constraints is still insufficient for matching users’ implicit preferences and evolving expectations.
4 In-depthAnalysis
Building on the main results in Section 3.2, we focus on Gemini-3.1-Pro-Preview, the strongest overall model
in Table 2, to diagnose two remaining gaps: unreliable interaction and unsuitable plans. We also analyze
inference cost to test whether more computation improves planning performance.
4.1 InteractionReliabilityacrossScenarios
Figure 4 shows that unreliable interaction mainly comes from state-consistent revision rather than response-
mode selection across all four scenarios. ❶ The model handles early updates, but struggles as requirements
7

<!-- page 8 -->

Performance Scores Error Analysis
Rule issue: hard/soft below full score
Date 1.00 Low user simulation score: <0.5 (dissatisfied)
Hotel 0.97
Transport reqs. 24%
Party 0.95
Budget 0.95 Attraction reqs. 17%
Restaurant 0.84 Meal reqs. 10%
Transport 0.82 Party/room reqs. 10%
Attraction 0.81
Comfort and pace 99%
Transport convenience 0.85
Interest match 0.68 Interest match 60%
Budget and value 0.65 Budget and value 31%
Comfort and pace 0.39 Transport convenience 26%
Preference 0.60
Traveler fatigue 97%
Schedule 0.52
Budget 0.50 Environmental exposure 95%
Hard constraint
Physical 0.49 Soft preference Cost stress 75%
Environment 0.43 User simulation Transfer burden 29%
0.0 0.2 0.4 0.6 0.8 1.0 0% 25% 50% 75% 100%
Score Plan-turns with Any Rule Issue or Low User Simulation Score
Figure5 Performance scores and error analysis of Gemini-3.1-Pro-Preview generated plans
accumulate. Response accuracy and request fulfillment initially improve from Turn 1 to 3, indicating that the
model can initially incorporate user-state updates. However, as requirements accumulate, request fulfillment
drops at Turn 4 and intent preservation falls to 0.71, showing that the model struggles to satisfy the growing
set of requirements and begins to forget earlier user requests. ❷ Clarification remains a bottleneck in request
resolution. At the ambiguous Turn 2, Response Accuracy drops temporarily to 0.77, showing that the model
is less reliable when clarification is required. After the ambiguity is resolved, response accuracy recovers, but
final request fulfillment reaches only 0.72. This gap shows that the model can return to the correct response
mode after clarification, but still struggles to apply the clarified requirement when revising the itinerary. ❸
The model detects environment changes, but often revises plans incorrectly. In environment-driven replanning,
response accuracy reaches 0.90, indicating that the model reliably detects when to update the itinerary.
However, Request Fulfillment drops to 0.60 and Intent Preservation to 0.77, demonstrating a clear deficiency
in producing revised plans that satisfy new conditions while preserving past constraints. ❹ Long-horizon
alignment is the hardest scenario. Under accumulated constraints, the ambiguous Turn 3 triggers a severe
performance bottleneck: Response Accuracy drops to 0.78, while Request Fulfillment plummets sharply to
0.41, highlighting the model’s high vulnerability to ambiguous inputs as constraints grow.
Better interaction requires revising plans reliably as constraints grow.
Takeaway1:
4.2 TravelerSuitabilityandFailureModes
We further analyze valid plans generated by Gemini-3.1-Pro-Preview. Figure 5 reports both component
scores and error rates. We observe: ❶ Hard constraints are strong overall, but itinerary-level choices remain
the main failure source. Dates, hotels, party size, and budget are handled reliably, all scoring at or above
0.95. However, constraints that require concrete itinerary decisions are weaker: restaurants, transport, and
attractions score 0.84, 0.82, and 0.81, respectively. These lower scores are reflected in the error rates, with
transport, attraction, and meal requirement errors appearing in 24%, 17%, and 10% of valid plans. ❷ Pace is
the most systematic personalization failure. Among soft preferences, comfort and pace receives the lowest
scoreat0.39. Theerroranalysisshowsthesamepattern: 99%ofvalidplanscontainpace-relatedburden, such
as overly dense schedules, insufficient rest, or tight transitions. This indicates that many feasible itineraries
are still exhausting or poorly paced for the target traveler. ❸ Valid plans still impose substantial experience
burden. Even among valid plans, user-simulation scores fall below 0.5 on key experience dimensions, including
environment, schedule and physical burden. The error analysis shows that these problems are frequent:
traveler fatigue appears in 97% of valid plans, and environmental exposure appears in 95%. This shows that
many valid itineraries are still tiring or environmentally unsuitable for the target traveler.
8

<!-- page 9 -->

Better personalization depends on pacing and burden control.
Takeaway2:
4.3 Cost–PerformanceTrade-off
40
35
30
25
20
15
10
2 4 6 8 10 12
Avg. LLM calls per T1 turn
nrut
1T
rep
sllac
loot
.gvA
Frontier Models: T1 Calls vs. Plan Avg.
Kimi 0.80
GLM-5.1 MiniMax
HY 0.75
GPT-5.4 Gemini Pro 0.70
DS-V4 off-scale (17.3 LLM/52.6 tool calls, 0.716)
0.65
Doubao
0.60
.gvA
nalP
1T
We analyze whether higher inference effort improves
Turn-1 Plan Avg. We use the average number of
LLM calls and tool calls at Turn 1, because the first
turn carries the full planning burden of building the
itinerary, while later turns mainly revise it. Fig-
ure 6 shows no clear monotonic relationship between
cost (LLM/tool calls) and Plan Avg. among fron-
tier models: DS-V4 and Kimi use more calls, while
Gemini Pro achieves the highest Turn-1 Plan Avg.
with moderate usage. We report the task-level cost
analysis across benchmark metrics in Appendix C.3,
which shows the similar pattern. Together, these
Figure6 Turn-1 Inference Cost vs. Plan Average.
results suggest that effective evidence use and plan
construction matter more than simply increasing the number of calls.
Better planning depends on effective evidence use, not more calls.
Takeaway3:
5 RelatedWork
Travel planning is a prime testbed for language agents. Early benchmarks
TravelPlanningBenchmarks.
primarily focused on basic feasibility and structured planning (Xie et al., 2024; Shao et al., 2024; Zhang et al.,
2026). Later works expanded into fine-grained itinerary quality, personalization, and complex interactive
scenarios like disruption-driven replanning (Chaudhuri et al., 2025; Wang et al., 2025; Yang et al., 2025; Deng
et al., 2025; Cheng et al., 2025; Shen et al., 2026; Karmakar et al., 2025). Despite this progress, existing
evaluations lack a unified framework for dynamic contexts and granular experiential feedback. In contrast,
Trip+ differentiates itself by treating the active user state, profile-derived suitability rules, expected response
mode, and activity-level experience trace as jointly constructed oracle fields.
Recent studies Laban et al. (2026) indicate that as agents deploy
User-CenteredInteractiveEvaluation.
into the real world, language models notoriously "get lost in multi-turn conversations," failing to track
long-term user states. To address this, recent benchmarks shift to interactive evaluation: UserBench
tests preference elicitation with simulated users, while τ-bench evaluates tool-mediated interactions under
policy constraints (Qian et al., 2025; Yao et al., 2024). While these works establish baseline capabilities in
conversation tracking, they fall short in physical-world coordination. Trip+ extends this perspective to travel
planning, challenging agents to remain unlost across executable timed itineraries, dynamic environmental
changes, and personalized traveler profiles.
6 Conclusion
We introduce Trip+, a benchmark evaluating travel-planning agents on generating feasible, traveler-suitable,
and intent-consistent itineraries under dynamic user needs and environments. Our evaluation reveals a
clear gap: while current models satisfy basic feasibility and explicit constraints, they struggle significantly
with stateful revisions, user alignment, and effective evidence use. Ultimately, we hope Trip+ drives the
development of agents that plan adaptive, profile-aligned experiences rather than merely executable trips.
9

<!-- page 10 -->

Limitations
While Trip+ provides a realistic setup, it has three primary limitations. First, synthetic queries lack organic
dialogue noise. We utilize them to ensure a reproducible baseline, leaving authentic conversation integration
for future work. Second, fixed evaluation rules may suffer from incomplete coverage, a challenge we leave for
future research on dynamic rule generation. Finally, the LLM as a judge paradigm cannot capture genuine
physical or emotional experiences. We mitigate this using multiple models and human verification, though
authentic human testing remains a crucial next step.
EthicalConsiderations
Trip+isdesignedstrictlyforresearch. Itreliesonafixedsandboxandsyntheticprofiles,posingnoprivacyrisks.
To prevent bias, we treat traveler profiles solely as objective planning constraints rather than demographic
stereotypes. The sandbox mimics actual travel entities, but these are reproducible references rather than
live availability or safety guarantees. Plus, our user simulations serve only as diagnostic signals for itinerary
quality and should never substitute for actual human feedback.
References
Anthropic. Claude fable 5 and claude mythos 5. https://www.anthropic.com/news/claude-fable-5-mythos-5, June
2026.
ByteDance Seed. Seed2.0: Towards intelligence frontier for real-world complexity. https://seed.bytedance.com/en/
seed2, February 2026.
Soumyabrata Chaudhuri, Pranav Purkar, Ritwik Raghav, Shubhojit Mallick, Manish Gupta, Abhik Jana, and Shreya
Ghosh. Tripcraft: A benchmark for spatio-temporally fine grained travel planning. In Proceedings of the 63rd
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 17035–17064,
2025.
Xiang Cheng, Yulan Hu, Xiangwen Zhang, Lu Xu, Zheng Pan, Xin Li, and Yong Liu. Travelbench: A real-world
benchmark for multi-turn and tool-augmented travel planning. arXiv preprint arXiv:2512.22673, 2025.
Lee J Cronbach. Coefficient alpha and the internal structure of tests. psychometrika, 16(3):297–334, 1951.
Alain Decrop and Dirk Snelders. A grounded typology of vacation decision-making. Tourism management, 26(2):
121–132, 2005.
DeepSeek-AI. DeepSeek V4 preview release. https://api-docs.deepseek.com/news/news260424, April 2026.
DeepSeek-AI,AixinLiu,AoxueMei,BangcaiLin,BingXue,BingxuanWang,BingzhengXu,BochaoWu,BoweiZhang,
Chaofan Lin, Chen Dong, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenhao Xu, Chong Ruan, Damai Dai,
Daya Guo, Dejian Yang, Deli Chen, Erhang Li, Fangqi Zhou, Fangyun Lin, Fucong Dai, Guangbo Hao, Guanting
Chen, Guowei Li, H. Zhang, Hanwei Xu, Hao Li, Haofen Liang, Haoran Wei, Haowei Zhang, Haowen Luo, Haozhe
Ji, Honghui Ding, Hongxuan Tang, Huanqi Cao, Huazuo Gao, Hui Qu, Hui Zeng, Jialiang Huang, Jiashi Li, Jiaxin
Xu, Jiewen Hu, Jingchang Chen, Jingting Xiang, Jingyang Yuan, Jingyuan Cheng, Jinhua Zhu, Jun Ran, Junguang
Jiang,JunjieQiu,JunlongLi,JunxiaoSong,KaiDong,KaigeGao,KangGuan,KexinHuang,KexingZhou,Kezhao
Huang, Kuai Yu, Lean Wang, Lecong Zhang, Lei Wang, Liang Zhao, Liangsheng Yin, Lihua Guo, Lingxiao Luo,
Linwang Ma, Litong Wang, Liyue Zhang, M. S. Di, M. Y Xu, Mingchuan Zhang, Minghua Zhang, Minghui Tang,
Mingxu Zhou, Panpan Huang, Peixin Cong, Peiyi Wang, Qiancheng Wang, Qihao Zhu, Qingyang Li, Qinyu Chen,
Qiushi Du, Ruiling Xu, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, Runqiu Yin, Runxin Xu, Ruomeng
Shen, Ruoyu Zhang, S. H. Liu, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shaofei Cai, Shaoyuan Chen,
Shengding Hu, Shengyu Liu, Shiqiang Hu, Shirong Ma, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan,
Songyang Zhou, Tao Ni, Tao Yun, Tian Pei, Tian Ye, Tianyuan Yue, Wangding Zeng, Wen Liu, Wenfeng Liang,
WenjiePang, Wenjing Luo, Wenjun Gao, WentaoZhang, Xi Gao, Xiangwen Wang, Xiao Bi, XiaodongLiu, Xiaohan
Wang, Xiaokang Chen, Xiaokang Zhang, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xingkai Yu,
Xingyou Li, Xinyu Yang, Xinyuan Li, Xu Chen, Xuecheng Su, Xuehai Pan, Xuheng Lin, Xuwei Fu, Y. Q. Wang,
Yang Zhang, Yanhong Xu, Yanru Ma, Yao Li, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Qian, Yi Yu,
Yichao Zhang, Yifan Ding, Yifan Shi, Yiliang Xiong, Ying He, Ying Zhou, Yinmin Zhong, Yishi Piao, Yisong
10

<!-- page 11 -->

Wang, Yixiao Chen, Yixuan Tan, Yixuan Wei, Yiyang Ma, Yiyuan Liu, Yonglun Yang, Yongqiang Guo, Yongtong
Wu, Yu Wu, Yuan Cheng, Yuan Ou, Yuanfan Xu, Yuduan Wang, Yue Gong, Yuhan Wu, Yuheng Zou, Yukun Li,
YunfanXiong,YuxiangLuo,YuxiangYou,YuxuanLiu,YuyangZhou,Z.F.Wu,Z.Z.Ren,ZehuaZhao,ZehuiRen,
Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhibin Gou, Zhicheng Ma, Zhigang
Yan, Zhihong Shao, Zhixian Huang, Zhiyu Wu, Zhuoshu Li, Zhuping Zhang, Zian Xu, Zihao Wang, Zihui Gu, Zijia
Zhu, Zilin Li, Zipeng Zhang, Ziwei Xie, Ziyi Gao, Zizheng Pan, Zongqing Yao, Bei Feng, Hui Li, J. L. Cai, Jiaqi Ni,
Lei Xu, Meng Li, Ning Tian, R. J. Chen, R. L. Jin, S. S. Li, Shuang Zhou, Tianyu Sun, X. Q. Li, Xiangyue Jin,
Xiaojin Shen, Xiaosha Chen, Xinnan Song, Xinyi Zhou, Y. X. Zhu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen
Zhu, Yunxian Ma, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Dongjie Ji, Jian Liang, Jianzhong Guo, Jin Chen,
Leyi Xia, Miaojun Wang, Mingming Li, Peng Zhang, Ruyi Chen, Shangmian Sun, Shaoqing Wu, Shengfeng Ye,
T. Wang, W. L. Xiao, Wei An, Xianzu Wang, Xiaowen Sun, Xiaoxiang Wang, Ying Tang, Yukun Zha, Zekai Zhang,
Zhe Ju, Zhen Zhang, and Zihua Qu. Deepseek-v3.2: Pushing the frontier of open large language models, 2025. URL
https://arxiv.org/abs/2512.02556.
Bin Deng, Yizhe Feng, Zeming Liu, Qing Wei, Xiangrong Zhu, Shuai Chen, Yuanfang Guo, and Yunhong Wang.
RETAIL: Towards real-world travel planning for large language models. In Christos Christodoulopoulos, Tanmoy
Chakraborty,CarolynRose,andVioletPeng,editors,Proceedingsofthe2025ConferenceonEmpiricalMethodsin
Natural Language Processing, pages 14870–14902, Suzhou, China, November 2025. Association for Computational
Linguistics. ISBN 979-8-89176-332-6. doi: 10.18653/v1/2025.emnlp-main.752. URL https://aclanthology.org/
2025.emnlp-main.752/.
Yann Dubois, Balázs Galambosi, Percy Liang, and Tatsunori B Hashimoto. Length-controlled alpacaeval: A simple
way to debias automatic evaluators. arXiv preprint arXiv:2404.04475, 2024.
Google.Gemini3Flash: Frontierintelligencebuiltforspeed.https://blog.google/products-and-platforms/products/
gemini/gemini-3-flash/, December 2025.
Google DeepMind. Gemini 3.1 Pro: Best for complex tasks and bringing creative concepts to life. https://deepmind.
google/models/gemini/pro/, February 2026a.
Google DeepMind. Gemma 4: Our most intelligent open models, built from Gemini 3 research and technology to
maximize intelligence-per-parameter. https://deepmind.google/models/gemma/gemma-4/, 2026b.
Priyanshu Karmakar, Soumyabrata Chaudhuri, Shubhojit Mallick, Manish Gupta, Abhik Jana, and Shreya Ghosh.
Triptide: A benchmark for adaptive travel planning under disruptions. arXiv preprint arXiv:2510.21329, 2025.
Jong-Hyeong Kim, JR Brent Ritchie, and Bryan McCormick. Development of a scale to measure memorable tourism
experiences. Journal of Travel research, 51(1):12–25, 2012.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gonzalez, Hao Zhang,
andIonStoica. Efficientmemorymanagementforlargelanguagemodelservingwithpagedattention. InProceedings
of the 29th symposium on operating systems principles, pages 611–626, 2023.
Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, and Jennifer Neville. Llms get lost in multi-turn conversation. In The
Fourteenth International Conference on Learning Representations, 2026.
Dawei Li, Bohan Jiang, Liangjie Huang, Alimohammad Beigi, Chengshuai Zhao, Zhen Tan, Amrita Bhattacharjee,
Yuxuan Jiang, Canyu Chen, Tianhao Wu, Kai Shu, Lu Cheng, and Huan Liu. From generation to judgment:
Opportunities and challenges of LLM-as-a-judge. In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn
Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on Empirical Methods in Natural Language
Processing,pages2757–2791,Suzhou,China,November2025.AssociationforComputationalLinguistics. ISBN979-
8-89176-332-6. doi: 10.18653/v1/2025.emnlp-main.138. URL https://aclanthology.org/2025.emnlp-main.138/.
MiniMax.MiniMaxM2.7: Modelself-improvement,drivingproductivityinnovationthroughtechnologicalbreakthroughs.
https://www.minimax.io/models/text/m27, March 2026.
Moonshot AI. Kimi K2.6 tech blog: Advancing open-source coding. https://www.kimi.com/blog/kimi-k2-6, February
2026.
OpenAI. GPT-5.5 instant: Smarter, clearer, and more personalized. https://openai.com/index/gpt-5-5-instant/,
May 2026a.
OpenAI. Introducing GPT-5.4. https://openai.com/index/introducing-gpt-5-4/, March 2026b.
OpenAI. Introducing GPT-5.4 mini and nano. https://openai.com/index/introducing-gpt-5-4-mini-and-nano/,
March 2026c.
11

<!-- page 12 -->

Cheng Qian, Zuxin Liu, Akshara Prabhakar, Zhiwei Liu, Jianguo Zhang, Haolin Chen, Heng Ji, Weiran Yao, Shelby
Heinecke, Silvio Savarese, Caiming Xiong, and Huan Wang. Userbench: An interactive gym environment for
user-centric agents, 2025. URL https://arxiv.org/abs/2507.22034.
Qwen Team. Qwen3.5: Towards native multimodal agents. https://qwen.ai/blog?id=qwen3.5, 2026a.
QwenTeam. Qwen3.6-27B:Flagship-levelcodingina27bdensemodel. https://qwen.ai/blog?id=qwen3.6-27b,2026b.
Qwen Team. Qwen3.6-35B-A3B: Agentic coding power, now open to all. https://qwen.ai/blog?id=qwen3.6-35b-a3b,
2026c.
Daniel Scott and Chr Lemieux. Weather and climate information for tourism. Procedia Environmental Sciences, 1:
146–183, 2010.
Jie-Jing Shao, Bo-Wen Zhang, Xiao-Wen Yang, Baizhi Chen, Si-Yu Han, Wen-Da Wei, Guohao Cai, Zhenhua Dong,
Lan-Zhe Guo, and Yu-Feng Li. Chinatravel: An open-ended benchmark for language agents in chinese travel
planning. arXiv preprint arXiv:2412.13682, 2024.
Yuanzhe Shen, Zisu Huang, Zhengyuan Wang, Muzhao Tian, Zhengkang Guo, Chenyang Zhang, Shuaiyu Zhou,
Zengjie Hu, Dailin Li, Jingwen Xu, Kaimin Wang, Wenhao Liu, Tianlong Li, Fengpeng Yue, Feng Hong, Cao Liu,
and Ke Zeng. Trip-bench: A benchmark for long-horizon interactive agents in real-world scenarios, 2026. URL
https://arxiv.org/abs/2602.01675.
Ercan Sirakaya and Arch G Woodside. Building and testing theories of decision making by travellers. Tourism
management, 26(6):815–832, 2005.
Charles Spearman. The proof and measurement of association between two things. 1961.
Jinkun Sun, Jin-He Zhang, Honglei Zhang, Chang Wang, Xiaofang Duan, and Min Chen. Development and validation
of a tourism fatigue scale. Tourism management, 81:104121, 2020.
TencentHyTeam.Hy3preview: Aleadingreasoningandagentmodelinitssize.https://github.com/Tencent-Hunyuan/
Hy3-preview, April 2026.
Karen Thompson and Peter Schofield. An investigation of the relationship between public transport performance and
destination satisfaction. Journal of transport geography, 15(2):136–144, 2007.
KaiminWang,YuanzheShen,ChangzeLv,XiaoqingZheng,andXuan-JingHuang. Triptailor: Areal-worldbenchmark
for personalized travel planning. In Findings of the Association for Computational Linguistics: ACL 2025, pages
9705–9723, 2025.
Paul Williams and Geoffrey N Soutar. Value, satisfaction and behavioral intentions in an adventure tourism context.
Annals of tourism research, 36(3):413–438, 2009.
JianXie,KaiZhang,JiangjieChen,TinghuiZhu,RenzeLou,YuandongTian,YanghuaXiao,andYuSu. Travelplanner:
A benchmark for real-world planning with language agents. arXiv preprint arXiv:2402.01622, 2024.
Dongjie Yang, Chengqiang Lu, Qimeng Wang, Xinbei Ma, Yan Gao, Yao Hu, and Hai Zhao. Wide-horizon think-
ing and simulation-based evaluation for real-world llm planning with multifaceted constraints. arXiv preprint
arXiv:2506.12421, 2025.
Shunyu Yao, Noah Shinn, Pedram Razavi, and Karthik Narasimhan. τ-bench: A benchmark for tool-agent-user
interaction in real-world domains. arXiv preprint arXiv:2406.12045, 2024.
Z.ai. GLM-4-32B-0414. https://huggingface.co/zai-org/GLM-4-32B-0414, 2025.
Z.ai. GLM-5.1: Towards long-horizon tasks. https://z.ai/blog/glm-5.1, April 2026.
Yinger Zhang, Shutong Jiang, Renhao Li, Jianhong Tu, Yang Su, Lianghao Deng, Xudong Guo, Chenxu Lv, and
JunyangLin. Deepplanning: Benchmarkinglong-horizonagenticplanningwithverifiableconstraints. arXivpreprint
arXiv:2601.18137, 2026.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li,
Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging llm-as-a-judge with mt-bench
and chatbot arena, 2023. URL https://arxiv.org/abs/2306.05685.
12

<!-- page 13 -->

Appendix
Trip+: Benchmarking Agents in Personalized Interactive Travel Planning
Table of Contents
A Benchmark Construction Details 13
A.1 Sandbox Data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
A.2 Tool Interface . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
A.3 Environment References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
A.4 Traveler Profile Schema . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
A.5 Base Query and Interaction Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
B Evaluation Metric Details 20
B.1 Response-Mode Gating . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
B.2 Itinerary Feasibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
B.3 Hard Constraint Satisfaction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
B.4 Soft Preference Satisfaction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
B.5 Profile-Conditioned User Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
B.6 User-Simulation Reliability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
B.7 Stateful Multi-Turn Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
C Experiments Details 25
C.1 Model Set . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
C.2 Model Parameters and Serving . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
C.3 Inference Cost Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
D Prompt Templates 27
E Query and Plan Field Examples 33
A BenchmarkConstructionDetails
Thisappendixsectiondocumentstheconstruction-sideartifactsbehindTrip+: thesandboxdata,toolinterface,
environment references, traveler profiles and base query and interaction construction.
A.1 SandboxData
The sandbox data provide a fixed, normalized evidence snapshot shared by agents and evaluators. Agents
access it through tools, and evaluators use it to verify entity grounding, timing, costs, route continuity,
and environment-aware revisions. Price-like fields are reproducible reference costs, not live inventory or
fares. Table 3 summarizes the evidence groups, and Figure 7 shows the departure-month and trip-duration
distributions of tasks.
13

<!-- page 14 -->

60
40
20
0
Nov. Apr. May Jul. Jan.
2025 2026 2026 2026 2027
sksaT
Departure month Trip duration
100
54 83
47 80
60
26
24
40
23
19 18
20
10
2
0
2 3 4 5 6
Days
Figure7 Departure-month and trip-duration distributions of benchmark tasks.
A.2 ToolInterface
Agents interact with the sandbox through 11 OpenAI-compatible tools. Table 4 groups detailed tools by the
evidence they provide.
A.3 EnvironmentReferences
The environment layer stores hidden destination-side references, including climate and seasonal context,
daily weather, local planning conditions, and environment-event triggers. These references support realistic
follow-up turns and let evaluators check whether revised itineraries respond to weather, crowding, traffic,
closures, availability changes, and local constraints. Table 5 summarizes the main reference families and their
use.
A.4 TravelerProfileSchema
Each instance separates traveler information into visible profile cues and hidden evaluation rules. For each
traveler template, we define candidate observable cues, including party composition, budget range, mobility
constraints, pacing preference, interests, and dislikes. We sample instance-specific cues and present them to
the agent as long-term user memory for itinerary planning. The same cues activate hidden profile-specific
Rule IDs for soft-preference evaluation, while the Rule IDs and scoring thresholds are never exposed to the
agent. Table 7 maps observable cues to hidden Rule IDs, Table 8 defines the scoring rubric, and Table 6
summarizes the profile components and their planning/evaluation roles.
Rationale for the soft-preference rubric. The soft-preference rubric is intended as a transparent and repro-
ducible diagnostic of traveler suitability, rather than as a calibrated psychometric model of tourist satisfaction.
Prior tourism research characterizes vacation planning as a contextual, multi-criteria decision process in
which travelers differ in constraints, motivations, decision styles, and trade-offs (Sirakaya and Woodside, 2005;
Decrop and Snelders, 2005). We therefore decompose suitability into separate rule families instead of using a
single global preference score. The rule families correspond to common sources of travel friction: comfort and
pace, local mobility, weather exposure, intercity transport convenience, budget/value, and interest-related
coverage. These dimensions are motivated by prior work on tourism fatigue (Sun et al., 2020), weather and
climate information for tourism (Scott and Lemieux, 2010), public-transport performance and destination
satisfaction (Thompson and Schofield, 2007), perceived value in tourism experiences (Williams and Soutar,
2009), and memorable tourism experiences (Kim et al., 2012).
The1.0/0.5/0.0scoresshouldbeinterpretedascoarseordinaldesignchoicesforbenchmarkevaluation. Ascore
of 1.0 indicates clear alignment with the corresponding traveler preference, 0.5 indicates partial alignment or
mildfriction, and0.0indicatesclearmismatchorsubstantialfriction. Thismiddlelevelisusefulbecausemany
itinerary-qualityissuesaregradedratherthanbinary: forexample, onelongtransferislessseverethanseveral
14

<!-- page 15 -->

Evidencegroup Mainfields Benchmarkrole
Attractions Name; category; coordinates; rating; opening window; POI grounding; opening, duration,
visit duration; ticket cost; popularity and crowd cost, crowd, and interest checks.
signals
Hotels Name; coordinates; star level; price; score; brand; Lodging grounding; room count,
service tags cost,location,andprofile-fitchecks.
Restaurants Name; coordinates; cuisine; opening window; rating; Meal grounding; cuisine, timing,
tags; per-person price cost, and local-route checks.
Local entity index Canonical names; coordinates; addresses; city anchors; Location search; entity resolution;
POI type labels endpoint and cross-file grounding.
Local movement Origin; destination; distance; duration; local reference Transfer feasibility; route
cost continuity; local burden, cost, and
buffer checks.
Subway evidence City file; line; ordered stations; station coordinates Subway paths; station proximity;
when available transit-modeandrail-accessburden
checks.
Weather City; date; condition; temperature; Weather-aware construction;
precipitation-related signals outdoor exposure and replanning
checks.
Intercity transport Endpoints; date; departure/arrival time; duration; Flight/train grounding; timing,
class; availability; price route, class, availability, and
budget checks.
Table3 Public sandbox evidence exposed through Trip+ tools.
Toolfamily Toolnames Planningevidencereturned
Intercity transport query_train_info; Candidate routes with endpoints, schedules,
query_flight_info duration, class, availability, and prices.
Lodging query_hotel_info Hotels with location, star level, price, score, brand,
and services.
Attractions query_attraction_details Attractions with location, category, openings, visit
recommend_attractions duration, ticket cost, rating, popularity, and crowd
risk.
Restaurants recommend_restaurants Restaurants with location, cuisine, openings,
query_restaurant_details rating, tags, and per-person price.
Local movement and search_location Entity coordinates; point-to-point
grounding query_road_route_info distance/duration; route mode; local cost.
query_city
_transport_plan
Weather query_city_weather Daily city weather for tool grounding and
environment-aware planning checks.
Table4 Tool interface exposed to evaluated agents.
very long transfers, and a slightly dense day is less problematic than an itinerary that repeatedly violates the
traveler’s pacing preference. Importantly, the cited tourism studies motivate the evaluated dimensions, but
do not define our exact numerical thresholds. Future work should calibrate these thresholds and dimension
weights with post-trip satisfaction surveys, stated-preference studies, revealed-choice data, human annotation,
and sensitivity analyses across traveler groups.
15

<!-- page 16 -->

Contextsource Storedreference Exampleuse
Climate and season Whetherthedestinationislikelytobehot, Generates weather-related follow-ups
cold, rainy, windy, high-altitude, or season- and checks whether the revised plan re-
sensitive for the trip month. duces risky outdoor exposure.
Local planning conditions Practical city facts that affect planning, Generates local-practical follow-ups and
such as difficult local transfers, long access checks whether the plan adds enough
routes, or places that need extra buffers. transfer or rest buffer.
Daily weather Weather for each city and date: condi- Supportsday-levelreplanning;e.g.,move
tion, temperature range, rain amount, rain outdoor visits away from rainy periods
hours, and location. and add indoor, rest, or buffer blocks.
Environment event refer- Event type, affected city/day/time, trigger Generates event-grounded follow-ups
ences condition,andrequiredenvironment-aware and checks whether the revised plan
response. adapts to weather, crowding, traffic, clo-
sure, or availability changes.
Table5 Hidden environment references for turn construction and evaluation.
Profilecomponent Visibility Roleinevaluation
Party composition Visible Specifies adults, children, and elderly companions; informs
room choice, pace, mobility, and safety checks.
Budget range Visible Captures budget sensitivity; becomes a hard constraint only
when the user states an explicit budget bound.
Accommodation style Visible Guides lodging choice, such as budget, comfort, or luxury
preference.
Mobility and physical Visible Signals walking limits, stroller or elderly needs, weather
tolerance sensitivity, and recovery needs.
Schedule rhythm and Visible Guides late starts, relaxed pacing, rest blocks, and avoidance
rest needs of overpacked days.
Interests and dislikes Visible Guides POI, restaurant, and activity choices; penalizes
disliked patterns such as red-eye travel or repeated costly
meals.
Transport preferences Visible Guides choices among trains, flights, taxis, walking, direct
routes, transfers, and early departures.
Derived profile rules Hidden Map visible traits to evaluable checks for walking burden,
meal timing, rest, budget pressure, weather exposure, POI fit,
and transport burden.
Turn-active profile Hidden Track profile changes introduced during interaction and
deltas determine which expectations remain active after each turn.
Table6 Traveler profile fields used for planning and evaluation.
A.5 BaseQueryandInteractionConstruction
We construct each instance in a state-first manner: the generator first builds a sandbox-grounded base query,
thenexpandsitintooneoffourverifiablemulti-turninteractionscenarios. Table9providesadetailedoverview
of the construction pipeline and the hidden supervision retained for evaluation.
16

<!-- page 17 -->

Profile Candidateobservableprofilecues Comfort/weatherrules Transportrules Budget/interestrules
P01Young moderate/densepace;heat/cold schedule_pacing; transport_avoid_transfer; hotel_value_first;
Backpacker optional;longlocal,red-eye, mobility_accessibility; transport_avoid_red_eye; budget_guarded;
expensivemeal;train/flight; weather_avoid_heat_exposure; transport_prefer_train; budget_tight_cap;
food/nature/shopping/land- weather_avoid_cold_exposure transport_prefer_flight meal_avoid_expensive;
mark interest_local_food;
interest_outdoor_nature;
interest_shopping;
interest_landmark
P02 relaxed/moderatepace;cold schedule_pacing; transport_avoid_transfer; budget_guarded;
Honeymoon optional;longlocalorred-eye; mobility_accessibility; transport_avoid_red_eye; interest_local_food;
Couple early/flight;food,nature,art, weather_avoid_cold_exposure transport_avoid_early_- interest_outdoor_nature;
shopping,landmark departure; interest_art;
transport_prefer_flight interest_shopping;
interest_landmark
P03Three- relaxedpace/rest;elder/child schedule_pacing; transport_avoid_transfer; budget_guarded;
Generation mobility;heat/cold/extreme mobility_accessibility; transport_avoid_red_eye; budget_tight_cap;
Family weather;late/train; weather_avoid_heat_exposure; transport_avoid_late_- interest_local_food;
food/nature/culture weather_avoid_cold_exposure; arrival; interest_outdoor_nature;
weather_need_backup transport_prefer_train interest_culture
P04Family relaxed/moderatepace;child schedule_pacing; transport_avoid_transfer; budget_guarded;
withChild rest,stroller/walk;heat/extreme mobility_accessibility; transport_avoid_red_eye; budget_tight_cap;
weather;late/train;expensive weather_avoid_heat_exposure; transport_avoid_late_- meal_avoid_expensive;
meal; weather_need_backup arrival; interest_local_food;
food/nature/culture/shopping transport_prefer_train interest_outdoor_nature;
interest_culture;
interest_shopping
P05 relaxedpace/rest;elder/walk; schedule_pacing; transport_avoid_transfer; budget_guarded;
Slow-Paced heat/cold/extremeweather; mobility_accessibility; transport_avoid_red_eye; budget_tight_cap;
Senior early/train;food/nature/culture weather_avoid_heat_exposure; transport_avoid_early_- interest_local_food;
Traveler weather_avoid_cold_exposure; departure; interest_outdoor_nature;
weather_need_backup transport_prefer_train interest_culture
P06Cultural moderatepace;coldoptional; schedule_pacing; transport_avoid_transfer; budget_guarded;
Explorer longlocal,red-eye,expensive mobility_accessibility; transport_avoid_red_eye; budget_tight_cap;
meal;train; weather_avoid_cold_exposure transport_prefer_train meal_avoid_expensive;
food/culture/shopping interest_local_food;
interest_culture;
interest_shopping
P07Budget moderate/densepace;heat schedule_pacing; transport_avoid_transfer; hotel_value_first;
Student optional;longlocal,expensive mobility_accessibility; transport_avoid_red_eye; budget_guarded;
Traveler meal,red-eye;train/flight; weather_avoid_heat_exposure transport_prefer_train; budget_tight_cap;
food/nature/culture/shopping transport_prefer_flight meal_avoid_expensive;
interest_local_food;
interest_outdoor_nature;
interest_culture;
interest_shopping
P08Business relaxed/moderatepace;heat schedule_pacing; transport_avoid_transfer; budget_guarded;
Traveler optional;longlocal,red-eye; mobility_accessibility; transport_avoid_red_eye; interest_local_food;
Extending late/flight;food,culture, weather_avoid_heat_exposure transport_avoid_late_- interest_culture;
theTrip shopping,landmark arrival; interest_shopping;
transport_prefer_flight interest_landmark
P09 relaxed/moderatepace;heat schedule_pacing; transport_avoid_transfer; hotel_value_first;
Food-First optional;expensivemeal,long mobility_accessibility; transport_avoid_red_eye; budget_guarded;
Traveler local,red-eye/late;food-centered weather_avoid_heat_exposure transport_avoid_late_arrival budget_tight_cap;
meal_avoid_expensive;
interest_local_food;
interest_outdoor_nature;
interest_culture;
interest_shopping
P10Nature moderate/densepace; schedule_pacing; transport_avoid_transfer; hotel_value_first;
Scenery heat/cold/extremeweather; mobility_accessibility; transport_avoid_red_eye budget_guarded;
Lover direct/red-eye;nature-centered weather_avoid_heat_exposure; budget_tight_cap;
weather_avoid_cold_exposure; interest_local_food;
weather_need_backup interest_outdoor_nature;
interest_culture
P11Friend moderate/densepace;heat schedule_pacing; transport_avoid_transfer; hotel_value_first;
Group optional;longlocal,expensive mobility_accessibility; transport_avoid_late_arrival budget_guarded;
meal;direct/late;food,nature, weather_avoid_heat_exposure budget_tight_cap;
shopping,amusement meal_avoid_expensive;
interest_local_food;
interest_outdoor_nature;
interest_shopping;
interest_amusement
Table7 Observableprofileevidenceandderivedevaluatorrules. Eachrowsummarizespossiblesampledevidenceseedsand
the canonical soft-preference rule IDs they can activate. A concrete query uses one sampled subset; unsupported or
inapplicable rules are skipped before averaging.
17

<!-- page 18 -->

RuleID(s)andcheckedevidence Score1.0 Score0.5 Score0.0
Comfortandpace:schedule,localmobility,andweather
schedule_pacing: maximumdaily Relax: ≤3;Mod: ≤4;Dense: Relax: 4;Mod: 5–6;Dense: 7–8 Relax: ≥5;Mod: ≥7;Dense: ≥9
attractioncount ≤6
schedule_pacing: averagedailyattraction Relax: ≤3;Mod: ≤4 Relax: >3and≤4;Mod: >4 Relax: >4;Mod: >5
count and≤5
schedule_pacing: maximumactiveday Relax: ≤10h;Mod: ≤12h; Relax: 10–12h;Mod: 12–13.5h; Relax: >12h;Mod: >13.5h;
span Dense: ≤14h Dense: 14–16h Dense: >16h
schedule_pacing: earliestdailystart Relax: ≥08:00 Relax: 07:00–08:00 Relax: <07:00
schedule_pacing: latestdailyend Relax/Mod: ≤21:00;Dense: Relax/Mod: 21:00–22:00;Dense: Relax/Mod: >22:00;Dense:
≤22:00 22:00–23:00 >23:00
schedule_pacing: requiredrestblock Relax: present Relax: missingonlightday(<5 Relax: missingonheavyday
attractions) (≥5attractions)
mobility_accessibility: maximum ≤240min 240–300min >300min
within-citytransfertime
mobility_accessibility: long/very-long Route-sensitive: long<2and Route-sensitive: long2–3or Route-sensitive: long≥4or
localtransfers very-long0; very-long1;walking-sensitive: very-long≥2;walking-sensitive:
walking-sensitive: long0and long1–2orvery-long1 long≥3orvery-long≥2
very-long0
mobility_accessibility: dailyoutdoor ≤240min 240–360min >360min
movement
weather_avoid_heat_exposure/ Heat: outdoor11:00–15:00 Heat/coldperiodoutdoor Heat/coldperiodoutdoor>120
weather_avoid_cold_exposure: outdoor ≤90min;cold: outdoorafter 90–120minortotaloutdoor minortotaloutdoor>300min
exposure 18:00≤90min;totaloutdoor 240–300min
≤240min
weather_need_backup: indoor/weather Backupexistsandoutdoor Backupmissingwithnon-high Highoutdoorload(>300min),
backup loadislow(≤240min) outdoorload,oroutdoorload especiallywithoutbackup
240–300min
Transportconvenience:intercitytransfers,timing,andpreferredmode
transport_avoid_transfer: intercity 0transfers 1transfer ≥2transfers
transfercount
transport_avoid_red_eye: late-night Noseverelate-nightsegment 1–2arrivals>21:00,andno Anysegmentstarts<06:00or
intercitytiming andnolatearrival segmentstarts<06:00orends ends>22:00,or≥3arrivals
>22:00 >21:00
transport_avoid_early_departure/ Notimingissueforthe Early-sensitive: 1departure Early-sensitive: ≥2departures
transport_avoid_late_arrival: early/late activesensitivity <07:00;late-sensitive: 1arrival <07:00;late-sensitive: ≥2
timing >21:00 arrivals>21:00
transport_prefer_train/ Atleastonepreferred-mode – Nopreferred-modesegment
transport_prefer_flight: preferredmode segment
Budgetandvalue:hotelpriceandmealcost
hotel_value_first: averagenightlyhotel Avg. nightlyhotel≤city CityP50–P75,ormissingprice >cityP75
price P50
budget_guarded/budget_tight_cap/ Noexpensivemeals Exactlyoneexpensivemeal;no ≥2expensivemeals,orany
meal_avoid_expensive: expensivemeal veryexpensivemeal veryexpensivemeal
count
Interestmatch:profile-themecoverage
interest_local_food/ Profile-themematchesreach Atleastoneprofile-theme Noprofile-themematch
interest_outdoor_nature/ targetcount match,butbelowtarget
interest_culture/interest_art/
interest_shopping/interest_landmark/
interest_amusement: profileinterest
themematch
Table8 Rule-IDsoft-preferencescoringrubric. Each row shows the canonical evaluator rule ID(s), the itinerary evidence
checkedbythatrule,andthedeterministicmappingto1.0,0.5,or0.0. Applicablerulescoresareaveragedwithineach
dimension, and evaluated dimension scores are then averaged. Note: P50/P75/P90 are the 50th/75th/90th city price
percentiles; required places and explicit must-use modes in the query are hard constraints.
18

<!-- page 19 -->

Pipelinestep Turns Code-levelconstructionaction Hiddensupervisionretained
Base-queryconstruction
Tripframe T1source Samplearouteoptionwithorigin,destination, Explicittripconstraintssuchasdate
dates,duration,partysize,roomcount,and range,partysize,roomcount,route
intercitymode;buildthefixedtripcontextusedby mode,andround-triptransport
theinitialrequest. requirements.
Travelerprofile T1source Sampleoneobservabletravelerprofileandderive HiddenprofileRuleIDsandscoring
hiddenprofilerulesfromit. Theobservableprofile basesforsoft-preferenceand
shapestheuser-facingrequestandplanner-visible traveler-experiencechecks;RuleIDsand
memory. thresholdsarenotexposed.
Grounded T1source Samplevisibledatabase-backedrequirementsover Constraintkeys,acceptablecandidates,
requirements transport,lodging,restaurants,andattractions; entityevidence,referencecosts,soft
optionallyaddbudgetandenvironmenthintswhen city/profilewishes,andhidden
theirgatesfire. environmentreferences.
Initialturn T1 Createthefirstturnwithsampled_deltas = Checksthattheinitialplansatisfies
wrapper [initial_request],must_update = [initial_plan],and visiblehardconstraintsandusesthe
therenderedbasequeryasthevisibleuser observableprofilewithoutreading
utterance. hiddenoraclefields.
Multi-turnexpansion
User-state 4turns Appendthree_evolution_deltafollow-upturnsafter Eachturnstoresstate_delta,
evolution T1. Eachturnsamplesadistinctuser-statefamily, must_update,must_preserve,andchecks
suchaspartychange,schedulechange,added suchasupdatedparty/roomcounts,
attraction,restaurantrequirement,hotel addedentities,schedulewindows,budget
requirement,dietaryrestriction,orbudgetupdate. caps,orpreservedhardconstraints.
Requestresolution 3turns Appendtworesolutionfollow-upturnsafterT1. Expectedresponsemodeispartofthe
Thefirstintroducesanambiguity,profile-priority oracle: clarificationforunresolved
conflict,orconflictwithapriorhardconstraint;the ambiguity/conflict,planafterresolution,
secondeitherresolvesthemissinginformation, orno-solutiononlywhentheuser
relaxesaconstraint,orexplicitlyauthorizes explicitlyasksforanimpossibility
no-solution. judgment.
Environment- 3turns Appendtwoenvironmentfollow-upturnsafterT1 Eacheventrecordsfactor,eventtype,
drivenreplanning fromfactorssuchasweatherrisk,crowdorqueue references,expectedadjustments,and
risk,trafficpeak,availabilitychange,transport checksthattheagentacknowledgesthe
disruption,orlocalpracticalconstraint. event,revisestheplan,andpreserves
priorhardconstraints.
Long-horizon 5turns Appendfourfollow-upturnsafterT1: one Theoracleaccumulatesactivehard
alignment user-stateevolutionturn,followedbyresolution, constraints,user-statedeltas,request
environment,orfinal-schedulepressuredepending resolutions,andenvironmentevents,
onthebranch. thencheckswhetherthefinalresponse
appliesallactivestatewhilepreserving
priorcommitments.
Renderingandvalidation
Turnrendering Allturns Rewriteeachrule-generatedturnintoanaturaluser Rejectorfallbackwhentherewriteis
utteranceusingtheprevioususerturnsandthe empty,toolong,losesrequiredanchors,
currentturncontract. Therenderermustpreserve orleaksinternalmarkerssuchas
state_delta,must_update,response-modecues,and state_delta,must_preserve,
literalanchors. verification_oracle,ororaclefields.
Oraclestate Allturns Afterturnsarebuilt,accumulatethehiddenstate Eachturnreceives
update with_with_oracle_state: activehardconstraints, oracle_state_after_turnand
profiledeltas,user-statedeltas,requestresolutions, verification_oracle,whichdefinethe
environmentevents,feasibilitystatus,andresponse evaluationtargetbutareneverexposed
expectation. totheplanner.
Table9 State-first construction pipeline for Trip+ instances. Turn counts start from the initial user request as T1.
Base-query construction creates the grounded travel state, while multi-turn expansion adds code-generated state
deltas, response-mode expectations, preservation targets, and verification oracles. Only rendered user utterances and
observable profiles are exposed to the planner.
19

<!-- page 20 -->

Responsemode Whenthepromptexpectsit Correctresponsebehavior Examplecase
Plan Default for complete requests, Return one complete <plan> The user adds a child,
normal updates, environment with the full updated itinerary: changesthebudget,or
changes, resolved priorities, and transport, lodging, meals, local reports rain; the agent
tool-verifiable revisions. movement, timing, and costs. revises the whole
itinerary.
Clarification Used only for unresolved blocking Return <clarification> asking The user says “change
ambiguity: missing edit target, for the missing decision, the restaurant”
hard-constraint conflict, or conflict priority, or relaxation direction. without a day, meal
with hard profile facts without a Do not invent a full plan. slot, location, or
priority decision. candidate set.
NoSolution Used only when hard constraints Return <no_solution> with the The user says not to
are clear, the user allows a direct grounded blocking reason. Do ask follow-up
impossibility judgment, and tool not include daily plans or reject questions, keeps a
evidence proves no feasible for soft-preference conflict. fixed date and hard
solution. budget, and tool
prices show every
feasible route exceeds
that budget.
Table10 Response-mode gate used before applying itinerary-level metrics.
B EvaluationMetricDetails
This section specifies what each metric reads, what it checks, how it is scored, and which diagnostics are
retainedforaudit. Foritinerary-levelevaluation,generatedPlanresponsesarefirstconvertedintoastructured
execution trace, which we call the converted itinerary. This representation normalizes activities, meals, rest
blocks, transfers, lodging, timestamps, durations, costs, and derived itinerary signals, so that plans can be
checked deterministically and used for simulation.
Aggregationprotocols. Unlessotherwisenoted,model-levelscoresareobtainedbyaveragingthecorresponding
per-turn or per-plan scores over the relevant evaluation set. We use three aggregation protocols:
• End-to-endinteraction. Response-Mode Gating, Request Fulfillment, and Intent Preservation are evaluated
for every turn-level response and averaged over all evaluated turns.
• Valid-planquality. Itinerary Feasibility, Hard Constraint Satisfaction, and Soft Preference Satisfaction are
evaluated only for turns where both the expected and observed response modes are Plan. The reported
score is averaged over these eligible generated plans.
• Usersimulation. User Simulation is computed on the final generated plan of each task and averaged over
tasks.
The subsections below define the corresponding per-turn or per-plan scores before aggregation.
B.1 Response-ModeGating
Response-mode gating is the first step of evaluation. The agent prompt allows exactly three final response
modes: Plan, Clarification, and NoSolution. Let m be the expected response mode and mˆ the
t t
observed response mode for turn t. The turn-level gate score is
R =1[mˆ =m ].
t t t
If the mode is incorrect, the turn is recorded as a response-mode mismatch and downstream valid-plan quality
metrics are skipped. Table 10 summarizes how the response-mode gate defines the applicable conditions,
correct response behavior, and representative examples for each response mode.
20

<!-- page 21 -->

Dimension Subscoresaveragedinsidethe Atomicchecksbehindthesubscores
dimension
Structure completeness Trip duration; route and stay Valid trip duration, closed-loop route
continuity; daily content coverage structure, seamless intercity transfers,
day-boundary continuity, traceable
accommodation, hotel-linked day endings, and
essential meal or attraction coverage.
Evidence validity POI grounding; transport grounding Database-grounded accommodations,
attractions, meals, intercity transport, and
local-move sanity.
Execution operability Time and transfer feasibility; venue Non-overlapping time slots, reasonable
and duration feasibility; intercity transfer time, attraction opening hours,
buffer feasibility; budget arithmetic restaurant service hours, closure days,
attraction and meal duration, required
intercity buffers, and cost calculation
correctness.
Table11 How itinerary feasibility is calculated from atomic checks.
B.2 ItineraryFeasibility
Motivated by verifiable long-horizon travel planning in Zhang et al. (2026), we define itinerary feasibility as
whether a generated trip can be executed in the fixed sandbox. The evaluator applies binary atomic checks
for structural completeness, sandbox grounding, temporal coherence, venue availability, supported transfers,
and cost arithmetic. We group these checks into three dimensions: structure completeness, evidence validity,
and execution operability.
Let z ∈{0,1} denote whether atomic check c passes, and let C be the set of checks under dimension d. The
c d
score of each dimension is the average pass rate of its checks:
1 (cid:88)
D = z .
d |C | c
d
c∈Cd
The final feasibility score is the average of the three dimension scores:
D +D +D
F = structure evidence operability.
p 3
Table 11 lists the atomic diagnostics included in each dimension.
B.3 HardConstraintSatisfaction
Hard constraints are active user requirements that must be satisfied for the response to answer the task.
The evaluator dispatches each normalized hard-constraint key to a deterministic checker and computes the
plan-level pass ratio:
N
H = pass,p.
p N
eval,p
Here N and N denote the number of passed and evaluated hard checks for plan p. Table 12 lists
pass,p eval,p
each hard-constraint dimension, what is evaluated, and the corresponding calculation target.
B.4 SoftPreferenceSatisfaction
Soft preferences are profile-derived, implicit expectations that qualitatively shape a high-quality itinerary
without acting as rigid hard constraints. Their evaluation follows a structured pipeline where the evaluator
maps candidate observable profile cues from a traveler template to hidden soft-rule IDs (Table 7) invisible to
the agent, inspects itinerary evidence to assign fine-grained scores of 1.0, 0.5, or 0.0 (Table 8), and groups
21

<!-- page 22 -->

Hard-constraintdimension Whatisevaluated Calculationtarget
Trip metadata Travel dates, number of days, party Checks that the itinerary has the
size, room count, and hard party facts. required travel dates, number of days,
party size, room count, and hard party
facts.
Intercity mode and tickets Transport mode, route endpoints, date, Checks required transport mode, route
time window, directness, ticket endpoints, date, departure or arrival
number, and seat or cabin class. window, flight or train number, seat or
cabin class, directness, and selected
candidate set.
Accommodation Hotel identity, star level, brand, Checks hotel name, star level, brand,
service, price range, and ranked-choice service, price range, cheapest or
requirements. highest-rated choice, and other visible
lodging requirements.
Dining Required restaurant, nearby anchor, Checks required restaurant, nearby
cuisine, ranking, meal placement, and anchor, cuisine or ranking requirement,
acceptable candidate set. meal placement, and acceptable
restaurant candidate set.
Attractions Required or banned attractions, Checks required or banned attractions,
attraction type, ranking, and attractiontype,rankingrequirement,and
acceptable candidate set. whether selected attractions come from
acceptable database-backed candidates.
Budget Explicit trip budget cap stated by the Checks total plan cost against an explicit
user. budget cap when the user states one;
profile budget range alone is not treated
as a hard budget.
Table12 Hard-constraint dimensions and deterministic calculation targets.
active rules into four preference families: comfort and pace, transport convenience, budget and value, and
interest match. To prevent families with an asymmetrical, dense number of rules from disproportionately
dominating the final metric, we employ a two-step hierarchical aggregation method instead of a naive flat
average. Specifically, the evaluator first averages the rule scores within each active preference family d:
1 (cid:88)
P = score(r),
p,d |R |
p,d
r∈Rp,d
where R denotes the set of active and applicable rules belonging specifically to preference family d for plan
p,d
p. Subsequently, the overall soft preference score P is computed by averaging across all valid families:
p
1 (cid:88)
P = P , A ={d:|R |>0},
p |A | p,d p p,d
p
d∈Ap
where A represents the index set of active preference families that contain at least one applicable rule (i.e.,
p
|R |>0). This family-level aggregation effectively neutralizes rule-density bias, ensuring that all four core
p,d
preference dimensions contribute equitably to the final evaluation score.
B.5 Profile-ConditionedUserSimulation
Following the extraction of deterministic feasibility, hard-requirement, and soft-preference evidence, the
profile-conditioned user simulation evaluates the holistic quality of the generated itinerary. The simulator
ingests a comprehensive context consisting of: (i) the query record and turn state to capture the multi-turn
interactive user intent; (ii) the active user profile defining the traveler’s demographic attributes, physical
constraints, and budget sensitivities; (iii) the city and environmental contexts providing localized external
22

<!-- page 23 -->

Experiencedimension Whatitcaptures Exampleevidence
Physical comfort Whether the itinerary is physically Long walks, long local transfers, high-intensity
manageable for the profiled attractions, early departures, late returns,
traveler. elders, children, stroller needs, low walking
tolerance, high altitude, and missing rest.
Environmental comfort Whether destination conditions Heat, cold, rain, altitude, coastal humidity,
make the itinerary uncomfortable crowd or queue risk, long outdoor exposure,
or risky. and whether the plan uses indoor or
lower-exposure alternatives.
Schedule comfort Whether the traveler has enough Dense activity sequences, short buffers, tight
time and recovery margin. intercity transfers, delayed meals, excessive
waiting, late finishes, and reasonable rest or
recovery slots.
Budget comfort Whether spending creates stress for Explicit budget caps, budget-sensitive profiles,
this traveler. total cost relative to the stated budget,
unexplained expensive choices, and cost
transparency.
Preference satisfaction Whether the executed experience Required places, interest-matched attractions
matches the user’s intended trip. or meals, disliked patterns, repetitive choices,
comfort upgrades, and whether preferred
activities are placed in workable contexts.
Table13 Five rubric dimensions used to report profile-conditioned user simulation.
constraints such as weather conditions and geographic layouts; (iv) the generated itinerary representing the
planning output under appraisal; and (v) the deterministic activity-level experience trace. This trace serves
as the primary factual backbone, providing a fine-grained timeline of the itinerary that chronicles specific
time slots for attraction visits, dining, bus transits, and flights, alongside their corresponding cost fields and
verification metrics.
The simulator evaluates the itinerary across five distinct experience dimensions detailed in Table 13: physical
comfort, environmental comfort, schedule comfort, budget comfort,andpreference satisfaction. Eachapplicable
dimension is scored on a 1–5 rubric according to the explicit qualitative criteria and score anchors defined in
Table 14. Dimensions without meaningful evidence are dynamically excluded from the evaluation to prevent
them from biasing the average toward a default neutral score. The final authoritative normalized score
S ∈[0,1] is derived from these dimensions via:
s¯ −1
S = dim ,
4
where s¯ is the mean 1–5 rubric score computed strictly over the applicable experience dimensions.
dim
B.6 User-SimulationReliability
LLM-as-a-judge is widely used for evaluating open-ended generation and instruction-following tasks (Li et al.,
2025; Dubois et al., 2024), but individual judges can show calibration differences and systematic biases (Zheng
et al., 2023). To reduce dependence on a single judge, we use four diverse LLM judges: qwen3.6-27b, gemini-
3.1-flash-lite, gpt-5.4-nano, and claude-haiku-4-5-20251001. Let s denote the normalized user-simulation
i,j
score assigned to target model i by judge j, where n=18 target models and k =4 judges. We report pairwise
rank alignment and ensemble consistency over model-level user-simulation scores. We further conduct human
rationale verification on 50 sampled itineraries, covering 1,825 activity-level evaluations, to check whether
scores align with rationales and itinerary segments.
23

<!-- page 24 -->

Score Physicalcomfort Environmentalcomfort Schedulecomfort Budgetcomfort Preferencesatisfaction
5 Easymovement; Benignor Relaxedpacing;clear Comfortablywithin Stronginterestmatch;
amplerecovery;fits well-mitigatedweather, buffers;normalmeals budgetorclearly dislikesavoided;
mobilityneeds. exposure,altitude,and andrest. justified. preferredexperiences
crowds. wellplaced.
4 Mostlycomfortable; Minordiscomfort, Mostlysmoothtiming Reasonablespending Mostlyaligned,with
onlyminorexertion reducedbytiming, withsmalltradeoffs. withminorpressure. smallgapsormissed
ortransferburden. indooroptions,orshort opportunities.
exposure.
3 Acceptablebut Noticeablebut Workableschedulewith Budgetevidenceis Acceptablebutonly
visiblytiringor tolerableweather, limitedbuffersor neutral: neither partlyalignedwith
effortful. exposure,altitude,or imperfecttiming. stressfulnor preferences.
crowdburden. comfortable.
2 Poorfit: long Uncomfortable Rushedorfragile Meaningfulstressfrom Weakalignment;
transfers,strenuous conditionsarenot timing;tightlinksor highcostortight genericorrepeated
activity,orlittle handledwell. delayedmeals. margin. mismatches.
rest.
1 Severeburdenor Severeunmanaged Impracticaltiming; Severestress, Clearconflictwith
clear environmentalburden repeatedrushormissed over-budget,or interests,dislikes,or
mobility-profile orrisk. recovery. unjustifiedexpense. tripstyle.
conflict.
Table14 Scoreanchorsforthe1–5profile-conditioneduser-simulationrubric: Ascoreof3indicatesrelevantbutneutral
or acceptable evidence; dimensions with no meaningful evidence are marked inapplicable, not defaulted to 3.
Pairwise Rank Alignment via Spearman’s ρ. As shown in Figure 8(a), we evaluate rank agreement between
judges using Spearman’s rank correlation (Spearman, 1961):
6 (cid:80)n d2
ρ =1− i=1 i,
a,b n(n2−1)
where d is the rank difference assigned to target model i by judges a and b. The ensemble yields an average
i
pairwise ρ=0.652, with the highest agreement observed between Qwen and Gemini (ρ=0.866).
Inter-Rater Consistency via Cronbach’s α. We further report Cronbach’s α (Cronbach, 1951) to measure
ensemble-level internal consistency:
 
α= k 1− (cid:80)k j=1 V
(cid:16)
arn i=1 (s i,j ) (cid:17),
k−1 Varn (cid:80)k s
i=1 j=1 i,j
where Var (·) denotes variance over target models. The ensemble achieves an overall reliability Cronbach’s α
i
of 0.833, as shown in Figure 8(b).
Human Rationale Verification. We audit simulator rationales at the dimension-score level. For each sampled
itinerary event, we inspect the five score–rationale pairs for physical comfort, environmental comfort, schedule
comfort, budget comfort, and preference satisfaction, and verify whether each pair is consistent with the
itinerary segment, traveler profile, cited evidence, and the 1–5 scoring rubric. As shown in Figure 8(c), the
results demonstrate a high overall consistency rate of 93.0%, with preference satisfaction reaching up to 96.5%,
confirming the strong alignment between simulator rationales and human judgments.
The remaining errors are mostly minor boundary or schema issues rather than systematic simulator failures.
For example, one activity starting at 09:02 was treated as an “early start” and assigned a low schedule comfort
score of 2, although this should only indicate mild schedule pressure under our rubric. Some judgments also
24

<!-- page 25 -->

(a) Pairwise Spearman (b) Overall Reliability (c) Human Rationale Verification
0.9
Dimension Consistent
Qwen
Overall 93.0%
0.7 0.833
Gemini Physical comfort 94.3%
Environmental comfort 90.0%
GPT
0.5 Schedule comfort 94.2%
Cronbach's alpha
Budget comfort 89.8%
Claude Good reliability
0.3 4 judges, 18 models Preference satisfaction 96.5%
Qwen Gemini GPT Claude
Figure8 Reliability and verification of the four user-simulation judges used for median aggregation: (a) pairwise
Spearman correlations, (b) overall Cronbach’s alpha, and (c) human rationale consistency.
contain missing or underspecified rationales, and some environmental comfort scores fail to consider weather
exposure when evaluating outdoor attractions or transfer segments. In addition, a few low-cost activities are
penalized under budget comfort without clear evidence that they create actual budget pressure.
B.7 StatefulMulti-TurnEvaluation
Stateful multi-turn evaluation separates adaptation from memory. At each update turn, request fulfillment
measures whether the agent satisfies what the user just added or revised, while intent preservation measures
whether it still satisfies earlier commitments that remain active.
Let U be the set of checks introduced or revised at turn t, including hard constraints, soft preferences, and
t
environment conditions:
U =∆H ∪∆Q∪∆E.
t t t t
The turn-level request-fulfillment score is the pass rate over this current-update set:
(cid:80)
1[pass(u,t)]
F = u∈Ut .
t |U |
t
Let P be the set of earlier hard constraints, soft preferences, and environment conditions that remain active
t
after turn t. Commitments explicitly removed or revised by the user are excluded. Intent preservation is the
pass rate over this preserved set:
(cid:80)
1[pass(p,t)]
I = p∈Pt .
t |P |
t
Final scores average only over turns with non-empty denominators:
1 (cid:88) 1 (cid:88)
F = F , I = I .
|T | t |T | t
F I
t∈TF t∈TI
Here T contains turns with at least one current-update check, and T contains turns with at least one
F I
preserved prior commitment. Turn 1 has no prior commitments, so it is excluded from intent preservation.
Reporting both scores prevents a model from scoring well by only following the newest update or only
preserving the old plan.
C ExperimentsDetails
C.1 ModelSet
We evaluate 18 tool-using LLM agents. The API-served group includes Gemini-3.1-Pro-Preview (Google Deep-
Mind, 2026a), Gemini-3-Flash-Preview (Google, 2025), GPT-5.4 (OpenAI, 2026b), GPT-5.4-Mini (OpenAI,
25

<!-- page 26 -->

Resp. Acc. Req. Fulfill Intent Pres. Feas.
DS-V4: 0.791 DS-V4: 0.666 DS-V4: 0.714 DS-V4: 0.675
Kimi Kimi Kimi Kimi
MiniMax MiniMax MiniMax MiniMax
60 GPT-5.4 GPT-5.4 GPT-5.4 GPT-5.4
Gemini Pro Gemini Pro Gemini Pro Gemini Pro 0.90
40 HY GLM-5.1 HY GLM-5.1 HY GLM-5.1 HY GLM-5.1
0.80
20 Doubao Doubao Doubao Doubao
Hard Cons. Soft Pref. User Sim. Plan Avg. 0.70
DS-V4: 0.838 DS-V4: 0.626 DS-V4: 0.510 DS-V4: 0.662
Kimi Kimi Kimi Kimi
60 GPT-5.4 MiniMax GPT-5.4 MiniMax GPT-5.4 MiniMax GPT-5.4 MiniMax 0.60
Gemini Pro Gemini Pro Gemini Pro Gemini Pro
40 HY GLM-5.1 HY GLM-5.1 HY GLM-5.1 HY GLM-5.1 0.50
20 Doubao Doubao Doubao Doubao
5 10 15 20 25 5 10 15 20 25 5 10 15 20 25 5 10 15 20 25
erocs
cirteM
Avg. LLM calls per task
ksat
rep
sllac
loot
.gvA
Task-Level Inference Cost vs. Benchmark Metrics
DeepSeek-V4 is an outlier: 48.7 LLM / 128.5 tool calls per task
Figure9 Task-level inference cost and planning performance across benchmark metrics
2026c), GLM-5.1 (Z.ai, 2026), Kimi-K2.6 (Moonshot AI, 2026), Doubao-Seed-2.0-Pro (ByteDance Seed, 2026),
DeepSeek-V4-Pro (DeepSeek-AI, 2026), DeepSeek-V3.2 (DeepSeek-AI et al., 2025), MiniMax-M2.7 (Min-
iMax, 2026), and Hy3-preview (Tencent Hy Team, 2026). All API-served models are accessed through
OpenAI-compatible remote endpoints and exposed to the same function-calling interface.
The lightweight/open-weight group includes Gemma-4-31B, Gemma-4-26B-A4B, Qwen3.5-27B, Qwen3.5-
122B-A10B-FP8, Qwen3.6-27B, Qwen3.6-35B-A3B, and GLM-4-32B (Google DeepMind, 2026b; Qwen Team,
2026a,b,c; Z.ai, 2025). These models are served locally with vLLM (Kwon et al., 2023) on 8 NVIDIA A100
80GB GPUs.
C.2 ModelParametersandServing
Allmodelsareevaluatedwithdeterministicgenerationwhenevertheendpointsupportsit. Thedefaultsettings
are temperature 0.0, top-p=1.0, and a maximum of 100 LLM calls per turn.
All target models are exposed to the benchmark through the same OpenAI-compatible function-calling
scaffold. Local vLLM services use tensor parallelism with two to four A100 PCIe 80GB GPUs per model,
bfloat16 inference, a 32,768-token maximum context unless explicitly overridden, prefix caching, chunked
prefill, up to 32 concurrent sequences, and a maximum batched-token budget of 65,536. For local vLLM
models, model-family-specific parsers and chat templates are used only inside the serving layer to translate
model-native outputs into this common interface: Qwen uses the Qwen tool-call parser with thinking disabled,
while Gemma and GLM use Gemma- and GLM-compatible chat templates and tool-call parsers.
C.3 InferenceCostAnalysis
We further examine whether higher inference effort leads to better planning quality. We use average LLM
and tool calls per task as lightweight cost proxies, since each task requires evidence retrieval, itinerary
constructionorrevision,andcross-turnstatetracking. Figure9showsnoclearmonotonicrelationshipbetween
inferencecostandbenchmarkperformanceacrossresponse-mode,constraint-satisfaction,feasibility,preference,
user-simulation, and overall planning metrics.
Higher-cost models do not necessarily produce better plans: DeepSeek-V4 is a clear outlier with 48.7 LLM
calls and 128.5 tool calls per task, yet it is not consistently the best model across metrics (e.g., dropping to
0.510onUserSim.). Kimialsousessubstantiallymoreinferencethanmostotherfrontiermodels, butitsgains
are uneven: it performs strongly on several rule-based metrics but does not dominate user-simulation quality.
26

<!-- page 27 -->

Bycontrast,GeminiProachievesthestrongestoverallplanningqualitywithoutreachingtheextremeinference
costs of the outliers. Furthermore, models like GPT-5.4 and GLM-5.1 demonstrate highly efficient and
competitive performance using roughly half the LLM calls of Gemini Pro and Kimi, while Doubao remains
both low-cost and weak. This suggests that effective evidence use and reasoning matters more than simply
increasing the number of calls.
D PromptTemplates
This appendix lists the agent framework prompt and the profile-conditioned user-simulation prompt used by
the implementation. Each blue box inlines the corresponding prompt text.
Agent Framework Prompt
You are a travel-planning assistant. Use the current user request, the visible traveler profile, and tool results
to return an executable, verifiable, parseable travel response.
The final answer must use exactly one mode: a complete `<plan>`, a complete `<clarification>`, or a complete `<
no_solution>`. Do not output tool-call XML, analysis, drafts, recalculation notes, self-corrections, multiple
budgets, or a plan followed by another conclusion.
================================================================
Workflow
================================================================
1. Decide the response mode first: plan by default; use `<clarification>` or `<no_solution>` only for unresolved
blocking cases listed under Response Modes.
2. Collect the required tool evidence: intercity transport, accommodation, required or candidate attractions,
required restaurants, and the adjacent intracity transfers that will actually appear in the final itinerary.
3. Return the complete final result: once evidence is sufficient, produce one complete `<plan>`; if tool results
rule out an early candidate, update the candidate and output only the final version, not the trial-and-error
process.
================================================================
Core Contract
================================================================
- Satisfy explicit user hard constraints first. The visible profile is for personalization unless it contains hard
facts such as party size, companions, mobility, or safety limits.
- In multi-turn dialogue, previously confirmed hard constraints, profile preferences, environment events, and user
tradeoffs remain active unless the user explicitly cancels, replaces, or relaxes them. The latest turn does
not reset the task.
- Entities, times, prices, routes, and transport facts in the plan must come from tool results. Do not fill gaps
from common knowledge. Query user-named places exactly first.
- All locatable entity names must exactly match tool-returned names, including hotels, attractions, restaurants,
transport hubs, and `travel_city` endpoints. Entity-name fields should contain only the name, not explanatory
text. Put activity purpose or status in the `buffer` description, the `hotel` action, or the scheduled time
instead.
- If the user asks to modify an earlier itinerary, still output the updated complete `<plan>`, not only the edited
fragment.
================================================================
Response Modes
================================================================
Plan directly by default. Use `<clarification>` only for these unresolved blocking cases:
- The latest message is only a local add/change request for an itinerary component, such as dining, attraction,
lodging, or transport, but gives no usable date, time slot, itinerary place, transport node, or candidate set,
so you cannot tell which part should change.
- The latest message introduces a new hard constraint that conflicts with still-active previous hard constraints,
and the user has not stated the priority or relaxation direction.
- The latest message introduces a new hard request that would clearly override hard facts or strong preferences in
the visible profile, such as party composition, children/elders, mobility, safety limits, relaxed pacing,
reduced walking, or recovery needs, and the user has not said whether the new goal or profile comfort has
priority.
Return a complete `<plan>` for complete initial travel requests, normal user-state updates, normal environment
changes, already prioritized or relaxed requests, and any itinerary revision that can be verified and
27

<!-- page 28 -->

executed with tools. When returning a plan, preserve all still-active constraints and preferences from
earlier turns. Decide restaurant anchors, attraction order, hotel area, transport tradeoffs, and rating/price
/opening-hour tie-breaks from tool results; do not ask about these execution details.
For complete initial requests, do not output `<clarification>` for these execution details: whether the stated
room count is really needed, choosing among hotel/apartment/homestay candidates, choosing highest-rated or
cheapest candidates, deciding whether a restaurant can be lunch or dinner from business hours, selecting a
return train/flight time, choosing an imperfect but budget-compatible hotel area, or deriving hotel nights
from explicit dates. If a tool-returned executable candidate exists, choose the candidate that best satisfies
the explicit constraints and output the plan.
Use `<no_solution>` only when all of the following are true:
- The current active hard constraints are clear; no date, place, candidate set, priority, or relaxation direction
is still missing.
- The user has authorized a direct no-solution judgment, such as saying not to ask follow-up questions, not to
silently replace requirements, or not to relax earlier constraints.
- Tool evidence or known constraints prove that the active hard constraints cannot all be satisfied, such as no
available transport on the required date, an explicit budget below the minimum verifiable cost, a required
entity unavailable on the usable date, or a new condition that the user insists on keeping despite conflict
with an active hard constraint.
If the missing piece is required information, priority, or relaxation direction, output `<clarification>`. If the
user has not authorized a direct no-solution judgment, ask which constraint can be relaxed instead of
outputting `<no_solution>`.
Do not output `<no_solution>` because of soft-preference conflict, few candidates, imperfect experience, missing
opening-hour fields, or facts that should be checked with tools. Do not fabricate entities, prices, routes,
business hours, or transport schedules to avoid `<clarification>` or `<no_solution>`.
Entity existence, opening hours, prices, distances, and routes are tool-verification duties, not clarification
reasons. An explicit user budget is a hard constraint; profile `budget_range` is not a hard budget for this
trip.
================================================================
Tool Evidence Requirements
================================================================
- Intercity transport: use `query_flight_info` or `query_train_info`; pass city names as `origin/destination`. The
returned `price` is the complete per-person reference price for the candidate route. For connecting routes,
write each segment with its own number, stations, and times; count the same-day route-level `price` only once
in the budget.
- Accommodation: for overnight trips or room requests, use `query_hotel_info`; for a named hotel/apartment/
homestay, use exact `hotelName`. Planned hotel names and prices must come from the tool.
- Attractions: before scheduling an attraction, use `query_attraction_details` for opening information, duration,
and ticket price. Do not schedule attractions that the tool clearly marks as closed.
- Restaurants: before scheduling a restaurant, use `recommend_restaurants` or `query_restaurant_details`. For a
named restaurant, use details lookup; for eating near a place, use that place only as the restaurant-search
anchor.
- Every `meal` line must contain a specific tool-returned restaurant name and per-person price. Across the
complete itinerary, prefer a different restaurant for each meal, and every restaurant name must come from
tool results, unless the user explicitly asks to revisit one; one restaurant should normally be used for only
one meal. Avoid repeating the same restaurant when possible, and do not use a generic restaurant name. Do
not write breakfast, self-arranged light meals, or rest as ungrounded `meal` entities; use a `buffer` or `
hotel` description when needed.
- Intracity transport evidence: when two adjacent activities in the same city happen at different places, insert a
`travel_city` segment between them and verify its route, duration, distance, and price with tools. Default
to `query_city_transport_plan`, especially for named places or when the user prefers metro/subway, fewer
transfers, less walking, lower cost, or shorter travel time; keep the returned mode/line summary in the final
itinerary. `query_road_route_info` is only a coordinate-level fallback: use `search_location` + `
query_road_route_info` only when you already have two exact coordinates and do not need metro/subway line
planning.
- Pass only necessary tool arguments: dates/times are used only for flights, trains, and weather; do not pass
dates/times to hotels, intracity transport, road routes, attractions, restaurants, or location search. If a
tool call repeats identical normalized arguments, reuse the previous result and continue with necessary new
arguments.
- Weather: for date-specific trips, you may use `query_city_weather`; if tools show clear weather risk, reflect a
reasonable adjustment in the plan.
- Comparative requirements such as cheapest, highest-rated, closest, required cabin/seat class, or time windows
are hard constraints and should be judged within the corresponding tool-returned candidate set.
================================================================
28

<!-- page 29 -->

Planning Rules
================================================================
- Provide a minute-level timeline for actual travel-related activities.
- Time and location must be continuous: use `travel_city` between different places, `travel_intercity_public` for
intercity segments, and `buffer` for procedures, waits, or short rests.
- Activity times must be compatible with transport schedules, opening/business hours, route order, and the visible
profile.
- Meal rules: do not schedule breakfast; assume it is handled at the hotel or before departure, and do not count
breakfast toward required meals. On a full sightseeing day in the destination city, schedule lunch and dinner.
On intercity days, decide meals from the effective time in the destination city: if arriving before 10:00,
schedule lunch and dinner; if arriving 10:00-15:00, schedule dinner and lunch is optional; if arriving after
15:00, schedule no meal or only dinner. If departing the destination before 09:00, schedule no meal in that
city; if departing 09:00-15:00, lunch is optional and dinner should not be scheduled; if departing after
15:00, schedule at least lunch and dinner is optional.
- Meal timing: lunch should preferably fit within 11:00-14:00, and dinner should preferably fit within 17:00-20:00.
Each meal usually takes 1-2 hours. If a day has both lunch and dinner, lunch end and dinner start should be
at least 3 hours apart. Restaurant business hours must cover the corresponding meal slot.
- Non-final days should end at that night's accommodation. Final day uses `Accommodation: -`.
- Before flights, write a 90-minute airport buffer; after flight arrival, write at least 30 minutes before leaving
the airport. Before trains, write a 30-minute station buffer; after train arrival, write at least 15 minutes
before leaving the station.
- `travel_city` duration should be close to the tool-returned duration. `travel_intercity_public` times must match
tool results. Attraction duration must fall within the tool-returned range.
================================================================
Output Format
================================================================
<plan>
Day [Day Number] ([YYYY-MM-DD]):
Current City: [from origin city to destination city / city name]
Accommodation: [tool-returned hotel name, ¥positive/room/night; use - on final day]
HH:MM-HH:MM | buffer | [security/waiting; deplaning/exiting; baggage claim; necessary short wait]
HH:MM-HH:MM | travel_intercity_public | [flight/train] [returned number], [returned departure station] - [returned
arrival station], [cabin/seat class], ¥[positive]/person
HH:MM-HH:MM | travel_city | [from] - [to], [taxi/walking/metro lines], [distance], [duration], ¥[price]
HH:MM-HH:MM | attraction | [returned attraction name], ¥[ticket]/person
HH:MM-HH:MM | meal | [lunch/dinner], [returned restaurant name], ¥[per person]/person
HH:MM-HH:MM | hotel | [check-in/check-out/rest], [returned hotel name]
**Budget Summary**:
**Transportation: X RMB**. Intercity tickets = one route-level price per same-day flight/train connection * people.
Intracity transport depends on the tool-returned mode: taxi/cab prices are per vehicle/trip and should be
multiplied by required vehicles (default taxi capacity: 4 people, rounded up); metro/bus/public-transit
prices are per person; walking costs 0.
**Accommodation: X RMB**. Hotel price * room count * nights.
**Meals: X RMB**. Per-person meal prices * people.
**Attractions & Tickets: X RMB**. Ticket prices * people.
**Other: X RMB**
**Total Estimated Budget: X RMB**
</plan>
<clarification>
[Ask one or two short questions naming the missing slot, conflicting constraints, or priority that the user must
confirm.]
</clarification>
<no_solution>
The current hard constraints cannot be jointly satisfied.
Blocking constraints: name the mutually conflicting or impossible user hard constraints.
Tool evidence: cite the key tool results, such as transport, accommodation, required meal, or ticket costs.
To continue planning, the user would need to relax: list at most two relaxation directions.
</no_solution>
29

<!-- page 30 -->

Profile-Conditioned User-Simulation Prompt
# Profile-Conditioned User Experience
You are the traveler described by `EXPERIENCE_TRACE.user_model`. You are now experiencing the itinerary in `PLAN`,
one activity at a time, under the environment and budget conditions in `EXPERIENCE_TRACE.environment` and `
EXPERIENCE_TRACE.budget`.
Describe your activity-level travel experience and score the itinerary's experience quality. Your scores must
follow the 1-5 rubric below.
Base the experience report on `EXPERIENCE_TRACE`. Use `PLAN` only as a raw itinerary reference for the matching
activity position, such as activity name, type, time slot, cost, transport mode, and accommodation. For
example, `D1-A1` maps to `PLAN.daily_plans[0].activities[0]`. Do not use `PLAN` to re-judge entity grounding,
factual validity, route validity, prices, hard constraints, or requirement success.
`EXPERIENCE_TRACE.activity_trace[].experience_facts` contains neutral facts, not pre-scored verdicts. Infer
comfort scores from those facts and the rubric. Boolean conditions are represented only as positive `
experience_flags`; absence of a flag means the condition is not evidenced. Do not assume that every cost is
budget stress. Treat minor costs as neutral for that activity; use activity cost for budget discomfort only
when `budget_cost_relevance` is moderate/high. Use near-limit/over-limit budget margin as whole-trip budget
context, not as a reason to penalize every paid activity equally.
Return JSON only. No markdown fences, comments, or extra text.
## Core Rule
Output exactly one `activity_simulations[]` item for each `EXPERIENCE_TRACE.activity_trace[]` item.
Preserve every expected ref exactly once:
```text
EXPERIENCE_TRACE.expected_activity_refs == activity_simulations[].item_ref
```
If evidence is weak or missing, keep the claim neutral or low-confidence and list the missing evidence in `
missing_evidence`.
## Evidence Priority
Use evidence in this order. Later sources may clarify raw fields, but they must not override earlier travel-
experience evidence.
1. `EXPERIENCE_TRACE.activity_trace[]`: one item per planned activity. Each item contains `item_ref`, compact `
event` fields, and neutral `experience_facts` such as duration bucket, positive experience flags, and cost
relevance. Use this as the primary source for every `activity_simulations[]` item.
2. `EXPERIENCE_TRACE.user_model`: the compact traveler profile. It may contain `party`, `comfort_sensitivities`, `
interest_preferences`, and `sensitivity_flags`. Use it only to interpret how this traveler would feel.
3. `EXPERIENCE_TRACE.environment`: destination or trip-context environment signals, such as heat, cold, rain,
exposure, or other risk tags. Use it for environment-related comfort only when connected to an activity.
4. `EXPERIENCE_TRACE.budget`: budget applicability, budget limit when available, estimated total, and margin level.
Use it for `budget_comfort`; set budget dimensions not applicable when budget is not applicable.
5. `PLAN`: compact raw itinerary fields, including `daily_plans[]`, `activities[]`, `accommodation`, and `
budget_summary`. Use it only to confirm raw fields for the matching activity position, where `D{day}-A{
activity_index}` maps to `PLAN.daily_plans[day-1].activities[activity_index-1]`. Do not use it to invent
subjective quality, factual validity, route validity, or hidden preferences.
Do not invent facts that are not in the inputs. For example, do not assume extra rest, sleep quality, delays,
crowds, weather, closures, scenic quality, restaurant quality, health conditions, preferences, or budget
sensitivity.
## Scores
Use a 1-5 scale where higher is better:
- 5: very good, low burden and strongly profile-aligned
- 4: good, minor issues
- 3: acceptable with visible tradeoffs
30

<!-- page 31 -->

- 2: poor, uncomfortable or stressful
- 1: very poor, severe discomfort, stress, or profile conflict
Return these five dimensions:
- `physical_comfort`: walking, transfers, standing, stamina, recovery
- `environmental_comfort`: weather, temperature, rain/snow, exposure, crowds when evidenced
- `schedule_comfort`: early starts, late finishes, tightness, buffers, meal timing, density
- `budget_comfort`: budget pressure from relevant costs or tight budget margin; set `applicable=false` if no
budget cap/sensitivity exists
- `preference_satisfaction`: interests, dislikes, pace, dining, hotel, transport preferences
Use the same dimensions inside every activity's `dimension_updates` and in top-level `experience_dimensions`.
For each activity, include all five dimensions in `dimension_updates`, but set `applicable=false` and `score_1_5=
null` when that activity has no direct evidence for a dimension. Do not fill unrelated dimensions with 3 just
to avoid null. Use score 3 only when a dimension is genuinely relevant and the evidenced experience is
neutral or acceptable.
For top-level `experience_dimensions`, give the traveler's standardized five-dimension judgment for the whole
itinerary or current chunk. Mark a top-level dimension `applicable=false` when there is no meaningful
evidence for that dimension anywhere in the chunk. Cite the key `item_ref` values behind each applicable
dimension.
`llm_reported_overall.dimension_analysis` explains the holistic overall score and may weight activities by trip
importance. `experience_dimensions` are the standardized dimension scores used by the evaluator. Keep both
grounded in cited `item_ref` values.
## Activity Fields
For each activity simulation, include:
- `item_ref`, `day`, `activity_index`
- compact `activity`: `type`, `name`, `time_slot`
- `dimension_updates` for all five dimensions
- one or two grounded `evidence` entries
- `confidence`: `high`, `medium`, or `low`
For each evidence entry, `source` names where the support came from, and `claim` states what that source supports.
Prefer sources from `EXPERIENCE_TRACE`; use `PLAN` only for activity identity, time, and cost verification.
Valid source formats include `EXPERIENCE_TRACE.activity_trace[D1-A1]`, `EXPERIENCE_TRACE.user_model`, `
EXPERIENCE_TRACE.environment`, `EXPERIENCE_TRACE.budget`, and `plan.daily_plans[0].activities[0]`.
Confidence:
- `high`: all important claims are directly supported by trace evidence
- `medium`: evidence-backed but partly indirect
- `low`: missing, weak, vague, or inferred evidence affects the score
Use the lowest confidence triggered by any important activity claim. Do not mark every item `high`.
## Required JSON Shape
Keep free-text fields short: one sentence, preferably under 12 words.
Top-level keys:
```text
llm_reported_overall
profile_summary
activity_simulations
experience_dimensions
missing_evidence
audit_notes
```
Minimal shape:
```json
{
31

<!-- page 32 -->

"llm_reported_overall": {
"score_1_5": 3.0,
"reason": "one short evidence-based explanation",
"dimension_analysis": {
"physical_comfort": {"score_1_5": 3.0, "reason": "", "evidence": ["D1-A1"]},
"environmental_comfort": {"score_1_5": 3.0, "reason": "", "evidence": ["D1-A1"]},
"schedule_comfort": {"score_1_5": 3.0, "reason": "", "evidence": ["D1-A1"]},
"budget_comfort": {"score_1_5": null, "applicable": false, "not_applicable_reason": ""},
"preference_satisfaction": {"score_1_5": 3.0, "reason": "", "evidence": ["D1-A1"]}
},
"authoritative": false
},
"profile_summary": {
"party": {},
"comfort_sensitivities": {},
"interest_preferences": {},
"sensitivity_flags": {},
"profile_uncertainties": []
},
"activity_simulations": [
{
"item_ref": "D1-A1",
"day": 1,
"activity_index": 1,
"activity": {"type": "", "name": "", "time_slot": ""},
"dimension_updates": {
"physical_comfort": {"score_1_5": 3.0, "applicable": true, "reason": ""},
"environmental_comfort": {"score_1_5": null, "applicable": false, "not_applicable_reason": ""},
"schedule_comfort": {"score_1_5": 3.0, "applicable": true, "reason": ""},
"budget_comfort": {"score_1_5": null, "applicable": false, "not_applicable_reason": ""},
"preference_satisfaction": {"score_1_5": null, "applicable": false, "not_applicable_reason": ""}
},
"evidence": [
{"item_ref": "D1-A1", "source": "EXPERIENCE_TRACE.activity_trace[D1-A1]", "claim": "", "score_impact": "
neutral"}
],
"confidence": "medium"
}
],
"experience_dimensions": {
"physical_comfort": {"score_1_5": 3.0, "applicable": true, "evidence": ["D1-A1"]},
"environmental_comfort": {"score_1_5": 3.0, "applicable": true, "evidence": ["D1-A1"]},
"schedule_comfort": {"score_1_5": 3.0, "applicable": true, "evidence": ["D1-A1"]},
"budget_comfort": {"score_1_5": null, "applicable": false, "not_applicable_reason": ""},
"preference_satisfaction": {"score_1_5": 3.0, "applicable": true, "evidence": ["D1-A1"]}
},
"missing_evidence": [],
"audit_notes": []
}
```
The evaluator will compute normalized scores from `score_1_5`; do not add extra scoring fields.
## Final Checks
Before returning JSON, verify:
1. Every expected activity ref appears exactly once.
2. Every activity has non-empty evidence.
3. Every evidence entry names both the supporting source and the supported claim.
4. Every applicable score is between 1 and 5.
5. No claim depends on invented facts.
32

<!-- page 33 -->

E QueryandPlanFieldExamples
This appendix presents one representative query record and its corresponding plan record to illustrate the
released data format. The query record includes the user-visible multi-turn request, active constraints,
requested update, and response contract used to specify the expected planning behavior. The plan record
is a lightly normalized model output from our evaluation pipeline, included to demonstrate the required
minute-level itinerary format. We remove raw tool traces, evaluator-side annotations, run identifiers, and
implementation metadata that are not needed to interpret the example.
Query Field Example (JSON)
{
"id": "mt_single_0005_turn_1",
"source_item_id": "mt_single_0005",
"query": {
"base_query_id": "single_0005",
"interaction_type": "long_horizon_alignment",
"interaction_label": "Long-Horizon Alignment",
"turn_count_in_dataset": 5,
"target_turn_id": 1,
"response_expectation": "plan",
"resolution_need": "none",
"feasibility_status": "solved",
"visible_turn_history": [
{
"turn_id": 0,
"role": "user",
"utterance": "My partner and I are planning a nature-focused getaway from Beijing to Shenzhen, arriving on
July 14, 2026 (Tuesday) and staying for 4 days, with our return flight on July 17, 2026 (Friday). We'll need
just one room. Since we love scenic parks, our main goal is to visit Nantou Ancient City. To keep things
easy, we'd like to book a single meal near \"Nantou Ancient City Museum\". For accommodation, we're looking
for the highest-rated hotel in the city, but we need to stick to a budget between 5400 and 7200 yuan.",
"sampled_deltas": ["initial_request"],
"state_delta": {
"initial_request": {
"base_query_id": "single_0005",
"hard_constraints": [
"budget_constraint",
"hotel_highest_rated",
"restaurant_closest_to_attraction",
"trip_date_range_required",
"room_count_required",
"intercity_round_trip_mode_required"
],
"observable_profile_visible": true
}
},
"must_update": ["initial_plan"],
"response_expectation": "plan"
},
{
"turn_id": 1,
"role": "user",
"utterance": "Please add \"Xianhu Botanical Garden\" to Day 3, while keeping every earlier requirement
unchanged.",
"sampled_deltas": ["add_db_grounded_attraction"],
"state_delta": {
"add_attraction": {
"name": "Xianhu Botanical Garden",
"insert_day": 3,
"source": "city_context.signature_or_crowd_attractions"
}
},
"must_preserve": [
"budget_constraint",
33

<!-- page 34 -->

"hotel_highest_rated",
"restaurant_closest_to_attraction",
"trip_date_range_required",
"room_count_required",
"intercity_round_trip_mode_required"
],
"must_update": ["add_attraction"],
"resolution_need": "none",
"response_expectation": "plan"
}
],
"active_constraints": {
"route": {
"origin_city": "Beijing",
"destination_city": "Shenzhen",
"intercity_mode": "flight",
"round_trip_required": true
},
"dates": {
"start_date": "2026-07-14",
"end_date": "2026-07-17",
"duration_days": 4,
"return_date": "2026-07-17"
},
"party": {
"travelers": 2,
"rooms": 1
},
"budget_rmb": {
"min": 5400,
"max": 7200,
"scope": "total estimated trip budget"
},
"lodging": {
"city": "Shenzhen",
"requirement": "highest-rated hotel in the destination city",
"nights": 3
},
"meal": {
"count": 1,
"near": "Nantou Ancient City Museum",
"selection_rule": "closest restaurant near the specified attraction"
},
"required_attractions": [
{"name": "Nantou Ancient City", "source": "initial request"},
{"name": "Xianhu Botanical Garden", "day": 3, "source": "turn 1 update"}
]
},
"preservation_contract": {
"must_preserve": [
"budget_constraint",
"hotel_highest_rated",
"restaurant_closest_to_attraction",
"trip_date_range_required",
"room_count_required",
"intercity_round_trip_mode_required"
],
"must_update": ["add_attraction"],
"forbidden_shortcuts": ["drop_existing_hard_constraints"]
}
}
}
34

<!-- page 35 -->

Plan Field Example
"plan": """
<plan>
Day 1 (2026-07-14):
Current City: from Beijing to Shenzhen
Accommodation: Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch), ¥354/room/night
08:00-09:30 | buffer | Arrive Beijing Capital International Airport, security and boarding
09:30-12:45 | travel_intercity_public | Flight HU7703, Beijing Capital International Airport - Bao'an
International Airport, Economy, ¥1075/person
12:45-13:15 | buffer | Deplaning and baggage claim at Bao'an International Airport
13:15-13:45 | travel_city | Bao'an International Airport - Orange Hotel (Shenzhen Nanshan Xili Metro Station
Branch), taxi, 14.85 km, 30 min, ¥36.1
13:45-14:15 | hotel | check-in, Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch)
14:15-14:18 | travel_city | Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch) - Dianbai Duck Porridge Shop,
walking, 287 m, 3 min, ¥0
14:18-15:30 | meal | lunch, Dianbai Duck Porridge Shop, ¥61/person
15:30-15:33 | travel_city | Dianbai Duck Porridge Shop - Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch),
walking, 287 m, 3 min, ¥0
15:33-18:00 | hotel | rest, Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch)
18:00-18:21 | travel_city | Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch) - Nantou Ancient City,
subway Line 5/Huanzhong - Line 12/Nanbao, 4.92 km, 21 min, ¥3/person
18:21-19:21 | attraction | Nantou Ancient City, ¥0/person
19:21-19:44 | travel_city | Nantou Ancient City - Hao Hao Wei Noodle House (Taoyuan Branch), walking, 1.91 km, 23
min, ¥0
19:44-21:00 | meal | dinner, Hao Hao Wei Noodle House (Taoyuan Branch), ¥26/person
21:00-21:25 | travel_city | Hao Hao Wei Noodle House (Taoyuan Branch) - Orange Hotel (Shenzhen Nanshan Xili Metro
Station Branch), subway Line 12/Nanbao - Line 5/Huanzhong, 6.26 km, 25 min, ¥3/person
Day 2 (2026-07-15):
Current City: Shenzhen
Accommodation: Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch), ¥354/room/night
10:00-11:14 | travel_city | Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch) - Dameisha Coastal Boardwalk,
taxi, 37.16 km, 74 min, ¥85.2
11:14-13:00 | attraction | Dameisha Coastal Boardwalk, ¥0/person
13:00-14:14 | travel_city | Dameisha Coastal Boardwalk - Dianbai Duck Porridge Shop, taxi, 36.88 km, 74 min, ¥84.5
14:14-15:30 | meal | lunch, Dianbai Duck Porridge Shop, ¥61/person
15:30-18:30 | hotel | rest, Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch)
18:30-18:33 | travel_city | Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch) - Dianbai Duck Porridge Shop,
walking, 287 m, 3 min, ¥0
18:33-20:00 | meal | dinner, Dianbai Duck Porridge Shop, ¥61/person
20:00-20:03 | travel_city | Dianbai Duck Porridge Shop - Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch),
walking, 287 m, 3 min, ¥0
Day 3 (2026-07-16):
Current City: Shenzhen
Accommodation: Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch), ¥354/room/night
09:30-10:17 | travel_city | Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch) - Xianhu Botanical Garden,
taxi, 23.71 km, 47 min, ¥55.6
10:17-12:17 | attraction | Xianhu Botanical Garden, ¥0/person
12:17-13:10 | travel_city | Xianhu Botanical Garden - Nantou Ancient City, taxi, 26.39 km, 53 min, ¥61.5
13:10-14:10 | attraction | Nantou Ancient City, ¥0/person
14:10-14:33 | travel_city | Nantou Ancient City - Hao Hao Wei Noodle House (Taoyuan Branch), walking, 1.91 km, 23
min, ¥0
14:33-15:45 | meal | lunch, Hao Hao Wei Noodle House (Taoyuan Branch), ¥26/person
15:45-16:10 | travel_city | Hao Hao Wei Noodle House (Taoyuan Branch) - Orange Hotel (Shenzhen Nanshan Xili Metro
Station Branch), subway Line 12/Nanbao - Line 5/Huanzhong, 6.26 km, 25 min, ¥3/person
16:10-18:30 | hotel | rest, Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch)
18:30-18:33 | travel_city | Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch) - Dianbai Duck Porridge Shop,
walking, 287 m, 3 min, ¥0
18:33-20:00 | meal | dinner, Dianbai Duck Porridge Shop, ¥61/person
20:00-20:03 | travel_city | Dianbai Duck Porridge Shop - Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch),
walking, 287 m, 3 min, ¥0
Day 4 (2026-07-17):
Current City: from Shenzhen to Beijing
Accommodation: -
10:00-10:30 | hotel | check-out, Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch)
35

<!-- page 36 -->

10:30-11:11 | travel_city | Orange Hotel (Shenzhen Nanshan Xili Metro Station Branch) - Bao'an International
Airport, subway Line 5/Huanzhong - Line 1/Luo Bao, 15.41 km, 41 min, ¥5/person
11:11-15:30 | buffer | Airport check-in, security, and boarding wait at Bao'an International Airport
15:30-17:00 | buffer | Continue waiting at gate before boarding
17:00-20:30 | travel_intercity_public | Flight CA1342, Bao'an International Airport - Beijing Capital
International Airport, Economy, ¥1200/person
20:30-21:00 | buffer | Deplaning and baggage claim at Beijing Capital International Airport
**Budget Summary**:
**Transportation: ¥4900.9**. Flights: (1075+1200) * 2 people = ¥4550. Intracity transport = ¥350.9.
**Accommodation: ¥1062**. ¥354 * 1 room * 3 nights.
**Meals: ¥592**. (61+26+61+61+26+61) * 2 people.
**Attractions & Tickets: ¥0**. Nantou Ancient City, Dameisha Coastal Boardwalk, and Xianhu Botanical Garden are
free.
**Other: 0 RMB**
**Total Estimated Budget: ¥6554.9**
</plan>
"""
36
