Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/07_Evaluation_Methodology/02_LLM_as_Judge_MT_Bench_Zheng2023_NeurIPS.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:08:45+00:00
- page_count: 29
- status: ok
- text_char_count: 80514

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- MT-Bench and Chatbot Arena (page 3)
  - Motivation (page 3)
  - MT-Bench (page 3)
  - Chatbot Arena (page 4)
- LLM as a Judge (page 4)
  - Types of LLM-as-a-Judge (page 4)
  - Advantages of LLM-as-a-Judge (page 4)
  - Limitations of LLM-as-a-Judge (page 4)
  - Addressing limitations (page 6)
  - Multi-turn judge (page 6)
- Agreement Evaluation (page 7)
  - Setup (page 7)
  - High agreement between GPT-4 and humans (page 7)
  - Win rates under different judges (page 8)
- Human Preference Benchmark and Standardized Benchmark (page 9)
- Discussion (page 9)
- Conclusion (page 10)
- Prompt templates (page 14)
- Case Study (page 18)
- Data Collection (page 23)
  - MT-bench human evaluation (page 23)
  - Chatbot Arena (page 24)
  - Data Release (page 24)
- Additional Experimental Results (page 25)
  - Position bias (page 25)
  - Few-shot judge (page 26)
  - Agreement Evaluation (page 26)
  - Category-wise scores with single-answer grading (page 26)
- Training Details of Vicuna Models (page 28)
- Exploring Vicuna as a judge (page 29)
  - Zero-Shot Vicuna (page 29)
  - Arena Fine-tuned Vicuna (page 29)

Markdown Content:

Judging LLM-as-a-Judge
with MT-Bench and Chatbot Arena
LianminZheng1∗ Wei-LinChiang1∗ YingSheng4∗ SiyuanZhuang1
ZhanghaoWu1 YonghaoZhuang3 ZiLin2 ZhuohanLi1 DachengLi13
EricP.Xing35 HaoZhang12 JosephE.Gonzalez1 IonStoica1
1UCBerkeley 2UCSanDiego 3CarnegieMellonUniversity 4Stanford 5MBZUAI
Abstract
Evaluatinglargelanguagemodel(LLM)basedchatassistantsischallengingdueto
theirbroadcapabilitiesandtheinadequacyofexistingbenchmarksinmeasuring
humanpreferences. Toaddressthis,weexploreusingstrongLLMsasjudgesto
evaluatethesemodelsonmoreopen-endedquestions. Weexaminetheusageand
limitationsofLLM-as-a-judge,includingposition,verbosity,andself-enhancement
biases,aswellaslimitedreasoningability,andproposesolutionstomitigatesome
ofthem.WethenverifytheagreementbetweenLLMjudgesandhumanpreferences
byintroducingtwobenchmarks: MT-bench,amulti-turnquestionset;andChatbot
Arena,acrowdsourcedbattleplatform. OurresultsrevealthatstrongLLMjudges
likeGPT-4canmatchbothcontrolledandcrowdsourcedhumanpreferenceswell,
achieving over 80% agreement, the same level of agreement between humans.
Hence,LLM-as-a-judgeisascalableandexplainablewaytoapproximatehuman
preferences,whichareotherwiseveryexpensivetoobtain. Additionally,weshow
ourbenchmarkandtraditionalbenchmarkscomplementeachotherbyevaluating
severalvariantsofLLaMAandVicuna. TheMT-benchquestions,3Kexpertvotes,
and30Kconversationswithhumanpreferencesarepubliclyavailableathttps:
//github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge.
1 Introduction
There has been a proliferation of LLM-based chat assistants (chatbots) that leverage supervised
instruction fine-tuning and reinforcement learning with human feedback (RLHF) to unlock new
instruction following and conversational abilities [31, 2, 30, 8, 52, 48, 14]. Once aligned with
humans,thesechatmodelsarestronglypreferredbyhumanusersovertheoriginal,unalignedmodels
onwhichtheyarebuilt. However,theheighteneduserpreferencedoesnotalwayscorrespondto
improvedscoresontraditionalLLMbenchmarks–benchmarkslikeMMLU[19]andHELM[24]
cannot effectively tell the difference between these aligned models and the base models. This
phenomenon suggests that there is a fundamental discrepancy between user perceptions of the
usefulnessofchatbotsandthecriteriaadoptedbyconventionalbenchmarks.
WearguethatthisdiscrepancyprimarilyarisesduetoexistingevaluationthatonlymeasuresLLMs’
core capability on a confined set of tasks (e.g., multi-choice knowledge or retrieval questions),
withoutadequatelyassessingitsalignmentwithhumanpreferenceinopen-endedtasks,suchasthe
abilitytoaccuratelyadheretoinstructionsinmulti-turndialogues. Asademonstration,weshow
∗Jointfirstauthors.Thispaperisanextendedversionofourearlierblogpost[8].
37thConferenceonNeuralInformationProcessingSystems(NeurIPS2023)TrackonDatasetsandBenchmarks.
3202
ceD
42
]LC.sc[
4v58650.6032:viXra

Question:If the FED buys bonds in the secondary market
(A) the money supply will increase. (B) the money supply will decrease. (C) the money supply will not be
affected. (D) the discount rate would be affected. Output the answer only.
Assistant A: Assistant B:
The Federal Reserve buys (A) the money supply will increase.
bonds in the secondary
market to increase the
money supply.
Follow-up Question: How does it affect my daily life? Give 3 examples.
Assistant A: Assistant B:
The Federal Reserve buys When the Federal Reserve buys bonds in the secondary market, it can have
bonds in the secondary several effects on the economy that can impact your daily life. Here are
market to increase the three examples:
money supply. This
affects your daily life 1. Interest rates: The Federal Reserve's actions in the bond market can
by: influence interest rates, which in turn can affect the cost of borrowing
1. Increasing the money money. For example, if the Federal Reserve buys bonds and drives up demand
supply. for them, interest rates on things like mortgages, car loans, and credit
2. Increasing the money cards may go up, making it more expensive to borrow money.
supply and lowering the 2. Inflation: When the money supply increases, it can lead to inflation,
discount rate. which is the general rise in prices of goods and services. This can impact
3. Increasing the money your daily life by making it more expensive to buy things like groceries,
supply and lowering the gas, and other necessities.
discount rate and 3. Employment: The Federal Reserve's actions in the bond market can also
increasing the money have an impact on employment. For example, if the Federal Reserve's
supply. actions lead to economic growth and increased demand for goods and
services, it can create more job opportunities and boost employment.
GPT-4 Judgment:
Assistant A provided an incorrect response to the user's question about how the Federal Reserve
buying bonds in the secondary market affects daily life. The answer given is repetitive and lacks
clear examples of how the action impacts daily life.
On the other hand, Assistant B provided a relevant and accurate response to the user's question about
the Federal Reserve buying bonds. The answer includes three clear examples of how the action impacts
daily life, such as interest rates, inflation, and employment.
Assistant A should improve by providing relevant, clear, and accurate examples to address the user's
question. Assistant B's response is more helpful, relevant, and detailed.
Figure1: Multi-turndialoguesbetweenauserandtwoAIassistants—LLaMA-13B(AssistantA)
andVicuna-13B(AssistantB)—initiatedbyaquestionfromtheMMLUbenchmarkandafollow-up
instruction. GPT-4isthenpresentedwiththecontexttodeterminewhichassistantanswersbetter.
conversation histories with two models on an MMLU question in Figure 1. The two models are
LLaMA-13B[39],apre-trainedbasemodelwithoutfine-tuning,andVicuna-13B,ourfine-tuned
model from LLaMA-13B on high-quality conversations (the training details are in Appendix E).
DespitethebaseLLaMAmodelsshowingcompetitiveperformanceonconventionalbenchmarks
(Table8),itsanswerstoopen-endedquestionsareoftennotpreferredbyhumans. Thismisalignment
ofconventionalbenchmarksunderscoresthecoreproblemdrivingthispaper: theneedforarobust
andscalableautomatedmethodtoevaluateLLMalignmentwithhumanpreferences.
Tostudythis,weintroducetwobenchmarkswithhumanratingsastheprimaryevaluationmetric:
MT-benchandChatbotArena. MT-benchisaseriesofopen-endedquestionsthatevaluateachatbot’s
multi-turnconversationalandinstruction-followingability–twocriticalelementsforhumanprefer-
ence. MT-benchisalsocarefullyconstructedtodifferentiatechatbotsbasedontheircorecapabilities,
suchasreasoningandmath. Inaddition,wedevelopChatbotArena,acrowdsourcedplatformfea-
turinganonymousbattlesbetweenchatbotsinreal-worldscenarios–Usersengageinconversations
withtwochatbotsatthesametimeandratetheirresponsesbasedonpersonalpreferences.
Whilehumanevaluationisthegoldstandardforassessinghumanpreferences,itisexceptionallyslow
andcostly. Toautomatetheevaluation,weexploretheuseofstate-of-the-artLLMs,suchasGPT-4,
asasurrogateforhumans. BecausethesemodelsareoftentrainedwithRLHF,theyalreadyexhibit
stronghumanalignment. Wecallthisapproach“LLM-as-a-judge”. Thisapproachhasbeentriedin
ourearlierblogpost[8]andotherconcurrentorfollow-upwork[5,29,14,12,52,18,33,40,7,43].
However,therehasnotbeenasystematicstudyofthisapproach.
In this paper, we study the LLM-as-a-judge approach by comparing it to the gold standard of
human evaluation. We examine several potential limitations of the LLM-as-a-judge approach
includingpositionbias, verbositybias, self-enhancementbias, andlimitedreasoningability. We
showthatsomeofthebiasesareminororcanbemitigated. Onceaddressed,ourresultsfrom3K
controlledexpertvotesand3KcrowdsourcedhumanvotesinthewildverifythatGPT-4judgematch
2

humanevaluationsatanagreementrateexceeding80%,achievingthesamelevelofhuman-human
agreement (§4.2, Table 4). Consequently, this suggests LLM-as-a-judge is a scalable method to
swiftlyevaluatehumanpreference,servingasapromisingalternativetotraditionalhumanevaluations.
This paper makes two contributions: (1) a systematic study of LLM-as-a-judge; and (2) human
preferencedatasetswithhigh-qualityquestionsanddiverseuserinteractionsfromMT-benchand
ChatbotArena. Inaddition,wearguefortheadoptionofahybridevaluationframeworkforfuture
LLMbenchmarks: bycombiningtheexistingcapability-basedbenchmarksandthenewpreference-
basedbenchmarkswithLLM-as-a-judge,onecanswiftlyandautomaticallyevaluateboththecore
capabilitiesandhumanalignmentofmodels. Wepubliclyrelease80MT-benchquestions,3Kexpert
votes,and30Kconversationswithhumanpreferencesforfuturestudy.
Table1: Samplemulti-turnquestionsinMT-bench.
Category SampleQuestions
1stTurn ComposeanengagingtravelblogpostaboutarecenttriptoHawaii,highlighting
Writing
culturalexperiencesandmust-seeattractions.
2ndTurn Rewriteyourpreviousresponse.StarteverysentencewiththeletterA.
1stTurn Giventhatf(x)=4x3−9x−14,findthevalueoff(2).
Math
2ndTurn Findxsuchthatf(x)=0.
1stTurn ProvideinsightsintothecorrelationbetweeneconomicindicatorssuchasGDP,
Knowledge
inflation,andunemploymentrates.Explainhowfiscalandmonetarypolicies...
2ndTurn Now,explainthemagainlikeI’mfive.
2 MT-BenchandChatbotArena
2.1 Motivation
WiththerecentadvancesofLLMs,LLM-basedassistantsstarttoexhibitartificialgeneralintelligence
acrossdiversetasks,fromwritingandchattingtocoding[5,30,1,37]. However,evaluatingtheir
broadcapabilitiesalsobecomesmorechallenging. Despitetheavailabilityofnumerousbenchmarks
forlanguagemodels,theyprimarilyfocusonevaluatingmodelsonclosed-endedquestionswithshort
responses. Giventhatthesechatassistantscannowpreciselyfollowuserinstructionsinmulti-turn
dialoguesandansweropen-endedquestionsinazero-shotmanner,currentbenchmarksareinadequate
forassessingsuchcapabilities. Existingbenchmarksmostlyfallintothefollowingthreecategories.
• Core-knowledge benchmarks, including MMLU [19], HellaSwag [50], ARC [9], Wino-
Grande[36],HumanEval[6],GSM-8K[10],andAGIEval[51],evaluatethecorecapabilitiesof
pre-trainedLLMsusingzero-shotandfew-shotbenchmarksets. TheytypicallyrequireLLMsto
generateashort,specificanswertobenchmarkquestionsthatcanbeautomaticallyvalidated.
• Instruction-followingbenchmarks,suchasFlan[27,46],Self-instruct[44],NaturalInstruc-
tions[28],Super-NaturalInstructions[45],expandtoslightlymoreopen-endedquestionsand
morediversetasksandareusedtoevaluateLLMsafterinstructionfine-tuning.
• Conversationalbenchmarks, likeCoQA[35], MMDialog[15]andOpenAssistant[23], are
closesttoourintendedusecases. However,thediversityandcomplexityoftheirquestionsoften
fallshortinchallengingthecapabilitiesofthelatestchatbots.
WhilelargelyoverlookedbyexistingLLMbenchmarks,humanpreferencesserveasadirectmeasure
of a chatbot’s utility in open-ended, multi-turn human-AI interactions. To bridge this gap, we
introducetwonovelbenchmarksexpresslytailoredtoassesshumanpreferences. Simultaneously,
thesebenchmarksaredesignedtodistinguishthecorecapabilitiesofstate-of-the-artmodels.
2.2 MT-Bench
WecreateMT-bench,abenchmarkconsistingof80high-qualitymulti-turnquestions. MT-benchis
designedtotestmulti-turnconversationandinstruction-followingability,coveringcommonusecases
andfocusingonchallengingquestionstodifferentiatemodels. Weidentify8commoncategories
of user prompts to guide its construction: writing, roleplay, extraction, reasoning, math, coding,
3

knowledgeI(STEM),andknowledgeII(humanities/socialscience). Foreachcategory, wethen
manuallydesigned10multi-turnquestions. Table1listsseveralsamplequestions.
2.3 ChatbotArena
OursecondapproachisChatbotArena,acrowdsourcingbenchmarkplatformfeaturinganonymous
battles. Onthisplatform, userscaninteractwithtwoanonymousmodelssimultaneously, posing
thesamequestiontoboth. Theyvoteforwhichmodelprovidesthepreferredresponse, withthe
identitiesofthemodelsdisclosedpost-voting. AfterrunningChatbotArenaforonemonth,wehave
collectedaround30Kvotes.Sincetheplatformdoesnotusepre-definedquestions,itallowsgathering
awiderangeofunrestrictedusecasesandvotesinthewild,basedonthediverseinterestsofusers. A
screenshotoftheplatformcanbefoundatAppendixC.2.
3 LLMasaJudge
WhileourinitialevaluationsusingMT-benchandChatbotArenarelyonhumanratings,collecting
human preferences can be costly and laborious [44, 38, 31, 2, 13]. To overcome this, we aim to
developamorescalableandautomatedapproach.GiventhatmostquestionsinMT-benchandChatbot
Arenaareopen-endedwithoutreferenceanswers,devisingarule-basedprogramtoassesstheoutputs
isextremelychallenging. Traditionalevaluationmetricsbasedonthesimilaritybetweenoutputsand
referenceanswers(e.g.,ROUGE[25],BLEU[32])arealsoineffectiveforthesequestions.
AsLLMscontinuetoimprove,theyshowpotentialinreplacinghumanannotatorsinmanytasks[17,
20]. Specifically,weareinterestedinwhetherLLMscaneffectivelyevaluatetheresponsesofchat
assistantsandmatchhumanpreferences. Next,wediscusstheuseandlimitationsofLLM-as-a-judge.
3.1 TypesofLLM-as-a-Judge
Wepropose3LLM-as-a-judgevariations. Theycanbeimplementedindependentlyorincombination:
• Pairwisecomparison. AnLLMjudgeispresentedwithaquestionandtwoanswers,andtasked
todeterminewhichoneisbetterordeclareatie. ThepromptusedisgiveninFigure5(Appendix).
• Singleanswergrading. Alternatively, anLLMjudgeisaskedtodirectlyassignascoretoa
singleanswer. ThepromptusedforthisscenarioisinFigure6(Appendix).
• Reference-guidedgrading. Incertaincases,itmaybebeneficialtoprovideareferencesolution
ifapplicable. AnexamplepromptweuseforgradingmathproblemsisinFigure8(Appendix).
These methods have different pros and cons. For example, the pairwise comparison may lack
scalability when the number of players increases, given that the number of possible pairs grows
quadratically;singleanswergradingmaybeunabletodiscernsubtledifferencesbetweenspecific
pairs,anditsresultsmaybecomeunstable,asabsolutescoresarelikelytofluctuatemorethanrelative
pairwiseresultsifthejudgemodelchanges.
3.2 AdvantagesofLLM-as-a-Judge
LLM-as-a-judgeofferstwokeybenefits: scalabilityandexplainability. Itreducestheneedforhuman
involvement,enablingscalablebenchmarksandfastiterations. Additionally,LLMjudgesprovide
notonlyscoresbutalsoexplanations,makingtheiroutputsinterpretable,asshowninFigure1.
3.3 LimitationsofLLM-as-a-Judge
WeidentifycertainbiasesandlimitationsofLLMjudges. However,wewillalsopresentsolutions
laterandshowtheagreementbetweenLLMjudgesandhumansishighdespitetheselimitations.
Position bias is when an LLM exhibits a propensity to favor certain positions over others. This
biasisnotuniquetoourcontextandhasbeenseeninhumandecision-making[3,34]andotherML
domains[22,41].
Figure11(Appendix)showsanexampleofpositionbias. GPT-4istaskedtoevaluatetworesponses
fromGPT-3.5andVicuna-13Btoanopen-endedquestion. WhenGPT-3.5’sanswerispositioned
4

Table 2: Position bias of different LLM judges. Consistency is the percentage of cases where a
judgegivesconsistentresultswhenswappingtheorderoftwoassistants. “Biasedtowardfirst”isthe
percentageofcaseswhenajudgefavorsthefirstanswer. “Error”indicateswrongoutputformats.
Thetwolargestnumbersineachcolumnareinbold.
Judge Prompt Consistency Biasedtowardfirst Biasedtowardsecond Error
default 23.8% 75.0% 0.0% 1.2%
Claude-v1 rename 56.2% 11.2% 28.7% 3.8%
default 46.2% 50.0% 1.2% 2.5%
GPT-3.5 rename 51.2% 38.8% 6.2% 3.8%
default 65.0% 30.0% 5.0% 0.0%
GPT-4 rename 66.2% 28.7% 5.0% 0.0%
Table4: Judgefailurerateon10mathquestions
Table3: Failurerateunder“repetitivelist”at- withdifferentprompts. WetestLLaMA-13Bvs.
tackfordifferentLLMjudgeson23answers. Vicuna-13Bandswappositions. Afailuremeans
whenGPT-4saysanincorrectansweriscorrect.
Judge Claude-v1 GPT-3.5 GPT-4
Default CoT Reference
Failurerate 91.3% 91.3% 8.7%
Failurerate 14/20 6/20 3/20
first,GPT-4considersGPT-3.5’sanswermoredetailedandsuperior. However,uponswitchingthe
positionsofthetworesponses,GPT-4’sjudgementflips,favoringVicuna’sanswer.
Toanalyzethepositionbias,weconstructtwosimilaranswerstoeachfirst-turnquestioninMT-bench
by calling GPT-3.5 twice with a temperature of 0.7. We then try three LLMs with two different
prompts: “default”isourdefaultpromptinFigure5(Appendix). “rename”renamestheassistantsin
ourdefaultprompttoseewhetherthebiasisonpositionsornames. AsinTable2,wefoundallof
themexhibitstrongpositionbias. MostLLMjudgesfavorthefirstposition. Claude-v1alsoshowsa
namebiaswhichmakesitfavors"AssistantA",asillustratedbythe"rename"prompt. Theposition
biascanbeverysignificant. OnlyGPT-4outputsconsistentresultsinmorethan60%ofcases.
Notethatthistestischallengingbecausetheanswersareverysimilarandoccasionallyindistinguish-
ableeventohumans.WewillshowthatpositionbiasislessprominentinsomecasesinAppendixD.1.
Asfortheoriginofthisbias,wesuspectthatitcouldberootedinthetrainingdataorinherenttothe
left-to-rightarchitectureofcausaltransformers,butleaveadeeperstudyasfuturework.
VerbositybiasiswhenanLLMjudgefavorslonger,verboseresponses,eveniftheyarenotasclear,
high-quality,oraccurateasshorteralternatives.
Toexaminethisbias,wedesigna“repetitivelist”attackwithmodelanswersfromMT-bench. We
first select 23 model answers from MT-bench that contain a numbered list. We then make them
unnecessarilyverbosebyaskingGPT-4torephrasethelistwithoutaddinganynewinformationand
inserttherephrasednewlisttothebeginningoftheoriginallist. Forexample,iftheoriginalresponse
contains5items,thenthenewresponsewillcontain10itemsbutthefirst5itemsarerephrasedfrom
theoriginal5items. AnexampleisshowninFigure12(Appendix). Wedefinetheattackissuccessful
ifanLLMjudgethinksthenewresponseisbetterthantheoldresponse. Table3showsthefailure
rateofLLMjudgesunderthisattack,demonstratingthatallLLMsmaybepronetoverbositybias
thoughGPT-4defendssignificantlybetterthanothers. Asacalibration,wefindLLMjudgesare
abletocorrectlyjudgeidenticalanswers(i.e.,theyalwaysreturnatiefortwoidenticalanswers)but
cannotpassthemoreadvanced“repetitivelist”attack.
Self-enhancementbias. Weadopttheterm“self-enhancementbias”fromsocialcognitionlitera-
ture[4]todescribetheeffectthatLLMjudgesmayfavortheanswersgeneratedbythemselves.
Weexaminethiseffectstatistically. Figure3(b)showsthewinrate(w/otie)ofsixmodelsunder
differentLLMjudgesandhumans. Comparedtohumans, wedoobservethatsomejudgesfavor
certainmodels. Forexample,GPT-4favorsitselfwitha10%higherwinrate;Claude-v1favorsitself
witha25%higherwinrate. However,theyalsofavorothermodelsandGPT-3.5doesnotfavoritself.
Duetolimiteddataandsmalldifferences,ourstudycannotdeterminewhetherthemodelsexhibit
aself-enhancementbias. Conductingacontrolledstudyischallengingbecausewecannoteasily
rephrasearesponsetofitthestyleofanothermodelwithoutchangingthequality.
5

Limitedcapabilityingradingmathandreasoningquestions. LLMsareknowntohavelimited
mathandreasoningcapability[10],whichresultsinitsfailureofgradingsuchquestionsbecausethey
donotknowthecorrectanswers. However,whatismoreintriguingisthatitalsoshowslimitationsin
gradingbasicmathproblemswhichitiscapableofsolving. Forinstance,inFigure13(Appendix),
wepresentanexampleofanelementarymathquestioninwhichGPT-4makesanincorrectjudgment.
It’sworthnotingthatalthoughGPT-4cansolvetheproblem(whenaskedseparately),itwasmisled
bytheprovidedanswers,ultimatelyresultinginincorrectjudgment. Thispatterncanalsobeseenin
areasoningquestionexampleinFigure14(Appendix). BothGPT-3.5andClaude-v1showasimilar
weakness. InSection3.4,wewillintroduceareference-guidedmethodtomitigatesuchissues.
3.4 Addressinglimitations
Wepresentafewmethodstoaddresspositionbiasandthelimitedgradingabilityformathquestions.
Swapping positions. The position bias can be addressed by simple solutions. A conservative
approachistocallajudgetwicebyswappingtheorderoftwoanswersandonlydeclareawinwhen
ananswerispreferredinbothorders. Iftheresultsareinconsistentafterswapping,wecancallita
tie. Anothermoreaggressiveapproachistoassignpositionsrandomly,whichcanbeeffectiveata
largescalewiththecorrectexpectations. Inthefollowingexperiments,weusetheconservativeone.
Few-shotjudge. Weassesswhetherfew-shotexamplescanimproveconsistencyinthepositionbias
benchmark. WeselectthreegoodjudgmentexamplesusingMT-bench-likequestions,GPT-3.5and
Vicunaforgeneratinganswers,andGPT-4forgeneratingjudgments. Theexamplescoverthreecases:
Aisbetter,Bisbetter,andtie. AsshowninTable12(Appendix),thefew-shotjudgecansignificantly
increasetheconsistencyofGPT-4from65.0%to77.5%. However,highconsistencymaynotimply
highaccuracyandwearenotsurewhetherthefew-shotexampleswillintroducenewbiases. Besides,
thelongerpromptsmakeAPIcalls4×moreexpensive. Weusethezero-shotpromptbydefaultin
ourfollowingexperimentsbutleaveanadditionalstudyinAppendixD.2.
Chain-of-thoughtandreference-guidedjudge. InSection3.3,wehaveshownLLM’slimited
capabilityingradingmathandreasoningquestions. Weproposetwosimplemethodstomitigate
thisissue: chain-of-thoughtjudgeandreference-guidedjudge. Chain-of-thoughtisawidelyused
techniquetoimproveLLM’sreasoningcapability[47]. Weproposeasimilartechniquetoprompt
anLLMjudgetobeginwithansweringthequestionindependentlyandthenstartgrading. Detailed
promptinFigure7(Appendix). However,evenwiththeCoTprompt,wefindthatinmanycases
LLM makes exactly the same mistake as the given answers in its problem-solving process (See
exampleinFigure15(Appendix),suggestingthatLLMjudgemaystillbemisledbythecontext.
Hence, we propose a reference-guided method, in which we first generate LLM judge’s answer
independently,andthendisplayitasareferenceanswerinthejudgeprompt. InTable4,weseea
significantimprovementinfailurerate(from70%to15%)overthedefaultprompt.
Fine-tuningajudgemodel. Wetryfine-tuningaVicuna-13Bonarenadatatoactasajudgeand
showsomepromisingpreliminaryresultsinAppendixF.
3.5 Multi-turnjudge
InMT-bench,everyquestioninvolvestwoturnstoevaluateconversationalabilities. Therefore,when
comparingtwoassistants,itbecomesnecessarytopresentatotaloftwoquestionsandfourresponses,
complicatingthepromptdesign. Weexploretwopossibledesigns,(1)breakingthetwoturnsintotwo
promptsor(2)displayingcompleteconversationsinasingleprompt. Ourfindingistheformerone
cancausetheLLMjudgestrugglingtolocatetheassistant’spreviousresponseprecisely. Weillustrate
acaseinFigure16(Appendix)whereGPT-4makesaninaccuratejudgmentduetoafaultyreference.
ThissuggeststhenecessityofdisplayingacompleteconversationtoenabletheLLMjudgetobetter
graspthecontext. Wethenconsiderthealternativedesignthatpresentstwofullconversationsina
singlepromptinwhichweasktheLLMjudgetofocusonthesecondquestion(Figure9(Appendix)).
Thisapproachhasbeenfoundtosignificantlyalleviatetheaforementionedreferencingissue.
6

4 AgreementEvaluation
We study the agreement between different LLM judges and humans on MT-bench and Chatbot
Arenadatasets. OnMT-bench,wealsostudytheagreementamonghumans. MT-benchrepresentsa
small-scalestudywithcontrolledhumanevaluation,whileChatbotArenarepresentsalarger-scale
studywithcrowdsourcedhumanevaluationinthewild.
4.1 Setup
MT-bench. Wegenerateanswersforall80questionswith6models: GPT-4,GPT-3.5,Claude-V1,
Vicuna-13B,Alpaca-13B[38],andLLaMA-13B[39]. Wethenuse2kindsofjudges: LLMjudges
and58expert-levelhumanlabelers. Thelabelersaremostlygraduatestudentssotheyareconsidered
expertsandmoreskilledthanaveragecrowdworkers. WeletLLMjudgesevaluateallpairsandlet
eachhumanevaluateatleast20randommulti-turnquestions. Thisresultedinaround3Kvotesforall
questions. ThedetaileddatacollectionprocessisinAppendixC.
Chatbot Arena. We randomly sample 3K single-turn votes from 30K arena data, which covers
modelsincludingGPT-4,GPT-3.5,Claude,Vicuna-7B/13B,Koala-13B[16],Alpaca-13B,LLaMA-
13B,andDolly-12B.Weusetwokindsofjudges: LLMjudgesandcollectedcrowdjudges(2114
uniqueIPs).
Metrics. We define the agreement between two types of judges as the probability of randomly
selectedindividuals(butnotidentical)ofeachtypeagreeingonarandomlyselectedquestion. See
moreexplanationinAppendixD.3. Averagewinrateistheaverageofwinratesagainstallother
players. Thesemetricscanbecomputedwithorwithoutincludingtievotes.
4.2 HighagreementbetweenGPT-4andhumans
WecomputeagreementonMT-benchdata. InTable5,GPT-4withbothpairwisecomparisonand
singleanswergradingshowveryhighagreementswithhumanexperts. TheagreementundersetupS2
(w/otie)betweenGPT-4andhumansreaches85%,whichisevenhigherthantheagreementamong
humans(81%). ThismeansGPT-4’sjudgmentscloselyalignwiththemajorityofhumans. Wealso
showthatGPT-4’sjudgmentsmayhelphumansmakebetterjudgments. Duringourdatacollection,
whenahuman’schoicedeviatedfromGPT-4,wepresentedGPT-4’sjudgmentstohumansandask
iftheyarereasonable(detailsinAppendixC.1). Despitedifferentviews,humansdeemedGPT-4’s
judgmentsreasonablein75%ofcasesandareevenwillingtochangetheirchoicesin34%ofcases.
ThedatafromArenashowsasimilartrend,asillustratedbyTable6. ComparingGPT-4andother
LLMjudges,wefindtheyreachasimilarnon-tieagreementratiobetweenhumansbutthenumber
ofnon-tiedvotesfromGPT-4ismuchlarger. ThismeansthatGPT-4ismoreaffirmativeandless
sufferedfrompositionbiasbutothermodelsalsoperformwellwhentheygiveanaffirmativeanswer.
Inbothtables,GPT-4withsingle-answergradingmatchesbothpairwiseGPT-4andhumanprefer-
encesverywell. ThismeansGPT-4hasarelativelystableinternalrubric. Althoughitmaysometimes
performslightlyworsethanpairwisecomparisonandgivemoretievotes,itisamorescalablemethod.
We then perform a breakdown analysis by computing agreement on different model pairs and
categories. Weonlyincludenon-tiedvotes. InFigure2,weobservetheagreementbetweenGPT-4
andhumanprogressivelyincreasesinlinewiththeperformancedisparityofthemodelpairs(i.e.,
largerwinratedifference),from70%tonearly100%. ThissuggeststhatGPT-4alignswithhumans
betterwhensignificantperformancedifferencesexistbetweenthemodels.
1.0 1.0 1.0 1.0
0.8 0.8 0.8 0.8
0.6 0.6 0.6 0.6
0.4 0.4 0.4 0.4
0.2 0.2 0.2 0.2
0.0 0.0 0.0 0.0
GPT-4 Claude GPT
V
-
i
3
cu
.5 na
A
-1
lp
3
a
B ca
L
-1
L
3
a
B MA-13B GPT-4 GPT-3.5 Cla
V
u
ic
d
u
e na
A
-1
lp
3
a
B ca
L
-1
L
3
a
B MA-13B GPT-4 Claude GPT
V
-
i
3
cu
.5 na
A
-1
lp
3
a
B ca
L
-1
L
3
a
B MA-13B GPT-4 Claude GPT
V
-
i
3
cu
.5 na
A
-1
lp
3
a
B ca
L
-1
L
3
a
B MA-13B
(a) All votes, first turn (b) Non-tied votes, first turn (c) All votes, second turn (d) Non-tied votes, second turn
etar
niW
GPT-4 Judge GPT-3.5 Judge Claude Judge Human Human (first turn)
Figure3: AveragewinrateofsixmodelsunderdifferentjudgesonMT-bench.
7

Table5: AgreementbetweentwotypesofjudgesonMT-bench. “G4-Pair”and“G4-Single”denote
GPT-4withpairwisecomparisonandsingle-answergradingrespectively. Thesingle-answergrading
can be converted into pairwise comparison results for calculating the agreement. We report two
setups:“S1”includesnon-tie,tie,andinconsistent(duetopositionbias)votesandcountsinconsistent
astie;“S2”onlyincludesnon-tievotes. Theagreementbetweentworandomjudgesundereachsetup
isdenotedas“R=”. Thetopvalueineachcellistheagreement,andthebottomgrayvalueis#votes.
Setup S1(R=33%) S2(R=50%) Setup S1(R=33%) S2(R=50%)
Judge G4-Single Human G4-Single Human Judge G4-Single Human G4-Single Human
70% 66% 97% 85% 70% 66% 95% 85%
G4-Pair 1138 1343 662 859 G4-Pair 1161 1325 727 864
60% 85% 59% 84%
G4-Single - 1280 - 739 G4-Single - 1285 - 776
63% 81% 67% 82%
Human - 721 - 479 Human - 707 - 474
(a)FirstTurn (b)SecondTurn
Table6:AgreementbetweentwotypesofjudgesonChatbot 1.0
Arena. “G4-S”denotesGPT-4withsingle-answergrading.
0.9
“G4”,“G3.5”and“C”denoteGPT-4,GPT-3.5,andClaude
withpairwisecomparison,respectively.“H”denoteshuman. 0.8
TheremainingoftablefollowsthesameformatasTable5. 0.7
Setup S1(Random=33%) S2(Random=50%) 0.0 0.5 1.0
Judge G4-S G3.5 C H G4-S G3.5 C H Win rate difference
72% 66% 66% 64% 95% 94% 95% 87%
G4 2968 3061 3062 3066 1967 1788 1712 1944
60% 62% 60% 89% 91% 85%
G4-S - 2964 2964 2968 - 1593 1538 1761
68% 54% 96% 83%
G3.5 - - 3057 3061 - - 1497 1567
53% 84%
C - - - 3062 - - - 1475
tnemeergA
Figure2: Agreementandwinratedif-
ference. Each point corresponds to a
modelpairandcountsonlythenon-tie
votesbetweenthetwomodels. Thex-
axisvalueisthewinratedifferencebe-
tweenthetwomodels.They-axisvalue
istheGPT-4andhumanagreement.
1.0 1.0
0.8 0.8
0.6 0.6
0.4 0.4
0.2 0.2
0.0 0.0
GPT-4 Claude GPT-3
V
.
i
5 cuna-13
V
B icuna-7
K
B oala-1
A
3
l
B paca-13B Dolly-1
L
2
L
B aMA-13B GPT-4 Claude GPT-3
V
.
i
5 cuna-13
V
B icuna-7
K
B oala-1
A
3
l
B paca-13B Dolly-1
L
2
L
B aMA-13B
(a) All votes (b) Non-tied votes
etar
niW
GPT-4 Judge GPT-3.5 Judge Human GPT-4-Single Judge
Figure4: AveragewinrateofninemodelsunderdifferentjudgesonChatbotArena.
Table7: Category-wisewinrateofmodels.
Model Writing Roleplay Reasoning Math Coding Extraction STEM Humanities
GPT-4 61.2% 67.9% 49.3% 66.1% 56.3% 66.2% 76.6% 72.2%
GPT-3.5 50.9% 60.6% 32.6% 63.8% 55.0% 48.8% 52.8% 53.8%
Vicuna-13B 39.7% 39.2% 20.1% 18.0% 36.9% 29.2% 47.0% 47.5%
LLaMA-13B 15.1% 15.1% 7.8% 7.5% 2.1% 9.3% 6.8% 10.1%
4.3 Winratesunderdifferentjudges
We plot the average win rate of models under different judges on MT-bench and Chatbot Arena
in Figure 3 and Figure 4, respectively. The win rate curves from LLM judges closely match the
curvesfromhumans. OnMT-benchsecondturn,proprietarymodelslikeClaudeandGPT-3.5are
morepreferredbythehumanscomparedtothefirstturn,meaningthatamulti-turnbenchmarkcan
better differentiate some advanced abilities of models. We also list the per-category win rate of
8

Table8: Evaluationresultsofseveralmodelvariants.
Model #TrainingToken MMLU(5-shot) TruthfulQA(0-shot) MT-BenchScore(GPT-4)
LLaMA-7B 1T 35.2 0.22 2.74
LLaMA-13B 1T 47.0 0.26 2.61
Alpaca-7B 4.4M 40.1 0.26 4.54
Alpaca-13B 4.4M 48.1 0.30 4.53
Vicuna-7B(selected) 4.8M 37.3 0.32 5.95
Vicuna-7B(single) 184M 44.1 0.30 6.04
Vicuna-7B(all) 370M 47.1 0.32 6.00
Vicuna-13B(all) 370M 52.1 0.35 6.39
GPT-3.5 - 70.0 - 7.94
GPT-4 - 86.4 - 8.99
representativemodelsinTable7toshowhowMT-benchdifferentiatesmodels,inwhichweseeGPT-4
issignificantlybetterthanothers. Vicuna-13BisnoticeablyworsethanGPT-3.5/4inreasoning,math,
andcodingcategories. Notethatinmath/codingcategory,GPT-3.5andGPT-4havesimilaroverall
win-ratebecausetheybothfailedtoanswersomehardquestions,butGPT-4isstillsignificantlybetter
thanGPT-3inthedirectpairwisecomparisonorsingle-answergrading. Pleaseseeaperformance
breakdownofMT-benchscoreforeachcategoryinAppendixD.4.
5 HumanPreferenceBenchmarkandStandardizedBenchmark
HumanpreferencebenchmarkssuchasMT-benchandChatbotArenaserveasvaluableadditions
tothecurrentstandardizedLLMbenchmarks. Theyfocusondifferentaspectsofamodelandthe
recommendedwayistocomprehensivelyevaluatemodelswithbothkindsofbenchmarks.
WeevaluateseveralmodelvariantsderivedfromLLaMAonMMLU[19],TruthfulQA[26](MC1),
andMT-bench(GPT-4judge). ThetrainingdetailsareinAppendixE.Sincewehaveshownthat
GPT-4single-answergradingalsoperformswellinSection4.2,weuseGPT-4single-answergrading
forMT-benchinfavorofitsscalabilityandsimplicity. WeaskGPT-4togiveascoreforeachturn
onascaleof10byusingourprompttemplates(Figure6,Figure10)andreportanaveragescoreof
160=80×2turns.Table8showstheresults.Wefindthatfine-tuningonhigh-qualitydialogdatasets
(i.e.,ShareGPT)canconsistentlyimprovethemodelperformanceonMMLUandtheimprovement
scaleswithfine-tuningdatasize. Ontheotherhand,asmallhigh-qualityconversationdatasetcan
quicklyteachthemodelastylepreferredbyGPT-4(orapproximatelyhuman)butcannotimprove
MMLUsignificantly,asshownbytheVicuna-7B(selected)whichistrainedwithonly4.8Mtokens
or3Kconversations. InTable8,nosinglebenchmarkcandeterminemodelquality,meaningthata
comprehensiveevaluationisneeded. OurresultsindicatethatusingLLM-as-a-judgetoapproximate
humanpreferencesishighlyfeasibleandcouldbecomeanewstandardinfuturebenchmarks. We
arealsohostingaregularlyupdatedleaderboardwithmoremodels2. Notably,DynaBench[21],a
researchplatformdedicatedtodynamicdatacollectionandbenchmarking, alignswithourspirit.
DynaBenchaddressesthechallengesposedbystaticstandardizedbenchmarks,suchassaturationand
overfitting,byemphasizingdynamicdatawithhuman-in-the-loop. OurLLM-as-a-judgeapproach
canautomateandscaleplatformsofthisnature.
6 Discussion
Limitations. This paper emphasizes helpfulness but largely neglects safety. Honesty and harm-
lessnessarecrucialforachatassistantaswell[2]. Weanticipatesimilarmethodscanbeusedto
evaluate these metrics by modifying the default prompt. Additionally, within helpfulness, there
aremultipledimensionslikeaccuracy, relevance, andcreativity, buttheyareallcombinedintoa
singlemetricinthisstudy. Amorecomprehensiveevaluationcanbedevelopedbyanalyzingand
separatingthesedimensions. Weproposepreliminarysolutionstoaddressthelimitationsandbiases
ofLLM-as-a-judgeinSection3.4,butweanticipatemoreadvancedmethodscanbedeveloped.
Datacollectionandrelease. AppendixCdescribesthedetaileddatacollectionandreleaseprocesses,
whichincludetheinstructionswegivetousers,thescreenshotsofthedatacollectioninterface,the
informationaboutparticipatedusers,andthecontentofthereleaseddata.
2https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard
9

Societalimpacts. Thesocietalimpactofthisstudyismulti-faceted. Ourevaluationmethodscan
helpenhancechatbotqualityanduserexperiences. However,addressingbiasesinthesemethodsis
crucial. Ourdatasetenablesbetterstudiesofhumanpreferencesandmodelbehavior. Advancedchat
assistantsmayreplacecertainhumantasks,resultinginjobdisplacementsandnewopportunities.
Futuredirections.1)Benchmarkingchatbotsatscalewithabroadersetofcategories2)Open-source
LLMjudgealignedwithhumanpreference3)Enhancingopenmodels’math/reasoningcapability.
7 Conclusion
In this paper, we propose LLM-as-a-judge for chatbot evaluation and systematically examine its
efficacyusinghumanpreferencedatafrom58expertsonMT-bench,aswellasthousandsofcrowd-
usersonChatbotArena. OurresultsrevealthatstrongLLMscanachieveanagreementrateofover
80%, on par with the level of agreement among human experts, establishing a foundation for an
LLM-basedevaluationframework.
Acknowledgement
ThisprojectispartlysupportedbygiftsfromAnyscale,Astronomer,Google,IBM,Intel,Lacework,
Microsoft,MBZUAI,SamsungSDS,Uber,andVMware. LianminZhengissupportedbyaMeta
Ph.D.Fellowship. WeextendourthankstoXinyangGeng,HaoLiu,EricWallace,XuechengLi,
TianyiZhang,QirongHo,andKevinLinfortheirinsightfuldiscussions.
References
[1] RohanAnil,AndrewMDai,OrhanFirat,MelvinJohnson,DmitryLepikhin,AlexandrePassos,
SiamakShakeri,EmanuelTaropa,PaigeBailey,ZhifengChen,etal. Palm2technicalreport.
arXivpreprintarXiv:2305.10403,2023.
[2] YuntaoBai,AndyJones,KamalNdousse,AmandaAskell,AnnaChen,NovaDasSarma,Dawn
Drain,StanislavFort,DeepGanguli,TomHenighan,etal. Trainingahelpfulandharmless
assistantwithreinforcementlearningfromhumanfeedback. arXivpreprintarXiv:2204.05862,
2022.
[3] NielsJBlunch. Positionbiasinmultiple-choicequestions. JournalofMarketingResearch,
21(2):216–220,1984.
[4] JonathonDBrown. Evaluationsofselfandothers:Self-enhancementbiasesinsocialjudgments.
Socialcognition,4(4):353–376,1986.
[5] SébastienBubeck,VarunChandrasekaran,RonenEldan,JohannesGehrke,EricHorvitz,Ece
Kamar,PeterLee,YinTatLee,YuanzhiLi,ScottLundberg,etal. Sparksofartificialgeneral
intelligence: Earlyexperimentswithgpt-4. arXivpreprintarXiv:2303.12712,2023.
[6] MarkChen,JerryTworek,HeewooJun,QimingYuan,HenriquePondedeOliveiraPinto,Jared
Kaplan,HarriEdwards,YuriBurda,NicholasJoseph,GregBrockman,etal. Evaluatinglarge
languagemodelstrainedoncode. arXivpreprintarXiv:2107.03374,2021.
[7] Cheng-HanChiangandHung-yiLee. Canlargelanguagemodelsbeanalternativetohuman
evaluations? arXivpreprintarXiv:2305.01937,2023.
[8] Wei-LinChiang,ZhuohanLi,ZiLin,YingSheng,ZhanghaoWu,HaoZhang,LianminZheng,
SiyuanZhuang,YonghaoZhuang,JosephE.Gonzalez,IonStoica,andEricP.Xing. Vicuna:
Anopen-sourcechatbotimpressinggpt-4with90%*chatgptquality,March2023.
[9] PeterClark,IsaacCowhey,OrenEtzioni,TusharKhot,AshishSabharwal,CarissaSchoenick,
andOyvindTafjord. Thinkyouhavesolvedquestionanswering? tryarc,theai2reasoning
challenge. arXivpreprintarXiv:1803.05457,2018.
[10] KarlCobbe,VineetKosaraju,MohammadBavarian,MarkChen,HeewooJun,LukaszKaiser,
MatthiasPlappert,JerryTworek,JacobHilton,ReiichiroNakano,etal. Trainingverifiersto
solvemathwordproblems. arXivpreprintarXiv:2110.14168,2021.
10

[11] TriDao,DanFu,StefanoErmon,AtriRudra,andChristopherRé. Flashattention: Fastand
memory-efficientexactattentionwithio-awareness.AdvancesinNeuralInformationProcessing
Systems,35:16344–16359,2022.
[12] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. Qlora: Efficient
finetuningofquantizedllms. arXivpreprintarXiv:2305.14314,2023.
[13] ShizheDiao,RuiPan,HanzeDong,KaShunShum,JipengZhang,WeiXiong,andTongZhang.
Lmflow: Anextensibletoolkitforfinetuningandinferenceoflargefoundationmodels. arXiv
preprintarXiv:2306.12420,2023.
[14] YannDubois,XuechenLi,RohanTaori,TianyiZhang,IshaanGulrajani,JimmyBa,Carlos
Guestrin,PercyLiang,andTatsunoriBHashimoto. Alpacafarm: Asimulationframeworkfor
methodsthatlearnfromhumanfeedback. arXivpreprintarXiv:2305.14387,2023.
[15] JiazhanFeng,QingfengSun,CanXu,PuZhao,YamingYang,ChongyangTao,DongyanZhao,
andQingweiLin. Mmdialog: Alarge-scalemulti-turndialoguedatasettowardsmulti-modal
open-domainconversation. arXivpreprintarXiv:2211.05719,2022.
[16] XinyangGeng,ArnavGudibande,HaoLiu,EricWallace,PieterAbbeel,SergeyLevine,and
DawnSong. Koala: Adialoguemodelforacademicresearch. Blogpost,April2023.
[17] FabrizioGilardi,MeysamAlizadeh,andMaëlKubli. Chatgptoutperformscrowd-workersfor
text-annotationtasks. arXivpreprintarXiv:2303.15056,2023.
[18] ArnavGudibande,EricWallace,CharlieSnell,XinyangGeng,HaoLiu,PieterAbbeel,Sergey
Levine, and Dawn Song. The false promise of imitating proprietary llms. arXiv preprint
arXiv:2305.15717,2023.
[19] DanHendrycks,CollinBurns,StevenBasart,AndyZou,MantasMazeika,DawnSong,and
Jacob Steinhardt. Measuring massive multitask language understanding. arXiv preprint
arXiv:2009.03300,2020.
[20] FanHuang,HaewoonKwak,andJisunAn. Ischatgptbetterthanhumanannotators? potential
andlimitationsofchatgptinexplainingimplicithatespeech. arXivpreprintarXiv:2302.07736,
2023.
[21] DouweKiela, MaxBartolo, YixinNie, DivyanshKaushik, AtticusGeiger, ZhengxuanWu,
BertieVidgen,GrushaPrasad,AmanpreetSingh,PratikRingshia,etal. Dynabench:Rethinking
benchmarkinginnlp. InProceedingsofthe2021ConferenceoftheNorthAmericanChapter
of the Association for Computational Linguistics: Human Language Technologies, pages
4110–4124,2021.
[22] MiyoungKo,JinhyukLee,HyunjaeKim,GangwooKim,andJaewooKang. Lookatthefirst
sentence: Positionbiasinquestionanswering. arXivpreprintarXiv:2004.14602,2020.
[23] AndreasKöpf,YannicKilcher,DimitrivonRütte,SotirisAnagnostidis,Zhi-RuiTam,Keith
Stevens,AbdullahBarhoum,NguyenMinhDuc,OliverStanley,RichárdNagyfi,etal. Ope-
nassistant conversations–democratizing large language model alignment. arXiv preprint
arXiv:2304.07327,2023.
[24] PercyLiang,RishiBommasani,TonyLee,DimitrisTsipras,DilaraSoylu,MichihiroYasunaga,
Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. Holistic evaluation of
languagemodels. arXivpreprintarXiv:2211.09110,2022.
[25] Chin-YewLin.Rouge:Apackageforautomaticevaluationofsummaries.InTextsummarization
branchesout,pages74–81,2004.
[26] StephanieLin, JacobHilton, andOwainEvans. Truthfulqa: Measuringhowmodelsmimic
humanfalsehoods. arXivpreprintarXiv:2109.07958,2021.
[27] ShayneLongpre,LeHou,TuVu,AlbertWebson,HyungWonChung,YiTay,DennyZhou,
QuocVLe,BarretZoph,JasonWei,etal. Theflancollection: Designingdataandmethodsfor
effectiveinstructiontuning. arXivpreprintarXiv:2301.13688,2023.
[28] SwaroopMishra,DanielKhashabi,ChittaBaral,andHannanehHajishirzi. Cross-taskgeneral-
izationvianaturallanguagecrowdsourcinginstructions. InACL,2022.
[29] OpenAI. Evalsisaframeworkforevaluatingllmsandllmsystems,andanopen-sourceregistry
ofbenchmarks. https://github.com/openai/evals.
[30] OpenAI. Gpt-4technicalreport,2023.
11

[31] LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,CarrollWainwright,PamelaMishkin,
ChongZhang,SandhiniAgarwal,KatarinaSlama,AlexRay,etal. Traininglanguagemodelsto
followinstructionswithhumanfeedback. AdvancesinNeuralInformationProcessingSystems,
35:27730–27744,2022.
[32] KishorePapineni,SalimRoukos,ToddWard,andWei-JingZhu. Bleu: amethodforautomatic
evaluationofmachinetranslation. InProceedingsofthe40thannualmeetingoftheAssociation
forComputationalLinguistics,pages311–318,2002.
[33] BaolinPeng,ChunyuanLi,PengchengHe,MichelGalley,andJianfengGao. Instructiontuning
withgpt-4. arXivpreprintarXiv:2304.03277,2023.
[34] PriyaRaghubirandAnaValenzuela. Center-of-inattention: Positionbiasesindecision-making.
OrganizationalBehaviorandHumanDecisionProcesses,99(1):66–80,2006.
[35] Siva Reddy, Danqi Chen, and Christopher D Manning. Coqa: A conversational question
answeringchallenge. TransactionsoftheAssociationforComputationalLinguistics,7:249–266,
2019.
[36] KeisukeSakaguchi,RonanLeBras,ChandraBhagavatula,andYejinChoi. Winogrande: An
adversarialwinogradschemachallengeatscale. CommunicationsoftheACM,64(9):99–106,
2021.
[37] Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid,
Adam Fisch, Adam R Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, et al.
Beyondtheimitationgame: Quantifyingandextrapolatingthecapabilitiesoflanguagemodels.
arXivpreprintarXiv:2206.04615,2022.
[38] RohanTaori,IshaanGulrajani,TianyiZhang,YannDubois,XuechenLi,CarlosGuestrin,Percy
Liang,andTatsunoriB.Hashimoto. Stanfordalpaca: Aninstruction-followingllamamodel.
https://github.com/tatsu-lab/stanford_alpaca,2023.
[39] HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,Timo-
théeLacroix,BaptisteRozière,NamanGoyal,EricHambro,FaisalAzhar,etal. Llama: Open
andefficientfoundationlanguagemodels. arXivpreprintarXiv:2302.13971,2023.
[40] PeiyiWang,LeiLi,LiangChen,DaweiZhu,BinghuaiLin,YunboCao,QiLiu,TianyuLiu,and
ZhifangSui. Largelanguagemodelsarenotfairevaluators. arXivpreprintarXiv:2305.17926,
2023.
[41] Xuanhui Wang, Nadav Golbandi, Michael Bendersky, Donald Metzler, and Marc Najork.
Positionbiasestimationforunbiasedlearningtorankinpersonalsearch. InProceedingsof
theEleventhACMInternationalConferenceonWebSearchandDataMining,pages610–618,
2018.
[42] YidongWang,ZhuohaoYu,ZhengranZeng,LinyiYang,CunxiangWang,HaoChen,Chaoya
Jiang,RuiXie,JindongWang,XingXie,WeiYe,ShikunZhang,andYueZhang. Pandalm: An
automaticevaluationbenchmarkforllminstructiontuningoptimization,2023.
[43] YizhongWang,HamishIvison,PradeepDasigi,JackHessel,TusharKhot,KhyathiRaghavi
Chandu,DavidWadden,KelseyMacMillan,NoahASmith,IzBeltagy,etal.Howfarcancamels
go?exploringthestateofinstructiontuningonopenresources.arXivpreprintarXiv:2306.04751,
2023.
[44] YizhongWang,YeganehKordi,SwaroopMishra,AlisaLiu,NoahA.Smith,DanielKhashabi,
andHannanehHajishirzi. Self-instruct: Aligninglanguagemodelwithselfgeneratedinstruc-
tions,2022.
[45] YizhongWang,SwaroopMishra,PegahAlipoormolabashi,YeganehKordi,AmirrezaMirzaei,
AnjanaArunkumar,ArjunAshok,ArutSelvanDhanasekaran,AtharvaNaik,DavidStap,etal.
Super-naturalinstructions:generalizationviadeclarativeinstructionson1600+tasks. InEMNLP,
2022.
[46] JasonWei,MaartenBosma,VincentYZhao,KelvinGuu,AdamsWeiYu,BrianLester,Nan
Du,AndrewMDai,andQuocVLe. Finetunedlanguagemodelsarezero-shotlearners. arXiv
preprintarXiv:2109.01652,2021.
[47] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,EdChi,QuocLe,andDenny
Zhou. Chainofthoughtpromptingelicitsreasoninginlargelanguagemodels. arXivpreprint
arXiv:2201.11903,2022.
12

[48] CanXu,QingfengSun,KaiZheng,XiuboGeng,PuZhao,JiazhanFeng,ChongyangTao,and
DaxinJiang. Wizardlm: Empoweringlargelanguagemodelstofollowcomplexinstructions.
arXivpreprintarXiv:2304.12244,2023.
[49] ZonghengYang,ZhanghaoWu,MichaelLuo,Wei-LinChiang,RomilBhardwaj,WoosukKwon,
SiyuanZhuang, FrankSifeiLuan, GautamMittal, ScottShenker, andIonStoica. SkyPilot:
Anintercloudbrokerforskycomputing. In20thUSENIXSymposiumonNetworkedSystems
DesignandImplementation(NSDI23),pages437–455,Boston, MA,April2023.USENIX
Association.
[50] RowanZellers,AriHoltzman,YonatanBisk,AliFarhadi,andYejinChoi. Hellaswag: Cana
machinereallyfinishyoursentence? arXivpreprintarXiv:1905.07830,2019.
[51] WanjunZhong,RuixiangCui,YiduoGuo,YaoboLiang,ShuaiLu,YanlinWang,AminSaied,
WeizhuChen,andNanDuan. Agieval: Ahuman-centricbenchmarkforevaluatingfoundation
models. arXivpreprintarXiv:2304.06364,2023.
[52] ChuntingZhou,PengfeiLiu,PuxinXu,SriniIyer,JiaoSun,YuningMao,XuezheMa,Avia
Efrat,PingYu,LiliYu,etal.Lima:Lessismoreforalignment.arXivpreprintarXiv:2305.11206,
2023.
13

A Prompttemplates
WelisttheprompttemplatesforLLMjudges. Pleaserefertoourgithubrepository3forfulldetails.
[System]
Please act as an impartial judge and evaluate the quality of the responses provided by two
AI assistants to the user question displayed below. You should choose the assistant that
follows the user’s instructions and answers the user’s question better. Your evaluation
should consider factors such as the helpfulness, relevance, accuracy, depth, creativity,
and level of detail of their responses. Begin your evaluation by comparing the two
responses and provide a short explanation. Avoid any position biases and ensure that the
order in which the responses were presented does not influence your decision. Do not allow
the length of the responses to influence your evaluation. Do not favor certain names of
the assistants. Be as objective as possible. After providing your explanation, output your
final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]"
if assistant B is better, and "[[C]]" for a tie.
[User Question]
{question}
[The Start of Assistant A’s Answer]
{answer_a}
[The End of Assistant A’s Answer]
[The Start of Assistant B’s Answer]
{answer_b}
[The End of Assistant B’s Answer]
Figure5: Thedefaultpromptforpairwisecomparison.
[System]
Please act as an impartial judge and evaluate the quality of the response provided by an
AI assistant to the user question displayed below. Your evaluation should consider factors
such as the helpfulness, relevance, accuracy, depth, creativity, and level of detail of
the response. Begin your evaluation by providing a short explanation. Be as objective as
possible. After providing your explanation, please rate the response on a scale of 1 to 10
by strictly following this format: "[[rating]]", for example: "Rating: [[5]]".
[Question]
{question}
[The Start of Assistant’s Answer]
{answer}
[The End of Assistant’s Answer]
Figure6: Thedefaultpromptforsingleanswergrading.
3https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge
14

[System]
Please act as an impartial judge and evaluate the quality of the responses provided by two
AI assistants to the user question displayed below. Your evaluation should consider
correctness and helpfulness. You will be given assistant A’s answer, and assistant B’s
answer. Your job is to evaluate which assistant’s answer is better. You should
independently solve the user question step-by-step first. Then compare both assistants’
answers with your answer. Identify and correct any mistakes. Avoid any position biases and
ensure that the order in which the responses were presented does not influence your
decision. Do not allow the length of the responses to influence your evaluation. Do not
favor certain names of the assistants. Be as objective as possible. After providing your
explanation, output your final verdict by strictly following this format: "[[A]]" if
assistant A is better, "[[B]]" if assistant B is better, and "[[C]]" for a tie.
[User Question]
{question}
[The Start of Assistant A’s Answer]
{answer_a}
[The End of Assistant A’s Answer]
[The Start of Assistant B’s Answer]
{answer_b}
[The End of Assistant B’s Answer]
Figure7: Thechain-of-thoughtpromptformathandreasoningquestions.
[System]
Please act as an impartial judge and evaluate the quality of the responses provided by two
AI assistants to the user question displayed below. Your evaluation should consider
correctness and helpfulness. You will be given a reference answer, assistant A’s answer,
and assistant B’s answer. Your job is to evaluate which assistant’s answer is better.
Begin your evaluation by comparing both assistants’ answers with the reference answer.
Identify and correct any mistakes. Avoid any position biases and ensure that the order in
which the responses were presented does not influence your decision. Do not allow the
length of the responses to influence your evaluation. Do not favor certain names of the
assistants. Be as objective as possible. After providing your explanation, output your
final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]"
if assistant B is better, and "[[C]]" for a tie.
[User Question]
{question}
[The Start of Reference Answer]
{answer_ref}
[The End of Reference Answer]
[The Start of Assistant A’s Answer]
{answer_a}
[The End of Assistant A’s Answer]
[The Start of Assistant B’s Answer]
{answer_b}
[The End of Assistant B’s Answer]
Figure8: Thepromptforreference-guidedpairwisecomparison.
15

[System]
Please act as an impartial judge and evaluate the quality of the responses provided by two
AI assistants to the user question displayed below. You should choose the assistant that
follows the user’s instructions and answers the user’s question better. Your evaluation
should consider factors such as the helpfulness, relevance, accuracy, depth, creativity,
and level of detail of their responses. Begin your evaluation by comparing the two
responses and provide a short explanation. Avoid any position biases and ensure that the
order in which the responses were presented does not influence your decision. Do not allow
the length of the responses to influence your evaluation. Do not favor certain names of
the assistants. Be as objective as possible. After providing your explanation, output your
final verdict by strictly following this format: "[[A]]" if assistant A is better, "[[B]]"
if assistant B is better, and "[[C]]" for a tie.
<|The Start of Assistant A’s Conversation with User|>
### User:
{question 1}
### Assistant A:
{answer 1}
### User:
{question 2}
### Assistant A:
{answer 2}
<|The End of Assistant A’s Conversation with User|>
<|The Start of Assistant B’s Conversation with User|>
### User:
{question 1}
### Assistant B:
{answer 1}
### User:
{question 2}
### Assistant B:
{answer 2}
<|The End of Assistant B’s Conversation with User|>
Figure9: Thepromptformulti-turnpairwisecomparison.
16

[System]
Please act as an impartial judge and evaluate the quality of the response provided by an
AI assistant to the user question. Your evaluation should consider correctness and
helpfulness. You will be given a reference answer and the assistant's answer. You
evaluation should focus on the assistant's answer to the second question. Begin your
evaluation by comparing the assistant's answer with the reference answer. Identify and
correct any mistakes. Be as objective as possible. After providing your explanation, you
must rate the response on a scale of 1 to 10 by strictly following this format:
"[[rating]]", for example: "Rating: [[5]]".
<|The Start of Reference Answer|>
### User:
{question_1}
### Reference answer:
{ref_answer_1}
### User:
{question_2}
### Reference answer:
{ref_answer_2}
<|The End of Reference Answer|>
<|The Start of Assistant A's Conversation with User|>
### User:
{question_1}
### Assistant A:
{answer_1}
### User:
{question_2}
### Assistant A:
{answer_2}
<|The End of Assistant A's Conversation with User|>
Figure10: Thepromptforreference-guidedmulti-turnsingle-answergrading.
17

B CaseStudy
Welistseveralcasestudies. Theexamplesaregeneratedbygpt-4-0314. Theymaynotbefully
reproduciblewithfutureGPT-4versions.
Question:What are some business etiquette norms when doing business in Japan?
Assistant A: Assistant B:
Here are some business etiquette norms to keep When doing business in Japan, it is important to be
in mind when doing business in Japan: aware of and respect the country’s business
1. Bowing: Bowing is a common greeting in etiquette norms. Some of these norms include:
Japan. It is a sign of respect and should 1. Greetings: A handshake and bow is the standard
be reciprocated. greeting in Japan. It is important to bow deeply
2. Business cards: Business cards are and to offer a firm handshake.
exchanged at the beginning of a meeting. It 2. Business cards: In Japan, business cards are
is important to receive and give business exchanged after the initial greeting. It is
cards with both hands and to take a moment important to handle the card with respect and to
to read the card before putting it away. read it carefully before placing it on the
3. Punctuality: Being on time is important in table.
Japan. Arrive a few minutes early to show 3. Meetings: Meetings in Japan are typically formal
respect for your colleagues. and conducted in a hierarchical manner. It is
4. Dress code: Dress conservatively and important to address people by their titles and
professionally. Men should wear dark suits to avoid direct eye contact.
and ties, while women should wear 4. Punctuality: Punctuality is highly valued in
conservative business attire. Japan. It is important to arrive on time for
5. Language: Learn a few basic Japanese meetings and to be prepared in advance.
phrases to show respect for the culture. It 5. Gift giving: Gift giving is a common practice in
is also important to speak clearly and Japan, but it is important to be mindful of the
avoid using slang or idioms. occasion and the relationship. Avoid giving
6. Gift giving: Gift giving is a common gifts that are considered too personal or
practice in Japan. Bring a small gift, such extravagant.
as a box of chocolates or a small souvenir 6. Dining: Dining is an important part of doing
from your home country. business in Japan. It is important to be aware
7. Dining etiquette: When dining with of the proper table manners and to avoid
colleagues, wait for the host to begin slurping or making loud noises while eating.
eating before you start. Use chopsticks 7. Communication: Communication in Japan is
correctly and avoid leaving food on your typically indirect and reserved. It is important
plate. to listen carefully and to avoid confrontational
language.
Remember, showing respect for Japanese culture
and customs is key to building strong business Overall, it is important to be respectful,
relationships in Japan. punctual, and mindful of hierarchy when doing
business in Japan.
GPT-4 Judgment (when A is placed in the first position):
Both Assistant A and Assistant B provide helpful and relevant information about business etiquette
norms in Japan. However, Assistant A’s answer is more detailed and organized, covering a wider range
of topics such as dress code and language, which are not mentioned in Assistant B’s response.
Assistant A also provides more specific advice on how to handle certain situations, such as
exchanging business cards and dining etiquette. Therefore, Assistant A’s answer is more comprehensive
and useful for someone looking to understand Japanese business etiquette.
GPT-4 Judgment (when B is placed in the first position):
Both Assistant A and Assistant B provide helpful and relevant information about business etiquette
norms in Japan. However, Assistant B’s answer is more detailed and covers a wider range of topics,
such as addressing people by their titles, avoiding direct eye contact, and being mindful of
communication styles. Assistant A’s answer is more concise but lacks some of the depth found in
Assistant B’s response. Therefore, Assistant B’s answer is better in this case.
Figure11: Anexampleofpositionbias. WhenAssistantAisplacedinthefirstposition, GPT-4
thinksAisbetter,butitsverdictchangeswhenweswapthepositionofAandB.Weobservesimilar
patternfromotherLLMjudgessuchasClaude/GPT-3.5.
18

Question:What is the central dogma of molecular biology? What processes are involved? Who named this?
Assistant A: Assistant B:
The central dogma of molecular biology is the The central dogma of molecular biology is the
fundamental principle that explains how genetic fundamental principle that explains how genetic
information flows within a biological system. It information flows within a biological system. It
states that DNA is transcribed into RNA, which is states that DNA is transcribed into RNA, which is
then translated into proteins. This means that then translated into proteins. This means that
the genetic information stored in DNA is first the genetic information stored in DNA is first
copied into RNA, which then serves as a template copied into RNA, which then serves as a template
for the synthesis of proteins. for the synthesis of proteins.
The processes involved in the central dogma are: The processes involved in the central dogma are:
1. Transcription rephrased: The act of copying 1. Transcription: The process by which the
genetic information from DNA to RNA. genetic information in DNA is copied into RNA.
2. Translation rephrased: The act of using 2. Translation: The process by which the genetic
genetic information in RNA to create proteins. information in RNA is used to synthesize
3. Transcription: The process by which the proteins.
genetic information in DNA is copied into RNA.
4. Translation: The process by which the genetic The term "central dogma" was coined by Francis
information in RNA is used to synthesize Crick, one of the co-discoverers of the structure
proteins. of DNA, in 1958.
The term "central dogma" was coined by Francis
Crick, one of the co-discoverers of the structure
of DNA, in 1958.
GPT-3.5 Judgment:
Assistant A provides a more detailed and accurate response to the user's question. While both
assistants correctly state the central dogma of molecular biology and who coined the term, Assistant
A provides a more comprehensive explanation of the processes involved in the central dogma, including
the rephrased definitions of transcription and translation. Therefore, I choose A as the better
assistant.
Claude-v1 Judgment:
Both assistants answer the question by defining the central dogma and detailing the two processes
involved, transcription and translation. However, assistant A provides a more in-depth and detailed
explanation by briefly rephrasing and elaborating on these processes. Assistant A also mentions who
coined the term "central dogma", which provides useful context and shows a more comprehensive
understanding of the topic. Overall, assistant A gives a fuller and more insightful response, so I
have chosen it as the better assistant for this question.
GPT-4 Judgment:
Both Assistant A and Assistant B provide accurate and relevant information about the central dogma of
molecular biology, the processes involved, and who named it. However, Assistant A's answer contains a
minor redundancy by rephrasing transcription and translation twice. Assistant B's answer is more
concise and avoids this redundancy. Therefore, Assistant B's answer is better.
Figure 12: An example of “repetitive list” attack to examine verbosity bias. Except for the two
rephraseditems(highlightedinred),AssistantA’sanswerisexactlythesameasAssistantB.Both
GPT-3.5andClaude-v1showaverbositybiastowardsthelongerandrepetitiveanswer. OnlyGPT-4
successfullydetectedthisattack.
19

Question:Benjamin went to a bookstore and purchased a variety of books. He bought 5 copies of a sci-fi
novel, each priced at $20, 3 copies of a history book priced at $30 each, and 2 copies of a philosophy book for
$45 each. What was the total cost of his purchases?
Assistant A: Assistant B:
The total cost of Benjamin’s purchases was $115. The total cost of his purchases is $295.
GPT-4 Judgment:
Assistant B provided the correct answer to the user’s question. Assistant A’s response was incorrect.
To calculate the total cost of Benjamin’s purchases, we need to multiply the number of books by their
respective prices and then add the results:
5 sci-fi novels * $20 = $100
3 history books * $30 = $90
2 philosophy books * $45 = $90
Total cost = $100 + $90 + $90 = $295
Assistant B’s response is accurate and directly answers the user’s question. Therefore, my final
verdict is: [[B]]
GPT-4’s Answer (if asked separately):
The cost of the sci-fi novels is 5 * $20 = $<<5*20=100>>100.
The cost of the history books is 3 * $30 = $<<3*30=90>>90.
The cost of the philosophy books is 2 * $45 = $<<2*45=90>>90.
The total cost of his purchases is $100 + $90 + $90 = $<<100+90+90=280>>280. Answer: \boxed{280}.
Figure13: Withadefaultprompt,GPT-4showslimitedcapabilityingradingmathquestions. Despite
beingabletoanswerthequestionitself,itsjudgmentwasinfluencedbythegivenanswers,leadingto
arithmeticmistakeshighlightedinyellow.
Question:Each problem consists of three statements. Based on the first two statements, the third statement
may be true, false,or uncertain.
1. Oranges cost more than apples.
2. Oranges cost less than bananas.
3. Bananas cost more than apples and bananas cost more than orange.
If the first two statements are true, then the third statement is
Assistant A: Assistant B:
false. False.
If oranges cost more than apples (statement 1) and If the first two statements are true, then the
oranges cost less than bananas (statement 2), then third statement is false. The first statement
it is not possible for bananas to cost less than says that oranges cost more than apples, and the
oranges and also cost more than both apples and second statement says that oranges cost less
oranges (statement 3). Therefore, statement 3 is than bananas. This means that oranges cost less
false. than bananas, which contradicts the third
statement that bananas cost more than apples and
more than oranges. Therefore, the third
statement must be false.
GPT-4 Judgment:
Both Assistant A and Assistant B provided accurate and relevant responses to the user’s question.
They both concluded that the third statement is false based on the first two statements. However,
Assistant B’s response is slightly clearer and more concise in explaining the contradiction between
the statements. Therefore, I choose Assistant B as the better response.
[[B]]
GPT-4’s Answer (if asked separately):
True.
If oranges cost more than apples (statement 1) and oranges cost less than bananas (statement 2), it
logically follows that bananas cost more than apples and bananas cost more than oranges, which is the
third statement. So, if the first two statements are true, the third one is also true.
Figure14: AnexampleofGPT-4’slimitedcapabilityingradingreasoningquestion. DespiteGPT-4
knows how to solve the question (if asked separately), it made a wrong judgement saying both
assistants’wronganswersarecorrect.
20

Question:How many integers are in the solution of the inequality |x + 5| < 10?
Assistant A: Assistant B:
There are 19 integers in the solution of the To solve the inequality |x + 5| < 10, we need to
inequality |x + 5| < 10. consider two cases:
Case 1: x + 5 is positive or zero
In this case, the inequality becomes x + 5 < 10,
which simplifies to x < 5.
Case 2: x + 5 is negative
In this case, the inequality becomes -(x + 5) < 10,
which simplifies to -x - 5 < 10. Adding 5 to both
sides gives -x < 15, and multiplying by -1 (and
flipping the inequality) gives x > -15.
So the solution to the inequality is -15 < x < 5. The
integers in this range are -14, -13, -12, ..., 4, for
a total of 20 integers. Therefore, there are 20
integers in the solution of the inequality.
GPT-4 Judgment:
To solve the inequality |x + 5| < 10, we need to consider two cases:
Case 1: x + 5 is positive or zero
In this case, the inequality becomes x + 5 < 10, which simplifies to x < 5.
Case 2: x + 5 is negative
In this case, the inequality becomes -(x + 5) < 10, which simplifies to -x - 5 < 10. Adding 5 to both
sides gives -x < 15, and multiplying by -1 (and flipping the inequality) gives x > -15.
So the solution to the inequality is -15 < x < 5. The integers in this range are -14, -13, -12, ...,
4, for a total of 20 integers. Therefore, there are 20 integers in the solution of the inequality.
Comparing the answers provided by the two AI assistants:
Assistant A: 19 integers
Assistant B: 20 integers
The correct answer is 20 integers, so Assistant B provided the correct and more helpful response.
Final verdict: [[B]]
GPT-4’s Answer (if asked separatedly):
We can split the inequality into two cases:
1) If $x+5\ge 0$, then $|x+5|=x+5$. So, we have $x+5<10$, which means $x<5$. Since $x+5\ge 0$, we
have $x\ge -5$. So in this case, $x$ can be any integer from $-5$ to $4$, inclusive, which gives us
$5-(-5)+1=10$ integers.
2) If $x+5<0$, then $|x+5|=-(x+5)$. So, we have $-(x+5)<10$, which means $x+5>-10$, which means $x>-
15$. Since $x+5<0$, we have $x<-5$. So in this case, $x$ can be any integer from $-14$ to $-6$,
inclusive, which gives us $-6-(-14)+1=9$ integers.
In total, there are $10+9=\boxed{19}$ integers in the solution.
Figure15:AnexampleofGPT-4’swrongjudgmentwithchain-of-thoughtprompt. WecanseeGPT-4
exactlycopiedAssistantB’sanswer(whichcontainsarithmeticerrors)anddeterminedAssistantA’s
answerisincorrect. ThissuggestGPT-4’schain-of-thoughtprocesscanbesignificantlyinfluencedby
thegivenanswersdespiteweaskittothinkindependently.
21

Question:Share ideas for adapting art masterpieces into interactive experiences for children. List 5 specific
artworks and associated ideas.
Assistant A: Assistant B:
Sure, here are five ideas for adapting art masterpieces into interactive (omitted)
experiences for children:
1. “The Starry Night” by Vincent van Gogh - Create a virtual reality experience
where children can explore the night sky and see the stars and constellations as
van Gogh saw them. They can also create their own starry night scenes using
different colors and brush strokes.
2. “The Persistence of Memory” by Salvador Dali - Create a sensory experience
where children can touch, feel, and smell different objects to explore the
surrealist themes of Dali’s painting. They can also create their own surreal
landscapes using different materials and textures.
3. ...
(omitted)
Follow-up Question: Write a concrete plan for your second example.Include budget estimates.
Assistant A: Assistant B:
Sure, here is a concrete plan for adapting “The Persistence of Memory” by Salvador (omitted)
Dali into an interactive experience for children:
1. Budget: $5,000
2. Objectives:
- To create a sensory experience that allows children to explore the surrealist
themes of Dali’s painting.
- To encourage children to create their own surreal landscapes using different
materials and textures.
...
GPT-4 Judgment:
Assistant A provided a concrete plan for adapting “The Persistence of Memory” by Salvador Dali into
an interactive experience for children, while Assistant B provided a plan for the “Mona Lisa
Interactive Experience for Children.” The user’s follow-up question specifically asked for a concrete
plan for the second example, which was the “Mona Lisa” experience provided by Assistant B.
Therefore, Assistant B’s answer is more relevant and directly addresses the user’s request.
My final verdict is: [[B]]
Figure 16: In this example, despite Assistant A correctly followed user’s instruction to generate
a concrete plan for the second example of its previous response, GPT-4 wrongly referred to the
secondexampleinAssistantB’sresponse,resultinginawrongjudgment. Thissuggeststheprompt
designthatbreaksthequestionsintotwopromptsmaycauseLLMjudgestruggletolocateassistants’
previousresponses.
22

C DataCollection
WedescribeourdatacollectionprocessforbothMT-benchandChatbotArena.
C.1 MT-benchhumanevaluation
Figure17showsthenormalvotinginterface. Figure18showsthatweadditionallyshowGPT-4’s
judgmenttousersandaskifitisreasonablewhenahumandiffersfromGPT-4.
Figure17: ThescreenshotofMT-benchdatacollection. Weshowaninstructionsimilartotheprompt
wegivetoGPT-4. WepresentquestionsfromMT-benchandanswersfromtworandomanonymous
assistantsandaskwhichoneisbetter. Wepresentthefirst-turnconversationandaskhumanstovote,
thenrepeatthesameprocedureforthesecond-turn. Ausercanskipupto5questionsiftheyarenot
confident. Forsomequestions(e.g.,math,reasoning),theycanalsoseeareferencesolution.
Figure18: ThescreenshotofMT-benchdatacollection. Whenhuman’svotediffersfromGPT-4,we
additionallyshowGPT-4’sjudgment(redregioninthescreenshot)andasktheusertoclickoneof
thethreebuttonstodecidewhetherGPT-4’sjudgmentisreasonable.
23

To invite participants, we obtained their consent by letting them sign an application form. We
paythem$20forjudging20questions, whichcorrespondstoanhourlyrateofaround$35. The
participantsaremostlygraduatestudentsfrommorethantenuniversities.
C.2 ChatbotArena
Figure 19 shows a screenshot of Chatbot Arena. Users are required to accept the terms of use,
whichobtaintheirconsentandgiveustherighttoreleasetheconversationdata. Theinstructions
are shown at the top of the interface. This is a free website. We do not pay users and any user
canusethisplatformwithoutregistration. Moreintroductionsandanalysescanbefoundathttps:
//lmsys.org/blog/2023-05-03-arena/.
Figure19: ThescreenshotofChatbotArena.
C.3 DataRelease
WewillcleanthePersonalIdentifiableInformation(PII)andtagtoxicconversationswithOpenAI
moderationAPIsforourdatasetrelease.
24

D AdditionalExperimentalResults
Wepresentsomeadditionalexperimentalresults.
D.1 Positionbias
WetesttwomorepromptsandpresentthefullresultsinTable9“score”changesthedefaultprompt
toletthemodeloutputtwoabsolutescoresinsteadofwhichoneisbetter. “short”isasimplified
versionofourdefaultpromptbyremovinginstructionslike“Avoidanypositionbias..”,“Beginyour
evaluation... andprovideashortexplanation”. Wecanfinddifferentpromptshavedifferenteffects
ondifferentmodels. Forexample,the"score"promptcanincreasetheconsistencyofGPT-3.5but
decreasesitforClaude-v1andGPT-4.
Table9: Positionbiasondifferentmodelsandprompts. Consistencyisthepercentageofcaseswhere
ajudgegivesconsistentresultswhenswappingtheorderoftwoassistants. “Biasedtowardfirst”is
thepercentageofcaseswhenajudgefavorsthefirstanswer. “Error”indicateswrongoutputformats.
Thetwolargestnumbersineachcolumnareinbold.
Judge Prompt Consistency Biasedtowardfirst Biasedtowardsecond Error
default 23.8% 75.0% 0.0% 1.2%
rename 56.2% 11.2% 28.7% 3.8%
claude-v1
score 20.0% 80.0% 0.0% 0.0%
short 22.5% 75.0% 2.5% 0.0%
default 46.2% 50.0% 1.2% 2.5%
rename 51.2% 38.8% 6.2% 3.8%
gpt-3.5-turbo
score 55.0% 33.8% 11.2% 0.0%
short 38.8% 57.5% 3.8% 0.0%
default 65.0% 30.0% 5.0% 0.0%
rename 66.2% 28.7% 5.0% 0.0%
gpt-4
score 51.2% 46.2% 2.5% 0.0%
short 62.5% 35.0% 2.5% 0.0%
AsshowninTable10,positionbiasismorenoticeableonopenquestionslikewritingandstem/hu-
manityknowledgequestions. Onmathandcodingquestions,LLMjudgesaremoreconfidenteven
thoughtheirjudgmentscanoftenbewrong,asweshowinSection3.3. Finally,westudyhowthe
modelpairsinfluencepositionbiasbyusingGPT-4andthedefaultprompttojudgethreedifferent
model pairs. As shown in Table 11, the position bias is more noticeable for models with close
performanceandcanalmostdisappearwhentheperformanceofthetwomodelsdiffersalot.
Table10: Positionbiasondifferentcategories. Thetwolargestnumbersineachcolumnareinbold.
Category Consistent Biasedtowardfirst Biasedtowardsecond
writing 42.0% 46.0% 12.0%
roleplay 68.0% 30.0% 2.0%
reasoning 76.0% 20.0% 4.0%
math 86.0% 4.0% 10.0%
coding 86.0% 14.0% 0.0%
extraction 78.0% 12.0% 10.0%
stem 44.0% 54.0% 2.0%
humanities 36.0% 60.0% 4.0%
Table11: Positionbiasondifferentmodelpairs.
Pair Consistent Biasedtowardfirst Biasedtowardsecond
GPT-3.5vsClaude-V1 67.5% 23.8% 8.8%
GPT-3.5vsVicuna-13B 73.8% 23.8% 2.5%
GPT-3.5vsLLaMA-13B 98.8% 1.2% 0.0%
25

D.2 Few-shotjudge
Weexaminehowfew-shotexamplesimproveLLMjudges. AsshowninTable12,theyimprovethe
consistencyofallthreeLLMjudgessignificantly. ItalmostalleviatesthepositionbiasofGPT-4,but
movesthepositionbiasofGPT-3.5fromthefirstpositiontothesecondposition. Wethenmeasure
theagreementbetweenfew-shotGPT-4pairwisecomparisonandhumansonMT-bench,butfoundit
performssimilarlytozero-shotGPT-4pairwisecomparison.
Table12: Improvementsofthefew-shotjudgeonconsistencyforpositionbias.
Model Prompt Consistency Biasedtowardfirst Biasedtowardsecond Error
zero-shot 23.8% 75.0% 0.0% 1.2%
Claude-v1
few-shot 63.7% 21.2% 11.2% 3.8%
zero-shot 46.2% 50.0% 1.2% 2.5%
GPT-3.5
few-shot 55.0% 16.2% 28.7% 0.0%
zero-shot 65.0% 30.0% 5.0% 0.0%
GPT-4
few-shot 77.5% 10.0% 12.5% 0.0%
D.3 AgreementEvaluation
Agreementcalculation. Wedefinetheagreementbetweentwotypesofjudgesastheprobability
ofrandomlyselectedindividuals(butnotidentical)ofeachtypeagreeingonarandomlyselected
question. Forexample,ifwearecomparingGPT-4andClaude,theagreementistheprobabilityof
GPT-4andClaudeagreeingonthevoteforarandomlyselectedquestion. IfwearecomparingGPT-4
andhumans,theagreementistheprobabilityofGPT-4andarandomlyselectedhumanagreeing
on the vote for a randomly selected question. The agreement among humans themselves is the
probabilityoftworandomlyselectedbutnotidenticalhumansagreeingonthevoteforarandomly
selectedquestion.
Notethattheagreementamonghumanscouldbealowerestimationcomparedtotheagreementof
GPT4andhumans. Considerthreehumanswhovoted“A”,“A”,and“B”foraquestion,respectively.
Theagreementamongthemisonly 1,astherearethreepairs“(A,A)”,“(A,B)”,and“(A,B)”.But
3
theagreementbetweenGPT4andthosethreeis 2 ifGPT4voted“first”and 1 otherwise.
3 3
Therefore,tohaveamorecomprehensiveunderstandingofwhathappened,weintroduceanewjudge
typecalledhuman-majority,whichconsidersthemajorityofhumanvotesforeachquestion. The
agreementbetweenGPT4andhuman-majorityisthencalculatedastheprobabilityofGPT4agreeing
withthemajorityofhumanvotesonarandomlyselectedquestion. Theupperboundoftheagreement
betweenGPT-4andhumansistheagreementbetweenhuman-majorityandhuman. Whenthereisno
majorityvoteforaquestion,theagreementiscountedbyanevensplit. Forexample,iftherearean
equalnumberof“A”and“B”humanvotesforaquestion,andGPT4votes“A”,theagreementis
countedas 1 onthisquestion.
2
Moreresults. Table13showsmoreagreementresultsonMT-bench. Inadditiontoexpertlabelers
(denotedas“Human”),wealsoincludeauthorvotes(denotedas“Author”).
D.4 Category-wisescoreswithsingle-answergrading
Weusesingle-answergradingtoevaluate6modelsonMT-benchandplotthecategory-wisescoresin
Figure20.
26

Table13: AgreementbetweentwotypesofjudgesonMT-bench. “G4-P”and“G4-S”denoteGPT-4
withpairwisecomparisonandsingle-answergrading,respectively. “C”denotesClaude. “Human”
denotes expert labelers (excluding authors). ‘Human-M” denotes the majority vote of humans.
The single-answer grading can be converted into pairwise comparison results for calculating the
agreement. Wereporttwosetups: “S1”includesnon-tie,tie,andinconsistent(duetopositionbias)
votesandcountsinconsistentasatie;“S2”onlyincludesnon-tievotes. Theagreementbetweentwo
randomjudgesundereachsetupisdenotedas“R=”. Thetopvalueineachcellistheagreement,and
thebottomgrayvalueis#votes.
Setup S1(R=33%) S2(R=50%)
Judge G4-S C Author Human Human-M G4-S C Author Human Human-M
70% 63% 69% 66% 67% 97% 94% 92% 85% 85%
G4-P 1138 1198 345 1343 821 662 582 201 859 546
66% 67% 60% 60% 90% 94% 85% 85%
G4-S - 1136 324 1280 781 - 563 175 739 473
58% 54% 55% 89% 85% 86%
C - - 343 1341 820 - - 141 648 414
69% 65% 55% 87% 83% 76%
Author - - 49 428 93 - - 31 262 46
63% 81% 81% 90%
Human - - - 721 892 - - - 479 631
(a)FirstTurn
Setup S1(R=33%) S2(R=50%)
Judge G4-S Author Human Human-M G4-S Author Human Human-M
70% 66% 66% 68% 95% 88% 85% 85%
G4-P 1161 341 1325 812 727 205 864 557
65% 59% 61% 89% 84% 85%
G4-S - 331 1285 783 - 193 776 506
67% 68% 63% 87% 86% 84%
Author - 49 413 87 - 31 273 54
67% 83% 82% 91%
Human - - 707 877 - - 474 629
(b)SecondTurn
Writing
model
Humanities Roleplay GPT-4
Claude-v1
GPT-3.5-turbo
Vicuna-13B
Alpaca-13B
STEM Reasoning LLaMA-13B
0 2 4 6 8 10
Extraction Math
Coding
Figure20: Category-wisescoresof6modelsonMT-bench.
27

E TrainingDetailsofVicunaModels
Vicunaiscreatedbyfine-tuningaLLaMAbasemodelusinguser-sharedconversationsgatheredfrom
ShareGPT.comwithitspublicAPIs. ShareGPTisawebsitewhereuserscansharetheirChatGPT
conversations. Toensuredataquality,weconverttheHTMLbacktomarkdownandfilteroutsome
inappropriateorlow-qualitysamples,whichresultsin125Kconversationsafterdatacleaning.4 We
thendividelengthyconversationsintosmallersegmentsthatfitthemodel’smaximumcontextlength.
WeconstructthreetrainingdatasetswithdifferentscalesfromthiscleanedShareGPTdataset. Their
statisticsareinTable8,wherewealsocompareitwithAlpaca[38]dataset. “All”isthefulldataset.
“Single”onlyincludesthefirstturnofeachconversation. “Selected”isasmallhigh-qualitydatasetof
3Ksequences. Toconstructthe“Selected”dataset,wepicksequencesthatincludeatleast3turnsof
conversationsgeneratedbyGPT-4andrunaclusteringalgorithmtodividetheminto3Kclustersand
pickthecentroidofeachcluster.
All models (Vicuna-7B/13B) are trained with the same hyperparameters: global batch size=128,
learning=2e-5,epochs=3,seqlength=2048. Exceptfor“Selected”,whichwetrainfor5epochs. The
trainingcodeisbuiltontopoftheAlpacacodebutadditionallyhandlesmulti-turnconversations. The
trainingisdonewith8xA100GPUs. Thelongestsingletrainingruntakesaround2days. Weutilize
SkyPilot[49]managedspotinstancesforsavingtrainingcostsandFlashAttention[11]formemory
optimizations. Thetrainingcodeisavailableathttps://github.com/lm-sys/FastChat.
Table14: Datasetstatistics
DatasetName Alpaca Selected Single All
#Token 4.4M 4.8M 184M 370M
#Sequence 52K 3K 257K 257K
Avg.turnsofconversation 1.0 4.0 1.0 2.9
Avg.responselength(token) 65 343 473 373
4Inthisstudy,weusemoredata(125K)thantheversioninourearlierblogpost(70K).
28

F ExploringVicunaasajudge
Inthispaper,wemostlyevaluatetheabilityofclose-sourcedmodelssuchasGPT-4asaproxyfor
human evaluations. However, model services such as GPT-4 can also become expensive with a
growingnumberofevaluations. Ontheotherhand,popularopen-sourcedLLMs,e.g. Vicuna-13B
showsstronglanguageunderstandingcapability,andaremuchcheaperthanclose-sourcedLLMs. In
thissection,wefurtherexplorethepotentialofusingVicuna-13Basamorecost-friendlyproxy.
F.1 Zero-ShotVicuna
When using as-it-is (zero-shot), Vicuna-13B noticeably suffers from limitations we discuss, e.g.
position bias. As shown in Table 15, Vicuna-13B has a consistency rate from 11.2% to 16.2%
acrossdifferentprompttemplates,muchlowerthanalltheclosed-sourcedmodels. Inaddition,it
hasahigherrorrate(from22.5%to78.8%)becauseofitsweakerinstruction-followingcapability.
In many scenarios, Vicuna-13B provides responses such as "Answer A is better than answer B",
withoutfollowingthepre-definedtemplate. Theseresponsesarerenderedasnaturallanguagesand
aredifficulttobeparsedautomatically,makingthemodellessusefulinascalableandautomatic
evaluationpipeline.
F.2 ArenaFine-tunedVicuna
Training Duetotheincapabilityofthezero-shotVicuna-13Bmodel,wefurtherfinetunethemodel
with human votes from ChatbotArena. Specifically, we randomly sample 22Ksingle-turn votes
fromthearena,coveringallmodelssupportedbythetimeofthispapersubmission(GPT-4,GPT-3.5,
Claude-v1,Vicuna-13b,Vicuna-7b,Koala-13B,Alpaca-13B,LLaMA-13B,Dolly-12B,FastChat-T5,
RWKV-4-Raven,MPT-Chat,OpenAssistant,ChatGLM,andStableLM),toexposethemodelwith
awiderrangeofchatbotoutputsandhumanpreferences. Weuse20Kvotesfortraining,and2K
forvalidation. Toaddresstheaforementionedweakinstructionfollowingproblem,weformulate
theproblemasa3-waysequenceclassificationproblem. Thus,themodelsimplyneedstopredict
whichoneofthechat-botoutputsisbetter(ortie),withoutneedingtoexactlyfollowingtheprovided
answertemplate. Inparticular,weconstructaninputbyusingthedefaultpromptandthetwomodel
answers. ThelabelsareA,B,andtie(includingboth-bad-voteandtie-vote). Wetrainfor3epochs
withacosinelearningratescheduleranda2e-5maximumlearningrate. Weusethe2Kvalidation
datasettochoosehyper-parameters,andtestonthesame3Kdatasetinthemainbodyofthepaper.
Position bias results The results for position bias are provided in Table 15. The consistency
improvessignificantlyfrom16.2%to65.0%. Duetotheclassificationformulation,everyoutputis
recognizable(errorrate0%). Inaddition,wemeasuretheclassificationaccuracyoverthetestdataset.
Agreementresults Itachieves56.8%whenincludingallthreelabels,and85.5%whenexcluding
tiepredictionsandlabels,significantlyoutperformingrandomguessesof33%and50%respectively,
andshowpositivesignalstomatchGPT-4(66%and87%respectively). Inconclusion, afurther
fine-tunedVicuna-13Bmodelshowsstrongpotentialtobeusedasacheapopen-sourcedreplacement
forexpensiveclosed-sourcedLLMs. Asimilarconclusionisalsofoundbyaconcurrentpaper[42].
Table15:PositionbiasoftheVicuna-13Bmodelwithoutandwithfurtherfine-tuning.Wedenotethem
asVicuna-13B-Zero-ShotandVicuna-13B-Fine-Tunerespectively. Consistencyisthepercentage
ofcaseswhereajudgegivesconsistentresultswhenswappingtheorderoftwoassistants. “Biased
towardfirst”isthepercentageofcaseswhenajudgefavorsthefirstanswer. “Error”indicateswrong
outputformats. Thelargestnumberineachcolumnisinbold.
Judge Prompt Consistency Biasedtowardfirst Biasedtowardsecond Error
default 15.0% 53.8% 8.8% 22.5%
Vicuna-13B-Zero-Shot rename 16.2% 12.5% 40.0% 31.2%
score 11.2% 10.0% 0.0% 78.8%
Vicuna-13B-Fine-Tune default 65.0% 27.5% 7.5% 0.0%
29
