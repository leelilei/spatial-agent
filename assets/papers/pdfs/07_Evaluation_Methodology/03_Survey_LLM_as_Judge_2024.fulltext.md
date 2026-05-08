Title: A Survey on LLM-as-a-Judge

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/07_Evaluation_Methodology/03_Survey_LLM_as_Judge_2024.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:08:48+00:00
- page_count: 64
- status: ok
- text_char_count: 227711

Metadata:
- author: Jiawei Gu; Xuhui Jiang; Zhichao Shi; Hexiang Tan; Xuehao Zhai; Chengjin Xu; Wei Li; Yinghan Shen; Shengjie Ma; Honghao Liu; Saizhuo Wang; Kun Zhang; Yuanzhuo Wang; Wen Gao; Lionel Ni; Jian Guo
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Abstract (page 1)
- 1 Introduction (page 2)
- Table of Contents (page 5)
- =Contents (page 5)
- 2 Background and Method (page 6)
  - 2.1 In-Context Learning (page 7)
  - 2.2 Model Selection (page 10)
  - 2.3 Post-processing (page 11)
  - 2.4 Evaluation Pipeline (page 13)
  - 2.5 Quick Practice (page 16)
- 3 Improvement Strategy (page 17)
  - 3.1 Prompt Design Strategy (page 18)
  - 3.2 Capability Enhancement Strategy (page 21)
  - 3.3 Final Output Optimization Strategy (page 23)
- 4 Evaluation of LLM-as-a-Judge (page 25)
  - 4.1 Agreement with Human Judgments (page 25)
  - 4.2 Bias (page 27)
  - 4.3 Adversarial Robustness (page 28)
  - 4.4 Empirical Experiment (page 29)
  - 4.5 Rethinking Meta-evaluation (page 33)
- 5 Applications (page 34)
  - 5.1 Machine Learning (page 35)
  - 5.2 Other Specific Domains (page 38)
- 6 Challenges (page 42)
  - 6.1 Reliability (page 42)
  - 6.2 Robustness (page 43)
  - 6.3 Limitations of Backbone Models (page 43)
  - 6.4 Interpretability and Transparency of Judgments (page 44)
  - 6.5 Meta-Evaluation and Temporal Consistency (page 44)
  - 6.6 Ethical and Social Implications (page 44)
- 7 Future Work (page 45)
  - 7.1 Reasoning-Centric Judgement (page 45)
  - 7.2 Theoretically Grounded Evaluation (page 47)
  - 7.3 More Reliable LLM-as-a-Judge (page 47)
  - 7.4 MLLM-as-a-Judge (page 48)
  - 7.5 Advancing Evaluation Benchmarks (page 48)
  - 7.6 LLM-as-a-Judge for Data Annotation (page 49)
  - 7.7 LLM-as-a-Judge for Scaling (page 49)
  - 7.8 LLM-as-a-Judge for Embodied Intelligence (page 50)
  - 7.9 LLM-as-a-Judge for LLM Optimization (page 50)
  - 7.10 Domain-Specific Reliable Applications (page 50)
- 8 Conclusion (page 51)
- References (page 52)

Markdown Content:

A Survey on LLM-as-a-Judge
JIAWEIGU1,2*,XUHUIJIANG1,3*,ZHICHAOSHI1,4,*,HEXIANGTAN4,XUEHAOZHAI5,
CHENGJINXU1,3,WEILI4,YINGHANSHEN4,SHENGJIEMA1,6,HONGHAOLIU1,
SAIZHUOWANG1,7,KUNZHANG4,ZHOUCHILIN1,BOWENZHANG1,LIONELNI7,8,
WENGAO9,YUANZHUOWANG4,†,JIANGUO1,†,
1IDEAResearch,InternationalDigitalEconomyAcademy,China
2SunYat-senUniversity,China
3DataArcTechLtd,China
4InstituteofComputingTechnology,ChineseAcademyofSciences,China
5DepartmentofCivilandEnvironmentalEngineering,ImperialCollegeLondon,UK
6GaolingSchoolofArtificialIntelligence,RenminUniversityofChina
7TheHongKongUniversityofScienceandTechnology,China
8TheHongKongUniversityofScienceandTechnology(Guangzhou),China
9DepartmentofComputerScienceandTechnology,PekingUniversity,China
ABSTRACT
Accurateandconsistentevaluationiscrucialfordecision-makingacrossnumerousfields,yetitremainsa
challengingtaskduetoinherentsubjectivity,variability,andscale.LargeLanguageModels(LLMs)have
achievedremarkablesuccessacrossdiversedomains,leadingtotheemergenceof"LLM-as-a-Judge,"where
LLMsareemployedasevaluatorsforcomplextasks.Withtheirabilitytoprocessdiversedatatypesand
providescalableandflexibleassessments,LLMspresentacompellingalternativetotraditionalexpert-driven
evaluations.However,ensuringthereliabilityofLLM-as-a-Judgesystemsremainsasignificantchallenge
thatrequirescarefuldesignandstandardization.ThispaperprovidesacomprehensivesurveyonLLM-as-a-
Judge,offeringaformaldefinitionandadetailedclassification,whilefocusingonaddressingthecore
question:HowtobuiltreliableLLM-as-a-Judgesystems?Weexplorestrategiestoenhancereliability,
includingimprovingconsistency,mitigatingbiases,andadaptingtodiverseassessmentscenarios.Additionally,
weproposemethodologiesforevaluatingthereliabilityofLLM-as-a-Judgesystems,supportedbyanovel
benchmarkdesignedforthispurpose.Toadvancethedevelopmentandreal-worlddeploymentofLLM-as-a-
Judgesystems,wealsodiscussedpracticalapplications,challenges,andfuturedirections.
Thissurveyservesasafoundationalreferenceforresearchersandpractitionersinthisrapidlyevolvingfield.
Ourcontributionsspanmultiplelevels:weestablishtheconceptualboundariesofLLM-as-a-Judge,reorganize
fragmentedliteratureintoaunifiedframework,andproposeanovelreliability-orientedbenchmark.Building
onthese,wealsoarticulateaforward-lookingresearchagenda,offeringboththeoreticalfoundationsand
practicalguidanceforconstructingreliableandsociallytrustworthyLLM-as-a-Judgesystems.Theassociated
resourcescanbeaccessedathttps://awesome-llm-as-a-judge.github.io/.
∗Theseauthorscontributedequallytothisresearch.
†Correspondingauthor.
.
,Vol.1,No.1,Article.Publicationdate:October2025.
5202
tcO
91
]LC.sc[
6v49551.1142:viXra

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
1 INTRODUCTION
Judgmentisthefacultyofthinkingtheparticularascontainedundertheuniversal.It
involvesthecapacitytosubsumeunderrules,thatis,todistinguishwhethersomething
fallsunderagivenrule.
——Kant,CritiqueofJudgment[59],IntroductionIV,5:179;CritiqueofPureReason[58],A132/B171.
Recently,LargeLanguageModels(LLMs)haveachievedremarkablesuccessacrossnumerous
domains[178],rangingfromtechnicalfields[142,191,210]tothehumanities[55,100,113,217]
andsocialsciences[45,127,164,177].ThisgrowingintereststemsfromLLMs’abilitytomimic
human-likereasoningandthinkingprocesses,enablingthemtotakeonrolestraditionallyreserved
forhumanexpertswhileofferingacost-effectivesolutionthatcanbeeffortlesslyscaledtomeet
increasingevaluationdemands.Forinstance,theuseofLLM-as-a-Judgeinacademicpeerreview1
offersapotentialmeanstoaddressthesharpgrowthinsubmissionswhilesustainingexpert-level
judgments.
Before the era of LLMs, finding a balance between comprehensive and scalable evaluation
posedapersistentchallenge.Ontheonehand,widelyusedsubjectivemethodslikeexpert-driven
assessments [38, 126] integrate holistic reasoning and fine-grained contextual understanding,
making them the gold standard in comprehensiveness. However, these approaches are costly,
difficulttoscale,andsusceptibletoinconsistency.Ontheotherhand,objectiveassessmentmethods,
such as automatic metrics, offer strong scalability and consistency. For example, tools such as
BLEU[109]orROUGE[85]canrapidlyevaluatemachine-generatedtranslationsorsummaries
againstreferencetextswithouthumanintervention.However,thesemetrics,whichheavilyrelyon
surface-levellexicaloverlaps,oftenfailtocapturedeepernuances,resultinginpoorperformance
intaskslikestorygenerationorinstructionaltexts[122].Asasolutiontothispersistentdilemma,
“LLM-as-a-Judge” has emerged as a promising idea to combine the strengths of the above two
evaluationmethods.Recentstudieshaveshownthatthisideacanmergethescalabilityofautomatic
methodswiththedetailed,context-sensitivereasoningfoundinexpertjudgments[18,79,162,213,
222].Moreover,LLMsmaybecomesufficientlyflexibletohandlemultimodalinputs[17]under
appropriatepromptlearningorfine-tuning[62].TheseadvantagessuggestthattheLLM-as-a-Judge
approachcouldserveasanovelandbroadlyapplicableparadigmforaddressingcomplexand
open-endedevaluationproblems.
LLM-as-a-Judgeholdssignificantpotentialasascalableandadaptableevaluationframework
comparedtotheaforementionedtwotraditionalmethods[158].However,itswidespreadadoptionis
hinderedbytwokeychallenges.Thefirstchallengeliesintheabsenceofasystematicreview,which
highlightsthelackofformaldefinitions,fragmentedunderstanding,andinconsistentusagepractices
intherelevantstudies.Asaresult,researchersandpractitionersstruggletofullyunderstandand
applyeffectively.Thesecondchallengeconcernsreliability[189],asmerelyemployingLLM-as-a-
Judgedoesnotensureaccurateevaluationsalignedwithestablishedstandards.Thesechallenges
emphasizetheneedforadeeperassessmentoftheoutputsgeneratedbyLLM-as-a-Judge,aswell
asacrucialinvestigationintothequestion:HowtobuildreliableLLM-as-a-Judgesystems?
Toaddressthesechallenges,thispaperprovidesasystematicreviewofresearchonLLM-as-a-
Judge.Itoffersacomprehensiveoverviewofthefieldandexploresstrategiesforbuildingreliable
LLM-as-a-Judgesystems.WebeginbydefiningLLM-as-a-Judgethroughbothformalandinformal
definitions,answeringthefoundationalquestion:"WhatisLLM-as-a-Judge?"Next,wecategorize
existingmethodsandapproaches,exploring"HowtouseLLM-as-a-Judge?".Followingthis,totackle
thecriticalquestion:"HowtobuildreliableLLM-as-a-Judgesystems?",weexploretwocoreaspects:
(1) strategies to enhance the reliability of LLM-as-a-Judge systems and (2) methodologies for
1https://blog.iclr.cc/2024/10/09/iclr2025-assisting-reviewers/
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
evaluatingthereliabilityofthesesystems.Forthefirstaspect,wereviewkeystrategiestooptimize
theperformanceofLLM-as-a-Judge.Forthesecondaspect,weexaminethemetrics,datasets,and
methodologiesusedtoevaluateLLM-as-a-Judgesystems,highlightingpotentialsourcesofbias
andmethodsfortheirmitigation.Buildingonthis,weintroduceanovelbenchmarkspecifically
designedforevaluatingLLM-as-a-Judgesystems.Finally,wediscussfutureresearchdirections,
emphasizingkeyareasforimprovingreliability,scalability,andapplicability.Thecontributionsof
thisstudycanbesummarizedasfollows:
(1) Atthedefinitionallevel,weestablishbothformalandinformaldefinitionsofLLM-as-a-
Judge,therebydelineatingtheconceptualboundariesofthisemergingparadigm.Wealso
introduceacontextualizeddefinitionofreliability,whichincorporatesinputvariability,model
characteristics,andcontextualdependencies,providingaprincipledfoundationfortheorizing
andbuildingreliablesystems.
(2) Attheframeworklevel,weconductasystematicreorganizationoffragmentedliterature
intoaunifiedconceptualstructure.Specifically,wemappriorworktofourfoundational
questions: what it is, how to use it, how to improve it, and how to evaluate it—framing
reliabilityastheunifyingthreadacrossthesedimensions.
(3) Attheempiricallevel,weperformcomparativeanalysesofexistingapproachesandfurther
proposeameta-evaluationbenchmarkspecificallytailoredforevaluatingLLM-as-a-Judge
systems.Thisbenchmarkfacilitatessystematicreliabilityassessment,uncoveringkeytrade-
offssuchasrobustnessversussensitivity,andofferingactionableinsightsforconstructing
trustworthyevaluationframeworks.
(4) Attheperspectivelevel,weofferacomprehensiveanalysisthatintegratestheapplications,
challenges,andfuturedirectionsofLLM-as-a-Judge,providingaroadmapthatextendsbeyond
thescopeofexistingsurveys.Bysystematicallyreviewingitsapplicationsincoremachine
learningandhigh-stakesdomains,weidentifydomain-specificreliabilityrequirementsand
underexplored challenges such as meta-evaluation and long-term consistency. Building
on these findings, we articulate a forward-looking agenda that emphasizes theoretically
groundedmethodologies,systematicbenchmarks,andhybridhuman–AIframeworksfor
constructingreliableandsociallytrustworthysystems.
TherestofthissurveyisorganizedasFigure1.Specifically,Section2providesanoverviewofthe
LLM-as-a-Judgefield,includingitsdefinitionsandcategorizationofexistingmethods.Foraquick
guideontheimplementationofanLLMasajudgeforspecificscenarios,youcanfindanswers
inQuickPractice(2.5).StrategiesforenhancingandevaluatingthereliabilityofLLM-as-a-Judge
systems are discussed in Sections 3 and 4 respectively. Notably, in Section 7.1, we discuss the
synergybetweenLLM-as-a-JudgeandReasoning-Centricenhancement,wheredynamicfeedback
isusedtooptimizereasoningpathsandsignificantlyimprovethemodel’sabilitytosolvecomplex
problems.Section5explorespracticalapplications,whileSections6and7addresschallengesand
outlinefutureresearchdirections.Finally,Section8presentsourconclusions.
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
[Section 2]
[Section 2]
[Section 3]
[Section 4]
[Section 5]
[Section 6]
[Section 7]
Fig.1. Theoverallframeworkofthispaper.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
Contents
Abstract . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2 BackgroundandMethod . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
2.1 In-ContextLearning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 ModelSelection . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.3 Post-processing. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.4 EvaluationPipeline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
2.5 QuickPractice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
3 ImprovementStrategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.1 PromptDesignStrategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.2 CapabilityEnhancementStrategy . . . . . . . . . . . . . . . . . . . . . . . . . . 21
3.3 FinalOutputOptimizationStrategy . . . . . . . . . . . . . . . . . . . . . . . . . 23
4 EvaluationofLLM-as-a-Judge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.1 AgreementwithHumanJudgments . . . . . . . . . . . . . . . . . . . . . . . . . 25
4.2 Bias . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
4.3 AdversarialRobustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
4.4 EmpiricalExperiment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.5 RethinkingMeta-evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
5 Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
5.1 MachineLearning . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.2 OtherSpecificDomains . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
6 Challenges . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
6.1 Reliability . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
6.2 Robustness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
6.3 LimitationsofBackboneModels . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
6.4 InterpretabilityandTransparencyofJudgments . . . . . . . . . . . . . . . . . . 44
6.5 Meta-EvaluationandTemporalConsistency . . . . . . . . . . . . . . . . . . . . . 44
6.6 EthicalandSocialImplications . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
7 FutureWork . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
7.1 Reasoning-CentricJudgement. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
7.2 TheoreticallyGroundedEvaluation. . . . . . . . . . . . . . . . . . . . . . . . . . 47
7.3 MoreReliableLLM-as-a-Judge . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
7.4 MLLM-as-a-Judge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
7.5 AdvancingEvaluationBenchmarks . . . . . . . . . . . . . . . . . . . . . . . . . . 48
7.6 LLM-as-a-JudgeforDataAnnotation . . . . . . . . . . . . . . . . . . . . . . . . . 49
7.7 LLM-as-a-JudgeforScaling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
7.8 LLM-as-a-JudgeforEmbodiedIntelligence . . . . . . . . . . . . . . . . . . . . . 50
7.9 LLM-as-a-JudgeforLLMOptimization . . . . . . . . . . . . . . . . . . . . . . . . 50
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
7.10 Domain-SpecificReliableApplications . . . . . . . . . . . . . . . . . . . . . . . . 50
8 Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
2 BACKGROUNDANDMETHOD
ThecapacityofLLMstoemulatehumanreasoningandevaluatespecificinputsagainstasetof
predefinedrules has pavedthe wayfor "LLM-as-a-Judge." Existing studiesindicate thatLLM’s
scalability,adaptability,andcost-effectivenessmakethemwell-suitedforagrowingnumberof
evaluativetasksthatweretraditionallydonebyhumans.TheseabilitiesarekeyinutilizingLLMs
flexiblyacrossvariousevaluationscenariosandobjectives.Asaresult,theadoptionofLLMin
evaluationhasprogressedrapidlyinpractice.Initially,theprimaryfocusofLLMswasonlanguage
generation and comprehension. With advancements in training paradigms like Reinforcement
LearningfromHumanFeedback(RLHF)[108],LLMsbecameincreasinglyalignedwithhuman
valuesandreasoningprocesses.ThisalignmenthasallowedLLMstotransitionfromgenerative
taskstoevaluation.Atitscore,LLM-as-a-JudgedenotestheuseofLLMstoevaluateobjects,actions,
ordecisionsbasedonpredefinedrules,criteria,orpreferences.Itencompassesabroadspectrum
of roles, including: Graders [28, 150], Evaluators/Assessors [80, 197], Critics [61, 111, 174],
Verifiers[88,128,165],Examiners[8],Reward/RankingModels[98,136,179,193],etc.
Currently,thedefinitionofhowtoeffectivelyuseLLM-as-a-Judgeforevaluationtasksislargely
informalorvague,lackingaclearandformalexpression.Therefore,wewillstartwithaformal
definitionofLLM-as-a-Judgeasfollows:
E ←P (𝑥 ⊕ C)
LLM
• E:ThefinalevaluationobtainedfromthewholeLLM-as-a-Judgeprocessintheexpected
manner.Itcouldbeascore,achoice,alabelorasentence,etc.
• P :TheprobabilityfunctiondefinedbythecorrespondingLLM,andthegenerationis
LLM
anauto-regressiveprocess.
• 𝑥:Theinputdatainanyavailabletypes(text,image,video),whichwaitingtobeevaluated.
• C:Thecontextfortheinput𝑥,whichisoftenprompttemplateorcombinedwithhistory
informationindialogue.
• ⊕:Thecombinationoperatorcombinestheinput𝑥 withthecontextC,andthisoperation
canvarydependingonthecontext,suchasbeingplacedatthebeginning,middle,orend.
TheformulationofLLM-as-a-JudgereflectsthatLLMisatypeofauto-regressivegenerative
model,whichgeneratessubsequentcontentbasedonthecontexttoobtaintargetevaluation.It
illustrateshowweutilizeLLMforevaluationtasks,encompassinginputdesign,modelselection,and
training,aswellasoutputpost-processing.ThebasicapproachesofimplementingLLM-as-a-Judge
canbeclassifiedbytheformulation:In-ContextLearning,ModelSelection,Post-processingMethod,
andEvaluationPipelineinFigure2.Byfollowingthispipeline,onecanbuildabasicLLM-as-a-Judge
forevaluation.Aquickpracticeguideisavailableinsection2.5.However,thebasicdefinitionalone
doesnotguaranteethereliabilityofevaluations.Toexplicitlyhighlightandaddressreliability,we
furtherproposethefollowingenhancedformaldefinition:
R ← 𝑓 (P ,𝑥,C)
R LLM
• R:Theevaluationexplicitlydesignedtoensureconsistency,robustness,andalignmentwith
humanjudgment.Thisreliabilityisverifiedthroughadditionalvalidation,calibration,and
standardizationstepsbeyondthebasicpipeline.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
LLM-as-a-Judge Evaluation Pipeline
To grade/evaluate/critique/verify/examine/rankdata, models, or agents
Scores General LLM Special Tokens Numbers
S a h n i c g d o h r 1 e e 0 s , t t . h w e it r h e 1 s 0 p o b n e s i e n g b e th tw e een 1 • Closed-source LLM • • T Re h s e p s o c n o s r e e 1 i s is 4 b . etter. 4
… • Options 1, 3, 4, and 6
Yes or No • Open-source LLM contain errors. Options
Text Is this response fact- … Logits Response1 / Modification
Image supported? needed.
Video Pairs Finetuned LLM Probability = Probability
Inputs W hu h m i a c n h - r li e k s e p ? onse is more Ev I a n l s u t a r t u e c d t i d o a n ta s O o L p u L e r M n c - e Selected sentences 0.3284
Multiple-choice Evaluations Choices
• sub-question: How many
S th e a le t c c t o t n h ta e i n r e f s a p c o t n u s a e l s b b as e i l s o . w LLM-as-a-Judge Evaluator p to a d ge ay s ? d id Julie read A,B,C,D; 1,3,4,6
In-Context Learning Model Selection Post-Processing Evaluation
Fig.2. LLM-as-a-Judgeevaluationpipelines.
• 𝑓 :AseriesofconstraintsandvalidationmethodsappliedsystematicallytothebasicLLM-
R
as-a-Judgeframeworktoenhanceevaluationreliability.Theseincludemethodstomitigate
biases,controlvariability,andconfirmrobustnessagainstadversarialinputs.
2.1 In-ContextLearning
ToapplyLLM-as-a-Judge,evaluationtasksaretypicallyspecifiedusingIn-ContextLearningmeth-
ods,whichprovideinstructionsandexamplestoguidethemodel’sreasoningandjudgment.This
processinvolvestwokeyaspects:inputdesignandpromptdesign.Forinputdesign,itisimportant
toconsiderthetypeofvariablestobeevaluated(suchastext,image,orvideo),themannerofinput
(e.g.,individually,inpairs,orinbatches),anditsposition(e.g.,atthebeginning,middle,orend).
Forthepromptdesign,fourdifferentmethodscanbeadopted,asillustratedinFigure2.These
methodsincludegeneratingscores,solvingtrue/falsequestions,conductingpairwisecomparisons,
andmakingmultiple-choiceselections.Furtherdetailswillbepresentedinthefollowingsections.
2.1.1 Generatingscores. Itisquiteintuitivetorepresentanevaluationusingacorresponding
score,showninFigure3.Whatrequiresmorecarefulconsideration,however,isthenatureand
rangeofthescoreusedforevaluation.Thescorecanbediscrete,withcommonrangeslike1-3,
1-5[56],or1-10[79,222].Alternatively,itcanbecontinuous,rangingfrom0to1or0to100[174].
Thesimplestwaytoscoreisthroughthecontext,settingtherangeofscoresandthemaincriteria
forscoring.Forexample,"Pleaseratethehelpfulness,relevance,accuracy,levelofdetailsoftheir
responses.Eachassistantreceivesanoverallscoreonascaleof1to10,whereahigherscoreindicates
betteroverallperformance"[222].Aslightlymorecomplexwayistoprovidemoredetailedscoring
criteria.MorecomplexscoringsituationscanbeasLanguage-Model-as-an-Examiner [8],which
useLikertscalescoringfunctionsasanabsoluteevaluativemeasure.Theevaluatorassignsscores
toagivenresponsealongpredefineddimensions,includingaccuracy,coherence,factuality,and
comprehensiveness.Eachofthesedimensionsisscoredonascaleof1to3,rangingfromworstto
best.Theevaluatorisalsoaskedtoprovideanoverallscorerangingfrom1to5,basedonthescores
assignedtotheprevious4dimensions.Thisscoreservesasanindicatoroftheoverallqualityof
theanswer.
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
Discrete Scores Continuous Scores
1-3
1-5 0-1
Likert
ChartMimic
1-5
Likert 0-100
G-Eval
LLaVA-Critic
1-10 Judge
with scores
Score the response between……
Fig.3. TheillustrationsofmethodgeneratingscoresinICL
EvaluationPromptTemplatesfromGaoetal.[38]
LikertScaleScoring:
Evaluatethequalityofsummarieswrittenforanewsarticle.Rateeachsummaryonfour
dimensions:{Dimension_1},{Dimension_2},{Dimension_3},and{Dimension_4}.Youshould
rateonascalefrom1(worst)to5(best).
Article:{Article}
Summary:{Summary}
PairwiseComparison:
Givenanewarticle,whichsummaryisbetter?Answer"Summary0"or"Summary1".You
donotneedtoexplainthereason.
Article:{Article}
Summary0:{Summary_0}
Summary1:{Summary_1}
2.1.2 SolvingYes/Noquestions. AYes/Noquestionrequiresajudgmentonagivenstatement,
focusingsolelyonitsaccuracy.Thistypeofquestionissimpleanddirect,providingonlytwofixed
responses—yesorno,trueorfalse—withoutanyadditionalcomparisonsorchoices.
Thistypeofevaluationisoftenutilizedinintermediateprocesses,creatingtheconditionsfora
feedbackloop.Forexample,itpromotesaself-optimizationcycle,asseeninReflexion[128],which
generatesverbalself-reflectionstoprovidevaluablefeedbackforfutureattempts.Inscenarioswith
sparserewardsignals,suchasabinarysuccessstatus(success/fail),theself-reflectionmodeluses
thecurrenttrajectoryandpersistentmemorytogeneratenuancedandspecificfeedback.Similarly,
inself-improvementcontexts[145],Yes/Noquestionscanbeemployedtoevaluatecustomphrases,
suchas"Modification needed."and"No modification needed.",facilitatingentryintothe
nextcycle.Moreover,theseevaluationsarecommonfortestingknowledgeaccuracyandassessing
whetherstatementsalignwithestablishedfacts[135],like"Givenaquestionandtheassociated
retrievedknowledgegraphtriples(entity,relation,entity),youareaskedtoanswerwhetherit’s
sufficientforyoutoanswerthequestionwiththesetriplesandyourknowledge(YesorNo)."A
detailedandspecificexamplecanbeseenintheFigure4.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
EvaluationPromptTemplatesforYes/NoandMultiple-ChoiceTasks
Yes/NoEvaluation:
Isthesentencesupportedbythearticle?Answer"Yes"or"No".
Article:{Article}
Sentence:{Sentence}
Multiple-ChoiceEvaluation:
Youaregivenasummaryandsomesemanticcontentunits.Foreachsemanticunit,choose
thosecanbeinferredfromthesummary,returntheirnumber.
Summary:{Summary}
Semanticcontentunits:
1.{SCU_1}
2.{SCU_2}
......
n.{SCU_n}
Score comparison
Word yes/no
Provide comparison results
Binary number 0/1 Binary sentence options C b h e o tt o e s r e o t n h e e " ” [ [ A B] ] ” " " b [ e [ t A t ] e ] r " , i " f [ a [B s ] s ] i " st i a f nt A is
"Modification needed." " [C]" assistant B is better,
"No modification needed." ”Response A." and "[[C]]" for a tie.
Judgeby
pairwise
comparisons
Judge
yes or no
Which response is better ?
Two options Three options Four options
Is this response …… ?
Win Win Win
Lose Tie Both good tie
Lose Both bad tie
Lose
Methods for Solving Yes/No questions Methods for Conducting pairwise comparisons
Fig.4. TheillustrationsofmethodSolvingYes/NoquestionsandConductingpairwisecomparisonsinICL
2.1.3 Conductingpairwisecomparisons. Pairwisecomparisonreferstocomparingtwooptions
andselectingwhichoneissuperiorormorealignedwithaspecificstandard,showedinFigure4.It
involvesmakingadecisionbetweentwooptionsratherthanjudgementbetween’yes’or’no’.The
comparisoncanbesubjectiveorbasedonobjectivecriteria.Thisevaluationisarelativeevaluation.
Pairwisecomparisonisoftenusedforrankingmultipleoptionsorprioritizingthem,whereseveral
comparisonsaremadebetweenpairstoidentifythebetterchoiceorestablishahierarchy.
Pairwisecomparisonisawell-establishedmethodthathassignificantlyimpactedavarietyof
fields [112]. As noted by [95], LLM and human evaluations are more aligned in the context of
pairwisecomparisonscomparedtoscore-basedassessments.Numerousstudieshavedemonstrated
thatpairwisecomparativeassessmentsoutperformotherjudgingmethodsintermsofpositional
consistency[96,213].Furthermore,pairwisecomparisonscanbeextendedtomorecomplexrelation-
basedassessmentframeworks,suchaslist-wisecomparisons,usingadvancedrankingalgorithms
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
[95,112],datafiltering[193].Inpairwisecomparativeassessments,LLM-as-a-Judgeispromptedto
selecttheresponsethatbetteranswersthequestionathand.Toaccommodatethepossibilityof
atie,severaloptionmodesareintroduced.TheTwo-Optionmoderequiresjudgestochoosethe
betterresponsefromtwogivenoptions.TheThree-Optionmodeintroducesanadditionalchoice,
allowingjudgestoindicateatieifneitherresponseispreferable,asshowninFigure4.Evaluations
typicallyinvolvedeterminingtheoutcomesofwin,tie,orlossforresponses[162]throughpairwise
comparisons,withwinroundscountedforeachresponse.TheFour-Optionmodefurtherexpands
thechoices,allowingjudgestoclassifyresponsesaseithera"bothgoodtie"ora"bothbadtie."
2.1.4 Makingmultiple-choiceselections. Multiple-choiceselectionsinvolveprovidingseveral
options,notgivingrelativechoicesinpairwisecomparison,normakingayes/nojudgment.The
evaluatormustchoosethemostappropriateorcorrectone.Thismethodallowsforabroaderrange
ofresponsescomparedtotrue/falsequestionsandcanassessdeeperunderstandingorpreferences.
However,thiskindofpromptdesignismorerarethanthefirstthree.
ReliabilityConcernsofIn-ContextLearning
When leveraging in-context learning, certain issues can surface, potentially impacting
thereliabilityofevaluations.TheseincludethevariabilityofLLMoutputsduetominor
promptchanges,whichcanleadtounstableresults.Furthermore,score-basedassessments
oftenexhibitinconsistentinter-raterreliability,influencedbytheinherentrandomnessof
LLMgenerationanditssensitivitytophrasing.Similarly,evaluationformatslikeYes/No
or multiple-choice questions are prone to ambiguity in response interpretation. Lastly,
LLM-as-a-Judgeevaluationsmayinadvertentlyreflectbiases,suchasfavoringresponses
basedontheirpositionorlength.
2.2 ModelSelection
2.2.1 GeneralLLM. ToautomateevaluationbyLLM-as-a-Judge,oneeffectiveapproachisto
employadvancedlanguagemodelssuchasGPT-4[107]insteadofhumanevaluators[213].For
instance, Li et al. [81] created a test set with 805 questions and assessed the performance by
comparingittotext-davinci-003usingGPT-4.Additionally,Zhengetal.[213]designed80multi-
roundtestquestionsacrosseightcommonareasandusedGPT-4toautomaticallyscorethemodel’s
responses.TheaccuracyoftheGPT-4-basedevaluatorhasbeendemonstratedtobehighcompared
toprofessionalhumanevaluators,showingsuperiorconsistencyandstabilityinevaluations.Atthe
sametime,ifthegeneralLLMusedhaslimitationsininstruction-followingorreasoningabilities,
theeffectivenessoftheLLM-as-a-Judgemethodmaybesignificantlyaffected.
2.2.2 Fine-tunedLLM. However,relyingonexternalAPIforevaluationmayintroducecon-
siderationaboutprivacyleakage,andtheopacityofAPImodelsalsochallengestheevaluation
reproducibility.Therefore,subsequentstudiesrecommendrefininglanguagemodelstailoredfor
evaluationsbyemphasizingtheuseofpairwisecomparisonsorgrading.Forinstance,PandaLM
[162]constructsdatabasedonAlpacainstructionsandGPT-3.5annotation,andthenfine-tunes
LLaMA-7B[147]asanevaluatormodel.JudgeLM[222]constructsdatafromdiversifiedinstruction
setsandGPT-4annotations,andfine-tunesVicuna[148]asascalableevaluatormodel.Auto-J
[79] constructs evaluation data upon multiple scenarios to train a generative evaluator model,
which can provide both evaluation and critical opinion. Prometheus [63] defines thousands of
evaluationcriteriaandconstructsafeedbackdatasetbasedonGPT-4,andfine-tunesafine-grained
evaluatormodel.Thetypicalprocessforfine-tuningajudgemodelinvolvesthreemainsteps.Step
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
1:DataCollection.Thetrainingdatagenerallyconsistsofthreecomponents:instructions,the
objectstobeevaluated,andevaluations.Instructionsaretypicallysourcedfrominstructiondatasets,
whileevaluationscancomefromeitherGPT-4orhumanannotations.Step2-PromptDesign.
Thestructureoftheprompttemplatecanvarybasedontheevaluationscheme,whichalready
detailedin§2.1.Step3:ModelFine-Tuning.Usingthedesignedpromptsandcollecteddata,
thefine-tuningprocessfortheevaluatormodeltypicallyadherestotheinstructionfine-tuning
paradigm[108].Themodelreceivesaninstructionalongwithoneormoreresponsestogenerate
outputthatincludesevaluationresultsandpossiblyexplanations.
Afterfine-tuning,theevaluatormodelcanbeemployedtoevaluatethetargetobject.While
thesefine-tunedmodelsoftendemonstratesuperiorperformanceonself-designedtestsets,they
are identified several limitations in their evaluation capabilities,which detailed in Section 4.2.
Thecurrentpromptandfine-tuningdatasetdesignsoftenresultinevaluationLLMswithpoor
generalization,makingthemdifficulttocomparewithstrongLLMslikeGPT-4.
ReliabilityConcernsofModelSelection
ThechoiceofmodelsignificantlyimpactsthedependabilityofLLM-as-a-Judgesystems.
Concerns arise from the black-box nature and version dependency of general-purpose
LLMs,whichcanhinderthereproducibilityofevaluationoutputs.Fine-tunedevaluators,
whilespecialized,oftenexhibitoverfittingandlimitedgeneralizationbeyondtheirtraining
data.Moreover,thesemodelscaninheritsubtlebiasesfromtheirtrainingdatasets,necessi-
tatingcarefulmeta-evaluationtoensurefairness.Finally,relianceonsmalleropen-source
models,whilecost-effective,mayintroduceinconsistenciesandmisalignmentwithhuman
judgments.
2.3 Post-processing
Post-processingrefinestheprobabilitydistributionsgeneratedbyLLM-as-a-Judgetoensureaccu-
rateevaluations.TheevaluationformatshouldalignwithourIn-ContextLearningdesignandmay
involveprocedurestoenhancethereliabilityofextractedevaluations,whichshouldbeapplied
consistently.Wefocusonthreemainpost-processingmethods:extractingspecifictokens,normal-
izingtheoutputlogits,andselectingsentenceswithhighreturns.However,itisimportanttonote
thateachmethodhassignificantlimitationswhenevaluatingobjectivequestions.Forexample,in
textresponseevaluation[189],failingtoaccuratelyextractthekeyanswertokenfromtheLLM’s
response can result in incorrect evaluation outcomes. These challenges in post-processing are
tightlylinkedtothepromptdesignusedinearlierICLstagesandtheselectedmodel’sabilityto
followinstructionsreliably.
2.3.1 Extractingspecifictokens. AsshowedinIn-contextLearning(Section2.1),whenthe
evaluationtargettaketheformofascore,selectingspecificoptions,orrespondingwithYes/No,
applying rule-match to extract the corresponding token from the response generated during
probabilitydistributioniterationiscommonused.ItisworthnotingthatYes/Noisabroaddefinition,
includingcustomstatementsinvolvingjudgment.ConsideringaYes/Noquestionforevaluationin
customphrases[145]:"Modification needed."and"No modification needed."orayes-no
question"Does the above answer need to be further modified?".Whentheinputsample
isputthroughthetemplate,itmighthaveoutputssuchas"Modificationneeded.","Conclusion:
Modificationneeded."or"Yes".Thisvarianceinresponseformatsisdifficulttoparseconsistently.
Thecorrespondingpost-processingwiththeresponseisnecessary.Usingrulestoextractspecific
tokensforourdesignedpromptsandinputcontent,aswellasthebackbonemodelusedforthe
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
evaluator,allhavehigherrequirementsaswediscussedinSection2.2.Incontextuallearning,if
thereisnoclearindicationoftheoutputformatforresponse,theremaybevariousexpressionsof
evaluation,whichcanbeseeninFigure2.Forexample,"Response1isbetter"and"Thebetterone
isresponse1",whichconveythesamechoicebutdifferinformatleadingtothedifficultyofrule
recognition.Simplesolutionsofteninvolveprovidingclearinstructions,suchas"Thelastsentence
shouldbestartedwith’Thebetterresponseis’",orusingafew-shotstrategy.Also,thegeneral
modelwithinsufficientinstructionfollowingcapabilitymaynotbeabletogeneratetheevaluation
format and content of the target according to the instruction, resulting in the post-processing
extractedaccordingtotherulesnotassmoothasexpected.
ConstraineddecodingisatechniquethatenforcesstructuredoutputfromLargeLanguageModels
(LLMs)byrestrictingtokengenerationaccordingtopredefinedschemas,typicallyinformatslike
JSON.Thisapproachusesafinitestatemachine(FSM)tocomputevalidnexttokensateachdecoding
step,effectivelymaskingthemodel’soutputprobabilitydistributiontoensureconformitywith
thedesiredschema.Whilethismethodguaranteessyntacticallyvalidoutputs,itpresentsseveral
challenges:itcandistortthemodel’slearneddistributionandpotentiallydegradeoutputquality,
requiressignificantengineeringimplementationeffort,andintroducescomputationaloverhead
duringinference.
Recentworkhasproposedvarioussolutionstoaddressthesechallenges.[11]introducesDOMINO,
adecodingalgorithmthatpreservesnaturaltokenizationwhileenforcingconstraints.Theirsystem
minimizesoverheadthroughprecomputationandspeculativedecoding,sometimesachievingfaster
performancethanunconstraineddecoding.[29]developsXGrammar,whichacceleratesgrammar-
constrainedgenerationbyseparatingtokensintothosethatcanbepre-checkedandthoserequiring
runtimeverification.Byco-designingthegrammarenginewithLLMinference,theyachieveup
to100xspeedupoverexistingapproaches.[215]presentsSGLang,combiningadomain-specific
languagewithanoptimizedruntime.TheirsystemfeaturesefficientKVcachereuseandcompressed
finitestatemachinesforfasterdecoding,demonstratingthatthoughtfulco-designofprogramming
modelandruntimecanminimizeconstraineddecodingoverhead.
2.3.2 Normalizingtheoutputlogits. LLM-as-a-JudgeintheintermediatestepswithYes/No
settingoftennormalizestheoutputlogitstoobtaintheevaluationintheformofacontinuous
decimalbetween0and1.Thisisalsoverycommoninagentmethodsandprompt-basedoptimization
methods[43,165,225].Forexample,theself-consistencyandself-reflectionscores[165]within
oneforwardpassofM ,areeffectivelyobtainedbyconstructingaprompt[(𝑥 ⊕C),"Yes"]
Evaluator
andacquiretheprobabilityofeachtokenconditionedontheprevioustokens𝑃(𝑡 𝑖|𝑡 <𝑖).Theauto-
regressivefeatureisleveraged,thusaggregatetheprobabilityoftherelevanttokenstocomputethe
self-consistentscore𝜌 andself-reflectionscore𝜌 .Thefinalscoreisproduced
Self-consistency Self-reflection
by𝜌 𝑗 =𝜌 SC,𝑗 ·𝜌 SR,𝑗.
𝜌 𝜌
(cid:32)(cid:32)(cid:32) SC(cid:32)(cid:32)(cid:32) SR (cid:40)
(cid:122)
(𝑥
(cid:125)
⊕
(cid:124)
C
(cid:123)
)
(cid:122)
"Y
(cid:125)
e
(cid:124)
s
(cid:123)
" ⇒
𝜌
SC
=(cid:206)
𝑡𝑖∈𝛼
𝑃(𝑡 𝑖|𝑡 <𝑖)·(cid:206)
𝑡𝑖∈𝛽
𝑃(𝑡 𝑖|𝑡 <𝑖)
−−−−−−−−−−−−−→ 𝜌
SR
=(cid:206)
𝑡𝑖∈"Yes"
𝑃(𝑡 𝑖|𝑡 <𝑖)
Inaddition,Self-evaluation[43]isalsocommonusingthismethodforLLM-as-a-Judge.Itcanbe
helpfultolettheLLMevaluateitselfbyasking,"Isthisreasoningstepcorrect?"andthenrewardit
basedontheprobabilityofthenextwordbeing"Yes."
2.3.3 Selectingsentences. Inadditiontoselectingspecifictokensandnormalizingtheoutput
logits,thecontentextractedbyLLM-as-a-Judgemayalsobeasentenceorparagraph.Asshowed
inFigure2,agentforreasoningtask[43],buildsareasoningtreebyiterativelyconsideringthe
mostpromisingreasoningsteps(actions,sub-questions)byLLM-as-a-Judge.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
ReliabilityConcernsofPost-processingMethod
Thepost-processingstepsappliedtoLLMoutputsintroducetheirownsetofreliability
challenges. Rule-based token extraction methods are inherently brittle and susceptible
tominorvariationsinresponses,potentiallyleadingtosilenterrors.Whilelogit-based
normalizationoffersprobabilisticscoring,itseffectivenessishighlydependentonprecise
promptdesignandconsistentmodeltokenization,whereinconsistenciescanintroduce
noise.Furthermore,methodsfocusingonsentence-levelevaluationorresponseselection
riskpropagatingbiasesifthescoringLLMisoverlysensitivetostylisticratherthansub-
stantivecues.Ultimately,allpost-processingstrategiesremainvulnerabletoadversarial
manipulationsdesignedtoinflateevaluationscoreswithoutgenuinecontentimprovement.
2.4 EvaluationPipeline
Aftercompletingthethreeprocesses,weobtainthefinalevaluationE.Frominputtooutput,these
stepscollectivelyconstitutetheLLM-as-a-Judgeevaluationpipeline,asillustratedinFigure2.This
pipelineiscommonlyappliedinfourscenarios:LLM-as-a-Judgeformodels,LLM-as-a-Judgefor
data,LLM-as-a-Judgeforagents,andLLM-as-a-Judgeforreasoningorthinking.
for Models for Data
LLM-as-a-Judge
Informal Definition
for Agents What is LLM-as-a Judge? for Reasoning/Thinking
Formal Definition
In-Context Learning
Model Selection
Fig.5. FourtypicalscenariosusingLLM-as-a-Judgeevaluationpipeline.
How to use LLM-as-a-Judge? Post-processing
Evaluation Pipeline
Quick Practice
Improving Prompts
(ICL Based)
Auto-J Wins Tie Auto-J Loses
Improving LLMs' Abilities
How to improSveel FLeLeM-as-a-Judge? 94.0% (Model B0a.s4e%d)5.6%
Arena Improving Final Results
L2Chat 84.5% (Post-proces0si.n9g% B1a4s.7e%d)
WizardLM 80.6% 3.0%16.4%
Basic metric
Vicuna 77.6%Bias 0.4% 22.0%
How to evaluate LLM-as-a-Judge? Adversarial Robustness
ChatGPT 73.7% 2.2%24.1%
LLM-as-a-Judge Meta-evaluation
GPT-4 54.3% 0.9B%enchm44a.r8k%
Why is LLM-as-a-Ju0.d0g%e im2p0o.0r%tant 4fo0.r0 A%GI?60.0% 80.0% 100.0%
Win-rate of AUTO-J against other models
Model Arena built by LLM-as-a-Judge Machine Learning
judged by GPT-4
Application Finance
Law
Fig.6. TheillustrationsofthescenarioLLM-as-a-JudgeforMOotdheerl ssp.eTcifihce doemxaainms pleof"win-tie-lose"isfromLi
Ai4Sci
etal.[79]
Others
Reliability
Challenges Robustness
,VPoowl.e1rf,ulN Boac.k1b,onAer Mtiocdleel.Publicationdate:October2025.
More Reliable LLM-as-a-Judge
LLM-as-a-Judge for Data Annotation
Future work MLLM-as-a-Judge
More LLM-as-a-Judge Benchmarks
LLM-as-a-Judge for LLM Optimization

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
2.4.1 LLM-as-a-JudgeforModels. ItisuniversallyknownthatthebestwaytoevaluateLLMsis
humanjudgment,butcollectinghumanannotationscanbecostly,time-consuming,andlaborious
[108,213].UsingstrongLLMs(usuallyclosed-sourceones,e.g.,GPT-4,Claude,ChatGPT)asan
automated proxy for assessing LLMs has become a natural choice [218], as shown in Figure 2.
Withappropriatepromptdesign,thequalityofevaluationandagreementtohumanjudgment
canbepromising[32,155,207,213].However,thecostconcernstillexistswhencallingtheAPIs
of these proprietary models, especially when there is a frequent need for model validation on
large-scale data. Moreover, closed-source LLM-as-a-Judge leads to low reproducibility due to
potentialchangesinmodelsbehindtheAPI.Somerecentworkshavestartedtomakeattemptsfor
open-sourcealternatives.SelFee[186]collectsgenerations,feedback,andrevisedgenerationsfrom
ChatGPTandfine-tunesLLaMAmodelstobuildacritiquemodel.Shepherd[159]trainsamodel
thatcanoutputcritiquesforsingle-responsewiththedataoffeedbackfromonlinecommunities
andhumanannotation.PandaLM[162]trainsamodeltoconductpairwisecomparisonforLLM
Instruction Tuning Optimization, and Zheng et al. [213] also fine-tune Vicuna [148] on a 20K
pairwisecomparisondatasettoexplorethepotentialofopen-sourcemodelsasamorecost-friendly
proxy.
2.4.2 LLM-as-a-JudgeforData. Dataannotationgenerallyreferstothelabelingorgenerating
ofrawdatawithrelevantinformation,whichcouldbeusedforimprovingtheefficacyofmachine
learning models. The process, however, is labor-intensive and costly. The emergence of LLMs
presentsanunprecedentedopportunitytoautomatethecomplicatedprocessofdataannotationby
LLM-as-a-Judge.MostofthedataneedtobeevaluatedbyLLM-as-a-Judgeisgeneratedbymodels,
orlarge-scalecrawleddata.Languagemodelsfirstconductsupervisedfine-tuningtoimitatehowto
alignwithhumaninstructions[143,160].Afterthat,reinforcementlearningtechniqueshavebeen
exploredtoalignlanguagemodelswithhumanpreferences[108,118].Themostsuccessfulwayis
applyingaRLHFframework[108]viatrainingarewardmodelonhumanfeedbackandusingPPO
[123]toobtainthepolicymodelforlanguagegeneration.However,inpractices,thePPOtraining
paradigmiscomplexincodingandhyper-parametertuningwhileitneedsfourmodelsthatare
hardfortraining.Thismotivatesustoexploresimplerandmorestraightforwardmethodstoalign
languagemodelswithhumanpreferences.ThisinvolveshowtouseLLM-as-a-Judgetoevaluate
whetherdifferentresponsesarealignedwithhumanpreferences.Forexample,[28,193]usegeneral
LLM(ChatGPT)togetbetteralignmentwithhumanpreferences.TheAplacaprompts[143]is
usedassamplingqueriestodifferentmodelsgenerateresponses.Andthesedatawasevaluated
by LLM-as-a-Judge to obtain human preference scores (reward score) to train a new language
model.OtherworkswouldliketouseSupervisedFine-Tuning(SFT)modelitselfasevaluator,like
generatingbetter-aligneddatasetsforSFTincludinghindsight-modifiedprompts[91,205]and
principle-drivenself-alignment[137].
Inaddition,thelackofdomain-specificmodeltrainingdataisacommonphenomenon.Inorderto
obtainannotatedhigh-qualitydata,itisalsoverycommontouseLLM-as-a-Judgeforthegeneration
andevaluationofdomaindata.WizardMath[98]woulduseitsInstructionRewardModel(IRM)as
Evaluator,aimingtojudgethequalityoftheevolvedinstructionsonthreeaspects:i)Definition,ii)
Precision,anditi)Integrity.ToproducetherankinglisttrainingdataofIRM,foreachinstruction,
ChatGPTandWizard-Eareusedtogenerate2-4evolvedinstructionsrespectively.Thenweleverage
Wizard-Etorankthequalityofthose4-8instructions.
However,solelyrelyingonLLM-as-a-Judgefordataannotationposeschallenges,particularly
as the value of annotated data diminishes with the rapid improvement of model performance.
To address this, approaches like Self-Taught Evaluator [158] offer a promising alternative by
eliminatingtheneedforhumanannotations.Thismethodleveragessynthetictrainingdata,starting
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
INPUTS Agent
Graph
Self-reflection LM
Locate
Search LLM-as-a-Judge Experience
Evaluator
Planning Memory
Retrieve
Read Trajectory Actor LM
Ask
Environment
OUTPUTS
Fig.7. LLM-as-a-Judgeappearsintwocommonformsintheagent.TheleftdiagramisAgent-as-a-Juge,
designingacompleteagenttoserveasanevaluator.TherightdiagramshowsusingLLM-as-a-Judgeinthe
processofanAgent.
withunlabeledinstructionsandgeneratingcontrastingoutputsfrommodels.Theseoutputsare
then used to train an LLM-as-a-Judge to produce reasoning traces and final judgments. With
eachiteration,theevaluatorimprovesbylearningfromitsrefinedpredictions,creatingacycleof
continuousself-enhancement.Thisiterativeapproachnotonlykeepsannotationsrelevantbutalso
ensuresthatevaluatorsevolvealongsideadvancingmodels.
Recentresearchonevaluatingmultimodaldatafocusesonaddressingvision-languagemisalign-
mentsinMultimodalLargeLanguageModels(MLLMs),whichoftencausehallucinations—outputs
inconsistentwithvisualorcontextualevidence[24,82,154].TechniqueslikeRLHFandFactually
AugmentedRLHFhavebeenemployedtoimprovemodelalignmentbyincorporatingstructured
ground-truthdataandimagecaptions,enhancinghallucinationdetection[136].Benchmarkssuch
asMLLM-as-a-Judge[17]assessthesemodelsusingtaskslikescoring,paircomparison,andbatch
ranking,revealinglimitationsinalignmentwithhumanpreferences.Persistentissuesincludebiases
(e.g.,position,verbosity)andhallucinations,withevenadvancedmodelslikeGPT-4Vdisplaying
challenges.Whilepaircomparisontasksalignbetterwithhumanjudgment,scoringandbatch
rankingrequiresignificantimprovementsforreliabledeployment.Thesefindingsemphasizethe
needforinnovativeframeworksanddatasetstorefineMLLMevaluationandalignment.
2.4.3 LLM-as-a-JudgeforAgents. TherearetwowaystoapplyLLM-as-a-Judgeforanagent.
Oneistoevaluatetheentireprocessoftheintelligentagent[226],andtheotheristoevaluateitat
aspecificstageintheagentframeworkprocess[43,128].Bothapproachesarebrieflyillustratedin
Figure7.UsingLLMasthebrainofagent,anagenticsystem[226]couldevaluatelikeahuman,it
wouldreducetheneedforhumaninvolvementandeliminatethetrade-offbetweenthoroughness
andeffort.Inaddition,theagent[128]caninteractwiththeenvironmentthroughlanguageand
receivefeedbackonactionsthroughLLMtomakedecisionsforthenextaction.
2.4.4 LLM-as-a-JudgeforReasoning/Thinking. Reasoning[50],definedasthecognitivepro-
cessofapplyinglogic,arguments,andevidencetodrawconclusions,iscentraltointellectualtasks
such as decision-making, problem-solving, and critical analysis. While reasoning is inherently
moredemandingandmultifacetedthanjudging,itoftendependsonjudgmentstoensurelogical
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
coherence,refineintermediatesteps,andachieveclarityinitsoutcomes.LLM-as-a-Judge,inthis
sense,becomesanintegraltoolforenhancingthereasoningcapabilityofLLM.
The role of LLM-as-a-Judge in enhancing reasoning or thinking can be understood through
twoframeworks:scalingtrainingtime[37,150]andscalingtesttime[129].Inthetrainingphase,
LLM-as-a-Judgefrequentlyoperateswithinreinforcementlearningparadigms,whereitfunctions
asarewardmodelorevaluatorfordataorprocesses.Thisenablesthecreationofhigh-quality
reasoningdatasetsthroughmechanismssuchasstep-by-stepverification[84],DirectPreference
Optimization(DPO)[115],andself-refinement[192].Recently,severalLLMstrainedwithreinforce-
mentlearningtoexhibitadvancedreasoningandthinkingabilitieshavegainedattention,suchas
o11,DeepSeek-R12,gemini-thinking3,andQVQ4.Inthetest-timeframework,LLM-as-a-Judgeis
crucialforevaluatingandselectingthebestreasoningpaths.Forexample,in"Best-of-N"gener-
ationscenarios,wheremultiplereasoningoutputsareproduced,thejudgedeterminesthemost
accurateandcoherentresponse.Thisdualroleinbothtrainingandtestphasesdemonstratesthe
indispensablenatureofLLM-as-a-Judgeinenhancingreasoningsystems.
ReliabilityConcernsofEvaluationPipeline
Withinthebroaderevaluationpipeline,severalfactorscancompromisetheintegrityof
LLM-basedassessments.Whenevaluatingmodels,inherentbiasessuchaspositionbiasand
self-enhancementcansignificantlyimpactfairness,requiringcarefulmitigationstrategies.
Indataevaluationcontexts,theextensiveuseofLLM-as-a-Judgeforpseudo-labelingrisks
amplifyingexistingmodelbiases,potentiallyleadingtothegenerationofunverifiedand
flawedtrainingdata.Foragenticframeworks,thesequentialapplicationofLLM-as-a-Judge
can lead to the accumulation of errors, where early misjudgments cascade into signifi-
cantinaccuraciesinfinaldecisions.Moreover,evaluatingcomplexreasoningtasksposesa
particularrisk;withoutrobustverificationoflogicalconsistency,LLMsmayproduceseem-
inglyconfidentbutfundamentallyflawedevaluations,underminingtrustinsophisticated
analyticalprocesses.
2.5 QuickPractice
ToeffectivelyapplyLLM-as-a-Judgedesign,itisrecommendedtofindmoreeffectiveconfigurations
inthetestingcycleforvariousscenarios.Crucially,reliabletestingshouldformthebedrockofthis
quickpractice,necessitatingiterativerefinement,continuousfeedbackloops,andtheestablishment
ofclearreliabilitymetrics.Theoverarchingaimistocontinuouslyoptimizeevaluationstability
andconsistencythroughdedicated,reliability-focusedtestingcycles.ThesuccessofusingLLM-
as-a-Judgealsoheavilydependsontheimplementationdetails,includingthetaskcomplexity,the
promptdesign,themodelselected,andthepost-processingmethod.
As shownin Figure8, Theprocess ofquickpractice forLLM-as-a-Judge involvesfour main
stages.Firstisthethinkingphase,inwhichusersdefinetheevaluationobjectivesbydetermining
whatneedstobeevaluated,understandingtypicalhumanevaluationapproaches,andidentifying
somereliableevaluationexamples.Thisinitialconceptualizationisvitalforpreemptingpotential
ambiguities and biases that could compromise the fairness and accuracy of subsequent LLM
judgments.
1https://openai.com/index/learning-to-reason-with-llms/
2https://api-docs.deepseek.com/news/news1120
3https://ai.google.dev/gemini-api/docs/thinking-mode
4https://huggingface.co/Qwen/QVQ-72B-Preview
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
Retest
Thinking PromptDesign ModelSelection Specification
What to evaluated ? Scoring Dimension Large Scale Model \boxed{XX}
How do humans Relative Strong Reasoning
evaluate ? comparisonbetter Ability The score is: XX
Any re e li x a a b m le p e le v s a l ? uation Example Strong Instruction- Yes or No
followingability
Test with cases
Fig.8. FlowchartofQuickPractice
Nextispromptdesign,detailedinSection2.1,wherebothwordingandformatsmatter.Themost
efficientandgenerallyeffectiveapproachinvolvesspecifyingscoringdimensions,emphasizing
relativecomparisonsforimprovedassessments,andcreatingeffectiveexamplestoguidetheLLM.
Carefulpromptengineeringisessentialtomitigateissueslikeoutputvariabilityandinter-rater
reliability,ensuringtheLLMconsistentlyinterpretsandrespondstoevaluationcriteriaasintended.
The third stage, model selection (Section 2.2), focuses on choosing a large-scale model with
strongreasoningandinstruction-followingabilitiestoensurereliableevaluations.Theinherent
biasesandgeneralizationlimitationsofdifferentmodels,aswellastheirblack-boxnature,under-
scoretheimportanceofselectingarobustandwell-understoodbackbonetominimizeevaluation
inconsistenciesandunverifiedjudgments.
Finally,standardizingtheevaluationprocessensuresthattheoutputsarestructured(Section2.3).
Thiscanbeachievedbyusingspecificformatslike\boxed{XX},numericalscores,orbinaryresponses
(e.g.,"Yes"or"No").Suchstandardizationiscrucialtocounteractthefragilityoftokenextraction
methodsandthepotentialforstylisticbiasestopropagate,therebyenhancingtheinterpretability
andvalidityofthefinalevaluationresults.Theentireprocessincludesiterativetestingwithcases
andrefinementthroughretesting,therebyenhancingreliability.Duringdevelopment,itisessential
tocomparemodelsorpromptsandverifyongoingimprovements.
3 IMPROVEMENTSTRATEGY
WhendirectlyutilizingLLMstoconductevaluationtasks—suchasscoring,selection,pairwisecom-
parison,orranking—theirinherentbiasesofLLMslikelengthbias,positionbias,andconcreteness
bias[110]willundermineevaluationoutcomes.Mitigatingtheseinherentbiasesandimproving
theoverallevaluationperformanceofLLMsremainsacriticalchallengeforapplyingLLMsas
evaluators. In this section, we introduce three improvement strategies to boost the evaluation
performanceofLLM-as-a-judge:designstrategyofevaluationprompts(in-contextlearningbased),
improvementstrategyofLLMs’evaluationcapabilities(model-based),andoptimizationstrategyof
finalevaluationresults(post-processingbased).AsshowninFigure9,ourcategorizationisbased
ontheformaldefinitionofLLM-as-a-judgeinSection2,focusingonenhancingtheevaluation
effectivenessbytargetingthreekeyphasesoftheprocess:thecontext C,theabilitiesofLLMs
themselves P LLM andthepost-processing←toobtainthefinalresults E
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
Few-shotprompting:FActScore[104]/
SALAD-Bench[80]/GPTScore[33]
Evaluationstepsdecomposition:G-Eval[93]/
DHP[163]/SocREval[44]/BSM[120]
ImprovingLLMs’Task Evaluationcriteriadecomposition:
Understanding HD-Eval[94]/HuandGaoetal.[47]
Shufflingcontents:Wangetal.[155]/
Auto-J[79]/JudgeLM[222]/PandaLM[162]
PromptDesignStrategy
(Sec.3.1) Conversionofevaluationtasks:Liuetal.[95]
Constrainingoutputsinstructuredformats:
StandardizingLLMs’ G-Eval[93]/DHP[163]/LLM-EVAL[86]
OutputFormat Providingevaluationswithexplanations:
CLAIR[16]/FLEUR[74]
Evaluationtemplate:PandaLM[162]/SALAD-Bench[80]
Improvement SpecializedFine-tuning
(Sec.3) CapabilityEnhancement Deeptransformation:OffsetBias[110]/JudgeLM[222]/
Strategy CritiqueLLM[61]/Yuetal.[188]
(Sec.3.2) Feedback-DrivenIterative
INSTRUCTSCORE[176]/JADE[202]/Think-J[48]
Refinement
Summarizebymultiplerounds:Sottanaetal.[133]/
PsychoBench[51]/Auto-J[79]
IntegratingMulti-Source
EvaluationResults VotebymultipleLLMs:CPAD[89]/Baietal.[8]/EvalMORAAL[105]
FinalOutput
OptimizationStrategy Hierarchicalevaluationframework:Jungetal.[57]/Zhangetal.[203]
R LL el M ia - b a l s e -a-Judge (Sec.3.3) Scoresmoothing:FLEUR[74]/G-Eval[93]/DHP[163]/TrustJudge[161]
DirectOutputOptimization
Selfvalidation:TrueTeacher[39]
EvaluationofAgreement
Agreement[144]Cohen’sKappa[144]
withHumanJudgments
Spearman’scorrelation[8,95]
(Sec.4.1)
Task-AgnosticBiases DiversityBias[185]CulturalBias
(Sec.4.2.1) Self-EnhancementBias[185,213]
EvaluationofBias
(Sec.4.2) PositionBias[126,144,155,185]
Evaluation Judgment-SpecificBiases Compassion-fadebias[66,185]
(Sec.4) (Sec.4.2.2) StyleBias[19,75,185]
LengthBias[49,110,185,213]
ConcretenessBias[19,110,185]
AdversarialPhrasesAttack[116]
EvaluationofAdversarial NullModelAttack[216]
Robustness(Sec.4.3) MajorityOpinionsAttack[66,185]
MeaninglessStatementRobustness[66,185]
Fig.9. StructureofhowtoimproveandevaluateLLM-as-a-Judge.
3.1 PromptDesignStrategy
AnevaluationpromptisaninputtoLLMevaluators,whichisusedtoguidetheLLMstocomplete
therequiredevaluationtasks.LLMspossessin-contextlearningability,enablingthemtolearnhow
toperformspecifiedtasksfromrelevantexamplesorinstructionsinprompts,withoutrequiring
weightupdatesorretraining[14].Thissuggeststhatthedesignstrategyofevaluationpromptswill
significantlyimpacttheeffectivenessofLLM-as-a-judge.Therefore,toachievereliableevaluations,
researchershaveexperimentedwithdiversepromptdesignstrategies,includingimprovingLLMs’
taskunderstandingandstandardizingLLMs’outputformatintheprompt.Thisapproachmitigates
reliability concerns of In-context learning mentioned in Section 2.1, such as unstable results,
inter-raterinconsistency,ambiguityinresponse,andpositionalorlengthbiases.
3.1.1 ImprovingLLMs’TaskUnderstanding. InoptimizationmethodsofpromptingLLMs
tobetterunderstandevaluationtasks,oneofthemostcommonlyusedandeffectiveapproaches
isfew-shotprompting[14].Byincorporatingseveralhigh-qualityevaluationexamplesintothe
evaluationprompts,LLMevaluatorscaneffectivelygrasptheobjectives,generalprocesses,and
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
roughevaluationcriteriaofevaluationtasks.Manyresearchworksemploythispromptparadigm
forevaluation,suchasFActScore[104],SALAD-Bench[80],andGPTScore[33].
Inadditiontoprovidinghigh-qualityexamples,refiningtheevaluationtaskinstructionsisalso
aneffectiveapproachtooptimizingLLMs’understandingofevaluationtasks.Currentmethodsfor
refiningevaluationtasksmainlyincludethedecompositionofevaluationstepsandcriteria:
• (a)DecompositionofEvaluationStepsentailsbreakingdowntheentireevaluationtasks
into smaller steps, providing detailed definitions and constraints for each small step in
prompts,therebyguidingLLMscomprehensivelythroughthewholeevaluationpipeline.
For instance, G-Eval[93] and DHP[163] use Chain-of-Thought(CoT)[167] to guide LLMs.
SocREval[44] employs the Socratic method to meticulously design each step to enhance
evaluationperformance.Inexistingresearch,thisparadigmresemblesprovidingdetailedand
sequentialexecutionstepswithinasinglepromptforaone-timeevaluation,whichguides
theLLM-as-a-judgetocompleteevaluationtasksalignedwithrequirements,asillustratedin
Fig10(a).Tobetterunderstandthisparadigm,wepresentademonstrativeexampleprompt
forevaluatingsummaryquality:"Youwillbegivenasummarywrittenforanarticle.......
EvaluationSteps:1.ReadtheSummaryThoroughly:Beforedivingintotheevaluation,ensurethat
you...;2.IdentifytheCentralTopic:Acoherentsummarywillhaveaclearcentraltopicortheme
...;3.LookforTransitionalElements:Coherentsummariesoftenhavecleartransitionsbetween
sentencesorideas...;4.CheckforLogicalFlow:Reviewthesummaryforlogicalsequencing...
X.GiveaScore:...SourceArticle:{{Article}}Summary:{{Summary}}".Inthisexample,the
evaluationtaskforsummaryqualityisdecomposedintomanysmallstepstoguidetheLLM
throughtheentireassessmentprocess—fromreadingandanalyzingtoscoring—enabling
methodicalevaluationofasummary.
• (b)DecompositionofEvaluationCriteriainvolvesbreakingdowncoarseevaluationcrite-
rialikeFluencyintofiner-grainedsub-criterialikeGrammar,Engagingness,andReadability,
andthengeneratingoverallscoresbasedonthesedifferentdimensions.Sahaetal.propose
Branch-Solve-Merge(BSM)[120],whichdividesevaluationtasksintomultipleparallelsub-
tasksbasedondifferentsub-criteriaforseparateevaluationandfinalmerge.HD-Eval[94]
proposesahierarchicalcriteriadecompositionmethodtoiterativelyalignLLMevaluators
withhumanpreference,therebyaddressingthepotentialbiasinLLMs.HuandGaoetal.[47]
summarizeandclearlydefineanexplicithierarchicalclassificationsystemencompassing11
criteria,addressingtheissueofLLMspotentiallyconfusingdifferentevaluationstandards.
Differentfromthedecompositionofsteps,thisparadigmpresentsgreatercomplexitydue
tosignificantvariationsinevaluationrequirementsandproceduresacrossdifferentcriteria
dimensions.Currentmethodologiestendtodecomposetheoriginalevaluationtaskintomul-
tiplesub-tasksbasedondistinctcriteria.Eachsub-taskisassessedviaadistinctprompt,with
resultssubsequentlymergedorsimplylistedinascoretable,asdemonstratedinFig10(b).
Inconclusion,thesedecompositionsarespecifictoenableLLMstounderstandthedetailsof
evaluationtasksmoredeeply,therebyaligningevaluationresultsmorecloselywithhumanevalua-
tionrequirementsandpreferences.Providingdetailedevaluationspecificationsandenhancingtask
comprehensioncanmitigateinter-raterinconsistencytosomeextent,whilealsoreducingpotential
ambiguity.
Furthermore,theevaluationcapabilitiescanbeoptimizedbasedonspecificshortcomingsof
LLMsinprompts.Forinstance,toaddressspecificbiaseslikepositionbias,whichiscommonin
pairwiseevaluations,severalresearcheffortshaveoptimizedpromptdesignbyrandomlyswapping
contents to be evaluated. Wang et al.[155] analyzed and validated the impact of position bias
onLLM-as-a-judgeandproposedacalibrationframeworktomitigatethisbiasbyswappingthe
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
Fig.10. SimplifiedEvaluationPipelineofTwoDecompositionParadigms.
contents and averaging the scores. Auto-J[79] and JudgeLM[222] also enhance the evaluation
consistencybyshufflingthetextstobeevaluated.Incontrasttoaveragingscores,PandaLM[162]
annotatestheconflictingevaluationresultsafterswappingas"Tie"toaddressthepositionbias.
Sincethecontenttobeevaluatedineachpositionalarrangementistakenintoaccountduring
evaluation,thefinalevaluationresultsarethusreliableandfreefrompositionalbias.
ToaddressthechallengeofLLMs’absolutescoringbeinglessrobustthanrelativecomparing[116],
some research works convert scoring tasks into pairwise comparison, thereby enhancing the
reliabilityofevaluationresults.Liuetal.[95]transformthescoringevaluationtorankingevaluation
and introduce Pairwise-Preference Search (PARIS), which employs LLMs to conduct pairwise
comparisonslocallyandefficientlyrankscandidatetextsglobally,makingevaluationresultsmore
alignedwithhumanpreferences.Unlikesinglenumericalscores,whicharemoresusceptibleto
promptvariationsandinherentrandomness,pairwisecomparisonsgeneraterelativeassessments.
ThisapproachonlyrequiresLLMstoevaluatetherelativemeritsbetweencandidates,consequently
yieldingmorestableandreliableresults.
Insummary,thedesignofpromptsforbetterunderstandingevaluationtasksisacoremethod
foroptimizingLLMs’in-contextuallearningabilities.Byrefiningtaskinstructionsandcriteria
inpromptsorfew-shotpromptingwithhigh-qualityexamples,thedetailsofevaluationprompts
canbeenriched,andtheunderstandingofLLMsonevaluationtaskscanbedirectlyorindirectly
enhanced.Additionally,targetedadjustmentstopromptscanaddresspotentialbiasesofLLMs,
suchaspositionbias.Thus,byimprovingLLMs’taskunderstanding,theinconsistentinter-rater
reliability,theambiguityinresponse,andthebiasesmentionedinSection2.1canbesolved.
3.1.2 Standardizing LLMs’ Output Format. Directly requiring LLM evaluators to output
evaluationresultsposesrobustnessproblems.Theresponsemayunexpectedlyvaryduetothe
inherentgenerativerandomnessofLLMs,suchasoutputtingtextlike"lowrelevance"whileasked
to measure with discrete scores, which hinders the automated extraction of evaluation results
fromLLM’soutput.Aneffectivemethodtoenhancetherobustnessofoutputformsistoconstrain
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
theoutputinstructuredformatswithinprompts.G-Eval[93]andDHPframework[163]perform
evaluationtaskswithaform-fillingparadigm,constrainingoutputswithformatslike"X:Y",where
X representsthedimensionormetrictobeevaluatedandY denotesanidentifiableoutputform
likescoresorspecifictokens.LLM-EVAL[86]furthermodifiesthisform-fillingparadigm,efficiently
outputsevaluationresultsinJSONformat,andobtainsmultidimensionalscores,leveragingLLMs’
highunderstandingandgenerationcapabilitiesofcode-liketexturalformats.
Apartfromchallengesinrobustness,directlyoutputtingevaluationresultsbyLLMsalsosuffers
fromalackofinterpretability.ThemeaningofevaluationresultsfromLLMevaluatorsisdifficultto
alignconsistentlywiththeinstructionsandmetricsprovidedinprompts.Toaddressthechallenges,
CLAIR[16]requiresLLMstooutputevaluationscoresbetween0-100simultaneouslywithrelevant
reasonsasexplanationsinJSONformat,whichenhancestherationalityandinterpretabilityofthe
scores.FLEUR[74]utilizesLLaVAtofirstprovidequalityscoresforimagecaptionsandsubsequently
asks with "Why? Tell me the reason." for explanations with the images, captions, and scores as
inputs,offeringastepwiseapproachtoprovideinterpretablescores.
Ingeneral,byconstrainingorguidingtheoutputprocessandformatofLLMevaluatorswithin
prompts,therobustnessandrationalityofevaluationresultscanbeeffectivelyimprovedthrough
structured outputs. This also facilitates the automated post-processing of evaluation results in
subsequentsteps,therebyenhancingtheoverallstabilityoftheevaluationpipeline.
3.2 CapabilityEnhancementStrategy
The evaluation capabilities of LLMs are a reflection of their powerful general language under-
standingandgenerationabilitiestriggeredbyspecificprompts.Methodsforoptimizingevaluation
throughpromptdesign——focusedonLLMs’in-contextuallearningcapabilities——requireLLMs
to comprehend the meaning of prompts fully and consistently follow the relevant evaluation
instructions.However,evenstate-of-the-artLLMslikeGPT-4encounterproblemssuchasconcep-
tualconfusion[47],andsmalleropen-sourceLLMshaveevenmorelimitationsintheirevaluation
capabilities.Fine-tuningLLMsmaybeacommonapproach,butasmentionedattheendofSec-
tion2.2,fine-tunedLLMsmightexhibitlimitedgeneralizationcapabilitybeyondtheirtraining
datadistribution,andcouldalsoremainsusceptibletosubtlebiaseswithinthefine-tuningdata
thatcompromisefairness,leadingtoinconsistencieswithhumanjudgment.Therefore,researchers
proposetwosolutions:Ononehand,constructingfairertrainingdatasetstofine-tuneLLMsand
eliminatejudgmentbiases;ontheotherhand,implementingfeedback-driveniterativerefinement
methods,whichcontinuouslyupdateLLMsduringusagetoenhancetheirgeneralizationcapability,
ultimatelyachievingreliableevaluationmodels.
3.2.1 SpecializedFine-tuning. Astraightforwardapproachtoenhancingtheevaluationca-
pabilitiesofLLMsistofine-tunethemviameta-evaluationdatasetsspecificallyconstructedfor
evaluationtasks,whichhelpsimprovetheLLMs’understandingofspecificevaluationprompts,
booststheevaluationperformance,oraddressespotentialbiases.Themostcriticalstepinthis
optimizationstrategyisthecollectionandconstructionoftrainingdata,sinceLLMswilladhere
totheinstructionalformatsdefinedbythetrainingdataandinheritanypotentiallysubtlebiases,
ultimately affecting the evaluation performance. As shown in Fig 11, there are primarily two
approachestoconstructingmeta-evaluationdata:EvaluationTemplatesandDeepTransformation.
Theformertypicallypopulatessampledrawdataintopresettemplatestoformtrainingdata,while
the latter employs algorithms or models to transform raw data in terms of style, content, and
structure,therebyconstructingtrainingdatamoreflexibly.
Usingevaluationtemplatesisacommonmethod,whichinvolvessamplingevaluationquestions
frompubliclyavailabledatasets,modifyingthemwithcertaintemplates,andsupplementingthe
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
Fig.11. Twoparadigmsoftheconstructionprocessofmetaevaluationdatasetsfortraining.
datasetwithevaluationresponsesgeneratedeithermanuallyorbypowerfulLLMslikeGPT-4.
Forinstance,PandaLM[162]samplesinputsandinstructionsfromAlpaca52K[143]andgenerates
responsesusingGPT-3.5toconstructtrainingdata,whileSALAD-Bench[80]buildsitstraining
datafromasubsetofLMSYS-Chat[214]andToxicchat[87].
Tobetteralignwiththerequirementsofevaluationtasks,manyresearchworksfurthertransform
inputsandinstructionssampledfrompublicdatasetstoconstructmoretargetedtrainingdata.
OffsetBias[110]aimstoreducebiasesofLLMsbyusingGPT4togenerateoff-topicversionsofthe
originalinputsandthenhavingGPT-3.5respondtothenewinputstoproducebadresponses.By
pairinggoodandbadresponsesastrainingdatatofine-tunetheLLMsasevaluators,thebiasesin
LLMsaresignificantlyreduced,includinglengthbias,concretenessbias,knowledgebias,andso
on.JudgeLM[222]enhancesLLMs’evaluationcapabilitiesbycreatingdifferenttypesoftraining
datathroughparadigmslikereferencesupportandreferencedrop.CritiqueLLM[61]proposesa
multi-pathpromptingapproach,combiningpointwise-to-pairwiseandreferenced-to-reference-free
promptingstrategiestorestructurereferencedpointwisegradingdataintofourtypes,whichhelps
createEval-Instructtofine-tuneLLMs,addressingshortcomingsinpointwisegradingandpairwise
comparison.Yuetal.[188]sampledatafromthepreferencedatasetandrewritejudgetemplatesto
synthesizetrainingdata,anduseGPT-4otoanalyzeandjudgethepairsofanswersinthesynthetic
data. The correct judgments, along with the synthetic data and analysis, will be processed as
trainingdatafortheSFTphaseofjudgemodels.
Insummary,constructingmeta-evaluationtrainingdatatargetedatspecificevaluationtasksand
fine-tuningLLMscandirectlyadjustthemodel’sinternalparameterizedknowledgeandlanguage
abilities.ThisisthemoststraightforwardmethodtoimprovetheevaluationperformanceofLLM
evaluatorsandaddresspotentialbiases.
3.2.2 Feedback-DrivenIterativeRefinement. Fine-tuningLLMsonmeta-evaluationdatasets
gives them the ability to produce evaluations that are more aligned with human preferences.
However,asdiscussedinSection2.2,LLMsexhibitversiondependency,andevenfine-tunedmodels
remainconstrainedbytheirtrainingdataandinherentlysufferfromout-of-distributionlimitations
tosomeextent.Consequently,LLM-as-a-Judgemaystillexhibitbiasesduringevaluationprocesses
in practice, ultimately compromising evaluation quality. A natural improvement strategy is to
iterativelyoptimizethemodelbasedonthefeedbackofevaluationresults,whichmainlycomes
fromstrongermodelsordirectlyfromhumanevaluators’correctionsoftheevaluationresults.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
AtypicalexampleisINSTRUCTSCORE[176].Toimprovemodelperformanceandfurtherbenefit
thefinalqualityscorecalculation,thisscoringframeworkcollectsfailuremodesofmetricoutputs,
queries GPT-4 on each failure mode to gather automatic feedback, and finally selects explana-
tions most aligned with human preferences to iteratively fine-tune the LLaMA model. Unlike
INSTRUCTSCORE,whichdirectlyoptimizesthemodel,theLLMevaluatorinJADE[202]relies
onhumanjudgestocorrectLLMs’evaluationresultsandupdatesthemostfrequentlycorrected
samplesintotheexamplesetsforfew-shotprompting.JADEutilizesthisrelativelylow-costmethod
toachieveiterativeupdatesoftheevaluationcapabilities.
Iterativeoptimizationmethodsarenotlimitedtoofflinetraining.ThesuccessofR1-stylemethods
showstheeffectivenessofonlinereinforcementlearning(RL)approaches.Thus,feedback-based
onlinelearningconstitutesanotherstrategicformofiterativeoptimization.Think-J[48]integrates
bothofflineandonlinelearningapproaches.Theofflineapproachtrainsacriticmodeltoevaluate
judgmentsfromthejudgemodel,therebyconstructingpositiveandnegativesamplesforSFTand
DPOoptimization.TheonlineapproachcontinuouslyoptimizesthejudgemodelusingtheGroup
RelativePolicyOptimization(GRPO)algorithmwithrule-basedrewardsasoptimizationfeedback.
Since the feedback is more closely aligned with human preferences, LLMs can dynamically
optimizetheirevaluationcapabilitiesbasedonthefeedback,leadingtobetterevaluationresults.
Thisfeedback-driveniterativerefinementstrategyaddressestheproblemofmodels’imperfect
generalizationandimprovestheevaluationcapabilitiesthroughdynamicupdates.
3.3 FinalOutputOptimizationStrategy
Throughoptimizationbasedonin-contextlearningandthemodel’sowncapabilities,LLMshave
becomefairlyreliableevaluatorsthatarecapableofunderstandingevaluationtaskrequirements
andprovidingrationalevaluationresults.However,theinherentgenerativerandomnessofLLM
blackboxes,thefragilityofoutputextractionmethods,andpotentialadversarialmanipulations,
asnotedattheendofSection2.3,maycollectivelycontributetounreliableandunfairevaluation
results. Therefore, it is necessary for LLM evaluators to design optimization strategies during
the post-processing stage from the outputs to the final evaluation results. Some strategies opt
todirectlymodifyoutputacquisitionmethodstoextractevaluationresultsmorerobustly,while
moremainstreamstrategiesfocusondesigningframeworksthatintegratemulti-sourceevaluation
results,whichmitigateadverseeffectscausedbyrandomnessandfragility,andenhanceresistance
toadversarialmanipulations.
3.3.1 IntegratingMulti-SourceEvaluationResults. Integratingmultipleevaluationresults
forthesamecontenttoobtainthefinalresultisacommonstrategyinvariousexperimentsand
engineeringpipelines,whichcanreducetheimpactsofaccidentalfactorsandrandomerrors.The
mostbasicoptimizationstrategyistoperformmultiplerunsofevaluationonthesamecontent
withdifferenthyper-parametersandsettings,andthensummarizetheseresults.Forexample,the
workofSottanaetal.[133]reducesrandomnessinevaluationsbyaveragingmultiplescoresof
the same sample. Similarly, PsychoBench[51] takes the mean and standard deviation from ten
independentruns.Auto-J[79]furtheramplifiesthedifferencesbetweenevaluationrounds,which
combinecritiqueswithandwithoutscenariocriteriatoobtainthefinalresults.
Inadditiontointegratingresultsfrommultipleroundsofevaluation,usingmultipleLLMevalua-
torstoassessthecontentssimultaneouslyandintegratingtheresultsisanothereffectivemethod,
whichcanreducebiasesintroducedbyLLMs.Forinstance,CPAD[89]utilizesChatGLM-6B[31],
Ziya-13B[200],andChatYuan-Large-v2[201]asevaluatorstoevaluatethecontentsandobtainthe
finalresultsbyvoting.Baietal.[8]proposeanovelevaluationmethodcalleddecentralizedpeer
reviewofLLMs,whichutilizesLLMsthatgeneratecontenttoevaluateeachother’sgenerated
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
contentandeventuallyintegratetheresults.EvalMORAAL[105]alsoemploysasimilarLLM-as-a-
judgepeerreviewmechanism,detectingconflictsinevaluationresultsbycheckingwhetherscore
differencesexceedapresetthreshold,andusesmajorityvotingtoresolveconflicts.
Theaforementionedmulti-roundormulti-modelapproachesrepresentatypeofpeer-parallel
evaluationstrategy,andtheirintegrationprocessisrelativelystraightforward.Researchershave
alsoproposedmanymorecomplexevaluationframeworksfeaturinggreaterinteractivitybetween
differentevaluations.Forexample,JaehunJungetal.proposedCascadedSelectiveEvaluation[57].
This framework transitions from weaker, smaller models to stronger, larger models based on
confidence,allowingthemajorityofevaluationstobehandledbysmallermodels,whichsignificantly
reducesthecostsofcomputingresourcesandimprovesefficiency.Recentwork[203],ontheother
hand, proposed Crowd-based Comparative Evaluation. This method utilizes multiple LLMs to
construct crowd responses based on candidate responses for comparison, thereby generating
multiplecrowdjudgmentsthatserveasreferencecontentforthefinalevaluation.Thisenables
LLM-as-a-Judgetocapturericherdetailsandenhanceevaluationreliability.
Insummary,formingthefinalevaluationresultsbycombiningmultipleroundsofevaluationsor
multipleLLMevaluatorscanreducetherandomeffectscausedbyaccidentalfactorsinasingle
roundandreducethepotentialbiasesofasingleLLMevaluator.Thisstrategysignificantlyenhances
thestabilityandreliabilityoftheevaluationresults.
3.3.2 DirectOutputOptimization. Differentfromobtainingevaluationresultsbasedonthe
outputs of multiple rounds or LLMs, directly optimizing the output of a single LLM evaluator
involvesfurtherprocessingtheevaluationoutputtomakeitmorereliable,especiallywhendealing
withscoringoutputsfromLLMevaluators.DuetotheinherentrandomnessinLLMs’generation,
the scores may not fully reflect the LLMs’ complete view of the evaluation criteria. Therefore,
to obtain more reliable evaluation results, it is necessary to optimize the LLM’s score outputs.
An effective optimization strategy is to combine the implicit logits, which capture the LLMs’
randomness,withtheexplicitoutputscores.Forexample,FLEUR[74]proposesascoresmoothing
strategy.ForscoresgeneratedbyLLaVA,theprobabilityofthetokencorrespondingtoeachdigit
𝑙 (0≤ 𝑙 ≤9) would be used as the weight to smooth the explicit scores and calculate the final
evaluationscores.TrustJudge[161]proposesadistribution-sensitivescoringmethodthatcomputes
continuousexpectationsfromdiscretescoringprobabilities,andalikelihood-awareaggregation
methodthatutilizesbidirectionalpreferenceprobabilities,toprocesstheevaluationresultsfrom
LLMs,addressingtheinconsistencyinLLM-as-a-Judge.
However,methodslikescoresmoothing,whichcombineimplicitlogitsandexplicitoutputs,
requiretheLLMstobeopen-sourceortoprovideinterfacesthatallowaccesstotokenprobabilities,
whichbringssomelimitations.InspiredbytheworkofWengetal.[168]andMadaanetal.[103],
self-verificationcanbeusedtofilterouttheevaluationresultswithoutsufficientrobustness.For
example,TrueTeacher[39]appliesself-verificationinitsevaluationofdistilleddatabyaskingthe
LLMevaluatorforitscertaintyabouttheevaluationresultsafterprovidingthemandretaining
onlythoseresultsthatpassself-verification.Self-verificationissuitableforallLLMsandrequires
nocomplexcomputingandprocessing.
Insummary,comparedtointegratingmultipleevaluationresults,directlyoptimizingtheLLMs’
outputstoobtainthefinalresultsisfasterandlower-cost,althoughtheeffectivenessstillneedsfur-
thervalidation.However,thesetwoapproachesarenotmutuallyexclusive.Performingintegration
afterdirectoptimizationofLLMs’outputmayleadtomorestableevaluationresults.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
Agreement with Human Bias
R1: 3.11 > 3.8
Dataset Position Bias R2: 3.8 > 3.11 R1 is better!
JudgeBench Length Bias
MTBench
Chatbot Concreteness Bias R R 2 1 : : 3 3 . . 8 1 1 > > 3 . 3 1 . 1 8 LLM R2 is better!
CALM
Arena Diversity Bias
LLM favor the first response.
FairEval KUDGE
Adversarial Robustness
Null Model Attack
Metric Spearman’s Question: Ali had $21.
Leila gave him half of her
correlation Majority Opinion Attack
Accuracy $100. How much does Ali
have now? Correct!
Percent Adversarial Phrases
F1-score Agreement Response: "Solution" LLM
System Prompt Attack
Fig.12. ThreeDimensionsofEvaluation.
4 EVALUATIONOFLLM-AS-A-JUDGE
FollowingthediscussionsontheapplicationandenhancementofLLM-as-a-Judge,wenowaddress
thecriticalquestionofitsevaluation.Whilethebasicevaluationpipelineprovidesaconceptual
foundation,itdoesnotinherentlyguaranteethereliabilityofthesystem.Toformallycapturethis
essentialproperty,werecalltheenhancedformaldefinitionofreliability:
R ← 𝑓 (P ,𝑥,C)
R LLM
ThisformulationhighlightsthatreliabilityR isafunctionofthreeindependentvariables:the
LLM’sprobabilityfunction(P ),theinputbeingevaluated(𝑥),andtheaccompanyingcontext
LLM
(C).AssessingLLM-as-a-Judge,therefore,requiresasystematicexaminationofhowthesethree
factorscollectivelyinfluenceitsperformance.
Reliability may degrade if the underlying model, defined by its probability function P ,
LLM
exhibitsinherentbiasesorinstability.Forinstance,alessrobustLLMmayproduceinconsistent
scores for identical prompts and inputs due to sampling variance or internal preference drift.
Similarly,thequalityofevaluationissusceptibletothenatureoftheinput𝑥.Noisyoradversarially
perturbedinputscancausetheLLMtomisjudgequality,thusdiminishingitsrobustness.Finally,
subtle changes in the prompt wording or the ordering of the context C can lead to different
judgmentsforthesameinput,aphenomenonthatunderminesreliability.
Therefore,acomprehensiveevaluationofLLM-as-a-Judgerequiresexaminingmultipleaspects.
We organize existing evaluation studies into three major dimensions: agreement with human
judgments(Section4.1),bias(Section4.2),andadversarialrobustness(Section4.3),asdepictedin
Figure12.
4.1 AgreementwithHumanJudgments
GiventhattheinitialmotivationofLLM-as-a-judgeliesinreplacinghumanannotation,theforemost
aspectofitsevaluationshouldnaturallybetheextenttowhichitalignswithhumanjudgments.
Numerous studies approach this by considering the LLM evaluator as a virtual annotator and
evaluatingtheextentofitsagreementwithhumanannotators.Thepercentageagreementmetric
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
representstheproportionofsamplesonwhichLLMandhumanannotatorsagree[144].
Agreement=
(cid:205)
𝑖∈D
I(S
llm
=S
human
)
∥D∥
whereD isthedataset,𝑆 and𝑆 aretheevaluationresultsoftheLLMevaluatorandhuman
llm human
judge, respectively, which can be in the form of both score or rank. Additionally, widely used
correlation metrics such as Cohen’s Kappa [144] and Spearman’s correlation [8, 95] are also
employed to assess agreement. Other works treat the LLM-as-a-judge task as a classification
problem,wherehumanannotationsserveasthelabels,andcomputeprecisionandrecalltoevaluate
theperformance[162,222].
EvaluationDimension
Benchmark ReleaseYear Size AnnotationFormat
Agreement PositionBias LengthBias BiasTypes
MTBench[213] 2023 80 Pairwise ✓ ✓ ✓ 3
ChatbotArena[213] 2023 30k Pairwise ✓ ✓ ✓ 3
FairEval[155] 2023 80 Pairwise ✓ ✓ ✗ 1
PandaLM[162] 2023 - Pairwise ✓ ✓ ✗ 0
LLMEval2[207] 2023 2553 Pairwise ✓ ✗ ✗ 0
Shepherd[159] 2023 1317 Score ✓ ✗ ✗ 0
EvalBiasBench[110] 2023 80 Pairwise ✓ ✓ ✓ 6
CALM[185] 2024 4356 Pairwise&Score ✗ ✓ ✓ 12
JudgeBench[139] 2024 - Pairwise ✓ ✗ ✗ 0
MLLM-as-a-Judge[17] 2024 30k Pairwise&Score ✓ ✗ ✗ 0
CodeJudge[212] 2024 1860 Score ✓ ✗ ✗ 0
KUDGE[130] 2024 3324 Pairwise&Score ✓ ✗ ✗ 0
Table1. Benchmarkformeta-evaluationofLLM-judge.
Datasets.BothoftheabovemetricsrelyonthedatasetswithLLM-generatedresponsesand
respondinghumanjudgments.Therefore,thereisalsoapracticalneedtoconstructacomprehensive
benchmarkforthemeta-evaluation.Table1showsexistingbanchmarks.MTBench[213]hasonly80
human-craftedquerieswiththeircorrespondinghumanannotationandLLMs’responses.FairEval
[155]isconstructedfromthe80queriesfromVicunaBench[148]withhuman-annotatedpreference
betweenChatGPTandVicunaresponses.ChatbotArenaConversations[213]isalargercollection
ofcrowdsourceddata(about30k)withhumanannotatedpreferences.Research[195]constructs
a benchmark to assess the capability of the LLM evaluator in evaluating whether a response
followstheinstruction.Thisdatasetcontainshuman-curated419pairsofoutputs,oneadheringto
instructionswhiletheotherdiverging,yetmaypossessdeceptivequalitiesthatmisleadanLLM
evaluator.Research[17]evaluatesthecapabilitiesofmulti-modalLLMsinassistingevaluation
tasksacrossvariousmodalitiesandintroducesMLLM-as-a-Judge,acomprehensivemulti-modal
benchmark.Recentadvancesalsoexpandthescopeofmeta-evaluationbenchmarkstospecialized
domains,includingcodeassessment[212]andnon-Englishlanguagetasks[130].Furthermore,
CALM [185] presents a systematic framework for bias quantification, featuring an automated
perturbation mechanism to generate meta-evaluation data for examining 12 distinct types of
potentialbiasesinLLMevaluators.
Currentmeta-evaluationprimarilyfocusesonLLM-as-a-judgeformodels,whilethereisalackof
sufficientmeta-evaluationwhentheseLLMevaluatorsareusedforautomaticallyannotatinglarge-
scaledatasets(Section2.4.2).Weadvocateformorerigorousassessmentofthealignmentbetween
LLM-as-a-judgeandhumanjudgmentwhentheyareemployedforlarge-scaledataannotation.
Additionally,itisalsocrucialtoassessthepotentialbiasandrobustness,whichwillbediscussedin
thefollowingsections.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
4.2 Bias
AsLLM-as-a-Judgebecomesmorewidelydeployed,ithasbeenobservedtomanifestarangeof
salientbiases,evenincaseswhereitsevaluationsalignwithhumanjudgments.Priorstudieshave
emphasizedthatlargelanguagemodelsinherentlyexhibitdiverseformsofbiasacrossdifferent
tasks[25,34,138].SuchinternalbiasesmaypropagateintotheLLM-as-a-Judgesetting,potentially
resultinginunfairevaluationoutcomesand,inturn,influencingthedevelopmentofdownstream
LLMs.Consequently,itisimperativetobothcharacterizethetypesofbiasesthatLLMevaluators
maycarryandtoestablishsystematicapproachesfortheirassessment.Inthissection,wereviewthe
majorcategoriesofbiasesinthecontextofLLM-as-a-Judge,outliningtheirdefinitions,associated
metrics,anddatasetscommonlyemployedforevaluation.
Themeta-evaluationofLLM-as-a-judgeintroducessystematicbiasesthatcanbebroadlycatego-
rizedintotwoclasses:task-agnosticbiasesinherenttoLLMsacrossgeneralapplications,and
judgment-specificbiasesuniquetoLLM-as-a-judgescenarios.Thistaxonomyaimstoclarify
theirdistinctcharacteristicsandimplications.Theformermaybepartiallyattributedtothecharac-
teristicsofthejudgmenttaskitself,suchasitsspecificinput-outputformat,whichcouldpotentially
bemitigatedthroughtask-specificdesign.Incontrast,task-agnosticbiasesaremorefundamental
issuesinherenttotheLLMsthemselvesandarethereforemoredifficulttoaddress.Mitigatingsuch
biaseslikelydependsonadvancementsinthefoundationmodels.
4.2.1 Task-AgnosticBiases. ThesebiasesmanifestacrossdiverseLLMapplications,including
open-domainQA,classification,andsummarization.However,whenarisingintheLLM-as-a-judge,
thebiasesareparticularlycriticalduetotheircascadingeffectsondownstreamtasks.WhenLLM-
generatedjudgmentsserveasfeedbackformodeltrainingordataannotation,thesebiasesrisk
beingamplifiedandpropagated.Wepresentafewtypicalexamplesandrecommendconsulting
comprehensivereviewsonlanguagemodelbias[35,42]foramorethoroughunderstanding.
DiversityBiasreferstobiasagainstcertaindemographicgroups[185],includingcertaingenders
[19],race,andsexualorientation[70].InthecontextofLLM-as-a-judgescenarios,thisbiasmay
appear when evaluators give higher scores to responses that align with stereotypes of certain
groups.
CulturalBias.Ingeneraldomains,culturalbiasreferstosituationswheremodelsmightmisin-
terpretexpressionsfromdifferentculturesorfailtorecognizeregionallanguagevariants[35].In
thecontextofLLM-as-a-judge,itindicatesthatevaluatorsmightscoreexpressionsfromunfamiliar
culturespoorly.
Self-EnhancementBiasdescribesthephenomenonthatLLMevaluatorsmaypreferresponses
generated by themselves [185, 213]. This bias has also been known as source bias in retrieval
task[26]andopen-domainquestionansweringsystems[138].Consideringthesignificantself-
enhancementbias,assuggestedin[185],weshouldavoidusingthesamemodelastheevaluator.
Thisisonlyastopgap,aswemaynotusetheoptimalevaluatorwhenevaluatingthemostadvanced
LLMs.
4.2.2 Judgment-SpecificBiases. Judgment-specificbiasesareeitheruniquetotheLLM-as-a-
judgesettingorhaveasignificantimpactonjudgmenttasks.Aclassicexampleisthe"position
bias",whichhasamorepronouncedeffectinthecontextofLLM-as-a-judge,wheretheevaluator
oftenneedstocomparepairwiseresponses.Differentfromtask-agnosticbiases,judgment-specific
biasesaremoredifficulttoresolvenaturallywiththedevelopmentoffoundationallargemodel
capabilitiesandrequiretargetedoptimizationforjudgmenttasks.
PositionBiasisthetendencyofLLMevaluatorstofavorresponsesincertainpositionswithin
the prompt [126, 144, 155, 185]. This bias may have detrimental effects, as Vicuna-13B could
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
outperformChatGPTwhenevaluatedbyChatGPT,simplybypositioningtheresponseofVicuna-
13B in the second place [155]. To measure this bias, recent work [126] proposed two metrics:
PositionConsistency,whichquantifieshowfrequentlyajudgemodelselectsthesameresponse
afterchangingtheirpositions,andPreferenceFairness,whichmeasurestheextenttowhichjudge
modelsfavoraresponseincertainpositions.Thestudy[155]alsointroducedametricConflict
Ratetomeasurethepercentofdisagreementafterchangingthepositionoftwocandidateresponses.
Theiranalyticalexperimentsrevealthatthedegreeofpositionalbiasfluctuatesdependingonthe
disparityinresponsequality,andthepreferredpositionvarieswithdifferentLLMs.Forinstance,
GPT-4tendstofavorthefirstposition,whileChatGPTshowsapreferenceforthesecondposition.
Compassion-fadebiasdescribestheeffectofthemodelnames[66,185].Thistendencyoc-
curswhenweexplicitlyprovidemodelnames.forinstance,evaluatorsmaybeinclinedtogive
higherscorestoresultslabeledas“gpt-4”.Thistendencyunderscoresthenecessityofanonymous
evaluation.
StyleBiasreferstothetendencytowardsacertaintextstyle.Asrevealedin[19],anevaluator
mayalsoprefervisuallyappealingcontent,regardlessofitsactualvalidity,suchasthetextwith
emojis.Furthermore,LLMevaluatorsmayfavorresponseswithcertainemotionaltones,suchas
cheerful,sad,angry,andfearful,whichisdefinedassentimentbias[75,185].
LengthBiasreferstothetendencytofavorresponsesofaparticularlength,suchasapreference
formoreverboseresponses,whichisalsoknownasverbositybias[49,110,185,213].Lengthbias
canberevealedbyrephrasingoneoftheoriginalresponsesintoamoreverboseone[185,213].Even
thoughtheseexpansionsdonotintroducenewinformation,thereisstillconcernregardingchanges
totheoriginalresponseintermsofperplexity,fluency,orstyle.Alternatively,apreviousstudy
[121]investigatedthisbiasbycomparingmultiplesampledresponsesandrevealedastatistical
tendencytowardslongeranswers.However,ensuringthecomparablequalityofmultiplesamples
remainsachallengingproblem.
ConcretenessBiasreflectsthatLLMevaluatorsfavorresponseswithspecificdetails,including
citationofauthoritativesources,numericalvalues,andcomplexterminologies,whichiscalled
authoritybias[110]orcitationbias[19,185].Thenegativeeffectsofconcretenessbiasarise
fromtheneglectofthefactualcorrectnessofthesedetails,therebyencouraginghallucination[1].
4.3 AdversarialRobustness
AsLLM-as-a-Judgebecomesfurtherintegratedintoevaluationpipelinesandincreasinglyserves
asthestandardprotocol,avarietyofadversarialattackshaveemerged.Adversarialrobustness
referstotheabilityofamodeltowithstanddeliberateattemptstomanipulatethescoresthrough
carefullycraftedinputs.Unlikebiasevaluations(Section4.2),whichmainlyfocusonnaturally
occurringsamples,adversarialrobustnessinvolvessamplesintentionallycraftedtomanipulate
scoring,suchasinsertingphrasesthatartificiallyenhancescores.Robustnessiscrucialbecause
insufficientrobustnessallowstrivialmanipulationstodeceivetheevaluatorsandtoundermine
theevaluationoftextquality.Ensuringrobustevaluatorsisessentialformaintainingaccurateand
reliableassessments,particularlyinhigh-stakesapplications.
Research[116]constructedasurrogatemodelfromtheblack-boxLLM-evaluatorandthenlearn
a adversarial attack phrases based on it. The evaluation score can be drastically inflated by
universallyinsertingthelearnedattackphraseswithoutimprovingthetextquality.Similarly,work
byLeeetal.[73]introducedEMBER,abenchmarkthatrevealedbiasesinwhenassessingoutputs
withepistemicmarkers,suchasexpressionsofcertaintyoruncertainty.Furthermore,otherwork
[216]demonstratedthatevena"nullmodel"thatoutputsaconstantresponseirrelevanttoinput
instructionscanachievehighwinratesforvariousLLM-as-a-judgemethods.Similarly,recentwork
[211]alsorevealedthaton-wordsymbols(e.g.,“:”)orreasoningopenerslike“Thoughtprocess:”can
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
oftenfoolLLMevaluatorstoproducepositiveevaluations.Severalrecentworks[66,185]proposed
toincreasetheevaluationscorebyaddingthemajorityopinions,suchas“90%believethisis
better”. Other research [66, 185] evaluated robustness against meaningless statement in the
SystemPrompt,e.g.,”AssistantAloveseatingpasta”.TheseworksrevealedthatLLM-as-a-judge
arestillinsufficientlyrobustagainstinterferenceirrelevanttotextquality.Defensivemeasures
liketheperplexityscore[52,116]canonlydetectlimitedtypesofadversarialexamples.Therefore,
constructingmorerobustLLM-as-a-judgeisacrucialresearchdirectionforthefuture.
4.4 EmpiricalExperiment
LLM-as-a-judge
Post-process
LLM-Evaluator
Prompt-Design
Iterative Multi-Turns
Loading of LLMs
Optimization Structured Shuffling
for Evaluator Multi-LLMs Query LLMs Output Contents
Extraction of
Few-shot
Score Smooth Results Task/Criteria
Scheduling of Explanation Decomposition
Self-Validation Decomposed Tasks
Fig.13. LLM-as-a-JudgeMeta-evaluationPipelineandTools
InSection3,wehaveintroducedtheimprovementstrategiesinexistingLLM-as-a-judgeworks
toimprovetheevaluationcapabilitiesofLLMs.Althoughnumerousworkshaveproposedmeta-
evaluation benchmarks to assess the performance of LLMs in evaluation tasks, there is a lack
ofmeta-evaluationonwhethertheseimprovementstrategieseffectivelymakeLLM-as-a-Judge
morereliable.SointheprecedingsubsectionofthisSection4,wesystematicallyintroducedthe
dimensionsandcriteriaforevaluatingtheevaluationperformanceandreliabilityofLLM-as-a-Judge,
therebyprovidingquantifiablemetricsthatinformtheevaluationoftheaforementionedstrategies.
Basedonpartialdimensionsmentionedinsec4.1andsec4.2,wedesignedarobustandscalable
meta-evaluationtoolasshowninFigure13andconductedasimplemeta-evaluationexperiment
ontheimprovementstrategiessummarizedinSection3,examiningtheireffectivenessfromthe
perspectivesofbiasesandagreementwithhumanevaluation.
4.4.1 ExperimentSettings.
EvaluationDimensionsandBenchmarks. Themostdirectmetrictoreflectthequalityof
automaticevaluationisthealignmentwithhumanevaluation.WeuseLLMEval2[207]toassessthe
alignmentofLLM-as-a-judgewithhumanevaluations.LLMEval2isthelargestandmostdiverse
evaluationbenchmarkforLLM-as-a-judgetodate,with2,553samplescompiledfrommultipledata
sourceswithhuman-annotatedpreferences.Eachsampleconsistsofaquestion,apairofcandidate
responses,andahumanlabelindicatingthepreferredresponse.
BiasisalsoacrucialdimensionforassessingthequalityofLLM-as-a-judgeevaluationresults.
WeuseEVALBIASBENCH[110]tomeasuresixtypesofbiasesinLLM-as-a-judge,includinglength
bias,concretenessbias,emptyreferencebias,contentcontinuationbias,nestedinstructionbias,
andfamiliarknowledgebias.EVALBIASBENCH consistsof80samples,eachcontainingaquestion,
apairofcandidateresponses,andalabelindicatingthecorrectresponsewithoutbiasinfluence.In
additiontothesixtypesofbiases,wealsoevaluatedpositionbias.Themeta-evaluationsamplesfor
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
positionbiasarethepairedsamplesconstructedbyswappingthepositionofcandidateresponses
withinpromptsinsamplesofLLMEval2andEVALBIASBENCH.
EvaluationMetrics. Forthealignmentwithhumanevaluation,weusePercentageAgreement
Metric[144]forevaluation,asshowninSection4.1.Forbiasesexceptforpositionbias,weuse
Accuracyforevaluation,whichrepresentstheproportionofsampleswhereLLM-as-a-judgeselects
thecorrectcandidateresponseannotatedinEVALBIASBENCH.
Forpositionbias,weusePositionConsistencyasthemetric,whichquantifieshowfrequently
theLLM-as-a-judgeselectsthesameresponseafterswappingthepositionofcandidateresponses.
Formally,given𝑁 samples{(𝑞
𝑖
,𝑟1𝑖 ,𝑟2𝑖)}
𝑖
𝑁
=1
,foreachsample(𝑞
𝑖
,𝑟1𝑖 ,𝑟2𝑖),wequeriedtheLLM-as-
a-judgewithtwoprompts𝑃(𝑞
𝑖
,𝑟1𝑖 ,𝑟2𝑖)and𝑃(𝑞
𝑖
,𝑟2𝑖 ,𝑟1𝑖),andobtainedtwoevaluationresults𝑆
𝑖
𝑟12
and𝑆 𝑖 𝑟21.Each𝑆 𝑖 is𝑟1𝑖,𝑟2𝑖 or"TIE".ThenwecalculatethePositionConsistencyasfollows:
(cid:205)𝑁 I(𝑆𝑟12 =𝑆𝑟21)
PositionConsistency=
𝑖=1 𝑖 𝑖
𝑁
whereI(·)istheindicatorfunction.
TargetLLMsandStrategies. ForLLMs,weselectedsixLLMscommonlyusedintheautomatic
evaluation,includingclosed-sourceLLMsGPT-4,GPT-3.5,andopen-sourceLLMsQwen2.5-7B,
LLaMA3-8B,Mistral-7B,andMixtral-8×7B.
Forimprovementstrategies,weselectedProvidingEvaluationswithExplanations,SelfValidation,
SummarizebyMultipleRounds,andVotebyMultipleLLMs,sincethesestrategiesareallstraight-
forwardandrelativelycommoninmanyworks.WeadoptGPT-3.5asthebaseevaluatorforthe
meta-evaluationoftheseimprovementstrategies.
ModelConfiguration. Forclosed-sourceLLMs,weinteractusingOpenAI’sofficialAPIs.The
model versions we selected are GPT-4-turbo and GPT-3.5-turbo, specifically referencing gpt-4-
turbo-2024-04-09andgpt-3.5-turbo-0125respectively1.
Foropen-sourceLLMs,weadoptQwen2.5-7B-Instruct2,Meta-Llama-3-8B-Instruct3,Mistral-7B-
Instruct-v0.34,Mixtral-8×7B-Instruct-v0.15,deployedonanUbuntumachineequippedwitha40GB
NVIDIAA100GPU.
To stabilize the evaluation results of LLMs, we set the hyper-parameter temperature to 0 to
reducetheimpactofrandomnessinLLMs’output.ForSummarizebyMultipleRounds,weconduct
5roundsforeachsampleandverifytheeffectsofthreedifferentprocessingmethodsforresults
ofmultiplerounds:majorityvoting(-majority@5),takingthemeanscore(-mean@5),andtaking
thebestscore(-best@5).ForVotebyMultipleLLMs,weconductexperimentsontwosettings,each
involvingthreeLLMs.Setting1consistsofGPT-4-turbo,GPT-3.5-turbo,andLLaMA3-8B-Instruct,
whilesetting2consistsofGPT-4-turbo,GPT-3.5-turbo,andQwen2.5-7B-Instruct.
4.4.2 ResultsandAnalysis.
ComparisonwithDifferentLLMs. TheexperimentresultsondifferentLLMsareshownin
Table2.ComparingtheevaluationperformanceofdifferentLLMs,wefoundGPT-4outperformed
otherLLMswithalargemarginacrossallmeta-evaluationdimensionsandshowedfewerbiases.
Therefore, when conditions allow, using GPT-4 as an evaluator may obtain more objective
andlessbiasedevaluations.Foropen-sourceLLMs,wefoundthatQwen2.5-7B-Instructshowed
1https://platform.openai.com/docs/models
2https://huggingface.co/Qwen/Qwen2.5-7B-Instruct
3https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
4https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3
5https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
Alignment Biases
with Concre- Empty Content Nested Familiar
LLMs Position Length
Human teness Reference Continuation Instruction Knowledge
(n=5106) (n=2633) (n=34) (n=28) (n=26) (n=24) (n=24) (n=24)
GPT-4-turbo 61.54 80.31 91.18 89.29 65.38 95.83 70.83 100.0
GPT-3.5-turbo 54.72 68.78 20.59 64.29 23.08 91.67 58.33 54.17
Qwen2.5-7B-Instruct 56.54 63.50 64.71 71.43 69.23 91.67 45.83 83.33
LLaMA3-8B-Instruct 50.72 38.85 20.59 57.14 65.38 75.00 45.83 54.17
Mistral-7B-Instruct-v0.3 55.42 59.78 26.47 67.86 53.85 66.67 37.50 41.67
Mixtral-8×7B-Instruct-v0.1 56.29 59.06 50.00 78.57 42.31 83.33 29.17 83.33
gemini-2.0-thinking 60.75 76.84 94.12 89.29 50.00 100.00 83.33 100.00
o1-mini 60.16 76.73 91.18 89.29 53.85 95.83 75.00 95.83
o3-mini 61.66 74.63 82.35 92.86 73.08 95.83 87.50 91.67
deepseekr1 56.48 69.17 94.12 100.00 50.00 100.00 75.00 87.50
Table2. Themeta-evaluationresultsfordifferentLLMs.Allthevaluesarepercentages.
human=model1 human=model2 human=TIE
LLMs
aligned/total accuracy(%) aligned/total accuracy(%) aligned/total accuracy(%)
GPT-4-turbo 1418/2071 68.47 1438/2070 69.47 286/962 29.73
gemini-2.0-thinking 1354/2070 65.41 1621/2070 78.31 127/962 13.20
o1-mini 1444/2070 69.76 1401/2071 67.65 227/963 23.57
o3-mini 1448/2004 72.26 1206/2004 60.18 399/943 42.31
deepseekr1 1369/2071 66.10 1342/2071 64.80 173/964 17.95
Table3. TheresultsofeachhumanlabelinLLMEval2.Onlyvalidresponsesarecountedwhencalculatingthe
accuracy,whilesamplesthatcouldn’treceiveresponsesduetotriggeringAzureOpenAI’scontentmanagement
policyareexcluded.Sotherearesomedifferencesinthetotalvaluesofdifferentmodels.
Alignment Biases
with Concre- Empty Content Nested Familiar
ImprovementStrategies Position Length
Human teness Reference Continuation Instruction Knowledge
(n=5106) (n=2633) (n=34) (n=28) (n=26) (n=24) (n=24) (n=24)
GPT-3.5-turbo
-base 54.72 68.78 20.59 64.29 23.08 91.67 58.33 54.17
-w/explanation 52.47 48.97 35.29 60.71 38.46 91.67 41.67 50.00
-w/self-validation 54.86 69.31 23.53 60.71 23.08 91.67 41.67 50.00
-w/multirounds
-majority@5 54.68 7011 26.47 67.86 23.08 95.83 54.17 50.00
-mean@5 54.72 69.58 11.76 57.14 26.92 87.50 50.00 50.00
-best-of-5 51.95 58.72 5.88 42.86 19.23 87.50 37.50 45.83
multiLLMs(set1) 57.66 32.28 26.47 64.28 46.15 87.50 66.67 62.50
multiLLMs(set2) 58.19 70.98 64.71 71.43 69.23 91.67 45.83 83.33
Table4. TheresultsfordifferentstrategiesbasedonGPT-3.5-turbo.Allthevaluesarepercentages.
exceptionalevaluationcapabilities,outperformingotheropen-sourceLLMsintheexperiments.
Moreover, it surpassed GPT-3.5-turbo in most dimensions except for Position Bias and Nested
InstructionBias,indicatingthatitcanbeapromisingchoiceasanopen-sourceLLM-as-a-Judge,
withthepotentialtoserveasarobustbasemodelforspecializedevaluatorsinspecificscenarios.
Additionally,weobservedthat,apartfromConcretenessBiasandContentContinuationBias,the
performanceofLLMs,exceptGPT-4-turbo,wasgenerallypoor,particularlyintheLengthBias.Even
GPT-4-turboexperiencedsubstantialdegradationinEmptyReferenceBiasandNestedInstruction
Bias.WhilePositionBiascanbemitigatedbyswappingthepositionsoftheinputs,addressing
otherbiasesmayrequireresearcherstoexploremoreeffectiveevaluationstrategies.Meanwhile,
wealsoobservedthatdifferentLLMsintheexperimentsshownosignificantdifferencesinthe
alignmentwithhumans,andthereisclearspaceforimprovement.
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
Therefore,toachievereliableevaluations,suggestionsformodelselectioninclude:First,prioritiz-
ingpowerfulorfine-tunedLLMsasfoundationalevaluators.Thisapproachincreasesthelikelihood
ofobtaininghuman-alignedjudgmentswhileleveragingstrongerinstruction-followingandcom-
prehensioncapabilitiestohandleevaluationpromptswithcomplexstrategies.Additionally,itis
advisabletoconductsmall-scalemeta-evaluationsbeforemodelselectiontodetectpotentialbiases.
Asexperimentalresultsdemonstrate,differentmodelsexhibitvaryingsusceptibilitytodistinct
biases—evenpowerfulLLMslikeGPT-4-Turbocanbeseverelyimpactedbyspecificbiasessuchas
EmptyReference.Thus,understandingamodel’sbiasprofilebeforeselectionaidsinformulating
effectiveevaluationstrategiesandobtainingreliableresults.
ComparisonwithDifferentStrategies. Table4showstheeffectivenessofdifferentimprove-
mentstrategiesforenhancingtheevaluationperformanceofGPT-3.5-turbo.Theresultsrevealthat
notallstrategieseffectivelyimproveLLM-as-a-judge’sperformance.ProvidingwithExplanation
(w/ explanation)providesinterpretabilitybyofferingreasonsalongsideevaluationscoresorselec-
tions,whichaidsinlogicalbacktrackingduringhumanreview.However,intermsofevaluation
performanceandbiasmitigation,itgenerallyhasanegativeimpact.Thisperformancedeclineis
speculatedtobecausedbydeeperbiasesintroducedbyself-explanation.SelfValidation(w/ self-
validation)showsminimaleffectiveness,likelyduetotheLLMs’overconfidence,whichmaylimit
itsre-evaluationeffortsduringself-validation.WewillfurtherdiscussthislimitationinSection6.1.
SummarizebyMultipleRoundswithmajorityvoting(w/ majority@5)isastrategywithclear
benefits,showingimprovementsacrossmultipledimensions.Itsuggeststhattakingthemajor-
ity voting results from repeated evaluations helps reduce the impact of randomness in LLMs,
therebyaddressingbiasissues.However,SummarizebyMultipleRoundswithtakingmeanscore(w/
mean@5)orwithtakingbestscore(w/ best-of-5)didnotimprovetheevaluationperformanceand
evenhadsomeadverseeffects.Comparedtow/ majority@5,whichselectsthemajorresultfrom
multiplerounds,w/ mean@5mightincluderesultswithbiasesinthemeanscorecalculation,and
similarlyw/ best-of-5couldpotentiallyselectoverlyhighscoresinfluencedbybiases.Therefore,
thelattertwostrategiesdonoteffectivelymitigatetheimpactofbiasesonautomatedevaluation.
TheevaluationresultsofVotebyMultipleLLMs(multiLLMsset1andset2)arecloselyrelated
to the LLM selection. Comparing set 1 and set 2, where LLaMA3-8B-Instruct was replaced by
Qwen2.5-7B-Instruct in set 2, it revealed significant differences in performance across various
dimensions. In set 1, the poor performance of GPT-3.5-turbo and LLaMA3-8B-Instruct in the
LengthBiasnegativelyimpactedtheoverallperformance,whereasinset2,theperformancein
this dimension was better, which was aligned with Qwen2.5-7B-Instruct. Similar trends were
observedindimensionslikePositionBias,FamiliarKnowledgeBias,andsoon.Thissuggeststhat
whenmultipleLLMsareadoptedforjointevaluation,thedifferencesbetweentheirevaluation
performancesmustbecarefullyconsidered.
Basedoncurrentexperiments,severalevaluationstrategydesignsuggestionsmaybebeneficial
forachievingreliableevaluations.First,integratingmultiple-sourceresultsservesasastraightfor-
wardandeffectiveapproach.Afterselectingreliablemodelsasevaluators,integratingmulti-source
resultseffectivelymitigatesthenegativeimpactsofinherentnoise(e.g.,stochasticityinLLMs),
enhancingthestabilityandtrustworthinessofevaluationresults.Second,experimentscomparing
majority@5andmean@5strategiesrevealthatpairwiseevaluationsbyLLMsyieldmorereliable
resultsthanpointwise—likelybecausethecomparisonprocessbettercapturesnuanceddistinctions.
Finally, simultaneously generating evaluations and explanations may not be advisable. While
explanationshelphumansunderstandLLMdecisionprocesses,theirsimultaneousexecutionmay
compromisethequalityofevaluations.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
EvaluationofReasoningLLM-as-a-Judge. AsdiscussedinSections2.4and2.5,judgment
servesasthefoundationforeffectivereasoningcapabilities.Inotherwords,modelswithstronger
reasoning capabilities are generally better equipped to perform as reliable judges. To validate
this assumption, we conducted evaluations on several reasoning LLMs, including o1-mini, o3-
mini,Gemini-thinking,andDeepseek-R1.TheresultsinTables2and3providekeyinsightsinto
theperformanceofreasoning-focusedLLMs.Whilethesemodels—gemini-2.0-thinking,o1-mini,
o3-mini,anddeepseekr1—demonstratecompetitivealignmentandaccuracyrelativetothe
top-performingGPT-4-turbo,theirimprovementsintasksrequiringhumanalignmentare
notaspronouncedasexpected.
GPT-4-turbo remains the benchmark for alignment, achieving the highest accuracy rates of
68.47%and69.44%inthehuman=model1andhuman=model2scenarios,respectively.Italsoexcels
in resolving ambiguous cases, with an accuracy of 29.67% in the human=TIE scenario, outper-
formingallothermodels.Amongreasoning-enhancedmodels,gemini-2.0-thinkingshowsstrong
performanceinthehuman=model2scenario,achievinganaccuracyof78.27%—surpassingGPT-4-
turbo—highlightingitscapabilitytoidentifymodelsthatalignmorecloselywithhumanjudgment.
However,thisstrengthdoesnotconsistentlyextendtoothertasksorscenarios.Similarly,o1-mini
anddeepseek-R1,whiletrailingslightlybehindGPT-4-turboandgemini-2.0-thinking,outperform
non-GPTmodelslikeMixtral-8×7B-Instruct-v0.1,demonstratingtheaddedvalueofreasoning-based
enhancementsinalignmenttasks.Theseresultsindicatethatreasoning-enhancedLLMsprovide
meaningfuladvancementsoverbaselinemodelsbutfallshortofdeliveringconsistent
advantagesinalignment-relatedtasks,suggestingroomforfurtheroptimizationinthisarea.
ExperimentSummary. DuetotheinherentcapabilitiesandpotentialrisksofLLMs,common
improvementstrategiesforLLM-as-a-judgearenotfullyeffectiveinimprovingtheperformanceor
mitigatingbiases.ThelimitationsandchallengeswillbefurtherdiscussedinSection6.
Based on the current experimental analysis, an empirical strategy for pairwise comparison
evaluationtasksistoselectmorepowerfulLLMsandtoadopttwoevaluationstrategies:
oneisswappingthepositionsoftheevaluationcontents,theotheristakingthemajority
votingresultsfrommultipleroundsofevaluation,whichcaneffectivelymitigatebiases.As
forimprovingthealignmentwithhumans,furtherexplorationisstillneeded.
4.5 RethinkingMeta-evaluation
Whilepriorworkhasintroducedvariousevaluationdimensions,datasets,andmetrics,suchefforts
remaininsufficientforevaluatingLLM-as-a-Judge.Basedonacomprehensivereviewofexisting
worksandtheempiricalanalysesforexperimentsinsec4.4,itcanbeobservedthatcurrentmeta-
evaluationframeworkscontinuetofacesubstantiallimitations,underscoringtheneedformore
systematicandrobustapproaches.
(1)NeedforUnifiedandComprehensiveBenchmark.Giventhediverseevaluationdimensions,
suchasagreement,multipletypesofbias,andadversarialrobustness,thereisapressingneed
foraunifiedbenchmarkthatsystematicallyandcomprehensivelyquantifiesthesebiaseswithin
asingleframework.AsshowninTable1,EVALBIASBENCH [110]wasproposedasatestsetto
measuresixtypesofbias.Otherwork[185]isdedicatedtoproposingaunifiedbiastestingprocess,
includingautomatedperturbationandaunifiedmetric.Theyconstructedabiasquantification
frameworkCALM,whichcovers12typesofbias.Despitetheseefforts,existingworkonlycoversa
subsetofevaluationdimensionsandlacksacomprehensiveframeworkthatincludesallrelevant
aspects.Asaresult,manycurrentstudiesthatadoptLLM-as-a-judgestillneedtodesigntheirown
meta-evaluationprotocolsandconductmanualverificationtojustifythereliability.Establishinga
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
unified,systematic,andauthoritativemeta-evaluationbenchmarkwouldsignificantlyadvancethe
developmentandadoptionofLLM-as-a-judge.
(2)ChallengesofControlledStudy.Whenevaluatingaspecificdimension,especiallyaparticular
typeofbias,itisoftenchallengingtoisolatethebiasofinterestfromotherconfoundingfactors
such as additional biases or general quality-related characteristics. For instance, in the case of
positionbias,lengtheningtheresponsecouldpotentiallyalterthestyle,fluency,andcoherence,or
evenintroducenewbiasessuchasself-enhancementbias.Additionally,thetendencyforGPT-4Itnoformal Definition
What is LLM-as-a Judge?
favoritsownresponsesoverthoseofGPT-3.5canbeinterpretedaseitherself-enhancementbiFaosrmal Definition
orapropertendencytowardshigherqualitytext.Therefore,itisessentialforanalyticalworkto
carefullycontrolforthesevariances. In-Context Learning
Model Selection
5 APPLICATIONS How to use LLM-as-a-Judge? Post-processing
TheapplicationofLLM-as-a-Judgespansawidespectrum,reflectingbothtechnicaladvancemenEtvsaluation Pipeline
anddomain-specificdemands.Inmachinelearning,theyareusedtoevaluateNLPtasks,asseQsusick Practice
socialintelligence,andsupportmulti-modalevaluation.Beyondthetechnicalsphere,LLMsare
increasinglyappliedincriticaldomains,asshowninFigure14,suchasfinance,law,andscientific Improving Prompts
(ICL Based)
discovery(Ai4Sci)[210],wheredomainexpertiseandrigorousevaluationareindispensable.
Improving LLMs' Abilities
How to improve LLM-as-a-Judge? (Model Based)
Improving Final Results
(Post-processing Based)
the viabil t i o ty e o v f a c lu re a a te ti ve ideas. the qualit t y o o e f v a a c l a u d a e te m ic works. Basic metric
Bias
How to evaluate LLM-as-a-Judge? Adversarial Robustness
LLM-as-a-Judge Meta-evaluation
Benchmark
Writer
Reviewer
Why is LLM-as-a-Judge important for AGI?
Machine Learning
Application Finance
Law
Doctor Quant Other specific domains
Ai4Sci
Others
to evaluate play as to evaluateR eliability
pa2ent data to diagnose condi7ons. market trends and financial risks.
Challenges Robustness
Powerful Backbone Model
Fig.14. ThedevelopmentprocessandfutureprospectsofLLM-as-a-Judge.
More Reliable LLM-as-a-Judge
IntheAIera[178],LLM-as-a-JudgesystemsarealsodemonstratingtheirpotenLtLiMa-last-oa-Jaudsgseis fotr oDrata Annotation
evenreplacehumanjudgmentacrossabroadrangeofprofessionaldFoumtuarein wso.rkMany r MoLlLeMs-aisn-ah-Jeurdegnetly
require the ability to evaluate, assess, or adjudicate complex scenarios, and LLMMorse, LLwMi-atsh-a-tJhudegier Benchmarks
advanced data processing and pattern recognition capabilities, are particularly LLwMe-alsl--as-Juuditgee dfor tLoLM Optimization
supportorenhancethesetasks[166].Forinstance,writerscanleverageLLMstoassesstheviability
andoriginalityofcreativeideasbyanalyzingnarrativestructuresandmarkettrends;doctorscan
employLLMstodiagnoseconditionsandpredictoutcomesfrommedicalrecordsandimaging
data [142, 206, 217]; quantitative analysts can utilize LLMs to forecast market movements and
assessrisksbyidentifyingpatternsinfinancialdata;andjudgescanrelyonLLMstointerpret
lawsandprecedents,aidingintheadjudicationoflegalcases.Theseemergingapplicationsfurther
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
demonstratetheadaptabilityofLLMevaluators,openingpathwaystowardbroaderintegration
in practice. This section systematically reviews these domains, outlining how LLM-as-a-Judge
contributestoreliableandscalableevaluationineach.
5.1 MachineLearning
LargeLanguageModels(LLMs)haveemergedaspowerfulevaluativetoolsacrossawiderange
ofmachinelearning(ML)tasks,givingrisetotheparadigmof“LLM-as-a-Judge”.Thisapproach
leveragesthelanguageunderstandingandreasoningcapabilitiesofLLMsnotonlytogenerate
responsesorpredictions,butalsotoassess,critique,andcomparemodeloutputsinvariousscenarios.
ApplicationsspanclassicNLPtasks,textgeneration,reasoningandproceduraltasks,information
retrieval,aswellasmorerecentadvancesinsocialintelligenceandmulti-modalunderstanding.
Inthefollowing,wecategorizethemainareaswhereLLM-as-a-Judgehasbeenactivelyapplied
withinmachinelearning,andanalyzetheuniquerequirementsandchallengesencounteredineach
domain.
5.1.1 NLP. LLMshavebeensuccessfullyemployedasevaluatorsinseveralNLPtasks,including
sentimentanalysis,machinetranslation,andtextsummarization.Insentimentanalysis,numerous
biasesinfluencingLLM-basedjudgmentshavebeenidentified,promptingthecreationofautomated
frameworkstosystematicallyquantifythesebiases.
TextGeneration. Textgenerationtasks,suchasdialogresponsegeneration,summarization,
storycreation,andcreativewriting,requirecontentthatissafe,accurate,andcontextuallyrelevant,
thoughthereisn’tasingle"correct"answer[6,9].Unliketraditionalmetrics-basedevaluations,
LLM-as-a-judgeoffersanuanced,adaptable,andcustomizedassessment.AccordingtoZhengetal.
[213], LLMs like GPT-4 can evaluate text generation comparably to humans. This method has
beenusedtoevaluateoutputsfromsinglemodelsandtocomparemultiplemodelsincompetitive
settings.Forinstance,Gaoetal.[38]employChatGPTforhuman-likesummarizationevaluation,
whileWuetal.[169]proposeacomparison-basedframeworkwhereLLMsactasjudgestoevaluate
summarizationquality.
ModernLLMsexcelatgeneratingdetailed,long-formresponses,butlongeroutputsincrease
theriskofhallucinations.Toaddressthis,Chengetal.[21]andZhangetal.[198]useGPT-4to
identifylogicallystructuredyetnonsensicalstatements.Additionally,Wangetal.[152]propose
acritique-basedsystemtoevaluatehallucinationsbyselectingrelevantevidenceandproviding
detailedcritiques.Beyondhallucinations,generatingharmfulorunsaferesponsesisasignificant
concern.Totacklethis,Lietal.[80]introduceMD-JudgeandMCQ-Judgeforevaluatingsafety-
relatedQApairs,focusingonqueriesdesignedtoprovokeunsaferesponses.However,anoverly
cautiousapproachcanleadtoexcessiverefusalresponses,affectinguserexperience.Toexplore
this,Xieetal.[172]conductameta-evaluationofvariousLLM-as-a-judgeframeworks,assessing
refusaltendenciesinresponsetopotentiallyunsafequeries.Additionally,Yuetal.[189]introduce
anLLM-basedanswerextractortoaccuratelyidentifycriticalpartsofanswersintextgeneration,
andAnetal.[2]proposeL-Eval,aframeworkforstandardizedevaluationoflong-contextlanguage
models,followedbyBaietal.[7]whouseLLM-as-a-judgetofilterevaluationdataforlong-context
LLMs.
RecentstudieshavealsousedLLM-as-a-judgetoevaluatethegeneralcapabilitiesofgenerative
modelsthroughdebate-basedframeworks.Forexample,Chanetal.[15]introduceamulti-agent
debateframeworktofacilitateautonomousdiscussionsandassessthequalityofgeneratedresponses
intasks.Similarly,Monirietal.[106]proposeanautomateddebateframeworktoevaluateLLMs
ondomainknowledge,problemdefinition,andinconsistencyrecognition.
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
Reasoning. Enhancing the reasoning capabilities of LLMs can overcome the limitations of
scalinglaws,unlockingtheirfullpotential.Effectivereasoningisessentialfortacklingcomplex
problems,makinginformeddecisions,anddeliveringaccurate,context-awareresponses.Weietal.
[167] introduce Chain-of-Thought (CoT) prompting to facilitate step-by-step reasoning. More
sophisticated cognitive structures [43, 182] have been proposed to further enhance reasoning,
yetselectingareliablereasoningpathremainsasignificantchallenge.LLM-as-a-judgehasbeen
employedtoaddressthisissue.
Somestudiesfocusonsample-levelreasoningpathselection.Gaoetal.[36]presentastrategy
evaluatorforassessingcandidatestrategies.KawabataandSugawara[60]proposeREPS(Rationale
Enhancement through Pairwise Selection), which uses pairwise self-evaluation to select valid
rationales.Lahotietal.[71]demonstratethatLLMscanidentifyandenhanceresponsediversityby
aggregatingmultiplecritiques.Inmulti-agentframeworks,Liangetal.[83]introducemulti-agent
debating(MAD),whereajudgeLLMselectsthemostreasonableresponse.Similarly,Lietal.[76]
utilize a judge LLM in layer-based multi-agent collaboration to improve response quality and
efficiency.
Forstep-levelreasoningpathselection,LLMsactasprocessrewardmodels(PRMs)toevaluate
statescores.Creswelletal.[23]breakdownreasoningintoSelectionandInference,usingLLMsto
judgepotentialreasoningtraces.Xieetal.[173]proposetheKwai-STaRframework,transforming
LLMsintostate-transitionreasonersformathematicalreasoning.Lightmanetal.[84]trainLLMsas
PRMsforinference-timesupervisionandbest-of-Nsampling.Setluretal.[124]introduceprocess
advantageverifiers(PAVs)togeneraterewardsbasedonthelikelihoodoffuturecorrectresponses.
Advanced cognitive structures are also simulated; Hao et al. [43] use LLMs as a world model
withMonteCarloTreeSearch(MCTS)fordeliberatepathselection.Bestaetal.[10]modelLLM
outputsasgraphstoevaluatecoherenceandlogicalreasoning.Additionally,critique-basedLLM
judges[4,72,184,194]providedetailedfeedbacktoenhancethereasoningprocess.
Yao et al. [183] pioneered the use of LLMs in an interleaved manner to generate reasoning
tracesandtask-specificactions.Reasoningtracesguidethemodelinupdatingactionplans,while
actionsfacilitateinteractionwithexternalsources.Buildingonthis,Yangetal.[180]introduced
Auto-GPT,whichleveragesLLM-as-a-judgetoenhancetoolusageaccuracy.Byintegratingavariety
ofexternaltools,LLMsbecomemoreversatile,improvingplanningperformancethroughjudicious
tool selection. Sha et al. [125] explored the potential of LLMs in decision-making for complex
autonomousdrivingscenarios,requiringhuman-likecommonsensereasoning.Zhouetal.[220]
employedaself-discoveryprocesswhereLLMsjudgequeriesandselectthemostsuitablereasoning
structureforsubsequentinference.
Retrieval. The role of LLM-as-a-judge in retrieval encompasses both traditional document
rankinganddynamicRetrieval-AugmentedGeneration(RAG)approaches.Intraditionalretrieval,
LLMs enhance ranking accuracy through advanced prompting techniques, enabling effective
documentorderingwithminimallabeleddata.RAGframeworksleverageLLMs’abilitytogenerate
contentguidedbyretrievedinformation,supportingapplicationsrequiringcomplexorevolving
knowledgeintegration.
RecentstudieshaveexploredLLMsasjudgesfordocumentranking,aimingtoboostprecision
andreducerelianceonextensivetrainingdata.Zhuangetal.[223]embedfine-grainedrelevance
labelswithinLLMprompts,enablingmodelstodistinguishsubtlerelevancevariationsforrefined
documentordering.InnovationsinlistwiserankingincludeMaetal.[102]’sListwiseReranker
withaLargeLanguageModel(LRL),whichreordersdocumentidentifierswithouttask-specific
trainingdata.Zhuangetal.[224]introduceaSetwisepromptingstrategyforzero-shotranking,
enhancingefficiencywithoutsacrificingperformance.Toaddresspositionalbiases,Tangetal.[141]
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
proposepermutationself-consistency,averagingmultiplelistorderstoyieldorder-independent
rankings.Qinetal.[112]critiquepointwiseandlistwiserankingprompts,proposingPairwise
RankingPrompting(PRP)withmedium-sized,open-sourceLLMsasacost-efficientalternativeto
largermodels.
RecentadvancementsinRAGhaveexploredLLMs’capacityforself-evaluationandimprovement
withoutannotateddatasetsorparameteradjustments.Tangetal.[140]proposeSelf-Retrieval,con-
solidatinginformationretrievalwithinasingleLLMusingnaturallanguageindexing,transforming
retrievalintoadocumentgenerationandself-assessmentprocess.Inquestionanswering,LLMsare
increasinglyusedasevaluativeagents.Rackauckasetal.[114]introduceanLLM-basedevaluation
frameworkgeneratingsyntheticqueriesfromuserinteractionsanddomain-specificdocuments,
withLLMsevaluatingretrieveddocumentsandrankingRAGagentvariantsviaRAGElo.Zhang
etal.[199]studyLLMs’abilitytoassessrelevanceversusutilityinopen-domainQA,demonstrating
effectivedistinctionandadaptabilitywithcounterfactualpassages.
Domain-specificRAGsystemsrevealLLMs’potentialtonavigatecomplexqueriesbyintegrating
specializedknowledgestructures.Wangetal.[153]presentBIORAG,enhancingvectorretrieval
withhierarchicalknowledgestructuresandaself-awareevaluatedretriever.Lietal.[77]introduce
DALK,combininganLLMwithacontinuouslyevolvingAlzheimer’sDiseaseknowledgegraph,
usingself-awareknowledgeretrievalfornoisefiltering.Jeongetal.[53]proposeSelf-BioRAG,
adaptingRAGprinciplestobiomedicalapplicationsLiuetal.[92],withLLMsselectingthebest
evidenceforanswergeneration.
Within NLP, especially for tasks such as text generation, reasoning and retrieval, LLM-as-a-
Judgeenablesflexible,scalable,andhuman-alignedevaluation.However,theopen-endednessand
diversityofNLPtasks(suchasdialogorstorygeneration)meanthattherequirementsforjudgment
reliabilityoftenfocusonrobustnesstocontext,avoidanceofhallucinations,andsensitivitytosubtle
errorsorbiases.Indomainssuchassafetyorfactualityevaluation,higherreliabilityisneededdue
totheriskofgeneratingunsafeormisleadingcontent.Thisspecificityraisesdemandsforboththe
reasoningabilityandthetransparencyoftheLLMjudge,ashighlightedbytheincreasingfocuson
critique-basedandmeta-evaluations.
5.1.2 SocialIntelligence. Asthecapabilitiesoflargelanguagemodels(LLMs)continuetogrow,
theyareincreasinglybeingappliedtotasksthatrequirenuancedsocialunderstanding—abilities
traditionallyconsidereduniquelyhuman.Socialintelligenceencompassesarangeofcompetencies,
includingtheinterpretationofsocialcontexts,adherencetoethicalandculturalnorms,under-
standingofemotionalcues,andparticipationinmulti-turninteractionsthatinvolvenegotiation,
persuasion,orempathy.Evaluatingthesecapabilitiesrequiresmovingbeyondconventionalaca-
demicbenchmarkstowardmoreinteractiveandcontext-sensitiveframeworks.
Recent studies have begun to systematically explore the social intelligence of LLMs. For ex-
ample,Xuetal.[175]conductacomprehensiveassessmentcomparingLLMs’socialreasoning
skillswiththeirperformanceonacademictasks.TheirfindingsindicatethatalthoughLLMshave
madesubstantialprogressinstructuredproblem-solving,theystilllagsignificantlyinsocialin-
telligencerelativetohumanstandards.Tofacilitatemorenuancedevaluation,Zhouetal.[221]
developedSOTOPIA,asimulatedenvironmentwheremultipleLLM-basedagentsinteractinrich
socialscenarioswithassignedgoalsandsocialconstraints.Theaccompanyingevaluationframe-
work,SOTOPIA-EVAL,employsGPT-4asanautomatedjudgetoassesstheagents’performance
ondimensionssuchasgoalachievement,financialdecision-making,andmaintenanceofsocial
relationships.Thislineofresearchhighlightsboththepotentialandthelimitationsofcurrent
LLMsinreplicatinghuman-likesocialreasoningandinteraction.Zhangetal.[196]introduces
“Agent-as-a-Judge,”ascalableframeworkinwhichlargelanguagemodelsareinstructedtoactas
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
sentientevaluatorsofmulti-agentsocialinteractions.ByembeddingLLMsinrole-playingscenarios
thatdemandtheory-of-mind,empathy,andconflictresolution,thestudyshowsthatGPT-4-based
judgescorrelatestronglywith humanratings(r=0.83)onhigher-ordersocialcognitiontasks,
whilealsorevealingsystematicbiasesthatincreasewithagentanonymity.
Furthereffortsarebeingmadetorefineevaluationprotocolsandexpandthescopeofsocial
intelligencebenchmarks.Someresearchersareincorporatinghuman-in-the-loopevaluationsto
calibrateautomatedjudgments,whileothersaredesigningmorediverseculturalandlinguistic
scenariostotestcross-culturaladaptability.ThesedevelopmentsarecriticalfordeployingLLMs
inapplicationssuchasvirtualassistants,educationaltools,andinteractiveentertainment,where
socialalignmentisessentialforusertrustandengagement.
5.1.3 Multi-ModalEvaluation. Theemergenceofmulti-modallargelanguagemodels(MLLMs)
thatintegratetextwithvisual,auditory,andothersensoryinputshascreatedaneedforrobust
evaluationframeworkscapableofassessingcross-modalunderstandingandgeneration.Multi-
modalevaluationintroducesuniquechallengessuchasmodalityalignment,semanticconsistency
acrossdomains,andtheintegrationofcontextualinformationfromheterogeneoussources.
Severalrecentbenchmarkshavebeendevelopedtoaddressthesechallenges.Chenetal.[17]
introducedacomprehensivebenchmarkforevaluatingMLLMsontasksincludingimagecaptioning,
visualquestionanswering,andmathematicalreasoningwithvisualinputs.Theirstudyrevealed
that while LLM-based judges perform well in pairwise comparisons—often matching human
preferences—theystrugglewithabsolutescoringandbatchrankingtasks,whereconsistencyand
calibrationaremoredifficulttoachieve.Inthecontextofnon-Englishmodalities,Wuetal.[170]
presentedabenchmarkfocusedonChinesemulti-modalalignment,identifyingspecificchallenges
relatedtocoherenceandreasoning.Theyproposedacalibratedevaluationmodelthatsignificantly
improvesjudgmentconsistencyoverexistingsystems.
Toincreasetransparencyinmulti-modalevaluations,Xiongetal.[174]exploredtheuseofLLM-
as-a-judgetonotonlyscoremodeloutputsbutalsogeneratenaturallanguagerationalesexplaining
eachassessment.Thisdualapproachimprovestheinterpretabilityofmodeljudgmentsandhelps
developersidentifyfailuremodes.Inaspecializedapplication,Chenetal.[20]constructedthe
firstbenchmarkforevaluatinglargevision-languagemodels(LVLMs)onself-drivingcornercases.
TheirresultsdemonstratethatLLM-basedjudgescorrelatemorecloselywithhumanevaluations
thanjudgmentsprovidedbyLVLMsthemselves,underscoringthegeneralizabilityoftext-based
judgeseveninvision-dominatedtasks.
Surveyingbroadertrends,Jiangetal.[54]reviewedadvancementsinmulti-modalandmulti-
agentsystems,highlightingmechanismsdesignedtoenhanceinter-agentcollaborationandreduce
cognitivebias.Ongoingresearchisextendingmulti-modalevaluationtodynamicvideocontent,
audio-visualintegration,andembodiedAIenvironments,wheretemporalandinteractivedimen-
sionsfurthercomplicateassessment.Theseeffortscollectivelycontributetomorereliable,scalable,
andhuman-alignedevaluationparadigmsformulti-modalAIsystems.
5.2 OtherSpecificDomains
5.2.1 Finance. LLMshavedemonstratedsignificantpotentialinthefinancedomain,particularly
intaskssuchasforecasting,anomalydetection,andpersonalizedtextgeneration[209].Asfinancial
applicationsfrequentlyrequirerigorousevaluationswithhighstakes,thereisanincreasingdemand
forreliableandtransparentLLM-basedevaluatorstailoredtofinancialcontexts.
CurrentresearchonLLM-as-a-Judgeapplicationsinfinanceprimarilyfallsintothreemainareas.
Firstly,considerableeffortshavefocusedondesigningevaluatorsthateffectivelyincorporateexpert
domainknowledge.Forinstance,Briefetal.[13]investigatedmulti-taskfine-tuningtechniques
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
LLM-as-a-Judge Quantitative Evaluation
Based on the eval result, I suggest several further {ic_score: 0.08, turnover: 0.24, Sharpe:
improvements: 1. incorporate ema smoothing … 1.21, vol: 0.24, max_drawdown: 0.24}
Real Environment
etadpU Submit
Writer
Knowledge
Shared Context retrieval
𝒕𝟎 𝒕𝟏 𝒕𝟐 𝒕𝑻 I
in
n
f
-
e
c
r
o
e
n
n
te
ce
xt
Trading t w t 6 s , s 6 _ _ ) z 6 s , s 6 u c ) m 2 o ) 5 ( r t 2 e / s ) ( , _ ( a t v 2 s 5 _ _ d 2 a ) i v f _ f( d c i a f s f( h c f a l s o h w f , l o t n 2 s t 5 _ a 2 z l ) s _ , c a o l 2 r p 5 e h 2 a ( ) _ c 0 ov ， ar a i l a p n h c a e _ ( 1 f , u ndame i _ - f a 1 _ v ) e g l ( s n e ew ( s c _ o s n e d n = t r i an ) k ) ( ), t s a _ l s p u h m a ( _ v 1 e , c I it n e n r e a r ti o lo n op
Idea: ……
Cashflow
KB alpha R f P u a e n s v d s i a e e m w d : e : M F nt A a a L y l d S a a E ls ta o a in s c c o o rp n o fi r r a m te a tion R s a P e c a e c n s v u t s i i e r m e a w d e te : : n M F t A t a o L y m S c E o a m ke b i i t n m e o w r i e th R Pa e s v s ie e w d : : T L R oo U k E s good to me!
Final
Answer
LLM-as-a-Judge
Fig.15. Illustrationofusingdual-LLMiterativefeedbackloopforalphagenerationinfinance.Figureadapted
fromWangetal.[157].
specificallydevelopedtoimproveLLMperformanceinfinance-relatedassessments.Similarly,Yu
etal.[190]introducedFinCon,amulti-agentsystemthatutilisesconceptualverbalreinforcement
fromanLLM-basedevaluatortosupportfinancialdecision-makingprocesses.
Secondly,developingrobustbenchmarksandevaluationframeworksconstitutesamajorareaof
research.RepresentativeeffortsincludeUCFE,afinancialevaluationbenchmarkbasedonuserfeed-
back[181];IndoCareer,adatasetconsistingofprofessionalfinancialexaminationquestions[67];
andAI-generated,domain-specificevaluationsetsdesignedtosystematicallyassessLLMs’under-
standingoffinancialknowledgeandreasoningabilities[117].
Thirdly, targeted research addresses specific application scenarios within finance, including
quantitativeinvestmentstrategies,creditscoring,andESG(Environmental,Social,andGovernance)
scoring.Wangetal.[157]proposedtheQuantAgentframework,whichemploysadual-LLMiterative
looptorefinetradingsignals.Inthisarchitecture,oneLLMgeneratesinitialtradingideas,whilea
secondLLMrigorouslyevaluatesanditerativelyimprovestheseideasusingquantitativemetrics
suchastheinformationcoefficientandSharperatio(seeFigure15).Additionally,recentstudieshave
demonstratedpromisingLLM-basedevaluatorsforcreditscoring[5,187]andESGscoring[209],
furtherhighlightingthebroadpotentialofLLMsinfinancialapplications.
Despitetheseadvancements,currentapplicationsremainintheirearlystages,constrainedby
several critical limitations. Ensuring factual accuracy and consistent judgments is challenging,
particularlywhennavigatingcomplexfinancialregulationsorrapidlyevolvingmarketdata.Addi-
tionally,LLMsprimarilyexcelinqualitativeassessmentsandtextualanalysis—suchasreviewing
financialnewsorreports—andcurrentlycannotautonomouslyperformquantitativetaskssuch
asportfoliooptimizationorhigh-frequencytrading.Assuch,theirroleremainspredominantly
auxiliary.
Insummary,LLM-as-a-Judgeapplicationsinfinanceareinanemergentphase,showingpromise
inqualitativeanalysisbutlimitedbyinconsistenciesinhandlingdynamicmarketdataandregulatory
complexities.Usersdemandhighreliabilityintheformoffactualaccuracyandconsistentjudgments
tomitigatefinancialrisks,echoingbroaderchallengesinbiasmitigationandrobustnessdiscussed
earlierinthissurvey.Assuch,integratingdomain-specificvalidationwillbekeytobuildingtrust
andenablingscalabledeployment.
5.2.2 Law. LLMshaveshowngrowingcapabilitiesinprovidingprofessionaladviceinspecialized
fieldssuchaslegalconsultation,particularlyexcellingintasksliketextsummarizationandlegal
reasoning.Giventhecomplexity,sensitivity,andsocietalimportanceoflegaldecisions,thelegal
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
domainexhibitsheightenedconcernsregardingpotentialbiases,factualinaccuracies,andtrans-
parencychallengesinherentinLLM-basedevaluators.Thus,rigorousevaluationmethodologies
areimperativeforresponsibledeploymentinthiscontext.
CurrentresearchonLLM-as-a-Judgeapplicationsinthelegaldomaincanbecategorizedinto
twomainareas.Firstly,considerableeffortsaredevotedtodevelopingspecializedevaluatorsthat
directlyincorporateexpertlegalknowledgeandpractices.Forexample,Maetal.[101]employ
generalLLMswithexpert-designedfew-shotpromptstosimulatetheannotationprocess,effectively
identifyinglegallyrelevantfactsandprecedents.Thisdemonstratesthepotentialofautomated
judicialevaluators.Cheongetal.[22]proposeacomprehensivefour-dimensionalframeworkfor
developingresponsibleLLM-drivenlegaladvicesystems.Thisframeworkexplicitlyconsidersuser
characteristics,queryspecificity,AIcapabilities,andbroadersocialimplications,emphasisingthe
needforanuancedandcontext-awareapproachtoLLMintegrationinlegalpractice.Similarly,
Ryuetal.[119]introduceEval-RAG,aretrieval-augmentedevaluatordesignedtovalidateLLM-
generatedlegaltexts.InexperimentsinvolvingKoreanlegalquestion-answeringtasks,Eval-RAG
achievedcloseralignmentwithhumanexpertjudgementsthanconventionalevaluationmethods,
reinforcingthevalueofintegratingdomain-specificretrievalmechanisms.
Secondly,thedevelopmentofcomprehensivebenchmarksandevaluationdatasetsrepresentsa
crucialresearcharea,aimingtosystematicallymeasureandimproveLLMlegalreasoningcapabili-
ties.Representativeexamplesincludemulti-domaindatasetssuchasIndoCareer,whichcontains
professionallegalexaminationquestions[67],andLegalBench,acollaborativebenchmarkspecif-
icallydesignedtoassesslegalreasoningskillsacrossmultiplejurisdictionsandlanguages[41].
Additionally,language-specificbenchmarkshavebeendeveloped,includingLexEvalforevaluating
Chineselegaltexts[78]andEval-RAGforKoreanlegalcontexts[119].Inadditiontoevaluating
technicalreasoningabilities,targetedbenchmarkshavealsobeenintroducedtoassessethically
sensitiveaspectsoflegaladvice,suchasethicalreasoning[204]andthepotentialharmfulness
orbiasespresentingeneratedoutputs[3],highlightingthecomplexityandsensitivityofLLM
evaluationinthelegaldomain.
Despitetheseadvancements,significantgapsandlimitationspersist,restrictingthewidespread
adoptionofLLMsinthelegaldomain.Legalreasoninginherentlyrequiresprecision,transparency,
andstrictadherencetoestablishedstatutesandcaseprecedents.However,currentLLMsarestill
pronetofactualhallucinationsandmayoverlooksubtlebutlegallysignificantdistinctions.Bias
isalsoamajorconcern.LLMstrainedonlarge-scaledatasetsmayunintentionallyincorporate
societalbiases,leadingtounfairorskewedlegaljudgments,especiallyinsensitivecasesinvolving
ethicsorhumanrights.Additionally,duetothecomplexityandvariabilityofjurisdiction-specific
legalframeworks,general-purposeLLMsoftenstruggletocapturenuanceddifferenceswithout
detailedcontextualizationandadditionalguidance.
Future research should prioritize addressing these limitations through targeted innovations.
Promisingdirectionsincludeenhancingfactualreliabilitybyintegratingrobustlegaldatabases
andretrievalmechanisms,therebyenablingreal-timecross-verificationofLLM-generatedoutputs
againstauthoritativelegalsources.Anotherimportantavenueisthedevelopmentofbiasmitigation
strategies, suchas selective filteringof training dataor calibrationprocesses guided byexpert
legal annotations. Crucially, greater interpretability and transparency will be essential. Future
LLMjudgesshouldideallyprovideexplicitrationales,relevantstatutoryreferences,andcoherent
justificationsforeachdecision.Ultimately,closecollaborationbetweenAIdevelopersandlegal
professionalswillbevitaltonavigatingregulatoryframeworks,ensuringethicalcompliance,and
facilitatingtheresponsibledeploymentofLLM-as-a-Judgesystemswithinlegalcontexts.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
5.2.3 AIforScience. LLMshavedemonstratednotablepotentialinscientificfields,particularly
indomainssuchasmedicineandmathematics,wheretheyincreasinglyactasevaluatorstoenhance
accuracyandconsistency[142,210,219].
CurrentresearchonLLM-as-a-Judgeinsciencecanbegroupedintothreemajordirections.First,
specializedevaluatorsarebeingcraftedforhigh-stakesclinicalreasoning.BrakeandSchaaf[12]
showedthataLLaMA-2evaluatorattainshuman-levelagreement(Cohen’s𝜅=0.79)whencheck-
ing the internal consistency of clinical notes, while Krolik et al. [68] reported similarly strong
performance for judging medical Q&A responses. Hosseini et al. [46] released the first public
benchmark targeting long-form medical QA; their study found that open-weight LLMs acting
asjudgescorrelatewellwithphysicianratingsoncriteriasuchascorrectness,helpfulnessand
harmfulness.
Second,mathematicsresearchhasembracedstep-wiserewardmodelingtoverifyreasoning
chains.WizardMathappliesReinforcementLearningfromEvol-InstructFeedbackandsurpasses
GPT-3.5onGSM8KandMATH[99].Buildingonthisidea,Math-Shepherdintroducesanautomatic
process-reward model that verifies each reasoning step without human annotations and then
reinforcesthesolver,boostingMistral-7Baccuracyto84.1%onGSM8K[156].Tongetal.proposed
DART-Math,adifficulty-awarerejection-tuningpipelinethatfocusestrainingonhardproblems
andachievesstate-of-the-artresultsacrosssixmathbenchmarks[146].Formultimodalscenarios,
Luetal.createdMathVistatoevaluatetextual–visualreasoning,revealingpersistentweaknesses
whendiagramsareinvolved[97].
Third,comprehensivebenchmarkingframeworksareemergingtoassessscientificLLMjudgesat
scale.NatureMedicine’s2024reviewhighlightedgapsinautomaticmetricsandadvocatedclinician-
in-the-looppipelinesforsummarizationtasks[151].StanfordHAI’sMedHELMintroducedaholistic
evaluationsuitecoveringelevenclinicaltasksandshowedthateventopcommercialmodelsstill
lagonmedication-safetyquestions[64].Inmathematics,Xiaetal.[171]builtalogic-coherence
judgethatscoresentireprooftrajectoriesratherthanfinalanswers,providingricherdiagnostic
signals.
Limitationsandfuturedirections.Despiterapidprogress,currentmedicalevaluatorsoftenrely
onexam-styleorshort-formoutputsandstrugglewithreal-worldclinicalcomplexity;hallucination
detectionremainsanopenproblem[64].Math-centricjudgesarestillbrittleonopen-endedor
multimodalproblems,andexhaustivestepverificationiscomputationallycostly.Futureworkshould
fuseLLMjudgeswithsymbolicsolversormedicalknowledgebasesforfact-checking,incorporate
uncertaintyestimation(e.g.calibratedrefusals),anddesignmultimodal-awarejudgescapableof
interpretingfiguresandtables.Finally,establishingpublic,diversescientificbenchmarks—paired
withtransparentreportingoffailurecases—willbecrucialfortrustworthydeploymentofLLM-as-
a-Judgesystemsinscientificresearchandpractice.
Insummary,theLLM-as-a-Judgeparadigminscientificdomainsisprogressingrapidly,supported
byspecialisedevaluatorsandbenchmarks.However,itsuptakeremainslimitedbymultimodal
constraintsandthehighcostofverificationincomplexsettings.Reliabilityrequirementstherefore
centreonhallucinationdetectionandevidence-basedrigourtomaintainscientificvalidity,echoing
thesurvey’sdiscussionofoutputconsistencyandadversarialrobustness.Integratinglargelanguage
models with structured knowledge bases is likely to meet these high-stakes needs for precise,
verifiablejudgements.
5.2.4 Others. LLMshavealsobeenemployedasevaluatorstoenhanceefficiencyandconsistency
acrossvariousfields.Insoftwareengineering,amethodwasproposedforusingLLMstoevaluate
bugreportsummarizations,demonstratinghighaccuracyinassessingcorrectnessandcomplete-
ness, even surpassing human evaluators who experienced fatigue [69]. This approach offers a
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
scalablesolutionforevaluation.Ineducation,automatedessayscoringandrevisinghavebeen
exploredusingopen-sourceLLMs,achievingperformancecomparabletotraditionaldeep-learning
models.Techniquessuchasfew-shotlearningandprompttuningimprovedscoringaccuracy,while
revisions effectively enhanced essay quality without compromising original meaning [132]. In
contentmoderation,anLLM-basedapproachwasdevelopedtoidentifyruleviolationsonplatforms
likeReddit,achievinghightrue-negativeratesbutencounteringchallengeswithcomplexrule
interpretation,emphasizingthenecessityofhumanoversightfornuancedcases[65].Inbehavioral
sciences,theLLM-as-a-Judgeframeworkwasevaluatedforassessinguserpreferencesbasedon
personas,revealinglimitationsinreliabilityandconsistencyduetooversimplifiedpersonas,but
improved significantly through verbal uncertainty estimation, achieving high agreement with
humanevaluationsforhigh-certaintycases[30].TheseapplicationsofLLMsasevaluatorshighlight
theirgrowingpotentialindiversesectors,emphasizingtheneedforintegratingdomain-specific
knowledgeandrefiningmethodologies.
Moreover,LLMsasevaluatorsdemonstratesignificantadvantagesinqualitativeassessments
thataredifficulttoquantify,suchasevaluatingservicequality,analyzinguserexperiencefeedback,
andassessingcreativecontentlikeartorliteraturereviews.LLMs’capabilitytounderstandand
generatenuancedlanguagemakesthemwell-suitedforsubjectiveevaluationtaskstraditionally
requiringhumanjudgment.Futureresearchwillfocusmoreontheseareas,exploringhowLLMsas
judgescanenhanceassessmentaccuracyandconsistencywheretraditionalquantitativemethods
fallshort.
Insummary,theLLM-as-a-Judgeparadigmisgainingtractionacrossdomainssuchassoftware
engineering,educationandbehaviouralscience,whereitenablesscalablequalitativeassessment.
Nevertheless,itsdeploymentisconstrainedbycontext-specificinconsistenciesandbythedifficulty
ofreplacingfatiguedhumanreviewers.Reliabilityrequirementsdifferbyfield.Theyoftencentre
on the consistent interpretation of nuanced rules or subjective preferences so as to minimise
bias,echoingthesurvey’sbroaderthemesofpromptoptimisationandself-consistency.Therefore,
domain-specificadaptationwillbeessentialtosatisfythesevarieddemandsandtosupportreliable,
efficientapplications.
6 CHALLENGES
In this chapter, we explore the key challenges that arise when utilizing LLMs for evaluation
tasks,particularlyinthecontextofLLM-as-a-Judge.Despitetheirgrowingcapabilities,LLMsstill
facesignificantissuesrelatedtoreliability,robustness,andtheirbackbonemodels’limitations.
Understanding these challenges is crucial for advancing the use of LLMs in a fair, consistent,
andreliablemanner.Weaddresstheseconcernsunderfourmainthemes:reliability,robustness,
powerfulbackbonemodels,andtheethicalandsocialimplicationsoftheiruse.
6.1 Reliability
ThereliabilityofLLM-as-a-Judgeisaprimaryconcern,asitdirectlyimpactstheconsistencyand
fairnessofevaluations.Whilehumanjudgesalsoexhibitinherentbiases,LLMsintroducetheirown
uniquesetofreliabilityissues.Theseissuesstemfromtheprobabilisticnatureofthemodelsand
theirsensitivitytoinputnuances.Wecanfurtherbreakdownreliabilitychallengesintoseveral
keyareas.
In-ContextLearningSensitivity. LLMs’in-contextlearningability,whereamodellearnsfrom
examplesinaprompt,canintroducesignificantreliabilityissues.Minorchangesinpromptwording
ortheorderofexamplescanleadtounstableandinconsistentresults.Forinstance,positionbias
isawell-documentedissuewhereLLMstendtofavorthefirstorlastresponseinalist,leading
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
tounfairevaluationsiftheexamplesarepoorlyarranged.Similarly,theinherentrandomnessof
anLLM’sgenerationcancauseinconsistentinter-raterreliability,wherethemodelgivesdifferent
scoresforthesameinput.
Overconfidence andSelf-Enhancement. A majorissue isoverconfidence,where models,
particularlythosetrainedwithReinforcementLearningwithHumanFeedback(RLHF),mayoffer
overlyfavorablescoresfortheirownresponses,leadingtomisleadingevaluations.Thisisoften
tiedtoself-enhancementbias,whereanLLMismorelikelytogiveahigherscoretoananswer
itgenerateditselfcomparedtoanequivalentanswergeneratedbyadifferentmodel.
ModelSelectionandGeneralization. ThechoiceofLLMitselfsignificantlyimpactsevaluation
dependability.Theblack-boxnatureandversiondependencyofcommercialmodelslikeGPT-4
hinderreproducibility.Whilefine-tunedevaluatorsmayseemlikeasolution,theyoftenexhibit
overfitting,meaningtheirevaluationcapabilitiesmaynotgeneralizewellbeyondtheirtraining
data.Thesemodelscanalsoinheritsubtlebiasesfromtheirtrainingdatasets,necessitatingcareful
meta-evaluationtoensurefairness.
6.2 Robustness
TherobustnessofLLM-as-a-Judgereferstoitsabilitytoresistadversarialattacksandinconsistent
inputs.WhileattacksontraditionalNaturalLanguageGeneration(NLG)modelsarewell-studied,
attacks on LLM-as-a-Judge are relatively under-explored. These attacks aim to exploit a judge
model’sbiases,inconsistencies,orloopholestomanipulateitsdecision-makingprocess.
AdversarialAttacks. Unliketraditionalattacksthataimtomakeamodelgenerateharmful
content,attacksonLLM-as-a-Judgeaimtosubtlymanipulatetheinputtochangetheevaluation
outcome.Forexample,anattackercouldintroduceimperceptibleperturbationstothetext—such
asparaphrasingakeysentenceoraddingamisleadingbutgrammaticallycorrectphrase—totrick
thejudgemodelintoadifferentconclusion.Theseattacksareparticularlyinsidiousbecausethe
manipulatedinputappearsharmlesstoahumanbutcancauseasignificantdeviationintheLLM’s
judgment.
InputSensitivityandJailbreaking. LLMjudgesarealsosusceptibletojailbreakingtech-
niques. An attacker could craft a prompt that bypasses the model’s safety and fairness filters,
causingittoproduceabiasedorinconsistentevaluation.Themodelmightbepromptedtotakeon
a"persona"withspecificprejudices,leadingtoskewedjudgments.Thisisasignificantconcernfor
open-sourceLLMjudges,whichmaynothavethesameleveloffine-tuningforsafetyasproprietary
models.
BrittlenessofScoringMechanisms. Therelianceonspecificscoringformatscanbeapoint
ofweakness.Ifapromptrequiresanexactnumericalscore(e.g.,"rateonascaleof1-5"),aclever
attackercouldcreateinputthatconfusesthemodel,causingittooutputtextinsteadofanumber,
thusbreakingtheautomatedscoringpipeline.Thisbrittlenessunderminesthereliabilityand
automationoftheentireevaluationsystem.
6.3 LimitationsofBackboneModels
TheeffectivenessofanyLLM-as-a-Judgesystemisdirectlytiedtoitsunderlyingbackbonemodel’s
capabilities. A primary bottleneck lies in the lack of robust models that can serve as reliable
judgesforcomplex,multimodalcontent.Whilepowerfulintext,currentmultimodalLLMslike
GPT-4Visionstillstrugglewithsophisticatedreasoningthatintegratesdifferentmodalities.For
example,inamedicalcontext,ajudgemodelmightneedtoevaluateadiagnosisbasedonbotha
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
textualdescriptionofsymptomsandanimageofanX-ray.Aflawedmodelcouldmissasubtlebut
criticalinconsistencybetweenthetwo,leadingtoaninaccuratejudgment.Thislimitationposesa
significantchallengetoachievingreliableevaluationsinawiderangeofreal-worldscenarios.
Evenforpurelytext-basedtasks,currentLLMshavelimitationsinabstractandcausalreasoning.
Whenevaluatingaresponsethatrequiresadeepunderstandingoflogicalconsistency,amodel
mightproduceaseeminglyconfidentbutfundamentallyflawedevaluation.Forinstance,injudging
acomplexscientificpaperorlegalargument,themodelmaygiveahighscoreforstylisticfluency
whilefailingtoidentifyasubtlebutfundamentalflawinthelogicalchainorcausalargument.
Thisgapbetweenthemodel’ssuperficialfluencyanditstruereasoningdepthunderminestrust
initsabilitytohandlesophisticatedanalyticalprocessesandhighlightstheneedformorerobust
reasoningbackbones.
6.4 InterpretabilityandTransparencyofJudgments
WhilecurrentLLM-as-a-Judgesystemscanprovideseeminglyreasonablescoresorconclusions
formanytasks,theirevaluationprocessisoftenanopaqueblackbox.Thislackoftransparency
significantlylimitsusertrustandconstrainstheapplicationinhigh-stakesdomainssuchasmedicine,
law,andeducation.Forinstance,inalegalcontext,anLLMjudgemightaccuratelysummarizea
caseandsuggestaverdict,butitcannotexplicitlyshowwhichcaseprecedentsitreferencedor
whichlegalstatutesitprioritizedinitsreasoningprocess.Thisisfundamentallydifferentfrom
humanlawyers,whocanalwaysprovideatraceablerationalefortheirjudgment.Acorechallenge,
therefore,liesindevelopingmethodsthatcanmakethereasoningbehindLLM-basedjudgments
explicitandverifiable,allowinghumanexpertstotraceandvalidatethemodel’slogicpath.
6.5 Meta-EvaluationandTemporalConsistency
ExistingresearchpredominantlyfocusesonassessingtheLLM-as-a-Judge’sevaluationresultson
aspecifictask,whilerarelysubjectingthe"evaluatoritself"tosystematicscrutiny.Thiscreates
acriticalgap,aswelackrigorousbenchmarkstomeasureajudge’saccuracy,stability,andbias.
Thisraisesanewresearchimperative:howdoweevaluatetheevaluator,therebyensuringthe
reliabilityofLLM-as-a-Judgesystems?Furthermore,extensiveempiricalevidencesuggeststhat
theperformanceofLLM-as-a-Judgeisnotstatic,withitsjudgmentspotentiallydriftingovertime
due to model updates or contextual changes. For example, a response to a controversial topic
mightberatedasacceptablebyamodelversionfromMarch,butsubsequentlypenalizedbyaJune
versionduetonewsafetyfine-tuning.This"evaluationdrift,"atypeoftemporalunreliability,is
aparticularlypronouncedissueinpracticalscenarioswhereusersdemandconsistentandstable
standardsoverthelongterm,ultimatelyunderminingtrustandraisingconcernsaboutfairness.
6.6 EthicalandSocialImplications
Beyondtechnicalchallenges,theuseofLLM-as-a-Judgeraisescriticalethicalandsocialquestions
thatmustbeaddressed.
BiasAmplification. LLMsaretrainedonvastamountsofinternetdata,whichoftencontains
societalbiasesrelatedtogender,race,andotherdemographics.Whenusedasjudges,thesemodels
canamplifyandperpetuatethesebiases,leadingtounfairevaluations.Forinstance,amodelmight
unfairlypenalizearesponsewritteninanon-standardEnglishdialectorawritingstyleassociated
withamarginalizedgroup.Thishasprofoundsocialimplications,especiallyinhigh-stakesareas
likehiringorcontentmoderation.
LackofAccountabilityandTransparency. The"blackbox"natureofproprietaryLLMsmakes
itdifficulttounderstandhowtheyarriveataspecificevaluation.Whenanevaluationisdeemed
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
unfairorincorrect,thereisnoclearwaytotracetheerrororholdthemodelaccountable.Thislack
of transparencyunderminestrustintheevaluationprocessandcanbeparticularlyproblematic
infieldswherehumanoversightandaccountabilityareparamount.
ImpactonCreativeandDiverseOutputs. Byactingasajudge,anLLMcaninadvertently
shapethetypesofcontentbeingproduced.Ifamodelconsistentlyfavorsacertainstyle,format,
ortone,itcouldstiflecreativeanddiverseoutputs,leadingtoahomogenizationofcontent.This
phenomenon,knownasevaluation-drivenconvergence,couldharminnovationandreducethe
richnessoftheinformationecosystem.
7 FUTUREWORK
The field of LLM-as-a-Judge is rapidly evolving, moving from an emerging concept to a core
componentofmodernAIdevelopment.Whilewe’veseensignificantprogressinusingLLMsfor
evaluation,therearestillcriticalchallengesandvastopportunitiestoexplore.Thissectionoutlines
keyfutureresearchdirectionsthatareessentialforbuildingmorereliable,versatile,andimpactful
LLM-as-a-Judgesystems.We’lldelveintotopicsrangingfromadvancingthefoundationalreasoning
andjudgmentcapabilitiesofthesemodelstoexpandingtheirapplicationintonewdomainslikedata
annotationandembodiedintelligence.Ourdiscussionalsofocusesonthenecessityofdeveloping
morerobusttheoreticalframeworksandbenchmarkstoensurethesesystemsarenotonlyeffective
butalsotrustworthyandalignedwithhumanvalues.Thisforward-lookingagendaaimstoguide
thenextgenerationofresearch,pavingthewayforLLM-as-a-Judgetobecomeanindispensable
toolinthepursuitofmoreintelligentandsociallybeneficialAI.
7.1 Reasoning-CentricJudgement
Movingforward,Movingforward,thefieldistransitioningfromtraditionalevaluationmethodstoa
reasoning-centricapproachmadepossiblebyLLM-as-a-Judge.Wewillfirstexaminethesymbiotic
relationship between reasoning and judgment, highlighting how their synergy is essential for
creatingsophisticatedandcapableAIsystems.Next,wewilldiscusshowtheintegrationofLLM-
as-a-Judgeintodynamicfeedbackloopsenablescontinuousself-improvement,whichiskeyto
advancingmodelcapabilities.Weconcludewiththelong-termvisionofSelf-EvolvingJudges,which
canadaptandrefinetheirownevaluativeabilitiesovertime.
Improve & Approach
LLM-as-a-Judge
Reasoning/Thinking
Support
Fig.16. TherelationshipofLLM-as-a-JudgeandReasoning/Thinking.
7.1.1 TheSynergyBetweenJudgmentandReasoning. AsshowninFigure16,reasoningand
judgmentaretwodeeplyconnectedyetdistinctcognitiveabilities.Reasoningisthelogicalprocess
ofdrawingconclusionsfromevidenceorpremises.It’stheenginethatpowersproblem-solving,
decision-making,andcriticalanalysis.Incontrast,judgmentistheactofevaluatingsomething—an
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
The Development of Evaluation Method
Fig.17. ThedevelopmentprocessandfutureprospectsofLLM-as-a-Judge.
idea,anoutput,orasituation—againstasetofstandardsorprinciplestodetermineitsqualityor
validity.Thisdistinctioniscrucial,buttheirrelationshipissymbiotic.
ThephilosopherImmanuelKantfamouslydescribedjudgmentas“thefacultyofthinkingthe
particularascontainedundertheuniversal.”InthecontextofLLMs,thismeansapplyingageneral
rule or set of principles (the "universal") to a specific output (the "particular") to determine its
quality.Forexample,anLLM-as-a-Judgemightevaluateageneratedsummaryagainsttheuniversal
principlesofconciseness,accuracy,andcoherence.Therelationshipbetweenthesetwofunctions
is not one-way; they are mutually reinforcing. Reasoning depends on judgment to validate its
intermediatesteps.Asamodelworksthroughacomplexproblem,itneedstoevaluatewhether
eachstepinitschainofthoughtislogicalandcontributestoasoundfinalconclusion.Thisinternal
evaluationisaformofjudgment.Conversely,effectivejudgmentrequiresstrongreasoningtoeval-
uateoptionsagainstalogicalframework.Youcan’tmakeagoodjudgmentwithoutunderstanding
theunderlyinglogic.
ThissynergyisatthecoreofadvancedLLMcapabilities.Whenjudgmentisperformedcontin-
uouslyandatahighfrequency—forinstance,anLLMevaluatingeverystepofitsownthought
process—itstartstoapproximatetheprocessofreasoningitself.Themoreamodelsystematically
evaluatesandrefinesitsownthoughtprocesses,themoreitbecomesaneffectivereasoner.This
iswhyLLM-as-a-Judgeismorethanjustanevaluationtool;it’samechanismforenhancinga
model’sreasoningcapabilities.
7.1.2 FeedbackLoopsandSelf-Improvement. ThetruepoweroftheLLM-as-a-Judgeparadigm
isunleashedwhenitisintegratedintoafeedbackloopthatenablescontinuousself-improvement.
AprimeexampleisOpenAI’so1model,whichdemonstratesenhancedproblem-solvingability
throughstructured,iterativereasoning.Acentralcomponentofo1’sadvancementistheuseofLLM-
as-a-Judgemodulesthatevaluatereasoningpathsateachstage,offeringfeedbackthatimproves
futuresteps.Thisallowsthemodeltocorrectinconsistencies,identifysimplerdecompositionsof
complexproblems,andprogressivelyrefineitsoutputs.
Thisdynamicfeedbackmechanismoperatesintwokeymodes:
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
(1) Training-TimeEvaluation:Duringthetrainingphase,anLLM-as-a-Judgeprovidesfeed-
backonamodel’sreasoningprocess.Thisfeedbackisintegratedintolearningobjectives,for
example,viaRLHForasimilarmechanism.Bylearningfromitsmistakesandsuccesses,the
modelinternalizesbetterreasoningstrategiesthatgeneralizeacrosstasks.
(2) Inference-TimeEvaluation:Duringthetestingordeploymentphase,theLLM-as-a-Judge
dynamicallyevaluatesthemodel’sreasoningasit’shappening.Thisreal-timefeedbackallows
themodeltomakeon-the-flycorrections,refiningitsoutputandleadingtobetterresults
withouttheneedforadditionaltraining.
Thiscontinuousloopofreasoning→judgment→refinementcloselymirrorstheprinciplesof
ConstitutionalAI,aframeworkwheremodelsaretrainedtoself-critiqueandself-correctbased
onasetofpredefinedprinciples.Forexample,inmodelslikeDeepSeek-R1,theLLMactsasitsown
judge,refiningitsdecisionsthroughinternalassessments.Thisself-generatedfeedbackloophelps
themodelimprovewithoutneedingexternalverification.ByintegratingLLM-as-a-Judgewithin
suchfeedback-richframeworks,modelsgaintheabilitytonotonlyevaluateexternalcontentbut
alsoto introspectandevolvetheir ownreasoning processes.This representsa significantstep
towardbuildingAIsystemsthatarecapableofLLMoptimizationandself-improvementovertime.
7.1.3 Self-EvolvingJudges. Along-termvisionistoenableLLM-as-a-Judgesystemstopossess
self-calibrationandself-correctionabilities.Thiswouldinvolveevaluatorsthatcancontinuously
refinetheirbiasesbasedonexternalfeedback,thusevolvingintomorereliable"evaluationagents"
overtime.Thisdirectionalignswiththeemergingideaof"WorldModel-as-a-Judge,"asshown
in Figure 17 where an AI system can use its internal models of the world to make and justify
judgments.Forexample,ajudgecouldnotonlyevaluateaproposedsolutiontoaproblembutalso
simulatetheconsequencesofthatsolutioninahypotheticalenvironment,identifyingpotential
flawsbeforetheyoccur.Thisvisionimpliesthatfutureevaluatorswillnolongerbestatictools
butratherdynamic,evolvingintelligentsystemsthatcanadaptandimprovetheirownjudgment
capabilities,markingasignificantsteptowardsmoreautonomousandtrustworthyAI.
7.2 TheoreticallyGroundedEvaluation
CurrentresearchonthereliabilityofLLM-as-a-Judgeprimarilyreliesonempiricalbenchmarks,but
itlacksasolidtheoreticalfoundation.Asanextstep,itisimperativetomovebeyondtheseempirical
approachesandestablishamoreformaltheoreticalframeworkforevaluation.Futureworkshould
borrowideasfromfieldslikestatisticsandmeasurementtheorytointroduceformaldefinitions
of concepts like consistency and robustness. For instance, researchers could adapt established
metricssuchasCohen’sKappaorKrippendorff’sAlphatoquantifytheinter-raterreliabilityof
differentLLMjudges.Suchaframeworkwouldallowustosystematicallycharacterizeandimprove
thereliabilityoftheseevaluators,movingthefieldfromatrial-and-errorapproachtoonethatis
scientificallygroundedandallowsforverifiable,reproducibleresults.
7.3 MoreReliableLLM-as-a-Judge
As highlighted in our Formulation (§ 2) and Strategy (§ 3), LLMs are probabilistic models that
requireextensiveresearchandoptimizationtoenhancetheirreliabilityasjudges.Althoughcurrent
methodshaveimprovedthereliabilityofLLM-as-a-Judge,manychallenges,includingadaptability
androbustness,remainunresolved.Toenableprobabilisticmodelstodeliverevaluationsclosely
alignedwithreal-worldscenarios,futureresearchshouldprioritizerefiningandimplementingLLM-
as-a-Judgeacrosstheevaluationpipeline.Thereisconsiderablepotentialforimprovingreliability
in various aspects, including in-context learning, model selection, post-processing techniques,
and the overall evaluation framework for LLM-as-a-Judge. These efforts should prioritize not
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
onlyenhancingthereliabilityofassessmentsbutalsodevelopingmethodologiestosystematically
evaluate and validate the robustness of these assessments. Furthermore, the establishment of
comprehensiveevaluationbenchmarksandinterpretableanalyticaltoolswillbecrucialforassessing
and improving the reliability of LLM evaluators. Finally, the uncertain and evolving nature of
robustness risks underscores the necessity of proactive mitigation strategies. These strategies
should include the development of adversarial training techniques tailored to judgment tasks,
theintegrationofrobustuncertaintyquantificationmethods,andtheimplementationofhuman-
in-the-loopsystemstooverseecriticaldecisions.Byaddressingthesechallenges,wecanbuild
moreresilientanddependablesystemscapableofmaintaininghighlevelsofreliabilityevenunder
adversarialconditions.
7.4 MLLM-as-a-Judge
AIsystemsareevolvingintohighlyversatileandmultifunctionalentities[27].Traditionally,spe-
cializedmodelswererequiredfordistinctlanguageprocessingtasks,suchassentimentanalysis,
syntacticparsing,anddialoguemodeling.However,largelanguagemodels(LLMs)havedemon-
stratedcompetenceacrossthesetasksusingasinglesetofweights[134].Similarly,advancements
arebeingmadetowardunifiedsystemscapableofprocessingmultipledatamodalities.Instead
of employing distinct architectures for processing text, audio, and images, recent models like
GPT-4o[107],Gemini[40],andLLaVA[90]integratethesecapabilitieswithinasingleframework.
Thesedevelopmentshighlightagrowingtrendtowardunificationinthestructureandfunctionality
ofAIsystems,whichextendstotheemergingparadigmofLLM-as-a-Judge.
Currently,MLLM-as-a-Judgeframeworks[17]areemergingforevaluatingmodels.However,re-
searchexploringhowMLLM-as-a-Judgecouldbeappliedtotheevaluationofdataoragentsremains
limited.Beyondmodelevaluation,MLLM-as-a-Judge,muchlikeLLM-as-a-Judge,isenvisionedto
havethecapabilitytoassessorannotatedata,functionasaRewardModel,orserveasaVerifier
withinintermediatereasoningprocesses.TheseexpandedroleswouldallowMLLM-as-a-Judgeto
contributemorebroadlytotheAIpipeline.
Thefutureofevaluationliesindevelopingrobustmulti-modalevaluatorscapableofreasoning
andassessingcomplexcontentspanningtext,audio,images,andvideo.Whilecurrentmulti-modal
LLMsexhibitpromisingcapabilities,theyoftenlackthereasoningdepthandreliabilityoftheir
text-basedcounterparts.Futureresearchmustaddresstheselimitations,withafocusonenhancing
reasoningcapabilities,improvingreliability,andenablingseamlessintegrationacrossmodalities.A
practicalmulti-modalevaluatorhasthepotentialtonotonlyadvanceAIresearchbutalsoenable
new applications in areas such as multi-modal content moderation and automated knowledge
extraction.
7.5 AdvancingEvaluationBenchmarks
Thedevelopmentofmorecomprehensiveandrigorousbenchmarksiscriticalforadvancingthe
reliabilityandapplicabilityofLLM-as-a-Judgesystems.Thiseffortmustproceedontwodistinct
butinterconnectedfronts:establishingaframeworktoevaluatethejudgeitselfandexpandingthe
scopeofwhatthejudgecanevaluate.
EvaluationoftheEvaluator(Meta-Evaluation). Acriticalfuturedirectionisthedevelopment
ofsystematicmeta-evaluationframeworksdesignedspecificallytotestthereliability,fairness,and
consistencyofLLMjudges.Unlikeexistingbenchmarksthatevaluateamodel’sperformanceona
task,thesenewframeworkswouldfocusontheevaluatoritself.Forexample,ameta-evaluation
benchmarkcouldincludeacarefullyconstructedsetofpromptswithknownadversarialqualities,
suchassubtlewordsubstitutionsorparaphrasing,totestajudge’srobustnesstoinputperturbations.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
Furthermore,theseframeworksmustbecapableofassessingthejudge’sstabilityovertimeand
acrossdifferentmodelversions,therebytrackingandmitigatingissueslike"evaluationdrift."This
typeofframeworkwouldbemodel-agnostic,capableofnotonlyquantifyingperformancebutalso
providingabasisforexplainingajudge’sbehavior,whichinturnfostersgreatertransparencyand
trustinthesystem.
ExpandingBenchmarkScope. Whilemeta-evaluationensurestheintegrityofthejudge,we
mustalsocontinuetodevelopmorecomprehensiveanddiversebenchmarkstopushtheboundaries
ofwhatLLM-as-a-Judgecanaccomplish.Futureeffortscouldfocusoncreatinghigh-quality,large-
scaledatasetsthatencompassawiderangeofscenarios,includingdomain-specificapplications,
multimodalcontent,andreal-worldcomplexities.Forinstance,anewbenchmarkcouldfeature
legaldocumentsandrequirethejudgetoevaluatethelogicalsoundnessofalegalargument,or
includeacombinationofimagesandtext,requiringthejudgetoidentifyinconsistenciesbetween
them.Thesebenchmarksshouldalsointegratemoredetailedandfine-grainedevaluationmetrics
thatgobeyondsimplescores.ByestablishingrigorousstandardsanddatasetsakintoImageNetin
scaleandimpact,theLLM-as-a-Judgefieldcanachievedeeperinsightsintomodelperformance
andacceleratethedevelopmentofmorecapableandreliableevaluationmethodologies.
7.6 LLM-as-a-JudgeforDataAnnotation
Incontrast,LLM-as-a-judgeisageneraltechniquewhereyouuseLLMtoapproximatehuman
labeling.WhenyouaskanLLMtoassessqualitieslike"faithfulnesstosource,""correctness,"or
"helpfulness,"youdefinewhatthesetermsmeanintheevaluationpromptandrelyonthesemantic
relationshipstheLLMlearnedfromtrainingdata. Despiteitswideapplications,dataannotation
posessignificantchallengesforcurrentmachine-learningmodelsduetothecomplexity,subjectivity,
anddiversityofdata.Thisprocessrequiresdomainexpertiseandisresource-intensive,particularly
whenmanuallylabelinglargedatasets.AdvancedLLMssuchasGPT-4[107],Gemini[40],and
LLaMA-2[149]offerapromisingopportunitytorevolutionizedataannotation.LLMsserveasmore
thanjusttoolsbutplayacrucialroleinimprovingtheeffectivenessandprecisionofdataannotation.
Theirabilitytoautomateannotationtasks[208],ensureconsistencyacrosslargevolumesofdata,
andadaptthroughfine-tuningorpromptingforspecificdomains[101,131],significantlymitigates
thechallengesencounteredwithtraditionalannotationmethods,settinganewstandardforwhat
isachievableintherealmofNLP.
Whetherinthefieldofscientificresearchorindustry,weareallstillsufferingfrominsufficient
target data and domain-specific data, or situations where the data quality is not high enough.
AssumingthatLLM-as-a-judgecanachievestableperformanceandbefairandreliable,wecan
useLLMtoannotatedatainscenarioswheredataisinsufficienttoexpandthedata.Inscenarios
withlowdataquality,wecanassessthedataqualitythroughLLM,andlabelthequalitytagsto
achievethegoalofselectinghigh-qualitydata.Currently,wehavenotbeenabletoexperimentally
relysolelyonLLMforareliableevaluationofvariousscenariosofdata;mostofthetime,westill
relyonhumanannotationtoensureprofessionalismandreliability.LLM-as-a-judgeoftenneedsto
learnfromhumanannotationsinordertoperformcertainlabelingtasks.
7.7 LLM-as-a-JudgeforScaling
TheparadigmofLLM-as-a-JudgeispoisedtobecomeacoremechanismforscalingAIdevelopment,
particularly in an era where models are increasingly trained through interactive and iterative
feedbackloops.Atitsmostfundamentallevel,thisinvolvesscalingdataannotation.Traditional
humanlabelingisamajorbottleneck,asitisbothcostlyandslow.LLM-as-a-Judgeoffersapath
torapidlygeneratemassive,high-qualitydatasetsthatwouldbeotherwiseimpossibletoobtain.
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
Forinstance,itcanbeusedtogeneratepreferencelabelsforRLHFatascalethatisprohibitive
forhumanannotators,thusfuelingthedevelopmentofmoresophisticatedmodels.Thejudgecan
alsobedeployedinsemi-automatedworkflowswhereitprovidesinitialannotationsthatarethen
quicklyverifiedbyhumans,significantlyboostingthroughputandefficiency.Beyondstaticdata
creation,thejudgecanscaletheentiremodeloptimizationprocessbyactingasanautomatedcritic
orrewardmodel.Inmulti-agentsystems,anLLMjudgecanevaluatethequalityofinter-agent
communicationandcollaborationinrealtime,andinoptimizationpipelines,itcanprovidenuanced,
dynamicfeedbacktoguidemodelfine-tuningandenhancereasoningchains,thusservingasa
scalablealternativetotraditional,fixedmetrics.
7.8 LLM-as-a-JudgeforEmbodiedIntelligence
WhileLLM-as-a-Judgehasprimarilyfocusedonevaluatingdigitaloutputsliketextandimages,
its application can be extended to the domain of embodied intelligence. This presents a novel
and complex challenge: judging the actions and behaviors of agents in physical or simulated
environments.Unlikeevaluatingatextresponse,judginganembodiedagentrequiresassessing
asequenceofactions,theirspatiotemporalrelationships,andtheiralignmentwithahigh-level
goal,whichnecessitatesadeepunderstandingofphysicsandcauseandeffect.Forinstance,an
LLMjudgecouldevaluatearobot’sperformanceinacomplextasklikepreparingameal.Thejudge
wouldneedtoassessnotonlyifthefinalproductiscorrect,butalsoiftherobot’smovementswere
efficient,safe,andfollowedalogicalsequence,suchascorrectlyaligningacupwithadispenserto
avoidspillage.Similarly,invirtualenvironmentsorgaming,anLLMjudgecouldassessanagent’s
strategicability,navigationskills,oritscapacitytosolvepuzzlesinahuman-likemanner.This
judgewouldactasacrucialfeedbackmechanism,providinghigh-dimensional,naturallanguage
feedbacktoguidetheembodiedagent’slearningprocess.Thisrichfeedback,farmoreinformative
thanasimplescalarrewardsignal,couldacceleratelearningandleadtomoregeneralizableand
human-alignedintelligentsystems.
7.9 LLM-as-a-JudgeforLLMOptimization
LLM-as-a-JudgeshowssubstantialpromiseforadvancingLLMoptimization.Recentstudies[226]
havebegunincorporatingLLM-as-a-Judgeintomulti-agentframeworkstoguideinter-agentinterac-
tions,therebyimprovingoveralldecision-makingefficiencyandquality.Inaddition,LLM-as-a-Judge
hasbeenemployedinReinforcedFine-Tuning(ReFT)pipelines[150],functioningasacrucialscor-
ingmoduleforevaluatingthereasoningprocessesofmodels.Byflexiblyadaptingtodiversecontent
formatsanddomains,LLM-as-a-Judgeoffersarobustandefficientevaluationmechanismfora
widerangeofoptimizationtasks.
Despitetheseencouragingdevelopments,currentresearcheffortsarestillintheirinfancy.Future
workshouldfocusonbroadeningtheapplicationdomainsandstrategiesforimplementingLLM-
as-a-Judge,especiallyincomplex,multi-modalscenarios.Furthermore,asystematicassessment
ofitsreliabilityandgeneralizationcapabilitieswillbecriticalforfullyrealizingthepotentialof
LLM-as-a-Judgeinenhancingmodelperformanceandrobustness.
7.10 Domain-SpecificReliableApplications
Thereliabilityrequirementsforevaluationdiffersignificantlyacrossdomains.Futureworkshould
focusondevelopingcustomizedLLM-as-a-Judgesystemstailoredforspecificapplicationscenarios,
suchasmedicaldiagnosis,legaladjudication,educationalassessment,andscientificpeerreview.
Thisrequiresmorethanjustadjustingpromptsorfine-tuningstrategies.Forinstance,ajudge
designedforlegalcasesmustbetrainedtoprioritizestrictadherencetolegalprecedentsandstatutes,
ensuringitsjudgmentsaredefensibleandauditable.Similarly,ajudgeformedicaldiagnosismust
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
berigorouslytestedonitsabilitytounderstandclinicalguidelinesandinterpretmedicaljargon
correctly.Thisdemandsaspecializeddesignconcerningevaluationstandards,biascontrol,and
socialresponsibilitytomeettheuniqueneedsofeachfieldandearnthetrustofdomainexperts.
8 CONCLUSION
LLM-as-a-Judgehasemergedasapromisingparadigmforautomatedevaluation,offeringscalability
andadaptabilitythatsurpasstraditionalexpert-drivenormetric-basedmethods.Byleveraging
thereasoningcapabilitiesoflargelanguagemodels,thisframeworkexcelsintaskssuchastext
qualityassessment,modelevaluation,andautomateddataannotation.Itisparticularlyvaluablefor
large-scale,efficient,andadaptableevaluation.Itsabilitytoprocessdiversecontentformatsand
integratedomain-specificknowledgemakesitparticularlywell-suitedforapplicationsineducation,
peerreview,anddecision-makingsystems.
Despite these strengths, several challenges must be addressed to fully realize its potential.
Ensuringreliabilityremainsakeyissue,becauseprobabilisticoutputscanintroduceinconsistencies,
overconfidence,andbiasesinheritedfromtrainingdata.AlthoughtechniquesRLHFhaveimproved
alignment with human judgment, they do not eliminate all sources of subjectivity. Moreover,
ensuringrobustnessisanothercriticalconcern.LLM-as-a-Judgecanbesusceptibletoadversarial
promptmanipulationandcontextualframingbiases,potentiallycausingunintendedorunreliable
evaluations.Finally,generalizationacrossdomainsandmodalitiesremainsasignificanthurdle,as
currentmodelsstrugglewithevaluatingmulti-modalinputs,reasoningoverstructureddata,and
adaptingtodomain-specificevaluationstandards.
Toaddressthesechallenges,thispaperhasofferedacomprehensiveandprincipledroadmap.
First,atthedefinitionallevel,wehaveprovidedbothformalandinformaldefinitionsofLLM-as-a-
Judge,therebyestablishingtheconceptualboundariesofthisparadigm.Critically,weintroduced
acontextualizeddefinitionofreliabilitythataccountsforinputvariability,modelcharacteristics,
and contextual dependencies, providing a foundational framework for designing trustworthy
systems.Second,attheframeworklevel,wehavebroughtstructuretothefragmentedliterature
byorganizingexistingworkaroundfourfoundationalquestions:WhatisLLM-as-a-Judge?How
touseit?Howtoimproveit?andHowtoevaluateit?Thissynthesisnotonlyunifiesascattered
bodyofresearchbutalsoidentifiescriticalgapsandopportunitiesforfutureexploration.Third,at
theempiricallevel,wehaveperformedcomparativeanalysesofexistingapproachesand,more
importantly,proposedanovelmeta-evaluationbenchmarktailoredtoassessthejudgeitself.This
empirical contribution facilitates systematic performance assessments, revealing crucial trade-
offs—such as robustness versus sensitivity—and providing actionable insights for constructing
methodologically rigorous and practically deployable evaluation frameworks. Finally, at the
perspectivelevel,wehavepresentedacomprehensiveanalysisthatintegratestheapplications,
challenges,andfuturedirectionsofthisparadigm.WehaveshownthatLLM-as-a-Judgecanserveas
anintegralcomponentinhigh-stakesdomains,fromfinancetolaw,byidentifyingunique,domain-
specific reliability requirements. Our forward-looking agenda, which emphasizes theoretically
grounded methodologies, systematic benchmarks for meta-evaluation, and hybrid human–AI
frameworks, aims to guide the community toward LLM-as-a-Judge systems that are not only
technicallyrobustbutalsoepistemicallysound,sociallytrustworthy,andbroadlyapplicablein
criticalsectors.
Ultimately,LLM-as-a-Judgeispoisedtobecomeanintegralcomponentofnext-generationevalu-
ationsystems,augmentinghumanexpertiseratherthanreplacingit.Byaddressingthechallenges
ofreliability,robustness,andgeneralization,wecancreatemoretrustworthy,adaptive,andcompre-
hensiveevaluators,pavingthewayfortheiradoptionacrossscientificresearch,education,industry,
andbeyond.
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
REFERENCES
[1] AyushAgrawal,MiracSuzgun,LesterMackey,andAdamTaumanKalai.2023.DoLanguageModelsKnowWhen
They’reHallucinatingReferences?arXivpreprintarXiv:2305.18248(2023).
[2] ChenxinAn,ShansanGong,MingZhong,XingjianZhao,MukaiLi,JunZhang,LingpengKong,andXipengQiu.
2023.L-eval:Institutingstandardizedevaluationforlongcontextlanguagemodels.arXivpreprintarXiv:2307.11088
(2023).
[3] MaksymAndriushchenko,AlexandraSouly,MateuszDziemian,DerekDuenas,MaxwellLin,JustinWang,Dan
Hendrycks,AndyZou,ZicoKolter,MattFredrikson,etal.2024.AgentHarm:ABenchmarkforMeasuringHarmfulness
ofLLMAgents.ArXivpreprintabs/2410.09024(2024). https://arxiv.org/abs/2410.09024
[4] ZacharyAnkner,MansheejPaul,BrandonCui,JonathanDChang,andPrithvirajAmmanabrolu.2024.Critique-out-
loudrewardmodels.arXivpreprintarXiv:2408.11791(2024).
[5] GolnooshBabaeiandPaoloGiudici.2024.GPTclassifications,withapplicationtocreditlending.MachineLearning
withApplications16(2024),100534.
[6] SherBadshahandHassanSajjad.2024. Reference-GuidedVerdict:LLMs-as-JudgesinAutomaticEvaluationof
Free-FormText.ArXivpreprintabs/2408.09235(2024). https://arxiv.org/abs/2408.09235
[7] YushiBai,ShangqingTu,JiajieZhang,HaoPeng,XiaozhiWang,XinLv,ShulinCao,JiazhengXu,LeiHou,Yuxiao
Dong,etal.2024.LongBenchv2:TowardsDeeperUnderstandingandReasoningonRealisticLong-contextMultitasks.
arXivpreprintarXiv:2412.15204(2024).
[8] YushiBai,JiahaoYing,YixinCao,XinLv,YuzeHe,XiaozhiWang,JifanYu,KaishengZeng,YijiaXiao,HaozheLyu,
JiayinZhang,JuanziLi,andLeiHou.2023.BenchmarkingFoundationModelswithLanguage-Model-as-an-Examiner.
InAdvancesinNeuralInformationProcessingSystems36:AnnualConferenceonNeuralInformationProcessing
Systems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,AliceOh,TristanNaumann,Amir
Globerson,KateSaenko,MoritzHardt,andSergeyLevine(Eds.). http://papers.nips.cc/paper_files/paper/2023/hash/
f64e55d03e2fe61aa4114e49cb654acb-Abstract-Datasets_and_Benchmarks.html
[9] Sergio Bermejo. 2024. Enhancing Annotated Bibliography Generation with LLM Ensembles. arXiv preprint
arXiv:2412.20864(2024).
[10] MaciejBesta,NilsBlach,AlesKubicek,RobertGerstenberger,MichalPodstawski,LukasGianinazzi,JoannaGajda,
TomaszLehmann,HubertNiewiadomski,PiotrNyczyk,andTorstenHoefler.2024. GraphofThoughts:Solving
ElaborateProblemswithLargeLanguageModels.InThirty-EighthAAAIConferenceonArtificialIntelligence,
AAAI2024,Thirty-SixthConferenceonInnovativeApplicationsofArtificialIntelligence,IAAI2024,Fourteenth
SymposiumonEducationalAdvancesinArtificialIntelligence,EAAI2014,February20-27,2024,Vancouver,Canada,
MichaelJ.Wooldridge,JenniferG.Dy,andSriraamNatarajan(Eds.).AAAIPress,17682–17690.doi:10.1609/AAAI.
V38I16.29720
[11] LucaBeurer-Kellner,MarcFischer,andMartinVechev.2024. GuidingLLMstherightway:fast,non-invasive
constrainedgeneration.InProceedingsofthe41stInternationalConferenceonMachineLearning(ICML’24,Vol.235).
JMLR.org,Vienna,Austria,3658–3673.
[12] NathanBrakeandThomasSchaaf.2024.ComparingTwoModelDesignsforClinicalNoteGeneration:IsanLLMa
UsefulEvaluatorofConsistency?FindingsoftheACL(2024).
[13] MeniBrief,OdedOvadia,GilShenderovitz,NogaBenYoash,RachelLemberg,andEitamSheetrit.2024.MixingIt
Up:TheCocktailEffectofMulti-TaskFine-TuningonLLMPerformance–ACaseStudyinFinance.ArXivpreprint
abs/2410.01109(2024). https://arxiv.org/abs/2410.01109
[14] TomB.Brown,BenjaminMann,NickRyder,MelanieSubbiah,JaredKaplan,PrafullaDhariwal,ArvindNeelakantan,
PranavShyam,GirishSastry,AmandaAskell,SandhiniAgarwal,ArielHerbert-Voss,GretchenKrueger,TomHenighan,
RewonChild,AdityaRamesh,DanielM.Ziegler,JeffreyWu,ClemensWinter,ChristopherHesse,MarkChen,Eric
Sigler,MateuszLitwin,ScottGray,BenjaminChess,JackClark,ChristopherBerner,SamMcCandlish,AlecRadford,
IlyaSutskever,andDarioAmodei.2020.LanguageModelsareFew-ShotLearners.InAdvancesinNeuralInformation
ProcessingSystems33:AnnualConferenceonNeuralInformationProcessingSystems2020,NeurIPS2020,December
6-12,2020,virtual,HugoLarochelle,Marc’AurelioRanzato,RaiaHadsell,Maria-FlorinaBalcan,andHsuan-TienLin
(Eds.). https://proceedings.neurips.cc/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html
[15] Chi-MinChan,WeizeChen,YushengSu,JianxuanYu,WeiXue,ShanghangZhang,JieFu,andZhiyuanLiu.2023.Chat-
Eval:TowardsBetterLLM-basedEvaluatorsthroughMulti-AgentDebate.InTheTwelfthInternationalConference
onLearningRepresentations.
[16] DavidChan,SuzannePetryk,JosephGonzalez,TrevorDarrell,andJohnCanny.2023. CLAIR:EvaluatingImage
CaptionswithLargeLanguageModels.InProceedingsofthe2023ConferenceonEmpiricalMethodsinNatural
LanguageProcessing,HoudaBouamor,JuanPino,andKalikaBali(Eds.).AssociationforComputationalLinguistics,
Singapore,13638–13646.doi:10.18653/v1/2023.emnlp-main.841
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
[17] DongpingChen,RuoxiChen,ShilinZhang,YaochenWang,YinuoLiu,HuichiZhou,QihuiZhang,YaoWan,PanZhou,
andLichaoSun.2024.MLLM-as-a-Judge:AssessingMultimodalLLM-as-a-JudgewithVision-LanguageBenchmark.
InForty-firstInternationalConferenceonMachineLearning. https://openreview.net/forum?id=dbFEFHAD79
[18] DaoyuanChen,YilunHuang,ZhijianMa,HesenChen,XuchenPan,CeGe,DaweiGao,YuexiangXie,ZhaoyangLiu,
JinyangGao,etal.2024.Data-juicer:Aone-stopdataprocessingsystemforlargelanguagemodels.InCompanionof
the2024InternationalConferenceonManagementofData.120–134.
[19] GuimingHardyChen,ShunianChen,ZicheLiu,FengJiang,andBenyouWang.2024.Humansorllmsasthejudge?a
studyonjudgementbiases.ArXivpreprintabs/2402.10669(2024). https://arxiv.org/abs/2402.10669
[20] KaiChen,YanzeLi,WenhuaZhang,YanxinLiu,PengxiangLi,RuiyuanGao,LanqingHong,MengTian,XinhaiZhao,
ZhenguoLi,etal.2024.Automatedevaluationoflargevision-languagemodelsonself-drivingcornercases.ArXiv
preprintabs/2404.10595(2024). https://arxiv.org/abs/2404.10595
[21] QinyuanCheng,TianxiangSun,WenweiZhang,SiyinWang,XiangyangLiu,MozhiZhang,JunliangHe,Mianqiu
Huang,ZhangyueYin,KaiChen,etal.2023. Evaluatinghallucinationsinchineselargelanguagemodels. ArXiv
preprintabs/2310.03368(2023). https://arxiv.org/abs/2310.03368
[22] InyoungCheong,KingXia,KJKevinFeng,QuanZeChen,andAmyXZhang.2024.(A)IAmNotaLawyer,But...:
EngagingLegalExpertstowardsResponsibleLLMPoliciesforLegalAdvice.InThe2024ACMConferenceonFairness,
Accountability,andTransparency.2454–2469.
[23] AntoniaCreswell,MurrayShanahan,andIrinaHiggins.2023.Selection-Inference:ExploitingLargeLanguageModels
forInterpretableLogicalReasoning.InTheEleventhInternationalConferenceonLearningRepresentations,ICLR
2023,Kigali,Rwanda,May1-5,2023.OpenReview.net. https://openreview.net/pdf?id=3Pf3Wg6o-A4
[24] ChenhangCui,YiyangZhou,XinyuYang,ShirleyWu,LinjunZhang,JamesZou,andHuaxiuYao.2023. Holistic
analysisofhallucinationingpt-4v(ision):Biasandinterferencechallenges.ArXivpreprintabs/2311.03287(2023).
https://arxiv.org/abs/2311.03287
[25] SunhaoDai,ChenXu,ShichengXu,LiangPang,ZhenhuaDong,andJunXu.2024.UnifyingBiasandUnfairness
inInformationRetrieval:ASurveyofChallengesandOpportunitieswithLargeLanguageModels.arXivpreprint
arXiv:2404.11457(2024).
[26] SunhaoDai,YuqiZhou,LiangPang,WeihaoLiu,XiaolinHu,YongLiu,XiaoZhang,GangWang,andJunXu.2024.
NeuralRetrieversareBiasedTowardsLLM-GeneratedContent.InProceedingsofthe30thACMSIGKDDConference
onKnowledgeDiscoveryandDataMining(Barcelona,Spain)(KDD’24).AssociationforComputingMachinery,New
York,NY,USA,526–537. doi:10.1145/3637528.3671882
[27] MRSBDATA.2024.Multimodalartificialintelligencefoundationmodels:Unleashingthepowerofremotesensing
bigdatainearthobservation.Innovation2,1(2024),100055.
[28] HanzeDong,WeiXiong,DeepanshuGoyal,YihanZhang,WinnieChow,RuiPan,ShizheDiao,JipengZhang,Kashun
Shum,andTongZhang.2023.RAFT:RewardrAnkedFineTuningforGenerativeFoundationModelAlignment.arXiv
preprintarXiv:2304.06767(2023). https://arxiv.org/abs/2304.06767
[29] YixinDong,CharlieF.Ruan,YaxingCai,RuihangLai,ZiyiXu,YilongZhao,andTianqiChen.2024. XGrammar:
FlexibleandEfficientStructuredGenerationEngineforLargeLanguageModels. doi:10.48550/arXiv.2411.15100
arXiv:2411.15100[cs].
[30] YijiangRiverDong,TianchengHu,andNigelCollier.2024. CanLLMbeaPersonalizedJudge? arXivpreprint
arXiv:2406.11657(2024).
[31] ZhengxiaoDu,YujieQian,XiaoLiu,MingDing,JiezhongQiu,ZhilinYang,andJieTang.2022.GLM:GeneralLanguage
ModelPretrainingwithAutoregressiveBlankInfilling.InProceedingsofthe60thAnnualMeetingoftheAssociation
forComputationalLinguistics(Volume1:LongPapers),SmarandaMuresan,PreslavNakov,andAlineVillavicencio
(Eds.).AssociationforComputationalLinguistics,Dublin,Ireland,320–335.doi:10.18653/v1/2022.acl-long.26
[32] YannDubois,ChenXuechenLi,RohanTaori,TianyiZhang,IshaanGulrajani,JimmyBa,CarlosGuestrin,Percy
Liang,andTatsunoriB.Hashimoto.2023.AlpacaFarm:ASimulationFrameworkforMethodsthatLearnfromHuman
Feedback.InAdvancesinNeuralInformationProcessingSystems36:AnnualConferenceonNeuralInformation
ProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,AliceOh,TristanNaumann,
AmirGloberson,KateSaenko,MoritzHardt,andSergeyLevine(Eds.). http://papers.nips.cc/paper_files/paper/2023/
hash/5fc47800ee5b30b8777fdd30abcaaf3b-Abstract-Conference.html
[33] JinlanFu,See-KiongNg,ZhengbaoJiang,andPengfeiLiu.2024.GPTScore:EvaluateasYouDesire.InProceedings
ofthe2024ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:Human
LanguageTechnologies(Volume1:LongPapers),KevinDuh,HelenaGomez,andStevenBethard(Eds.).Association
forComputationalLinguistics,MexicoCity,Mexico,6556–6576. https://aclanthology.org/2024.naacl-long.365
[34] IsabelOGallegos,RyanARossi,JoeBarrow,MdMehrabTanjim,SungchulKim,FranckDernoncourt,TongYu,Ruiyi
Zhang,andNesreenKAhmed.2024.Biasandfairnessinlargelanguagemodels:Asurvey.ComputationalLinguistics
(2024),1–79.
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
[35] IsabelOGallegos,RyanARossi,JoeBarrow,MdMehrabTanjim,SungchulKim,FranckDernoncourt,TongYu,Ruiyi
Zhang,andNesreenKAhmed.2024.Biasandfairnessinlargelanguagemodels:Asurvey.ComputationalLinguistics
50,3(2024),1097–1179.
[36] ChangGao,HaiyunJiang,DengCai,ShumingShi,andWaiLam.2023.Strategyllm:Largelanguagemodelsasstrategy
generators,executors,optimizers,andevaluatorsforproblemsolving.arXivpreprintarXiv:2311.08803(2023).
[37] LeoGao,JohnSchulman,andJacobHilton.2023.Scalinglawsforrewardmodeloveroptimization.InInternational
ConferenceonMachineLearning.PMLR,10835–10866.
[38] MingqiGao,JieRuan,RenliangSun,XunjianYin,ShipingYang,andXiaojunWan.2023.Human-likesummarization
evaluationwithchatgpt.ArXivpreprintabs/2304.02554(2023). https://arxiv.org/abs/2304.02554
[39] ZorikGekhman,JonathanHerzig,RoeeAharoni,ChenElkind,andIdanSzpektor.2023.TrueTeacher:LearningFactual
ConsistencyEvaluationwithLargeLanguageModels.InProceedingsofthe2023ConferenceonEmpiricalMethods
inNaturalLanguageProcessing,HoudaBouamor,JuanPino,andKalikaBali(Eds.).AssociationforComputational
Linguistics,Singapore,2053–2070.doi:10.18653/v1/2023.emnlp-main.127
[40] Google.2023.Gemini:afamilyofhighlycapablemultimodalmodels.ArXivpreprintabs/2312.11805(2023). https:
//arxiv.org/abs/2312.11805
[41] NeelGuha,JulianNyarko,DanielE.Ho,ChristopherRé,AdamChilton,AdityaK,AlexChohlas-Wood,AustinPeters,
BrandonWaldon,DanielN.Rockmore,DiegoZambrano,DmitryTalisman,EnamHoque,FaizSurani,FrankFagan,
GalitSarfaty,GregoryM.Dickinson,HaggaiPorat,JasonHegland,JessicaWu,JoeNudell,JoelNiklaus,JohnJ.Nay,
JonathanH.Choi,KevinTobia,MargaretHagan,MeganMa,MichaelA.Livermore,NikonRasumov-Rahe,Nils
Holzenberger,NoamKolt,PeterHenderson,SeanRehaag,SharadGoel,ShangGao,SpencerWilliams,SunnyGandhi,
TomZur,VarunIyer,andZehuaLi.2023. LegalBench:ACollaborativelyBuiltBenchmarkforMeasuringLegal
ReasoninginLargeLanguageModels.InAdvancesinNeuralInformationProcessingSystems36:AnnualConference
onNeuralInformationProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,Alice
Oh,TristanNaumann,AmirGloberson,KateSaenko,MoritzHardt,andSergeyLevine(Eds.). http://papers.nips.cc/
paper_files/paper/2023/hash/89e44582fd28ddfea1ea4dcb0ebbf4b0-Abstract-Datasets_and_Benchmarks.html
[42] YufeiGuo,MuzheGuo,JuntaoSu,ZhouYang,MengqiuZhu,HongfeiLi,MengyangQiu,andShuoShuoLiu.2024.
Biasinlargelanguagemodels:Origin,evaluation,andmitigation.arXivpreprintarXiv:2411.10915(2024).
[43] ShiboHao,YiGu,HaodiMa,JoshuaHong,ZhenWang,DaisyWang,andZhitingHu.2023.ReasoningwithLanguage
ModelisPlanningwithWorldModel.InProceedingsofthe2023ConferenceonEmpiricalMethodsinNatural
LanguageProcessing,HoudaBouamor,JuanPino,andKalikaBali(Eds.).AssociationforComputationalLinguistics,
Singapore,8154–8173.doi:10.18653/v1/2023.emnlp-main.507
[44] HangfengHe,HongmingZhang,andDanRoth.2024.SocREval:LargeLanguageModelswiththeSocraticMethodfor
Reference-freeReasoningEvaluation.InFindingsoftheAssociationforComputationalLinguistics:NAACL2024,
KevinDuh,HelenaGomez,andStevenBethard(Eds.).AssociationforComputationalLinguistics,MexicoCity,Mexico,
2736–2764. https://aclanthology.org/2024.findings-naacl.175
[45] ShijunHe,FanYang,Jian-pingZuo,andZe-minLin.2023.ChatGPTforscientificpaperwriting—promisesandperils.
TheInnovation4,6(2023).
[46] PedramHosseini,JessicaM.Sin,BingRen,BrycetonG.Thomas,ElnazNouri,AliFarahanchi,andSaeedHassanpour.
2024.ABenchmarkforLong-FormMedicalQuestionAnswering.InProceedingsofEMNLP.
[47] XinyuHu,MingqiGao,SenHu,YangZhang,YichengChen,TengXu,andXiaojunWan.2024. AreLLM-based
EvaluatorsConfusingNLGQualityCriteria?.InProceedingsofthe62ndAnnualMeetingoftheAssociationfor
ComputationalLinguistics(Volume1:LongPapers).9530–9570. https://aclanthology.org/2024.acl-long.516
[48] HuiHuang,YanchengHe,HongliZhou,RuiZhang,WeiLiu,WeixunWang,WenboSu,BoZheng,andJiahengLiu.
2025.Think-j:Learningtothinkforgenerativellm-as-a-judge.arXivpreprintarXiv:2505.14268(2025).
[49] HuiHuang,YingqiQu,JingLiu,MuyunYang,andTiejunZhao.2024. Anempiricalstudyofllm-as-a-judgefor
llmevaluation:Fine-tunedjudgemodelsaretask-specificclassifiers.ArXivpreprintabs/2403.02839(2024). https:
//arxiv.org/abs/2403.02839
[50] JieHuangandKevinChen-ChuanChang.2023.TowardsReasoninginLargeLanguageModels:ASurvey.InFindings
oftheAssociationforComputationalLinguistics:ACL2023,AnnaRogers,JordanBoyd-Graber,andNaoakiOkazaki
(Eds.).AssociationforComputationalLinguistics,Toronto,Canada,1049–1065.doi:10.18653/v1/2023.findings-acl.67
[51] Jen-tseHuang,WenxuanWang,EricJohnLi,ManHoLam,ShujieRen,YouliangYuan,WenxiangJiao,ZhaopengTu,
andMichaelLyu.2023.Onthehumanityofconversationalai:Evaluatingthepsychologicalportrayalofllms.InThe
TwelfthInternationalConferenceonLearningRepresentations. https://openreview.net/forum?id=H3UayAQWoE
[52] NeelJain,AviSchwarzschild,YuxinWen,GowthamiSomepalli,JohnKirchenbauer,Ping-yehChiang,MicahGoldblum,
AniruddhaSaha,JonasGeiping,andTomGoldstein.2023.Baselinedefensesforadversarialattacksagainstaligned
languagemodels.ArXivpreprintabs/2309.00614(2023). https://arxiv.org/abs/2309.00614
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
[53] MinbyulJeong,JiwoongSohn,MujeenSung,andJaewooKang.2024.Improvingmedicalreasoningthroughretrieval
andself-reflectionwithretrieval-augmentedlargelanguagemodels.Bioinformatics40,Supplement_1(2024),i119–
i129.
[54] BowenJiang,YangxinyuXie,XiaomengWang,WeijieJSu,CamilloJoseTaylor,andTanwiMallick.2024.Multi-modal
andmulti-agentsystemsmeetrationality:Asurvey.InICML2024WorkshoponLLMsandCognition.
[55] TheodoreT.Jiang,LiFang,andKaiWang.2023.Deciphering“thelanguageofnature”:Atransformer-basedlanguage
modelfordeleteriousmutationsinproteins.TheInnovation4,5(2023),100487. doi:10.1016/j.xinn.2023.100487
[56] JaylenJones,LingboMo,EricFosler-Lussier,andHuanSun.2024.AMulti-AspectFrameworkforCounterNarrative
EvaluationusingLargeLanguageModels.InProceedingsofthe2024ConferenceoftheNorthAmericanChapter
oftheAssociationforComputationalLinguistics:HumanLanguageTechnologies(Volume2:ShortPapers),Kevin
Duh,HelenaGomez,andStevenBethard(Eds.).AssociationforComputationalLinguistics,MexicoCity,Mexico,
147–168. https://aclanthology.org/2024.naacl-short.14
[57] JaehunJung,FaezeBrahman,andYejinChoi.2024. TrustorEscalate:LLMJudgeswithProvableGuaranteesfor
HumanAgreement.arXivpreprintarXiv:2407.18370(2024).
[58] ImmanuelKant.1781.CritiqueofPureReason(a/bed.).Macmillan,London. Akademie-Ausgabe,Vol.3,A132/B171.
[59] ImmanuelKant.1790.CritiqueofJudgment.HackettPublishingCompany,Indianapolis. Akademie-Ausgabe,Vol.5,
5:179.
[60] AkiraKawabataandSakuSugawara.2024. Rationale-AwareAnswerVerificationbyPairwiseSelf-Evaluation.In
Proceedingsofthe2024ConferenceonEmpiricalMethodsinNaturalLanguageProcessing.16178–16196.
[61] PeiKe,BosiWen,AndrewFeng,XiaoLiu,XuanyuLei,JialeCheng,ShengyuanWang,AohanZeng,YuxiaoDong,
HongningWang,etal.2024. CritiqueLLM:TowardsanInformativeCritiqueGenerationModelforEvaluationof
LargeLanguageModelGeneration.InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputational
Linguistics(Volume1:LongPapers).13034–13054. https://aclanthology.org/2024.acl-long.704
[62] MuhammadUzairKhattak,HanoonaRasheed,MuhammadMaaz,SalmanKhan,andFahadShahbazKhan.2023.
Maple:Multi-modalpromptlearning.InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPattern
Recognition.19113–19122.
[63] SeungoneKim,JaminShin,YejinCho,JoelJang,ShayneLongpre,HwaranLee,SangdooYun,SeongjinShin,Sungdong
Kim,JamesThorne,etal.2023.Prometheus:InducingFine-grainedEvaluationCapabilityinLanguageModels.ArXiv
preprintabs/2310.08491(2023). https://arxiv.org/abs/2310.08491
[64] PangWeiKoh,JialinZhang,JaneLee,andPercyLiang.2024.MedHELM:HolisticEvaluationofLanguageModels
forMedicalApplications.TechnicalReport.StanfordHuman-CenteredArtificialIntelligence.
[65] MahiKolla,SiddharthSalunkhe,EshwarChandrasekharan,andKoustuvSaha.2024.LLM-Mod:CanLargeLanguage
ModelsAssistContentModeration?.InExtendedAbstractsoftheCHIConferenceonHumanFactorsinComputing
Systems.1–8.
[66] RyanKoo,MinhwaLee,VipulRaheja,JongInnPark,ZaeMyungKim,andDongyeopKang.2023.Benchmarking
cognitivebiasesinlargelanguagemodelsasevaluators.ArXivpreprintabs/2309.17012(2023). https://arxiv.org/abs/
2309.17012
[67] FajriKoto.2024.CrackingtheCode:Multi-domainLLMEvaluationonReal-WorldProfessionalExamsinIndonesia.
ArXivpreprintabs/2409.08564(2024). https://arxiv.org/abs/2409.08564
[68] JackKrolik,HerpritMahal,FerozAhmad,GauravTrivedi,andBahadorSaket.2024. TowardsLeveragingLarge
LanguageModelsforAutomatedMedicalQuestion–AnswerEvaluation.arXivpreprintarXiv:2403.01892(2024).
[69] AbhishekKumar,SoniaHaiduc,ParthaPratimDas,andParthaPratimChakrabarti.2024. LLMsasEvaluators:A
NovelApproachtoEvaluateBugReportSummarization.ArXivpreprintabs/2409.00630(2024). https://arxiv.org/
abs/2409.00630
[70] AbhishekKumar,SarfarozYunusov,andAliEmami.2024. SubtleBiasesNeedSubtlerMeasures:DualMetrics
forEvaluatingRepresentativeandAffinityBiasinLargeLanguageModels. ArXivpreprintabs/2405.14555(2024).
https://arxiv.org/abs/2405.14555
[71] PreethiLahoti,NicholasBlumm,XiaoMa,RaghavendraKotikalapudi,SahityaPotluri,QijunTan,HansaSrinivasan,
BenPacker,AhmadBeirami,AlexBeutel,andJilinChen.2023.ImprovingDiversityofDemographicRepresentation
inLargeLanguageModelsviaCollective-CritiquesandSelf-Voting.InProceedingsofthe2023Conferenceon
EmpiricalMethodsinNaturalLanguageProcessing,HoudaBouamor,JuanPino,andKalikaBali(Eds.).Association
forComputationalLinguistics,Singapore,10383–10405.doi:10.18653/v1/2023.emnlp-main.643
[72] TianLan,WenweiZhang,ChenXu,HeyanHuang,DahuaLin,KaiChen,andXian-LingMao.[n.d.]. CriticEval:
EvaluatingLarge-scaleLanguageModelasCritic.InTheThirty-eighthAnnualConferenceonNeuralInformation
ProcessingSystems.
[73] DongryeolLee,YerinHwang,YongilKim,JoonsukPark,andKyominJung.2024. AreLLM-judgesrobusttoex-
pressionsofuncertainty?investigatingtheeffectofepistemicmarkersonLLM-basedevaluation. arXivpreprint
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
arXiv:2410.20774(2024).
[74] YebinLee,ImseongPark,andMyungjooKang.2024.FLEUR:AnExplainableReference-FreeEvaluationMetricfor
ImageCaptioningUsingaLargeMultimodalModel.InProceedingsofthe62ndAnnualMeetingoftheAssociation
forComputationalLinguistics.3732–3746. https://aclanthology.org/2024.acl-long.205
[75] AliceLiandLuanneSinnamon.2023.Examiningquerysentimentbiaseffectsonsearchresultsinlargelanguage
models.InTheSymposiumonFutureDirectionsinInformationAccess(FDIA)co-locatedwiththe2023European
SummerSchoolonInformationRetrieval(ESSIR).
[76] DaweiLi,ZhenTan,PeijiaQian,YifanLi,KumarSatvikChaudhary,LijieHu,andJiayiShen.2024.SMoA:Improving
Multi-agentLargeLanguageModelswithSparseMixture-of-Agents.ArXivpreprintabs/2411.03284(2024). https:
//arxiv.org/abs/2411.03284
[77] DaweiLi,ShuYang,ZhenTan,JaeYoungBaik,SunkwonYun,JosephLee,AaronChacko,BojianHou,DuyDuong-
Tran,YingDing,etal.2024. DALK:DynamicCo-AugmentationofLLMsandKGtoanswerAlzheimer’sDisease
QuestionswithScientificLiterature.ArXivpreprintabs/2405.04819(2024). https://arxiv.org/abs/2405.04819
[78] HaitaoLi,YouChen,QingyaoAi,YueyueWu,RuizheZhang,andYiqunLiu.2024. LexEval:AComprehensive
ChineseLegalBenchmarkforEvaluatingLargeLanguageModels. ArXivpreprintabs/2409.20288(2024). https:
//arxiv.org/abs/2409.20288
[79] JunlongLi,ShichaoSun,WeizheYuan,Run-ZeFan,HaiZhao,andPengfeiLiu.2023.Generativejudgeforevaluating
alignment.ArXivpreprintabs/2310.05470(2023). https://arxiv.org/abs/2310.05470
[80] Lijun Li, Bowen Dong, Ruohui Wang, Xuhao Hu, Wangmeng Zuo, Dahua Lin, Yu Qiao, and Jing Shao. 2024.
SALAD-Bench:AHierarchicalandComprehensiveSafetyBenchmarkforLargeLanguageModels.InFindingsofthe
AssociationforComputationalLinguisticsACL2024.3923–3954. https://aclanthology.org/2024.findings-acl.235
[81] XuechenLi,TianyiZhang,YannDubois,RohanTaori,IshaanGulrajani,CarlosGuestrin,PercyLiang,andTatsunoriB.
Hashimoto.2023.AlpacaEval:AnAutomaticEvaluatorofInstruction-followingModels.https://github.com/tatsu-
lab/alpaca_eval.
[82] YifanLi,YifanDu,KunZhou,JinpengWang,XinZhao,andJi-RongWen.2023.EvaluatingObjectHallucinationin
LargeVision-LanguageModels.InProceedingsofthe2023ConferenceonEmpiricalMethodsinNaturalLanguage
Processing,HoudaBouamor,JuanPino,andKalikaBali(Eds.).AssociationforComputationalLinguistics,Singapore,
292–305.doi:10.18653/v1/2023.emnlp-main.20
[83] TianLiang,ZhiweiHe,WenxiangJiao,XingWang,YanWang,RuiWang,YujiuYang,ZhaopengTu,andShuming
Shi.2023. Encouragingdivergentthinkinginlargelanguagemodelsthroughmulti-agentdebate. ArXivpreprint
abs/2305.19118(2023). https://arxiv.org/abs/2305.19118
[84] HunterLightman,VineetKosaraju,YuriBurda,HarrisonEdwards,BowenBaker,TeddyLee,JanLeike,JohnSchulman,
IlyaSutskever,andKarlCobbe.2023.Let’sverifystepbystep.InTheTwelfthInternationalConferenceonLearning
Representations.
[85] Chin-YewLin.2004.Rouge:Apackageforautomaticevaluationofsummaries.InTextsummarizationbranchesout.
74–81.
[86] Yen-TingLinandYun-NungChen.2023. LLM-Eval:UnifiedMulti-DimensionalAutomaticEvaluationforOpen-
DomainConversationswithLargeLanguageModels.InProceedingsofthe5thWorkshoponNLPforConversational
AI(NLP4ConvAI2023),Yun-NungChenandAbhinavRastogi(Eds.).AssociationforComputationalLinguistics,
Toronto,Canada,47–58.doi:10.18653/v1/2023.nlp4convai-1.5
[87] ZiLin,ZihanWang,YongqiTong,YangkunWang,YuxinGuo,YujiaWang,andJingboShang.2023. ToxicChat:
UnveilingHiddenChallengesofToxicityDetectioninReal-WorldUser-AIConversation.InFindingsoftheAssociation
forComputationalLinguistics:EMNLP2023,HoudaBouamor,JuanPino,andKalikaBali(Eds.).Associationfor
ComputationalLinguistics,Singapore,4694–4702.doi:10.18653/v1/2023.findings-emnlp.311
[88] ZhanLing,YunhaoFang,XuanlinLi,ZhiaoHuang,MinguLee,RolandMemisevic,andHaoSu.2024.Deductiveveri-
ficationofchain-of-thoughtreasoning.InProceedingsofthe37thInternationalConferenceonNeuralInformation
ProcessingSystems(NewOrleans,LA,USA)(NIPS’23).CurranAssociatesInc.,RedHook,NY,USA,Article1580,
27pages.
[89] ChengyuanLiu,FubangZhao,LizhiQing,YangyangKang,ChanglongSun,KunKuang,andFeiWu.2023. Goal-
OrientedPromptAttackandSafetyEvaluationforLLMs.arXive-prints(2023),arXiv–2309. https://arxiv.org/abs/
2309.11830
[90] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023. Visual Instruction Tuning. In Advances
in Neural Information Processing Systems 36: Annual Conference on Neural Information Processing Systems
2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,AliceOh,TristanNaumann,AmirGlober-
son,KateSaenko,MoritzHardt,andSergeyLevine(Eds.). http://papers.nips.cc/paper_files/paper/2023/hash/
6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
[91] HaoLiu,CarmeloSferrazza,andPieterAbbeel.2023. Languagesarerewards:Hindsightfinetuningusinghuman
feedback.ArXivpreprintabs/2302.02676(2023). https://arxiv.org/abs/2302.02676
[92] YuanLiu,YameiChen,andLengHan.2023.Bioinformatics:Advancingbiomedicaldiscoveryandinnovationinthe
eraofbigdataandartificialintelligence.TheInnovationMedicine1,1(2023),100012.
[93] YangLiu,DanIter,YichongXu,ShuohangWang,RuochenXu,andChenguangZhu.2023.G-Eval:NLGEvaluation
usingGpt-4withBetterHumanAlignment.InProceedingsofthe2023ConferenceonEmpiricalMethodsinNatural
LanguageProcessing,HoudaBouamor,JuanPino,andKalikaBali(Eds.).AssociationforComputationalLinguistics,
Singapore,2511–2522.doi:10.18653/v1/2023.emnlp-main.153
[94] YuxuanLiu,TianchiYang,ShaohanHuang,ZihanZhang,HaizhenHuang,FuruWei,WeiweiDeng,FengSun,andQi
Zhang.2024.HD-Eval:AligningLargeLanguageModelEvaluatorsThroughHierarchicalCriteriaDecomposition.In
Proceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers).
7641–7660. https://aclanthology.org/2024.acl-long.413
[95] YinhongLiu,HanZhou,ZhijiangGuo,EhsanShareghi,IvanVulic,AnnaKorhonen,andNigelCollier.2024.Aligning
withhumanjudgement:Theroleofpairwisepreferenceinlargelanguagemodelevaluators.InThe1stConference
onLanguageModeling.
[96] AdianLiusie,PotsaweeManakul,andMarkGales.2024.LLMComparativeAssessment:Zero-shotNLGEvaluation
throughPairwiseComparisonsusingLargeLanguageModels.InProceedingsofthe18thConferenceoftheEuropean
ChapteroftheAssociationforComputationalLinguistics(Volume1:LongPapers),YvetteGrahamandMatthew
Purver(Eds.).AssociationforComputationalLinguistics,St.Julian’s,Malta,139–151. https://aclanthology.org/2024.
eacl-long.8
[97] YuxuanLu,XiaoyiDing,LingfengWang,ZhengZhu,andJunxianHe.2023.MathVista:EvaluatingMathematical
ReasoninginVisualContexts.arXivpreprintarXiv:2308.14737(2023).
[98] HaipengLuo,QingfengSun,CanXu,PuZhao,JianguangLou,ChongyangTao,XiuboGeng,QingweiLin,Shifeng
Chen,andDongmeiZhang.2023.Wizardmath:Empoweringmathematicalreasoningforlargelanguagemodelsvia
reinforcedevol-instruct.ArXivpreprintabs/2308.09583(2023). https://arxiv.org/abs/2308.09583
[99] HaipengLuo,QingfengSun,CanXu,PuZhao,JianguangLou,ChongyangTao,XiuboGeng,QingweiLin,Shifeng
Chen,andDongmeiZhang.2023.WizardMath:EmpoweringMathematicalReasoningforLargeLanguageModels
viaReinforcedEvol-Instruct.arXivpreprintarXiv:2308.09583(2023).
[100] MingLuo,WenyuYang,LongBai,LinZhang,Jia-WeiHuang,YinhongCao,YuhuaXie,LipingTong,HaiboZhang,
LeiYu,etal.2024.Artificialintelligenceforlifesciences:Acomprehensiveguideandfuturetrends.TheInnovation
Life2,4(2024),100105–1.
[101] ShengjieMa,ChongChen,QiChu,andJiaxinMao.2024.LeveragingLargeLanguageModelsforRelevanceJudgments
inLegalCaseRetrieval.arXiv:2403.18405[cs.AI] https://arxiv.org/abs/2403.18405
[102] XueguangMa,XinyuZhang,RonakPradeep,andJimmyLin.2023.Zero-shotlistwisedocumentrerankingwitha
largelanguagemodel.ArXivpreprintabs/2305.02156(2023). https://arxiv.org/abs/2305.02156
[103] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha
Dziri,ShrimaiPrabhumoye,YimingYang,ShashankGupta,BodhisattwaPrasadMajumder,KatherineHermann,
SeanWelleck,AmirYazdanbakhsh,andPeterClark.2023. Self-Refine:IterativeRefinementwithSelf-Feedback.
InAdvancesinNeuralInformationProcessingSystems36:AnnualConferenceonNeuralInformationProcessing
Systems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,AliceOh,TristanNaumann,Amir
Globerson,KateSaenko,MoritzHardt,andSergeyLevine(Eds.). http://papers.nips.cc/paper_files/paper/2023/hash/
91edff07232fb1b55a505a9e9f6c0ff3-Abstract-Conference.html
[104] SewonMin,KalpeshKrishna,XinxiLyu,MikeLewis,Wen-tauYih,PangKoh,MohitIyyer,LukeZettlemoyer,and
HannanehHajishirzi.2023. FActScore:Fine-grainedAtomicEvaluationofFactualPrecisioninLongFormText
Generation.InProceedingsofthe2023ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,Houda
Bouamor,JuanPino,andKalikaBali(Eds.).AssociationforComputationalLinguistics,Singapore,12076–12100.
doi:10.18653/v1/2023.emnlp-main.741
[105] HadiMohammadi,AnastasiaGiachanou,andAyoubBagheri.2025.EvalMORAAL:InterpretableChain-of-Thought
andLLM-as-JudgeEvaluationforMoralAlignmentinLargeLanguageModels. arXivpreprintarXiv:2510.05942
(2025).
[106] BehradMoniri,HamedHassani,andEdgarDobriban.2024.EvaluatingthePerformanceofLargeLanguageModels
viaDebates.ArXivpreprintabs/2406.11044(2024). https://arxiv.org/abs/2406.11044
[107] OpenAI.2023.GPT-4TechnicalReport.arXiv:2303.08774[cs.CL]
[108] LongOuyang,JeffreyWu,XuJiang,DiogoAlmeida,CarrollL.Wainwright,PamelaMishkin,ChongZhang,Sandhini
Agarwal,KatarinaSlama,AlexRay,JohnSchulman,JacobHilton,FraserKelton,LukeMiller,MaddieSimens,
AmandaAskell,PeterWelinder,PaulF.Christiano,JanLeike,andRyanLowe.2022. Traininglanguagemodels
tofollowinstructionswithhumanfeedback.InAdvancesinNeuralInformationProcessingSystems35:Annual
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
ConferenceonNeuralInformationProcessingSystems2022,NeurIPS2022,NewOrleans,LA,USA,November28
-December9,2022,SanmiKoyejo,S.Mohamed,A.Agarwal,DanielleBelgrave,K.Cho,andA.Oh(Eds.). http:
//papers.nips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html
[109] KishorePapineni,SalimRoukos,ToddWard,andWei-JingZhu.2002.Bleu:amethodforautomaticevaluationof
machinetranslation.InProceedingsofthe40thannualmeetingoftheAssociationforComputationalLinguistics.
311–318.
[110] JunsooPark,SeungyeonJwa,MeiyingRen,DaeyoungKim,andSanghyukChoi.2024.Offsetbias:Leveragingdebiased
datafortuningevaluators.ArXivpreprintabs/2407.06551(2024). https://arxiv.org/abs/2407.06551
[111] PranavPutta,EdmundMills,NamanGarg,SumeetMotwani,ChelseaFinn,DivyanshGarg,andRafaelRafailov.2024.
Agentq:Advancedreasoningandlearningforautonomousaiagents.arXivpreprintarXiv:2408.07199(2024).
[112] ZhenQin,RolfJagerman,KaiHui,HongleiZhuang,JunruWu,LeYan,JiamingShen,TianqiLiu,JialuLiu,Donald
Metzler,XuanhuiWang,andMichaelBendersky.2024. LargeLanguageModelsareEffectiveTextRankerswith
PairwiseRankingPrompting.InFindingsoftheAssociationforComputationalLinguistics:NAACL2024,KevinDuh,
HelenaGomez,andStevenBethard(Eds.).AssociationforComputationalLinguistics,MexicoCity,Mexico,1504–1518.
https://aclanthology.org/2024.findings-naacl.97
[113] YouzhiQu,PenghuiDu,WenxinChe,ChenWei,ChiZhang,WanliOuyang,YataoBian,FeiyangXu,BinHu,KaiDu,
etal.2024.Promotinginteractionsbetweencognitivescienceandlargelanguagemodels.TheInnovation5,2(2024).
[114] ZackaryRackauckas,ArthurCâmara,andJakubZavrel.2024. Evaluatingrag-fusionwithragelo:anautomated
elo-basedframework.ArXivpreprintabs/2406.14783(2024). https://arxiv.org/abs/2406.14783
[115] RafaelRafailov,ArchitSharma,EricMitchell,ChristopherDManning,StefanoErmon,andChelseaFinn.2024.Direct
preferenceoptimization:Yourlanguagemodelissecretlyarewardmodel.AdvancesinNeuralInformationProcessing
Systems36(2024).
[116] VyasRaina,AdianLiusie,andMarkGales.2024. IsLLM-as-a-JudgeRobust?InvestigatingUniversalAdversarial
AttacksonZero-shotLLMAssessment.ArXivpreprintabs/2402.14016(2024). https://arxiv.org/abs/2402.14016
[117] RaviRaju,SwayambhooJain,BoLi,JonathanLi,andUrmishThakkar.2024.Constructingdomain-specificevaluation
setsforllm-as-a-judge.ArXivpreprintabs/2408.08808(2024). https://arxiv.org/abs/2408.08808
[118] RajkumarRamamurthy,PrithvirajAmmanabrolu,KiantéBrantley,JackHessel,RafetSifa,ChristianBauckhage,
HannanehHajishirzi,andYejinChoi.2023. IsReinforcementLearning(Not)forNaturalLanguageProcessing:
Benchmarks,Baselines,andBuildingBlocksforNaturalLanguagePolicyOptimization.InTheEleventhInternational
ConferenceonLearningRepresentations,ICLR2023,Kigali,Rwanda,May1-5,2023.OpenReview.net. https://
openreview.net/pdf?id=8aHzds2uUyB
[119] CheolRyu,SeolhwaLee,SubeenPang,ChanyeolChoi,HojunChoi,MyeonggeeMin,andJy-YongSohn.2023.
Retrieval-based Evaluation for LLMs: A Case Study in Korean Legal QA. In Proceedings of the Natural Legal
Language Processing Workshop 2023, Daniel Preot,iuc-Pietro, Catalina Goanta, Ilias Chalkidis, Leslie Barrett,
GerasimosSpanakis,andNikolaosAletras(Eds.).AssociationforComputationalLinguistics,Singapore,132–137.
doi:10.18653/v1/2023.nllp-1.13
[120] SwarnadeepSaha,OmerLevy,AsliCelikyilmaz,MohitBansal,JasonWeston,andXianLi.2024. Branch-Solve-
MergeImprovesLargeLanguageModelEvaluationandGeneration.InProceedingsofthe2024Conferenceofthe
NorthAmericanChapteroftheAssociationforComputationalLinguistics:HumanLanguageTechnologies(Volume
1:LongPapers),KevinDuh,HelenaGomez,andStevenBethard(Eds.).AssociationforComputationalLinguistics,
MexicoCity,Mexico,8352–8370. https://aclanthology.org/2024.naacl-long.462
[121] KeitaSaito,AkifumiWachi,KokiWataoka,andYouheiAkimoto.2023.Verbositybiasinpreferencelabelingbylarge
languagemodels.ArXivpreprintabs/2310.10076(2023). https://arxiv.org/abs/2310.10076
[122] NatalieSchluter.2017. ThelimitsofautomaticsummarisationaccordingtoROUGE.InProceedingsofthe15th
ConferenceoftheEuropeanChapteroftheAssociationforComputationalLinguistics:Volume2,ShortPapers,
MirellaLapata,PhilBlunsom,andAlexanderKoller(Eds.).AssociationforComputationalLinguistics,Valencia,Spain,
41–45. https://aclanthology.org/E17-2007
[123] JohnSchulman,FilipWolski,PrafullaDhariwal,AlecRadford,andOlegKlimov.2017.Proximalpolicyoptimization
algorithms.ArXivpreprintabs/1707.06347(2017). https://arxiv.org/abs/1707.06347
[124] AmrithSetlur,ChiragNagpal,AdamFisch,XinyangGeng,JacobEisenstein,RishabhAgarwal,AlekhAgarwal,
JonathanBerant,andAviralKumar.2024. RewardingProgress:ScalingAutomatedProcessVerifiersforLLM
Reasoning.arXivpreprintarXiv:2410.08146(2024).
[125] HaoSha,YaoMu,YuxuanJiang,LiChen,ChenfengXu,PingLuo,ShengboEbenLi,MasayoshiTomizuka,WeiZhan,
andMingyuDing.2023.Languagempc:Largelanguagemodelsasdecisionmakersforautonomousdriving.ArXiv
preprintabs/2310.03026(2023). https://arxiv.org/abs/2310.03026
[126] LinShi,WeichengMa,andSoroushVosoughi.2024.JudgingtheJudges:ASystematicInvestigationofPositionBiasin
PairwiseComparativeAssessmentsbyLLMs.ArXivpreprintabs/2406.07791(2024). https://arxiv.org/abs/2406.07791
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
[127] YiShi.2024.DrugdevelopmentintheAIera:AlphaFold3iscoming!TheInnovation5,5(2024).
[128] NoahShinn,FedericoCassano,AshwinGopinath,KarthikNarasimhan,andShunyuYao.2023. Reflexion:lan-
guageagentswithverbalreinforcementlearning.InAdvancesinNeuralInformationProcessingSystems36:Annual
ConferenceonNeuralInformationProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10
-16,2023,AliceOh,TristanNaumann,AmirGloberson,KateSaenko,MoritzHardt,andSergeyLevine(Eds.).
http://papers.nips.cc/paper_files/paper/2023/hash/1b44b878bb782e6954cd888628510e90-Abstract-Conference.html
[129] CharlieSnell,JaehoonLee,KelvinXu,andAviralKumar.2024.Scalingllmtest-timecomputeoptimallycanbemore
effectivethanscalingmodelparameters.arXivpreprintarXiv:2408.03314(2024).
[130] GuijinSon,HyunwooKo,HoyoungLee,YewonKim,andSeunghyeokHong.2024.Llm-as-a-judge&rewardmodel:
Whattheycanandcannotdo.ArXivpreprintabs/2409.11239(2024). https://arxiv.org/abs/2409.11239
[131] FeifanSong,BowenYu,MinghaoLi,HaiyangYu,FeiHuang,YongbinLi,andHoufengWang.2024.PreferenceRank-
ingOptimizationforHumanAlignment.InThirty-EighthAAAIConferenceonArtificialIntelligence,AAAI2024,
Thirty-SixthConferenceonInnovativeApplicationsofArtificialIntelligence,IAAI2024,FourteenthSymposium
onEducationalAdvancesinArtificialIntelligence,EAAI2014,February20-27,2024,Vancouver,Canada,MichaelJ.
Wooldridge,JenniferG.Dy,andSriraamNatarajan(Eds.).AAAIPress,18990–18998.doi:10.1609/AAAI.V38I17.29865
[132] YishenSong,QiantaZhu,HuaiboWang,andQinhuaZheng.2024.AutomatedEssayScoringandRevisingBasedon
Open-SourceLargeLanguageModels.IEEETransactionsonLearningTechnologies(2024).
[133] AndreaSottana,BinLiang,KaiZou,andZhengYuan.2023.EvaluationMetricsintheEraofGPT-4:ReliablyEvaluating
LargeLanguageModelsonSequencetoSequenceTasks.InProceedingsofthe2023ConferenceonEmpiricalMethods
inNaturalLanguageProcessing,HoudaBouamor,JuanPino,andKalikaBali(Eds.).AssociationforComputational
Linguistics,Singapore,8776–8788.doi:10.18653/v1/2023.emnlp-main.543
[134] AarohiSrivastava,AbhinavRastogi,AbhishekRao,AbuAwalMdShoeb,AbubakarAbid,AdamFisch,AdamR
Brown,AdamSantoro,AdityaGupta,AdriàGarriga-Alonso,etal.2022.Beyondtheimitationgame:Quantifyingand
extrapolatingthecapabilitiesoflanguagemodels.ArXivpreprintabs/2206.04615(2022). https://arxiv.org/abs/2206.
04615
[135] JiashuoSun,ChengjinXu,LumingyuanTang,SaizhuoWang,ChenLin,YeyunGong,Heung-YeungShum,andJian
Guo.2023.Think-on-graph:Deepandresponsiblereasoningoflargelanguagemodelwithknowledgegraph.ArXiv
preprintabs/2307.07697(2023). https://arxiv.org/abs/2307.07697
[136] ZhiqingSun,ShengShen,ShengcaoCao,HaotianLiu,ChunyuanLi,YikangShen,ChuangGan,Liang-YanGui,
Yu-XiongWang,YimingYang,etal.2023.Aligninglargemultimodalmodelswithfactuallyaugmentedrlhf.arXiv
preprintarXiv:2309.14525(2023). https://arxiv.org/abs/2309.14525
[137] ZhiqingSun,YikangShen,QinhongZhou,HongxinZhang,ZhenfangChen,DavidD.Cox,YimingYang,andChuang
Gan.2023.Principle-DrivenSelf-AlignmentofLanguageModelsfromScratchwithMinimalHumanSupervision.
InAdvancesinNeuralInformationProcessingSystems36:AnnualConferenceonNeuralInformationProcessing
Systems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,AliceOh,TristanNaumann,Amir
Globerson,KateSaenko,MoritzHardt,andSergeyLevine(Eds.). http://papers.nips.cc/paper_files/paper/2023/hash/
0764db1151b936aca59249e2c1386101-Abstract-Conference.html
[138] HexiangTan,FeiSun,WanliYang,YuanzhuoWang,QiCao,andXueqiCheng.2024.BlindedbyGeneratedContexts:
HowLanguageModelsMergeGeneratedandRetrievedContextsWhenKnowledgeConflicts?.InProceedings
ofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers),Lun-Wei
Ku,AndreMartins,andVivekSrikumar(Eds.).AssociationforComputationalLinguistics,Bangkok,Thailand.
doi:10.18653/v1/2024.acl-long.337
[139] SijunTan,SiyuanZhuang,KyleMontgomery,WilliamYTang,AlejandroCuadron,ChenguangWang,RalucaAda
Popa,andIonStoica.2024.Judgebench:Abenchmarkforevaluatingllm-basedjudges.arXivpreprintarXiv:2410.12784
(2024).
[140] QiaoyuTang,JiaweiChen,BowenYu,YaojieLu,ChengFu,HaiyangYu,HongyuLin,FeiHuang,BenHe,Xianpei
Han,etal.2024.Self-Retrieval:BuildinganInformationRetrievalSystemwithOneLargeLanguageModel.ArXiv
preprintabs/2403.00801(2024). https://arxiv.org/abs/2403.00801
[141] RaphaelTang,CrystinaZhang,XueguangMa,JimmyLin,andFerhanTure.2024.FoundintheMiddle:Permutation
Self-ConsistencyImprovesListwiseRankinginLargeLanguageModels.InProceedingsofthe2024Conferenceofthe
NorthAmericanChapteroftheAssociationforComputationalLinguistics:HumanLanguageTechnologies(Volume
1:LongPapers),KevinDuh,HelenaGomez,andStevenBethard(Eds.).AssociationforComputationalLinguistics,
MexicoCity,Mexico,2327–2340. https://aclanthology.org/2024.naacl-long.129
[142] Yi-DaTang,Er-DanDong,andWenGao.2024.LLMsinmedicine:Theneedforadvancedevaluationsystemsfor
disruptivetechnologies.TheInnovation5,3(2024).
[143] RohanTaori,IshaanGulrajani,TianyiZhang,YannDubois,XuechenLi,CarlosGuestrin,PercyLiang,andTatsunoriB.
Hashimoto.2023.StanfordAlpaca:AnInstruction-followingLLaMAmodel.https://github.com/tatsu-lab/stanford_
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
alpaca.
[144] AmanSinghThakur,KartikChoudhary,VenkatSrinikRamayapally,SankaranVaidyanathan,andDieuwkeHupkes.
2024.JudgingtheJudges:EvaluatingAlignmentandVulnerabilitiesinLLMs-as-Judges.ArXivpreprintabs/2406.12624
(2024). https://arxiv.org/abs/2406.12624
[145] YufeiTian,AbhilashaRavichander,LianhuiQin,RonanLeBras,RajaMarjieh,NanyunPeng,YejinChoi,Thomas
Griffiths,andFaezeBrahman.2024.MacGyver:AreLargeLanguageModelsCreativeProblemSolvers?.InProceedings
ofthe2024ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:Human
LanguageTechnologies(Volume1:LongPapers),KevinDuh,HelenaGomez,andStevenBethard(Eds.).Association
forComputationalLinguistics,MexicoCity,Mexico,5303–5324. https://aclanthology.org/2024.naacl-long.297
[146] YuxuanTong,XiwenZhang,RuiWang,RuidongWu,andJunxianHe.2024.DART-Math:Difficulty-AwareRejection
TuningforMathematicalProblem-Solving.InNeurIPS.
[147] HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,TimothéeLacroix,Baptiste
Rozière,NamanGoyal,EricHambro,FaisalAzhar,etal.2023.Llama:Openandefficientfoundationlanguagemodels.
ArXivpreprintabs/2302.13971(2023). https://arxiv.org/abs/2302.13971
[148] HugoTouvron,ThibautLavril,GautierIzacard,XavierMartinet,Marie-AnneLachaux,TimothéeLacroix,Baptiste
Rozière,NamanGoyal,EricHambro,FaisalAzhar,etal.2023.Vicuna:Openandefficientfoundationlanguagemodels.
ArXivpreprintabs/2302.13971(2023). https://arxiv.org/abs/2302.13971
[149] HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,YasmineBabaei,NikolayBashlykov,
SoumyaBatra,PrajjwalBhargava,ShrutiBhosale,etal.2023.Llama2:Openfoundationandfine-tunedchatmodels.
ArXivpreprintabs/2307.09288(2023). https://arxiv.org/abs/2307.09288
[150] LuongTrung,XinboZhang,ZhanmingJie,PengSun,XiaoranJin,andHangLi.2024.Reft:Reasoningwithreinforced
fine-tuning.InProceedingsofthe62ndAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
1:LongPapers).7601–7614.
[151] DaanVanVeen,AkshayKolluri,andetal.2024.CurrentandFutureStateofEvaluationofLargeLanguageModels
forClinicalSummarization.NatureMedicine(2024).
[152] BinjieWang,SteffiChern,EthanChern,andPengfeiLiu.2024.Halu-J:Critique-BasedHallucinationJudge.ArXiv
preprintabs/2407.12943(2024). https://arxiv.org/abs/2407.12943
[153] ChengruiWang,QingqingLong,XiaoMeng,XunxinCai,ChengjunWu,ZhenMeng,XuezhiWang,andYuanchun
Zhou.2024.BioRAG:ARAG-LLMFrameworkforBiologicalQuestionReasoning.ArXivpreprintabs/2408.01107
(2024). https://arxiv.org/abs/2408.01107
[154] JunyangWang,YiyangZhou,GuohaiXu,PengchengShi,ChenlinZhao,HaiyangXu,QinghaoYe,MingYan,JiZhang,
JihuaZhu,etal.2023. Evaluationandanalysisofhallucinationinlargevision-languagemodels. ArXivpreprint
abs/2308.15126(2023). https://arxiv.org/abs/2308.15126
[155] PeiyiWang,LeiLi,LiangChen,ZefanCai,DaweiZhu,BinghuaiLin,YunboCao,LingpengKong,QiLiu,TianyuLiu,
andZhifangSui.2024.LargeLanguageModelsarenotFairEvaluators.InProceedingsofthe62ndAnnualMeeting
oftheAssociationforComputationalLinguistics(Volume1:LongPapers).9440–9450.
[156] PeiyiWang,LeiLi,ZhihongShao,RuiXu,DamaiDai,YifeiLi,DeliChen,YuWu,andZhifangSui.2023. Math-
Shepherd:VerifyandReinforceLLMsStep-by-StepwithoutHumanAnnotations.arXivpreprintarXiv:2312.08935
(2023).
[157] SaizhuoWang,HangYuan,LionelM.Ni,andJianGuo.2024. QuantAgent:SeekingHolyGrailinTradingby
Self-ImprovingLargeLanguageModel.doi:10.48550/arXiv.2402.03755arXiv:2402.03755[cs].
[158] TianluWang,IliaKulikov,OlgaGolovneva,PingYu,WeizheYuan,JaneDwivedi-Yu,RichardYuanzhePang,Maryam
Fazel-Zarandi,JasonWeston,andXianLi.2024. Self-taughtevaluators. arXivpreprintarXiv:2408.02666(2024).
https://arxiv.org/abs/2408.02666
[159] TianluWang,PingYu,XiaoqingEllenTan,SeanO’Brien,RamakanthPasunuru,JaneDwivedi-Yu,OlgaGolovneva,
LukeZettlemoyer,MaryamFazel-Zarandi,andAsliCelikyilmaz.2023. Shepherd:ACriticforLanguageModel
Generation.ArXivpreprintabs/2308.04592(2023). https://arxiv.org/abs/2308.04592
[160] YizhongWang,YeganehKordi,SwaroopMishra,AlisaLiu,NoahA.Smith,DanielKhashabi,andHannanehHajishirzi.
2023.Self-Instruct:AligningLanguageModelswithSelf-GeneratedInstructions.InProceedingsofthe61stAnnual
MeetingoftheAssociationforComputationalLinguistics(Volume1:LongPapers),AnnaRogers,JordanBoyd-
Graber,andNaoakiOkazaki(Eds.).AssociationforComputationalLinguistics,Toronto,Canada,13484–13508.
doi:10.18653/v1/2023.acl-long.754
[161] YidongWang,YunzeSong,TingyuanZhu,XuanwangZhang,ZhuohaoYu,HaoChen,ChiyuSong,QiufengWang,
CunxiangWang,ZhenWu,etal.2025.TrustJudge:InconsistenciesofLLM-as-a-JudgeandHowtoAlleviateThem.
arXivpreprintarXiv:2509.21117(2025).
[162] YidongWang,ZhuohaoYu,ZhengranZeng,LinyiYang,CunxiangWang,HaoChen,ChaoyaJiang,RuiXie,Jindong
Wang,XingXie,etal.2023.PandaLM:AnAutomaticEvaluationBenchmarkforLLMInstructionTuningOptimization.
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
ArXivpreprintabs/2306.05087(2023). https://arxiv.org/abs/2306.05087
[163] YichengWang,JiayiYuan,Yu-NengChuang,ZhuoerWang,YingchiLiu,MarkCusick,ParamKulkarni,ZhengpingJi,
YasserIbrahim,andXiaHu.2024.DHPBenchmark:AreLLMsGoodNLGEvaluators?ArXivpreprintabs/2408.13704
(2024). https://arxiv.org/abs/2408.13704
[164] YileiWang,JiabaoZhao,DenizSOnes,LiangHe,andXinXu.2025.Evaluatingtheabilityoflargelanguagemodels
toemulatepersonality.Scientificreports15,1(2025),519.
[165] ZilongWang,ZifengWang,LongLe,HuaixiuStevenZheng,SwaroopMishra,VincentPerot,YuweiZhang,Anush
Mattapalli,AnkurTaly,JingboShang,etal.2024.Speculativerag:Enhancingretrievalaugmentedgenerationthrough
drafting.ArXivpreprintabs/2407.08223(2024). https://arxiv.org/abs/2407.08223
[166] ZhenyuWang,JinZhang,PeiHua,YuanzhengCui,ChunhuiLu,XiaojunWang,QiuwenChen,andPeterKrebs.2023.
Fillinginmissingpiecesintheco-developmentofartificialintelligenceandenvironmentalscience.TheInnovation
Geoscience1,1(2023),100007–14.
[167] JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,BrianIchter,FeiXia,EdH.Chi,QuocV.Le,andDenny
Zhou.2022. Chain-of-ThoughtPromptingElicitsReasoninginLargeLanguageModels.InAdvancesinNeural
InformationProcessingSystems35:AnnualConferenceonNeuralInformationProcessingSystems2022,NeurIPS
2022,NewOrleans,LA,USA,November28-December9,2022,SanmiKoyejo,S.Mohamed,A.Agarwal,DanielleBel-
grave,K.Cho,andA.Oh(Eds.). http://papers.nips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-
Abstract-Conference.html
[168] YixuanWeng,MinjunZhu,FeiXia,BinLi,ShizhuHe,ShengpingLiu,BinSun,KangLiu,andJunZhao.2023.
LargeLanguageModelsareBetterReasonerswithSelf-Verification.InFindingsoftheAssociationforComputational
Linguistics:EMNLP2023,HoudaBouamor,JuanPino,andKalikaBali(Eds.).AssociationforComputationalLinguistics,
Singapore,2550–2575.doi:10.18653/v1/2023.findings-emnlp.167
[169] NingWu,MingGong,LinjunShou,ShiningLiang,andDaxinJiang.2023. Largelanguagemodelsarediverse
role-playersforsummarizationevaluation.InCCFInternationalConferenceonNaturalLanguageProcessingand
ChineseComputing.Springer,695–707.
[170] YuhangWu,WenmengYu,YeanCheng,YanWang,XiaohanZhang,JiazhengXu,MingDing,andYuxiaoDong.
2024.AlignMMBench:EvaluatingChineseMultimodalAlignmentinLargeVision-LanguageModels.ArXivpreprint
abs/2406.09295(2024). https://arxiv.org/abs/2406.09295
[171] ZhengXia,LiQian,andHaoWang.2024.BeyondAccuracy:EvaluatingLogicalCoherenceofMathematicalReasoning
inLargeLanguageModels.arXivpreprintarXiv:2405.11234(2024).
[172] TinghaoXie,XiangyuQi,YiZeng,YangsiboHuang,UdariMadhushaniSehwag,KaixuanHuang,LuxiHe,BoyiWei,
DachengLi,YingSheng,etal.2024. Sorry-bench:Systematicallyevaluatinglargelanguagemodelsafetyrefusal
behaviors.ArXivpreprintabs/2406.14598(2024). https://arxiv.org/abs/2406.14598
[173] YiqingXie,WenxuanZhou,PradyotPrakash,DiJin,YuningMao,QuintinFettes,AryaTalebzadeh,SinongWang,
HanFang,CarolynRose,etal.2024.ImprovingModelFactualitywithFine-grainedCritique-basedEvaluator.arXiv
preprintarXiv:2410.18359(2024).
[174] TianyiXiong,XiyaoWang,DongGuo,QinghaoYe,HaoqiFan,QuanquanGu,HengHuang,andChunyuanLi.
2024. LLaVA-Critic:LearningtoEvaluateMultimodalModels. ArXivpreprintabs/2410.02712(2024). https:
//arxiv.org/abs/2410.02712
[175] RuoxiXu,HongyuLin,XianpeiHan,LeSun,andYingfeiSun.2024.AcademicallyintelligentLLMsarenotnecessarily
sociallyintelligent.ArXivpreprintabs/2403.06591(2024). https://arxiv.org/abs/2403.06591
[176] WendaXu,DanqingWang,LiangmingPan,ZhenqiaoSong,MarkusFreitag,WilliamWang,andLeiLi.2023. IN-
STRUCTSCORE:TowardsExplainableTextGenerationEvaluationwithAutomaticFeedback.InProceedingsofthe
2023ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,HoudaBouamor,JuanPino,andKalikaBali
(Eds.).AssociationforComputationalLinguistics,Singapore,5967–5994.doi:10.18653/v1/2023.emnlp-main.365
[177] YongjunXu,FeiWang,ZhulinAn,QiWang,andZhaoZhang.2023.Artificialintelligenceforscience—bridgingdata
towisdom.TheInnovation4,6(2023).
[178] YongjunXu,FeiWang,andTangtangZhang.2024.Artificialintelligenceisrestructuringanewworld.TheInnovation
5,6(2024).
[179] AnYang,BeichenZhang,BinyuanHui,BofeiGao,BowenYu,ChengpengLi,DayihengLiu,JianhongTu,JingrenZhou,
JunyangLin,KemingLu,MingfengXue,RunjiLin,TianyuLiu,XingzhangRen,andZhenruZhang.2024.Qwen2.5-
MathTechnicalReport:TowardMathematicalExpertModelviaSelf-Improvement.arXivpreprintarXiv:2409.12122
(2024).
[180] HuiYang,SifuYue,andYunzhongHe.2023. Auto-gptforonlinedecisionmaking:Benchmarksandadditional
opinions.ArXivpreprintabs/2306.02224(2023). https://arxiv.org/abs/2306.02224
[181] YuzheYang,YifeiZhang,YanHu,YilinGuo,RuoliGan,YueruHe,MingcongLei,XiaoZhang,HainingWang,Qianqian
Xie,etal.2024.UCFE:AUser-CentricFinancialExpertiseBenchmarkforLargeLanguageModels.ArXivpreprint
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
abs/2410.14059(2024). https://arxiv.org/abs/2410.14059
[182] ShunyuYao,DianYu,JeffreyZhao,IzhakShafran,TomGriffiths,YuanCao,andKarthikNarasimhan.2023.Treeof
Thoughts:DeliberateProblemSolvingwithLargeLanguageModels.InAdvancesinNeuralInformationProcessing
Systems36:AnnualConferenceonNeuralInformationProcessingSystems2023,NeurIPS2023,NewOrleans,LA,
USA,December10-16,2023,AliceOh,TristanNaumann,AmirGloberson,KateSaenko,MoritzHardt,andSergey
Levine(Eds.). http://papers.nips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-
Conference.html
[183] ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,KarthikR.Narasimhan,andYuanCao.2023. ReAct:
SynergizingReasoningandActinginLanguageModels.InTheEleventhInternationalConferenceonLearning
Representations,ICLR2023,Kigali,Rwanda,May1-5,2023.OpenReview.net. https://openreview.net/pdf?id=WE_
vluYUL-X
[184] ZonghaiYao,AdityaParashar,HuixueZhou,WonSeokJang,FeiyunOuyang,ZhichaoYang,andHongYu.2024.
MCQG-SRefine:MultipleChoiceQuestionGenerationandEvaluationwithIterativeSelf-Critique,Correction,and
ComparisonFeedback.arXivpreprintarXiv:2410.13191(2024).
[185] JiayiYe,YanboWang,YueHuang,DongpingChen,QihuiZhang,NunoMoniz,TianGao,WernerGeyer,ChaoHuang,
Pin-YuChen,etal.2024.JusticeorPrejudice?QuantifyingBiasesinLLM-as-a-Judge.ArXivpreprintabs/2410.02736
(2024). https://arxiv.org/abs/2410.02736
[186] SeonghyeonYe,YongraeJo,DoyoungKim,SungdongKim,HyeonbinHwang,andMinjoonSeo.2023.SelFee:Iterative
Self-RevisingLLMEmpoweredbySelf-FeedbackGeneration.Blogpost. https://kaistai.github.io/SelFee/
[187] SungwookYoon.2023.DesignandImplementationofanLLMsystemtoImproveResponseTimeforSMEsTechnology
CreditEvaluation.InternationalJournalofAdvancedSmartConvergence12,3(2023),51–60.
[188] JiachenYu,ShaoningSun,XiaohuiHu,JiaxuYan,KaidongYu,andXuelongLi.2025.Improvellm-as-a-judgeability
asageneralability.arXivpreprintarXiv:2502.11689(2025).
[189] QingchenYu,ZifanZheng,ShichaoSong,ZhiyuLi,FeiyuXiong,BoTang,andDingChen.2024.xFinder:Robustand
PinpointAnswerExtractionforLargeLanguageModels.arXivpreprintarXiv:2405.11874(2024).
[190] YangyangYu,ZhiyuanYao,HaohangLi,ZhiyangDeng,YupengCao,ZhiChen,JordanWSuchow,RongLiu,
ZhenyuCui,DenghuiZhang,etal.2024.FinCon:ASynthesizedLLMMulti-AgentSystemwithConceptualVerbal
ReinforcementforEnhancedFinancialDecisionMaking.ArXivpreprintabs/2407.06567(2024). https://arxiv.org/
abs/2407.06567
[191] JYuan,PBao,ZChen,MYuan,JZhao,JPan,YXie,YCao,YWang,ZWang,etal.2023.Advancedpromptingasa
catalyst:Empoweringlargelanguagemodelsinthemanagementofgastrointestinalcancers. TheInnovation521
(2023).
[192] WeizheYuan,RichardYuanzhePang,KyunghyunCho,SainbayarSukhbaatar,JingXu,andJasonWeston.2024.
Self-rewardinglanguagemodels.arXivpreprintarXiv:2401.10020(2024).
[193] ZhengYuan,HongyiYuan,ChuanqiTan,WeiWang,SongfangHuang,andFeiHuang.2023.Rrhf:Rankresponsesto
alignlanguagemodelswithhumanfeedbackwithouttears.ArXivpreprintabs/2304.05302(2023). https://arxiv.org/
abs/2304.05302
[194] KamerAliYukselandHassanSawaf.2024.AMulti-AIAgentSystemforAutonomousOptimizationofAgenticAI
SolutionsviaIterativeRefinementandLLM-DrivenFeedbackLoops.arXivpreprintarXiv:2412.17149(2024).
[195] ZhiyuanZeng,JiatongYu,TianyuGao,YuMeng,TanyaGoyal,andDanqiChen.2023.EvaluatingLargeLanguage
ModelsatEvaluatingInstructionFollowing. https://arxiv.org/abs/2310.07641
[196] BangZhang,RuotianMa,QingxuanJiang,PeisongWang,JiaqiChen,ZhengXie,XingyuChen,YueWang,Fanghua
Ye,JianLi,etal.2025. SentientAgentasaJudge:EvaluatingHigher-OrderSocialCognitioninLargeLanguage
Models.arXivpreprintarXiv:2505.02847(2025).
[197] BeichenZhang,KunZhou,XilinWei,XinZhao,JingSha,ShijinWang,andJi-RongWen.2024. Evaluatingand
improvingtool-augmentedcomputation-intensivemathreasoning. AdvancesinNeuralInformationProcessing
Systems36(2024).
[198] HengyuanZhang,YanruWu,DaweiLi,SakYang,RuiZhao,YongJiang,andFeiTan.2024. Balancingspecial-
ityandversatility:acoarsetofineframeworkforsupervisedfine-tuninglargelanguagemodel. arXivpreprint
arXiv:2404.10306(2024).
[199] HengranZhang,RuqingZhang,JiafengGuo,MaartendeRijke,YixingFan,andXueqiCheng.2024. AreLarge
LanguageModelsGoodatUtilityJudgments?.InProceedingsofthe47thInternationalACMSIGIRConferenceon
ResearchandDevelopmentinInformationRetrieval.1941–1951.
[200] JiaxingZhang,RuyiGan,JunjieWang,YuxiangZhang,LinZhang,PingYang,XinyuGao,ZiweiWu,XiaoqunDong,
JunqingHe,etal.2022.Fengshenbang1.0:Beingthefoundationofchinesecognitiveintelligence.ArXivpreprint
abs/2209.02970(2022). https://arxiv.org/abs/2209.02970
,Vol.1,No.1,Article.Publicationdate:October2025.

ASurveyonLLM-as-a-Judge
[201] LiangXuXuanweiZhangandKangkangZhao.2022.Chatyuan:Alargelanguagemodelfordialogueinchineseand
english.
[202] MiZhang,XudongPan,andMinYang.2023. Jade:Alinguistics-basedsafetyevaluationplatformforllm. ArXiv
preprintabs/2311.00286(2023). https://arxiv.org/abs/2311.00286
[203] QiyuanZhang,YufeiWang,YuxinJiang,LiangyouLi,ChuhanWu,YashengWang,XinJiang,LifengShang,Ruiming
Tang,FuyuanLyu,etal.2025.Crowdcomparativereasoning:Unlockingcomprehensiveevaluationsforllm-as-a-judge.
arXivpreprintarXiv:2502.12501(2025).
[204] RuizheZhang,HaitaoLi,YueyueWu,QingyaoAi,YiqunLiu,MinZhang,andShaopingMa.2024.EvaluationEthics
ofLLMsinLegalDomain.ArXivpreprintabs/2403.11152(2024). https://arxiv.org/abs/2403.11152
[205] TianjunZhang,FangchenLiu,JustinWong,PieterAbbeel,andJosephE.Gonzalez.2023.TheWisdomofHindsight
MakesLanguageModelsBetterInstructionFollowers.InInternationalConferenceonMachineLearning,ICML
2023,23-29July2023,Honolulu,Hawaii,USA(ProceedingsofMachineLearningResearch,Vol.202),AndreasKrause,
EmmaBrunskill,KyunghyunCho,BarbaraEngelhardt,SivanSabato,andJonathanScarlett(Eds.).PMLR,41414–41428.
https://proceedings.mlr.press/v202/zhang23ab.html
[206] WenjingZhang,YongfengLu,ChenyiSu,YiboWang,Yong-FeiWang,BoZhang,ChengJiang,KeyingGuo,and
ChuanXu.2023.Confinement-guidedultrasensitiveopticalassaywithartificialintelligencefordiseasediagnostics.
TheInnovationMedicine1,2(2023),100023–1.
[207] XinghuaZhang,BowenYu,HaiyangYu,YangyuLv,TingwenLiu,FeiHuang,HongboXu,andYongbinLi.2023.
Wideranddeeperllmnetworksarefairerllmevaluators.ArXivpreprintabs/2308.01862(2023). https://arxiv.org/
abs/2308.01862
[208] ZhuoshengZhang,AstonZhang,MuLi,andAlexSmola.2023.AutomaticChainofThoughtPromptinginLarge
LanguageModels.InTheEleventhInternationalConferenceonLearningRepresentations,ICLR2023,Kigali,Rwanda,
May1-5,2023.OpenReview.net. https://openreview.net/pdf?id=5NTt8GFjUHkr
[209] HuaqinZhao,ZhengliangLiu,ZihaoWu,YiweiLi,TianzeYang,PengShu,ShaochenXu,HaixingDai,LinZhao,
GengchenMai,etal.2024. Revolutionizingfinancewithllms:Anoverviewofapplicationsandinsights. ArXiv
preprintabs/2401.11641(2024). https://arxiv.org/abs/2401.11641
[210] TianjieZhao,ShengWang,ChaojunOuyang,MinChen,ChenyingLiu,JinZhang,LongYu,FeiWang,YongXie,Jun
Li,etal.[n.d.].Artificialintelligenceforgeoscience:Progress,challengesandperspectives.TheInnovation([n.d.]).
[211] YulaiZhao,HaolinLiu,DianYu,SYKung,HaitaoMi,andDongYu.2025.OneTokentoFoolLLM-as-a-Judge.arXiv
preprintarXiv:2507.08794(2025).
[212] YuweiZhao,ZiyangLuo,YuchenTian,HongzhanLin,WeixiangYan,AnnanLi,andJingMa.2024.CodeJudge-Eval:
CanLargeLanguageModelsbeGoodJudgesinCodeUnderstanding?arXivpreprintarXiv:2408.10718(2024).
[213] LianminZheng,Wei-LinChiang,YingSheng,SiyuanZhuang,ZhanghaoWu,YonghaoZhuang,ZiLin,Zhuohan
Li,DachengLi,EricP.Xing,HaoZhang,JosephE.Gonzalez,andIonStoica.2023. JudgingLLM-as-a-Judgewith
MT-BenchandChatbotArena.InAdvancesinNeuralInformationProcessingSystems36:AnnualConferenceon
NeuralInformationProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,Alice
Oh,TristanNaumann,AmirGloberson,KateSaenko,MoritzHardt,andSergeyLevine(Eds.). http://papers.nips.cc/
paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html
[214] LianminZheng,Wei-LinChiang,YingSheng,TianleLi,SiyuanZhuang,ZhanghaoWu,YonghaoZhuang,Zhuohan
Li,ZiLin,EricXing,etal.2023.Lmsys-chat-1m:Alarge-scalereal-worldllmconversationdataset.ArXivpreprint
abs/2309.11998(2023). https://arxiv.org/abs/2309.11998
[215] LianminZheng,LiangshengYin,ZhiqiangXie,ChuyueSun,JeffHuang,CodyHaoYu,ShiyiCao,ChristosKozyrakis,
IonStoica,JosephE.Gonzalez,ClarkBarrett,andYingSheng.2024. SGLang:EfficientExecutionofStructured
LanguageModelPrograms.doi:10.48550/arXiv.2312.07104arXiv:2312.07104[cs].
[216] XiaosenZheng,TianyuPang,ChaoDu,QianLiu,JingJiang,andMinLin.2024.Cheatingautomaticllmbenchmarks:
Nullmodelsachievehighwinrates.ArXivpreprintabs/2410.07137(2024). https://arxiv.org/abs/2410.07137
[217] JunZhong,JianxinShi,andLaufeyTAmundadottir.2023.Artificialintelligenceandimprovedearlydetectionfor
pancreaticcancer.TheInnovation4,4(2023).
[218] ChuntingZhou,PengfeiLiu,PuxinXu,SrinivasanIyer,JiaoSun,YuningMao,XuezheMa,AviaEfrat,PingYu,
LiliYu,SusanZhang,GargiGhosh,MikeLewis,LukeZettlemoyer,andOmerLevy.2023. LIMA:LessIsMorefor
Alignment.InAdvancesinNeuralInformationProcessingSystems36:AnnualConferenceonNeuralInformation
ProcessingSystems2023,NeurIPS2023,NewOrleans,LA,USA,December10-16,2023,AliceOh,TristanNaumann,
AmirGloberson,KateSaenko,MoritzHardt,andSergeyLevine(Eds.). http://papers.nips.cc/paper_files/paper/2023/
hash/ac662d74829e4407ce1d126477f4a03a-Abstract-Conference.html
[219] Hang-YuZhou,YalingLi,Jia-YingLi,JingMeng,andAipingWu.2024.Harnessingthepowerofartificialintelligenceto
combatinfectiousdiseases:Progress,challenges,andfutureoutlook.TheInnovationMedicine2,4(2024),100091–1.
,Vol.1,No.1,Article.Publicationdate:October2025.

J.Gu,X.Jiang,Z.Shi,J.Guo,etal.
[220] PeiZhou,JayPujara,XiangRen,XinyunChen,Heng-TzeCheng,QuocVLe,EdHChi,DennyZhou,SwaroopMishra,
andHuaixiuStevenZheng.2024.Self-discover:Largelanguagemodelsself-composereasoningstructures.ArXiv
preprintabs/2402.03620(2024). https://arxiv.org/abs/2402.03620
[221] XuhuiZhou,HaoZhu,LeenaMathur,RuohongZhang,HaofeiYu,ZhengyangQi,Louis-PhilippeMorency,Yonatan
Bisk,DanielFried,GrahamNeubig,etal.2023. Sotopia:Interactiveevaluationforsocialintelligenceinlanguage
agents.ArXivpreprintabs/2310.11667(2023). https://arxiv.org/abs/2310.11667
[222] LianghuiZhu,XinggangWang,andXinlongWang.2023.Judgelm:Fine-tunedlargelanguagemodelsarescalable
judges.ArXivpreprintabs/2310.17631(2023). https://arxiv.org/abs/2310.17631
[223] HongleiZhuang,ZhenQin,KaiHui,JunruWu,LeYan,XuanhuiWang,andMichaelBendersky.2024.BeyondYes
andNo:ImprovingZero-ShotLLMRankersviaScoringFine-GrainedRelevanceLabels.InProceedingsofthe2024
ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:HumanLanguage
Technologies(Volume2:ShortPapers),KevinDuh,HelenaGomez,andStevenBethard(Eds.).Associationfor
ComputationalLinguistics,MexicoCity,Mexico,358–370. https://aclanthology.org/2024.naacl-short.31
[224] ShengyaoZhuang,HongleiZhuang,BevanKoopman,andGuidoZuccon.2024.Asetwiseapproachforeffectiveand
highlyefficientzero-shotrankingwithlargelanguagemodels.InProceedingsofthe47thInternationalACMSIGIR
ConferenceonResearchandDevelopmentinInformationRetrieval.38–47.
[225] YuchenZhuang,XiangChen,TongYu,SaayanMitra,VictorBursztyn,RyanARossi,SomdebSarkhel,andChao
Zhang.2023.Toolchain*:Efficientactionspacenavigationinlargelanguagemodelswitha*search.ArXivpreprint
abs/2310.13227(2023). https://arxiv.org/abs/2310.13227
[226] MingchenZhuge,ChangshengZhao,DylanAshley,WenyiWang,DmitriiKhizbullin,YunyangXiong,ZechunLiu,
ErnieChang,RaghuramanKrishnamoorthi,YuandongTian,etal.2024. Agent-as-a-Judge:EvaluateAgentswith
Agents.ArXivpreprintabs/2410.10934(2024). https://arxiv.org/abs/2410.10934
,Vol.1,No.1,Article.Publicationdate:October2025.
