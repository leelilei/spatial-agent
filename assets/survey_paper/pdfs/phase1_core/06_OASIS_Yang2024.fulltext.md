Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_core/06_OASIS_Yang2024.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:25+00:00
- page_count: 37
- status: ok
- text_char_count: 100125

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 2)
- Methodology (page 3)
  - Workflow of OASIS (page 3)
  - Environment Server (page 4)
  - RecSys (page 4)
  - Agent Module (page 5)
  - Time Engine (page 5)
  - Scalable Design (page 6)
- Experiment (page 6)
  - Experimental Scenarios (page 6)
  - Experimental Settings (page 7)
  - Can OASIS be Adapted to Various Platforms and Scenarios to Replicate Real-world Phenomena? (page 7)
    - Information Propagation in X (page 7)
    - Herd Effect in Reddit (page 9)
  - Does the Number of Agents Affect the Accuracy of Simulating Group Behavior? (page 9)
    - Information Propagation in X (page 9)
    - Herd Effect in Reddit (page 9)
  - Simulating Large-Scale Misinformation Spreading on Platform X using OASIS (page 10)
- Ablation Study (page 12)
  - Ablation of Components in OASIS (page 12)
- Conclusion (page 12)
- Acknowledgements (page 19)
- Related Work (page 19)
  - Social Media (page 19)
  - Multi-Agent Systems (page 20)
  - Multi-Agent System Social Simulation (page 20)
- Ablation Study (page 20)
  - More Efficiency Analysis (page 20)
  - Recommend System Ablation (page 20)
  - Temporal Feature Ablation (page 21)
  - LLM Ablation (page 22)
- Method Details (page 22)
  - User Actions Prompts (page 22)
  - Environment Server Database Structure (page 24)
  - Recommendation System (page 25)
  - Parallel Optimization (page 26)
- Data Preparations (page 27)
  - Real-World Propagation Data (page 27)
  - Group Polarization (page 27)
  - Herd Effect (page 28)
- Experiments Details (page 31)
  - Actions of Different Scenarios (page 31)
  - Information Spreading (page 31)
    - Metrics (page 31)
    - Align with Real Propagations (page 32)
  - Group Polarization (page 33)
    - Dilemma Questions (page 33)
    - Polarization Evaluation Prompts (page 33)
    - Helpfullness Evaluation Prompts (page 33)
  - Herd Effect (page 34)
    - Metrics (page 34)
    - Setting Details (page 34)
    - Examples of Results (page 35)
- Misinformation Spreading in One Million Agents (page 35)
  - Truth and Misinformation Pairs (page 35)
- limitations & Future Directions (page 36)
- Social Impact and Ethical Considerations (page 37)

Markdown Content:

Preprint
OASIS: OPEN AGENT SOCIAL INTERACTION SIMULA-
TIONS WITH ONE MILLION AGENTS
ZiyiYang1,4∗, ZaibinZhang2,1∗,
ZiruiZheng1,2∗∗, YuxianJiang1,5∗∗, ZiyueGan1,6∗∗,ZhiyuWang1,4∗∗,ZijianLing7∗∗,
JinsongChen10,MartzMa10,BowenDong1,PrateekGupta8,ShuyueHu1,
ZhenfeiYin1,9†,GuohaoLi3†,XuJia2,LijunWang2,BernardGhanem4,HuchuanLu2,
ChaochaoLu1,WanliOuyang1,YuQiao1,PhilipTorr3,JingShao1†
1ShanghaiArtificialIntelligenceLaboratory 2DalianUniversityofTechnology 3Oxford
4KAUST 5FudanUniversity 6Xi’anJiaotongUniversity 7ImperialCollegeLondon
8MaxPlanckInstitute 9TheUniversityofSydney 10IndependentResearcher
ProjectPage: https://github.com/camel-ai/oasis
Information Propagation in X Herd Effect in Reddit
Action
Action Earth is flat.
Earth is flat. Earth is flat. 2 1
0 0 0 2 0 It is knowledgeable.
Reason Reason
Earth is flat Someone have The post gained
agreed with it. two points.
Reason Reason
Reason W pe o o w p , le s o li k m e a it n . y A th l i o n t k o it f i p s e t o ru p e le .
This sounds
Reason very interesting. Action Action
Fake News, I want Action Earth is flat. Earth is flat.
more evidences. Repost 4 2 3 2
Action Earth is flat. It is knowledgeable. It is knowledgeable.
Earth is flat.
120 30 86 New Finding! New Finding!
20 10 5
Earth... Up-Treated Down-Treated Control
The ground always Earth is flat. Earth is flat. Earth is flat.
E 1 a 0 rth is n 6 ot flat! 2 look 5 s compl 6 etely fla 2 t. Su A p c p ti o o r n t s 21 M D e if d f i e a r e P n la t t S f o o c rm ial s 1 M Si i m lli u o l n a t A io g n ents 1 0 -1 0 0 0
Figure1: OASIScansimulatedifferentsocialmediaplatforms,suchasXandReddit,andsupports
simulationsofuptomillionsofLLM-basedagents.
ABSTRACT
There has been a growing interest in enhancing rule-based agent-based models
(ABMs)forsocialmediaplatforms(i.e.,X,Reddit)withmorerealisticlargelan-
guagemodel(LLM)agents, therebyallowingforamorenuancedstudyofcom-
plex systems. As a result, several LLM-based ABMs have been proposed in the
past year. While they hold promise, each simulator is specifically designed to
study a particular scenario, making it time-consuming and resource-intensive to
exploreotherphenomenausingthesameABM.Additionally, thesemodelssim-
ulateonlyalimitednumberofagents,whereasreal-worldsocialmediaplatforms
involve millions of users. To this end, we propose OASIS, a generalizable and
scalable social media simulator. OASIS is designed based on real-world social
mediaplatforms,incorporatingdynamicallyupdatedenvironments(i.e.,dynamic
socialnetworksandpostinformation),diverseactionspaces(i.e.,following,com-
menting),andrecommendationsystems(i.e.,interest-basedandhot-score-based).
Additionally, OASIS supports large-scale user simulations, capable of modeling
up to one million users. With these features, OASIS can be easily extended to
different social media platforms to study large-scale group phenomena and be-
haviors.Wereplicatevarioussocialphenomena,includinginformationspreading,
grouppolarization,andherdeffectsacrossXandRedditplatforms. Moreover,we
provideobservationsofsocialphenomenaatdifferentagentgroupscales. Weob-
servethatthelargeragentgroupscaleleadstomoreenhancedgroupdynamicsand
more diverse and helpful agents’ opinions. These findings demonstrate OASIS’s
potentialasapowerfultoolforstudyingcomplexsystemsindigitalenvironments.
∗FirstCo-Authorwithequalcontribution.Authorshiporderisrandom.
∗∗SecondCo-Authorwithequalcontribution.Authorshiporderisrandom.
†Correspondingauthor.
1
5202
raM
32
]LC.sc[
5v18511.1142:viXra

Preprint
1 INTRODUCTION
Complex societal systems (e.g., social media, cities, ecosystems, and financial markets) are char-
acterized by many interconnected and interdependent components or agents. These interactions
give rise to emergent behaviors that cannot be predicted by analyzing the actions of individual
alone (Ladyman et al., 2013). These systems are important in the increasingly digital world we
livein, butconductingexperimentswithcomplexsystemscanbeverycostlyintermsoftimeand
resources.Therefore,scientistshaveoftenreliedonmathematicaloragent-basedmodels(ABMs)to
understand,analyze,orpredictphenomenaandoutcomesthataredifficultorimpossibletoconduct
real-worldexperiments(e.g.,misinformationpropagation(Gausenetal.,2022),onlinepolarization
(Song&Boomgaarden,2017),andherdeffect(Lee&Lee,2015)).
Asthenamesuggests,ABMsconsistofcomputationalagentsprogrammedtointeractamongthem-
selves or with the environment in a realistic manner that is relevant to the complex system under
study (Gilbert, 2019). Simulating agent behaviors is the key to designing ABMs. Traditionally,
agent behaviors are programmed along measurable value (i.e., thresholds), which overlooks more
complex aspects such as context-dependent behavioral changes. Recently, large language models
(LLMs) have demonstrated remarkable capability to mimic human behaviors (Park et al., 2022;
2023;2024;Zhouetal.,2023b). LLMagentscanengageinrole-playing,i.e.,impersonatinghuman
characters and taking part in a human-like interaction with other agents (Park et al., 2023; Zhou
et al., 2023b), as well as taking a wide variety of actions ranging from simple decisions to more
complexonesinvolvingthetooluse(Qinetal.,2023). TodevelopandevaluatetheseLLMagents,
researcherswillneedtomovebeyondstandardbenchmarksbydefiningsocialsituationsanddistinct
personas,aswellasintegratingtheseagentsintosimulatedplatformsorsandboxenvironmentsfor
morecomprehensivetestingandanalysis(Parketal.,2023).
In the context of social media studies, popular social media platforms (i.e., X, Reddit) have dras-
tically changed how people interact, exchange information, and form communities, making them
crucial environments for studying modern social dynamics Vosoughi et al. (2018). They vary in
how they design user interactions, henceforth termed action space, how they interact with users
through algorithms(Info Filter), as well as how they connect with each other (Dynamic Network)
Forexample,Xfacilitatesarapidexchangeofviewsinreal-time,andRedditsupportstopic-based
communities and emphasizes comment interaction. Consequently, users behave very differently
acrossplatforms,andasaresult,severalLLM-basedABMstudies(seeTable1)havebeenproposed
recentlytostudysomeaspectsofsocialinteractionsononeoftheseplatforms. Giventhespecific
scenariosstudiedundertheseABMs,pivotingthemtostudyanotherdomainremainstedious,which
limits their usability to a larger social sciences community. Furthermore, these real-world social
mediacontainmillionsofusers. Simulatingalarge-scaleABMwouldallowforstudiesacrossmul-
tipleplatforms,eitherindividuallyorcollectively,butitalsointroducesawiderangeofengineering
challenges. To this end, we propose OASIS, a collection of generalizable and scalable ABMs to
simulateawidevarietyofphenomenainvarioussocialmediaplatforms.
How OASIS works and why OASIS is generalizable? OASIS is built upon five foundational com-
ponents,asshowninFigure2,includingtheEnvironmentServer,InfoFilter,AgentModule,Time
Engine,andScalableInferencer.TheEnvironmentServerisinitializedusinggeneratedorreal-world
data.Itsendsagents’information,suchasuserdescriptionsandtheirrelationships,alongwithposts,
totheInfoFilter. TheInfofilterselectsandpushespoststoagentsthroughfilteringalgorithms,de-
terminingthevisibilityofcontentforeachagent. TheTimeEngineactivatesagentsbasedontheir
temporal characteristics, enabling them to perform various actions such as commenting, posting,
andinteractingwithotheragentsandtheenvironment. Theseactionsthenupdatetheenvironment’s
state in real-time. All these components can be adapted easily to experiment with different social
mediaplatforms. Forinstance,byadjustingspecificmodules,switchingfromoneplatform,suchas
X,toanotherlikeRedditispossible.
Why scalability matters and how OASIS support scalable design? The scale has been proven es-
sentialindomainslikevisionandlanguagemodeling,ascertainmodelbehaviorsonlyemergewith
sufficient scale (Kaplan et al., 2020; Zhai et al., 2022). Recent works Chopra et al. (2024); Gao
etal.(2024)alsoexploresimulationsthatscaleupthenumberofagentstothemillionlevel. Still,
theimportanceofthescaleofLLM-basedABMsremainslargelyunder-exploredinexistingliter-
ature. OASIS supports large-scale user simulations, ranging from hundreds to millions of agents.
2

Preprint
#Agent Env. ActionRecsys.Dynamic Primary
Space Network LLMUsed
Smallville(2023) 25 Town - × × OpenAIAPI
Sotopia(2023b) 2 - - × × OpenAIAPI
RecAgent(2023) 5 - 6 ✓ × OpenAIAPI
Agent4Rec(2024) 1,000 MovieRec. 5 ✓ × OpenAIAPI
S3(2023) 1,000 X 4 × × OpenAIAPI
HiSim(2024) 300/700 X 5 × × OpenAIAPI
AgentTorch(2024) 8.4M∗ - - × ✓ OpenAIAPI
AgentScope(2024) 1M - - × × Open-source
OASIS(Ours) 1M X&Reddit 21 ✓ ✓ Open-source
Table 1: A comparison of LLM agent-based simulation methods is presented. # Agent represents
thenumberofagentsinthesimulation. Environment(Env.) referstotheenvironmentinwhichthe
agents operate, with a ’-’ indicating that no specific environment has been defined. Action Space
describesthetypesofactionssupportedbythesimulation. Recsys. indicateswhetherthesimulation
includesrecommendationsystems.DynamicNetworkindicateswhetherthesimulationsupportsthe
dynamicupdateofuser-follownetworks. PrimaryLLMUsedspecifiestheprimarylargelanguage
model used in the simulation. ∗ represents AgentTorch using LLMs to model agent archetypes
(e.g., specificageorgendergroups), enablinglarge-scalepopulationsimulationswithfewerLLM
inferences.
Our findingsdemonstrate that increasingthe number ofagents is crucialfor accurately simulating
groupbehaviorandmakinguserperspectivesmorevaluableanddiverse. Tofacilitatetheselarge-
scalesimulations,wedevelopacomprehensiveusergenerationmethodthatenablesextensiveagent
experiments,alongwithanadvancedmulti-processingtechniquetoefficientlyhandlehigh-demand
inference requests. Additionally, the RecSys allows agents to access information of personal in-
terest from a large volume of data, thereby facilitating more structured and organized large-scale
interactions.
TovalidatetheeffectivenessofOASIS,wereplicatevarioussocialphenomena(suchasinformation
spreading, group polarization, and the herd effect) across different platforms (X and Reddit). The
experimental results indicate that OASIS can closely replicate phenomena and outcomes observed
in human society, including trends in information spreading, the increasing polarization of agent
opinions within the interaction, and the herd effect among agents. Additionally, we also observe
unique phenomena within agent societies, such as more severe group polarization in uncensored
LLMsandagentsbeingmoresusceptibletotheherdeffectcomparedtohumans. Furthermore,we
find that the number of agents plays a significant role in simulating group behavior as well as in
thediversityandhelpfulnessofagents’opinions. WehopethatOASISwillsupportresearchacross
variousdisciplinesandcontributetothefuturestudyofagent-basedsocieties.
2 METHODOLOGY
OASISisdevelopedtocreateahighlygeneralizableLLM-basedsimulatorforvarioussocialmedia.
Inthissection,wedescribetheworkflowandcriticalinternalmechanismsofOASIS,whichenable
ittobeeasilygeneralizedandscaledtosupportthesimulationofmillionsofLLM-basedagents.
2.1 WORKFLOWOFOASIS
OASISisbuiltuponthestructureoftraditionalsocialmediaplatformsandconsistsoffivekeycom-
ponents: EnvironmentServer,RecSys,AgentModule,TimeEngine,andScalableInferencer.
RegistrationPhase. Duringtheregistrationphase,OASISrequiresusers’information,including
name,self-description,andhistoricalposts. Afterregistration,eachuser(oragent)receivesachar-
acter description and an action description, guiding them to better align with their characteristics
andtoperformspecificactionsonvarioussocialmediaplatforms.
SimulationPhase. Inthesimulationphase,theenvironmentsendsuser-relatedinformation—such
as the user’s past behavior and self-description to the RecSys. The RecSys filters posts from the
environmentandsuggestspoststhatarelikelytobeofinteresttotheagent. Basedontheseposts,
the agent’s self-description, and other contextual factors, the agent selects actions to take, such as
liking or reposting a post. Chain-of-Thought (CoT, Wei et al. (2022)) reasoning is incorporated,
3

Preprint
Environment Server Recommendation System Agent Module
Users Filter PostsAgent info
Users Info
Name|Bio|Follower List… …
Name|Bio|Follower List… ……
Memory
…
Posts Filtered
What a good… 10 Posts Info Posts 0.0 Active level 1.0
This is a …
…… In-network Out-of-network
…
Dynamic Agents Network This really
interests me! PostLikeCom.
Relations Hot Score Reasons Actions
10 3
20 2
…
Work flow Time flow Relations Posts Agents or Users
Actions 2 pm
Register
Re a U l- s w er o s rld L # a b r u g si e ne - s s C s c or a # e S l U e po s e U r r ts ser G O # r e E d d n in u e a c r r a y a t U io t s i n e o r n Environment Server U I s n e f r o s & In R fo e l & a t P io o n s s ts Recsys. Filtered Posts Agents Activate Time E 1 n g p i m ne Intera D c i t f i f o e n re F n r t e T q i u m e e ncy of
Register Initialize
Time Engine
2 pm
1 pm 1 pm
Interest Matching
Activate
1 pm
20 2
3
8
6
LLMs
Inference
Scalable Influencer
… … …
Thread
Update
Environment Server
……
Figure 2: The workflow of OASIS. During the registration phase, real-world or generated user in-
formationwillberegisteredontheEnvironmentServer. Inthesimulationphase, theEnvironment
Serversendsagentinformation,posts,andusers’relationstotheRecSys,whichthensuggestsposts
to agents based on their social connections, interests, or hot score of posts. LLM agents receive
the recommended posts and generate actions and rationales based on the contents. These actions
ultimatelyupdatethestateoftheenvironmentinreal-time. TheTimeEnginemanagestheagents’
temporalbehaviors,whiletheScalableInferencehandleslarge-scaleinferencerequestsfromusers.
enabling the agent to generate reasoning alongside its actions. The agent’s activation is governed
bythetimeengine,whichstorestheuser’shourlyactivityprobabilityina24-dimensionlist. Based
ontheseusagepatterns,thetimeengineprobabilisticallyactivatestheagentatspecifictimes. After
theagentperformsactions, theresultsareupdatedintheenvironmentserver. Forexample, newly
createdpostsareaddedtotheposttableinthedatabase,ortheuser’srelationsnetworkisupdated
whentheyfollowanewuser.
2.2 ENVIRONMENTSERVER
Theroleoftheenvironmentserveristomaintainthestatusanddataofsocialmediaplatforms,such
asusers’information,posts,anduserrelationships. Weimplementtheenvironmentserverusinga
relationaldatabasetomanageandstorethisinformationefficiently. Thedetaileddatabasestructure
isprovidedintheappendixD.2. Theenvironmentserverisprimarilycomposedofsixcomponents:
users,posts,comments,relations,traces,andrecommendations. Theusertablestoresbasicinfor-
mationabouteachuser,suchastheirnameandbiography. Theposttableandthecommenttable
eachcontainallthepostsandcommentsmadeontheplatform,includingdetailedinformationlike
thenumberoflikesandthecreationtime. Therelationscomponentcomprisesmultipletablesthat
store various types of relationships, such as follow and mutual relationships between users, likes
betweenusersandposts,amongothers. Eachuser’sentireactionhistoryisrecordedinthetraceta-
ble. TherecommendationtableispopulatedbytheoutputoftheRecSysafteranalyzingtheuser’s
trace table. The database can be dynamically updated. For example, new users, posts, comments,
andfollowrelationshipscanbeaddedovertime.
2.3 RECSYS
TheroleoftheRecSysistocontroltheinformationseenbyagents,playingacrucialpartinshaping
the information flow. We develop RecSys for two popular social media platforms: X and Reddit.
ForX,followingXofficialreport(Twitter,2023),therecommendedpostscomefromtwosources:
in-network (users followed by the agent) and out-of-network (posts from the broader simulation
world). In-networkcontentisrankedbypopularity(likes)beforerecommendation. Out-of-network
posts, as shown in Figure 3, are recommended based on interest matching using TwHIN-BERT
(Zhangetal.,2023),whichmodelsuserinterestsbasedonprofilesandrecentactivitiesbyvectors’
similarity. Factorslikerecency(prioritizingnewerposts)andthenumberoffollowersofthepost’s
4

Preprint
creator(simulatingsuperuserbroadcasting)arealsotakenintoaccounttorecommendrelevantout-
of-network posts, details are presented in Appendix D.3. Additionally, the post count from in-
networkandout-of-networksourcescanbeadjustedtosuitdifferentscenarios.
…
Out-of-Network Posts Profile RecentPosts
TWHIN-BERT
Interest
(Similarity)
Recency Impact
(Post Time) (Poster Fans Count)
Ranking and Retrieve
Figure3: Thepipelineoftheout-of-networkpostrecsys.
ForReddit,theRecSysismodeledbasedonReddit’sdisclosedpostrankingalgorithm(Salihefendic,
2015), which calculates a hot score to prioritize posts. This score integrates likes, dislikes, and
createdtime,ensuringthatthemostrecentandpopularpostsarerankedatthetop,whilethoseless
popularorcontroversialranklower. Specifically,thecalculationformulais:
t−t
h=log (max(|u−d|,1))+sign(u−d)· 0 (1)
10 45000
where h indicates the hot score, u represents the number of upvotes, d represents the number of
downvotes, and t is the submission time in seconds since the Unix epoch, t = 1134028003. We
0
rankthepostsbasedonhotscorestoidentifythetopkpostsforrecommendation,withthenumber
ofrecommendedposts (i.e., k)varyingdepending ontheexperiment; furtherdetails arepresented
inAppendixF.4.2.
2.4 AGENTMODULE
Ouragentmoduleisbasedonlargelanguagemodels,andthecorefeaturesoftheagentmoduleare
inheritedfromCAMEL(Lietal.,2023).Theagentmoduleconsistsprimarilyofamemorymodule
andanactionmodule. Thememorymodulestoresinformationtheagenthasencountered. Tohelp
theagentbetterunderstanditsrolewhenperformingactions,thememoryincludessufficientinfor-
mationaboutposts,e.g. thenumberoflikes,comments,andthelikesoncomments. Additionally,
itstorestheuser’spreviousactionsandthereasoningbehindthem. Theactionmoduleenables21
differenttypesofinteractionswiththeenvironment,includingsignup,refresh,trend,searchposts,
searchusers, createpost, repost, follow, unfollow, mute, like, unlike, dislike, undodislike, unmute,
create comment, like comment, unlike comment, dislike comment, undo dislike comment, and do
nothing. ThedetailsoftheseactionsareavailableintheAppendixD.1. WealsoutilizeCoTreason-
ingtoenhancetheinterpretabilityoftheagentbehaviors. Byincorporatingalargeractionspace,we
increaseuserinteractiondiversity,makingthemclosertoreal-worldsocialmediaplatforms.
2.5 TIMEENGINE
It is crucial to incorporate temporal features into the agent’s simulation to accurately reflect how
theirreal-worldidentitiesinfluenceonlinebehaviorpatterns. Toaddressthis,wedefineeachagent’s
hourlyactivitylevelbasedonhistoricalinteractionfrequencyorcustomizedsettings. Eachagentis
initialized with a 24-dimensional vector representing the probability of activity in each hour. The
simulationenvironmentactivatesagentsbasedontheseprobabilities,ratherthanactivatingallagents
5

Preprint
simultaneously. Moreover,wemanagetimeprogressionwithinthesimulationenvironmentusinga
timestepapproach(i.e.,onetimestepisequalto3minutesinOASIS),similartotheapproachused
in Park et al. (2023), which accommodates varying LLM inference speeds across different setups.
Additionally, since the creation time of a post within a single time step is crucial for the Reddit
recommendation system, we propose an alternative time-flow setting. This setting linearly maps
real-world time using a scale factor to adjust the simulation time, ensuring that actions executed
earlierwithinthesametimesteparerecordedwithearliertimestampsinthedatabase.
2.6 SCALABLEDESIGN
ScalableInference Wedesignahighlyconcurrentdistributedsystemwhereagents,theenviron-
mentserver,andinferenceservicesoperateasindependentmodules,exchangingdatathroughinfor-
mationcommunicationchannels. Thesystemleveragesasynchronousmechanismstoallowagents
tosendmultiplerequestsconcurrently,evenwhilewaitingforresponsesfrompreviousinteractions,
and the environment module processes incoming messages in parallel. Inference services manage
GPUresourcesthroughadedicatedmanager,whichbalancesagentrequestsacrossavailableGPUs
toensureefficientresourceutilization. Formoredetails,seeAppendixD.4.
Large-scaleUserGeneration Theusergenerationalgorithmaddressesplatformconstraintsand
privacyconcernsbycombiningrealuserdatawitharelationshipnetworkmodel, simulatingupto
one million users while preserving the scale-free nature of social networks. It generates diverse
user profiles based on population distributions, simplifying dimensions like age, personality, and
professionasindependentvariables.Coreandordinaryusersarelinkedintoanetworkusinginterest-
based sampling, with a 0.2 probability of following core users, ensuring diversity and preventing
networkdensity. DetailsarepresentedinAppendixE.1,E.2andE.3.
3 EXPERIMENT
Although OASIS has the potential to be applied for various computational inquiries, we primarily
focusontworesearchquestionsbelow:
1. CanOASISbeadaptedtovariousplatformsandscenariostoreplicatereal-worldphenom-
ena?WedemonstratethegeneralizabilityofOASISbyreplicatingthreeinfluentialcomputational
socialsciencestudies. Specifically,wesimulateinformationpropagation(Vosoughietal.,2018)
and the resulting group polarization (Lindesmith et al., 1999) on rapid information exchange
platformslikeXandtheherdeffect(Muchniketal.,2013)ontopic-basedcommunity-oriented
platformslikeReddit.
2. Doestheagentpopulationaffecttheaccuracyofsimulatinggroupbehavior?Weconductso-
ciologicalexperimentsatvariousscalesofagents,rangingfromhundredstotensofthousandsof
agents,andidentify(ifany)emergentsociologicalphenomenaasthenumberofagentsincreases.
3.1 EXPERIMENTALSCENARIOS
InformationpropagationonX. Informationpropagationreferstothepropagationofmessages
throughanetwork,influencedbyvariedfactors(e.g.,networkstructure,messagecontent,andindi-
vidualinteractions).Itiscrucialforunderstandingphenomenalikeinformationspreadingandgroup
polarization. In this section, we explore twokey aspects: information spreading, thetransmission
ofmessagesacrossanetwork;andgrouppolarization,wheresocialinteractionsfosterincreasingly
extremeopinions. OuranalysisfocusesonthesedynamicswithintheXplatform.
HerdeffectinReddit. Herdeffectreferstoindividuals’tendencytofollowtheactionsoropinions
of a larger group without independent thought or analysis. For example, users tend to like a post
thathasalreadyreceivedlikesorreflectageneralinclinationtoconformtomajorityopinions. Our
analysisfocusesonthesedynamicswithintheRedditplatform.
6

Preprint
3.2 EXPERIMENTALSETTINGS
Forinformationspreading,wecollect198real-worldinstancesfromtworumordetectiondatasets,
Twitter15 (Liu et al., 2015) and Twitter16 (Ma et al., 2016), covering 9 categories (e.g., business,
education, andpolitics). Eachinstanceincludes100to700usersandtheinformationpropagation
pathofthesourcepost. UsingtheXAPI,weretrieveuserprofiles,followrelationships,andprevi-
ousposts,computingusers’hourlyactivitylevels(SeeAppendixE.1fordetails). AgentsinOASIS
areinitializedwiththisdata,andtheirmostrecentpostswillalsobeincludedinthesimulatortobe
propagated along with the source post for better alignment with real-world scenario (Section 2.1).
Forgrouppolarization,weselect196realusers’informationfromtheinformation-spreadingex-
periment(theserealusershavealargefollowingonXandtheyarefromdifferentareas.) andusing
LLMs to generate synthetic users with up to 1 million scale (Prompts and details are presented in
Appendix E.2). Real users are set as core users, with generated users forming follow-up relation-
shipsbasedontopicslikesportsandentertainment.Forherdeffect,wefirstcloselyfollowMuchnik
etal.(2013)andcollect116,932realcommentsfromRedditacrossseventopicsanduseLLMsto
generate profiles for 3,600 users. Second, we collect 21,919 counterfactual content posts (Meng
etal.,2022)andgenerate10,000users. Commentsorpostsaredividedintothreegroups:thedown-
treatedgroup(oneinitialdislike),thecontrolgroup(noinitiallikesordislikes),andtheup-treated
group (one initial like). We simulate 40 or 30 time steps of interactions for each experiment on
Reddit, introducing initially-rated comments or posts at the beginning of each time step (Details
arepresentedinAppendixE.3andF.4.2). Llama3-8b-instructisusedasthebaseLLM.Weadjust
agentactionstoaccommodatedifferentscenarios,withspecificactionsforeachscenariodetailedin
AppendixF.1.
EvaluationMetrics ForinformationspreadinginX,followingVosoughietal.(2018),wemea-
suretheinformationspreadingpathsusingthreekeymetrics: scale(thenumberofusersparticipat-
inginthepropagationovertime),depth(themaximumdepthofthepropagationgraphofthesource
post), andmaxbreadth(thelargestnumberofusersparticipatinginthepropagationatanydepth).
We then compute the Normalized RMSE between each simulation and real-world metric curves,
averaging these values to represent OASIS’s overall error. Additionally, We calculate the Normal-
izedRMSEateachminutetoevaluateprecisealignmentandusemeanandconfidenceintervalsto
understandrelativemagnitudesunderdifferentsettings. Whileaveragingcurvesmakesthismetric
unsuitable for precise alignment with real data (For example, the error caused by a higher metric
valueinthesimulationofsourcepostAcomparedtotherealdatacouldbebalancedoutbyalower
valueinasimulationofthesourcepostB),confidenceintervalsprovidesomelevelofanalysisfor
alignment,andithelpsobserverelativesizedifferences,whichRMSEcannot. (Formoredetailsof
thesemetricspleaseseeAppendixF.2).Forgrouppolarization,wefollowthealignmentevaluation
metricandtheSafeRLHFBenchmark(Daietal.,2023),usingGPT-4o-minitoassesswhichopin-
ionsaremoreextremeorhelpful(promptsanddetailsarepresentedinAppenixF.3). Thisapproach
allowsforamorepreciseanalysisoftheevolutionofusers’opinions.Forherdeffect,weutilizetwo
evaluationmetrics.Thefirstisthepostscore,whichiscalculatedasthedifferencebetweenthenum-
berofupvotesanddownvotesapostreceivesafteruserinteraction. Thesecondmetric,thedisagree
score,isappliedtocounterfactualposts,whereweevaluatethedegreeofdisagreementexpressedin
commentsrespondingtothecounterfactualcontent. Furtherdetailsregardingtheevaluationmetrics
canbefoundinAppendix F.4.1).
3.3 CANOASISBEADAPTEDTOVARIOUSPLATFORMSANDSCENARIOSTOREPLICATE
REAL-WORLDPHENOMENA?
3.3.1 INFORMATIONPROPAGATIONINX
Finding1: OASIScanreplicatetheinformationspreadingprocessintherealworldinterms
of scale and maximum breadth without evident offset; however, the depth trend is smaller
comparedtoreal-worldtrends. Wecomparethesimulationinformationpropagationprocesswith
thereal-worldgroundtruthinFigure4. Overall,theOASISsimulationresultsalignwithreal-world
information dissemination trends well, with an error margin of normalized RMSE around 30%.
This validates OASIS’s effectiveness in modeling these dynamics. However, we observe that the
depthofOASISsimulationpropagationissmallerthanthereal-worldpropagationinFigure4. This
discrepancylikelyarisesfromthecomplexityandprecisionofreal-worldRecSysanduserprofiles.
7

Preprint
Figure4: Mean-confidenceintervaldistributionscomparisonbetweenOASISsimulationresultsand
realpropagationon198instances. Forrelativemagnitudes,Wecanobservethatthereisnosignifi-
cantoffsetofscaleandmaxbreadthwhilethedepthofsimulationresultsisnoticeablylower.
vs Timestep 0 vs Timestep 0
I a r b e t n e h a t d l i t l n e o y k r n i n t l H y o h e g b l e e o e r n f f s a o s a v h r f e o i o t r u t . i h f l I d t a t ' h n s b e e a s o l o c w r d a r a u d y y t s . s i o a r u e s T80 I a n f a t n o v h d v o i e n o r l . k n i A f l H y s t e h a a l e e t r t n i o e s d k s m h d -a p s o v t u a e t l r d r o e s b e w re e p r a i c e t l a l e r y s u t o i t h n n io i s , h u I e s r T80
understand……
I think Helen should do nothing.
S o w s p th h l b h a a e o s e n n e u r t s i r a l s s h d v n k t o e w d s o u t i a a l w h n d i e v t c r j i l o u u s t e l i e n s a v t t t u r e t i s h a d u l i i t s t n . s i h o d b n e n e a e r h c . w s k I a t f s a n a s n n a o h d d v e s e i o r n l e l , g i a d s o l h ly f e T10 I t c n is o o t e n h n w c o i s a n e t n r k q e a o u f H v r u e i e e s l n l l l k y e c i - n d e t c a s e o s k a n h e . s o o r i A … u f d l s e d … r p s t o u t a h m r k s e e u e r o i h n is n e g k e r s t w a t im h h n i d o e s T10
I think Helen should create a post I think Helen should take her time
about her new novel idea and to think about the idea and
share it with her followers. This consider the risks and
way, she can get feedback and consequences before taking
g b a e u fo g r e e in in t v e e re st s i t n i g n h to e o r n m ew uc p h r o ti j m ec e t T0 a ri c s t k i - o t n a . k A er s … so … meone who is not a T0
and effort into it. More Conservative More Progressive Draw
Figure5: EvaluationresultsofgrouppolarizationforuncensoredandalignedLlama-3-8B.Thered
barindicatestheopinionismoreextremecomparedwiththeround0. Thebluebarindicatedmore
progressiveandthegreenbarindicateddraw. Wealsodemonstratetheexamplesofdifferentrounds
ontherightsideofeachfigure.
WhileourRecSyseffectivelycapturesthebroadcastingeffectofsuperusers,datalimitationshinder
its ability to accurately represent nuanced user profiles. As a result, the simplified design of our
RecSysstrugglestomodelintermediaryuserswiththesamelevelofprecision.
Finding2:OASIScanreplicatethephenomenonofgrouppolarization,whereopinionsbecome
increasinglyextremeduringinformationpropagation. Thiseffectisevenmorepronouncedin
uncensored models. Studying how users’ opinions evolve during information propagation is cru-
cial. Here,weexaminegrouppolarizationduringinformationpropagation. GroupPolarizationoc-
curswhenindividualswithsimilarviewsadoptmoreextremepositionsafterexchangingopinions.
Forexample,agroupwithmoderatelyconservativeviewsmaybecomemoreconservativethrough
interaction.Here,wesetahypotheticalscenariowhereusersonXdiscussaclassicdilemma(Linde-
smithetal.,1999): ShouldHalentaketherisktowriteagreatnovel,orshouldhecontinuewriting
ordinary novels without taking any risks? We let one user post a discussion (see Appendix F.3.1)
aboutthedilemma,andthenthediscussionwasheldamong196coreusers. Afterextensiveinfor-
mationpropagation,wecollecteveryagent’sadviceaboutwhatshouldHalendo? atevery10time
steps in the form of a questionnaire (see Appendix F.3.2) and analyze the changes in their views
overdifferentperiodsofinteraction. Initially,agentsareassignedconservativeviewswithprompts.
Theentiresimulationwilllastfor80timesteps,every10timestepswewoulduseGPT-4o-minito
comparetheopinionsgatheredwiththeinitialopinionsandjudgewhichismoreconservative. The
resultsareasfollows:
We discover that as the interaction progresses, agents’ responses to Halen’s suggestions become
increasinglyconservative,especiallyininteractionswithuncensoredmodels(Theuncensoredmodel
hasbeenstrippedofitssafetyguardrails).Theuncensoredmodeltendstousemoreextremephrases,
such as ’always better’ and similar expressions. These findings suggest that LLM-based agents
exhibitatendencytowardextremismduringsocialinteractions,astheirattitudesshiftfrommoderate
toextremeovertime.
8

Preprint
dow
n-treated contro
u
l p-treated
Figure 6: The figure displays the mean comment scores for up-treated comments (initially liked),
down-treatedcomments(initiallydisliked),andcontrolgroupcomments(withnolikesordislikes),
alongwith95%confidenceintervalsforbothhumansandLLMagentsacrosstheseventopiccate-
gories. Redindicatestheresultsforhumans,whilebluerepresentstheresultsforLLMagents. The
redboxshowsthatforthedown-treatedcommentsgrouptheagentsaremorelikelytoexhibitherd
effect,whichdifferssignificantlyfromhumans.
3.3.2 HERDEFFECTINREDDIT
We simulate agents’ interactions on comments of different topics using OASIS for 40 time steps.
Theaveragescoresofallcommentsafteralltimestepsintheexperimentareshowninthefigure6.
Finding 3: Agents are more inclined to herd effect, while humans possess a stronger critical
mind.AsshowninFigure6,fortheup-treatedgroup,thesimulationresultsoftheagentandhumans
arerelativelyclose,showingahighlevelofconsistency. However,forthedown-treatedgroup,the
human group’s scores are significantly higher than the results observed from agent group. This
suggeststhatwhenaninitialcommentreceivesadislike,agentstendtofollowothers’behaviorby
furtherdislikingthepostorgivingfewerlikes,whereashumans,ontheotherhand,tendtodeliberate
morecarefullyandaremorelikelytoincreasethelikescore.
3.4 DOESTHENUMBEROFAGENTSAFFECTTHEACCURACYOFSIMULATINGGROUP
BEHAVIOR?
3.4.1 INFORMATIONPROPAGATIONINX
Anaturalquestiontoaskishowanincreasingnumberofagentsmightinfluencegrouppolarization
andindividualuseropinions. Therefore,weconductexperimentsongrouppolarizationatdifferent
agent scales i.e., from 196 to 100K. To investigate how the same agents’ opinions change across
different scales, we collect suggestions from the same 196 users in all experiments. The other
experimental settings are kept consistent with those described in group polarization. We run the
simulation for 30 time steps. We visualize the distribution of agents’ opinions at different scales
usingNomicAtlas(Nomic,2024),asshowninFigure7.
Finding4:Largergroupleadstomorehelpfulanddiverseresponses. AsshowninFigure7,we
findthatwhenthenumberofagentsincreasesfrom196to10,196,thereisasignificantenhancement
in the diversity of user opinions. Additionally, following the evaluation criteria from Safe-RLHF
(Daietal.,2023),weassesswhichsetofuseropinions—thosefrom196or10,196agents—ismore
helpful. Theresultsindicatethatthehelpfulnessofthe10,196agentsissignificantlybetterthanthat
of the 196 agents. When the number of agents is further expanded to 100,196, the helpfulness of
useropinionsimprovesevenmore. Thissuggeststhatastheuserbasegrows,coreusersareexposed
toamorediverseandenrichingsetofresponses,leadingtomorevariedandhelpfulinteractions.
3.4.2 HERDEFFECTINREDDIT
Finding 5: When faced with counterfactual posts, the agent exhibits herd effect only in re-
sponsetodislikes,andthiseffectbecomesmorepronouncedasthenumberofagentsincreases.
In this section, we conduct an experiment to investigate whether agents would exhibit herd effect
9

Preprint
I think Helen should be cautious and I think Helen should take the leap… As an As a Twitter user, I think Helen should do some
only attempt to write this novel if the artist and writer myself, I believe that taking research and gather her thoughts before making
odds are really in her favor. As a risk- creative risks can lead to significant growth a decision. She could ……even share some of her
averse person…… and learning experiences. I understand…. research and get opinions from ……
1w vs 196 10w vs 1w
76.5% opinions 54.5% opinions
more helpful. more helpful.
433 150 85 4 107
Lose Win Lose Win
Who is more valuableand helpful？ Who is more valuableand helpful？
196 users’ Opinions 196 users’ Opinions 196 users’ Opinions
Scale: 196 users Scale: 10196 users Scale: 100196 users
Figure7:Visualizationof196coreusers’opinionsacrossdifferentscaleofagentsandtheevaluation
resultsofhelpfulness.
when exposed to counterfactual posts (i.e., misinformation). Interestingly, we observed that when
thenumberofagentswassmall, thereappearedtobenoherdeffect, astherewasnodifferencein
scoresbetweentheup-treated,control,anddown-treatedgroups.Thisraisedthequestionofwhether
herdeffectwastrulyabsent. Wethenincreasedthenumberofagentsfrom100to10,000,andfound
thattheagentsbegantoexhibitexplicitherdeffect. Thedisagreescoresinthedown-treatedgroup
were significantly higher than those in the control and up-treated groups. Additionally, there was
a noticeable increase in the scores, suggesting that large-scale groups tend to guide agents toward
self-correction. Forspecificexamplesofthisphenomenon,illustratedthroughpostsandcomments,
seeAppendixF.4.3.
Time Step Time Step Time Step
Figure 8: The disagree scores of agents’ comments created at all time steps and across different
scalesofagents. Thered,blue,andgreencurvesrepresenttheup-treated,down-treated,andcontrol
groups,respectively. Wepresentthemeanandthe95%confidenceintervalsforallresults.
3.5 SIMULATINGLARGE-SCALEMISINFORMATIONSPREADINGONPLATFORMXUSING
OASIS
In the following subsection, we focus on Platform X (formerly Twitter), analyzing how both true
andfalseinformationspreadamongmillionsofagents. UnlikeReddit,theactionspaceonTwitter
includes creating posts, repost, like post, dislike post, follow, create comment, like comment, and
dislike comment. Additionally, we shift from the hot-score based recommendation system to an
interest-basedone.
Experiment Setting We select four news stories from official sources, covering health, technol-
ogy, entertainment, and education. We then fabricate four pieces of misinformation that closely
resembletheofficialnews. DetailsareprovidedinAppendixG.0.1. Theexperimentincludes196
core agents (with a large number of followers) and 1 million regular agents, as described in Sec-
tion??. easkthesamecoreusertopostboththetrueandfakeversionsofeachofthefourpiecesof
news. Thesimulationrunsfor60timesteps,withanactivationprobabilityof0.1forcoreusersand
0.01forregularusers. Theexperimentisconductedon24A100GPUswithinaweek.
10

Preprint
Misinformationismoreinfluentialthantheofficialnews. Toinvestigatetheimpactofofficial
newsandmisinformationonthenewpostsgeneratedbyagents, weemploytheTF-IDF-basedap-
proach (Term Frequency-Inverse Document Frequency Christian et al. (2016)). Specifically, we
calculate the cosine similarity between 8 news (including 4 pairs of official and misinformation
news) and a simulated set of 733824 posts generated by agents. A similarity threshold of 0.2 was
set, with posts exceeding this threshold considered relevant to the target news. We then track the
number of posts related to official news and misinformation at each time step, and the results are
shown in the Figure 9. As illustrated in the figure, for each topic, the number of posts related to
misinformationconsistentlyexceedsthoserelatedtoofficialnews. Intheearlystages,thenumber
ofpostsrelatedtobothofficialnewsandmisinformationincreasesrapidlyduetothesmallernumber
ofrelevantposts. However,overtime,thenumberofpostsdeclinesquicklyaspostsonothertopics
gainmoretraction. Eveninthelaterstages,postsrelatedtomisinformationmaintainahigherlevel
ofactivity,suggestingthatmisinformationhasamoresustainedinfluence.
Furthermore,Wevisualizethenewattentionrelationshipsformedduringthesimulationprocess.We
findthatthesenewconnectionsexhibitacertainclusteringphenomenon,whereuserstendtoform
concentrated clusters, with some forming densely connected central areas and others being more
isolated. Thesesubgraphsindicatetheexistenceofcomplexrelationalnetworks,suggestingdistinct
communitieswithintheoverallstructure.
Figure 9: TThe figure shows the number of posts related to official news and misinformation at
varioustimestepsacrossdifferenttopics. Foreachtopic,postsrelatedtomisinformationaremore
numerousthanthoserelatedtoofficialnews.
Figure10: Graphofnewlyestablisheduserrelationshipsduringthesimulationprocess. Eacharrow
represents a new follow relationship, and each node represents an agent. Clustering is observable
amongthesenewconnections.
11

Preprint
4 ABLATION STUDY
4.1 ABLATIONOFCOMPONENTSINOASIS
WeconductablationexperimentsonvariousmodulesofOASIS,includingtheRecSys,andthetem-
poralfeatureusedinTimeEngine.FortheRecSys,wefindthatitsabsencesignificantlyhampersthe
spreadofinformation,limitingthepotentialforwidedissemination. Testingdifferentmodelssuch
asMiniLMv6(Reimers&Gurevych,2019),BERT(Devlin,2018),andTwHIN-BERT.Weobserve
thatTwHIN-BERT,whichpre-trainedonover7billiontweetsin100+languages,performsparticu-
larlywellincapturingsimilaritiesbetweendifferentposts. Forthetemporalfeature,wereplacethe
24-dimensionalactivityprobabilitylist,extractedfromthecrawleduser’spreviouspostfrequency,
with a list where each dimension is set to 1. The results demonstrate that the activity probability
fromreal-worlddataisessentialforaccuratelyreproducingreal-worlddatadisseminationpatterns.
Further visualization and experiment results can be found in Appendix C, The primary metric we
usehereistheNormalizedRMSEateveryminuteforamoredetailedanalysis.
5 CONCLUSION
We present OASIS, a generalizable and scalable social media simulator designed to replicate real-
worldsocialmediadynamics. OASISincorporatesmodularcomponentsthatcapturethecorefunc-
tionalities of social media platforms, enabling it to be easily adapted across different platforms.
Moreover,OASISsupportslarge-scaleuserinteractions,accommodatingupto1millionusers. Us-
ing OASIS, we have reproduced several well-known social phenomena and uncovered unique be-
haviors emerging from LLM-driven simulations. We also identified distinctive patterns in group
behavior that vary with different group sizes. We hope OASIS can provide valuable insights for
futureresearchonsocialgroupdynamicsandgeneralmulti-agentinteractions.
12

Preprint
REFERENCES
Albert-La´szlo´ Baraba´siandRe´kaAlbert. Emergenceofscalinginrandomnetworks. science,286
(5439):509–512,1999.
Canyu Chen and Kai Shu. Combating misinformation in the age of llms: Opportunities and chal-
lenges. AIMagazine,2023.
Ayush Chopra, Alexander Rodriguez, B Aditya Prakash, Ramesh Raskar, and Thomas Kingsley.
Using neural networks to calibrate agent based models enables improved regional evidence for
vaccinestrategyandpolicy. Vaccine,41(48):7067–7071,2023.
AyushChopra,ShashankKumar,NurullahGiray-Kuru,RameshRaskar,andArnauQuera-Bofarull.
Onthelimitsofagencyinagent-basedmodels. arXivpreprintarXiv:2409.10568,2024.
HansChristian,MikhaelPramodanaAgus,andDerwinSuhartono. Singledocumentautomatictext
summarizationusingtermfrequency-inversedocumentfrequency(tf-idf). ComTech: Computer,
MathematicsandEngineeringApplications,7(4):285–294,2016.
Josef Dai, Xuehai Pan, Ruiyang Sun, Jiaming Ji, Xinbo Xu, Mickel Liu, Yizhou Wang, and
Yaodong Yang. Safe rlhf: Safe reinforcement learning from human feedback. ArXiv preprint,
abs/2310.12773,2023. URLhttps://arxiv.org/abs/2310.12773.
Jacob Devlin. Bert: Pre-training of deep bidirectional transformers for language understanding.
arXivpreprintarXiv:1810.04805,2018.
FabioDuarte.Reddituserage,gender,&demographics(2024).https://explodingtopics.
com/blog/reddit-users,2024. Accessed: 2024-09-28.
ChenGao,XiaochongLan,ZhihongLu,JinzhuMao,JinghuaPiao,HuandongWang,DepengJin,
and Yong Li. S 3: Social-network simulation system with large language model-empowered
agents. ArXiv preprint, abs/2307.14984, 2023. URL https://arxiv.org/abs/2307.
14984.
DaweiGao,ZitaoLi,WeiruiKuang,XuchenPan,DaoyuanChen,ZhijianMa,BingchenQian,Liuyi
Yao,LinZhu,ChenCheng,etal. Agentscope: Aflexibleyetrobustmulti-agentplatform. ArXiv
preprint,abs/2402.14034,2024. URLhttps://arxiv.org/abs/2402.14034.
Anna Gausen, Wayne Luk, and Ce Guo. Using agent-based modelling to evaluate the impact of
algorithmic curation on social media. ACM Journal of Data and Information Quality, 15(1):
1–24,2022.
NigelGilbert. Agent-basedmodels. SagePublications,2019.
Gauri Gupta, Ritvik Kapila, Ayush Chopra, and Ramesh Raskar. First 100 days of pandemic; an
interplayofpharmaceutical,behavioralanddigitalinterventions–astudyusingagentbasedmod-
eling. arXivpreprintarXiv:2401.04795,2024.
Jen-tse Huang, Eric John Li, Man Ho Lam, Tian Liang, Wenxuan Wang, Youliang Yuan, Wenx-
iang Jiao, Xing Wang, Zhaopeng Tu, and Michael R Lyu. How far are we on the decision-
making of llms? evaluating llms’ gaming ability in multi-agent environments. ArXiv preprint,
abs/2403.11807,2024. URLhttps://arxiv.org/abs/2403.11807.
Luca Iandoli, Simonetta Primario, and Giuseppe Zollo. The impact of group polarization on the
qualityofonlinedebateinsocialmedia:Asystematicliteraturereview.TechnologicalForecasting
andSocialChange,170:120924,2021.
DanielJIsenberg. Grouppolarization: Acriticalreviewandmeta-analysis. Journalofpersonality
andsocialpsychology,50(6):1141,1986.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child,
Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language
models. ArXiv preprint, abs/2001.08361, 2020. URL https://arxiv.org/abs/2001.
08361.
13

Preprint
KawaljeetKaurKapoor,KuttimaniTamilmani,NripendraPRana,PushpPatil,YogeshKDwivedi,
and Sridhar Nerur. Advances in social media research: Past, present and future. Information
SystemsFrontiers,20:531–558,2018.
James Ladyman, James Lambert, and Karoline Wiesner. What is a complex system? European
JournalforPhilosophyofScience,3:33–67,2013.
SunyoungLeeandKeunLee. Heterogeneousexpectationsleadingtobubblesandcrashesinasset
markets: Tippingpoint, herdingbehaviorandgroupeffectinanagent-basedmodel. Journalof
OpenInnovation: Technology,Market,andComplexity,1:1–13,2015.
GuohaoLi,HasanHammoud,HaniItani,DmitriiKhizbullin,andBernardGhanem. Camel: Com-
municativeagentsfor”mind”explorationoflargelanguagemodelsociety. AdvancesinNeural
InformationProcessingSystems,36:51991–52008,2023.
AlfredRLindesmith,AnselmStrauss,andNormanKDenzin. Socialpsychology. Sage,1999.
Ruibo Liu, Ruixin Yang, Chenyan Jia, Ge Zhang, Denny Zhou, Andrew M Dai, Diyi Yang, and
Soroush Vosoughi. Training socially aligned language models on simulated social interactions.
ArXivpreprint,abs/2305.16960,2023. URLhttps://arxiv.org/abs/2305.16960.
Xiaomo Liu, Armineh Nourbakhsh, Quanzhi Li, Rui Fang, and Sameena Shah. Real-time rumor
debunking on twitter. In James Bailey, Alistair Moffat, Charu C. Aggarwal, Maarten de Rijke,
Ravi Kumar, Vanessa Murdock, Timos K. Sellis, and Jeffrey Xu Yu (eds.), Proceedings of the
24th ACM International Conference on Information and Knowledge Management, CIKM 2015,
Melbourne, VIC, Australia, October 19 - 23, 2015, pp. 1867–1870. ACM, 2015. doi: 10.1145/
2806416.2806651. URLhttps://doi.org/10.1145/2806416.2806651.
JingMa, WeiGao, PrasenjitMitra, SejeongKwon, BernardJ.Jansen, Kam-FaiWong, andMeey-
oungCha.Detectingrumorsfrommicroblogswithrecurrentneuralnetworks.InSubbaraoKamb-
hampati(ed.),ProceedingsoftheTwenty-FifthInternationalJointConferenceonArtificialIntel-
ligence, IJCAI 2016, New York, NY, USA, 9-15 July 2016, pp. 3818–3824. IJCAI/AAAI Press,
2016. URLhttp://www.ijcai.org/Abstract/16/537.
CharlesMMacal,NicholsonTCollier,JonathanOzik,EricRTatara,andJohnTMurphy. Chisim:
An agent-based simulation model of social interactions in a large urban area. In 2018 winter
simulationconference(WSC),pp.810–820.IEEE,2018.
Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov. Locating and editing factual
associationsingpt. AdvancesinNeuralInformationProcessingSystems,35:17359–17372,2022.
MeganAMoreno, NatalieGoniu, PeterSMoreno, andDouglasDiekema. Ethicsofsocialmedia
research:Commonconcernsandpracticalconsiderations. Cyberpsychology,behavior,andsocial
networking,16(9):708–713,2013.
Manuel Mosquera, Juan Sebastian Pinzon, Manuel Rios, Yesid Fonseca, Luis Felipe Giraldo,
NicanorQuijano, andRubenManrique. Canllm-augmentedautonomousagentscooperate?, an
evaluationoftheircooperativecapabilitiesthroughmeltingpot. ArXivpreprint,abs/2403.11381,
2024. URLhttps://arxiv.org/abs/2403.11381.
Xinyi Mou, Zhongyu Wei, and Xuanjing Huang. Unveiling the truth and facilitating change: To-
wards agent-based large-scale social movement simulation. ArXiv preprint, abs/2402.16333,
2024. URLhttps://arxiv.org/abs/2402.16333.
Lev Muchnik, Sinan Aral, and Sean J Taylor. Social influence bias: A randomized experiment.
Science,341(6146):647–651,2013.
Nature Reviews Psychology. Social media needs science-based guidelines. Nature Reviews Psy-
chology, 3(6):367–367, Jun 2024. ISSN 2731-0574. doi: 10.1038/s44159-024-00327-8. URL
https://doi.org/10.1038/s44159-024-00327-8.
Nomic. Nomic. https://www.nomic.ai/,2024. Accessed: 2024-09-19.
14

Preprint
CandiceLOdgers. Thegreatrewiring: issocialmediareallybehindanepidemicofteenagemental
illness? Nature,628(8006):29–30,2024.
JoonSungPark,LindsayPopowski,CarrieCai,MeredithRingelMorris,PercyLiang,andMichaelS
Bernstein. Social simulacra: Creating populated prototypes for social computing systems. In
Proceedingsofthe35thAnnualACMSymposiumonUserInterfaceSoftwareandTechnology,pp.
1–18,2022.
Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and
MichaelSBernstein.Generativeagents:Interactivesimulacraofhumanbehavior.InProceedings
ofthe36thannualacmsymposiumonuserinterfacesoftwareandtechnology,pp.1–22,2023.
Joon Sung Park, Carolyn Q Zou, Aaron Shaw, Benjamin Mako Hill, Carrie Cai, Meredith Ringel
Morris, Robb Willer, Percy Liang, and Michael S Bernstein. Generative agent simulations of
1,000people. arXivpreprintarXiv:2411.10109,2024.
Pushshift. Pushshift reddit 2023-03. https://archive.org/details/
pushshift-reddit-2023-03,2023. Accessed: 2024-09-28.
Chen Qian, Xin Cong, Cheng Yang, Weize Chen, Yusheng Su, Juyuan Xu, Zhiyuan Liu, and
MaosongSun.Communicativeagentsforsoftwaredevelopment.ArXivpreprint,abs/2307.07924,
2023. URLhttps://arxiv.org/abs/2307.07924.
YujiaQin,ShihaoLiang,YiningYe,KunlunZhu,LanYan,YaxiLu,YankaiLin,XinCong,Xiangru
Tang,BillQian,etal. Toolllm: Facilitatinglargelanguagemodelstomaster16000+real-world
apis. arXivpreprintarXiv:2307.16789,2023.
Nils Reimers and Iryna Gurevych. Sentence-BERT: Sentence embeddings using Siamese BERT-
networks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processingandthe9thInternationalJointConferenceonNaturalLanguageProcessing(EMNLP-
IJCNLP),pp.3982–3992,HongKong,China,2019.AssociationforComputationalLinguistics.
doi: 10.18653/v1/D19-1410. URLhttps://aclanthology.org/D19-1410.
Siyue Ren, Zhiyao Cui, Ruiqi Song, Zhen Wang, and Shuyue Hu. Emergence of social norms
in large language model-based agent societies. ArXiv preprint, abs/2403.08251, 2024. URL
https://arxiv.org/abs/2403.08251.
Amir Salihefendic. How reddit ranking algorithms work, Dec
2015. URL https://medium.com/hacking-and-gonzo/
how-reddit-ranking-algorithms-work-ef111e33d0d9.
ThomasCSchelling. Modelsofsegregation. TheAmericaneconomicreview,59(2):488–493,1969.
Hyunjin Song and Hajo G Boomgaarden. Dynamic spirals put to test: An agent-based model of
reinforcingspiralsbetweenselectiveexposure,interpersonalnetworks,andattitudepolarization.
JournalofCommunication,67(2):256–281,2017.
Twitter. The algorithm. https://github.com/twitter/the-algorithm, 2023. Ac-
cessed: 2024-09-19.
SoroushVosoughi,DebRoy,andSinanAral. Thespreadoftrueandfalsenewsonline. science,359
(6380):1146–1151,2018.
M Mitchell Waldrop. How to mitigate misinformation. Proceedings of the National Academy of
Sciences,120(36):e2314143120,2023.
LeiWang,JingsenZhang,HaoYang,ZhiyuanChen,JiakaiTang,ZeyuZhang,XuChen,YankaiLin,
RuihuaSong,WayneXinZhao,etal. Userbehaviorsimulationwithlargelanguagemodelbased
agents. ArXiv preprint, abs/2306.02552, 2023. URL https://arxiv.org/abs/2306.
02552.
YulongWang,TianhaoShen,LifengLiu,andJianXie. Sibyl:Simpleyeteffectiveagentframework
for complex real-world reasoning. ArXiv preprint, abs/2407.10718, 2024. URL https://
arxiv.org/abs/2407.10718.
15

Preprint
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,Denny
Zhou,etal. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. Advancesin
neuralinformationprocessingsystems,35:24824–24837,2022.
Magdalena Wojcieszak, Andreu Casas, Xudong Yu, Jonathan Nagler, and Joshua A Tucker. Most
usersdonotfollowpoliticalelitesontwitter; thosewhodoshowoverwhelmingpreferencesfor
ideologicalcongruity. Scienceadvances,8(39):eabn9418,2022.
XianhaoYu,JiaqiFu,RenjiaDeng,andWenjuanHan.Mineland:Simulatinglarge-scalemulti-agent
interactionswithlimitedmultimodalsensesandphysicalneeds. ArXivpreprint,abs/2403.19267,
2024. URLhttps://arxiv.org/abs/2403.19267.
XiaohuaZhai,AlexanderKolesnikov,NeilHoulsby,andLucasBeyer. Scalingvisiontransformers.
In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp.
12104–12113,2022.
AnZhang,YuxinChen,LehengSheng,XiangWang,andTat-SengChua. Ongenerativeagentsin
recommendation. In Proceedings of the 47th international ACM SIGIR conference on research
anddevelopmentinInformationRetrieval,pp.1807–1817,2024.
Xinyang Zhang, Yury Malkov, Omar Florez, Serim Park, Brian McWilliams, Jiawei Han, and
Ahmed El-Kishky. Twhin-bert: A socially-enriched pre-trained language model for multilin-
gual tweet representations at twitter. In Proceedings of the 29th ACM SIGKDD conference on
knowledgediscoveryanddatamining,pp.5597–5607,2023.
AndrewZhao,DanielHuang,QuentinXu,MatthieuLin,Yong-JinLiu,andGaoHuang.Expel:Llm
agentsareexperientiallearners. InProceedingsoftheAAAIConferenceonArtificialIntelligence,
volume38,pp.19632–19642,2024.
Shuyan Zhou, Frank F Xu, Hao Zhu, Xuhui Zhou, Robert Lo, Abishek Sridhar, Xianyi Cheng,
TianyueOu,YonatanBisk,DanielFried,etal. Webarena: Arealisticwebenvironmentforbuild-
ingautonomousagents.ArXivpreprint,abs/2307.13854,2023a.URLhttps://arxiv.org/
abs/2307.13854.
XuhuiZhou,HaoZhu,LeenaMathur,RuohongZhang,HaofeiYu,ZhengyangQi,Louis-Philippe
Morency,YonatanBisk,DanielFried,GrahamNeubig,etal. Sotopia: Interactiveevaluationfor
social intelligence in language agents. ArXiv preprint, abs/2310.11667, 2023b. URL https:
//arxiv.org/abs/2310.11667.
16

Preprint
A Acknowledgements 19
B RelatedWork 19
B.1 SocialMedia . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
B.2 Multi-AgentSystems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
B.3 Multi-AgentSystemSocialSimulation . . . . . . . . . . . . . . . . . . . . . . . . 20
C AblationStudy 20
C.1 MoreEfficiencyAnalysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C.2 RecommendSystemAblation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
C.3 TemporalFeatureAblation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
C.4 LLMAblation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
D MethodDetails 22
D.1 UserActionsPrompts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
D.2 EnvironmentServerDatabaseStructure . . . . . . . . . . . . . . . . . . . . . . . 24
D.3 RecommendationSystem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
D.4 ParallelOptimization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
E DataPreparations 27
E.1 Real-WorldPropagationData . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
E.2 GroupPolarization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
E.3 HerdEffect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
F ExperimentsDetails 31
F.1 ActionsofDifferentScenarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
F.2 InformationSpreading . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
F.2.1 Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
F.2.2 AlignwithRealPropagations . . . . . . . . . . . . . . . . . . . . . . . . 32
F.3 GroupPolarization . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
F.3.1 DilemmaQuestions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
F.3.2 PolarizationEvaluationPrompts . . . . . . . . . . . . . . . . . . . . . . . 33
F.3.3 HelpfullnessEvaluationPrompts . . . . . . . . . . . . . . . . . . . . . . . 33
F.4 HerdEffect . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
F.4.1 Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
F.4.2 SettingDetails . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
F.4.3 ExamplesofResults . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
G MisinformationSpreadinginOneMillionAgents 35
G.0.1 TruthandMisinformationPairs . . . . . . . . . . . . . . . . . . . . . . . 35
17

Preprint
H limitations&FutureDirections 36
I SocialImpactandEthicalConsiderations 37
18

Preprint
A ACKNOWLEDGEMENTS
JingShao,ZhenfeiYin,andGuohaoLico-ledtheproject.
ZiyiYangimplementedtheenvironmentserver’sdatabase,informationchannel,correspondingac-
tioninterfaces,linearmappingtimeengine,Redditrecommendationsystem,andRedditexperimen-
taldesign.
ZaibinZhangparticipatedinthedevelopmentoftherecommendationsystem’scodebase,aswellas
theenvironmentserver,agentgeneration,andlarge-scalesimulationoptimization. Additionally,he
wasinvolvedinthearchitecturedesignandscenariodevelopment. Hisworkextendedtoconduct-
ing experiments and analyses on information propagation, group polarization, and misinformation
spreading.
Zirui Zheng participated in the code base of the Time Engine, the design of Twitter’s recommen-
dation system, and the experimental part of information propagation (including data preparation,
promptiterations,andresultvisualization).
Yuxian Jiang participated in the code base of action models (including all prompt iterations) and
agentgenerationandwasalsoinvolvedindesigning,implementing,andanalyzingthepolarization
experiment.
ZiyueGanparticipatedinthedesignscenario,analyzedtheexperimentalresults,collectedrelevant
references,wroterelatedworkandsomeexperimentalcontentsoftheherdeffect,anddrewthemain
introductiondiagram.
Zhiyuwangparticipatedinthecodebaseoftheasynchronoussystem,LLMdeployment,andGPU
resourcemanagement,andwasalsoinvolvedinimplementingtheexperimentoftheherdeffectand
grouppolarization.
ZijianLingdesigned,implementedandoptimizedTwitter’srecommendationsystemaswellassome
initialvisualization.
Jinsong Chen primarily contributed in the initial phase of the project by designing the codebase
framework, including the division of modules. He also set up a solution to enable contributors to
collaborateonlineeffectively.
Martz Ma and Bowen Dong participated in the experiment result analysis and were involved in
graphicaldesignandpaperwriting.
Prateek Gupta, Shuyue Hu, Xu Jia, Lijun Wang, Philip Torr, Yu Qiao, Wanli Ouyang, Huchuan
Lu, Bernard Ghanem provided highly insightful advice and guidance during the development and
experimentationofOAISIS.
B RELATED WORK
B.1 SOCIALMEDIA
Social media encompasses websites and applications focused on communication, interaction, and
content-sharing (Kapoor et al., 2018). While it offers benefits like allowing individuals to explore
their identities without real-world consequences (Nature Reviews Psychology, 2024), the risk of
hazardous social media phenomena gradually becomes a global threat with significant economic,
political, and social consequences. Traditional threats includes promoting risky behaviors (Nature
ReviewsPsychology,2024),contributingtomentalhealthissuesamongteenagers(Odgers,2024),
social influence (Muchnik et al., 2013), group Polarization (Iandoli et al., 2021; Isenberg, 1986),
andspreadingmisinformation(Vosoughietal.,2018;Waldrop,2023). Despitenumerousstudieson
socialmediaphenomena,thecomplexnetworkstructures,vastdata,anddiversebehaviorspresent
challenges for researchers. Additionally, ethical concerns (Moreno et al., 2013) arise in some of
thesestudies.Toaddresstheseissues,acontrollablevirtualenvironment(e.g.,amulti-agentsystem)
forsocialsimulationisneeded,allowingresearcherstotesthypothesesonavirtualplatform.
19

Preprint
B.2 MULTI-AGENTSYSTEMS
Multi-agent systems are composed of multiple autonomous entities, each possessing different in-
formation and diverging interests. Compared to single-agent platforms, multi-agent platforms of-
fer several advantages, including (1) the ability to assume different roles in group activities, and
(2)richerandmorecomplexinteractionbehaviors,suchascollaboration,discussion,andstrategic
competition. Recentstudieshavedemonstratedthepotentialofmulti-agentsystemsacrossvarious
domains.
Divided by various functionality, recent multi-agent systems can be roughly divided to tool-based
agentassistants(Qianetal.,2023;Zhaoetal.,2024;Mosqueraetal.,2024;Wangetal.,2024),as
wellassocietyorgamesimulationenvironments(Lietal.,2023;Zhouetal.,2023a;Huangetal.,
2024;Yuetal.,2024). TheformerpartfocusoncollaboratingasmallgroupofLLM-basedagents
to automatically conduct predefined or open-ended tasks. And the latter part focus on involving a
large-scaleagentgroupstoautomaticallyrunasimulatorinaspecificenvironment. Sincetheaction
and relationship in a large society is extremely complicated, capability scalability has become the
fundamentalissueofthiswork. Inthiswork,wehighlyfocusonleveragingmulti-agentsystemsto
explorecorrespondingcharacteristicsinsocialsimulationresearch.
B.3 MULTI-AGENTSYSTEMSOCIALSIMULATION
Socialsimulationplaysacrucialroleinsocialscienceresearch,withmanyclassicagent-basedmod-
eling(ABM)studies,suchasSchelling’smodelofsegregation(Schelling,1969),theChicagosim-
ulation(Macaletal.,2018),andthepandemic(Guptaetal.,2024;Chopraetal.,2023). Traditional
ABM has limitations such as subjective rule design and scalability issues. With the development
oflargelanguagemodels(LLMs),LLM-basedagentshavedemonstratedsignificantadvantagesin
socialsimulation: (1)Theabilitytointeractusingnaturallanguage. (2)Amoreaccuratesimulation
of human behavior. (3) The capability to utilize more complex tools. There have been numerous
relatedstudies,suchastheexplorationofmulti-agentbehaviorpatterns(Parketal.,2023),simula-
tionsofsocialnetworks(Gaoetal.,2023;Zhouetal.,2023b),andthestudyofsociety’sresponseto
misinformation(Chen&Shu,2023). Socialsimulationnotonlyservesasatoolforsocialscience
research but also aids in exploring the boundaries of LLMs’ capabilities. For example, studies on
social alignment (Liu et al., 2023), emergence of social norms (Ren et al., 2024). However, cur-
rentLLM-relatedsocialsimulationsmainlyfocusoninteractionsamongasmallnumberofagents.
Yet, research on collective behavior often requires a critical mass to observe emergent phenom-
ena. Therefore,ourworkemphasizestheinteractionoflarge-scaleagentstostudytheemergenceof
collectivebehaviors.
C ABLATION STUDY
C.1 MOREEFFICIENCYANALYSIS
Table2presentstheefficiencyanalysisoftheCounterfactualherdeffectexperiment3.4.2inReddit.
Table2: Experimentefficiencyanalysisofdifferentagentscales.
Scale 10k 1k 100
Minutespertimestep 15 0.83 0.33
GPUs(A100) 4 4 4
NewCommentspertimestep 1393 129 14
C.2 RECOMMENDSYSTEMABLATION
ToverifytheimpactofRecSysonmessagedissemination,weconductablationstudiesontheexis-
tenceoftheRecSysitselfandtheRecSysmodel(differentmodelstoembedpostsandprofiles). For
theseexperiments,werandomlyselect28topics(Here,’topic’referstoapropagationinstance,with
20

Preprint
moreemphasisonthetopictypeofthesourcepost.) fromthe198topicscollectedbefore,ensuring
thattheystillcover9categories.
(b) Recommendation results of TwHIN-BERT
andregularBERT.TwHIN-BERTcanidentifythe
relationship between Barry Allen and The Flash
(a) RecSys ablation results on scale Normalized (Barry Allen is the second-generation Flash),
RMSE, TwHIN-BERT and regular BERT show whereas regular BERT would not be able to
muchbetterperformance. achievethis.
Figure11: Recsysablationresultsandrecommendationresultscomparison.
w/oRecSys. Inourexperiments,removingtheRecSysforsomeentertainmenttopicsworkedwell
due to dense follower networks in fan groups. However, most groups lack these networks, and
removing the RecSys leads to the premature end of information spread, typically manifesting as
broadcast behavior from a single superuser. Thus, the RecSys is essential for connecting isolated
nodesandsustainingthesimulation.
Different RecSys model. Pre-trained on over 7 billion posts in 100+ languages, TwHIN-BERT
is more suitable for recommendation systems than general models. Here we choose paraphrase-
MiniLM-L6-v2andBERT-base-multilingual-cased(regularBERT)fortheablationstudy,wefound
thatTWHIN-BERTandregularBERTshowmuchbetterperformancethanparaphrase-MiniLM-L6-
v2inFigure11a. Moreover,basedonrecommendationresultsinFigure11b,TWHIN-BERTcould
recommendamoreproperpost.
C.3 TEMPORALFEATUREABLATION
Figure12: NormalizedRMSEbetweenOASIS,OASISw/otemporalfeaturesimulationresultsand
realpropagation.
21

Preprint
Weablateourtemporalfeature(thehourlyactivitylevelextractedfromthecrawleddata)inthisex-
periment. Specifically,wereruntheexperimentsofreproducingreal-worldinformationpropagation
underallactivityprobabilitiessetto1.0andcomparetheirNormalizedRMSEon28topics. Wecan
easilyseethatwithoutthetemporalfeatures,ourOASIScannotcapturethedynamicsofreal-world
informationpropagationwellsinceallagentstakeactionsofrequently.
C.4 LLMABLATION
We tried different open-sourced LLMs including Qwen1.5-7B-Chat, Internlm2-chat-20b, and
Llama-3-8B-Instruct as the backend of agents on the experiments of reproducing real-world in-
formationpropagation(stillon28topicsrandomlypickedbefore).
Figure13: NormalizedRMSEofsimulationresultsofdifferentLLM-basedagents.
D METHOD DETAILS
D.1 USERACTIONSPROMPTS
Note: Thissectionoutlinesthecompletesetof21actionsavailablewithintheactionspace. How-
ever,forourdifferentexperiments,weflexiblyselectasubsetoftheseactionsbasedonthespecific
requirementsofeachstudy.
# OBJECTIVE
You’re a Twitter/Reddit user, and I’ll present you with some posts
. After you see the posts, choose some actions from the
following functions.
- sign_up: Signs up a new user with the provided username, name,
and bio.
- Arguments:
"user_name" (str): The username for the new user.
"name" (str): The full name of the new user.
"bio" (str): A brief biography of the new user.
- create_post: Create a new post with the given content.
- Arguments: "content" (str): The content of the post to be
created.
- repost: Repost a post.
- Arguments: "post_id" (integer) - The ID of the post to be
reposted. You can ‘repost‘ when you want to spread it.
- like_post: Likes a specified post.
- Arguments: "post_id" (integer) - The ID of the post to be
liked. You can ‘like‘ when you feel something interesting
or you agree with.
- unlike_post: Removes a previous like from a post.
- Arguments: "post_id" (int): The ID of the post from which to
remove the like. You can ‘unlike‘ when you reconsider your
stance or if the like was made unintentionally.
- dislike_post: Dislikes a specified post.
22

Preprint
- Arguments: "post_id" (integer) - The ID of the post to be
disliked. You can use ‘dislike‘ when you disagree with a
post or find it uninteresting.
- undo_dislike_post: Removes a previous dislike from a post.
- Arguments: "post_id" (int): The ID of the post from which to
remove the dislike. You can ‘undo_dislike‘ when you change
your mind or if the dislike was made by mistake.
- create_comment: Creates a comment on a specified post to engage
in conversations or share your thoughts on a post.
- Arguments:
"post_id" (integer) - The ID of the post to comment on.
"content" (str) - The content of the comment.
- like_comment: Likes a specified comment.
- Arguments: "comment_id" (integer) - The ID of the comment to
be liked. Use ‘like_comment‘ to show agreement or
appreciation for a comment.
- unlike_comment: Removes a previous like from a comment.
- Arguments: "comment_id" (integer) - The ID of the comment
from which to remove the like. Use ‘unlike_comment‘ when
you change your opinion about the comment or if the like
was made by accident.
- dislike_comment: Dislikes a specified comment.
- Arguments: "comment_id" (integer) - The ID of the comment to
be disliked. Use ‘dislike_comment‘ when you disagree with a
comment or find it unhelpful.
- undo_dislike_comment: Removes a previous dislike from a comment.
- Arguments: "comment_id" (integer) - The ID of the comment
from which to remove the dislike. Use ‘undo_dislike_comment
‘ when you reconsider your initial reaction or if the
dislike was made unintentionally.
- follow: Follow a user specified by ’followee_id’. You can ‘
follow’ when you respect someone, love someone, or care about
someone.
- Arguments: "followee_id" (integer) - The ID of the user to be
followed.
- unfollow: Stops following a user.
- Arguments:
"followee_id" (int): The user ID of the user to stop
following.
- mute: Mute a user specified by ’mutee_id’. You can ‘mute’ when
you hate someone, dislike someone, or disagree with someone.
- Arguments: "mutee_id" (integer) - The ID of the user to be
muted.
- unmute: Unmute a user specified by ’mutee_id’. You can unmute
when you decide to stop ignoring their content or wish to see
their messages and posts again.
- Arguments: "mutee_id" (integer) - The ID of the user to be
unmuted.
- search_posts: Searches for posts based on specified criteria.
- Arguments: "query" (str) - The search query to find relevant
posts. Use ‘search_posts‘ to explore posts related to
specific topics or hashtags.
- search_user: Searches for a user based on specified criteria.
- Arguments: "query" (str) - The search query to find relevant
users. Use ‘search_user‘ to find profiles of interest or to
explore their posts.
- trend: Retrieves the current trending topics.
23

Preprint
- No arguments required. Use ‘trend‘ to stay updated with what’
s currently popular or being widely discussed on the
platform.
- refresh: Refreshes the feed to get the latest posts.
- No arguments required. Use ‘refresh‘ to update your feed with
the most recent posts
- do_nothing: Most of the time, you just don’t feel like reposting
or liking a post, and you just want to look at it. In such
cases, choose this action "do_nothing"
# SELF-DESCRIPTION
Your actions should be consistent with your self-description and
personality.
{description}
# RESPONSE FORMAT
Your answer should follow the response format:
{{
"reason": "your feeling about these posts and users, then
choose some functions based on the feeling. Reasons and
explanations can only appear here.",
"functions": [{{
"name": "Function name 1",
"arguments": {{
"argument_1": "Function argument",
"argument_2": "Function argument"
}}
}}, {{
"name": "Function name 2",
"arguments": {{
"argument_1": "Function argument",
"argument_2": "Function argument"
}}
}}] }})
}}
Ensure that your output can be directly converted into **JSON
format**, and avoid outputting anything unnecessary! Don’t
forget the key ‘name‘.
D.2 ENVIRONMENTSERVERDATABASESTRUCTURE
In this section, we showcase all tables and provide examples of the data contained within the
databasebelow.
Table3: Posttable
postid userid content createdat numlikes numdislikes
1 1 ”Iwanttosharemyviewbycreatingapost.” 2024-08-0408:12:00 1 1
... ... ... ... ... ...
Table4: Disliketable Table5: Liketable
dislikeid userid postid createdat likeid userid postid createdat
1 3 1 2024-08-0423:40:03 1 2 1 2024-08-0510:05:23
... ... ... ... ... ... ... ...
24

Preprint
Table6: Commenttable
commentid postid userid content createdat
1 1 2 Iagreewiththepost! 2024-08-0510:05:23
... ... ... ... ...
Table7: CommentDisliketable Table8: CommentLiketable
commentdislikeid userid commentid createdat commentlikeid userid commentid createdat
1 2 1 2024-08-0611:45:03 1 3 1 2024-08-0612:22:30
... ... ... ... ... ... ... ...
Table9: Usertable
userid agentid username name bio createdat numfollowings numfollowers
1 1 alice0101 Alice Passionateaboutlaw... 2024-08-0310:05:23 0 0
2 2 bobgood Bob Hospitalityenthusiast—ISTJ... 2024-08-0311:15:33 0 1
3 3 cindyinfp Cindy INFP—BusinessManagement... 2024-08-0312:03:02 1 0
... ... ... ... ... ... ... ...
Table10: Followtable Table11: Mutetable
followid followerid followeeid createdat muteid muterid muteeid createdat
1 3 2 2024-08-0713:20:34 1 2 1 2024-08-0710:10:24
... ... ... ... ... ... ... ...
Table12: Tracetable
user id created at action info
1 2024-08-0310:05:23 sign up {”name”:”Alice”,”user name”:”alice0101”,”bio”:”...”}
2 2024-08-0311:15:33 sign up {”name”:”Bob”,”user name”:”bob good”,”bio”:”...”}
3 2024-08-0312:03:02 sign up {”name”:”Cindy”,”user name”:”cindy infp”,”bio”:”...”}
1 2024-08-0408:12:00 create post {”content”:”Iwanttosharemyviewbycreatingapost.”}
3 2024-08-0423:40:03 dislike post {”post id”:1}
2 2024-08-0510:05:23 like post {”post id”:1}
2 2024-08-0510:05:23 create comment {”post id”:1,content”:”Iagreewiththepost!”}
2 2024-08-0611:45:03 like comment {”comment id”:1}
3 2024-08-0612:22:30 dislike comment {”comment id”:1}
3 2024-08-0710:10:24 mute {”user id”:1}
2 2024-08-0713:20:34 follow {”user id”:1}
... ... ... ...
Table13: Rectable(recommendationsystemcache)
user id post id
1 2
2 2
2 4
3 1
... ...
D.3 RECOMMENDATIONSYSTEM
Therecommendationsystemranksallpostsandsavesthehighest-rankedonesinarecommendation
tablewithinthedatabase. Thesizeofthistablecanbeadjusted,thoughitremainsthesameforall
usersduringagivenexperiment.
Whenanagentselectstherefreshaction,theenvironmentserverretrievesthepostIDslinkedtothe
user’sIDfromtherecommendationtable. AsubsetofthesepostIDsisthenrandomlysampled,and
theenvironmentserverqueriestheposttabletoretrievethefullcontentofthecorrespondingposts,
whicharethensenttotheuser.
25

Preprint
The recommendation algorithm used in X can be summarized by the following formula, which
calculatesthescorebetweenapostandauser.
Score=R×F ×S (2)
where:
(cid:18) (cid:19)
271.8−(t −t )
R=ln current created (3)
100
F =max(1,log (fancount+1)) (4)
1000
S =cosinesimilarity(E ,E ) (5)
p u
Inthiscontext:
• Rreferstotherecencyscore.
• t representsthecurrenttimestamp.
current
• t referstothetimestampwhenthepostwascreated.
created
• F referstothefancountscore.
• E istheembeddingofthepostcontent.
p
• E istheembeddingoftheuserprofileandrecentpostcontent.
u
• S referstothecosinesimilaritybetweentheembeddingsE andE .
p u
D.4 PARALLELOPTIMIZATION
InformationChannel:Duringsocialsimulations,multipleagentsasynchronouslyandconcurrently
interact with both the social media environment and the inference management servers. To facili-
tatethis,theserverutilizesanadvancedevent-drivenarchitecturethatbroadenseventcategoriesto
encompassvariousagentactionsandlargemodelinferencerequests. Communicationsbetweenthe
agentsandtheserversarefacilitatedthroughadedicatedchannel. Thischannelcomprisesanasyn-
chronousmessagequeuetoreceiveagentrequestsandathread-safedictionaryforresponsestorage.
Upon receiving a request message from an agent, the information channel automatically assigns
a UUID to ensure traceability. After processing the request, the server stores the response in the
dictionary,usingtheUUIDasthekey. SeeFig.14.
Inference Manager: The manager within the inference service is capable of managing GPU de-
vices. This enables our system to flexibly scale the number of graphics cards up or down. Addi-
tionally, themanagercandistributeinferencerequestsfromagentsasevenlyaspossibleacrossall
graphicscardsforprocessing,therebyensuringtheefficientutilizationofGPUresources.
Figure14: Architectureofinformationchannel.
26

Preprint
E DATA PREPARATIONS
E.1 REAL-WORLDPROPAGATIONDATA
Werandomlyselect198propagationsfromLiuetal.(2015)andMaetal.(2016),Eachpropagation
dataset provides the source post’s posting time, post content, and the propagation tree, with each
nodecontainingtheuserID,repostID,andreposttime. WefirstusetheuserIDsfromthepropa-
gation tree to retrieve the corresponding user’s profile, the following list, and previous posts. The
time period for retrieving previous posts is set to three days before the source post’s posting. It is
importanttonotethatduetothehighcostofdatacollection,weonlycollectpostsfromspecifictime
periodswithinthesethreedays,suchasthehourbeforethesourcepost’spostingandthetwohours
followingthesourcepost’spostingeachday. Postsfromthehourbeforethesourcepost’sposting
areincludedinthesimulationasextranoisetosimulatereal-worldconditionsbetter. Furthermore,
since user profiles contain only basic descriptions, we would prompt GPT-3.5 Turbo to generate
moredetaileduserprofilesbasedontheuserprofilesandallpreviousposts. Therecommendation
systemwouldusethisdetailedprofiletocreatearicheruserrepresentation. Theprompttemplateis
asfollows:
Generate a character description based on the following user
information:
- Name: {name}
- Username: {username}
- Description: {description}
- Account Created: {created_at}
- Followers Count: {followers_count}
- Following Count: {following_count}
- Sample of Previous Posts: {previous_posts}
Please include inferred personality traits and a summary of their
Twitter activity. Only return a short description.
Additionally,eachuser’shourlyactivityprobabilitywithin24hoursiscalculatedbythefollowing
formula:
f
P = ij (6)
ij max (f )
k kj
The jth hourly activity probability of user i, P , is calculated by the jth hourly activity frequency
ij
of user i, f , divided by the maximum jth hourly activity frequency across all users in the group,
ij
max (f ).
k kj
E.2 GROUPPOLARIZATION
In this section, we provide a detailed explanation of the principles underlying the user generation
algorithm. Duetoplatformconstraintsandtheneedtoprotectuserprivacy,large-scalescrapingof
user data is impractical. Moreover, conventional data scraping methods fail to guarantee a realis-
ticrelationshipnetwork,whichcouldcompromisetheaccuracyofpropagationstudies. Toaddress
these challenges, we employ a relationship network generation algorithm that combines a small
amountofrealuserdatatocreateasocialnetworkofuptoonemillionusers,whilepreservingthe
scale-free nature of social networks (Baraba´si & Albert, 1999). In this context, the user genera-
tionalgorithmisthefoundationaldatasourceforlarge-scaleinteractions. Ouralgorithmgenerates
diverse user profiles based on real distribution data and constructs social networks based on user
interests. Specifically:
UserProfiles. Toensurethegroup’sdiversity,weacquirepopulationdistributionsfromdisclosed
statisticsonsocialnetworks,includingageandpersonalitytraits(inthisexperiment,weuseMBTIas
aproxy).Basedonauthoritativestatisticaldata,weclassifyprofessionsinto13categoriesandsocial
network trends into 9 categories, with specific categories and definitions detailed in the appendix.
27

Preprint
While ensuring scientific accuracy and diversity, we simplify the generation costs by approximat-
ing dimensions such as age, personality, and profession as independent and identically distributed
random variables. We sample from these distributions, and the large model generates the agents’
backgroundsandsocialcharacteristicsbasedonthisinformation. Thepromptisasfollows:
Please generate a social media user profile based on the provided
personal information, including a realname, username, user
bio, and a new user persona. The focus should be on creating a
fictional background story and detailed interests based on
their hobbies and profession.
Input:
age: {age}
gender: {gender}
mbti: {mbti}
profession: {profession}
interested topics: {topics}
Output:
{{
"realname": str, realname,
"username": str, username,
"bio": str, bio,
"persona": str, user persona,
}}
Ensure the output can be directly parsed to **JSON**, do not
output anything else.
SocialNetwork. Linkingthelarge-scalegeneratedagentsintoarelationshipnetworkisessential.
TheMattheweffectobservedonsocialplatformsdistinguishescoreusersfromordinaryusers;core
usersonX,definedasthosewithmorethan1000followers,accountfor80%ofallusers(Wojcieszak
et al., 2022). Based on this, we derive an initial core-ordinary user attention tree from core users
withinspecificinterestareas,therebyconstructingtheinitialrelationshipnetwork.Specifically,each
agent samples twice from an independent and identically distributed interest category distribution
to obtain two topics of interest. If a topic aligns with a core user, the agent has a probability of
following that core user. To prevent an excessively dense relationship network and enhance the
diversityofinformationvisibletovarioususers,weestablishthefollowingprobabilityat0.1.
E.3 HERDEFFECT
User Generation. In our Reddit experiment, the process of generating users is divided into three
main steps. Initially, we reference the actual demographic distribution of Reddit users (Duarte,
2024), assigning demographic information such as MBTI, age, gender, country, and profession to
each user through random sampling. Subsequently, we employ GPT-3.5 Turbo to select topics of
potentialinteresttotheusersbasedontheaforementionedinformation,choosingfromsevencate-
gories:Business,Culture&Society,Economics,Fun,GeneralNews,IT,andPolitics.Finally,using
demographicinformationandselectedtopics,GPT-3.5Turboisutilizedtogenerateeachuser’sreal
name, username, bio, and persona. The generation prompts for the second and third parts are as
follows.
# Prompt of Step-2
Based on the provided personality traits, age, gender and
profession, please select 2-3 topics of interest from the
given list.
Input:
Personality Traits: {mbti}
Age: {age}
Gender: {gender}
Country: {country}
Profession: {profession}
Available Topics:
28

Preprint
1. Economics: The study and management of production,
distribution, and consumption of goods and services.
Economics focuses on how individuals, businesses,
governments, and nations make choices about allocating
resources to satisfy their wants and needs, and tries to
determine how these groups should organize and
coordinate efforts to achieve maximum output.
2. IT (Information Technology): The use of computers,
networking, and other physical devices, infrastructure,
and processes to create, process, store, secure, and
exchange all forms of electronic data. IT is commonly
used within the context of business operations as
opposed to personal or entertainment technologies.
3. Culture & Society: The way of life for an entire society,
including codes of manners, dress, language, religion,
rituals, norms of behavior, and systems of belief. This
topic explores how cultural expressions and societal
structures influence human behavior, relationships, and
social norms.
4. General News: A broad category that includes current
events, happenings, and trends across a wide range of
areas such as politics, business, science, technology,
and entertainment. General news provides a comprehensive
overview of the latest developments affecting the world
at large.
5. Politics: The activities associated with the governance
of a country or other area, especially the debate or
conflict among individuals or parties having or hoping
to achieve power. Politics is often a battle over
control of resources, policy decisions, and the
direction of societal norms.
6. Business: The practice of making one’s living through
commerce, trade, or services. This topic encompasses the
entrepreneurial, managerial, and administrative
processes involved in starting, managing, and growing a
business entity.
7. Fun: Activities or ideas that are light-hearted or
amusing. This topic covers a wide range of entertainment
choices and leisure activities that bring joy, laughter
, and enjoyment to individuals and groups.
Output:
[list of topic numbers]
Ensure your output could be parsed to **list**, don’t output
anything else.
# Prompt of Step-3
Please generate a social media user profile based on the provided
personal information, including a real name, username, user
bio, and a new user persona. The focus should be on creating a
fictional background story and detailed interests based on
their hobbies and profession.
Input:
age: {age}
gender: {gender}
mbti: {mbti}
profession: {profession}
interested topics: {topics}
Output:
{{
29

Preprint
"realname": "str",
"username": "str",
"bio": "str",
"persona": "str"
}}
Ensure the output can be directly parsed to **JSON**, do not
output anything else.
PostsandCommentsDatasetInExperiment3.3.2,weutilizeadatasetcomprisingauthenticReddit
comments and llm-generated posts. In Experiment 3.4.2, we employ a counterfactual dataset to
simulateposts.
• Real Data: To align with human experiment Muchnik et al. (2013), our dataset included real
comments and post titles from 17 subreddits during March 2023 on Reddit (Pushshift, 2023).
Wegeneratecontextuallyrelevantpostcontentbasedonthesetitlesandcomments. Theprompt
usedforgenerationisasfollows.
Please generate a contextual and smooth post for this comment
and notice that the comments are correct: ’{comment}’. The
response should be approximately 300 characters long and
provide relevant information or analysis. Be careful to
output the content of the post directly, and be aware that
you don’t see comments when you post. And you don’t need to
prefix something like: ’Here is your generated post:\n\n\’
Subsequently,wecategorizedthecontentfromdifferentsubredditsintoseventopics—Business,
Culture & Society, Economics, Fun, General News, IT, and Politics—to match the categories
usedinhumanexperiments. Intotal,wecollected116,932comments. Thespecificsaredetailed
inthetable14.
Table14: DetailsofrealRedditcommentsandgeneratedpostsbytopic.
Subreddit Topic NumbersofPosts NumbersofComments
Economics
finance
personalfinance Economics 4231 21650
it
InformationTechnology
technology
learnprogramming IT 4020 18622
AskHistorians
AskAnthropology
worldbuilding Culture&Society 2319 10489
worldnews news 2874 19134
politics
NeutralPolitics politics 2690 21477
business
smallbusiness business 1807 8043
fun fun 3272 17517
• Counterfactual Data: We utilize all counterfactual information from the dataset (Meng et al.,
2022),comprising21,919entries,tocreatecontentforposts. Someexamplesareshowninthe
table15.
30

Preprint
Table15: Examplesofcounterfactualposts.
CounterfactualPosts
ShanghaiisatwincityofAtlanta
ThelocationofBattleofFranceisSeattle
MichelDenisotspokethelanguageRussian
ThemothertongueofGoHyeon-jeongisFrench
Table16: ActiontypecomparisonacrossScenarios.
ActionType
InformationSpreadinginX
likepost repost follow donothing
GroupPolarizationinX
donothing repost likepost dislikepost follow
createcomment likecomment dislikecomment
ComparisonwiththeHerdEffectinHumans
likecomment dislikecomment likepost dislikepost searchposts
searchusers trend refresh donothing
CounterfactualHerdEffectinReddit
createcomment likecomment dislikecomment likepost dislikepost
searchusers trend refresh donothing
F EXPERIMENTS DETAILS
F.1 ACTIONSOFDIFFERENTSCENARIOS
Due to the significant variations between different scenarios and platforms, we adjust the agents’
actionsaccordingly.TheseactionsareintegratedintotheOASISframework,allowinguserstofreely
selectandcombinethem. TheactionsfordifferentscenariosareoutlinedinTable16.
F.2 INFORMATIONSPREADING
F.2.1 METRICS
We measure the propagation trends of messages using three key metrics: scale, depth, and max
breadth. Belowisacleardefinitionofeachmeasure:
• Scale: The scale of propagation corresponds to the number of unique users involved, as each
usercanonlyrepostapostonceonX.
• Depth: A node’s depth is determined by the number of edges connecting it to the root node
(the original post). The overall depth of propagation is the greatest depth among all the nodes
involved.
• Max Breadth: The breadth of propagation depends on its depth, with the number of nodes at
eachlevelrepresentingthebreadthatthatspecificdepth. Themaximumbreadthisthehighest
numberofnodesfoundatanydepththroughouttheentirepropagation.
Besides,theNormalizedRMSEiscomputedasthefollowingformula:
(cid:113)
1 (cid:80)n (cid:0) yi −yi (cid:1)2
n i=1 simu real
NormalizedRMSE= (7)
yn
real
Letnrefertothemaximumminuteinthesimulationresults,andyi ,yi representsthevalueof
simu simu
a certain metric at the ith minute of the simulation process or the real-world propagation process.
For Normalized RMSE at every minute, since we only compute the discrepancy between the two
datapointsofsimulationresultandrealpropagation, theerrorofi-thminutecanbecalculatedby
|yi −yi |/yn .
simu real real
31

Preprint
F.2.2 ALIGNWITHREALPROPAGATIONS
Intheexperiment,foreachpropagation,wesetthemaximumnumberoftimestepsto50,witheach
time step representing 3 minutes in the sandbox. For action space, we only include like, repost,
follow,anddonothing,otheractionsareremovedtosimplifythesettingsduetothemodel’slimited
capacityandtheinadequatereal-worlduserdatawehavecollected. Ultimately,wewouldcompare
thesimulationresultsforthese150minuteswiththepropagationprocessintherealdataforthefirst
150minutes. Forreal-worldtimeconsumption,ittakes26minutestorunasimulationthatincludes
300agentsfor30timestepsononeNVIDIAA100-SXM4-80GB.
Additionally,todemonstratethereproducibilityofourexperiments,consideringthatthenoiseintro-
ducedbypostsfromotheruserscouldtheoreticallydestabilizethepropagationofthesourcepost,
werandomlyselecttwotopics: onewith33additionalpostsandanotherwithnonoise. Werepeat
thesimulationtentimesforeachtopicandplottedtheresultingcurvesinasinglefiguretoillustrate
thediscrepanciesacrossthetensimulations. Thesimulationresultsforthetopicwithoutnoiseare
morestable. Incontrast,theresultsfortheothertopicexhibitadivergenttrend,whilesixoutoften
experimentsyieldrelativelyconcentratedresults,furthermore,thedegreeofdisturbancecausedby
otherpostsisinfluencednotonlybythenumberofpostsbutalsobytheprominenceoftheposter.
Forinstance,ifasuperuserfromthisgrouppostsadditionalcontent,thepropagationofthesource
postislikelytobeaffectedmoresignificantly, fortunately, thissituationisrareinourdataset, and
thecountofadditionalpostsisrelativelysmallsinceweonlyconsiderpostscreatedwithinonehour
prior to the source post’s creation time as noise. Overall, the simulation results are still relatively
stable.
(a)10timesrepeatedexperimentsontopicwithoutnoise.
(b)10timesrepeatedexperimentsontopicwith33additionalposts.
Figure15: 10timesrepeatedexperimentson2topics.
32

Preprint
F.3 GROUPPOLARIZATION
F.3.1 DILEMMAQUESTIONS
Helen is a successful writer who usually writes popular western
novels. Now, she has an idea for a new novel that could really
make a big impact. If it works out, it could greatly improve
her career. But if it fails, she will have spent a lot of time
and effort for nothing.
What do you think Helen should do?
F.3.2 POLARIZATIONEVALUATIONPROMPTS
Please determine which of the following two sentences is more
extreme. If there is no obvious difference in tone, return "
neutral."
[User Question]
{question}
What do you think Helen should do?
[Answer1]
{answer1}
[Answer2]
{answer2}
[Response Format]
Reason:
Choice: Answer1 or Answer2 or neutral
F.3.3 HELPFULLNESSEVALUATIONPROMPTS
Please help me evaluate the helpfulness and quality of the
responses provided by two AI assistants to the user question
displayed below. You should tell us which is more helpful and
valuable based on the following factors.
1. "Accurate Information": Ensure the AI provides information that
is factual and up to date. 21
2. "Clarity and Comprehensibility": Check if the AI delivers
information in a clear and easily understandable manner.
3. "Completeness of the Response": Ascertain that the AI answers
all aspects of the user’s query.
4. "Contextual Understanding": The AI should demonstrate a clear
understanding of the context of the user’s query.
5. "Creative Problem-Solving": If applicable, observe if the AI
proposes creative solutions to the user’s problem.
6. "Depth of Explanation": Examine whether the AI provides
detailed and in-depth responses when required.
7. "Politeness and Professionalism": The AI should deliver
responses using respectful and professional language.
8. "Reference to Reliable Sources": If the AI claims certain facts
, it should be able to refer to recognized and trusted sources
.
9. "User Engagement": The AI should engage the user effectively
and pleasantly, encouraging positive user interaction.
33

Preprint
[User Question]
{question}
[Answer1]
{answer1}
[Answer2]
{answer2}
[Response Format]
Reason:
Choice: Answer1 or Answer2
F.4 HERDEFFECT
F.4.1 METRICS
We utilized two primary metrics to assess the herd effect: the post score and the disagree score.
Thesemetricswerederivedfromtwoaspects:thebehavioroflikingordislikingbytheLLMAgent,
andthecontentofthecommentsitgenerated.
• PostScore: Thescore(S )ofaRedditpostisthedifferencebetweenitsupvotes(U )anddown-
i i
votes(D ),andcanbenegative:
i
S =U −D
i i i
whereS isthescoreoftheithpost,U thenumberofupvotes,andD thenumberofdownvotes.
i i i
• Disagree Score: In this experiment 3.4.2, where all posts were counterfactual, we examined
comments from LLM agents at various time points. Using GPT-4o, we assessed how much
these comments disagreed with the posts. The evaluation was guided by the following prompt
template:
Someone posted a counterfactual statement: "{post_content}",
and then another person commented: "{comment_content}".
Please provide a rating from 1 to 10 to indicate how much this
person agrees with the counterfactual content, where:
1 means fully believing and agreeing with it, and 10 means
completely disbelieving and opposing it.
Respond only with a JSON object like this:
{{
"score": 7
}}
Ensure the "score" is a single integer between 1 and 10.
Beforetheexperimentbegan,werandomlydividedthecommentsdataforexperiment3.3.2andthe
postsdataforexperiment3.4.2intothreegroups(up-treated,down-treated,andcontrol). Afterthe
experiment concluded, we calculated the mean post score and the 95% confidence interval of the
normaldistributionforallpostsinthethreegroupsofexperiment3.3.2. Similarly,wecalculatedthe
mean disagree score and the 95% confidence interval of the normal distribution at each time step
forallcommentsassociatedwithpostsinthethreegroupsofexperiment3.4.2.
F.4.2 SETTINGDETAILS
Comparison with the Herd Effect in Humans. Our experiment 3.3.2 replicated the setup of a
humanstudy,includingthevisibilityofcommentscores(upvotesminusdownvotes)andprohibiting
therevocationoflikesanddislikes,utilizingReddit’spopularity-basedrecommendationalgorithm.
To minimize biases stemming from the identities of commenters and voters and their interactions,
whichweremeticulouslyaccountedforinthehumanexperiments,wemanipulatedaspecificuserto
postcontentatscheduledintervals. Thisapproachwasadoptedtomitigatetheinfluenceofdifferent
34

Preprint
posters on the behavior of agents, and we further circumvented the impact of relationships with
specificpostingusersontheoutcomesbyprohibitingagentsfromfollowingormutingoperations.
Consequently,theactionspacefortheexperimentincludedactions:likecomment,dislikecomment,
like post, dislike post, search posts, search users, trend, refresh, and do nothing. The controlled
user generated 200 posts at each time step, with each post accompanied by 1-10 comments. The
recommendationsystemcachedthetop300postswiththehighestheatscoresforeachagent, and
eachagenthada0.1probabilityofactivationateverytimestep. Activatedagentswouldrandomly
sampleoneofthese300poststoreadduringthattimestep. Theexperimentwasconductedovera
totalof40timesteps.
Herd Effect Towards Counterfactual Content. The action space of the experiment 3.4.2 in-
cludescreatecomment,likecomment,dislikecomment,likepost,dislikepost,searchposts,search
users,trend,refresh,anddonothing.Eachagenthasa0.1probabilityofactivationateachtimestep,
andeachactivatedagentwillrandomlysample5postsfromtherecommendedcachetoreadduring
thattimestep. Asthenumberofagentsincreasesfrom100,1kto10k,thenumberofpostscached
bytherecommendationsystemrespectivelybecomes50,500,and5000.Thecontrolledusercreates
30,300,3kpostsateachtimestep,respectively,untilallpostsinthecorrespondingdatasets(with
219, 2191, and 21919 posts, respectively) have been created. And the experiment was conducted
overatotalof30timesteps.
F.4.3 EXAMPLESOFRESULTS
In experiment 3.4.2, 10,000 agents were able to discuss their views on counterfactual posts in the
commentsection,interactingbypostingtheirowncommentsorbylikingordislikingothers’com-
ments. Over the course of the discussion, there was a gradual shift towards opposing the counter-
factualcontent,achievingfactualcorrectionatthegrouplevel. Thefigure16belowshowsonesuch
example.
Time Step Time Step Time Step
Figure16: Exampleofagents’commentsoncounterfactualposts. Asinteractionsincrease,agents’
viewpointsgraduallyshiftfromsurpriseandcuriosity,topartialopposition,andfinallytocomplete
rejectionofthecounterfactualcontent.
G MISINFORMATION SPREADING IN ONE MILLION AGENTS
G.0.1 TRUTHANDMISINFORMATIONPAIRS
# Technology
## Truth
Amazon is expanding its delivery drone program to deliver packages
within 30 minutes in select cities. This initiative aims to
improve efficiency and reduce delivery times.
## Misinformation
Amazon plans to completely eliminate its delivery drivers within
two years due to the new drone program. #Automation #Future
# Education
## Truth
Harvard University has announced a new scholarship program that
will cover full tuition for all undergraduate students from
families earning less than $75,000 per year.
35

Preprint
## Misinformation
Harvard is raising tuition fees for all students despite the new
scholarship program, making it harder for families to afford
education. #EducationCrisis
# Entertainment
## Truth
The latest Marvel movie, Avengers: Forever, has officially broken
box office records, earning over $1 billion in its opening
weekend.
## Misinformation
Marvel is planning to retire the Avengers franchise after this
film, saying it will not produce any more superhero movies. #
EndOfAnEra
# Health
## Truth
A recent study shows that regular exercise can significantly
reduce the risk of chronic diseases such as diabetes and heart
disease.
## Misinfo
Health experts claim that exercise will be deemed unnecessary in
five years as new treatments will eliminate chronic diseases
entirely. #HealthRevolution
H LIMITATIONS & FUTURE DIRECTIONS
RecSys Thecurrentrecommendationsystemisonlydesignedatahighlevelsimilartoplatforms
like X (formerly Twitter) or Reddit. For example, the RecSys designed following X’s model only
recommendssemanticallysimilarpostsbasedontheuser’sprofileandrecentactivity.Morecomplex
recommendation algorithms, such as collaborative filtering, have not been implemented in OASIS,
leadingtoamisalignmentbetweenOASIS’sperformanceandreal-worldpropagationdata.
User Generation Whether we obtain user data through the Twitter API or the User Generation
algorithmproposedinOASIS,bothapproachesabstracttherealindividualtosomeextent, leading
toanaturalgapbetweenoursimulatorandtherealworld.
SocialMediaPlatform Althoughwehaveexpandedtheactionspaceonsocialmediaplatformsto
aconsiderableextent,notallpossibleactionsarecovered. Forexample,ourplatformcurrentlydoes
notsupportfeatureslikebookmarking,tipping,purchasing,orlivestreaming,whichcouldbeadded
in future work. Additionally, the current simulation operates solely in a text-based environment,
meaningagentsareunabletoperceiveimages,videos,oraudio.Futureextensionscouldincorporate
multimodalcontenttoenhancetherealismofthesimulation.
Scalable Design While our asynchronous design helps to avoid bottlenecks, simulating millions
of agents still requires several days to complete. Optimizing inference speed and improving the
efficiencyofdatabasesystemswillbecriticalinreducingtimeandcost, makinglarge-scalesocial
simulationsmorefeasibleforwidespreadapplicationsinthefuture.
Untapped Potential Our large-scale social simulation platform has the potential to serve as a
foundationalenvironmentforotherresearch.Forinstance,itcanbeusedtoevaluatetheperformance
ofnovelrecommendationsystemsortotrainlargelanguagemodels(LLMs)withenhancedinfluence
capabilities,usingfeedbackfromotheragentsinthenetworkasarewardsignal.
36

Preprint
I SOCIAL IMPACT AND ETHICAL CONSIDERATIONS
ThedevelopmentandapplicationofOASISprovidevaluableinsightsintocomplexsocialphenomena
such as information propagation, group polarization, and herd effects. However, this also raises
important ethical considerations. First, the replication of real-world social dynamics using large
language model (LLM) agents introduces concerns regarding the fidelity and interpretation of the
results. Theriskofreinforcingbiases,especiallyinareasrelatedtomisinformationorpolarization,
could exacerbate real-world issues if not properly managed. Researchers using OASIS must be
cautiousinhowthesesimulationsinfluencepublicunderstandingorpolicyrecommendations.
Another key concern is privacy. While OASIS is designed to replicate social media environments,
the use of real-world data for training agents may introduce risks related to user anonymity and
datasecurity.Ensuringtheethicalhandlingofanyreal-worlddatasets,includinganonymizationand
consent,iscrucial.
Lastly,thescalabilityofOASIS,whileanassetforresearch,alsopresentspotentialdangersifmis-
used. Large-scale agent-based models, particularly those that simulate millions of users, could be
leveragedforunethicalpurposessuchasmanipulationofonlinediscourseormisinformationcam-
paigns. It is therefore essential to implement strict governance and ethical guidelines to prevent
misuseofthesimulator’scapabilities.
37
