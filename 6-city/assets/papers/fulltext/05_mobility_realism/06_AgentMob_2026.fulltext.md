# Extracted fulltext (pdfplumber)

Source: https://arxiv.org/abs/2606.05130
<!-- page 1 -->

Towards Efficient and Evidence-grounded Mobility Prediction
with LLM-Driven Agents
LinyaoChen1 QinlaoZhao2 ZechenLi3 MingmingLi1
LikunNi5 JinyuChen1,† YuhaoYao4,†
XuanSong7 NoboruKoshizuka1 HirokiH.Kobayashi1
1TheUniversityofTokyo 2HuazhongUniversityofScienceandTechnology
3UniversityofNewSouthWales,Sydney 4LocationMindInc.
5SouthernUniversityofScienceandTechnology
7JilinUniversity †Correspondingauthors
Abstract
a Deep Neural Network (DNN) Drawbacks
Individual-levelmobilitypredictioniscentral 1. Blackbox Model
to urban simulation, transportation planning, Train Predict H wh a y rd a t o lo i c n a te ti r o p n r e is t
predicted.
andpolicyanalysis. Supervisedsequencemod-
2. Data Deficiency
els achieve strong accuracy but require task- Tra G je P c S tory DNN Model T P r r a e j d e i c c t t o e r d y R la e b q e u le ir d e d s a la ta rg a e n -s d c c a o le stly
retraining.
specific training and offer limited decision-
leveltransparency. RecentLLM-basedmeth- b LLM (Prompt Engineering) Drawbacks
odsimproveinterpretability,yetmostlyrelyon 1. Irreversible Inference
staticpromptsandsingle-passinference,lim- Textualize Convert Predict S w re i i v n th i g s l n e e o . -p c a h s a s n p c r e e d to iction
w iti h n e g n th m e o ir b a il b it i y lity sig to na s l e s ek ar a e d w di e ti a o k na o l r e c v o id n e fl n ic c t e - Tra G je P c S tory T t e r x a t je u c a t l o iz r e y d (Co C M m o e n p m t r e o e x s r t y s ) ed LLM Te lo x c tu a a ti l o iz n ed 2 A co . l l m I e n p v f r o id e r e s m n s c e a e d ti i o i s n n to B a ottleneck
bounded prompt.
ing. We propose AgentMob, a training-free
c Our Method: Agentic Framework Our Advantages
LLM-drivenagentframeworkthatformulates
next-locationpredictionasadaptiveevidence- 1)Individualmobilityknowledge Predict 1. Adaptive Planning
controlled decision making. AgentMob re- Textualize Refine Retrieve F d si e a g e s n t p a - p l r s a e a a th s r e o fo n w r i n e ro g a u k o t / i n c n l o e y n w c fl a i h c s t e e in n s g ; .
solvesroutinecasesthroughafastpathbased Tra G je P c S tory T T e r x a t j u e a c l t i o z r e y d Mo k b n ili o ty w b le e d h g a e vior Te lo x c tu a a ti l o iz n ed 2. Grounded Inference
2) Tool Box Leverages multi-source
onhistoricalregularity,whileambiguouscases m ev o id b e ili n ty c e & f o g r e o re g l r ia a b p l h e ic
... predictions.
t r r ie ig s g , e h r is i t t o e r r i a c t a iv l e be t h o a o v l io u r s , e st o a v y e - r m r o e v c e en li t k t e r l a i j h e o c o to d - , r Mceot o rni b etei v lixt e ytr GIenR ofoe grt rmr a ie pav hteiior cnal SEtsatyim-Maotover Invoke LL A M g -b e a n s t ed 3 I c t r e . o r I s a t s e ti - v r c e a h l e t y i c v g k e a s t h e R e v e r id s f e i a n n n e c d e m , ent
enabling self-correction
andgeographicalevidence.Acrossthreemobil- and better decisions.
3) Urban
itydatasets,AgentMobachievesthestrongest Geographical Knowledge Retrieve
(POIs,Regions Descriptions, etc.)
overallperformanceamongtraining-freeLLM-
basedmethods,withGPT-5.4reaching71.42%
From static prediction to adaptive, evidence-grounded,andIterative inference.
Acc@1onBW,33.14%onYJMob100K,and
33.50%onShanghaiISP.OnBWnon-fast-path Figure1: Comparisonbetweendifferentmobilitypre-
cases, the LLM controller improves Acc@1 diction paradigms. Our method proposes adaptive,
from30.65%to48.62%overasame-toolsta- evidance-groundedanditerativepredictioninatraining-
tisticalbaseline,showingthatitsmainbenefit freemanner,provideseffecientandreliablepredictions.
liesinresolvingambiguouspredictionsthrough
adaptiveevidencegathering. Ourcodeisavail-
andthegeographicalsemanticsofcandidateloca-
ableatAgentMob.
tions.
Existing approaches largely follow two
1 Introduction
paradigms. Supervised sequence models,
Accuratehumanmobilitypredictionisfundamental including RNNs (Feng et al., 2018), Transform-
tourbanplanning(Zhengetal.,2014),transporta- ers(Vaswanietal.,2017),andtheirvariants,learn
tion management (Luca et al., 2021), and public mobility regularities from large-scale trajectory
health analysis (Barbosa et al., 2020). At the in- data and can achieve strong predictive accuracy.
dividual level, next-location prediction supports However, they require task-specific training, are
location-based services (Zheng, 2015), demand- costlytoadapttonewcitiesorspatialgranularities,
awaretransportationsystems,andtargetedpublic and typically provide limited insight into why a
healthinterventions(Oliveretal.,2020). Thecore particularlocationispredicted. RecentLLM-based
challengeistoinferauser’snextspatialstatefrom methods (Zhao et al., 2026; Zhang et al., 2024)
historical trajectories, recent movement context, offeramoreinterpretablealternativebyconverting
1
6202
nuJ
3
]GL.sc[
1v03150.6062:viXra

<!-- page 2 -->

trajectories into text and leveraging language- mobility datasets with different spatial granulari-
model reasoning. Fine-tuning approaches (Feng ties. Experiments show that AgentMob achieves
etal.,2024;Lietal.,2024a)stillinheritsubstantial thestrongestoverallperformanceamongtraining-
trainingcost,whileprompt-basedmethods(Wang freeLLM-basedmethods,whileadditionalanaly-
etal.,2024b;Calderónetal.,2025)avoidretraining ses demonstrate that the LLM controller is most
but compress all available evidence into a static beneficialwhendeterministicmobilitystatisticsare
prompt. Agent-like mobility frameworks (Feng insufficientorconflicting. Insummary,ourcontri-
et al., 2025; Li et al., 2025) introduce structured butionsareasfollows:
memory or reasoning modules, but often rely on
• Adaptiveevidence-controlformulation. We
pre-scripted workflows with limited ability to
recastnext-locationpredictionasaninstance-
adapt the amount and type of evidence used for
leveldecisionprocess,whereanLLMagent
eachprediction.
chooses between a fast historical-regularity
This static prediction paradigm is problematic
pathandadditionalevidencegatheringforam-
since mobility instances are not equally difficult.
biguouscases.
Many cases are routine: a user repeatedly visits
the same location at a similar weekday and hour, • Training-free tool-augmented mobility
so historical regularity may be sufficient. Other agent. We develop AgentMob, which
casesareambiguous: recentmovement,long-term
selectivelyinvokesmobilitytoolsoverrecent
routines,stay–movetendencies,andgeographical
context, historical behavior, stay–move
plausibilitymaypointtodifferentcandidateloca-
likelihood, and geographical evidence to
tions. In such cases, a reliable predictor should
produceauditablepredictiontraces.
notcommitafterasingleforwardpass. Itshould
retrievetargetedevidence,cross-checkconflicting • Strong and explainable training-free per-
signals, and stop once the evidence is sufficient. formance. Across three mobility datasets
Existingprompt-onlyLLMmethodslackthiscapa- and multiple LLM backbones, AgentMob
bilitysincepredictionisperformedthroughafixed achievesthestrongestoverallresultsamong
contextandasinglegenerationstep,withnostruc- training-freeLLM-basedmethods,withanal-
turedmechanismtoverifyorrevisethedecision. ysesshowingthatadaptiveevidencegathering
To address this limitation, we propose Agent- ismostusefulwhenmobilitysignalsconflict.
Mob,atraining-freeagenticframeworkthatformu-
2 RelatedWork
latesnext-locationpredictionasadaptiveevidence-
controlleddecisionmaking. Insteadoftreatingthe Individual Next-Location Prediction. Next-
LLM as a direct trajectory predictor, AgentMob locationpredictionhasevolvedfromMarkov-chain
usesitasacontrollerthatdecideshowmuchevi- and factorization-based methods (Rendle et al.,
denceisneededforeachinstance. Routinecases 2010;Gambsetal.,2012)todeepsequencemodels
exitthroughafastpathbasedonstronghistorical basedonRNNs(Fengetal.,2018;Liuetal.,2016),
regularity,whileambiguouscasestriggeriterative Transformers(Lianetal.,2020; Luoetal.,2021;
tooluseoverrecenttrajectorycontext,historicalbe- Qinetal.,2022;Sunetal.,2024),andGNNs(Wang
havioralstatistics,stay–movelikelihood,geograph- et al., 2024c; Wu et al., 2024). These methods
ical distance, and location semantics. The final learncomplexspatiotemporaldependenciesfrom
predictionisthusgroundedinexplicittooloutputs large-scalemobilitydata,buttypicallyrequiretask-
ratherthanopaqueprompt-onlygeneration. specifictrainingandprovidelimiteddecision-level
As illustrated in Figure 1, AgentMob differs transparency. Recent LLM-based methods con-
from supervised DNNs and prompt-based LLM verttrajectoriesintotextualinputsformobilitypre-
methods in both computation and reasoning. It diction or generation (Wang et al., 2023, 2024a;
doesnotrequiretask-specificmodeltraining,andit Liangetal.,2024);somefine-tuneLLMsforpoint-
avoidsforcingallsamplesthroughthesamefixed of-interest recommendation or trajectory genera-
inference procedure. Instead, it allocates reason- tion (Li et al., 2024a,b), while others integrate
ing effort according to prediction difficulty and memory, urban knowledge, or structured reason-
records timestamp-bounded tool outputs for au- ing modules (Feng et al., 2025; Ju et al., 2025;
ditability. WeevaluateAgentMobwithbothopen- Zhong et al., 2025; Liu et al., 2025). However,
sourceandclosed-sourceLLMbackbonesonthree most existing LLM-based mobility methods still
2

<!-- page 3 -->

followafixedinferenceprocedure,wherehistory polygons or uniform grid cells depending on the
orknowledgeisretrievedinadvance,compressed dataset. Eachspatialunitispairedwithaconcise
intoapromptorscriptedworkflow,andthenused textualdescriptionofitsurbanfunction,allowing
toproduceaprediction. Closelyrelatedagenticmo- the LLM to reason over both trajectory statistics
bilityframeworks,suchasAgentMove(Fengetal., andlocationsemantics. Thepredictiontaskisthen
2025)andARMove(Wangetal.,2026),introduce defined as selecting the spatial unit that the user
structuredmemory,userprofiling,featuremanage- willvisitnext,giventheuserID,targettimestamp,
ment,orfeatureoptimization. Incontrast,Agent- historicaltrajectoryrecords,andtheobservedcon-
Mobtreatsnext-locationpredictionasaninstance- textbeforethetargettime.
levelevidence-controlproblem: theagentdecides
Fast-pathPrediction. AgentMobfirstperforms
whetherasamplecanexitthroughafasthistorical-
a lightweight regularity check before invoking
regularitypath,whichtoolstoinvokeforambigu-
the full tool-calling loop. If the user’s historical
ouscases,andhowtoresolveconflictsamongre-
records show a dominant location for the same
centcontext,historicalbehavior,stay–movelikeli-
weekdayandhour,theagentreturnsthislocation
hood,andgeographicalplausibility.
directly as the prediction. This fast path resolves
LLM-Driven Agents and Evidence-Grounded routinecasesefficientlyandpreventsunnecessary
ToolUse. LLM-drivenagentsextendLMsfrom LLM/toolcomputationwhenthehistoricalsignal
passive text generation to interactive reasoning isalreadystrong.
and action. Prior work has explored instruction-
AdaptiveTool-callingPrediction. Whenstrong
following (Ouyang et al., 2022), multi-agent col-
historical regularity is absent, AgentMob enters
laboration (Li et al., 2023; Wu et al., 2023; Li
the tool-calling mode. The agent invokes tools
et al., 2026), general task automation (Hu et al.,
from the mobility-analysis toolbox described in
2025; Tang et al., 2025), social simulation (Park
Section3.2. Thesetoolsprovidetwocomplemen-
et al., 2023), and tool-augmented problem solv-
tarytypesofevidence: behavioralevidence,such
ing(Nakanoetal.,2021;Qinetal.,2023). These
as recent trajectory context, same-time visitation
studiessuggestthatLLMscancoordinateinterme-
statistics,stay–movelikelihood,andhistoricaltran-
diateevidenceandexternaltools,buttheyarenot
sitionsundersimilarconditions;andgeographical
directlydesignedfornext-locationpredictionunder
evidence, such as distance to candidate locations
spatiotemporaluncertainty. AgentMobinstantiates
and textual descriptions of their urban functions.
evidence-groundedtooluseformobilityprediction,
Based on the evidence collected so far, the agent
where tool invocation is controlled by prediction
mayrequestadditionaltooloutputs,comparecom-
difficulty and each decision is traceable through
peting candidates, or proceed to a final decision.
timestamp-bounded behavioral and geographical
Theloopiscappedatteniterationstoboundinfer-
evidence.
encecost.
3 Methodology
Prediction and Auditability. After evidence
3.1 PipelineofLLM-basedToolAgentfor gathering, the agent outputs a final top-1 predic-
NextLocationPrediction tion together with a ranked top-K candidate list
Figure2illustratestheoverallworkflowofAgent- forrank-basedevaluation. Alltoolinvocationsare
Mob. Weformulatenext-locationpredictionasan constrained to the training split and to observa-
adaptiveevidence-controlprocess,whereanLLM tionsavailablebeforethetargettimestamp,ensur-
agentdecideswhetheratestinstancecanbesolved ing chronological validity. For auditability, each
fromhistoricalregularityorrequiresadditionalevi- prediction trace stores the user ID, target times-
dencefrommobility-analysistools. Theframework tamp,allowedhistoryrange,invokedtools,serial-
is implemented with smolagents (Roucher et al., izedtooloutputs,LLMreasoningsteps,andfinal
2025),butthekeydesignisindependentofaspe- rankedprediction.
cificagentlibrary: theLLMactsasacontrollerthat
3.2 MobilityAnalysisToolbox
selectstools,interpretstheiroutputs,andproduces
arankedpredictionovercandidatespatialunits. Thetoolboxexposescompact,timestamp-bounded
Given raw GPS records, we first discretize co- evidencethattheagentcanselectivelyquery,with
ordinates into spatial units, either administrative each tool summarizing a distinct mobility signal
3

<!-- page 4 -->

Toolbox
Mobility Recent Trajectory
Context
Retriever Historical visitation Statistics
(Too To l o in l v A o g a e c n t t ion) G In e R f o o e g r t r m r a ie p a v h t e i i o c r n a l G Ge eo o g gr ra a p p h h i i c c a a l l D De is s t c a r n ip ce tion co N m n e o t e e r d e xt ? Yes
S E t s a t y im -m a o to v r e Probability of Movement No (LL T M oo In l A fe g r e e n n t ce)
Yes
Historical Enough
Behavior Behavioral statistics on location context?
Retriever
No Iteration: Maximally 10
No
Timestamp Strong
historical
User ID regularity? Yes
Predicted location
Figure2: AgentMobTheworkflowofAgentmob. Thekeyfaetureincludes: 1. fast-pathpredictionforhighly
regularcases2. adaptivetooluseforambiguouscases,andevidence-controlledstoppingbeforefinalprediction3.
Theprimarytoolretrievesmulti-dimensionalinformationforreliableevidence-groundedinference.
instead of passing raw trajectories directly to the evidenceisespeciallyusefulwhenrecentcontinu-
LLM.Together,thesetoolscoverfourcomplemen- ityconflictswithtransition-basedpredictions.
taryaspectsofnext-locationprediction: recentcon-
Historical Behavior Retriever. This tool re-
text, geographical plausibility, stay–move uncer-
trievesbehavioralevidencefrompastvisitstothe
tainty, and historical behavior under comparable
sameornearbylocationsundercomparabletempo-
conditions.
ralcontexts,suchassimilartimeofdayordayof
Mobility Context Retriever. Given a target week. Itsummarizestypicaldwelltimes,frequent
timestamp, this tool summarizes the user’s short- next destinations, transition tendencies, and visit
termmovementcontextandroutinetemporalpat- regularity. The agent uses this evidence to verify
terns. Itreturnstherecentsequenceofvisitedlo- uncertaincandidatesandresolveconflictsamong
cationsoverthepastseveralhours, togetherwith competingmobilitysignals.
visitationstatisticsforthesameweekdayandhour
intheuser’shistoricalrecords. Thisevidencehelps 4 Experiment
theagentdistinguishimmediatemovementconti-
nuityfromlong-termtemporalregularity. 4.1 ExperimentalSetup
Datasets. We evaluate AgentMob on three mo-
GeographicalInformationRetriever. Thistool
bility datasets with different spatial granularities
providesspatialandsemanticevidenceforcandi-
and observation mechanisms. BW (Blogwatcher,
date locations. It returns the distance from the
Inc.,2024)isamobile-phoneGPSdatasetfromthe
currentlocationtoeachcandidate,aswellasacon-
Tokyometropolitanarea,whererawGPSrecords
cise textual description of the candidate’s urban
aremappedtothird-leveladministrativepolygons
function. Thisallowstheagenttocheckwhethera
annotatedwithhierarchicalregionnamesandfunc-
candidateisgeographicallyplausibleandsemanti-
tionaldescriptions. YJMob100K(Yabeetal.,2024)
callyconsistentwiththeuser’smobilitycontext.
is a large-scale mobile-phone GPS dataset dis-
Stay–Move Estimator. This tool estimates cretizedintoanonymized500m×500mgridcells;
whethertheuserismorelikelytoremainatthecur- sincecellsdonothaverealplacenames,wegener-
rentlocationormoveelsewhere. Itcomparesthe atetextualdescriptionsfromtheprovidedPOIcat-
currentstaydurationwithhistoricalstay-duration egorydistributionsusingLLM-basedPOIsumma-
statisticsatthesamelocationandreturnsamove- rization(AppendixB).ForBWandYJMob100K,
mentlikelihoodderivedfrompastbehavior. This we select the 100 most active users and convert
4

<!-- page 5 -->

Statistic BW YJMob100K ShanghaiISP thereciprocalrankofthegroundtruthwithinthe
Records 427,248 310,546 4,944 topfivepredictionsandassignszeroifitisabsent;
Region Tokyo Anonymized Shanghai
Spatialunit Admin.polygons 500mgrids 500mgrids and mean top-1 geographic distance, which mea-
Eval.setting Top-100users Top-100users 200first-testusers
Visitedlocations 4,188polygons 12,430cells 1,385cells surestheHaversinedistanceinkilometersbetween
Move/staytransitions 28.6/71.4% 74.7/25.3% 90.0/10.0%
Avg.uniquelocations 104.8 413.7 10.7 thepredictedandground-truthlocations.
Table1: Datasetstatisticsandevaluationsettings.
4.2 MainResults
PerformanceagainstBaselines. Table2reports
continuoustrajectoriesintospatial-unitsequences
themaincomparisononBW,YJMob100K,andthe
with location descriptions (Table 1). Shanghai
ShanghaiISPfirst-test-pointsetting. TheShanghai
ISP(Fengetal.,2019)isananonymizedmobile-
ISPevaluationfollowsthesame200-userfirst-test
networktrajectorybenchmarkcollectedfrommo-
sampleusedinpriorwork(Fengetal.,2025),and
bilenetworklogsinShanghai,containing325,215
allmethodsareevaluatedunderthesamechrono-
recordsfromApril19to26,2016;followingrecent
logical split within each dataset. Overall, Agent-
LLM-based next-location prediction work (Feng
Mob achieves the strongest performance among
etal.,2025),wediscretizebase-stationcoordinates
training-free LLM-based methods. With GPT-
into500m×500mgridcellsandgeneratetextual
5.4, AgentMob obtains 71.42% Acc@1, 78.84%
descriptionsforeachcell.
MRR@5, and 2.20km distance on BW; 33.14%,
Baselines. WecompareAgentMobwithtwosu- 46.55%,and4.29kmonYJMob100K;and33.50%,
pervised sequence models and four LLM-based 47.44%, and 4.23km on Shanghai ISP. These re-
mobility prediction methods. The supervised sults show that adaptive evidence gathering im-
baselines include DeepMove (Feng et al., 2018), provesLLM-basedmobilitypredictionacrossdif-
an attentional RNN designed to capture peri- ferentspatialgranularitiesandobservationsettings.
odic mobility patterns and long-term user prefer- Compared with supervised baselines, Agent-
ences, and a vanilla Transformer (Vaswani et al., Mob does not always dominate task-specific se-
2017). The LLM-based baselines include Agent- quence models. On BW, Transformer achieves
Move (Feng et al., 2025), which decomposes thebestoverallAcc@1andMRR@5,suggesting
zero-shotpredictionintospatial-temporalmemory, that supervised training remains highly effective
worldknowledge,andcollectivepatternmodules; whensufficientregularmobilitydataareavailable.
LLM-Mob(Wangetal.,2023),whichformulates However, AgentMob with GPT-5.4 outperforms
predictionasin-contextlearningoverstructuredtra- supervisedbaselinesonYJMob100KandShang-
jectoryprompts;TrajLLM(Juetal.,2025),which haiISP,wherethelocationspaceisdenserorthe
convertsmobilitysequencesintotextualrepresen- available history is shorter. This suggests that
tationsforsequentialreasoning;andLLMUrban evidence-grounded LLM reasoning can be com-
Residents(Wangetal.,2024a),whichmodelsin- petitivewithtask-specifictrainingwhencalibrated
dividuals as LLM agents conditioned on activity mobilitystatistics,recentcontext,andlocationse-
patternsandretrieveddailymotivations. ForLLM- manticsprovideusefuldecisionevidence.
basedmethods,weevaluateQwen3-8B(Yangetal., Among LLM-based baselines, GPT-5.4 gener-
2025), GPT-4.1-mini (OpenAI, 2025), and GPT- allyimprovesperformance,butthegainsvaryby
5.4(OpenAI,2026)asbackbones. Allmethodsare methodanddataset. LLMUrbanResidentsremains
evaluatedunderthesamechronologicaltrain/test astrongbaselineonBW,likelybecauseitsactivity-
splitforeachdataset. DeepMoveandTransformer patternmodelingalignswiththestrongertemporal
aretrainedonlyonthetrainingsplit,whileLLM- regularity of this dataset. AgentMove is compet-
basedbaselinesandAgentMobcanaccessthesame itive on YJMob100K, while AgentMob achieves
training-historyrecordsandonlytheobservedcon- better overall ranking and/or spatial accuracy by
textbeforeeachtargettimestampduringinference. explicitlycross-checkingbehavioralandgeograph-
ical evidence. The distance metric is particularly
EvaluationMetrics. Foreachtestinstance,the informative: on YJMob100K and Shanghai ISP,
modeloutputsarankedlistofcandidatelocations. AgentMobavoidsthelargerspatialdriftobserved
Wereportthreemetrics: Acc@1,whichmeasures inseveralprompt-basedorscriptedLLMbaselines.
whether the top-ranked prediction matches the AppendixD.1providesonecaseforeachdataset–
ground-truthlocation;MRR@5,whichcomputes baselinepair,showinghowtheseaggregatediffer-
5

<!-- page 6 -->

Table2: MainperformancecomparisonunderchronologicalevaluationonBW,YJMob100K,andtheShanghaiISP
first-test-pointsetting. Boldmarksthebestresultamongallmethods,andunderliningmarksthebestresultamong
training-freeLLM-basedmethods.
BW YJMob100K ShanghaiISP
Method Backbone
Acc@1↑ MRR@5↑ Dist.↓ Acc@1↑ MRR@5↑ Dist.↓ Acc@1↑ MRR@5↑ Dist.↓
DeepMove 72.13% 78.92% 2.21 31.52% 44.86% 4.86 20.50% 30.00% 6.95
DeepNeuralNetwork
Transformer 73.04% 79.67% 2.18 33.12% 46.12% 4.81 22.00% 32.25% 9.26
GPT-4.1-mini 58.52% 70.16% 3.53 29.25% 41.33% 4.77 26.50% 39.26% 4.78
AgentMove Qwen3-8B 52.58% 64.09% 4.21 29.41% 41.84% 5.36 28.00% 38.48% 5.75
GPT-5.4 64.20% 74.02% 3.07 33.09% 46.51% 4.46 27.00% 39.28% 5.35
GPT-4.1-mini 55.08% 66.10% 3.52 21.38% 35.42% 5.98 33.00% 47.61% 5.22
LLM-Mob Qwen3-8B 56.19% 65.53% 3.45 23.57% 36.50% 5.84 26.50% 40.67% 6.87
GPT-5.4 66.48% 74.84% 2.52 26.20% 39.15% 5.20 29.50% 45.38% 6.44
GPT-4.1-mini 53.08% 64.33% 6.58 24.25% 37.21% 11.57 22.50% 36.30% 7.18
TrajLLM Qwen3-8B 52.58% 64.04% 4.71 28.12% 42.23% 5.16 22.00% 35.00% 6.54
GPT-5.4 62.23% 72.54% 3.48 29.35% 43.20% 4.68 25.00% 39.46% 19.74
GPT-4.1-mini 64.38% 72.89% 2.59 26.59% 40.02% 5.21 32.00% 47.28% 4.23
LLMUrbanRes. Qwen3-8B 58.93% 68.00% 3.29 25.89% 39.51% 5.90 19.5% 24.74% 7.37
GPT-5.4 68.40% 76.36% 2.22 29.36% 42.91% 4.62 31.50% 46.96% 4.45
GPT-4.1-mini 66.30% 76.33% 2.51 31.81% 45.97% 4.25 33.00% 45.48% 4.23
Ours Qwen3-8B 62.65% 74.30% 2.90 30.56% 45.27% 4.39 32.00% 46.78% 4.30
GPT-5.4 71.42% 78.84% 2.20 33.14% 46.55% 4.29 33.50% 47.44% 4.23
As shown in Figure 3, structured mobility statis-
ticsalreadyprovideastrongbaseline,buttheLLM
controllerfurtherimprovesdecisionqualitywhen
evidence needs to be reconciled. On BW, Agent-
Mob improves Acc@1 from 60.05% to 71.42%,
MRR@5from70.48%to78.84%,andreducesdis-
tancefrom3.44kmto2.20km. OnShanghaiISP,
Figure3: EffectoftheLLMcontroller. AGENTMOB- Acc@1 increases from 25.50% to 33.50%, with
STATISTICSusesthesametoolevidenceasAgentMob distancereducedfrom5.86kmto4.23km.
but replaces the LLM controller with a deterministic
The gain is smaller on YJMob100K, where
decisionrule. FullAgentMobusesGPT-5.4.
AGENTMOB-STATISTICS and AgentMob are
nearly tied in Acc@1. This is likely because YJ-
encesappearatthepredictionlevel.
Mob100Kusesanonymizedgridcellswithlimited
ShanghaiISPrevealsametric-specificexception.
semantic cues, and the structured mobility statis-
LLM-MobwithGPT-4.1-miniachievesthehighest
tics already capture much of the predictable rou-
MRR@5,whileAgentMobachieveshigherAcc@1
tine. Nevertheless, AgentMob slightly improves
and lower geographic distance. Since Shanghai
MRR@5andreducesspatialerror,suggestingthat
ISPcontainsonlyeightdaysoftrajectories,several
thecontrollermainlyhelpsavoidworseoff-target
nearbygridscanremainplausibleforagivenuser,
predictionsratherthanchangingmanyexacttop-1
makingtop-K rankingeasierthanselectingtheex-
decisions.
acttop-1location. AgentMobisoptimizedforthe
The benefit of the controller becomes clearer
finalevidence-groundeddecision,whichimproves
on difficult cases. On the BW non-fast-path
top-1 accuracy and spatial error, but does not al-
subset, where strong historical regularity is ab-
waysyieldthemostfavorableorderingamongthe
sent, AgentMob improves Acc@1 from 30.65%
remainingplausiblecandidates. Qualitativetrajec-
to48.62%andMRR@5from46.67%to60.66%
toryvisualizationsareprovidedinAppendixA.
over AGENTMOB-STATISTICS. Thissupportsour
ReasoningProcessAnalysis. Toisolatethecon- central hypothesis: the LLM controller is most
tributionoftheLLMcontrollerfromtheunderly- useful when deterministic mobility statistics are
ingmobilitystatistics,weintroduce AGENTMOB- insufficientandmultipleevidencesourcesmustbe
STATISTICS, a non-LLM baseline that uses the cross-checked.
sametoolevidenceasAgentMobbutreplacesthe Appendix D.1 provides representative traces.
LLMcontrollerwithadeterministicdecisionrule. TheBWfast-pathcaseisresolveddirectlybyaper-
6

<!-- page 7 -->

Dataset Method Fastpath Tools Tokens Wall
/sample /sample (s/sample)
BW LLMUrbanRes. – – 4.15k 2.32
BW AgentMob 62.54% 1.16 6.02k 0.57
YJMob100K AgentMove – – 1.84k 1.53
YJMob100K AgentMob 12.74% 2.66 12.96k 0.77
ShanghaiISP LLMUrbanRes. – – 81.40k 68.77
ShanghaiISP AgentMob 0.00% 1.00 4.82k 2.87
Table 3: Efficiency statistics for GPT-5.4 runs. For
eachdataset,thebaselineisthestrongestGPT-5.4LLM
baselineinTable2. Toolsdenoteevidence-toolcallsin
AgentMobexcludingfinalanswersubmission;tokens
Figure4: Difficulty-stratifiedgainsofAgentMobover includepromptsandresponses;wall-clocktimeismea-
AGENTMOB-STATISTICS on BW and YJMob100K. suredinsecondspersampleundertherecordedworker
ThesamplesizeN isshownundereachsubset. parallelism.
fectlyrepeatedtarget-hourpattern,whiletheother
casesshowAgentMobcorrectingtemptingbaseline exitthroughthefastpath,whileambiguouscases
choicesbycheckinghour-specifictransitions,local receiveadditionaltoolcallsandLLMreasoning.
movementevidence,orcandidate-rankingsignals. OnBW,62.54%ofsamplesareresolvedbythe
These examples support the same mechanism as fastpath,leadingtoonly1.16evidence-toolcalls
theaggregatecontrollerresults: theagentismost per sample and a lower wall-clock time than the
usefulwhenitcancross-checkaplausiblebutweak strongestLLMbaseline. YJMob100Khasweaker
cuebeforecommittingtothefinaltop-1prediction. routineregularity,somoresamplesenterthetool-
callingmodeandtheaveragetokenusageincreases.
Difficulty-stratifiedanalysis. Figure4compares
ShanghaiISPhasnofast-pathexitsbecauseeach
AgentMobwith AGENTMOB-STATISTICS across
usercontributesonlyonesparsefirst-testinstance,
fast-path and harder cases. AgentMob improves
butAgentMobstillreducestokenusageby94.1%
the accuracy of all cases, but the gains are larger
comparedwiththestrongestGPT-5.4baselineby
whendeterministicevidenceisweaker. Theleast
replacinglonghistory-heavypromptswithcompact
gainof+6.58%Acc@1and+4.39%MRR@5ap-
structuredevidence.
pearsonnon-fast-pathcases,themostis+13.09%
These results show that AgentMob is not de-
Acc@1and+9.87%MRR@5underhighconflict
signedtominimizetokenusageuniformlyacross
cases. This indicates the role of the LLM con-
all datasets. Instead, it allocates computation ac-
troller in the system. Highly regular cases can
cordingtopredictiondifficulty. Evenwhensome
oftenberesolvedbystructuredstatistics,whereas
non-fast-path samples require more tool reason-
difficult cases benefit from the evidence analysis
ing,AgentMobachieveslowerobservedwall-clock
and inference by the LLM controller. When de-
time on all three benchmarks under the recorded
terministicregularityisweak,candidatescoresare
workerparallelism. AppendixD.1providesafast-
close,orhistoricalroutinesareunreliable,theLLM
path example where a strong target-hour pattern
controllercancomparetemporal,transition,stay-
allowstheagenttoreturnapredictionwithoutun-
move,andspatialevidencebeforemakingthefinal
necessarytoolloops.
prediction. The effect is also dataset-dependent.
OnYJMob100KandShanghaiISP,wherelocation 4.3 Ablations
informationisanonymizedgridcellandsemantic
Figure 5 reports the effect of removing each evi-
evidenceislimited,theLLMhaslessersemantic
dencesourcefromAgentMob. Overall,nosingle
informationbeyondthestatistics. Asaresult,the
tool dominates all metrics, which is expected be-
metricimprovementofAgentMobisnotsosignifi-
causethetoolstargetdifferenttypesofuncertainty.
cantas AGENTMOB-STATISTICS.
The full model achieves the most stable overall
Efficiency and Cost Analysis. Table 3 reports performance, especially in rank-based accuracy
trace-derivedefficiencystatisticsforGPT-5.4runs. andspatialerror. Someablationscanslightlyim-
Foreachdataset,wecompareAgentMobwiththe proveAcc@1onaspecificdataset,buttheyusually
strongestGPT-5.4LLM-basedbaselineinTable2. worsenMRR@5orgeographicdistance,indicating
Theefficiencybehaviorreflectstheadaptiveallo- thattheremovedevidencehelpspreventspatially
cation strategy of AgentMob: routine cases can pooralternativesevenwhentheexacttop-1label
7

<!-- page 8 -->

Effect of the Location Profiler. The Location
Profilerservesasanoptionalverificationtoolfor
candidate locations. Removing it causes only a
smalldroponBW,from67.57%to67.51%Acc@1,
butaclearerdroponYJMob100K,from32.88%to
32.48%. Thismatchesitsroleinambiguouscases:
ithelpscheckwhetheracandidateisspatiallyplau-
sibleandsemanticallyconsistentbeforetheagent
changesitsdecision. Apairedtraceisprovidedin
Figure5:ToolablationresultswithGPT-5.4onBWand
YJMob100K,reportedbeforedeterministiccalibration AppendixC.
toisolatetheeffectofeachevidencesource. Barsshow
Acc@1,andlinesshowgeographicdistance. SensitivitytothebackboneLLM. AgentMob
also depends on the backbone model’s tool-use
changeslittle.
ability. ComparedwithGPT-4.1-mini,Qwen3-8B
showsweakermulti-toolcoordination: afterenter-
EffectoftheStay–MoveEstimator. Removing
ingtool-callingmode,29.1%ofcasesfailtoinvoke
theStay–MoveEstimatorconsistentlyweakensper-
theStay–MoveEstimatorasprescribed. Sincere-
formance. OnBW,Acc@1dropsfrom67.57%to
liabletooluserequiresinstructionfollowing,API
66.41%, MRR@5 from 76.90% to 76.27%, and
selection,andmulti-stepplanning(Qinetal.,2023),
distance increases from 2.39km to 2.61km. On
smallerorlessalignedmodelsmayrequirestricter
YJMob100K, Acc@1 decreases from 32.88% to
tool-callvalidation,simplifiedorchestration,ordis-
32.47%,withdistanceincreasingfrom4.25kmto
tillation of tool-use behavior. This is consistent
4.36km. This shows that stay–move evidence is
withreportedmodel-scalevariationinQwen3in-
usefulforboundarycaseswhererecentcontinuity
structionfollowing(Yangetal.,2025).
andhistoricaldeparturepatternsdisagree. Apaired
traceisprovidedinAppendixC.
5 ConclusionandFutureWork
Effect of the Historical Behavior Retriever.
The Historical Behavior Retriever provides We presented AgentMob, a training-free LLM-
location-specificevidencesuchasvisitfrequency, agent that formulates next-location prediction as
dwell time, and frequent next destinations. Re- adaptiveevidence-controlleddecisionmaking. In-
moving it reduces BW Acc@1 from 67.57% to stead of relying on static prompt-only inference,
66.67% and increases distance from 2.39km to AgentMoballocatesreasoningeffortaccordingto
2.47km. On YJMob100K, Acc@1 slightly in- prediction difficulty. Routine cases are resolved
creasesfrom32.88%to33.12%,butdistancewors- throughafastpath,whileambiguouscasestrigger
ens from 4.25km to 4.50km. This suggests that selective tool use over recent context, historical
historicalbehaviorevidenceisespeciallyusefulfor behavior,stay–movelikelihood,andgeographical
spatialgrounding: evenwhenexacttop-1accuracy evidence. Experimentsondifferentdatasetsshow
changeslittle,ithelpsavoidfartheroff-targetpre- AgentMob achieves strong training-free perfor-
dictionsindensegridsettings. Additionalcasesare mancewhileproducingauditablepredictiontraces.
showninAppendixC. Further analyses demonstrate that the LLM con-
troller is most useful when deterministic mobil-
EffectoftheMobilityContextRetriever. The
itystatisticsareinsufficientorconflicting. Future
MobilityContextRetrieversuppliesrecenttrajec-
workincludesstrongeruncertaintyestimation,risk-
tory context and same-time historical visitation
aware mobility planning, and broader multi-city
statistics. Removing it causes smaller but con-
transfer.
sistent degradation: BW Acc@1 decreases from
67.57%to67.18%, andYJMob100KAcc@1de- 6 Limitations
creasesfrom32.88%to32.69%,withdistancealso
increasing on both datasets. This indicates that Wediscussseveralscopeboundariesofthecurrent
long-termregularityalreadysolvesmanyroutine studyandhowtheymotivatefutureextensions.
cases,butrecentcontextremainsusefulwhenthe First,AgentMobreliesonthebackboneLLM’s
userhasjustdeparted,returned,orstayedunusually ability to follow tool-use instructions and coor-
long. ApairedtraceisprovidedinAppendixC. dinate multi-step reasoning. This is inherent to
8

<!-- page 9 -->

tool-augmentedagentframeworksratherthanspe- in urban mobility: Integrating llm reasoning into
cifictomobilityprediction. Ourbackboneanaly- multi-agentsimulations. Sensors,25(18):5688.
sisshowsthatstrongerinstruction-followingmod-
JieFeng,YuweiDu,andYongLi.2024. Limp: Large
els can better exploit the evidence-control proto- languagemodelenhancedintent-awaremobilitypre-
col,whilesmallermodelsmayrequireadditional diction. arXivpreprintarXiv:2408.12832.
safeguards. Futureworkcouldimproverobustness
Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. 2025.
throughstrictertool-callvalidation,simplifiedor-
AgentMove: A large language model-based agen-
chestration, or distillation of successful tool-use ticframeworkforzero-shotnextlocationprediction.
tracesintosmallermodels.
JieFeng,YongLi,ChaoZhang,FuningSun,Fanchao
Second,ourevaluationfocusesonautomatically
Meng,AngGuo,andDepengJin.2018. Deepmove:
collected mobility trajectories, including contin-
Predictinghumanmobilitywithattentionalrecurrent
uous GPS datasets and a sparse mobile-network networks. In Proceedings of the 2018 world wide
benchmark. Thischoicematchesourgoalofstudy- webconference,pages1459–1468.
ing next-location prediction under chronological
Jie Feng, Mingyang Zhang, Huandong Wang, Zeyu
constraintsfrompassivelysensedtrajectories. We
Yang,ChaoZhang,YongLi,andDepengJin.2019.
thereforedonotdirectlyevaluateonsocialcheck- DPLink: Useridentitylinkageviadeepneuralnet-
in datasets such as Foursquare, where locations workfromheterogeneousmobilitydata. InProceed-
ingsofthe2019WorldWideWebConference,pages
areactivelyreportedeventsandfollowadifferent
459–469.
observationmechanismfromcontinuoussensing.
ExtendingAgentMobtobridgecheck-indata,con- SébastienGambs,Marc-OlivierKillijian,andMiguel
tinuousGPStraces,andmobile-networkrecordsis NúñezdelPradoCortez.2012. Nextplaceprediction
usingmobilitymarkovchains. InProceedingsofthe
animportantdirectionforbroadergeneralization.
FirstWorkshoponMeasurement,Privacy,andMo-
Finally,thecurrenttoolboxisdesignedaround
bility,MPM’12,NewYork,NY,USA.Association
generalevidencecategoriesformobilityprediction: forComputingMachinery.
recentcontext,historicalbehavior,stay–movelike-
MengkangHu,YuhangZhou,WendongFan,Yuzhou
lihood, and geographical plausibility. Although
Nie, Bowei Xia, Tao Sun, Ziyu Ye, Zhaoxuan Jin,
thesetoolsareeffectiveacrossthestudieddatasets,
YingruLi,QiguangChen,and1others.2025. Owl:
their boundaries and invocation policy are manu- Optimized workforce learning for general multi-
allyspecified. Moresystematicoptimizationoftool agentassistanceinreal-worldtaskautomation. arXiv
preprintarXiv:2505.23885.
designandorchestrationcouldfurtherimproveper-
formance,forexamplethroughautomatedprompt
Chenlu Ju, Jiaxin Liu, Shobhit Sinha, Hao Xue, and
tuning,learnedtool-selectionpolicies,ordynamic Flora Salim. 2025. TrajLLM: A modular LLM-
tool composition. These extensions are comple- enhancedagent-basedframeworkforrealistichuman
trajectorysimulation.
mentary to our core contribution of formulating
mobilitypredictionasadaptiveevidence-controlled
Guohao Li and 1 others. 2023. Camel: Communica-
decisionmaking. tiveagentsfor“mind”explorationoflargelanguage
modelsociety. arXivpreprintarXiv:2303.17760.
7 RiskStatement
PeiboLi,MaartendeRijke,HaoXue,ShuangAo,Yang
Song, and Flora D. Salim. 2024a. Large language
Thecurrenttooldesignisbasedonthecapabilities
models for next point-of-interest recommendation.
of existing LLMs and may become less effective
InProceedingsofthe47thInternationalACMSIGIR
asLLMcapabilitiesevolve. ConferenceonResearchandDevelopmentinInfor-
mation Retrieval, SIGIR 2024, pages 1463–1472.
ACM.
References
QiumengLi,ChunhouJi,andXinyueLiu.2025. From
HugoBarbosa,FernandoB.deLima-Neto,Alexandre narrativetoaction: Ahierarchicalllm-agentframe-
Evsukoff,andRonaldoMenezes.2020. Thescales work for human mobility generation. Preprint,
ofhumanmobility. Nature,586(7831):402–407. arXiv:2510.24802.
Blogwatcher, Inc.2024. Blogwatcher. https://www. SiyuLi,ToanTran,HaowenLin,JohnKrumm,Cyrus
blogwatcher.co.jp/. (Japaneseonly). Shahabi, Lingyi Zhao, Khurram Shafique, and
Li Xiong. 2024b. Geo-llama: Leveraging llms for
ChristianCalderón,PasqualMartí,JaumeJordán,Javier humanmobilitytrajectorygenerationwithspatiotem-
Palanca,andVicenteJulian.2025. Cognitiveagents poralconstraints. arXivpreprintarXiv:2408.13918.
9

<!-- page 10 -->

ZechenLi,BaiyuChen,HaoXue,andFloraD.Salim. JoonSungPark,CarrieO’Brien,CarrieJunCai,Mered-
2026. Zara: Training-freemotiontime-seriesreason- ith Ringel Morris, Percy Liang, and Michael S
ingviaevidence-groundedllmagents. arXivpreprint Bernstein. 2023. Generative agents: Interactive
arXiv:2508.04038. simulacra of human behavior. arXiv preprint
arXiv:2304.03442.
DefuLian,YongjiWu,YongGe,XingXie,andEnhong
Chen.2020. Geography-awaresequentiallocation CanwenQin,AstonZhang,ZhuoshengChen,HengJi,
recommendation. InProceedingsofthe26thACM XiangRen,YizhouSun,and1others.2023. Toolllm:
SIGKDDinternationalconferenceonknowledgedis- Facilitatinglargelanguagemodelstomaster16,000+
covery&datamining,pages2009–2019. real-worldapis. arXivpreprintarXiv:2307.16789.
Yanjun Qin, Yuchen Fang, Haiyong Luo, Fang Zhao,
Yuebing Liang, Yichao Liu, Xiaohan Wang, and
and Chenxing Wang. 2022. Next point-of-interest
Zhan Zhao. 2024. Exploring large language mod-
recommendation with auto-correlation enhanced
els for human mobility prediction under public
multi-modal transformer network. In Proceedings
events. Computers,EnvironmentandUrbanSystems,
ofthe45thInternationalACMSIGIRConferenceon
112:102153.
ResearchandDevelopmentinInformationRetrieval,
pages2612–2616.
QiLiu,CanLi,andWanjingMa.2025. Gatsim: Urban
mobility simulation with generative agents. arXiv
Steffen Rendle, Christoph Freudenthaler, and Lars
preprintarXiv:2506.23306.
Schmidt-Thieme. 2010. Factorizing personalized
markovchainsfornext-basketrecommendation. In
QiangLiu,ShuWu,LiangWang,andTieniuTan.2016.
Proceedingsofthe19thinternationalconferenceon
Predictingthenextlocation: arecurrentmodelwith
Worldwideweb,pages811–820.
spatialandtemporalcontexts. InProceedingsofthe
ThirtiethAAAIConferenceonArtificialIntelligence, AymericRoucher,AlbertVillanovadelMoral,Thomas
AAAI’16,pages194–200.AAAIPress. Wolf, Leandro von Werra, and Erik Kaunismäki.
2025. ‘smolagents‘: a smol library to build
MassimilianoLuca,GianniBarlacchi,BrunoLepri,and great agentic systems. https://github.com/
Luca Pappalardo. 2021. A survey on deep learn- huggingface/smolagents.
ingforhumanmobility. ACMComputingSurveys,
55(1):1–44. TianaoSun,KeFu,WeimingHuang,KaiZhao,Yong-
shunGong,andMengChen.2024. Goingwhere,by
Yingtao Luo, Qiang Liu, and Zhaocheng Liu. 2021. whom, and at what time: Next location prediction
Stan: Spatio-temporalattentionnetworkfornextlo- considering user preference and temporal regular-
cationrecommendation. InProceedingsoftheweb ity. InProceedingsofthe30thACMSIGKDDCon-
conference2021,pages2177–2185. ferenceonKnowledgeDiscoveryandDataMining,
pages2784–2793.
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Karl
Cobbe,LianeDao,MatthewJones,NicholasKornis, Y.Tangand1others.2025. Agent-kb: Knowledgebase
VladMalaya,KathrynMillican,PamelaMishkin,and enhancedmulti-agentcollaborationforcomplextask
1others.2021. Webgpt: Browser-assistedquestion- solving. arXivpreprintarXiv:2507.06229.
answering with human feedback. arXiv preprint
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
arXiv:2112.09332.
Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz
Kaiser,andIlliaPolosukhin.2017. Attentionisall
NuriaOliver,BrunoLepri,HaraldSterly,and1others.
youneed. InAdvancesinNeuralInformationPro-
2020. Mobilephonedataforinformingpublichealth
cessingSystems(NeurIPS),volume30.
actions across the COVID-19 pandemic life cycle.
ScienceAdvances,6(23):eabc0764.
Chuyue Wang, Jie Feng, Yuxi Wu, Shenglin Yi, and
HangZhang.2026. ARMove: Learningtopredict
OpenAI.2025. Gpt-4.1-mini: Acompactandefficient
humanmobilitythroughagenticreasoning. Preprint,
largelanguagemodel. https://openai.com/. Ac-
arXiv:2604.17419.
cessed: 2026-03-16.
Jiawei Wang, Renhe Jiang, Chuang Yang, Zengqing
OpenAI. 2026. Introducing GPT-5.4. https:// Wu,MakotoOnizuka,RyosukeShibasaki,Noboru
openai.com/index/introducing-gpt-5-4/. Ac- Koshizuka,andChuanXiao.2024a. Largelanguage
cessed: 2026-05-24. modelsasurbanresidents: Anllmagentframework
forpersonalmobilitygeneration. AdvancesinNeural
LongOuyang,JeffWu,XuJiang,DiogoAlmeida,Car- InformationProcessingSystems,37:124547–124574.
rollLWainwright,PamelaMishkin,ChongZhang,
SandhiniAgarwal, KatarinaSlama, AlexRay, and Xinglei Wang, Meng Fang, Zichao Zeng, and Tao
1others.2022. Traininglanguagemodelstofollow Cheng. 2023. Where would i go next? large lan-
instructions with human feedback. arXiv preprint guagemodelsashumanmobilitypredictors. arXiv
arXiv:2203.02155. preprintarXiv:2308.15197.
10

<!-- page 11 -->

Xinglei Wang, Meng Fang, Zichao Zeng, and Tao Toolbox
Cheng. 2024b. Where would i go next? large lan- R MCeoo trnb ite ilev itxe ytr R H e is c t e o n ri t c T a r l a v je is c it t a o t r i y on Statistics
g
pr
u
e
a
p
g
r
e
in
m
ta
o
r
d
X
el
i
s
v:
a
2
s
3
h
0
u
8.
m
15
a
1
n
9
m
7.
obilitypredictors. arXiv (TooTol oinlv Aogaecnttion) GIne Rfooe grt rmr a
ie
pav hteiioc rna l G
Ge
eo
o
g
gr
ra
a
p
p
h
h
i
i
c
c
a
a
l
l
D
De
is
s
t
c
a
r
n
ip
ce
tion co
N m
n
e o
t
e
e
r d e
xt ?
Yes
SEtsatyim-maotovre Probability of Movement No (LLTMoo Inl Afegreenntce)
Yu Wang, Tongya Zheng, Shunyu Liu, Zunlei Feng,
KaixuanChen,YunzhiHao,andMingliSong.2024c. H RBi ees tht r oaie rvi v cioe arr l Behavioral statistics on location c E o n n o t u e g xt h ? Yes
Spatiotemporal-augmented graph neural networks No Iteration: Maximally 10 No
forhumanmobilitysimulation. IEEETransactions Timestamp hi S s t t r o o r n ic g a l
User ID regularity? Yes
onKnowledgeandDataEngineering,36(11):7074– Predicted location
7086.
Figure 6: Part of predictions for a sample user. (a)
Groundtruth(b)Ourmethod(c-e)Baselines.
Jiaman Wu, Shangqing Cao, Giuseppe Perona, and
MartaCGonzalez.2024. Imitatetherightdata: City-
wide mobility generation with graph learning. In
A QualitativeTrajectoryVisualization
Proceedingsofthe32ndACMInternationalConfer-
ence on Advances in Geographic Information Sys-
B LocationDescriptionprediction
tems,pages609–612.
Since raw GPS coordinates and anonymous cell
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran
IDs carry no semantic information, we design a
Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang, Shaokun Zhang, Jiale Liu, and 1 others. description-predictionstepthatconvertseachspa-
2023. Autogen: Enabling next-gen llm applica- tialunitintoaconcisetextualcharacterization,en-
tions via multi-agent conversation. arXiv preprint
abling the LLM to reason about locations based
arXiv:2308.08155.
ontheirfunctionalroles. Alldescriptionsaregen-
TakahiroYabe,KotaTsubouchi,ToruShimizu,Yoshi- eratedoncewithGPT-4oandsharedacrossevery
hide Sekimoto, Kaoru Sezaki, Esteban Moro, and LLM-basedmethodevaluatedinthispaper.
Alex Pentland. 2024. Yjmob100k: City-scale and
longitudinaldatasetofanonymizedhumanmobility BW. Each polygon corresponds to a third-level
trajectories. ScientificData,11(1):397. administrativeunitandisidentifiedbyahierarchi-
calplacename(prefecture/municipality/district,
AnYang,AnfengLi,BaosongYang,BeichenZhang,
e.g.,To¯kyo¯-to,Itabashi-ku,Hasune). Weretrieve
BinyuanHui,BoZheng,andOthers.2025. Qwen3
technicalreport. Preprint,arXiv:2505.09388. publiclyavailablegeographicinformationforeach
placenameandpromptGPT-4otoproduceaone-
Peiyuan Zhang, Guangtao Zeng, Tianduo Wang, and
sentence functional summary. For example, the
Wei Lu. 2024. Tinyllama: An open-source small
polygonTo¯kyo¯-to,Itabashi-ku,Hasuneyields:
languagemodel. Preprint,arXiv:2401.02385.
“Itfunctionsprimarilyasaquietresidentialneigh-
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, borhood,wheretheareaischaracterizedbyapart-
XiaoleiWang,YupengHou,YingqianMin,Beichen ment complexes, small parks, and local conve-
Zhang,JunjieZhang,ZicanDong,YifanDu,Chen niencestores,withnearbytransitaccessviaHa-
Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang, suneStationontheMitaLine.”
RuiyangRen,YifanLi,XinyuTang,ZikangLiu,and
3others.2026. Asurveyoflargelanguagemodels. YJMob100K. Cells are anonymized
Preprint,arXiv:2303.18223. 500m×500m grid squares with no place
names. WeleveragethePOIcategoryvectors(85
YuZheng.2015. Trajectorydatamining: Anoverview.
categories)providedbythedatasetauthors(Yabe
ACMTransactionsonIntelligentSystemsandTech-
et al., 2024), and prompt GPT-4o to summarize
nology,6(3):1–41.
each cell’s top POI categories and their relative
YuZheng, LiciaCapra, OuriWolfson, andHaiYang. proportions into a one-sentence description. For
2014. Urbancomputing: concepts,methodologies,
example, a cell whose top categories are Hair
andapplications. ACMTransactionsonIntelligent
Salon(8.3%),TransitStation(7.4%),andHospital
SystemsandTechnology,5(3):1–55.
(7.0%)yields:
Lin Zhong, Lingzhi Wang, Xu Yang, and Qing Liao.
“Itfunctionsprimarilyasadiversemixed-useser-
2025. Comapoi: Acollaborativemulti-agentframe-
vicearea,wherethemappedprofileisledbymany
workfornextpoipredictionbridgingthegapbetween
hairsalonsalongsidemanytransitstationsand
trajectoryandlanguage. InProceedingsofthe48th
manyhospitals,withadjacentcellsindicatinga
InternationalACMSIGIRConferenceonResearch moreactive,service-richamenitylandscapeand
and Development in Information Retrieval, pages nosingleactivityclearlydominatingtheamenity
1768–1778. mix.”
11

<!-- page 12 -->

C AblationCaseExamples “Although the current-location stay sig-
nal is strong, the strongest Tier-1 evi-
Stay-move Estimator. For user
dence is the past same Thursday 07:00
fef58e6c6288Bad60f5629111c489116 at
example and the weekly 07:00 pattern,
2023-06-16 07:00 in BW, the no-stay-move
both pointing to 35995. Because this
ablation predicts 76620, while the full method
isacommutewindowandthedominant
predicts the ground-truth location 17833. The
day+hourlocationdiffersfromthecur-
pairedtracesshowwhytheStay-moveEstimator
rentlocation,Ioverridetherank-1can-
matters.
didateandpredict35995.”
No-stay-moveablationtrace
“The user has stayed at 76620 for the Full-methodtrace
last five hours, transition continuation
“Recent Trajectory (last 6): 2023-05-
fromthecurrentlocationstronglyfavors
25T01:00:00: ID 60203 ... 2023-05-
remainingat76620(88.4%),andthetop
25T06:00:00: ID 60203. Last 4 hours:
compositescoreisalso76620. Although
ID60203→60203→60203→60203
theFriday07:00historicalsignalpoints
(stable).”
to 17833, it is based on only one prior
instance and is weaker than the strong
“AlthoughpastThursday07:00examples
currentstay/transitionevidence.”
favor35995,theuserhasbeensettledat
Full-methodtrace 60203for7hours,currentstaymatches
thehistoricalaverage,andbothoverall
“Average stay: 8.6h. Current stay:
and 07:00-specific transitions strongly
5h (0.58x average). Typical departure
favorremainingat60203. Giventhesta-
hours: 7:00. Currenthour7:00matches
ble overnight trajectory and 78% self-
a typical departure hour. Transitions
transition at07:00, staying at60203 is
at 07:00 from Location 76620: 17833:
themostlikelyoutcome.”
64%;76620(stay): 24%.”
“Although76620isthetoprawcandidate, Thiscasesupportstheablationresult: withoutre-
multiplestrongermovesignalspointto centtrajectory,theagentfollowsthesameweekday-
17833: 07:00isatypicaldeparturehour hourmemory;withtheMobilityContextRetriever,
from 76620, hour-specific transitions itseesthattheuserisinastablelocalcontinuation
from 76620 go to 17833 64% vs only state.
24%stay,andtheonlypastFriday07:00
Historical Behavior Retriever. For user
example is also 17833. These aligned
b1774dafe8Ba1caac3e7aeb1b2b001d4 at 2023-
commute-timesignalsjustifyoverriding
06-21 13:00 in BW, the no-retriever ablation
therank-1staycandidate.”
predicts33524,whilethefullmethodpredictsthe
Thiscasesupportstheaggregateablationresult: ground-truth location 96817. The paired traces
without the Stay-move Estimator, the agent over- showthattheHistoricalBehaviorRetrieverhelps
weightsrecentcontinuity;withtheestimator,itcan the agent audit whether a sparse historical signal
identifydeparture-boundarycaseswheretheuser correspondstoatrulyvisitedlocation.
islikelytomovedespiteseveralrecenthoursatthe No-retrieverablationtrace
samelocation.
“The strongest signal is the Wednesday
Mobility Context Retriever. For user
13:00historicalpattern,whereID33524
ed1fedcdf0c95e6748f68ee552aba4d2 at
accountsfor50.0%ofpastinstancesand
2023-05-2507:00inBW,theno-recent-trajectory
alsoreceivesthestrongestinitialsupport.
ablation predicts 35995, while the full method
Current-location stay evidence is weak
predicts the ground-truth location 60203. The
withnotransitionordurationhistoryfor
pairedtracesshowthatrecentcontextpreventsthe
96817,sothedominantsame-day/hour
agentfromoverreactingtoasparseweekday-hour
patternshouldoverridestayingnearby.”
pattern.
No-recent-trajectoryablationtrace Full-methodtrace
12

<!-- page 13 -->

“Location Details: 96818. Visit fre- continuation/self-transition to 37601 is
quency: 0.00%(0visits).” thesafestprediction.”
“ThestrongWednesday13:00historical Thiscasesupportstheablationresult: optional
signalpointsto96818,butthatlocation profilingisnotneededforeverysample,butithelps
isnotinthecandidatelistandshowsno inambiguouscasesbycheckingwhetheratempt-
visit history in the details lookup. With ing alternative is supported by concrete location-
no transition data from 96817 and the levelevidence.
useronlyhavingstayedthere1houraf-
D InferenceCaseStudies
ter local movement, I choose the only
plausible nearby visited continuation D.1 Baseline-by-DatasetComparisonCases
amongcandidates: remainingatcurrent
Thissectiongivesonerepresentativecomparison
location 96817, though with low confi-
foreachdataset-baselinepair. Eachcasereportsthe
dence.”
groundtruth,AgentMob’sprediction,andthebase-
line’s top-ranked prediction, followed by a short
This case supports the ablation result: with-
explanationofthedecisiondifference.
outtheretriever,theagentfollowsacoarsesame-
day/hourpattern;withtheretriever,itcancheckthe BW–AgentMove.
visitation evidence behind that pattern and avoid Dataset: BW
trustinganunsupportedhistoricalcandidate. Groundtruth: 36166
Ours: correct
Location Profiler. For user
AgentMove: wrong(17844rankedfirst)
5c6fe37f6005d3aeb4e3062f44bb32d3 at
2023-06-01 12:00 in BW, the no-optional-tools Oursinference
ablation predicts 55472, while the full method Thepredictionismadedirectlythroughthefast-
predicts the ground-truth location 37601. The pathmechanism. Thetemporalevidenceshows
aperfectlyrepeatedpattern: onFridayat09:00,
pairedtracesshowthattheLocationProfilerhelps
the user was at location 36166 in 18 out of 18
theagentrejectanunsupportedhistoricaloverride historicalinstances.Sincetheday-hourpatternis
beforeleavingastablecurrentlocation. fullyconsistent,themodelcanconfidentlyrelyon
thisstructuredtemporalsignalwithoutinvoking
No-optional-toolsablationtrace
additionaltools.
“The user has been stationary at 37601 AgentMoveinference
for24hours,butthisfarexceedsthehis-
The user’s most visited location is 17844 with
torical average stay and matches typi- a high overall visit rate and a significant pres-
enceintheirlong-termhistory,indicatingastrong
cal departure timing, so move signals
likelihood to return especially during weekday
are strong. Among plausible move des- mornings.
tinations, 55472 has the highest com- ...36166...isrankedthird.
posite score and is strongly supported BW–LLM-Mob.
byhourlyandoverallvisitationpatterns, Dataset: BW
whiletheThursday-12:00historicalsig- Groundtruth: 84174
nal for 66619 is based on only one in- Ours: correct
stanceandisnotinthecandidateset.” LLM-Mob: wrong(60263rankedfirst)
Full-methodtrace Oursinference
Thecandidaterankingstepcorrectedtheinitial
“Location Details: 66619. Visit fre-
prediction and selected 84174. Although sev-
quency: 0.00%(0visits).” eral overnight locations were plausible, the fi-
nalevidence-supportedcandidatewastheground-
“Despite the top composite score for truthlocation.
55472, the user has remained at 37601
LLM-Mobinference
for 24 hours with a settled pattern and
LLM-MobemphasizedtheWednesday01:00his-
allrecenthoursunchanged. Thestrong toricalpatternandtheimmediatelyprecedingtra-
Thursday-12:00signalpointsto66619, jectory,ranking60263firstbecauseitappeared
tomatchovernightbehavior.Ittreated84174asa
but that location has 0 recorded vis-
laterearly-morninglocationandrankeditbelow
its and is not a valid candidate, so thetopcandidates.
13

<!-- page 14 -->

BW–LLMUrbanResidents. YJMob100K–LLMUrbanResidents.
Dataset: BW Dataset: YJMob100K
Groundtruth: 4419 Groundtruth: (169,126)
Ours: correct Ours: correct
LLM Urban Residents: wrong (76623 ranked LLMUrbanResidents: wrong((138,89)ranked
first) first)
Oursinference Oursinference
AgentMobusedthehour-specifictransitionev-
The candidate ranking step selected (169,126),
idencetomoveawayfromtheinitialcandidate
preserving the evidence for the current work-
andselected4419.Thedecisionfollowsthelocal
related location rather than extrapolating from
early-morningevidenceratherthanthebroader
thelatestmovementcluster.
persona-levelroutine.
LLMUrbanResidentsinference
LLMUrbanResidentsinference
LLM Urban Residents emphasized a week- LLMUrbanResidentsreliedontherecentmove-
endovernightmovementpatternandtheuser’s mentwithinthe(138,88)–(139,88)clusteranda
broaderactivitypersona,ranking76623firstasa factory-workerpersona,ranking(138,89)firstas
likelyearly-morningreturnlocation.Theground- alikelycontinuation.Theground-truthlocation
truthlocation4419waskeptasalower-ranked wasincludedonlyasalower-rankedalternative.
recentstop.
ShanghaiISP–AgentMove.
YJMob100K–AgentMove.
Dataset: ShanghaiISP
Dataset: YJMob100K
Groundtruth: (138,114)
Groundtruth: (134,83)
Ours: correct
Ours: correct
AgentMove: wrong((129,121)rankedfirst)
AgentMove: wrong((155,106)rankedfirst)
Oursinference
Oursinference
AgentMobkeptthebaseprediction(138,114),in-
Thecandidaterankingstepselected(134,83)af-
dicatingthattheavailableevidencedidnotjustify
tercomparingtheimmediatecandidateevidence.
movingtoafartherhistoricalanchorinthissparse
Thispreventsthepredictionfromcollapsingtoa
first-testsetting.
distantlong-termanchorwhenthecurrentsample
favorsadifferentlocation.
AgentMoveinference
AgentMoveinference
AgentMoveemphasizedtheuser’soverallprefer-
AgentMoveprioritizedtheuser’sdominantlong- encefor(129,121)andfrequenttransitionsaround
termanchor(155,106),whichaccountsforalarge thatarea. Thislong-termanchordominatedits
shareofvisitsandhasstrongself-transitionbe- prediction, even though the target remained at
havior.Thisbroadroutinesignaloutweighedthe (138,114).
sample-specificevidencefor(134,83).
ShanghaiISP–LLM-Mob.
YJMob100K–LLM-Mob.
Dataset: ShanghaiISP
Dataset: YJMob100K
Groundtruth: (92,105)
Groundtruth: (107,75)
Ours: correct
Ours: correct
LLM-Mob: wrong((71,91)rankedfirst)
LLM-Mob: wrong((98,78)rankedfirst)
Oursinference
Oursinference
AgentMobusedhour-transitioncalibrationtore-
AgentMobcorrectedtheinitialnearbycandidate
visethebasepredictionfrom(71,91)to(92,105).
andselected(107,75). Thefinaldecisionstays
Thefinalanswerfavorsthetarget-timeevidence
withinthecurrentlocalmovementcorridorrather
overarepeatedbutlessreliablerecentmorning
thanfollowingarepeatedafternoonpatternfrom
pattern.
anothergridcluster.
LLM-Mobinference LLM-Mobinference
LLM-Mobemphasizedarepeatedhistoricalpat- LLM-Mobranked(71,91)firstbecausetheuser
ternaround(98,78),rankingthatlocationfirst.It appearedthereat08:00ontworecentdays.Itstill
consideredthe107-clusterplausiblebutplacedit ranked(92,105)second,butdidnotelevateitto
belowthestrongerroutinesignal. thefinaltop-1prediction.
14

<!-- page 15 -->

ShanghaiISP–LLMUrbanResidents.
Dataset: ShanghaiISP
Groundtruth: (125,108)
Ours: correct
LLMUrbanResidents: wrong((126,107)ranked
first)
Oursinference
AgentMobusedhour-transitioncalibrationtose-
lect(125,108)insteadoftheneighboringmorning
anchor (126,107). The correction is small spa-
tiallybutchangestheexacttop-1label.
LLMUrbanResidentsinference
LLMUrbanResidentsranked(126,107)firstbe-
causeitwasaregular08:00locationacrossrecent
similardays.Itplaced(125,108)second,showing
thatthebaselineidentifiedtherightlocalareabut
missedtheexactgrid.
15
