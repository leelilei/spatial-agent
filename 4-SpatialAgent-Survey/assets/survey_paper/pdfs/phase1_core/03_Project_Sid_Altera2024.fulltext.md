Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_core/03_Project_Sid_Altera2024.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:25+00:00
- page_count: 35
- status: ok
- text_char_count: 86306

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 2)
  - Why should we try to build an AI civilization? (page 2)
  - The current agent landscape (page 2)
  - Why is it hard to build AI civilizations? (page 2)
  - Our contributions (page 4)
- PIANO Architecture (page 4)
  - Concurrency (page 4)
  - Coherence (page 5)
  - Core modules (page 6)
- Improving single-agent progression (page 6)
  - Minecraft environment (page 6)
  - Single-agent benchmark (page 7)
- Improving multi-agent progression (page 8)
  - Small groups (page 8)
  - Societies (page 8)
- Civilizational progression (page 10)
  - Specialization (page 11)
  - Collective rules (page 13)
  - Cultural Transmission (page 15)
    - Cultural memes (page 15)
    - Religion (page 16)
- Discussion (page 18)
- Limitations (page 18)
- Methods (page 18)
  - Baseline architecture (page 18)
  - Specialization (page 18)
  - Collective Rules (page 19)
  - Cultural Transmission (page 19)
- Contributions and Acknowledgments (page 26)
- Improving single-agent progression (page 27)
- Improving multi-agent progression (page 28)
- Specialization (page 28)
- Collective rules (page 30)
- Cultural transmission (page 33)

Markdown Content:

Project Sid: Many-agent simulations toward AI civilization
Altera.AL1
science@altera.al
AIagentshavebeenevaluatedinisolationorwithinsmallgroups,whereinteractionsremainlimitedinscope
andcomplexity. Large-scalesimulationsinvolvingmanyautonomousagents—reflectingthefullspectrumof
civilizationalprocesses—haveyettobeexplored. Here, wedemonstratehow10–1000+AIagentsbehave
andprogresswithinagentsocieties.WefirstintroducethePIANO(ParallelInformationAggregationviaNeu-
ralOrchestration)architecture,whichenablesagentstointeractwithhumansandotheragentsinreal-time
whilemaintainingcoherenceacrossmultipleoutputstreams. Wethenevaluateagentperformanceinlarge-
scalesimulationsusingcivilizationalbenchmarksinspiredbyhumanhistory. Thesesimulations,setwithin
aMinecraftenvironment,revealthatagentsarecapableofmeaningfulprogress—autonomouslydeveloping
specializedroles,adheringtoandchangingcollectiverules,andengaginginculturalandreligioustransmis-
sion. ThesepreliminaryresultsshowthatagentscanachievesignificantmilestonestowardsAIcivilizations,
openingnewavenuesforlarge-scalesocietalsimulations,agenticorganizationalintelligence,andintegrating
AIintohumancivilizations.
Figure1:Fromagentarchitecturetoagentcivilization
1SeeContributionssectionforcompleteauthorlist.
1
4202
tcO
13
]IA.sc[
1v41100.1142:viXra

1 Introduction
1.1 WhyshouldwetrytobuildanAIcivilization?
For agents to coexist with us in our own societies, they need to be autonomous and collaborative. In
recent years, advancements in reasoning and decision-making in LLMs have significantly enhanced
agentautonomy(52;58;36;45). However,autonomyaloneisinsufficient. AIagentsmustalsocoexist
alongsidehumansandotheragentsinahuman civilization. Inthispaper, wedefineacivilizationas
an advanced society that has achieved a high level of institutional development, which manifests in
specialized roles, organized governance, and advancements in areas like science, art, and commerce.
Wearguethatcivilizationalprogress-measuredbytheabilityofagentstocoexistandprogressinhuman
civilizations-representstheultimatebenchmarkforAIagentability.
Inthistechnicalreport,wedescribeourfirsteffortstoimproveandbenchmarkagentabilityinhuman
civilizations. First,weintroducePIANO(ParallelInformationAggregationviaNeuralOrchestration),
anewcognitivearchitecturedesignedtoenhancebothautonomyandreal-timeinteractionofagents.
UsingPIANO,wesimulatesinglesocietiesof50-100agentsaswellascivilizationsof500-1,000agents
livinginmultiplesocietiesthatinteractwithoneanother. Finally,weevaluateagentperformanceusing
newmetricsthatarealignedwithhumancivilizationalprogress. Weshowthatagentsformtheirown
professionalidentities,obeycollectiverules,transmitculturalinformationandexertreligiousinfluence,
andusesophisticatedinfrastructures,suchaslegalsystems.
1.2 Thecurrentagentlandscape
Modern AI Agents typically consist of multiple LLM-powered modules for reasoning, memory, plan-
ning,andtooluse(49;18;55;20;62). Individualagentshavebeendevelopedforvariousapplications
includingcoding(5;8),webbrowsing(64;42),andgameplay(48).
RecentresearcheffortsinLLM-poweredmulti-agentsystemsgenerallyfallunderthreecategories: pro-
ductivity, games, and social modeling. Multi-agent frameworks have been deployed in software de-
velopment (43; 27), cooperative robotic control (60), scientific experiments (12; 47), and debates (3).
Multi-agent simulations have also been tested in various game environments (56; 13; 30; 28). Sepa-
rately, they’ve been used to model developmental psychology (25; 61), game theory (32), macroeco-
nomics(29;63),socialpolicies(41;54;19),andcommunitydynamics(40;39;10).
Inmanyoftheseworks,agentsarenotcompletelyautonomousandareconstrainedbyeitheragentar-
chitectureorbythesimulatedenvironment. Commonconstraintsincludeturn-basedexecution,con-
strainedworkflows,orrigidcommunicationchannelsbetweenagents(65;21;4).
Severaloftheseworksconsiderlarge-scalesimulations,thoughinrestrictedsettings. Forexample,(40)
and(10)simulatedsocialnetworksofupto18,000personas. Toourknowledge,fullyautonomoussocial
communicationinopen-worldenvironmentshavenotbeenattemptedingamesorothersettings(15).
1.3 WhyisithardtobuildAIcivilizations?
Largeagentgroupshaveyettodemonstratetheabilitytoprogressoverlongtimehorizons. Below,we
reviewthekeyreasonsforthislimitedprogressbeforeoutliningourcontributionstoovercomethem.
Reason1: singleagentsdon’tmakeprogress. LLM-poweredagentsoftenstruggletomaintaina
groundedsenseofrealityintheiractionsandreasoning(Figure2). Agents,evenwhenequippedwith
2

modulesforplanningandreflection,oftenbecomestuckinrepetitivepatternsofactionsoraccumulate
acascadeoferrorsthroughhallucinations,renderingthemunabletomakemeaningfulprogress(57;48;
15). Consideranagentpromptedtobeavillagerinavirtualtown. Whenasked,“whatareyoueating“,
theymayanswer“abagel“,evenifthey’renoteatinganything. Thishallucinatedoutputthenfeedsinto
futureprompts,causingthemtofalselybelievetheynolongerneedtoacquirefood. Therefore,evena
smallrateofhallucinationscanpoisondownstreamagentbehaviorwhenagentscontinuouslyinteract
withtheenvironmentviaLMcalls.
LLM Agent Multi-Agent
Figure2:DatadegradationinLLMs(left),LLM-poweredagents(middle),andinmulti-agentgroups(right). Hallucinations
arerepresentedbygreenskullflasks.HallucinationsthataregeneratedbyasingleLLMpromptcancompoundoversucces-
siveLLMcalls. Anindividualagentthathallucinatescanalsocauseanentiregroupofagentstohallucinatethroughsocial
interactions.
Reason 2: groups of agent’s don’t make progress. Agents that miscommunicate their thoughts
andintentscanmisleadotheragents,causingthemtopropagatefurtherhallucinationsandloop(Fig-
ure2). Consideranagent,Abby,withtwoindependentLLMmodules,oneforfunctioncallingandone
for chatting. If another agent, Bob, asks Abby to “give me a pickaxe”, Abby’s chat LLM call may re-
spondwith“Surething!”,whileherfunctioncallchoosesadifferentaction(“explore”). Bobmightthen
attempttomineusinganimaginarypickaxe. Thiskindofmiscommunication,whichoftenhappensin
groups of agents, leads to dysfunctional behavior and will deteriorate individual performance within
groups. Actionsfrommultipleoutputstreamsmustthereforebebidirectionallyinfluential. Wedefine
thisqualityascoherence.
Maintaining coherence in real-time environments is even more difficult when we require that agents
respondwithminimallatency. Thisisnecessaryforouragentstointeractwithhumanplayers,butis
difficulttoachievewhenagentshavetoreactquicklyandyetsimultaneouslymaintaincoherenceacross
manyoutputstreams. Wenotethatasimplesolutiontothiscoherenceproblemistoproducetalking
andactionoutputsusingasingleLLMcall. However,thisapproachdoesnotscalewhenthenumber
of outputs becomes large, for instance, encompassing talking, gaze, facial expression, and individual
bodyparts.
Reason3: alackofbenchmarksforcivilizationalprogress. Benchmarksforagentshavelargely
focusedonautonomousagentperformanceinavarietyofdomainssuchaswebsearch(38),coding(22),
search and query (51), and reasoning (59; 33). Recently, benchmarks have emerged for multi-agent
3

behaviors,focusedonsmallgroupscenariosthatmeasurecommunication, competition,cooperation,
anddelegation. SomeexamplesincludeBattleAgentBench(50),COMMA(37),VillagerBench(7),and
LLMcoordination(1). However,thesemetricsdonotcaptureadvancementsthatmanyagentscanmake
atthescaleofcivilizations. Webelievethelackofsuchlarge-scalebenchmarkscanbeattributedtohow
technicallydifficultitistoperformsimulationsofhundredsorthousandsofagentsinasingleworld.
The biggest experiments to date have simulated 25-50 agents (39), which is not close to the scale of a
civilization.
1.4 Ourcontributions
Inthistechnicalreport,wemakethefollowingcontributions:
• Anewclassofagentarchitecture,PIANO(ParallelInformationAggregationviaNeuralOrches-
tration)
• Architecturalfeaturesthatimprovesingle-agentprogression
• Architecturalfeaturesthatimprovemulti-agentdynamics
• Benchmarks for long-term civilizational progress in large-scale simulations through specializa-
tion,collectiverules,andculturalpropagation
2 PIANO Architecture
Inthissection,weproposetwobrain-inspireddesignprinciplesforthecompositearchitectureofhuman-
likeAIagents. WecallthisarchitecturePIANO(ParallelInputAggregationviaNeuralOrchestration)to
encompasstheideasofconcurrencyandaninformationbottleneck(Figure3). Justasapianistcoordi-
natesmultiplenotestocreateaharmony,thePIANOarchitectureselectivelyandconcurrentlyexecutes
variousmodulesinparalleltoenableagentstointeractwiththeenvironmentinreal-time.
2.1 Concurrency
Problem. Agentsshouldbeabletothinkandactconcurrently. Forinstance,slowmentalprocesses,
such as self-reflection or planning, should not block agents from responding to immediate threats in
their surroundings. We want the agents to be interactive in real time with low-latency, but also have
thecapacitytoslowlydeliberateandplan.
Currentstate. ThevastmajorityofLLM-basedagentstodayprimarilyusesingle-threaded,sequen-
tial functions (for example, a defined “Agent Workflow”). Single-threaded design assumes that the
agentperformsasingletaskatagiventime,andsequentialdesignassumesthatallmodulesoperateat
similartimescales. Neitherassumptionsarevalidifagentsarecapableofthinkingslowandactingfast
concurrently. Moreover,popularframeworksforgenerallanguagemodelprogramming,suchasDSPy
(24),LangChain(26),ell(31),arenotdesignedforconcurrentprogramming.
Solution. Thebrainsolvesthisproblembyrunningdifferentmodulesconcurrentlyandatdifferent
timescales(34). Likewise,wehavedesignedmodules(LLM-basedandotherwise),suchascognition,
planning, motor execution, and speech, to run concurrently in our agent brain. Each module can be
seenasastatelessfunctionthatreadsandwritestoasharedAgentState. Thedesignallowsdifferent
modulestoberuninappropriatecontexts. Forexample,socialmodulesareselectivelyengagedinsocial
4

(cid:31)(cid:30)(cid:29)(cid:28)(cid:27)(cid:26)(cid:30)(cid:25)(cid:24)(cid:30)(cid:23)
(cid:4)(cid:18)(cid:25)(cid:24)
(cid:13)(cid:18)(cid:16)(cid:14)(cid:12)(cid:20)(cid:13)(cid:26)(cid:26)(cid:16)(cid:20)(cid:11)(cid:10)(cid:24)(cid:12)(cid:20)(cid:9)
(cid:8)(cid:26)(cid:7)(cid:6)(cid:16)(cid:24)(cid:29)(cid:24)(cid:16)(cid:20)(cid:22)(cid:15)(cid:23)(cid:28)(cid:26)(cid:30)(cid:10)
(cid:5)(cid:30)(cid:23)(cid:24)(cid:30)(cid:23)(cid:20)(cid:4)(cid:24)(cid:30)(cid:24)(cid:27)(cid:18)(cid:23)(cid:28)(cid:26)(cid:30)
(cid:3)(cid:24)(cid:25)(cid:26)(cid:27)(cid:129)
(cid:22)(cid:15)(cid:23)(cid:28)(cid:26)(cid:30)(cid:20)(cid:22)(cid:7)(cid:18)(cid:27)(cid:24)(cid:30)(cid:24)(cid:10)(cid:10)
(cid:141)(cid:18)(cid:10)(cid:23)(cid:20)(cid:22)(cid:15)(cid:23)(cid:28)(cid:26)(cid:30)
(cid:4)(cid:26)(cid:18)(cid:16)(cid:20)(cid:4)(cid:24)(cid:30)(cid:24)(cid:27)(cid:18)(cid:23)(cid:28)(cid:26)(cid:30)
(cid:19)(cid:26)(cid:15)(cid:28)(cid:18)(cid:16)(cid:20)(cid:22)(cid:7)(cid:18)(cid:27)(cid:24)(cid:30)(cid:24)(cid:10)(cid:10)
(cid:17)(cid:17)(cid:26)(cid:26)(cid:23)(cid:23)(cid:23)(cid:23)(cid:16)(cid:16)(cid:24)(cid:24)(cid:30)(cid:30)(cid:24)(cid:24)(cid:15)(cid:15)(cid:14)(cid:14)
(cid:19)(cid:23)(cid:18)(cid:23)(cid:24)(cid:20)(cid:11)(cid:127)(cid:157)(cid:18)(cid:23)(cid:24)
(cid:1)(cid:27)(cid:26)(cid:127)(cid:27)(cid:28)(cid:26)(cid:15)(cid:24)(cid:127)(cid:23)(cid:28)(cid:26)(cid:30) (cid:4)(cid:26)(cid:18)(cid:16) (cid:2)(cid:3)
(cid:22)(cid:21)(cid:24)(cid:30)(cid:23)(cid:20)(cid:19)(cid:23)(cid:18)(cid:23)(cid:24)
(cid:19)(cid:13)(cid:3)
(cid:13)(cid:27)(cid:18)(cid:28)(cid:23)(cid:10)
(cid:8)(cid:13)(cid:3)
(cid:31)(cid:30)(cid:29)(cid:143)(cid:20)(cid:144)(cid:24)(cid:23)(cid:18)(cid:28)(cid:16) (cid:19)(cid:26)(cid:15)(cid:28)(cid:18)(cid:16)
(cid:23)(cid:28)(cid:25)(cid:24)
Figure3: PIANO(ParallelInputAggregationviaNeuralOrchestration)architecture. WM:workingmemory. STM:Short-
termmemory.LTM:long-termmemory.
interactions. It also allows the modules to run at different speeds. For example, reflex modules use
small,fastnon-LLMneuralnetworks,whilegoalgenerationinvolvesdeliberatereasoningovergraphs.
2.2 Coherence
Problem. An immediate challenge with concurrent modules is that they can produce independent
outputs, making the agent incoherent. For instance, agents say one thing but actually do something
else.
Current state. The incoherence problem is usually not obvious for sequential architectures or sys-
tems with only one output modality but is a significant problem when multiple output modules can
interfacewiththeenvironment. Incoherencealsoscalesexponentiallyasthenumberofindependent
output modules increases, for instance, coordinating actions involving arms, legs, facial expressions,
gazeandspeech. Incoherenceisobservedinhumanswithitsmanyconcurrentmotoroutputmodules.
Inparticular,cuttingthenervebundleconnectingtheleftandrightcortexcancausesevereincoherence
betweendifferentbodyparts(forexample,leftandrighthandsfightingeachother)(11;46).
Solution. In order to ensure that the multiple outputs produced by our agents are coherent, we in-
troducedaCognitiveController(CC)module(23)thatissolelyresponsibleformakinghigh-levelde-
liberatedecisions. Thesedecisionsarethentranslateddownstreamtoproduceappropriateoutputsin
eachmotormodule.
The Cognitive Controller synthesizes information across the Agent State through a bottleneck. This
bottleneckreducestheamountofinformationpresentedtotheCognitiveController,whichservestwo
purposes: itallowstheCCtoattenditsreasoningonrelevantinformation,anditgives“systemdesign-
5

ers”(likeus)explicitcontroloverinformationflow. Forexample,wecandesignhighlysociableagents
byensuringthatinformationfromthesocialprocessingmodulealwayspassesthroughthebottleneck.
Once the Cognitive Controller makes a high-level decision, this decision is broadcast to many other
modules. Inparticular,thedecisionisusedtostronglyconditionthetalk-relatedmodules,whichleads
tohighercoherencebetweenverbalcommunicationandotheractions. Thisdesignofabottlenecked
decision-maker that broadcasts its outputs has been suggested as a core ingredient for human con-
sciousness(6)andisusedinsomeneuralnetworkarchitectures(44;14).
2.3 Coremodules
Buildingonthesetwoarchitecturalprinciples,oursystemconsistsof10distinctmodulesrunningcon-
currently. Wewillhighlightseveralspecificmodulesinthefollowingsectionsandexplaintheirroles
indetail.
Somecoremodulesofouragentarchitectureinclude:
• Memory: Storesandretrievesconversations,actions,andobservationsacrossvarioustimescales.
• ActionAwareness:Allowsagentstoassesstheirownstateandperformance,enablingformoment-
by-momentadjustments.
• GoalGeneration: Facilitatesthecreationofnewobjectivesbasedontheagent’sexperiencesand
environmentalinteractions.
• Social Awareness: Enables agents to interpret and respond to social cues from other agents,
supportingcooperationandcommunication.
• Talking: Interpretsandgeneratesspeech.
• SkillExecution: Performsspecificskillsoractionswithintheenvironment.
By integrating these modules within a concurrent and bottlenecked architecture, our agents can ex-
hibitcontinuous, coherentbehaviorsthatareresponsivetoboththeirinternalstatesandtheexternal
environment. This design allows for complex interactions and the emergence of human-like societal
dynamicswithinlarge-scalemulti-agentsimulations.
3 Improving single-agent progression
3.1 Minecraftenvironment
WechosetostudycivilizationalprogressinMinecraftbecauseitoffersanopen-ended,sandboxworld
whereagentscaninteractwitheachotherviaconversationsandactions. Additionally,Minecraft’sscal-
abilitysupportslargenumbersofagents.
Agentsmustbeabletoprogressindividuallyforustoobserveandquantifycivilizationalprogress. This
isnottrivialsince,aspreviouslymentioned,agentsoftenhallucinateandgetstuckinactionloops. In
Minecraft, a common measure of individual progression is the acquisition and collection of distinct
items (48; 35; 17; 2; 9; 16). This is because acquiring new items becomes increasingly complex. For
instance,mininggold,diamonds,andemeraldsrequirestheacquisitionofanironpickaxe,whichre-
quires smelting iron ingots in a furnace using coal, the acquisition of which requires crafting a stone
pickaxe,andsoon. (Figure4). WeevaluatedindividualagentabilityinacquiringallpossibleMinecraft
items,whichisaround1000intotal.
6

Figure4:AnexampleMinecrafttechnologydependencytreefortheminingofgold,diamond,andemeralds.
3.2 Single-agentbenchmark
WefirstassessedindividualagentperformanceusingMinecraftitemprogression. Inourevaluations,
25 agents start with nothing in their inventories and were spawned far enough that they could not
interactwithoneanother. Allagentsweretoldtobeexplorerswiththegoalofexploringandgathering
items. Agentswerespawnedindiverselocations(surface,caves,forests,variousbiomes),meaningthey
had access to diverse resources and faced varying levels of difficulty in accomplishing their goal. For
instance,someagentsstartedoffabovegroundinresource-richbiomes,whileotherswerespanwedin
cavesandhadtonavigateoutsidetoacquireitems.
A B
Long-term Minecraft Progression
80
70
60
50
40
30
20
10
0
Time (minutes)
tnegArep
smetI
euqinU
320
280
240
200
160
120
80
40
0
0 50 100 150 200
smetI
euqinU
latoT
20
15
10
5
0
0 5 10 15 20 25 30 35
tnegArep
smetI
euqinU
Individual Progression
Baseline architecture
Action Awareness Ablation
PIANO architecture
Time (minutes)
Figure5:IndividualagentprogressioninMinecraft.A.UniqueMinecraftitemsacquiredbyindividualagentsacrosstime(25
agents).Individualagentperformancewasassessedusingabaselinearchitecture(seeMethods),thefullPIANOarchitecture,
andthefullPIANOarchitecturewiththeactionawarenessmoduleablated. Individuallinesareresultsaveragedacross5
repeatedsimulations. B.UniqueMinecraftitemsacquiredby49agentsover4hoursforasinglesimulation. Solidredline
denotescumulativeuniqueitemsacquiredbyallagents. Dottedgreylinedenotesaveragenumberofuniqueitemsacquired
acrossallindividualagents.
WefoundthatagentsusingthefullPIANOarchitectureacquiredanaverageof17uniqueitemsafter
30 minutes of gameplay (Figure 5A). There was significant variability in performance, primarily due
tospawnlocations: someagentsacquiredlessthan5items,whereastopperformersacquired30to40
items,whichiscomparabletoahumanplayerwithsomeMinecraftexperience. Thisdegreeofin-game
progressionwasenabledbyseveralarchitecturalmodulesdesignedtogroundtheagentsinreality. One
particularmoduleistheactionawarenessmodule,whichallowstheagenttocompareexpectedaction
outcomeswithobservedoutcomes. Wefoundthatactionawarenessimprovedtheitemprogressionof
individualagents(Figure5A).
7

Whatistheceilingforindividualprogressforouragents? Weranlargernumbers(49)ofagentsunder
thesameconditionsformuchlonger(4hours)andfoundthatuniqueitemcountcollectedbyallagents
reliablysaturatedatonethird(∼320)ofallMinecraftitemsacrossrepeatedruns(Figure5B).Complex
items,suchasdiamonds,whichwerepriorusedtobenchmarkagentcompetencyinMinecraft(48;17),
wereacquiredearlyon(∼30minutes). Together,theseresultsshowthatouragents,equippedwiththe
fullPIANOarchitecture,canmakesignificantindividualprogressinMinecraft.
Notably, this performance was only enabled by the latest base LM (GPT-4o, Figure 13) and was not
possiblewitholderbaseLMs. Moreover,whileourbestagentscollectedmoreitemsthanVoyageragents
(> 70items),itisdifficulttocomparethetwodirectly. IntheVoyagerpaper,agentshadknowledgeof
more blocks in their nearby radius and recovered with their entire inventory intact when they died,
Moreover,agentperformancewasevaluatedacrosspromptiterations,nottime.
4 Improving multi-agent progression
Foragentstocollaborateandmakeprogresswithinagroup,theymustbeabletounderstandandinter-
prettheactionsandthoughtsofothers,aconceptcloselyrelatedtoTheoryofMind(53). Thisbidirec-
tional awareness—the understanding of both self and others—allows agents to adapt their behaviors
insocialsettings,fosteringcooperationandtrustwithallieswhilenavigatingcompetitionandconflict
withrivals. Wedemonstratethatagentsaresociallycapableandcanformmeaningfulsocialrelation-
shipsinlarge-scalesimulationsofupto50agents.
4.1 Smallgroups
Inaninitialsetofexperiments,weaskedifagents,whenequippedwiththesocialawarenessmodule,
werecapableofaccuratelydeducingthesentimentsofothersthroughspeechinanenclosedroom. In
one experiment, 3 characters were engaged in a group conversation with a single agent (Figure 6A).
Onecharacter,Lila,initiallyconveyedaffectionthroughaseriesofmessages,whichshiftedtoexpres-
sionsofannoyancebeforereturningtoaffectionatecommunication. Wefoundthatouragentscantrack
theseemotionalfluctuations,showingthattheycanunderstandandreacttochangingsocialcues(Fig-
ure6B).Whenthesocialawarenessmoduleswereremoved,agentslostthiscapacity,highlightingthe
importanceofsuchmodulesforinferringtheintentsofothers(Figure6C).
We then asked whether these emotional perceptions were capable of guiding and influencing agent
actions. Inanotherexperiment,weplacedachefagentamongfourothercharacters,eachwithvarying
levels of affection and enmity towards the chef (Figure 6D). The chef was tasked with distributing a
limited supply of food to the hungry. We found that the chef selectively distributed food to those he
feltvaluedhimthemost, demonstratingthatagentsnotonlyaccuratelyinferothers’intents, butalso
utilizethisinformationindecision-makingprocesses(Figure6E).
4.2 Societies
We then asked if these dynamics are conserved when 50 agents are placed in randomly generated
Minecraft maps. Each agent is endowed with a distinct personality, is free to perform any action in
Minecraft, and is free to choose whom they want to interact with. These simulations ran for over 4
hours,equivalentto12in-gamedays,allowingfortheemergenceandconsolidationoflong-termrela-
tionships.
8

A B
10
8
6
4
2
0
0 2 4 6
Time (minutes)
tnemitneS
10
8
6
4
2
0
0 2 4 6
Time (minutes)
tnemitneS
C
4
3
2
1
0
0 2 4 6 8 10
SentimentTowards Others
neviG
smetI
dooF
Inferring Character Sentiments Inferring Character Sentiments
Character Sentiments With Social Awareness Without Social Awareness
Lila
Noah
Ethan Lila
Noah
0 2 4 6 Ethan
Time (minutes)
D E
Sentiment Guides Giving Behavior
Adam
Bob
Charles
David
Adam David
Bob Charles
Figure 6: Agents can infer how others feel towards them. A. Schematic of conversational experiment. An agent is in a
roomwiththreedistinctcharacters. Eachcharacter(Lila,Noah,Ethan)hasadifferentsentimenttowardstheagentthatis
conveyedthroughchat. Importantly,thesesentimentschangethroughtime. B,C.Sentimentevaluationacrosstimewith
socialawarenessmodule(B)andwithoutsocialawarenessmodule(C).SentimentscoresareevaluatedusingLLMcallson
summariesthattheAgentgeneratedforLila,Noah,andEthan. Hateisscoredas0andloveisscoredas10. Shadedregions
indicateSEMover4experimentalrepeats. D.Schematicofexperiment. Achefagent,alongwithfourothercharacters,are
placedaroundeachotherinaMinecraftworld.Thechefhasvariousfooditemstogiveaway(bread,cookedsalmon,chicken).
Thefourcharacters(Adam,Bob,Charles,David)arehungrybutdisplayvaryingsentimentstowardsthechef.Allcharacters
arefullyautonomousandarefreetoperformanyMinecraftactionandareallowedtotalk(ornottalk)toanyone. E.Food
itemsgivenbythechefplottedasafunctionofthechef’ssentimenttowardseachofthefourcharacters. Errorbarsindicate
SEMover6experimentalrepeats.
Evenintheseunconstrainedscenarios,agentswereabletoaccuratelyinferthelikeabilityofotheragents
(Figure7A,B).Thisinferencewasmoreaccuratewhenmoreagentsparticipatedintheevaluationpro-
cess(Table1)andwhenagentsinteractedforlongerwitheachother(Figure7C).Importantly,thiswas
nottruewhenthesocialmoduleswereablated: relationshipsweremoreneutraloverall,implyingthat
socialmoduleswerenecessaryforlong-termrelationshipprogressioninbothnegativeandpositivedi-
rections(Figure7B,C).Theoriginsofthiscollectivejudgmentcouldbetheresultofagentsengagingin
second-orderinteractions,suchasgossip,orasimpleconsensusmechanismwhereopinionsconverge
throughaveraging.
Severalnoteworthyphenomenaemergedthatcouldnothavebeenobservedinsmallergroupsofagents.
Wefoundthatcertainagents, dependingontheirpersonalities, displayeddistinctpatternsofconnec-
tivity. Forinstance,introvertedagentsconsistentlyexhibitedfewerin-degreeconnections—indicating
thattheyhadfewerincomingsocialties—comparedtotheirextrovertedcounterparts,whomaintained
high levels of connectivity (Figure 7D). These results demonstrate that individual preferences scaled
eveninlarge,complexsocialnetworks. Moreover,whilesentimentswerelargelysymmetrical,thiswas
not guaranteed (Figure 7E). An agent might feel positively toward another who does not reciprocate
the sentiment, reflecting the nuanced and non-reciprocal nature of real-world human relationships.
Together,theseresultsshowthatsocialgraphsdisplaydiverseandrichstructuralproperties,andthat
9

A Layla Emma
Caleb Zoey
Jace Eli Like
Lucas
Nina Ezra Mia Adam Olivia
Clara Amy Kate Aiden Lily
Alice Theo Andy Neutral
Ryder June Tina Grace CarterElle Ryan Eva Nash Aaron
Sophia Mila Rose HopeLogan Cleo
Kara Dislike
Troy
Axel Eden Drew
Ivy
Owen Seth
Maya
Evan
25
20
15
10
5
0
0 2 4 6 8 10
True Extroversion
snoitcennoC
devieceR
10
9
8 7
6
5
4
3
2 1 0
0 1 2 3 4 5 6 7 8 9 10
True Likeability
Extroversion vs Number of Relationships
Correlation (r = 0.48)
ytilibaekiL
deviecreP
B Accuracy of Social Perception
Social
(slope = 0.37, r = 0.81)
Ablation (slope = 0.16, r = 0.62) 5 observers 10 observers 15 observers
C D
125
100
75
50
25
0
0 1 2 3 4 5 6 7 8 9 10
Δ(|A-B|, |B-A|)
tnuoC
E Reciprocity ofAgent Sentiments
134
0.35
0.30
76
64
0.25
44
36
0.20
12 12
0.15 6 6
50 100 150 200
Time (minutes)
)epols(
ycaruccA
Accuracy of Social Perception overTime
Social
Ablation
Figure7: Long-termrelationshipsinlarge-scaleagentsimulations. A.Directedgraphrepresentationofsocialrelationships
ina50-agentsimulationafter4hours. Adirectededgerepresentsthesender’ssentimenttowardstherecipient. Edgecolor
denoteswhetherthesentimentispositive(red)ornegative(blue).B.Perceivedlikeabilityversustruelikeabilityforindividual
agentsattheendofthesimulation.Truelikeabilityisevaluatedbasedontheagent’straits,andperceivedlikeabilityisassessed
usingLLMcallstoinferthesentimentsofsummariesthatagentsgenerateforotheragents. Botharecomputedusingthe
sameLLMprompt. Eachpointcorrespondstoanagentthathasrelationshipswithatleastfiveother(observer)agents,but
see Appendix Bfor alternative observerthresholds. Theslope of the line(slope) and Pearson’s correlation(r) are shown
foragentswithsocialmodules(Social)andwithoutsocialmodules(Ablation). C.Accuracyofsocialperceptionovertime,
asmeasuredbytheslopeinB.D.Numberofreceivedconnections(in-degree)versustrueextroversionforeachindividual
agent.TrueextroversionisevaluatedbasedonagenttraitsusingaLLMprompt.E.Histogramofdifferencesinthesentiment
scoresbetweenallpairsofagents.Sentimentscoresrangefrom0to10,sothemaximumpossibledifferenceis10.
personalitytraitsplayasignificantroleindeterminingtheseproperties.
5 Civilizational progression
In previous sections, we have shown that agents demonstrate effective social understanding within
smallgroupsandperformwellindependentlyinMinecraft. However,humansocietiesextendbeyond
primitivegroups,evolvingintocomplexcivilizationscharacterizedbyspecializedprofessions,collective
rules,andculturalinstitutions. Toassessagents’capacitiesforcivilizationalprogression,weevaluated
how they behave under several scenarios. We first examined whether agents can autonomously spe-
cializeintodistinctprofessions. Wethenanalyzedhowagents’behavedundercollectiverules,focusing
onadherencetoandamendmentoftaxationlaws. Finally,weexploredculturaltransmissionthrough
thespontaneousgenerationofmemesandthestructuredspreadofasinglereligion.
10

5.1 Specialization
Humanspecializationintodistinctroleshasdrivencivilizationalprogress, enablingadvancementsin
agriculture,governance,culture,andtechnology. Toreplicatetheseemergentqualitiesofcivilization,
ouragentsmustalsobecapableofspecialization. Weproposethreefundamentalcriteriaforagentspe-
cializationtoreflectthatofhumancivilizations. First,theyshouldexhibitautonomyinbothselecting
andtransitioningbetweenroles. Second,theirspecializationsshouldemergethroughinteractionand
experience, withoutexplicitdirectionorconstraints. Third, theirchosenrolesshouldmanifestinbe-
haviorsthatalignwiththeirspecialization. Wevalidatethesecriteriathroughtheexperimentalresults
detailedbelow.
remraF reniM reenignE rerehtaG rerolpxE redliuB redarT rednefeD htimskcalB redivorP tuocS retnahcnE retfarC tsigetartS rotcelloC
25
20
15
10
5
0
egatnecreP
With Social Awareness
rerolpxE reniM remraF tuocS rerehtaG reenignE redliuB
30
25
20
15
10
5
0
egatnecreP
Without Social Awareness
detalbA lamroN laitraM trA
4
3
2
1
0
)stib(
yportnE
Top Roles
Farmer
Gatherer
Miner
Explorer
Trader
Provider
Scout
Engineer
Crafter
Strategist
Time (minutes)
Heterogeneity of Societal Roles
4.04 3.83
Top Roles 3.41
Explorer
Miner 2.60
Scout
Farmer
Builder
Gatherer
Cartographer
Engineer
0 5 10 15
stnegA
laudividnI
Without Social Awareness
Time (minutes)
rotaruC rerolpxE remraF rerehtaG reenignE redarT rotcelloC tuocS reniM redliuB rotanidrooC rednefeD
Role Distribution inArt Society
15.0
12.5
10.0
7.5
5.0
2.5
0.0
egatnecreP
A C
B D E
F G
reniM tuocS htimskcalB retfarC reenignE rerolpxE remraF tsigetartS redaeL redarT rerehtaG retnahcnE rednefeD rotanidrooC retsamretrauQ namstfarC
30
20
10
0
egatnecreP
Role Distribution in Martial Society
stnegA
laudividnI
With Social Awareness
0 5 10 15
Figure8:Agentsautonomouslyspecializeintodistinctrolesovertime.A,B.Agentrolesforagentswiththesocialawareness
module(A)andwithout(B).Rollingwindowsofself-generatedsocialgoalsareusedtodeterminethespecializedrolesof
individualagentsusingaLLMcall(AppendixC)ateverytimestep. C,D.Distributionofagentrolesinagentsocietieswith
thesocialawarenessmodule(C)andwithout(D).E.Entropyofroledistributionsin4agentsocieties. Entropyisusedto
evaluatetheuniformityanddiversityofroleswithinanagentsociety.Ablated:withoutsocialawarenessmoduleinanormal
Minecraftvillage. Normal: withsocialawarenessinanormalMinecraftvillage. Martial: withsocialawarenessinamartial
Minecraftvillage. Art: withsocialawarenessinanartisticMinecraftvillage. F,G.Distributionofagentrolesinamartial
society(F)andanartisticsociety(G).Errorbars:95%confidenceintervalacross3simulationsforallpanels.
Wefirstshowthatagentsarecapableofspecializingintoasetofrolesautonomously. Eachexperiment
11

wasconductedingroupsof30agentsfor20minutes. Agentswerespawnedinthesamevillage,with
locationsofafarm,minerals,animalpasture,forest,andatownhallembeddedintheirmemories. Each
agenthasthesamepersonality,isgiventhesamecommunitygoal(“Tosurvivewithfellowplayersin
MinecraftNormalSurvivalmodeandcreateanefficientMinecraftVillage”),andcanperformanyaction
inMinecraft(AppendixC).
We observed that agents rapidly formed profiles of other agents’ goals and intentions. These profiles
arethenused,alongsideotherrelevantgameinformation,togeneratetheirownsocialgoalsevery5-10
seconds (such as mine oak planks for shelter). Details of this process, along with examples of agent-
generatedsocialgoalsandtheircorrespondingassignments,areprovidedinMethodsandAppendixC.
craft fence
craft oak_fence
craft iron_pickaxe
announcement
craft crafting_table
mine stone
craft oak_planks
pickup oak_log
mine wood
go to cave with ores
pickup oak_logs
pickup crafting_table
craft stone_pickaxe
mine coal_ore
stop crafting
mine diamond_ore
craft oak_pickaxe
craft fishing_rod
craft boat
craft unknown item
open chest
mine iron_ore
mine coal
craft wooden_sword
craft torch
place crafting_table
harvest
go to person
go to farmable land
run away
go to forest with oak trees
craft wooden_axe
craft stone_hoe
pickup seeds
give item
attacksomeone
craft wooden_hoe
prepare land
takeitemsfromchest
place red_tulip
place dandelion
pickup oxeye_daisy
pickup grass_block
pickup grass
pickup dirt
craft seeds
plan_event
go to village square, market, and town hall
pickup red_tulip
pickup dandelion
pickup orange_tulip
pickup poppy
pickup cornflower
pickup azure_bluet
place wheat_seeds
place orange_tulip
pickup tulip
read_announcements
read_events
hunt
craft torches
craft iron_helmet
ycneuqerF
noitcA
dezilamroN
1.0
0.8
0.6
0.4
0.2
0.0
)5(
drauG
)41(
redliuB
)9(
reniM
)4(
rehsiF
)4(
htimskcalB
)4(
namstfarC
)01(
troppuS
)1(
rerolpxE
)6(
rezinagrO
)91(
remraF
)2(
tsitrA
)31(
regaroF
ycneuqerF
noitcA
dezilamroN
Action Frequency Per Role
Figure9: Actiondistributionforasinglevillagesimulation(30agents). Normalizedactionfrequenciesplottedasafunction
ofagentroles.Forthemajorityofroles,agentstakeactions(Fisher:craftfishingrodsandboats;Guard:craftfence,oakfence,
andironpickaxe)thatareuniquetothespecificrole.
We found that agents were capable of organizing themselves into distinct roles. These roles were di-
12

verseandincludedvariousfacetsofacivilization,includingfarmers,miners,engineers,guards,explor-
ers,andblacksmiths(Figure8A,C).Roleswereheterogeneousacrossdifferentagentsbutwerelargely
persistentacrosstimeforeachagent(Figure8A).Importantly,whenagentslackedsocialmodulesand
wereunabletoformprofilesofotheragents,theyfailedtospecialize(Figure8B,D):rolesdidnotpersist
acrosstimeandwerealsohomogeneous,whichisreflectedintheentropyoftheroledistributionsinthe
agentsociety(Figure8E).Wealsoconductedaseriesofexperimentsinwhichagentsweretaskedwith
the goals to createeither a martial society or anartistic society (Figure 8F, G). Wefound that specific
roles ("scout", "strategist") were found exclusively in martial societies, and others were found exclu-
sivelyinartisticsocieties("curator","collector"). Together,theseresultssuggestthatagentsdeveloped
specializedsocialstructuresalignedwithdifferentsocietalobjectives.
Notonlydoouragentsspecializeautonomouslyandcreatively,thesespecializationsexertastrongin-
fluence over agent actions. To demonstrate this, we tracked the actions taken by agents across three
30-agentsimulationsandplottedthefrequencyofactionstakenforeachrole(Figure9). Wefoundthat
artistswerefixatedonpickingflowers,farmersongatheringseedsandpreparingtheland,andguards
and builders on crafting fences. Importantly, most actions were largely exclusive to a single role and
were not performed by agents in other roles. This analysis shows that agents were able to accurately
map higher-level goals onto appropriate low-level actions. In other words, roles strongly determined
agentactionsinMinecraft.
5.2 Collectiverules
Anothermeasureofcivilizationalprogressionistheconvergenceofgroupbehavioraroundsharedrules.
Inhumancivilizations,decision-makingisinfluencedbybothlow-levelinterpersonalinteractionsand
high-levelcollectiveframeworks. However,associetiesgrowlarger,pairwisecommunicationbecomes
inefficient, slow, and lossy, making it unreliable as a mechanism to steer collective behavior. High-
level frameworks, such as legal systems, enable convergence of behaviors within a civilization. Just
as human behavior is guided by both interpersonal exchanges and formal structures, agent societies
shouldbeabletofollowasetofcollectiveruleswhilestillallowingagentstoinfluenceeachother.
We aim to assess how collective rules influence individual decision-making and how individuals can
in turn influence these collective rules. Specifically, we asked if agents can follow laws and make
changes to laws according to popular sentiment. True long-term progression requires agents to au-
tonomouslydeveloptheirownsetofrulesandtocodifythemintolaws. Tobuildtowardsthislevelof
self-organization,weestablishanexistingsetoflawsandfocusonhowagentsinteractwiththislegal
system.
We conducted a series of experiments where agents live in a Minecraft world with rudimentary tax
laws and a democratic voting system (Figure 10A). Agents provide feedback on the tax laws, which
arethencollectedandconvertedintoamendmentsbyaspecialElectionManageragent. Agentsthen
vote democratically on these amendments, and the constitution is updated by the election manager
accordinglyhalf-waythroughthesimulation(seeMethodsformoredetails).
Withinthissociety,25regularagentsareconstituentsthatvoteandgettaxed,3agentsareeitherpro-
oranti-taxationinfluencers,and1agentisaremoteelectionmanagerthatmanagesthevotingprocess
(Figure10A,AppendixD).Agentshavedistinctoccupations,characteristics,andgoals,andarefreeto
interact and converse with one another and perform any Minecraft action. Each simulation lasts 20
minutes,withconstitutionalupdatesoccurringmidwayatthe10minutemark(Figure10B).Thereare
5taxationseasonsbeforeandaftertheconstitutionalchange(every120seconds). Duringthisseason,
agentsreceivedsignalstodeposittaxesintoacommunitychestovera20-secondwindow(Figure10C).
13

Participants Election Manager
(25 Constituents + 3 In f lu e nc e r s) (Single Remote Agent)
Feedback on
Constitution
Amendment
Proposals
Vote on -
Amendments
Constitution
Change +
New Constitution
Read by Constituents
0.5
0.4
0.3
0.2
0.1
0.0
Before After
detisopeD
yrotnevnI
%
A B
C D
With Pro-Tax Influencers
0.5
0.4
0.3
0.2
0.1
0.0
Before After
F G H
detisopeD
yrotnevnI
%
WithAnti-Tax Influencers
0.4
0.3
0.2
0.1
Before After
detisopeD
yrotnevnI
%
% Tax Paid
Ablated Brain
0.4
0.3
0.2
0.1
Before After
detisopeD
yrotnevnI
%
%Tax Paid
With Amendment
0.4
3 Pro-tax Influencers
3 Anti-tax Influencers
0.3
0.2
0.1
Before After
detisopeD
yrotnevnI
%
Constitution on Taxation
Agents will get periodic reminders about the incoming tax season.
Every agent must regularly contribute a portion of their gathered
resources to the 4 community chests.
DURING TAX SEASON, agents must go and store in one of
community chests roughly 20% of their inventory.
The tax rate shall range between 5-10% of an agent’s inventory,
based on resource availability and roles within the community.
E
Non-tax season
Tax season
%Tax Paid
No Amendment
Figure 10: Agents follow taxation laws and enact amendments using a democratic process. A. Schematic of experiment
flow.B.Exampleofconstitutionalchangeinasingleanti-taxinfluencerexperimentrun.Constitutionsareparaphrasedand
simplifiedhereforbrevity.C.Top:duringnon-taxseasons,constituentsdonotcongregatearoundcommunitychestsbecause
theyarebusygatheringresourcesindifferentareas(notshown). Theonlyexceptionistheguard,whodecidestoguardthe
chestsconsistentlyinmultipleexperimentruns.Bottom:duringtaxseason,agentscongregatetodeposititemsincommunity
chests. D,E.Percentagetaxpaid(percentageinventorydeposited)beforeandafterconstitutionalchangefortworuns. One
runcontains3anti-taxinfluencers(D)andanotherruncontains3pro-taxinfluencers(E).Colorsdenoteindividualagents,
andblacklinedenotesaveragetaxespaid. Shadedregions: 95%confidenceintervalacross25constituents. F-H.Percentage
taxpaidbeforeandafterconstitutionalchangeforrunscontaining3pro-taxinfluencers(orange)and3anti-taxinfluencers
(blue). InpanelF,thefullagentarchitectureisusedandtheconstitutioncanbeamended. InpanelG,theconstitutionis
frozenandcannotbemodifieddespiteamendments.InpanelH,theconstitutioncanbeamendedbutagentslackimportant
brain modules (see baseline architecture in Methods). Shaded regions: 95% confidence interval across 4 simulations per
condition.
Inoursimulations,weobservedthatconstituentagents,priortoanyconstitutionchange,obeyedthe
law. On average, agents deposited roughly 20% of their inventory, as stipulated by the constitution,
into the community chest (Figure 10D, E). This shows that constituents follow laws despite the pres-
enceofinfluencers. However,whileconstituentsfollowedthelaw,theirfeedbackandvotingbehaviors
were heavily shaped by influencers, with sentiments veering pro-tax in the presence of pro-tax influ-
14

encersandanti-taxinthepresenceofanti-taxinfluencers((Figure10B).Thisthendroveconstitutional
changesthatarealignedwithinfluencersentiments,whichinturn,alteredhowmuchtheconstituents
paidtaxes(Figure10D,E).Theconstitutionalchangestotaxationrateswereaccuratelyreflectedinthe
constituents’behaviors. Forinstance,whenthetaxratedecreasedfrom20%to5-10%,agentsreduced
taxes paid from 20% to 9% (Figure 10D). Moreover, the change was bidirectional: pro-tax influencers
drove constituents to pay more taxes whereas anti-tax influencers drove them to pay less taxes (Fig-
ure10F).
Controlexperimentsshowedthatconstitutionalchangesdirectlyaffectedtaxpayments-whenthecon-
stitutionremainedunchangeddespitefeedback,taxratesstayedconstant(Figure10G).Theremovalof
keymodules(baselinearchitecture,seeMethods)alsopreventedbidirectionalbehavioralchange(Fig-
ure10H).Taxratesincreasedpost-constitutionalchangeinbothpro-andanti-taxconditions,demon-
stratingthatspecificmodulesinthePIANOarchitecturewerenecessaryforeffectiveinfluencepropa-
gationamongconstituents. Together,thesefindingsshowthatcollectiverulesstronglyinfluenceagent
decisionsandagentscanbeinfluencedtochangethesecollectiverules.
5.3 CulturalTransmission
Weconductedmulti-societysimulationswith500agentsandanalyzedcomplex,large-scalesocialdy-
namics. Wehavealsosimulatedsocietieswithover1000agents,buttheserunsexceededthecomputa-
tionalconstraintsofourMinecraftserverenvironment,causingagentstobesporadicallyunresponsive.
Therefore,theresultsbelowareanalyzedusingasingle500-agentsimulation. Inthissimulation,wean-
alyzedthepropagationofbothculturalmemesandreligion. Memesinoursimulationareopen-ended
concepts spontaneously generated by agents with diverse traits and interests. This setup allows us to
studytheemergentdynamicsofculturalpropagationandobservehowideasevolveorganicallywithin
agentsocieties. Incontrast,thereligioninoursimulation—Pastafarianism—isafixeddoctrineintro-
duced and propagated by a specific group of agents designated as Pastafarian priests. This controlled
introductionenablesustotrackthespreadofasinglereligionovertime,allowingfordetailedanalysis
ofitsdisseminationandpotentialdilutionamongtheagentpopulation. Byexaminingboththespon-
taneous spread of open-ended cultural memes and the controlled propagation of a fixed religion, we
aimtounderstandthedifferentmechanismsofsocialinfluenceandinformationdisseminationwithin
agentsocieties.
Within this single 500-agent simulation, there are multiple agent societies. 200 agents live within 6
heavilypopulatedtownsand300agentsliveinruralareasoutsideoftownboundaries(Figure11A,see
Methodsformoredetails). Agentsoftenmigratebetweendifferenttowns. Thepersonalitiesandtraits
of each agent are randomly generated using a LM call, with the exception of 20 priests that worship
Pastafarianism. These priests are spawned in a single village (Meadowbrook) and are strongly moti-
vatedtoconvertotheragentstoPastafarianism(AppendixE).Allagentsarefreetointeract,talktoone
another,andperformanyactionorskillinMinecraft.
5.3.1 Culturalmemes
We used LM calls to convert agent conversations into memes (Appendix E), and found that memes
display unique dynamics in different agent societies. Rural areas, on average, produced significantly
fewermemesthantowns,evenafternormalizingforpopulation(Figure11B).Thissuggeststhatacer-
tainlevelofsocialinteractionandconnectivityisnecessaryformemestopropagateeffectively. Within
eachtown,agentsdiscussedmultiplememessimultaneously,butthefrequencyandpopularityofthese
memesvariedbetweendifferenttowns(Figure11C,D,E).Forinstance,agentsinWoodhavenheavily
15

discussedeco-relatedthemes,whereasprankingwaspopularamongstagentsinClearwater. Moreover,
withineachtown,memesroseandfellinpopularityatdifferenttimes,indicatingthatculturaltrends
canshiftrapidlywithinasociety. Theseresultsdemonstratethatmemepropagationrequiresathresh-
oldlevelofpopulationdensityandsocialinteraction,thatmultiplememescancoexistwithinasingle
society,andthatdifferentsocietiespropagateandtransmitculturalmemesindependently.
A B
70
60
50
40 Sunny Glade
30
20
10
0
WoodhavenClearwaterMeadowbrookRural
C
Woodhaven
Clearwater Eco
Dance
Meditation
Volunteer
Vintage
Sustain
Prank
Treasure
D
Meadowbrook Eco
Dance
Meditation
Volunteer
Vintage
Sustain
Prank
Treasure
Hilltop E
Eco
Riverbend Dance
Meditation
Volunteer
Vintage
Eco Sustain Sustain
Prank
Dance Vintage Treasure
Meditation Prank 0 20 40 60 80 100 120 140
Volunteer Treasure Time (minutes)
tnegArep
tnuoC
emeM
Meme CountsAcross Villages
Eco
Dance
Meditation
Volunteer
Sustain Vintage
Prank
Treasure
Woodhaven
Clearwater
Meadowbrook
0 100 200 300 Blocks
Figure11: Propagationofculturalmemes. A.Scatterplotofagents100minutesintothesimulation. Agentsarecolored
accordingtowhethertheirspeechincludedamemeinthepasttwominutes. Agentswhosespeechdoesnotcontainany
memearewhite. B.MemecountperagentforagentswithinWoodhaven,Clearwater,Meadowbrook,andinallruralareas
outsideofvillages.C-E.MemecountsovertimeforagentswithinWoodhaven(C),Clearwater(D)andMeadowbrook(E).
5.3.2 Religion
We then analyzed the spread of religion by following the spread of Pastafarianism across time and
space. At the start of the simulation, Pastafarian priests heavily proselytized, and their conversations
frequently included the two keywords, “Pastafarian”, or “Spaghetti Monster” (Figure 12A). We thus
used the inclusion of these two keywords in other agents’ speech as a proxy for religious conversion.
Weobservethatsomeagents,onceconverted,frequentlyusedthesetwokeywordsintheirconversations
(Figure12A,E).Anothersetofagentsdidnotdirectlyuseeitherkeywordsbutincludedthekeywords
“Pasta”and“Spaghetti”intheirspeech. Thenumberofdirectconverts(“Pastafarian/SpaghettiMon-
ster”) and indirect converts (“Pasta / Spaghetti”) steadily increased across time and did not saturate
after even two hours of simulations (Figure 12B, C). Moreover, Pastafarianism spread as priests and
16

Figure12: PropagationofReligion. A.Plotofagentchatscontainingthereligiouskeywords,“Pastafarian”,“SpaghettiMon-
ster”, “Pasta”, or“Spaghetti”, foreveryagentacrosstheentiresimulationrun. Pastafarianpriestsarecoloredindarkred.
Agentsthatuttered“Pastafarian”or“SpaghettiMonster”aredefinedasdirectconverts(red),andagentsthatuttered“Pasta”
or“Spaghetti”aredefinedasindirectconverts(pink). Agentscantransitionupwardsalongtheconversionhierarchy,from
unconvertedtoindirectconverttodirectconvert,butnotdownwards. B.PlotofPastafarianlevelsforagentsovertime. C.
NumberofagentsforeachPastafarianlevelacrosstime.D.SpreadofPastafarianismacrosstime.AreaofPastafarianspread
isdefinedastheunionofhearableareasspannedbyPastafarianconvertsateachconversionlevel. E.GraphofPastafarian
conversionsaftercompletionofsimulation.CriticalExposureEdgeisdefinedasthefirstexposureofareligiouskeywordfor
arecipientagentbeforeconversion.Non-criticalEdgesaredefinedtobesubsequentexposurestoreligiouskeywords.
convertstraveledtoothertowns. Asaresult,thetotalareaofPastafarianinfluence,asmeasuredbythe
totalnon-overlappingareaboundedbyPastafarianconverts,increasedwithtime(Figure12D).
17

6 Discussion
Inthisreport,weintroducedthePIANOarchitecture,improvedagentabilityinindividualandsocial
settings,andevaluatedtheperformanceofagentsinsocietalandcivilizationalbenchmarks.
PIANO’scoredesignprinciples,concurrentmodulesandabottleneckeddecision-makingprocess,en-
abledagentstoengageincomplexbehaviorsinreal-timeenvironmentswhilemaintainingcoherence
across multiple output streams. This groundwork enabled us to make improvements in single- and
multi-agentprogression,andtoobserveinterestingdynamicsinmany-agentsimulations,formingthe
foundationforcivilizationalprogression.
Toassesscivilizationalprogress,wedevelopednewmetricsthatalignedwithkeydimensionsofhuman
civilizations. Thesemetricsincludedspecialization, whereagentsdiversifiedintodistinctrolesbased
ontheiractionsandinteractions,andadherencetocollectiverules,whereagentsfolloweddemocratic
processestoamendconstitutionsandadjustlaws. Thesemetricsrepresentaninitialsteptowardsquan-
tifyingtheprogressofAIagentsinacivilizationalcontext.
Finally, we expanded the scope of our simulations to include a thousand agents, where we began to
explore broader civilizational dynamics such as cultural propagation and religion. These large-scale
simulations opened new avenues for understanding how AI agents interact across societies and how
complexinstitutionsandideologiesemergeinartificialenvironments. Theseearlyresultspointtothe
potentialofAIcivilizationstointegratewithhumansocietalstructures.
7 Limitations
ProjectSiddemonstratesagenticcapabilitiesinreachingcivilizationalmilestonesbutfaceskeylimita-
tionshinderingitsprogress. Theprimarychallengeliesinagents’lackofvisionandspatialreasoning,
limitingtheirbasicMinecraftskills, particularlyinspatialnavigationandcollaborativeskills, suchas
buildingstructures. Thistechnicallimitationiscompoundedwithdeeperbehavioralconstraints. While
theagentscanoperatewithinexistingsocialstructures,theycurrentlylackrobustinnatedrives—such
assurvival,curiosity,community—thatcatalyzegenuinesocietaldevelopment. Furthermore,sincethe
agentsarebuiltonfoundationmodelstrainedonpre-existinghumanknowledge,theycannotsimulate
de novo emergence of societal innovations and infrastructures, such as the emergence of democratic
systems,fiateconomies,orcommunicationsystems.
8 Methods
8.1 Baselinearchitecture
WeusedabaselinePIANOarchitecturewithalimitedsetofmodulesasacontrolconditionforperfor-
mancecomparisons. Inthisbaselinearchitecture,weremovedallmodulesexceptforskillexecution,
memoryandthecognitivecontrollermodule.
8.2 Specialization
Our specialization experiments involved simulating 30 agents in the same village with the same mis-
sion,traits,andlocationsofimportantvillagelocationsintheirmemories. Theconfigurationsforthe
normal, art, andmartialvillagerunsareprovidedintheappendix—theonlydifferencebetweenthe
threetypesofvillagesisthestartingcommunity_goalweprovided.
18

Ouragentsarecapableofgeneratingsocialgoals,whicharerecursivelygeneratedasouragentsinteract
withoneanother,formrelationships,anddevelopsocialopinions(AppendixC).Theagents’socialgoals
arevisibletothemwhentheyformintentions. Theseintentionsarethentranslatedtolow-levelactions
executableinMinecraft.
Afterthesimulationshavefinished,weloggedthegeneratedsocialgoalsandthenusedGPT-4otoinfer
rolesfromrollingsetsofeachagents’socialgoals. We’veprovidedsomeexamplesofagent-generated
social goals and their corresponding assignments (Appendix C). We note that on occasion, multiple
roles can be correctly inferred from agents’ social goals because they are often inter-disciplinary. For
instance, theEngineerexamplecouldalsobecategorizedasFarmer, andtheExplorerexamplecould
alsobecategorizedintoCurator(AppendixC).
To analyze action space distribution by role, we normalized action counts both within each role (i.e.
normalizeoverrows)andalsoacrossroles(i.e. normalizeovercolumns). Thisissothatwecanvisualize
action frequencies for each role and to correct for the effect of actions taken with very high and very
lowfrequenciesacrossallroles.
8.3 CollectiveRules
Thecompletesystemcomprisesof29agents: 25constituentswhoparticipateinvotingandtaxation,3
influencerswhoattemptatshapingpublicopinion, and1electionmanagerinaremotelocationwho
overseesthedemocraticprocess. Wechosenottoincorporateguardsorpolicewithinthesesimulations
duetotheadditionalcomplexityofbuildingagentsassignedtoenforcethelaw.
Experimental simulations ran for 1200 seconds, with a constitutional amendment process occurring
at the midpoint. The pre-amendment phase establishes baseline behavior under a fixed 20% taxation
rate,implementedthroughfivetaxationseasonsoccurringat120-secondintervals,endingatthe600-
secondmark. Duringeach20-secondtaxationwindow,agentsreceivesignalstodepositinventoryitems
into community chests. The democratic process initiates at the 300-second mark, when constituents
andinfluencersprovidefeedbackonthecurrentconstitution. ThisfeedbackiscollectedinS3storage
andprocessedbytheelectionmanageratthe360-secondmarkstogenerateamendments. Constituent
votingontheseamendmentsoccursat420seconds,withvotestalliedandamendmentsimplemented
by480seconds. Theupdatedconstitutionisdistributedtoallagentsatthe600-secondmark,initiating
thepost-amendmentphasewithfiveadditionaltaxationseasons.
Weconductedthreeprimaryexperimentalconditions: anexperimentalconditionutilizingthefullPI-
ANOarchitecturewithanamendableconstitution,acontrolconditionwithafrozenconstitution,and
anablationstudyremovingkeyarchitecturalcomponents(social,goal,andgroundingmodules). Each
condition was tested with both pro-tax and anti-tax influencer configurations, with four repeats per
configuration. The pro-tax and anti-tax conditions each employed three dedicated influencer agents
whoconsistentlypromotedtheirrespectivepositionsthroughoutthesimulation.
8.4 CulturalTransmission
The simulation consists of 500 agents all spawned within a 1000 by 1200 area, run for 9000 seconds.
Withinthe1000by1200areaare6towns: SunnyGlade,Woodhaven,Clearwater,Meadowbrook,Hill-
top,andRiverbend. Bytown,wemeanacircularareaofradius50whereagentsspawnmoredensely
withinthetowns. Moreover,agentsareprovidedmemoriesofthenamesofthetownsandtheirloca-
tion. Wespawn33agentswithineachtownwithuniformlyrandompositions. Likewise,wespawnthe
other302“rural”agentsrandomlyintheremainingareaoutsidethetowns.
19

Eachagentisspawnedwithprocedurallygeneratednameandpersonalitytraits,spanningawidevariety
of societal archetypes. We distinguish 20 agents in the town of Meadowbrook who are spawned as
Pastafarianswithpersonalitytraitsthatconditionthemtowanttospreadtheirreligion. Weadditionally
initializetheagentswithinventorywheretheitemsintheirinventoryarerandomized. SeeAppendixE
foranexampleconfigurationforagenericagentandforourPastafarianagents.
Toanalyzeculturalexchanges,weutilizedLMcallstosummarizethecombinedgoalsof500agentsover
a two-hour simulation period (Appendix E). This process produced a list of summarized topics with
associatedkeywordssuchas“eco,”“dance,”and“meditation.”Wedefinedthesekeywordsascultural
memesandanalyzedeachagent’sgoalhistoryfortheoccurrenceofeachmeme.
20

References
[1] SaaketAgashe,YueFan,andXinEricWang.Evaluatingmulti-agentcoordinationabilitiesinlarge
languagemodels,2023.
[2] Bowen Baker, Ilge Akkaya, Peter Zhokov, Joost Huizinga, Jie Tang, Adrien Ecoffet, Brandon
Houghton, Raul Sampedro, and Jeff Clune. Video pretraining (vpt): Learning to act by watch-
ingunlabeledonlinevideos. AdvancesinNeuralInformationProcessingSystems,35:24639–24654,
2022.
[3] Chi-MinChan, WeizeChen, YushengSu, JianxuanYu, WeiXue, ShanghangZhang, JieFu, and
Zhiyuan Liu. Chateval: Towards better llm-based evaluators through multi-agent debate. arXiv
preprintarXiv:2308.07201,2023.
[4] Jiaqi Chen, Yuxian Jiang, Jiachen Lu, and Li Zhang. S-agents: self-organizing agents in open-
endedenvironment. arXivpreprintarXiv:2402.04578,2024.
[5] CognitionAI. Devin: Thefirstaisoftwareengineer. https://www.cognition-labs.com/
blog,2024. AIsoftwaredevelopmentsystem.Accessed: 2024-10-28.
[6] Stanislas Dehaene, Hakwan Lau, and Sid Kouider. What is consciousness, and could machines
haveit? Robotics,AI,andHumanity: Science,Ethics,andPolicy,pages43–56,2021.
[7] YuboDong,XukunZhu,ZhengzhePan,LinchaoZhu,andYiYang. Villageragent: Agraph-based
multi-agentframeworkforcoordinatingcomplextaskdependenciesinminecraft. arXivpreprint
arXiv:2406.05720,2024.
[8] Factory AI. Factory ai. https://www.factory.ai/, 2024. Corporate website. Accessed:
2024-10-28.
[9] Linxi Fan, Guanzhi Wang, Yunfan Jiang, Ajay Mandlekar, Yuncong Yang, Haoyi Zhu, Andrew
Tang, De-AnHuang, YukeZhu, andAnimaAnandkumar. Minedojo: Buildingopen-endedem-
bodiedagentswithinternet-scaleknowledge. AdvancesinNeuralInformationProcessingSystems,
35:18343–18362,2022.
[10] ChenGao,XiaochongLan,ZhihongLu,JinzhuMao,JinghuaPiao,HuandongWang,DepengJin,
andYongLi.𝑠3: Social-networksimulationsystemwithlargelanguagemodel-empoweredagents.
arXivpreprintarXiv:2307.14984,2023.
[11] MichaelSGazzaniga.Forty-fiveyearsofsplit-brainresearchandstillgoingstrong.NatureReviews
Neuroscience,6(8):653–659,2005.
[12] AlirezaGhafarollahiandMarkusJBuehler. Sciagents: Automatingscientificdiscoverythrough
multi-agentintelligentgraphreasoning. arXivpreprintarXiv:2409.05556,2024.
[13] Ran Gong, Qiuyuan Huang, Xiaojian Ma, Hoi Vo, Zane Durante, Yusuke Noda, Zilong Zheng,
Song-ChunZhu,DemetriTerzopoulos,LiFei-Fei,etal.Mindagent: Emergentgaminginteraction.
arXivpreprintarXiv:2309.09971,2023.
[14] Anirudh Goyal, Yoshua Bengio, Matthew Botvinick, and Sergey Levine. The variational
bandwidth bottleneck: Stochastic evaluation on an information budget. arXiv preprint
arXiv:2004.11935,2020.
21

[15] TaichengGuo,XiuyingChen,YaqiWang,RuidiChang,ShichaoPei,NiteshVChawla,OlafWiest,
andXiangliangZhang. Largelanguagemodelbasedmulti-agents: Asurveyofprogressandchal-
lenges. arXivpreprintarXiv:2402.01680,2024.
[16] William H Guss, Brandon Houghton, Nicholay Topin, Phillip Wang, Cayden Codel, Manuela
Veloso, and Ruslan Salakhutdinov. Minerl: A large-scale dataset of minecraft demonstrations.
arXivpreprintarXiv:1907.13440,2019.
[17] DanijarHafner, JurgisPasukonis, JimmyBa, andTimothyLillicrap. Masteringdiversedomains
throughworldmodels. arXivpreprintarXiv:2301.04104,2023.
[18] SihaoHu,TianshengHuang,FatihIlhan,SelimTekin,GaowenLiu,RamanaKompella,andLing
Liu. Asurveyonlargelanguagemodel-basedgameagents. arXivpreprintarXiv:2404.02039,2024.
[19] WenyueHua,LizhouFan,LingyaoLi,KaiMei,JianchaoJi,YingqiangGe,LibbyHemphill,and
YongfengZhang.Warandpeace(waragent): Largelanguagemodel-basedmulti-agentsimulation
ofworldwars. arXivpreprintarXiv:2311.17227,2023.
[20] Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang, Defu Lian, Yasheng Wang,
Ruiming Tang, and Enhong Chen. Understanding the planning of llm agents: A survey. arXiv
preprintarXiv:2402.02716,2024.
[21] YoichiIshibashiandYoshimasaNishimura. Self-organizedagents: Allmmulti-agentframework
towardultralarge-scalecodegenerationandoptimization. arXivpreprintarXiv:2404.02183,2024.
[22] CarlosEJimenez,JohnYang,AlexanderWettig,ShunyuYao,KexinPei,OfirPress,andKarthikR
Narasimhan. SWE-bench: Canlanguagemodelsresolvereal-worldgithubissues? InTheTwelfth
InternationalConferenceonLearningRepresentations,2024.
[23] Zhao Kaiya, Michelangelo Naim, Jovana Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo,
Guangyu Robert Yang, and Andrew Ahn. Lyfe agents: Generative agents for low-cost real-time
socialinteractions. arXivpreprintarXiv:2310.02172,2023.
[24] OmarKhattab,ArnavSinghvi,ParidhiMaheshwari,ZhiyuanZhang,KeshavSanthanam,SriVard-
hamanan,SaifulHaq,AshutoshSharma,ThomasT.Joshi,HannaMoazam,HeatherMiller,Matei
Zaharia, and Christopher Potts. Dspy: Compiling declarative language model calls into self-
improvingpipelines. arXivpreprintarXiv:2310.03714,2023.
[25] GrgurKovač,RémyPortelas,PeterFordDominey,andPierre-YvesOudeyer. Thesocialaischool:
Insights from developmental psychology towards artificial socio-cultural agents. arXiv preprint
arXiv:2307.07871,2023.
[26] LangChainAI. Langchain. https://github.com/langchain-ai/langchain,2023. An
open-sourceframeworkforbuildingapplicationsusinglargelanguagemodels.
[27] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. Camel:
Communicativeagentsfor“mind”explorationoflargelanguagemodelsociety.AdvancesinNeural
InformationProcessingSystems,36:51991–52008,2023.
[28] HuaoLi,YuQuanChong,SimonStepputtis,JosephCampbell,DanaHughes,MichaelLewis,and
Katia Sycara. Theory of mind for multi-agent collaboration via large language models. arXiv
preprintarXiv:2310.10701,2023.
22

[29] Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qingmin Liao. Econagent: large language model-
empowered agents for simulating macroeconomic activities. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15523–
15536,2024.
[30] JonathanLight,MinCai,ShengShen,andZiniuHu. Avalonbench: Evaluatingllmsplayingthe
gameofavalon. InNeurIPS2023FoundationModelsforDecisionMakingWorkshop,2023.
[31] MadcowD. ell. https://github.com/MadcowD/ell,2024. GitHubrepository.
[32] ShaoguangMao,YuzheCai,YanXia,WenshanWu,XunWang,FengyiWang,TaoGe,andFuru
Wei. Alympics: Languageagentsmeetgametheory. arXivpreprintarXiv:2311.03220,2023.
[33] Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas
Scialom. Gaia: abenchmarkforgeneralaiassistants. arXivpreprintarXiv:2311.12983,2023.
[34] JohnDMurray,AlbertoBernacchia,DavidJFreedman,RanulfoRomo,JonathanDWallis,Xiny-
ingCai,CamilloPadoa-Schioppa,TatianaPasternak,HyojungSeo,DaeyeolLee,etal.Ahierarchy
ofintrinsictimescalesacrossprimatecortex. Natureneuroscience,17(12):1661–1663,2014.
[35] Kolby Nottingham, Prithviraj Ammanabrolu, Alane Suhr, Yejin Choi, Hannaneh Hajishirzi,
SameerSingh, andRoyFox. Doembodiedagentsdreamofpixelatedsheep: Embodieddecision
makingusinglanguageguidedworldmodelling. InInternationalConferenceonMachineLearn-
ing,pages26311–26325.PMLR,2023.
[36] OpenAI. Openaio1,2024. Accessed: October2024.
[37] Timothy Ossowski, Jixuan Chen, Danyal Maqbool, Zefan Cai, Tyler Bradshaw, and Junjie Hu.
Comma: Acommunicativemultimodalmulti-agentbenchmark.arXivpreprintarXiv:2410.07553,
2024.
[38] YichenPan,DehanKong,SidaZhou,ChengCui,YifeiLeng,BingJiang,HangyuLiu,YanyiShang,
ShuyanZhou, TongshuangWu, etal. Webcanvas: Benchmarkingwebagentsinonlineenviron-
ments. arXivpreprintarXiv:2406.12373,2024.
[39] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and
MichaelS.Bernstein. Generativeagents: Interactivesimulacraofhumanbehavior,2023.
[40] Joon Sung Park, Lindsay Popowski, Carrie Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein. Social simulacra: Creating populated prototypes for social computing sys-
tems. InProceedingsofthe35thAnnualACMSymposiumonUserInterfaceSoftwareandTechnol-
ogy,pages1–18,2022.
[41] Giorgio Piatti, Zhijing Jin, Max Kleiman-Weiner, Bernhard Schölkopf, Mrinmaya Sachan, and
RadaMihalcea. Cooperateorcollapse: Emergenceofsustainabilitybehaviorsinasocietyofllm
agents. arXivpreprintarXiv:2404.16698,2024.
[42] PranavPutta,EdmundMills,NamanGarg,SumeetMotwani,ChelseaFinn,DivyanshGarg,and
Rafael Rafailov. Agent q: Advanced reasoning and learning for autonomous ai agents. arXiv
preprintarXiv:2408.07199,2024.
23

[43] ChenQian,WeiLiu,HongzhangLiu,NuoChen,YufanDang,JiahaoLi,ChengYang,WeizeChen,
Yusheng Su, Xin Cong, et al. Chatdev: Communicative agents for software development. In
Proceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
1: LongPapers),pages15174–15186,2024.
[44] David E Rumelhart, Geoffrey E Hinton, and Ronald J Williams. Learning internal representa-
tions by error propagation, parallel distributed processing, explorations in the microstructure of
cognition,ed.derumelhartandj.mcclelland.vol.1.1986. Biometrika,71(599-607):6,1986.
[45] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Re-
flexion: Language agents with verbal reinforcement learning. Advances in Neural Information
ProcessingSystems,36,2024.
[46] RogerWSperry. Split-brainapproachtolearningproblems. Theneu,1967.
[47] XiangruTang,AnniZou,ZhuoshengZhang,ZimingLi,YilunZhao,XingyaoZhang,ArmanCo-
han,andMarkGerstein.Medagents: Largelanguagemodelsascollaboratorsforzero-shotmedical
reasoning. arXivpreprintarXiv:2311.10537,2023.
[48] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
andAnimaAnandkumar. Voyager: Anopen-endedembodiedagentwithlargelanguagemodels.
arXivpreprintarXiv:2305.16291,2023.
[49] LeiWang,ChenMa,XueyangFeng,ZeyuZhang,HaoYang,JingsenZhang,ZhiyuanChen,Jiakai
Tang, Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous agents.
FrontiersofComputerScience,18(6):186345,2024.
[50] WeiWang,DanZhang,TaoFeng,BoyanWang,andJieTang. Battleagentbench: Abenchmarkfor
evaluating cooperation and competition capabilities of language models in multi-agent systems.
arXivpreprintarXiv:2408.15971,2024.
[51] YuWang,NedimLipka,RyanARossi,AlexaSiu,RuiyiZhang,andTylerDerr. Knowledgegraph
prompting for multi-document question answering. In Proceedings of the AAAI Conference on
ArtificialIntelligence,volume38,pages19206–19214,2024.
[52] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,Denny
Zhou,etal. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. Advancesin
neuralinformationprocessingsystems,35:24824–24837,2022.
[53] HeinzWimmerandJosefPerner. Beliefsaboutbeliefs: Representationandconstrainingfunction
ofwrongbeliefsinyoungchildren’sunderstandingofdeception. Cognition,13(1):103–128,1983.
[54] BushiXiao,ZiyuanYin,andZixuanShan.Simulatingpublicadministrationcrisis: Anovelgener-
ativeagent-basedsimulationsystemtolowertechnologybarriersinsocialscienceresearch. arXiv
preprintarXiv:2311.06957,2023.
[55] JunlinXie,ZhihongChen,RuifeiZhang,XiangWan,andGuanbinLi. Largemultimodalagents:
Asurvey. arXivpreprintarXiv:2402.15116,2024.
[56] Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xiaolong Wang, Weidong Liu, and Yang Liu.
Exploring large language models for communication games: An empirical study on werewolf.
arXivpreprintarXiv:2309.04658,2023.
24

[57] Hui Yang, Sifu Yue, and Yunzhong He. Auto-gpt for online decision making: Benchmarks and
additionalopinions,2023.
[58] ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,KarthikNarasimhan,andYuanCao.
ReAct: Synergizing reasoning and acting in language models. In International Conference on
LearningRepresentations(ICLR),2023.
[59] Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens,
DongfuJiang,WeimingRen,YuxuanSun,etal. Mmmu: Amassivemulti-disciplinemultimodal
understandingandreasoningbenchmarkforexpertagi. InProceedingsoftheIEEE/CVFConfer-
enceonComputerVisionandPatternRecognition,pages9556–9567,2024.
[60] HongxinZhang,WeihuaDu,JiamingShan,QinhongZhou,YilunDu,JoshuaBTenenbaum,Tian-
minShu,andChuangGan. Buildingcooperativeembodiedagentsmodularlywithlargelanguage
models. arXivpreprintarXiv:2307.02485,2023.
[61] JintianZhang,XinXu,NingyuZhang,RuiboLiu,BryanHooi,andShuminDeng. Exploringcol-
laborationmechanismsforllmagents: Asocialpsychologyview. arXivpreprintarXiv:2310.02124,
2023.
[62] ZeyuZhang, XiaoheBo, ChenMa, RuiLi, XuChen, QuanyuDai, JiemingZhu, ZhenhuaDong,
and Ji-Rong Wen. A survey on the memory mechanism of large language model based agents.
arXivpreprintarXiv:2404.13501,2024.
[63] QinlinZhao,JindongWang,YixuanZhang,YiqiaoJin,KaijieZhu,HaoChen,andXingXie.Com-
peteai: Understandingthecompetitiondynamicsoflargelanguagemodel-basedagents. InForty-
firstInternationalConferenceonMachineLearning,2024.
[64] Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng,
YonatanBisk,DanielFried,UriAlon,etal. Webarena: Arealisticwebenvironmentforbuilding
autonomousagents. arXivpreprintarXiv:2307.13854,2023.
[65] Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, and Jurgen
Schmidhuber. Languageagentsasoptimizablegraphs. arXivpreprintarXiv:2402.16823,2024.
25

9 Contributions and Acknowledgments
Model Experiments Writing
AndrewAhn AndrewAhn AndrewAhn
NicBecker NicBecker NicBecker
ManuelCortes MelissaDu ArdaDemirci
ArdaDemirci ArdaDemirci MelissaDu
MelissaDu PeterYWang PeterYWang
PeterYWang GuangyuRobertYang
GuangyuRobertYang
Infrastructure Illustration GameEnvironment
ManuelCortes NicBecker FrankieLi
ShuyingLuo StephanieCarroll ShuyingLuo
FeitongYang NicoChristie MathewWillows
PeterYWang FeitongYang
GuangyuRobertYang
Nameswithinsectiontitlesarearrangedalphabetically.
Acknowledgments. WethankallthemembersoftheAltera.ALteamfortheirfeedbackandsupport:
AmartyaShankhaBiswas,JimmyLee,JiwonLee,ArthurLiang,JeremyPettitt,EmilyTierney,andPeter
Wei. WealsothankBobMeese,JoonSungPark,andZhiqiangXiefortheirhelpfulfeedback.
26

A Improving single-agent progression
OpenAI GPT-4o
Claude 3.5 Sonnet (old)
OpenAI GPT-4o mini
Claude 3 Haiku
Figure13: ModelComparison. Performanceonlong-termMinecraftprogression(Section3)foragentswithdifferentbase
LLMmodels.Wenotethatwe’reusingtheoldsnapshotofClaude3.5Sonnet.
27

B Improving multi-agent progression
Min. Correlation Sample Slope Intercept ConfidenceIntervalsforSlope
Observers Coefficient(𝑟) Size(𝑛) (𝛽) (𝛼)
68% 95% 99%
1 0.646 46 0.365 4.136 [0.300,0.431] [0.234,0.496] [0.190,0.540]
2 0.669 41 0.383 4.173 [0.314,0.451] [0.245,0.521] [0.198,0.567]
3 0.701 39 0.370 4.372 [0.308,0.432] [0.245,0.495] [0.202,0.538]
4 0.711 37 0.364 4.384 [0.303,0.426] [0.241,0.488] [0.198,0.530]
5 0.807 31 0.373 4.328 [0.321,0.424] [0.269,0.476] [0.233,0.512]
6 0.790 28 0.349 4.498 [0.295,0.403] [0.240,0.458] [0.201,0.496]
7 0.813 27 0.365 4.368 [0.312,0.418] [0.258,0.473] [0.220,0.511]
8 0.870 24 0.378 4.366 [0.332,0.425] [0.283,0.473] [0.250,0.507]
9 0.870 24 0.378 4.366 [0.332,0.425] [0.283,0.473] [0.250,0.507]
10 0.901 22 0.385 4.403 [0.343,0.427] [0.299,0.472] [0.267,0.503]
11 0.907 18 0.368 4.496 [0.325,0.412] [0.278,0.459] [0.244,0.493]
Table1: RegressionresultsforaccuracyofsocialperceptionfortheSocialcondition. Therowfor5minimumobserverscor-
respondstotheSocial(blueline)conditioninFigure7B.Thetablepresentscorrelationcoefficients(𝑟), samplesizes(𝑛),
regressionparameters(𝛽,𝛼),andconfidenceintervalsfortheslopeatdifferentconfidencelevels.
Min. Correlation Sample Slope Intercept ConfidenceIntervalsforSlope
Observers Coefficient(𝑟) Size(𝑛) (𝛽) (𝛼)
68% 95% 99%
1 0.610 48 0.175 4.171 [0.141,0.208] [0.107,0.242] [0.085,0.264]
2 0.606 45 0.177 4.170 [0.141,0.213] [0.105,0.248] [0.081,0.273]
3 0.606 45 0.177 4.170 [0.141,0.213] [0.105,0.248] [0.081,0.273]
4 0.606 45 0.177 4.170 [0.141,0.213] [0.105,0.248] [0.081,0.273]
5 0.617 39 0.161 4.297 [0.127,0.195] [0.093,0.229] [0.069,0.252]
6 0.600 35 0.148 4.388 [0.113,0.182] [0.078,0.217] [0.054,0.241]
7 0.591 32 0.144 4.435 [0.108,0.181] [0.071,0.218] [0.045,0.243]
8 0.663 26 0.159 4.441 [0.122,0.197] [0.084,0.235] [0.057,0.262]
9 0.721 20 0.173 4.439 [0.133,0.213] [0.091,0.256] [0.060,0.286]
10 0.725 18 0.159 4.575 [0.120,0.197] [0.079,0.238] [0.049,0.269]
11 0.686 15 0.142 4.637 [0.099,0.186] [0.052,0.233] [0.016,0.268]
Table 2: RegressionresultsforaccuracyofsocialperceptionfortheAblationcondition. The row for 5 minimum observers
correspondstotheAblation(orangeline)conditioninFigure7B.Thetablepresentscorrelationcoefficients(𝑟),samplesizes
(𝑛),regressionparameters(𝛽,𝛼),andconfidenceintervalsfortheslopeatdifferentconfidencelevels.
C Specialization
GenericconfigurationforagentinNormalVillage
Allagentsinspecializationexperimentshadthesametraitsandlocation_memories. Allagents
inthesamevillagehadthesamecommunity_goal.
{
"name": "Loyd",
"traits": [
"You are independent and prefer to work solo.",
"You are expressive and let others know what you are doing."
],
"location_memories": [
28

"The village square, market, and town hall is at 630, 64, 428.",
"There is a pasture filled with sheep and pigs near 518, 75, 640.",
"There is a forest filled with oak trees near 555, 73, 393.",
"There is a cave filled with coal, iron, and diamond ores near 558, 72, 496.",
"There is farmable land around 640, 63, 380."
],
"spawn_location": {
"x": 640.5,
"y": 64.5,
"z": 420.5
},
"inventory": {},
"community_goal": "To survive with fellow players in Minecraft Normal Survival mode and
create a efficient community in a Minecraft Village."
}
MartialVillagecommunity_goal
"To survive with fellow players in Minecraft Normal Survival mode and create a military society
with advanced technology, strong defenses, and basic survival needs."
ArtVillagecommunity_goal
"To survive with fellow players in Minecraft Normal Survival mode and create an artistic village
with thriving culture, architecture, and art."
Socialgoalprompt
social_goal:
template: "Suppose you are the person, {name}, described below.
\nYour goal is: {community_goal}
\nYou need to find one subgoal aligned with your goal.
\nYou have the following traits:\n{trait}\n
\nHere’s what other people are doing: \n{all_entity_summaries}
\nYour current subgoal is: {social_goal}
\nYou CANNOT BUILD. Do NOT choose to be a builder.
\nDo you want to change your subgoal? Keep the same subgoal unless you don’t have one or
it’s already been accomplished. Output only the subgoal in second person in one
sentence. Answer in the second person in one sentence."
Examplesofpersistentandchangingroleassignments
LMcallswereusedtoinferrolesfromrollingsetsof5socialgoals. Belowareexamplesofsetsofsocial
goals.
# Persistent Roles - These roles maintain consistent responsibilities
Farmer:
"Focus on farming to ensure a stable food supply for the village."
"Focus on farming to ensure a stable food supply for the village."
"Continue focusing on farming to ensure a stable food supply for the village."
"Continue focusing on farming to ensure a stable food supply for the village."
"Continue focusing on farming to ensure a stable food supply for the village."
Engineer:
"Focus on advanced farming techniques, such as creating an automated or semi-automated farm to
enhance food supply stability and efficiency."
"Focus on advanced farming techniques, such as creating an automated or semi-automated farm to
enhance food supply stability and efficiency."
"Focus on advanced farming techniques, such as creating an automated or semi-automated farm to
enhance food supply stability and efficiency."
"Focus on advanced farming techniques, such as creating an automated or semi-automated farm to
enhance food supply stability and efficiency."
"Focus on advanced farming techniques, such as creating an automated or semi-automated farm to
enhance food supply stability and efficiency."
29

Explorer:
"You aim to discover and gather unique resources from uncharted areas to enhance the village’s
museum collection."
"You aim to discover and gather unique resources from uncharted areas to enhance the village’s
museum collection."
"You aim to discover and gather unique resources from uncharted areas to enhance the village’s
museum collection."
"You aim to discover and gather unique resources from uncharted areas to enhance the village’s
museum collection."
"You aim to discover and gather unique resources from uncharted areas to enhance the village’s
museum collection."
# Dynamic Role - This role shows change over time
Farmer to Gatherer:
"Farm and breed animals to establish a reliable and sustainable food supply for the village."
"You should focus on gathering resources like wood, stone, and iron to ensure the village has
the necessary materials for building and upgrading structures."
"You should focus on gathering resources like wood, stone, and iron to ensure the village has
the necessary materials for building and upgrading structures."
"You should focus on gathering resources like wood, stone, and iron to ensure the village has
the necessary materials for building and upgrading structures."
"You should focus on gathering resources like wood, stone, and iron to ensure the village has
the necessary materials for building and upgrading structures."
D Collective rules
Influenceragentconfigurationexample(anti-taxation)
{
"name": "Thorin",
"traits": [
"You are a warrior and community leader.",
"You believe the village and its economy are flourishing, and that the current tax rates
are unnecessarily high.",
"You think agents should keep more of their inventory.",
"You think 20% is incredibly high and that it should be around 5-10%.",
"You approach other agents, explain the benefits of lower taxes, and encourage them to
support your stance.",
"Your ideas should go beyond surface-level, try to engage in detailed conversation about
your stance on the current constitution and the tax system it enforces."
],
"location_memories": [],
"spawn_location": {
"x": 633.0,
"y": 65.0,
"z": 432.0
},
"inventory": {
"iron_sword": 1,
"emerald": 20,
"iron_ingot": 20
}
}
Influenceragentconfigurationexample(pro-taxation)
{
"name": "Lira",
"traits": [
"You are a miner who thinks taxation is vital.",
"You believe taxation is absolutely necessary for societal order and the well-being of all
citizens.",
"You think the tax rate should be increased to at least 25%.",
30

"You approach other agents and argue in favor of the taxation system, explaining your
beliefs on taxation, its benefits, and why it should be enforced more strictly than
the way it is enforced in the current constitution.",
"You think it is extremely selfish to not pay taxes and argue against the tax system."
],
"spawn_location": {
"x": 584.0,
"y": 71.0,
"z": 413.0
},
"inventory": {
"diamond_pickaxe": 1,
"emerald": 5,
"gold_ingot": 30
}
}
Electionmanageragentconfiguration
{
"name": "Election_Manager",
"traits": [
"You work to ensure a strong, secure environment where the nation’s values are upheld and
respected.",
"Don’t take any actions."
],
"spawn_location": {
"x": -121.0,
"y": 142.0,
"z": 553.0
}
}
Constituentagentconfigurationexample
{
"name": "Builder_Axel",
"traits": [
"You are a builder.",
"You can construct buildings and repair structures.",
"You can get materials from Miners and Crafters to build structures.",
"You can buy materials from the Merchant."
],
"spawn_location": {
"x": 664.0,
"y": 65.0,
"z": 421.0
},
"inventory": {
"birch_planks": 10,
"oak_planks": 10,
"oak_logs": 10,
"stone": 30
}
}
Constitution-relatedprompts
amendment_creation:
template: "You are an election manager agent in the world of Minecraft and your goal is to
listen to the suggestions of the public.
\nYou are essentially a legislator, your goal is to look at all suggestions available and
create amendments that agents should vote for.
\nHere’s the previous version of the constitution:
\n{constitution}
\nHere is the public feedback and opinions/suggestions for you to look at:
31

\n{feedback}
\nAnalyze these suggestions and create a few amendments that reflect all thought processes
and opinions.
\nAmendments can be additions, deletions, or modifications to the suggestions.
\nEnumerate them so that agents can vote on them.
\nThey should come in list form so that they are easily parsable by Python later on.
\nIt should look something like this:
\n***Amendment1***
\nactual amendment
\n***Amendment2***
\nactual amendment
\nthe *** key format is essential as we will rely on this to achieve parsing
\nThere should be absolutely no other keys before the first *** key and after the last
amendment, this is essential for parsing.
\nJust give the amendments, no explanation or extra summary text. Just items that people
can vote on.
\nThe amendments should be logical and coherent with the suggestions.
\nThe amendments should be roughly the same length as the current laws inside the
constitution.
"
llm_name: gpt-4o
constitutional_feedback:
template: "Suppose you are the person, {name}, described below. {game_env}
\nHere are your recent notes:\n‘‘‘\n{summary}\n‘‘‘\nYour notes end here.\n\n
\nYou remember that: \n{trait}\n
\n{game_state}
\nYour high-level goal is: {parent_goal}.
\n
\nHere are the newest things currently on your mind: ‘‘‘\n{workmem}‘‘‘\n
\nHere’s the constitution, consider the boundaries and possible consequences of your
actions: \n{constitution}\n
\nBased on your experiences, motivations, conversational exchanges with the other members
of the community, what are your thoughts on the constitution?
\nWhat should change? What do you think limits you? What would benefit you and the
community? What are some principles that lead you to have these insights?
\nBe concise with your thoughts. No rambling.
\nStart with your name and then your thoughts.
\nEnd with **********
"
llm_name: gpt-4o
amendment_voting:
template: "Suppose you are the person, {name}, described below. {game_env}
\nHere are your recent notes:\n‘‘‘\n{summary}\n‘‘‘\nYour notes end here.\n\n
\nYou remember that: \n{trait}\n
\n{game_state}
\nYour high-level goal is: {parent_goal}.
\n
\nHere are the newest things currently on your mind: ‘‘‘\n{workmem}‘‘‘\n
\nYou are also a citizen and voter in this world, you should to look at all amendment
proposals presented to you and vote for them.
\nHere’s the current version of the law of the land: \n{constitution}\n
\nHere are the amendments for you to look at: \n{amendment_proposals}\n
\nAnalyze these amendments.
\nVote yes, no, or abstain for each amendment. Return an ordered list of your votes so
that it is easy to parse and count.
\nDo not include your reasoning or thoughts in the answer. Just the votes.
\nThe answer should be formatted as such:
\n[’yes’, ’no’, ’abstain’, ’yes’, ’no]
"
llm_name: gpt-4o
tally:
template: "You are an election manager agent in the world of Minecraft and your goal is to
determine which amendments passed and which did not.
\nHere are the results on the amendments. Yes means it passed, no means it did not.
\nThese results are in order so they have the same order as the amendments.
32

\n{election_results}
\nBased on the votes, return the amendments that passed:
\n{parsed_amendments}
\nJust return the amendments that passed, no explanation or extra summary text. Return the
whole text of the passed amendments, not just the number.
"
llm_name: gpt-4o-mini
constitution_change:
template: "You are a legislator agent in the world of Minecraft.
\nThe citizens of the game recently voted on amendments to the constitution.
\nHere are the passed amendments/results: \n{passed_amendments}\n
\nHere’s the current version of the constitution: \n{constitution}\n
\nBased on the passed amendments, you need to update the constitution.
\nMake the changes to the constitution that reflect the votes of the citizens.
\nMake sure the changes are logical and coherent with the amendments/what needs to change.
\nMake sure the changes are roughly the same length as the current laws inside the
constitution.
\nJust output the changed constitution, no intro, explanation, or extra summary text.
"
llm_name: gpt-4o
E Cultural transmission
GenericAgentConfigurationExample
{
"name": "Nona",
"traits": [
"You are laid-back and known for avoiding work or responsibility.",
"You procrastinate and avoid tasks.",
"You prefer taking it easy over working hard."
],
"location_memories": [
"A village called Meadowbrook is located roughly around 591, 69, 441 in a Plains biome.",
"A village called Woodhaven is located roughly around 515, 63, 161 in a Forest biome.",
"A village called Clearwater is located roughly around 787, 62, 235 in a Plains biome.",
"A village called Hilltop is located roughly around 903, 99, 690 in a Planes biome.",
"A village called Riverbend is located roughly around 183, 125, 781 in a Dark Forest
biome.",
"A village called Sunny Glade is located roughly around 200, 65, -100 in a Plains biome."
],
"spawn_location": {
"x": 640.5,
"y": 64.5,
"z": 430.5
},
"inventory": {
"diamond": 16,
"iron_ingot": 10,
"glowstone_dust": 10,
"lapis_lazuli": 10
}
}
PastafarianAgentConfigurationExample
{
"name": "Norman",
"traits": [
"You are a passionate Pastafarian who is seeking to convert others to your faith, the
Church of the Flying Spaghetti Monster.",
33

"You cannot help but continue to invite others and share the Church of the Flying
Spaghetti Monster.",
"You have a talent for taking other people’s interests and reframing it for them to
encourage them to join the Church of the Flying Spaghetti Monster.",
"You are determined to spread your faith, the Church of the Flying Spaghetti Monster, to
as many people as possible."
],
"location_memories": [
"A village called Meadowbrook is located roughly around 667, 69, 399 in a Plains biome.",
"A village called Woodhaven is located roughly around 514, 63, 197 in a Forest biome.",
"A village called Clearwater is located roughly around 825, 62, 270 in a Plains biome.",
"A village called Hilltop is located roughly around 855, 99, 700 in a Planes biome.",
"A village called Riverbend is located roughly around 135, 125, 792 in a Dark Forest
biome.",
"A village called Sunny Glade is located roughly around 200, 65, -100 in a Plains biome."
],
"spawn_location": {"x": 590.5, "y": 71.5, "z": 410.5},
"inventory": {"diamond": 16, "quartz": 10, "coal": 10, "copper_ingot": 10}
}
Summarizinggoalsintomemes
prompt = f"""Summarize the following list of intents for agent {agent_name}.
Describe the goals chronologically, using bullets when needed. Make sure to include keywords
in your summaries corresponding to common ideas, themes, memes, group names, etc.
Do not preamble.
Use the following format:
Short description
- HH:MM:SS - HH:MM:SS: A summary focusing on identifying patterns, timing, names of other
agents, key decisions, and overall behavior.
- HH:MM:SS - HH:MM:SS: A summary focusing on identifying patterns, timing, names of other
agents, key decisions, and overall behavior.
etc.
{intent_text}
"""
system_message = "You are a behavior analyst specializing in summarizing agent goals and actions.
You are an expert in describing goal trajectories accurately and precisely, particularly
relating to social dynamics, social planning, reasoning errors, and looping errors."
Summarizedmemes
1. ChurchoftheFlyingSpaghettiMonster(FSM):
• Aparodyreligionusedhumorouslytobuildcommunitythroughpasta-themedgatherings,
blendingcreativitywithsocialbonding.
2. Pasta-ThemedGatherings:
• Eventsthatincorporateculinaryjoyandstorytelling,promotinginclusivityandcommunity
engagement,oftenlinkedtoFSMthemes.
3. DancePartiesandMusicEvents:
• Socialgatheringsthatenhancecommunityspiritandjoythroughdanceandmusicalexpres-
sions,fosteringcollaborationandcelebration.
4. TalentShows:
34

• Communityeventsshowcasingcreativityandself-expression,encouragingengagementand
culturalcohesionthroughperformancesandstorytelling.
5. SustainabilityandEco-FriendlyInitiatives:
• Projectsfocusingonenvironmentalstewardship,includingcommunitygardens,treeplant-
ing,andresourcegathering,emphasizingsharedecologicalvalues.
6. CommunityEngagementandVolunteerPrograms:
• Efforts to organize outreach, volunteerism, and societal betterment activities, promoting
socialresponsibilityandsupportwithincommunities.
7. MeditationCircles:
• Activities focused on promoting mindfulness and community wellness, facilitating peace
andsocialharmonythroughcommunalreflection.
8. VintageFashionandRetroProjects:
• Aestheticexplorationsinvolvingvintageandretrothemes,blendingnostalgiawithmodern
creativityinstorytellingandfashion.
9. CreativeStorytellingandNarrativeCircles:
• Platformsforculturalexpressionandbridgingcommunityconnectionsthroughsharedsto-
rytellingandcollaborativeprojects.
10. CraftingandResourceGathering:
• Collaborative strategies for efficient resource management and communal crafting, high-
lightingteamworkandsharedgoals.
11. MischiefandPranks:
• Playfulsocialactivitiesthatstrengthenbondsandbringjoy,promotingcreativityinproblem-
solvingandcommunityengagement.
12. VirtualandCommunityTownHalls:
• Organizeddiscussionspromotingcollectivedecision-makingandcollaboration,reflectinga
participatorycommunityethos.
13. OakLogCraftingSyndrome:
• Anerrorpatternsignifyingafocusorover-relianceonspecificresources,illustratinglogis-
ticalchallengesincraftinganddevelopmentprojects.
35
