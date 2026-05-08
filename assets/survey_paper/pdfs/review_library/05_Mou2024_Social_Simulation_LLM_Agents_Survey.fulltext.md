Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/review_library/05_Mou2024_Social_Simulation_LLM_Agents_Survey.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:22+00:00
- page_count: 35
- status: ok
- text_char_count: 167567

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Background (page 3)
  - Large Language Model-based Agents (page 3)
  - Multi-agent Systems (page 3)
- Individual Simulation (page 3)
  - Architecture (page 3)
    - Profile (page 5)
    - Memory (page 5)
    - Planning (page 5)
    - Action (page 6)
  - Construction (page 6)
    - Nonparametric Prompting (page 6)
    - Parametric Training (page 6)
  - Simulation Objectives (page 7)
    - Demographics (page 7)
    - Characters (page 7)
  - Evaluation (page 7)
    - Static Evaluation (page 7)
    - Interactive Evaluation (page 8)
- Scenario Simulation (page 9)
  - System (page 9)
    - Environment (page 9)
    - Role (page 11)
    - Organization (page 11)
    - Communication (page 12)
  - Scenario (page 12)
    - Dialog-Driven Scenario (page 12)
    - Task-Driven Scenario (page 13)
  - Evaluation (page 13)
- Society Simulation (page 14)
  - Social Construction Elements (page 14)
    - Composition (page 14)
    - Network (page 16)
    - Social Influence (page 16)
    - Outcomes (page 17)
  - Scenario (page 17)
    - General Economics (page 17)
    - Sociology and Political Science (page 17)
    - Online Platform (page 18)
  - Evaluation (page 18)
- Datasets and Benchmarks (page 19)
  - Individual Simulation (page 19)
  - Scenario Simulation (page 19)
  - Social Simulation (page 19)
- Trend of Social Simulations (page 19)
  - Trend of Individual Simulation (page 19)
    - Coarse Simulation on Superficial Features (page 22)
    - More Nuanced Simulation on Specific Characters (page 22)
    - Situation-Oriented Simulation (page 22)
  - Trend of Scenario Simulation (page 23)
    - Simple Scenario (page 23)
    - Multi-Stage Scenario (page 23)
    - Collaborative Scenario (page 23)
  - Trend of Society Simulation (page 23)
    - Constructing Preliminary Environments (page 24)
    - Exploring Alignment on Specific Scenarios (page 24)
    - Scaling Up and towards Multi-Modal (page 24)
- Conclusion (page 24)

Markdown Content:

From Individual to Society: A Survey on Social Simulation Driven by Large
Language Model-based Agents
XinyiMou1∗, XuanwenDing2∗, QiHe1∗, LiangWang3∗,
JingcongLiang1, XinnongZhang1, LiboSun1, JiayuLin1,
JieZhou2, XuanjingHuang1 and ZhongyuWei1,4†
1FudanUniversity
2EastChinaNormalUniversity
3HarbinInstituteofTechnology,Shenzhen
4ShanghaiInnovationInstitute
zywei@fudan.edu.cn
Abstract totesttheoreticalhypotheses,understandsocialphenomena,
and predict collective outcomes. While these methods can
Traditionalsociologicalresearchoftenreliesonhu-
provide highly authentic data, they are expensive, challeng-
man participation, which, though effective, is ex-
ingtoscale,andinvolvecertainethicalrisks.
pensive,challengingtoscale,andwithethicalcon-
Recently, large language models (LLMs) have demon-
cerns. Recent advancements in large language
stratedimpressive capabilitiesinhuman-level reasoningand
models (LLMs) highlight their potential to simu-
planning [5–9]. They can perceive the environment, make
latehumanbehavior,enablingthereplicationofin-
decisions, and take corresponding actions, showcasing their
dividualresponsesandfacilitatingstudiesonmany
potentialasautonomousagentsthatcanserveashumansub-
interdisciplinary studies. In this paper, we con-
stitutes. In appropriate settings, LLM-driven agents can ac-
duct a comprehensive survey of this field, illus-
curately simulate responses from corresponding individuals
trating the recent progress in simulation driven by
byleveragingtheirrole-playingabilities[10,11],aproperty
LLM-empowered agents. We categorize the sim-
known as algorithmic fidelity [12, 13]. This characteristic
ulations into three types: (1) Individual Simula-
makesLLM-drivenagentshighlyvaluableinsimulatinghu-
tion, which mimics specific individuals or demo-
man behavior. By reproducing individual response patterns
graphic groups; (2) Scenario Simulation, where
inspecificscenarios, LLM-drivenagentshelpresearchersto
multipleagentscollaboratetoachievegoalswithin
betterunderstand,validate,andpredicthumanreactions.
specificcontexts;and(3)SocietySimulation,which
Just as individuals do not exist independently within so-
models interactions within agent societies to re-
ciety, in addition to separate individual agents, interactions
flect the complexity and variety of real-world dy-
between multiple agents have also been widely studied to
namics. These simulations follow a progression,
solvespecificproblemsorsimulatecomplexdynamicsinthe
rangingfromdetailedindividualmodelingtolarge-
real world [14, 15]. On one hand, LLMs can be special-
scale societal phenomena. We provide a detailed
ized as agents with detailed knowledge and skills, leverag-
discussion of each simulation type, including the
ingcollectiveintelligencetosolvecomplexproblems,suchas
architecture or key components of the simulation,
softwaredevelopment[16,17],automaticdiagnosis[18,19]
theclassificationofobjectivesorscenariosandthe
andjudicialdecision-making[20]. Inthiscase, multipleau-
evaluationmethod.Afterward,wesummarizecom-
tonomous agents collaborate on planning, discussion, and
monly used datasets and benchmarks. Finally, we
decision-making, reflectingthecooperativenatureofhuman
discuss the trends across these three types of sim-
groupswhensolvingproblems. Ontheotherhand,simplein-
ulation. A repository for the related sources is at
teractionsbetweenmultipleagentscanleadtotheemergence
https://github.com/FudanDISC/SocialAgent.
ofcomplexcollectivebehaviorsorpatterns[21–23],thereby
replicating complex social dynamics in the real world, such
1 Introduction asopiniondynamics[24–26]andmacroeconomicsphenom-
ena[27]. Suchsimulationsprovidevaluabletoolsforunder-
Socialscienceinvestigateshumanbehaviorandsocialstruc-
standing,analyzing,andpredictingcomplexphenomenathat
tures to understand how societies function. Traditional so-
maybedifficultorimpracticaltoobservedirectlyinreallife,
ciological research heavily relies on human participation to
offeringstrongsupportfordecision-makinginareassuchas
conduct experiments and gather data. Questionnaires [1, 2]
policy-makingandsocialmanagement.
and psychological experiments [3, 4] are commonly used
Thisresearchfieldisrapidlyexpanding,withpapersfocus-
∗Theseauthorscontributedequally. ingonvariousaspects.Consideringthepurposeofsimulation
†Correspondingauthor. and the varying demands for diversity, scale, and accuracy
4202
ceD
4
]LC.sc[
1v36530.2142:viXra

Demand for Precision of Individual Simulation
Sharing
Opinions
Epidemic
Name: David Modeling
Gender: Male
Age: 29
Finishing a
Race: White Morning Routine
Occupation: Engineer
…
Profile Memory Environment Role Composition Network
Planning Action Organization Communication Social Influence Outcomes
Individual Simulation
Scenario Simulation
Society Simulation
Demand for Diversification and Scale of Individual Simulation
Figure1: IllustrationofsimulationsempoweredbyLLM-drivenagents. Wecategorizethesimulationsintoindividualsimulation,scenario
simulationandsocietysimulation. Fromlefttoright, thediversityandscaleofindividualmodelinggenerallyincrease. Conversely, from
righttoleft,thegranularityofindividualmodelingbecomesmorerefined.
inindividualmodeling,wecategorizetheexistingworkinto Although this field has seen rapid growth, with some sur-
threetypes,asillustratedinFigure1: veyssummarizingagentarchitectures[7,9,15]orcertainas-
pects of single-agent ability or multi-agent systems [11, 14,
1. Individual Simulation: leveraging LLM-based agents
34],thereisanabsenceofasystematicreviewtosummarize
tomimicspecificindividualsorgroupsofpeoplesharing
theworkfromtheindividualtosociety,providingacompre-
commondemographiccharacteristics[10,11,28]. This
hensive blueprint for this field. This motivates us to present
lineofresearchfocusesonthereplicationoffeaturesof
this survey, aiming to contribute to the research and devel-
a single person, e.g., personality, and has not involved
opmentofsimulationsdrivenbyLLM-basedagents, aswell
multi-agentinteractions.
asawiderrangeofinterdisciplinarystudies. Tocomprehen-
2. ScenarioSimulation: organizingagroupofagentsina sivelydescribeourlandscape,weorganizeoursurveyasfol-
concentratedscenario,drivenbyspecificgoalsortasks, lows. After a brief introduction to the background in § 2,
suchassoftwaredevelopment[16,17],questionanswer- webeginin §3bydetailinghowtoconductindividualsim-
ing [29] and paper reviewing [30]. Such simulations ulationthroughdiscussionsof(1)thearchitectureofasingle
areusuallyfocusedonsmall-scaleagentswithinspecific agent, (2) construction method of individual simulation, (3)
scenarios,emphasizingthecollectivewisdomofagents theclassificationofobjectives,and(4)theevaluationofindi-
withspecializedexpertise. vidualsimulation. Next,in §4,wesummarizescenariosim-
ulation, including (1) the elements that constitute a scenario
3. Society Simulation: simulating more complex and di-
simulationsystem,(2)theclassificationofscenarios,and(3)
verse behaviors in the agent society to explore so-
theevaluationofscenariosimulation,exploringhowmultiple
cial dynamics in real-world applications. Such simu-
agents collaborate to achieve objectives within a single sce-
lations could test social science theories within a small
nario.Followingthis,in §5,weintroducesocietysimulation,
scope [31] or populate virtual spaces and communities
examining how multi-agent systems can construct complex
withlarge-scalerealisticsocialphenomena[32,33].The
socialdynamicsthrough(1)thesocialconstructionelements
composition of individuals in such simulations is more
ofsocietysimulation,(2)theclassificationofsocietysimula-
complexanddiverse.
tionscenarios,and(3)theevaluationofsocietysimulation.In
Thesethreetypesofsimulationsexhibitaprogressiverela- §6,wesummarizeexistingdatasetsandbenchmarks. Based
tionship. Individualsimulationmodelsaspecificpersonora on the earlier sections, we analyze trends in these three as-
typeofperson,servingasthefoundationforscenariosimula- pectsin §7andpresenttheconclusionin §8.
tionandsocietysimulation. Theoretically,societysimulation
can encompass a chaotic world composed of countless sub-
scenarios,thoughcurrentworkfocusesonspecificscenarios.

Construction Objective
Prompting Training Characters Demographics
Architecture
Profile Memory Planning Action
Evaluation
Level Strategy
Static Interactive Subjective Objective
Support
Promptengineering Pre-training Virtual Real
“Youareanexpert…” Finetuning
“Youareahelpfulassistant…” Reinforcementlearning
Integrate
Construction Type Type Situation
manual,LLMgeneration short-term,long-term empatheticplanning dialogue,caftedsituation
Form Operation Domain
subjectiveplanning
descriptions,conversaions writing,retrieval,reflection closed,opendomain
Evaluate
Figure2:Illustrationofindividualsimulationblueprint.Anindividualagentistypicallycomposedofanarchitecturewithmodulesinvolving
profile,memory,planning,andactionthroughconstructionmethod,promptingortraining,tosimulatespecificobjectiveslikecharactersor
demographics.Individualsimulationcanbeevaluatedstaticallyandinteractivelywithdifferentdimensionsbeingobserved.
2 Background as distinct tasks. These agents can be organized in various
ways, such as layered or centralized structures [48–50], and
cancommunicatethroughdifferentmethods[51–53]. These
2.1 LargeLanguageModel-basedAgents factorssignificantlyinfluencetheeffectivenessandefficiency
ofmulti-agentinteractions.
Benefiting from the large-scale parameters and pre-training
onvastamountsofdata,therecentlyemerginglargelanguage
models have shown great potential in achieving human-like 3 IndividualSimulation
intelligence[6,35,36].Thishassparkedariseintheresearch
of LLM-empowered agents, where the key idea is to equip
theLLMswithhumancapabilitiessuchasmemory[37,38], Individual simulation focuses on designing a modular ar-
planning[39,40]andtoolusage[41,42]. Thememorymod- chitecturethatintegratesindividualizeddatafortheconstruc-
ule enables agents to store and operate historical informa- tionofagentsandsimulatingthespecificobjectivewithhigh
tion to facilitate future actions. Memory of different struc- fidelity. Inthissection,wefirstoutlinethebasicarchitecture
tures[32,43]andformats[44,45]havebeenintegratedinto oftheagentintheindividualsimulationwithfourkeycompo-
LLM-basedagents. Theplanningmodulehelpsagentstode- nentsin§3.1. Then,twoconstructionmethodsarediscussed
composecomplextasksintosubtasks,wherevariousplanning in §3.2 to implement the integration of individualized data
strategies[5,39]areadopted. Thetool-usagemoduleallows into objectives introduced in §3.3. The evaluation methods
agentstomakeuseofexternaltoolsorresources[39,46]to areexaminedfromdifferentperspectivesin§3.4. Theoverall
solvetasks. Overall,thesemodulesassistagentsinoperating frameworkispresentedinFigure2andrepresentativeworks
moreeffectivelyincomplexanddiverseenvironments. aresummarizedinTable1.
2.2 Multi-agentSystems
3.1 Architecture
Torealizecomplexscenarios,asingleagentisneverenough.
A system where interaction between multiple agents is in- Toeffectivelyaccomplishindividualsimulation,itisessential
volved is referred to as a multi-agent system (MAS). The to construct an agent architecture that can accurately repli-
agents may have a common goal, such as working together cate the features of the individual. This requires a balance
to accomplish a task [16, 17] or solve a problem [29], or betweentheoreticalabstractionandpracticalimplementation
theymayjusthaveself-interestedgoalsthatcancausethemto tocapturethecomplexityofhumanbehaviors. Typically,this
competeforlimitedresources[47]. Inamulti-agentsystem, architectureismodularizedintofourcorecomponents: pro-
each agent may be assigned distinct roles and skills, as well file,memory,planning,andaction.

Aritecture
Objectives Paper Construtction
Profile Memory Planning ActionDomain
Brahmanetal.[54] Dialogue/Description Short-term - Open/Closed Parametric
Parametric /Non-
Chenetal.[55] Dialogue/Description Short-term - Open
parametric
Schwitzgebeletal.[56] Dialogue Short-term - Open Parametric
GenerativeAgents[57] Description Short/Long-term - Open Nonparametric
Agrawaletal.[58] Dialogue/Description Short-term - Open Parametric
ChatHaruhi[59] Dialogue Short-term - Open Parametric
LiveChat[60] Dialogue/Description Short/Long-term - Open/Closed Parametric
RoleLLM[28] Description/Dialogue Short-term - Open/Closed Parametric
Characters CharacterLLM[10] Description Short-term Subjective Open Parametric
InCharacter[61] - Short-term - Open/Closed -
CharacterGLM[62] Description/Dialogue Short-term - Open Parametric
RoleEval[63] Description Short-term - Closed Parametric
CharacterEval[64] Dialogue Short-term - Open Nonparametric
Neeko[65] Description Short-term - Open Parametric
CharacterisDestiny[66] Description Short/Long-term - Closed Nonparametric
Yuanetal.[67] Description Short-term - Open/Closed Nonparametric
CapturingMinds[68] Description/Dialogue Short/Long-term Subjective Open/Closed Parametric
MMRole[69] Description Short-term - Open Parametric
Yuetal.[70] Dialogue Short-term - Open Parametric
Rationalsensibility[71] - Short-term Empathetic Closed Parametric
Karraetal.[72] Dialogue/Description Short-term - Closed Parametric
Jiangetal.[73] Description Short-term - Closed Nonparametric
Liuetal.[74] Description Short/Long-term - Open Parametric
OutofOne,Many[12] Description Short-term - Open Nonparametric
SimulatedEconomic Description Short-term - Closed Nonparametric
Agents[75]
Thewallstreetneophyte Description Short-term Empathetic Closed Nonparametric
[76]
ToxicityinChatGPT[77] Description Short-term - Open Nonparametric
Songetal.[78] Description Short-term - Closed Nonparametric
MarkedPersonas[79] Description Short-term - Open Nonparametric
Wangetal.[80] Description Short/Long-term - Open Nonparametric
Serapio-Garc´ıaetal.[81] Description Short-term - Open Nonparametric
Huangetal.[82] Description Short-term - Closed Nonparametric
CharacterChat[83] Description Short/Long-term - Open Nonparametric
Conversationalhealth Description Short/Long-term Empathetic Open Nonparametric
agents[84]
Demographics Chenetal.[85] Description Short/Long-term - Closed Nonparametric
EconAgent[86] Description Short/Long-term - Open Nonparamaetric
Sheaetal.[87] Dialogue Short-term - Open Parametric
BeSelfish,ButWisely[88] Dialogue Short-term - Open Parametric
ChainofEmpathy[89] - Short-term Empathetic Open Nonparametric
BiasRunsDeep[90] Description Short-term - Open Nonparametric
Lietal.[91] Dialogue Short-term - Open Parametric
Xieetal.[92] Description Short-term Subjective Closed Nonparametric
Leeetal.[93] Description Short-term - Closed Nonparametric
CultureLLM[94] Dialogue Short-term - Open Parametric
ControlLM[95] - Short/Long-term - Open Nonparamatric
RandomSiliconSampling Description Short-term - Closed Nonparametric
[96]
Bisbeeetal.[97] Description Short-term - Closed Nonparametric
PersonaHub[98] Description Short-term - Open Parametric
Quetal.[99] Description Short-term - Closed Nonparametric
InteractiveAgents[100] Description Short-term - Open Nonparametric
Table1:Alistofrepresentativeworksofindividualsimulation.

3.1.1 Profile ing scene descriptions [58, 76] and scene-related experi-
Profile differentiates the unique characteristics of simulated ences [10, 66], which navigate agents through the simula-
individuals, encompassing attributes, behaviors, and con- tiontoperformtasksappropriately.Long-termmemorystores
straints. The profiles differ in the ways of construction and persistentglobalinformation,preventingdeviationsfromin-
theirforms. tended goals, which holds extensive individual-specific in-
formation stably, including past experiences and behaviors,
ProfileConstruction Profileconstructionreferstothepro-
currentknowledge,andskills[66,86]. Withtheproposalof
cess of collecting individual-related information, which can
using the vector database as the long-term memory hub, the
becategorizedintomanualmodificationandLLMgeneration.
management, retrieval, and organization of memory is more
Manual modification takes advantage of publicly available
effective[108].
data to create high-quality profiles through a human-guided
process. According to the collected sources, manual mod- MemoryOperation Memoryoperationsstandforthecon-
ification can also be classified into three categories: hand- tinuous updating and utilization of memory by the agent.
crafting, online communities, and historical works. Hand- Thecommonmemoryoperationsincludethreetypes,namely
crafting manually organized some coarse strength informa- memorywriting,memoryretrieval,andmemoryreflection.
tion, such as well-known characters [101] and specific per- Memorywritingaimstoincorporatetherelevanthistorical
sonalities [77, 79], while online communities construct pro- contentintothememory. Thisprocessmirrorshumanmem-
files built on the web data like Wikipedia [10] and social oryformation,whereusefulinformationisretainedforfuture
media [60], where the profile implicitly exists in conversa- retrieval. Thememoriestobewrittenvaryfromuser-specific
tionsandmaterials. Inaddition,literaryworksserveasaddi- dialogue history [103], new skills [109], to selected papers
tionaldescriptionsthatreflecttheauthor’sthoughts[56]and andotherforms[110].
characters in the storyline [54, 59]. LLM generation auto- Memory retrieval serves to extract valuable content from
matically generates the expected persona-based information memorybasedoncustomizedrequirements. Theoverallper-
profiles by prompting LLMs with essential individual de- formance of the individual simulation highly relies on the
tails[28,61,83]. Thismethodexploresdiverseprofileswith effectiveness of memory retrieval since simulations are sen-
ease,whilethequalityneedshumansupervisionwithcaution. sitive to the context. Traditional retrieval technologies rely
on similarity such as keyword matching [111] and embed-
ProfileForm Profileformdefinestheformatofindividual
dingvectors[108],whilerecentworksintroducetheretrieval
information, which can be categorized into descriptions and
modeltoselectthemostrelevantinformation[112,113].
conversations.Descriptionsdirectlydescribebasicindividual
Memory reflection mirrors the human ability to recon-
informationoridentitywithdetailslikename,age,andgen-
sider past behaviors and opinions. Specifically, it helps the
der[101,102]. Whiledescriptionscanintuitivelyreflectthe
agenttoorganize,refine,andelevatememoriesintomoreab-
basic attributes of an individual, deeper contextual informa-
stractandinsightfulconcepts. GenerativeAgents[57]main-
tioncanalsobeignored. Onthecontrary,conversationsim-
tains a comprehensive record of agents’ experiences with a
plicitlyreflectthecharacterprofilethroughdialogue. Asub-
tree-structuredreflectionprocesstooptimizememoryusage.
stantialamountofconversationaldataisderivedfromsources
ProAgent [114]incorporates memoryreflection withvalida-
such as films, literary works, and scripts [54, 70, 103, 104].
tionandbeliefcorrectiontoimprovetheagent’splanningand
Considering the extensive commonsense knowledge learned
decision-making. Voyager [109] allows agents to reflect on
by LLMs in the pre-training stage, recent works leverage
their behavior and update their skill libraries through self-
LLMs to generate individual dialogues [59, 98], which de-
verification. Although the application scenarios of memory
finestheartisticgenrethroughsixessentialelementstogen-
reflectionarestilllimited,itshowsgreatimprovementinen-
eratedetaileddramascripts[105]andimitatesspeakingstyles
hancingperformanceandincreasingthedepthofsimulations,
throughcontextlearning[28,65].
especiallyincomplexenvironments.
3.1.2 Memory 3.1.3 Planning
Memoryisdesignedtostoreperceivedorgeneratedinforma- Planning is the process of deciding on a series of actions
tion, helping agents maintain consistency and continuity of aimedatachievingspecificgoals. Traditionalplanningtasks
behaviorandovercomethelimitedcontextwindowofLLMs. typicallyfocusonsolvingparticularproblems,suchasmathe-
Consideringthecomplexityofmemory,researchersstruggle maticalreasoning[115]orembodiedtasks[116,117]. Atthe
todesignmoreefficientmemorytypesandoperations. individual simulation level, however, agents are expected to
gobeyondmereproblem-solving.Theyshouldalsobeableto
Memory Type Based on the temporal span of stored
simulatepersonalizedthinkingandemotionalresponsesdur-
content, memory can be commonly divided into two
inginteractionswithspecificindividuals. Thisextendsplan-
types, namely short-term memory and long-term mem-
ningintotwoadditionalcategories: empatheticplanningand
ory. Short-term memory records the instant local infor-
subjectiveplanning.
mation that the agent perceives, which can be further di-
vided into simulation contents and simulation supplements. Empathetic planning Empathetic planning refers to an
Simulation contents include essential interaction data like agent’s ability to infer and perceive the behavior and emo-
user instructions [56, 77], dialogue history [106, 107], tionsofothersbeforetakingaction. ItinvolvesusingChain-
and user/environment responses [76]. Simulation supple- of-Thought (CoT) reasoning to understand the situations of
ments provide additional environmental information includ- othersandmakeadaptivedecisionsorjudgments[71,76,89].

This allows the agent to tailor its actions based on the emo- lect specific functions to complete concrete tasks, like rec-
tionalandbehavioralcontext,guidingtheacquisitionofper- ommending,browsing,andcompiling. Individualsimulation
sonalizedfeedback. withagentsinclosed-domaintaskscanimprovehumanwork
efficiency,extendingbeyondentertainmentpurposes.
Subjective planning Subjective planning refers to the ac-
Opendomainsimulationplacesfewrestrictionsonactions,
tions an agent takes based on its own thoughts and feelings,
allowing LLMs to generate responses freely. This approach
in line with its predefined role or identity. This can involve
more closely resembles real-world conditions, but also de-
utilizinginnermonologuesfromsimulatedcharacterstofine-
mands higher standards for individual simulation. Among
tuneLLMs[10,68]orusingCoTtoguideLLMstoexpress
various open-domain tasks, taking actions through conver-
themselvesaccordingtotheirownbeliefs[92]. Thisformof
sation is a popular method for simulating individual behav-
planningisdrivenbytheagent’sinternalstate,ratherthanby
ior [54, 59, 62, 65], in which the varied settings stimu-
externalstimuliortheneedsofothers.
late LLMs’ potential for individual simulation and allow re-
3.1.4 Action searchers to oversee simulations across diverse and nuanced
ActionreferstothedirectinteractionbetweenLLMsandtheir dimensions. Anothergrowingmethodofopen-domainsimu-
environment. Action encompasses two key aspects: the ac- lationisscenario-basedinteraction,whereLLMsareassigned
tion situation, which describes the context in which actions rolesandarerequiredtointeractincratedsituationslikesand-
occur,andtheactiondomain,whichdefinestherequirements box[108,109]orestablishedgamesettings[119,121].
foractionspace. Actionservesastheinterfaceforsimulating
3.2 Construction
humanbehavior,allowingLLMstoexecutetasksthatmimic
real-world actions and responses. This interaction enables a Construction indicates the process of integrating individual
deeperunderstandingofhuman-likedecision-makingandex- data into the established model of LLMs, which aligns the
ecutioninvariousscenarios. design model and the individual, thus creating the simu-
lating LLMs. Generally, construction methods are distin-
Action Situation With individual simulations focusing on
guished into two types, namely nonparametric prompting
more and more diverse and complicated situations, various
andparametrictraining.
action situations spring out accordingly, ranging from dia-
logue [118], games [119], real word [106], etc. Typically, 3.2.1 NonparametricPrompting
action situations can be divided into simple dialogues and
Nonparametric prompting, i.e. prompt engineering, is a
craftedsituations.
method of interacting with LLMs by designing and opti-
Simple dialogues are few-turn conversations without re-
mizing input prompts. In some individual simulations, the
stricted environments, such as constructing dialogues be-
description-basedprofileisimplementedbyasystemprompt.
tween two characters [54]. Recent researches utilize sim-
Researchersoftencreatesystempromptsthatbeginwith“You
pledialoguestoinducepotentialattributeswithinthemodels,
area...”toassignmodelsspecificdemographicfeaturesand
involving personality [72, 73], traits [81] and toxicity [77].
roles [77]. Besides, LLM outputs are enhanced in some
Other works conduct evaluations of persona with interview-
worksthroughfew-shotpromptingbyprovidingspecificex-
ing [61] or questionnaire [120] with simple dialogues to fa-
amples to inject detailed information and improve response
cilitatetheirexperiment.
quality. Moreover,incorporatingproblem-specificdetailsdi-
Crafted situations are elaborately designed environments rectlywithinpromptstructurescansignificantlyenhancethe
includingdetailedrulesandsurroundingdescriptions. Com- effectivenessofthesimulation.
mon situations like games are modified from simple dia-
Short-termmemoryisoftenimplementedbynonparamet-
logues. They leverage game rules to provide a settled vir-
ricprompting.Forsituation-basedindividualsimulations,en-
tual topic for both users and agents to play in, especially in
vironmentdescriptionsandbehaviorrulesaretypicallycon-
the board role-playing games [119, 119] [121]. Besides, re-
veyed through prompt engineering [121]. Since situational
searchershavedevelopedamoredelicateenvironmentcalled
informationisgenerallyobjectiveandmustbefollowed,em-
sandbox[111],whichnotonlyincludesrulesbutestablishan
phasizingthisinformationdirectlyintheinputisaratheref-
objectiveenvironment. Tofurtherenrichtheindividualsimu-
fective method for constructing simulations. However, due
lationsituation,someauthorsaddsomeelementsexistingin
to the context window limitations of LLMs, the quality of
scriptslikefacialexpression,tinymovements[58,105],and
the profile prompt significantly restricts prompt-based indi-
nuancedinformationfromenvironmentimages[69].
vidualsimulations. Moreover,thepresettemplateconfigura-
Action Domain The Action domain can be commonly di- tionsasthe“assistant”withinLLMsposeamajorchallenge
vided into close domain and open domain based on the re- forpromptengineeringinindividualsimulations[83].
strictionofactionspace.
3.2.2 ParametricTraining
Closed domain simulation occurs when the available ac-
Parametric training modifies the model by directly updating
tionspaceislimited. Insimplesituationssuchascompleting
the LLM parameters with given data. The training methods
questionnaires testing [72], making decisions from a set of
canbegenerallycategorizedintopre-training,finetuning,and
options[75],orratingwithpredefinedstandards[61],theac-
reinforcementlearning.
tion space of LLMs is determined by researchers ahead of
simulation to make responses predictable. In practical sce- Pre-training The pre-training method in individual sim-
narios, LLMs are required to choose tools [112, 122] or se- ulation focuses on aligning the original LLMs with basic

individual-related data and setting up a fundamental knowl- demographicsimulationscanalsocontributetosocietalsim-
edge of individuals for LLMs. The targets of training ulationstudies[111]. Inmostcases,demographicsimulation
datasets vary in recent studies, including individual descrip- isimplementedthroughnonparametricprompting. Manyre-
tions [113], literature summaries [54], and philosophical searchersinthisfieldfocusondesigningtasks,suchasques-
worksorutterances[56]. tionnairesorsocialexperiments[75],tofullytapintothesim-
ulatingpotentialofLLMs.
Finetuning The finetuning method is designed for adapt-
ing LLMs for individual simulation in specific tasks and
3.3.2 Characters
situations. Researchers collect and modify supervised in-
structiondatasetstailoredforspecificsituationsandfine-tune Characters are distinct individuals who differ from one an-
their models to equip them with the corresponding capabili- other.Theymaybeordinaryplatformusers,well-knownpub-
ties. Usingpersona-enhanceddatasetsisaneffectivemethod lic figures, or fictional characters from novels. Researchers
to regulate the models’ behavior in individual simulation, favor these characters because they enhance the expertise of
which is constructed by adding instruction tuning samples LLMs in specific domains and challenge the learning capa-
of the simulated individual’s behavior [68, 98]. LoRA fine- bilities of these models. From Haruhi and Li Yunlong [59]
tuning method can integrate multiple characters into a sin- toBeethoven[66],individualsimulationsselecttheirprotag-
gle model [65, 123]. In multimodal finetuning scenarios, onistsfrombothrealandvirtualworlds.
bothvisualandtextual informationareconsideredtosignif-
RealCharacters Realcharacters,typicallyfamousfigures,
icantly enhance LLMs’ simulation behavior in multimodal
are associated with high-quality data from platforms like
contexts [69, 113]. Compared to prompt engineering, fine-
Wikipediaandsocialmedia,makingiteasiertoestablishob-
tuning leverages large datasets more effectively and reduces
jective profiles and evaluate simulations. Many LLMs fo-
thelimitationsimposedbythepre-trainingphaseofLLMs.
cus on historical figures, celebrities across various periods
Reinforcement Learning The reinforcement learning and backgrounds [10, 129], characters from online encyclo-
method is used to refine models in dynamic environments pedias[64],andpopularlivestreamersonDouyin[60]. Since
with the goal of maximizing cumulative rewards. In sim- LLMsoftenhavepriorknowledgeoftheseindividuals,creat-
ulations involving conversations and dialogues, the quality ingtheirprofilesisrelativelystraightforward. Realandsim-
of the LLM’s responses directly influences the rewards it ulatedcharactersarealsousedtotestLLMsimulationcapa-
receives [87, 124, 125], which encourages the model to bilities,suchasinphilosophersimulations[56].
learn the appropriate ways to respond in dialogues. By
modifyingtherewardfunction,researcherscaninfluencethe Virtual Characters Virtual characters are fictional roles
model’s preference and thus manage to mimic the personas created in novels, movies, and video games. Advance-
of the simulated individuals [88]. As individual simulations ments in virtual character simulation can significantly ben-
become more diverse and complex, reinforcement learning efitentertainmentsectorslikethegamingindustryandtheme
plays a crucial role in improving the dynamic behavior of parks. Many researchers have drawn inspiration from fa-
simulatedLLMs. mous fictional characters, such as Harry Potter [55], Sun
Wukong [62], and Tong Xiangyu [130]. Additionally, some
3.3 SimulationObjectives experiments design virtual characters [119] with specific at-
The simulation objectives of individual simulation for vari- tributes or objectives. However, despite the attention vir-
ouspurposescanbedividedintotwocategories: (1)Demo- tualcharactersimulationattracts,developingvirtualindivid-
graphics: a group of people who share the same character- ual LLMs presents challenges, particularly in ensuring the
istics, such as psychological traits (e.g., INTJ) or identity- quality and reliability of their datasets. Most simulations of
related features (e.g., farmers). (2) Characters: a specific virtual characters are designed for interactive conversations,
individual,whetherrealorvirtual,whoiswidelyrecognized enhancinguserexperienceinvariousentertainingscenarios.
bygroupsofpeople.
3.4 Evaluation
3.3.1 Demographics
Demographicindividualsrefertoagroupofpeoplewhoshare To measure the performance of individual simulations, pro-
thesamefeatures. Inanabstractsense,demographicscanbe vide insights into their feasibility, and guide improvements
understood as the centroid of an embedding space that rep- to simulation architectures, researchers have developed di-
resents common opinions and beliefs, essentially clustering verseevaluationstandardsandmethods,rangingfromsimple
individual embeddings for classification purposes [91]. De- to complex approaches. These methods can be categorized
mographicsimulationinvolvesassigninganidentity,suchas intostaticevaluationandinteractiveevaluation.
“student,” to LLMs and guiding the simulators to perform
3.4.1 StaticEvaluation
specific tasks. Early demographic simulations have focused
on investigating the internal demographic attributes within Static evaluation refers to the dialogue-based assessment of
pre-trainedmodels[74,126],layingthegroundworkforfur- LLMs by directly inducing their generation and measuring
thersimulations. Additionally, thesesimulationsareusedto theirquality. Itcanbecategorizedintosubjectiveevaluation,
reflect opinion surveys [93] or evaluate preferences and bi- whichinvolvesassessmentsbybothLLMsandhumaneval-
ases[99,127]ofparticulargroups. Withtheabilitytoscale uators,andobjectiveevaluation,whichutilizesmathematical
syntheticdialogue[63,98,128]involvingspecificpersonas, toolsforanalysis.

Dialog-Driven Scenario Task-Driven
Integrate
System
Role Environment
Communicator Configuration
Worker
Participants
State
Directors Planner
History
Coordinator
Organization Communication
Integrator Structure Mode Format Style Tool
Evaluate
Level Evaluation Strategy
Sub-Task Task System Automatic LLM Human
Figure3:Illustrationofscenariosimulations.Givenaspecificscenario,buildingamulti-agentsysteminvolvesmodelingenvironment,roles,
organization,andcommunicationwithdetailedmodulesormechanismsadjustedtothetargetedscenariobeingsupported. Aftersimulating
thescenario,thedesiredoutput,typicallytheresultofataskorproblem,isobtainedandevaluatedusingdifferentlevelsandstrategies.
Subjective Evaluation Subjective evaluation refers to as- must be developed to facilitate the evaluation of simulation
sessments conducted by humans or LLMs based on subjec- ingivendimensions.
tivestandards.Itofteninvolvesleveragingconversationswith
varyingformsandcontexts. Interviewtechniquesarewidely
adopted [28, 61] because they can effectively prompt LLMs 3.4.2 InteractiveEvaluation
to generate expected responses. Other approaches, such as
utterance imitation [77], are also favored in some research. Interactive evaluation refers to a circumstance-based assess-
Oncedialoguesaregenerated,somestudiesutilizeadvanced ment that creates a detailed interactive environment to mea-
LLMs to evaluate the output on a given scale [61, 65, 130], suretheabilityofindividualsimulationsincomplexscenar-
considering performance dimensions. These dimensions ios. It is commonly applied in areas such as game perfor-
range from psychology-based metrics, such as the Big Five mance [119, 121], task completion [112, 135, 136], and nu-
Personality Traits (BFI) and Myers-Briggs Type Indicator anced role-playing [88, 104]. Three key features of interac-
(MBTI), to language-based factors like grammar and tone. tive evaluation are the carefully designed environment, real-
Human annotators are often involved in experiments to pro- time interactive external responses, and multi-stage assess-
videhumanreferencepoints [57,84,131]. ments. Information about the crafted environment has been
introducedin§3.1.4.Real-timeinteractiveexternalresponses
Objective Evaluation Objective evaluation refers to as- refer to the feedback from the external environment in reac-
sessmentsbasedonobjectiveindicators,utilizingmathemat- tion to the outputs of simulating LLMs. Agent-environment
ical and statistical tools. It takes advantage of mathemati- interactions construct multiple dialogues between the LLMs
cal tools to grade the generation of simulating LLMs. Ex- and the environment. These interactions help reveal the
amination commonly involves option choosing(or question- LLMs’capabilitiesincomplexcontexts,leadingtomoredy-
naire)[72], ranking[60]andquestionanswering[102]. Ac- namic simulations. Single-aspect measurements are insuffi-
curacy [91, 106], F1 score, recall [132, 133] are used in cientforinteractiveevaluation,somanystudiesadoptevalu-
option choosing and ranking. In the examination of gener- atedobjectivesthatrangefromspecificactionstohybridac-
ation(question answering), text sequence related tools such tions[110],orfromsingle-turninteractionstomulti-turndia-
as perplexity [58, 118, 134], ROUGE-L [55, 74, 106] and logues[10]. Otherstudiesassessgenerationquality,focusing
BLUE[60,74,132,134]arebroadlyusedintheevaluation, onaspectssuchasaccuracyrelativetogroundtruth,nuanced
especiallythosewithareferenceversion[55]. ObjectiveEx- simulations like tone imitation [28, 107], and self-reporting
amination is a more credible method of evaluating the per- consistency [137]. In interactive evaluation, researchers pri-
formance of LLMs in individual simulation. However, it is oritizenotonlyaccuracybutalsothedegreetowhichthesim-
highly restricted, and occasionally, specific objective tools ulationresemblesreal-worldscenarios.

4 ScenarioSimulation their interests, goals, and roles [17, 142, 172]. Agents can
alsobeconfiguredtohaveaccesstoexternalresources,such
as related research papers [171], predefined strategies [142]
In the real world, individuals do not function in isolation.
ordiseaseinformation[18].
They frequently engage in collaborative efforts to complete
taskswithinspecificscenarios. Thisraisesacrucialquestion: State Environment states encompass the information pro-
can LLM-based agents cooperate like humans or even sur- videdbytheenvironmentduringscenarioexecution(config-
passhumanperformanceinachievingcollectiveintelligence? urations are fixed at the beginning instead). They directly
Toanswerthisquestion,researcherssimulatetheinteractions influencetheagents’decision-makingandbehavior. Accord-
andcollaborationsofmultipleindividualsacrossvarioussce- ingtohowagentsreceivethem,statescanbefurtherdivided
narios[16,17,147],rangingfromeverydayconversationsto intoobservationandfeedback.
complexprofessionaltasks,toenhancecollectiveintelligence Observation involves changes in the environment and the
andproblem-solvingcapabilities. Ascenariosimulationtyp- current state of surrounding entities. For example, proper-
icallystartswithdesigningamulti-agentsystemthatincludes tiesandspatialpositions[164,189,194,197]ofotheragents
constructingthescenarioenvironment,modelingagentroles, are provided to agents to inform real-time decision-making.
and establishing organizational structures and communica- Moreover, continuously updating agents’ physical states are
tionprotocolstomanageinteractionsamongagents. utilized to establish real-time spatial relationships with their
In this section, we begin discussing the system composi- environmentandneighboringagents[161,194,197,198].
tion of a scenario simulation with four key aspects in §4.1. Feedback consists of responses received by agents after
Followingthis,wesummarizeseveralscenariosthathavere- they perform actions, which guide future strategy adjust-
cently attracted the attention of researchers in §4.2. Finally, ments. Some studies [162, 164, 190] describe how agents’
wereviewthemethodsandmetricscommonlyusedforeval- cognitivestatesandstrategiesaremodifiedbasedonfeedback
uating scenario simulations in §4.3. The overall framework aftereachinteraction,allowingthemtosimulatehuman-like
ispresentedinFigure3andrepresentativeworksaresumma- adaptability. Meanwhile,feedbackonmarketeventsordeci-
rizedinTable2. sions made by others [162, 182] and execution results from
external tools [17, 147, 177] are provided, to facilitate strat-
4.1 System
egyadjustmentandguidefutureactions.
The diversity of scenarios presents challenges in proposing
a unified system applicable to scenarios. Most of the cur- History As the scenario runs, past states and interactions
rentsystemscanbesummarizedas“agentsorganizedtoplay accumulateintoaseriesofhistoryrecords. Agentscanlever-
roles in dedicated environments through constrained com- agethemtoadapttonewsituationsandrefinestrategies,en-
munications”. Based on this general description, we iden- suring more coherent and effective task performance in dy-
tifyfourkeyconceptsinscenariosimulations: environment, namicenvironments. Wesummarizefourwidelyusedmeth-
role,organizationandcommunication.
odstoprocessandutilizethehistory,includingdirectintegra-
tion,refinement,summarizationandmemorymechanisms.
4.1.1 Environment Direct integration appends the history to the current in-
The environment in scenario simulation defines the specific put without modification. Agents may retain task continu-
contextsinwhichagentsoperateandinteractwitheachother. ity by incorporating past dialogue directly into the current
Just as humans gather information from their surroundings, session [29, 145, 147, 166]. Excessive content is truncated
agentsdependontheenvironmenttoreceiveinputfromvar- to fit token limits while preserving key historical informa-
ious sources. These signals guide the behaviors and strate- tion[194,196].
gies of agents within the system. Thus, a comprehensive Refinement iteratively updates and enhances responses
understanding of the environment paves the way for agents’ based on the history. Ma et al. [149] uses a subgraph-
decision-making and task continuity. We analyze the envi- focusingmechanismtorefineanswers,allowingagentstoop-
ronment of existing work by focusing on four key aspects: timize outcomes after each reasoning step. Similarly, Weiss
configuration,state,historyandtools. etal.[183]andD’Arcyetal.[30]iterativelyimprovesinitial
Configuration Theenvironmentconfigurationprovidesba- answerstoconvergetomoreaccurateresults.
sic information, especially essential elements necessary for Summarization distills essential insights from the history.
thetasksandgoalsinthescenario. Thesystemwillinitialize Thiscanbeachievedbysynthesizingcoreactionsfrommul-
agentsaccordinglysothattheyinteractwithclearobjectives. tipleplanstoestablishareferencefordiversescenarios[161],
Morespecifically,anenvironmentconfigurationmayinclude summarizingreportsfrommultipleagentstoconsolidatefind-
eventsintheenvironmentandprofilesofagents. ings[168],andsharingkeysolutionssubtasks[177]toavoid
Events are represented as a primary focus that needs to lengthydialoguehistories.
be resolved, such as the specific cases brought before the Memory mechanisms process the history through agents’
court[20,181,185,186],andthetopicsthatserveasthebasis memorymodules. Thisdynamicapproachenablesagentsto
formulti-agentdebates.[29,144–149]. preserverelevantinformationbothwithinandacrosssessions
Profile refers to personalized information relevant to the [26, 48, 173, 180, 182, 195, 199, 200]. In addition, Hong
agents specific to the scenario. Different from the basic at- etal.[17]proposedsharedmessagepoolstofurtherenhance
tributes described in individual simulation, this module en- communicationefficiency,whereagentsexchangestructured
compassesvariousaspectsoftheagents’identities,including messagesdirectlyandretrieveinformationinapersonalized

Environment DirectorRole
Scenario Task Paper Organization Communication
Configuration State History Tools Planner Coordinator Integrator
Sotopia[138] ✓ ✓ ✓ static,single UNL
Elicitron[139] ✓ ✓ static,multi UNL
Social APAM[140] ✓ ✓ static,single UNL
Interaction SimuLife++[141] ✓ ✓ static,single UNL
Self-Emotion[142] ✓ ✓ ✓ dynamic,single UNL
ICL-AIF[143] ✓ ✓ ✓ static,single UNL
FORD[144] ✓ ✓ ✓ static,multi UNL
duetal.[29] ✓ ✓ static,single UNL
MAD[145] ✓ ✓ ✓ static,single UNL
Question ChatEval[146] ✓ ✓ ✓ static,single UNL
Answering AutoGen[147] ✓ ✓ ✓ dynamic,single UNL
AmazonHistoryPrice[148] ✓ ✓ static,single UNL
DoG[149] ✓ ✓ ✓ dynamic,single UNL
ChatLLM[49] ✓ static,single UNL
Dialog- xuetal.[150] ✓ ✓ static,multi UNL
Driven ReCon[151] ✓ ✓ static,multi UNL
MachineSoM[152] ✓ ✓ dynamic,single UNL
AvalonBench[153] ✓ ✓ static,multi UNL
lanetal.[154] ✓ ✓ static,multi UNL
xuetal.[155] ✓ ✓ static,multi UNL
ThinkThrice[156] ✓ ✓ dynamic,single UNL
Game CodeAct[157] ✓ ✓ static,multi UNL
wuetal.[158] ✓ ✓ static,multi UNL
WWQA[159] ✓ ✓ ✓ ✓ static,multi UNL
PLAYER[160] ✓ ✓ dynamic,multi UNL
GITM[161] ✓ ✓ ✓ ✓ static,multi UNL
sreedharetal.[162] ✓ ✓ ✓ static,single UNL
AmongAgents[163] ✓ ✓ ✓ static,multi UNL
S-Agents[164] ✓ ✓ ✓ ✓ ✓ dynamic,single UNL
VIDS[165] ✓ ✓ dynamic,multi UNL
DR-CoT[166] ✓ ✓ static,single UNL
ChatGPTResearchGroup[167] ✓ ✓ ✓ ✓ dynamic,multi UNL
MedAgents[168] ✓ ✓ ✓ dynamic,multi UNL,SL
MARG[30] ✓ ✓ ✓ static,multi UNL
AIHospital[19] ✓ ✓ ✓ static,multi UNL,SL
REVIEWER2[169] ✓ static,multi UNL
Foundational CosmoAgent[170] ✓ ✓ ✓ dynamic,single UNL
andApplied FPS[26] ✓ ✓ dynamic,single UNL
Science ResearchAgent[171] ✓ ✓ static,multi UNL
AgentHospital[18] ✓ ✓ dynamic,multi UNL,SL
CulturePark[50] ✓ ✓ ✓ dynamic,single UNL
SynthPAI[172] ✓ ✓ ✓ dynamic,single UNL
DreamFactory[173] ✓ ✓ ✓ static,multi UNL,SL
AutoTQA[174] ✓ ✓ ✓ ✓ ✓ static,multi UNL
DERA[175] ✓ ✓ ✓ static,single UNL
Self-collaboration[176] ✓ ✓ dynamic,multi UNL
ChatDev[177] ✓ ✓ ✓ ✓ static,multi UNL,SL
Software MetaGPT[17] ✓ ✓ ✓ ✓ ✓ ✓ static,multi SL
Development ExperientialCo-Learning[178] ✓ ✓ ✓ ✓ dynamic,multi UNL,SL
Task- AutoCodeRover[179] ✓ ✓ ✓ static,multi UNL,SL
Driven IER[180] ✓ ✓ dynamic,single UNL,SL
BlindJudgement[181] ✓ static,single UNL
TradingGPT[182] ✓ ✓ ✓ dynamic,single UNL
InformationBazaar[183] ✓ ✓ static,single UNL
SimuCourt[20] ✓ ✓ ✓ ✓ static,multi UNL,SL
MATHVC[184] ✓ ✓ ✓ static,multi UNL
bakeretal.[185] ✓ ✓ static,multi UNL
LawLuo[186] ✓ ✓ ✓ dynamic,multi UNL
MAIC[187] ✓ ✓ ✓ ✓ dynamic,multi UNL
CAMEL[188] ✓ ✓ ✓ static,single UNL
Other SwiftSage[189] ✓ ✓ ✓ static,single UNL
Industries Multi-AgentCollaboration[190] ✓ ✓ ✓ ✓ dynamic,single UNL
CoELA[191] ✓ ✓ ✓ static,multi UNL
RoCo[192] ✓ ✓ ✓ static,single UNL
AgentVerse[193] ✓ ✓ ✓ ✓ ✓ dynamic,multi UNL
Scalable[194] ✓ ✓ ✓ ✓ dynamic,single UNL
AutoAgents[195] ✓ ✓ ✓ ✓ dynamic,single UNL
OpenAgents[196] ✓ ✓ ✓ ✓ dynamic,single SL
TWOSOME[197] ✓ ✓ static,single -
ReAd[198] ✓ ✓ ✓ ✓ dynamic,single UNL
MACNET[48] ✓ ✓ dynamic,single UNL
Table2:Alistofrepresentativeworksofscenariosimulation.UNL:unstructurednaturallanguage;SL:structuredlanguage.

manner. optimize the process by maximizing the advantage func-
tion[164]anddevelopplansbasedonuserinquiries[174].
Tools Externaltoolsofferspecializedfunctionalitiesrelated
Coordinatorsareresponsibleformanagingandcoordinat-
toscenariosimulationtasks,enablingmoreaccurateandpre-
ingthecollaborationbetweenagentstoensureeffectivetask
ciseoutcomes.Thespectrumoftoolsutilizedinscenariosim-
execution, monitor progress, and facilitate cooperation. The
ulation encompasses a wide range, from programming lan-
project managers [17, 167] in software development over-
guages such as Python and SQL to APIs facilitating exter-
see task distribution and project progress, ensuring efficient
nal interactions. Generally, Python is mainly employed to
collaborationamongteammembersthroughoutthedevelop-
execute and verify programmes [17, 147, 177]. SQL [174]
ment cycle. Judge assistant agents [20] aids in organizing
andknowledgegraphsquerytools [149,171]havebeenhar-
information during court proceedings, and the main contact
nessedtoretrieveexternalstructureddata. Incertainscenar-
agents[50]manageinterculturalconversations. Additionally,
ios, task-related tools such as calculators, predefined tools,
the secretary agents [170] manage interactions among civi-
andAPIs[195,196]arealsoutilizedtoprovideintermediate
lization agents. Meanwhile, coordinators also provide feed-
results,simplifyingtheprocessingworkflowofagents.
back to guide better interactions. Critic agents [143] evalu-
ate negotiation strategies and guide agents through iterative
4.1.2 Role
learning processes. Judge agents [144, 145, 201] serve as
Inscenariosimulations,weassignagentsdistinctrolesbased
an authoritative evaluator, assessing arguments and perfor-
on their tasks and functionalities. As demonstrated in Fig-
mancesduringdebates.
ure3,therearetwogroupsofrolesinatypicalsetting: par-
Integrators encompass various decision-making and sum-
ticipantscarryoutthetaskswithinthescenario,anddirectors
marization functions critical for guiding the system’s trajec-
managethetask executionprocesseswhileprovidingneces-
tory. Deciders [175] autonomously evaluate contributions
saryassistance. Eachrolehasitsownresponsibilitythatem-
fromtheresearchertomakeinformedjudgmentsonthedia-
phasizes different aspects of the system’s operations. They
logue’soutcome. Summarizeragents[146]enhancecommu-
collaboratetoachievethesystem’soverallgoals.
nication clarity by providing concise summaries of discus-
sions after each iteration, effectively integrating key points
Participants Participantsarethekeymembersthatactively
intotheongoingdialogue. Inmedicalscenarios,medicalre-
engagedintaskexecutionanddiscussion. Theirorganization
port assistants [168] compile analyses into a cohesive docu-
and communication are the core of task completion in sce-
mentthatsupportscollaborativeexpertdiscussions,whilethe
nario simulations. Participants can be further classified into
communicatorsandworkersaccordingtotheirtasks. medicaldecisionmakerensuresthatfinaldecisionsreflectthe
collectiveexpertiseofthespecialistsinvolved. Additionally,
Communicators primarily focus on communication, such
the chief physician [19] evaluates diagnostic performance
as information exchange, feedback, and task guidance.
basedonaccuracyandeffectiveness,reinforcingthesystem’s
Specifically, this kind of agents can process information for
overall reliability. In legal contexts, the judge [20] oversees
certain disciplines and research applications [175, 181] and
judicial processes, making critical decisions grounded in le-
advocate diverseviewpoints [49,144], claims[145] andun-
galargumentsandassessingtheevidencepresented.
derlyingneeds[50,139].
Workersaredirectlyinvolvedintaskexecutionandopera- 4.1.3 Organization
tions, demonstrating specialized skills and efficiency. This Effectivetaskexecutionnecessitatescarefulcoordinationand
typically includes the common professional roles present schedulingoftheinteractionsbetweenindividualagents.The
in each scenario, such as coder and tester in software de- organizational structures establish how each agent collabo-
velopment [176], buyer and seller in negotiations [143], rateswithotherstoachieveagoal. Typically, wecandepict
doctors and medical professional agents in healthcare do- anorganizationschemabyitsmodeandstructure.
main[18,166],andreceptionist,lawyer,andsecretaryinthe
Mode Theorganizationalstructuredetermineswhetherthe
legalcontexts[186].
relationships among agents remain stable or evolve dynami-
Directors Whileparticipantsexecutemostofthetasks,di- cally throughout the simulation process. In terms of how to
rectors can provide essential support in crucial aspects such organize agents, there are mainly two modes in existing re-
asplanningprocedures,coordinatingcommunication,andin- search,i.e.,staticanddynamicmode.
tegratingresults. WenamethemPlanners,Coordinatorsand Static mode refers to the organizational structure prede-
Integratorsrespectively. fined based on the nature of the tasks. Agents communi-
Planners play a vital role in task definition and strate- cateandworkinanorderlymanneraccordingtothesestatic
gic formulation, facilitating effective inter-agent collabora- structures.Thestaticmodecanbefurtherdividedintosingle-
tionthroughtaskssuchasdefiningobjectives,analyzinguser stageandmulti-stagesetups. Inthesingle-stagesetup,agents
requirements, andoptimizingexecutionplans. Task-specific follow a fixed structure in multiple rounds of communica-
agents [188], central planners [193], analysts [176] and de- tion, such as structured debates [143, 146, 175, 188], skill
composer [161] are responsible for breaking down require- training [140, 141] and integrating ideas [49, 181]. In the
ments and dividing overarching objectives into specific sub- multi-stage setup, tasks are divided into distinct stages, and
goals. Productmanagers[17]contributebycreatingdetailed theorganizationmaychangewithstages. Thiscanbefound
productrequirementsdocuments. Otherplannerscanalsore- in the design, coding, and testing stages in software devel-
fine execution plans according to task requirements [194], opmentscenariosfollowingthewaterfallmodelorstandard-

ized operating procedures [17, 177], and multi-stage pro- collective outcomes, like software development[17, 176,
cessinjudicialscenarios[20,185]andproblem-solvingpro- 177], medical diagnosis[19, 168], and case handling[181,
cesses[149,161,191]. 186]. Incontrast,agentsincompetitivecommunicationtypi-
Dynamic mode explores more open and adaptive orga- callyholddifferingviewpointsandpositions,eachstrivingto
nizational structures, often relying on dynamic and heuris- achieveindividualobjectives. Suchscenariosarecommonly
tic communication. This also includes both single-stage foundinsettingslikegames[150,151,159]anddebates[143–
and multi-stage setups. The single-stage setup emphasizes 145], where agents maintain opposing stances and seek to
agent collaboration and adaptability in a single stage. The outmaneuvereachother.
agents can be flexibly created and recruited [149, 193, 195,
196,202], coordinatedthroughliaisonagents[50,170], and 4.2 Scenario
self-organized [164]. The multi-stage setup mainly fea- Using the collective capabilities of agents with specialized
tures dynamic discussions among agents. Agents can be in- expertise, scenario simulations have been applied to various
volvedacrossmultiplestages,buttheycancommunicateau- domains. Herewedividedifferentscenariosintotwogroups:
tonomously based on the current state [167, 168, 176, 186, dialog-drivenonesthatcoversocialinteractionandquestion-
187]. answering, and task-driven ones that focus on specialized
Structure The organization structure, meanwhile, reflects tasks.
howagentsareconnectedwitheachother.Typically,anorga-
4.2.1 Dialog-DrivenScenario
nizationcanbelayered,centralizedordecentralized.Layered
Dialog-driven scenarios encompass scenarios in people’s
structures adopt a hierarchical framework, with agents as-
daily lives where the dialog itself is centered, such as those
signedtodistinctlevels. Interactionsarepredominantlycon-
for social or entertainment purposes. These scenarios share
fined to agents within the same level or occur between ad-
a common emphasis on tackling general goals that are not
jacent layers, thereby facilitating a controlled and organized
related to any specific task or domain. We identify three
flowofinformation[49,177,181]. Centralizedstructuresof-
primary typesof dialog-drivenscenarios: social interaction,
teninvolveahigh-levelrole(e.g.,coordinator)thatservesas
question-answering,andgamescenarios.
the core of the organization, overseeing communication and
functioning as the central hub for interactions among other Social Interaction Some works focus on task completion
agents[19, 50, 170]. Decentralized structures, in contrast, is insimplesocialinteractionscenarios,typicallyinvolvingso-
more flattened, where agents can engage in peer-to-peer in- cialtasksbetweentwoorafewagents,suchaspersuasionor
teractionsasneeded[145,146,149]. comforting a partner. Zhou et al. [138] discusses the social
intelligence of agents in social scenarios, revealing signifi-
4.1.4 Communication cantperformancedifferencesamongmodelsacrossdifferent
Thecommunicationbetweenagentscontrolsthetransmission dimensions. The exploration in social intelligence is further
ofinformation. Tobetterunderstandtheinternalmechanism extended to objective action-level evaluation [204] and di-
ofcommunication,wedissectcommunicationfromitsformat versescenariosandothers’informationreasoning[205]. Fur-
andstyle. thermore, some works propose interactive learning meth-
ods[140,206,207]tohelplearnsocialskills.
Format From theperspective ofinformation format, there
exist two common communication protocols: unstructured Question Answering Another mainstream scenario is the
naturallanguageandstructuredlanguage. question answering, emphasizing collaborative processes,
Unstructurednaturallanguageismostcommonlyusedin strategic reasoning, and integration to enhance model per-
multi-agentcommunication,enablingflexibleandimmediate formance. On the one hand, some studies focus on im-
exchanges through free-form, conversational language that proving reasoning through debate. FORD [144] facilitates
mirrors human dialogue [29, 140, 141, 143, 144, 167, 175, athree-stagecommonsensereasoningdebate,demonstrating
188]. Communication based on natural language is diverse thatLLMscanreachconsensusevenamidstinconsistencies.
andflexible, butitcanalsosufferfromissuessuchasambi- MAD [29], involves agents debating under a judge’s super-
guityandredundancy. vision,addressingtheDegeneration-of-Thoughtproblem. In
Structured language, such as code and JSON documents, addition, a “society of minds” approach [29] is presented to
isanotherprotocolthatmayalleviatetheissuesfromnatural guide multiple debate rounds, improving mathematical rea-
language. In software development, agents transit informa- soning and factual accuracy while reducing hallucinations.
tion between phases through code [17, 177]. In the medical Ontheotherhand,someworksfocusonoptimizingstrategies
domain, structured summaries of reports are utilized to gain in strategic reasoning and negotiation. OG-Narrator [148]
keyinsights[168]. Inadditiontopredefinedformats,agents is proposed to improve negotiation strategies, increasing the
canalsoautonomouslychoosetheappropriateformatduring Buyers’dealsuccessrates.Maetal.[149]utilizeasubgraph-
interactionstoimproveefficiency[51,203]. Recently, more focusing mechanism and a multi-role debate team to im-
complexcommunicationprotocolsusingmorethanonelan- prove reasoning accuracy and reliability, outperforming ex-
guagehavebeendesignedtoimprovecommunication[53]. istingmethods.
Style Communication, by nature, can be cooperative or Game Gamesprovideauniqueplatformforexploringsce-
competitive regarding its style. In cooperative communica- nario simulation, evolving from basic game reproduction to
tion, agents share a common objective, aiming to optimize complexsocialdynamics. Earlystudies, suchas[150,151],

introduce Werewolf and Avalon to examine LLM perfor- Other Industries In the realm of broad social science,
mance in communication games, specifically investigating several studies leverage multi-agent systems to enhance
how LLMs handle aspects like trust and leadership. Build- decision-makingprocessesacrossdiversefields,suchasjour-
ing on these complex interactions, reinforcement learning nalism[210],judiciary,economics,andeducation. Intheju-
frameworks in [155, 158] allow agents to adapt their strate- dicial field, legal consultations have been improved through
gies, achieving near-human-level decision-making. To ex- LawLuo [186], which simulates collaborative discussions.
plore deeper social phenomena, [158, 160] expand on game Hamilton et al. [181] and He et al. [20] design multi-agent
dynamics by incorporating tools that enhance memory, rea- systemstosimulateU.S.SupremeCourtdecisionsandcourt
soning, and adaptability. Additionally, [159] examines the trialsthroughdetailedstepssuchasdebate,resourceretrieval,
role of opinion leadership, while [156, 157, 208] tackle ad anddecisionrefinement,complementedbyadditionalbench-
hoc teamwork, where agents adapt and collaborate without marksthatenhancelegalarticlegeneration. Intheeconomic
predefined protocols, revealing both the challenges and po- sector, Lietal.[182]proposeamulti-agentframeworkwith
tentialofLLMagentsinteam-basedcollaboration. layeredmemorytoimproveLLMperformanceinstocktrad-
ing. Additionally, Weiss et al. [183] address the buyer’s in-
4.2.2 Task-DrivenScenario spectionparadoxininformationmarketsbysimulatingamar-
Intask-drivenscenarios,agentsrole-playpersonaswithspe- ketplacewhereintelligentagentsuseLLMstonavigateinfor-
cific functions for a certain task or task-set. Most of these mationaccessandbiases,exploringtheimpactofpricingand
scenarios fall into one or more specific domains related to budgetsonoutcomes. Intheeducationdomain,MAIC[187],
the tasks. Here, agents are increasingly leveraged to solve asystemsimulatingAI-enhancedclassroomshascontributed
complex,domain-specificproblemsbyautomatingtasksand tothedevelopmentofacomprehensiveAI-drivenonlineed-
improvingdecision-makingprocesses. ucation platform. Yue et al. [184] presents MATHVC, an
LLM-driven virtual classroom designed to simulate interac-
FoundationalandAppliedScience Sciencedomains,such
tions among students, thereby fostering the development of
as medicine, mathematics, data science, and content analy-
mathematicalskills.
sis, have been popular experimental fields for scenario sim-
ulation. In the medical domain, medical reasoning and au- 4.3 Evaluation
tomating diagnostic processes have been refined through in-
Forscenariosimulations,theevaluationfocusesonhowwell
novative methodologies such as chain-of-thought prompting
the tasks of the scenarios are solved. Based on the scope
and multi-agent collaboration[18, 166, 168, 209]. Zheng
oftheevaluation,itcanbecategorizedintotaskevaluation,
et al.[167] integrates ChatGPT with Bayesian optimization
sub-taskevaluationandsystemevaluation,eachemploying
techniques to enhance research workflows in chemistry lab-
variousautomatic,LLM-based,andhumanevaluationmeth-
oratories, demonstrating significant improvements in effi-
odstoassessperformance.
ciencyandproductivity. Hassanetal.[165]introduceacon-
versationalframeworkthatenablesseamlessinteractionwith TaskEvaluation TaskEvaluationmeasurestheoverallper-
machinelearningmodels,specificallyfortaskslikedatavisu- formance of tasks assigned to the scenario. The evaluation
alizationandpredictiveanalytics. Thesestudiesdemonstrate cancarriedoutinautomaticwaysorbyLLMsorhumans. In
thepotentialofLLM-basedagentstotransformtraditionalre- termsofautomaticevaluation,predefinedmetricsandmath-
searchpatterns. ematical tools are used to objectively assess the task out-
comes,suchasaccuracy[144,181],pass@k[188]forcoding
Software Development Recent research has increasingly
tasks, success rate, and coverage for exploration [161], and
focusedonharnessingagentstoaddresscomplexchallenges
dealpricefornegotiation[143]. Thesemethodsareefficient
in software development and life-cycle management. Early
and scalable but may overlook complex behaviors. Thus,
worksfocusondesigningframeworksforcollaborativecode
LLMs [49] and human experts [145, 188] have been applied
generation. Dong et al. [176] presents a self-collaboration
toprovidemorenuancedevaluationforqualitativetasksand
frameworkwhereLLMagentsfunctionasdistinct“experts,”
comparesolutionsbasedonspecificcriteria.
eachmanagingspecificsubtaskstofacilitateautonomouscol-
laborativecodegeneration. Buildingonthis, ChatDev[177], Sub-Task Evaluation Sub-task Evaluation assesses the
a chat-powered framework utilizes unified language-based completion of sub-tasks within a scenario simulation and
communication among agents to effectively address design, their impact on overall task performance. It serves as a
coding, andtestingphases. Meanwhile,Hongetal.[17]en- process evaluation for the execution of complex tasks. The
hancesLLMcollaborationsbyencodingStandardizedOper- automatic evaluation uses metrics like transport rate, aver-
ating Procedures into prompts, enabling agents to verify re- age steps, task success rate, re-plan attempts, and efficiency
sultsandproducecoherentsolutionsthroughanassemblyline improvementtoassesssub-taskperformanceandstrategyef-
approach. Afterward, some works focus on enabling agents ficiency [191, 192]. Completeness, executability, and con-
tolearnfrompastexperiencesandrefinetheirprocessesover sistency metrics are often applied in software generation
time [178,180]. Furthereffortsfocusonautonomousissue tasks[177,178]. LLM-basedevaluationfocusesonpairwise
resolution and program understanding [179]. These studies comparisonsorwinratejudgments,capturingqualitativeas-
show the potential of multi-agent collaboration in software pects of sub-task performance [177]. Meanwhile, human
engineering,offeringrobusttoolsforautomaticdevelopment evaluationreliesonparticipantstoprovidesubjectiveassess-
andmanagement. mentsonmetricssuchasexecutability,revisioncosts,orcom-

Scenario
General Economic Online Platform Sociology and Politics
Economics Social Media Sociology
Game
…
Theory Rec
…
Sys Po
…
litics
Support
Social Construction Element
Composition Network Social Influence Outcome
age
…
opinion
gender
norm
Relation
offline online
Evaluate
Level Evaluation Strategy
Micro Macro System Subjective Objective
Figure4: Illustrationofsocietysimulations. Toconstructsocietysimulations,thecorrespondingsociety’sconstructionelements,i.e.,com-
position,network,socialinfluenceandoutcomesneedtobecarefullydesigned. Buildingonthis,variousscenarioscanbesimulated. The
performanceofindividualsandtheoverallperformanceofthesystemareevaluated.
mentquality,offeringpracticalinsightsintosub-taskperfor- onrevealingandexplainingemergentbehaviorsandtheout-
mance[17,30]. comesofinteractionsamongnumerousagents. Societysim-
ulations have been a vital tool for theoretical validation and
SystemEvaluation SystemEvaluationaimstocapturethe
predictingsocialdynamics.
effectivenessandefficiencyofthesysteminascenariosimu-
In this section, we summarize the components of social
lationasawhole.Automaticevaluationreliesonmetricssuch
construction to capture the key features reflected in society
astokenconsumption,tasksuccessrate,andhuman-likeness
simulationsin§5.1. Then,wepresentthedifferentcategories
scorestomeasuretheefficiencyandrealismofagents[197].
of scenarios in society simulation in §5.2. After that, we
Additional metrics like accuracy, precision, recall, and F1
introduce the evaluation of society simulation in §5.3. The
scores are used to assess system accuracy and consistency
overall framework is illustrated in Figure 4 and representa-
in diagnostic or predictive tasks [19]. LLM-based evalua-
tiveworksaresummarizedinTable3.
tion often involves GPT-4 to assess qualitative aspects, such
as human-likeness or diagnostic report quality [18, 197].
5.1 SocialConstructionElements
Humanevaluationtypicallyinvolvessubjectiveassessments,
suchasratinginstructionalcontentfortone,clarity,andsup- Considering the complexity of society, a major challenge in
portivenessonaLikertscale[187],oftenusedtocomplement societysimulationisbridgingthegapbetweenindividualand
automatic methods and capture human perspectives on sys- societal scales. Some core elements serve as the foundation
temoutputs. formodelingsocialsystems. Weoutlinefourkeydimensions
thatunderpinsocietalstructuresanddynamics:composition,
5 SocietySimulation network,socialinfluence,andoutcomes.
5.1.1 Composition
While scenarios discuss multi-agent interactions in rela-
Societyiscomposedofmassiveanddiverseindividuals. This
tivelyfocusedandsmall-scalecontextsandprovidesolutions
diversity,alsoreferredtoasheterogeneity[259]insocialsci-
withinspecificdomains,societyismorecomplexthanasim-
ence, encompasses a wide range of beliefs, preferences, be-
plescenario. Itscomplexityliesinmanyaspects,suchasthe
haviors, normative values, and positions within social struc-
diversityofitscomponents,thevarietyofstructures,andnon-
tures. Modeling this diversity is essential for capturing the
linear effects [259]. Considering this, a series of studies fo-
variedbehavioralpatternsandcomplexsocialdynamicsthat
cusonsocietysimulation. Intermsofresearchtopic,society
emergefromindividualdifferenceswithinasocialsystem.
simulationgenerallyhopestoinvestigatesocietalandmacro-
levelresults. Intermsofresearchpurpose,societysimulation Individual Composition To model a diverse society, the
does not aim to solve a task or problem, instead, it focuses compositionofindividualsinsocietyneedstobedetermined.

ConstructionElement
Scenario Field Paper #Agents
Composition Network SocialInfluence Outcome
Agent-trust[211] (0,10] ✓ ✓ ✓
LELMA[212] (0,10] ✓ ✓
EconomicsArena[213] (0,10] ✓ ✓
Fontanaetal.[214] (0,10] ✓ ✓
GameTheory
SABM[215] (0,10] ✓ ✓ ✓ ✓
and
NohandChang.[216] (0,10] ✓ ✓ ✓
StrategicInteractions
Mozikovetal.[217] (0,10] ✓ ✓
Wuetal.[218] (10,100] ✓ ✓ ✓
General
CompeteAI[219] (10,100] ✓ ✓ ✓ ✓
Economic
WarAgent[47] (10,100] ✓ ✓ ✓ ✓
Horton[220] (10,100] ✓ ✓
EconAgent[27] (10,100] ✓ ✓
SRAP-Agent[221] (10,100] ✓ ✓ ✓ ✓
Economic
Ghaffarzadeganetal.[222] (10,100] ✓ ✓ ✓
Contexts
EC[223] (10,100] ✓ ✓ ✓ ✓
Williamsetal.[224] (100,∞) ✓ ✓ ✓ ✓
AgentTorch[225] (100,∞) ✓ ✓ ✓
Argyleetal.[12] (100,∞) ✓ ✓
Leeetal.[226] (100,∞) ✓ ✓
ChaudharyandChaudhary[13] (100,∞) ✓ ✓
PublicOpinion
ElectionSim[227] (100,∞) ✓ ✓
Survey
GABSS[228] (100,∞) ✓ ✓ ✓ ✓
Parketal.[229] (100,∞) ✓ ✓
Sunetal.[96] (100,∞) ✓ ✓
Aheretal.[230] (0,10] ✓ ✓
Zhangetal.[152] (0,10] ✓ ✓
LyfeAgents[231] (0,10] ✓ ✓ ✓ ✓
CRSEC[232] (0,10] ✓ ✓ ✓ ✓
Sociology
Chuangetal.[24] (0,10] ✓ ✓ ✓ ✓
and
ChoiceMates[233] (0,10] ✓ ✓ ✓ ✓
PoliticalScience
Jarrettetal.[234] (0,10] ✓ ✓
Individual
AgentReview[235] (0,10] ✓ ✓ ✓
and
GenerativeAgents[32] (10,100] ✓ ✓ ✓ ✓
Organizational
AGA[236] (10,100] ✓ ✓ ✓ ✓
BehaviorObservation
MineLand[237] (10,100] ✓ ✓ ✓ ✓
Chuangetal.[31] (10,100] ✓ ✓ ✓ ✓
CareerAgent[238] (10,100] ✓ ✓ ✓ ✓
SuzukiandArita[239] (10,100] ✓ ✓ ✓
Chuangetal.[240] (100,∞) ✓ ✓
Lietal.[241] (100,∞) ✓ ✓ ✓
MATRIX[242] (100,∞) ✓ ✓
Caietal.[243] (0,10] ✓ ✓
FPS[26] (10,100] ✓ ✓ ✓ ✓
FUSE[244] (10,100] ✓ ✓ ✓ ✓
Wangetal.[245] (10,100] ✓ ✓ ✓ ✓
Concordia[246] (10,100] ✓ ✓ ✓ ✓
SocialSimulacra[247] (100,∞) ✓ ✓ ✓ ✓
Social S3[248] (100,∞) ✓ ✓ ✓ ✓
Platforms To¨rnbergetal.[249] (100,∞) ✓ ✓ ✓ ✓
YSocial[250] (100,∞) ✓ ✓ ✓ ✓
Online
TIS[251] (100,∞) ✓ ✓ ✓ ✓
Platform
HiSim[25] (100,∞) ✓ ✓ ✓ ✓
OASIS[33] (100,∞) ✓ ✓ ✓ ✓
MindEcho[252] (100,∞) ✓ ✓
BASES[253] (100,∞) ✓
InteRecAgent[254] (0,10] ✓
Rec4Agentverse[255] (0,10] ✓ ✓
Recommendation
RecAgent[256] (10,100] ✓ ✓ ✓ ✓
Environments
Agent4Rec[257] (100,∞) ✓ ✓ ✓ ✓
AgentCF[258] (100,∞) ✓ ✓ ✓ ✓
Table3:Alistofrepresentativeworksofsocietysimulation.

There are three main approaches to determining the compo- hoodofcommunication. Highlysimilarindividualsaremore
sition of individuals in a system simulating a microcosm of likelytoestablishconnectionscomparedtothosewithgreater
society. Some works rely on virtual individual synthesis, differences [262, 263]. This principle also informs the con-
often not focused on alignment with the real world, aim- struction of networks in society simulations. The methods
ing to ensure that the system includes users with a variety forconstructingsocialnetworksvaryacrossdifferentscenar-
ofattributes, typicallybygeneratingvirtualindividualswith ios. Here, we divide them into offline networks and online
the help of LLMs or humans [31, 260]. Other works uti- networks.
lize existing datasets, such as MovieLens-1M [256, 257],
Offline Network An offline network represents connec-
to define user composition within a simulated recommenda-
tionsformedthroughin-personinteractions,suchasface-to-
tionplatform. Agentsareinitializedonthebasisoftheuser
face communication or the spread of opinions and diseases
information within these datasets, reflecting the distribution
in physical settings. On the one hand, some studies aim to
of users in that context. Recently, an increasing number of
simulate interactions in virtual worlds, thus determining the
studies have focused on real-world distribution replication,
connectionsbetweenagentsinarandomorpredefinedman-
such as the composition of users on social platforms [33]
ner [32, 232, 236]. On the other hand, when some studies
or the distribution of voters in surveys [227]. For small-
aim to simulate the spread of a disease or event information
scale individual sets, individual data are typically collected
intherealworld, consideringthedifficultyofobtainingreal
manually [229, 233]. In cases where large-scale popula-
data, they often estimate the social relations using external
tionsarerequiredorobtainingrealdataisdifficult,individu-
algorithms or agents themselves [224, 228]. However, in
alsmaybesampledbasedonreal-worldmacrodistributions
studieswithalargescaleofagents,thenetworkrelationships
or generated by LLMs to match desired attribute distribu-
between individuals are sometimes ignored, and individuals
tion[12,226,227].
aretreatedasindependent[227]. Alternatively,somestudies
Trade-offbetweenSimulationPrecisionandScale When provide rough information, such as community statistics, in
simulating individuals in society simulations, many studies placeofspecificdetailsabouttheagents’neighbors[225].
adopt detailed role modeling to enhance the authenticity of
Online Network An online network is a digital structure
agentbehavior.Beyondcommondemographicattributes,this
whereindividualsorentitiesinteractthroughplatforms,such
may include factors such as an individual’s past statements
as online social platforms and recommendation platforms,
andinteractionhistory[32,214,219,256,257]. However,as
forming connections based on activities, relationships, or
thenumberofindividualsincreases,suchfine-grainedmodel-
shared interests. At the beginning, some studies randomly
ingbecomesexpensive.Consequently,atrade-offoftenarises
initializethesocialrelationsforusersexistingdatasets[256]
betweentheprecisionofindividualmodelingandthescaleof
or synthesized users [26], while other efforts have focused
thesimulation.Inlarge-scalesimulations,toreducecomputa-
oncrawlingauthenticsocialrelationshipsfromsocialmedia
tionalcosts,thedetailsofeachagentaretypicallysimplified,
platformslikeWeibo[248]andTwitter[25]. However,asthe
byretainingonlythemostessentialandcommoncharacteris-
scaleofindividualsincrease,itmaybechallengingtoobtain
tics[224,225]orcompressingauxiliarydialogueinformation
all of their authentic relationships. Therefore, some studies
intosharedmemory[236].
constructnetworksusingasmallportionofrealrelationship
Special Modeling on Outliers As previously mentioned, data combined with a large amount of synthetic relationship
thecompositionofindividualsinsocietyisdiverse.However,
data [33], or connect similar users based on the assumption
notallindividualsplayanequallysignificantrole. Somein-
ofhomophily[242].
dividuals,whoseattributesorbehaviorssignificantlydeviate
fromthemajority,arereferredtoasoutliers[259].Compared 5.1.3 SocialInfluence
toaverageindividuals,outliersoftenintroducevariabilityand Socialinfluencereferstotheinfluenceagentshaveonothers
unpredictabilitytosociety. Examplesincludecelebritiesand andtheinfluencetheyreceivefromothersduringinteractions.
opinion leaders [251, 252], who frequently hold prominent Thisisalsoknownasembeddednessinsocialsciences[259],
positionswithinsocialstructuresandamplifytheirinfluence. which suggests that individuals behavior and decisions are
Insituationswithlimitedresources,somestudies[25]priori- influenced by their environment. When conducting society
tizedetailedmodelingofthesecorecontentproducers,while simulations,itisnecessarytoconsiderthemodelingofsuch
simplifying the modeling for the majority. Meanwhile, in- socialinfluence.
tervention policies based on simulation results often focus
InfluenceReceivedbytheInfluencee Thesameinforma-
on these key nodes in networks [261], aiming to influence
tionmayproducedifferenteffectswhenreceivedbyindivid-
theoverallsystem’sbehaviorbyblockingorinterferingwith
uals with different traits. Currently, most studies have mod-
them.
eledhowtheinfluencereceivedbytherecipientvariesbased
5.1.2 Network on their profile [26, 33, 248]. This can be easily achieved
Social interactions are often conducted through social net- byintegratingtheindividual’sprofile,memoryandtheinfor-
works,whichcanbedescribedusinggraphstructureswhere mationreceivedfromothersintothesamecontext. Building
nodes represent individuals and edges represent their rela- this,afewworksfurtherinduceadditionalmechanismssuch
tions. The network determines the direction of information as cognitive bias [24] and reflection on norms [232] to en-
andinfluencedissemination.Insocialscience,ithasbeenob- hance agents’ understanding and perception of the received
served that homophily of individuals can increase the likeli- messages.

Influence Exerted by the Influencer The same message 5.2 Scenario
conveyed by different individuals can result in varying so-
Society simulation has been widely applied to various sce-
cial impacts. The Pareto distribution and the Matthew Ef-
narios related to human society. These scenarios cover dif-
fect[25,256]indicatethatinformation,influence,orattention
ferent aspects of daily human life, and existing studies can
tendstoconcentrateonasmallgroupofindividualswhoare
becategorizedintothreeprimaryareas: generaleconomics,
already dominant in the community. Therefore, when simu-
sociologyandpoliticalscience,aswellasonlineplatforms.
lating social interactions, the identity, status, and reputation
oftheinformationsenderarealsocrucial. Somestudiesstart 5.2.1 GeneralEconomics
withreal-worlddatatoconductdetailedmodelingofopinion Simulations in general economics analyze decision-making
leaders[251,252]. Otherstudies,insteadoffocusingonthe andbehaviorsrelatedtoresourceallocationandcompetition.
roleoftheinfluencer, modeltheinfluenceexertedbythein- These studies primarily investigate how agents make deci-
fluencerbyincorporatingtherelationinformationsuchasso- sions influenced by economic incentives, market rules and
cialimpressionmemory[236]andsharepartyaffiliation[31]. resource constraints, while also examining how interactions
In addition to the influence exerted by individuals, research amonggroupsshapebroadereconomictrends.
hasfoundthatasgroupsizeincreases,theimpactofasingle
GameTheory andStrategicInteractions Someresearch
influencermaydiminish.However,theinfluenceofthegroup
mainly focuses on game theory and strategic interaction.
onindividualsoftendrivesthemtoaligntheirbehaviorwith
Thesescenariostypicallyinvolvesmallgroupsofagents,with
thegroup,leadingtotheemergenceoftheherdeffect[33].
aprimaryfocusonthecomplexinteractionsbetweenagents.
5.1.4 Outcomes Someworksuseclassicgametheorygames,suchasthePris-
oner’sDilemma,toexploreagentbehavioringame-theoretic
Social emergence suggests that the collective behaviors or
scenarios, including trust behavior [211], logic reasoning
phenomenaarisefromindividualinteractionsarenotalinear
and decision-making [212], rationality and strategic reason-
sumofindividualactionsbutrathercomplexpatternsemerge
ing ability [213], cooperation tendencies [214] and how
from the interactions [21, 259]. These interaction outcomes
emotional states can disrupt rational decision-making [217].
maybemeasurablemacroresults,suchasvotingresultsand
Other studies focus on real-world scenarios other than the
public opinion levels, or they may also be qualitative social
games,suchasspontaneouscooperationincompetitiveenvi-
phenomenaandnorms. Next,wewilldiscussthesetwotypes
ronments [218], complex market behaviors in firm competi-
ofoutcomesseparately.
tion[215],andcompetitionbetweenrestaurantandcustomer
MacroStatisticalResults Macrostatisticalresultsaretyp- agents [219]. Overall, the former kind of scenarios simpli-
ically the focus of existing studies, as they are closely re- fies the environment, making it easier to conduct controlled
lated to predefined research objectives such as market re- researchonagentbehavior,whilethelatterprovidesmorein-
search, election predictions, and public opinion forecasting. sightsforreal-worldapplications.
These studies often aim to calculate the sum or average of
Economic Contexts In addition to close studies on game
thechoices oropinionsof allagents inthesystem. To geta
theory and strategic interactions, some studies focus on the
static opinion distribution, some studies overlook the social
use of agents and their interactions within economic envi-
interactionsandinsteaddirectlysumupindividualchoicesto
ronments. Horton [220] examines economic agents driven
obtain macro outcomes [96, 227], simplifying the complex-
by LLMs in various experiments to replicate human be-
ity of social dynamics. Another line of research focuses on
havior in economic scenarios. EconAgent [27] introduces
the change of indicators by modeling multiple rounds of in-
agents for macroeconomic simulation, emphasizing the in-
teractions among the agents over a period of time and then
fluence of macroeconomic trends. SRAP-Agent [221] pro-
statisticallyanalyzingtheresults[27,215,218,248,249].
poses a framework for simulating and optimizing scarce re-
Formation of Social Phenomena and Social Norms In sourceallocationineconomics,specificallyinpublichousing
addition to the quantifiable macro results, some social phe- allocation scenarios. Besides, some studies involve broader
nomenaandsocialnormsarealsoimportantoutcomesofso- macroeconomic domains, using agents to simulate and pre-
cialinteractions. Ontheonehand,somestudieshaveidenti- dictthespreadofdiseasesandthechangeinunemployment
fiedthebubbleeffectinrecommendationsystems[257],echo rates[224,225].
chambers in social media [25, 33, 245], Matthew effect in
5.2.2 SociologyandPoliticalScience
competitiveagentinteractions[219], andspontaneouscoop-
Societysimulationhasbeenwidelyusedinsociologicaland
eration of competing agents [218] by calculating additional
political science research. These studies range from small-
metrics or observing the trends of primary indicators. On
scale laboratory experiments that validate theories and hy-
theotherhand,somestudiesexaminesocialnormsasanim-
pothesestolarge-scalesocialsurveysaimedatunderstanding
portant byproduct of social interactions. This includes sim-
public choices. The goal is to leverage agents as substitutes
ulating and testing whether community rules can shape de-
for humans in studying human behavior within sociological
siredsocialnorms[247],constructingnormativearchitecture
andpoliticalcontexts.
toobservetheemergenceofsocialnorms[232],studyinghow
social media language evolves in the presence of regulatory PublicOpinionSurvey Amainstreamapplicationofsoci-
constraints [243], and observing changes in social norms in ety simulation is public opinion survey, which aims to pre-
real-worldscenariossuchasautonomousdriving[264]. dict the perspectives of specific groups toward a given sub-

ject through simulation and aggregate their opinions to sup- ulate personalized behaviors such as item selection, prefer-
port advanced needs such as election forecasting and public ences,andemotionalresponses,oftenintegratingusermem-
administration. Argyle et al. [12] first propose that LLMs ory and contextual factors [256–258]. Additionally, some
could serve as silicon samples of humans, through several approachesincorporateexternalknowledgeorself-reflection
large-scale surveys conducted in the United States. Build- mechanisms, allowing agents to adapt and learn from their
ing on this, some studies have expanded their focus to sce- interactionsovertime[267]. Thesestudiescollectivelyshow
narios of opinion surveys [13, 226, 240], such as election how LLMs can bridge the gap between traditional recom-
polls[227]andresponsetopublicadministrationcrisis[228], mender systems and more interactive, human-like behavior
delvingdeeperintoissueslikepopulationcomplexityandal- simulations, offering new ways to improve recommendation
gorithmic bias. Recently, agents have demonstrated the po- accuracyandbetterunderstanduserdynamics.
tentialtoreplicateparticipants’responsesinindividualinter-
views [229]. These studies lay the foundation for new tools 5.3 Evaluation
toinvestigateindividualandcollectivebehavior. For society simulations, the evaluation primarily focuses on
thecomparisonbetweenthesimulationresultsandreal-world
Individual and Organizational Behavior Observation
data, with assessments centered on micro level, macro level
Otherstudiesfocusonobservingindividualororganizational
andsystemlevel.
behaviorincommonorspecificsettings. Someworksdonot
specify a particular scenario but instead observe agents’ so- Micro-level Evaluation Individual simulation accuracy is
cialinteractionsandpotentialphenomenaindailylifewithin key to society simulation. Therefore, micro-level evalua-
asandboxenvironment[32,231,232,237].Otherstudiesaim tion of society simulation has received widespread atten-
tovalidatetheoriesorhypothesesinspecificscenarios, such tion. Initially, evaluations in non-real-world simulations
asthewisdomofpartisancrowds[31],informationmanage- draw on the Turing test, assessing agent behavior’s resem-
ment[233], organizationalbehaviormanagement[238], and blance to human behavior, often subjectively by humans or
theevolutionofpersonalitytraits[239]. LLMs [32, 236, 268]. For specific scenarios, metrics like
partisan bias and human likeness index are proposed [31].
5.2.3 OnlinePlatform
When simulations target real-world scenarios with available
OnlinePlatformsareavitalcomponentofsocietysimulation, empiricaldata,automatedmetricslikeemotion,attitude,be-
offering a practical means to study complex social phenom- haviorconsistency,andusertastealignmentcanbedesigned
ena in digital environments. These platforms, ranging from formoreobjectiveevaluationsbycomparingsimulationcon-
socialmediatoonlinecommunities,allowagentstosimulate tentwithreal-worlddata[25,248,257].
real-world interactions and study dynamics such as opinion
Macro-level Evaluation Social interactions often lead to
formation,informationspread,andcollectivebehaviors.
collective outcomes, so it is important to evaluate whether
SocialPlatforms Onlinesocialplatformshavelongserved macro-leveloutcomesshowpatternsandtrendsthatarecon-
as an important testing ground for studying the propagation sistent with the real world. For sociology and online plat-
of information and the evolution of opinions. These stud- forms, attention is typically given to whether the scale of
ies typically recreate environments similar to popular so- propagation, the distribution and trends of collective opin-
cial platforms, such as Twitter, Reddit, and Weibo, with ac- ions and traits align with those of the real world. In addi-
tionspacesthatincludebehaviorslikesharing,commenting, tiontoqualitativemethodssuchassubjectiveevaluation[248,
and liking. By simulating these scenarios, researchers can 257], some studies have proposed quantitative metrics, such
model the spread of information and track changes in user as fitted parameters, correlation coefficients and change of
attitudes following events, covering a wide range of topics toxicity of community content to measure this differences
suchasgeneralnews,rumors,andtheroleofopinionleaders objectively [25, 26, 33, 249]. Similarly, in economic sim-
[26, 243, 244, 248, 250, 251]. In such scenarios, the roles ulation, the evaluation of simulated economic systems de-
and relationships of agents play a critical role in ensuring pendsonwhethertheycanreproducethemostrepresentative
realistic simulations. Initially, many studies relied on real- macroeconomiclaws[27].
world data scraped from platforms to maintain consistency
System-level Evaluation System-level evaluation is con-
[25, 248]. However, as the scale of these simulations grew
cerned with assessing the overall performance of a simula-
and data acquisition became more challenging, researchers
tion system, irrespective of the specific content being sim-
beganexploringtheuseofsyntheticdata[33]. Furthermore,
ulated. With the growing number of agents in simulation,
toaccommodatetheincreasingdemandforsimulatinglarger
the focus of contemporary research has been on system ef-
numbers of agents, some studies have developed large-scale
ficiencyandassociatedcosts. Efficiencyisassessedthrough
society simulation platforms [265, 266], employing parallel
variousmetrics,suchasthetimeittakestorunasimulation,
processing and other strategies to enhance simulation effi-
the resources that are utilized during the process, and how
ciency.
well the simulation can scale with an increasing number of
Recommendation Environments Another widely studied agents [33, 256, 266]. These metrics are crucial for under-
scenario is the recommendation environment, where these standinghowwellthesystemcanhandlecomplexityandthe
worksuseagentstosimulateuserresponsesinordertovali- demandsoflargersimulations. Onthecostside,evaluations
dateandimproverecommendationalgorithms[254,255]. A often center on the number of tokens consumed during the
key feature across these studies is the use of agents to em- simulationorthefinancialexpenditureincurred[236].

Domain Dataset Type Source #individualnum #dialoguenum Paper Link
FinalDialogueDataset Dialogue Wikipedia / 22,311 [269] Link
P-weiboDataset Dialogue/Description Weibo / 2,000,000 [103] /
P-Ubuntudialoguecorpus Dialogue/Description Corpus / 2,000,000 [103] /
LISCUDataset Description Books,Summaries 9,499 / [54] Link
FoCusDataset Description Wikipedia / 86,712 [102] Link
ConvAI2benchmarkdataset Description Human / 18,878 [118] /
HPDBenchmark Dialogue/Description Books 1 about2,500 [55] Link
LaMPBenchmark Description / / / [113] Link
MultimodalPersonaChat Image/Dialogue Reddit / 15,000 [133] Link
LiveChat Description/Dialogue Douyin 351 1,330,000 [60] Link
COMSET Dialogue Strips 13 53,903 [58] Link
Characters ChatHaruhiDataset Dialogue Movies,Script 32 54,000 [59] Link
RoleBench Dialogue Scripts 100 168,093 [28] Link
Character-LLMDataset Description / 9 14,400 [10] Link
PersonaChatDataset Description / / / [270] Link
CharacterDial Description/Dialogue LiteraryResources,LLM,Human 250 1,034 [62] Link
SyntheticPersonaChat Description/Dialogue LLM 10,371 21,907 [104] Link
RoleEvalDataset Description Wikipedia,Baidu,Fandom,Moegirlpedia 300 6,000 [63] Link
CharacterEvalDataset Description/Dialogue Novels,Scripts 77 1,785 [64] Link
LifeChoiceDataset Description Books 1,401 / [66] /
CrossDataset Description Books / / [67] Link
MMRole-Data Description/Dialogue/Image Wikipedia,Baidu 85 14000 [69] Link
RPDataset Dialogue Novels,Scripts 331 3552 [70] Link
MPIdataset Description / / / [73] Link
WhoisGPT3Dataset / / / / [271] Link
DatasetMovielens1M / / / / [80] Link
EmotionBench / / / / [82] Link
Demographics OpinionQADataset / Surveys / / [91] Link
CultureLLMDataset Dialogue Survey / / [94] Link
PersonaHubDataset Description LLM 200,000 375,000 [98] Link
Table4:Summaryofcommonlyuseddatasetsforindividualsimulation.
6 DatasetsandBenchmarks 6.3 SocialSimulation
We summarize commonly used datasets or benchmarks for
socialsimulationsinTable6. Insocialsimulations, datasets
6.1 IndividualSimulation often consist of two parts: those for initialization of agents
and those for evaluation. Data used for agent initializa-
We summarize commonly used datasets for scenario simu-
tiontypicallycontainprofilesandpotentialrelationsbetween
lation in Table 4. Datasets for individual simulation can be
agents, to helpinitializethe simulation settings. Incontrast,
classified into two types: description datasets and dialogue
datasets for evaluation provide the reference data of behav-
datasets. Descriptiondatasets includeindividual-specificin-
iors of real-world individuals. These datasets are sourced
formation, such as life experiences, relationships, and ba-
in various ways, such as public surveys, existing datasets
sic demographic details like career, age, and gender, often
like MovieLens and Amazon-Book, and crawling from on-
sourced from literature summaries or search engines like
lineplatformslikeTwitter.
Baidu and Wikipedia. Dialogue datasets consist of single-
turnormulti-turnconversationsinspecificscenarios,created
7 TrendofSocialSimulations
byextractingrelevantplotsfortargetedcharactersorgather-
ingutterancesfromsocialmedia. Somedatasetsaredesigned
specifically for evaluation, combining basic personal infor-
mation with customized questions or tasks to assess simula- 7.1 TrendofIndividualSimulation
tionperformance.
Evolving from social science, individual simulation pow-
ered by LLMs has progressed through three distinct stages,
6.2 ScenarioSimulation
namely coarse simulation, more nuanced simulation, and
Wesummarizecommonlyuseddatasetsforscenariosimula- situation-oriented simulation, which is depicted in Fig-
tioninTable5,comprisingdialog-drivenandtask-drivensce- ure5. SinceJune2022,researchersstartedtofocusoncoarse
narios. Thedatasetscoverawiderangeofformats,including simulations, especially for superficial traits like testing the
QA, multiple-choice, rating, code, and game. We observed personalities of LLMs and simulating well-known charac-
thatQAandmultiple-choiceformatsdominatethedatatypes, ters[81,137]. AfterAugust2023,thetrendsshiftedtowards
while domain-specific datasets like judicial, game, and me- morerefinedsimulationsofspecificindividuals,withstudies
dia prefer to preserve domain-tailored data type. Based on evaluatingthecognitiveaspectsofsimulatedmodels[61,67]
task complexity, datasets are categorized into three levels: andimprovingtheirsimulationcapabilities[65,84]. ByMay
easy, medium, and hard. Additionally, according to the col- 2024,researchersbeganconductingindividualsimulationsin
lection methods, datasets are classified as human-annotated, specificscenarios[70,111], furtherexpandingthecomplex-
real-world,orsynthetic. ityandrealismofthesesimulations.

Domain Datasets Type Complexity #case Collection Usedby DataLink
MiniWob++ WebInteraction Hard / human [147] Link
SOTOPIA Open-EndedEnvironment Hard / human [138] Link
WebQuestions QA Easy 5,810 human [149] Link
WebQSP QA Easy 4,737 human [149] Link
CWQ QA Easy 34,689 human [149] Link
GrailQA QA Easy 64,331 human [149] Link
NaturalQuestions QA Easy 323,045 human [147] Link
FairEval QA Medium 80 human [146] Link
MMLU Multiple-Choice Hard 115,700 realworld [29,152,168,172,197] Link
BIG-bench / Hard / human [29,152,193] Link
MetaQA QA Medium 407,513 realworld,human [149] Link
AmazonHistoryPrice ProductInfo Hard 930 realworld [148] Link
MATH MathProblem Medium 12,500 realworld [147] Link
Arithmetic MathExpression Easy / human [29] Link
Counter-IntuitiveAR ReasoningProblem Easy 200 human [145] Link
CommonMT TranslationTriple Medium 1,200 human [145] Link
Dialog-
Overcooked-AI Game Medium / human [198] Link
Driven
AVALONBENCH Game Easy / human [153] Link
Jubensha Game Medium 1,115 realworld [156] Link
FanLang-9 Game Easy 18,800 realworld [158] Link
WellPlay QA Hard 1,482 human [160] Link
WWQA QA Medium 2,053 synthetic [159] Link
Biographies Biographies Easy 524 realworld [29] Link
ALFWorld EmbodiedEnvironment Medium 3,827 human [147] Link
EDdataset Conversational Hard 24,850 human [142] Link
Topical-Chat Conversational Medium 10,784 human [146] Link
COPA Multiple-Choice Easy 500 realworld [144] Link
αNLI Multiple-Choice Easy 1,507 human [144] Link
CSQA Multiple-Choice Easy 1,221 human [144] Link
SocialIQa Multiple-Choice Easy 1,935 human [144] Link
PIQA Multiple-Choice Easy 1,838 human [144,197] Link
StrategyQA Multiple-Choice Easy 2,290 human [144] Link
e-CARE Multiple-Choice Easy 2,122 human [144] Link
WiKiTQ QA Easy 22,033 realworld [174] Link
TabFact QA Hard 118,275 realworld,human [174] Link
FeTaQA QA Hard 10,330 realworld,human [174] Link
HumanEval Code Easy 164 realworld [17,172,176,193] Link
MBPP Code Easy 974 realworld [17,176] Link
APPS Code Easy / realworld [176] Link
Code Conversational Hard 50,000 synthetic [188] Link
CoderEval Code Medium 230 realworld [176] Link
SRDD SoftwareRequirement Medium 1,200 synthetic [172,177,178,180] Link
SoftwareDev TaskPrompt Hard 70 human [17] Link
SWE-bench Code Easy 2,294 realworld [179] Link
AISociety Conversational Easy 25,000 synthetic [188] Link
SynthPAI Comment Hard 7,823 synthetic [48] Link
ScienceWorld InteractiveEnvironment Hard / human [189] Link
Science QA Medium 60,000 synthetic [188] Link
TriviaQA QA Easy 650,000 realworld [195] Link
MT-bench QA Medium 80 human [195] Link
RoCoBench-Text QA Medium 269 human [192] Link
PubMedQA QA Medium 273,500 human,synthetic [168] Link
MedQA Multiple-Choice Medium 61,097 realworld [168,175] Link
Task-
DDXPlus MedicalRecord Hard 1,300,000 synthetic [166] Link
Driven
MedMCQA Multiple-Choice Hard 194,000 realworld [168] Link
MVME MedicalRecord Medium 506 realworld [19] Link
ARIES ReviewComment Easy 3,900 human,synthetic [30] Link
Reviewer2 Review Easy 99,727 human,synthetic [169] Link
GSM8K MathProblem Easy 8,500 human [29,184] Link
MGSM MathProblem Hard 2,750 human [193] Link
Math QA Hard 50,000 synthetic [152,188] Link
SimuCourt LegalCases Medium 420 realworld [20] Link
KINLED Conversational Medium 10,546 human,synthetic [186] Link
SupremeCourtDatabase LegalCases Easy 9,095 realworld [181] Link
TDW-MAT EmbodiedEnvironment Medium / human [191] Link
C-WAH EmbodiedEnvironment Medium / human [191] Link
RoCoBench EmbodiedEnvironment Medium / human [192] Link
FED DialogueResponse Medium 4,712 human [193] Link
CulturePark Conversational Medium 41,000 synthetic [50] Link
CommonGen-Hard Concept Easy 200 human [172,193] Link
ARCChallenge Multiple-Choice Easy 2,590 human [197] Link
HellaSwag Multiple-Choice Easy 70,000 synthetic [197] Link
UCF101 VideoClip Medium 7,000 human [173] Link
HMDB51 VideoClip Medium 13,320 realworld [173] Link
Table5:Summaryofcommonlyuseddatasetsforscenariosimulation.

Scenario Dataset Init. Eval. Content #case SimulationObjectives Usedby DataLink
2018U.S.population ✓ profile 100people macroeconomicactivities [27] Link
publicgovernmentdata ✓ rentinformation 51users resourceallocation [221] Link
names-dataset3.1.0 ✓ profile 1,000people epidemicmodeling [224] Link
General big-five-data ✓ profile 1,000people epidemicmodeling [224] Link
Economics AmericanCommunitySurvey ✓ profile 8.4Mpeople epidemicmodeling [225] Link
BureauofLaborStatistics ✓ laborstatistics 8.4Mpeople unemploymentrate [225] Link
CDC ✓ infectionrate 8.4Mpeople epidemicmodeling [225] Link
ANES ✓ ✓ profile,answer 15,626responses voting [12,96,227] Link
PigeonholingPartisans ✓ ✓ profile,answer 2,107responses partisanbias [12] Link
GlobalWarming ✓ ✓ profile,answer 2,310responses opinion [226] /
Twitter ✓ statements 1,006,517users voting [227] /
Interview ✓ ✓ profile,answer 1,002users opnionandbehavior [229] Link
Name ✓ name 500names / [230] Link
UltimatumGame ✓ moneyallocation 10,000pairs moneyallocation [230] Link
Sociology GardenPathSentences ✓ gardenpathsentences 96sentences languageparsing [230] Link
and WisdomofCrowds ✓ answerstoquestions 15,000answers wisdomofcrowds [230] Link
PoliticalScience MilgramShockExperiment ✓ behaviorrecords 100people obediencebehavior [230] Link
15Topics ✓ profile,opinion 10users opiniondynamics [24] Link
FormativeStudy ✓ ✓ profile,interview 14users information [233] /
management
UserStudy ✓ ✓ profile,interview 36users information [233] /
management
collectivedecision-making ✓ ✓ profile,opinion 2,290users collective [234] /
decision-making
Becker-2019 ✓ ✓ profile,answers 1,120users wisdomofcrowds [31] Link
ControversialBeliefsSurvey ✓ ✓ profile,opinion 564users opinion [240] /
FPS ✓ / 6topics opiniondynamics [26] /
EchoChambers ✓ profile 3networks opinionpolarization [245] /
GenderDiscrimination ✓ ✓ profile,opinion 8,563users opiniondynamics [248] /
NuclearEnergy ✓ ✓ profile,opinion 17,945users opiniondynamics [248] /
ANES ✓ profile 500users partisanbias [249] Link
SAGraph ✓ ✓ profile,interaction 40300influencers influencerselection [251] /
Metoo ✓ ✓ profile,opinion 1,000users opiniondynamics [25] Link
Roe ✓ ✓ profile,opinion 1,000users opiniondynamics [25] Link
BLM ✓ ✓ profile,opinion 1,000users opiniondynamics [25] Link
Online Twitter15 ✓ ✓ profile,behavior 198news rumorpropagation [33] Link
Platforms Twitter16 ✓ ✓ profile,behavior 198news rumorpropagation [33] Link
Reddit ✓ ✓ profile,comment 116,932comments herdeffect [33] /
MindEcho ✓ ✓ profile,comment 14KOL keyopinionleader [252] /
WARRIORS ✓ ✓ profile, 100,000users searchbehavior [253] /
searchbehavior
AmazonBeauty ✓ ✓ profile, 15,577users user-item [254] Link
user-iteminteraction interaction
Steam ✓ ✓ profile, 281,205users user-item [254,257] Link
user-iteminteraction interaction
MovieLens ✓ ✓ profile, 298,074users user-item [254,256,257] Link
user-iteminteraction interaction
AmazonBook ✓ ✓ profile, / user-item [257] Link
user-iteminteraction interaction
AmazonReviewCD ✓ ✓ profile, 100users user-item [258] Link
user-iteminteraction interaction
AmazonReviewOffice ✓ ✓ profile, 100users user-item [258] Link
user-iteminteraction interaction
Table6: Summaryofcommonlyuseddatasetsforsocietysimulation. Init. meansthedataprovidesprofiletoinitializeagents, andEval.
meansitprovidesdatatovalidatethesimulationeffectiveness.

Individual Simulation
Coarse Simulation on More Nuanced Simulation on Situation-oriented
Superficial Features Specific Characters Simulation
Conversational Health Agents [84]
Out of one, many [12]
Demographic Chain of Empathy [89] Interactive Agents [100]
Improving Personality Consistency [74]
Persona CultureLLM [94] HIRPF[123]
The wall street neophyte [76]
Faithful Persona-based Conversational Dataset [104]
RoleLLM [28]
Capturing Minds, Not Just Words[68]
CharacterLLM [10]
Charactcer Large Language Models Meet Harry Potter [55] InCharacter [61] MMRole [69]
Creating a Large Language Model of a Philosopher [56] CharacterGLM [62] Beyond Dialogue [70]
Persona
LiveChat [60] Neeko [65] From Role-Play to Drama-Interaction [105]
Character is Destiny [66] Social Bench [111] Year
Evaluating Character Understanding [67]
Jun. 2022 Aug. 2023 Apr. 2024
Figure5:Illustrationofindividualsimulationtrend,whichgoesthroughcoarsesimulation,morenuancedsimulation,andsituation-oriented
simulation.
Scenario Simulation
Simple Scenario Multi-Stage Scenario Collaborative Scenario
Improving factuality and reasoning [29] MetaGPT [17] Self-Emotion [141]
Dialog-Driven ChatLLM [49] Empirical Study on Werewolf [150] DoG [149]
ICL-AIF [143] Recon [151]
Scenario S-Agents [164]
FORD [144] MachineSoM [152]
GITM [161] AvalonBench [153] AgentSense [205]
Task-Driven D Se E l R f-c A o [ l 1 la 7 b 5 o ] ration [176] V C Tr I h a D a d S t i D n [ g e 1 G v 6 5 [ P 1 ] T 7 7 [1 ] 82] A M I A H T o H s V p C ita [ l 1 [ 8 1 4 9 ] ]
TWOSOME [197]
Scenario Blind Judgement [181] Multi-Agent Collaboration [190]
CAMEL [188] C R o o E C L o A [1 [ 9 1 2 9 ] 1] R AG eA A d [ 2 [1 3 9 6 8 ] ]
Year
Jan. 2023 Jun. 2023 Feb. 2024
Figure6:Illustrationofscenariosimulationtrend,whichgoesthroughsimplescenario,multi-stagescenario,andcollaborativescenario.
7.1.1 CoarseSimulationonSuperficialFeatures the individual simulation gained growing attention. Some
Many individual simulation works born since June 2022, works implement new functionalities and refine the mod-
the majority of which initially focus on simulating superfi- els’ architecture, such as incorporating memory and plan-
cialfeatures impliedinhuman behaviors. Asignificantpor- ningmodules[66,84], whileothersfocusondesigningspe-
tion of the effort was dedicated to collecting and standard- cifictasksfortrainingandevaluation,likemulti-dimensional
izing character-related information to build persona-based interviews [61] and simulation with rich information from
datasets [55, 56]. Additionally, eliciting the underlying de- scenedescriptionsandexperientialmemories[28].
mographic personalities of prevailing LLMs posed a chal-
7.1.3 Situation-OrientedSimulation
lengeinthisearlystage[81,120]. Theearlytrialsoncoarse
individual simulations shed light on LLMs’ attributes dur- Situation-oriented individual simulations begin within game
ingsimulation,includinghallucinations,inherentbiases,and environments [119], where LLMs are required to make ap-
stereotypes,whichareproventobecrucialforfuturesimula- propriatedecisionsbasedonpredefinedrules. Inmorecom-
tions. plexenvironments,simulatedindividualsaresupposedtoin-
teract dynamically with their surroundings, responding to
7.1.2 MoreNuancedSimulationonSpecificCharacters real-time environmental feedback [100, 111]. Beyond tra-
Asindividualsimulationmethodsadvanced,theprecisionof ditionalsimulationslikedialogue, situation-orientedsimula-
simulationssignificantlyimproved. Morenuancedaspectsof tionsexpandintoareassuchasdramaticperformances[105],

Society Simulation
Constructing Preliminary Exploring Alignment on Scaling up and towards
Environments Specific Scenarios Multi-Modal
Choicemates [233] Prisoner's Dilemma [214]
General Economics Epidemic Modeling[224] EconAgent [27]
Holacracy view [277]
Personality Traits [239]
RecAgent [256] HiSim [25]
S^3 [248] FPS [26]
Online Platform Social Simulacra [247] AgentCF [258] Influencer Selection [251]
Agent4Rec [257] AgentTorch [225]
News Feed [249] OASIS [33]
WarAgent [47] CRSEC [232]
Sociology and Politics Generative Agents [57] Wisdom of Partisan Crowds [31] Instruments of Power [13]
AgentSims [199] Beyond Demographics [240]
Public Administration Crisis [228] ElectionSim [227] Year
Mar. 2023 Jun. 2023 Feb. 2024
Figure 7: Illustration of society simulation trend, which goes through three stages: constructing preliminary environments, exploring
alignmentonspecificscenarios,andscalingupwhilemovingtowardsmulti-modal.
digitalgameexploration[109],and3Dtaskexecution[107]. 7.2.2 Multi-StageScenario
As the complexity of these simulations grows, the demands Different from simple task-oriented scenarios, multi-stage
ontheunderlyingarchitecturegrowaswell. scenariosarenolongerlimitedtomereagentinteractions.In-
stead,theyemphasizethefine-grainedconstructionofscenar-
ios. This stage introduces multiple roles and task decompo-
7.2 TrendofScenarioSimulation
sitionascentralelements,enablingagentstocollaboratenot
merely on single tasks but through incremental task break-
The development of scenario simulation has progressed
downsthatrequirecoordinatedeffort[191,192]. Insoftware
throughseveraldistinctstages. StartingfromJanuary2023,
development, [17, 177] decomposed the development pro-
different researches focused primarily on simple scenarios
cess into multiple stages like design, coding and testing to
concerning single objectives and facilitated basic contextual
enhance the capacity for achieving complex objectives and
interactions[144,175,181,188]. ByJune2023,theempha-
improving software quality. Additionally, communication
sischangedtomulti-stagescenarios,incorporatingmulti-step
gameswereintroducedtoinvestigatehumanbehaviorwithin
tasks that enabled agents to engage in sequential decision-
complexconversationalscenarios,addingdepthtointeraction
making and adaptive responses across varied contexts to
analysis[150–153].
achieve the more complex goal [165, 182, 190, 192]. By
February 2024, research has increasingly focused on multi- 7.2.3 CollaborativeScenario
agent collaborative scenarios, emphasizing agents’ capabili- With the growing interest in scenario simulation, research
tiestocooperateandadaptwithincomplex,high-ordersimu- shiftedtowardcollaborativescenarios,emphasizingadvanced
lations[149,164,184,236]. social dynamics and cooperative strategies in agent interac-
tions. [197, 198] introduce reinforcement learning to align
LLM with embodied environments. To build efficient sce-
7.2.1 SimpleScenario
nario simulations, [236] focused on reducing LLM infer-
In the initial phase of scenario simulation, researchers fo- ence costs by modeling social relationships while [164] uti-
cused on constructing simple scenarios that supported foun- lized dynamic “agent trees” in environments like Minecraft,
dational agent interactions. Much of this work concentrated enabling asynchronous task execution for efficient resource
on dialogue-driven decision-making frameworks, which fa- gathering. Inaddition, [19,141]simulatedcollaborativeen-
cilitated structured information exchange and agent align- vironments in the real world, reflecting complex social in-
ment [49, 175, 188]. Additionally, studies explored the col- teractionssuchasmedicalprocessesandthedevelopmentof
laborative potentials of agents through multi-agent debate socialskills,withagentshandlingevolvingmultisteptasks.
frameworks, employing debate and critical feedback to as-
7.3 TrendofSocietySimulation
sesscooperativereasoningandperformanceenhancementin
LLMs [29, 143, 144]. Simultaneously, other studies applied Sincetheconceptofsocialsimulationwasfirstintroducedby
scenario simulations within specific domains—such as law, Park et al. [247], numerous notable studies have emerged.
software development, scientific analysis, and recommen- Broadly,thedevelopmentofthisfieldcanbecategorizedinto
dation systems—demonstrating the versatility of task-based three phases. Prior to June 2023, researchers concentrated
simulations in achieving domain-specific objectives [161, onconstructingpreliminaryenvironments[32,199,224]. By
176,181]. February2024,thefocusshiftedtowardexploringalignment

within specific scenarios, such as persona modeling and tar- hottopicinresearch. Itincorporatesothermodalinformation
geted environments, marking the first significant surge of elementssuchasvisioninlifeintothesimulationthroughtext
publications [27, 248, 272]. Most recently, the trend has descriptions. However,withaseriesofadvancesinthefield
movedtowardsscalingupandincorporatingmulti-modalap- ofVision-LanguageModel(VLM)[36,275,276],researchers
proaches. In this phase, large-scale precise modeling has began to incorporate VLM-based agents into society simu-
gainedrecognition, withothermodalitiessuchasvisionand lation research. [273] provide rich multi-modal interaction
voicebeingintegratedintosimulations[25,158,232,273]. information and detailed annotations in large-scale scenar-
Themaincharacteristicscanbesummarizedas: ios. [237]focusonsimulatingtheperceptuallimitationsand
physicaldemandsoftherealworldtofacilitatemorerealistic
7.3.1 ConstructingPreliminaryEnvironments
socialinteractions.
The complexity of society simulation, to a certain extent,
stemsfromthecomplexityoftheenvironmentinvolved. So-
8 Conclusion
cietysimulationusuallyinvolvemultipleinteractingindivid-
uals (such as people, organizations, groups, etc.), which act In this paper, we categorize LLM-driven social simulations
inaspecificenvironment(suchascities,markets,cyberspace, into three types: individual, scenario, and society simula-
etc.). Therefore,thepioneerworkfocusesonhowtodesigna tion, highlighting their progression from modeling individ-
specificenvironmenttosupportsocietysimulation. [32]built ual behaviors to replicating complex social dynamics. By
an interactive sandbox environment by extending a LLM to systematically reviewing architectures, methods, and evalu-
storeacompleterecordofanagent’sexperienceanddynam- ationsacrossthesecategories,weprovideastructuredframe-
ically synthesizing memory to plan behavior. [224] built an workforadvancingresearchinthisfield. Thisworkaimsto
epidemic spread simulation environment that simulates hu- guidethedevelopmentofLLM-basedsimulationsandfoster
manbehaviorattheindividualleveltoreproducethespread interdisciplinarystudiestoaddressreal-worldchallengesand
of an epidemic in a simulated environment. [199] created supportdecision-making.
aneasy-to-use infrastructurethatallows researcherstobuild
evaluationtasksbyaddingagentsandbuildings,providinga References
visualandprogram-basedplatformfortestingLLMs.
[1] MarkSGranovetter. Thestrengthofweakties. Amer-
7.3.2 ExploringAlignmentonSpecificScenarios icanjournalofsociology,78(6):1360–1380,1973.
Withthedevelopmentofsimulationenvironmenttechnology,
[2] DanielKatzandRobertKahn. Thesocialpsychology
societysimulationhasbasicallybecomeoperational. Atthis
oforganizations. InOrganizationalbehavior2,pages
time,totestthecredibilityofsimulation,evaluatingthealign-
152–168.Routledge,2015.
ment performance of agents with real situations on specific
tasks has gradually become an important research direction. [3] SE ASCH. Effects of group pressure upon the mod-
[248]userealsocialnetworkdatatomeasuretheaccuracyof ification and distortion of judgments. Groups, Lead-
simulation by evaluating the behavior and decision-making ership and Men: Research in Human Relations, page
of agents at the individual and group levels in a simulated 177,1951.
social network environment. [27] evaluate the decision ra- [4] StanleyMilgram. Behavioralstudyofobedience. The
tionality of LLM agents by simulating macroeconomic ac-
Journalofabnormalandsocialpsychology,67(4):371,
tivities and comparing the performance of LLM agents with
1963.
traditional rule-based agents or language agents in generat-
ingclassicmacroeconomicphenomenasuchasinflationand [5] JasonWei, XuezhiWang, DaleSchuurmans, Maarten
unemployment. Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
etal. Chain-of-thoughtpromptingelicitsreasoningin
7.3.3 ScalingUpandtowardsMulti-Modal large language models. Advances in neural informa-
Scaling up Before LLM-based agents became widely tionprocessingsystems,35:24824–24837,2022.
adoptedforsocietysimulation,researcherspredominantlyre-
[6] TakeshiKojima,ShixiangShaneGu,MachelReid,Yu-
liedonagent-basedmodeling(ABM)methods,whereagents
taka Matsuo, and Yusuke Iwasawa. Large language
were typically programmed to react based on predefined al-
modelsarezero-shotreasoners.Advancesinneuralin-
gorithms. With the advent of LLM providing glimpses of
formationprocessingsystems,35:22199–22213,2022.
human-likeintelligence[274],LLM-basedagentsenteredthe
spotlight. GiventhegoodperformanceofLLM-basedagents [7] Zhiheng Xi, Wenxiang Chen, Xin Guo, Wei He, Yi-
inaseriesofspecificscenarios,researchersbegantoexpand wenDing,BoyangHong,MingZhang,JunzheWang,
the scale of simulation. [25, 232] involve the core elements SenjieJin,EnyuZhou,etal. Theriseandpotentialof
oflarge-scalesocietysimulationandstudytheinteractionbe- large language model based agents: A survey. arXiv
tween agents and the generation of behavioral norms. [158] preprintarXiv:2309.07864,2023.
proposedaprovinggroundforassessingadvancedreasoning
[8] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,
capabilitiesofLLMagentsinalarge-scalesocietysimulation
Tom Griffiths, Yuan Cao, and Karthik Narasimhan.
context.
Tree of thoughts: Deliberate problem solving with
Multi-Modal With the development of language models, large language models. Advances in Neural Informa-
using language agents for society simulation has become a tionProcessingSystems,36,2024.

[9] Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, [20] ZhitaoHe,PengfeiCao,ChenhaoWang,ZhuoranJin,
HaoYang,JingsenZhang,ZhiyuanChen,JiakaiTang, Yubo Chen, Jiexin Xu, Huaijun Li, Xiaojian Jiang,
XuChen,YankaiLin,WayneXinZhao,ZheweiWei, Kang Liu, and Jun Zhao. Simucourt: Building ju-
and Jirong Wen. A survey on large language model dicial decision-making agents with real-world judge-
basedautonomousagents. FrontiersofComputerSci- ment documents. arXiv preprint arXiv:2403.02959,
ence,18(6),March2024. 2024.
[10] Yunfan Shao, Linyang Li, Junqi Dai, and Xipeng [21] Thomas C Schelling. Dynamic models of segrega-
Qiu.Character-llm:Atrainableagentforrole-playing, tion. Journal of mathematical sociology, 1(2):143–
2023. 186,1971.
[22] Rainer Hegselmann and Ulrich Krause. Opinion dy-
[11] JiangjieChen,XintaoWang,RuiXu,SiyuYuan,Yikai
namicsdrivenbyvariouswaysofaveraging. Compu-
Zhang, Wei Shi, Jian Xie, Shuang Li, Ruihan Yang,
tationalEconomics,25:381–405,2005.
TinghuiZhu,etal.Frompersonatopersonalization:A
surveyonrole-playinglanguageagents.arXivpreprint [23] Yun-ShiuanChuangandTimothyTRogers.Computa-
arXiv:2404.18231,2024. tionalagent-basedmodelsinopiniondynamics:Asur-
veyonsocialsimulationsandempiricalstudies. arXiv
[12] Lisa P. Argyle, Ethan C. Busby, Nancy Fulda,
preprintarXiv:2306.03446,2023.
Joshua R. Gubler, Christopher Rytting, and David
[24] Yun-Shiuan Chuang, Agam Goyal, Nikunj Harlalka,
Wingate. Out of one, many: Using language mod-
Siddharth Suresh, Robert Hawkins, Sijia Yang, Dha-
els to simulate human samples. Political Analysis,
van Shah, Junjie Hu, and Timothy T Rogers. Simu-
31(3):337–351,February2023.
lating opinion dynamics with networks of llm-based
[13] Yaqub Chaudhary and Jonnie Penn. Large language agents. arXivpreprintarXiv:2311.09618,2023.
models as instruments of power: New regimes of au-
[25] XinyiMou,ZhongyuWei,andXuanjingHuang. Un-
tonomous manipulation and control. arXiv preprint
veiling the truth and facilitating change: Towards
arXiv:2405.03813,2024.
agent-based large-scale social movement simulation.
[14] Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi arXivpreprintarXiv:2402.16333,2024.
Chang,ShichaoPei,NiteshVChawla,OlafWiest,and [26] YuhanLiu,XiuyingChen,XiaoqingZhang,XingGao,
XiangliangZhang.Largelanguagemodelbasedmulti- Ji Zhang, and Rui Yan. From skepticism to accep-
agents: A survey of progress and challenges. arXiv tance: Simulating the attitude dynamics toward fake
preprintarXiv:2402.01680,2024. news. arXivpreprintarXiv:2403.09498,2024.
[15] ChenGao,XiaochongLan,NianLi,YuanYuan,Jing- [27] N.Li,C.Gao,M.Li,etal.Econagent:Largelanguage
taoDing,ZhilunZhou,FengliXu,andYongLi. Large model-empowered agents for simulating macroeco-
language models empowered agent-based modeling nomic activities. In Proceedings of the 62nd Annual
and simulation: A survey and perspectives. Humani- MeetingoftheAssociationforComputationalLinguis-
tiesandSocialSciencesCommunications,11(1):1–24, tics (Volume 1: Long Papers), pages 15523–15536,
2024. 2024.
[16] Chen Qian, Xin Cong, Wei Liu, Cheng Yang, Weize [28] Zekun Moore Wang, Zhongyuan Peng, Haoran
Que, Jiaheng Liu, Wangchunshu Zhou, Yuhan Wu,
Chen,YushengSu,YufanDang,JiahaoLi,JuyuanXu,
Hongcheng Guo, Ruitong Gan, Zehao Ni, Jian Yang,
Dahai Li, et al. Communicative agents for software
ManZhang,ZhaoxiangZhang,WanliOuyang,KeXu,
development. arXivpreprintarXiv:2307.07924,2023.
StephenW.Huang,JieFu,andJunranPeng. Rolellm:
[17] Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Benchmarking, eliciting, and enhancing role-playing
Cheng,JinlinWang,CeyaoZhang,ZiliWang,Steven abilitiesoflargelanguagemodels,2024.
Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al.
[29] Yilun Du, Shuang Li, Antonio Torralba, Joshua B
Metagpt: Meta programming for multi-agent collab-
Tenenbaum,andIgorMordatch. Improvingfactuality
orativeframework. arXivpreprintarXiv:2308.00352,
andreasoninginlanguagemodelsthroughmultiagent
2023.
debate. arXivpreprintarXiv:2305.14325,2023.
[18] Junkai Li, Siyu Wang, Meng Zhang, Weitao Li, [30] MikeD’Arcy,TomHope,LarryBirnbaum,andDoug
Yunghwei Lai, Xinhui Kang, Weizhi Ma, and Yang Downey. Marg:Multi-agentreviewgenerationforsci-
Liu. Agent hospital: A simulacrum of hospi- entificpapers.arXivpreprintarXiv:2401.04259,2024.
tal with evolvable medical agents. arXiv preprint
[31] Yun-Shiuan Chuang, Nikunj Harlalka, Siddharth
arXiv:2405.02957,2024.
Suresh, Agam Goyal, Robert Hawkins, Sijia Yang,
[19] Zhihao Fan, Jialong Tang, Wei Chen, Siyuan Wang, DhavanShah,JunjieHu,andTimothyTRogers. The
Zhongyu Wei, Jun Xi, Fei Huang, and Jingren Zhou. wisdom of partisan crowds: Comparing collective in-
Ai hospital: Interactive evaluation and collaboration telligence in humans and llm-based agents. In Pro-
of llms as intern doctors for clinical diagnosis. arXiv ceedings of the Annual Meeting of the Cognitive Sci-
preprintarXiv:2402.09742,2024. enceSociety,volume46,2024.

[32] Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, llmswithdatabasesastheirsymbolicmemory. arXiv
Meredith Ringel Morris, Percy Liang, and Michael S preprintarXiv:2306.03901,2023.
Bernstein. Generativeagents: Interactivesimulacraof
[45] Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye,
human behavior. In Proceedings of the 36th annual
andYanlinWang. Memorybank: Enhancinglargelan-
acm symposium on user interface software and tech-
guagemodelswithlong-termmemory. InProceedings
nology,pages1–22,2023.
oftheAAAIConferenceonArtificialIntelligence,vol-
[33] Ziyi Yang, Zaibin Zhang, Zirui Zheng, Yuxian Jiang, ume38/17,pages19724–19731,2024.
Ziyue Gan, Zhiyu Wang, Zijian Ling, Jinsong Chen,
[46] JingqingRuan,YihongChen,BinZhang,ZhiweiXu,
Martz Ma, Bowen Dong, et al. Oasis: Open agents
TianpengBao,GuoqingDu,ShiweiShi,HangyuMao,
social interaction simulations on one million agents.
Ziyue Li, Xingyu Zeng, et al. Tptu: large language
arXivpreprintarXiv:2411.11581,2024.
model-basedaiagentsfortaskplanningandtoolusage.
[34] Junwei Liu, Kaixin Wang, Yixuan Chen, Xin Peng, arXivpreprintarXiv:2308.03427,2023.
Zhenpeng Chen, Lingming Zhang, and Yiling Lou.
[47] WenyueHua,LizhouFan,LingyaoLi,KaiMei,Jian-
Largelanguagemodel-basedagentsforsoftwareengi-
chaoJi,YingqiangGe,LibbyHemphill,andYongfeng
neering: A survey. arXiv preprint arXiv:2409.02977,
Zhang. War and peace (waragent): Large language
2024.
model-based multi-agent simulation of world wars.
[35] Tom B Brown. Language models are few-shot learn- arXivpreprintarXiv:2311.17227,2023.
ers. arXivpreprintarXiv:2005.14165,2020.
[48] Chen Qian, Zihao Xie, Yifei Wang, Wei Liu,
[36] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Yufan Dang, Zhuoyun Du, Weize Chen, Cheng
Ahmad,IlgeAkkaya,FlorenciaLeoniAleman,Diogo Yang, Zhiyuan Liu, and Maosong Sun. Scal-
Almeida, Janko Altenschmidt, Sam Altman, Shyamal ing large-language-model-based multi-agent collabo-
Anadkat,etal. Gpt-4technicalreport. arXivpreprint ration. arXivpreprintarXiv:2406.07155,2024.
arXiv:2303.08774,2023.
[49] Rui Hao, Linmei Hu, Weijian Qi, Qingliu Wu,
[37] Kevin A Fischer. Reflective linguistic programming Yirui Zhang, and Liqiang Nie. Chatllm network:
(rlp): A stepping stone in socially-aware agi (so- More brains, more intelligence. arXiv preprint
cialagi). arXivpreprintarXiv:2305.12647,2023. arXiv:2304.12998,2023.
[38] Lei Wang, Jingsen Zhang, Hao Yang, Zhiyuan Chen, [50] ChengLi,DamienTeney,LinyiYang,QingsongWen,
Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Rui- Xing Xie, and Jindong Wang. Culturepark: Boosting
huaSong,WayneXinZhao,etal. Userbehaviorsim- cross-culturalunderstandinginlargelanguagemodels.
ulationwithlargelanguagemodelbasedagents. arXiv arXivpreprintarXiv:2405.15145,2024.
preprintarXiv:2306.02552,2023.
[51] Weize Chen, Chenfei Yuan, Jiarui Yuan, Yusheng
[39] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Su, Chen Qian, Cheng Yang, Ruobing Xie, Zhiyuan
Shafran, Karthik Narasimhan, and Yuan Cao. React: Liu, and Maosong Sun. Beyond natural lan-
Synergizingreasoningandactinginlanguagemodels. guage: Llms leveraging alternative formats for en-
arXivpreprintarXiv:2210.03629,2022. hancedreasoningandcommunication. arXivpreprint
[40] Shibo Hao, Yi Gu, Haodi Ma, Joshua Jiahua Hong, arXiv:2402.18439,2024.
Zhen Wang, Daisy Zhe Wang, and Zhiting Hu. Rea- [52] Chau Pham, Boyi Liu, Yingxiang Yang, Zhengyu
soning with language model is planning with world Chen, Tianyi Liu, Jianbo Yuan, Bryan A Plummer,
model. arXivpreprintarXiv:2305.14992,2023. ZhaoranWang,andHongxiaYang. Letmodelsspeak
[41] Aaron Parisi, Yao Zhao, and Noah Fiedel. Talm: ciphers: Multiagent debate through embeddings. In
Tool augmented language models. arXiv preprint The Twelfth International Conference on Learning
arXiv:2205.12255,2022. Representations,2024.
[42] Timo Schick, Jane Dwivedi-Yu, Roberto Dess`ı, [53] Samuele Marro, Emanuele La Malfa, Jesse Wright,
Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke GuohaoLi,NigelShadbolt,MichaelWooldridge,and
Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Philip Torr. A scalable communication protocol for
Toolformer:Languagemodelscanteachthemselvesto networks of large language models. arXiv preprint
usetools. AdvancesinNeuralInformationProcessing arXiv:2410.11905,2024.
Systems,36,2024. [54] Faeze Brahman, Meng Huang, Oyvind Tafjord, Chao
[43] Noah Shinn, Federico Cassano, Ashwin Gopinath, Zhao, Mrinmaya Sachan, and Snigdha Chaturvedi.
Karthik Narasimhan, and Shunyu Yao. Reflexion: ”let your characters tell their story”: A dataset for
Language agents with verbal reinforcement learning. character-centricnarrativeunderstanding,2021.
Advances in Neural Information Processing Systems,
[55] NuoChen,YanWang,HaiyunJiang,DengCai,Yuhan
36,2024.
Li, Ziyang Chen, Longyue Wang, and Jia Li. Large
[44] Chenxu Hu, Jie Fu, Chenzhuang Du, Simian Luo, languagemodelsmeetharrypotter:Abilingualdataset
Junbo Zhao, and Hang Zhao. Chatdb: Augmenting foraligningdialogueagentswithcharacters,2023.

[56] Eric Schwitzgebel, David Schwitzgebel, and Anna Yang. Evaluating character understanding of large
Strasser.Creatingalargelanguagemodelofaphiloso- languagemodelsviacharacterprofilingfromfictional
pher,2023. works,2024.
[57] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, [68] Yiting Ran, Xintao Wang, Rui Xu, Xinfeng Yuan, Ji-
MeredithRingelMorris,PercyLiang,andMichaelS. aqingLiang,YanghuaXiao,andDeqingYang.Captur-
Bernstein. Generativeagents: Interactivesimulacraof ingminds,notjustwords:Enhancingrole-playinglan-
humanbehavior,2023. guagemodelswithpersonality-indicativedata,2024.
[58] Harsh Agrawal, Aditya Mishra, Manish Gupta, and [69] Yanqi Dai, Huanran Hu, Lei Wang, Shengjie Jin,
Mausam. Multimodal persona based generation of Xu Chen, and Zhiwu Lu. Mmrole: A comprehensive
comicdialogs. InAnnaRogers,JordanBoyd-Graber, framework for developing and evaluating multimodal
and Naoaki Okazaki, editors, Proceedings of the 61st role-playingagents,2024.
AnnualMeetingoftheAssociationforComputational [70] Yeyong Yu, Runsheng Yu, Haojie Wei, Zhanqiu
Linguistics (Volume 1: Long Papers), pages 14150– Zhang, and Quan Qian. Beyond dialogue: A profile-
14164, Toronto, Canada, July 2023. Association for dialogue alignment framework towards general role-
ComputationalLinguistics. playinglanguagemodel,2024.
[59] Cheng Li, Ziang Leng, Chenxi Yan, Junyi Shen, Hao [71] LinzhuangSun,YaoDong,NanXu,JingxuanWei,Bi-
Wang, Weishi MI, Yaying Fei, Xiaoyang Feng, Song hui Yu, and Yin Luo. Rational sensibility: Llm en-
Yan, HaoSheng Wang, Linkang Zhan, Yaokai Jia, hancedempatheticresponsegenerationguidedbyself-
PingyuWu, andHaozhenSun. Chatharuhi: Reviving presentationtheory. arXivpreprintarXiv:2312.08702,
anime character in reality via large language model, 2023.
2023.
[72] SakethReddyKarra,SonTheNguyen,andThejaTu-
[60] JingshengGao,YixinLian,ZiyiZhou,YuzhuoFu,and labandhula. Estimating the personality of white-box
BaoyuanWang. Livechat: Alarge-scalepersonalized languagemodels,2023.
dialogue dataset automatically constructed from live
[73] Guangyuan Jiang, Manjie Xu, Song-Chun Zhu, Wen-
streaming,2023.
juanHan, ChiZhang, andYixinZhu. Evaluatingand
[61] XintaoWang,YunzeXiao,JentseHuang,SiyuYuan, inducing personality in pre-trained language models,
Rui Xu, Haoran Guo, Quan Tu, Yaying Fei, Ziang 2023.
Leng, Wei Wang, Jiangjie Chen, Cheng Li, and [74] Yifan Liu, Wei Wei, Jiayi Liu, Xianling Mao, Rui
YanghuaXiao. Incharacter: Evaluatingpersonalityfi-
Fang, and Dangyang Chen. Improving personality
delityinrole-playingagentsthroughpsychologicalin-
consistency in conversation by persona extending. In
terviews,2024.
Proceedingsofthe31stACMInternationalConference
[62] JinfengZhou,ZhuangChen,DazhenWan,BosiWen, onInformation&KnowledgeManagement,volume39
Yi Song, Jifan Yu, Yongkang Huang, Libiao Peng, ofCIKM’22,page1350–1359.ACM,October2022.
Jiaming Yang, Xiyao Xiao, Sahand Sabour, Xiaohan [75] John J. Horton. Large language models as simulated
Zhang, Wenjing Hou, Yijia Zhang, Yuxiao Dong, Jie
economicagents: Whatcanwelearnfromhomosili-
Tang, and Minlie Huang. Characterglm: Customiz-
cus?,2023.
ingchineseconversationalaicharacterswithlargelan-
[76] QianqianXie,WeiguangHan,YanzhaoLai,MinPeng,
guagemodels,2023.
and Jimin Huang. The wall street neophyte: A zero-
[63] Tianhao Shen, Sun Li, Quan Tu, and Deyi Xiong. shotanalysisofchatgptovermultimodalstockmove-
Roleeval: A bilingual role evaluation benchmark for mentpredictionchallenges,2023.
largelanguagemodels,2024.
[77] Ameet Deshpande, Vishvak Murahari, Tanmay Ra-
[64] Quan Tu, Shilong Fan, Zihang Tian, and Rui Yan. jpurohit, Ashwin Kalyan, and Karthik Narasimhan.
Charactereval: A chinese benchmark for role-playing Toxicity in chatgpt: Analyzing persona-assigned lan-
conversationalagentevaluation,2024. guagemodels,2023.
[65] Xiaoyan Yu, Tongxu Luo, Yifan Wei, Fangyu Lei, [78] XiaoyangSong,AkshatGupta,KiyanMohebbizadeh,
YimingHuang,HaoPeng,andLiehuangZhu. Neeko: Shujie Hu, and Anant Singh. Have large language
Leveraging dynamic lora for efficient multi-character models developed a personality?: Applicability of
role-playingagent,2024. self-assessmenttestsinmeasuringpersonalityinllms,
[66] RuiXu,XintaoWang,JiangjieChen,SiyuYuan,Xin- 2023.
feng Yuan, Jiaqing Liang, Zulong Chen, Xiaoqing [79] MyraCheng,EsinDurmus,andDanJurafsky. Marked
Dong, and Yanghua Xiao. Character is destiny: Can personas: Usingnaturallanguagepromptstomeasure
large language models simulate persona-driven deci- stereotypesinlanguagemodels,2023.
sionsinrole-playing?,2024.
[80] Lei Wang, Jingsen Zhang, Hao Yang, Zhiyuan Chen,
[67] Xinfeng Yuan, Siyu Yuan, Yuhan Cui, Tianhe Lin, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Rui-
Xintao Wang, Rui Xu, Jiangjie Chen, and Deqing hua Song, Wayne Xin Zhao, Jun Xu, Zhicheng Dou,

Jun Wang, and Ji-Rong Wen. User behavior simula- warming? an empirical assessment of algorithmic fi-
tionwithlargelanguagemodelbasedagents,2024. delityandbias.PLOSClimate,3(8):e0000429,August
2024.
[81] GregSerapio-Garc´ıa,MustafaSafdari,Cle´mentCrepy,
LuningSun, StephenFitz, PeterRomero, MarwaAb- [94] ChengLi,MengzhouChen,JindongWang,Sunayana
dulhai, Aleksandra Faust, and Maja Mataric´. Person- Sitaram,andXingXie. Culturellm: Incorporatingcul-
alitytraitsinlargelanguagemodels,2023. turaldifferencesintolargelanguagemodels,2024.
[82] Jen tse Huang, Man Ho Lam, Eric John Li, Shujie [95] Yixuan Weng, Shizhu He, Kang Liu, Shengping Liu,
Ren, Wenxuan Wang, Wenxiang Jiao, Zhaopeng Tu, andJunZhao. Controllm: Craftingdiversepersonali-
andMichaelR.Lyu.Emotionallynumborempathetic? tiesforlanguagemodels,2024.
evaluatinghowllmsfeelusingemotionbench,2024. [96] Seungjong Sun, Eungu Lee, Dongyan Nan, Xiangy-
[83] QuanTu,ChuanqiChen,JinpengLi,YanranLi,Shuo ing Zhao, Wonbyung Lee, Bernard J. Jansen, and
Jang Hyun Kim. Random silicon sampling: Simulat-
Shang,DongyanZhao,RanWang,andRuiYan.Char-
ing human sub-population opinion using a large lan-
acterchat:Learningtowardsconversationalaiwithper-
guagemodelbasedongroup-leveldemographicinfor-
sonalizedsocialsupport,2023.
mation,2024.
[84] Mahyar Abbasian, Iman Azimi, Amir M. Rahmani,
[97] James Bisbee, Joshua D. Clinton, Cassy Dorff, Bren-
andRameshJain.Conversationalhealthagents:Aper-
ton Kenkel, and Jennifer M. Larson. Synthetic re-
sonalizedllm-poweredagentframework,2024.
placementsforhumansurveydata? theperilsoflarge
[85] Jiangjie Chen, Siyu Yuan, Rong Ye, Bod- language models. Political Analysis, 32(4):401–416,
hisattwa Prasad Majumder, and Kyle Richardson. 2024.
Put your money where your mouth is: Evaluating
[98] Tao Ge, Xin Chan, Xiaoyang Wang, Dian Yu, Haitao
strategic planning and execution of llm agents in an
Mi,andDongYu. Scalingsyntheticdatacreationwith
auctionarena,2024.
1,000,000,000personas,2024.
[86] NianLi,ChenGao,MingyuLi,YongLi,andQingmin
[99] Yao Qu and Jue Wang. Performance and biases of
Liao. Econagent: Large language model-empowered
large language models in public opinion simulation.
agentsforsimulatingmacroeconomicactivities,2024.
AcademyofManagementProceedings,2024.
[87] Ryan Shea and Zhou Yu. Building persona consis- [100] HuachuanQiuandZhenzhongLan.Interactiveagents:
tent dialogue agents with offline reinforcement learn- Simulating counselor-client psychological counseling
ing,2023. viarole-playingllm-to-llminteractions,2024.
[88] KushalChawla,IanWu,YuRong,GaleM.Lucas,and [101] Zhilin Wang, Yu Ying Chiu, and Yu Cheung Chiu.
Jonathan Gratch. Be selfish, but wisely: Investigat- Humanoidagents:Platformforsimulatinghuman-like
ing the impact of agent personality in mixed-motive generativeagents,2023.
human-agentinteractions,2023.
[102] Yoonna Jang, Jungwoo Lim, Yuna Hur, Dongsuk Oh,
[89] Yoon-Kyung Lee, Sowon Hahn, Seo-Yeon Bae, Inju Suhyune Son, Yeonsoo Lee, Donghoon Shin, Seun-
Lee, and Minjung Shin. Enhancing empathic reason- gryongKim, andHeuiseokLim. Callforcustomized
ingoflargelanguagemodelsbasedonpsychotherapy conversation:Customizedconversationgroundingper-
modelsforai-assistedsocialsupport. KoreanJournal sonaandknowledge,2022.
ofCognitiveScience,35(1):23–48,032024.
[103] Juntao Li, Chang Liu, Chongyang Tao, Zhangming
[90] ShashankGupta,VaishnaviShrivastava,AmeetDesh- Chan, Dongyan Zhao, Min Zhang, and Rui Yan. Di-
pande, Ashwin Kalyan, Peter Clark, Ashish Sabhar- alogue history matters! personalized response selec-
wal, and Tushar Khot. Bias runs deep: Implicit rea- tioninmulti-turnretrieval-basedchatbots,2021.
soningbiasesinpersona-assignedllms,2024. [104] Pegah Jandaghi, XiangHai Sheng, Xinyi Bai, Jay Pu-
[91] Junyi Li, Ninareh Mehrabi, Charith Peris, Palash jara, and Hakim Sidahmed. Faithful persona-based
Goyal, Kai-Wei Chang, Aram Galstyan, Richard conversational dataset generation with large language
Zemel, and Rahul Gupta. On the steerability of large models,2023.
languagemodelstowarddata-drivenpersonas,2024. [105] Weiqi Wu, Hongqiu Wu, Lai Jiang, Xingyuan Liu,
[92] Chengxing Xie, Canyu Chen, Feiran Jia, Ziyu Ye, JialeHong,HaiZhao,andMinZhang. Fromrole-play
Kai Shu, Adel Bibi, Ziniu Hu, Philip Torr, Bernard todrama-interaction: Anllmsolution,2024.
Ghanem, and Guohao Li. Can large language model [106] Jiannan Xiang, Tianhua Tao, Yi Gu, Tianmin Shu,
agentssimulatehumantrustbehaviors?,2024. ZiruiWang, ZichaoYang, andZhitingHu. Language
modelsmeetworldmodels:Embodiedexperiencesen-
[93] Sanguk Lee, Tai-Quan Peng, Matthew H. Goldberg,
hancelanguagemodels,2023.
Seth A. Rosenthal, John E. Kotcher, Edward W.
Maibach, and Anthony Leiserowitz. Can large lan- [107] Jiangyong Huang, Silong Yong, Xiaojian Ma,
guage models estimate public opinion about global Xiongkun Linghu, Puhao Li, Yan Wang, Qing Li,

Song-ChunZhu,BaoxiongJia,andSiyuanHuang. An [121] Kranti Chalamalasetti, Jana Go¨tze, Sherzod Haki-
embodiedgeneralistagentin3dworld,2024. mov, Brielen Madureira, Philipp Sadler, and David
Schlangen. Clembench: Using game play to evalu-
[108] Jiaju Lin, Haoran Zhao, Aochi Zhang, Yiting Wu,
atechat-optimizedlanguagemodelsasconversational
HuqiuyuePing,andQinChen. Agentsims: Anopen-
agents,2023.
source sandbox for large language model evaluation,
2023. [122] Haoqi Yuan, Chi Zhang, Hongcheng Wang, Feiyang
Xie, PenglinCai, HaoDong, andZongqingLu. Skill
[109] Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
reinforcement learning and planning for open-world
dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and An-
long-horizontasks,2023.
imaAnandkumar. Voyager: Anopen-endedembodied
agentwithlargelanguagemodels,2023. [123] Libo Sun, Siyuan Wang, Xuanjing Huang, and
Zhongyu Wei. Identity-driven hierarchical role-
[110] Xintao Wang, Jiangjie Chen, Nianqi Li, Lida Chen,
playing agents. arXiv preprint arXiv:2407.19412,
Xinfeng Yuan, Wei Shi, Xuyang Ge, Rui Xu, and
2024.
YanghuaXiao. Surveyagent: Aconversationalsystem
forpersonalizedandefficientresearchsurvey,2024. [124] Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda
Askell, Anna Chen, Nova DasSarma, Dawn Drain,
[111] Hongzhan Chen, Hehong Chen, Ming Yan, Wenshen
Stanislav Fort, Deep Ganguli, Tom Henighan,
Xu, Xing Gao, Weizhou Shen, Xiaojun Quan, Chen-
Nicholas Joseph, Saurav Kadavath, Jackson Kernion,
liangLi,JiZhang,FeiHuang,andJingrenZhou. So-
Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac
cialbench: Socialityevaluationofrole-playingconver-
Hatfield-Dodds, Danny Hernandez, Tristan Hume,
sationalagents,2024.
Scott Johnston, Shauna Kravec, Liane Lovitt, Neel
[112] Zhipeng Chen, Kun Zhou, Beichen Zhang, Zheng Nanda,CatherineOlsson,DarioAmodei,TomBrown,
Gong, Wayne Xin Zhao, and Ji-Rong Wen. Chatcot: JackClark,SamMcCandlish,ChrisOlah,BenMann,
Tool-augmented chain-of-thought reasoning on chat- andJaredKaplan. Trainingahelpfulandharmlessas-
basedlargelanguagemodels,2023. sistantwithreinforcementlearningfromhumanfeed-
[113] AlirezaSalemi,ShesheraMysore,MichaelBendersky, back,2022.
and Hamed Zamani. Lamp: When large language [125] Joel Jang, Seungone Kim, Bill Yuchen Lin, Yizhong
modelsmeetpersonalization,2024. Wang, JackHessel, LukeZettlemoyer, HannanehHa-
jishirzi,YejinChoi,andPrithvirajAmmanabrolu. Per-
[114] Ceyao Zhang, Kaijie Yang, Siyi Hu, Zihao Wang,
sonalized soups: Personalized large language model
Guanghe Li, Yihang Sun, Cheng Zhang, Zhaowei
alignmentviapost-hocparametermerging,2023.
Zhang, Anji Liu, Song-Chun Zhu, Xiaojun Chang,
Junge Zhang, Feng Yin, Yitao Liang, and Yaodong [126] XingxuanLi,YutongLi,LinQiu,ShafiqJoty,andLi-
Yang.Proagent:Buildingproactivecooperativeagents dong Bing. Evaluating psychological safety of large
withlargelanguagemodels,2024. languagemodels,2024.
[115] LeiWang,WanyuXu,YihuaiLan,ZhiqiangHu,Yun- [127] SangukLee,Kai-QiYang,Tai-QuanPeng,RuthHeo,
shi Lan, Roy Ka-Wei Lee, and Ee-Peng Lim. Plan- and Hui Liu. Exploring social desirability response
and-solve prompting: Improving zero-shot chain-of- bias in large language models: Evidence from gpt-4
thought reasoning by large language models. arXiv simulations,2024.
preprintarXiv:2305.04091,2023. [128] Won Ik Cho, Yoon Kyung Lee, Seoyeon Bae, Jihwan
[116] Zhenyu Wu, Ziwei Wang, Xiuwei Xu, Jiwen Lu, Kim, Sangah Park, Moosung Kim, Sowon Hahn, and
and Haibin Yan. Embodied task planning with large Nam Soo Kim. When crowd meets persona: Creat-
language models. arXiv preprint arXiv:2307.01848, ing a large-scale open-domain persona dialogue cor-
2023. pus,2023.
[117] Chan Hee Song, Jiaman Wu, Clayton Washington, [129] Xinyi Mou, Zejun Li, Hanjia Lyu, Jiebo Luo, and
Brian M. Sadler, Wei-Lun Chao, and Yu Su. Llm- Zhongyu Wei. Unifying local and global knowledge:
planner: Few-shot grounded planning for embodied Empowering large language models as political ex-
agentswithlargelanguagemodels,2023. perts with knowledge graphs. In Proceedings of the
ACM on Web Conference 2024, pages 2603–2614,
[118] Itsugun Cho, Dongyang Wang, Ryota Takahashi, and
2024.
HiroakiSaito. Apersonalizeddialoguegeneratorwith
implicituserpersonadetection,2022. [130] Yuanchun Li, Hao Wen, Weijun Wang, Xiangyu Li,
Yizhen Yuan, Guohong Liu, Jiacheng Liu, Wenxing
[119] Jonathan Light, Min Cai, Sheng Shen, and Ziniu Hu.
Xu,XiangWang,YiSun,RuiKong,YileWang,Han-
Avalonbench: Evaluating llms playing the game of
feiGeng,JianLuan,XuefengJin,ZilongYe,Guanjing
avalon,2023.
Xiong,FanZhang,XiangLi,MengweiXu,ZhijunLi,
[120] KeyuPanandYawenZeng. Dollmspossessaperson- Peng Li, Yang Liu, Ya-Qin Zhang, and Yunxin Liu.
ality? makingthembtitestanamazingevaluationfor Personalllmagents: Insightsandsurveyabouttheca-
largelanguagemodels,2023. pability,efficiencyandsecurity,2024.

[131] Jinheon Baek, Nirupama Chandrasekaran, Silviu [143] Yao Fu, Hao Peng, Tushar Khot, and Mirella Lap-
Cucerzan, Allen herring, and Sujay Kumar Jauhar. ata. Improvinglanguagemodelnegotiationwithself-
Knowledge-augmentedlargelanguagemodelsforper- play and in-context learning from ai feedback. arXiv
sonalizedcontextualquerysuggestion,2024. preprintarXiv:2305.10142,2023.
[132] Hezekiah J. Branch, Jonathan Rodriguez Cefalu, [144] KaiXiong,XiaoDing,YixinCao,TingLiu,andBing
Jeremy McHugh, Leyla Hujer, Aditya Bahl, Daniel Qin. Examining inter-consistency of large language
delCastilloIglesias,RonHeichman,andRameshDar- modelscollaboration:Anin-depthanalysisviadebate.
wishi. Evaluatingthesusceptibilityofpre-trainedlan- arXivpreprintarXiv:2305.11595,2023.
guage models via handcrafted adversarial examples,
[145] Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang,
2022.
YanWang,RuiWang,YujiuYang,ZhaopengTu,and
[133] Jaewoo Ahn, Yeda Song, Sangdoo Yun, and Gun- ShumingShi. Encouragingdivergentthinkinginlarge
hee Kim. MPCHAT: Towards multimodal persona- language models through multi-agent debate. arXiv
groundedconversation.InAnnaRogers,JordanBoyd- preprintarXiv:2305.19118,2023.
Graber, and Naoaki Okazaki, editors, Proceedings of
[146] ChiMingChan,WenhaoChen,YiSu,etal. Chateval:
the 61st Annual Meeting of the Association for Com-
Towards better llm-based evaluators through multi-
putationalLinguistics(Volume1:LongPapers),pages
agentdebate. arXivpreprintarXiv:2308.07201,2023.
3354–3377, Toronto, Canada, July 2023. Association
forComputationalLinguistics. [147] Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu,
ShaokunZhang,ErkangZhu,BeibinLi,LiJiang,Xi-
[134] Jiwei Li, Michel Galley, Chris Brockett, Georgios P.
aoyun Zhang, and Chi Wang. Autogen: Enabling
Spithourakis, Jianfeng Gao, and Bill Dolan. A
next-genllmapplicationsviamulti-agentconversation
persona-basedneuralconversationmodel,2016.
framework. arXivpreprintarXiv:2308.08155,2023.
[135] Zejun Wang, Jia Li, Ge Li, and Zhi Jin. Chatcoder:
[148] Tian Xia, Zhiwei He, Tong Ren, Yibo Miao, Zhu-
Chat-based refine requirement improves llms’ code
osheng Zhang, Yang Yang, and Rui Wang. Mea-
generation,2023.
suring bargaining abilities of llms: A benchmark
[136] NicholasFarnandRichardShin. Tooltalk: Evaluating and a buyer-enhancement method. arXiv preprint
tool-usageinaconversationalsetting,2023. arXiv:2402.15813,2024.
[137] Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xu- [149] JieMa,ZhitaoGao,QiChai,WangchunSun,Pinghui
anyu Lei, Hanyu Lai, Yu Gu, Hangliang Ding, Kai-
Wang,HongbinPei,JingTao,LingyunSong,JunLiu,
wenMen, KejuanYang, ShudanZhang, XiangDeng,
ChenZhang,etal. Debateongraph: aflexibleandre-
Aohan Zeng, Zhengxiao Du, Chenhui Zhang, Sheng
liablereasoningframeworkforlargelanguagemodels.
Shen,TianjunZhang,YuSu,HuanSun,MinlieHuang,
arXivpreprintarXiv:2409.03155,2024.
Yuxiao Dong, and Jie Tang. Agentbench: Evaluating
llmsasagents,2023. [150] Y.Xu,S.Wang,P.Li,etal. Exploringlargelanguage
modelsforcommunicationgames:Anempiricalstudy
[138] Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong
onwerewolf,2023.
Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe
Morency, Yonatan Bisk, Daniel Fried, Graham Neu- [151] Shenzhi Wang, Chang Liu, Zilong Zheng, Siyuan
big, et al. Sotopia: Interactive evaluation for so- Qi, Shuo Chen, Qisen Yang, Andrew Zhao, Chaofei
cial intelligence in language agents. arXiv preprint Wang, Shiji Song, and Gao Huang. Avalon’s game
arXiv:2310.11667,2023. of thoughts: Battle against deception through recur-
sivecontemplation. arXivpreprintarXiv:2310.01320,
[139] Mohammadmehdi Ataei, Hyunmin Cheong, Daniele
2023.
Grandi, Ye Wang, Nigel Morris, and Alexander
Tessier. Elicitron: An llm agent-based simulation [152] Jintian Zhang, Xin Xu, and Shumin Deng. Explor-
framework for design requirements elicitation. arXiv ingcollaborationmechanismsforllmagents: Asocial
preprintarXiv:2404.16045,2024. psychology view. arXiv preprint arXiv:2310.02124,
2023.
[140] DiyiYang,CalebZiems,WilliamHeld,OmarShaikh,
Michael S Bernstein, and John Mitchell. Social skill [153] Jonathan Light, Min Cai, Sheng Shen, and Ziniu Hu.
training with large language models. arXiv preprint Fromtexttotactic: Evaluatingllmsplayingthegame
arXiv:2404.04204,2024. ofavalon. arXivpreprintarXiv:2310.05036,2023.
[141] Zihan Yan, Yaohong Xiang, and Yun Huang. Social [154] YihuaiLan,ZhiqiangHu,LeiWang,YangWang,De-
lifesimulationfornon-cognitiveskillslearning. arXiv heng Ye, Peilin Zhao, Ee-Peng Lim, Hui Xiong, and
preprintarXiv:2405.00273,2024. Hao Wang. Llm-based agent society investigation:
Collaboration and confrontation in avalon gameplay.
[142] QiangZhang, JasonNaradowsky, andYusukeMiyao.
arXivpreprintarXiv:2310.14985,2023.
Self-emotion blended dialogue generation in social
simulation agents. arXiv preprint arXiv:2408.01633, [155] Zelai Xu, Chao Yu, Fei Fang, Yu Wang, and Yi Wu.
2024. Language agents with reinforcement learning for

strategic play in the werewolf game. arXiv preprint [169] ZhaolinGao,Kiante´Brantley,andThorstenJoachims.
arXiv:2310.18940,2023. Reviewer2: Optimizing review generation through
promptgeneration. arXivpreprintarXiv:2402.10886,
[156] DekunWu,HaochenShi,ZhiyuanSun,andBangLiu.
2024.
Decipheringdigitaldetectives: Understandingllmbe-
haviorsandcapabilitiesinmulti-agentmysterygames. [170] Mingyu Jin, Beichen Wang, Zhaoqian Xue, Suiyuan
arXivpreprintarXiv:2312.00746,2023. Zhu,WenyueHua,HuaTang,KaiMei,MengnanDu,
and Yongfeng Zhang. What if llms have different
[157] Zijing Shi, Meng Fang, Shunfeng Zheng, Shilong
world views: Simulating alien civilizations with llm-
Deng, Ling Chen, and Yali Du. Cooperation on the
basedagents. arXivpreprintarXiv:2402.13184,2024.
fly: Exploring language agents for ad hoc teamwork
intheavalongame. arXivpreprintarXiv:2312.17515, [171] Jinheon Baek, Sujay Kumar Jauhar, Silviu Cucerzan,
2023. andSungJuHwang.Researchagent:Iterativeresearch
idea generation over scientific literature with large
[158] S.Wu, L.Zhu, T.Yang, etal. Enhancereasoningfor
language models. arXiv preprint arXiv:2404.07738,
largelanguagemodelsinthegamewerewolf,2024.
2024.
[159] Silin Du and Xiaowei Zhang. Helmsman of the [172] Hanna Yukhymenko, Robin Staab, Mark Vero, and
masses? evaluate the opinion leadership of large lan- Martin Vechev. A synthetic dataset for personal at-
guage models in the werewolf game. arXiv preprint tribute inference. arXiv preprint arXiv:2406.07217,
arXiv:2404.01602,2024.
2024.
[160] Qinglin Zhu, Runcong Zhao, Jinhua Du, Lin Gui, [173] ZhifeiXie,DanielTang,DingweiTan,JacquesKlein,
and Yulan He. Player*: Enhancing llm-based multi- Tegawend F Bissyand, and Saad Ezzini. Dream-
agent communication and interaction in murder mys- factory: Pioneering multi-scene long video genera-
terygames. arXivpreprintarXiv:2404.17662,2024. tion with a multi-agent framework. arXiv preprint
[161] Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, arXiv:2408.11788,2024.
Weijie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei [174] Jun-Peng Zhu, Peng Cai, Kai Xu, Li Li, Yishen Sun,
Lu, Xiaogang Wang, et al. Ghost in the minecraft: ShuaiZhou,HaihuangSu,LiuTang,andQiLiu. Au-
Generallycapableagentsforopen-worldenvironments totqa: Towards autonomous tabular question answer-
vialargelanguagemodelswithtext-basedknowledge ingthroughmulti-agentlargelanguagemodels. Proc.
andmemory. arXivpreprintarXiv:2305.17144,2023. VLDBEndow.,17(12):3920–3933,November2024.
[162] Karthik Sreedhar and Lydia Chilton. Simulating hu- [175] Varun Nair, Elliot Schumacher, Geoffrey Tso, and
man strategic behavior: Comparing single and multi- Anitha Kannan. Dera: enhancing large language
agentllms. arXivpreprintarXiv:2402.08189,2024. model completions with dialog-enabled resolving
agents. arXivpreprintarXiv:2303.17071,2023.
[163] YizhouChi,LingjunMao,andZinengTang.Amonga-
gents:Evaluatinglargelanguagemodelsintheinterac- [176] Yihong Dong, Xue Jiang, Zhi Jin, and Ge Li. Self-
tivetext-basedsocialdeductiongame. arXivpreprint collaboration code generation via chatgpt. arXiv
arXiv:2407.16521,2024. preprintarXiv:2304.07590,2023.
[164] Jiaqi Chen, Yuxian Jiang, Jiachen Lu, and Li Zhang. [177] Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen,
S-agents: self-organizing agents in open-ended envi- Yufan Dang, Jiahao Li, Cheng Yang, Weize Chen,
ronment. arXivpreprintarXiv:2402.04578,2024. Yusheng Su, Xin Cong, et al. Chatdev: Communica-
tive agents for software development. In Proceed-
[165] Md Mahadi Hassan, Alex Knipper, and Shubhra
ingsofthe62ndAnnualMeetingoftheAssociationfor
KantiKarmakerSantu. Chatgptasyourpersonaldata
Computational Linguistics (Volume 1: Long Papers),
scientist. arXivpreprintarXiv:2305.13657,2023.
pages15174–15186,2024.
[166] Cheng-KuangWu,Wei-LinChen,andHsin-HsiChen. [178] Chen Qian, Yufan Dang, Jiahao Li, Wei Liu, Weize
Largelanguagemodelsperformdiagnosticreasoning. Chen, Cheng Yang, Zhiyuan Liu, and Maosong
arXivpreprintarXiv:2307.08922,2023. Sun. Experiential co-learning of software-developing
[167] Zhiling Zheng, Oufan Zhang, Ha L Nguyen, Nakul agents. arXivpreprintarXiv:2312.17025,2023.
Rampal,AliHAlawadhi,ZichaoRong,TeresaHead- [179] Yuntong Zhang, Haifeng Ruan, Zhiyu Fan, and Ab-
Gordon, Christian Borgs, Jennifer T Chayes, and hikRoychoudhury. Autocoderover: Autonomouspro-
Omar M Yaghi. Chatgpt research group for optimiz- gram improvement. In Proceedings of the 33rd ACM
ing the crystallinity of mofs and cofs. ACS Central SIGSOFT International Symposium on Software Test-
Science,9(11):2161–2170,2023. ingandAnalysis,pages1592–1604,2024.
[168] Xiangru Tang, Anni Zou, Zhuosheng Zhang, Yilun [180] Chen Qian, Jiahao Li, Yufan Dang, Wei Liu, YiFei
Zhao, XingyaoZhang, ArmanCohan, andMarkGer- Wang, Zihao Xie, Weize Chen, Cheng Yang, Yingli
stein. Medagents: Largelanguagemodelsascollabo- Zhang,ZhiyuanLiu,etal. Iterativeexperiencerefine-
ratorsforzero-shotmedicalreasoning. arXivpreprint ment of software-developing agents. arXiv preprint
arXiv:2311.10537,2023. arXiv:2405.04219,2024.

[181] Sil Hamilton. Blind judgement: Agent-based [193] W. Chen, Y. Su, J. Zuo, et al. Agentverse: Facilitat-
supreme court modelling with gpt. arXiv preprint ing multi-agent collaboration and exploring emergent
arXiv:2301.05327,2023. behaviors,2023.
[182] Yang Li, Yangyang Yu, Haohang Li, Zhi Chen, and [194] Yongchao Chen, Jacob Arkin, Yang Zhang, Nicholas
KhaldounKhashanah.Tradinggpt:Multi-agentsystem Roy,andChuchuFan. Scalablemulti-robotcollabora-
with layered memory and distinct characters for en- tionwithlargelanguagemodels:Centralizedordecen-
hanced financial trading performance. arXiv preprint tralizedsystems? In2024IEEEInternationalConfer-
arXiv:2309.03736,2023. enceonRoboticsandAutomation(ICRA),pages4311–
4317.IEEE,2024.
[183] Martin Weiss, Nasim Rahaman, Manuel Wuthrich,
YoshuaBengio,LiErranLi,BernhardSch”¨olkopf,and [195] Guangyao Chen, Siwei Dong, Yu Shu, Ge Zhang,
Christopher Pal. Rethinking the buyer’s inspection Jaward Sesay, B”¨orje F Karlsson, Jie Fu, and Yemin
paradoxininformationmarketswithlanguageagents. Shi. Autoagents: A framework for automatic agent
OpenReview,2024. generation. arXivpreprintarXiv:2309.17288,2023.
[184] MurongYue,WijdaneMifdal,YixuanZhang,Jennifer [196] TianbaoXie,FanZhou,ZhoujunCheng,PengShi,Lu-
Suh,andZiyuYao. Mathvc: Anllm-simulatedmulti- oxuanWeng,YitaoLiu,TohJingHua,JunningZhao,
charactervirtualclassroomformathematicseducation. Qian Liu, Che Liu, et al. Openagents: An open plat-
arXivpreprintarXiv:2404.06711,2024. form for language agents in the wild. arXiv preprint
arXiv:2310.10634,2023.
[185] Zachary R Baker and Zarif L Azher. Simulating the
us senate: An llm-driven agent approach to modeling [197] Weihao Tan, Wentao Zhang, Shanqi Liu, Longtao
legislativebehaviorandbipartisanship. arXivpreprint Zheng, Xinrun Wang, and Bo An. True knowledge
arXiv:2406.18702,2024. comesfrompractice:Aligningllmswithembodieden-
vironmentsviareinforcementlearning. arXivpreprint
[186] Jingyun Sun, Chengxiao Dai, Zhongze Luo, Yangbo
arXiv:2401.14151,2024.
Chang,andYangLi. Lawluo: Achineselawfirmco-
run by llm agents. arXiv preprint arXiv:2407.16252, [198] Yang Zhang, Shixin Yang, Chenjia Bai, Fei Wu, Xiu
2024. Li, Xuelong Li, and Zhen Wang. Towards efficient
llmgroundingforembodiedmulti-agentcollaboration.
[187] JifanYu,ZheyuanZhang,DanielZhang-li,Shangqing
arXivpreprintarXiv:2405.14314,2024.
Tu,ZhanxinHao,RuiMiaoLi,HaoxuanLi,Yuanchun
Wang,HanmingLi,LinluGong,etal. Frommoocto [199] J.Lin,H.Zhao,A.Zhang,etal. Agentsims: Anopen-
maic: Reshapingonlineteachingandlearningthrough source sandbox for large language model evaluation,
llm-driven agents. arXiv preprint arXiv:2409.03512, 2023.
2024. [200] Yuan Li, Yixuan Zhang, and Lichao Sun. Metaa-
[188] Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii gents: Simulatinginteractionsofhumanbehaviorsfor
Khizbullin, and Bernard Ghanem. Camel: Commu- llm-basedtask-orientedcoordinationviacollaborative
nicative agents for”” mind”” exploration of large lan- generative agents. arXiv preprint arXiv:2310.06500,
guagemodelsociety. AdvancesinNeuralInformation 2023.
ProcessingSystems,36:51991–52008,2023. [201] Jingcong Liang, Rong Ye, Meng Han, Ruofei Lai,
[189] Bill Yuchen Lin, Yicheng Fu, Karina Yang, Faeze XinyuZhang,XuanjingHuang,andZhongyuWei.De-
Brahman, Shiyu Huang, Chandra Bhagavatula, batrix: Multi-dimensinal debate judge with iterative
Prithviraj Ammanabrolu, Yejin Choi, and Xiang Ren. chronological analysis based on llm. arXiv preprint
Swiftsage: A generative agent with fast and slow
arXiv:2403.08010,2024.
thinking for complex interactive tasks. Advances in [202] WeiLiu,ChenxiWang,YifeiWang,ZihaoXie,Rennai
NeuralInformationProcessingSystems,36,2024. Qiu, Yufan Dang, Zhuoyun Du, Weize Chen, Cheng
[190] YasharTalebiradandAmirhosseinNadiri.Multi-agent Yang, and Chen Qian. Autonomous agents for col-
laborative task under information asymmetry. arXiv
collaboration: Harnessingthepowerofintelligentllm
agents. arXivpreprintarXiv:2306.03314,2023.
preprintarXiv:2406.14928,2024.
[191] Hongxin Zhang, Weihua Du, Jiaming Shan, Qinhong [203] Weize Chen, Jiarui Yuan, Chen Qian, Cheng Yang,
ZhiyuanLiu,andMaosongSun. Optima: Optimizing
Zhou, Yilun Du, Joshua B Tenenbaum, Tianmin Shu,
effectivenessandefficiencyforllm-basedmulti-agent
and Chuang Gan. Building cooperative embodied
system. arXivpreprintarXiv:2410.08115,2024.
agents modularly with large language models. arXiv
preprintarXiv:2307.02485,2023. [204] Chenxu Wang, Bin Dai, Huaping Liu, and Baoyuan
[192] Zhao Mandi, Shreeya Jain, and Shuran Song. Roco: Wang. Towards objectively benchmarking social in-
telligence for language agents at action level. arXiv
Dialectic multi-robot collaboration with large lan-
preprintarXiv:2404.05337,2024.
guagemodels.In2024IEEEInternationalConference
on Robotics and Automation (ICRA), pages 286–299. [205] Xinyi Mou, Jingcong Liang, Jiayu Lin, Xinnong
IEEE,2024. Zhang, Xiawei Liu, Shiyue Yang, Rong Ye, Lei

Chen, Haoyu Kuang, Xuanjing Huang, et al. [217] MikhailMozikov,NikitaSeverin,ValeriaBodishtianu,
Agentsense: Benchmarkingsocialintelligenceoflan- Maria Glushanina, Mikhail Baklashkin, Andrey V
guage agents through interactive scenarios. arXiv Savchenko,andIlyaMakarov. Thegood,thebad,and
preprintarXiv:2410.19346,2024. the hulk-like gpt: Analyzing emotional decisions of
large language models in cooperation and bargaining
[206] Ruiyi Wang, Haofei Yu, Wenxin Zhang, Zhengyang
games. arXivpreprintarXiv:2406.03299,2024.
Qi, Maarten Sap, Graham Neubig, Yonatan Bisk,
and Hao Zhu. Sotopia-pi: Interactive learning of [218] Zengqing Wu, Run Peng, Shuyuan Zheng, Qianying
socially intelligent language agents. arXiv preprint Liu, Xu Han, Brian Kwon, Makoto Onizuka, Shaojie
arXiv:2403.08715,2024. Tang, and Chuan Xiao. Shall we team up: Explor-
ingspontaneouscooperationofcompetingllmagents.
[207] XuhuiZhou,ZheSu,TiwalayoEisape,HyunwooKim,
InFindingsoftheAssociationforComputationalLin-
andMaartenSap. Isthisthereallife? isthisjustfan-
guistics: EMNLP2024,pages5163–5186,2024.
tasy? the misleading success of simulating social in-
teractionswithllms.arXivpreprintarXiv:2403.05020, [219] Qinlin Zhao, Jindong Wang, Yixuan Zhang, Yiqiao
2024. Jin,KaijieZhu,HaoChen,andXingXie. Competeai:
Understandingthecompetitiondynamicsoflargelan-
[208] Ran Gong, Qiuyuan Huang, Xiaojian Ma, Hoi Vo,
guagemodel-basedagents. InForty-firstInternational
Zane Durante, Yusuke Noda, Zilong Zheng, Song-
ConferenceonMachineLearning,2024.
Chun Zhu, Demetri Terzopoulos, Li Fei-Fei, et al.
Mindagent: Emergent gaming interaction. arXiv [220] John J Horton. Large language models as simulated
preprintarXiv:2309.09971,2023. economicagents: Whatcanwelearnfromhomosili-
cus? Technical report, National Bureau of Economic
[209] Zhijie Bao, Qingyun Liu, Ying Guo, Zhengqiang Ye,
Research,2023.
Jun Shen, Shirong Xie, Jiajie Peng, Xuanjing Huang,
and Zhongyu Wei. Piors: Personalized intelligent [221] JiaruiJi,YangLi,HongtaoLiu,ZhichengDu,Zhewei
outpatient reception based on large language model Wei,QiQi,WeiranShen,andYankaiLin. Srap-agent:
with multi-agents medical scenario simulation. arXiv Simulating and optimizing scarce resource allocation
preprintarXiv:2411.13902,2024. policywithllm-basedagent. InFindingsoftheAsso-
ciationforComputationalLinguistics: EMNLP2024,
[210] Xiawei Liu, Shiyue Yang, Xinnong Zhang, Haoyu
pages267–293,2024.
Kuang, Libo Sun, Yihang Yang, Siming Chen, Xuan-
jing Huang, and Zhongyu Wei. Ai-press: A multi- [222] Navid Ghaffarzadegan, Aritra Majumdar, Ross
agent news generating and feedback simulation sys- Williams, and Niyousha Hosseinichimeh. Generative
tempoweredbylargelanguagemodels.arXivpreprint agent-based modeling: Unveiling social system
arXiv:2410.07561,2024. dynamics through coupling mechanistic models with
generative artificial intelligence. arXiv preprint
[211] Chengxing Xie, Canyu Chen, Feiran Jia, Ziyu Ye, arXiv:2309.11456,2023.
Kai Shu, Adel Bibi, Ziniu Hu, Philip Torr, Bernard
[223] I de Zarza`, J de Curto`, Gemma Roig, Pietro Man-
Ghanem, and Guohao Li. Can large language model
zoni, and Carlos T Calafate. Emergent cooperation
agentssimulatehumantrustbehaviors? arXivpreprint
andstrategyadaptationinmulti-agentsystems:Anex-
arXiv:2402.04559,2024.
tended coevolutionary theory with llms. Electronics,
[212] AgnieszkaMensfelt,KostasStathis,andVinceTrenc- 12(12):2722,2023.
senyi. Logic-enhanced language model agents
[224] R. Williams, N. Hosseinichimeh, A. Majumdar, et al.
for trustworthy social simulations. arXiv preprint
Epidemic modeling with generative agents. arXiv
arXiv:2408.16081,2024.
preprintarXiv:2307.04986,2023.
[213] ShangminGuo,HaoranBu,HaochuanWang,YiRen,
[225] Ayush Chopra, Shashank Kumar, Nurullah Giray-
DianboSui,YumingShang,andSitingLu.Economics
Kuru,RameshRaskar,andArnauQuera-Bofarull. On
arena for large language models. arXiv preprint
the limits of agency in agent-based models. arXiv
arXiv:2401.01735,2024.
preprintarXiv:2409.10568,2024.
[214] Nicolo´ Fontana, Francesco Pierri, and Luca Maria
[226] Sanguk Lee, Tai-Quan Peng, Matthew H Goldberg,
Aiello. Nicer than humans: How do large language
Seth A Rosenthal, John E Kotcher, Edward W
models behave in the prisoner’s dilemma? arXiv
Maibach, and Anthony Leiserowitz. Can large lan-
preprintarXiv:2406.13605,2024.
guage models capture public opinion about global
[215] X.Han,Z.Wu,andC.Xiao. ”guineapigtrials”utiliz- warming? an empirical assessment of algorithmic fi-
inggpt:Anovelsmartagent-basedmodelingapproach delity and bias. arXiv preprint arXiv:2311.00217,
forstudyingfirmcompetitionandcollusion,2023. 2023.
[216] Sean Noh and Ho-Chun Herbert Chang. Llms with [227] Xinnong Zhang, Jiayu Lin, Libo Sun, Weihong
personalities in multi-issue negotiation games. arXiv Qi, Yihang Yang, Yue Chen, Hanjia Lyu, Xinyi
preprintarXiv:2405.05248,2024. Mou, Siming Chen, Jiebo Luo, et al. Electionsim:

Massive population election simulation powered by [240] Yun-Shiuan Chuang, Zach Studdiford, Krirk Nirun-
large language model driven agents. arXiv preprint wiroj,AgamGoyal,VincentVFrigo,SijiaYang,Dha-
arXiv:2410.20746,2024. vanShah, JunjieHu, andTimothyTRogers. Beyond
[228] B.Xiao,Z.Yin,andZ.Shan.Simulatingpublicadmin- demographics:Aligningrole-playingllm-basedagents
usinghumanbeliefnetworks,2024.
istration crisis: A novel generative agent-based sim-
ulation system to lower technology barriers in social [241] ChaoLi,XingSu,HaoyingHan,CongXue,Chunmo
scienceresearch,2023. Zheng, and Chao Fan. Quantifying the impact of
largelanguagemodelsoncollectiveopiniondynamics.
[229] Joon Sung Park, Carolyn Q Zou, Aaron Shaw, Ben-
arXivpreprintarXiv:2308.03313,2023.
jaminMakoHill,CarrieCai,MeredithRingelMorris,
Robb Willer, Percy Liang, and Michael S Bernstein. [242] ShuoTang,XianghePang,ZexiLiu,BohanTang,Rui
Generative agent simulations of 1,000 people. arXiv Ye,XiaowenDong,YanfengWang,andSihengChen.
preprintarXiv:2411.10109,2024. Synthesizingpost-trainingdataforllmsthroughmulti-
agent simulation. arXiv preprint arXiv:2410.14251,
[230] GatiVAher,RosaIArriaga,andAdamTaumanKalai.
2024.
Usinglargelanguagemodelstosimulatemultiplehu-
mansandreplicatehumansubjectstudies. InInterna- [243] Jinyu Cai, Jialong Li, Mingyue Zhang, Munan
tional Conference on Machine Learning, pages 337– Li, Chen-Shu Wang, and Kenji Tei. Language
371.PMLR,2023. evolution for evading social media regulation via
llm-based multi-agent simulation. arXiv preprint
[231] Zhao Kaiya, Michelangelo Naim, Jovana
arXiv:2405.02858,2024.
Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo,
Guangyu Robert Yang, and Andrew Ahn. Lyfe [244] Yuhan Liu, Zirui Song, Xiaoqing Zhang, Xiuying
agents:Generativeagentsforlow-costreal-timesocial Chen,andRuiYan.Fromatinysliptoagiantleap:An
interactions. arXivpreprintarXiv:2310.02172,2023. llm-based simulation for fake news evolution. arXiv
preprintarXiv:2410.19064,2024.
[232] S. Ren, Z. Cui, R. Song, et al. Emergence of social
[245] Chenxi Wang, Zongfang Liu, Dequan Yang, and Xi-
norms in large language model-based agent societies,
uyingChen. Decodingechochambers: Llm-powered
2024.
simulations revealing polarization in social networks.
[233] Jeongeon Park, Bryan Min, Xiaojuan Ma, and Juho
arXivpreprintarXiv:2409.19338,2024.
Kim. Choicemates: Supporting unfamiliar online
[246] Maximilian Puelma Touzel, Sneheel Sarangi, Austin
decision-making with multi-agent conversational in-
Welch, Gayatri Krishnakumar, Dan Zhao, Zachary
teractions. arXivpreprintarXiv:2310.01331,2023.
Yang, Hao Yu, Ethan Kosak-Hine, Tom Gibbs, An-
[234] Daniel Jarrett, Miruna Pislar, Michiel A Bakker,
dreea Musulan, et al. A simulation system towards
MichaelHenryTessler,RaphaelKoster,JanBalaguer, solving societal-scale manipulation. arXiv preprint
Romuald Elie, Christopher Summerfield, and Andrea arXiv:2410.13915,2024.
Tacchetti. Language agents as digital representatives
[247] J. S. Park, L. Popowski, C. Cai, et al. Social simu-
incollectivedecision-making. InNeurIPS2023Foun-
lacra: Creating populated prototypes for social com-
dationModelsforDecisionMakingWorkshop,2023.
puting systems. In Proceedings of the 35th Annual
[235] Yiqiao Jin, Qinlin Zhao, Yiyang Wang, Hao Chen, ACMSymposiumonUserInterfaceSoftwareandTech-
Kaijie Zhu, Yijia Xiao, and Jindong Wang. Agen- nology,pages1–18,2022.
treview: Exploring peer review dynamics with llm
[248] C.Gao,X.Lan,Z.Lu,etal. S3: Social-networksim-
agents. arXivpreprintarXiv:2406.12708,2024.
ulationsystemwithlargelanguagemodel-empowered
[236] YangbinYu,QinZhang,JunyouLi,QiangFu,andDe- agents,2023.
hengYe. Affordablegenerativeagents. arXivpreprint
[249] Petter To¨rnberg, Diliara Valeeva, Justus Uitermark,
arXiv:2402.02053,2024.
and Christopher Bail. Simulating social media us-
[237] XianhaoYu,JiaqiFu,RenjiaDeng,andWenjuanHan. inglargelanguagemodelstoevaluatealternativenews
Mineland: Simulating large-scale multi-agent inter- feed algorithms. arXiv preprint arXiv:2310.05984,
actions with limited multimodal senses and physical 2023.
needs. arXivpreprintarXiv:2403.19267,2024.
[250] Giulio Rossetti, Massimo Stella, Re´my Cazabet,
[238] Chen Zhu, Yihang Cheng, Jingshuai Zhang, Yusheng KatherineAbramski,EricaCau,SalvatoreCitraro,An-
Qiu, Sitao Xia, and Hengshu Zhu. Generative or- drea Failla, Riccardo Improta, Virginia Morini, and
ganizationalbehaviorsimulationusinglargelanguage ValentinaPansanella. Ysocial: anllm-poweredsocial
modelbasedautonomousagents:Aholacracyperspec- mediadigitaltwin,2024.
tive. arXivpreprintarXiv:2408.11826,2024. [251] XiaoqingZhang, XiuyingChen, YuhanLiu, Jianzhou
[239] R.SuzukiandT.Arita. Anevolutionarymodelofper- Wang, Zhenxing Hu, and Rui Yan. A large-scale
sonality traits related to cooperative behavior using a time-aware agents simulation for influencer selec-
largelanguagemodel. ScientificReports,14(1):5989, tion in digital advertising campaigns. arXiv preprint
2024. arXiv:2411.01143,2024.

[252] Rui Xu, Dakuan Lu, Xiaoyu Tan, Xintao Wang, Siyu flexibleyetrobustmulti-agentplatform.arXivpreprint
Yuan,JiangjieChen,WeiChu,andXuYinghui. Min- arXiv:2402.14034,2024.
decho: Role-playing language agents for key opinion
[266] XuchenPan,DaweiGao,YuexiangXie,YushuoChen,
leaders,2024.
ZheweiWei,YaliangLi,BolinDing,Ji-RongWen,and
[253] Ruiyang Ren, Peng Qiu, Yingqi Qu, Jing Liu, Jingren Zhou. Very large-scale multi-agent simula-
WayneXinZhao,HuaWu,Ji-RongWen,andHaifeng tioninagentscope. arXivpreprintarXiv:2407.17789,
Wang. Bases: Large-scale web search user simula- 2024.
tion with large language model based agents. arXiv [267] YanchengWang,ZiyanJiang,ZhengChen,FanYang,
preprintarXiv:2402.17505,2024.
Yingxue Zhou, Eunah Cho, Xing Fan, Xiaojiang
[254] XuHuang,JianxunLian,YuxuanLei,JingYao,Defu Huang, Yanbin Lu, and Yingzhen Yang. Recmind:
Lian,andXingXie. Recommenderaiagent: Integrat- Large language model powered agent for recommen-
ing large language models for interactive recommen- dation. arXivpreprintarXiv:2308.14296,2023.
dations. arXivpreprintarXiv:2308.16505,2023. [268] Tian Liang, Zhiwei He, Jen-tes Huang, Wenx-
[255] Jizhi Zhang, Keqin Bao, Wenjie Wang, Yang Zhang, uan Wang, Wenxiang Jiao, Rui Wang, Yujiu Yang,
Wentao Shi, Wanhong Xu, Fuli Feng, and Tat-Seng Zhaopeng Tu, Shuming Shi, and Xing Wang. Lever-
Chua.Prospectpersonalizedrecommendationonlarge aging word guessing games to assess the intelli-
languagemodel-basedagentplatform. arXivpreprint gence of large language models. arXiv preprint
arXiv:2402.18240,2024. arXiv:2310.20499,2023.
[256] LeiWang,JingsenZhang,XuChen,YankaiLin,Rui- [269] Emily Dinan, Stephen Roller, Kurt Shuster, An-
huaSong,WayneXinZhao,andJi-RongWen. Reca- gela Fan, Michael Auli, and Jason Weston. Wiz-
gent: A novel simulation paradigm for recommender ardofwikipedia: Knowledge-poweredconversational
systems. arXivpreprintarXiv:2306.02552,2023. agents,2019.
[257] A. Zhang, Y. Chen, L. Sheng, et al. On generative [270] Saizheng Zhang, Emily Dinan, Jack Urbanek, Arthur
agentsinrecommendation,2024. Szlam,DouweKiela,andJasonWeston.Personalizing
dialogueagents: Ihaveadog, doyouhavepetstoo?,
[258] JunjieZhang,YupengHou,RuobingXie,WenqiSun,
2018.
Julian McAuley, Wayne Xin Zhao, Leyu Lin, and Ji-
Rong Wen. Agentcf: Collaborative learning with au- [271] Marilu` Miotto, Nicola Rossberg, and Bennett Klein-
tonomous language agents for recommender systems. berg. Whoisgpt-3? anexplorationofpersonality,val-
InProceedingsoftheACMonWebConference2024, uesanddemographics,2022.
pages3679–3689,2024. [272] S. Wang, C. Liu, Z. Zheng, et al. Avalon’s game of
[259] Flaminio Squazzoni, Wander Jager, and Bruce Ed- thoughts: Battle against deception through recursive
monds. Social simulation in the social sciences: A contemplation,2023.
brief overview. Social Science Computer Review, [273] H.Wang,J.Chen,W.Huang,etal. Grutopia: Dream
32(3):279–294,2014. generalrobotsinacityatscale,2024.
[260] Marcel Binz and Eric Schulz. Turning large lan- [274] J.Browning. Personhoodandai: Whylargelanguage
guage models into cognitive models. arXiv preprint modelsdon’tunderstandus. AI&Society,pages1–8,
arXiv:2306.03917,2023. 2023.
[261] Xinyi Li, Yu Xu, Yongfeng Zhang, and Edward C [275] A. Radford, J. W. Kim, C. Hallacy, et al. Learning
Malthouse. Largelanguagemodel-drivenmulti-agent transferable visual models from natural language su-
simulationfornewsdiffusionunderdifferentnetwork pervision. InProceedingsoftheInternationalConfer-
structures. arXivpreprintarXiv:2410.13909,2024. enceonMachineLearning,pages8748–8763.PMLR,
2021.
[262] Jacqueline Johnson Brownand Peter H Reingen. So-
cialtiesandword-of-mouthreferralbehavior. Journal [276] Haotian Liu, Chunyuan Li, Qingyang Wu, and
ofConsumerresearch,14(3):350–362,1987. Yong Jae Lee. Visual instruction tuning. Advances
inneuralinformationprocessingsystems,36,2024.
[263] GueorgiKossinetsandDuncanJWatts. Originsofho-
mophilyinanevolvingsocialnetwork.Americanjour-
nalofsociology,115(2):405–450,2009.
[264] BoxuanWang,HaonanDuan,YanhaoFeng,XuChen,
YongjieFu,ZhaobinMo,andXuanDi. Canllmsun-
derstand social norms in autonomous driving games?
arXivpreprintarXiv:2408.12680,2024.
[265] DaweiGao,ZitaoLi,XuchenPan,WeiruiKuang,Zhi-
jian Ma, Bingchen Qian, Fei Wei, Wenhao Zhang,
Yuexiang Xie, Daoyuan Chen, et al. Agentscope: A
