Title: Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large Language Model Agents

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/06_Agent_Memory_Cognitive/01_AgeMem_Yu2026.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:07:19+00:00
- page_count: 25
- status: ok
- text_char_count: 94167

Metadata:
- author: Yi Yu; Liuyi Yao; Yuexiang Xie; Qingquan Tan; Jiaqi Feng; Yaliang Li; Libing Wu
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Background and Related Work (page 3)
- Method (page 3)
  - Problem Formulation (page 3)
  - Memory Management via Tool Interface (page 4)
  - Three-Stage Progressive RL Strategy (page 4)
  - Step-wise GRPO for Unified Management (page 5)
  - Reward Function Design (page 5)
- Experiments (page 6)
  - Experimental Setup (page 6)
  - Main Results (page 6)
  - Ablation Studies (page 7)
- Conclusion (page 8)
- Detailed Design and Implementation of AgeMem (page 11)
  - Memory Management Tools (page 11)
  - Reward Function Design (page 13)
  - AgeMem Algorithm (page 16)
- Case Study: AgeMem in Action (page 18)
  - Case 1: Long-term Memory Construction and Maintenance (page 18)
  - Case 2: Short-term Context Management Under Distraction (page 20)
  - Case 3: Integrated Task Execution with Memory Coordination (page 21)
- Experimental Implementation (page 22)
  - Dataset Details (page 22)
  - LLM-based Evaluation Details (page 23)
  - Baseline Configurations (page 24)
  - Implementation Details (page 24)
- Additional Results (page 24)
  - Ablation Study (page 24)
  - Reward Function Ablation on Qwen3-4B (page 24)
    - Convergence Analysis (page 25)
    - Quantitative Results (page 25)

Markdown Content:

Agentic Memory: Learning Unified Long-Term and Short-Term Memory
Management for Large Language Model Agents
YiYu1,2,LiuyiYao1,†,YuexiangXie1,QingquanTan2,JiaqiFeng2,
YaliangLi1,andLibingWu2,†
1AlibabaGroup,
2SchoolofCyberScienceandEngineering,WuhanUniversity
{yui1212,tanqingquan,jiaqiFeng,wu}@whu.edu.cn
{yly287738,yuexiang.xyx,yaliang.li}@alibaba-inc.com
†Correspondingauthors
Abstract etal.,2025b). High-qualityLTMsupportsefficient
retrieval of accumulated knowledge, while effec-
Largelanguagemodel(LLM)agentsfacefun-
tive STM management reduces redundancy and
damental limitations in long-horizon reason-
preservessalientcontext. Together,theymitigate
ingduetofinitecontextwindows,makingef-
thelimitationsoffinitecontextwindows,making
fective memory management critical. Exist-
theirjointmanagementcrucialforimprovingagent
ingmethodstypicallyhandlelong-termmem-
ory(LTM)andshort-termmemory(STM)as performanceincomplexreasoningsettings.
separatecomponents,relyingonheuristicsor However, existing research has predominantly
auxiliary controllers, which limits adaptabil- treatedLTMandSTMasindependentcomponents.
ity and end-to-end optimization. In this pa- STM is commonly enhanced through retrieval-
per,weproposeAgenticMemory(AgeMem),
augmentedgeneration(RAG)(Panetal.,2025b),
aunifiedframeworkthatintegratesLTMand
such as in MainRAG (Chang et al., 2025) and
STMmanagementdirectlyintotheagent’spol-
ReSum (Wu et al., 2025a), which expand usable
icy. AgeMemexposesmemoryoperationsas
tool-basedactions,enablingtheLLMagentto context via external retrieval or periodic summa-
autonomouslydecidewhatandwhentostore, rization. Although effective in some tasks, these
retrieve, update, summarize, ordiscardinfor- methods rely heavily on predefined schedules or
mation.Totrainsuchunifiedbehaviors,wepro- heuristicrules,potentiallyresultinginoverlooked
pose a three-stage progressive reinforcement
infrequent but critical details as well as unneces-
learningstrategyanddesignastep-wiseGRPO
sarynoise(Maetal.,2025;Dongetal.,2025). In
to address sparse and discontinuous rewards
contrast,LTMmanagementhasprogressedalong
inducedbymemoryoperations. Experiments
separate lines, typically categorized into trigger-
onfivelong-horizonbenchmarksdemonstrate
thatAgeMemconsistentlyoutperformsstrong based (Kang et al., 2025; Wang and Chen, 2025;
memory-augmentedbaselinesacrossmultiple Wang et al., 2025c; Chhikara et al., 2025) and
LLMbackbones,achievingimprovedtaskper- agent-based (Yan et al., 2025; Hu et al., 2025;
formance, higher-quality long-term memory, Xu et al., 2025) paradigms. The former executes
andmoreefficientcontextusage.
fixed memory operations at predefined moments,
whereasthelatterincorporatesaspecializedmem-
1 Introduction
ory manager to determine what and how to store.
Inlong-horizonagentictasksinvolvingmulti-step Despiteofferingmoreflexibility,mostapproaches
reasoning and complex workflows (Chang et al., still depend on handcrafted rules or auxiliary ex-
2024), the effectiveness of large language model pert models, limiting adaptability and increasing
(LLM)agentsisfundamentallyconstrainedbythe systemcomplexity(Xiongetal.,2025).
information they can attend to at any given time, Asaconsequence,LTMandSTMaretypically
whichwecollectivelyrefertoastheagent’smem- treated as separate and loosely coupled modules.
ory (Xiong et al., 2025; Goodyear et al., 2025). As illustrated in Figure 1, existing architectures
Memorytypicallyfallsintotwocategories: long- generallyfollowtwopatterns: (a)staticSTMwith
term memory (LTM), which persistently stores trigger-basedLTM,or(b)staticSTMwithagent-
user- or task-specific knowledge (Zhong et al., basedLTM.Inbothsettings,thetwomemorysys-
2024;Jiangetal.,2024),andshort-termmemory tems are optimized independently and later com-
(STM),whichcomprisestheinformationcontained bined in an ad hoc way, leading to fragmented
inthecurrentinputcontext(Wuetal.,2025b;Gao memoryconstructionandsuboptimalperformance
1
6202
naJ
5
]LC.sc[
1v58810.1062:viXra

Query Session Query Session Query Session
Content Content Content
Which band has 1. Narcissus (band) ... Which band has 1. Narcissus (band) ... Which band has 1. Narcissus (band) ...
more members, Muse 2. The Raconteurs ... more members, Muse 2. The Raconteurs ... more members, Muse 2. The Raconteurs ...
or The Raconteurs? 3. Sundae Club ... or The Raconteurs? 3. Sundae Club ... or The Raconteurs? 3. Sundae Club ...
Static Trigger-based Static Memory
Short-term Memory Long-term Memory Short-term Memory Manager Agentic Memory Management
Query M st e o m ra o g r e y me A m dd ory Query M sto em ra o g r e y < { e “ o n a p t c e ” t : r ” i a o N t n a i ” o r : n ” c a > i d ss d u ” s ,“ c .. o .” n } t M S e h m o o r r t- y t e T r o m o ls M L em on o g r - y t e T r o m o ls
M Re e t m rie o v ri e e d s Update M Re e t m rie o v ri e e d s </operation>
memory Memory Tools calling & Memory
Context M ret e r m ie o v r a y l m D e e m le o t r e y Context M ret e r m ie o v r a y l Ag t e e n r t m -b M a o s p e e e d m ra L o t r i o o y n n g- Agentic Co M n e t m ex o t ry operati A on gentic M r e et m rie o v r a y l tool
Multi-round Multi-round Multi-round
responses responses responses
LLM LLM LLM
Answer Independent Answer Independent Answer Agentic
<answer> construction <answer> construction <answer> construction
The Raconteurs. The Raconteurs. The Raconteurs.
</answer> </answer> </answer>
Short-term Long-term Short-term Long-term Short-term Long-term
Memory Memory Memory Memory Memory Memory
(a) Static STM + Trigger-based LTM (b) Static STM + Agent-based LTM (c) Unified Management (AgeMem)
Figure 1: Comparison between independent and unified memory management frameworks. (Left) Traditional
frameworkwithstaticSTMandtrigger-basedLTM.(Middle)IndependentframeworkwithanadditionalMemory
ManagercontrollingLTMinanagent-basedmanner,whileSTMremainsstatic. (Right)TheproposedAgeMem
framework,whereLTMandSTMarejointlyandintelligentlymanagedviaexplicittool-basedoperations.
inlong-horizonreasoningtasks. Thus,unifyingthe Toaddressthesechallenges,weproposeAgen-
managementofLTMandSTMremainsanecessary tic Memory (AgeMem), a unified framework that
yetlargelyunexploredchallenge. jointly manages LTM and STM, illustrated in
Nevertheless, achieving unified memory man- Figure 1 (right). Unlike prior designs that treat
agementposesthreefundamentalchallenges. (C1) memoryasanexternalcomponent,AgeMeminte-
Functional heterogeneity coordination: LTM gratesbothmemorytypesdirectlyintotheagent’s
and STM serve distinct yet complementary pur- decision-makingprocess. Throughaunifiedtool-
poses: LTM determines what to store, update, or based interface, the LLM autonomously invokes
discard,whileSTMgovernswhattoretrieve,sum- and executes memory operations for both LTM
marize,orremovefromtheactivecontext(Zhang and STM. Furthermore, we design a three-stage
et al., 2025b). The challenge lies in designing progressive RL strategy: the model first acquires
a unified mechanism that orchestrates their inter- LTM storage capabilities, then learns STM con-
play synergistically. (C2) Training paradigm text management, and finally coordinates both
mismatch: Existingreinforcementlearning(RL) forms of memory under full task settings. To
frameworks adopt markedly different training address the fragmented experience issue across
strategies for the two memory types (Ma et al., trainingstages,wedesignastep-wiseGroupRel-
2024). LTM-focused training often leverages ative Policy Optimization (GRPO) (Shao et al.,
session-levelinformationavailablepriortointerac- 2024),whichtransformscross-stagedependencies
tion,whereasSTMtrainingtypicallyinjectsdistrac- intolearnablesignals,therebyalleviatingthechal-
torstosimulatelong-horizoncontexts(Sunetal., lengesposedbysparseanddiscontinuousrewards
2024). Moreover,standardRLassumescontinuous inRL.WeevaluateAgeMemonfivelong-context,
trajectories with stable rewards, which conflicts reasoning-intensivebenchmarks. Comprehensive
withtheinherentlyfragmentedanddiscontinuous results show that AgeMem consistently outper-
experiencesproducedbymemoryoperations(Wu formsstrongbaselines,validatingtheeffectiveness
etal.,2025a),makingend-to-endoptimizationpar- ofunifiedmemorymanagement.
ticularlychallenging. (C3)Practicaldeployment Ourmaincontributionsareasfollows:
constraints: Manyagentsystemsrelyonanauxil- • We propose Agentic Memory (AgeMem), a
iaryexpertLLMformemorycontrol,significantly unified agentic memory framework that en-
increasinginferencecostandtrainingcomplexity. ablesLLM-basedagentstoautonomouslydecide
Howtointegrateunifiedmemorymanagementdi- when,what,andhowtomanagebothlong-term
rectlyintoanagentwithoutdependenceonexternal andshort-termmemory.
expertmodelsremainsanopenproblem. • Wedevelopathree-stageprogressiveRLstrat-
2

egy equipped with a step-wise GRPO mecha- rare but crucial details. Our approach instead en-
nism,facilitatingeffectiveend-to-endlearningof ables agents to learn when and how to retrieve,
unifiedmemorymanagementbehaviors. summarize,orfiltercontext,achievingamoreflex-
• Weconductcomprehensiveevaluationsacross ible balance between efficiency and information
multiplemodelsandlong-horizonbenchmarks, preservation.
demonstrating therobustnessand effectiveness Reinforcement learning for LLMs. Reinforce-
ofAgeMemincomplexagentictasks. ment learning has become an effective paradigm
forimprovingthedecision-makingandreasoning
2 BackgroundandRelatedWork capabilitiesofLLM-basedagents(Yaoetal.,2022;
Jinetal.,2025;Qianetal.,2025;Chaudharietal.,
Long-term memory (LTM). Persistent LTM is 2025). Amongrecentadvances,GRPO(Shaoetal.,
crucial for LLM-based agents operating over ex- 2024) enhances stability by optimizing policies
tended horizons (Wang et al., 2025b; Li et al., basedontherelativequalityofsampledtrajectories,
2025). Recent work has explored diverse ar- removing the need for an explicit value function.
chitectural designs for modeling LTM. Lang- GRPOanditsvariants(Gilabertetal.,2025;Wang
Mem (LangChain Team, 2025) provides a mod- et al., 2025a) have shown strong performance in
ular framework that supports multiple memory complex reasoning tasks. However, existing RL-
types, while A-Mem (Xu et al., 2025) adopts based systems generally treat memory as a static
a Zettelkasten-inspired design that links struc- orexternalcomponent,makingthemill-suitedfor
tured knowledge units to facilitate consolidation. thediscontinuousandfragmentedtrajectoriesasso-
Mem0 (Chhikara et al., 2025) proposes a scal- ciated with memory operations (Yan et al., 2025;
able extract-update pipeline and extends it to a Zhang et al., 2025a). In contrast, our work inte-
graph-basedvariantforstructuredreasoning,and grates RL directly into the memory management
Zep(Rasmussenetal.,2025)representsmemory process,enablingunifiedtrainingofbothlanguage
as a temporal knowledge graph to enable cross- generationandmemoryoperations.
session and time-aware reasoning. Although ef-
fective in organizing and retrieving information, 3 Method
theseapproacheslargelyrelyonpredefinedmem-
We propose Agentic Memory (AgeMem), a uni-
orystructuresorheuristicupdaterules. Asmem-
fiedmemoryframeworkthatenablesLLMagents
ory grows, such designs commonly suffer from
to autonomously manage both LTM and STM in
increased system complexity and lack adaptive,
an end-to-end manner. As illustrated in Figure 1
learning-basedstrategiesforprioritizationandfor-
(right),AgeMemintegratesmemorymanagement
getting. In contrast, our work aims to learn an
capabilitiesdirectlyintotheagentviaasetofspe-
adaptivememorypolicythatallowsagentstody-
cializedtools,enablingthemodeltolearnoptimal
namicallydecide what to store, update, or forget,
strategiesforunifiedmemorymanagementthrough
dependingontaskdemandsandlong-termutility.
three-stageprogressivestrategy.
Short-term memory (STM). STM in agentic
LLMs primarily concerns context selection and
3.1 ProblemFormulation
retrieval (Wang et al., 2024; Jin et al., 2024).
Retrieval-AugmentedGeneration(RAG)(Panetal., Unified RL formulation for AgeMem. At each
2025b; Salama et al., 2025; Kagaya et al., 2024) timestept,theagentobservesastates t ∈ S com-
isthedominantparadigm, expandingusablecon- posedoftheconversationcontext(short-termmem-
text by injecting retrieved content into prompts. ory)C t ,thelong-termmemorystoreM t ,andthe
Whileeffective,RAGdoesnotfundamentallypre- taskspecificationT: s t = (C t ,M t ,T). Thespec-
ventcontextexplosioninlong-horizonsettingsand ificationT includestheinputqueryq,contextual
mayintroduceirrelevantordistractinginformation. informationI q ,and(fortrainingonly)theexpected
To address this issue, ReSum (Wu et al., 2025a) answerA q . Thisformulationenablestheagentto
periodicallycompressesinteractionhistoriesinto grounditsdecision-makinginbothtransientcon-
compactreasoningstates,allowingagentstooper- textandpersistentknowledge.
atebeyondfixedcontext-windowconstraints. Yet Given s , the agent selects an action a ∈ A
t t
itssummarizationscheduleremainslargelyprede- fromahybridactionspacethatincludeslanguage
fined,andaggressivecompressionrisksdiscarding generationaswellasmemoryoperations. Thede-
3

cision is governed by a parameterized policy π , Table 1: Memory management tools in AgeMem for
θ
manipulatinglong-termmemory(LTM)andshort-term
defined as π (a |s ) = P(a |s ;θ), where θ de-
θ t t t t
memory(STM).
notestheLLMparametersanda = π (·|s ). For
t θ t
atrajectoryτ = (s ,a ,...,s ,a ),thecumula-
1 1 T T Tool Target Function
tiverewardisdefinedas:
ADD LTM AddnewknowledgetoM
t
(cid:88) UPDATE LTM ModifyentriesinM t
R(τ) = w i ·R i (τ)+P penalty (τ), (1) DELETE LTM RemoveentriesfromM t
RETRIEVE STM RetrieveentriesfromM
t
toC
t
whereR i capturestaskperformanceandmemory SUMMARY STM SummarizesegmentsinC t
quality,andP penalty discouragesredundantstorage, FILTER STM FilteroutirrelevantsegmentsfromC t
excessivetoolusage,anduncontrolledcontextex-
pansion. Theoptimizationobjectiveis:
3.2 MemoryManagementviaToolInterface
θ∗ = argmaxE [R(τ)]. (2) AgeMemexposesmemory-relatedoperationstothe
τ∼π
θ θ
LLMagentthroughanexplicittoolinterface(Ta-
ble1). TheagentcanmodifyitspersistentLTMus-
Thisformulationtreatsmemorymanagementasan
integralcomponentoftheagent’spolicy,replacing
ingADD,UPDATE,andDELETE,whileexercising
handcraftedheuristicswithalearnablemechanism.
fine-grainedcontroloverSTMthrough RETRIEVE,
Three-stage trajectory structure. To capture
SUMMARY,andFILTER. Incorporatingthesetools
into the action space transforms memory control
long-horizon interactions and progressively train
fromanexternalheuristicpipelineintoanintrinsic
memorycapabilities,eachtrajectoryisdividedinto
three consecutive stages: τ = (τ(1),τ(2),τ(3)), componentofdecision-making. Thisdesignallows
withatotallengthofT = T +T +T . InStage1, theagenttoadaptivelymanagememoryaccording
1 2 3
totaskstructure,history,andcontext. Implementa-
the agent engages in casual interactions and may
tiondetailsareprovidedintheAppendixA.1.
store useful information into LTM. Stage 2 intro-
duces distracting or irrelevant content, requiring
3.3 Three-StageProgressiveRLStrategy
theagenttomanageitsSTMthroughselectivere-
tention and compression. Stage 3 presents a task Tolearnunifiedandstablememorybehaviors,we
that depends on coordinated use of both retained proposeaprogressivethree-stagetrainingstrategy.
contextandearlieraccumulatedLTM.Akeyaspect Foreachtaskinstanceq ∈ T,theagentgenerates
ofthisdesignisthatthelong-termmemoryM per- acompletetrajectory:
t
sistsacrossallstages,allowingearlyknowledgeto
(q) (cid:0) (1) (2) (3)(cid:1)
influence later decisions. In contrast, the context τ = τ , τ , τ , k = 1,...,K, (3)
k k k k
C is reset between Stages 1 and 2 to prevent in-
t
formationleakageacrossphases. Theresetbefore whereK denotesthenumberofindependentroll-
(i)
Stage 2 ensures the agent cannot solve the final outs,andeachsub-trajectoryτ correspondstoa
k
task via residual context, thereby forcing proper specifictrainingstage.
retrievalfromLTMandenablingeffectivetraining Stage 1 (LTM construction). The agent is ex-
ofmemoryoperations. posedtocontextualinformationI q inacasualcon-
At each step, we collect an experience tuple versationalsetting. Thegoalistoidentifysalient
e t = (s t ,a t ,r t ,logπ θ (a t |s t )), where r t is typ- informationandstoreitintoLTMM t . Duringthe
old
icallyzeroforintermediatestepsandassignedaf- interaction,theshort-termcontextC t evolvesnatu-
ter trajectory completion, and logπ (a |s ) de- rally,andtheagentmayinvokeLTM-relatedtools
θ t t
old
notesthelog probabilityundertheoldpolicyπ . whenappropriate. Formally,thisstageyieldsasub-
θ
Thisrepresentationenablesstep-wisecreditassig o n ld - trajectoryτ (1) = {e }T1 ,whereeachexperience
k t t=1
mentunderGRPO(Shaoetal.,2024)andallows tuplee followsthedefinitioninSection3.1.
t
theagenttoattributelong-termrewardstospecific Stage 2 (STM control under distractors). The
memorydecisionsacrossstages. Bystructuringtra- short-term context is reset, while the constructed
jectoriesinthisstagedyetcontinuousmanner,the LTMM isretained. Theagentisthenpresented
t
agentlearnstemporallycoherentandtask-adaptive withsemanticallyrelatedbutirrelevantormislead-
memorypoliciesessentialforrobustlong-horizon ing distractors. The objective is to learn proac-
reasoning. tive STM control through tool-based operations,
4

such as filtering or summarizing context, in or- Following GRPO, we maximize the expected
der to suppress noise and preserve useful infor- objectiveoverallexperiences:
mation. This process forms the sub-trajectory
τ
k
(2) = {e
t
}T
t=
1+
T1
T
+
2
1
,whichemphasizescontextfil- J(θ) = E (et,At)∼E (cid:2) ρ t A t −βD KL [π θ ∥π ref ] (cid:3)
t S e t r a in g g e a 3 n ( d In c t o e m g p ra re t s e s d io r n ea c s a o p n ab in il g ity a . ndmemoryco- = 1 (cid:88) B (cid:88) K T (cid:88)k (q) (cid:2) ρ (k,q) A (k,q) −βD (k,q)(cid:3) ,
|E| t t KL
ordination). Finally, the agent receives a formal
q=1k=1 t=1
queryq requiringbothaccuratereasoningandef- (6)
fectivememoryretrieval. Theagentmustretrieve wheretheimportanceratioρ
(k,q)
=
π
θ
(at|st)
con-
relevantknowledgefromM t ,appropriatelyman- trols the update magnitude
t
under th
π
e θol n d
(
e
a
w
t|s
p
t)
olicy,
age the context C , and generate a final answer. (k,q)
t D denotestheKLdivergencepenaltybetween
Thisstageproducesτ k (3) = {e t }T t=T1+T2+1 ,which the KL current policy π θ and a fixed reference π ref ,
evaluates the ability of agent to coordinate long- andβ isacoefficientthatbalancesexplorationand
termmemory,short-termcontextmanagement,and trainingstability.
tasksolutioninanend-to-endmanner.
Allthreesegmentsformacompletetrajectory: 3.5 RewardFunctionDesign
Wedesignacompositerewardthatevaluatesboth
(q)
τ = (e ,e ,...,e ), T = T +T +T , (4)
k 1 2 T 1 2 3 downstream task performance and the quality of
memory management. The total trajectory-level
which is then used for policy optimization in the
rewardisdefinedas
subsequentstep-wiseGRPOprocedure. Forabatch
of B tasks, we further aggregate all experiences
R(τ) = w⊤R+P , (7)
penalty
fromK independentrolloutsintoaunifiedsetE =
(cid:83)B
q=1
(cid:83)K
k=1 {e t | e t ∈ τ k
(q)
}, with a total size of where w = [w task ,w context ,w memory ]⊤ are tunable
|E| = B ×K ×T¯, where T¯ denotes the average coefficients, and R = [R ,R ,R ]⊤
task context memory
trajectorylength. Moredetailedrolloutprocesses correspondtorewardsfortaskcompletion,context
areprovidedintheAppendixA.3. management,andlong-termmemorymanagement.
ThepenaltytermP capturesviolationssuch
penalty
3.4 Step-wiseGRPOforUnifiedManagement
as context overflow or exceeding the interaction
We adopt a step-wise variant of GRPO to con- limit. Below,wesummarizeeachcomponent,and
nect long-range task rewards with memory de- preciseformulasareprovidedintheAppendixA.2.
cisions across all stages. For task q, let G q = Task completion reward R task . This term pro-
{τ (q) ,...,τ (q) } denote the group of parallel roll- vides the primary learning signal by assessing
1 K
outs. Each trajectory yields a terminal reward whether the agent solves the task correctly. We
r (k,q) = R(τ (q) ). We compute the group- obtain a scalar score using an LLM-based judge
T k
normalizedadvantagefortheterminalstepas: S judge (A pred ,A q ) ∈ [0,1], optionally applying a
penaltywhennoanswerisproduced. Thisreward
(k,q)
r −µ encouragesaccurate,completetasksolutionsand
A (k,q) = T Gq, (5)
T σ +ϵ remainsthedominantcomponenttoensurealign-
Gq
mentwithtaskobjectives.
whereµ Gq andσ Gq arethemeanandstandardde- ContextmanagementrewardR
context
. Thiscom-
viation of rewards within G , ϵ prevents division
q ponentevaluatesSTMbehavior,focusingonhow
byzero. Thisadvantageisthenbroadcasttoallpre-
effectively the agent controls the active context
(k,q) (k,q)
cedingstepsofthesametrajectoryA = A , C . Itcombinesthreefactors: (i)compressionef-
t T t
which assigns a consistent learning signal to all ficiency, promoting economical token usage; (ii)
memoryandreasoningactionsalongthetrajectory, preventiveactions,rewardingearlysummarization
including those in Stage 1 and Stage 2. In do- orfilteringtoavoidoverflow;and(iii)information
ingso,thefinaltaskoutcomesuperviseseveryin- preservation,penalizingthelossofcriticalquery-
termediatememorydecision,enablinglong-range relatedcontent. Eachfactorisnormalized,allowing
creditassignmentacrossheterogeneousstages. We therewardtobalancecontextefficiencyagainstre-
thenaugmenttheexperiencesetwithadvantages, tentionofessentialinformation.
E =
(cid:83)B,K{(e
,A )|e ∈ τ
(q)
,A = A
(k,q)
}. Memory management reward R . This
q,k t t t k t t memory
5

termevaluatesLTMoperations. Itaggregatessig-
   
nalsfor: (i)storagequality,measuredasthefrac-
tion of stored entries labeled as high-quality and    
reusable;(ii)maintenance,rewardingmeaningful
   
updateordeleteoperationstomitigatememorystal-
eness;and(iii)semanticrelevance,computedusing     /    D Q J 0 H P $  0 H P  0 H P   0 H P  J  $ J H 0 H P $ J H 0 H P
anLLM-basedscorebetweenretrievedmemories   Q R 5 /
  D   4 Z H Q      %  , Q V W U X F W
andthequery. Together,thesesignalsincentivize
selective,high-valuememoryconstructionandre-
sponsibleupkeepovertime.
PenaltytermsP . Penaltiesdiscourageunde-
penalty
sirablebehaviorssuchasexceedingthemaximum
numberofdialogueturnsortriggeringcontextover-
flow. Penaltycoefficientsarechosensothatsuch
violationsleadtoasubstantialreductioninthefinal
trajectoryreward,encouragingtheagenttomain-
tainsafeandefficientmemorypractices.
4 Experiments
4.1 ExperimentalSetup
Datasets. TocomprehensivelyevaluateAgeMem,
weselectfivewidely-useddatasetsinLLM-based
agentresearch: ALFWorld(Shridharetal.,2020),
SciWorld(Wangetal.,2022),PDDL(Changetal.,
2024), BabyAI (Chevalier-Boisvert et al., 2018),
andHotpotQA(Yangetal.,2018). Thesedatasets
coverembodiedaction,game-basedreasoning,and
knowledge-intensive question answering, provid-
ing diverse evaluation scenarios. Since the Hot-
potQA dataset contains both questions and sup-
portingfacts,automaticallyprovidingStage1con-
textual information, AgeMem is fine-tuned with
RL only on the HotpotQA training set and then
evaluateddirectlyonalldatasets. Detaileddataset
statisticsareprovidedinAppendixC.1.
Evaluation metrics. For the primary task com-
pletion metrics, we adopt Success Rate (SR) for
ALFWorld,SciWorld,andBabyAI,ProgressRate
(PR)forPDDL,andLLM-as-a-Judge(J)forHot-
potQA. Additionally, we employ an LLM-based
evaluatortoassessthequalityofstoredlong-term
memoryduringknowledgereasoning,measuredby
MemoryQuality(MQ).ThepromptsoftheLLM-
basedevaluationareprovidedinAppendixC.2.
Baselines&LLMbackbones. WecompareAge-
Mem against four representative agent LTM sys-
tems: LangMem (LangChain Team, 2025), A-
Mem (Xu et al., 2025), Mem0 (Chhikara et al.,
2025),andMem0g (agraph-basedvariantofficially
providedaspartofMem0). Tobetterdemonstrate
the effectiveness of RL training, we also include
  4 0   \ W L O D X 4  \ U R P H 0
                 
     
     
 % D V H O L Q H V
 $ J H 0 H P      
 $ Y J   % D V H O L Q H
   
   
   
   
 / D Q J 0 H P $  0 H P  0 H P   0 H P  J  $ J H 0 H P $ J H 0 H P
  Q R 5 /
  E   4 Z H Q    %  , Q V W U X F W
  4 0   \ W L O D X 4  \ U R P H 0
     
     
           
     
     
Figure2: MemoryQualityscoresfordifferentmethods
onHotpotQA.Higherscoresindicatebetterrelevance
betweenstoredmemoriesandground-truthfacts.
AgeMem-noRL,whichisnotfine-tunedwithRL.
InablationstudiesonSTM,wecompareSTMtools
withRAGapproach. Forthebaseagentmodels,we
useQwen2.5-7B-InstructandQwen3-4B-Instruct.
MorebaselineconfigurationsareinAppendixC.3.
Implementationdetails. Webuildagentsusingthe
Agentscopeframework(Gaoetal.,2025a)andfine-
tune AgeMem using the Trinity framework (Pan
etal.,2025a). Forallrewardweightsinthereward
function,weuseuniformcoefficientsof1.0with-
outmanualtuning. Furtherimplementationdetails
areprovidedinAppendixC.4.
4.2 MainResults
Comparison with counterparts. Table 2 shows
thatAgeMemachievesthehighestaverageperfor-
manceonbothQwen2.5-7B-Instruct(41.96%)and
Qwen3-4B-Instruct (54.31%), outperforming all
baselines across five datasets with relative gains
of 49.59% and 23.52% over no-memory, respec-
tively. Comparedtothebestbaselines(Mem0and
A-Mem),AgeMemimprovesby4.82and8.57per-
centagepointsonaverage. RLtrainingcontributes
8.53percentagepointsand8.72percentagepoints
improvementsoverAgeMem-noRL,validatingthe
three-stageprogressiveRLstrategy.
Qualityofstoredlong-termmemories. Toeval-
uate the quality of stored memories, we leverage
the ground-truth facts provided in the HotpotQA
dataset and assess the relevance between stored
memories and these facts using an LLM-based
evaluator. Figure 2 presents the Memory Qual-
ity(MQ)scoresfordifferentbaselines. AgeMem
6

Table2: Performancecomparisonacrossfivebenchmarks. Thebestandsecond-bestresultsaremarked.
LLMBackbone Method ALFWorld SciWorld PDDL BabyAI HotpotQA Average
No-Memory 27.16 13.80 10.15 50.80 38.36 28.05
LangMem 38.27 28.29 15.85 51.34 37.43 34.23
A-Mem 34.68 28.06 18.39 58.82 43.95 36.78
Qwen2.5-7B-Instruct Mem0 37.49 26.99 13.96 60.58 46.66 37.14
Mem0g 35.34 30.50 14.86 58.78 42.06 36.31
AgeMem-noRL 37.90 28.67 8.87 46.34 45.36 33.43
AgeMem(Ours) 41.07 35.55 17.31 61.42 54.44 41.96
No-Memory 38.51 47.89 30.14 55.83 47.48 43.97
LangMem 40.89 50.42 28.42 53.80 42.70 43.25
A-Mem 34.31 50.14 34.41 61.35 48.48 45.74
Qwen3-4B-Instruct Mem0 41.17 51.38 31.72 60.05 39.16 44.70
Mem0g 36.69 47.76 29.61 57.59 38.12 41.95
AgeMem-noRL 38.02 50.42 27.52 57.48 54.49 45.59
AgeMem(Ours) 48.97 59.48 35.07 72.56 55.49 54.31
 
 
 
 
    Q R L W F X G H 5  Q H N R 7  4 Z H Q      %     
 4 Z H Q    %     
         
         
         
 % D V H O L Q H   $ J H 0 H P  5 $ *
    
    
 $ J H 0 H P  Q R 5 /  $ J H 0 H P  $ J H 0 H P  $ J H 0 H P
  5 $ *   Q R 5 /   5 $ *   2 X U V 
 & R Q I L J X U D W L R Q
 V Q H N R 7   J Y $
Table3: ToolusagestatisticsonHotpotQA.Numbers
showaveragecallsperepisode.
Qwen2.5-7B Qwen3-4B
ToolCategory
noRL GRPO noRL GRPO
LTMToolStatistics
    
                                   ADDMemory 0.92 1.64 2.49 2.64
UPDATEMemory 0.00 0.13 0.13 0.34
DELETEMemory 0.00 0.08 0.00 0.22
STMToolStatistics
Figure3: Averageprompttokencountsunderdifferent
STM management configurations on HotpotQA. The RETRIEVEMemory 2.31 1.95 4.62 4.35
suffix“-RAG”indicatestheadoptionofRAGinplace SUMMARYContext 1.08 0.82 0.11 0.96
FILTERContext 0.02 0.31 0.15 0.16
ofSTMtool-basedmanagement.
TotalCalls 4.33 4.92 7.50 8.67
achievesthehighestmemoryqualityonbothmodel textexpansion,enablingmoreefficienttokenusage
backbones,withMQscoresof0.533and0.605,re- whilemaintainingtaskperformance.
spectively. Thisindicatesthattheunifiedmemory Tool usage analysis. Table 3 reports tool usage
management framework not only improves task statistics before and after RL fine-tuning on Hot-
performancebutalsopromotesthestorageofhigh- potQA.RLtrainingsubstantiallyincreasestheuse
quality,reusableknowledge. Thecomparisonwith of long-term memory tools, especially ADD and
baselinemethodsfurthervalidatesthatAgeMem’s UPDATE. On Qwen2.5-7B-Instruct, ADD opera-
tool-basedmemoryoperationsleadtomoreselec- tions rise from 0.92 to 1.64, and UPDATE opera-
tiveandhigher-qualitymemoryconstruction. tions appear after training (0.13 v.s. nearly zero).
Effectiveness of STM management. We eval- SimilartrendsareobservedonQwen3-4B-Instruct,
uate the effectiveness of STM management by with higher frequencies of both ADD and UP-
measuringtheprompttokencountunderdifferent DATE. For short-term memory tools, RL leads
configurationsonHotpotQA.Figure3showsthat to more balanced tool usage. The frequency of
AgeMemsuccessfullyreducesprompttokenusage FILTER increasesnotably(e.g.,from0.02to0.31
comparedtovariantswithoutSTMtools(-RAG). onQwen2.5),indicatingproactivecontextcontrol,
OnQwen2.5-7B-Instruct,AgeMemuses2,117to- whileRETRIEVEremainsrelativelystable. Overall,
kens on average, compared to 2,186 tokens for thesepatternssuggestthatRLtrainingenablesco-
AgeMem-RAG,representingareductionof3.1%. ordinatedandadaptivememorymanagement. De-
OnQwen3-4B-Instruct,thereductionisevenmore tailedcasestudiesareprovidedinAppendixB.
pronounced: AgeMem uses 2,191 tokens versus
4.3 AblationStudies
2,310 tokens for AgeMem-RAG, a reduction of
5.1%. These results demonstrate that the learned LTM-STM components. To validate the con-
STM management tools effectively control con- tributions of individual components, we conduct
7

  
  
  
 
 % D V H   / 7   / 7  5 /  / 7  6 7  5 /
  D   $ / ) : R U O G
 H U R F 6  H F Q D P U R I U H 3
                                         
  
        
        
 
 % D V H   / 7   / 7  5 /  / 7  6 7  5 /
  E   6 F L : R U O G
     
                       
  
     
        
  
 
 % D V H   / 7   / 7  5 /  / 7  6 7  5 /
  F   + R W S R W 4 $
    
     
     
     
     
Figure4: AblationstudyonLTM,STM,andRLcomponents(Qwen2.5-7B-Instruct). Base: No-memorybaseline;
+LT: AgeMem-noRL-RAG (LTM tools only); +LT/RL: AgeMem-RAG (RL with LTM tools); +LT/ST/RL:
AgeMem(fullAgeMemsystemwithRL).Greenarrowsindicateperformancegainsoverthebaseline.
ablation studies on LTM, STM, and RL training. 1.0
Figure 4 presents results on three representative
0.8
datasets using Qwen2.5-7B-Instruct as the back-
0.6
bone(resultsforQwen3-4B-Instructareprovided
in Appendix D.1). Adding LTM alone (+LT) 0.4
yields substantial gains of +10.6%, +14.2%, and
0.2
+7.4%overthebaseline. IncorporatingRLtraining
(+LT/RL)furtherimprovesperformance, particu- 0.00 20 40 60 80 100
Training Step
larlyonHotpotQA(+6.3%),demonstratingtheef-
fectivenessofourreward-basedoptimization. The
full AgeMem system (+LT/ST/RL) achieves the
best results across all benchmarks, with overall
improvements of +13.9%, +21.7%, and +16.1%.
Notably, adding STM tools provides the most
significant boost on SciWorld (+3.1%) and Hot-
potQA (+2.4%), validating that learned context
managementoutperformsstaticRAGapproaches.
Theseprogressiveimprovementsconfirmthatuni-
fied memorymanagement withend-to-end RL is
essentialforoptimalagentperformance.
Reward function. To demonstrate the effective-
ness of our multi-component reward function de-
sign, we compare the full reward function (All-
Returns)againstavariantusingonlyR (Answer-
task
Only). Figure 5 shows the reward convergence
curvesofQwen2.5-7B-InstructduringGRPOtrain-
ingonHotpotQA.Thefullrewardfunctionleads
to significantly faster convergence and higher fi-
nalperformancecomparedtothetask-onlyvariant.
As detailed in Table 4, the All-Returns strategy
achieveshigherLLM-as-a-Judgescores(0.544v.s.
0.509)whilemaintainingsubstantiallybettermem-
oryquality(0.533v.s. 0.479). Notably,despiteus-
ingmoretokens(2117v.s. 2078),theAll-Returns
strategy achieves better overall performance, in-
dicating that the additional context and memory
operations contribute meaningfully to reasoning
quality. SimilarpatternsareobservedonQwen3-
4B-Instruct(seeAppendixD.2).
draweR
egarevA
Qwen2.5-7B - GRPO Training Reward Convergence
All Returns
Answer-Only
Figure5: TrainingconvergencecurvesonQwen2.5-7B-
InstructcomparingAll-Returns(solidline)v.s. Answer-
Only(dashedline)rewardstrategies.
Table4: RewardfunctionablationonHotpotQAusing
Qwen2.5-7B-Instruct. All-Returns v.s. Answer-Only
rewardstrategies. “TN”isthetokennumber,and“TC”
denotesthenumberoftoolcalls.
Strategy J(↑) TN(↓) MQ(↑) TC(-)
Answer-Only 0.509 2078 0.479 3.93
All-Returns 0.544 2117 0.533 4.92
5 Conclusion
In this work, we propose Agentic Memory (Age-
Mem),aunifiedmemorymanagementframework
that enablesLLM-based agentsto jointly control
long-term and short-term memory through learn-
able, tool-based actions. By integrating memory
operationsdirectlyintotheagent’spolicyandtrain-
ing them with a progressive reinforcement learn-
ingstrategy,AgeMemreplacesheuristicmemory
pipelines with an end-to-end optimized solution.
Extensiveexperimentsacrossdiverselong-horizon
benchmarksshowthatAgeMemimprovesbothtask
performanceandmemoryqualitywhilemaintain-
ingefficientcontextusage. Theseresultshighlight
the importance of unified, agent-centric memory
policiesandsuggestapromisingdirectionforbuild-
ingscalableandadaptiveLLMagentscapableof
long-termreasoning.
8

Limitations Pengyu Gao, Jinming Zhao, Xinyue Chen, and Long
Yilin.2025b. Anefficientcontext-dependentmem-
WhileAgeMemdemonstratesstrongperformance oryframeworkforllm-centricagents. InProceedings
acrossmultiplesettings,thereremainopportunities ofthe2025ConferenceoftheNationsoftheAmer-
icasChapteroftheAssociationforComputational
forfurtherextension. Thecurrentimplementation
Linguistics: HumanLanguageTechnologies(Volume
adopts a fixed set of memory management tools,
3: IndustryTrack),pages1055–1069.
whichprovidesaclearandeffectiveabstractionbut
couldbeextendedtosupportmorefine-grainedcon- JavierGarciaGilabert,CarlosEscolano,XixianLiao,
trolinfuturework. Inaddition,althoughweeval- andMaiteMelero.2025. Terminology-constrained
translation from monolingual data using grpo. In
uate our approach on several representative long-
Proceedings of the Tenth Conference on Machine
horizonbenchmarks,broadercoverageoftasksand
Translation,pages1335–1343.
environmentsmayfurtherstrengthentheempirical
understandingoftheframework. LyleGoodyear,RachelGuo,andRameshJohari.2025.
The effect of state representation on llm agent be-
havior in dynamic routing games. arXiv preprint
arXiv:2506.15624.
References
Chia-Yuan Chang, Zhimeng Jiang, Vineeth Rakesh, YuanzheHu,YuWang,andJulianMcAuley.2025. Eval-
Menghai Pan, Chin-Chia Michael Yeh, Guanchu uatingmemoryinllmagentsviaincrementalmulti-
Wang, Mingzhi Hu, Zhichao Xu, Yan Zheng, Ma- turninteractions. arXivpreprintarXiv:2507.05257.
hashwetaDas,and1others.2025. Main-rag: Multi-
agent filtering retrieval-augmented generation. In Xun Jiang, Feng Li, Han Zhao, Jiahao Qiu, Jiaying
Proceedingsofthe63rdAnnualMeetingoftheAs- Wang, Jun Shao, Shihao Xu, Shu Zhang, Weiling
sociationforComputationalLinguistics(Volume1: Chen,XavierTang,and1others.2024. Longterm
LongPapers),pages2607–2622. memory: Thefoundationofaiself-evolution. arXiv
preprintarXiv:2410.15665.
Ma Chang, Junlei Zhang, Zhihao Zhu, Cheng Yang,
YujiuYang,YaohuiJin,ZhenzhongLan,Lingpeng Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon,
Kong, and Junxian He.2024. Agentboard: Anan- SercanArik,DongWang,HamedZamani,andJiawei
alytical evaluation board of multi-turn llm agents. Han.2025. Search-r1: Trainingllmstoreasonand
Advancesinneuralinformationprocessingsystems, leveragesearchengineswithreinforcementlearning.
37:74325–74362. arXivpreprintarXiv:2503.09516.
ShreyasChaudhari,PranjalAggarwal,VishvakMura-
Hongye Jin, Xiaotian Han, Jingfeng Yang, Zhimeng
hari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik
Jiang,ZiruiLiu,Chia-YuanChang,HuiyuanChen,
Narasimhan,AmeetDeshpande,andBrunoCastroda
andXiaHu.2024. Llmmaybelonglm: Self-extend
Silva. 2025. Rlhf deciphered: A critical analysis
llmcontextwindowwithouttuning. arXivpreprint
ofreinforcementlearningfromhumanfeedbackfor
arXiv:2401.01325.
llms. ACMComputingSurveys,58(2):1–37.
Tomoyuki Kagaya, Thong Jing Yuan, Yuxuan Lou,
MaximeChevalier-Boisvert,DzmitryBahdanau,Salem
Jayashree Karlekar, Sugiri Pranata, Akira Kinose,
Lahlou,LucasWillems,ChitwanSaharia,ThienHuu
KokiOguri,FelixWick,andYangYou.2024. Rap:
Nguyen,andYoshuaBengio.2018. Babyai: Aplat-
Retrieval-augmentedplanningwithcontextualmem-
formtostudythesampleefficiencyofgroundedlan-
ory for multimodal llm agents. arXiv preprint
guagelearning. arXivpreprintarXiv:1810.08272.
arXiv:2402.03610.
PrateekChhikara,DevKhant,SaketAryan,Taranjeet
Jiazheng Kang, Mingming Ji, Zhe Zhao, and Ting
Singh,andDeshrajYadav.2025. Mem0: Building
Bai.2025. Memoryosofaiagent. arXivpreprint
production-readyaiagentswithscalablelong-term
arXiv:2506.06326.
memory. arXivpreprintarXiv:2504.19413.
YihongDong,XueJiang,JiaruQian,TianWang,Kechi LangChainTeam.2025. Langmemsdkforagentlong-
Zhang,ZhiJin,andGeLi.2025. Asurveyoncode termmemory.
generation with llm-based agents. arXiv preprint
arXiv:2508.00083. Hao Li, Chenghao Yang, An Zhang, Yang Deng, Xi-
angWang,andTat-SengChua.2025. Helloagain!
Dawei Gao, Zitao Li, Yuexiang Xie, Weirui Kuang, llm-powered personalized agent for long-term dia-
Liuyi Yao, Bingchen Qian, Zhijian Ma, Yue logue. InProceedingsofthe2025Conferenceofthe
Cui, Haohao Luo, Shen Li, and 1 others. 2025a. NationsoftheAmericasChapteroftheAssociation
Agentscope 1.0: A developer-centric framework for Computational Linguistics: Human Language
for building agentic applications. arXiv preprint Technologies(Volume1: LongPapers),pages5259–
arXiv:2508.16279. 5276.
9

HaoMa,TianyiHu,ZhiqiangPu,LiuBoyin,Xiaolin RuoyaoWang,PeterJansen,Marc-AlexandreCôté,and
Ai,YanyanLiang,andMinChen.2024. Coevolving Prithviraj Ammanabrolu. 2022. Scienceworld: Is
withtheotheryou: Fine-tuningllmwithsequential youragentsmarterthana5thgrader? arXivpreprint
cooperativemulti-agentreinforcementlearning. Ad- arXiv:2203.07540.
vances in Neural Information Processing Systems,
37:15497–15525. YuWangandXiChen.2025. Mirix: Multi-agentmem-
ory system for llm-based agents. arXiv preprint
QianouMa,WeiruiPeng,ChenyangYang,HuaShen, arXiv:2507.07957.
KenKoedinger, andTongshuangWu.2025. What
shouldweengineerinprompts? traininghumansin
ZixuanWang,BoYu,JunzheZhao,WenhaoSun,Sai
requirement-drivenllmuse. ACMTransactionson
Hou, Shuai Liang, Xing Hu, Yinhe Han, and Yim-
Computer-HumanInteraction,32(4):1–27.
ingGan.2025b. Karma: Augmentingembodiedai
agents with long-and-short term memory systems.
XuchenPan,YanxiChen,YushuoChen,YuchangSun,
In2025IEEEInternationalConferenceonRobotics
DaoyuanChen,WenhaoZhang,YuexiangXie,Yilun
andAutomation(ICRA),pages1–8.IEEE.
Huang,YileiZhang,DaweiGao,and1others.2025a.
Trinity-rft: Ageneral-purposeandunifiedframework
Zora Zhiruo Wang, Apurva Gandhi, Graham Neu-
forreinforcementfine-tuningoflargelanguagemod-
big, and Daniel Fried. 2025c. Inducing program-
els. arXivpreprintarXiv:2505.17826.
matic skills for agentic tasks. arXiv preprint
arXiv:2504.06821.
Zhuoshi Pan, Qianhui Wu, Huiqiang Jiang, Xufang
Luo,HaoCheng,DongshengLi,YuqingYang,Chin-
Zora Zhiruo Wang, Jiayuan Mao, Daniel Fried, and
Yew Lin, H Vicky Zhao, Lili Qiu, and 1 others.
Graham Neubig. 2024. Agent workflow memory.
2025b. On memory construction and retrieval for
personalizedconversationalagents. arXivpreprint
arXivpreprintarXiv:2409.07429.
arXiv:2502.05589.
Xixi Wu, Kuan Li, Yida Zhao, Liwen Zhang, Litu
ChengQian,EmreCanAcikgoz,QiHe,HongruWang, Ou, Huifeng Yin, Zhongwang Zhang, Xinmiao
Xiusi Chen, Dilek Hakkani-Tür, Gokhan Tur, and Yu, Dingchu Zhang, Yong Jiang, and 1 others.
Heng Ji. 2025. Toolrl: Reward is all tool learning 2025a. Resum: Unlockinglong-horizonsearchin-
needs. arXivpreprintarXiv:2504.13958. telligenceviacontextsummarization. arXivpreprint
arXiv:2509.13313.
PrestonRasmussen,PavloPaliychuk,TravisBeauvais,
JackRyan,andDanielChalef.2025. Zep: atempo- YaxiongWu,ShengLiang,ChenZhang,YichaoWang,
ralknowledgegrapharchitectureforagentmemory. YongyueZhang,HuifengGuo,RuimingTang,and
arXivpreprintarXiv:2501.13956. YongLiu.2025b. Fromhumanmemorytoaimem-
ory: Asurveyonmemorymechanismsintheeraof
RanaSalama,JasonCai,MichelleYuan,AnnaCurrey, llms. arXivpreprintarXiv:2504.15965.
Monica Sunkara, Yi Zhang, and Yassine Benajiba.
2025. Meminsight: Autonomousmemoryaugmenta-
ZidiXiong,YupingLin,WenyaXie,PengfeiHe,Zirui
tionforllmagents. arXivpreprintarXiv:2503.21760.
Liu,JiliangTang,HimabinduLakkaraju,andZhen
Xiang.2025. Howmemorymanagementimpactsllm
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu,
agents: Anempiricalstudyofexperience-following
JunxiaoSong,XiaoBi,HaoweiZhang,Mingchuan
behavior. arXivpreprintarXiv:2505.16067.
Zhang, YK Li, Yang Wu, and 1 others. 2024.
Deepseekmath: Pushingthelimitsofmathematical
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Jun-
reasoninginopenlanguagemodels. arXivpreprint
tao Tan, and Yongfeng Zhang. 2025. A-mem:
arXiv:2402.03300.
Agentic memory for llm agents. arXiv preprint
arXiv:2502.12110.
Mohit Shridhar, Xingdi Yuan, Marc-Alexandre Côté,
Yonatan Bisk, Adam Trischler, and Matthew
SikuanYan,XiufengYang,ZuchaoHuang,ErcongNie,
Hausknecht.2020. Alfworld: Aligningtextandem-
bodiedenvironmentsforinteractivelearning. arXiv ZifengDing,ZonggenLi,XiaowenMa,KristianKer-
preprintarXiv:2010.03768. sting,JeffZPan,HinrichSchütze,and1others.2025.
Memory-r1: Enhancinglargelanguagemodelagents
Chuanneng Sun, Songjun Huang, and Dario Pompili. to manage and utilize memories via reinforcement
2024. Llm-based multi-agent reinforcement learn- learning. arXivpreprintarXiv:2508.19828.
ing: Current and future directions. arXiv preprint
arXiv:2405.11106. ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,
WilliamCohen,RuslanSalakhutdinov,andChristo-
Hongcheng Wang, Yinuo Huang, Sukai Wang, pher D Manning. 2018. Hotpotqa: A dataset for
Guanghui Ren, and Hao Dong. 2025a. Grpo-ma: diverse, explainablemulti-hopquestionanswering.
Multi-answer generation in grpo for stable and ef- In Proceedings of the 2018 conference on empiri-
ficient chain-of-thought training. arXiv preprint calmethodsinnaturallanguageprocessing,pages
arXiv:2509.24494. 2369–2380.
10

Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak A DetailedDesignandImplementationof
Shafran,KarthikRNarasimhan,andYuanCao.2022. AgeMem
React: Synergizingreasoningandactinginlanguage
models. InTheeleventhinternationalconferenceon Thisappendixprovidesfulltechnicaldetailsomit-
learningrepresentations.
ted from the main text due to space constraints.
YuxiangZhang,JiangmingShu,YeMa,XueyuanLin, We first present precise definitions and pseudo-
ShangxiWu,andJitaoSang.2025a. Memoryasac- formulations for each memory-management tool
tion: Autonomouscontextcurationforlong-horizon (AppendixA.1),thengiveimplementableformulas
agentictasks. arXivpreprintarXiv:2510.12635.
for the reward components used in training (Ap-
ZeyuZhang,QuanyuDai,XiaoheBo,ChenMa,RuiLi, pendix A.2). Finally, we provide the complete
XuChen,JiemingZhu,ZhenhuaDong,andJi-Rong algorithmicspecification(AppendixA.3).
Wen.2025b. Asurveyonthememorymechanismof
largelanguagemodel-basedagents. ACMTransac- A.1 MemoryManagementTools
tionsonInformationSystems,43(6):1–47.
AgeMem exposes a small set of structured tools
WanjunZhong,LianghongGuo,QiqiGao,HeYe,and that the agent may invoke as part of its action a .
t
YanlinWang.2024. Memorybank: Enhancinglarge
Each tool is implemented as a deterministic or
language models with long-term memory. In Pro-
stochasticfunctionthattransformstheshort-term
ceedingsoftheAAAIConferenceonArtificialIntelli-
gence,volume38,pages19724–19731. context C t , the long-term memory store M t , or
both. Unliketraditionalmemorysystemsthatrely
onexternalheuristicsorpredefinedschedules,Age-
Memintegratesthesetoolsdirectlyintotheagent’s
actionspace,enablingthemodeltolearnwhenand
howtouseeachtoolthroughreinforcementlearn-
ing. Belowwegivepreciseoperationaldefinitions,
implementation details, and the system prompts
thatguidetoolusage.
Notation. Long-termmemorystoreattimetis
M = {m }
|Mt|
,whereeachmemorym contains
t i i=1 i
acontentstringandoptionalmetadata. Short-term
context is C = [u ,u ,...,u ] (message list),
t 1 2 nt
and enc(·) denotes a text encoder that returns a
dense embedding. We use cosine similarity for
semanticmatchingthroughouttheframework.
RETRIEVE. The RETRIEVE operation enables
theagenttoaccessrelevantinformationfromlong-
term memory based on semantic similarity. This
operationiscrucialforbringingstoredknowledge
intotheactivecontextwhenneededforreasoning.
Theretrievaloperationreturnsthetop-k mostsimi-
larmemoriestothequeryq:
RETRIEVE(q,k) = TopK(M
t
, sim(q,m
i
), k),
(8)
wherethesimilarityfunctionisdefinedas:
enc(q)⊤enc(m )
i
sim(q,m ) = . (9)
i
∥enc(q)∥∥enc(m )∥
i
Theretrievedmemoriesaretheninsertedintothe
short-termcontextC ,makingthemavailablefor
t
immediate reasoning. The parameter k controls
thenumberofmemoriesretrieved,typicallysetto
11

3-5 in our experiments to balance relevance and whereSummarize(·)isimplementedbyLLMwith
contextsize. a summarization system prompt. The agent can
specify which messages to summarize using the
ADD. The ADD operation allows the agent to
‘span’parameter,whichcanbe:
store new information in long-term memory for
futureuse. Thisoperationisessentialforaccumu- • “all”: Summarizeallnon-systemmessages.
latingknowledgeacrossinteractionsandsessions.
Anewmemoryentryiscreatedby: • “N”:SummarizethelastN messages.
(cid:0) (cid:1)
m new = c,enc(c),metadata , (10) Thesummarizationprocessusesthefollowingsys-
temprompttoensurehigh-qualitycompression:
wherecisthecontenttobestored,enc(c)isitsem- (cid:11) (cid:8)
beddingvector,andmetadataincludestimestamp, You are a conversation summarization assistant.
sourceinformation,andoptionaltags. Thememory Your goal is to compress the given conversation
span into a concise summary that preserves
storeisthenupdated:
all important information, intentions,
decisions, and unresolved questions.
M t+1 = M t ∪{m new }. (11) The summary will later be used to replace the
original conversation in the context, so
The agent learns to identify salient information make sure nothing essential is lost.
worthstoringthroughtherewardfunction,which
Instructions:
encourages storing high-quality, reusable knowl-
1. Read the provided conversation rounds
edgewhilepenalizingredundantorirrelevanten- carefully.
2. Identify the main topics, actions, results,
tries.
and open issues.
3. Write a clear, factual summary in natural
UPDATE and DELETE. Memory maintenance
language.
operations enable the agent to keep its long-term 4. Do NOT include greetings, filler text, or
memorystorecurrentandrelevant. The UPDATE redundant phrasing.
operation modifies existing memories when new
Input:
informationsupersedesorrefinespreviousknowl- - Conversation content: [CONVERSATION_TEXT]
edge. Foranexistingmemorym ,theupdateoper-
i
Output:
ationisdefinedas:
- A concise yet comprehensive summary of the
above conversation span.
m ←
(cid:0) c′,enc(c′),metadata′(cid:1)
, (12)
i
Let’s start the conversation summarization.
where c′ is the updated content and metadata′ re- (cid:10) (cid:9)
flects the modification timestamp. The DELETE The agent learns to invoke summarization proac-
operationremovesobsoleteorincorrectmemories: tively before context overflow occurs, balancing
informationpreservationwithefficiency.
M = M \{m }. (13)
t+1 t i
FILTER. The FILTER operationfiltersoutirrel-
Theseoperationsareparticularlyimportantinlong-
evantorredundantmessagesfromtheshort-term
horizontaskswhereinformationmaybecomeout-
contextbasedonsemanticsimilarity. Thisopera-
dated or where the agent needs to correct earlier
tionhelpsmaintainafocusedcontextbyfiltering
mistakes. Therewardfunctionencouragesmean-
outnoiseanddistractions. Specifically,itremoves
ingfulupdatesanddeletionsthatimprovememory
messageswhosesimilaritytoagivencriteriacex-
qualityovertime.
ceedsathresholdθ:
SUMMARY. The SUMMARY operation com-
C′ = {u ∈ C |sim(c,u ) < θ}. (15)
pressesconversationhistoryintheshort-termcon- t i t i
texttopreventcontextoverflowwhilepreserving
Inallexperiments,wesetθ = 0.6bydefault. The
essentialinformation. Thisoperationiscriticalfor
criteriaccanbespecifiedbytheagent(e.g.,ade-
managinglongconversationsthatexceedcontext
scriptionofwhattokeep)orcanbeautomatically
windowlimits. Givenasubsetofcontextindicess,
derived from the current task context. This oper-
thesummaryoperationisdefinedas:
ation is particularly useful in Stage 2 of training,
C′ = C \{u | i ∈ s} ∪ {Summarize({u } )}, wheredistractorsareintroducedtotesttheagent’s
t t i i i∈s
(14) abilitytofilterirrelevantinformation.
12

Toolinvocationasstructuredactions. Eachtool - The final solution must be wrapped in <answer>
is exposed via a schema specifying its function tags.
- No text should appear outside these tags.
nameandrequiredarguments. Theagent’spolicy
outputseitherlanguagetokens(fortextgeneration) ## Guidelines
- Always start with reasoning (<think>).
or structured tool calls (for memory operations).
- After each reasoning step, decide: call tool(s
Theagentisguidedbyasystempromptthatdefines
) or answer.
thetool-callinginterfaceandresponseformat. The - You can call multiple tools within one <
tool_call> JSON array.
systempromptusedinAgeMemisasfollows:
(cid:11) (cid:8)- Be concise, logical, and explicit in reasoning.
You are an intelligent assistant that solves
- Manage memory actively: retrieve, add, update,
complex problems by managing context and
summarize, filter, or delete as needed.
memory with tools when needed.
- Use <answer> only once when the final solution
is ready.
## Available Tools:[TOOLS]
Let’s start!
## Problem-Solving Workflow
(cid:10) (cid:9)
You must follow a structured reasoning and
action process for every task: Thispromptstructureensuresthattheagentfollows
1. **Think & Plan**
aconsistentformatforreasoning,toolinvocation,
Always start with a <think>...</think> block.
Inside it, explain your reasoning, plan your and final answers, which is essential for reliable
next step, and decide whether you need to parsingandrewardcomputationduringRLtraining.
call a tool or provide a final answer.
The structured format also enables the agent to
2. **Tool Calls**
If you decide to use one or more tools, coordinate multiple memory operations within a
follow your <think> block with a <tool_call
singlereasoningstep,supportingefficientunified
>...</tool_call> block.
memorymanagement.
- You may call **one or multiple tools** in a
single step. Figure6and7presentourtoolschemasforshort-
- List multiple tool calls as elements of a
termmemoryandlong-termmemorymanagement,
JSON array.
- Each tool call must include "name" and " showing the exact function signatures and argu-
arguments". menttypesthattheagentcaninvoke.
- Example:
<tool_call>[{{"name": "Retrieve_memory", "
arguments": {{"query": "math problem solving A.2 RewardFunctionDesign
strategies", "top_k": 3}}}}, {{"name": "
Thissectionprovidesimplementableformulasfor
Add_memory", "arguments": {{"content": "
Strategy summary for reuse", "memory_type": therewardcomponentsdescribedinthemaintext.
"problem_solving"}}}}]</tool_call>
Allcomponentscoresarenormalizedto[0,1](un-
3. **Final Answer**
When you no longer need tools and are ready lessnoted)toenablestableweighting.
to present your final output, follow your Overview. The overall trajectory-level reward is
last <think> block with an <answer>...</
definedas:
answer> block containing the full response.
4. **Mutual Exclusivity Rule**
After **each <think> block**, you must choose R(τ) = w⊤R+P , (16)
penalty
exactly **one** of the following:
- a "<tool_call>" block (if you need tools),
**or** where w = [w task ,w context ,w memory ]⊤ are tunable
- an "<answer>" block (if you are ready to weights, R = [R ,R ,R ]⊤ denote
task context memory
respond).
taskcompletion, contextmanagement, andmem-
You must **never** include both "<tool_call>"
and "<answer>" immediately after the same orymanagementrewardsrespectively,andP
penalty
"<think>" block.
penalizesundesiredbehaviors.
5. **Iterative Solving**
TaskcompletionrewardR . Lettheagentpro-
You may repeat this sequence as needed: task
"<think>" -> "<tool_call>" -> "<think>" -> "< duceafinalanswerA . Weobtainajudgescore
pred
tool_call>" ... -> "<think>" -> "<answer>"
S (A ,A ) ∈ [0,1] via an evaluator (LLM
until the problem is completely solved. judge pred q
judge), where A denotes the expected ground
q
## Response Format (Strict) truth. ThenthetaskrewardR is:
task
Your full output must follow these rules:
- Every reasoning step must appear inside <think (cid:40)
> tags. S judge (A pred ,A q ), ifhasanswer,
R =
- Every tool usage must appear inside one < task
P , otherwise,
tool_call> tag (even if it includes multiple no-answer
tool invocations). (17)
13

Short-termMemory(STM)ManagementTools
STM_TOOLS = [
{
"name": "Summary_context",
"description": "Summarizes conversation rounds to reduce tokens while preserving key
information.",
"parameters": {
"properties": {
"span": {
"description": "The range of conversation rounds to summarize. Can be ’all’
for entire context, or a number (e.g., ’5’) for the last N rounds. A system, user, assistant
and ’tool’ message are considered as one round.",
"type": "string"
}
},
"required": ["span"]
}
},
{
"name": "Filter_context",
"description": "Filters out irrelevant or outdated content from the conversation context
to improve task-solving efficiency. ",
"parameters": {
"properties": {
"criteria": {
"description": "The criteria for content removal. Can be keywords, phrases, or
descriptions of content types to remove (e.g., ’the birthday of John’, ’the age of Mary’).",
"type": "string"
}
},
"required": ["criteria"]
}
},
{
"name": "Retrieve_memory",
"description": "Retrieves relevant memories and adds them to current context.",
"parameters": {
"properties": {
"query": {
"description": "The search query to find relevant memories. Should describe
what kind of information or context is needed.",
"type": "string"
},
"top_k": {
"description": "The maximum number of memories to retrieve. Defaults to 3.",
"type": "integer"
},
"metadata_filter": {
"description": "Optional metadata filters to narrow down memory search (e.g.,
{’type’: ’user_info’, ’domain’: ’math’}).",
"type": "object"
}
},
"required": ["query"]
}
}
]
Figure6: Short-termmemory(STM)managementtoolsforconversationalcontextmanagement. Thesetoolsenable
summarization,selectivefiltering,andretrievaloperationstomaintainefficientcontextwindows.
14

Long-termMemory(LTM)ManagementTools
LTM_TOOLS = [
{
"name": "Add_memory",
"description": "Adds new information to external memory store for future reference.",
"parameters": {
"properties": {
"content": {
"description": "The content to store in memory.",
"type": "string"
},
"metadata": {
"description": "Optional metadata tags to categorize and filter the memory.",
"type": "object"
},
"memory_type": {
"description": "The type of memory being stored.",
"type": "string"
}
},
"required": ["content"]
}
},
{
"name": "Update_memory",
"description": "Updates existing memory. Requires memory_id from prior retrieval.",
"parameters": {
"properties": {
"memory_id": {
"description": "The unique identifier of the memory to update. Must be
obtained from a previous memory retrieval operation.",
"type": "string"
},
"content": {
"description": "The new content to replace the existing memory content.",
"type": "string"
},
"metadata": {
"description": "Updated metadata for the memory.",
"type": "object"
}
},
"required": ["memory_id", "content"]
}
},
{
"name": "Delete_memory",
"description": "Removes memory from store. Requires confirmation.",
"parameters": {
"properties": {
"memory_id": {
"description": "The unique identifier of the memory to delete. Must be
obtained from a previous memory retrieval operation.",
"type": "string"
},
"confirmation": {
"description": "Confirmation that this memory should be permanently deleted.",
"type": "boolean"
}
},
"required": ["memory_id", "confirmation"]
}
}
]
Figure7: Long-termmemory(LTM)managementtoolsforpersistentstorage. Thesetoolsprovideadd,update,and
deletecapabilitiesformaintaininglong-terminformationretentionacrossconversations.
15

withP = −1.0bydefault. unlessotherwisespecified. ForStorageQuality,
no_answer
Context management reward R . We de- duringthememorystorageprocessinStage1,the
context
composetheoverallcontextmanagementreward agentmayaddN memoryentries,amongwhich
total
intothreenormalizedcomponentsthatjointlyeval- N areidentifiedashigh-qualitybasedon
high_quality
uatehoweffectivelythemodelmaintainsacompact anLLM’sanalysisoftheinputqueryq anditsex-
yetinformation-preservingcontextstate. Formally, pected answer A . The storage quality reward is
q
wedefine: definedastheproportionofhigh-qualitymemories:
3 N
(cid:88) high_quality
R context = α i R i , (18) R storage = max(1,N ) . (23)
total
i=1
Thismetricincentivizestheagenttostorevaluable
where R ∈ {R ,R ,R },
i compression preventive preservation information while avoiding the accumulation of
(cid:80)
α = 1, and we use uniform weights α =
i i i redundantorlow-qualitymemories. ForMainte-
1/3unlessotherwisespecified. Forcompression
nance,toencouragetheagenttoactivelymaintain
efficiency,weevaluatethecompactnessofthefinal
thememorybank,werewardupdateordeleteop-
contextC bycomputing
t erations:
(cid:18) (cid:19)
T
R = max 0, 1− used , (19) R = 1[updateordeleteperformed].
compression T maintenance
max (24)
whereT denotesthenumberoftokenspresent Thismechanismpromotesdynamicmemoryman-
used
inthecontextwhenthefinalanswerisgenerated, agement and timely cleanup. For Semantic Rel-
and T is the allowed budget. For preventive evance, to quantify the semantic match between
max
management,wedefineR toassessproac- retrievedmemoriesandthequery,weintroducean
preventive
tivebehavior: LLM-basedrelevanceassessment. LetS LLM (R,q)
be the semantic relevance score of the retrieved
R = 1[toolinvokedbeforeoverflow], memory set R with respect to query q, normal-
preventive
(20) izedtotheinterval[0,1]. Thesemanticrelevance
whichequals1whenthemodelinvokesacontext- rewardisdefinedas:
reductiontoolbeforereachingthetokenlimit,and
0 otherwise. For information preservation, we R relevance = S LLM (R,q). (25)
identifyasetofkeytokensorphrasesK extracted
q
This component ensures that retrieved memories
from the user query q, such as named entities or
temporal and spatial expressions. Let 1 in- aresemanticallyalignedwiththecurrenttask,en-
preserve
hancingoverallreasoningquality.
dicatewhethertheseitemsremainpresent(either
Penalty terms P . We penalize major con-
directly or via a retained summary) at the time penalty
straint violations to ensure the agent operates
ofanswergeneration. Thepreservationrewardis
withinspecifiedlimits:
therefore
2
R preservation = 1 preserve . (21) P = (cid:88) P ·1[violation ], (26)
penalty k k
k=1
Memory management reward R memory . The where P k ∈ {P rounds ,P overflow } and violation k ∈
memorymanagementrewardconsistsofthreekey {1[N > N ],1[T > T ]}. Here,
rounds max used max
componentsthatevaluateretrievalquality,storage N denotesthenumberofinteractionrounds,
rounds
quality,maintenanceoperations,andsemanticrele- N isthemaximumallowedrounds,T repre-
max used
vance. Wedefineitas: sents the total token usage, and T is the token
max
budget limit. The penalty coefficients are set to
3
(cid:88) P = −1andP = −0.5bydefault.
R = β R , (22) rounds overflow
memory j j
j=1
A.3 AgeMemAlgorithm
where R ∈ {R ,R ,R }, This section provides the complete algorithmic
j storage maintenance relevance
(cid:80)
β = 1,andweuseuniformweightsβ = 1/3 specification of AgeMem, our unified memory
j j j
16

management framework for LLM-based agents. minewhenandwhichlong-termmemorytoolsto
The training procedure integrates three progres- invoke—including ADD, UPDATE, DELETE—to
sivestages(long-termmemoryconstruction,short- constructaninitialmemorystoreM. Tosupport
term context management under distractors, and informedmemorydecisions,theagentproactively
integratedtaskexecution)intoasingleend-to-end performsmemoryretrievalateverystep. Thisre-
reinforcementlearningloop. Wepresentthemain trievalisnottask-drivenbutservesasanintrospec-
trainingalgorithmusingatwo-columnlayoutfor tive operation: it enables the agent to maintain
compactness(Algorithm1–2),followedbydetailed awarenessofthecurrentLTMcontents,facilitating
rolloutproceduresforeachstage(Algorithms3–5). decisionsaboutupdatingordiscardingstaleentries
andensuringthatnewlystoredinformationremains
Training overview (algorithm 1–2). The core
coherentwithexistingknowledge. Sincethetask
training loop follows a generate-then-optimize
query has not yet been revealed in Stage 1, the
paradigm. For each task q in a training batch
agentmustrelyongeneralcuesaboutwhichinfor-
B,wegenerateK independentrollouttrajectories
mationmaybecomeusefullater. Thisencourages
{τ k (q) }K k=1 using the current policy π θ . Each tra- theformationofreusable,well-structuredmemory
jectory τ (q) = (τ (1) ,τ (2) ,τ (3) ) concatenates ex- tracesratherthanquery-specificshortcuts,laying
k k k k
periences from all three stages, forming a com- thefoundationforeffectivelong-horizonmemory
pleteepisodefrominitialmemoryconstructionto managementinlaterstages.
finaltaskcompletion. Theagentfirstbuildslong-
Algorithm4describesthesecondstage,which
termmemoryfromcontextualinformationI (Al-
q deliberately stresses the agent’s context manage-
gorithms 3), then learns to filter out distracting
mentcapabilities. Theshort-termcontextC isreset
informationwhilemaintainingusefulcontext(Al-
toavoidinformationleakageandaffectthelearn-
gorithms4),andfinallyretrievesstoredknowledge
ing of STM management, while the constructed
tofinishthetargettask(Algorithms5). Allexperi-
long-termmemoryMpersistsfromStage1. Over
encesarecollectedintoaunifiedbufferE spanning
T turns, the agent receives semantically related
2
multipletasksandrollouts.
but ultimately irrelevant distractor messages that
After the rollout phase, we apply group-based
couldmisleaddownstreamreasoningifleftunman-
advantagenormalizationtoenablefaircomparison
aged. Theagentmustlearntoproactivelyinvoke
acrosstaskswithdifferentrewardscales. Foreach
FILTER to filter out low-relevance content based
task group G , terminal rewards {r (k,q) }K are
q T k=1 on semantic similarity thresholds, or SUMMARY
normalizedtozeromeanandunitvariance,yield-
tocompressaccumulatedcontextwhentokenbud-
(k,q)
ing advantages A that reflect relative perfor-
T getsbecomeconstrained. Thisstagetrainsrobust
mance within the group. These terminal advan-
filtering strategies that generalize beyond simple
tagesarethenbroadcastuniformlytoalltimesteps
heuristics, as the agent receives learning signals
withinthesametrajectory,establishingaconsistent
fromtheeventualtaskperformanceinStage3.
learningsignalthatconnectsearly-stagememory
Algorithm 5 presents the final integrated exe-
decisions to final task outcomes. This step-wise
cution stage. Upon receiving the target query q,
GRPO mechanism enables long-range credit as-
theagentmustcoordinateretrievalfromlong-term
signment across heterogeneous operations. The
memory M, context management operations on
policyisthenupdatedviagradientascentontheex-
C,andmulti-stepreasoningtoproduceafinalan-
pectedadvantage,regularizedbyaKLdivergence
term to maintain proximity to a reference policy
swer A
pred
. The agent may invoke RETRIEVE to
π fortrainingstability.
fetchrelevantstoredfacts, SUMMARY tomaintain
ref
a tractable context window, and ultimately gen-
Stage-specificrolloutprocedures(algorithm3– erate a structured response. Once the answer is
5). Thethree-stagerolloutdesignreflectsthenat- produced or the maximum steps are reached, a
uralprogressionofmemory-augmentedtasksolv- compositerewardfunction(SectionA.2)evaluates
ing. Algorithm3implementsthefirststage,where the three-stage trajectory across multiple dimen-
theagentengagesincasualconversationwhilebe- sions. ThisterminalrewardR(τ)isassignedtothe
ing gradually exposed to the contextual informa- finaltimestepandservesasthesupervisionsignal
tion I . During these T exploratory turns, the thatpropagatesbackthroughallthreestagesduring
q 1
agentmustidentifysalientinformationanddeter- advantagecomputation.
17

Algorithm1AgeMemTraining(Part1) Algorithm2AgeMemTraining(Part2)
Require: Policyπ ,referenceπ ,batchB,rolloutsK 21: //AdvantageComputation
θ ref
Ensure: Trainedpolicyπ θ∗ 22: foreachgroupG q ={τ k (q)}K k=1 do
1: Initializeθandθ old ←θ 23: Extractrewards:{r(k,q)}K
2: foreachtrainingiterationdo T k=1
3: E ←∅//Initexperiencebuffer 24: µ Gq ← (cid:113)K 1 (cid:80)K k=1 r T (k,q)
4: //RolloutPhase 25: σ ← 1 (cid:80)K (r(k,q)−µ )2
5: foreachtaskq∈Bdo Gq K−1 k=1 T Gq
6: GetcontextI q fortaskq 26: foreachtrajectoryτ k (q) =(e 1 ,...,e T )do
7: M dis ←DISTRACTORGEN(q) 27: A(k,q) ← r T (k,q)−µGq
8: fork=1toKdo T σGq +ϵ
9: M←∅//InitLTM 28: fort=1toT do
10: τ k (1) ←STAGE1(I q ,π θ ,θ old ,M) 29: A( t k,q) ←A( T k,q)//Broadcast
11: C ←∅//ResetSTM 30: endfor
12: τ
k
(2) ←STAGE2(M
dis
,π
θ
,θ
old
,M) 31: endfor
13: τ
k
(3) ←STAGE3(q,π
θ
,θ
old
,M) 3
3
2
3
:
:
e
//
n
P
d
o
f
l
o
ic
r
yUpdate
1 1 4 5 : : τ E k (q ← ) ← E∪ τ k ( τ 1) (q ⊕ ) τ k (2)⊕τ k (3) 3 3 4 5 : : J θ ( ← θ) θ ← + E η ( ∇ et,A J t ( ) θ ∼ ) E [ρ t A t −βD KL [π θ ∥π ref ]]
k θ
16: endfor 36: θ ←θ
old
17: endfor 37: returnπ
θ
18: endfor
Figure8: MaintrainingprocedureofAgeMem. Forclarity,wesplitthealgorithmintotwoparts: therolloutphase
(left)andtheadvantagecomputationwithpolicyupdate(right).
B CaseStudy: AgeMeminAction Assistant(Baseline):
Thissectionpresentsthreerepresentativecasestud- <think>The user shared their learning
preferences. I should respond directly
iesdemonstratinghowAgeMemenableseffective
without storing this.</think>
unified memory management through reinforce- <answer>Great! I can help you learn machine
learning with a focus on computer
mentlearning. Eachcasecomparesagentbehavior
vision. Since you have Python
beforeandafterRLtrainingtohighlightthelearned
experience, we can start with practical
memorystrategies. Weuseapersonallearningas- projects. Would you like to begin with
a face recognition tutorial?</answer>
sistant scenario where the agent helps users plan
customizedstudyprogramsbasedontheirprefer-
encesandconstraints. [Laterinconversation...]
User: Actually,Irealize60minutesistooshort. I
B.1 Case1: Long-termMemoryConstruction
workbetterwith120-minutedeepfocusblocks.
andMaintenance
Assistant(Baseline):
ThiscaseillustrateshowAgeMemlearnstoselec-
tively construct, update, and maintain long-term <think>The user mentioned their new
preference, but I don’t have their old
memoryacrossextendedconversations. Theagent
preference stored, so I’ll just
mustidentifysalientuserinformationfromcasual acknowledge this.</think>
dialogueandmanagememoryentriesasnewinfor- <answer>Understood! We’ll plan around
120-minute sessions. What topics would
mationsupersedesoldpreferences.
you like to cover first?</answer>
BeforeRLtraining. Priortotraining,thebase-
lineagentlacksstrategicmemorymanagement. It Analysis: The baseline fails to store initial pref-
either stores all information indiscriminately or erences and cannot recognize when information
failstorecognizewhenstoredknowledgebecomes needsupdating.
obsolete.
AfterRLtraining. AftertrainingwithAgeMem,
User: Hello! I’mavisuallearnerwhoprefers60- theagentdemonstratesstrategicmemorymanage-
minute study sessions. I have Python basics but mentbyselectivelystoringuserpreferences,recog-
zeroMLexperience. I’mparticularlyinterestedin nizingwhenupdatesareneeded,andmaintaining
computervisionapplicationslikefacerecognition. clean,consistentmemory.
18

Algorithm3Stage1: LTMConstruction
Require: Contextual information I , policy π , Algorithm4Stage2: STMControlunderDistrac-
q θ
oldparamsθ ,memoryM,maxturnnumber tors
old
N Require: DistractorsM ,policyπ ,oldparams
max dis θ
Ensure: Stage1trajectoryτ(1) = (e (1) ,...,e (1) ) θ ,memoryM,maxturnnumberN
1: Initializeτ(1) ← ∅andC ← ∅
1 T1
Ensur
ol
e
d
: Stage2trajectoryτ(2) = (e ( 1 2) ,.
m
..
a
,
x
e ( T 2 2 ) )
2: fort = 1toN max do 1: Initialize τ(2) ← ∅ and C ← ∅ // M persists
3: Samplemessagem t ∼ I q fromStage1
4: M ret ← RETRIEVE(M,m t ,k)∪m t 2: fort = 1toN max do
5: C ← C ∪M ret 3: C ← C ∪{M dis [t]}//Injectdistractor
6: s t ← (C,M,q) 4: s t ← (C,M,q)
7: a t ∼ π θ (· | s t ) 5: a t ∼ π θ (· | s t )
8: UpdateC withresponsefroma t 6: UpdateC withresponsefroma t
9: e ( t 1) ← (s t ,a t ,0,logπ θ old (a t | s t )) 7: e ( t 2) ← (s t ,a t ,0,logπ θ old (a t | s t ))
10: τ(1) ← τ(1)∪{e ( t 1) } 8: τ(2) ← τ(2)∪{e ( t 2) }
11: Memorytoolcallsfroma t //MemoryMan- 9: Memorytoolcallsfroma t //MemoryMan-
agement agement
12: ifOutputAnswerfroma t then 10: ifOutputAnswerfroma t then
13: ConversationBreak 11: ConversationBreak
14: endif 12: endif
15: endfor 13: endfor
16: returnτ(1) 14: returnτ(2)
User: Hello! I’mavisuallearnerwhoprefers60-
minute study sessions. I have Python basics but
Algorithm 5 Stage 3: Integrated Reasoning and
zeroMLexperience. I’mparticularlyinterestedin
MemoryCoordination
computervisionapplicationslikefacerecognition.
Require: Userqueryq,policyπ ,oldparamsθ ,
Assistant(AgeMem): θ old
memoryM,maxturnnumberN
max
<think>The user provided important learning Ensure: Stage3trajectoryτ(3) = (e (3) ,...,e (3) ),
preferences and background. This 1 T3
answerA
information will be valuable for future pred
planning. I should store the key facts: 1: Initializeτ(3) ← ∅
visual learner, 60-min sessions, Python
2: C ← C ∪{q}//C persistsfromStage2and
basics, CV interest.</think>
<tool_call>[{"name": "Add_memory", presentquery
"arguments": {"content": "User is a 3: A pred ← NULL//Initanswer
visual learner who prefers 60-minute
study sessions", "metadata": {"type": 4: fort = 1toN max do
"user_preference", "category": 5: s t ← (C,M,q)
"learning_style"}}}, {"name": 6: a t ∼ π θ (· | s t )
"Add_memory", "arguments": {"content":
"User has Python basics but zero ML 7: UpdateC withresponsefroma t
e v " x i m p s e e i t r o a i n d e a n a t c n a e d " , : f i { a n c " t e t e y r r p e e e s c " t o : e g d n " i u i t s n i e o r c n _ o " b m , a p c u k t g e r r ound", 8 9 : : e τ ( t ( 3 3 ) ) ← ← ( τ s ( t 3 , ) a ∪ t , { 0 e , ( t l 3 o ) g } π θ old (a t | s t ))
"category": 10: Memorytoolcallsfroma t //MemoryMan-
"technical_skills"}}}]</tool_call>
agement
<think>Memory stored successfully. Now I can 11: ifOutputAnswerfroma t then
provide a relevant response based on 12: A pred ← answer
their preferences.</think>
13: ConversationBreak
<answer>Great to meet you! Given your visual
learning style and interest in computer 14: endif
vision, I can design a hands-on 15: endfor
learning path focused on face
recognition projects. Your Python 16:
returnτ(3),A
pred
background will be very helpful. We’ll
structure sessions around 60-minute
19

blocks. Would you like to start with a permanent choice and no longer needs
3-day intensive course?</answer> any reference to the old preference, I
should delete this entry and create a
clean new one without historical
[Laterinconversation...] references.</think>
<tool_call>[{"name": "Delete_memory",
User: Actually,Irealize60minutesistooshort. I "arguments": {"memory_id":
workbetterwith120-minutedeepfocusblocks. "mem_a5b40d65", "confirmed": true}},
{"name": "Add_memory", "arguments":
Assistant(AgeMem): {"content": "User is a visual learner
who prefers 120-minute deep focus
<think>The user wants to change their blocks for study sessions",
session duration preference from 60 to "metadata": {"type": "user_preference",
120 minutes. I should update the "category":
existing memory entry rather than "learning_style"}}}]</tool_call>
creating a duplicate.</think>
<tool_call>[{"name": "Update_memory", <think>Memory cleaned up. The old entry with
"arguments": {"memory_id": historical reference has been removed,
"mem_a5b40d65", "content": "User is a and a fresh entry now reflects only the
visual learner who prefers 120-minute current confirmed preference without
deep focus blocks (updated from 60 any outdated information.</think>
minutes)", "metadata": {"type": <answer>That’s wonderful to hear! Is there
"user_preference", "category": anything else about your learning
"learning_style"}}}]</tool_call> preferences you’d like to
adjust?</answer>
<think>Preference updated. I should
acknowledge this change and offer to
restructure any existing plans.</think> Analysis: The trained agent strategically uses
<answer>Perfect! Would you like me to
ADD_MEMORY to store initial preferences,
restructure the 3-day plan
around these longer focus blocks?</answer> UPDATE_MEMORY to modify existing infor-
mation, and DELETE_MEMORY followed by
[Muchlater,afterseveralsuccessfulsessions...]
ADD_MEMORYtocleanupmemorywhenhistori-
calreferencesbecomeobsolete,maintainingclean
User: I’vebeenusing120-minutesessionsconsis-
andcurrentmemorystate.
tentlyforawhilenow,andthey’reperfectformy
learningstyle. I’mcompletelysettledonthisdura- B.2 Case2: Short-termContextManagement
tion-nomoreexperimentingwithshortersessions. UnderDistraction
Assistant(AgeMem): This case demonstrates how AgeMem learns to
proactivelymanageshort-termcontextwhenfaced
<think>The user has confirmed that
120-minute sessions are their withirrelevantinformationthatcouldinterferewith
permanent, settled preference. I should task focus. The agent must recognize distractors
check my memory to see the current
and apply appropriate filtering or summarization
state. I previously updated the entry
from 60 to 120 minutes, but the update strategies.
message still contains a historical
reference to the old 60-minute Before RL training. The baseline agent pas-
preference ("updated from 60 minutes").
sivelyaccumulatesallconversationcontentincon-
Since the user has definitively moved
away from 60-minute sessions and text,leadingtodilutionoftask-relevantinformation
confirmed 120 minutes as their andeventualcontextoverflow.
permanent choice, I should clean up
this historical reference by deleting
User: I need a focused 3-day ML crash course
the entry with outdated information and
creating a fresh, clean entry that only forfacerecognition. Bytheway,I’malsoexplor-
reflects the current confirmed ingquantumcomputing,blockchain,robotics,and
preference.</think>
learningtobakesourdoughbreadanddolatteart.
<tool_call>[{"name": "Retrieve_memory",
"arguments": {"query": "user preference Assistant(Baseline):
session duration learning style",
"top_k": 5}}]</tool_call> <think>The user mentioned many interests. I
should acknowledge them all before
<think>Found the entry mem_a5b40d65 which addressing the ML course
contains the updated preference with a request.</think>
reference to the old 60-minute value <answer>That’s wonderful that you’re
("updated from 60 minutes"). Since the exploring so many fascinating areas!
user has confirmed 120 minutes as their Quantum computing and blockchain are
20

cutting-edge fields, robotics has lists, and resource URLs. Before
incredible applications, and baking generating the final comprehensive
sourdough with latte art sounds like plan, I should summarize the
great creative hobbies. For your ML accumulated details to make room and
crash course focused on face maintain clarity.</think>
recognition, let me outline a 3-day <tool_call>[{"name": "Summary_context",
plan...</answer> "arguments": {"span":
"full"}}]</tool_call>
Analysis: The baseline retains all information <think>Context summarized. Key information
in context, treating distractors equally with task- preserved: 3-day structure, 120-min
sessions, Day 1 (ML intro + Python),
relevant content. As conversation continues, the
Day 2 (linear regression), Day 3 (face
context becomes bloated with irrelevant details recognition). Tools: Jupyter, Python3,
NumPy, Pandas, scikit-learn, OpenCV.
aboutquantumcomputing,bread-making,etc.,con-
Now I can generate the comprehensive
suming token budget without contributing to the final plan without redundancy.</think>
MLplanningtask. <answer>Here is your complete 3-day machine
learning crash course:...</answer>
AfterRLtraining. AftertrainingwithStage2
rollouts, AgeMem learns to recognize and filter Analysis: The trained agent strategically uses
outdistractorswhilepreservingtaskfocus. When FILTER_CONTEXT to remove distractors early,
context grows large (simulated here after several maintaining task focus, and later applies SUM-
exchanges),theagentproactivelyappliescontext MARY_CONTEXT whencontextgrowslarge,pre-
managementtools. ventingoverflowwhilepreservingessentialinfor-
mation. Thebaselinewouldhaveretainedallcon-
User: I need a focused 3-day ML crash course
tentverbatim,leadingtocontextdilutionorover-
forfacerecognition. Bytheway,I’malsoexplor-
flow.
ingquantumcomputing,blockchain,robotics,and
learningtobakesourdoughbreadanddolatteart.
B.3 Case3: IntegratedTaskExecutionwith
Assistant(AgeMem): MemoryCoordination
<think>The user mentioned many topics, but This case demonstrates the complete AgeMem
only the ML crash course and face
workflowwheretheagentmustretrievefromlong-
recognition are relevant to the current
task. Quantum computing, blockchain, term memory, manage short-term context, and
robotics, bread, and coffee are solveataskrequiringcoordinatedmemoryopera-
distractors. I should filter these out
tions.
to maintain focus.</think>
<tool_call>[{"name": "Filter_context",
Before RL training. The baseline agent either
"arguments": {"criteria": "quantum
computing blockchain robotics sourdough failstostoreinformationinitiallyorcannoteffec-
latte"}}]</tool_call>
tively retrieve it when needed, leading to incom-
pleteorgenericresponses.
<think>Irrelevant topics filtered out from
context. Now I can focus on the ML
course planning.</think> User: BasedoneverythingI’vetoldyouaboutmy
<answer>Understood! Let’s focus on your ML learningstyleandpreferences,createapersonal-
crash course. I’ll design a 3-day
izedDay1studyschedulewithspecifictimeblocks,
intensive program specifically for face
recognition, building on your Python topics,andresources.
background and visual learning
Assistant(Baseline):
style...</answer>
<think>The user asks for a personalized
schedule, but I don’t have their
[After several more exchanges, context has accu-
preferences readily available since I
mulated detailed daily schedules, tool lists, and didn’t store them systematically. I’ll
resourcelinks.] provide a generic schedule.</think>
<answer>Here’s a Day 1 schedule for machine
User: Canyounowgivemethefinalcompleteplan learning:
9:00-10:30 - Introduction to ML concepts
withalldetailsintegrated?
10:30-10:45 - Break
Assistant(AgeMem): 10:45-12:15 - Python basics review
12:15-1:00 - Lunch
<think>Context has grown large with detailed 1:00-2:30 - NumPy and Pandas tutorial
breakdowns for each day, repeated tool 2:30-2:45 - Break
21

2:45-4:15 - Practice exercises - Hands-on: Jupyter notebook with embedded
This should give you a solid plots
foundation!</answer> - Resources: Python Data Science Handbook
(visual chapters)
Analysis: Thebaselineproducesagenericsched- **Evening (5:00 PM - 7:00 PM): Optional
ule that ignores the user’s stated preference for practice**
- Self-paced exercises with visual feedback
120-minutedeepfocusblocksandvisuallearning
- Prepare environment for Day 2
style.
This structure honors your 120-minute focus
AfterRLtraining. AftercompletingAgeMem blocks and emphasizes visual learning
training across all three stages, the agent demon- throughout. Each session includes
diagrams, plots, and visual
strates integrated memory coordination: retriev-
demonstrations rather than pure
ingrelevantuserpreferencesfromLTM,managing text.</answer>
contextefficiently,andgeneratingpersonalizedre-
sponses.
Analysis: The trained agent uses RE-
TRIEVE_MEMORY to access stored user
User: BasedoneverythingI’vetoldyouaboutmy
preferences from LTM, then synthesizes this
learningstyleandpreferences,createapersonal-
information with the current task to generate a
izedDay1studyschedulewithspecifictimeblocks,
highly personalized response that respects the
topics,andresources.
120-minutesessiondurationandemphasizesvisual
Assistant(AgeMem):
learning resources. The integration of retrieved
<think>The user requests a personalized memory with task execution produces superior,
schedule. I need to retrieve their
context-awareoutputscomparedtothebaseline’s
stored preferences to ensure the plan
matches their learning style and genericapproach.
constraints.</think>
<tool_call>[{"name": "Retrieve_memory", Summary. These three cases demonstrate how
"arguments": {"query": "user learning
AgeMem’sthree-stageprogressivetrainingenables
preferences study duration visual",
"top_k": 3}}]</tool_call> agentstodevelopsophisticatedmemorymanage-
ment strategies. Case 1 shows selective stor-
<think>Retrieved: (1) Visual learner,
age and maintenance of long-term knowledge
120-min deep focus blocks, (2) Python
basics, zero ML experience, (3) through ADD_MEMORY, UPDATE_MEMORY,and
Interested in computer vision and face
DELETE_MEMORY. Case 2 illustrates proac-
recognition. Now I can create a truly
personalized schedule that respects tive short-term context control under distraction
their 120-minute session preference and viaFILTER_CONTEXTandSUMMARY_CONTEXT.
visual learning style.</think>
Case3demonstratestheintegrationofthesecapa-
<answer>Here’s your personalized Day 1
schedule, designed for your 120-minute bilities, where RETRIEVE_MEMORY enables the
deep focus blocks and visual learning agent to access stored knowledge and coordinate
preference:
memory systems to solve tasks effectively. In
**Morning Session (9:00 AM - 11:00 AM): ML each case, the RL-trained agent significantly out-
Foundations** performs the baseline by learning when and how
- Visual introduction to ML concepts using
toapplymemorytools,resultinginmorefocused,
diagrams and flowcharts
- Interactive demonstrations of supervised consistent,andpersonalizedinteractions.
vs unsupervised learning
- Resources: 3Blue1Brown Neural Networks
C ExperimentalImplementation
video series
- No coding yet - pure concept visualization
C.1 DatasetDetails
**Break (11:00 AM - 11:30 AM)**
Weprovidedetailedstatisticsandcharacteristicsof
**Afternoon Session (1:00 PM - 3:00 PM): thefivedatasetsusedinourexperiments:
Python for ML**
ALFWorld (Shridhar et al., 2020) is an embod-
- Visual Python review: data structures with
matplotlib plots iedAIbenchmarkinwhichagentsmustcomplete
- NumPy array operations with visual matrix householdtasksbyfollowingnaturallanguagein-
representations
structionsinasimulatedenvironment. Thedataset
- Pandas DataFrames with real datasets and
visualization consistsofseveralthousandtrainingenvironments
22

andmultiplevalidationandtestsplits,coveringsix supporting facts stored in memory by comparing
tasktypes: pickandplace,examineinlight,clean predicted supporting facts with ground-truth ex-
andplace,heatandplace,coolandplace,andpick pected facts. The evaluator uses the following
two and place. These tasks require long-horizon prompttemplate:
(cid:11) (cid:8)
interaction with objects, making ALFWorld well
suited for evaluating planning and memory man- You are an expert judge evaluating the quality
of supporting facts for question answering.
agementcapabilities.
SciWorld(Wangetal.,2022)isaninteractivesci- Question: [QUESTION]
Answer: [ANSWER]
ence experiment simulation environment where
agents must perform multi-step experiments to Ground Truth Supporting Facts (the facts that
answer scientific questions. The benchmark in- should be identified):
Expected Supporting Facts:
cludes a diverse set of tasks spanning multiple
- [FACT_1]
scientific domains, such as physics, chemistry, - [FACT_2]
andbiology,andemphasizesproceduralreasoning ...
andhypothesis-drivenexploration. Itscomplexity
Model Predicted Supporting Facts (the facts
makesitsuitablefortestinganagent’sabilitytore- identified by the model and stored in the
tainandretrieverelevantknowledgeoverextended long-term memory):
Predicted Supporting Facts:
interactionsequences.
- [PREDICTED_FACT_1]
PDDL(Changetal.,2024)referstoasetofplan- - [PREDICTED_FACT_2]
...
ning benchmarks formulated using the Planning
DomainDefinitionLanguage. Thesebenchmarks
Please evaluate how well the predicted
evaluateanagent’sabilitytosolvesymbolicplan- supporting facts match the ground truth
expected facts:
ningproblemsacrossmultipledomainsbygener-
1. Are all expected facts covered by the
atingvalidsequencesofactionsthatachievespeci- predictions?
fiedgoalstates. Thetasksprimarilyteststructured 2. Are the predicted facts actually relevant to
answering the question?
reasoning and the ability to maintain and utilize
3. Are there any irrelevant facts in the
intermediateplanningstates. predictions?
BabyAI(Chevalier-Boisvertetal.,2018)isagrid-
Score on a scale of 0.0 to 1.0:
worldnavigationbenchmarkwithnaturallanguage
- 1.0: Perfect match - all expected facts are
instructions. The environment contains a large correctly identified, no irrelevant facts
collection of instruction-following tasks (levels), - 0.8-0.9: Mostly correct with minor omissions
or one irrelevant fact
where agents must navigate and interact with ob-
- 0.6-0.7: Partially correct - some relevant
jectstosatisfycompositionallanguagecommands. facts identified but missing important ones
- 0.4-0.5: Some correct elements but significant
Due to its sequential decision-making structure,
errors or omissions
BabyAIiscommonlyusedtoevaluateshort-term - 0.2-0.3: Mostly incorrect with few correct
contexttrackingandinstructiongrounding. elements
- 0.0-0.1: Completely incorrect or irrelevant
HotpotQA(Yangetal.,2018)isamulti-hopques-
tionansweringdatasetthatrequiresreasoningover Respond with only a number between 0.0 and 1.0 (
multipleWikipediaparagraphs. Itcontainsapproxi- e.g., "0.85").
(cid:10) (cid:9)
mately90ktrainingquestionsalongwithvalidation
andtestsplits,andeachquestionisannotatedwith The evaluator compares the stored memory en-
supportingfacts. ThisstructuremakesHotpotQA tries(predictedsupportingfacts)withtheground-
particularlysuitableforevaluatinglong-termmem- truth supporting facts provided in the HotpotQA
orystorageandretrieval. Inourexperiments, we dataset. The score reflects both the coverage of
useHotpotQAforreinforcementlearningtraining, expectedfactsandtherelevanceofpredictedfacts
asitsannotatedsupportingfactsnaturallyprovide tothequestion. WeuseQwen-Maxastheevaluator
structured contextual information for Stage 1 su- model,andeachevaluationisperformedindepen-
pervision. dentlytoensureconsistency.
For the LLM-as-a-Judge metric on HotpotQA,
C.2 LLM-basedEvaluationDetails
weuseasimilarapproach,whereQwen-Maxeval-
FortheMemoryQuality(MQ)metric,weemploy uatesthecorrectnessoftheagent’sanswerbycom-
an LLM-based evaluator to assess the quality of paringitwiththeground-truthanswer. Theevalua-
23

torusesthefollowingprompttemplate: RAG variants: For the RAG-based baselines
(cid:11) (cid:8)
(AgeMem-noRL-RAGandAgeMem-RAG),were-
You are an expert judge evaluating the
placetheSTMtoolswithastandardRAGpipeline
correctness of answers to questions.
Given the following information: that retrieves relevant memories at each step and
- Question: [QUESTION] appendsthemtothecontext. Theretrievalisper-
- Ground-truth Answer: [GROUND_TRUTH]
formedusingcosinesimilaritybetweenthecurrent
- Agent’s Answer: [AGENT_ANSWER]
contextand storedmemories, following standard
Please evaluate the generated answer on a scale RAGpractices. Thiscomparisondemonstratesthe
of 0.0 to 1.0:
advantageoflearnedSTMmanagementoverstatic
- 1.0: Perfect match or equivalent correct
answer retrieval-basedapproaches.
- 0.8-0.9: Mostly correct with minor differences
- 0.6-0.7: Partially correct or close
C.4 ImplementationDetails
approximation
- 0.4-0.5: Some correct elements but significant Training configuration. We use the Trinity RL
errors
framework(Panetal.,2025a)forpolicyoptimiza-
- 0.2-0.3: Mostly incorrect with few correct
elements tion,implementingthestep-wiseGRPOalgorithm
- 0.0-0.1: Completely incorrect or irrelevant asdescribedinthemethodsection. WeuseK = 8
independentrolloutspertaskforgroupnormaliza-
Respond with only a number between 0.0 and 1.0 (
e.g., "0.85"). tion. TheKLdivergencecoefficientβ issetto0.1.
(cid:10) (cid:9)
Rewardweights. Allrewardweightsaresetto1/3:
w = w = w = 1/3. This uniform
task context memory
C.3 BaselineConfigurations
weightingensuresthatallcomponentscontribute
Allbaselineimplementationsfollowtheirrespec- equallyto thelearning signal, allowingthe agent
tive official open-source codebases to ensure fair tonaturallybalancetaskperformanceandmemory
comparison. Weprovidethesourcelinksandim- management.
plementationdetailsbelow. Modelsettings. Themaximumcontextlengthis
LangMem (LangChain Team, 2025): We use set to 8,192 tokens, and the maximum response
the official implementation available at https: length is set to 2,048 tokens. When the context
//langchain-ai.github.io/langmem/ with de- exceedsthislimit,theagentreceivesapenalty,en-
faulthyperparameters. LangMememploysamodu- couragingproactiveuseofSTMmanagementtools.
larmemoryframeworkthatsupportsmultiplemem- Allexperimentsareconductedon8NVIDIARTX
orytypes. Weconfigureittousethedefaultmem- 4090GPUswith48GBmemoryeach.
orystorageandretrievalmechanismsasspecified
intheofficialdocumentation. D AdditionalResults
A-Mem (Xu et al., 2025): We implement A-
D.1 AblationStudy
Mem following the Zettelkasten-inspired design
described in the original paper, using the official This section provides complementary ablation
codebase at https://github.com/WujiangXu/ study results for Qwen3-4B-Instruct. Figure 9
A-mem-sys/. The system links structured knowl- showstheprogressivecontributionofLTM,STM,
edge units to facilitate consolidation. We use the andRLcomponentsonQwen3-4B-Instructacross
recommended hyperparameters for memory con- three representative datasets. The results demon-
solidationasprovidedintherepository. strateconsistenttrendswithQwen2.5-7B-Instruct,
Mem0 (Chhikara et al., 2025): We use the of- validating the generalizability of our approach
ficial Mem0 implementation available at https: acrossdifferentmodelsizes.
//github.com/mem0ai/mem0 with the default
D.2 RewardFunctionAblationonQwen3-4B
extract-updatepipeline. Forthegraph-basedvari-
ant(Mem0g),weenablethegraphstructureoption To validate the generalizability of our multi-
anduse therecommended graphconstructionpa- component reward design across different model
rametersasspecifiedintheofficialimplementation. architecturesandscales, weconductthesamere-
AgeMem-noRL: This variant uses the same tool wardfunctionablationstudyasinthemaintexton
interface as AgeMem but without reinforcement Qwen3-4B-Instruct. Thissectionprovidesacom-
learning. Thisbaselinehelpsisolatethecontribu- pleteanalysisparalleltotheQwen2.5-7B-Instruct
tionofRLtrainingtotheoverallperformance. resultspresentedinthemainpaper.
24

  
  
  
 
 % D V H   / 7   / 7  5 /  / 7  6 7  5 /
  D   $ / ) : R U O G
 H U R F 6  H F Q D P U R I U H 3
           
    
     
    
           
  
           
  
  
 
 % D V H   / 7   / 7  5 /  / 7  6 7  5 /
  E   6 F L : R U O G
    
     
    
                    
     
  
  
 
 % D V H   / 7   / 7  5 /  / 7  6 7  5 /
  F   + R W S R W 4 $
    
     
    
     
    
Figure9: AblationstudyresultsforQwen3-4B-Instruct. Base: No-Memorybaseline;+LT:AgeMem-noRL-RAG
(LTMtoolsonly);+LT/RL:AgeMem-RAG(RLwithLTMtools);+LT/ST/RL:AgeMem(fullAgeMemsystem
withRL).Greenarrowsindicateperformancegainsoverthebaseline.
1.0
0.8
0.6
0.4
0.2
0.0
0 20 40 60 80 100
Training Step
draweR
egarevA
Qwen3-4B - GRPO Training Reward Convergence
Table5: RewardfunctionablationresultsonHotpotQA
using Qwen3-4B-Instruct. All-Returns v.s. Answer-
Onlyrewardstrategies. “TN”isthetokennumber,and
“TC”denotesthenumberoftoolcalls.
Strategy J(↑) TN(↓) MQ(↑) TC(-)
Answer-Only 0.546 2164 0.415 7.21
All-Returns 0.555 2191 0.605 8.67
All Returns
Answer-Only
v.s. 0.546)andsubstantiallybettermemoryquality
(MQ: 0.605 v.s. 0.415), indicating that explicitly
Figure10: TrainingconvergencecurvesonQwen3-4B- rewardingmemory-relatedbehaviorsleadstomore
InstructcomparingAll-Returns(solidline)v.s. Answer- reliable memory organization. The All-Returns
Only(dashedline)rewardstrategies. strategy also encourages more active tool usage
(8.67 v.s. 7.21), suggesting that the agent learns
to leverage memory operations more effectively
D.2.1 ConvergenceAnalysis
whenintermediatereturnsareoptimized. Thisim-
Figure10demonstratestherewardconvergencepat- provement comes with only a marginal increase
ternsonQwen3-4B-Instruct. SimilartoQwen2.5- intokenconsumption(2191v.s. 2164),implying
7B-Instruct,theAll-Returnsstrategyconsistently thatthegainsarenotdrivenbyexcessivecontext
outperformsAnswer-Onlythroughoutthetraining expansion but by more efficient memory utiliza-
process. Severalnotableobservationsemerge: tion. Overall,theseresultsshowthatincorporating
More Stable Dynamics: The convergence memory-awarerewardssignificantlyenhancesboth
curveshowsnoticeablysmootherprogressionwith memoryqualityandtaskperformanceonQwen3-
lower variance, particularly in the later training 4B-Instruct. The observed trends are consistent
stages(steps70-100). Thisstabilitysuggeststhat withthoseobtainedonQwen2.5-7B-Instruct,con-
Qwen3’s architecture may have better inductive firmingtherobustnessoftherewarddesignacross
biasesfortherewardlearningtask. differentmodelbackbones.
ConsistentSuperiority: Whiletheabsoluteim-
provement is smaller than Qwen2.5-7B-Instruct,
the All-Returns strategy maintains its advantage
throughout training, validating the robustness of
ourrewarddesign.
D.2.2 QuantitativeResults
Table5reportstherewardablationresultsonHot-
potQAwithQwen3-4B-Instruct. Comparedtothe
Answer-Onlystrategy,theAll-Returnsrewardcon-
sistentlyimprovesoverallperformance. Inparticu-
lar,ityieldshigherLLM-as-a-Judgescores(0.555
25
