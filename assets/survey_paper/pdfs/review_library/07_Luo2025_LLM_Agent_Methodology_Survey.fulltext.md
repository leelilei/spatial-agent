Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/review_library/07_Luo2025_LLM_Agent_Methodology_Survey.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:31+00:00
- page_count: 26
- status: ok
- text_char_count: 164952

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Agent Methodology (page 2)
  - Agent Construction (page 3)
    - Profile Definition (page 3)
    - Memory Mechanism (page 4)
    - Planning Capability (page 4)
    - Action Execution (page 5)
  - Agent Collaboration (page 5)
    - Centralized Control (page 6)
    - Decentralized Collaboration (page 6)
    - Hybrid Architecture (page 6)
  - Agent Evolution (page 7)
    - Autonomous Optimization and Self-Learning (page 7)
    - Multi-Agent Co-Evolution (page 7)
    - Evolution via External Resources (page 8)
- Evaluation and Tools (page 8)
  - Evaluation Benchmarks and Datasets (page 8)
    - General Assessment Frameworks (page 8)
    - Domain-Specific Evaluation System (page 9)
    - Collaborative Evaluation of Complex Systems (page 9)
  - Tools (page 9)
    - Tools used by LLM agents (page 9)
    - Tools created by LLM agents (page 10)
    - Tools for deploying LLM agents (page 10)
- Real-World Issues (page 10)
  - Agent-centric Security (page 11)
    - Adversarial Attacks and Defense (page 11)
    - Jailbreaking Attacks and Defense (page 11)
    - Backdoor Attacks and Defense (page 11)
    - Model Collaboration Attacks and Defense (page 11)
  - Data-centric Security (page 12)
    - External Data Attack and Defense (page 12)
    - Interaction Attack and Defense (page 12)
  - Privacy (page 13)
    - LLM Memorization Vulnerabilities (page 13)
    - LM Intellectual Property Exploitation (page 14)
  - Social Impact and Ethical Concerns (page 14)
    - Benefits to Sociaty (page 14)
    - Ethical Concerns (page 14)
- Applications (page 15)
  - Scientific Discovery (page 15)
    - Agentic AI Across Scientific Disciplines (page 15)
    - Agentic AI in Chemistry, Materials Science and Astronomy (page 16)
    - Agentic AI in Biology (page 16)
    - Agentic AI in Scientific Dataset Construction (page 16)
    - Agentic AI in Medical (page 16)
  - Gaming (page 17)
  - Social Science (page 17)
  - Productivity Tools (page 18)
- Challenges and Future Trends (page 18)
  - Scalability and Coordination (page 18)
  - Memory Constraints and Long-Term Adaptation. (page 18)
  - Reliability and Scientific Rigor (page 18)
  - Multi-turn, Multi-agent Dynamic Evaluation (page 18)
  - Regulatory Measures for Safe Deployment (page 19)
  - Role-playing Scenarios (page 19)
- Conclusion (page 19)
- References (page 19)

Markdown Content:

1
Large Language Model Agent: A Survey on
Methodology, Applications and Challenges
Junyu Luo, Weizhi Zhang, Ye Yuan, Yusheng Zhao, Junwei Yang, Yiyang Gu, Bohan Wu, Binqi Chen,
Ziyue Qiao, Qingqing Long, Rongcheng Tu, Xiao Luo, Wei Ju, Zhiping Xiao, Yifan Wang, Meng Xiao,
Chenwu Liu, Jingyang Yuan, Shichang Zhang, Yiqiao Jin, Fan Zhang, Xian Wu, Hanqing Zhao,
Dacheng Tao, Fellow, IEEE, Philip S. Yu, Fellow, IEEE and Ming Zhang
Abstract—Theeraofintelligentagentsisuponus,drivenbyrevolutionaryadvancementsinlargelanguagemodels.LargeLanguage
Model(LLM)agents,withgoal-drivenbehaviorsanddynamicadaptationcapabilities,potentiallyrepresentacriticalpathwaytoward
artificialgeneralintelligence.ThissurveysystematicallydeconstructsLLMagentsystemsthroughamethodology-centeredtaxonomy,
linkingarchitecturalfoundations,collaborationmechanisms,andevolutionarypathways.Weunifyfragmentedresearchthreadsby
revealingfundamentalconnectionsbetweenagentdesignprinciplesandtheiremergentbehaviorsincomplexenvironments.Ourwork
providesaunifiedarchitecturalperspective,examininghowagentsareconstructed,howtheycollaborate,andhowtheyevolveovertime,
whilealsoaddressingevaluationmethodologies,toolapplications,practicalchallenges,anddiverseapplicationdomains.Bysurveying
thelatestdevelopmentsinthisrapidlyevolvingfield,weofferresearchersastructuredtaxonomyforunderstandingLLMagentsand
identifypromisingdirectionsforfutureresearch.Thecollectionisavailableathttps://github.com/luo-junyu/Awesome-Agent-Papers.
IndexTerms—Largelanguagemodel,LLMagent,AIagent,intelligentagent,multi-agentsystem,LLM,literaturesurvey
✦
1 INTRODUCTION once required human expertise, from in-depth research to
computeroperation,whileadaptingtospecificuserneeds.
Artificial Intelligence is entering a pivotal era with the Compared totraditionalagentsystems[2], LLM-based
emergenceofLLMagents—intelligententitiespowered agents have achieved generational across multiple dimen-
by large language models (LLMs) capable of perceiving sions, including knowledge sources [3], generalization ca-
environments, reasoning about goals, and executing ac- pabilities[4],andinteractionmodalities[5].Today’sagents
tions[1].UnliketraditionalAIsystemsthatmerelyrespond represent a qualitative leap driven by the convergence of
to user inputs, modern LLM agents actively engage with threekeydevelopments:❶unprecedentedreasoningcapabil-
their environments through continuous learning, reason- itiesofLLMs[6],❷advancementsintoolmanipulationand
ing, and adaptation. This shift represents a technological environmentalinteraction[7],and❸sophisticatedmemory
advancement and a fundamental reimagining of human- architecturesthatsupportlongitudinalexperienceaccumu-
machine relationships. Commercial LLM agent systems lation[8],[9].Thisconvergencehastransformedtheoretical
(e.g.,DeepResearch,DeepSearch,andManus)exemplifythis constructsintopracticalsystems,increasinglyblurringthe
paradigmshift—autonomouslyexecutingcomplextasksthat boundary between assistants and collaborators. This shift
fundamentallyarisesfromLLMs’roleasgeneral-purposetask
processors,unifyingperception,decision-making,andaction
• Junyu Luo, Ye Yuan, Yusheng Zhao, Junwei Yang, Yiyang Gu, Bohan
within semantic space through generative architectures,
Wu,BinqiChen,WeiJu,ChenwuLiu,JingyangYuan,andMingZhang
are with the School of Computer Science and PKU-Anker LLM Lab, therebyforminghuman-likecognitiveloops[10].
Peking University, Beijing, China. (e-mail: luojunyu@stu.pku.edu.cn, Ourstudypresentsanovelexaminationofagentsystems
mzhang cs@pku.edu.cn)
throughaunifiedtaxonomythatconnectsagentconstruction,
• WeizhiZhangandP.S.YuarewiththeDepartmentofComputerScience,
UniversityofIllinoisatChicago,Chicago,USA. collaborationmechanisms,andevolutionarypathways.We
• ZiyueQiaoiswiththeSchoolofComputingandInformationTechnology, offer a comprehensive perspective tracing on how agents
GreatBayUniversity,Guangdong,China. aredefined,howtheyfunctionindividuallyorcollectively,
• QingqingLongandMengXiaoarewiththeComputerNetworkInforma-
and how they evolve over time. Beyond clarifying the
tionCenter,ChineseAcademyofSciences,Beijing,China.
• Rongcheng Tu, Hanqing Zhao, and Dacheng Tao are with Nanyang current landscape, our work not only clarifies the current
TechnologicalUniversity,Singapore. landscapebutidentifiesemergingpatternsthatsignalfuture
• Xiao Luo is with the Department of Computer Science, University of
developments.Therapidadvancementofagenttechnologies
California,LosAngeles,USA.
• Zhiping Xiao is with Paul G. Allen School of Computer Science and necessitatestimelysurveystoprovideresearcherswithan
Engineering,UniversityofWashington,Seattle,USA. up-to-datetaxonomyforunderstandingthisdynamicfield.
• YifanWangiswiththeSchoolofInformationTechnology&Management, Figure 1 presents our organizational framework for
UniversityofInternationalBusinessandEconomics,Beijing,China.
understanding the LLM agent ecosystem. At its core, our
• ShichangZhangiswithHarvardUniversity,Cambridge,USA.
• YiqiaoJiniswithGeorgiaInstituteofTechnology,Atlanta,USA. methodology-centered approach examines the technical
• FanZhangandXianWuarewithJarvisResearchCenter,TencentYouTu foundationsofagentsystemsthroughthreeinterconnected
Lab,Shenzhen,China.
dimensions:construction(howagentsaredefinedandbuilt),
5202
raM
72
]LC.sc[
1v06412.3052:viXra

2
Agent Methodology Evaluation and Tools
Construction Collaboration Evolution Benchmark and Datasets Tools
Profile
Definition Centralized Self-Learning General LLM Use
Control Assessment Tools
Memory
Mechanism Decentralized Multi-agent Domain-specific LLM Create
Planning Collaboration Co-Evolution Evaluation Tools
Capability
Hybrid External Collaboration Tools Develop
Action Architecture Resource Evaluation LLM
Execution
Real-World Issues Applications
Security Privacy Social Impact
Materials
Chemistry Astronomy
Science
Agent-centric Memorization
Benefits
Security Vulnerability
Dataset
Biology Medical
Construction
Data-centric Intellectual Ethical
Social Productivity
Security Property Exploitation Concerns Gaming
Science Tools
Fig.1:AnoverviewoftheLLMagentecosystemorganizedintofourinterconnecteddimensions:❶AgentMethodology,
covering the foundational aspects of construction, collaboration, and evolution; ❷ Evaluation and Tools, presenting
benchmarks,assessmentframeworks,anddevelopmenttools;❸Real-WorldIssues,addressingcriticalconcernsaround
security,privacy,andsocialimpact;and❹Applications,highlightingdiversedomainswhereLLMagentsarebeingdeployed.
WeprovideastructuredframeworkforunderstandingthecompletelifecycleofmodernLLM-basedagentsystems.
collaboration (how they interact and work together), and collaborativesystems,whereaspriorstudieshaveoften
evolution (how they learn and improve over time). This examinedtheseaspectsseparately[22],[24].
tripartite foundation is complemented by practical consid- 3) Frontier applications and real-world focus: Beyond
erations,includingevaluationmethodologies,development addressing theoretical concepts, our work examines
tools, real-world challenges related to security and ethics, cutting-edge tools, communication protocols, and di-
anddiverseapplicationdomains.Thisframeworkshapesthe verse applications on LLM agents. We provide com-
structureofoursurvey,enablingasystematicexplorationof prehensive analysis of pressing real-world challenges
eachdimensionwhilehighlightingtheirinterconnections. including security, privacy, and ethics. This forward-
DistinctionfromPreviousSurveys.Despiteseveralsurveys looking perspective is particularly valuable as agent
exploring various aspects of AI agents in recent years, technologies transition from research to widespread
our study makes a distinctive contribution through its implementation.
methodologicalfocusandcomprehensiveanalysisofLLM Oursurveyprovidesresearchersandpractitionerswith
agentarchitectures.Previoussurveyshaveprimarilyfocused amorestructuredtaxonomyforunderstanding,comparing,
onspecificapplications(e.g.,gaming[11],[12]),deployment and advancing research of LLM agents from different per-
environments[13],[14],multi-modality[15]orsecurity[16], spectives.AsLLMagentsystemsincreasinglyintegrateinto
whileothershaveprovidedbroadoverviewswithoutade- variouscriticaldomains,understandingtheirarchitectural
tailedmethodologicaltaxonomy[1],[17].Recentworksalso foundationsbecomesessentialnotonlyforresearchersbut
haveexaminedLLM-basedagentscomparedtotraditionalAI alsoforpolicyscholars,industrypractitioners,andsociety
agents[9],multi-agentinteraction[18],workflows[19],and atlarge.Thissurveyaimstoprovidethisfoundationwhile
cooperativedecision-makingmechanisms[20].Incontrastto chartingapathforwardforthisrapidlyevolvingfield.
theseworks,oursurveystandsoutthrough:
1) Methodology-centered taxonomy: We propose a sys-
2 AGENT METHODOLOGY
tematictaxonomythatdeconstructsLLMagentsystems
intotheirfundamentalmethodologicalcomponents,in- This section presents a comprehensive framework for un-
cludingroledefinition,memorymechanisms,planning derstanding LLM-based agent systems through three in-
capabilities,andactionexecution[21]. terconnected dimensions: construction, collaboration, and
2) Build-Collaborate-Evolveframework:Weanalyzethree evolution.AsillustratedinFigure2,wefirstexamineagent
interconnecteddimensionsofLLMagents-construction, construction (Section 2.1), which establishes the founda-
collaboration, and evolution - offering a more holistic tional components including profile definition, memory
understanding than previous approaches [22], [23]. mechanisms, planning capabilities, and action execution.
Thisintegratedarchitecturalperspectivehighlightsthe Wethenexplorecollaborationparadigms(Section2.2)that
continuity between individual LLM agent design and enablemultipleagentstoworktogetherthroughcentralized

3
tnegAledoMegaugnaLegraL
Human-Curated
Camel[25],AutoGen[26],MetaGPT[27],ChatDev[28],AFlow[29]
StaticProfiles
ProfileDefinition
§2.1.1
Betch-Generated
GenerativeAgents[30],RecAgent[31],DSPy[32]
DynamicProfiles
Short-Term
ReAct[33],ChatDev[28],GraphofThoughts[34],AFlow[29]
Memory
Memory Long-Term Voyager[35],GITM[36],ExpeL[37],Reflexion[38],TPTU[39],
Mechanism Memory OpenAgents[40],Lego-Prover[41],MemGPT[42]
§2.1.2
Knowledge
RAG[43],GraphRAG[44],ChainofAgnets[45],IRCoT[46],
Retrieval
Llatrieval[47],KG-RAR[48],DeepRAG[49]
asMemory
Plan-and-solvePrompting[50],DistributedProblemSolvingand
TaskDecompo- Planning[51],ReAct[33],Chain-of-discussion[52],Tree-planner
sitionStrategies [53],ReAcTree[54],ToT[55],ReST-MCTS*[56],LLM-MARS[57],
Planning LLMasBT-planner[58],ConceptAgent[59]
Capability
§2.1.3
Feedback- BrainBody-LLM[60],TrainerAgent[61],RASC[62],REVECA[63],
DrivenIteration AdaPlanner[64],AIFP[65]
ToolUtilization TRICE[66],GPT4Tools[67],EASYTOOL[68],AvaTaR[69],
ActionExecution
§2.1.4
Physical
DriVLMe[70],ReAd[71],CollaborativeVoyager[72]
Interaction
Centralized
Coscientist[73],LLM-Blender[74],MetaGPT[27],AutoAct[75],
Control
Meta-Prompting[76],Wjudge[77]
§2.2.1
Agent Decentralized
GAgents[30],CAMEL[25],MedAgents[78],ReConcile[79],MAD
Collaboration Collaboration
[80],MADR[81],MDebate[82],AutoGen[26]
§2.2 §2.2.2
Hybrid
Architecture KnowAgent[83],WKM[84],Textgrad[85]
§2.2.3
Autonomous
SE[86],EvolutionaryOptimization[87],DiverseEvol[88],SELF-
Optimizationand
REFINE[89],STaR[90],V-STaR[91],Self-Verification[92],Self-
Self-Learning
Rewarding[93],RLCD[94],RLC[95]
§2.3.1
AgentEvolution Multi-Agent ProAgent[96],CORY[97],CAMEL[25],Red-TeamLLMs[98],
§2.3 Co-Evolution Multi-AgentDebate[82],MAD[99]
§2.3.2
Evolutionvia
KnowAgent[83],WKM[84],CRITIC[100],STE[101],SelfEvolve
ExternalResources
[102]
§2.3.3
Fig.2:Ataxonomyoflargelanguagemodelagentmethodologies.
control,decentralizedcooperation,orhybridarchitectures. profiles. The construction paradigm emphasizes modular
Finally, we investigate evolution mechanisms (Section 2.3) interoperabilitywhilepreservingsystem-widecoherence,en-
thatallowagentstoimproveovertimethroughautonomous ablingsubsequentcollaborationandevolutionaryadaptation
optimization,multi-agentco-evolution,andexternalresource mechanisms,whichwillbediscussedinlatersections.
integration. This three-dimensional framework provides a
systematicapproachtoanalyzingthefulllifecycleofLLM 2.1.1 ProfileDefinition
agentsystems. Profile definition establishes an agent’s operational iden-
tity by configuring its intrinsic attributes and behavioral
2.1 AgentConstruction patterns [25], [26]. Current methodologies encompass two
Agent construction serves as the foundational phase in approaches: human-curated static profiles ensure domain-
developingLLM-basedautonomoussystems,encompassing specific consistency through manual specification, while
thesystematicdesignofcorecomponentsthatenablegoal- batch-generated dynamic profiles adaptively modulate opera-
directedbehaviors.Thisprocessprioritizesfourinterdepen- tional parameters to stochastically yield a batch of agent
dent pillars: profile definition (2.1.1), memory mechanism initializations. These mechanisms collectively govern an
(2.1.2),planningcapability(2.1.3),andactionexecution(2.1.4). agent’sdecisionboundariesandinteractionprotocolswhile
Thesecomponentscollectivelyformarecursiveoptimization maintainingalignmentwithpredefinedobjectives.
loop,wherememoryinformsplanning,executionoutcomes Human-Curated Static Profiles. This approach establishes
update memory, and contextual feedback refines agent fixedagentprofilesthroughmanualspecificationbydomain

4
experts,embeddingexplicitrulesanddomain-specificknowl- transferred to new scenarios. Furthermore, due to LLMs’
edge. It ensures strict adherence to predefined behavioral context window limitations, practical implementations re-
guidelines and task requirements enabling standardized quireactiveinformationcompression(e.g.,summarizationor
communicationprotocolsamongagents.Thisisparticularly selectiveretention)andimposemanyconstraintsonmulti-
effective in scenarios demanding high interpretability and turninteractiondepthtopreventperformancedegradation.
regulatorycompliance.Suchframeworkstypicallyemploy Long-Term Memory. Long-term memory systematically
coordinatedinteractionsbetweenpredefinedagentcompo- archives agents’ intermediate reasoning trajectories and
nentstoachievecomplexfunctionalitiesthroughstructured synthesizes them into reusable tools for future invoca-
communication patterns. Representative implementations tion. This process transforms ephemeral cognitive efforts
demonstrate two key paradigms: systems like Camel [25], into persistent operational assets through three dominant
AutoGen [26], and OpenAgents [40] orchestrate human- paradigms:❶skilllibrariesthatcodifyproceduralknowledge
agentcollaborationthroughpredefinedconversationalroles (e.g.,Voyager’sautomatedskilldiscoveryinMinecraft[35]
(e.g., user proxy and assistant), enabling task execution and GITM’s text-based knowledge base [36]), ❷ experi-
throughstructureddialogues.Meanwhile,frameworkssuch ence repositories that store success/failure patterns (e.g.,
as MetaGPT [27], ChatDev [28], and AFlow [29] showcase ExpeL’sdistilledexperiencepool[37]andReflexion’strial-
role-based coordination patterns. ChatDev specializes in optimizedmemory[38]),and❸toolsynthesisframeworks
codedevelopmentbycoordinatingstatictechnicalroles(e.g., that evolve capabilities through combinatorial adaptation
product managers and programmers) with deterministic (e.g.,TPTU’sadaptivetoolcomposition[39]andOpenAgents’
interactionprotocols,whileMetaGPTandAFlowextendthis self-expandingtoolkit[40]).Cross-domainimplementations,
paradigm to general task solving through structured role such as Lego-Prover’s theorem bank [41] and MemGPT’s
orchestration. tiered memory architecture [42], further demonstrate how
Batch-GeneratedDynamicProfiles.Thisparadigmemploys structuredlong-termstorageenhancesreasoningefficiency
parameterized initialization to systematically generate di- throughstrategicknowledgereuse.
verseagentprofilesthatemulatehumansocietalbehaviors. Knowledge Retrieval as Memory. This paradigm di-
By injecting controlled variations into personality traits, vergesfromagent-internalmemorygenerationbyintegrat-
knowledge backgrounds, or value systems during agent ing external knowledge repositories into generation pro-
creation(e.g.,throughtemplate-basedpromptingorlatent cesses,effectivelyexpandingagents’accessibleinformation
space sampling), the framework produces heterogeneous boundaries. Current implementations exhibit three domi-
populationscapableofexhibitingcomplexsocialdynamics. nant approaches: ❶ Static knowledge grounding through
Suchparameter-drivendiversityisessentialforsimulating text corpora (RAG [43]) or structured knowledge graphs
realistic human-agent interactions in applications ranging (GraphRAG [44]), ❷ Interactive retrieval that integrates
from social behavior studies to emergent group intelli- agent dialogues with external queries, as demonstrated in
gence simulations. This is demonstrated in systems for ChainofAgents[45]whereshort-terminter-agentcommu-
human behavior simulation [30] and simulated user data nicationstriggercontextualizedknowledgefetching,and❸
collection[31]wheredifferentprofileconfigurationsdirectly Reasoning-integrated retrieval, exemplified by IRCoT [46]
shape collective interaction patterns. Moreover, DSPy [32] andLlatrieval[47],whichinterleavestep-by-stepreasoning
can further optimize the parameters of the agent profile with dynamic knowledge acquisition. Advanced variants
initialization. likeKG-RAR[48]furtherconstructtask-specificsubgraphs
duringreasoning,whileDeepRAG[49]introducesfine-tuned
2.1.2 MemoryMechanism retrievaldecisionmodulestobalanceparametricknowledge
and external evidence. These hybrid architectures enable
Memorymechanismsequipagentswiththeabilitytostore,
agentstotranscendtrainingdatalimitationswhilemaintain-
organize,andretrieveinformationacrosstemporaldimen-
ingcontextualrelevance,establishingknowledgeretrievalas
sions. Short-term memory maintains transient contextual
criticalinfrastructureforscalablememorysystems.
data for immediate task execution, while long-term mem-
orypreservesstructuredexperientialknowledgeforpersis-
2.1.3 PlanningCapability
tentreference.Integratingknowledgeretrievalmechanisms
further optimizes information accessibility with Retrieval- PlanningcapabilitiesareacriticalaspectofLLMagents’abil-
AugmentedGeneration(RAG)techniques[43]. ities,enablingthemtonavigatethroughcomplextasksand
Short-Term Memory. Short-term memory retains agent- problem-solvingscenarioswithhighaccuracy[103].Effective
internal dialog histories and environmental feedback to planningisessentialfordeployingLLMagentsinreal-world
support context-sensitive task execution. This mechanism applications, where they must handle a diverse range of
is widely implemented in frameworks such as ReAct [33] complex tasks and scenarios. The planning capability of
for thinking with reflection, ChatDev [28] for software an LLM agent can be viewed from two perspectives: task
development, Graph of Thoughts [34] for solving elabo- decompositionandfeedback-driveniteration.
rate problems, and AFlow [29] for workflow automation, Task Decomposition Strategies. Task decomposition rep-
demonstrating its versatility across domains. While this resents a basic approach to enhancing LLM planning ca-
mechanismenablesdetailedreasoningthroughinteractive pabilities by breaking down complex problems into more
exchanges, its transient nature limits knowledge retention manageablesubtasks.Althoughsolvinganentireproblem
beyondimmediatecontexts—intermediatereasoningtraces may be challenging for LLM agents, they can more easily
oftendissipateaftertaskcompletionandcannotbedirectly handle subtasks and then integrate the results to address

5
TABLE1:Asummaryofagentcollaborationmethods.
thefullproblem.Taskdecompositionstrategiesfallintotwo
main categories: single-path chaining and multi-path tree
Category Method KeyContribution
expansion.
Coscientist[73] Human-centralizedexperimentalcontrol
Single-pathchainingisasimplemethodwiththesimplist LLM-Blender[74] Cross-attentionresponsefusion
MetaGPT[27] Role-specializedworkflowmanagement
CentralizedControl
versionaszero-shotchain-of-thought[104],[105].Itfirstasks AutoAct[75] Triple-agenttaskdifferentiation
Meta-Prompting[76] Meta-prompttaskdecomposition
theagenttodeviseaplan,whichconsistsofasequenceof WJudge[77] Weak-discriminatorvalidation
subtasksthatarebuiltupononeanother.Subsequently,the MedAgents[78] Expertvotingconsensus
ReConcile[79] Multi-agentanswerrefinement
agent is asked to solve the subtasks in the order they are METAL[115] Domain-specificrevisionagents
DS-Agent[116] Database-drivenrevision
DecentralizedCollaboration
presented[50],[105].Thisplan-and-solveparadigm[51]is MAD[80] Structuredanti-degenerationprotocols
MADR[81] Verifiablefact-checkingcritiques
straightforward and easy to implement. However, it may MDebate[82] Stubborn-collaborativeconsensus
AutoGen[26] Group-chatiterativedebates
suffer from a lack of flexibility and error accumulation
CAMEL[25] Groupedrole-playcoordination
duringchaining,astheagentisrequiredtofollowthepre- AFlow[29] Three-tierhybridplanning
EoT[117] Multi-topologycollaborationpatterns
HybridArchitecture
defined plan without any deviation during the problem- DiscoGraph[118] Pose-awaredistillation
DyLAN[119] Importance-awaretopology
solvingprocedure.Therefore,onelineofworkproposesto MDAgents[120] Complexity-awarerouting
adoptdynamicplanningthatonlygeneratesthenextsubtask
basedonthecurrentsituationoftheagent[33],[105].This
help evaluate the agent’s performance and thus guide its
enables the agent to receive environmental feedback and
planning.Forinstance,theagentcanusefeedbacktoupdate
adjust its plan accordingly, enhancing its robustness and
(regenerate)itsplan,adjustitsreasoningpath,orevenmodify
adaptability. Moreover, another line of work proposes to
itsgoal.Thisiterativeprocesscontinuesuntilasatisfactory
usemultiplechain-of-thoughtstoimprovetherobustnessof
planisachieved[64],[65].
theplanningprocess.Thisissimilartoensemblemethods,
involvingself-consistency[62],[106],majorityvoting[107],
2.1.4 ActionExecution
and agent discussion [52] to combine multiple chains. By
combining the wisdom of multiple chains, the agent can With the planning capability, it is important for the LLMs
makemoreaccuratedecisionsandreducetheriskoferror tohavetheabilitytoexecutetheplannedactionsinthereal
accumulation. world. Action execution is a critical aspect of LLM agents’
A more complicated method is to use trees instead abilities,asgoodplansareuselessiftheagentcannotexecute
of chains as the planning data structure, where multiple themeffectively.Actionexecutioninvolvestwoaspects:tool
possible reasoning paths exist when the agent is planning, utilization[113],andphysicalinteraction[114].
and the agent is allowed to backtrack with information Tool utilization [113] is an important aspect of LLM
from feedback [53], [54]. Long et al. [55] propose a tree- action execution, enabling a wide range of abilities such
of-thought (ToT) method that explores the solution space as precise calculation of numbers, up-to-date information
through a tree-like thought process. This allows the LLMs understanding, and proficient code generation. The tool
to backtrack to previous states, which makes it possible useabilityinvolvestwoaspects:toolusedecisionandtool
for the model to correct its previous mistakes, enabling selection. The tool-use decision is the process of deciding
applications to various complicated tasks that involve the whethertouseatooltosolveaproblem.Whentheagentis
”trial-error-correct”process.Inmorerealisticscenarios,the generatingcontentwithlessconfidenceorfacingproblems
agentcangatherfeedbackfromtheenvironmentorhumans relatedtospecifictoolfunctions,theagentshoulddecideto
and dynamically adjust its reasoning path, potentially in- usespecifictools[66],[67].Toolselectionisanotherimportant
corporatingreinforcementlearning[56],[108].Thisenables aspect of tool utilization, involving the understanding of
the agent to make more informed decisions in real-world toolsandtheagent’scurrentsituation[68],[69].Forexample,
applicationsusingadvancedalgorithmssuchasMonteCarlo Yuanetal.[68]proposesimplifyingthetooldocumentation
TreeSearch[109],facilitatingusecasesinrobotics[57]–[59] to better understand the available tools, enabling a more
andgame-playing[110],[111]. accurateselectionoftools.
Physical interaction [114] is a fundamental aspect of
Feedback-DrivenIteration.Feedback-driveniterationisacru-
embodied LLM agents. Their ability to perform specific
cialaspectofLLMplanningcapabilities,enablingtheagent
actionsintherealworldandinterpretenvironmentalfeed-
tolearnfromthefeedbackandenhanceitsperformanceover
backiscrucial.Whendeployedinreal-worldsettings,LLM
time.Feedbackcanoriginatefromvarioussources,suchas
agentsmustcomprehendvariousfactorstoexecuteactions
environmentalinput,humanguidance,modelintrospection,
accurately. These factors include robotic hardware [114],
andmulti-agentcollaboration.
social knowledge [70], and interactions with other LLM
Environmentalfeedbackisoneofthemostcommontypes agents[71],[72].
offeedbackinrobotics[60],generatedbytheenvironment
in which the embodied agent operates. Human feedback,
2.2 AgentCollaboration
anothercrucialtype,comesfromuserinteractionsormanu-
ally labeled data prepared in advance [61], [112]. Model Collaboration among LLM agents plays a crucial role in
introspection provides an additional source of feedback, extending their problem-solving capabilities beyond indi-
which is generated by the agent itself [62]. Multi-agent vidual reasoning. Effective collaboration enables agents to
collaboration also serves as a feedback mechanism, where leverage distributed intelligence, coordinate actions, and
multiple agents work together to solve a problem and refinedecisionsthroughmulti-agentinteractions[26],[121].
exchange insights [63], [112]. These sources of feedback We categorize existing collaboration paradigms into three

6
fundamental architectures: centralized control, decentralized Revision-based Systems. In this paradigm, agents only
cooperation,andhybridarchitectures.Theseparadigmsdiffer observefinalizeddecisionsgeneratedbypeersanditeratively
intheirdecisionhierarchies,communicationtopologies,and refineasharedoutputthroughstructurededitingprotocols.
taskallocationmechanisms,eachofferingdistinctadvantages Thisapproachtypicallyproducesmorestandardizedandde-
forspecificapplicationscenarios. terministicoutcomes.Forinstance,MedAgents[78]employs
predefineddomain-specificexpertagentsthatsequentially
2.2.1 CentralizedControl
proposeandmodifydecisionsindependently,withconsensus
Centralized control architectures employ a hierarchical co- achieved through final voting. ReConcile [79] coordinates
ordinationmechanismwhereacentralcontrollerorganizes agentstoiterativelyrefineanswersthroughmutualresponse
agent activities through task allocation and decision inte- analysis,confidenceevaluation,andhuman-curatedexem-
gration,whileothersub-agentscanonlycommunicatewith plars. METAL [115] introduces specialized text and visual
thecontroller.Thisparadigmfeaturestwoimplementation revision agents for chart generation tasks, demonstrating
strategies: explicit controller systems utilize dedicated co- how domain-specific refinement improves output quality.
ordination modules (often implemented as separate LLM Notably,revisionsignalsmayoriginatenotonlyfromagent
agents) to decompose tasks and assign subgoals, while interactions but also from external knowledge bases [116],
differentiation-based systems achieve centralized control by [123],enablinghybridrefinementstrategies.
usingpromptstoguidethemetaagentinassumingdistinct
Communication-basedSystems.Comparedtorevision-based
sub-roles.Thecentralizedapproachexcelsinmission-critical
approaches, communication-based methods feature more
scenarios requiring strict coordination, such as industrial
flexibleorganizationalstructures,allowingagentstodirectly
automation[122]andscientificresearch[73].
engageindialoguesandobservepeers’reasoningprocesses.
Explicit Controller Systems. Multiple related works have This makes them particularly suitable for modeling dy-
beendevelopedtoexplicitlyimplenmentcentralizedarchitec- namicscenariossuchashumansocialinteractions[30].Key
tures.TheCoscientist[73]exemplifiestheexplicitcontroller implementations include: MAD [80] employs structured
paradigm, where a human operator serves as the central communication protocols to address the ”degeneration-of-
controller.Itestablishesstandardizedscientificexperimental thought” problem, where agents overly fixate on initial
workflows,allocatesspecializedagentsandtoolstodistinct solutions. MADR [81] enhances this by enabling agents to
experimentalphases,andmaintainsdirectcontroloverthe critique implausible claims, refine arguments, and gener-
final execution plan. LLM-Blender [74] explicitly creates ateverifiableexplanationsforfact-checking.MDebate[82]
a controller that employs a cross-attention encoder for optimizesconsensus-buildingthroughstrategicalternation
pairwisecomparisontoidentifythebestresponses,andthen betweenstubbornadherencetovalidpointsandcollaborative
fuses the top-ranked responses, enhancing their strengths refinement.AutoGen[26]implementsagroup-chatframe-
whilemitigatingweaknesses.MetaGPT[27]simulatesreal- work that supports multi-agent participation in iterative
worldsoftwaredevelopmentworkflows,direcltyassigning debatesfordecisionrefinement.
specializedmanagerstocontroldistinctfunctionalrolesand
phases. 2.2.3 HybridArchitecture
Differentiation-based Systems. AutoAct [75] exemplifies
Hybrid architectures strategically combine centralized co-
thedifferentiation-basedparadigm,whichimplicitlydiffer-
ordination and decentralized collaboration to balance con-
entiates the meta-agent into three sub-agents—plan-agent,
trollabilitywithflexibility,optimizeresourceutilization,and
tool-agent, and reflect-agent—to break down the complex
adapt to heterogeneous task requirements. This approach
ScienceQA task. Meta-Prompting [76] decomposes com-
introducestwoimplementationpatterns:staticsystemswith
plex tasks into domain-specific subtasks through carefully
predefinedcoordinationrulesanddynamicsystemsfeaturing
craftedmeta-prompts.Asinglemodelactsasacoordinator,
self-optimizingtopologies.
dynamically assigning subtasks to specialized sub-agents
Static Systems. Static systems predefine fixed patterns for
guidedbytask-orientedprompts.Thecentrolmanagerthen
combiningdifferentcollaborationmodalities.Representative
integrates all intermediate outputs to produce the final
implementationsinclude:CAMEL[25]partitionsagentsinto
solution.Theseworkspredominantlyemployhighlycapable
intra-groupdecentralizedteamsforrole-playingsimulations,
agentsascentralcontrollerstooptimizetaskallocationand
whilemaintaininginter-groupcoordinationthroughcentral-
decisionaggregation.However,WJudge[77]demonstrates
izedgovernance.AFlow[29]employsathree-tierhierarchy
thatevencontrollerswithlimiteddiscriminativepowercan
consisting of centralized strategic planning, decentralized
alsosignificantlyenhancetheoverallperformanceofagent
tacticalnegotiation,andmarket-drivenoperationalresource
systems.
allocation.EoT[117]formalizesfourcollaborationpatterns
2.2.2 DecentralizedCollaboration (BUS, STAR, TREE, RING)toalignnetworktopologieswith
In contrast to centralized architectures where a single con- specifictaskcharacteristics.
trol node often becomes a bottleneck due to handling all DynamicSystems.Recentinnovationsintroduceneuraltopol-
inter-agentcommunication,taskscheduling,andcontention ogyoptimizersthatdynamicallyreconfigurecollaboration
resolution,decentralizedcollaborationenablesdirectnode- structuresbasedonreal-timeperformancefeedback,enabling
to-nodeinteractionthroughself-organizingprotocols.This automaticadaptationtochangingconditions.Keyimplemen-
paradigm can be further categorized into two distinct tationsdemonstratethisparadigm:DiscoGraph[118]intro-
approaches: revision-based systems and communication-based ducestrainablepose-awarecollaborationthroughateacher-
systems. student framework. The teacher model with holistic-view

7
TABLE2:Asummaryofagentevolutionmethods.
by identifying and addressing errors. For instance, SELF-
REFINE[89]appliesiterativeself-feedbacktoimprovegen-
Category Method KeyContribution
SE[86] Adaptivetokenmaskingforpretraining eratedresponseswithoutexternalsupervision.Inreasoning
Self-SupervisedLearning EvolutionaryOptimization[87] Efficientmodelmergingandadaptation
DiverseEvol[88] Improvedinstructiontuningviadiversedata tasks,STaR[90]andV-STaR[91]trainmodelstoverifyand
SELF-REFINE[89] Iterativeself-feedbackforrefinement refinetheirownproblem-solvingprocesses,reducingreliance
Self-Reflection&Self-Correction S V S T e -S l a f T R -V a [ R e 9 r 0 i [ fi 9 ] 1 ca ] tion[92] B B Tr o a a c o i k t n s w i t n r a g a r p d a p v v in e e g r r i i fi fi re c e a a r s t u i o o s n n i i n n f g o g r D w c P o it O r h re f c e t w ion rationales on labeled data. Additionally, self-verification techniques
Self-Rewarding[93] LLM-as-a-Judgeforself-rewarding enable models to retrospectively assess and correct their
Self-Rewarding&RL RLCD[94] Contrastivedistillationforalignment
RLC[95] Evaluation-generationgapforoptimization outputs, leading to more reliable decision-making [92].
ProAgent[96] Intentinferenceforteamwork
CooperativeCo-Evolution CORY[97] Multi-agentRLfine-tuning TheseapproachescollectivelyenhanceLLMagents’ability
CAMEL[25] Role-playingframeworkforcooperation
Red-TeamLLMs[98] Adversarialrobustnesstraining to self-reflectand self-correct, reducing hallucinationsand
CompetitiveCo-Evolution Multi-AgentDebate[82] Iterativecritiqueforrefinement
MAD[99] Debate-drivendivergentthinking improvingreasoningquality.
Knowledge-EnhancedEvolution K W n K o M wA [8 g 4 e ] nt[83] A Sy c n ti t o h n es k iz n i o n w g l p ed ri g o e r f a o n r d p d la y n n n a i m ng icknowledge Self-RewardingandReinforcementLearning.Self-rewarding
CRITIC[100] Tool-assistedself-correction
Feedback-DrivenEvolution STE[101] Simulatedtrial-and-errorfortoollearning and reinforcement learning approaches enable LLMs to
SelfEvolve[102] Automateddebuggingandrefinement
enhanceperformancebygeneratinginternalrewardsignals.
Self-generatedrewardshelpmodelsrefinedecision-making,
inputsguidesthestudentmodelviafeaturemapdistillation, with techniques ensuring stable and consistent learning
while matrix-valued edge weights enable adaptive spatial improvements[93].Contrastivedistillationfurtherenables
attentionacrossagents.DyLAN[119]firstutilizestheAgent modelstoalignthemselvesthroughself-rewardingmecha-
Importance Score to identify the most contributory agents nisms[94].Additionally,RLC[95]leveragestheevaluation-
and then dynamically adjusts the collaboration structure generation gap via reinforcement learning strategies, fa-
tooptimizetaskcompletion.MDAgents[120]dynamically cilitating self-improvement. These methods enhance LLM
assigns collaboration structures based on the task at hand. adaptability by integrating self-rewarding strategies and
Itfirstperformsacomplexitychecktoclassifytasksaslow, reinforcementlearningparadigms.
moderate,orhighcomplexity.Simpletasksarehandledby
a single agent, while more complex tasks are addressed 2.3.2 Multi-AgentCo-Evolution
throughhierarchicalcollaboration. Multi-agentco-evolutionenablesLLMstoimprovethrough
interactions with other agents. This involves cooperative
learning, where agents share information and coordinate
2.3 AgentEvolution
actions, as well as competitive co-evolution, where agents
LLMAgentsareevolvingthroughvariousmechanismsthat engage in adversarial interactions to refine strategies and
enable autonomous improvement, multi-agent interaction, enhanceperformance.
andexternalresourceintegration.Thissectionexploresthree Cooperative and Collaborative Learning. Multi-agent col-
keydimensionsofagentevolution:autonomousoptimization laborationenhancesLLMsbyenablingknowledgesharing,
andself-learning,multi-agentco-evolution,andevolutionvia joint decision-making, and coordinated problem-solving.
externalresources.Thesemechanismscollectivelyenhance For instance, ProAgent [96] enables LLM-based agents
modeladaptability,reasoning,andperformanceincomplex to adapt dynamically in cooperative tasks by inferring
environments.WesummarizethemethodsinTable2. teammates’intentionsandupdatingbeliefs,enhancingzero-
shotcoordination.CORY[97]extendsRLfine-tuningintoa
2.3.1 AutonomousOptimizationandSelf-Learning cooperativemulti-agentframework,whereLLMsiteratively
improve through role-exchange mechanisms, enhancing
Autonomous optimization and self-learning allow LLMs
policyoptimalityandstability.CAMEL[25]developsarole-
toimprovetheircapabilitieswithoutextensivesupervision.
playingframeworkwherecommunicativeagentscollaborate
This includes self-supervised learning, self-reflection, self-
autonomouslyusinginceptionprompting,improvingcoor-
correction,andself-rewardingmechanismsthatenablemod-
dinationandtask-solvingefficiencyinmulti-agentsettings.
elstoexplore,adapt,andrefinetheiroutputsdynamically.
Theseapproachescontributetomoreefficient,adaptable,and
Self-Supervised Learning and Adaptive Adjustment. Self- intelligentmulti-agentLLMsystems.
supervised learning enables LLMs to improve using un- CompetitiveandAdversarialCo-Evolution.Competitiveco-
labeled or internally generated data, reducing reliance on evolutionstrengthensLLMsthroughadversarialinteractions,
human annotations. For example, self-evolution learning debate, and strategic competition. For example, Red-team
(SE)[86]enhancespretrainingbydynamicallyadjustingto- LLMs [98] dynamically evolve in adversarial interactions,
kenmaskingandlearningstrategies.Evolutionaryoptimiza- continuously challenging LLMs to uncover vulnerabilities
tiontechniquesfacilitateefficientmodelmergingandadap- andmitigatemodecollapse,leadingtomorerobustsafety
tation,improvingperformancewithoutextensiveadditional alignment. Du et al. propose a multi-agent debate frame-
resources [87]. DiverseEvol [88] refines instruction tuning work [82] to enhance reasoning by having multiple LLMs
byimprovingdatadiversityandselectionefficiency.These critique and refine each other’s arguments over multiple
advancementscontributetotheautonomousadaptabilityof rounds, improving factuality and reducing hallucinations.
LLMs,enablingmoreefficientlearningandgeneralization Furthermore, the MAD framework [99] structures debates
acrosstasks. amongagentsinatit-for-tatmanner,encouragingdivergent
Self-ReflectionandSelf-Correction.Self-reflectionandself- thinking and refining logical reasoning in complex tasks.
correction enable LLMs to iteratively refine their outputs These competitive co-evolution strategies drive LLMs to

8
toolshavebecomeessentialcomponentsoftheagentecosys-
Evaluation and Tools
tem.Thissectionexploresthecomprehensivelandscapeof
Benchmark and Datasets Tools
benchmarks,datasets,andtoolsthatenablethedevelopment,
assessment,anddeploymentofLLMagents.Wefirstexamine
As G s e e n ss e m ra e l nt Mult C i a -d p i a m b e il n it s y ional And S D e y l n f a - m ev ic olving T L o L o M ls A U g se e d nt b s y K R n e o t w r l i e e d va g l e Computation API Interactions evaluation methodologies in Section 3.1, covering general
assessmentframeworks,domain-specificevaluationsystems,
andcollaborativeevaluationapproaches.Wethendiscussthe
toolsecosysteminSection3.2,includingtoolsusedbyLLM
Dom Ev a a in lu -s a p ti e o c n ific C D om om pe a t in e - n s c p y e T ci e f s ic t s Environ R m ea e l n - t w o S r im ld u lation To L ol L s M C r A e g a e t n e t d s by Creation Decision Execution Reflection agents,toolscreatedbyagentsthemselves,andinfrastructure
fordeployingagentsystems.
Co E l v la a b lu o a r t a i t o i n on Inte W ra e c b tion Gen C e o r d a e tion Tool L s L f M o r A D ge e n p t lo s ying Productionization and O M p a e i r n a t t e i n o a n nce Mod P e ro l t C o o c n o t l ext 3.1 EvaluationBenchmarksandDatasets
The evolution of LLM agents has driven the creation of
Fig. 3: An overview of evaluation benchmarks and tools specializedbenchmarksthatsystematicallyevaluateagent
for LLM agents. The left side shows various evaluation capabilities across technical dimensions and application
frameworks categorized by general assessment, domain- domains.Theseframeworksaddressthreekeyrequirements:
specificevaluation,andcollaborationevaluation.Theright general assessment frameworks, domain-specific scenario
side illustratestools used byLLM agents, toolscreatedby simulation,andcollaborativeevaluationofcomplexsystems.
agents,andtoolsfordeployingagents.
3.1.1 GeneralAssessmentFrameworks
developstrongerreasoning,resilience,andstrategicadapt-
The evolution of intelligent agents requires evaluation
abilityinamulti-agentadversarialmanner.
frameworks to move beyond simple success-rate metrics
tocomprehensivecognitiveanalysis.Recentadvancesfocus
2.3.3 EvolutionviaExternalResources
onbuildingadaptiveandinterpretableassessmentsystems
External resources enhance the evolution of agents by
capableofcapturingthesubtleinterplaybetweenreasoning
providingstructuredinformationandfeedback.Knowledge-
depth,environmentaladaptability,andtaskcomplexity.
enhanced evolution integrates structured knowledge to
Multi-DimensionalCapabilityAssessment.Modernbench-
improve reasoning and decision-making, while external
marks are increasingly adopting a hierarchical paradigm
feedback-drivenevolutionleveragesreal-timefeedbackfrom
that dissects agent intelligence across various dimensions
toolsandenvironmentstorefinemodelperformance.
of reasoning, planning, and problem solving. AgentBench
Knowledge-Enhanced Evolution.LLMscanevolvebyinte-
[124] builds a unified test field across eight interactive
gratingstructuredexternalknowledge,improvingreasoning,
environments, revealing the advantages of a commercial
decision-making,andtaskexecution.Forexample,KnowA-
LLM in complex reasoning. Mind2Web [125] extends this
gent[83]improvesLLM-basedplanningbyintegratingaction
paradigm to web interaction scenarios, proposing the first
knowledge,constrainingdecisionpaths,andmitigatinghallu-
generalistagentforevaluating137real-worldwebsiteswith
cinations,leadingtomorereliabletaskexecution.Theworld
differenttasksspanning31domains.Thisopenenvironment
knowledge model (WKM) [84] enhances agent planning
benchmarkenablesmulti-dimensionalcapabilityassessment
bysynthesizingexpertandempiricalknowledge,providing
through real web-based challenges. This is in line with
globalpriorsanddynamiclocalknowledgetoguidedecision-
MMAU[126],whichenhancesexplainabilitythroughgranu-
making.Theseapproachescollectivelyimprovetheevolution
larcapabilitymappingandbreaksdownagentintelligence
of LLM by incorporating diverse and structured external
intofivecorecompetenciesbymorethan3,000cross-domain
information.
tasks.BLADE[127]extendsevaluationtoscientificdiscovery
ExternalFeedback-DrivenEvolution.LLMscanrefinetheir by tracking the analytical decision patterns of expert vali-
behavior by leveraging external feedback from tools, eval- dationworkflows.VisualAgentBench[128]furtherextends
uators, and humans to improve performance iteratively. thisapproachtomultimodalfoundationagents,establishing
For example, CRITIC [100] allows LLMs to validate and aunifiedbenchmarkacrossmaterializedinteractions,GUI
revisetheiroutputsthroughtool-basedfeedback,improving operations,andvisualdesigntasks,andrigorouslytesting
accuracyandreducinginconsistencies.STE[101]enhances the LLM’s ability to handle the dynamics of the complex
toollearningbysimulatingtrial-and-error,imagination,and visual world. Embodied Agent Interface [129] introduces
memory, enabling more effective tool use and long-term modular inference components (object interpretation, sub-
adaptation.SelfEvolve[102]adoptsatwo-stepframework object decomposition, etc.) to provide fine-grained error
whereLLMsgenerateanddebugcodeusingfeedbackfrom classification for embedded systems. CRAB [130] offers
execution results, enhancing performance without human cross-platformtestingwithgraphics-basedassessmentand
intervention. These approaches enable LLMs to evolve a unified Python interface. These frameworks emphasize
iteratively by integrating structured feedback, improving the shift from a single measure of success to multifaceted
adaptabilityandrobustness. cognitiveanalysis.
Dynamic and Self-Evolving Evaluation Paradigms. Next-
3 EVALUATION AND TOOLS generation framework addresses baseline obsolescence
As LLM agents continue to evolve in complexity and through adaptive generation and human-AI collaboration.
capability, robust evaluation frameworks and specialized BENCHAGENTS [131] automatically creates benchmarks

9
throughLLMagentsforplanning,validating,andmeasuring capabilities in dynamic environments. GTA [150] further
designs, enabling rapid capacity expansion. Benchmark integratesreal-worlddeployedtoolsandmulti-modalinputs
self-evolving[132]introducessixrefactoringoperationsto (images,webpages)toevaluatereal-worldproblem-solving
dynamically generate test instances for short-cut biases. capabilities.
Revisiting Benchmark [133] proposed TestAgent with re-
3.1.3 CollaborativeEvaluationofComplexSystems
inforcementlearningfordomainadaptiveassessment.Other
methodssuchasSeal-Tools[134](1,024nestedinstancesof Asagencysystemsevolvetowardorganizationalcomplexity,
toolcalls)andCToolEval[135](398ChineseAPIsacross14 evaluationframeworksmustquantifyemergentcoordination
domains),complementstaticdatasetsandstandardizetool patternsandcollectiveintelligence.Recentapproachesshift
usageevaluation. evaluation from isolated agent proficiency to system-level
cognitive collaboration, revealing scalability challenges in
3.1.2 Domain-SpecificEvaluationSystem multi-agentworkflows.
Multi-Agent System Benchmarking. TheAgentCompany
Theincreasingspecializationofagentapplicationsrequires
[151]pioneeredenterprise-levelassessmentsusingsimulated
evaluationsystemstailoredtodomain-specificknowledge
softwarecompanyenvironmentstotestwebinteractionand
andenvironmentalconstraints.Researchersaredeveloping
code collaboration capabilities. Comparative analysis like
dual-axis frameworks that combine vertical competency
AutoGenandCrewAI[152]establishesmethodologicalstan-
testingforprofessionalscenarioswithhorizontalvalidation
dardsthroughMLcodegenerationchallenges.LargeVisual
inreal-worldsimulatedenvironments.
LanguageModelSurvey[153]systematizesover200multi-
Domain-SpecificCompetencyTests.Severalkeyapplication
modal benchmarks. For multi-agent collaboration, MLRB
areas are specifically benchmarked with scenario-driven
[154] designs 7 competition-level ML research tasks, and
assessments.Forexample,healthcareapplicationsarerigor-
MLE-Bench[144]evaluatesKaggle-stylemodelengineering
ouslytestedbyMedAgentBench[136]andAIHospital[137].
through71real-worldcompetitions.Theseeffortscollectively
Specifically,MedAgentBenchcontainstasksdesignedby300
establishrigorousevaluationprotocolsforemergentagent
cliniciansinanFHIR-compliantenvironment,whiletheAI
coordinationcapabilities.
hospital simulates clinical workflows through multi-agent
collaboration.Theautonomousdrivingsystembenefitsfrom
3.2 Tools
LaMPilot[138],whichconnectstheLLMtotheautonomous
Tools are an important part of LLM agents. When dealing
driving architecture through code generation benchmarks.
withcomplextasks,LLMagentscancallonexternaltoolsto
Data science capabilities are evaluated by DSEval [139]
generatemorepreciseanswers.Dependingontheircreativity,
and DA-Code [140], covering lifecycle management from
they can also create tools to solve tasks. In addition, LLM
datadebatetomodeldeployment,whileDCA-Bench[141]
agents need corresponding tools for deployment, mainte-
evaluatesdatasetcurationagentsbasedonreal-worldquality
nance,anddataacquisition.
issues.TravelPlanner[142]providesasandboxenvironment
for travel planning scenarios. It contains 1225 planning
3.2.1 ToolsusedbyLLMagents
tasks that require multi-step reasoning, tool integration,
Since LLM agents do not perform well in handling some
and constraint balancing under realistic conditions (e.g.,
specifictasks,suchaasthoserequiringreal-timeinformation
budgetandtime).Machinelearningengineeringcapabilities,
and accurate calculations, external tools are introduced to
measured by MLAgant-Bench [143] and MLE-Bench [144],
help the LLM agents perform these tasks more effectively.
simulatekaggle-likechallengesthatrequireoptimizationof
These external tools can be categorized into three main
anend-to-endpipeline.Security-focusedAgentHarm[145]
groups.
curated 440 malicious agent tasks in 11 hazard categories,
andsystematicallyassessedLLMabuseriskforthefirsttime
Knowledge Retrieval.Forthosereal-timeinformationthat
in a multi-step tool usage scenario. These domain-specific LLMagentsarenotawareof,knowledgeretrievaltools,such
benchmarksrevealsignificantperformancegapscompared as search engines, can help LLM agents to quickly access
togeneraltestinginpracticalapplications. up-to-dateknowledgesothattheyarenolongerlimitedto
theknowledgebasetheyhadduringtraining.WebGPT[155]
Real-WorldEnvironmentSimulation.Severalbenchmarks
successfullycombinesonlinesearchenginesandLLMswith
bridge the simulation to reality gap with real interactive
the incorporation of the commercial API1. WebCPM [156],
environments. OSWorld [146] builds the first scalable real-
inspiredbyWebGPT,developsawebsearchinterfaceand
computer ecosystem that supports 369 multi-application
uses it to construct the first Chinese long-form question
tasksacrossUbuntu/Windows/macOS.TurkingBench[147]
answer(LFQA)dataset.ToolCoder[157]usesDuckDuckgo2
evaluates 158 micro-tasks using a crowdsourcing-derived
asthesearchengineforthosefrequentlyusedpubliclibraries
HTMLinterface,andLaMPilot[138]introducesanexecutable
andemploystheBM25[158]scoreforthoseless-knownor
codegenerationbenchmarkforautonomousdrivingscenar-
privatelibraries.
ios.OmniACT[148]provides32Kweb/desktopautomation
Computation.LLMagentsmaysufferhallucinationswhen
instanceswithbasicrequirementsforvisualization.EgoLife
dealingwithtasksrequiringprecisecomputation.Compu-
[149] advances real-world simulation through a 300-hour
tationaltoolslikePythoninterpretersandmathcalculators
multimodalegocentricdatasetcapturingdailyhumanactivi-
ties(e.g.,shopping,cooking,socializing),pairedwithEgo-
1.https://www.microsoft.com/en-us/bing/apis/bing-web-search-
LifeQAtasksthattestagents’long-termmemoryretrieval, api
healthhabitmonitoring,andpersonalizedrecommendation 2.https://duckduckgo.com

10
canhelpLLMagentswithcomplexcodeexecutionorcom-
Real-world Issues
putationaltasks.AutoCoder[159]designsadatasetwiththe
interactionwithcodingexecutionresultstofacilitateLLM-
Security
basedcodegeneration.RLEF[160]improvescodegeneration Age S n e t c - u c r e i n ty tr ic Ad A v t e t r a s c a k r s i al J A a t il t b a r c e k a s k B A a t c t k a d c o k o s r Coll M ab o o d r e a l tion Da S t e a c -c u e r n it t y ric Ext A er t n ta a c l k D s ata In A te tt r a a c c k ti s on
performancethroughanend-to-endreinforcementlearning
frameworkthatenablesLLMstolearnfeedbackfromcode
executors. CodeActAgent [161] is an automatic agentic M Vu e l m ne o r r a iz b a i t li i t o y n Ex A t t D r t a a a t c c a t k i s on I M A nf t e e t m r a e b c n k e c s r e I A A n t f t t e t r r a ib e c u n k t c s e e Intel E le x c p t lo u i a t l a P t r io o n perty Mod A e t l t S ac te k a s ling Prom A p t t t a S c t k e s aling Privacy
systemwhichcanupdatetheactionsbasedontheinteraction
with the code interpreter. Toolformer [162] integrates a
Social
rangeoftools,includingcalculators,tosignificantlyimprove
the performance of models in tasks such as mathematical Benefits E A n u h t a o n m ce a m ti e o n n t T an J r d a o n b W s f C o o r r r e k m a f t a o i t o r i c n o e n I D n i E s f t n o r h r i m a b n u a c t t e i i o o n n Ethical Concerns Dis B cr ia im s i a n n a d tion Accountability Impact
calculationswithoutcompromisingthemodel’sgenerality.
ART [163] enables LLM to invoke external tools, such Fig. 4: An overview of real-world issues in LLM agent
as calculators, when solving complex tasks and excels in systems,organizedintothreedomains:securitychallenges
mathematicalreasoningandcomplexcomputationaltasks. (including agent-centric and data-centric threats), privacy
concerns(coveringmemorizationvulnerabilitiesandintellec-
APIInteractions.BuildingonexternalAPIs,suchasREST
tualpropertyexploitation),andsocialimpactconsiderations
APT, can enable LLM agents to call external services and
(highlightingbothbenefitsandethicalchallenges).
extendtheirfunctionality,suchasmanipulatingdatabases
and implementing end-to-end automated processes. Rest-
buildingLLMapplicationsthatishighlyextensibleandal-
GPT [164] explores more realistic scenarios by combining
lowsuserstocreatecustommodulesandworkflowstomeet
LLM with RESTful APIs and presents RestBench to evalu-
theirspecificneeds.LlamaIndex[171]isadataframework
atetheperformanceofRestGPT.GraphQLRestBench[165]
serving large model applications, allowing users to build
buildsadatasetconsistingofsequencesofnaturallanguage
LLM applications based on local data. It also provides a
statements,andfunctioncallstoreviewexistingopen-source
richtoolboxforaccessingandindexingdata,retrievingand
LLMs,exploringthecapabilitiesofLLMsforAPIcalls.
reordering,andbuildingcustomqueryengines.Dify[172]is
anopen-sourceLLMapplicationdevelopmentplatformthat
3.2.2 ToolscreatedbyLLMagents
differsfromotherplatformsinthatitallowsuserstobuild
Since the users of traditional tools tend to be humans, andtestpowerfulAIworkflowsoncanvas.
LLM agents often have limitations when making calls. In Operationand Maintenance.AfterdeployingLLMagents,
addition, the limitations of existing tools make it difficult the O&M tool ensures that the model performs well dur-
to effectively handle new problems. In recent years, many ing training and remains reliable during production. Ol-
studies have explored how LLM agents can create their lama[173]isaplatformforbuildingLLMagentsthatalso
tools.CRAFRT[166]providesaflexibleframeworkfortool offersobservabilityandmonitoringsupport,allowingteams
creation and retrieval by collecting GPT-4 code solutions to track their models’ performance in real-time. Dify [172]
for specific tasks and abstracting them into code snippets enablesuserstomonitorandanalyzeapplicationlogsand
to create specialized tool sets for the tasks. Toolink [167] performance over time, allowing for continuous improve-
performs task resolution by creating a toolset and then mentsinprompts,datasets,andmodelsbasedonproduction
integratingtheplanningandinvocationoftoolsthrougha dataandannotations.
ChainofSolutions(CoS)approach.CREATOR[168]proposes
Model Context Protocol. MCP3 is an open protocol that
afour-phaseframework–Creation,Decision,Execution,and
standardizes how applications provide context to LLMs.
Reflection–toenableLLMagentstocreatetoolsandimprove
It is used to create secure links between LLMs and data
the robustness of the output. LATM [169] proposes a two-
sourcesaswellastobuildLLMagentsandworkflows.MCP-
stage framework that allows LLMs to act as tool makers
Agent [174] is a simple framework to build agents using
and tool users, respectively and proposes a tool caching
MCP. As more services become MCP-aware, users will be
mechanismthatimprovestheefficiencyoftasksolvingand
abletotakefulladvantageofthem.
reducesthecostwhilemaintainingperformancebyassigning
different models to different tasks with different levels of
difficulty. 4 REAL-WORLD ISSUES
AsLLMagentsbecomeincreasinglyintegratedintovarious
3.2.3 ToolsfordeployingLLMagents
aspects of society, they bring forth significant real-world
LLM tools are essential for the deployment, development,
challenges that must be addressed for responsible deploy-
operation,andmaintenanceofLLMagentsandforthesecure
ment. Figure 4 provides an overview of these challenges,
transmissionofdata.Accordingtotheirrole,thesetoolscan
categorized into three primary domains: security, privacy,
becategorizedintothreetypes.
andsocialimpact.Securityconcernsencompassbothagent-
Productionization. The main purpose of the production- centricthreats(Section4.1)thattargetmodelcomponentsand
ization tools is to make it easy for users to deploy LLM data-centricthreats(Section4.2)thatcontaminateinputdata.
agents in production environments. AutoGen [26] is an Privacyissues(Section4.3)includememorizationvulnerabil-
open-source framework that enables developers to build itiesandintellectualpropertyexploitation.Beyondtechnical
LLMapplicationswithcustomizable,conversationalmultiple
agents. LangChain [170] is an open-source framework for 3.https://modelcontextprotocol.io/introduction

11
concerns,LLMagentsraiseimportantethicalconsiderations mutationagentandaselectionagent,enhancedbyin-context
andhavebroadsocietalimplications(Section4.4),including learningandchain-of-thoughttechniques.RLbreaker[186]
bothpotentialbenefitsandriskstosociety.Understanding isablack-boxjailbreakingattackusingdeepreinforcement
thesechallengesiscrucialfordevelopingrobust,trustworthy learningtomodeljailbreakingasasearchproblem,featuring
agentsystems. a customized reward function and PPO algorithm. Path-
Seeker [187] also uses multi-agent reinforcement learning
toguidesmallermodelsinmodifyinginputsbasedonthe
4.1 Agent-centricSecurity
targetLLM’sfeedback,witharewardmechanismleveraging
Agent-centric security targets defending different types
vocabulary richness to weaken security constraints. For
of attacks on the agent models, where attacks aim to
jailbreakingdefensemethods,AutoDefense[188]proposesa
manipulate, tamper, and steal critical components of the
multi-agentdefenseframeworkthatusesLLMagentswith
weights, architecture, and inference process of the agent
specializedrolestocollaborativelyfilterharmfulresponses,
models. These agent-centric attacks may lead to perfor-
effectivelyresistingjailbreakattacks.Guardians[189]uses
mancedegradation,maliciouslymanipulatedoutputs,and
three examination methods—reverse Turing Tests, multi-
privacy leaks within agent systems. Li et al. [175] analyze
agent simulations, and tool-mediated adversarial scenar-
the security vulnerabilities of LLM agents under attacks
ios—todetectrogueagentsandcounterjailbreakingattacks.
categorized by threat actors, objectives, entry points, and
ShieldLearner[190]proposesanoveldefenseparadigmfor
so on. They also conduct experiments on certain popular
jailbreakattacksbyautonomouslylearningattackpatterns
agentstodemonstratetheirsecurityvulnerabilities.Agent
andsynthesizingdefenseheuristicsthroughtrialanderror.
securitybench[176]introducesacomprehensiveframework
to evaluate attacks and defenses for LLM-based agents 4.1.3 BackdoorAttacksandDefense
across10scenarios,10agents,400+tools,23attack/defense
Backdoor attacks implant specific triggers to cause the
methods,and8metrics,revealingsignificantvulnerabilities
model to produce preset errors when encountering these
and limited defense effectiveness of current LLM agents.
triggers while performing normally under normal inputs.
Wesummarizetheagent-centricsecurityissuesintheblow
Forbackdoorattackmethods,DemonAgent[191]proposesa
categories.
dynamicallyencryptedmuti-backdoorimplantationattack
methodbyusingdynamicencryptiontomapanddecompose
4.1.1 AdversarialAttacksandDefense
backdoors into multiple fragments to avoid safety audits.
Adversarialattacksaimtocompromisethereliabilityofthe Yang et al. [192] investigate and implement diverse forms
agents, rendering them ineffective in specific tasks. Mo et of backdoor attacks on LLM-based agents, demonstrat-
al.[177]categorizeadversarialattacksintothreecomponents, ing their vulnerability through experiments on tasks like
i.e.,Perception,Brain,andAction.AgentDojo[178]providesan webshoppingandtoolutilization.BadAgent[193]attacks
evaluationframeworkdesignedtomeasuretheadversarial LLM-basedintelligentagentstotriggerharmfuloperations
robustnessofAIagentsbytestingthemon97realistictasks throughspecificinputsorenvironmentcuesasbackdoors.
and629securitytestcases.ARE[179]evaluatesmultimodal BadJudge[194]introducesabackdoorthreatspecifictothe
agentrobustnessunderadversarialattacks.Foradversarial LLM-as-a-judgeagentsystem,whereadversariesmanipulate
attackmethods,CheatAgent[180]usesanLLM-basedagent evaluatormodelstoinflatescoresformaliciouscandidates,
toattackblack-boxLLM-empoweredrecommendersystems demonstratingsignificantscoreinflationacrossvariousdata
byidentifyingoptimalinsertionpositions,generatingadver- accesslevels.DarkMind[195]isalatentbackdoorattackthat
sarial perturbations, and refining attacks through iterative exploitsthereasoningprocessesofcustomizedLLMagents
prompttuningandfeedback.GIGA[181]introducesgener- by covertly altering outcomes during the reasoning chain
alizableinfectiousgradientattackstopropagateadversarial withoutrequiringtriggerinjectioninuserinputs.
inputs across multi-agent, multi-round LLM-powered sys-
temsbyfindingself-propagatinginputsthatgeneralizewell 4.1.4 ModelCollaborationAttacksandDefense
across contexts. For adversarial attacks defense methods, Model collaboration attack is an emerging type of attack
LLAMOS [182] introduces a defense technique for adver- thatmainlytargetsscenarioswheremultiplemodelswork
sarial attacks by purifying adversarial inputs using agent together. In this type of attack, attackers manipulate the
instructionanddefenseguidancebeforetheyareinputinto interactionorcollaborationmechanismsbetweenmultiple
theLLM.Chernetal.[183]introduceamulti-agentdebate modelstodisrupttheoverallfunctionalityofthesystem.For
methodtoreducethesusceptibilityofagentstoadversarial modelcollaborationattackmethods,CORBA[196]introduces
attacks. anovelyetsimpleattackmethodfortheLLMmulti-agent
system.Itexploitscontagionandrecursion,whicharehard
4.1.2 JailbreakingAttacksandDefense to mitigate via alignment, disrupting agent interactions.
Jailbreakingattacksattempttobreakthroughtheprotection AiTM[197]introducesanattackmethodtotheLLMmulti-
of the model and obtain unauthorized functionality or agentsystembyinterceptingandmanipulatinginter-agent
information. For jailbreaking attack methods, RLTA [184] messagesusinganadversarialagentwithareflectionmech-
usesreinforcementlearningtoautomaticallygenerateattacks anism. For the defense methods, Netsafe [198] identifies
that produce malicious prompts, triggering LLM agents’ criticalsafetyphenomenaandtopologicalpropertiesthatin-
jailbreakingtoproducespecificoutput.Thesecanbeadapted fluencethesafetyofmulti-agentnetworksagainstadversarial
to both white box and black box scenarios. Atlas [185] attacks.G-Safeguard[199]isalsobasedontopologyguidance
jailbreaks text-to-image models with safety filters using a and leverages graph neural networks to detect anomalies

12
TABLE3:Summaryofagent-centricattacksanddefensein
everystepofinformationflowandagentprocess,including
LLMagents.
functioncallsandtoolexecution,tomakesuretheexecution
aligns with the original instructions and intentions. In the
Reference Description
ASB [176] benchmark, a sandwich defend strategy adds
AdversarialAttacksandDefense
additionalguardinginstructionstohelpLLMagentsignore
Moetal.[177] Attack:Adversarialattackbenchmark
AgentDojo[178] Attack:Adversarialattackframework maliciousinjections.
ARE[179] Attack:Adversarialattackevaluationformultimodalagents
GIGA[181] Attack:Generalizableinfectiousgradientattacks DarkPsychologicalGuidance.Attackerscancarryoutdark
CheatAgent[180] Attack:Adversarialattackagentforrecommendersystems
LLAMOS[182] Defense:Purifyingadversarialattackinput psychologicalguidanceintheprompts,e.g.,use“cheating”
Chernetal.[183] Defense:Defenseviamulti-agentdebate insteadof“care”,“betrayal”insteadof“fairness”,“subver-
JailbreakingAttacksandDefense
sion”insteadof“authority”.ThenLLMagentsareguided
RLTA[184] Attack:Producejailbreakingpromptsviareinforcementlearning
Atlas[185] Attack:Jailbreakstext-to-imagemodelswithsafetyfilters to be aggressive and antisocial, which may cause serious
RLbreaker[186] Attack:Modeljailbreakingasasearchproblem socialimpacts.[210]proposesthe“EvilGeniuses”togenerate
PathSeeker[187] Attack:Usemulti-agentreinforcementlearningtojailbreak
AutoDefense[188] Defense:Multi-agentdefensetofilterharmfulresponses prompts to put agents into specific role-playing states. Its
Guardians[189] Defense:Detectrogueagentstocounterjailbreakingattacks.
ShieldLearner[190] Defense:Learnattackjailbreakingpatterns. promptsareoptimizedthroughthered-blueexercises.[201]
BackdoorAttacksandDefense injects the dark psychological traits into the user inputs.
DemonAgent[191] Attack:Encryptedmuti-backdoorimplantationattack Todefensedarkpsychologicalinjections,doctorandpolice
Yangetal.[192] Attack:BackdoorattacksevaluationsonLLM-basedagents
BadAgent[193] Attack:Inputsorenvironmentcuesasbackdoors agents[201]areincorporatedintotheagentssystems.The
BadJudge[194] Attack:BackdoortotheLLM-as-a-judgeagentsystem doctoragentsconductthepsychologicalassessment,while
DarkMind[195] Attack:latentbackdoorattacktocustomizedLLMagents
thepoliceagentssupervisethesafetyofagentsystems.They
AgentCollaborationAttacksandDefense
CORBA[196] Attack:Multi-agentattackviamulti-agent worktogethertoguardthehealthypsychologyatanytime.
AiTM[197] Attack:Intercepteandmanipulateinter-agentmessages
Netsafe[198] Defense:Identifycriticalsafetyphenomenainmulti-agentnetworks External Source Poisoning. Many attackers pay their at-
G-Safeguard[199] Defense:leveragesgraphneuralnetworkstodetectanomalies tention to the RAG-based LLM agents, as they have been
Trustagent[200] Defense:Agentconstitutionintaskplanning.
PsySafe[201] Defense:Mitigatesafetyrisksviaagentpsychology proven to be more reliable than general memory-based
LLM agents [211]. The attackers inject poisoning samples
into the knowledge databases [175], [212]. Based on this,
in the LLM multi-agent system. Trustagent [200] aims to
theIndirectPromptInjection(IPI)attackembedsmalicious
enhancetheplanningsafetyofLLMagenticframeworkin
instructions into other external knowledge sources [213],
threedifferentplanningstages.PsySafe[201]isgroundedin
suchasthewebsites,supportliterature,emails,onlineBBS,
agentpsychologytoidentify,evaluate,andmitigatesafety
which can manipulate agents and cause them to deviate
risksinmulti-agentsystemsbyanalyzingdarkpersonality
fromtheoriginalintentions.WIPI[214]controlstheagents
traits, assessing psychological and behavioral safety, and
throughapublicwebpagetoindirectlypoisoninstructions.
devisingriskmitigationstrategies.
[215] describes a Foot-in-the-Door (FITD) attack, which
beginswithinconspicuous,unrelatedrequestsandgradually
4.2 Data-centricSecurity incorporates harmless ones. This approach increases the
likelihoodoftheagentexecutingsubsequentactions,leading
Thegoalofdata-centricattacksistocontaminatetheinput
to resource consumption that could have been avoided.
dataofLLMagents,ultimatelyleadingtounreasonabletool
AgentPoison [216] is a typical red teaming work, which
calling,aggressiveoutputsandresourcedepletion,etc[202].
achieves a high success rate in knowledge-intensive QA
In data-centric attacks, any components in LLM agent
agent.[183]employsamulti-agentdebatefordefense,where
systemsordefaultparametersarenotallowedtobemodified.
eachagentactsasadomainexperttoverifythefacticityof
Basedonthedatatype,wecategorizeattacksintoexternal
externalknowledge.
data attacks and execution data attacks. Corresponding
defense strategies are summarized to counter these agent
4.2.2 InteractionAttackandDefense
attacks.
Interaction between user and agent interface. Some LLM
4.2.1 ExternalDataAttackandDefense agents store the private user-agent interactions in users’
UserInputFalsifying.Modifyingtheuserinputisthemost computermemorytoenhancedialogueperformance.During
straightforwardandwidelyuseddata-centricattacks.These these interactions, LLM agents are usually black-box to
injections [176] can lead to uncontrolled and dangerous attackers. [217] is a private memory extraction attack that
outputs.Thoughitissimple,italwaysachievesthehighest aggregates multiple levels of knowledge from the stored
AttackSuccessRate(ASR)[176],[203].Lietal.[204]propose memory.[218]presentsanattackthatoccursattheinterface
malicious prefix prompts, such as “ignore the document”. betweenusersandLLMagents,whereitsolicitsinformation
InjectAgent [205] and Agentdojo [203] are two prompt fromusers.
injectionbenchmarks,whichtestthesingleandmulti-turn InteractionamongLLMagents.Inmulti-agentLLMsystems,
attacksinLLMagents.Asthewidespreadeffectofinjections theinteractionsamongagentsarefrequentandessential[12].
on user inputs increases, various defense models have Attackers poison a single agent, which then infects other
beendesigned.Mantis[206]defensesthroughhackingback agents [219]. This recursive attack can ultimately deplete
to attackers’ own systems. [207] offers a defense module the computational resources. AgentSmith [220] concludes
called the Input Firewall, which extracts key points from that the infectious spread occurs exponentially fast. The
users’naturallanguageandconvertsthemintoastructured Contagious Recursive Blocking Attack (CORBA) [196] is
JSONformat.RTBAS[208]andTaskShield[209]checkthe designed to disrupt the communications among agents,

13
TABLE 4: Summary of data-centric attack and defense in
tionally,itdiscussespotentialcountermeasurestomitigate
LLMagents.
theserisks.
Reference Description
ExternalDataAttacksandSecurity
4.3.1 LLMMemorizationVulnerabilities
Lietal.[204] Attack:Maliciousprefixinjection
Psysafe[201] Attack:Adarkpsychologicalinjectionbenchmark
Tianetal.[210] Attack:Guideagentsintospecificrole-playingstates IthasbeenshownthatLLMsareabletogeneratetextsimilar
InjectAgent[205] Attack:Apromptinginjectionbenchmark
Agentdojo[203] Attack:Auserinjectionbenchmark tohumans.However,suchgeneratedtextmayberetained
AgentPoison[216] Attack:Poisoningsamplesinknowledgedatabases trainingdata,whichposesseriousprivacyprotectionissues.
Nakashetal.[215] Attack:IndirectpromptinjectionthroughFITDattack
WIPI[214] Attack:controlagentsthroughapublicwebpage These risks are particularly severe in multi-agent systems,
ASB[176] Attack:Amulti-typeattackbenchmark
AgentHarm[223] Attack:Amulti-typeattackbenchmark whereLLMsmayleaksensitiveinformationwhencollaborat-
Mantis[206] Defense:Hackingbacktoattackers
Chernetal.[183] Defense:Employmulti-agentdebatetoverifyexternalknowledge ingtosolvecomplextasks.Thissectionexplorestheprivacy
RTBAS[208] Defense:Checkeverystepofagentinformationflow threats posed by LLM memory and discusses protection
TaskShield[209] Defense:Checkeverystepofagentprocess
Zhangetal.[201] Defense:Doctorandpoliceagentsguardthehealthypsychology measuresagainstthesethreats.
InteractionAttacksandSecurity
DataExtractionAttacks.Theyexploitthememorycapacity
Wangetal.[217] Attack:Privatememoryextractionattack
CORBA[196] Attack:Disruptthecommunicationsamongagents of LLMs to extract sensitive information from training
AgentSmith[220] Attack:Poisononeagenttoinfectiousotheragents
Leeetal.[221] Attack:Conductinjectionstoself-replicateamongagents data. Carlini et al. [224] show that an attacker can extract
Heetal.[197] Attack:Injectsemanticdisruptionstoagentcommunications personallyidentifiableinformation(PII)suchasname,email,
BlockAgents[222] Defense:IncorporateblockchainandPoTagainstbyzantineattacks
Abdelnabietal.[207] Defense:Amulti-layeragentfirewall and phone number from a GPT-2 model through specific
queries.Theriskofdataextractionincreaseswithmodelsize,
frequencyofrepeateddata,andcontextlength[225].Huang
allowingtheinfectiontopropagateacrosstheentirecommu- etal.[226]furtherstudydataextractionattacksagainstpre-
nicationnetwork.[197]incorporatesareflectionmechanism trainedLLMssuchasGPT-neo,highlightingthefeasibility
to finish disruptions based on the semantic understand- ofsuchattacksinpracticalapplications.
ingofcommunications.[221]injectsmaliciousinstructions
Member Inference Attacks. Their purpose is to determine
into one agent, enabling them to self-replicate across the
whetheraparticulardatasamplehasbeenpartoftheLLM
agentnetwork,resemblingthespreadofacomputervirus.
trainingdata.Mireshghallahetal.[227]empiricallyanalyze
Additionally, [221] develops a tagging strategy to control
thevulnerabilityoffine-tunedLLMstomembershipinfer-
the infection spread. To defend against Byzantine attacks
enceattacksandfindthatfine-tuningthemodelheadmakes
duringtheagentinteractions,BlockAgents[222]introduces
itmorevulnerabletosuchattacks.Fuetal.[228]proposea
a consensus mechanism based on blockchain and proof-
self-calibratedmembershipinferenceattackmethodbased
of-thought(PoT)techniques.Theagentthatcontributesthe
on probability changes, which provides a more reliable
mosttotheplanningprocessisgrantedtheaccountingrights.
membership signal through these variations. This type of
Interaction between agents and tools. To call appropri-
attackisparticularlydangerousinmulti-agentsystems,as
ate tools, the agents first make a plan, and then finish
the training data may originate from multiple sources of
the action. The interaction between agents and tools is
sensitiveinformation.Inresponsetotheserisks,protection
vulnerable. Some attackers maliciously modify planning
strategiessuchasdifferentialprivacy(DP)andknowledge
thoughts, and thus alter the agent actions. The agent may
distillationhavebeendeveloped[229],[230].
callunconvincingorharmfultoolstocompletethetask,and
AttributeInferenceAttacks.Thegoalofattributeinference
furthercauseunexpectedconsequences.AgentHarm[223]
attacks is to infer a certain feature or characteristic of a
addsharmfuldistractionsduringmulti-stepexecutiontasks.
datasampleusingtrainingdata.Toconfirmtheexistenceof
InjectAgent[205]conductsattacksduringtheagentplanning
sensitiveattributeinferenceinLLMs,Panetal.[231]conduct
process.Themulti-layeragentfirewall[207]incorporatesa
an in-depth study of privacy issues related to attribute
self-correctionmechanism,knownasthetrajectoryfirewall
inferenceattacksinLLMs.Wangetal.[232]studyattribute
layer,tocorrectthedeviatedtrajectoryofagents.Thisfirewall
existence inference attacks on generative models and find
layerverifiesthegeneratedresponsestoensurecompliance
thatmostgenerativemodelsarevulnerabletosuchattacks.
withsecurityrules.
ProtectiveMeasures.Severalprotectivestrategieshavebeen
proposedtoreducethechanceofLLMmemorization.Data
4.3 Privacy
cleaningstrategiescansuccessfullyreducetheriskofmem-
The widespread use of LLMs in multi-agent systems has orizationbylocatingandeliminatingsensitiveinformation
alsoraisedseveralprivacyconcerns.Theseissuesaremainly in training data [233]. Another effective way to minimize
causedbythememorycapacityofLLMs,whichmaylead privacy leakage is to introduce differential privacy noise
totheleakageofprivateinformationduringconversations into model gradients and training data [229] during pre-
orwhencompletingtasks.Inaddition,LLMagentsarevul- trainingandfine-tuning.Knowledgedistillationtechniques
nerabletoattacksinvolvingmodelandprompttheft,along have become an intuitive means of privacy protection by
withotherformsofintellectualpropertytheft.Thissection transferring knowledge from private teacher models to
explorestheprivacythreatsposedbyLLM Memorization public student models [230]. In addition, privacy leakage
VulnerabilitiesandLLMIntellectualPropertyExploitation detectiontoolssuchasProPILEcanhelpserviceproviders
emphasizingtheimportanceofensuringthesafeandsecure assesstheextentoftheirPIIleakagebeforedeployingLLM
deploymentofLLMsincollaborativeenvironments.Addi- agents[234].

14
TABLE5:Summaryofprivacythreatsandcountermeasures 4.4 SocialImpactandEthicalConcerns
inLLMagents.
LLMagentsprofoundlyimpactsociety,drivingautomation,
Reference Description industrial innovation, and productivity gains. However,
LMMemorizationVulnerabilities ethicalconcernsremain.Thefollowingsectionexploresboth
Carlinietal.[224] Attack:DataExtraction the benefits and challenges associated with their use. We
Huangetal.[226] Attack:DataExtractiononPretrainedLLMs
summarizethecontentinTable6.
Mireshghallahetal.[227] Attack:MembershipInferenceonFine-TunedLLMs
Fuetal.[228] Attack:Self-CalibratedMembershipInference
Panetal.[231] Attack:AttributeInferenceinGeneral-PurposeLLMs
Wangetal.[232] Attack:PropertyExistenceInferenceinGenerativeModels 4.4.1 BenefitstoSociaty
Kandpaletal.[233] Defense:DataSanitizationtoMitigateMemorization
Hooryetal.[229] Defense:DifferentialPrivacyforPre-TrainedLLMs LLM agents have significantly impacted human society,
Kangetal.[230] Defense:KnowledgeDistillationforPrivacyPreservation
Kimetal.[234] Defense:PrivacyLeakageAssessmentTool offeringnumerousbenefitsacrossvariousdomains.
LMIntellectualPropertyExploitation AutomationEnhancement.LLMagentshavefoundapplica-
Krishnaetal.[235] Attack:ModelStealingviaQueryAPIs tionsacrossdiversefields,includinghealthcare,biomedicine,
Nasehetal.[236] Attack:StealingDecodingAlgorithmsofLLMs
Lietal.[237] Attack:ExtractingSpecializedCodeAbilitiesfromLLMs law,andeducation[243].Byautomatinglabor-intensivetasks,
Shenetal.[240] Attack:PromptStealinginText-to-ImageModels
Shaetal.[241] Attack:PromptStealinginLLMs they reduce time costs and enhance efficacy. In healthcare,
Huietal.[242] Attack:Closed-BoxPromptExtraction for example, they assist in interpreting clinical symptoms,
Kirchenbaueretal.[238] Defense:ModelWatermarkingforIPProtection
Linetal.[239] Defense:BlockchainforIPVerification explaininglabresults,andevendraftingmedicaldocumen-
tation. In legal and educational settings, they streamline
administrative work, generate summaries, and provide
4.3.2 LMIntellectualPropertyExploitation instant,context-awareresponses[243]–[245].Theirabilityto
alleviaterepetitiveworkloadsallowsprofessionalstofocus
LLM agents are subject to memory concerns as well as on more complex, high-stake tasks, ultimately improving
privacyrisksassociatedwithintellectualproperty(IP),such productivityandaccessibilityacrossindustries.
as model theft and prompt theft. These attacks put both Job Creation and Workforce Transformation. While re-
individuals and organizations at serious danger by taking searchers acknowledge the potential for AI agents to re-
advantageoftheLLMs’seconomicvalueandsignaling. place human jobs and disrupt the job market [243], others
Model Stealing Attacks. Model theft attacks attempt to argue that their advancements will reshape workforce de-
extractmodelinformation(suchasparametersorhyperpa- mands[246].TheriseofLLMagentsistransformingthejob
rameters)byqueryingthemodelandobservingitsresponses. market,notonlyexpandingtechnicalrolessuchasmachine
Krishnaetal.[235]showthatanattackercanstealinforma- learning engineers and data scientists but also driving
tionfromlanguagemodelssuchasBERTthroughmultiple demandformanagerialpositionslikeAIprojectmanagers
querieswithoutaccessingtheoriginaltrainingdata.Naseh and business strategists. Given their growing economic
et al. [236] demonstrate that attackers can steal the types impact,governmentsareencouragedtosupportAI-focused
andhyperparametersofLLMdecodingalgorithmsatalow training programs to equip individuals for this evolving
cost. Li et al. [237] investigate the feasibility of extracting landscape. Unlike LLMs, which often require specialized
specializedcodefromLLMs,highlightingtheriskofmodel expertise to use effectively, LLM agents are designed for
theft in multi-agent systems. In response to these attacks, accessibility, attracting a broader user base and enabling
protective measures such as model watermarking [238] wider applications across various industries. As a result,
and blockchain-based IP authentication [239] have been their societal impact is expected to surpass that of LLMs
proposed. or other AI models alone, bringing both challenges and
unprecedentedopportunities.
Prompt Stealing Attacks. Prompt theft attacks involve
Enhance Information Distribution. Businesses reliant on
inferring original hints from generated content that may
large-scaletextgeneration,suchasonlineadvertising,benefit
have significant business value. Shen et al. [240] conduct
significantlyfromLLMagents.However,theirmisuseisa
the first study of prompt stealer attacks against text-to-
growingconcern,particularlyregardingtheproliferationof
image generation models and propose an effective attack
fakenewsandmisinformation[244],[245].Beyondacceler-
method called PromptStealer. Sha et al. [241] extend this
atingadvertisementdistribution,enhancedinformationdis-
studytoLLMs,usingaparameterextractortodeterminethe
seminationoffersbroadersocietalbenefits.Forinstance,the
properties of the original prompt. Hui et al. [242] propose
globalshortageofpatient,experienced,andknowledgeable
PLEAK, a closed-box prompt extraction framework that
teachers has long been a challenge. LLM agents introduce
extractssystempromptsforLLMapplicationsbyoptimizing
transformativesolutions,suchasintelligentonlinetutoring
adversarial queries. To prevent prompt theft, adversarial
systems,revolutionizingeducationaccessibility[247].
samples have been proposed as an effective method to
obstruct attackers from inferring the original prompt by
introducingdisturbancetothegeneratedcontent[240]. 4.4.2 EthicalConcerns
TheprivacychallengesforLLMagentsaremultifaceted, Although LLM agents bring numerous benefits to society,
rangingfrommemorythreatstorisksrelatedtointellectual they also pose potential risks that cannot be overlooked.
property.AsLLMscontinuetoevolve,robustprivacypro- These challenges raise significant ethical concerns, includ-
tection technologies must be developed to mitigate these ing bias in decision-making, misinformation propagation,
privacyriskswhileensuringthatLLMsplayaneffectiverole and privacy issues, highlighting the need for responsible
inmulti-agentsystems. developmentandregulation.

15
TABLE6:OverviewofSocialImpactsandEthicalConsidera-
BiasandDiscrimination.LLMagentsinherentlyinheritbi-
tionsinLLMAgents.
asespresentintheirtrainingdatasetsandmayevenamplify
themduringthelearningprocess,leadingtoskewedoutputs
Impact Reference
andreinforcingexistingstereotypes[248].Recognizingthis
BenefitstoSociety
issue,manyexistingworkshaveimplementedstrategiesto AutomationEnhancement FoundationModels[243],GPT-3[244],LLaMA[245]
WorkforceTransformation FoundationModels[243],RedefiningWork[246]
mitigateharmfulcontentgeneration.Thesemethodsinclude EnhanceInformationDistribution GPT-3[244],LLaMa[245],EmpowerOnlineEducation[247]
EthicalConcerns
filtering sensitive topics, applying reinforcement learning
BiasandDiscrimination FairUse[249],FairLearning[250]
withhumanfeedback,andrefiningmodeltrainingprocesses Accountability StochasticParrots[252],Governance[253],[254]
Copyright FairLearning[250],EthicsofLLMs[255],AIcollapse[256]
topromotefairnessandreducebias[243]–[245].Thepursuit DataPrivacy FoundationModels[243],EthicalandSocialRisks[257]
Manipulation&Misinformation Data-PoisoningAttacks[259]
of fairness has become a critical focus in studies on LLM Others Overreliance[244],Alignment[261],CarbonFootprint[262],Expenses[263]
agents,asresearchersstrivetodevelopmodelsthatminimize
bias,promoteinclusivity,andensureethicalAIdeployment
surveysthebroadspectrumofLLMagentapplications,from
inreal-worldapplications[249],[250].
accelerating scientific discovery (Section 5.1) to enhancing
Accountability.Despiteeffortstomitigatetoxiccontentin interactivegamingexperiences(Section5.2),modelingcom-
LLMagents,theriskofharmfuloutputspersists[244],[245], plex social phenomena (Section 5.3), and boosting produc-
[251].Accountabilityremainsakeychallenge,asdocumented tivity(Section5.4).Theseapplicationsdemonstratehowthe
datasets provide limited oversight, while vast amounts of integrationofLLM-basedagentsystemsenablesenhanced
undocumented data can be easily integrated into training. problem-solvingcapabilitiesthroughspecializedknowledge
Rigorous dataset documentation is essential, despite its application,multi-agentcollaboration,andhuman-AIinter-
costs [252]. Additionally, proper governance frameworks actionparadigms.
arenecessarytoensureaccountabilityinLLMagents[253],
[254].
5.1 ScientificDiscovery
Copyright.Copyrightconcernsarecloselylinkedtoprivacy
ByleveragingmultiplespecializedLLMagentsthatcommu-
and accountability. Some argue that AI should adhere to
nicate and coordinate, LLM-based multi-agent AI systems
the same legal and ethical standards as humans, ensuring
can combine diverse expertise, access external tools, and
fair use and intellectual property protection [250]. Many
decompose tasks, thereby extending the capabilities of
creatorsopposetheirworkbeingusedtotrainmodelsthat
single LLMs [264], [265]. In this part, we survey advances
could replace them, yet the absence of clear regulations
in applying LLM-driven multi-agent systems to scientific
and the growing demand for data lead to widespread
researchoverthepastthreeyears.
misuse[255].Thisissueisoftenunderestimatedandrequires
urgentattention,asitthreatenshumancreators,increasesthe
5.1.1 AgenticAIAcrossScientificDisciplines
prevalenceofAI-generatedcontentoverhuman-produced
LLM-based multi-agent systems are increasingly applied
work in certain domains, and risks content degradation,
acrossscientificdisciplinestoemulatehumancollaborative
particularlywhenlargeAImodelsareincreasinglytrained
workflowsandtacklecomplex,interdisciplinaryproblems
on AI-generated data [256]. Addressing these issues is
thatrequirediverseknowledgeandskills.Forexample,the
particularly crucial in the use of LLM agents, where users
SciAgents[266]frameworkusesdistinctLLMagentssuchas
oftenlackdirectawarenessofthetrainingdatasources.This
“Ontologist,”“Scientist,”and“Critic”tocollectivelygenerate
opacity increases the risk of unintended consequences, as
and refine scientific hypotheses. Centered on an ontolog-
individuals may unknowingly rely on models trained on
ical knowledge graph that encodes relationships between
controversialdatasets,potentiallyresultinginreputational
scientificconcepts,SciAgentsorchestratesChatGPT-4-based
harmorevenlegalrepercussions.
agents to generate novel research ideas and experimental
Others.SomeethicalconcernsintheuseofLLMagents,such
plans.Inacasestudyonbio-inspiredmaterials,oneagent
asprivacy[243],[257],[258],datamanipulation[259],and
generatedaproposaltointegratesilkwithnovelpigments;
misinformation[244],[260],aresocriticalthatweprovidea
anotheragentsuggestedsimulationexperimentstotestthe
thoroughdiscussioninSections4.1,4.2and4.3.Beyondthese,
idea,andacriticalagentidentifiedweaknessesandprompted
additionalethicalconcernsremain.Onemajorissueisthat
improvements.Beyondhypothesisgeneration,LLM-based
LLMagentslacktruesemanticandcontextualunderstanding,
agents are being used to plan and execute experimental
relyingpurelyonstatisticalwordassociations.Thislimitation
research. For instance, Curie [267] developed an AI agent
isoftenmisinterpretedandoverestimated,leadingtoundue
frameworkforrigorousautomatedexperimentation.InCurie,
relianceonthesemodels[244],especiallywhentheirbehavior
anArchitectagentfirstdesignshigh-levelexperimentalplans
maynotalignwellwithhumanintentions[261].Moreover,
to answer a scientific question, then multiple Technician
concernshavebeenraisedaboutthesignificantcarbonfoot-
agentscarryoutspecificexperimentalsteps.Intestsonques-
printofLLMagents,posingenvironmentalchallenges[262],
tionsderivedfromcomputerscienceresearchpapers,Curie’s
alongside the high computational costs associated with
structuredmulti-agentapproachimprovedthecorrectness
traininglargemodels[263].
ofexperimentalresults,outperformingmorestraightforward
prompt-basedautomationbyanotablemargin.Thisindicates
5 APPLICATIONS
thatmulti-agentsystemscanbringnotjustcreativitybutalso
TheversatilityofLLMagentshasledtotheiradoptionacross disciplineandreliability.Asidefromscientificfindings,LLMs
diverse domains, transforming how complex tasks are ap- arealsousedtoimprovethegenerationpipelineofacademic
proachedinbothresearchandindustrysettings.Thissection works. AgentReview [268] proposes an LLM-agent-based

16
frameworkforsimulatingacademicpeerreviewprocesses, 5.1.4 AgenticAIinScientificDatasetConstruction
offeringvaluableinsightstoimprovethedesignofevaluation
Multi-agent systems also accelerate the construction of
protocolsforacademicpapers.
scientific datasets. For instance, PathGen-1.6M [276] gen-
erated a massive pathology image dataset via multi-agent
collaboration, where multiple AI models played different
5.1.2 Agentic AI in Chemistry, Materials Science and As-
roles:onevisionmodelscannedwhole-slidehistologyimages
tronomy
toselectrepresentativeregions,another(anLLMormulti-
Duetotheabundanceofdigitaltoolsanddatainthesefields, modalmodel)generateddescriptivecaptionsforeachregion,
chemistry,materialsscience,andAstronomyhavebeenearly and additional agents iteratively refined the captions for
adoptersofLLM-basedagenticAI.Inthechemistrydomain, accuracy.KALIN[277]developedamulti-agentcollaborative
ChemCrow[269]exemplifiesanLLM-drivenchemistryagent frameworktogenerateahigh-qualitydomainLLMtraining
designed to foster scientific advancement by bridging the corpus.Specifically,twodistinctLLMsaretrainedtogenerate
gap between experimental and computational chemistry. scientificquestionswithinputchunkedresearcharticlesas
ChemCrow integrates an LLM with a suite of 18 expert- context. Then, KAILIN utilizes a knowledge hierarchy to
designed chemistry tools, such as molecule property pre- self-evaluatethealignmentofgeneratedquestionswiththe
dictors,reactionplannersanddatabases,enablingittoplan inputcontext,thenself-evolvingtomorein-depthquestions.
and execute chemical syntheses autonomously. Materials GeneSUM [278] is designed to maintain the gene function
science problems, which often span multiple scales and descriptionknowledgedatasetautomatically.Specifically,a
modalities(fromatomicsimulationstoempiricaldata),also singledescriptionagentservesasareaderforgeneontology,
benefitfrommulti-agentAI.AtomAgents[270]framework aretrievalagentfunctionsasareaderforrelatedliterature,
isaphysics-awaremulti-agentsystemforautomatingalloy andasummarizationagentactsasthegenerator.GeneSUM
design.Inthissystem,aPlanneragent(GPT-4)decomposesa thuscanautomaticallyreademerginggene-function-related
complexmaterialsdesignchallengeintoasequenceoftasks, research articles and renew the database of gene function
which are then verified by a Critic agent and delegated to descriptions. These approaches demonstrate a virtuous
specialist modules. Similar principles are being applied in cycle: AI systems can consume scientific data and create
physics and astronomy. For example, an AI copilot agent it,improvingthenextgenerationofmodels.
has been developed for the Cherenkov Telescope Array
in astronomy [271], using an instruction-tuned LLM to 5.1.5 AgenticAIinMedical
autonomouslymanagetelescopeconfigurationdatabasesand
Digitization of medical records [279], [280] brings great
evengeneratecodefordataanalysisworkflows.Although
potential in applying agentic AI in medical service. One
still experimental, these efforts indicate that LLM-based
lineofresearchhascreatedsimulatedclinicalenvironments
agentscouldsoonbeusedinphysicslabsandastronomical
in which autonomous doctors and patient agents interact.
observatories.Theycouldhandleroutinedecision-making
AgentHospital[281]isavirtualhospitalpopulatedbyLLM-
andfreehumanscientiststofocusonhigh-levelinsights.
driven doctors, nurses, and patient agents, modeling the
full cycle of care from triage to diagnosis to treatment. In
5.1.3 AgenticAIinBiology this system, each patient agent presents symptoms, and
doctoragentsmustconversewiththepatient,ordervirtual
The life sciences are likewise beginning to embrace LLM- tests,makeadiagnosis,andprescribetreatment.Inparallel,
based multi-agent systems for hypothesis generation and otherworkfocusesonaligningmulti-agentAIdirectlywith
data analysis [272]. One notable direction is using LLM clinicaldecisionsupportinrealscenarios.ClinicalLab[282]in-
agentstoproposebiologicalexperimentsorinterpretmulti- troduced a comprehensive benchmark and an agent for
omicsdata.BioDiscoveryAgent[273]proposedanAIagentto multi-departmentmedicaldiagnostics,whichinvolved150
designgeneticperturbationexperimentsinmolecularbiology. diseasesacross24medicalspecialties,reflectingthebreadth
Byparsingliteratureandgenedatabases,anLLMagentcan of knowledge required in hospital settings. Multi-agent
suggest which gene knockouts or edits might elucidate a systems can also enhance conversational applications by
certainbiologicalpathway.Anothersystem,GeneAgent[274], introducing roles and simulations. AIPatient [283] is a
usesaself-refinementlooptodiscovergeneassociationsfrom system that creates realistic patient simulators powered
biomedicaldatabases,improvingthereliabilityoffindings by LLMs. It leverages a structured knowledge graph of
by cross-checking against known gene sets. RiGPS [275] medical information as a source of ground truth about a
developedamulti-agentsystemwithanexperiment-based patient’s conditions, and a Reasoning RAG workflow that
self-verifiedreinforcementlearningframework,enhancing allows the patient agent to retrieve relevant details and
the biomarker identification task in the single-cell dataset. respond to a doctor’s questions in a convincing manner.
BioRAG[211]developedamulti-agent-basedRAGsystem Medicalimagingisanotherdomainripeformulti-agentAI
to handle biology-related QA, where several agents are integration. For instance, CXR-Agent [284] uses a vision-
designedtoretrieveinformationusingmultipletools,and language model together with an LLM to interpret chest
one agent is specifically used to self-evaluate the retrieval X-rays and generate radiology reports with uncertainty
results. These examples illustrate the methodology of self- estimates.MedRAX[285]integratesseveralspecializedtools,
questioningorself-verificationinmulti-agentAI:oneormore suchasanopticalcharacterreaderforreadingpriorreports,
agentsproposeascientificinsight,andanotherevaluatesits asegmentationmodelforhighlightingimageregions,and
plausibilitywithknownknowledge,therebyreducingerrors. an LLM for clinical reasoning, to solve complex chest

17
TABLE7:OverviewofApplicationsinLLMAgents.
evaluationandchessgameplay.GLAM[288]buildsanagent
in the BabyAI-text environment, where a policy is used to
Method Domain CoreIdea
selectthenextaction,withtrainingconductedthroughonline
ScientificDiscovery
reinforcementlearning.
SciAgents[266] GeneralSciences Collaborativehypothesisgeneration
Curie[267] GeneralSciences Automatedexperimentation Game Generation. In game generation, LLMs are used to
ChemCrow[269] Chemistry Tool-augmentedsynthesisplanning
AtomAgents[270] MaterialsScience Physics-awarealloydesign createdynamicandinteractivegamecontent.CALYPSO[289]
D.Kostuninelal[271] Astronomy Telescopeconfigurationmanagement
BioDiscoveryAgent[273] Biology Geneticperturbationdesign creates LLM agents as the assistants to help build a com-
GeneAgent[274] Biology Self-verifyinggeneassociationdiscovery pelling narrative to present in the context of playing Dun-
RiGPS[275] Biology Biomarkeridentification
BioRAG[211] Biology Biology-focusedretrievalaugmentation geons & Dragons. GameGPT [290] leverages dual-agent
PathGen-1.6M[276] MedicalDataset Pathologyimagedatasetgeneration
KALIN[277] BiologyDataset Scientificquestioncorpusgeneration collaboration and a hierarchical approach, using multiple
GeneSUM[278] BiologyDataset Genefunctionknowledgemaintenance internal dictionaries to automate and enhance the game
AgentHospital[281] Medical Virtualhospitalsimulation
ClinicalLab[282] Medical Multi-departmentdiagnostics development process. Sun et al. [291] create an interactive
AIPatient[283] Medical Patientsimulation
CXR-Agent[284] Medical ChestX-rayinterpretation storytellinggameexperiencein1001Nights,whereinstruc-
MedRAX[285] Medical Multimodalmedicalreasoning tivelanguagemodelsandimagegenerationarecombinedto
Gaming
shapethenarrativeandworld.
ReAct[33] GamePlaying Reasoningandactingintextenvironments
Voyager[35] GamePlaying LifelonglearninginMinecraft
ChessGPT[287] GamePlaying Chessgameplayevaluation
GLAM[288] GamePlaying Reinforcementlearningintextenvironments 5.3 SocialScience
CALYPSO[289] GameGeneration NarrativegenerationforD&D
GameGPT[290] GameGeneration Automatedgamedevelopment
Sunetal.[291] GameGeneration Interactivestorytellingexperience The application of LLM agents in social science has seen
SocialScience significantadvancements,providingnewopportunitiesfor
Econagent[292] Economy Economicdecisionsimulation understanding and simulating complex human behaviors
TradingGPT[293] Economy Financialtradingsimulation
CompeteAI[294] Economy Marketcompetitionmodeling andinteractions.Thesemodelsfacilitateinsightsintovari-
Maetal.[295] Psychology Mentalhealthsupportanalysis ous domains, including economics, psychology and social
Zhangetal.[296] Psychology Socialbehaviorsimulation
TE[297] Psychology Psychologicalexperimentsimulation simulation. Below, we explore how LLM agents are being
Generativeagents[30] SocialSimulation Humanbehavioremulation
Liuetal.[298] SocialSimulation Learningfromsocialinteractions appliedacrossthesethreecriticalareas.
S3[299] SocialSimulation Socialnetworkbehaviormodeling
Economy. In economics, LLM agents are utilized to ana-
ProductivityTools
lyzefinancialdataandsimulatefinancialactivities.Econa-
SDM[300] SoftwareDevelopment Self-collaborationforcodegeneration
ChatDev[301] SoftwareDevelopment Chat-powereddevelopmentframework gent[292]employspromptengineeringtocreateagentsthat
MetaGPT[27] SoftwareDevelopment Meta-programmingforcollaboration
Agent4Rec[302] RecommenderSystems Userbehaviormodeling mimichuman-likedecisionsormacroeconomicsimulations.
AgentCF[303] RecommenderSystems User-iteminteractionmodeling TradingGPT [293] presents a multi-agent framework for
MACRec[304] RecommenderSystems Multi-agentrecommendation
RecMind[305] RecommenderSystems Knowledge-enhancedrecommendation financial trading, which simulates human decision pro-
cessesbyincorporatinghierarchicalmemorystructuresand
debate mechanisms with individualized trading profiles.
X-ray cases that require referring to patient history and
CompeteAI[294]leveragesLLMagentstomodelavirtual
imaging simultaneously. Evaluations of these approaches
townwhererestaurantsandcustomersinteract,providing
on standard chest X-ray benchmarks [286] showed that it
insightsconsistentwithsociologicalandeconomictheories.
couldachievediagnosticaccuracyonparwithstate-of-the-art
Psychology. In psychological research, LLM agents are
standalonemodelswhilealsoprovidinganuncertaintyscore
utilized to model human behavior with diverse traits and
that correlates with its correctness. In summary, the multi-
cognitive processes. Ma et al. [295] investigate the psycho-
agent paradigm in medicine holds promise for improving
logical effects and potential benefits of using LLM-based
AIreliabilitybyintroducingredundancy,specialization,and
conversational agents for mental health support. Zhang
oversight.However,italsocomplicatesthesystem,requiring
et al. [296] examine how LLM agents with unique traits
rigorousvalidation.
and thought processes replicate human-like social behav-
iors,includingconformityandmajorityinfluence.TE[297]
5.2 Gaming
uses LLM agents to simulate psychological experiments,
ThedevelopmentofLLMagentsoffersanunprecedentedop- potentiallyrevealingconsistentdistortionsinhowlanguage
portunityingaming,enablingagentstotakeondiverseroles modelsreplicatespecifichumanbehaviors.
and exhibit human-like decision-making skills in intricate Social Simulation. In societal simulation, LLM agents are
game environments. Based on the different characteristics employedtomodelcomplexsocietalbehaviors.Thesesimu-
ofthegamesandrolesoftheagent,theapplicationscanbe lationshelpinunderstandingreal-worldphenomena,such
categorizedintogameplayingandgamegeneration. as social influence, information diffusion, and collective
Game Playing. In role-playing games, LLM agents can decision-making.Generativeagents[30]introduceamulti-
assume various character roles, both as player-controlled agentinteractionmodelwithinaninteractivesandboxenvi-
characters and non-player characters (NPCs). ReAct [33] ronment,leveragingLLMagentstosimulaterealistichuman
prompts LLMs to integrate reasoning and reflection into behavior in a variety of contexts. Building on this, Liu et
actiongeneration,enhancingdecision-makingintheembod- al. [298] introduce a training paradigm that enables LLMs
iedenvironment.Voyager[35]introducesanLLM-powered tolearnfromthesesimulatedsocialinteractionsinvolving
lifelonglearningagentinMinecraftthatpersistentlyexplores multipleLLMagents.S3[299]developsanLLM-basedmulti-
the game world. ChessGPT [287] presents an autonomous agentsystemtoensuretheagents’behaviorscloselymimic
agentonmixedgame-languagedatatofacilitateboardstate thoseofrealhumanswithinsocialnetworks.

18
5.4 ProductivityTools 6.2 MemoryConstraintsandLong-TermAdaptation.
LLMagentsareincreasinglyleveragedtoboostproductivity Maintainingcoherenceacrossmulti-turndialoguesandthe
by automating diverse tasks, facilitating collaboration in longitudinalaccumulationofknowledgerequireseffective
solvingcomplexproblems,andoptimizingefficiencyacross memorymechanisms[310].However,asLLMspossessvery
multipledomains.Below,wehighlighttheirapplicationsin limited effective context [74], [311], integrating sufficient
softwaredevelopmentandrecommendersystems. historical information into prompts becomes challenging.
Thishindersthemodels’contextualawarenessoverextended
SoftwareDevelopment.Sincesoftwaredevelopmentinvolves
interactions.Ensuringinteractioncontinuityrequiresefficient
multipleroles,suchasproductmanagers,developers,and
memoryscalabilityandrelevancemanagement[312]beyond
testers, all working together to deliver high-quality prod-
current practice such as vector databases, memory caches,
ucts,LLMagentsareincreasinglybeingusedtostreamline
context window management, and retrieval-augmented
various aspects of the process. SDM [300] introduces a
generation(RAG)[43].Futuredirectionsincludehierarchical
self-collaboration framework that guides multiple LLM
memoryarchitecturesthatcombineepisodicmemoryforshort-
agents to work together on code generation tasks, enhanc-
termplanningwithsemanticmemoryforlong-termretention,
ing their ability to tackle complex software development
as well as autonomous knowledge compression [313] to
challenges collaboratively. ChatDev [301] proposes a chat-
refine memory dynamically and enhance reasoning over
powered software development framework, where agents
extendedinteractions.
are guided on both what to communicate and how to
communicateeffectively.MetaGPT[27]furtherincorporates
humanworkflows(i.e.,StandardizedOperatingProcedures) 6.3 ReliabilityandScientificRigor
into LLM-powered multi-agent collaboration through a
LLMs,whileknowledge-rich,areneithercomprehensivenor
meta-programmingapproachtoenhancecoordinationand
up-to-date,thuspotentiallyunsuitableasstandalonereplace-
streamlinethecollaborativeprocess.
mentsforstructureddatabases.Theirstochasticnaturemakes
Recommender Systems. In the realm of recommender sys- outputshighlysensitivetominorvariationsinprompts[314],
tems,LLMagentsareincreasinglyutilizedtosimulateuser causinghallucinations[315]andcompoundinguncertainty
behaviors.Agent4Rec[302]employsLLMagentswithinte- in multi-agent systems, such as agentic frameworks for
grateduserprofiling,memory,andactionmodulestomodel medical applications and autonomous scientific discov-
user behavior in recommender systems. AgentCF [303] ery[316],whereunreliableoutputscanmisleadhigh-stake
treats both users and items as LLM agents, introducing decision-making.Addressingthesechallengesnecessitates
a collaborative learning framework to model user-item the development of rigorous validation mechanisms and
interactionsinrecommendersystems.MACRec[304]directly structuredverificationpipelines,includingknowledge-graph-
developsmultipleagentstotackletherecommendationtask. based verification, where outputs are cross-checked against
RecMind[305]employsLLMagentstoincorporateexternal structureddatabases[317],andcross-referencingviaretrieval,
knowledge and carefully plans the utilization of tools for which grounds responses in cited source like web pages
zero-shotpersonalizedrecommendations. asinWebGPT[318].Alongthisdirection,futureworkcan
exploreLLMscapableofdirectcitationgeneration,aswell
asup-to-dateandcomprehensiveknowledgesourcesreadily
6 CHALLENGES AND FUTURE TRENDS availableforLLMapplications.Meanwhile,inhigh-stakes
domains like healthcare, law, or scientific research, pure
Advancements in LLM-based multi-agent systems bring
automationremainsrisky.AI-humanverificationloopsarebe-
significantopportunitiesbutalsopresentpressingchallenges
comingstandardforensuringsafety,reliability,andaccount-
inscalability,memory,reliability,andevaluation.Thissection
ability [315]. Future works can enhance cross-referencing
outlines key obstacles and emerging trends shaping the
mechanisms[319],self-consistency[320],andstandardized
futureofagenticAI.
AI auditing frameworks, such as fact-checking logs, to
improveaccountability.Forexample,onecriticalchallengeis
determiningoptimalinterventionpointsamidthevastscale
6.1 ScalabilityandCoordination
ofLLM-generatedcontent.
Scaling LLM-based multi-agent systems remains challeng-
ing due to high computational demands, inefficiencies in
6.4 Multi-turn,Multi-agentDynamicEvaluation
coordination,andresourceutilization[306],[307].Existing
multi-agent frameworks, designed for lightweight agents Traditional AI evaluation frameworks, designed for static
likefunctioncallsandrule-basedsystems[308],[309],lack datasetsandsingle-turntasks,failtocapturethecomplexities
system-level optimization for LLM agents with billion- of LLM agents in dynamic, multi-turn, and multi-agent
scaleparameters[26].Futuredirectionsincludehierarchical environments [310]. Current benchmarks primarily assess
structuring,wherehigh-levelLLMagentsdelegatesubtasks task execution such as code completion [321], [322] and
tospecializedlower-levelagents,anddecentralizedplanning, dialogue generation [57] in isolated settings, overlooking
whichenablesagentstoplanconcurrentlyandsynchronize emergentagentbehaviors,long-termadaptation,andcollab-
periodicallytomitigatebottlenecks.Advancementsinrobust orativereasoningthatunfoldacrossmulti-turninteractions.
communication protocols and efficient scheduling mecha- Additionally,staticbenchmarksstruggletokeeppacewith
nismsareneededtoenhancecoordination,real-timedecision- evolvingLLMcapabilities[323].Concernspersistregarding
making,andsystemrobustness[306],[307]. potential data contamination, where model performance

19
may stem from memorization rather than genuine reason- REFERENCES
ing. Future research should focus on dynamic evaluation
[1] Z. Xi, W. Chen, X. Guo, W. He, Y. Ding, B. Hong, M. Zhang,
methodologies,integratingmulti-agentinteractionscenarios, J. Wang, S. Jin, E. Zhou et al., “The rise and potential of large
structuredperformancemetrics,andadaptivesamplegen- languagemodelbasedagents:Asurvey,”ScienceChinaInformation
erationalgorithms[324]tocreatemorerobustandreliable Sciences,vol.68,no.2,p.121101,2025.
[2] M.WooldridgeandN.R.Jennings,“Intelligentagents:Theory
assessmentframeworks.
andpractice,”Theknowledgeengineeringreview,vol.10,no.2,pp.
115–152,1995.
[3] D.Zheng,M.Lapata,andJ.Z.Pan,“Largelanguagemodelsas
6.5 RegulatoryMeasuresforSafeDeployment reliableknowledgebases?”arXivpreprintarXiv:2407.13578,2024.
[4] S.Lotfi,M.Finzi,Y.Kuang,T.G.Rudner,M.Goldblum,andA.G.
AsagenticAIsystemsgainautonomy,regulatoryframeworks Wilson,“Non-vacuousgeneralizationboundsforlargelanguage
models,”arXivpreprintarXiv:2312.17173,2023.
mustevolvetoensureaccountability,transparency,andsafety.
[5] H. Fei, Y. Yao, Z. Zhang, F. Liu, A. Zhang, and T.-S. Chua,
Akeychallengeismitigatingalgorithmicbias–agentsmay “Frommultimodalllmtohuman-levelai:Modality,instruction,
inadvertentlydiscriminatebasedongender,age,ethnicity, reasoning,efficiencyandbeyond,”inCOLING,2024,pp.1–8.
[6] J. Huang and K. C.-C. Chang, “Towards reasoning in large
or other sensitive attributes, often in ways imperceptible
languagemodels:Asurvey,”arXivpreprintarXiv:2212.10403,2022.
to developers [248], [325]. Addressing this requires stan-
[7] C.Wang,W.Luo,Q.Chen,H.Mai,J.Guo,S.Dong,Z.Li,L.Ma,
dardizedauditingprotocolstosystematicallyidentifyand S.Gaoetal.,“Tool-lmm:Alargemulti-modalmodelfortoolagent
correct biases, alongside traceability mechanisms that log learning,”arXive-prints,pp.arXiv–2401,2024.
[8] Z.Zhang,X.Bo,C.Ma,R.Li,X.Chen,Q.Dai,J.Zhu,Z.Dong,
decision-makingpathwaysandmodelconfidenceforpost-
and J.-R. Wen, “A survey on the memory mechanism of large
hocaccountability.Futureworkcanexploremultidisciplinary languagemodelbasedagents,”arXivpreprintarXiv:2404.13501,
approaches combining fairness-aware training pipelines 2024.
[9] P. Zhao, Z. Jin, and N. Cheng, “An in-depth survey of large
with legal and ethical safeguards. Collaboration between
languagemodel-basedartificialintelligenceagents,”arXivpreprint
policymakers, researchers, and industry stakeholders will
arXiv:2309.14365,2023.
becriticaltoensuringAI-drivensystemsoperatesafelyand [10] T.Sumers,S.Yao,K.Narasimhan,andT.Griffiths,“Cognitive
equitablyinalignmentwithsocietalvalues[326]. architecturesforlanguageagents,”TMLR,2023.
[11] S.Hu,T.Huang,F.Ilhan,S.Tekin,G.Liu,R.Kompella,andL.Liu,
“Asurveyonlargelanguagemodel-basedgameagents,”arXiv
preprintarXiv:2404.02039,2024.
6.6 Role-playingScenarios [12] X.Xu,Y.Wang,C.Xu,Z.Ding,J.Jiang,Z.Ding,andB.F.Karlsson,
“Asurveyongameplayingagentsandlargemodels:Methods,
LLMagentscansimulaterolessuchasresearchers,debators, applications, and challenges,” arXiv preprint arXiv:2403.10249,
and instructors [307], [327], but their effectiveness is con- 2024.
[13] M. Xu, H. Du, D. Niyato, J. Kang, Z. Xiong, S. Mao, Z. Han,
strainedbytrainingdatalimitationsandanincompleteun-
A.Jamalipour,D.I.Kim,X.Shenetal.,“Unleashingthepower
derstandingofhumancognition[326],[328].SinceLLMsare ofedge-cloudgenerativeaiinmobilenetworks:Asurveyofaigc
predominantlytrainedonweb-basedcorpora,theystruggle services,”IEEECommunicationsSurveys&Tutorials,vol.26,no.2,
toemulateroleswithinsufficientrepresentationonline[329] pp.1127–1170,2024.
[14] G.Qu,Q.Chen,W.Wei,Z.Lin,X.Chen,andK.Huang,“Mobile
and often produce conversations lacking diversity [268].
edge intelligence for large language models: A contemporary
Futureresearchshouldfocusonenhancingrole-playfidelity survey,”IEEECommunicationsSurveys&Tutorials,2025.
byimprovingmulti-agentcoordination,incorporatingreal- [15] Z.Durante,Q.Huang,N.Wake,R.Gong,J.S.Park,B.Sarkar,
R. Taori, Y. Noda, D. Terzopoulos, Y. Choi et al., “Agent ai:
worldreasoningframeworks,andrefiningdialoguediversity
Surveyingthehorizonsofmultimodalinteraction,”arXivpreprint
tobettersupportcomplexhuman-AIinteractions. arXiv:2401.03568,2024.
[16] Y. Wang, Y. Pan, Q. Zhao, Y. Deng, Z. Su, L. Du, and
T. H. Luan, “Large model agents: State-of-the-art, cooperation
paradigms,securityandprivacy,andfuturetrends,”arXivpreprint
7 CONCLUSION arXiv:2409.14457,2024.
[17] L.Wang,C.Ma,X.Feng,Z.Zhang,H.Yang,J.Zhang,Z.Chen,
This survey has presented a systematic taxonomy of LLM J.Tang,X.Chen,Y.Linetal.,“Asurveyonlargelanguagemodel
basedautonomousagents,”FrontiersofComputerScience,vol.18,
agents, deconstructing their methodological components
no.6,p.186345,2024.
acrossconstruction,collaboration,andevolutiondimensions. [18] X.Li,S.Wang,S.Zeng,Y.Wu,andY.Yang,“Asurveyonllm-based
We have advanced a unified architectural perspective that multi-agentsystems:workflow,infrastructure,andchallenges,”
bridgesindividualagentdesignprincipleswithmulti-agent Vicinagearth,vol.1,no.1,p.9,2024.
[19] X.Li,“Areviewofprominentparadigmsforllm-basedagents:
collaborativesystems—anapproachthatdistinguishesour
Tooluse(includingrag),planning,andfeedbacklearning,”arXiv
workfromprevioussurveys.Despiteremarkableprogress, preprintarXiv:2406.05804,2024.
significant challenges remain, including scalability limita- [20] W. Jin, H. Du, B. Zhao, X. Tian, B. Shi, and G. Yang, “A com-
prehensivesurveyonmulti-agentcooperativedecision-making:
tions, memory constraints, reliability concerns, and inade-
Scenarios,approaches,challengesandperspectives,”arXivpreprint
quateevaluationframeworks.Lookingforward,weantici- arXiv:2503.13415,2025.
patetransformativedevelopmentsincoordinationprotocols, [21] Y. Ma, Z. Song, Y. Zhuang, J. Hao, and I. King, “A survey on
hybrid architectures, self-supervised learning, and safety vision-language-actionmodelsforembodiedai,”arXivpreprint
arXiv:2405.14093,2024.
mechanisms that will enhance agent capabilities across
[22] T. Guo, X. Chen, Y. Wang, R. Chang, S. Pei, N. V. Chawla,
diverse domains. By providing this foundational under- O. Wiest, and X. Zhang, “Large language model based multi-
standingandidentifyingpromisingresearchdirections,we agents: A survey of progress and challenges,” arXiv preprint
hopetocontributetotheresponsibleadvancementofLLM
arXiv:2402.01680,2024.
[23] T.Masterman,S.Besen,M.Sawtell,andA.Chao,“Thelandscape
agenttechnologiesthatmayfundamentallyreshapehuman-
ofemergingaiagentarchitecturesforreasoning,planning,and
machinecollaboration. toolcalling:Asurvey,”arXivpreprintarXiv:2404.11584,2024.

20
[24] Y.Cheng,C.Zhang,Z.Zhang,X.Meng,S.Hong,W.Li,Z.Wang, [46] H.Trivedi,N.Balasubramanian,T.Khot,andA.Sabharwal,“Inter-
Z.Wang,F.Yin,J.Zhaoetal.,“Exploringlargelanguagemodel leavingretrievalwithchain-of-thoughtreasoningforknowledge-
based intelligent agents: Definitions, methods, and prospects,” intensivemulti-stepquestions,”arXivpreprintarXiv:2212.10509,
arXivpreprintarXiv:2401.03428,2024. 2022.
[25] G. Li, H. A. A. K. Hammoud, H. Itani, D. Khizbullin, and [47] X.Li,C.Zhu,L.Li,Z.Yin,T.Sun,andX.Qiu,“Llatrieval:Llm-
B.Ghanem,“Camel:Communicativeagentsfor”mind”explo- verifiedretrievalforverifiablegeneration,”inNAACL,2024,pp.
rationoflargelanguagemodelsociety,”inNeurIPS,2023. 5453–5471.
[26] Q.Wu,G.Bansal,J.Zhang,Y.Wu,B.Li,E.Zhu,L.Jiang,X.Zhang, [48] W.Wu,Y.Jing,Y.Wang,W.Hu,andD.Tao,“Graph-augmented
S.Zhang,J.Liu,A.H.Awadallah,R.W.White,D.Burger,and reasoning:Evolvingstep-by-stepknowledgegraphretrievalfor
C.Wang,“Autogen:Enablingnext-genllmapplicationsviamulti- llmreasoning,”2025.
agentconversation,”2023. [49] X.Guan,J.Zeng,F.Meng,C.Xin,Y.Lu,H.Lin,X.Han,L.Sun,
[27] S.Hong,X.Zheng,J.Chen,Y.Cheng,J.Wang,C.Zhang,Z.Wang, andJ.Zhou,“Deeprag:Thinkingtoretrievalstepbystepforlarge
S.K.S.Yau,Z.Lin,L.Zhouetal.,“Metagpt:Metaprogramming languagemodels,”arXivpreprintarXiv:2502.01142,2025.
foramulti-agentcollaborativeframework,”inICLR,2024. [50] L. Wang, W. Xu, Y. Lan, Z. Hu, Y. Lan, R. K.-W. Lee, and E.-
[28] C.Qian,W.Liu,H.Liu,N.Chen,Y.Dang,J.Li,C.Yang,W.Chen, P.Lim,“Plan-and-solveprompting:Improvingzero-shotchain-
Y.Su,X.Congetal.,“Chatdev:Communicativeagentsforsoftware of-thoughtreasoningbylargelanguagemodels,”arXivpreprint
development,”inACL,2024,pp.15174–15186. arXiv:2305.04091,2023.
[29] J.Zhang,J.Xiang,Z.Yu,F.Teng,X.-H.Chen,J.Chen,M.Zhuge, [51] E. H. Durfee, “Distributed problem solving and planning,” in
X.Cheng,S.Hong,J.Wang,B.Liu,Y.Luo,andC.Wu,“AFlow: ECCAIAdvancedCourseonArtificialIntelligence. Springer,2001,
Automatingagenticworkflowgeneration,”inICLR,2025. pp.118–149.
[30] J.S.Park,J.O’Brien,C.J.Cai,M.R.Morris,P.Liang,andM.S. [52] M. Tao, D. Zhao, and Y. Feng, “Chain-of-discussion: A multi-
Bernstein,“Generativeagents:Interactivesimulacraofhuman modelframeworkforcomplexevidence-basedquestionanswer-
behavior,”inUIST,2023,pp.1–22. ing,”arXivpreprintarXiv:2402.16313,2024.
[31] L.Wang,J.Zhang,H.Yang,Z.-Y.Chen,J.Tang,Z.Zhang,X.Chen, [53] M. Hu, Y. Mu, X. Yu, M. Ding, S. Wu, W. Shao, Q. Chen,
Y.Lin,H.Sun,R.Songetal.,“Userbehaviorsimulationwithlarge B. Wang, Y. Qiao, and P. Luo, “Tree-planner: Efficient close-
languagemodel-basedagents,”ACMTransactionsonInformation looptaskplanningwithlargelanguagemodels,”arXivpreprint
Systems,vol.43,no.2,pp.1–37,2025. arXiv:2310.08582,2023.
[32] O.Khattab,A.Singhvi,P.Maheshwari,Z.Zhang,K.Santhanam, [54] J.-W. Choi, H. Kim, H. Ong, Y. Yoon, M. Jang, J. Kim et al.,
S. Vardhamanan, S. Haq, A. Sharma, T. T. Joshi, H. Moazam, “Reactree:Hierarchicaltaskplanningwithdynamictreeexpansion
H.Miller,M.Zaharia,andC.Potts,“Dspy:Compilingdeclarative usingllmagentnodes,”2025.
languagemodelcallsintoself-improvingpipelines,”inICLR,2024. [55] J.Long,“Largelanguagemodelguidedtree-of-thought,”arXiv
[33] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and preprintarXiv:2305.08291,2023.
Y. Cao, “React: Synergizing reasoning and acting in language [56] D.Zhang,S.Zhoubian,Z.Hu,Y.Yue,Y.Dong,andJ.Tang,“Rest-
models,”inICLR,2023. mcts*:Llmself-trainingviaprocessrewardguidedtreesearch,”
[34] M.Besta,N.Blach,A.Kubicek,R.Gerstenberger,M.Podstawski, NeurIPS,vol.37,pp.64735–64772,2024.
L.Gianinazzi,J.Gajda,T.Lehmann,H.Niewiadomski,P.Nyczyk [57] A. Lykov, M. Dronova, N. Naglov, M. Litvinov, S. Satsevich,
etal.,“Graphofthoughts:Solvingelaborateproblemswithlarge A.Bazhenov,V.Berman,A.Shcherbak,andD.Tsetserukou,“Llm-
languagemodels,”inAAAI,vol.38,no.16,2024,pp.17682–17690. mars:Largelanguagemodelforbehaviortreegenerationandnlp-
[35] G.Wang,Y.Xie,Y.Jiang,A.Mandlekar,C.Xiao,Y.Zhu,L.Fan, enhanceddialogueinmulti-agentrobotsystems,”arXivpreprint
andA.Anandkumar,“Voyager:Anopen-endedembodiedagent arXiv:2312.09348,2023.
withlargelanguagemodels,”TMLR,2023. [58] J. Ao, F. Wu, Y. Wu, A. Swikir, and S. Haddadin, “Llm as bt-
[36] X. Zhu, Y. Chen, H. Tian, C. Tao, W. Su, C. Yang, G. Huang, planner:Leveragingllmsforbehaviortreegenerationinrobot
B.Li,L.Lu,X.Wangetal.,“Ghostintheminecraft:Generally taskplanning,”arXivpreprintarXiv:2409.10444,2024.
capableagentsforopen-worldenvironmentsvialargelanguage [59] C.Rivera,G.Byrd,W.Paul,T.Feldman,M.Booker,E.Holmes,
modelswithtext-basedknowledgeandmemory,”arXivpreprint D.Handelman,B.Kemp,A.Badger,A.Schmidtetal.,“Concepta-
arXiv:2305.17144,2023. gent:Llm-drivenpreconditiongroundingandtreesearchforro-
[37] A.Zhao,D.Huang,Q.Xu,M.Lin,Y.-J.Liu,andG.Huang,“Expel: busttaskplanningandexecution,”arXivpreprintarXiv:2410.06108,
Llmagentsareexperientiallearners,”inAAAI,2024,pp.19632– 2024.
19642. [60] V.Bhat,A.U.Kaypak,P.Krishnamurthy,R.Karri,andF.Khorrami,
[38] N.Shinn,F.Cassano,A.Gopinath,K.Narasimhan,andS.Yao, “Groundingllmsforrobottaskplanningusingclosed-loopstate
“Reflexion:Languageagentswithverbalreinforcementlearning,” feedback,”arXivpreprintarXiv:2402.08546,2024.
NeurIPS,vol.36,pp.8634–8652,2023. [61] H.Li,H.Jiang,T.Zhang,Z.Yu,A.Yin,H.Cheng,S.Fu,Y.Zhang,
[39] J.Ruan,Y.Chen,B.Zhang,Z.Xu,T.Bao,H.Mao,Z.Li,X.Zeng, and W. He, “Traineragent: Customizable and efficient model
R. Zhao et al., “Tptu: Task planning and tool usage of large trainingthroughllm-poweredmulti-agentsystem,”arXivpreprint
languagemodel-basedaiagents,”inNeurIPS,2023. arXiv:2311.06622,2023.
[40] T.Xie,F.Zhou,Z.Cheng,P.Shi,L.Weng,Y.Liu,T.J.Hua,J.Zhao, [62] G. Wan, Y. Wu, J. Chen, and S. Li, “Dynamic self-consistency:
Q.Liu,C.Liuetal.,“Openagents:Anopenplatformforlanguage Leveraging reasoning paths for efficient llm sampling,” arXiv
agentsinthewild,”arXivpreprintarXiv:2310.10634,2023. preprintarXiv:2408.17017,2024.
[41] H.Wang,H.Xin,C.Zheng,Z.Liu,Q.Cao,Y.Huang,J.Xiong, [63] S.Seo,J.Lee,S.Noh,andH.Kang,“Llm-basedcooperativeagents
H.Shi,E.Xie,J.Yinetal.,“Lego-prover:Neuraltheoremproving usinginformationrelevanceandplanvalidation,”arXivpreprint
withgrowinglibraries,”inICLR,2024. arXiv:2405.16751,2024.
[42] C. Packer, V. Fang, S. G. Patil, K. Lin, S. Wooders, and J. E. [64] H. Sun, Y. Zhuang, L. Kong, B. Dai, and C. Zhang, “Adaplan-
Gonzalez,“Memgpt:Towardsllmsasoperatingsystems,”CoRR, ner:Adaptiveplanningfromfeedbackwithlanguagemodels,”
2023. NeurIPS,vol.36,pp.58202–58245,2023.
[43] P.Lewis,E.Perez,A.Piktus,F.Petroni,V.Karpukhin,N.Goyal, [65] M.Jafaripour,S.Golestan,S.Miwa,Y.Mitsuka,andO.Zaiane,
H.Ku¨ttler,M.Lewis,W.-t.Yih,T.Rockta¨scheletal.,“Retrieval- “Adaptiveiterativefeedbackpromptingforobstacle-awarepath
augmented generation for knowledge-intensive nlp tasks,” planningviallms,”inAAAIWorkshop,2025.
NeurIPS,vol.33,pp.9459–9474,2020. [66] S.Qiao,H.Gui,C.Lv,Q.Jia,H.Chen,andN.Zhang,“Making
[44] D.Edge,H.Trinh,N.Cheng,J.Bradley,A.Chao,A.Mody,S.Truitt, languagemodelsbettertoollearnerswithexecutionfeedback,”
D. Metropolitansky, R. O. Ness, and J. Larson, “From local to arXivpreprintarXiv:2305.13068,2023.
global:Agraphragapproachtoquery-focusedsummarization,” [67] R. Yang, L. Song, Y. Li, S. Zhao, Y. Ge, X. Li, and Y. Shan,
arXivpreprintarXiv:2404.16130,2024. “Gpt4tools:Teachinglargelanguagemodeltousetoolsviaself-
[45] Y.Zhang,R.Sun,Y.Chen,T.Pfister,R.Zhang,andS.Arik,“Chain instruction,”NeurIPS,vol.36,pp.71995–72007,2023.
ofagents:Largelanguagemodelscollaboratingonlong-context [68] S. Yuan, K. Song, J. Chen, X. Tan, Y. Shen, R. Kan, D. Li, and
tasks,”AdvancesinNeuralInformationProcessingSystems,vol.37, D.Yang,“Easytool:Enhancingllm-basedagentswithconcisetool
pp.132208–132237,2024. instruction,”arXivpreprintarXiv:2401.06201,2024.

21
[69] S. Wu, S. Zhao, Q. Huang, K. Huang, M. Yasunaga, K. Cao, [93] W. Yuan, R. Y. Pang, K. Cho, X. Li, S. Sukhbaatar, J. Xu, and
V. Ioannidis, K. Subbian, J. Leskovec, and J. Y. Zou, “Avatar: J.Weston,“Self-rewardinglanguagemodels,”2024.
Optimizingllmagentsfortoolusageviacontrastivereasoning,” [94] K.Yang,D.Klein,A.Celikyilmaz,N.Peng,andY.Tian,“Rlcd:
NeurIPS,vol.37,pp.25981–26010,2025. Reinforcementlearningfromcontrastivedistillationforlmalign-
[70] Y.Huang,J.Sansom,Z.Ma,F.Gervits,andJ.Chai,“Drivlme: ment,”inICLR,2024.
Enhancingllm-basedautonomousdrivingagentswithembodied [95] J.-C.Pang,P.Wang,K.Li,X.-H.Chen,J.Xu,Z.Zhang,andY.Yu,
andsocialexperiences,”inIROS. IEEE,2024,pp.3153–3160. “Languagemodelself-improvementbyreinforcementlearning
[71] Y. Zhang, S. Yang, C. Bai, F. Wu, X. Li, Z. Wang, and X. Li, contemplation,”inICLR,2024.
“Towardsefficientllmgroundingforembodiedmulti-agentcollab- [96] C. Zhang, K. Yang, S. Hu, Z. Wang, G. Li, Y. Sun, C. Zhang,
oration,”arXivpreprintarXiv:2405.14314,2024. Z.Zhang,A.Liu,S.-C.Zhuetal.,“Proagent:buildingproactive
[72] B.Colle,“Improvingembodiedllmagentscapabilitiesthrough cooperativeagentswithlargelanguagemodels,”inAAAI,vol.38,
collaboration,”2024. no.16,2024,pp.17591–17599.
[73] D.A.Boiko,R.MacKnight,B.Kline,andG.Gomes,“Autonomous [97] H. Ma, T. Hu, Z. Pu, L. Boyin, X. Ai, Y. Liang, and M. Chen,
chemicalresearchwithlargelanguagemodels,”Nature,vol.624, “Coevolvingwiththeotheryou:Fine-tuningllmwithsequential
no.7992,pp.570–578,2023. cooperativemulti-agentreinforcementlearning,”NeurIPS,vol.37,
[74] H. Jiang, Q. Wu, C.-Y. Lin, Y. Yang, and L. Qiu, “Llmlingua: pp.15497–15525,2024.
Compressingpromptsforacceleratedinferenceoflargelanguage [98] C. Ma, Z. Yang, H. Ci, J. Gao, M. Gao, X. Pan, and Y. Yang,
models,”inEMNLP,2023,pp.13358–13376. “Evolvingdiversered-teamlanguagemodelsinmulti-roundmulti-
[75] S.Qiao,N.Zhang,R.Fang,Y.Luo,W.Zhou,Y.E.Jiang,C.Lv, agentgames,”arXivpreprintarXiv:2310.00322,2023.
andH.Chen,“Autoact:Automaticagentlearningfromscratch [99] T.Liang,Z.He,W.Jiao,X.Wang,Y.Wang,R.Wang,Y.Yang,S.Shi,
forqaviaself-planning,”arXivpreprintarXiv:2401.05268,2024. andZ.Tu,“Encouragingdivergentthinkinginlargelanguage
[76] M. Suzgun and A. T. Kalai, “Meta-prompting: Enhancing lan- modelsthroughmulti-agentdebate,”inEMNLP,2024,pp.17889–
guage models with task-agnostic scaffolding,” arXiv preprint 17904.
arXiv:2401.12954,2024. [100] Z.Gou,Z.Shao,Y.Gong,Y.Yang,N.Duan,W.Chenetal.,“Critic:
[77] A. Khan, J. Hughes, D. Valentine, L. Ruis, K. Sachan, A. Rad- Large language models can self-correct with tool-interactive
hakrishnan,E.Grefenstette,S.R.Bowman,T.Rockta¨schel,and critiquing,”inICLR,2024.
E. Perez, “Debating with more persuasive llms leads to more [101] Y.Song,D.Yin,X.Yue,J.Huang,S.Li,andB.Y.Lin,“Trialand
truthfulanswers,”arXivpreprintarXiv:2402.06782,2024. error:Exploration-basedtrajectoryoptimizationofllmagents,”in
[78] X.Tang,A.Zou,Z.Zhang,Z.Li,Y.Zhao,X.Zhang,A.Cohan,and ACL,2024,pp.7584–7600.
M.Gerstein,“Medagents:Largelanguagemodelsascollaborators [102] S. Jiang, Y. Wang, and Y. Wang, “Selfevolve: A code evo-
forzero-shotmedicalreasoning,”arXivpreprintarXiv:2311.10537, lution framework via large language models,” arXiv preprint
2023. arXiv:2306.02907,2023.
[79] J.C.-Y.Chen,S.Saha,andM.Bansal,“Reconcile:Round-table [103] X.Huang,W.Liu,X.Chen,X.Wang,H.Wang,D.Lian,Y.Wang,
conferenceimprovesreasoningviaconsensusamongdiversellms,” R.Tang,andE.Chen,“Understandingtheplanningofllmagents:
arXivpreprintarXiv:2309.13007,2023. Asurvey,”arXivpreprintarXiv:2402.02716,2024.
[80] T. Liang, Z. He, W. Jiao, X. Wang, Y. Wang, R. Wang, Y. Yang, [104] T.Kojima,S.S.Gu,M.Reid,Y.Matsuo,andY.Iwasawa,“Large
S. Shi, and Z. Tu, “Encouraging divergent thinking in large languagemodelsarezero-shotreasoners,”NeurIPS,vol.35,pp.
language models through multi-agent debate,” arXiv preprint 22199–22213,2022.
arXiv:2305.19118,2023. [105] J.Wei,X.Wang,D.Schuurmans,M.Bosma,F.Xia,E.Chi,Q.V.Le,
[81] K.Kim,S.Lee,K.-H.Huang,H.P.Chan,M.Li,andH.Ji,“Can D.Zhouetal.,“Chain-of-thoughtpromptingelicitsreasoningin
llms produce faithful explanations for fact-checking? towards largelanguagemodels,”NeurIPS,vol.35,pp.24824–24837,2022.
faithfulexplainablefact-checkingviamulti-agentdebate,”arXiv [106] X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, S. Narang,
preprintarXiv:2402.07401,2024. A.Chowdhery,andD.Zhou,“Self-consistencyimproveschain
[82] Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, and I. Mordatch, of thought reasoning in language models,” arXiv preprint
“Improvingfactualityandreasoninginlanguagemodelsthrough arXiv:2203.11171,2022.
multiagentdebate,”inICML,2023. [107] W.LiandW.Pan,“Enhancingchain-of-thoughtreasoninginlarge
[83] Y. Zhu, S. Qiao, Y. Ou, S. Deng, N. Zhang, S. Lyu, Y. Shen, languagemodelsthroughtextstylediversityandpromptfusion,”
L.Liang,J.Gu,andH.Chen,“Knowagent:Knowledge-augmented inEIBDCT,vol.13181. SPIE,2024,pp.226–232.
planningforllm-basedagents,”arXivpreprintarXiv:2403.03101, [108] J. Jiang, Z. Chen, Y. Min, J. Chen, X. Cheng, J. Wang, Y. Tang,
2024. H.Sun,J.Deng,W.X.Zhaoetal.,“Technicalreport:Enhancing
[84] S.Qiao,R.Fang,N.Zhang,Y.Zhu,X.Chen,S.Deng,Y.Jiang, llm reasoning with reward-guided tree search,” arXiv preprint
P. Xie, F. Huang, and H. Chen, “Agent planning with world arXiv:2411.11694,2024.
knowledgemodel,”NeurIPS,vol.37,pp.114843–114871,2024. [109] C.B.Browne,E.Powley,D.Whitehouse,S.M.Lucas,P.I.Cowling,
[85] R.Fang,S.Qiao,andZ.Xi,“Refiningguidelineknowledgefor P.Rohlfshagen,S.Tavener,D.Perez,S.Samothrakis,andS.Colton,
agentplanningusingtextgrad,”inICKG. IEEE,2024,pp.102–103. “Asurveyofmontecarlotreesearchmethods,”IEEETransactions
[86] Q. Zhong, L. Ding, J. Liu, B. Du, and D. Tao, “Self-evolution onComputationalIntelligenceandAIingames,vol.4,no.1,pp.1–43,
learningfordiscriminativelanguagemodelpretraining,”inACL 2012.
Findings,2023,pp.4130–4145. [110] H. Guo, Z. Liu, Y. Zhang, and Z. Wang, “Can large language
[87] T.Akiba,M.Shing,Y.Tang,Q.Sun,andD.Ha,“Evolutionaryop- modelsplaygames?acasestudyofaself-playapproach,”arXiv
timizationofmodelmergingrecipes,”NatureMachineIntelligence, preprintarXiv:2403.05632,2024.
pp.1–10,2025. [111] Y.Liu,P.Sun,andH.Li,“Largelanguagemodelsasagentsin
[88] S.Wu,K.Lu,B.Xu,J.Lin,Q.Su,andC.Zhou,“Self-evolved two-playergames,”arXivpreprintarXiv:2402.08078,2024.
diverse data sampling for efficient instruction tuning,” arXiv [112] A. R. Laleh and M. N. Ahmadabadi, “A survey on enhancing
preprintarXiv:2311.08182,2023. reinforcementlearningincomplexenvironments:Insightsfrom
[89] A.Madaan,N.Tandon,P.Gupta,S.Hallinan,L.Gao,S.Wiegreffe, humanandllmfeedback,”arXivpreprintarXiv:2411.13410,2024.
U. Alon, N. Dziri, S. Prabhumoye, Y. Yang et al., “Self-refine: [113] Z. Shen, “Llm with tools: A survey,” arXiv preprint
Iterative refinement with self-feedback,” NeurIPS, vol. 36, pp. arXiv:2409.18807,2024.
46534–46594,2023. [114] C.Y.Kim,C.P.Lee,andB.Mutlu,“Understandinglarge-language
[90] E.Zelikman,Y.Wu,J.Mu,andN.D.Goodman,“Star:Self-taught model(llm)-poweredhuman-robotinteraction,”inHRI,2024,pp.
reasonerbootstrappingreasoningwithreasoning,”inNeurIPS, 371–380.
vol.1126,2024. [115] B.Li,Y.Wang,J.Gu,K.-W.Chang,andN.Peng,“Metal:Amulti-
[91] A.Hosseini,X.Yuan,N.Malkin,A.Courville,A.Sordoni,and agent framework for chart generation with test-time scaling,”
R.Agarwal,“V-star:Trainingverifiersforself-taughtreasoners,” arXivpreprintarXiv:2502.17651,2025.
inCOLM,2024. [116] S. Guo, C. Deng, Y. Wen, H. Chen, Y. Chang, and J. Wang,
[92] Y. Weng, M. Zhu, F. Xia, B. Li, S. He, S. Liu, B. Sun, K. Liu, “Ds-agent: Automated data science by empowering large
andJ.Zhao,“Largelanguagemodelsarebetterreasonerswith language models with case-based reasoning,” arXiv preprint
self-verification,”inEMNLPFindings,2023,pp.2550–2575. arXiv:2402.17453,2024.

22
[117] Z. Yin, Q. Sun, C. Chang, Q. Guo, J. Dai, X. Huang, and [139] Y.Zhang,Q.Jiang,X.Han,N.Chen,Y.Yang,andK.Ren,“Bench-
X.Qiu,“Exchange-of-thought:Enhancinglargelanguagemodel marking data science agents,” arXiv preprint arXiv:2402.17168,
capabilitiesthroughcross-modelcommunication,”arXivpreprint 2024.
arXiv:2312.01823,2023. [140] Y.Huang,J.Luo,Y.Yu,Y.Zhang,F.Lei,Y.Wei,S.He,L.Huang,
[118] Y.Li,S.Ren,P.Wu,S.Chen,C.Feng,andW.Zhang,“Learning X. Liu, J. Zhao et al., “Da-code: Agent data science code gen-
distilledcollaborationgraphformulti-agentperception,”NeurIPS, eration benchmark for large language models,” arXiv preprint
vol.34,pp.29541–29552,2021. arXiv:2410.07331,2024.
[119] Z. Liu, Y. Zhang, P. Li, Y. Liu, and D. Yang, “A dynamic llm- [141] B. Huang, Y. Yu, J. Huang, X. Zhang, and J. Ma, “Dca-
poweredagentnetworkfortask-orientedagentcollaboration,”in bench:Abenchmarkfordatasetcurationagents,”arXivpreprint
COLM,2024. arXiv:2406.07275,2024.
[120] Y.Kim,C.Park,H.Jeong,Y.S.Chan,X.Xu,D.McDuff,H.Lee, [142] J.Xie,K.Zhang,J.Chen,T.Zhu,R.Lou,Y.Tian,Y.Xiao,and
M.Ghassemi,C.Breazeal,H.Parketal.,“Mdagents:Anadaptive Y.Su,“Travelplanner:Abenchmarkforreal-worldplanningwith
collaboration of llms for medical decision-making,” NeurIPS, languageagents,”arXivpreprintarXiv:2402.01622,2024.
vol.37,pp.79410–79452,2024. [143] Q.Huang,J.Vora,P.Liang,andJ.Leskovec,“Benchmarkinglarge
[121] L. Ying, T. Zhi-Xuan, V. Mansinghka, and J. B. Tenenbaum, language models as ai research agents,” in NeurIPS Workshop,
“Inferringthegoalsofcommunicatingagentsfromactionsand 2023.
instructions,”inProceedingsoftheAAAISymposiumSeries,vol.2, [144] J. S. Chan, N. Chowdhury, O. Jaffe, J. Aung, D. Sherburn,
no.1,2023,pp.26–33. E.Mays,G.Starace,K.Liu,L.Maksin,T.Patwardhanetal.,“Mle-
[122] J.VyasandM.Mercango¨z,“Autonomousindustrialcontrolusing bench:Evaluatingmachinelearningagentsonmachinelearning
anagenticframeworkwithlargelanguagemodels,”arXivpreprint engineering,”arXivpreprintarXiv:2410.07095,2024.
arXiv:2411.05904,2024. [145] M.Andriushchenko,A.Souly,M.Dziemian,D.Duenas,M.Lin,
[123] D.Dell’Anna,N.Alechina,F.Dalpiaz,M.Dastani,andB.Logan, J.Wang,D.Hendrycks,A.Zou,J.Z.Kolter,M.Fredriksonetal.,
“Data-drivenrevisionofconditionalnormsinmulti-agentsystems,” “Agentharm:Benchmarkingrobustnessofllmagentsonharmful
JournalofArtificialIntelligenceResearch,vol.75,pp.1549–1593,2022. tasks,”inICLR,2024.
[124] X.Liu,H.Yu,H.Zhang,Y.Xu,X.Lei,H.Lai,Y.Gu,H.Ding, [146] T.Xie,D.Zhang,J.Chen,X.Li,S.Zhao,R.Cao,J.H.Toh,Z.Cheng,
K.Men,K.Yangetal.,“Agentbench:Evaluatingllmsasagents,” D.Shin,F.Leietal.,“Osworld:Benchmarkingmultimodalagents
arXivpreprintarXiv:2308.03688,2023. foropen-endedtasksinrealcomputerenvironments,”NeurIPS,
vol.37,pp.52040–52094,2025.
[125] X.Deng,Y.Gu,B.Zheng,S.Chen,S.Stevens,B.Wang,H.Sun,
[147] K. Xu, Y. Kordi, T. Nayak, A. Asija, Y. Wang, K. Sanders,
andY.Su,“Mind2web:Towardsageneralistagentfortheweb,”
A. Byerly, J. Zhang, B. Van Durme, and D. Khashabi, “Tur [k]
NeurIPS,vol.36,pp.28091–28114,2023.
ingbench:Achallengebenchmarkforwebagents,”arXivpreprint
[126] G.Yin,H.Bai,S.Ma,F.Nan,Y.Sun,Z.Xu,S.Ma,J.Lu,X.Kong,
arXiv:2403.11905,2024.
A.Zhangetal.,“Mmau:Aholisticbenchmarkofagentcapabilities
[148] R.Kapoor,Y.P.Butala,M.Russak,J.Y.Koh,K.Kamble,W.Al-
acrossdiversedomains,”arXivpreprintarXiv:2407.18961,2024.
Shikh,andR.Salakhutdinov,“Omniact:Adatasetandbenchmark
[127] K.Gu,R.Shang,R.Jiang,K.Kuang,R.-J.Lin,D.Lyu,Y.Mao,
forenablingmultimodalgeneralistautonomousagentsfordesk-
Y.Pan,T.Wu,J.Yuetal.,“Blade:Benchmarkinglanguagemodel
topandweb,”inECCV. Springer,2024,pp.161–178.
agentsfordata-drivenscience,”arXivpreprintarXiv:2408.09667,
[149] J.Yang,S.Liu,H.Guo,Y.Dong,X.Zhang,S.Zhang,P.Wang,
2024.
Z.Zhou,B.Xie,Z.Wangetal.,“Egolife:Towardsegocentriclife
[128] X. Liu, T. Zhang, Y. Gu, I. L. Iong, Y. Xu, X. Song, S. Zhang,
assistant,”arXivpreprintarXiv:2503.03803,2025.
H.Lai,X.Liu,H.Zhaoetal.,“Visualagentbench:Towardslarge
[150] J.Wang,M.Zerun,Y.Li,S.Zhang,C.Chen,K.Chen,andX.Le,
multimodalmodelsasvisualfoundationagents,”arXivpreprint
“Gta:abenchmarkforgeneraltoolagents,”inNeurIPS,2024.
arXiv:2408.06327,2024.
[151] F. F. Xu, Y. Song, B. Li, Y. Tang, K. Jain, M. Bao, Z. Z. Wang,
[129] M. Li, S. Zhao, Q. Wang, K. Wang, Y. Zhou, S. Srivastava,
X.Zhou,Z.Guo,M.Caoetal.,“Theagentcompany:benchmarking
C.Gokmen,T.Lee,E.L.Li,R.Zhangetal.,“Embodiedagent
llm agents on consequential real world tasks,” arXiv preprint
interface: Benchmarking llms for embodied decision making,”
arXiv:2412.14161,2024.
NeurIPS,vol.37,pp.100428–100534,2025.
[152] R. Barbarroxa, L. Gomes, and Z. Vale, “Benchmarking large
[130] T.Xu,L.Chen,D.-J.Wu,Y.Chen,Z.Zhang,X.Yao,Z.Xie,Y.Chen,
languagemodelsformulti-agentsystems:Acomparativeanalysis
S. Liu, B. Qian et al., “Crab: Cross-platfrom agent benchmark
ofautogen,crewai,andtaskweaver,”inInternationalConferenceon
formulti-modalembodiedlanguagemodelagents,”inNeurIPS
PracticalApplicationsofAgentsandMulti-AgentSystems. Springer,
Workshop,2024.
2024,pp.39–48.
[131] N.Butt,V.Chandrasekaran,N.Joshi,B.Nushi,andV.Balachan- [153] Z. Li, X. Wu, H. Du, H. Nghiem, and G. Shi, “Benchmark
dran,“Benchagents:Automatedbenchmarkcreationwithagent evaluations,applications,andchallengesoflargevisionlanguage
interaction,”arXivpreprintarXiv:2410.22584,2024. models:Asurvey,”arXivpreprintarXiv:2501.02189,2025.
[132] S.Wang,Z.Long,Z.Fan,Z.Wei,andX.Huang,“Benchmarkself- [154] M. Kenney, “Ml research benchmark,” arXiv preprint
evolving:Amulti-agentframeworkfordynamicllmevaluation,” arXiv:2410.22553,2024.
arXivpreprintarXiv:2402.11443,2024.
[155] R. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, C. Kim,
[133] W. Wang, Z. Ma, P. Liu, and M. Chen, “Revisiting benchmark C.Hesse,S.Jain,V.Kosaraju,W.Saunders,X.Jiang,K.Cobbe,
andassessment:Anagent-basedexploratorydynamicevaluation T. Eloundou, G. Krueger, K. Button, M. Knight, B. Chess, and
frameworkforllms,”arXivpreprintarXiv:2410.11507,2024. J.Schulman,“Webgpt:Browser-assistedquestion-answeringwith
[134] M.Wu,T.Zhu,H.Han,C.Tan,X.Zhang,andW.Chen,“Seal-tools: humanfeedback,”2022.
Self-instructtoollearningdatasetforagenttuninganddetailed [156] Y.Qin,Z.Cai,D.Jin,L.Yan,S.Liang,K.Zhu,Y.Lin,X.Han,
benchmark,”inNLPCC. Springer,2024,pp.372–384. N. Ding, H. Wang, R. Xie, F. Qi, Z. Liu, M. Sun, and J. Zhou,
[135] Z.Guo,Y.Huang,andD.Xiong,“Ctooleval:achinesebenchmark “WebCPM:InteractivewebsearchforChineselong-formquestion
forllm-poweredagentevaluationinreal-worldapiinteractions,” answering,”inACL,A.Rogers,J.Boyd-Graber,andN.Okazaki,
inACLFindings,2024,pp.15711–15724. Eds. Toronto,Canada:AssociationforComputationalLinguistics,
[136] Y.Jiang,K.C.Black,G.Geng,D.Park,A.Y.Ng,andJ.H.Chen, Jul.2023,pp.8968–8988.
“Medagentbench: Dataset for benchmarking llms as agents in [157] K. Zhang, H. Zhang, G. Li, J. Li, Z. Li, and Z. Jin, “Toolcoder:
medicalapplications,”arXivpreprintarXiv:2501.14654,2025. Teachcodegenerationmodelstouseapisearchtools,”2023.
[137] Z. Fan, J. Tang, W. Chen, S. Wang, Z. Wei, J. Xi, F. Huang, [158] S. Robertson, H. Zaragoza et al., “The probabilistic relevance
andJ.Zhou,“Aihospital:Benchmarkinglargelanguagemodels framework: Bm25 and beyond,” Foundations and Trends® in
in a multi-agent medical interaction simulator,” arXiv preprint InformationRetrieval,vol.3,no.4,pp.333–389,2009.
arXiv:2402.09742,2024. [159] B. Lei, Y. Li, and Q. Chen, “Autocoder: Enhancing code large
[138] Y.Ma,C.Cui,X.Cao,W.Ye,P.Liu,J.Lu,A.Abdelraouf,R.Gupta, languagemodelwithAIEV-INSTRUCT,”2024.
K.Han,A.Beraetal.,“Lampilot:Anopenbenchmarkdatasetfor [160] J.Gehring,K.Zheng,J.Copet,V.Mella,Q.Carbonneaux,T.Cohen,
autonomousdrivingwithlanguagemodelprograms,”inCVPR, and G. Synnaeve, “Rlef: Grounding code llms in execution
2024,pp.15141–15151. feedbackwithreinforcementlearning,”2025.

23
[161] X.Wang,Y.Chen,L.Yuan,Y.Zhang,Y.Li,H.Peng,andH.Ji, [186] X. Chen, Y. Nie, W. Guo, and X. Zhang, “When llm meets
“Executable code actions elicit better llm agents,” ArXiv, vol. drl:Advancingjailbreakingefficiencyviadrl-guidedsearch,”in
abs/2402.01030,2024. NeurIPS,2024.
[162] T.Schick,J.Dwivedi-Yu,R.Dess`ı,R.Raileanu,M.Lomeli,E.Ham- [187] Z.Lin,W.Ma,M.Zhou,Y.Zhao,H.Wang,Y.Liu,J.Wang,and
bro,L.Zettlemoyer,N.Cancedda,andT.Scialom,“Toolformer: L.Li,“Pathseeker:Exploringllmsecurityvulnerabilitieswitha
Languagemodelscanteachthemselvestousetools,”Advancesin reinforcementlearning-basedjailbreakapproach,”arXivpreprint
NeuralInformationProcessingSystems,vol.36,pp.68539–68551, arXiv:2409.14177,2024.
2023. [188] Y.Zeng,Y.Wu,X.Zhang,H.Wang,andQ.Wu,“Autodefense:
[163] B.Paranjape,S.Lundberg,S.Singh,H.Hajishirzi,L.Zettlemoyer, Multi-agentllmdefenseagainstjailbreakattacks,”arXivpreprint
andM.T.Ribeiro,“Art:Automaticmulti-stepreasoningandtool- arXiv:2403.04783,2024.
useforlargelanguagemodels,”arXivpreprintarXiv:2303.09014, [189] S.Barua,M.Rahman,M.J.Sadek,R.Islam,S.Khaled,andA.Kabir,
2023. “Guardiansoftheagenticsystem:Preventingmanyshotsjailbreak
[164] Y.Song,W.Xiong,D.Zhu,W.Wu,H.Qian,M.Song,H.Huang, withagenticsystem,”arXivpreprintarXiv:2502.16750,2025.
C.Li,K.Wang,R.Yao,Y.Tian,andS.Li,“Restgpt:Connecting [190] Z.Ni,H.Wang,andH.Wang,“Shieldlearner:Anewparadigmfor
largelanguagemodelswithreal-worldrestfulapis,”2023. jailbreakattackdefenseinllms,”arXivpreprintarXiv:2502.13162,
[165] A.Saha,L.Mandal,B.Ganesan,S.Ghosh,R.Sindhgatta,C.Eber- 2025.
hardt, D. Debrunner, and S. Mehta, “Sequential API function [191] P.Zhu,Z.Zhou,Y.Zhang,S.Yan,K.Wang,andS.Su,“Demona-
calling using GraphQL schema,” in EMNLP, Y. Al-Onaizan, gent:Dynamicallyencryptedmulti-backdoorimplantationattack
M.Bansal,andY.-N.Chen,Eds.,Miami,Florida,USA,Nov.2024, onllm-basedagent,”arXivpreprintarXiv:2502.12575,2025.
pp.19452–19458. [192] W.Yang,X.Bi,Y.Lin,S.Chen,J.Zhou,andX.Sun,“Watchoutfor
[166] L.Yuan,Y.Chen,X.Wang,Y.R.Fung,H.Peng,andH.Ji,“Craft: youragents!investigatingbackdoorthreatstollm-basedagents,”
Customizing llms by creating and retrieving from specialized NeurIPS,vol.37,pp.100938–100964,2025.
toolsets,”arXivpreprintarXiv:2309.17428,2023. [193] Y. Wang, D. Xue, S. Zhang, and S. Qian, “Badagent: Inserting
[167] C.Qian,C.Xiong,Z.Liu,andZ.Liu,“Toolink:Linkingtoolkit andactivatingbackdoorattacksinllmagents,”inACL,2024,pp.
creation and using through chain-of-solving on open-source 9811–9827.
model,”inNAACL,2024,pp.831–854. [194] T.Tong,F.Wang,Z.Zhao,andM.Chen,“Badjudge:Backdoor
[168] C.Qian,C.Han,Y.Fung,Y.Qin,Z.Liu,andH.Ji,“CREATOR: vulnerabilitiesofllm-as-a-judge,”inICLR,2025.
Toolcreationfordisentanglingabstractandconcretereasoningof [195] Z. Guo and R. Tourani, “Darkmind: Latent chain-of-thought
largelanguagemodels,”inEMNLPFindings,H.Bouamor,J.Pino, backdoor in customized llms,” arXiv preprint arXiv:2501.18617,
andK.Bali,Eds.,Singapore,Dec.2023,pp.6922–6939. 2025.
[169] T.Cai,X.Wang,T.Ma,X.Chen,andD.Zhou,“Largelanguage [196] Z. Zhou, Z. Li, J. Zhang, Y. Zhang, K. Wang, Y. Liu, and
modelsastoolmakers,”2024. Q.Guo,“Corba:Contagiousrecursiveblockingattacksonmulti-
[170] “LangChain,”12023.[Online].Available:https://github.com/ agentsystemsbasedonlargelanguagemodels,”arXivpreprint
langchain-ai/langchain arXiv:2502.14529,2025.
[171] “LlamaIndex,”112022.[Online].Available:https://github.com/ [197] P.He,Y.Lin,S.Dong,H.Xu,Y.Xing,andH.Liu,“Red-teamingllm
jerryjliu/llama index multi-agentsystemsviacommunicationattacks,”arXivpreprint
arXiv:2502.14847,2025.
[172] “Dify,” 5 2023. [Online]. Available: https://github.com/
[198] M.Yu,S.Wang,G.Zhang,J.Mao,C.Yin,Q.Liu,Q.Wen,K.Wang,
langgenius/dify
andY.Wang,“Netsafe:Exploringthetopologicalsafetyofmulti-
[173] “Ollama,” 7 2023. [Online]. Available: https://github.com/
agentnetworks,”arXivpreprintarXiv:2410.15686,2024.
ollama/ollama
[199] S.Wang,G.Zhang,M.Yu,G.Wan,F.Meng,C.Guo,K.Wang,
[174] “MCPAgent,”22025.[Online].Available:https://github.com/
and Y. Wang, “G-safeguard: A topology-guided security lens
lastmile-ai/mcp-agent
andtreatmentonllm-basedmulti-agentsystems,”arXivpreprint
[175] A.Li,Y.Zhou,V.C.Raghuram,T.Goldstein,andM.Goldblum,
arXiv:2502.11127,2025.
“Commercial llm agents are already vulnerable to simple yet
[200] W.Hua,X.Yang,M.Jin,Z.Li,W.Cheng,R.Tang,andY.Zhang,
dangerousattacks,”arXivpreprintarXiv:2502.08586,2025.
“Trustagent: Towards safe and trustworthy llm-based agents
[176] W.Zhang,K.Tang,H.Wu,M.Wang,Y.Shen,G.Hou,Z.Tan, throughagentconstitution,”inEMNLPFindings,2024.
P. Li, Y. Zhuang, and W. Lu, “Agent-pro: Learning to evolve
[201] Z. Zhang, Y. Zhang, L. Li, H. Gao, L. Wang, H. Lu, F. Zhao,
viapolicy-levelreflectionandoptimization,”inACL,2024,pp.
Y.Qiao,andJ.Shao,“Psysafe:Acomprehensiveframeworkfor
5348–5375.
psychological-basedattack,defense,andevaluationofmulti-agent
[177] L.Mo,Z.Liao,B.Zheng,Y.Su,C.Xiao,andH.Sun,“Atrembling systemsafety,”arXivpreprintarXiv:2401.11880,2024.
house of cards? mapping adversarial attacks against language
[202] Z.Deng,Y.Guo,C.Han,W.Ma,J.Xiong,S.Wen,andY.Xiang,
agents,”arXivpreprintarXiv:2402.10196,2024.
“Aiagentsunderthreat:Asurveyofkeysecuritychallengesand
[178] E.Debenedetti,J.Zhang,M.Balunovic,L.Beurer-Kellner,M.Fis- futurepathways,”ACMComputingSurveys,2024.
cher, and F. Tramer, “Agentdojo: A dynamic environment to
[203] E.Debenedetti,J.Zhang,M.Balunovic,L.Beurer-Kellner,M.Fis-
evaluatepromptinjectionattacksanddefensesforllmagents,”in
cher, and F. Trame`r, “Agentdojo: A dynamic environment to
NeurIPS,vol.37,2024,pp.82895–82920.
evaluatepromptinjectionattacksanddefensesforllmagents,”
[179] C.H.Wu,J.Y.Koh,R.Salakhutdinov,D.Fried,andA.Raghu- NeurIPS,vol.37,pp.82895–82920,2025.
nathan,“Adversarialattacksonmultimodalagents,”arXivpreprint [204] X.Li,Z.Li,Y.Kosuga,Y.Yoshida,andV.Bian,“Targetingthe
arXiv:2406.12814,2024. core:Asimpleandeffectivemethodtoattackrag-basedagentsvia
[180] L.-b.Ning,S.Wang,W.Fan,Q.Li,X.Xu,H.Chen,andF.Huang, directllmmanipulation,”arXivpreprintarXiv:2412.04415,2024.
“Cheatagent:Attackingllm-empoweredrecommendersystemsvia [205] Q.Zhan,Z.Liang,Z.Ying,andD.Kang,“Injecagent:Benchmark-
llmagent,”inKDD,2024,pp.2284–2295. ingindirectpromptinjectionsintool-integratedlargelanguage
[181] W. Yu, K. Hu, T. Pang, C. Du, M. Lin, and M. Fredrikson, modelagents,”arXivpreprintarXiv:2403.02691,2024.
“Infecting llm agents via generalizable adversarial attack,” in [206] D.Pasquini,E.M.Kornaropoulos,andG.Ateniese,“Hackingback
NeurIPSWorkshop,2024. theai-hacker:Promptinjectionasadefenseagainstllm-driven
[182] G.LinandQ.Zhao,“Largelanguagemodelsentinel:Llmagent cyberattacks,”arXivpreprintarXiv:2410.20911,2024.
foradversarialpurification,”arXivpreprintarXiv:2405.20770,2024. [207] S.Abdelnabi,A.Gomaa,E.Bagdasarian,P.O.Kristensson,and
[183] S.Chern,Z.Fan,andA.Liu,“Combatingadversarialattackswith R.Shokri,“Firewallstosecuredynamicllmagenticnetworks,”
multi-agentdebate,”arXivpreprintarXiv:2401.05998,2024. arXivpreprintarXiv:2502.01822,2025.
[184] X.Wang,J.Peng,K.Xu,H.Yao,andT.Chen,“Reinforcement [208] P. Y. Zhong, S. Chen, R. Wang, M. McCall, B. L. Titzer, and
learning-drivenllmagentforautomatedattacksonllms,”inACL H.Miller,“Rtbas:Defendingllmagentsagainstpromptinjection
Findings,2024,pp.170–177. andprivacyleakage,”arXivpreprintarXiv:2502.08966,2025.
[185] Y. Dong, Z. Li, X. Meng, N. Yu, and S. Guo, “Jailbreaking [209] F. Jia, T. Wu, X. Qin, and A. Squicciarini, “The task shield:
text-to-image models with llm-based agents,” arXiv preprint Enforcing task alignment to defend against indirect prompt
arXiv:2408.00523,2024. injectioninllmagents,”arXivpreprintarXiv:2412.16682,2024.

24
[210] Y.Tian,X.Yang,J.Zhang,Y.Dong,andH.Su,“Evilgeniuses: [233] N.Kandpal,E.Wallace,andC.Raffel,“Deduplicatingtraining
Delving into the safety of llm-based agents,” arXiv preprint datamitigatesprivacyrisksinlanguagemodels,”inICML. PMLR,
arXiv:2311.11855,2023. 2022,pp.10697–10707.
[211] C.Wang,Q.Long,X.Meng,X.Cai,C.Wu,Z.Meng,X.Wang,and [234] S.Kim,S.Yun,H.Lee,M.Gubri,S.Yoon,andS.J.Oh,“Propile:
Y.Zhou,“Biorag:Arag-llmframeworkforbiologicalquestion Probing privacy leakage in large language models,” NeurIPS,
reasoning,”arXivpreprintarXiv:2408.01107,2024. vol.36,pp.20750–20762,2023.
[212] Y.Gan,Y.Yang,Z.Ma,P.He,R.Zeng,Y.Wang,Q.Li,C.Zhou, [235] K.Krishna,G.S.Tomar,A.P.Parikh,N.Papernot,andM.Iyyer,
S.Li,T.Wangetal.,“Navigatingtherisks:Asurveyofsecurity, “Thievesonsesamestreet!modelextractionofbert-basedapis,”
privacy, and ethics threats in llm-based agents,” arXiv preprint arXivpreprintarXiv:1910.12366,2019.
arXiv:2411.09523,2024. [236] A.Naseh,K.Krishna,M.Iyyer,andA.Houmansadr,“Stealing
[213] Z.Xiang,Y.Zeng,M.Kang,C.Xu,J.Zhang,Z.Yuan,Z.Chen, thedecodingalgorithmsoflanguagemodels,”inACMSIGSAC,
C.Xie,F.Jiang,M.Panetal.,“Clas2024:Thecompetitionforllm 2023,pp.1835–1849.
andagentsafety,”inNeurIPSWorkshop,2024. [237] Z.Li,C.Wang,P.Ma,C.Liu,S.Wang,D.Wu,C.Gao,andY.Liu,
[214] F.Wu,S.Wu,Y.Cao,andC.Xiao,“Wipi:Anewwebthreatfor “On extracting specialized code abilities from large language
llm-drivenwebagents,”arXivpreprintarXiv:2402.16965,2024. models:Afeasibilitystudy,”inICSE,2024,pp.1–13.
[215] I.Nakash,G.Kour,G.Uziel,andA.Anaby-Tavor,“Breakingreact [238] J.Kirchenbauer,J.Geiping,Y.Wen,J.Katz,I.Miers,andT.Gold-
agents: Foot-in-the-door attack will get you in,” arXiv preprint stein,“Awatermarkforlargelanguagemodels,”inICML. PMLR,
arXiv:2410.16950,2024. 2023,pp.17061–17084.
[216] Z. Chen, Z. Xiang, C. Xiao, D. Song, and B. Li, “Agentpoison: [239] Y.Lin,Z.Gao,H.Du,D.Niyato,J.Kang,Z.Xiong,andZ.Zheng,
Red-teaming llm agents via poisoning memory or knowledge “Blockchain-basedefficientandtrustworthyaigcservicesinmeta-
bases,”NeurIPS,vol.37,pp.130185–130213,2025. verse,”IEEETransactionsonServicesComputing,2024.
[217] B.Wang,W.He,P.He,S.Zeng,Z.Xiang,Y.Xing,andJ.Tang, [240] X.Shen,Y.Qu,M.Backes,andY.Zhang,“Promptstealingattacks
“Unveiling privacy risks in llm agent memory,” arXiv preprint against{Text-to-Image}generationmodels,”inUSENIX,2024,
arXiv:2502.13172,2025.
pp.5823–5840.
[218] E.T.Red,“Maliciouschatgptagents:Howgptscanquietlygrab
[241] Z. Sha and Y. Zhang, “Prompt stealing attacks against large
yourdata(demo),”EmbraceTheRed,2023.
languagemodels,”arXivpreprintarXiv:2402.12959,2024.
[219] Y. Li, H. Wen, W. Wang, X. Li, Y. Yuan, G. Liu, J. Liu, W. Xu,
[242] B.Hui,H.Yuan,N.Gong,P.Burlina,andY.Cao,“Pleak:Prompt
X.Wang,Y.Sunetal.,“Personalllmagents:Insightsandsurvey
leakingattacksagainstlargelanguagemodelapplications,”in
about the capability, efficiency and security,” arXiv preprint
ACMSIGSAC,2024,pp.3600–3614.
arXiv:2401.05459,2024.
[243] R.Bommasani,D.A.Hudson,E.Adeli,R.Altman,S.Arora,S.von
[220] X. Gu, X. Zheng, T. Pang, C. Du, Q. Liu, Y. Wang, J. Jiang,
Arx,M.S.Bernstein,J.Bohg,A.Bosselut,E.Brunskilletal.,“On
and M. Lin, “Agent smith: A single image can jailbreak one
theOpportunitiesandRisksofFoundationModels,”arXivpreprint
millionmultimodalllmagentsexponentiallyfast,”arXivpreprint
arXiv:2108.07258,2021.
arXiv:2402.08567,2024.
[244] L.FloridiandM.Chiriatti,“GPT-3:ItsNature,Scope,Limits,and
[221] D.LeeandM.Tiwari,“Promptinfection:Llm-to-llmpromptinjec-
Consequences,”MindsandMachines,vol.30,pp.681–694,2020.
tionwithinmulti-agentsystems,”arXivpreprintarXiv:2410.07283,
[245] H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux,
2024.
T. Lacroix, B. Rozie`re, N. Goyal, E. Hambro, F. Azhar et al.,
[222] B. Chen, G. Li, X. Lin, Z. Wang, and J. Li, “Blockagents: To-
“LLaMA:OpenandEfficientFoundationLanguageModels,”arXiv
wardsbyzantine-robustllm-basedmulti-agentcoordinationvia
preprintarXiv:2302.13971,2023.
blockchain,”inACMTuringAwardCelebrationConference,2024,pp.
187–192. [246] P.TadasandS.Agarmore,“RedefiningWorkintheAgeofAI:
ChallengesandPathwaystoOpportunities,”inSPICES. IEEE,
[223] M.Andriushchenko,A.Souly,M.Dziemian,D.Duenas,M.Lin,
2024,pp.1–5.
J.Wang,D.Hendrycks,A.Zou,Z.Kolter,M.Fredriksonetal.,
“Agentharm: A benchmark for measuring harmfulness of llm [247] S.Moore,R.Tong,A.Singh,Z.Liu,X.Hu,Y.Lu,J.Liang,C.Cao,
agents,”arXivpreprintarXiv:2410.09024,2024. H.Khosravi,P.Dennyetal.,“EmpoweringEducationwithLLMs-
TheNext-GenInterfaceandContentGeneration,”inInternational
[224] N.Carlini,F.Tramer,E.Wallace,M.Jagielski,A.Herbert-Voss,
ConferenceonArtificialIntelligenceinEducation. Springer,2023,pp.
K. Lee, A. Roberts, T. Brown, D. Song, U. Erlingsson et al.,
32–37.
“Extractingtrainingdatafromlargelanguagemodels,”inUSENIX,
2021,pp.2633–2650. [248] S.Liu,Y.Jin,C.Li,D.F.Wong,Q.Wen,L.Sun,H.Chen,X.Xie,
[225] N. Carlini, D. Ippolito, M. Jagielski, K. Lee, F. Tramer, and andJ.Wang,“Culturevlm:Characterizingandimprovingcultural
C. Zhang, “Quantifying memorization across neural language understandingofvision-languagemodelsforover100countries,”
models,”inICLR,2022. arXiv:2501.01282,2025.
[226] J.Huang,H.Shao,andK.C.-C.Chang,“Arelargepre-trained [249] P.Henderson,X.Li,D.Jurafsky,T.Hashimoto,M.A.Lemley,and
language models leaking your personal information?” arXiv P.Liang,“FoundationModelsandFairUse,”JMLR,vol.24,no.
preprintarXiv:2205.12628,2022. 400,pp.1–79,2023.
[227] F. Mireshghallah, K. Goyal, A. Uniyal, T. Berg-Kirkpatrick, [250] M.A.LemleyandB.Casey,“FairLearning,”Tex.L.Rev.,vol.99,
andR.Shokri,“Quantifyingprivacyrisksofmaskedlanguage p.743,2020.
models using membership inference attacks,” arXiv preprint [251] S.Oh,Y.Jin,M.Sharma,D.Kim,E.Ma,G.Verma,andS.Kumar,
arXiv:2203.03929,2022. “Uniguard: Towards universal safety guardrails for jailbreak
[228] W.Fu,H.Wang,C.Gao,G.Liu,Y.Li,andT.Jiang,“Practicalmem- attacksonmultimodallargelanguagemodels,”arXiv:2411.01703,
bershipinferenceattacksagainstfine-tunedlargelanguagemodels 2024.
viaself-promptcalibration,”arXivpreprintarXiv:2311.06062,2023. [252] E.M.Bender,T.Gebru,A.McMillan-Major,andS.Shmitchell,
[229] S.Hoory,A.Feder,A.Tendler,S.Erell,A.Peled-Cohen,I.Laish, “OntheDangersofStochasticParrots:CanLanguageModelsBe
H.Nakhost,U.Stemmer,A.Benjamini,A.Hassidimetal.,“Learn- TooBig?”inFAccT,2021,pp.610–623.
ingandevaluatingadifferentiallyprivatepre-trainedlanguage [253] M.Brundage,S.Avin,J.Wang,H.Belfield,G.Krueger,G.Hadfield,
model,”inEMNLPFindings,2021,pp.1178–1189. H.Khlaaf,J.Yang,H.Toner,R.Fongetal.,“TowardTrustworthy
[230] M. Kang, S. Lee, J. Baek, K. Kawaguchi, and S. J. Hwang, AIDevelopment:MechanismsforSupportingVerifiableClaims,”
“Knowledge-augmentedreasoningdistillationforsmalllanguage arXivpreprintarXiv:2004.07213,2020.
modelsinknowledge-intensivetasks,”NeurIPS,vol.36,pp.48573– [254] D.Ganguli,D.Hernandez,L.Lovitt,A.Askell,Y.Bai,A.Chen,
48602,2023. T.Conerly,N.Dassarma,D.Drain,N.Elhageetal.,“Predictability
[231] X.Pan,M.Zhang,S.Ji,andM.Yang,“Privacyrisksofgeneral- andSurpriseinLargeGenerativeModels,”inFAccT,2022,pp.
purposelanguagemodels,”inIEEESymposiumonSecurityand 1747–1764.
Privacy(SP). IEEE,2020,pp.1314–1331. [255] C.Deng,Y.Duan,X.Jin,H.Chang,Y.Tian,H.Liu,H.P.Zou,
[232] L.Wang,J.Wang,J.Wan,L.Long,Z.Yang,andZ.Qin,“Property Y.Jin,Y.Xiao,Y.Wangetal.,“DeconstructingTheEthicsofLarge
existenceinferenceagainstgenerativemodels,”inUSENIX,2024, LanguageModelsfromLong-standingIssuestoNew-emerging
pp.2423–2440. Dilemmas:ASurvey,”arXive-prints,pp.arXiv–2406,2024.

25
[256] I.Shumailov,Z.Shumaylov,Y.Zhao,N.Papernot,R.Anderson, [277] X.Cai,C.Wang,Q.Long,Y.Zhou,andM.Xiao,“Knowledgehi-
and Y. Gal, “AI models collapse when trained on recursively erarchyguidedbiological-medicaldatasetdistillationfordomain
generateddata,”Nature,vol.631,no.8022,pp.755–759,2024. llmtraining,”arXivpreprintarXiv:2501.15108,2025.
[257] L.Weidinger,J.Mellor,M.Rauh,C.Griffin,J.Uesato,P.-S.Huang, [278] Z. Chen, C. Hu, M. Wu, Q. Long, X. Wang, Y. Zhou, and
M. Cheng, M. Glaese, B. Balle, A. Kasirzadeh et al., “Ethical M.Xiao,“Genesum:Largelanguagemodel-basedgenesummary
andsocialrisksofharmfromLanguageModels,”arXivpreprint extraction,”in2024IEEEInternationalConferenceonBioinformatics
arXiv:2112.04359,2021. andBiomedicine(BIBM). IEEE,2024,pp.1438–1443.
[258] Y. Xiao, Y. Jin, Y. Bai, Y. Wu, X. Yang, X. Luo, W. Yu, X. Zhao, [279] K. Keshavjee, J. Bosomworth, J. Copen, J. Lai, B. Kucukyazici,
Y.Liu,Q.Guetal.,“Largelanguagemodelscanbecontextual R.Lilani,andA.M.Holbrook,“Bestpracticesinemrimplementa-
privacyprotectionlearners,”inEMNLP,2024,pp.14179–14201. tion:asystematicreview,”inAMIAAnnualSymposiumProceedings,
vol.2006,2006,p.982.
[259] D.A.Alber,Z.Yang,A.Alyakin,E.Yang,S.Rai,A.A.Valliani,
J.Zhang,G.R.Rosenbaum,A.K.Amend-Thomas,D.B.Kurland [280] X. Ye, M. Xiao, Z. Ning, W. Dai, W. Cui, Y. Du, and Y. Zhou,
et al., “Medical large language models are vulnerable to data- “Needed: Introducing hierarchical transformer to eye diseases
poisoningattacks,”NatureMedicine,pp.1–9,2025. diagnosis,”inProceedingsofthe2023SIAMInternationalConference
onDataMining(SDM). SIAM,2023,pp.667–675.
[260] Y.Jin,X.Wang,R.Yang,Y.Sun,W.Wang,H.Liao,andX.Xie,
[281] J.Li,Y.Lai,W.Li,J.Ren,M.Zhang,X.Kang,S.Wang,P.Li,Y.-Q.
“Towardsfine-grainedreasoningforfakenewsdetection,”inAAAI,
Zhang,W.Maetal.,“Agenthospital:Asimulacrumofhospital
vol.36,no.5,2022,pp.5746–5754.
withevolvablemedicalagents,”arXivpreprintarXiv:2405.02957,
[261] T.Shen,R.Jin,Y.Huang,C.Liu,W.Dong,Z.Guo,X.Wu,Y.Liu,
2024.
andD.Xiong,“LargeLanguageModelAlignment:ASurvey,”
[282] W. Yan, H. Liu, T. Wu, Q. Chen, W. Wang, H. Chai, J. Wang,
arXivpreprintarXiv:2309.15025,2023.
W.Zhao,Y.Zhang,R.Zhangetal.,“Clinicallab:Aligningagents
[262] A. S. Luccioni, S. Viguier, and A.-L. Ligozat, “Estimating the
for multi-departmental clinical diagnostics in the real world,”
CarbonFootprintofBLOOM,a176BParameterLanguageModel,” arXivpreprintarXiv:2406.13890,2024.
JMLR,vol.24,no.253,pp.1–15,2023.
[283] H. Yu, J. Zhou, L. Li, S. Chen, J. Gallifant, A. Shi, X. Li,
[263] E. Strubell, A. Ganesh, and A. McCallum, “Energy and Policy W.Hua,M.Jin,G.Chen,Y.Zhou,Z.Li,T.Gupte,M.-L.Chen,
Considerations for Deep Learning in NLP,” in AAAI, vol. 34, Z. Azizi, Y. Zhang, T. L. Assimes, X. Ma, D. S. Bitterman,
no.09,2020,pp.13693–13696. L. Lu, and L. Fan, “Aipatient: Simulating patients with ehrs
[264] J. Zhou, “Awesome ai agents for scien- andllmpoweredagenticworkflow,”2024.[Online].Available:
tific discovery,” https://github.com/zhoujieli/ https://arxiv.org/abs/2409.18924
Awesome-LLM-Agents-Scientific-Discovery,2024. [284] N.Sharma,“Cxr-agent:Vision-languagemodelsforchestx-ray
[265] AAAI,“Aaai2025presidentialpanel:Futureofairesearch,”2025. interpretationwithuncertaintyawareradiologyreporting,”arXiv
[Online].Available:https://aaai.org/wp-content/uploads/2025/ preprintarXiv:2407.08811,2024.
03/AAAI-2025-PresPanel-Report-FINAL.pdf [285] A.Fallahpour,J.Ma,A.Munim,H.Lyu,andB.Wang,“Medrax:
[266] A. Ghafarollahi and M. J. Buehler, “Sciagents: Automating Medicalreasoningagentforchestx-ray,”2025.[Online].Available:
scientificdiscoverythroughbioinspiredmulti-agentintelligent https://arxiv.org/abs/2502.02673
graph reasoning,” Advanced Materials, vol. n/a, no. n/a, p. [286] R. W. Lee, K. H. Lee, J. S. Yun, M. S. Kim, and H. S. Choi,
2413523. [Online]. Available: https://advanced.onlinelibrary. “Comparativeanalysisofm4cxr,anllm-basedchestx-rayreport
wiley.com/doi/abs/10.1002/adma.202413523 generation model, and chatgpt in radiological interpretation,”
[267] P.T.J.Kon,J.Liu,Q.Ding,Y.Qiu,Z.Yang,Y.Huang,J.Srinivasa, JournalofClinicalMedicine,vol.13,no.23,p.7057,2024.
M.Lee,M.Chowdhury,andA.Chen,“Curie:Towardrigorous [287] X.Feng,Y.Luo,Z.Wang,H.Tang,M.Yang,K.Shao,D.Mguni,
andautomatedscientificexperimentationwithaiagents,”2025. Y. Du, and J. Wang, “Chessgpt: Bridging policy learning and
[Online].Available:https://arxiv.org/abs/2502.16069 languagemodeling,”inNeurIPS,2023,pp.7216–7262.
[268] Y.Jin,Q.Zhao,Y.Wang,H.Chen,K.Zhu,Y.Xiao,andJ.Wang, [288] T. Carta, C. Romac, T. Wolf, S. Lamprier, O. Sigaud, and P.-
“Agentreview:Exploringpeerreviewdynamicswithllmagents,” Y. Oudeyer, “Grounding large language models in interactive
inEMNLP,2024,pp.1208–1226. environmentswithonlinereinforcementlearning,”inICML,2023,
pp.3676–3713.
[269] A. M. Bran, S. Cox, O. Schilter, C. Baldassari, A. D. White,
[289] A. Zhu, L. Martin, A. Head, and C. Callison-Burch, “Calypso:
and P. Schwaller, “Chemcrow: Augmenting large-language
Llmsasdungeonmaster’sassistants,”inAAAI,2023,pp.380–390.
models with chemistry tools,” 2023. [Online]. Available:
https://arxiv.org/abs/2304.05376 [290] D.Chen,H.Wang,Y.Huo,Y.Li,andH.Zhang,“Gamegpt:Multi-
agent collaborative framework for game development,” arXiv
[270] A. Ghafarollahi and M. J. Buehler, “Atomagents: Alloy
preprintarXiv:2310.08067,2023.
design and discovery through physics-aware multi-modal
[291] Y.Sun,Z.Li,K.Fang,C.H.Lee,andA.Asadipour,“Languageas
multi-agent artificial intelligence,” 2024. [Online]. Available:
reality:aco-creativestorytellinggameexperiencein1001nights
https://arxiv.org/abs/2407.10022
usinggenerativeai,”inAAAI,2023,pp.425–434.
[271] D. Kostunin, V. Sotnikov, S. Golovachev, and A. Strube, “Ai
[292] N.Li,C.Gao,M.Li,Y.Li,andQ.Liao,“Econagent:largelan-
agents for ground-based gamma astronomy,” 2025. [Online].
guagemodel-empoweredagentsforsimulatingmacroeconomic
Available:https://arxiv.org/abs/2503.00821
activities,”ACL,pp.15523–15536,2024.
[272] B. Qi, K. Zhang, K. Tian, H. Li, Z.-R. Chen, S. Zeng, E. Hua,
[293] Y. Li, Y. Yu, H. Li, Z. Chen, and K. Khashanah, “Tradinggpt:
H.Jinfang,andB.Zhou,“Largelanguagemodelsasbiomedical
Multi-agent system with layered memory and distinct charac-
hypothesis generators: A comprehensive evaluation,” 2024.
tersforenhancedfinancialtradingperformance,”arXivpreprint
[Online].Available:https://arxiv.org/abs/2407.08940
arXiv:2309.03736,2023.
[273] Y.Roohani,A.Lee,Q.Huang,J.Vora,Z.Steinhart,K.Huang, [294] Q.Zhao,J.Wang,Y.Zhang,Y.Jin,K.Zhu,H.Chen,andX.Xie,
A. Marson, P. Liang, and J. Leskovec, “Biodiscoveryagent: An “Competeai:Understandingthecompetitiondynamicsinlarge
aiagentfordesigninggeneticperturbationexperiments,”arXiv languagemodel-basedagents,”inICML,2024,pp.61092–61107.
preprintarXiv:2405.17631,2024. [295] Z.Ma,Y.Mei,andZ.Su,“Understandingthebenefitsandchal-
[274] Z.Wang,Q.Jin,C.-H.Wei,S.Tian,P.-T.Lai,Q.Zhu,C.-P.Day, lengesofusinglargelanguagemodel-basedconversationalagents
C.Ross,andZ.Lu,“Geneagent:Self-verificationlanguageagent for mental well-being support,” in AMIA Annual Symposium
forgenesetknowledgediscoveryusingdomaindatabases,”2024. Proceedings,vol.2023,2024,p.1105.
[Online].Available:https://arxiv.org/abs/2405.16205 [296] J.Zhang,X.Xu,N.Zhang,R.Liu,B.Hooi,andS.Deng,“Exploring
[275] M.Xiao,W.Zhang,X.Huang,H.Zhu,M.Wu,X.Li,andY.Zhou, collaboration mechanisms for llm agents: A social psychology
“Knowledge-guidedbiomarkeridentificationforlabel-freesingle- view,”inACL,2024,pp.14544–14607.
cellrna-seqdata:Areinforcementlearningperspective,”arXiv [297] G.V.Aher,R.I.Arriaga,andA.T.Kalai,“Usinglargelanguage
preprintarXiv:2501.04718,2025. modelstosimulatemultiplehumansandreplicatehumansubject
[276] Y. Sun, Y. Zhang, Y. Si, C. Zhu, Z. Shui, K. Zhang, J. Li, studies,”inICML,2023,pp.337–371.
X.Lyu,T.Lin,andL.Yang,“Pathgen-1.6m:1.6millionpathology [298] R.Liu,R.Yang,C.Jia,G.Zhang,D.Zhou,A.M.Dai,D.Yang,
image-textpairsgenerationthroughmulti-agentcollaboration,” andS.Vosoughi,“Trainingsociallyalignedlanguagemodelson
2024.[Online].Available:https://arxiv.org/abs/2407.00203 simulatedsocialinteractions,”inICLR,2024.

26
[299] C.Gao,X.Lan,Z.Lu,J.Mao,J.Piao,H.Wang,D.Jin,andY.Li, [323] K.Zhu,J.Chen,J.Wang,N.Z.Gong,D.Yang,andX.Xie,“Dyval:
“S3:Social-networksimulationsystemwithlargelanguagemodel- Dynamicevaluationoflargelanguagemodelsforreasoningtasks,”
empoweredagents,”arXivpreprintarXiv:2307.14984,2023. inICLR,2024.
[300] Y. Dong, X. Jiang, Z. Jin, and G. Li, “Self-collaboration code [324] K.Zhu,J.Wang,Q.Zhao,R.Xu,andX.Xie,“Dynamicevaluation
generationviachatgpt,”ACMTransactionsonSoftwareEngineering of large language models by meta probing agents,” in ICML.
andMethodology,vol.33,no.7,pp.1–38,2024. PMLR,2024,pp.62599–62617.
[301] C.Qian,X.Cong,C.Yang,W.Chen,Y.Su,J.Xu,Z.Liu,andM.Sun, [325] X.Yi,J.Yao,X.Wang,andX.Xie,“Unpackingtheethicalvalue
“Chatdev:Communicativeagentsforsoftwaredevelopment,”in alignmentinbigmodels,”arXivpreprintarXiv:2310.17551,2023.
ACL,2024,pp.15174–15186. [326] X.Wang,L.Jiang,J.Hernandez-Orallo,D.Stillwell,L.Sun,F.Luo,
andX.Xie,“Evaluatinggeneral-purposeaiwithpsychometrics,”
[302] A. Zhang, Y. Chen, L. Sheng, X. Wang, and T.-S. Chua, “On
arXivpreprintarXiv:2310.16379,2023.
generativeagentsinrecommendation,”inSIGIR,2024,pp.1807–
[327] Y. Wu, Z. Jiang, A. Khan, Y. Fu, L. Ruis, E. Grefenstette, and
1817.
T.Rockta¨schel,“Chatarena:Multi-agentlanguagegameenviron-
[303] J.Zhang,Y.Hou,R.Xie,W.Sun,J.McAuley,W.X.Zhao,L.Lin,
mentsforlargelanguagemodels,”2023.
andJ.-R.Wen,“Agentcf:Collaborativelearningwithautonomous
[328] J.Yao,X.Yi,Y.Gong,X.Wang,andX.Xie,“Valuefulcra:Mapping
languageagentsforrecommendersystems,”inWWW,2024,pp.
largelanguagemodelstothemultidimensionalspectrumofbasic
3679–3689.
humanvalue,”inNAACL,2024,pp.8754–8777.
[304] Z.Wang,Y.Yu,W.Zheng,W.Ma,andM.Zhang,“Macrec:A
[329] V.C.Nguyen,M.Taher,D.Hong,V.K.Possobom,V.T.Gopalakr-
multi-agent collaboration framework for recommendation,” in
ishnan, E. Raj, Z. Li, H. J. Soled, M. L. Birnbaum, S. Kumar
SIGIR,2024,pp.2760–2764.
etal.,“Dolargelanguagemodelsalignwithcorementalhealth
[305] Y. Wang, Z. Jiang, Z. Chen, F. Yang, Y. Zhou, E. Cho, X. Fan, counselingcompetencies?”inNAACL,2025.
X. Huang, Y. Lu, and Y. Yang, “Recmind: Large language
model powered agent for recommendation,” arXiv preprint
arXiv:2308.14296,2023.
[306] C.Qian,Z.Xie,Y.Wang,W.Liu,Y.Dang,Z.Du,W.Chen,C.Yang,
Z.Liu,andM.Sun,“Scalinglarge-language-model-basedmulti-
agentcollaboration,”arXiv:2406.07155,2024.
[307] C.-M.Chan,W.Chen,Y.Su,J.Yu,W.Xue,S.Zhang,J.Fu,and
Z.Liu,“Chateval:Towardsbetterllm-basedevaluatorsthrough
multi-agentdebate,”arXivpreprintarXiv:2308.07201,2023.
[308] O. F. Rana and K. Stout, “What is scalability in multi-agent
systems?” in Proceedings of the fourth international conference on
Autonomousagents,2000,pp.56–63.
[309] R. Deters, “Scalable multi-agent systems,” in Proceedings of the
2001jointACM-ISCOPEconferenceonJavaGrande,2001,p.182.
[310] G. Verma, R. Kaur, N. Srishankar, Z. Zeng, T. Balch, and
M.Veloso,“Adaptagent:Adaptingmultimodalwebagentswith
few-shotlearningfromhumandemonstrations,”arXivpreprint
arXiv:2411.13451,2024.
[311] Y. Jin, M. Choi, G. Verma, J. Wang, and S. Kumar, “Mm-soc:
Benchmarkingmultimodallargelanguagemodelsinsocialmedia
platforms,”inACLFindings,2024.
[312] Z. Yao, Z. Tang, J. Lou, P. Shen, and W. Jia, “Velo: A vector
database-assistedcloud-edgecollaborativellmqosoptimization
framework,”inICWS. IEEE,2024,pp.865–876.
[313] X.Cheng,X.Wang,X.Zhang,T.Ge,S.-Q.Chen,F.Wei,H.Zhang,
andD.Zhao,“xrag:Extremecontextcompressionforretrieval-
augmentedgenerationwithonetoken,”inNeurIPS,2024.
[314] Y. Jin, M. Chandra, G. Verma, Y. Hu, M. De Choudhury, and
S.Kumar,“Bettertoaskinenglish:Cross-lingualevaluationof
largelanguagemodelsforhealthcarequeries,”inWWW,2024,pp.
2627–2638.
[315] V.Agarwal,Y.Jin,M.Chandra,M.DeChoudhury,S.Kumar,and
N.Sastry,“Medhalu:Hallucinationsinresponsestohealthcare
queriesbylargelanguagemodels,”arXiv:2409.19492,2024.
[316] C. Lu, C. Lu, R. T. Lange, J. Foerster, J. Clune, and D. Ha,
“Theaiscientist:Towardsfullyautomatedopen-endedscientific
discovery,”arXivpreprintarXiv:2408.06292,2024.
[317] G. Agrawal, T. Kumarage, Z. Alghamdi, and H. Liu, “Can
knowledgegraphsreducehallucinationsinllms?:Asurvey,”in
NAACL,2024,pp.3947–3960.
[318] R. Nakano, J. Hilton, S. Balaji, J. Wu, L. Ouyang, C. Kim,
C.Hesse,S.Jain,V.Kosaraju,W.Saundersetal.,“Webgpt:Browser-
assistedquestion-answeringwithhumanfeedback,”arXivpreprint
arXiv:2112.09332,2021.
[319] T. Gao, H. Yen, J. Yu, and D. Chen, “Enabling large language
modelstogeneratetextwithcitations,”inEMNLP,2024.
[320] X.Wang,J.Wei,D.Schuurmans,Q.V.Le,E.H.Chi,S.Narang,
A.Chowdhery,andD.Zhou,“Self-consistencyimproveschainof
thoughtreasoninginlanguagemodels,”inICLR,2023.
[321] S.Zhou,U.Alon,S.Agarwal,andG.Neubig,“Codebertscore:
Evaluatingcodegenerationwithpretrainedmodelsofcode,”in
EMNLP,2023,pp.13921–13937.
[322] Z. Wang, S. Zhou, D. Fried, and G. Neubig, “Execution-based
evaluationforopen-domaincodegeneration,”inEMNLP,2023,
pp.1271–1290.
