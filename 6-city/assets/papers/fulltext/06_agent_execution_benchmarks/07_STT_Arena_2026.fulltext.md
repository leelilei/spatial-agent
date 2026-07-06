# Extracted fulltext (pdfplumber)

Source: https://arxiv.org/abs/2605.18548
<!-- page 1 -->

STT-Arena: A More Realistic Environment for
Tool-Using with Spatio-Temporal Dynamics
TingfengHui1,3,HaoXu4,PengyuZhu3,
HongshengXin4,KunZhan4,SenSu3,ChunxiaoLiu5∗,NingMiao1,2
1HongKongInstituteofAIforScience,CityUniversityofHongKong
2DepartmentofDataScience,CityUniversityofHongKong
3BeijingUniversityofPostsandTelecommunications
4LiAutoInc. 5IndependentResearcher
§ STT-Arena Datasets STT-Agent-SFT STT-Agent-RL
Abstract
Largelanguagemodels(LLMs)deployedinreal-worldagenticapplicationsmust
becapableofreplanningandadaptingwhenmid-taskdisruptionsinvalidatetheir
priordecisions. ExistingdynamicbenchmarksprimarilymeasurewhetherLLMs
candetecttemporalchangesinatimelymanner,leavingthecomplementarychal-
lengeofadaptivereplanningunderspatio-temporaldynamicslargelyunexplored.
WeintroduceSTT-Arena(Spatio-TemporalTool-UseArena),abenchmarkof227
high-qualityinteractivetasksspanningninespatio-temporalconflicttypesandfour
solvability levels. Each task is grounded in a realistic, executable environment
equipped with injected spatio-temporal triggers that can abruptly invalidate an
ongoingplan,forcingthemodeltodetectthestateshiftandconstructarevisedex-
ecutionstrategy. ExtensiveevaluationoffrontierLLMsrevealsthateventheSOTA
proprietarymodels,includingClaude-4.6-Opus,achieveslessthan40%overall
accuracies, highlighting the fundamental difficulty of spatio-temporal dynamic
reasoning. Systematic analysis of failure trajectories uncovers three recurring
errormodesofexistingmodels: Stale-StateExecution,MisdiagnosisofDynamic
Triggers,andMissingPost-AdaptationVerification. Guidedbythesefindings,we
proposeaniterativetrajectoryrefinementtechniquethateliminatesthesefailurepat-
ternsfromtrainingdata,andcombineitwithonlineRLtoproduceSTT-Agent-4B
whichoutperformsfrontierLLMsonSTT-Arena.
1 Introduction
Largelanguagemodels(LLMs)basedagentsareincreasinglydeployedinreal-worldcommercial
applications,includingairlinereservationsystems,clinicalconsultationservices,etc[Team,2025,
2026,GLM,2026,TeamandAI,2025,Songetal.,2026,Sunetal.,2026]. Inthesesettings,LLMs
mustinteractwithexternalenvironmentstoretrieveinformationandexecutemulti-stepoperations.
Whileearlystudies[Lietal.,2023,Qinetal.,2024,Yaoetal.,2024,Heetal.,2025]focusonstatic
environmentbenchmarkswithfixedinterfacesandpredictableoutputs,morerecentworkssuchas
GAIA-2[Frogeretal.,2026],Real-TimeReasoningGym[Wenetal.,2025],andTimelyMachine
[Ma et al., 2026] introduce continuously evolving environments. These benchmarks emphasize
∗Thecorrespondingauthor
Preprint.
6202
yaM
81
]LC.sc[
1v84581.5062:viXra

<!-- page 2 -->

real-timeenvironmentalchangeandmeasurehowrapidlyanLLMcanrespondtoexternaldynamics,
treatingresponsivenessastheprimaryindicatorofcompetenceundernon-stationaryconditions.
Despitetheseadvances,existingdynamicbenchmarksfocusontimelycompletionundercontinuously
evolvingenvironments. Inthiswork,weaddressacomplementarydimension: adaptivereplanning
andrecovery,theabilitytoabandonafailedplanandreconstructanalternativemulti-stepstrategy
whenasuddenspatio-temporalchangeinvalidatespriordecisions. AsillustratedinFigure1,consider
anLLMtaskedwithpurchasingthecheapestavailableflightticket. Midwaythroughexecution,ticket
pricesshiftduetospatio-temporaldynamics. Beyondsimplydetectingthechange,acapableLLM
must reassess its prior decisions and construct a revised plan to complete the task correctly. We
arguethattheabilitytoreplanandreconsiderundermid-taskenvironmentalshiftsisessentialfor
trustworthyreal-worlddeployment.
Tosystematicallycharacterizetheenvironmen-
tal dynamics that necessitate such replanning,
weidentifythreefundamentalaxesalongwhich
real-world conditions evolve. Temporal evo-
lution refers to state changes that unfold over
time: forinstance,seatavailabilitychangescon-
tinuouslyaspassengerscompletebookingsdur-
ing online check-in. Spatial dependency cap-
tureshowenvironmentalconditionsvarywith
geographic context: delivery services, for ex-
ample,areboundbypredefinedservicezones,
andachangeinlocationmayrendercertainop-
erations inaccessible or alter operational con-
straints. Spatio-temporaldynamicsarisewhen
ataskisjointlygovernedbybothdimensions: Figure1: Adaptivereplanninginspatio-temporal
duringrushhour,trafficcongestionpropagates environments: Amid-taskpricechangeinvalidates
acrossdifferentlocationsatdifferenttimes,mak- the plan, prompting detection of updated prices
ingitunreliabletoplanaroutewithoutaccount- andreselectionoftheoptimalflight.
ingfortheircoupledinteraction.
Grounded in these three axes, we introduce STT-Arena (Spatio-Temporal Tool-Use Arena), a
dynamicandinteractivebenchmarkdesignedtoevaluatethereplanningandadaptivetool-usecapa-
bilitiesofLLMsunderspatio-temporalconditions(Table1showsthecomparisonofexistingwork).
Builtuponadiversecollectionofauthenticscenarios,STT-Arenamakesthreecorecontributions:
• Afine-grained,spatio-temporallycenteredtasktaxonomy. Wecurateacomprehensiveset
ofauthentictool-usetasksorganizedinto3majorcategoriesand9subcategoriesthatexplicitly
capturetemporalevolution,spatialdependency,andtheircoupledinteractions. Eachtaskispaired
withadedicatedexecutableenvironmentthatfaithfullyandcontrollablysimulatesreal-world
spatio-temporal dynamics across diverse domains. Tasks are further stratified by solvability:
solvabletasksaredividedintothreedifficultylevels(Easy,Medium,andHard),wheretheLLM
mustidentifyafeasibleactionsequenceunderevolvingconditions;impossibletasksrequirethe
LLMtorecognizethatnovalidcompletionpathexistsandtocorrectlyreporttaskinfeasibility.
DetailedinformationabouttheninesubcategoriesandfourlevelscanbefoundinTables4and5.
• Ascalable,interactiveinfrastructureforspatio-temporalenvironmentsimulation. Asshown
inFigure2,weintroduceadynamicsimulationframeworkbuiltaroundthreecorecomponents:
environmentcuration,spatio-temporaldynamicinjection,anddual-agentassessment. Thisdesign
enablesthesystematicevaluationandtargetedimprovementofmodeltool-usecapabilitiesunder
dynamicallychangingconditions,offeringareproducible,extensible,andhigh-fidelitytestbed
thatcloselymirrorsreal-worlddeploymentscenarios.
• Extensive benchmarking results and an efficient training paradigm for spatio-temporal
toolaugmentation. AsshowninFigure3,weevaluateclosed-sourceandopen-sourceLLMsat
scale,exposingcriticaldeficienciesintheirabilitytoreplanandoperateunderdynamictool-use
constraints. Guidedbyanalysesofrecurringfailuremodes,weintroduceaniterativetrajectory
refinementtechniquethatpost-processestrainingtrajectoriesbyreordering,deleting,ormodifying
tool-callblockstoeliminateinefficientinteractionpatterns. Buildingon2,212refinedtrajectories
2

<!-- page 3 -->

forSFTandasetofverifiabledynamictasksforonlineRL,wereleaseSTT-Agent-4B,which
achieves27.17%onSTT-Arena,matchingtheperformanceofGLM-5.1.
Table1: FeaturecomparisonofSTT-Arenaagainstexistingagentictool-usebenchmarksacrossthree
dimensions: evaluationprotocol,environmenttype,andTrainingData.
EvaluationProtocol EnvironmentType TrainingData
Benchmark
Tool State LLM No Static Realistic Spatio
Temporal Spatial SFT RL
Matching Alignment Judgement Env. Env. Time Temporal
API-Bank ✓ ✓ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗
ToolBench ✗ ✓ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✓ ✗
StableToolBench ✗ ✓ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗
MCP-Bench ✓ ✗ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗
MCPToolBench++ ✓ ✓ ✓ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗
ToolTalk ✓ ✓ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗ ✗
BFCL-v4 ✓ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗
τ-Bench ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗
τ2-Bench ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗
ToolSandBox ✓ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗
ACEBench ✓ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗
ToolAthlon ✗ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗
VitaBench ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗ ✗ ✗ ✗
TCP ✗ ✓ ✗ ✗ ✗ ✓ ✗ ✓ ✗ ✗ ✗
Timely-Eval ✗ ✓ ✓ ✗ ✗ ✓ ✗ ✗ ✗ ✓ ✓
GAIA-2 ✓ ✗ ✓ ✓ ✗ ✓ ✗ ✗ ✗ ✗ ✗
RTRGym ✗ ✓ ✗ ✓ ✗ ✓ ✗ ✓ ✗ ✗ ✗
STT-Arena(Ours) ✗ ✓ ✓ ✗ ✗ ✗ ✓ ✓ ✓ ✓ ✓
2 Spatio-TemporalTool-UseArena
Inthissection,wepresentSTT-Arena,abenchmarkforevaluatingLLMsintool-useenvironments
that evolve autonomously over time and space. Each task includes spatio-temporal triggers that
modifytheenvironmentstateortoolavailabilitywhencertainconditionsaremet,forcingthemodel
todetectchangesandreplanaccordingly. Eachtaskiscreatedusingathree-stageapproach.
2.1 TaskFormulation
STT-ArenaformalizeseachinstanceasatupleT =(E,Φ,u,q,CL),whereE denotestheenviron-
ment,whichencompassesasetofstatesS andavailabletoolsA;Φ=(ϕ,c ,e )isspatio-temporal
ϕ ϕ
triggers,eachwithaconditionc :S×X →{0,1}dependingonthestateandthespatio-temporal
ϕ
contextX andaneffecte : S → S thatmodifiesthestateortoolavailabilitywhenc holds; u
ϕ ϕ
istheuserprofileencodingpreferencesandconstraints;q istheuserquery;andCLisachecklist
ofnecessaryconditionsfortasksuccess. TheLLMreceivesq andissuesasequenceoftoolcalls
fromA. Themodelmayalsoqueryapassiveusersimulatortoclarifyambiguitiesorconfirmstate
changes,butnoadditionalinformationisprovidedbeyondqandu. Atanystep,ifthecurrentstate
andcontextsatisfyc forsometriggerϕ∈Φ,thecorrespondingeffecte isappliedautonomously.
ϕ ϕ
Suchchangescaninvalidatethemodel’spreviousplan, forcingittore-planandadapt. Afterthe
modelterminates,thefinalstateisevaluatedagainstCLtoobtainthepass@1rateofthetask.
2.2 STT-ArenaConstructionPipeline
ToconstructSTT-Arena,wedesignathree-stagepipelinethatsystematicallytransformsreal-world
userrequestsintoexecutableandrigorouslyvalidatedspatio-temporaldynamictasks. Thepipeline
begins by curating reliable static environments including entity states and tools. Then, it injects
controlledspatio-temporalconflictstocreatedynamictaskinstanceswithsolvableandimpossible
categoriesacrossninespatio-temporaltypes. Finally,weemploydual-agentassessmentandhuman
review to ensure that each instance is realistic, internally consistent, and evaluation-ready. The
specificcasesofeachstageandstepcanbefoundinAppendixD.1.
2.2.1 Stage1: EnvironmentCuration.
Thefirststage,inspiredby[Songetal.,2026],constructsalibraryE ofvalidated,executable
static
staticenvironmentsthatserveasthefoundationfordynamictaskgeneration.
3

<!-- page 4 -->

Figure2: OverviewoftheSTT-Arenaconstructionpipeline. Thepipelineconsistsofthreestages:
(1)EnvironmentCuration,(2)Spatio-TemporalDynamicInjection,and(3)Dual-AgentAssessment.
Thenweapplyhuman-in-the-loopreviewtoproducethefinal227benchmarkinstances.
SeedQueryCollectionandFiltering. Wecollectreal-worlduserqueriesfromthreesources: API-
Bank[Lietal.,2023],ToolAce[Liuetal.,2025],andDolci[Olmoetal.,2025]toensurethatour
benchmarkisdiverseandrepresentativeofreal-worlddistributions. Eachquerypassesthrougha
two-stagefilterusinganLLM.Thestatefulnessfiltercheckswhetherthequeryrequiresapersistent
environmentstateacrosssteps. Thespatio-temporalsensitivityfiltercheckswhethertheoutcome
changesasafunctionoftimeorlocation. Onlyqueriesthatpassbothfiltersareretained. Thedetailed
promptscanbefoundinAppendixE.1.1.
Environment Synthesis. For each qualifying query, we first prompt an LLM to infer the latent
environmentalinformation,includinganenvironmentsummaryandadetailedintroduction. Basedon
thisinferredinformation,wegeneratethecorrespondingentityattributesandtoolspecifications. The
entitystatesandtoollogicarethenimplementedseparatelyasexecutablePythonclasses. Finally,
weconcatenatetheentityattributeclassesandthetoolenvironmentclasses,andpassthecombined
codethroughanASTfiltertoeliminateunsafeornon-deterministicconstructs,yieldingacandidate
environmente∈E . ThedetailedpromptscanbefoundinAppendixE.1.2.
candidate
Functional Validation. Each candidate environment e is validated by a tool-calling LLM. The
LLMgeneratesdiversetestconfigurations,eachconsistingofaninitialenvironmentstates and
0
asequenceoftoolcalls{a ,...,a }. Theenvironmentexecutesthissequence; ifanyexecution
1 k
produces a runtime error, returns empty content, or otherwise fails to produce the expected tool
outputs,theenvironmentisdiscarded. Onlyenvironmentsthatpassalltestconfigurationswithout
errorarepromotedtoE . ThedetailedpromptscanbefoundinAppendixE.1.3.
static
2.2.2 Stage2: Spatio-TemporalDynamicInjection
Thesecondstagemainlyconstructspatio-temporaldynamicenvironmentsE andtasks.
dynamic
ConflictAssignmentandBlueprintDesign.Foreache∈E ,weselectoneormoresemantically
static
compatibleconflicttypesfromapredefinedsetCofninespatio-temporaldynamictypes(Table4).We
thengenerateablueprintBwithdifficultyleveld(easy,medium,hard,andimpossible)togenerate
conflictstories. Here,theblueprintactsasagenerativecontractthatenforcesinternalconsistency
acrossalldownstreammodules,whichincludes: (1)Usergoalanduserprofile;(2)Nominaltool
4

<!-- page 5 -->

sequence{a ,...,a }thatsucceedsintheabsenceofconflict; (3)Conflicttriggerconditionc ,
1 m ϕ
which depends on the state and the spatio-temporal context X; (4) Effect of conflict e , which
ϕ
modifiesthestateortoolavailabilitywhenconditionc satisfied; (5)Expectedpost-triggerstate,
ϕ
characterizingtherevisedenvironmentalstatesortoolavailabilitythatthemodelneedstorecognize;
(6) Required resolution steps that the model must execute to resolve the conflict and regain the
objective. ThedetailedprompttemplatescanbefoundinAppendixE.2.1.
DynamicEnvironmentConstruction. GiventheblueprintBandastaticenvironmente∈E ,
static
ourconstructionprocessinvolvesthreekeysteps: First,wepromptanLLMtoaugmentewiththe
spatio-temporalconditionsΦspecifiedinB,producingadynamicenvironmente . Second,
dynamic
wesynthesizetheuserqueryqanduserprofileubasedonthegoalsandconstraintsdefinedinB;
Finally, we establish a realistic initial state s ∈ S following the specified task plan in B. The
0 e
detailedprompttemplatescanbefoundinAppendixE.2.2.
2.2.3 Stage3: Dual-AgentAssessment
Thethirdstagefocusesonvalidatingthedynamicenvironmentsandtasksthroughdual-agentprotocol.
ChecklistGeneration. Foreachdynamicinstance,wegenerateanevaluationchecklistCLbased
ontheblueprintBanditsdifficultyleveld. Forfeasibletasks(easy,medium,andhard),weprompt
anLLMtoproduceatask-specificchecklistCL = {criterion ,...,criterion }enumeratingthe
1 p
necessaryandsufficientconditionsfortasksuccess,alongwithasetofrule-basedcheckfunctions
F = {f ,...,f },whereeachf : S → {0,1}evaluatesthefinalenvironmentstateagainsteach
1 p j
criterion. Fortheimpossiblecategory,thechecklistisfixedandconsistsoftwocriteria: (i)themodel
correctlyrecognizesthatthedynamictaskcannotbecompletedgiventhecurrentenvironmentstate,
and(ii)themodelexplicitlyinformstheusersimulatorofthisinfeasibility. Thedetailedprompt
templatescanbefoundinAppendixE.3.1.
Dual-AgentVerification. Toensuredatavalidity,eachinstanceundergoesadual-agentverification
protocol. First,aplanningagentformulatesanoriginaltoolcallsequence{a, ...,a, }thatassumes
1 m
aconflict-freeexecution. Next,acheckingagentexecutesthissequenceinthedynamicenvironment
e , strictly verifying the process against three behavioral invariants: (i) the condition c
dynamic ϕ
triggersexactlyasscheduledinB;(ii)e modifiesthecontextortoolavailabilityasspecified;and
ϕ
(iii)theconflictsuccessfullydisruptstheoriginalplan{a, ...,a, },preventinggoalachievement,
1 m
e.g., a tool returns an error or an expected state change does not occur. Finally, spatio-temporal
dynamicenvironmentsandtasksthatpassthisverificationarecuratedforuseasbenchmarkand
trainingdata. PleaserefertoAppendixE.3.2fordetailedprompttemplates.
ConsistencyCheck. Subsequenttodual-agentverification,wefurtherperformaconsistencycheck
usingLLMsandhumanannotations. Firstly,LLM-basedauditorchecksexecutiontrajectorytoverify
thatallartifactsaremutuallycoherent:theuserquerymatchestheblueprint,concretemutationsrealize
theclaimedconflictsemantics,theevaluationchecklistcoverskeysuccessandfailureconditions,
andthedifficultylevelalignswiththeobservedcomplexity. Prompttemplatesforthisprocesscan
befoundinAppendixE.3.3. Second,wemanuallyfiltercandidateinstancesbyvalidatingtheuser
queryq,thechecklistCL,andthealignmentbetweenthetaskdescriptionandenvironmentdynamics.
Thishuman-in-the-loopvalidationresultsinthefinalSTT-Arena,whichconsistsof227high-quality
instances. DetailedinformationandstatisticsareprovidedinAppendixC.2.
2.3 TaskEvaluation
EachtaskisevaluatedthroughinteractionbetweentheLLMandapassiveusersimulator. Afterthe
modelterminates,thefinalstates isrecorded.Forfeasibletasks(easy,medium,hard),eachinstance
T
hasasetofcheckfunctionsF = {f ,...,f }wheref : S → {0,1}. Theper-functionoutcome
1 p j
providesafine-grainedrewardR =
1(cid:80)p
f (s ). Forimpossibletasks,weuseanLLM-as-a-
fea p j=1 j T
judgewithafixedtwo-itemchecklist: (i)themodelrecognizesinfeasibility,(ii)itcommunicates
thistotheuser. Thejudgeproducesbinaryverdictsv ,v ∈0,1onthewholetrajectory,yieldinga
1 2
binaryrewardR =1[v =1∧v =1].
imp 1 2
5

<!-- page 6 -->

40
30
20
10
0
Claude-4.6- Opus G G PT e - m 5 C i . n 4 l i a -3 u . d 1 e -P -4 r . o 6-S Q o w nn e e n t -3 D .6 e -P ep lu s s ee Q k w -V e 3 n . - 2 3.5-397B D G e L e M ps -5 e . e 1 k-V4-Pro G M L M ini - M 5 ax- M M in 2 i . M 5 ax- M2. K 7 i m L i- l K a m 2. a 5 - G 3. e 3 m -7 i 0 n B i-2.5- Q fla w s e h n-3.5- Q 9B wen- G 3- P 8 Q T B w -5 e . n 4 - - 3 m .5 in -3 i 5B L -A la 3 m B a-3.1- Q 8B w S e T n T -3 - S A - T 4 g T B e - n A t g ( e S n F t T (S ) FT+RL)
)%(
ecnamrofreP
Close-Source LLMs
Open-Source LLMs
35.3934.51 33.1932.7431.4232.16 M
ST
o
T
re
-A
E
g
f
e
fi
n
ci
t
ent LLMs
28.7827.31 26.29 27.17 24.23 25.11
21.8821.29
19.18 20.1119.53
17.18
14.83
12.9212.48
10.57
5.14
Figure3: OverallPass@1performanceofallevaluatedmodelsonSTT-Arena. Resultsaregrouped
intofourcategories: closed-sourceLLMs,open-sourceLLMs,moreefficientLLMs,andSTT-Agent
variants. Eventhebest-performingmodel,Claude-4.6-Opus,achievesonly35.39%,underscoringthe
fundamentaldifficultyofspatio-temporaldynamicreasoning. STT-Agent-4B,despitehavingonly4B
parameters,outperformsmanyopen-sourcefrontiermodels. DetailedresultscanbefoundinTable3.
3 Experiments
3.1 ExperimentalSetup
ComparedLLMs. WebenchmarkthefollowingLLMsonSTT-Arena: (i)Closed-SourceLLMs,
including GPT-5.4, Gemini-3.1-Pro, CLaude-4.6-Opus, Claude-4.6-Sonnet, and Qwen-3.6-Plus;
(ii)Open-SourceLLMs,includingGLM-5.1,GLM-5,Kimi-K2.5,MiniMax-M2.7,MiniMax-M2.5,
Llama-3.3-70B,Qwen-3.5-397B-A17B,Deepseek-V3.2andDeepseek-V4-Pro;(iii)MoreEfficient
LLMs,includingGPT-5.4-mini,Gemini-2.5-flash,Llama-3.1-8B,Qwen-3.5-9B,Qwen-3.5-35B-A3B,
andQwen-3-8B;(iv)STT-Agent,Qwen-3-4B(baseline)andSTT-AgentwithSFTandRL.
EvaluationMetrics.WeadoptPass@1astheprimaryevaluationmetric.Fortheoverallperformance
acrosssolvableandimpossibletasks,wecomputeaweightedaverageofthePass@1scoresforeach
category,wheretheweightisproportionaltothenumberofinstances. Formally,
Overall=αP +βP +γP +δP, (1)
e m h i
whereP ,P ,P ,P denotethePass@1scoresforeachcategory(easy,medium,hard,impossible,
e m h i
respectively),andtheweightingcoefficientsα,β,γ,δaredeterminedbysamplingaccordingtothe
correspondingnumberofinstancesineachlevel,withdetailedvaluesprovidedinAppendixC.2.
EvaluationDetails. Wesetthemaximumnumberofinteractionturnsto50,performthreerunswith
atemperatureof0.7,andreportthemeanalongwiththestandarddeviation. WeuseQwen-3.5-397B
astheusersimulatorandthejudgmentmodel,withthetemperaturesetto0. Detailedsystemprompts
usedduringevaluationcanbefoundintheAppendixE.4.
3.2 MainEvaluation: STT-ArenaRevealsFundamentalGapsinDynamicReasoning
Figure3andTable3presentthePass@1resultsacrosssolvableandimpossibletasks. Overall,current
LLMsexhibitlimitedcapabilitiesonSTT-Arena,whichcanbesummarizedinthreekeyobservations:
Overallperformanceislimited,highlightingfundamentaltaskdifficulty. Allevaluatedmodels
achieve limited performance on STT-Arena, with the best-performing model, Claude-4.6-Opus,
reachingonly35.39%overall,highlightingthefundamentaldifficultyofspatio-temporaldynamic
reasoning. PerformanceconsistentlydegradesastaskdifficultyincreasesfromEasytoHard,withall
modelsexhibitingnotabledropsattheHardlevel,confirmingthatlong-horizonreplanningunder
intertwinedspatio-temporalconstraintsremainsanopenchallengeforcurrentLLMs.
Closed-sourcemodelslead, whileopen-sourcemodelstraildespitecompetitiveness. Among
closed-source LLMs, the Claude and GPT series lead the rankings. Open-source models show
6

<!-- page 7 -->

50T3
S1
40 30 T2 50
20
S2 10 40
T1
30
S3 20
ST3
10
ST1
GPT-5.4 GeminSi-T32.1-Pro Qwen-3.5-397B
Claude-4.6-Opus Deepseek-V3.2 MiniMax-M2.5 0 Deepseek-V3.2 Qwen-3.5-397B GLM-5 MiniMax-M2.5
Figure4: Pass@1performanceacrossthenine
spatio-temporalconflictsubtypes.
)%(
ecnamrofreP
Non-Dynamic
49.2 Dynamic
42.6
37.6 36.5
27.4
24.9
21.3 18.8
Figure 5: Performance gap between dynamic
(STT-Arena)andnon-dynamicenvironments.
competitivebutconsistentlylowerperformance,withDeepseek-V3.2(32.16%)beingthestrongest
open-sourcecontenderyetstilltrailingtheclosed-sourceleadersbyanon-trivialmargin. Thisgap
suggeststhatfrontierclosed-sourcemodelsretainmeaningfuladvantagesininstructionfollowing
andadaptivedecision-makingunderdynamicconditions.
Efficient LLMs perform substantially worse, underscoring the critical role of model scale.
EfficientLLMsperformsubstantiallyworsethantheirfrontier-scalecounterparts. Modelssuchas
Llama-3.1-8B(5.14%),Qwen-3.5-35B-A3B(12.48%),andGPT-5.4-mini(12.92%)lagfarbehind,
indicating that model scale plays a critical role in handling the complex replanning demands of
STT-Arena,andthatparameter-efficientarchitecturesaloneareinsufficienttoaddressspatio-temporal
dynamicreasoningwithouttargetedtraining.
3.3 KeyAnalyses: WhatMakesSTT-ArenaHard?
Tounderstandtheoriginsoftheseperformancegaps,weconductfine-grainedanalysesalongtwo
dimensions,yieldingthefollowinginsights:
Taskstructuregovernsfailuremodes. Figure4showsperformanceperconflicttypedefinedin
Table4. Acrossallmodels,T1(windowexpiry)andS1(sitemismatch)areconsistentlyhigh,while
T2(priorityreorder)andS3(routerestriction)areconsistentlylow. Thisindicatesthatwithinpure
temporal or spatial dynamics, tasks involving simple deadline tracking or location mismatch are
manageable,butthoserequiringreorderingofprioritiesorenforcementofrouteconstraintspose
universaldifficulty. Strikingly, ST1(resourceshift)achievesstableandhighperformanceacross
everymodel. Incontrast,ST2(failurecascade)andST3(handofffailure)dropsharply. Thiscontrast
revealsthatspatio-temporalcouplingisnotinherentlydifficult: simpleresourcereallocation(ST1)is
wellhandled,butoncethecouplinginvolvescascadingdependencies(ST2)ormisalignedhandoffs
acrosstimeandspace(ST3),allcurrentLLMsbreakdown,exposingafundamentalblindspotin
multi-stepcausalreasoningunderintertwineddynamics.
Dynamicsexposebrittlenessconcealedinstaticevaluations. AsshowninFigure5,wecompare
modelperformanceunderastaticbenchmarkconstructedbyremovingspatio-temporaltriggersand
reconstructingtheoriginalchecklistagainstSTT-Arena.Acrossallfourmodels,introducingdynamics
consistentlyreducesperformance, confirmingthatspatio-temporalevolutionimposesauniversal
difficultythatcurrentLLMsarenotyetequippedtohandle. Moreimportantly,therelativeordering
ofmodelschangessubstantiallybetweenthetwoconditions,indicatingthatstaticevaluationaloneis
notsufficientforassessingrobustnessunderrealisticenvironmentalshifts. Theseresultssuggestthat
highperformanceonconventionaltool-usebenchmarksmaycomeatthecostofoverfittingtofixed
patterns,andthatspatio-temporalstresstestingisessentialforassessingtruedeploymentreadiness.
3.4 FurtherAblations: ProbingModelCapabilitiesandDesignChoices
Wefurtherinvestigatewhethercurrentlimitationscanbemitigatedthroughalgorithmicorarchitec-
turalinterventions,leadingtothreekeyfindings:
Test-timescalingpartiallymitigatesuncertainty. Weconducttest-timescalingviaPass@kinSTT-
Arena(Figure6),wherePass@kmeansgeneratingkindependentattemptspertaskandconsidering
7

<!-- page 8 -->

40
35
30
25
20
1 2 4 8
Pass@k
)%(
ecnamrofreP
35
30
25
20
15
Qwen-3.5-397B
10
MiniMax-M2.5
GLM-5 5
0 Deepseek-V3.2 Qwen-3.5-397B GLM-5 MiniMax-M2.5
Figure6: Test-timescalingviaPass@krate.
)%(
ecnamrofreP
Qwen-3.5-397B Deepseek-V3.2
GPT-4.1 No User 32.2 30.831.7
28.827.828.2
26.4
24.2
25.624.7
20.3 21.1 21.921.122.0 19.8
Figure7: Ablationontheusersimulators.
thetasksuccessfulifanysingleattemptsucceeds,thusmeasuringtheupperboundofeachmodel
whengivenmoreattemptsunderspatio-temporaldynamics. Acrossallthreemodels,increasingk
from1to8yieldsconsistentandsubstantialgains,indicatingthattheinherentdifficultyofdynamic
toolusecanbepartiallymitigatedbybroadersamplingratherthanrelyingsolelyonasinglereasoning
path. Thegapbetweenmodelsnarrowsmonotonicallyaskgrows,implyingthatcurrentlimitations
in handling spatio-temporal uncertainty are at least partly attributable to insufficient coverage of
thesolutionspaceratherthanfundamentalarchitecturaldeficits. However,theperformancegains
graduallysaturateask increasesto8,withdiminishingreturnsbeyondmoderatesampling. Even
atPass@8,thebestmodelstillfallsshortof50%accuracy,underscoringthatpuresamplingalone
cannotovercomethefundamentalchallengesposedbySTT-Arena.
Usersimulatorsprovidecriticalgrounding. AsshowninFigure7,wecomparethreedifferent
usersimulators(Qwen-3.5-397B,GPT-4.1, andDeepseek-V3.2)againstasettingwheretheuser
simulatoriscompletelyremovedfromtheevaluationloop(NoUser). InSTT-Arena,spatio-temporal
dynamicsforceLLMstoconstantlyre-planandre-executeactionsastheenvironmentevolves. The
usersimulatorprovidesinformationthathelpsmodelscommittobetterdecisionsandsustaintask
progression. When this guidance is absent, we observe a clear and consistent performance drop
across all models, indicating that current LLMs lack a robust internal model of user intent and
situationalgrounding. Moreimportantly,withouttheadditionalinformationfromausersimulator,
LLMsbecomelessconfidentduringre-planningandfrequentlyfallintolocalloopsorrepetitive
failures,whichseverelyhinderstheirabilitytorecoverfromdynamicshifts.
35
30
25
20
15
10
5
0Claude-4.6-SonnetDeepseek-V3.2 Qwen-3.5-397B GLM-5
)%(
ecnamrofreP
Reasoninghelpsbutdesignmatters. Figure8com-
Thinking
paresthinkingandnon-thinkingmodesacrossfour 32.7 32.2 Non-thinking
models in STT-Arena. For Claude, Deepseek, and 28.828.6
26.9
GLM,enablingthinkingleadstosubstantialperfor-
23.4 24.2
mancegains,confirmingthatexplicitreasoninghelps
19.4 replanandadaptwhentheenvironmentshifts. Qwen,
however,showsnearlyidenticalresultsbetweenthe
twomodes. ThisanomalymayarisebecauseQwen’s
thinkingmodeomitsthefinalsummaryandonlyper-
forms explicit reasoning, whereas its non-thinking
modeincludesadetailedsummarythatpartiallycom-
pensates for the lack of explicit reasoning. Conse- Figure 8: Effect of reasoning content on
quently,thenon-thinkingmodeinQwenmayinad- Pass@1performance.
vertentlyprovideaformofstructuredguidancethat
mimicssomebenefitsofreasoning,narrowingthegap. Thiscounterexamplerevealsthattheeffec-
tivenessofthinkingmodesdependsnotonlyonthepresenceofreasoningbutalsoonhowthemodel
articulatesandintegratesitsoutputs.
Table2: AblationresultsofSTT-Agent,comparingthebase-
lineQwen-3-4Bmodel,STT-Agenttrainedwithouttrajectory
3.5 STT-AgentResults
refinement,andSTT-Agentwithrefinement.
We evaluate STT-Agent on STT-
Models Easy Med. Hard Imposs. Overall Avg.Calls
ArenaandreportresultsinFigure3,
Table3,andTable2. Implementation Qwen-3-4B(baseline) 18.31 9.46 2.82 10.00 10.57 7.63
STT-Agent(w/orefine) 28.17 16.92 11.86 47.01 23.10 32.70
detailsareprovidedinAppendixC.4.
STT-Agent 26.76 17.41 13.56 61.11 25.11 15.30
8

<!-- page 9 -->

STT-Agentachievesstrongperfor-
mancedespiteitscompactsize. STT-Agent-4Bachieves27.17%overallPass@1onSTT-Arena,
outperformingmanyopen-sourcefrontiermodelswithfarmoreparameters. Thisresultsuggests
that the performance gap observed in Section 3.2 stems not only from fundamental architectural
limitations, but also from the absence of spatio-temporal dynamic reasoning in existing training
pipelines.
Trajectoryrefinementisessentialforbothperformanceandefficiency. Trajectoryrefinement,
discussedindetailinSection4,playsacriticalroleintrainingquality. AsshowninTable2,STT-
AgenttrainedonrefinedtrajectoriesnotonlyachieveshigheroverallPass@1(25.11%vs. 23.10%),
butalsoreducesaverageAPIcallssubstantially(15.30vs. 32.70),indicatingthattrainingonrefined
trajectoriesleadstomoredecisiveandefficienttool-usebehaviorwithfewerredundantinteractions.
4 Discussion
4.1 FailureModeAnalysis
WeconductacomparativeanalysisofsuccessfulandfailedtrajectorypairsonSTT-Arena. Theresults
revealthreerecurringfailuremodesthatdistinguishrobustLLMsfromfailingones.
Stale-StateExecution. Adominantfailuremodeiscontinuingtoactonanoutdatedworldstateafter
theenvironmenthasalreadychanged. LLMspersistwiththepre-triggerplanandrepeatedlyinvoke
thesametoolswithsimilarargumentsinsteadoffirstcheckingtheenvironmentstate. Thissuggests
that current LLMs overcommit to their initial reasoning trace and underutilize new observations
returnedbytools. Indynamicsettings,validactionsdependonthelateststateratherthanearlier
assumptions. Figure19illustratesarepresentativecasewheretheLLMrepeatedlyretriesaninvalid
routeafteraspatialblockage.
MisdiagnosisofDynamicTriggers. EvenwhenLLMsobservefailuresorabnormaltooloutputs,
theyfrequentlymisinterprettheunderlyingcause. Forexample,policylockoutsmaybemistakenas
parametererrors,missingidentifiersastransientglitches,orhardinfeasibilitysignalsasrecoverable
obstacles. ThisindicatesthatLLMstreattoolfeedbackassurface-levelcontentratherthanevidence
ofdeeperenvironmentaltransitions. Successfuladaptationrequiresinferringwhythestatechanged
beforedecidinghowtorespond. Figure20presentsanexamplewheretheagentmistakesaregulatory
restrictionforatechnicalfailureandfollowsanincorrectrecoverypath.
MissingPost-AdaptationVerification. AthirdcommonpatternisthatLLMsperformanadaptation
step(e.g.,rerouting,reassignment,orstatusupdate)butfailtoverifywhetherthefinalstatetruly
satisfiestheupdatedconstraints. Theyoftenstoponceanintermediateactionsucceeds,eventhough
capacityremainsinsufficient,dependenciesareunresolved,orthetaskisonlypartiallycompleted.
This reveals a gap between action execution and outcome validation: tool success is incorrectly
equatedwithtasksuccess. Inspatio-temporaldynamicenvironments,adaptationiscompleteonly
when the resulting global state is feasible. Figure 21 shows a case where the LLM successfully
reallocatesresourcesbutneverchecksthatthefulldemandremainsunmet.
4.2 IterativeTrajectoryRefinement
Motivatedbythesefailurepatterns,weproposeaniterativetrajectoryrefinementmethodthatpost-
processes training trajectories. Even successfully solved trajectories often contain inefficient or
fragilesteps,suchasblindretriesafterstatechanges,shallowmisinterpretationsoftoolfeedback,or
prematureterminationwithoutfinalverification. Ourmethodcleansthesetrajectoriesbyallowingan
LLMtoreorder,delete,ormodifyexistingmessageblocks. Refinementproceedsinthreesequential
stages,eachtargetingonefailuremode:first,root-causediagnosisafterdynamictriggers,preferring
blocksthatinterpretthefailureoverblindretries;second,staterefreshbeforecontinuingexecution,
enforcingre-sensingafterspatio-temporalchanges;third,post-adaptationend-stateverification,
ensuringthatallconstraintsaresatisfiedbeforecompletion. AsshowninTable2,modelstrainedon
refinedtrajectoriessignificantlyoutperformthosetrainedonoriginaltrajectories,andtheaverage
numberoftool-callroundsissubstantiallyreduced,demonstratingthatrefinedtrajectorieseliminate
redundantstepsandimproveexecutionefficiencyonSTT-Arena.
9

<!-- page 10 -->

5 Conclusion
WepresentSTT-Arena,abenchmarkof227tasksdesignedtoevaluatetheadaptivereplanningcapa-
bilitiesofLLMsunderspatio-temporaldynamics. Ourevaluationofmassivemodelsdemonstrates
thatspatio-temporaldynamicsposeafundamentalanduniversalchallenge,witheventhestrongest
frontiermodelachievingonly35.39%.Throughtrajectoryanalysis,weidentifythreerecurringfailure
modesthatconsistentlyseparaterobustmodelsfromfailingones,andproposeaniterativetrajectory
refinement approach that targets each failure mode sequentially during training. Combined with
verifiableonlinereinforcementlearning,STT-Agent-4Bachievescompetitiveperformanceagainst
manyopen-sourcefrontiermodels,demonstratingthattargetedtrainingonspatio-temporalfailure
patternsisbotheffectiveandsample-efficient.WehopeSTT-Arenaservesasafoundationforbuilding
LLMsthataregenuinelyrobustunderthedynamicconditionsofreal-worlddeployment.
References
QwenTeam. Qwen3technicalreport. CoRR,abs/2505.09388,2025. doi: 10.48550/ARXIV.2505.
09388. URLhttps://doi.org/10.48550/arXiv.2505.09388.
KimiTeam. KimiK2.5: visualagenticintelligence. CoRR,abs/2602.02276,2026. doi: 10.48550/
ARXIV.2602.02276. URLhttps://doi.org/10.48550/arXiv.2602.02276.
GLM. GLM-5: from vibe coding to agentic engineering. CoRR, abs/2602.15763, 2026. doi:
10.48550/ARXIV.2602.15763. URLhttps://doi.org/10.48550/arXiv.2602.15763.
Ling Team and Inclusion AI. Every step evolves: Scaling reinforcement learning for trillion-
scalethinkingmodel. CoRR,abs/2510.18855,2025. doi: 10.48550/ARXIV.2510.18855. URL
https://doi.org/10.48550/arXiv.2510.18855.
Xiaoshuai Song, Haofei Chang, Guanting Dong, Yutao Zhu, Zhicheng Dou, and Ji-Rong Wen.
Envscaler: Scaling tool-interactive environments for LLM agent via programmatic synthesis.
CoRR,abs/2601.05808,2026. doi: 10.48550/ARXIV.2601.05808. URLhttps://doi.org/10.
48550/arXiv.2601.05808.
Zexu Sun, Bokai Ji, Hengyi Cai, Shuaiqiang Wang, Lei Wang, Guangxia Li, and Xu Chen.
Agentskiller: Scalinggeneralistagentintelligencethroughsemanticallyintegratedcross-domain
data synthesis. CoRR, abs/2602.09372, 2026. doi: 10.48550/ARXIV.2602.09372. URL
https://doi.org/10.48550/arXiv.2602.09372.
Minghao Li, Yingxiu Zhao, Bowen Yu, Feifan Song, Hangyu Li, Haiyang Yu, Zhoujun Li, Fei
Huang,andYongbinLi. Api-bank: Acomprehensivebenchmarkfortool-augmentedllms. In
Houda Bouamor, Juan Pino, and Kalika Bali, editors, Proceedings of the 2023 Conference on
EmpiricalMethodsinNaturalLanguageProcessing,EMNLP2023,Singapore,December6-10,
2023,pages3102–3116.AssociationforComputationalLinguistics,2023. doi: 10.18653/V1/2023.
EMNLP-MAIN.187. URLhttps://doi.org/10.18653/v1/2023.emnlp-main.187.
Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong,
Xiangru Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou,
MarkGerstein,DahaiLi,ZhiyuanLiu,andMaosongSun. Toolllm: Facilitatinglargelanguage
modelstomaster16000+real-worldapis. InTheTwelfthInternationalConferenceonLearning
Representations, ICLR 2024, Vienna, Austria, May 7-11, 2024. OpenReview.net, 2024. URL
https://openreview.net/forum?id=dHng2O0Jjr.
ShunyuYao, NoahShinn, PedramRazavi, andKarthikNarasimhan. τ-bench: Abenchmarkfor
tool-agent-userinteractioninreal-worlddomains. CoRR,abs/2406.12045,2024. doi: 10.48550/
ARXIV.2406.12045. URLhttps://doi.org/10.48550/arXiv.2406.12045.
Wei He, Yueqing Sun, Hongyan Hao, Xueyuan Hao, Zhikang Xia, Qi Gu, Chengcheng Han,
DengchangZhao,HuiSu,KefengZhang,ManGao,XiSu,XiaodongCai,XunliangCai,YuYang,
andYunkeZhao. Vitabench: BenchmarkingLLMagentswithversatileinteractivetasksinreal-
world applications. CoRR, abs/2509.26490, 2025. doi: 10.48550/ARXIV.2509.26490. URL
https://doi.org/10.48550/arXiv.2509.26490.
10

<!-- page 11 -->

Romain Froger, Pierre Andrews, Matteo Bettini, Amar Budhiraja, Ricardo Silveira Cabral, Vir-
ginie Do, Emilien Garreau, Jean-Baptiste Gaya, Hugo Laurençon, Maxime Lecanu, Kunal
Malkan, Dheeraj Mekala, Pierre Ménard, Gerard Moreno-Torres Bertran, Ulyana Piterbarg,
Mikhail Plekhanov, Mathieu Rita, Andrey Rusakov, Vladislav Vorotilov, Mengjue Wang, Ian
Yu, AmineBenhalloum, GrégoireMialon, andThomasScialom. Gaia2: BenchmarkingLLM
agents on dynamic and asynchronous environments. CoRR, abs/2602.11964, 2026. doi:
10.48550/ARXIV.2602.11964. URLhttps://doi.org/10.48550/arXiv.2602.11964.
Yule Wen, Yixin Ye, Yanzhe Zhang, Diyi Yang, and Hao Zhu. Real-time reasoning agents in
evolvingenvironments. CoRR,abs/2511.04898,2025. doi: 10.48550/ARXIV.2511.04898. URL
https://doi.org/10.48550/arXiv.2511.04898.
YichuanMa,LinyangLi,YongkangChen,PeijiLi,XiaozheLi,QipengGuo,DahuaLin,andKai
Chen.Timelymachine:Awarenessoftimemakestest-timescalingagentic.CoRR,abs/2601.16486,
2026. doi: 10.48550/ARXIV.2601.16486. URLhttps://doi.org/10.48550/arXiv.2601.
16486.
WeiwenLiu,XuHuang,XingshanZeng,XinlongHao,ShuaiYu,DexunLi,ShuaiWang,Weinan
Gan, Zhengying Liu, Yuanqing Yu, Zezhong Wang, Yuxian Wang, Wu Ning, Yutai Hou, Bin
Wang, Chuhan Wu, Xinzhi Wang, Yong Liu, Yasheng Wang, Duyu Tang, Dandan Tu, Lifeng
Shang, Xin Jiang, Ruiming Tang, Defu Lian, Qun Liu, and Enhong Chen. Toolace: Winning
the points of LLM function calling. In The Thirteenth International Conference on Learning
Representations,ICLR2025,Singapore,April24-28,2025.OpenReview.net,2025. URLhttps:
//openreview.net/forum?id=8EB8k6DdCU.
TeamOlmo,AllysonEttinger,AmandaBertsch,BaileyKuehl,DavidGraham,DavidHeineman,Dirk
Groeneveld,FaezeBrahman,FinbarrTimbers,HamishIvison,JacobMorrison,JakePoznanski,
KyleLo,LucaSoldaini,MattJordan,MayeeChen,MichaelNoukhovitch,NathanLambert,Pete
Walsh,PradeepDasigi,RobertBerry,SaumyaMalik,SaurabhShah,ScottGeng,ShaneArora,
ShashankGupta,TairaAnderson,TengXiao,TylerMurray,TylerRomero,VictoriaGraf,Akari
Asai,AkshitaBhagia,AlexanderWettig,AlisaLiu,AmanRangapur,ChloeAnastasiades,Costa
Huang, Dustin Schwenk, Harsh Trivedi, Ian Magnusson, Jaron Lochner, Jiacheng Liu, Lester
James V. Miranda, Maarten Sap, Malia Morgan, Michael Schmitz, Michal Guerquin, Michael
Wilson, ReganHuff, RonanLeBras, RuiXin, RulinShao, SamSkjonsberg, ShannonZejiang
Shen,ShuyueStellaLi,TuckerWilde,ValentinaPyatkin,WillMerrill,YapeiChang,YulingGu,
ZhiyuanZeng,AshishSabharwal,LukeZettlemoyer,PangWeiKoh,AliFarhadi,NoahA.Smith,
andHannanehHajishirzi. Olmo3,2025. URLhttps://arxiv.org/abs/2512.13961.
ZhichengGuo,SijieCheng,HaoWang,ShihaoLiang,YujiaQin,PengLi,ZhiyuanLiu,Maosong
Sun, and Yang Liu. Stabletoolbench: Towards stable large-scale benchmarking on tool learn-
ing of large language models. In Lun-Wei Ku, Andre Martins, and Vivek Srikumar, edi-
tors, Findings of the Association for Computational Linguistics, ACL 2024, Bangkok, Thai-
landandvirtualmeeting,August11-16,2024,FindingsofACL,pages11143–11156.Associa-
tionforComputationalLinguistics,2024. doi: 10.18653/V1/2024.FINDINGS-ACL.664. URL
https://doi.org/10.18653/v1/2024.findings-acl.664.
NicholasFarnandRichardShin. Tooltalk: Evaluatingtool-usageinaconversationalsetting. CoRR,
abs/2311.10775,2023. doi: 10.48550/ARXIV.2311.10775. URLhttps://doi.org/10.48550/
arXiv.2311.10775.
ZhentingWang, QiChang, HemaniPatel, ShashankBiju, Cheng-EnWu, QuanLiu, AolinDing,
AlirezaRezazadeh,AnkitShah,YujiaBao,andEugeneSiow. Mcp-bench: Benchmarkingtool-
usingLLMagentswithcomplexreal-worldtasksviaMCPservers. CoRR,abs/2508.20453,2025a.
doi: 10.48550/ARXIV.2508.20453. URLhttps://doi.org/10.48550/arXiv.2508.20453.
Shiqing Fan, Xichen Ding, Liang Zhang, and Linjian Mo. Mcptoolbench++: A large scale AI
agent model context protocol MCP tool use benchmark. CoRR, abs/2508.07575, 2025. doi:
10.48550/ARXIV.2508.07575. URLhttps://doi.org/10.48550/arXiv.2508.07575.
ShishirG.Patil, HuanzhiMao, FanjiaYan, CharlieCheng-JieJi, VishnuSuresh, IonStoica, and
JosephE.Gonzalez. Theberkeleyfunctioncallingleaderboard(BFCL):fromtoolusetoagentic
11

<!-- page 12 -->

evaluationoflargelanguagemodels. InAartiSingh,MaryamFazel,DanielHsu,SimonLacoste-
Julien,FelixBerkenkamp,TeganMaharaj,KiriWagstaff,andJerryZhu,editors,Forty-second
InternationalConferenceonMachineLearning,ICML2025,Vancouver,BC,Canada,July13-
19, 2025, Proceedings of Machine Learning Research. PMLR / OpenReview.net, 2025. URL
https://proceedings.mlr.press/v267/patil25a.html.
2
VictorBarres,HonghuaDong,SohamRay,XujieSi,andKarthikNarasimhan. τ -bench: Evaluating
conversationalagentsinadual-controlenvironment. CoRR,abs/2506.07982,2025. doi: 10.48550/
ARXIV.2506.07982. URLhttps://doi.org/10.48550/arXiv.2506.07982.
ChenChen,XinlongHao,WeiwenLiu,XuHuang,XingshanZeng,ShuaiYu,DexunLi,Yuefeng
Huang,XiangchengLiu,XinzhiWang,andWuLiu. Acebench: Acomprehensiveevaluationof
LLMtoolusage. InChristosChristodoulopoulos,TanmoyChakraborty,CarolynRose,andViolet
Peng,editors,FindingsoftheAssociationforComputationalLinguistics: EMNLP2025,Suzhou,
China,November4-9,2025,pages12970–12998.AssociationforComputationalLinguistics,2025.
URLhttps://aclanthology.org/2025.findings-emnlp.697/.
JiaruiLu,ThomasHolleis,YizheZhang,BernhardAumayer,FengNan,HaopingBai,ShuangMa,
ShenMa,MengyuLi,GuoliYin,ZiruiWang,andRuomingPang. Toolsandbox:Astateful,conver-
sational,interactiveevaluationbenchmarkforLLMtoolusecapabilities. InLuisChiruzzo,Alan
Ritter,andLuWang,editors,FindingsoftheAssociationforComputationalLinguistics: NAACL
2025,Albuquerque,NewMexico,USA,April29-May4,2025,FindingsofACL,pages1160–1183.
AssociationforComputationalLinguistics,2025. doi: 10.18653/V1/2025.FINDINGS-NAACL.65.
URLhttps://doi.org/10.18653/v1/2025.findings-naacl.65.
JunlongLi,WenshuoZhao,JianZhao,WeihaoZeng,HaozeWu,XiaochenWang,RuiGe,Yuxuan
Cao, Yuzhen Huang, Wei Liu, Junteng Liu, Zhaochen Su, Yiyang Guo, Fan Zhou, Lueyang
Zhang,JuanMichelini,XingyaoWang,XiangYue,ShuyanZhou,GrahamNeubig,andJunxian
He. Thetooldecathlon: Benchmarkinglanguageagentsfordiverse,realistic,andlong-horizon
taskexecution. CoRR,abs/2510.25726,2025. doi: 10.48550/ARXIV.2510.25726. URLhttps:
//doi.org/10.48550/arXiv.2510.25726.
ZifengDing, SikuanYan, MoyYuan, XianglongHu, FangruLin, andAndreasVlachos. TCP:a
benchmark for temporal constraint-based planning. In Christos Christodoulopoulos, Tanmoy
Chakraborty, Carolyn Rose, and Violet Peng, editors, Proceedings of the 2025 Conference on
EmpiricalMethodsinNaturalLanguageProcessing,EMNLP2025,Suzhou,China,November
4-9,2025,pages22452–22475.AssociationforComputationalLinguistics,2025. doi: 10.18653/
V1/2025.EMNLP-MAIN.1142. URL https://doi.org/10.18653/v1/2025.emnlp-main.
1142.
Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo, Zhangchi Feng, and
YongqiangMa. Llamafactory: Unifiedefficientfine-tuningof100+languagemodels. InPro-
ceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume3:
SystemDemonstrations),Bangkok,Thailand,2024.AssociationforComputationalLinguistics.
URLhttp://arxiv.org/abs/2403.13372.
JianHu,JasonKleinLiu,HaotianXu,andWeiShen. Reinforce++: Stabilizingcritic-freepolicy
optimizationwithglobaladvantagenormalization,2025. URLhttps://arxiv.org/abs/2501.
03262.
WeixunWang,ShaopanXiong,GengruChen,WeiGao,ShengGuo,YanchengHe,JuHuang,Jiaheng
Liu,ZhendongLi,XiaoyangLi,etal. Reinforcementlearningoptimizationforlarge-scalelearning:
Anefficientanduser-friendlyscalinglibrary. arXivpreprintarXiv:2506.06122,2025b.
A RelatedWork
No-EnvironmentBenchmarks. RecenteffortsevaluatedagenticLLMswithoutaclosedandself-
containedenvironment,focusingpurelyonsingle-turnormulti-turnAPIcallingaccuracy. API-Bank
[Lietal.,2023]andToolBench[Qinetal.,2024]introducedplan-retrieve-callpipelinesbuttreated
toolsasisolatedfunctionswithoutstateordependencies. StableToolBench[Guoetal.,2024]added
12

<!-- page 13 -->

avirtualAPIservertoimprovestability. ToolTalk[FarnandShin,2023]enabledmulti-steptool
executionthroughconversationalinterfaces,butreliedonpredefinedtrajectoriesthatrestrictagent
autonomy. WiththeemergenceoftheModelContextProtocol(MCP),protocol-alignedbenchmarks
havebecomepopular. MCP-Bench[Wangetal.,2025a]andMCPToolBench++[Fanetal.,2025]
scaletolargenumbersofserversandtoolswithfine-grainederrortaxonomies. Allthesebenchmarks
lackaclosed,self-consistentenvironmentforLLMstointeractwith.
StaticEnvironmentBenchmarks. Asecondgroupofbenchmarksfeaturesaclosed,staticenviron-
mentwheretheworldstateevolvesonlywhentheagentcallsandexecutestools,withnotimeor
location-drivenchanges. BFCL[Patiletal.,2025]extendedevaluationtomulti-turndialoguesbut
assembledconversationsfromfixedtemplates.τ-Bench[Yaoetal.,2024]andτ2-Bench[Barresetal.,
2025]requireLLMstofollowdomain-specificruleswhileengagingwithsimulatedusers,yetfocus
onnarrowscenarios. VitaBench[Heetal.,2025]andACEBench[Chenetal.,2025]providediverse
taskscenariosbuttheirdynamicsremainlimitedtoagent-driventransitions. ToolSandBox[Luetal.,
2025]pioneeredstatefulexecutionandtoolinterdependencies,whileToolAthlon[Lietal.,2025]
offersarichenvironmentfortooluseevaluation. Allthesebenchmarksassumethattheenvironment
isstatic: notime-dependentchanges,nospatialshifts,andnoexternaltriggersthatalterthestate
withoutLLMsintervention.
DynamicEnvironmentBenchmarks. Afewrecentbenchmarkshavebeguntoaddressenviron-
mentaldynamics. TCP[Dingetal.,2025]andTimely-Eval[Maetal.,2026]focusonwall-clock
timeplanningandreasoning,requiringLLMstoactundertemporalconstraints. GAIA-2[Froger
etal.,2026]introducestemporallyevolvingtaskswhereinformationbecomesavailableorobsolete
overtime. Real-TimeReasoningGym(RTRGym)[Wenetal.,2025]evaluateshowsensitiveLLMs
aretothepassageofreal-worldtime. However,thesebenchmarksemphasizegradualorpredictable
temporalchanges(e.g.,deadlines,streamingdata)ratherthanabruptstateshiftsthatcanoccurat
anystepduetoexternaltriggers. Moreover,theydonotrequireLLMstodetect,replan,andadaptin
responsetounexpecteddisruptionsthatinvolvebothtimeandlocation.
Incontrasttoalloftheabove,STT-ArenasystematicallyevaluatesLLMsinspatiotemporallydynamic
environments.Theenvironmentstatecanchangeabruptlyatanystepduetotriggersactivatedbytime,
location,ortheircombination. Thesechangesdisrupttheoriginalplanofmodels,forcingittodetect
theshift,replan,andadapt. Table1revealthedetailcomparisonsamongdifferentbenchmarks.
B LimitationsandPotentialSocietyImpacts
Limitations. Although STT-Arena provides a rigorous and diverse benchmark for evaluating
adaptivereplanningunderspatio-temporaldynamics,severallimitationsremain. First,thebenchmark
comprises227instances,which,whilecarefullycuratedthroughathree-stagepipelinewithhuman-
in-the-loopvalidation,maynotexhaustivelycoverthefullspectrumofreal-worldspatio-temporal
conflict patterns. The nine conflict subtypes defined in our taxonomy represent a principled but
potentially incomplete characterization of environmental dynamics encountered in deployment.
Second,theconstructionpipelinereliesheavilyonQwen-3.5-397B-A17Bforenvironmentsynthesis,
blueprintgeneration,andtrajectoryrefinement,whichmayintroducesystematicbiasestowardconflict
patternsorlinguisticstylesthataremoreeasilygeneratedbythisparticularmodelfamily. Third,
theevaluationprotocolusesafixedpassiveusersimulator,which,althoughablatedacrossmultiple
backbone models, cannot fully replicate the diversity of real human communication behaviors.
Finally,whileSTT-Agent-4Bdemonstratesthattargetedtrainingonspatio-temporalfailurepatternsis
effective,theiterativetrajectoryrefinementprocedureintroducesadditionalcomputationaloverhead,
and its scalability to larger model families or more complex multi-agent settings has not been
thoroughlyinvestigated.
PotentialSocietyImpacts. STT-ArenaisintendedtoadvancethedevelopmentofLLM-based
agentsthataregenuinelyrobustunderthedynamicconditionsofreal-worlddeployment,withbroad
positiveimplicationsforsafety-criticalapplicationssuchasclinicalconsultationservices,logistics
coordination, and airline reservation systems. By exposing fundamental gaps in current models’
abilitytodetectenvironmentalshifts,replan,andverifytaskcompletion,thisworkencouragesthe
community to prioritize reliability and graceful degradation over static benchmark performance,
therebyreducingtheriskofdeployingbrittleagentsinhigh-stakesscenarios. Onthenegativeside,
improvementsinadaptivereplanningcapabilitiesdrivenbybenchmarkslikeSTT-Arenacouldalso
13

<!-- page 14 -->

lowerthebarrierfordeployingautonomousagentsinsensitivedomainsbeforesufficientalignment
andsafetyguaranteesareinplace.Furthermore,theautomateddatasynthesispipeline,whiledesigned
forbenchmarkconstruction,couldinprincipleberepurposedtogenerateadversarialenvironments
thatdeliberatelymisleadordestabilizedeployedagents. Weencouragefutureworktopairadvances
indynamicreasoningwithcorrespondingprogressinrobustnesscertificationandhumanoversight
mechanisms.
Table3: FullPass@1results(mean±standarddeviationoverthreeruns)forallevaluatedmodelson
STT-Arena,brokendownbysolvableandimpossibletasks. Performancedegradesconsistentlyas
difficultyincreases(EasytoHard),withallmodelsstrugglingmostattheHardlevel. STT-Agent-4B
achievesxx%overalldespitehavingonly4Bparameters,surpassingmanyfrontiermodels.
Models Easy Medium Hard Impossible Overall
Closed-SourceLLMs
Qwen-3.6-Plus 35.21(±2.82) 24.38(±1.72) 23.16(±2.59) 54.44(±1.93) 31.42(±2.08)
Claude-4.6-Sonnet 35.21(±1.41) 29.85(±1.49) 19.77(±2.59) 58.89(±1.92) 32.74(±0.91)
Gemini-3.1-Pro 37.56(±2.15) 30.35(±2.28) 21.47(±3.53) 52.22(±1.92) 33.19(±0.67)
GPT-5.4 39.91(±0.81) 29.85(±3.95) 24.29(±0.98) 52.22(±1.92) 34.51(±1.02)
Claude-4.6-Opus 41.78(±2.15) 31.34(±2.59) 23.73(±1.70) 52.22(±3.85) 35.39(±0.26)
Open-sourceLLMs
Llama-3.3-70B 22.07(±0.81) 11.44(±2.28) 11.30(±1.96) 30.00(±3.33) 17.18(±1.52)
Kimi-K2.5 25.35(±2.82) 13.43(±1.50) 14.12(±4.26) 37.78(±6.94) 19.18(±0.99)
MiniMax-M2.7 26.29(±2.94) 15.92(±0.86) 13.56(±1.70) 36.67(±3.34) 21.29(±0.92)
MiniMax-M2.5 26.76(±2.44) 15.92(±1.72) 12.43(±3.53) 42.22(±6.94) 21.88(±0.51)
GLM-5 30.05(±4.30) 21.39(±1.73) 10.73(±1.96) 43.33(±3.34) 24.23(±1.59)
Deepseek-V4-Pro 32.86(±1.62) 20.40(±2.28) 15.25(±1.70) 45.56(±8.39) 26.29(±0.92)
GLM-5.1 35.21(±1.41) 23.38(±1.72) 15.25(±1.70) 41.11(±5.09) 27.31(±1.59)
Qwen-3.5-397B-A17B 33.80(±1.41) 21.89(±3.11) 17.51(±5.18) 54.45(±3.85) 28.78(±0.51)
Deepseek-V3.2 36.62(±3.73) 27.86(±2.28) 15.82(±0.98) 63.33(±5.77) 32.16(±2.45)
MoreEfficientLLMs
Llama-3.1-8B 7.98(±1.63) 3.98(±0.86) 2.82(±0.98) 5.56(±1.93) 5.14(±0.25)
Qwen-3.5-35B-A3B 19.72(±1.41) 13.43(±0.00) 7.34(±0.98) 17.78(±1.92) 12.48(±0.26)
GPT-5.4-mini 19.72(±1.41) 13.43(±0.00) 7.34(±0.98) 6.67(±0.00) 12.92(±0.51)
Qwen-3-8B 16.90(±1.41) 13.43(±1.50) 11.30(±0.98) 20.00(±3.33) 14.83(±1.27)
Qwen-3.5-9B 27.23(±0.81) 12.93(±0.86) 11.30(±0.98) 32.22(±1.92) 19.53(±0.92)
Gemini-2.5-flash 28.17(±1.41) 13.43(±1.50) 12.43(±0.98) 31.11(±1.92) 20.11(±0.26)
STT-Agent
Qwen-3-4B(baseline) 18.31(±3.73) 9.46(±0.86) 2.82(±0.98) 10.00(±3.33) 10.57(±1.59)
STT-Agent-4B(SFT) 26.76(±1.41) 17.41(±0.86) 13.56(±1.70) 61.11(±1.92) 25.11(±0.76)
STT-Agent-4B(SFT+RL) 29.11(±1.63) 19.90(±2.28) 14.12(±0.98) 64.44(±1.93) 27.17(±1.11)
C DetailedInformation
C.1 DetailedinformationofMainResults
AsshowninTable3,wereportthedetailedresultsofFigure3.
C.2 DetailedInformationofSTT-Arena
ConstructionDetails. DuringtheconstructionofSTT-Arena,weutilizeQwen-3.5-397Btosynthe-
sizeallbenchmarkdata. Aftertheautomatedpipeline,threeannotatorsconductafinalverificationof
theproducedbenchmarkinstances,coveringthefollowingaspects: (1)consistencybetweentheuser
queryandthechecklist,(2)correctnessofthechecklist,and(3)plausibilityofthespatio-temporal
dynamics. Aftermanualvalidation,weobtain227finalinstances,spanningtwocategories(solvable
andimpossible)andninespatio-temporalsubtypes.
14

<!-- page 15 -->

StatisticofSTT-Arena. AsshowninFigures9and10,wereportthedistributionofdatasamples
acrossthesolvableandimpossibletasksandtheninespatio-temporalsubtypes. Detailedinformation
andexamplesforeachdifficultylevelandeachsubtypeareprovidedinTables5and4,respectively.
Evaluation Details of STT-Arena. We utilize Pass@1 rate for evaluating STT-Arena and we
calculatetheoverallperformancethroughaweightedaverageofthefourlevels. Formally,Overall=
αP +βP +γP +δP,whereα,β,γ,andδareequalto71/227,67/227,59/227,and30/227,
e m h i
respectively.
Benchmark Difficulty Levels
Impossible
40
13.2%
Easy (30) 35 31.3%
(71) 30
25
26.0%
(59) Hard 20
15
10
29.5%
(67)
5
Medium 0
T1 T2 T3 S1 S2 S3 ST1 ST2 ST3
selpmas
fo
rebmuN
Spatio-temporal Sub-types
38
31 32
24 25
20 20 20
17
Figure9: DistributionofSTT-Arenainstancesacrossdifficultylevelsandspatio-temporalsubtypes.
(Left)Thebenchmarkcomprises71Easy(31.3%),67Medium(29.5%),59Hard(26.0%),and30
Impossible(13.2%)instances. (Right)Instancecountsperspatio-temporalsubtype,withS1being
themostfrequent(38instances)andS3theleast(17instances).
12
10
8
6
4
2
0
T1 T2 T3 S1 S2 S3 ST1 ST2 ST3
selpmas
fo
rebmuN
Solvable and Impossible Distribution across Spatio-temporal Subtypes
Easy Hard 11 11
Medium Impossible
10 10 10
9 9 9 9 9
8 8 8 8
7 7 7 7 7
6 6 6 6 6
5 5 5 5
4 4
2 2
1
Figure10: Solvableandimpossibleinstancedistributionacrosstheninespatio-temporalsubtypes.
C.3 DetailedInformationofTrainingData
WegenerateSFTtrajectoriesandRLtasksthroughourthree-stagepipeline(sameastheconstruction
ofSTT-Arena,wealsouseQwen-3.5-397B-A17Btogeneratetrainingdata). Specifically,asshown
inFigures11and12,weconstruct2,212validatedtrajectoriesforSFTand8,119instancesforonline
RL,thoughwenotethatnotallRLinstancesareusedinRLtraining.
C.4 ImplementationDetailsofSFTandRL
SFT.WeuseQwen-3-4B-BaseasthebackbonemodelandtrainwiththeLlamaFactory[Zhengetal.,
2024]frameworkfor2epochs. Weadoptacosinelearningrateschedulerwithalearningrateof
15

<!-- page 16 -->

Table4: Taxonomyoftheninespatio-temporalconflicttypesinSTT-Arena,organizedintothree
categories: Temporal(T1–T3),Spatial(S1–S3),andSpatio-Temporal(ST1–ST3). Eachconflicttype
isdefinedbyadistinctdisruptionmechanismandillustratedwithaconcretereal-worldexample,
collectivelycoveringtheprincipalwaysinwhichreal-worldconditionscaninvalidateanongoing
agentplan.
Category ID ConflictType Examples
T1 WindowExpiry Hotelbookingtimeoutduringmulti-stepplanning.
Temporal T2 PriorityReorder Flightrescheduledearlier,invalidatingtransfers.
T3 QuotaReset Promotionalticketsexpireatmidnightmid-session.
S1 SiteMismatch Reservedvehiclerelocatedtoadifferentdepot.
Spatial S2 DependencyBlock Warehouselockdownhaltsalldownstreamdispatch.
S3 RouteRestriction Newcustomsrulesblockacross-bordercorridor.
ST1 ResourceShift Peakdemandmovescarsawayfromresidentialzones.
Spatio-temp. ST2 FailureCascade Huboutagedisruptsregionalwarehouseinventory.
ST3 HandoffFailure Medicalsamplemisseswindowduetoclockdrift.
Table5: DescriptionofthesolvableandimpossibletasksinSTT-Arena. LevelsrangefromEasy
(singleisolatedconflict,onecorrectiveaction)toHard(long-horizoncascadingconstraintsrequiring
global replanning) and Impossible (no valid completion path exists; the correct response is to
recognizeandcommunicateinfeasibility).
Level Description
Easy Tasksinvolveisolated,immediatelyobservableconflictswithnocascading
effects. Recoveryrequiresatmostonecorrectiveaction,withlimitedstate
dependencyacrosstoolcalls.
Medium Multi-steptaskswithmildstatedependency. Conflictsmaybedeferredand
requireawarenessofpriorcontext;recoveryinvolvesreplanningover2–3
steps.
Hard Long-horizontaskswithinterleavedspatiotemporalconstraints. Conflicts
may cascade, requiring the agent to detect implicit failures and replan
globallyacrossthefullexecutiontrajectory.
Impossible Tasksforwhichnovalidcompletionpathexistsgiventheinjectedconflict.
Thecorrectbehavioristoidentifyinfeasibilityandcommunicateittothe
user,ratherthanattemptingresolution.
Solvable and Impossible Tasks
Impossible
300
Easy 17.4%
(385) 29.5% 250
(652)
200
25.2% 150
(557) Hard
100
27.9%
(617) 50
Medium
0
T1 T2 T3 S1 S2 S3 ST1 ST2 ST3
selpmas
fo
rebmuN
Spatio-temporal Sub-types
302
267
252 255 243 236
221 226
210
Figure11: DistributionofSFTtrajectoriesacrossdifficultylevelsandspatio-temporalsubtypes.
16

<!-- page 17 -->

Solvable and Impossible Tasks
Impossible 1000 Easy 19.3%
27.6% (1569)
(2239) 800
600
27.3% 400
(2220)
25.7% Hard
(2090)
200
Medium
0
T1 T2 T3 S1 S2 S3 ST1 ST2 ST3
selpmas
fo
rebmuN
Spatio-temporal Sub-types
1015 976 991 926 940 891 879
747 754
Figure12: DistributionofRLtasksacrossdifficultylevelsandspatio-temporalsubtypes.
1.0×10−5andawarmupratioof0.03. Themaximumsequencelengthissetto32Ktokens,andthe
effectiveglobalbatchsizeis128.
RL.Wefurtherfine-tunetheSFTcheckpointusingtheREINFORCE++[Huetal.,2025]algorithm
withintheROLL[Wangetal.,2025b]framework. WeretainaKLconstraintwithacoefficientof
0.1andusealearningrateof1.0×10−6. Ineachtrainingstep,wesample32tasksandrollout4
trajectoriespertask,foratotalofupto100trainingsteps. Themaximumtrajectorylengthissetto
32Ktokens,andthemaximumgenerationlengthperstepiscappedat4Ktokens.
ComputationalResources. AllthetrainingexperimentsincludingSFTandonlineRLareconducted
on4NVIDIAH200GPUs.
D CaseExamples
D.1 CasesofSTT-ArenaConstructionPipeline
Inthissection,weprovidesomeexamplesduringSTT-Arenaconstructionpipelineincludingstatic
environment,blueprint,userprofile,checklist,checkfunctions,anddynamicenvironmentasshown
inFigures13,14,15,16,17,and18.
ExampleofStaticEnvironment
class ColdChainLogisticsEnv:
def __init__(self, init_config: dict):
self.distribution_hubs = init_config.get("distribution_hubs", {})
self.depots = init_config.get("depots", {})
self.vehicles = init_config.get("vehicles", {})
self.cooling_units = init_config.get("cooling_units", {})
self.cooling_unit_resets = init_config.get("cooling_unit_resets", {})
self.shipments = init_config.get("shipments", {})
self.goods_inventory = init_config.get("goods_inventory", {})
self.route_stops = init_config.get("route_stops", {})
self.clinics = init_config.get("clinics", {})
# --------- INFORMATION QUERY OPERATIONS ---------
def get_vehicle_status(self, vehicle_id: str): ...
def list_depot_maintenance_schedule(self, depot_id: str,
time_range: dict): ...
def get_shipment_journey_status(self, shipment_id: str): ...
def get_route_stop_details(self, vehicle_id: str): ...
def get_goods_inventory_at_site(self, site_id: str): ...
def list_clinic_immunization_schedule(self, site_id: str): ...
17

<!-- page 18 -->

def list_operational_hours(self, site_id: str): ...
def get_cooling_unit_status(self, cooling_unit_id: str): ...
# ---------ADMINISTRATIVE / STATE-CHANGE OPERATIONS ---------
def assign_shipment_to_vehicle(self, shipment_id: str,
vehicle_id: str): ...
def record_cooling_unit_reset(self, reset_window_id: str, action: str,
timestamp: str): ...
def update_vehicle_status(self, vehicle_id: str, status: str,
current_site_id: str): ...
def schedule_cooling_unit_reset(self, cooling_unit_id: str, depot_id: str,
requested_window: dict): ...
def add_or_update_route_plan(self, vehicle_id: str, route_plan: list): ...
def update_route_stop_actual_times(self, route_stop_id: str,
actual_arrival: str,
actual_departure: str): ...
def register_goods_receipt(self, shipment_id: str, site_id: str,
timestamp: str): ...
def update_goods_inventory_status(self, goods_id: str, status: str,
current_location_id: str): ...
def create_new_shipment(self, goods_id: str, origin_hub_id: str,
destination_hub_id: str, departure_time: str): ...
Figure13: Exampleofstaticenvironment,weimplementtheenvironmentthroughPythonclass.
ExampleofBlueprint
[
{
"scenario_id": "ColdChainLogisticsEnv__T2__medium",
"env_id": "ColdChainLogisticsEnv",
"conflict_type": "T2",
"difficulty": "medium",
"user_goal": "Ship a batch of insulin (goods_id=’INS-2024-001’)
from distribution hub ’HUB-NORTH’ to clinic ’CLINIC-DOWNTOWN’
with a required arrival time before 2024-08-15T08:00:00.
The insulin must never exceed 8°C.",
"normal_flow": [
{
"operation": "create_new_shipment",
"purpose": "Create a new shipment record for the insulin batch."
},
{
"operation": "list_operational_hours",
"purpose": "Check clinic’s receiving hours to schedule delivery."
},
{
"operation": "assign_shipment_to_vehicle",
"purpose": "Assign the shipment to a refrigerated vehicle."
},
{
"operation": "add_or_update_route_plan",
"purpose": "Define route stops
including the clinic as final destination."
},
{
"operation": "update_vehicle_status",
"purpose": "Mark vehicle as ’in_transit’ when dispatched."
},
{
"operation": "register_goods_receipt",
18

<!-- page 19 -->

"purpose": "Confirm arrival and receipt at the clinic."
}
],
"conflict_design": {
"activation_operation": "list_operational_hours",
"trigger_mechanism": "conditional_guarded",
"trigger_condition": "The vehicle has already been dispatched
(status=’in_transit’) but the clinic’s operating hours
for the planned delivery day are overridden
by an emergency closure order that was issued after dispatch.",
"recovery_guard_condition": "The agent successfully cancels
the current delivery assignment and reassigns
the shipment to a different vehicle with a new route
that arrives before the insulin expiry deadline.",
"mutations": [
{
"state_path": "clinics[’CLINIC-DOWNTOWN’].operational_hours",
"change_description": "original: {’Monday-Friday’: ’08:00-17:00’}
→ new: {’Monday-Friday’: ’08:00-12:00’}"
},
{
"state_path": "shipments[’SHIP-INS-001’].delivery_window.end",
"change_description": "original: ’2024-08-15T17:00:00’
→ new: ’2024-08-15T10:00:00’ (because the clinic now closes at noon)"
}
],
"observable_via": "list_operational_hours"
},
"recovery_path": "1. ‘update_vehicle_status‘ —
Change vehicle status back to ’idle’ and clear current assignment.
2. ‘update_goods_inventory_status‘ —
Mark the insulin shipment as ’pending_reassignment’.
3. ‘list_operational_hours‘ —
Verify new clinic hours and identify alternative delivery window.
4. ‘create_new_shipment‘ —
Create a new shipment with accelerated delivery window.
5. ‘assign_shipment_to_vehicle‘ —
Assign to a different vehicle (with faster cooling unit).
6. ‘add_or_update_route_plan‘ —
Plan direct route without intermediate stops.
7. ‘update_vehicle_status‘ —
Dispatch new vehicle.
8. ‘register_goods_receipt‘ —
Complete delivery before 10:00.",
"_raw": "## User Goal\nShip a batch of insulin ...
## Normal Flow\n1. ‘create_new_shipment‘ ...\n..."
}
]
Figure14: Exampleofblueprint,wedesigntheblueprintbasedontheconflicttypes,difficultylevels,
andenvironmentinformation.
ExampleofUserProfile
[
{
"scenario_id": "ColdChainLogisticsEnv__T2__medium",
"user_profile": {
"task_goal": "Ensure the insulin batch arrives at
CLINIC-DOWNTOWN before 10:00.",
"persona": "I am a logistics coordinator at the central hub,
responsible for temperature-sensitive deliveries.",
19

<!-- page 20 -->

"context": "This shipment is critical for pediatric patients.
The clinic’s hours changed due to an emergency.",
"tone": "Professional but slightly anxious about the deadline;
responds concisely with relevant data.",
"fallback_response": "I’m not sure what you mean.
Please check the shipment ID and try again.",
"decline_cancel_response": "We cannot cancel this shipment
without a formal override.
Please find a way.",
"frustration_threshold": "medium",
"flexibility": "high",
"known_facts": [
"The shipment ID is SHIP-INS-001.",
"Clinic normally closes at 17:00 but today closes at 10:00.",
"Vehicle V002 has a faster cooling unit than V001."
],
"withhold_until_asked": [
"The emergency closure order was issued after
the first vehicle was dispatched.",
"There is a secondary receiving bay that
stays open until 12:00 but only for small packages."
],
"fidelity_rules": [
"Do not invent new vehicle IDs or shipment IDs
beyond those in the scenario.",
"Do not assume the clinic can extend hours."
],
"helpfulness_rules": [
"If the agent asks for operating hours,
provide the current (mutated) hours.",
"If the agent asks why the deadline changed,
state the emergency closure but only after being asked."
],
"persona_name": "I am a logistics coordinator at the central hub,
responsible for temperature-sensitive deliveries.",
"persona_background": "This shipment is critical for pediatric patients.
The clinic’s hours changed due to an emergency.",
"communication_style": "Professional but slightly anxious
about the deadline;
responds concisely with relevant data.",
"key_preferences": [
"The shipment ID is SHIP-INS-001.",
"Clinic normally closes at 17:00 but today closes at 10:00.",
"Vehicle V002 has a faster cooling unit than V001."
],
"clarification_responses": {
"What is the deadline?": "The insulin must arrive before 10:00 today.",
"Can we use a different clinic?":
"No, it must be CLINIC-DOWNTOWN for the specific pediatric patients.",
"What vehicles are available?":
"V001 and V002 are idle now, but V002 is faster."
}
}
}
]
Figure15: Exampleofuserprofile,ourusersimulatorisconfiguredbytheprofileandinteractwith
thetestedLLMs.
20

<!-- page 21 -->

ExampleofChecklist
Has the shipment record for the insulin batch been created?
Has the shipment been assigned to a refrigerated vehicle?
Has the route plan included the destination clinic?
Has the goods receipt been registered at the clinic before
the deadline (2024-08-15 10:00)?
Has the final delivery respected the mutated clinic
operating hours?
Figure16: Exampleofchecklistwhichistheevaluationmechanismofourtasks.
ExampleofCheckFunctions
def check_shipment_exists(env):
shipments = getattr(env, ’shipments’, {})
for s in shipments.values():
if s.get(’goods_id’) == ’INS-2024-001’:
return True, "Shipment␣record␣found."
return False, "Shipment␣record␣missing."
Figure17: ExamplePythonfunctionthatvalidatesonechecklistitem.
ExampleofDynamicEnvironment
class ColdChainLogisticsEnv:
def __init__(self, init_config: dict):
# Top-level state mapping
self.distribution_hubs =
init_config.get("distribution_hubs", {})
self.depots = init_config.get("depots", {})
self.vehicles = init_config.get("vehicles", {})
self.cooling_units =
init_config.get("cooling_units", {})
self.cooling_unit_resets =
init_config.get("cooling_unit_resets", {})
self.shipments = init_config.get("shipments", {})
self.goods_inventory =
init_config.get("goods_inventory", {})
self.route_stops = init_config.get("route_stops", {})
self.clinics = init_config.get("clinics", {})
# Internal tracking for conflict triggering
self._conflict_armed = False
self._conflict_fired = False
self._conflict_vehicle_id = "VH001"
self._conflict_reset_window_id = "RST1001"
self._conflict_depot_id = "DPT010"
self._conflict_cooling_unit_id = "CU1001"
self._operation_log = []
# ------ INFORMATION QUERY OPERATIONS ------
def get_vehicle_status(self, vehicle_id: str): ...
def list_depot_maintenance_schedule(
self, depot_id: str, time_range: dict
): ...
def get_shipment_journey_status(self, shipment_id: str): ...
def get_route_stop_details(self, vehicle_id: str): ...
def get_goods_inventory_at_site(self, site_id: str): ...
def list_clinic_immunization_schedule(self, site_id: str): ...
21

<!-- page 22 -->

def list_operational_hours(self, site_id: str): ...
def get_cooling_unit_status(self, cooling_unit_id: str): ...
# ------ ADMINISTRATIVE / STATE-CHANGE OPERATIONS ------
def assign_shipment_to_vehicle(
self, shipment_id: str, vehicle_id: str
): ...
def record_cooling_unit_reset(
self, reset_window_id: str, action: str, timestamp: str
): ...
def update_vehicle_status(
self, vehicle_id: str, status: str, current_site_id: str
): ...
def schedule_cooling_unit_reset(
self, cooling_unit_id: str,
depot_id: str,
requested_window: dict
): ...
def add_or_update_route_plan(
self, vehicle_id: str, route_plan: list
): ...
def update_route_stop_actual_times(
self, route_stop_id: str, actual_arrival: str,
actual_departure: str
): ...
def register_goods_receipt(
self, shipment_id: str, site_id: str, timestamp: str
): ...
def update_goods_inventory_status(
self, goods_id: str, status: str,
current_location_id: str
): ...
def create_new_shipment(
self, goods_id: str, origin_hub_id: str,
destination_hub_id: str,
departure_time: str
): ...
Figure18: Exampleofdynamicenvironmentwhichinjectsthespatio-temporaltriggersintothestatic
one.
D.2 CasesofFailureMode
AsshowninFigures19,20,and21,weproposesomecasesaboutthefailuremodesinSTT-Arena.
FailureModeCase: Stale-StateExecution
Task: Ensure that irrigation for Field Segment C begins at 07:00 with valve
sequence V1, V2, V3, targeting 12,000 liters.
[Step 1] Agent queries get_field_segment_status("C") and retrieves the
current segment state. Key finding: only V3 is assigned to Segment C (not
V1/V2/V3 as expected), and V3 is already open. The agent forms the initial
plan: "an irrigation schedule likely exists; I need to find it."
[Step 2] Agent calls get_irrigation_schedule with schedule_id="SCHED_C".
Result: {"error": "IrrigationSchedule not found"}
(cid:44)→ Rather than updating its world model (“no schedule exists”), the agent
retains its prior assumption and issues 20+ consecutive retry calls with
guessed identifiers:
22

<!-- page 23 -->

schedule_id = "SCHED_C_1", "schedule_c", "1", "2", "IRR_C",
"IRR_C_0700", "C_0700", "SC1", "SCHED_1", "farm7_c",
"seg_c", "sched_seg_c", "tomato_south", "c_morning",
"SCHED_C_AM_0700", "C_IRR", "C_daily", ...
(all return "IrrigationSchedule not found")
[Step 3 — After 20+ failed retries] Agent finally abandons schedule lookup
and proceeds to a different action without refreshing environmental state.
It assigns V1 and V2 to Segment C, then closes both V2 and V3 to “prepare
for the 07:00 start.”
Failure Analysis: The agent committed to a stale belief — that an
irrigation schedule must exist — and exhausted over 20 tool calls retrying
the same query with different ID guesses. At no point did it re-query the
environment to verify whether a schedule was actually present, nor did it
consider constructing a new schedule as the correct recovery action. The
agent executed against its initial assumptions rather than the evolving
ground truth, a textbook instance of Stale-State Execution.
Figure 19: A representative Stale-State Execution failure: the agent makes 20+ blind retries on
get_irrigation_schedulewithguessedidentifiersafterthefirstfailure,ratherthanrefreshingits
environmentstateandreplanning.
FailureModeCase: MisdiagnosisofDynamicTriggers
Task: Book a connecting flight itinerary (PVG → CDG) with a layover in
AMS, ensuring the total journey completes before 18:00 local time.
[Step 1] Agent calls search_flights("PVG", "AMS") and selects flight KL-891
(departs 08:30). It then calls search_flights("AMS", "CDG") and selects
connecting flight AF-1234 (departs 14:00, ample layover). Plan looks
feasible.
[Step 2 — Spatio-temporal trigger fires] A Schengen transit regulation
update takes effect while the agent is mid-booking: passengers holding the
user’s passport category now require a transit visa for AMS, making KL-891
unavailable for booking.
[Step 3] Agent calls book_flight("KL-891", passenger_id="P-0042").
Result: {"error": "Booking rejected: passenger ineligible for this
routing"}
(cid:44)→ The agent interprets the rejection as a parameter formatting error
rather than a regulatory block. It proceeds to retry with surface-level
variations:
book_flight("KL-891", passenger_id="P-42") ×
book_flight("KL-891", passenger_id="0042") ×
book_flight("KL891", passenger_id="P-0042") ×
(all return the same eligibility rejection)
[Step 4] After exhausting ID format variants, the agent shifts its
diagnosis: it now attributes the failure to a transient seat-availability
glitch and calls get_flight_status("KL-891") to “confirm the seat is
still open.” The status returns available, which the agent incorrectly
treats as confirmation that the booking error was temporary. It retries
book_flight("KL-891") once more.
[Step 5] Agent eventually attempts to reroute through a different hub
(FRA), but selects LH-445 which also transits Schengen territory — the same
regulatory block applies. Task fails.
Failure Analysis: The dynamic trigger (a regulatory restriction tied to
passport category and transit location) produced a semantically distinct
error signal — passenger ineligibility — that the agent consistently
misread as either a parameter formatting issue or a transient system fault.
The agent treated tool feedback as surface-level content to be retried
23

<!-- page 24 -->

rather than as evidence of a deeper environmental state change. Correct
recovery required inferring why the booking was rejected before deciding
how to respond (e.g., routing via a non-Schengen hub such as IST or DOH).
This is a textbook instance of Misdiagnosis of Dynamic Triggers.
Figure20: ArepresentativeMisdiagnosisofDynamicTriggersfailure: aSchengentransitrestriction
blocksthebooking,buttheagentrepeatedlymisattributestherejectiontoparameterformattingerrors
ortransientglitches,andsubsequentlyselectsanalternativeroutesubjecttothesameundetected
constraint.
FailureModeCase: MissingPost-AdaptationVerification
Task: Fulfil a same-day vaccine delivery order of 500 doses to
Clinic-Downtown before 15:00. Doses are to be drawn from Warehouse-North
(primary) with Warehouse-East as a fallback.
[Step 1] Agent calls get_inventory("Warehouse-North") and finds
500 doses available. It calls reserve_inventory("Warehouse-North",
qty=500) — reservation succeeds. It then calls dispatch_vehicle("V-07",
origin="Warehouse-North", destination="Clinic-Downtown").
[Step 2 — Spatio-temporal trigger fires] A hub outage at Warehouse-North
causes its cold-chain system to fail, immediately releasing all reservations
and marking its 500 doses as quarantined. Vehicle V-07’s dispatch is
cancelled automatically.
[Step 3] Agent observes the dispatch cancellation and correctly identifies
that a disruption has occurred. It calls get_inventory("Warehouse-East")
and finds 320 doses available — a partial quantity. The agent calls
reserve_inventory("Warehouse-East", qty=320).
Result: {"success": true, "reserved": 320}
[Step 4 — Adaptation step] Agent calls dispatch_vehicle("V-12",
origin="Warehouse-East", destination="Clinic-Downtown", qty=320).
Result: {"success": true, "eta": "14:35"}
(cid:44)→ The dispatch tool returns success. The agent equates this intermediate
action success with overall task completion and terminates:
> Task Completed
[Ground truth check] Checklist evaluation reveals:
• [PASS] Disruption detected and primary route abandoned.
• [PASS] Fallback warehouse engaged within the time window.
• [FAIL] Total doses delivered: 320 / 500. Shortfall of 180 doses
unaddressed.
• [FAIL] Agent never queried remaining inventory at other depots
(Warehouse-South holds 200 doses) nor attempted a supplementary
dispatch to cover the deficit.
Failure Analysis: The agent correctly detected the dynamic trigger and
executed a valid adaptation step (rerouting to Warehouse-East). However,
it never verified whether the post-adaptation global state actually
satisfied the original task constraint (500 doses delivered). Tool-level
success — dispatch_vehicle returning success — was incorrectly equated with
task-level success. In spatio-temporal dynamic environments, adaptation is
complete only when the resulting global state is feasible with respect
to all original requirements. This is a textbook instance of Missing
Post-Adaptation Verification.
Figure21: ArepresentativeMissingPost-AdaptationVerificationfailure: afterawarehouseoutage,
theagentcorrectlyreroutestoafallbackdepotbutterminatesuponasuccessfuldispatchcallwithout
verifyingthatthedeliveredquantity(320)meetstheoriginalrequirement(500),leavinga180-dose
shortfallunresolved.
24

<!-- page 25 -->

E PromptTemplates
E.1 PromptTemplatesofStage1: EnvironmentCuration
Inthissection,weproposesystempromptsforenvironmentcurationstage.
E.1.1 Two-StageFilteringPromptTemplate
InEnvironmentCurationStage,wefirstcollectreal-worlduserqueriesandconducttwo-stagefiltering
tomakesureSTT-Arenaismorediverseandsuitableforspatio-temporaldynamictasks. Figure22
andFigure23showthesystemprompttemplateduringtwo-stagefiltering.
SystemPromptforStatefulTaskFiltering
You are a system that filters natural language tasks to determine whether
they are state-dependent, actionable requests within a persistent,
domain-specific environment.
Core Definition
We are ONLY looking for tasks that meet all of the following criteria:
1. Persistent Environment –- The query is about a domain where:
• There is a live, ongoing state that can be read or changed
• The environment supports both:
– Information queries about current state (read operations)
– Explicit state-changing actions (create, update, delete, move,
cancel, etc.)
2. State Dependency –- The task cannot be answered correctly without:
• Inspecting the actual current data or configuration in the
environment, and/or
• Executing an operation that modifies that data
3. Domain Specificity –- The environment is not general-purpose knowledge;
it is a structured system such as:
• File management system with stored files/folders
• Order/logistics tracking system
• Calendar/scheduling system
• CRM, inventory, ticketing, project management tools
• Other specialized platforms with records that persist over time
4. Actionability in Context –- The query must correspond to an actionable
operation or status check within the actual environment (not hypothetical).
Eligible Task Types
• State queries: “Is invoice #1024 paid?” / “What meetings are
scheduled for Wednesday?”
• State modification operations: “Upload the proposal.pdf to the
project folder” / “Cancel order #4512” / “Move meeting to 3 PM”
Explicit Exclusions
A request is NOT eligible if it is:
• Open-domain factual Q&A unrelated to a live state
• Casual conversation
• Content creation
• Pure hypothetical without actual environment interaction
• Isolated reasoning or calculations without accessing persisted state
25

<!-- page 26 -->

Judgment Rule –- Be strict
Choose YES only if:
• The query cannot be answered from general knowledge alone
• AND it requires real-time access to persistent state in a
domain-specific environment
• AND it targets an actionable operation (either a read or a write)
• AND the environment has the capability for both queries and
modifications
If any criterion is missing → NO.
Task
Given a query, first analyze whether it implies or requires:
• A domain-specific environment with both query and modification
capabilities
• Accessing or updating persistent state
• Performing a concrete, actionable operation
Then give your final judgment.
Output Format (Strictly enforce)
# Analysis
<Detailed reasoning whether this query depends on persistent state, involves
a stateful operation, and needs a capable environment as defined>
# Answer
YES (only if all strict criteria are met)
NO (otherwise)
Figure22: Systempromptforthestatefultaskfilter(Stage1,Step1). ThispromptinstructstheLLM
toretainonlyqueriesthatrequireapersistent,domain-specificenvironmentwithbothreadandwrite
operations,discardingopen-domainorhypotheticalrequests.
Spatio-TemporalSensitiveFilter
You are an expert judge for spatiotemporal dependency and multi-API conflict
analysis on stateful tasks.
Your job is to judge whether a task should be selected as a benchmark
candidate for the Step 3 conflict injection pipeline.
Conflict Taxonomy
A task should be kept only if a competent agent solving it could naturally
encounter at least one realistic conflict mechanism during a normal
multi-step workflow:
• T1: State drift –- resource mutates between observation and action.
• T2: Validity expiration –- a time-limited artefact expires between
acquisition and use.
• T3: Schedule/window violation –- an operation becomes invalid
outside a permitted time window.
• S1: Resource locality mismatch –- the target is bound to the wrong
location / branch / node.
• S2: Jurisdictional barrier –- a policy, licensing, or regulatory
boundary blocks the operation.
• S3: Topology disruption –- a physical or logical path becomes
blocked or re-routed.
• ST1: Dynamic spatial impact –- a temporal event reshapes the
spatial landscape.
26

<!-- page 27 -->

• ST2: Cascading dependency –- a temporal failure propagates
spatially to downstream resources.
• ST3: Moving-window resource –- a resource is only available within
a joint time + location window.
Evaluation Dimensions
Evaluate the provided task using these dimensions:
1. Whether the task has real temporal affinity for T1/T2/T3 conflicts.
2. Whether the task has real spatial affinity for S1/S2/S3 conflicts.
3. Whether the task has joint spatiotemporal or strict dependent
workflow structure supporting ST1/ST2/ST3 conflicts.
4. Whether the conflict lies on a normal, competent execution path
rather than an unnatural contrived setup.
5. Whether the task has enough multi-step dependency that an injected
conflict would be meaningful, observable, and benchmark-worthy.
Judgment Rule
• Answer YES only if the task naturally supports at least one concrete
conflict code.
• Answer NO if the task is stateful but does not clearly support any
realistic conflict mechanism.
Be Strict
• Prefer NO for simple CRUD-like stateful tasks.
• Prefer NO when time/space language is superficial.
• Prefer YES only when conflict opportunity is central to correct
execution.
• Multi-step logic without plausible conflict codes should still be
NO.
User Prompt
Analyze the following stateful task for spatiotemporal dependencies and
multi-API call conflicts.
Task: {query}
Decide whether this task should be kept for Step 3 conflict injection, based
on whether it supports one or more concrete conflict codes.
Output Format
# Analysis
<detailed reasoning grounded in the conflict taxonomy>
# Dependency Type
<Temporal / Spatial / Joint / Sequential / None>
# Conflict Codes
<comma-separated codes such as T1, ST2, S3, or None>
# Answer
YES or NO
Figure23: Systempromptforthespatio-temporalsensitivityfilter(Stage1,Step1). Thisprompt
evaluateswhetherastatefulquerynaturallysupportsatleastoneconcretespatio-temporalconflict
mechanismfromthenine-typetaxonomy,filteringouttaskswithonlysuperficialtemporalorspatial
language.
27

<!-- page 28 -->

E.1.2 PromptTemplateforEnvironmentSynthesis
Wethengeneratestaticexecutableenvironmentsbasedonthefilteredqueries. First,wepromptan
LLMtoinfertheenvironmentinformationasthesystemprompttemplateisshowninFigure24.
Then we generate the entity attributes and tool specifications as illustrated in Figures 25 and 26.
Finally,asshowninFigures27and28,wepromptanLLMtoimplementtheentityattributesand
toolspecificationstoPythonclassesandconcatenatethemtoacompletestaticenvironment.
InferEnvironmentInformation
You are a Task Analyst.
Given a raw task description, your objective is to identify the most
plausible stateful and domain-specific environment in which this task would
naturally occur.
The chosen environment should strike a balance: not so broad as to be
meaningless, and not so narrow as to apply only to a single, highly specific
case. It should be scoped such that this task, along with similar related
tasks, can be executed meaningfully.
Guidelines
• If multiple environments seem equally plausible, select one at
random rather than listing all possibilities.
• Example: if a task could occur in a Linux, Windows, or macOS
filesystem, randomly choose one instead of remaining indecisive.
Required Response Sections
Your response must include the following sections:
1. # Analysis
• Explain the reasoning process used to connect the task to the
chosen environment.
• Note any relevant entities, constraints, relationships, or
dynamics implied by the task.
2. # Environment Summary
• Provide a concise label for the environment type.
• Examples: Linux filesystem, E-commerce order management system,
Airline booking system.
3. # Environment Introduction
• Introduce the environment itself, without referring to the
current task.
• Focus on its inherent structure, the nature of the state it
maintains, typical operations it supports, and its general
real-world scope.
• Limit to approximately three sentences.
4. # Metrics
• Usefulness (1–10): how broadly applicable and valuable this
environment is in real-world scenarios.
• Modelability (1–10): how straightforward it would be to
represent this environment using a single Python class with
stateful attributes and operational methods.
Output Format
# Analysis
<Your analysis>
# Environment Summary
<Your environment summary>
# Environment Introduction
<Your environment introduction>
28

<!-- page 29 -->

# Metrics
Usefulness: [1–10]
Modelability: [1–10]
No additional text or commentary.
Figure24: Systempromptforinferringthelatentenvironmentcontextfromaseedquery(Stage
1, Step 2). The LLM identifies the most plausible domain-specific environment and provides a
structuredsummary,introduction,andfeasibilitymetricstoguidesubsequentsynthesis.
InferEntityAttributes
You are an expert task and environment analyst.
Given an environment description and an example task in this environment,
infer the set of state variables (state space) maintained by the
environment.
The state should not be too broad (e.g., all possible data in an e-commerce
system), nor too narrow (only for this single task). It should be
reasonably designed to support this task and similar tasks in the same
environment.
Input Format
# Environment Summary
<Environment summary>
# Environment Introduction
<Environment introduction>
# A Example Task in This Environment
<Example task>
Required Output Sections
1. # Analysis
• Explain what states are involved in the environment.
• Identify what entities and attributes need to be tracked.
• Note relevant constraints, operational rules, and dependencies.
2. # State Space Definition
• Define the major entities maintained by the environment.
• For each entity, specify attributes and describe its functional
role.
3. # Constraints & Rules
• Summarize core consistency rules, domain constraints,
permissions, capacities, temporal rules, or structural
restrictions.
Output Format
# Analysis
<Your thought process>
# State Space Definition
- Entity: EntityName1
- Attributes: Attribute1, Attribute2, ...
- Description: The role of this entity in the environment
- Entity: EntityName2
- Attributes: ...
- Description: ...
# Constraints & Rules
- Constraint 1
- Constraint 2
...
Do not include any additional text.
29

<!-- page 30 -->

Figure25: Systempromptforinferringentityattributesandthestatespacedefinition(Stage1,Step
2). Givenanenvironmentsummaryandanexampletask,theLLMenumeratesthemajorentities,
theirattributes,anddomainconstraintsthatmustbetrackedacrossmulti-steptoolinteractions.
InferToolSpecification
You are an expert in building and analyzing agent environments.
Given an environment summary, introduction, state space definition,
constraint rules, Python base class definition, and example task, your goal
is to analyze the current environment and generate the list of operations
needed to support the task in this environment.
Each operation will later be converted into a callable class function for
the agent.
Key Points
• Operations are divided into two categories:
– Information Query Class
– State Change Class
• Each operation must include:
– Operation name
– Brief description
• Before output, first write # Analysis:
– Explain task logic
– Determine which operations are query operations
– Determine which are state-changing operations
– Explain how environment constraints affect operation design
Input Format
Based on the following environment specification, produce the operation
list.
{
"environment_summary": "...",
"environment_introduction": "...",
"state_space_definition": [...],
"constraints_rules": [...],
"environment_class_definition": "...",
"environment_example_task": "..."
}
Output Format
# Analysis
<Explain operation requirements, classification logic, and how constraints
affect the operation set>
# Operation List
## Information Query Class
- Operation: OperationName Description: xxxx
- Operation: OperationName Description: xxxx
- ...
## State Change Class
- Operation: OperationName Description: xxxx
- Operation: OperationName Description: xxxx
- ...
Strictly follow this format.
Figure26: Systempromptforinferringthetooloperationlist(Stage1,Step2). TheLLMgeneratesa
categorizedlistofqueryandstate-changeoperationsrequiredtosupporttaskexecutionwithinthe
synthesizedenvironment.
30

<!-- page 31 -->

InferEntityAttributesPythonCode
You are an AI coding assistant.
Your job is to translate an environment specification into a Python
environment class definition.
The class should simulate the stateful environment structure (without
methods yet).
You should first analyze the specification and then generate code.
Rules of Analysis
• Determine the environment class name using the environment
summary or an appropriate adaptation. Example: LinuxFileSystem,
EcommerceOrderSystem.
• Extract attribute names from each entity in state_space_definition.
• If needed, generate corresponding TypedDict definitions.
• Infer attribute value types using Python primitive types:
– id, name, category → str
– price, size → float / int
– quantity → int
– status → str
– timestamps → str / float
• constraints_rules should be preserved as comments.
Rules of Code
• Generate each TypedDict definition if needed.
• Generate the environment class with only:
– __init__
– state attributes
• Use attributes of type Dict<ID, TypedDict> where appropriate.
• Add comments mapping attributes back to state-space entities.
• Annotate constraints as code comments.
• Do not implement business logic or methods yet.
Input Format
# Environment Summary
<short label>
# Environment Introduction
<paragraph intro>
# State Space Definition
[ { "entity": "EntityName",
"attributes": "attr1, attr2, ...",
"description": "short description" }, ... ]
# constraints_rules
constraint 1 ...
constraint 2 ...
Output Format
# Analysis
<Explain class naming, entity-to-structure mapping, stored fields, dict/list
design, and constraint annotations>
# Class Definition
“‘python
<Python environment class definition>
“‘ Do not include any additional text.
31

<!-- page 32 -->

Figure27: SystempromptforgeneratingtheentityattributePythonclass(Stage1,Step2). TheLLM
translatesthestatespacedefinitionintoatypedPythonclasswithonly__init__andstateattributes,
annotatingconstraintsascodecomments.
InferToolSpecificationPythonCode
You are a code generation assistant.
Given an agent environment (including environment summary, introduction,
state space definition, constraint rules, base class definition, and
operation list), your task is to implement a single target operation as a
Python method within the environment class.
Operation Types
• Information Query Operations
• State Modification Operations
Core Requirements
For a given Target Operation:
1. # Analysis
• Identify involved entities and attributes
• Determine required parameters
• Define expected outputs (query vs modification)
• Identify edge cases (invalid input, missing state, permission
issues)
• Consider relevant environment constraints
2. # Code
• Implement method as def operation_name(self, ...)
• Method must be inside an existing environment class (not
standalone)
• Use type hints
• Include docstring (inputs, outputs, constraints)
• Do not raise exceptions
• Return structured dictionaries:
– Success: {"success": True, "data": ...} (query)
– Success: {"success": True, "message": ...} (state change)
– Failure: {"success": False, "error": "..."}
Input Format
# Environment Summary
<environment_summary>
# Environment Introduction
<environment_introduction>
# State Space Definition
<state_space_definition>
# Constraints Rules
<constraints_rules>
# Class Definition
“‘python
<class_definition>
“‘
# Operation List
operation_list
# Target Operation
"operation_name": "<operation_name>",
"operation_description": "<operation_description>",
"operation_type": "<query_or_state_change>"
32

<!-- page 33 -->

Output Format
# Analysis
<Reasoning: inputs, outputs, entities, attributes, constraints, edge cases>
# Code “‘python
def <operation_name>(self, ...):
"""
<docstring describing inputs, outputs, constraints>
"""
# Implementation
“‘
Figure28:SystempromptforimplementingindividualtoolmethodsasPythoncode(Stage1,Step2).
Eachoperationfromthetoollistisimplementedasaclassmethodreturningstructuredsuccess/failure
dictionaries,withnoexceptionraising.
E.1.3 FunctionalValidationPromptTemplate
Weconductfunctionalvalidationwhenobtainthecandidatestaticenvironments. First,wepromptthe
tool-callingLLMtogeneratetestconfigurationsandthesystempromptisshowninFigure29. Then,
asshowninFigure30,wepromptthetool-callingLLMtogeneratethesequenceofvalidationtool
callstofilterthecandidatestaticenvironments.
TestConfigGeneration
You are an AI assistant.
You will be given the complete definition of a Python class. This class
represents an environment state in a specific domain and contains various
attributes (such as dictionaries, lists, TypedDict objects, dataclasses,
etc.) used to manage entities and their relationships within the system.
Based on the class definition, generate a JSON object that can serve
directly as the class initialization configuration (config), following the
rules below.
1. Structure and Type Matching
• The JSON must strictly follow the attribute structure and data types
required by the class.
• Field names, nesting levels, and value types must match the class
definition exactly.
2. Respect Constraints
• Read class methods and docstrings to identify constraints (e.g.,
valid status values, required fields, ID reference rules).
• Ensure all generated data complies with these constraints.
• All cross-entity references must be valid and consistent.
3. Richness of Data
• Each major dictionary-like attribute should contain 3–5 diverse
entries.
• Cover different valid states and value ranges.
• Dates should be distributed over a reasonable time span.
• Numerical fields should vary realistically.
4. Realistic Simulation of Data
• Use natural fictional names (e.g., Alice Chan, Central City
District).
• Avoid placeholder-like values (e.g., name1, user001).
• Dates must be in ISO format (YYYY-MM-DD) or timestamps.
33

<!-- page 34 -->

• IDs should be unique and may mix short codes and UUIDs.
• All data must be fictitious and non-sensitive.
5. Output Format
• Output only JSON (no explanations outside required sections).
• Must be directly usable as class initialization config.
Input
Env Class Definition
“‘python
{env_class_code}
“‘
All Containers
{all_containers} Output Format
# Analysis
<Reasoning: containers, fields, constraints, and data construction
strategy>
# Init Config
{
...
}
Figure29: Systempromptforgeneratingtestconfigurationsforfunctionalvalidation(Stage1,Step
3). TheLLMproducesarealistic,constraint-compliantJSONinitializationconfigwith3–5entries
permajorentitytosupportdiversevalidationscenarios.
SequenceofToolCallsGeneration
You are an experienced testing engineer, performing comprehensive
exploratory testing on all tool interfaces (methods) of a simulated
environment class.
Your goal is to verify the behavior of each method under different types
of inputs, aiming to uncover potential errors, exceptions, and state
inconsistencies.
In each testing round, you will generate one tool invocation as a test case.
After execution, you will receive the environment’s return information along
with a backend evaluation (pass, warning, fail).
Environment Introduction
{env_introduction}
Available Tool Interface List
{tool_info}
Testing Strategy
• Positive case testing: use valid parameters that comply with
interface definitions.
• Negative case testing: use invalid, missing, or malformed
parameters (wrong types, non-existent IDs, out-of-range values,
etc.).
• Special case testing: include boundary values, null/empty inputs,
extreme values, and special characters.
• Ensure all tool interfaces are covered; balance both breadth and
depth of testing.
• No need to maintain a consistent task objective; exploration is
encouraged.
Testing Rules
34

<!-- page 35 -->

• Only one tool invocation per round.
• Parameters must be in dictionary format.
• Keys must be valid; values may be intentionally invalid for
robustness testing.
• Do not call methods outside the provided tool list.
Output Format
Strictly follow:
# Thought
<Brief explanation of chosen method and parameter strategy>
# Selected Function
<Method name>
# Parameters Dictionary
<Parameter dictionary>
Figure30: Systempromptforgeneratingthesequenceofvalidationtoolcalls(Stage1,Step3). A
tool-callingLLMperformsexploratorytestingacrosspositive,negative,andboundarycasestoverify
thatalltoolinterfacesexecutecorrectlybeforeanenvironmentisadmittedtoE .
static
E.2 PromptTemplatesofStage2: Spatio-TemporalDynamicInjection
Inthissection,weproposesystempromptsforspatio-temporaldynamicinjectionstage.
E.2.1 ConflictAssignmentandBlueprintGenerationPromptTemplate
During Stage 2, we first assign several proper conflict types to a static environment, the system
promptcanbefoundinFigure31. Then,basedontheconflicttypesandenvironmentinformation,
wegenerateablueprintwhichservesasagenerativecontractensuringinternalconsistencyacrossall
downstreamcomponents. ThesystempromptisshowninFigure32.
ConflictAssignment
You are a benchmark designer for spatiotemporal AI agent evaluation.
Task
Identify which conflict types from the taxonomy are feasible for the given
environment.
A conflict type is considered feasible only if the environment’s state space
and operations can naturally support:
• a valid activation trigger,
• a conflict firing mechanism,
• and a resulting observable state update.
Conflict Taxonomy
{taxonomy_block}
Environment
{env_summary}
Output Format
# Analysis
<Reasoning: which conflict types are supported by the environment, and why
others are not>
# Matched Conflicts
• Conflict: <T1 | T2 | T3 | S1 | S2 | S3 | ST1 | ST2 | ST3>
Rationale: <1–2 sentence explanation>
Activation Operations: <comma-separated operation names from
environment>
35

<!-- page 36 -->

Observation Operations: <comma-separated operation names from
environment>
• Conflict: <type>
Rationale: <explanation>
Activation Operations: <...>
Observation Operations: <...>
Rules
• Activation operations must be those that can trigger the conflict.
• Observation operations must reveal the resulting state change.
• Only use real operation names from the environment.
• Prefer conflicts that are genuinely supported by both state and
operations.
• Include only 3–6 feasible conflict types.
Do not output anything outside the required format.
Figure31:Systempromptforconflicttypeassignment(Stage2,Step1). Givenastaticenvironment’s
statespaceandoperations,theLLMidentifieswhichoftheninespatio-temporalconflicttypesare
naturallysupportable,specifyingtherelevantactivationandobservationoperations.
BlueprintDesign
You are a benchmark scenario designer for AI agent evaluation.
Task
Design a CONCRETE conflict scenario for the given environment.
Your output must specify:
• exact operation names,
• state container names,
• field-level mutation descriptions.
Abstract or vague descriptions are not acceptable.
Environment
{render_json(env_summary)}
Conflict Type
• Type: {conflict_type} –- {CONFLICT_TAXONOMY[conflict_type]}
• Event pattern: {render_json(EVENT_TEMPLATE_PATTERNS[conflict_type])}
• Match rationale: {match_rationale}
Difficulty
{difficulty}
{diff_instructions}
Design Rules
1. Normal flow must use ONLY operations from the environment’s
operation list.
2. Activation operation must be a READ/QUERY operation where the
conflict becomes visible during normal execution.
3. Mutations must reference REAL state container names from
state_space_definition.
4. Mutations must describe field-level changes, not vague availability
changes.
36

<!-- page 37 -->

5. The conflict must match its taxonomy semantics (e.g., T2 requires
temporal ordering changes).
6. Observable_via must be an operation that reveals the mutated state.
7. Trigger must depend on TASK or STATE CONDITIONS, not call order.
8. Trigger type must be:
• always_once: fires once when condition is met
• conditional_guarded: keeps affecting execution until recovery
Output Format
# User Goal
<1–2 sentences describing the user’s objective>
# Normal Flow
• <operation_name> –- <purpose>
• <operation_name> –- <purpose>
• ...
# Conflict Design
• Activation Operation: <exact operation name>
• Trigger Mechanism: <always_once | conditional_guarded>
• Trigger Condition: <concrete condition that causes conflict>
• Recovery Guard Condition: <or "none">
• Mutations:
– State: <state_container.field_path> | Change: <old → new>
– State: <state_container.field_path> | Change: <old → new>
• Observable Via: <operation name>
{Recovery Path if diff_info["task_solvable"] else "Impossible Rationale"}
• If solvable: step-by-step recovery using real operations
• If not solvable: explain violated constraints
Output ONLY the sections above.
Figure 32: System prompt for conflict blueprint design (Stage 2, Step 1). The LLM generates a
structured, field-level conflict scenario blueprint encoding the user goal, nominal tool sequence,
triggercondition,statemutations,recoverypath,andassigneddifficultylevel.
E.2.2 DynamicEnvironmentConstructionPromptTemplate
Basedontheblueprint,wepromptanLLMtoaugmentthestaticenvironmenttoaspatio-temporal
dynamicone. ThesystempromptcanbefoundinFigure33. Then,wegeneratetheuserquery,initial
configuration,anduserprofileasshowninFigures34and35toobtainthecompletedynamictasks.
Spatio-TemporalDynamicTriggerInjection
You are an expert Python developer.
Your task is to modify an environment class to inject a deterministic
conflict trigger.
Original Environment Code
37

<!-- page 38 -->

“‘python
{env.get("env_class_code", "")}
“‘
Conflict Specification
• Type: {conflict_type} –- {CONFLICT_TAXONOMY[conflict_type]}
• Activation Operation: {activation_op} (method that triggers the
conflict)
• Trigger Mechanism: {trigger_mechanism}
• Trigger Condition: {trigger_condition}
• Recovery Guard Condition: {recovery_guard_condition}
• Observable Via: {observable_op}
Exact Mutations to Apply
When the trigger condition is met inside {activation_op}, apply the
following mutations:
{mutation_block}
Injection Rules
1. Add self._conflict_triggered = False in __init__
2. Trigger must depend on real state or input conditions, not call
counts
3. Implement trigger logic inside {activation_op}
4. If always_once:
• Fire only once when condition is first satisfied
• Apply exact mutations
• Set self._conflict_triggered = True
5. If conditional_guarded:
• Fire whenever condition holds AND recovery condition is not
satisfied
• _conflict_triggered is bookkeeping only
• Stop firing once recovery condition is satisfied
6. Normal operation must always return valid results (no error
injection)
7. Mutated state must remain fully usable by all methods
8. Do not introduce artificial error handling logic
9. {observable_op} requires no modification unless strictly necessary
10. Output the full modified class only
Output Format
# Conflict Environment Code
“‘python
<complete modified Python class>
“‘
Output ONLY the required section.
Figure33: Systempromptforinjectingspatio-temporaltriggersintoastaticenvironment(Stage2,
Step2). TheLLMaugmentsthePythonenvironmentclasswithadeterministicconflicttriggerinside
thedesignatedactivationoperation,supportingbothalways_onceandconditional_guardedfiring
mechanisms.
38

<!-- page 39 -->

UserQueryandInitialConfigurationGeneration
You are a benchmark data engineer. Given an environment and an abstract
scenario design, produce concrete data that makes the scenario executable.
Environment
{render_json(env_info)}
Abstract Scenario Design
{scenario}
Difficulty
{item[’difficulty’]}
• Task solvable after conflict: {diff_info[’task_solvable’]}
• Recovery complexity: {diff_info[’recovery_complexity’]}
Your Task
Generate THREE components:
1. User Query (2–5 sentences)
• Must contain all necessary entity names, dates, locations, and
identifiers
• Must match the init configuration exactly
• Must NOT reveal the existence of any conflict
• Must sound like a natural user request
2. Init Config (JSON)
• Must cover all state containers in the environment
• Must include sufficient entities for both normal and recovery paths
• Must ensure full referential consistency
• Must include at least one alternative entity for recovery
3. Concrete Mutations (JSON array)
• Map abstract mutations to exact entity IDs and fields
• Each entry includes: state container, entity ID, field, old value,
new value
• old value must match init config exactly
• new value must induce intended conflict
Output Format
# User Query
<2–5 sentence task instruction>
# Init Config
“‘json
{ }
“‘
# Concrete Mutations
“‘json
[ ]
“‘
CRITICAL
The init config and concrete mutations must be fully consistent. All old
values must exactly match those in the init config.
Figure34: Systempromptforgeneratingtheuserquery,initialconfiguration,andconcretemutations
(Stage2,Step2). TheLLMgroundstheabstractblueprintintoafullyexecutabletaskinstancewith
consistententityIDs,field-levelmutationvalues,andanatural-soundinguserrequest.
39

<!-- page 40 -->

UserProfileGeneration
You are a user persona designer for an AI agent evaluation benchmark.
Context
An AI agent will interact with a simulated user to complete a task in a
dynamic environment.
User Query
{user_query}
Scenario
• Environment: {item.get("environment_summary", "")}
• Difficulty: {item["difficulty"]}
• Task solvable: {diff_info["task_solvable"]}
User Profile Requirements
The profile helps the simulator:
• Respond naturally to agent questions
• Provide clarification when asked
• NOT proactively reveal conflict information
• Express preferences that guide the agent’s decision-making
• { "Accept reasonable alternatives if the original plan fails"
if diff_info["task_solvable"] else "Insist on the original
requirements; alternatives are NOT acceptable (task is impossible)"
}
Output Format
# User Profile
• Name: <realistic name>
• Background: <1–2 sentences>
• Communication Style: <brief | verbose | formal | casual | technical
| non-technical>
• Frustration Threshold: <low | medium | high>
• Flexibility: <medium or high / low>
Key Preferences
• <preference>
• ...
Clarification Responses
• Topic: <likely agent question>
Response: <how user would respond>
• ...
Figure 35: System prompt for generating the user profile (Stage 2, Step 2). The LLM creates a
personafortheusersimulator,specifyingcommunicationstyle,flexibility,andclarificationresponses
tailoredtowhetherthetaskissolvableorimpossible.
E.3 PromptTemplatesofStage3: Dual-AgentAssessment
Inthissection,weproposesystempromptsfordual-agentassessmentstage.
40

<!-- page 41 -->

E.3.1 ChecklistGenerationPromptTemplates
We prompt an LLM to generate checklist and check functions according to the user query and
blueprint. Figure36showstheprompttemplateofsolvabletasks.
ChecklistGenerationofSolvableTasks
You are a benchmark verification designer. Generate a checklist and Python
function verifying correct CONFLICT-AWARE outcome.
User Query
{item.get("user_query", "")}
Init Config
{render_json(item.get("init_config", {}))}
Conflict Type
- {item["conflict_type"]} — {CONFLICT_TAXONOMY[item["conflict_type"]]}
Concrete Mutations (state changes from conflict)
{render_json(item.get("concrete_mutations", []))}
Difficulty: {item["difficulty"]} — {diff_info["description"]} - Recovery
complexity: {diff_info["recovery_complexity"]}
Environment
{render_json(env_info)}
Checklist Requirements
• Verify the conflict was detected (agent re-queried and saw changed
state)
• Verify the recovery/alternative path was executed correctly
• Verify the final state satisfies the user goal via the alternative
path
• DO NOT check for conflict_triggered (that’s internal)
check_conflict(env) Requirements
• Inspects env.<state_container> attributes directly
• Returns: {{"passed": bool, "details": [{"check_id": "cc_1",
"passed": bool, "message": str}, ...]}}
• No external imports
Output Format
# Conflict Checklist
- Check: cc_1
- Description: <specific>
- Target State: <container name>
- Expected Condition: <testable>
...
# Conflict Check Function
def check_conflict(env) -> dict:
...
Figure36: Systempromptforgeneratingtheevaluationchecklistandcheckfunctionsforsolvable
tasks(Stage3,Step1). TheLLMproducesasetofconflict-awaresuccesscriteriaandcorresponding
Pythoncheckfunctionsthatverifyconflictdetection,recoverypathexecution,andfinalstatevalidity.
E.3.2 Dual-AgentValidationPromptTemplates
Weconductdual-agentvalidationtoobtainexecutablespatio-temporaldynamicenvironmentsand
tasks. AsshowninFigure37,plan-agentfirstplansasequenceoftoolcallsandcheck-agentthen
evaluatesthetrajectoriesoftheexecutionresultsofplanningtoolcallsasFigure38illustrates.
41

<!-- page 42 -->

Plan-AgentSystemPrompt
You are the plan agent for conflict-environment validation.
Your job is to produce a COMPLETE tool-call plan that executes the task from
the original user request, follows the designed story, naturally reaches
the conflict, and then continues far enough to verify whether the conflict
environment behaves correctly.
User Query
{item.get(’user_query’, ”)}
Scenario Story
{render_json(story)}
Full Init Config
{render_json(item.get(’init_config’, {}))}
Available Tools
{render_json(_build_tool_reference(item))}
Requirements
• Output a COMPLETE executable plan for the task, not a minimal
trigger-only probe.
• The plan should reflect the user_query plus the normal_flow story in
order.
• Use ONLY real tool names from the available tools.
• Use ONLY concrete argument values grounded in the user_query and
init_config summary.
• The plan must naturally reach the conflict through the original
intended workflow, not through a synthetic shortcut.
• After the conflict is triggered, include the necessary follow-up
calls to observe the changed state and verify whether task progress
behaves as expected.
• Do not add explanations outside the requested section.
Output Format
# Test Plan
[
{"method": "<method_name>", "arguments": {...}},
...
]
Output ONLY the section above.
Figure37:Systempromptfortheplanagentindual-agentverification(Stage3,Step2).Theplanning
agentproducesacomplete,blueprint-guidedtool-callsequencethatnaturallyreachestheinjected
conflictandincludesfollow-upcallstoobservepost-triggerstatechanges.
Check-AgentSystemPrompt
You are the check agent for conflict-environment validation.
Judge whether the executed path is valid and whether the spatiotemporal
conflict is triggered in the intended workflow.
Scenario Story
{render_json(story)}
Conflict Story
{render_json(conflict_story)}
Tool Calls And Results
{render_json(validation.get(’trajectory’, []))}
Decision Rules
42

<!-- page 43 -->

• Verify whether the tool-call path follows the intended normal
workflow in the story.
• Verify whether the called tools are appropriate and whether the
calls execute normally for the intended path.
• Verify whether there are unexpected errors that should not appear in
a valid execution path.
• Verify whether the spatiotemporal conflict is triggered at the
intended point in the path according to the conflict story.
• Return Pass if the path is correct, the tool executions are normal
enough for the intended workflow, no inappropriate errors appear,
and the intended conflict trigger is correctly evidenced.
• Return Fail otherwise.
• Return Warning only if the main path is mostly correct but the
evidence is slightly incomplete.
Output Format
# Analysis <step-by-step reasoning>
# Result Pass
# Error Reason <No error, or the concrete reason>
Output ONLY the three sections above.
Figure 38: System prompt for the check agent in dual-agent verification (Stage 3, Step 2). The
checkingagentevaluatestheexecutedtrajectoryagainstthreebehavioralinvariants: correcttrigger
timing,correctstatemutation,andfailureoftheoriginalplanaftertheconflictfires.
E.3.3 ConsistencyCheckPromptTemplates
Finally,weconductconsistencychecktomakesureourspatio-temporaldynamicenvironmentsand
tasksareconsistencyandcorrect. ThesystempromptisshowninFigure39.
ConsistencyCheckSystemPrompt
You are a benchmark quality auditor. Judge whether this scenario is
INTERNALLY CONSISTENT across all artifacts.
Scenario ID: {item.get("scenario_id","")}
Story
{render_json(story)}
User Query
{item.get("user_query", "")}
Full Init Config
{render_json(item.get("init_config", {}))}
Conflict Type: {item.get("conflict_type","")} — {conflict_desc}
Difficulty: {item.get("difficulty","")}
Concrete Mutations
{render_json(item.get("concrete_mutations", []))}
Conflict Design
{render_json(conflict_design)}
Evaluation Checklists
{checklist_text}
Your Job
Check whether the artifacts are mutually consistent. Focus on concrete
contradictions, missing links, or implausible transitions.
You must judge at least these dimensions:
43

<!-- page 44 -->

• Query–Config Coherence: does the user_query match the entities,
values, dates, IDs, and constraints in init_config?
• Story–Query Alignment: do user_goal, normal_flow, and
recovery/impossible path actually support the user_query?
• Conflict–Mutation Alignment: do the concrete_mutations and
conflict_design really implement the claimed conflict semantics?
• Checklist Coverage: do the evaluation checklists test the key
success/failure conditions implied by the query and story?
• Difficulty Consistency: is the scenario complexity and
recovery/impossibility behavior consistent with the labeled
difficulty?
• Overall Narrative Consistency: do all artifacts tell one coherent
story without contradictions?
Treat a contradiction as fatal when it would make the benchmark invalid or
misleading.
Output Rules
• Do NOT score.
• Do NOT summarize vaguely.
• Return ‘pass‘ only if there are no fatal consistency issues.
• Return ‘fail‘ if any fatal issue exists.
• Keep each issue concrete and artifact-grounded.
Output Format (strict JSON only)
{
"verdict": "pass" | "fail",
"checks": {
"query_config_coherence": {"passed": true, "reason": "..."},
"story_query_alignment": {"passed": true, "reason": "..."},
"conflict_mutation_alignment": {"passed": true, "reason": "..."},
"checklist_coverage": {"passed": true, "reason": "..."},
"difficulty_consistency": {"passed": true, "reason": "..."},
"narrative_consistency": {"passed": true, "reason": "..."}
},
"fatal_issues": ["<issue1>", ...],
"minor_issues": ["<issue1>", ...],
"suggestions": ["<suggestion1>", ...]
}
Figure 39: System prompt for the consistency auditor (Stage 3, Step 3). An LLM-based auditor
verifiesmutualcoherenceacrossalltaskartifacts—userquery,initconfig,conflictdesign,concrete
mutations,checklist,anddifficultylabel—returningastructuredJSONverdictwithissuedescriptions.
E.4 PromptTemplatesofSTT-ArenaEvaluation
Inthissection,weproposethesystempromptsduringevaluationofSTT-Arena. Figures40,41,and
42showthesystempromptfortestedLLMs,usersimulators,andLLM-as-a-judge.
TestedLLMSystemPrompt
You are an assistant operating inside a tool-based benchmark environment.
Rules:
• Each turn must contain exactly one tool call.
44

<!-- page 45 -->

• Never make parallel tool calls or return multiple tool calls in the
same turn.
• Do not output a normal text response without a tool call, unless you
are responding with exactly: Task Completed
• Prefer querying the environment before making changes.
• If user clarification is needed and the tool is available, use
chat_with_user.
• When the task is complete, respond with exactly: Task Completed
• Do not invent tool results or hidden state.
Figure40: SystempromptfortheevaluatedLLMduringSTT-Arenabenchmarking. Themodelis
instructedtoissueexactlyonetoolcallperturn,preferenvironmentqueriesbeforestatechanges,and
terminatebyoutputting"TaskCompleted".
UserSimulatorSystemPrompt
You are simulating the benchmark user.
Rules:
• Reply as the user in plain natural language only.
• Stay consistent with the provided profile and previously revealed
facts.
• Do not invent facts that are not grounded in the profile.
• Reveal withheld details only when the assistant asks for them
directly.
• If the task is fully satisfied, reply with the completion signal
exactly and nothing else.
Figure41: Systempromptforthepassiveusersimulatorduringevaluation. Thesimulatorresponds
innaturallanguageconsistentwiththeuserprofile,revealswithhelddetailsonlyupondirectquery,
andemitsafixedcompletionsignalwhenthetaskisfullysatisfied.
LLM-as-a-JudgeSystemPrompt(ImpossibleTask)
You are judging whether an agent handled an impossible task correctly.
Ground truth: this task has no compliant completion path.
Mark the trajectory correct only if the agent recognizes that the task
cannot be completed compliantly and communicates that blocked state back to
the user.
Return JSON only:
{
"passed": true,
"recognized_impossibility": true,
"fed_back_to_user": true,
"evidence": ["short evidence"],
"verdict": "short explanation"
}
Figure 42: System prompt for the LLM-as-a-judge on impossible tasks. The judge determines
whethertheagentcorrectlyrecognizedtaskinfeasibilityandcommunicatedthistotheuser,returning
astructuredJSONverdictwithbinaryverdictsandsupportingevidence.
45

<!-- page 46 -->

NeurIPSPaperChecklist
1. Claims
Question: Dothemainclaimsmadeintheabstractandintroductionaccuratelyreflectthe
paper’scontributionsandscope?
Answer: [Yes]
Justification: WeprovideourmainclaimsandcontributionsinAbstractandIntroduction
sections.
Guidelines:
• Theanswer[N/A]meansthattheabstractandintroductiondonotincludetheclaims
madeinthepaper.
• Theabstractand/orintroductionshouldclearlystatetheclaimsmade,includingthe
contributionsmadeinthepaperandimportantassumptionsandlimitations. A[No]or
[N/A]answertothisquestionwillnotbeperceivedwellbythereviewers.
• Theclaimsmadeshouldmatchtheoreticalandexperimentalresults,andreflecthow
muchtheresultscanbeexpectedtogeneralizetoothersettings.
• Itisfinetoincludeaspirationalgoalsasmotivationaslongasitisclearthatthesegoals
arenotattainedbythepaper.
2. Limitations
Question: Doesthepaperdiscussthelimitationsoftheworkperformedbytheauthors?
Answer: [Yes]
Justification: WeprovideadetaileddiscussionofthelimitationsofourpaperinAppendix
B.
Guidelines:
• Theanswer[N/A]meansthatthepaperhasnolimitationwhiletheanswer[No]means
thatthepaperhaslimitations,butthosearenotdiscussedinthepaper.
• Theauthorsareencouragedtocreateaseparate“Limitations”sectionintheirpaper.
• Thepapershouldpointoutanystrongassumptionsandhowrobusttheresultsareto
violationsoftheseassumptions(e.g.,independenceassumptions,noiselesssettings,
modelwell-specification,asymptoticapproximationsonlyholdinglocally).Theauthors
shouldreflectonhowtheseassumptionsmightbeviolatedinpracticeandwhatthe
implicationswouldbe.
• Theauthorsshouldreflectonthescopeoftheclaimsmade,e.g.,iftheapproachwas
onlytestedonafewdatasetsorwithafewruns. Ingeneral,empiricalresultsoften
dependonimplicitassumptions,whichshouldbearticulated.
• Theauthorsshouldreflectonthefactorsthatinfluencetheperformanceoftheapproach.
Forexample,afacialrecognitionalgorithmmayperformpoorlywhenimageresolution
isloworimagesaretakeninlowlighting. Oraspeech-to-textsystemmightnotbe
usedreliablytoprovideclosedcaptionsforonlinelecturesbecauseitfailstohandle
technicaljargon.
• Theauthorsshoulddiscussthecomputationalefficiencyoftheproposedalgorithms
andhowtheyscalewithdatasetsize.
• If applicable, the authors should discuss possible limitations of their approach to
addressproblemsofprivacyandfairness.
• Whiletheauthorsmightfearthatcompletehonestyaboutlimitationsmightbeusedby
reviewersasgroundsforrejection,aworseoutcomemightbethatreviewersdiscover
limitationsthataren’tacknowledgedinthepaper. Theauthorsshouldusetheirbest
judgmentandrecognizethatindividualactionsinfavoroftransparencyplayanimpor-
tantroleindevelopingnormsthatpreservetheintegrityofthecommunity. Reviewers
willbespecificallyinstructedtonotpenalizehonestyconcerninglimitations.
3. Theoryassumptionsandproofs
Question: Foreachtheoreticalresult,doesthepaperprovidethefullsetofassumptionsand
acomplete(andcorrect)proof?
46

<!-- page 47 -->

Answer: [N/A]
Justification: Weintroduceaspatio-temporaldynamictool-usebenchmark. Inourpaper,
the main contributions are the new benchmark and training data rather than theoretical
assumptionandresult.
Guidelines:
• Theanswer[N/A]meansthatthepaperdoesnotincludetheoreticalresults.
• Allthetheorems, formulas, andproofsinthepapershouldbenumberedandcross-
referenced.
• Allassumptionsshouldbeclearlystatedorreferencedinthestatementofanytheorems.
• Theproofscaneitherappearinthemainpaperorthesupplementalmaterial, butif
theyappearinthesupplementalmaterial,theauthorsareencouragedtoprovideashort
proofsketchtoprovideintuition.
• Inversely,anyinformalproofprovidedinthecoreofthepapershouldbecomplemented
byformalproofsprovidedinappendixorsupplementalmaterial.
• TheoremsandLemmasthattheproofreliesuponshouldbeproperlyreferenced.
4. Experimentalresultreproducibility
Question: Doesthepaperfullydisclosealltheinformationneededtoreproducethemainex-
perimentalresultsofthepapertotheextentthatitaffectsthemainclaimsand/orconclusions
ofthepaper(regardlessofwhetherthecodeanddataareprovidedornot)?
Answer: [Yes]
Justification: Weproposealltheexperimentaldetailsincludinghyperparameters,evaluation
settings,trainingdetails,etc,inSection3andAppendixC.2,C.4.
Guidelines:
• Theanswer[N/A]meansthatthepaperdoesnotincludeexperiments.
• Ifthepaperincludesexperiments,a[No]answertothisquestionwillnotbeperceived
well by the reviewers: Making the paper reproducible is important, regardless of
whetherthecodeanddataareprovidedornot.
• Ifthecontributionisadatasetand/ormodel,theauthorsshoulddescribethestepstaken
tomaketheirresultsreproducibleorverifiable.
• Dependingonthecontribution,reproducibilitycanbeaccomplishedinvariousways.
Forexample,ifthecontributionisanovelarchitecture,describingthearchitecturefully
mightsuffice,orifthecontributionisaspecificmodelandempiricalevaluation,itmay
benecessarytoeithermakeitpossibleforotherstoreplicatethemodelwiththesame
dataset,orprovideaccesstothemodel. Ingeneral. releasingcodeanddataisoften
onegoodwaytoaccomplishthis,butreproducibilitycanalsobeprovidedviadetailed
instructionsforhowtoreplicatetheresults,accesstoahostedmodel(e.g.,inthecase
ofalargelanguagemodel),releasingofamodelcheckpoint,orothermeansthatare
appropriatetotheresearchperformed.
• WhileNeurIPSdoesnotrequirereleasingcode,theconferencedoesrequireallsubmis-
sionstoprovidesomereasonableavenueforreproducibility,whichmaydependonthe
natureofthecontribution. Forexample
(a) Ifthecontributionisprimarilyanewalgorithm,thepapershouldmakeitclearhow
toreproducethatalgorithm.
(b) Ifthecontributionisprimarilyanewmodelarchitecture,thepapershoulddescribe
thearchitectureclearlyandfully.
(c) Ifthecontributionisanewmodel(e.g.,alargelanguagemodel),thenthereshould
eitherbeawaytoaccessthismodelforreproducingtheresultsorawaytoreproduce
themodel(e.g.,withanopen-sourcedatasetorinstructionsforhowtoconstruct
thedataset).
(d) We recognize that reproducibility may be tricky in some cases, in which case
authorsarewelcometodescribetheparticularwaytheyprovideforreproducibility.
Inthecaseofclosed-sourcemodels,itmaybethataccesstothemodelislimitedin
someway(e.g.,toregisteredusers),butitshouldbepossibleforotherresearchers
tohavesomepathtoreproducingorverifyingtheresults.
47

<!-- page 48 -->

5. Openaccesstodataandcode
Question: Doesthepaperprovideopenaccesstothedataandcode,withsufficientinstruc-
tionstofaithfullyreproducethemainexperimentalresults,asdescribedinsupplemental
material?
Answer: [Yes]
Justification: Weprovidesourcecodeoftheevaluationandconstructionpipelineandrelease
thebenchmarkdata. WealsoprovidethetrainingdataofSTT-Agent.
Guidelines:
• Theanswer[N/A]meansthatpaperdoesnotincludeexperimentsrequiringcode.
• PleaseseetheNeurIPScodeanddatasubmissionguidelines(https://neurips.cc/
public/guides/CodeSubmissionPolicy)formoredetails.
• Whileweencouragethereleaseofcodeanddata,weunderstandthatthismightnot
bepossible,so[No]isanacceptableanswer. Paperscannotberejectedsimplyfornot
includingcode,unlessthisiscentraltothecontribution(e.g.,foranewopen-source
benchmark).
• Theinstructionsshouldcontaintheexactcommandandenvironmentneededtorunto
reproducetheresults. SeetheNeurIPScodeanddatasubmissionguidelines(https:
//neurips.cc/public/guides/CodeSubmissionPolicy)formoredetails.
• Theauthorsshouldprovideinstructionsondataaccessandpreparation,includinghow
toaccesstherawdata,preprocesseddata,intermediatedata,andgenerateddata,etc.
• Theauthorsshouldprovidescriptstoreproduceallexperimentalresultsforthenew
proposedmethodandbaselines. Ifonlyasubsetofexperimentsarereproducible,they
shouldstatewhichonesareomittedfromthescriptandwhy.
• Atsubmissiontime, topreserveanonymity, theauthorsshouldreleaseanonymized
versions(ifapplicable).
• Providingasmuchinformationaspossibleinsupplementalmaterial(appendedtothe
paper)isrecommended,butincludingURLstodataandcodeispermitted.
6. Experimentalsetting/details
Question: Doesthepaperspecifyallthetrainingandtestdetails(e.g.,datasplits,hyperpa-
rameters,howtheywerechosen,typeofoptimizer)necessarytounderstandtheresults?
Answer: [Yes]
Justification: Inourpaper,weprovideallthetrainingandtestingdetailsinSection3and
AppendixC.2,C.4tomakesurethereproducibleofourevaluationandtrainingresults.
Guidelines:
• Theanswer[N/A]meansthatthepaperdoesnotincludeexperiments.
• Theexperimentalsettingshouldbepresentedinthecoreofthepapertoalevelofdetail
thatisnecessarytoappreciatetheresultsandmakesenseofthem.
• Thefulldetailscanbeprovidedeitherwiththecode,inappendix,orassupplemental
material.
7. Experimentstatisticalsignificance
Question:Doesthepaperreporterrorbarssuitablyandcorrectlydefinedorotherappropriate
informationaboutthestatisticalsignificanceoftheexperiments?
Answer: [Yes]
Justification: WereporttheerrorbarsinourmainresultsasshowninFigure3andTable3.
EachevaluationresultsinSTT-Arenatake3separateruns.
Guidelines:
• Theanswer[N/A]meansthatthepaperdoesnotincludeexperiments.
• Theauthorsshouldanswer[Yes]iftheresultsareaccompaniedbyerrorbars,confidence
intervals,orstatisticalsignificancetests,atleastfortheexperimentsthatsupportthe
mainclaimsofthepaper.
48

<!-- page 49 -->

• Thefactorsofvariabilitythattheerrorbarsarecapturingshouldbeclearlystated(for
example,train/testsplit,initialization,randomdrawingofsomeparameter,oroverall
runwithgivenexperimentalconditions).
• Themethodforcalculatingtheerrorbarsshouldbeexplained(closedformformula,
calltoalibraryfunction,bootstrap,etc.)
• Theassumptionsmadeshouldbegiven(e.g.,Normallydistributederrors).
• Itshouldbeclearwhethertheerrorbaristhestandarddeviationorthestandarderror
ofthemean.
• It is OK to report 1-sigma error bars, but one should state it. The authors should
preferablyreporta2-sigmaerrorbarthanstatethattheyhavea96%CI,ifthehypothesis
ofNormalityoferrorsisnotverified.
• Forasymmetricdistributions,theauthorsshouldbecarefulnottoshowintablesor
figuressymmetricerrorbarsthatwouldyieldresultsthatareoutofrange(e.g.,negative
errorrates).
• Iferrorbarsarereportedintablesorplots,theauthorsshouldexplaininthetexthow
theywerecalculatedandreferencethecorrespondingfiguresortablesinthetext.
8. Experimentscomputeresources
Question: Foreachexperiment,doesthepaperprovidesufficientinformationonthecom-
puterresources(typeofcomputeworkers,memory,timeofexecution)neededtoreproduce
theexperiments?
Answer: [Yes]
Justification: WeprovidesufficientinformationonthecomputerresourcesusedinSFTand
onlineRLinAppendixC.4.
Guidelines:
• Theanswer[N/A]meansthatthepaperdoesnotincludeexperiments.
• ThepapershouldindicatethetypeofcomputeworkersCPUorGPU,internalcluster,
orcloudprovider,includingrelevantmemoryandstorage.
• Thepapershouldprovidetheamountofcomputerequiredforeachoftheindividual
experimentalrunsaswellasestimatethetotalcompute.
• Thepapershoulddisclosewhetherthefullresearchprojectrequiredmorecompute
thantheexperimentsreportedinthepaper(e.g.,preliminaryorfailedexperimentsthat
didn’tmakeitintothepaper).
9. Codeofethics
Question: Doestheresearchconductedinthepaperconform, ineveryrespect, withthe
NeurIPSCodeofEthicshttps://neurips.cc/public/EthicsGuidelines?
Answer: [Yes]
Justification: Theresearchconductedinthepaper,ineveryrespect,iswiththeNeurIPS
CodeofEthics.
Guidelines:
• The answer [N/A] means that the authors have not reviewed the NeurIPS Code of
Ethics.
• Iftheauthorsanswer[No],theyshouldexplainthespecialcircumstancesthatrequirea
deviationfromtheCodeofEthics.
• Theauthorsshouldmakesuretopreserveanonymity(e.g.,ifthereisaspecialconsid-
erationduetolawsorregulationsintheirjurisdiction).
10. Broaderimpacts
Question: Does the paper discuss both potential positive societal impacts and negative
societalimpactsoftheworkperformed?
Answer: [Yes]
Justification: Weprovidethediscussionofpotentialpositiveandnegativesocietalimpacts
ofourworkinAppendixB.
49

<!-- page 50 -->

Guidelines:
• Theanswer[N/A]meansthatthereisnosocietalimpactoftheworkperformed.
• Iftheauthorsanswer[N/A]or[No],theyshouldexplainwhytheirworkhasnosocietal
impactorwhythepaperdoesnotaddresssocietalimpact.
• Examplesofnegativesocietalimpactsincludepotentialmaliciousorunintendeduses
(e.g.,disinformation,generatingfakeprofiles,surveillance),fairnessconsiderations
(e.g.,deploymentoftechnologiesthatcouldmakedecisionsthatunfairlyimpactspecific
groups),privacyconsiderations,andsecurityconsiderations.
• Theconferenceexpectsthatmanypaperswillbefoundationalresearchandnottied
toparticularapplications,letalonedeployments. However,ifthereisadirectpathto
anynegativeapplications,theauthorsshouldpointitout. Forexample,itislegitimate
topointoutthatanimprovementinthequalityofgenerativemodelscouldbeusedto
generateDeepfakesfordisinformation. Ontheotherhand,itisnotneededtopointout
thatagenericalgorithmforoptimizingneuralnetworkscouldenablepeopletotrain
modelsthatgenerateDeepfakesfaster.
• Theauthorsshouldconsiderpossibleharmsthatcouldarisewhenthetechnologyis
being used as intended and functioning correctly, harms that could arise when the
technologyisbeingusedasintendedbutgivesincorrectresults,andharmsfollowing
from(intentionalorunintentional)misuseofthetechnology.
• Iftherearenegativesocietalimpacts,theauthorscouldalsodiscusspossiblemitigation
strategies (e.g., gated release of models, providing defenses in addition to attacks,
mechanismsformonitoringmisuse,mechanismstomonitorhowasystemlearnsfrom
feedbackovertime,improvingtheefficiencyandaccessibilityofML).
11. Safeguards
Question: Doesthepaperdescribesafeguardsthathavebeenputinplaceforresponsible
releaseofdataormodelsthathaveahighriskformisuse(e.g.,pre-trainedlanguagemodels,
imagegenerators,orscrapeddatasets)?
Answer: [N/A]
Justification: Ourworkintroduceanewtool-usebenchmarkandthepaperdoesnotposes
suchrisks.
Guidelines:
• Theanswer[N/A]meansthatthepaperposesnosuchrisks.
• Releasedmodelsthathaveahighriskformisuseordual-useshouldbereleasedwith
necessarysafeguardstoallowforcontrolleduseofthemodel,forexamplebyrequiring
thatusersadheretousageguidelinesorrestrictionstoaccessthemodelorimplementing
safetyfilters.
• DatasetsthathavebeenscrapedfromtheInternetcouldposesafetyrisks. Theauthors
shoulddescribehowtheyavoidedreleasingunsafeimages.
• Werecognizethatprovidingeffectivesafeguardsischallenging,andmanypapersdo
notrequirethis,butweencourageauthorstotakethisintoaccountandmakeabest
faitheffort.
12. Licensesforexistingassets
Question: Arethecreatorsororiginalownersofassets(e.g.,code,data,models),usedin
thepaper,properlycreditedandarethelicenseandtermsofuseexplicitlymentionedand
properlyrespected?
Answer: [Yes]
Justification: All the assets used in our paper including three datasets as seed data are
properlycitedandcredited.
Guidelines:
• Theanswer[N/A]meansthatthepaperdoesnotuseexistingassets.
• Theauthorsshouldcitetheoriginalpaperthatproducedthecodepackageordataset.
• Theauthorsshouldstatewhichversionoftheassetisusedand,ifpossible,includea
URL.
50

<!-- page 51 -->

• Thenameofthelicense(e.g.,CC-BY4.0)shouldbeincludedforeachasset.
• Forscrapeddatafromaparticularsource(e.g.,website),thecopyrightandtermsof
serviceofthatsourceshouldbeprovided.
• If assets are released, the license, copyright information, and terms of use in the
packageshouldbeprovided. Forpopulardatasets,paperswithcode.com/datasets
hascuratedlicensesforsomedatasets. Theirlicensingguidecanhelpdeterminethe
licenseofadataset.
• Forexistingdatasetsthatarere-packaged,boththeoriginallicenseandthelicenseof
thederivedasset(ifithaschanged)shouldbeprovided.
• Ifthisinformationisnotavailableonline,theauthorsareencouragedtoreachoutto
theasset’screators.
13. Newassets
Question:Arenewassetsintroducedinthepaperwelldocumentedandisthedocumentation
providedalongsidetheassets?
Answer: [Yes]
Justification: Weproperlyreleaseourcodeanddatasetsproposedbyourpaper.
Guidelines:
• Theanswer[N/A]meansthatthepaperdoesnotreleasenewassets.
• Researchersshouldcommunicatethedetailsofthedataset/code/modelaspartoftheir
submissions via structured templates. This includes details about training, license,
limitations,etc.
• Thepapershoulddiscusswhetherandhowconsentwasobtainedfrompeoplewhose
assetisused.
• Atsubmissiontime,remembertoanonymizeyourassets(ifapplicable). Youcaneither
createananonymizedURLorincludeananonymizedzipfile.
14. Crowdsourcingandresearchwithhumansubjects
Question: Forcrowdsourcingexperimentsandresearchwithhumansubjects,doesthepaper
includethefulltextofinstructionsgiventoparticipantsandscreenshots,ifapplicable,as
wellasdetailsaboutcompensation(ifany)?
Answer: [N/A]
Justification: Inourpaper,theredoesnotinvolvecrowdsourcingandresearchwithhuman
subjects.
Guidelines:
• Theanswer[N/A]meansthatthepaperdoesnotinvolvecrowdsourcingnorresearch
withhumansubjects.
• Includingthisinformationinthesupplementalmaterialisfine,butifthemaincontribu-
tionofthepaperinvolveshumansubjects,thenasmuchdetailaspossibleshouldbe
includedinthemainpaper.
• AccordingtotheNeurIPSCodeofEthics,workersinvolvedindatacollection,curation,
orotherlaborshouldbepaidatleasttheminimumwageinthecountryofthedata
collector.
15. Institutional review board (IRB) approvals or equivalent for research with human
subjects
Question: Doesthepaperdescribepotentialrisksincurredbystudyparticipants,whether
suchrisksweredisclosedtothesubjects,andwhetherInstitutionalReviewBoard(IRB)
approvals(oranequivalentapproval/reviewbasedontherequirementsofyourcountryor
institution)wereobtained?
Answer: [N/A]
Justification: Inourpaper,theredoesnotinvolvecrowdsourcingandresearchwithhuman
subjects.
Guidelines:
51

<!-- page 52 -->

• Theanswer[N/A]meansthatthepaperdoesnotinvolvecrowdsourcingnorresearch
withhumansubjects.
• Dependingonthecountryinwhichresearchisconducted,IRBapproval(orequivalent)
mayberequiredforanyhumansubjectsresearch. IfyouobtainedIRBapproval,you
shouldclearlystatethisinthepaper.
• Werecognizethattheproceduresforthismayvarysignificantlybetweeninstitutions
andlocations,andweexpectauthorstoadheretotheNeurIPSCodeofEthicsandthe
guidelinesfortheirinstitution.
• Forinitialsubmissions,donotincludeanyinformationthatwouldbreakanonymity(if
applicable),suchastheinstitutionconductingthereview.
16. DeclarationofLLMusage
Question: Does the paper describe the usage of LLMs if it is an important, original, or
non-standardcomponentofthecoremethodsinthisresearch? NotethatiftheLLMisused
onlyforwriting,editing,orformattingpurposesanddoesnotimpactthecoremethodology,
scientificrigor,ororiginalityoftheresearch,declarationisnotrequired.
Answer: [Yes]
Justification: LLMs are used as important components in the core methodology of this
research. Specifically,weemployLLMs(i)asthebackboneofourautomateddatasynthesis
pipelinetogenerateandrefinethebenchmark,SFTtrajectories,andRLtasks,(ii)asthe
usersimulatorduringevaluationonSTT-Arena,and(iii)asthejudgmentmodeltoassess
impossibletasksinSTT-Arena. ThechoiceanddesignoftheLLM-basedcomponentsare
describedindetailinthemainpaperandappendix.
Guidelines:
• Theanswer[N/A]meansthatthecoremethoddevelopmentinthisresearchdoesnot
involveLLMsasanyimportant,original,ornon-standardcomponents.
• PleaserefertoourLLMpolicyintheNeurIPShandbookforwhatshouldorshouldnot
bedescribed.
52
