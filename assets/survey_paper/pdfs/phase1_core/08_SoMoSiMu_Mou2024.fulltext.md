Title: 08_SoMoSiMu_Mou2024

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/phase1_core/08_SoMoSiMu_Mou2024.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:37+00:00
- page_count: 21
- status: ok
- text_char_count: 71675

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

Unveiling the Truth and Facilitating Change: Towards Agent-based
Large-scale Social Movement Simulation
XinyiMou1,ZhongyuWei1,2,XuanjingHuang3,4
∗
1SchoolofDataScience,FudanUniversity,China
2ResearchInstituteofIntelligentandComplexSystems,FudanUniversity,China
3SchoolofComputerScience,FudanUniversity,China
4ShanghaiCollaborativeInnovationCenterofIntelligentVisualComputing,China
{xymou20,zywei,xjhuang}@fudan.edu.cn
Abstract
GGeeoorrggee FFllooyydd,, aa 4466--yyeeaarr--oolldd AAffrriiccaann--AAmmeerriiccaann mmaann,, ddiieedd iinn
MMiinnnneeaappoolliiss aafftteerr bbeeiinngg hhaannddccuuffffeedd aanndd ppiinnnneedd ttoo tthhee ggrroouunndd bbyy
DDeerreekk CChhaauuvviinn,, aa wwhhiittee ppoolliiccee ooffffiicceerr……
Socialmediahasemergedasacornerstoneof
social movements, wielding significant influ- John Smith @user1: It’s time for … 𝑡
He/him
ence in driving societal change. Simulating Highly active and
passionate about #BlackLiveMatters He
theresponseofthepublicandforecastingthe sharing information can not breathe! TT
and taking part … ww
p
p
o
o
t
r
e
ta
n
n
ti
t
a
.
l
H
im
ow
pa
e
c
v
t
er
h
,
a
e
s
x
b
is
e
t
c
in
o
g
m
m
e
e
in
th
c
o
re
d
a
s
si
f
n
o
g
r
l
s
y
im
im
u
-
-
Message Feed
TT
rr
eettttii
𝑡+1
lating such phenomena encounter challenges
A
A H
n
n e
n
r n
a
/ s a
is
h D
m
e a
o
v
de
is
rately
@JohnSmith: #Black…
ee
nniill ee mmii
concerningtheirefficacyandefficiencyincap- active. She enjoys The officer was too
detailing and cruel. We must …
turing the behaviors of social movement par- refining ideas …
ticipants. Inthispaper,weintroduceahybrid … …
framework for social media user simulation,
wherein users are categorized into two types. Figure1:Anillustrationofuserinteractionsandattitude
CoreusersaredrivenbyLargeLanguageMod- changesafteratriggereventhappens. Userscantake
els, while numerous ordinary users are mod- actionssuchaspostingandretweetingaccordingtotheir
eled by deductive agent-based models. We traits,andtheirgeneratedcontentwillbestoredinthe
further construct a Twitter-like environment Twittertimelineandfedtotheirconnectedusers. Users
to replicate their response dynamics follow- canchangeattitudesonceperceiveothers’opinions.
ingtriggerevents. Subsequently,wedevelopa
multi-facetedbenchmarkSoMoSiMu-Bench
forevaluationandconductcomprehensiveex- tions. Therefore,proactivemeasurestoanticipate
periments across real-world datasets. Exper- theimpactofsucheventsbecomeimperative.
imental results demonstrate the effectiveness Previous research on analyzing online social
andflexibilityofourmethod1.
movements has primarily concentrated on retro-
spectiveanalysisofcontentandusers(Giorgietal.,
1 Introduction
2022;RoyandGoldwasser,2023),ratherthanuti-
In the past decades, social media has wit- lizingsimulationforprediction. Agent-basedmod-
nessed many social movements, such as the els (ABMs) have been extensively employed for
Arab Spring (Rane and Salem, 2012) and simulationinsocialscience(Schelling,2006;Jack-
#Metoo(Brünkeretal.,2020). Twitterstandsout son et al., 2017), wherein each agent symbolizes
as a prominent forum giving powerful voices to anindividual,andinteractionsamongagentsgive
groups demanding change. As illustrated in Fig- risetodistinctsocialphenomena. Typically,ABMs
ure1,thedisseminationofbreakingnewsonTwit- are micro-level mathematical models that define
terpromptstheproliferationofopinions,influenc- howindividualsaffecteachother,creatingcollec-
ingcollectivesentimentandshapingsocietalagen- tivesocialpatternsthroughsimulatinginteraction
das,oftenresultinginreal-worldactions(Royand atscale(Törnbergetal.,2023).
Goldwasser, 2023). Although the majority of so- Recently,LargeLanguageModels(LLMs)have
cial movements are reported peaceful, the sheer demonstratedimpressiveabilityinhuman-levelin-
scaleofparticipationcansometimesescalateinto telligence (Wang et al., 2023b; Xi et al., 2023).
violenceanddestruction,posingpotentialramifica- LLM-based user simulations have been success-
fullyexperimentedindomainssuchasrecommen-
∗Correspondingauthor.
dation (Wang et al., 2023c; Zhang et al., 2023)
1Code and data are available at https://github.com/
xymou/social_simulation. and collaborative work (Chen et al., 2023; Qian
4789
FindingsoftheAssociationforComputationalLinguistics:ACL2024,pages4789–4809
August11-16,2024©2024AssociationforComputationalLinguistics

et al., 2023b). However, the exploration of con- threereal-worldmovementsandcorresponding
ductinglarge-scaleonlinesocialmovementsimu- evaluationmethods. Experimentresultsandanal-
lationsusingLLMsremainslimitedandpresents ysisdemonstratetheeffectivenessofourmethod.
the following challenges: (1) How to accurately
simulateusersofsocialmediaandreplicatetheir 2 FormalizationofPublicOpinion
behaviorswithinthecommunity? (2)Howtoeffi- DynamicsSimulation
cientlysimulatealargenumberofusers,giventhe
Modelingthechangeinpeople’sattitudes,beliefs
impracticalityofemployingthousandsofLLMs?
and opinions is crucial since opinion change can
(3)Howtocomprehensivelyevaluatetheeffective-
result in societal phenomena such as bipolariza-
nessofthesimulation?
tionandextremization. Inthissection,wepresent
Tohandlethesechallenges,thispaperintroduces
the preliminaries of agent-based models and the
anovelhybridframeworkforsocialmediauser
formulationofthetargetedtask.
simulation. ConsideringtheParetodistribution2
inherentinsocialmediauserengagement,wecate- 2.1 Preliminaries
gorizeusersintotwotypes: coreusers,comprising
2.1.1 Agent-basedModelsinOpinion
activeandinfluentialfiguressuchasopinionlead-
Dynamics
ers, and ordinary users. Core users are character-
Agent-basedmodels(ABMs)aremicro-levelmath-
ized and driven by LLMs, enabling emulation of
ematicalmodelsdefininghowanindividualagent
their complex behaviors, while a vast number of
adjusts the attitudes toward specific topics based
ordinaryusersaregovernedbyABMs,providinga
on the opinions of others (Lorenz et al., 2021;
practicalwayforusersimulationinlargescale.
ChuangandRogers,2023). Bysimulatinginterac-
Based on the hybrid mechanism composed of
tions among individual behaviors, ABMs enable
two types of users, we establish an online so-
the identification of emergent, group-level mech-
cial media environment tailored for online so-
anismsthatcouldnotbepredictedusingthechar-
cialmovementsimulationandevaluation. Inthis
acteristics of individuals within a social system
environment, messages are organized in Twitter-
alone(Törnbergetal.,2023).
like timelines and offline news can be dissemi-
Typically,inABMsforopiniondynamics,each
nated. User interactions and resultant collective
agentkeepsacontinuousattitudescorerepresent-
attitudesareobservedthroughattitudescores. To
ingitsopinion,wherethesignofthescorerepre-
systematically evaluate the simulation, we pro-
sents attitude direction, i.e., positive or negative,
pose a novel benchmark SoMoSiMu-Bench, in-
and the magnitude of the score describes the at-
cludingthreereal-worldcollecteddatasets(Metoo,
titude intensity. ABMs define how this score is
RoeOverturnedandBlackLivesMatter)andaneval-
changed under the influence of others. Although
uation strategy at both the micro and macro lev-
the exact formulations vary in different ABMs,
els,focusingonindividualuseralignmentandsys-
mostmodelscanbedecomposedintocomponents
temicoutcomesrespectively. Evaluationresultson
thatarepresentacrossABMsandbeexpressedin
SoMoSiMu-Benchdemonstratetheeffectiveness
aunifiedformulation(ChuangandRogers,2023),
ofoursimulationframework.
wherethreekeyfunctionscanspecifyit,i.e.,theat-
Ourcontributionscanbesummarizedasfollows:
titudeupdatefunctionf ,theselectionfunction
update
- We introduce a hybrid simulation framework f andthemessagefunctionf .
selection message
where two types of users are separately mod-
UpdateFunction Theupdatefunctiongenerally
eled,totacklethecostandefficiencychallenges
definesthechangeofattitudes. Formally,theatti-
associatedwithsimulatingmassiveparticipants.
tudeupdateis:
- Wedevelopasimulatortailoredforonlinesocial
movements,featuringaTwitter-likeenvironment ∆a i,t = a i,t+1 a i,t = f update (a i,t ,M i,t ), (1)
−
andmodelingofuseropiniondynamics. where∆a istheattitudechangeofagentifrom
i,t
- We provide the first benchmark SoMoSiMu- time step t to t + 1, a and a are the atti-
i,t i,t+1
Bench for social movement simulation evalua- tude of agent i before and after interaction, and
tion, including a data collection consisting of M = m j J are the messages the
i,t j,t i,t
{ | ∈ }
agent i receive from J , i.e., those who interact
2https://en.wikipedia.org/wiki/Pareto_ i,t
distribution withtheagentiattimestept.
4790

Agent Interaction
core user
ordinary user
Timeline 𝑡=1 𝑡=2 … 𝑡=𝑛
Core User Context to Core User @Anna: Ordinary User
You are Anna. Anna is a left- Attitude at time 𝑡
Memory Profile Module Memory leaning user who is active …
Writing Retrieval
Memory Module The news you got is …
Update Function 𝑓𝑢𝑝𝑑𝑎𝑡𝑒
Your memory is …
Action Module
Post Retweet
The Twitter page is … Selection Function 𝑓𝑠𝑒𝑙𝑒𝑐𝑡𝑖𝑜𝑛
Reply Like R
W
e
h
s
a
p
t
o
w
n
i
s
ll
e
y
:
ou do next? Message Function 𝑓𝑚𝑒𝑠𝑠𝑎𝑔𝑒
Post a tweet: This is a total farce! Attitude at time 𝑡+1
Do Nothing #BlackLiveMatters
postprocess➔ attitude:
Figure2: Theproposedframeworkarchitecture. Thebottompartillustratesthearchitectureofcoreusersandthe
mechanismforordinaryusers. Thetoppartpresentsthesimulationprocess. Ateachround,coreuseragentstake
actionbygeneratingtextualresponsesbasedoncontextualinformation,andtheirattitudesareconveyedtoordinary
usersafterpostprocessing,whileordinaryuserscommunicateusingattitudescoresdirectly.
SelectionFunction Theselectionfunctiondeter- self-evolve,deconstructcomplextasks,andtrans-
minesthesetofagentsJ thatwillhaveasocial late the agent’s decisions into specific outcomes.
i,t
influenceonagenti. Itcanbedrivenbyinternalfac- Benefiting from the strong generative ability of
torslikeinternalintendancytointeractwiththose LLMs,LLM-empoweredagentscanmodelmore
more similar to them, or by external factors such complexbehaviorsofusersinsteadofsimplyrep-
asrecommendationalgorithmsoftheplatforms. resentingopinionswithasinglescore.
MessageFunction Themessagefunctiondeter-
2.2 TaskFormulation
minesthemessagem thatagentj sharesbased
j,t
onitsattitudea . Formally,itisalsoacontinuous In this paper, we aim to predict how a group of
j,t
score,afunctionoftheattitudea : users’opinionsonasocialmovementeventchange
j,t
throughagent-basedsimulation,andcomparethe
m = f (a ), (2) simulation results with real-world scenarios. We
j,t message j,t
consider a group of users = 1,...,U , each
U { }
Most ABMs assume that agents convey their in- of whom participates in an online social move-
ternalattitudewithotheragentswithoutbias,i.e., mentandhasanattitudeonthespecifictopic. The
m j,t = f message (a j,t ) = a j,t . attitudes evolve through social interaction. Let
a i,t A = [ 1,1]betheattitudethatuseriholds
2.1.2 LLM-empoweredAgents ∈ −
at time step t 1,2,... = N, where the sign
∈ { }
Recently,agrowingresearchareaemploysLLMs ofa entailsthedirectionoftheattitudeandthe
i,t
toconstructautonomousagents,wherethekeyidea absolutevalueofa representsthemagnitudeof
i,t
istoequipLLMswithcrucialhumancapabilities theattitude. Foreachuser,weinstantiatethecorre-
such as memory and planning. In terms of agent spondingagentwiththeuser’sinitialattitudeand
architecture,existingresearchcanbesynthesized profile, and construct the social networks based
intoaunifiedframeworkconsistingoftheprofile ontheauthenticfollowingrelationshipsonTwitter.
module,thememorymodule,theplanningmodule, Then,weaimto(1)simulatethebehaviorsofusers
andtheactionmodule(Wangetal.,2023b). They attheindividuallevelgivenacertaincontextinthe
are designed to indicate the profiles of the agent patternofsingle-roundsimulation;and(2)simulate
roles,helptheagentsaccumulateexperiencesand continuously to observe how collective opinions
4791

shiftovertimeresultingfromuserinteractions. post original content. (2) Amplifier: users who
collectmultiplethoughtsandshareideasandopin-
3 HybridFrameworkforSocialMedia ions. (3) Curator: they use a broader context to
Simulation defineideas. Theytendtotaketheideasofothers
andeithervalidate,question,challengeordismiss
Userengagementinsocialnetworksoftenexhibits
them. (4) Commentator: users who take part in
aParetodistribution,wherethebulkofcontentorig-
somethingtowhichtheystronglyfeelabout. They
inatesfromasmallfractionofindividuals. Thus,
retweet actively. (5) Viewer: the inactive major-
thosemoreactiveandinfluentialsuchasopinion
ity,whoprefertoconsumeinformationratherthan
leadersshouldbemodeledfinely,whilethesilent
createorshareinformationonline.
majoritycanbecontrolledbysimplermodels. The
overallframeworkisillustratedinFigure2,where
3.1.2 MemoryModule
socialmediausersaredividedintocoreusersand
We consider two types of memory to fully char-
ordinaryusers. Thetwotypesofusersaredrivenby
acterizethesocialmediauserandreconstructthe
differentmodels,toaddressthecostandefficiency
human-like memory mechanisms. (1) Personal
issuesofusingthousandsofLLMs.
Experience: Thepersonalexperienceisauthentic
3.1 SimulationofCoreUsers recordsoftheusers,whichcanbeextractedfrom
the users’ historical tweets before the event hap-
We build an agent architecture by empowering
pens. By retrieving the relevant experience and
LLMswiththenecessarycapabilitiesforcoreuser
opinions of the user, it would be easier to infer
simulation. Anoverviewoftheagent’sarchitecture
how this user would behave in similar situations.
isillustratedintheleftlowerpartofFigure2. The
(2)EventMemory: Theeventmemoryrepresents
agent is equipped with a profile module, a mem-
the observation of the agent itself and other visi-
orymodule,andanactionmodule,tocompletethe
ble agents. It captures specific and concentrated
complexoperationsonTwitter.
insightsaftertheeventhappens,i.e.,afterthesim-
3.1.1 ProfileModule ulation starts. We integrate a memory module to
manipulatethememoriesofagents,mainlyinclud-
Weextractandsummarizethefollowinginforma-
ingthreeoperations:
tionfromrealuserdataandpromptthecorrespond-
ingagentswhensimulating:
MemoryWriting Therawobservationsinclud-
Demographics Thebasicprofileisdemograph- ingbehaviorsperformedbytheagentsthemselves
ics, such as name, gender, political leaning and andtweetsvisibletotheagentsareinputintothe
accounttype(Brünkeretal.,2020). Thisinforma- memorymoduleaftereachround’sinteraction,in
tionishighlyrelatedtotheuser’spotentialstance bothformsofnaturallanguagesandvectors.
onsocialevents. Weinducethedemographicsfrom
MemoryRetrieval Agentscanextractinforma-
users’biographiesandprevioustweets. Theimple-
tionfromthememoriesconsideringdifferentfac-
mentationdetailscanbefoundinAppendixB.2.
tors. Theretrievalfunctiongetsobservationsbased
SocialTraits Asparticipantsinasocialplatform, onrecency,relevance,importanceandimmediacy
agents’socialtraitssuchasactivityandinfluence (Park et al., 2023; Chen et al., 2023), where re-
also capture important characteristics. Activity cency assigns a higher score to memory objects
quantifies the frequency of a user’s interaction, that were recently accessed, relevance assigns a
whileinfluencereflectsthequalityandpopularity higherscoretomemoryobjectsthatarerelatedto
ofgeneratedcontent. Sinceusersexhibitlong-tail thecurrentsituation,importanceassignsahigher
distributionamongthesesocialtraits,wesegment score to memory objects that the agent believes
themintothreeuneventiers(Zhangetal.,2023). to be important, and immediacy assigns a higher
scoretomemorythatneedsquickattentionorim-
Communication Roles To more accurately de-
mediate response. The top-ranked memories are
scribeusersinparticipationofsocialmovements,
subsequentlyintegratedaspartoftheprompt.
weintegrateEdelman’stopologyofinfluence(TOI)
(Bentwood, 2008; Tinati et al., 2012) to identify Memory Reflection We incorporate the reflec-
thecommunicationrolesofonlineusers: (1)Idea tionoperationtourgetheagentstogeneratehigh-
Starter: individualswhostarttheconversationand level thoughts. We follow Park et al. to im-
4792

plementreflectionperiodically,withstepsinclud- time step t+1 for other users who follow Anna.
ing: (1)generatingthemostsalientquestionsthat Forordinaryusers, informationistransmittedac-
canbeaskedgiventheagent’srecentexperiences; cordingtothemessagefunctiondefinedinABMs.
(2)promptingagentstoextracthigh-levelinsights
Interaction between Heterogeneous Agents
from retrieved relevant memories. This type of
SinceABMsonlyacceptnumericinputsandout-
memorywillbeincludedalongsideotherobserva-
puts, we need to transform the content generated
tionswhenretrievaloccurs.
by core users into attitude scores for ABMs. Ex-
3.1.3 ActionModule ternalLLMsareemployedtoannotatethestance,
Wedesignanactionmoduletailoredforsocialme- i.e.,attitudedirectionofthecontent,andsentiment
diaecology,whereactionsarehighlyrelatedtoin- analysistoolisappliedtocalculatetheattitudein-
formationandattitudepropagation,including: (1) tensity. After this postprocessing, the scores can
Post: postoriginalcontent;(2)Retweet: retweet be processed by the message function in ABMs.
anexistingtweetintheagent’spage,eitherforward Considering that the impact of ordinary users on
directly or post additional statements; (3) Reply: coreusersissubtle,wecurrentlydonotaddressthe
reply to authors of existing tweets or replies; (4) influencefromordinaryuserstocoreusers.
Like: likeanexistingtweet; (5)DoNothing: do
3.4 SimulationEnvironment
nothingandkeepsilent. Theoptionalactionsare
presentedtotheagentsviaprompting. Theagents’ To simulate and evaluate users’ reactions during
responsesarethenparsedintoconcreteeffectson realevents,webuildaTwitter-likesimulationplat-
the environment, such as adding a new tweet or formthattheagentsaresituatedwithinanddiscuss
increasingtheretweetsofanexistingtweet. theexecutionofthesimulation.
3.2 SimulationofOrdinaryUsers MessageFeedMechanism Theenvironmentop-
eratesbasedontheconceptoftimeline(Tinatietal.,
InitialAttitudes Torestoretherealsituationand
2012). Inthisenvironment, eachuserhasatime-
laythefoundationforreliablesimulation,weini-
lineoftweetscreatedbythemselvesandotherusers
tialize the attitudes based on the corresponding
theyfollow. Also,apublictimelineiskepttostore
user’stweetsatthattimeperiod,insteadofsetting
tweets sent by all users. At each round, the most
theinitialopinionsuniformlydistributed. Thiscan
recenttweetsareprovidedforprompting.
be implemented by annotating the direction and
densityoftheirgeneratedcontentonTwitter. Offline News Feed Some offline events often
actascatalystsforsocialmovements,suchasthe
Attitude Change Mechanism We employ
George Floyd incident triggering the widespread
ABMsinopiniondynamicsinSec.2.1.1tomodel
#BlackLivesMatter movement. Thus,weprovide
theattitudechangeofordinaryusers. Formally,at
real-worldeventsdescribedinnaturallanguagesas
time step t, agent i interacts with a set of agents
backgroundinformationtothecoreuseragents.
J based on the selection function f . The
i,t selection
selectedagentsthensharetheirmessagesbasedon
3.5 SimulationProcess
themessagefunctionf ,whichisafunction
message
Oursimulatoroperatesindifferentwaysfordiffer-
of their attitudes. After receiving the messages,
entpurposesinSec.2.2. Tovalidatethereplication
agentiupdatesitsattitudefroma toa based
i,t i,t+1
ofuserbehaviors,thesimulatorcanruninasingle
ontheattitudeupdatefunctionf .
update
round,wheretheprovidedcontextisauthentic. To
3.3 InteractionbetweenAgents estimatefuturepublicopinion,oursimulatorcan
also operate in a round-by-round manner, where
Inthehybridsystem,theinteractionbetweendif-
thesubsequentcontextcontainssimulatedcontent.
ferentagentsisshownatthetopofFigure2.
Duringeachround,i.e.,timestep,agentsforcore
Interaction between Homogeneous Agents users autonomously give a thought before taking
Coreusersconveytheirthoughtstoothersbygen- actions and then decide what actions they would
eratingspecificcontent,intheformofnaturallan- liketotake. Overall,LLMagentsforcoreusersper-
guages. For example, as shown in Figure 2, user formactionsbasedonthefollowinginformation:
Annageneratesapostattimestept,andthiscon- (1)profileordescriptionoftheagent;(2)memory
tentwillbepartofthe"Twitterpage"inpromptat of the agent; (3) triggering offline news; (4) the
4793

Dataset Event #Users #Tweets TimeSpan theiroveralltweetfrequency. Next,werandomly
E1 1,000 18,638 Oct15-Oct22,2017 sampleordinaryusersfromthosewhotweeteddur-
Metoo
E2 1,000 13,291 Jan06-Jan13,2018 ingtheeventperiod. Subsequently,wecollecttheir
E1 1,000 61,687 May02-May09,2022
Roe social networks and tweets during the event pe-
E2 1,000 59,829 Jun24-Jul01,2022
P1 1,000 10,710 May25-Jun01,2020 riod and annotate the attitude scores using GPT-
BLM
P2 1,000 21,480 Jun02-Jun09,2020 3.5(OpenAI,2023)andTextblob3.
To reduce the annotation cost for validation,
Table1: Statisticsofourdataset. InMetoo,E1isAmer-
rather than the simulation cost, we retain 700 or-
ican actress Alyssa Milano starts the #Metoo move-
dinaryusers. Asaresult,1,000usersareacquired
mentandE2is#Timesupcampaignonthe2019Golden
forthesimulationofeachevent. Thestatisticsof
Globes Awards; In Roe, E1 is The leakage of the
Supreme Court draft opinion and E2 is The Supreme thedatasetsarepresentedinTable1. Moredetails
CourtoverturnsRoev. Wade;InBLM,weincludetwo canbefoundinAppendixB.
phasesaftertheMurderofGeorgeFloyd.
4.2 MicroAlignmentEvaluation
To evaluate the effectiveness of the simulation at
Twitter page showing tweets visible to the agent;
theindividuallevel,wesimulateinsingleroundsby
(5)notificationscontainingrepliestotheagent. A
providingauthenticcontextualinformationtoeach
fullpromptexamplecanbefoundinAppendixC.3.
coreuseragentandassesstheirdecision-making.
Agents for ordinary users update their attitudes
based on the pre-defined formulas in ABMs and
- Stance Alignment: We evaluate the stance of
perceivedmessagesfromotheragents. Theprocess
generatedcontent,i.e.,classifyitintothreecat-
isshowninthealgorithmsinAppendixC.1.
egories: support,neutralandoppose. Sincethe
categoriesareconcentratedonsupportandneu-
4 SoMoSiMu-Bench: ABenchmarkfor
tral,themeanabsoluteerror(MAE)ofattitude
SocialMovementSimulation
scoresisalsoreported.
Inthissection,wepresenttheSoMoSiMu-Bench, - Content Alignment: We classify the agent-
a benchmark for simulation evaluation. We con- generatedcontentinto5types,i.e.,CallforAc-
structadatacollection, composedofthreesocial tion, Sharing of Opinion, Reference to a Third
movementsonTwitter. Then,evaluationstrategies Party, Testimony and Other (Brünker et al.,
atthemicroandmacrolevelsaredesigned. 2020). Accuracy and macro F1 score are re-
ported,andcosinesimilaritybetweensimulated
4.1 Datasets
contentandrealcontentisalsoprovided.
Wefirstpresenttheconstructionofourdataset.
- Behavior Alignment: We evaluate whether the
agents take the corresponding actions done by
Data Collection To broadly evaluate the sim-
users. Sinceonlypostingandretweetingcanbe
ulation performance of the proposed method,
observedinTwitterdatasets,wenarrowdownthe
we construct three Twitter datasets by collecting
actionspacetopostandretweet. Accuracyand
tweets related to specific social movements, i.e.,
macroF1scorearereported.
Metoo (Maiorana et al., 2020), RoeOverturned
(Roe) (Chang et al., 2023) and BlackLivesMatter
4.3 MacroSystemEvaluation
(BLM) (Giorgi et al., 2022). For each movement,
Toevaluatetheeffectivenessofthesimulationat
wecollecttweetsspanningtwospecificeventsor
themacrolevel,wequantifytheattitudedistribu-
phases,asoutlinedinTable1.
tionfrombothhorizontalandverticalperspectives
UserSelection Duetotheabsenceofanauthor- inacompletemulti-roundsimulation.
itative definition for core users, we identify core
- StaticAttitudeDistribution: Wecapturecharac-
users by ranking all participants based on the ac-
teristics of attitude distribution in quantitative
tivityandinfluencemetricsinpractice. Fromthe
terms: BiasandDiversity(Lorenzetal.,2021).
gatheredtweets,weselect300coreusersbyfirst
Bias is measured as the deviation of the mean
identifyingthetop100mostinfluentialindividuals
attitudefromtheneutralattitude,andDiversityis
basedonthenumberofreceivedretweets. Wethen
thestandarddeviationofattitudes. Wemeasure
extendthisselectionbyselectinganadditional200
active users from their social networks, based on 3https://github.com/sloria/TextBlob
4794

at every time step and average over time. Dif- Stance Content Behavior
Datasets
Acc. F1 MAE Acc. F1 Sim. Acc. F1
ferences between simulated and real measures
Metoo 0.9679 0.3400 0.2311 0.7010 0.1988 0.8064 0.7313 0.5212
∆Biasand∆Div.arereported. Roe 0.9430 0.3361 0.2058 0.6423 0.1957 0.8090 0.6665 0.4691
BLM 0.8991 0.3735 0.1627 0.7353 0.2218 0.8406 0.7796 0.5759
- TimeSeriesoftheAverageAttitude: Wemeasure
thesimilaritybetweenthetimeseriesofaverage Table2: Resultsofmicroalignmentevaluation.
attitude and the simulated one, using Dynamic
TimeWarping(DTW)(Müller,2007)andPear- coreusersbasedonAgentVerse(Chenetal.,2023),
soncorrelationcoefficient(Cohenetal.,2009). whileforordinaryusersweusethemesa4 library
to implement the conventional agent-based mod-
CalibrationandValidation Tofindtheproper
els. For micro alignment evaluation, we sample
parametersforABMsinthehybridsystem,weper-
(user, context) pairs from the dataset detailed in
formthecalibrationandvalidationsettings(Geste-
Appendix B.4 to reduce cost. For macro system
feldandLorenz,2023). Calibrationaimstofindthe
evaluation,werun14stepsforeacheventandmore
bestcombinationofparametersthatcanhelpmatch
detailscanbefoundinAppendixC.
theempiricaldistributions. Wespecifyparameter
valuesforaparametersweeptoproducesimulation
5.2 MicroAlignmentEvaluation
resultsonE1orP1ofeachmovement. Then,we
Table 2 shows the results of the micro alignment
report the validation results on E2 or P2. Since
evaluationonthethreedatasets. Wecanobserve:
simulatingwithLLMshundredsoftimesisunaf-
fordable,weperformcalibrationinpureABMsand - LLM-empoweredagentseffectivelymodelcore
applytheoptimalparameterstothehybridmodel. users’ stances on specific topics. This can be
ThedetailscanbefoundinAppendix C.4. attributedtothepersonalizedprofilesreflecting
users’ leanings. However, they struggle to gen-
5 Experiments
eratenon-supportivecontent,resultinginlowF1
scores. This is because LLMs tend to produce
5.1 ExperimentSettings
contentwithclearstances,unlikerealusers,who
WeincorporatethefollowingABMsforordinary
mayillustratemorecomplexbehaviors,suchas
users in the hybrid framework. Meanwhile, we
sharingexternallinksormentions.
employtheseABMstomodelallusers(referredto
- The LLM-empowered agents can replicate the
aspureABMs)asbaselinesforcomparison. More
contentgeneratedbyusers. Bothintherealdata
detailscanbefoundinAppendixA.
andsimulatedresults,user-generatedcontentis
- Bounded Confidence Model (BC) (Deffuant concentrated in call for action and sharing of
etal.,2000): itassumesthatifthereceivedmes- opinions. It’sdifficultforagentstogeneratetes-
sage is close enough to an agent’s attitude, the timonycontentsincetheylacktheofflineexperi-
messagehasanassimilationforceontheagent. ence ofthe users. Moreover, theoverallcosine
- Bounded Confidence Model-Multiple similaritybetweenrealandsimulatedcontentap-
(HK) (Rainer and Krause, 2002): a vari- proaches80%,affirmingtheircapabilitytorepli-
antofBC,whichcanhandlemultiplesources. cateuserresponsestospecificcontexts.
- RelativeAgreementModel(RA)(Deffuantetal., - The LLM-empowered agents can well distin-
2002): extendstheBCinthatthesimilaritybias guish between different users who are more in-
isacontinuouslydecayingfunction. clined to create original content and those who
prefertoretweet,achievingover72%accuracy
- Social Judgement Model (SJ) (Jager and Am-
on all the three datasets. It can be attributed to
blard, 2005): additionally includes a repulsion
theportrayalofsocialtraitsandcommunication
forcebasedonBC.
roles in the profile, which indirectly influences
- Lorenz(Lorenzetal.,2021): includesassimila-
theagents’choiceofactions. Theablationstudy
tion force, reinforcement force, similarity bias,
inAppendixD.1furtherdemonstratesthis.
polarizationfactorandsourcecredibility.
5.3 MacroSystemEvaluation
Foralltheexperiments,weuseGPT-3.5-Turbo-
0613 to simulate core users, with max tokens set Table3showstheresultsofthemacrosystemeval-
to 256 and temperature set to 0 for more deter- uation. Wecanobserve:
ministicresults. WeimplementLLM-empowered 4https://mesa.readthedocs.io/en/stable/
4795

Metoo Roe BLM
Method
∆Bias↓ ∆Div.↓ DTW↓ Corr.↑ ∆Bias↓ ∆Div.↓ DTW↓ Corr.↑ ∆Bias↓ ∆Div.↓ DTW↓ Corr.↑
BC 0.0124 0.0184 2.7760 0.4831 0.0265 0.0144 5.7662 -0.7755 0.0078 0.0036 5.2289 -0.4404
Hybridw/BC 0.0135 0.0108 1.8440 0.7043 0.0239 0.0121 2.4611 0.3607 0.0300 0.0069 3.9254 0.1248
HK 0.0093 0.0105 2.9171 0.0262 0.0258 0.0185 7.7254 -0.7532 0.0081 0.0101 4.1204 -0.3026
Hybridw/HK 0.0126 0.0037 1.9136 0.6517 0.0319 0.0157 3.6752 -0.0807 0.0578 0.0093 3.7288 -0.2433
RA 0.0062 0.0055 3.1063 -0.0687 0.0237 0.0120 2.9521 0.0811 0.0039 0.0017 3.0441 0.2666
Hybridw/RA 0.0117 0.0008 1.7829 0.7238 0.0221 0.0104 2.3326 0.4274 0.0376 0.0070 2.2353 0.6050
SJ 0.0064 0.0192 2.2994 0.2009 0.0209 0.0106 1.2739 0.6177 0.0411 0.0072 2.7778 0.4475
Hybridw/SJ 0.0098 0.0119 2.2789 0.6327 0.0203 0.0095 1.1896 0.6598 0.0076 0.0018 2.4564 0.5167
Lorenz 0.0131 0.0198 5.3049 -0.4657 0.0352 0.0172 1.1027 0.7329 0.0895 0.0094 2.8897 0.4387
Hybridw/Lorenz 0.0035 0.0116 2.9857 0.6103 0.0093 0.0147 1.0148 0.7576 0.0023 0.0079 2.5394 0.5055
Table3:Resultsofmacrosystemevaluation. Theaverageresultsof3runsarereported. Inthevastmajorityofcases,
hybridsystemsshowimprovementsacrossvariousaspectscomparedtoABMs. Boldpresentsthebestperformance
inthecolumn. UnderlineindicatesthemetricforthehybridmodeldidnotsurpassthatofthecorrespondingABM.
- Overall, the hybrid models outperform pure 0.016
ABMsintermsofbothstaticmeasuresandtime
0.012 seriesmeasures. Amongthemodels,thosebased
on the RA and Lorenz demonstrate advantages 0.008
acrossvariousdatasets,benefitingfromtheabil- 0.004
300 600 9001000
ityofRAandLorenzinmodelingsituationsof # of Agents
(a)
extremism(ChuangandRogers,2023).
- Hybrid models usually exhibit higher attitude
bias compared with the corresponding pure
ABMs. It’salsotheresultoftheLLMs’leaning
togeneratecontentwithclearstances. Withmore
agentsmodeledaspositivetowardsthetopic,the
overalllevelofattitudeisalsooverestimated.
- Takingadvantageoftheaccuratereplicationofat-
titudesofcoreusersempoweredbyLLMs,even
whenpureABMsfailtocapturetheoveralltrend
inattitudechanges,theoveralltrendcanbecor-
rectedinthehybridmodelsundertheguidance
ofthesepowerfulLLM-basedagents.
5.4 ScalabilityAnalysis
Figure 3depictstheperformanceandruntimevari-
ations observed in the Metoo experiment across
differentnumbersofagents. Forcomparativeanal-
ysis, we establish the real distribution of 1,000
agents in Sec. 5.3 as the reference and assess the
performanceofhybridmodelsfeaturing300core
usersalongsidevaryingnumbersofordinaryusers.
In Figure 3a, except for ∆ , all other metrics
Bias
exhibit only a slight decline as the proportion of
ordinaryusersincreases,indicatingthatasampling
simulationapproachcanyieldcompetitiveresults.
Figure 3billustratesthesimulationtimeratiowith
varyingnumbersofagentsrelativetothetimeinthe
mainexperimentwith1,000agents,wherethecore
users remain fixed at 300. Notably, the runtime
primarily depends on the time required for LLM
serusaeM
citatS
1.175
1.150 1.125
Bias Div. 1.100 DTW 1.075 Corr.
1.050
1.025
300 500 800 1000 5000 10000
# of Agents
(b)
oitaR
emiT
1.800
1.600
1.400 1.200
1.000
0.800
serusaeM
seireS
emiT
Figure 3: (a) System metrics when simulating with
varyingnumbersofagents(betterviewedincolor);(b)
RunningEfficiencywithvaryingnumbersofagents.
APIkeyinvocation,withscalingupthenumberof
ordinaryusershardlyimposingadditionalburden,
unlessthesimulationpopulationexceedsmillions,
whenfurtherengineeringenhancementsandhard-
wareoptimizationsbecomenecessary. Thisobser-
vationunderscoresthescalabilityofourmethod.
5.5 FurtherAnalysis
Wefurtherdiscussmoredetailsaboutthesimula-
tion of the LLM-empowered core users, offering
insightstoenhancecommunitycommunication.
5.5.1 ReplicationofEchoChambers
Weaimtoassesswhetherthesimulationcanrepli-
catetheechochamber,acommonphenomenonin
online social networks. We explore this question
fromtheperspectiveoftheconsumptionandpro-
duction of content (Garimella et al., 2018). The
contentofproductionisthecontentgeneratedby
theagents,whilethecontentofconsumptionisthat
generatedbyagentsthey“follow”. Thesimilarity
betweenproductionandconsumptionindicatesthe
users’tendencytoconsumecontentthatissimilar
to their own. Figure 4 reveals that as the number
ofepochsincreases,theaveragesimilarityshows
anoverallupwardtrend. Theseresultsvalidatethe
system’scapabilitytoreflecttheechochambers.
4796

0.96
0.95
0.94
0.93
0.92
2 4 6 8 10
Epochs
(a)
ytiralimiS
0.98
0.97
0.96
0.95
2 4 6 8 10
Epochs
(b)
ytiralimiS
versal framework, agents with slightly different
architectureshavebeenwidelyappliedinvarious
scenarios and applications. Among these works,
some are utilized for task-solving purposes, i.e.,
executing pre-defined tasks, such as software de-
velopment(Qianetal.,2023a,b;Hongetal.,2023),
collaboration(Chenetal.,2023),andexploringthe
worldinMinecraft(Wangetal.,2023a). Othersfo-
Figure4: (a)Similarityofcontentofconsumptionand
cusonsimulation,wherethereplicationofhuman
productiononMetoosimulation;(b)Similarityofcon-
behaviors is focused. Scenarios including social
tentofconsumptionandproductiononRoesimulation.
interaction, (Park et al., 2022; Liu et al., 2023)
BLMisnotreportedsinceitisapartialphrase.
recommendation(Wangetal.,2023c;Zhangetal.,
2023),theworldwar(Huaetal.,2023)andcommu-
Method Avg. Homogeneity Avg. Toxity
nicationgame(Xuetal.,2023)havebeenexplored
S1 0.8551 0.1426 toprovideinsightsoncommunication. Mostworks
S2 0.8580 0.1296 onlyrequireasmallnumberofagentsandhaven’t
S3 0.8962 0.1163 consideredscenariosrequiringlarge-scaleagents.
Table4:Resultsofsolutionstobreaktheechochambers.
6.2 SocialSimulation
Boldpresentsthebestperformanceinthecolumn.
Agent-basedmodelsforsocialsimulationonopin-
ion dynamics mainly focus on how individu-
5.5.2 Intervention: BreaktheEchoChambers
als change their attitudes due to others’ influ-
Giventhatechochambersoftencontributetopolar-
ence (Chuang and Rogers, 2023; Chuang et al.,
ization,weaimtoexplorestrategiestomitigatethis
2023). Thesemodelscanbedividedintodeductive
effectwhilesafeguardingusers’freedomofexpres-
ABMs and inductive ABMs. Represented by the
sion. We propose and test three solutions in our
BoundedConfidenceModel(Deffuantetal.,2000),
simulationframework: S1-Feedingtheopposite
theformercategoryisbasedonpsychology,such
opinions; S2 - Feeding the neutral opinions; S3 -
asthesocialjudgmenttheory(SherifandHovland,
Establishingpublicspacesfordebateordiscussion,
1961). By contrast, the latter often involves hu-
achieved by encouraging users to share opinions
man experiments, which are expensive and with
usingplatform-providedpublichashtags. Weexper-
limited scale. With ability in human-level intelli-
imentontheMetoodatasetandevaluatethehomo-
gence,LLM-empoweredagentshavepotentialto
geneityandtoxicityofdifferentsituations. Theho-
serveasasubstituteforhumansubjects. Parketal.
mogeneityismeasuredbythemethodinSec.5.5.1
andTörnbergetal. provideasimulationplatform
andthetoxicityismeasuredusingthePerspective
to help designers see beyond social interactions
API5.Table4illustratesthatallthreeapproaches
thatpeopleintendandimprovesocialinteraction.
canreducetheechochambers,buttheintroduction
Sotopia(Zhouetal.,2023)designsanevaluation
of opposing opinions can increase the toxicity of frameworkforsocialintelligence. S3 (Gaoetal.,
thecommunity,whileestablishingspacesforopen
2023) simulate public opinion through Markov
discussioncanpromotemorepeacefulexchanges.
ChainandLLMs,buthowtheydealwiththelarge
scaleofusersremainsambiguous.
6 RelatedWork
6.1 LLM-empoweredAutonomousAgents 7 Conclusion
With the prominent development of Large Lan-
Inthispaper,weproposeahybridframeworkfor
guageModels,theLLM-empoweredautonomous
social media user simulation. We empower core
agenthasrecentlygainedsignificantattention. In-
users and ordinary users with LLMs and ABMs,
tegratingprofile,memory,reflectionandplanning
and we provide a Twitter-like environment and a
modules, Park et al. design generative agents to
benchmarkSoMoSiMu-Benchforsimulationand
simulate the human daily life. Based on this uni-
evaluation. Experiment results demonstrate the
5https://developers.perspectiveapi.com/ effectivenessandflexibilityofourmethod.
4797

Acknowledgement Felix Brünker, Magdalena Wischnewski, Milad
Mirbabaie, and Judith Meinert. 2020. The role of
ThisworkissupportedbyNationalNaturalScience socialmediaduringsocialmovements–observations
FoundationofChina(No. 62176058)andNational fromthe#metoodebateontwitter.
KeyR&DProgramofChina(2023YFF1204800).
Rong-ChingChang,AshwinRao,QiankunZhong,Mag-
The project’s computational resources are sup-
dalena Wojcieszak, and Kristina Lerman. 2023. #
portedbyCFFFplatformofFudanUniversityand roeoverturned: Twitterdatasetontheabortionrights
thedatacollectingissupportedbyDBCloud. We controversy. In Proceedings of the International
AAAI Conference on Web and Social Media, vol-
would also like to thank the chairs and reviewers
ume17,pages997–1005.
fortheirconstructivefeedback.
Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang,
Limitations Chenfei Yuan, Chen Qian, Chi-Min Chan, Yujia
Qin, Yaxi Lu, Ruobing Xie, et al. 2023. Agent-
Our work is the first step towards a large-scale verse: Facilitatingmulti-agentcollaborationandex-
simulation implemented by a hybrid framework ploringemergentbehaviorsinagents. arXivpreprint
and it is limited in two aspects. In terms of data, arXiv:2308.10848.
although we have incorporated a larger number
Yun-Shiuan Chuang, Agam Goyal, Nikunj Harlalka,
ofagentsthanotherstudies, duetolimitationsin
SiddharthSuresh,RobertHawkins,SijiaYang,Dha-
annotationcosts,wehavenotyetvalidatedinterac- vanShah,JunjieHu,andTimothyTRogers.2023.
tionsamongmillionsofagents. IntermsofLLM- Simulatingopiniondynamicswithnetworksofllm-
basedagents. arXivpreprintarXiv:2311.09618.
empoweredagents,duetoreinforcementlearning
techniques, LLMs are also biased toward being
Yun-ShiuanChuangandTimothyTRogers.2023. Com-
morepolite,articulateandrespectfulthanuserson putationalagent-basedmodelsinopiniondynamics:
real-worldsocialmediaplatforms(Törnbergetal., Asurveyonsocialsimulationsandempiricalstudies.
arXivpreprintarXiv:2306.03446.
2023), bringing bias to our study. More careful
promptengineeringwillbeconsideredtosolvethis
IsraelCohen,YitengHuang,JingdongChen,JacobBen-
probleminfuturework. esty,JacobBenesty,JingdongChen,YitengHuang,
andIsraelCohen.2009. Pearsoncorrelationcoeffi-
EthicsStatement cient. Noisereductioninspeechprocessing,pages
1–4.
DataCollectionandPrivacy Ourdatacollection
GuillaumeDeffuant,FrédéricAmblard,GérardWeis-
isincompliancewithTwitter’stermsofserviceand
buch,andThierryFaure.2002. Howcanextremism
matches previous publications. Although tweets
prevail? astudybasedontherelativeagreementin-
arepublic,whenreleasingdata,wewillsharetweet teractionmodel. Journalofartificialsocietiesand
idratherthanrawdata,tominimizetheprivacyrisk. socialsimulation,5(4).
Furthermore,duringthesimulation,weanonymize
Guillaume Deffuant, David Neau, Frederic Amblard,
eachuserbyrenamingthem.
andGérardWeisbuch.2000. Mixingbeliefsamong
interacting agents. Advances in Complex Systems,
SimulationforSocialGood Thepurposeofthis
3(01n04):87–98.
paper is to use simulation to recreate the real sit-
uation of social movements and provide insights ChenGao,XiaochongLan,ZhihongLu,JinzhuMao,
forimprovingharmoniouscommunicationamong Jinghua Piao, Huandong Wang, Depeng Jin, and
YongLi.2023. S3: Social-networksimulationsys-
users. But it might also be misused to label peo-
temwithlargelanguagemodel-empoweredagents.
ple with a specific label that they do not want to
arXivpreprintarXiv:2307.14984.
be associated with. We suggest that when in use
the tools should be accompanied by descriptions Kiran Garimella, Gianmarco De Francisci Morales,
AristidesGionis,andMichaelMathioudakis.2018.
abouttheirlimitationsandimperfectperformance,
Politicaldiscourseonsocialmedia: Echochambers,
as well as allow users to opt out from being the
gatekeepers,andthepriceofbipartisanship. InPro-
subjectsofmeasurement. ceedings of the 2018 world wide web conference,
pages913–922.
MartinGestefeldandJanLorenz.2023. Calibratingan
References
opiniondynamicsmodeltoempiricalopiniondistri-
JonnyBentwood.2008. Distributedinfluence: Quanti- butionsandtransitions. JournalofArtificialSocieties
fyingtheimpactofsocial. andSocialSimulation,26(4).
4798

SalvatoreGiorgi,SharathChandraGuntuku,McKenzie Chen Qian, Xin Cong, Cheng Yang, Weize Chen,
Himelein-Wachowiak, AmyKwarteng, SyHwang, YushengSu,JuyuanXu,ZhiyuanLiu,andMaosong
MuhammadRahman,andBrendaCurtis.2022. Twit- Sun.2023a. Communicativeagentsforsoftwarede-
ter data of the #blacklivesmatter movement and velopment. arXivpreprintarXiv:2307.07924.
counterprotests: 2013to2021.
Chen Qian, Yufan Dang, Jiahao Li, Wei Liu, Weize
Chen, Cheng Yang, Zhiyuan Liu, and Maosong
Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng
Sun. 2023b. Experiential co-learning of software-
Cheng,JinlinWang,CeyaoZhang,ZiliWang,Steven
developingagents. arXivpreprintarXiv:2312.17025.
KaShingYau,ZijuanLin,LiyangZhou,etal.2023.
Metagpt:Metaprogrammingformulti-agentcollabo-
HegselmannRainerandUlrichKrause.2002. Opinion
rativeframework. arXivpreprintarXiv:2308.00352.
dynamicsandboundedconfidence: models,analysis
andsimulation.
Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei,
Jianchao Ji, Yingqiang Ge, Libby Hemphill, and HalimRaneandSumraSalem.2012. Socialmedia,so-
YongfengZhang.2023. Warandpeace(waragent): cialmovementsandthediffusionofideasinthearab
Largelanguagemodel-basedmulti-agentsimulation uprisings. Journalofinternationalcommunication,
ofworldwars. arXivpreprintarXiv:2311.17227. 18(1):97–111.
Shamik Roy and Dan Goldwasser. 2023. “a tale of
Joshua Conrad Jackson, David Rand, Kevin Lewis,
two movements’: Identifying and comparing per-
MichaelINorton,andKurtGray.2017. Agent-based
modeling: A guide for social psychologists. So- spectivesin#blacklivesmatterand#bluelivesmatter
cialPsychologicalandPersonalityScience,8(4):387– movements-relatedtweetsusingweaklysupervised
graph-basedstructuredprediction. InFindingsofthe
395.
AssociationforComputationalLinguistics: EMNLP
2023,pages10437–10467.
WanderJagerandFrédéricAmblard.2005. Uniformity,
bipolarizationandpluriformitycapturedasgeneric
ThomasCSchelling.2006. Micromotivesandmacrobe-
stylized behavior with an agent-based simulation
havior. WWNorton&Company.
modelofattitudechange. Computational&Mathe-
maticalOrganizationTheory,10:295–303. MuzaferSherifandCarlIHovland.1961. Socialjudg-
ment: Assimilationandcontrasteffectsincommuni-
RuiboLiu,RuixinYang,ChenyanJia,GeZhang,Denny cationandattitudechange.
Zhou, Andrew M Dai, Diyi Yang, and Soroush
Vosoughi.2023. Trainingsociallyalignedlanguage Ramine Tinati, Leslie Carr, Wendy Hall, and Jonny
modelsinsimulatedhumansociety. arXivpreprint Bentwood. 2012. Identifying communicator roles
arXiv:2305.16960. intwitter. InProceedingsofthe21stinternational
conferenceonWorldWideWeb,pages1161–1168.
Jan Lorenz, Martin Neumann, and Tobias Schröder.
Petter Törnberg, Diliara Valeeva, Justus Uitermark,
2021. Individualattitudechangeandsocietaldynam-
andChristopherBail.2023. Simulatingsocialme-
ics: Computationalexperimentswithpsychological
dia using large language models to evaluate al-
theories. PsychologicalReview,128(4):623.
ternative news feed algorithms. arXiv preprint
arXiv:2310.05984.
ZacharyMaiorana,PabloMoralesHenry,andJennifer
Weintraub.2020. #metooDigitalMediaCollection- Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
TwitterDataset. dlekar,ChaoweiXiao,YukeZhu,LinxiFan,andAn-
imaAnandkumar.2023a. Voyager: Anopen-ended
MeinardMüller.2007. Dynamictimewarping. Infor- embodiedagentwithlargelanguagemodels. arXiv
mationretrievalformusicandmotion,pages69–84. preprintarXiv:2305.16291.
LeiWang,ChenMa,XueyangFeng,ZeyuZhang,Hao
OpenAI.2023. Openaigpt3.5-turboapi.
Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai Tang,
XuChen,YankaiLin,etal.2023b. Asurveyonlarge
JoonSungPark,JosephO’Brien,CarrieJunCai,Mered-
language model based autonomous agents. arXiv
ithRingelMorris,PercyLiang,andMichaelSBern-
preprintarXiv:2308.11432.
stein.2023. Generativeagents: Interactivesimulacra
ofhumanbehavior. InProceedingsofthe36thAn-
LeiWang,JingsenZhang,XuChen,YankaiLin,Rui-
nual ACM Symposium on User Interface Software
huaSong,WayneXinZhao,andJi-RongWen.2023c.
andTechnology,pages1–22.
Recagent: Anovelsimulationparadigmforrecom-
mendersystems. arXivpreprintarXiv:2306.02552.
JoonSungPark,LindsayPopowski,CarrieCai,Mered-
ithRingelMorris,PercyLiang,andMichaelSBern- ZhihengXi,WenxiangChen,XinGuo,WeiHe,Yiwen
stein. 2022. Social simulacra: Creating populated Ding, Boyang Hong, Ming Zhang, Junzhe Wang,
prototypesforsocialcomputingsystems. InProceed- Senjie Jin, Enyu Zhou, et al. 2023. The rise and
ings of the 35th Annual ACM Symposium on User potential of large language model based agents: A
InterfaceSoftwareandTechnology,pages1–18. survey. arXivpreprintarXiv:2309.07864.
4799

Yuzhuang Xu, Shuo Wang, Peng Li, Fuwen Luo, Xi- A Agent-basedModels
aolong Wang, Weidong Liu, and Yang Liu. 2023.
Exploring large language models for communica- Inthissection,wepresenttheagent-basedmodels
tiongames: Anempiricalstudyonwerewolf. arXiv based on different psychological theories in de-
preprintarXiv:2309.04658.
tail,followingtheunifiedformulationproposedby
AnZhang,LehengSheng,YuxinChen,HaoLi,Yang ChuangandRogers(2023). Assumethatthereare
Deng,XiangWang,andTat-SengChua.2023. On N agentswithindexi 1,2,...,N inasystem
∈ { }
generativeagentsinrecommendation. arXivpreprint I , where each agent has an attitude toward
system
arXiv:2310.10108.
the same topic. Let a be the attitude score of
i,t
XuhuiZhou,HaoZhu,LeenaMathur,RuohongZhang, agentiattimet,J i,t bethesetofagentsthatwill
HaofeiYu,ZhengyangQi,Louis-PhilippeMorency, influenceagentiattimet,m bethemessagethat
j,t
Yonatan Bisk, Daniel Fried, Graham Neubig, et al.
agentj conveytootheragentsattimet.
2023. Sotopia: Interactive evaluation for social
intelligence in language agents. arXiv preprint
A.1 BoundedConfidenceModel(BC)
arXiv:2310.11667.
Thebounded-confidence(BC)modelwasproposed
by (Deffuant et al., 2000). It assumes that when
the message m is close enough to the agent i’s
j,t
attitude a , the message exerts an assimilation
i,t
forceontheagent’sattitude.
Update Function The attitude update function
is:
∆a = α sim(a ,m ) (a a ), (3)
i,t i i,t j,t j,t i,t
· · −
where
1, if a a < ε
sim(a i,t ,m j,t ) = 0 | , o j, t t h − erw i i , s t e | i ,
(cid:26)
(4)
SelectionFunction Theselectionfunctionis:
J =f (i,t) = onerandomagentj
i,t select
{
inthesystemwithintheconfidencebound,
i.e.,whose a a < ε , exceptthe
j,t i,t i
| − |
agentiitself ,
}
(5)
wherethenumberofsourceagentsissettoN =
J
1.
MessageFunction Themessagefunctionis:
m = f (a ) = a , (6)
j,t message j,t j,t
OtherAssumptions α i [0,1]
∈
A.2 BoundedConfidenceModel-Multiple
(HK)
Rainer and Krause (2002)’s bounded confidence
modelisanextensionoftheboundedconfidence
model,whereitcanhandlemultiplesourceagents,
i.e.,1 <= N <= N.
J
4800

UpdateFunction Theupdatefunctionis: h i,j istheoverlapbetweenseg i,t andseg j,t . The
termh /u isreferredtoastherelativeagreement
N 1 i,j j
∆a i,t =
εi
oftheagentj withtheagenti.
(N +1) · (N )
εi εi
(7)
sim(a ,a ) (a a ), SelectionFunction Theselectionfunctionis:
i,t j,t i,t j,t
· · −
j X∈ Ji,t J i,t =f select (i,t) = onerandomagentj in
{
where I ,excepttheagentiitself},
system
1, if a a < ε (13)
sim(a i,t ,m j,t ) = 0 | , o j, t t h − erw i i , s t e | i ,
(cid:26) MessageFunction Themessagefunctionis:
(8)
m = f ([a u ,a +u ])
ε istheconfidencebound,N isthenumberof j,t message j,t j,t j,t j,t
i εi − (14)
agentswithintheconfidencebound. = [a j,t u j,t ,a j,t +u j,t ],
−
SelectionFunction Theselectionfunctionis: OtherAssumptions α i [0,1].
∈
J =f (i,t) = I i = {alltheN
i,t select system
\{ } A.4 SocialJudgementModel(SJ)
agentsinthesystemexcepttheagenti ,
} The social judgment (SJ) model differs from the
(9)
bounded confidence model in that it additionally
Notethatonlythosewithintheconfidencebound includesarepulsionforce. Itassumesthatanagent
influencetheagenti’sattitude. will assimilate towards the message m if it is
j,t
closeenoughtoitsattitudea ,andwilldistance
MessageFunction Themessagefunctionis: i,t
away from the message if it is too far away from
m = f (a ) = a , (10) itsattitude.
j,t message j,t j,t
Other Assumptions The strength of the social Update Function The attitude update function
influenceisafunctionofthenumberofagentsin is:
theconfidencebound,i.e.,α (N ) =
Nεi
.
i εi (Nεi +1) ∆a
i,t
=α
i
·
[sim(a
i,t
,m
j,t
)
·
(a
j,t
−
a
i,t
)
(15)
+rep(a ,m )],
A.3 RelativeAgreementModel(RA) i,t j,t
The relative agreement (RA) model extends the where
bounded confidence model in that the similarity
sim(a ,a ) (a a ) =
bias asm(a ,m ) is a continuously decaying i,t j,t j,t i,t
i,t j,t · −
function. The RA model assumes that the more (a a ),
j,t − i,t (16)
themessagem agreeswitha ,themoresuscep- if a a < u ,
j,t i,t j,t i,t i
 | − |
tibletheagentiistoitsassimilationforce. 0,otherwise

IntheRAmodel,thereisanuncertaintyu > 0
i,t

around each agent’s attitude a . Therefore, the
i,t
(a a ),
agenti’sattitudeismodeledasasegmentseg
i,t
=
−
j,t
−
i,t
rep(a ,a ) = if a a > t , (17)
[a i,t u i,t ,a i,t +u i,t ]. When agent j influences i,t j,t  | j,t − i,t | i
− 0, otherwise
theagenti,thelargertheirsegments"agree",the 
largertheinfluenceshouldbe.
u andt specifythelatitudeofacceptanceand
i i
UpdateFunction Theupdatefunctionis: thelatitudeofrejection,respectively.
∆a = α sim(a ,u ,a ,u ) (a a ), SelectionFunction Theselectionfunctionis:
i,t i i,t i,t j,t j,t i,t j,t
· · −
(11)
J =f (i,t) = onerandomagentj in
i,t select
{
where I ,excepttheagentiitself},
system
(h /u ) 1, (18)
i,j j
−
sim(a ,u ,a ,u ) = if (h /u ) > 1 ,
i,t i,t j,t j,t i,j j
 MessageFunction Themessagefunctionis:
0, otherwise

(12)
m = f (a ) = a , (19)
 j,t message j,t j,t
4801

Figure5: Thedataprocessingprocess.
OtherAssumptions α i [0,1]. SelectionFunction Theselectionfunctionis:
∈
J =f (i,t) = onerandomagentj inI
A.5 LorenzModel i,t select system
,excepttheagentiitself},
Lorenz et al. (2021) proposed a model which in- (cid:8)
cludesassimilationforce,reinforcementforce,sim- (25)
ilaritybias,polarizationfactor,andsourcecredibil-
MessageFunction Themessagefunctionis:
ity.
m = f (a ) = a , (26)
Update Function The attitude update function j,t message j,t j,t
is:
B DataCollection
∆a =α s(i,j)pol(a )sim(a ,m )
i,t i i,t i,t j,t
[ρ asm(a ,m )+(1 ρ) ref(m )],
i,t j,t j,t
· · − ·
B.1 TweetsofSocialMovements
(20)
We get tweet ids of the three social movements
wherethepolarizationfactoris: from Maiorana et al., Chang et al. and (Giorgi
et al., 2022), andcrawl those duringthe required
M2 a 2
pol(a ) = − i,t , (21) event periods. Overall, a total of 4,985,000,
i,t M2
22,869,406, and 25,112,678 tweets were col-
ThehyperparameterparameterM isthetheoretical lected. Subsequently, we sample users described
boundaryfortheattitudespace. Thesimilaritybias inSec.4.1fromtheauthorsofthesetweets. After
is: collectingthesedata,thepost-processingprocess
isshowninFigure 5.
λk
sim(a ,m ) = , (22)
i,t j,t λk + m a k B.2 ProfileConstruction
j,t i,t
| − |
AsmentionedinSec.3.1.1,weincludedemograph-
The hyperparameters λ and k specify the shape ics, social traits and communication roles in the
ofthesimilaritybiasfunction. Thereinforcement profile of each agent. We construct profiles from
forceis: thebiosandtweetsofTwitterusers.
ref(m ) = m , (23) Demographics In order to minimize the noise
j,t j,t
causedbyannotating,wefirstidentifygender,po-
Theassimilationforceis: litical leaning and account type from one’s bio
using regular expression with strict rules. Then,
asm(a ,m ) = (m a ), (24) wepromptGPT-3.5-Turbo-0613toinferthosecan
i,t j,t j,t i,t
−
4802

not be directly matched. The candidate list for PromptforProfileGeneration
account type was acquired from (Brünker et al.,
Given the following observation about
2020): [Journalist,PrivatePerson,Celebrity,Me-
anindividual{name},pleasesummarize
dia Organization, Activist, Politician, Social Bot,
therelevantdetailsfromtheprofile. His
NGO,InternationalOrganization,Company,Gov-
orherprofileinformationisasfollows:
ernmentalOrganization,SuspendedAccounts].
Social Traits The activity level and influence Name: {name}
level are measured by the number of tweets and Gender: {gender}
number of followers for each user. We follow PoliticalLeaning: {ideo}
(Zhang et al., 2023) to allocate the social trait of ActivityLevel: {activity}
activity and influence to each user based on the InfluenceLevel: {influence}
ascendingorderofthemeasurementwitharatioof Feature: {commu_role}
6:3:1. Theactivitylevelsinclude[notactive,mod- AccountType: {account_type}
erately active, highly activity] and the influence ShortBio: {bio}
levelsinclude[notinfluential,moderatelyinfluen- Aselectionofpostedtweets: {tweets}
tial,highlyinfluential]. You can deduce the preferences and
personalityfromthebioandtweets,but
CommunicationRole Weidentifythecommuni-
pleaseavoidrepeatingtheobservationin
cationrolesofeachuserbycalculatingthemetrics
thesummary.
proposedby (Tinatietal.,2012)and (Bentwood,
Summary:
2008). Then,weassigncorrespondingdescriptions
oftheroleswhengeneratingprofilesofusers.
B.3 AnnotationofUser-generatedContent
• IdeaStarter: Startaconversationalmeme,and
Weannotatethestanceandcontenttypeexpressed
tendtobehighlyengagedwiththemediaand
inusers’tweetsandsimulatedcontentusingGPT-
postoriginalcontent.
3.5-Turbo-0613withtemperaturesetto0:
• Amplifier: Collect multiple thoughts and
PromptforContentAnnotation
share ideas and opinions. Enjoy being the
firstonetoretweetoriginalcontent.
Please classify the text into one of the
followingcategoriesbasedonitscontent.
• Curator: Useabroadercontexttodefineideas.
Onlyoutputyourchoice.
Tendtotakeideasofothersandeithervalidate,
question,challenge,ordismissthem. Tendto
1. call for action: tweet contained
bethetiesthatformbetweenothers,aggregat-
a call for action (e.g. requesting, chal-
ingideastogethertohelpclarifyandsteerthe
lenging,promoting,inviting,summoning
topicofconversation.
someonetodosomething).
• Commentator: Detailandrefineideas. Take 2. testimony: tweet contained a
partinsomethingtowhichheorshestrongly testimony of the victim (e.g. report,
feelsabout. Wanttoshareinformationnotfor declaration,first-personexperience).
self-benefit. 3. sharing of opinion: e.g. evaluation,
appreciation, addition, analysis of
• Viewer: Takeapassiveinterestintheconver- opinions.
sation. Leavefootprintbyviewingratherthan 4. reference to a third party: reporting
contributingtotheconversation. Prefertocon- on something/-one, direct and indirect
sumeinformationratherthancreateorshare quotes.
informationonline. 5. other: othercontentthatdoesnotfall
intotheabovecategories.
After acquiring the attributes of the user, we
promptGPT-3.5-Turbo-0613torephrasetheprofile
Text: {text}
usingnaturallanguages. Theprompttemplateisas
Answer:
follows:
4803

Dataset Size Stance Content Behavior Algorithm 1 Single-round Simulation for Core
Metoo 2,214 2,166:33:15 89:78:67:1,792:188 422:1,792 UserBehaviorReplication
Roe 3,595 3,528:29:38 48:6:72:3,362:107 233:3,362
1: Inputs: CoreusersU andcorrespondingreal
BLM 971 934:33:4 31:10:20:887:23 84:887
contextsC,sizeof(user,context)pairsN
Table5: DescriptionofDatasetforMicro-levelAlign- 2: Outputs: Predictedbehaviorofeachagentfor
mentEvaluation. Stancecolumnindicatesthedistribu- usersU
tion of support, neutral and oppose; Content column
3: Initializeagents:
indicatesthedistributionofcallforaction,testimony,
4: foriin1toN do
sharingofopinion,referencetoathirdpartyandother;
Behave column indicates the distribution of post and 5: Assigntheprofileofuseru i toitsagent
retweet. 6: endfor
7: Simulate:
8: foriin1toN do
PromptforStanceAnnotation 9: agentu i generatesresponsebasedonitspro-
fileandcontextc
What’s the author’s stance on {target}? i
10: endfor
Please choose from Support, Neutral,
11: return simulatedresponseofeach(user,con-
andOppose. Onlyoutputyourchoice.
text)pair
Text: {text}
Stance:
to 256 and temperature set to 0 for more deter-
ministicresults. WerunthesimulatoronaLinux
serverwithasingleNVIDIAGeForceRTX4090
B.4 Micro-levelDatasetDescription
24GBGPUandanIntel(R)Xeon(R)Gold6226R
CPU. The average cost for the whole simulation
Whenpreparingmicro-level(user,context)sam-
for an event is around 20-30 dollars. (Note that
ples, we randomly sample from the datasets, in-
thecostwasestimatedwhenGPT-3.5-Turbopoints
stead of using the whole dataset to reduce cost.
toGPT-3.5-Turbo-0613,sothecostsmayincrease
Whensampling,wesetsomerulestoremovethose
now since GPT-3.5-Turbo-0613 becomes one of
difficult or ambiguous for LLMs to annotate: (1)
theoldermodels). Foreachevent,wesimulate14
Weremovesampleswhosegroundtruthresponse
steps, with the step size estimated by calculating
tweets have fewer than 10 words after removing
theaveragepostingintervalofusersintheempir-
hashtagsandURLs. (2)Weremovetweetsthatare
ical data. For the validation of pure ABMs, we
merelydirectrepostsofnewsarticleswithoutex-
reporttheaverageresultsof10runs. Forthevalida-
pressingtheiropinions. Asaresult,wegotdatasets
tionofhybridmodels,wesimulateonceandkeep
for micro-level alignment shown in Table 5. We
thegeneratedcontentofcoreuseagentstorunthe
havemanuallyreviewed100randomsamplesfor
hybrid systems 10 times and report the average
eachlabelcategoryandfoundtheGPTannotation
results.
consistencytobe0.93and0.92forstanceandcon-
tentrespectively. C.3 PromptandResponseExampleforCore
UserAgent
C SimulationDetails
PromptExampleofCoreUsersinMetoo
C.1 SimulationProcess Movement.
Thesimulationprocessesformicro-leveluserbe-
You are using the social media Twitter.
haviorreplicationandmacro-levelopiniondynam-
You might need to perform reaction to
icsmodelingareshowninAlgorithm1andAlgo-
the observation. You need to answer
rithm2respectively.
what you will do to the observations
basedonthefollowinginformation:
C.2 SimulationSettings
(1) You are e***1. e***1 is a highly
For all the experiments, we use GPT-3.5-Turbo-
active and influential activist on social
0613 to simulate core users, with max tokens set
4804

media. e***1 enjoys collecting and
sharing ideas and opinions, often being
thefirsttodoso. e***1tendstovalidate,
question,challenge,ordismisstheideas
of others and help clarify and steer
conversations. e***1’s bio includes
Algorithm2Multi-roundSimulationforOpinion hashtags and affiliations related to
DynamicsForecasting progressive causes such as supporting
1: Inputs: CoreusersUc andordinaryusersUo Joe Biden and Kamala Harris, Black
Lives Matter, LGBTQ+ rights, and
2: Outputs: Attitude scores for each agent of
usersinUc andUo,attime1toT resistance against oppressive systems.
e***1hasretweetedpostsaboutmeeting
3: Initializeagents:
4: foreachuseragentiin1toUc do Kamala Harris, hiring Mary to score a
5: Assigntheprofileofuseruc toitsagent film, criticizing Senator Ron Johnson,
i
recommending Neal Katyal for a case,
6: Setinitialattitudescorea i,t
andexpressingexcitementforthefuture
7: Setvisibleagentsetaccordingtotheauthen-
ofImpact.
ticsocialnetworks
(2)Currenttimeis2018-01-0712:00:00
8: endfor
9: foreachuseragentj in1toUo do (3)Thenewsyougotis"AttheGolden
GlobesAwardsceremonyinLosAngeles,
10: Setinitialattitudescorea j,t
mostguestsshowedupdressedinblack
11: endfor
out of solidarity with the MeToo and
12: Simulatecontinuousinteractions:
Time’sUpmovementandthevictimsof
13: foreachtimestepin1toT do
14: foreachuseragentiin1toUc do sexualviolence."
(4) Your personal experience is e***1
15: Manipulatethememorybyreflectingand
leanstowardssupportingcandidateswho
retrievingrelevantmemory
prioritizehumanrights,opposepotential
16: Generateresponser i,t basedonitsprofile,
national abortion bans, and criticize
memory, triggering news, Twitter page
somegovernmentactions.
andnotificationsattimet
(5) Your recent memory is [g***n]:
17: Update the attitude score a i,t according
g***nrepliesto[G***s]: Iapplaudthe
tor
i,t
guests at the Golden Globes for using
18: Manipulatethememorybywritingobser-
theirplatformtosupporttheMeTooand
vations
Time’s Up movement. It’s important to
19: endfor
20: foreachuseragentj in1toUo do continueraisingawarenessaboutsexual
violence. #GoldenGlobes #MeToo
21: Select the set of agents to interact with
#TimesUp.
A throughtheselectionfunction
j,t
[s***e]: s***e replies to [C***N]: It’s
22: Update the attitude score a j,t based on
disappointing to see President Trump
theupdatefunctionandattitudescoresof
endorsing someone accused of sexual
agentsinA
j,t
misconduct. We need leaders who take
23: endfor
theseallegationsseriously. #MeToo.
24: endfor
[j***3]: j***3 replies to [C***N]: It’s
25: return Attitudescoresforeachagentofusers
inUc andUo,attime1toT concerning that President Trump en-
dorsedRoyMooredespitetheallegations
ofsexualmisconductagainsthim. This
sends a message that such behavior is
acceptable. #MeToo#TimesUp.
[e***1]: e***1likesatweetof[w***r]:
’PresidentTrump’sendorsementofRoy
4805

Moore, accused of sexual misconduct, #MeToo #TimesUp –Post Time: 2018-
is deeply troubling. It undermines the 01-0620:00:00
fight against sexual violence and the (7)Thenotificationsyoucanseeare
valuesoftheMeToomovement. #MeToo
#TimesUp’. In terms of how you actually per-
[T***x]: The solidarity shown at the form the action, you take action by
Golden Globes Awards ceremony in callingfunctions. Currently,therearethe
support of the MeToo and Time’s Up followingfunctionsthatcanbecalled.
movement is inspiring. Let’s keep the - do_nothing(): Do nothing. There is
conversation going and work towards nothingthatyouliketorespondto.
a more inclusive and equal society. -post(content): Postatweet. ‘content‘is
#MeToo#TimesUp thesentencethatyouwillpost.
(6) The twitter page you can see is - retweet(content, author, origi-
tweet id: 356 [T***x]: The solidarity nal_tweet_id, original_tweet). Retweet
shown at the Golden Globes Awards orquoteanexistingtweetinyourTwitter
ceremony in support of the MeToo and page. ‘content‘ is the statements that
Time’sUpmovementisinspiring. Let’s youattachwhenretweeting. Ifyouwant
keep the conversation going and work to say nothing, set ‘content‘ to None.
towards a more inclusive and equal ‘author‘ is the author of the tweet that
society. #MeToo#TimesUp–PostTime: you want to retweet, it should be the
2018-01-0704:00:00 concretename. ‘original_tweet_id‘and
tweet id: 244 [w***r]: President ‘original_tweet‘aretheidandcontentof
Trump’s endorsement of Roy Moore, theretweetedtweet.
accusedofsexualmisconduct,isdeeply - reply(content, author, origi-
troubling. Itunderminesthefightagainst nal_tweet_id). Replytoanexistingtweet
sexual violence and the values of the in your Twitter page or reply one of
MeToo movement. #MeToo #TimesUp replies in your notifications, but don’t
–PostTime: 2018-01-0620:00:00 reply to yourself and those not in your
tweet id: 132 [T***x]: I applaud the Twitter page. ‘content‘ is what you
guestsattheGoldenGlobesforstanding will reply to the original tweet or other
insolidaritywiththeMeTooandTime’s comments. ‘author‘ is the author of the
Upmovement. It’simportanttosupport originaltweetorcommentthatyouwant
thevictimsofsexualviolenceandwork toreplyto. ‘original_tweet_id‘istheid
towards a safer and more equal society. oftheoriginaltweet.
#GoldenGlobes #MeToo #TimesUp - like(author, original_tweet_id). Press
–PostTime: 2018-01-0620:00:00 likeonanexistingtweetinyourTwitter
tweet id: 129 [e***1]: It’s inspiring page. ‘author‘ is the author of the
to see the guests at the Golden Globes original tweet that you like. ‘origi-
Awards ceremony showing solidarity nal_tweet_id‘ is the id of the original
with the MeToo and Time’s Up move- tweet.
ment. Thisisanimportantsteptowards
ending sexual violence and creating Call one function at a time, please
a safer world for everyone. #MeToo give a thought before calling these
#TimesUp #GoldenGlobes –Post Time: actions, i.e., use the following format
2018-01-0620:00:00 strictly:
tweetid: 72[r***7]: PresidentTrump’s
endorsement of Roy Moore, despite [OPTION1]
the allegations of sexual misconduct, Thought: Noneoftheobservationattract
is deeply troubling. We must hold our myattention,Ineedto:
leaders accountable for their actions. Action: do_nothing()
4806

Dataset Models alpha bc_bound init_uct acc_thred rej_thred lambda k tho
BC 0.10 0.30 - - - - - -
[OPTION2] HK 0.25 0.10 - - - - - -
Metoo RA 0.30 - 0.20 - - - - -
Thought: dueto‘xxx‘,Ineedto: SJ 0.15 - - 0.10 0.90 - - -
Lorenz 0.10 - - - - 1.00 2.00 0.90
Action: post(content="yyy") BC 0.15 0.10 - - - - - -
HK 0.25 0.10 - - - - - -
Roe RA 0.10 - 0.20 - - - - -
SJ 0.30 - - 0.10 1.90 - - -
Lorenz 0.10 - - - - 2.00 10.00 0.50
[OPTION3] BC 0.15 0.10 - - - - - -
HK 0.10 0.10 - - - - - -
Thought: dueto‘xxx‘,Ineedto: BLM RA 0.10 - 0.20 - - - - -
SJ 0.20 - - 0.50 1.50 - - -
Lorenz 0.10 - - - - 2.00 2.00 0.30
Action: retweet(content="yyy", au-
thor="zzz", original_tweet_id="0", Table 6: Calibrated parameters of the ABMs. “-” de-
original_tweet="kkk") notesnon-applicableparameters.
[OPTION4] Datasets Stance Content Behavior
Acc. F1 MAE Acc. F1 Sim. Acc. F1
Thought: dueto‘xxx‘,Ineedto:
Metoo 0.9679 0.3400 0.2311 0.7010 0.1988 0.8064 0.7313 0.5212
Action: reply(content="yyy", au- w/osoc. 0.9630 0.2720 0.2344 0.6671 0.1915 0.8016 0.7019 0.5136
w/ocom. 0.9535 0.3393 0.2299 0.6671 0.1960 0.8027 0.7010 0.5128
thor="zzz",original_tweet_id="0") Roe 0.9430 0.3361 0.2058 0.6423 0.1957 0.8090 0.6665 0.4691
w/osoc. 0.9302 0.3214 0.1914 0.6120 0.1895 0.8062 0.6403 0.4645
w/ocom. 0.9193 0.3229 0.2170 0.5839 0.1826 0.8082 0.6106 0.4494
[OPTION5] BLM 0.8991 0.3735 0.1627 0.7353 0.2218 0.8406 0.7796 0.5759
w/osoc. 0.8679 0.3692 0.1800 0.6220 0.1814 0.7703 0.7570 0.5217
Thought: dueto‘xxx‘,Ineedto: w/ocom. 0.8805 0.3839 0.1856 0.7281 0.2075 0.8235 0.7734 0.5663
Action: like(author="zzz", origi-
Table7: Resultsofablationstudy.
nal_tweet_id="1")
Now begin your actions. Remem- thedataofE1orP1foreachmovement,wherewe
ber only write one function call after runthemodelswitheachparametercombination5
‘Action:‘. timesandrecordtheaverageresult. Theparameter
Based on the above history, what will combination with the lowest ∆Bias and ∆Div.
you,e***1,donext? is retained. The parameter combinations used in
pureABMsandourhybridmodelsareillustrated
inTable6. Theexplanationsofeachparameteris
asfollows:
Response Example of Core Users in
MetooMovement.
- alpha: the strength of the social influence of
Thought: The observation about the sourceagents;
solidarity shown at the Golden Globes
- bc_bound: theconfidenceboundoftheagentsin
insupportoftheMeTooandTime’sUp
theBoundedConfidenceModels;
movement aligns with my progressive
- init_uct: the uncertainty term in the Relative
valuesandinterests.
AgreementModel;
Action: retweet(content=None, au-
thor="T***x",original_tweet_id="356", - acc_thred: the threshold for the latitude of ac-
original_tweet="The solidarity shown ceptance of the agents in the Social Judgement
attheGoldenGlobesAwardsceremony Model;
insupportoftheMeTooandTime’sUp - rej_thred: thethresholdforthelatitudeofrejec-
movement is inspiring. Let’s keep the tionoftheagentsintheSocialJudgementModel;
conversation going and work towards
- lambda: hyperparameterspecifyingtheshapeof
a more inclusive and equal society.
thesimilaritybiasfunctionintheLorenzModel;
#MeToo#TimesUp")
- k: hyperparameter specifying the shape of the
similaritybiasfunctionintheLorenzModel;
- tho: the degree of assimilation, which controls
C.4 ParametersofABMs
therelativecontributionoftheassimilationforce
versus the reinforcement force in the Lorenz
As mentioned in Sec. 4.3, we find the best pa- Model.
rameter combinations by parameter sweeping on
4807

Metoo Roe BLM
Method temp.
∆Bias↓ ∆Div.↓ DTW↓ Corr.↑ ∆Bias↓ ∆Div.↓ DTW↓ Corr.↑ ∆Bias↓ ∆Div.↓ DTW↓ Corr.↑
0 0.0135 0.0108 1.8440 0.7043 0.0239 0.0121 2.4611 0.3607 0.0300 0.0069 3.9254 0.1248
Hybridw/BC
1 0.0160 0.0145 3.2916 0.4363 0.0229 0.0030 3.6380 0.2041 0.0290 0.0046 3.5227 -0.0838
0 0.0126 0.0037 1.9136 0.6517 0.0319 0.0157 3.6752 -0.0807 0.0578 0.0093 3.7288 -0.2433
Hybridw/HK
1 0.0131 0.0091 3.4085 0.3111 0.0334 0.0057 6.1835 -0.4999 0.0410 0.0071 4.5660 -0.2447
0 0.0117 0.0008 1.7829 0.7238 0.0221 0.0104 2.3326 0.4274 0.0376 0.0070 2.2353 0.6050
Hybridw/RA
1 0.0116 0.0042 3.1318 0.4829 0.0207 0.0016 2.8546 0.5260 0.0257 0.0035 2.5903 0.6009
0 0.0098 0.0119 2.2789 0.6327 0.0203 0.0095 1.1896 0.6598 0.0076 0.0018 2.4564 0.5167
Hybridw/SJ
1 0.0107 0.0180 2.9388 0.5447 0.0188 0.0080 2.5737 0.7047 0.0034 0.0037 3.4908 0.5333
0 0.0035 0.0116 2.9857 0.6103 0.0093 0.0147 1.0148 0.7576 0.0023 0.0079 2.5394 0.5055
Hybridw/Lorenz
1 0.0013 0.0158 2.3384 0.5796 0.0148 0.0052 0.9340 0.8765 0.0154 0.0049 3.2131 0.5038
Table8: ResultsofmacrosystemevaluationwithLLM-empoweredagents’temperaturesetto0and1.
D SimulationResults choose to retweet, although we have em-
phasized that it is news that can not be
D.1 AblationStudy
retweeted directly. This could be related to
Tovalidatetheeffectivenessoftheproposedcom- theinstruction-followingabilityofLLMs. We
ponentsintheLLMagentprofilemodule,wecon- believe fine-tuning LLMs with social media
duct an ablation study on the micro-level align- userdatawouldmitigatethisproblem.
ment of core users, where the social traits (soc.)
andcommunicationroles(com.) areexcluded. Ta- • Repeat retweeting itself: sometimes the
ble7showsthatalltheseelementscontributetothe agentsrepeatretweetingthemselvesforcon-
alignmentoftheusers. secutive steps. This results from the limited
context of agents in simulation, where the
D.2 TheInfluenceofTemperature mostseveresituationisthattherearenopeo-
We test different temperatures for the generation ple an agent follows in the subgraph, so the
ofcoreuseragents,tohelptradeoffthecertainty signalsitreceivesarelimited. Therootcause
and diversity of the generation results. Table 8 ofthisproblemisthattherealusercontextis
showstheresultsofthemacrosystemevaluation muchmorecomplexthanthatinsimulation,
whenthetemperatureofLLMsissetto0(inour withmoreinformationsourcesfromdifferent
main experiments) and 1. The results show that channelsevenoutsideTwitter,soreproducing
thetemperatureparameterinfluencingthegenera- realbehaviorsischallenging.
tioncontentofcoreuseragentscanmakeahuge
difference to the systematic results. Among all
thecandidates,hybridmodelswithSJandLorenz
modelsshowthebestrobustnessonthetimeseries
metrics.
D.3 VisualizationofCollectiveResults
We observe the simulated systematical outcomes
at the macro level. Figure 6 shows examples of
thesimulatedresultsandtheircorrespondingtrue
situations.
D.4 ErrorAnalysis
Inthissection,wepresenttheerrorsandbiasinthe
simulation.
UnintendedBehavior Duringthesimulation,we
observedsomeunintendedbehaviorsgeneratedby
coreuseragents:
• Retweet non-tweet news: sometimes the
agents mistake the news as a "tweet" and
4808

Figure6: Examplesofcollectiveresults. (a)ExampleofthesimulationresultsofHybridw/BC(temperature=0)
onMetoomovement. SincetheempiricaldatacontainsadiscussionaboutDonaldTrump’sendorsementofRoy
Moore, wealsoincludethisbackgroundinformationwiththenewsoftheTime’sUpmovementattheGolden
GlobesAwardsceremony. (b)ExampleofthesimulationresultsofHybridw/Lorenz(temperature=1)onRoe
movement. (c)ExampleofthesimulationresultsofHybridw/RA(temperature=0)onBLMmovement.
4809
