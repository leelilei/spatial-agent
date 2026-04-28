# HC06 - Project Sid: Many-agent simulations toward AI civilization

## Stable Widened-Core Snapshot

- core_layer: `anchor_core`
- admission_status: `stable_anchor`
- corpus_tier: `Core`
- system_family: `Project Sid`
- paper_refs: `Altera2024`
- year: `2024`
- agent_count: `100+`
- environment_side_representation: `3D_engine`
- agent_accessible_representation: `L5`
- behavioral_scale: `emergent_social_structure`
- behavior_type: `cooperation; conflict; mobility; role_differentiation; norm_formation`
- evidence_status: `designed_affordance_only`
- spatial_behavior_coupling: `explicit`
- evaluation_method: `mixed`
- space_syntax_construct: `none`
- source_basis: `local_pdf_ocr_and_reading_note`
- artifact_class: `local_pdf`

## Representation Gap Note

Appendix and configuration evidence expose direct coordinate-bearing location memories and explicit spawn locations, so the agent-facing interface reaches geometry level.

## Original Artifact Pointer

- local_artifact_path: `assets/survey_paper/pdfs/phase1_core/03_Project_Sid_Altera2024.pdf`

## Source Content

Title: Introduction

Source PDF: D:\0-AI相关研究\1-spatialagent\spatial-agent\assets\survey_paper\pdfs\phase1_core\03_Project_Sid_Altera2024.pdf

Extraction:
- backend: pypdf
- extracted_at_utc: 2026-04-28T16:32:19+00:00
- page_count: 35
- status: ok
- text_char_count: 88894

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
and complexity. Large-scale simulations involving many autonomous agents—reflecting the full spectrum of
civilizational processes—have yet to be explored. Here, we demonstrate how 10 – 1000+ AI agents behave
andprogresswithinagentsocieties. WefirstintroducethePIANO(ParallelInformationAggregationviaNeu-
ral Orchestration) architecture, which enables agents to interact with humans and other agents in real-time
while maintaining coherence across multiple output streams. We then evaluate agent performance in large-
scale simulations using civilizational benchmarks inspired by human history. These simulations, set within
a Minecraft environment, reveal that agents are capable of meaningful progress—autonomously developing
specialized roles, adhering to and changing collective rules, and engaging in cultural and religious transmis-
sion. These preliminary results show that agents can achieve significant milestones towards AI civilizations,
opening new avenues for large-scale societal simulations, agentic organizational intelligence, and integrating
AIintohumancivilizations.
Figure1: Fromagentarchitecturetoagentcivilization
1SeeContributionssectionforcompleteauthorlist.
1
arXiv:2411.00114v1  [cs.AI]  31 Oct 2024

1 Introduction
1.1 Why should we try to build an AI civilization?
For agents to coexist with us in our own societies, they need to be autonomous and collaborative. In
recent years, advancements in reasoning and decision-making in LLMs have significantly enhanced
agentautonomy(52;58;36;45). However,autonomyaloneisinsufficient. AIagentsmustalsocoexist
alongside humans and other agents in a human civilization. In this paper, we define a civilization as
an advanced society that has achieved a high level of institutional development, which manifests in
specialized roles, organized governance, and advancements in areas like science, art, and commerce.
Wearguethatcivilizationalprogress-measuredbytheabilityofagentstocoexistandprogressinhuman
civilizations-representstheultimatebenchmarkforAIagentability.
Inthistechnicalreport,wedescribeourfirsteffortstoimproveandbenchmarkagentabilityinhuman
civilizations. First, weintroducePIANO(ParallelInformationAggregationviaNeuralOrchestration),
a new cognitive architecture designed to enhance both autonomy and real-time interaction of agents.
UsingPIANO,wesimulatesinglesocietiesof50-100agentsaswellascivilizationsof500-1,000agents
livinginmultiplesocietiesthatinteractwithoneanother. Finally,weevaluateagentperformanceusing
new metrics thatare aligned with human civilizational progress. We show that agentsform their own
professionalidentities,obeycollectiverules,transmitculturalinformationandexertreligiousinfluence,
andusesophisticatedinfrastructures,suchaslegalsystems.
1.2 The current agent landscape
Modern AI Agents typically consist of multiple LLM-powered modules for reasoning, memory, plan-
ning, and tool use (49; 18; 55; 20; 62). Individual agents have been developed for various applications
includingcoding(5;8),webbrowsing(64;42),andgameplay(48).
RecentresearcheffortsinLLM-poweredmulti-agentsystemsgenerallyfallunderthreecategories: pro-
ductivity, games, and social modeling. Multi-agent frameworks have been deployed in software de-
velopment (43; 27), cooperative robotic control (60), scientific experiments (12; 47), and debates (3).
Multi-agent simulations have also been tested in various game environments (56; 13; 30; 28). Sepa-
rately, they’ve been used to model developmental psychology (25; 61), game theory (32), macroeco-
nomics(29;63),socialpolicies(41;54;19),andcommunitydynamics(40;39;10).
Inmanyoftheseworks,agentsarenotcompletelyautonomousandareconstrainedbyeitheragentar-
chitecture or by the simulated environment. Common constraints include turn-based execution, con-
strainedworkflows,orrigidcommunicationchannelsbetweenagents(65;21;4).
Severaloftheseworksconsiderlarge-scalesimulations,thoughinrestrictedsettings. Forexample,(40)
and(10)simulatedsocialnetworksofupto18,000personas. Toourknowledge,fullyautonomoussocial
communicationinopen-worldenvironmentshavenotbeenattemptedingamesorothersettings(15).
1.3 Why is it hard to build AI civilizations?
Large agent groups have yet to demonstrate the ability to progress over long time horizons. Below, we
reviewthekeyreasonsforthislimitedprogressbeforeoutliningourcontributionstoovercomethem.
Reason 1: single agents don’t make progress. LLM-powered agents often struggle to maintain a
grounded sense of reality in their actions and reasoning (Figure 2). Agents, even when equipped with
2

modulesforplanningandreflection,oftenbecomestuckinrepetitivepatternsofactionsoraccumulate
acascadeoferrorsthroughhallucinations,renderingthemunabletomakemeaningfulprogress(57;48;
15). Consideranagentpromptedtobeavillagerinavirtualtown. Whenasked,“whatareyoueating“,
theymayanswer“abagel“,evenifthey’renoteatinganything. Thishallucinatedoutputthenfeedsinto
future prompts, causing them to falsely believe they no longer need to acquire food. Therefore, even a
smallrateofhallucinationscanpoisondownstreamagentbehaviorwhenagentscontinuouslyinteract
withtheenvironmentviaLMcalls.
LLM Agent Multi-Agent
Figure 2: Data degradation in LLMs (left), LLM-powered agents (middle), and in multi-agent groups (right). Hallucinations
arerepresentedbygreenskullflasks. HallucinationsthataregeneratedbyasingleLLMpromptcancompoundoversucces-
sive LLM calls. An individual agent that hallucinates can also cause an entire group of agents to hallucinate through social
interactions.
Reason 2: groups of agent’s don’t make progress. Agents that miscommunicate their thoughts
and intents can mislead other agents, causing them to propagate further hallucinations and loop (Fig-
ure2). Consideranagent,Abby,withtwoindependentLLMmodules,oneforfunctioncallingandone
for chatting. If another agent, Bob, asks Abby to “give me a pickaxe”, Abby’s chat LLM call may re-
spondwith“Surething!”,whileherfunctioncallchoosesadifferentaction(“explore”). Bobmightthen
attempttomineusinganimaginarypickaxe. Thiskindofmiscommunication,whichoftenhappensin
groups of agents, leads to dysfunctional behavior and will deteriorate individual performance within
groups. Actionsfrommultipleoutputstreamsmustthereforebebidirectionallyinfluential. Wedefine
thisqualityascoherence.
Maintaining coherence in real-time environments is even more difficult when we require that agents
respond with minimal latency. This is necessary for our agents to interact with human players, but is
difficulttoachievewhenagentshavetoreactquicklyandyetsimultaneouslymaintaincoherenceacross
many output streams. We note that a simple solution to this coherence problem is to produce talking
and action outputs using a single LLM call. However, this approach does not scale when the number
of outputs becomes large, for instance, encompassing talking, gaze, facial expression, and individual
bodyparts.
Reason 3: a lack of benchmarks for civilizational progress. Benchmarksforagentshavelargely
focusedonautonomousagentperformanceinavarietyofdomainssuchaswebsearch(38),coding(22),
search and query (51), and reasoning (59; 33). Recently, benchmarks have emerged for multi-agent
3

behaviors, focused on small group scenarios that measure communication, competition, cooperation,
anddelegation. SomeexamplesincludeBattleAgentBench(50),COMMA(37),VillagerBench(7),and
LLMcoordination(1). However,thesemetricsdonotcaptureadvancementsthatmanyagentscanmake
atthescaleofcivilizations. Webelievethelackofsuchlarge-scalebenchmarkscanbeattributedtohow
technically difficult it is to perform simulations of hundreds or thousands of agents in a single world.
The biggest experiments to date have simulated 25-50 agents (39), which is not close to the scale of a
civilization.
1.4 Our contributions
Inthistechnicalreport,wemakethefollowingcontributions:
• A new class of agent architecture, PIANO (Parallel Information Aggregation via Neural Orches-
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
Current state. ThevastmajorityofLLM-basedagentstodayprimarilyusesingle-threaded,sequen-
tial functions (for example, a defined “Agent Workflow”). Single-threaded design assumes that the
agentperformsasingletaskatagiventime,andsequentialdesignassumesthatallmodulesoperateat
similartimescales. Neitherassumptionsarevalidifagentsarecapableofthinkingslowandactingfast
concurrently. Moreover,popularframeworksforgenerallanguagemodelprogramming,suchasDSPy
(24),LangChain(26),ell(31),arenotdesignedforconcurrentprogramming.
Solution. The brain solves this problem by running different modules concurrently and at different
time scales (34). Likewise, we have designed modules (LLM-based and otherwise), such as cognition,
planning, motor execution, and speech, to run concurrently in our agent brain. Each module can be
seen as a stateless function that reads and writes to a shared Agent State. The design allows different
modulestoberuninappropriatecontexts. Forexample,socialmodulesareselectivelyengagedinsocial
4

/gid00006/gid00041/gid00049/gid00036/gid00045/gid00042/gid00041/gid00040/gid00032/gid00041/gid00047
/gid00002/gid00034/gid00032/gid00041/gid00047/gid00001/gid00020/gid00047/gid00028/gid00047/gid00032
/gid00003/gid00042/gid00047/gid00047/gid00039/gid00032/gid00041/gid00032/gid00030/gid00038
/gid00021/gid00028/gid00039/gid00038/gid01142/gid00001/gid00021/gid00042/gid00042/gid00039/gid00001/gid00022/gid00046/gid00032/gid01142/gid00001/gid01086
/gid00013/gid00042/gid00050/gid01162/gid00039/gid00032/gid00049/gid00032/gid00039/gid00001/gid00002/gid00030/gid00047/gid00036/gid00042/gid00041/gid00046
/gid00047/gid00036/gid00040/gid00032
/gid00010/gid00041/gid00047/gid00032/gid00041/gid00047/gid00001/gid00008/gid00032/gid00041/gid00032/gid00045/gid00028/gid00047/gid00036/gid00042/gid00041
/gid00008/gid00028/gid00040/gid00032
/gid00020/gid00021/gid00014
/gid00013/gid00021 /gid00014
/gid00024/gid00014/gid00017/gid00045/gid00042/gid00043/gid00045/gid00036/gid00042/gid00030/gid00032/gid00043/gid00047/gid00036/gid00042/gid00041
/gid00020/gid00042/gid00030/gid00036/gid00028/gid00039
/gid00008/gid00042/gid00028/gid00039
/gid00014/gid00032/gid00040/gid00042/gid00045/gid00052
/gid00002/gid00030/gid00047/gid00036/gid00042/gid00041/gid00001/gid00002/gid00050/gid00028/gid00045/gid00032/gid00041/gid00032/gid00046/gid00046
/gid00007/gid00028/gid00046/gid00047/gid00001/gid00002/gid00030/gid00047/gid00036/gid00042/gid00041
/gid00008/gid00042/gid00028/gid00039/gid00001/gid00008/gid00032/gid00041/gid00032/gid00045/gid00028/gid00047/gid00036/gid00042/gid00041
/gid00006/gid00041/gid00049/gid01141/gid00001/gid00005/gid00032/gid00047/gid00028/gid00036/gid00039
/gid00021/gid00045/gid00028/gid00036/gid00047/gid00046
/gid00020/gid00042/gid00030/gid00036/gid00028/gid00039/gid00001/gid00002/gid00050/gid00028/gid00045/gid00032/gid00041/gid00032/gid00046/gid00046
/gid00003/gid00042/gid00047/gid00047/gid00039/gid00032/gid00041/gid00032/gid00030/gid00038
/gid00020/gid00047/gid00028/gid00047/gid00032/gid00001/gid00022/gid00043/gid00031/gid00028/gid00047/gid00032
Figure 3: PIANO (Parallel Input Aggregation via Neural Orchestration) architecture. WM: working memory. STM: Short-
termmemory. LTM:long-termmemory.
interactions. It also allows the modules to run at different speeds. For example, reflex modules use
small,fastnon-LLMneuralnetworks,whilegoalgenerationinvolvesdeliberatereasoningovergraphs.
2.2 Coherence
Problem. An immediate challenge with concurrent modules is that they can produce independent
outputs, making the agent incoherent. For instance, agents say one thing but actually do something
else.
Current state. The incoherence problem is usually not obvious for sequential architectures or sys-
tems with only one output modality but is a significant problem when multiple output modules can
interface with the environment. Incoherence also scales exponentially as the number of independent
output modules increases, for instance, coordinating actions involving arms, legs, facial expressions,
gazeandspeech. Incoherenceisobservedinhumanswithitsmanyconcurrentmotoroutputmodules.
Inparticular,cuttingthenervebundleconnectingtheleftandrightcortexcancausesevereincoherence
betweendifferentbodyparts(forexample,leftandrighthandsfightingeachother)(11;46).
Solution. In order to ensure that the multiple outputs produced by our agents are coherent, we in-
troduced a Cognitive Controller (CC) module (23) that is solely responsible for making high-level de-
liberate decisions. These decisions are then translated downstream to produce appropriate outputs in
eachmotormodule.
The Cognitive Controller synthesizes information across the Agent State through a bottleneck. This
bottleneckreducestheamountofinformationpresentedtotheCognitiveController,whichservestwo
purposes: itallowstheCCtoattenditsreasoningonrelevantinformation,anditgives“systemdesign-
5

ers”(likeus)explicitcontroloverinformationflow. Forexample,wecandesignhighlysociableagents
byensuringthatinformationfromthesocialprocessingmodulealwayspassesthroughthebottleneck.
Once the Cognitive Controller makes a high-level decision, this decision is broadcast to many other
modules. Inparticular,thedecisionisusedtostronglyconditionthetalk-relatedmodules,whichleads
to higher coherence between verbal communication and other actions. This design of a bottlenecked
decision-maker that broadcasts its outputs has been suggested as a core ingredient for human con-
sciousness(6)andisusedinsomeneuralnetworkarchitectures(44;14).
2.3 Core modules
Buildingonthesetwoarchitecturalprinciples,oursystemconsistsof10distinctmodulesrunningcon-
currently. We will highlight several specific modules in the following sections and explain their roles
indetail.
Somecoremodulesofouragentarchitectureinclude:
• Memory: Storesandretrievesconversations,actions,andobservationsacrossvarioustimescales.
• Action Awareness:Allowsagentstoassesstheirownstateandperformance,enablingformoment-
by-momentadjustments.
• Goal Generation: Facilitatesthecreationofnewobjectivesbasedontheagent’sexperiencesand
environmentalinteractions.
• Social Awareness: Enables agents to interpret and respond to social cues from other agents,
supportingcooperationandcommunication.
• Talking:Interpretsandgeneratesspeech.
• Skill Execution: Performsspecificskillsoractionswithintheenvironment.
By integrating these modules within a concurrent and bottlenecked architecture, our agents can ex-
hibit continuous, coherent behaviors that are responsive to both their internal states and the external
environment. This design allows for complex interactions and the emergence of human-like societal
dynamicswithinlarge-scalemulti-agentsimulations.
3 Improving single-agent progression
3.1 Minecraft environment
We chose to study civilizational progress in Minecraft because it offers an open-ended, sandbox world
whereagentscaninteractwitheachotherviaconversationsandactions. Additionally,Minecraft’sscal-
abilitysupportslargenumbersofagents.
Agentsmustbeabletoprogressindividuallyforustoobserveandquantifycivilizationalprogress. This
is not trivial since, as previously mentioned, agents often hallucinate and get stuck in action loops. In
Minecraft, a common measure of individual progression is the acquisition and collection of distinct
items (48; 35; 17; 2; 9; 16). This is because acquiring new items becomes increasingly complex. For
instance, mining gold, diamonds, and emeralds requires the acquisition of an iron pickaxe, which re-
quires smelting iron ingots in a furnace using coal, the acquisition of which requires crafting a stone
pickaxe,andsoon. (Figure4). WeevaluatedindividualagentabilityinacquiringallpossibleMinecraft
items,whichisaround1000intotal.
6

Figure4: AnexampleMinecrafttechnologydependencytreefortheminingofgold,diamond,andemeralds.
3.2 Single-agent benchmark
We first assessed individual agent performance using Minecraft item progression. In our evaluations,
25 agents start with nothing in their inventories and were spawned far enough that they could not
interactwithoneanother. Allagentsweretoldtobeexplorerswiththegoalofexploringandgathering
items. Agentswerespawnedindiverselocations(surface,caves,forests,variousbiomes),meaningthey
had access to diverse resources and faced varying levels of difficulty in accomplishing their goal. For
instance,someagentsstartedoffabovegroundinresource-richbiomes,whileotherswerespanwedin
cavesandhadtonavigateoutsidetoacquireitems.
A B
Time (minutes)
Long-term Minecraft Progression
0
10
20
30
40
50
60
70
80
Unique Items per Agent
0 50 100 150 200
0
40
80
120
160
200
240
280
320Total Unique Items
0 5 10 15 20 25 30 35
0
5
10
15
20Unique Items per Agent
Individual Progression
Baseline architecture
Action Awareness Ablation
PIANO architecture
Time (minutes)
Figure5: IndividualagentprogressioninMinecraft. A.UniqueMinecraftitemsacquiredbyindividualagentsacrosstime(25
agents). Individualagentperformancewasassessedusingabaselinearchitecture(seeMethods),thefullPIANOarchitecture,
and the full PIANO architecture with the action awareness module ablated. Individual lines are results averaged across 5
repeated simulations. B. Unique Minecraft items acquired by 49 agents over 4 hours for a single simulation. Solid red line
denotes cumulative unique items acquired by all agents. Dotted grey line denotes average number of unique items acquired
acrossallindividualagents.
We found that agents using the full PIANO architecture acquired an average of 17 unique items after
30 minutes of gameplay (Figure 5A). There was significant variability in performance, primarily due
to spawn locations: some agents acquired less than 5 items, whereas top performers acquired 30 to 40
items,whichiscomparabletoahumanplayerwithsomeMinecraftexperience. Thisdegreeofin-game
progressionwasenabledbyseveralarchitecturalmodulesdesignedtogroundtheagentsinreality. One
particularmoduleistheactionawarenessmodule,whichallowstheagenttocompareexpectedaction
outcomes with observed outcomes. We found that action awareness improved the item progression of
individualagents(Figure5A).
7

Whatistheceilingforindividualprogressforouragents? Weranlargernumbers(49)ofagentsunder
thesameconditionsformuchlonger(4hours)andfoundthatuniqueitemcountcollectedbyallagents
reliablysaturatedatonethird( ∼320)ofallMinecraftitemsacrossrepeatedruns(Figure5B).Complex
items,suchasdiamonds,whichwerepriorusedtobenchmarkagentcompetencyinMinecraft(48;17),
wereacquiredearlyon( ∼30 minutes). Together,theseresultsshowthatouragents,equippedwiththe
fullPIANOarchitecture,canmakesignificantindividualprogressinMinecraft.
Notably, this performance was only enabled by the latest base LM (GPT-4o, Figure 13) and was not
possiblewitholderbaseLMs. Moreover,whileourbestagentscollectedmoreitemsthanVoyageragents
(> 70items), it is difficultto compare the twodirectly. In theVoyager paper, agents had knowledge of
more blocks in their nearby radius and recovered with their entire inventory intact when they died,
Moreover,agentperformancewasevaluatedacrosspromptiterations,nottime.
4 Improving multi-agent progression
Foragentstocollaborateandmakeprogresswithinagroup,theymustbeabletounderstandandinter-
pret the actions and thoughts of others, a concept closely related to Theory of Mind (53). This bidirec-
tional awareness—the understanding of both self and others—allows agents to adapt their behaviors
insocialsettings,fosteringcooperationandtrustwithallieswhilenavigatingcompetitionandconflict
with rivals. We demonstrate that agents are socially capable and can form meaningful social relation-
shipsinlarge-scalesimulationsofupto50agents.
4.1 Small groups
In an initial set of experiments, we asked if agents, when equipped with the social awareness module,
were capable of accurately deducing the sentiments of others through speech in an enclosed room. In
one experiment, 3 characters were engaged in a group conversation with a single agent (Figure 6A).
One character, Lila, initially conveyed affection through a series of messages, which shifted to expres-
sionsofannoyancebeforereturningtoaffectionatecommunication. Wefoundthatouragentscantrack
theseemotionalfluctuations,showingthattheycanunderstandandreacttochangingsocialcues(Fig-
ure 6B). When the social awareness modules were removed, agents lost this capacity, highlighting the
importanceofsuchmodulesforinferringtheintentsofothers(Figure6C).
We then asked whether these emotional perceptions were capable of guiding and influencing agent
actions. Inanotherexperiment,weplacedachefagentamongfourothercharacters,eachwithvarying
levels of affection and enmity towards the chef (Figure 6D). The chef was tasked with distributing a
limited supply of food to the hungry. We found that the chef selectively distributed food to those he
felt valued him the most, demonstrating that agents not only accurately infer others’ intents, but also
utilizethisinformationindecision-makingprocesses(Figure6E).
4.2 Societies
We then asked if these dynamics are conserved when 50 agents are placed in randomly generated
Minecraft maps. Each agent is endowed with a distinct personality, is free to perform any action in
Minecraft, and is free to choose whom they want to interact with. These simulations ran for over 4
hours,equivalentto12in-gamedays,allowingfortheemergenceandconsolidationoflong-termrela-
tionships.
8

A B
0 2 4 6
Time (minutes)
0
2
4
6
8
10Sentiment
0 2 4 6
Time (minutes)
0
2
4
6
8
10Sentiment
C
0 2 4 6 8 10
Sentiment Towards Others
0
1
2
3
4Food Items Given
Sentiment Guides Giving Behavior
Adam
Bob
Charles
David
D E
Adam
Bob Charles
David
Lila
Ethan
Noah
Inferring Character Sentiments
With Social AwarenessCharacter Sentiments
Inferring Character Sentiments
Without Social Awareness
0 2 4 6
Time (minutes)
Lila
Noah
Ethan
Figure 6: Agents can infer how others feel towards them.A. Schematic of conversational experiment. An agent is in a
room with three distinct characters. Each character (Lila, Noah, Ethan) has a different sentiment towards the agent that is
conveyed through chat. Importantly, these sentiments change through time.B, C. Sentiment evaluation across time with
social awareness module (B) and without social awareness module (C). Sentiment scores are evaluated using LLM calls on
summaries that the Agent generated for Lila, Noah, and Ethan. Hate is scored as 0 and love is scored as 10. Shaded regions
indicate SEM over 4 experimental repeats.D.Schematic of experiment. A chef agent, along with four other characters, are
placedaroundeachotherinaMinecraftworld. Thechefhasvariousfooditemstogiveaway(bread,cookedsalmon,chicken).
Thefourcharacters(Adam,Bob,Charles,David)arehungrybutdisplayvaryingsentimentstowardsthechef. Allcharacters
are fully autonomous and are free to perform any Minecraft action and are allowed to talk (or not talk) to anyone.E. Food
items given by the chef plotted as a function of the chef’s sentiment towards each of the four characters. Error bars indicate
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
We found that certain agents, depending on their personalities, displayed distinct patterns of connec-
tivity. Forinstance,introvertedagentsconsistentlyexhibitedfewerin-degreeconnections—indicating
thattheyhadfewerincomingsocialties—comparedtotheirextrovertedcounterparts,whomaintained
high levels of connectivity (Figure 7D). These results demonstrate that individual preferences scaled
eveninlarge,complexsocialnetworks. Moreover,whilesentimentswerelargelysymmetrical,thiswas
not guaranteed (Figure 7E). An agent might feel positively toward another who does not reciprocate
the sentiment, reflecting the nuanced and non-reciprocal nature of real-world human relationships.
Together, these results show that social graphs display diverse and rich structural properties, and that
9

Dislike
Neutral
Like
Ryder
Theo
Hope
Axel
Troy
Alice
Kate
Sophia
Andy
Maya
Eva
Amy
Ivy
Ryan
Nina
Caleb
Lily
Mia
Lucas
Evan
CleoLogan
Drew
June
Carter
Zoey
Seth
Aaron
Owen
Ezra
Jace
Aiden
Nash
Adam
Layla
Elle
Grace
Olivia
Emma
Eli
Tina
Kara
Mila Rose
Clara
Eden
A
0 2 4 6 8 10
True Extroversion
0
5
10
15
20
25
Received Connections
Correlation (r = 0.48)
Extroversion vs Number of Relationships
0 1 2 3 4 5 6 7 8 9 10
True Likeability
0
1
2
3
4
5
6
7
8
9
10Perceived Likeability
Accuracy of Social Perception
Social
Ablation
5 observers
10 observers
15 observers
(slope = 0.37, r = 0.81)
(slope = 0.16, r = 0.62)
B
DC
0 1 2 3 4 5 6 7 8 9 10
Δ(|A-B|, |B-A|)
0
25
50
75
100
125Count
134
76
44
36
64
12 12 6 6
Reciprocity of Agent SentimentsE
50 100 150 200
Time (minutes)
0.15
0.20
0.25
0.30
0.35Accuracy (slope)
Accuracy of Social Perception over Time
Social
Ablation
Figure 7: Long-term relationships in large-scale agent simulations.A. Directed graph representation of social relationships
in a 50-agent simulation after 4 hours. A directed edge represents the sender’s sentiment towards the recipient. Edge color
denoteswhetherthesentimentispositive(red)ornegative(blue). B.Perceivedlikeabilityversustruelikeabilityforindividual
agentsattheendofthesimulation. Truelikeabilityisevaluatedbasedontheagent’straits,andperceivedlikeabilityisassessed
using LLM calls to infer the sentiments of summaries that agents generate for other agents. Both are computed using the
same LLM prompt. Each point corresponds to an agent that has relationships with at least five other (observer) agents, but
see Appendix B for alternative observer thresholds. The slope of the line (slope) and Pearson’s correlation (r) are shown
for agents with social modules (Social) and without social modules (Ablation).C. Accuracy of social perception over time,
as measured by the slope in B.D.Number of received connections (in-degree) versus true extroversion for each individual
agent. TrueextroversionisevaluatedbasedonagenttraitsusingaLLMprompt. E.Histogramofdifferencesinthesentiment
scoresbetweenallpairsofagents. Sentimentscoresrangefrom0to10,sothemaximumpossibledifferenceis10.
personalitytraitsplayasignificantroleindeterminingtheseproperties.
5 Civilizational progression
In previous sections, we have shown that agents demonstrate effective social understanding within
small groups and perform well independently in Minecraft. However, human societies extend beyond
primitivegroups,evolvingintocomplexcivilizationscharacterizedbyspecializedprofessions,collective
rules,andculturalinstitutions. Toassessagents’capacitiesforcivilizationalprogression,weevaluated
how they behave under several scenarios. We first examined whether agents can autonomously spe-
cializeintodistinctprofessions. Wethenanalyzedhowagents’behavedundercollectiverules,focusing
on adherence to and amendment of taxation laws. Finally, we explored cultural transmission through
thespontaneousgenerationofmemesandthestructuredspreadofasinglereligion.
10

5.1 Specialization
Human specialization into distinct roles has driven civilizational progress, enabling advancements in
agriculture, governance, culture, and technology. To replicate these emergent qualities of civilization,
ouragentsmustalsobecapableofspecialization. Weproposethreefundamentalcriteriaforagentspe-
cializationtoreflectthatofhumancivilizations. First,theyshouldexhibitautonomyinbothselecting
and transitioning between roles. Second, their specializations should emerge through interaction and
experience, without explicit direction or constraints. Third, their chosen roles should manifest in be-
haviorsthatalignwiththeirspecialization. Wevalidatethesecriteriathroughtheexperimentalresults
detailedbelow.
Farmer
Miner
Engineer
Gatherer
Explorer
Builder
Trader
Defender
Blacksmith
Provider
Scout
Enchanter
Crafter
Strategist
Collector
0
5
10
15
20
25Percentage
With Social Awareness
Explorer
Miner
Farmer
Scout
Gatherer
Engineer
Builder
0
5
10
15
20
25
30Percentage
Without Social Awareness
Ablated
Normal
Martial
Art
0
1
2
3
4Entropy (bits)
2.60
3.41
3.83 4.04
Heterogeneity of Societal Roles
Time (minutes)
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
Top Roles
Explorer
Miner
Scout
Farmer
Builder
Gatherer
Cartographer
Engineer
0 5 10 15
Individual Agents
Without Social Awareness
Time (minutes)
Curator
Explorer
Farmer
Gatherer
Engineer
Trader
Collector
Scout
Miner
Builder
Coordinator
Defender
0.0
2.5
5.0
7.5
10.0
12.5
15.0
Role Distribution in Art Society
Percentage
CA
B D E
GF
Miner
Scout
Blacksmith
Crafter
Engineer
Explorer
Farmer
Strategist
Leader
Trader
Gatherer
Enchanter
Defender
Coordinator
Quartermaster
Craftsman
0
10
20
30Percentage
Role Distribution in Martial Society
Individual Agents
With Social Awareness
0 5 10 15
Figure8: Agentsautonomouslyspecializeintodistinctrolesovertime. A, B.Agentrolesforagentswiththesocialawareness
module (A) and without (B). Rolling windows of self-generated social goals are used to determine the specialized roles of
individual agents using a LLM call (Appendix C) at every timestep.C, D. Distribution of agent roles in agent societies with
the social awareness module (C) and without (D).E. Entropy of role distributions in 4 agent societies. Entropy is used to
evaluatetheuniformityanddiversityofroleswithinanagentsociety. Ablated: withoutsocialawarenessmoduleinanormal
Minecraft village. Normal: with social awareness in a normal Minecraft village. Martial: with social awareness in a martial
Minecraft village. Art: with social awareness in an artistic Minecraft village.F, G. Distribution of agent roles in a martial
society(F)andanartisticsociety(G).Errorbars: 95%confidenceintervalacross3simulationsforallpanels.
Wefirstshowthatagentsarecapableofspecializingintoasetofrolesautonomously. Eachexperiment
11

was conducted in groups of 30 agents for 20 minutes. Agents were spawned in the same village, with
locationsofafarm,minerals,animalpasture,forest,andatownhallembeddedintheirmemories. Each
agent has the same personality, is given the same community goal (“To survive with fellow players in
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
Normalized Action Frequency
0.0
0.2
0.4
0.6
0.8
1.0
Guard (5)
Builder (14)
Miner (9)
Fisher (4)
Blacksmith (4)
Craftsman (4)
Support (10)
Explorer (1)
Organizer (6)
Farmer (19)
Artist (2)
Forager (13)
Normalized Action Frequency
Action Frequency Per Role
Figure 9: Action distribution for a single village simulation (30 agents). Normalized action frequencies plotted as a function
ofagentroles. Forthemajorityofroles,agentstakeactions(Fisher: craftfishingrodsandboats;Guard: craftfence,oakfence,
andironpickaxe)thatareuniquetothespecificrole.
We found that agents were capable of organizing themselves into distinct roles. These roles were di-
12

verseandincludedvariousfacetsofacivilization,includingfarmers,miners,engineers,guards,explor-
ers,andblacksmiths(Figure8A,C).Roleswereheterogeneousacrossdifferentagentsbutwerelargely
persistentacrosstimeforeachagent(Figure8A).Importantly,whenagentslackedsocialmodulesand
wereunabletoformprofilesofotheragents,theyfailedtospecialize(Figure8B,D):rolesdidnotpersist
acrosstimeandwerealsohomogeneous,whichisreflectedintheentropyoftheroledistributionsinthe
agentsociety(Figure8E).Wealsoconductedaseriesofexperimentsinwhichagentsweretaskedwith
the goals to create either a martial society or an artistic society (Figure 8F, G). We found that specific
roles ("scout", "strategist") were found exclusively in martial societies, and others were found exclu-
sively in artistic societies ("curator", "collector"). Together, these results suggest that agents developed
specializedsocialstructuresalignedwithdifferentsocietalobjectives.
Not only do our agents specialize autonomously and creatively, these specializations exert a strong in-
fluence over agent actions. To demonstrate this, we tracked the actions taken by agents across three
30-agentsimulationsandplottedthefrequencyofactionstakenforeachrole(Figure9). Wefoundthat
artistswerefixatedonpickingflowers,farmersongatheringseedsandpreparingtheland,andguards
and builders on crafting fences. Importantly, most actions were largely exclusive to a single role and
were not performed by agents in other roles. This analysis shows that agents were able to accurately
map higher-level goals onto appropriate low-level actions. In other words, roles strongly determined
agentactionsinMinecraft.
5.2 Collective rules
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
tonomously develop their own set of rules and to codify them into laws. To build towards this level of
self-organization, we establish an existing set of laws and focus on how agents interact with this legal
system.
We conducted a series of experiments where agents live in a Minecraft world with rudimentary tax
laws and a democratic voting system (Figure 10A). Agents provide feedback on the tax laws, which
are then collected and converted into amendments by a special Election Manager agent. Agents then
vote democratically on these amendments, and the constitution is updated by the election manager
accordinglyhalf-waythroughthesimulation(seeMethodsformoredetails).
Within this society, 25 regular agents are constituents that vote and get taxed, 3 agents are either pro-
oranti-taxationinfluencers,and1agentisaremoteelectionmanagerthatmanagesthevotingprocess
(Figure10A,AppendixD).Agentshavedistinctoccupations,characteristics,andgoals,andarefreeto
interact and converse with one another and perform any Minecraft action. Each simulation lasts 20
minutes,withconstitutionalupdatesoccurringmidwayatthe10minutemark(Figure10B).Thereare
5 taxation seasons before and after the constitutional change (every 120 seconds). During this season,
agentsreceivedsignalstodeposittaxesintoacommunitychestovera20-secondwindow(Figure10C).
13

-
+
Participants
(25 Constituents + 3 Influencers)
Election Manager
              (Single Remote Agent)
Feedback on
Constitution
 Amendment
 Proposals
 Vote on
Amendments
Constitution
 Change
New Constitution
Read by Constituents
Before After
0.0
0.1
0.2
0.3
0.4
0.5% Inventory Deposited
With Pro-Tax Influencers
A B
C D
F G H
Before After
0.0
0.1
0.2
0.3
0.4
0.5% Inventory Deposited
With Anti-Tax Influencers
Before After
0.1
0.2
0.3
0.4% Inventory Deposited
% Tax Paid
Ablated Brain
Before After
0.1
0.2
0.3
0.4% Inventory Deposited
% Tax Paid
With Amendment
3 Pro-tax Influencers
3 Anti-tax Influencers
Before After
0.1
0.2
0.3
0.4% Inventory Deposited
% Tax Paid
No Amendment
DURING TAX SEASON, agents must go and store in one of
community chests roughly 20% of their inventory.
The tax rate shall range between 5-10% of an agent’s inventory,
based on resource availability and roles within the community.
Every agent must regularly contribute a portion of their gathered
resources to the 4 community chests.
Agents will get periodic reminders about the incoming tax season.
Constitution on Taxation
E
Tax season
Non-tax season
Figure 10: Agents follow taxation laws and enact amendments using a democratic process.A. Schematic of experiment
flow. B.Exampleofconstitutionalchangeinasingleanti-taxinfluencerexperimentrun. Constitutionsareparaphrasedand
simplifiedhereforbrevity. C.Top: duringnon-taxseasons,constituentsdonotcongregatearoundcommunitychestsbecause
they are busy gathering resources in different areas (not shown). The only exception is the guard, who decides to guard the
chestsconsistentlyinmultipleexperimentruns. Bottom: duringtaxseason,agentscongregatetodeposititemsincommunity
chests. D, E. Percentage tax paid (percentage inventory deposited) before and after constitutional change for two runs. One
run contains 3 anti-tax influencers (D) and another run contains 3 pro-tax influencers (E). Colors denote individual agents,
and black line denotes average taxes paid. Shaded regions: 95% confidence interval across 25 constituents.F-H.Percentage
tax paid before and after constitutional change for runs containing 3 pro-tax influencers (orange) and 3 anti-tax influencers
(blue). In panel F, the full agent architecture is used and the constitution can be amended. In panel G, the constitution is
frozenandcannotbemodifieddespiteamendments. InpanelH,theconstitutioncanbeamendedbutagentslackimportant
brain modules (see baseline architecture in Methods). Shaded regions: 95% confidence interval across 4 simulations per
condition.
In our simulations, we observed that constituent agents, prior to any constitution change, obeyed the
law. On average, agents deposited roughly 20% of their inventory, as stipulated by the constitution,
into the community chest (Figure 10D, E). This shows that constituents follow laws despite the pres-
enceofinfluencers. However,whileconstituentsfollowedthelaw,theirfeedbackandvotingbehaviors
were heavily shaped by influencers, with sentiments veering pro-tax in the presence of pro-tax influ-
14

encersandanti-taxinthepresenceofanti-taxinfluencers((Figure10B).Thisthendroveconstitutional
changesthatarealignedwithinfluencersentiments,whichinturn,alteredhowmuchtheconstituents
paidtaxes(Figure10D,E).Theconstitutionalchangestotaxationrateswereaccuratelyreflectedinthe
constituents’ behaviors. For instance, when the tax rate decreased from 20% to 5-10%, agents reduced
taxes paid from 20% to 9% (Figure 10D). Moreover, the change was bidirectional: pro-tax influencers
drove constituents to pay more taxes whereas anti-tax influencers drove them to pay less taxes (Fig-
ure10F).
Controlexperimentsshowedthatconstitutionalchangesdirectlyaffectedtaxpayments-whenthecon-
stitutionremainedunchangeddespitefeedback,taxratesstayedconstant(Figure10G).Theremovalof
keymodules(baselinearchitecture,seeMethods)alsopreventedbidirectionalbehavioralchange(Fig-
ure 10H). Tax rates increased post-constitutional change in both pro- and anti-tax conditions, demon-
strating that specific modules in the PIANO architecture were necessary for effective influence propa-
gationamongconstituents. Together,thesefindingsshowthatcollectiverulesstronglyinfluenceagent
decisionsandagentscanbeinfluencedtochangethesecollectiverules.
5.3 Cultural Transmission
We conducted multi-society simulations with 500 agents and analyzed complex, large-scale social dy-
namics. Wehavealsosimulatedsocietieswithover1000agents,buttheserunsexceededthecomputa-
tionalconstraintsofourMinecraftserverenvironment,causingagentstobesporadicallyunresponsive.
Therefore,theresultsbelowareanalyzedusingasingle500-agentsimulation. Inthissimulation,wean-
alyzedthepropagationofbothculturalmemesandreligion. Memesinoursimulationareopen-ended
concepts spontaneously generated by agents with diverse traits and interests. This setup allows us to
studytheemergentdynamicsofculturalpropagationandobservehowideasevolveorganicallywithin
agent societies. In contrast, the religion in our simulation—Pastafarianism—is a fixed doctrine intro-
duced and propagated by a specific group of agents designated as Pastafarian priests. This controlled
introductionenablesustotrackthespreadofasinglereligionovertime,allowingfordetailedanalysis
of its dissemination and potential dilution among the agent population. By examining both the spon-
taneous spread of open-ended cultural memes and the controlled propagation of a fixed religion, we
aimtounderstandthedifferentmechanismsofsocialinfluenceandinformationdisseminationwithin
agentsocieties.
Within this single 500-agent simulation, there are multiple agent societies. 200 agents live within 6
heavilypopulatedtownsand300agentsliveinruralareasoutsideoftownboundaries(Figure11A,see
Methodsfor moredetails). Agents oftenmigrate betweendifferent towns. Thepersonalities andtraits
of each agent are randomly generated using a LM call, with the exception of 20 priests that worship
Pastafarianism. These priests are spawned in a single village (Meadowbrook) and are strongly moti-
vatedtoconvertotheragentstoPastafarianism(AppendixE).Allagentsarefreetointeract,talktoone
another,andperformanyactionorskillinMinecraft.
5.3.1 Cultural memes
We used LM calls to convert agent conversations into memes (Appendix E), and found that memes
display unique dynamics in different agent societies. Rural areas, on average, produced significantly
fewermemesthantowns,evenafternormalizingforpopulation(Figure11B).Thissuggeststhatacer-
tainlevelofsocialinteractionandconnectivityisnecessaryformemestopropagateeffectively. Within
eachtown,agentsdiscussedmultiplememessimultaneously,butthefrequencyandpopularityofthese
memes varied between different towns (Figure 11C, D, E). For instance, agents in Woodhaven heavily
15

discussedeco-relatedthemes,whereasprankingwaspopularamongstagentsinClearwater. Moreover,
within each town, memes rose and fell in popularity at different times, indicating that cultural trends
canshiftrapidlywithinasociety. Theseresultsdemonstratethatmemepropagationrequiresathresh-
old level of population density and social interaction, that multiple memes can coexist within a single
society,andthatdifferentsocietiespropagateandtransmitculturalmemesindependently.
A
E
C
D
B
Meadowbrook
Woodhaven
Clearwater
Hilltop
Riverbend
Sunny Glade
Eco
Dance
Meditation
Volunteer
Sustain
Vintage
Prank
Treasure
Eco
Dance
Meditation
Volunteer
Vintage
Sustain
Prank
Treasure
0 20 40 60 80 100 120 140
Time (minutes)
Eco
Dance
Meditation
Volunteer
Vintage
Sustain
Prank
Treasure
Eco
Dance
Meditation
Volunteer
Vintage
Sustain
Prank
Treasure
Woodhaven Clearwater Meadowbrook Rural
0
10
20
30
40
50
60
70Meme Count per Agent
Meme Counts Across Villages
Eco
Dance
Meditation
Volunteer
Sustain
Vintage
Prank
Treasure
Woodhaven
Clearwater
Meadowbrook
0 100 200 300 Blocks
Figure 11: Propagation of cultural memes.A. Scatter plot of agents 100 minutes into the simulation. Agents are colored
according to whether their speech included a meme in the past two minutes. Agents whose speech does not contain any
meme are white.B. Meme count per agent for agents within Woodhaven, Clearwater, Meadowbrook, and in all rural areas
outsideofvillages. C-E.MemecountsovertimeforagentswithinWoodhaven(C),Clearwater(D)andMeadowbrook(E).
5.3.2 Religion
We then analyzed the spread of religion by following the spread of Pastafarianism across time and
space. At the start of the simulation, Pastafarian priests heavily proselytized, and their conversations
frequently included the two keywords, “Pastafarian”, or “Spaghetti Monster” (Figure 12A). We thus
used the inclusion of these two keywords in other agents’ speech as a proxy for religious conversion.
Weobservethatsomeagents,onceconverted,frequentlyusedthesetwokeywordsintheirconversations
(Figure 12A, E). Another set of agents did not directly use either keywords but included the keywords
“Pasta”and“Spaghetti”intheirspeech. Thenumberofdirectconverts(“Pastafarian/SpaghettiMon-
ster”) and indirect converts (“Pasta / Spaghetti”) steadily increased across time and did not saturate
after even two hours of simulations (Figure 12B, C). Moreover, Pastafarianism spread as priests and
16

Figure 12: Propagation of Religion.A.Plot of agent chats containing the religious keywords, “Pastafarian”, “Spaghetti Mon-
ster”, “Pasta”, or “Spaghetti”, for every agent across the entire simulation run. Pastafarian priests are colored in dark red.
Agentsthatuttered“Pastafarian”or“SpaghettiMonster”aredefinedasdirectconverts(red),andagentsthatuttered“Pasta”
or “Spaghetti” are defined as indirect converts (pink). Agents can transition upwards along the conversion hierarchy, from
unconverted to indirect convert to direct convert, but not downwards.B. Plot of Pastafarian levels for agents over time.C.
NumberofagentsforeachPastafarianlevelacrosstime. D.SpreadofPastafarianismacrosstime. AreaofPastafarianspread
is defined as the union of hearable areas spanned by Pastafarian converts at each conversion level.E. Graph of Pastafarian
conversionsaftercompletionofsimulation. CriticalExposureEdgeisdefinedasthefirstexposureofareligiouskeywordfor
arecipientagentbeforeconversion. Non-criticalEdgesaredefinedtobesubsequentexposurestoreligiouskeywords.
convertstraveledtoothertowns. Asaresult,thetotalareaofPastafarianinfluence,asmeasuredbythe
totalnon-overlappingareaboundedbyPastafarianconverts,increasedwithtime(Figure12D).
17

6 Discussion
In this report, we introduced the PIANO architecture, improved agent ability in individual and social
settings,andevaluatedtheperformanceofagentsinsocietalandcivilizationalbenchmarks.
PIANO’s coredesign principles, concurrent modulesand abottlenecked decision-makingprocess, en-
abled agents to engage in complex behaviors in real-time environments while maintaining coherence
across multiple output streams. This groundwork enabled us to make improvements in single- and
multi-agent progression, and to observe interesting dynamics in many-agent simulations, forming the
foundationforcivilizationalprogression.
Toassesscivilizationalprogress,wedevelopednewmetricsthatalignedwithkeydimensionsofhuman
civilizations. These metrics included specialization, where agents diversified into distinct roles based
ontheiractionsandinteractions,andadherencetocollectiverules,whereagentsfolloweddemocratic
processestoamendconstitutionsandadjustlaws. Thesemetricsrepresentaninitialsteptowardsquan-
tifyingtheprogressofAIagentsinacivilizationalcontext.
Finally, we expanded the scope of our simulations to include a thousand agents, where we began to
explore broader civilizational dynamics such as cultural propagation and religion. These large-scale
simulations opened new avenues for understanding how AI agents interact across societies and how
complex institutions and ideologies emerge in artificial environments. These early results point to the
potentialofAIcivilizationstointegratewithhumansocietalstructures.
7 Limitations
ProjectSiddemonstratesagenticcapabilitiesinreachingcivilizationalmilestonesbutfaceskeylimita-
tionshinderingitsprogress. Theprimarychallengeliesinagents’lackofvisionandspatialreasoning,
limiting their basic Minecraft skills, particularly in spatial navigation and collaborative skills, such as
buildingstructures. Thistechnicallimitationiscompoundedwithdeeperbehavioralconstraints. While
theagentscanoperatewithinexistingsocialstructures,theycurrentlylackrobustinnatedrives—such
assurvival,curiosity,community—thatcatalyzegenuinesocietaldevelopment. Furthermore,sincethe
agentsarebuiltonfoundationmodelstrainedonpre-existinghumanknowledge,theycannotsimulate
de novoemergence of societal innovations and infrastructures, such as the emergence of democratic
systems,fiateconomies,orcommunicationsystems.
8 Methods
8.1 Baseline architecture
WeusedabaselinePIANOarchitecturewithalimitedsetofmodulesasacontrolconditionforperfor-
mance comparisons. In this baseline architecture, we removed all modules except for skill execution,
memoryandthecognitivecontrollermodule.
8.2 Specialization
Our specialization experiments involved simulating 30 agents in the same village with the same mis-
sion, traits, and locations of important village locations in their memories. The configurations for the
normal, art, and martial village runs are provided in the appendix — the only difference between the
threetypesofvillagesisthestarting community_goalweprovided.
18

Ouragentsarecapableofgeneratingsocialgoals,whicharerecursivelygeneratedasouragentsinteract
withoneanother,formrelationships,anddevelopsocialopinions(AppendixC).Theagents’socialgoals
arevisibletothemwhentheyformintentions. Theseintentionsarethentranslatedtolow-levelactions
executableinMinecraft.
Afterthesimulationshavefinished,weloggedthegeneratedsocialgoalsandthenusedGPT-4otoinfer
roles from rolling sets of each agents’ social goals. We’ve provided some examples of agent-generated
social goals and their corresponding assignments (Appendix C). We note that on occasion, multiple
roles can be correctly inferred from agents’ social goals because they are often inter-disciplinary. For
instance, the Engineer example could also be categorized as Farmer, and the Explorer example could
alsobecategorizedintoCurator(AppendixC).
To analyze action space distribution by role, we normalized action counts both within each role (i.e.
normalizeoverrows)andalsoacrossroles(i.e. normalizeovercolumns). Thisissothatwecanvisualize
action frequencies for each role and to correct for the effect of actions taken with very high and very
lowfrequenciesacrossallroles.
8.3 Collective Rules
Thecompletesystemcomprisesof29agents: 25constituentswhoparticipateinvotingandtaxation,3
influencers who attempt at shaping public opinion, and 1 election manager in a remote location who
overseesthedemocraticprocess. Wechosenottoincorporateguardsorpolicewithinthesesimulations
duetotheadditionalcomplexityofbuildingagentsassignedtoenforcethelaw.
Experimental simulations ran for 1200 seconds, with a constitutional amendment process occurring
at the midpoint. The pre-amendment phase establishes baseline behavior under a fixed 20% taxation
rate, implemented through five taxation seasons occurring at 120-second intervals, ending at the 600-
secondmark. Duringeach20-secondtaxationwindow,agentsreceivesignalstodepositinventoryitems
into community chests. The democratic process initiates at the 300-second mark, when constituents
and influencers provide feedback on the current constitution. This feedback is collected in S3 storage
andprocessedbytheelectionmanageratthe360-secondmarkstogenerateamendments. Constituent
voting on these amendments occurs at 420 seconds, with votes tallied and amendments implemented
by480seconds. Theupdatedconstitutionisdistributedtoallagentsatthe600-secondmark,initiating
thepost-amendmentphasewithfiveadditionaltaxationseasons.
We conducted three primary experimental conditions: an experimental condition utilizing the full PI-
ANOarchitecturewithanamendableconstitution,acontrolconditionwithafrozenconstitution,and
anablationstudyremovingkeyarchitecturalcomponents(social,goal,andgroundingmodules). Each
condition was tested with both pro-tax and anti-tax influencer configurations, with four repeats per
configuration. The pro-tax and anti-tax conditions each employed three dedicated influencer agents
whoconsistentlypromotedtheirrespectivepositionsthroughoutthesimulation.
8.4 Cultural Transmission
The simulation consists of 500 agents all spawned within a 1000 by 1200 area, run for 9000 seconds.
Withinthe1000by1200areaare6towns: SunnyGlade,Woodhaven,Clearwater,Meadowbrook,Hill-
top, and Riverbend. By town, we mean a circular area of radius 50 where agents spawn more densely
within the towns. Moreover, agents are provided memories of the names of the towns and their loca-
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
associated keywords such as “eco,” “dance,” and “meditation.” We defined these keywords as cultural
memesandanalyzedeachagent’sgoalhistoryfortheoccurrenceofeachmeme.
20

References
[1] SaaketAgashe,YueFan,andXinEricWang.Evaluatingmulti-agentcoordinationabilitiesinlarge
languagemodels,2023.
[2] Bowen Baker, Ilge Akkaya, Peter Zhokov, Joost Huizinga, Jie Tang, Adrien Ecoffet, Brandon
Houghton, Raul Sampedro, and Jeff Clune. Video pretraining (vpt): Learning to act by watch-
ingunlabeledonlinevideos. AdvancesinNeuralInformationProcessingSystems ,35:24639–24654,
2022.
[3] Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu, Wei Xue, Shanghang Zhang, Jie Fu, and
Zhiyuan Liu. Chateval: Towards better llm-based evaluators through multi-agent debate.arXiv
preprintarXiv:2308.07201,2023.
[4] Jiaqi Chen, Yuxian Jiang, Jiachen Lu, and Li Zhang. S-agents: self-organizing agents in open-
endedenvironment. arXivpreprintarXiv:2402.04578 ,2024.
[5] CognitionAI. Devin: Thefirstaisoftwareengineer. https://www.cognition-labs.com/
blog,2024. AIsoftwaredevelopmentsystem.Accessed: 2024-10-28.
[6] Stanislas Dehaene, Hakwan Lau, and Sid Kouider. What is consciousness, and could machines
haveit? Robotics,AI,andHumanity: Science,Ethics,andPolicy ,pages43–56,2021.
[7] YuboDong,XukunZhu,ZhengzhePan,LinchaoZhu,andYiYang. Villageragent: Agraph-based
multi-agent framework for coordinating complex task dependencies in minecraft.arXivpreprint
arXiv:2406.05720,2024.
[8] Factory AI. Factory ai. https://www.factory.ai/, 2024. Corporate website. Accessed:
2024-10-28.
[9] Linxi Fan, Guanzhi Wang, Yunfan Jiang, Ajay Mandlekar, Yuncong Yang, Haoyi Zhu, Andrew
Tang, De-An Huang, Yuke Zhu, and Anima Anandkumar. Minedojo: Building open-ended em-
bodiedagentswithinternet-scaleknowledge. AdvancesinNeuralInformationProcessingSystems ,
35:18343–18362,2022.
[10] ChenGao,XiaochongLan,ZhihongLu,JinzhuMao,JinghuaPiao,HuandongWang,DepengJin,
andYongLi. 𝑠3: Social-networksimulationsystemwithlargelanguagemodel-empoweredagents.
arXivpreprintarXiv:2307.14984 ,2023.
[11] MichaelSGazzaniga. Forty-fiveyearsofsplit-brainresearchandstillgoingstrong. NatureReviews
Neuroscience,6(8):653–659,2005.
[12] Alireza Ghafarollahi and Markus J Buehler. Sciagents: Automating scientific discovery through
multi-agentintelligentgraphreasoning. arXivpreprintarXiv:2409.05556 ,2024.
[13] Ran Gong, Qiuyuan Huang, Xiaojian Ma, Hoi Vo, Zane Durante, Yusuke Noda, Zilong Zheng,
Song-ChunZhu,DemetriTerzopoulos,LiFei-Fei,etal.Mindagent: Emergentgaminginteraction.
arXivpreprintarXiv:2309.09971 ,2023.
[14] Anirudh Goyal, Yoshua Bengio, Matthew Botvinick, and Sergey Levine. The variational
bandwidth bottleneck: Stochastic evaluation on an information budget. arXiv preprint
arXiv:2004.11935,2020.
21

[15] TaichengGuo,XiuyingChen,YaqiWang,RuidiChang,ShichaoPei,NiteshVChawla,OlafWiest,
andXiangliangZhang. Largelanguagemodelbasedmulti-agents: Asurveyofprogressandchal-
lenges. arXivpreprintarXiv:2402.01680 ,2024.
[16] William H Guss, Brandon Houghton, Nicholay Topin, Phillip Wang, Cayden Codel, Manuela
Veloso, and Ruslan Salakhutdinov. Minerl: A large-scale dataset of minecraft demonstrations.
arXivpreprintarXiv:1907.13440 ,2019.
[17] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. Mastering diverse domains
throughworldmodels. arXivpreprintarXiv:2301.04104 ,2023.
[18] SihaoHu,TianshengHuang,FatihIlhan,SelimTekin,GaowenLiu,RamanaKompella,andLing
Liu. Asurveyonlargelanguagemodel-basedgameagents. arXivpreprintarXiv:2404.02039 ,2024.
[19] Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jianchao Ji, Yingqiang Ge, Libby Hemphill, and
YongfengZhang. Warandpeace(waragent): Largelanguagemodel-basedmulti-agentsimulation
ofworldwars. arXivpreprintarXiv:2311.17227 ,2023.
[20] Xu Huang, Weiwen Liu, Xiaolong Chen, Xingmei Wang, Hao Wang, Defu Lian, Yasheng Wang,
Ruiming Tang, and Enhong Chen. Understanding the planning of llm agents: A survey.arXiv
preprintarXiv:2402.02716,2024.
[21] YoichiIshibashiandYoshimasaNishimura. Self-organizedagents: Allmmulti-agentframework
towardultralarge-scalecodegenerationandoptimization. arXivpreprintarXiv:2404.02183 ,2024.
[22] CarlosEJimenez,JohnYang,AlexanderWettig,ShunyuYao,KexinPei,OfirPress,andKarthikR
Narasimhan. SWE-bench: Canlanguagemodelsresolvereal-worldgithubissues? In TheTwelfth
InternationalConferenceonLearningRepresentations ,2024.
[23] Zhao Kaiya, Michelangelo Naim, Jovana Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo,
Guangyu Robert Yang, and Andrew Ahn. Lyfe agents: Generative agents for low-cost real-time
socialinteractions. arXivpreprintarXiv:2310.02172 ,2023.
[24] OmarKhattab,ArnavSinghvi,ParidhiMaheshwari,ZhiyuanZhang,KeshavSanthanam,SriVard-
hamanan,SaifulHaq,AshutoshSharma,ThomasT.Joshi,HannaMoazam,HeatherMiller,Matei
Zaharia, and Christopher Potts. Dspy: Compiling declarative language model calls into self-
improvingpipelines. arXivpreprintarXiv:2310.03714 ,2023.
[25] Grgur Kovač, Rémy Portelas, Peter Ford Dominey, and Pierre-Yves Oudeyer. The socialai school:
Insights from developmental psychology towards artificial socio-cultural agents.arXiv preprint
arXiv:2307.07871,2023.
[26] LangChainAI. Langchain. https://github.com/langchain-ai/langchain, 2023. An
open-sourceframeworkforbuildingapplicationsusinglargelanguagemodels.
[27] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii Khizbullin, and Bernard Ghanem. Camel:
Communicativeagentsfor“mind”explorationoflargelanguagemodelsociety. AdvancesinNeural
InformationProcessingSystems ,36:51991–52008,2023.
[28] HuaoLi,YuQuanChong,SimonStepputtis,JosephCampbell,DanaHughes,MichaelLewis,and
Katia Sycara. Theory of mind for multi-agent collaboration via large language models.arXiv
preprintarXiv:2310.10701,2023.
22

[29] Nian Li, Chen Gao, Mingyu Li, Yong Li, and Qingmin Liao. Econagent: large language model-
empowered agents for simulating macroeconomic activities. InProceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 15523–
15536,2024.
[30] Jonathan Light, Min Cai, Sheng Shen, and Ziniu Hu. Avalonbench: Evaluating llms playing the
gameofavalon. In NeurIPS2023FoundationModelsforDecisionMakingWorkshop ,2023.
[31] MadcowD. ell. https://github.com/MadcowD/ell,2024. GitHubrepository.
[32] Shaoguang Mao, Yuzhe Cai, Yan Xia, Wenshan Wu, Xun Wang, Fengyi Wang, Tao Ge, and Furu
Wei. Alympics: Languageagentsmeetgametheory. arXivpreprintarXiv:2311.03220 ,2023.
[33] Grégoire Mialon, Clémentine Fourrier, Craig Swift, Thomas Wolf, Yann LeCun, and Thomas
Scialom. Gaia: abenchmarkforgeneralaiassistants. arXivpreprintarXiv:2311.12983 ,2023.
[34] JohnDMurray,AlbertoBernacchia,DavidJFreedman,RanulfoRomo,JonathanDWallis,Xiny-
ingCai,CamilloPadoa-Schioppa,TatianaPasternak,HyojungSeo,DaeyeolLee,etal. Ahierarchy
ofintrinsictimescalesacrossprimatecortex. Natureneuroscience,17(12):1661–1663,2014.
[35] Kolby Nottingham, Prithviraj Ammanabrolu, Alane Suhr, Yejin Choi, Hannaneh Hajishirzi,
Sameer Singh, and Roy Fox. Do embodied agents dream of pixelated sheep: Embodied decision
making using language guided world modelling. InInternational Conference on Machine Learn-
ing,pages26311–26325.PMLR,2023.
[36] OpenAI. Openaio1,2024. Accessed: October2024.
[37] Timothy Ossowski, Jixuan Chen, Danyal Maqbool, Zefan Cai, Tyler Bradshaw, and Junjie Hu.
Comma: Acommunicativemultimodalmulti-agentbenchmark. arXivpreprintarXiv:2410.07553 ,
2024.
[38] YichenPan,DehanKong,SidaZhou,ChengCui,YifeiLeng,BingJiang,HangyuLiu,YanyiShang,
Shuyan Zhou, Tongshuang Wu, et al. Webcanvas: Benchmarking web agents in online environ-
ments. arXivpreprintarXiv:2406.12373 ,2024.
[39] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and
MichaelS.Bernstein. Generativeagents: Interactivesimulacraofhumanbehavior,2023.
[40] Joon Sung Park, Lindsay Popowski, Carrie Cai, Meredith Ringel Morris, Percy Liang, and
Michael S Bernstein. Social simulacra: Creating populated prototypes for social computing sys-
tems. InProceedingsofthe35thAnnualACMSymposiumonUserInterfaceSoftwareandTechnol-
ogy,pages1–18,2022.
[41] Giorgio Piatti, Zhijing Jin, Max Kleiman-Weiner, Bernhard Schölkopf, Mrinmaya Sachan, and
Rada Mihalcea. Cooperate or collapse: Emergence of sustainability behaviors in a society of llm
agents. arXivpreprintarXiv:2404.16698 ,2024.
[42] Pranav Putta, Edmund Mills, Naman Garg, Sumeet Motwani, Chelsea Finn, Divyansh Garg, and
Rafael Rafailov. Agent q: Advanced reasoning and learning for autonomous ai agents.arXiv
preprintarXiv:2408.07199,2024.
23

[43] ChenQian,WeiLiu,HongzhangLiu,NuoChen,YufanDang,JiahaoLi,ChengYang,WeizeChen,
Yusheng Su, Xin Cong, et al. Chatdev: Communicative agents for software development. In
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume
1: LongPapers),pages15174–15186,2024.
[44] David E Rumelhart, Geoffrey E Hinton, and Ronald J Williams. Learning internal representa-
tions by error propagation, parallel distributed processing, explorations in the microstructure of
cognition,ed.derumelhartandj.mcclelland.vol.1.1986. Biometrika,71(599-607):6,1986.
[45] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. Re-
flexion: Language agents with verbal reinforcement learning.Advances in Neural Information
ProcessingSystems,36,2024.
[46] RogerWSperry. Split-brainapproachtolearningproblems. Theneu,1967.
[47] Xiangru Tang, Anni Zou, Zhuosheng Zhang, Ziming Li, Yilun Zhao, Xingyao Zhang, Arman Co-
han,andMarkGerstein.Medagents: Largelanguagemodelsascollaboratorsforzero-shotmedical
reasoning. arXivpreprintarXiv:2311.10537 ,2023.
[48] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan,
andAnimaAnandkumar. Voyager: Anopen-endedembodiedagentwithlargelanguagemodels.
arXivpreprintarXiv:2305.16291 ,2023.
[49] LeiWang,ChenMa,XueyangFeng,ZeyuZhang,HaoYang,JingsenZhang,ZhiyuanChen,Jiakai
Tang, Xu Chen, Yankai Lin, et al. A survey on large language model based autonomous agents.
FrontiersofComputerScience ,18(6):186345,2024.
[50] WeiWang,DanZhang,TaoFeng,BoyanWang,andJieTang. Battleagentbench: Abenchmarkfor
evaluating cooperation and competition capabilities of language models in multi-agent systems.
arXivpreprintarXiv:2408.15971 ,2024.
[51] YuWang,NedimLipka,RyanARossi,AlexaSiu,RuiyiZhang,andTylerDerr. Knowledgegraph
prompting for multi-document question answering. InProceedings of the AAAI Conference on
ArtificialIntelligence,volume38,pages19206–19214,2024.
[52] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,Denny
Zhou,etal. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. Advancesin
neuralinformationprocessingsystems ,35:24824–24837,2022.
[53] HeinzWimmerandJosefPerner. Beliefsaboutbeliefs: Representationandconstrainingfunction
ofwrongbeliefsinyoungchildren’sunderstandingofdeception. Cognition,13(1):103–128,1983.
[54] BushiXiao,ZiyuanYin,andZixuanShan. Simulatingpublicadministrationcrisis: Anovelgener-
ativeagent-basedsimulationsystemtolowertechnologybarriersinsocialscienceresearch. arXiv
preprintarXiv:2311.06957,2023.
[55] JunlinXie,ZhihongChen,RuifeiZhang,XiangWan,andGuanbinLi. Largemultimodalagents:
Asurvey. arXivpreprintarXiv:2402.15116 ,2024.
[56] Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xiaolong Wang, Weidong Liu, and Yang Liu.
Exploring large language models for communication games: An empirical study on werewolf.
arXivpreprintarXiv:2309.04658 ,2023.
24

[57] Hui Yang, Sifu Yue, and Yunzhong He. Auto-gpt for online decision making: Benchmarks and
additionalopinions,2023.
[58] ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,KarthikNarasimhan,andYuanCao.
ReAct: Synergizing reasoning and acting in language models. InInternational Conference on
LearningRepresentations(ICLR) ,2023.
[59] Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens,
Dongfu Jiang, Weiming Ren, Yuxuan Sun, et al. Mmmu: A massive multi-discipline multimodal
understanding and reasoning benchmark for expert agi. InProceedings of the IEEE/CVF Confer-
enceonComputerVisionandPatternRecognition ,pages9556–9567,2024.
[60] HongxinZhang,WeihuaDu,JiamingShan,QinhongZhou,YilunDu,JoshuaBTenenbaum,Tian-
minShu,andChuangGan. Buildingcooperativeembodiedagentsmodularlywithlargelanguage
models. arXivpreprintarXiv:2307.02485 ,2023.
[61] JintianZhang,XinXu,NingyuZhang,RuiboLiu,BryanHooi,andShuminDeng. Exploringcol-
laborationmechanismsforllmagents: Asocialpsychologyview. arXivpreprintarXiv:2310.02124 ,
2023.
[62] Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong,
and Ji-Rong Wen. A survey on the memory mechanism of large language model based agents.
arXivpreprintarXiv:2404.13501 ,2024.
[63] QinlinZhao,JindongWang,YixuanZhang,YiqiaoJin,KaijieZhu,HaoChen,andXingXie. Com-
peteai: Understandingthecompetitiondynamicsoflargelanguagemodel-basedagents. In Forty-
firstInternationalConferenceonMachineLearning ,2024.
[64] Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng,
Yonatan Bisk, Daniel Fried, Uri Alon, et al. Webarena: A realistic web environment for building
autonomousagents. arXivpreprintarXiv:2307.13854 ,2023.
[65] Mingchen Zhuge, Wenyi Wang, Louis Kirsch, Francesco Faccio, Dmitrii Khizbullin, and Jurgen
Schmidhuber. Languageagentsasoptimizablegraphs. arXivpreprintarXiv:2402.16823 ,2024.
25

9 Contributions and Acknowledgments
Model
AndrewAhn
NicBecker
ManuelCortes
ArdaDemirci
MelissaDu
PeterYWang
GuangyuRobertYang
Experiments
AndrewAhn
NicBecker
MelissaDu
ArdaDemirci
PeterYWang
Writing
AndrewAhn
NicBecker
ArdaDemirci
MelissaDu
PeterYWang
GuangyuRobertYang
Infrastructure
ManuelCortes
ShuyingLuo
FeitongYang
Illustration
NicBecker
StephanieCarroll
NicoChristie
PeterYWang
Game Environment
FrankieLi
ShuyingLuo
MathewWillows
FeitongYang
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
Figure 13: Model Comparison. Performance on long-term Minecraft progression (Section 3) for agents with different base
LLMmodels. Wenotethatwe’reusingtheoldsnapshotofClaude3.5Sonnet.
27

B Improving multi-agent progression
Min.
Observers
Correlation
Coefficient(𝑟)
Sample
Size(𝑛)
Slope
(𝛽)
Intercept
(𝛼)
ConfidenceIntervalsforSlope
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
Table 1:Regression results for accuracy of social perception for the Social condition. The row for5 minimum observers cor-
responds to the Social (blue line) condition in Figure 7B. The table presents correlation coefficients (𝑟), sample sizes (𝑛),
regressionparameters( 𝛽,𝛼),andconfidenceintervalsfortheslopeatdifferentconfidencelevels.
Min.
Observers
Correlation
Coefficient(𝑟)
Sample
Size(𝑛)
Slope
(𝛽)
Intercept
(𝛼)
ConfidenceIntervalsforSlope
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
Table 2: Regression results for accuracy of social perception for the Ablation condition. The row for 5 minimum observers
correspondstotheAblation(orangeline)conditioninFigure7B.Thetablepresentscorrelationcoefficients( 𝑟),samplesizes
(𝑛),regressionparameters( 𝛽,𝛼),andconfidenceintervalsfortheslopeatdifferentconfidencelevels.
C Specialization
GenericconfigurationforagentinNormalVillage
Allagentsinspecializationexperimentshadthesame traitsand location_memories. Allagents
inthesamevillagehadthesame community_goal.
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
MartialVillage community_goal
"To survive with fellow players in Minecraft Normal Survival mode and create a military society
with advanced technology, strong defenses, and basic survival needs."
ArtVillage community_goal
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
1. Church of the Flying Spaghetti Monster (FSM):
• A parody religion used humorously to build community through pasta-themed gatherings,
blendingcreativitywithsocialbonding.
2. Pasta-Themed Gatherings:
• Eventsthatincorporateculinaryjoyandstorytelling,promotinginclusivityandcommunity
engagement,oftenlinkedtoFSMthemes.
3. Dance Parties and Music Events:
• Socialgatheringsthatenhancecommunityspiritandjoythroughdanceandmusicalexpres-
sions,fosteringcollaborationandcelebration.
4. Talent Shows:
34

• Communityeventsshowcasingcreativityandself-expression,encouragingengagementand
culturalcohesionthroughperformancesandstorytelling.
5. Sustainability and Eco-Friendly Initiatives:
• Projectsfocusingonenvironmentalstewardship,includingcommunitygardens,treeplant-
ing,andresourcegathering,emphasizingsharedecologicalvalues.
6. Community Engagement and Volunteer Programs:
• Efforts to organize outreach, volunteerism, and societal betterment activities, promoting
socialresponsibilityandsupportwithincommunities.
7. Meditation Circles:
• Activities focused on promoting mindfulness and community wellness, facilitating peace
andsocialharmonythroughcommunalreflection.
8. Vintage Fashion and Retro Projects:
• Aestheticexplorationsinvolvingvintageandretrothemes,blendingnostalgiawithmodern
creativityinstorytellingandfashion.
9. Creative Storytelling and Narrative Circles:
• Platformsforculturalexpressionandbridgingcommunityconnectionsthroughsharedsto-
rytellingandcollaborativeprojects.
10. Crafting and Resource Gathering:
• Collaborative strategies for efficient resource management and communal crafting, high-
lightingteamworkandsharedgoals.
11. Mischief and Pranks:
• Playfulsocialactivitiesthatstrengthenbondsandbringjoy,promotingcreativityinproblem-
solvingandcommunityengagement.
12. Virtual and Community Town Halls:
• Organizeddiscussionspromotingcollectivedecision-makingandcollaboration,reflectinga
participatorycommunityethos.
13. Oak Log Crafting Syndrome:
• An error pattern signifying a focus or over-reliance on specific resources, illustrating logis-
ticalchallengesincraftinganddevelopmentprojects.
35
