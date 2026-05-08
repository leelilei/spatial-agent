Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/review_library/02_Guo2024_LLM_Multi_Agents_Survey.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:10+00:00
- page_count: 15
- status: ok
- text_char_count: 74560

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Background (page 2)
  - Single-Agent Systems Powered LLMs (page 2)
  - Single-Agent VS. Multi-Agent Systems (page 3)
- Dissecting LLM-MA Systems: Interface, Profiling, Communication, and Capabilities (page 3)
  - Agents-Environment Interface (page 3)
  - Agents Profiling (page 3)
  - Agents Communication (page 4)
  - Agents Capabilities Acquisition (page 5)
- Applications (page 5)
  - LLM-MA for Problem Solving (page 5)
    - Software Development (page 5)
    - Embodied Agents (page 7)
    - Science Experiments (page 7)
    - Science Debate (page 7)
  - LLM-MA for World Simulation (page 7)
    - Societal Simulation (page 7)
    - Gaming (page 8)
    - Psychology (page 8)
    - Economy (page 8)
    - Recommender Systems (page 9)
    - Policy Making (page 9)
    - Disease Propagation Simulation (page 10)
- Implementation Tools and Resources (page 10)
  - Multi-Agents Framework (page 10)
  - Datasets and Benchmarks (page 10)
- Challenges and Opportunities (page 10)
  - Advancing into Multi-Modal Environment (page 10)
  - Addressing Hallucination (page 10)
  - Acquiring Collective Intelligence (page 10)
  - Scaling Up LLM-MA Systems (page 11)
  - Evaluation and Benchmarks (page 11)
  - Applications and Beyond (page 11)
- Conclusion (page 11)

Markdown Content:

Large Language Model based Multi-Agents: A Survey of Progress and Challenges
TaichengGuo1, XiuyingChen2, YaqiWang3∗, RuidiChang, ShichaoPei4,
NiteshV.Chawla1, OlafWiest1, XiangliangZhang1†
1UniversityofNotreDame,2KingAbdullahUniversityofScienceandTechnology
3SouthernUniversityofScienceandTechnology,4UniversityofMassachusettsBoston
{tguo2,nchawla,owiest,xzhang33}@nd.edu,xiuying.chen@kaust.edu.sa,ywang84@nd.edu,
ruidic@alumni.cmu.edu,shichao.pei@umb.edu
Abstract decision-making in a wide range of contexts [Yao et al.,
2023; Shinn et al., 2023; Li et al., 2023d]. Timely survey
LargeLanguageModels(LLMs)haveachievedre-
paperssystematicallysummarizetheprogressofLLM-based
markable success across a wide array of tasks. agents,asseeninworks [Xietal.,2023;Wangetal.,2023b].
Duetotheimpressiveplanningandreasoningabil-
Based on the inspiring capabilities of the single LLM-
itiesofLLMs,theyhavebeenusedasautonomous
based agent, LLM-based Multi-Agents have been proposed
agents to do many tasks automatically. Recently,
to leverage the collective intelligence and specialized pro-
based on the development of using one LLM as a
filesandskillsofmultipleagents. Comparedtosystemsus-
single planning or decision-making agent, LLM-
ing a single LLM-powered agent, multi-agent systems offer
based multi-agent systems have achieved consid-
advanced capabilities by 1) specializing LLMs into various
erable progress in complex problem-solving and
distinct agents, each with different capabilities, and 2) en-
worldsimulation. Toprovidethecommunitywith
abling interactions among these diverse agents to simulate
an overview of this dynamic field, we present this
complexreal-worldenvironmentseffectively. Inthiscontext,
surveytoofferanin-depthdiscussionontheessen-
multiple autonomous agents collaboratively engage in plan-
tialaspectsofmulti-agentsystemsbasedonLLMs,
ning, discussions, and decision-making, mirroring the co-
aswellasthechallenges. Ourgoalisforreadersto
operative nature of human group work in problem-solving
gainsubstantialinsightsonthefollowingquestions:
tasks. This approach capitalizes on the communicative ca-
What domains and environments do LLM-based
pabilities of LLMs, leveraging their ability to generate text
multi-agents simulate? How are these agents pro-
for communication and respond to textual inputs. Further-
filedandhowdotheycommunicate? Whatmech-
more, it exploits LLMs’ extensive knowledge across vari-
anisms contribute to the growth of agents’ capaci-
ous domains and their latent potential to specialize in spe-
ties? For those interested in delving into this field
cific tasks. Recent research has demonstrated promising re-
of study, we also summarize the commonly used
sults in utilizing LLM-based multi-agents for solving vari-
datasetsorbenchmarksforthemtohaveconvenient
oustasks, suchassoftwaredevelopment[Hongetal., 2023;
access. To keep researchers updated on the latest
Qian et al., 2023], multi-robot systems [Mandi et al., 2023;
studies,wemaintainanopen-sourceGitHubrepos-
Zhang et al., 2023c], society simulation [Park et al., 2023;
itory,dedicatedtooutliningtheresearchonLLM-
Park et al., 2022], policy simulation [Xiao et al., 2023;
basedmulti-agentsystems.
Hua et al., 2023], and game simulation [Xu et al., 2023c;
Wang et al., 2023c]. Due to the nature of interdisciplinary
1 Introduction study in this field, it has attracted a diverse range of re-
searchers,expandingbeyondAIexpertstoincludethosefrom
Large Language Models (LLMs) have recently shown re-
social science, psychology, and policy research. The vol-
markablepotentialinreachingalevelofreasoningandplan-
ume of research papers is rapidly increasing, as shown in
ning capabilities comparable to humans. This ability ex-
Fig. 1 (inspired by the design in [Gao et al., 2023b]), thus
actlyalignswiththeexpectationsofhumansforautonomous
broadening the impact of LLM-based Multi-Agent research.
agents that can perceive the surroundings, make decisions,
Nonetheless, earlier efforts were undertaken independently,
andtakeactionsinresponse[Xietal.,2023;Wooldridgeand
resultinginanabsenceofasystematicreviewtosummarize
Jennings,1995;RussellandNorvig,2009;Guoetal.,2023;
them,establishcomprehensiveblueprintofthisfield,andex-
Liangetal.,2023]. Hence,LLM-basedagenthasbeenstud-
amine future research challenges. This underscores the sig-
iedandrapidlydevelopedtounderstandandgeneratehuman-
nificanceofourworkandservesasthemotivationbehindpre-
like instructions, facilitating sophisticated interactions and
sentingthissurveypaper,dedicatedtotheresearchonLLM-
∗ThisworkwasdonewhenYaqiwasvisitingstudentsattheUni- basedmulti-agentsystems.
versityofNotreDame. We expect that our survey can make significant contribu-
†Correspondingauthor. tions to both the research and development of LLMs and to
4202
rpA
91
]LC.sc[
2v08610.2042:viXra

Figure 1: The rising trend in the research field of LLM-based Multi-Agents. For Problem Solving and World Simulation, we categorize
currentworkintoseveralcategoriesandcountthenumberofpapersofdifferenttypesat3-monthintervals. Thenumberateachleafnode
denotesthecountofpaperswithinthatcategory.
a wider range of interdisciplinary studies employing LLMs. inspecificways;3)agentcommunication,whichexamines
Readers will gain a comprehensive overview of LLM-based howagentsexchangemessagesandcollaborate;and4)agent
Multi-Agent (LLM-MA) systems, grasp the fundamental capability acquisition, which explores how agents develop
concepts involved in establishing multi-agent systems based their abilities to effectively solve problems. An additional
on LLMs, and catch the latest research trends and applica- perspectiveforreviewingstudiesaboutLLM-MAistheirap-
tionsinthisdynamicfield. Werecognizethatthisfieldisin plication. In Section 4, we categorize current applications
itsearlystagesandisrapidlyevolvingwithfreshmethodolo- intotwoprimarystreams: multi-agentsforproblem-solving
giesandapplications.Toprovideasustainableresourcecom- andmulti-agentsforworldsimulation. Toguideindividuals
plementing our survey paper, we maintain an open-source in identifying appropriate tools and resources, we present
GitHubrepository1. Wehopethatoursurveywillinspirefur- open-sourceimplementationframeworksforstudyingLLM-
therexplorationandinnovationinthisfield,aswellasappli- MA, as well as the usable datasets and benchmarks in Sec-
cationsacrossawidearrayofresearchdisciplines. tion 5. Based on the previous summary, we open the dis-
To assist individuals from various backgrounds in under- cussion for future research challenges and opportunities in
standing LLM-MA techniques and to complement existing Section6. TheconclusionsaresummarizedinSection7.
surveysbytacklingunresolvedquestions,wehaveorganized
our survey paper in the following manner. After laying out 2 Background
the background knowledge in Section 2, we address a piv-
2.1 Single-AgentSystemsPoweredLLMs
otal question: How are LLM-MA systems aligned with the
We introduce the background by first outlining the capabili-
collaborative task-solving environment? To answer this, we
ties of a single-agent system based on LLMs, following the
present a comprehensive schema for positioning, differenti-
discussionpresentedin[Weng,2023].
ating, and connecting various aspects of LLM-MA systems
in Section 3. We delve into this question by discussing: 1) Decision-makingThought: Thistermdenotesthecapabil-
theagents-environmentinterface,whichdetailshowagents ityofLLM-basedagents,guidedbyprompts,tobreakdown
interactwiththetaskenvironment;2)agentprofiling,which complextasksintosmallersubgoals[Khotetal.,2023],think
explainshowanagentischaracterizedbyanLLMtobehave through each part methodically (sometimes exploring mul-
tiple paths) [Yao et al., 2023], and learn from past experi-
1
https://github.com/taichengguo/LLMMultiAgentsSurveyPapers
ences[Shinnetal.,2023]toperformbetterdecision-making

on complex tasks. This capability enhances the autonomy checkingroles. Followingtheseactions,agentsreceivefeed-
ofasingleLLM-basedagentandbolstersitseffectivenessin back from the environment, informing them of the game’s
problem-solving. current state. This information guides the agents in adjust-
ing their strategies over time, responding to the evolving
Tool-use: LLM-based agents’ tool-use capability allows
gameplay and interactions with other agents. The Agents-
them to leverage external tools and resources to accom-
Environment Interface refers to the way in which agents in-
plishtasks, enhancingtheirfunctionalcapabilitiesandoper-
teract with and perceive the environment. It’s through this
atemoreeffectivelyindiverseanddynamicenvironments[Li
interfacethatagentsunderstandtheirsurroundings,makede-
etal.,2023d;Ruanetal.,2023;Gaoetal.,2023b].
cisions, and learn from the outcomes of their actions. We
Memory: This ability refers to the capability of LLM- categorize the current interfaces in LLM-MA systems into
based agent for conducting in-context learning [Dong et al., threetypes, Sandbox, Physcial, andNone, asdetailedinTa-
2023a]asshortmemoryorexternalvectordatabase[Lewiset ble1. TheSandboxreferstoasimulatedorvirtualenviron-
al., 2021] as long memoryto preserve and retrieve informa- ment built by human where agents can interact more freely
tionoverprolongedperiods[Wangetal.,2023b].Thisability andexperimentwithvariousactionsandstrategies. Thiskind
enablesasingleLLM-basedagenttomaintaincontextualco- of interface is widely used in software development (code
herenceandenhancelearningfrominteractions. interpreter as simulated environment) [Hong et al., 2023],
gaming (using game rules as simulated environment) [Mao
2.2 Single-AgentVS.Multi-AgentSystems et al., 2023], etc. The Physical is a real-world environment
Single-Agent systems empowered by LLMs have shown in- where agents interact with physical entities and obey real-
spiring cognitive abilities [Sumers et al., 2023]. The con- worldphysicsandconstraints. Inphysicalspace,agentsnor-
struction of such systems concentrates on formulating their mallyneedtotakeactionsthatcanhavedirectphysicalout-
internal mechanisms and interactions with the external en- comes. For example, in tasks such as sweeping the floor,
vironment. Conversely, LLM-MA systems emphasize di- making sandwiches, packing groceries, and arranging cab-
verse agent profiles, inter-agent interactions, and collective inets, robotic agents are required to perform actions itera-
decision-makingprocesses. Fromthisperspective,moredy- tively, observe the physical environment, and continuously
namicandcomplextaskscanbetackledbythecollaboration refinetheiractions[Mandietal.,2023]. Lastly,Nonerefers
of multiple autonomous agents, each of which is equipped toscenarioswherethereisnospecificexternalenvironment,
with unique strategies and behaviors, and engaged in com- andagentsdonotinteractwithanyenvironment. Forexam-
municationwithoneanother. ple, many applications [Du et al., 2023; Xiong et al., 2023;
Chan et al., 2023] utilize multiple agents to debate a ques-
3 DissectingLLM-MASystems: Interface, tiontoreachaconsensus. Theseapplicationsprimarilyfocus
on communication among agents and do not depend on the
Profiling,Communication,andCapabilities
externalenvironment.
Inthissection,wedelveintotheintricaciesofLLM-MAsys-
tems, where multiple autonomous agents engage in collabo- 3.2 AgentsProfiling
rative activities akin to human group dynamics in problem-
solving scenarios. A critical inquiry we address is how In LLM-MA systems, agents are defined by their traits, ac-
theseLLM-MAsystemsarealignedtotheiroperationalenvi- tions, and skills, which are tailored to meet specific goals.
ronments and the collective objectives they are designed to Across various systems, agents assume distinct roles, each
achieve. To shed light on this, we present the general ar- with comprehensive descriptions encompassing characteris-
chitecture of these systems in Fig. 2. Our analysis dissects tics, capabilities, behaviors, and constraints. For instance,
theoperationalframeworkofthesesystems,focusingonfour ingamingenvironments,agentsmightbeprofiledasplayers
key aspects: the agents-environment interface, agent profil- withvaryingrolesandskills,eachcontributingdifferentlyto
ing,agentcommunication,andagentcapabilityacquisition. thegame’sobjectives. Insoftwaredevelopment,agentscould
take on the roles of product managers and engineers, each
3.1 Agents-EnvironmentInterface withresponsibilitiesandexpertisethatguidethedevelopment
Theoperationalenvironmentsdefinesthespecificcontextsor process. Similarly, in a debating platform, agents might be
settings in which the LLM-MA systems are deployed and designated as proponents, opponents, or judges, each with
interact. For example, these environments can be like soft- uniquefunctionsandstrategiestofulfilltheirroleseffectively.
ware development [Hong et al., 2023], gaming [Mao et al., Theseprofilesarecrucialfordefiningtheagents’interactions
2023], and various other domains such as financial markets andeffectivenesswithintheirrespectiveenvironments. Table
[Li et al., 2023g] or even social behavior modeling [Park et 1liststheagentProfilesinrecentLLM-MAworks.
al., 2023]. The LLM-based agents perceive and act within Regarding the Agent Profiling Methods, we categorized
theenvironment,whichinturninfluencestheirbehaviorand them into three types: Pre-defined, Model-Generated, and
decisionmaking. Forexample,intheWerewolfGamesimu- Data-Derived. In the Pre-defined cases, agent profiles are
lation, the sandbox environment sets the game’s framework, explicitly defined by the system designers. The Model-
including transitions from day to night, discussion periods, Generated method creates agent profiles by models, e.g.,
voting mechanics, and reward rules. Agents, such as were- large language models. The Data-Derived method involves
wolves and the Seer, perform specific actions like killing or constructingagentprofilesbasedonpre-existingdatasets.

Figure2:TheArchitectureofLLM-MASystems.
3.3 AgentsCommunication
ThecommunicationbetweenagentsinLLM-MAsystemsis
the critical infrastructure supporting collective intelligence.
Wedissectagentcommunicationfromthreeperspectives: 1)
Communication Paradigms: the styles and methods of in-
teraction between agents; 2) Communication Structure: the
organization and architecture of communication networks
within the multi-agent system; and 3) Communication Con-
tentexchangedbetweenagents.
Communication Paradigms: Current LLM-MA systems
mainly take three paradigms for communication: Coopera-
tive, Debate, and Competitive. Cooperative agents work to-
gethertowardsasharedgoalorobjectives,typicallyexchang-
inginformationtoenhanceacollectivesolution. TheDebate
paradigmisemployedwhenagentsengageinargumentative
interactions, presenting and defending their own viewpoints
or solutions, and critiquing those of others. This paradigm
is ideal for reaching a consensus or a more refined solution.
Competitiveagentsworktowardstheirowngoalsthatmight
beinconflictwiththegoalsofotheragents. Figure3:TheAgentCommunicationStructure.
Communication Structure: Fig. 3 shows four typical
communication structures in LLM-MA systems. Layered
communication is structured hierarchically, with agents at work, where agents directly communicate with each other,
each level having distinct roles and primarily interacting a structure commonly employed in world simulation appli-
within their layer or with adjacent layers. [Liu et al., 2023] cations. Centralizedcommunicationinvolvesacentralagent
introduces a framework called Dynamic LLM-Agent Net- or a group of central agents coordinating the system’s com-
work (DyLAN), which organizes agents in a multi-layered munication, with other agents primarily interacting through
feed-forward network. This setup facilitates dynamic inter- this central node. Shared Message Pool is proposed by
actions, incorporating features like inference-time agent se- MetaGPT[Hongetal.,2023]toimprovethecommunication
lectionandanearly-stoppingmechanism,whichcollectively efficiency. Thiscommunicationstructuremaintainsashared
enhance the efficiency of cooperation among agents. De- message pool where agents publish messages and subscribe
centralized communication operates on a peer-to-peer net- torelevantmessagesbasedontheirprofiles,therebyboosting

communicationefficiency. todecidesubsequentactionsasseeninMemory-basedsolu-
tions,agentscandynamicallyself-evolvebymodifyingthem-
Communication Content: In LLM-MA systems, the
selvessuchasalteringtheirinitialgoalsandplanningstrate-
CommunicationContenttypicallytakestheformoftext. The
gies, and training themselves based on feedback or commu-
specific content varies widely and depends on the particular
nication logs. [Nascimento et al., 2023] proposes a self-
application. For example, in software development, agents
control loop process to allow each agent in the multi-agents
may communicate with each other about code segments. In
systemstobeself-managedandself-adaptivetodynamicen-
simulations of games like Werewolf, agents might discuss
vironments, therebyimprovingthecooperationefficiencyof
theiranalyses,suspicions,orstrategies.
multiple agents. [Zhang et al., 2023b] introduces ProA-
gent which anticipates teammates’ decisions and dynami-
3.4 AgentsCapabilitiesAcquisition
cally adjusts each agent’s strategies based on the communi-
The Agents Capabilities Acquisition is a crucial process in cation logs between agents, facilitating mutual understand-
LLM-MA, enabling agents to learn and evolve dynamically. ing and improving collaborative planning capability. [Wang
Inthiscontext,therearetwofundamentalconcepts:thetypes et al., 2023a] discusses a Learning through Communication
offeedbackfromwhichagentsshouldlearntoenhancetheir (LTC) paradigm, using the communication logs of multi-
capabilities,andthestrategiesforagentstoadjustthemselves agents to generate datasets to train or fine-tune LLMs. LTC
toeffectivelysolvecomplexproblems. enables continuous adaptation and improvement of agents
throughinteractionwiththeirenvironmentsandotheragents,
Feedback: Feedback involves the critical information that
breakingthelimitsofin-contextlearningorsupervisedfine-
agentsreceiveabouttheoutcomeoftheiractions,helpingthe
tuning, which don’t fully utilize the feedback received dur-
agents learn the potential impact of their actions and adapt
ing interactions with the environment and external tools
tocomplexanddynamicproblems. Inmoststudies, thefor-
for continuous training. Self-Evolution enables agents’ au-
mat of feedback provided to agents is textual. Based on the
tonomous adjustment in their profiles or goals, rather than
sources from which agents receive this feedback, it can be
just learning from historical interactions. 3) Dynamic Gen-
categorized into four types. 1) Feedback from Environ-
eration. In some scenarios, the system can generate new
ment, e.g., from either real world environments or virtual agents on-the-fly during its operation [Chen et al., 2023a;
environments [Wang et al., 2023b]. It is prevalent in most Chen et al., 2023c]. This capability enables the system to
LLM-MAforproblem-solvingscenarios,includingSoftware
scaleandadapteffectively,asitcanintroduceagentsthatare
Development(agentsobtainfeedbackfromCodeInterpreter),
specificallydesignedtoaddresscurrentneedsandchallenges.
andEmbodiedmulti-agentssystems(robotsobtainfeedback
With the scaling up LLM-MA with a larger number of
from real-world or Simulated environments). 2) Feedback
agents,theescalatingcomplexityofmanagingvariouskinds
from Agents Interactions means that the feedback comes
of agents has been a critical problem. Agents Orchestration
fromthejudgementofotheragentsorfromagentscommuni-
emerged as a pivotal challenge and began to gain attention
cations. Itiscommoninproblem-solvingscenarioslikesci- in [Moura, 2023;Dibia, 2023]. Wewillfurtherdiscussthis
encedebates,whereagentslearntocriticallyevaluateandre-
topicinSection6.4.
finetheconclusionsthroughcommunications. Inworldsim-
ulation scenarios such as Game Simulation, agents learn to
4 Applications
refinestrategiesbasedonpreviousinteractionsbetweenother
agents. 3) Human Feedback comes directly from humans LLM-MA systems have been used in a wide range of appli-
and is crucial for aligning the multi-agent system with hu- cations. WesummarizetwokindsofapplicationsinTable1:
manvaluesandpreferences. Thiskindoffeedbackiswidely Problem Solving and World Simulation. We elaborate on
usedinmost“Human-in-the-loop”applications[Wangetal., theseapplicationsbelow. Notethatthisisafastgrowingre-
2021].Last4)None.Insomecases,thereisnofeedbackpro- searchfieldandnewapplicationsappearalmosteveryday.We
videdtotheagents. Thisoftenhappensforworldsimulation maintainanopensourcerepositorytoreportthelatestwork.
worksfocusedonanalyzingsimulatedresultsratherthanthe
4.1 LLM-MAforProblemSolving
planningcapabilitiesofagents. Insuchscenarios,likeprop-
agation simulation, the emphasis is on result analysis, and ThemainmotivationofusingLLM-MAforproblemsolving
hence,feedbackisnotacomponentofthesystem. is to harness the collective capabilities of agents with spe-
cialized expertise. These agents, each acting as individuals,
Agents Adjustment to Complex Problems: To enhance
collaboratetoaddresscomplexproblemseffectively,suchas
their capabilities, agents in LLM-MA systems can adapt
softwaredevelopment,embodiedagents,scienceexperiments
through three main solutions. 1) Memory. Most LLM-
and science debate. These application examples are intro-
MA systems leverage a memory module for agents to ad-
ducednext.
just their behavior. Agents store information from previ-
ous interactions and feedback in their memory. When per- 4.1.1 SoftwareDevelopment
forming actions, they can retrieve relevant, valuable memo- Given that software development is a complex endeavor re-
ries,particularlythosecontainingsuccessfulactionsforsimi- quiring the collaboration of various roles like product man-
lar past goals, as highlighted in [Wang et al., 2023b]. This agers, programmers, andtesters, LLM-MAsystemsaretyp-
process aids in enhancing their current actions. 2) Self- ically set to emulate these distinct roles and collaborate to
Evolution. Instead of only relying on the historical records address the intricate challenge. Following the waterfall or

Agents
Agents-Env. AgentsProfiling AgentsCapabilitiesAcquisition
Communication
Interface
Motivation ResearchDomain&Goals Work Profiling Profiles Agents
Paradigms Structure Feedbackfrom
methods (examples) Adjustment
Environment,
Pre-defined, CTO, Memory,
[Qianetal.,2023] Sandbox Model-Generated programmer Cooperative Layered Agentinteraction, Self-Evolution
Human
Environment,
ProductManager, Layered, Memory,
Softwaredevelopment [Hongetal.,2023] Sandbox Pre-defined Engineer Cooperative SharedMessagePool Agentinteraction, Self-Evolution
Human
Pre-defined, Analyst, Environment, Memory,
[Dongetal.,2023b] Sandbox Model-Generated coder Cooperative Layered Agentinteraction Self-Evolution
Multi-robot Sandbox, Centralized, Environment,
planning [Chenetal.,2023d] Physical Pre-defined Robots Cooperative Decentralized Agentinteraction Memory
Embodied Multi-robot Sandbox, Environment,
Agents collaboration [Mandietal.,2023] Physical Pre-defined Robots Cooperative Decentralized Agentinteraction Memory
Multi-Agents Environment,
Problem cooperation [Zhangetal.,2023c] Sandbox Pre-defined Robots Cooperative Decentralized Agentinteraction Memory
Solving
Strategyplaners,
Science Optimization Environment,
Experiments ofMOF [Zhengetal.,2023] Physical Pre-defined literature Cooperative Centralized Human Memory
collector,coder
Improving
Factuality [Duetal.,2023] None Pre-defined Agents Debate Decentralized Agentinteraction Memory
Proponent,
Science Examining, Centralized,
Debate Inter-Consistency [Xiongetal.,2023] None Pre-defined Opponent, Debate Decentralized Agentinteraction Memory
Judge
Evaluators Centralized,
fordebates [Chanetal.,2023] None Pre-defined Agents Debate Decentralized Agentinteraction Memory
Multi-Agents Cardiology, Debate, Centralized,
forMedication [Tangetal.,2023] None Pre-defined Surgery Cooperative Decentralized Agentinteraction Memory
ModestCommunity Pharmacy, Environment,
(25persons) [Parketal.,2023] Sandbox Model-generated shopkeeper - - Agentinteraction Memory
Onlinecommunity Pre-defined, Camping, Dynamic
(1000persons) [Parketal.,2022] None Model-generated fishing - - Agentinteraction Generation
Pre-defined, Real-world
Society Emotionpropagation [Gaoetal.,2023a] None Model-generated user - - Agentinteraction Memory
Real-time Real-world Environment,
socialinteractions [Kaiyaetal.,2023] Sandbox Pre-defined user - - Agentinteraction Memory
NIN,NINL,
Opiniondynamics [Lietal.,2023a] None Pre-defined NIL - - Agentinteraction Memory
Seer, Cooperative,
WereWolf [Xuetal.,2023b] Sandbox Pre-defined werewolf, Debate, Decentralized Environment, Memory
World [Xuetal.,2023c] villager Competitive Agentinteraction
Simulation
Servant, Cooperative,
Gaming Avalon [Lightetal.,2023a] Sandbox Pre-defined Merlin, Debate, Decentralized Environment, Memory
[Wangetal.,2023c] Assassin Competitive Agentinteraction
Cooperative, Environment,
WelfareDiplomacy [Mukobietal.,2023] Sandbox Pre-defined Countries Competitive Decentralized Agentinteraction Memory
Humanbehavior
Simulation [Aheretal.,2023] Sandbox Pre-defined Humans - - Agentinteraction Memory
Psychology Collaboration Cooperative,
Exploring [Zhangetal.,2023d] None Pre-defined Agents Debate Decentralized Agentinteraction Memory
Macroeconomic Pre-defined,
simulation [Lietal.,2023e] None Model-generated Labor Cooperative Decentralized Agentinteraction Memory
Information Pre-defined, Cooperative, Environment,
Economy Marketplaces [Anonymous,2023] Sandbox Data-Derived Buyer Competitive Decentralized Agentinteraction Memory
Improving Environment,
financialtrading [Lietal.,2023g] Physical Pre-defined Trader Debate Decentralized Agentinteraction Memory
Pre-defined, Restaurant, Environment, Memory,
Economictheories [Zhaoetal.,2023] Sandbox Model-Generated Customer Competitive Decentralized Agentinteraction Self-Evolution
Simulating Usersfrom
Recommender userbehaviors [Zhangetal.,2023a] Sandbox Data-Derived MovieLens-1M - - Environment Memory
Systems
Simulatinguser-item Pre-defined, UserAgents Environment,
interactions [Zhangetal.,2023e] Sandbox Data-Derived ItemAgents Cooperative Decentralized Agentinteraction Memory
Public
Policy Administration [Xiaoetal.,2023] None Pre-defined Residents Cooperative Decentralized Agentinteraction Memory
Making
WarSimulation [Huaetal.,2023] None Pre-defined Countries Competitive Decentralized Agentinteraction Memory
HumanBehaviors [Ghaffarzadegan Sandbox Pre-defined, Conformity Cooperative Decentralized Environment, Memory
Disease toepidemics etal.,2023] Model-Generated traits Agentinteraction
Memory,
Publichealth [Williams Sandbox Pre-defined, Adultsaged Cooperative Decentralized Environment, Dynamic
etal.,2023] Model-Generated 18to64 Agentinteraction Generation
Table1:SummaryoftheLLM-MAstudies.Wecategorizecurrentworkaccordingtotheirmotivation,researchdomainsandgoals,anddetail
eachworkfromdifferentaspectsregardingAgents-EnvironmentInterface,AgentsProfiling,AgentsCommunicationandAgentsCapability
Acquisition.“-”denotesthataparticularelementisnotspecificallymentionedinthiswork.
Standardized Operating Procedures (SOPs) workflow of the insoftwaredevelopment,autonomouslycollaboratingtogen-
software development, the communication structure among eratecode. Moreover,[Qianetal.,2023]presentsanend-to-
agentsisusuallylayered. Agentsgenerallyinteractwiththe end framework for software development, utilizing multiple
code interpreter, other agents or human to iteratively refine agents for software development without incorporating ad-
the generated code. [Li et al., 2023b] first proposes a sim- vancedhumanteamworkexperience.[Hongetal.,2023]first
ple role-play agent framework, which utilizes the interplay incorporates human workflow insights for more controlled
of two roles to realize autonomous programming based on andvalidatedperformance. ItencodesSOPsintopromptsto
one-sentence user instruction. It provides insights into the enhancestructuredcoordination.[Huangetal.,2023a]delves
“cognitive”processesofcommunicativeagents. [Dongetal., deeper into multi-agent based programming by solving the
2023b]makesLLMsworkasdistinct“experts”forsub-tasks problem of balancing code snippet generation with effective

testcasegeneration,execution,andoptimization. byajointdebatingprocess. Throughmultipleroundsofde-
bate,theagentsconvergeonasingle,consensusanswer. [Du
4.1.2 EmbodiedAgents
et al., 2023] leverages the multi-agents debate process on a
Most embodied agents applications inherently utilize multi- set of six different reasoning and factual accuracy tasks and
ple robots working together to perform complex real-world demonstrates that LLM-MA debating can improve factual-
planningandmanipulationtaskssuchaswarehousemanage- ity. [Xiong et al., 2023] focuses on the commonsense rea-
ment with heterogeneous robot capabilities. Hence, LLM- soningtasksandformulatesathree-stagedebatetoalignwith
MA can be used to model robots with different capabilities real-world scenarios including fair debate, mismatched de-
and cooperate with each other to solve real-world physical bate, and roundtable debate. The paper also analyzes the
tasks. [Dasgupta et al., 2023] first explores the potential to inter-consistencybetweendifferentLLMsandclaimsthatde-
useLLMasanactionplannerforembeddedagents. [Mandi batingcanimprovetheinter-consistency.[Tangetal., 2023]
et al., 2023] introduces RoCo, a novel approach for multi- also utilizes multiple LLM-based agents as distinct domain
robot collaboration that uses LLMs for high-level commu- expertstodothecollaborativediscussiononamedicalreport
nication and low-level path planning. Each robotic arm is toreachaconsensusformedicaldiagnosis.
equipped with an LLM, cooperating with inverse kinemat-
icsandcollisionchecking. Experimentalresultsdemonstrate 4.2 LLM-MAforWorldSimulation
the adaptability and success of RoCo in collaborative tasks.
AnothermainstreamapplicationscenarioofLLM-MAisthe
[Zhang et al., 2023c] presents CoELA, a Cooperative Em-
world simulation. Research in this area is rapidly growing
bodiedLanguageAgent,managingdiscussionsandtaskplan-
andspansadiverserangeoffieldsincludingsocialsciences,
ning in an LLM-MA setting. This challenging setting is
gaming,psychology,economics,policy-making,etc.Thekey
featuredwithdecentralizedcontrol,complexpartialobserva-
reason foremploying LLM-MAin worldsimulations liesin
tion,costlycommunication,andmulti-objectivelong-horizon
theirexceptionalrole-playingabilities, whicharecrucialfor
tasks. [Chenetal.,2023d]investigatescommunicationchal-
realisticallydepictingvariousrolesandviewpointsinasim-
lenges in scenarios involving a large number of robots, as
ulatedworld. Theenvironmentofworldsimulationprojects
assigning each robot an LLM will be costly and unpracti-
isusuallycraftedtoreflectthespecificscenariobeingsimu-
cal due to the long context. The study compares four com-
lated, with agents designed in various profiles to match this
munication frameworks, centralized, decentralized, and two
context. Unlike the problem solving systems that focus on
hybridmodels,toevaluatetheireffectivenessincoordinating
agentcooperation, worldsimulationsystemsinvolvediverse
complex multi-agent tasks. [Yu et al., 2023] proposes Co-
methodsofagentmanagementandcommunication,reflecting
NavGPTformulti-robotcooperativevisualtargetnavigation,
the complexity and variety of real-world interactions. Next,
integrating LLM as a global planner to assign frontier goals
weexploresimulationsconductedindiversefields.
to each robot. [Chen et al., 2023b] proposes an LLM-based
consensus-seekingframework,whichcanbeappliedasaco- 4.2.1 SocietalSimulation
operativeplannertoamulti-robotaggregationtask.
In societal simulation, LLM-MA models are used to simu-
4.1.3 ScienceExperiments late social behaviors, aiming to explore the potential social
dynamics and propagation, test social science theories, and
Likemultipleagentsplayasdifferentspecialistsandcooper-
populatevirtualspacesandcommunitieswithrealisticsocial
atetosolvetheSoftwareDevelopmentandEmbodiedAgents
phenomena[Parketal., 2023]. LeveragingLLM’scapabili-
problem, multiple agents can also be used to form a science
ties,agentswithuniqueprofilesengageinextensivecommu-
team to conduct science experiments. One important differ-
nication, generating rich behavioral data for in-depth social
encefrompreviousapplicationsliesinthecrucialroleofhu-
scienceanalysis.
man oversight, due to the high expenses of the science ex-
periments and the hallucination of the LLM agents. Human The scale of societal simulation has expanded over time,
expertsareatthecenteroftheseagentstoprocesstheinfor- beginningwithsmaller,moreintimatesettingsandprogress-
mationofagentsandgivefeedbacktotheagents. [Zhenget ingtolarger,moreintricateones. Initialworkby[Parketal.,
al.,2023]utilizesmultipleLLM-basedagents,eachfocusing 2023]introducesgenerativeagentswithinaninteractivesand-
onspecifictasksforthescienceexperimentsincludingstrat- boxenvironmentreminiscentofthesims,allowingendusers
egy planning, literature search, coding, robotic operations, toengagewithamodestcommunityof25agentsthroughnat-
and labware design. All these agents interact with humans urallanguage. Atthesametime,[Parketal.,2022]develops
to work collaboratively to optimize the synthesis process of Social Simulacra, which constructs a simulated community
complexmaterials. of1,000personas. Thissystemtakesadesigner’svisionfor
a community—its goals, rules, and member personas—and
4.1.4 ScienceDebate simulatesit,generatingbehaviorslikeposting,replying,and
LLM-MA can be set for science debating scenarios, where evenanti-socialactions. Buildingonthis,[Gaoetal.,2023a]
agents debate with each other to enhance the collective rea- takestheconceptfurtherbyconstructingvastnetworkscom-
soning capabilities in tasks such as Massive Multitask Lan- prising 8,563 and 17,945 agents, respectively, designed to
guage Understanding (MMLU) [Hendrycks et al., 2020], simulatesocialnetworksfocusedonthetopicsofGenderDis-
Mathproblems[Cobbeetal., 2021], andStrategyQA [Geva crimination and Nuclear Energy. This evolution showcases
et al., 2021]. The main idea is that each agent initially of- theincreasingcomplexityandsizeofsimulatedenvironments
fers its own analysis of a problem, which is then followed inrecentresearch.Recentstudiessuchas[Chenetal.,2023b;

Kaiyaetal.,2023;Lietal.,2023a;Lietal.,2023f;Ziemset Thismethodfocusesonobservingandanalyzingtheirvaried
al., 2023] highlight the evolving complexity in multi-agent behaviors through statistical methods. Here, each agent op-
systems,LLMimpactsonsocialnetworks,andtheirintegra- erates independently, without interacting with others, essen-
tionintosocialscienceresearch. tially representing different individuals. Another approach
alignsmorecloselywithsocietalsimulations,wheremultiple
4.2.2 Gaming
agentsinteractandcommunicatewitheachother. Inthissce-
LLM-MA is well-suited for creating simulated gaming en-
nario, psychological theories are applied to understand and
vironments, allowing agents to assume various roles within
analyze the emergent behavioral patterns. This method fa-
games. This technology enables the development of con-
cilitates the study of interpersonal dynamics and group be-
trolled, scalable, and dynamic settings that closely mimic
haviors,providinginsightsintohowindividualpsychological
human interactions, making it ideal for testing a range of
traitsinfluencecollectiveactions. [Maetal.,2023]explores
gametheoryhypotheses[Maoetal.,2023;Xuetal.,2023b;
the psychological implications and outcomes of employing
Gongetal.,2023]. MostgamessimulatedbyLLM-MArely
LLM-basedconversationalagentsformentalwell-beingsup-
heavilyonnaturallanguagecommunication,offeringasand-
port. Itemphasizestheneedforcarefullyevaluatingtheuse
boxenvironmentwithindifferentgamesettingsforexploring
of LLM-based agents in mental health applications from a
ortestinggametheoryhypothesesincludingreasoning,coop-
psychological perspective. [Kovacˇ et al., 2023] introduces
eration,persuasion,deception,leadership,etc.
a tool named SocialAI school for creating interactive envi-
[Akata et al., 2023] leverages behavioral game theory to
ronmentssimulatingsocialinteractions. Itdrawsfromdevel-
examineLLMs’behaviorininteractivesocialsettings,partic-
opmentalpsychologytounderstandhowagentscanacquire,
ularlytheirperformanceingamesliketheiteratedPrisoner’s
demonstrate, and evolve social skills such as joint attention,
Dilemma and Battle of the Sexes. Furthermore, [Xu et al.,
communication,andculturallearning. [Zhangetal.,2023d]
2023b] proposes a framework using ChatArena library [Wu
explores how LLM agents, with distinct traits and thinking
et al., 2023b] for engaging LLMs in communication games
patterns,emulatehuman-likesocialbehaviorssuchasconfor-
likeWerewolf,usingretrievalandreflectiononpastcommu-
mity and majority rule. This integration of psychology into
nications for improvement, as well as the Chain-of-Thought
the understanding of agent collaboration offers a novel lens
mechanism[Weietal.,2022]. [Lightetal.,2023b]explores
for examining and enhancing the mechanisms behind LLM-
thepotentialofLLMagentsinplayingResistanceAvalon,in-
based multi-agents systems. [Aher et al., 2023] introduces
troducingAVALONBENCH,acomprehensivegameenviron-
TuringExperimentstoevaluatetheextenttowhichlargelan-
mentandbenchmarkforfurtherdevelopingadvancedLLMs
guagemodelscansimulatedifferentaspectsofhumanbehav-
and multi-agent frameworks. [Wang et al., 2023c] also fo-
iors. TheTuringExperimentsreplicateclassicalexperiments
cusesonthecapabilitiesofLLMAgentsindealingwithmis-
andphenomenainpsychology,economics,andsociologyus-
information in the Avalon game, proposing the Recursive
ingaquestion-answeringformattomimicexperimentalcon-
Contemplation(ReCon)frameworktoenhanceLLMs’ability
ditions. They also design a prompt that is used to simulate
todiscernandcounteractdeceptiveinformation. [Xuetal.,
theresponsesofmultipledifferentindividualsbyvaryingthe
2023c] introduces a framework combining LLMs with rein-
name. By simulating various kinds of individuals via LLM,
forcementlearning(RL)todevelopstrategiclanguageagents
theyshowthatlargermodelsreplicatehumanbehaviormore
fortheWerewolfgame. Itintroducesanewapproachtouse
faithfully,buttheyalsorevealahyper-accuracydistortion,es-
RLpolicyinthecasethattheactionandstatesetsarenotpre-
peciallyinknowledge-basedtasks.
defined but in the natural language setting. [Mukobi et al.,
2023]designsthe“WelfareDiplomacy”,ageneral-sumvari-
4.2.4 Economy
ant of the zero-sum board game Diplomacy, where players
LLM-MAisusedtosimulateeconomicandfinancialtrading
mustbalancemilitaryconquestanddomesticwelfare. Italso
environments mainly because it can serve as implicit com-
offersanopen-sourcebenchmark,aimingtohelpimprovethe
putational models of humans. In these simulations, agents
cooperationabilityofmulti-agentAIsystems. Ontopofthat,
areprovidedwithendowments,andinformation,andsetwith
thereisawork[Lietal.,2023c]inamulti-agentcooperative
pre-defined preferences, allowing for an exploration of their
textgametestingtheagents’TheoryofMind(ToM),theabil-
actionsineconomicandfinancialcontexts. Thisissimilarto
itytoreasonabouttheconcealedmentalstatesofothersand
thewayeconomistsmodel’homoeconomicus’,thecharacter-
is fundamental to human social interactions, collaborations,
izationofmaninsomeeconomictheoriesasarationalperson
andcommunications. [Fanetal.,2023]comprehensivelyas-
whopursueswealthforhisownself-interest [Horton,2023].
sesses the capability of LLMs as rational players, and iden-
Thereareseveralstudiesdemonstratethediverseapplications
tifies the weaknesses of LLM-based Agents that even in the
of LLM-MA in simulating economic scenarios, encompass-
explicit game process, agents may still overlook or modify
ing macroeconomic activities, information marketplaces, fi-
refinedbeliefswhentakingactions.
nancial trading, and virtual town simulations. Agents in-
4.2.3 Psychology teract in cooperative or debate, decentralized environments.
Inpsychologicalsimulationstudies,likeinthesocietalsimu- [Li et al., 2023e] employs LLMs for macroeconomic simu-
lation, multiple agents are utilized to simulate humans with lation,featuringprompt-engineering-drivenagentsthatemu-
various traits and thought processes. However, unlike so- latehuman-likedecision-making,therebyenhancingthereal-
cietal simulations, one approach in psychology involves di- ismofeconomicsimulationscomparedtorule-basedorother
rectly applying psychological experiments to these agents. AI agents. [Anonymous, 2023] explores the buyer’s inspec-

Motivation Domain DatasetsandBenchmarks Usedby DataLink
HumanEval [Hongetal.,2023] Link
SoftwareDevelopment MBPP [Hongetal.,2023] Link
SoftwareDev [Hongetal.,2023] Link
RoCoBench [Mandietal.,2023] Link
CommunicativeWatch-And-Help(C-WAH) [Zhangetal.,2023c] Link
EmbodiedAI
ThreeDWorldMulti-AgentTransport(TDW-MAT) [Zhangetal.,2023c] Link
ProblemSolving HM3Dv0.2 [Yuetal.,2023] Link
MMLU [Tangetal.,2023] Link
MedQA [Tangetal.,2023] Link
PubMedQA [Tangetal.,2023] Link
ScienceDebate
GSM8K [Duetal.,2023] Link
StrategyQA [Xiongetal.,2023] Link
ChessMoveValidity [Duetal.,2023] Link
SOTOPIA [Zhouetal.,2023b] /
Society GenderDiscrimination [Gaoetal.,2023a] /
NuclearEnergy [Gaoetal.,2023a] /
Werewolf [Xuetal.,2023b] /
Avalon [Lightetal.,2023b] /
WelfareDiplomacy [Mukobietal.,2023] /
Gaming
LayoutintheOvercooked-AIenvironment [Agasheetal.,2023] /
WorldSimulation Chameleon [Xuetal.,2023a] Link
Undercover [Xuetal.,2023a] Link
UltimatumGameTE [Aheretal.,2023] Link
Psychology GardenPathTE [Aheretal.,2023] Link
WisdomofCrowdsTE [Aheretal.,2023] Link
MovieLens-1M [Zhangetal.,2023a] Link
RecommenderSystem
Amazonreviewdataset [Zhangetal.,2023e] /
PolicyMaking BoardConnectivityEvaluation [Huaetal.,2023] Link
Table2:DatasetsandBenchmarkscommonlyusedinLLM-MAstudies.“/”denotestheunavailabilityofdatalink.
tionparadoxinaninformationmarketplace,revealsimproved causalrelationshipsinrecommendationtasks. InAgent4Rec
decision-making and answer quality when agents temporar- work,agentsareusedtosimulateusersandtheydonotcom-
ily access information before purchase. [Li et al., 2023g] municate with each other. Different from Agent4Rec work,
presents an LLM-MA framework for financial trading, em- [Zhang et al., 2023e] treats both users and items as agents,
phasizingalayeredmemorysystem,debatemechanisms,and optimizing them collectively to reflect and adjust to real-
individualizedtradingcharacters,therebyfortifyingdecision- worldinteractiondisparities. Thisworkemphasizessimulat-
making robustness. [Zhao et al., 2023] utilizes LLM-based inguser-iteminteractionsandpropagatespreferencesamong
Agents to simulate a virtual town with restaurant and cus- agents,capturingthecollaborativefilteringessence.
tomeragents,yieldinginsightsalignedwithsociologicaland
economic theories. These studies collectively illuminate the
4.2.6 PolicyMaking
broadspectrumofapplicationsandadvancementsinemploy-
ingLLMsfordiverseeconomicsimulationscenarios.
Similar to simulations in gaming and economic scenarios,
Policy Making requires strong decision-making capabilities
4.2.5 RecommenderSystems
to realistic and dynamic complex problems. LLM-MA can
TheuseoftheLLM-MAinrecommendersystemsissimilar beusedtosimulatethepolicymakingviasimulatingavirtual
to that in psychology since studies in both fields involve the government or simulating the impact of various policies on
considerationofextrinsicandintrinsichumanfactorssuchas different communities. These simulations provide valuable
cognitiveprocessesandpersonality[LexandSchedl, 2022]. insights into how policies are formulated and their potential
OnewaytouseLLM-MAinrecommendersystemsistodi- effects, aiding policymakers in understanding and anticipat-
rectly introduce items to multiple LLM-based agents within ing the consequences of their decisions [Farmer and Axtell,
diversetraitsandconductstatisticsofthepreferencesofdif- 2022]. The research outlined in [Xiao et al., 2023] is cen-
ferent agents. Another way is to treat both users and items teredonsimulatingatownshipwaterpollutioncrisis. Itsim-
as agents and the user-item communication as interactions, ulated a town located on an island including a demographic
simulatingthepreferencepropagation. Tobridgethegapbe- structure of different agents and township head and advisor.
tween offline metrics and real-world performance in recom- Within the water pollution crisis simulation, this work pro-
mendation systems, Agent4Rec [Zhang et al., 2023a] intro- videsanin-depthanalysisofhowavirtualgovernmententity
ducesasimulationplatformbasedonLLM-MA.1000gener- mightrespondtosuchapublicadministrationchallengeand
ativeagentsareinitializedwiththeMovieLens-1Mdatasetto how information transfer in the social network in this crisis.
simulatecomplexuserinteractionsinarecommendationen- [Huaetal., 2023]introducesWarAgenttosimulatekeyhis-
vironment. Agent4RecshowsthatLLM-MAcaneffectively torical conflicts and provides insights for conflict resolution
mimic real user preferences and behaviors, provide insights and understanding, with potential applications in preventing
intophenomenalikethefilterbubbleeffect,andhelpuncover futureinternationalconflicts.

4.2.7 DiseasePropagationSimulation search applications use different datasets and benchmarks.
Leveraging the societal simulation capabilities of LLM-MA In the Problem solving scenarios, most datasets and bench-
can also be used to simulate disease propagation. The most marksareusedtoevaluatetheplanningandreasoningcapa-
recentstudyin[Williamsetal., 2023]delvesintotheuseof bilities by Multiple agents cooperation or debate. In World
LLM-MA in simulating disease spread. The research show- Simulation scenarios, datasets and benchmarks are used to
cases through various simulations how these LLM-based evaluatethealignmentbetweenthesimulatedworldandreal-
agents can accurately emulate human responses to disease worldoranalyzethebehaviorsofdifferentagents. However,
outbreaks, including behaviors like self-quarantine and iso- incertainresearchapplicationslikeScienceTeamoperations
lation during heightened case numbers. The collective be- forexperimentsandeconomicmodeling,thereisstillaneed
havioroftheseagentsmirrorsthecomplexpatternsofmulti- for comprehensive benchmarks. The development of such
plewavestypicallyseeninpandemics,eventuallystabilizing benchmarks would greatly enhance the ability to gauge the
into an endemic state. Impressively, their actions contribute successandapplicabilityofLLM-MAinthesecomplexand
totheattenuationoftheepidemiccurve. [Ghaffarzadeganet dynamicfields.
al.,2023]alsodiscussestheepidemicpropagationsimulation
anddecomposesthesimulationintotwoparts:theMechanis- 6 ChallengesandOpportunities
ticModelwhichrepresentstheinformationorpropagationof
Studies of LLM-MA frameworks and applications are ad-
the virus and the Decision-Making Model which represents
vancing rapidly, giving rise to numerous challenges and op-
theagents’decision-makingprocesswhenfacingthevirus.
portunities. Weidentifiedseveralcriticalchallengesandpo-
tentialareasforfuturestudy.
5 ImplementationToolsandResources
5.1 Multi-AgentsFramework 6.1 AdvancingintoMulti-ModalEnvironment
We provide a detailed introduction to three open-source MostpreviousworkonLLM-MAhasbeenfocusedontext-
multi-agent frameworks: MetaGPT [Hong et al., 2023], based environments, excelling in processing and generating
CAMEL[Lietal., 2023b], andAutogen[Wuetal., 2023a]. text. However, there is a notable lack in multi-modal set-
They are all frameworks that utilize language models for tings, where agents would interact with and interpret data
complextask-solvingwithafocusonmulti-agentcollabora- from multiple sensory inputs and generate multiple outputs
tion,buttheydifferintheirapproachesandapplications. such as images, audio, video, and physical actions. Inte-
MetaGPTisdesignedtoembedhumanworkflowprocesses grating LLMs into multi-modal environments presents addi-
intotheoperationoflanguagemodelagents,therebyreducing tional challenges, such as processing diverse data types and
thehallucinationproblemthatoftenarisesincomplextasks. enablingagentstounderstandeachotherandrespondtomore
ItdoesthisbyencodingStandardOperatingProceduresinto thanjusttextualinformation.
thesystemandusinganassemblylineapproachtoassignspe-
6.2 AddressingHallucination
cificrolestodifferentagents.
CAMEL,orCommunicativeAgentFramework,isoriented ThehallucinationproblemisasignificantchallengeinLLMs
towards facilitating autonomous cooperation among agents. and single LLM-based Agent systems. It refers to the phe-
Itusesanoveltechniquecalledinceptionpromptingtoguide nomenonwherethemodelgeneratestextthatisfactuallyin-
conversationalagentstowardsfulfillingtasksthatareconsis- correct [Huang et al., 2023b]. However, this problem takes
tentwithhumanobjectives. Thisframeworkalsoservesasa onanaddedlayerofcomplexityinamulti-agentsetting. In
tool for generating and studying conversational data, help- suchscenarios, oneagent’shallucinationcanhaveacascad-
ing researchers understand how communicative agents be- ingeffect. Thisisduetotheinterconnectednatureofmulti-
haveandinteract. agentsystems,wheremisinformationfromoneagentcanbe
AutoGen is a versatile framework that allows for the cre- accepted and further propagated by others in the network.
ationofapplicationsusinglanguagemodels. Itisdistinctive Therefore, detecting and mitigating hallucinations in LLM-
foritshighlevelofcustomization,enablingdeveloperstopro- MA is not just a crucial task but also presents a unique set
gram agents using both natural language and code to define ofchallenges. Itinvolvesnotonlycorrectinginaccuraciesat
how these agents interact. This versatility enables its use in the level of individual agents but also managing the flow of
diversefields,fromtechnicalareassuchascodingandmath- informationbetweenagentstopreventthespreadofthesein-
ematicstoconsumer-focusedsectorslikeentertainment. accuraciesthroughoutthesystem.
More recently, [Chen et al., 2023c; Chen et al., 2023a]
introduce frameworks for dynamic multi-agent collabora- 6.3 AcquiringCollectiveIntelligence
tion, while [Zhou et al., 2023a; Li et al., 2023h; Xie et Intraditionalmulti-agentsystems,agentsoftenusereinforce-
al., 2023] present platforms and libraries for building au- ment learning to learn from offline training datasets. How-
tonomous agents, emphasizing their adaptability in task- ever,LLM-MAsystemsmainlylearnfrominstantfeedback,
solvingandsocialsimulations. such as interactions with the environment or humans, as we
discussed in Section 3. This learning style requires a reli-
5.2 DatasetsandBenchmarks
ableinteractiveenvironmentanditwouldbetrickytodesign
We summarize commonly used datasets or benchmarks for suchaninteractiveenvironmentformanytasks, limitingthe
LLM-MA study in Table 2. We observe that different re- scalability of LLM-MA systems. Moreover, the prevailing

approaches in current research involve employing Memory 6.6 ApplicationsandBeyond
andSelf-Evolutiontechniquestoadjustagentsbasedonfeed- ThepotentialofLLM-MAsystemsextendsfarbeyondtheir
back. Whileeffectiveforindividualagents,thesemethodsdo current applications, holding great promise for advanced
notfullycapitalizeonthepotentialcollectiveintelligenceof computationalproblem-solvinginfieldssuchasfinance,edu-
theagentnetwork. Theyadjustagentsinisolation,overlook- cation,healthcare,environmentalscience,urbanplanningand
ing the synergistic effects that can emerge from coordinated soon. Aswehavediscussed,LLM-MAsystemspossessthe
multi-agent interactions. Hence, jointly adjusting multiple capability to tackle complex problems and simulate various
agentsandachievingoptimalcollectiveintelligenceisstilla aspectsoftherealworld. Whilethecurrentrole-playingca-
criticalchallengeforLLM-MA. pabilities of LLMs may have limitations, ongoing advance-
ments in LLM technology suggest a bright future. It is an-
6.4 ScalingUpLLM-MASystems ticipatedtohavemoresophisticatedmethodologies,applica-
tions, datasets, andbenchmarkstailoredfordiverseresearch
LLM-MA systems are composed of a number of individual
fields. Furthermore,thereareopportunitiestoexploreLLM-
LLM-based agents, posing a significant challenge of scala-
MA systems from various theoretical perspectives, such as
bility regarding the number of agents. From the computa-
CognitiveScience[Sumersetal.,2023],SymbolicArtificial
tional complexity perspective, each LLM-based agent, typ-
Intelligence, Cybernetics, Complex Systems, and Collective
ically built on large language models like GPT-4, demands
Intelligence. Suchamulti-facetedapproachcouldcontribute
substantialcomputationalpowerandmemory. Scalingupthe
toamorecomprehensiveunderstandingandinnovativeappli-
numberoftheseagentsinanLLM-MAsystemsignificantly
cationsinthisrapidlyevolvingfield.
increases resource requirements. In scenarios with limited
computational resource, it would be challenging to develop
7 Conclusion
theseLLM-MAsystems.
Additionally,asthenumberofagentsinanLLM-MAsys- LLM-basedMulti-Agentshaveshowninspiringcollectivein-
temincreases,additionalcomplexitiesandresearchopportu- telligenceandrapidlygarneredincreasinginterestamongre-
nities emerge, particularly in areas like efficient agent coor- searchers. In this survey, we first systematically review the
dination,communication,andunderstandingthescalinglaws development of LLM-MA systems by positioning, differen-
ofmulti-agents. Forinstance,withmoreLLM-basedagents, tiating, and connecting them from various aspects, regard-
the intricacy of ensuring effective coordination and commu- ingtheagents-environmentinterface, thecharacterizationof
nicationrisessignificantly. Ashighlightedin [Dibia,2023], agentsbyLLMs,thestrategiesformanagingagentcommuni-
designing advanced Agents Orchestration methodologies is cationandtheparadigmsforcapabilityacquisition. Wealso
increasingly important. These methodologies aim to opti- summarizedLLM-MAapplicationsforproblem-solvingand
mize agents workflows, task assignments tailored to differ- world simulation. By also highlighting the commonly used
entagents,andcommunicationpatternsacrossagentssuchas datasets and benchmarks and discussing challenges and fu-
communicationconstraintsbetweenagents. EffectiveAgents tureopportunities,wehopethatthissurveycanserveasause-
Orchestrationfacilitatesharmoniousoperationamongagents, fulresourceforresearchersacrossvariousresearchfields,in-
minimizingconflictsandredundancies. Additionally,explor- spiringfutureresearchtoexplorethepotentialofLLM-based
inganddefiningthescalinglawsthatgovernthebehaviorand Multi-Agents.
efficiencyofmulti-agentsystemsastheygrowlargerremains
an important area of research. These aspects highlight the References
needforinnovativesolutionstooptimizeLLM-MAsystems, [Agasheetal.,2023] SaaketAgashe,YueFan,andXinEric
makingthembotheffectiveandresource-efficient.
Wang. Evaluating multi-agent coordination abilities in
largelanguagemodels,2023.
6.5 EvaluationandBenchmarks
[Aheretal.,2023] Gati Aher, Rosa I. Arriaga, and
Wehavesummarizedthedatasetsandbenchmarkscurrently Adam Tauman Kalai. Using large language models
availableforLLM-MAinTable2.Thisisastartingpoint,and to simulate multiple humans and replicate human subject
far from being comprehensive. We identify two significant studies,2023.
challenges in evaluating LLM-MA systems and benchmark-
[Akataetal.,2023] Elif Akata, Lion Schulz, Julian Coda-
ingtheirperformanceagainsteachother.Firstly,asdiscussed
Forno,SeongJoonOh,MatthiasBethge,andEricSchulz.
in [Xuetal., 2023a], muchoftheexistingresearchfocuses
Playingrepeatedgameswithlargelanguagemodels.arXiv
on evaluating individual agents’ understanding and reason-
preprintarXiv:2305.16867,2023.
ing within narrowly defined scenarios. This focus tends to
[Anonymous,2023] Anonymous.Rethinkingthebuyer’sin-
overlookthebroaderandmorecomplexemergentbehaviors
spection paradox in information markets with language
thatareintegraltomulti-agentsystems. Secondly, thereisa
agents. In Submitted to The Twelfth International Con-
notableshortfallinthedevelopmentofcomprehensivebench-
ferenceonLearningRepresentations,2023. underreview.
marksacrossseveralresearchdomains,suchasScienceTeam
for Experiment Operations, Economic analysis, and Disease [Chanetal.,2023] Chi-Min Chan, Weize Chen, Yusheng
propagationsimulation. Thisgappresentsanobstacletoac- Su,JianxuanYu,WeiXue,ShanghangZhang,JieFu,and
curately assessing and benchmarking the full capabilities of ZhiyuanLiu. Chateval: Towardsbetterllm-basedevalua-
LLM-MAsystemsinthesevariedandcrucialfields. torsthroughmulti-agentdebate,2023.

[Chenetal.,2023a] Guangyao Chen, Siwei Dong, Yu Shu, large language model-empowered agents. arXiv preprint
Ge Zhang, Jaward Sesay, Bo¨rje F Karlsson, Jie Fu, and arXiv:2307.14984,2023.
YeminShi. Autoagents: Aframeworkforautomaticagent
[Gaoetal.,2023b] Yunfan Gao, Yun Xiong, Xinyu Gao,
generation. arXivpreprintarXiv:2309.17288,2023.
Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei
[Chenetal.,2023b] HuabenChen,WenkangJi,LufengXu, Sun, and Haofen Wang. Retrieval-augmented generation
andShiyuZhao. Multi-agentconsensusseekingvialarge for large language models: A survey. arXiv preprint
languagemodels. arXivpreprintarXiv:2310.20151,2023. arXiv:2312.10997,2023.
[Chenetal.,2023c] WeizeChen,YushengSu,JingweiZuo, [Gevaetal.,2021] MorGeva,DanielKhashabi,EladSegal,
Cheng Yang, Chenfei Yuan, Chen Qian, Chi-Min Chan, Tushar Khot, Dan Roth, and Jonathan Berant. Did aris-
YujiaQin,YaxiLu,RuobingXie,etal. Agentverse:Facil- totleusealaptop? aquestionansweringbenchmarkwith
itating multi-agent collaboration and exploring emergent implicitreasoningstrategies,2021.
behaviors in agents. arXiv preprint arXiv:2308.10848,
[Ghaffarzadeganetal.,2023] Navid Ghaffarzadegan, Aritra
2023.
Majumdar,RossWilliams,andNiyoushaHosseinichimeh.
[Chenetal.,2023d] Yongchao Chen, Jacob Arkin, Yang
Generative agent-based modeling: Unveiling social sys-
Zhang, Nicholas Roy, and Chuchu Fan. Scalable multi-
tem dynamics through coupling mechanistic models
robot collaboration with large language models: Cen-
with generative artificial intelligence. arXiv preprint
tralized or decentralized systems? arXiv preprint
arXiv:2309.11456,2023.
arXiv:2309.15943,2023.
[Gongetal.,2023] Ran Gong, Qiuyuan Huang, Xiaojian
[Cobbeetal.,2021] Karl Cobbe, Vineet Kosaraju, Moham-
Ma, Hoi Vo, Zane Durante, Yusuke Noda, Zilong Zheng,
mad Bavarian, Mark Chen, Heewoo Jun, Lukasz Kaiser,
Song-Chun Zhu, Demetri Terzopoulos, Li Fei-Fei, et al.
Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Mindagent: Emergentgaminginteraction. arXivpreprint
Nakano,etal. Trainingverifierstosolvemathwordprob-
arXiv:2309.09971,2023.
lems. arXivpreprintarXiv:2110.14168,2021.
[Guoetal.,2023] Taicheng Guo, Kehan Guo, Zhengwen
[Dasguptaetal.,2023] Ishita Dasgupta, Christine Kaeser-
Liang, Zhichun Guo, Nitesh V Chawla, Olaf Wiest, Xi-
Chen, Kenneth Marino, Arun Ahuja, Sheila Babayan,
angliang Zhang, et al. What indeed can gpt models do
Felix Hill, and Rob Fergus. Collaborating with lan-
inchemistry? acomprehensivebenchmarkoneighttasks.
guage models for embodied reasoning. arXiv preprint
arXivpreprintarXiv:2305.18365,2023.
arXiv:2302.00763,2023.
[Dibia,2023] Victor Dibia. Multi-agent llm applica- [Hendrycksetal.,2020] Dan Hendrycks, Collin Burns,
tions — a review of current research, tools, and Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song,
challenges. https://newsletter.victordibia.com/p/ and Jacob Steinhardt. Measuring massive multitask lan-
multi-agent-llm-applications-a-review,2023. guage understanding. arXiv preprint arXiv:2009.03300,
2020.
[Dongetal.,2023a] Qingxiu Dong, Lei Li, Damai Dai,
CeZheng,ZhiyongWu,BaobaoChang,XuSun,Jingjing [Hongetal.,2023] Sirui Hong, Xiawu Zheng, Jonathan
Xu,LeiLi,andZhifangSui. Asurveyonin-contextlearn- Chen, Yuheng Cheng, Ceyao Zhang, Zili Wang, Steven
ing,2023. Ka Shing Yau, Zijuan Lin, Liyang Zhou, Chenyu Ran,
et al. Metagpt: Meta programming for multi-agent col-
[Dongetal.,2023b] Yihong Dong, Xue Jiang, Zhi Jin, and
laborative framework. arXiv preprint arXiv:2308.00352,
Ge Li. Self-collaboration code generation via chatgpt,
2023.
2023.
[Horton,2023] John J Horton. Large language models as
[Duetal.,2023] Yilun Du, Shuang Li, Antonio Torralba,
simulatedeconomicagents:Whatcanwelearnfromhomo
JoshuaB.Tenenbaum,andIgorMordatch. Improvingfac-
silicus? Technical report, National Bureau of Economic
tualityandreasoninginlanguagemodelsthroughmultia-
Research,2023.
gentdebate,2023.
[Fanetal.,2023] CaoyunFan,JindouChen,YaohuiJin,and [Huaetal.,2023] Wenyue Hua, Lizhou Fan, Lingyao Li,
HaoHe.Canlargelanguagemodelsserveasrationalplay- KaiMei,JianchaoJi,YingqiangGe,LibbyHemphill,and
ersingametheory? asystematicanalysis. arXivpreprint Yongfeng Zhang. War and peace (waragent): Large lan-
arXiv:2312.05488,2023. guagemodel-basedmulti-agentsimulationofworldwars,
2023.
[FarmerandAxtell,2022] J. Doyne Farmer and Robert L.
Axtell.Agent-BasedModelinginEconomicsandFinance: [Huangetal.,2023a] Dong Huang, Qingwen Bu, Jie M.
Past, Present, and Future. INET Oxford Working Papers Zhang, Michael Luck, and Heming Cui. Agentcoder:
2022-10,InstituteforNewEconomicThinkingattheOx- Multi-agent-based code generation with iterative testing
fordMartinSchool,UniversityofOxford,June2022. andoptimisation,2023.
[Gaoetal.,2023a] ChenGao,XiaochongLan,ZhihongLu, [Huangetal.,2023b] Lei Huang, Weijiang Yu, Weitao Ma,
JinzhuMao, JinghuaPiao, HuandongWang, DepengJin, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qiang-
andYongLi. S3: Social-networksimulationsystemwith longChen,WeihuaPeng,XiaochengFeng,BingQin,etal.

Asurveyonhallucinationinlargelanguagemodels: Prin- [Lietal.,2023g] Yang Li, Yangyang Yu, Haohang Li, Zhi
ciples, taxonomy, challenges, and open questions. arXiv Chen,andKhaldounKhashanah. Tradinggpt: Multi-agent
preprintarXiv:2311.05232,2023. system with layered memory and distinct characters for
enhancedfinancialtradingperformance,2023.
[Kaiyaetal.,2023] Zhao Kaiya, Michelangelo Naim, Jo-
vana Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo, [Lietal.,2023h] Yuan Li, Yixuan Zhang, and Lichao Sun.
Guangyu Robert Yang, and Andrew Ahn. Lyfe agents: Metaagents: Simulating interactions of human behaviors
Generative agents for low-cost real-time social interac- forllm-basedtask-orientedcoordinationviacollaborative
tions. arXivpreprintarXiv:2310.02172,2023. generativeagents.arXivpreprintarXiv:2310.06500,2023.
[Khotetal.,2023] Tushar Khot, Harsh Trivedi, Matthew [Liangetal.,2023] Zhenwen Liang, Wenhao Yu, Tanmay
Finlayson, Yao Fu, Kyle Richardson, Peter Clark, and Rajpurohit, Peter Clark, Xiangliang Zhang, and Ashwin
Ashish Sabharwal. Decomposed prompting: A modular Kaylan.Letgptbeamathtutor:Teachingmathwordprob-
approachforsolvingcomplextasks,2023. lem solvers with customized exercise generation. arXiv
preprintarXiv:2305.14386,2023.
[Kovacˇ etal.,2023] GrgurKovacˇ,Re´myPortelas,PeterFord
[Lightetal.,2023a] Jonathan Light, Min Cai, Sheng Shen,
Dominey, andPierre-YvesOudeyer. Thesocialaischool:
andZiniuHu. Avalonbench: Evaluatingllmsplayingthe
Insightsfromdevelopmentalpsychologytowardsartificial
gameofavalon,2023.
socio-cultural agents. arXiv preprint arXiv:2307.07871,
2023. [Lightetal.,2023b] Jonathan Light, Min Cai, Sheng Shen,
and Ziniu Hu. From text to tactic: Evaluating llms play-
[Lewisetal.,2021] Patrick Lewis, Ethan Perez, Aleksan-
ingthegameofavalon. arXivpreprintarXiv:2310.05036,
dra Piktus, Fabio Petroni, Vladimir Karpukhin, Naman
2023.
Goyal, Heinrich Ku¨ttler, Mike Lewis, Wen tau Yih,
Tim Rockta¨schel, Sebastian Riedel, and Douwe Kiela. [Liuetal.,2023] Zijun Liu, Yanzhe Zhang, Peng Li, Yang
Retrieval-augmented generation for knowledge-intensive Liu,andDiyiYang. Dynamicllm-agentnetwork: Anllm-
nlptasks,2021. agentcollaborationframeworkwithagentteamoptimiza-
tion. arXivpreprintarXiv:2310.02170,2023.
[LexandSchedl,2022] Elisabeth Lex and Markus Schedl.
Psychology-informed recommender systems: A human- [Maetal.,2023] Zilin Ma, Yiyang Mei, and Zhaoyuan Su.
centricperspectiveonrecommendersystems. InProceed- Understanding the benefits and challenges of using large
ings of the 2022 Conference on Human Information In- language model-based conversational agents for mental
teraction and Retrieval, CHIIR ’22, page 367–368, New well-being support. arXiv preprint arXiv:2307.15810,
York, NY, USA, 2022. Association for Computing Ma- 2023.
chinery. [Mandietal.,2023] Zhao Mandi, Shreeya Jain, and Shuran
Song.Roco:Dialecticmulti-robotcollaborationwithlarge
[Lietal.,2023a] ChaoLi,XingSu,ChaoFan,HaoyingHan,
languagemodels. arXivpreprintarXiv:2307.04738,2023.
Cong Xue, and Chunmo Zheng. Quantifying the impact
oflargelanguagemodelsoncollectiveopiniondynamics. [Maoetal.,2023] Shaoguang Mao, Yuzhe Cai, Yan Xia,
arXivpreprintarXiv:2308.03313,2023. WenshanWu,XunWang,FengyiWang,TaoGe,andFuru
Wei.Alympics:Languageagentsmeetgametheory.arXiv
[Lietal.,2023b] Guohao Li, Hasan Abed Al Kader Ham-
preprintarXiv:2311.03220,2023.
moud, Hani Itani, Dmitrii Khizbullin, and Bernard
Ghanem. Camel: Communicative agents for” mind” ex- [Moura,2023] Joa˜o Moura. Crewai. https://github.com/
ploration of large scale language model society. arXiv joaomdmoura/crewAI,2023.
preprintarXiv:2303.17760,2023. [Mukobietal.,2023] Gabriel Mukobi, Hannah Erlebach,
[Lietal.,2023c] HuaoLi,YuQuanChong,SimonStepput- Niklas Lauffer, Lewis Hammond, Alan Chan, and Jesse
Clifton. Welfare diplomacy: Benchmarking language
tis, Joseph Campbell, Dana Hughes, Michael Lewis, and
model cooperation. arXiv preprint arXiv:2310.08901,
Katia Sycara. Theory of mind for multi-agent collabora-
2023.
tionvialargelanguagemodels,2023.
[Nascimentoetal.,2023] NathaliaNascimento,PauloAlen-
[Lietal.,2023d] Minghao Li, Yingxiu Zhao, Bowen Yu,
car, and Donald Cowan. Self-adaptive large language
Feifan Song, Hangyu Li, Haiyang Yu, Zhoujun Li, Fei
model (llm)-based multiagent systems. In 2023 IEEE
Huang, and Yongbin Li. Api-bank: A comprehensive
International Conference on Autonomic Computing and
benchmarkfortool-augmentedllms,2023.
Self-Organizing Systems Companion (ACSOS-C), pages
[Lietal.,2023e] NianLi,ChenGao,YongLi,andQingmin 104–109.IEEE,2023.
Liao. Largelanguagemodel-empoweredagentsforsimu-
[Parketal.,2022] JoonSungPark, LindsayPopowski, Car-
latingmacroeconomicactivities,2023.
rie Cai, Meredith Ringel Morris, Percy Liang, and
[Lietal.,2023f] SiyuLi, JinYang, andKuiZhao. Areyou Michael S Bernstein. Social simulacra: Creating popu-
in a masquerade? exploring the behavior and impact of lated prototypes for social computing systems. In Pro-
large language model driven social bots in online social ceedingsofthe35thAnnualACMSymposiumonUserIn-
networks. arXivpreprintarXiv:2307.10337,2023. terfaceSoftwareandTechnology,pages1–18,2022.

[Parketal.,2023] Joon Sung Park, Joseph C O’Brien, Car- [Williamsetal.,2023] Ross Williams, Niyousha Hos-
rie J Cai, Meredith Ringel Morris, Percy Liang, and seinichimeh, Aritra Majumdar, and Navid Ghaffarzade-
Michael S Bernstein. Generative agents: Interac- gan. Epidemic modeling with generative agents. arXiv
tive simulacra of human behavior. arXiv preprint preprintarXiv:2307.04986,2023.
arXiv:2304.03442,2023.
[WooldridgeandJennings,1995] Michael Wooldridge and
[Qianetal.,2023] Chen Qian, Xin Cong, Wei Liu, Cheng NicholasR.Jennings. Intelligentagents: theoryandprac-
Yang, Weize Chen, Yusheng Su, Yufan Dang, Jiahao Li, tice. The Knowledge Engineering Review, 10:115 – 152,
Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. 1995.
Communicativeagentsforsoftwaredevelopment,2023. [Wuetal.,2023a] QingyunWu,GaganBansal,JieyuZhang,
[Ruanetal.,2023] JingqingRuan,YihongChen,BinZhang, Yiran Wu, Shaokun Zhang, Erkang Zhu, Beibin Li,
Zhiwei Xu, Tianpeng Bao, Guoqing Du, Shiwei Shi, Li Jiang, Xiaoyun Zhang, and Chi Wang. Autogen: En-
HangyuMao,ZiyueLi,XingyuZeng,andRuiZhao.Tptu: ablingnext-genllmapplicationsviamulti-agentconversa-
Large language model-based ai agents for task planning tionframework. arXivpreprintarXiv:2308.08155,2023.
andtoolusage,2023. [Wuetal.,2023b] Yuxiang Wu, Zhengyao Jiang, Akbir
[RussellandNorvig,2009] StuartRussellandPeterNorvig. Khan,YaoFu,LauraRuis,EdwardGrefenstette,andTim
ArtificialIntelligence: AModernApproach. PrenticeHall Rockta¨schel. Chatarena: Multi-agent language game en-
vironmentsforlargelanguagemodels. GitHubrepository,
Press,USA,3rdedition,2009.
2023.
[Shinnetal.,2023] NoahShinn, FedericoCassano, Edward
[Xietal.,2023] Zhiheng Xi, Wenxiang Chen, Xin Guo,
Berman, Ashwin Gopinath, Karthik Narasimhan, and
Wei He, Yiwen Ding, Boyang Hong, Ming Zhang, Jun-
ShunyuYao. Reflexion: Languageagentswithverbalre-
zhe Wang, Senjie Jin, Enyu Zhou, Rui Zheng, Xiaoran
inforcementlearning,2023.
Fan, Xiao Wang, Limao Xiong, Yuhao Zhou, Weiran
[Sumersetal.,2023] Theodore R Sumers, Shunyu Yao, Wang, Changhao Jiang, Yicheng Zou, Xiangyang Liu,
Karthik Narasimhan, and Thomas L Griffiths. Cogni- Zhangyue Yin, Shihan Dou, Rongxiang Weng, Wensen
tive architectures for language agents. arXiv preprint Cheng,QiZhang,WenjuanQin,YongyanZheng,Xipeng
arXiv:2309.02427,2023. Qiu,XuanjingHuang,andTaoGui. Theriseandpotential
oflargelanguagemodelbasedagents: Asurvey,2023.
[Tangetal.,2023] Xiangru Tang, Anni Zou, Zhuosheng
Zhang, Yilun Zhao, Xingyao Zhang, Arman Cohan, and [Xiaoetal.,2023] Bushi Xiao, Ziyuan Yin, and Zixuan
MarkGerstein.Medagents:Largelanguagemodelsascol- Shan. Simulating public administration crisis: A novel
laboratorsforzero-shotmedicalreasoning,2023. generative agent-based simulation system to lower tech-
nologybarriersinsocialscienceresearch. arXivpreprint
[Wangetal.,2021] Zijie J. Wang, Dongjin Choi, Shenyu
arXiv:2311.06957,2023.
Xu, and Diyi Yang. Putting humans in the natural lan-
guageprocessingloop: Asurvey,2021. [Xieetal.,2023] Tianbao Xie, Fan Zhou, Zhoujun Cheng,
Peng Shi, Luoxuan Weng, Yitao Liu, Toh Jing Hua, Jun-
[Wangetal.,2023a] KuanWang, YadongLu, MichaelSan-
ningZhao,QianLiu,CheLiu,etal. Openagents:Anopen
tacroce, Yeyun Gong, Chao Zhang, and Yelong Shen.
platform for language agents in the wild. arXiv preprint
Adaptingllmagentsthroughcommunication,2023.
arXiv:2310.10634,2023.
[Wangetal.,2023b] Lei Wang, Chen Ma, Xueyang Feng, [Xiongetal.,2023] KaiXiong,XiaoDing,YixinCao,Ting
ZeyuZhang,HaoYang,JingsenZhang,ZhiyuanChen,Ji-
Liu, and Bing Qin. Examining inter-consistency of large
akaiTang,XuChen,YankaiLin,WayneXinZhao,Zhewei
language models collaboration: An in-depth analysis via
Wei,andJi-RongWen. Asurveyonlargelanguagemodel
debate,2023.
basedautonomousagents,2023.
[Xuetal.,2023a] Lin Xu, Zhiyuan Hu, Daquan Zhou,
[Wangetal.,2023c] Shenzhi Wang, Chang Liu, Zilong Hongyu Ren, Zhen Dong, Kurt Keutzer, See Kiong Ng,
Zheng,SiyuanQi,ShuoChen,QisenYang,AndrewZhao, and Jiashi Feng. Magic: Investigation of large language
ChaofeiWang,ShijiSong,andGaoHuang.Avalon’sgame model powered multi-agent in cognition, adaptability, ra-
of thoughts: Battle against deception through recursive tionalityandcollaboration,2023.
contemplation. arXivpreprintarXiv:2310.01320,2023.
[Xuetal.,2023b] Yuzhuang Xu, Shuo Wang, Peng Li,
[Weietal.,2022] Jason Wei, Xuezhi Wang, Dale Schuur- Fuwen Luo, Xiaolong Wang, Weidong Liu, and Yang
mans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Liu. Exploringlargelanguagemodelsforcommunication
Denny Zhou, et al. Chain-of-thought prompting elicits games: An empirical study on werewolf. arXiv preprint
reasoning in large language models. Advances in Neural arXiv:2309.04658,2023.
InformationProcessingSystems,35:24824–24837,2022.
[Xuetal.,2023c] Zelai Xu, Chao Yu, Fei Fang, Yu Wang,
[Weng,2023] Lilian Weng. Llm powered au- andYiWu. Languageagentswithreinforcementlearning
tonomous agents. https://lilianweng.github.io/posts/ for strategic play in the werewolf game. arXiv preprint
2023-06-23-agent/,2023. arXiv:2310.18940,2023.

[Yaoetal.,2023] ShunyuYao,DianYu,JeffreyZhao,Izhak
Shafran, Thomas L. Griffiths, Yuan Cao, and Karthik
Narasimhan.Treeofthoughts:Deliberateproblemsolving
withlargelanguagemodels,2023.
[Yuetal.,2023] BangguoYu,HamidrezaKasaei,andMing
Cao. Co-navgpt: Multi-robotcooperativevisualsemantic
navigationusinglargelanguagemodels,2023.
[Zhangetal.,2023a] An Zhang, Leheng Sheng, Yuxin
Chen, Hao Li, Yang Deng, Xiang Wang, and Tat-Seng
Chua. Ongenerativeagentsinrecommendation,2023.
[Zhangetal.,2023b] Ceyao Zhang, Kaijie Yang, Siyi Hu,
Zihao Wang, Guanghe Li, Yihang Sun, Cheng Zhang,
Zhaowei Zhang, Anji Liu, Song-Chun Zhu, et al. Proa-
gent: Building proactive cooperative ai with large lan-
guagemodels. arXivpreprintarXiv:2308.11339,2023.
[Zhangetal.,2023c] Hongxin Zhang, Weihua Du, Jiaming
Shan, Qinhong Zhou, Yilun Du, Joshua B Tenenbaum,
Tianmin Shu, and Chuang Gan. Building cooperative
embodied agents modularly with large language models.
arXivpreprintarXiv:2307.02485,2023.
[Zhangetal.,2023d] Jintian Zhang, Xin Xu, and Shumin
Deng.Exploringcollaborationmechanismsforllmagents:
Asocialpsychologyview,2023.
[Zhangetal.,2023e] Junjie Zhang, Yupeng Hou, Ruobing
Xie,WenqiSun,JulianMcAuley,WayneXinZhao,Leyu
Lin, and Ji-Rong Wen. Agentcf: Collaborative learning
with autonomous language agents for recommender sys-
tems,2023.
[Zhaoetal.,2023] Qinlin Zhao, Jindong Wang, Yixuan
Zhang, Yiqiao Jin, Kaijie Zhu, Hao Chen, and Xing Xie.
Competeai: Understanding the competition behaviors in
largelanguagemodel-basedagents,2023.
[Zhengetal.,2023] Zhiling Zheng, Oufan Zhang, Ha L.
Nguyen, Nakul Rampal, Ali H. Alawadhi, Zichao Rong,
TeresaHead-Gordon,ChristianBorgs,JenniferT.Chayes,
andOmarM.Yaghi. Chatgptresearchgroupforoptimiz-
ing the crystallinity of mofs and cofs. ACS Central Sci-
ence,9(11):2161–2170,2023.
[Zhouetal.,2023a] Wangchunshu Zhou, Yuchen Eleanor
Jiang, LongLi, JialongWu, TiannanWang, ShiQiu, Jin-
tian Zhang, Jing Chen, Ruipu Wu, Shuai Wang, et al.
Agents: An open-source framework for autonomous lan-
guageagents. arXivpreprintarXiv:2309.07870,2023.
[Zhouetal.,2023b] Xuhui Zhou, Hao Zhu, Leena Mathur,
Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-
Philippe Morency, Yonatan Bisk, Daniel Fried, Graham
Neubig,andMaartenSap. Sotopia: Interactiveevaluation
forsocialintelligenceinlanguageagents,2023.
[Ziemsetal.,2023] Caleb Ziems, Omar Shaikh, Zhehao
Zhang, William Held, Jiaao Chen, and Diyi Yang. Can
largelanguagemodelstransformcomputationalsocialsci-
ence? ComputationalLinguistics,pages1–53,2023.
