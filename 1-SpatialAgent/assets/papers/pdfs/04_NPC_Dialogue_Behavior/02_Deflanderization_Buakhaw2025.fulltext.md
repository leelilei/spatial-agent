Title: Deflanderization for Game Dialogue: Balancing Character Authenticity with Task Execution in LLM-based NPCs

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/04_NPC_Dialogue_Behavior/02_Deflanderization_Buakhaw2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:06:58+00:00
- page_count: 16
- status: ok
- text_char_count: 47508

Metadata:
- author: Pasin Buakhaw; Kun Kerdthaisong; Phuree Phenhiran; Pitikorn Khlaisamniang; Supasate Vorathammathorn; Piyalitt Ittichaiwong; Nutchanon Yongsatianchot
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Related Work (page 3)
  - Agents for Game-Oriented Dialogue (page 3)
  - Tool calling (page 3)
- Competition Overview (page 3)
  - Competition Tasks (page 3)
    - Task 1: Task-Oriented Dialogue Agents (page 3)
    - Task 2: Context-Aware Dialogue Agents (page 3)
- Competition Tracks (page 4)
  - API Track (page 4)
  - GPU Track (page 4)
- Results (page 5)
  - API Track (page 5)
- Discussion (page 6)
- Appendix (page 6)
- Exploratory Data Analysis (page 9)
- Evaluation Metrics (page 9)
  - Task 1 (page 9)
    - Function name exact match (page 9)
    - Function argument exact match (page 9)
    - BERTScore (page 10)
  - Task 2 (page 10)
    - BLEU-4 (page 10)
    - Word-level F1 (page 10)
    - CPDCscore (page 10)
- Prompts (page 10)
  - Additional Data Generation (page 10)
  - FewShot (page 11)
  - Chain of Thought (page 12)
  - Deflanderization (page 12)
  - Most word (page 12)
  - Guide (page 13)
- Compute Constraints (page 14)
- Additional Results (page 14)
  - Supervised Fine-Tuning (SFT) (page 14)
  - LoRA (page 14)
  - GRPO Tuning on Reasoning Data (page 14)
  - Inference with vLLM and LoRA Adapters (page 15)
- Final Leader Board (page 15)

Markdown Content:

Deflanderization for Game Dialogue: Balancing Character Authenticity
with Task Execution in LLM-based NPCs
PasinBuakhaw1*,KunKerdthaisong2*,PhureePhenhiran2*,PitikornKhlaisamniang3,
SupasateVorathammathorn3,PiyalittIttichaiwong4,5†,NutchanonYongsatianchot2†
1DepartmentofComputerEngineeringandDigitalTechnology,FacultyofEngineering,ChulalongkornUniversity
2FacultyofEngineering,ThammasatSchoolofEngineering,ThammasatUniversity
3ArtificialIntelligenceAssociationofThailand
4SchoolofBiomedicalEngineering&ImagingSciences,King’sCollegeLondon
5SirirajInformaticsandDataInnovationCenter(SIData+),FacultyofMedicine,SirirajHospital,MahidolUniversity
Abstract patterns (Salemietal.,2023). Thesepersonaliza-
tionsystemsleverageuser-specificinformationto
The emergence of large language models providetailoredresponses,recommendations,and
(LLMs)hasopenednewopportunitiesforcre-
interactions. Forexample,LaMP(LargeLanguage
ating dynamic non-player characters (NPCs)
ModelsMeetPersonalization)introducescompre-
in gaming environments, enabling both func-
hensive benchmarks for evaluating personalized
tional task execution and persona-consistent
textgeneration (Salemietal.,2023),whileanother
dialogue generation. In this paper, we
(TU_Character_lab)reportourparticipation work explores personalized dialogue agents that
intheCommonsensePersona-GroundedDia- maintainconsistentuserpreferencesacrossconver-
logueChallenge(CPDC)2025Round2,which sations (Zhangetal.,2018).
evaluates agents across three tracks: task-
Second,environmentadaptationinvolvesLLMs
orienteddialogue,context-awaredialogue,and
taskedwithmaintainingconsistentpersonaswithin
their integration. Our approach combines
specific contexts, commonly referred to as role-
twocomplementarystrategies: (i)lightweight
playing. Thisapproachhasgainedsignificanttrac-
promptingtechniquesintheAPItrack,includ-
ingaDeflanderizationpromptingmethodto tionin multi-agentsystems whereLLMs assume
suppressexcessiverole-playandimprovetask distinctprofessionalroles. ChatDev (Qianetal.,
fidelity,and(ii)fine-tunedlargemodelsinthe 2023)exemplifiesthisparadigmbycreatingavir-
GPUtrack,leveragingQwen3-14Bwithsuper-
tualsoftwaredevelopmentcompanywherediffer-
visedfinetuning(SFT)andLow-RankAdapta-
ent agents handle specialized tasks such as pro-
tion(LoRA).Ourbestsubmissionsranked2nd
gramming,testing,anddocumentation. Similarly,
onTask1,2nd onTask3(APItrack),and4th
MetaGPT (Hong et al., 2023) proposes a meta-
onTask3(GPUtrack).
programming framework for collaborative multi-
1 Introduction agentworkflows,whileGenerativeAgents (Park
etal.,2023)demonstratesbelievablehumanbehav-
Therevolutionoflargelanguagemodels(LLMs) ior simulation through persistent agent personas.
hasdemonstratedthattransformerarchitecturescan Advanced frameworks like CAMEL (Li et al.,
engageinhuman-likedialogueinteractionswithin 2023) and Voyager (Wang et al., 2023) further
virtual environments. Recent studies have cate- explorehowrole-playingagentscanengageincom-
gorized persona-enabled LLMs into two distinct plexproblem-solvingandopen-endedexploration
adaptationapproaches: user-focusedpersonaliza- tasks.
tion and environment-based role-playing (Tseng
These developments showcase the remarkable
etal.,2024).
abilityofmodernLLMstofacilitateandembody
First, user persona-LLMs are designed as given personas, with applications spanning from
purpose-built assistants that adapt to individual personalizeduserassistancetosophisticatedmulti-
users’ preferences, backgrounds, and behavioral agentcollaborationsinvirtualenvironments (Jiang
etal.,2022).
*Equalcontribution.
†Correspondingauthors. DespitetherapidgrowthofLLMresearch,the
5202
tcO
62
]LC.sc[
3v68531.0152:viXra

tionships. Collaborativequestcompletionsystems
in Minecraft showcase how LLM-driven NPCs
canworkalongsidehumanplayerstoaccomplish
sharedobjectives (Raoetal.,2024),whilefunction-
calling capabilities enable AI Game Masters or
NPCs to manage complex game mechanics and
narrativeprogression(Songetal.,2024a). Further-
more, specialized datasets like MCPDial (Alavi
et al., 2024) and PeaCoK (Gao et al., 2023) pro-
viderichpersona-drivendialoguecollectionsthat
enhance the authenticity and depth of NPC inter-
actions, supporting the development of more so-
Figure1: Examplesofplayer–NPCinteractionsusing
phisticatedconversationalagentsingamingenvi-
LLM-basedagentsintheCPDC2025competition,Top
ronments.
panel: EarlySummer7PM,clearnightattheWeapon
Thegrowinginterestinpersona-groundedgam-
Shop,showinganexampleofuser-NPCinteractionin
ingapplicationshasculminatedinorganizedinitia-
Task1(functiongeneration). Bottompanel: LateWin-
ter2PM,rainyconditionsattheQuestReceptionDesk, tivessuchastheCommonsensePersona-Grounded
showinganexampleofdialoguegenerationinTask2. DialogueChallenge(CPDC)2025(SonyAI,2025).
Thiscompetitioninvitedsubmissionsaimedatde-
veloping NPC agents capable of demonstrating
entertainmentfieldhasremainedrelativelyunder-
bothpersonaconsistencyandtaskexecutionprofi-
explored,particularlyintraditionalentertainment
ciencywithinafantasyRole-PlayingGame(RPG)
mediacreationsuchasvideogames. Conventional
environment,asillustratedinFigure1.
gamedevelopmentreliesheavilyonprogrammed
Building upon this challenge, our work inves-
logic, where in-game events and character inter-
tigates multiple complementary strategies for en-
actionsfollowpredeterminedscriptsanddialogue
hancing the coherence and reliability of LLM-
trees. Toenhanceplayerimmersionandnarrative
driven NPCs across diverse interaction settings.
depth,developershavebegunincorporatingLLMs
Specifically,weexploreaDeflanderizationprompt-
asintegralcomponentsofNPCs. Thisintegration
ingapproachthatmitigatescharacterdriftandpre-
enablesthemtoexhibithuman-likebehaviorsand
serves personality coherence during extended di-
engageindynamic,contextually-awareconversa-
alogues,ensuringbalancedperformancebetween
tionswithplayers (Songetal.,2024b).
dialoguegenerationandfunctionexecution. Tofur-
However,maintainingtheconsistencyanddepth therstrengthencontextualgrounding,weintegrate
ofthesedynamicpersonasoverlong-terminterac- a Retrieval-Augmented Generation (RAG) mech-
tions presents a significant challenge. One such anism that incorporates memory and similarity-
pitfall, drawn from media analysis, is the trend based retrieval from prior interactions, allowing
of"flanderization"(Larsen,2019). Flanderization NPCs to produce responses aligned with both in-
istheprocessthroughwhichacomplexcharacter gamehistoryandestablishedworldknowledge. Fi-
is progressively simplified over time, eventually nally,weemploySupervisedFinetuning(SFT)with
becomingacaricaturedefinedbyasingle,exagger- Low-RankAdaptation(LoRA)torefinemodelbe-
atedtrait. Thetermoriginatesfromthecharacter havior at the parameter level, enhancing stylistic
NedFlandersinTheSimpsons,whoevolvedfrom consistencyandfunctionalprecisionwhileremain-
agenuinelygood-naturedneighbor—whosefaith ingcomputationallyefficient.
wasoneofmanyaspectsofhispersonality—intoa Together, these methods constitute a uni-
one-dimensionalreligiouszealot. fied framework that examines the interplay be-
RecentadvancesinLLM-drivenNPCsdemon- tweenprompting,retrieval-augmentedreasoning,
stratesignificantpotentialfortransformingplayer and finetuned adaptation in achieving persona-
experiences. Cross-platform dialogue systems consistent,context-aware,andgoal-directedNPC
allow NPCs to maintain consistent interactions performancewithintheCPDC2025setting.
across both game environments and social plat- Fromourparticipationinthischallengeacross
formslikeDiscord (Songetal.,2024b),creating everytrack,bothGPUandAPIdivisions,thefol-
unprecedentedcontinuityinplayer-characterrela- lowingarekeypointsthatweinvestigated:

• Deflanderization prompting technique to ingtheenvironment,validatingresults,controlling
maintaindialoguegenerationandfunction theoverallplan,andretrievingtoolsfromatoolset
generationabilityincommonfantasyRPG (Xuetal.,2025).
worldsetting. A key challenge in this domain is the develop-
mentofrobustevaluationbenchmarks. Whileex-
• Explore the performance trade-offs be-
istingbenchmarkshavefocusedonsingle-control
tween dialogue generation and func-
environmentswhereonlytheAIagentcaninteract
tion generation tasks using the proposed
withtools,recentworkhasintroducedmorecom-
promptengineeringtechnique.
plexscenarios. Forinstance (Barresetal.,2025),
2 RelatedWork the τ2-Bench introduces a dual-control environ-
mentwhereboththeagentandtheusercanutilize
2.1 AgentsforGame-OrientedDialogue toolstoactinashared,dynamicworld. Thissetup
Task-oriented systems are designed to efficiently isdesignedtomoreaccuratelyrepresentreal-world
complete specific tasks within larger workflows, collaborativescenarios,suchastechnicalsupport,
oftenservingasprerequisitesforlaterstages. Inte- andtoexposethechallengesofagentcoordination
gratingagenticsystemsenhancestheseworkflows andcommunicationthatareabsentinsingle-user
byenablingagentstoanalyzeproblems,plan,and controlevaluations. TheperformanceofLLMsde-
execute actions toward defined goals. Research grades significantly in such dual-control settings,
on task-oriented dialogue (TOD) systems, such underscoringthedifficultyofguidinguseractions
as (Kazi et al., 2024), benchmarks agent perfor- andtheimportanceoffurtherresearchinthisarea.
mance by assessing planning effectiveness, goal
3 CompetitionOverview
alignment,andinteractionmethodsusedtogather
informationandachievesuccessfuloutcomes. 3.1 CompetitionTasks
Inthecontextofgaming,completingasequence
TheCPDCcompetitionaimstofacilitatedialogues
ofeventsofteninvolvesaccomplishingaseriesof
thatseamlesslyintegratecontextualunderstanding,
tasks. Toaidplayers,especiallynewcomers, (Lee
knowledgeutilizationandtaskexecutioncapabili-
etal.,2025)developedaspecializedgameassistant.
tiesinafantasyRPGgamesetting(SonyAI,2025).
ThisassistantleveragesanLLMthathasundergone
Thecompetitioncomprisestwotracks,APITrack
continuous pre-training and instruction tuning to
andGPUTrack(detailedinthenextsection),and
answer specific game-related questions, thereby
eachtrackconsistsofthreetasks:
helpingusersnavigatecomplexgamemechanics.
Toensurethatinteractiveagentscansuccessfully • Task1: Task-OrientedDialogueAgents,
completetheirobjectiveswithinagame(Phillips
etal.,2025)introducedaframeworkthatutilizes • Task2: Context-AwareDialogueAgents,
two distinct agents: a Dialogue agent and a goal-
• Task3: IntegratedContextualDialogueand
verifyingagent. Thissystememployssharedmem-
Task Execution (combining both Task 1 and
orytomanageinteractions,ensuringthatdialogue
Task2).
and actions remain aligned with the overarching
taskgoals. Examples of these tasks are illustrated in Fig-
ure1.
2.2 Toolcalling
Tool-callingorfunction-calling,anabilityofLLMs 3.1.1 Task1: Task-OrientedDialogueAgents
to interact with external tools or functions, expe- Inthistask,participantsdevelopdialogueresponse
rienced a recent surge in interest, driven by the generationsystemsthatoperateintwophases: first,
potentialofLLMstoautonomouslycompletetasks assessingconversationalcontexttodeterminenec-
bydynamicallyaccessingandactinguponexternal essaryfunctioncalls,andsecond,executingthese
resources, extending their capabilities to become calls with appropriately selected arguments that
agenticAI (Xuetal.,2025;Patiletal.,2025). alignwiththeconversationfortaskexecution. For
The architecture of these agents typically in- example,merchantNPCsingamesselectweapons
volvesamulti-stepframeworktoensureaccuracy tosellbasedonplayerdialogue. Evaluationinthis
incomplex,real-worldtasks. Thisframeworkin- trackprimarilyfocusesonthecorrectnessoffunc-
cludescomponentsforexecutingactions,perceiv- tioncallsandtheaccuracyofargumentselection.

3.1.2 Task2: Context-AwareDialogueAgents respondnaturallyandconciselywhileavoid-
Inthistask,participantsdevelopdialogueresponse ingexaggeratedrole-playing. Ourerroranal-
generationsystemsthatfocusongeneratingNPC ysisofthebaselinesetupfromthechallenge
responseswithtonesalignedtotheirassignedper- comparing generated responses with gold-
sonas. Evaluationemphasizestheextenttowhich standard outputs revealed that the baseline
generatedresponsesmaintainconsistencywiththe setupoftenproducedoverlyelaborateandcon-
NPC’sdefinedpersonaandcharactertraits. textuallydiffuseoutputs,focusingexcessively
onthenarrativesetting(e.g.,adoptinganRPG
characterpersona)ratherthanaddressingthe
Start
immediateconversationalintenttoplayer. In
contrast,thegoldresponsesreflectedamore
human-likeunderstandingofplayerrequests
and directly activated the appropriate func-
Step1: PrepareFunctionCallingPrompt
tionswithclarity.
• F (Fewshot): Includes two sample dia-
logues(merchantandguildreceptionist)from
sample.jsonintheprompt.
Step2: FunctionGeneration(APICall#1)
• ZeroShot: Uses the initial baseline prompt
fromthecompetitionrepository.
Step3: ExecuteFunctions • CoT (Chain of Thought): Instructs the
modeltothinkstep-by-stepbeforeanswering.
• RW (Remove world setting): Removes
worldviewinformationwhenconstructingdi-
Step4: PrepareDialoguePrompt
alogueprompts.
• G(Guide): Guidesresponsestylebylimiting
to1–2shortsentences,usingsimplelanguage,
andrestrictingtoprovidedknowledge.
Step5: DialogueGeneration(APICall#2)
• MW (Most word): Guides word usage and
providesexamplephrases.
FinalResponse • Definefunction: Providestwosamplefunc-
tionarguments(merchantandguildreception-
ist)withtheiritemsinJSONformat.
Figure2: MainpipelinefortheAPITracktask3. The
promptingstagesareStep1andStep4andgenerataion Our best submission (ranked 2nd on Task 3,
stagesareinStep2andStep5
2nd onTask1and5th onTask2)onpublicleader
boardusedonlyD-RWcombinedwithtwoturns
4 CompetitionTracks ofsampledialogues.
4.2 GPUTrack
4.1 APITrack
Due to the compute limitations described in Ap-
In the API track, participants submit their work
pendixD,weselectedmodelsthatcanbeexecuted
within specific environment and constraints such
ontheAWSg5e.2xlargeinstanceswithL40sGPUs
as the allowed LLM is GPT-4o-mini (see D for
instance. Wefirstvalidatedinferencesubmission
full details). We focused on prompting methods.
feasibility using Qwen2.5 (Qwen et al., 2024),
Our pipeline is illustrated in Figure 2. We sys-
Qwen3(Yangetal.,2025),LLaMA3.1(Grattafiori
tematicallyexploredthefollowingpromptingap-
etal.,2024),andPhi-4(Abdinetal.,2024),before
proaches:
proceeding with finetuning experiments on both
• D(Deflanderization): Promptsthemodelto initialandaugmenteddata.

To improve dialogue grounding, we incorpo- train.json, sample.json. Tables 1 and 2 sum-
ratedahybridRetrievalAugmentedGeneration marizethetheAPItrackresultsforTask1andTask
(RAG) + Memory approach. The retrieval mod- 3,respectively. Weobserveseveralnotabletrends:
ule encodes both player and NPC conversation 1. EffectivenessofDeflanderizationprompt-
historiesusingQwen3-Embedding-0.6B,enabling ing.
similarity search across pre-collected interaction Acrossbothtasks,theDeflanderization(D)strat-
datasets. The retrieved context is injected at two egyconsistentlyimprovedscorescomparedtothe
stages: (i) Function Selection, where prior con- zero-shot baseline. In Task 3 (Table 2), D-RW
versationsguideaccuratetoolinvocation,and(ii) achieveda+0.013absolutegaininCPDCscore(all)
DialogueDrafting,whererelevantNPCresponses comparedtozero-shot. Thissupportsourhypothe-
providestyleandfactualgrounding. sisthatoverlystrongrole-playingcanhinderfunc-
Additionally,weexploredaRAG+Refinestep, tional correctness by diverting the model toward
wheregenerateddraftsarerewrittentomatchthe stylisticembellishmentratherthanmorerealistic
toneandlengthofhigh-similaritygoldenresponses, character.
ensuring stylistic consistency with provided in- 2. Sample-based prompting further boosts
gamedialogue. accuracy.
Our best-performing submission (ranked 4th Addingfew-shotexamples(F)totheDeflander-
on Task 3 public leaderboard) was achieved izationpromptprovidedclearbenefitsinTask1(Ta-
with Qwen3-14B. We applied Supervised ble 1), with improvements of +0.092 and +0.133
Finetuning (SFT) with Low-Rank Adaptation on train.json, respectively. Notably, our best-
(LoRA) (Hu et al., 2022) using the Unsloth performingAPIsubmissioncombinedD-RWwith
framework (Daniel Han and team, 2023). The two-turnfew-shotexamples,yieldingthehighest
training procedure was divided into two stages: leaderboardplacement(2nd onTask3,2nd onTask
(1) Full SFT on initial and synthetic multi-turn 1,and5th onTask2).
dialogue data, followed by (2) LoRA-SFT 3. Limitedbenefitsofmorecomplexprompt-
(rank=32, α = 32) on combined dialogue and ing.
function-callingdatasets. Chain-of-Thought(CoT),guidingresponses(G),
We generated the datasets using gemini-2.5- andMostWord(MW)constraintsyieldedmarginal
pro-preview-05-06(deepmind,2025)forfunction- orinconsistentgains. Forinstance,CoTimproved
calling data and GPT-4o-mini (OpenAI, 2024) BERTScore in Task 1 but decreased function ar-
fordialoguedata. Thegenerateddatasetsconsist gument accuracy, likely due to verbose reason-
of: Multi-turn(2,800datapoints),Multi-turnrea- ing diluting key arguments. Similarly, MW im-
soning(2,800datapoints)forTask2(3.1.2)and provedBLEUontrain.jsonbutdidnottransfer
Funtion-calling generation (328 data points) for totheleaderboardCPDCscore. Thissuggeststhat
Task1(3.1.1). Promptsusedfordatageneration lightweightstrategies(D+few-shot)aremorero-
areprovidedin C.1. bustundercompetitionconstraintsthancomplex,
For inference, we optimized deploy- multi-signalpromptsforthesetasks.
ment with vLLM (Kwon et al., 2023) Table 3 presents results for Task 3 under the
using the following hyperparameters: GPUtrack.
dtype=’bfloat16’, gpu_memory_utilization=0.8, 1. Model scaling and finetuning are critical.
enable_LoRA, max_model_len=4096, and dis- Baseline submissions with smaller models (e.g.,
able_sliding_window=True,enablingQwen3-14B LLaMA3.1-8B,Phi-4-mini)underperformed,with
torunwithintheL40smemorybudget. all-scores below 0.40. In contrast, Qwen3-14B
with full SFT and LoRA achieved a significant
5 Results improvement, reaching 0.598 all-score, ranking
4th ontheleaderboard. Thishighlightstheimpor-
5.1 APITrack
tanceofbothmodelsizeandtargetedfinetuningon
Before submitting to the (AIcrowd, 2025) sub- domain-specificdata.
mission system, we focused on testing the API 2. Retrieval augmentation provided modest
track on existing datasets to explore possible improvements. RAG+RefineandRAG+Memory
prompting technique. The dataset consists of approaches improved Qwen3-8B performance to
Task 1 train.json, sample.json and Task 2: 0.522forTask1,showingthatretrievalhelpsstabi-

Table1: APITrackTask1Result
Dataset metrics ZeroShot(Z) CoT(CoT) F(F) Definefunction(func) OurBest(D),(RW)
Functionnameexactmatch 0.622 0.537 0.633 0.615 0.714
train.json Functionargumentexactmatch 0.226 0.211 0.199 0.210 0.359
BERTScore 0.542 0.566 0.538 0.539 0.569
Functionnameexactmatch 0.667 0.333 0.600 0.714 0.727
sample.json Functionargumentexactmatch 0.333 0.000 0.100 0.429 0.364
BERTScore 0.509 0.534 0.491 0.496 0.534
test(submission) CPDCscore(Task1) 0.422 0.383 0.441 0.430 0.586
Table2: APITrackTask3Result
Dataset metrics ZeroShot D(D) D-F-RW(RW) D-F-G-RW(G) D-F-MW-G-RW(MW) OurBest
BLEU-4 0.031 0.035 0.032 0.041 0.043 0.040
train.json Word-levelF1 0.293 0.273 0.279 0.290 0.300 0.292
BERTScore 0.525 0.543 0.527 0.537 0.542 0.540
BLEU-4 0.027 0.028 0.024 0.030 0.050 0.095
sample.json Word-levelF1 0.276 0.281 0.293 0.319 0.327 0.331
BERTScore 0.536 0.548 0.553 0.557 0.568 0.577
CPDCscore(Task1) 0.422 0.436 0.429 0.432 0.441 0.587
test(submission) CPDCscore(Task2) 0.598 0.614 0.619 0.612 0.612 0.615
CPDCscore(all) 0.510 0.525 0.524 0.522 0.526 0.601
lizedialoguegrounding. However,thesemethods pendixF.
fellshortofthegainsachievedbyLoRA-SFT.We
Acknowledgments
attributethistothelimitedscaleoftheretrievalcor-
pusandthechallengeofinjectingretrievedcontext ThisresearchwassupportedbytheFacultyofEngi-
seamlesslywithoutoverloadingprompts. neering,ThammasatSchoolofEngineering,Tham-
3. Trade-offbetweenTask1andTask2. Inter- masat University also thanks to PreceptorAI that
estingly,whileRAG+RefinegavethebestTask1 providesAPIforgenerateadditionaltrainingdata.
score (0.522), it underperformed on Task 2 com-
paredtobaseline. Conversely,LoRA-SFTbalanced
References
bothtasks,producingthehighestjointscore. This
suggeststhatalignmentbetweenfunctionalreason- Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien
ing(Task1)andpersona-groundeddialogue(Task Bubeck, Ronen Eldan, Suriya Gunasekar, Michael
Harrison,RussellJ.Hewett,MojanJavaheripi,Piero
2)requiresjointoptimization,ratherthanmodular
Kauffmann,JamesR.Lee,YinTatLee,YuanzhiLi,
improvementsinisolation.
WeishungLiu,CaioC.T.Mendes,AnhNguyen,Eric
Price,GustavodeRosa,OlliSaarikivi,and8others.
6 Discussion
2024. Phi-4technicalreport.
Overall,ourfindingsrevealcomplementarystrate- AIcrowd.2025. Aicrowd: Openchallengesandcom-
gies across the API and GPU tracks. Prompting- petitions. https://www.aicrowd.com/. Accessed:
2025-06-26.
based Deflanderization with few-shot grounding
proved effective in low-resource API settings, SeyedHosseinAlavi,SudhaRao,AshutoshAdhikari,
whilefinetunedlargemodelsdominatedtheGPU GabrielADesGarennes,AkankshaMalhotra,Chris
Brockett,MahmoudAdada,RaymondT.Ng,Vered
track. Importantly,bothtrackshighlightedthechal-
Shwartz, and Bill Dolan. 2024. Mcpdial: A
lengeofbalancingpersonaconsistencywithfunc-
minecraftpersona-drivendialoguedataset. Preprint,
tionalprecision: methodsthatimprovedrole-play arXiv:2410.21627.
fidelitysometimeshurtargumentcorrectness,and
Victor Barres, Honghua Dong, Soham Ray, Xujie Si,
vice versa. Future work should explore hybrid andKarthikNarasimhan.2025. t2-bench:Evaluating
strategies that unify lightweight prompting with conversationalagentsinadual-controlenvironment.
retrieval-augmentedfinetuning,enablingagentsto
StevenBird,EwanKlein,andEdwardLoper.2009. Nat-
sustainbothaccuracyandbelievabilityinfantasy
ural Language Processing with Python. O’Reilly
RPGenvironments. OurfinalrankingsareinAp- Media.

Table3: ResultsubmissionatGPUTrackonTask3.
Model Method ScoreTask1 ScoreTask2 All
LLaMA3.1-8B baseline 0.439 0.333 0.386
Phi4-mini baseline 0.328 0.354 0.341
Qwen2.5-7B baseline 0.440 0.587 0.513
Qwen3-8B baseline 0.449 0.587 0.518
Rag+Refine 0.522 0.549 0.535
Qwen3-14B-FP8 RagMemory 0.502 0.532 0.517
SFT+LoRA(OurBest) 0.590 0.606 0.598
Steven Bird, Edward Loper, Ewan Klein, and the TaahaKazi,RuiliangLyu,SizheZhou,DilekHakkani-
NLTK Team. 2025. Natural Language Toolkit Tur,andGokhanTur.2024. Largelanguagemodels
(NLTK). GitHub repository. Commit as of latest asuser-agentsforevaluatingtask-oriented-dialogue
access;seehttps://github.com/nltk/nltk. systems.
MichaelHanDanielHanandUnslothteam.2023. Un- Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying
sloth. Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E.
Gonzalez, Hao Zhang, and Ion Stoica. 2023. Effi-
deepmind. 2025. Gemini 2.5: Our newest cientmemorymanagementforlargelanguagemodel
gemini model with thinking. https: servingwithpagedattention. InProceedingsofthe
//blog.google/technology/google-deepmind/ ACMSIGOPS29thSymposiumonOperatingSystems
gemini-model-thinking-updates-march-2025/. Principles.
Accessed: 2025-05-18.
Brittany Larsen. 2019. Gatekeeping remix: Fandom
SilinGao,BeatrizBorges,SoyoungOh,DenizBayazit, spacesandidentitypolitics. Master’sthesis,Illinois
Saya Kanno, Hiromi Wakaki, Yuki Mitsufuji, and StateUniversity.
AntoineBosselut.2023. PeaCoK:Personacommon-
senseknowledgeforconsistentandengagingnarra- JeehyunLee,Seung-MooYang,andWonIkCho.2025.
tives. InProceedingsofthe61stAnnualMeetingof AMAN:Agentformentoringandassistingnewbies
theAssociationforComputationalLinguistics(Vol- in MMORPG. In Proceedings of the 31st Interna-
ume 1: Long Papers), pages 6569–6591, Toronto, tionalConferenceonComputationalLinguistics: In-
Canada.AssociationforComputationalLinguistics. dustryTrack,pages522–532,AbuDhabi,UAE.As-
sociationforComputationalLinguistics.
AaronGrattafiori,AbhimanyuDubey,AbhinavJauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al- Guohao Li, Hasan Abed Al Kader Hammoud, Hani
Dahle, Aiesha Letman, Akhil Mathur, Alan Schel- Itani, Dmitrii Khizbullin, and Bernard Ghanem.
ten,AlexVaughan,AmyYang,AngelaFan,Anirudh 2023. Camel: Communicative agents for "mind"
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi- explorationoflargelanguagemodelsociety. arXiv
tra, Archie Sravankumar, Artem Korenev, Arthur preprintarXiv:2303.17760.
Hinsvark,and542others.2024. Thellama3herdof
models. Chia-WeiLiu,RyanLowe,IulianSerban,MikeNose-
worthy, Laurent Charlin, and Joelle Pineau. 2016.
Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng How NOT to evaluate your dialogue system: An
Cheng, Ceyao Wang, Zili Wang, Steven CH Yau, empiricalstudyofunsupervisedevaluationmetrics
Zijuan Lin, Liyang Zhou, Chenyu Ran, and 1 oth- fordialogueresponsegeneration. InProceedingsof
ers. 2023. Metagpt: Meta programming for multi- the2016ConferenceonEmpiricalMethodsinNatu-
agent collaborative framework. arXiv preprint ralLanguageProcessing,pages2122–2132,Austin,
arXiv:2308.00352. Texas.AssociationforComputationalLinguistics.
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Jekaterina Novikova, Ondˇrej Dušek, Amanda Cer-
Allen-Zhu,YuanzhiLi,SheanWang,LuWang,and casCurry,andVerenaRieser.2017. Whyweneed
WeizhuChen.2022. LoRA:Low-rankadaptationof newevaluationmetricsforNLG. InProceedingsof
largelanguagemodels. InInternationalConference the2017ConferenceonEmpiricalMethodsinNatu-
onLearningRepresentations. ralLanguageProcessing,pages2241–2252,Copen-
hagen,Denmark.AssociationforComputationalLin-
GuangyuanJiang, ManjieXu, Song-ChunZhu, Wen- guistics.
juanHan,ChiZhang,andYixinPeng.2022. Evaluat-
ingandinducingpersonalityinpre-trainedlanguage OpenAI.2024. Gpt-4omini: advancingcost-efficient
models. arXivpreprintarXiv:2206.07550. intelligence. Accessed: 2025-05-18.

JoonSungPark,JosephCO’Brien,CarrieJCai,Mered- Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
ith Ringel Morris, Percy Liang, and Michael S dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and
Bernstein. 2023. Generative agents: Interactive AnimaAnandkumar.2023. Voyager: Anopen-ended
simulacra of human behavior. arXiv preprint embodiedagentwithlargelanguagemodels. arXiv
arXiv:2304.03442. preprintarXiv:2305.16291.
Shishir G. Patil, Huanzhi Mao, Charlie Cheng-Jie Ji, Weikai Xu, Chengrui Huang, Shen Gao, and Shuo
FanjiaYan, VishnuSuresh, IonStoica, andJoseph Shang. 2025. Llm-based agents for tool learning:
E. Gonzalez. 2025. The berkeley function calling Asurvey. DataScienceandEngineering.
leaderboard (bfcl): From tool use to agentic eval-
uation of large language models. In Forty-second AnYang,AnfengLi,BaosongYang,BeichenZhang,
InternationalConferenceonMachineLearning. Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Dayi-
AdonPhillips,JochenLang,andDavidMould.2025. hengLiu,FanZhou,FeiHuang,FengHu,HaoGe,
Goal-orientedinteractionsingamesusingllms. IEEE HaoranWei,HuanLin,JialongTang,and41others.
TransactionsonGames,17(2):510–521. 2025. Qwen3technicalreport.
SaizhengZhang, EmilyDinan, JackUrbanek, Arthur
Chen Qian, Xin Liu, Jingyao Liu, Ziyi Wen, Yufan
Szlam,DouweKiela,andJasonWeston.2018. Per-
Zhao,YueDang,and1others.2023. Communica-
tiveagentsforsoftwaredevelopment. arXivpreprint sonalizing dialogue agents: I have a dog, do you
arXiv:2307.07924. havepetstoo? Proceedingsofthe56thAnnualMeet-
ingoftheAssociationforComputationalLinguistics
Qwen, :, An Yang, Baosong Yang, Beichen Zhang, (Volume1: LongPapers),pages2204–2213.
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan
Weinberger,andYoavArtzi.2019. Bertscore: Evalu-
Lin,JianYang,JianhongTu,JianweiZhang,Jianxin
atingtextgenerationwithbert.
Yang,JiaxiYang,JingrenZhou,and25others.2024.
Qwen2.5technicalreport.
Abhijeet Rao, Yiming Xu, Dakshinamurthy Karra
Chaudhary,LucianPistol,YolandaDobre,Jonathan
Ho,AlistairKnott,andCraigMcDonald.2024. Col-
laborative quest completion with llm-driven non-
player characters in minecraft. arXiv preprint
arXiv:2407.03460.
AlirezaSalemi,ShesheraMysore,MichaelBendersky,
andHamedZamani.2023. Lamp: Whenlargelan-
guagemodelsmeetpersonalization. arXivpreprint
arXiv:2304.11406.
JaewooSong,AndrewZhu,andChrisCallison-Burch.
2024a. Youhavethirteenhoursinwhichtosolvethe
labyrinth: Enhancingaigamemasterswithfunction
calling. Preprint,arXiv:2409.06949.
LiSongand1others.2024b. Llm-drivennpcs: Cross-
platformdialoguesystemforgamesandsocialplat-
forms. arXivpreprintarXiv:2504.13928.
SonyAI.2023. Thecommonsensepersona-grounded
dialogue challenge 2023. Competition timeline:
November3,2023-March15,2024.
SonyAI.2025. Thecommonsensepersona-groundeddi-
aloguechallenge2025. Competitiontimeline: April
9-June30,2025.
Yu-MinTseng,Yu-ChaoHuang,Teng-YunHsiao,Wei-
Lin Chen, Chao-Wei Huang, Yu Meng, and Yun-
NungChen.2024. Twotalesofpersonainllms: A
surveyofrole-playingandpersonalization. InFind-
ingsoftheAssociationforComputationalLinguis-
tics: EMNLP2024.AssociationforComputational
Linguistics.

Appendix
A ExploratoryDataAnalysis
Before doing some experiments, we perform
data analysis on Task 1_train.json and Task
2_train.json.
Figure 6: Merchant NPC Response Return Value Ra-
tiosinTask1_train.json(Green=return;Red=no
return)
Figure 3: Age-gender of characters in Task
2_train.json,thediagramshownthatbalancedNPC
characters(20merchantand20guildreceptionist)most
NPCarewomenwiththeyoungeragethanmen.
Figure 7: Barplotof frequency merchant/guild recep-
tionistmappedwiththeirweatheronthatsituation.
automaticallyevaluatethedialoguegenerationso
we try to use some of these metrics in our local
environmentfortaskdialoguegenerationB.2and
task function generation we use these metrics in
Figure4: Date-timedistributioninTask2_train.json,
experimentsB.1.
mostofeventoccurafter1pmandthereareonlyquest
receptionplaceeventinwinterseason. Whileautomaticmetricsalonearenotfullyre-
liable for evaluating dialogue systems (Liu et al.,
2016;Novikovaetal.,2017),theorganizersthere-
forereliedonhumanevaluationforthefinalprivate
leaderboard.
B.1 Task1
B.1.1 Functionnameexactmatch
Thismetricchecksifthepredictedfunctionname
matchesthereferenceexactly:
Figure5: GuildNPCResponseReturnValueRatiosin
Task1_train.json(Green=return;Red=noreturn)
Acc = 1 (cid:88)
N
1{fpred = fref}, (1)
name N i i
i=1
B EvaluationMetrics
InCPDC2023(SonyAI,2023)theyusedWordF1,
wherefpred andfref
denotethefunction’sname
i i
BLEU,CPDScore,USEScoreandBERTScoreto setsofinstancei.

B.1.2 Functionargumentexactmatch B.2.3 CPDCscore
This metric checks if all predicted arguments ex-
Shown in public leader board it is expected that
actlymatchthereference:
weighted between WordF1, BLEU, USEScore
N and BERTScore in dialogue generation task and
Acc = 1 (cid:88) 1{Apred = Aref}, (2) weightedexactmatchfunctionname,argsinfunc-
args N i i
i=1 tiongenerationtask.
whereApred andAref
denotetheargumentsetsof
i i
instancei.
C Prompts
B.1.3 BERTScore
We also measure semantic similarity of function C.1 AdditionalDataGeneration
callswithBERTScore(Zhangetal.,2019). Given
tokens X = (x ,...,x ) from prediction and
1 m promptfordatagenerationinTask1by
Y = (y ,...,y )fromreference:
1 n Gemini-2.5-pro
E(x )·E(y )
i j """You are tasked with generating high-
s(x ,y ) = , (3)
i j
∥E(x i )∥∥E(y j )∥ qualitygamedialoguebetweenaplayerand
anNPCwhohasamerchantrole. Youare
m n
(cid:88) (cid:88) providedwith:
P = 1 maxs(x ,y ),R = 1 maxs(y ,x )
m i j n j i 1. Alistofavailablefunctioncallsthatthe
j i
i=1 j=1
NPC can use to respond. 2. Structured
(4)
knowledgerelevanttotheNPC’sinventory,
2PR
BERTScore-F1 = . (5) abilities,oritemlore.
P +R
Yourresponsibilitiesare:
B.2 Task2 -Generateanaturalandcontextuallyappro-
priateplayerdialoguethatclearlyexpresses
InTrack2,weevaluaterole-playingconsistencyus-
the player’s intent or question. - Select a
ingfourmetrics,includingBERTScore(described
functioncallfromtheprovidedlistthatap-
in Appendix B.1.3), with the remaining metrics
propriatelyaddressestheplayer’srequest. -
detailedbelow.
Fillinthefunction’sparametersusingonly
B.2.1 BLEU-4 theprovidedknowledgebase. Donotinvent
newvalues.
BLEU-4 is based on modified n-gram precision
—
(forn = 1,2,3,4)withabrevitypenalty(BP):
#ProvidedFunction(s)formatted_tools
(cid:32) 4 (cid:33) #Knowledgeknowledge
(cid:88)
BLEU-4 = BP·exp 1 logp , (6) —
4 n
n=1 #DesiredOutputFormat
“‘json "player_dialogue": "<string>",
where p is the modified n-gram precision and
n "gold_functions": [ "name": "<string>",
BP = 1ifc > r,otherwiseexp(1−r/c),withc =
"parameters": "<parameter_name>": "<pa-
candidatelengthandr =referencelength.
rameter value>" ] #Example Out-
put "player_dialogue": "The price is
B.2.2 Word-levelF1
reasonable. Though before deciding,
First we tokenize both Tpred and Tref using
could you tell me more about how other
NLTK(Birdetal.,2025,2009)thencalculateWord-
magic users integrate this dagger into
levelF1overtokensets:
their combat style?", "gold_functions": [
2·P ·R "name": "check_description","parameters":
F1 = , (7)
P +R "item_name": "ManGauche" ] """
|T ∩T | |T ∩T |
whereP = pred ref andR = pred ref .
|T | |T |
pred ref

promptfordatagenerationinTask2by
astheNPC."
Gpt4o-mini
"role": "system","content": "Youaretasked C.2 FewShot
withgeneratinganaturalandimmersivedi-
FewShotpromptforTask2inAPITrack
aloguebetweenaplayercharacter(adven-
turer) and a non-player character (NPC) "
"#Instruction""YouareactingasanNPC
"in afantasy RPGgamesetting, usingthe
character in game." "Respond naturally
providedNPCpersonaandrole."
andconcisely,basedonlyontheprovided
"Theplayer’sdialoguemustshowclearpur-
knowledge." "Avoid exaggerated roleplay
pose and in-world context — such as:" "-
or guessing. It’s okay to say you’re un-
preparingforamission""-reportingback
sure." "Speak like a real person in that
from a quest" "- gathering supplies for an
world — short, simple, and in charac-
event(e.g. beforesunset)""-checkingfor
ter." "" "# NPC Character Profile" #"Play
newtasksafterreturningtotown"
this character without over-acting. Use
"Do NOT let the player speak in vague or
brief, helpful, and realistic responses."
generic ways. Avoid lines like: ’Got any-
"{character_setting}""""#Knowledge""1.
thing?’,’Whatdoyouhave?’,’Anywork?’
FunctionCallKnowledge(recentandspe-
—instead,havethemspeakbasedontime,
cific)""{function_knowledge}""2. General
place,orsituation. Maketheirgoalandur-
Knowledge (background/context)" "{gen-
gencyclear."
eral_knowledge}""""#ExampleDialogue"
"NPC responses must:" "- be short and
"Player: ’I’mgatheringinformationabout
natural (2–3 sentences only)" "- ask at
thelegendarysword. Haveyouheardanyof
most ONE question" "- reflect their per-
thetalesaboutit?’""NPC:’Oh,absolutely.
sona, role, and current knowledge" "-
Everywarriordreamsofit. Manyhaveven-
avoid formal or bookish vocabulary (e.g.,
turedintounknownterritoriesinsearchof
’commendable’, ’evaluate’, ’indeed’)" "-
it. I’ve heard stories of people traveling
avoid exaggerated roleplay or dramatic
to all sorts of places, from the continent
taglines" "- be grounded in the world —
to the seas.’" "Player: ’Everyone seems
it’s fine to say ’I’m not sure’, or sug-
to be interested in legendary weapons. I
gestnextsteps", "role":"user","content":
guesstheymustbethatprestigious,huh?’"
f"NPCRole: NPC_ROLE"f"NPCPersona:
"NPC:’Yeah, that’s probably true. But I
NPC_PERSONA",
thinkit’snotsomuchabouttheweaponit-
selfhavinghonor,butmoreaboutwhether
the person wielding it has the skill and is
promptforreasoninggenerationinTask
worthyofit."
2byGpt4o-mini
"Youareanon-playercharacter(NPC)ina
FewShotpromptforTask1inAPITrack
fantasyRPGgame."
"Youwillbegiven:""-Your**Role**""- "#Instruction""Youareanassistantinesti-
Your **Persona** (your personality and matingfunctionnamesandargumentsgiven
worldview)" "- A **Player’s Dialogue** some dialogues in a video game world."
(themessagetheysaytoyou)""-Yourown "Youwillneedthefollowinginformationto
**NPCResponse**(whatyousaidback)" respondtotheuser’sinput. ""Usethefol-
"Your task is to **reason from your NPC lowingstepstoestimatethenecessaryfunc-
point of view**:" "**Explain why you re- tionnamesandarguments. """"1. Readthe
spondedthatway**—whatintheplayer’s dialogueandthetargetitem. ""2. Fromthe
message triggered your response? What givenfunctioninformation,selectthefunc-
logic,emotion,orinstinctguidedyou?""" tions that can obtain the information you
"DoNOTincludeanytitle,heading,orex- need. ""3. Fillintheargumentsneededby
planation—onlyyourinternalmonologue the function as appropriate. " "Note: You

C.4 Deflanderization
may select multiple functions or no func-
tionsatall. """"#AdditionalInformation
Deflanderization prompt for Task 2 in
" "{}" "# Example Function Information"
APITrack
"{merchant_info}""{guild_info}""#Dia-
logue""Theuserinputforthecurrentturn "#Instruction""YouareactingasanNPC
isasfollows. " characterinavideogame.""Respondnatu-
rallyandconcisely,basedonlyonthepro-
videdknowledge.""Avoidexaggeratedrole-
play or guessing. It’s okay to say you’re
unsure." "Speak like a real person in that
world — short, simple, and in character."
"""#CharacterProfile""Playthischaracter
C.3 ChainofThought
withoutover-acting. Usebrief,helpful,and
realisticresponses.""{character_setting}"
"" "# Knowledge" "There are two parts
of knowledge. The first part is the spe-
Chain ofThought prompt for Task 1in
cificknowledgeobtainedfromthefunction
APITrack
calls. " "The second part is the general
"#Instruction""Youareanassistantinesti- knowledge of all items involved in the di-
matingfunctionnamesandargumentsgiven alogue. " "" "## Knowledge from Func-
some dialogues in a video game world." tion Calls" "{function_knowledge}" "##
"You will need the following information General Knowledge of All Items" "{gen-
to respond to the user’s input and always eral_knowledge}" "" "# Worldview: It de-
explainsyourreasoningbeforemakingany scribesthesettingoftheworldinthevideo
functioncall.""Ineachturn, firstoutputa game. ""{worldview}"
paragraphbeginningwith’**Reasoning:**’
explainingwhatyouaretryingtodo,"
C.5 Mostword
"andwhythefunction(s)youarecallingare
needed." "Then, generate the appropriate Most word prompt for Task 2 in API
functioncall(s)." Track
"#Use the following steps to estimate the
"# Instruction" "You are acting as an
necessaryfunctionnamesandarguments."
NPC character in game." "Respond nat-
"YouMUSTfollowthestructurebelow. If
urally and concisely, based only on the
youskipanypart,youranswerwillbecon-
providedknowledge.""Avoidexaggerated
sideredinvalid."
roleplay or guessing. It’s okay to say
"## Step-by-step:" "1. Read the dialogue
you’re unsure." "Speak like a real person
andthetargetitem.""2. Selectthefunctions
in that world — short, simple, and in
that can retrieve the information needed."
character.""""#CharacterProfile"#"Play
"3. Fillintheargumentsbasedoncontext."
this character without over-acting. Use
"4. First,generatea‘ResponseOutputMes-
brief, helpful, and realistic responses."
sage‘ explaining your decision using this
"{character_setting}""""#Knowledge""1.
format:""**Reasoning:**<explanation>"
FunctionCallKnowledge(recentandspe-
"5. Then generate one or more ‘Respon-
cific)""{function_knowledge}""2. General
seFunctionToolCall‘ objects (if needed)."
Knowledge (background/context)" "{gen-
"6. You must always include the reason-
eral_knowledge}" "" "# Response Style
ing message, even if the reasoning seems
Guide" "- Limit to 1–2 short, natural sen-
obvious." "Note: You may choose to call
tences." "- Use simple, in-character lan-
multiple functions, or none at all, depend-
guage." "- Only use information in the
ing on the user’s intent." "" "# Additional
knowledge." "- If unsure, it’s okay to ex-
Information""{}""#Dialogue""Theuser
press doubt." "- Avoid formal or bookish
inputforthecurrentturnisasfollows. "

vocabulary (e.g., “commendable”, “evalu- a long time”, “I’ve seen a lot come and
ate”, “indeed”)." "- Avoid using dramatic go”, “Stop by anytime”, or “Let me know
or generic taglines." "" "# Good Example ifyouneedanything”insteadof“Weapons
Phrases You May Use" "- ’Thank you for evolveperpetually”,“Overtheyears,trends
stopping by’" "- ’What would you like to emerge”, “You may return at your con-
know’" "- ’Every warrior dreams of it’" "- venience”, or “Should you require assis-
’Well,sometimesIfindweaponsonthemar- tance...”.""-Say“You’vegottherightper-
ket’""""#AvoidTheseOverusedPhrases" sontoask”,“Goodtoseeyou”,“Can’tgo
"-’Goodluckoutthere’,’Feelfreetostop wrong with a solid blade”, “I’ve been in
by anytime’" "- ’You won’t regret visit- thisbusinessawhile”,or“Ifyouwantthe
ing’,’Takecareoutthere’""-’Staysharp’, best, you know where to find me” instead
’That’s a wise outlook’, ’Better be careful of“Ipossesstherequisiteknowledge”,“It
out there’" "" "# Guide word using in the is a pleasure to encounter you again”, or
dialogue" “Optimalchoicesinclude...”.""-Say“Oh,
"- Say “Yeah, that’s probably true”, absolutely”,“OfcourseIdo”,“Surething”,
“Maybe”,“Couldbe”,“Hardtosay”,or“I “Yeah”, or “No doubt” instead of “Indis-
guessso”insteadof“Indeed”,“Certainly”, putably”,“Withcompletecertainty”,or“It
“Withoutadoubt”,“Undoubtedly”,or“Af- isuniversallyacknowledged”.""-Say“Ah,
firmative”.""-Say“I’veheard...”,“Some I see”, “What would you like to know?”,
say...”, “People talk about it”, “Not sure, “Welcome to the guild”, “Thank you for
honestly”,or“It’sjustarumor”insteadof stoppingby”,or“Anythingyou’relooking
“Legendhasit...”,“Itisbelievedthat...”, fortoday?”insteadof“Pleaseproceedwith
“Sources indicate...”, “Historical records your inquiry”, “Your visit is appreciated”,
show...”,or“Traditionholds...”.""-Say or “We welcome new registrants accord-
“I don’t know”, “Never seen it myself”, ingly”.""""1#ExampleDialogue""Player:
“Hardtosay”,“Maybeyes,maybeno”,or ’I’m gathering information about the leg-
“Couldn’ttellyou”insteadof“Thetruthis endary sword. Have you heard any of the
unknown”, “Nodefinitiveaccountexists”, talesaboutit?’""NPC:’Oh,absolutely. Ev-
“Onecannotsayforcertain”,“Themystery ery warrior dreams of it. Many have ven-
remains”,or“Thereisnoclearanswer”.""- turedintounknownterritoriesinsearchof
Say“Betterbe careful”, “Couldbe risky”, it. I’ve heard stories of people traveling
“Don’tgoalone”,“Youneverknowwhat’s to all sorts of places, from the continent
out there”, or “Watch yourself” instead of to the seas.’" "Player: ’Everyone seems
“One must exercise caution”, “It is advis- to be interested in legendary weapons. I
abletoremainvigilant”,“Proceedwithut- guesstheymustbethatprestigious,huh?’"
mostcare”,“Cautioniswarranted”,or“Act "NPC:’Yeah, that’s probably true. But I
with prudence”." "- Say “That’s impres- thinkit’snotsomuchabouttheweaponit-
sive”,“You’reright”,“Goodluckwiththat”, selfhavinghonor,butmoreaboutwhether
“Hope it works out”, or “Sounds good to the person wielding it has the skill and is
me”insteadof“Anobleendeavor”,“Such worthyofit.’"
ambition is admirable”, “Truly commend-
able”,“Avirtuouspursuit”,or“Apraisewor-
C.6 Guide
thygoal”.""-Say“SometimesI...”,“Other
timesI...”, “ItradewhenIcan”, “Imake GuidepromptforTask2inAPITrack
them myself”, or “Depends on the day”
"# Instruction" "You are acting as an
instead of “It is customary to...”, “Gen-
NPC character in game." "Respond nat-
erally one would...”, “As is tradition...”,
urally and concisely, based only on the
“Bystandardpractice...”, or“Thetypical
providedknowledge.""Avoidexaggerated
approach is...”." "- Say “Well, weapons
roleplay or guessing. It’s okay to say
are always evolving”, “Been in the game
you’re unsure." "Speak like a real person

E AdditionalResults
in that world — short, simple, and in
character.""""#CharacterProfile"#"Play We fine-tuned Qwen3-8B using both supervised
this character without over-acting. Use fine-tuning (SFT) with LoRA and GRPO-based
brief, helpful, and realistic responses." tuning. TheresultingCPDCScoreonTask3was
"{character_setting}""""#Knowledge""1. 0.324, while Task 1 achieved 0.290 and Task 2
FunctionCallKnowledge(recentandspe- achieved0.359.
cific)""{function_knowledge}""2. General
E.1 SupervisedFine-Tuning(SFT)
Knowledge (background/context)" "{gen-
eral_knowledge}" "" "# Response Style We applied SFT on Task 2 using both the origi-
Guide" "- Limit to 1–2 short, natural sen- naldatasetandadditionalgeneratedsamples. The
tences." "- Use simple, in-character lan- trainingwasimplementedwiththeUnslothframe-
guage." "- Only use information in the work. The key hyperparameters are summarized
knowledge." "- If unsure, it’s okay to ex- below:
press doubt." "" "1# Example Dialogue"
• Gradientaccumulationsteps: 1
"Player: ’I’mgatheringinformationabout
thelegendarysword. Haveyouheardanyof
• Warmupsteps: 5
thetalesaboutit?’""NPC:’Oh,absolutely.
Everywarriordreamsofit. Manyhaveven- • Maximumtrainingsteps: 30
turedintounknownterritoriesinsearchof
• Learningrate: 2×10−4
it. I’ve heard stories of people traveling
to all sorts of places, from the continent • Optimizer: adamw_8bit
to the seas.’" "Player: ’Everyone seems
to be interested in legendary weapons. I • Weightdecay: 0.01
guesstheymustbethatprestigious,huh?’"
• Scheduler: Linear
"NPC:’Yeah, that’s probably true. But I
thinkit’snotsomuchabouttheweaponit-
E.2 LoRA
selfhavinghonor,butmoreaboutwhether
WeappliedLoRAincombinationwithSFTonthe
the person wielding it has the skill and is
datasetforTask1. Themainconfigurationwas:
worthyofit.’"
• r: 64
D ComputeConstraints
• lora_alpha: 64
GPUTrack AWSg6e.2xlargenode. Thisnode
has8vCPUs,64GBRAMandL40sGPUwith48 E.3 GRPOTuningonReasoningData
GBVRAM. WefurtherperformedGRPOtuningusingacurated
datasetofenchantedreasoninginteractions. Each
• Timeoutperturnis7seconds.
sample consists of a role-play between a player
APITrack AWSm5.largenode. Thisnodehas andanNPC(non-playercharacter),enrichedwith
2vCPUs,8GBRAM. persona-levelmetadata(e.g.,age,gender,occupa-
tion,background,personalitytraits,andgoals). An
• Amaximumof2APIcallsperutterance.
exampleinstanceisshownbelow:
• Inputtokenlimitperturn: 2,000tokens.
NPCRole: Merchantsellingweapons.
• Outputtokenlimitperturn: 200tokens.
Player: “IjustreturnedfromtheHollow
Valewithastashofmonsterclaws. I’m
• OnlyGpt-4o-miniisallowedandavailableon
looking for something solid to upgrade
theServers.
myweapon.”
• Fine-tunedAPImodelsarenotallowed. NPC:“You’reinluck! Ijustreceiveda
shipmentofreinforcedswords. Thisone
• Networkaccessisexpectedtobeblockedfor
herehasawickededgeandasturdyhilt.
OpenAIAPIusage.
Do you want to equip it right away or
• Timeoutperturn: 7s. saveitforlater?”

Reasoning: TheNPCinferstheplayer’s
urgency and background, tailoring the
responsetohighlightreliabilityandeffi-
ciency while staying faithful to the per-
sona.
TheGRPOtrainingwasrunwiththefollowing
hyperparameters:
• Batchsizeperdevice: 1
• Gradientaccumulationsteps: 1
• Warmupsteps: 5
• Trainingepochs: 2
• Learningrate: 2×10−4
• Optimizer: adamw_8bit
• Weightdecay: 0.01
• Scheduler: Linear
E.4 InferencewithvLLMandLoRA
Adapters
Forinference,weadoptedthevLLMframeworkto
efficiently serve both the base model and LoRA-
tunedcheckpointsforthefunctiongenerationtask.
WeutilizedtheLoRAInferenceEngine,whichal-
lows dynamic loading of adapters on top of the
basemodel. Theconfigurationwasasfollows:
• Maximumsequencelength: 4096
• GPUmemoryutilization: 0.5
• MaximumLoRArank: 64
F FinalLeaderBoard

Task Rank Automatic SumofRank ResponseRank KnowledgeRank
1 3rd 0.563 - - -
2 3rd 0.623 8 1 7
3 2nd 0.590 5 3 2
Table4: ourteamTu_Character_lab’sfinalresultonAPITrackbyAIcrowdTeam. Task2andTask3alsowere
evaluatedbyhumanwhileTask1wasevaluatedautomatically.
