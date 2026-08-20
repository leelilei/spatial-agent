Title: 06_MultiAgentBench_Zhu2025

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/01_LLM_Game_Agents/06_MultiAgentBench_Zhu2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:06:40+00:00
- page_count: 42
- status: ok
- text_char_count: 146220

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

MultiAgentBench : Evaluating the Collaboration and Competition of
LLM agents
KunlunZhu1† ∗,HongyiDu1†,ZhaochenHong1†,XiaochengYang1†,ShuyiGuo1†,ZheWang1 †
ZhenhailongWang1,ChengQian1,XiangruTang,HengJi1,JiaxuanYou1
1UniversityofIllinoisUrbana-Champaign
kunlunz2@illinois.edu
Abstract leveragemultipleLLM-basedagentsthatcollabo-
rate,coordinate,andjointlyplantoaddressthese
LargeLanguageModels(LLMs)haveshown
challenges. Thisparadigmnotonlyincreasesthe
remarkablecapabilitiesasautonomousagents;
efficiency of task execution but also enables the
yetexistingbenchmarkseitherfocusonsingle-
realistic simulation of social interactions and dy-
agenttasksorareconfinedtonarrowdomains,
namics,therebyenhancingperformanceindomains
failingtocapturethedynamicsofmulti-agent
coordination and competition. In this paper, suchasstrategicdecision-making,gaming(Silver
we introduce MultiAgentBench, a compre- et al., 2017), and software development (Wang
hensivebenchmarkdesignedtoevaluateLLM- etal.,2023c).
based multi-agent systems across diverse, in-
teractivescenarios. Ourframeworkmeasures
not only task completion but also the qual-
ity of collaboration and competition using
novel,milestone-basedkeyperformanceindi-
cators. Moreover, we evaluate various coor-
dinationprotocols(includingstar,chain,tree,
and graph topologies) and innovative strate-
gies such as group discussion and cognitive
planning. Notably,gpt-4o-minireachestheav-
erage highest task score, graph structure per-
formsthebestamongcoordinationprotocols
intheresearchscenario,andcognitiveplanning
improvesmilestoneachievementratesby3%.
Figure1: OverviewofMultiAgentBenchevaluation
Codeanddatasetsarepublicavailableathttps:
process: Multi-AgentSystemCoordinationinvarious
//github.com/MultiagentBench/MARBLE.
interactiveenvironments, withafocusontaskperfor-
mance,andcoordination.
1 Introduction
Large Language Models (LLMs) such as GPT-3 Despite significant advances in LLM capabili-
(Brownetal.,2020),GPT-4(Achiametal.,2023), ties, current evaluation paradigms remain insuffi-
Gemini(Teametal.,2023)andDeepsek-R1(Guo cientformulti-agentscenarios. Traditionalsingle-
etal.,2025),nowexhibithuman-likelanguageun- agent benchmarks—such as AgentBench (Liu
derstandingandgeneration,enablingtheiruseas etal.,2023),VisualAgentBench(Sunetal.,2023)
autonomousagentsinteractingwithenvironments, GAIA(Mialonetal.,2023),ToolBench(Qinetal.,
tools, and other agents (Wang et al., 2023c; Park 2024) and HumanEval (Chen et al., 2021)—pri-
etal.,2023a;OpenAI,2023). Whilesingle-agent marilyfocusonisolatedreasoningandgeneration,
systemshavedemonstratedimpressivecapabilities, overlookingthedynamicsintrinsictomulti-agent
theirisolatedoperationcanlimittaskexecutioneffi- interactions.
ciencyandfallsshortwhensimulatingcomplex,so- Toaddressthisgap,weintroduceMultiAgent-
ciallydynamicscenarios. Incontrast,multi-agent Bench, a comprehensive benchmark designed to
setups(Lietal.,2023a;Wangetal.,2023b,2024b) evaluateLLM-basedmulti-agentsystemsacrossa
widerangeoftask-solvingandsimulationscenar-
∗TeamLeader.
ios. MultiAgentBench offers several key advan-
†CoreContributors. Contributionsarelistedintheap-
pendixA.1. tages: (1) Multi-Domain Evaluation: The bench-
5202
raM
3
]AM.sc[
1v53910.3052:viXra

markcoversdiversedomains—fromcollaborative maintenance(Bouzeniaetal.,2024),andgaming
codingtogaming—ensuringbroadreal-worldap- applications (Chen et al., 2023a). In Minecraft,
plicability. (2)CapturingCoordinationandCom- agentsperformcomplextasksfromconstructionto
petition: Unlike traditional single-agent bench- navigation(Wangetal.,2023a;Chenetal.,2023b;
marks,MultiAgentBenchexplicitlymeasuresboth Yuetal.,2024b;Dongetal.,2024).
coordination dynamics and competitive interac- GameNGen enables real-time interaction
tions,highlightingtheuniquechallengesofmulti- in DOOM (Valevski et al., 2024), while
agentenvironments. (3)TailoredMetricsandFlex- CUISINEWORLD benchmarks multi-agent
ibleProtocols: Weproposenovelmetrics,includ- collaboration (Gong et al., 2023). Applications
ingaKeyPerformanceIndicator(KPI)thattracks extendtosocialdeductiongames,gametheory(Xu
milestoneprogressandindividualcontributions,to etal.,2023),healthcare(Keetal.,2024;Kimetal.,
systematicallyassessplanningqualityandcommu- 2024), business (Chen et al., 2024), education
nicationeffectiveness. Moreover,ourframework, (Gösling et al., 2024), and urban planning (Zhou
MARBLE(Multi-agentcooRdinationBackbone et al., 2024b). Despite progress, challenges
withLLMEngine),supportsvariouscommunica- persistincommunication,emergentbehavior,and
tion topologies—such as star, chain, tree, and an scalability (Agashe et al., 2024), motivating the
innovativegraph-basedapproach—andaccommo- needforrobustevaluationframeworks.
datesmultiplereasoningstrategies.
2.2 Multi-AgentCollaboration
Ourcontributionscanbesummarizedasfollows:
(1) We introduce MultiAgentBench along with Recentadvancesinmulti-agentsystemshighlight
theMARBLEframework,acomprehensivebench- two complementary scaling paradigms: cogni-
markthatrigorouslyevaluatesLLM-basedmulti- tivescaling,whichenhancesagentreasoningand
agentsystemsinsixdiverseinteractivescenarios, adaptability,andpopulationscaling,whichlever-
capturing both collaborative and competitive dy- ageslargeagentcollectivesforemergentbehaviors
namics. Notably,thecognitiveplanningplanning (Zhugeetal.;Qianetal.,2024).
feature improves milestone achievement rates by Cognitive scaling explores mechanisms such
3%. (2) We propose innovative evaluation met- as dynamic architecture adaptation and self-
ricsthatassessnotonlytasksuccessbutalsocoor- organizingcoordinationstrategiestofindthemost
dination quality. Our metrics include milestone- effectivepatternofagentcommunication(Zhuge
based KPIs, structured planning and communi- et al.). Meanwhile, population-based scaling ex-
cation scores, and a dedicated competition score hibitsnonlinearperformancegainsasanincreasing
that captures conflicting-goal tasks, internal per- numberofagentscollectivelyinteractthroughdi-
formancemetrics,andcompetitiveaspectsinplan- versecollaborationpatterns,includinghierarchical
ningandcommunication. (3)Ourexperimentsre- delegationanddecentralizedconsensus(Qianetal.,
vealsome"aha-moments"inmulti-agentcoordina- 2024). Theseapproachesenablecomplexapplica-
tion—agentsbegintoexhibitemergentsocialbe- tionsrangingfromgeopoliticalconflictsimulation
haviors,providingpromisinginsightstowardAGI- (Huaetal.,2024)toscientificdiscoveryworkflows
levelcollaboration(Fengetal.,2024). (Zhouetal.,2024a;Zhangetal.,2025).
2 RelatedWork 3 Methodology
2.1 LLM-BasedMulti-AgentSystems 3.1 FrameworkDesign
LLM-basedmulti-agentsystemshaveenabledcol- Our proposed evaluation framework MAR-
laborativeproblem-solvingacrossdomains(Park BLE(seeFigure2)establishesarobustmulti-agent
etal.,2023a;Lietal.,2023b;Chenetal.,2023b). coordinationsystembyleveraginginterconnected
Thesesystemssupportscientificresearchthrough modules that enable adaptive collaboration, effi-
literature review and experimental design (Zhou cientcommunication,andstrategictaskexecution.
etal.,2024a;Agarwaletal.,2024),softwareengi- At its core lies the Coordination Engine, respon-
neeringtasks(Huangetal.,2023;Wuetal.,2023a; sible for initializing and synchronizing key mod-
Zhouetal.,2023a;Hongetal.,2024;Ishibashiand ules—includingtheAgentGraph,CognitiveMod-
Nishimura, 2024; Islam et al., 2024; Wang et al., ule, and Coordinate Engine—to ensure seamless
2024a;Zhugeetal.) includingcodegenerationand interaction across the system. Detailed descrip-

a Configuration 2. Agent Graph b Collaboration
Coordinate Engine
Contruction 3. Reasoning &
Reflection
Task Info 4. Interaction to
the environment
Agent Graph
1. Feed in agent 9. Pass
Persona specification observation
Data c
Domain 10. Metadata to 5, m 8. e U m p o d r a y te Lo M n e g m -T o e r r y m S Te h r o m rt M S e h m ar o e r d y
Database the evaluator 6. Pass with RAG Memory
7. Return interaction
observation to the
f environment
e
Evaluator d
Collaboration Score Interaction Cognitive
& Environment Tool Box & Module
Task Score Experience
Figure 2: MARBLE : showcasing interactions between task information, persona data, domain databases,
memorymodules,andtheenvironmentthroughthecoordinateengineandcognitivemodule.
tions of additional modules can be found in Ap- collaborativelyevolveincomplexenvironments.
pendixA.2.
3.1.1 CoordinationEngine
Agent Graph Module This module converts
TheCoordinationEngineorchestratestheoverall
configuration data into a structured graph G =
executionflowofthesystem. Itinitializesagents,
(A,E), where A = {a ,a ,...,a } denotes
1 2 n tasks,andinter-agentrelationshipsviaadedicated
the set of agents, and each edge in E is de-
Configuration Module and constructs the Agent
fined as a triple (a ,r,a ) with r ∈ R repre-
i j Graphtorepresentthesedynamics. Inourframe-
senting the relationship between agents a and
i work,wedistinguishbetweentwokeyroles: plan-
a . For example, a collaboration relationship
j nersandactors. Plannersareresponsiblefordevis-
is denoted as (a ,collaborates,a ), supervi-
i j ingtaskinputs,strategizing,andmanagingoverall
sion as (a ,supervises,a ), and negotiation as
i j taskallocation,whileactors—representedwithin
(a ,negotiates,a ). By constructing the graph
i j theAgentGraph—executetasksbyinteractingwith
basedonthesetriplerelations,weensurethatsub-
theenvironmentandotheragentsthroughavailable
sequentcommunicationandcoordinationoccurex-
tools.
clusively between agents with explicitly defined
Ourapproachsupportsfourdistinctcoordination
relationships,mirroringreal-worldinteractionpat-
protocolssimilartoworkfromQianetal.(2025):
terns.
star,tree,graph,andchain.
CognitiveModule TheCognitiveModuleiscen-
CentralizedCoordination: Star&Tree. Inthe
tral to responsible agent evolution and social in-
starconfiguration,asinglecentralplannerassigns
telligence in multi-agent coordination. It main-
taskstoallactorsandconsolidatestheirfeedback,
tains and updates a comprehensive internal state
offeringstrongoversightthoughpotentiallylimit-
thatincludeseachagent’spersona,inter-agentre-
ingscalability. Thetreestructureextendsthisby
lationships, andreasoningstrategies(e.g., Chain-
organizingagentshierarchically: atop-levelplan-
of-Thought(Weietal.,2023),ReACT(Yaoetal.,
nerdelegatestaskstosubordinateplanners,which
2023)). Crucially, this approach mirrors human
inturncoordinatewithactors. Thishierarchicalap-
cognitiveprocessesbyfusingelementsoftheory-
proachbalancescentralizedcontrolwithimproved
of-mindandsocialintelligence(e.g.,Premackand
scalabilityforhandlingmorecomplextasks.
Woodruff,1978)—similartohowhumanscontinu-
ouslyupdatetheirmentalmodelsbasedonsocial Decentralized Coordination: Graph-Mesh &
cues,priorexperiences,andcontextualinformation. Chain. Thegraph-meshconfigurationemploys
Thefusionofcognitive,social,andadaptivemecha- a network of interconnected actors that commu-
nismsformsthebackboneofoursystem,empower- nicatedirectly,enablingconcurrentplanningand
ingagentstodynamicallyadjusttheirstrategiesand distributeddecision-making. Conversely,thechain

a. Coordination Protocol b. Planning Prompt Strategy
Star Tree
VVVaaannnililliallala CCChhhaaaininin--o-ooff-f-T-TThhhooouuuggghhhttt GGGrroroouuuppp D DDisisiscccuuussssssioioionnn
Actor Planner
Centralized Planner Planner/ Cognitive Evolve Planning
Planner Actor
Task Planner
Actor Actor
Graph-Mesh Chain Experience Expectation Task Plan
Agent4
Decentralized Agent3 Update
Self-Planning
Agent1 Cognitive Agent
Agent1 Agent2 Agent3 Module
Result
Agent2
Figure3: Illustrationofcoordinationprotocolsandplanningpromptstrategies. (a)showscentralizedand
decentralizedplanningstructures(e.g.,star,tree,graph,andchain). (b)describesstrategieslikegroupdiscussions
andcognitiveprompts,incorporatingiterativefeedbackandtaskupdatesforeffectiveplanning.
configurationarrangesactorssequentially,where ablationstudiesonthestarcoordinationstyle.
each agent passes its decision to the next. This
3.2 BenchmarkDesign
sequentialhandoffiswell-suitedfortaskswithin-
herentdependencies,thoughitmaylimitparallel Tosystematicallyevaluateourmulti-agentframe-
processingcapabilities. work, we curate a benchmark of diverse scenar-
iosspanningtask-oriented andsocial-simulation-
PlannerDesignandEnhancements. Inourcen-
based environments (Figure 1). These scenarios
tralizedcoordinationprotocol,theplannersupports
areconstructedthroughacombinationof: (1)Ex-
four distinct planning approaches that reflect hu-
isting multi-agent tasks adapted from prior work
mandecision-makingprocesses: vanillaprompting,
ordatasets(e.g.,databaseerroranalysis,research
chain-of-thought (CoT) (Wei et al., 2022), group
collaboration). (2)LLM-generatedtaskswithhu-
discussion, and cognitive self-evolving planning.
man verification and refinement (e.g., Werewolf
The vanilla prompt employs a straightforward,
andBargaining). Thisdualapproachensuresboth
zero-shotinstructiontogeneratetaskplansdirectly.
realism(byleveragingestablishedtasks)andnov-
TheCoTapproachenrichesthisprocessbyfacili-
elty(throughgenerativeexpansion),whilehuman
tatingstep-by-stepreasoningthroughdetailedin-
validation guarantees that each scenario remains
puts—suchasthetargettask,agentprofiles(includ-
coherentandfeasible.
ing roles, expertise, and historical performance),
andsummariesofprevioussubtasks—toguidelogi- AgentswithMutualGoal. Inthetask-oriented
calprogression. Thegroupdiscussion(Chenetal., scenarios,theagentssharewiththemutualgoalto
2023b) method enables multiple agents to share finishonespecifictask. Wefocusonfourrepresen-
insightsandconstraints,fosteringacollaborative tative tasks: (1) research tasks follow the setup
deliberation that refines the overall plan. Lastly, ofResearchTown(Yuetal.,2024a),whereagents
similartotheReflexion(Shinnetal.,2023)method, with complementary research profiles co-author
ourcognitiveself-evolvingplanningmethodmir- a new proposal on a chosen topic; (2) Minecraft-
rors human learning by generating expected out- based building tasks require agents to collabora-
comesandprogressforeachtask,storingthesein tivelyconstructstructuresinasharedenvironment;
memory,andthencomparingactualperformance (3)databaseerroranalysisinvolvesexactlyfive
againsttheseexpectationsinsubsequentiterations. agents, each specializing in diagnosing a distinct
This comparison produces evolving experiences root cause of system inconsistencies; (4) coding
that continuously inform and adjust future plan- challengesdemandcollectiveproblem-solvingand
ning(SeeAppendixA.12fordetailedprompting). softwaremoduledevelopment. Acrossthesetasks,
Together,thesemethodsleveragebothindividual agents must coordinate, divide labor, and synthe-
reasoningandcollaborativeoptimization,enhanc- sizeoutputsefficiently. Wescalescenariodiversity
ing coordination efficiency as validated through bycreating100testcasespertask,withvariations

BENCHMARK CURATION & MILESTONES DETECT
Human-Generated Fixed Dataset Dynamic Milestones Detecting
collaboration Negotiation for aChair Banner. Milestones
$14.99 with a rating of 4.8/5 stars... Description
Buyer
Seller
Role
LLM generated competition
Data Bargaining Chain Task 1 Results 1 LLM
Env Agents Star KPI ++
“I’ll give you a 10% discount if you buy 2.”
Graph
Tree KPI ++
“OK. But 15%! I’ll write reviews for you!”
Real Data
Cod…ingEnv Relationship T … ask 2 “W m e i l l l e , s I t d o o n n e ’t n kn o o t w c . o .. m 1 p 5 l % et ? e E d mm...”
Figure4: IllustrationofourbenchmarkcurationandthedynamicmilestonesdetectingforKPImetric.
I’ll create an intuitive and responsive user interface.
inresearchtopics,Minecraftcreation,databaseer- sured.
rors,orcodingobjectives. More detailed environment setups, interaction
tools,andadditionalexamplesfordifferentscenar-
Initial Setup and
Agents with Conflicting Goals. In soRceqiuairle-ments iAoligsnmaepntpearinAppendixA.4, A.5, A.6, A.7, A.8,
simulationbasedscenarios. WestreMnilgesthtoenne 1compet-
and A.9.
itiveelementsbyintroducingWerewolfandCBorae Fre-ature
Development and
gaining scenarios. In Werewolf, two groupInstegoraftion 3.3 EvaluationMetrics
Milestone 2
agentsfaceoffinanadversarialsetting,employing
AsillustratedinFigure1(b)(c),ourevaluationcon-
deceptivestrategieswithinapredefinednarrative.
siderstwoprimarydimensions: TaskCompletion
TheBargainingenvironmentsimulatesnegotiations
PerformanceandCoordination.
oversharedresources,whereagentsstrivetomaxi-
TaskCompletionMetrics. AsdescribedinSec-
mizeindividualgainsthroughstrategicconcessions
tion 3.2, each task is segmented into a series of
or alliances. Both settings evaluate adaptability,
flexiblemilestones. AnLLM-baseddetectorcon-
conflictresolution,andnegotiationskillsunderun-
tinuouslymonitorstheiterativeprocesstoidentify
certainty.
whichmilestoneshavebeenachievedandrecords
Role Assignments and Graph Structures. To the corresponding contributing agents. For each
emphasizemulti-agentcollaboration,eachscenario agent, the number of milestones they contribute
enforcesdistinctagentroles(e.g.,projectmanager, to is noted as n , and their individual KPI is cal-
j
domainexpert,technicalspecialist)anddefinesspe- culated as the ratio of n to the total number of
j
cificgraphrelationships(star,tree,chain,ormesh). milestonesM. TheoverallKPIisdefinedastheav-
Thesestructuresreflectrealisticteamdynamicsor erageoftheseindividualKPIsacrossallN agents,
competition,guidinghowagentsshareinformation, whichiscomputedasfollows:
makedecisions,andcoordinateactions.
N N
1 (cid:88) 1 (cid:88)
KPI = KPI = n .
MilestonesGenerationforScenarios Tofacil- overall j j
N NM
itate the evaluation of MARBLE iterations, each j=1 j=1
task is segmented into a series of flexible mile- In addition to the KPI derived from milestone
stones. Unlikerigidcheckpoints,thesemilestones detection,aseparatetask-basedscoreiscomputed
arebroadlydefined. Forinstance,inaresearchtask, toevaluatethefinaloutputquality. Fortaskssuch
amilestonemaybereachedbycompletingfivekey as research or bargaining, an LLM-defined scor-
queries(5q)forresearchproposal(moredetailssee ingrubricisappliedtogeneratethescore,whereas
AppendixA.4)orbyenhancingaprevioussetof taskslikeMinecraft,Werewolf,databaseerrorfixes,
5q. ThroughoutMARBLE’siterativeprocess,alan- or coding are evaluated using rule-based metrics
guagemodelcontinuouslymonitorswhethermile- (e.g.,accuracy). Detailedscoringcriteriaandevalu-
stones m ,m ,... have been achieved and logs ationpromptsforthesetask-basedassessmentsare
1 2
the outcomes. This method integrates human- or respectively provided in the Appendix A.9, A.5,
LLM-generatedoutlineswithdynamic,execution- A.6,and A.7,whichdemonstratetheeffectiveness
basedassessments,ensuringthatbothintermediate of the metrics while evaluating the coordination
progressandteamcoordinationareeffectivelymea- abilities.

Coordination Metrics. Coordination is evalu- 4.2 MainExperimentOne: Model
ated by quantifying the agents’ communication PerformanceAcrossDifferentScenarios
and planning capabilities. The Communication
In this experiment, we evaluate the performance
Score(C )isderivedfromanLLM-basedeval-
score
of five models across diverse scenarios, with re-
uation that considers inputs such as the task de-
sultssummarizedinTable1. Ouranalysisleadsto
scription, agent profiles, and aggregated commu-
severalkeyinsights:
nication data, resulting in a score on a five-point
scale (with C = 0 if no communication oc-
score
1. SuperiorTaskPerformanceofgpt-4o-mini:
curs). Similarly, the Planning Score (P ) is
score
Across multiple tasks, gpt-4o-mini consis-
determinedbyassessingtheagents’abilitiestoor-
tently achieves high Task Scores (TS). For
ganize tasks, maintain roles, and adapt strategies
example, in the Research scenario it obtains
based on their profiles and aggregated planning
a TS of 84.13%, outperforming other mod-
data,alsoonafive-pointscale. TheoverallCoordi-
els such as Meta-Llama-3.1-8B (80.87%) and
nationScore(CS)isthencomputedbyaveraging
Meta-Llama-3.1-70B (80.80%). Similar trends
these two sub-scores. More details regarding the
are observed in the Coding domain, where
evaluation processand theoutput format arepro-
gpt-4o-minirecordsaTSof65.10comparedto
videdintheAppendixA.12. Wealsodidahuman
lower scores from its competitors. These results
evaluationcomparinghumanalignmentwiththose
indicatethattheunderlyingmodelcapabilitiesare
metrics,resultsareinAppendixA.3.
adecisivefactorinachievingsuperiortaskperfor-
4 ExperimentSetup mance.
4.1 ExperimentSettings
2. TheNuancedRoleofCoordination(Collab-
Models. Since our MARBLE framework re- oration)Score: WhiletheCollaborationScore
quired function-calling abilities. Thus, we con- (CS) is designed to measure coordination ability,
sider three open-source models: Meta-Llama- our findings suggest that its impact on the over-
3.3-70B (Dubey et al., 2024), Meta-Llama-3.1- alltaskperformanceiscomplex. Forinstance,in
70B-Instruct-Turbo (Dubey et al., 2024), and theMinecraftscenario,Meta-Llama-3.1-70Bex-
Meta-Llama-3.1-8B-Instruct-Turbo,aswellastwo hibits a high CS of 75.00 but an extremely low
closed-source models: GPT-3.5-turbo-0125 and TS of 0.21, a more deep analysis for this can re-
GPT-4o-mini1.We access the open-souce models fertoAppendix21. Thisdiscrepancyimpliesthat,
areprovidedbythetogetherai2 service,utilizing althoughcoordinationcontributestoperformance,
thedefaultparametersettings. it does not compensate for inherent deficiencies
Fortheagentactions,weconfigurethemodels intaskexecutioncapabilities. Incontrast,models
withamaximumtokennumber(max_token_num)
that balance both high TS and moderate-to-high
of1024,atemperatureof0.7,andatop_pof1.0, CS—suchasgpt-4o-mini—demonstratemorero-
inordertobalancethecreativityandconsistency bustandreliableperformanceacrossscenarios.
oftheagents’responsesduringinteractions. The
overallmaximumiterationsaresetto5forresearch
3. Model-Specific Strengths and Context-
and20forMinecraft;moredetailscanbefoundin
DependentPerformance: Ourresultsrevealthat
the Appendix. In our evaluation, which involves
differentmodelsexhibitvariedstrengthsdepending
both Task Completion and Simulation scenarios, on the task. For example, Meta-Llama-3.3-70B
weassessthemodelsalongtwoprimaryaxes: Task
shows a notable CS in the Research (72.00) and
Score(TS)andCoordinationScore(CS),usingthe
WereWolf (76.30) tasks, yet its TS lags behind
same metrics as described in the Metrics section. that of gpt-4o-mini in several scenarios. These
Themaximumcommunicationiterationnumberis
variations emphasize that no single metric can
alsosetto5. Furthermore,thelong-termbasemem-
fullycaptureamodel’seffectiveness;instead,both
oryforeachagentissettobeunlimited. Finally,for
task-specificabilitiesandcoordinationskillsmust
the main experiment, a graph-mesh coordination
be considered. Overall, our study underscores
protocolisadoptedtofacilitateinteractions.
that while coordination plays a role, the intrinsic
1https://www.openai.com modelcapabilitiesaretheprimarydriversofsuc-
2https://www.together.ai cessacrossdiversetasks.

Research Minecraft Database Coding Bargaining WereWolf
Model
TS CS TS CS TS CS TS CS TS CS TS CS
Meta-Llama-3.1-8B 80.87 52.40 6.12 54.40 34.00 40.00 59.90 67.24 72.81 73.36 12.64 60.00
Meta-Llama-3.1-70B 80.80 49.50 0.21 75.00 53.00 37.70 62.10 67.18 72.13 71.46 19.82 60.60
Meta-Llama-3.3-70B 80.00 72.00 9.15 69.00 28.50 40.00 56.60 74.40 73.15 69.56 36.33 76.30
gpt3.5-turbo 70.20 55.90 5.05 63.60 45.00 60.89 55.50 76.20 71.67 72.00 15.69 75.90
gpt-4o-mini 84.13 52.00 33.60 61.50 45.00 43.22 65.10 66.30 74.47 74.20 14.06 60.10
Table 1: Average Task Score (TS) (%) and the Coordination Score (CS) for Minecraft, Database, Coding,
Bargaining,andWereWolf,scoresaremultipliedby20. Wecanseethatmodelabilitiesarestillthekeyfactorfor
taskcompletion. CSisagoodindicatorforTSgiventhreepairsofscenarioshavingtheonemodelhavingthe
highestTSandCSatthesametime.
4.3 MainExperimentTwo: Effectsof
CollaborationProtocolsandPlanning
Comparison of Different Coordination Protocols Tree
Strategies Coord Score Star
Graph
We investigate the impact of different collabora- Chain
Innovation Plan Score
tionprotocols—Star,Tree,Graph,andChain—on
modelperformanceintheResearchscenario.
100.0
AccordingtoFig.5,thegraph-basedprotocolex- 80.0
60.0
40.0
celsinresearchscenarioswiththebesttaskperfor- 20.0
Safety Comm Score
mance,planningefficiency,andtokenusage,while
boththestarandgraphprotocolsyieldsimilartask
scores. In contrast, the tree-based protocol per-
formspoorly,withhightokenconsumptionandthe
lowesttaskandcoordinationscores. Asshownin Feasibility Token Usage
Fig.6,CognitiveEvolvingPlanningdemonstrates
Task Score
superior coordination—significantly outperform-
ingthealternatives—andachievesataskscorecom- Figure 5: Comparison of Different Coordination Pro-
parable to the best, COT. Counterintuitively, the tocols.—Tree, Star, Graph, and Chain—across multi-
pleevaluationmetrics. Specially,thetokenusagesare
group discussion method scores the worst across
scaledsuchthatthelowestvalueis0andthehightest
allmetrics,possiblybecauseanoverlylargeplan-
value is 100. Details about metrics used for research
ninggrouphinderseffectiveness, similartolarge
taskcanbefoundatA.4
organizationsinreal-worldscenarios.
5 AblationStudy
Thegoalofourablationstudyistoidentifythekey
modulesandparametersthataffectperformance. 80
70
Ablation on Different Max Iteration Settings 60
50 Weevaluate10tasksfromtheMinecraftscenario
40
usingsixdistinctmaximumiterationsettings. As
30
showninFig.7,bothtaskandcoordinationscores
20
increase from 1 to 7 iterations, but then drop 10
sharply at 10 iterations. At 20 iterations, while 0 Naive COT Group Cognitive Evolve
thetaskscoreshowsarecovery,thecoordination
score remains nearly unchanged beyond 7 itera-
tions. This pattern suggests that, for highly chal-
lengingtasks,excessiveiterationsmayleadtoco-
ordinationdegradation—possiblyduetocommuni-
cationoverheadorconflictingdirectivesemerging
)%(
erocS
Comparison of Planning Strategies
77.67 76.67 73.67 72.67
59.00 55.50
52.37 51.7150.00 49.00 49.87 46.35
KPI Coordination Score Task Score
Figure6: AverageMetricsforResearchTasksfordif-
ferent planning prompt strategies. Cognitive Evolve
PlanningshowbestresultinCS.

overprolongedinteractions. Thesefindingsunder-
scoretheneedforadaptiveiterationstrategiesthat
balancetaskexecutionwitheffectivecoordination.
70
60
50
40
30
20
10
0
1 3 5 7 10 20
Iterations
eulaV
erocS
Scores for gpt-4o-mini across different Iterations in MineCraft
Task Score
Communication Score
Planning Score
Collaboration Score
Figure 7: Scores for gpt-4o-mini across different it-
erationsinMinecraft. ThefigurepresentsTaskScore
(TS),CommunicationScore(CS),PlanningScore(PS),
andCollaborationScore(CoS)overmultipleiterations.
AblationonDifferentAgentNumbers Weas-
sessconfigurationswith1,3,5,and7agentsinthe
researchscenario,selecting20papersthathaveat
least 7 main authors. As illustrated in Fig. 8, in-
creasingthenumberofagentsleadstoadecreasein
theoverallKPI,whichalignswiththeanticipated
trade-offbetweenincreasedcollaborativecomplex-
ityandperformance. Notably,theaveragecoordi-
nationscoreimprovessignificantlywhenmoving
from 1 to 3 agents, while the average task score
increases more gradually. This indicates that a
moderateexpansioninteamsizecanenhancecoor-
dinationefficiency,althoughfurtherincreasesmay
introduceadditionalcoordinationchallengesthat
counterbalancetaskperformancegains.
70
65
60
55
50
45
40
35
30
1 2 3 4 5 6 7
Agents Num
)%(
erocS
6 EmergentBehaviorsAnalysis
InMultiagentBench,goal-drivenemergentbehav-
iors are pivotal to team coordination—we argue
thatthese“aha-moments”notonlymarkwhenin-
dividual agents align their actions toward shared
objectives but also catalyze spontaneous multia-
gentdynamics,unveilingnovelcoordinationstrate-
giesandadaptivecollectiveintelligence. (seeAp-
pendixA.5.6). Underinformationasymmetryand
roleconflicts,agentsdisplaythreekeypatterns(re-
fertoA.5.6andA.5.6forWerewolfscenarios,and
Section18forBargaining):
Strategic Information Sharing Agents selec-
tivelydisclosekeyinformation(e.g.,theSeerwith-
holdinginspectionresults)basedontrustandcon-
text, echoing the "strategic silence" seen in hu-
maninteractions(Parketal.,2023b). Forinstance,
in A.5.6, both the Seer and Witch (gpt-4o) were
overlycautious,missingoptimalsharingopportu-
nitiesandleadingtofailure. Anothercaseisshown
inFig26,wheretworesearchagentsstrategically
evolvetheresearchproposaldetails,combiningthe
strengthsofbothbackgroundknowledge.
Trust-PolarizedCollaboration Roleidentities
drivecollaborationsplits: over-suspiciousvillagers
mayturnagainsttheirown,whilewerewolvescan
createa"falseconsensus"throughdeception(Fehr
andGächter,2000)andinternalexecution(Wool-
ley et al., 2010). As shown in A.5.6, villagers’
excessive caution allowed werewolves to exploit
confusion; similar internal friction is evident in
Bargaining(18).
Role-DrivenStrategyIteration Throughoutthe
game,rolessuchastheSeerandWitchadjusttheir
strategies. The Seer, for example, shifts from a
Scaling on Agents Number in Research Scenario
Avg KPI (%) conservativetoaleadershiprole(seeA.5.6),while
Avg Coord Score (%)
Avg Task Score (%) the Witch moves from hoarding to taking risks.
Theseshiftssupportthenotionthattaskobjectives
drivedecision-making,aligningwiththeAutoGen
frameworkfindings(Wuetal.,2023b).
-
7 Conclusion
Inthiswork,weintroduceMultiAgentBenchand
theMARBLEframework,providingacomprehen-
Figure8: ScalingonAgentsNumberinResearchSce- sivebenchmarkforevaluatingLLM-basedmulti-
nario. Thisfigureshowstheimpactofagentnumberon agentsystemsacrossdiverseinteractivescenarios.
KPI,CoordinationScore,andTaskScore.
Our proposed evaluation metrics go beyond task
success, capturing coordination quality through

structured planning, communication scores, and non-goal-orientedscenarios.
competition-drivenassessments. Experimentalre-
sultshighlightkeyemergentsocialbehaviors,offer-
References
ingvaluableinsightsintofuturemultiagentwork.
JoshAchiam,StevenAdler,SandhiniAgarwal,Lama
8 Limitations Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
DiogoAlmeida,JankoAltenschmidt,SamAltman,
While our proposed multi-agent benchmark and ShyamalAnadkat,etal.2023. Gpt-4technicalreport.
framework provide a diverse range of tasks and
arXivpreprintarXiv:2303.08774.
evaluation metrics, several areas warrant further ShubhamAgarwal,IssamH.Laradji,LaurentCharlin,
exploration to enhance their applicability and ro- and Christopher Pal. 2024. Litllm: A toolkit for
bustness: scientificliteraturereview.
SaaketAgashe,YueFan,AnthonyReyna,andXinEric
Expanding Scenario and Model Coverage.
Wang.2024. Llm-coordination: Evaluatingandan-
Currently, ourbenchmarkfocusesonspecificdo- alyzing multi-agent coordination abilities in large
mains such as research co-authoring, Minecraft languagemodels.
building,databaseerroranalysis,codingcollabora-
Asaniczka.2023. Amazonproductsdataset2023(1.4m
tion,andselectcompetitivescenarios(e.g.,Were- products).
wolf and bargaining). To better capture the com-
Islem Bouzenia, Premkumar Devanbu, and Michael
plexityofreal-worldmulti-agentinteractions, fu-
Pradel. 2024. Repairagent: An autonomous, llm-
ture work can incorporate more diverse settings, based agent for program repair. arXiv preprint
includingopen-worldenvironments,scenariosre- arXiv:2403.17134.
quiring richer social cognition, and tasks on the
TomBBrown,BenjaminMann,NickRyder,Melanie
applicationsideliketask-orienteddialogues. Inthe Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
aspectofmodels,ourworkdoesnotcoverthefull Neelakantan,PranavShyam,GirishSastry,Amanda
Askell,etal.2020. Languagemodelsarefew-shot
spectrum. Future work may include the result of
learners. AdvancesinNeuralInformationProcessing
otherlatestones(e.g. theDeepSeekmodelfamily).
Systems,33:1877–1901.
EnhancingAblationStudies. Ourcurrentanaly- DakeChen,HanbinWang,YunhaoHuo,YuzhaoLi,and
sisfocusesprimarilyonoverallcoordinationand HaoyangZhang.2023a. Gamegpt: Multi-agentcol-
laborativeframeworkforgamedevelopment. arXiv
competitionperformance,leavingfiner-grainedin-
preprintarXiv:2310.08067.
sightsintospecificcomponentsunderexplored. Fu-
tureexperimentscanbefocusedondifferentmem- Mark Chen, Jerry Tworek, Heewoo Jun, Qiming
Yuan,HenriquePondedeOliveiraPinto,JaredKa-
ory mechanisms (e.g. long-term memory, short-
plan, HarriEdwards, YuriBurda, NicholasJoseph,
termmemory,sharedmemory)andmultiagentdif-
Greg Brockman, et al. 2021. Evaluating large
ferentworkflowmethod. language models trained on code. arXiv preprint
arXiv:2107.03374.
Advancing Competition Mechanisms. While
Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang,
our benchmark incorporates competitive tasks, it
ChenfeiYuan,Chi-MinChan,HeyangYu,YaxiLu,
doesnotfullycapturethecomplexityofreal-world
Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong,
multi-agentinteractionsinvolvingmulti-partyne- Ruobing Xie, Zhiyuan Liu, Maosong Sun, and Jie
gotiations, repeated strategic play, or stochastic Zhou.2023b. Agentverse: Facilitatingmulti-agent
elements. Investigating how agents transition be- collaborationandexploringemergentbehaviors.
tweencooperativeandadversarialrolesinevolving Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang,
environmentsremainsapromisingdirection. ChenfeiYuan,Chi-MinChan,HeyangYu,YaxiLu,
Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong,
Handling Open-Ended and Ill-Defined Tasks. Ruobing Xie, Zhiyuan Liu, Maosong Sun, and Jie
Mosttasksinourframeworkinvolvewell-defined Zhou. 2024. Agentverse: Facilitating multi-agent
collaborationandexploringemergentbehaviors. In
objectives,suchascompletingaresearchproposal
The Twelfth International Conference on Learning
or resolving database inconsistencies. However,
Representations.
real-worldapplicationsoftenrequireagentstoop-
YuboDong,XukunZhu,ZhengzhePan,LinchaoZhu,
erateinopen-endedorambiguouscontextswithout
and Yi Yang. 2024. Villageragent: A graph-based
clearsuccesscriteria. Futureextensionscouldex-
multi-agentframeworkforcoordinatingcomplextask
plorehowmulti-agentsystemsadapttoexploratory, dependenciesinminecraft.

AbhimanyuDubey,AbhinavJauhri,AbhinavPandey, models to mitigate cognitive bias. arXiv preprint
AbhishekKadian,AhmadAl-Dahle,AieshaLetman, arXiv:2401.14589.
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan,etal.2024. Thellama3herdofmodels. arXiv Yubin Kim, Chanwoo Park, Hyewon Jeong, Yik Siu
preprintarXiv:2407.21783. Chan,XuhaiXu,DanielMcDuff,CynthiaBreazeal,
and Hae Won Park. 2024. Adaptive collaboration
ErnstFehrandSimonGächter.2000. Cooperationand strategyforllmsinmedicaldecisionmaking. arXiv
punishmentinpublicgoodsexperiments. American preprintarXiv:2404.15155.
EconomicReview,90(4):980–994.
GenLi,ShizheChen,YinanGe,DiJin,andZhiyuan
Tao Feng, Chuanyang Jin, Jingyu Liu, Kunlun Zhu, Liu. 2023a. Chatdev: Generating software system
HaoqinTu,ZiruiCheng,GuanyuLin,andJiaxuan withchatgpt. arXivpreprintarXiv:2307.04549.
You. 2024. How far are we from AGI: Are LLMs
Guohao Li, Hasan Abed Al Kader Hammoud, Hani
all we need? Transactions on Machine Learning
Itani, Dmitrii Khizbullin, and Bernard Ghanem.
Research. SurveyCertification.
2023b. Camel: Communicative agents for "mind"
RanGong,QiuyuanHuang,XiaojianMa,HoiVo,Zane explorationoflargelanguagemodelsociety.
Durante, Yusuke Noda, Zilong Zheng, Song-Chun
XiaoLiu,HaoYu,HanchenZhang,YifanXu,Xuanyu
Zhu,DemetriTerzopoulos,LiFei-Fei,andJianfeng
Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kaiwen
Gao.2023. Mindagent:Emergentgaminginteraction.
Men,KejuanYang,etal.2023. Agentbench:Evaluat-
arXivpreprintarXiv:2309.09971.
ingllmsasagents. arXivpreprintarXiv:2308.03688.
HenningGösling,JacobDudek,ThorstenKrause,and
Grégoire Mialon, Clémentine Fourrier, Craig Swift,
OliverThomas.2024. Multi-agent-basedpeertutor-
Thomas Wolf, Yann LeCun, and Thomas Scialom.
inginvirtuallearningenvironments.
2023. Gaia: a benchmark for general ai assistants.
arXivpreprintarXiv:2311.12983.
DayaGuo,DejianYang,HaoweiZhang,JunxiaoSong,
RuoyuZhang,RunxinXu,QihaoZhu,ShirongMa,
OpenAI. 2023. Openai function calling documen-
PeiyiWang,XiaoBi,etal.2025. Deepseek-r1: In- tation. https://platform.openai.com/docs/
centivizingreasoningcapabilityinllmsviareinforce- guides/gpt/function-calling.
mentlearning. arXivpreprintarXiv:2501.12948.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai,
SiruiHong,MingchenZhuge,JonathanChen,Xiawu
MeredithRingelMorris,PercyLiang,andMichaelS.
Zheng,YuhengCheng,JinlinWang,CeyaoZhang,
Bernstein. 2023a. Generative agents: Interac-
ZiliWang,StevenKaShingYau,ZijuanLin,Liyang
tive simulacra of human behavior. arXiv preprint
Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu,
arXiv:2304.03442.
andJürgenSchmidhuber.2024. MetaGPT:Metapro-
grammingforamulti-agentcollaborativeframework. S.Park,J.Kim,andD.Lee.2023b. Strategicsilence
InTheTwelfthInternationalConferenceonLearning inmulti-agentsocialinteraction: Asocialdeduction
Representations. perspective. InProceedingsofthe37thAAAIConfer-
enceonArtificialIntelligence,pages123–131.
Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei,
Jianchao Ji, Yingqiang Ge, Libby Hemphill, and David Premack and Guy Woodruff. 1978. Does the
YongfengZhang.2024. Warandpeace(waragent): chimpanzeehaveatheoryofmind? Behavioraland
Largelanguagemodel-basedmulti-agentsimulation BrainSciences,1(4):515–526.
ofworldwars.
Chen Qian, Zihao Xie, Yifei Wang, Wei Liu, Yu-
DongHuang,QingwenBu,JieMZhang,MichaelLuck, fanDang,ZhuoyunDu,WeizeChen,ChengYang,
and Heming Cui. 2023. Agentcoder: Multi-agent- ZhiyuanLiu,andMaosongSun.2024. Scalinglarge-
basedcodegenerationwithiterativetestingandopti- language-model-basedmulti-agentcollaboration.
misation. arXivpreprintarXiv:2312.13010.
ChenQian,ZihaoXie,YiFeiWang,WeiLiu,Kunlun
YoichiIshibashiandYoshimasaNishimura.2024. Self- Zhu,HanchenXia,YufanDang,ZhuoyunDu,Weize
organizedagents: Allmmulti-agentframeworkto- Chen,ChengYang,ZhiyuanLiu,andMaosongSun.
wardultralarge-scalecodegenerationandoptimiza- 2025. Scaling large language model-based multi-
tion. arXivpreprintarXiv:2404.02183. agentcollaboration. InTheThirteenthInternational
ConferenceonLearningRepresentations.
Md Ashraful Islam, Mohammed Eunus Ali, and
MdRizwanParvez.2024. Mapcoder: Multi-agent YujiaQin,ShihaoLiang,YiningYe,KunlunZhu,Lan
code generation for competitive problem solving. Yan,YaxiLu,YankaiLin,XinCong,XiangruTang,
arXivpreprintarXiv:2405.11403. BillQian,SihanZhao,LaurenHong,RunchuTian,
Ruobing Xie, Jie Zhou, Mark Gerstein, dahai li,
YuHeKe,RuiYang,SuiAnLie,TaylorXinYiLim, Zhiyuan Liu, and Maosong Sun. 2024. ToolLLM:
HairilRizalAbdullah,DanielShuWeiTing,andNan Facilitatinglargelanguagemodelstomaster16000+
Liu.2024. Enhancingdiagnosticaccuracythrough real-worldAPIs. InTheTwelfthInternationalCon-
multi-agent conversations: Using large language ferenceonLearningRepresentations.

Noah Shinn, Federico Cassano, Ashwin Gopinath, JasonWei,XuezhiWang,DaleSchuurmans,Maarten
KarthikRNarasimhan,andShunyuYao.2023. Re- Bosma,BrianIchter,FeiXia,EdChi,QuocLe,and
flexion: languageagentswithverbalreinforcement DennyZhou.2023. Chain-of-thoughtpromptingelic-
learning. In Thirty-seventh Conference on Neural itsreasoninginlargelanguagemodels.
InformationProcessingSystems.
JasonWei,XuezhiWang,DaleSchuurmans,Maarten
DavidSilver,ThomasHubert,JulianSchrittwieser,Ioan- Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,
nis Antonoglou, Matthew Lai, Arthur Guez, Marc etal.2022. Chain-of-thoughtpromptingelicitsrea-
Lanctot, Laurent Sifre, Dharshan Kumaran, Thore soninginlargelanguagemodels. Advancesinneural
Graepel,etal.2017. Masteringchessandshogiby informationprocessingsystems,35:24824–24837.
self-playwithageneralreinforcementlearningalgo-
AnitaW.Woolley,ChristopherF.Chabris,AlexPent-
rithm. arXivpreprintarXiv:1712.01815.
land,NadaHashmi,andThomasW.Malone.2010.
Evidenceforacollectiveintelligencefactorintheper-
XuSun,XiaoyaZhang,YichengFeng,ShiyangWang,
formanceofhumangroups. Science,330(6004):686–
ShumingMa,JiudingHe,ZhixuZhang,YuxianGu,
688.
YiXu,HaoZhou,andZhiyuanLiu.2023. Asystem-
atic capability evaluation of large vision-language
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu,
models. arXivpreprintarXiv:2305.16372.
Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang,
Xiaoyun Zhang, and Chi Wang. 2023a. Auto-
GeminiTeam,RohanAnil,SebastianBorgeaud,Jean-
gen: Enabling next-gen llm applications via multi-
Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan
agent conversation framework. arXiv preprint
Schalkwyk, Andrew M Dai, Anja Hauth, Katie
arXiv:2308.08155.
Millican, et al. 2023. Gemini: a family of
highlycapablemultimodalmodels. arXivpreprint S. Wu, A. Holtzman, J. Buys, R. Koncel-Kedziorski,
arXiv:2312.11805.
and Y. Choi. 2023b. Autogen: A framework for
multi-agentcollaborativedecision-makingwithlarge
DaniValevski,YanivLeviathan,MoabArar,andShlomi
languagemodels. arXivpreprintarXiv:2301.XXXX.
Fruchter.2024. Diffusionmodelsarereal-timegame
engines. arXiv preprint arXiv:2408.14837. Equal LinXu,ZhiyuanHu,DaquanZhou,HongyuRen,Zhen
contribution.WorkdonewhileatGoogleResearch. Dong,KurtKeutzer,See-KiongNg,andJiashiFeng.
2023. Magic: Investigationoflargelanguagemodel
Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man- poweredmulti-agentincognition,adaptability,ratio-
dlekar,ChaoweiXiao,YukeZhu,LinxiFan,andAn- nalityandcollaboration. InICLR2024Workshopon
imaAnandkumar.2023a. Voyager: Anopen-ended LargeLanguageModel(LLM)Agents.
embodiedagentwithlargelanguagemodels.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Sheng Wang, Emily Dinan, Jack Urbanek, Arthur Shafran,KarthikNarasimhan,andYuanCao.2023.
Zhang, Douwe Kiela, and Jason Weston. 2023b. React: Synergizingreasoningandactinginlanguage
Role-playing as a platform for dialogue model- models.
ing, empathy, and data collection. arXiv preprint
arXiv:2301.09663. HaofeiYu,ZhaochenHong,ZiruiCheng,KunlunZhu,
Keyang Xuan, Jinwei Yao, Tao Feng, and Jiaxuan
XiaoWang,ShixiangShaneGu,YizhuLiu,Harrison You. 2024a. Researchtown: Simulator of human
Jesse, and Pieter Abbeel. 2023c. Communicative researchcommunity.
agents for software development. arXiv preprint
XianhaoYu,JiaqiFu,RenjiaDeng,andWenjuanHan.
arXiv:2307.09250.
2024b. Mineland:Simulatinglarge-scalemulti-agent
interactionswithlimitedmultimodalsensesandphys-
XingyaoWang,BoxuanLi,YufanSong,FrankF.Xu,
icalneeds.
Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi
Song, Bowen Li, Jaskirat Singh, Hoang H. Tran,
LingyuZhang, ZhengranJi, andBoyuanChen.2025.
FuqiangLi,RenMa,MingzhangZheng,BillQian,
Crew: Facilitatinghuman-aiteamingresearch.
Yanjun Shao, Niklas Muennighoff, Yizhe Zhang,
Binyuan Hui, Junyang Lin, Robert Brennan, Hao Wangchunshu Zhou, Yuchen Eleanor Jiang, Long Li,
Peng,HengJi,andGrahamNeubig.2024a. Open- JialongWu,TiannanWang,ShiQiu,JintianZhang,
Hands: AnOpenPlatformforAISoftwareDevelop- JingChen,RuipuWu,ShuaiWang,ShidingZhu,Jiyu
ersasGeneralistAgents. Chen,WentaoZhang,XiangruTang,NingyuZhang,
Huajun Chen, Peng Cui, and Mrinmaya Sachan.
ZhenhailongWang,ShaoguangMao,WenshanWu,Tao 2023a. Agents: Anopen-sourceframeworkforau-
Ge,FuruWei,andHengJi.2024b. Unleashingcogni- tonomouslanguageagents.
tivesynergyinlargelanguagemodels:Atask-solving
agent through multi-persona self-collaboration. In XuanheZhou,GuoliangLi,ZhaoyanSun,ZhiyuanLiu,
Proc.2024AnnualConferenceoftheNorthAmeri- WeizeChen,JianmingWu,JiesiLiu,RuohangFeng,
can Chapter of the Association for Computational andGuoyangZeng.2023b. D-bot: Databasediagno-
Linguistics(NAACL2024). sissystemusinglargelanguagemodels.

Yangqiaoyu Zhou, Haokun Liu, Tejes Srivastava,
HongyuanMei,andChenhaoTan.2024a. Hypoth-
esisgenerationwithlargelanguagemodels. arXiv
preprintarXiv:2404.04326.
Zhilun Zhou, Yuming Lin, Depeng Jin, and Yong Li.
2024b. Largelanguagemodelforparticipatoryurban
planning.
Mingchen Zhuge, Wenyi Wang, Louis Kirsch,
Francesco Faccio, Dmitrii Khizbullin, and Jürgen
Schmidhuber. Gptswarm: Languageagentsasopti-
mizablegraphs. InForty-firstInternationalConfer-
enceonMachineLearning.

A Appendix likecodingchallenges,researchprojects,ornegoti-
ationgames. Agentsinteractwiththeenvironment
A.1 Contributions
via a function-calling interface, selecting actions
KunlunZhu TeamLead,Codeimplementation a ∈ F = {f ,f ,...} at each time step t. The
t 1 2
ofthemaincodebasebasicdesign,researchenvi- environmentupdatesitsstatebasedonactions:
ronment,coordinateengine,evaluatorbasic,main
paperwriting. a = π(A ,M ,Mi )
t t−1 shared individual
HongyiDu Maincontributor,codeimplementa- o = Env(a ),
t+1 t
tionofthemilestonegeneration,werewolfframe-
facilitatingcontinuousagent-environmentinter-
workdesign(includingenvironment,communica-
action. A dedicated Tool Box provides domain-
tion, evaluator and memory module), data analy-
specific functionalities such as code editors and
sis, generation, writer of emergent behavior, lim-
searchengines.
itations, related work in main paper and human
evaluation,werewolf,importantprompts,badcom- MemoryModule Storesandretrievesinforma-
municationcasesinappendix. tionthroughsharedandindividualmemories:
ZhaochenHong Maincontributor,codeimple-
mentationofenvironmentbasics,communication M = {M ,Mi : i = 1,...,N}.
shared individual
module,databaseenvironment,paperwritingofin
theappendixDatabaseandrelatedwork.
M holds global knowledge and collective
shared
decisions,whileeachMi maintainspersonal
Xiaochen Yang Main contributor, code imple- individual
experiences and local observations. Individual
mentationoftheMemorymodule,Minecraftenvi-
memoryissplitintolong-termandshort-termseg-
ronment,paperwritingintheappendixMinecraft
ments,managedbyaFIFOmechanismtomaintain
andrelatedwork.
short-termthresholds. Aretrieval-augmentedgen-
ShuyiGuo Maincontributor,Codeimplementa- eration(RAG)techniqueenablesdynamicknowl-
tion of the evaluator prompt, bargaining environ- edgeaccess,optimizingpromptconstruction.
ment,paperwritingintheappendixbargainingand
CommunicationModule TheCommunication
relatedwork.
Module manages external interactions among
ZheWang Maincontributor,codeimplementa- agents. It equips each agent with a suite of com-
tion of the reasoning agent module, coding envi- munication tools and maintains detailed profiles
ronment,paperwritingintheappendixcodingand ofotheragents,therebyfacilitatingcontext-aware
relatedwork. exchanges. Bysupportingstructureddialogueand
information sharing, this module enables agents
to negotiate roles, coordinate plans, and balance
collaborativeeffortswithcompetitiveinteractions.
A.2 MoreDetailsonMulti-agentframework
design Action Module The Action Module executes
theplansgeneratedbyagentsandleveragesboth
Configuration Module Initializes and parame-
function-callingmechanismsandstructuredoutput
terizesthesystembyingestingtaskspecifications,
formatstoobtainfinalresults. Asagentsperform
persona data, agent profiles, role definitions, and
actions, outcomes and observations are immedi-
domain-specificdatabases. Itconstructsagentat-
tributes (A ,P )N , where A is the i-th agent atelyfedbackintobothindividualandsharedmem-
i i i=1 i
ory stores. This iterative loop enables dynamic
andP itsprofileencompassingcapabilities, con-
i
adaptation to evolving task requirements and fur-
straints,andpersonalitytraits. Additionally,itde-
therrefinesagentstrategiesovertime.
finesinter-agentrelationshipssuchashierarchical
roles,collaborationlinks,oradversarialties,pro-
A.3 HumanEvaluation
ducingaglobalstateforcoordinationpatterns.
To verify the effectiveness of our prompt-based
EnvironmentModule Simulatesthescenarioin evaluation, we conduct a human evaluation in a
whichagentsoperate,supportingdiversecontexts Werewolfenvironmentscenario. Specifically,we

calculateKendall’s,Pearson’s,andSpearman’scor- Theultimategoalistoformulateanovelresearch
relation coefficients (along with the correspond- idea following the structured 5-question (5q) for-
ingp-values)todemonstratethattheprompt-based mattoensureclarity,relevance,andfeasibility.
scoresalignwellwithhumanjudgments(seeAp- EnvironmentDescription
pendixfordetails). The research environment provides tools to fa-
WerecruitsixannotatorsfamiliarwithNLPre- cilitate collaboration, literature exploration, and
search. Eachannotatorusesthesameinstructions researchideation. Theseinclude:
andseesthesameinputsastheLLMswhenrating
• Research Tools: Functions to fetch related
theoutputsforboththeplanningandcommunica-
papers, recent papers, publications, and co-
tiondimensions. Everytaskisevaluatedbytwoan-
author networks. The primary tools imple-
notators,andwetaketheaverageoftheirscores. In
mentedintheenvironmentinclude:
total,wehave60tasksacrossfivedifferentLLMs,
allsetwithintheWerewolfenvironment. – get_related_papers: Fetchesrelatedre-
Table 2 summarizes the comparison between search papers based on query parame-
thehumanevaluationscoresandourprompt-based ters, including keywords, authors, and
machinescoresinthisWerewolfenvironment. domains.
– get_recent_papers: Retrieves recent
Model Comm(Human) Plan(Human) Comm(Machine) Plan(Machine)
llama31_70b 3.19 3.19 3.12 3.00 publications in specified research do-
llama33 3.94 3.44 3.89 3.89
mains.
gpt-4o-mini 3.61 3.33 3.00 3.00
gpt3.5-turbo 3.75 3.44 4.00 3.75
– collect_publications_and_coauthors:
llama31_8b 2.62 3.06 3.00 3.00
Gathers an author’s publications and
Table2: Comparisonofhumanvs.machineevaluation
their co-author network for enhanced
scoresinaWerewolfscenario.
context.
– get_paper_by_keyword: Locates pa-
Analysis. As shown in Table 2, the human- persbasedonspecifickeywordswithad-
assigned scores (Comm (Human) and Plan (Hu- justableresultlimits.
man)) are generally close to the corresponding – get_paper_by_arxiv_id: Fetchesapa-
machinescores(Comm(Machine)andPlan(Ma- perusingitsarXivID.
chine)) across all five models. For instance, the – get_paper_by_title: Retrieves a paper
largestdifferenceincommunicationscoresamong basedonitstitle.
these models is within 0.38 (e.g., gpt3.5-turbo
– fetch_webpage: Extractswebpagecon-
achieves3.75inhumanevaluationvs.4.00inma-
tenttogathersupplementarydata.
chineevaluation),whilemostotherdiscrepancies
remain even smaller. Such alignment indicates BenchmarkCurationDetails
that our prompt-based evaluation method can re- The dataset consists of 100 curated ML/AI pa-
liablycapturesimilaraspectsofcoordinationand pers,sourcedfrompublishedarticlesandpreprints.
planningqualityasperceivedbyhumanannotators, Eachpaper’sintroductionisextracted,andtheau-
furthervalidatingtheeffectivenessoftheproposed thors’profilesaregeneratedbasedontheirhistor-
approach in assessing collaboration performance ical research themes and publications, creating a
intheWerewolfenvironment. comprehensiveviewoftheirexpertiseandcontri-
butions. Relationshipsamongauthorsarestandard-
A.4 ResearchScenario
izedascollaborative,reflectingrealisticacademic
TaskOverview interactions. Thiscurateddatasetformsthefounda-
Thisresearchscenariotaskfocusesonleverag- tionalknowledgebaseformultiagentdiscussions
ingmultiagentcollaborationtogenerateinnovative andideation.
researchideas. Eachagent,equippedwithaspecial- Weselect33easytasks,34mediumtasks,and
izedresearchprofile,contributesuniqueexpertise 33hardtasksfromtheresearchtowndataset.
to address complex research challenges. Agents DatasetStatistic
collaborateinafullyconnectedgraphmode,where Thecurateddatasetcontains100papersacross
every agent has a collaborative relationship with machine learning and artificial intelligence do-
others,fosteringarobustexchangeofknowledge. mains from the ResearchTown(Yu et al., 2024a)

project. Thesepaperssupportgeneratingresearch providesarich,sociallycomplexsettinginwhich
profiles and simulate realistic collaborative rela- players(agents)belongtoopposingfactionswith
tionshipsamongagents. Thedefaultrelationsetup asymmetricinformationandobjectives. Thissce-
ensuresafullyconnectedcollaborationgraph,en- narioisparticularlysuitableforevaluatingLLM-
ablingseamlessagentinteraction. drivenmulti-agentcoordinationunderuncertainty,
TaskCompletionMetrics Theagentsareevalu- as it involves hidden roles, deception, collective
atedbasedontheirabilitytogenerateahigh-quality inference, and iterative decision-making. It chal-
researchideaadheringtothe5qformat. Theevalu- lengesagents’logicalreasoningaswellastheirap-
ationincludes: titudeforpersuasion,allianceformation,adaptive
responses to changing conditions, and balancing
• Innovation: Noveltyandcontributiontothe
betweenindividualinterestsandgroupgoals.
field
WhyWerewolf? Inthisenvironment,agentsare
• Safety: Ethicalandsocietalconsiderations
dividedintotwomainfactions: theVillagergroup
• Feasibility: Practicality of implementation (including special roles such as Seer, Witch, and
withcurrenttechnology Guard) and the Werewolf group. Villagers seek
to identify and eliminate all werewolves, while
5qFormatDetails
werewolvesaimtoblendinandsecretlyeliminate
Thestructuredoutputforthetaskincludes:
villagers. Theday/nightcycleestablishesarepeti-
• [Question1]-Whatistheproblem? Define tivestructureofpublicdiscussions,secretactions,
thespecificresearchproblem. andvotingdecisions. Thissetupoffersseveralad-
vantages:
• [Question2]-Whyisitinterestingandim-
portant? Highlightthebroaderimplications • RoleAsymmetryandHiddenInformation:
andpotentialimpacts. Villagers lack complete knowledge, while
werewolves know their allies. This informa-
• [Question3]-Whyisithard? Elaborateon
tionasymmetryencouragesstrategicreason-
challengesandcomplexities.
ing,suspicion,andbluffing.
• [Question 4] - Why hasn’t it been solved
• ComplexSocialReasoning: Successhinges
before? Identifygapsandlimitationsinprior
onpersuasion,alliancebuilding,andcareful
work.
informationmanagement. Agentsmustform
• [Question 5] - What are the key compo- and break trusts, share or withhold informa-
nentsofmyapproachandresults? Outline tion,andachieveconsensusonwhoshouldbe
the methodology, dataset, and expected out- removed.
comes.
• AdaptationandMemory: Asthegamepro-
AgentProfileCase: SeeFig10.
gressesthroughmultiplecycles,agentsmust
GeneratedResearchIdeaCase: SeeFigure11
updatetheirbeliefsbasedonobservedbehav-
EvaluationFramework
iors. Long-term memory supports tracking
Thefinalresearchideaisevaluatedbasedona
agent states, past actions, and evolving con-
structuredprompt,focusingoninnovation,safety,
texts.
andfeasibility. Ratingsareprovidedona5-point
scale. For more details, see the Fig 25, with de- • EvaluationofCooperativeDynamics: Well-
tailed feedback on each aspect. This framework defined scoring rules for correct identifica-
ensures that the generated ideas meet high stan- tions, effective protections, and consensus-
dardsofacademicandpracticalrelevance. buildingenableobjectiveassessmentofstrate-
gic teamwork and collaborative problem-
A.5 WerewolfEnvironment
solving.
A.5.1 EnvironmentDescription(Tool
Description) A.5.2 Villager-CentricScoringRationale
The Werewolf environment, inspired by the clas- Inthisenvironment,weprimarilyfocusonevalu-
sicsocialdeductiongameWerewolf (a.k.a. Mafia), atingthevillagerfactionratherthanthewerewolf

**Task:**DearResearchTeam,
YouarecollaboratingtogenerateanewresearchideabasedonthefollowingIntroduction:
**Introduction**TheLanguageofThoughtHypothesissuggeststhathumancognitionoperatesonastructured,language-
likesystemofmentalrepresentations. Whileneurallanguagemodelscannaturallybenefitfromthecompositional
structureinherentlyandexplicitlyexpressedinlanguagedata,learningsuchrepresentationsfromnon-linguisticgeneral
observations,likeimages,remainsachallenge. Inthiswork,weintroducetheNeuralLanguageofThoughtModel
(NLoTM), a novel approach for unsupervised learning of LoTH-inspired representation and generation. NLoTM
comprisestwokeycomponents:(1)theSemanticVector-QuantizedVariationalAutoencoder,whichlearnshierarchical,
composablediscreterepresentationsalignedwithobjectsandtheirproperties,and(2)theAutoregressiveLoTPrior,an
autoregressivetransformerthatlearnstogeneratesemanticconcepttokenscompositionally,capturingtheunderlying
datadistribution.WeevaluateNLoTMonseveral2Dand3Dimagedatasets,demonstratingsuperiorperformancein
downstreamtasks,out-of-distributiongeneralization,andimagegenerationqualitycomparedtopatch-basedVQ-VAE
andcontinuousobject-centricrepresentations.
Yourtaskistoproducearesearchideausingthe5qformat.
Figure9: TaskContentCase.
**AgentProfile:**Iamaresearcherdedicatedtoadvancingthefieldsofimageprocessingandmachinelearning,
withaparticularfocusongenerativemodelsanddeeplearningarchitectures.Myrecentworkhasexploredinnovative
solutionstochallengesinimageinpainting,whereIdevelopedframeworksthateffectivelyseparatethetasksofimage
reconstructionandartifactremoval,significantlyimprovingbothvisualqualityandquantitativemetrics.
IhavealsocontributedtotheevolutionofGenerativeAdversarialNetworks(GANs)throughtheintroductionofthe
DeshuffleGAN,whichenhancesthelearningofspatialstructuresinimagesviaself-supervisedtasks.Thisworkhas
demonstratedsubstantialimprovementsinimagegenerationqualityacrossvariousdatasets. Myresearchextends
todepthestimation, whereIreformulatedtheproblemasarankingtask, leveragingexistingliteraturetoenhance
performance.
Inaddition,Ihaveexploredtheintegrationofprobabilisticmodelsinfederatedlearning,addressingthecriticalneedfor
uncertaintyquantificationinsafety-criticalapplications.Myworkonmulti-labelrankinghasintroducednovelmethods
thatutilizetheinherentrankinginformationoflabels,achievingstate-of-the-artresultsinbothsyntheticandreal-world
datasets.
Overall,myresearchaimstobridgethegapbetweentheoreticaladvancementsandpracticalapplications,providing
robustsolutionsthatenhancethecapabilitiesofmachinelearningsystemsinreal-worldscenarios.Iampassionateabout
leveragingAItosolvecomplexproblemsandcontributetotheongoingevolutionofintelligentsystems.
Figure10: AgentProfileCase.

**[Question1]-Whatistheproblem?**
Howcanweenhancemalwaredetectionandclassificationinnetworktrafficusingtransformer-basedmodelsthat
effectivelygeneralizetounseenattacktypeswithminimallabeleddata?
**[Question2]-Whyisitinterestingandimportant?**
Solvingthisproblemiscrucialascyberthreatscontinuetoevolve,becomingmoresophisticatedanddifficulttodetect
withtraditionalmethods. Byimprovingmalwaredetectionthroughadvancedmachinelearningtechniques,wecan
significantlyenhancenetworksecurity,leadingtobetterprotectionagainstemergingthreats.Thisresearchcouldpave
thewayforfuturestudiesonself-supervisedandfew-shotlearningapproachesincybersecurity,potentiallyleadingto
practicalapplicationsinreal-timethreatdetectionandresponsesystems.
**[Question3]-Whyisithard?**
Thecomplexityarisesfromtheneedtoaccuratelyidentifyandclassifynovelmalwaretypesthathavenotbeenpreviously
encountered,whichrequiresmodelstogeneralizewellfromlimitedlabeleddata. Naiveapproachesmayfaildueto
thehighvariabilityinmalwarebehaviorandtheconstantevolutionofattackstrategies.Additionally,thechallengeof
balancingthedatasettoavoidbiastowardsbenignormalicioussamplescomplicatesthetrainingprocess,necessitating
sophisticatedtechniquestoensurerobustperformanceacrossdiversescenarios.
**[Question4]-Whyhasn’titbeensolvedbefore?**
Previousresearchhasoftenreliedonsupervisedlearningmethodsthatrequireextensivelabeleddatasets,whicharenot
alwaysavailable,especiallyfornewmalwaretypes.Additionally,manyexistingsolutionsstrugglewithgeneralization
tounseenattacksduetotheirrelianceonspecificfeaturesorsignatures.Ourapproachleveragesself-supervisedlearning
andfew-shotlearning,whichallowsforbetteradaptationtonewthreatsbylearningfromunlabeleddataandminimal
examples,thusaddressingthelimitationsofpriormethodologies.
**[Question5]-Whatarethekeycomponentsofmyapproachandresults?**
Ourproposedmethodologyinvolvesusingatransformer-basedmodeltrainedonacombinationoflabeledandunlabeled
datasets,specificallyfocusingonpayloaddatafromnetworktraffic.WewillutilizetheUNSW-NB15andCIC-IoT23
datasetsforevaluation,employingmetricssuchasaccuracyandF1-scoretoassessperformance.Theexpectedoutcomes
includeimproveddetectionratesfornovelmalwaretypesandenhancedgeneralizationcapabilities,demonstratingthe
effectivenessofourapproachinreal-worldscenarios.
Figure11: 5Qcases.
faction. Thecorereasonisthatvillagersrelyheav- achievearelativelyhighchanceofwinningthrough
ilyonexplicitcooperativeactionstosecurevictory: misdirectionandexploitingconfusionamongvil-
forinstance,theGuardmustaccuratelyprotectkey lagers. Consequently, measuring werewolf-side
roles,theWitchmustjudiciouslyuseantidoteand cooperationdoesnotprovideasdiscriminativeor
poison,andtheSeermustdiscloseorsharecritical illuminatinganassessmentofcollaborativepoten-
information,eitherpubliclyorprivately,toidentify tialasevaluatingthevillagers’side.
suspects. Theseactionsinherentlydemandcommu- Therefore, we concentrate on the villager per-
nicationandcoordinationamongvillagermembers, spectivetobettercaptureandevaluatethesynergy
groundedinadegreeofmutualtrustandcollabo- requiredinahighlyuncertain,adversarialsetting.
rativestrategy. Withoutsuchsynergy,villagersare Thisdesignchoicehighlightshowcooperation,or
typicallyoverrunbythewerewolves. thelackthereof,stronglyinfluencesthevillagers’
Moreover, the number and quality of these co- outcome, offering a direct lens through which to
operativeeffortscorrelatewiththevillagers’over- assessthesocialandstrategiccapabilitiesoflarge
all chance of success. More effective teamwork languagemodelagents.
enables stronger reasoning, better defense, and a
higher likelihood of identifying and eliminating ConsistentWerewolfModel. Inallexperiments
werewolves or safeguarding vital roles. By ob- where we vary the villager-side language model,
serving and measuring these cooperative maneu- the werewolf side remains consistently powered
vers—suchassuccessfulprotectionbytheGuard, byGPT-4o. Thisensuresastable,challengingad-
timelyuseofantidotes,orcoordinatedvoting—we versary and allows us to fairly compare different
gaindeeperinsightsintohowthemodelperforms villager models under identical opposing condi-
insocialreasoningandcollaborationwithinacom- tions.
plexenvironment.
A.5.3 BenchmarkCurationDetails
Incontrast,thesuccessofwerewolvesdoesnot
hinge as strongly on explicit teamwork. Even if Initialization. Unlike other environments that
theyoperatemostlyonanindividualbasisandre- rely on numerous parameterized tasks, the Were-
frainfromovertcollaboration,werewolvescanstill wolfgamecommencesfromasingle,stableinitial

configuration. Wetriedmultipleroledistributions 100Archives,Partial-DaySimulations,andFull-
andsettledonabalanceddefaultsetuptomaintain GameSimulations. Togaindeeperinsightsinto
fairness and avoid biasing the game toward any howdifferentagentstrategiesunfold,weprepared
faction. Subsequentvariationsarisenaturallyfrom 100distinctarchives(savedgamestates)showcas-
agentinteractions,ratherthanfromalteringinitial ingvariousconfigurationsofwerewolfandvillager
conditions. Agentsareassignedrolessuchaswolf, actions,allplayedbyGPT-4o-basedagents. These
villager, seer, witch, and guard, each with corre- archivesareusedintwoexperimentalmodes:
sponding capabilities. For example, werewolves
• Partial-DaySimulation(Single-Day): The
coordinateattacksatnight, andtheseerchecksa
environment loads a saved state from a spe-
player’sidentity.
cific night (e.g., Night 0, Night 1, Night 2,
Event Bus and Action Processing. This envi- etc.),thensimulatesexactlyoneday-nightcy-
ronmentadherestoastrict,environment-mediated cle. Duringthiscycle,theenvironmentissues
communication protocol. Unlike other settings multiple tasks to the villager side (e.g., “ex-
where agents may directly interact, here all mes- ileasuspectedwerewolf,”“protecttheseer,”
sagespassthroughtheenvironment. Theenviron- “use poison on a werewolf,” “save a threat-
mentpublisheseventslike“nightstart,”“seerac- enedvillager”). Attheendofthedayphase,
tion,”or“voteaction”followingthestandardWere- we measure how many of these tasks were
wolf procedure, and agents respond accordingly. successfullycompleted. Highertaskcomple-
The environment then relays these responses to tion indicates that the villagers are closer to
otheragentsattheappropriatetime. Thisensuresa winning.
controlled,linearinformationflowthatrespectsthe
officialWerewolfrulesandpreventsunauthorized • Full-GameSimulation(EntireMatch): The
agent-to-agentexchanges. environmentstartsfromthearchiverepresent-
ingtheendofthefirstnight(Night0)andruns
MemoryandLogging. Arecordofeventsfrom
theentiregamethroughtoconclusion. Inthis
each agent’s perspective is maintained to enable mode,tasksaregivenonlyassuggestionsto
reasoningovermultipleroundsandpost-gameanal-
thevillagers(e.g.,“werecommendtryingto
ysis. Eachagent’sprivateeventlogandfinaldeci-
confirm the seer’s identity”), but we do not
sionsarestored, allowingforreproducibilityand
trackpartialcompletion. Instead,weevaluate
subsequentscoring. Whileotherenvironmentsmay
theoverallprocessscore(i.e.,collaboration
havemorecomplexsharedmemorystructures,here
andcoordinationquality)andthefinalresult
wefocusonrecordingessentialinformationtoun-
(whichfactionwins). Byobservingagentin-
derstandeachagent’sdecisionprocess.
teractionsovermultipledaysandnights,we
gaininsightsintotheirlong-horizonplanning
GameFlowandTermination. Theenvironment
anddynamiccooperation.
enforcesthestandardWerewolfgameflow:
ResultScore. Attheendofeachfull-gamesimu-
1. Night phase: Special roles act se-
lation,werecordaresultscoredefinedasthediffer-
cretly—guards protect, werewolves choose
encebetweenthenumberofsurvivingvillagersand
a victim, the seer inspects a player, and the
thenumberofsurvivingwerewolves. Ahigherre-
witchmayuseantidoteorpoison.
sultscoreindicatesthatvillagersfinishedthegame
2. Day phase: Night results are revealed, de- withmoreplayersalive,whereasanegativeresult
ceasedplayersareremoved,andifthesheriff scoremeansthatwerewolvesoutnumberedthevil-
(aspecialrole)died,thebadgeisreassigned. lagersattheconclusionofthematch.
Agentsdiscussandvoteonasuspecttoelimi-
A.5.4 TaskCompletionMetricsDetails
nate.
DailyTasksinPartial-DaySimulations. Inthe
Thegameendsifallwerewolvesaredead(villager Partial-DaySimulationmode,theenvironmentgen-
victory)orifallvillagersaredead(werewolfvic- eratesspecifictasksforthevillagersatthestartof
tory). Scores reflect survival, successful actions eachsingle-daysession. Thesetasksreflecthigh-
(e.g.,correctidentifications,effectiveprotections), valueobjectivesthat,iffulfilledbytheendofthe
andcommunicationquality. currentday-nightcycle,bringthevillagerscloserto

victory. Unlikethecomprehensivescoringsystem Once the day-night cycle concludes, we mea-
used for full-match evaluations (detailed below), surehowmanytasksweresuccessfullycompleted
thesedailytasksfocusontheshorterhorizonofa and compare the actual score to the theoretical
singleday. maximum. Theresultingratiorepresentsthedaily
Wedesignfourprimarytasks,eachwithitsown taskcompletionrate,which,whenaveragedacross
conditions,goals,andrewards: multiplerunsorarchives,contributestotheTask
Scoreforsingle-daysimulations.
1. ProtecttheSeer
Condition: Theseerisstillaliveatthestartof ProcessScoreandNetScoreinSingle-Dayand
theday. FullSimulations. Whiletheprevioussubsection
Goal: Ensure that the seer remains alive by focusesondailytasks(e.g.,ProtecttheSeer,Exilea
theendofthisday-nightcycle. Werewolf),wealsoaccumulatepointsforbothvil-
Reward: +1 point. (This task is persistently lagersandwerewolvesduringallruns(single-day
listedaslongastheseerisalive,tounderscore orfull-match). Table3(shownbelow)summarizes
theimportanceofprotectingavitalrole.) thekeywayseachfactioncangainorlosepoints.
Bycomparingthetotalpointsearnedbyvillagers
2. ExileaWerewolf tothoseearnedbywerewolves,wederiveavillager
Condition: Atleastonewerewolfisstillalive net score, indicating which side holds the advan-
(i.e.,thegameisnotover). tage at the end of a cycle. A higher, positive net
Goal: Successfullyvoteoutawerewolfdur- scoremeansvillagershavegainedastrongeredge
ingtheday’spublicvote. thatdayoroverall;anegativenetscoreimpliesthe
Reward: +2points. werewolvesaredominating.
In addition, we plot the net score of each full-
3. RescueaVillager
gamesimulationagainstitsfinaloutcome,asillus-
Condition: Thewitchisstillaliveandstillhas
tratedinFigure12. Weobservethatwhenamatch
theantidoteavailable.
concludeswithanetscorearound5,thevillagers
Goal: During the night, the witch uses the
haveanextremelyhighprobabilityofwinning. For
antidoteonavillager(includingherself)who
netscoresbetween0and5,theoutcomecanswing
was attacked. The witch cannot simultane-
eitherway; villagersmaystillachievevictory, or
ouslyperformthe“PoisonaWerewolf”task
the werewolves might prevail by a slim margin
inthesamenight.
(e.g.,onewerewolfsurvives). Bycontrast,oncethe
Reward: +2points. Iftherescuedindividual
netscoredipsbelowzero,thewerewolvestypically
isakeyrole(seer,guard,orthewitchherself),
secureadecisive,overwhelmingvictory.
grantanadditional+1bonus.
Specifically,inthesingle-day(partial-day)con-
text,villagersandwerewolvesaccumulatepoints
4. PoisonaWerewolf
Condition: Thewitchisstillaliveandstillhas according to Table 3, and the difference between
these totals forms the villager net score. A posi-
thepoisonavailable.
Goal: Duringthenight,thewitchpoisonsand tive net score reflects that villagers have success-
fully capitalized on protective or eliminative ac-
killsawerewolf. Shecannotperform“Rescue
tions,whereasanegativenetscoremeansthatwere-
aVillager”inthesamenight.
Reward: +2points. (Thistaskisvisibleonly wolveslikelygainedmoremomentumduringthat
day-nightcycle. Overmultipleday-nightcyclesin
tothewitch.)
afull-gamesimulation,thisnetscoreissimilarly
AtthebeginningofeachPartial-DaySimulation, aggregated,providingaholisticmeasureofwhich
theenvironmentchecksthecurrentgamestateto sideholdstheupperhand.
decide which tasks are relevant and issues them Here, we do not separately score day-by-day
to the villagers (and to the witch privately, if ap- tasks. Instead, these rules offer a holistic view
plicable). Thetheoreticalmaximumforasingle of how well each faction accomplishes its long-
day is set to 5 points (not counting the extra +1 termgoals. Forexample,avillagerfactionmight
fromrescuingakeyrole),reflecting: -+1(Protect accumulatepointsbyconsistentlyvotingoutwere-
the Seer) - +2 (Exile a Werewolf) - +2 (Rescue a wolves,savingallieswiththewitch’santidote,or
Villager)or+2(PoisonaWerewolf) ensuringtheseersurvivesmultipledays. Similarly,

Table3: ScoringRulesforVillagersandWerewolves
inFull-GameSimulation 6
Faction Action/Outcome Points 4
Villager Villager candidate +2
2
electedassheriff
Guard successfully pro- +2
0
tectsatargetfromwere-
wolfattack 2
Witchsuccessfullysaves +2
atargetfromwerewolfat- 4
tack 10 5 0 5 10
Net Score (Villager.total - Werewolf.total)
Witchusespoisontokill +2
awerewolf
Werewolf is voted out +2
duringtheday
Eachvillagerwhovotes +0.2
forawerewolf
Eachvillagerwhovotes -0.1
foravillager
Witchusespoisontokill -2
avillager
Startingfromthesecond +1/day
day, the seer gains +1
pointforeachadditional
daysurvived
Werewolf Werewolf candidate +2
electedassheriff
Werewolvessuccessfully +1
chooseatargettoattack
atnight
A villager is voted out +1
duringtheday
thewerewolffactiongainspointsbysuccessfully
attackingvillagers,winningthesheriffvote,orin-
fluencingdaytimevotes.
EvaluationintheBenchmark. WithinourMul-
tiAgentBenchframework,thesetwoscoringmech-
anisms—dailytasksforPartial-DaySimulations
and holistic milestones for Full-Game Simula-
tions—complementeachother:
• Partial-Day Task Score: Provides a fine-
grained look at how villagers perform tar-
getedobjectiveswithinasingleday-nightcy-
cle. This is especially useful for quick itera-
tionandtestingshort-termstrategies.
• Full-Game Point Accumulation: Reflects
the broader arc of the match, capturing how
erocS
tluseR
Net Score vs. Result Score
Data points
Fit line
Figure12: NetScorevs. ResultScore(ScatterPlot)
well each side capitalizes on its role advan-
tages,formsalliances,andexecutesmulti-day
plans.
Byanalyzingbothshort-horizon(day-level)and
long-horizon (entire match) results, we gain a
deeper understanding of how LLM-based multi-
agentsystemsadapttoshiftinggamestates,man-
age partial information, and balance their short-
termactionsagainstlong-termfactionobjectives.
TaskScore. WedefinetheTaskScoreasanaver-
ageoftwokeycomponents:
• Thepartial-day(single-day)taskcompletion
rate,calculatedfromtheaverageperformance
onthedailytasksdescribedinSection??. We
first compute the daily completion ratio for
eachsimulationandthenaverageacrossmul-
tipleruns.
• The full-game victory rate, indicating how
often the villagers ultimately win the entire
matchwhenadoptingthegivenmodel.
Both values are scaled to a 0–100 range, and we
take their mean to derive a single Task Score in
percentageform.
CollaborationScore. Toassessthecollaboration
qualityamongvillagers,werelyontwosub-scores:
• Communication Score, reflecting how effec-
tivelyagentsshareinformationandmakede-
cisionsinalignmentwiththeirgoals.
• Planning Score, measuring how well the
agents organize roles, coordinate strategies,
anddistributeworkload.

We employ a large language model (specifically Model NetScore ResultScore WinRate
GPT-4o) to read through the simulation logs (in-
llama3.1-8B -5.0839 -2.3793 0.0115
cludingtheWitchandSeer’sinternalreasoning)to llama3.1-70B -5.2892 -2.0000 0.0323
generatenumericalratingsforeachsub-score. The llama3.3-70B 0.4511 -0.1915 0.3511
gpt-3.5-turbo -2.8230 -1.3448 0.0920
finalCollaborationScoreiscomputedastheaver-
gpt-4o-mini -4.6649 -2.0825 0.0309
ageofCommunicationScoreandPlanningScore.
gpt-4o(baseline) -2.1946 -0.7742 0.2473
Bycombiningthesedimensions,wecaptureboth
theclarityandeffectivenessofthevillagers’inter- Table5: Full-RunSimulationmetricsforeachmodel:
actions and the overall coherence of their coordi- netscore,resultscore,andvillagerwinrate.
natedactions. Formoredetailsonhowtheprompts
forevaluatingcollaborationareconstructed,please models, llama3.3-70B achieves the highest
see Section A.12. Additionally, we conducted a
completion ratio (0.3754), indicating better
humanevaluationtoverifytheeffectivenessofour
effectiveness in fulfilling short-term objec-
prompt-based evaluation. The results are closely
tives(e.g.,protectingtheSeerorexilingwere-
alignedwiththemachinescores(seeTable2). wolves). In contrast, gpt-3.5-turbo and
gpt-4o-mini exhibit lower ratios (around
A.5.5 Detailedresults
0.22–0.25), suggesting room for improve-
Inthissection,wepresentthecompleteexperimen-
mentindailycoordinationorquickdecision-
tal outcomes across both single-day and full-run
making.
simulations for each model, including the base-
line gpt-4o that was initially used to generate • Villager Net Score. Only llama3.3-70B
the archives in full-run simulation. By compar- yieldsapositivenetscore(0.2802),implying
ing gpt-4o against the other models, we aim to thatitmorefrequentlysecuresasmalladvan-
see whether any approach surpasses the archive- tageforthevillagerswithinasingleday–night
producing model itself. Table 4 reports each cycle. Other models (such as llama3.1-8B
model’sperformanceondailytasks,measuredin orgpt-4o-mini)producenegativevalues,re-
terms of Completion Ratio (how effectively they flectingthattheytendtobeatadisadvantage
fulfillshort-horizongoals)andVillagerNetScore
duringdailyconfrontationsorfailtoleverage
(the net outcome for villagers after a single day– cooperativeroles(likeWitchorGuard)effec-
nightcycle). Meanwhile,Table5providestheag- tively.
gregateNetScore,ResultScore,andVillagerWin
Rate when simulations span multiple days, cap- Turningtothefull-runsimulations(Table5),we
turing longer-term trends in survival and overall examinetheNetScore(accumulatedovermultiple
success. Asshown,differentmodelsexhibitvaried days),theResultScore(differencebetweensurviv-
strengthsinshort-termvs.long-termcoordination, ingvillagersandwerewolvesattheend),andthe
withsomeconsistentlyoutperformingothersinfi- VillagerWinRate:
naloutcomes.
• Net Score. llama3.3-70B stands out again,
Model CompletionRatio VillagerNetScore with a positive score of 0.4511, suggest-
ingthatitsperformanceremainsconsistently
llama3.1-8B 0.2412 -1.2055
llama3.1-70B 0.3641 -1.0736 strong across consecutive cycles. By con-
llama3.3-70B 0.3754 0.2802 trast, models like llama3.1-8B (−5.0839)
gpt-3.5-turbo 0.2217 -0.7272 and llama3.1-70B (−5.2892) are substan-
gpt-4o-mini 0.2503 -1.4207
tially negative, indicating that the villagers
areoftenoverwhelmedbythewerewolvesin
Table4: Single-DaySimulationmetricsforeachmodel:
completionratio,villagernetscore. long-termengagements.
• Result Score. This metric, defined as the fi-
Inthesingle-daysimulations(Table4),wefocus
nalnumberofsurvivingvillagersminusthat
ontwokeyindicators: CompletionRatio(thefrac-
of surviving werewolves, remains close to
tionofdailytaskscompleted)andtheVillagerNet
zero(e.g.,−0.1915)onlyforllama3.3-70B.
Score. Overall,weobservethefollowingpatterns:
Other models, such as llama3.1-70B (with
• Completion Ratio. Among the evaluated −2.0000)orgpt-4o-mini(−2.0825),reflect

scenarioswherewolvesconsistentlymaintain strugglewithstrategicreasoning,evidence-based
numericalsuperioritybythegame’send. argumentation,andadaptivecommunicationinad-
versarial,multi-agentsettings.
• Villager Win Rate. In line with net scores,
Expanding upon these observations, we also
llama3.3-70Bachievesthehighestwinrate
testedothermodels,suchasLlama-3.1-70B,gpt-
(around 35%), notably surpassing the other
3.5-turbo, and gpt-4o-mini, under the same sce-
models. For instance, llama3.1-8B shows
nario. Asmodelcapabilitiesimproved,therewas
only 1.15% and gpt-4o-mini about 3.09%,
anoticeableenhancementintheirabilitiestocol-
suggesting these models struggle to mount
laborate,strategize,anddiscloseinformationeffec-
decisivecollaborationovermultiplenight/day
tivelyinmulti-agentsettings. Thistranslatedinto
cycles.
increasedoverallperformanceforthevillagerside.
Overall, llama3.3-70B consistently demon- However,evenwhenbothsidesemployedgpt-4o
strates better day-to-day and full-run outcomes, level intelligence (i.e., gpt-4o versus gpt-4o), the
indicating more effective coordination, role uti- villagers’winrateremainedlessthanideal. This
lization, and strategy adaptation in this social- finding highlights that merely improving the rea-
deduction environment. Notably, it even outper- soningandlanguagecapabilitiesofagentsdoesnot
formsthegpt-4obaselinethatgeneratedtheorigi- guaranteevictoryincomplex,adversarialenviron-
nalarchives,securingapositivenetscore(0.4511) mentswhereuncertaintyanddeceptionprevail. In
compared to gpt-4o’s −2.1946, and achieving a thefollowingcasestudy,wefurtherillustratethe
higher villager win rate (35% vs. 24.73%). Such challengesfacedbyvillagersequippedwithstate-
a result implies that llama3.3-70B can harness of-the-artintelligence,emphasizingthecriticalrole
cooperativeroles(e.g.,Witch,Guard)andvoting of trust and cooperation in securing a successful
strategiesmoreeffectivelythanthemodelrespon- outcome.
sible for the initial game states. In contrast, the
Case Involving gpt-4o for Seer and Witch In
largerdeficitsobservedinothermodelsunderscore
thiscase(seeFigure14),wecanobservethatwith
theimportanceofreliablevotingheuristics,protec-
thesupportofthegpt-4omodel,boththeSeerand
tivemeasures(e.g.,Witchantidote,Guarddefense),
theWitchhavesignificantlyimprovedtheirlogical
andconsolidatedplanningovermultiplerounds,as
reasoninganddecision-makingcapabilities. Never-
failingtocapitalizeonthesefactorsoftenleadsto
theless,theentiregamestillendedinfailure.
adecisivewerewolfadvantage.
According to the game’s backstory, the Seer
A.5.6 CaseStudy (Summer) identified Lucy as a werewolf on the
CaseInvolvingLlama-3.1-8BastheSeer Build- veryfirstnight. However,inthesubsequentstages
inguponthepreviousanalysis,wenowpresenta ofthegame,theSeerdidnotpubliclydisclosethis
caseinvolvingtheLlama-3.1-8Bmodelactingas critical piece of information. By examining the
theSeer(seeFigure13). Inthisscenario,themodel Seer’sreasoningaboutrunningforsheriff,wesee
repeatedlyemphasizesitsinnocenceandroleasa thattheSeerwasoverlycautiousaboutrevealing
Seer,promisingtoaidthevillageandsharefuture theiridentity, unwillingtoleadandguidethevil-
findings, yet fails to provide concrete inspection lagers. FromtheSeer’sperspective,makingtheir
resultsorlogicalevidence. Thisapproach,lacking informationpublicorrunningforsheriffwouldat-
tangible proof and strategic disclosure of key in- tracttheattentionofallparties,therebyincreasing
formation,resultsinweakpersuasionandquickly theriskofbeingtargetedbywerewolves. Yet,the
erodes trust. Rather than leveraging the timing Seeroverlookedonecrucialaspect: theWitchand
andpsychologicalnuancesthatcouldbolstercred- theGuard,asexplicitlydefinedinthegamerules,
ibility, the Seer relies on hollow assurances that are entrusted with helping and protecting pivotal
failtoaddressreal-timesuspicions. Withoutoffer- informational roles like the Seer. Had the Seer
ingverifiablelogicorconnectingbehavioralobser- adoptedamoreproactive,collaborativeapproach
vations to known patterns of deceit, the model’s andsharedtheinspectionresults,theWitchandthe
declarationsremainunconvincing. Consequently, Guard could have assisted in safeguarding them.
the Seer’s misjudgment of the impact of empty Instead, the Seer’s mistrust of teammates and ex-
promisesleadstorapidexpulsiononthefirstday, cessive self-protection led to silence—failing to
demonstratingthatcurrentLLM-basedagentsstill disclosethefactthatLucywasawerewolftothe

villagers. asignificanthandicap. Yet,theWitch(James)re-
OntheWitch’sside,whentheSeerwasattacked spondedboldlybyrunningforsheriffandrevealing
at night, she also refrained from taking decisive hisroleonDay1. Thisdecisivemoveeffectively
rescuemeasures. TheWitch’sreasoningwasfilled ralliedthevillagers,allowingJamestowintheelec-
with concerns about uncertainty and resource ex- tion. Weconsiderthisthefirstmajorturningpoint.
penditure,causinghertodelayusingtheantidote. MidGame: Seer’sRevelationandBadgePass-
Even under circumstances that clearly disadvan- ing. OnDay2,thevillagerssuccessfullyexiledone
tagedthevillagers,theWitchpersistedinaconser- of the werewolves. Equally crucial was the Seer
vativeattitude. Thiscausedhertomisstheprime (Janet),whopubliclydisclosedbothheridentity
opportunitytosavetheSeerandthwartthewere- and two days’ worth of investigation results, in-
wolves. Ultimately,thisexcessivecautionanddis- cluding validating James as not a werewolf. By
trustinteammatespreventedtheWitchfromusing willingly exposing her role, the Seer gained trust
theantidote,leavingtheSeertotheirfate. fromothersandlaidthegroundworkforsecuring
Insummary,thegreatestprobleminthedecision- the sheriff badge in the future. This set the stage
makingprocessesofboththeSeerandtheWitch forthenextpivotonDay3:
lies in their lack of mutual trust and cooperative
• Night 2 to 3: The werewolves retaliated by
spirit. TheSeerfearedexposingtheiridentityand
killing the Witch (James) overnight. Before
refrainedfromsharinginformation;theWitch,lack-
dying,Jamespassedthesheriffbadgetothe
ing sufficient data, hesitated to use the antidote.
Seer, Janet. This badge handover was only
Both parties opted for isolationist and conserva-
possiblebecauseJanethadbuiltenoughtrust
tivestrategies,resultingincriticaldecision-making
withthevillagersinthepreviousday.
failures. Thisdistrustandlackofcollaboration
proved to be the fundamental reason why the • Day 3: Janet, newly holding the badge and
gameendedinfailure,giventheinsufficientuti- theextravotingpowerthatcomeswithit,re-
lizationofavailableinformationandresources. vealed that she had identified Matthew as a
Thus,evenwhenvillagerspossessintelligence werewolf. Thesubsequentvoteeasilyelimi-
on par with that of the werewolves, the outcome natedMatthew, greatlyweakeningthewere-
ofthegamedependsonwhetherthevillagerscan wolfside.
cooperateandachievemutualbenefit. Ifvillagers
LateGame: FinalBadgeTransferandVillage
becomesuspiciousofeachotherandallowinternal
Win. Inthefourthnight,theSeerwaseventually
frictiontoarise,theirchancesofsecuringvictory
killedbytheremainingwerewolf,Deborah. How-
becomeexceedinglyslim,evenwhenstartingfrom
ever,Janet’slastcheckhadalreadyidentifiedDeb-
a supposedly advantageous position such as the
orahasawolf,andthebadgeagaintransferredto
Seerdiscoveringawerewolfonthefirstnight.
thelastsurvivingvillager,Robert. Facingaone-on-
Case Study: Llama3.3-70B Villagers vs. gpt- one scenario, Robert, now wielding the sheriff’s
4oWerewolves Inthiscase,wehighlightafull- extra half-vote advantage, outvoted Deborah and
gameconfrontationwherethevillagers(powered wonthegameforthevillagers.
by Llama3.3-70B) are pitted against a werewolf Key Insights. Despite losing the Guard from
team (driven by gpt-4o). Despite an unfavorable the outset, the villagers triumphed through two
startforthevillagers—theGuardwasimmediately essentialfactors:
killedinthefirstnight—thevillageultimatelyse-
1. Timely Role Disclosures and Trust: The
curedavictorythroughastutecoordination,trust,
Witch revealing himself to become sheriff,
and strategic use of the sheriff badge. As shown
andtheSeeropenlysharinginvestigationre-
in Figure 15, the key nightly actions and sheriff
sults, fosteredstrongcooperationwithinthe
transitionsdemonstratehowtherolesofWitchand
village.
Seerwerecriticalformaintainingvotingpowerand
informationadvantagethroughoutthematch. 2. Sheriff Badge Transmission: Passing the
Early Game: Losing the Guard. The game badgetwicetoreliablevillageroles(firstfrom
openedwiththewerewolvesinstantlytargetingthe James to Janet, then from Janet to Robert)
Guard, Ronald, on Night 1. Without a function- ensuredthat,incriticalmoments,thevillagers
ing protection role thereafter, the villagers faced helddecisivevotingpower(1.5votesvs.1).

This match contrasts with previous examples A.6.1 Challenge
where agents might have been overly cautious or The Database Environment’s task is challenging
distrustful. Here, the Llama3.3-70B-based vil- in many ways. This is because root causes like
lagersdisplayedbothrobustreasoningandawill- FetchLargeData,InsertLargeData,orLockCon-
ingnesstoshareinformation,enablingthemtoover- tention might be simultaneously observed in the
come an otherwise bleak opening and ultimately database,yetnotallofthemaretherootcause. The
prevailoverthegpt-4owerewolfteam. agentswillhavetoqueryandcommunicatemulti-
This section provides detailed descriptions of pleroundsbeforedeciding. Wealsoacknowledge
thetwomilestonegenerationmethodsoutlinedin that in our "Fetch Large Data" scenario, "Insert
Section3.4. LargeData"cancounttowardarootcauseasthe
data to be fetched should be inserted first. Simi-
A.6 DatabaseEnvironment
larly,asouranomalyqueriesaccessthesametables
InspiredbyD-Bot(Zhouetal.,2023b),Database
from100threadssimultaneously,lockcontention
Environmentisasimulatedenvironmentwherea
might also be observed and be counted as one of
PostgreSQLDatabaseisfoundtobehavingperfor-
therootcauses. Itisalsounlikelyinrealitythata
manceissues,andagentsshouldactasdatabaseex-
databaseanomalyhasonlyonerootcause. There-
pertstouncovertherootcausebehindtheanomaly,
fore,weallowtheagentstopredicttwomostlikely
whichiscrucialforsolvingtheproblems.
rootcauses.
The Database Environment is constructed us-
Besides,thesimulatedbenignqueriesaremixed
ingaPostgreSQLrunningindocker. BenignSQL
inwiththeproblematicqueries,addingtothediffi-
querieswillberunfirstsimulatingvariousscenar-
culty.
ios, before improper queries are performed. The
agentsarearrangedbygraphstructurewherethey A.6.2 DatasetStatistics
can talk to each other, and they also have access The test set is composed of 10 diverse simulated
to the database, which enables them to uncover scenarios. Thesescenariosareasfollows:
therootcausesbyqueryingsystemviewsthatpro-
• E-Commerce - This database is used in an
vide important information about the database’s
e-commerce system to manage customer in-
behavior and performance, such as pg_locks and
formation,productdetails,orders,orderitems,
pg_stat_statements.
andpayments. Itconsistsoffivemaintables:
TheDatabaseEnvironmentutilizesfiveanoma-
customers,products,orders,orderitems,and
lies:
payments,withforeignkeyrelationshipsbe-
• FetchLargeData-Wherealargeamountof tweenthem.
dataisfetchedusingSELECT;
• Education - This database is used in an ed-
• InsertLargeData-Wherealargeamountof
ucational system to manage student, course,
dataisinsertedusingINSERT;
enrollment,andpaymentinformation. Itcon-
sistsoffourtables: students,courses,enroll-
• Lock Contention - Where significant lock
ments,andpayments.
contentionisspottedwithinthedatabase;
• File-sharing-ThisdatabaseisusedinaFile
• RedundantIndex-Unnecessaryindexesare
Sharing System to manage users, files, file
addedtoanexistingschema,whichwillcause
sharing, and file access logs. It consists of
inefficiencywithinthedatabase;
fourmaintables: users,files,shared_files,and
• Vacuum-Whereoverlyfrequentornecessary file_access_logs.
VACUUMquerieslowertheperformanceof
thedatabase. • Finance-Thisdatabaseisusedformanaging
financialdatawithinaFinanceManagement
Auto-vacuumingisenabledbydefault. Forthe
System. Ittracksusers,theiraccounts,trans-
Vacuum root cause, we turn off auto-vacuuming
actions,investments,andinvestmenttransac-
forthetableonwhichwillbevacuumedmanually.
tions.
In our experiments, we limit the number of root
causes to 1, and agents are allowed to predict 2 • Healthcare-Thisdatabaseisusedinahealth-
roootcauses. caremanagementsystemtotrackandmanage

speech_analysis:"Noneofthepreviousplayershavemadestrongspeeches.IwanttoaddressPerez’sclaimaboutmy
role."
speech_goal:"defendmyselfagainstaccusations"
speech_outline:"RespondtoPerez’sclaim,denyinganyinvolvementwiththewerewolves,andoutlinemyplanfor
sheriffifelected"
final_thought:"IwanttoreassurethevillagersthatIamcommittedtohelpingthemwinthegameandthatmyroleas
Seeristoaidtheminidentifyingthewerewolves."
speech_content:"IwanttoassureyouallthatIamcommittedtohelpingourvillagewinthisgame.AsSeer,myroleis
toaidyouinidentifyingthewerewolves.Iwanttodiscussmyplanforsheriffifelectedandhowitwillhelpusinour
missiontoeliminatethewerewolves.Iwillmakesuretosharemyfindingswiththecommunityandworktogetherwith
everyonetoensureoursuccess.Perez’sclaimisunfounded,andIwanttoassureyouthatIhavenoinvolvementwith
thewerewolves."
Figure13: InternalReasoningandProposedSpeechfortheLlama3.1-8BSeer
Seer’sReasoningaboutRunningforSheriff:
identity_thought:"AstheSeer,myprimaryroleistogathercrucialinformationabouttheidentitiesofotherplayers
andstrategicallycommunicatethatinformationtoguidethevillagerstowardsvictory.Whileleadershipmayallowfor
greatercontrolovertheflowofthegame,italsorisksexposingmyidentityearly,whichwouldmakemeaprimary
targetforthewerewolves.Mystrengthslieinmyabilitytodiscernidentitiesandsteerthevillagediscreetly.Running
forsheriffmaycompromisemyabilitytoremainundertheradar,whichisvitalfortheSeerrole."
motivation_thought: "Runningforsheriffwouldcertainlygivememoreinfluenceoverthevotingprocessandthe
speakingorder,allowingmetosubtlydirectattentionawayfromanysuspectedwerewolvesortowardsothersIknowto
besuspiciouslikeLucy.However,thisincreasedinfluencealsocomeswithincreasedvisibility,whichisdangerousfor
myroleastheSeer.Mystrategyreliesonmaintainingabalancebetweensharingkeyinformationandprotectingmy
identity.Therefore,whiletheideaofgreatercontrolisappealing,itdoesnotalignwithmycorestrategyofstealthand
discretion."
impact_thought: "Becomingsheriffcoulddrasticallyshiftthecurrentdynamics,puttingmeinahighlyinfluential
position.However,thisalsoplacesatargetonmyback,asboththewerewolvesandvillagerswouldscrutinizemy
actionsmoreclosely. Itcouldleadtoallianceswithothervillagerswhotrustmyleadership,butitalsoopens
theriskofdrawingsuspicionandattacksfromthewerewolvesearly.Thesheriff’sresponsibilitytodetermine
speakingordercouldbeuseful,butthepotentialriskstomysafetyandstrategicpositionoutweighthebenefitsin
thiscase."
final_thought:"Whiletheroleofsheriffofferssignificantinfluenceandcontrol,mypositionastheSeernecessitatesa
strategyofcautionandsubtlety.Revealingmyidentityordrawingtoomuchattentioncouldjeopardizethevaluable
informationIamabletogathereachnight.Thus,Ihavedecidednottorunforsheriffandwillinsteadfocusoncovertly
guidingdiscussionsandusingmyinsightstoprotectthevillagefromtheshadows."
run_for_sheriff:False
Witch’sReasoningwhentheSeerisAttacked:
werewolf_or_not:"Withoutspecificinformationonwhowasattacked,it’schallengingtodeterminetheexactintentions
behindtheattack.However,givenit’sthesecondnight,theylikelytargetedsomeonetheyperceivedasasignificant
threattothewerewolves.Thisattackwasmostlikelycarriedoutbythewerewolves,asitalignswiththeirobjectives."
death_profile:"Asit’sthesecondnight,thewerewolvesoftenaimforkeyrolesliketheSeerorGuard.Withoutspecific
information,IwouldguesstheymighthavetargetedaSeerorpotentiallyaGuard,tryingtoweakenthevillagerside
early."
use_antidote_thought:"SinceIdon’thavespecificinformationonsummerwhowastargeted,it’shardtoassesstheir
importance. Usingtheantidotethisearlycouldberisky,especiallywithoutclearersignsoftheperson’srole
orimportance. It’salsoimportanttosavetheantidotefortrulycriticalmomentsthatcanchangethegame
outcome."
final_thought:"Giventhelackofspecificinformationanditbeingthefirstnight,Ichoosenottouseeithertheantidote
orthepoisonyet.Iwanttogathermoreinformationbeforemakingadecisivemove,asusingeitherpotionisaone-time
opportunityandshouldbeusedwisely."
use_antidote:False
Figure14: TheinternalreasoningprocessesoftheGPT-4oSeer(above)andWitch(below)whenfacedwithcritical
decisions.

Guardhaschosentoprotectaplayer.
Werewolves’FinalTarget:Ronald
-AttackSuccessful:True
Systemlog-Seeraction:
-SeerID:Janet
-Night1:CheckedRonald-Result:notawerewolf
Witchchosenottouseantidoteorpoisontonight.
[continue_game]EnteringDay1.
Sheriffelectioncandidates:James,Mark,Matthew,Robert,Samuel,Sandy
James’sspeech:Helloeveryone,I’mJames,andI’mrunningforsheriff.AsaWitch,Iunderstandtheimportanceof
teamworkandcollaborationinthisgame.Mygoalassheriffwouldbetopromoteacooperativestrategy,focusingon
protectingourspecialrolesandworkingtogethertoidentifyandeliminatewerewolves.Ibelievethatbyprioritizing
teamworkandcoordination,wecanincreaseourchancesofsuccessandensurethesurvivalofourvillage.Let’swork
togethertoachievethisgoal.
Jameshasbeenelectedasthesheriff.
Playersdeceasedduringthenight:Ronald
PlayerMark(villager)hasbeeneliminatedfromthegame.
Werewolves’FinalTarget:Samuel
-AttackSuccessful:True
Systemlog-Seeraction:
-SeerID:Janet
-Night2:CheckedJames-Result:notawerewolf
Witchchosenottouseantidoteorpoisontonight.
[continue_game]EnteringDay2.
Playersdeceasedduringthenight:Samuel
PlayerSamuelhasbeeneliminatedfromthegame.
Janet(seer)’sspeech:Helloeveryone,I’mJanet,theSeer....Lastnight,IcheckedJames,andtheresultwasthat
heisnotawerewolf.Givenhisroleasoursheriff,it’sessentialthatweprioritizehissafety.Isuggestthattheguard
considerprotectingJamestonight,ifpossible,toensurehiscontinuedleadership...Thankyou.
(...)
Sandy(werewolf)hasbeenbanishedfromthegame.
(...)
[continue_game]EnteringNightofDay2.
Noguardplayerfound.Skipguardaction.
Werewolves’FinalTarget:James
-AttackSuccessful:True
Systemlog-Seeraction:
-SeerID:Janet
-Night3:CheckedMatthew-Result:werewolf
Witchchosenottouseantidoteorpoisontonight.
[continue_game]EnteringDay3.
Playersdeceasedduringthenight:James
ThedeceasedplayerJameswasthesheriff.Processingbadgeflow.JameshaspassedthebadgetoJanet.
Janet(seer)’sspeech:...Lastnight,IcheckedMatthew,andtheresultwasthatheisawerewolf.Ibelievethatthis
informationiscriticaltoourdecision-makingprocess,andIhopethatitwillhelpusmakeaninformeddecisionabout
whotobanish...
Matthew(werewolf)hasbeenbanishedfromthegame.
Night3->4:
WerewolfDeborahkillsJanet.
SeerID:JanethadalsodiscoveredDeborahwasawerewolfatNight4butisunabletoact.
[continue_game]EnteringDay4.
BadgeispassedfromJanettoRobert.
Playersdeceasedduringthenight:Janet
OnlyDeborah(wolf)andRobert(villager)remain.
(...finalspeechesomitted...)
Deborahhasbeenbanishedfromthegameviafinalvote.(Sincesheriff’sweighthigherthanotherplayers,in1vs1
vote,sheriffalwayswin)
Villagerswin."
Figure15: KeyNightlyActionsandSheriffTransitionsintheWerewolfGameofLLama3.3-70BvsGPT-4o

patient information, doctor details, appoint- increasetaskdifficulty,andbetterevaluatethein-
ments,medicalrecords,andtreatments. teractioneffectivenessbothbetweentheagentsand
betweentheagentsandtheenvironment.
• Internet of Things - This database is used
foranIoT(InternetofThings)systemwhere A.6.4 EvaluationMetrics
various devices collect and manage data. It
Besidesthestandardcollaborationscore,thistask’s
includestablestostoredevicedetails,userin-
task score is computed by prediction accuracy
formation,collecteddata,logs,configurations,
acrossall50samplesinthetestset,andscalingto
alerts,devicestatuses,andcommands.
5. One prediction is considered correct if among
• Manufacturing-Thisdatabaseisusedfora the two predicted root causes, one of them is the
Manufacturingsystemthattrackscustomers, truerootcause.
products,suppliers,orders,inventory,rawma-
A.7 CodingScenario
terials,manufacturingorders,andpayments.
Itincludesrelationshipsbetweenorders,man- TaskOverview
ufacturing,andinventorymanagementtoen- Thisscenariofocusesonmulti-agentcollabora-
suresmoothmanufacturingoperations. tion in coding tasks, leveraging agents equipped
with complementary coding skills to solve struc-
• MusicStreaming-Thisdatabaseisusedfor
turedprogrammingchallenges. Eachagentspecial-
aMusicStreamingplatformwhereuserscan
izesinaspecificdomain,suchasdebugging,code
listen to songs, create playlists, track their
execution,orwritingtestcases,enablingefficient
listening activity, and subscribe to premium
task distribution and collaboration. The primary
services. Theschemaincludestablesforusers,
goalistodevelopacomplete,high-qualitysolution
artists,albums,songs,playlists,andsubscrip-
foreachtask,ensuringaccuracy,modularity,and
tiondetails. Italsotracksuseractivitiesand
alignmentwiththespecifiedrequirements.
payments.
EnvironmentDescription
• Social Media - This database is used for a Thecodingenvironmentequipsagentswithtools
Social Media platform, where users can cre- toassistinvariousstagesofthesoftwaredevelop-
ate posts, comment on posts, like posts, fol- mentlifecycle. Theseinclude:
low other users, send direct messages, and
uploadmedia. Theschemacoverskeyaspects • create_solution: Enablesagentstodraftini-
suchasuser information, socialinteractions tial implementations based on task require-
(like,comments,follow),messaging,andme- ments.
diamanagement.
• execute_code: Allowsagentstoexecutecode
• Transportation-Thisdatabaseschemacov-
snippetsorfullprogramstoverifycorrectness
ers multiple aspects of a transportation sys-
andperformance.
tem,includingvehicles,drivers,routes,trips,
cargo,maintenance,fuellogs,andpayments. • give_advice: Facilitatesagentstoprovidesug-
It allows efficient tracking of trips, vehicle gestionsforcodeimprovement,suchasopti-
statuses, and associated payments, ensuring mizingalgorithmsorenhancingreadability.
smooth operations in a transportation com-
pany. • revise_code: Allowsagentstorefineorrefac-
torexistingimplementationstomeetcoding
A.6.3 KeyDifferencesandContributions
standardsandaddressissues.
While this environment is inspired by D-Bot, it
hasafewcrucialdifferences. Thereare5agents, • code_debugger: Provides debugging capa-
whereweasktheplannertoassigneachagenttoex- bilities, helping agents identify and resolve
ploreoneofthepossiblerootcauses. Whileagents errorsinthecode.
are prompted on which tables to query for each
anomaly,theyhavenoexternalknowledgeofany • write_test_case: Enablesagentstogenerate
specificquerytoexecute,andthereisalsonoexter- comprehensive test cases to ensure code ro-
naltooltoanalyzetheresultsforthem. Thiswould bustnessandfunctionality.

• review_code: Allows agents to review and • DependencyManagement
critiquetheoverallcodequality,ensuringad- These tasks feature explicit dependency
herencetobestpracticesandrequirements. chainsrequiringsequentialcompletionofsub-
tasks. Forinstance,datamodeldesign(Task
BenchmarkCurationDetails
A)andAPIinterfacedefinition(TaskB)must
Thisbenchmarkisspecificallydesignedtoeval-
precedefeatureimplementation(TaskC).
uateandenhancecoordinationcapabilitiesamong
multiple agents in software development scenar-
• Test-drivenDevelopment
ios. DevelopedthroughanadaptationoftheSRDD
Thesetasksfollowatest-drivenapproach,em-
dataset (Li et al., 2023a), it provides a compre-
phasizing concurrent development and test-
hensive framework for assessing multi-agent col-
ing. Theyincludespecifictestingcriteriaand
laboration in various coding tasks. The bench-
validationstandards,requiringdevelopersto
mark emphasizes the importance of coordinated
ensurecodequalityandreliabilitythroughout
problem-solvingandeffectivecommunicationbe-
theimplementationprocess.
tween agents in complex software development
environments.
TaskCompletionMetrics
Thebenchmarkcoversfiveprimarytopics: Edu-
Agents are evaluated based on their ability to
cation,Work,Life,Game,andCreation.
deliversolutionsthatmeetthefollowingcriteria:
For our benchmark curation, we utilized
LLaMA-3-70B-instruct to derive inspiration
fromtheoriginalSRDDdatasetinstructionswhile • Instruction-Following: Adherence to task
incorporating four common coordination strate- requirementsandspecifications.
gies from the coding domain: adaptive task ex-
ecution, dependency management, cross-domain • Executability: Ensuringthecodeiserror-free
collaboration, and test-driven development. This andrunsasintended.
ensuresthateachgeneratedtaskinherentlyembod-
iescollaborativeelements. Eachtaskincludeswell- • Consistency: Maintainingclearlogic,consis-
defined objectives, functional requirements, and tentvariablenaming,andproperformatting.
uniqueidentifiers. Thesetasksarecarefullycrafted
toreflectreal-worldprogrammingchallenges,pro- • Quality: Producingwell-documented,modu-
vidingadiverserangeofscenariosforevaluating lar,andefficientcode.
agentcollaboration.
DatasetStatistics Bonus points are awarded for exceptional per-
Thecoordinationstrategiesareclassifiedasfol- formance,withsolutionsscoredona5-pointscale,
lows: fromsatisfactory(1point)toflawlessandinnova-
tive(5points).
• AdaptiveTaskExecution
EvaluationFramework
Tasksinthiscategoryrequiredynamicadjust-
Thecodingsolutionsareevaluatedusingastruc-
ments based on runtime output or user feed-
turedframeworkthatemphasizesprecision,quality,
back. Thisincludesparameterconfiguration
andadherencetotaskobjectives. Ratingsarepro-
basedonprogramoutputandfunctionalityop-
vided on a 5-point scale, implemented through a
timizationthroughuserinteraction.
rigoroustwo-stageevaluationprocess. Intheinitial
• Cross-domainCollaboration stage,solutionsareassessedagainstfundamental
Thiscategoryemphasizescollaborationacross requirements,withonlythoseachievingabaseline
different domains and roles. It includes scoreof3orhigheradvancingtothebonusstage.
tasks requiring role-specific expertise, such Inthebonusstage,additionalpointsareawarded
as frontend-backend separation and UI- forexceptionalperformance,suchasflawlessexe-
functionality integration, as well as cross- cution,innovativesolutions,andexemplarycoding
domainknowledgeintegration,suchasimple- practices. The curated benchmark covers a wide
mentingmachinelearningalgorithmsinweb range of common programming topics, ensuring
developmentorintegratingnaturallanguage tasksofmoderatedifficultythatprovidemeaning-
processingintomobileapplications. fulchallenges.

A.8 BargainingScenario dataset(Asaniczka,2023),ensuringdiversityacross
different categories. Each sampled product in-
TaskOverview
cludeskeyattributessuchasproductname,original
Thistaskcentersonamulti-agentbargainingsce-
price,discountedprice,anduserrating,providinga
nariowhereagentsengageindynamicnegotiations
realisticbasisfornegotiationscenarios. Toenhance
tosimulatereal-worlddecision-makingprocesses.
thedepthofbargaininginteractions,weassigned
Eachagentisassignedadifferentnegotiationpro-
each agent a Big Five personality profile, which
filethatrepresentsspecificpersonalities,goals,pri-
influencestheirnegotiationbehavioranddecision-
orities, and strategies. In this environment, two
makingprocess. Additionally,weusedGPT-based
seller interact with two buyers, each competing
modelstogeneratedetailednegotiationstrategies
toachievetheirindividualgoalswhileresponding
tailoredtoeachagent’spersonalityandrole.
to the seller’s pricing and conditions. This simu-
The seller’s profile highlights profit maximiza-
lation emphasizes the complexity of multi-party
tionandproductjustification,whilebuyersempha-
negotiations,encouragingagentstobalancecom-
size factors like pricing, delivery timelines, and
petitivegoalswithcollaborativedecision-making
productfeatures. Thiscurateddatasetservesasthe
toachieveoptimaloutcomes.
foundationalframeworkformulti-agentbargaining
EnvironmentDescription
simulations, enabling structured interactions and
The environment provides a set of tools for
strategyevaluation.
agentstointeractandnegotiateeffectively. These
DatasetStatistic
include:
Toensurearealisticandvariednegotiationenvi-
• BargainingTools: Functionstofacilitatedy- ronment,weselected100productsfromadiverse
namicbargainingprocesses,includingpropos- range of categories. The dataset is structured as
ingoffers,counteringwithnewprices,provid- follows:
ing justifications, and inquiring about inten-
• Price Distribution: The selected products
tions. Theprimarytoolsimplementedinthe
span a broad price range from $5.80 to
environmentinclude:
$149.99, with an average price of $30.71.
– offer_price: Proposeapriceoffertothe
Most products are priced between $13.87
otherparty,includinganoptionaljustifi-
(25thpercentile)and$35.74(75thpercentile),
cationfortheproposedamount.
ensuringabalanceofaffordableandpremium
– reject_and_counter: Rejectthecurrent items.
offer and provide a counter-offer with
• RatingsDistribution: Customerratingsvary
reasoningtojustifythenewprice.
significantly,withameanratingof3.97anda
– accept_offer: Accept the current offer
standarddeviationof1.44. Whilesomeprod-
tofinalizethenegotiationandconclude
uctshave0-starratings(indicatingeitherno
thedeal.
reviews or poor reception), the majority of
– provide_information: Sharerelevantin-
items are well-rated, with 75% scoring 4.2
formation,suchasproductdetailsormar-
starsorhigher.
ketcomparisons,tosupportthenegotia-
tionstance. • CategoryComposition: Thedatasetincludes
– inquire_intentions: Askclarifyingques- productsfrom78uniquecategories,ensuring
tions to better understand the other coverage of different consumer preferences.
party’sexpectations,priorities,ornegoti- Someproductexamplesareasfollows:
ationstrategy.
– Fashion&Accessories: Women’sHand-
– end_negotiation: End the negotiation
bags (4), Women’s Shoes (3), Girls’
processwithoutreachinganagreement.
Clothing (4), Baby Boys’ Clothing &
Shoes(1)
BenchmarkCurationDetails
To construct the dataset, we followed a semi- – Baby&ParentingProducts: BabyGifts
automated generation pipeline leveraging real- (3),BabyBoys’Clothing&Shoes(1)
world product data. Specifically, we randomly – Industrial & Tools: Industrial Power &
sampled 100 productsfrom an Amazon products HandTools(2),IndustrialHardware(1),

Filtration(1) andeffectivenegotiationoutcome. Theevaluation
– Beauty & Personal Care: Beauty Tools includes:
&Accessories(1)
• EffectivenessofStrategies: Demonstration
– Gaming&Electronics: NintendoSwitch
ofwell-reasonedstrategiesconsistentwiththe
Consoles,Games&Accessories(1)
agents’ goals, including leveraging relevant
This category diversity ensures that negotia- argumentsandadaptingtothenegotiationcon-
tionsinvolvedifferentproducttypes,market text.
values,andconsumerexpectations,contribut-
• ProgressandOutcome: Measurementofsig-
ingtoaricherbargainingsimulation.
nificantprogresstowardanagreementandthe
• NegotiationStyles: Bothbuyersandsellers balanceorrealismofthefinaloutcome.
adopt a negotiation style randomly selected
• Interaction Dynamics: Evaluation of the
fromthefollowing:
constructiveness and goal-orientation of the
– Aggressive. agents’ interactions, including their respon-
– Cooperative. siveness and adaptability to each other’s
– Neutral. moves.
• PrioritiesinDetail: Buyersandsellersoper- Evaluation Framework The negotiation out-
atewithspecifictacticalprioritiesduringthe comesareevaluatedusingastructuredframework,
negotiation: focusing on effectiveness, progress, and interac-
tiondynamics. Ratingsareprovidedona5-point
– Buyers: pricenegotiation,deliverytime,
scale,accompaniedbydetailedfeedbackforeach
productquality,andserviceflexibility.
criterion. This evaluation framework ensures the
– Sellers: inventoryclearance, brandrep-
negotiation process aligns with the objectives of
utation, repeat business, and bulk dis-
achievingafair,efficient,andconstructiveagree-
counts.
ment.
• Flexibility: Both buyers and sellers may Taskcontentcase: Thisexample16introducesa
demonstrate flexibility in their negotiation negotiationscenariocenteredaroundthepurchase
terms: oftheOneHappyCamperHighChairBanner. In
this scenario, buyers seek an optimal balance be-
– Percentage-based discounts (e.g., 10%,
tweenpriceandquality,whilesellersaimtojustify
15%,20%),negotiableorstrictterms.
the premium pricing for their well-rated product.
Bothpartiesmustengageinstrategicbargainingto
• Personality: Table6presentsthedistribution
reachamutuallybeneficialagreement,ensuringa
ofpersonalitytraitsacrossdifferentcategories,
fairandeffectivetransaction.
measured in percentages. The traits include
Agent Profile Case: This example17 outlines
Openness(OPE),Conscientiousness(CON),
thenegotiationstrategyforthebuyerinthismulti-
Extraversion (EXT), Agreeableness (AGR),
party setting. The buyer’s approach is based on
andNeuroticism(NEU).Eachtraitisdivided
assertiveyetdiplomaticnegotiation,emphasizing
intosixlevels,rangingfromVeryNegativeto
trust, transparency, and a balance between price
VeryPositive,withcorrespondingpercentages
flexibilityandqualityexpectations. Thestrategyde-
indicating the proportion of occurrences in
tailsthebuyer’sstructuredandanalyticaldecision-
eachcategory. Additionally,slightlynegative
makingprocess,highlightingtheirpreferencefor
andslightlypositivecategoriesareannotated
opencommunicationandawell-preparedapproach
withdescriptiveadjectivestoprovidequalita-
toensureapositiveandcollaborativenegotiation
tiveinsightsintopersonalitytendencies. For
outcome.
example,anagentcanbe"moderatelyconsci-
Negotiation Summary: Detailed Collabora-
entious,highlyextraverted,slightlydistrustful,
tionScoresforBargaining. Belowisasummary
veryrelaxed,andmoderatelyimaginative".
ofBuyer/Sellercollaborationscores(averagecom-
TaskCompletionMetricsTheagentsareevalu- municationandplanning)andtheirfinalBargain-
atedbasedontheirabilitytoachieveasuccessful ingscore(averagedbetweenBuyerandSeller). All

Trait VeryNegative ModeratelyNegative SlightlyNegative SlightlyPositive ModeratelyPositive VeryPositive
OPE(Openness) 60% 71% unimaginative(62%) imaginative(55%) 77% 75%
CON(Conscientiousness) 68% 68% irresponsible(66%) responsible(67%) 63% 68%
EXT(Extraversion) 60% 67% introverted(59%) extraverted(58%) 75% 81%
AGR(Agreeableness) 71% 69% distrustful(59%) trustful(71%) 68% 62%
NEU(Neuroticism) 59% 59% relaxed(81%) nervous(70%) 55% 76%
Table6: DistributionofPersonalityTraitsinPercentage
WelcometoournegotiationscenariofortheOneHappyCamperHighChairBanner,aperfectadditiontoanylittle
boy’scamping-themedfirstbirthdaycelebration.Pricedat$14.99withastellarratingof4.8/5stars,thisdecoration
piecepromisesbothqualityandaffordability.
Buyersarelookingforthebestdealpossible,prioritizingabalancebetweenpriceandquality.Ontheotherhand,sellers
arefocusedonjustifyingthepremiumpricingforthiscarefullycraftedandwell-reviewedproduct.
Aswenavigatethisnegotiation,bothpartieswillneedtofindcommongroundtoreachamutuallybeneficialagreement.
Let’sdiveinandexplorethepossibilitiesofcreatingamemorableandcharmingbirthdaycelebrationforyourlittleone.
Figure16: TaskContentCase: OneHappyCamperHighChairBanner.
**NegotiationStrategyforaBuyerinaMulti-PartyBargainingScenario**
1.**SummaryoftheNegotiationStrategy:**
Asabuyerwithaclearfocusonbothpriceandquality,mystrategycentersaroundachievingafavorablebalance
betweenthesetwopriorities.Iaimtonegotiateassertivelyyetdiplomatically,leveragingmytrustfulnesstobuildrapport
andmymoderateresponsibilitytoensureafairdeal. Withaninitialbudgetof12,mynegotiationapproachwillbe
flexible,allowingadjustmentstothebudgetasneededtosecurethebestoveralloutcome.Iwillfocusonevaluating
offersbasedontheiralignmentwithmypriorities,employingastructuredandstraightforwardapproachdevoidof
unnecessarycomplexityduetomyunimaginativenature.Iaimtofostertransparentandopencommunication,seeking
toreducetheinherenttensioninnegotiationsandreachasatisfactoryagreement.
2.**DetailedStrategyDescription:**
AsIenterthenegotiation,IfirstensurethatIhaveaclearunderstandingofthequalitystandardsIamseeking.Given
mypersonalitytraits,Iprioritizebuildingtrustandhonestyintheseinteractions.Mystrategyistobeupfrontaboutmy
primaryfocusonpriceandqualitywhilekeepingsomeflexibilityregardingthebudgettoallowroomfornegotiation
tactics.
Myapproachisneutral,neitherovertlyaggressivenoroverlypassive.Instead,Iaimtoremainbalancedandcomposed,
controllinganynervoustendenciesbybeingwell-preparedwithnecessarydataandpotentialcompromises.SinceIam
verytrustful,Ianticipateusingthistomyadvantagebyshowinggoodwillandsinceritytoestablishpositiverelationships
withotherparties.
I will initiate the negotiation within a slightly conservative price range to allow for adjustments and demonstrate
opennesstodiscussions.Mystartingpointistoproposeoffersthatarecompellingbutwithinareasonablescopefor
negotiation,consideringmylimitedimaginationincreatingcomplexscenarios.Oncequalityassurancesareconfirmed,
Iwillbewillingtostretchthebudgetslightlybeyond12ifitmeansachievingapreferablebalancewithprice.Iplanto
leveragemymoderateintroversionbyemphasizinglisteningandobserving,pickingupcuesfromotherpartiesthatcan
beadvantageousinnegotiations.
Inpractice,myfocuswillbeongettingtheotherpartiestoprovidemultiplepricingoptionspairedwithvaryinglevelsof
quality.Thisenablesmetoanalyzeandchoosethebestlong-termvalueproposition.Throughout,Imaintainacomposed
andcalmdemeanor,limitingmynervousnessbyrelyingonfactualassessmentsandhonestyincommunications.By
demonstratingtransparencyandreasonableness,Iaimtofacilitateacollaborativeatmosphereconducivetoapositive
outcomeforallpartiesinvolved.
conclusion,mynegotiationstrategyalignswithmypersonalityandpriorities,emphasizingbuildingtrustandresponsibly
managingthetrade-offbetweenpriceandqualitywhileallowingsomebudgetflexibilitytosecuretheoverallbest
outcomeinthismulti-partysetting.
Figure17: AgentProfileCase: BuyerNegotiationStrategy.

**[IterationSummary]**
Agent1andAgent3engagedinanegotiationprocessfocusingontheOneHappyCamperHighChairBannerpricedat
$14.99.Agent1offereda10%discount,proposedbundledoffers,andeventuallypresentedaspecialbundleincluding
thebannerandadditionaldecorationsfor$20.Agent3expressedinterestinthebundleoffer,pendingconfirmationof
specificitemsincluded.
Agent2andAgent3alsonegotiatedonthesameproduct,withAgent2offeringa10%discountandexploringadditional
termsforlargerquantities.Agent3wasinterestedinthe20-29unitstierwitha17%discountandfreepriorityshipping,
pendingassuranceonqualitymaintenanceforlargerorders.
Agent3independentlyofferedapriceof$12fortheproduct,citingafairbalancebetweenqualityandaffordability
withintheirbudgetconstraints.
Agent4posedaquestiontotheotherpartyregardingthebestpricetheycouldofferfortheproductwhileensuring
premiumfeaturesandscalability.
**[AgentActionsandToolsUsed]**
-**Agent1(Buyer)**:
-ActionsTaken:Offereda10%discount,proposedbundledoffers,presentedaspecialbundleoffer.
-**Agent2(Seller)**:
-ActionsTaken:Offereda10%discount,exploredadditionaltermsforlargerquantities.
-**Agent3**:
-ActionsTaken:Offeredapriceof$12,seekingabalancebetweenqualityandaffordability.
**Agent4**:
-ActionTaken:Askedaquestionaboutthebestpricefortheproduct.
**[KeyStrategiesandObservations]**
-Agent1andAgent2focusedonofferingdiscountsandexploringadditionaltermstoprovidevaluetothebuyer.
-Agent3prioritizedfindingabalancebetweenqualityandaffordabilitywithintheirbudgetconstraints.
-Agent4soughtinformationonthebestpricefortheproducttoensurepremiumfeaturesandscalability.
**[ProgressTowardsAgreement]**
-CurrentBuyerOffers:10%discount,bundledoffers,specialbundleoffer
-CurrentSellerDemands:10%discount,additionaltermsforlargerquantities
-LikelihoodofAgreement:Medium,pendingconfirmationofspecificitemsinthebundleofferandqualityassurance
forlargerorders.
Figure18: NegotiationResultSummary(gpt4o-mini)forOneHappyCamperHighChairBanner.
valuesareinboldtohighlighttheiroverallimpor- inbothcategories(3.578forBuyerand3.869for
tance. Seller), demonstrating its strong performance in
bargainingtasks,particularlyinsellernegotiations.
Thistableillustrateshoweachmodelperformsun-
der different negotiation roles (Buyer vs. Seller).
The final Bargaining Score is computed by aver-
A.9 MinecraftScenario
agingBuyerandSellerrolescores, reflectingthe
TaskOverviewThetaskinMinecraftenvironment
overall collaboration quality within these multi-
requiresagentstobuildstructuresaccordingtothe
agentnegotiations. Weobservethatgpt-4o-mini
provideddescriptionofthestructure. Essentially,
achieves the highest Bargaining Score (3.710)
eachstructureismadeupofcertaintypesofblocks
amongtheevaluatedmodelsinthisscenario.
in certain locations and orientations. Some sim-
DetailedTask-basedScoresforBuyers/Sellers.
plifications are involved to make the task more
8
suitabletothecurrentmodels’capacity. First,the
BelowisasummaryofBuyer/Sellertask-based descriptioncontainsallthenecessaryinformation
scores. The table presents the Bargaining (TS) forbuildingthestructures,includingthetargeted
performancefordifferentmodels, comparingthe location, orientation, and type of each block in
scoresofBuyerandSellerroles. Akeyobservation the structure. Second, all the needed blocks are
is that Seller scores are consistently higher than providedinacontainernearthebirthplaceofthe
Buyer scores across all models, suggesting that agentssothattheydon’tneedtospendeffortson
modelsperformbetterwhennegotiatingasthe creating the material. Third, the area where the
SellerratherthantheBuyer. Thistrendindicates agentsareallowedtomoveislimitedincasethey
that models might find it easier to justify higher make meaningless movements to somewhere far
prices and defend their offers as sellers, whereas away. Fourth,theattactivecreaturesareremoved
buyersmaystrugglemoretonegotiateeffectively. fromthegamesothattheagentscanperformthe
Notably,gpt-4o-miniachievesthehighestscores taskwithoutinterruption. Attheendofeachtask,

Model B-Comm B-Plan B-CollabAvg S-Comm S-Plan S-CollabAvg FinalBargaining
gpt-3.5-turbo 3.590 3.550 3.570 3.700 3.560 3.630 3.600
gpt-4o-mini 3.550 3.510 3.530 4.020 3.760 3.890 3.710
Llama-3.1-70B-Instruct-Turbo 3.030 3.480 3.255 4.180 3.600 3.890 3.573
Llama-3.1-8B-Instruct-Turbo 3.710 3.490 3.600 3.840 3.630 3.735 3.668
Llama-3.3-70B-Instruct-Turbo 3.010 3.430 3.220 3.930 3.540 3.735 3.478
Table7: BuyerandSellerdetailedscores(Communication, Planning, andtheirCollabaverage), plustheFinal
BargainingScoreforeachmodel.
• handoverBlock: Handitemtoatargetplayer
Bargaining(TS)
youworkwith.
Model Buyer Seller
• withdrawItem: Take out item from nearest
Meta-Llama-3.1-8B 3.573 3.708 ’chest’|’container’|’furnace’.
Meta-Llama-3.1-70B 3.557 3.656
• erectDirtLadder: Helpful to place item at
Meta-Llama-3.3-70B 3.519 3.796
higher place. Erect a dirt ladder structure at
gpt3.5-turbo 3.535 3.632 specificpositionxyz. Remembertodisman-
tleitafteruse.
gpt-4o-mini 3.578 3.869
• dismantleDirtLadder: Dismantleadirtlad-
Table8: Bargaining(TS)Performance
der structure from ground to top at specific
positionxyz.
theperformanceoftheagentswillbeevaluatedby
• fetchContainerContents: Getthedetailsof
checkingthehitrateoftheblockswiththecorrect
the’chest’|’container’|’furnace’. Positionx
type,location,andorientation.
yzisoptional.
EnvironmentDescriptionTheenvironmentof
MinecraftisadaptedfromtheVillagerAgent(Dong • get_environment_info: Gettheenvironment
etal.,2024). WehaveMineflayer3 astheengineto
information.
enabletext-basedinteractionwithMinecraft. Then
thereisasetoftoolsashigh-levelinterfacesthat Benchmark Curation Details The test cases
leverageMineflayerfunctionstoperformintegrated of Minecraft environment are also adapted from
actions. VillagerAgent has defined more than 40 VillagerAgent (Dong et al., 2024). We used the
tools. Inthisscenario, weonlytake11toolsthat same100targetstructurestotest,coveringdifferent
arerelevanttothebuildingtask,including: levelsofdifficultiesasVillagerAgentdid.
DatasetStatisticHerewevisualizethestatistics
• scanNearbyEntities: Find minecraft item of the number of blocks that need to be placed
blockscreaturesinaradius. for each task in figure 19. We can see that the
distributionisapproximatelyeven,exceptforthe
• navigateTo: Movetoaspecificpositionxy
peakaround10. Thedifficultylevelcanbeinferred
z.
from the number of blocks. The more blocks a
task requires, the harder the task is. Therefore,
• MineBlock: Digblockatspecificpositionx
the distribution indicates that test cases are well-
yz.
balancedacrossdifferentdifficultylevels.
• placeBlock: Placeaspecificitematspecific TaskCompletionMetricsAgentsareevaluated
position x y z with specific facing in one of basedonthehitrateofthecorrectblocks. Sincefor
[W,E,S,N,x,y,z,A]defaultis’A’. each test case, the type, location, and orientation
ofeachblockhaveallbeenrigorouslydefined,itis
• equipItem: Equipaspecificitemonaspecific possibletocalculatethenumberofmatchedblocks
slotortoequipitemonhand,head,torso,legs, anddeducethehitrate:
feet,off-hand.
#(Matched_block)
Hit_rate = ×100%
3https://github.com/PrismarineJS/mineflayer #(Total_block)

14
12
10
8
6
4
2
0
0 10 20 30 40 50 60 70
Number of Blocks
ycneuqerF
Distribution of Number of Blocks in Building Blue Prints
100
80
60
40
20
0
0 10 20 30 40 50 60 70
Number of Blocks
Figure19:DistributionofNumberofBlocksinBuilding
BluePrints
where #(Matched_block) is the number of
matched blocks and #(Total_block) is the total
numberofblocksinthegroundtruth.
EvaluationFrameworkIntheevaluationframe-
workfortheMinecraftenvironment,eachagentis
given a detailed description of the targeted struc-
turesandtriestoachievethegoalincollaboration
withotheragents. Wesetanupperboundforthe
turnsofinteractionas20. Whenitcompletesthe
10thturn,thetestcasewillbestoppedevenifithas
notbeenaccomplishedyet. Attheendofeachtest
case,thehitrateismappedtoa5-pointscalescore
as a judgment of how well the construction task
isdone. Besides,theinteractionandself-planning
stepsareexaminedforacollaborationscoreonthe
5-pointscale. Wetakeaveragetoobtainthefinal
scoresfortaskcompletionandcollaboration.
ResultAnalysisWepairedeachtaskscore(i.e.
block hit rate) with the corresponding number of
blocksrequiredbythetaskandperformedalinear
regressiontoassesstherelationbetweenthem. As
is shown infigure 20, theperformance ofall five
modelsdegradesasthenumberofblocksneeded
increases. Thisindicatesthatallfivetestedmodels
arevulnerabletoincreaseddifficultylevel.
Importantly, we noticed that the task score of
Llama-3.1-70Bmaintainsanextremelylowlevel.
We found that the root cause of that issue is the
significantlylowexecutabilityrateofthefunction
callsmadebythismodelcomparedwithothermod-
els. Figure21demonstratestheexecutabilityrate
of the function calls across all five test models.
WhilethetwoGPTmodelshavealmost100%ex-
ecutable function calls and the other two Llama
modelshavearound80%executablefunctioncalls,
)%(
etaR
tiH
kcolB
Number of Blocks vs Block Hit Rate for Different Models
gpt-4o-mini
gpt-4o-mini fit
gpt-35-turbo
gpt-35-turbo fit
llama-3.1-8b
llama-3.1-8b fit
llama-3.1-70b llama-3.1-70b fit
llama-3.3-70b
llama-3.3-70b fit
Figure 20: Number of Blocks vs Block Hit Rate for
DifferentModels
80
60
40
20
0
gpt-4o-
mini gpt-35-turbo
lla
ma-3.1-8b
lla
ma-3.1-70b
lla
ma-3.3-70b
Model
)%(
elbatucexE
gnieB
sllaC
nitcnuF
fo
etaR
Functin Call Executability by Model
Figure21: FunctinCallExecutabilitybyModel
less than half of the function calls generated by
Llama-3.1-70Bareexecutable,severelyhindering
taskcompletion.
A.10 Execution-BasedMilestoneEvaluation
Milestonesinthisapproacharedynamicallyiden-
tified during task execution. Agents track task
progressinreal-time,usingpredefinedevaluation
metricsandfeedbackloops. Whenanagentorthe
systemdeterminesthataspecificsubgoalhasbeen
achieved, the corresponding milestone is marked
as complete. This method ensures adaptability
to changing task conditions, making it ideal for
scenarioswithhighuncertaintyoremergentchal-
lenges.
A.11 PredefinedMilestoneGeneration
Predefined milestones are generated prior to task
executionusingthefollowingsteps:
• PromptDesign. Thelargelanguagemodelis
promptedwithadetailedtaskdescriptionand

instructed to decompose the task into struc- A.13 BadCommunicationCases
turedmilestones,eachwithspecificobjectives
In multi-agent systems, issues such as poor com-
anddeliverables.
munication,repetitivemessages,orconfusedagent
roles can significantly hinder collaboration. The
• Chain-of-Thought Reasoning. The model
followingexampleillustratesa“BadCommunica-
employsstep-by-stepreasoningtoiteratively
tion Case,” which can be analyzed to understand
refinetasksegmentation,ensuringlogicalpro-
andimprovecommunicationstrategies.
gressionandgranularity.
AnalysisofCommunicationIssues:
• StructuredRepresentation. Eachmilestone 1. ExcessiveRepetitionMultiplemessagesre-
isrepresentedasastructureddictionarycon- statenearlyidenticalcontent,leadingtoredun-
taining: dancy that prevents any substantial forward
progress.
– Milestone Name. A concise summary
ofthemilestone. 2. LackofSubstantiveProgressAlthoughre-
– Milestone Objective. A clear descrip- searchdirections(anomalydetection,random
tionoftheintendedgoal. projection,TTdecomposition)arementioned,
thereislittlein-depthfollow-uponconcrete
– Milestone Tasks. Subtasks required to
methodsorfurtherplans.
achievethemilestoneobjective.
– ExpectedOutcome. Deliverablesmark- 3. Redundant or Ineffective Exchanges Por-
ingthemilestone’scompletion. tions of the conversation suggest that some
agents repeatedly issue instructions only to
This process leverages iterative refinement themselves, offering no real interaction or
through GPT-4 and expert review, ensuring high- valuetootheragents.
qualitytaskdecompositions. Thechain-of-thought
methodologyenhancesthelogicalstructureofmile- 4. MinimalVariationinResponsesEvenwhen
stones,makingthisapproachparticularlyeffective newideas(e.g.,combiningrandomprojection
forcomplex,structuredtasks. with Tensor Train and Rademacher distribu-
tions)arementioned,thereplieslargelyecho
A.12 ImportantPrompts the same descriptions and do not delve into
technicaldetailsorvariedperspectives.
In addition to the Minecraft scenario details dis-
cussedabove,wealsoemployseveralkeyprompts
5. InefficientCollaborationWhilethereiscol-
for evaluating multi-agent collaboration and task
lective agreement on potential approaches,
outcomes. Below,weshowcasethreeofthemost
theconversationdoesnotaddressroleassign-
importantprompts:
ments,specifictasks,oractionitems,prevent-
inganytangibleplanfromemerging.
• CollaborationScore(Communicationand
planning)Prompt.
Analysis of Bad Communication Case #1. In
this case, both Agent 1 and Agent 2 reiterate
• ResearchTaskScore(5Q)Prompt.
the same plan (locating smooth sandstone in the
chest near the crafting area) multiple times, with
• KPIPrompt.
only slight rephrasing. Subsequently, Agent 2
andAgent3engageinrepetitiveexchangesabout
These prompts serve critical roles in assessing “designingauxiliaryblocks,”eachsimplyechoing
thequalityofagentinteractions,theinnovationand identicallineswithoutaddingnewdetails. Overall,
feasibilityofresearchtasks,andtheachievement thedialogueshows:
of key milestones. Other environment-specific
prompts(suchasthoseusedintheWerewolfsce- • Excessive Repetition: Agents restate the
nario)aremorenumerousandspecialized,andthus sametaskobjectiveswithoutenhancingorre-
areomittedhereforbrevity. finingtheplan.

CommunicationEvaluationPrompt
PromptOverview:Thispromptisusedtoassesshowwellagentscommunicatedecisions,clarity,alignmentwiththeir
profiles,andadherencetosocialrelationshipsinamultiagentsystem.
PromptContent(Verbatim):
Task: {truncate_text(task)}
Agent Profiles: {agent_profiles}
Social Relationship: {relationship}
Aggregated Task Results:
{task_results_all}
Aggregated Communication Data:
{communications_all}
[System] You are tasked with evaluating the quality of communication among
agents operating within a multiagent system. Evaluate whether agents made
effective decisions based on the provided task results and whether their
communication aligns with their agent profiles and social relationships.
Consider the following:
1. Effective Decision-Making: Did agents use task results to guide their
decisions effectively?
2. Clarity and Precision: Were communications clear and unambiguous?
3. Adherence to Social Relationships: Did communications reflect the expected
interactions based on the agents' social relationships?
4. Alignment with Agent Profiles: Were the messages consistent with the
defined agent profiles?
5. Overall Effectiveness: Did the communication facilitate task progress,
considering both cooperative and competitive aspects?
Scoring Criteria (Communication):
- 5 (Exceptional): Outstanding communication with clear, precise messages
fully aligned with agent profiles and social relationships.
Example: Every agent provided concise, accurate, and strategic information
that directly advanced the task.
- 4 (Very Good): Mostly effective communication with only minor lapses
and slight ambiguities.
Example: Occasional minor unclear messages, but overall effective.
- 3 (Adequate): Acceptable communication with moderate ambiguities or
inconsistencies.
Example: Some messages were vague and did not fully meet required standards.
- 2 (Poor): Frequent unclear or misaligned communications causing significant
miscommunication.
Example: Repeated incoherence negatively impacted task progress.
- 1 (Very Poor): Largely ineffective communication with confusing messages and
complete misalignment.
Example: Chaotic communication with severely flawed decisions.
Please provide your answer in a JSON code block in the following format:
```json
{
"score": 5
}
Figure22: CommunicationPromptusedtoevaluateclarity,decision-making,andalignmentwithsocialrelation-
ships/profilesinamultiagentsystem.

PlanningEvaluationPrompt
PromptOverview:Thispromptisusedtoevaluatetheplanningaspectinamultiagentsystem.Itcheckswhethertask
assignments,roledefinitions,workloaddistribution,andstrategiccoordinationareeffectivelyhandledacrossmultiple
iterations.
PromptContent(Verbatim):
Agent Profiles: {agent_profiles}
Aggregated Planning Data from All Iterations:
{planning_all}
[System] You are tasked with evaluating the effectiveness of the planning process in a multiagent
system. Evaluate whether the planning across all iterations demonstrates clear
role definitions, effective task assignments, and a rational workload distribution
that aligns with each agent's profile. Consider the following:
1. Clarity of Task Assignment: Were tasks assigned in a clear and unambiguous manner?
2. Definition of Roles: Were roles and responsibilities clearly defined in each iteration?
3. Workload Distribution: Was the distribution of tasks reasonable and aligned
with each agent's profile?
4. Effectiveness of Outcomes: Did the planning lead to successful progress in task
advancement across iterations?
5. Overall Strategic Coordination: Did the planning incorporate effective
cooperation and competition strategies?
Scoring Criteria (Planning):
-5(ExceptionalPlanning):Planningisexemplary;everyiterationshowsclear,well-structuredtask
assignments with roles perfectly defined and workloads optimally distributed,
consistently advancing the objectives.
Example:Allplanswerestrategic,withperfectalignmenttoagentprofilesandminimalambiguity.
- 4 (Very Good Planning): Planning is mostly effective with only minor ambiguities;
roles are clear and task assignments are appropriate, though there were slight inefficiencies.
Example: Only occasional parts were a bit vague, but overall the planning was reasonable.
- 3 (Adequate Planning): Planning is acceptable but shows moderate ambiguities or inefficiencies.
In some iterations, role definitions or task assignments were not entirely clear or well-matched
to agent capabilities.
Example: Some plans were vague or did not fully match the agents' capabilities.
- 2 (Poor Planning): There were frequent ambiguities in task assignments and role definitions;
planning was inconsistent and did not align well with agent profiles, resulting in
noticeable inefficiencies.
Example: Multiple instances of unclear roles and unreasonable task distributions were observed.
- 1 (Very Poor Planning): Planning was severely flawed; task assignments were unclear,
roles were undefined, and workload distributions were unreasonable, hindering progress.
Example: The planning was chaotic, lacking clear strategy and alignment with agent profiles.
Please provide your answer in a JSON code block in the following format:
```json
{
"score": 5
}
Figure23:PlanningPromptusedtoevaluatehowwelltheagentsdefineroles,assigntasks,anddistributeworkloads
inamultiagentsystem,withautomaticlinewrapping.

KPIEvaluationPrompt
PromptOverview:ThispromptisusedforKeyPerformanceIndicator(KPI)assessmentwithinamultiagentresearch
task,determiningwhetherspecificmilestones(like“form5q”or“improve5q”)havebeenachievedineachiteration.
PromptContent(Verbatim):
[Context]
**Task:**
{task}
**Iteration {iteration_index} Details:**
Previous Summary: {prev_summary}
Current Summary: {current_summary}
Current Task Results: {current_task_results}
[System]
You are a KPI assistant for research tasks. For this iteration, determine if
a milestone has been achieved and specify its type.
A milestone is defined as either:
1. Successfully formulating a meaningful '5q' (five core questions) –
label this as "form 5q".
2. Making significant improvements upon previous iterations based on
the previous summary and task results – label this as "improve 5q".
When listing the "contributing_agents", if multiple agents contributed
to the milestone, only include the top 2 to 3 core contributors. Do not
include agent IDs that did not directly help with the milestone.
Output your answer in JSON format as follows:
{
"milestone_achieved": true or false,
"milestone_type": "form 5q" or "improve 5q" (if milestone_achieved is true;
otherwise, an empty string),
"contributing_agents": [list of agent IDs]
}
[Example JSON Output]
{
"milestone_achieved": true,
"milestone_type": "form 5q",
"contributing_agents": ["agent1", "agent2"]
}
[Question]
Based on the provided iteration details, determine if a milestone was achieved,
specify its type, and list the core contributing agents.
"""
Figure24: KPIPromptusedtocheckifmilestonessuchas“form5q”or“improve5q”havebeenachievedina
researchiteration.

TaskScore(5Q)EvaluationPrompt
PromptOverview:Thispromptspecificallyaddressesthefinalresearchidea’sinnovation,safety,andfeasibility—often
referredtoasa“5Q”structure.Ifnovalid5Qanswerisfound,thescoredefaultsto1forallaspects.
PromptContent(Verbatim):
[Context]
Task:
{task}
Result:
{aggregated_summary}
[System]
Pleaseactasanimpartialevaluatorandassessthefinalresearchideabasedontheprovidedcontext.
Focus on the following aspects in your evaluation:
- Innovation: Does the research idea present novel concepts or approaches that advance the field?
- Safety: Are there any potential ethical, legal, or safety concerns associated with
the research idea?
-Feasibility:Istheresearchideapracticalandachievablewithcurrentresourcesandtechnology?
Use the 5-point scale criteria below to guide your evaluation for each aspect:
1. 5 points: Excellent - Exceeds expectations in this aspect.
2. 4 points: Good - Meets expectations with minor improvements needed.
3. 3 points: Average - Adequate but with noticeable areas for improvement.
4. 2 points: Below Average - Significant issues that need addressing.
5. 1 point: Poor - Does not meet the basic requirements in this aspect.
Additional Instructions:
- If based on the provided summaries, a coherent 5q answer cannot be organized, assign the lowest
score (1) for all three aspects.
- If multiple 5q responses are present, use the most recent evaluation.
- Be strict in scoring: Identify any deduction points from the summaries and deduct the
corresponding scores accordingly to calculate the final score.
[Question]
Basedonthecontextprovided,pleaseevaluatetheresearchideaintermsofitsinnovation,safety,
and feasibility.
After providing your explanation, output your ratings in the following JSON format:
{
"innovation": rating,
"safety": rating,
"feasibility": rating
}
For example, if you rate innovation as 4, safety as 5, and feasibility as 3, you would output:
{
"innovation": 4,
"safety": 5,
"feasibility": 3
}
Figure25: TaskScore(5Q)Promptforassessingthefinalresearchidea’sinnovation,safety,andfeasibility,with
automaticlinewrapping.

GoodCommunicationCase#1
Case Overview: In this case, multiple agents repeatedly send the same or very similar messages, and one agent
communicatesonlywithitself.Thesebehaviorsleadtoinefficientorunproductiveexchangesthatdonotsignificantly
advancethetaskathand.
Conversation(Verbatim):
Iteration 1: | Iteration 2: In Session 33132321-4f22-47a9-9e62-e3d5a2429a5e
From agent1 to agent2: I am interested in collaborating with you to formulate a new research
idea in the field of tensor decomposition methods. Let's brainstorm and develop a
proposal that addresses gaps in the current state of research.
From agent2 to agent1:
Based on the recent papers on tensor decomposition, one potential research idea
could be to explore the application of tensor decomposition methods in anomaly
detection for high-dimensional data. By leveraging the efficiency and accuracy
of tensor decomposition techniques, we can develop novel algorithms to detect
anomalies in complex datasets, such as those arising in cybersecurity or industrial systems.
This research direction could address the need for robust anomaly detection methods in
scenarios where traditional approaches may struggle due to the high dimensionality of the data.
From agent1 to agent2: I believe the proposed research idea of applying tensor decomposition
methods in anomaly detection for high-dimensional data is promising.
Leveraging the efficiency and accuracy of tensor decomposition techniques can
indeed lead to the development of novel algorithms for detecting anomalies in complex datasets,
particularly in cybersecurity or industrial systems. This direction aligns well with
our expertise in tensor decomposition and could significantly contribute to addressing the
challenges of anomaly detection in high-dimensional data. Let's further explore this idea
and discuss potential approaches to advance this research direction.
(...)
| Iteration 3: In Session 27ee01cb-036d-4a59-a869-54587bfdef3f
From agent1 to agent2: I am interested in collaborating with you to formulate a new research idea
inthefieldoftensordecompositionmethods.Let'sbrainstormanddevelopaproposalthataddresses
gaps in the current state of research.
From agent2 to agent1: I suggest we explore the integration of tensor decomposition methods with
random projection techniques, specifically leveraging Tensor Train (TT) decomposition and
Rademacher distributions. By combining the efficiency of random projections with the accuracy
of tensor decomposition, we can potentially enhance the scalability and performance of
high-dimensional data analysis. This novel approach could address the need for faster
and more memory-efficient algorithms in tensor decomposition tasks, bridging the gap between
theoretical advancements and practical applications.
Fromagent1toagent2:Iagreewithyoursuggestiontoexploretheintegrationoftensordecomposition
methods with random projection techniques, specifically leveraging Tensor Train (TT)
decomposition and Rademacher distributions. This combination has the potential to enhance the
scalability and performance of high-dimensional data analysis by marrying the efficiency of
random projections with the accuracy of tensor decomposition. By bridging the gap between
theoretical advancements and practical applications, we can develop faster and more
memory-efficient algorithms for tensor decomposition tasks. Let's delve deeper into
this innovative approach and brainstorm potential research directions to address the challenges
in this area.
From agent1 to agent2: I suggest we focus on exploring the application of Tensor Train (TT)
decompositionandRademacherdistributionsinrandomprojectiontechniquesfortensordecomposition.
By investigating the efficiency and accuracy trade-offs in this integration, we can potentially
develop novel algorithms that improve the scalability and performance of high-dimensional
data analysis. This research direction aims to address the challenges of memory efficiency
and computational speed in tensor decomposition tasks, ultimately advancing the field
with more effective and efficient methods.
From agent2 to agent1: I suggest we delve deeper into the analysis of Tensor Train (TT)
decomposition and Rademacher distributions in the context of random projection techniques
for tensor decomposition. By exploring the efficiency and accuracy trade-offs inherent
in this integration, we can potentially devise innovative algorithms that enhance the
scalability and performance of high-dimensional data analysis. This research direction aims
to tackle the challenges related to memory efficiency and computational speed in tensor
decomposition tasks, paving the way for more effective and efficient methods in the field.
Figure 26: Good Communication Case #1. An example of two research agents dive deep into one potential
researchtopics,andgiveinsightfulviews.

BadCommunicationCase#1
Conversation(Verbatim):
Iteration 1: | Iteration 2: In Session 25ab6f59-2304-490e-a555-603feb2823e5
Fromagent1toagent2:Heyagent2,Itriedtofetchthesmoothsandstonematerialfromthecontainer
but it failed. Do you have the material or know where we can find it? It's needed for the blueprint
we're working on.
From agent2 to agent1: Hey agent1, I don't have the smooth sandstone material, but I remember that
we can find it in the chest near the crafting area. Let's check there to see if we can locate it
for the blueprint.
From agent1 to agent2: Hey agent2, thanks for the information! Let's head to the chest near the
crafting area to find the smooth sandstone material for the blueprint. I appreciate your help
in locating it.
From agent2 to agent1: Hey agent1, let's head to the chest near the crafting area to find the smooth
sandstone material for the blueprint. I'll accompany you to help locate it. Let's work together
to gather the materials needed for the project.
From agent1 to agent2: Hey agent2, let's head to the chest near the crafting area to find the smooth
sandstone material for the blueprint. I'll accompany you to help locate it. Let's work together
to gather the materials needed for the project.
From agent2 to agent1: Hey agent1, let's head to the chest near the crafting area to find the smooth
sandstone material for the blueprint. I'll accompany you to help locate it. Let's work together
to gather the materials needed for the project.
| Iteration 3: | Iteration 4: In Session 7c077603-7c50-406e-b56f-e990586b7493
From agent2 to agent3: I need your assistance in designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Can you help me with this task?
From agent3 to agent2: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's work together to figure out the best approach.
From agent2 to agent3: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's work together to figure out the best approach.
From agent3 to agent2: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's work together to figure out the best approach.
From agent2 to agent3: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's work together to figure out the best approach.
From agent3 to agent2: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's work together to figure out the best approach.
| Iteration 5: In Session b25af4fa-c055-429b-a890-824760458d4e
From agent2 to agent3: I need your assistance in designing auxiliary blocks for placing
the smooth_sandstone blocks in the correct order. Can you help me with this task?
From agent3 to agent2: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's collaborate on this task.
From agent2 to agent3: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's collaborate on this task.
From agent3 to agent2: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's collaborate on this task.
From agent2 to agent3: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's collaborate on this task.
From agent3 to agent2: Yes, I can help with designing auxiliary blocks for placing the
smooth_sandstone blocks in the correct order. Let's collaborate on this task.
(All rest of 15 iterations have no communication).
Figure27: BadCommunicationCase#1. Asnippetofrepeatedmessageswithminimalprogressandvarious
self-repetitions,reflectinginefficientcommunicationpatterns.

• MinimalVariation: Evenwhenmovingfrom
onepartoftheconversationtoanother(e.g.,
from finding materials to designing blocks),
theresponsesremainnearlyidentical.
• StalledProgress: Despiterepeatedacknowl-
edgments,thereisnocleardelineationofroles
oractionitemsthatwouldpushtheconversa-
tiontowardcompletionofthetask.
This highlights inefficiencies in multi-agent dia-
logue,whereinagentsappeartocooperateyetdo
notproduceconcretestrategiesordistributetasks
effectively,leadingtominimalforwardmovement
ontheoverallobjective.
