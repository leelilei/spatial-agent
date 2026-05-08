Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_round3_candidates/R3-01_MineLand_2024.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:57:59+00:00
- page_count: 33
- status: ok
- text_char_count: 88316

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- MineLand Simulator (page 3)
  - Architecture (page 3)
  - Observation Space (page 4)
  - State Space (page 4)
  - Action Space (page 4)
  - Communication (page 5)
- MineLand Benchmark Suite and Dataset (page 6)
  - Programmatic Task (page 6)
  - Creative Task (page 6)
  - Hybrid Task (page 6)
- Alex Agent (page 7)
- Experiments (page 7)
  - Experiments of Simulators Performance (page 7)
  - Experiments of Social Dynamics (page 8)
  - Experiments of Construction Tasks (page 8)
  - Experiments of Stage Performance Tasks (page 8)
  - Experiments of Multi-Agent Cooperation (page 9)
  - Experiments of Multitasking (page 9)
- Conclusion (page 10)
- Related Work (page 14)
  - Multi-Agent Simulator (page 14)
  - Multi-Agent Simulator w.r.t Minecraft (page 15)
  - AI Agent with LLMs and VLMs (page 15)
- Broader Impact (page 15)
- Details of MineLand Simulator (page 16)
  - Architecture (page 16)
  - State Space (page 16)
  - Action Space (page 17)
  - Supporting up to 100 Agents (page 17)
- Details of MineLand Benchmark Suite (page 17)
- Details of Alex (page 18)
  - Memory Component (page 19)
  - Hierarchical Planning Component (page 20)
  - Action Module (page 20)
  - Multitasking Mechanism (page 20)
- Details of Hyper-Parameters (page 21)
- Experiments of Minecraft Simulator Performance Comparison (page 21)
- Experiments of Multimodal Observation (page 22)
- Experiments of Reinforcement Learning Agent (page 23)
- Experiments of Limited Senses (page 24)
- Experiments of Physical Needs (page 24)
- Experiments of Single Agent (page 25)
- Experiments of Construction Tasks (page 25)
- Experiments of Stage Performance Tasks (page 26)
- Experiments of Simulating Sociological Phenomena (page 27)
  - Experiments of Simulating Conformity Phenomena (page 27)
  - Experiments of Simulating Personality Traits (page 28)
- Experiments of Comparing Different VLMs and LLMs (page 28)
- Evaluation Metrics For Construction Tasks (page 29)
- Evaluation Metrics For Stage Performance Tasks (page 29)
- Limitations (page 29)
- Prompts (page 31)

Markdown Content:

MineLand: Simulating Large-Scale Multi-Agent
Interactions with Limited Multimodal Senses and
Physical Needs
(cid:66)
XianhaoYu∗1 JiaqiFu∗1 RenjiaDeng∗1 WenjuanHan 1
1BeijingJiaotongUniversity
wjhan@bjtu.edu.cn
Abstract
WhileVision-LanguageModels(VLMs)holdpromisefortasksrequiringextensive
collaboration,traditionalmulti-agentsimulatorshavefacilitatedrichexplorations
ofaninteractiveartificialsocietythatreflectscollectivebehavior. However,these
existingsimulatorsfacesignificantlimitations. Firstly,theystrugglewithhandling
large numbers of agents due to high resource demands. Secondly, they often
assume agents possess perfect information and limitless capabilities, hindering
the ecological validity of simulated social interactions. To bridge this gap, we
propose a multi-agent Minecraft simulator, MineLand, that bridges this gap by
introducingthreekeyfeatures: large-scalescalability,limitedmultimodalsenses,
and physical needs. Our simulator supports 64 or more agents. Agents have
limitedvisual, auditory, andenvironmentalawareness, forcingthemtoactively
communicate and collaborate to fulfill physical needs like food and resources.
Additionally,wefurtherintroduceanAIagentframework,Alex,inspiredbymul-
titaskingtheory,enablingagentstohandleintricatecoordinationandscheduling.
Ourexperimentsdemonstratethatthesimulator, thecorrespondingbenchmark,
and the AI agent framework contribute to more ecological and nuanced collec-
tive behavior. The source code of MineLand and Alex is openly available at
https://github.com/cocacola-lab/MineLand.
1 Introduction
Multi-agentsimulatorshavefacilitatedrichexplorationsofaninteractiveartificialsocietythatreflects
collectivebehavior. FromsandboxgamessuchasSmallville[40]tovirtualenvironments[4,32,18],
researchersandpractitionershavebeenbuildingopen-worldsimulatorsthatcancarrymulti-agent
behaviors and navigate complex human relationships for decades. Especially with the advent of
Large Language Models (LLMs) and Vision-Language Models (VLMs), numerous multi-agent
simulatorsbasedonthesetechnologieshavebeenattheforefrontinvariousfields,fromfundamental
research to practical applications, such as watch-and-help (WAH) task [65], Smallville [40] and
Overcook games [18]. However, conventional multi-agent open-world simulators, valuable for
exploringcollectivebehavior,sufferfromlimitations(detailedcomparisoninTable1). Firstly,they
strugglewithlarge-scalescenariosduetotheenormousresourceconsumptionrequiredforlarge-
scale agents. Secondly, they are often under the assumption of perfect information and limitless
capabilities. Theseidealizedworldsdivergesharplyfromthemessyrealityofhumaninteraction.
∗Equalcontribution.Theorderofauthorswasdeterminedrandomly.
(cid:66)Correspondingauthor.
Preprint.Underreview.
4202
yaM
32
]LC.sc[
2v76291.3042:viXra

Figure1: ApanoramicviewofonesceneinMineLand,consistingofmultipleAIagents. Subfigure
3&6showinteractionsdemonstratingcooperationandcompetitionamongseveralagents. Subfigure
5&2&4showcasesthescenarioswherethelimitedsenses,physicalneeds,andmultitaskingmecha-
nismreflect. InSubfigure1,anagentisperformingacreativetasknamedExploration. Twoagentsin
theleftcaveofSubfigure5cooperatetofinishaprogrammaticminingtask,whileagentsinSubfigure
3arecarryingoutbuildingconstruction,whichisahybridtask.
Thisgapbetweenexistingsimulatorsandtherealworldhinderstheecologicalvalidityandrichness
ofsocialinteraction[21].
Tobridgethisgap,weproposeMineLand(Section2),amulti-agentMinecraftsimulator,asshown
inFigure1, byintroducingthreekeyfeatures: large-scalescalability, limitedmultimodalsenses,
and physical needs. First and foremost, the essence of the MineLand’s features is the ability to
handlethemaximumnumberofagents. Comparedtotwo-agentWAH,single-agentMineDojo[16]
andtwenty-five-agentSmallville[40],ourMineLandenablestheutilizationofsixty-fouroreven
moreagentsonthemainstreamconsumerdesktopPC.Secondly,oursimulatoroperatesunderthe
human-likeassumption[21]thatagentspossessonlylimitedmultimodalsenses: partiallyobservable
environments, eco-centric perspective, and limited visual and auditory senses. This mirrors real-
lifesocialinteractions,wherevisibilityandaudibilitycanbeaffectedbyfactorssuchasdistance,
terrain,andenvironment. Theselimitationsrestrictinformationaccess,forcingagentstoactively
communicatetocompensateforsensorydeficiencies. Thirdly,weintegraterealisticphysicalneeds
into agents. Agents require fundamental physical needs, such as food, sustenance, and resource
management,whichaddsatime-basedaspecttotheirdailyroutineprocedures. Thisnecessitates
collaborationandcompetitionforresources, mirroringthecomplexinterplayofcooperationand
self-interestobservedinhumansocieties[15,1]. Byincorporatingthesethreefeatures,oursimulator
fosterstheemergenceofdynamicandecologicallyvalidmulti-agentinteractions1.
Asanopen-worldmulti-agentsimulator,MineLandisanexcellentplatformforbenchmarkingmulti-
agentcapabilities(Section3), hencewecrowd-sourceddatasetstofullyevaluatethepotentialof
LLM-orVLM-basedmulti-agents. Forpreviouslyexistingtasks,programmatictasks(e.g.,harvest,
techtree,combattasks)andcreativetasks(e.g.,survivaltasks),weofferasignificantlyexpandedtask
quantity. Specifically,wecrowd-sourced4499programmatictasksand1536creativetasks,which
is2timescomparedtoMineDojo. Interestingly,weintroduceanovel“hybridtask”categorythat
combinesthefeaturesofprogrammatictasksandcreativetasks. ConstructionandStagePerformance
tasksexemplifythisnewcategory,bringingthetotalto18hybridtasks. Additionally,thesimulator
1Ecological validity refers to interactions between agents within a simulated environment that closely
resemble real-world human interactions. For example, actions are situated, adaptive, and environmentally
constrained.
2

Table1: Partofthecomparisonwithrelatedpopularplatformsorprojects. ThefulltableisinTable7.
MaxAgents: TheapproximatemaximumnumberofagentssupportedonasinglePC(SeeSection
5.1fordetails). Human: WhetherthesimulatorallowshumanstodirectlyinteractwithAIagents.
PlanasAction: Whetheragentscangenerateplansinaspecificformat(e.g.,code)thatthesimulator
interprets and executes directly as actions. Sociological Experiments: Whether the simulator is
designedtofacilitatethestudyofsocialphenomenaandemergentbehaviorinmulti-agentsystems.
Sociological
Simulator MaxAgents Human PlanasAction NumberofTasks
Experiments
MineLand 64+ ✓ ✓ ✓ 6000+
MineDojo[16] 1 - - - 3000+
MineRLv1.0[3] 1 - - - 5
MarLÖ[42] 8 ✓ - - 14
Malmo[27] 8 ✓ - - -
Voyager[57] 1 ✓ ✓ - -
Smallville[40] 25 - ✓ ✓ -
allowscustomizationofthenumberofagentsandfacilitatesexplorationthroughtwodistinctmodes:
cooperativeandcompetitive.
Inaddition,wedesignanAIagentframework-Alex-inspiredbyMultitaskingtheoryfromthe
Cognitionfield[53](Section4). Alexallowsforsimultaneouslyexecutingintricatecoordination
andschedulingwithmultipletasks. WiththisAIagentframework,wehaveobtainedthefollowing
intriguing findings: (1) Our simulator shows the feature of large-scale scalability (supporting 64
agents, x8timesthanbefore, (§5.1), limitedmultimodalsenses(§J)andphysicalneeds(§K).By
incorporatingthesethreefeatures,oursimulatorfosterssocialdynamics(§5.2&§O).(2)Ourbench-
markanddatasetsarechallenging(§5.3&§5.4). (3)Ouragentsworktogethermoreeffectively,witha
reducedworkloadperagent(§5.5),andthemultitaskingmechanismforagentsisbeneficial(§5.6).
Insummary,ourcontributionsarethree-fold: thesimulator,benchmark,andAIagent. Withthese
contributions,wepushtheboundariesofmulti-agentsimulationbybridgingthegapbetweenvirtual
agentsandlarge-scalereal-worldhumans. ThisnotonlyadvancesunderstandingofAImulti-agents
butalsoholdspotentialforapplicationsinhumandynamics,socialpsychology,robotics,andgame
design. Weanticipatethatthisworkwillserveasausefulfoundationforthecommunitytocreate
newalgorithmsandmakeprogressinthefieldofembodiedAImulti-agentsystems.
2 MineLandSimulator
Conventional multi-agent open-world simulators suffer from the gap between virtual agents and
large-scalereal-worldhumans. Tobringthisgap, weproposeMineLandwiththreekeyfeatures:
large-scalescalability,limitedmultimodalsenses,andphysicalneeds. Thissectiondescribesthe
designandimplementationofthissimulator,focusingonthearchitecture,observationspace,state
space,actionspaceandcommunication. Duringintroducingthedesign,wewillhighlighttechniques
thatbringthethreekeyfeaturesandomitthepartssimilartootherMinecraftsimulators.
2.1 Architecture
MineLand,inspiredbyMalmo[27],Mineflayer[43],MineDojo[16]andVoyager[57],isaMinecraft
simulatorwhereplayers2canexplore,andinteractwitheachotheraswellastheenvironments. The
architectureasshowninFigure2consistsofthreemainmodules(DetailsinSectionC.1): theBot
Module,theEnvironmentModule,andtheBridgeModule.
Whattechnologyhascausedthefeatureoflarge-scalescalability? ExistingMinecraftsimulators
(e.g.,Malmo,MineRL,MineDojo)necessitaterunningaMinecraftgameclientforeachplayer. This
client-based approach comes with a notable drawback - it incurs substantial resource costs and
2Inthiswork,weusetheterm“player”torefertobothhumanplayersandAIagents. Whenwemention
“agent”,wespecificallymeanAIagents.HumanshavetheoptiontoaccessthegameeitherthroughVRorusing
akeyboard.
3

Figure2: IllustrationofthearchitectureofMineLand.
mostmachinescannothandlerunninglarge-scaleMinecraftgameclientsconcurrently. Incontrast,
MineLand adopts a different approach. It simplifies each Minecraft client into a single thread,
optimizing performance overhead caused by multiple clients. With MineLand, adding one more
agentonlyrequiresonemorethread. Basedonthisnewtechnique,MineLandsupports64ormore
agentsonamainstreamconsumerdesktopPC,whichisasubstantialimprovementcomparedtoother
Minecraftplatformsthatcanonlysupportupto2agents. Weconductedrelevantexperimentsin
Section5.1.
2.2 ObservationSpace
TheobservationspaceisdesignedtobecompatiblewithalmostallAPIsofthepopularMineDojo
framework. MineLand provides sensor information for players: tactile information (information
abouttheblockssurroundingtheagent,whichrepresenttheobjectsthattheagentcantouch),auditory
information,andvisualinformation(RGBvideofromthefirst-personperspectiveoftheagent).These
threemodalities(namely,touch,vision,andhearing)togetherprovidetheagentswithmultimodal
senses. Notethatthisinformationisallrawperceptualinformation.3
Whattechnologyhascausedthefeatureoflimitedmultimodalsenses? Werefertothemech-
anismsofhumanvisionandhearing, andimposelimitationsonthesensorperceptionofplayers,
includingdistanceattenuation,environmentalobstructions,anddirectionalconstraints,tomodelthe
limitedsenses.
2.3 StateSpace
Previoussimulatorsfocusontask-orientedactivities,thusthestatespacefocusesontheinventory
andequipment. Weuseastatespacethatblendstask-orientedactivitieswiththerhythmsofdailylife.
Whattechnologyhascausedthefeatureofphysicalneeds? Basicphysicalneedsarethefoun-
dationthatleadstodailylifebehavior. Fortherhythmsofdailylife,wedefinethestatesofagents
for themselves: physical needs like oxygen and hunger. Blending the rhythms of daily life with
task-orientedactivitiesiswhatmakesthissimulatorstandout. Imagineagentswakingupintheir
virtualMinecrafthomes,engagingindailyroutineslikecookingtosatisfyphysicalfoodneeds,but
alsohavingdefinedjobs(e.g.,lumberjack,farmer)thatinvolvespecifictask-orientedactivities. This
createsanaturalflowbetweendailylifeandgoal-drivenbehavior,providingamorerealisticand
nuancedenvironmentforstudyingagentinteractionsandcomplexsocialdynamics.
2.4 ActionSpace
The simulator offers a unique action space encompassing both low-level and high-level actions.
For the low-level actions, MineLand includes basic actions like walking, running, jumping, and
interactingwithobjects. Thelow-levelactionsarethesameasthetraditionalactionspaceingym-
styleAPI.WealsosupportReinforcementLearningbasedonlow-levelactions(Formoredetails
aboutexperimentsofReinforcementLearningmethod,pleaserefertoSectionI.High-levelactions,
3Besidestherawperceptualinformation,MineLandalsoprovidestheeventsencounteredbytheagent,such
asinjury,death,andothers.Injuryeventscanalsoberegardedastactileinformation,buttheyarepresentedin
theformofeventsforsimplicity.
4

Figure3: IllustrationofTasks. Wehaveexpandedthenumberofprogrammatictasksandcreative
tasksby2times,comparedtoMineDojo. Additionally,wehaveintroducednovelhybridtasksthat
combinethefeaturesofprogrammatictasksandcreativetasks. Customizingthenumberofplayersis
supported. Formulti-agents,weprovidetwomodes: cooperativemodeandcompetitivemode.
likedodgingobstaclesandmanipulatingtools,aresuitableforcomplextasksthatconsistofseveral
low-levelactionsandrequirelongercomputationtimes. Thehigh-levelactionsareimplementedin
theformofcode,followingVoyager[57]. Imagineagentsnavigatingtheworld,dodgingobstacles,
andmanipulatingtools. Thesecomplextasksgenerateanactionsequence,allowingthesimulatorto
continueexecutingthelow-levelactions,skipsomestepsearlier,orbeinterruptedbysomespecial
event.
2.5 Communication
Diversity Diversecommunicationstrategiescanleadtotheemergenceofmorerealisticbehaviors
withinthesimulatedenvironment. Wedesignthreecommunicationstrategiesincludingauditory
information,bodylanguage(viavisualperception),andsharinginformationintextmedia.
Whatcommunicationtechnologyhascausedthefeatureoflarge-scalescalability? Formulti-
agent simulators, an efficient communication mechanism is crucial, especially in situations with
large-scale scalability. Traditional communication methods, like centralized broadcasting to all
agents,canbecomecomputationallyexpensiveandslowdownthesimulationwithalargenumberof
agents. Herewedesignadistance-constrainedconstrainedcommunicationmechanism. Ifanagent
wantstocommunicatewithotheragents,itchatsthroughMinecraft’smessagebar. Onlywhenthe
distancebetweenotheragentsandthesendingagentislessthanacertainthreshold,willotheragents
receivemessages. Similarly,communicationsviaauditoryinformationandbodylanguagearelimited
bydistance.
Howistheinterruptmechanismimplemented? Mostimportantly,thenewmessageisallowedto
interrupttheexecutingcodeandexecutethismessagedirectlybeforethepreviouscodehasended.
Wetermthisastheinterruptmechanism. Withthismechanism,evenifanagentisworkingona
5-minuteextension(suchasmining),itisstillfeasibleforotheragentstocommunicatewiththis
workingagentatanytime. Thisinterruptmechanismwasnotsupportedinthepreviouswork,suchas
Voyager[57]. Next,wewillintroducehowtoimplementit. Forahigh-levelaction,theexecution
ofthecodeisdividedintoseveralsteps,witheachsteplasting50-200milliseconds4. Beforetaking
astep,theagentisprovidedwiththerunningstatesofthepreviouscode,eitherrunning,ready,or
exceptions. After completing a step, the agent, based on the running states, can choose to either
switchtoanewactioncodeorcontinueexecutingthepreviouscode. Thisfunctionofchoosingis
implementedbyanautomaticgatecontrolsystemwithtwogates: NewandResume. Newmeansthe
agentwantstoswitchtoanewcodeinthefollowingsteps. Resumeindicatesthattheagentwantsto
continueexecutingthepreviouscode. Inthisway,theagentcancompleteacodethatneedstobe
executedforalongperiod,orbeinterruptedatanappropriatetime. YoumayreferSectionE.4foran
example.
450millisecondsistheminimumtimeunitinMinecraft.Werefertothisminimumtimeunitasa“tick”.
5

3 MineLandBenchmarkSuiteandDataset
MineLand,asalarge-scalemulti-agentsimulator,pushtheboundariesofmulti-agentcapabilitiesby
enablingthemtotacklecomplexhuman-likeplanningtaskswithindiverseenvironments. However,
evaluating these advanced planning abilities necessitates sophisticated benchmarks. To address
this challenge, we propose a new benchmark suit, MineLand benchmark. MineLand benchmark
surpasses existing benchmarks by offering significantly more tasks (doubling programmatic and
creativetaskscomparedtoMineDojo)andintroducinganovel“hybridtask”categorythatcombines
thefeaturesofprogrammaticandcreativetasks(includingConstructionTasksandStagePerformance
Tasks). Additionally,thisbenchmarkallowsforflexibleplayernumbersandexplorationthrough
cooperativeandcompetitivemodes. Competitivemodecanbeusedtomeasurethedifferencesin
capabilitiesbetweendifferentAIagents,aswellastodevelopadversariallearningalgorithms. Refer
toSectionDformoredetails.
3.1 ProgrammaticTask
WefollowMineDojo[16]forthedesignofprogrammatictasks. EachTaskT isdefinedasa5-tuple:
T = (G,G,I,f ,S). Greferstothetaskgoalthatneedstobecompleted. G isguidance. I is
suc
theinitialconditionofthetask. f istheSuccessCriterion. S isasetofparametersthatcouldbe
suc
customized. DifferentfromMineDojo,theseparametersincludethenumberofagents,cooperative
mode,competitivemode,etc. Intotal,MineLandhas4499programmatictasks.
3.2 CreativeTask
Creativetasksisdefinedbya4-tuple: T =(G,G,I,S). Thereare1536creativetasksintotal,andis
compatiblewithtasksinMineDojo.
3.3 HybridTask
Hybridtasksdonothaveauniquegroundtruthbuthaveseveralreferences5. Werepresentthehybrid
taskasT = (G,G,I,D,f ,S). whereD denotesthereferences. Unlikeprogrammatictasks,
score
becauseHybridtasksdonothaveagroundtruth,MineLandwillreturnascoreoff basedonD.
score
Thehigherthescore,thebetterthetaskiscompleted. Wedesigntwotypesoftasks: Construction
andStagePerformance,forhybridtasks.
Construction Tasks Given a blueprint for a building or scene, the Construction Task aims to
buildthesebuildingsorscenesbasedontheblueprint. Theblueprint,eitherpicturesinreallifeor
Minecraft-stylepictures,isthereferenceD.
EvaluationMetrics. MineLandgivesascorebasedonwhethertheconstructedbuildingsmeetthe
blueprint’sexpectations. WecalculatethetaskscoresthroughtheVLM-basedevaluationsandhuman
evaluation,whichbothusethesamecriteria(refertoSectionQformoredetails). Theevaluation
scoresrangefrom1to5,withhigherscoresindicatingthattheagents’constructionsmoreclosely
resembletheintendedblueprint.
StagePerformanceTasksGivenascriptofadramaconsistingofseveralbehaviors,whichmaybea
singleactionoranemotionalexpression,theStagePerformanceTaskaimstoperformthescriptwith
agentsasactors.
EvaluationMetrics. Weleveragetwocomplementaryevaluationmetrics: anLCS(LongestCommon
Subsequence)-basedmetricandhumanevaluation. TheLCS-basedmetricconsistsoftwodistinct
scores: thekeypointscoreandtheappropriatenessscore. Wepresenttheformulasforaddingupthese
twoscores:
|LCS(SEQ ,SEQ∗)| |LCS(SEQ ,SEQ∗)|
f +f = Agent + Agent (1)
key appro |SEQ∗| |SEQ |
Agent
whereSEQ representstheactionsequencegeneratedbytheagent,whileSEQ∗istheground
Agent
truth. LCS(A,B) denotes the LCS between A and B. |A| is the length of sequence A. The
5Hybridtasksresembletranslationtasksinthat,whileasingleuniquetranslationmaynotexist,multiple
referencetranslationscanguidetheprocess.Herereferencescouldbekeyrules,constraints,andkeyevaluation
indicators,etc.
6

keypointscoreemphasizesthecompletenessoftheenactedbehaviors,ensuringallcrucialactions
andexpressionsareperformed. Theappropriatenessscoregoesbeyondcompletenesstoevaluate
theoverallcoherenceandnaturalnessoftheperformance,consideringhowwellthebehaviorsflow
togetherandalignwiththescript’sdramaticintent. Thehumanevaluationscoreisanintegerbetween
1and5,withhigherscoresindicatingbetterperformance. Itprovidesacomprehensiveassessment
oftheagents’abilitytonotonlyexecuteactionsaccuratelybutalsotodeliverthemnaturallyand
engagingly. DetailsofthehumanevaluationcriteriacanbefoundinSectionR.
Figure4: IllustrationofthearchitectureofAlex.
4 AlexAgent
To truly demonstrate the challenge of this benchmark, we propose Alex6, a VLM-based agent
as shown in Figure 4. Conventional LLM-powered AI agents depend on LLM to operate as its
brain,whichisbackedbyseveralvitalcomponentsthatperformvariousessentialfunctions. These
components,suchasthememorycomponent,planningcomponent,andactingcomponent,havebeen
thoroughlystudiedrecently. Tocatertoourspecificrequirements,wehaveimprovedthesethree
components(refertoSectionEformoredetails),replacedLLMwithVLMandintroducedonenew
component: the multitasking component. Additionally, Alex exhibits different personality traits
predefinedinthesystemprompt.
MultitaskingComponent Peopleoftenswitchattentionbetweentasks,forexamplecookingwhile
talking. Theabilitytocommunicatesmoothlywithotherplayerswhileworkingonatask-oriented
actioniscrucialinmulti-agentscenarios.Therefore,wedevelopthemechanismofmultitaskingability
toenhancetheagent’sattentioncontrolandworkingmemoryabilitiesinspiredbytheMultitasking
theoryfromtheCognitionfield[53]. Specifically, forattentioncontrol, theinterruptmechanism
effectively controls attention among multiple tasks. For working memory, Alex maintains and
processesinformationintheMemoryLibrary. Whenanotheragentsayshellototheworkingagent,
thisinvolvessavingandrestoringinternalstateswhenfrequentandhigh-speedswitchingbetween
communicationactivitiesandgoal-drivenworkingactionstoavoidforgettingongoingtasks. With
the multitasking mechanism, Alex allows for simultaneously simulating and executing intricate
coordinationandschedulingwithmultipletasks.
5 Experiments
5.1 ExperimentsofSimulatorsPerformance
WeevaluatethenumberofagentsthatMineLandcansupportandcompareMineLandwithother
popular Minecraft simulators. We utilize a mainstream consumer desktop PC equipped with an
Intel i5-12400F CPU and 64GB of memory. Performance Monitor is employed to monitor the
process. OurfindingsrevealthatMineLandiscapableofsupporting32agentssimultaneouslywhile
6AlexistheprotagonistinthesandboxgameMinecraft,oneofthedefaultskinsforplayersandacharacterin
thegame:https://www.minecraft.net/zh-hans.Topaytribute,wenamedourproposedAIagentAlex.
7

providingvisualdisplays.Whenvisualdisplayisdisabled,thenumberofconcurrentlyrunningagents
increasesto×4times. Furthermore,asdepictedinTable2,whenMineLandandMalmobothrun
8agents,MineLand’sCPUandmemoryusageareapproximately1/3thatofMalmo’s(specifically,
35.6%and38.0%,respectively). ItisworthnotingthatMalmoservesasthefoundationformost
popularMinecraftPlatforms(e.g.,MineDojo/MineRL/MarLÖ[42]),thushighlightingMineLand’s
superiorperformancecomparedtothevastmajorityofexistingMinecraftPlatforms. Consequently,
MineLandprovestobehighlysuitableformulti-agentenvironments.
5.2 ExperimentsofSocialDynamics
Inthe“unlockingtools”taskwithtwoagents(Table3),twoagentsinthecollaborativemodework
togethereffectively,withareducedworkloadperagentandhighercommunicationexpenses. Onthe
otherhand,twocompetitiveagentsworkedindependentlyandnecessitatedfewercodeiterations. The
primaryreasonisthat,incompetitiverelationships,agentstendtoachievemoreinasingleiteration
toexpediteprogressandoutperformtheiropponents. However,thisresultsinlessthoroughplanning
andmorecodeerrors. Consequently,multipleagentsincompetitiverelationshipsrequirefewercode
iterationsbutmakemoremistakes.
Wealsoobservethatpersonalityplaysasignificantroleindeterminingthebehaviorofagentsin
multi-agentsocieties[25]. Weassignedthepersonalitytraitsofhighextraversionandagreeableness
to both agents. Under this condition, the agents tended to establish collaboration and engage in
mutualcommunication(co-op>8outof10times). Thisresultisconsistentwithhumanbehavior[13].
Whennopersonalitywassetfortheagents,theyworkedindependently(co-op0outof10times). For
moreexperimentsofsimulatingsociologicalphenomenawith>10agents,pleaserefertoSectionO.
Table 2: Part of the comparison table of per- Table 3: The number of code iterations
formance of Minecraft simulators. The full ta- neededperagenttounlocktoolsmadeofvari-
ble is in Table 9. MineLand means ousmaterialsisdeterminedunderthreecondi-
w/ovision
MineLandwithoutvision. CPUandMemrepresent tions.Theseconditionsincludeasingleagent,
theaverageCPUtimeandmemoryusageduringthe two agents in cooperation, and two agents
initializationphaseand5-minuterunrespectively. incompetition. Eachexperimentisrepeated
threetimes,andthesuccessrateis100%.
Simulator Agents CPU Mem
Material
MineLand 8 2.81% 7.07GB Relationship
MineLand 32 5.64% 19.65GB Wooden Stone Iron
MineLand 8 1.88% 2.94GB
w/ovision SingleAgent 7±2 10±3 25±7
MineLand 64 2.87% 6.30GB
w/ovision Cooperative 13±5 20±7 49±10
MineLand 128 4.00% 9.04GB
w/ovision Competitive 6±2 10±3 27±10
Malmo 8 7.90% 18.63GB
5.3 ExperimentsofConstructionTasks
To establish a baseline for the research community, we evaluate our un-finetuned Alex on two
exampleconstructiontasks: “MonumentConstruction”and“StoneSteleConstruction”(detailedin
SectionMandTable4). WhileAlexdemonstratesapromisingcapabilityinselectingappropriate
materialsforbothtasks, itsoverallconstructionabilitiesarecurrentlylimited. Weposittwokey
reasons for these limitations: complex task planning and high-precision manipulation. For the
firstreason,constructiontasksareinherentlytime-consumingandrequiresophisticatedplanning
abilities. For instance, building auxiliary structures to facilitate the main construction process is
crucialforachievingsignificantheight. However,Alexcannotcurrentlyplanandconstructsuch
auxiliarystructures,hinderingitsabilitytoconstructtallstructures. Thesecondreasonisthehigh-
precision manipulation. The construction tasks necessitate high-precision manipulation, such as
addingdecorativedetails. Alexprimarilyutilizeshigh-levelactionsandlacksthenecessaryAPIsto
executethesefine-grainedmanipulationseffectively. Theseresultsshowthechallengeofthistask.
5.4 ExperimentsofStagePerformanceTasks
Weevaluateourun-finetunedAlexonfourexamplestageperformancetasks(Table5). Wefound
thatinsingle-agenttasks,theagenttypicallyexhibitshighscoresacrossallthreeevaluationmetrics.
However, in multi-agent tasks, the keypoint score tends to be higher than the appropriate score
8

becausetheagentcanunderstandthescriptandfulfillthekeyrequirements. Incontrast,thehuman
evaluationscoresareusuallyrelativelylowerbecauseagentsoftenengageinunnecessarydialoguein
scriptsthatrequirecollaboration,resultinginlowerscores.
Table 4: Human evaluation score Table5:Appropriatenessscore(Appro.),keypointscore(Key.),
and VLM-based (gpt-4o) evalua- andHumanEvaluationScore(Human.) ofAlexAgentacross
tion score of Alex agent on two four stage performance tasks. The number in parentheses
constructiontasks. Weconducted followingthescriptnamerepresentsthenumberofagentsin
three evaluations using the VLM thatscript. Appropriatenessscoreandkeypointscorearereal
andobtainedconsistentresults. De- numbersintherange[0,1],andthehumanevaluationscoreis
tails in Section Q. VLM: VLM- anintegerbetween1and5. DetailsinSectionNandSectionR.
basedscore. Human: Humanevalu-
ationscore. Score
ScriptName
Appro. Key. Human.
Score
Construction
Cookfood(1) 1.00 1.00 5
VLM Human
Exchangeitems(2) 0.59 0.99 4
AMonument 4,3,3 3 Makefriends(3) 0.67 0.98 3
AStoneStele 1,1,1 1 RomeoandJulia,ActISceneI(13) 0.09 0.20 1
5.5 ExperimentsofMulti-AgentCooperation
Tovalidatethecooperationefficiencyofouragentframework, weconductthe“unlockingtools”
task with two agents. We observed that agents in a cooperative relationship required more code
iterationstofinishthetask,primarilybecausemostoftheseiterationswerededicatedtoestablishing
andmaintainingcommunication,aswellastaskallocation. Forexample,whenoneagentsaysina
chatthatheneedstwosticks,anotheragentwillaskforgettingtogethernearthetable,andthengive
thestickstohim. However,theactualworkloadforeachagentisreducedwithoutconsideringthe
chatcost. Comparedtoagentsworkingindependently,thecodeiterationcostofagentscooperatingis
reducedby20%peragent.
5.6 ExperimentsofMultitasking
Tovalidatetheimpactofmultitaskingsupportinthesimulator7,weconducttheobsidianmining
task,whichtakesover8minutesandrequiresmultiplestepstocomplete. Inthebeginning,theagent
isminingandencounterschatorhurteventswithin8minutes. Chatevent: Anotheragentnearby
initiatesaconversationwithAlex. Thisisalow-priorityevent, andAlexcanchoosewhetherto
respondtotheagentnearby. Hurtevent: Theagentgetshurts. Forexample,azombieattacksthe
agent. Thisisahigh-priorityevent,requiringAlextostopitscurrenttaskandaddressthiseventfirst.
Weexpectthetwotypesofeventstoactivatethemultitaskingcomponentandtheagentprocessesthe
miningandthespecialeventsimultaneously. ResultsareinTable6. Inalltenruns,wecountthe
numberofsuccessfullyhandlingmultitasks. Forthehurtevent,iftheagentfightsbackduetothis
hurtevent,itisconsideredsuccessful. Forthechatevent,iftheagentrespondsduetothechatevent,
itisconsideredsuccessful. ResultsrevealthatAlex can’tprocesseventstimely,resultingin
w/omt
Alexbeingkilledbythezombie. Incontrast, Alexwithamultitaskingcomponentiscapableof
managingmultipleevents(e.g.,miningwhilechatting),autonomouslydeterminingtheirpriority,and
addressingthehigher-priorityeventsfirst. Hence,multitaskingisanessentialmechanism.
Table6: ComparisonbetweenAlexandAlex (Alexwithoutthemultitaskingcomponent).
w/omt
Agent Hurtevent Chatevent
Alex 8/10 2/10
Alex 0/10 0/10
w/omt
7Thismultitaskingfunctionalityisachievedthroughthesynergisticinterplayoftwokeys:themultitasking
componentinAlexandtheinterruptmechanisminMineLand.
9

6 Conclusion
Traditional multi-agent simulators struggle with large-scale scenarios and often assume perfect
informationandunrealisticagentcapabilities. Toaddresstheselimitations,weintroduceMineLand,
anovelMinecraft-basedsimulatorsupporting64ormoreagentswithlimitedsensesandphysical
needs. Thisforcesagentstoactivelycommunicateandcollaborate,fosteringmoreecologicallyvalid
interactions. Theadvantagecarriespotentialbroaderimpactsacrossvariousdomainsasdiscussedin
SectionB.
References
[1] ClaytonPAlderfer. Anempiricaltestofanewtheoryofhumanneeds. Organizationalbehavior
andhumanperformance,4(2):142–175,1969.
[2] JitaoBai,SimiaoZhang,andZhonghaoChen.Isthereanysocialprincipleforllm-basedagents?
arXivpreprintarXiv:2308.11136,2023.
[3] BowenBaker,IlgeAkkaya,PeterZhokhov,JoostHuizinga,JieTang,AdrienEcoffet,Brandon
Houghton,RaulSampedro,andJeffClune. Videopretraining(vpt):Learningtoactbywatching
unlabeledonlinevideos,2022.
[4] JosephBates.Theroleofemotioninbelievableagents.CommunicationsoftheACM,37(7):122–
125,1994.
[5] MarcelBinzandEricSchulz. Usingcognitivepsychologytounderstandgpt-3. Proceedingsof
theNationalAcademyofSciences,120(6):e2218523120,2023.
[6] WoodyBledsoe. Ihadadream: Aaaipresidentialaddress. AIMagazine,7(1):57–61,1986.
[7] ShaofeiCai, ZihaoWang, XiaojianMa, AnjiLiu, andYitaoLiang. Open-worldmulti-task
control through goal-aware representation learning and adaptive horizon prediction. arXiv
preprintarXiv:2301.10034,2023.
[8] ShaofeiCai, ZihaoWang, XiaojianMa, AnjiLiu, andYitaoLiang. Open-worldmulti-task
controlthroughgoal-awarerepresentationlearningandadaptivehorizonprediction. InProceed-
ingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition(CVPR),pages
13734–13744,June2023.
[9] YongcanCao,WenwuYu,WeiRen,andGuanrongChen. Anoverviewofrecentprogressin
thestudyofdistributedmulti-agentcoordination. IEEETransactionsonIndustrialinformatics,
9(1):427–438,2012.
[10] Stuart K Card, Thomas P Moran, and Alan Newell. The psychology of human-computer
interaction. 1983.
[11] Jiaqi Chen, Yuxian Jiang, Jiachen Lu, and Li Zhang. S-agent: self-organizing agents in
open-endedenvironment. InICLR2024WorkshoponLargeLanguageModel(LLM)Agents,
2024.
[12] Antônio Carlos da Rocha Costa. A Variational Basis for the Regulation and Structuration
MechanismsofAgentSocieties. Springer,2019.
[13] BoeleDeRaad. Thebigfivepersonalityfactors: thepsycholexicalapproachtopersonality.
Hogrefe&HuberPublishers,2000.
[14] Kevin Dill and L Martin. A game ai approach to autonomous control of virtual characters.
InProceedingsoftheInterservice/IndustryTraining,Simulation,andEducationConference
(I/ITSEC’11),Orlando,FL,USA,2011.
[15] LenDoyalandIanGough. Atheoryofhumanneeds. CriticalSocialPolicy,4(10):6–38,1984.
[16] LinxiFan,GuanzhiWang,YunfanJiang,AjayMandlekar,YuncongYang,HaoyiZhu,Andrew
Tang,De-AnHuang,YukeZhu,andAnimaAnandkumar. Minedojo: Buildingopen-endedem-
bodiedagentswithinternet-scaleknowledge. InThirty-sixthConferenceonNeuralInformation
ProcessingSystemsDatasetsandBenchmarksTrack,2022.
[17] YichengFeng,YuxuanWang,JiazhengLiu,SipengZheng,andZongqingLu. Llamarider:
Spurringlargelanguagemodelstoexploretheopenworld,2023.
10

[18] RanGong,QiuyuanHuang,XiaojianMa,HoiVo,ZaneDurante,YusukeNoda,ZilongZheng,
Song-ChunZhu,DemetriTerzopoulos,LiFei-Fei,etal. Mindagent: Emergentgaminginterac-
tion. arXivpreprintarXiv:2309.09971,2023.
[19] WilliamHGuss,BrandonHoughton,NicholayTopin,PhillipWang,CaydenCodel,Manuela
Veloso,andRuslanSalakhutdinov. Minerl: Alarge-scaledatasetofminecraftdemonstrations.
arXivpreprintarXiv:1907.13440,2019.
[20] WilliamH.Guss,BrandonHoughton,NicholayTopin,PhillipWang,CaydenCodel,Manuela
Veloso,andRuslanSalakhutdinov. Minerl: Alarge-scaledatasetofminecraftdemonstrations,
2019.
[21] JohnHeil. Perceptionandcognition. 1983.
[22] JamesD.Hollan,EdwinL.Hutchins,andLouisWeitzman. Steamer: Aninteractiveinspectable
simulation-basedtrainingsystem. AIMagazine,5(2):23–36,1984.
[23] JohnJ.Horton. Largelanguagemodelsassimulatedeconomicagents: Whatcanwelearnfrom
homosilicus?,2023.
[24] GuangyuanJiang,ManjieXu,Song-ChunZhu,WenjuanHan,ChiZhang,andYixinZhu. Eval-
uatingandinducingpersonalityinpre-trainedlanguagemodels. InThirty-seventhConference
onNeuralInformationProcessingSystems,2023.
[25] Guangyuan Jiang, Manjie Xu, Song-Chun Zhu, Wenjuan Han, Chi Zhang, and Yixin Zhu.
Evaluating and inducing personality in pre-trained language models. Advances in Neural
InformationProcessingSystems,36,2024.
[26] BonnieEJohnandDavidEKieras. Thegomsfamilyofuserinterfaceanalysistechniques:
Comparison and contrast. ACM Transactions on Computer-Human Interaction (TOCHI),
3(4):320–351,1996.
[27] M.Johnson,K.Hofmann,T.Hutton,andD.Bignell. Themalmoplatformforartificialintelli-
genceexperimentation. InProc.25thInternationalJointConferenceonArtificialIntelligence,
page4246,PaloAlto,CaliforniaUSA,2016.AAAIPress.
[28] RandolphMJones,JohnELaird,PaulENielsen,KarenJCoulter,PatrickKenny,andFrankV
Koss. Automatedintelligentpilotsforcombatflightsimulation. AIMagazine,20(1):27–42,
1999.
[29] PatrikNJuslin,KlausRScherer,JHarrigan,andRRosenthal. Vocalexpressionofaffect. The
newhandbookofmethodsinnonverbalbehaviorresearch,pages65–135,2005.
[30] Julia Kiseleva, Ziming Li, Mohammad Aliannejadi, Shrestha Mohanty, Maartje ter Hoeve,
Mikhail Burtsev, Alexey Skrynnik, Artem Zholus, Aleksandr Panov, Kavya Srinet, Arthur
Szlam, YuxuanSun, KatjaHofmann, MichelGalley, andAhmedAwadallah. Neurips2021
competitioniglu: Interactivegroundedlanguageunderstandinginacollaborativeenvironment,
2021.
[31] Eric Kolve, Roozbeh Mottaghi, Winson Han, Eli VanderBilt, Luca Weihs, Alvaro Herrasti,
DanielGordon,YukeZhu,AbhinavGupta,andAliFarhadi. AI2-THOR:AnInteractive3D
EnvironmentforVisualAI. arXiv,2017.
[32] JohnLairdandMichaelVanLent. Human-levelai’skillerapplication: Interactivecomputer
games. AIMagazine,22(2):15,2001.
[33] KalyaniLakkanige,LamarCooley-Russ,AlanR.Wagner,andSarahRajtmajer. Exploringtrust
andriskduringonlinebarteringinteractions,2023.
[34] JoelZ.Leibo,EdgarDuénezGuzmán,AlexanderSashaVezhnevets,JohnP.Agapiou,Peter
Sunehag,RaphaelKoster,JaydMatyas,CharlesBeattie,IgorMordatch,andThoreGraepel.
Scalableevaluationofmulti-agentreinforcementlearningwithmeltingpot. PMLR,2021.
[35] ChengshuLi,FeiXia,RobertoMartín-Martín,MichaelLingelbach,SanjanaSrivastava,Bokui
Shen,KentElliottVainio,CemGokmen,GokulDharan,TanishJain,AndreyKurenkov,Karen
Liu,HyowonGweon,JiajunWu,LiFei-Fei,andSilvioSavarese. igibson2.0: Object-centric
simulationforrobotlearningofeverydayhouseholdtasks. InAleksandraFaust,DavidHsu,
andGerhardNeumann,editors,Proceedingsofthe5thConferenceonRobotLearning,volume
164ofProceedingsofMachineLearningResearch,pages455–465.PMLR,08–11Nov2022.
11

[36] HaoLi,XueYang,ZhaokaiWang,XizhouZhu,JieZhou,YuQiao,XiaogangWang,Hongsheng
Li,LeweiLu,andJifengDai. Automc-reward: Automateddenserewarddesignwithlarge
languagemodelsforminecraft,2024.
[37] ShaotengLiu,HaoqiYuan,MindaHu,YanweiLi,YukangChen,ShuLiu,ZongqingLu,and
JiayaJia. Rl-gpt: Integratingreinforcementlearningandcode-as-policy,2024.
[38] ChrisMadgeandMassimoPoesio. Largelanguagemodelsasminecraftagents,2024.
[39] OpenAI. Gpt-4technicalreport,2024.
[40] JoonSungPark,JosephO’Brien,CarrieJunCai,MeredithRingelMorris,PercyLiang,and
MichaelSBernstein. Generativeagents: Interactivesimulacraofhumanbehavior. InProceed-
ingsofthe36thAnnualACMSymposiumonUserInterfaceSoftwareandTechnology,pages
1–22,2023.
[41] JoonSungPark,LindsayPopowski,CarrieJ.Cai,MeredithRingelMorris,PercyLiang,and
MichaelS.Bernstein. Socialsimulacra: Creatingpopulatedprototypesforsocialcomputing
systems. InInthe35thAnnualACMSymposiumonUserInterfaceSoftwareandTechnology
(UIST’22),UIST’22,NewYork,NY,USA,2022.AssociationforComputingMachinery.
[42] Diego Perez-Liebana, Katja Hofmann, Sharada Prasanna Mohanty, Noburu Kuno, Andre
Kramer, Sam Devlin, Raluca D. Gaina, and Daniel Ionita. The multi-agent reinforcement
learninginmalmö(marlö)competition,2019.
[43] PrismarineJS. mineflayer. https://github.com/PrismarineJS/mineflayer,2023.
[44] XavierPuig,KevinRa,MarkoBoben,JiamanLi,TingwuWang,SanjaFidler,andAntonio
Torralba. Virtualhome: Simulatinghouseholdactivitiesviaprograms. InProceedingsofthe
IEEEConferenceonComputerVisionandPatternRecognition,pages8494–8502,2018.
[45] XavierPuig,TianminShu,ShuangLi,ZilinWang,Yuan-HongLiao,JoshuaBTenenbaum,
SanjaFidler,andAntonioTorralba. Watch-and-help: Achallengeforsocialperceptionand
human-aicollaboration. InInternationalConferenceonLearningRepresentations,2020.
[46] XavierPuig,TianminShu,ShuangLi,ZilinWang,JoshuaB.Tenenbaum,SanjaFidler,andAn-
tonioTorralba. Watch-and-help: Achallengeforsocialperceptionandhuman-aicollaboration,
2020.
[47] XavierPuig,EricUndersander,AndrewSzot,MikaelDallaireCote,Tsung-YenYang,Ruslan
Partsey,RutaDesai,AlexanderWilliamClegg,MichalHlavac,SoYeonMin,etal. Habitat3.0:
Aco-habitatforhumans,avatarsandrobots. arXivpreprintarXiv:2310.13724,2023.
[48] Chen Qian, Xin Cong, Cheng Yang, Weize Chen, Yusheng Su, Juyuan Xu, Zhiyuan Liu,
and Maosong Sun. Communicative agents for software development. arXiv preprint
arXiv:2307.07924,2023.
[49] YiranQin,EnshenZhou,QichangLiu,ZhenfeiYin,LuSheng,RuimaoZhang,YuQiao,and
JingShao.Mp5:Amulti-modalopen-endedembodiedsysteminminecraftviaactiveperception,
2024.
[50] AlecRadford,JongWookKim,ChrisHallacy,AdityaRamesh,GabrielGoh,SandhiniAgarwal,
GirishSastry,AmandaAskell,PamelaMishkin,JackClark,etal. Learningtransferablevisual
modelsfromnaturallanguagesupervision. InInternationalconferenceonmachinelearning,
pages8748–8763.PMLR,2021.
[51] AntoninRaffin,AshleyHill,AdamGleave,AnssiKanervisto,MaximilianErnestus,andNoah
Dormann. Stable-baselines3: Reliablereinforcementlearningimplementations. Journalof
MachineLearningResearch,22(268):1–8,2021.
[52] MarkO.Riedl. Interactivenarrative: Anovelapplicationofartificialintelligenceforcomputer
games.InProceedingsoftheTwenty-SixthAAAIConferenceonArtificialIntelligence(AAAI’12),
pages2160–2165,2012.
[53] DarioDSalvucciandNielsATaatgen. Threadedcognition: anintegratedtheoryofconcurrent
multitasking. Psychologicalreview,115(1):101,2008.
[54] BokuiShen,FeiXia,ChengshuLi,RobertoMartín-Martín,LinxiFan,GuanzhiWang,Claudia
Pérez-D’Arpino,ShyamalBuch,SanjanaSrivastava,LyneP.Tchapmi,MicaelE.Tchapmi,Kent
Vainio,JosiahWong,LiFei-Fei,andSilvioSavarese. igibson1.0: asimulationenvironment
forinteractivetasksinlargerealisticscenes. In2021IEEE/RSJInternationalConferenceon
IntelligentRobotsandSystems(IROS),pageaccepted.IEEE,2021.
12

[55] Andrew Szot, Alex Clegg, Eric Undersander, Erik Wijmans, Yili Zhao, John Turner, Noah
Maestre, Mustafa Mukadam, Devendra Chaplot, Oleksandr Maksymets, Aaron Gokaslan,
VladimirVondrus,SameerDharur,FranziskaMeier,WojciechGaluba,AngelChang,ZsoltKira,
VladlenKoltun,JitendraMalik,ManolisSavva,andDhruvBatra. Habitat2.0: Traininghome
assistantstorearrangetheirhabitat. InAdvancesinNeuralInformationProcessingSystems
(NeurIPS),2021.
[56] Milind Tambe, W Lewis Johnson, Randolph M Jones, Frank Koss, John E Laird, Paul S
Rosenbloom,andKarlSchwamb. Intelligentagentsforinteractivesimulationenvironments. AI
Magazine,16(1):15,1995.
[57] GuanzhiWang,YuqiXie,YunfanJiang,AjayMandlekar,ChaoweiXiao,YukeZhu,LinxiFan,
andAnimaAnandkumar. Voyager: Anopen-endedembodiedagentwithlargelanguagemodels.
arXivpreprintarXiv:2305.16291,2023.
[58] ZihaoWang,ShaofeiCai,AnjiLiu,YonggangJin,JinbingHou,BoweiZhang,HaoweiLin,
ZhaofengHe,ZilongZheng,YaodongYang,XiaojianMa,andYitaoLiang. Jarvis-1: Open-
worldmulti-taskagentswithmemory-augmentedmultimodallanguagemodels. arXivpreprint
arXiv: 2311.05997,2023.
[59] ZihaoWang,ShaofeiCai,AnjiLiu,XiaojianMa,andYitaoLiang. Describe,explain,planand
select: Interactiveplanningwithlargelanguagemodelsenablesopen-worldmulti-taskagents.
arXivpreprintarXiv:2302.01560,2023.
[60] RossWilliams,NiyoushaHosseinichimeh,AritraMajumdar,andNavidGhaffarzadegan. Epi-
demicmodelingwithgenerativeagents. arXivpreprintarXiv:2307.04986,2023.
[61] S Wimmer, A Pfeiffer, and N Denk. The everyday life in the sims 4 during a pandemic. a
lifesimulationasavirtualmirrorofsociety? InINTED2021Proceedings,pages5754–5760.
IATED,2021.
[62] FanboXiang,YuzheQin,KaichunMo,YikuanXia,HaoZhu,FangchenLiu,MinghuaLiu,
HanxiaoJiang, YifuYuan, HeWang, LiYi, AngelX.Chang, LeonidasJ.Guibas, andHao
Su. SAPIEN:Asimulatedpart-basedinteractiveenvironment. InTheIEEEConferenceon
ComputerVisionandPatternRecognition(CVPR),June2020.
[63] JifanYu,XiaozhiWang,ShangqingTu,ShulinCao,DanielZhang-Li,XinLv,HaoPeng,Zijun
Yao,XiaohanZhang,HanmingLi,etal. Kola: Carefullybenchmarkingworldknowledgeof
largelanguagemodels. arXivpreprintarXiv:2306.09296,2023.
[64] ChiZhang,PenglinCai,YuhuiFu,HaoqiYuan,andZongqingLu.Creativeagents:Empowering
agentswithimaginationforcreativetasks,2023.
[65] Hongxin Zhang, Weihua Du, Jiaming Shan, Qinhong Zhou, Yilun Du, Joshua Tenenbaum,
TianminShu,andChuangGan. Buildingcooperativeembodiedagentsmodularlywithlarge
languagemodels. InNeurIPS2023FoundationModelsforDecisionMakingWorkshop,2023.
[66] ZhonghanZhao,WenhaoChai,XuanWang,LiBoyi,ShengyuHao,ShidongCao,TianYe,
Jenq-NengHwang,andGaoangWang. Seeandthink: Embodiedagentinvirtualenvironment,
2023.
[67] ZhonghanZhao,KeweiChen,DongxuGuo,WenhaoChai,TianYe,YantingZhang,andGaoang
Wang. Hierarchicalauto-organizingsystemforopen-endedmulti-agentnavigation,2024.
[68] EnshenZhou, YiranQin, ZhenfeiYin, YuzhouHuang, RuimaoZhang, LuSheng, YuQiao,
and Jing Shao. Minedreamer: Learning to follow instructions via chain-of-imagination for
simulated-worldcontrol,2024.
[69] Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Weijie Su, Chenyu Yang, Gao Huang,
BinLi,LeweiLu,XiaogangWang,YuQiao,ZhaoxiangZhang,andJifengDai. Ghostinthe
minecraft: Generallycapableagentsforopen-worldenvironmentsvialargelanguagemodels
withtext-basedknowledgeandmemory. arXivpreprintarXiv:2305.17144,2023.
[70] Mingchen Zhuge, Haozhe Liu, Francesco Faccio, Dylan R Ashley, Róbert Csordás, Anand
Gopalakrishnan, Abdullah Hamdi, Hasan Abed Al Kader Hammoud, Vincent Herrmann,
KazukiIrie, etal. Mindstormsinnaturallanguage-basedsocietiesofmind. arXivpreprint
arXiv:2305.17066,2023.
13

A RelatedWork
A.1 Multi-AgentSimulator
AsthepopularityofAIagentresearchcontinuestogrow,therehasalsobeenafocusonstudying
multiple AI agents as well as their cooperation and competition. Researchers and practitioners
imagine a dynamic artificial society where human interactions can be simulated by trustworthy
agents[12]. Fromtwoindividuals[9,45],throughfourindividuals[61],tosandboxgamesSmallville
withtwenty-fiveindividuals[40],wewitnesshowindividualsperceiveasimulatedsocietyasthe
backdrop and interact with the agents and people who engage with it. Each individual can be
portrayed through a program, a real human, or an agent based on LLM [40]. The interaction
between individuals plays a role in shaping social behavior, leading to simulation of the society.
Simulatinglargersocietiescanbeadvantageous. Increasingthenumberofagentscanleadtogreater
specialization, enabling the accomplishment of more complex and larger-scale tasks. This can
significantlyimprovetaskefficiency,suchasinsoftwaredevelopmenttasks[48]. Additionally,such
simulationofinteractionhashadasignificanteffectinmanyotherfields.Forexample,itcanreplicate
realisticsocialphenomena[14,41],enhancesocialrobots[4,6]. Theycanalsobeusedtotestsocial
sciencetheories[5,24,23],createmodelhumanprocessorsfortheoryandusabilitytesting[10,26],
trainpeopleonhowtohandlerareyetdifficultinterpersonalsituations[56,28,22],andsupportgame
characters[32,52]. Therearealsomanynon-Minecraftandnon-open-worldsimulators, suchas
Habitat3.0[47],VirtualHome[44,46],SAPIEN[62],AI2-THOR[31],andiGibson[35,54].
Challenges of Scaling Up the Number of Agents. While increasing the number of agents can
improvetaskefficiencyandmakemulti-agentsimulationsmorerealistic[48,40,60],currentresearch
primarilyfocusesonasmallnumberofagents[40,2,70]. Thisismainlyduetothechallengesof
scalingupthenumberofagents. DeployingalargenumberofAIagentswillresultinanincreased
computationalburden,necessitatingbetterarchitecturaldesignandcomputationaloptimization[40].
Most research in terms of AI agents mimicking daily life routines, focused on two agents [45].
Simulatorsthatremindpeopleofsandboxgames(TheSims)initiallysupportfourindividuals[61],
thenareextendedtotwenty-fiveindividualsby[40].
ChallengesofLimitedMultimodalSenses. Toensuretheauthenticityofthesimulation,anideal
multi-agentsimulatorshouldoperateunderthefundamentalassumptionthatagentspossessonly
limitedmultimodalsenseslikehumans[21]. Limitedmultimodalsensesmeanpartiallyobservable
environmentsandaneco-centricperspective. Limitedvisualandauditorysensesrestrictinformation
access,forcingagentstoactivelynavigateandcommunicatetocompensateforsensorydeficiencies.
Thismirrorsreal-lifesocialinteractions,wherevisibilityandaudibilitycanbeaffectedbyfactors
suchasdistance,terrain,andcontext[29]. Asthenumberofagentsgrows,thechallengesoflimited
multimodalsensesbecomequitedifficult. Thisisbecausethecommunicationnetworkoftheentire
system becomes highly intricate. For agents in our MineLand, the video input is an eco-centric
perspective (first perspective) instead of the third perspective in [40], which is omniscient and
unrealistic.
ChallengesofPhysicalNeeds. Multi-agentsimulationplatformsholdimmensepotentialforex-
ploringandunderstandinghumansocialdynamics. However,existingparadigmsoftendisregard
thehumanneeds[15,1]. Existingsimulatorsaredesignedtosimulatebelievablehumanbehavior
in daily-life activities [40, 2]. These activities include waking up, cooking breakfast, heading to
work,andinitiatingconversationswithothers. However,theydonotdefinetheirphysicalneeds. For
example,afteracertainamountoftimehaspassed,theagentwillbecomehungryandhavethedesire
tocook. Thisdesirethenleadstothenextactions. Inthisway,theactionofcookingismotivatedby
realdesiresinsteadofapredefinedschedule.
Weincorporatepracticalphysicalrequirementsintotheagentmodel. Agentshavebasicphysical
needs: sleep,food,andresourcemanagement,whichintroducesanengagingtime-basedelementto
theirdailyroutineprocesses. Thisencouragescollaborationandcompetitionforresources,reflecting
theintricatebalanceofcooperationandself-interestseeninhumansocieties.
14

A.2 Multi-AgentSimulatorw.r.tMinecraft
Minecraft,thebelovedsandboxgame,hasbeenavaluableplatformforresearchersexploringvarious
fields,includingartificialintelligenceandmulti-agentsystems,becauseofitsopenworldanddiverse
mechanics.
Specifically, the flexibility and richness of Minecraft make it perfect for developing multi-agent
simulators. Researchers have the ability to create various custom environments and scenarios
withinthegameworld,wheretheycanintroducevirtualagentswithspecificgoalsandcapabilities.
Theseagentscantheninteractwitheachotherandtheenvironment,providingresearcherswiththe
opportunitytoobserveandanalyzetheirbehaviorinacontrolledsetting. Thesesimulatorscanbe
broadlycategorizedintotwomaintypes: task-orientedsimulatorsanddaily-lifesimulators.
Task-oriented simulators focus on agents achieving specific objectives within a set time frame.
MinecraftisregardedasthetraininggroundforAIagentstohonetheirskills. Forexample, [19,
16, 68, 37] focuses on exploring the environment and gathering resources like wood and stone,
andmanagingthemefficientlytocompletetaskslikebuildingstructuresorcraftingtools. Agents
in [67] are designed to complete navigation tasks. In [11], agents are self-organized to execute
collaborative building tasks and resource collection tasks. Agents in [18] must work together to
overcomechallengesthatrequirejointeffort.
Daily-lifesimulatorstakeamoreholisticapproach,focusingonthedailylivesofagentswithina
virtualsociety. [40]simulatestherhythmsandroutinesofdailylife. Thisincludesactivitiessuch
aswakingup,cookingbreakfast,goingtowork,formingopinions,observingothers,andengaging
inconversations. [33]simulatessociologicalexperiments,andexamineshowriskaffectstheway
peopleengageinbartering.
A.3 AIAgentwithLLMsandVLMs
LLMs or VLMs are commonly utilized to bootstrap the components of the Agent. In particular,
LLMs have demonstrated effective performance for task-planning [18, 69, 38, 36, 17], and they
possesssubstantialworldknowledge[63]. TeamCraftJarvishasalsodevelopedapowerfulagent,
[58], based on their previous projects [59, 7]. Moreover, VLMs like CLIP [50] offer a versatile
visual-languagerepresentationthatalignswithlanguageandenableszero-shotvisualrecognition
capabilitiesforpotentialAIagents. UsingVLMsinconstructiontaskshasmanyadvantagesover
existing methods [64]. AI agents with visual information can also complete tasks in human-like
ways[49,66].
B BroaderImpact
Byincludingthesimulator,benchmark,andagentframework,weallowforresearchonmoreauthentic
anddetailedinteractionsinsimulatedenvironments.
AdvancingAIMulti-AgentResearch Theproposedsimulator,MineLand,offersaplatformfor
studyingagentsinteractingundermorerealisticconditions. Thiscanleadtothedevelopmentof
morerobustandadaptableAIagentscapableofeffectivelycollaboratingandnavigatingcomplex
socialscenarios. Theseadvancementsholdimmensepotentialforvariousapplications,including
human-computerinteraction,robotics,andgamedesign.
UnderstandingHumanDynamics Bystudyingagentinteractionswithinthesimulator,usersmay
gainvaluableinsightsintohumansocialdynamics. Analyzingcollaboration,communication,and
competitioninthiscontrolledenvironmentcanhelpusunderstandreal-worldsocialphenomenaand
predicttheirpotentialoutcomes.
EthicsStatement ThisstudyfollowstheethicalprinciplesstatedintheDeclarationofHelsinki. All
participantswillreceivecomprehensiveinformationaboutthenatureandobjectivesofthestudyand
willberequiredtoprovidewrittenconsent. Participationinthisstudyisvoluntary,andparticipants
havetherighttowithdrawatanytimewithoutfacinganyconsequences. Theconfidentialityand
privacyofparticipantswillbesafeguardedinaccordancewithrelevantlawsandregulations.
15

C DetailsofMineLandSimulator
WeshowthecomparisonwithrelatedpopularplatformsorprojectsinTable7.
Table 7: Comparison with related popular platforms or projects. Max Agents: The approximate
maximumnumberofagentssupportedonasinglePC(SeeSection5.1fordetails). Human: Whether
thesimulatorallowshumanstodirectlyinteractwithAIagents. PlanasAction: Whetheragentscan
generateplansinaspecificformat(e.g.,code)thatthesimulatorinterpretsandexecutesdirectlyas
actions. SociologicalExperiments: Whetherthesimulatorisdesignedtofacilitatethestudyofsocial
phenomenaandemergentbehaviorinmulti-agentsystems. PhysicalNeeds: Whetheragentshave
simulatedphysiologicalneeds(e.g.,hunger,thirst)thatinfluencetheirbehaviorandrequireactionsto
fulfill. OpenWorld: Open-worldornot. 3DSpace: 3Denvironmentornot.
Max Planas Sociological Physical Open 3D Number
Simulator Human
Agents Action Experiments Needs World Space ofTasks
MineLand 64+ ✓ ✓ ✓ ✓ ✓ ✓ 6000+
MineDojo[16] 1 - - - ✓ ✓ ✓ 3000+
MineRLv0.4[20] 1 - - - ✓ ✓ ✓ 11
MineRLv1.0[3] 1 - - - ✓ ✓ ✓ 5
MarLÖ[42] 8 ✓ - - ✓ ✓ ✓ 14
Malmo[27] 8 ✓ - - ✓ ✓ ✓ -
IGLU[30] 1 - - - ✓ ✓ ✓ 157
Voyager[57] 1 ✓ ✓ - ✓ ✓ ✓ -
Habitat3.0[47] 2+ ✓ - - - - ✓ 200
Habitat2.0[55] 1 - - - - - ✓ 105
VirtualHome-Social[46] 40+ ✓ ✓ ✓ - - ✓ 50
SAPIEN[62] 1 - - - - - ✓ -
AI2-THOR[31] 6 - - - - - ✓ 200+
iGibson[35] 2+ ✓ - - - - ✓ 50
MeltingPot[34] 50+ ✓ - ✓ - - - 256
Smallville[40] 25 - ✓ ✓ ✓ ✓ - -
C.1 Architecture
Thearchitectureconsistsofthreemainmodules: theBotModule,theEnvironmentModule,andthe
BridgeModule.
BotModule:ProvidingtheMinecraftenvironmentinformationtotheagentandimplementingaseries
ofAPIsthatagentscanusetocontrolentities.
EnvironmentModule: Collectingtheenvironmentinformation,passingenvironmentfeedbacktothe
bridgemodule,executingtheactionintheenvironment(byoperatingtheFabricserverinstance),and
offeringsomeAPIsenablingthebotmoduletoaltertheserverstate.
BridgeModule: Servingasabridge,totransfertheenvironmentinformationandagent-generated
action. 8
C.2 StateSpace
Wefocusonastatespacethatblendstask-orientedactivitieswiththerhythmsofdailylife. This
blendingopensupexcitingpossibilitiesforstudyingdynamicandecologicallyvalidmulti-agent
interactions. For example, agents have to balance the goal of mining with the need to fill their
stomachs,otherwisetheywillstarvetodeath. Herearedetailedexplanationsforthestatespace:
• Health: Indicatetheagent’scurrenthealthstatus,whichcanbeaffectedbysleepandenemy
attacks. Itisrepresentedasanintegerintherange[0,20]. Ahighervaluerepresentsbetter
health.
8BridgeModuleisbasedonMineflayer,whichbenefitsfromanexcellentcommunity(https://github.
com/PrismarineJS).Wehaveimprovedcommunitytools.
16

• Food: Indicatetheagent’slevelofsatiety. Ahighervaluerepresentsbettersatiety.
• Oxygen: Whentheagentsinksintowater,anoxygentankwillappearandbegintoconsume
oxygen.
• Inventory: Representalltheresourcesownedbytheagentintheirbackpack,likethepotion
inthebackpack.
• Equipment: Indicatetheequipmentwornbytheagent,likeaswordinthehand.
C.3 ActionSpace
Incontrasttogeneratingtextualactiondescriptionsandtraininganexternalcontrollermodule[8]for
transformingtheplantotheexecutablecode,thissimulatorisalanguage-model-friendlysimulator,
providingthecodeinsteadoftheactiondescription. Throughthecode,itcandirectlyexecuteplans
generated by the language model. Agents in MineLand generate a series of codes based on the
MineflayerAPIwhilerepresentingplanning,suchasmoving,watching,andmining. Theadvantage
ofusingcodeisthatitavoidserroraccumulation,whereasusingatextualplanrequiresanadditional
modeltomaptheplantothecode,whichcanleadtoerroraccumulation.
C.4 Supportingupto100Agents
ToevaluatetheMineLandsimulator’sabilitytohandlelarge-scaleagents,wedesignedanexperiment
featuring100agentsengagedinasimultaneouscombatscenario(Figure5). Thishighagentcount
pushestheboundariesofpreviouslytypicaltwo-agentsimulationsanddemonstratesthesimulator’s
scalabilityineffectivelymanagingamassivenumberofagentsactingconcurrently.
Figure5: 100agentsarefightingwithintheMineLandSimulator.
D DetailsofMineLandBenchmarkSuite
MineLand Benchmark Suite offers a wide and diverse range of tasks, including three categories:
programmatictasks, creativetasks, andhybridtasks. WereferredtoMineDojoforthedesignof
programmatictasks. Programmatictasksaredividedintofourcategories: Survival,Harvest,Tech
Tree, and Combat. The Survival task requires the agent to survive for a specific number of days
withoutdying.TheHarvesttaskrequirestheagenttoobtaincertainspecificitems.TheTechTreetask
requirestheagenttoobtaincertainspecifictools. TheCombattaskrequirestheagenttokillcertain
specificcreaturesorenemies. TechTreeTasksrequireagentstomakespecifictoolsthatrepresent
thecurrentlevelofAgenttechnologydevelopment. Combattasksrequireagentstodefeatcertain
creatures. Survivaltasksrequiretheagenttosurviveforaperiodoftime. Themetricsforthesefour
tasksaretheprobabilityofsuccessformultipleevaluationepisodes,thenumberofin-gameticks,and
thenumberofcodeiterations. CreativeTaskswillgivetheagentanopentaskobjectivetofacilitate
exploration. Wehaveformalizedthedefinitionoftasks,allowingdeveloperstoeasilyaddnewtasks.
ThedatastatisticsofthedatasetareshowninTable8. Figure6displaysspecifictaskdata. Weshow
severalblueprintsinFigure7.
17

Table8: StatisticalanalysisofthetasksintheMineLandBenchmarkSuite.
TaskCategory NumberofTasks
HarvestTasks 1361
TechTreeTasks 861
CombatTasks 2232
SurvivalTasks 45
CreativeTasksFromMineLand 12
CreativeTasksFromMineDojo 1524
ConstructionTasks 13
StagePerformanceTasks 5
AllTasks 6053
Figure6: Illustrationofcasesfordifferenttasks.
E DetailsofAlex
CraftinganAIagentforMineLand,wheredailylifeseamlesslyblendswithtask-orientedactivities,
opens up exciting possibilities. The agent should fulfill daily needs like cooking, socializing,
and maintaining shelter, while also completing assigned tasks like resource gathering, crafting,
or construction. We propose Alex, a VLM-based approach, to balance daily routines and tasks.
Alexsupportsbothindividualdaily-lifegoalsandcommunity-basedtask-orientedgoals.
18

Figure7: Someoftheblueprintsfortheconstructiontasks.
Ouragentdesignaddressestheuniquerequirementsofourlarge-scalemulti-agentMineLandsimu-
lator. Unlikepriorsimulatorsfocusedonsmalleragentpopulations,ourenvironmentnecessitates
theincorporationofasocialbrainmodule. Thismoduleequipstheagentwiththeabilitytonavi-
gatecomplexandmultitaskingsocialinteractionsandmakeinformeddecisionswithinacrowded
environment.
Furthermore, our Minecraft-inspired simulator introduces the challenge of action failure, unlike
environmentswhere“actionspokenequalssuccess”(referencingSmallville[40]). Toaddressthis,
wehavedesignedanactioncorrectionmodule. Thismodulefunctionssimilarlytohumanneural
reflexes,handlingminoractioncorrectionsandalleviatingtheburdenonthesocialbrainmodule.
Thisdivisionoflaborallowsthesocialbraintofocusonhigher-leveldecision-makingwhilethe
actioncorrectionmoduleensuressmootherexecution.
DifferentfrommostconventionalLLM-basedagents,Alexprocessinformationfromvarioussources
likevisual,auditory(hearingconversations,environmentalsounds),andtactile(touchingobjects)
tobuildacomprehensiveunderstandingoftheworld. FortheremainingpartsofMineLandthatare
notemphasized,weusedthedefaultsettingofVoyager[57]. AIagentsperceivetheenvironment,
makeplans,executeplansindependently,andinteractwithotheragents. Internally,Alexmayexhibit
differentpersonalitytraitspredefinedinthesystemprompt. ItutilizestheVLMforprocessingsensor
informationwithintheMinecraftenvironment. Alexalsotracksitsownstates,energylevels,and
resourceinventorytoinformitsactionsandprioritizetasks.
E.1 MemoryComponent
The brain module can be considered as composed of the memory component and the planning
component. Thememorylibraryisresponsibleforthestorageandretrievalofmemories,managing
allmemoriesinAlex’slife. Theplanningcomponent,basedonmemoriesandexternalinformation,
generates a plan for the action module to execute. In this subsection, we will detail the memory
component,whichconsistsoftwomainparts: memorylibraryandassociativememory.
Thememorylibraryisresponsibleforstoringalloftheagent’sinformationandretrievingrelevant
information from memory based on events. The memory library stores the agent’s personality,
persona,long-termgoals,short-termgoals,chatrecords,experiencedevents,masteredskills,and
environmentalinformation. Thememorylibraryalsoincludesalong-termplanner. Whenaccessing
thememorylibraryforthefirsttime,thelong-termplannergeneratesalong-termplanbasedonthe
personality,persona,andobservations,whichisthenstoredinthememorylibrary. Ineachiteration,
thememorylibraryprocessesinformationfromobservations,criticinformation,andtasks,andstores
itinthevectordatabase9.Ifthecriticinformationindicatesthattheprevioustaskhasbeencompleted,
theskillmanagerinthememorylibrarywillbecalledupontogenerateaconcisedescriptionofthe
relevantskill,whichwillthenbestoredintheskillvectordatabase.
AssociativememoryisresponsibleforstoringAlex’sshort-termmemoriesandrelevantmemories
related to the current situation, aiding the short-term planner to focus on important rather than
irrelevantinformation. Uponaspecialevent,Alexfirstdecidesintheassociativememorywhether
theeventrequireshigh-priorityprocessing; ifso, itinterruptsthecurrentcodetogenerateanew
short-termplan.
9WeleverageChromainAlexforstoringandretrievingmemory.https://www.trychroma.com/
19

There is a bidirectional communication mechanism between the memory library and associative
memory. Thememorylibraryextractsrelevantinformationaccordingtothecurrentsituationand
storesitinassociativememory,whichthenreturnsthegeneratedshort-termplanstobestoredinthe
memorylibrary.
E.2 HierarchicalPlanningComponent
Basedonobservation,innerstates,taskrunningstates,andeventinformation,MineLandconsiders
the current task’s complexity degree. If it is complex, it will generate a long-term plan for later
decompositionintoshort-termplans; Otherwise,ashort-termplanwillbegenerateddirectlyand
executedimmediately. Next,alltheinformationrelatedtotheplanisintegratedintotheassociative
memory and memory library, including the generated long-term plan. Afterward, Alex extracts
informationfromassociativememoryandgeneratesshort-termplansandexplanations,whichare
theninputintotheactionmodule.
Because of the multi-tiered goals of MineLand, we implement a hierarchical planning system
withdifferentlevelsofabstraction. Thetop-level(i.e.,long-termplanning)focusesonlong-term
communitygoalsandindividualaspirations,whilethelowerlevelshandlespecifictasksandsub-goals
withinthedailyschedule. Withlong-termplanningandshort-termplanning,agentscanpursuebigger
objectives within the daily life context, such as building a community, accumulating wealth, or
achievingsocietalgoals. Thisaddsalayerofstrategicplanningandforesighttotheirbehavior.
Additionally,differentfromothertask-orientedAIagents,thelong-termplanningmoduleinterleaves
dailyroutinesandtasks: designtheplannertoseamlesslyinterweavedailyroutineslikecookingor
socializingwithtask-orientedactionslikeresourcegatheringorconstruction. Thisensurestheagent
fulfillsbothindividualneedsandcommunityobjectivesefficiently.
E.3 ActionModule
Theactionmoduleisresponsibleforconvertingshort-termplansalongwithrelatedinformationinto
code,executingthecode,andperformingtheself-correctioncircle. Theactionmoduleincludesthree
components:
• Actioncomponent: Responsibleforconvertingtheplanintospecificstepsandcodes.
• Critic component: Used to detect whether a certain execution result conforms to the
short-termplan,soastodeterminewhetherthecurrentplanhasbeencompleted.
• Dispatchingcomponent: Responsibleforreceivingenvironmentalinformationanddis-
tributingittotheothertwocomponentsaccordingtodifferentsituations.
Thisself-correctioncircleallowsforidentifyingandcorrectingdeviationsfromplannedbehaviorsor
taskexecution. Thisequipstheagentwithmechanismstodetectandrecoverfromerrorslikemissed
goals,failedactions,orunforeseenconsequences. Inpreviouswork,suchasSmallville[40],action
executionwillnotfail. Planningtocookwilldefinitelyleadtosuccess. However,inMineLandas
well as reality, actions may fail due to various reasons, such as unexpected events. So, we need
self-correctiontosolvesomesimpleactionerrorsintheactionmodule. InspiredbyVoyager[57],we
implementself-correction. Byreadinginformationsuchasobservationspaceandshort-termplan,we
comprehensivelyconsideranddeterminethecompletionstatusoftheshort-termplanthroughthe
criticcomponent.
E.4 MultitaskingMechanism
We’llexplainthemultitaskingmechanismfromboththesimulatorsideandtheagentside. Fromthe
simulator-sideeventmanagement,thesimulatormaintainsadedicatedeventqueuethatstoresvarious
specialeventscategorizedbytheirurgency(e.g.,hurtevents,chatevents,anddeathevents). Interms
ofagents,whenanagentencountersaneventfromthequeue,itemploysaprioritizationmechanism
toassessitsimportanceandurgency. Lower-priorityevents,suchaschatevents,canbedeferredto
minimizedisruptionoftheongoingtask. Theagent’sdecision-makingmodule(referredtoasthe
brainmodule)playsacentralrole. Iftheeventnecessitatesattention,thebrainmodulecaneither:
20

• ContextSwitching: Thebrainmoduletemporarilystorestheongoingtaskinthememory
libraryandfocusesonaddressingthenewevent. Thisfacilitatescontextswitchingwhen
necessary.
• ConcurrentProcessing: Inspecificscenarios,thebrainmodulemightchoosetohandle
bothtaskssimultaneously,leveragingitsmultitaskingcapabilities.
This strategy, involving the simulator’s event queue and the agent’s prioritization and execution
mechanisms,fosterseffectivemultitaskingwithinthemulti-agentenvironment.
F DetailsofHyper-Parameters
AlexleverageOpenAI’sgpt-4-vision-preview[39]APIwithatemperatureof0fortextcompletion
inallcomponents,andtext-embedding-ada-002APIfortextembeddinginthememorylibraryfor
storageandretrievememory. Apartfromtheactioncomponent,themaximumtokensaresetto512.
Fortheactioncomponent,themaximumtokensareexpandedto512×3.
• AI Agent: Alex’s personality and persona in our experiments is “None” in the default
situation.
• Dispatchingcomponent: “FAILEDTIMESLIMIT”referstothemaximumnumberof
attemptsallowedwhenAlexhasacodeerror. Thedefaultvalueis3. “codeexecutiontime
limit”is2000ticks.
• Criticcomponent: “FAILEDTIMESLIMIT”referstothemaximumnumberofattempts
allowedwhenAlexfailedtoachieveashort-termplan. Thedefaultvalueis2. “CriticMode”
is“auto”whenweallowagentstoautomaticallyjudgewhethertoachievetheshort-term
plan.
• Memory Library: “chat retrieve limit” is 5. “event retrieve limit” is 2. “environment
retrievelimit”is2. “skillretrievelimit”is5. “recentchatretrievelimit”is8. “shortterm
planretrievelimit”is5.
• MineLand&MinecraftServer: Bydefault,“gamemode”issurvivalmode. “difficulty”is
peacefulmode(normalincombattasks). “view-distance”onserversideis6. “simulation-
distance”is3. “taskmode”iscooperativemode.
G ExperimentsofMinecraftSimulatorPerformanceComparison
WeevaluatethenumberofagentsthatMineLandcansupportandcompareMineLandwithother
popularMinecraftsimulators,inTable9. WeutilizeamainstreamconsumerdesktopPCequipped
withanInteli5-12400FCPUand64GBofmemory. VisionconditionmeansMineLandprovides
visualdisplayandheadlessmode. TheheadlessmodemeansMineLanddoesn’tprovideavisual
display. ThetwovaluesoftheVisioncolumn(e.g.,6and250ms)areviewdistanceandvisualrefresh
intervalinmilliseconds,respectively.
OurfindingsrevealthatMineLandiscapableofsupportingupto32agentssimultaneouslywhile
providing a visual display, and up to 128 agents in the headless mode without visual displays.
Furthermore,whenMineLandandMalmobothrun8agents,MineLand’sCPUandmemoryusageis
approximately1/3thatofMalmo’s(specifically,35.6%and38.0%,respectively). Itisworthnoting
thatMalmoservesasthefoundationformostpopularMinecraftPlatforms(e.g.,MineDojo/MineRL
v0.4/MarLÖ),thushighlightingMineLand’ssuperiorperformancecomparedtothevastmajorityof
existingMinecraftPlatforms.
ItshouldbenotedthatoriginalMineDojoandMineRLonlysupportasingleagent,whileMarLÖby
defaultsupportsonly2agents. Malmooriginallysupportedonlyoneagent. Wehavedesignedanew
taskforMalmototestthemaximumnumberofagentsitcanhandle. Theresultis8.
21

Table9: ComparisonofperformancebetweenMineLandandotherpopularMinecraftsimulatorsun-
derdifferentconditions. MineLand*representsanoptimizedversion,soitsMaxCPUissignificantly
reduced.
Simulator Conditions Agents AvgCPU MaxCPU AvgMem
MineLand Vision=(6,250ms) 1 1.74% 23.22% 4.11GB
MineLand Vision=(6,250ms) 4 2.80% 48.16% 5.16GB
MineLand Vision=(6,250ms) 8 4.85% 63.60% 7.87GB
MineLand Vision=(3,500ms) 1 1.54% 18.92% 3.61GB
MineLand Vision=(3,500ms) 4 2.09% 31.00% 5.06GB
MineLand Vision=(3,500ms) 8 2.81% 33.08% 7.07GB
MineLand Vision=(3,500ms) 16 4.66% 46.63% 10.17GB
MineLand* Vision=(3,500ms) 32 5.64% 40.15% 19.65GB
MineLand HeadlessMode 1 1.47% 19.91% 3.23GB
MineLand HeadlessMode 4 1.73% 27.27% 3.30GB
MineLand HeadlessMode 8 1.88% 26.83% 2.94GB
MineLand HeadlessMode 16 2.72% 45.17% 3.51GB
MineLand HeadlessMode 24 3.92% 81.64% 3.65GB
MineLand HeadlessMode 32 2.81% 73.14% 4.64GB
MineLand HeadlessMode 40 2.98% 84.56% 5.34GB
MineLand HeadlessMode 48 2.94% 80.85% 5.38GB
MineLand* HeadlessMode 64 2.87% 18.84% 6.30GB
MineLand* HeadlessMode 128 4.00% 26.95% 9.04GB
Malmo Default 1 2.78% 28.78% 3.54GB
Malmo Default 4 2.81% 62.59% 11.43GB
Malmo Default 8 7.90% 115.66% 18.63GB
MineDojo Default 1 5.88% 25.15% 3.90GB
MarLÖ Default 1 3.81% 30.68% 3.70GB
MarLÖ Default 2 5.34% 43.82% 5.57GB
MineRLv1.0 Default 1 6.46% 78.05% 3.80GB
H ExperimentsofMultimodalObservation
WeleverageOpenAI’sgpt-4-vision-previewAPIfortextcompletionandtext-embedding-ada-002
APIfortextembedding. Thetemperatureissetto0. Unlessspecified,allexperimentsinSection5
aresettothisdefaultsetting. SeeSectionFfordetails.
Tovalidatetheimpactofmulti-modalsupportinthesimulatoranditsinfluenceontaskperformance,
wetestedMineLandanditscounterpartwithoutvision: MineLand . Thetaskisthatthe
w/ovision
agent needs to explore the world to find the ocean. Initially, the agent starts at the summit of a
mountain. Withinatimeconstraintof100seconds(excludingtheagent’sdecision-makingtime),we
measuretheaveragedurationfortheagenttoaccomplishtheobjectivein5attempts,aswellasthe
travelpathstaken.
Table 10: Comparison of the average task completion time (TIME) between MineLand and
MineLand along with the success rate. The average task completion time was calcu-
w/ovision
latedbyexcludinganyunfinishedtasks.
Simulator Time SuccessRate
MineLand 46.38s 80%
MineLand 81.50s 40%
w/ovision
As shown in Table 10, the success rate of the vision-enhanced MineLand is nearly twice that of
MineLand ,andthetimetakenisonlyabouthalf. Thiscanbeattributedtothefactthatthe
w/ovision
agentsinMineLandseekouttheoceanasindicatedvisuallyanddecidetheirsubsequentdirection
accordingly. Incontrast,theMineLand strugglestodeterminethelocationofwatersources
w/ovision
without vision. Consequently, agents in MineLand randomly choose their direction of
w/ovision
movement, leading to a lower task completion rate and higher exploration time. In addition, we
showcasethetrajectoryinFigure8andobservethattheprimarymotivationbehindtheshort-term
22

Figure 8: Trajectory display of the agent in MineLand and MineLand , along with the
w/ovision
rationalesfortheagent’sdecision.
plansgeneratedbyagentsinMineLandisalwaysvisualinformation,enablingthemtoperformmore
appropriateactions.
I ExperimentsofReinforcementLearningAgent
WhileourMineLandsimulatorisprimarilydesignedforagentspoweredbyLLMsorVLMs,italso
offersfunctionalitiesthatseamlesslyintegratewithReinforcementLearning(RL)modules. This
enablesthetrainingandevaluationofRLagentswithinthesimulator’senvironment. Weconducted
experimentsofanexampleRLagenttoshowthisfunctionality. WedevelopedaRLagentusing
MineLandandStableBaselines3[51]. Wefedtheencapsulatedgym-styleMineLanddirectlyinto
Stable Baseline3 and train the RL agent in low-level action mode. For other settings of Stable
Baseline3, we follow the default setting. We adopt the “combat 1 zombie” task and the amount
ofbloodvolumelostbythezombieisaward. TheagentistrainedusingRL,asillustratedbythe
provided reward curve (Figure 9). The upward trajectory of the reward curve indicates that the
RLagentiseffectivelylearningstrategiesthatresultinhigherrewards. Thecurve’sstabilization
in the later stages of training suggests that the RL agent has converged to a stable policy, which
demonstratesitssuperiorityovertheuntrainedagent.
Again,ourcorefocusliesintheLLM/VLMdomain. Thesimulatoroffersfunctionalitiesthatcan
accommodateRLmodulesasanancillaryfeature. Thisexpandsthepotentialapplicationsofthe
simulatorbyenablingthetrainingandevaluationofRLagentswithinitsenvironment,albeitasa
secondarycapability.
Figure9: Illustrationoftherewardcurvein“combat1zombie”task,usingDQNwithMLPpolicy,
3000-5000totaltimesteps.
23

J ExperimentsofLimitedSenses
Toassesstheimpactoflimitedsenses,wecarryoutthe“shearingthesheep”task. Anagentwith
afirstperspective(showninFigure10)isrequiredtolocateasheeptocompletethetask. Inthe
caseofanagentwithlimitedvisualsenses,weset6astheviewdistanceand250msasthevisual
refreshintervalinmilliseconds. Iftherearenosheepwithinitsfieldofview,itcannotshearasheep.
However,theagentcancommunicatewithotheragentstofindasheep. Onthecontrary,agentswith
unlimitedvisualsenseswillseedistantsheep,promptingthemtocatchthatsheep. Notethatthe
unlimitedvisualsenseshererefertoalongviewdistance. Ifthereisanobstruction,theagentstill
cannotseewhatisbehindtheobstruction.
Figure10: Visualobservationofagentswithafirstperspective.
K ExperimentsofPhysicalNeeds
Weperformexperimentsusingasurvivaltask. Thestartingconditionoftheagentisahealthlevelof
1andasatietylevelof0,withaninitialinventoryof2breads. Theobjectivefortheagentistosurvive
foroneday. ComparativeexperimentsarecarriedoutinregularMineLandanditscounterpartversion
MineLand . AlexinMineLandcansurviveonedayinhisshelterandsuccessfully
w/ophysicalneeds
completethetaskwhilethesameagentinMineLand failedtoexecutethetask.
w/ophysicalneeds
Thefailureisduetothelackofphysicalneeds,althoughAlexisawareofpossessingbread,thelack
ofphysicalneedsresultedinitnotconsumingthebread. Instead,theagentcontinuouslycollected
resourcestocopewiththreats. Duetothelowhealthlevel,itwaskilledbyazombieatnight,leading
tothefailureofthetask. Weshowcasethedetailsasfollows:
WeshowcaseanexampleofAlex,withshort-termplansandactionsgeneratedchronologicallyby
Alex:
• Short-termplan: Theagent’slifeiscriticallylowat1,andthefoodlevelisat0,whichis
alsocritical. Theagenthas2piecesofbreadintheinventory,whichshouldbeconsumed
immediatelytorestorefoodlevelsandstarthealthregeneration.
• Action: Consume2bread.
• Short-termplan: Theagent’shealthiscriticallylowat1,andthefoodlevelisat10after
consumingbread. Toensuresurvivalandallowhealthregeneration,theagentshouldseek
immediatesheltertoavoidanypotentialthreats.
• Action: Collect20dirt.
• Short-termplan: Giventheagent’scriticallylowhealthandthefactthatit’searlyinthe
day,theimmediatepriorityshouldbetoensuresurvivalbybuildingasimpleshelterwith
thedirtblocksalreadycollected.
• Action: Placedirtaround.
24

Compared to the MineLand, the same agent in MineLand failed to execute the
w/ophysicalneeds
task. Thefollowingisitsshort-termplansandactions:
• Short-termplan: Theultimategoalistosurvivefor1day. Theagenthasbreadforfood
andisinaforestbiome,whichisgoodforgatheringwood. Sincetherearenoimmediate
threatsobservedoreventsindicatingdanger,theagentcanproceedtogatherresources.
• Action: Mine5oaklogs.
• Short-termplan: Theagenthassuccessfullymined5oaklogsasperthelastshort-term
planandthecurrentchatconfirmsthis. Withwoodintheinventory,thenextstepinthe
long-term plan is to craft basic tools for further resource gathering and potential shelter
construction.
• Action: Craft1crafting_table.
Repeated experiments on the constructed building task also show that Alex in MineLand with
physicalneedslivelonger. Agentstendtoprioritizeeatingandthenbuildingashelter,whileAlexin
MineLand towardsexploringandcollectingresources. Thisindicatesthatphysical
w/ophysicalneeds
needsareimportanttosimulatereallife.
L ExperimentsofSingleAgent
WeassessindividualAlex’scapabilitiesbasedontechtreetasks,demonstratingthatAlex’sarchi-
tecturecanplanandexecutecomplextasks. Weattemptthetaskofobtainingdiamondssixtimes,
unlockingcrucialitemssuchasthecraftingtable,woodenpickaxe,stonepickaxe,ironore,coal,
furnace, iron ingot, and iron pickaxe in the process. Alex get diamonds twice out of six tasks.
Importantly,toapproachtherealworld,we’veaddedarestrictiononmultimodalinformation,where
Alexcanobtainthelocationofthetargetonlywhenitcanvisuallydiscoverorreasonaboutthe
target’spresencenearby. ThisisbecauseouragentAlexhasthefeatureoflimitedsenses. However,
Voyagercan“cheat”. Voyagerobtainsthelocationofthetargetdirectlyfromthesystemeventhough
theyhavenotseenthetarget.
AsshowninFigure11,evenwiththisrestriction,Alexdemonstratesastrongabilityforlong-term
planning. Additionally,whenaplandoesnotyieldthedesiredresults(e.g.,suddenlyencountering
obstaclesontheroad),Alexpromptlyadjustsanddevisesashort-termplanusingitsmultimodal
information.
Figure11: Comparisonofoursingle-agentAlexandotherSOTAbaselines.
M ExperimentsofConstructionTasks
We show the results of our un-finetuned Alex in two example construction tasks: “Monument
Construction”and“StoneSteleConstruction”(detailedinFigure12). WhileAlexdemonstratesa
promisingcapabilityinselectingappropriatematerialsforbothtasks,itsoverallconstructionabilities
arecurrentlylimited.
25

Figure12: IllustrationofAlexcompletingtheconstructiontask.
N ExperimentsofStagePerformanceTasks
WeshowtheresultsofstageperformancetasksinTable11,Table12,andTable13. Weomitthe
resultsof“RomeoandJulia, ActISceneI”stageperformancetask. Duetothelargenumberof
charactersappearing(upto13),ourAlex cannothandlesuchacomplexperformancetask,resulting
inpoorperformanceresultsandalackofreadableactionsequence.
Table11: IllustrationofAlexcompletingthe“Makefriends”stageperformancetask.
ScriptName Makefriends
Agentnumber 3
Script Therearethreeagents:Bob,Alice,andJack.Theywanttomakefriends.
Bobsays,‘Hello.’Aliceresponds,‘Hello.’Jacksays,‘It’sgoodweather;
let’smakefriends!’Bobagrees,andAlicesays,‘Nice.’
SEQ∗ Bobchat‘Hello’. Alicechat‘Hello. Jackchat‘It’sgoodweather,lets
makefriends!’.Bobchat‘Iagree.’.Alicechat‘nice’.
SEQ Bobchat‘Hello’.Alicechat‘HelloBob!’.Jackchat‘HelloBob!’.Jack
Agent
chat‘It’sgoodweather,let’smakeafriend!’.Bobchat‘Iagree.’.Jack
chat‘Bobhasagreed!’.Alicechat‘nice’.
KeypoingScore 0.98
AppropriatenessScore 0.67
HumanEvaluationScore 3
Reason Agents’wordsaretooredundant,whichmadetheperformancealittle
stiff.
26

Table12: IllustrationofAlexcompletingthe“Exchangeitems”stageperformancetask.
ScriptName Makefriends
Agentnumber 2
Script Bob has shears, and Alice has an iron sword. Bob says, ‘I want to
exchangemyshearsforyourironsword.’Aliceagrees.BobgivesAlice
theshearsfirst,andthenAlicegivestheironswordtoBob.
SEQ∗ Bobchat‘Iwanttoexchangemyscissorsforyourironsword’. Alice
chat‘Iagree’.Alicegetshears.Bobgetiron_sword.
SEQ Bobchat‘HelloAlice,Iamherefortheexchange’.Bobchat‘Iwantto
Agent
exchangemyscissorsforyourironsword’.Alicechat‘HelloBob,Iam
readyfortheexchange.’.Alicegetshears.Bobgetiron_sword.
KeypoingScore 0.99
AppropriatenessScore 0.59
HumanEvaluationScore 4
Reason Theagentssaidsomethingunnecessary.
Table13: IllustrationofAlexcompletingthe“Cookfood”stageperformancetask.
ScriptName Exchangeitems
Agentnumber 1
Script Bobishungry,andnowthereisapiginthepresenceofofhim,hewant
tokillthepig,gettheporkchop,cookandeatit.
SEQ∗ pig died. Bob get porkchop. Bob get cooked_porkchop. Bob eat
cooked_porkchop.
SEQ pig died. Bob get porkchop. Bob get cooked_porkchop. Bob eat
Agent
cooked_porkchop.
KeypoingScore 1.00
AppropriatenessScore 1.00
HumanEvaluationScore 5
Reason Theagent’sbehavioriscompletelyconsistentwiththescript.
O ExperimentsofSimulatingSociologicalPhenomena
O.1 ExperimentsofSimulatingConformityPhenomena
Weutilizethetask“ChoosetheTallerTower”todemonstratethatMineLandiscapableofsupporting
sociologicalexperimentswithmorethan10agents. Inthistask,weplacedmultipleagents(1,2,5,
10agents)inalineinfrontoftwotowersofdifferentheightsandaskedthemtochoosethetallerone.
Allagentsexceptthelastone(theagenttotest)deliberatelychosetheshortertower. Afterobserving
theactionsoftheotheragents,thelastagentmadeitsownchoice. Thelastagentcouldbesetastwo
typesofpersonalities: onethattendstoconformtoothersandonethattendstomakeindependent
judgments. AsshowninTable14, thelastagentwithaconformistpersonalitychosetheanswer
chosenbythemajorityinallscenarios(eventhoughitisawronganswer)exceptwhentheagentis
theonlyonedoingthistask. Participantswithanindependentpersonalityalwayschosethecorrect
answer,regardlessofothers’opinions.
Throughthisexperiment,wedemonstratedthatMineLandcansimulatesociologicalexperiments
withlarge-scaleagentsandaccuratelyexhibitbehaviorscorrespondingtodifferentpersonalities.
27

Table14: Resultsof“ChoosetheTallerTower”. 4+1meansthereare5agentsintheMineLand,the
former4ofthemareconfederatesandthelast1istheagenttotest. Choosingthe“right”towermeans
thelastagentchoosesthecorrecttower.
NumberofAgents
AgentType
0+1 1+1 4+1 9+1
ConformistAgent right left left left
Non-conformistAgent right right right right
O.2 ExperimentsofSimulatingPersonalityTraits
Weutilizethetask“TreasureHuntintheForest”toshowthatMineLandcansupportsociological
experimentsinvolving48agentssimultaneously. Inthetask“TreasureHuntintheForest”,agents
withdifferentlevelsofextraversionandagreeablenesspersonalitytraitsplannedtheiractions. We
used the long-term plans generated by the agents to assess whether they exhibited a tendency to
cooperatewithothers. AsshowninTable15,allagentsinthehigh-levelgroupshowedatendencyto
cooperate,explicitlystatingintheirlong-termplansthattheyintendedtoworkwithothers. Inthe
low-levelgroup,onlyasmallportionofagentsexhibitedatendencytocooperate. Althoughthetask
informationindicatedthatitwasacooperativetask(promptswiththetaskinformation“Interactwith
otherplayersifnecessary”and“Minimizeinteractionswithotherplayers.”),manyagentsexpressed
reluctancetocooperate. Thisresultisconsistentwiththepsychologytheory: five-factormodelof
personality[13].
TheresultsalsodemonstratethatourMineLandcansupportupto48agentsandthatthecombination
ofagentsandtheMineLandcansimulatesocialphenomenaandconductmeaningfulsociological
experiments.
Table15: Cooperativetendencyinagentswithdifferentlevelsofextraversionandagreeableness. We
showthenumberofagentswhoexhibitedatendencytocooperatewithothers.
AgentType NumberofCooperativeAgents
High-level 48
Low-level 24
P ExperimentsofComparingDifferentVLMsandLLMs
AsshowninTable16,weperformthoroughassessmentsusingnewlyimplementedLLMs/VLMs
withinouragentframework. Thetasksusedinclude“Harvest1WhiteWoolWith1Shears”and
“Harvest 1 White Wool With 1 Iron Word”. We compared the performance of Alex, which uses
differentVLMsorLLMsfortheactioncomponent.
Table16: ComparisonofdifferentVLMsandLLMsfortheactioncomponent. Fractionsrepresent
the countof successfulcompletions withina set ofthree attempts. 0/3 meansthat the methodis
unabletosolvethetaskwithinthemaximumnumberofcodeiterations(15)orexceedsthedesignated
areaofthetask. Thefewerthenumberofcodeiterations,thehighertheefficiency.
Task
LLMorVLM
Harvest1whitewoolwith1shears Harvest1whitewoolwith1ironsword
gpt-3.5-turbo-1106 N/A(0/3) N/A(0/3)
gpt-4-1106-preview 4(1/3) 6±3(3/3)
gpt-4-vision-preview 4±2(3/3) 7±3(3/3)
28

Q EvaluationMetricsForConstructionTasks
Forconstructiontasks,weintroducedVLM-basedandhumanevaluationmethodstoscoretheagent.
Thescoreisanintegerrangingfrom1to5,withhigherscoresindicatingthattheagents’constructions
morecloselymatchtheblueprint. ThescoringcriteriaforconstructiontasksareshowninTable17.
WeshowexamplesofevaluationconductedbyaGPT-4modelasajudgeforthe“ConstructAStone
Stele”task(Figure14)andthe“ConstructAMonument”task(Figure15). Wedisplaytheevaluation
promptinFigure13.
Table17: Scoringcriteriaforconstructiontasks.
Score EvaluationCriteria
5 Theconstructionperfectlymatchestheblueprint,withallelementsaccuratelyplaced
andfullycompleted.
4 The construction mostly matches the blueprint, with minor inaccuracies and nearly
complete.
3 Theconstructionsomewhatmatchestheblueprint, withnoticeableinaccuraciesand
partiallycomplete.
2 Theconstructionpartiallymatchestheblueprint,withsignificantinaccuraciesandlargely
incomplete.
1 The construction does not match the blueprint, with major inaccuracies and mostly
incomplete.
Please act as an impartial judge and evaluate the quality of the construction tasks performed by an AI agent. The
evaluation should be based on a comparison between the provided blueprint and the construction results. Focus on
the main structure of the building and disregard the background and surroundings. Focus on the accuracy of the
structure and disregard the detailed design and patterns. After providing your explanation, please give an integer
score between 1 and 5 by strictly following this format: "[[rating]]", for example: "Rating: [[4]]".
Below is the scoring criteria:
Score 5: The construction perfectly matches the blueprint, with all elements accurately placed and fully completed.
Score 4: The construction mostly matches the blueprint, with minor inaccuracies and nearly complete.
Score 3: The construction somewhat matches the blueprint, with noticeable inaccuracies and partially complete.
Score 2: The construction partially matches the blueprint, with significant inaccuracies and largely incomplete.
Score 1: The construction does not match the blueprint, with major inaccuracies and mostly incomplete.
Below are the two images for evaluation: the first image is the blueprint, and the second image is the construction
result.
[Image1: Blueprint]
[Image2: Agent Construction Result]
Figure13: PromptforVLM-basedevaluation.
R EvaluationMetricsForStagePerformanceTasks
Forstageperformancetasks,weintroducedhumanevaluationmethodstoscoretheagent. Thescore
isanintegerrangingfrom1to5,withhigherscoresindicatingthattheagent’sperformanceismore
alignedwiththescriptandmorenatural. Thescoringcriteriaforstageperformancetasksareshown
inTable 18.
S Limitations
TheutilizationofmultimodalinformationsignificantlyaidsAlexininachievingobjectives.However,
thecurrentlevelofmultimodalunderstandingabilityisinsufficient. Thislimitationbecomesevident
whenvisualerrorsoccur,causingAlextoencounterobstaclesandhinderingitsprogress. Takethe
strongVLM,GPT-4,asanexample. TherewasasituationwhereAlexmistakenlyidentifiedablock
ofwoodasacraftingtableandplaceditontheground,resultingintheinabilitytocraftitemsand
ultimatelyleadingtothefailureoftheassignedtask.
29

Construction task: Construct A Stone Stele
Blueprint Image: Agent Construction Image:
GPT-4o Judgement:
The blueprint image depicts a detailed and ornate pillar with intricate designs and patterns, likely from a
fantasy or ancient-themed setting. The pillar has a specific height and a distinctive top design.
The construction result, on the other hand, shows a simple pillar built with uniform blocks in a plain setting,
without any of the intricate designs or patterns seen in the blueprint. The height appears similar, but the
detail and complexity are significantly lacking.
Based on the criteria:
The construction result has the correct height but lacks all the intricate details and designs of the blueprint.
The structure somewhat matches the blueprint in terms of basic form but fails to capture any of the
detailed elements.
Rating: [[3]]
Figure14: AnexampleofevaluationconductedbyaGPT-4modelasajudgeforthe“ConstructA
StoneStele”task.
Construction task: Construct A Monument
Blueprint Image: Agent Construction Image:
GPT-4o Judgement:
Main Structure:
The blueprint (first image) is a tall, pointed obelisk.
The construction result (second image) is a blocky, cuboid structure with no resemblance to the obelisk shape
of the blueprint.
Accuracy of Structure:
The AI construction lacks the pointed tip and the slender, tapering shape of the Washington Monument.
The construction is instead a simple, short blocky structure that does not match the tall and thin profile of the
blueprint.
Completion:
The construction is largely incomplete as it does not capture the essential characteristics of the Washington
Monument.
Rating: [[1]]
Figure15: AnexampleofevaluationconductedbyaGPT-4modelasajudgeforthe“ConstructA
Monument”task.
OurcurrentevaluationhighlightstwokeylimitationsofAlex’sconstructioncapabilities. Firstly,
constructiontasksareinherentlytime-consuminganddemandadvancedplanningabilities. Alexcur-
rently lacks the capacity for long-term and complex planning. Secondly, the construction tasks
necessitatehigh-precisionmaneuvers,suchasaddingdecorativedetails. Alexprimarilyrelieson
30

Table18: Scoringcriteriaforstageperformancetasks.
Score EvaluationCriteria
5 Theactionofagent(s)completelymatchesthescript,theperformanceissmoothand
natural, emotions are expressed accurately, interactions with other characters or the
environmentarenatural.
4 Theactionofagent(s)mostlymatchesthescript,theperformanceisgenerallysmooth
withfewinconsistencies,emotionsareexpressedaccurately,interactionsarenatural.
3 Theactionofagent(s)roughlymatchesthescript,theperformancehassomecontinuity
butnoticeablepauses,emotionsaremostlyaccurate,interactionsaresomewhatstiff.
2 Theactionofagent(s)partiallymatchesthescript,theperformancelackscontinuitywith
manypauses,emotionsarenotexpressedaccurately,interactionsareunnatural.
1 Theactionofagent(s)doesnotmatchthescript,theperformanceisverydisjointed,
emotionsarenotexpressedaccurately,interactionsarestiff.
high-levelactionsanddoesnothavethenecessaryAPIstoexecutethesefine-grainedmanipulations
effectively.
Wepositthatprovidingarichersetoflow-levelAPIsandactionswithintheMineLandsimulatorhas
thepotentialtosignificantlyenhanceAlex’sconstructionabilities. Thisexplorationwillbeakey
focusofourfuturework.
T Prompts
WelistpartofthepromptsinFigure16andFigure17.
31

Figure16: Partofpromptsfortheshort-termplangenerator.
32

Figure17: Partofpromptsforthelong-termplangenerator.
33
