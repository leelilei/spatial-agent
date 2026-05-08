Title: SimWorld: An Open-ended Realistic Simulator for Autonomous Agents in Physical and Social Worlds

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_core/12_HC12_SimWorld.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:47+00:00
- page_count: 24
- status: ok
- text_char_count: 73018

Metadata:
- author: Jiawei Ren; Yan Zhuang; Xiaokang Ye; Lingjun Mao; Xuhong He; Jianzhi Shen; Mrinaal Dogra; Yiming Liang; Ruixuan Zhang; Tianai Yue; Yiqing Yang; Eric Liu; Ryan Wu; Kevin Benavente; Rajiv Mandya Nagaraju; Muhammad Faayez; Xiyan Zhang; Dhruv Vivek Sharma; Xianrui Zhong; Ziqiao Ma; Tianmin Shu; Zhiting Hu; Lianhui Qin
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 3)
- The SimWorld Simulator (page 4)
  - Unreal Engine Backend (page 4)
    - Diverse Scenes (page 5)
    - Rich Assets and Physics Realism (page 6)
  - Environment (page 8)
    - Procedural City Generation (page 8)
    - LLM-based Scene Editing (page 9)
    - Waypoint System (page 9)
    - Traffic System (page 10)
    - Gym-like Interface for Agent-Environment Interaction (page 11)
  - Agent (page 12)
    - Agent Framework (page 12)
    - Observation Space (page 12)
    - Action Space (page 12)
    - Action Planner (page 13)
  - UnrealCV+ Communication Module (page 15)
- Case Study: Delivery Task (page 15)
  - Task Formulation (page 15)
  - Main Results (page 16)
  - Ablation Study (page 17)
- Related Works (page 20)

Markdown Content:

TechnicalReport
SimWorld: An Open-ended Realistic Simulator for
Autonomous Agents in Physical and Social Worlds
JiaweiRen1* YanZhuang2* XiaokangYe1* LingjunMao1 XuhongHe3 JianzhiShen4
MrinaalDogra1 YimingLiang5 RuixuanZhang4 TianaiYue4 YiqingYang6 EricLiu7 RyanWu4
KevinBenavente1 RajivMandyaNagaraju7 MuhammadFaayez4 XiyanZhang4
DhruvVivekSharma1 XianruiZhong3 ZiqiaoMa8 TianminShu4† ZhitingHu1† LianhuiQin1†
1UCSD 2UVA 3UIUC 4JHU 5Purdue 6PolyU 7USC 8UMich
https://simworld.org
LLM/VLM agents in SimWorld
Spawna taxi car
Open-
endedness
Open-ended
Diverse Scenes Environment Text-to-3D Generation Open-ended Action
Realistic
Simulation
Physics Social Interaction Traffic Robots
collision
DiverseUse Recorded FPV Video
replanning
Action
Rotation Position
Data Synthesis Large-scale Simulation Real-world Planning
Figure1: AnOverviewoftheSimWorldSimulator,featuringthreekeydesigns: (1)realistic,open-ended
worldsimulation,(2)richinterfaceforLLM/VLMagents,and(3)diversephysicalandsocialreasoningscenarios.
*Equalcontribution;†Equaladvising
6202
naJ
22
]IA.sc[
2v87010.2152:viXra

While LLM/VLM-powered AI agents have advanced rapidly in math, coding, and computer use, their
applications in complex physical and social environments remain challenging. Building agents that can
surviveandthriveintherealworld(e.g.,byautonomouslyearningincomeorrunningabusiness)requires
massive-scaleinteraction,reasoning,training,andevaluationacrossdiverseembodiedscenarios. However,
existingworldsimulatorsforsuchdevelopmentfallshort: theyoftenrelyonlimitedhand-craftedenvironments,
simulatesimplifiedgame-likephysicsandsocialrules,andlacknativesupportforLLM/VLMagents. We
introduceSimWorld,anewsimulatorbuiltonUnrealEngine5,designedfordevelopingandevaluating
LLM/VLMagentsinrich,real-world-likesettings. SimWorldoffersthreecorecapabilities: (1)realistic,
open-endedworldsimulation,includingaccuratephysicalandsocialdynamicsandlanguage-drivenprocedural
environmentgeneration;(2)richinterfaceforLLM/VLMagents,withmulti-modalworldinputs/feedback
andopen-vocabularyactionoutputsatvaryinglevelsofabstraction;and(3)diverseextensiblephysicaland
socialreasoningscenariosthatareeasilycustomizablebyusers. WedemonstrateSimWorldbydeploying
frontier LLM agents (e.g., GPT-4o, Gemini-2.5-Flash, Claude-3.5, and DeepSeek-Prover-V2) on
long-horizonmulti-agentdeliverytasksinvolvingstrategiccooperationandcompetition. Theresultsreveal
distinctreasoningpatternsandlimitationsacrossmodels. Weopen-sourceSimWorldandhopeitbecomesa
foundationalplatformforadvancingreal-worldagentintelligenceacrossdisciplines: https://simworld.org.
Table of Contents
1 Introduction 3
2 TheSimWorldSimulator 4
2.1 UnrealEngineBackend . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.1.1 DiverseScenes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.1.2 RichAssetsandPhysicsRealism . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Environment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.1 ProceduralCityGeneration. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2.2 LLM-basedSceneEditing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.2.3 WaypointSystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.2.4 TrafficSystem. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.2.5 Gym-likeInterfaceforAgent-EnvironmentInteraction . . . . . . . . . . . . . . . . . . 11
2.3 Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.1 AgentFramework . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.2 ObservationSpace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.3 ActionSpace . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.3.4 ActionPlanner . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.4 UnrealCV+CommunicationModule . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3 CaseStudy: DeliveryTask 15
3.1 TaskFormulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
3.2 MainResults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3.3 AblationStudy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4 RelatedWorks 20
2

1. Introduction
Largelanguageandvisionmodels(e.g.,LLMsandVLMs)haveemergedaspowerfulfoundationsforbuilding
intelligentagents,demonstratingremarkablereasoningcapabilities,particularlyinstructureddomainssuchas
mathematics,coding,andcomputeruse(e.g.,webbrowsing). However,thesemathematicalanddigitalsettings
arerelativelyclean,withwell-definedrulesandclearfeedback. Incontrast,theembodiedphysicalandsocial
worlds, where real-world agents and robots are ultimately expected to operate, are inherently complex, noisy,
dynamic,andunpredictable. Insuchenvironments,agentsmustinteractwithrichandevolvingcontexts,from
navigating urban spaces and interacting with humans, to pursuing long-term goals such as earning a living,
buildingacareer,orrunninganorganization(Brohanetal.,2023;Driessetal.,2023;Wangetal.,2023).
Toadvanceembodiedagentdevelopment,recenteffortshaveexploredsimulationenvironmentsthatofferdifferent
interactiveexperiencesfortrainingandevaluation(Table1). However,game-likeplatformssuchasMinecraft(Fan
et al., 2022; White et al., 2025; Wang et al., 2023; Long et al., 2024; Liu et al., 2024; Li et al., 2025b) and
Pokémon (Ha, 2025; Anthropic, 2025) provide accessible setups for embodied interaction but lack realistic
physical dynamics and social structures, limiting real-world generalization. Domain-specific simulators such
asCARLA(Dosovitskiyetal.,2017)andAI2-THOR(Kolveetal.,2017)targetareaslikeautonomousdriving
and household robotics but are limited to narrow task scopes or static environments. Social sandboxes such
as Virtual Village (Park et al., 2023) and Project Sid (AL et al., 2024) simulate interpersonal interactions in
scripted,small-scalecommunities,butlacktheopen-endednessandscalabilityrequiredformodelingrichersocial
complexity. Moreover,manyoftheseenvironmentsdonotsupportnaturallanguageinterfacesforgoalsetting,
planning,andcontrol,limitingtheircompatibilitywithmodernLLM-basedagents.
Tomeetthesegrowingdemands,wepresentSimWorld,aplatformdesignedtosupportthedevelopmentand
evaluationofautonomousagentsincomplex,dynamic,andinteractiveenvironments. SimWorldisgroundedin
threecoredesignprinciples(Figure1):
1)Realistic,Open-EndedWorldSimulation. SimWorldadvancessimulationbyintegratingtwokeyaspects:
realisticphysicalandsocialdynamics,andopen-ended,language-steerableworldgeneration. Ontherealism
side,SimWorldproducescomplex,dynamicenvironmentsgroundedinphysicallaws(e.g.,gravity,momentum)
and enriched with dynamic elements such as lighting, weather, and pedestrian flow in city-scale 3D scenes.
It also embeds socially grounded behaviors, such as obeying traffic signals and maintaining personal space,
directly into agent logic to support realistic interactions. On the open-ended side, SimWorld offers a broad
rangeofscenes(e.g.,city,countryside,wilderness,islands)andsupportsinfiniteenvironmentexpansionthrough
proceduralgeneration,includingdiverseroadnetworks,buildinglayouts,andurbanconfigurations. Moreover,
usersorAIagentscanmodifysceneson-the-flyvianaturallanguageprompts(e.g.,“add a tree next to the
hospital”). PoweredbySimWorld’sLLM-basededitingandasset-generationmodules,thiscapabilityenables
adaptive,interactiveworldcreation.
2)RichInterfaceforLLM/VLMAgents. SimWorldprovidesaGym-likeinterfacethatenablesLLM/VLM
agentstointeractwithsimulatedworldsusingopen-endednaturallanguageactions. Agentscanperceiverich
multimodalobservations(e.g.,visualscenes,abstractlayouts,andactionfeedback)andrespondwithhigh-level
languagecommands. Forexample,anagentmayreasonandgenerateanabstractaction,“sit on the nearest
chair,” which SimWorld automatically decomposes into a sequence of low-level actions (e.g., navigating
throughwaypoints,sittingdown). Afterexecutingtheactions,thesimulatorprovidesupdatedobservationsand
feedback,allowingtheagenttorefineitsstrategyandcontinuereasoning. Thisclosed-loopinteractionsupports
open-ended, language-driven behaviors and empowers agents to perform long-horizon reasoning at a proper
abstractionlevel.
3)DiversePhysicalandSocialReasoningScenarios. Buildingontheabovephysicallyandsociallygrounded
environmentsandtheagenticinterface,SimWorldnaturallysupportssystematicevaluationandtrainingofagent
reasoningindiverserealistic,long-horizonsettings. Beyondshort,task-orientedbehaviors,agentscanpursue
extendedobjectivessuchasearningmoney, developingacareertrajectory, orrunningamulti-agentbusiness,
wherestrategicdecisionscompoundovertimeandsocialdynamicsinfluenceoutcomes. Toillustratehowthese
capabilities integrate in practice, we showcase a Delivery Task, a case study demonstrating how physical and
socialreasoningjointlyleadtomulti-agentcollaborationandcompetitioninSimWorld. Thetaskmodelsan
urbandeliveryeconomyinwhichagentsbid,invest,andshareorderswhilenavigatingdynamicenvironments.
3

Table1: Comparisonof SimWorldandExistingSimulatorsacrosskeydimensions: Open-endedWorld
(proceduralscene/assetgeneration,language-controllableediting),Physical/SocialRealism(fidelitytoreal-world
mechanics), Action Space (action abstraction level, open-vocabulary action space), Agent Type (types of
controllable agents: Humanoid (Hum.), Robot, Drone or Vehicle (Veh.)), and Physics Engine (underlying
simulation engine). H means high-level actions (e.g., “deliver”, “navigate to”), and L means low-level
actions(e.g.,“forward by 1 step”).
Open-endedWorld Physical/Social ActionSpace
Simulator AgentType PhysicsEngine
Procedural Lang.-Ctrl Realism Abstr. Open-Vocab
Minedojo(Fanetal.,2022) ✓ ✗ + L ✗ Hum. Minecraft
Mindcraft(Whiteetal.,2025) ✓ ✗ + H ✗ Hum. Minecraft
MetaUrban(Wuetal.,2025) ✓ ✗ ++ L ✗ Veh. PyBullet
EmbodiedCity(Gaoetal.,2024) ✗ ✗ +++ L ✗ Drone/Veh. UnrealEngine
CARLA(Dosovitskiyetal.,2017) ✗ ✗ +++ L ✗ Veh. UE&Unity
GRUtopia(Wangetal.,2024a) ✗ ✗ ++ L ✗ Hum./Robot IsaacSim
OmniGibson(Lietal.,2024) ✗ ✗ ++ H/L ✗ Robot Omniverse
AI2-THOR(Kolveetal.,2017) ✓ ✗ ++ L ✗ Robot Unity
Habitat3.0(Puigetal.,2023) ✗ ✗ ++ L ✗ Hum./Robot Bullet
Genesis (Authors,2024) ✓ ✗ +++ L ✗ Robot Taichi
VirtualCommunity (Zhouetal.,2025) ✓ ✗ ++ L ✗ Hum./Robot Genesis
UnrealZoo(Zhongetal.,2025) ✗ ✗ +++ L ✗ Hum./Robot/Veh. UnrealEngine
SimWorld ✓ ✓ +++ H/L ✓ Hum./Robot/Veh. UnrealEngine
Withdifferentpersonas,budgets,andtools(e.g.,vehicles),agentsdevelopdiversestrategiesshapedbytheirgoals
andchangingconditions(e.g.,fluctuatingprices). Thetaskhighlightscomplexdecision-makingandlong-horizon
planning,wherecooperation,competition,andemergentsocialbehaviorsarisenaturally.
WedeployfrontierLLMsasagentssuchasGPT-4o,Claude-3.5-Sonnet,Gemini-2.5-Flash,andotherson
theDeliveryTask. WeobservethatClaude-3.5-SonnetandDeepSeek-V3earnthehighestprofits,butoften
behaveerratically,suchasoverbiddingonlow-valueordersorspendingalltheirmoneyonscooterstheyneveruse.
Incontrast,Gemini-2.5-FlashandDeepSeek-Prover-V2followmoreconservative,stablestrategies,trading
peakperformanceforconsistency. Personalitytraitsalsoshapeagentbehavior: conscientiousagentsfocuson
taskcompletion,whileopenagentsexplorebutfrequentlylosemoney. Thesefindingsexposeboththestrengths
andlimitationsofLLM-basedagents,whilerevealingrich,oftenunexpectedbehaviorsthatemergefromtheir
interactionwithcomplexenvironments.
We open-source SimWorld with the aim of establishing a foundational infrastructure for real-world agent
researchacrossdisciplines. BysupportingadvancedLLM/VLM-basedagentsandenablinglarge-scale,realistic
agent–environmentandagent–agentinteractions,SimWorldexpandsthecapabilitiesofmodernagent-based
simulation (ABS). This allows researchers in robotics, business, public health, social science, education, and
beyondtostudycomplexsystemsandemergentbehaviorsinrich,dynamic,andcontrollableenvironments. More
detailsoftheSimWorldprojectareavailableathttps://simworld.org.
2. The SimWorld Simulator
Realistic,open-ended,andnativelyLLM/VLM-compatiblesimulatorsarecrucialforadvancingagentdevelopment
incomplexphysicalandsocialscenarios. SimWorldtakesasteptowardthisgoalthroughathree-tierarchitecture
as illustrated in Figure 2. It separates the Unreal Engine Backend (§2.1) from two added Python layers: the
EnvironmentlayerprovidinginfiniteenvironmentgenerationandstandardGym-likeenvironment-agentinterface
(§2.2), and the Agent layer supporting diverse input observations, open-ended output actions, and different
reasoning/planningcomponents(§2.3). Inaddition,theUnrealCV+communicationmoduleenablesseamless
interactionbetweentheUnrealEnginebackendandtheEnvironmentlayer(§2.4).
2.1.UnrealEngineBackend
TheUnrealEnginebackendformsthefoundationof SimWorld,providinghigh-fidelityrenderingandphysics
simulation. It consists of three tightly coupled modules: (1) Scenes (§2.1.1) supporting both procedurally
generatedandcuratedmaps;(2)AssetLibrary(§2.1.2)ensuringdiverseandphysicallygroundedcontent;and
4

Observation LLM/VLM Backend History
Step 45: Pick up
Step 44: Move to (-8, 10)
Step 43: Turn left 75°
Agent Framework …
Memory
Agent …
Sensors
(Python) root Perception Mental Action Planner
State
road 1st Avanue2nd Street World
Reasoning
building school Model
Planning
Scene Graph GPS
Observation Action
Procedural Generation Scene Editing Gym-like Interface Traffic System
def agent_thread(agent):
Environment
Add def step(action):
(Python) Details env.execute(action)
Place a tree to the obs = env.get_observation()
right of the hospital.
UnrealCV+ Scene Get Execute Traffic
(TCP) Generation Observation Action Simulation
Text-to-3D
Character Assets Object Assets
Unreal Engine
Backend
(C++)
Effect Assets Animation Assets
Scenes Asset Library Physics Simulation
Import
UE marketplace
Figure2: Architectureof SimWorld. SimWorldadoptsahierarchical,closed-looparchitecturethatdecouples
agentreasoningfromhigh-performancerenderingwhilemaintainingcoherentinformationflowacrossmodules.
Atitscore,theUnrealEngineBackendprovideshigh-fidelityscenes,assets,andphysics,servingasthefoundation
for realistic simulation. Built upon it, the Environment layer functions as an intermediary that abstracts the
underlyingrenderingandphysicsintostructuredrepresentations. Itenablesproceduralcitygeneration,traffic
simulation,andexposesaGym-likeinterfaceforagentinteractionthroughUnrealCV+. TheAgentlayeroperates
on this interface, integrating LLM/VLM agents that interpret observations from the Environment, perform
reasoning,andissueactionsthataresubsequentlyexecutedthroughtheEnvironment’sconnectiontotheUnreal
EngineBackend,therebyformingaclosedperception–planning-actionloop.
(3)PhysicsSimulation(§2.1.2)governingrealisticphysicalbehaviors.
2.1.1.DiverseScenes
SimWorldsupportstwoscene-buildingmodes: handcraftedscenesandprocedurallygeneratedscenes.
HandcraftedScenes. ThankstoSimWorld’sfoundationinUnrealEngine,userscaneasilyimportalarge
collectionofhigh-qualityenvironmentsdirectlyfromtheUnrealEngineMarketplace1 orcreatecustomscenesby
1https://www.fab.com/
5

Figure3: ExampleScenesinSimWorld.
hand. Inourcurrentimplementation,wecurateover100handcraftedscenes2 spanningawidevarietyofvisual
andstructuralstyles,fromancienttownsandnaturallandscapestofuturisticcitiesandimaginativefantasyworlds.
Eachsceneprovidesdistinctvisualcues,spatiallayouts,andinteractionaffordances,enablingthoroughevaluation
ofembodiedagentsacrossdiversesettings. Figure3illustratesseveralexamples.
ProcedurallyGeneratedScenes. Complementingthesehandcraftedassets,SimWorldfeaturesaprocedural
generation module for automatically constructing diverse urban environments. Users can specify high-level
parameters(e.g.,citysize,roaddensity,layoutstyle),andthesystemgenerateslargenumbersofcityvariants
efficientlyandconsistently. Thissupportsscalableexperimentationundercontrolled,customizableconditions.
AdditionaldetailsareprovidedinSection2.2.1.
Bycombininghigh-fidelityhandcraftedsceneswithflexibleproceduralgeneration,SimWorldoffersabroadand
extensiblesetofenvironmentssuitableforbothcontrolledexperimentsandopen-endedagentresearch.
2.1.2.RichAssetsandPhysicsRealism
SimWorldprovidesacomprehensiveassetlibrarytosupportrealistic,physics-drivensimulationsacrossdiverse
environments. Thesystemintegratesstaticassets(e.g.,buildings)anddynamicassets(e.g.,pedestrians),and
furtherincorporatesenvironmentalfactors(e.g.,lighting,weather)tocreateimmersivevirtualworlds. Italso
supportsawiderangeofanimationsandinteractions,enablingagentstoperformdiverseactionsfaithfullywithin
theenvironments.
ObjectAssets. Theobjectassetlibraryformsthestructuralbackboneof SimWorldenvironments,whereeach
scenecanbeviewedasacompositionofmultipleobjectassets. Theseassetsincludedetailedmaterialdefinitions
and collision meshes, enabling a wide range of physically accurate interactions such as reflection, occlusion,
andcontactdynamics. Overall,theycanbebroadlygroupedintothreecategories: (i)Buildingassets: Primary
2TheSimWorldreleaseincludesallscenesasexecutablebuilds,availableathttps://github.com/SimWorld-AI/SimWorld.
6

Vehicle Robot Human
Figure4: EmbodiedAgents. SimWorldsupportsthreetypesofagentembodiments: vehicle,robot,andhuman.
structuralelementsofurbanscenes,coveringawiderangeofarchitecturaltypes(e.g.,residential,commercial,
industrial) and supporting both indoor and outdoor environment construction. (ii) Vegetation assets: Natural
elements such as trees, grass, and shrubs, modeled with realistic material appearance and optional seasonal
variations. (iii)Urbanpropassets: Fine-grainedobjectssuchasbenches,mailboxes,lampposts,andtrafficsigns,
enablingdiverseagentinteractionssuchassitting,opening,ormanipulatingobjects.
Text-to-3D Asset Generation. To further expand the range of available objects, SimWorld introduces an
AssetGenerationPipelinebasedonrecentText-to-3Dmodels(Hunyuan3D,2025). Thissystemallowsusers
todescribeassetsinnaturallanguage,automaticallygenerating3Dobjectswithconsistentscale,texture,and
physical properties. The generated assets can be seamlessly integrated into the simulator, inheriting various
properties(e.g.,materials,lighting,collisionconfigurations)compatiblewithUE’sphysicsengine.
CharactersandEmbodiments. CharacterassetsinSimWorldrepresentembodiedentitiescapableofacting,
navigating,andinteractingwithinthevirtualenvironment. Thesystemsupportsthreeprimarytypesofagent
embodiments: human,vehicle,androbot(Figure4). Humanembodimentscapturediversehumanappearances
and employ fully rigged skeletal structures that enable realistic animations produced through coordinated
bonearticulation,suchasrunningorcarryingobjects. Vehicleembodimentsreproducearangeofreal-world
transportationmodes(e.g.,buses,cars)andimplementaccuratephysicaldrivingdynamics,suchasacceleration,
steering,braking,andtraction. Roboticembodimentsmodelspecificcategoriesofrobots(e.g.,quadrupedsystems)
withrealisticactuation,jointcontrol,andsensingmodules,makingthemsuitableforevaluatingrobotlocomotion
andstabilityacrossdifferentenvironmentsandtasks. Alltheseembodimentsoperatewithinaunifiedphysics
frameworkandsharecommonattributes(e.g.,mass,inertia,contactforces),whichensuresconsistenthandlingof
physicalpropertiesandinteractionsacrossallentities.
WeatherandLighting. SimWorldsupportsawiderangeoflightingandweatherconditions. Thelighting
systemmodelsmultiplelighttypes(e.g.,directional,ambient,anddynamicsources)withcontrollableparameters
suchasintensity,orientation,andcolortemperature. Theweathersystemsupportsavarietyofconditions(e.g.,
rain,snow,andfog)thatinfluencevisualappearanceanddriveatmosphericeffects,includingphenomenalike
fog-inducedlightscattering. Together,thesecomponentsrecreatethecomplexityanddynamismofreal-world
environments,enablingthestudyofembodiedagents’perceptionandadaptationunderrealisticconditions.
PhysicalDynamicsandAnimations. PoweredbyUnrealEngine,SimWorldprovidesaccurateandcontinuous
physical simulation. Unlike popular agent environments suchas Minecraft (Fan et al., 2022; Yu et al., 2024),
which rely on discrete, block-based mechanics without real gravity or inertia, SimWorld models real-world
physicaldynamics. Agentsaresubjecttophysicalforcesthatproducegroundedbehaviorslikeslidingdownslopes
ortrippingoversteps. Theseeffectsproducephysicallygrounded,embodiedinteractions. BycombiningUnreal
Engine’sphysicsenginewithphysicallyinformedanimations(e.g.,motionblending,inversekinematics,collision
responses),SimWorldmaintainscoherencebetweenmotionandenvironmentalforces,enablingbelievableand
adaptableagentbehaviorsincomplexenvironments.
7

Algorithm1ProceduralCityLayoutGenerationusingQuadTree
1: Input: Configurationparametersconfig
2: Output: FinalQuadTreeQ representingthecitylayout
city
3: InitializeemptyQuadTreeQ
city
4: if s = roadthen
5: Generateroadnetworkviagrowth-basedmodel ▷Proceduralstreetexpansion
6: InsertroadgeometriesintoQ ▷Storeroadsegments
s
7: MergeQ intoQ ▷Integrateroadlayout
s city
8: if s = buildingthen
9: Samplebuildingcandidates(orientation,position)
10: Rejectinvalidsamplesbycollisiontest ▷Spatialconsistencyfiltering
11: Greedyfillremaininggapswithvalidbuildings
12: InsertbuildingsintoQ
s
13: MergeQ intoQ ▷Integratebuildinglayout
s city
14: if s = streetelementthen
15: Sampledecorative/environmentalelements
16: Rejectoverlappingsamplesbycollisiontest
17: InsertdetailelementsintoQ
s
18: MergeQ intoQ ▷Integratestreet-leveldetails
s city
19: returnQ
city
2.2.Environment
SimWorldintroducesanenvironmentlayerontopoftheUnrealEnginebackend(Figure2). Thislayermanages
the creation and organization of simulated environments and provides a clean abstraction that enables easy
deployment of agents into Unreal Engine–based worlds through AI-native, user-friendly interfaces, without
requiring users to handle the complexities of the underlying UE system. Specifically, the environment layer
integratesmodulesforProceduralCityGeneration(§2.2.1),LLM-basedSceneEditing(§2.2.2),TrafficSystems
(§2.2.4),and,crucially,aGym-likeInterface(§2.2.5)foragent–environmentinteraction. Italsooffersanauxiliary
WaypointSystem(§2.2.3)thatsimplifiesagentnavigationwithincomplexworlds.
2.2.1.ProceduralCityGeneration
Previoussimulatorstypicallyrelyonalimitedsetofhand-craftedscenes(e.g.,15scenesinCARLAand211
scenesinHabitat3.0). SimWorlddevelopsaproceduralgenerationsystem(Figure5a)capableofproducing
diverse,unlimitedurbanenvironments,includingroadnetworks,buildinglayouts,dynamictraffic,andfine-grained
elementslikestreetfurniture,enablingeffectivelyinfinitesimulationscenarios. Allparameters(e.g.,citysize,
buildingdensity,vehicleandpedestriancount)arecustomizable,allowinguserstogeneratevariedandcontrollable
environmentswithminimalmanualeffort.
Inspired by (Phiresky, 2024), SimWorld ’s procedural generation system adopts a modular and extensible
architecture. Thepipelineproceedsthroughthreesequentialstages: roadgeneration,buildinggeneration,and
streetelementgeneration,eachprogressivelyenrichingtheenvironmentwithstructuralandvisualcomplexity.
ThesystemconstructsahierarchicalscenegraphbasedonaquadtreedatastructureasillustratedinAlgorithm1.
RoadGeneration. Roadgenerationdefinesthestructuralbackboneofthecitylayout. Roadsarefirstinitialized
andthenexpandedusingaspanning-tree–basedalgorithmwithapriorityqueuethatbalancesdepthandbranching
duringnetworkconstruction. Additionalprocedures,includingroad-endattachmentandintersectionvalidation,
maintaintopologicalcoherenceandrealisminthegeneratedlayout.
BuildingGeneration. Followingtheroadgenerationstage,thepipelineproceedstobuildinggeneration,where
buildingassetsareprocedurallyinstantiatedalongroadsegments. Candidatelocationsaresampledandvalidated
forspatialfeasibilitytopreventoverlap. Agreedyplacementstrategythenfillsresidualgapsnearintersections
androadends,improvingspatialutilizationandmaintainingvisualconsistency.
8

“Add some tables 1
and treesin front of
the gate of hospital
near clock tower”
tables Add Tables x 4
Road Generation Building Generation Element Generation trees Retrieval
Add Trees x 4
2
Text to 3D
Generation
Assets Library
(a)ProceduralCityGeneration (b)LLM-ControllableSceneEdit
Figure5: OverviewofProceduralCityGenerationandLLM-BasedSceneEditing.
Street Element Generation. Finally, street element generation adds detailed environmental elements (e.g.,
trees,roadcones,benches,andparkedvehicles). Elementsarecategorizedandpositionedbasedoncontextual
zones,eitheradjacenttobuildingsoralongsidewalks. Whilestrictcollisionenforcementisrelaxedtomaintain
performance,placementstillrespectsbasicaccessibilityandspatialcoherenceconstraints.
2.2.2.LLM-basedSceneEditing
Beyondproceduralgeneration,SimWorldsupportsnaturallanguage-basedsceneediting(Figure5b),enabling
dynamicworldconstructionthroughopen-endedinstructions. UsersorAIagentscanmodifysceneson-the-fly
withcommandssuchas“add a red sports car next to the hospital near a museum”. SimWorld
contains a retrieval-augmented LLM-based scene agent that grounds the command by querying the current
environment’sscenegraph. Theagentidentifiestheintendedlocationusingspatialanchors(e.g.,“hospital”)
andcontextuallandmarks(“museum”),retrievesamatchingassetfromalibrary,andinsertsitaccordingly. Ifa
suitableassetisunavailable,theagentinvokesanoff-the-shelftext-to-3Dgenerationmodel(Hunyuan3D,2025)
to synthesize a new object from the prompt (“red sports car”), converts it into a compatible format, and
integratesitintotheenvironment. Thisapproachenablessemanticallygrounded,spatiallycoherent,andscalable
worldconstruction,layingthefoundationforinteractiveandcompositionalsimulation.
2.2.3.WaypointSystem
SimWorldimplementsawaypointsystemthatprovidesastructuredrepresentationofnavigablespacetosupport
agentnavigationandpathplanning(Figure6). Asanauxiliaryabstractionlayer,thewaypointsystemsimplifies
movementbyofferingaclean,graph-basedrepresentationofwhereagentscangoandhowtheycangetthere. It
formsthespatialbackboneforboththetrafficsystem(§2.2.4)andtheactionplanner(§2.3.4),enablingagentsto
moveefficientlythroughcomplexenvironments.
Thesystemincludestwocomplementarywaypointrepresentations,coarse-grainedandfine-grained,whichtogether
createaunifiednavigationgraph. Coarsewaypointscapturehigh-levelconnectivity(e.g.,roads,intersections),
whilefine-grainedwaypointsrepresentdetailedwalkablepaths. Thishierarchicalstructureenablesflexibleand
robustnavigationbehaviors,includinglanefollowing,turning,detouring,andobstacleavoidance.
Coarse-grainedWaypoints. Thecoarse-grainedwaypointsaregeneratedfromthegeometricoutputsofthe
procedural city generation module (§2.2.1), including road centerlines and intersection coordinates. These
waypointsrepresentmajorstructuralpointswithintheroadnetworkandcapturetheprimaryconnectivityamong
differentroutes.
Fine-grainedWaypoints. Thefine-grainedwaypointsareinterpolatedalongtheroadsbetweencoarse-grained
waypoints. These additional points increase the density of the navigation graph, allowing agents to follow
9

Figure 6: Overview of Waypoint System. Vehicles and pedestrians navigate through the environment by
followingwaypoints.
Traffic
Controller
Traffic Vehicle Pedestrian Intersection
Network Manager Manager Manager
Traffic Lane Sidewalk Crosswalk Vehicle Pedestrian Intersection
PID Controller Traffic Signal
Figure7: ArchitectureofTrafficSysteminSimWorld.
smootherandmorecontinuoustrajectories. Parameterssuchasinterpolationstepsizeandspatialoffsetmagnitude
canbecustomizedbyusers.
2.2.4.TrafficSystem
ThetrafficsysteminSimWorldsimulatesdynamicroadusageinvolvingbothvehiclesandpedestrians. Itmodels
realistictrafficflowthroughmodulesofvehiclespawning,routeassignment,intersectioncontrol,andpedestrian
movement (Figure 7). By managing interactions among agents and coordinating traffic signals, the system
supportscomplexurbanphenomenasuchascongestion,pedestriancrossings,andtrafficlightsynchronization.
Thetrafficsimulationsupportsrouteassignment,intersectioncontrol,andpedestrianflowsimulation,runningon
afixed-timestepupdateloopforconsistentanddeterministicupdates(Algorithm2). Vehiclemotionisgoverned
byaproportional–integral–derivative(PID)controller,withempiricallytunedparametersforrealisticacceleration,
braking,andturningdynamics(Jain&Babel,2024). Pedestrianmotionfollowsalightweightmodelthatadjusts
pedestrians’ orientations incrementally toward their goals based on angular differences. To simulate realistic
patterns,SimWorldusesastochasticroutingpolicyatintersections,i.e.,agentsselectoutgoingroutesaccording
topredefinedprobabilitydistributions. Thisstochasticbehaviorintroducesnaturalvariabilityandenhancesscene
diversity.
Thetrafficsystemisbuiltuponthewaypointsystem(§2.2.3),enablingtrafficsimulationthatgeneralizestoany
procedurally generated city layout. Using the waypoints, the system calculates the detailed traffic areas (e.g.,
road lanes, sidewalks, and crosswalks) and procedurally instantiates vehicles, pedestrians, and traffic signals
accordingly. Threespecializedmanagerscoordinatetheseprocesses:
VehicleManager. Vehiclemanagerinitializesvehiclesalongdesignatedtrafficlanesandassignseitherpredefined
ordynamicallygeneratedroutesthroughthenavigationnetwork.
10

Algorithm2SimulationLoopforUrbanTrafficEnvironments
1: Initialize: SampleinitialstatesforvehiclesV,pedestriansP,andtrafficsignalsS.
2: Setsimulationtimet ← 0.
3: whilet < T do ▷Mainsimulationloop
max
4: UpdateVehicles(V,P,S)
5: UpdatePedestrians(P,V,S)
6: UpdateSignals(S,t)
7: t ← t+∆t
10: functionUpdateVehicles(V,P,S)
11: forallv ∈ V do
12: Perceiveenvironment(V,P,S)
13: Executedrivingmodel(throttle,brake,steering)
14: Updatev’sstate(position,velocity)
16: functionUpdatePedestrians(P,V,S)
17: forallp ∈ P do
18: Perceive(V,S),executewalkinglogic
19: Updatep’sposition
21: functionUpdateSignals(S,t)
22: foralls ∈ S do
23: Updatesaccordingtotimingplanoradaptivepolicy
PedestrianManager. Pedestrianmanagerspawnspedestriansonsidewalksandgovernstheirmotionpatterns,
includingcrossingbehaviorandlocalavoidanceatintersections.
IntersectionManager. Intersectionmanagerdetectsintersectionswithinthetrafficnetworkanddeploystraffic
signalsthatregulateright-of-wayaccordingtoconfigurabletimingcyclesoradaptivecontrolpolicies.
Together,thesecomponentsconstituteaunifiedtrafficsimulationpipeline,enablingthevirtualcitytoexhibit
realistic,adaptive,andscalablemobilitydynamicsacrossdiverseurbanlayouts.
2.2.5.Gym-likeInterfaceforAgent-EnvironmentInteraction
SimWorldprovidesastandardGym-likeinterface,enablingseamlessintegrationwithexistingreinforcement
learningpipelinesandagentframeworks. BecausethisinterfacefollowsthewidelyadoptedAPIconventions
ofGym(FaramaFoundation,2023),suchasstandardizedreset(),step(),andobservation–actionexchange
(Figure 2), it becomes straightforward for users to plug in their RL agents and immediately begin interacting
withSimWorld’ssimulatedenvironments. Thisdesignsignificantlylowersthebarrierforconductinglarge-
scaleexperimentation,benchmarking,andagent–environmentinteractionstudiesusingmodernLLM/VLMor
policy-basedagents.
Tosupportabroadvarietyofresearchgoalsrangingfromopen-endedsimulationstohighlycontrolledevaluations,
SimWorld offers two simulation modes inspired by prior work such as CARLA (Dosovitskiy et al., 2017):
asynchronousandsynchronousexecution.
AsynchronousMode. Inasynchronousmode,eachagentrunsinitsownthreadandadvancesindependently,
withoutwaitingforotheragentstofinishtheirreasoningoractiongeneration. Agentspullobservationsfroma
centralizedbufferandsubmitactionswhenevertheyareready. Theenvironmentprocessesallreceivedactionsat
fixedintervals(default: 0.1s),allowingreal-time,continuous,andscalablemulti-agentinteractions. Thismodeis
idealforlarge-scale,open-ended,orexploratorysimulationswherethroughput,diversity,andresponsivenessare
key.
SynchronousMode. Insynchronousmode,allagentsadvanceinlockstep: thesimulatorproceedstothenext
steponlyaftereveryagenthassubmitteditsaction. Thisensuresstricttemporalalignmentbetweenperceptionand
control,makingthemodeparticularlysuitableforexperimentsrequiringreproducibility,coordinatedmulti-agent
11

behavior,orhigh-qualitydatacollection(e.g.,videogenerationorRLtrainingwithfixedsteptiming).
2.3.Agent
SimWorldprovidesaunifiedinterfaceforLLM/VLMagents,supportingaflexibleAgentFramework(§2.3.1),
adiverseObservationSpace(§2.3.2)andanopen-endedActionSpace(§2.3.3). Thisinterfaceisdesignedto
accommodatebothlow-levelcontrolandhigh-levelreasoningforLLM/VLMagentsthroughanActionPlanner
(§2.3.4)module,servingastheprimaryentrypointforagent–environmentinteraction.
2.3.1.AgentFramework
TheagentframeworkinSimWorlddefinesaunifiedinterfacethatstructuresthefullagentloopofperception,
reasoning, planning, and execution. Across different embodiments—humanoids, vehicles, and robots—the
frameworkprovidesacommoncontrolpipeline.
Each agent first acquires observations from SimWorld ’s observation space (§2.3.2) via API calls (e.g.,
get_camera_observation(), get_agent_location()). These observations (e.g., visual inputs, scene
graphs)arethenprocessedbytheagent’sreasoningbackend,whichmayincorporateLLMs,VLMs,VLAs,or
other decision-making models. Based on these observations, agents can employ any advanced reasoning or
planningalgorithms(Guoetal.,2025;Haoetal.,2023;ALetal.,2024).
Reasoningoutputsmaybeexpressedinnaturallanguage(e.g.,“sit on the nearest chair”)orinstructured
formatssuchasfunctioncalls. Bothformatsarecompatiblewiththeactionplanner(§2.3.4),whichinterprets
themintoexecutablelow-levelactions.
Theframeworkisalsohighlyextensible. Researcherscanpluginadvancedreasoningcomponentssuchasworld
models(Hu&Shu,2023;Xingetal.,2025),memorysystems(Hoetal.,2025;Wangetal.,2024b),ormental-state
modules(e.g.,emotionsorpreferences),enablingbroadinvestigationintolong-horizonreasoning,planning,and
embodiedintelligence.
2.3.2.ObservationSpace
SimWorldprovidesmultipleobservationmodalitiesforagentperceptionandreasoning. Theobservationspace
isorganizedintotwoprimarycategories: visualobservationsandstructuredsemanticinformation(Figure2).
VisualObservations. Agentscanaccessthreetypesofcamera-basedinputsfromafirst-personview: (1)color
imagescapturingtherawvisualappearanceoftheenvironment,(2)depthmapsencodinggeometricdistancefrom
theagent’sviewpoint,and(3)semanticsegmentationmasksprovidingpixel-levelobjectcategoryinformation.
StructuredSemanticObservations. Beyondpixel-basedperception,SimWorldexposeshigh-levelspatialand
semanticrepresentations,includingasemanticscenegraphandGPS-likelocalizationinformation. Thescene
graphencodesentities,attributes,andrelationalstructureswithintheenvironment,offeringasymbolicabstraction
ofthe3Dworld. Thelocalizationinterfacespecifieseachagent’sorobject’spositionandorientation,enabling
precisereasoningaboutspatialrelationships.
2.3.3.ActionSpace
SimWorldenablesopen-vocabularyactionexecutionbyorganizingtheactionspaceintotwohierarchicallayers:
high-levelsemanticactionsandlow-levelprimitiveactions:
High-LevelSemanticActions. Tofacilitateabstractreasoningandlong-horizondecision-making,agentscan
issuenaturallanguagecommands. Thesecommandsareinterpretedandexecutedbythebuilt-inactionplanner
(§2.3.4),enablingflexible,open-endedbehaviors(e.g.,“sit on the nearest chair”).
Low-LevelPrimitiveActions. Primitiveactionsprovidefine-grainedcontroloveragents. Vehiclessupport
continuous control signals (e.g., “acceleration”, “braking”, and “steering”). Robots allow continuous
translation and rotation (e.g., “forward”, “backward”, “lateral_movement”, and “rotation”). Human
12

Table2: Low-LevelPrimitiveActionsinSimWorld.
Action AgentType Description
ObjectInteractionActions
PickUp/DropOff Humanoid Grasporreleaseanobject
Carry/PutDownHeavyObject Humanoid Transportandplacelargeobjects
SitDown/StandUp Humanoid Transitionbetweenseatedandstandingstates
OpenDoor/Enter/ExitCar Humanoid Interactwithdoorsorvehicles
RideScooter Humanoid Controlandrideascooter
ObservationActions
LookUp/Down Humanoid,Dog Adjustgazevertically
Focus Humanoid,Dog Narroworwidenthefieldofview
TakePhoto All Capturecurrentviewasanimage
SocialActions
HaveConversation/Discuss Humanoid Exchangeverbalcommunication
PointDirection/WaveHand Humanoid Usegesturesforsocialsignaling
ArguewithBodyLanguage Humanoid Expressdisagreementthroughgestures
NavigationActions
MoveForward/StepForward–Backward Humanoid,Dog Moveorstepinthecurrentdirectionforashortduration
Rotate/Steering Humanoid,Dog,Vehicle Adjustfacingorsteeringdirection
Throttle/Brake Vehicle Accelerateordeceleratethevehicle
Stop All Haltallcurrentmotion
agentscannavigate(“move”,“turn”)andperforminteractiveactions,includinghuman–object(e.g.,“pick_up”,
“drop”, “sit”), human–vehicle (e.g., “enter_car”, “exit_car”), and human–human (e.g., “wave_hands”,
“discussion”)interactions. AcompletelistofsupportedactionsisprovidedinTable2.
2.3.4.ActionPlanner
SimWorldincludesanactionplannermodulethatbridgeshigh-levelreasoningwithlow-levelexecution,allowing
researcherstofocusonabstractplanningwithoutneedingtomanageembodiment-specificcontroldetails. The
plannerconsistsoftwocomponents: aparserandanexecutor. Theparserreceiveshigh-levelplansfromthe
agent, often expressed in natural language or structured function calls, and translates them into sequences of
low-levelprimitiveactions. Theexecutorthencarriesouttheseactionsstepbystep,conditionedonthecurrent
environmentstate.
To support diverse research objectives, SimWorld provides two executor variants: a rule-based executor,
whichoperatesonabstractcity-layoutinformation,andavisual-basedexecutor,whichdirectlyconsumesvisual
observations from the simulator. The latter enables seamless integration with VLMs or VLAs, supporting
end-to-endperception–reasoning–actionpipelines.
By handling the translation from high-level intent to low-level control, the action planner enables agents to
performlong-horizon,semanticplanningwhileSimWorldautomaticallymanagesmovement,navigation,and
interactiondetails.
Forexample,whentheactionplannerreceivesaplansuchas“go to the nearest chair and sit down”,
the parser first decomposes the instruction into an action list: “navigate” and “agent_sit_down". The
navigateactionisnon-atomicandcanbefurtherexpandedintoprimitiveoperationssuchas“step_forward”
and“rotate”byexecutor. Intherule-based executionmode,theplannercomputestheshortestpathfromthe
agent’scurrentpositiontothenearestchair,generatingasequenceofnavigationprimitivessuchasnavigate(0,
1),navigate(1, 10),andnavigate(10, 10),where(10, 10)denotesthechair’slocation. Oncetheagent
reachesthechair,theexecutorexecutes“agent_sit_down”andterminateswhentheactionlistbecomesempty.
Inthevisual-based mode,theexecutordirectlyfeedsenvironmentalobservationsintoaVLM(e.g.,GPT-4o),
whichdeterminesthenextactionstepbystep(e.g.,execute“step_forward”then“step_forward”andfinally
“agent_sit_down”)basedonvisualcontext.
13

1. Assets Preparation
Download from FAB Marketplace Generated by assets generation models
Download A motor cycle
with orange
3DAssets
body color…
Generation Model
Overview of Buildings
2. Scene Preparation
Load layouts to Unreal
Load
Rendered Scenes
Layouts of Scenes in Unreal Engine
3. Spawning Agent
Spawn vehicles, pedestrains and agents step by step
Original Scene Pedestrians/Vehicles Spawned Agents Spawned
4. Simulation
Managing and control task pipeline
bid for 100$ Go picking up order 1
👍 Next waypoint:
bid for 80$
(100, 20)
I have an order…
Dispatch Order Broadcast Collaboration Track Actions Calculate Reward
Delivery Task Loop
5. Evaluation
Evaluate agents capabilities Analysis agent behaviors
Figure8: WorkflowforConstructingaTaskSuiteinSimWorld.
14

2.4.UnrealCV+CommunicationModule
InspiredbyUnrealCV(Qiuetal.,2017),wedevelopUnrealCV+asacommunicationmodulethatbridgesthe
UnrealEnginebackend(§2.1)withtheenvironmentlayer(§2.2). ByestablishingaTransmissionControlProtocol
(TCP)connection,UnrealCV+enablesefficient,reliable,andbidirectionalcommunicationbetweenthetwosides.
ImplementedinbothPythonandC++,themodulesupportsflexibledataexchangeandfine-grainedcontrolofthe
simulation.
To adapt UnrealCV+ to agent-task scenarios, we introduce a customized command set for scene control,
actor manipulation, and data querying. For example, the environment layer can issue commands to the
UnrealEnginebackendsuchas“spawn actors at locations”,“get position of a pedestrian”,or
“execute action of a robot”.
Within the simulation loop, the environment layer governs the logical evolution of the simulation, while the
Unreal Engine backend continuously returns updated physical states and visual observations of all agents.
AllcommunicationsaretransmittedthroughUnrealCV+. Thisdecoupledarchitecturecleanlyseparateslogic
computationfromrendering,improvingflexibility,scalability,andmodularity.
3. Case Study: Delivery Task
SimWorldisbuiltwithextensibilityandevaluationtaskcreationascoredesigngoals. Itprovidestoolstoeasily
definetasks,agentroles,rewardfunctions,andevaluationmetrics,minimizingtheengineeringeffortrequiredto
createnewexperiments. Figure8showcaseshowtodefineamulti-agentdeliverytaskwithintheSimWorld
ecosystem. Theprocessisdelineatedasfollows:
First, users prepare assets for the delivery task, either by importing 3D assets purchased from third-party
marketplacesorbygeneratingthemusingtext-to-3Dmodels. Next,SimWorldinitializesthecityenvironments
via its procedural city generation module to build roads, buildings, trees, and city props. Third, vehicles,
pedestriansanddeliveryagentsarespawned. Fourth,thesimulationruns,allowingdeliveryagentstoactand
interact within the configured environment dynamics. Finally, delivery agents are evaluated across multiple
dimensions, such as delivery success rate, average completion time, and total profit. The following sections
providedetaileddefinitionsandanalysis. TheeventualarchitectureofthedeliverytaskisshowninFigure9.
3.1.TaskFormulation
The delivery task is designed to evaluate the social reasoning capabilities of foundation models in realistic,
open-worldurbanenvironments. LLMagentsaredeployedasdeliveryagentsinacity-scaleenvironmentbuilt
usingSimWorld. Theirgoalistogrowandthriveinthisdynamicsetting. Toenhancerealismandcomplexity,the
environmentincorporatesseveraldynamicsystems: (1)anenergysystem,whereagentsmustmanagestaminaand
replenishitthroughconsumables;(2)aneconomicsystem,whereagentsearnandspendcurrencyonpurchases
suchasscootersanddrinks;(3)anorder-sharingmechanism,enablingagentstocollaboratebysharingdelivery
tasksandoptimizinggroupperformance. Thesecomponentscreatearich,interactivesimulationenvironmentfor
evaluatingagents’decision-making,adaptability,andsocialreasoningincomplexurbanscenarios. Theoverview
ofthedeliverytaskisshowninFigure10.
Environment. Allexperimentsareconductedonthesamemapgeneratedbytheproceduralcitygeneration
moduleinSimWorld. Toensurefairandefficientevaluation,graphicalrenderingisdisabledduringsimulation.
However,thephysicalsimulationandevaluationmodulesremainactivetopreserveenvironmentdynamicsand
taskfidelity.
Action Space. The task features a two-tiered action space: high-level actions decided by LLM agents and
low-levelactionsexecutedbytheSimWorldactionplanner. Ateachdecisionstep,theagentmaychoose: Bid
Order(offerapricetocompeteforaneworder),PickUpOrder(navigatetothepick-uppoint),DeliverOrder
(complete delivery at the destination), Share Order (publish the order for collaboration), Purchase Scooter
(purchaseascooterandequipittomovefaster). ThefullactionspaceisshowninTable3.
15

Avg. Avg. Avg. Avg. Avg.
Evaluation
Profit Success Rate Order Shared Rate Invalid Action Rate Delay Time
State Action History
A1 S1 A2 S2 Action: Moving Moving_forward
Logging Energe left: 89 Ture_left
Message Speed: 100 Moving_forward
TaskStateMachine Logging History BaSlatnactee: 2&5 $Act…ion History
Agent
Output: Next Activity Description Prompt:You are a delivery man in the city. Your goal is
Activity: go and pick up Order 1 maximize your profit.
Route Plan: I need first go to intersection 1, Your current state is: <Current State>
and then go straight, and then turn left … You have observations as <Muti-modal Observations>
Local Planner Action: pick_up(order1) LLMs Your action history is: <Action History>
balance balance balance
50-10=40$0+10=10$5-10 < 0$
Simulator
-10$ +10$ -10$
+ A x1 c tion - C x1 h ec + k e x1 r Multi-modal Observations
SimulatedScene
Scenes
Figure9: ArchitectureoftheDeliveryTask.
BaselineAgents. Weevaluatemultiplefoundationmodelsservingasthebackboneofdeliveryagents,including
Claude-3.5-Sonnet, DeepSeek-V3, GPT-4o, Gemini-2.5-Flash, and QWQ. The ReAct (Yao et al., 2022)
promptingframeworkisemployedtoexplicitlyseparatereasoningandactionselection.
Metrics. Alignedwiththeagent’shierarchicaldecision-making,wedesignathree-levelevaluationframework.
Overall performance is measured by total profit (the cumulative monetary gain the agent achieves over the
simulationperiod),whileoperationaleffectivenessisassessedusingordersuccessrate(theproportionoforders
thattheagentsuccessfullycompletesrelativetothetotalassignedorders),energyefficiency(theratioofenergy
consumedtorevenuegenerated),ordersharingcount(thenumberofsharingorders),andinvestmentcount(the
numberofstrategicinvestments).
3.2.MainResults
Foreachevaluation,wesample20agentscontrolledbythesamelanguagemodel,eachrunningfor5000simulation
steps. At each step, an agent issues two API requests, averaging around 7000 tokens per request. Based on
resultsinTable4,ourempiricalanalysisoverthreesimulationroundsrevealsdistinctoperationalbehaviorsacross
models.
DeepSeek-V3 (69.475 ± 16.772) and Claude-3.5-Sonnet (69.068 ± 20.685) achieved the highest mean
profits,withClaude-3.5-Sonnetalsoleadinginmeansuccessfulorders(2.733±1.102)andenergyefficiency
(0.5411±0.1981). Notably, these superior average outcomes were associated with substantial performance
variability,asreflectedintheirrespectivestandarddeviations.
Conversely,Gemini-2.5-Flash,whileattainingamoderatemeanprofitof42.423,exhibitedmarkedlymore
consistentprofitgenerationwithastandarddeviationof±3.103,andalsodemonstratedstabilityinsuccessful
orders (2.100±0.173). Extreme variability was evident in specific metrics for certain models; for instance,
sharingcountsforDeepSeek-Prover-V2(7.333±8.386)andClaude-3.5-Sonnet(11.333±8.386)showed
standarddeviationsexceedingtheirmeans,indicatinghighlyunpredictablebehaviorinthisaspect.
16

Case Study: Delivey Task - Multi-Agent Collaboration and Competition
Big-five Current State Reasoning Go picking up
Personality Personality: conscientious My current balance is -30$, I need order 1 Next w (1 ay 0 p 0 o , i 2 n 0 t: ) Pursuing
Balance: -30$ to make money by delivering
$0
LLM Current Order: order1 order. My currernt order is order1. Profit
Energy: 100 I need to pick it up. The next
$-30
Speed: 200cm/s waypoint is
Init Money
(100, 20)
Current State Reasoning
Personality: open my current balance is 100$. I am -$100 Making
Balance: 100$ open to try new method in work,
$100 Current Order: Null and buying a scooter can bring me Investment
Energy: 100 potential benefit. I will spend Speed x 5
$30 Speed: 200cm/s 100$ to do investement. Efficiency x 2
Current State Reasoning
Personality: extroverted I am an extroverted delivery man.
Balance: 0$ I am open to cooperate with 👍
Store1 Current Order: order3 others. I'll share my current order Collaborating
pos: (120, 150) Energy: 100 with others so that both of us can
Speed: 200cm/s benefit from it.
Order2
been as O si r g d n e e r1 d Is in bidding Current State Reasoning bid for 100$
Personality: neurotic I need to make money . I do not bid for 80$
Balance: 30$ take any order and order2 has the Competing
Current Order: Null lowest bid at 100$. I will bid
Customer1 Energy: 100 order2 for price 80$ to get this I have an order…
pos: (100, 20) Speed: 200cm/s order.
Figure10: DeliveryTask. Adeliveryscenariorequiringmulti-agentcollaborationandcompetition. Eachagent
isinitializedwithdistinctpersonalitiesandinternalstatesandcanacttogrow,thrive,andultimatelymaximizeits
earnings.
TheGPT-4o-minimodelconsistentlyyieldedzerovaluesacrossallmetrics(0.000±0.000),suggestingitdoes
not truly understand the goals well enough to make reasonable decisions based on the given instructions and
context.
Higherinvestmentstrategies,suchasthoseadoptedbyDeepSeek-V3(8.000±3.000)andClaude-3.5-Sonnet
(9.000±3.464), generally correlated with greater mean profit achievement but also with increased outcome
volatility. These findings underscore a prevalent trade-off between optimizing for peak average performance
metrics and ensuring consistent, predictable agent behavior, a critical consideration for robust deployment in
dynamicenvironments.
Takeaway: ModelPerformancesinMulti-agentTasks
Top-performing models such as DeepSeek-V3 and Claude-3.5-Sonnet achieve high average profits
but show greater variance, whereas Gemini-2.5-Flash demonstrates more consistent yet moderate
performance. GPT-4o-mini failed entirely across allmetrics. Overall, the results highlight a trade-off
betweenmaximizingaverageperformanceandensuringconsistent,reliablebehavior(Table4).
3.3.AblationStudy
Totakeastepdeeperonmulti-agentcollaborationandcompetition,weconductthreeablationexperiments. In
the Model Competition setting, we sample 24 agents controlled by 12 models, with each model managing
twoagentsover1000rounds. Inthisablationexperiment,westudyhowmodelsmakechoiceswithinahighly
competitiveenvironmentinordertomaximizetheirreturns;IntheEnvironmentConfigurationsetting,wevary
twoenvironmentconfigurations: theinitialfinancialbudgetandtheglobalordervolume. Foreachconfiguration,
we sample several stages from low to high to observe how agents’ behavior changes with the environment
conditions;InthePersonasetting,weusethemodelwiththebestperformancetocontroltheagentswithpersona
17

Table3: HierarchicalActionSpaceDesigninDeliveryTask. High-levelactionsaregiventolanguagemodels
tomakedecision,whichcorrespondtostrategicdecisions,whilelow-levelactionsareonlyexposedtolocalaction
plannermoduletoexecuteconcretemovementsandinteractions.
ActionLevel ActionName Description InvocationMethod
BidOrder OfferapricetoaneworderonplatformtocompetewithotherModelGenerations
PickUpOrder Navigatetothepick-uppointoforder
DeliverOrder Navigatetothedeliverypointandcompletetheorder
ShareOrder Publishtheorderformulti-modelgenerationcooperation
High-Level CancelShareOrder Cancelasharedorderthathasbeenpublished ModelGeneration
GotoMeet-point Navigatetothemeetpointforthesharedorde
PurchaseScooter Buyanduseascooter
PurchaseDrinks Buyconsumablestorestoreenergy
AdjustSpeed Adjusttravelspeed
MoveForward Basicmovementaction
Stop Stopmoving
Low-Level Rotate Adjustthefacingdirection ActionPlanner
ChangeSpeed Adjustwalkingspeed
DriveScooter Controlascooterformovement
Table4: PerformanceofModel-ControlledAgents. Metricsarereportedasmean(Avg)andstandarddeviation
(Std)overthree5000-stepsimulations. BoldindicatesthebestAvgpercolumn.
Model Profit SuccessfulOrders EnergyEfficiency SharingCount InvestmentCount
Avg Std Avg Std Avg Std Avg Std Avg Std
DeepSeek-V3 69.48 16.77 2.10 0.47 0.34 0.07 2.33 0.47 8.00 3.00
Claude-3.5-Sonnet 69.07 20.69 2.73 1.10 0.54 0.20 11.33 8.39 9.00 3.46
GPT-4o 43.91 14.16 1.63 0.43 0.30 0.06 0.67 0.47 4.67 0.47
Gemini-2.5-Flash 42.42 3.10 2.10 0.17 0.17 0.04 2.67 1.25 2.00 2.00
Gemini-2.0-Flash 28.72 12.04 1.53 0.58 0.11 0.03 0.67 0.47 0.67 1.00
Qwen3-32B 24.73 7.95 1.37 0.13 0.40 0.17 1.33 0.47 5.33 2.06
DeepSeek-Prover-V2 21.66 7.18 0.67 0.14 0.42 0.03 7.33 8.39 1.00 1.00
QwQ 17.31 4.07 0.87 0.20 0.41 0.20 0.33 0.47 3.33 2.52
GPT-4o-mini 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00
descriptioninprompts. Wesample20agents,assigneachpersonatotwoagents,andobservehowthesepersonas
shapetheagents’behaviorsanddecisionstrategies.
ModelCompetition. Tointensifyinter-agentcompetition,weconstraineachagenttohandleatmostoneorder
atatimeandsettheenvironment’shungerrateto0.9,ensuringahighdemandfordelivery. Ineachexperimental
session,24agentsarejointlycontrolledby12differentmodels,whereeachmodelgovernstwoagents. These
agentsactivelybidforordersinasharedenvironmentwiththegoalofmaximizingprofit. Eachsessionrunsfor
1000simulationsteps,andresultsareaveragedacrossthreerandomseeds.
As shown in Figure 11a, models exhibit distinct bidding behaviors. Notably, Claude-3.7-Sonnet,
Gemini-2.5-Flash and Gemini-2.0-Flash demonstrate broad bid price distributions, indicating a flexi-
blebiddingstrategy. Thisflexibilityincreasestheirchancesofwinningorderswhenincompetitionwithother
models. Incontrast,modelssuchasLLaMA-4-ScoutandLLaMA-3.2-11btendtousenarrowerbiddingranges,
whichlimitstheircompetitivenessandresultsinlowerwinrates.
Figure11bpresentsthehead-to-headcompetitionoutcomes. Deepseek-Prover-V2andQwen3-32Bachieve
thehighestwinratesagainstothermodels. Thisisprimarilybecausetheyoftenbidlowerprices,makingtheir
offersmorelikelytobeacceptedbytheplatform. Conversely,modelslikeGPT-4oandLLaMA-3.2-11btend
to place higher bids, reducing their success rate despite frequent participation. Models such as QwQ-32B and
GPT-4o-mini are less active overall, leading to fewer bids and lower order acquisition rates. This inactivity
contributestotheirdiminishedfinalprofit,asshowninTable4.
18

Takeaway: Multi-AgentCompetition
Models with flexible bidding strategies, like Claude-3.7-Sonnet and Gemini-2.5-Flash, achieve
higher order win rates, while those with narrow or high bids, like LLaMA-3.2-11b and GPT-4o, un-
derperform. Models that bid aggressively, such as Deepseek-Prover-V2 and Qwen3-32B, dominate
head-to-headcompetitions,whereasinactivemodelslikeGPT-4o-minifailtosecurebidsandprofits. QwQ
andGPT-4o-minishowminimalbiddingactivityandweaktaskparticipation(Figure11).
Bid Distribution by Model
qwen3-32b All Bids claude-3.7-sonnet
gemini-2.5-flash Successful Bids gemini-2.5-flash
gemini-2.0-flash
deepseek-v3 llama-4-scout
deepseek-prover-v2 claude-3.5-sonnet
deepseek-prover-v2 llama-3.2-11b deepseek-v3 llama-4-scout gpt-4o
claude-3.5-sonnet llama-3.2-11b
qwen3-32b
claude-3.7-sonnet
gpt-4o-mini
gpt-4o qwq-32b
(a)B g id em pr i i n c i e -2 d . i 0 st - r f i l b a u s t h ion 1 b 00 ymodel. 110 Theviol 1 i 2B0 n i p d l o P t r s ic il e l 13 u 0 stratethe 140 distribut 1 i 50 on claude g - e 3 m .7 g i - n e s i m - o 2 n i . n n 5 i e c l - - l l f t 2 a a l d . a m u 0 e s d - a e h f e - p l - a 4 s 3 s - e . h s 5 e c k - o s - u p o t d n ro e n v e e e p t r s - e v l e l 2 a k m - g v a p 3 - t 3 q - . 4 w 2 o - e 1 g n 1 p 3 b t - - 3 4 2 o b q -m w i q n - i 32b
ofbidpricesgeneratedbyeachmodel. Redpointsindicatebidsthatwere Opponent Model
successfullyaccepted.
ledoM
Head-to-Head Results with
competition between models
0 1 2 4 1 -2 1 2 -2-1 0 0
-1 0-13-12-3 9 7 7 -2 2 0 0 10
-213 0 -8 2 -2-1 3 2 -2 0 0
-412 8 0 4 4 -81013-7 0 0 5
-1 3 -2-4 0 -2-1 6 -1-2 1 0
2 -9 2 -4 2 0 2 4 3 -2 0 0 -1-7 1 8 1 -2 0 1 7 -2 0 1 0 -2-7-3-10-6-4-1 0 -1 0 0 0
2 2 -2-131 -3-7 1 0 -3 0 0 5
1 -2 2 7 2 2 2 0 3 0 0 0
0 0 0 0 -1 0 0 0 0 0 0 0 10
0 0 0 0 0 0 -1 0 0 0 0 0
)-(
sessoL
/ )+(
sniW
(b)Win-LossMatrixofModelCompetition.
Figure11: BiddingBehaviorandEvaluationResults. (a)Lowerbidpricesmayincreasethelikelihoodofbeing
assignedanorder,butoftencomeatthecostofreducedprofitmargins. (b)Highervaluesinredrepresentmore
wins;lowervaluesinblueindicatemorefrequentlossesinpairs.
EnvironmentConfiguration. Wefurtherinvestigatehowdifferentenvironmentalconfigurationsimpactagent
behaviorandoverallperformance. Specifically,weexploretwokeyfactors: theglobalorderavailabilityandthe
agents’initialfinancialendowment. Foreachfactor,weconductaseriesofcontrolledexperimentstoobservehow
variationsaffectagents’actiondistributions.
As shown in Figure 12a, when the total number of available orders increases, agents tend to perform fewer
pickupanddeliveryactionsandinsteadchoosethedo nothingactionmorefrequently. Thissuggeststhatin
resource-richenvironments,agentsaremoreinclinedtoconserveenergyandavoidunnecessaryeffort,opting
to wait for optimal opportunities rather than actively pursue deliveries. Conversely, in low-resource settings,
agents are more motivated to engage in delivery tasks to secure profits. Additionally, as resource abundance
increases,agentsdemonstrateahighertendencytoinitiateandcompleteshareddeliveries,likelyasameansto
reduceenergycoststhroughcollaboration.
Figure12billustratestheimpactofagents’initialmonetaryresources. Asinitialcapitalincreases, agentsare
lessreliantonaggressivebiddingandinsteadprioritizeactionssuchasorderpickup. Whenfundsarelimited,
competitionintensifies,leadingtomorefrequentbiddingbehavior. Furthermore,withsufficientinitialcapital,
agentsaremorewillingtoinvestininfrastructure,suchaspurchasingascooter,whichenhancestheirlong-term
deliveryefficiency.
Takeaway: ResourceandDecision-MakingStrategy
Orderresourcescarcityincreasesagentcompetitivenessandtaskurgency. Sufficientagentinitialmoney
leadstomorerelaxed,profit-insensitivebehavior(Figure12).
Theseobservationssuggestthatagentsaremorecompetitiveandtask-driveninresource-constrainedenvironments.
In contrast, resource-rich conditions reduce the urgency to complete tasks and generate immediate profits.
Importantly,agentsarealsomorelikelytoengageinactionsthatinvolveupfrontcostsbutpromiselong-term
benefits—suchasinvestmentandshareddelivery—providedtheyhavethefinancialcapacityandenoughorders
takentodoso.
19

DO_NOTHING PICK_UP_ORDER BUY_BEVERAGE GO_TO_MEETING_POINT BUY_BIKE
BID_ORDER DELIVER_ORDER OPEN_SHARED_ORDER CHANGE_WALKING_SPEED
   
   
 
                       
Total Order Quantity
tnuoC
Main Actions
 
 
 
 
                       
Total Order Quantity
tnuoC
Auxiliary Actions
600
400
200
0 -30 0 30 60 90 120
Agent Initial Money
(a)EffectofOrderQuantity
tnuoC
Main Actions
15
10
5
0 -30 0 30 60 90 120
Agent Initial Money
tnuoC
Auxiliary Actions
(b)EffectofInitialMoney
Figure12: ActionDistributionacrossEnvironmentalSettings. (a)showshowglobalorderquantityaffects
agentbehavior;(b)showstheeffectofinitialmoneyonactionselection.
InfluenceofPersona. Personalitytraitssignificantlyaffectthedecision-makingandperformanceofdelivery
agents. AsshowninFigure13,agentswithhigherConscientiousnesstendtoexhibitalowerfrequencyofbidding
actions,ahigherfrequencyoftask-completionactions(e.g.,pickinguporders),andachieveahigherbidwinrate.
Thissuggeststhatconscientiousagentsprioritizetaskcompletionoverstrategiccompetition. Agentswithhigher
Agreeablenessarelesslikelytoremaininactive(i.e.,performdo nothingactions)andtendtoachievehigher
bidwinrates. Conversely,agentswithlowerAgreeablenessdisplayhigherinactivityandnarrowerbiddingprice
ranges,limitingtheircompetitiveness. Interestingly,agentswithhigherOpennessexhibitreducedengagementin
deliverytasks,possiblybecausetheyexplorecompetitiveorunconventionalbiddingstrategiesthatdivertattention
fromtaskexecution.
Trait vs Win Rate/Action Proportion
1.00
Openness 0.02 0.38 -0.10-0.70-0.44-0.04 0.51 0.9 0.75 0.8
Conscientiousness 0.65 -0.64 0.66 0.08 0.44 0.28 -0.42 0.50 0.7 0.6 0.25
0.5
Extraversion 0.25 -0.03 0.15 -0.37 0.00 -0.01 0.53 0.00 0.0 C0.2onsci0e.4ntiou0.s6ness0.8
0.25
Agreeableness 0.63 0.34 -0.20 0.01 -0.35-0.70 0.00
0.50
Neuroticism 0.08 -0.11 0.19 0.04 -0.07-0.08-0.39 0.75
Bid W Bid i P n O i R c r k a d t U e e r p D C O o e r u l d i n v e e t r r B C O u o y r u d n B e t e r v C e o r D u a o g n t e N C ot o h u in n B g t u C y o B u i n k t e Count 1.00
(a)Pearsoncorrelationb/wBigFivepersonalitytraitsand
agentbehaviors.
redrO
diB
Conscientiousness
vs Bid Order
r = -0.64 0.07 RMSE = 0.096 0.06 0.05
0.04 0.03 0.02
0.01
0.00 0.2 Ag0.4reeabl0.6eness0.8 1.0
gnihtoN
oD
Agreeableness
vs Do Nothing
r = -0.70 0.175 RMSE = 0.016 0.150 0.125
0.100 0.075 0.050
0.025
0.000 0.1 0.2 0.3 O0.4pen0.5ne0s.6s 0.7 0.8 0.9
redrO
revileD
Openness vs
Deliver Order
r = -0.70 RMSE = 0.035
0.10
0.09
0.08
0.07 0.06 0.05 0.04 0.030.0 C0.2onsci0e.4ntiou0.s6ness0.8
etaR
niW diB
Conscientiousness
vs Bid Win Rate
0.10
0.09
0.08
0.07 0.06 r = 0.65 0.05 RMSE = 0.017 0.04 0.03 0.2 Ag0.4reeabl0.6eness0.8 1.0
etaR
niW diB
Agreeableness
vs Bid Win Rate
0.40
0.35
0.30
0.25 0.20 RMSE r = = 0 0 .0 .6 1 3 7 0 0 0 . . . 0 1 1 5 0 5 0.0 C0.2onsci0e.4ntiou0.s6ness0.8
redrO
pU kciP
Conscientiousness
vs Pick Up Order
r = 0.66 RMSE = 0.076
(b)LinearRegressionRevealsStrongCorrelationsbetweenBehaviorsand
PersonaTraits.
Figure13: PersonaInfluenceonAgentPerformanceandBehavior. (a)AgentswithhigherAgreeablenessare
lesslikelytoremaininactiveandtendtoachievehigherbidwinrates. Conversely,agentswithloweragreeable–
nessdisplayhigherinactivityandnarrowerbiddingpriceranges,limitingtheircompetitiveness. (b)Theresults
demonstratethatagentbehaviorsaretightlyalignedwiththeircorrespondingpersonaattributes,highlightingthe
effectivenessoftrait-drivenbehaviormodeling.
Takeaway: ImpactofPersonainMulti-agentInteraction
Agent personalities shape strategic tendencies: conscientious agents prioritize task fulfillment, while
opennessandagreeablenessmodulatecompetitivenessandinactivity(Figure13).
4. Related Works
Simulations have played a crucial role in constructing environments for training and evaluating autonomous
agents. Text-basedsimulatorsoftenemphasizesocialscenarios,suchashumaninteraction(Yangetal.,2024),
20

dailyactivities(Parketal.,2023),andrelationalpolarization(Piaoetal.,2025). Popularembodiedsimulators
supportabroaderrangeofapplications,particularlyinembodiedAIresearchand2D/3Dscenesynthesis(Lietal.,
2025a). However,mostembodiedsimulatorsremainconstrainedtoeitherindoorhouseholdenvironments(e.g.,
AI2-THOR(Kolveetal.,2017),Habitat(Puigetal.,2023),iGibson(Lietal.,2021))oroutdoordrivingscenarios
(e.g., CARLA (Dosovitskiy et al., 2017), MetaDrive (Li et al., 2022)) or natural scenes (e.g., AirSim (Shah
etal.,2017)). Mostofthesesimulators(Dosovitskiyetal.,2017;Puigetal.,2023;Lietal.,2021;Shahetal.,
2017;Wangetal.,2024a;Gaoetal.,2024)relyonalimitednumberofmanuallycraftedscenes,whichhinders
scalability and diversity. Some platforms, such as MetaUrban (Wu et al., 2025), MetaDrive (Li et al., 2022),
AI2-THOR (Kolve et al., 2017) and Genesis (Authors, 2024), introduce rule-based procedural generation to
alleviatethisissue. Nonetheless,existingembodiedsimulatorstypicallylacksupportfordynamicmulti-agent
interactionsincomplexdiverseenvironments.
Recentadvancementshaveintroducedlarge-scale,language-drivensocialsimulatorscapableofmodelingcomplex
societalbehaviors. OASIS(Yangetal.,2024)simulatesuptoonemillionLLM-poweredagentsinteractingon
socialmediaplatforms,capturingphenomenasuchasinformationdiffusion,echochambers,andpolarization.
Casevo(Jiangetal.,2024)integrateschain-of-thoughtreasoning,retrieval-augmentedgeneration,andcustomizable
memory mechanisms to simulate intricate social phenomena and decision-making processes. MineLand (Yu
etal.,2024)offersamulti-agentMinecraftenvironmentwhereagents,drivenbyphysiologicalneedsandlimited
multimodalperception, engagein collectivebehaviors, fosteringecologicalanddetailedsimulations. Project
sid(ALetal.,2024)furtheradvancesthislandscapebydeployingalargenumberofAIagentswithinaMinecraft
environment to explore the emergence of AI civilizations. VirtualCommunity (Zhou et al., 2025) leverages
Genesissimulatortoconductcommunityinfluencetaskinoutdoor,multi-agentscenes. Thesesimulationplatforms
demonstrateagents’capabilitiestoformcomplexsocialstructures,economies,andgovernancesystems,providing
insightsintolarge-scalesocietalsimulationsandagenticorganizationalintelligence.
Noneoftheexistingsimulatorsareexplicitlydesignedtosupportdynamic,multi-agentinteractionsinlarge-scale
outdoor and other diverse environments with both realistic rendering and physical simulation. SimWorld
addressesthislimitationbyprovidingascalable,procedurallygenerated,andLLM/VLM-compatibleplatform
that enables multi-agent collaboration and competition, language-grounded interactions, and comprehensive
benchmarkingforembodiedintelligence.
Another emerging direction in world simulation involves end-to-end neural world models, which generate
interactivevideopredictionsconditionedonenvironmentstates,agentactions,andhigh-levelcontrols(Xiangetal.,
2024;DeepMind,2025;Xiangetal.,2025). Recentsystemscansimulateshortvideorolloutsor3D-consistent
scenesusinglearneddynamics,offeringaflexiblealternativetotraditionalengine-basedsimulation. Ontheother
hand,SimWorld,builtontheUnrealEngine,provideshigh-fidelity,physicallygrounded,anddeterministically
controllable environments capable of supporting thousands to even millions of interacting agents at scale.
Moreover,becauseSimWorldsupportsdiverse,high-qualityproceduralandhandcraftedscenes,itcanserveas
apowerfulgeneratoroflarge-scaletrainingdata,offeringarichsourceofsupervisedtrajectories,multi-agent
interactions,andphysicallyrealisticrolloutsthatcanbeusedtotrainandimproveneuralworldmodels.
References
AL,A.,Ahn,A.,Becker,N.,Carroll,S.,Christie,N.,Cortes,M.,Demirci,A.,Du,M.,Li,F.,Luo,S.,Wang,
P.Y.,Willows,M.,Yang,F.,andYang,G.R. Projectsid: Many-agentsimulationstowardaicivilization,2024.
URLhttps://arxiv.org/abs/2411.00114.
Anthropic. Claude’s extended thinking, 2025. URL https://www.anthropic.com/research/
visible-extended-thinking. Accessed: 2025-05-14.
Authors,G. Genesis: Agenerativeanduniversalphysicsengineforroboticsandbeyond,December2024. URL
https://github.com/Genesis-Embodied-AI/Genesis.
Brohan,A.,Chebotar,Y.,Finn,C.,Hausman,K.,Herzog,A.,Ho,D.,Ibarz,J.,Irpan,A.,Jang,E.,Julian,R.,
etal. Doasican,notasisay: Groundinglanguageinroboticaffordances. InConferenceonrobotlearning,pp.
287–318.PMLR,2023.
21

DeepMind. Genie 3: A new frontier for world models. https://deepmind.google/blog/
genie-3-a-new-frontier-for-world-models/,2025. Accessed: 2025-11-27.
Dosovitskiy,A.,Ros,G.,Codevilla,F.,Lopez,A.,andKoltun,V. CARLA:Anopenurbandrivingsimulator. In
Proceedingsofthe1stAnnualConferenceonRobotLearning,pp.1–16,2017.
Driess,D.,Xia,F.,Sajjadi,M.S.,Lynch,C.,Chowdhery,A.,Wahid,A.,Tompson,J.,Vuong,Q.,Yu,T.,Huang,
W.,etal. Palm-e: Anembodiedmultimodallanguagemodel. 2023.
Fan,L.,Wang,G.,Jiang,Y.,Mandlekar,A.,Yang,Y.,Zhu,H.,Tang,A.,Huang,D.-A.,Zhu,Y.,andAnandkumar,
A. Minedojo: Building open-ended embodied agents with internet-scale knowledge. Advances in Neural
InformationProcessingSystems,35:18343–18362,2022.
FaramaFoundation. Gymnasium. https://gymnasium.farama.org/,2023. Accessed: 2025-11-27.
Gao,C.,Zhao,B.,Zhang,W.,Mao,J.,Zhang,J.,Zheng,Z.,Man,F.,Fang,J.,Zhou,Z.,Cui,J.,etal.Embodiedcity:
Abenchmarkplatformforembodiedagentinreal-worldcityenvironment. arXivpreprintarXiv:2410.09604,
2024.
Guo,D.,Yang,D.,Zhang,H.,Song,J.,Zhang,R.,Xu,R.,Zhu,Q.,Ma,S.,Wang,P.,Bi,X.,etal. Deepseek-r1:
Incentivizingreasoningcapabilityinllmsviareinforcementlearning. arXivpreprintarXiv:2501.12948,2025.
Ha, A. Google’s gemini has beaten pokémon blue (with a little
help). TechCrunch, 2025. URL https://techcrunch.com/2025/05/03/
googles-gemini-has-beaten-pokemon-blue-with-a-little-help/. Accessed: 2025-05-14.
Hao, S., Gu, Y., Ma, H., Hong, J. J., Wang, Z., Wang, D. Z., and Hu, Z. Reasoning with language model is
planningwithworldmodel. arXivpreprintarXiv:2305.14992,2023.
Ho,M.,Si,C.,Feng,Z.,Yu,F.,Yang,Y.,Liu,Z.,Hu,Z.,andQin,L. Arcmemo: Abstractreasoningcomposition
withlifelongllmmemory. arXivpreprintarXiv:2509.04439,2025.
Hu, Z. and Shu, T. Language models, agent models, and world models: The law for machine reasoning and
planning. arXivpreprintarXiv:2312.05230,2023.
Hunyuan3D,T. Hunyuan3d2.0: Scalingdiffusionmodelsforhighresolutiontextured3dassetsgeneration,2025.
Jain,H.andBabel,P. Acomprehensivesurveyofpidandpurepursuitcontrolalgorithmsforautonomousvehicle
navigation. arXivpreprintarXiv:2409.09848,2024.
Jiang,Z.,Shi,Y.,Li,M.,Xiao,H.,Qin,Y.,Wei,Q.,Wang,Y.,andZhang,Y. Casevo: Acognitiveagentsand
socialevolutionsimulator. arXivpreprintarXiv:2412.19498,2024.
Kolve,E.,Mottaghi,R.,Han,W.,VanderBilt,E.,Weihs,L.,Herrasti,A.,Deitke,M.,Ehsani,K.,Gordon,D.,Zhu,
Y.,etal. Ai2-thor: Aninteractive3denvironmentforvisualai. arXivpreprintarXiv:1712.05474,2017.
Li,C.,Xia,F.,Martín-Martín,R.,Lingelbach,M.,Srivastava,S.,Shen,B.,Vainio,K.,Gokmen,C.,Dharan,G.,
Jain,T.,etal. igibson2.0: Object-centricsimulationforrobotlearningofeverydayhouseholdtasks. arXiv
preprintarXiv:2108.03272,2021.
Li, C., Zhang, R., Wong, J., Gokmen, C., Srivastava, S., Martín-Martín, R., Wang, C., Levine, G., Ai, W.,
Martinez,B.,etal. Behavior-1k: Ahuman-centered,embodiedaibenchmarkwith1,000everydayactivities
andrealisticsimulation. arXivpreprintarXiv:2403.09227,2024.
Li,Q.,Peng,Z.,Feng,L.,Zhang,Q.,Xue,Z.,andZhou,B. Metadrive: Composingdiversedrivingscenariosfor
generalizablereinforcementlearning. IEEEtransactionsonpatternanalysisandmachineintelligence,45(3):
3461–3475,2022.
Li,X.,Song,R.,Xie,Q.,Wu,Y.,Zeng,N.,andAi,Y. Simworld: Aunifiedbenchmarkforsimulator-conditioned
scenegenerationviaworldmodel. arXivpreprintarXiv:2503.13952,2025a.
22

Li, Z., Xie, Y., Shao, R., Chen, G., Jiang, D., and Nie, L. Optimus-2: Multimodal minecraft agent with
goal-observation-actionconditionedpolicy. InProceedingsoftheComputerVisionandPatternRecognition
Conference(CVPR),pp.9039–9049,June2025b.
Liu,S.etal. Odyssey: Empoweringminecraftagentswithopen-worldskills. arXivpreprintarXiv:2407.15325,
2024.
Long,Q.,Li,Z.,Gong,R.,Wu,Y.N.,Terzopoulos,D.,andGao,X. Teamcraft: Abenchmarkformulti-modal
multi-agentsystemsinminecraft. arXivpreprintarXiv:2412.05255,2024.
Park,J.S.,O’Brien,J.,Cai,C.J.,Morris,M.R.,Liang,P.,andBernstein,M.S. Generativeagents: Interactive
simulacraofhumanbehavior. InProceedingsofthe36thannualacmsymposiumonuserinterfacesoftware
andtechnology,pp.1–22,2023.
Phiresky. procedural-cities. https://github.com/phiresky/procedural-cities,2024.
Piao,J.,Yan,Y.,Zhang,J.,Li,N.,Yan,J.,Lan,X.,Lu,Z.,Zheng,Z.,Wang,J.Y.,Zhou,D.,etal. Agentsociety:
Large-scalesimulationofllm-drivengenerativeagentsadvancesunderstandingofhumanbehaviorsandsociety.
arXivpreprintarXiv:2502.08691,2025.
Puig,X.,Undersander,E.,Szot,A.,Cote,M.D.,Yang,T.-Y.,Partsey,R.,Desai,R.,Clegg,A.W.,Hlavac,M.,
Min,S.Y.,etal. Habitat3.0: Aco-habitatforhumans,avatarsandrobots. arXivpreprintarXiv:2310.13724,
2023.
Qiu, W., Zhong, F., Zhang, Y., Qiao, S., Xiao, Z., Kim, T. S., and Wang, Y. Unrealcv: Virtual worlds for
computer vision. In Proceedings of the 25th ACM International Conference on Multimedia, MM ’17, pp.
1221–1224,NewYork,NY,USA,2017.AssociationforComputingMachinery. ISBN9781450349062. doi:
10.1145/3123266.3129396. URLhttps://doi.org/10.1145/3123266.3129396.
Shah,S.,Dey,D.,Lovett,C.,andKapoor,A. Airsim: High-fidelityvisualandphysicalsimulationforautonomous
vehicles. In Field and service robotics: Results of the 11th international conference, pp. 621–635. Springer,
2017.
Wang, G., Xie, Y., Jiang, Y., Mandlekar, A., Xiao, C., Zhu, Y., Fan, L., and Anandkumar, A. Voyager: An
open-endedembodiedagentwithlargelanguagemodels. arXivpreprintarXiv:2305.16291,2023.
Wang,H.,Chen,J.,Huang,W.,Ben,Q.,Wang,T.,Mi,B.,Huang,T.,Zhao,S.,Chen,Y.,Yang,S.,etal. Grutopia:
Dreamgeneralrobotsinacityatscale. arXivpreprintarXiv:2407.10943,2024a.
Wang,Y.,Gao,Y.,Chen,X.,Jiang,H.,Li,S.,Yang,J.,Yin,Q.,Li,Z.,Li,X.,Yin,B.,etal. Memoryllm: Towards
self-updatablelargelanguagemodels. arXivpreprintarXiv:2402.04624,2024b.
White,I.,Nottingham,K.,Maniar,A.,Robinson,M.,Lillemark,H.,Maheshwari,M.,Qin,L.,andAmmanabrolu,
P. Collaborating action by action: A multi-agent llm framework for embodied reasoning. arXiv preprint
arXiv:2504.17950,2025.
Wu,W.,He,H.,He,J.,Wang,Y.,Duan,C.,Liu,Z.,Li,Q.,andZhou,B. Metaurban: Anembodiedaisimulation
platformforurbanmicromobility. InternationalConferenceonLearningRepresentation,2025.
Xiang,J.,Liu,G.,Gu,Y.,Gao,Q.,Ning,Y.,Zha,Y.,Feng,Z.,Tao,T.,Hao,S.,Shi,Y.,etal. Pandora: Towards
generalworldmodelwithnaturallanguageactionsandvideostates. arXivpreprintarXiv:2406.09455,2024.
Xiang,J.,Gu,Y.,Liu,Z.,Feng,Z.,Gao,Q.,Hu,Y.,Huang,B.,Liu,G.,Yang,Y.,Zhou,K.,etal. PAN:Aworld
modelforgeneral,interactable,andlong-horizonworldsimulation. arXivpreprintarXiv:2511.09057,2025.
Xing,E.,Deng,M.,Hou,J.,andHu,Z. Critiquesofworldmodels. arXivpreprintarXiv:2507.05169,2025.
Yang,Z.,Zhang,Z.,Zheng,Z.,Jiang,Y.,Gan,Z.,Wang,Z.,Ling,Z.,Chen,J.,Ma,M.,Dong,B.,etal. Oasis:
Openagentssocialinteractionsimulationsononemillionagents. arXivpreprintarXiv:2411.11581,2024.
23

Yao,S.,Zhao,J.,Yu,D.,Du,N.,Shafran,I.,Narasimhan,K.R.,andCao,Y. React: Synergizingreasoningand
actinginlanguagemodels. InTheeleventhinternationalconferenceonlearningrepresentations,2022.
Yu,X.,Fu,J.,Deng,R.,andHan,W. Mineland: Simulatinglarge-scalemulti-agentinteractionswithlimited
multimodalsensesandphysicalneeds. arXivpreprintarXiv:2403.19267,2024.
Zhong,F.,Wu,K.,Wang,C.,Chen,H.,Ci,H.,Li,Z.,andWang,Y. Unrealzoo: Enrichingphoto-realisticvirtual
worldsforembodiedai. InProceedingsoftheIEEE/CVFInternationalConferenceonComputerVision,pp.
5769–5779,2025.
Zhou,Q.,Zhang,H.,Lin,X.,Zhang,Z.,Chen,Y.,Liu,W.,Zhang,Z.,Chen,S.,Fang,L.,Lyu,Q.,etal. Virtual
community: Anopenworldforhumans,robots,andsociety. arXivpreprintarXiv:2508.14893,2025.
24
