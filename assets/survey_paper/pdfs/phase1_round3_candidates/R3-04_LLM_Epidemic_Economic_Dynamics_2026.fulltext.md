Title: An LLM-Driven Multi-Agent Simulation Framework for Coupled Epidemic–Economic Dynamics

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_round3_candidates/R3-04_LLM_Epidemic_Economic_Dynamics_2026.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:20:17+00:00
- page_count: 24
- status: ok
- text_char_count: 58166

Metadata:
- author: Shanrui Wang, Huiyong Liu, Shiyi Zhang and Qunsheng Yang
- doi: unknown
- keywords: large language models; agent-based modeling; computational social science; epidemic–economic coupling; multi-agent simulation
- subject: Traditional Agent-based Models (ABMs) often struggle to capture the nuance of adaptive human decision-making during complex crises due to their reliance on static, predefined rules. Large Language Models (LLMs) offer a transformative solution by acting as cognitive engines that empower agents with human-like common-sense reasoning. In this paper, we introduce an LLM-driven Multi-Agent Simulation framework to investigate coupled epidemic–economic dynamics, incorporating a Perception-Deliberation-Action (PDA) loop. Agents, acting as heterogeneous cognitive entities, utilize Chain-of-Thought processes to autonomously balance health risks against economic necessities. This approach endogenously generates adaptive behaviors without explicit scripting. Extensive experiment results across diverse LLM backends confirm the framework's robustness, revealing divergent socio-economic trajectories under distinct macroscopic conditions and effectively quantifying the trade-offs between public health and economic stability. This approach establishes a high-fidelity computational laboratory for investigating complex scenarios under distinct macroscopic conditions, effectively bridging the gap between micro-level cognition and macro-level societal outcomes.

Outline:
- Introduction (page 1)
- Related Work (page 2)
  - ABM in Social Science (page 2)
  - Coupled Epidemic–Economic Models (page 3)
  - LLM-Based Multi-Agent Systems (page 3)
- Materials and Methods (page 3)
  - Simulation Environment (page 4)
  - Agent Design (page 5)
  - LLM-Driven Cognitive Architecture (page 5)
  - Implementation Architecture (page 5)
  - Model Parameter Configuration (page 6)
- Experimental Design (page 7)
  - Stage One: Core Scenario Exploration (page 7)
    - Scenario A: The Baseline (Laissez-Faire) (page 8)
    - Scenario B: Health-Priority Intervention (Lockdown + Stimulus) (page 8)
    - Scenario C: Decentralized Adaptation (Remote Work) (page 8)
  - Stage Two: Model Robustness Validation (page 8)
    - Parameter Scale Setup (page 8)
    - LLM Generalization Setup (page 9)
- Results (page 9)
  - Core Scenario Exploration Results (page 9)
    - Scenario A: Baseline (page 9)
    - Scenario B: Dynamic Health Priority (page 10)
    - Scenario C: Decentralized Adaptation (page 10)
  - Deep Mechanism Analysis (page 11)
  - Model Robustness Validation Results (page 14)
    - Parameter Scale Results (page 14)
    - LLM Generalization Results (page 14)
  - Sensitivity Analysis (page 15)
  - External Validation Against Empirical Epidemic Data (page 16)
- Discussion (page 17)
  - Theoretical Implications (page 17)
  - Practical Implications (page 17)
  - Comparison with Related Work (page 17)
- Conclusions (page 18)
  - Limitations and Future Perspectives (page 18)
    - Limitations of Model Simplification (page 18)
    - Computational Feasibility and Scalability Analysis (page 18)
- LLM Prompt Templates (page 19)
  - Appendix A.1 (page 19)
  - Appendix A.2 (page 20)
  - Sample Output (page 21)
  - Appendix A.4 (page 21)
  - Appendix A.5 (page 22)
- References (page 23)

Markdown Content:

Article
An LLM-Driven Multi-Agent Simulation Framework for
Coupled Epidemic–Economic Dynamics
ShanruiWang ,HuiyongLiu* ,ShiyiZhang andQunshengYang
SchoolofComputerScience,BeijingInformationScienceandTechnologyUniversity,Beijing102206,China;
2023012140@bistu.edu.cn(S.W.);2023012104@bistu.edu.cn(S.Z.);2023012130@bistu.edu.cn(Q.Y.)
* Correspondence:liuhy@bistu.edu.cn
Abstract
TraditionalAgent-basedModels(ABMs)oftenstruggletocapturethenuanceofadaptive
humandecision-makingduringcomplexcrisesduetotheirrelianceonstatic,predefined
rules. LargeLanguageModels(LLMs)offeratransformativesolutionbyactingascog-
nitiveenginesthatempoweragentswithhuman-likecommon-sensereasoning. Inthis
paper, we introduce an LLM-driven Multi-Agent Simulation framework to investigate
coupledepidemic–economicdynamics,incorporatingaPerception-Deliberation-Action
(PDA)loop. Agents,actingasheterogeneouscognitiveentities,utilizeChain-of-Thought
processestoautonomouslybalancehealthrisksagainsteconomicnecessities.Thisapproach
endogenouslygeneratesadaptivebehaviorswithoutexplicitscripting. Extensiveexperi-
mentresultsacrossdiverseLLMbackendsconfirmtheframework’srobustness,revealing
divergentsocio-economictrajectoriesunderdistinctmacroscopicconditionsandeffectively
quantifyingthetrade-offsbetweenpublichealthandeconomicstability. Thisapproach
establishesahigh-fidelitycomputationallaboratoryforinvestigatingcomplexscenarios
underdistinctmacroscopicconditions,effectivelybridgingthegapbetweenmicro-level
cognitionandmacro-levelsocietaloutcomes.
Keywords: largelanguagemodels;agent-basedmodeling;computationalsocialscience;
epidemic–economiccoupling;multi-agentsimulation
1. Introduction
Theoutbreakofinfectiousdiseasesposesadualchallengetomodernsociety: manag-
ingthebiologicalpropagationoftheviruswhilemitigatingthesocio-economicshockwaves
caused by containment measures. Since the foundational work of Kermack and McK-
endrick[1],mathematicalmodelshavebeenthebedrockofepidemiologicalforecasting.
However,ashighlightedduringtheCOVID-19pandemic,theinterplaybetweenpublic
AcademicEditor:KatsuhideFujita healthpoliciesandindividualeconomicbehaviorscreatesacomplexadaptivesystemthat
oftendefiesthepredictionsofaggregateequation-basedmodels[2].
Received:16January2026
Revised:24February2026 Tounderstandthesenon-lineardynamics,computationalsocialsciencehasincreas-
Accepted:26February2026 inglyturnedtoinsilico experiments,withAgent-basedModels(ABMs)emergingasa
Published:5March2026 powerfulparadigmforgrowingmacroscopicsocialphenomenafromthebottomup[3,4].
Copyright:©2026bytheauthors. By modeling heterogeneous agents interacting in a shared environment, ABMs allows
LicenseeMDPI,Basel,Switzerland.
researcherstoexplorehowindividualdecisionsaccumulateintosystemicoutcomes. Yet,
Thisarticleisanopenaccessarticle
traditionalABMsfaceacriticalchallenge: theypredominantlyrelyonpre-defined,static
distributedunderthetermsand
rulestogovernagentbehavior.
conditionsoftheCreativeCommons
Attribution(CCBY)license.
Information2026,17,259 https://doi.org/10.3390/info17030259

Information2026,17,259 2of24
Recently, LLMs have demonstrated impressive capabilities in human-level intelli-
gence[5]. Unlikerule-basedscripts,itcanoffersatransformativesolutiontothisbottleneck
byleveragingtheirvastinternalizedknowledgeandcommon-sensereasoningcapabili-
ties[6]. Buildingupontheseadvances,LargeLanguageModel-basedMulti-AgentSystems
(MASs)havefurtherextendedthepowerofLLMsintomulti-agentinteractionsandsimula-
tion,injectingnewvitalityintothefieldofABMs.Andtherecentstudieshavedemonstrated
thatLLM-basedMASshasachievedgreatsuccessinABMsforvariousapplications[7,8].
However,LLM-basedMASsforepidemiologicalABMsremainunder-explored.
Inthispaper,weproposeanLLM-drivenMulti-AgentSimulationframeworkspecif-
icallydesignedtoinvestigatethecoupledepidemic–economicdynamics. Inoursystem,
eachagentisnotmerelyadatapointbutacognitiveentitythatperceivesitsinfectionstatus
andfinancialpressure,deliberatesontherisksofgoingtoworkversusthesafetyofstaying
home,andmakesautonomousdecisionsthatfeedbackintothemacroscopicsystem. This
approachallowsustobuildahigh-fidelity“ComputationalPolicyLaboratory”,wherethe
impactofNPIs(Non-PharmaceuticalInterventions)canbeevaluatednotjustbyinfection
curves,butbytheemergentbehavioralresponsesofadiversepopulation.
Thecontributionsofthispaperarelistedbelow:
• FrameworkProposal: WeproposeanovelLLM-drivenMulti-AgentSimulationframe-
workforcoupledepidemic–economicdynamics,enablingagentstoexhibithuman-
levelreasoningandadaptivebehaviors,thusovercomingtherigidityoftraditional
rule-basedmodels.
• CognitiveArchitecture: WedesignaPerception-Deliberation-Action(PDA)loopwith
aChain-of-Thought-Action(CoTA)mechanism,effectivelytranslatingcomplexenvi-
ronmentalstatesintonaturallanguagepromptsandmappingLLMreasoningback
intoexecutablesimulationactions.
• High-Fidelity Simulation: We demonstrate the framework’s capability to achieve
high-fidelitysimulationofreal-worldepidemicdynamics,effectivelycapturingthe
complex,non-linearevolutionofviruspropagationdrivenbyadaptivehumanbehav-
iors,offeringavaluablereferenceformanagingpublichealthcrises.
• Robustness&GeneralizationValidation: Throughcomprehensiveexperiments,we
substantiatethesystem’srobustnessacrossdiverseLargeLanguageModelbackends
and population scales, quantifying the divergent socio-economic trajectories that
emergeunderdistinctmacroscopicconditions.
2. RelatedWork
This research intersects three domains: Agent-Based Modeling (ABM), coupled
epidemic–economicdynamics,andLLM-basedMulti-AgentSystems.
2.1. ABMinSocialScience
ABMisacoretoolforsimulatingbottom-upsocialphenomena,enablingtheexplo-
rationofemergentmacro-patternsfrommicro-levelinteractions[3,9]. Thisparadigmhas
beenappliedacrossdomainsfromurbandynamicstofinancialmarkets[4,10]. However,
traditionalABMs,oftengovernedbyrigidheuristics,facechallengesinbehavioralreal-
ismandadaptability,particularlyincrisisscenarios[11]. Recentadvancesaimtobridge
thisgapbycalibratingABMswithlarge-scaleempiricaldatatocreate“digitaltwins”of
societyandbyintegratingformalcausalinferencemethodstoenhancepolicyevaluation
capabilities[12]. Furthermore,asABMsincreasinglyincorporatecomplexAI,newresearch
isexploringtheemergentethicaldilemmaswithinthesesimulatedsocieties[13].
https://doi.org/10.3390/info17030259

Information2026,17,259 3of24
2.2. CoupledEpidemic–EconomicModels
epidemic–economicinteractionsarestudiedviatwomainapproaches. Macro-level
models[14–16]coupleepidemiologicalequationswithrepresentativeagentoptimization,
excelling at policy trade-off analysis but overlooking heterogeneity crucial for targeted
interventions. Micro-level ABMs offer granularity but traditionally rely on static rules.
For instance, while influential models like COVID-ABS [17] successfully capture basic
transmissionmechanics,theiragentsactonrigidheuristics(e.g.,fixedcompliancerates)
thatfailtoreflecttheadaptive,nuanced,andoftenirrationaltrade-offshumansmakewhen
facingthedilemmaof“healthversuslivelihood.”
2.3. LLM-BasedMulti-AgentSystems
Integrating LLMs into MAS enables agents to act as sophisticated “computational
socialentities”[5,18].Pioneeringworks[8]demonstratedLLMagents’capacityformemory
andreflection,whileadvancesincognitivearchitectures[19]enhancetheirreasoning. This
hasspurredanewwaveoflarge-scalesimulations,fromevolvingsocialnetworkstocom-
plexlegalsystems[20].WhileLLMagentshavebeenappliedtoeconomiccompetition[7,11]
anddomain-specificchallengeslikeclimatechange[21]andgeospatialanalysis[22],their
applicationtocoupledepidemic–economiccrisismanagementremainsnascent. Ourwork
addressesthisgap,leveragingLLMstosimulateadaptivedecision-makinginhigh-stakes
policyscenarios.
3. MaterialsandMethods
To investigate the behavior and consequences of LLM-driven agents in a coupled
socio-economic–epidemiological system, we designed and implemented an LLM-MAS
simulationplatform. Thissectiondetailsitscorecomponents: thesimulationenvironment,
agentdesign,andtheLLMinteractionmechanismthatservesastheagent’scognitivecore
(Figure1).
Figure1.SystemArchitectureoftheLLM-DrivenMulti-AgentSimulationFramework.Thediagram
illustratesthecorefeedbackloop:TheDynamicSimulationEnvironmentprovidesperceptualstateto
theMulti-levelAgentPopulation.Agents,governedbytheLLMCognitiveEngineviaaPDAloop,
makedecisionsandexecuteactionsthat,inturn,modifytheenvironment.
https://doi.org/10.3390/info17030259

Information2026,17,259 4of24
3.1. SimulationEnvironment
Oursimulationenvironmentisarectangular2Dgridworld,representinganabstract
city.Theenvironmentcontainsthreetypesofentities:Persons,Businesses,andGovernment.
Individualsmove,work,andconsumeintheenvironment;businessesserveasworkplaces
andprovidersofgoods/services;thegovernmentactsastheformulatorandenforcerof
macropolicies. Timeprogressesindiscrete“iterations”(hours).
The epidemic spread follows the classic SEIR model framework, but adapted for
agent-basedexecutionusingbiologicaltimersratherthanexplicitstatebins.
• ExposureandLatency(E-phase):Uponsuccessfultransmission(probabilityp =0.9
trans
within contact distance d = 1.0), an agent enters the latent phase. While their
contact
internalstatusisflaggedasinfected, theyremainnon-infectiousuntiltheirinfection
timert exceedstheincubationperiod(T =5days).
inf exp
• Infectiousness (I-phase): Agents become contagious only during the window
T < t < (T +T ). Duringthisphase,theycantransmitthevirustoSuscepti-
exp inf exp inf
bleneighbors.
• DiseaseProgression: Clinicalseverity(Asymptomatic→Hospitalization→Critical
→Death)isprobabilisticallydetermineddailybasedonage-stratifiedrisktables,as
detailedinTable1.
• Recovery: Ifanagentsurvivesbeyondtherecoverythreshold(T =20days),they
rec
transitiontotheRecoveredstate,gainingpermanentimmunity.
Thisgranulartemporalmodelingallowsfortheemergenceofrealistictransmission
chains,includingpre-symptomaticspreadandvariableviralsheddingwindows.
Table1.Epidemiologicalparametersstratifiedbyagegroup.Projectionsadaptedfrom[2].
AgeCohort(Years) Hospitalization(%) ICURequirement(%) FatalityRatio(%)
0–9 0.1 5.0 0.002
10–19 0.3 5.0 0.006
20–29 1.2 5.0 0.030
30–39 3.2 5.0 0.080
40–49 4.9 6.3 0.150
50–59 10.2 12.2 0.600
60–69 16.6 27.4 2.200
70–79 24.3 43.2 5.100
80+ 27.3 70.9 9.300
Torigorouslydefinetheinteractiontopology,thesimulationisstructuredasamulti-
layerednetworkconnectingtheState,Businesses,andPopulation:
• Government-StateLayer: TheStateismodeledasacentralizedsingletonentity(Gov-
ernmentAgent)thatfunctionsasthemacro-regulator.Itisfullyconnectedtotheentire
populationnetworkthroughtwoverticalchannels: apolicychannelforbroadcasting
mandates(e.g., Lockdowns)andafiscalchannelforcollectingtaxesanddistribut-
ingstimulus.
• Socio-Economic Layer: The population is embedded in a dual-network structure.
Socially,agentsaregroupedintodistinctHouseholdUnitsrepresentingco-livingnet-
works. Economically,agentsarelinkedtoBusinessEntitiesviaemploymentcontracts,
formingabipartitegraphthatgovernslaborflowsandincomegeneration.
• PhysicalContactLayer: Superimposedonthesestructurallinksisadynamicspatial
network. Diseasetransmissionoccursnotthroughstaticedgesbutthroughphysical
proximitywithinthecontinuous2Dgrid,allowingforemergenttransmissionchains
thatrespectbothsocialclusteringandstochasticencounters.
https://doi.org/10.3390/info17030259

Information2026,17,259 5of24
3.2. AgentDesign
Theplatformdefinesthreedistinctagenttypes: Persons,Businesses,andGovernment,
eachcharacterizedbyspecificstates,objectives,andactionspaces.
PersonAgent. Asthefundamentaldecision-makingunit,eachindividualmaintainsa
dynamic state encompassing health (SEIR status), wealth, and occupation. Their primary
objectiveistobalanceeconomicsurvivalwithhealthpreservation.Theiractionspaceincludes:
Move(selectingdestinations),Work(earningincome),Consume(purchasingessentials),along
withadditionalactionsthatsimulatecommonhumanbehaviorsinreal-worldenvironments.
BusinessAgent. Representingcommercialenterprises,theseagentsmanagewealth
and workforce with the goal of profit maximization. Key actions include Hire or Fire
(adjustingworkforce)andsettingtheOperationalMode(e.g.,remoteworkpolicies).
GovernmentAgent. Actingasthemacro-regulator,thisagentmanagesfiscalreserves
to control the epidemic while maintaining economic stability. Its interventions include
issuingLockdownOrdersanddistributingEconomicStimulustounemployedagents.
3.3. LLM-DrivenCognitiveArchitecture
The core of our framework is a Perception–Deliberation–Action (PDA) cycle that
bridgesmicro-levelcognitionwithmacro-levelsimulation. Toemulatehumans’reasoning
capabilityandmaintainrigoroussimulationlogic,weenforceastrictseparationbetween
globalstateevolutionandindividualdecision-making.
PerceptionandInformationFiltering. Agentactionsaredrivenbyafilteredperception
layerthatconstrainsobservabilityacrossbiologicalandspatialdimensions. Biologically,
observabilityispartial: agentsscantheirimmediatelocalitybutcanonlydetectinfection
basedonvisiblesymptoms;exposedorasymptomaticcarriersappearindistinguishable
from healthy individuals, forcing agents to act under uncertainty. Informationally, we
enforcestricttemporalcausality:agentsbasetheirdecisionsontheglobalstatefrozenatthe
startofthecurrentiteration. Thisdesignisnotmerelyforcomputationalconveniencebutis
criticaltocreatingrealisticconcurrency. Itensuresthatallagentsdeliberatesimultaneously
basedonthesamesnapshotofreality,preventing“look-aheadbias”whereagentsacting
laterintheloopcouldartificiallyreacttothedecisionsofearlieragentswithinthesame
timestep. (DetailedpromptscanbefoundinAppendixA).
ReasoningandExecution. Theseconstrainedobservationsaresynthesizedintody-
namic prompts using a Chain-of-Thought–Action (CoTA) strategy. The LLM explicitly
deliberatesontrade-offs—suchasweighingincomestabilityagainstinfectionrisk—before
generatingastructureddecision. Toensurethatagentinteractionsremainfairandrealistic,
weimplementaConcurrentExecutionMechanism.Insteadofprocessingagentsonebyone,
thesystemworksintwodistinctphases: first,allagentsindependently“think”andsubmit
theirdecisionsbasedonthesamefrozensnapshotoftheworld;onlyaftereveryonehas
decidedaretheseactionsappliedtotheenvironmenttogether. Thispreventsearly-acting
agentsfromalteringtheworldforthoseactinglaterinthesamemoment,strictlypreserving
thesimultaneousnatureofreal-worldbehavior.
3.4. ImplementationArchitecture
TooperationalizethetheoreticalPDAloop,wedevelopedamulti-layeredarchitecture
centeredonaStatusPool.Thiscomponentactsasacentralizedrepositoryforenvironmental
statesandagentmemories,implementingstrictprotocolstoenforcerealisticinformation
asymmetry. Thesimulationproceedsthroughathree-phasepipeline: (1)StateAggregation,
computing global epidemiological and economic indicators; (2) Cognitive Processing,
wherethesystemconstructspromptsbyintegratingenvironmentalcontext,agentprofiles,
anddecisionhistoriespriortodispatchingbatchedLLMqueries;and(3)ActionExecution,
https://doi.org/10.3390/info17030259

Information2026,17,259 6of24
whereanActionRegistryvalidatesandmapsnaturallanguagedecisionstoexecutable
primitives. Toensurebehavioralconcurrency,abufferingmechanismtemporarilyholdsall
decisionsforthecurrentiteration. Thispreventsearlyactorsfromprematurelyalteringthe
environmentstateseenbyothers,therebysimulatingthesimultaneousnatureofreal-world
human decision-making. Additionally, periodic economic activities (e.g., payrolls) are
triggeredbyfixedtimers,operatingindependentlyofthecognitivelooptoauthentically
simulateuniversallyacceptedreal-worldeconomiccycles.
Figure2providesacomprehensivevisualoverviewofthisexecutionpipeline.Itdelin-
eatesthesequentialflowfromsysteminitialization,throughthecycliciterationofthemain
simulationloop(encompassingenvironmentalevolution,theLLM-drivenPDAcycle,and
actionsynchronization),tothefinaldataanalysisphase.Thisstructuralmappingensuresthat
thetheoreticalcognitivemodelisrigorouslytranslatedintoexecutableprocedurallogic.
Figure2. OperationalWorkflowoftheSimulationPlatform. TheflowchartdetailstheThree-Phase
Pipeline:(1)Initializationestablishesthedemographicandeconomicbaseline;(2)MainLooporchestrates
theconcurrentPDAcycle,whereenvironmentalevolutionandagentdeliberationoccurinsynchronized
steps;(3)OutputandAnalysislogsmulti-dimensionaldataforposthocvisualization.
3.5. ModelParameterConfiguration
Toensurereproducibilityandreal-worldalignment,thissectiondetailsthekeypa-
rameters. We referenced and expanded upon the parameter settings from the baseline
paper[17],leveragingpubliclyavailabledatafromhighlycrediblethird-partyorganiza-
tionsasthefundamentalconfigurationparameters, whileincorporatingempiricaldata
to ensure high realism. Specifically, the synthetic population (N = 50) is generated to
mirrorreal-worlddemographicstructures. AgeassignmentsfollowaBetadistribution
(α = 2,β = 4) scaled to [0,100] to reflect a realistic age pyramid [23], while household
compositionandvulnerabilitylayersareinitializedbasedonofficialcensusandhomeless
populationreports[24,25]. Furthermore, initialwealthisallocatedaccordingtoLorenz
curveprinciples(Table2),ensuringarepresentativewealthinequalitydistribution(Table3).
https://doi.org/10.3390/info17030259

Information2026,17,259 7of24
Table2.IncomestratificationbasedonWorldBankquintiledata(γ )[26].
dist
IncomeQuintile ClassDesignation WealthShare(%) Cumulative(%)
Q1 LowestIncome 3.62 3.62
Q2 LowIncome 7.88 11.50
Q3 MiddleIncome 12.62 24.17
Q4 HighIncome 19.71 43.88
Q5 HighestIncome 56.12 100.00
Table3.Simulationconfiguration:EconomicstructureandAgentdynamics.
Symbol Parameter Value Description Source
Business&AgentDynamics
N BusinessCount 5 Totalenterprises [27]
biz
∆t AgentTimeStep 2/24/72h Decisioncycles EmpiricallyDefined
p/b/g
EconomicStructure
γ IncomeDistribution Table2 Incomestrata [26]
dist
γ BusinessDensity 0.01875 Firmspercapita [28]
dens
Y InitialSystemGDP 1.8M Totalsystemwealth EmpiricallyDefined
init
u InitialUnemployment 0.12 Initialrate [29]
init
4. ExperimentalDesign
Torigorouslyassessthevalidityandheuristicpoweroftheproposedframework,we
structuredtheexperimentalevaluationintotwodistinctphases: (1)CoreScenarioExplo-
ration,whichfunctionsasa“computationalpolicylaboratory”toinvestigateemergent
socio-economicdynamicsunderdistinctmacroscopicconditions;and(2)ModelRobust-
nessValidation,whichscrutinizestheinternalconsistencyoftheLLM-drivencognitive
architectureacrossdifferentparameterscalesandbackendmodels.
4.1. StageOne: CoreScenarioExploration
Wedesignedthreerepresentativescenariostoexplorethenon-linearcouplingbetween
epidemiccontrolandeconomicsustainability. Toensurestatisticalreliabilityandmitigate
theimpactofstochasticity,eachscenariowasrepeatedfivetimesusingtheDeepSeek-V3
model in the standard experimental environment (N = 50, see Table 4). Crucially, to
eliminatebiasfromspecificinitializationartifacts,thepopulationisresampledforeach
run using independent random seeds. This ensures that the aggregated results reflect
robustsystemicdynamicsvalidacrossdiversedemographicconfigurations,ratherthan
accumulatingfromasinglefixedpopulationstructure.
Table4.Simulationconfiguration:EnvironmentalandEpidemiologicalparameters(N=50).
Symbol Parameter Value Description Source
SocialandDemographic
H ,W GridDimensions 207×207 Mapdimensions EmpiricallyDefined
grid grid
N TotalPopulation 50 Totalagentcount EmpiricallyDefined
pop
D AgeDistribution β(2,4) Agestructure [23]
age
S MeanFamilySize 3(Std: 1) Meanhouseholdsize [24]
family
ρ HomelessnessRatio 0.0005 Homelessratio [25]
home
https://doi.org/10.3390/info17030259

Information2026,17,259 8of24
Table4.Cont.
Symbol Parameter Value Description Source
Epidemiological
d ContactDistance 1.0 Safedistance [2]
contact
p TransmissionProb. 0.9 Transmissionrate [2]
trans
T LatencyPeriod 5 Incubationdays [30,31]
exp
T InfectiousnessPeriod 10 Infectiousdays [32]
inf
T RecoveryPeriod 20 Recoverydays [33]
rec
4.1.1. ScenarioA:TheBaseline(Laissez-Faire)
Thiscontrolscenariosimulatesthesystem’snaturalevolutionwithoutcentralizedin-
tervention. TheGovernmentagentispassive,issuingnoNPIsorfiscalstimulus,simulating
agovernmentthatimposesnorestrictionsduringthepandemic,allowingagentstoact
freelyastheywouldduringnon-pandemicperiods. Individualagentsrelyentirelyontheir
autonomousrisk-rewardassessmentstonavigatethecrisis. Theobjectiveistoestablishthe
baselinetrajectoryoftheepidemic–economicsystem,isolatingtheendogenousinteraction
dynamicsbetweenviralspreadandspontaneousagentbehavior.
4.1.2. ScenarioB:Health-PriorityIntervention(Lockdown+Stimulus)
Thisscenariosimulatesanaggressive,health-centricgovernmentstrategyimplement-
ingthefollowingapproachestomodelagovernmentthatprioritizescitizens’livesasits
primaryprotectiongoal: (1)Dynamiccircuitbreakermechanism,triggeringmandatory
stay-at-home orders when infection rates exceed 5% and lifting them when transmis-
sionfallstosafelevels;(2)Targetedeconomicrelief,withthegovernmentautomatically
distributingfiscalstimulustounemployedagents;(3)Reinforcedgovernmentinterven-
tion, emphasizing in the prompts to government agents their governing style—willing
toprotectpublichealthatallcosts,regardlessofeconomicconsequences. Ourobjective
istoassessthetrade-offsofsuppressionstrategies,specificallyquantifyingtheextentto
whichstrictcontainmentflattenstheinfectioncurveandwhetherparallelfiscalaidbuffers
economicvolatility.
4.1.3. ScenarioC:DecentralizedAdaptation(RemoteWork)
This scenario differs from top-down mandates by introducing labor market flexibil-
ity. TheWorkFromHomeAction(WFH)mechanismisactivated, allowingagentstoau-
tonomouslyswitchtoremoteworkbasedonriskperception. Wemodelamoderndigital
economywhereremoteworkisfullyefficient,enablingagentstomaintainfullincomewithout
physicalpresence.Weinvestigatewhetherdecentralizedautonomousadaptationcanserveas
aviablesoftcontainmentstrategy,balancingpublichealthandeconomiccontinuity.
4.2. StageTwo: ModelRobustnessValidation
ThisstageaddressesafundamentalepistemologicalquestioninLLM-basedsimulation:
To what extent are the observed macroscopic phenomena attributable to the system’s
structuraldesignratherthanstochasticartifacts,parameterscale,ormodel-specificbiases?
4.2.1. ParameterScaleSetup
WeconductedcomparativeexperimentsusingtheDeepSeek-V3modelatalargerscale
(N =500)toverifyifthemacroscopictrendsobservedinthestandardenvironment(N =50)
holdtrue.TheN =500experimentswererepeatedtwiceduetohighercomputationalcosts.
Table5summarizesthescalinglogic.
https://doi.org/10.3390/info17030259

Information2026,17,259 9of24
Table5.Parameterconfigurationfortherobustnessexperiments.
Parameter MainExp. ScaleExp. Rationale
Population(N ) 50 500 10×scalefactor
pop
Grid(H×W) 207×207 655×655 Constantdensity
Businesses(N ) 5 15 1vs. 3perstratum
biz
GDP(Y ) 1.8M 18M Proportional(36k/capita)
init
4.2.2. LLMGeneralizationSetup
Wedeployedfourdistinctcommercialandopen-sourceLLMs(DeepSeek-V3,GPT-4o-
mini,Qwen2.5,Gemini2.0-flash)todrivetheagentpopulationinthestandardenvironment
(N =50). ThesimulationparametersmirroredtheBaselineScenario(ScenarioA),allowing
foradirectcomparisonoftime-seriesoutputsacrosskeymacroscopicindicators.
5. Results
Thissectionpresentstheresultsofourcomputationalexperiments. Wefirstdetailthe
socio-economicdynamicsrevealedbythecorescenarios,thenprovideamicroscopicanalysis
ofagentbehaviorstodemonstratehighfidelity,andfinallyconfirmthesystem’srobustness.
5.1. CoreScenarioExplorationResults
Wesimulatedthethreecorescenarios,andthecomparisonoftheirmacroscopicresults
revealsprofounddifferencesunderdistinctmacroscopicconditions. Figure3providesan
overallcomparisonofkeymetrics,whileFigures4–6presentdetaileddynamics.
Figure 3. Macroscopic Dynamics Comparison across Core Scenarios. This figure contrasts the
infectioncurvesandeconomicindicators(suchasunemploymentandGDPloss)acrossthedistinct
macroscopicconditions,highlightingthetrade-offsbetweenhealthandeconomy.
5.1.1. ScenarioA:Baseline
Theresultsofthebaselinescenario(Figure4)revealthenaturalevolutionarytrajectory
ofthesystemwithoutexternalintervention. Epidemiologically,thesystemexperienced
dramaticexponentialgrowth,withtheinfectedpopulationpeakingaroundday24and
leadingtorapiddepletionofsusceptibleindividuals. Deathscontinuedtorise,stabilizing
atapproximately12%ofthepopulation. Economically,whilewealthinteractionremained
https://doi.org/10.3390/info17030259

Information2026,17,259 10of24
stable initially, the rapid epidemic spread caused a healthcare system collapse and ex-
cessive medical expenses. These results demonstrate that a laissez-faire strategy in the
faceofahighlycontagiousepidemicinevitablyleadstoadualcrisisinpublichealthand
theeconomy.
Figure4. DetailedDynamicsofScenarioA(Baseline). Thepanelsshowthetimeevolutionofthe
epidemic(SEIRstates)andeconomicstatus(wealth,unemployment)underalaissez-fairepolicy.
5.1.2. ScenarioB:DynamicHealthPriority
InScenarioB(Figure5), thedynamiclockdownstrategysuccessfullyflattenedthe
curve,delayingtheinfectionpeakandreducingtotalfatalities. However,thissuccesscame
atasteepeconomicprice. Thestop-and-gonatureoflockdownscausedseverefluctuations
inbusinessoperations,leadingtocyclicalspikesinunemployment. Thisillustratesthe
classictrade-off: strictcontainmentpreserveslifebutinducesdeep,intermittenteconomic
recessionsdisproportionatelyaffectinglower-incomeagents.
Figure5. DetailedDynamicsofScenarioB(HealthPriority). Thepanelsillustratetheimpactof
dynamic lockdown policies, showing “flattened” infection curves but significant fluctuations in
economicactivity.
5.1.3. ScenarioC:DecentralizedAdaptation
ScenarioC(Figure6)demonstratestheSoftLandingeffectofthedecentralizedWFH
mechanism. Asinfectionratesrose,agentsspontaneouslyshiftedtoremotework,reducing
contactdensitywithoutgovernmentcoercion. Thisautonomousadaptationsignificantly
loweredthepeakinfectionrate. Economically,asthesimulationmodelsadigitaleconomy
whereremoteproductivityisfullypreserved,thesystemavoidedthedeeprecessionseenin
ScenarioB.Thissuggeststhatempoweringindividualflexibilitycanbeasuperiorstrategy
torigidtop-downmandates.
https://doi.org/10.3390/info17030259

Information2026,17,259 11of24
Figure6. DetailedDynamicsofScenarioC(RemoteWork). Thepanelsshowtheoutcomesofthe
WFHmechanism,highlightinga“SoftLanding”effectonbothhealthandeconomy.
5.2. DeepMechanismAnalysis
Beyondverifyingbasicrationality,ourdeepanalysisofthesimulationlogsreveals
complexcausalchainsthatdrivethedivergentoutcomes. Tosystematicallyexplainthese
emergent phenomena, we constructed a Causal Loop Diagram (Figure 7) based on the
agentinteractiontraces.
Figure7. CausalInfluenceDiagramofPandemicEconomics. Thisfiguremapsthedistinctlogic
chainsforeachscenario,derivedfromthesimulation’sexecutiontraces.Itillustrateshowmicro-level
behaviors(e.g.,WFH,Lockdown)propagatethroughtheeconomicnetworktoproducemacro-level
outcomes(e.g.,Deficit,Recovery).Arrowsindicatecausaldirection.
IntheBaselinescenario,theeconomiccollapseisdrivenbyapassivedrainmechanism.
The exponential infection rate leads to a surge in medical expenses. The model design
specifiesthatmedicalcostsareshared: 50%ispaidbytheindividual(depletinghousehold
savings)andtheremainderissubsidizedbythegovernment(viathehealthcaresystem).
This creates a Cost-Push Deficit where the government, despite having no active fiscal
policy,isdrainedbythemassivehealthcarebill,leadingtothedualbankruptcyofboth
householdsandthestate.
ScenarioBrevealsthehiddeneconomiccostsofstrictcontainment. Whilethelock-
downeffectivelycurbedtransmissionbyrestrictingmobility,itinducedadualstagnation
inbothconsumptionandproduction. Onthedemandside,confinedindividualsdrasti-
https://doi.org/10.3390/info17030259

Information2026,17,259 12of24
callyreducedshopping,causingbusinessrevenuestodeclinesignificantly. Onthesupply
side,businessescontinuedtoincurfixedoperationalcostsdespiteworkforceabsence. To
balancetheirbooks,firmswereforcedtoexecutemasslayoffs,leadingtoasharpspikein
unemployment(asshowninFigure8).
Figure 8. ComparisonofUnemploymentMetricsacrossScenarios. Theradarcharthighlightsthe
structuraldamagetothelabormarketinScenarioBcomparedtotheresilienceobservedinScenarioC.
However,thiseconomicresiliencecomesatanepidemiologicalcost. Figure9presents
the total cumulative case counts across the three scenarios. While Scenario C avoids
economiccollapse,itresultsinahigheraveragetotalinfectioncount(47.0±1.67)compared
toScenariosA(39.8±17.9)andB(33.2±18.6). TheremarkablylowvarianceinScenario
C reflects the “Soft Landing” mechanism, where decentralized adaptation flattens the
curvebutprolongstheepidemicduration,leadingtoastable,deterministicprogression.
In contrast, Scenarios A and B exhibit high volatility due to their reliance on extreme
strategies—eithercompletelaissez-faireorrigidblocking. ParticularlyinScenarioB,the
outcomeishypersensitivetointerventiontiming; slightvariationsinthegovernment’s
decisionwindowcanleadtovastlydifferenttrajectories,causingthesystemtobifurcate
betweensuccessfulsuppressionandfull-scaleoutbreak.
ScenarioCpresentsacomplextrade-offbetweenepidemicdurationandeconomic
resilience. The remote work mechanism functioned as a “soft isolation,” successfully
lowering the infection peak but significantly extending the epidemic’s tail. Unlike the
other scenarios which concluded within a month, Scenario C persisted into the second
month. However,thecriticaladvantageofthisstrategyliesinitspreservationofthelabor
market: bymaintainingcoreproductivitythroughremotework,businessesavoidedthe
masslayoffsseeninScenarioB.
Fine-GrainedAnalysisofMacro-EconomicMechanisms. Adetaileddecomposition
oftheexperimentalresultsrevealsthatScenarioB(Health-PriorityIntervention),despite
imposingstrictlimitationsoneconomicactivity,preservesthehighestlevelofGovernment
Wealthamongtheexploredscenarios. Thisphenomenonstemsfromthedistinctinteraction
patternsbetweenepidemiologicalloadsandfiscaltriggermechanismsineachsetting.
https://doi.org/10.3390/info17030259

Information2026,17,259 13of24
Figure9.ComparisonofTotalCumulativeCasesacrossScenarios.Thebarchartdisplaysthefinal
infectedpopulationcount(Mean±Std).ScenarioCshowshighertotalinfectionsbutwithminimal
variance,reflectingaconsistent“flattening”strategythatprolongstheoutbreak,whereasAandB
showhighoutcomeuncertainty.
IntheBaselineScenario(A),theunmitigatedtransmissionofthevirusgeneratesa
substantial medical financial burden. Under the model’s mechanism where healthcare
costsaresharedbetweenindividualsandthegovernment,thehighinfectionratetranslates
intoanaccumulationofmedicalliabilities. Attheendofthemonthlybillingcycle, the
government is required to settle these extensive costs, resulting in a direct and severe
reductioninfiscalreserves.
InScenarioC(DecentralizedAdaptation),althoughremoteworkstrategiesmaintain
infectionratesclosertoScenarioBlevels,adiscordanceemergesbetweencontinuedpayroll
obligations and reduced consumption. Analysis of the agent decision logs (specifically
theconsumptionfrequencyaudit)indicatesthatwhileagentssecureincomeviatelework,
theirrisk-aversebehaviorleadstoamarkeddeclineinphysicalshoppingactivities. Conse-
quently,businessrevenuesfallsignificantlybelowthewageobligationsrequiredtobepaid
atmonth-end. Toensurethesurvivalofeconomicentities,thegovernmentistriggeredto
providefinancialaidtocoverthesewagedeficits,therebytransferringtheprivatesector’s
operatinglossestothepublicfiscalbalance.
Furthermore,thesharpeconomicvolatilityobservednearDay30acrossallscenarios
is driven by the system’s synchronized financial cycle. At the end of each month, a
compoundsettlementeventoccurswherebusinessesdisbursewages,householdsandfirms
paytaxes,andthegovernmentclearsaccumulatedmedicalsubsidieswhiledistributing
unemploymentstimulus. Thissimultaneousliquidityclearingcreatesadistinct“pulse”
inthewealthtrajectories(visibleinFigure4),physicallymodelingtheperiodicnatureof
real-worldmacroeconomicflows.
Incontrast,ScenarioBeffectivelyminimizesbothexpenditurevectors. Epidemiologi-
cally,thedynamiccircuitbreakerkeepsinfectionratessignificantlybelowthoseofScenario
A.Critically,giventhesubstantialdisparityinfinancialimplicationsacrossdifferentincome
strata(referencingTable2),evenmoderatereductionsininfectionprevalencepreventthe
disproportionateaccumulationofmedicalcostsassociatedwithwidespreadtransmission,
therebysignificantlyamplifyingthefiscaladvantagesoflowinfectionrates. Economically,
themandatorybusinessclosuresinScenarioBsuspendnotonlyrevenuegenerationbut
https://doi.org/10.3390/info17030259

Information2026,17,259 14of24
alsotheimmediatepressureofwagepaymentobligations. UnlikeScenarioC,wherethe
governmentmustintervenetobridgetherevenue-wagegap,thesuspendedeconomicstate
ofScenarioBalleviatestheneedforemergencyfiscalstimulus. Thus,bysimultaneously
mitigatingthemedicalexpenditureshockobservedinScenarioAandavoidingthesub-
sidyburdensactivatedinScenarioC,ScenarioBdemonstratessuperiorperformancein
preservinggovernmentfiscalsolvency.
5.3. ModelRobustnessValidationResults
5.3.1. ParameterScaleResults
WecomparedthemacroscopicinfectionandeconomiccurvesbetweentheN =50and
N =500experiments(bothusingDeepSeek-V3).Theresultsindicatethatwhiletheabsolute
valuesscaleproportionally,thekeystructuralfeatures—suchasthetimingoftheinfection
peak (Day 24 vs. Day 26), the final infection rate (≈98%), and the shape of the recession
curve—remainhighlyconsistent. Thisconfirmsthatourfindingsarerobusttopopulation
scaleandthattheN =50experimentalsetupisavalidproxyforlarger-scaledynamics.
5.3.2. LLMGeneralizationResults
Theexperimentalresults(Figure10)clearlyindicatethatsimulationsdrivenbythefour
modelsconvergetohighlysimilarsocialdynamicsatthemacroscopiclevel. Specifically,
thepeakoftheinfectioncurveisreachedaroundday25forall, andthefinalmortality
rateandmagnitudeofeconomicrecessionarealsoofthesameorder. Thiscross-model
consistencystronglydemonstratesthatthesocio-economic–epidemiologicalinteraction
patternsrevealedbyoursimulationframeworkareauniversalfeatureoftheLLM-driven,
common-sense-basedagentarchitecture,ratherthananartifactofanyspecificLLM.
Figure10.LLMGeneralizationComparison.Thefiguredemonstratestherobustnessofourframe-
workacrossfourdifferentLLMbackends(DeepSeek-V3,GPT-4o-mini,Qwen2.5,Gemini2.0-flash).
Despitedifferencesinunderlyingarchitectures,themacroscopicsocio-economicdynamics—including
infectionpeaksandeconomicrecessiontrends—remainqualitativelyconsistent.
https://doi.org/10.3390/info17030259

Information2026,17,259 15of24
5.4. SensitivityAnalysis
Tovalidatethemodel’sresponsivenesstocriticalparametersandensureitsreliability
as a policy laboratory, we performed sensitivity analyses on both epidemiological and
economicdimensions.Intheseanalyses,thebaselinemetricsarederivedfromtheaveraged
experimentalresultsofScenarioA.
Impact of Transmission Probability. Figure 11 illustrates the system’s response to
varyingviraltransmissionprobabilities(p ),withthep =0.9curverepresentingthe
trans trans
baselinedatafromScenarioA.Theresultsdemonstrateaclearandsignificantsensitivity:
as p decreasesto0.6and0.3,thecumulativemortalityratedropsdisproportionately,
trans
andthecurve’sgrowthtrajectoryflattensmarkedly. Thisnon-linearresponseconfirmsthat
themodelcorrectlycapturesthemechanicalsensitivityofinfectiondynamicstochangesin
contactparameters.
Figure 11. Sensitivity of Epidemic Mortality to Transmission Probability (ptrans). The solid red
linerepresentsthebaselinedatafromScenarioA(ptrans = 0.9). Thedashedlinessimulatelower
transmission scenarios (p = 0.6,0.3), showing a non-linear reduction in cumulative deaths and
flattenedgrowthcurves,demonstratingthemodel’sepidemiologicalresponsiveness.
Impact of Medical Costs on Household Wealth. We further examined the model’s
sensitivitytoeconomicvariablesbyvaryingthedailymedicalexpenseparameter.Figure12
compares the wealth trajectories under Low, Medium (Scenario A baseline), and High
cost conditions. The model exhibits distinct behavioral responses to these parameter
shifts: duringtheoutbreakphase(Days0–30),theHighCostscenariotriggersadrastic
depletion of household wealth compared to the baseline, while the Low Cost scenario
demonstratessignificanteconomicpreservation. Thissharp,phase-dependentdivergence
highlightsthemodel’scapabilitytosensitivelyreflecthoweconomicshockparameters
interactwithepidemiologicalstates, confirmingitsefficacyinquantifyingthegranular
impactofeconomicvariableswithincoupleddynamics.
https://doi.org/10.3390/info17030259

Information2026,17,259 16of24
Figure12.SensitivityofPersonalWealthtoMedicalExpenses.TheGreenlinerepresentsthebaseline
wealthtrajectoryfromScenarioA(MediumCost).ThesignificantdeviationoftheRed(HighCost)
andBlue(LowCost)linesduringMonth1illustratesthedistincteconomicshockscausedbyvarying
medicalcostsduringtheinfectionpeak,followedbyparallelrecoverytrends.
5.5. ExternalValidationAgainstEmpiricalEpidemicData
TovalidatethemacroscopicemergentbehaviorsofourLLM-basedmulti-agentsimu-
lationandenhancethepersuasivenessofourresults,weconductedanexternalvalidation
bycomparingourbaselinetemporaltrajectorieswithreal-worldepidemiologicaldatafrom
theearlystagesoftheCOVID-19outbreak. Accordingtothecomprehensiveepidemio-
logicalcharacteristicsreportof72,314casespublishedbytheChineseCenterforDisease
Control and Prevention (China CDC) [34], the real-world epidemic curve exhibited an
initialexponentialgrowthphasearound12January2020,whichsubsequentlyreachedits
firstmajorincidencepeakon24January2020. Thisrepresentsanaturalevolutionperiodof
approximately12daysfromtheearlyoutbreakstagetothefirstepidemicpeak.
Itiscrucialtonotethattheinfectionstatuson12Januaryintheempiricaldataclosely
mirrorstheinitialstateofoursimulation. Remarkably,thetemporaldynamicsgenerated
by our simulation align closely with these empirical observations. In our unmitigated
baseline scenario (Scenario A), starting from this comparable initial infection state, the
simulationdemonstratedthattheinfectionratepeakedatTick284. Giventhateachtick
inourmodelrepresentsonehourofsimulatedtime,thistranslatestoexactly11.83days.
Thenear-perfectalignmentbetweenthesimulatedtime-to-peak(11.83days)andthereal-
worldtime-to-peak(12days)fromsimilarstartingconditionsprovidesstrongevidencethat
ourLLM-drivenagents,despiteoperatingonindividualbehavioralprompts,collectively
generatemacroscopicepidemiologicaltrajectoriesthatarehighlyconsistentwithreal-world
infectiousdiseasedynamics. AsillustratedinFigure13,thesimulatedinfectionratiocurve
closelytrackstheexponentialgrowthandpeaktimingoftheempiricaldailynewcases,
visuallyconfirmingthetemporalvalidityofourmodel.
https://doi.org/10.3390/info17030259

Information2026,17,259 17of24
Figure13.ComparisonofEpidemicTrajectories:EmpiricalDatavs.Simulation.Theblueline(leftaxis)
representstheempiricaldailynewcasesfromtheChinaCDCreport,startingfrom12January(Day0).
Thereddashedline(rightaxis)representsthesimulatedinfectionratiofromourbaselineScenarioA.
Bothcurvesexhibitahighlysynchronizedexponentialgrowthphase,reachingtheirrespectivepeaksat
approximatelyDay12(24Januaryintheempiricaltimeline),demonstratingthemodel’stemporalvalidity.
6. Discussion
Thecorecontributionofthisstudyistheproposalandvalidationofamulti-agentsim-
ulationframeworkdrivenbyLLMsforexploringcomplexsocio-economic–epidemiological
systems. In this section, we delve into the theoretical and practical implications of the
experimentalresults,compareourworkwithexistingresearch,andcandidlydiscussits
limitationsandfuturedirections.
6.1. TheoreticalImplications
OurexperimentsdemonstratethatLLMscaneffectivelyserveasthe“cognitiveengine”
forcomputationalsocialagents. ThehighfidelityobservedintheMicro-BehavioralAnaly-
sissuggeststhatLLMssuccessfullyinternalizehuman-likeriskassessmentanddecision-
makinglogic. Thisoffersatheoreticalbridgebetweenmicro-levelcognitivepsychology
andmacro-levelsocialdynamics,supportingthegenerativesocialscienceparadigm.
6.2. PracticalImplications
TheCoreScenarioExplorationvividlydemonstratesthewickednatureofpolicymak-
ing. Our“ComputationalPolicyLaboratory”revealsthattherearenoperfectsolutions,
onlytrade-offs. Thehealth-prioritystrategysaveslivesbutinflictseconomicpain,while
thedecentralizedadaptationstrategyoffersapromisingmiddlepath. Crucially,ourdeep
mechanismanalysisuncoveredhiddenliabilities—suchasthegovernment’sroleasthe
payeroflastresort—thatareofteninvisibleinstandardaggregatemodels. Thesefindings
providepolicymakerswithaquantifiablereferenceforanticipatingthecomplex,non-linear
consequencesoftheirinterventionsbeforeimplementation.
6.3. ComparisonwithRelatedWork
Ourframeworkoffersdistinctadvantagesoverexistingparadigms. UnlikeEquation-
Based Models that rely on homogeneous mixing assumptions, our approach connects
macro-phenomena to micro-behavioral foundations. Compared to Rule-Based ABMs,
itenablestheendogenousemergenceofheterogeneousbehaviorswithoutpre-scripted
https://doi.org/10.3390/info17030259

Information2026,17,259 18of24
rules. Furthermore, while recent LLM-based simulations often focus on general social
interactions[8],ourworkrigorouslytargetsthehigh-stakesdomainofepidemic–economic
coupling,providingaspecializedtestbedforpolicyevaluation.
7. Conclusions
This paper introduces a novel LLM-driven multi-agent simulation framework for
coupledepidemic–economicdynamics. Ourexperimentsdemonstratethatthisapproach
cangeneratehigh-fidelity,emergentsocialbehaviorsandprovideapowerfulcomputational
laboratoryforpolicyanalysis. Byreplacingrigidheuristicswiththenuancedreasoning
of LLMs, we offer a new paradigm for building more realistic and adaptive models in
computationalsocialscience,bridgingthegapbetweenmicro-levelcognitionandmacro-
levelsocietaloutcomes.
7.1. LimitationsandFuturePerspectives
7.1.1. LimitationsofModelSimplification
The current model simplifies real-world complexities such as detailed contact net-
worksandsupplychains;incorporatingricherempiricalstructureswouldimproverealism.
Intermsofepidemiologicalfidelity,whiletheSEIRframeworkcapturesfundamentaltrans-
missiondynamics,itcurrentlyabstractsawaycomplexpharmaceuticalinterventions. The
systemdoesnotyetaccountforvaccinatedcompartments,immunewaning,orvariant-
specific reinfection pathways, limiting its applicability to long-term endemic scenarios.
Furthermore,theeconomicmoduleapproximateshealthcareimpactsthroughaggregate
government subsidies, simplifying the granular financial shocks of hospitalization on
diversehouseholdstrata.
7.1.2. ComputationalFeasibilityandScalabilityAnalysis
Regarding the computational and financial costs of large-scale simulations, we ac-
knowledge that using LLM inference for every agent at every time step constitutes a
significantresourcebottleneck. Inourexperimentalconfiguration(usingtheDeepSeek-V3
model), the average inference time for a single agent’s decision step is approximately
1.2s. Forasimulationscaleof N = 50,theparallelprocessingmechanismimplemented
viaThreadPoolExecutorkeepsthetotalcomputationaltimeperupdatecycle(simulation
hour) within 10 s. However, costs grow linearly with scale, posing a barrier to direct
expansiontocity-levelpopulations(N >10,000).
Tomitigatethisissue,wehaveadoptedthefollowingoptimizationstrategiesinour
engineeringimplementationandfutureplanning:
Parallel Execution and Context Storage Optimization: Our system employs a
ThreadPoolExecutor-based concurrent inference architecture to mask network latency.
Simultaneously,weimplementcontextstorageoptimizationduringtheecosystemPrompt
constructionphasetostrictlycontrolTokenconsumption,preventingcostsfromgrowing
exponentiallywithenvironmentalcomplexity.
ModelCompatibilityandCostOptimization: TheLLMgeneralizationanalysisinthis
paper(seeSection4.2.2)confirmsthatourmulti-agentframeworkexhibitshighlyconsistent
macroscopicsocio-economicdynamicsacrossdifferentLLMbackends(includingDeepSeek-
V3,GPT-4o-mini,Qwen2.5,andGemini2.0-flash). Thisfindingindicatestheframework’s
robustnessregardingthechoiceof“cognitiveengine.” Theexperimentalresultsestablisha
clearpathforlow-costscaling: researcherscansafelyswitchtolightweightmodelswith
fewerparametersandlowerinferencecosts(suchasGPT-4o-minioropen-sourcemodels)
to significantly reduce the computational and financial costs of large-scale simulations
withoutsacrificingthevalidityandfidelityoftheresults.
https://doi.org/10.3390/info17030259

Information2026,17,259 19of24
Future work will focus on enriching the model with finer-grained empirical data,
supportedbytheaforementionedcomputationaloptimizationtechniquestoenablelarger-
scalesimulations. Specifically,wewillpursuethreekeydirections: (1)Epidemiological
Extension, incorporating vaccination, immune decay, and detailed hospitalization cost
models;(2)CognitiveEnhancement,enrichingagentswithlong-termmemoryandcommu-
nicationprotocolstosimulatecollectivebehaviorslikerumorpropagation;and(3)Scale
andEfficiency,leveraginglow-costlightweightmodelstoscalesimulationstocity-level
populationswhileexploringmodeldistillationtechniques.
AuthorContributions:Conceptualization,S.W.andH.L.;methodology,S.W.;software,S.W.andQ.Y.;
validation,S.W.,S.Z.andQ.Y.;formalanalysis,S.W.;investigation,S.Z.;resources,H.L.;datacuration,
S.W.;writing—originaldraftpreparation,S.W.;writing—reviewandediting,H.L.;visualization,S.W.;
supervision,H.L.;projectadministration,H.L.Allauthorshavereadandagreedtothepublished
versionofthemanuscript.
Funding:Thisresearchreceivednoexternalfunding.
InstitutionalReviewBoardStatement:Notapplicable.
InformedConsentStatement:Notapplicable.
DataAvailabilityStatement:Theoriginalcontributionspresentedinthisstudyareincludedinthe
article.Furtherinquiriescanbedirectedtothecorrespondingauthor.
ConflictsofInterest:Theauthorsdeclarenoconflictsofinterest.
AppendixA.LLMPromptTemplates
Toensurereproducibility,thisappendixprovidesthecompleteprompttemplatessent
totheLargeLanguageModels(LLMs). Oursystemusesadynamicpromptconstruction
mechanismthatgeneratespromptsbasedontheagent’simmediatestate(PerceptionLayer)
andstaticattributes(RoleLayer).
ComputationalEnvironment: ThisframeworkwasimplementedinPython(version3.12,
https://www.python.org/). Thefollowingboxespresentthecoreprompttemplatesused
toguidetheLLMagents’behaviorduringthesimulation.
AppendixA.1. SystemPrompt
Thesystempromptsetsthebasicroleandsimulationconstraintsfortheagent.
SystemPrompt
YouaresimulatingapersonduringaCOVID-19epidemic. Yourdecisionsshouldbalance
personalsafety,economicsurvival,andsocialresponsibility. Berationalandconsiderboth
short-termandlong-termconsequences. AlwaysrespondinvalidJSONformat.
You are a 45 year old middle-aged adult. You have moderate risk from COVID-19 and
responsibilities to family/work. Your social class is low-income. Your limited financial
resourcesmeanyoumustbalancesafetywitheconomicsurvival. Missingworkcouldbe
devastating.
https://doi.org/10.3390/info17030259

Information2026,17,259 20of24
AppendixA.2. UserContextPrompt
Theuserpromptprovidescurrentobservationstate,environmentalinformation,and
availableactionspace.
UserPrompt
CurrentState(Day5,Hour8):
• Health: Susceptible
• Position: (12.5,8.4)
• Age: 45yearsold
• Wealth: $450.00
• SocialClass: Low-income
EpidemicNews(LastUpdated: Day5):
• RiskLevel: High
• ReportedInfectionRate: ∼2.5%
• ReportedDeathRate: ∼0.1%
• GovernmentAdvice: Wearmasksandavoidcrowds
NearbyPeople:
• Adultpersonat2.1m—LOOKSSICK(coughing)
• Elderlypersonat4.5m—appearshealthy
Shopping&EconomicResponsibility:
• Nearestbusiness: 120maway(OPEN,$15.00/item)
• Lastshopping: 4.2daysago(HighUrgency)
• It’sbeenawhile—considershoppingtosupportlocaleconomy
DecisionTask: YouneedtochooseONEactionfromtheavailableoptionsbelow.
Considerhealthrisks,economicneeds,andyourpersonalcharacteristics. Remem-
ber: YoucanonlyseeifnearbypeopleLOOKsick(symptomatic),nottheirexact
healthstatus!
AvailableActions:
1. GoToWork: Go to work. Earn money but risk infection. (Current wealth:
$450.00)
2. GoShopping: Gotonearestbusiness. Buysupplies(−$50)andsupportecon-
omy.
3. StayHome: Stay at home. Safe from infection but consume savings
(−$20/day).
4. SeekMedicalCare: Gotohospital. Cost: $100. Cureprobability: 80%.
ResponseFormat: PleaserespondinJSONformatwithyourchosenaction:
{
"action": "GoToWork" | "GoShopping" | "StayHome" | "SeekMedicalCare",
"params": {}, // Include parameters if required by the action
"reasoning": "Brief explanation of your decision (1-2 sentences)"
}
Important:
• ChooseEXACTLYONEactionfromthelistabove
• Provideclearreasoningforyourchoice
https://doi.org/10.3390/info17030259

Information2026,17,259 21of24
AppendixA.3. SampleOutput
TheLLMreturnsadecisioncompliantwiththeJSONformat:
LLMResponseExample
{
"action": "GoToWork",
"params": {},
"reasoning": "Despite the high epidemic risk, my low-income status and
dwindling savings ($450) force me to work to avoid financial ruin,
as implied by the devastating consequences of missing work."
}
AppendixA.4. CoreLogicImplementation
Tofurtherincreasetransparency,weprovidethecorePythonfunctionlogicusedto
generatetheaboveprompts(ListingsA1andA2).
ListingA1: RoleDescriptionGenerationFunction
def get_agent_role_desc(age: int, status: Status, social_stratum: int) -> str:
"""Generate role description for an agent"""
# Age category
if age < 18:
age_desc = "child"
age_concerns = "You are young and generally healthy, but must follow adult
guidance."
elif age < 30:
age_desc = "young adult"
age_concerns = "You are young and have lower risk from COVID-19, but can
still transmit the virus."
elif age < 50:
age_desc = "middle-aged adult"
age_concerns = "You have moderate risk from COVID-19 and responsibilities to
family/work."
# ... (code truncated for brevity)
# Social class
wealth_levels = ["poor", "low-income", "middle-class", "wealthy", "affluent"]
if social_stratum <= 1:
wealth_concerns = "Your limited financial resources mean you must balance
safety with economic survival. Missing work could be devastating."
# ...
return f"""You are a {age} year old {age_desc}.
{age_concerns}
Your social class is {wealth_levels[social_stratum]}.
{wealth_concerns}"""
https://doi.org/10.3390/info17030259

Information2026,17,259 22of24
ListingA2: DecisionPromptConstructionFunction(agents.py)
def _build_decision_prompt(self, visible_info, action_registry, available_actions=
None):
"""Build REALISTIC prompt for LLM decision"""
# ... (state extraction)
prompt = f"""
**Current State (Day {visible_info[’day’]}, Hour {visible_info[’hour’]}):**
- Health: {own_status[’health’]}
- Position: ({pos_x:.1f}, {pos_y:.1f})
- Age: {own_status[’age’]} years old
- Wealth: ${wealth:.2f}
- Social Class: {[’Poor’, ’Low-income’][own_status[’social_stratum’]]}...
{epidemic_section}
**Nearby People:** {len(visible_info[’nearby_agents’])} people within 10 units
{self._format_nearby_agents(visible_info[’nearby_agents’])}
**Decision Task:**
You need to choose ONE action from the available options below.
Consider health risks, economic needs, and your personal characteristics.
Remember: You can only see if nearby people LOOK sick (symptomatic), not their exact
health status!
**Available Actions:**
{action_list}
...
"""
return prompt
AppendixA.5. ActionDescriptions
Each option in the action space has a specific description informing the LLM of
potentialconsequences.
TableA1.ActionDescriptionsusedinPrompts.
Action DescriptionPrompt
Gotowork—Normalworkschedule,earnsalaryincome(exposurerisk)
[CRITICAL]Missingworkfor3consecutivedays(72h)willresultin
GoToWork termination and job loss. [INCOME] Work provides monthly salary.
Unemployed=noregularincome. [RISK]Exposuretocoworkersand
customersduringepidemic.
Stay home—Avoid exposure risk, but has employment consequences
[SAFETY]Stayhometoprotecthealthandavoidvirusexposure.[WARN-
StayHome ING]Ifemployed:Missingworkfor3consecutiveDAYS(72h)willresult
inTERMINATION—Youwillbefiredandloseyourjob. [BALANCE]
Considerifstayinghomeisworthriskingjobloss.
Go shopping—Purchase household necessities [PURPOSE] Maintain
householdsuppliesandsupportlocaleconomy. [CONSIDERATIONS]—
GoShopping Health risk: Exposure to other people—Economic impact: Supports
localbusinesses—Householdneeds: Importantwhensuppliesarerun-
ninglow.
https://doi.org/10.3390/info17030259

Information2026,17,259 23of24
References
1. Kermack,W.O.;McKendrick,A.G.Acontributiontothemathematicaltheoryofepidemics.Proc.R.Soc.Lond.Ser.AContain.Pap.
Math.Phys.Character1927,115,700–721.[CrossRef]
2. Ferguson,N.M.;Laydon,D.;Nedjati-Gilani,G.;Imai,N.;Ainslie,K.;Baguelin,M.;Bhatia,S.;Boonyasiri,A.;Cucunuba,Z.;
Cuomo-Dannenburg,G.; etal. Report9: ImpactofNon-PharmaceuticalInterventions(NPIs)toReduceCOVID-19Mortalityand
HealthcareDemand;Report9;ImperialCollegeLondon:London,UK,2020.[CrossRef]
3. Epstein,J.M.GenerativeSocialScience:StudiesinAgent-BasedComputationalModeling;PrincetonUniversityPress:Princeton,NJ,USA,2006.
4. Helbing,D.;Balietti,S. Agent-basedmodeling. InSocialSelf-Organization: Agent-BasedSimulationsandExperimentstoStudy
EmergentSocialBehavior;Springer:Berlin/Heidelberg,Germany,2012;pp.25–70.
5. Wang,L.;Ma,C.;Feng,X.;Zhang,Z.;Yang,H.;Zhang,J.;Chen,Z.;Tang,J.;Chen,X.;Lin,Y.;etal. Asurveyonlargelanguage
modelbasedautonomousagents. Front.Comput.Sci.2024,18,186345.[CrossRef]
6. Bommasani,R.;Hudson,D.A.;Adeli,E.;Altman,R.;Arora,S.;vonArx,S.;Bernstein,M.S.;Bohg,J.;Bosselut,A.;Brunskill,E.;etal.On
theOpportunitiesandRisksofFoundationModels. arXiv2021,arXiv:2108.07258.[CrossRef]
7. Zhao,Q.;Wang,J.;Zhang,Y.;Jin,Y.;Zhu,K.;Chen,H.;Xie,X. Competeai:Understandingthecompetitiondynamicsinlarge
languagemodel-basedagents. arXiv2023,arXiv:2310.17512.
8. Park,J.S.;O’Brien,J.C.;Cai,C.J.;Morris,M.R.;Liang,P.;Bernstein,M.S. Generativeagents: Interactivesimulacraofhuman
behavior. arXiv2023,arXiv:2304.03442.[CrossRef]
9. DeMarchi,S.;Page,S.E. Agent-basedmodels. Annu.Rev.PoliticalSci.2014,17,1–20.[CrossRef]
10. Farmer,J.D.;Foley,D. Theeconomyneedsagent-basedmodelling. Nature2009,460,685–686.[CrossRef]
11. Filippas,A.;Horton,J.J.;Manning,B.S.Largelanguagemodelsassimulatedeconomicagents:Whatcanwelearnfromhomo
silicus? InProceedingsofthe25thACMConferenceonEconomicsandComputation,NewHaven,CT,USA,8–11July2024;
pp.614–615.
12. Pearl,J.;Glymour,M.;Jewell,N.P.CausalInferenceinStatistics:APrimer;JohnWiley&Sons:Hoboken,NJ,USA,2016.
13. Hornyak,T. AgenticAIIsHere—ButAreWeReady? Res.Technol.Manag.2025,68,59–60.[CrossRef]
14. Eichenbaum,M.S.;Rebelo,S.;Trabandt,M. Themacroeconomicsofepidemics. Rev.Financ.Stud.2021,34,5149–5187.[CrossRef]
15. Acemoglu,D.;Chernozhukov,V.;Werning,I.;Whinston,M.D. OptimaltargetedlockdownsinamultigroupSIRmodel. Am.
Econ.Rev.Insights2021,3,487–502.[CrossRef]
16. Alvarez,F.;Argente,D.;Lippi,F. AsimpleplanningproblemforCOVID-19lock-down,testing,andtracing. Am. Econ. Rev.
Insights2021,3,367–382.[CrossRef]
17. Silva,P.C.;Batista,P.V.;Lima,H.S.;Alves,M.A.;Guimarães,F.G.;Silva,R.C. COVID-ABS:Anagent-basedmodelofCOVID-19
epidemictosimulatehealthandeconomiceffectsofsocialdistancinginterventions. ChaosSolitonsFractals2020,139,110088.
[CrossRef]
18. Xi,Z.;Chen,W.;Guo,X.;He,W.;Ding,Y.;Hong,B.;Zhang,M.;Wang,J.;Jin,S.;Zhou,E.;etal. Theriseandpotentialoflarge
languagemodelbasedagents:Asurvey. Sci.ChinaInf.Sci.2025,68,121101.[CrossRef]
19. Sumers,T.;Yao,S.;Narasimhan,K.;Griffiths,T.Cognitivearchitecturesforlanguageagents.Trans.Mach.Learn.Res.2023.
20. Tao,L.;Liu,H.;Ning,G.;Cao,W.;Huang,B.;Lu,C. LLM-basedframeworkforbearingfaultdiagnosis. Mech.Syst.SignalProcess.
2025,224,112127.[CrossRef]
21. Wang, L.; He, X.; Luo, D. Deep reinforcement learning for greenhouse climate control. In Proceedings of the 2020 IEEE
InternationalConferenceonKnowledgeGraph(ICKG),Nanjing,China,9–11August2020;pp.474–480.
22. Zhang,Y.;Wei,C.;Wu,S.;He,Z.;Yu,W. Geogpt:UnderstandingandprocessinggeospatialtasksthroughanautonomousGPT.
arXiv2023,arXiv:2307.07930.[CrossRef]
23. IBGE.PirâmideEtária.2020.Availableonline:https://educa.ibge.gov.br/jovens/conheca-o-brasil/populacao/18318-piramide-
etaria.html(accessedon2June2020).
24. IBGE.Censodemográfico:Tabela2019—MoradoresemDomicíliosParticularesPermanentesporDensidadedeMoradorespor
CômodoeNúmerodeBanheiros.2020.Availableonline:https://sidra.ibge.gov.br/tabela/2019(accessedon2June2020).
25. IPEA.EstimativadaPopulaçãoemSituaçãodeRuanoBrasil;TextoparaDiscussão2246;InstitutodePesquisaEconômicaAplicada:
Brasília,Brazil,2020
26. WorldBank.LacEquityLab:IncomeInequality—CompositionbyQuintile.2020.Availableonline:https://www.worldbank.
org/en/topic/poverty/lac-equity-lab1/income-inequality/composition-by-quintile(accessedon3June2020).
27. IBGE.DemografiadasEmpresaseEmpreendedorismo2017: TaxadeSobrevivênciafoide84.8%. IBGEAgênciadeNotícias,
Release25738,2017.Availableonline:https://agenciadenoticias.ibge.gov.br/(accessedon2June2020).
28. WorldBank.BusinessDensityandtheNumberofNewBusinessRegistrations.2020.Availableonline:https://data.worldbank.
org/indicator/IC.BUS.NREG(accessedon1December2024).
29. Exame.DesempregoAtinge12.2%No1ºTrimestre,dizIBGE.2020.Availableonline:https://exame.com/economia/brasil-tem-
desemprego-de-122-no-primeiro-trimestre-diz-ibge/(accessedon3June2020).
https://doi.org/10.3390/info17030259

Information2026,17,259 24of24
30. Lima,C.M.A.d.O.Informaçõessobreonovocoronavírus(COVID-19). Radiol.Bras.2020,53,V–VI.[CrossRef]
31. Li,Q.;Guan,X.;Wu,P.;Wang,X.;Zhou,L.;Tong,Y.;Ren,R.;Leung,K.S.;Lau,E.H.;Wong,J.Y.;etal.Earlytransmissiondynamics
inWuhan,China,ofnovelcoronavirus–infectedpneumonia.N.Engl.J.Med.2020,382,1199–1207.[CrossRef][PubMed]
32. Lauer,S.A.;Grantz,K.H.;Bi,Q.;Jones,F.K.;Zheng,Q.;Meredith,H.R.;Azman,A.S.;Reich,N.G.;Lessler,J. Theincubation
periodofcoronavirusdisease2019(COVID-19)frompubliclyreportedconfirmedcases:Estimationandapplication. Ann.Intern.
Med.2020,172,577–582.[CrossRef]
33. Housen, T.; Parry, A.E.; Sheel, M.HowLongAreYouInfectiousWhenyouHaveCoronavirus? Conversation2020, 135295.
Availableonline:https://theconversation.com/(accessedon2June2020).
34. EpidemiologyWorkingGroupforNCIPEpidemicResponse,ChineseCenterforDiseaseControlandPrevention.Theepidemio-
logicalcharacteristicsofanoutbreakof2019novelcoronavirusdiseases(COVID-19)inChina.ZhonghuaLiuXingBingXueZaZhi
=ZhonghuaLiuxingbingxueZazhi2020,41,145–151.[CrossRef]
Disclaimer/Publisher’sNote: Thestatements, opinionsanddatacontainedinallpublicationsaresolelythoseoftheindividual
author(s)andcontributor(s)andnotofMDPIand/ortheeditor(s).MDPIand/ortheeditor(s)disclaimresponsibilityforanyinjuryto
peopleorpropertyresultingfromanyideas,methods,instructionsorproductsreferredtointhecontent.
https://doi.org/10.3390/info17030259
