# Extracted fulltext (pdfplumber)

Source: https://arxiv.org/abs/2602.22638
<!-- page 1 -->

MobilityBench: A Benchmark for Evaluating Route-Planning
Agents in Real-World Mobility Scenarios
ZhihengSong∗ JingshuaiZhang∗ ChuanQin†
ComputerNetworkInformation AMAP,AlibabaGroup ComputerNetworkInformation
Center,ChineseAcademyofSciences Beijing,China Center,ChineseAcademyofSciences
AMAP,AlibabaGroup zhangjingshuai0@gmail.com Beijing,China
Beijing,China chuanqin0426@gmail.com
songzhiheng0426@gmail.com
ChaoWang ChaoChen LongfeiXu
IndependentResearcher AMAP,AlibabaGroup AMAP,AlibabaGroup
China Beijing,China Beijing,China
chadwang2012@gmail.com cc201598@alibaba-inc.com longfei.xl@alibaba-inc.com
KaikuiLiu XiangxiangChu HengshuZhu†
AMAP,AlibabaGroup AMAP,AlibabaGroup ComputerNetworkInformation
Beijing,China Beijing,China Center,ChineseAcademyofSciences
damon@alibaba-inc.com cxxgtxy@gmail.com Beijing,China
zhuhengshu@gmail.com
Abstract struggleconsiderablywithPreference-ConstrainedRoutePlanning,
Route-planningagentspoweredbylargelanguagemodels(LLMs) underscoringsignificantroomforimprovementinpersonalized
haveemergedasapromisingparadigmforsupportingeveryday mobilityapplications.Wepubliclyreleasethebenchmarkdata,eval-
human mobility through natural language interaction and tool- uationtoolkit,anddocumentationathttps://github.com/AMAP-
mediateddecisionmaking.However,systematicevaluationinreal- ML/MobilityBench.
worldmobilitysettingsishinderedbydiverseroutingdemands,non-
Keywords
deterministicmappingservices,andlimitedreproducibility.Inthis
study,weintroduceMobilityBench,ascalablebenchmarkforeval- Largelanguagemodels,route-planningagents,benchmarking
uatingLLM-basedroute-planningagentsinreal-worldmobilitysce-
ACMReferenceFormat:
narios.MobilityBenchisconstructedfromlarge-scale,anonymized
Zhiheng Song, Jingshuai Zhang, Chuan Qin, Chao Wang, Chao Chen,
realuserqueriescollectedfromAmapandcoversabroadspec- LongfeiXu,KaikuiLiu,XiangxiangChu,andHengshuZhu.2026.Mobility-
trumofroute-planningintentsacrossmultiplecitiesworldwide.To Bench:ABenchmarkforEvaluatingRoute-PlanningAgentsinReal-World
enablereproducible,end-to-endevaluation,wedesignadetermin- MobilityScenarios.InProceedingsofMakesuretoenterthecorrectconference
isticAPI-replaysandboxthateliminatesenvironmentalvariance titlefromyourrightsconfirmationemail(Conferenceacronym’XX).ACM,
fromliveservices.Wefurtherproposeamulti-dimensionaleval- NewYork,NY,USA,11pages.https://doi.org/XXXXXXX.XXXXXXX
uationprotocolcenteredonoutcomevalidity,complementedby
assessmentsofinstructionunderstanding,planning,tooluse,and 1 Introduction
efficiency.UsingMobilityBench,weevaluatemultipleLLM-based Theadvanceoflargelanguagemodels(LLMs)hascatalyzedthe
route-planningagentsacrossdiversereal-worldmobilityscenarios emergenceoftool-augmentedagents,whichintegratenaturallan-
andprovideanin-depth analysisof theirbehaviorsand perfor- guagereasoningwithexecutableactionsviaexternalAPIs[21,24].
mance.Ourfindingsrevealthatcurrentmodelsperformcompe- Bygroundinguserintentinprogrammaticinteractionswithreal-
tentlyonBasicinformationretrievalandRoutePlanningtasks,yet worldservices,suchagentssubstantiallybroadentherangeoftasks
theycansupport,fromsimpleinformationretrievaltocomplex
∗Bothareco-firstauthorsandcontributeequallytothiswork.
†Correspondingauthors. decision-makingworkflows,suchaswebnavigation[18,25],com-
puterinteraction[11,17],androuteplanning[4,36].
Permissiontomakedigitalorhardcopiesofallorpartofthisworkforpersonalor
Among these agents, route-planning agents constitute a par-
classroomuseisgrantedwithoutfeeprovidedthatcopiesarenotmadeordistributed
forprofitorcommercialadvantageandthatcopiesbearthisnoticeandthefullcitation ticularlychallengingapplicationdomain,operatingunderdiverse
onthefirstpage.Copyrightsforcomponentsofthisworkownedbyothersthanthe anddynamicreal-worldconstraintsthatshapeeverydayhuman
author(s)mustbehonored.Abstractingwithcreditispermitted.Tocopyotherwise,or
mobility[3,5,27].Real-worldmobilityrequestsextendfarbeyond
republish,topostonserversortoredistributetolists,requirespriorspecificpermission
and/orafee.Requestpermissionsfrompermissions@acm.org. simple point-to-point navigation [33], often involving multiple,
Conferenceacronym’XX, interacting constraints, such as user preferences (e.g., avoiding
©2026Copyrightheldbytheowner/author(s).PublicationrightslicensedtoACM.
highwaysorminimizingtransfers),orderedwaypoints,modality-
ACMISBN978-x-xxxx-xxxx-x/YYYY/MM
https://doi.org/XXXXXXX.XXXXXXX dependentconditions,andtime-sensitiverequirements.Addressing
6202
nuJ
01
]IA.sc[
2v83622.2062:viXra

<!-- page 2 -->

Conferenceacronym’XX, Song&Zhangetal.
Figure1:OverviewofMobilityBench,asystematicbenchmarkforevaluatingroute-planningagents.
suchdemandsrequiresagentstoaccuratelyinterpretnuanceduser thelargestmapandnavigationserviceprovidersinChina,and
instructions,invokeappropriatetravel-relatedAPIs,andgenerate is designed to reflect the diversity and complexity of everyday
executableitinerarieswithreliablecostestimates—includingtravel mobilityneedswhileremovingallpersonallyidentifiableinforma-
time,distance,andtransfercounts—capabilitiesthatremaindifficult tion.Itcoversabroadspectrumofreal-worldroute-planningin-
toevaluatesystematicallyinrealisticmobilitysettings. tents,includingpoint-to-pointrouting,customizedmulti-waypoint
Recentbenchmarksforevaluatingtheplanningcapabilitiesof itineraries,andmultimodalrouteplanningthatintegratesdriving,
LLMsandagents,suchasTravelBench[5]andTravelPlanner[27], walking,cycling,andpublictransit.Inaddition,MobilityBench
primarily focus on high-level itinerary generation and abstract supportspreference-awarenavigation,suchasavoidinghighways
constraintreasoning.Asaresult,theyfallshortofcapturingthe orminimizingtransfers,aswellasmobility-relatedinformation
complexityofrouteplanningforeverydayhumanmobility,which access,includingbusstationdetails,buslineinformation,androad
requiresfine-grainedreasoningoverlarge-scale,map-basedenvi- congestionstatus.Thebenchmarkspansqueriesfromover350
ronmentsanddynamicallychangingconditions.Meanwhile,sys- citiesworldwideandisdesignedtobeeasilyextensible,enabling
tematicallyevaluatingroute-planningagentsinreal-worldmobility continuousexpansiontonewregions,scenarios,andintenttypes.
scenariosstillfacesseveralfundamentalchallenges:(1)scalable Giventheinherentnon-determinismandreproducibilitychal-
scenariocoverage,asevaluationmustspanroute-planningprob- lengesoflivemappingservices,MobilityBenchisbuiltarounda
lemsofvaryingdifficultyandcombinationsofconstraints,ranging deterministicAPI-replaysandbox thatenablesreproducible,end-
fromsimplepoint-to-pointqueriestocomplexmulti-constraint to-endevaluationofroute-planningagents.Duringdatasetcon-
requests;(2)non-determinismoflivemappingAPIs,whosere- struction,responsesfromroutingandpoints-of-interestAPIsare
sponsesvaryovertimeduetotrafficdynamics,serviceavailability, capturedandcachedthroughastandardizedinterface,effectively
andbackendupdates[16,29],therebyunderminingreproducibility freezingtrafficconditionsandservicestatesatthetimeofcollec-
andfaircomparison;(3)comprehensiveandreliableevalua- tion.Duringevaluation,allAPIcallsissuedbyanagentareinter-
tion,aseffectiveassessmentrequiresintegratingmultipleobjective ceptedandresolvedagainstthecachedresponsestore,ensuring
criteriabeyondLLM-basedsubjectivejudging[37]toverifyAPI- thatidenticalinputsconsistentlyyieldidentical,verifiableoutputs.
call validity, constraint satisfaction, and factual grounding; and Byeliminatinguncontrolledenvironmentalvarianceintroduced
(4)extensibleandreproducibleevaluationtoolkit,asrapid byliveservices,thissandbox-baseddesignensuresthatmeasured
advancesinLLMbackbonesandagentframeworksdemandalight- performancefaithfullyreflectsanagent’sreasoningandtool-use
weight,modulartoolkitthatsupportseasydeployment,scalable capabilitiesratherthanfluctuationsinexternalsystems.
dataexpansion,andconsistentevaluationacrosssettings. Wefurtherproposeamulti-dimensionalevaluationprotocolthat
Toaddressthesechallenges,weintroduceMobilityBench,a centersonoutcomevaliditywhileprovidingcomplementaryassess-
scalablebenchmarkforevaluatingroute-planningagentsinreal- mentsofinstructionunderstanding,planning,tooluse,andefficiency.
worldmobilityscenarios.MobilityBenchisconstructedfromlarge-
scale,anonymizedrealuserqueriescollectedfromAmap,oneof

<!-- page 3 -->

MobilityBench:ABenchmarkforEvaluatingRoute-PlanningAgentsinReal-WorldMobilityScenarios Conferenceacronym’XX,
Thisprotocolintegratesmultipleobjectivecriteriatoverifyexe- 2.2 Tool-augmentedAgentBenchmark
cutablecorrectness,constraintsatisfaction,andgroundedAPIus- Buildingontheemergenceoftool-augmentedagentsenabledby
age,enablingfine-grainedandreliableassessmentbeyondsurface- LLMs,recentworkhasfocusedonevaluatingagents’abilityto
levelplausibility.Tofacilitatereproducibleresearchandrapiditera- followinstructionsandinteractwithexternaltools.Forinstance,
tion,wepubliclyreleasethebenchmarkdata,evaluationtoolkit,and ToolBench[22]constructsalarge-scalebenchmarkoverreal-world
documentationathttps://github.com/AMAP-ML/MobilityBench, APIs,requiringagentstoperformsequentialsearchandplanning
supporting easy deployment, extensibility to new agent frame- tocompletecomplexinstructions.𝜏-bench[30]furtheremphasizes
works,andconsistentcomparisonacrossmodelsandsettings. interactiveevaluationbysimulatinguser–agentinteractionsand
measuringbehavioralconsistencyacrossrepeatedtrials.Incontrast
tothesegeneral-purposeevaluations,recentworkinurbancomput-
inghasproposeddomain-specificbenchmarksforagentevaluation.
TravelPlannerintroducesabenchmarkformulti-dayitinerarycon-
2 RelatedWork structionbyintegratingdomain-specifictoolssuchasflightand
restaurantsearch,andevaluatesagentsunderitinerary-levelenvi-
2.1 RoutePlanninginUrbanComputing
ronmental,commonsense,andhardconstraints[27].TravelBench
Routeplanningisalong-standingprobleminurbancomputing, furtherextendsthistasktomulti-turndialoguescenarios,enabling
attractingsustainedattentionfrombothacademiaandindustry theevaluationofagents’abilitytoinferandrefineusers’implicit
duetoitscentralroleinlarge-scaletransportationsystemsand preferencesthroughinteraction[5].Despitetheseadvances,ex-
location-basedservices.Earlystudiesprimarilyfocusedonopti- istingbenchmarksprimarilyfocusonhigh-levelitinerarygenera-
mizing physical costs, such as distance or travel time, under a tionandabstractconstraintsatisfaction,anddonotsystematically
graph-theoreticsetting.Classicalshortest-pathalgorithms,includ- evaluateagents’abilitytoperformfine-grainedrouteplanningun-
ingDijkstra[9]andA*[8,10],werewidelyadoptedtoguarantee dermobility-specificconstraints,suchaspreference-awarerouting
optimalitywhileimprovingscalabilityinreal-worldroadnetworks. (e.g.,avoidinghighwaysorminimizingtransfers),orderedwaypoint
Thesemethodsestablishedthealgorithmicfoundationsofmod- requirements,modality-dependentconditions,andtime-sensitive
ernnavigationsystems,buttypicallyassumehomogeneousobjec- constraints.Toaddressthisgap,weintroduceMobilityBench,ascal-
tivesandwell-definedcostfunctions.Asmobilitydemandsbecame ablebenchmarkdesignedtoevaluateLLM-basedroute-planning
increasinglydiverse,subsequentresearchmovedbeyondsingle- agentsinreal-worldmobilityscenarios.
objectiveoptimizationtowardpreference-awarerouteplanning.
Theseapproachesincorporateuserinterestsandcontextualfac-
3 MobilityBench
tors by integrating routing with recommendation models, such
asINTSR[28].Nevertheless,mostexistingmethodsrelyonstruc- MobilityBenchisascalablebenchmarkforevaluatingroute-planning
turedfeaturesorpredefinedpreferencespaces,whichlimittheir agentsinreal-worldmobilityscenarios.Wefirstdescribehowthe
abilitytoaccommodatelong-tail,ambiguous,orweaklyspecified benchmarkisbuiltfromlarge-scaleanonymizedmobilityqueries
requirementsexpressedinnaturallanguage.Recently,LLMshave andorganizedintoacomprehensivetasktaxonomy.Wethenin-
beenexploredasanewinterfaceforrouteplanning,owingtotheir troduceastructuredground-truthrepresentationthatexplicitly
strongcapabilityinunderstandingcomplexsemanticinstructions. capturestheminimaltoolinteractionsandintermediateevidence
However,priorworkhasshownthatLLMsaloneareunreliable requiredtocorrectlyresolveeachrequest,servingasastableand
forspatialreasoningandconstrainedoptimizationingeographic interpretablereferenceforevaluation.Toensurereproducibility,all
settings[2,12].Tomitigatetheselimitations,hybridframeworks toolinteractionsareexecutedwithinadeterministicreplaysandbox.
havebeenproposedthatcoupleLLMswithtraditionalplanners, Finally,wepresentamulti-dimensionalevaluationprotocolthat
usingLLMsforhigh-leveldecisionguidance[19,35]orintentand leveragesthisstructuredgroundtruthtoassessagentperformance.
constraintextraction[34].Furtherstudiesintroducehierarchical
planningarchitectures[36]andreinforcementlearning–basedopti- 3.1 BenchmarkConstruction
mizationstrategies[6,7,20,23]toimproverobustnessundermulti-
3.1.1 Episode-centricFormulation. Toenablerigorousevaluation
pleobjectivesandconstraints.Inparallel,tool-augmentedlanguage
ofroute-planningagentsinrealisticmobilityscenarios,Mobility-
agentshavedemonstratedstrongcapabilitiesininteractingwith
Benchadoptsanepisode-centricformulation,inwhicheachepisode
real-worldsystemsandcoordinatingexternaltoolsforstructured
encapsulatesaself-containedmobilityrequestsolvableviatool
decision-making,makingthemapromisingparadigmforroute
augmentation.Formally,anepisodeisrepresentedasafour-tuple
planninginreal-worldmobilityscenarios.Existingtravelplanning 𝑒 =(𝑥,𝑧,S,𝑦),where:
agents,however,mainlyfocusonhigh-levelitinerarygeneration
andabstractconstraintreasoning,withouttightlyintegratingse- • 𝑥 denotesananonymizednatural-languageuserquery;
manticintentunderstandingwithlow-levelrouteoptimizationover • 𝑧 encodescontextualinformationassociatedwiththerequest,
realroadnetworks.Asaresult,theyfallshortofcapturingthecom- suchasuserlocation,city,andotherbackgroundvariablesrele-
plexityofrouteplanningrequiredforeverydayhumanmobility.In vanttomobilitydecision-making;
thiswork,weintroduceMobilityBench,ascalablebenchmarkfor • S denotesafixedandreplayablesnapshotofrelevantAPIre-
evaluatingLLM-basedroute-planningagentsinreal-worldmobility sponsesprovidedbythereplaysandbox(Section3.1.4),enabling
scenarios,toadvanceresearchinthisarea. consistentanddeterministicevaluationacrossagentruns;and

<!-- page 4 -->

Conferenceacronym’XX, Song&Zhangetal.
Table1:OverviewoftaskscenariosinMobilityBench,groupedbyintentfamily.
IntentFamily TaskScenario ExampleQuery
POIQuery Whereisthegasstation?
GeolocationQuery WhereamI?
BasicInformation
NearbyQuery SearchforrestaurantsnearBeijingCapitalInternationalAirport.
Retrieval
WeatherQuery WhatistheweatherlikeinWuhantomorrow?
TrafficInfoQuery IsthereatrafficjamonChengduAvenuerightnow?
Route-Dependent RoutePropertyQuery HowfarisitfromHefeitoHuangshan?
InformationRetrieval Arrival/DepartureTimeQuery IfIdrivefrommyhometoCapitalInternationalAirportnow,whenwillIarrive?
Point-to-PointPlanning DrivefromTiananmenSquaretoCapitalInternationalAirport.
BasicRoutePlanning
Multi-stopPlanning RouteplanningstartingfromNo.60QinheRoad,viaYinjiMallandZhenghongCity.
Preference-Constrained Option-ConstrainedRoutePlanning PlanadrivingroutetoShanghaiDisneylandthatavoidstolls/highways.
RoutePlanning Route-ConstrainedPlanning RoutetoShanghaiDisneylandviaPeople’sSquare,avoidInnerRingElevatedRoad.
• 𝑦denotesastructuredground-truthannotationconstructed(Sec- intentspace.Theresultingtaxonomycomprises11taskscenarios,
tion3.1.3)andusedexclusivelytosupporttheautomatedevalua- whicharefurtherorganizedintofourhigh-levelTaskfamilies:
tionprotocol(Section3.2).Itisneverexposedtotheagentand • BasicInformationRetrieval,whichencompassesfundamen-
servessolelyforevaluationanddiagnosticanalysis. talinformation-seekingtasks,includingPOIQuery,Geolocation
Throughoutthiswork,theroute-planningagentsarenotpermitted Query,NearbyQuery,WeatherQuery,andTrafficInfoQuery.
toaskusersforclarification.Consequently,allepisodesaredesigned • Route-DependentInformationRetrieval,whichtargetsin-
tobefullysolvablebasedsolelyontheinitialuserquery𝑥. formationneedsthatrequirecomputingarouteasanintermedi-
atestep,includingRoutePropertyQuery(e.g.,distanceorpath
3.1.2 DataCollectionandTaskTaxonomyConstruction. Mobility-
characteristics)andArrival/DepartureTimeQuery.
Benchisconstructedfromlarge-scale,anonymizedmobilityqueries • BasicRoutePlanning,whichconsistsoftwostandardnaviga-
collectedfromAMapoverthepastsixmonths.Inreal-worldon-the-
tiontasks:Point-to-PointPlanning,routingfromasingleorigin
goscenariossuchasdrivingorwalking,safetyandconvenience
toasingledestination,andMulti-stopPlanning,routingacross
constraintslimitusers’abilitytointeractwithmobiledevices,mak-
multipleintermediatedestinations.
ingvoiceanaturalandprevalentinputmodalityforexpressing • Preference-ConstrainedRoutePlanning,whichcoversroute
mobilityintent.Asaresult,voicequeriesprovidedirectandlargely
planningtasksinvolvingexplicituser-specifiedpreferencesor
unconstrainedexpressionsofrealuserintent,encompassingdes-
constraintsbeyondbasicnavigation.ThisfamilyincludesOption-
tinationgoals,situationalinformationneeds,andexplicitprefer-
ConstrainedRoutePlanning,whichappliestool-native,standard-
enceconstraints.Inourdataset,thesevoicequeriesaretranscribed
izedroutingoptionssuchasminimizingtolls,preferringhigh-
into text and treated uniformly as query inputs for subsequent
ways,optimizingforthefastestroute,fewertransfers,orless
processing.Fromalargecorpusofrawqueries,weconstructthe
walking;andRoute-ConstrainedPlanning,whichenforcesexplicit
benchmarkthroughamulti-stagefilteringandcurationpipeline,
path-levelconstraintsspecifiedbyusers,suchasrequiredway-
resultinginasubstantialcollectionofhigh-qualityepisodes.Under
pointsorexcludedroads.
astrictno-clarificationassumption,whereeachquerymustbeself-
Table1presentsrepresentativeexamplesforeachtaskscenario,
containedandsolvablewithoutfollow-upinteraction,weremove
while detailed scenario definitions and additional examples are
malformed,underspecified,orambiguousrequestsanddeduplicate
providedinAppendixA,TableS1.
near-identicalqueriestoensurediversity.
Followingthisapproach,weleverageQwen-4Btoperformin- 3.1.3 Ground-Truth Construction. To enable automated evalua-
tent classification over the curated queries, identifying diverse tion,weconstructastructuredground-truthannotation𝑦foreach
real-world mobility scenarios that define the task taxonomy of episodefollowingscenario-specificstandardoperatingprocedures
our benchmark. Specifically, we initialize the process with two (SOPs)definedbydomainexperts,whichspecifytheminimalse-
coarse-grainedintentroots:informationaccess(e.g.,POI,traffic, quenceoftoolinteractionsrequiredtocorrectlyresolveaquery.
andweatherlookup)androuteplanning(e.g.,navigationtoadesti- Specifically,weconstructascenario-specificstandardtoolprogram
nation).Toidentifylong-tailandpreviouslyunobservedintents,we thatdefinestheminimalsequenceoftoolcallsrequiredtoanswer
adoptanopen-setlabelingprotocol,wherebyqueriesthatcannot aquery.TheworkflowoperationalizesthecorrespondingSOPas
bealignedwithexistinglabelspromptthemodeltoproposenew astructuredandexecutableprogram,executesitwithinanexist-
candidateintentsalongwithconcisedefinitions.Thesecandidatela- ingagentframeworktoorchestratetoolinvocations,validatesthe
belsaresubsequentlyiterativelyconsolidated,merged,andrefined resultingoutputsagainsthistoricaldatawithreliabilityfiltering,
throughmultipleroundsofexpertadjudication,ensuringseman- andconsolidatesthefullexecutiontracetogetherwithkeyinter-
ticclarity,mutualexclusivity,andcomprehensivecoverageofthe mediateartifactsintoaground-trutharchive.Thestandardtool

<!-- page 5 -->

MobilityBench:ABenchmarkforEvaluatingRoute-PlanningAgentsinReal-WorldMobilityScenarios Conferenceacronym’XX,
programconsistsofthreecoresteps:(i)extractingandnormal-
izingqueryslotssuchaspointsofinterest,temporalconstraints,
travelmodes,anduserpreferences;(ii)resolvingtextuallocations
intostructuredentitiesorgeographiccoordinatesviaPOIretrieval
orgeocodingtools;and(iii)afterparametervalidation,invoking
downstreamtoolsincludingrouting,real-timetraffic,andweather
serviceswhileverifyingconstraintfeasibilitywhenapplicable.The
resultingtoolevidenceisthenconvertedintoastructuredreference
𝑦forautomatedevaluationanddiagnosticanalysis.
3.1.4 Deterministic Replay Sandbox. During ground-truth con-
struction,werelyontoolsprovidedbytheAMapWebServiceAPI1
toderivereferenceoutputs.Duringevaluation,however,agentsare Figure2:GlobalcoverageofMobilityBenchData.
prohibitedfromqueryingliveAPIendpoints,asreal-timeupdates
(e.g.,dynamictrafficandweatherconditions)andexternalfactors InstructionUnderstanding,Planning,ToolUse,andDecisionMaking,
(e.g.,APIratelimits)wouldotherwiseintroducenon-determinism correspondingtothekeystagesofroute-planningreasoning.Each
andcompromisefairandreproduciblecomparisons.Instead,all capabilityisfurtherquantifiedusingasetoffine-grainedindicators,
toolinteractionsareroutedthroughadeterministicreplaysandbox enablingprecisediagnosisofperformancebottlenecksandfailure
thatservespre-recorded,contextuallyconsistentresponses. modesthatareinvisibletoend-to-endmetrics.
Thereplaysandboxreturnsresponsescapturedduringground-
3.2.1 InstructionUnderstanding. Sinceaccurateinterpretationof
truthexecutionandensuresdeterministicbehavioracrossagent
userrequirementsisaprerequisiteforrouteplanning,wefirsteval-
runs.Eachtoolinvocationisresolvedfromapre-recordedcache
uatetheagent’sinstructionunderstandingcapability.Drawingon
keyedbycanonicalizedarguments,suchasnormalizedcoordinates
standardparadigmsinnaturallanguageunderstanding[1,13],this
andstandardtimeformats.Whenanexactcachehitisunavailable,
capabilityisassessedthroughtwoindicators,detailedasfollows:
thesandboxappliestask-appropriatefallbackstrategies,includ-
IntentDetection(ID).Wequantifytheagent’sabilitytounder-
ingfuzzymatchingforentity-basedqueriesandnearest-neighbor
standtheinstructionalintentembeddedinauserquery.Specifically,
spatialmatchingforcoordinate-basedqueries,subjecttoamaxi-
theagentisexplicitlyinstructedtooutputasetofintentlabelscor-
mumdistancethreshold.Alltoolinvocationsundergostrictschema
respondingtothetaskscenariocategoriesdefinedinSection3.1.2.
validation,includingrequired-fieldchecksandtypeandrangecon-
Wemeasureintentdetectionbycomparingtheagent’spredicted
straints.Callsthatfailvalidationorcannotberesolvedaretreated
intentlabel𝑦ˆ (𝑥) withtheground-truthintentlabel𝑦 (𝑥) for
astool-usefailuresandareexplicitlyreflectedintheevaluation ID ID
eachquery𝑥.Apredictionisconsideredcorrectifthesimilarity
metrics(Section3.2),enablingfairandreproducibleevaluation.
betweenthetwolabelsexceedsapredefinedthreshold𝛼 .
threshold
3.1.5 DatasetStatistics. Afterconstructingground-truth,wefilter Theoverallintentdetectionscoreiscomputedas:
outepisodeswhoseanswerscannotbereliablyobtainedorverified 1 ∑︁
viatoolexecution,retainingonlyepisodeswithexecutableand ID= |X| I(sim(𝑦ˆ ID (𝑥),𝑦 ID (𝑥))≥𝛼 threshold ). (1)
checkableoutcomes.Asaresult,MobilityBenchcontains100,000 𝑥∈X
episodes covering diverse geographic regions. Specifically, our InformationExtraction(IE).Thisindicatorevaluatesanagent’s
benchmarkspans22countriesandover350cities(includingmet- abilitytoextractexplicitandimplicitconstraintsfromuserqueries,
ropolitanareas),withalong-taileddistributionacrosslocations. includingspatialattributes(e.g.,originsanddestinations),tempo-
Wereportthescenariodistributionacrossthe11intents,where ralparameters(e.g.,departurewindowsanddurationconstraints),
36.6%ofepisodesbelongtoBasicInformationRetrievaltasks,9.6% andpreference-relatedsignals(e.g.,trafficavoidanceormodality
toRoute-DependentInformationRetrievaltasks,42.5%toBasic priorities).Foraquery𝑥,let𝑦ˆ IE (𝑥)and𝑦 IE (𝑥)denotethepredicted
RoutePlanningtasks,and11.3%toPreference-ConstrainedRoute andground-truthconstraintsets,respectively.Anextractioniscon-
Planningtasks. sideredcorrectonlyifthetwosetsexactlymatch.TheoverallIE
scoreiscomputedas:
3.2 EvaluationProtocol 1 ∑︁
IE= I(𝑦ˆ (𝑥)=𝑦 (𝑥)). (2)
Toenableacomprehensiveandin-depthevaluationofroute-planning |X| IE IE
𝑥∈X
agents across diverse mobility scenarios, we introduce a multi-
3.2.2 Planning. Effective planning is a core capability of LLM-
dimensional evaluation protocol. Existing evaluations predomi-
basedagents,especiallyinreal-worldmobilityscenarioswhere
nantlyrelyonend-to-endsuccessrates,whichtreatagentbehavior
routeplanningrequiresmulti-stepreasoningunderuncertainty.
as a black box and obscure the intermediate failures along the
Thisdimensionevaluatestheagent’sabilitytogeneratealogically
decision-making chain. Such coarse-grained metrics are insuffi-
coherentandsequentialexecutionplanforcomplexroutingtasks.
cientfordiagnosingthecomplexreasoningprocessesrequiredin
TaskDecomposition(DEC).Thisdimensionevaluatesanagent’s
realisticrouteplanningtasks.Toaddressthislimitation,ourpro-
abilitytodecomposeahigh-levelusergoalintoacoherentsequence
tocoldecomposesanagent’sbehaviorintofourcorecapabilities:
ofatomicactions,reflectingwhethertheagentproducestheright
1https://lbs.amap.com/api/webservice/summary stepswithoutomissionsorredundancy.Givenapredictedaction

<!-- page 6 -->

Conferenceacronym’XX, Song&Zhangetal.
sequence𝑉 𝑝𝑟𝑒𝑑(𝑥)={𝑣
1
,𝑣
2
,...,𝑣 𝑛}andthecorrespondingground- 3.2.5 Efficiency. Inadditiontoagentbehavioralquality,weevalu-
truthsequence𝑉 𝑔𝑜𝑙𝑑(𝑥),weassesstaskdecompositionqualityby ateefficiencytocharacterizecomputationaloverheadandpractical
jointlyconsideringstepcoverageandstepcorrectness,thatis, deployability.Weconsiderthefollowingindicator:
DEC-P=
1 ∑︁ |𝑉 𝑝𝑟𝑒𝑑(𝑥)∩𝑓𝐷𝐸𝐶 𝑉 𝑔𝑜𝑙𝑑(𝑥)|
,
I
c
n
on
p
t
u
e
t
x
T
tu
o
a
k
l
e
in
n
fo
(I
r
T
m
)
a
.
t
T
io
h
n
is
p
m
ro
et
c
r
e
i
s
c
s
m
ed
ea
b
s
y
ur
th
es
e
t
m
he
od
cu
el
m
,i
u
n
l
c
a
l
t
u
iv
d
e
in
v
g
ol
s
u
y
m
st
e
e
o
m
f
|X|
𝑥∈X
|𝑉 𝑝𝑟𝑒𝑑|
prompts,taskinstructions,andthehistoricaltrajectoryofobser-
(3)
DEC-R=
1 ∑︁ |𝑉 𝑔𝑜𝑙𝑑(𝑥)∩𝑓𝐷𝐸𝐶 𝑉 𝑝𝑟𝑒𝑑(𝑥)|
,
vationsandactions.AhigherITcounttypicallyreflectsaheavier
|X|
𝑥∈X
|𝑉 𝑔𝑜𝑙𝑑| r
O
e
u
lia
tp
nc
u
e
t
o
T
n
o
l
k
on
en
g-c
(O
on
T
te
).
x
T
tr
h
e
i
a
s
s
m
on
e
i
t
n
r
g
ic
o
q
r
u
a
a
m
nt
o
i
r
fi
e
e
v
s
e
t
r
h
b
e
os
t
e
ot
f
a
e
l
ed
n
b
u
a
m
ck
be
lo
r
o
o
p
f
.
where𝐴∩𝑓𝐷𝐸𝐶 𝐵 = {𝑎 ∈ 𝐴 | ∃𝑏 ∈ 𝐵,𝑓 𝐷𝐸𝐶(𝑎,𝑏) = True} and tokensgeneratedbythemodel.WhilehigherOTindicatemore
𝑓 𝐷𝐸𝐶(·,·)isafunctionthatdetermineswhethertwoatomicactions thoroughreasoning,italsoimpliesincreasedgenerationtimeand
areconsideredamatch. resourceconsumption.
3.2.3 ToolUse. Toolinvocationservesastheinterfacebetweenthe
4 Experiments
agentandthesandboxenvironment.Tocomprehensivelyevaluate
anagent’stoolinvocationcapability,wedefinethreeevaluation 4.1 ExperimentalSetup
indicators:toolselection,schemacompliance,andparameterfilling. 4.1.1 DataSampling. Ourbenchmarkisconstructedfrom100,000
ToolSelection(TS).Thismetricevaluateswhetheranagentcor- episode𝑒collectedfromreal-worldmobilityscenarios.Tobalance
rectlyidentifiestherequiredtool(s)fromacandidatetoolsetT
statisticalsignificancewithcomputationalefficiency,weperformed
basedontheinferreduserintent.Let𝑇 𝑝𝑟𝑒𝑑(𝑥) denotethesetof stratifiedrandomsamplingacrossthe11coreperformanceanalysis
toolsselectedbytheagent,and𝑇 𝑔𝑜𝑙𝑑(𝑥)denotetheground-truth
scenariosdefinedinSection3.1.2,whilejointlyenforcingstratifica-
setofrequiredtools.Wemeasuretoolselectionqualityfromtwo tionbycity.Specifically,westrivetomaintainabalancedsample
complementaryaspects:coverageandredundancy.Coveragere- distributionacrossscenarioswhilemaintainingproportionalcover-
flectswhetherallnecessarytoolsareselected,whileredundancy ageacrossdiverseurbanregionsandcitytiers,therebymitigating
penalizesunnecessarytoolcalls,(foreasiercomparison,wereport geographicbiasduringscenarioselection.Thisjointsamplingstrat-
redundancyasitscomplement. egyyieldsafinalevaluationsetof7,098episodesforsubsequent
1 ∑︁ |𝑇 𝑝𝑟𝑒𝑑(𝑥)∩𝑇 𝑔𝑜𝑙𝑑(𝑥)| analysisofagentperformance.
TS-P= .
|X|
𝑥∈X
|𝑇 𝑝𝑟𝑒𝑑|
4.1.2 LLMBackbones. Weevaluatedadiversesuiteofrepresenta-
(4)
1 ∑︁ |𝑇 𝑔𝑜𝑙𝑑(𝑥)∩𝑇 𝑝𝑟𝑒𝑑(𝑥)| tiveopen-sourceandclosed-sourceLLMsasthebackbonesofrout-
TS-R= ,
|X|
𝑥∈X
|𝑇 𝑔𝑜𝑙𝑑|
(
p
i
l
)
a
s
n
m
n
a
in
ll
g
-a
a
n
g
d
en
la
t
r
s
g
,
e
s
-
p
p
a
a
n
r
n
am
in
e
g
te
a
r
b
d
r
e
o
n
a
s
d
e
r
m
an
o
g
d
e
el
o
s,
f
(
m
ii)
o
M
de
ix
l
t
c
u
h
r
a
e
r
-
a
o
c
f-
t
E
er
x
i
p
st
e
i
r
c
t
s
s
:
Schema Compliance (SC). This metric evaluates whether an (MoE)architectures,and(iii)reasoning-oriented(Thinking)models.
agent’stoolinvocationconformstopredefinedAPIspecifications, Open-sourcebackbones.WeevaluatedtheQwenfamily(Qwen3-
requiringthatallmandatoryparametersareprovidedandthattheir 4B,Qwen3-30B-A3B,Qwen3-32B,Qwen3-235B-A22B)andDeepSeek
valuesfallwithinvalidformatsandranges.Foreachquery𝑥,let models(DeepSeek-R1,DeepSeek-V3.2-Exp).
𝑆𝑇 𝑝𝑟𝑒𝑑(𝑥)denotethesequenceoftoolinvocationsproducedbythe Closed-sourcebackbones.WeevaluatedOpenAIGPTmodels
agent,andlet𝑃(𝑡) denotethesetofparametersassociatedwith (GPT-4.1,GPT-5.2),AnthropicClaudemodels(Claude-Opus-4.5,
eachtoolcall𝑡 ∈𝑆𝑇 𝑝𝑟𝑒𝑑(𝑥).Wedefine𝑓 𝑆𝐶(𝑃(𝑡),𝑡)asanindicator Claude-Sonnet-4.5), and Google Gemini models (Gemini-3-Pro-
functionthatdetermineswhethertheparametersprovidedfora Preview,Gemini-3-Flash-Preview).
tool𝑡 conformtothepredefinedvalidformatsandranges.Along
thisline,theoverallSCscoreiscalculatedby: 4.1.3 AgentImplementations. ToevaluatetheeffectivenessofLLM-
basedagentworkflowsforrouteplanning,weconstructedroute-
1 ∑︁ 1 ∑︁
SC= |X| 𝑥∈X (cid:12) (cid:12) 𝑆𝑇 𝑝𝑟𝑒𝑑(𝑥) (cid:12) (cid:12)𝑡∈𝑆𝑇𝑝𝑟𝑒𝑑(𝑥) 𝑓 𝑆𝐶(𝑃(𝑡),𝑡). (5) p an la d nn P i l n a g n- a a g n e d n - t E s x b e a c se u d te on [2 t 6 w ]. o A re t p t r h e i s s e s n t t a a g ti e v , e w fr e a d m id ew n o o r t k i s n : c R o e r A p c o t r [ a 3 t 2 e ]
alternativeagentframeworkssuchasLLMCompiler,LATS,orTree-
3.2.4 Decision Making. Decision quality evaluates whether an
of-Thought[14,15,31,38].Thisdesignchoicewasmotivatedbytwo
agentcanproduceafinalsolutionandwhetherthatsolutionis
considerations.First,theselectedframeworksarewidelyregarded
correct.Weassessthisdimensionusingthefollowingtwometrics:
asrepresentativeofmainstreamagentreasoningpipelines,cover-
DeliveryRate(DR).Thisindicatormeasurestheproportionof
ingreactiveandplanning-basedparadigms.Second,approaches
queriesforwhichanagentsuccessfullygeneratesacompleteand
suchasLATSandTree-of-Thoughttypicallyincursubstantially
executablefinaloutput(e.g.,afullitinerary)withoutinterruption
highercomputationaloverheadandexhibitlimitedadaptabilityto
ortoolinvocationfailure.Thismetricreflectstheagent’sabilityto
thetask-specificconstraints,toolinteractions,andlatencyrequire-
completetheend-to-endtaskpipeline.
mentsinherentinourroute-planningsetting.
FinalPassRate(FPR).Thisindicatorevaluatestheeffectiveness
ofthegeneratedsolution.Asolutionisconsideredsuccessfulonly 4.1.4 ExperimentalDetails. Toensurereproducibilityandfaircom-
ifitsatisfiesalluser-specifiedexplicitandimplicitconstraints,cap- parison,weappliedaunifiedsetofevaluationsettingsacrossall
turingtheagent’sabilitytoproduceavalidfinaloutcome. LLMbackbonesandagentframeworks.

<!-- page 7 -->

MobilityBench:ABenchmarkforEvaluatingRoute-PlanningAgentsinReal-WorldMobilityScenarios Conferenceacronym’XX,
Table2:PerformanceofmodelsonMobilityBench.Abbreviations:Instr.Und.forInstructionUnderstanding;Dec.Mak.for
DecisionMaking;IDforIntentDetection;IEforInformationExtraction;DECforTaskDecomposition;TSforToolSelection;
SCforSchemaCompliance;DRforDeliveryRate;FPRforFinalPassRate;ITforInputToken;andOTforOutputToken.
Instr.Und. Planning ToolUse Dec.Mak. Efficiency
Model ID IE DEC-P DEC-R TS-P TS-R SC DR FPR IT OT
ReAct
GPT-4.1 85.86 90.07 75.53 74.14 82.38 81.92 97.00 79.23 61.66 18680.81 1166.27
GPT-5.2 82.16 89.65 81.24 62.22 82.42 76.20 95.49 79.09 61.90 18304.90 1166.12
Claude-Sonnet-4.5 88.70 93.06 80.71 74.76 82.83 82.99 97.42 80.62 63.17 18856.68 1311.01
Claude-Opus-4.5 85.99 91.23 84.12 70.15 83.21 83.73 97.52 80.20 62.22 19672.63 1305.40
Gemini-3-Flash-Preview 84.00 88.16 71.95 68.34 90.37 76.46 98.31 85.18 67.90 21072.79 1232.76
Gemini-3-Pro-Preview 83.54 88.75 68.70 65.11 90.74 75.04 98.70 84.38 69.09 20164.76 1242.48
DeepSeek-V3.2-Exp 78.18 90.78 71.85 77.19 87.99 82.19 98.23 84.95 68.88 15427.89 622.05
Qwen3-4B 77.89 86.75 47.24 81.56 80.74 72.82 94.46 63.80 53.80 26078.99 657.78
Qwen3-30B-A3B 74.73 91.23 70.60 72.93 84.04 83.35 97.06 84.57 66.65 15013.79 560.19
Qwen3-32B 80.87 88.46 68.37 77.58 83.08 83.94 96.76 83.16 65.68 15544.50 583.22
Qwen3-235B-A22B 82.13 90.51 72.23 77.75 84.13 84.66 97.24 85.95 66.69 15391.23 604.73
PlanandExecute
GPT-4.1 94.40 94.79 89.46 68.85 84.61 73.26 97.02 80.70 63.40 13426.36 747.35
GPT-5.2 89.58 96.58 81.90 74.68 81.12 75.94 95.94 77.26 59.81 15312.45 1644.18
Claude-Sonnet-4.5 97.21 95.69 89.46 71.81 84.63 78.17 96.89 81.96 64.31 13267.99 863.81
Claude-Opus-4.5 76.82 95.81 88.80 70.99 84.76 76.53 97.22 83.53 65.77 12643.41 808.83
Gemini-3-Flash-Preview 97.28 94.41 89.60 66.18 85.44 68.13 97.86 80.50 62.87 14515.42 784.06
Gemini-3-Pro-Preview 96.35 95.32 88.97 65.71 85.12 64.38 97.35 78.64 62.80 15936.49 815.26
DeepSeek-V3.2-Exp 96.93 95.92 89.62 69.55 83.83 75.28 97.23 80.73 63.06 12394.29 706.14
Qwen3-4B 95.98 94.53 86.83 73.26 81.64 69.20 96.88 78.06 59.55 13612.71 673.03
Qwen3-30B-A3B 95.56 94.35 83.91 71.19 82.91 68.97 97.48 78.81 60.60 14820.45 667.69
Qwen3-32B 96.03 94.63 86.83 66.98 84.25 69.80 97.17 80.24 62.43 13658.79 703.31
Qwen3-235B-A22B 97.24 94.36 89.39 66.96 84.59 73.49 97.01 81.22 64.16 12563.66 703.60
AgentInputs.Eachagentinstancereceivedtheuserqueryalong gapisnarrowingsignificantly.Amongopen-sourcemodels,Qwen3-
withspatialcontextsignals,suchascityandgeographiclocation. 235B-A22B, a MoE architecture activating only 22B parameters
Whentoolusewasenabled,weadditionallyprovidedstructured perforwardpass,achievedaDRof85.95%andanFPRof66.69%
toolschemasorinvocationpatternstostandardizetoolusageacross undertheReActframework.Similarly,DeepSeek-V3.2-Expdemon-
differentframeworksandbackbones. stratedstrongcompetitiveness,attaininganFPRof68.88%while
ModelConfiguration.Tofurthercontrolevaluationvariance,we maintainingsubstantiallylowerinferencecostsduetoitsefficient
setthesamplingtemperatureto0.1forallevaluatedLLMbackbones architecture.Thisprovidesahigh-performanceandcost-effective
andcappedthemaximumoutputlengthat8,192tokens. optionforenterprise-levelprivatedeployments.
AgentConfiguration.Tobalanceinferenceefficiencyandrobust- FrameworkComparison:ReActvs.Plan-and-Execute.Asys-
ness(e.g.,preventingdegeneratetool-callingloops),welimitedthe tematiccomparisonofthetwoexecutionarchitecturesrevealsa
maximumnumberofinferencestepsto10. fundamentaltrade-offbetweentasksuccessrateandcomputational
efficiency.ThefinalpassrateoftheReActisgenerallybetterthan
4.2 ExperimentalResults that of Plan-and-Execute. This is mainly due to its closed-loop
"think-act-observe"mechanism,whichallowstheagenttodynam-
4.2.1 OverallPerformance.
ically adjust its strategy based on real-time results returned by
LLMperformance.UnderthePlan-and-Executeframework,Claude-
tools,whilePlan-and-Execute’sstaticpre-planningshowsasignifi-
Opus-4.5 stands out as the strongest performer, achieved a De-
cantlackofrobustnesswhenfacingdynamicfeedbackinmobile
livery Rate of 83.53% and a Final Pass Rate of 65.77%, both the
scenarios.However,ReAct’ssuperiorrobustnesscomesatanon-
highestamongallevaluatedmodelsinthissetting.WithintheRe-
trivialcomputationalcost.Duetothecontinuousaccumulation
Actframework,Gemini-3-Pro-PreviewattainedthehighestFPRof
ofobservationhistorywithintheinferencecontext,theaverage
69.09%.Thisresulthighlightsitsexceptionalabilitytopreservetask-
numberofinputtokens(IT)consumedbyReActissignificantly
relevantcontextandmaintaingoalfocusacrossextendediterative
higherthanthatofPlan-and-Execute.Acrossallmodels,ReAct’s
inferenceloops.
averageITisapproximately35.38%higherthanPlan-and-Execute’s.
Closed-Sourcevs.Open-SourceModels.AsshowninTable2,
ThisincreasetranslatesdirectlyintohigherAPIcostsandlonger
Claude-Sonnet-4.5,Gemini-3-Pro-Previewstillmaintainedaclear
wall-clockinferencetimes.
leadininstructionunderstandingdimensions,withaveragescores
of90.88%and88.61%undertheReActframework.However,the

<!-- page 8 -->

Conferenceacronym’XX, Song&Zhangetal.
Figure3:Performanceacrossfourhigh-leveltaskfamilies.
4.2.2 ScenarioStudy. Tofurtherrevealthecapabilitiesofthemodel
indifferenttaskscenarios,wecreatedmulti-dimensionalindicator
radarchartsforfourcorecategoriesinFigure3,evaluatingrepre-
sentativeopen-sourceandclosed-sourcemodelsunderbothReAct
andPlan-and-Executeframeworks.Thescenefromlefttoright
representsasignificantincreaseinthedepthoftasklogicandthe
complexityofconstraints,andPreference-constrainedPlanningis
thecategorywherethemodelisthemostlikelytobeerrorasweex-
pected.Inthistypeoftasks,Plan-andExecuteframeworkperforms
bestbecauseitestablishesaclearstrategyinadvance,whichmakes
handlingstructuredtaskswithlogicalordermorepredictableand
efficient,therebysuppressingillusionsandtrajectorydeviations.
Figure 4: Final pass rate comparison (Thinking vs. Non-
thinking)underthePlan-and-Executeframework.
4.2.3 ModelStudy. Weconductamodel-centricstudytoexamine
achievesafinalpassrateof70.46%,servingasacompetitiverefer-
howmodelscalingandreasoningmode(Thinkingvs.Non-thinking)
encepoint.Acrossmodels,enablingthinkingconsistentlyimproves
influence route-planning agent performance on MobilityBench.
performance,withthelargestgainobservedforQwen-30B-A3B,
Scalingeffect.Experimentsrevealaclearperformancegapacross
finalpassrateincreasedby5.98%absolutely.Despitethesegains,
modelsizes(Table2).Underthesamedensearchitecture,scaling
Thinkingsubstantiallyincreasesthegeneratedtokenvolume,lead-
thebasemodelfrom4Bto32Byieldsaconsistentimprovementin
ingtomarkedlyhigherinferencecostandlatency.Thisoverhead
averagesuccessrate,increasingby0.91%.UndertheMoEsetting,
makesitchallengingtodeployThinking-enabledagentsinreal-
Qwen-30B-A3BfurtherscalestoQwen-235B-A22B,bringingan
time,production-gradeonlinesettings.
additionalgainof5.43%.Overall,theseresultsalignwiththeclassic
scalinglaw:increasingparameterscaleleadstohighersuccessrates 5 Conclusion
inreal-worldmobilityscenarios.ByjointlyexaminingDEC-Pand
Inthiswork,wepresentedMobilityBench,ascalablebenchmarkfor
DEC-R, we observethat, compared with smaller models,larger
thesystematicevaluationofLLM-basedroute-planningagentsin
modelstendtoproducelongersolutiontrajectories(i.e.,moreplans)
real-worldmobilityscenarios.Builtfromlarge-scale,anonymized
toexploreabroaderspaceofpossibleoutcomes.Althoughsome
realuserqueries,MobilityBenchcapturedthediversityandcom-
ofthesestepscanberedundant,thismoreexhaustivesearch-and-
plexityofeverydaymobilitydemandswhileenablingreproducible,
verificationprocessultimatelyimprovesthetasksuccessrate.
end-to-endevaluationthroughadeterministicAPI-replaysandbox.
Thinkingvs.Non-thinking.Toexaminetheintrinsicpotential
Wefurtherintroducedamulti-dimensionalevaluationprotocolcen-
ofLLMsoncomplexroute-planningtasks,westudytheimpact
teredonoutcomevalidityandcomplementedbyassessmentsof
ofreasoningmode(Thinkingvs.Non-thinking)whileaccounting
instructionunderstanding,planning,tooluse,andefficiency.Using
fortheextracostandlatencyintroducedbyThinking.Wesample
MobilityBench,weevaluatedmultipleLLM-basedroute-planning
1,000representativeinstancesfromMobilityBenchforacontrolled
agentsacrossdiversereal-worldmobilityscenariosandconducted
comparison,andevaluatehowdifferentreasoningpatternsaffect
anin-depthanalysisoftheirbehaviorsandperformance,reveal-
finaltasksuccess.Figure4reportsthefinalpassrateofeachmodel
ingboththeirstrengthsandlimitationsunderrealisticconditions.
withandwithoutThinkingenabled.
MobilityBenchprovidesarobustandextensiblefoundationforad-
WeevaluateQwen-4B,Qwen-32B,Qwen-30B-A3B,andQwen-
vancingresearchonroute-planningagentsandforenablingfair
235B-A22Bunderbothsettings,andadditionallyincludeDeepSeek-
andreproduciblecomparisonacrossLLMsandagentframeworks.
R1asastrongreasoning-orientedbaseline(Figure4).DeepSeek-R1

<!-- page 9 -->

MobilityBench:ABenchmarkforEvaluatingRoute-PlanningAgentsinReal-WorldMobilityScenarios Conferenceacronym’XX,
References
[24] TimoSchick,JaneDwivedi-Yu,RobertoDessì,RobertaRaileanu,MariaLomeli,
[1] ICMLT2020:20205thInternationalConferenceonMachineLearningTechnolo- EricHambro,LukeZettlemoyer,NicolaCancedda,andThomasScialom.2023.
gies.2020. Proceedingsofthe20205thInternationalConferenceonMachine Toolformer:Languagemodelscanteachthemselvestousetools. Advancesin
LearningTechnologies. NeuralInformationProcessingSystems36(2023),68539–68551.
[2] PalaashAgrawal,ShavakVasania,andChestonTan.2025.CanLLMsPerform [25] JunhongShen,AtishayJain,ZedianXiao,IshanAmlekar,MouadHadji,Aaron
StructuredGraphReasoningTasks?.InInternationalConferenceonPatternRecog- Podolny,andAmeetTalwalkar.2025. WorkflowAgent:TowardsSpecialized
nition.Springer,287–308. WebAgentsUsingProduction-ScaleWorkflowData.InICLR2025Workshopon
[3] SoumyabrataChaudhuri,PranavPurkar,RitwikRaghav,ShubhojitMallick,Man- FoundationModelsintheWild.
ishGupta,AbhikJana,andShreyaGhosh.2025. Tripcraft:Abenchmarkfor [26] LeiWang,WanyuXu,YihuaiLan,ZhiqiangHu,YunshiLan,RoyKa-WeiLee,
spatio-temporallyfinegrainedtravelplanning.arXivpreprintarXiv:2502.20508 andEe-PengLim.2023.Plan-and-solveprompting:Improvingzero-shotchain-
(2025). of-thoughtreasoningbylargelanguagemodels.arXivpreprintarXiv:2305.04091
[4] AiliChen,XuyangGe,ZiquanFu,YanghuaXiao,andJiangjieChen.2024. (2023).
Travelagent:Anaiassistantforpersonalizedtravelplanning. arXivpreprint [27] JianXie,KaiZhang,JiangjieChen,TinghuiZhu,RenzeLou,YuandongTian,
arXiv:2409.08069(2024). YanghuaXiao,andYuSu.2024. Travelplanner:Abenchmarkforreal-world
[5] XiangCheng,YulanHu,XiangwenZhang,LuXu,ZhengPan,XinLi,andYong planningwithlanguageagents.arXivpreprintarXiv:2402.01622(2024).
Liu.2025. TravelBench:AReal-WorldBenchmarkforMulti-TurnandTool- [28] HuiminYan,LongfeiXu,JunjieSun,NiOu,WeiLuo,XingTan,RanCheng,Kaikui
AugmentedTravelPlanning.arXivpreprintarXiv:2512.22673(2025). Liu,andXiangxiangChu.2025.Intsr:Anintegratedgenerativeframeworkfor
[6] XiangxiangChu,HailangHuang,XiaoZhang,FeiWei,andYongWang.2026. searchandrecommendation.arXivpreprintarXiv:2509.21179(2025).
GPG:ASimpleandStrongReinforcementLearningBaselineforModelReasoning. [29] ShunyuYao,HowardChen,JohnYang,andKarthikNarasimhan.2022.Webshop:
InTheFourteenthInternationalConferenceonLearningRepresentations. https: Towardsscalablereal-worldwebinteractionwithgroundedlanguageagents.
//openreview.net/forum?id=inccdtfx8x AdvancesinNeuralInformationProcessingSystems35(2022),20744–20757.
[7] YanqiDai,YuxiangJi,XiaoZhang,YongWang,XiangxiangChu,andZhiwuLu. [30] ShunyuYao,NoahShinn,PedramRazavi,andKarthikNarasimhan.2024. 𝜏-
2026.HarderIsBetter:BoostingMathematicalReasoningviaDifficulty-Aware bench:ABenchmarkforTool-Agent-UserInteractioninReal-WorldDomains.
GRPOandMulti-AspectQuestionReformulation.InTheFourteenthInterna- arXivpreprintarXiv:2406.12045(2024).
tionalConferenceonLearningRepresentations. https://openreview.net/forum?id= [31] ShunyuYao,DianYu,JeffreyZhao,IzhakShafran,TomGriffiths,YuanCao,and
nfURupkdRJ KarthikNarasimhan.2023.Treeofthoughts:Deliberateproblemsolvingwith
[8] DanielDelling,PeterSanders,DominikSchultes,andDorotheaWagner.2009. largelanguagemodels. Advancesinneuralinformationprocessingsystems36
Engineeringrouteplanningalgorithms. InAlgorithmicsoflargeandcomplex (2023),11809–11822.
networks:design,analysis,andsimulation.Springer,117–139. [32] ShunyuYao,JeffreyZhao,DianYu,NanDu,IzhakShafran,KarthikRNarasimhan,
[9] EWDlJKSTRA.1959. ANoteonTwoProblemsinConnexionwithGraphs. andYuanCao.2022.React:Synergizingreasoningandactinginlanguagemodels.
Numer.Math.50(1959),269–271. InTheeleventhinternationalconferenceonlearningrepresentations.
[10] PeterEHart,NilsJNilsson,andBertramRaphael.1968.Aformalbasisforthe [33] JiahaoYu,YihaiDuan,LongfeiXu,ChaoChen,ShuliangLiu,KaikuiLiu,FanYang,
heuristicdeterminationofminimumcostpaths. IEEEtransactionsonSystems XiangxiangChu,andNingGuo.2025.DSFNet:LearningDisentangledScenario
ScienceandCybernetics4,2(1968),100–107. FactorizationforMulti-ScenarioRouteRanking.InCompanionProceedingsofthe
[11] SiyuanHu,MingyuOuyang,DifeiGao,andMikeZhengShou.2024.Thedawnof ACMonWebConference2025.567–576.
guiagent:Apreliminarycasestudywithclaude3.5computeruse.arXivpreprint [34] LiangqiYuan,Dong-JunHan,ChristopherGBrinton,andSabineBrunswicker.
arXiv:2411.10323(2024). 2025.LLMAP:LLM-AssistedMulti-ObjectiveRoutePlanningwithUserPrefer-
[12] ZhehuiHuang,GuangyaoShi,andGauravSSukhatme.2024.CanLargeLanguage ences.arXivpreprintarXiv:2509.12273(2025).
ModelsSolveRobotRouting?arXivpreprintarXiv:2403.10795(2024). [35] JunlinZeng,XinZhang,XiangZhao,andYanPan.2025.A1000×FasterLLM-
[13] MouradJbene,AbdellahChehri,RachidSaadane,SmailTigani,andGwanggil enhancedAlgorithmForPathPlanninginLarge-scaleGridMaps.arXivpreprint
Jeon.2025.Intentdetectionfortask-orientedconversationalagents:Acompara- arXiv:2510.02716(2025).
tivestudyofrecurrentneuralnetworksandtransformermodels.ExpertSystems [36] TaoZhe,RuiLiu,FatemeMemar,XiaoLuo,WeiFan,XinyueYe,ZhongrenPeng,
42,2(2025),e13712. andDongjieWang.2025.Constraint-AwareRouteRecommendationfromNatural
[14] YuxiangJi,ZiyuMa,YongWang,GuanhuaChen,XiangxiangChu,andLiaoni LanguageviaHierarchicalLLMAgents.arXivpreprintarXiv:2510.06078(2025).
Wu.2026.TreeSearchforLLMAgentReinforcementLearning.InTheFourteenth [37] LianminZheng,Wei-LinChiang,YingSheng,SiyuanZhuang,ZhanghaoWu,
InternationalConferenceonLearningRepresentations. https://openreview.net/ YonghaoZhuang,ZiLin,ZhuohanLi,DachengLi,EricXing,etal.2023.Judging
forum?id=ZpQwAFhU13 llm-as-a-judgewithmt-benchandchatbotarena.Advancesinneuralinformation
[15] SehoonKim,SuhongMoon,RyanTabrizi,NicholasLee,MichaelWMahoney, processingsystems36(2023),46595–46623.
KurtKeutzer,andAmirGholami.2024. Anllmcompilerforparallelfunction [38] AndyZhou,KaiYan,MichalShlapentokh-Rothman,HaohanWang,andYu-Xiong
calling.InForty-firstInternationalConferenceonMachineLearning. Wang.2023.Languageagenttreesearchunifiesreasoningactingandplanning
[16] XiaoLiu,HaoYu,HanchenZhang,YifanXu,XuanyuLei,HanyuLai,YuGu, inlanguagemodels.arXivpreprintarXiv:2310.04406(2023).
HangliangDing,KaiwenMen,KejuanYang,etal.2023.Agentbench:Evaluating
llmsasagents.ICLR(2023).
[17] JuntingLu,ZhiyangZhang,FangkaiYang,JueZhang,LuWang,ChaoDu,Qing- A Appendix
weiLin,SaravanRajmohan,DongmeiZhang,andQiZhang.2025.Axis:Efficient
human-agent-computerinteractionwithapi-firstllm-basedagents.InProceed- A.1 MobilityBenchTaskScenarios
ingsofthe63rdAnnualMeetingoftheAssociationforComputationalLinguistics
Tofacilitateathoroughunderstandingofthebenchmark’scoverage
(Volume1:LongPapers).7711–7743.
[18] KaixinMa,HongmingZhang,HongweiWang,XiaomanPan,WenhaoYu,and anddesignrationale,wepresentadetailedtaxonomyoftaskscenar-
DongYu.2023.Laser:Llmagentwithstate-spaceexplorationforwebnavigation. iosinTableS1,includingfine-grainedsubtypesandtheirdefinitions,
arXivpreprintarXiv:2309.08172(2023).
[19] SilinMeng,YiweiWang,Cheng-FuYang,NanyunPeng,andKai-WeiChang. andprovideadditionalrepresentativeexamplesforeachcategory,
2024.Llm-a*:Largelanguagemodelenhancedincrementalheuristicsearchon whicharedesignedtoreflectthediversityofnaturallanguageex-
pathplanning.arXivpreprintarXiv:2407.02511(2024).
pressionsthatusersmayemploywhenissuingmobility-related
[20] YansongNing,RuiLiu,JunWang,KaiChen,WeiLi,JunFang,KanZheng,
NaiqiangTan,andHaoLiu.2025.Deeptravel:Anend-to-endagenticreinforce- instructions.
mentlearningframeworkforautonomoustravelplanningagents.arXivpreprint
arXiv:2509.21842(2025).
[21] ShishirGPatil,TianjunZhang,XinWang,andJosephEGonzalez.2024. Go- A.2 SandboxTools
rilla:Largelanguagemodelconnectedwithmassiveapis. AdvancesinNeural
A core design principle of MobilityBench is to evaluate agents
InformationProcessingSystems37(2024),126544–126565.
[22] YujiaQin,ShihaoLiang,YiningYe,KunlunZhu,LanYan,YaxiLu,YankaiLin,Xin withinarealisticyetreproducibletool-useenvironment.Tothis
Cong,XiangruTang,BillQian,etal.2023.Toolllm:Facilitatinglargelanguage end,weprovideacomprehensivetoolspecificationtableasshown
modelstomaster16000+real-worldapis.arXivpreprintarXiv:2307.16789(2023).
[23] YincenQu,HuanXiao,FengLi,GregoryLi,HuiZhou,XiangyingDai,andXiaoru inTableS2.Itdocumentseachtoolusedinthebenchmarksandbox,
Dai.2025.TripScore:Benchmarkingandrewardingreal-worldtravelplanning includingthetoolname,inputargumentsandoutputfields.The
withfine-grainedevaluation.arXivpreprintarXiv:2510.09011(2025).
sandboxtoolsaresourcedfromtheAMapOpenPlatform.More

<!-- page 10 -->

Conferenceacronym’XX, Song&Zhangetal.
TableS1:MobilityBenchtaskscenarios.Foreachscenario,weprovideaconcisedefinitionandrepresentativeuserqueries.
Scenario Introduction QueryExamples
POISearch Retrieveapointofinterest(POI)bynameor
• FindaStarbucks.
categoryandreturnkeyattributes(e.g.,address,
• SearchforapharmacyinNanshanDistrict.
latitude/longitude).
• Whereistheshoppingmall?
GeolocationQuery Reversegeocodingconvertscoordinates(orthe
• Givememycurrentlocation.
currentlocation)intoanaddress,placename,and
• TellmewhereIamrightnow.
administrativeregion.
• What’sthelatitudeandlongitudeofBeijingRailwayStation?
NearbySearch FindPOIswithinaspecifiedradiusofatarget
• Anyparkinglotswithin500metersofmylocation?
location.
• FindthenearestEVchargingstation.
• Whereisthenearestrestroomnearby?
WeatherQuery Querycurrentweatherandforecastsforatarget
• I’marrivinginHangzhoutomorrow—what’stheweatherlike
areatosupporttraveldecisions.
there?
• What’sthetemperatureinBeijingtomorrowmorning?
• Givea3-dayforecastforShenzhen.
TrafficInfoQuery Retrievereal-timetrafficcongestioninformationfor
• HowistrafficonYan’anElevatedRoadrightnow?
roadsorareas,includingseverityandaffected
• IstherecongestionnearGuomao?
segments.
• Howisthetrafficflowonthewaytotheairport?
RoutePropertyQuery Queryattributesofagivenroute/itinerary(distance,
• HowlongfromLujiazuitoHongqiaobymetro?
duration,transfers,etc.).
• Howmanytransfersarethereonthistransitroute?
• What’sthedistancetoJiuzhaigouValley?
Arrival/DepartureTime Planrouteswithtimeconstraints
• Imustarriveattheairportby7:30;whenshouldIleave?
Query (depart-at/arrive-by)andinferfeasibleschedules.
• Mytraindepartsat9:00PMtonight—what’sthebesttimeto
leaveforNanchangRailwayStation?
• IfIleaveat6PM,canIreachtheconcertby7?
Point-to-PointPlanning Planaroutefromanorigintoadestinationundera
• HowdoIgetfromPudongAirporttoTheBundbysubway?
specifiedtravelmode.
• DrivefromTsinghuaUniversitytoSanlitunnow.
• BikefrommylocationtoZhongshanPark.
Multi-stopPlanning Plananorderedmulti-stoproutethatvisitsmultiple
• StartfromtheGrandHyattBeijing,stopatWangfujingDe-
waypointssequentially.
partmentStore,thenproceedtoBeijingSouthRailwayStation.
• TravelfromGuangzhouSouthRailwayStationtoChimelong
TouristResortviaTianheSportsCenter.
Option-ConstrainedRoute Planroutesbasedonstandarduserpreferences
• Drivetothezoobutavoidhighways.
Planning supportedbytheroutingAPI(e.g.,avoid_tolls,
• Takepublictransitwithatmostonetransfer.
avoid_highways,minimize_transfers).
• Findthecheapestroutetotheairport.
CustomizedPlanning Planroutesunderbespokeconstraintsthatmustbe
• ImusttakeMetroLine2;plantheroutetothestadium.
satisfied(e.g.,designatedline/stop/segment).
• RoutetothehospitalviaPeople’sSquareStation.
• Planaroutetotheairportwiththefewesttrafficlights.
detailedparameterdefinitionsandresponsefielddescriptionsare
availableintheofficialdocumentation2. 2https://lbs.amap.com/api/webservice/summary

<!-- page 11 -->

MobilityBench:ABenchmarkforEvaluatingRoute-PlanningAgentsinReal-WorldMobilityScenarios Conferenceacronym’XX,
TableS2:Overviewofmap-relatedtoolsandtheirtool-functionI/O.
Tool Function Input Output
poi_query Search points of interest (POIs) us- keyword(s),category,city,optionalfil- CandidatePOIs:name,address,coor-
ingkeywords,categories,cityorcity ters(e.g.,limit). dinates,category,briefmetadata.
code.
nearby_poi_query RetrievenearbyPOIswithinaradius center coordinate (lat/lon), radius, Nearby POI list with distance (op-
matchingacategory/keyword. keyword/category, optional filters tional), name, address, coordinates,
(e.g.,limit/sort). category.
reverse_geocoding Convertgeographiccoordinatesinto coordinate(lat/lon). Addressfields(province/city/district,
ahuman-readableaddress. street,number),nearbylandmark/POI
(optional),formattedaddress.
weather_query Querycurrentweatherorforecastfor citynameorcoordinate(lat/lon),time Weatherreport:temperature,precipi-
alocation. range/type(current/forecast). tation,wind,humidity,conditions;air
quality(optional).
traffic_info_query Retrievereal-time/recenttrafficcon- roadsegment/areaidentifierorpoly- Trafficstatus:congestionlevel,speed,
ditionsforaroadsegment/area. line/bbox,optionaltimewindow. incidents/events (optional), times-
tamp,suggestedimpactonETA(op-
tional).
driving_planning Planadrivingroutebetweenorigin origin(lat/lon),destination(lat/lon), Route: distance, ETA, poly-
anddestination. optionalwaypoints,routepreferences line/geometry, turn-by-turn steps,
(avoidhighways/tolls),traffic-aware traffic-awareETA(optional).
flag.
bus_planning Planapublic-transitroutebetween origin(lat/lon),destination(lat/lon), Transit plan: lines, transfers,
originanddestination. departuretime(optional),preferences walking segments, total duration,
(busorsubway,mintransfers). fare/operatinginfo(ifavailable),step
details.
bicycling_planning Planacyclingroutebetweenorigin origin(lat/lon),destination(lat/lon), Cycling route: distance, ETA,
anddestination. optionalpreferences(bikelanes). polyline/geometry, step-by-step
directions,elevation/road-typehints
(optional).
walking_planning Planawalkingroutebetweenorigin origin(lat/lon),destination(lat/lon). Walking route: distance, ETA,
anddestination. polyline/geometry, step-by-step
directions.
