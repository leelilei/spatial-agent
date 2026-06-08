Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/review_library/01_Feng2025_Spatial_Intelligence_Across_Scales.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:07+00:00
- page_count: 14
- status: ok
- text_char_count: 68527

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Background and Taxonomy (page 2)
  - Spatial Intelligence of Human (page 2)
    - Cognitive Map (page 2)
    - Spatial Schema (page 2)
  - Taxonomy of Spatial Intelligence (page 3)
- Foundational Capabilities of Spatial Intelligence in LLMs (page 3)
  - Spatial Memory and Knowledge in LLMs (page 3)
  - Abstract Spatial Reasoning of LLMs (page 4)
- LLM based Spatial Intelligence for the Real World (page 4)
  - Embodied Spatial Intelligence (page 4)
    - Spatial Perception and Understanding (page 5)
    - Spatial Interaction and Navigation (page 5)
  - Urban Spatial Intelligence (page 6)
    - Spatial Understanding and Memory (page 6)
    - Spatial Reasoning and Intelligence (page 7)
  - Earth Spatial Intelligence (page 7)
    - Global Encoding (page 8)
    - Climate (page 8)
    - Geography (page 8)
    - Other Disciplines (page 9)
- Challenges and Discussions (page 9)
  - Fundamental Spatial Intelligence (page 9)
  - Embodied Spatial Intelligence (page 9)
  - Urban Spatial Intelligence (page 10)
  - Earth Spatial Intelligence (page 10)
  - Relation with World Model (page 10)
- Conclusion (page 10)

Markdown Content:

A Survey of Large Language Model-Powered Spatial Intelligence Across Scales:
Advances in Embodied Agents, Smart Cities, and Earth Science
JieFeng,JinweiZeng,QingyueLong,βHongyiChen,JieZhao,†YanxinXi,ZhilunZhou,
YuanYuan,§ShengyuanWang,QingbinZeng,SongweiLi,YunkeZhang,
YumingLin,TongLi,JingtaoDing,ChenGao,FengliXu,YongLi
DepartmentofElectronicEngineering,BNRist,TsinghuaUniversity,Beijing,China,
β ShenzhenInternationalGraduateSchool,TsinghuaUniversity,Shenzhen,China,
§DepartmentofComputerScience,TsinghuaUniversity,Beijing,China,
†DepartmentofComputerScience,UniversityofHelsinki,Helsinki,Finland
{fengjie,liyong07}@tsinghua.edu.cn
Abstract towayfindingstrategies,haveprovidedfoundationalinsights
intohumanintelligence.Ontheotherhand,spatialintelligence
Over the past year, the development of large lan-
haslonghadpracticalsignificanceinreal-worldapplications,
guage models (LLMs) has brought spatial intelli-
suchasembodiednavigation[Linetal., 2024], geographic
gence into focus, with much attention on vision-
information systems (GIS) [Zhao et al., 2024], and climate
basedembodiedintelligence. However,spatialin-
prediction[Sheetal.,2024]. Thestudyofspatialintelligence
telligencespansabroaderrangeofdisciplinesand
continuestoevolve,bridgingcognitivescience,artificialintel-
scales, from navigation and urban planning to re-
ligence,andapplieddomains.
motesensingandearthscience. Whatarethediffer-
The rapid advancements in deep learning, particularly in
encesandconnectionsbetweenspatialintelligence
largelanguagemodels(LLMs),havesignificantlycontributed
across these fields? In this paper, we first review
to spatial intelligence research of recent years. LLMs have
humanspatialcognitionanditsimplicationsforspa-
madenotableprogresswithworldknowledge,planningand
tialintelligenceinLLMs. Wethenexaminespatial
reasoning capabilities, and powerful generalization across
memory, knowledge representations, and abstract
tasks. Theseadvancementshavefueledresearchinembodied
reasoninginLLMs,highlightingtheirrolesandcon-
intelligence[Guptaetal.,2021],whereLLMsplayacentral
nections. Finally, we analyze spatial intelligence
roleinareassuchasroboticnavigation,multimodalperception,
acrossscales—fromembodiedtourbanandglobal
andcontrol. Recentworks,suchasSpatialVLM[Chenetal.,
levels—followingaframeworkthatprogressesfrom
2024]andVoxposer[Huangetal.,2023b],havedemonstrated
spatial memory and understanding to spatial rea-
howLLMscanimprovespatialreasoninganddecision-making
soning and intelligence. Through this survey, we
inembodiedagents,enablingthemtooperatemoreeffectively
aimtoprovideinsightsintointerdisciplinaryspatial
incomplexenvironments.
intelligenceresearchandinspirefuturestudies.
Beyond embodied intelligence, LLMs have also inspired
new research in urban and global-scale spatial intelligence.
1 Introduction Inurbanresearch,forexample,LLMshavebeenintegrated
withgeospatialdatatooptimizeurbanplanning[Zhouetal.,
Spatialintelligenceisaninherentlyinterdisciplinaryresearch
2024b],trafficprediction[Lietal.,2024e]andinfrastructure
field,encompassingdiversechallenges,applicationscenarios,
management[Laietal.,2023]. Ataglobalscale,researchers
andmethodologiesacrossmultipledomains.Forexample,nav-
haveexploredhowLLMscanenhanceremotesensinganaly-
igatingwithinaroomrequiresspatialintelligence,designinga
sis[Kuckrejaetal.,2024]anddisasterprediction[Zhanget
15-minutecommunityreliesonspatialintelligence,predicting
al.,2023b],andsoon,whichillustratethepotentialofLLMs
thepossiblelocationofanimageinvolvesspatialintelligence,
to process large-scale geospatial information and generate
and analyzing the spatial patterns of climate is also a form
meaningfulinsightsforglobal-scaledecision-making. These
of spatial intelligence. In other words, spatial intelligence
interdisciplinaryapplicationshighlightthetransformativeim-
is ubiquitous and plays a crucial role in human society and
pactofLLMsonspatialintelligenceresearch,pavingtheway
physicalworld.
forfuturedevelopmentsacrossmultipledomains.
Researchonspatialintelligencehasdeephistoricalroots.
Despite the growing of research on spatial intelligence
On the one hand, it serves as a crucial avenue for humans
acrossvariousfields,thereisstillalackofaunifiedframework
to understand their own cognitive and perceptual mecha-
forcomprehensivelyunderstandingandanalyzingit. Existing
nisms[Ishikawa,2021;EichenbaumandCohen,2014]. Stud-
studiesoftenfocusonspecificaspects,suchasvision-based
iesonhumanspatialcognition,rangingfrommentalmapping
embodiedintelligence,urbanplanning,orremotesensingin-
Allauthorscontributeequallytothiswork. telligence,withoutintegratinginsightsacrossdisciplinesand
5202
rpA
41
]IA.sc[
1v84890.4052:viXra

Embodied Spatial Intelligence Urban Spatial Intelligence Earth Spatial Intelligence
Figure1:Multiplescalespatialintelligenceinrealworld:fromembodiedspatialintelligencetoearthspatialintelligence.
scales. Tobridgethisgap,thissurveytracesthedevelopment hippocampus’sroleinspatialandnon-spatialmemory. Atthe
ofspatialintelligencefromtheperspectiveofhumancogni- neurallevel,spatialrepresentationreliesonplacecellsinthe
tion,fundamentalspatialcapabilities,andmulti-scalesystem hippocampusandgridcellsintheentorhinalcortex[Moser
intelligence from embodied agents, urban intelligence and et al., 2008; Moser et al., 2017]. Place cells activate when
earthscience. Bysynthesizingtheseperspectives,weaimto an individual is in a specific location, while grid cells pro-
provideacohesivefoundationforinterdisciplinaryresearch, videacoordinate-likesystemformappingtheenvironment.
offeringinsightsandinspirationforfutureadvancementsin These cells, along with head direction cells and boundary
spatialintelligence. cells,formtheneuralbasisforconstructingspatialcognitive
Oursurveymakesthreekeycontributions. First,itestab- maps [Long et al., 2025]. Recent advancements, such as
lishes a structured analytical framework for understanding theTolman-EichenbaumMachine(TEM)[Whittingtonetal.,
spatialintelligenceacrossdiversedisciplinesandscales,ad- 2020],highlighttheabilitytogeneralizespatialandrelational
vancing from spatial memory and perception to reasoning memorythroughstructuralabstractionandcross-environment
and higher-level intelligence. Second, it synthesizes exist- representationbygridcells. Comparatively, largelanguage
ingliteratureonspatialintelligenceapplicationswithLLMs models(LLMs)leverageTransformerarchitecturestoemu-
acrossmultiplefields,alongsidediscussionsonspatialmem- latespatialtasks,suchaspositionalencodingandnavigation,
ory,knowledgerepresentation,andspatialreasoninginLLMs, drawingparallelstohippocampalfunctions[Whittingtonet
providing researchers with a timely and valuable reference. al.,2021].
Third,itexploreskeychallengesandopenquestionsininterdis-
2.1.2 SpatialSchema
ciplinaryspatialintelligenceresearch,uncoveringconnections
betweenembodied,urban,andglobal-scaleintelligencewhile Schemasarehigh-levelknowledgestructuresthatencapsulate
outliningpromisingdirectionsforfutureexploration. the common features abstracted from multiple experiences.
Thesestructuresplayacriticalroleintheprocessesofperceiv-
ing,interpreting,andrememberingevents. Theycontinuously
2 BackgroundandTaxonomy
evolvewiththeaccumulationofnewexperiencesandmemo-
2.1 SpatialIntelligenceofHuman ries,influencingtheformation,consolidation,andretrievalof
memory[GilboaandMarlatte,2017]. Inhumanspatialcog-
Here,wefirstreviewhumanspatialintelligenceresearchfrom
nition,schemasplayacrucialrole. Spatialschemasarehigh-
theperspectivesofneuroscienceandcognitivescience,eluci-
levelspatialcognitivestructuresformedthroughthetransfer
datingthepotentialabilitiesandoriginsofspatialintelligence
and generalization of experiences across different environ-
acrossvariousdomainsandscales. Furthermore,weexplore
ments. Unlikecognitivemaps,theirprocessingiscenteredin
therelationshipbetweenspatialintelligenceandotherhuman
specificregionsoftheneocortex. Spatialschemasarehighly
intelligences. Thesefindingswillenhanceourunderstanding
abstractinnature,emergingthroughtheintegrationofover-
ofthecriticalcapabilitiesofcross-domainspatialintelligence
lappingneuralrepresentationsinsimilarenvironments. They
andfacilitatethedevelopmentofmoreeffectivemethodsfor
serve as higher-order spatial representations that transcend
constructingandenhancingspatialintelligence.
specificenvironments,suchastheanticipatedlayoutofamod-
2.1.1 CognitiveMap erncity[Farzanfaretal.,2023].Spatialschemasandcognitive
Spatial cognitive map is the internal representation of envi- maps,asdistinctlevelsofspatialcognitivestructures,interact
ronmentalknowledge,characterizedbysubjectivityanddis- andinfluenceeachother,jointlycontributingtohumanspatial
tortion[Ishikawa,2021]. Tolmanintroducedthisconceptin cognition.
1948[Tolman,1948],laterexpandedbyEichenbaumetal.[Co- Recentresearchhasexploredthesimilaritiesandconnec-
hen,1993;EichenbaumandCohen,2014],emphasizingthe tionsbetweenspatialintelligencebasedonLLMsandhuman

ecnegilletnIlaitapSderewopmE-ledoMegaugnaLegraL
InternalEncoded[Petronietal.,2019],[GurneeandTegmark,2024],[Robertsetal.,2020]
SpatialMemory
andKnowledge ExternallyIntegrated[MansourianandOucheikh,2024][Yuetal.,2024b]
Foundational
Capabilities QualitativeReasoning[Yamadaetal.,2023],[Sharma,2023],[Lehnertetal.,2024],[Lietal.,2024a]
AbstractSpatial
GeometricReasoning: GeoEval[Zhangetal.,2024],GeomVerse[Kazemietal.,2023]
Reasoning
Graph-theoreticalReasoning: GraphInstruct[Luoetal.,2024]
SpatialPerceptionandUnderstanding: LLMI3D[Yangetal.,2024a],3D-MEM[Yangetal.,2024d],
EmbodiedScan[Wangetal.,2024b],Scene-LLM[Fuetal.,2024],SpatialBot[Caietal.,2024]
EmbodiedSpatial
Intelligence
SpatialInteractionandNavigation: RT-2[Zitkovichetal.,2023],VIMA[Jiangetal.,2022],
Guide-LLM[Songetal.,2024],NavGPT[Zhouetal.,2024a],TopV-Nav[Zhongetal.,2024]
SpatialUnderstandingandMemory: GeoLLM[Manvietal.,2023],GeoChat[Kuckrejaetal.,2024],
UrbanCLIP[Yanetal.,2024],ReFound[Xiaoetal.,2024],UrbanKGEnt[NingandLiu,2024]
UrbanSpatial
SpatialIntelligence
Intelligence
forRealWorld SpatialReasoningandIntelligence: GeoReasoner[Lietal.,2024c],LLMob[Wangetal.,2024a],
AgentMove[Fengetal.,2024b],Mobility-LLM[Gongetal.,2024],FLAME[Xuetal.,2024a],
GlobalEncoding: TorchSpatialBenchmark[Wuetal.,2024]
Climate: LLMDiff[Sheetal.,2024],CLLMate[Lietal.,2024b],GenCast[Ravurietal.,2021]
EarthSpatial
Intelligence
Geography: GeoGPT[Zhangetal.,2023a],GeoSEE[Hanetal.,2024],GeoReasoner[YanandLee,2024]
OtherDisciplines: OceanPlan[Yangetal.,2024c],Orca[Lietal.,2024d],MineAgent[Yuetal.,2024a]
Figure2:Ataxonomyoflargelanguagemodel-empoweredspatialintelligencewithrepresentativeexamples.
spatial intelligence, e.g., Momennejad et al. [Momennejad withspatialmemoryandknowledge[Bhandarietal.,2023].
et al., 2024] assessed their cognitive mapping capabilities. Multi-modal large language models (MLLMs) also extend
However, LLMs exhibit limitations, including topological thiscapability,exhibitingtheirmemoryandknowledgeabout
reasoningerrors(e.g.,fictitiouspaths,inefficiency)andvisual- spatial information from both linguistic and visual modali-
spatial perception gaps. While studying cognitive maps in ties [Yang et al., 2024b]. Spatial memory and knowledge
bothhumansandLLMsprovidesvaluableinsightsintospa- can be derived from internal or external sources. Inter-
tialintelligence,significantchallengesremaininenhancing nally, spatial memory and knowledge are encoded within
LLMs’schemalearningandspatialsyntaxintegration. theparametersofLLMsduringpretrainingorpost-training
stages [Petroni et al., 2019; Gurnee and Tegmark, 2024;
2.2 TaxonomyofSpatialIntelligence Roberts et al., 2020]. Externally, LLM’s can utilize outer
Buildingonhumanspatialmemoryandintelligence,wepro- spatialmemoryorknowledgestorageforspecificinformation
poseataxonomyforspatialmemoryandintelligenceinLLMs, whenneeded[MansourianandOucheikh,2024]. LLMs’spa-
asillustratedinFigure2,andprovideacomprehensivesurvey tialmemoryandknowledgeisanessentialpartoftheirspatial
ofcurrentresearchbasedonthisframework. Specifically,we intelligence. Manygeneralandspatial-specifictasksarebased
firstintroducethefoundationalcapabilitiesthatenablespatial onaccurateandadequatememoryandknowledgeaboutthe
intelligenceinLLMs,whicharedividedintospatialmemory
spatialenvironment,includingquestionanswering[Maietal.,
andknowledge,aswellasabstractspatialreasoningabilities.
2021;Yamadaetal.,2023],navigation[Epsteinetal.,2017;
Subsequently, we focus on the application of spatial intelli- Feng et al., 2024c], and geolocalization[Haas et al., 2024].
genceintherealworld,exploringthreedimensions:embodied PracticestoimproveLLM’sspatialmemoryandknowledge
intelligence,urbanintelligence,andearthintelligence. emerge along the bloom of pre-trained generative models.
Varioustrainingmethodsareimplementedtoencodespatial
information[Fengetal.,2024a]. Otherworksintegrateexter-
3 FoundationalCapabilitiesofSpatial
nalknowledgebasetoprovidespatialmemoryandknowledge
IntelligenceinLLMs [Yu et al., 2024b]. Previous works have also attempted to
leveragecompressedspatialknowledgewithinLLMs[Manvi
3.1 SpatialMemoryandKnowledgeinLLMs
etal.,2023].
Spatial memory refers to the cognitive ability to recall spa-
tial relationships, entities, and attributes encountered in the Despite these rapid advancements, challenges remain in
past. Spatialknowledge,abroaderconcept,encompassesnot the domain of spatial memory and knowledge in LLMs.
onlythismemorybutalsocommonsensereasoningandlogical Onesignificantchallengeishallucination[Leeetal.,2022],
thinkingrelatedtospace. Generalspatialmemoryandknowl- where LLMs may generate non-factual or non-faithful con-
edgecombinebothabstractspatialcognitionandreal-world tents[Huangetal.,2023a],underminingtheeffectivenessof
environmentalcapabilities. taskinspatialcontexts. Anotherpressingchallengeisknowl-
Recently, state-of-the-art large language models (LLMs) edgeediting[Zhangetal.,2023c]. Giventhedynamicnature
havedemonstratedtheirproficiencyinhandlingspatialtasks ofthespatialenvironment,itisnecessarytocontinuallyand

Sources
Spatial Memory and Knowledge in LLMs
Challenges Internal Pre-
Spatial memoryand training/
Spatial Relation
Hallucination knowledgeareencoded Post-
Mitigation Entity and Attribute withinthe parameters training
Knowledge Commonsense Reasoning
Editing External
Spatial logical thinking
… Spatial memory and Inference
knowledge are storedin
externalknowledgebase
…
Question Answering Navigation Geolocalization
…
Down-stream Tasks
Figure3: ThisfigureillustratesthecoreconceptsofSpatialMemoryandKnowledgeinLLMs. LLMsbuildtheirspatialmemoryand
knowledgefrombothinternalandexternalsourcestoperformtaskslikequestionanswering,navigation,andgeolocalization,whilealsofacing
challengessuchashallucinationmitigationandknowledgeediting.
timelyupdateLLM’smemoryandknowledgetoreflectaccu- demonstratesVLMs’struggleswithdeepgeometricreason-
ratespatialinformation. ingtasksrequiringlonginferencechainsratherthansimple
knowledgeretrieval. Graph-theoreticalreasoningexamines
3.2 AbstractSpatialReasoningofLLMs
models’capabilitiesinunderstandingandmanipulatinggraph
Abstractreasoningabilityisacrucialcognitivecapabilitythat structures. Inthisfield,GraphInstruct[Luoetal.,2024]de-
enablesintelligentagentstosimplifycomplexrealityintoop- velopedacomprehensivetestset,whichrevealedthatLLMs
erablementalmodels. Inthecontextofspatialintelligence, stillstrugglewithcomplexgraphalgorithmslikeminimum
abstractreasoningplaysacrucialrole: itnotonlysimplifies spanningtrees,Hamiltonianpaths,andshortestpaths. How-
complexphysicalspacesintomanageablementalmodelsbut ever, theirresearchalsodemonstratedthattheselimitations
alsoprovidesafoundationforhigher-levelspatialcognition, canbeovercomethroughstructuredtrainingapproachesthat
serving as a vital bridge between objective spatial environ- emphasizeintermediatereasoningsteps. Besides,Xu[Xuet
mentsandcognitiverepresentations. al.,2025]etal.pioneerapsychometricframeworkthatdefines
With LLMs showing promise in cognitive tasks, assess- fivebasicspatialabilities(BSAs)invision-languagemodels
ingtheirspatialabstractreasoningcapabilitieshasemerged (VLMs), while highlighting issues such as weak geometry
asacriticalresearchdirection, bothforunderstandingtheir encodingandtheabsenceofdynamicsimulationcapabilities.
limitationsandguidingfutureimprovements. Currentassess- In summary, current evaluations across these three direc-
ments of LLMs’ spatial abstract reasoning capabilities pri- tionsrevealthatpre-trainedLLMsprimarilyrelyonlanguage
marily focus on three directions: qualitative spatial reason- understanding to process abstract spatial problems, lacking
ing[Yamadaetal.,2023;Sharma,2023;Lehnertetal.,2024; genuinespatialcognitiveabilities. Methodologicalimprove-
Li et al., 2024a], geometric reasoning [Zhang et al., 2024; ments,includingstructuredreasoningframeworks,knowledge-
Kazemi et al., 2023], and graph-theoretical reasoning [Luo guidedtraining,andintermediateprocesssupervision,have
et al., 2024]. Qualitative spatial reasoning evaluates mod- shownpromiseinaddressingtheselimitations. Movingfor-
els’ ability to understand and reason about spatial relations ward,thefieldrequiresbothmorecomprehensiveevaluation
and transformations through linguistic descriptions. In this standards and meaningful comparisons with human perfor-
domain,LLMshaverevealedsignificantperformancedegra- mancetobetterunderstandandadvanceLLMs’spatialreason-
dationinmulti-hopreasoningtaskswhiledemonstratingthat ingcapabilities.
structuredthinkingframeworkscaneffectivelymitigatethese
limitations [Li et al., 2024a]. In spatial planning problems,
4 LLMbasedSpatialIntelligencefortheReal
[Lehnertetal.,2024]showthattrainingstrategieslikesearch
World
dynamics bootstrapping have shown notable improvements
in complex spatial planning tasks. Geometric reasoning fo-
4.1 EmbodiedSpatialIntelligence
cusesonassessingmodels’understandingofmathematical-
geometricconceptsandtheirapplicationsinspatialproblem- AsshowninFig.5,spatialintelligenceinembodiedAIcom-
solving. GeoEval[Zhangetal.,2024]comprehensivelyeval- prisestwokeystages: 1)spatialperceptionandunderstanding,
uatesLLMsacrossvariousgeometrydomainsandidentified whereagentsacquireandprocessspatialinformationtocon-
theirweaknessininversereasoningcomparedtoforwardrea- structinternalrepresentationsoftheenvironment,and2)spa-
soningwhileshowingtheeffectivenessofproblemrephrasing tialinteractionandnavigation,wheretheserepresentationsare
strategies. GeomVerse[Kazemietal.,2023]systematically leveragedformovement,taskexecution,anddecision-making.

Abstract Spatial Modeling in LLMs
Mental Models for Spatial Tasks
Qualitative Geometric Graph
Spatial Relations Shapes Networks
Planning Problem solving Paths
Transformations Visual logic Patterns
… … …
Challenge: Bridging Language Understanding to Spatial Cognition
Figure4: ConceptualframeworkofAbstractSpatialReasoning. Theframeworkillustratesthreeprimarydimensionsofspatialreasoning
capabilities:qualitativereasoning,geometricreasoning,andgraphreasoning.LLMsstillfacethechallengeofbridginglanguageunderstandto
abstractspatialcognition.
4.1.1 SpatialPerceptionandUnderstanding Mem [Yang et al., 2024d] introduces multi-view Memory
Spatial perception and understanding are essential for em- Snapshotstostoreexploredspatialdataandfrontiersnapshots
bodied intelligence, allowing agents (e.g., robots) to navi- toidentifyunexploredareas,helpingagentsbalanceknowl-
gate, interact, and reason about their surroundings. Recent edgeretrievalandactiveexploration. Thisapproachenhances
researchhasexploredhowmulti-modallargelanguagemodels lifelong learning and autonomous adaptation, yet ensuring
(MLLMs)enhancethesecapabilitiesbyintegratingvisualand scalabilityanddevelopingefficientretrievalmechanismswill
textualdata,improvingspatialreasoning,andenablinginter- beimportantforpracticaldeployment.
activedecision-making. Advancementsinthisfieldprimarily Asresearchprogresses,improvingmulti-modalfusion,re-
involvethreeaspects: multi-modalspatialperception,scene- finingspatialreasoning,andoptimizingmemorymechanisms
levelspatialreasoning,andmemory-basedspatialexploration. willbecrucialforadvancingLLM-drivenspatialperception
Multimodal spatial perception focuses on fusing RGB, andunderstandinginembodiedintelligence.
depth,andtextualinformationtoenhanceobjectlocalization
andunderstanding.Forinstance,LLMI3D[Yangetal.,2024a] 4.1.2 SpatialInteractionandNavigation
enables3Dobjectpositionestimationfromasingle2Dim- Spatial interaction and navigation involve action execution
ageusingspatial-enhancedfeatureextractionand3Dquery basedonspatialperceptionandunderstanding. Theactions
token-baseddecoding. SpatialBot[Caietal.,2024]integrates includeplanningroboticactionsandpredictingfuturetrajec-
depthperceptiontoimproveroboticmanipulationandspatial toriesinspatialenvironments. Emergingresearchhasdived
reasoning,supportedbyitsSpatialQAdataset,whichtrains intocombiningMLLMsinspatialinteractionandnavigation.
modelsindepthestimationandobjectgrounding. Whilethese Progressinthisareamainlyfocusesontwoaspects: motion
approachesexpandLLMs’perceptualabilities,challengesre- controlandnavigation.
mainineffectivelyintegratingmulti-modaldataandimproving Motioncontrolcanbecategorizedintosimpleactiongen-
fine-graineddepthreasoning. eration and interaction with a complex environment. The
Beyondobject-levelperception,scene-levelspatialreason- formerappliestheperceptionabilityofMLLMstodirectly
ingenablesagentstounderstandspatialrelationships,align generatethetargetaction. Forexample,RT-2[Zitkovichetal.,
multi-viewinformation,andinterpretdynamicenvironments. 2023]integratesvision-languagemodels(VLMs)pre-trained
Video-3D LLM [Zheng et al., 2024] enhances video-based on internet-scale data into robot actions generation. VIMA
LLMsbyembedding3Dspatialcoordinatesintovideofea- [Jiangetal.,2022]leveragesatransformer-basedarchitecture
tures, supporting 3D question answering, visual grounding, designedtoprocessmultimodalpromptsandgeneratemotor
anddensecaptioning. Scene-LLM[Fuetal.,2024]integrates actionsautoregressively. However,inacomplexenvironment,
egocentric and global 3D scene representations, using 3D the reasoning ability enables spatial intelligence to handle
point-basedfeaturesformoreeffectivesceneunderstanding open-settasks. VexPoser[Huangetal.,2023b]generates3D
andinteractiveplanning.Thesemodelsimproveagents’ability spatialrepresentationsandplanrobotactionsbyleveraging
toprocessspatialinformationovertime,thoughaligningcon- MLLMs’reasoningandcode-writingcapabilities. GAJ-VGG
tinuous3Dspatialstructureswithlanguage-basedreasoning [Wangetal., 2023]designsagraphneuralnetwork(Graph
remainsanopenchallenge. ActionJustification)toconstructagraphdatarepresentingthe
For long-term spatial reasoning and adaptive decision- layoutofobstaclesandtheirsurroundingenvironmentthrough
making, memory-based spatial exploration allows agents spatialandsemanticrelationships,andtherobotoutputsthe
to retain and recall spatial knowledge. For example, 3D- optimalaction.

Environment with Embodied Complex
Multimodal Data Agent Spatial Task
object identify observe
'
scene understanding manipulate
spatial memory move
Spatial Perception and Spatial Interaction and
Understanding Navigation
Figure5: Asimpleschematicofembodiedspatialintelligence. Theframeworkillustratestwosequentialstages: spatialperceptionand
understandingandspatialinteractionandnavigation.
Navigationtaskperceivesandmemorizesthesurrounding tivemapping,pathfinding,trajectoryoptimization,andeven
environment, and predict the next location through reason- generativespatialdesign.
ing. Based on the category of large model employed, navi- Urbanenvironmentsemergeasanoptimaltestingground
gationcanbedividedintolanguage-model-basedandvision- forthesemacro-scalespatialintelligencedevelopments. As
language-model-basedtask. Byfeedingstructuredtext-based the most complex human-created spatial systems, cities in-
mapsintoanLLM,Guide-LLM[Songetal.,2024]achieves tegrateheterogeneouselementsintomultilayeredstructures
indoorspatialperceptionandleveragesthereasoningcapabili- encompassingphysicalinfrastructure,functionalzones,and
tiesofLLMforpathplanning. NavGPT[Zhouetal.,2024a] socioeconomicnetworks. Theirinherentspatialcomplexity
perceivestheenvironmentbyusingvisionmodelstoconvert hasalreadypropelledinterdisciplinaryresearchfrontierslike
environmentimagesintotextandappliesanLLMtointegrate urban computing and spatial econometrics, establishing es-
thecurrentenvironmentaldescriptionswithhistoricalenviron- sential methodological foundations. As shown in Figure 6,
mentsummaries,andperformtrajectoryplanning. Tobridge to systematically investigate urban spatial intelligence, we
thegapbetweenLLM-basednavigationparadigmsandVision- proposeaframeworkthatdistinguishesbetweenunderstand-
Language-Navigation(VLN)-specializedmodels,NavGPT-2 ing, memory, reasoning, and intelligence capabilities. The
[Zhouetal.,2025]integratesindoorvisualobservationwith former evaluates the ability of LLMs to encode and retain
MLLMs and combining navigation policy networks to im- massive urban elements, while the latter examines their op-
provenavigationalreasoning. TopV-Nav[Zhongetal.,2024] erationalcompetenceinexecutingurban-specifictaskssuch
promptsMLLMswiththespatialarrangementofobjectsusing asmobilitysimulation,serviceallocationoptimization,and
boundingboxesandtextlabelsinthebird-viewenvironment urbanplanning.
imageandconductsdynamicmapscalingandtarget-guided
navigationthroughMLLMreasoning. MP5[Qinetal.,2024] 4.2.1 SpatialUnderstandingandMemory
designsanembodiedsystemthatdecomposescomplexopen- Spatialmemoryreferstotheabilityofmodelstorecallgeo-
worldtasksandperceivestheenvironmentthroughactiveper- graphicinformationandrelationshipsbetweendifferentspatial
ceptioninMinecraftbycallingMLLMS.VSI-Bench[Yanget elements[GurneeandTegmark,2024]. Pre-trainedlargelan-
al.,2024b]probestheMLLMstoconductindoorrouteplan- guagemodels(LLMs)naturallyacquirespatialpriorsfromthe
ningandfindsthatMLLMscanworkeffectivelywithnaive geographicaldataembeddedintheirtrainingcorpus[Manvi
cognitive map design. NWM [Bar et al., 2024] proposes a et al., 2024]. This enables models to recognize, store, and
controllablevideogenerationmodelthatpredictsfuturetarget retrievespatialinformationinawaythatmimicshumanspa-
framefornavigation. tialmemory,whichiscrucialfortasksthatrequiregeographic
reasoningorinterpretation.
4.2 UrbanSpatialIntelligence
Itcanbecategorizedintotwokeyaspects: (1)regionalfea-
Theembodiedspatialintelligenceprimarilyinvolvesinterac- tureunderstandingand(2)reasoningaboutspatiallocations
tionandmovementwithinarm’s-reachmicro-spaces,whereas andrelationships. Tounderstandregionalfeatures,Manviet
atlargerscales,LLMsnecessitatefundamentallydistinctspa- al.[Manvietal.,2023]haveproposedGEOLLMtoextract
tial reasoning paradigms. This paradigm shift stems from geospatialknowledgefromLLMs. Thebiasesingeographic
a critical scaling effect: as spatial dimensions expand, the information learned by LLMs are also examined [Manvi et
agent’s physical size becomes negligible relative to the en- al., 2024]. Kuckreja et al.[Kuckreja et al., 2024] utilize
vironment. Consequently, the agent transitions from oper- satellite images to understand regional features. Satellite
atingwithinabody-embeddedconcretespacetoprocessing images, combined with LLMs, are also used to predict so-
extendedspatialdomainsbeyondimmediatephysicalreach. cioeconomicindicators[Yanetal.,2024]. Moreover,multi-
Thistransformationnecessitatesacognitiveshiftfromsubjec- modaldata—suchassatelliteimages, language, andPoints
tiveembodimenttoobjectivespatialrepresentation,requiring ofInterest(POIs)—isemployedtobetterunderstandregional
LLMstoconceptualizespaceasanindependententitywith characteristics and predict socioeconomic outcomes [Xiao
abstract properties. Such representational capacity enables et al., 2024]. To reason about spatial locations and rela-
advancedspatialfunctionsincludingbutnotlimitedtocogni- tionships, Ning et al.[Ning and Liu, 2024] leverage LLM-

Paradigms Paradigms
• Extract geospatial knowledge with • Store spatial relationship
prompt engineering based on LLM
• Use LLMs to generate • Use tools to construct spatial
training data relationship datasets
Tasks Tasks
Regional Feature Understanding Spatial Relationships
Paradigms Paradigms
• Design a workflow to Urban • Utilize LLM agents
break down tasks • Align multimodal data
Environment
• Integrate multiple factors to
Tasks
reason
Tasks
Geo-localization Mobility Generation Navigation Planning Signal Control
Figure6:Urbanspatialintelligencecanbecategorizedintofourmaintypes:spatialunderstanding,spatialmemory,spatialreasoning,and
spatialintelligence.Eachtypeincludesitsuniquetasksandparadigms.
Agenttoconstructurbanknowledgegraphs[Liuetal.,2022; ofmobilityintentions[Shaoetal.,2024]. Gongetal. designa
Liuetal.,2023]. Wesummarizethekeymethodologiesfor visitingintentmemorynetworkandahumantravelpreference
bothaspectsofspatialunderstanding. Forregionalfeatureun- promptpooltohelpLLMsbetterunderstandthesemanticsof
derstanding,onecommonapproachisextractingpriorknowl- visitingintentionsandtravelpreferences[Gongetal.,2024].
edgethroughpromptengineering,whichinvolvescollecting Spatialintelligenceincitiesfocusesonmakingdecisions
spatial information from open-source data and aligning re- andrespondingbasedonspatialdata,withtheabilitytomake
gional features using multimodal data integration. Another real-timejudgmentsincomplexurbanenvironments. Forex-
importantstrategyisleveragingLLMstoassistdownstream ample, urbanplanningisatypicaltaskthatrequiresspatial
tasksbygeneratingtrainingdataandprovidingguidancefor decision-making. Zhouetal. proposeamulti-agentcollabora-
modeltraining. Regardingspatiallocationsandrelationships, tiveframeworkforparticipatoryurbanplanning[Zhouetal.,
modelscaninferspatialstructuresbasedontheirpre-trained 2024b].Moreover,trafficsignalcontroldynamicallyadjuststo
priors,usingembeddedgeographicknowledgetoreasonabout thespatialenvironment,optimizingthetrafficsystem’soverall
spatialrelationships. Additionally,automatedtoolshavebeen efficiency. LLMLightintegratesthetaskdescriptionandreal-
developedtoconstructandvalidaterelationshipdatasets,fa- timetrafficconditionsintotheprompt,leveragingtheLLM’s
cilitatingthestructuredrepresentationofspatialdataanden- Chain-of-Thoughtreasoningcapabilitytodeterminetheopti-
hancinggeographicreasoning. malcontrolstrategy[Laietal.,2023]. Navigationtaskscan
recognizereal-timechangesincomplexspatialenvironments,
4.2.2 SpatialReasoningandIntelligence
providingoptimalnavigationsolutions. Forexample,Xuet
Spatialreasoningincitiesreferstoderivingnewspatialinfor- al. proposeFlame[Xuetal.,2024a],whichenhancesreason-
mationorpredictingfutureurbandynamicsbasedonspatial ingcapabilitiesinthreestages: fromunderstandingasingle
data or spatial relationships through reasoning. For exam- streetviewdescriptiontasktohandlingpathplanningtasks
ple, GeoReasoner is a framework that integrates LLMs for with multiple images, and ultimately achieving end-to-end
geospatial localization, leveraging high-quality street view spatialdecision-makingfornavigation. Schumannetal. com-
datasets to enhance spatial reasoning capabilities [Li et al., bineLLMwithreal-worldenvironmentalinteraction,using
2024c]. Moreover,someresearchfocusesonreasoningabout alinguisticapproachtoprocesstrajectoriesandvisualobser-
the potential behavior patterns of urban residents. Wang et vations, providing contextual prompts to the LLM to solve
al. useLLMtomodelindividualmobilityintwostages: first, decision-makingproblemsinnavigationtasks[Schumannet
identifyingspatiotemporalpatternsofresidents’mobility,and al.,2024]. Specifically,Zengetal. proposeaPerceive-Reflect-
second,usingthesepatternstogeneratetrajectories[Wanget Planworkflow,enablingtheLLMagenttoautonomouslynav-
al.,2024a]. Similarly,Fengetal. breakthetrajectorypredic- igateinurbanenvironments[Zengetal.,2024].
tionintothreesub-tasksthatinfluencemobility: remembering
4.3 EarthSpatialIntelligence
individualmobilitypatterns,learningsharedspatialtransition
relationshipsofthegroup,andintegratingspatialknowledge Earth Spatial Intelligence (ESI) is an interdisciplinary field
ofurbanstructures,fullyleveragingLLMs’knowledgeofge- attheintersectionofartificialintelligenceandEarthsciences.
ographic space [Feng et al., 2024b]. Shao et al. develop a ESI addresses complex challenges across domains, includ-
ChainofPlannedBehavior,whichleveragesthestep-by-step ingclimatescience,geography,oceanography,andgeology,
reasoningcapabilityofLLMstoachieverecursiveinference by leveraging large-scale spatio-temporal data and cutting-

Climate Geographic Other Disciplines
Paradigms Paradigms Paradigms
• Align multi-modal input data • Integrating GIS tools for autonomous • Align spatial features with
for VLM encoding geospatial workflow LLM input embeddings
• Incorporate the pretrained • Directly query LLM or fine-tune LLM for • Design agentic workflow for
transformer layer in LLM for
geospatial tasks complex spatial reasoning
time-series modeling
Tasks Tasks Tasks
Extreme Weather Temperature GIS Tool Geospatial AUV Wave Height Geological
Forecast Prediction Automation Reasoning Control Prediction Prediction
Spatial Representation
Figure7:Illustrationsofrepresentativeearthspatialintelligencefieldsandparadigms.
edgetechniqueslikeLLMsandmultimodalLLMs(MLLMs). spatialrepresentationtechniques—significantlyoutperforms
These models process vast datasets, uncover patterns, and GPT-4V[Wuetal.,2024]. Thisphenomenonmayunderscore
generateinsightsthatdrivemodeling,decision-making,and the discouraging applicability of large language models to
environmentalresilienceadvancements. Inclimatescience, explicitspatiallearningtasks;however,theyexcelinfew-shot,
LLMs enhance the forecasting of precipitation and climate zero-shot,andsimilarscenarios,anddemonstrateremarkable
eventsbycapturingspatio-temporaldependenciesandintegrat- flexibilityinleveragingmulti-sourcedata.
ingmeteorologicalrasterdata. Ingeography,theycombine
4.3.2 Climate
with Geographic Information Systems (GIS) for automated
Climate events have a strong spatio-temporal dependency,
geospatialreasoningandlocalizedspatialanalyseswhileim-
whichhasbeensummarizedasknowledgeandcommanded
provingcontextualdeductionthroughadaptivemodulesand
bylanguagemodelstosomeextent. Therefore,therehasbeen
contrastivelearning.Inoceanography,vision-languagemodels
sometrialsinutilizinglanguagemodelstopredictorforecast
enablenaturallanguagecontrolofAutonomousUnderwater
climateevents. LLMDiffincorporatedafrozentransformer
Vehicles(AUVs),whilespatio-temporalencodingaddresses
blockfrompre-trainedLLMtoserveasauniversalvisualen-
datasparsity, advancingwaveheightpredictionandmarine
coderlayer,withanintentionofcapturinglong-termtemporal
environmentalmodeling. Ingeology,LLMsintegrateimagery
and surveys to model geological phenomena, improve spa- dependenciesandaccuratelyestimatingmotiontrendsforim-
provedprecipitationnowcasting[Sheetal.,2024]. CLLMate
tialreasoning,andstreamlineremotesensing-basedmineral
incorporated LLM and VLM to align meteorological raster
exploration. ESI is transforming Earth sciences by uniting
datawithweatherandclimateeventinformationandtrainon
naturallanguageunderstanding,multimodalintegration,and
thealigneddatasets,enablingaccurateforecastingofclimate
spatio-temporalreasoning. Thisrapidlyevolvingfieldoffers
events with raster data [Li et al., 2024b]. Notably, for the
profoundopportunitiesforscientificdiscovery,sustainablere-
climatedomain,largemodelshavebeenlargelyappliedand
sourcemanagement,andtacklingpressingglobalchallenges.
explored. GenCast[Ravurietal.,2021]proposedamachine
learning-basedweatherpredictionmodelthatgeneratesaccu-
4.3.1 GlobalEncoding
rate15-dayprobabilisticensembleweatherforecasts. Pangu-
At the global scale, a crucial aspect of intelligence is the Weather[Bietal.,2023]introducedthree-dimensionaldeep
properencodingoflocation,enablingmachinestoperceive networkswithEarth-specificpriorsandahierarchicaltemporal
andunderstandspatialinformationeffectively. Whilelarge
aggregationstrategytoachievemedium-rangeglobalweather
language model-based applications typically represent lo- forecasting. NowcastNet[Zhangetal.,2023b]achievednon-
cation using longitude and latitude [Manvi et al., 2023;
linear nowcasting for extreme precipitation by combining
YanandLee,2024],machinelearninganddeeplearningap-
physical-evolution schemes and conditional-learning meth-
proacheshaveadoptedavarietyofspatialrepresentationmeth-
odstoproducehigh-resolution,physicallyplausibleforecasts
ods[Wuetal.,2024]. Specifically,2Drepresentationmethods with lead times up to 3 hours. Fuxi [Chen et al., 2023] in-
includeapproachessuchasdirecttileIDencoding,sinusoidal
troduced a cascaded machine learning weather forecasting
location encoders, and kernel-based techniques, while 3D
system,whichutilizes39yearsofECMWFERA5reanalysis
methodsencompassCartesiancoordinateencodingandvari-
datatoprovide15-dayglobalforecastsata6-hourtemporal
ousself-supervisedrepresentationstrategies. Accordingtothe resolutionand0.25°spatialresolution. Thesuccessoflarge
TorchSpatialbenchmark[Wuetal.,2024],theSphere2Vec-
modelsinclimatemodelingvalidatesthegrowingprediction
sphereC+ method [Mai et al., 2023]—a self-supervised 3D
capabilitiesthroughtrainingwithlarge-scaledata.
encodingtechniquethatpreservestheorderbetweenanytwo
pointsonEarth—isthemosteffectiveandinformativelocation 4.3.3 Geography
encodingapproach. Notably,eventhedirecttileIDencoding Consideringtherichgeographicknowledgecommandedby
method—despitebeingthelowest-performingamongcommon largelanguagemodels,theirdirectapplicationtogeography-

related tasks has been widely explored. Geography-related patchreprogramming,andinputthemintoLLMforprediction.
tasks either involve the extraction and sensing of location- Yu et al. propose a multi-agent collaboration framework to
relatedknowledgeacrosstheglobalscale,ortasksrequiring enhance the spatial reasoning ability of MLLM for remote-
directjudgmentsandoperationsinvolvingspecificlocations, sensing mineral exploration [Yu et al., 2024a]. It construct
suchaslocalizationandmapping.Twobenchmarkworkscom- multipleMLLMagentsresponsibleforidentifyingdifferent
prehensivelyassesslargelanguagemodels’capacitiesinthese featuresfromdifferentremote-sensingimagesandintegrate
two types of tasks. Manvi et al. find that naively querying themtogether,whichshowsconsiderableperformance.
LLMsusinggeographiccoordinatesaloneisineffectivefor Overall,theapplicationofLLMspatialintelligenceinthese
predictingkeyindicatorslikepopulationdensity;however,in- disciplines can be summarized in two ways: (1) Aligning
corporatingauxiliarymapdatafromOpenStreetMapintothe spatialfeatureswithpromptembeddingsandinputtheminto
prompts significantly improves prediction accuracy [Manvi theLLMforpredictiontasks. (2)Designingagenticworkflow
etal.,2023]. Robertsetal. findthatwhileMLLMsperform withLLMstoenablecomplexspatialreasoning.
wellinmemory-basedgeographictasks,suchasidentifying
locationsorrecognizingpatternsfromprovidedinformation,
5 ChallengesandDiscussions
theyfacesignificantchallengesinreasoning-basedormore
intelligenttasks,suchascontextualdeductionandadvanced 5.1 FundamentalSpatialIntelligence
geospatialanalysis[Robertsetal.,2024]. Toaddresstheex-
Thestudyoffundamentalspatialintelligenceraisesseveral
istinglimitationsoflargelanguagemodels,GeoGPTutilizes
critical questions and challenges. First, the form of spatial
mature GIS tools to tackle geospatial tasks, integrating the
reasoning—thecoreofspatialintelligence—remainsacentral
semantic understanding ability of LLMs with GIS tools in
an autonomous manner [Zhang et al., 2023a]. GeoSEE in- issue: islanguage-basedspatialreasoningthemosteffective
formcurrentlyknown,oraretheremoreuniversalandeffec-
corporatessixinformationcollectionmodules,whichLLMs
tive modeling approaches, such as graph-based representa-
automaticallyselecttoadapttospecificindicatorsandcoun-
tries[Hanetal.,2024]. GeoReasonerincorporatestwocon- tionsormulti-modalframeworks? Second,thecomprehensive
evaluationofgeneralspatialintelligenceposesasignificant
trastive losses to enhance the reasoning ability of language
challenge. Currentframeworksoftenfocusonspecifictasks
modelsbymakingrepresentationsofnearbylocationsandthe
sameentitiesmoresimilar[YanandLee,2024]. ordomains,lackingaunifiedapproachtoassessspatialintel-
ligence across diverse contexts, domains, and scales. Such
4.3.4 OtherDisciplines aunifiedevaluationiscrucialforunderstandingtherelation-
ship between fundamental spatial intelligence and its mani-
LLMs have also been applied in other disciplines such as
festationsinotherdomains. Thisrequiresinvestigatinghow
marinescienceandgeology. With remarkableabilitieslike
corespatialabilities,likementalrotationorspatialmemory,
naturallanguageunderstanding,generalizability,andreason-
translateintohigher-orderapplicationsinspecializedfields.
ing,LLMshavebeenleveragedtotackletypicalchallengesin
Addressingthesequestionswillnotonlyadvanceourtheoreti-
thesedisciplinessuchasdatasparsityandcomplexdecision-
calunderstandingofspatialintelligencebutalsoinformthe
making.
developmentofmorerobustandeffectivemodelsforartificial
Inmarinescience,LLMshavebeenusedforvehiclecontrol
generalintelligence.
duetotheircapabilityofspatialplanningandreasoning. For
example,OceanPlanleveragesLLMstocontrolAutonomous
5.2 EmbodiedSpatialIntelligence
Underwater Vehicle (AUV) through natural language com-
mand[Yangetal.,2024c]. Specifically,itleveragesavision- Forembodiedintelligence,twosignificantchallengesremain
language model to convert image observation into textual in the research on spatial memory and intelligence. First,
semanticmaptomemorizetheexploredoceanenvironment. It thecurrentworkonembodiedintelligenceonlypartiallyin-
furtherproposesahierarchicalplanningframeworktoconvert corporatespriorknowledgeofspatialcognitionasasource
naturallanguagecommandstocontrolinputsforAUV,and of inspiration in method design. While some studies draw
adaptivelyadjusttheplaninspecialcircumstances. Moreover, looselyfromprinciplesofhumanspatialcognition—suchas
the generalization and few-shot learning abilities of LLMs wayfinding,mentalmapping,orobjectmanipulation—these
are suitable for addressing the data-sparsity issue in spatial inspirationsareoftensuperficialandlackasystematicinte-
prediction. Lietal. useLLMstopredicttheoceansignificant gration into the computational models. Therefore, there is
waveheightwithsparseobservationdata[Lietal.,2024d]. To a pressing need for an approach that deeply couples model
enhancethespatialunderstandingabilityofLLM,theyfirst designwiththeunderlyingmechanismsofhumanspatialcog-
encodethespatio-temporalfeaturesfromtheobservationdata nition. Suchanapproachwouldnotonlyimprovetherobust-
throughaspatio-temporalencoder,whichisthenalignedwith nessandadaptabilityofthesemodelsbutalsoprovideinsights
theembeddingsofnaturallanguagepromptandfedintothe intothefundamentalprinciplesofhumanintelligence. How-
LLMtogetherforprediction. ever,achievingthisintegrationisinherentlychallenging,as
Ingeology,Xuetal. useLLMstopredictthegeological itrequiresbridgingthegapbetweencognitivescience,neuro-
conditionintunnels[Xuetal.,2024b]. Theyfirstconstructa science,andembodiedartificialintelligence. Second,research
knowledgegraph(KG)tointegratemultimodaldataandtrans- on embodied intelligence encompasses a wide spectrum of
formthemintolow-dimensionalKGembeddings. Thenthey multi-levelspatialintelligenceandcognition,eachwithdis-
aligntheKGembeddingswithpromptembeddingsthrough tinct characteristics. For example, at the lower level, tasks

suchasroboticmanipulationdemandfine-grainedmotorcon- datarequirementsandfosteringknowledgesharing. Bench-
trolandprecisespatialreasoningtointeractwithobjectsin markingplatformslikeOceanBenchandintegratedsystems
aconstrainedenvironment. Ontheotherhand,higher-level suchasGeoGPTcouldprovidestandardizationandrigorous
taskslikepath-planningforunmannedaerialvehicles(UAVs) evaluation across ESI subfields, enabling targeted advance-
involvelarge-scalespatialreasoning. Therefore,itisanopen ments. Human-in-the-loopsystemsandexplainableAI(XAI)
questionwhetheritispossibletobuildauniversalmodelinte- frameworkscouldfurtherenhanceinterpretabilityandtrust,
gratingmulti-level(i.e.,multi-grained)spatialintelligencein whileadvancesincausalinferenceofferthepotentialtobetter
embodiedAItasks. capturedynamicEarthprocesses. Interdisciplinarycollabo-
rationwillbeessentialtotranslatetheseadvancementsinto
5.3 UrbanSpatialIntelligence actionablesolutionsforclimateresilienceandsustainablede-
velopment. Bytacklingthesechallenges,LLMscanunlock
Although significant progress has been made in urban spa-
moreprecisepredictionsandinsightstoaddressglobalenvi-
tialintelligence,severalcriticalchallengesremain. First,the
ronmentalchallenges.
heterogeneity of urban data poses fundamental limitations:
currentframeworksstruggletoharmonizemultimodalinputs 5.5 RelationwithWorldModel
(e.g.,satelliteimagery,POIs,andmobilitypatterns)intouni-
Inthispaper,weinvestigatespatialunderstandingandtask-
fiedspatialrepresentations,oftenleadingtofragmentedun-
solvingwithinthedomainofspatialintelligence. Theconcept
derstanding. And the most often text-based representation
ofworldmodelshasrecentlyemergedasasignificanttopic
ofcomplexspatialstructuresisalwaysdoubtableforurban
inthisfield,particularlyinembodiedspatialintelligence,pro-
professionals. Second,therobustnessofspatialreasoningre-
pelledbyadvancementsindiffusion-basedgenerativemodels.
mainsconstrainedbyLLMs’relianceonstatictrainingdata,
Asoutlinedinarecentsurvey[Dingetal.,2024],worldmod-
whichinadequatelycapturedynamicurbanphenomenasuch
els—rootedinpsychologicalmentalmodels—servetwokey
asreal-timetrafficflowsorevolvingsocioeconomicfactors.
functions: constructing internal representations to interpret
Third,theinterpretabilitygapinLLM-drivenspatialdecisions
theunderlyingmechanismsoftheworldandpredictingfuture
inurbanplanningandnavigationtasksraisesconcernsabout
statestoguidedecision-making. Ourworkprimarilyfocuses
trustworthiness, particularlywhenmodelsprioritizestatisti-
on the first function, developing internal representations to
calcorrelationsovercausalspatialrelationships. Therefore,
deepenspatialcomprehension. Incomputationalterms,this
futureresearchmayprioritizethreedirections: (1)dynamic
alignswithmodel-basedreinforcementlearning,whereparam-
spatialmodelingtointegratereal-timedatawithLLMs, en-
eterizedenvironmentalmodelsenhanceintelligentbehavior.
ablingadaptiveresponsestourbandynamicswhileaddress-
Whileweaddressmostaspectsofworldmodels,ouremphasis
ingconstraints;(2)Causalspatialreasoningframeworksthat
liesinunderstandingratherthanthegenerativeaspect,such
disentangleenvironmental,social,andinfrastructuralinterde-
asforecastingoutcomes. Foramoreextensiveexplorationof
pendencies,solvingtheconcernandresistanceaboutdealing
generativecapabilities,wereferreadersto[Dingetal.,2024].
spatialinformationintextparadigm; (3)Ethicalchallenges
Lookingforward,weproposethatintegratingthesegenerative
inthemitigationofspatialbias,whichishighlightedbygeo-
capabilitiesintospatialintelligencemodelingholdsconsider-
graphicpriorsinLLM,demandsystematicauditingmethods
ablepromise. Thiscouldenablemorerobustsystemscapable
toensureequitableurbanintelligenceapplications.
ofnotonlyunderstandingbutalsopredictingandactingwithin
thephysicalworld,potentiallyaddressinglimitationsseenin
5.4 EarthSpatialIntelligence
currentfoundationmodels,suchasthelackofgranularityin
LLMholdstransformativepotentialforadvancingEarthSpa- urbanknowledgehighlightedbyFengetal.[Fengetal.,2024a;
tial Intelligence, but several challenges must be overcome Fengetal.,2024c].
tofullyrealizetheircapabilities. Onekeylimitationistheir
performanceinreasoning-intensivetasks,suchascontextual 6 Conclusion
deductionandadvancedspatialanalysisingeography,geol-
Thispaperbeginswithadiscussionofhumanspatialintelli-
ogy, and other domains, where bottlenecks persist. While
genceresearchinneuroscienceandcognitivescience,review-
multimodalLLMs(MLLMs)andemergingframeworkslike
ingandsummarizingstudiesonspatialintelligenceacrossvar-
GeoReasoner and MineAgent show promise by leveraging
iousdisciplines,particularlyatdifferentspatialscales,since
contrastive learning and multi-agent systems, further inno-
theeraofLLMs. Itaimstoprovideacomprehensiveoverview
vation is required to achieve robust geospatial understand-
of spatial intelligence research across domains, helping to
ing. The integration of domain-specific data also presents
contextualizeexistingstudiesandinspirefutureresearchdi-
significanthurdles. Forinstance,marinesciencesoftengrap-
rections. We believe that cross-domain spatial intelligence
ple with data sparsity, necessitating tailored solutions like
researchatmulti-scaleswillemergeasacrucialareaofstudy
OceanGPT and spatio-temporal encoders. Meanwhile, do-
in the future, generating significant impacts and profound
mains like geology and climate science depend heavily on
applicationsacrossmultiplefields. Furthermore,in-depthin-
complexandmultimodalinputs,includingknowledgegraph
vestigationsintospatialintelligencewill,inturn,informthe
embeddingsandspecializedprompts,whichdemandseamless
developmentofgeneralartificialintelligence,layingasolid
alignmentwithinLLMarchitectures. Futureresearchdirec-
foundationforhumanity’sadvancementtowardtrueartificial
tionsincludeleveragingtransferlearningtoadaptpre-trained
generalintelligence.
modelsacrossrelatedEarthsciencedomains,therebyreducing

References and Yong Li. Citybench: Evaluating the capabilities of
largelanguagemodelsforurbantasks,2024.
[Baretal.,2024] Amir Bar, Gaoyue Zhou, Danny Tran,
TrevorDarrell,andYannLeCun. Navigationworldmodels. [Fuetal.,2024] RaoFu,JingyuLiu,XilunChen,YixinNie,
arXivpreprintarXiv:2412.03572,2024. andWenhanXiong. Scene-llm: Extendinglanguagemodel
for3dvisualunderstandingandreasoning. arXivpreprint
[Bhandarietal.,2023] Prabin Bhandari, Antonios Anasta-
arXiv:2403.11401,2024.
sopoulos, andDieterPfoser. Arelargelanguagemodels
geospatiallyknowledgeable? InProceedingsofthe31st [GilboaandMarlatte,2017] Asaf Gilboa and Hannah Mar-
ACMInternationalConferenceonAdvancesinGeographic latte.Neurobiologyofschemasandschema-mediatedmem-
InformationSystems,pages1–4,2023. ory. Trendsincognitivesciences,21(8):618–631,2017.
[Bietal.,2023] Kaifeng Bi, Lingxi Xie, Hengheng Zhang, [Gongetal.,2024] LetianGong,YanLin,XinyueZhang,Yi-
Xin Chen, Xiaotao Gu, and Qi Tian. Accurate medium- wenLu,XuediHan,YichenLiu,ShengnanGuo,Youfang
rangeglobalweatherforecastingwith3dneuralnetworks. Lin, and Huaiyu Wan. Mobility-llm: Learning visit-
Nature,619(7970):533–538,2023. ing intentions and travel preferences from human mo-
bility data with large language models. arXiv preprint
[Caietal.,2024] WenxiaoCai,YaroslavPonomarenko,Jian-
arXiv:2411.00823,2024.
hao Yuan, Xiaoqi Li, Wankou Yang, Hao Dong, and
BoZhao. Spatialbot: Precisespatialunderstandingwith [Guptaetal.,2021] AgrimGupta,SilvioSavarese,etal. Em-
visionlanguagemodels. arXivpreprintarXiv:2406.13642, bodied intelligence via learning and evolution. Nature
2024. communications,2021.
[Chenetal.,2023] LeiChen,XiaohuiZhong,etal. Fuxi: A [GurneeandTegmark,2024] WesGurneeandMaxTegmark.
cascade machine learning forecasting system for 15-day Languagemodelsrepresentspaceandtime,2024.
globalweatherforecast. npjClim.Atmos.Sci.,2023. [Haasetal.,2024] LukasHaas,MichalSkreta,SilasAlberti,
[Chenetal.,2024] BoyuanChen,ZhuoXu,etal. Spatialvlm: andChelseaFinn. Pigeon: Predictingimagegeolocations.
InProceedingsoftheIEEE/CVFConferenceonComputer
Endowingvision-languagemodelswithspatialreasoning
capabilities. InProc.ofCVPR,2024.
VisionandPatternRecognition,pages12893–12902,2024.
[Cohen,1993] NJ Cohen. Memory, amnesia and the hip- [Hanetal.,2024] SungwonHan,DonghyunAhn,Seungeon
Lee, Minhyuk Song, Sungwon Park, Sangyoon Park, Ji-
pocampalsystem. MITPress,1993.
hee Kim, and Meeyoung Cha. Geosee: Regional socio-
[Dingetal.,2024] Jingtao Ding, Yunke Zhang, Yu Shang, economicestimationwithalargelanguagemodel. arXiv
Yuheng Zhang, Zefang Zong, Jie Feng, Yuan Yuan, preprintarXiv:2406.09799,2024.
Hongyuan Su, Nian Li, Nicholas Sukiennik, et al. Un-
[Huangetal.,2023a] Lei Huang, Weijiang Yu, Weitao Ma,
derstandingworldorpredictingfuture? acomprehensive
Weihong Zhong, Zhangyin Feng, Haotian Wang, Qiang-
surveyofworldmodels. arXivpreprintarXiv:2411.14499,
longChen,WeihuaPeng,XiaochengFeng,BingQin,etal.
2024.
Asurveyonhallucinationinlargelanguagemodels: Prin-
[EichenbaumandCohen,2014] Howard Eichenbaum and ciples,taxonomy,challenges,andopenquestions. arXiv
Neal J Cohen. Can we reconcile the declarative mem- preprintarXiv:2311.05232,2023.
oryandspatialnavigationviewsonhippocampalfunction?
[Huangetal.,2023b] WenlongHuang,ChenWang,Ruohan
Neuron,83(4):764–770,2014.
Zhang,YunzhuLi,JiajunWu,andLiFei-Fei. Voxposer:
[Epsteinetal.,2017] Russell A Epstein, Eva Zita Patai, Composable3dvaluemapsforroboticmanipulationwith
Joshua B Julian, and Hugo J Spiers. The cognitive map languagemodels. arXivpreprintarXiv:2307.05973,2023.
inhumans: spatialnavigationandbeyond. Natureneuro-
[Ishikawa,2021] ToruIshikawa. Spatialthinking,cognitive
science,20(11):1504–1513,2017.
mapping, and spatial awareness. Cognitive Processing,
[Farzanfaretal.,2023] Delaram Farzanfar, Hugo J Spiers, 22(Suppl1):89–96,2021.
MorrisMoscovitch,andRShaynaRosenbaum.Fromcogni-
[Jiangetal.,2022] Yunfan Jiang, Agrim Gupta, Zichen
tivemapstospatialschemas.NatureReviewsNeuroscience,
Zhang, Guanzhi Wang, Yongqiang Dou, Yanjun Chen,
24(2):63–79,2023.
Li Fei-Fei, Anima Anandkumar, Yuke Zhu, and Linxi
[Fengetal.,2024a] Jie Feng, Yuwei Du, Tianhui Liu, Siqi Fan. Vima: Generalrobotmanipulationwithmultimodal
Guo, Yuming Lin, and Yong Li. Citygpt: Empowering prompts. arXivpreprintarXiv:2210.03094,2(3):6,2022.
urban spatial cognition of large language models. arXiv
[Kazemietal.,2023] Mehran Kazemi, Hamidreza Alvari,
preprintarXiv:2406.13948,2024.
AnkitAnand,JialinWu,XiChen,andRaduSoricut. Ge-
[Fengetal.,2024b] JieFeng,YuweiDu,JieZhao,andYong omverse: Asystematicevaluationoflargemodelsforgeo-
Li.Agentmove:Predictinghumanmobilityanywhereusing metricreasoning. arXivpreprintarXiv:2312.12241,2023.
large language model based agentic framework. arXiv
[Kuckrejaetal.,2024] KartikKuckreja,MuhammadSohail
preprintarXiv:2408.13986,2024.
Danish, Muzammal Naseer, Abhijit Das, Salman Khan,
[Fengetal.,2024c] Jie Feng, Jun Zhang, Tianhui Liu, Xin andFahadShahbazKhan. Geochat: Groundedlargevision-
Zhang,TianjianOuyang,JunboYan,YuweiDu,SiqiGuo, languagemodelforremotesensing. InProceedingsofthe

IEEE/CVF Conference on Computer Vision and Pattern [Luoetal.,2024] Zihan Luo, Xiran Song, Hong Huang,
Recognition,pages27831–27840,2024. Jianxun Lian, Chenhao Zhang, Jinqi Jiang, and Xing
[Laietal.,2023] SiqiLai,ZhaoXu,WeijiaZhang,HaoLiu, Xie. Graphinstruct: Empoweringlargelanguagemodels
withgraphunderstandingandreasoningcapability. arXiv
and Hui Xiong. Large language models as traffic signal
preprintarXiv:2403.04483,2024.
controlagents: Capacityandopportunity. arXivpreprint
arXiv:2312.16044,2023. [Maietal.,2021] Gengchen Mai, Krzysztof Janowicz, Rui
[Leeetal.,2022] NayeonLee,WeiPing,PengXu,Mostofa Zhu,LingCai,andNiLao.Geographicquestionanswering:
Patwary,PascaleNFung,MohammadShoeybi,andBryan challenges,uniqueness,classification,andfuturedirections.
Catanzaro. Factualityenhancedlanguagemodelsforopen- AGILE:GIScienceseries,2:8,2021.
ended text generation. Advances in Neural Information [Maietal.,2023] Gengchen Mai, Yao Xuan, et al.
ProcessingSystems,35:34586–34599,2022. Sphere2Vec: A general-purpose location representa-
[Lehnertetal.,2024] LucasLehnert,SainbayarSukhbaatar, tion learning over a spherical surface for large-scale
DiJia Su, Qinqing Zheng, Paul Mcvay, Michael Rabbat, geospatialpredictions. ISPRSJ.P.RemoteSens.,2023.
and Yuandong Tian. Beyond a*: Better planning with
[MansourianandOucheikh,2024] Ali Mansourian and
transformers via search dynamics bootstrapping. arXiv
RachidOucheikh. Chatgeoai: Enablinggeospatialanalysis
preprintarXiv:2402.14083,2024.
forpublicthroughnaturallanguage,withlargelanguage
[Lietal.,2024a] FangjunLi,DavidCHogg,andAnthonyG models. ISPRSInternationalJournalofGeo-Information,
Cohn. Advancingspatialreasoninginlargelanguagemod- 13(10):348,2024.
els: An in-depth evaluation and enhancement using the
[Manvietal.,2023] RohinManvi,SamarKhanna,Gengchen
stepgamebenchmark. InProceedingsoftheAAAIConfer-
Mai, MarshallBurke, DavidLobell, andStefanoErmon.
enceonArtificialIntelligence, volume38, pages18500–
Geollm: Extractinggeospatialknowledgefromlargelan-
18507,2024.
guagemodels. arXivpreprintarXiv:2310.06213,2023.
[Lietal.,2024b] HaoboLi, ZhaoweiWang, JiachenWang,
[Manvietal.,2024] RohinManvi,SamarKhanna,Marshall
AlexisKaiHonLau,andHuaminQu. Cllmate: Amulti-
Burke, David Lobell, and Stefano Ermon. Large lan-
modalllmforweatherandclimateeventsforecasting.arXiv
guage models are geographically biased. arXiv preprint
preprintarXiv:2409.19058,2024.
arXiv:2402.02680,2024.
[Lietal.,2024c] LingLi,YuYe,BingchuanJiang,andWei
Zeng. Georeasoner: Geo-localization with reasoning in [Momennejadetal.,2024] IdaMomennejad,HoseinHasan-
streetviewsusingalargevision-languagemodel. InForty- beig,FelipeVieiraFrujeri,HiteshiSharma,NebojsaJojic,
firstInternationalConferenceonMachineLearning,2024. HamidPalangi,RobertNess,andJonathanLarson.Evaluat-
ingcognitivemapsandplanninginlargelanguagemodels
[Lietal.,2024d] ZheLi,RonghuiXu,JilinHu,ZhongPeng,
withcogeval. AdvancesinNeuralInformationProcessing
Xi Lu, Chenjuan Guo, and Bin Yang. Ocean significant
Systems,36,2024.
waveheightestimationwithspatio-temporallyawarelarge
languagemodels. InProceedingsofthe33rdACMInterna- [Moseretal.,2008] Edvard I Moser, Emilio Kropff, and
tionalConferenceonInformationandKnowledgeManage- May-BrittMoser.Placecells,gridcells,andthebrain’sspa-
ment,pages3892–3896,2024. tialrepresentationsystem. Annu.Rev.Neurosci.,31(1):69–
89,2008.
[Lietal.,2024e] Zhonghang Li, Lianghao Xia, et al. Ur-
bangpt: Spatio-temporallargelanguagemodels. InProc. [Moseretal.,2017] EdvardIMoser,May-BrittMoser,and
ofKDD,2024. Bruce L McNaughton. Spatial representation in the hip-
pocampal formation: a history. Nature neuroscience,
[Linetal.,2024] JinzhouLin,HanGao,etal. Advancesin
20(11):1448–1464,2017.
EmbodiedNavigationUsingLargeLanguageModels: A
survey. arXiv:2311.00530,2024. [NingandLiu,2024] Yansong Ning and Hao Liu. Ur-
[Liuetal.,2022] YuLiu,JingtaoDing,andYongLi. Devel- bankgent:Aunifiedlargelanguagemodelagentframework
opingknowledgegraphbasedsystemforurbancomputing. for urban knowledge graph construction. arXiv preprint
InProceedingsofthe1stACMSIGSPATIALInternational arXiv:2402.06861,2024.
Workshop on Geospatial Knowledge Graphs, pages 3–7, [Petronietal.,2019] FabioPetroni,TimRockta¨schel,Patrick
2022. Lewis,AntonBakhtin,YuxiangWu,AlexanderHMiller,
[Liuetal.,2023] Yu Liu, Jingtao Ding, Yanjie Fu, and and Sebastian Riedel. Language models as knowledge
Yong Li. Urbankg: An urban knowledge graph system. bases? arXivpreprintarXiv:1909.01066,2019.
ACMTransactionsonIntelligentSystemsandTechnology,
[Qinetal.,2024] Yiran Qin, Enshen Zhou, Qichang Liu,
14(4):1–25,2023.
ZhenfeiYin,LuSheng,RuimaoZhang,YuQiao,andJing
[Longetal.,2025] XiaoyangLong,DanielBush,BinDeng, Shao. Mp5: Amulti-modalopen-endedembodiedsystem
NeilBurgess,andSheng-JiaZhang. Allocentricandego- in minecraft via active perception. In 2024 IEEE/CVF
centricspatialrepresentationscoexistinrodentmedialen- ConferenceonComputerVisionandPatternRecognition
torhinalcortex. NatureCommunications,16(1):356,2025. (CVPR),pages16307–16316.IEEE,2024.

[Ravurietal.,2021] Suman Ravuri, Karel Lenc, Matthew [Wangetal.,2024b] Tai Wang, Xiaohan Mao, Chenming
Willson, Dmitry Kangin, Remi Lam, Piotr Mirowski, Zhu,RunsenXu,RuiyuanLyu,PeisenLi,XiaoChen,Wen-
Megan Fitzsimons, Maria Athanassiadou, Sheleem weiZhang,KaiChen,TianfanXue,etal.Embodiedscan:A
Kashem, Sam Madge, et al. Skilful precipitation now- holisticmulti-modal3dperceptionsuitetowardsembodied
casting using deep generative models of radar. Nature, ai. InProceedingsoftheIEEE/CVFConferenceonCom-
597(7878):672–677,2021. puterVisionandPatternRecognition,pages19757–19767,
2024.
[Robertsetal.,2020] AdamRoberts,ColinRaffel,andNoam
Shazeer. How much knowledge can you pack into [Whittingtonetal.,2020] JamesCRWhittington,TimothyH
the parameters of a language model? arXiv preprint Muller, Shirley Mark, Guifen Chen, Caswell Barry,
arXiv:2002.08910,2020. Neil Burgess, and Timothy EJ Behrens. The tolman-
eichenbaummachine: unifyingspaceandrelationalmem-
[Robertsetal.,2024] JonathanRoberts,TimoLu¨ddecke,Re-
orythroughgeneralizationinthehippocampalformation.
hanSheikh,KaiHan,andSamuelAlbanie. Chartingnew
Cell,183(5):1249–1263,2020.
territories:Exploringthegeographicandgeospatialcapabil-
itiesofmultimodalllms. InProceedingsoftheIEEE/CVF [Whittingtonetal.,2021] James CR Whittington, Joseph
ConferenceonComputerVisionandPatternRecognition, Warren,andTimothyEJBehrens. Relatingtransformers
pages554–563,2024. tomodelsandneuralrepresentationsofthehippocampal
formation. arXivpreprintarXiv:2112.04035,2021.
[Schumannetal.,2024] RaphaelSchumann,WanrongZhu,
[Wuetal.,2024] NeminWu,QianCao,etal. Torchspatial:
WeixiFeng,Tsu-JuiFu,StefanRiezler,andWilliamYang
Alocationencodingframeworkandbenchmarkforspatial
Wang. Velma: Verbalization embodiment of llm agents
representationlearning. InProc.ofNeurIPS,2024.
forvisionandlanguagenavigationinstreetview. InPro-
ceedingsoftheAAAIConferenceonArtificialIntelligence, [Xiaoetal.,2024] CongxiXiao,JingboZhou,YixiongXiao,
volume38,pages18924–18933,2024. JizhouHuang,andHuiXiong. Refound:Craftingafounda-
tionmodelforurbanregionunderstandinguponlanguage
[Shaoetal.,2024] ChenyangShao,FengliXu,BingbingFan,
andvisualfoundations. InProceedingsofthe30thACM
JingtaoDing,YuanYuan,MengWang,andYongLi. Be-
SIGKDDConferenceonKnowledgeDiscoveryandData
yondimitation: Generatinghumanmobilityfromcontext-
Mining,pages3527–3538,2024.
awarereasoningwithlargelanguagemodels.arXivpreprint
arXiv:2402.09836,2024. [Xuetal.,2024a] Yunzhe Xu, Yiyuan Pan, Zhe Liu, and
Hesheng Wang. Flame: Learning to navigate with
[Sharma,2023] Manasi Sharma. Exploring and improving
multimodal llm in urban environments. arXiv preprint
thespatialreasoningabilitiesoflargelanguagemodels. In
arXiv:2408.11051,2024.
ICan’tBelieveIt’sNotBetterWorkshop: FailureModesin
theAgeofFoundationModels,2023. [Xuetal.,2024b] ZhenhaoXu,ZhaoyangWang,ShucaiLi,
Xiao Zhang, and Peng Lin. Geopredict-llm: Intelligent
[Sheetal.,2024] LeiShe,ChenghongZhang,XinMan,and
tunneladvancedgeologicalpredictionbyreprogramming
JieShao. Llmdiff: Diffusionmodelusingfrozenllmtrans-
largelanguagemodels.IntelligentGeoengineering,1(1):49–
formersforprecipitationnowcasting.Sensors,24(18):6049,
57,2024.
2024.
[Xuetal.,2025] WenruiXu,DalinLyu,WeihangWang,Jie
[Songetal.,2024] SangmimSong,SarathKodagoda,Amal
Feng, Chen Gao, and Yong Li. Defining and evaluating
Gunatilake, Marc G Carmichael, Karthick Thiyagarajan,
visuallanguagemodels’basicspatialabilities: Aperspec-
andJodiMartin. Guide-llm: Anembodiedllmagentand
tivefrompsychometrics. arXivpreprintarXiv:2502.11859,
text-basedtopologicalmapforroboticguidanceofpeople
2025.
withvisualimpairments. arXivpreprintarXiv:2410.20666,
[Yamadaetal.,2023] YutaroYamada,YihanBao,AndrewK
2024.
Lampinen, Jungo Kasai, and Ilker Yildirim. Evaluating
[Tolman,1948] Edward C Tolman. Cognitive maps in rats spatial understanding of large language models. arXiv
andmen. Psychologicalreview,55(4):189,1948. preprintarXiv:2310.14540,2023.
[Wangetal.,2023] Xiaohan Wang, Yuehu Liu, Xinhang [YanandLee,2024] YiboYanandJoeyLee. Georeasoner:
Song,BeibeiWang,andShuqiangJiang. Generatingex- Reasoning on geospatially grounded context for natural
planations for embodied action decision from visual ob- languageunderstanding. InProceedingsofthe33rdACM
servation. InProceedingsofthe31stACMInternational InternationalConferenceonInformationandKnowledge
ConferenceonMultimedia,pages2838–2846,2023. Management,pages4163–4167,2024.
[Wangetal.,2024a] Jiawei Wang, Renhe Jiang, Chuang [Yanetal.,2024] YiboYan,HaominWen,SiruZhong,Wei
Yang,ZengqingWu,MakotoOnizuka,RyosukeShibasaki, Chen,HaodongChen,QingsongWen,RogerZimmermann,
NoboruKoshizuka,andChuanXiao. Largelanguagemod- and Yuxuan Liang. Urbanclip: Learning text-enhanced
elsasurbanresidents:Anllmagentframeworkforpersonal urbanregionprofilingwithcontrastivelanguage-imagepre-
mobility generation. arXiv preprint arXiv:2402.14744, trainingfromtheweb. InProceedingsoftheACMonWeb
2024. Conference2024,pages4006–4017,2024.

[Yangetal.,2024a] FanYang,SichengZhao,YanhaoZhang, [Zhengetal.,2024] Duo Zheng, Shijia Huang, and Liwei
Haoxiang Chen, Hui Chen, Wenbo Tang, Haonan Lu, Wang. Video-3dllm: Learningposition-awarevideorep-
Pengfei Xu, Zhenyu Yang, Jungong Han, et al. Llmi3d: resentation for 3d scene understanding. arXiv preprint
Empoweringllmwith3dperceptionfromasingle2dimage. arXiv:2412.00493,2024.
arXivpreprintarXiv:2408.07422,2024.
[Zhongetal.,2024] LinqingZhong,ChenGao,ZihanDing,
[Yangetal.,2024b] Jihan Yang, Shusheng Yang, Anjali W. YueLiao,andSiLiu. Topv-nav: Unlockingthetop-view
Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. Think- spatial reasoning potential of mllm for zero-shot object
inginspace: Howmultimodallargelanguagemodelssee, navigation. arXivpreprintarXiv:2411.16425,2024.
remember,andrecallspaces,2024.
[Zhouetal.,2024a] GengzeZhou,YicongHong,andQiWu.
[Yangetal.,2024c] Ruochu Yang, Fumin Zhang, and Navgpt: Explicit reasoning in vision-and-language nav-
Mengxue Hou. Oceanplan: Hierarchical planning and igation with large language models. In Proceedings of
replanning for natural language auv piloting in large- theAAAIConferenceonArtificialIntelligence,volume38,
scale unexplored ocean environments. arXiv preprint pages7641–7649,2024.
arXiv:2403.15369,2024.
[Zhouetal.,2024b] ZhilunZhou,YumingLin,DepengJin,
[Yangetal.,2024d] YuncongYang,HanYang,JiachenZhou, andYongLi. Largelanguagemodelforparticipatoryurban
PeihaoChen,HongxinZhang,YilunDu,andChuangGan. planning. arXivpreprintarXiv:2402.17161,2024.
3d-mem: 3dscenememoryforembodiedexplorationand
[Zhouetal.,2025] GengzeZhou,YicongHong,ZunWang,
reasoning. arXivpreprintarXiv:2411.17735,2024.
XinEricWang,andQiWu. Navgpt-2: Unleashingnaviga-
[Yuetal.,2024a] Beibei Yu, Tao Shen, Hongbin Na, Ling
tionalreasoningcapabilityforlargevision-languagemod-
Chen,andDenqiLi. Mineagent: Towardsremote-sensing els. InEuropeanConferenceonComputerVision,pages
mineralexplorationwithmultimodallargelanguagemod-
260–278.Springer,2025.
els. arXivpreprintarXiv:2412.17339,2024.
[Zitkovichetal.,2023] Brianna Zitkovich, Tianhe Yu,
[Yuetal.,2024b] Jun Yu, Yunxiang Zhang, Zerui Zhang,
SichunXu,PengXu,TedXiao,FeiXia,JialinWu,Paul
ZhaoYang,GongpengZhao,FengzhaoSun,FanruiZhang,
Wohlhart, Stefan Welker, Ayzaan Wahid, et al. Rt-2:
QingsongLiu,JianqingSun,JiaenLiang,etal. Rag-guided
Vision-language-actionmodelstransferwebknowledgeto
largelanguagemodelsforvisualspatialdescriptionwith
roboticcontrol. InConferenceonRobotLearning,pages
adaptive hallucination corrector. In Proceedings of the
2165–2183.PMLR,2023.
32ndACMInternationalConferenceonMultimedia,pages
11407–11413,2024.
[Zengetal.,2024] Qingbin Zeng, Qinglong Yang, Shunan
Dong, Heming Du, Liang Zheng, Fengli Xu, and Yong
Li. Perceive, reflect, and plan: Designing llm agent for
goal-directedcitynavigationwithoutinstructions. arXiv
preprintarXiv:2408.04168,2024.
[Zhangetal.,2023a] Yifan Zhang, Cheng Wei, Shangyou
Wu,ZhengtingHe,andWenhaoYu. Geogpt: understand-
ingandprocessinggeospatialtasksthroughanautonomous
gpt. arXivpreprintarXiv:2307.07930,2023.
[Zhangetal.,2023b] Yuchen Zhang, Mingsheng Long,
Kaiyuan Chen, Lanxiang Xing, Ronghua Jin, Michael I
Jordan,andJianminWang. Skilfulnowcastingofextreme
precipitationwithnowcastnet. Nature,619(7970):526–532,
2023.
[Zhangetal.,2023c] ZihanZhang,MengFang,LingChen,
Mohammad-RezaNamazi-Rad, andJunWang. Howdo
large language models capture the ever-changing world
knowledge? areviewofrecentadvances. arXivpreprint
arXiv:2310.07343,2023.
[Zhangetal.,2024] Jiaxin Zhang, Zhongzhi Li, Mingliang
Zhang, Fei Yin, Chenglin Liu, and Yashar Moshfeghi.
Geoeval: benchmarkforevaluatingllmsandmulti-modal
models on geometry problem-solving. arXiv preprint
arXiv:2402.10104,2024.
[Zhaoetal.,2024] TianjieZhao,ShengWang,etal. Artifi-
cialintelligenceforgeoscience: Progress,challengesand
perspectives. TheInnovation,2024.
