Title: TongSIM: A General Platform for Simulating Intelligent Machines

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_adjacent/09_BK06_TongSIM.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:14+00:00
- page_count: 26
- status: ok
- text_char_count: 80787

Metadata:
- author: Zhe Sun; Kunlun Wu; Chuanjian Fu; Zeming Song; Langyong Shi; Zihe Xue; Bohan Jing; Ying Yang; Xiaomeng Gao; Aijia Li; Tianyu Guo; Huiying Li; Xueyuan Yang; Rongkai Liu; Xinyi He; Yuxi Wang; Yue Li; Mingyuan Liu; Yujie Lu; Hongzhao Xie; Shiyun Zhao; Bo Dai; Wei Wang; Tao Yuan; Song-Chun Zhu; Yujia Peng; Zhenliang Zhang
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Related Works (page 2)
  - Simulators for Embodied AI (page 2)
  - Benchmarks for Embodied AI (page 4)
- TongSIM Platform (page 4)
  - Platform Overview (page 4)
  - High Fidelity Scenes (page 6)
  - Customize Tasks and Scenes (page 6)
  - Agent (page 7)
  - Platform Features (page 7)
    - Physical Simulation (page 7)
    - Interactive Objects (page 7)
    - Experimental features (page 8)
    - Parallel Training (page 10)
- Benchmarks (page 11)
  - Single Agent Task: Spatial Exploration and Navigation (page 11)
    - Benchmark Overview (page 11)
    - Baseline (page 11)
    - Metrics (page 11)
    - Experiments and Results (page 12)
  - Multi Agent Task: Multi-Agent Cooperative Search (page 12)
    - Benchmark Overview (page 12)
    - Baseline (page 13)
    - Experiments and Results (page 14)
  - Human-Robot Hybrid Task: Robot Social Navigation (page 14)
    - Benchmark Overview (page 14)
    - Baseline and Metrics (page 15)
    - Experiments and Results (page 16)
  - Primary Composite Tasks: Household Benchmarking Test (page 16)
    - Benchmark Overview (page 16)
    - Test Procedure (page 17)
    - Experiments and Results (page 18)
  - Advanced Composite Tasks: Spatially Situated Social Intelligence Test (page 18)
    - Benchmark Overview (page 18)
    - Baselines and Test Procedure (page 19)
    - Experiments and Results (page 19)
- Discussion (page 20)
  - Various benchmarks (page 20)
  - Potential Applications (page 21)
  - Future Works (page 21)
- Conclusions (page 22)

Markdown Content:

TONGSIM: A GENERAL PLATFORM FOR SIMULATING
INTELLIGENT MACHINES
ZheSun,KunlunWu,ChuanjianFu,ZemingSong,LangyongShi,ZiheXue,BohanJing,
YingYang,XiaomengGao,AijiaLi,TianyuGuo,HuiyingLi,XueyuanYang,RongkaiLiu,
XinyiHe,YuxiWang,YueLi,MingyuanLiu,YujieLu,HongzhaoXie,ShiyunZhao,BoDai,
WeiWang,TaoYuan,Song-ChunZhu,YujiaPeng,ZhenliangZhang
StateKeyLaboratoryofGeneralArtificialIntelligence,BIGAI,Beijing,China
ABSTRACT
As artificial intelligence (AI) rapidly advances, especially in multimodal large
language models (MLLMs), research focus is shifting from single-modality text
processing to the more complex domains of multimodal and embodied AI. Em-
bodiedintelligencefocusesontrainingagentswithinrealisticsimulatedenviron-
ments, leveraging physical interaction and action feedback rather than conven-
tionallylabeleddatasets.Yet,mostexistingsimulationplatformsremainnarrowly
designed, each tailored to specific tasks. A versatile, general-purpose training
environment that can support everything from low-level embodied navigation to
high-levelcompositeactivities,suchasmulti-agentsocialsimulationandhuman-
AI collaboration, remains largely unavailable. To bridge this gap, we introduce
TongSIM, a high-fidelity, general-purpose platform for training and evaluating
embodied agents. TongSIM offers practical advantages by providing over 100
diverse, multi-room indoor scenarios as well as an open-ended, interaction-rich
outdoor town simulation, ensuring broad applicability across research needs. Its
comprehensiveevaluationframeworkandbenchmarksenablepreciseassessment
of agent capabilities, such as perception, cognition, decision-making, human-
robotcooperation,andspatialandsocialreasoning.Withfeatureslikecustomized
scenes, task-adaptive fidelity, diverse agent types, and dynamic environmental
simulation, TongSIM delivers flexibility and scalability for researchers, serving
as a unified platform that accelerates training, evaluation, and advancement to-
ward general embodied intelligence. The source code is publicly available at
https://github.com/bigai-ai/tongsim.
1 INTRODUCTION
Theemergenceoflargelanguagemodels(LLMs)hasrevolutionizedtheunderstandingofartificial
intelligence(AI).ResearchersquicklyuncoveredadiversearrayofcapabilitiesofLLMswithinthe
textmodal,includingmulti-turndialogueagents[17,1,45],automaticcustomerservices[29,42],
novel generation and completion [41, 25], text-based automatic non-player characters (NPCs) [5,
57], role-playing[30,35], andAI-engagededucationalsystems[6,10,11]. Asthecompetenceof
LLMs rapidly increases, expectations for these models have begun to shift from purely text-based
applicationstowardmultimodalextensions.
Consequently, a series of research works focused on connecting AI to the real world has emerged
[40,30,18,59].AparticularlyprominentareawithinthistrendisEmbodiedAI.Ratherthanrelying
on conventional labeled data, researchers in this field propose that training agents in high-fidelity
simulated environments and providing them with an embodiment and corresponding action-based
feedbackcaninjectnewvitalityintoAIdevelopment[36]. Asufficientlyrealisticsimulationenvi-
ronmentiscrucialtothisfield.Thisnecessityhasspurredthedevelopmentofavarietyofsimulation
platforms,suchasInteractiveGibson[52]andMINOS[37]thatfocusedonnavigation,VRGym[54]
addressingvarioushumaninterfacesformultimodalinteraction,andplatformsdedicatedtoindoor
household tasks [44, 21, 33]. While some simulation platforms primarily support only one or a
1
5202
ceD
32
]IA.sc[
1v60202.2152:viXra

Figure 1: TongSIM, a simulation platform for general-purpose embodied AI agent training and
evaluation. We provide diverse high-fidelity indoor and outdoor scenes that suit a large range of
tasks,aswellasmultipleembodiments,includingnotonlyhuman-likefiguresbutalsoroboticones.
few categories of embodied AI tasks, the scope of supported task types is observably increasing
[49,34,23].
Againstthisbackdrop,ageneral-purposesimulationplatformthatcansupportbothlow-leveltasks,
such as embodied robot training, and high-level tasks, such as single-agent and even multi-agent
socialsimulations,isessential. Suchaplatformcanprovideahighlyconsistentembodiedgeneral-
purposeagenttrainingenvironment, facilitatingresearchersfromdifferentfieldstoconductmodel
training, testing, and even develop new tasks on the same platform, which will help advance the
developmentofgeneral-purposeembodiedintelligence.
In this work, we present TongSIM, a high-fidelity, universal embodied intelligence training and
testingplatformthatsupportscomplexindoorandoutdoorscenesimulation,asshowninFigure1.
In this platform, we have constructed a diverse range of indoor and outdoor scenes. Leveraging
thesediverseandrichscenes, wehaveproposedaseriesofbenchmarks. Thesebenchmarkscover
awiderangeofagentcapabilities, includingperception, cognition, decision-making, human-robot
cooperation, spatial and social understanding, covering both low-level tasks (such as navigation)
andhigh-abstractiontasks(suchasmulti-agentgames),formingacomprehensiveevaluationsystem
thatspanstheentirespectrum[31]. Userscanindependentlyselectdifferentbenchmarkstotrainor
test specialized agents or integrate these benchmarks for general-purpose agents. Specifically, we
propose5categoriesofbenchmarkingtasks,includingsingle-agenttasks,multi-agenttasks,human-
robotinteractiontasks,primaryfamilycompositetasks,andadvancedfamilycompositetasks.
2 RELATED WORKS
ProgressinEmbodiedAIisinextricablytiedtodevelopmentsinsimulationtechnologiesandeval-
uation benchmarks. High-fidelity simulation environments offer low-cost, safe, and reproducible
training platforms for agents, while diverse benchmarks drive the evolution of these agents from
foundationalvisualnavigationtocomplex,long-horizontaskexecution.
2.1 SIMULATORSFOREMBODIEDAI
Theevolutionofsimulationplatformsoutlinesacleartechnicaltrajectory: transitioningfromstatic,
visually faithful environments designed for navigation, to physics-rich interactive worlds support-
2

Table 1: Comparison of embodied AI simulators. We compare TongSIM (Ours) with state-of-
the-artplatformsacrosssimulationengines,assetdiversity,platformfeatures,andsupportedtasks.
TongSIMpossessesthecommonfeaturesofcurrentstate-of-the-artsimulators,anditstandsoutin
city-levelinteraction,task-orientedfidelity,andthevarietyofthesupportedtasks.
TongSIM GRUtopia OmniGibson Habitat VirtualHome VirtualCommunity
Features
(Ours) [49] [24] [34] [32] [63]
Core EngineBase UE5 IsaacSim IsaacSim Bullet Unity3D Genesis
Scene 115 100Annotated 50 211 6 35UrbanAreas
Environment IndoorScope ✓ ✓ ✓ ✓ ✓ ✓
&Scenes OutdoorScope ✓ ✓ ✓ ✗ ✗ ✓
City-levelInteraction ✓ ✓ ✗ ✗ ✗ ✓
ParallelTraining ✓ ✓ ✓ ✓ ✗ ✗
Platform Task-orientedfidelity ✓ ✗ ✗ ✗ ✗ ✗
Features NPCControl ✓ ✓ ✗ ✓ ✓ ✓
Sim-to-RealSupport ✓ ✓ ✓ ✓ ✗ ✓
Single-Agent ✓ ✓ ✓ ✓ ✓ ✓
Supported Multi-Agent ✓ ✓ ✗ ✓ ✓ ✓
Tasks Human-RobotTeaming ✓ ✗ ✗ ✓ ✗ ✓
ingfine-grainedmanipulation,andcurrentlyadvancingtowardsgenerative,open-endedecosystems
poweredbyAI,aimingtoreconcilethetrade-offbetweentrainingscalabilityandphysicalrealism.
The Habitat platform [38] epitomizes high-efficiency and large-scale simulation. Comprising the
high-performance3DsimulatorHabitat-Simandtheembodiedreinforcementlearning(RL)frame-
workHabitat-Lab, itscoreadvantageliesinextremerenderingthroughput. Capableofrunningin
parallel at thousands of frames per second, it significantly accelerates the training cycle of RL al-
gorithms. Earlyiterations, primarilyutilizingreal-world3Dscandatasets(e.g., Matterport3D[9]),
focused on visual fidelity to support visual navigation tasks. With the release of Habitat 2.0 [46],
the platform integrated the Bullet physics engine, extending capabilities to interactive navigation.
Most recently, Habitat 3.0 [34] introduced humanoid avatars, establishing “Co-Habitat” scenarios
for human-robot-environment coexistence, marking a shift towards social interaction capabilities.
Sharing this focus on human-centric environments, VirtualHome [32] utilizes Unity3D to abstract
householdactivitiesintoexecutableprograms,specificallytargetingactionunderstandingandhigh-
leveltaskplanning.
UnlikeHabitat’semphasisonscenescale,SAPIEN[53]andiGibson2.0[23]prioritizeinteraction
precisionattheobjectlevel. SAPIENfocusesonmanipulationtasksinvolvingarticulatedobjects,
utilizingphysics-drivenactivestereoscopicvisionsimulationtobridgethevisualSim-to-Realgap.
iGibson 2.0 [23], an open-source environment built on the PyBullet physics engine, emphasizes
object-centric simulation. It supports various long-horizon household tasks, such as cleaning and
cooking,andintroducesanevaluationsystembasedonlogicalstates.
To further narrow the Sim-to-Real domain gap, some simulators have adopted GPU-accelerated
physics engines and ray-tracing technologies. NVIDIA’s Isaac Sim [28], built on the Omniverse
platform, leverages the PhysX 5 engine to provide high-fidelity physics simulation and integrates
real-timeraytracing. ItiswidelyappliedinindustrialrobotmanipulationandSim-to-Realtransfer
research. As the successor to iGibson [23], OmniGibson [24] has also migrated to the Omniverse
architecture. Utilizing the PhysX backend, it achieves real-time simulation of complex materials
suchasfluidsandcloth,accommodatinglarge-scalebenchmarkslikeBEHAVIOR-1K[24].
Furthermore, the field is evolving towards generative simulation. Genesis [4] acts as a nascent
universal physics engine, unifying simulation frameworks for rigid bodies, fluids, and soft bodies,
whileexploringtheuseofgenerativeAItoconstruct4Ddynamicworlds. Buildinguponthisgener-
ativecapability,VirtualCommunity[63]expandsthesimulationhorizonfromsinglehouseholdsto
city-levelecosystems.Itleveragesagenerativepipelinetoconstructdiverseurbandistricts,support-
ing complex physical and social planning tasks that require agents to navigate and interact within
metropolitan contexts. Concurrently, ProcTHOR [15] employs procedural generation to automati-
callyconstructmassiveenvironments,offeringaneffectivesolutiontothescarcityofscenedatafor
training. WecomparedthefeaturesofTongSIMandseveralstate-of-the-artsimulatorsinTable1.
Currently, simulationtechnologystillfacesatrade-offbetweenruntimeefficiencyandphysicalfi-
delity: platformspursuingextremespeed(e.g.,Habitat[38,46,34])oftensimplifycontactdynam-
3

ics, whereas those prioritizing high-fidelity physics (e.g., Isaac Sim [28], OmniGibson [24]) incur
significantly higher computational costs. Constructing a unified architecture that balances large-
scaleparalleltrainingwithhigh-precisionphysicalinteractionremainsacoreengineeringchallenge
inthefield.
2.2 BENCHMARKSFOREMBODIEDAI
Benchmarks in Embodied AI reflect the trajectory of task complexity: evolving from instruction
following and navigation to object manipulation in household settings, and finally to general task
planninginopenworlds.
Early benchmarks primarily focused on an agent’s spatial understanding of natural language in-
structions.Room-to-Room(R2R)[2]isaseminalworkinVision-and-LanguageNavigation(VLN),
requiring agents to plan paths in real-world scanned indoor environments based on linguistic in-
structions. Although R2R [2] propelled the development of multimodal models, the simplicity of
itsactionspaceandtaskstatetransitionslimiteditsutilityforevaluatingcomplexembodiedintelli-
gence.
ALFRED[43]elevatedthechallengetolong-horizon,compositionalhouseholdmanipulationtasks
(e.g., “rinse a mug and place it in the coffee maker”). ALFRED’s core contribution lies in intro-
ducingirreversiblestatechangesandlongactionsequences,rigorouslytestinganagent’slong-term
memory, task decomposition, and planning capabilities. This benchmark shifted the research fo-
cusfrompurenavigationtoscenariosrequiringfine-grainedobjectmanipulation,oftengroundedin
interactiveenvironmentslikeAI2-THOR[22].
Pursuing the goal of artificial general intelligence (AGI), subsequent benchmarks have sought
greater scale and behavioral diversity. BEHAVIOR-1K [24] represents a significant step toward
traininggeneralistagents.Containing1,000everydayhumanactivities,itemphasizeshuman-centric
behaviorsandrealisticsimulation, aimingtofostercapabilitiesfordiverse, open-endedtasks. Re-
gardingenvironmentscale, ProcTHOR[15]utilizesproceduralgenerationtobreaktheconstraints
oflimitedreal-worldscans,enablingtherapidcreationofmassiveembodiedAIenvironments. Af-
ter constructing simulation environments, the next step is to deploy tasks, which can be used for
both evaluation and training. Recent research has increasingly emphasized dynamic task genera-
tion,ratherthanrelyingontraditionallymanuallycollectedtasks[16,12,13]. However,mosttask
generation approaches are designed for highly structured domains, such as code-based tasks [61],
GUI-based tasks [7], or game-based tasks [62, 47]. Existing task generation approaches for em-
bodied 3D simulation environments are largely limited to low-level variations, such as modifying
scenes,objects,orspatiallayouts[15,50].
Recent research explores ultra-long-horizon planning and larger-scale environments. CookBench
[8]focusesoncomplexcookingscenarios,requiringintentrecognitionandfine-grainedinteraction
over long sequences, posing severe challenges to the reasoning capabilities of LLMs and vision-
language models (VLMs). GRUtopia [49] signifies a migration from indoor to city-scale environ-
ments,aimingtoexploreScalingLawsinEmbodiedAIandprovidingthefirstsimulationplatform
forgeneral-purposerobotsincomplex,socializedurbanscenarios.
These complex benchmarks collectively reveal a critical challenge: error accumulation in long-
horizon planning. In tasks like CookBench, minor deviations in early actions can be amplified
exponentially in subsequent steps, leading to task failure. Consequently, research into Embodied
World Models is becoming increasingly vital, with the core challenge being the maintenance of
temporal consistency and the mitigation of error accumulation. The evaluation paradigm is also
shifting, moving beyond simple task success rates to quantifying an agent’s capacity for physical
consistency,stateunderstanding,andcounterfactualreasoning.
3 TONGSIM PLATFORM
3.1 PLATFORMOVERVIEW
TongSIM is designed as a comprehensive and versatile simulation platform for general intelligent
machines. Built upon Unreal Engine 5.6 (UE5.6), the platform extends the native capabilities of
4

Multimodal data sensor High-fidelity simulation Indoor navigation Multi-agent cooperation
Env.
Large-scale NPC system Parallel training Home composite tasks Situated social reasoning
Functional Features Various Tasks
Infrastructure Support Task Dara
Value
Vision
Learning
Motor
Language
Cognition Level of intelligence
Software Evaluation System
Figure 2: Overview of the TongSIM system architecture. The platform contains a unreal engine-
based simulator and a python controller which can communicate with the simulator. Within the
simulator,fourfeaturesaresupported,includingmultimodaldatasensors,high-fidelitysimulation,
large-scaleNPCsystems,andparalleltraining. Basedonthisplatform,varioustasksaredeveloped
tosupportembodiedAI,suchasindoornavigation,multi-agentcooperation,homecompositetasks,
etc. Also,theplatformintegratestheevaluationsystemtoevaluatetheperformanceofagentsabout
tasks,abilities,andlevelofintelligence.
theenginethroughasuiteofcustom-developedwrappersandinterfaces. Theseextensionsfacilitate
robustcommunication, debugging, andcontrol, effectivelymanaginghigh-dimensionalsimulation
data—including scene semantics, object states, and agent metadata—to streamline agent training,
testing,andsecondarydevelopment.
Specifically,theTongSIMplatformcomprises115distinctsimulationscenarios,designedtosupport
adiversearrayoftasks. Theseenvironmentsarepopulatedwiththousandsofhigh-fidelityobjects.
To emulate realistic anthropomorphic behavioral patterns, we implemented 28 distinct interaction
functionstosatisfytheinteractionrequirementsofbothembodiedagentsandhumanusers.
TongSIM provides rich semantic annotations to support learning tasks. We assign category labels
to common objects, facilitating efficient filtering and supervised training. To support rule-based
autonomousnavigationforvirtualhumansandrobots,wehavebakednavigationmeshesintoboth
indoorandoutdoorenvironments. Furthermore, eachenvironmentisequippedwithaSceneMan-
ager, which provides users with ground-truth data, including scene metadata, segmentation maps,
spawnpoints,andnavigationinformation.Allprovidedassetssupportcustomsecondaryannotation,
allowingresearcherstotailordatatospecificrequirements.
ThesystemarchitectureofTongSIMisillustratedinFigure2. Tofacilitatetheintegrationofdiverse
agentsandmodels,TongSIMprovidesacomprehensiveapplicationprogramminginterfaces(APIs)
of Python. This enables developers to exert granular control over the simulation environment and
embodied agents via Python scripts. Key functionalities include: level management (loading/un-
loading),dynamicinstantiationofobjectsandavatars,charactermanipulation,stateretrieval,cam-
era control, retrieval of objects near specific coordinates, and the execution of native UE console
commands.
AtypicaloperationalworkflowcommenceswiththeinitializationoftheTongSIMUEServer,fol-
lowedbythedeploymentofaTongSIMUEClienttoestablishaconnection. UtilizingthePython
software development kit (SDK), users manipulate scenes, objects, NPCs, and agents, while the
resultingvisualstatesarerenderedandstreamedtoawebinterfaceforobservationbybothhuman
operatorsandagents. Simultaneously,theTongSIM-Audio2Facemodulesynthesizesandsynchro-
nizesfacialexpressionsandvocalizationsforNPCsandagents. Furthermore,theplatformsupports
immersive interaction via virtual reality (VR) devices, requiring the execution of a dedicated VR
Clienttointerfacewiththeserver.
5

Figure 3: Statistics of indoor environments in TongSIM. The dataset spans diverse functional cat-
egories (e.g., residential, commercial) and architectural styles (e.g., modern, classical Chinese),
designedtosupportcomplex,human-centrictasks.
3.2 HIGHFIDELITYSCENES
To support comprehensive and general-purpose agent training and testing, the TongSIM platform
offers a vast and diverse collection of simulation environments featuring varying levels of fidelity.
Specifically, this comprises 115 indoor environments and extends support to urban-scale outdoor
scenarios.
Regardingindoorsettings, adefiningcharacteristicofTongSIMisitscapacitytosupportcomplex
hybriddailylivingtasks. Toensuresemanticrealism,weengagedprofessionaldesignerstomanu-
allycuratespatiallayoutsandfurniturearrangements,therebyguaranteeingthattheseenvironments
strictlyadheretoanthropomorphicbehaviorallogic. Buildingupontheseexpert-designedenviron-
ments, we developed an automated expansion pipeline that scales the repository to a total of 115
distinctscenes. Functionally,theseenvironmentscoverdiversecategoriessuchasresidentialunits,
cafes, and retail stores. Stylistically, they span a wide architectural spectrum, ranging from mod-
ern apartments and villas to medieval castles, traditional Japanese gardens, and classical Chinese
architecture. DetailedstatisticsregardingtheindoorscenesarepresentedinFigure3.
Regarding outdoor scenarios, rather than assembling isolated environmental fragments, we have
constructedaholisticvirtualmetropolis,asillustratedinFigure4. Thisunifiedworldencompasses
diversefunctionalzones,includingeducationalinstitutions,residentialcomplexes,commercialdis-
tricts,andmedicalfacilities,alongwithacomprehensiveroadnetworkandadynamictrafficsimula-
tionsystem. Crucially,thesefunctionalzonesarespatiallycontiguous. Thisdesignenablesembod-
ied agents to navigate seamlessly across distinct regions, thereby preserving contextual continuity
duringlong-horizontrainingandevaluationtasks.
3.3 CUSTOMIZETASKSANDSCENES
ToenhancethescalabilityanddiversityoftheTongSIMenvironment,wedevelopedanautomated
proceduralgenerationpipelinecapableofexpandingthescenerepositorybasedonexistingassets.
Thismethodfollowsacoarse-to-finestrategy. Inthecoarse-grainedphase,wedecomposeexisting
indoorscenesintoindependentfunctionalunits(e.g.,bedroom,study,kitchen). Theseunitsarethen
stochastically recombined to synthesize novel layout configurations, where the door frames serve
asalignmentanchors. Inthefine-grainedphase,weintroducemicro-levelvariationstotheinterior.
Specifically,weapplyrandomperturbationstotheposesofmovableobjectsandrandomlyreplacea
subsetofassetswiththesame-categorycounterpartsretrievedfromourobjectlibrary. Thisprocess
significantlyenrichesthediversityofinteriordecor,spatiallayouts,andobjectappearances. Finally,
toguaranteethehighfidelityoftheTongSIMplatform,weemployahuman-in-the-loopvalidation
step where professional designers filter and fine-tune the generated scenes, pruning any instances
thatexhibitsemanticimplausibility.
Complementingtheautomatedgenerationpipeline,TongSIMfeaturesarobustexternalcontentim-
port framework. This framework is designed for high compatibility with mainstream digital con-
6

Figure4: VisualizationoftheTongSIMOutdoorWorld. Theplatformsimulatesaholistic,spatially
contiguousurbanenvironmentratherthanisolatedfragments.
tent creation (DCC), computer-aided design (CAD), and 3D scanning workflows, allowing exist-
ingassetstobeseamlesslyintegratedintotheplatform’ssimulationtasksandevaluationpipelines.
Throughaminimalpreprocessingprocedure,includingcomprisingunitstandardization,coordinate
systemalignment, andlightingconfiguration, userscanefficientlyimportcustomenvironmentsor
third-partyassets. Currently,TongSIMsupportsformatsincludingglTF2.0(.gltf/.glb),FBXScene,
andDatasmith(.udatasmith),comprehensivelycoveringindustry-standard3Ddatarepresentations.
3.4 AGENT
TongSIMprovidesdiverseagentsthatcanservebothasembodimentsforAImodelsduringtraining
and evaluation, and as NPCs to facilitate task execution and enhance environmental fidelity. To
governthebehaviorsoftheseNPCs, TongSIMimplementsahybridautomaticcontrolmechanism
drivenbyrule-basedlogicandLLMs.
TongSIMequipstheseagentswithversatilefunctionalcapabilitiesanddiversevisualappearances,
allowing external AI models to drive embodiments via a Python API. The supported action space
spansmultiplelevelsofcomplexity,includingkinematicprimitives(e.g.,nodding,waving,turning),
target-drivenbehaviorsdirectedatspecificcoordinatesorobjects(e.g.,gazing,point-to-pointnavi-
gation),andfundamentalobjectinteractions(e.g.,pick-and-place,togglingdoors,sitting/standing).
Furthermore, the platform supports complex composite activities that involve multi-step sequenc-
ingandhigh-levelsemantics,suchasconsumingitems,pouringliquids,mopping,wipingsurfaces,
reading,cuttingfood,andsimulatingdailyroutineslikesleepingorwashing.
3.5 PLATFORMFEATURES
3.5.1 PHYSICALSIMULATION
The platform leverages the built-in Chaos physics engine of Unreal Engine 5 to achieve rigid
body dynamics, fluid simulation, destruction, cloth, etc. This feature makes TongSIM suitable
for constructing relative complicated 3D scenes, which supports the testing for embodied AI like
robots. Meanwhile,wealsotrytointegrateanotherphysicssimulationlibrary(NVIDIAFlex)into
TongSIM, which uses a unified particle to represent all object types, allowing different simulation
materialstoseamlesslyinteract.
3.5.2 INTERACTIVEOBJECTS
Theplatformconstructsaprotocol-basedinteractionsystem,achievinggranularcontroloversimu-
lationentitiesthroughcoreprotocolssuchasinteractableability. Theplatformsupports28distinct
7

Figure5: StatisticsoftheobjectsinTongSIM.Thedatasetspansdiversefunctionalcategories(e.g.,
residential,commercial)andarchitecturalstyles(e.g.,modern,classicalChinese),designedtosup-
portcomplex,human-centrictasks.
interactionprimitivesandprovidesthousandsofinteractableobjects. Thestatisticsofsomeofthe
objects in TongSIM are shown in Figure 5. This system not only covers basic operations, such
as entity lifecycle management (generation, destruction) and geometric transformations (rotation,
scaling),butalsoimplementsdeepsimulationofelectromechanicallogicandspatialsemantic.
ElectromechanicalLogic. Thesystememploysadual-layercontrolmechanismthatdecouplesthe
“poweredstate”fromthe“activationstate”toaccuratelysimulatetheoperationalprinciplesofreal-
world devices. The final operational state of a device is jointly determined by its physical power
supply and switch control status; consequently, if an entity lacks a power connection, it remains
non-functionaleveniflogicallyactivated.Thisdesignfaithfullyreproducesthephysicaldependency
betweenelectricalconnectivityanddevicemanipulation.
Spatial Interaction Anchors. To address the challenges of fine-grained manipulation in complex
environments, the platform defines semantically annotated spatial interaction anchors. These an-
chorsguideend-effectors(e.g.,hands,roboticarms)topreciselytargetthecoordinatesoffunctional
zones,suchashandlesorbuttons,therebyestablishingrobustconnectionconstraints. Furthermore,
tofacilitatecompositeinteractionsinvolvingmulti-objectsynergy,wheretaskcompletionrelieson
specificspatialcoordinationbetweenentities,thesystemintroducestheconceptofPlacementPoints.
Thesepointsserveaspredefinedspatialdockingslotsthatautomaticallycalibratetherelativealign-
mentbetweenobjects,suchasaligningacupbeneathawaterdispenser.
3.5.3 EXPERIMENTALFEATURES
Automatic Procedural Actions. This module provides animation-asset-free, procedural locomo-
tion and arm articulation capabilities for humanoid agents within the TongSIM platform. An ex-
ampleisshowninFigure6. LeveragingControlRigandInverseKinematics(IK),thesystemsyn-
thesizes naturalistic gaits in real-time, adapting seamlessly to diverse skeletal structures and pro-
portions. It is designed for real-time, large-scale interactive scenarios. In TongSIM, procedural
animationserves asaunified foundationallocomotionlayer, deeply integratedwiththe platform’s
task,navigation,physics,andperceptionpipelines.Bysupportingparameterizationandcontrollable
stochasticity, the module ensures stability across diverse scenes, allowing users to rapidly deploy
agentsacrossarbitraryenvironmentsandbenchmarktaskswithoutmodifyingskeletalassets.
Text-Driven Motion Generation. This module implements a diffusion-based motion generation
modelthatsynthesizesplayablecharacteranimationsequencesinreal-time,utilizingtextualintent
and environmental voxel maps as inputs. A typical procedure is shown in Figure 7. The system
featuresthefollowingcorecapabilities. (1)Text-drivencontrol(naturallanguage+targetcontext):
Thesystemencapsulatesnaturallanguageexpressionsalongsidetargetpositionsandinteractionob-
jects within instructions. These are unified and parsed into executable intents and constraints for
8

Figure 6: In TongSIM, programmatic animation functions, as a unified fundamental motion layer,
areintegratedwiththeplatform’stask,navigation,physics,andperceptionpipelines. Programmatic
animationsupportsparameterizationandcontrollablerandomness,maintainingstabilityacrossdif-
ferent scenes. Users can rapidly deploy it in any scene and benchmark task without needing to
modifytheskeletonassets.
Figure7: Atypicalprocedureoftext-drivenmotiongeneration.
the model. (2) Environmental perception (voxelized geometric semantics): The system performs
real-timesamplingofvoxelgridsaroundthecharacter’scurrentpositionandthefirsttwotrajectory
waypoints. Thisconstructsspatialsemanticsrepresentingnavigableareasandobstaclestofacilitate
modelplanningandcollisionavoidance. (3)Segmentedgenerationandstreamingplayback: Lever-
agingabi-directionalgRPCstreamingpipeline,thesystemimplementsa“generate-while-playing”
mechanism. This ensures seamless concatenation and automatic continuation of subsequent se-
quences,achievinglow-latencyreal-timegeneration. (4)Voxelgenerationengine: Thiscomponent
providescomprehensiveenvironmentalvoxelencoding.Itconstructsavoxelvolumearoundthefirst
two path waypoints, performs parallel sampling of geometric occupancy, and generates a bitmap
byte stream transmitted with the request. (5) Controllable root motion fusion: The server dictates
therhythmofverticalmotion(e.g., undulationandfootfalltiming), whilehorizontaldisplacement
andsteeringaredynamicallyplannedbylocalnavigationandcontrolmodules.
Large-Scale Crowd Simulation. To support human-robot hybrid tasks (e.g., social navigation,
collaborative guidance, and interactive behavior learning), as shown in Figure 8, we constructed a
hierarchical crowd simulation module designed to simultaneously achieve individual-level physi-
calfidelityandgroup-levelbehavioraldiversity. (1)Low-levelmotioncontrol: Socialforcemodel
(SFM) and A*-based feasible region sampling. The foundational layer employs the social force
model, introducing force-based interpersonal interactions and environmental constraints to realize
naturalobstacleavoidanceandaggregationbehaviorsinlocalspace.(2)High-leveldecisionmaking
andplanning:Atthehigh-leveldecisionlayer,thesystemincorporatesVLMstosimulatetheseman-
tic behaviors of human agents and support interaction and collaboration with robotic agents. This
9

Figure8: Simulationofdiversecrowdandpedestrianmovementpatterns.
(a) (b)
Figure9: Paralleltraining. (a)Visualizationof48ParallelEnvironments. (b)ThestepsperSecond
variesasthenumberofparallelenvironments.
mechanism endows crowd simulation with semantic controllability and task relevance, achieving
semanticalignmentandintelligentsynergywiththerobot’staskplanningmodules.
From Simulation to Reality. To facilitate realistic robotic tasks and bridge the Simulation-to-
Reality(Sim-to-Real)gap,wehaveexploredtwoexperimentalintegrationstrategies. Thefirststrat-
egy involves replacing the native UE5 physics engine with the open-source MuJoCo engine [48].
In this configuration, thephysical simulation of all scene entitiesis delegated to MuJoCo, and the
resultingstateupdatesaresynchronizedwithUE5’srenderingpipelineforvisualoutput. Thisap-
proach integrates MuJoCo’s superior physical fidelity and robust robotic training capabilities into
TongSIM, effectively compensating for the limitations of UE5’s native dynamics simulation. The
second strategy introduces native support for Isaac Lab, migrating both the physics and rendering
enginestoIsaacSim. Crucially,thisintegrationpreservesTongSIM’sestablishedtaskarchitecture
andagentinterfaces.Thisdesignfacilitatesseamlessalignmentwiththeroboticscommunity,allow-
ing for the reuse of extensive toolchains within the robotics research ecosystem. Both approaches
are currently in the experimental phase, aiming to extend TongSIM’s compatibility to a broader
spectrumofagenttypesandachieveaunifiedsimulationframeworkfordiverseembodiments.
3.5.4 PARALLELTRAINING
Toaccommodatethedemandsforefficientagenttrainingandoptimizedatasamplingefficiencyin
RL, TongSIM introduces a multi-environment parallel execution mechanism. By simultaneously
loadingmultiplemutuallyindependentsub-levelswithinasingleUEinstance,thismechanismen-
ables agents to concurrently acquire interaction data from diverse environments at each time step,
therebysignificantlyamplifyingsamplegenerationthroughput.
10

Toevaluatetheperformanceofthismechanism,weutilizedthe“spatialexplorationandnavigation”
task (see Subsect. 4.1) as a benchmark. Experiments were conducted on a personal workstation
equipped with an Intel Core i9-13900KF CPU (24 cores/32 threads, 3.00 GHz) and an NVIDIA
GeForce RTX 4090 GPU. Experimental results demonstrate that, compared to single-environment
sequential execution, the parallel setting achieves a substantial increase regarding the interaction
throughputmeasuredinstepspersecond. Specifically,thesamplingrateexhibitsnear-linearscaling
as the number of parallel environments increases, as shown in Figure 9 (b). However, at higher
degreesofparallelism,performancegainsgraduallysaturateduetooverheadassociatedwithinter-
processcommunicationandsystemscheduling.
TongSIM’s parallel execution mechanism effectively enhances sample acquisition efficiency and
minimizestrainingtimecosts,establishingarobustfoundationforlarge-scalereinforcementlearn-
ingincomplexsimulationenvironments.
4 BENCHMARKS
4.1 SINGLEAGENTTASK: SPATIALEXPLORATIONANDNAVIGATION
4.1.1 BENCHMARKOVERVIEW
Autonomousexplorationandnavigationrepresentcriticalpillarsforintelligentagentsoperatingin
partiallyobservablephysicalenvironments. Effectiveexplorationdemandsthatanagentmaximize
coverage of the state space, converting unknown areas into semantic maps to locate targets of in-
terest. Subsequently, navigation entails executing optimal paths to reach these identified locations
while negotiating obstacles. To rigorously evaluate these competencies, we introduce the spatial
exploration and navigation test, a benchmark specifically designed to assess the exploration and
navigationperformanceofintelligentagents.
Thebenchmarkcentersonachallengingcleanuptask,asillustratedinFigure10,requiringtheagent
to navigate complex, multi-room indoor environments cluttered with obstacles to collect scattered
paper balls. To foster diversity, the quantity and spatial distribution of the targets, as well as the
agent’s initialization pose, are fully randomized. Crucially, to guarantee task feasibility, we pre-
calculatethetraversablefreespacebasedontheagent’scollisiongeometryandenvironmentalob-
stacles,ensuringthatboththeagentandalltargetsarestrictlyspawnedwithinreachableregions.The
environmentprovidesarichobservationspacecomprisingegocentricRGBimages,depthmaps,and
voxel grids. Correspondingly, the agent utilizes an action space designed for navigation, enabling
movementtospecificcoordinatesandrotationtowardtargetorientations.
4.1.2 BASELINE
Inthisbenchmark,weprojectthevolumetricvoxeldataofthetaskspaceontoa2Dplanetogenerate
an occupancy grid. Specifically, we extract an egocentric 19 × 19 local grid, corresponding to
a physical area of 208 cm × 208 cm, to serve as the agent’s observation. To establish a robust
baselineforcomparison,wetrainapolicyusingproximalpolicyoptimization(PPO)algorithm[39].
Furthermore,weincorporatehumantrialsintotheevaluationframeworktoquantifytheperformance
gapbetweentheautonomousagentandhumanoperators.
4.1.3 METRICS
Weemploytwoprimarymetricstoevaluateagentperformance: successrate(SR)andefficiency.
The success rate measures the ratio of episodes where the agent successfully explores the entire
taskspaceandeliminatesallscattereddebriswithinapredefinedmaximumnumberofsteps(T ).
max
Theefficiencyquantifiestheagent’stemporalperformancebasedonstepconsumption. Sincefewer
steps indicate superior performance, we formulate efficiency as a normalized score relative to the
maximumallowablesteps. Thesuccessrateiscalculatedasfollows:
N
SR= success ×100% (1)
N
total
11

Figure 10: An exemplary scenario of the paper ball cleaning task. The environment consists of
multiple rooms, eachfurnished with variousitems, with paper ballsscattered randomlyacross the
floor. Theagentundertestisspawnedatarandomlocationwithinoneoftherooms. Itisrequired
toexploretheseroomstocleanupallthepaperballs.
whereN representsthetotalnumberofevaluationepisodes,andN denotesthenumberof
total success
successfulepisodes. Theefficiencyisdefinedas:
Efficiency=
1
N (cid:88)success(cid:18)
T
max
−S
i
(cid:19)
(2)
N T
success max
i=1
where N is the count of successful episodes, T represents the maximum number of steps
success max
allowed per episode, and S denotes the number of steps taken by the agent to complete the i-th
i
successfulepisode.
4.1.4 EXPERIMENTSANDRESULTS
Table2: PerformancecomparisonbetweenHumanandRLAgent(PPO)onthebenchmark.
Agent SuccessRate Efficiency
PPO 0.6 0.34
Human 1.0 0.54
Usingtheproposedbenchmark,weevaluatedboththeRLbaselinemodel(PPO)andhumanoper-
ators. The comparative results are presented in Table 2. Quantitative analysis reveals that the RL
agentachievesasuccessrateofonly60%. Whiletheagentdemonstratesthecapabilitytocomplete
thecleanuptasktoacertainextent,itsperformancesignificantlylagsbehindthehumanbaselinein
bothsuccessrateandefficiency.
Toinvestigatetheunderlyingcausesoftheagent’ssuboptimalperformance, weconductedaqual-
itative analysis of the failure cases. We identified two primary limitations as follows. (1) Obsta-
cle avoidance in cluttered environments: The RL agent frequently collides with obstacles or be-
comestrappedwithinnarrow, obstacle-denseregions, indicatingadeficiencyinfine-grainedcolli-
sionavoidancecapabilities. (2)Long-horizonnavigation: Theagentexhibitsdifficultyintraversing
betweendistinctrooms,highlightinglimitationsinitsspatialplanningandlong-horizonnavigational
reasoning.
4.2 MULTIAGENTTASK: MULTI-AGENTCOOPERATIVESEARCH
4.2.1 BENCHMARKOVERVIEW
To facilitate research on multi-agent collaboration in complex 3D environments, we introduce the
multi-agentcooperativesearch(MACS)task. BuiltupontheTongSIMplatform,thetasksimulates
a partially observable post-flood search scenario characterized by stochastic dynamic hazards and
12

(a) (b)
Figure11: Visualizationofthemulti-agentcooperativesearch(MACS)taskscenarios. (a)Detailed
scenario view. Key entities are explicitly labeled: agents, target supplies requiring collaborative
collection, anddynamichazardsthatmustbeproactivelyevaded. Thegreenlinesemanatingfrom
the agents provide a visualization of the radial ray-casting sensor array, illustrating the localized
perception mechanism under conditions of partial observability. (b) Parallel training array: The
top view of 3 × 3 array showing concurrent execution environments utilized for scalable multi-
agenttraining. Thebluedottedcircumferencesdelineatethemaximumsensorydetectionrangefor
individualagentswithinthecomplexenvironment.
staticobstacles, asshowninFigure11. Thecorechallengeliesinevaluatingtheagents’abilityto
achievethefollowingobjectivesunderconditionsofpartialobservability:
• Collaboration: Agents must collaborate to collect supplies that require multi-agent ma-
nipulation.
• SafetyConstraints: Agentsarerequiredtoproactivelyidentifyandevadehazardousma-
terialsmovingrandomlywithintheenvironment.
• Efficient Navigation: Relying solely on local sensory data, agents must plan energy-
efficient,optimalpathsthroughcomplex,dynamicenvironments.
Fundamentally, MACS serves as a robust experimental platform for the training and evaluation
of state-of-the-art multi-agent reinforcement learning (MARL) algorithms. Technically, the envi-
ronment is formulated with a continuous 2-dimensional action space (Box(−1.0,1.0)) governing
agents’ movements, and a high-dimensional observation space constructed from a radial array of
sensorsthatcapturetherelativedistance,orientation,andvelocityofsurroundingentities. Further-
more,toaccommodatediverseexperimentalrequirements,theenvironmentfeatureshighconfigura-
bility. ThekeyparametersandtheirdefaultsettingsaredetailedinTable3.
4.2.2 BASELINE
To validate the efficacy of the proposed benchmark and establish a reference for future research,
we evaluate two representative MARL algorithms. These baselines span from fully decentralized
approachestocentralizedtrainingparadigms. (1)IndependentPPO(IPPO)[14]: Afullydecentral-
izedalgorithmwhereeachagentlearnsanindependentpolicybasedsolelyonitslocalobservation,
ignoringthejointstateinformation. (2)Multi-AgentPPO(MAPPO)[56]: Awidely-adoptedalgo-
rithmfollowingthecentralizedtrainingwithdecentralizedexecution(CTDE)paradigm. Itutilizes
a centralized value function to exploit global state information during training while maintaining
decentralizedpoliciesduringexecution.
Wetrainandevaluatethesebaselinesunderthestandardenvironmentconfiguration(defaultvalues
provided in Table 3). We employ the mean episodic return per agent (R¯) as our primary metric,
definedasthetotalteamrewardnormalizedbytheagentpopulationN. Formally:
N T
R¯ = 1 (cid:88)(cid:88) r(i) (3)
N t
i=1 t=1
13

Table3: DetailedenvironmentspecificationsanddefaulthyperparametersfortheMACSTask.
Parameter Description Default
n agents Numberofrescueagents 5
n supplies Numberofvaluablesupplyitems 10
n hazards Numberofhazarditems 10
n coop Agentsrequiredforsuccessfulcooperation 2
n sensors Numberofsensorsperagent 30
sensor range Maximumsensingrange 500.0
max cycles Maximumstepsperepisode 500
supply reward Rewardforsuccessfullycollectingsupplies 10.0
hazard reward Penaltyforencounteringhazards −1.0
encounter reward Rewardfortouchingasupplywithoutcapture 0.01
thrust penalty Energycostmultiplierpermovementstep −0.01
local ratio Ratiooflocalrewardstoglobalrewards 0.9
Table4: PerformancecomparisonofbaselinealgorithmsontheMACSTask. Resultsareaveraged
overevaluationepisodes.
Method MeanStepReward MeanEpisodicReturnperAgent
MAPPO(CTDE) 0.0380 19.24
IPPO(Independent) 0.0295 14.75
Random -0.013 -6.51
wherer(i)denotestherewardreceivedbyagentiattimestept,andT representstheepisodehorizon.
t
Weadditionallyreportthemeanstepreturn,calculatedasR¯/T,whichquantifiestheaveragereward
densitypertimestep.
4.2.3 EXPERIMENTSANDRESULTS
Table4presentsthecomparativeperformanceofthebaselinealgorithms. Empiricalresultsdemon-
stratethatthecentralizedtrainingapproachsignificantlyoutperformsthefullydecentralizedmethod.
MAPPOachievesthehighestmeanepisodicreturnperagentof19.24,whereasIPPOyields14.75.
ThisperformancegapindicatesthattheCTDEparadigmeffectivelyleveragesglobalinformationto
coordinate agents in complex search tasks. Both learning-based methods significantly surpass the
Randompolicybaseline.
4.3 HUMAN-ROBOTHYBRIDTASK: ROBOTSOCIALNAVIGATION
4.3.1 BENCHMARKOVERVIEW
Autonomous robots represent the quintessential manifestation of embodied intelligence within the
physical world. In the era of human-robot symbiosis, achieving safe and efficient human-centric
interaction within large-scale, dynamic, and unstructured environments has emerged as a pivotal
scientificchallengeinthefieldsofAGIandrobotics. Toadvanceresearchinthisdomain,complex
open-world testing environments such as Virtual Community [63] and SimWorld [55] have been
developed. These platforms facilitate the evaluation of intelligent behaviors of embodied agents
withincomplexsocialscenarios,rangingfromautonomouslynavigatingintersectionscharacterized
by mixed pedestrian-vehicle traffic to assisting human agents in task execution. However, Virtual
Community is limited to supporting a maximum concurrency of 15-25 human agents and robots
withinasinglescene.Conversely,whileSimWorldaccommodatesalargerpopulation,itsnavigation
reliesonpredefineddiscretewaypoints,therebyfailingtosimulatethecontinuouscrowddynamics
requiredforrigorouslyevaluatingtheperformanceofrealisticautonomousrobots.
Leveraging TongSIM’s comprehensive asset library and robust control API, we employ the social
forcemodel(SFM)tosimulatehigh-fidelity,dynamiccrowdbehaviors.Thesystemensuresstability
for simulations involving over 100 concurrent pedestrians. Virtual robots feature standard ROS2
14

Figure12: Overviewoftherobotsocialnavigationtaskindynamicsocialscenarios.
integration,allowingforseamlessinteroperabilitywiththebroaderroboticecosystem.Furthermore,
thesystemsupportshumanteleoperationofvirtualavatarsviaVR,enablingsubjectiveexperience
analysisandinteractionevaluation.
Withinanurbanstreet-levelenvironment,wehavedesignedafundamentalsocialnavigationbench-
markingtask. Thistaskrequiresarobottonavigatetoadesignatedtargetlocationinsideahighly
dynamiccrowd, characterizedbyrandomlygeneratedagentsexhibitingdiversemotionprimitives.
Thisbenchmarkaimstoevaluatetherobot’sperception,planning,andsocialcognitivecapabilities
within complex social settings, thereby providing a reproducible platform for research in human-
robotinteraction(HRI).Figure12showsanoverviewofthisbenchmark.
Therobotistaskedwithnavigatingtoadesignatedtargetlocationwithinaspecifiedtimelimitwhile
traversingacomplexenvironment. Thecoreobjectiveistogeneratecollision-freetrajectoriesthat
strictly adhere to proxemic constraints (i.e., maintaining appropriate social distances from pedes-
trians). Thistaskservesasabenchmarktorigorouslyevaluatetheautonomousagent’sperceptual
robustness, motion planning efficiency, and social compliance (cognitive understanding of social
norms)indynamic,populatedsettings.
Therobotperceivestheenvironmentthroughamulti-modalsensorsuite,including:1)RGB-Dcam-
era,2)3DLiDAR,and3)GPSmodule. Thedecisionmoduleoutputscontinuouscontrolcommands
viathestandardROSinterface.
4.3.2 BASELINEANDMETRICS
Baseline. To evaluate performance, we compare the following decision-making approaches. (1)
Human Teleoperation: Expert baseline via manual keyboard control. (2) Hierarchical planner
(DWA)[19]: A*globalplanner[20]+DynamicWindowApproach(DWA)localreactivecontroller.
(3) Hierarchical planner (MPPI)[51]: A* global planner + Model Predictive Path Integral (MPPI)
sampling-basedlocaloptimizer.
EvaluationMetrics. Weemployacomprehensivesetofmetricstoquantitativelyevaluateperfor-
mance. The evaluation module operates as a background process with a sampling frequency of 2
Hz.
• Efficiency(EFF):Measuresthetimeefficiencyofthenavigationtaskbasedontheactual
completion time (T ), normalized by the theoretical minimum time (T ) and the
actual min
maximumallottedtime(T ). Itiscalculatedas:
max
T −T
EFF=1− actual min (4)
T −T
max min
• SuccessRate(SRT):Theratioofsuccessfullycompletedepisodestothetotalnumberof
experimentaltrials.
15

• Safety(SAF):Adiscretescoringmetricreflectingcollisionfrequency. Weassignascore
of1.0forzerocollisions,0.5for1–3collisions,and0.0formorethan3collisions.
• SocialNormCompliance(SNC):quantifiesthepercentageoftasktimeduringwhichthe
robot intrudes into a human’s personal space, distinguishing Type-1 intrusions (distance
d<0.45m)andType-2intrusions(distance0.45m≤d≤1.2m).
• TotalScore: Aweightedaggregatescorequantifyingoverallperformance:
Total=100×(0.2·EFF+0.2·SRT+0.3·SAF+0.3·SNC) (5)
4.3.3 EXPERIMENTSANDRESULTS
Table 5: Performance comparison of baseline methods in the crowded intersection crossing task.
The test environment consists of a circular area (r = 20m) populated with 30 randomly moving
pedestrians,withaminimumstart-to-goaldistanceof40m.
Baseline Robot EFF SRT SAF SNC Total
HumanTeleoperation UnitreeGo2 0.89 1.0 0.95 0.88 92.7
A∗+DWA UnitreeGo2 0.42 0.1 0 0 10.4
A∗+MPPI UnitreeGo2 0.73 0.6 0.25 0.31 43.1
AspresentedinTable5, thereisamarkeddisparityinperformanceacrosstheevaluateddecision-
making baselines within the fundamental social navigation task. Human Teleoperation achieved
superiorperformanceacrossallfourmetrics(TotalScore=92.7),underscoringthehumancapacity
to leverage contextual reasoning and social cognition for high-quality navigation amidst complex
crowddynamics. Instarkcontrast,globalA∗withlocalDWAplannerexhibitedinstabilityinhighly
dynamicscenarios,recordinganexceptionallylowsuccessrate(SRT=0.1). Themethodsuffered
fromfrequentcollisionsandseverespatialintrusions,resultinginzeroscoresforbothsafety(SAF)
and social norm compliance (SNC), yielding a total score of only 10.4. This highlights the inad-
equacy of local planners relying solely on geometric constraints when confronting the stochastic
natureofmulti-agentbehaviors. WhileglobalA∗ withlocalMPPIplannerdemonstratedimprove-
mentsinefficiencyandsuccessratesthroughsampling-basedoptimization(achievingmoderateper-
formanceinsafetyandsocialcompliance,andtotalscore=43.1)itstillfallssignificantlyshortof
humanbenchmarks. Thisperformancegapindicatesthattraditionalplanningframeworks, lacking
socialbehavioralunderstanding,struggletoadapttodensecrowdinteractions.
The quantitative experimental results validate a core conclusion: in complex, dynamic social en-
vironments, the absence of social contextual reasoning and normative cognition causes traditional
autonomousplanningmethodstosystematicallylagbehindhumanperformanceintermsofsafety,
success rate, and social compliance. Embodied agents relying exclusively on geometric obstacle
avoidance or local optimization cannot achieve reliable and socially normative interactive behav-
iors. This critical limitation emphasizes the necessity of integrating models endowed with social
cognitivecapabilities.
4.4 PRIMARYCOMPOSITETASKS: HOUSEHOLDBENCHMARKINGTEST
4.4.1 BENCHMARKOVERVIEW
Recentadvancementsinmultimodallargelanguagemodels(MLLMs)havesignificantlyenhanced
AIcapabilitiesinperceptionandlinguisticcomprehension.However,existingbenchmarks(e.g.,Im-
ageNet[16],COCO[26],VQA[3])predominantlyfocusonisolated,domain-specifictasks. These
benchmarks suffer from limitations regarding hyperspecialization and susceptibility to overfitting,
making them insufficient for comprehensively gauging a model’s capabilities in open-ended, dy-
namicreal-worldenvironments—competenciesessentialfortheprogressiontowardsAGI.Although
multi-taskplatformslikeMMBench[27]offermultidimensionaltesting,theygenerallylackembod-
iedinteractioncapabilities,failingtoevaluatemodelreasoningandactionexecutionwithinphysical
andsocialcontexts.
Toaddressthiscriticallimitation,weproposeanovelevaluationparadigm: anembodiedcomposite
task benchmark situated in everyday household environments and drawing inspiration from early
16

Figure13: Overviewoftheprimaryfamilycompositetasksbenchmark.
childhooddevelopmentalpsychology,asshowninFigure13. Thecoreobjectiveofthisbenchmark
is to evaluate how MLLM agents integrate perception, reasoning, and action to accomplish com-
positetasksrequiringsynergisticcapabilities,therebyprovidingamorerealisticassessmentoftheir
generalintelligence.
4.4.2 TESTPROCEDURE
Focusingoncompositetaskscenariosfrequentinhouseholdsettings,wedesignedanevaluationset
comprisingeighttasktypes,categorizedintothreecoredomains:
• ObjectUnderstanding: Includingobjectcountingandgiftselection.
• SpatialIntelligence:Includingblockconstruction,puzzlesolving,andunderstandingbut-
tonfunctionality.
• SocialActivity: Includingtablesetting,roomorganization,andluggagepreparation.
Weconstructhigh-fidelity3DvirtualhomeenvironmentswithintheTongSIMsimulationplatformto
serveasatestbedformodelevaluation. Leveragingpromptengineering,weencapsulatethetarget
models into agents capable of executing tasks within these embodied interactive settings. Conse-
quently, we establish a standardized perception-reasoning-action loop framework for the MLLMs
underassessment:
• Perception: At each time step, the agent receives observational data from the environ-
ment,comprisingmulti-viewRGBimagesandJSONscenedescriptionscontainingobject
attributes(e.g.,name,color,position).
• ReasoningandDecision-Making: Basedonobservationaldataandnaturallanguagetask
goals, the MLLM employs a ReAct-style reasoning process to output a natural language
reasoningtraceandanexecutablesequenceofAPIcalls.
• Action: ThesystemexecutestheAPIcallsequence(e.g.,MoveToObject,PickUp),which
encompasses both atomic and high-level actions, thereby driving the virtual character to
interactwiththeenvironment.
• Loop: Thisprocessiteratesuntilthetaskiscompletedoratimeoutoccurs.
Todirectlyassesstheintrinsiccapabilitiesofthemodels,wedidnotperformretrainingorintroduce
external augmentation modules; instead, we encapsulated the MLLMs as embodied agents solely
throughcarefullydesignedprompts.
17

4.4.3 EXPERIMENTSANDRESULTS
We conducted a systematic evaluation of 17 proprietary and open-source MLLMs (including the
GPT,Gemini,Claude,andLlamaseries). Theprimaryresultsareasfollows:
• OverallSuboptimalPerformance: Averagescoresacrossallmodelsoncompositetasks
were universally low. The top-performing model, Gemini-2.5-Pro, achieved an aver-
age score of merely 24.53/100. This indicates a substantial gap between state-of-the-art
MLLMsandtherequirementsforhandlingreal-worldembodiedtasks.
• Proprietaryvs. Open-SourceModels:Whileproprietarymodelsgenerallyoutperformed
open-source counterparts, the margin was not overwhelming. The best-performing open-
sourcemodelwasLlama-4-Maverick,withascoreof14.48.
• Domain-SpecificAnalysis: (1)ObjectUnderstandingprovedtobetherelativestrengthof
themodels;forinstance,GPT-5achievedascoreof69.06inthe“GiftSelection”task.This
suggeststhatcurrentmodelspossesscertainadvantagesinperceptionandbasicclassifica-
tiontasks. (2)SpatialIntelligenceemergedasthemostchallengingdomain, withmodels
scoringextremelylowontaskssuchasblockconstructionandpuzzlesolving. Thisiden-
tifiesspatialreasoning,physicalunderstanding,andmanipulationplanningastheweakest
linksincurrentMLLMs. (3)SocialActivityperformancewasinconsistent,withdifferent
models leading in different tasks; however, even the highest scores hovered in the 20-30
range. This reflects difficulties in comprehending complex social contexts and executing
goal-orientedactions.
Experimentalresults,showninTable6,demonstratethatwhilecurrentMLLMshavemadesignif-
icant strides in perception and language tasks, their architectures, training mechanisms, and mul-
timodalfusionstrategiesremaininsufficienttosupportthecompositecapabilitiesrequiredforem-
bodiedtasks. Futureresearchmustprioritizethein-depthdevelopmentofembodiedreasoning,spa-
tialintelligence, andsocialunderstanding. Thebenchmarkproposedinthisworkservesas avital
evaluationtoolandprovidesdirectionalguidanceforadvancingMLLMstowardgeneralembodied
intelligence.
4.5 ADVANCEDCOMPOSITETASKS: SPATIALLYSITUATEDSOCIALINTELLIGENCETEST
4.5.1 BENCHMARKOVERVIEW
The integration of embodied agents into human environments demands embodied social intelli-
gence: reasoning over both social norms and physical constraints. However, existing evaluations
fail to address this integration, as they are limited to either disembodied social reasoning (e.g., in
text)orsocially-agnosticphysicaltasks.Bothapproachesfailtoassessanagent’sabilitytointegrate
andtradeoffbothphysicalandsocialconstraintswithinarealistic,embodiedcontext.
Table6: Modelperformancecomparisonontheprimaryfamilycompositetasksbenchmark.
ObjectUnderstanding SpatialIntelligence SocialActivity
Model Counting Selecting Building Jigsaw Understanding Setting TidyingUp Preparing Mean
Objects Gifts Blocks Puzzle Buttons Tables Rooms Baggage
Gemini-2.5-Pro 48.00 68.06 10.00 5.05 3.33 26.68 22.77 12.38 24.53
Gemini-2.5-Flash 42.00 68.20 5.50 5.30 3.33 25.83 23.22 11.05 23.05
o3 54.00 65.92 10.00 6.40 3.33 14.31 18.77 10.30 22.88
GPT-5 36.00 69.06 3.75 6.03 3.33 28.68 16.00 9.50 21.54
Claude-3.7-Sonnet 46.00 59.74 8.88 6.28 0.00 23.76 16.12 3.40 20.52
Claude-4-Sonnet 44.00 65.44 8.75 6.03 0.00 19.81 14.85 5.18 20.51
Doubao-1.5-vision-pro 36.00 56.70 12.50 6.88 5.00 24.17 4.22 7.75 19.15
Claude-3.5-Sonnet 42.00 64.24 8.00 4.50 0.00 12.33 13.47 6.00 18.82
Grok3 52.00 50.24 9.88 8.00 0.00 8.37 17.20 3.35 18.63
o4-mini 38.00 66.40 0.00 6.62 3.33 13.67 1.52 4.23 16.72
GPT-4o 32.00 46.30 10.00 7.08 3.33 18.42 6.30 8.18 16.45
GPT-4o-mini 34.00 54.96 5.75 7.05 1.67 19.07 1.50 3.75 15.97
Qwen-VL-max 44.00 48.14 0.00 7.55 0.00 15.96 1.25 0.00 14.61
Llama-4-Maverick 36.00 50.30 3.75 6.58 0.00 15.75 0.42 3.00 14.48
Llama-4-Scout 28.00 42.56 6.25 5.72 0.00 8.94 1.38 2.00 11.86
Qwen-VL-plus 6.00 34.16 0.00 7.65 0.00 16.67 1.82 0.38 8.33
Llama-3.2 6.00 6.80 0.00 4.60 0.00 4.67 0.42 0.00 2.81
18

Figure 14: A typical seat arrangement task involves a given room layout and several NPCs. The
agentundertest(T-Agent)needstointeractwiththeNPCsandexploretheroomtodeviseaseating
arrangementthatsatisfieseveryone.
To address this challenge, we introduce spatially situated social intelligence test (S3IT), a bench-
mark specifically designed to evaluate embodied social intelligence. As shown in Figure 14, it is
centered on a novel and challenging seat-ordering task, requiring an agent to arrange seating in a
3DenvironmentforagroupofLLM-drivenNPCswithdiverseidentities,preferences,andintricate
interpersonal relationships. Our procedurally extensible framework generates a vast and diverse
scenariospacewithcontrollabledifficulty,compellingtheagenttoacquirepreferencesthroughac-
tive dialogue, perceive the environment via autonomous exploration, and perform multi-objective
optimizationwithinacomplexconstraintnetwork.
Inthisbenchmark,weconstructed5sceneenvironmentswithdynamiclayoutcharacteristics,where
keyfacilities(e.g.,chairs,furniturelayouts)supportparametricconfiguration. Simultaneously,we
establishedavirtualcommunitycomprising59NPCswithindependentbackgroundsettings,andde-
finedtheirinternalcomplexfamilyandsocialrelationshipnetworks. Basedonthis,weconstructed
7,000 problems. Each problem includes one room and several NPCs; while basic information re-
mainsinvariant,weadditionallyconfiguredspecifichobbies,seatingpreferences,andconflictswith
othersforeachNPCineveryproblem.Furthermore,weassigned3-Likertpointintensities(weights)
tothesepreferencesandconflictstoenrichtheproblems.
4.5.2 BASELINESANDTESTPROCEDURE
Within this benchmark, we propose a testing framework designed to integrate LLMs. To enable
theagentsundertesttoeffectivelycomprehendandexecutetheseatingarrangementtasks,wehave
systematically designed and standardized the inputs, outputs, and prompt structures. The pipeline
comprises three phases for testing the agent that is named as “T-Agent”. In Phase I (NPC Prefer-
ence Extraction and Summarization), the T-Agent constructs detailed preference profiles for each
NPC. Then, in Phase II (Environmental Cognition ), the T-Agent needs to construct a structured
representation of the 3D environment through comprehensive exploration. Finally, in Phase III
(Multi-ConstraintDecision-Making),theT-Agentintegratesinformationfromtheprecedingphases
to generate, reflect, and iteratively refine seating solutions. To enable scalable evaluation, we in-
troduceanautomatedscoringframework. Thisframework evaluates thepreferencesatisfactionof
agent-generatedseatingplans,therebyprovidinganobjective,quantitativemetricforeachsolution.
Furthermore, to analyze the T-Agent’s capability in prioritizing based on weights, we statistically
trackeditspreferencesatisfactionbasedontheirstrengths. Wedefinetheprioritizationgap(PG)as:
PG=S −S (6)
high low
whereS denotesthesatisfyingrateofhigh-weightedpreferences,andS denotesthesatisfying
high low
rateoflow-weightedpreferences.
4.5.3 EXPERIMENTSANDRESULTS
AsshowninTable7,Gemini-2.5-proemergedastheSOTAmodel(47.8)andwasuniquelycapable
ofexceeding40onthe“EmbodiedPreference”dimension. Thesemodelsexhibitaconsistenttrend
that scores are lowest in the embodied dimension, followed by the social dimension. In contrast,
19

Table7: ModelperformancesontheS3ITbenchmark’stestset. Bestresultsareinbold. PGstands
fortheprioritizationgap.
Model Embodied Social Conflict PG Average
Gemini-2.5-pro 40.6 56.2 85.7 8.8 47.8
o3 32.9 53.8 89.0 12.7 43.1
GPT-5 29.0 56.9 86.1 15.4 42.7
o4-mini 29.0 54.5 89.5 6.8 41.4
GPT-4.1 23.3 43.2 55.4 3.8 29.3
Doubao-1.5 24.6 43.0 62.5 3.8 28.3
GPT-4o 24.6 43.0 51.7 3.3 28.2
GPT-4.1-mini 22.8 39.3 42.5 3.7 26.8
Claude-4.5 19.1 37.6 46.0 4.8 23.1
GPT-4o-mini 16.7 34.7 45.8 1.6 19.3
performanceintheconflictdimensionisgenerallystrongacrosstheboard,withsomemodelseven
demonstrating a good capacity for conflict resolution. These findings validate the hypothesis that
spatial intelligence is the cornerstone of effective embodied social reasoning. All models demon-
stratedpositivePGscores,indicatingthattheyhaveafundamentalabilitytodistinguishpreference
strengths. Higher-priority preferences are fulfilled with greater precedence. Among the evaluated
models,GPT-5,withanupdatedadaptivereasoningarchitecture,excelsatconsideringpreferences
ofvaryingintensities.
5 DISCUSSION
5.1 VARIOUSBENCHMARKS
TongSIM is established not merely as a simulation platform, but as a holistic proving ground
aimed at catalyzing agent evolution. Underpinned by a versatile suite of benchmarks, our multi-
dimensionalarchitecturalphilosophyenablesafull-spectrumdiagnosisandvalidationofagentpro-
ficiency.
First,adistinguishingfeatureofourplatformisthehierarchicalevaluationofagentcapabilities.Our
benchmarksspanacomprehensivespectrum,rangingfromlow-levelperceptionandlocomotionto
high-levelcomplextasksandsocialintelligence. Atthefoundationallevel,weassessatomicsingle-
agentcapabilities, including locomotion, steering, andbasic visualperception, whichare incorpo-
ratedintoallourproposedbenchmarks. Buildinguponthis,single-agenttasksinvolvehigher-level
assessmentssuchasobjectattributerecognition,spatialmemoryconstruction,andsemanticnaviga-
tion. Forinstance,requiringanagenttoexploreanunknownroomtolocatea“paperball”testsits
semanticunderstandingoftheenvironment. Atthehighestlevel,theplatformemphasizessociality
andcollaborativeintelligence. Thisencompasseshigh-dimensionalchallengesrangingfrommulti-
agent collaboration (e.g., the MACS task) to complex scenarios (e.g., navigation in dense crowds
andexecutionofcomplexhouseholdtasks). Thesebenchmarksaimtoadvancethedevelopmentof
agentstowardsAGIequippedwithsocialattributes.
Second, high-fidelity simulation scenarios are pivotal to bridging the Sim-to-Real gap. In con-
trast to traditional grid worlds or symbolic, low-fidelity environments, all tasks within our plat-
form are situated in photorealistic environments constructed upon advanced physics engines and
ray-tracingtechnologies. TongSIMscenariosencompasscomplexilluminationvariations,specular
reflections,shadowocclusions,andrichtexturaldetails,therebycompellingtheagents’visualsys-
tems to demonstrate robustness against real-world sensory noise. Furthermore, TongSIM features
rich physical simulation capabilities, enabling the modeling of rigid body dynamics, fluid interac-
tions, and deformable object deformations (e.g., cloth and liquids). Under such constraints, the
planning capabilities of agents can be evaluated within scenarios that closely approximate reality.
Forinstance,whengraspingacupfilledwithwater,theagentmustaccountforshiftsinthecenter
ofgravityandfriction. Thistrainingregimeensuresthatmodelparameters,upontransfertophys-
icalrobotichardware,candirectlyadapttoreal-worldphysicalconstraints,significantlymitigating
20

the costs associated with fine-tuning. Although this paper does not go into detail about this fea-
ture,theexperimentaldevelopmentworkhasbeenbasicallycompleted,whichwillbeintroducedin
subsequentwork.
WeprioritizeagentgeneralizabilityandarededicatedtothepursuitofAGI;accordingly,TongSIMis
engineeredtosupportmassive,large-scaletaskstofacilitatethisobjective. Topreventagentsfrom
overfitting to specific spatial configurations, the platform is designed to enable large-scale scene
generation. Leveragingproceduralgeneration,wecansynthesizethousandsofindoorenvironments
featuring diverse layouts and stylistic variations. This diversity ensures that agents acquire gener-
alizedinteractionlogic(e.g.,understandingtheaffordancethatadoorrequirespushingorpulling)
rather than relying on the rote memorization of map coordinates. An extensive suite of additional
benchmarkswillbeprogressivelyreleasedtotheresearchcommunity.
5.2 POTENTIALAPPLICATIONS
In light of our ultimate objective to achieve AGI, the inception and architectural design of this
platformareintrinsicallyalignedwiththisvision.Ratherthanmerelysupplyingdatasets,weprovide
aholisticecosystemdesignedtoincubatehigh-levelintelligence.
TongSIM offers users an exceptional degree of freedom and extensibility, thereby broadening its
multidisciplinaryapplicationhorizons:
• PlanninginSymbolicSpace: Researcherscanleveragehigh-levelAPIstofocusontask
decomposition,causalreasoning,andtheapplicationofknowledgegraphs,withoutbeing
encumberedbylow-levelcontroldynamics.
• End-to-End Embodied Control: Researchers in reinforcement learning and imitation
learningcanutilizethecomprehensiveinterfacesandrichenvironmentaldata(e.g.,RGB-D
images,semanticobjectlabels)totrainend-to-endneuralnetworks.
• Verification of Hybrid Architectures: The platform facilitates the validation of “LLM-
Brain+Controller-Cerebellum”hybridarchitectures.Forinstance,userscanemployLLMs
forhigh-levelstrategicplanningwhileinvokinglow-levelmotionprimitivestoexecutespe-
cificoperations.
Totranscendthelimitationsoftraditionalplatformsrestrictedtofixedtasks,weprovidestandardized
Python/C++APIs,diversevirtualavatars,andextensivefunctionalcapabilities. Thesetoolsenable
userstorapidlyconstructcustomtasks:
• DomesticServiceScenarios: Userscandefinea“roomtidying”task,requiringtheagent
toidentifydebrisonthefloor,classifyitems,andplacethemintostoragecontainers.
• OperationsinExtremeEnvironments:Simulatingpost-fireruinscenariostotrainagents
in Search and Rescue and hazardous material removal, testing their robustness within
chaoticenvironments.
• Human-Robot Interaction: Configuring NPCs with social attributes to train agents in
comprehending human gestures and gaze intent, as well as engaging in natural language
dialogue.
Thesetasksarenotconfinedtotheplatform’spresetbenchmarks;researcherscanrapidlyconstruct
experimentalenvironmentstailoredtotheirspecificscientifichypotheses,therebysignificantlyen-
hancingiterationefficiency.
5.3 FUTUREWORKS
Currently,theplatformisundergoingiterativedevelopment. Wearecommittedtoprogressivelyre-
fining both indoor and outdoor environments, expanding the benchmark suite, and releasing these
contributionstotheopen-sourcecommunity.Regardingenvironmentalexpansion,whileourcurrent
focuslieswithincomplexindoordomesticenvironments,weareactivelyconstructinganexpansive
world model. Future iterations will extend into outdoor scenarios, enriching supported interac-
tionsandsemanticannotations. Thisincludesthesimulationofurbanstreetinteractions,crowdand
traffic network dynamics, unstructured natural terrains (e.g., forests, mountains), and specialized
21

outdoor zones (e.g., industrial complexes). These developments are poised to support research in
autonomousdriving, logisticsdistribution, andfieldexplorationrobotics. Furthermore, weplanto
enhance the temporal and environmental dynamics of the simulator. Future scenes will transcend
static snapshots by incorporating diurnal cycles, meteorological variations (e.g., rain, fog, snow),
and dynamic obstacles (e.g., pedestrians, vehicles), thereby approximating the stochasticity and
complexityoftherealworld.
The future of embodied AI is inextricably linked to human cognitive guidance and cross-reality
interaction. The emerging paradigm of symmetrical reality [60, 58], utilizing human-in-the-loop
methodologiesacrossphysicalandvirtualworlds,grantsagentsdirectexposuretodatadistributions
ofhybridenvironments,fosteringrobusttrainingforextensibletasks.
Through theseendeavors, we envisionthis platform notmerely as atesting tool, butas a stepping
stonetowardafutureofhuman-machinesymbiosis,contributingsubstantivemomentumtothereal-
izationofAGIendowedwithcomprehensiveperception,reasoning,andactuationcapabilities.
6 CONCLUSIONS
This paper formally introduces TongSIM, a universal training and evaluation platform for embod-
ied AI designed to bridge the simulation-to-reality gap through high-fidelity simulation technolo-
gies. TongSIMestablishesanexpansiveworldfeaturing115meticulouslycraftedinteractiveindoor
scenesandlarge-scalecontinuousurbanenvironments,andprovideshighlychallengingmultimodal
sensory inputs to agents. Leveraging high-fidelity physics simulation, native parallel training sup-
port,anddiverseagentdrivingmodalities,TongSIMestablishesataskspectrumthatsurpassesex-
istingplatforms.
Wedesignandimplementfivebenchmarkcategorieswithinthe3Dinteractiveenvironments,cover-
ingsingle-agentautonomousnavigation,multi-agentcooperation,socialnavigationinhuman-robot
hybrid environments, and both basic and advanced household service tasks. Extensive empirical
evaluationsrevealthatwhileagentsdrivenbyreinforcementlearningandMLLMsexcelinspecific
tasks,theyexhibitsignificantdeficienciesinlong-horizonplanning,complexspatialreasoning,and
adherencetosocialnorms.
Tofostercommunitydevelopment, wereleaseTongSIMasanopen-sourceplatform. Weenvision
this infrastructure serving as a catalyst for general embodied intelligence research, empowering
both academia and industry to cultivate next-generation agents capable of robust perception, deep
reasoning,andefficientcooperationwithinopenanddynamicenvironments.
REFERENCES
[1] M.Ahn,A.Brohan,N.Brown,Y.Chebotar,O.Cortes,B.David,C.Finn,C.Fu,K.Gopalakr-
ishnan,K.Hausman,etal.Doasican,notasisay:Groundinglanguageinroboticaffordances.
arXivpreprintarXiv:2204.01691,2022.
[2] P. Anderson, Q. Wu, D. Teney, J. Bruce, M. Johnson, N. Su¨nderhauf, I. Reid, S. Gould, and
A.VanDenHengel. Vision-and-languagenavigation: Interpretingvisually-groundednaviga-
tion instructions in real environments. In Proceedings of the IEEE conference on computer
visionandpatternrecognition,pages3674–3683,2018.
[3] S.Antol,A.Agrawal,J.Lu,M.Mitchell,D.Batra,C.L.Zitnick,andD.Parikh. Vqa: Visual
questionanswering.InProceedingsoftheIEEEInternationalConferenceonComputerVision,
pages2425–2433,2015.
[4] G. Authors. Genesis: A generative and universal physics engine for robotics and beyond,
December2024.
[5] S.Bailis,J.Friedhoff,andF.Chen. Werewolfarena: Acasestudyinllmevaluationviasocial
deduction. arXivpreprintarXiv:2407.13943,2024.
[6] A. Bhattacharjee, Y. Zeng, S. Y. Xu, D. Kulzhabayeva, M. Ma, R. Kornfield, S. I. Ahmed,
A. Mariakakis, M. P. Czerwinski, A. Kuzminykh, et al. Understanding the role of large lan-
guagemodelsinpersonalizingandscaffoldingstrategiestocombatacademicprocrastination.
22

InProceedingsofthe2024CHIConferenceonHumanFactorsinComputingSystems,pages
1–18,2024.
[7] W.Bu,Y.Wu,Q.Yu,M.Gao,B.Miao,Z.Zhang,K.Pan,Y.Li,M.Li,W.Ji,etal.Whatlimits
virtualagentapplication? omnibench: Ascalablemulti-dimensionalbenchmarkforessential
virtualagentcapabilities. arXivpreprintarXiv:2506.08933,2025.
[8] M. Cai, X. Chen, Y. An, J. Zhang, X. Wang, W. Xu, W. Zhang, and T. Liu. Cookbench: A
long-horizon embodied planning benchmark for complex cooking scenarios. arXiv preprint
arXiv:2508.03232,2025.
[9] A.Chang, A.Dai, T.Funkhouser, M.Halber, M.Niessner, M.Savva, S.Song, A.Zeng, and
Y. Zhang. Matterport3d: Learning from rgb-d data in indoor environments. arXiv preprint
arXiv:1709.06158,2017.
[10] Z.Chu,S.Wang,J.Xie,T.Zhu,Y.Yan,J.Ye,A.Zhong,X.Hu,J.Liang,P.S.Yu,etal. Llm
agentsforeducation: Advancesandapplications. arXivpreprintarXiv:2503.11733,2025.
[11] D.-M.Co´rdova-Esparza. Ai-powerededucationalagents: Opportunities,innovations,andeth-
icalchallenges. Information,16(6):469,2025.
[12] M.Cordts,M.Omran,S.Ramos,T.Rehfeld,M.Enzweiler,R.Benenson,U.Franke,S.Roth,
andB.Schiele.Thecityscapesdatasetforsemanticurbansceneunderstanding.InProceedings
oftheIEEEConferenceonComputerVisionandPatternRecognition(CVPR),June2016.
[13] S.Cui,X.He,J.Han,Z.Zhang,andY.Peng. Abilitydecompositionanddifficultyquantifica-
tionofvisualtasks: Towardssystematicevaluationsofartificialgeneralintelligence. Science
ChinaTechnologicalSciences,68,2025.
[14] C.S.DeWitt,T.Gupta,D.Makoviichuk,V.Makoviychuk,P.H.Torr,M.Sun,andS.White-
son.Isindependentlearningallyouneedinthestarcraftmulti-agentchallenge? arXivpreprint
arXiv:2011.09533,2020.
[15] M. Deitke, E. VanderBilt, A. Herrasti, L. Weihs, K. Ehsani, J. Salvador, W. Han, E. Kolve,
A.Kembhavi,andR.Mottaghi. Procthor: Large-scaleembodiedaiusingproceduralgenera-
tion. AdvancesinNeuralInformationProcessingSystems,35:5982–5994,2022.
[16] J.Deng,W.Dong,R.Socher,L.-J.Li,K.Li,andL.Fei-Fei. Imagenet: Alarge-scalehierar-
chicalimagedatabase. InProceedingsoftheIEEEconferenceoncomputervisionandpattern
recognition,pages248–255.Ieee,2009.
[17] G. Dulac-Arnold, N. Levine, D. J. Mankowitz, J. Li, C. Paduraru, S. Gowal, and T. Hester.
Challenges of real-world reinforcement learning: definitions, benchmarks and analysis. Ma-
chineLearning,110(9):2419–2468,2021.
[18] K. Fang, P. Yin, A. Nair, H. R. Walke, G. Yan, and S. Levine. Generalization with lossy
affordances: Leveraging broad offline data for learning visuomotor tasks. In Conference on
RobotLearning,pages106–117.PMLR,2023.
[19] D. Fox, W. Burgard, and S. Thrun. The dynamic window approach to collision avoidance.
IEEERobotics&AutomationMagazine,4(1):23–33,1997.
[20] P. E. Hart, N. J. Nilsson, and B. Raphael. A formal basis for the heuristic determination of
minimumcostpaths. IEEETransactionsonSystemsScienceandCybernetics,4(2):100–107,
1968.
[21] Y. Hong, Z. Zheng, P. Chen, Y. Wang, J. Li, and C. Gan. Multiply: A multisensory object-
centricembodiedlargelanguagemodelin3dworld. InProceedingsoftheIEEE/CVFConfer-
enceonComputerVisionandPatternRecognition,pages26406–26416,2024.
[22] E. Kolve, R. Mottaghi, W. Han, E. VanderBilt, L. Weihs, A. Herrasti, M. Deitke, K. Ehsani,
D.Gordon,Y.Zhu,etal. Ai2-thor: Aninteractive3denvironmentforvisualai. arXivpreprint
arXiv:1712.05474,2017.
23

[23] C.Li,F.Xia,R.Mart´ın-Mart´ın,M.Lingelbach,S.Srivastava,B.Shen,K.Vainio,C.Gokmen,
G.Dharan,T.Jain,etal. igibson2.0: Object-centricsimulationforrobotlearningofeveryday
householdtasks. arXivpreprintarXiv:2108.03272,2021.
[24] C.Li,R.Zhang,J.Wong,C.Gokmen,S.Srivastava,R.Mart´ın-Mart´ın,C.Wang,G.Levine,
M. Lingelbach, J. Sun, M. Anvari, M. Hwang, M. Sharma, A. Aydin, D. Bansal, S. Hunter,
K.-Y.Kim,A.Lou,C.R.Matthews,I.Villa-Renteria,J.H.Tang,C.Tang,F.Xia,S.Savarese,
H.Gweon,K.Liu,J.Wu,andL.Fei-Fei.BEHAVIOR-1k:AbenchmarkforembodiedAIwith
1,000everydayactivitiesandrealisticsimulation.InProceedingsofthe6thAnnualConference
onRobotLearning,2022.
[25] H.Li,Y.Wang,andH.Qu.Wherearewesofar?understandingdatastorytellingtoolsfromthe
perspectiveofhuman-aicollaboration. InProceedingsofthe2024CHIConferenceonHuman
FactorsinComputingSystems,pages1–19,2024.
[26] T.-Y.Lin,M.Maire,S.Belongie,J.Hays,P.Perona,D.Ramanan,P.Dolla´r,andC.L.Zitnick.
Microsoft coco: Common objects in context. In European Conference on Computer Vision,
pages740–755.Springer,2014.
[27] Y.Liu,H.Duan,Y.Zhang,B.Li,S.Zhang,W.Zhao,Y.Yuan,J.Wang,C.He,Z.Liu,etal.
Mmbench: Is your multi-modal model an all-around player? In European Conference on
ComputerVision,pages216–233.Springer,2024.
[28] V.Makoviychuk,L.Wawrzyniak,Y.Guo,M.Lu,K.Storey,M.Macklin,D.Hoeller,N.Rudin,
A.Allshire,A.Handa,etal. Isaacgym: Highperformancegpu-basedphysicssimulationfor
robotlearning. arXivpreprintarXiv:2108.10470,2021.
[29] L.MeinckeandC.Terwiesch.Reimaginingcustomerservicejourneyswithllms:Aframework
forchatbotdesignandworkflowintegration. 2025.
[30] J.S.Park,J.O’Brien,C.J.Cai,M.R.Morris,P.Liang,andM.S.Bernstein.Generativeagents:
Interactivesimulacraofhumanbehavior. InProceedingsofthe36thannualacmsymposium
onuserinterfacesoftwareandtechnology,pages1–22,2023.
[31] Y.Peng,J.Han,Z.Zhang,L.Fan,T.Liu,S.Qi,X.Feng,Y.Ma,Y.Wang,andS.-C.Zhu. The
tong test: Evaluating artificial general intelligence through dynamic embodied physical and
socialinteractions. Engineering,34:12–22,2024.
[32] X.Puig,K.Ra,M.Boben,J.Li,T.Wang,S.Fidler,andA.Torralba. Virtualhome: Simulating
householdactivitiesviaprograms. InProceedingsoftheIEEEconferenceoncomputervision
andpatternrecognition,pages8494–8502,2018.
[33] X. Puig, T. Shu, S. Li, Z. Wang, Y.-H. Liao, J. B. Tenenbaum, S. Fidler, and A. Torralba.
Watch-and-help:Achallengeforsocialperceptionandhuman-aicollaboration. arXivpreprint
arXiv:2010.09890,2020.
[34] X.Puig,E.Undersander,A.Szot,M.D.Cote,T.-Y.Yang,R.Partsey,R.Desai,A.W.Clegg,
M.Hlavac, S.Y.Min, etal. Habitat3.0: Aco-habitatforhumans, avatarsandrobots. arXiv
preprintarXiv:2310.13724,2023.
[35] S.Rao,W.Xu,M.Xu,J.Leandro,K.Lobb,G.DesGarennes,C.Brockett,andB.Dolan. Col-
laborativequestcompletionwithllm-drivennon-playercharactersinminecraft. arXivpreprint
arXiv:2407.03460,2024.
[36] N.Roy,I.Posner,T.Barfoot,P.Beaudoin,Y.Bengio,J.Bohg,O.Brock,I.Depatie,D.Fox,
D. Koditschek, et al. From machine learning to robotics: Challenges and opportunities for
embodiedintelligence. arXivpreprintarXiv:2110.15245,2021.
[37] M. Savva, A. X. Chang, A. Dosovitskiy, T. Funkhouser, and V. Koltun. Minos: Multimodal
indoor simulator for navigation in complex environments. arXiv preprint arXiv:1712.03931,
2017.
24

[38] M.Savva,A.Kadian,O.Maksymets,Y.Zhao,E.Wijmans,B.Jain,J.Straub,J.Liu,V.Koltun,
J.Malik,etal. Habitat:Aplatformforembodiedairesearch. InProceedingsoftheIEEE/CVF
internationalconferenceoncomputervision,pages9339–9347,2019.
[39] J.Schulman,F.Wolski,P.Dhariwal,A.Radford,andO.Klimov.Proximalpolicyoptimization
algorithms. arXivpreprintarXiv:1707.06347,2017.
[40] Y.Seo,D.Hafner,H.Liu,F.Liu,S.James,K.Lee,andP.Abbeel. Maskedworldmodelsfor
visualcontrol. InConferenceonRobotLearning,pages1332–1344.PMLR,2023.
[41] H. Shakeri, C. Neustaedter, and S. DiPaola. Saga: Collaborative storytelling with gpt-3. In
Companion Publication of the 2021 Conference on Computer Supported Cooperative Work
andSocialComputing,pages163–166,2021.
[42] J.Shi,J.Li,Q.Ma,Z.Yang,H.Ma,andL.Li. Chops: Chatwithcustomerprofilesystemsfor
customerservicewithllms. arXivpreprintarXiv:2404.01343,2024.
[43] M. Shridhar, J. Thomason, D. Gordon, Y. Bisk, W. Han, R. Mottaghi, L. Zettlemoyer, and
D. Fox. Alfred: A benchmark for interpreting grounded instructions for everyday tasks. In
ProceedingsoftheIEEE/CVFconferenceoncomputervisionandpatternrecognition, pages
10740–10749,2020.
[44] M.Shridhar,X.Yuan,M.-A.Coˆte´,Y.Bisk,A.Trischler,andM.Hausknecht.Alfworld:Align-
ingtextandembodiedenvironmentsforinteractivelearning.arXivpreprintarXiv:2010.03768,
2020.
[45] S.SinhaandY.M.Lee. Challengeswithdevelopinganddeployingaimodelsandapplications
inindustrialsystems. DiscoverArtificialIntelligence,4(1):55,2024.
[46] A.Szot,A.Clegg,E.Undersander,E.Wijmans,Y.Zhao,J.Turner,N.Maestre,M.Mukadam,
D. S. Chaplot, O. Maksymets, et al. Habitat 2.0: Training home assistants to rearrange their
habitat. Advancesinneuralinformationprocessingsystems,34:251–266,2021.
[47] X. Tang, J. Li, Y. Liang, S.-c. Zhu, M. Zhang, and Z. Zheng. Mars: Situated inductive rea-
soning in an open-world environment. Advances in Neural Information Processing Systems,
37:17830–17869,2024.
[48] E. Todorov, T. Erez, and Y. Tassa. Mujoco: A physics engine for model-based control. In
Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems,
pages5026–5033.IEEE,2012.
[49] H.Wang,J.Chen,W.Huang,Q.Ben,T.Wang,B.Mi,T.Huang,S.Zhao,Y.Chen,S.Yang,
et al. Grutopia: Dream general robots in a city at scale. arXiv preprint arXiv:2407.10943,
2024.
[50] Y.Wang,Z.Xian,F.Chen,T.-H.Wang,Y.Wang,K.Fragkiadaki,Z.Erickson,D.Held,and
C.Gan.Robogen:Towardsunleashinginfinitedataforautomatedrobotlearningviagenerative
simulation. arXivpreprintarXiv:2311.01455,2023.
[51] G. Williams, A. Aldrich, and E. Theodorou. Model predictive path integral control using
covariancevariableimportancesampling. arXivpreprintarXiv:1509.01149,2015.
[52] F. Xia, W. B. Shen, C. Li, P. Kasimbeg, M. E. Tchapmi, A. Toshev, R. Mart´ın-Mart´ın, and
S.Savarese.Interactivegibsonbenchmark:Abenchmarkforinteractivenavigationincluttered
environments. IEEERoboticsandAutomationLetters,5(2):713–720,2020.
[53] F. Xiang, Y. Qin, K. Mo, Y. Xia, H. Zhu, F. Liu, M. Liu, H. Jiang, Y. Yuan, H. Wang, et al.
Sapien: A simulated part-based interactive environment. In Proceedings of the IEEE/CVF
conferenceoncomputervisionandpatternrecognition,pages11097–11107,2020.
[54] X.Xie,H.Liu,Z.Zhang,Y.Qiu,F.Gao,S.Qi,Y.Zhu,andS.-C.Zhu.Vrgym:Avirtualtestbed
for physical and interactive ai. In Proceedings of the ACM Turing Celebration Conference-
China,pages1–6,2019.
25

[55] X.Ye,J.Ren,Y.Zhuang,X.He,Y.Liang,Y.Yang,M.Dogra,X.Zhong,E.Liu,K.Benavente,
et al. Simworld: An open-ended simulator for agents in physical and social worlds. In Pro-
ceedingsoftheThirty-ninthAnnualConferenceonNeuralInformationProcessingSystems.
[56] C.Yu,A.Velu,E.Vinitsky,J.Gao,Y.Wang,A.Bayen,andY.Wu.Thesurprisingeffectiveness
ofppoincooperativemulti-agentgames.AdvancesinNeuralInformationProcessingSystems,
35:24611–24624,2022.
[57] Z.Zhang,Y.Lan,Y.Chen,L.Wang,X.Wang,andH.Wang. Dvm: Towardscontrollablellm
agents in social deduction games. In Proceedings of the IEEE International Conference on
Acoustics,SpeechandSignalProcessing(ICASSP),pages1–5.IEEE,2025.
[58] Z. Zhang, C. Wang, D. Weng, Y. Liu, and Y. Wang. Symmetrical reality: Toward a unified
frameworkforphysicalandvirtualreality. InProceedingsoftheIEEEConferenceonVirtual
Realityand3DUserInterfaces(VR),pages1275–1276.IEEE,2019.
[59] Z.Zhang,D.Weng,H.Jiang,Y.Liu,andY.Wang.Inverseaugmentedreality:avirtualagent’s
perspective. In Proceedings of the IEEE International Symposium on Mixed and Augmented
RealityAdjunct(ISMAR-Adjunct),pages154–157.IEEE,2018.
[60] Z. Zhang, Z. Zhang, Z. Jiao, Y. Su, H. Liu, W. Wang, and S.-C. Zhu. On the emergence
of symmetrical reality. In Proceedings of the IEEE Conference Virtual Reality and 3D User
Interfaces(VR),pages639–649.IEEE,2024.
[61] A.Zhao,Y.Wu,Y.Yue,T.Wu,Q.Xu,M.Lin,S.Wang,Q.Wu,Z.Zheng,andG.Huang. Ab-
solutezero: Reinforcedself-playreasoningwithzerodata. arXivpreprintarXiv:2505.03335,
2025.
[62] X.Zheng,H.Lin,K.He,Z.Wang,Q.FU,H.Fu,Z.Zheng,andY.Liang.MCU:Anevaluation
framework for open-ended game agents. In Proceedings of the Forty-second International
ConferenceonMachineLearning,2025.
[63] Q.Zhou,H.Zhang,X.Lin,Z.Zhang,Y.Chen,W.Liu,Z.Zhang,S.Chen,L.Fang,Q.Lyu,
et al. Virtual community: An open world for humans, robots, and society. arXiv preprint
arXiv:2508.14893,2025.
26
