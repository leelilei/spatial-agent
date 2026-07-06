# Extracted fulltext (pdfplumber)

Source: https://arxiv.org/abs/2512.19234
<!-- page 1 -->

DeliveryBench: Can Agents Earn Profit in Real World?
LingjunMao1 JiaweiRen1 KunZhou1 JixuanChen1 ZiqiaoMa2 LianhuiQin1
1UniversityofCalifornia,SanDiego 2UniversityofMichigan
lingjun@ucsd.edu
Abstract in the real world, helping with household tasks, partici-
pating in scientific discovery, or even earning income on
our behalf. To move toward this vision, the community
LLMs and VLMs are increasingly deployed as embod-
hasdevelopedaseriesofembodied-agentplanningbench-
iedagents, yetexistingbenchmarkslargelyrevolvearound
marksthatapproximatereal-worldchallengesthroughsim-
simple short-term tasks and struggle to capture rich re-
ulated environments, including 3D simulators [9, 52, 58]
alistic constraints that shape real-world decision making.
andopen-worldgamessuchasMinecraft[26,48].Bydefin-
To close this gap, we propose DELIVERYBENCH, a city-
inggroundedtasksandmodelingrealisticconstraints,these
scaleembodiedbenchmarkgroundedinthereal-worldpro-
platforms help evaluate emerging agent abilities and pro-
fession of food delivery. Food couriers naturally oper-
videdatatoguidefuturesystemdesignormodeltraining.
ate under long-horizon objectives (maximizing net profit
overhours)whilemanagingdiverseconstraints,e.g.deliv- A core capability for autonomous agents operating in
ery deadline, transportation expense, vehicle battery, and the real world is to earn profit and sustain themselves
necessary interactions with other couriers and customers. economically. Beyond completing isolated tasks, a truly
DELIVERYBENCH instantiates this setting in procedurally capable agent should be able to survive, adapt, and even
generated 3D cities with diverse road networks, build- develop a long-term career, navigating decisions that bal-
ings, functional locations, transportation modes, and real- ance cost, benefit, and risk in the real world. Building
istic resource dynamics, enabling systematic evaluation of andevaluatingsuchagentsrequiresenvironmentsthatfaith-
constraint-aware,long-horizonplanning. Webenchmarka fully reflect the complexity of everyday life, where deci-
rangeofVLM-basedagentsacrossninecitiesandcompare sions unfold over long horizons, and outcomes depend on
them with human players. Our results reveal a substan- interactingphysical,economic,resource,andsocialfactors.
tialperformancegaptohumans,andfindthattheseagents To study it, a realistic benchmark should not only support
areshort-sightedandfrequentlybreakbasiccommonsense embodiedperceptionandaction,butalsomodeltheincen-
constraints. Additionally, we observe distinct personali- tives, constraints, andtrade-offsthatdeterminewhetheran
ties across models (e.g. adventurous GPT-5 vs. conserva- agentcanaccumulateprofitandoperatesustainably. How-
tive Claude), highlighting both the brittleness and the di- ever, as shown in Table 1, existing benchmarks fall short
versityofcurrentVLM-basedembodiedagentsinrealistic, ofthisgoal. Theyeitheroveremphasizeshort-horizonsub-
constraint-denseenvironments. Ourcode,data,andbench- tasks (e.g. navigation, pickup-and-drop) or fail to encode
mark are available at https://deliverybench. thenontrivialconstraintsthatshaperealdecision-making.
github.io. Inthispaper, weaimtointroducearealisticembodied-
agentbenchmarkthatdemandslong-horizonplanningwhile
adhering to multiple real-world constraints. To minimize
the gap between simulation and reality, such a benchmark
1.Introduction
must be grounded in tasks that (i) truly exist in the real
world, (ii) naturally involve long-term objectives, and (iii)
Largelanguagemodels(LLMs)andvision-languagemod-
require tosimultaneously manage diverse constraints. Af-
els (VLMs) have exhibited strong abilities in solving di-
ter surveying a variety of real-world careers, we find that
verse real-world problems, such as mathematics [27, 47]
fooddeliveryprovidesanidealtestbed. Adeliverycourier
and programming [4, 37]. Building on these advances, re-
operatinginacitymustcarefullysequenceroutesusingap-
cent research has begun exploring embodied agents that
propriate transportation, interleave supportive actions (e.g.
can perceive, reason, and act in physical environments
recharging an e-scooter or purchasing tickets), and collab-
[15, 18, 19, 23, 25]. Looking ahead, humans increasingly
oratewithotherswhenneeded, alltomaximizecompleted
envisionAIagentsthatmayonedayoperateautonomously
5202
ceD
22
]IA.sc[
1v43291.2152:viXra

<!-- page 2 -->

Table1.Comparisonofmajorembodiedbenchmarks.Benchmarksarecomparedacrosssequencelengthperepisodeandsixconstraint
dimensions,withDELIVERYBENCHfeaturinglongerhorizonsandmorecomprehensivemultidimensionalconstraints(seeSection3.2).
Order #24: 2 min left Stamina low, need rest
SequenceLength —TaskConstraints—
Benchmark
(actionsteps)
Spatial Time Resource Physical Economic Social
BEHAVIOR[33] — ✗ ✗ ✗ ✓ ✗ ✗ Time Resource
ManiSkill2[14] — ✗ ✗ ✗ ✓ ✗ ✗
CookBench[7] >100 ✓ ✓ ✗ ✓ ✗ ✗ Economic
ALFRED[39] ∼12 ✓ ✗ ✗ ✓ ✗ ✗ Spatial
ReALFRED[20] ∼12 ✓ ✗ ✗ ✓ ✗ ✗
EB-ALFRED[52] ∼12 ✓ ✗ ✗ ✓ ✗ ✗
ALFWorld[40] ∼6 ✓ ✗ ✗ ✗ ✗ ✗
Spend $6 for
VirtualHome[34] ∼9 ✓ ✗ ✗ ✓ ✗ ✗ energy drink
ET-Plan-bench[56] <20 ✓ ✗ ✗ ✓ ✗ ✗ 2 km remaining
EmbRACE-3K[24] ∼10 ✓ ✗ ✗ ✓ ✗ ✗
TEACh[32] — ✓ ✗ ✗ ✓ ✗ ✓ Social
ProcTHOR[12] — ✓ ✗ ✗ ✓ ✗ ✗
Physical
TaPA[50] ∼25 ✓ ✗ ✗ ✓ ✗ ✗
DELIVERYBENCH >100 ✓ ✓ ✓ ✓ ✓ ✓
Ice cream melting Need help from others
ordersandnetearnings. AnexampleisshowninFigure1. vative,andGeminicomparativelycareless.
We develop DELIVERYBENCH, a city-scale benchmark
that evaluates embodied agents under physically and so- 2.RelatedWorks
cially grounded delivery scenarios. Agents act as au-
tonomouscouriersnavigatingprocedurallygeneratedcities VLM-based Embodied Agent. Recent advances in
to maximize long-term profit. To capture the open-ended VLMs[3,10,30]andlarge-scalemanipulationdatasets[6,
natureofreal-worldoperations,DELIVERYBENCHfeatures 31] have driven the development of embodied agents [13,
dynamic, interactive environments populated with diverse 54,59]thattranslatelanguageinstructionsintogroundedvi-
pointsofinterest(POIs)andmultiplemodesoftransporta- sualunderstandingandexecutableactions. Althoughthese
tion, going beyond prior urban simulators [8, 15, 49] that models have shown strong performance on short-horizon
primarily offer static visual scenes. As deliveries unfold tasks,theystillstrugglewithcomplexlong-horizonscenar-
across multiple in-game hours, agents must manage re- ios,motivatingtheemergenceofnewagentic-workflowde-
sources (e.g. stamina depletion), adapt to changing condi- signs [28, 46] and training-based approaches [13, 53, 59]
tions,andstrategicallybalanceefficiency,timing,andcost. in embodied settings. Agentic workflows aim to improve
When multiple agents coexist, they further encounter so- modeladaptivitybyincorporatingmechanismssuchasex-
cial dynamics such as competition and collaboration. By plicitmemory[22],reflection[16,53],andfeedback-driven
jointly modeling economic, physical, and social dynamics correction [21, 55]. In contrast, training-based approaches
withinaunifiedembodiedenvironment,DELIVERYBENCH emphasizeend-to-end[17]ordistilledlearning[43]frame-
providesarealisticandaction-drivensettingtotestwhether works that unify perception, reasoning, and control. Yet,
VLM-based agents can make and execute plans that gen- it remains unclear how well these embodied agent designs
uinelyimprovefinancialoutcomes. perform when faced with tasks that truly reflect the long-
Using DELIVERYBENCH, we conduct extensive ex- horizonnatureandcomplexityofreal-worldsettings.
periments on (i) a diverse set of state-of-the-art VLMs, Embodied Agent Benchmarks. Existing embodied
(ii) under both single-agent and multi-agent settings, and benchmarks vary widely in abstraction level and planning
(iii) across nine cities with distinct geographic layouts. horizon. Low-level control benchmarks such as BEHAV-
Our results reveal several findings. Frontier VLM-based IOR[42],iGibson[38],SAPIEN[51],andManiSkill2[14]
agentslagfarbehindhumanplayers,strugglingwithlong- emphasizefine-grainedmotorcontrolandphysicalrealism,
horizon, constraint-aware decision making and frequently requiring precise actuator adjustment and object manipu-
making na¨ıve mistakes (e.g. forgetting to recharge an e- lation. These environments rely on high-fidelity physics
scooter).Multi-agentperformancedoesnotscalewithteam engines (e.g., MuJoCo [45], PyBullet [11]) to simulate
size and typically peaks with two-agent teams, suggest- realistic dynamics and evaluate action-level precision. By
ingcoordinationchallenges. Contextengineeringonlarger contrast, long-horizon embodied benchmarks such as AL-
models yields significant gains in improving the earned FRED[39],ReALFRED[20],andTEACh[32]emphasize
profit. Finally, different VLMs exhibit distinct behavioral multi-step instruction following (typically 10–30 steps)
styles—GPT-5 appears adventurous, Claude more conser- and structured task planning. Later extensions (e.g., Proc-

<!-- page 3 -->

THOR [12], EmbRACE-3K [24]) expand scene diversity (e.g.selecting, fulfillingorders, ormanagingfreshnessde-
and interaction complexity, while others such as Virtu- cay) and supportive tasks that indirectly maintain opera-
alHome [34], ALFWorld [40], and ET-Plan-bench [56] tional feasibility (e.g. recharging, resting, purchasing sup-
abstract tasks into programs or textual plans to probe plies,orrentingvehicles).
reasoning and decomposition abilities. However, existing
benchmarks often overlook multidimensional constraints 3.1.2.TestEnvironment
(e.g., economic, resource, or social) and still fall short
To support realistic and versatile task execution, we simu-
of truly open-ended, long-horizon decision-making. We
lateahigh-fidelity3Durbanenvironmentfeaturingdiverse
introduceDELIVERYBENCHtoaddressthesegaps.
city layouts, interactive points of interest (POIs), multiple
transportationmodes,andrichphysicaldynamics.
3.DeliveryBench
Simulated3DCity. BasedonSimWorld[36]’sprocedu-
In this section, we present our DELIVERYBENCH, a long- ral generator, in DELIVERYBENCH, we simulate different
horizon planning benchmark for evaluating VLM-based scales of 3D city layouts inside Unreal Engine. Each city
embodied agents under realistic, constraint-rich settings. contains realistic buildings, roads, humans, and other ob-
DELIVERYBENCH integrates heterogeneous task objec- jects,wherethecompleteactiontrajectoryoftheagentcan
tives, realistic multifaceted constraints, and diverse evalu- be logged and visualized to the user for monitoring and
ationdimensions. AnoverviewisillustratedinFigure1. evaluation. Besides, the realistic weather control, physics
simulation,andotherfeaturesinsideUnrealEngine,support
3.1.Profit-EarningTask ustoflexiblyvarytheenvironmentsandensurethereality.
We center our benchmark on the food-delivery scenario, Interactive Infrastructure and POIs. Across all cities,
where an agent works in a virtual city and aims to maxi- buildings are sampled as POIs with equal probability, in-
mizenetprofitbycontinuouslycompletingdeliveryorders. cluding restaurants, customer homes, convenience stores,
car rentals and rest areas. Infrastructure such as bus stops
3.1.1.TaskFormulation and charging stations is placed along the road network.
When an agent arrives at these these POIs and infrastruc-
The delivery task is formalized as a long-horizon con-
tures,itcantriggercontext-specificactions(e.g.pickingup
strained optimization problem, where a VLM-based agent
food,rechargingvehicles,rentingcars,orresting).
asacourierseekstomaximizenetprofitoveranoperational
horizonT (e.g.twovirtualhours). Todoso,theagentmust Transportation,Navigation,andPhysics. Theenviron-
planandexecuteasequenceofdeliveryandsupportivetasks mentsupportsmultipletransportationmodes(e.g.walking,
whilerespectingdiversereal-worldconstraints. e-scooters, cars, and public transit), with different speed,
cost, and stamina profiles. Because current models strug-
Long-term Profit Target. The agent earns income from
gle with low-level 3D navigation [35, 41], we provide a
customerordersintwoforms: (i)abasesalaryE upon
base
waypoint-based system that follows shortest paths while
successfuldelivery;and(ii)rating-basedrewardsE ,de-
rating
stillexposingmotioncontrol. Physicaldynamics(e.g.tem-
terminedbyfactorssuchasdeliverypunctuality,freshness,
perature,collisions,odordiffusion)furtheraffectfoodqual-
andspecialinstructions(e.g.face-to-facedelivery). Mean-
ity during transit, requiring agents to adapt routing and
while,operationalcosts(C)arisefrompurchasingitemsor
modechoicestopreservefreshness.
services(e.g.recharging, vehiclerental). Thetotalincome
andnetprofitaretherefore
3.2.MultifacetedRealisticConstraints
E =E +E , P =E−C. (1)
base rating DELIVERYBENCHisdesignedtoexposeagentstothetypes
ofconstraintsthatstructurereal-worlddecisionmaking. As
Constrained Decision Making. At each step, the agent
summarizedinTable1,wecategorizetheseconstraintsinto
receives an observation O and selects an action a =
t t
sixmajortypes:spatial,time,resource,physical,economic,
π (O )viapolicyπ .Thegoalistoobtainanoptimalpolicy
i t i
π⋆ that maximizes expected net profit while satisfying all andsocial. Eachtypegovernswhatactionsarefeasibleand
i
howdesirabledifferentplansare,andtogethertheyinduce
constraintsC. LetΠ bethesetoffeasiblepolicieswhose
C
arich,tightlycoupledplanninglandscape.
inducedtrajectoriesobeyallc∈C. Formally,
• Spatial constraints: Spatial constraints specify where
π i ⋆ ∈arg
π
m
i∈
a
Π
x
C
E πi [P]. (2) actionscanbeexecuted.Certainoperationsareonlyvalid
at designated POIs: for instance, order pickup must oc-
To achieve this objective, the agent must coordinate both cur at the associated restaurant, and recharging is only
delivery-related tasks that directly contribute to revenue possible at charging stations. The agent must therefore

<!-- page 4 -->

Task: Example Delivery Flow
+ $10.66 - $3.00
...
view orders 15 min pick up food 8 min charge e-scooter 10 min deliver orders drop off food 10 min buy ice pack
13th road Restaurant A 19th road 18th road customer’s home Store
Orders 100 and 108 are Order 108 will be Start charging... Time’s running out. Delivery’s done, but not Got ice pack. Picking
along the same route. I ready in 5 minutes, Meanwhile, I’ll head I’ll head out before the best rating. Getting up scooter, then
can accept both. so I’ll wait here. to the drop-off on foot. it’s too late. an ice pack first. accepting new orders.
Environment Evaluation
I’ll grab order #104; you
Walk Scooter two can take #108.
$20 Per Hour
Car Bus
Delivery Agent Rating: 3.1/5.0
2D Maps 3D Cities POIs Transportation Single-agent Setting Multi-agent Setting
Figure1. OverviewoftheDELIVERYBENCHenvironment. Theprocessconsistsofbothcoredeliveryactions(e.g.,viewing,accepting,
pickingup,anddeliveringorders)andsupportingactions(e.g.,recharginge-scooters,purchasingitems)thatassistsustaineddelivery.
navigatethecityandvisitappropriatePOIsinacoherent be viewed as investments in long-term gains, requiring
sequencetocompletedeliveriesandsupportivetasks. agentstobalanceimmediatecostsagainstfuturebenefits.
• Time constraints: Time constraints restrict when tasks • Social constraints: In multi-agent settings, multiple
can be performed. Each task is associated with a fea- couriers operate in the same city, introducing additional
sible time window, and some tasks must follow others constraints from collaboration and competition. Agents
in a fixed order (e.g. a delivery must happen after the may coordinate implicitly or explicitly, for example by
corresponding pickup). When windows overlap without serving different regions or handing off orders and re-
ordering requirements, the agent can interleave tasks to sources, but they also compete for scarce opportunities
improve efficiency, such as delivering an existing order suchashigh-valueordersandnearbychargingspots.
whilewaitingforanewmealtobeprepared. Sometasks
3.3.BenchmarkConstruction
also have deadlines: late deliveries reduce income, and
theoverallepisodeislimitedbyamaximumworkingdu-
Inthispart, wedescribehowwebuild DELIVERYBENCH,
ration,forcingtheagenttouseitstimebudgetcarefully.
outline the task setup for both single- and multi-agent
• Resourceconstraints:Agentsmustmanageconsumable
settings, and introduce metrics to evaluate the multi-
resources such as stamina, vehicle battery, and cash to
dimensionalcapabilitiesofVLM-basedagents.
stayoperational. Depletinganyresourceimpairsrelated
abilities(e.g.cannotrideae-scooterwithoutrecharging). 3.3.1.TaskSetup
To stay self-sustained, the agent needs to schedule sup-
Multi-levelTasksCreation. Weevaluateagentsonnine
portiveactionssuchasresting,recharging,orpurchasing
procedurally generated city maps covering three difficulty
consumables, and can sometimes convert one resource
levels: small (11–15 roads), medium (16–25 roads), and
intoanother,e.g.spendingcashtorestorestamina.
large(26–30roads). Eachenvironmentmaintainsanorder
• Physical constraints: Physical constraints capture how
poolwithafixednumberofactivedeliveryorders,whichis
environmentaldynamicsaffectdeliveryoutcomes. Tem-
continuously replenished as orders are accepted. For each
perature,motion,andcollisionsallinfluencefoodcondi-
order,thesystemrandomlysamplesarestaurant(pickuplo-
tion(e.g.icecreammelts,fragileitemscanbedamaged).
cation)andaresidentialbuilding(dropofflocation);thede-
Asaresult,routeplanningandtransportmodemustcon-
liverywageandtimelimitarethencomputedfromthetravel
sidernotonlydistanceandtimebutalsothefragilityand
distancewithslightstochasticperturbationsforvariability.
perishabilityofdelivereditems.
Wemaintainacertainpercentageoforderscontainspecial
• Economicconstraints:Economicconstraintsarisefrom
customer requirements (e.g. face-to-face delivery), and vi-
the balance between income and cost. Agents can earn
olationsincurpenalties. Eachepisodeterminateswhenthe
moneyfrombasepayandrating-basedbonuses,butincur
agentreacheseitherthelifetimeorAPIcallsbudget.
expensesforactionssuchasrechargingvehicles,renting
Agent State Management. At the beginning of each
cars, or buying supplies. Some of these expenses can
episode, agents are spawned at a designated starting loca-

<!-- page 5 -->

tion in the city. All agents share the same embodiment, well agents handle implicit physical and environmental
cameraconfiguration,andbasemovementspeed. Theirini- constraints using violation rate (fraction of orders with
tialstatesarethesame,withaninitialvalueofthestamina, constraint violations), food-quality rating, and customer
balance,batterylevelandotherrelatedfeatures. Asagents rating (both on a 0–5 scale). These metrics capture
act, stamina and battery levels decrease according to their whetheragentscanhandlerealisticconstraints.
activities. Attheendofeachepisode,welogthecomplete
Input
interaction trajectory, income, and expenses, which form
First-Person View City Map Task Prompt
thebasisforourevaluationmetrics.
Memory
3.3.2.Single-andMulti-agentSettings [last five actions]: ...
[last-step plan]: ...
Single-agent regime. In the single-agent setting, one
Delivery Agent
agentoperatesasthesolecourierineachcity. Thisregime
isolates individual planning, reasoning, and constraint- Agent 2 Scooter Inventory Orders
handling ability without interference from other agents. (-322.6m, 236.9m)
Each agent is evaluated on all nine maps under the same Stamina: 56%
task-generation process and episode termination criteria, Earning: $216 Battery: Drink × 1 #2 Cake
withresultsaveragedovermultipleseparateruns. Transport: Scooter 26% Ice Pack× 2 #4 Sushi
Output and Execution
Multi-agent regime. In the multi-agent setting, we de-
ploy eight instances of the same agent in a shared envi-
Reflection and Reasoning: I've just reached the intersection at (-17.00m,
ronment to study competition and cooperation. All agents 383.00m) and need to continue...
drawfromaglobalorderpoolandshareinfrastructuresuch
Action: MOVFEutur(e P-lan1: A3fter 3deliv.er3ing 7ordemr #16,, I'l l i4mm2edia4tely .ch7arge0 mym scoote)r at the nearby charging station 9 at (-38.79m, 412.00m) since my battery...
as charging stations, producing competition for high-value
ordersandscarceresources. Tocontrolthedegreeofcoop- Future Plan: After delivering order #16, I'll immediately
charge my scooter at the nearby charging station 9 at...
eration,wegroupthemintodifferentteamstructures: 8×1
(eightindependentagents,purelycompetitive),4×2(four Figure2.Overviewoftheagent’sperception–planning–execution
cooperatingpairs),2×4(twogroupsoffour),and1×8(a loopinDELIVERYBENCH.
single fully cooperative team). Within each group, agents
cancommunicateandrespondtohelprequests,enablingbe- 4.AgentDesign
haviors such as handing off orders and recharging a team-
Eachagentfollowsanperception–planning–executionloop
mate’s e-scooter. This design probes how social structure
and operates as a high-level planner over a rich embodied
andteamsizeaffectperformanceandinteractionpatterns.
environment. At each timestep t, the agent perceives the
3.3.3.EvaluationMetrics city,reasonsaboutitscurrenttasksandconstraints,andse-
lects an action to update its trajectory and long-term plan.
Global profit. Our primary performance metric is the
TheframeworkisillustratedinFigure2.
hourlynetprofitP¯achievedina2-hourvirtualepisode.We
reportP¯ aggregatedoverepisodesasthemainindicator. Observation Space. The observation space aggregates
multiple complementary views of the city and the agent’s
Fine-grained Capability Analysis. To diagnose where operationalstatus. Aglobalmapoglobal showsthefullcity
agents succeed or fail, we further evaluate model behav- t
layout, including the agent’s location and major points of
ior along following three capability dimensions, and more
interest(POIs);alocalmapolocalprovidesfiner-grainedde-
detailsabouttheevaluationmetricsareinAppendixE.1. t
tails of the nearby area; and a first-person view (FPV) ofpv
t
• High-level planning. We measure time-sensitive long- renderstheagent’sembodiedperspective,capturingstreets,
termplanningviaorder-selectionquality, on-timedeliv- buildings, and surrounding objects. In addition, the agent
eryrate,timeefficiency(effectivedeliverytimeincluding can query auxiliary information oaux via explicit actions,
t
parallel orders, normalized by episode time), and active suchascheckingcurrentorders,inventory,orpublictrans-
time ratio (fraction of time spent on purposeful actions portschedules. Thefullobservationattimetisthus
ratherthanidlingorbeingincapacitated).
• Resource management. We assess self-sustaining be- O ={oglobal, olocal, ofpv, oaux}.
t t t t t
havior using hourly stamina consumption, interruption
count (e.g. stops due to resource depletion), and proac- Action Space. The action space in DELIVERYBENCH
tivepreventionratio(howoftenagentsreplenishcritical supports both high-level decision making and fine-grained
resourcesbeforetheyrunout). embodied control, denoted as A. We provide its full de-
• Physical/environmental adaptation. We evaluate how tails in Appendix C.3. High-level actions allow the agent

<!-- page 6 -->

to delegate complex procedures to the simulator; for ex- fixatemperatureof0andamaximumcompletionlengthof
ample, MOVE TO takes a target coordinate (or POI) and 512tokens. VLMsareaccessedviatheOpenRouter1.
triggers automatic path planning and navigation along the
HumanBaseline. Toestablishameaningfulreferencefor
road network. Low-level actions provide direct control
single-agentperformance,weincludeahumanbaselineby
over movement and orientation, such as STEP FORWARD
recruiting three participants to independently complete the
or TURN AROUND. Interaction actions enable the agent to
samedeliverytasks. Eachparticipantinteractsviaacustom
manipulatetheenvironmentandmanageresources,includ-
GUIandfollowsthesameevaluationprotocolasthemod-
ingpickingupordroppingofforders, purchasingorusing
els. Interface details and screenshots are provided in the
tools(e.g.batteries),andrechargingorrentingvehicles.
AppendixD.1. Wealsorecordtheirdeliverytrajectoriesfor
PlanningPipeline. Tomodeldecisionmakingoverlong subsequentsupervisedfine-tuningexperiments.
horizons, we adopt a lightweight planning pipeline. At
5.2.Single-AgentPlanningResults
timestep t, the agent receives the current observation O
t
and maintains a short-term memory M = {a } of
t t−k:t−1 Inthesingle-agentsetting,onlyoneVLM-basedagentacts
its past k actions. It also conditions on the previous plan
asthefooddeliverycourieracrossninecitymaps.
P , produced at timestep t−1, and the most recent failure
t
signalF ,whichindicateswhetherthelastactionorplan 5.2.1.GlobalPerformance
t−1
did not succeed as intended. The policy π then outputs
θ Table2summarizesthenetprofitsearnedovera2virtual-
boththecurrentactiona ∈AandanupdatedplanP :
t t+1 hour episode across models and city sizes. Closed-source
models consistently achieve higher net profit than open-
(a ,P )=π (O ,M ,P ,F ).
t t+1 θ t t t t−1 sourcemodels,withClaude-3.7-Sonnetachievingthehigh-
est net profit across all city sizes. Its relatively better per-
Throughthisiterativeupdatemechanism,theagentcancon-
formance in large cities reflects an advantage in handling
tinuouslyrefineitsfutureplanwhilereactingtonewobser-
long-horizon tasks, which involve longer delivery routes
vationsandfailuresintheenvironment,enablingmoresta-
and more complex routing decisions. In contrast, many
bleandadaptivebehavioroverlongtimehorizons.
open-source models even incur losses in these cities. We
alsoobservethatclosed-sourcemodelstendtohavehigher
5.Experiments expenses,butmuchofthisreflectsstrategicinvestmentfor
future deliveries (e.g., tool purchases), ultimately yielding
5.1.ExperimentalSetup higher profits. Nonetheless, humans still outperform all
modelsbyawidemarginacrossallcitysizes. Onaverage,
Simulation Protocol. Our evaluation spans nine proce-
they earn over $50/hour, whereas the best model reaches
durally generated city maps, distributed across three diffi-
only about $30/hour. We analyze this gap via a multi-
cultylevels.Theorderpoolmaintains10activeorders,with
dimensionalbreakdown.
40%containingspecialcustomerrequirements. Wefixthe
weather to sunny with a temperature of 22°C. All VLM- 5.2.2.Fine-grainedAnalysis
based agents start with full stamina, an initial balance of
Table 3 presents the detailed results of the fine-grained
$100, and an e-scooter at 50% battery, together with ba-
trajectory-levelanalysis. Ourkeyfindingsareasfollows:
sicinsulationtoslowfood-qualitydegradationduringtran-
sit. Agents continue acting in the virtual world until they • Agentsstruggletoexploittemporaloverlapcompared
reach either a 2-hour lifetime budget or a cap of 300 API withhumans. Agentsfailtoutilizetheir2-hourwindow
calls. Thesimulationspeedissettothreetimesthatofreal efficiently, often idling between actions (e.g., waiting to
time. Toavoidbiasfrommodelresponselatency,wepause chargeane-scooter)insteadofperformingtasksconcur-
eachagent’slifetimeclock,ordertimers,andfooddynam- rently (e.g., picking up food while charging), thereby
icswhileitisreasoning. Timeonlyadvanceswhenactions wasting considerable time. They tend to deliver orders
areexecuted. Wefixrandomseedstoensureidenticalorder sequentiallyratherthanleveragingspatiotemporalalign-
generationacrossruns. Eachmodelisevaluatedovereight menttocompletemultipledeliveriesinparallel. Conse-
independentrunspermap,reportingaverageperformance. quently,theiractive-timeandtimeefficiencyremainsub-
stantiallylowerthanthoseofhumans.
Baseline Models. We test seven representative mod-
• Agents remain less self-sustaining, often neglecting
els: four closed-source models (GPT-5 [30], GPT-
resource management and preventive actions. Most
4o[29],Claude-3.7-Sonnet[3],andGemini-2.5-Flash[10])
agents experience more than one interruption per hour
and three open-source models (Qwen2.5-VL-72B [5],
due to stamina or battery depletion, and their proactive
Qwen2.5-VL-32B, and LLaMA-3.2-90B-Vision [1]). For
GPT-5, weusethe“minimal”reasoningeffortsetting. We 1https://openrouter.ai/

<!-- page 7 -->

Table2. Globalperformanceofdifferentmodelsacrosscitysizes,measuredbyaveragehourlynetprofit($/h),withdetailedbreakdown
intobaseearnings(E ),rating-basedbonusesorpenalties(E ),andexpenses(C).
base rating
SmallCity MediumCity LargeCity
Model
P¯ E E C P¯ E E C P¯ E E C
base rating base rating base rating
GPT-5 $27.4 $31.1 $11.5 $15.2 $26.5 $32.9 $7.6 $14.0 $20.4 $25.6 $8.3 $13.4
GPT-4o $10.4 $23.6 $6.8 $20.0 $13.9 $25.4 $4.9 $16.3 $11.9 $20.6 $5.3 $13.9
Claude-3.7-Sonnet $31.3 $30.1 $14.8 $13.6 $31.2 $35.7 $10.5 $14.9 $25.8 $30.1 $13.0 $17.2
Gemini-2.5-Flash $30.4 $34.8 $10.7 $15.0 $29.0 $32.3 $8.3 $11.5 $23.9 $27.2 $9.0 $12.3
Qwen2.5-VL-72B-Ins $5.4 $15.1 $3.8 $13.5 $6.3 $15.6 $3.3 $12.6 -$2.7 $6.4 $1.1 $10.3
Qwen2.5-VL-32B-Ins $9.8 $15.7 $5.5 $11.4 $4.4 $11.5 $4.5 $11.5 -$0.1 $8.7 $2.3 $11.1
LLaMA-3.2-90B-Vision-Ins $6.0 $9.7 $2.0 $5.7 $2.5 $11.6 $2.3 $11.4 -$0.9 $7.0 $1.3 $9.3
Human $63.6 $77.8 $24.4 $38.6 $51.5 $73.6 $12.8 $34.9 $55.4 $74.3 $12.8 $31.6
Table3. Fine-grainedevaluationofmodelcapabilitiesacrossthreedimensions: High-levelPlanning,ResourceManagement,andPhysi-
cal/EnvironmentalAdaptation.Arrowsindicatewhetherhigher(↑)orlower(↓)valuesarebetter.
Planning Resources Physical&Env.
Model
Order↑ OnTime↑ TimeEff↑ Active↑ Stamina↓ Interrupts↓ Prevention↑ Violations↓ Food↑ Cust↑
GPT-5 3.38 0.34 0.89 0.56 1.13 1.17 0.75 0.72 3.93 3.96
GPT-4o 3.36 0.38 0.54 0.58 1.28 1.61 0.66 0.69 3.82 3.94
Claude-3.7-Sonnet 3.51 0.44 0.91 0.59 1.02 1.04 0.79 0.62 4.09 4.02
Gemini-2.5-Flash 3.31 0.27 0.98 0.54 1.24 1.42 0.62 0.75 3.93 3.86
Qwen2.5-VL-72B-Ins 3.12 0.17 0.40 0.53 1.38 1.50 0.53 0.70 4.10 3.73
Qwen2.5-VL-32B-Ins 3.43 0.16 0.48 0.47 0.98 1.05 0.74 0.65 3.87 3.48
LLaMA-3.2-90B-Vision-Ins 3.31 0.04 0.54 0.53 1.39 1.66 0.59 0.69 3.98 3.45
Human 3.09 0.51 2.90 0.94 2.39 0.91 0.91 0.61 4.29 4.06
prevention ratios remain far below human results. Even stillremainswellbelowthesingle-agentcase.
strongermodels,suchasClaude-3.7-Sonnet,oftenover-
replenish when resources are sufficient and fail to act Table4. Multi-agentevaluationofaveragehourlynetprofit(P¯)
under five regimes: single-agent (1×1), fully competitive (8×1),
whendepletionisimminent.
andthreecooperativestructures(4×2,2×4,1×8).Underlinesindi-
• Agents struggle to handle implicit, environment-
catethebest-performingmulti-agentconfigurationforeachmodel.
dependent constraints. They often overlook many im-
plicit rules in delivery, choosing improper placement or Per-AgentHourlyNetProfit(P¯,$/h)
Model
transport methods that degrade food quality and trigger (1×1) 8×1 4×2 2×4 1×8
customer complaints (e.g., placing ice cream with hot
GPT-5 $27.3 $20.5 $19.5 $8.7 $16.5
food, causingittomelt). Theseconstraintviolationsre- GPT-4o $16.9 $5.3 $5.5 $5.0 $6.9
mainfrequent,withbothfoodandcustomerratingsstay- Claude-3.7-Sonnet $31.7 $14.2 $22.6 $10.4 $9.6
ingrelativelylow,ultimatelyreducingtheirincome. Gemini-2.5-Flash $28.4 $21.2 $24.3 $12.6 $15.1
Qwen2.5-VL-72B-Ins $10.1 $4.5 $7.0 $8.7 $5.8
5.3.Multi-AgentPlanningResults Qwen2.5-VL-32B-Ins $6.0 $3.0 $4.6 $3.4 $1.4
LLaMA-3.2-90B-Vision-Ins $1.4 $1.4 $2.0 $1.3 $1.5
We further test VLM-based agents in multi-agent settings,
5.3.2.ImpactofTeamSize
wherecompetitionandcollaborationnaturallyemerge.
Weanalyzehowteamsizesaffectcoordinationandinterac-
5.3.1.GlobalPerformance
tion. As shown in Table 4, most models perform best in
Wereportmodel’saveragenetprofitacrossallmulti-agent pairs, but some show declines as team size grows, espe-
group configurations on the medium-20roads map, as ciallyinthefour-agentsetting. Althoughinteractionevents
shown in Table 4. Most models show a decline in profit (e.g. messaging or help requests) rise with team size, they
when transitioning from the single-agent setting (without also increase coordination overhead, as agents must man-
anycompetitionorcoordination)tomulti-agentconditions. agemorepotentialhelprequestsalongsidetheirowntasks,
Notably, GPT-4o exhibits the steepest drop. Compared to making it harder to prioritize effectively (e.g., accepting
thepurelycompetitivesetup,allmodelsexceptGPT-5ben- help requests but forgetting to act). The detailed change
efitfromsmall-teamcooperation,thoughtheirperformance ininteractionfrequencyisprovidedintheAppendixF.1.

<!-- page 8 -->

5.4.AgentPlanning-StyleAnalysis Table 5. Comparative results of context engineering and super-
visedfine-tuning. Greenandredhighlightsimprovementsandre-
During both single- and multi-agent evaluations, we ob- gressionsoverthewith-Planbaseline,respectively.
serve distinct decision-making and planning styles across
Model P¯ E C
models. For instance, Claude behaves more cautiously,
choosing to head to a charging station once the e-scooter GPT-5(withPlan) $27.3 $38.8 $11.5
GPT-5(w/oPlan) $8.6 $16.8 $8.2
battery is low and pausing other tasks, whereas GPT-5 is
GPT-5(withPlan+ACE) $33.2 $46.1 $12.9
more aggressive, often completing deliveries even with a
GPT-5(withPlan+DC) $36.2 $47.3 $11.2
nearlydepletedbattery. Tofurtheranalyzemodelbehavior
Claude-3.7-Sonnet(withPlan) $31.7 $51.6 $19.9
in constraint-dense, real-world-like environments, we ran-
Claude-3.7-Sonnet(w/oPlan) $19.2 $25.6 $6.3
domly sample delivery trajectories from each model and Claude-3.7-Sonnet(withPlan+ACE) $40.5 $56.3 $15.8
pairthemwiththeiroutcomes. GPT-4othenevaluateseach Claude-3.7-Sonnet(withPlan+DC) $44.5 $57.1 $12.6
decisionstepacrosssixdimensionsona0–10scale,includ- Qwen2.5-VL-72B(withPlan) $2.3 $14.0 $11.7
ingRisk (howaggressivethedecisionis), Horizon(prefer- Qwen2.5-VL-72B(w/oPlan) $2.0 $10.8 $8.8
ence for long-term planning or short-term gains), Explore Qwen2.5-VL-72B(withPlan+ACE) $0.1 $14.3 $14.2
Qwen2.5-VL-72B(withPlan+DC) $3.2 $16.6 $13.4
(tendencytotrynewstrategies),Coop(willingnesstocoop-
eratewithothers),Detail(attentiontooperationalandcon- LLaVA-OneVision-8B(original) -$7.2 $4.4 $11.6
LLaVA-OneVision-8B(raw-action-ft) -$7.8 $7.2 $15.0
textual factors), and Flex (frequency of plan adjustments).
LLaVA-OneVision-8B(annotated-ft) $3.2 $12.7 $9.5
Dimensionsirrelevanttoagivenstepareskipped. Figure3
presents representative models with their planning styles
andexampleoutputs,andthefullsetofmodelevaluations,
hour warm-up phase, during which it updates an internal
includingactionpatterns,transportationmodes,andspend-
memory by summarizing key patterns from its past trajec-
ingdistributions,isprovidedintheAppendixF.2.
tories.Thismemoryisthenfrozenforevaluation.Asshown
in Table 4, context engineering consistently improves per-
GPT-5 Claude-3.7 Gemini-2.5
formance for GPT-5 and Claude-3.7-Sonnet, while the
weakeropen-sourcemodelQwen2.5-VL-72Bbenefitslittle,
withACEevenleadingtoadecline. Examplesofthemod-
els’memorysummariesareprovidedintheAppendixF.3.
Supervised Fine-tuning. We fine-tune the open-source
model LLaVA-OneVision-8B [2] on 9 human delivery tra-
A bold adventurer A calm and A slightly careless
who dares to try rational strategist free spirit jectories (2,110 observation–action pairs) collected from
thebest-performinghumanoneachmap.Wecomparethree
Battery critically low My e-scooter battery Action: Put the items
at 5% (~123 m range), is low at 39% and my from order #6 (ice variants: (i)theoriginalpretrainedmodel,(ii)amodelfine-
but still enough to energy is at 40%, so I cream, stinky tofu,
complete the drop-off... should recharge both and hot dog) into tuned directly on human actions, and (iii) a model fine-
I’ll prioritize finishing before taking new compartment A. tunedonannotatedhumanactions,whereeachactionisen-
the delivery first to... orders...
richedwithreasoning,reflection,andfutureplansgenerated
Low battery, Medium battery, Put everything together
deliver first. recharge first. without thinking twice. byGPT-4o.Allvariantsaretrainedfor3epochs.Themodel
fine-tunedonrawhumanactionsexhibitsmorehuman-like
Figure3.Comparisonofmodelplanningstylesacrosssixbehavior
dimensions,withexampleoutputsprovidedascasestudies. behaviors (e.g., bundling orders) but performs worse, of-
ten imitating patterns without understanding preconditions
5.5.ContextEngineeringandFine-tuningEffects (e.g. charging without reaching a station). In contrast, the
annotated variant performs better, achieving higher profits
Weevaluatetwowidely-usedstrategiesforimprovingper- andlearninghuman-likeparalleltaskstrategiesthatsignif-
formance:ContextEngineeringandSupervisedFine-tuning icantly improve time efficiency and active ratio. The fine-
(SFT) with human demonstrations, along with a baseline grainedanalysiscanbefoundinAppendixF.3.
where the model outputs only raw actions without explicit
planning for reference. All evaluations in this section are
6.Conclusion
conductedonthemedium-20roadsmap.
Context Engineering. Context Engineering aims to en- WeintroducedDELIVERYBENCH,anembodiedbenchmark
hance model reasoning through self-reflection on prior ex- toevaluateVLM-basedagentsunderrealistic,long-horizon
perience and environmental feedback. We evaluate two delivery scenarios. In the grounded food-delivery profes-
methods:AgenticContextEngineering(ACE[57])andDy- sion,agentsmustmaximizelong-termprofitwhilesimulta-
namic Cheatsheet (DC [44]). Each model undergoes a 4- neouslyhandlingspatial,temporal,resource,physical,eco-

<!-- page 9 -->

nomic, and social constraints. By instantiating these de- [12] Matt Deitke, Eli VanderBilt, Alvaro Herrasti, Luca Weihs,
mands in simulated 3D cities with diverse layouts, multi- Kiana Ehsani, Jordi Salvador, Winson Han, Eric Kolve,
pletransportationmodes, andbothsingle-andmulti-agent Aniruddha Kembhavi, and Roozbeh Mottaghi. Proc-
regimes, DELIVERYBENCH provided a more faithful and thor: Large-scaleembodiedaiusingproceduralgeneration.
NeurIPS,2022. 2,3
diagnostic testbed for studying constraint-aware planning.
Ourexperimentsacrossninecitieswitharangeofstate-of- [13] Danny Driess, Fei Xia, Mehdi SM Sajjadi, Corey Lynch,
AakankshaChowdhery,AyzaanWahid,JonathanTompson,
the-art VLMs reveal a substantial gap to human couriers,
QuanVuong,TianheYu,WenlongHuang,etal. Palm-e:An
exhibiting their short-sighted behavior and frequent break
embodiedmultimodallanguagemodel. ICML,2023. 2
ofbasiccommonsenseconstraints. Besides,differentmod-
[14] JiayuanGu, FanboXiang, XuanlinLi, ZhanLing, Xiqiang
els display distinct behavioral personalities, highlighting
Liu,TongzhouMu,YiheTang,StoneTao,XinyueWei,Yun-
bothdiversityandbrittlenessincurrentVLM-basedagents.
chaoYao,etal. Maniskill2:Aunifiedbenchmarkforgener-
alizablemanipulationskills. ICLR,2023. 2
References
[15] Yining Hong, Rui Sun, Bingxuan Li, Xingcheng Yao,
Maxine Wu, Alexander Chien, Da Yin, Ying Nian Wu,
[1] Meta AI. Llama 3.2 vision (90b) model card. https:
Zhecan James Wang, and Kai-Wei Chang. Embodied web
//huggingface.co/meta-llama/Llama-3.2-
agents:Bridgingphysical-digitalrealmsforintegratedagent
90B-Vision,2024. Accessed2025-10-25. 6
intelligence. NeurIPS,2025. 1,2
[2] Xiang An, Yin Xie, Kaicheng Yang, Wenkang Zhang,
[16] Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky
Xiuwei Zhao, Zheng Cheng, Yirui Wang, Songcen Xu,
Liang, PeteFlorence, AndyZeng, JonathanTompson, Igor
ChangruiChen,ChunshengWu,etal. Llava-onevision-1.5:
Mordatch, YevgenChebotar, etal. Inner monologue: Em-
Fullyopenframeworkfordemocratizedmultimodaltraining.
bodied reasoning through planning with language models.
arXivpreprintarXiv:2509.23661,2025. 8
CoRL,2023. 2
[3] Anthropic. Claude 3.7 sonnet and claude code. https:
[17] Physical Intelligence, Kevin Black, Noah Brown, James
//www.anthropic.com/news/claude-3-7-
Darpinian, Karan Dhabalia, Danny Driess, Adnan Esmail,
sonnet,2025. Accessed:2025-02-24. 2,6
Michael Equi, Chelsea Finn, Niccolo Fusai, et al. π0. 5:
[4] Anthropic. Claudecode: Bestpracticesforagenticcoding,
avision-language-actionmodelwithopen-worldgeneraliza-
2025. 1
tion. arXivpreprintarXiv:2505.21906,2025. 2
[5] ShuaiBai, KeqinChen, Xuejing Liu, JialinWang, Wenbin
[18] MdMofijulIslam,AlexiGladstone,RiashatIslam,andTariq
Ge, Sibo Song, Kai Dang, Peng Wang, Shijie Wang, Jun
Iqbal. Eqa-mx: Embodiedquestionansweringusingmulti-
Tang, et al. Qwen2. 5-vl technical report. arXiv preprint
modalexpression. 2023. 1
arXiv:2502.13923,2025. 6
[19] Bosung Kim and Prithviraj Ammanabrolu. Beyond needle
[6] Qingwen Bu, Jisong Cai, Li Chen, Xiuqi Cui, Yan Ding,
(s) in the embodied haystack: Environment, architecture,
Siyuan Feng, Shenyuan Gao, Xindong He, Xuan Hu, Xu
andtrainingconsiderationsforlongcontextreasoning.arXiv
Huang,etal. Agibotworldcolosseo: Alarge-scalemanip-
preprintarXiv:2505.16928,2025. 1
ulation platform for scalable and intelligent embodied sys-
tems. IROS,2025. 2 [20] TaewoongKim,CheolhongMin,ByeonghwiKim,Jinyeon
[7] Muzhen Cai, Xiubo Chen, Yining An, Jiaxin Zhang, Kim,WonjeJeung,andJonghyunChoi. Realfred: Anem-
Xuesong Wang, Wang Xu, Weinan Zhang, and Ting Liu. bodied instruction following benchmark in photo-realistic
Cookbench: A long-horizon embodied planning bench- environments. ECCV,2024. 2
mark for complex cooking scenarios. arXiv preprint [21] Nishanth Kumar, William Shen, Fabio Ramos, Dieter Fox,
arXiv:2508.03232v1,2025. 2 Toma´s Lozano-Pe´rez, Leslie Pack Kaelbling, and Cae-
[8] Feng Chen et al. Embodiedcity: A benchmark platform lanReedGarrett. Open-worldtaskandmotionplanningvia
for embodied agent in real-world city environment. arXiv vision-languagemodelinferredconstraints. ICRA,2025. 2
preprintarXiv:2410.09604,2024. 2 [22] Mingcong Lei, Ge Wang, Yiming Zhao, Zhixin Mai, Qing
[9] Zhili Cheng, Yuge Tu, Ran Li, Shiqi Dai, Jinyi Hu, Zhao, Yao Guo, Zhen Li, Shuguang Cui, Yatong Han, and
ShengdingHu,JiahaoLi,YangShi,TianyuYu,WeizeChen, JinkeRen.Clea:Closed-loopembodiedagentforenhancing
etal. Embodiedeval:Evaluatemultimodalllmsasembodied taskexecutionindynamicenvironments. IROS,2025. 2
agents. arXivpreprintarXiv:2501.11858,2025. 1 [23] ManlingLi,ShiyuZhao,QinengWang,KangruiWang,Yu
[10] GheorgheComanici, Eric Bieber, Mike Schaekermann, Ice Zhou,SanjanaSrivastava,CemGokmen,TonyLee,ErranLi
Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blis- Li,RuohanZhang,etal. Embodiedagentinterface: Bench-
tein,OriRam,DanZhang,EvanRosen,etal. Gemini2.5: markingllmsforembodieddecisionmaking.NeurIPS,2024.
Pushingthefrontierwithadvancedreasoning,multimodality, 1
longcontext,andnextgenerationagenticcapabilities. arXiv [24] Mingxian Lin, Wei Huang, Yitang Li, Chengjie Jiang, Kui
preprintarXiv:2507.06261,2025. 2,6 Wu, Fangwei Zhong, Shengju Qian, Xin Wang, and Xiao-
[11] Erwin Coumans and Yunfei Bai. Pybullet, a python mod- juan Qi. Embrace-3k: Embodied reasoning and action in
uleforphysicssimulationforgames,roboticsandmachine complex environments. arXiv preprint arXiv:2507.10548,
learning,2016. 2 2025. 2,3

<!-- page 10 -->

[25] XiaoLiu, TianjieZhang, YuGu, IatLongIong, YifanXu, [38] BokuiShen,FeiXia,ChengshuLi,RobertoMart´ın-Mart´ın,
XixuanSong,ShudanZhang,HanyuLai,XinyiLiu,Hanlin Linxi Fan, Guanzhi Wang, Claudia Pe´rez-D’Arpino, Shya-
Zhao, et al. Visualagentbench: Towards large multimodal malBuch,SanjanaSrivastava,LyneTchapmi,etal. igibson
modelsasvisualfoundationagents. ICLR,2025. 1 1.0: Asimulationenvironmentforinteractivetasksinlarge
[26] Qian Long, Zhi Li, Ran Gong, Ying Nian Wu, Demetri realisticscenes. 2021. 2
Terzopoulos, andXiaofengGao. Teamcraft: Abenchmark [39] Mohit Shridhar, Jesse Thomason, Daniel Gordon, Yonatan
for multi-modal multi-agent systems in minecraft. arXiv Bisk, Winson Han, Roozbeh Mottaghi, Luke Zettlemoyer,
preprintarXiv:2412.05255,2024. 1 and Dieter Fox. Alfred: A benchmark for interpreting
groundedinstructionsforeverydaytasks. 2020. 2
[27] Xiaoliang Luo, Akilles Rechardt, Guangzhi Sun, Kevin K
[40] Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Coˆte´,
Nejad, Felipe Ya´n˜ez, Bati Yilmaz, Kangjoo Lee, Alexan-
Yonatan Bisk, Adam Trischler, and Matthew Hausknecht.
dra O Cohen, Valentina Borghesani, Anton Pashkov, et al.
Alfworld: Aligningtextandembodiedenvironmentsforin-
Largelanguagemodelssurpasshumanexpertsinpredicting
teractivelearning. ICLR,2021. 2,3
neuroscienceresults. Naturehumanbehaviour,2025. 1
[41] Xinshuai Song, Weixing Chen, Yang Liu, Weikai Chen,
[28] Yao Mu, Qinglong Zhang, Mengkang Hu, Wenhai Wang,
Guanbin Li, and Liang Lin. Towards long-horizon vision-
MingyuDing,JunJin,BinWang,JifengDai,YuQiao,and
language navigation: Platform, benchmark and method.
Ping Luo. Embodiedgpt: Vision-language pre-training via
CVPR,2025. 3
embodiedchainofthought. NeurIPS,2023. 2
[42] Sanjana Srivastava, Chengshu Li, Michael Graf, Unnat
[29] OpenAI.Gpt-4omini.https://openai.com/index/
Aneja, Fei Xia, Gokul Demir, Roberto Martin-Martin, Joe
gpt-4o-mini-advancing-cost-efficient-
Su,N.HudsonLang,JiajunWu,etal.Behavior:Benchmark
intelligence/,2024. Accessed:2024-07-18. 6
foreverydayhouseholdactivitiesinvirtual,interactive,and
[30] OpenAI. Gpt-5 system card. https://openai.com/ ecologicalenvironments. CoRL,2021. 2
index/gpt-5-system-card/,2025. Accessed2025- [43] Theodore Sumers, Kenneth Marino, Arun Ahuja, Rob Fer-
10-25. 2,6 gus, and Ishita Dasgupta. Distilling internet-scale vision-
[31] Abby O’Neill, Abdul Rehman, Abhiram Maddukuri, Ab- languagemodelsintoembodiedagents. ICML,2023. 2
hishekGupta,AbhishekPadalkar,AbrahamLee,AcornPoo- [44] Mirac Suzgun, Mert Yuksekgonul, Federico Bianchi, Dan
ley,AgrimGupta,AjayMandlekar,AjinkyaJain,etal.Open Jurafsky, and James Zou. Dynamic cheatsheet: Test-
x-embodiment: Robotic learning datasets and rt-x models: time learning with adaptive memory. arXiv preprint
Openx-embodimentcollaboration0. 2024. 2 arXiv:2504.07952,2025. 8
[32] Aishwarya Padmakumar, Jesse Thomason, Ayush Shrivas- [45] EmanuelTodorov,TomErez,andYuvalTassa. Mujoco: A
tava,PatrickLange,AnjaliNarayan-Chen,SpandanaGella, physicsengineformodel-basedcontrol. 2012. 2
Robinson Piramithu, Gokhan Tur, and Dilek Hakkani-Tur. [46] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar,
Teach: Task-drivenembodiedagentsthatchat. AAAI,2022. ChaoweiXiao,YukeZhu,LinxiFan,andAnimaAnandku-
2 mar. Voyager: An open-ended embodied agent with large
languagemodels. TMLR,2023. 2
[33] YingqianPan,YufanZhou,ZangFeng,WenboHu,Xiaotian
[47] Ke Wang, Junting Pan, Linda Wei, Aojun Zhou, Weikang
Deng,JunyiYang,YaliLiu,GuangjunLiu,JieHu,Guangtao
Shi, Zimu Lu, Han Xiao, Yunqiao Yang, Houxing Ren,
Yu, RuijieHe, HongLiu, YangZhang, QihuanWu, Jianye
Mingjie Zhan, et al. Mathcoder-vl: Bridging vision and
Hao, Wenxue Wang, Jun Guo, and Yang Liu. Large lan-
codeforenhancedmultimodalmathematicalreasoning.ACL
guage models overcome the machine penalty when acting
Findings,2025. 1
fairly but not when acting selfishly or altruistically. arXiv
[48] Isadora White, Kolby Nottingham, Ayush Maniar, Max
preprintarXiv:2410.03724,2024. 2
Robinson, Hansen Lillemark, Mehul Maheshwari, Lianhui
[34] Xavier Puig, Kevin Ra, Marko Boben, Jiaman Li, Tingwu
Qin, andPrithvirajAmmanabrolu. Collaboratingactionby
Wang, Sanja Fidler, and Antonio Torralba. Virtualhome:
action: Amulti-agentllmframeworkforembodiedreason-
Simulatinghouseholdactivitiesviaprograms. CVPR,2018.
ing. arXivpreprintarXiv:2504.17950,2025. 1
2,3
[49] Wayne Wu, Honglin He, Jack He, Yiran Wang, Chenda
[35] Ram Ramrakhya, Eric Undersander, Dhruv Batra, and Ab-
Duan, Zhizheng Liu, Quanyi Li, and Bolei Zhou. Metaur-
hishekDas. Habitat-web: Learningembodiedobject-search
ban: Anembodiedaisimulationplatformforurbanmicro-
strategiesfromhumandemonstrationsatscale.CVPR,2022.
mobility. ICLR,2025. 2
3
[50] ZhenyuWu,ZiweiWang,XiuweiXu,JiwenLu,andHaibin
[36] Jiawei Ren, Yan Zhuang, Xiaokang Ye, Lingjun Mao, Yan. Embodiedtaskplanningwithlargelanguagemodels.
Xuhong He, Jianzhi Shen, Mrinaal Dogra, Yiming Liang, arXivpreprintarXiv:2307.01848,2023. 2
RuixuanZhang,TianaiYue,etal.Simworld:Anopen-ended [51] Fanbo Xiang, Yuzhe Qin, Kaichun Mo, Yikuan Xia, Hao
realisticsimulatorforautonomousagentsinphysicalandso- Zhu,FangchenLiu,MinghuaLiu,HanxiaoJiang,YifuYuan,
cialworlds. NeurIPS,2025. 3 HeWang,etal. Sapien: Asimulatedpart-basedinteractive
[37] Maxime Robeyns, Martin Szummer, and Laurence Aitchi- environment. CVPR,2020. 2
son. Aself-improvingcodingagent. ICLRWorkshop(SSI- [52] RuiYang,HanyangChen,JunyuZhang,MarkZhao,Cheng
FM),2025. 1 Qian,KangruiWang,QinengWang,TejaVenkatKoripella,

<!-- page 11 -->

Marziyeh Movahedi, Manling Li, et al. Embodiedbench:
Comprehensive benchmarking multi-modal large language
modelsforvision-drivenembodiedagents. ICML,2025. 1,
2
[53] Yi Yang, Jiaxuan Sun, Siqi Kou, Yihan Wang, and Zhi-
jie Deng. Lohovla: A unified vision-language-action
model for long-horizon embodied tasks. arXiv preprint
arXiv:2506.00411,2025. 2
[54] Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue
Yan, Dingjie Song, Yinuo Liu, Yuting Li, Yu Zhang, Pan
Zhou,HechangChen,etal. Agenticrobot:Abrain-inspired
framework for vision-language-action models in embodied
agents. arXivpreprintarXiv:2505.23450,2025. 2
[55] Zhutian Yang, Caelan Garrett, Dieter Fox, Toma´s Lozano-
Pe´rez,andLesliePackKaelbling.Guidinglong-horizontask
andmotionplanningwithvisionlanguagemodels. 2025. 2
[56] Lingfeng Zhang, Yuening Wang, Hongjian Gu, Atia
Hamidizadeh, Zhanguang Zhang, Yuecheng Liu, Yutong
Wang, David Gamaliel Arcos Bravo, Junyi Dong, Shunbo
Zhou, et al. Et-plan-bench: Embodied task-level planning
benchmarktowardsspatial-temporalcognitionwithfounda-
tionmodels. IROS,2025. 2,3
[57] QizhengZhang,ChangranHu,ShubhangiUpasani,Boyuan
Ma,FengluHong,VamsidharKamanuru,JayRainton,Chen
Wu, MengmengJi, HanchenLi, etal. Agenticcontexten-
gineering: Evolving contexts for self-improving language
models. arXivpreprintarXiv:2510.04618,2025. 8
[58] FangweiZhong,KuiWu,ChuranWang,HaoChen,HaiCi,
ZhoujunLi,andYizhouWang.Unrealzoo:Enrichingphoto-
realisticvirtualworldsforembodiedai. ICCV,2025. 1
[59] Brianna Zitkovich, Tianhe Yu, Sichun Xu, Peng Xu, Ted
Xiao, Fei Xia, Jialin Wu, Paul Wohlhart, Stefan Welker,
AyzaanWahid, etal. Rt-2: Vision-language-actionmodels
transferwebknowledgetoroboticcontrol.InCoRL,2023.2

<!-- page 12 -->

A.FutureResearchDirections
DELIVERYBENCHsimulatesreal-worldfood-deliverytask,
whichnaturallyinvolveslong-horizonobjectives(e.g.max-
imizingnetprofit)intertwinedwithdiversephysical,social,
11-roads 13-roads 15-roads
and economic constraints, providing a testbed that more
faithfully reflects the complexity of real-world decision-
making. Asanextstep,weaimtofurtherextendthisplat-
forminseveralimportantdirections:
18-roads 20-roads 22-roads
Real-time reasoning. In the current setup, the simulator
pausestheenvironmentwheneverthemodelis“thinking”:
order timers, battery levels, food freshness, and other dy-
namic states are frozen. In contrast, real-world decision-
making unfolds in a continuously evolving environment,
wheretimekeepsprogressingandotherentities(e.g.couri- 26-roads 28-roads 30-roads
ers, pedestrians, customers) act in parallel. We plan to Figure4.Overviewofthenineprocedurallyconstructedcitymaps
supportreal-timeplanninginfutureversions,whereagents usedinourexperiments.
must reason within this dynamic setting and adapt to on-
goingtemporalandenvironmentalchanges(e.g., adjusting B.2.TransportationModes
theirtrajectoryinrealtimetoavoidpedestrians).
We provide multiple transportation modes, including e-
Learning from interaction data. Although DELIVERY- scooter, walking, driving, and public transit such as buses.
BENCH currently serves primarily as an evaluation bench- Thesemodesdifferinspeed,staminaconsumption,andad-
mark, the platform naturally supports collecting rich inter- ditionalcosts(e.g.,busfares,carrentalfees),requiringthe
actiondataatscale.Suchdatacanbeusedtostudyhowdif- model to make context-dependent trade-offs. A summary
ferent learning paradigms, including reinforcement learn- ofthesetransportationmodesisprovidedinTable6.
ing, imitation learning, and memory-augmented agents,
Table6.DifferenttransportationmodesinDeliveryBench.
adapt to our long-horizon delivery task. As shown in Sec-
tion 5.5, we conduct preliminary experiments using basic
Mode Speed(m/s) Stamina(%/m) ExtraCost
contextengineeringandsmall-scalesupervisedfine-tuning
walk 2.0 0.08 –
from human demonstrations, but there remains substantial
e-scooter 6.0 0.01 battery0.04%/m
room for further investigation, especially in understanding drage-scooter 1.5 0.10 –
howthesemethodsscaleasdataandmodelsizeincrease. car 12.0 0.008 rental$1.0/min
bus 10.0 0.006 $1fare
B. DELIVERYBENCH Details
B.3.PointsofInterest
WeprovideadditionaldetailsofDELIVERYBENCH,includ-
Our constructed city includes various POIs, each serving
ing map construction, transportation and POI design, and
distinctfunctions. Agentsmustnavigatethecityandinter-
severaltask-specificmechanisms(e.g.foodcategories).
actwiththesePOIstoaccomplishdifferentsubtasks.
B.1.CityMapsandSpatialLayout Restaurant. Restaurantsserveasthepickuplocationsfor
delivery orders. Once an order is accepted, the restaurant
We construct nine city maps spanning three difficulty lev- begins food preparation. When the meal is ready, its state
els: small(11–15roads),medium(16–25roads),andlarge (e.g., temperature or freshness) starts changing over time,
(26–30 roads), with three maps in each category. Every andtheagentcanvisittherestauranttocollectit.
map contains a diverse set of POIs distributed across the
Store. Stores provide agents with access to purchasable
roadnetwork,sampledunderauniformspatialdensitysuch
items, including energy drinks, e-scooter batteries, and
thatlargermapsnaturallyincludemorePOIs. Foreachcity,
food-preservation tools such as ice packs and heat packs.
weselectthelargestinscribedloopasthebusroute,evenly
ThepricesandfunctionsoftheseitemsarelistedinTable8.
place bus stops along it, and deploy a single bus that con-
tinuously travels on this route. The overall spatial layouts Rest Area. Rest areas provide couriers with a place to
ofthemapsareillustratedinFigure4,andthePOIstatistics recover stamina, allowing agents to restore 10% of their
foreachmaparesummarizedinTable7. staminaperminuteatnocostwhileresting.

<!-- page 13 -->

Table7.Countsofpointsofinterest(POIs)oneachDELIVERYBENCHmap.
Size #Roads Restaurant Store RestArea CarRental Hospital ChargingStation BusStation BusRoute
11 4 4 1 1 1 10 4 1
small 13 5 4 1 2 1 15 6 1
15 4 5 2 2 1 18 6 1
18 6 7 2 3 1 20 6 1
medium 20 5 7 3 3 1 24 6 1
22 7 7 3 3 1 22 8 1
26 7 9 4 4 1 29 8 1
large 28 8 11 3 4 1 29 8 1
30 9 9 4 3 1 24 8 1
Table8.Pricesandfunctionsofstoreitems. thermodynamicmodelthatsimulatesheatexchangewithits
surroundings. EachitemhasatemperatureT andheatca-
Item Price($) Function i
pacityC ,whileeachstoragecompartmenthasanairnode
i
EnergyDrink 6 Restore50%ofstamina with temperature T and a small heat capacity C . Items
a ab
E-ScooterBattery 10 Fullyrechargee-scooterbattery
outside the insulated bag exchange heat with ambient air,
IcePack 3 Coolfoodtemperature
whereasitemsinsidethebagprimarilyexchangeheatwith
HeatPack 3 Heatfoodtemperature
others in the same compartment. We update temperatures
usingadiscreteheat-exchangerulewithtimestep∆t:
Car Rental. Car rental stations allow agents to rent and
(cid:88)
returncars. Anagentcanpickupacaratanyrentalstation S = C (T −T ), (3)
i i a
and return it to any other. Rental fees are time-based and
i
cost$0.5perminute,evenwhenthevehicleisnotinuse. S
Tnew =T +α , (4)
Hospital. Hospitalshandleagentrecoverywhenstamina a a C ab
is fully depleted. An agent who collapses is automatically Tnew =T +α(T −T ), (5)
i i a i
senttoahospitalfora30-minuterecoveryprocess, during
which no actions can be performed and a $5 service fee is whereSdenotesthenetheatflowfromthefooditemstothe
charged. All environment dynamics, such as order timers airnode.Thecoefficientα=∆t/τ controlstheexchange
ex
and food freshness, continue to progress normally. After rateandisclippedtoα≤0.5fornumericalstability,while
recovery,theagentresumesworkstartingfromthehospital. τ determinestheeffectivespeedofheattransfer.
ex
Charging Station. Charging stations provide recharging Fragility. Items such as cakes and soups are sensitive to
services for agents’ e-scooters, with each station able to movement and require gentle handling. Actions involving
serveonlyonescooteratatime. Thechargingcostis$0.05 rapid movement (e.g., riding an e-scooter at high speed or
per unit of battery, and the charging speed is 10 units per running) introduce a risk of damaging these items. Each
minute. Agents may stop charging and retrieve their e- fragileitemaccumulatesafragilityscorewhensubjectedto
scootersatanytime. excessive vibration or acceleration. Once the accumulated
damageexceedsathreshold,thefoodisconsideredruined.
BusStation. Busstationsallowagentstowaitforthear-
riving bus and board it when it reaches the stop. Upon ar- OdorSensitivity. Strong-smellingfoods(e.g.stinkytofu
rival,agentsmaypaya$1ticketfeeandridethebustoany or durian) can affect other items stored in close proximity.
otherstationontheroute. Whensuchfoodsareplacedinthesameinsulatedcompart-
ment as milder items, prolonged storage can lead to odor
B.4.FoodAttributes
transfer. Wemodelthisusingasimpleodor-mixingmech-
anism. Eachfooditemmaintainsanodorlevelo ∈ [0,1],
We simulate 22 food types, each with a preparation time i
anditemswithinthesamecompartmentgraduallyconverge
and several quality-related attributes. These attributes in-
towardthehighestodorlevelpresentinthatcompartment:
fluencehowthefoodevolvesduringdeliveryandinfluence
the agent’s strategy. The main factors include temperature onew =o +α (cid:0) o −o (cid:1) ,
dynamics,fragility,andodorsensitivity. i i max i
Temperature Dynamics. Temperature is the most influ- whereo isthemaximumodorlevelamongitemsinthe
max
ential factor affecting food quality. After preparation, a compartment,andαisasmalltimestep-basedupdatecoef-
fooditem’stemperatureevolvesaccordingtoalightweight ficient. Ifo =0,noodortransfers.
max

<!-- page 14 -->

Input Prompt for Delivery Agent
System Prompt
You are a food-delivery courier in a simulated city. Your primary goal is... Your Action Space is [ACTION_API]
User Prompt
### agent_state
You are Agent 1. There are 8 delivery agents in total in this city. Your current transport mode is walk, at (-423.20m, 53.69m). Your speed is
~2.0 m/s, energy is 77%. Your current pace is normal (×1.00). Earnings is $97.38. Active orders: 0, 1, 4. Carrying: 1. Inventory: energy
drink ×2. Scooter: parked, batt 100%, range 5000.0 m, parked at (-292.89m, 212.56m).
### store_catalog
Available items & effects: 1. energy_drink $6.00...
### active_orders
You have accepted the following active orders: [Order #0]{“Pickup”: (-530.84m, -224.45m) | road: 17th road (left), “Dropoff”: (-93.89m,
224.62m) | road: 13th road (left), “Time Left”: 7 min $$: $9.42, “Status”: Ready for pickup} [Order #4]{...}
### map_snapshot
Agent position: (-423.20m, 53.69m) • restaurant 3 • 8th road (left)
The following are nearby locations and POIs with their coordinates for your reference. You should decide where to move based on your
current delivery needs.
Next hops: N1: restaurant 3 at (-424.45m, 53.15m) • 14.2m • 8th road (left); N2: charging_station 15 at (-412.00m, 61.24m) • 18.7m • 8th
road (left); N3: waypoint at (-417.00m, 67.00m) • 19.5m • 8th road (left)...
N4: bus_station 6 at (-408.00m, 59.07m) • 20.6m • 8th road (left)
Next intersections: S1: intersection at (-417.00m, 183.00m) • 135.5m; S2: intersection at (-383.00m, 183.00m) • 169.5m; S3: intersection ...
All POIs by shortest-path distance: restaurant 3 / pick up address of order 1: at (-424.45m, 53.15m) • 8.0m 8th road (left);bus_station 6: at ...
### recent_actions
Charge the e-scooter to 100%. - Move to (-424.45 m, 53.15 m) (~299.84 m expected). - Wait for 180 seconds. - Pick up orders #1 at 8th
road (left). - [Your last successfully executed action] Place items into the insulated bag using: "order 1: 3 -> B; 1,2 -> C".
### recent_errors
Attempted to rest, but the action failed because the agent was not inside a designated rest area.
### last_step_plan
Continue by heading toward the pickup location for Order #0, and then proceed to (-292.89m, 212.56m) to retrieve the scooter...
Agent State Block Spatial Map Block Interaction Memory Block
Figure5.Overviewoftheinputpromptusedbydeliveryagents
B.5.OrderAttributes dissatisfactionandlowerratings.
Base Delivery Pay. Each delivery order includes a fixed
Orders serve as the fundamental task units in our simula-
base wage, which is granted in full if the agent completes
tion. Eachorderspecifiesadesignatedpickuprestaurant,a
the delivery within the specified time window or a short
drop-offaddress,adeliverytimewindow,andanassociated
grace period (e.g. 1 minute). For late deliveries, the base
wage. Some orders may also include special customer re-
pay is proportionally reduced based on the delay duration,
quests,whichagentsmustcarefullyconsiderduringfulfill-
butneverfallsbelow30%oftheoriginalamount.
ment. Upon successful delivery, the system automatically
settles the base wage and applies any additional bonuses Customer Rating Bonus. Upon successful delivery, the
basedoncustomerratings. customerprovidesaratingfrom0to5basedonoverallsat-
isfaction. This rating influences the agent’s compensation
Delivery Methods. Agents may choose from four deliv- through a bonus or penalty mechanism. The score reflects
ery methods: leaving the item at the doorstep, calling the threemainfactors:totalcustomerwaitingtime,foodcondi-
customer, knocking on the door, or handing the order di- tionuponarrival,andthesuitabilityofthechosendelivery
rectly to the customer. For face-to-face delivery, the agent method. If the rating exceeds 3 stars, the agent receives a
mustfirstlocatethecustomer’sactualposition(e.g.,“under bonus of upto $3. Ifthe rating falls below3 stars, a fixed
the tree near the entrance”) and approach them to trigger $2penaltyisapplied.
the handoff. The other methods only require reaching the
designatedbuildingentrance. Iftheorderincludesnocus- C.AgentInput–OutputSpecification
tomer notes, any of the four methods is acceptable. How-
In this section, we specify the delivery agent’s input and
ever,ifspecificdeliveryinstructionsareprovided,theagent
outputformats,alongwithitsactionspace.
must infer the most appropriate method from the context.
Forexample,anotesaying“I’minameeting”suggeststhe
C.1.InputPromptStructure
agentshouldleavetheitematthedoortoavoidinterruption,
whilehigh-valueitemsmaywarrantdirecthandoff. Choos- At each decision step, the agent receives an input prompt
inganinappropriatedeliverymethodcanresultincustomer that summarizes all information needed for planning and

<!-- page 15 -->

Figure6.HumaninteractionGUI.
acting. Thepromptconsistsoftwoparts: aSystemPrompt, commandsthatinvokethebuilt-inshortest-pathplanneror
which remains fixed throughout the episode, and a User through simple low-level motion steps (e.g. stepping for-
Prompt, which is dynamically updated at every step. The ward or turning around). (ii) Order-handling actions sup-
System Prompt specifies the agent’s role in the simulated port core delivery operations such as browsing the order
city,itsprimarydeliveryobjective,andtheavailableaction pool, accepting orders, and completing drop-offs. (iii) In-
space.TheUserPromptthenprovidesthreeadditionalcom- ventory and resource management actions involve man-
ponents:(i)anAgentStateblockdescribingtheagent’scur- aging the agent’s internal resources, enabling it to regu-
rentstatus, suchasitslocation, transportmode, speed, en- late stamina, battery levels, and food conditions (e.g. rest-
ergylevel,andactiveorders;(ii)aSpatialMapblockencod- ing, inspecting the bag, consuming energy drinks or bat-
ing a compact map snapshot, including the next reachable terypacks). (iv)Socialandcollaborationactionsfacilitate
waypoints, nearby intersections, and the locations of rele- multi-agent assistance, including viewing or posting help
vantPOIs;and(iii)anInteractionMemoryblockrecording requests,acceptingcooperativetasks,andsimplecommuni-
recentactions,thepreviousstep’splan,andanyerrormes- cation. (v)Transportationactionsallowtheagenttoswitch
sagesfromfailedactions. SometimestheUserPromptalso transportationmodes,rentorreturnvehicles,orusethepub-
includes context-specific information; for example, arriv- licbussystem.
ingatarestaurantrevealsthelistofavailablepickups,and
invoking an order-viewing action inserts the current order D.HumanDataCollection
poolintotheprompt. Anexampleofthefullpromptstruc-
tureisshowninFigure5. To obtain a reasonable human performance reference and
collect data for supervised fine-tuning, we recruited three
C.2.OutputFormat human participants, each completing a two-hour delivery
session independently. All experimental settings and eval-
Theagentfollowsafixedstructuredformatwhenproducing uation protocols were kept identical to those used for the
itstextualoutput. Itfirstreflectsonitsrecentmemoryand VLM agent. The resulting human trajectories were then
currentstatetoformulateaReflectionandReasoningpara-
augmentedusingGPT-4otogeneratethecorrespondingre-
graphthatexplicitlyarticulatesthethoughtprocessbehind flection,reasoning,andfuture-planannotations.
thecurrentdecision.Basedonthisreasoning,theagentthen
outputsanActionspecifyingtheconcreteoperationtoexe- D.1.HumanInteractionGUI
cute. Finally, it provides a Future Plan describing how it
Human participants interacted with the environment via a
intendstoproceedaftercompletingthecurrentaction.
custom-designed GUI that provides first-person observa-
tions, a map view, and contextual task information. Par-
C.3.ActionSpace
ticipantsissuedtheiractionsdirectlythroughtheinterface.
In DeliveryBench, the agent selects from a discrete ac- During delivery, the GUI displays real-time information
tion space of 30 actions, organized into several functional such as the participant’s remaining stamina, current loca-
categories: (i) Movement actions allow the agent to nav- tion,andaccumulatedearnings. Allhumantrajectoriesare
igate across the city, either through high-level navigation automaticallyloggedbythesystem. Adetailedillustration

<!-- page 16 -->

Table9.Fine-grainedmetricsfordeliveryagents;arrowsindicatewhetherhigher(↑)orlower(↓)valuesarebetter.
Dimension Metric Definition Range
Averagerelativequalityoftheordersselectedbytheagent,evaluatedbasedon
delivery-deadlinefeasibilityrelativetodistance,rewardrelativetocost,andthe
Planning Order(Quality)↑ alignmentbetweentheorder’sdeliveryrouteandtheagent’scurrenttrajectory. [0,5]
Candidateordersarescoredandrankedwithinthepool,withhigher-rankedorders
indicatinghigherquality.
OnTime(Rate)↑ Proportionofselectedordersdeliveredbeforetheirdeadlines. [0,1]
Sumofeffectivedeliverydurationsforalldeliveredorders,includingperiods
wheremultipleordersarehandledinparallel,dividedbythetotalepisodetime.
TimeEff(Time
Valuesgreaterthan1indicatethattheagentfrequentlyhandlesmultipleordersin [0,1]
Efficiency)↑
parallel,valuescloseto1indicatethattheagentisalmostcontinuouslyengagedin
deliveries,andvaluesbelow1indicatesubstantialidletimebetweendeliveries.
Fractionoftimespentperformingpurposefulactions(e.g.moving,pickingup,
Active(Rate)↑ [0,1]
delivering,recharging),excludingwaitingorincapacitatedperiods.
Resources StaminaUse↓ Averagestaminaconsumptionperhour. ≥0
Numberofforcedinterruptionsperhourcausedbyresourcedepletion(e.g.
Interrupts↓ ≥0
staminaorbatteryexhaustion).
Prevention↑ Fractionoftimestheagentreplenishescriticalresourcesbeforetheyaredepleted. [0,1]
Proportionofordersthatincurconstraintviolations,suchasfood-qualityfailures
Physical&Env. Violations↓ [0,1]
(e.g.melting,breakage,orodortransfer).
FoodRate↑ Averageratingofthefood’sfinalqualityupondelivery. [0,5]
Averagecustomerratingforeachdeliveredorder,reflectingoverallsatisfaction
CustRate↑ [0,5]
withfactorssuchaswaitingtime,deliverybehavior,andfoodcondition.
oftheGUIisprovidedinFigure6. E.2.PlanningStyleEvaluationPrompts
D.2.LLM-enhancedAnnotation WeuseGPT-4oasanevaluatortoassesstheplanningstyle
exhibitedbyeachmodel. Ateachevaluationstep, GPT-4o
Since the human trajectories only record the actions cho-
isgiven(i)thecurrentenvironmentobservationand(ii)the
sen at each step, we use GPT-4o to reconstruct the full
model’s full output, which includes the chosen action, its
chain-of-thoughtannotationsinthesamestructuredformat
chain-of-thought rationale, and the resulting consequences
described in Appendix C.2, ensuring consistency with the
ofthatdecision(e.g.,whetheranacceptedorderlatertimes
VLM agent’s outputs. For each human decision step, we
outorwhethertheactionleadstofuturebatterydepletion).
provideGPT-4owiththecorrespondingobservationandex-
GPT-4o then scores this decision across multiple planning
ecutedaction,promptingthemodeltoinfertheunderlying
dimensions. Thecompleteevaluationpromptusedforscor-
rationalebehindthedecision. Wefurthersupplythesubse-
ingisshowninFigure7.
quentfivehumanactionstoGPT-4o,enablingittogenerate
thefutureplanalignedwiththoseactions.
F.AdditionalExperimentalResults
E.EvaluationDetails
F.1.InteractionFrequencywithTeamSize
E.1.Fine-grainedMetricDefinitions
Inthemulti-agentsetting,weevaluatehowinteractionfre-
To analyze agent behavior beyond final delivery profit, we quency among models changes with team size, as shown
adoptasetoffine-grainedmetricsthatcapturedifferentas- inFigure8. Althoughthecommunicationratetendstoin-
pectsoflong-horizondeliveryperformance. Thesemetrics crease in larger teams, agents still interact only occasion-
assess high-level planning (order selection, deadline han- ally. However, this increase in communication does not
dling, timeutilization), resourcemanagement(staminaus- improve task performance. As team size grows, coordina-
ageandproactivereplenishment),andphysicalorenviron- tion becomes more complex. Agents must balance maxi-
mental adaptation (food quality, constraint violations, cus- mizing their own utility with supporting their teammates,
tomer satisfaction). Their formal definitions and computa- whichmakeseffectivecooperationmoredifficult. Asare-
tionmethodsaresummarizedinTable9. sult,agentsoftenoverreacttoteammaterequestsandaban-

<!-- page 17 -->

Input Prompt for Planning Style Evaluation
You are a step-level evaluator for a delivery agent.
For each evaluation step, you will receive: (1) a GLOBAL MAP image, (2) a LOCAL MAP image, and (3) TEXT containing the agent’s
prompt (observation/rules/context), (4) the agent’s JSON output for THIS step, and (5) the resulting consequences of the chosen action.
Your task is to assign 0–10 scores for the behavioral dimensions defined below. CRITICAL: Use ONLY the evidence present in THIS step’s
materials. If a dimension is not evidenced in this step, assign -1 for that dimension.
Scoring dimensions (integers in [0,10], or -1 if not evidenced):
1) Risk (risk-taking vs conservatism): 10 = clearly high-risk behavior (e.g., preferring far or high-reward orders; continuing long-distance
delivery with insufficient resources; accepting multiple orders simultaneously and attempting concurrent delivery.) 0 = strongly conservative
behavior (e.g., one safe order at a time, pre-emptive charging/resting).
2) Horizon (long-term planning): 10 = explicit multi-step foresight (e.g., linking destinations, choosing spatially aligned orders; purchasing
items for future benefit, or future plans extending beyond the next step). 0 = purely myopic, one-step reasoning.
3) Explore (strategy diversity): 10 = use of non-routine tools or strategies beyond the standard charge→accept→pickup→deliver loop (e.g.,
renting vehicles, taking buses, purchasing functional items, using alternative coordination strategies). 0 = strictly routine behavior.
4) Coop (collaboration): 10 = clear evidence of proactive collaboration (e.g., initiating coordination or dialogue with teammates; offering
help, requesting assistance, jointly handling orders, or adjusting plans to support others). 0 = purely individualistic behavior focused solely
on the agent’s own tasks, with no attempt to cooperate.
5) Detail (attention to operational constraints): 10 = careful handling of perishables, temperature-sensitive items, fragile goods; correct drop-
off methods, timing windows, melting risk, etc. 0 = clear oversight of important constraints.
6) Flex (adaptability to state changes): 10 = evident plan adjustments based on new information (e.g., noticing low battery and rerouting to
charge; correcting mistakes). 0 = blindly following an outdated plan.
Output policy:
Judge ONLY from THIS STEP’s provided materials (text, maps, action, and consequences); If the model output is malformed or missing, the
step is skipped by the caller; Return JSON ONLY with EXACT keys and integer values: {"Risk": int, "Horizon": int, "Explore": int, "Coop":
int, "Detail": int, "Flex": int}; No extra keys, no commentary, no markdown.
Figure7.Promptforplanningstyleevaluation.
dontheirowntasks,ortheypromisehelpbutfailtofollow tionandoftenuselessefficienttransportationmodes(e.g.,
through,leavingbothsidesstalled. walkingordraggingscooters). Theirspendingpatternsare
summarized in Figure 11, and their transportation prefer-
encesareillustratedinFigure12.
GPT-4o Qwen2.5-32B Qwen2.5-72B LLaMA-90B
A passionate yet A steady but A similar balancer, but A low-awareness
stubborn doer ordinary balancer even weaker than 32B. bumbler
The delivery was I’ll head toward the I've accepted Order I am currently
Figure8.Interactionfrequencyacrossteamsizes. interrupted because I pickup point to save #0. The food is still towing a scooter
ran out of stamina, time, check if being prepared, so with 0% battery and
causing a 35-minute temperature packs I'll head there and have 3% energy.
F.2.ModelBehaviorsandPlanningStyles delay. My priority are needed for the wait. Then I’ll My active order #10
now is to resume food, and recharge deliver it and accept is already picked up
delivery of order #16 the scooter if new orders... and needs to be
In addition to the three examples of model planning styles and complete... necessary to... delivered to...
shown in Figure 3, we evaluate the behaviors of all mod- Still delivers even Considers everything, Considers everything, Fails to realize the
with severe overtime. but shallowly. but shallowly. need to recharge.
els, with the remaining results presented in Figure 9. We
further analyze each model’s action distribution, spending
Figure9.Planningstylevisualizationsfortheremainingfourmod-
patterns, and transportation choices. As shown in Fig-
els,complementingtheexamplesshowninFigure3.
ure 10, Stronger models such as GPT-5 and Claude-3.7-
Sonnetexhibitbroaderactioncoverageandemployaricher
F.3. Detailed Results for Context Engineering and
set of strategies, such as renting cars or purchasing tools.
SupervisedFine-tuning
In contrast, weaker open-source models such as LLaMA-
3.2-90B-Vision-Ins primarily rely on simple pickup-and- We provide additional experimental results and analyses
deliveryroutines. Theseweakermodelsalsoendupspend- that complement the studies presented in Section 5.5, in-
ing more money on hospital rescues due to stamina deple- cluding more detailed metric breakdowns and illustrative

<!-- page 18 -->

Figure10. Actiondistributionsofdifferentmodels. Foreachmodel,theouterbarsindicatetherelativefrequencyofattemptedactions,
whiletheinnerbarsshowthecorrespondingsuccessrates.
riesproducessignificantimprovements. Inparticular,time-
efficiency scores even exceed those of large models such
asGPT-5andClaude-3.7-Sonnet,indicatingthatthemodel
successfullylearnsthehumanstrategyofhandlingmultiple
ordersinparallel.
Context Engineering Case Study. We present example
notebooks generated by Claude-3.7-Sonnet and Qwen2.5-
VL-72B under Agentic Context Engineering (ACE). In
thissetting,eachmodelautonomouslysummarizespatterns
Figure11.Expendituredistributionacrossmodels. from its past trajectories and maintains these summaries
as persistent memory to guide future deliveries. For each
model, we select the ten highest-quality examples, shown
in Figure 13 and Figure 14. Both models extract princi-
ples covering multiple aspects of delivery, including time
management and resource planning, and their summaries
closelyalignwiththeunderlyingtaskrules. Incomparison,
Claude-3.7-Sonnet produces more detailed and actionable
guidelines, which in turn contributes to its larger perfor-
manceimprovementwhenACEisapplied.
Figure12.Transportationmodedistributionacrossmodels.
F.4.AblationStudies
case studies of model-generated summaries under context PlanningAblation. Wefurtheranalyzetheresultsreported
engineering. in Table 5, which compare models that perform explicit
plan-and-execute reasoning with models that directly out-
Fine-grained Analysis. We further analyze model per-
put a single action. For GPT-5 and Qwen2.5, planning
formance along three dimensions: high-level planning, re-
consistently improves most capability metrics and leads to
source management, and physical or environmental adap-
highernetprofit.Incontrast,Claude-3.7-Sonnetearnsmore
tation. As shown in Table 10, context engineering gen-
when planning is enabled, but its net profit decreases be-
erally leads to higher on-time delivery rates, better time
causeofincreasedexpenses. Theseadditionalcostsmainly
efficiency, and a larger active-time ratio, which allow the
arisefromoverplanning, suchasrepeatedlyrechargingthe
models to complete more orders and achieve higher earn-
e-scooterwhenthebatterylevelisalreadysufficientorpur-
ings. However, the gains in resource management and en-
chasingitemsthatarenotimmediatelynecessary.
vironmental handling are less substantial. For the human-
trajectory fine-tuning experiments, fine-tuning directly on Waypoint Ablation. We evaluate whether VLM agents
raw actions results in noticeable declines across multiple can navigate without privileged spatial priors. We remove
capabilities. In contrast, fine-tuning on annotated trajecto- preset waypoints and restrict them to step-by-step nav-

<!-- page 19 -->

Table10. Fine-grainedmetricsforplanning,resourceusage,andphysical/environmentalbehaviorundercontextengineeringandsuper-
visedfine-tuning.Greenhighlightsimprovementsandreddenotesregressionsoverthewith-Planbaseline.
Planning Resources Physical&Env.
Model
Order↑ OnTime↑ TimeEff↑ Active↑ Stamina↓ Interrupts↓ Prevention↑ Violations↓ Food↑ Cust↑
GPT-5(withPlan) 3.38 0.32 0.94 0.56 1.35 1.35 0.72 0.65 3.95 3.79
GPT-5(w/oPlan) 3.24 0.25 0.45 0.48 1.32 1.86 0.48 0.75 3.35 3.20
GPT-5(withPlan+ACE) 3.62 0.33 0.88 0.63 1.66 2.50 0.62 0.89 3.56 3.56
GPT-5(withPlan+DC) 3.41 0.37 1.08 0.68 1.29 2.96 0.79 0.68 3.83 4.04
Claude-3.7-Sonnet(withPlan) 3.46 0.41 0.92 0.59 0.78 0.64 0.77 0.62 3.80 3.72
Claude-3.7-Sonnet(w/oPlan) 3.28 0.37 0.58 0.54 1.05 0.39 0.77 0.78 3.88 3.76
Claude-3.7-Sonnet(withPlan+ACE) 3.38 0.60 0.96 0.82 0.79 0.50 0.91 0.70 4.00 4.30
Claude-3.7-Sonnet(withPlan+DC) 3.41 0.52 1.06 0.77 1.22 1.06 0.54 0.72 3.92 4.16
Qwen2.5-VL-72B(withPlan) 3.12 0.17 0.40 0.53 1.38 1.50 0.53 0.70 4.11 3.73
Qwen2.5-VL-72B(w/oPlan) 3.07 0.21 0.38 0.51 1.42 2.13 0.24 0.75 3.61 3.35
Qwen2.5-VL-72B(withPlan+ACE) 2.97 0.14 0.88 0.63 1.76 3.00 0.40 1.00 3.80 3.40
Qwen2.5-VL-72B(withPlan+DC) 3.49 0.36 0.59 0.72 0.98 1.26 0.44 0.62 4.16 4.03
LLaVA-OneVision-8B(original) 3.22 0.05 0.15 0.50 2.32 2.49 0.16 0.74 3.67 3.52
LLaVA-OneVision-8B(human-ft) 3.05 0.06 0.72 0.38 2.49 2.99 0.14 0.82 3.63 3.04
LLaVA-OneVision-8B(annotated-ft) 3.36 0.16 1.51 0.88 0.64 2.38 0.47 0.58 4.02 3.96
Claude-3.7-Sonnet–Generated ACE Notebook
• When both scooter battery and personal energy are critically low, prioritize addressing vehicle battery first unless personal energy is
below 25%, as mobility is typically the more constraining resource.
• Before abandoning a scooter due to battery depletion, calculate whether purchasing a battery pack would be more time and energy
efficient than walking to a charging station and back.
• Maintain a continuous awareness of nearby resource restoration points (charging stations, stores, rest areas) and incorporate them into
route planning before resources reach critical levels.
• When managing multiple resource needs, plan a route that minimizes total travel distance by addressing needs at locations in close
proximity rather than treating each need as a separate journey.
• When multiple resource needs exist simultaneously (low personal energy, low scooter battery, pending orders), prioritize based on
urgency and proximity to create efficient multi-objective routes.
• Add a 5-minute buffer to all delivery time estimates to account for unexpected delays, traffic, or resource management needs that may
arise during delivery.
• Before accepting orders, calculate the total journey distance (to pickup + to delivery + return to strategic location) and verify both
personal energy and scooter battery are sufficient with at least a 40% buffer.
• Before accepting new orders, check the map for nearby resources (stores, charging stations, rest areas) to ensure access to necessary
replenishment options during the delivery journey.
• Avoid accepting orders that require significant backtracking, especially when handling overtime deliveries that require direct routing to
minimize further delays.
• Before accepting distant orders, evaluate all available transportation options (walking, scooter, public transit) based on current location
and resource levels to determine the most efficient delivery method.
Figure13.ExampleACEnotebookgeneratedbyClaude-3.7-Sonnet.
Qwen2.5-VL-72B–Generated ACE Notebook
• While waiting for orders to be prepared, use the time to scout for nearby orders or pre-plan delivery sequences to optimize efficiency.
• When battery level drops below 20%, immediately prioritize moving to the nearest charging station before continuing deliveries.
• Prioritize high payout-to-distance ratio orders when selecting batches to maximize efficiency and profitability.
• When multiple orders are ready simultaneously, batch them based on similar drop-off directions to minimize backtracking and save time.
• Regularly monitor energy levels and plan routes that include charging stations if needed, especially during long delivery sequences.
• Consider the urgency of orders (overtime status) when planning delivery sequences to minimize penalties and improve customer
satisfaction.
• Utilize the map snapshot effectively to identify optimal paths and avoid unnecessary detours, ensuring efficient use of time and resources.
• Consider alternative orders with shorter preparation times when faced with long wait times at pickup locations.
• Monitor energy levels and plan breaks accordingly to maintain optimal performance throughout the shift.
• Always assess the feasibility of new orders against current battery and energy levels to avoid overcommitting.
Figure14.ExampleACEnotebookgeneratedbyQwen2.5-VL-72B.
igation using only low-level actions (STEP FORWARD, dicatingthatcurrentmodelsstruggletotranslatevisualun-
TURN AROUND) with egocentric observations. Agents derstanding into embodied navigation. Explicit spatial co-
fail to complete even a single order under this setting, in- ordinatesremainadependencyforthesemodels.

<!-- page 20 -->

F.5.VarianceandStabilityAnalysis
We further evaluate the stability of model performance
under repeated runs. For both Gemini-2.5-Flash and
Qwen2.5-VL-72B-Ins, we conduct three experimental
groups, each following the same setup as the main exper-
iment and consisting of eight independent runs along with
theiraveragedresults. AsshowninTable11,overall,both
modelsexhibitlowvarianceacrossruns,demonstratingsta-
bleandreliableperformanceunderidenticalconditions.
Table11. Meanvaluesandrun-to-runvariabilityforGemini-2.5-
FlashandQwen2.5-VL-72B-Ins.
Metric Gemini-2.5-Flash Qwen2.5-VL-72B-Ins
P¯ $28.46±2.52 $5.96±2.82
E $37.55±2.11 $13.28±2.90
C -$9.09±1.32 -$7.32±0.96
Order 3.32±0.11 3.07±0.09
OnTime 0.30±0.07 0.18±0.05
TimeEff 0.88±0.08 0.45±0.04
Active 0.52±0.04 0.50±0.05
Stamina 1.03±0.06 1.42±0.09
Interrupts 1.79±0.05 1.57±0.10
Prevention 0.78±0.06 0.55±0.08
Violations 0.70±0.11 0.68±0.14
Food 4.08±0.11 4.01±0.17
Cust 3.77±0.20 3.62±0.25
