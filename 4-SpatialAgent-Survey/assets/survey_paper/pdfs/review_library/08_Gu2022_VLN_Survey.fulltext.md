Title: 08_Gu2022_VLN_Survey

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/review_library/08_Gu2022_VLN_Survey.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:36+00:00
- page_count: 18
- status: ok
- text_char_count: 71185

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

Vision-and-Language Navigation:
A Survey of Tasks, Methods, and Future Directions
JingGu1 ElianaStefani1 QiWu2 JesseThomason3 XinEricWang1
1UniversityofCalifornia,SantaCruz
2TheUniversityofAdelaide 3UniversityofSouthernCalifornia
{jgu110,estefani,xwang366}@ucsc.edu
qi.wu01@adelaide.edu.au, jessetho@usc.edu
Abstract
n O
o b
A long-term goal of AI research is to build
ati s
e
intelligentagentsthatcancommunicatewith
b
s er
v rv
a tio
humansinnaturallanguage,perceivetheenvi- O o n Environment A c n
ronment,andperformreal-worldtasks. Vision- A
cti tio
n
and-Language Navigation (VLN) is a funda-
mentalandinterdisciplinaryresearchtopicto-
wardsthisgoal,andreceivesincreasingatten-
tion from natural language processing, com- Natural Language
puter vision, robotics, and machine learning Communication
communities. Inthispaper,wereviewcontem- Agent Oracle
porary studies in the emerging field of VLN, Figure1: TheagentandoraclediscusstheVLNtask
covering tasks, evaluation metrics, methods, innaturallanguage. Bothobserveandinteractwiththe
etc. Through structured analysis of current navigableenvironmenttoaccomplishatask.
progressandchallenges,wehighlightthelim-
itationsofcurrentVLNandopportunitiesfor
futurework. Thispaperservesasathorough communicatewithhumansinnaturallanguageand
referencefortheVLNresearchcommunity.1
navigateinreal3Denvironments. VLNextendsvi-
sualnavigationinbothsimulated(Zhuetal.,2017;
1 Introduction
Mirowski,2019)andrealenvironments(Mirowski
Humans communicate with each other using nat- etal.,2018)withnaturallanguagecommunication.
urallanguagetoissuetasksandrequesthelp. An As illustrated in Figure 1, VLN is a task that in-
agentthatcanunderstandhumanlanguageandnav- volvestheoracle(frequentlyahuman),theagent,
igate intelligently would significantly benefit hu- and the environment. The agent and the oracle
man society, both personally and professionally. communicateinnaturallanguage. Theagentmay
Such an agent can be spoken to in natural lan- askforguidanceandtheoraclecouldrespond. The
guage,andwouldautonomouslyexecutetaskssuch agentnavigatesandinteractswiththeenvironment
as household chores indoors, repetitive delivery tocompletethetaskaccordingtotheinstructionsre-
work outdoors, or work in hazardous conditions ceivedandtheenvironmentobserved. Meanwhile,
following human commands (bridge inspection; theoracleobservestheenvironmentandagentsta-
fire-fighting). Scientifically, developing such an tus,andmayinteractwiththeenvironmenttohelp
agent explores how an artificial agent interprets theagent.
naturallanguagefromhumans,perceivesitsvisual Sincethedevelopmentandreleaseofworkssuch
environment,andutilizesthatinformationtonavi- asRoom-to-Room(R2R)(Andersonetal.,2018b),
gatetocompleteatasksuccessfully. many VLN datasets have been introduced. Re-
Vision-and-Language Navigation (VLN) (An- gardingthedegreeofcommunication,researchers
derson et al., 2018b; Chen et al., 2019; Thoma- createbenchmarkswheretheagentisrequiredto
son et al., 2019b) is an emerging research field passivelyunderstandoneinstructionbeforenaviga-
thataimstobuildsuchanembodiedagentthatcan tion,tobenchmarkswhereagentsconversewiththe
oracleinfree-formdialog. Regardingthetaskob-
1WealsoreleaseaGithubrepotokeeptrackofadvances
jective,therequirementsfortheagentrangefrom
in VLN: https://github.com/eric-ai-lab/
awesome-vision-language-navigation strictly following the route described in the ini-
7606
Proceedingsofthe60thAnnualMeetingoftheAssociationforComputationalLinguistics
Volume1:LongPapers,pages7606-7623
May22-27,2022(cid:13)c2022AssociationforComputationalLinguistics

tial instruction to actively exploring the environ- navigationandunderstandsfurtheroracleguidance.
mentandinteractingwithobjects. Inaslightabuse Task Objective defines how the agent attains
of terminology, we refer to benchmarks that in- its goal based on the initial instructions from the
volve object interaction together with substantial oracle. In the first objective type, Fine-grained
sub-problemsofnavigationandlocalization,such Navigation,theagentcanfindthetargetaccording
asALFRED(Shridharetal.,2020),asVLNbench- toadetailedstep-by-steproutedescription. Inthe
marks. secondtype,Coarse-grainedNavigation,theagent
ManychallengesexistinVLNtasks. First,VLN isrequiredtofindadistanttargetgoalwithacoarse
facesacomplexenvironmentandrequireseffective navigationdescription,requiringtheagenttorea-
understandingandalignmentofinformationfrom sonapathinanavigableenvironmentandpossibly
differentmodalities. Second,VLNagentsrequirea elicit additional oracle help. Tasks in the previ-
reasoningstrategyforthenavigationprocess. Data oustwotypesonlyrequiretheagenttonavigateto
scarcity is also an obstacle. Lastly, the general- completethemission. Inthethirdtype,Navigation
ization of a model trained in seen environments and Object Interaction, besides reasoning a path,
to unseen environments is also essential. We cat- theagentalsoneedstointeractwithobjectsinthe
egorize the solutions according to the respective environment to achieve the goal since the object
challenges. (1)Representationlearningmethods mightbehiddenorneedtochangephysicalstates.2
helpunderstandinformationfromdifferentmodal- Aswithcoarse-grainednavigation,someobjectin-
ities. (2) Action strategy learning aims to make teractiontaskscanrequireadditionalsupervision
reasonable decisions based on gathered informa- viadialoguewiththeoracle.
tion. (3)Data-centriclearningmethodseffectively
2.1 InitialInstruction
utilize the data and address data challenges such
as data scarcity. (4) Prior exploration helps the InmanyVLNbenchmarks,theagentisgivenanat-
modelfamiliarizeitselfwiththetestenvironment, urallanguageinstructionforthewholenavigation
improvingitsabilitytogeneralize. process,suchas“Goupstairsandpassthetablein
We make three primary contributions. (1) We thelivingroom. Turnleftandgothroughthedoor
systematicallycategorizecurrentVLNbenchmarks inthemiddle.”
fromcommunicationcomplexityandtaskobjective Fine-grained Navigation An agent needs to
perspectives,witheachcategoryfocusingonadif- strictlyfollowthenaturallanguageinstructionto
ferent type of VLN task. (2) We hierarchically reachthetargetgoal. Andersonetal.(2018b)create
classifycurrentsolutionsandthepaperswithinthe theR2RdatasetbasedontheMatterport3Dsimula-
scope. (3)Wediscusspotentialopportunitiesand tor(Changetal.,2017). AnembodiedagentinR2R
identifyfuturedirections. movesthroughahouseinthesimulatortraversing
edgesonanavigationgraph,jumpingtoadjacent
2 TasksandDatasets nodes containing panoramic views. R2R is ex-
tended to create other VLN benchmarks. Room-
The ability for an agent to interpret natural lan-
for-Room joins paths in R2R to longer trajecto-
guageinstructions(andinsomeinstances,request
ries (Jain et al., 2019). Yan et al. (2020) collect
feedback during navigation) is what makes VLN
XL-R2RtoextendR2RwithChineseinstructions.
uniquefromvisualnavigation(Bonin-Fontetal.,
RxR (Ku et al., 2020) contains instructions from
2008). In Table 2, we mainly categorize current
English,Hindi,andTelegu. Thedatasethasmore
datasetsontwoaxes,CommunicationComplexity
samplesandtheinstructionsinitaretime-aligned
andTaskObjective.
tothevirtualposesoftheinstruction. TheEnglish
CommunicationComplexitydefinesthelevel
splitofRxRisfurtherextendedtobuildLandmark-
at which the agent may converse with the oracle,
RxR(Heetal.,2021)byincorporatinglandmark
andwedifferentiatethreelevels: Inthefirstlevel,
information.
theagentisonlyrequiredtounderstandanInitial
Inmostcurrentdatasets, agentstraverseanav-
Instructionbeforenavigationstarts. Inthesecond
igation graph at predefined viewpoints. To facil-
level,theagentsendsasignalforhelpwheneverit
isunsure,utilizingtheGuidancefromtheoracle. In 2Navigation and Object Interaction includes both fine-
grainedandcoarse-grainedinstructions,whichideallyshould
thethirdlevel,theagentwithDialogueabilityasks
besplitfurther.Butgiventhatthereareonlyfewdatasetsin
questionsintheformofnaturallanguageduringthe thiscategory,wekeepthecurrentcategorizationinTable2.
7607

Comm TaskObjective
Complexity
Fine-grainedNavigation Coarse-grainedNavigation Nav+ObjectInteraction
Room-to-Room(Andersonetal.,2018b),
InitialIn- Room-for-Room (Jain et al., 2019), RoomNav(Wuetal.,2018), IQA(Gordonetal.,2018),
struction(s) Room-Across-Room (Ku et al., 2020), EmbodiedQA(Dasetal., CHAI(Misraetal.,2018),
XL-R2R(Yanetal.,2020),Landmark- 2018),REVERIE(Qietal., ALFRED(Shridharetal.,
RxR(Heetal.,2021),VLNCE(Krantz 2020b),SOON(Zhuetal., 2020)
et al., 2020), TOUCHDOWN (Chen 2021a)
et al., 2019), StreetLearn (Mirowski
etal.,2019),StreetNav(Hermannetal.,
2020), Talk2Nav (Vasudevan et al.,
2021),LANI(Misraetal.,2018)
VNLA(Nguyenetal.,2019),
Oracle JustAsk(Chietal.,2020) HANNA (Nguyen and None
Guidance DauméIII,2019)
CVDN (Thomason et al., TEACh (Padmakumar et al.,
Dialogue None 2019b), RobotSlang (Baner- 2021), Minecraft Collabora-
jee et al., 2020), Talk the tiveBuilding(Narayan-Chen
Walk (de Vries et al., 2018), etal.,2019),DialFRED(Gao
CEREALBAR (Suhr et al., etal.,2022)
2019)
Table1: Vision-and-LanguageNavigationbenchmarksorganizedbyCommunicationComplexityversusTask
Objective. Please refer to Appendix for more details about the datasets and the commonly used underlying
simulators.
itate transfer learning to real agents, VLN tasks sinceitmaybeunknowntothehumaninstructor
should provide a continuous action space and a (oracle). Usually,instructionsaremoreconciseand
freelynavigableenvironment. Tothisend,Krantz containmerelyinformationofthetargetgoal.
etal.(2020)reconstructthenavigationgraphbased
RoomNav(Wuetal.,2018)requiresagentnavi-
R2Rtrajectoriesincontinuousenvironmentsand
gateaccordingtoinstruction“gotoX”,whereXis
createVLNCE.Irshadetal.(2021)proposeRobo-
apredefinedroomorobject.
VLNtaskwheretheagentoperatesinacontinuous
In Embodied QA (Das et al., 2018), the agent
actionspaceoverlong-horizontrajectories.
navigates through the environment to find an-
Outdoor environments are usually more com-
swer for a given question. The instructions in
plexandcontainmoreobjectsthanindoorenviron-
REVERIE(Qietal.,2020b)areannotatedbyhu-
ments. InTOUCHDOWN(Chenetal.,2019),an
mans,andthusmorecomplicatedanddiverse. The
agentfollowsinstructionstonavigateastreetview
agent navigates through the rooms and differen-
rendered simulation of New York City to find a
tiates the object against multiple competing can-
hiddenobject. Mostphoto-realisticoutdoorVLN
didates. In SOON (Zhu et al., 2021a), an agent
datasets including TOUCHDOWN (Chen et al.,
receivesalong,complexcoarse-to-fineinstruction
2019),StreetLearn(Mirowskietal.,2019;Mehta
whichgraduallynarrowsdownthesearchscope.
etal.,2020),StreetNav(Hermannetal.,2020),and
Navigation+ObjectInteraction Forsometasks,
Talk2Nav (Vasudevan et al., 2021) are proposed
thetargetobjectmightbehidden(e.g.,thespoonin
basedonGoogleStreetView.
adrawer),orneedtochangestatus(e.g.,aslicedap-
Some work uses natural language to guide
pleisrequestedbutonlyawholeappleisavailable).
drones. LANI (Misra et al., 2018) is a 3D syn-
Inthesescenarios,itisnecessarytointeractwith
theticnavigationenvironment,whereanagentnav-
theobjectstoaccomplishthetask(e.g.,openingthe
igates between landmarks following natural lan-
drawerorcuttingtheapple). InteractiveQuestion
guageinstructions. Currentdatasetsondronenavi-
Answering (IQA) requires the agent to navigate
gationusuallyfallinasyntheticenvironmentsuch
and sometimes to interact with objects to answer
asUnity3D(Blukisetal.,2018,2019).
agivenquestion. BasedonindoorscenesinAI2-
Coarse-grainedNavigation Inreallife,detailed THOR(Kolveetal.,2017),Shridharetal.(2020)
informationaboutthe routemaynotbe available propose the ALFRED dataset, where agents are
7608

providedwithbothcoarse-grainedandfine-grained developedforthiscategoryforsuperlonghorizon
instructionscompletehouseholdtasksinaninterac- navigation tasks in complex environments espe-
tivevisualenvironment. CHAI(Misraetal.,2018) ciallywithrichdynamicswheredialogisnecessary
requirestheagenttonavigateandsimplyinteract toclearconfusions.
withtheenvironments. Coarse-grainedNavigation CVDN(Thomason
et al., 2019b) is a dataset of human-human dia-
2.2 OracleGuidance
logues. Besidesinterpretinganaturallanguagein-
AgentsinGuidanceVLNtasksmayreceivefurther structionanddecidingonthefollowingaction,the
naturallanguageguidancefromtheoracleduring VLNagentalsoneedstoaskquestionsinnatural
navigation. For example, if the agent is unsure language for guidance. The oracle, with knowl-
ofthenextstep(e.g.,enteringthekitchen),itcan edge of the best next steps, needs to understand
senda[help]signal,andtheoraclewouldassistby andcorrectlyanswersaidquestions.
responding“goleft”(Nguyenetal.,2019). Dialogueisimportantincomplexoutdoorenvi-
Fine-grainedNavigation Theinitialfine-grained ronments. deVriesetal.(2018)introducetheTalk
navigationinstructionmaystillbeambiguousina theWalkdataset,wheretheguidehasknowledge
complex environment. Guidance from the oracle fromamapandguidesthetouristtoadestination,
couldclarifypossibleconfusion. Chietal.(2020) butdoesnotknowthetourist’slocation;whilethe
introduceJustAsk—ataskwhereanagentcould touristnavigatesa2Dgridviadiscreteactions.
askoracleforhelpduringnavigation.
Navigation+Object Interaction Minecraft Col-
Coarse-grainedNavigation Withonlyacoarse-
laborative Building (Narayan-Chen et al., 2019)
grainedinstructiongivenatthebeginning,theagent
studieshowanagentplacesblocksintoabuilding
tendstobemoreconfusedandspendsmoretimeex-
bycommunicatingwiththeoracle. TEACh(Pad-
ploring. Furtherguidanceresolvesthisambiguity.
makumaretal.,2021)isadatasetthatstudiesob-
VNLA(Nguyenetal.,2019)andHANNA(Nguyen
jectinteractionandnavigationwithfree-formdia-
and Daumé III, 2019) both train an agent to nav-
log. Thefollowerconverseswiththecommander
igate indoors to find objects. The agent could
and interacts with the environment to complete
request help from the oracle, which responds by
various house tasks such as making coffee. Dial-
providing a subtask which helps the agent make
FRED(Gaoetal.,2022)extendsALFRED(Shrid-
progress. WhileoracleinVNLAusespredefined
har et al., 2020) dataset by allowing the agent to
scripttorespond,theoracleinHANNAusesaneu-
activelyaskquestions.
ralnetworktogeneratenaturallanguageresponses.
CEREALBAR(Suhretal.,2019)isacollaborative 3 Evaluation
taskbetweenaleaderandafollower. Bothagents
moveinavirtualgameenvironmenttocollectvalid Goal-oriented Metrics mainly consider the
setsofcards. agent’s proximity to the goal. The most intuitive
Navigation+Object Interaction While VLN is is Success Rate (SR), which measures how fre-
stillinitsyouth,therearenoVLNdatasetsinsup- quentlyanagentcompletesthetaskwithinacertain
portofGuidanceandObjectInteraction. distance of the goal. Goal Progress (Thomason
et al., 2019b) measures the reduction in remain-
2.3 HumanDialogue
ing distance to the target goal. Path Length (PL)
Itishuman-friendlytousenaturallanguagetore- measures the total length of the navigation path.
questhelp(Banerjeeetal.,2020;Thomasonetal., Shortest-PathDistance(SPD)measuresthemean
2019b). For example, when the agent is not sure distancebetweentheagent’sfinallocationandthe
about what fruit the human wants, it could ask goal. Since a longer path length is undesirable
“Whatfruitdoyouwant,thebananaintherefrig- (increases duration and wear-and-tear on actual
eratorortheappleonthetable?”,andthehuman robots), Success weighted by Path Length (SPL)
responsewouldprovideclearnavigationdirection. (Anderson et al., 2018a) balances both Success
Fine-grainedNavigation Nodatasetsareinthe RateandPathLength. Similarly,Successweighted
scope of this category. Currently, route-detailed by Edit Distance (SED) (Chen et al., 2019) com-
instructionwithpossibleguidancecouldhelpthe parestheexpert’sactions/trajectorytotheagent’s
agentachieverelativelygoodperformanceinmost actions/trajectory,alsobalancingSRandPL.Ora-
simulatedenvironments. Weexpectdatasetstobe cleNavigationError(ONE)takestheshortestdis-
7609

tancefromanynodeinthepathratherthanjustthe
Methods
lastnode,andOracleSuccessRate(OSR)measures
whetheranynodeinthepathiswithinathreshold
Represen-
Prior Strategy Data-centric
fromthetargetlocation. tation
Exploration Learning
Learning
Path-fidelityMetrics evaluatetowhatextentan
agentfollowsthedesiredpath. Sometasksrequire Pre-training Reinforcement Data
the agent not only to find the goal location but Learning Augmentation
Semantic
alsotofollowspecificpath. Fidelitymeasuresthe Exploration
Understanding during Curriculum
matchesbetweentheactionsequenceintheexpert Graph Navigation Learning
demonstrationandtheactionsequenceintheagent Representation
Navigation Multitask
trajectory. Coverage weighted by LS (CLS) (Jain Memory Planning Learning
et al., 2019) is the product of the Path Coverage Structure
(PC)andLengthScore(LS)withrespecttotheref- Auxiliary Asking for Instruction
Task Help Interpretation
erencepath. Itmeasureshowcloselyanagent’stra-
jectoryfollowsthereferencepath. NormalizedDy- Figure2: CategoriesofVLNmethods. Methodsmay
namicTimeWarping(nDTW)(Ilharcoetal.,2019) notbemutuallyexclusivetoanindividualcategory.
softlypenalizesdeviationsfromthereferencepath
tocalculatethematchbetweentwopaths. Success
4.1.1 Pretraining
weighted by normalized Dynamic Time Warping
VisionorLanguage Usingapretrainedmodelto
(SDTW) (Ilharco et al., 2019) further constrains
initializeavisionortextencoderprovidesagents
nDTWtoonlysuccessfulepisodestocaptureboth
with single-modality knowledge. pretrained vi-
successandfidelity.
sion models may use a ResNet (He et al., 2016)
orVisionTransformers(Dosovitskiyetal.,2020).
4 VLNMethods
Other navigation tasks (Wijmans et al., 2019b)
mayalsoprovidevisualinitialization(Krantzetal.,
AsshowninFigure2,wecategorizeexistingmeth-
2020). Largepretrainedlanguagemodelssuchas
odsintoRepresentationLearning,ActionStrategy
BERT(Devlinetal.,2019)andGPT(Radfordetal.,
Learning, Data-centric Learning, and Prior Ex-
2019)canencodelanguageandimproveinstruction
ploration. Representation learning methods help
understanding(Lietal.,2019),whichcanbefur-
agent understand relations between these modal-
therpretrainedwithVLNinstructions (Pashevich
ities since VLN involves multiple modalities, in-
etal.,2021)beforefine-tuninginVLNtask.
cluding vision, language, and action. Moreover,
Vision and Language Vision-and-language pre-
VLNisacomplexreasoningtaskwheremissionre-
trained models provide good joint representation
sultsdependontheaccumulatingsteps,andbetter
for text and vision. A common practice is to ini-
actionstrategieshelpthedecision-makingprocess.
tializetheVLNagentwithapretrainedmodelsuch
Additionally, VLN tasks face challenges within
asViLBERT(Luetal.,2019). Theagentmaybe
theirtrainingdata. Onesevereproblemisscarcity.
furthertrainedwithVLN-specificfeaturessuchas
CollectingtrainingdataforVLNisexpensiveand
objectsandrooms(Qietal.,2021).
time-consuming,andtheexistingVLNdatasetsare
VLN Downstreamtasksbenefitfrombeingclosely
relativelysmallwithrespecttothecomplexityof
related to the pretraining task. Researchers also
VLNtasks. Therefore,data-centricmethodshelp
exploredpretrainingontheVLNdomaindirectly.
to utilize the existing data and create more train-
VLN-BERT(Majumdaretal.,2020)pretrainsnav-
ing data. Prior exploration helps adapt agents to
igation models to measure the compatibility be-
previouslyunseenenvironments,improvingtheir
tweenpathsandinstructions,whichformatsVLN
ability to generalize, decreasing the performance
as a path selection problem. PREVALENT (Hao
gapbetweenseenversusunseenenvironments.
etal.,2020)istrainedfromscratchonimage-text-
action triplets to learn textual representations in
4.1 RepresentationLearning
VLNtasks. Theoutputembeddingfromthe[CLS]
Representationlearninghelpstheagentunderstand tokeninBERT-basedpretrainingmodelscouldbe
howthewordsintheinstructionrelatetotheper- leveraged in a recurrent fashion to represent his-
ceivedfeaturesintheenvironment. torystate(Hongetal.,2021;Moudgiletal.,2021).
7610

Airbert (Guhur et al., 2021) achieve good perfor- 4.1.4 Memory-augmentedModel
mance on few-shot setting after pretraining on a
Information accumulates as the agent navigates,
large-scalein-domaindataset.
which is not efficient to utilize directly. Memory
structure helps the agent effectively leverage the
4.1.2 SemanticUnderstanding navigationhistory. Somesolutionsleveragemem-
orymodulessuchasLSTMsorrecurrentlyutilize
SemanticunderstandingofVLNtasksincorporates informativestates(Hongetal.,2021),whichcanbe
knowledge about important features in VLN. In relativelyeasilyimplemented,butmaystruggleto
addition to the raw features, high-level semantic rememberfeaturesatthebeginningofthepathas
representations also improve performance in un- pathlengthincreases. Anothersolutionistobuilda
seenenvironments. separatememorymodeltostoretherelevantinfor-
Intra-Modality Visualortextualmodalitiescan mation(Zhuetal.,2020c;Linetal.,2021;Nguyen
bedecomposedintomanyfeatures,whichmatter andDauméIII,2019). Notably,byhierarchically
differentlyinVLN.Theoverallvisualfeaturesex- encoding a single view, a panorama, and then all
tractedbyaneuralmodelmayactuallyhurttheper- panoramasinhistory,HAMT(Chenetal.,2021b)
formanceinsomecases(Thomasonetal.,2019a; successfullyutilizedthefullnavigationhistoryfor
Huetal.,2019;Zhangetal.,2020b). Therefore,it decision-making.
isimportanttofindthefeature(s)thatbestimprove
4.1.5 AuxiliaryTasks
performance. High-level features such as visual
appearance, route structure, and detected objects Auxiliary tasks help the agent better understand
outperformthelowlevelvisualfeaturesextracted the environment and its own status without extra
byCNN(Huetal.,2019). Differenttypesoftokens labels. Fromthemachinelearningperspective,an
withintheinstructionalsofunctiondifferently(Zhu auxiliary task is usually achieved in the form of
etal.,2021b). Extractingthesetokensandencod- an additional loss function. The auxiliary task
ingtheobjecttokensanddirectionstokensarecru- could, for example, explain its previous actions,
cial(Qietal.,2020a;Zhuetal.,2021b). orpredictinformationaboutfuturedecisions(Zhu
et al., 2020a). Auxiliary tasks could also involve
Inter-Modality Semantic connections between
the current mission such as current task accom-
differentmodalities: actions,scenes,observedob-
plishment,andvision&instructionalignment(Ma
jects,directionclues,andobjectsmentionedinin-
et al., 2019a; Zhu et al., 2020a). Notably, auxil-
structionscanbeextractedandthensoftlyaligned
iary tasks are effective when adapting pretrained
with attention mechanism (Qi et al., 2020a; Gao
representationsforVLN(Huangetal.,2019).
etal.,2021). Thesoftalignmentalsohighlightsrel-
evantpartsoftheinstructionwithrespecttothecur-
4.2 ActionStrategyLearning
rentstep(Landietal.,2019;Zhangetal.,2020a).
Withmanypossibleactionchoicesandcomplicated
environment, action strategy learning provides a
4.1.3 GraphRepresentation
varietyofmethodstohelptheagentdecideonthose
Buildinggraphtoincorporatestructuredinforma- bestactions.
tionfrominstructionandenvironmentobservation
4.2.1 ReinforcementLearning
providesexplicitsemanticrelationtoguidethenav-
igation. The graph neural network may encode VLNisasequentialdecision-makingproblemand
therelationbetweentextandvisiontobetterinter- can naturally be modeled as a Markov decision
pret the context information (Hong et al., 2020a; process. So Reinforcement Learning (RL) meth-
Dengetal.,2020). Thegraphcouldrecordtheloca- ods are proposed to learn better policy for VLN
tioninformationduringthenavigation,whichcan tasks. AcriticalchallengeforRLmethodsisthat
used to predict the most likely trajectory (Ander- VLNagentsonlyreceivethesuccesssignalatthe
son et al., 2019a) or probability distribution over endoftheepisode,soitisdifficulttoknowwhich
actionspace(Dengetal.,2020). Whenconnected actions to attribute success to, and which to pe-
withpriorexploration,anoverviewgraphaboutthe nalize. To address the ill-posed feedback issue,
navigableenvironment(Chenetal.,2021a)canbe Wangetal.(2019)proposeRCMmodeltoenforces
builttoimprovenavigationinterpretation. cross-modalgroundingbothlocallyandglobally,
7611

withgoal-orientedextrinsicrewardandinstruction- 4.2.4 AskingforHelp
fidelityintrinsicreward. Heetal.(2021)propose Anintelligentagentasksforhelpwhenuncertain
toutilizethelocalalignmentbetweentheinstruc- about the next action. Action probabilities or a
tion and critical landmarks as the reward. Eval- separately trained model (Chi et al., 2020; Zhu
uation metrics such as CLS (Jain et al., 2019) or et al., 2021c; Nguyen et al., 2021a) can be lever-
nDTW (Ilharco et al., 2019) can also provide in- aged to decide whether to ask for help. Using
formative reward signal (Landi et al., 2020), and naturallanguagetoconversewiththeoraclecovers
naturallanguagemayalsoprovidesuggestionsfor awiderproblemscopethansendingasignal. Both
reward(Fuetal.,2019). rule-basedmethods(Padmakumaretal.,2021)and
To model the dynamics in the environment, neural-basedmethods(Romanetal.,2020;Nguyen
Wangetal.(2018)leveragemodel-basedreinforce- et al., 2021a) have been developed to build navi-
mentlearningtopredictthenextstateandimprove gationagentswithdialogability. Meanwhile,for
thegeneralizationinunseenenvironment. Zhang tasks(Thomasonetal.,2019b;Padmakumaretal.,
etal.(2020a)findrecursivelyalternatingthelearn- 2021)thatdonotprovideanoracleagenttoanswer
ingschemesofimitationandreinforcementlearn- questioninnaturallanguage,researchersalsoneed
ingimprovetheperformance. to build a rule-based (Padmakumar et al., 2021)
orneural-based(Romanetal.,2020)oracle. Dial-
FRED(Gaoetal.,2022)usesalanguagemodelas
4.2.2 ExplorationduringNavigation
anoracletoanswerquestions.
Exploring and gathering environmental informa-
4.3 Data-centricLearning
tionwhilenavigatingprovidesabetterunderstand-
ing of the state space. Student-forcing is a fre- Compared with previously discussed works that
quentlyusedstrategy,wheretheagentkeepsnav- focus on building a better VLN agent structure,
igating based on sampled actions and is super- data-centric methods most effectively utilize the
visedbytheshortest-pathaction(Andersonetal., existingdata,orcreatesyntheticdata.
2018b).
4.3.1 DataAugmentation
There is a tradeoff between exploration versus
Trajectory-Instruction Augmentation Aug-
exploitation: withmoreexploration,theagentsees
mentedpath-instructionpairscouldbeusedinVLN
betterperformanceatthecostofalongerpathand
directly. Currentlythecommonpracticeistotrain
longerduration,sothemodelneedstodetermine
aspeakermoduletogenerateinstructionsgivena
whenandhowdeeptoexplore (Wangetal.,2020a).
navigation path (Fried et al., 2018). This gener-
After having gathered the local information, the
ateddatahavevaryingquality(Zhaoetal.,2021).
agent needs to decide which step to choose, or
Thereforeanalignmentscorer(Huangetal.,2019)
whether to backtrack (Ke et al., 2019). Notably,
or adversarial discriminator (Fu et al., 2020) can
Koh et al. (2021) designed Pathdreamer, a visual
selecthigh-qualitypairsforaugmentation.
worldmodeltosynthesizevisualobservationfuture
EnvironmentAugmentation Generatingmoreen-
viewpointswithoutactuallylookingahead.
vironmentdatanotonlyhelpsgeneratemoretrajec-
tories,butalsoalleviatestheproblemofoverfitting
4.2.3 NavigationPlanning inseenenvironments. Randomlymaskingthesame
visualfeatureacrossdifferentviewpoints(Tanetal.,
Planing future navigation steps leads to a better 2019)orsimplysplittingthehousescenesandre-
action strategy. From the visual side, predicting mixing them (Liu et al., 2021) could create new
thewaypoints(Krantzetal.,2021),nextstateand environments,whichcouldfurtherbeusedtogen-
reward(Wangetal.,2018),generatefutureobser- eratemoretrajectory-instructionpairs(Friedetal.,
vation (Koh et al., 2021) or incorporating neigh- 2018). Training data may also be augmented by
bor views (An et al., 2021) has proven effective. replacingsomevisualfeatureswithcounterfactual
Thenaturallanguageinstructionalsocontainsland- ones(Parvanehetal.,2020).
marks and direction clues to plan detailed steps.
Anderson et al. (2019b) predict the forthcoming 4.3.2 CurriculumLearning
events based on the instruction, which is used to Curriculumlearning(Bengioetal.,2009)gradually
predictactionswithasemanticspatialmap. increases the task’s difficulty during the training
7612

process. Theinstructionlengthcouldbeametric etal.(2020)proposeenvironment-basedpriorex-
for task difficulty. BabyWalk (Zhu et al., 2020b) ploration,wheretheagentcanonlyexploreapar-
keepincreasingtrainingsamples’instructionlength ticular environment where it is deployed. When
during the training process. Attributes from the utilizinggraph,priorexplorationmayconstructa
trajectorymayalsobeusedtoranktaskdifficulty. map or overview about the unseen environment
Zhangetal.(2021)rearrangetheR2Rdatasetusing toprovideexplicitguidancefornavigation(Chen
the number of rooms each path traverses. They etal.,2021a;Zhouetal.,2021).
found curriculum learning helps smooth the loss
5 RelatedVisual-and-LanguageTasks
landscapeandfindabetterlocaloptima.
ThispaperfocusesonVision-and-LanguageNav-
4.3.3 MultitaskLearning
igation tasks with an emphasis on photo-realistic
DifferentVLNtaskscanbenefitfromeachotherby
environments. 2D map may also be a uesful vir-
cross-taskknowledgetransfer. Wangetal.(2020c)
tual environment for navigation tasks (Vogel and
proposeanenvironment-agnosticmultitasknaviga-
Jurafsky, 2010; Chen and Mooney, 2011; Paz-
tionmodelforbothVLNandNavigationfromDi-
ArgamanandTsarfaty,2019). Syntheticenviron-
alogHistorytasks(Thomasonetal.,2019b). Chap-
ments may also be a substitute for realistic envi-
lotetal.(2020)proposeanattentionmoduletotrain
ronment (MacMahon et al., 2006; Blukis et al.,
amultitasknavigationagenttofollowinstructions
2020). Tellexetal.(2011)proposetoinstantiatea
andanswerquestions(Wijmansetal.,2019a).
probabilisticgraphicalmodelfornaturallanguage
commandsinroboticnavigationandmobilemanip-
4.3.4 InstructionInterpretation
ulationprocess.
Atrajectoryinstructioninterpretedmultipletimes
InVLN,anagentneedstofollowthegivenin-
indifferentwaysmayhelptheagentbetterunder-
structionandevenaskforassistantsinhumanlan-
standitsobjective. LEO(Xiaetal.,2020)leverages
guage. AnagentinVisualNavigationtasksisusu-
andencodesalltheinstructionswithasharedset
ally not required to understand information from
ofparameterstoenhancethetextualunderstanding.
textualmodality. VisualNavigationisaproblemof
LWIT(Nguyenetal.,2021b)interpretstheinstruc-
navigatinganagentfromthecurrentlocationtofind
tions to make it clear to interact with what class
thegoaltarget. Researchershaveachievedsuccess
ofobjects. Shorter,andmoreconciseinstructions
inbothsimulatedenvironments(Zhuetal.,2017;
provide clearer guidance for the agent compared
Mirowski,2019)andrealenvironments(Mirowski
tolonger,semanticallyentangledinstructions,thus
etal.,2018).
Hong et al. (2020b) breaks long instructions into
shorterones,allowingtheagenttotrackprogress 6 ConclusionandFutureDirections
andfocusoneachatomicinstructionindividually.
In this paper, we discuss the importance of VLN
4.4 PriorExploration agentsasapartofsociety,howtheirtasksvaryas
afunctionofcommunicationlevelversustaskob-
Goodperformanceinseenenvironmentsoftencan-
jective,andhowdifferentagentsmaybeevaluated.
not generalize to unseen environments (Hu et al.,
WebroadlyreviewVLNmethodologiesandcate-
2019;Parvanehetal.,2020;Tanetal.,2019). Prior
gorizethem. Thispaperonlydiscussestheseissues
explorationmethodsallowtheagenttoobserveand
broadlyatanintroductorylevel. Inreviewingthese
adapttounseenenvironments,3 bridgingtheperfor-
papers,wecanseetheimmenseprogressthathas
mancegapbetweenseenandunseenenvironments.
alreadybeenmade,aswellasdirectionsthatthis
Wang et al. (2019) introduce a self-supervised
researchtopiccanbeexpandedon.
imitation learning to learn from the agent’s own
Currentmethodsusuallydonotexplicitlyutilize
past, good behaviors. The best navigation path
external knowledge such as objects and general
determined to align the instruction the best by a
house descriptions in Wikipedia. Incorporating
matching critic will be used to update the agent.
knowledgealsoimprovestheinterpretabilityand
Tanetal.(2019)leveragethetestingenvironments
trustofembodiedAI.Moreover,currentlyseveral
to sample and augment paths for adaptation. Fu
navigation agents learn which direction to move
and with what to interact, but there is a last-mile
3Thuspriorexplorationmethodsarenotdirectlycompara-
blewithotherVLNmethods. problemofVLN—howtointeractwithobjects. An-
7613

dersonetal.(2018b)askedwhetherarobotcould ference, VLN agents may observe and store sen-
learnto“Bringmeaspoon”;newresearchmayask sitiveinformationthatcangetleakedormisused.
howarobotcanlearnto“Pickupaspoon”. The Effectivenavigationwithprivacyprotectioniscru-
environmentsalsolackdiversity: mostinteriorter- ciallyimportant. Relevantareassuchasfederated
restrialVLNdataconsistsofAmericanhouses,but learning(Konecˇny` etal.,2016)ordifferentialpri-
never warehouses or hospitals: the places where vacy(Dworketal.,2006)couldalsobestudiedin
theseagentsmaybeofmostuse. VLN domain to preserve the privacy of training
Belowwedetailadditionalfuturedirections: andinferenceenvironments.
Multicultural VLN VLN lacks diversity in
Collaborative VLN Current VLN benchmarks
3D environments: most outdoor VLN datasets
andmethodspredominantlyfocusontaskswhere
useGoogle StreetView recorded inmajor Amer-
only one agent navigates, yet complicated real-
icancities,butlacksdataindevelopingcountries.
worldscenariosmayrequireseveralrobotscollabo-
Agents trained on American data face potential
rating. Multi-agentVLNtasksrequiredevelopment
generalization problems in other city or housing
inswarmintelligence,informationcommunication,
layouts. Futureworkshouldexploremorediverse
and performance evaluation. MeetUp! (Ilinykh
environmentsacrossmultipleculturesandregions.
et al., 2019) is a two-player coordination game
Multilingual VLN datasets (Yan et al., 2020; Ku
where players move in a visual environment to
etal.,2020)couldbegoodresourcestostudymulti-
find each other. VLN studies the relationship be-
culturaldifferencesfromthelinguisticperspective.
tweenthehumanandtheenvironmentinFigure1,
yetherehumansareoraclessimplyobserving(but
notactingon)theenvironment. Collaborationbe-
References
tween humans and robots is crucial for them to
DongAn,YuankaiQi,YanHuang,QiWu,LiangWang,
worktogetherasteams(e.g.,aspersonalassistants
and Tieniu Tan. 2021. Neighbor-view enhanced
orhelpinginconstruction). Futureworkmaytarget
model for vision and language navigation. arXiv
at collaborative VLN between multiple agents or preprintarXiv:2107.07201.
betweenhumanandagents.
PeterAnderson,AngelChang,DevendraSinghChap-
SimulationtoReality Thereisaperformanceloss
lot, Alexey Dosovitskiy, Saurabh Gupta, Vladlen
whentransferredtoreal-liferobotnavigation(An- Koltun,JanaKosecka,JitendraMalik,RoozbehMot-
dersonetal.,2020). Realrobotsfunctionincontin- taghi, Manolis Savva, et al. 2018a. On evalua-
tionofembodiednavigationagents. arXivpreprint
uousspace,butmostsimulatorsonlyallowagents
arXiv:1807.06757.
to “hop” through a pre-defined navigation graph
whichisunrealisticforthreereasons(Krantzetal., PeterAnderson,AyushShrivastava,DeviParikh,Dhruv
2020). Navigation graphs assume: (1) perfect Batra, and Stefan Lee. 2019a. Chasing ghosts: In-
struction following as bayesian state tracking. In
localization—intherealworlditisanoisyestimate;
AdvancesinNeuralInformationProcessingSystems
(2)oraclenavigation—realrobotscannot“teleport”
(NeurIPS).
toanewnode;(3)knowntopology—inrealityan
agentmaynothaveaccesstoapresetlistofnaviga- PeterAnderson,AyushShrivastava,DeviParikh,Dhruv
Batra, andStefanLee.2019b. Chasingghosts: In-
blenodes. Continuousimplementationsofrealistic
struction following as bayesian state tracking. Ad-
environmentsmaycontainpatchesoftheimages,
vances in Neural Information Processing Systems,
be blurred, or have parallax errors, making them 32:371–381.
unrealistic. A simulation that is based on both
PeterAnderson,AyushShrivastava,JoanneTruong,Ar-
a 3D model and realistic imagery could improve
jun Majumdar, Devi Parikh, Dhruv Batra, and Ste-
thematchbetweenvirtualsensors(insimulation)
fanLee.2020. Sim-to-realtransferforvision-and-
andrealsensors. Lastly,mostsimulatorsassumea languagenavigation. InConferenceonRobotLearn-
staticenvironmentonlychangedbytheagent. This ing(CoRL).
doesnotaccountforotherdynamicssuchaspeople
Peter Anderson, Qi Wu, Damien Teney, Jake Bruce,
walkingorobjectsmoving,nordoesitaccountfor
MarkJohnson,NikoSünderhauf,IanReid,Stephen
lightingconditionsthroughtheday. VLNenviron- Gould,andAntonvandenHengel.2018b. Vision-
mentswithprobabilistictransitionfunctionsmay and-language navigation: Interpreting visually-
grounded navigation instructions in real environ-
alsonarrowthegapbetweensimulationandreality.
ments. InProceedingsoftheIEEEConferenceon
Ethics & Privacy During both training and in- ComputerVisionandPatternRecognition(CVPR).
7614

ShurjoBanerjee,JesseThomason,andJasonJ.Corso. ShizheChen,Pierre-LouisGuhur,CordeliaSchmid,and
2020. TheRobotSlangBenchmark: Dialog-guided IvanLaptev.2021b. Historyawaremultimodaltrans-
robotlocalizationandnavigation. InConferenceon former for vision-and-language navigation. arXiv
RobotLearning(CoRL). preprintarXiv:2110.13309.
Yoshua Bengio, Jérôme Louradour, Ronan Collobert,
Ta-ChungChi,MinminShen,MihailEric,Seokhwan
and Jason Weston. 2009. Curriculum learning. In
Kim, and Dilek Hakkani-tur. 2020. Just ask: An
Proceedingsofthe26thannualinternationalconfer-
interactive learning framework for vision and lan-
enceonmachinelearning,pages41–48.
guagenavigation. InAAAIConferenceonArtificial
Intelligence.
ValtsBlukis,NatalyBrukhim,AndrewBennett,RossA.
Knepper,andYoavArtzi.2018. Followinghigh-level
navigation instructions on a simulated quadcopter AbhishekDas,SamyakDatta,GeorgiaGkioxari,Stefan
with imitation learning. In Robotics: Science and Lee,DeviParikh,andDhruvBatra.2018. Embodied
Systems(RSS). questionanswering. InProceedingsoftheIEEECon-
ferenceonComputerVisionandPatternRecognition,
ValtsBlukis,YannickTerme,EyvindNiklasson,RossA. pages1–10.
Knepper, and Yoav Artzi. 2019. Learning to map
naturallanguageinstructionstophysicalquadcopter HarmdeVries,KurtShuster,DhruvBatra,DeviParikh,
control using simulated flight. In Conference on Jason Weston, and Douwe Kiela. 2018. Talk the
RobotLearning(CoRL). walk: Navigating new york city through grounded
dialogue.
ValtsBlukis,YannickTerme,EyvindNiklasson,RossA.
Knepper, and Yoav Artzi. 2020. Learning to map
Zhiwei Deng, Karthik Narasimhan, and Olga Rus-
naturallanguageinstructionstophysicalquadcopter
sakovsky.2020. Evolving graphicalplanner: Con-
control using simulated flight. In Proceedings of
textualglobalplanningforvision-and-languagenavi-
theConferenceonRobotLearning,volume100of
gation. AdvancesinNeuralInformationProcessing
ProceedingsofMachineLearningResearch,pages
Systems,2020-December.
1415–1438.PMLR.
FranciscoBonin-Font,AlbertoOrtiz,andGabrielOliver. Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
2008. Visualnavigationformobilerobots: Asurvey. KristinaToutanova.2019. Bert: Pre-trainingofdeep
Journalofintelligentandroboticsystems,53(3):263– bidirectionaltransformersforlanguageunderstand-
296. ing. InNAACL-HLT(1).
AngelChang,AngelaDai,ThomasFunkhouser,Maciej
Alexey Dosovitskiy, Lucas Beyer, Alexander
Halber, MatthiasNiessner, ManolisSavva, Shuran
Kolesnikov, Dirk Weissenborn, Xiaohua Zhai,
Song,AndyZeng,andYindaZhang.2017. Matter-
Thomas Unterthiner, Mostafa Dehghani, Matthias
port3D:LearningfromRGB-Ddatainindoorenvi-
Minderer,GeorgHeigold,SylvainGelly,etal.2020.
ronments. International Conference on 3D Vision
An image is worth 16x16 words: Transformers
(3DV).
for image recognition at scale. In International
ConferenceonLearningRepresentations.
DevendraSinghChaplot,LisaLee,RuslanSalakhutdi-
nov,DeviParikh,andDhruvBatra.2020. Embodied
multimodal multitask learning. In Proceedings of CynthiaDwork, FrankMcSherry, KobbiNissim, and
theTwenty-NinthInternationalJointConferenceon AdamSmith.2006. Calibratingnoisetosensitivity
ArtificialIntelligence,IJCAI-20.InternationalJoint inprivatedataanalysis. InTheoryofcryptography
ConferencesonArtificialIntelligenceOrganization. conference,pages265–284.Springer.
David Chen and Raymond Mooney. 2011. Learning Daniel Fried, Ronghang Hu, Volkan Cirik, Anna
tointerpretnaturallanguagenavigationinstructions Rohrbach,JacobAndreas,Louis-PhilippeMorency,
fromobservations. InAAAIConferenceonArtificial Taylor Berg-Kirkpatrick, Kate Saenko, Dan Klein,
Intelligence. and Trevor Darrell. 2018. Speaker-follower mod-
els for vision-and-language navigation. In Neural
Howard Chen, Alane Suhr, Dipendra Misra, Noah
InformationProcessingSystems(NeurIPS).
Snavely,andYoavArtzi.2019. Touchdown: Natural
languagenavigationandspatialreasoninginvisual
JustinFu,AnoopKorattikara,SergeyLevine,andSergio
streetenvironments. In2019IEEE/CVFConference
Guadarrama.2019. Fromlanguagetogoals: Inverse
onComputerVisionandPatternRecognition(CVPR),
reinforcementlearningforvision-basedinstruction
pages12530–12539.
following. arXivpreprintarXiv:1902.07742.
Kevin Chen, Junshen K Chen, Jo Chuang, Marynel
Vázquez, andSilvioSavarese.2021a. Topological Tsu-Jui Fu, Xin Eric Wang, Matthew Peterson, Scott
planningwithtransformersforvision-and-language Grafton,MiguelEckstein,andWilliamYangWang.
navigation. InProceedingsoftheIEEE/CVFConfer- 2020. Counterfactual vision-and-language naviga-
enceonComputerVisionandPatternRecognition, tionviaadversarialpathsampler. InEuropeanCon-
pages11276–11286. ferenceonComputerVision(ECCV).
7615

Chen Gao, Jinyu Chen, Si Liu, Luting Wang, Qiong ProceedingsoftheIEEE/CVFConferenceonCom-
Zhang,andQiWu.2021. Room-and-objectaware puterVisionandPatternRecognition(CVPR),pages
knowledgereasoningforremoteembodiedreferring 1643–1653.
expression. InProceedingsoftheIEEE/CVFConfer-
RonghangHu,DanielFried,AnnaRohrbach,DanKlein,
enceonComputerVisionandPatternRecognition,
Trevor Darrell, and Kate Saenko. 2019. Are you
pages3064–3073.
looking? groundingtomultiplemodalitiesinvision-
XiaofengGao,QiaoziGao,RanGong,KaixiangLin, and-languagenavigation. InProceedingsofthe57th
GovindThattai,andGauravSSukhatme.2022. Dial- AnnualMeetingoftheAssociationforComputational
fred: Dialogue-enabledagentsforembodiedinstruc- Linguistics,pages6551–6557,Florence,Italy.Asso-
tionfollowing. arXivpreprintarXiv:2202.13330. ciationforComputationalLinguistics.
HaoshuoHuang,VihanJain,HarshMehta,Alexander
Daniel Gordon, Aniruddha Kembhavi, Mohammad
Ku, Gabriel Magalhaes, Jason Baldridge, and Eu-
Rastegari, Joseph Redmon, Dieter Fox, and Ali
geneIe.2019. Transferablerepresentationlearning
Farhadi. 2018. Iqa: Visual question answering in
invision-and-languagenavigation. InProceedings
interactiveenvironments. InProceedingsoftheIEEE
oftheIEEE/CVFInternationalConferenceonCom-
conferenceoncomputervisionandpatternrecogni-
puterVision(ICCV).
tion,pages4089–4098.
GabrielIlharco,VihanJain,AlexanderKu,EugeneIe,
Pierre-LouisGuhur,MakarandTapaswi,ShizheChen,
andJasonBaldridge.2019. Generalevaluationforin-
Ivan Laptev, and Cordelia Schmid. 2021. Airbert:
structionconditionednavigationusingdynamictime
In-domainpretrainingforvision-and-languagenav-
warping. arXivpreprintarXiv:1907.05446.
igation. In Proceedings of the IEEE/CVF Interna-
tionalConferenceonComputerVision(ICCV),pages Nikolai Ilinykh, Sina Zarrieß, and David Schlangen.
1634–1643. 2019. Meetup! a corpus of joint activity dia-
logues in a visual environment. arXiv preprint
WeituoHao,ChunyuanLi,XiujunLi,LawrenceCarin, arXiv:1907.05084.
andJianfengGao.2020. Towardslearningageneric
agent for vision-and-language navigation via pre- Muhammad Zubair Irshad, Chih-Yao Ma, and Zsolt
training. ConferenceonComputerVisionandPattern Kira. 2021. Hierarchical cross-modal agent for
Recognition(CVPR). robotics vision-and-language navigation. arXiv
preprintarXiv:2104.10674.
KaimingHe,XiangyuZhang,ShaoqingRen,andJian
VihanJain,GabrielMagalhaes,AlexanderKu,Ashish
Sun.2016. Deepresiduallearningforimagerecog-
Vaswani, Eugene Ie, and Jason Baldridge. 2019.
nition. In Proceedings of the IEEE conference on
Stayonthepath: Instructionfidelityinvision-and-
computervisionandpatternrecognition,pages770–
languagenavigation. InProceedingsofthe57thAn-
778.
nualMeetingoftheAssociationforComputational
KejiHe,YanHuang,QiWu,JianhuaYang,DongAn, Linguistics,pages1862–1872,Florence,Italy.Asso-
ShuanglinSima,andLiangWang.2021. Landmark- ciationforComputationalLinguistics.
rxr: Solving vision-and-language navigation with
LiyimingKe,XiujunLi,YonatanBisk,AriHoltzman,
fine-grainedalignmentsupervision. InNeurIPS.
ZheGan,JingjingLiu,JianfengGao,YejinChoi,and
Siddhartha Srinivasa. 2019. Tactical rewind: Self-
Karl Moritz Hermann, Mateusz Malinowski, Piotr
correctionviabacktrackinginvision-and-language
Mirowski,AndrasBanki-Horvath,KeithAnderson,
navigation. In Proceedings of the IEEE Confer-
and Raia Hadsell. 2020. Learning to follow direc-
ence on Computer Vision and Pattern Recognition
tionsinstreetview. InAAAIConferenceonArtificial
(CVPR).
Intelligence.
Jing Yu Koh, Honglak Lee, Yinfei Yang, Jason
YicongHong,CristianRodriguez,YuankaiQi,QiWu,
Baldridge,andPeterAnderson.2021. Pathdreamer:
and Stephen Gould. 2020a. Language and visual
A world model for indoor navigation. In Proceed-
entity relationship graph for agent navigation. Ad-
ingsoftheIEEE/CVFInternationalConferenceon
vances in Neural Information Processing Systems,
ComputerVision(ICCV),pages14738–14748.
33:7685–7696.
EricKolve,RoozbehMottaghi,WinsonHan,EliVan-
YicongHong,CristianRodriguez,QiWu,andStephen derBilt,LucaWeihs,AlvaroHerrasti,DanielGordon,
Gould. 2020b. Sub-instruction aware vision-and- Yuke Zhu, Abhinav Gupta, and Ali Farhadi. 2017.
language navigation. In Proceedings of the 2020 AI2-THOR:AnInteractive3DEnvironmentforVi-
Conference on Empirical Methods in Natural Lan- sualAI. arXiv.
guageProcessing(EMNLP),pages3360–3376,On-
line.AssociationforComputationalLinguistics. JakubKonecˇny`,HBrendanMcMahan,FelixXYu,Pe-
ter Richtárik, Ananda Theertha Suresh, and Dave
YicongHong,QiWu,YuankaiQi,CristianRodriguez- Bacon.2016. Federatedlearning: Strategiesforim-
Opazo, and Stephen Gould. 2021. Vln bert: A re- proving communication efficiency. arXiv preprint
currentvision-and-languagebertfornavigation. In arXiv:1610.05492.
7616

JacobKrantz,AaronGokaslan,DhruvBatra,StefanLee, Matt MacMahon, Brian Stankiewicz, and Benjamin
andOleksandrMaksymets.2021. Waypointmodels Kuipers.2006. Walkthetalk: Connectinglanguage,
forinstruction-guidednavigationincontinuousenvi- knowledge, and action in route instructions. Def,
ronments. InProceedingsoftheIEEE/CVFInterna- 2(6):4.
tionalConferenceonComputerVision(ICCV),pages
15162–15171. ArjunMajumdar,AyushShrivastava,StefanLee,Peter
Anderson,DeviParikh,andDhruvBatra.2020. Im-
JacobKrantz,ErikWijmans,ArjunMajumdar,Dhruv provingvision-and-languagenavigationwithimage-
Batra,andStefanLee.2020. Beyondthenav-graph: textpairsfromtheweb. InProceedingsoftheEuro-
Vision-and-languagenavigationincontinuousenvi- peanConferenceonComputerVision(ECCV).
ronments. InComputerVision–ECCV2020,pages
104–120,Cham.SpringerInternationalPublishing. Manolis Savva*, Abhishek Kadian*, Oleksandr
Maksymets*,YiliZhao,ErikWijmans,BhavanaJain,
AlexanderKu,PeterAnderson,RomaPatel,EugeneIe, JulianStraub,JiaLiu,VladlenKoltun,JitendraMa-
and Jason Baldridge. 2020. Room-Across-Room: lik, Devi Parikh, and Dhruv Batra. 2019. Habitat:
Multilingual vision-and-language navigation with APlatformforEmbodiedAIResearch. InProceed-
densespatiotemporalgrounding. InConferenceon ingsoftheIEEE/CVFInternationalConferenceon
EmpiricalMethodsforNaturalLanguageProcessing ComputerVision(ICCV).
(EMNLP).
HarshMehta,YoavArtzi,JasonBaldridge,EugeneIe,
FedericoLandi,LorenzoBaraldi,MarcellaCornia,Mas- andPiotrMirowski.2020. Retouchdown: Releasing
similiano Corsini, and Rita Cucchiara. 2020. Per- touchdownonStreetLearnasapublicresourcefor
ceive,transform,andact: Multi-modalattentionnet- languagegroundingtasksinstreetview. InProceed-
worksforvision-and-languagenavigation. ingsoftheThirdInternationalWorkshoponSpatial
LanguageUnderstanding,pages56–62,Online.As-
FedericoLandi,LorenzoBaraldi,MassimilianoCorsini,
sociationforComputationalLinguistics.
and Rita Cucchiara. 2019. Embodied vision-and-
languagenavigationwithdynamicconvolutionalfil-
PiotrMirowski.2019. Learningtonavigate. In1stIn-
ters. InProceedingsoftheBritishMachineVision
ternationalWorkshoponMultimodalUnderstanding
Conference.
andLearningforEmbodiedApplications,MULEA
’19,page25,NewYork,NY,USA.Associationfor
Xiujun Li, Chunyuan Li, Qiaolin Xia, Yonatan Bisk,
ComputingMachinery.
Asli Celikyilmaz, Jianfeng Gao, Noah Smith, and
YejinChoi.2019. Robustnavigationwithlanguage
PiotrMirowski, AndrasBanki-Horvath, KeithAnder-
pretraining and stochastic sampling. In Empirical
son, Denis Teplyashin, Karl Moritz Hermann, Ma-
MethodsinNaturalLanguageProcessing(EMNLP).
teuszMalinowski, MatthewKoichiGrimes, Karen
Simonyan,KorayKavukcuoglu,AndrewZisserman,
XiangruLin,GuanbinLi,andYizhouYu.2021. Scene-
etal.2019. Thestreetlearnenvironmentanddataset.
intuitiveagentforremoteembodiedvisualground-
arXivpreprintarXiv:1903.01292.
ing. In Proceedings of the IEEE/CVF Conference
onComputerVisionandPatternRecognition,pages
Piotr Mirowski, Matthew Koichi Grimes, Mateusz
7036–7045.
Malinowski, Karl Moritz Hermann, Keith Ander-
Chong Liu, Fengda Zhu, Xiaojun Chang, Xiaodan son, Denis Teplyashin, Karen Simonyan, Koray
Liang, Zongyuan Ge, and Yi-Dong Shen. 2021. Kavukcuoglu,AndrewZisserman,andRaiaHadsell.
Vision-languagenavigationwithrandomenvironmen- 2018. Learningtonavigateincitieswithoutamap.
talmixup. InProceedingsoftheIEEE/CVFInterna- InProceedingsofthe32ndInternationalConference
tionalConferenceonComputerVision(ICCV),pages onNeuralInformationProcessingSystems,NIPS’18,
1644–1654. page2424–2435,RedHook,NY,USA.CurranAsso-
ciatesInc.
JiasenLu, DhruvBatra, DeviParikh, andStefanLee.
2019. Vilbert: Pretrainingtask-agnosticvisiolinguis- DipendraMisra,AndrewBennett,ValtsBlukis,Eyvind
ticrepresentationsforvision-and-languagetasks. In Niklasson, Max Shatkhin, and Yoav Artzi. 2018.
AdvancesinNeuralInformationProcessingSystems, Mappinginstructionstoactionsin3denvironments
volume32.CurranAssociates,Inc. with visual goal prediction. In Proceedings of the
2018ConferenceonEmpiricalMethodsinNatural
Chih-YaoMa,JiasenLu,ZuxuanWu,GhassanAlRegib, LanguageProcessing,pages2667–2678.
Zsolt Kira, Richard Socher, and Caiming Xiong.
2019a. Self-monitoringnavigationagentviaauxil- Abhinav Moudgil, Arjun Majumdar, Harsh Agrawal,
iaryprogressestimation. InInternationalConference Stefan Lee, and Dhruv Batra. 2021. Soat: A
onLearningRepresentations(ICLR). scene-andobject-awaretransformerforvision-and-
languagenavigation. InNeurIPS.
Chih-YaoMa,ZuxuanWu,GhassanAlRegib,Caiming
Xiong,andZsoltKira.2019b. Theregretfulagent: Anjali Narayan-Chen, Prashant Jayannavar, and Ju-
Heuristic-aidednavigationthroughprogressestima- lia Hockenmaier. 2019. Collaborative dialogue in
tion. In Proceedings of the IEEE Conference on Minecraft. InProceedingsofthe57thAnnualMeet-
ComputerVisionandPatternRecognition(CVPR). ingoftheAssociationforComputationalLinguistics,
7617

Florence,Italy.AssociationforComputationalLin- Yuankai Qi, Qi Wu, Peter Anderson, Xin Wang,
guistics. William Yang Wang, Chunhua Shen, and Anton
van den Hengel. 2020b. Reverie: Remote embod-
KhanhNguyen,YonatanBisk,andHalDauméIIIau2. iedvisualreferringexpressioninrealindoorenviron-
2021a. Learningwhenandwhattoask:ahierarchical ments. InProceedingsoftheIEEEConferenceon
reinforcementlearningframework. ComputerVisionandPatternRecognition(CVPR).
Khanh Nguyen and Hal Daumé III. 2019. Help, Alec Radford, Jeff Wu, Rewon Child, David Luan,
anna! visualnavigationwithnaturalmultimodalas- DarioAmodei,andIlyaSutskever.2019. Language
sistanceviaretrospectivecuriosity-encouragingimi- modelsareunsupervisedmultitasklearners.
tationlearning. InProceedingsofthe2019Confer-
enceonEmpiricalMethodsinNaturalLanguagePro- HomeroRomanRoman,YonatanBisk,JesseThomason,
cessingandthe9thInternationalJointConference Asli Celikyilmaz, and Jianfeng Gao. 2020. RMM:
onNaturalLanguageProcessing(EMNLP-IJCNLP), Arecursivementalmodelfordialognavigation. In
pages684–695,HongKong,China.Associationfor FindingsofEmpiricalMethodsinNaturalLanguage
ComputationalLinguistics. Processing(EMNLPFindings).
KhanhNguyen,DebadeeptaDey,ChrisBrockett,and Mohit Shridhar, Jesse Thomason, Daniel Gordon,
Bill Dolan. 2019. Vision-based navigation with YonatanBisk,WinsonHan,RoozbehMottaghi,Luke
language-basedassistanceviaimitationlearningwith Zettlemoyer, and Dieter Fox. 2020. ALFRED: A
indirect intervention. In The IEEE Conference on Benchmark for Interpreting Grounded Instructions
ComputerVisionandPatternRecognition(CVPR). for Everyday Tasks. In The IEEE Conference on
ComputerVisionandPatternRecognition(CVPR).
Van-QuangNguyen,MasanoriSuganuma,andTakayuki
Okatani. 2021b. Look wide and interpret twice: ShuranSong,FisherYu,AndyZeng,AngelXChang,
Improving performance on interactive instruction- ManolisSavva,andThomasFunkhouser.2017. Se-
followingtasks. arXivpreprintarXiv:2106.00596. manticscenecompletionfromasingledepthimage.
CVPR.
AishwaryaPadmakumar,JesseThomason,AyushShri-
vastava,PatrickLange,AnjaliNarayan-Chen,Span- JulianStraub,ThomasWhelan,LingniMa,YufanChen,
dana Gella, Robinson Piramithu, Gokhan Tur, and Erik Wijmans, Simon Green, Jakob J. Engel, Raul
Dilek Hakkani-Tur. 2021. Teach: Task-driven em- Mur-Artal,CarlRen,ShobhitVerma,AntonClark-
bodiedagentsthatchat. son,MingfeiYan,BrianBudge,YajieYan,Xiaqing
Pan,JuneYon,YuyangZou,KimberlyLeon,Nigel
AminParvaneh,EhsanAbbasnejad,DamienTeney,Qin- Carter,JesusBriales,TylerGillingham,EliasMueg-
fengShi,andAntonvandenHengel.2020. Counter- gler, Luis Pesqueira, Manolis Savva, Dhruv Batra,
factualvision-and-languagenavigation: Unravelling HaukeM.Strasdat,RenzoDeNardi,MichaelGoe-
theunseen. InNeurIPS. sele, Steven Lovegrove, and Richard Newcombe.
2019. TheReplicadataset:Adigitalreplicaofindoor
AlexanderPashevich,CordeliaSchmid,andChenSun. spaces. arXivpreprintarXiv:1906.05797.
2021. Episodictransformerforvision-and-language
navigation. InProceedingsoftheIEEE/CVFInterna- Alane Suhr, Claudia Yan, Jack Schluger, Stanley Yu,
tionalConferenceonComputerVision(ICCV),pages Hadi Khader, Marwa Mouallem, Iris Zhang, and
15942–15952. Yoav Artzi. 2019. Executing instructions in situ-
ated collaborative interactions. In Proceedings of
Tzuf Paz-Argaman and Reut Tsarfaty. 2019. Run the2019ConferenceonEmpiricalMethodsinNatu-
throughthestreets: Anewdatasetandbaselinemod- ralLanguageProcessingandthe9thInternational
els for realistic urban navigation. arXiv preprint JointConferenceonNaturalLanguageProcessing
arXiv:1909.08970. (EMNLP-IJCNLP),pages2119–2130,HongKong,
China.AssociationforComputationalLinguistics.
YuankaiQi,ZizhengPan,YicongHong,Ming-Hsuan
Yang,AntonvandenHengel,andQiWu.2021. The Q.Sun,Y.Zhuang,Z.Chen,Y.Fu,andX.Xue.2021.
roadtoknow-where: Anobject-and-roominformed Depth-guidedadainandshiftattentionnetworkfor
sequential bert for indoor vision-language naviga- vision-and-language navigation. In 2021 IEEE In-
tion. InProceedingsoftheIEEE/CVFInternational ternational Conference on Multimedia and Expo
ConferenceonComputerVision(ICCV),pages1655– (ICME),pages1–6,LosAlamitos,CA,USA.IEEE
1664. ComputerSociety.
Yuankai Qi, Zizheng Pan, Shengping Zhang, Anton Andrew Szot, Alex Clegg, Eric Undersander, Erik
van den Hengel, and Qi Wu. 2020a. Object-and- Wijmans, Yili Zhao, John Turner, Noah Maestre,
actionawaremodelforvisuallanguagenavigation. Mustafa Mukadam, Devendra Chaplot, Oleksandr
In Computer Vision–ECCV 2020: 16th European Maksymets, Aaron Gokaslan, Vladimir Vondrus,
Conference,Glasgow,UK,August23–28,2020,Pro- SameerDharur,FranziskaMeier,WojciechGaluba,
ceedings,PartX16,pages303–317.Springer. AngelChang,ZsoltKira,VladlenKoltun,Jitendra
7618

Malik,ManolisSavva,andDhruvBatra.2021. Habi- Xin Wang, Qiuyuan Huang, Asli Celikyilmaz, Jian-
tat2.0: Traininghomeassistantstorearrangetheir fengGao,DinghanShen,Yuan-FangWang,William
habitat. arXivpreprintarXiv:2106.14405. Wang, and Lei Zhang. 2019. Reinforced cross-
modalmatchingandself-supervisedimitationlearn-
HaoTan,LichengYu,andMohitBansal.2019. Learn- ingforvision-languagenavigation. InProceedings
ingtonavigateunseenenvironments: Backtransla- of the CVF/IEEE Conference on Computer Vision
tionwithenvironmentaldropout. InProceedingsof and Pattern Recognition, Long Beach, CA, USA.
the2019ConferenceoftheNorthAmericanChap- CVF/IEEE.
teroftheAssociationforComputationalLinguistics:
HumanLanguageTechnologies,Volume1(Longand Xin Wang, Wenhan Xiong, Hongmin Wang, and
ShortPapers),pages2610–2621,Minneapolis,Min- William Yang Wang. 2018. Look before you leap:
nesota.AssociationforComputationalLinguistics. Bridgingmodel-freeandmodel-basedreinforcement
learningforplanned-aheadvision-and-languagenav-
SinanTan,MengmengGe,DiGuo,HuapingLiu,and igation. ProceedingsoftheEuropeanConferenceon
FuchunSun.2022. Self-supervised3dsemanticrep- ComputerVision(ECCV2018).
resentationlearningforvision-and-languagenaviga-
tion. arXivpreprintarXiv:2201.10788. XinEricWang,VihanJain,EugeneIe,WilliamYang
Wang, Zornitsa Kozareva, and Sujith Ravi. 2020c.
Stefanie Tellex, Thomas Kollar, Steven Dickerson, Environment-agnosticmultitasklearningfornatural
Matthew Walter, Ashis Banerjee, Seth Teller, and languagegroundednavigation. InEuropeanConfer-
NicholasRoy.2011. Understandingnaturallanguage enceonComputerVision(ECCV’20).
commandsforroboticnavigationandmobilemanipu-
lation. InAAAIConferenceonArtificialIntelligence. ErikWijmans, SamyakDatta, OleksandrMaksymets,
AbhishekDas,GeorgiaGkioxari,StefanLee,Irfan
Jesse Thomason, Daniel Gordon, and Yonatan Bisk. Essa,DeviParikh,andDhruvBatra.2019a. Embod-
2019a. Shiftingthebaseline: Singlemodalityperfor- ied Question Answering in Photorealistic Environ-
manceonvisualnavigation&QA. InProceedings mentswithPointCloudPerception. InProceedings
ofthe2019ConferenceoftheNorthAmericanChap- oftheIEEEConferenceonComputerVisionandPat-
teroftheAssociationforComputationalLinguistics: ternRecognition(CVPR).
HumanLanguageTechnologies,Volume1(Longand
ShortPapers),pages1977–1983,Minneapolis,Min- ErikWijmans, AbhishekKadian, AriMorcos, Stefan
nesota.AssociationforComputationalLinguistics. Lee, Irfan Essa, Devi Parikh, Manolis Savva, and
DhruvBatra.2019b. Dd-ppo: Learningnear-perfect
JesseThomason,MichaelMurray,MayaCakmak,and pointgoalnavigatorsfrom2.5billionframes. InIn-
LukeZettlemoyer.2019b. Vision-and-dialognaviga- ternationalConferenceonLearningRepresentations.
tion. InConferenceonRobotLearning(CoRL).
Yi Wu, Yuxin Wu, Georgia Gkioxari, and Yuandong
Arun Balajee Vasudevan, Dengxin Dai, and Luc Tian. 2018. Building generalizable agents with a
VanGool.2021. Talk2nav: Long-rangevision-and- realisticandrich3denvironment.
languagenavigationwithdualattentionandspatial
memory. InternationalJournalofComputerVision, FeiXia,AmirR.Zamir,ZhiyangHe,AlexanderSax,
129(1):246–266. JitendraMalik,andSilvioSavarese.2018. Gibson
env: Real-worldperceptionforembodiedagents. In
AdamVogelandDanJurafsky.2010. Learningtofollow ProceedingsoftheIEEEConferenceonComputer
navigationaldirections. InProceedingsofthe48th VisionandPatternRecognition(CVPR).
annualmeetingoftheassociationforcomputational
linguistics,pages806–814. Qiaolin Xia, Xiujun Li, Chunyuan Li, Yonatan Bisk,
ZhifangSui,JianfengGao,YejinChoi,andNoahA.
HanqingWang,WenguanWang,WeiLiang,Caiming Smith. 2020. Multi-view learning for vision-and-
Xiong, andJianbingShen.2021. Structuredscene languagenavigation.
memoryforvision-languagenavigation. InProceed-
ingsoftheIEEE/CVFConferenceonComputerVi- An Yan, Xin Eric Wang, Jiangtao Feng, Lei Li, and
sionandPatternRecognition(CVPR),pages8455– William Yang Wang. 2020. Cross-lingual vision-
8464. languagenavigation.
Hanqing Wang, Wenguan Wang, Tianmin Shu, Wei Jiwen Zhang, Zhongyu Wei, Jianqing Fan, and Jiajie
Liang,andJianbingShen.2020a. Activevisualinfor- Peng. 2021. Curriculum learning for vision-and-
mationgatheringforvision-languagenavigation. In languagenavigation. InNeurIPS.
EuropeanConferenceonComputerVision(ECCV).
WeixiaZhang,ChaoMa,QiWu,andXiaokangYang.
Hu Wang, Qi Wu, and Chunhua Shen. 2020b. Soft 2020a. Language-guidednavigationviacross-modal
expertrewardlearningforvision-and-languagenavi- groundingandalternateadversariallearning. IEEE
gation. InEuropeanConferenceonComputerVision TransactionsonCircuitsandSystemsforVideoTech-
(ECCV’20). nology.
7619

YuboZhang,HaoTan,andMohitBansal.2020b. Diag-
nosingtheenvironmentbiasinvision-and-language
navigation. InProceedingsoftheTwenty-NinthInter-
nationalJointConferenceonArtificialIntelligence,
IJCAI-20,pages890–897.InternationalJointConfer-
encesonArtificialIntelligenceOrganization. Main
track.
Ming Zhao, Peter Anderson, Vihan Jain, Su Wang,
AlexanderKu,JasonBaldridge,andEugeneIe.2021.
Ontheevaluationofvision-and-languagenavigation
instructions. InProceedingsofthe16thConference
oftheEuropeanChapteroftheAssociationforCom-
putational Linguistics: Main Volume, pages 1302–
1316.
XinzheZhou,WeiLiu,andYadongMu.2021. Rethink-
ing the spatial route prior in vision-and-language
navigation.
FengdaZhu,XiwenLiang,YiZhu,QizhiYu,Xiaojun
Chang,andXiaodanLiang.2021a. Soon: Scenario
orientedobjectnavigationwithgraph-basedexplo-
ration. InProceedingsoftheIEEE/CVFConference
onComputerVisionandPatternRecognition,pages
12689–12699.
Fengda Zhu, Yi Zhu, Xiaojun Chang, and Xiaodan
Liang.2020a. Vision-languagenavigationwithself-
supervisedauxiliaryreasoningtasks. InProceedings
of the IEEE/CVF Conference on Computer Vision
andPatternRecognition(CVPR).
WangZhu,HexiangHu,JiachengChen,ZhiweiDeng,
Vihan Jain, Eugene Ie, and Fei Sha. 2020b. Baby-
Walk: Goingfartherinvision-and-languagenaviga-
tion by taking baby steps. In Proceedings of the
58thAnnualMeetingoftheAssociationforCompu-
tationalLinguistics,pages2539–2556.Association
forComputationalLinguistics.
WanrongZhu,YuankaiQi,PradyumnaNarayana,Ka-
zoo Sone, Sugato Basu, Xin Eric Wang, Qi Wu,
Miguel Eckstein, and William Yang Wang. 2021b.
Diagnosingvision-and-languagenavigation: What
reallymatters.
Yi Zhu, Yue Weng, Fengda Zhu, Xiaodan Liang,
Qixiang Ye, Yutong Lu, and Jianbin Jiao. 2021c.
Self-motivatedcommunicationagentforreal-world
vision-dialog navigation. In Proceedings of the
IEEE/CVF International Conference on Computer
Vision(ICCV),pages1594–1603.
Yi Zhu, Fengda Zhu, Zhaohuan Zhan, Bingqian Lin,
Jianbin Jiao, Xiaojun Chang, and Xiaodan Liang.
2020c. Vision-dialognavigationbyexploringcross-
modal memory. In Proceedings of the IEEE/CVF
ConferenceonComputerVisionandPatternRecog-
nition,pages10730–10739.
YukeZhu,RoozbehMottaghi,EricKolve,JosephJLim,
Abhinav Gupta, Li Fei-Fei, and Ali Farhadi. 2017.
Target-drivenvisualnavigationinindoorscenesus-
ingdeepreinforcementlearning. In2017IEEEin-
ternationalconferenceonroboticsandautomation
(ICRA),pages3357–3364.IEEE.
7620

A DatasetDetails meshes. Matterport3Ddataset(Changetal.,2017)
isalsointegratedintotheGibsonsimulator.
Here in Table 2, we introduce more information
House3D(Wuetal.,2018)convertsSUNCG’s
about the datasets. Compared with the number
static environment into a virtual environment,
of the datasets, the simulators are limited. More
where the agent can navigate with physical con-
specifically,mostindoordatasetsarebasedonMat-
straints (e.g. it cannot pass through walls or ob-
terport3Dandmostoutdoordatasetsarebasedon
jects).
GoogleStreetView. Also,moredatasetsareabout
LANI(Misraetal.,2018)isa3Dsimulatorbuilt
indoorenvironmentsratherthanoutdoorenviron-
inUnity3Dplatform. TheenvironmentinLANIis
ments. Outdoor environments are usually more
afenced,square,grassfieldcontainingrandomly
complexandcontainmoreobjectscomparedwith
placedlandmarks. Anagentneedstonavigatebe-
indoorenvironments.
tween landmarks following the natural language
instruction. Dronenavigationtasks(Blukisetal.,
B Simulator
2018,2019)arealsobuiltbasedonLANI.
Thevirtualfeaturesofthedatasetaredeeplycon- Currently, most datasets and simulators focus
nected with the simulator in which datasets are onindoorsnavigablescenespartlybecauseofthe
built. Here we summarize simulators frequently difficultyofbuildinganoutdoorphoto-realistic3D
usedduringtheVLNdatasetcreationprocess. simulatoroutoftheincreasedcomplexity. Google
House3D(Wuetal.,2018)isarealisticvirtual StreetView4,anonlineAPIthatisintegratedwith
3DenvironmentbuiltbasedontheSUNCG(Song GoogleMaps,iscomposedofbillionsofrealistic
etal.,2017)dataset. Anagentintheenvironment street-levelpanoramas. Ithasbeenfrequentlyused
has access to first-person view RGB images, to- tocreateoutdoorVLNtaskssincethedevelopment
getherwithsemantic/instancemasksanddepthin- ofTOUCHDOWN(Chenetal.,2019).
formation.
Matterport3D(Andersonetal.,2018b)simula- C Room-to-RoomLeaderboard
tor is a large-scale visual reinforcement learning
Room-to-Room (R2R) (Anderson et al., 2018b)
simulation environment for research on embod-
is the benchmark used most frequently for evalu-
iedAIbasedontheMatterport3Ddataset(Chang
ating different methods. Here we collect all the
et al., 2017). Matterport3D contains various in-
reportedperformancemetricsinthecorresponding
doorscenes,includinghouses,apartments,hotels,
papers and the official R2R leaderboard5. Since
offices, and churches. An agent can navigate be-
beamsearchexploresmoreroutes,andsinceprior
tweenviewpointsalongapre-definedgraph. Most
explorationhasadditionalobservationsinthetest
indoorsVLNdatasetssuchasR2Randitsvariants
environment,theirperformancecannotbedirectly
arebasedontheMatterport3Dsimulator.
comparedwithothermethods.
Habitat(ManolisSavva*etal.,2019;Szotetal.,
2021)isa3Dsimulationplatformfortrainingem-
bodiedAIin3Dphysics-enabledscenarios. Com-
paredwithothersimulationenvironments,Habitat
2.0 (Szot et al., 2021) shows strength in system
responsespeed. Habitathasthefollowingdatasets
built-in: Matterport3D (Chang et al., 2017), Gib-
son (Xia et al., 2018), and Replica (Straub et al.,
2019). AI2-THOR (Kolve et al., 2017) is a near
photo-realistic3Dindoorsimulationenvironment,
whereagentscouldnavigateandinteractwithob-
jects. Based on the object interaction function, it
helpstobuildadatasetthatrequiresobjectinterac-
tion,suchasALFRED(Shridharetal.,2020).
Gibson(Xiaetal.,2018)isareal-worldpercep-
tioninteractiveenvironmentwithcomplexseman-
4https://developers.google.com/maps/
documentation/streetview/overview
tics. EachviewpointhasasetofRGBpanoramas
5https://eval.ai/web/challenges/
with global camera poses and reconstructed 3D challenge-page/97/leaderboard/270
7621

Name Simulator Language-Active Environment
Room-to-Room(Andersonetal.,2018b) Matterport3D ✗ Indoor
Room-for-Room(Jainetal.,2019) Matterport3D ✗ Indoor
Room-Across-Room(Kuetal.,2020) Matterport3D ✗ Indoor
Landmark-RxR(Heetal.,2021) Matterport3D ✗ Indoor
XL-R2R(Yanetal.,2020) Matterport3D ✗ Indoor
VLNCE(Krantzetal.,2020) Habitat ✗ Indoor
StreetLearn(Mirowskietal.,2019) GoogleStreetView ✗ Outdoor
StreetNav(Hermannetal.,2020) GoogleStreetView ✗ Outdoor
TOUCHDOWN(Chenetal.,2019) GoogleStreetView ✗ Outdoor
Talk2Nav(Vasudevanetal.,2021) GoogleStreetView ✗ Outdoor
LANI(Misraetal.,2018) - ✗ Outdoor
RoomNav(Wuetal.,2018) House3D ✗ Indoor
EmbodiedQA(Dasetal.,2018) House3D ✗ Indoor
REVERIE(Qietal.,2020b) Matterport3D ✗ Indoor
SOON(Zhuetal.,2021a) Matterport3D ✗ Indoor
IQA(Gordonetal.,2018) AI2-THOR ✗ Indoor
CHAI(Misraetal.,2018) CHALET ✗ Indoor
ALFRED(Shridharetal.,2020) AI2-THOR ✗ Indoor
VNLA(Nguyenetal.,2019) Matterport3D ✓ Indoor
HANNA(NguyenandDauméIII,2019) Matterport3D ✓ Indoor
CEREALBAR(Suhretal.,2019) - ✓ Indoor
JustAsk(Chietal.,2020) Matterport3D ✓ Indoor
CVDN(Thomasonetal.,2019b) Matterport3D ✓ Indoor
RobotSlang(Banerjeeetal.,2020) - ✓ Indoor
TalktheWalk(deVriesetal.,2018) - ✓ Outdoor
MCCollab(Narayan-Chenetal.,2019) Minecraft ✓ Outdoor
TEACh(Padmakumaretal.,2021) AI2-THOR ✓ Indoor
DialFRED(Gaoetal.,2022) AI2-THOR ✓ Indoor
Table2: Vision-and-LanguageNavigationdatasets. Language-Activemeanstheagentneedstousenaturallanguage
torequesthelp,includingbothGuidancedatasetsandDialogdatasetsinTable1.
Simulator Photo-realistic 3D
House3D(Wuetal.,2018) ✓ ✓
Matterport3D(Changetal.,2017) ✓ ✓
Habitat(ManolisSavva*etal.,2019) ✓ ✓
AI2-THOR(Kolveetal.,2017) ✗ ✓
Gibson(Xiaetal.,2018) ✓ ✓
LANI(Misraetal.,2018) ✗ ✓
*GoogleStreetView ✓ ✓
Table3: CommonsimulatorsusedtobuildVLNdatasets. *GoogleStreetViewisonlineAPI,providingsimilar
functionalityasasimulatorforbuildingVLNdatasets.
7622

Leader-Board(TestUnseen) SingleRun PriorExploration BeamSearch
Models TL↓ NE↓ OSR↑ SR↑ SPL↑ TL↓ NE↓ OSR↑ SR↑ SPL↑ TL↓ NE↓ OSR↑ SR↑ SPL↑
Random 9.89 9.79 0.18 0.13 0.12 - - - - - - - - - -
Human 11.85 1.61 0.90 0.86 0.76 - - - - - - -
Seq-to-Seq(Andersonetal.,2018b) 8.13 20.4 0.27 0.20 0.18 - - - - - - - - - -
RPA(Wangetal.,2018) 9.15 7.53 0.32 0.25 0.23 - - - - - - - - - -
Speaker-Follower(Friedetal.,2018) 14.82 6.62 0.44 0.35 0.28 - - - - - 1257.38 4.87 0.96 0.54 0.01
ChasingGhosts(Andersonetal.,2019a) 10.03 7.83 0.42 0.33 0.30 - - - - - - - - - -
Self-Monitoring(Maetal.,2019a) 18.04 5.67 0.59 0.48 0.35 - - - - - 373.1 4.48 0.97 0.61 0.02
RCM!(Wangetal.,2019) 11.97 6.12 0.50 0.43 0.38 9.48 4.21 0.67 0.60 0.59 357.6 4.03 0.96 0.63 0.02
RegretfulAgent(Maetal.,2019b) 13.69 5.69 0.56 0.48 0.40 - - - - - - - - - -
FAST(Keetal.,2019) 22.08 5.14 0.64 0.54 0.41 - - - - - 196.5 4.29 0.90 0.61 0.03
ALTR(Huangetal.,2019) 10.27 5.49 0.56 0.48 0.45 - - - - - - - - -
EnvDrop(Tanetal.,2019) 11.66 5.23 0.59 0.51 0.47 9.79 3.97 0.70 0.64 0.61 686.8 3.26 0.99 0.69 0.01
PRESS(Lietal.,2019) 10.52 4.53 0.63 0.57 0.53 - - - - - - - - - -
PTA(Landietal.,2020) 10.17 6.17 0.47 0.40 0.36 - - - - - - -
EGP(Dengetal.,2020) - 5.34 0.61 0.53 0.42 - - - - - - - - - -
SERL(Wangetal.,2020b) 12.13 5.63 0.61 0.53 0.49 - - - - - 690.61 3.21 0.99 0.70 0.01
OAAM(Qietal.,2020a) 10.40 - 0.61 0.53 0.50 - - - - - - - - - -
CMG-AAL(Zhangetal.,2020a) 12.07 3.41 0.76 0.67 0.60 - - - - - - - - -
AuxRN(Zhuetal.,2020a) - 5.15 0.62 0.55 0.51 10.43 3.69 0.75 0.68 0.65 40.85 3.24 0.81 0.71 0.21
RelGraph(Hongetal.,2020a) 10.29 4.75 0.61 0.55 0.52 - - - - - - - - - -
PRRVALENT(Haoetal.,2020) 10.51 5.30 0.61 0.54 0.51 - - - - - - - - - -
ActiveExploration(Wangetal.,2020a) 21.03 4.34 0.71 0.60 0.43 9.85 3.30 0.77 0.70 0.68 176.2 3.07 0.94 0.70 0.05
VLN-BERT(Majumdaretal.,2020) - - - - - - - - - - 686.62 3.09 0.99 0.73 0.01
DASA(Sunetal.,2021) 10.06 5.11 - 0.54 0.52 - - - - - - - - - -
ORIST(Qietal.,2021) 11.31 5.10 - 0.57 0.52 - - - - - - - - - -
NvEM(Anetal.,2021) 12.98 4.37 0.66 0.58 0.54 - - - - - - - - - -
SSM(Wangetal.,2021) 20.39 4.57 0.70 0.61 0.46 - - - - - - - - - -
RecurrentVLNBERT(Hongetal.,2021) 12.35 4.09 0.70 0.63 0.57 - - - - - - - - - -
SOAT(Moudgiletal.,2021) 12.26 - 4.49 58 53
REM(Liuetal.,2021) 13.11 3.87 0.72 0.65 0.59 - - - - - - - - - -
HAMT(Chenetal.,2021b) 12.27 3.93 0.72 0.65 0.60 - - - - - - - - - -
SpatialRoutePrior(Zhouetal.,2021) - - - - - - - - - - 625.27 3.55 0.99 0.74 0.01
Airbert(Guhuretal.,2021) - - - - - - - - - - 686.54 2.58 0.99 0.78 0.01
3DSR(Tanetal.,2022) 15.89 3.73 0.73 0.66 0.60 - - - - - - - - - -
Table4: LeaderboardofRoom-to-RoombenchmarkasofMarch,2022
7623
