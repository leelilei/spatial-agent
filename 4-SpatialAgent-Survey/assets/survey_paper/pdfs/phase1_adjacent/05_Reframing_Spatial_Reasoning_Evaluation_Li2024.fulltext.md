Title: Reframing Spatial Reasoning Evaluation in Language Models: A Real-World Simulation Benchmark for Qualitative Reasoning

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_adjacent/05_Reframing_Spatial_Reasoning_Evaluation_Li2024.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:55:10+00:00
- page_count: 8
- status: ok
- text_char_count: 37863

Metadata:
- author: Fangjun Li, David C. Hogg, Anthony G. Cohn
- doi: unknown
- keywords: Natural Language Processing: NLP: Resources and evaluation, Knowledge Representation and Reasoning: KRR: Qualitative & geometric & spatial & temporal reasoning, Constraint Satisfaction and Optimization: CSO: Applications, Knowledge Representation and Reasoning: KRR: Learning and reasoning
- subject: Paper accepted and presented at IJCAI-2024

Outline:
- Introduction (page 1)
- Analysis of Existing Datasets and Benchmarks for QSR in Text (page 2)
  - bAbI (page 2)
  - StepGame (page 3)
  - SpartQA and SpaRTUN (page 3)
- Data Generation Framework (page 4)
  - Problem Definition (page 4)
  - Data Generation Process (page 4)
  - Define House Scenes and Objects (page 4)
  - Specify Spatial Relationships (page 4)
    - Object Layout within Room (page 5)
    - Relations between Objects (page 5)
  - CSP Example Generation (page 5)
    - Building a Constraint Graph (page 5)
    - Answer - Consistency Checking (page 5)
  - Generate Textual Descriptions (page 6)
- Evaluation (page 6)
  - Model Settings and Prompting (page 6)
  - Results (page 7)

Markdown Content:

ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI-24)
Reframing Spatial Reasoning Evaluation in Language Models:
A Real-World Simulation Benchmark for Qualitative Reasoning
FangjunLi1, DavidC.Hogg1, AnthonyG.Cohn1,2
1SchoolofComputing,UniversityofLeeds,UK
2AlanTuringInstitute,UK
{scfli,d.c.hogg,a.g.cohn}@leeds.ac.uk
Abstract Renz, 2008] [Alomari et al., 2022]. Existing benchmarks
likebAbI[Westonetal.,2016],StepGame[Shietal.,2022],
Spatial reasoning plays a vital role in both hu-
SpartQA[Mirzaeeetal.,2021],andSpaRTUN[Mirzaeeand
man cognition and machine intelligence, prompt-
Kordjamshidi, 2022] have significantly contributed to the
ingnewresearchintolanguagemodels’(LMs)ca-
field,yettheyexhibitlimitationsinrepresentingthecomplex-
pabilities in this regard. However, existing bench-
ityandnaturalnessfoundinreal-worldspatialreasoning.
marksrevealshortcomingsinevaluatingqualitative
Inthispaper,weconductanextensiveanalysisoftaskcom-
spatial reasoning (QSR). These benchmarks typ-
plexity and limitations in four widely used datasets for tex-
ically present oversimplified scenarios or unclear
tualspatialreasoningevaluation. bAbIandStepGame,orig-
natural language descriptions, hindering effective
inatingfromsimplified, toy-liketasks, utilizegrid-baseden-
evaluation. We present a novel benchmark for as-
vironments with fixed distances and angles for spatial rela-
sessing QSR in LMs, which is grounded in realis-
tions. Thisapproachforconstructingspatialreasoningdata,
tic 3D simulation data, offering a series of diverse
whileensuringuniquesolutions,oversimplifiesthetasks,fail-
roomlayoutswithvariousobjectsandtheirspatial
ing to capture the complexity of spatial relationships in the
relationships. This approach provides a more de-
real world. Moreover, the primary challenge in StepGame
tailedandcontext-richnarrativeforspatialreason-
liesinconstructingachainofobjectsfrommultipleshuffled
ingevaluation,divergingfromtraditional,toy-task-
relations, overshadowing the spatial reasoning aspect. Our
orientedscenarios. Ourbenchmarkencompassesa
previous research indicates that GPT-4 excels in the spatial
broadspectrumofqualitativespatialrelationships,
reasoning aspects of relation mapping and coordinate calcu-
includingtopological, directional, anddistancere-
lationneededforthistaskoncethechainisestablished.
lations. These are presented with different view-
On the other hand, SpartQA and SpaRTUN, which cover
ingpoints,variedgranularities,anddensityofrela-
awiderrangeofspatialrelationships, donotalwayscontain
tion constraints to mimic real-world complexities.
clear and fluent language descriptions. Common issues ob-
Akeycontributionisourlogic-basedconsistency-
servedincludecomplexobjectdescriptionsanddisorderedre-
checking tool, which enables the assessment of
lationalsequencing. Objectsaredescribedusingacombina-
multiple plausible solutions, aligning with real-
tionofcolor,size,andshape. Thislevelofdetailcomplicates
worldscenarioswherespatialrelationshipsareof-
the narrative, shifting the focus away from spatial reasoning
ten open to interpretation. Our benchmark evalu-
and towards deciphering the object descriptions. The disor-
ation of advanced LMs reveals their strengths and
deredrelationalsequencinghinderstheunderstandingofthe
limitationsinspatialreasoning. Theyfacedifficul-
corespatialproblem,addingunnecessarycomplexity.
tieswithmulti-hopspatialreasoningandinterpret-
ingamixofdifferentviewdescriptions,pointingto In response to the limitations of current benchmarks in
areasforfutureimprovement. qualitative spatial reasoning, this paper introduces a new,
more comprehensive benchmark to evaluate LMs’ abilities
in this domain. Our benchmark seeks to present more nat-
1 Introduction
urally described stories, employing language that is easily
Inrecentyears,advancementsinlanguagemodels[OpenAI, understandable and processable by both humans and LMs.
2023][Touvronetal.,2023]havesignificantlyimprovedtheir We aim to move away from overly logical expressions and
capabilities in understanding and reasoning with textual in- toward narratives that mirror everyday communication. To
formation[Lietal., 2022]. However, promotingthesemod- achievethisgoal,thescenariosforourbenchmarkaresourced
els’ ability to process and reason about spatial relationships from3Dsimulationdataratherthantoytasks,encompassing
remains a complex challenge [Bang et al., 2023] [Cohn and avarietyofroomlayoutswithdiverseobjects,eachannotated
Hernandez-Orallo, 2023]. Spatial reasoning, a critical com- withspecificattributes.Thisapproachallowseachscenarioto
ponentofhumancognition,involvesunderstandingandnav- showcaseadistinctarrangementofeverydayobjects. During
igatingtherelationshipsbetweenobjectsinspace[Cohnand datacreation,theplacementofobjects,theirlayout,andtheir
6342

ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI-24)
videarefinedassessmentoftheircapabilitiesinQSR.
Overall, these contributions advance LM evaluation for
spatialreasoning,aligningmorecloselywithreal-worldsce-
nariosandhumancognitiveprocesses.
2 AnalysisofExistingDatasetsand
BenchmarksforQSRinText
Representative benchmarks like bAbI, StepGame, SpartQA,
andSpaRTUNfocusonspatialreasoning. Theyinvolvetasks
wheremodelsarerequiredtoinfernewspatialrelationsfrom
providedfactsorchecktheconsistencyofrelations.
2.1 bAbI
The bAbI benchmark [Weston et al., 2016], featuring a col-
lectionofsynthetictasks,wascraftedtoevaluatelearningal-
gorithms in terms of their text understanding and reasoning
abilities.Amongits20tasks,Tasks17and19arespecifically
designedforspatialreasoningevaluation.
Task17testsLMs’abilitytounderstandandreasonabout
Figure1:Onetestinstanceinourbenchmark,consistingonlyoftext relative spatial relations ‘left’, ‘right’, ‘above’, and ‘below’.
forevaluatingLMs.Theaccompanyingimagesareforvisualization The task operates within a 5x5 grid environment. In this
butcouldbeusedtotestmulti-modalLLMs.
structuredsetting,threeentitiesaresequentiallypositionedat
specificnodes.Theplacementofeachentityisdeterminedby
its spatial relation to the adjacent nodes. The narratives dis-
spatialrelationshipswithotherobjectsaredetermined. This
tinguish three entities based on their color and shape. Each
informationformsthebasisforgeneratingstories,questions,
example can include up to 10 sentences - 2 describing spa-
andanswersforeachinstance.
tial relations between two pairs of objects and 8 for gener-
Recognizing that spatial reasoning often yields multiple
atingquestionsaboutadifferentpair,asillustratedinFigure
plausiblesolutions,wefocusonassessingtheconsistencyof
2. These questions are structured in a yes/no format, with
LMs’ answers within the given constraints rather than seek-
answersbasedontheentities’actualpositionsonthegrid.
ing a single ‘correct’ answer. This approach aligns with the
Task19iscenteredaroundidentifyingpathsbetweenspec-
real-world nature of spatial reasoning, where multiple inter-
ified objects, utilizing the four cardinal directions: north,
pretationsareoftenvalid.
south, east, and west. These objects are described as vari-
Finally, we evaluate some LLMs’ performance on our
ous locations, such as bedrooms and bathrooms. In the ‘en-
benchmark,toofferamorenuancedandcomprehensiveeval-
valid-10k’ version of bAbI1, each story typically includes 5
uationofLLMs’qualitativespatialreasoningability.Accord-
sentencesrelatedtospatialrelations: 2effectivelydescribing
ingtoourresults,GPT-4showssuperiorcapabilityinspatial
thepathand3servingasdecoys,asshowninFigure2. The
reasoningtasksacrossvarioussettings. Allmodelsfacechal-
task’schallengeliesinmappingoutasequentialpathfromthe
lenges in reasoning about spatial relations between objects
startentitytotheendentity.Theinclusionofdecoysentences
as multi-hop spatial reasoning complexity increases. How-
addsalayerofcomplexitytothetask.
ever, there is a clear trend toward improved performance as
thestory’sconstraintgraphbecomesmorecomplete.
This paper presents several contributions to the field of
QSR evaluation, particularly in the context of LM perfor-
mance. Thesecontributionsareasfollows:
• Comprehensive analysis of existing benchmarks. We pro-
videanin-depthanalysisofthecomplexityandlimitations
inherentincurrentspatialreasoningbenchmarks.
• Constructingamorenaturalandrealisticbenchmarkbyde- Figure2:ExamplesofTask17andTask19fromthebAbI’senvalid-
velopingscenariosderivedfrom3Dsimulationdata,offer- 10kdatasetversion.
ingadiverseseriesofdata,eachvaryinginthegranularity
ofrelationshipsandtheselectionofrelationalconstraints. The bAbI tasks, designed as simplified ‘toy tasks’, have
• Introductionofalogic-basedconsistencycheckingtoolfor limitations in testing spatial reasoning. They restrict spatial
evaluation, which evaluates whether spatial relations pre- relations to basic cardinal directions north, south, west, and
dictedbyLMsarefeasible,giventhesetconstraints. east (also referred to as above, below, left, and right in task
• Detailed evaluation of LLMs’ spatial reasoning abilities. 1https://www.kaggle.com/datasets/roblexnana/the-babi-tasks-
By applying our benchmark to test various LMs, we pro- for-nlp-qa-system
6343

ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI-24)
Figure4:AtestexampleinSpaRTUN.
Figure3: Illustrationofdirectionalspatialrelationshipsandtestin-
stanceconstraintchainbuildingprocessinStepGame.
thespatialreasoningcomponent itself. Whenprovidedwith
a pre-constructed reasoning chain, GPT-4 demonstrates re-
17)withsetdistancesandangles,lackingthecomplexityand
markableproficiencyinhandlingsuchreasoningtasks.
ambiguity of real-world spatial scenarios. Additionally, us-
ing a single template for each relation may not adequately
2.3 SpartQAandSpaRTUN
challengeamodel’sunderstandingandreasoninginmorenu-
anced, context-rich environments. Consequently, while use-
SpartQA[Mirzaeeetal.,2021]andSpaRTUN[Mirzaeeand
fulforbasictraining, bAbItasksmaynotfullytestorequip Kordjamshidi, 2022] start from 2D images featuring objects
modelsfortheintricaciesofreal-worldspatialreasoning. (rectangle,triangle,square)distributedacrossdistinctsquare
blocks (scenes). They extend beyond mere directional spa-
2.2 StepGame tial relationships to include Region Connection Calculus 8
Building upon bAbI, the StepGame benchmark [Shi et al., (RCC-8) [Randell et al., 1992] and distance (near and far).
2022] utilizes a grid-based system and introduces higher SpaRTUN is an updated version of SpartQA-Auto and con-
tainsmorerelationtypesandrules.
complexityinthreekeyaspects:
Unliketheprevioustwogrid-basedbenchmarks,SpartQA
• An expanded set of directional spatial relations is in- andSpaRTUN’sdefinespatialrelationsusingasquarebound-
cluded, encompassing eight relations: top (north), down ary framework. Each spatial relation is determined by the
(south), left (west), right (east), top-left (north-west), top- (x,y) coordinates of the lower-left points of the square
right (north-east), down-left (south-west), and down-right boundaryboxesoftwoobjectsandthesizeoftheseboxes.
(south-east). Each is defined by a unique angle and dis-
• For object-to-object relations, EC, NEAR, FAR, LEFT /
tance. Theserelationscanbevisuallyillustratedonagrid,
RIGHT,ABOVE/BELOWareconsidered;
asshownintheleftdiagramofFigure3,withtheinclusion
ofan‘overlap’relationforoverlappingobjectlocations. • For object-to-scene relations, TPP / TPPi, and NTPP /
NTPPiareconsidered;
• Enhancedmulti-hopreasoningchallenges:Movingbeyond
the4-hopreasoninginbAbI,StepGameincreasesthecom- • Forscene-to-scenerelations,DC,EC,PO,TPP/TPPi,and
plexity to span 1-hop to 10-hop sequences. The right dia- NTPP/NTPPiareconsidered.
gramofFigure3illustratesthesequentialbuildingofrela-
The scene description was generated from the selected
tionalconstraints,basedonk,thenumberofrelationships.
story triplets using context-free grammar (CFG). They in-
This produces a chain of constraints linking objects in a
creasethevarietyofspatialexpressionsbyusingavocabulary
directpathfromo too ,continuingthroughtoo .
1 2 n+1 of various entity properties and relation expressions. They
• Employing richer, crowdsourced narratives describing maptherelationtypesandtheentitypropertiestothelexical
eightpossiblespatialrelationsbetweentwoentities,which formsfromaspecificallycollectedvocabulary.
serveasthebasisforgeneratingstory-questionpairs. Although these two benchmarks include rich spatial re-
lationships, they struggle to provide effective descriptions.
The spatial configuration used in StepGame introduces
Theyusesimplesyntaxandwordchoicebutlacklogicalflow
limitationsthatmayaffecttheevaluationofLMs’spatialrea-
andcontentclarity,particularlyintwoaspects:
soning abilities. Commonsense human understanding does
not confine directional relationships to strict distance or an- • The spatial relations are described as a sequence of ran-
gular constraints. For example, when we say ‘A is east of domlyselectedstorytriplets,whichdeviatesfromthetyp-
B’inatwo-dimensionalframework,itsimplymeansthatthe ical human approach to describing a scene. In the exam-
x-coordinate of A, denoted as x , is larger than that of B, plefromFigure4,amorenaturalhumandescriptionwould
A
x . Thisdoesnotnecessarilydictatethatx shouldexceed typicallystartwithoutliningtherelationshipsbetweentwo
B A
x byanexactvalueoralignwithaspecificangle,suchasa boxes,followedbydetailingthecontentsofeachbox,and
B
1-unitdifferenceora90◦angle. then explaining the relations between the objects. How-
StepGame’s design yields unique solutions for all in- ever,intheirnarrativestructure,thereisalackofaninitial
stances, but with limited complexity (as depicted in the Ap- summary of the objects contained in each box, with ob-
pendix). Prior research [Li et al., 2024] indicates that the jectsbeingintroducedindividuallyandsomewhatdisjoint-
mostchallengingaspectforLLMsinthistaskisconstructing edly. Additionally, the narrative places the object-to-box
the object-linking chain from shuffled relations, rather than relationships prior to the box-to-box relationships, which
6344

ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI-24)
further diverges from the typical human method of spatial
description,leadingtopotentialconfusioninunderstanding
theoverallspatiallayout.
• Theexcessiveuseofdetailedandrepetitiveentitynaming,
involving terms like ‘medium yellow apple’, ‘medium or-
angeapplenumberone’, and‘mediumorangeapplenum-
ber two’, results in overly lengthy text. This verbosity
Figure5: Samplescenesfromourdatasetshowcasingfourtypesof
transforms a simple description such as ‘South of A is B’
roomsinatop-downview.
intoamoreconvolutedonelike‘Southofmediumorange
apple number one is medium orange apple number two’.
Such complexity not only adds confusion but also shifts of objects on the floor plane. In the dataset, width and
thefocusfromunderstandingthespatialrelationshiptode- lenghtharealwaysequal,yieldingsquarerooms.
ciphering which specific object is being referred to. This
• misthenumberofbinaryconstraintsovernobjects,setby
can make it hard for readers to grasp the intended spatial
themethoddescribedinSection3.5. Themaximumpossi-
relationshipsandhindersmoothcomprehension.
ble number of constraints on n variables is n(n−1), under
Consequently, the narrative’s lack of smooth flow in tex- 2
which each variable is constrained by all other variables
tualdescriptionsmakesitdifficultforbothLMsandhumans
andthegraphisacompletegraph,i.e.,ann-clique.
toformaclearmentalimageoftheentiresceneandtograsp
informationaboutspecificobjectsinquestion.Thiscomplex- • pistheconstrainttightness.Forunaryconstraints,pranges
ityhinderstheLMsfromengaginginspatialreasoningeffec- from 0 to d, and for binary constraints, from 0 to d×d.
tively and drawing conclusive answers based on the limited Here, d is the domain size for one variable, d×d corre-
informationpresented. sponds to the total possible pairs of values between two
variables. Foreachbinaryconstraint,thenumberofdisal-
3 DataGenerationFramework lowedvaluepairsiscalculatedasp×(d×d). pisrelated
to the types of constraints, as outlined in Section 3.4. We
3.1 ProblemDefinition analysetheconstrainttightnessintheAppendix.
Wefocusonconstraintsatisfactionproblems(CSP),defined All constructed constraint networks are transformed into
by a set of variables V defined over a domain D and a col- a textual format using the method outlined in Section 3.6,
lectionofconstraintsθ. Thegoalistofindaspecificinstan- specificallyforthepurposeofevaluatingLMs. Ourtestsets
tiationwhereallconstraintsinθaresimultaneouslysatisfied. are available in varying sizes: RoomSpace-100 includes a
Weparticularlyemphasizebinaryconstraints,whichsimulta- sample of 100 rooms. RoomSpace-1K consists of 1,000
neouslyrestrictthedomainoftwovariables. Anexampleof rooms, andRoomSpace-10Kcomprises10,000rooms. The
thisis‘Thedeskisplacedinfrontofthesofa.’ initial100roomsinRoomSpace-1K(ID0-99)areidenticalto
Oneinstanceofspatialreasoningproblemcanbeconcep- thoseinRoomSpace-100. Similarly,thefirst1,000roomsin
tualized as a constraint network framework: consider a net- RoomSpace-10K(ID0-999)matchthoseinRoomSpace-1K.
workcomprisingnspatialvariablesV = {o ,...,o }within
1 n
a domain Dn. In this network, each node is identified by 3.3 DefineHouseScenesandObjects
a variable o or by the variable’s index i, and each directed
i We utilize the ProcTHOR [Deitke et al., 2022] framework
edgeismarkedwithabinaryrelationconstraint. Weusethe
tocreatephysics-enabledenvironments, whichallowforthe
notationrij todenotetherelationthatconstrainsthepairof
generation of a variety of virtual house environments. The
variables ⟨o ,o ⟩. One relation constraint in θ can thus be
i j
initial ProcTHOR dataset includes simulated houses with
denotedasr (o ,o )or(o ,r ,o ).
ij i j i ij j
multiplerooms. Forourindoorsetup,weadaptthistogener-
Given a set of k relations and a query (o ,r ,o ), LMs
a ab b
atesceneswithinasingle-roomconfigurationtosimplifythe
are tasked with predicting the relation r . If all constraints
ab
spatialreasoningchallenges(seeFigure5forexamples).
presentinthestory,includingthepredictedrelationconstraint
Each room is uniformly square-shaped, enclosed by four
(o ,r ,o ),canbesimultaneouslysatisfied,weconsiderthe
a ab b
walls(north,south,east,andwest)thatincorporateelements
predictiontobeaneffectivesolution.
such as doors and windows. Despite this structural consis-
3.2 DataGenerationProcess tency, each room type is distinguished by diverse configura-
tionsofhouseholdobjects.
Our benchmark data encompasses a range of configura-
tions, each aligning with specific elements of the constraint
3.4 SpecifySpatialRelationships
network. These configurations are denoted by the tuple
⟨n,d,m,p⟩,where: We incorporate three types of spatial relations: topological,
directional,anddistancerelations.Theseareutilizedtodetail
• n is the number of objects used to form the story in the
thepositioningofobjectswithinrooms(C )andtodefinethe
scene,asisestablishedthroughtheprocessinSection3.5. l
relationships between objects (C ). The layout constraints,
o
• disthenumberofsquaretilesina width×lengthtessella- C ,areexpressedas(o ,r ,Room),i ∈ [1,n],andtheinter-
l i i
tionwhosecentresdefinepossiblepositionsforthecentres objectconstraints,C ,areformulatedas(o ,r ,o ),i̸=j.
o i ij j
6345

ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI-24)
Figure7: Anoverviewofdirectionalanddistancespatialrelation-
ships:Theleftimagedisplaystheroom’sspatialdivisions.Themid-
dleimagedisplaysbothdirectionalanddistance-basedrelationships
among objects from a top-down view. The right image illustrates
Figure6: Illustrationshowcasingtwotopologicalspatialrelations: directionalrelationsasseenfromanorth-facingperspective.
TPP(inred,denotingobjectstouchingtheroom’swalls)andNTPP
(ingreen,representingobjectspositionedinsidetheroom’sbound-
p
arieswithouttouchingthewalls). (x −x )2+(z −z )2. The qualitative distance rela-
1 2 1 2
tions are defined based on the ratio dis or √dis , where w is
w √ 2w
ObjectLayoutwithinRoom thelengthandwidthofthesquareroom, 2wcorrespondsto
We incorporate directional and topological spatial relation- the diagonal length of the room. We have incorporated two
shipstodetailhowobjectsarepositionedwithinrooms. levelsofdistancerelationsettingsinourbenchmark:
Directional Relations. The representation of directional • close, far (Threshold: w). A binary classification where
2
relations between objects extended in 2D space, we just use close is within half the room’s width/length w, and far is
their central points. As depicted in the left part of Figure 7, beyondit,providingasimpledistancedistinction.
wedivide theroom intonine regions: North(N), West(W), √ √
• close,medium,far(Thresholds: 2w, 2 2w). Themedium
East (E), South (S), Center (C), North-West (NW), North- 3 3
category is introduced for a more nuanced understanding,
East (NE), South-West (SW), and South-East (SE). The lo- √ √ √
cation of an object in a room is determined by the region in withcloseupto 2w,mediumbetween 2w and 2 2w,far
√ 3 3 3
whichthecentreofitsboundingboxissituated. beyond 2 2w,asdepictedinthemiddlepartofFigure7.
3
TopologicalRelations. Twosettingsareconsidered:
3.5 CSPExampleGeneration
• Uniform Inclusion. All objects are considered within the
BuildingaConstraintGraph
room,withnospecifictopologicaldistinctionsmade.
Ourbenchmarkoffersavarietyofstorieswithvaryinglevels
• Tangential Proper Part (TPP) and Non-Tangential Proper of complexity, accomplished by adjusting two key parame-
Part (NTPP). Just record objects’ topological relations to ters: n for object selection and m for constraint determina-
thewall,notthefloor,asdepictedinFigure6. tion. Ourmethodologyisimplementedasfollows:
NodeSelection. Wefocusonprominent,largerobjectsthat
RelationsbetweenObjects
occupymorespaceinaroom. Forexample,inthecontextof
We define the relationships between any two objects using
‘an apple on a desk’, we would prioritize the desk over the
directional and distance-based spatial relations, determined
apple. OftheN prominentobjectsinthescene,werandomly
bycomparingthexandycoordinatesoftheircentrepoints.
selectntorepresentasnodesinthegraph.
Directional Relations. We use a projection-based method
ConstraintSelection. Inaconstraintgraphwithnobjects,
to represent the nine different directional relations in cardi- thereareC2potentialpairconnections. Forexample,agraph
nal algebra [Ligozat, 1998], as illustrated in the middle part with5obje n ctsyieldsC2 = 10possibleconstraintpairs. For
of Figure 7. We use two reference frames: top-down view 5
allpossiblepairsofobjects,wefirstselectonepairtoformthe
andnorth-facingview,differingintheexpressionofbinary- question.Then,fortheremainingC2−1pairs,theparameter
directionalrelations.Inthetop-downview,theserelationsare n
misusedtoestablishgraph.
depicted using cardinal directions (north, south, east, west)
and their combinations. In the facing view, the cardinal di- Answer-ConsistencyChecking
rections are adapted to localized terms (front, behind, right, We include two types of questions: Find Relation (FR):
left)toprovideapotentiallymoreintuitiveunderstandingof identifythedirectionalspatialrelationshipbetweentwospec-
spatialrelationsfromtheobserver’sviewpoint2. ified objects. Yes/No (YN): ascertain the validity of a state-
mentconcerningthespatialrelationshipbetweenobjects.
Distance Relations. The distance between objects is
Generating ground-truth answers for spatial relations be-
determined by calculating the Euclidean distance be-
tween objects o and o from the simulation system can be
tween the center points of their bounding boxes dis = 1 2
automated through comparing their coordinates, represented
2It would not be intuitive in the aboriginal language Guugu as (x 1 ,y 1 ) and (x 2 ,y 2 ). However, key considerations arise:
Yimithirr,whichlackswordsfor‘left’or‘right’,andspatialinforma- Given the stories formed with limited qualitative relations,
tionismainlyconveyedusingcardinaldirections[Haviland,1998]. canwedefinitivelydeducetheanswer? Isthereapossibility
6346

ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI-24)
Figure 8: The percentage of single, multiple, and no solution occurrences (Rows 1, 2) and the average CPU time (seconds) for solution
searches (Rows 3, 4) in RoomSpace-100 with different d. For Rows 1 and 3, n varies while m = n−1; for Rows 3 and 4, m varies
withnconstantat5. SpatialrelationsettingsincludeLayout: Thebasicsettingwithdirectionalobjectlayoutrelations. TPP:Enhanced
objectlayoutwithtopologicalrelationsTPPandNTPP.O2:Pureinter-objectdirectionalrelations. O2+D2:O2expandedwithtwodistance
relations;O2+D3:O2expandedwiththreedistancerelations;O2+D2+LayoutandO2+D3+Layout:Combininginter-objectsrelationswith
objectlayoutrelations.
of multiple validsolutions? Forexample, inthe scenario‘A S l →Thisroomcontainsacollectionoffurniture, includ-
is to the left of B, and C is to the left of A,’ the position of
ing⟨S0⟩,⟨S1⟩,...,⟨Sn⟩.
l l l
A relative to C is ambiguous based on the information pro- ST →⟨ST01⟩. ⟨ST12⟩. .... ⟨STij⟩.
o o o ot
vided. A could be to the right, left, or overlapping with C. SN →Imagineyourselfatthesouthernwall’sdoor, look-
o
The stories in our benchmark offer a partial view of spatial inginwards. Fromthisperspective,⟨SN01⟩. ....⟨SNij⟩.
o o
layouts.Giventhelimitedqualitativedescriptions,asingular,
definitiveanswermaynotalwaysbeattainable. Si →⟨x ⟩placedinthe⟨rDir⟩,⟨rTPP⟩thewall
l i i i
Recognizing the potential for multiple valid solutions STij →⟨x ⟩isplacedtothe⟨rDir⟩of⟨x ⟩,⟨rDis⟩
o i ij j ij
withintheconstraintsdetailedinthestory,wehavedeveloped SNij →⟨x ⟩is⟨rDirN⟩⟨x ⟩,⟨rDis⟩.
o i ij j ij
a consistency-checking tool using the python-constraint
package3, whichemploysabacktrackingalgorithmtodeter- Table1: Ourdesignedgrammar. SN representssentencesdescrib-
minewhetheraplausibleconfigurationofobjectrelationships ingnorth-facingviewrelations,andST fortop-downviews.
can exist to meet all specified constraints. Additional infor-
mationaboutthisreasonerisavailableintheAppendix.
3.6 GenerateTextualDescriptions
In Figure 8, we analyze the occurrence of single, multi-
During this phase, we transform the spatial logical expres-
ple,andnosolutionpossibilitiesundervariousconstraintset-
sionsC andC intonaturallanguagesentencesS andS ,a
tings. With a smaller domain size of 9×9, the Layout and l o l o
processknownaslogic-to-textgeneration.
O2relationsettingsconsistentlyyieldsolutions;however,the
We develop specific logic-to-string templates using
likelihoodofnosolutionissignificantlyhighercomparedto
context-freegrammar(CFG).Whenformingstories,thelog-
the larger domain size of 12 × 12 when incorporating dis-
ical components such as ⟨x ⟩,⟨x ⟩, ⟨rDir⟩,⟨rTPP⟩, ⟨rDir⟩,
tance constraints. Additionally, the search cost (CPU time) i j i i ij
requiredtofindsolutionswiththelargerdomainsizeiscon- ⟨rDis⟩ are replaced with corresponding textual expressions,
ij
siderably higher than with the smaller one. We examine the enabling the creation of varied descriptions of spatial rela-
searchcostsassociatedwithfindingsolutionsforFRandYN tionships. OurCFGhastwoparts,asshowninTable1.
questions. FR questions generally involve multiple answers
andrequireevaluatingallninedirectionrelationstoidentify 4 Evaluation
all potential solutions that meet the constraints. In contrast,
4.1 ModelSettingsandPrompting
YNquestionsinvolvecheckingonlyonerelationalcandidate,
We access GPT-3 (Davinci) [Brown et al., 2020], GPT-3.5
resultinginlowersearchcosts.
(Turbo), and GPT-4 [OpenAI, 2023] via the Azure OpenAI
Service, usingtheAPIversion“2023-09-15-preview”forall
3https://github.com/python-constraint/python-constraint threemodels. Toyieldmoredeterministicresults,wesetthe
6347

ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI-24)
temperatureto0inallexperiments. Theremainingparame-
terswereleftatthestandardconfigurationsforthesemodels.
We conduct experiments with two sets of prompts [Bom-
masani et al., 2021]: one set directly presents stories and
questionstoLLMs,whiletheotherincorporatestaskdescrip-
tionsanddetailsaboutrelationshipdefinitions,asdetailedin
theAppendix,toguideLLMs’responses.
Experiment results (in Appendix) illustrates a slight im- Figure9: Performanceofgpt-35-turboontheRoomSpace-100test
provementintheperformanceofgpt-35-turbowiththeLay- setswithn = 5andm = 4usingtop-downviewandnorth-facing
out, O2+D2, and O2+D2+Layout settings. However, in- viewonYNquestions.
corporatingtaskdescriptionpromptsresultsinadecreasein
accuracy within the TPP settings. Therefore, although the
added prompts about task description provide valuable in-
sights into the spatial reasoning problem, the minimal vari-
ation in performance suggests that for subsequent experi-
ments,wemaintainastraightforwardstoryandquestionfor-
matprompt.
4.2 Results
Figure9andFigure10presentthecomparativeresultsacross
Figure 10: Performance of GPT models with top-down view O2
models, relation settings, parameters n and m, highlighting
settingacrossvariationsinparametersnandmonRoomSpace-100.
severalkeyobservations:
Model Comparison. GPT-4 consistently surpasses both
Turbo and Davinci in nearly all categories and from various thisparametergenerallyleadstoimprovedaccuracy(seeFig-
viewpoints. Turboshowscomparativelyloweraccuracythan ure 10, right). It appears that larger m values, with more
theothertwomodels,withitsaccuracyfallingtozerounder densely interlinked spatial relationships, though adding text
theconditionwheren=6andm=5. length,tendtoenhanceLMs’performance.
ViewingPerspectiveInfluence. Thenorth-facingviewde-
scriptions do not significantly impact the results when the Conclusion
narrative already includes descriptions from that view, as in
OurstudyidentifiesgapsincurrentQSRdatasetsandpresents
the O2 setting and its combinations with distance or lay-
a new benchmark to better evaluate LMs’ capabilities in
out, where accuracy remains comparable to the top-down
spatial reasoning. We enhance QSR dataset creation with
view. However,undertheLayoutsetting,whichincludesdi-
a benchmark that addresses multiple complexities, includ-
rectional descriptions from the top-down view, introducing
ing topological, directional, and distance relationships. Our
north-facing view descriptions in the questions complicates
benchmarkuniquelyincorporatesdifferentviewingperspec-
comprehensionforLLMs,leadingtoadeclineinaccuracy.
tivesinspatialreasoning,movingtowardsmoreaccurateLM
ImpactofSpatialReasoningSettings. Layoutvs. O2: In evaluations. Our results underscore the necessity for en-
theLayoutsetting,theintroductionofTPPdoesnotmarkedly hancements in current state-of-the-art LLMs, opening new
affectaccuracy.Evenwithn=5,GPTconsistentlyperforms avenuesforenhancingspatialreasoninginAImodels.
well,efficientlyextractingandanalyzinginformation. How- Future directions include incorporating object size and
ever, when dealing with only the relationships between ob- shape,asourcurrentfocusisonobjectcentersforspatialrela-
jectsinmulti-objectscenes,thetaskbecomeschallengingfor tionships. Additionally,exploringmoretopologicalrelations
GPT,highlightingthemodel’slimitationsinmulti-hopspatial beyond TPP and NTPP can deepen the benchmark’s scope.
reasoning. We also aim to include more complex perspectives, such as
Distance Settings (D2, D3): Interestingly, Turbo’s perfor- anagent’sviewpointwithinaroom,introducingnaturalfront-
mance slightly improves with the introduction of distance facingscenariosformorechallengingreasoningtasks.
constraints. This may suggest GPT-4’s better handling of
ThispaperprovidesapreliminaryevaluationofOpenAI’s
morecomplexspatialrelations.
GPTseriesmodelsonournewdatasetRoomSpace-100. Ex-
Combination of Layout, O2 and Distance: The combined
panding this research to assess and compare the spatial rea-
settings typically yield performance that is on par with the
soningabilitiesofotherLLMswouldbebeneficial.Addition-
best-performing individual setting, in this instance, aligning
ally, although our benchmark covers both FR and YN ques-
withtheresultsobservedinthelayoutsetting.
tions,ourevaluationislimitedtotheYNquestions. FRques-
VariationwithParameters(nandm). Thereisadecline tions,whichtypicallyrequiremultiple-choiceanswers,repre-
inaccuracyasnincreasesfrom3to7,suggestingthatlarger sentamoresignificantchallenge.Futureresearchcoulddelve
nvaluescreatemorecomplexandchallengingscenarios(see intothesemoreintricatescenarios.Moreover,whileoureval-
Figure 10, left). This trend aligns with the observations in uationsutilizeRoomSpace-100,exploringlargersets,suchas
Figure 8 - the time taken by the CPU to find solutions in- the1Kand10Kversions,couldprovidemorecomprehensive
creases with higher n values. In terms of m, an increase in insights.
6348

ProceedingsoftheThirty-ThirdInternationalJointConferenceonArtificialIntelligence(IJCAI-24)
Acknowledgments Van Harmelen, Vladimir Lifschitz, and Bruce Porter, ed-
itors,Handbookofknowledgerepresentation,pages551–
We thanks the anonymous referees for their helpful com-
596.Elsevier,2008.
ments. This work has been partially supported by: (1)
Microsoft Research - Accelerating Foundation Models Re- [Deitkeetal.,2022] Matt Deitke, Eli VanderBilt, Alvaro
searchprogram,withtheprovisionofAzureresourcestoac- Herrasti,LucaWeihs,KianaEhsani,JordiSalvador,etal.
cessGPT;(2)theTuring’sDefenceandSecurityprogramme Procthor: Large-scale embodied ai using procedural gen-
throughapartnershipwiththeUKgovernmentinaccordance eration. AdvancesinNeuralInformationProcessingSys-
withtheframeworkagreementbetweenGCHQandTheAlan tems,35:5982–5994,2022.
Turing Institute; (3) Economic and Social Research Council [Haviland,1998] J B Haviland. Guugu Yimithirr cardinal
(ESRC)undergrantES/W003473/1. directions. Ethos,26(1):25–47,1998.
[Lietal.,2022] FangjunLi,DCHogg,andAGCohn.Ontol-
DataAccessStatement
ogy knowledge-enhanced in-context learning for action-
effect prediction. Advances in Cognitive Systems. ACS-
Data associated with this paper are available from the
2022,2022.
University of Leeds data repository https://doi.org/10.5518/
1518. Codeandappendixareavailableathttps://github.com/ [Lietal.,2024] FangjunLi,DavidCHogg,andAnthonyG
Fangjun-Li/RoomSpace. Cohn.Advancingspatialreasoninginlargelanguagemod-
els: An in-depth evaluation and enhancement using the
ContributionStatement stepgamebenchmark. InProceedingsoftheAAAIConfer-
ence on Artificial Intelligence, volume 38, pages 18500–
ACconceivedtheoriginalideaforthebenchmarkwhichwas 18507,2024.
thenrefinedindiscussionswithFJandDH.FJimplemented
[Ligozat,1998] Gerard Ligozat. Reasoning about cardinal
thebenchmarkanddesignedalldetails,performedtheevalu-
directions. Journal of Visual Languages & Computing,
ations, andwrotetheoriginaldraftofthepaper. Allauthors
9(1):23–44,1998.
contributedtothesubsequentdrafts.
[MirzaeeandKordjamshidi,2022] Roshanak Mirzaee and
ParisaKordjamshidi. Transferlearningwithsyntheticcor-
References
pora for spatial role labeling and reasoning. In Proceed-
[Alomarietal.,2022] Muhannad Alomari, Fangjun Li, ingsofthe2022ConferenceonEmpiricalMethodsinNat-
David C Hogg, and Anthony G Cohn. Online perceptual uralLanguageProcessing,pages6148–6165.Association
learningandnaturallanguageacquisitionforautonomous forComputationalLinguistics,December2022.
robots. ArtificialIntelligence,303:103637,2022. [Mirzaeeetal.,2021] Roshanak Mirzaee, Hossein Rajaby
[Bangetal.,2023] Yejin Bang, Samuel Cahyawijaya, Faghihi,QiangNing,andParisaKordjamshidi. SpartQA:
Nayeon Lee, Wenliang Dai, Dan Su, Bryan Wilie, Holy atextualquestionansweringbenchmarkforspatialreason-
Lovenia, Ziwei Ji, Tiezheng Yu, Willy Chung, et al. ing. In Proceedings of the 2021 Conference of the North
A multitask, multilingual, multimodal evaluation of American Chapter of the Association for Computational
ChatGPT on reasoning, hallucination, and interactivity. Linguistics: HumanLanguageTechnologies,pages4582–
arXivpreprintarXiv:2302.04023,2023. 4598,2021.
[Bommasanietal.,2021] Rishi Bommasani, Drew A Hud- [OpenAI,2023] OpenAI. GPT-4 technical report. ArXiv,
abs/2303.08774,2023.
son, Ehsan Adeli, Russ Altman, Simran Arora, Syd-
ney von Arx, Michael S Bernstein, Jeannette Bohg, An- [Randelletal.,1992] David A Randell, Zhan Cui, and An-
toine Bosselut, Emma Brunskill, et al. On the oppor- thonyGCohn. Aspatiallogicbasedonregionsandcon-
tunities and risks of foundation models. arXiv preprint nection. KR,92:165–176,1992.
arXiv:2108.07258,2021.
[Shietal.,2022] Zhengxiang Shi, Qiang Zhang, and Aldo
[Brownetal.,2020] TomBrown,BenjaminMann,NickRy- Lipani. Stepgame: A new benchmark for robust multi-
der, Melanie Subbiah, Jared D Kaplan, Prafulla Dhari- hopspatialreasoningintexts. InProceedingsoftheAAAI
wal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, conference on Artificial Intelligence, volume 36, pages
Amanda Askell, et al. Language models are few-shot 11321–11329,2022.
learners. Advances in neural information processing sys- [Touvronetal.,2023] Hugo Touvron, Louis Martin, Kevin
tems,33:1877–1901,2020. Stone,PeterAlbert,etal. Llama2: Openfoundationand
[CohnandHernandez-Orallo,2023] Anthony G Cohn and fine-tunedchatmodels,2023.
Jose Hernandez-Orallo. Dialectical language model [Westonetal.,2016] Jason Weston, Antoine Bordes, Sumit
evaluation: An initial appraisal of the commonsense Chopra, Alexander M Rush, Bart Van Merrie¨nboer, Ar-
spatial reasoning abilities of LLMs. arXiv preprint mand Joulin, and Tomas Mikolov. Towards AI-complete
arXiv:2304.11164,2023. questionanswering: Asetofprerequisitetoytasks. In4th
International Conference on Learning Representations,
[CohnandRenz,2008] Anthony G Cohn and Jochen Renz.
ICLR,2016.
Qualitativespatialrepresentationandreasoning. InFrank
6349
