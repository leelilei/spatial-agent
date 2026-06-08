Title: CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale LLM-Driven Agent Simulation

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_core/13_HC15_CitySim.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:51+00:00
- page_count: 13
- status: ok
- text_char_count: 50858

Metadata:
- author: Nicolas Bougie; Narimasa Watanabe
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Related Work (page 2)
- Method (page 2)
  - Cognitive State Representation (page 2)
    - Persona Module (page 2)
    - Memory Module (page 2)
    - Belief Module (page 3)
    - Needs Module (page 3)
    - Long-Term Goal Module (page 3)
    - Perception Module (page 3)
  - Mobility Behaviors (page 3)
    - Planning Module (page 3)
    - Place Selection Module (page 4)
    - Vehicle Selection Module (page 4)
  - Social Behaviors (page 4)
- Experiments (page 4)
  - Macro-level Time Use (page 5)
  - Pairwise Human Preferences (page 5)
  - Travel Patterns (page 5)
  - Predicting POI Popularity (page 5)
  - Social Studies using Synthetic Agents (page 6)
  - Modeling Crowd Density (page 6)
- Conclusion (page 6)
- Limitations (page 7)
- Ethics Statement (page 7)
- Experimental Setup (page 9)
  - Module Details (page 10)
    - Planning Module (page 10)
    - Social Module (page 10)
- Discussion (page 10)
  - Pseudo-Code (page 11)
- Additional Experiments (page 12)
  - Performance Evaluation (page 12)
  - Human Likeliness (page 12)
  - Needs Evolution (page 12)
  - Belief Estimation (page 12)
  - Ablation Study (page 13)

Markdown Content:

5202
nuJ
62
]IA.sc[
1v50812.6052:viXra
CitySim: Modeling Urban Behaviors and City Dynamics with Large-Scale
LLM-Driven Agent Simulation
1 1
NicolasBougie ,NarimasaWatanabe
{nicolas.bougie,narimasa.watanabe}@woven.toyota
1
WovenbyToyota
Abstract Recentadvancementsinlargelanguagemodels
(LLMs)offerpromisingavenuesincreatinghuman-
Modeling human behavior in urban environ-
likeagentsforstudyingcomplexurbanphenomena,
ments is fundamental for social science, be-
enablingdetailedexplorationintoindividual-level
havioral studies, and urban planning. Prior
decisions and social interactions (Epstein, 1999;
work often rely on rigid, hand-crafted rules,
limitingtheirabilitytosimulatenuancedinten- MacalandNorth,2005;Gaoetal.,2024;Parketal.,
tions,plans,andadaptivebehaviors. Address- 2023a). Numerous studies have pointed out that
ingthesechallenges,weenvisionanurbansim- afterbeingempoweredbyLLMs,agentsgainthe
ulator(CitySim),capitalizingonbreakthroughs ability to reason, plan, and interact through natu-
inhuman-levelintelligenceexhibitedbylarge
ral language (Gao et al., 2024; Wei et al., 2022;
language models. In CitySim, agents gener-
BougieandWatanabe,2025;Lietal.,2023;Park
aterealisticdailyschedulesusingarecursive
etal.,2023a;BougieandWatanabe,2024). Api-
value-drivenapproachthatbalancesmandatory
oneering example is the Generative Agent (Park
activities,personalhabits,andsituationalfac-
tors. Toenablelong-term,lifelikesimulations, etal.,2023a),whichconstructsasmall-scalesoci-
weendowagentswithbeliefs,long-termgoals, etywithina2Dgameengine. Recently,AgentSoci-
andspatialmemoryfornavigation.CitySimex- ety(Piaoetal.,2025)hasintroducedalarge-scale
hibitscloseralignmentwithrealhumansthan multi-agentplatform,butlackslong-termcognitive
priorwork,bothatmicroandmacrolevels. Ad-
mechanismssuchasevolvinggoals,evolvingpref-
ditionally,weconductinsightfulexperiments
erences, or spatial memory. Despite advances in
by modeling tens of thousands of agents and
modelingmotivation,memory,andsocialinterac-
evaluatingtheircollectivebehaviorsundervar-
ious real-world scenarios, including estimat- tion(Yeetal.,2025),currentapproachesstillface
ingcrowddensity,predictingplacepopularity, severalchallenges. (1)Agentsoftenplanactivities
andassessingwell-being. Ourresultshighlight inafixedsequentialmanner,overlookingtherela-
CitySimasascalable,flexibletestbedforun- tiveimportanceandinterdependenciesamongdaily
derstandingandforecastingurbanphenomena.
tasks;(2)Long-termsimulationisunderexplored,
ignoring the effect of beliefs and long-term goal
1 Introduction
formationandadaptation. (3)Placeselectionand
Simulatingrealisticcity-scalebehaviorsisalong- vehiclechoiceareusuallynotconsidered.
standinggoalinsocialscienceandartificialintel- In this work, we present CitySim, a scalable
ligence (Hofmanetal.,2021;Lazeretal.,2009). citysimulationframeworkempoweredbyLLMs.
Traditional models often leverage hand-crafted CitySimagentsautonomouslygeneratedailysched-
rulesorutilityfunctions,restrictingtheirabilityto ulesandlong-termplansthrougharecursive,value-
representthediversity,adaptability,andlong-term driven planning process that balances mandatory
dynamicsinherentinhumans (Zhengetal.,2022; activities,personalhabits,andsituationalcontext.
Wang et al., 2023). As a result, they often yield Eachagentisequippedwithspatialandtemporal
unrealisticbehaviors: rigidschedules,inabilityto memories,whichenableagentstorecallpastexpe-
develop new preferences, and poor adaptation to riences,formandupdatebeliefsaboutplacesthey
novelorchangingenvironments (Fengetal.,2024). visit,andadapttheirfuturedecisionsaccordingly.
Hence,itremainschallengingtosimulatenuanced Namely,agentscontinuouslyrevisebeliefs,trans-
psychological, social, and environmental drivers portationchoices,andinternalstates(suchasmood
shapingactionsinurbansettings. orsatisfaction)inresponsetoneeds,environmental
1

feedback, and social interactions. To lay a reli- 3 Method
able and diverse foundation, agents are equipped
We introduce CitySim, a framework simulat-
with a persona module derived from real-world
ing human-like behavior in a dynamic, graph-
surveys,encompassingdemographic,personality
structuredurbanenvironment. Agentsareendowed
traits,preferencesandhabits. Thisresultsinhetero-
withadvancedcognitiverepresentations,including
geneous,context-awareurbanpopulationscapable
personas,long-termgoals,beliefs,andneeds. At
ofcapturingthecomplexityofrealsocieties.
eachsimulationstep,anagentfirstperceivesitsen-
vironment(e.g.,location,presenceoffriends)and
2 RelatedWork
internalstate. Alongwithinsightsretrievedfroma
memorymodule,itdecidesonacourseofaction–
Replicatinghumanbehaviorinurbanenvironments
seekingfoodwhenhungry. Theagentthenreacts
remainsachallenge (Hofmanetal.,2021;Lazer
byeitherfollowingitscurrentplan,adjustingfuture
etal.,2009). Traditionalagent-basedmodelshave
activities when an unexpected event happens, or
been widely used to study complex phenomena,
fillingtheagent’sfreetimeviavalue-drivenplan-
resourceallocation,andpolicyevaluation(Epstein,
ning. Finally, it reflects on recent experiences to
1999; Macal and North, 2005; Wilensky, 2015).
developbeliefs,opinionsandhabits,synthesizing
Yet,theydependonhard-codedrulesorfixedutil-
memoriesintohigher-levelreflections.
ityfunctions,constrainingtheircapacitytocapture
behavioral diversity, adaptability, and long-term
3.1 CognitiveStateRepresentation
dynamics (Feng et al., 2024; Zheng et al., 2022;
Wang et al., 2023). Recent frameworks such as 3.1.1 PersonaModule
CityBench(Fengetal.,2024)andAI4SIM(Zheng The persona module is fundamental for aligning
et al., 2022) have begun to integrate richer, data- agentswithgenuinehumanbehaviorsinurbansim-
drivenapproaches,yetrealisticcognitiveandmoti- ulation. Tolayareliablefoundation,questionnaire-
vationalmodelingremainslimited. derivedattributesinclude:
Recently, LLMs have opened new possibili- • Demographic Attributes: Name, age, gen-
ties for simulating human-like agents in virtual der,occupation,income,hobbies,education,
worlds (Park et al., 2023a; Gao et al., 2024; Li householdcomposition,andlifestage. These
etal.,2023;Weietal.,2022). LLM-poweredagents modulatetheagent’sactivityspace(e.g.,chil-
canreason,plan,andinteractthroughnaturallan- dren attend school; retirees prefer daytime
guage(Gaoetal.,2024;Weietal.,2022;Bougie leisure)andshapepatternsindailyroutines.
and Watanabe, 2025; Park et al., 2023a; Bougie • Spatial Anchors: Home, and work/school
and Watanabe, 2024). Nevertheless, most LLM- locations.
basedagentsstillplanactivitiesinamyopicorrigid • PsychographicTraits: Personalitytraitsare
manner,struggletoupdatebeliefsfromexperience, defined by the Big Five personality facets:
andoftenrepresentpersonassolelyviademograph- Openness, Conscientiousness, Extraversion,
ics(Wangetal.,2023). Tosupportdifferentappli- Agreeableness, and Neuroticism, each mea-
cationscenarios,Zhouetal.(2023)presentanopen- suredona1to3scale.
sourceframeworkforautonomouslanguageagents, • HabitsandPreferences: routinesthatunder-
and Hong et al. (2024) demonstrate how agents lie human activity. Each agent is initialized
can collaborate in complex software engineering with a set of empirically-derived habits and
tasks. Asresearchmovestowardlarger-scalesimu- preferences, including activity preferences,
lations,computationalefficiencybecomescrucial. habits(e.g.,earlyriser),andleisurepatterns.
Park et al. (2024) scale up simulations to 1,000
3.1.2 MemoryModule
agents but still inherits prohibitive costs. Frame-
workssuchasAgentSociety(Piaoetal.,2025)or Humans retain diverse memories, bifurcating
MobileCity (Ye et al., 2025) use episodic mem- mainly into factual and emotional categories
oryandgravity-basedplaceselection,butneglect (LaBarandCabeza,2006). InCitySim,themem-
habits and transport choices. CitySim advances orymodulecomprisesthreecomponents: tempo-
thisareabyintegratingrecursiveactivityplanning, ral,reflective,andspatialmemories.
dynamicmemoryandbeliefmodules,enablinglife- Temporal Memory This memory is organized
like,context-sensitive,long-termbehaviors. chronologically, with multiple memory nodes in
2

each stream. Each memory node contains four max(0, s (t−∆t) −α ∆t). Followingeachac-
n n
components: time,location,andobservation,and tivity or significant events, the LLM evaluates
key. The key serves to filter observations during outcomes and updates scores based on agent ex-
retrieval. Newentriesareappendedateachsimula- perience, contextual information, and current in-
tionstep,action,orreflection. ternal state. Needs are prioritized (hungry >
ReflectiveMemoryThereflectivememoryrecords safe > tired > social) using thresholds T :
n
the agent’s thoughts and attitudes toward events dominantneed = argmin {s ≤ T }. Ifahigher-
n n n
storedintemporalmemory. Eachentryislinkedto priority need arises, ongoing plans may be inter-
oneormorenodesinthetemporalmemory,reflect- ruptedandneedsreprioritized. Thedominantneed
inghowtheagentperceivesorreactstoaspecific isstoredasplaintextinthepersonamodule.
event. Attheendofeachday,wesynthesizethose
3.1.5 Long-TermGoalModule
memoriesintohigher-levelreflections,enablingthe
Wemodeltheformationandrevisionoftheagents’
agenttodrawconclusionsaboutitself.
high-levelaspirations,drawingontheMaslow’sHi-
Spatial Memory. Spatial memory maintains be-
liefs b ∈ RK about point of interests (POIs), erarchyofNeeds(Huitt,2007). Goalsarerevisited
i
monthly or following major life events (e.g., em-
where each dimension corresponds to an aspect
∈ {price,atmosphere,satisfaction,convenience}. ploymentchanges). Indetail,theLLMisqueried
When the agent visits a POI i at time t and ob- usingpersona,financialstatus,socialcontacts,re-
(t) (t) centactivities,andcurrentgoals. Alongwiththese
servesoutcomeo ,thebeliefb isupdatedusing
i i inputs,wecomputetheneedfulfillment,definedas
aKalmanfiltertoreducenoise(seeAppendix). If
theproportionofthedayduringtheneedsexceed
a POI i has not been visited, b is initialized via
i
theirthresholds. Wealsomonitorfinancialstress
embedding-based similarity to previously visited
(income < 0.9×expenses) and social isolation
locations: b
i
← E
j∈N(i)
[b
j
],whereN(i)denotes
(fewer than 3 unique contacts in last 7 days). To
similarPOIsretrievedfromspatialmemory. Note
capturetheinterest,wecalculatetheproportionof
that the uncertainty is retrieved along b to guide
i
recentlyvisitedPOIswhosecurrentsatisfactionbe-
theagentduringthePOIselection. Toreflectfor-
liefexceeds0.5: interest = 1 ∑ I [b sat > 0.5],
gettingandenvironmentalchanges,weintroducea ∣V∣ i∈V i
sat
decay. Afterasimulatedday,eachdimensiondof whereb i isthesatisfactionbeliefforPOIiandV
b isupdatedas: b ← (1−λ)b +λb ,where isthesetofPOIsvisitedinthelast30days. Given
i i,d i,d 0,d
b 0 istheneutralvalue(0.5)andλisthedecayrate. thiscontextc,astructuredpromptp goal conditions
the LLM to generate coherent short (few weeks)
3.1.3 BeliefModule andlong-termgoals: g 1 ,g 2 ,...,g M ∼ LLM(p ∣
t t t goal
Thismoduleistriggeredeachtimetheagentvisits θ,c),whereresultinggoalsg m informsubsequent
t
aplace. UponvisitingPOIi,theagentgeneratesa planningmodules.
(t)
subjectiveobservationo bypromptinganLLM
i 3.1.6 PerceptionModule
with visit-specific context, including the agent’s
Ateachsimulationtimestep,theperceptionmodule
persona, currentactivity, emotionalstate, andde-
receivesanobservationfromtheenvironmentand
scriptionofthePOI.Thisobservationcapturesthe
determines whether the agent should react. If so,
agent’simmediateappraisalofthevisit,providing
theperceptionmoduleenumeratesthesetofavail-
a multi-dimensional assessment with associated
able modules, each accompanied by a functional
reasoning. Thenewobservationisthenintegrated
(t−1) description,andqueriestheLLMtoselectthemost
withthepriorbeliefb ,asdescribedabove.
i appropriatemoduleforthecurrentsituation. Mod-
3.1.4 NeedsModule ule selection is managed by a dispatcher, which
The agent’s tracks and prioritizes four pri- invokesthecorrespondingmodule(e.g.,planning,
mary needs: hunger, energy, safety, and so- social interaction) based on the agent’s inferred
cial connection. At the start of each day, needs,shortexplanation,andrequiredparameters.
an LLM prompt, conditioned on demographic
3.2 MobilityBehaviors
and temporal context, serves to initialize scores:
s = {hunger, energy, safety, social} ∈ [0,1] 4 . 3.2.1 PlanningModule
0
Throughout the day, scores decay continuously Dailyschedulesaregeneratedviaarecursivede-
based on decay rate α for need n: s (t) = compositionoftimeinto[blocks], eachinclud-
n n
3

ingastartingtime,duration,andactivity/intention. cluding distance d to the next POI, time of day
Planning begins each day with mandatory tasks t, month m, weather w, temperature T, and per-
(e.g.,sleep,work)basedoneachagentpersonaand sona p, a structured prompt p is used to query
v
needs, then recursively fills remaining [EMPTY] the LLM: LLM(p ∣ d,t,m,w,T,p,θ,V), where
v
blockswithmedium-prioritytasks(e.g.,meals,hy- V is the set of available vehicles. Along with
∗
giene). Ifaselectedactivitydoesnotfilltheentire the selected vehicle v , the agent is instructed to
interval,theblockmaybesubdividedaccordingto provide a brief justification, which are stored in
theactivityduration. thereflectivememory. Theprocessapproximates
∗
Some [blocks] remain unfilled after this pro- v = argmax
v∈V
U(d,t,m,w,T,p,θ,V),where
cess. According to Maslow’s Hierarchy (Huitt, U( ⋅ )isanimplicitutilityfunctionimplementedby
2007),thesearetypicallyusedforleisureorlong- theLLM’sreasoningovertheprovidedcontext.
termgoals(e.g.,hobbies,socializing),andarefilled
at execution time based on the agent’s state, lo- 3.3 SocialBehaviors
cation, needs, and schedule using value-driven
Thefoundationofoursocialmoduleisaweighted
planning. For each empty block, the agent gen-
social network where each edge encodes an
eratesandevaluatesmultiplecandidateactivities,
agent’sevolvingsocialbeliefsaboutothers. Each
selectingtheoneexpectedtobestsatisfyintrinsic
agent u maintains a social belief vector b
desires. Thisselectionishandledthroughasingle u,v
for every contact v, capturing dimensions: ∈
structuredLLMcallwithinternalreasoningsteps.
{affinity,trust,familiarity}. These beliefs are ini-
3.2.2 PlaceSelectionModule tializedatsimulationstartbasedondemographic
Foreachactivity,thelocationisdeterminedusinga similarityandrelationships,thenupdatedcontinu-
belief-awaregravitymodel,extendingAgentSoci- ously. Weconsidertwotypesofinteractions: face-
ety(Piaoetal.,2025). Forhomeorworkactivities, to-face and online. After an interaction, b u,v is
addressesfromtheagent’spersonaareused. updatedusingobservedoutcome(positive,neutral,
Step1: Macro-levelAreaSelection. Theagentde- negative)foreachdimension.
cideswhethertoremaininthevicinityortravelfar- Face-to-face interactions occur when agents
therbypromptingtheLLMwithintention,sched- are co-located in same space. Agent u selects a
ule,emotionalstate,areavisithistory,andpopular conversation partner v according to their current
nearbyareas(rankedbydistanceandpopularity). belief score, with probability: p = b u,v ,
Step 2: Micro-level POI Selection. Within the
v ∑
v
′∈V b
u,v
′
where V is the set of eligible co-located agents,
chosenarea,theagent:
andb isthecurrentbelieftowardv.
u,v
Intention Extraction: Determines required POI
Onlineinteractionssimulateremotecommuni-
types (e.g., café, park) andadjust feasible ranges
cation(e.g.,phonecallsormessasing). Whenagent
by integrating internal (e.g., age, daily schedule)
u’ssocialsatisfactionscorefallsbelowadefined
and environmental factors (e.g., weather, traffic),
threshold,itseekstocontactanacquaintancedur-
providingasetofPOIscandidates.
ing leisure time, with selection probability based
Belief-weightedGravityModel: Foreachcandi-
onbeliefsandrelationshipstrengths.
datePOIi,computestheselectionweightas
(b +ε)/D
1+γ(b
j
−0.5)
4 Experiments
j ij
p = (1)
ij
∑ (b +ε)/D
1+γ(b
k
−0.5)
Settings. Experiments are conducted using the
k k ik
urbansimulationframeworkproposedinAgentSo-
whereb isthebelief-basedattractivenessofloca-
j
ciety(Piaoetal.,2025). Allagentsarepoweredby
tionj,andD isthedistance,γ controlsdistance
ij
theGPT-4o-miniversionofChatGPT,exceptwhen
decay,andεisasmallpositiveconstanttoensure
specifieddifferently,withthenumberofagentsset
numericalstability. Here, b istheweightedsum
j
to1,000locatedinTokyometropolitanarea.
of current beliefs. If no belief exists for j, it is
BaselinesWecompareCitySimwithGeAn(Park
estimatedfromsimilarPOIsinspatialmemory.
etal.,2023b),AGA(Yuetal.,2024),HumanoidA-
3.2.3 VehicleSelectionModule gent (Wang et al., 2023). We also report results
Finally, the most appropriate transport mode is withourclosestcompetitors,MobileCity(Yeetal.,
estimated for each trip. Given trip context, in- 2025)andAgentSociety(Piaoetal.,2025).
4

Figure 1: Time-use distribution across activity cate- Figure3: Averagenumberofagenttravelsperhouron
gories and age groups. Solid bars represent ground weekdays(left)andweekends(right).
truth;stripedbarsshowresultsfromoursimulation.
pareanonymizeddailyroutinesusingthreecriteria:
(i)Naturalness,(ii)Coherence; and(iii)Plausi-
bility. The pairwise win rate (Figure 2) reflects
howofteneachagentwasjudgedmorehuman-like
than another. CitySim achieves the highest aver-
age win rates, outperforming all baselines. This
ismainlyduetoexplicitneedmodeling,dynamic
goals,andmemory-basedplanning,whichsupport
adaptive, context-sensitive behavior. In contrast,
MobileCityandAgentSocietyaremorerigidand
repetitive,oftendisregardingcommonsocialand
temporalnorms, contributingtosuspicionsofAI
involvement.
Figure2: Pairwisewinratematrix. Eachentrydenotes
4.3 TravelPatterns
theproportionoftrialsinwhichtherowagentisjudged
morehuman-likethanthecolumnagent. We now compare simulated travel distributions
withground-truthdata,derivedfromaproprietary
city-scale dataset. Figure 3 shows the average
4.1 Macro-levelTimeUse
numberoftravelsperhourforbothweekdaysand
Toassessmacro-levelbehavioralrealism,wecom- weekends. CitySimcloselyreproducesreal-world
pareouragents’time-usedistributionwithground- patterns, matching the timing and amplitude of
truthdatafromthe2021Japanesenationaltimeuse commutingpeaksandweekendleisureactivity. In
survey (Statistics Bureau of Japan, 2021). Each contrast, MobileCity exhibits overly rigid spikes
agent simulates two months of daily activities, atcommutetimes,whileBaselineremainslargely
which are mapped to the high-level activity cat- static. Other agent methods (AGA, HumanoidA-
egoriesusedinthesurvey(e.g.,Work,Commute, gent,AgentSociety)capturesomebroadtrendsbut
Housework,PersonalCare&Sleep). Weaggregate displayeitherdiffusedormistimedtravelpeaks. In
and normalize the total time spent on each activ- contrast,ourapproachproducestemporallycoher-
ity by age group, reporting the share of day. As ent,human-likemobilitypatternsthatconsistently
showninFigure1, thedistributionofdailyactiv- outperformotherLLMagentbaselines
ities closely matches the survey statistics. These
findingsdemonstratethatourmodelcanfaithfully 4.4 PredictingPOIPopularity
producecity-scale,macro-levelactivitypatterns.
A key application is forecasting which POI will
attract the most visitors, essential for urban plan-
4.2 PairwiseHumanPreferences
ning,retailstrategy,oreventmanagement. Inlight
Toevaluatethebehavioralrealism,weconducted ofthis,weevaluateCitySim’sasapredictivetool
15 independent trials for each approach. To miti- forreal-worldPOIpopularityinShibuya(Tokyo,
gatestylisticbiasingeneratedactivitysequences, Japan). Ground-truthwasestimatedusingratings
alloutputswerefirstnormalizedusingLlama-3.1 fromGoogleMaps. Simulatedpopularitywasmea-
70Btoensureconsistentformattingacrossmodels. suredbycountingagentvisitstoeachPOIovera
Foreachagentpair,GPT-4owaspromptedtocom- simulatedmonth. WecomparedCitySimwithSo-
5

Figure4: Comparisonofreal-worldPOIpopularityand Figure 5: Comparison of simulated (left) and real-
simulated-basedvisitsinShibuya. world(right)crowddensityheatmapsinShibuya,Tokyo.
Warmercolorsindicatehigherdensities.
F1-macro(mean±std)
pleteagentbackgroundknowledgeandimperfect
GeAn 0.19±0.03
AGA 0.20±0.03 personainitialization,whichrestricttheirabilityto
HumanoidAgent 0.22±0.03 fullyreplicatethenuancesofhumanwell-being.
AgentSociety 0.28±0.02
MobileCity 0.21±0.02 4.6 ModelingCrowdDensity
CitySim 0.36±0.02 Predictingspatialcrowddensityisvitalforurban
GBDT 0.45±0.04 management, public safety, and event planning.
WenowassessCitySim’sabilitytoreproducereal-
Table1: MacroF1-scoreforwell-beingclassprediction
worldpatternsofpedestrianconcentrationacross
(5-class)acrossmodels,evaluatedonaproprietaryagent
Shibuya(Japan). Weaggregateagentvisitcounts
survey. Medalsindicatetop-3methods.
by location to generate simulated crowd density
heatmaps,andcomparetheseagainstground-truth
cietyAgentbycalculatingSpearmanrankcorrela- distributionsestimatedfromsmartphonelocation
tionsbetweensimulatedandreal-worldpopularity. data. As shown in Figure 5, CitySim accurately
As shown in Figure 4, CitySim achieves positive mimics mobility patterns observed in real world,
alignment, whereas SocietyAgent yields notably with the highest densities around central transit
weakercorrelations. Notably,CitySimagentsex- nodes and along major commercial streets. We
hibitapositivebiastowardwell-knownorbranded alsonoticethatCitySimsometimesunderestimates
POIs,leadingtoaninflatedestimateoftheirreal- crowd in small streets, likely due to its belief-
worldpopularity. Thesefindingsshowthepotential enhancedgravitymodel,whichmayreflectLLM
of CitySim as a practical tool for predicting POI popularity bias (Lichtenberg et al., 2024). This
popularityforlocation-basedbusinessstrategies. furtherhighlightsthepotentialofanagent-driven
approachfora/bandwhat-iftesting,includingsce-
4.5 SocialStudiesusingSyntheticAgents nariosdifficulttoobserveinreal-worldsettings.
WeassessthepotentialofCitySimtoestimatepop-
5 Conclusion
ulation well-being. We use a proprietary dataset
comprising1,200well-beingsurveyresponsescol- WepresentCitySim,alarge-scaleframeworkfor
lected in Japan. Each record consists of a set of simulatinghuman-likeurbanbehaviorusingLLM-
questionsdesignedtoestimatewell-beingamong poweredagentsequippedwithrecursiveplanning,
5 classes. Agents were initialized with persona real-worldgroundedpersonas,long-termgoalfor-
profilesmatchingtherealsurveyrespondentsand mation,andbelief-awarememory. Resultsdemon-
engagedinthreeweeksofsimulatedcitylife, us- stratecloseralignmentofouragentswiththeirhu-
ingtheirmemorymoduletoanswerthesamesetof mancounterpartsatbothmicroandmacrolevels.
questions. Webenchmarkourmethodagainstagra- CitySimenablesthestudyofcomplexurbanphe-
dientboostingmodel(GBDT)trainedoncollected nomenaandsupportsmorerealistic,adaptiveagent
activities/locationsfromthedataset. Asreportedin behaviorscomparedtoprioragent-basedmodels.
Table1,theXGBoostbaselineachievesthehigh- ExperimentalresultshighlightCitySimasarobust
estmacroF1-score,whileCitySimcloselyfollows foundationforresearchandindustryapplicationsat
and outperforms prior agent-based work. These theintersectionofbehavioralmodelingandurban
simulation-basedapproachesarelimitedbyincom- planning,andsocialstudies.
6

6 Limitations marginalize the involvement of actual residents,
stakeholders,anddomainexpertsinthedesignand
Despiteachievingthebestperformancecompared
evaluationprocess. Werecommendthatsynthetic
tootherbaselines,itisimportanttoacknowledge
humansbeemployedprimarilytocomplement,not
severallimitationsofthiswork. Alimitationofthis
replace,humaninput,especiallyintheearlyphases
work lies in reproducibility of this work, which
of social studies or when involving real people
is limited because the data used for some exper-
posespracticalorethicalchallenges. Byadhering
iments is not public. Besides, our method may
to these principles, we aim to ensure that the use
inheritcultural,gender,andsocioeconomicbiases,
ofsyntheticurbanagentsisconductedinamanner
due to the nature of LLMs. Related to this, oc-
thatisethical,transparent,andsociallyresponsible.
casionalhallucinationshavebeenobservedwhen
generatingappraisalforrecentorless-knownPOIs,
whichcanleadtoinaccuratesimulationoutcomes. References
Moreover,theefficacyofourframeworkislargely
Nicolas Bougie and Narimasa Watanabe. 2024. Gen-
reliantonthestrengthsandweaknessesoftheun-
erativeadversarialreviews: Whenllmsbecomethe
derlyingLLMs. Theaccuracyofthesimulateduser critic. arXivpreprintarXiv:2412.10415.
behavior may be impacted by LLMs’ occasional
Nicolas Bougie and Narimasa Watanabe. 2025.
inconsistent,biased,orunfoundedoutputs. Finally,
Simuser: Simulating user behavior with large lan-
thelargenumberofinteractingmodulesmakesit guage models for recommender system evaluation.
difficult to isolate the effect of each component; arXivpreprintarXiv:2504.12722.
weincludeablationstudiesintheAppendixtopar-
Cheng-HanChiangandHung-yiLee.2023. Canlarge
tially address this. In the future, we will explore languagemodelsbeanalternativetohumanevalua-
andimprovetheseaspects. tions? arXivpreprintarXiv:2305.01937.
JoshuaMEpstein.1999. Agent-basedcomputational
7 EthicsStatement
models and generative social science. Complexity,
4(5):41–60.
ThispaperintroducesanLLM-drivenagentframe-
workforsimulatingurbanhumanbehavioratscale, JieFeng,JunZhang,JunboYan,XinZhang,Tianjian
enablingthestudyofcitydynamicsandsocialbe- Ouyang,TianhuiLiu,YuweiDu,SiqiGuo,andYong
Li.2024. Citybench: Evaluatingthecapabilitiesof
haviors in a realistic and cost-effective manner.
largelanguagemodelasworldmodel. arXivpreprint
While our approach brings clear advantages in arXiv:2406.13945.
termsofscalabilityandfaithfulness,italsoraises
ChenGao,XiaochongLan,NianLi,YuanYuan,Jingtao
importantethicalconsiderations.
Ding, ZhilunZhou, FengliXu, andYongLi.2024.
Theuseofsyntheticagentsinurbansimulation
Largelanguagemodelsempoweredagent-basedmod-
mayinadvertentlyamplifybiases, suchasstereo- eling and simulation: A survey and perspectives.
types about age, gender, occupation, or lifestyle, Humanities and Social Sciences Communications,
11(1):1–24.
if such patterns are present in the training data
oragentinitialization. Thereisalsothepotential ÖnderGürcan,VanjaFalck,MarkusGRousseau,and
risk of reinforcing or introducing new inequities Larissa L Lima. 2025. Towards an llm-powered
social digital twinning platform. arXiv preprint
insimulatedurbanpolicies,astheseagentsmight
arXiv:2505.10681.
reactinwaysthatprivilegeordisadvantagecertain
demographicgroups. Additionally,large-scalesim- Jake M Hofman, Duncan J Watts, Susan Athey, Filiz
Garip, Thomas L Griffiths, Jon Kleinberg, Helen
ulationofagentinteractionscouldenabletheiden-
Margetts,SendhilMullainathan,MatthewJSalganik,
tification and manipulation of behavioral trends,
SimineVazire,and1others.2021. Integratingexpla-
potentiallyinformingurbaninterventionsthatsteer nationandpredictionincomputationalsocialscience.
collective behavior in subtle or non-transparent Nature,595(7866):181–188.
ways. This raises concerns around consent and
SiruiHong,MingchenZhuge,JonathanChen,Xiawu
autonomy, especiallyifagentoutputsareusedto Zheng,YuhengCheng,JinlinWang,CeyaoZhang,
influencereal-worldpoliciesorindividualchoices ZiliWang,StevenKaShingYau,ZijuanLin,Liyang
withoutadequateoversight. Zhou, Chenyu Ran, Lingfeng Xiao, Chenglin Wu,
andJürgenSchmidhuber.2024. Metagpt: Metapro-
Finally, while synthetic agents can greatly ac-
grammingforAmulti-agentcollaborativeframework.
celerate early-stage exploration of urban scenar-
InInternationalConferenceonLearningRepresenta-
ios, there is a risk that their deployment might tions(ICLR).
7

WilliamHuitt.2007. Maslow’shierarchyofneeds. Ed- Statistics Bureau of Japan. 2021. Survey on
ucationalpsychologyinteractive,23. time use and leisure activities, 2021. https:
//www.e-stat.go.jp/en/stat-search/files?
KevinSLaBarandRobertoCabeza.2006. Cognitive page=1&toukei=00200533&tstat=000001158160.
neuroscienceofemotionalmemory. NatureReviews AccessedJuly2024.
Neuroscience,7(1):54–64.
ZhilinWang,Yu-YingChiu,andYuCheungChiu.2023.
DavidLazer,AlexPentland,LadaAdamic,SinanAral, Humanoidagents: Platformforsimulatinghuman-
Albert-László Barabási, Devon Brewer, Nicholas likegenerativeagents. InConferenceonEmpirical
Christakis, Noshir Contractor, James Fowler, My- MethodsinNaturalLanguageProcessing(EMNLP).
ron Gutmann, and 1 others. 2009. Computational
socialscience. Science,323(5915):721–723. JasonWei,XuezhiWang,DaleSchuurmans,Maarten
Bosma,FeiXia,EdChi,QuocVLe,DennyZhou,
Guohao Li, Hasan Hammoud, Hani Itani, Dmitrii and1others.2022. Chain-of-thoughtpromptingelic-
Khizbullin, and Bernard Ghanem. 2023. Camel: its reasoning in large language models. Advances
Communicative agents for “mind” exploration of inneuralinformationprocessingsystems,35:24824–
largelanguagemodelsociety. AdvancesinNeural 24837.
InformationProcessingSystems,36:51991–52008.
U Wilensky. 2015. An Introduction to Agent-Based
JanMalteLichtenberg,AlexanderBuchholz,andPola Modeling:ModelingNatural,Social,andEngineered
Schwöbel.2024. Largelanguagemodelsasrecom- ComplexSystemswithNetlogo. TheMITPress.
mendersystems: Astudyofpopularitybias. arXiv
preprintarXiv:2406.01285. FengXia,JinzhongWang,XiangjieKong,ZhiboWang,
JianxinLi, andChengfeiLiu.2018. Exploringhu-
Jesús López Baeza, José Carpio-Pinedo, Julia Siev- manmobilitypatternsinurbanscenarios: Atrajec-
ert, André Landwehr, Philipp Preuner, Katharina torydataperspective. IEEECommunicationsMaga-
Borgmann, Maša Avakumovic´, Aleksandra Weiss- zine,56(3):142–149.
bach,JürgenBruns-Berentelg,andJörgRainerNoen-
nig.2021. Modelingpedestrianflows: Agent-based XiaotongYe,NicolasBougie,ToshihikoYamasaki,and
simulations of pedestrian activity for land use dis- NarimasaWatanabe.2025. Mobilecity: Anefficient
tributions in urban developments. Sustainability, frameworkforlarge-scaleurbanbehaviorsimulation.
13(16). arXivpreprintarXiv:2504.16946.
CharlesMMacalandMichaelJNorth.2005. Tutorial YangbinYu,QinZhang,JunyouLi,QiangFu,andDe-
on agent-based modeling and simulation. In Pro- hengYe.2024. Affordablegenerativeagents. CoRR,
ceedingsoftheWinterSimulationConference,2005., abs/2402.02053.
pages14–pp.IEEE.
Stephan Zheng, Alexander Trott, Sunil Srinivasa,
OpenStreetMapcontributors.2025. Openstreetmap. David C Parkes, and Richard Socher. 2022. The
aieconomist: Taxationpolicydesignviatwo-level
JoonSungPark,JosephO’Brien,CarrieJunCai,Mered- deepmultiagentreinforcementlearning. Sciencead-
ithRingelMorris,PercyLiang,andMichaelSBern- vances,8(18):eabk2607.
stein. 2023a. Generative agents: Interactive simu-
lacraofhumanbehavior. InProceedingsofthe36th Wangchunshu Zhou, Yuchen Eleanor Jiang, Long Li,
AnnualACMSymposiumonUserInterfaceSoftware JialongWu,TiannanWang,ShiQiu,JintianZhang,
andTechnology,pages1–22. JingChen,RuipuWu,ShuaiWang,ShidingZhu,Jiyu
Chen,WentaoZhang,NingyuZhang,HuajunChen,
Joon Sung Park, Joseph C. O’Brien, Carrie Jun Cai, PengCui,andMrinmayaSachan.2023. Agents: An
MeredithRingelMorris,PercyLiang,andMichaelS. open-source framework for autonomous language
Bernstein.2023b. Generativeagents:Interactivesim- agents. CoRR,abs/2309.07870.
ulacraofhumanbehavior. InThe36thAnnualSym-
posiumonUserInterfaceSoftwareandTechnology
(UIST),pages2:1–2:22.
Joon Sung Park, Carolyn Q. Zou, Aaron Shaw, Ben-
jamin Mako Hill, Carrie J. Cai, Meredith Ringel
Morris, Robb Willer, Percy Liang, and Michael S.
Bernstein. 2024. Generative agent simulations of
1,000people. CoRR,abs/2411.10109.
JinghuaPiao,YuweiYan,JunZhang,NianLi,Junbo
Yan,XiaochongLan,ZhihongLu,ZhihengZheng,
JingYiWang,DiZhou,and1others.2025. Agentso-
ciety: Large-scalesimulationofllm-drivengenera-
tiveagentsadvancesunderstandingofhumanbehav-
iorsandsociety. arXivpreprintarXiv:2502.08691.
8

Need thresholds for action interruption are
T = 0.3,T = 0.3,T = 0.2,T =
hunger energy safety social
0.2,andpriorityorderishunger>safety>energy
>social. Long-termgoalsarerevisedmonthlyor
aftermajorlifeevents,usinganeedfulfillmentin-
dex(representingtheproportionofthedaywhen
all core needs exceed their thresholds), financial
stress(income<0.9×expenses),andsocialisola-
tion(fewerthan3uniquecontactsin7days)astrig-
gers. Simulationoperateswitha5minutetimestep,
andallrandomseedsarefixedforreproducibility.
Daily schedules are constructed from time
Figure6:OverviewofCitySim:LLM-basedagentswith
diversepersonasplandailyactivities,interactsocially, blockswithaminimumgranularityof5minutes,
andnavigateavirtualcityenvironment. matching the resolution of human routine report-
ingintime-usesurveys. Invalue-drivenplanning,
N = 3candidateactivitiesaregeneratedforeach
A ExperimentalSetup
leisure block, balancing agent diversity and com-
We provide an illustration of CitySim in Figure putational efficiency. During place selection, the
6. All agent attributes in the persona module agentconsidersthetop10nearbyareasandupto
are initialized from a proprietary survey-based 200candidatePOIsbyrelevanceandproximityfor
dataset, conducted in Japan. The attribute distri- each activity. The gravity model uses γ = 2.0 as
butions closely match those observed in recent distance decay, with ε = 10
−3
for stability. Be-
Japanese census statistics and lifestyle surveys lief score considered in the gravity model is the
(Statistics Bureau of Japan, 2021). Big Five per- theaverageoftheagent’sbeliefsaboutthisplace
sonality traits are discretized on a 3-point scale across four dimensions, as recorded in its spatial
(1=low, 2=medium, 3=high). Each agent’s home memory. Fortransport,availablevehiclesinclude
and workplace (or school) locations are assigned walk,bicycle,car,bus,andtrain. Face-to-facein-
accordingtoJapanesepopulationdensity,basedon teractionsarelimitedtoonepartnerper30-minute
OpenStreetMapdata(OpenStreetMapcontributors, ticktoavoidexcessivesocialbehaviors.
2025),ensuringrealisticurbanspatialdistribution At the end of each day, the agent synthesizes
andfeasiblecommutes. higher-level insights regarding its habits, prefer-
Thetemporalmemoryretrievesthetopk = 5 ences, and beliefs through a structured reflection
1
entriesfromthepast∆t = 24hours(cosineembed- process. Specifically,themostrecententriesfrom
theagent’stemporalmemoryarecompiledandpro-
dingsimilarity);eachmemorynodestores{time,
vided to the language model. The initial prompt
location,observation,key}. Reflectivememoryis
instructs the model to identify salient, high-level
synthesizedattheendofeachday,linkingtotempo-
ralevents. Spatialmemorybeliefsb ∈ R4 ({price, questionsthatcanbeansweredusingonlythepro-
i
vided memory records. The questions in our ap-
atmosphere,satisfaction,convenience})areinitial-
izedas0.5(neutral)forunvisitedPOIs,updatedat proachareexplicitlyformulatedtouncoverrecur-
ringpatternsofbehavior(habits),preference,and
eachvisitviaaKalmanfilter,acknowledgingthis
evolvingbeliefs. Foreachgeneratedquestion,rele-
slightabuseofnotationforconvenience:
vantmemoryentriesareretrievedusingsemantic
K(t) =
σ(t
σ
−
b (
1
t
)
−
+
1)
σ
b(
i
t) =K(t)o(
i
t)+(1−K(t) )b(
i
t−1) s
m
im
od
i
e
la
l
r
i
i
s
ty
th
a
e
n
n
d
p
t
r
e
o
m
m
p
p
o
te
r
d
al
to
pr
e
o
x
x
tr
i
a
m
ct
it
u
y
p
. T
to
h
fi
e
v
l
e
an
d
g
is
u
ti
a
n
g
c
e
t
b o insights, eachsupportedbyexplicitreferencesto
σ b
(t) =(1−K(t)
)σ b
(t−1)
the underlying memory entries (e.g., The agent
(2)
prefers evening study sessions (evidence:
(t)
where σ b denotes uncertainties in beliefs, and 8, 13, 22, 45)). Both direct observations and
withσ (0) = 0.25andσ = 0.2,andsubjecttodaily priorreflectivestatementsareeligibletoserveas
b o
decay with λ = 0.03. Beliefs for unvisited POIs evidence, enabling the recursive construction of
areimputedfromthek = 10mostsimilarvisited abstracted self-knowledge. All resulting insights
locationsbasedonembeddingdistances. arestoredinthereflectivememory.
9

Forpairwisehumanpreference,wedefinedthe A.1.2 SocialModule
followingcriterion: (i)Naturalness—theextentto
Beyond maintaining evolving belief vectors over
whichactionsalignwiththeagent’sprofile,habits,
social ties, our social module incorporates struc-
andcontext;(ii)Coherence—thelogicalprogres-
turedreasoningtosupportcontext-sensitivecom-
sion and goal-directedness of activities; and (iii)
munication. Wheninitiatingaconversation,agents
Plausibility—the overall believability of the se-
rely on LLM-generated judgments that consider
quencegivenrealisticurbanbehavior.
notonlyrelationshipstrengthbutalsotheagent’s
intention,emotionalstate,andongoingthoughtpro-
A.1 ModuleDetails
cesses. Messagegenerationissimilarlyguidedby
We now provide a comprehensive explanation of apromptframeworkthatreflectspersonalitytraits,
some modules, detailing the implementation and pastinteractions,andconstraineddiscussiontopics
technicaldetails. derivedfromtheagent’spersona.
Followingeachinteraction,beliefsareupdated
A.1.1 PlanningModule by evaluating the sentiment and outcome of the
exchange: positive,neutral,ornegativesignalsare
Daily planning follows a two-step recursive ap-
extractedfromtheconversationandusedtoincre-
proach:
mentally adjust the affinity, trust, and familiarity
1. Mandatory Block Assignment: Starting
scores between agents. In addition, social inter-
fromanemptyday,theplannerassignsfixed,
actions are not statically scheduled. Instead, un-
non-negotiable activities (e.g., sleep, work,
metsocialneedsdynamicallytriggeracquaintance
medical appointments) using agent persona,
searchandinteractionplanning. Forinstance,when
occupation, and needs. If a selected activity
social satisfaction falls below a threshold, agents
doesnotfilltheentireinterval,theblockmay
proactivelyevaluatewhomtocontactandwhether
besubdividedaccordingtotheactivitydura-
themodeofinteractionshouldbeface-to-faceor
tion.
online. Thisdecisionprocessishandledbyasingle
2. Medium-Priority Recursive Filling: Af-
LLMcall,producingboththemodalityandthetar-
terplanningmandatoryactivities,remaining
getagentinstructuredform. Thesefeaturesenable
[EMPTY]blocksarerecursivelyprocessedfor
theemergenceofdiverse,adaptivesocialpatterns
medium-priority tasks (e.g., meals, hygiene,
acrossagentsovertime.
essentialerrands).
Onemaynoticethatsome[blocks]remainempty.
B Discussion
Following Maslow’s Hierarchy of Needs (Huitt,
2007), those blocks are typically reserved for Weacknowledgethatourmethodexhibitscertain
leisureactivitiesortosatisfylong-termgoals/needs limitations. The collective behaviors generated
(e.g.,hobbies,socializing,exploration). Therefore, by CitySim agents are well-aligned with estab-
theyarefilledatexecutionbasedontheagent’scur- lishedtheoriesinurbanstudiesandcommonlyob-
rentstate,location,dominantneeds,futuresched- servedpatternsincitylife. Micro-levelphenomena,
ule, using a value-driven planning. For each such as individual activity selection, place visits,
emptyinterval,wearguethattheparadigmofpre- androuteplanning,emergefromtheendogenous
sentingmultiplecandidateactivitiesandevaluating decision-making of our agents. However, the un-
them enables the agent to select the best action. derlying reasons for why agents exhibit specific
Thus, we prompt the agent to generate N candi- motivationalandplanningpatternsremainpartially
dates—withmaximumdurationbeingtheblock, unexplainedduetotheinherentblack-boxnature
thatmayimproveenjoyment,satisfaction,orfulfill of large language models. One possible explana-
aneedorgoal. Next,itevaluateseachactivityby tionisthatLLMsencodeknowledgeandbehaviors
imaginingtheresultingdesirestatesthattheagent presentintheirdiversetrainingcorpora,whichin-
would experience after taking action. Based on cludestextualdescriptionsofurbanroutines,spa-
theseevaluations,theagentselectstheactivityat tial preferences, and daily life across global con-
thatisexpectedtobestfulfilltheagent’sintrinsic texts.
desires. Thisschemeisexecutedthroughasingle Afurtherlimitationstemsfromthedependency
structuredLLMcallwithmultipleinternalreason- on sufficient behavioral and interactional data to
ingsteps. constructdetailedandfaithfulagentpersonas. In
10

somecases,real-worlddatamaybelimited,particu- #Agents CitySim(mean±SD)[s] AgentSociety(mean±SD)[s]
larlyforcold-startpopulationsormarginalizeduser 103 9.0×10 −3±3.2×10 −5 8.6×10 −3±3.0×10 −5
groupswithfewerobservedinteractions. Thiscon- 104 9.7×10 −3±2.1×10 −5 9.1×10 −3±1.5×10 −5
straintreducestheeffectivenessofmodulessuchas
105 2.1×10 −2±5.0×10 −4 1.8×10 −2±5.7×10 −4
106 0.183±5.6×10 −4 0.168±5.3×10 −4
persona,belief,orlong-termgoalformation,which
rely on rich historical context. To mitigate this, Table2: Meantimepersimulationstep(seconds)and
weinitializeagentpersonasusingadiversesetof standarddeviationasafunctionofagentpopulation.
demographicfeatures(age,occupation,lifestage)
andpersonalitytraitssampledfromempiricaldis-
tributions,butthisremainsanimperfectproxyof
cess, enabling agents to account for micro-scale
geniunehumans.
attractorsandlocalaccessibility(Xiaetal.,2018;
As with any LLM-based simulation, there is a
López Baeza et al., 2021). Moreover, incorporat-
riskthatmodel-drivenagentsinheritbiasespresent
ing adaptive behavioral modules that encourage
inlarge-scaledata,potentiallyleadingtotheunder-
agentstooccasionallyexplorelesspopularareas,
representationoroversimplificationofcertainur-
eitherthroughlearnednovelty-seekingorroutine
bangroupsorbehaviors. Thiscanposechallenges
variation,mayhelpbettercapturethediversityof
whenapplyingsimulationresultstoreal-worldur-
real-worldmovement(Gürcanetal.,2025).
banpolicyorplanning,astheneedsofunderrepre-
sentedgroupsmightbeoverlooked. Toaddressthis, Finally, while CitySim faithfully models daily
ourexperimentsensureabroadspectrumofsimu- routines,beliefformation,andadaptiveplanning,
latedpersonas—encompassingoccupations,age itabstractsawaysomecontextualfactorsthatinflu-
groups,andpersonalityprofiles, andwequantify encereal-worldappraisal,includingweathercondi-
discrepancies between generated and real-world tions,crowding,transportationdelays,oraccessi-
behaviordistributions. Asfuturework,weaimto bilityconstraints. Moreover,someinternalneeds
analyzetherepresentationofminorityandvulnera- likeself-esteemandself-actualizationarenotyet
blegroupsinoursyntheticsociety,andtoextend fully represented, as they are subjective and of-
CitySimtoadditionaldomains(e.g.,health,mobil- ten depend on individual values, goals, and life
ity,foodenvironments). circumstances. Thisintroducesapotentialgapbe-
Some experiments in our paper rely on LLM- tween the richness of real urban interactions and
as-judgeevaluationsusingGPT-4o,whileGPT-4o- our agent-based simulation. Capturing these fac-
minipowerstheagentsthemselves. Althoughthis tors requires more nuanced modeling beyond ob-
circularevaluationapproachmayintroducesignifi- servable behaviors, which presents ongoingchal-
cantbias,asLLMstendtofavorcontentgenerated lengesforsimulationenvironmentslikeCitySim.
in their own style, it remains a common practice
due to the scalability and consistency offered by
automatedevaluations. Nevertheless,weacknowl- B.1 Pseudo-Code
edgethelimitationsinherentinthismethodology,
including the potential for inflated performance Weprovidethepseudo-codeofourmethod.
metricsanddiminishedgeneralizabilitytorealhu-
manjudgment. Tomitigatetheseconcerns,future
Algorithm1: DailySimulationLoop
work should incorporate more diverse evaluation
strategies,includinghumanassessmentsandcross- Foreachday:
modelvalidation. Foreachagent:
plan_day()
While CitySim accurately reproduces major
Foreachtimestep:
crowd patterns in central and highly accessible
perceive()
areas, it tends to underrepresent pedestrian den- action←decide_action()
sity in smaller streets due to the belief-enhanced ifaction.requires_move:
gravitymodel’semphasisonprominentPOIs. To
poi←select_POI()
vehicle←select_vehicle(poi)
mitigatethislimitation,futureworkcouldintegrate
move(poi, vehicle)
additional urban context features—such as land else:
use data, pedestrian infrastructure, or historical execute(action)
reflect() //beliefs,goals,needs,habits,...
mobility traces—into the location selection pro-
11

Method Activity Dialogue Mobility EventReaction
GeAn 3.11±0.18 3.96±0.04 3.08±0.17 3.03±0.21
AGA 3.22±0.28 4.00±0.03 3.16±0.24 3.15±0.19
HumanoidAgent 3.30±0.31 3.99±0.05 3.29±0.22 3.21±0.17
AgentSociety 4.02±0.22 4.08±0.06 3.82±0.25 3.75±0.21
MobileCity 4.09±0.27 4.04±0.06 3.96±0.18 3.89±0.17
CitySim 4.37±0.18 4.23±0.04 4.14±0.15 4.09±0.16
Table 3: Human-likeness score evaluated by GPT-4o
acrosscitysimulationdomains. Highervaluesindicate
greatersimilaritytorealhumanresponses.
C AdditionalExperiments
C.1 PerformanceEvaluation
Figure 7: Evolution of basic needs (hunger, energy,
Toassessthescalabilityandefficiencyofourcity safety,socialsatisfaction)forfiveagentsacrossoneday.
simulationframework,weconductaperformance
3
analysis. We simulate agent populations of 10 ,
reactionscores. Furthermore,ouragent’sexplicit
4 5 6
10 ,10 ,and10 individuals,distributingtheirde-
modelingofneeds,feelings,andlong-termgoals
parturetimesaccordingtotypicalweekdaypeaks.
leadstomoreconsistentandbelievableroutines. In
As done in AgentSociety (Piao et al., 2025), for
contrast,baselineagentsaremorelikelytoproduce
eachagent,wealternatebetweensettingandfetch-
repetitiveactionsorunrealisticschedules—unusu-
ing queries (at a 1:999 ratio) to mimic realistic
allylongbreakfastsorworkstartingatypicallylate,
simulationworkloads. Thesimulationrunsfor24
contributingtosuspicionsofAIinvolvement.
virtualhours,withthemainmetricbeingthemean
simulationsteptimeperagent. Eachsettingisre- C.3 NeedsEvolution
peated five times to obtain average and standard
Toassesstherealismandadaptabilityofouragent-
deviationvalues. Thesimulationspeedresultsare
based planning framework, we simulate the evo-
presentedinTable2. Weobservethat,evenasboth
lutionofbasicneedsacrossatypicaldayforfive
theagentpopulationandqueryfrequencygrowby
agentprofiles: amid-careerofficeworker,ahigh-
severalordersofmagnitude,theaveragetimeper
school student, a night-shift nurse, a freelance
simulation step increases modestly. This demon-
designer, and a retired senior. Figure 7 presents
stratesthatourframeworksupportslarge-scalesim-
the resulting need trajectories, which display dis-
ulations with negligible loss of efficiency, and is
tinct, context-dependent patterns consistent with
well-suitedformodelingcomplexurbanscenarios
real-worldroutines. Theofficeworkerandstudent
withmassiveagentpopulations.
exhibitdipsinhungerandenergyprecedingfollow-
ing periods of sustained activity, with occasional
C.2 HumanLikeliness
snackstorestorehungerduringtheday. Thenight-
AsLLMEvaluators(ChiangandLee,2023)have shiftnurse’strajectoriescaptureirregularsleepand
demonstratedperformanceonparwithhumanan- mealpatternsinherenttoshiftwork,whilethefree-
notators, we leverage GPT-4o to judge whether lancedesignerdemonstratesvariableself-careand
agent behaviors in our simulation appear human flexiblescheduling. Theretiredseniorshowsmore
orLLMgenerated. Foreachbaseline, wecollect regularmealtimes,napping,andconsistentlyhigh
20,000 outputs across four domains: daily activ- socialsatisfactionduetolivingwiththeirfamily.
ities, dialogue, mobility choices, and event reac-
C.4 BeliefEstimation
tions. GPT-4oassesseseachsampleusinga5-point
Likertscale,withhigherscoresindicatingstronger Beliefs are central in shaping human behaviors.
resemblancetohuman-likeresponses. Resultsin To evaluate the accuracy and consistency of our
Table3showthatourmodelsignificantlyoutper- belief estimation, we conduct a study in which
forms all baselines across the evaluated domains. each agent is first initialized with belief vectors
Notably, theintegrationofvalue-drivenplanning from a dataset of visited POIs, then tasked with
and belief-aware mobility contributes to substan- predicting beliefs for a disjoint set of POIs. For
tial improvements in both the mobility and event each test POI, we compute the mean absolute er-
12

Activity Dialogue Mobility EventReaction
Value Value Value Value
CitySim(full) 4.37±0.18 4.23±0.04 4.14±0.15 4.09±0.16
w/oBelief 3.85±0.22 3.92±0.08 3.75±0.18 3.60±0.21
w/oRec.Plan 3.72±0.17 3.85±0.06 3.80±0.17 3.65±0.16
w/oLTGoal 3.80±0.19 3.95±0.07 3.88±0.14 3.70±0.18
w/oNeeds 3.55±0.21 3.82±0.09 3.73±0.16 3.50±0.20
w/oPersona 3.60±0.20 3.60±0.10 3.72±0.17 3.58±0.17
Table4: AblationstudyforCitySim,evaluatedbyGPT-4o. Metricsreflecthuman-likeness(Likert,1-5scale,mean
±std)foractivity,dialogue,mobility,andeventreaction. Medalsdenotetop-3performanceineachdomain.
Figure8: Category-wisemeanabsoluteerror(MAE)ofbeliefestimationforunvisitedPOIs,evaluatedacrossfive
semanticcategories(Restaurants,Parks,Shops,Transport,Entertainment)andtenLLM-basedagentmodels. Lower
valuesindicatehigheraccuracy.
ror (MAE) between the agent’s predicted belief demonstratesthecriticalroleofbeliefsinenabling
andtheground-truthvalue,reportingresultssepa- value-driven,experience-awaredecisions.
ratelyacrossfivesemanticPOIcategories. Figure8 Ablatingrecursiveplanningreducesscoresfur-
presentscategory-wisebeliefestimationerrorfor ther,particularlyinactivityandmobility. Without
allevaluatedmodels. AsshowninFigure8,larger thismechanism,agentsarelesscapableofadapting
modelslikeGPT-4oachievethelowestMAEacross routinestonewinternalorenvironmentalfeedback,
allcategories,followedbyGPT-4ominiandQwen- whichinturndiminishesthecoherenceandflexi-
14B.ToolLLaMAexcelsinTransport andShops, bilityoftheirschedules.
while smaller LLaMA-2 models show higher er- Weobservethatexcludingthelong-termgoal
rors,especiallyforEntertainment. Overall,larger modulehasamorelocalizedimpact,withthemost
LLMsgeneralizebeliefsmoreaccuratelyindiverse noticeabledeclineindialogueandmobility. This
urbancontexts. suggests that long-term, high-level goal manage-
mentprimarilybenefitslife-courseconsistencyand
C.5 AblationStudy contextualcoherenceovermultipledays.
Disablingtheneedsmoduleresultsinthelargest
We conduct a systematic ablation study to assess
drop in both activity and event reaction scores.
thespecificcontributionofeacharchitecturalmod-
Agentswithoutexplicitneedsprioritizationbecome
ule to agent performance. As shown in Table 4,
unabletointerruptorreordertheirplansinresponse
weremovekeycomponents—beliefmodule,re-
tointernalstates,oftenleadingtounrealistic,rigid
cursive daily planning, goal module, needs mod-
behaviorandmissedopportunitiestofulfillbasic
ule,andpersonamodule,fromourfullframework
requirements.
andevaluatetheireffectonhuman-likenessscores
Finally,removingthepersonamodule—thereby
acrossalldomains.
eliminatingdemographicandpsychologicaldiver-
Removingthebeliefmoduleleadstoamarked
sity—causesasharpdecreaseinallmetrics. Agents
dropinperformance,especiallyforactivitiesand
convergetoabland,homogenizedpattern,lacking
event reactions. Agents without beliefs lack the
theindividualizedroutinesandreactionsessential
ability to accumulate or leverage prior expecta-
forhuman-likeness.
tions about places, resulting in less adaptive and
lesscontextuallygroundedplans. Thisexperiment
13
