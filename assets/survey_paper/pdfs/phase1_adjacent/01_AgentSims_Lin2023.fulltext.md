Title: 01_AgentSims_Lin2023

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_adjacent/01_AgentSims_Lin2023.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:04+00:00
- page_count: 7
- status: ok
- text_char_count: 24235

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

AgentSims: An Open-Source Sandbox for Large Language Model
Evaluation
JiajuLin1,2,HaoranZhao1,3 ∗,AochiZhang1,YitingWu1,4,
HuqiuyuePing1,5,QinChen6
1PTAStudio
2 PennsylvaniaStateUniversity,3 BeihangUniversity,
4 SunYat-senUniversity,5ZhejiangUniversity,6EastChinaNormalUniversity
3zhaohaoran@buaa.edu.cn
2jjlin.unfake@gmail.com and 6qchen@cs.ecnu.edu.cn
Abstract diversespectrumofabilities,includingclose-book
question-answering (QA) based knowledge test-
With ChatGPT-like large language models
ing(Hendrycks et al., 2020; Huang et al., 2023),
(LLM) prevailing in the community, how to
human-centric standardized exams(Zhong et al.,
evaluatetheabilityofLLMsisanopenques-
2023), multi-turn dialogue(Lin and Chen, 2023),
tion. Existingevaluationmethodssufferfrom
reasoning(Liuetal.,2023a;benchauthors,2023)
followingshortcomings: (1)constrainedevalu-
ationabilities,(2)vulnerablebenchmarks,(3) andsafetyassessment(Sunetal.,2023).
unobjective metrics. We suggest that task- However, there are still many problems with
basedevaluation,whereLLMagentscomplete
thesenewbenchmarks. 1)Evaluatedabilitiesare
tasks in a simulated environment, is a one-
limited by the task formats. Since a majority of
for-allsolutiontosolveaboveproblems. We
these tasks adopt a single-turn QA format, they
presentAgentSims,aneasy-to-useinfrastruc-
are insufficient to comprehensively evaluate vari-
tureforresearchersfromalldisciplinestotest
the specific capacities they are interested in. ous aspects of LLMs’ capabilities. For instance,
Researcherscanbuildtheirevaluationtasksby they fail to assess the models’ proficiency in ad-
addingagentsandbuildingsonaninteractive hering to instructions in dialogue or mimicking
GUI or deploy and test new support mecha- human-likesocialinteractions. 2)Benchmarkscan
nisms,i.e. memory,planningandtool-usesys-
beeasilyhacked. Avoidingtheleakageoftestsetis
tems, by a few lines of codes. Our demo is
ofparamountimportancewhenevaluateamodel’s
availableathttps://agentsims.com.
ability. Nonetheless, considering the amount of
1 Introduction pretrainedknowledgeofLLM,ithasbecomemore
andmoreinevitabletoinadvertentlymixtestcases
LLMshaverevolutionizedNaturalLanguagePro- into the training set.(Gunasekar et al., 2023). 3)
cessing (NLP) and beyond. They demonstrate Foropen-endedQA,existingmetricsarenotobjec-
great potential in few-shot learning(Brown et al., tive. Previousmetricsforopen-endedQAinvolve
2020),codegeneration(Nijkampetal.,2023),rea- automaticmetrics,andhuman-ratingassubjective
soning(Yaoetal.,2023)andothertasks. Further- metrics(Zhouetal.,2023). IntheLLMera,textseg-
more, LLM powered autonomous agents(Weng, mentmatchingbasedmetricsbecomeout-of-date.
2023)arewidelyappliedinsolvingcomplexprob- Tomitigatethehigh-costlyissueofhuman-rating,
lems,likemultimodalgeneration(Shenetal.,2023), today’sresearchersemploywell-alignedLLMslike
softwaredeveloping(Qianetal.,2023)andsocial GPT4asautomaticraters. Nevertheless,themost
simulating(Parketal.,2023). significantproblemofthisapproachisthatitcan
Although LLMs have reformed the paradigm notevaluatesuperGPT4-levelmodels,andLLMs
of NLP, the problem of evaluation keeps haunt- are biased toward specific features (Wang et al.,
ing this field. Old benchmarks become out-of- 2023b).
date. Since LLMs achieve human-level Natural
Based on these observations, we suggest task-
LanguageUnderstanding(NLU)andNaturalLan-
based evaluation for LLM benchmarks. Specifi-
guageGeneration(NLG)abilities(OpenAI,2023).
cally,givenanartificialsocial-economicenviron-
Toaddressthepressingneedfornovelbenchmarks,
ment,LLM-drivenagentsshouldachievethepre-
the NLP community has introduced an array of
definedtaskgoalstoprovetheirabilities,justlike
freshevaluationtasksanddatasets,encompassinga
humansaccomplishinggoalsinrealworldorgames
∗∗Correspondingauthor. toshowtheircapacities. Task-basedevaluationis
1
3202
guA
8
]IA.sc[
1v62040.8032:viXra

a one-for-all solution for current issues: 1) Task- cooperationbetweendifferentfieldsandthefu-
basedevaluationcantestanLLM’soverallability. tureprosperityoftheLLMcommunity.
Thecomplexityofsocialsimulationandadaptation
2 RelatedWork
far exceeds simple QA and can formulate more
challengingtasksforLLMs. LLMagentsneedto
2.1 BenchmarksforLargeLanguageModels
beequippedwiththeabilityfromNLUtoTheory
ofMind(ToM)(PremackandWoodruff,1978). 2) The emergency of ChatGPT and other LLMs re-
Tasksolvingprocessesarelesslikelytobehacked. quires new benchmarks for effective evaluation.
Differentfromunchangedtestdatasetswhosefor- benchauthors(2023)isthemostacceptedbench-
matscanbeeasilymimickedandaddedtotraining mark to evaluate LLM’s general abilities. It con-
data. Tasksettingsarediversifiedandtheemergent tains more than 200 tasks, covering from child-
social behaviors and groups are less likely to be hood development, to social bias. Zhong et al.
describedandincludedintrainingcorpus. 3)Task (2023)collecttesttasksfromhuman-centricstan-
passingrateisanobjectivemetric. Comparedwith dardized exams like GRE and SAT. (Hendrycks
popular rating methods by ChatGPT, the passing et al., 2020; Huang et al., 2023) are benchmarks
ratedoesnotrelyonanyblack-boxratingprocess, focusingonmeasuringknowledgeacquiredinpre-
i.e. deepneuralnetworksorhumanbrains,thusit training. They covers subjects across STEM, the
isanobjectiveandfairmetricforthecomparison humanities, the social sciences. Lin and Chen
betweenLLMs. (2023) build a benchmark for LLMs’ multiturn
To all-around estimate LLMs’ capacities, we dialogueabilities. Everydialogueislimitedtotwo
hoperesearchersfromallfieldstakepartinthede- turnsforsimplicity. Sunetal.(2023)focusonmea-
velopmentofevaluationtasks. However,akeyob- surethesafetyofLLMs. Theycurateaadversarial
stacletofosteringacollaborativeresearchcommu- attackdatasetcontaininginsultinginstructionsand
nityistheabsenceofastandardparadigm,aneasy- test whether LLMs can be jailbroke. However,
to-useandextensibleresearchplatform. Previous asmentionedabove,existingdatasetshaveissues
workspursuethemostefficientwaytoimplementa that can not fully demonstrate abilities of LLMs.
sandboxwhileignoringtheneedofnon-specialist AgentSimsovercomesthesedifficultiesandrenders
users. Besides,thepoorreadabilityfurtherresults achanceforoverallevaluationofLLMs.
inpoorextensiblityanduserchurn. Moreover,the
2.2 MultiAgentCooperation
agents’performancevarieswithdifferentsupport
systems, i.e. memory, planning and tool-use sys- WithLLMsdemonstratetheiroverwhelmingabil-
tem. Weneedastandardimplementationtoensure ities, researchers find that multi LLM agents can
thereproducibilityofexperimentalresults. generatebetterresultsthanasingleone. Nairetal.
Tothisend, weintroduce AgentSims, an inter- (2023)isoneoftheearliestattemptsofmulti-agent
active, visualized, and program-based infrastruc- cooperation. It builds a forum for agents to com-
ture for curating evaluation tasks for LLMs. It municate feedback and iteratively improve their
creates an artificial town with various buildings healthcare suggestions. Li et al. (2023) expand
andresidents. ThecoreobjectiveofAgentSimsis theapplicationfieldofagentcooperationmethod
tostreamlinethetaskdesignprocess,eliminating by role-playing. From programming to domain-
hurdlesthatresearchersfromvariousbackgrounds specificQA,itsurpasssingleagentbaselines. Qian
andprogrammingproficienciesmightencounter. et al. (2023) build a software development com-
pany, by meticulously dividing the development
• For researchers focusing on LLM, AgentSims
processintofourdistinctstages,leadingtoefficient
is extendable and combinable to allow users
resolutionofspecificsubtasks. Liuetal.(2023b)
tocombinedifferentplan,memoryandlearning
firstapplymulti-agentsimulatedsocietyforalign-
systemstostudytheimpactsandeffectivenessof
ment,whereagentsinasandboxlearnfromsocial
varioussystemdesign.
interactiontounderstandmoralrules. (Parketal.,
• Forexpertsfromotherfieldslikebehavioraleco- 2023)isthemostsophisticatedapplicationofmulti
nomics or social psychology, AgentSims pro- agentsandbox. Authorsbuildsupportmechanisms
videsaninteractiveUIformapdesignandagent toenableagentstoproducebelievableindividual
creation and lower the entry threshold. Such a and emergent social behaviors. However, none
user-friendly architecture further facilitates the existingmethodsprovideauser-friendlyinterface
2

Figure1: FrontendofAgentSims,showinginapixelgamestyle. Userscancreateagentsandbuildingsinthe
left-sidepanelandobserveagentsbehaviorsinthemainscreen. Besidessetting-then-observing,userscanalsoplay
asthemayorandtalkwithagentstointervenetheexperiment.
forunprofessionalresearchersorbuildastandard ning System reorganizes a goal by decomposing
paradigm for agent support system. Nonetheless, thetarget,summarizingcurrentconditionandgen-
currentmulti-agentsystemsaretask-orientedrather eratingsubtasks. Specifically,itisassembledbya
than evaluation-oriented. AgentSims works as a seriesofpluggablepromptmodules,whichassess
platformforeasybenchmarkconstruction. currentachievementofultimategoalsbychecking
thememorysystemandmakingdecisionsfornext
3 KeyComponents steps. Onceanewstepiscompleted, itwouldbe
recordedinthememorysystem.
As shown in Figure 2, key components of
AgentSimscanbedividedintotwoparts: 1)genera- MemorySystem. Agentscapableofemulating
tiveagentsdrivenbyLLMsupportmechanisms. 2) humanbehaviornecessitatecomprehendingavast
buidlingsandequipmentthatconsistthesandbox array of experiences, beyond what a prompt can
environment. contain. The complete memory stream is too ex-
pensivetobeaccommodatedinthelimitedcontext
3.1 GenerativeAgents window,andattemptingtodosocanoverwhelmthe
model. Thus,weaddamemorysystemforagents’
If prompted properly, LLMs can generate believ-
experience retention and retrieval. The system is
able behaviors(Park et al., 2022). However, to
builtuponavectordatabaseforefficientstoringand
achievehuman-likememoryperformanceandlong-
retrieving. Specifically,everyagent’sdailymem-
termcoherence,LLMisnotenough. Weneedaux-
oryisencodedintoembeddingsandstoredinthe
iliary systems to enable agents to perform more
database. Everytimewhenagentsfacesomenew
naturally. Referring to recent work(Park et al.,
situationthatneedsthepreviousmemory,suchas
2023; Wang et al., 2023a), we abstract these sup-
chattingwithfamiliarpeople,thememorysystem
portivemechanismsintothreeparts: PlanningSys-
canretrievetheinformationabouttheirrelationship
tem,MemorySystem,andTool-UseSystem.
toimproveagentbehaviourconsistency.
PlanningSystemLLMshaveshownsomeplan-
ning and reasoning capacities. However, faced Tool-UseSystem. Ideally,agentscontinuously
withcomplextasks,vanillaLLMsalwaysfailfor explorethesimulatedworldwouldlearnfrompre-
lacking long-term arrangement abilities. Hence, viousfailuresandsuccesses,thenacquirediverse
weintroduceaPlanningSystemtoensureagents’ skills. Inourframework,torealizethisfeature,we
behaviors are coherent and believable. The Plan- present a tool-use system, which endows agents
3

Figure2: OverviewofAgentSimsarchitecture
withtheabilitytoaccomplishreal-worldtasks. Par- feedbackandrefineitsoperations.
ticularly, the tool use system stores equipment-
operation pairs learning from feedback of using 4 Interactionscenarios
equipment. Once agents select equipment to in-
Regarding the researchers’ backgrounds and pur-
teractwithbyplanningandmemorysystem,they
poses, we design two interaction modes: User
needtoinferaninitialoperationbythedescription
ModeandDeveloperMode. IntheUserMode,re-
oftheequipment. Andtheequipmentwillreturnan
searcherswhoconsiderlittleaboutbackgroundsup-
operationresultasfeeedback. Iftheagentbelieves
portsystemsaretargetusers. Forresearcherschas-
theresultmeetstheiroperationpurpose,anewskill
ing better LLMs performance, Developer Mode
wouldbestoredintheTool-UseSystem.
provides flexible protocols for their development
3.2 BuildingsandEquipment ofdifferentsupportmechanisms.
Interactivebuildingsandequipmentarenecessities
4.1 UserMode
for the diversity of an LLM sandbox. They com-
pose the physical environments of the simulated In the User Mode, AgentSims provides an inter-
world. Inourframework,abuildingorlocationcon- activeinterfaceinapixelgamestyle,asshownin
tainsequipmentlikestovesorofficedesks. Thus, Figure1. Researcherscancreateagents,construct
buildings are defined by the equipment they con- buildingsandequipmentinagraphicalinterface,fo-
tainandequipmentisthebasicelementcomposing cusingontherationalityofexperimentdesign,free
theinteractiveenvironment. Morespecifically,the fromcomplexbackgrounddrivingmechanisms.
equipmentcanbedefinedbysomedefinitiontexts AgentCreation. Userscandefineagentswithin
describingitsfeaturesandsupportfunction,which the system through an easy-to-use front end, as
can be either hard-coded by the developer or a shownintheFigure3. AgentSimsprovidesvarious
languagemodelthatsupportsself-adaptiveagent- protocolsforuserstocreatefunctionalagents. Not
equipment interaction. When an agent interacts only basic information like goals and biography,
withequipment,asshowninFigure2,itsoperation butalsooptionsofMemoryandPlanningSystems.
textwillbesenttothebackgroundsupportmodel. Wepre-designalistofmemoryandplanningsys-
The support function then returns the operation temsanduserscanchoosetheirpreferencefroma
outcome based on the predefined rules or model- drop-downmenu.
generatedtexts. Forexample,ifanagentwantsto Building Creation. Users can also customize
getacupofteafromastove,theoperationis’Get thephysicalenvironmentbyconstructingbuildings.
acupoftea’andthesupportfunctionmayreturn As shown in Figure 4, users define a building by
’Meaninglessoperation’accordingtothehardcode choosingapre-configuredbuildingwithequipment
or’Youcannotgetteafromastove’generatedby inside. Tobenoticed,theequipmentinbuildings
the model. Then the agent would learn from the arepredefinedbutcanbemodifiedintheDeveloper
4

class LLMCaller:
def __init__(self, model: str) -> None:
self.model = get_model(model)
def ask(self, prompt: str) :
result = self.model.generate(prompt)
return result
class Agent:
def __init__(self, name, bio, goal, model,
memorySystem, planSystem, buildings,
cash):
self.state = State()
self.state.buildings = buildings
Figure3: AgentCreation self.state.cash = cash
self.caller = Caller(model)
def plan(self) -> None:
self.state.plan_prompt = ...
self.state.plan =
self.caller.ask(self.state.pl_prompt)
def memory_store(self) -> None:
self.state.memory_prompt = ...
self.state.memory =
self.caller.ask(self.state.mem_prompt)
def use(self, facility: str, operation: str,
description: str) -> None:
self.state.use_prompt = ...
self.state.use =
self.caller.ask(self.state.use_prompt)
Figure4: BuildingCreation
BuildingandEquipmentDesign. Tocustomize
the physical environment, developers can design
Mode. newbuildingsandequipmentbyconfiguringcorre-
Experiment Intervene. Besides observing, spondingjsonfiles.
users can play as the major agent to participate A new equipment can be defined by its type, de-
in the experiment. By talking with other agents, scriptionandasupportfunction.
userscanintervenetheexperimentnaturallyrather
[{"id": 1,
thanmodifyagents’memoryorgoalsroughly.
"type": "counter",
"function":...,
4.2 DeveloperMode "description": "This is the counter ...",}]
DeveloperModeisdesignedforprofessionaldevel- In some cases, agents can purchase commodities
operswhoarefamiliarwiththepropertiesofLLMs orearnsalariesattheequipment. Weuseanother
andpursuebetterperformanceofLLMsonawell- configurefiletoannotatetheseeconomicfeatures.
definedcomplextask. Thehighly-modularizedfea-
[{ "id": 1,
tureofAgentSimsenablesdeveloperstoaddnew "menu": {
functionswithinafewlinesofcode. "chicken": 20,},
"salary":0,}],
Agent Design. Developers have the flexibility
tocreateagentstailoredforvariousobjectivesand Wedefinebuildingsbyatypeandtheequipmentit
assemble diverse agents within a single sandbox contains. Henceweuseatwo-dimensionalarrayto
forobservation. Tostreamlinetheprocessofagent markthefacilityidsinthebuildingblocks.
customization, we’ve abstracted the LLM back-
[{"assets": "store_v1.2_0719",
bone and distinct support systems into separate
"id": 1,
classes and function calls, as illustrated below. "price": 2000,
"type": "store",
Thisempowersdeveloperstopersonalizeanagent
"blocks":[[1,0,0...1,1]],
bymakingadjustmentstotheseabstractfunctions. "equipment":[0,1,0..]]}]
5

5 Implementation andmodifytheout-of-dateones,foundnewfunc-
tionalbuildingstosatisfyemergingrequirements,
AgentSims isrun usingPython 3.91 and requires
andsoon. ByanalyzingthesuccessrateofLLM
installingtherequirements.txtfileprovidedinthe
mayorunderdifferentdifficulties,researcherscan
codebaseusingPython’spackagemanagerPyPI2.
gainvaluableinsightsintothediversecapabilities
oftheLLM.
5.1 Backend
The web server is built using Tornado3, a 6.3 ApplicationsbesidesEvaluation
lightweight Python web framework. It also uses
BesidesevaluatingLLMs,AgentSimscanbeused
thewebsocketslibraryforAPIcallsandpushnoti-
asadatagenerationplatform. Duetothefantastic
fications,andmysql-connector-pythontointeract
NLGabilitiesofLLMs,researchershaveapplied
withtheMySQL4 database.
themindataannotation andaugmentation. How-
ever, some data involving social judgement and
5.2 Frontend
participationnecessitateamoreintricateapproach
FrontendThewebclientisbuiltwithUnity5. The than a single prompt can provide. Thus, we can
clientbuiltbyWebGL6 isembeddedintheproject simulateaspecificsocialbackgroundandletLLMs
codeandcanbeaccessedthroughabrowserafter generate data more precisely. Liu et al. (2023b)
proxyingwithnginx7.
have applied simulated society in alignment data
generation. WithAgentSimstailoredformoreintri-
6 ExampleApplicationTasks
catesocialsimulations,itspotentialforenhancing
datagenerationacrossvariousdisciplinesisunde-
6.1 SubjectLLMasparticipants
niable.
When subject LLM agents are participants of an
Moreover,ourprogramcanalsobenefitsocialsci-
artificialscenario,researcherscanevaluateLLM’s
enceresearchers,byconductingmorecontrollable
socialabilities,likeToM.Inthiscase,theformu-
preliminary experiments. Given that sota LLMs
lationofspecificsocialscenesisrealizedbyother
can understand human instructions and simulate
baselineagentsdrivenbystrongerLLMs. Forex-
humanbehaviours,socialscienceresearcherscan
ample, to study a new model’s social adaptation
designsocialenvironmentsastheywishforprelim-
abilities in a hostile environment, we can embed
inarystudies. Onceresearchershaveahypothesis,
colleagueagentsdrivenbyGPT4withastrongde-
pilotexperimentscanbeconductedinourvirtual
sireofbullyingnewcomers. Thenweplacesubject
sandboxasafeasibilitycheck.
agentsintothisadversarialmilieuandtestwhether
thenewmodelcanunderstandother’semotionand 7 Conclusion
improvehowcolleaguesperceiveit.
In this paper, we present AgentSims, avisualized
and program-based infrastructure for LLM test
6.2 SubjectLLMasmayor
sandbox construction. AgentSims aims to facil-
ToassessLLM’slong-termplanningandorganiza-
itateresearchersineffectivelybuildingLLMevalu-
tion abilities, researchers can appoint the subject
ationtasks. Itnotonlyintendstomakeallitscode
LLMasthemayorofatownorthepresidentofa
openlyavailablebutalsocommitstocontinuously
company,whereresidentsoremployeesaredriven
updating its documentation with comprehensive
by baseline agents like GPT4. To overcome the
tutorials.
difficultiessetaheaddeliberatelyoremergingdur-
Limitations
ingtheexperiments,thenachievethefinalgoalof
thetask,thesubjectLLMneedstorecruitnewresi- Asasandboxsystem,AgentSims’simulationabil-
dentstohandlenewproblems,issuesoundpolicies ity is limited by the accuracy of LLMs and the
diversityofbuildingsandequipment. Itcannever
1https://www.python.org/downloads/release/
fully reflect real world cases. Besides, although
python-390
2https://pypi.org/ task-basedevaluationisasoundapproachtomea-
3https://www.tornadoweb.org/en/stable/ surethegeneralabilityofLLMs,itcanhardlyre-
4https://www.mysql.com/
flectfine-grainedabilitieslikemathreasoning. The
5https://unity3d.com
6https://get.webgl.org passrateoftaskscannotprovideinsightsonwhy
7https://nginx.org/en/ LLMssuccessorfail.
6

References OpenAI.2023. Gpt-4technicalreport.
BIGbenchauthors.2023. Beyondtheimitationgame: Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai,
Quantifyingandextrapolatingthecapabilitiesoflan- MeredithRingelMorris,PercyLiang,andMichaelS.
guagemodels. TransactionsonMachineLearning Bernstein.2023. Generativeagents: Interactivesim-
Research. ulacraofhumanbehavior.
TomB.Brown,BenjaminMann,NickRyder,Melanie Joon Sung Park, Lindsay Popowski, Carrie J. Cai,
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind MeredithRingelMorris,PercyLiang,andMichaelS.
Neelakantan,PranavShyam,GirishSastry,Amanda Bernstein.2022. Socialsimulacra: Creatingpopu-
Askell, Sandhini Agarwal, Ariel Herbert-Voss, latedprototypesforsocialcomputingsystems.
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, David Premack and Guy Woodruff. 1978. Does the
ClemensWinter,ChristopherHesse,MarkChen,Eric chimpanzeehaveatheoryofmind? Behavioraland
Sigler,MateuszLitwin,ScottGray,BenjaminChess, brainsciences,1(4):515–526.
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei. Chen Qian, Xin Cong, Cheng Yang, Weize Chen,
2020. Languagemodelsarefew-shotlearners. YushengSu,JuyuanXu,ZhiyuanLiu,andMaosong
Sun.2023. Communicativeagentsforsoftwarede-
Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio velopment.
CésarTeodoroMendes,AllieDelGiorno,Sivakanth
Gopi,MojanJavaheripi,PieroKauffmann,Gustavo YongliangShen,KaitaoSong,XuTan,DongshengLi,
deRosa,OlliSaarikivi,etal.2023. Textbooksareall WeimingLu,andYuetingZhuang.2023. Hugging-
youneed. arXivpreprintarXiv:2306.11644. gpt: Solvingaitaskswithchatgptanditsfriendsin
huggingface. arXivpreprintarXiv:2303.17580.
DanHendrycks,CollinBurns,StevenBasart,AndyZou,
MantasMazeika,DawnSong,andJacobSteinhardt. HaoSun,ZhexinZhang,JiawenDeng,JialeCheng,and
2020. Measuringmassivemultitasklanguageunder- MinlieHuang.2023. Safetyassessmentofchinese
standing. arXivpreprintarXiv:2009.03300. largelanguagemodels.
Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
Zhang, Jinghan Zhang, Tangjun Su, Junteng Liu, dlekar,ChaoweiXiao,YukeZhu,LinxiFan,andAn-
Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao imaAnandkumar.2023a. Voyager: Anopen-ended
Fu, Maosong Sun, and Junxian He. 2023. C- embodiedagentwithlargelanguagemodels.
eval: A multi-level multi-discipline chinese evalu-
JiaanWang,YunlongLiang,FandongMeng,Zengkui
ation suite for foundation models. arXiv preprint
Sun,HaoxiangShi,ZhixuLi,JinanXu,JianfengQu,
arXiv:2305.08322.
andJieZhou.2023b. Ischatgptagoodnlgevaluator?
Guohao Li, Hasan Abed Al Kader Hammoud, Hani apreliminarystudy.
Itani,DmitriiKhizbullin,andBernardGhanem.2023.
LilianWeng.2023. Llm-poweredautonomousagents.
Camel: Communicative agents for "mind" explo-
lilianweng.github.io.
rationoflargescalelanguagemodelsociety.
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,
Yen-Ting Lin and Yun-Nung Chen. 2023. Llm-eval:
Thomas L. Griffiths, Yuan Cao, and Karthik
Unifiedmulti-dimensionalautomaticevaluationfor
Narasimhan. 2023. Tree of thoughts: Deliberate
open-domainconversationswithlargelanguagemod-
problemsolvingwithlargelanguagemodels.
els.
WanjunZhong,RuixiangCui,YiduoGuo,YaoboLiang,
HanmengLiu,RuoxiNing,ZhiyangTeng,JianLiu,Qiji
ShuaiLu,YanlinWang,AminSaied,WeizhuChen,
Zhou,andYueZhang.2023a. Evaluatingthelogical
and Nan Duan. 2023. Agieval: A human-centric
reasoningabilityofchatgptandgpt-4.
benchmarkforevaluatingfoundationmodels.
RuiboLiu,RuixinYang,ChenyanJia,GeZhang,Denny
ChuntingZhou,PengfeiLiu,PuxinXu,SriniIyer,Jiao
Zhou, Andrew M. Dai, Diyi Yang, and Soroush
Sun,YuningMao,XuezheMa,AviaEfrat,PingYu,
Vosoughi.2023b. Trainingsociallyalignedlanguage
Lili Yu, Susan Zhang, Gargi Ghosh, Mike Lewis,
modelsinsimulatedhumansociety.
LukeZettlemoyer,andOmerLevy.2023. Lima:Less
Varun Nair, Elliot Schumacher, Geoffrey Tso, and ismoreforalignment.
Anitha Kannan. 2023. Dera: Enhancing large lan-
guagemodelcompletionswithdialog-enabledresolv-
ingagents.
ErikNijkamp,BoPang,HiroakiHayashi,LifuTu,Huan
Wang,YingboZhou,SilvioSavarese,andCaiming
Xiong. 2023. Codegen: An open large language
modelforcodewithmulti-turnprogramsynthesis.
7
