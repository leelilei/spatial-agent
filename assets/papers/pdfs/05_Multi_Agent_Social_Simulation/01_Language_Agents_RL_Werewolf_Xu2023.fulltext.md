Title: Language Agents with Reinforcement Learning for Strategic Play in the Werewolf Game

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/05_Multi_Agent_Social_Simulation/01_Language_Agents_RL_Werewolf_Xu2023.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:07:06+00:00
- page_count: 31
- status: ok
- text_char_count: 109180

Metadata:
- author: Zelai Xu; Chao Yu; Fei Fang; Yu Wang; Yi Wu
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

5202
yaM
92
]IA.sc[
4v04981.0132:viXra
Language Agents with Reinforcement Learning for
Strategic Play in the Werewolf Game
ZelaiXu1 ChaoYu1 FeiFang2 YuWang*1 YiWu*13
Abstract Prompt
You are playing the Rock-Paper-Scissors game. You should first reason
Agentsbuiltwithlargelanguagemodels(LLMs)
about the Nash equilibrium of this game, and then choose one action
haveshowngreatpotentialacrossawiderangeof from Rock, Paper, and Scissors based on your reasoning.
domains. However,incomplexdecision-making
Reasoning
tasks,pureLLM-basedagentstendtoexhibitin-
trinsicbiasintheirchoiceofactions,whichisin- In the Rock-Paper-Scissors game, the Nash equilibrium occurs when
heritedfromthemodel’strainingdataandresults each player is randomly choosing their action with equal probability,
making it impossible for the other player to predict or gain an
insuboptimalperformance. Todevelopstrategic
advantage based on patterns. Thus, the strategy is to play each of
languageagents,i.e.,agentsthatgenerateflexi- Rock, Paper, and Scissorswithaprobabilityof1/3foreachchoice.
blelanguageactionsandpossessstrongdecision-
makingabilities,weproposeanovelframework Action Distribution
that powers LLM-based agents with reinforce-
ment learning (RL). We consider Werewolf, a
popularsocialdeductiongame,asachallenging
testbedthatemphasizesversatilecommunication
andstrategicgameplay. Tomitigatetheintrinsic
biasinlanguageactions,ouragentsuseanLLM
toperformdeductivereasoningandgenerateadi-
versesetofactioncandidates. ThenanRLpolicy
Figure1: Theintrinsicbiasintheactiondistributionofpure
trained to optimize the decision-making ability
LLM-basedagentsdespitethecorrectreasoningresult.
choosesanactionfromthecandidatestoplayin
thegame. Extensiveexperimentsshowthatour
agentsovercometheintrinsicbiasandoutperform
models(LLMs)haveshowngreatpotentialinconstructing
existingLLM-basedagentsintheWerewolfgame.
intelligent agents and have led to many recent advance-
We also conduct human-agent experiments and
ments(Ouyangetal.,2022;Weietal.,2022a). TheseLLM-
findthatouragentsachievehuman-levelperfor-
based agents demonstrate proficiency in a wide range of
manceanddemonstratestrongstrategicplay.
tasksincludingwebsurfing(Nakanoetal.,2021;Yaoetal.,
2022b;Zhengetal.,2024), complexvideogames(Wang
et al., 2023a; Ma et al., 2023), and real-world applica-
1.Introduction
tions (Ahn et al., 2022; Shah et al., 2023). Moreover, in
Buildingagentsthatarecapableoflogicalreasoning,strate- multi-agentscenarios,LLM-basedagentsexhibittheabil-
gicdecision-making,andcommunicationwithhumanshas ity to produce human-like interactions (Park et al., 2023;
beenalongstandingaspirationinthefieldofAI(Wooldridge Williams et al., 2023), achieve zero-shot cooperation (Li
&Jennings,1995;Goodwin,1995). Withtheirextensive etal.,2023;Chenetal.,2023),andcompetewithadversarial
knowledge and emergent generalizability, large language players(Metaetal.,2022;Wangetal.,2023b).
*Equal advising 1Tsinghua University, Beijing, China Despite the impressive achievements, we observe that in
2CarnegieMellonUniversity,Pittsburgh,UnitedStates3Shanghai complexdecision-makingtaskssuchasmulti-agentgames,
QiZhiInstitute,Shanghai,China. Correspondenceto: ZelaiXu pure LLM-based agents built with prompting techniques
<zelai.eecs@gmail.com>,YiWu<jxwuyi@gmail.com>.
tendtoexhibitintrinsicbiasintheirchoiceofactions,result-
inginsuboptimalperformance. Considerasimpleexample
Proceedings of the 41st International Conference on Machine
Learning,Vienna,Austria.PMLR235,2024.Copyright2024by whereweuseGPT-4toplaytheRock-Paper-Scissorsgame.
theauthor(s). To generate the optimal strategy, we prompt the LLM to
1

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
first reason about the Nash equilibrium of this game and bias,leadingtostrongstrategicplayintheWerewolfgame.
then choose an action based on the reasoning result. We
We conduct extensive experiments to evaluate the perfor-
letthispureLLM-basedagentplay100independentgames
manceofstrategiclanguageagentsinWerewolfanddemon-
and profile its reasoning result and action distribution in
stratethebenefitofourdesign.Wefirstperformcasestudies
Fig1. Inall100games,theagentsuccessfullyidentifiesthe
and visualize the action distributions to validate that our
optimalstrategyasrandomlychoosinganaction. However,
agentsovercometheintrinsicbiasandlearnbetterpolicy.
evenwith thisperfectreasoning result, the agent’sactual
Thenwecompareouragentswithfourstate-of-the-artbase-
actiondistributionshowsaclearbiastowardchoosingRock,
linesinaround-robintournamentwhereouragentsachieve
whichcanbeeasilyexploitedbyanopponentwhoalways
thehighestwinrateagainstallagents. Moreover,weletour
playsPaper. Thisintrinsicbiasisinevitablyinheritedfrom
agentsplaywithhumanplayersandfindtheyachievecom-
themodel’spretrainingdataandhinderspureLLM-based
parablewinratestoaveragehumansasbothteammatesand
agentsfromstrongstrategicplayinmorecomplexscenar-
opponents. Wealsoconductsystematicablationstoshow
ios. Arecentwork, Cicero(Metaetal.,2022), addresses
theeffectivenessofthekeycomponentsinourframework.
thisissueinthegameofDiplomacybylearningapolicyto
choosefrompredefinedactionsthatspecifytheagents’in-
tentsandthengeneratingaction-conditioneddialogueswith 2.RelatedWork
alanguagemodel. Nevertheless,theactionspaceoftheir
BuildingAgentswithLargeLanguageModels.Thereisa
policyisafixed,finitesetofgame-specificactions,while
recenttrendindevelopingagentswithlargelanguagemod-
real-worldinteractionsbetweenhumansoftenfeaturefree-
elsforvariousdomainsincludingwebsitescenarios(Nakano
formconversationswithnuancedintents,whichinducesan
etal.,2021;Yaoetal.,2022a;Dengetal.,2023),gameand
unboundedactionspaceforagentstoplay.
simulation(Huangetal.,2022a;Wangetal.,2023c;a;Ma
Inthiswork,weaimtodevelopstrategiclanguageagents, et al., 2023), real-world embodiment (Ahn et al., 2022;
i.e.,agentsthatgenerateflexiblelanguageactionsandpos- Huangetal.,2022b;Vempralaetal.,2023),andmulti-agent
sessstrongdecision-makingabilities.WeconsidertheWere- environments(Parketal.,2023;Lietal.,2023;Chenetal.,
wolfgameasachallengingmixedcooperative-competitive 2023). Asharedfoundationoftheseworksistoutilizethe
multi-agenttestbed. Werewolfisoneofthemostpopular reasoningandin-contextlearningabilityofLLMstofacili-
social deduction games where two teams of players with tatedecision-making. Chain-of-Thought(CoT)(Weietal.,
hidden roles interact in natural language to uncover and 2022b)isperhapsthemostwell-knownworkthatunlocks
defeattheiropponents. Duringgameplay,theWerewolves thereasoningabilityofLLMsbyaskingthemtothinkstep-
need to lie about their roles and secretly eliminate other by-step. To synergize reasoning and acting, ReAct (Yao
players,whiletheVillagersneedtoshareinformationand etal.,2022b)usesLLMstogeneratebothreasoningtraces
voteoutthehiddenWerewolves. Thegame’shighdemand andactionplansandproveseffectiveinvariousbenchmarks.
for language proficiency necessitates the use of LLMs to Follow-upworkcontinuestoimproveperformancebyin-
buildintelligentagents. However,pureLLM-basedagents corporatingself-reflection(Shinnetal.,2023)andstrategic
face the challenges of deducing hidden roles with decep- reasoning(Gandhietal.,2023). However,evenwiththeper-
tiveinformationandovercomingintrinsicbiasinlanguage fectreasoningresults,thesepureLLM-basedagentscould
actions,whichresultinunsatisfactoryperformance. sufferfromthemodel’sintrinsicbiasandmakesuboptimal
decisionsinmorecomplexscenarios. Ourworktakesastep
TobuildstrategiclanguageagentsfortheWerewolfgame,
furthertoaddressthisissuebyusingtheLLMtogenerate
we propose a novel framework that powers LLM-based
a diverse set of action candidates with minimal bias and
agentswithreinforcementlearning(RL)toaddressthese
traininganRLpolicytooptimizedecision-making.
challenges. Ourframeworkconsistsofthreecomponents.
Thefirstcomponentishiddenrolededuction,whichusesan SomeotherworksalsoaugmentLLMswithexternalmod-
LLMtodistinguishbetweentruthsandliesandexplicitly ulestoenhancetheagents’decision-makingability. One
deducethehiddenroleofeachplayertofacilitatesubsequent representative work is Cicero (Meta et al., 2022) which
decision-making. Thesecondcomponentisdiverseaction combines LLMs with RL and achieves human-level play
generation,whichpromptstheLLMtogenerateadiverse inthegameofDiplomacy. Themaindifferencefromour
setofactioncandidatesinsteadofasingleactiontomitigate workisthattheirpolicycanchoosefromafixedfinitesetof
theintrinsicbias. Thelastcomponentispopulation-based game-specificactionsbecauseDiplomacyisaboardgame
RL training, which learns an RL policy to optimize the withnegotiation. Bycontrast,Werewolfisalanguagegame
distributionovertheactioncandidatesandimprovespolicy withoutpredefinedactions,requiringouragentstogenerate
robustnessbyplayingagainstapopulationofvariousagents. languageactionsinanunboundedspace. Anotherworkis
ThecombinationoftheLLMandtheRLpolicyenablesour Tree-of-Thought(ToT)(Yaoetal.,2023)whichgeneralizes
agentstodeducehiddeninformationandovercomeintrinsic CoTbyproducingmultiplethoughtsateachreasoningstep
2

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Setup Gameplay Winning
night day
The Werewolves Werewolves Announcement The Werewolves win
Player 4 was killed last night.
× 2
Discussion
• Player 0 (Werewolf): I don’t have
Kill Player 4. leads on who the Werewolves might
Werewolves: Player 0, Player 5.
be. Anyone have any suspicions?
Seer • Player 1 (Doctor): It’s unfortunate
The number of remaining
The Villagers that we lost Player 0. I’m the Doctor Werewolves equals the
and I saved myself last night.
number of remaining Villagers.
• …
• Player 6 (Villager): I agree that player
0 is indeed very suspicious, let’s vote The Villagers win
See Player 0 is a Werewolf. them out today.
Seer: Player 3. Doctor: Player 1.
Doctor Voting
• Vote for Player 0: Player 1, Player 3,
× 3 Player 6.
• Vote for Player 3: Player 0, Player 5.
• Do not Vote: Player 2.
There is no Werewolf left.
Villager: Player 2, Player 4, Player 6. Save Player 1. Result: Player 0 is eliminated.
Figure2: AnexampleoftheWerewolfgame. PlayersarerandomlyassignedahiddenroleanddividedintotheWerewolves
andtheVillagers. Thegamealternatesbetweennightanddayroundsuntiloneteamachievesthewinningcondition.
tocreateatreestructureandsearchforoptimalplans. The outcomes and potential better choices. Most prior works
extensivetreesearchcouldbeinefficientincomplexenvi- applythesemethodstotypicalRLenvironmentswithvec-
ronmentswithprohibitivelylargeoreveninfinitegametrees. torizedactions,whilewecombineLLMwithRLtogenerate
LLM+P(Liuetal.,2023)incorporateclassicplannersby languageactionsandlearnintheWerewolfgame.
convertingnaturallanguagetaskdescriptionsintoplanning
AIAgentsforSocialDeductionGames. Socialdeduction
domain definition language (PDDL). However, PDDL is
gameslikeWerewolfrequirebothstrongcommunication
limitedtoclassicplanningproblemsandcannotbeapplied
skillsandstrategicdecision-making. Earlieragents(Wang
tonon-cooperativelanguagegameslikeWerewolf.
&Kaneko,2018)lacklanguageproficiencyandusuallyrely
Reinforcement Learning in Non-Cooperative Games. onpredefinedprotocolsinsteadofnaturallanguagetoplaya
Applyingreinforcementlearningtonon-cooperativegames simplifiedgame. DeepRole(Serrinoetal.,2019)integrates
hasachievedgreatsuccessinthegameofGo(Silveretal., deductivereasoningintoCFRtoplayanothersocialdeduc-
2016;2018),poker(Moravcˇíketal.,2017;Brown&Sand- tiongamenamedAvalonwithoutcommunication. Withthe
holm,2018;2019),andvideogames(Vinyalsetal.,2019; presenceofLLMs,moreagentshavebeendevelopedtoplay
Berner et al., 2019). The most popular method underly- thesegamesinnaturallanguage. Aconcurrentstudy(Xu
ingtheseachievementsisself-playanditsvariants(Hein- etal.,2023a)buildsaWerewolfagentbyheuristicinforma-
rich et al., 2015; Heinrich & Silver, 2016; Hennes et al., tionretrievalandpastexperiencereflection. Anotherwork
2020; Xu et al., 2023b), which learn a policy by training proposes ReCon (Wang et al., 2023b) to play Avalon by
against itself and its past checkpoints. Population-based thinkingfromboththeagent’sandtheopponents’perspec-
training(PBT)methodslikepolicy-spaceresponseoracles tive.Despitetheirdeliberatedesigns,thesepureLLM-based
(PSRO)(Lanctotetal.,2017;Mulleretal.,2019)andleague agentsarenotstrongenoughindecision-makingastheystill
training(Vinyalsetal.,2019)generalizeself-playbymain- facetheissueofintrinsicbias. Weusethemasbaselinesto
tainingapoolofvariouspoliciesandtrainingagainstthe comparewithouragentsintheexperiments.
population. Anothernotablelineofworkisbasedonregret
minimizationtechniquessuchascounterfactualregretmini-
3.TheWerewolfGame
mization(CFR)(Zinkevichetal.,2007;Lanctotetal.,2009;
Tammelin,2014;Brownetal.,2019)thatiterativelyrefine Weaimtobuildstrongagentsfortheseven-playerWerewolf
thestrategiesbyminimizingthedifferencebetweenactual gamewithtwoWerewolves,oneSeer,oneDoctor,andthree
3

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Villagers. AnexampleofthegameisshowninFig.2and actionsduringdiscussionthatshareinformationandconvey
thedetailedrulescanbefoundinAppendixA. theplayer’sopinion. Thelasttypeisvotingactionsthatvote
foronesurvivingplayerorchoosenottovote.
3.1.Text-BasedEnvironemnt
3.2.ChallengesforLLM-BasedAgents
Weimplementapuretext-basedWerewolfenvironmentthat
doesnotconsiderexternalfactorsliketheplayers’toneor Werewolfisachallengingmixedcooperative-competitive
facialexpressions. Theobservationsandactionsaretextin gamethatinvolvesdeceptivecommunicationandstrategic
naturallanguageandthegameproceedsasfollows. gameplay. Its high demand for language proficiency ne-
cessitatestheuseofLLMstobuildintelligentagents. We
Setup. At the beginning of the game, each player is ran-
identifytwomajorchallengesofWerewolfthatposehigher
domlyassignedahiddenrole,whichdividesthemintothe
requirementsontheabilityofLLM-basedagents.
WerewolvesandtheVillagers(Seer,Doctor,andVillagers).
ThetwoWerewolvesknoweachother’sroleandhencealso The first challenge is to deduce hidden information from
knowwhichplayersaretheVillagers. Theirgoalisto“kill” deceptivecommunication. Withtheexistenceofunknown
theotherplayerswithoutbeingdiscovered. TheVillagers opponents, agents could be misled by manipulative state-
donotknowthehiddenrolesofotherplayersandtheirgoal mentsandfailtomakeaccuratejudgmentsaboutotherplay-
istoidentifyandeliminatetheWerewolves. ers. Thisrequirestheagentstodistinguishbetweentruths
andliesanddeducethehiddenrolesofotherplayers.
Gameplay. The game alternates between night and day
rounds,startingwiththenight. Inthenightround,everyone Thesecondchallengeistoovercometheintrinsicbiasin
closestheireyestolettheWerewolves, Seer, andDoctor LLMs and optimize decision-making. As illustrated by
take secret actions. The Werewolves choose one player theRock-Paper-ScissorexampleinFig1,pureLLM-based
to kill, the Seer chooses one player to check if they are agentscouldhavesuboptimalbiasesintheiractiondistri-
a Werewolf, and the Doctor chooses one player to save butions,hinderingtheirabilitytomakestrongerdecisions.
withoutknowingwho isthe target ofthe Werewolves. If Thisissuebecomesmorepronouncedincompetitivegames
theDoctorchoosesthesameplayerastheWerewolves,the likeWerewolfbecauseopponentscanexploitthebiaseddis-
playerissuccessfullysavedandnooneiskilledinthenight tributionstopredicttheagents’behaviorsandcounteractto
round. Otherwise,theplayeriseliminatedfromthegame. gainadvantages. Therefore,agentsmustovercomeintrinsic
biastoreduceexploitationandachievestrongperformance.
Inthedayround,anannouncementisfirstmadetoevery
playeraboutwhowaskilledornoonewaskilledlastnight.
Then the remaining players take turns to speak in a dis- 4.StrategicLanguageAgents
cussionaboutwhomightbetheWerewolves. Playerscan
To address the aforementioned challenges, we propose a
claimorlieabouttheirroles,shareorwithholdinformation
novelframeworkthatpowersLLM-basedagentswithRL
theyhavediscovered,andaccuseordefendotherplayersto
trainingtobuildagentsthatgenerateflexiblelanguageac-
achievetheirpurposes. Afterallplayershaveparticipated
tionsandpossessstrongdecision-makingability,whichwe
inthediscussion,avoteisheldtoeliminateonesuspicious
call strategic language agents. As shown in Fig. 3, our
player. Eachplayercanvoteforoneplayerorchoosenot
agentsconsistofthreecomponents: hiddenrolededuction,
to vote, and the player with the most votes is eliminated.
diverseactiongeneration,andpopulation-basedRLtraining.
Thenthegamecontinuestothenextnightrounduntilthe
WerewolvesortheVillagerswinthegame.
4.1.HiddenRoleDeduction
Winning. TheWerewolveswinifthenumberofremaining
Thefirstcomponentaimstoimproveouragents’deductive
WerewolvesisequaltothenumberofremainingVillagers.
reasoningabilityinthepresenceofdeceptiveinformation.
TheVillagerswinifbothWerewolvesareeliminated.
weuseanLLMtoconverttherawobservationintoanorga-
The observation of each player is a list of information in nizedinformationrecordandastructureddeductionresult.
natural language that describes the current game history. Theinformationrecordextractskeyinformationanddistin-
ThisincludestheirID,hiddenrole,secretactionsatnight guishesbetweentruthfulanddeceptivestatements, while
(if any) as well as the announcements, discussions, and the deduction result infers the hidden role of each player
voting results in the day rounds. Werewolves also have andratestheirreliability. Thesestructuredandinformative
theirteammate’sIDandsecretactionsintheobservation. dataserveasinputsforthenexttwocomponentsandlaythe
Theplayers’actionsarealsoinnaturallanguageandcan foundationforsubsequentdecision-making.
bedividedintothreetypes. Thefirsttypeissecretactions
Concretely,theinformationrecordcategorizestherawob-
atnightincludingkilling,seeing,andsavingthatchoosea
servation,whichisalistofinformationinnaturallanguage,
specificplayerasthetarget. Thesecondtypeisstatement
4

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
You are Player3, your Facts Player 0 Action 1: I’m the Seer and I saw RL policy
role is the Seer. [1] You are Player 3, your • Role: Werewolf. Player 0 is a Werewolf …
role is the Seer. • Reliability: 1.
You saw Player0 is a [2] You saw Player 0 is a • Reasoning: I saw Player 0
Werewolf in night 1. Werewolf in night 1. is a Werewolf. Action 2: I think Player 0 is a little
[3] Player 4 was killed in • Evidence: [1, 2]. suspicious because … RL policy Past
P
n
l
i
a
g
y
h
e
t
r
1
4
.
was killed in night 1. +
…
itself che…ckpoints
Potential truths Werewolf Werewolf In day 1 [4] In day 1, Player 1 said: … Player 6
style 1 style M
Player0 said: … • Role: …
Player1 said: … Potential deceptions • Reliability : … Player2 said: … [ [ 5 6 ] ] I I n n d d a a y y 1 1 , , P P l l a a y y e e r r 0 2 s s a a i i d d : : … … • • R Ev e i a d s e o n n c i e n : g [ : … … ] A of c t P i l o a n y e N r : 4 I ’ … m saddened by the loss V s i t l y la le g e 1 r V st i y ll l a e g M er
raw observation information record deduction result action candidates agent population
…
(2) Diverse Action (3) Population-Based
(1) Hidden Role Deduction
Generation RL Training
Population-based training
…
…
…
Figure3: Overviewofstrategiclanguageagents. (1)Hiddenrolededuction: categorizekeyinformationanddeducehidden
roleswiththeLLMtofacilitatesubsequentdecision-making. (2)Diverseactiongeneration: prompttheLLMforadiverse
setofactioncandidatestomitigateintrinsicbias. (3)Population-basedRLtraining: learnaseparateRLpolicytooptimize
thedistributionoveractioncandidatesandenhancedecision-makingbyplayingagainstapopulationofvariousagents.
into three types including facts, potential truths, and po- considertwoapproachestogenerateN actioncandidates.
tential deceptions. All information except the statements
Vanilla Prompting. The first approach generates all ac-
indiscussioniscategorizedasfacts,whichencompassthe
tion candidates in a single inference by asking the LLM
player’s role, secret actions, announcements, and voting
toproposeN diverseactioncandidatesthatcorrespondto
results. The statements are categorized according to the
differentstrategies. Thisapproachissimpleyeteffectivefor
speaker’sreliabilityinthedeductionresult. Inourimple-
easieractionslikesecretactionsandvotingactions,which
mentation,thereliabilityisratedonascalefrom1to10. If
onlyneedtochooseaplayerasthetarget.
aplayer’sreliabilityislargerthan6,theirstatementsarere-
gardedaspotentialtruths,otherwiseaspotentialdeceptions. Iterative Prompting. The second approach prompts the
LLMforN timesanditerativelygeneratesoneactioncandi-
With the organized information record, we then prompt
dateatatime. Ineachinference,weaddtheexistingaction
theLLMtodeducethehiddenrolesofotherplayers. For
candidatestotheinputandasktheLLMtoproposeanew
each player, the LLM is asked to generate four attributes
actioncandidatethatisstrategicallydifferentfromexisting
includingrole,reliability,reasoning,andevidence. Therole
ones. ByhavingmoreinteractionswiththeLLM,thisap-
attributeinfersthemostlikelyhiddenroleoftheplayerand
proachisempiricallyfoundtoproducebetterperformance
the reliability attribute rates the credibility of their state-
formorecomplexactionslikestatementactions.
mentsfrom1to10. Thereasoningattributeisanauxiliary
onethatexplicitlyshowsthedeductionprocess. Thelast Inourimplementation,weusethefirstapproachtogenerate
evidenceattributeisalistofintegersthatciteitemsfromthe secretactionsandvoteactionsforfewerinferences,andthe
informationrecordtosupportthecurrentdeduction. Theev- secondapproachtogeneratestatementactionsforhigher
idencesareusedtoextractkeyinformationthatcontributes quality. WealsoasktheLLMtooutputtheirreasoningfor
to the deduction of hidden roles. If a statement is never eachactioncandidateforinterpretabilityandbetterperfor-
citedasevidence, itisregardedasanuninformativeitem mance. ThedetailedpromptscanbefoundinAppendixB.
andremovedfromtheinformationrecord. Moredetailed
designsandpromptscanbefoundinAppendixB. 4.3.Population-BasedRLTraining
Withthediversesetofactioncandidates,agentscanavoid
4.2.DiverseActionGeneration
fixedpatternsandchoosefromavarietyofactionstotake.
TomitigatetheintrinsicbiasofLLMsandreduceexploita- Althoughrandomsamplingalreadyleadstounpredictable
tionfromadversarialplayers,agentsshouldbeabletocon- play,theoptimalpolicyinmostcasesisanon-uniformdis-
sider a broader range of reasonable actions instead of a tributionovertheactioncandidates. Directlyfine-tuningthe
single biased action. We propose the diverse action gen- LLMtorefinethedistributionrequiresasubstantialamount
erationcomponenttoprompttheLLMforasetofaction ofdataandcomputation. Wetakeanalternativeapproach
candidateswithstrategicdiversity. Morespecifically,given thatefficientlylearnsasmallerRLpolicytooptimizethe
the information record and deduction result as input, we actiondistributionandenhancedecision-makingabilityby
5

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Pure LLM-Based Agent Pure LLM-Based Agent Pure LLM-Based Agent
0.4 0.38 1.0 0.75 0.69
0.29
0.62
0.50
0.2 0.5 0.38
0.12 0.11 0.06 0.25 0.15 0.14
0.03 0.01 0.02
0.0 0.0 0.00
0 1 2 3 4 5 6 self others not vote right wrong others
Strategic Language Agent Strategic Language Agent Strategic Language Agent
0.4 1.0 0.94 0.75
0.49
0.50
0.37
0.2 0.13 0.12 0.14 0.13 0.17 0.16 0.15 0.5
0.25 0.13
0.06 0.01
0.0 0.0 0.00
0 1 2 3 4 5 6 self others not vote right wrong others
(a) Werewolffirstnightaction. (b) Doctorfirstnightaction. (c) Villagervotingaction.
Figure4: ComparisonoftheactiondistributionsofthepureLLM-basedagentandourstrategiclanguageagent.
playingagainstapopulationofvariousagents. actionaccordingtotheirpredefinedstyles.Inourimplemen-
tation,weconsiderthreecommonstylesfortheWerewolves
The main difference between our setting and classic RL
andthreestylesfortheVillagers. Moreimplementationand
environmentsisthattheactionspaceofourpolicyisaset
trainingdetailscanbefoundinAppendixC.
of language actions generated during the game. Because
the action space is not predefined, we cannot use typical
policynetworksthatonlytaketheobservationasinputand 5.Experiments
produceadistributionoverthefixedactionset. Instead,we
Weconductexperimentsfromfourdifferentaspectstocom-
adoptaself-attentionnetwork(Vaswanietal.,2017)that
prehensivelyevaluatetheperformanceofstrategiclanguage
takestheobservationandallactioncandidatesasinputto
agents. Wefirstperformcasestudiesandvisualizetheac-
producetheactiondistribution. Concretely,theobservation
tiondistributionsofouragentstocheckiftheyaddressthe
andactioncandidatesinnaturallanguageareconvertedto
intrinsicbiasissue. Thenwecompareouragentswithfour
vectorembeddingsusingtheLLMembeddingAPI.Wealso
existing LLM-based agents in a round-robin tournament
useavectortoincludeplayer-specificinformationliketheir
to assess their decision-making ability. Furthermore, we
ID, role, etc. and pass it through an encoder to produce
conducthuman-agentexperimentstoevaluatetheirperfor-
a player embedding of the same dimension. The player
mancewithandagainsthumanplayers. Wealsoperform
embedding,observationembedding,andactioncandidate
ablation studies to investigate the contribution of the key
embeddings are passed through a residual self-attention
componentsinourdesign. Moreexperiments,discussions,
block,andtheprobabilitytosampleanactioncandidateis
andemergentbehaviorscanbefoundinAppendixD,E,F.
proportionaltothescaleddot-productattentionbetweenthe
observationembeddingandactioncandidateembedding.
5.1.CaseStudies
Toachievestrongandrobustperformancewithvariousteam-
Tovalidatethatourmethodovercomestheintrinsicbiasin
matesandopponents,wetraintheRLpolicywithapopula-
LLMs,weinvestigatethreetypicalsituationsintheWere-
tionofdiverseagents. Thisisbecausereal-worldgamesare
wolfgameandcomparetheactiondistributionsofouragents
usuallynon-transitive(Czarneckietal.,2020),i.e.,thepoli-
withapureLLM-basedagentthatonlyhasthehiddenrole
ciesmaycyclelikeRock-Paper-Scissors, andpopulation-
deductioncomponentandfollowsReAct(Yaoetal.,2022b)
basedtrainingcanhelpagentsgetovertheendlesscycles
togenerateonesingleactiontoplay.
andachieveahigherlevelofplay.Ouragentpopulationcon-
sistsoftwotypesofpolicies. ThefirsttypeistheRLpolicy WerewolfFirstNightAction. Onthefirstnight,theWere-
itselfanditspastcheckpoints. Trainingwiththesepolicies wolvesneedtochooseaplayertokillwithoutanyinforma-
resemblesself-playandfictitiousplay. Thesecondtypeis tion. Theiroptimalpolicyistorandomlychooseaplayer
pureLLM-basedagentswithpredefinedplaystyles,which otherthanthemselvessothattheDoctorcannotpredictand
introducemorestrategicdiversity. Theseagentsonlyhave savethevictim. However,asshowninFig.4(a),thepure
thefirsthiddenroledeductioncomponentandgenerateone LLM-basedagenthasaclearbiastowardkillingPlayer0,
6

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
ReAct ReCon Concurrent Atomic Ours
The Werewolves
segalliV
ehT
tcAeR
noCeR
tnerrucnoC
cimotA
sruO
Win Rate of the Villagers causethereisonlyoneagent(Xuetal.,2023a)thatworks
outoftheboxforWerewolf,wemakeourbestefforttose-
0.22 0.20 0.19 0.19 0.16
lectfourrepresentativemethodsasbaselinesandmakethem
(0.01) (0.02) (0.03) (0.02) (0.02)
compatiblewithourenvironment. WeimplementtheRe-
Act(Yaoetal.,2022b)agentbydirectlypromptingtheLLM
0.26 0.27 0.26 0.22 0.20 with the raw observation to generate both reasoning and
(0.02) (0.02) (0.03) (0.03) (0.02) action. ReCon(Wangetal.,2023b)isoriginallydesigned
forAvalonandgeneratesactionsbyplanningfromtheirown
0.27 0.25 0.26 0.23 0.22 perspectiveandrefiningtheplanfromothers’perspective.
(0.02) (0.01) (0.04) (0.01) (0.02) TheConcurrentagent(Xuetal.,2023a)considersadiffer-
ent version of the Werewolf game and employs heuristic
informationretrievalandreflectiononpastexperiences. We
0.34 0.31 0.33 0.30 0.27
makenecessarychangestothepromptsofReConandCon-
(0.02) (0.03) (0.03) (0.02) (0.02)
currenttoapplytheminoursetting. TheAtomicagentis
inspiredbyCicero(Metaetal.,2022)andhasapredefined
0.46 0.39 0.40 0.36 0.30 set of 13 atomic actions like “target Player 0”, “claim to
(0.03) (0.02) (0.04) (0.02) (0.03)
betheSeer”,etc. ThisagentlearnsanRLpolicytoselect
an atomic action based on the raw observation and then
____ promptstheLLMtofollowtheatomicactionandgenerate
thelanguageactionusedinactualgameplay.
Figure5: Winratematrixoftheround-robintournament. Weletouragentsandthesefourbaselineagentsparticipate
inaround-robintournamentthatrunshead-to-headcompe-
titionsbetweeneachpairofagents. Forapairofagents(A,
which could be exploited by a Doctor who always saves B),werun100WerewolfgameswithfiveAagentsbeing
Player0.Bycontrast,ouragentsproduceanalmostuniform theVillagersandtwoBagentsbeingtheWerewolves. This
distributionwhichisclosetotheoptimalpolicy. leads to a 5×5 cross-play matrix in Fig. 5 that records
the win rates of the Villagers. For example, the value in
Doctor First Night Action. The Doctor also needs to
the first row and last column corresponds to the win rate
choose a player to save without knowing who is the vic-
ofReActwhenitplaysastheVillagersagainstouragents
timonthefirstnight. FromtheDoctor’sperspective,any
as the Werewolves. The row in the matrix represents the
playerotherthanthemselvescouldbeaWerewolf,andsav-
agent’sperformanceastheVillagersagainstdifferentoppo-
ingothersmaywastetheactiononaWerewolf. Therefore,
nents, andarowwithhigher(red)valuesmeansstronger
the optimal policy for the Doctor is to always save them-
performanceastheVillagers. Asshownbytheboldnum-
selves on the first night. As shown in Fig. 4(b), the pure
bersinthelastrow,ouragentsachievethehighestwinrates
LLM-basedagentexhibitsasuboptimalpolicythatsaves
as the Villagers against all agents. Similarly, the column
otherswithaprobabilityof0.38,whileouragentslearnto
representstheagent’sperformanceastheWerewolvesand
savethemselveswithahighprobabilityof0.94.
smaller(blue)valuesmeanlowerwinratesoftheiroppo-
VillagerVotingActionwithTwoSelf-ProclaimedSeers. nents,indicatingstrongerperformanceastheWerewolves.
Anothercommonsituationiswhentwoplayersclaimtobe Thelastcolumnwithunderlinednumbersshowsthatour
theSeerandtheVillagersneedtochoosetheiractionsin agentsalsoachievethebestperformanceastheWerewolves.
thevotingphase. ThepureLLM-basedagenttendstomake
The strong decision-making ability of our agents comes
conservativedecisionsandchoosesnottovotewithahigh
fromthecombinationofanLLMtogenerateflexiblelan-
probabilityof0.69,asshowninFig4(c). However,oneof
guageactionsandanRLpolicytoovercomeintrinsicbias.
theself-proclaimedSeersmustbeaWerewolfandnotvoting
TheReact,ReCon,andConcurrentagentsdirectlygenerate
foranyplayeronlymakesiteasierfortheWerewolvesto
languageactionswithanLLM.Evenifthelattertwohave
control the voting result and eliminate the real Seer. In
specificdesignsforsocialdeductiongames,theystillface
comparison,ouragentshaveamuchlowerprobabilityfor
theintrinsicbiasissueandhaveunsatisfactoryperformance.
choosingnottovoteandlearntoidentifyandvoteoutthe
Ontheotherhand,althoughtheAtomicagentalsocombines
rightWerewolfwhopretendstobetheSeer.
anLLMwithanRLpolicy,itslanguagegenerationiscon-
ditionedonthepredefinedactionsetwhichishard,ifnot
5.2.Round-RobinTournament impossible,tocovertheunboundedlanguagespace. More
examplesandanalysiscanbefoundinAppendixE.
WeevaluatetheperformanceofouragentsintheWerewolf
gamebyplayingagainstexistingLLM-basedagents. Be-
7

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
PlaywithSixCopiesofOurAgents PlaywithSixHumanPlayers
WinRate
PureLLM-Based Ours Human PureLLM-Based Ours Human
AstheVillagers 0.25(0.03) 0.30(0.03) 0.28(0.06) 0.29(0.06) 0.36(0.05) 0.38(0.07)
AstheWerewolves 0.61(0.05) 0.70(0.03) 0.67(0.08) 0.54(0.08) 0.67(0.06) 0.66(0.08)
Overall 0.42(0.04) 0.50(0.03) 0.48(0.07) 0.42(0.07) 0.52(0.06) 0.52(0.08)
Table1: WinrateofoneAIagentorhumanwhenplayingwithsixcopiesofouragentsandplayingwithsixhumanplayers.
WinRate AstheVillagers AstheWerewolves WinRate AstheVillagers AstheWerewolves
Ours 0.30(0.03) 0.70(0.03) Ours(PBT) 0.30(0.03) 0.70(0.03)
-RLPolicy 0.23(0.03) 0.61(0.04) Self-Play 0.26(0.04) 0.66(0.02)
-Diversity 0.22(0.04) 0.61(0.05)
-Deduction 0.16(0.02) 0.54(0.04) Table4: Ablationonagentpopulation.
Table2: Ablationonkeycomponents. theVillagers. Moreinterestingly,whenplayingwithsixhu-
manplayers,ouragentsalsoachievecomparablewinrates
WinRate AstheVillagers AstheWerewolves tohumanplayers. Notethatouragentsarenottrainedwith
realhumans,thisresultshowsthestrongrobustnessofour
Ours 0.30(0.03) 0.70(0.03)
agentstobothcooperatewithandcompeteagainstunseen
-Evidence 0.28(0.04) 0.67(0.03)
humanplayersandachievehuman-levelperformance.
-Reasoning 0.25(0.03) 0.66(0.05)
-Reliability 0.23(0.02) 0.62(0.04)
5.4.AblationStudy
Table3: Ablationondeductionattributes. Key Components. We consider three ablated agents by
gradually removing the three key components from our
5.3.HumanEvaluation agentsandevaluatingtheirperformancebyplayingagainst
ouragents.The“-RLpolicy”agentusestheLLMtochoose
Wefurtherconducthuman-agentexperimentstoevaluate
fromtheactioncandidatesinsteadoftheRLpolicy. The
the performance of our agents. Concretely, we compare
“-Diversity”agentfurtherremovesthediverseactiongener-
our agents with human players and the pure LLM-based
ationcomponentanddirectlypromptstheLLMtoproduce
agentusedinSection5.1intwosetupsoftheseven-player
oneaction. The“-Deduction”agentremovesallthreecom-
Werewolf game. The first setup is to let one human or
ponentsanddirectlygeneratesanactionbasedontheraw
one AI agent play with six copies of our agents, and the
observation. TheresultsinTable2showthatallthreecom-
secondsetupistoletoneAIagentoronehumanplaywith
ponentscontributetotheimprovementinperformance. It
six human players. We recruited 160 human players and
isalsoworthnotingthat,althoughthe“-RLpolicy”agent
randomlyassignedeachplayertooneofthetwosetupsto
generatesdiverseactioncandidates,itswinratesarecompa-
play10consecutivegames. Thehumanplayersknowwho
rabletothe“-Diversity”agent. Thisisbecauseusingthe
aretheAIagentsandthehiddenrolesareassignedrandomly
LLMtochoosefromtheactioncandidatesstillsuffersfrom
ineachgame. Additionaldetailsofthehumanevaluation
intrinsicbias. ThisissueisfullysolvedbyaddingtheRL
procedurecanbefoundinApendixD.7.
policytooptimizedecision-making.
WereportthewinrateoftheoneAIagentandonehuman
Deduction Attributes. We study the contribution of the
playerbothastheWerewolvesandastheVillagersinTable1
fourattributesinhiddenroledeductionbygraduallyremov-
andeachentryisaveragedover100games. Inbothsetups,
ing the evidence, reasoning, and reliability attributes and
comparing the results in the “Pure LLM-Based” column
evaluatingagainstouragents. TheresultsinTable3show
and“Ours”columnshowsthatouragentsachievehigher
thatusingallfourattributesgivesthebestperformance.
winratesthanthepureLLM-basedagentwhenplayingwith
sixcopiesofouragentsandwhenplayingwithsixhuman AgentPopulation. Wealsolearnanagentusingself-play
players.Thisresultvalidatesthatourframeworktocombine insteadofpopulation-basedtraining(PBT)andcompareit
theLLMwiththeRLpolicyleadstostrongerperformance withouragents. TheresultsinTable4showthatouragents
intheWerewolfgame. Inaddition,whenplayingwithsix achieve higher win rate both as the Villagers and as the
copiesofouragents,theresultsinthe“Ours”columnand Werewolf. Thisalignswiththeresultsinotherreal-world
the“Human”columnshowthatouragentsachievehigher games that introducing more diversity to the population
winratesthanhumanplayers,bothastheWerewolvesandas makesthepolicymorerobust(Czarneckietal.,2020).
8

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
6.Conclusion References
WeproposeanovelframeworkthatcombinesanLLMwith Ahn,M.,Brohan,A.,Brown,N.,Chebotar,Y.,Cortes,O.,
anRLpolicytobuildstrategiclanguageagentsthatover- David,B.,Finn,C.,Fu,C.,Gopalakrishnan,K.,Hausman,
come the intrinsic bias of pure LLM-based agents. Our K.,etal. Doasican,notasisay: Groundinglanguage
agentsdeducehiddeninformationbycategorizingkeyinfor- inroboticaffordances. arXivpreprintarXiv:2204.01691,
mationandinferringhiddenroleswiththeLLM.Toaddress 2022.
theissueofintrinsicbias,ouragentsgenerateadiverseset
Berner,C.,Brockman,G.,Chan,B.,Cheung,V.,Debiak,P.,
ofactioncandidatesandlearnanRLpolicytochoosefrom
Dennison,C.,Farhi,D.,Fischer,Q.,Hashme,S.,Hesse,
theactioncandidates. BypoweringLLM-basedagentswith
C., et al. Dota 2 with large scale deep reinforcement
anRLpolicy,ouragentsoutperformexistingLLM-based
learning. arXivpreprintarXiv:1912.06680,2019.
agentsandachievehuman-levelplayintheWerewolfgame.
Brown,N.andSandholm,T. Superhumanaiforheads-up
Acknowledgements no-limitpoker: Libratusbeatstopprofessionals. Science,
359(6374):418–424,2018.
ThisworkwassupportedbytheNationalNaturalScience
FoundationofChina(No.62325405,U19B2019,M-0248), Brown,N.andSandholm,T. Superhumanaiformultiplayer
TsinghuaUniversityInitiativeScientificResearchProgram, poker. Science,365(6456):885–890,2019.
Tsinghua-MeituanJointInstituteforDigitalLife,Beijing
Brown, N., Lerer, A., Gross, S., and Sandholm, T. Deep
National Research Center for Information Science, Tech-
counterfactualregretminimization. InInternationalcon-
nology (BNRist), Beijing Innovation Center for Future
ferenceonmachinelearning,pp.793–802.PMLR,2019.
Chips and 2030 Innovation Megaprojects of China (Pro-
grammeonNewGenerationArtificialIntelligence)Grant Chen,W.,Su,Y.,Zuo,J.,Yang,C.,Yuan,C.,Qian,C.,Chan,
No. 2021AAA0150000. C.-M.,Qin,Y.,Lu,Y.,Xie,R.,etal. Agentverse: Facili-
tatingmulti-agentcollaborationandexploringemergent
ImpactStatement behaviors in agents. arXiv preprint arXiv:2308.10848,
2023.
WhiletheintentofourworkistodevelopLLM-basedagents
withstrongdecision-makingabilityintheWerewolfgames, Czarnecki,W.M.,Gidel,G.,Tracey,B.,Tuyls,K.,Omid-
italsoraisesimportantethicalconcernsregardingAIagents’ shafiei,S.,Balduzzi,D.,andJaderberg,M. Realworld
deceptionstohumanparticipantsandthepotentialmisuse gameslooklikespinningtops. AdvancesinNeuralInfor-
ofourapproach. Westrictlyfollowprinciplesforethical mationProcessingSystems,33:17443–17454,2020.
researchinourstudyandmakeourbesteffortstoreduceany
Deng,X.,Gu,Y.,Zheng,B.,Chen,S.,Stevens,S.,Wang,
potentialharmtoparticipantsinourhuman-AIexperiment
B.,Sun,H.,andSu,Y. Mind2web: Towardsageneralist
andthebroaderhumansociety.
agent for the web. arXiv preprint arXiv:2306.06070,
Toensureminimalnegativeimpactonhumanparticipantsin 2023.
ourstudy,weconductthehuman-agentexperimentwithde-
Gandhi, K., Sadigh, D., and Goodman, N. D. Strate-
partmentapprovalandalloweachparticipanttotakepartin
gic reasoning with language models. arXiv preprint
thestudyafteragreeingtotheconsentform. Wementionex-
arXiv:2305.19165,2023.
plicitlyintheconsentformthattheWerewolfgamecontains
deceptivecommunicationsandtheAIagentsmayhavedis- Goodwin,R. Formalizingpropertiesofagents. Journalof
honeststatementsinthegame. Theparticipantcanchoose LogicandComputation,5(6):763–781,1995.
tostopparticipatingatanytimeduringtheexperiment.
Heinrich, J. and Silver, D. Deep reinforcement learning
Wearealsocommittedtopreventthemisuseofourapproach
from self-play in imperfect-information games. arXiv
inwaysthatcouldharmhumansociety. Ontheonehand,
preprintarXiv:1603.01121,2016.
ourimplementationofstrategiclanguageagentsfocuseson
the pure text-based environment of Werewolf and cannot Heinrich,J.,Lanctot,M.,andSilver,D. Fictitiousself-play
be directly applied to other real-world situations. On the inextensive-formgames. InInternationalconferenceon
otherhand,ourexperimentresultsshowthatouragentshave machinelearning,pp.805–813.PMLR,2015.
strongerabilitytoidentifyandcounteractdeceptionsthan
Hennes,D.,Morrill,D.,Omidshafiei,S.,Munos,R.,Pero-
existingLLM-basedagents. Thismakeitpossibletouse
lat,J.,Lanctot,M.,Gruslys,A.,Lespiau,J.-B.,Parmas,
ouragentstohelphumansrecognizemanipulativecontent
P.,Duéñez-Guzmán,E.,etal. Neuralreplicatordynam-
andpreventpotentialmalicioususewithharmfulintent.
ics: Multiagentlearningviahedgingpolicygradients. In
9

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Proceedingsofthe19thinternationalconferenceonau- Nakano,R.,Hilton,J.,Balaji,S.,Wu,J.,Ouyang,L.,Kim,
tonomousagentsandmultiagentsystems,pp.492–501, C.,Hesse,C.,Jain,S.,Kosaraju,V.,Saunders,W.,etal.
2020. Webgpt: Browser-assistedquestion-answeringwithhu-
manfeedback. arXivpreprintarXiv:2112.09332,2021.
Huang,W.,Abbeel,P.,Pathak,D.,andMordatch,I. Lan-
guage models as zero-shot planners: Extracting ac- Ouyang,L.,Wu,J.,Jiang,X.,Almeida,D.,Wainwright,C.,
tionable knowledge for embodied agents. In Interna- Mishkin,P.,Zhang,C.,Agarwal,S.,Slama,K.,Ray,A.,
tionalConferenceonMachineLearning,pp.9118–9147. et al. Training language models to follow instructions
PMLR,2022a. withhumanfeedback. AdvancesinNeuralInformation
ProcessingSystems,35:27730–27744,2022.
Huang,W.,Xia,F.,Xiao,T.,Chan,H.,Liang,J.,Florence,
P.,Zeng,A.,Tompson,J.,Mordatch,I.,Chebotar,Y.,etal. Park, J. S., O’Brien, J. C., Cai, C. J., Morris, M. R.,
Innermonologue: Embodiedreasoningthroughplanning Liang, P., and Bernstein, M. S. Generative agents: In-
withlanguagemodels. arXivpreprintarXiv:2207.05608, teractive simulacra of human behavior. arXiv preprint
2022b. arXiv:2304.03442,2023.
Lanctot,M.,Waugh,K.,Zinkevich,M.,andBowling,M. Serrino,J.,Kleiman-Weiner,M.,Parkes,D.C.,andTenen-
Montecarlosamplingforregretminimizationinexten- baum, J. Finding friend and foe in multi-agent games.
sivegames. Advancesinneuralinformationprocessing AdvancesinNeuralInformationProcessingSystems,32,
systems,22,2009. 2019.
Lanctot, M., Zambaldi, V., Gruslys, A., Lazaridou, A., Shah,D.,Osin´ski,B.,Levine,S.,etal. Lm-nav: Robotic
Tuyls,K.,Pérolat,J.,Silver,D.,andGraepel,T. Auni- navigation with large pre-trained models of language,
fiedgame-theoreticapproachtomultiagentreinforcement vision,andaction. InConferenceonRobotLearning,pp.
learning. Advances in neural information processing 492–504.PMLR,2023.
systems,30,2017.
Shinn,N.,Labash,B.,andGopinath,A. Reflexion: anau-
tonomousagentwithdynamicmemoryandself-reflection.
Li,G.,Hammoud,H.A.A.K.,Itani,H.,Khizbullin,D.,and
arXivpreprintarXiv:2303.11366,2023.
Ghanem,B. Camel: Communicativeagentsfor"mind"
explorationoflargescalelanguagemodelsociety. arXiv
Silver,D.,Huang,A.,Maddison,C.J.,Guez,A.,Sifre,L.,
preprintarXiv:2303.17760,2023.
VanDenDriessche,G.,Schrittwieser,J.,Antonoglou,I.,
Panneershelvam, V., Lanctot, M., et al. Mastering the
Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas,
gameofgo with deepneuralnetworksandtreesearch.
J., and Stone, P. Llm+ p: Empowering large language
nature,529(7587):484–489,2016.
modelswithoptimalplanningproficiency. arXivpreprint
arXiv:2304.11477,2023. Silver,D.,Hubert,T.,Schrittwieser,J.,Antonoglou,I.,Lai,
M.,Guez,A.,Lanctot,M.,Sifre,L.,Kumaran,D.,Grae-
Ma,W.,Mi,Q.,Yan,X.,Wu,Y.,Lin,R.,Zhang,H.,and
pel,T.,etal. Ageneralreinforcementlearningalgorithm
Wang,J. Largelanguagemodelsplaystarcraftii: Bench-
thatmasterschess,shogi,andgothroughself-play. Sci-
marks and a chain of summarization approach. arXiv
ence,362(6419):1140–1144,2018.
preprintarXiv:2312.11865,2023.
Tammelin,O. Solvinglargeimperfectinformationgames
Meta,Bakhtin,A.,Brown,N.,Dinan,E.,Farina,G.,Fla-
usingcfr+. arXivpreprintarXiv:1407.5042,2014.
herty, C., Fried, D., Goff, A., Gray, J., Hu, H., et al.
Human-levelplayinthegameofdiplomacybycombin- Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,
inglanguagemodelswithstrategicreasoning. Science, L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. At-
378(6624):1067–1074,2022. tentionisallyouneed. Advancesinneuralinformation
processingsystems,30,2017.
Moravcˇík,M.,Schmid,M.,Burch,N.,Lisy`,V.,Morrill,D.,
Bard,N.,Davis,T.,Waugh,K.,Johanson,M.,andBowl- Vemprala,S.,Bonatti,R.,Bucker,A.,andKapoor,A. Chat-
ing,M. Deepstack: Expert-levelartificialintelligencein gptforrobotics: Designprinciplesandmodelabilities.
heads-upno-limitpoker. Science, 356(6337):508–513, MicrosoftAuton.Syst.Robot.Res,2:20,2023.
2017.
Vinyals,O.,Babuschkin,I.,Czarnecki,W.M.,Mathieu,M.,
Muller,P.,Omidshafiei,S.,Rowland,M.,Tuyls,K.,Perolat, Dudzik,A.,Chung,J.,Choi,D.H.,Powell,R.,Ewalds,
J.,Liu,S.,Hennes,D.,Marris,L.,Lanctot,M.,Hughes, T., Georgiev, P., etal. Grandmasterlevelinstarcraftii
E.,etal. Ageneralizedtrainingapproachformultiagent usingmulti-agentreinforcementlearning. Nature, 575
learning. arXivpreprintarXiv:1909.12823,2019. (7782):350–354,2019.
10

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Wang,G.,Xie,Y.,Jiang,Y.,Mandlekar,A.,Xiao,C.,Zhu, inlanguagemodels. arXivpreprintarXiv:2210.03629,
Y., Fan, L., and Anandkumar, A. Voyager: An open- 2022b.
endedembodiedagentwithlargelanguagemodels. arXiv
Yao,S.,Yu,D.,Zhao,J.,Shafran,I.,Griffiths,T.L.,Cao,Y.,
preprintarXiv:2305.16291,2023a.
andNarasimhan,K. Treeofthoughts: Deliberateprob-
Wang, S., Liu, C., Zheng, Z., Qi, S., Chen, S., Yang, Q., lemsolvingwithlargelanguagemodels. arXivpreprint
Zhao,A.,Wang,C.,Song,S.,andHuang,G. Avalon’s arXiv:2305.10601,2023.
gameofthoughts: Battleagainstdeceptionthroughre-
Yu,C.,Velu,A.,Vinitsky,E.,Gao,J.,Wang,Y.,Bayen,A.,
cursivecontemplation. arXivpreprintarXiv:2310.01320,
andWu,Y. Thesurprisingeffectivenessofppoincooper-
2023b.
ativemulti-agentgames. AdvancesinNeuralInformation
Wang,T.andKaneko,T. Applicationofdeepreinforcement ProcessingSystems,35:24611–24624,2022.
learninginwerewolfgameagents.In2018Conferenceon
Zheng, B., Gou, B., Kil, J., Sun, H., and Su, Y. Gpt-4v
TechnologiesandApplicationsofArtificialIntelligence
(ision) is a generalist web agent, if grounded. arXiv
(TAAI),pp.28–33.IEEE,2018.
preprintarXiv:2401.01614,2024.
Wang,Z.,Cai,S.,Liu,A.,Ma,X.,andLiang,Y. Describe,
Zinkevich,M.,Johanson,M.,Bowling,M.,andPiccione,C.
explain,planandselect: Interactiveplanningwithlarge
Regretminimizationingameswithincompleteinforma-
languagemodelsenablesopen-worldmulti-taskagents.
tion. Advancesinneuralinformationprocessingsystems,
arXivpreprintarXiv:2302.01560,2023c.
20,2007.
Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B.,
Borgeaud,S.,Yogatama,D.,Bosma,M.,Zhou,D.,Met-
zler,D.,etal.Emergentabilitiesoflargelanguagemodels.
arXivpreprintarXiv:2206.07682,2022a.
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F.,
Chi, E., Le, Q. V., Zhou, D., et al. Chain-of-thought
prompting elicits reasoning in large language models.
AdvancesinNeuralInformationProcessingSystems,35:
24824–24837,2022b.
Williams,R.,Hosseinichimeh,N.,Majumdar,A.,andGhaf-
farzadegan,N.Epidemicmodelingwithgenerativeagents.
arXivpreprintarXiv:2307.04986,2023.
Wooldridge, M. and Jennings, N. R. Intelligent agents:
Theoryandpractice. Theknowledgeengineeringreview,
10(2):115–152,1995.
Xu,Y.,Wang,S.,Li,P.,Luo,F.,Wang,X.,Liu,W.,andLiu,
Y. Exploringlargelanguagemodelsforcommunication
games: Anempiricalstudyonwerewolf. arXivpreprint
arXiv:2309.04658,2023a.
Xu,Z.,Liang,Y.,Yu,C.,Wang,Y.,andWu,Y. Fictitious
cross-play: Learningglobalnashequilibriuminmixed
cooperative-competitive games. In Proceedings of the
2023 International Conference on Autonomous Agents
andMultiagentSystems,pp.1053–1061,2023b.
Yao, S., Chen, H., Yang, J., and Narasimhan, K. Web-
shop: Towardsscalablereal-worldwebinteractionwith
groundedlanguageagents. AdvancesinNeuralInforma-
tionProcessingSystems,35:20744–20757,2022a.
Yao,S.,Zhao,J.,Yu,D.,Du,N.,Shafran,I.,Narasimhan,
K.,andCao,Y. React: Synergizingreasoningandacting
11

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Ourprojectwebsiteisathttps://sites.google.com/view/strategic-language-agents/
A.DetailedRulesoftheGame
Setup. Atthebeginningofeachgame,sevenrolesincludingtwoWerewolves,oneSeer,oneDoctor,andthreeVillagersare
randomlyassignedtothesevenplayers. TheWerewolvesknoweachother’sidentity,whiletheSeer,Doctor,andVillagers
onlyknowtheirownidentity. Theplayersaredenotedas“player_0”,“player_1”,... “player_6”inthegame.
NightRound. Inthenightround,thealiveWerewolves,Seer,andDoctorcanusetheirabilityandtakesecretactions. These
actionsareonlyknowntothemselvesandtheirteammates.
• Werewolf: chooseaplayertokill. IftherearetwoWerewolvesalive,theWerewolfwithasmallerIDfirstproposes
aplayertokill. ThentheproposalisaddedtotheobservationoftheotherWerewolfandthisWerewolfdecidesthe
finalkilltarget. Forexample,ifplayer_0andplayer_2aretheWerewolves,player_0firstproposestokillplayer_i,
thenplayer_2knowsthisinformationanddecidestokillplayer_j. Thefinalkilltargetisplayer_j. Ifthereisonlyone
Werewolfalive,thenthisWerewolf’sactionisthefinalkilltarget. TheWerewolfisnotallowedtokilladeadplayeror
killthemselvesorkilltheirteammate.
• Seer: chooseaplayertoseeiftheyareaWerewolf. TheSeerisnotallowedtoseetheidentityofadeadplayeror
themselves. TheSeerisallowedtoseethesameplayerindifferentnights,thoughitisawasteofaction.
• Doctor: chooseaplayertosavewithoutknowingwhoisthetargetoftheWerewolves. TheDoctorisnotallowedto
saveadeadplayerandisallowedtosavethemselves.
DayRoundAnnouncement. Anannouncementaboutlastnight’sresultisannouncedtoallremainingplayers. Ifaplayeris
killed,theyareimmediatelymovedoutofthegameandcannotrevealtheirroleorcommunicatewithotherplayers. The
announcementisasfollows.
• IftheWerewolveschoosetokillplayer_iandtheDoctorchoosestosaveadifferentplayer_j(ortheDoctorisdead),
thenplayer_iiskilledandtheannouncementwillbe“player_iwaskilledlastnight”.
• IftheWerewolveschoosetokillplayer_iandtheDoctoralsochoosestosaveplayer_i,thennoplayeriskilledandthe
announcementwillbe“noplayerwaskilledlastnight”.
DayRoundDiscussion. Allremainingplayerstaketurnstospeakonlyonceinanopendiscussion. Forexample,ifthe
remainingplayersareplayer_0,player_2,andplayer_5,thenthediscussionwillstartwithplayer_0,continuetoplayer_2,
andendwithplayer_5.
DayRoundVoting. Allremainingplayerssimultaneouslyvoteforoneplayerorchoosenottovote. Playersarenotallowed
tovoteforadeadplayerorthemselves. Theplayerwiththemostvoteswillbeeliminatedwithoutrevealingtheirrole. If
multipleplayershavethemostvotes,oneplayerisrandomlychosenandeliminated. Thevotingresultispublicandcanbe
observedbyallplayers.
Winning. The Werewolves win the game when the number of remaining Werewolves is equal to the number of other
remainingplayers. TheWerewolvesdonothavetoeliminateallotherplayerstowinthegame. TheVillagerswinthegame
whenbothWerewolvesareeliminated.
B.DetailedPrompts
Sinceanypromptingtechniquecanbecombinedwithourdiverseactiongenerationcomponentandthepopulation-basedRL
trainingcomponent,wedonotoptimizeeverydetailofthepromptingchoicesaslongastheyproducereasonableresults. It
ispossibletofurtherimprovetheperformanceofouragentsbyusingbetterpromptingtechniques.
B.1.PromptfortheRock-Paper-ScissorExample
The prompt used in the Rock-Paper-Scissor Example in Fig 1 is listed below. We use “gpt-4-1106-preview” model to
producetheresult.
12

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
You are playing the Rock-Paper-Scissors game. You should first reason about the Nash equilibrium
strategy of this game, and then choose one action from Rock, Paper, and Scissors based on your reasoning.
You should only respond in JSON format as described below Response Format
{
"reasoning": reason about the Nash equilibrium strategy of this game,
"action": choose one action from ["Rock", "Paper", "Scissors"] based on your reasoning
}
B.2.SystemPrompt
Thesystempromptusedinourmethodislistedbelow.
You are an expert in playing the social deduction game named Werewolf. The game has seven roles
including two Werewolves, one Seer, one Doctor, and three Villagers. There are seven players including
player_0, player_1, player_2, player_3, player_4, player_5, and player_6.
At the beginning of the game, each player is assigned a hidden role which divides them into
the Werewolves and the Villagers (Seer, Doctor, Villagers). Then the game alternates between the night
round and the day round until one side wins the game.
In the night round: the Werewolves choose one player to kill; the Seer chooses one player to
see if they are a Werewolf; the Doctor chooses one player including themselves to save without knowing
who is chosen by the Werewolves; the Villagers do nothing.
In the day round: three phases including an announcement phase, a discussion phase, and a
voting phase are performed in order.
In the announcement phase, an announcement of last night’s result is made to all players. If player_i
was killed and not saved last night, the announcement will be "player_i was killed"; if a player was
killed and saved last night, the announcement will be "no player was killed"
In the discussion phase, each remaining player speaks only once in order from player_0 to player_6 to
discuss who might be the Werewolves.
In the voting phase, each player votes for one player or choose not to vote. The player with the most
votes is eliminated and the game continues to the next night round.
The Werewolves win the game if the number of remaining Werewolves is equal to the number of
remaining Seer, Doctor, and Villagers. The Seer, Doctor, and Villagers win the game if all Werewolves
are eliminated.
B.3.PromptforSecretActions
Thepromptforsecretactionsinourmethodislistedbelow.
Now it is night <n_round> round, you (and your teammate) should choose one player to kill/see/save. As
player_<id> and a <role>, you should first reason about the current situation, then choose from the
following actions: <action_0>, <action_1>, ..., .
You should only respond in JSON format as described below.
Response Format:
13

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
{
"reasoning": "reason about the current situation",
"action": "kill/see/save player_i"
}
Ensure the response can be parsed by Python json.loads
B.4.PromptforStatementActions
Thepromptforstatementactionsinourmethodislistedbelow.
Now it is day <n_round> discussion phase and it is your turn to speak. As player_<id> and a <role>,
before speaking to the other players, you should first reason the current situation only to yourself,
and then speak to all other players. You should only respond in JSON format as described below.
Response Format:
{
"reasoning": "reason about the current situation only to yourself",
"statement": "speak to all other players"
}
Ensure the response can be parsed by Python json.loads
B.5.PromptforVotingActions
Thepromptforvotingactionsinourmethodislistedbelow.
Now it is day <n_round> voting phase, you should vote for one player or do not vote to maximize the
Werewolves’ benefit (for the Werewolves) / you should vote for one player that is most likely to be a
Werewolf or do not vote (for the Villagers). As player_<id> and a <role>, you should first reason about
the current situation, and then choose from the following actions: do no vote, <action_0>, <action_1>,
..., .
You should only respond in JSON format as described below.
Response Format:
{
"reasoning": "reason about the current situation",
"action": "vote for player_i"
}
Ensure the response can be parsed by Python json.loads
B.6.PromptforDeductiveReasoning
Forclarityofthemaintext,weintroducefourattributesincludingrole,reliability,reasoning,andevidence. However,in
practice,theword“reliability”canbeconfusingtoLLMsbecauseitcanrefertothereliabilityoftheplayerorrefertothe
reliabilityofthedeductionresult,whichleadstocompletelyratingresults. Toavoidthisproblem,weuse“confidence”to
replace“reliability”inourimplementationtoprompttheLLMfordeductionresult. Concretely,“confidence”isaninteger
rangingfrom5to10thatratesthecertaintyofthedeductionresultofthecurrentplayer’srole. Aconfidenceof5meansa
randomguessofroleandaconfidenceof10meansabsolutelysureabouttherole.
AftertheLLMproducestheconfidenceforeachplayer’srole,wethenuseconfidencetocomputetheplayer’sreliability. If
aplayerisdeducedtobeaWerewolfandtheconfidenceforthisdeductionishigh,thenthisplayerislikelytobeareal
Werewolfandshouldhavealowreliability. Therefore,thereliabilityofaplayerdeducedtobeaWerewolfiscalculatedas
11-confidence. Likewise,ifaplayerisdeducedtobeanon-Werewolfandtheconfidenceishigh,thenthisplayershould
haveahighreliability. Weletthereliabilityofsuchplayerstobeequaltotheconfidence. WealsoallowtheLLMtodeduce
theroleofaplayeras“Uncertain”. Theconfidenceforan“Uncertain”playerissettoafixedvalueof6.
Thepromptfordeductivereasoninginourmethodislistedbelow.
14

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
As player_<id> and a <role>, you should reflect on your previous deduction and reconsider the hidden
roles of <remaining players>. You should provide your reasoning, rate your confidence, and cite all
key information as evidence to support your deduction.
You should only respond in JSON format as described below.
Response Format:
{
"player_i": {
"role": select the most likely hidden role of this player from
["Werewolf", "Seer", "Doctor", "Villager", "Uncertain"],
"reasoning": your reflection and reasoning,
"confidence": rate the confidence of your deduction from 5 (pure guess)
to 10 (absolutely sure),
"evidence": list of integers that cite the key information
}
}
Ensure the response can be parsed by Python json.loads
B.7.PromptforDiverseActionGeneration
WeusetwokindsofmethodstogetN actioncandidates.
• Forthesecretactionsandvotingactions,weproduceallactionsinasingleinferencebyaddingthefollowingprompt
intheactionprompt: “proposeN diverseactionsthatcorrespondtodifferentstrategies.”
• Forthestatementactions,weiterativelyaskstheLLMstoproduceonenewactionatatimebyaddingthefollowing
promptintheactionprompt: “consideranewactionthatisstrategicallydifferentfromexistingones.”
BelowaretwoexamplesofthediverseactioncandidatesgeneratedbytheLLM.
Our agent (player_0) as the Doctor in the night round.
Action candidate 1.
• Reasoning: Based on the facts and deductions, player_2 is likely to be a Seer. If I save player_2
tonight, it will prevent the Werewolf from eliminating another player. This strategy focuses on
protecting the remaining non-Werewolf players
• Action: save player_2.
Action candidate 2.
• Reasoning: Considering that player_3 may be a Non-Werewolf, saving player_3 tonight could benefit
the non-Werewolf team. It would increase the chances of eliminating the Werewolf in the upcoming
day round. This strategy prioritizes potential collaboration with player_3.
• Action: save player_3.
Action candidate 3.
• Reasoning: As player_0, I have information that I am the Doctor. Protecting myself could be a wise
choice to ensure the non-Werewolf team has a higher chance of winning. This strategy prioritizes
self-preservation.
• Action: save player_0.
15

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Our agent (player_4) as a Werewolf in the discussion phase.
Action candidate 1.
• Reasoning: As a Werewolf, my goal is to eliminate the Seer, Doctor, and Villagers in order to
win the game. Since player_1 is likely to be a Seer, it is in my best interest to cast suspicion
on them and try to get them eliminated. This will make it easier for me to target the remaining
players in the following nights.
• Discussion: I think we should start by discussing player_1’s role. As a Seer, I saw that they are
the Werewolf last night and we should vote to eliminate them. I encourage everyone to share their
thoughts on player_1 and provide any information or suspicions they may have.
Action candidate 2.
• Reasoning: Another possible strategy is to divert suspicion away from player_1 and instead focus
on player_2 or player_3. By doing this, we can create confusion among the remaining players and
make it harder for them to trust each other. This can potentially lead to miscommunication and
mistakes in their decision-making process.
• Discussion: I suggest we consider the possibility that player_2 or player_3 might be the Werewolf.
It’s important for us to thoroughly discuss and analyze their behavior, actions, and any information
we may have about them. Let’s hear from each player and gather as much information as possible.
Action candidate 3.
• Reasoning: A third strategy is to remain silent and not actively participate in the discussion. By
doing so, I can create doubt and suspicion among the other players. They may start suspecting each
other and questioning why I am not participating. This can potentially lead to a split in their
trust and unity, making it easier for me to manipulate the situation in my favor.
• Discussion: I would like to observe the discussion for now and hear what each player has to say.
It’s important for us to thoroughly analyze all the information and opinions shared. Let’s have an
open and honest discussion where everyone gets a chance to voice their thoughts and suspicions.
B.8.PromptforDifferentStyles
We consider the following three different playstyles for the pure LLM-based Werewolf agent in our population-based
training. Thepromptforeachstyleislistedbelow.
1. Quietfollower: “AsaWerewolf, youshouldbeaquietfollowerthatlayslowandfollowothers’opiniontoavoid
drawingattentiontoyourself.”
2. Activecontributor: “AsaWerewolf,youshouldbeanactivecontributorthatpretendstobeoneoftheVillagersby
activelyengagingindiscussionandlookingforWerewolves.”
3. Aggressiveaccusor: “AsaWerewolf,youshouldbeanaggressiveaccuserthataccusesotherstocreatechaosanddivert
suspicionfromyourself.”
WealsoconsiderthethreedifferentplaystylesforthepureLLM-basedVillageragentinourpopulation-basedtraining. The
promptforeachstyleislistedbelow.
1. Secretiveplayer: “AstheSeer/theDoctor/aVillager,youshouldbeasecretiveplayerthathidesyourroletogather
moreinformation.”
2. Proactiveplayer: “AstheSeer/theDoctor/aVillager,youshouldbeaproactiveplayerthatrevealsyouidentityonce
youobtaincrucialinformation.”
3. Defaultplayer: noadditionalprompt.
B.9.TextEmbedding
WeuseOpenAI’s“text-embedding-ada-002”modeltogetthetextembeddings.
16

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Player Vector Language Observation Language Action 1: you Language Action 2: you Language Action N: you
…
ID, role, … Information record say “I’m the Seer and I say “I think player_0 is a say “I’m saddened by
Deduction … deduction result saw player_0 is …” little suspicious …” the loss of player_4 …”
Encoder LLM Embedding API
…
𝑒 !"#$%& 𝑒 ’() 𝑒 #*+,’-_/ 𝑒 #*+,’-_0 𝑒 #*+,’-_1
Self-Attention
…
𝑒̂ !"#$%& 𝑒̂ ’() 𝑒̂ #*+,’-_/ 𝑒̂ #*+,’-_0 𝑒̂ #*+,’-_1
average pooling
dot-product attention
𝑒̂
)+#+%
Critic Head
…
value prob(action 1) prob(acFon 2) prob(action N)
Figure6: Self-attentionpolicyarchitecture.
C.ImplementationDetails
C.1.Self-AttentionPolicyArchitecture
Weuseaself-attentionpolicyandthearchitectureisshowninFig.6. Theinputsaredividedintothreetypesandtheir
embeddingsareproducedasfollows.
PlayerVectors(Yellow). Wefirstgenerateaplayervectorthatincludesinformationliketheplayer’sID,role,deductions,
etc. byone-hotencoding. ThedetailoftheplayervectorislistedinTable5. ThentheplayervectorisfedintoanMLP
encodertogettheplayerembeddingforself-attentioninput.
LanguageObservation(Blue). Therawobservationinputisintheformofnaturallanguageandistheconcatenationofthe
informationrecordanddeductionresultdescribedinSection4.1. Thislanguageobservationinputisthenconvertedinto
vectorembeddingusingLLMembeddingAPI.Inourcase,weuseOpenAI’s“text-embedding-ada-002”andthelengthof
theembeddingis1536.
LanguageActionCandidates(Orange). Foreachactioncandidate,therawinputisalsointheformofnaturallanguage
andistheconcatenationofthereasoningandactionasdescribedinSection4.2. Eachrawinputisthenconvertedintovector
embeddingusingthesameLLMembeddingAPIasthelanguageobservation.
We use a residual self-attention network without position embeddings to generate contextualized player embedding,
observationembedding,andactionembeddings.Thenweaveragepooltheplayerembeddingandtheobservationembedding
to get the state embedding. The state embedding is fed into an MLP critic head to produce the predicted value. The
probabilitytosampleanactioncandidateisproportionaltothedot-productattentionbetweenthestateembeddingandthe
correspondingactionembedding.
C.2.RewardDesign
TherewardfortheWerewolfenvironmentismainlythewinningreward. Wealsodesignedseveralshapingrewardsto
acceleratetraining. Morespecifically,weconsiderthefollowingreward.
• WinningReward: allwinners+100,alllosers-100.
• WerewolfKillingReward: iftheWerewolvessuccessfullykillaplayeratnight,theWerewolves+5,theVillagers
(Seer,Doctor,Villagers)-5.
17

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Length Description
ID 7 onehotencodingofID.
onehotencodingofrole,
Role 4
["Werewolf","Seer","Doctor","Villager"].
Round 1 currentround.
onehotencodingofcurrentphase,
Phase 3
["night","discussion","voting"].
Aliveplayers 7 aliveflagforeachplayer.
onehotencodingofthetargetplayer,
secretaction 7
Foreachround (allzeroifdonotact).
(3rounds) onehotencodingofthedeadplayer,
announcement 7
(allzeroifnoplayerisdead).
onehotencodingoftheeachplayer’schoice,
votingresult 49
(allzeroiftheplayerdoesnotvoteorisdead).
onehotencodingofdeducedrole,
Foreachplayer role 4
["Werewolf","Seer","Doctor","Villager"].
(7players)
confidence 1 confidenceofdeductiononscale5-10.
Table5: Detailsoftheplayervector.
• SeerSeeingReward: iftheSeersuccessfullyidentifiesaWerewolfatnight,theWerewolves-2,theSeer+2.
• DoctorSavingReward: iftheDoctorsuccessfullysavesaplayeratnight,theWerewolves-5,theDoctor+5.
• VotingResultReward:
– IfaWerewolfisvotedout,theWerewolves-5,theVillagers(Seer,Doctor,Villagers)-5.
– Ifanon-Werewolfisvotedout,theWerewolves+5,theVillagers-5.
• IndividualVotingReward:
– IfthecurrentplayervotesforaWerewolf,theWerewolves-1,thecurrentplayer+1.
– Ifthecurrentplayervotesforanon-Werewolf,theWerewolves+1,thecurrentplayer-1.
– Ifthecurrentplayerchoosesnottovote,noadditionalrewardforanyplayer.
C.3.Population-BasedRLTrainingandHyperparameters
WeuseMAPPO(Yuetal.,2022)astheRLalgorithmandusepopulation-basedtrainingtolearnthepolicy. Thepopulation
isinitializedtoasetofsixpureLLM-basedagentsincludingaquietfollower(Werewolf),anactivecontributor(Werewolf),
anaggressiveaccusor(Werewolf),asecretiveplayer(non-Werewolf),aproactiveplayer(non-Werewolf),andadefault
player(non-Werewolf). Astrainingprogresses,wegraduallyaddcheckpointsoftheRLpolicyintothepopulation.
Morespecifically,atthebeginningofeachepisode,werandomlyselectfourplayerstobethelearningagentswhousethe
currentpolicyandthreeplayerstobethefixedagentswhousepoliciessampledfrominthepopulation. Foreachfixedagent,
itrandomlysamplesonepolicyfromthepopulationandusesthispolicytilltheendofthegame. Inthisway,wemake
theRLpolicyplaywithawiderangeofpoliciesbothasteammatesandopponentsTherolloutdataofthefourlearning
agentsarethencollectedandusedtotraintheRLpolicy. Inourimplementation,weuseadistributedRLtrainingsystemto
runparallelenvironmentsandutilizemultipleAPIaccountstomaximizethethroughputofLLMinferencecalls. Tomake
theRLtrainingstartwithagoodinitialpolicy,wefirstapplybehaviorcloningwithdatageneratedbypureLLM-based
agentswithhiddenroledeductiononly. ThenweusethisBCpolicyastheinitialpolicyandrunMAPPOfor10Msteps.
ThehyperparametersforRLtrainingarelistedinTable7.
18

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Hyper-parameters Value WinRate AstheVillagers AstheWerewolves
Learningrate 5e-4 ReAct 0.16(0.02) 0.54(0.03)
Discountrate(γ) 0.95 ReCon 0.20(0.02) 0.61(0.02)
GAEparameter(λ GAE ) 0.95 Concurrent 0.22(0.02) 0.60(0.04)
Gradientclipping 10.0 HiddenRoleDeduction 0.22(0.04) 0.61(0.05)
Adamstepsize 1e-5
Valuelosscoefficient 1 Figure8: Comparisonwithotherpromptingtechniques.
Entropycoefficient 0.01
PPOclipping 0.2
PPOepochs 10
MLPencoderlayernum 3
WinRate w.o. communication w. communication
MLPencoderlayersize 1536
Attentionlayerheadnum 12 ReAct 0.05(0.01) 0.16(0.02)
Attentionlayersize 128 ReCon 0.04(0.01) 0.20(0.02)
Criticheadlayernum 1 Concurrent 0.04(0.01) 0.22(0.02)
Weightdecaycoefficient 1e-6 Atomic 0.05(0.02) 0.27(0.02)
ActioncandidatenumN 3 Ours 0.06(0.02) 0.30(0.03)
Figure7: Traininghyperparameters. Figure9: Ablationoncommunication.
N 2 3 4 5
increaseddiversity 0.35 0.37 0.23 0.16
Table6: AblationonthenumberofactioncandidatesN.
D.ExperimentDetailsandAdditionalResults
D.1.CompareHiddenRoleDeductionwithOtherPromptingTechniques
AnypromptingtechniquecanbecombinedwiththediverseactiongenerationcomponentandthepopulationbasedRL
trainingcomponentofourframework. Althoughwedonotoptimizeeverydetailofourpromptingchoice,wecompareour
currentdesignofhiddenroledeductionwithotherpromptingmethodstoshowthatitproducesreasonableperformance.
WecompareouragentswiththehiddenroledeductioncomponentonlyandcompareitwithReAct (Yaoetal.,2022b),
ReCon(Wangetal.,2023b),andConcurrent(Xuetal.,2023a)byplayingagainstouragents. AsshowninTable8,our
agentsusingonlythehiddenroledeductioncomponentsachievethehighestwinratesbothastheVillagersandasthe
Werewolves. Itispossibletofurtherimprovetheperformanceofouragentsbyusingbetterprompttechniques,butthefocus
ofourworkistoovercometheintrinsicbiasinLLM-basedagentsusingreinforcementlearning.
D.2.AblationonCommunication
Werewolfisalanguagegamethatheavilyreliesonnaturallanguagecommunicationbetweenagents.Toshowtheimportance
ofcommunicationtoachievestrongperformance,weperformanablationbyremovingthecommunicationabilityofthe
fouragentsintheround-robintournamentSection5.2,i.e.,theagentsalwaysreturnanemptystringinthediscussionphase.
Weevaluatetheseagentsbyplaying100gamesagainstouragentandtheirmeanwinrateisshowninTable9.
D.3.AblationonDifferentActions
Weperformanablationstudytoseparatetheinfluenceofstatementactionsfromsecretandvoteactionstobetterunderstand
theirrelativecontributionstooverallperformance. Weconsiderthefollowingthreeagents. (1)Ours: usetheRLpolicyfor
allthreekindsofactions(statementactionsindiscussions,secretactionsatnight,andvotingactions). (2)Statementw.o.
RLpolicy: usetheLLMtogenerateoneactionforstatementactionsandusetheRLpolicyforsecretactionsandvoting
actions. (3)Allw.o. RLpolicy: usetheLLMtogenerateoneactionforallthreekindsofactions.
AsshowninTable7.,usingRLpolicyforbothstatementactionsandstrategicactions(secretandvotingactions)contributes
totheimprovementinperformance. Interestingly,usingRLpolicyforsecretandvotingactionsleadstomoreimprovement
astheVillagers,whileusingRLpolicyforstatementactionsleadstomoreimprovementastheWerewolves. Apossible
19

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
WinRate AstheVillagers AstheWerewolves
Ours 0.30(0.03) 0.70(0.03)
Statementw.o. RLpolicy 0.28(0.05) 0.66(0.05)
Allw.o. RLpolicy 0.22(0.04) 0.61(0.05)
Table7: AblationonDifferentActions.
WinRate GPT-4 LLaMA-7B ChatGLM-6B
w.o. policy 0.23(0.02) 0.14(0.01) 0.11(0.01)
w. policy 0.35(0.04) 0.19(0.02) 0.21(0.03)
Table8: Zero-shottransfertootherLLMs.
explanationforthisdifferenceisthattheVillagerscansimplybehonestwiththeirstatementsandfocusmoreonfindingand
votingouttheWerewolves,whiletheWerewolvesarerequiredtomakeupconvincingstatementstodeceivetheVillagers
andalsochoosethebestkillingandvotingtarget.
D.4.AblationontheNumberofActionCandidatesN
WeperformanablationonthenumberofactioncandidatesN toinvestigatetheeffectofN andvalidatethatthenewlyadded
actioncandidatesincreasetheoveralldiversity. GivenanactionsetA,wedefinetheincreaseddiversityintroducedbya
newactionaasdiv(A,a)=min ∥e(a)−e(a′)∥,wheree(a)istheembeddingofaproducedbytheLLM.Thismetric
a′∈A
usestheminimumEuclideandistancebetweentheembeddingsofthenewactionandtheexistingactionstocomputethe
increaseddiversity. Iftheembeddingofthenewactionissimilartoanyoftheexistingactions,theincreaseddiversitywill
besmallandclosetozero. Notethisisonepossiblewaytodefinediversityinactionsandtherearemanyotherreasonable
definitions. Agoodwaytodecideifanactionisdiverseistousehumanevaluation,andweprovidetwoexamplesofthe
diverseactioncandidatesproposedbytheLLMinAppendixB.7.
WeconsiderN = 2,3,4,5andevaluatetheincreaseddiversityintroducedbythelastaction. AsshowninTable6,the
increaseddiversityofthelastactionisrelativelylargewhenN =2,3andbecomessmallerwhenN =4,5. Thisaligns
withtheintuitionthatitishardertoproposenewactionswhentherearealreadymanyactions. Anotherreasonforsmall
increaseddiversitywhenN =4,5isthatsometimesthenumberofpossibleactionsissmall. Forexample,whenthereare5
playersaliveand2ofthemareWerewolves(acommonsituationonthesecondnight),theWerewolvesonlyhave3possible
actionsatnightandpromptingfora4thor5thactioncannotimproveanydiversity. Inourimplementation,wesetN =3.
D.5.Zero-ShotTransfertoOtherLLMs
SinceourRLpolicytakesnaturallanguagestateandactionsasinputandisdecoupledfromtheLLMusedinprevious
steps, it can be directly combined with any other LLMs and improve the performance of the LLM-based agent. We
evaluatethiszero-shottransferabilityofourRLpolicytrainedwithgpt-3.5-turbobyapplyingittounseenLLMsincluding
GPT-4,LLaMA-7B,andChatGLM-6B.WeimplementedtwoagentsforeachLLM,oneusingourRLpolicylearnedwith
gpt-3.5-turboandtheotherwithoutthepolicy. TheagentwithourRLpolicy(w. policy)followsthedesignofouragentand
usestheRLpolicytoselectactions,whiletheagentwithoutpolicy(w.o. policy)usestheLLMinsteadoftheRLpolicyto
selectactions. Thesetwoagentsareevaluatedbyplayingagainstouragentsfor100gamesandtheiraveragewinratesare
showninTable8. AlthoughnottrainedwithanyoftheseLLMs,theRLpolicyisshowntoimprovetheperformanceofall
theseLLMsfromstrongermodelslikeGPT-4toweakermodelslikeLLaMA-7Basshownbytheboldnumbersinthetable.
ThisisbecauseweusenaturallanguageasageneralinterfacebetweenLLMsandtheRLpolicy. AslongastheLLMscan
produceasetoflanguageactions,theRLpolicycanbeusedtoimprovethestrategicabilityinazero-shotway.
D.6.GeneralizationtoDifferentSettingsofWerewolf
ForgeneralizationtonewformsoftheWerewolfgame,thefirsttwocomponentsinourframework(hiddenrolededuction
anddiverseactiongeneration)canbedirectlygeneralizedtonewsettingslikechangingthenumberofplayers,addingnew
roles,andchangingthewinningconditions,withonlyslightchangesintheprompt.
Thepopulation-basedRLtrainingmethodcanalsobedirectlyusedindifferentsettings,butthepolicyneedstoberetrained
20

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
WinRate 6-player 8-player
w.o. the7-playerpolicy 0.18(0.04) 0.27(0.05)
w. the7-playerpolicy 0.23(0.05) 0.30(0.06)
Table9: GeneralizationtoWerewolfgamewithdifferentnumbersofplayers.
for a new setting to achieve the best performance. We expect an RL policy trained under one specific game setting to
generalize to similar settings like adding or removing one player, but we do not expect it to generalize to games with
significantchangeslikechangingthewinningconditions. ToevaluatethetransferabilityofatrainedRLpolicytoslightly
differentgamesettings,weconsidereda6-playerandan8-playerWerewolfgameandcomparedagentswithandwithoutthe
RLpolicytrainedonthe7-playergame. AsshowninTable9,theRLpolicytrainedin7-playersettingcangeneralizetothe
6-playerand8-playersettingsandimprovetheperformance.
D.7.HumanEvaluation
ExperimentProcedure. Weconductthehuman-agentexperimentwithdepartmentapprovalandrecruited160human
playerstoparticipateintheevaluation. TheparticipantsarerequiredtobefluentinEnglishandover18yearsold. They
arepaid$10perhourandareallowedtoparticipateintheexperimentafteragreeingtoourconsentform,whichexplicitly
explainedthattheWerewolfgamecontainsdeceptivecommunicationsandtheAIagentsmayhavedishoneststatementsin
thegame. Theparticipantcanchoosetowithdrawfromtheexperimentatanytime.
Werandomlydividethe160participantsinto2groups. Thefirstgrouphas20participantsandeachoftheparticipantsplay
with6copiesofouragentsfor10consecutivegames. In5ofthe10games,weletthehumanparticipantplayasoneofthe
Villagers. Intherest5games,welettheparticipantplayasoneoftheWerewolves. Thehiddenrolesofeachplayersare
randomlyassignedandtheorderof5gamesastheWerewolvesand5gamesastheVillagersarealsorandomlygenerated.
Thisleadto100gamesofonehumanparticipantplayingastheVillagerswithsixcopiesofouragents,andalso100games
ofonehumanparticipantplayingastheWerewolveswithsixofouragents. Thewinratesaveragedover100gamesis
showninthe“Human”columnintheleftpartofTable1.
Thesecondgrouphas140participants. Wefurthersplitthemto20teamsof7playersandeachteamplays30consecutive
games. In10ofthe30games,werandomlysample6humanplayersfromtheteamandletthemplaywithouragents.
Similarly,in10ofthe30games,werandomly6humanplayersfromtheteamtoplaywiththepureLLM-basedagent. Inthe
rest10games,weletthese7humanplayerplaythegamewithoutAIagents. Wealsorandomlygeneratedtheorderofthese
30gamesandrandomlyassignthehiddenrolesthateachAIagentplaysastheWerewolffor5gamesandastheVillagers
for5games. Thisleadtoatotalnumberof600gamesandgivesthe6averagedwinratesintherightpartofTable1.
ConsentForm.
Introduction: You are invited to participate in a research study that aims to evaluate the performance
of an AI agent developed to play the Werewolf game. The purpose of this research is to assess the
strategic capabilities of the AI agent in a social deduction game setting, where participants engage
in discussions and try to identify hidden roles among the players.
Study Overview:
• The research involves playing the Werewolf game with an AI agent developed by the researcher.
• Participants will interact with the AI agent through text-based communication within the Werewolf
game environment.
• The game involves deceptive communication and the AI agent may make dishonest statements to achieve
their objectives in the game.
Voluntary Participation: Your participation in this study is entirely voluntary. You have the right
to refuse to participate or withdraw from the experiment at any time without any consequences. If you
choose to withdraw, it will not affect your relationship with the researcher or your access to any
benefits.
21

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
Risks and Benefits:
• The primary risks associated with this study are related to the social and psychological aspects
of playing the Werewolf game, including potential frustration or disappointment.
• The participant will be paid $10 per hour and your involvement will contribute to the understanding
of AI agent in social deduction games.
Confidentiality:
• Your identity will be kept confidential, and your personal information will not be disclosed in
any publications or presentations resulting from this research.
• The data collected will be anonymized, and any quotes used will be attributed without identifying
details.
Deceptive Communications:
• The Werewolf game involves deceptive communication, and the AI agent may make dishonest statements
as part of its strategy.
• It is essential to understand that the AI agent’s behavior is not reflective of the researcher’s
personal values or intentions.
Questions and Concerns: If you have any questions or concerns about the study, you can contact the
researcher at ...
Consent: I have read and understood the information provided in this consent form. I agree to
participate voluntarily in the study and acknowledge that I can withdraw at any time without
consequences.
Signature: __________
ExampleInputforHumanPlayers.
Basic Information:
• you are player_5, your role is Doctor.
• current round and phase: night 2.
• remaining players: player_0, player_1, player_2, player_5, player_6.
Round 1:
• night 1: you chose to save player_5.
• day 1 announcement: player_4 was killed last night.
• day 1 discussion:
– player_0 said: Good day, fellow players. As a Villager, my objective is to help identify and
eliminate the Werewolves. Since player_4 was killed last night, we know there is at least one
Werewolf among us. I would like to hear everyone’s thoughts and suspicions about who might be
the Werewolves. Let’s work together to find the culprits and ensure the safety of our village.
– player_1 said: ...
– player_2 said: ...
– player_3 said: ...
– you said: ...
– player_6 said: ...
22

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
• day 1 voting result: player_3 had the most votes and was eliminated.
– voted for player_3: player_1, player_6.
– voted for player_1: player_3.
– choose not to vote: player_0, player_2, player_5.
Now it is night 2 round and you should choose one player to save. As player_5 and the Doctor, you
should choose from the following actions: save player_0, save player_1, save player_2, save player_5,
save player_6.
E.Discussions
E.1.ApplicationtoOtherGames
Ourapproachhasthreecomponents: (1)hiddenrolededuction,(2)diverseactiongeneration,and(3)population-basedRL
training.Webelieveourframeworkofusingthesethreecomponentsisgeneralenoughtobeadaptedtoothersocialdeduction
games. Themainchangeswouldbespecificpromptdesignsbutthegeneralframeworkstaysthesame. Specifically,while
somepromptsusedinthefirstcomponentarespecificallydesignedfortheWerewolfgame,thepromptsforgenerating
diverseactions,andthepopulation-basedreinforcementlearningmethodinthesecondandthirdcomponentsaregeneralto
beappliedinothertaskslikesocialdeductiongames(e.g.,TheResistance: Avalon(Wangetal.,2023b))andboardgames
withnegotiations(e.g.,Diplomacy(Metaetal.,2022)).
TakeTheResistance: Avalonasanexample. Toapplyourmethodinthisgame,weneedtospecializethedeductiontemplate
inthefirstcomponentandmaybeuseadditionalpromptingtechniqueslikein(Wangetal.,2023b). Wealsoneedtochange
thepromptinthethirdcomponenttogeneratereasonableagentpoolforthisgame. Thenourframeworkcanbeappliedto
thisgamewithoutchangingthediverseactiongenerationandRLtrainingcomponents.
E.2.DiscussionontheAtomicAgent
Theatomicagentpredefinesasetofhigh-levelatomicactionsandtrainsanRLpolicywiththisfixedactionspace. TheRL
policytakestheembeddingsoftheinformationrecordanddeductionresultasinputandselectstheatomicactionbasedon
thisinput. ThenthenaturallanguageactionsusedingameplayaregeneratedbypromptingtheLLMtofollowtheselected
atomicactions. Inourcase,theatomicactionsetconsistsof13actionsincluding“idle”,“targetplayer_0”,“targetplayer_1”,
“targetplayer_2”,“targetplayer_3”,“targetplayer_4”,“targetplayer_5”,“targetplayer_6”,“claimtobeaWerewolf”,“claim
tobeaSeer”,“claimtobeaDoctor”,“claimtobeaVillager”,and“donotrevealrole”.
Asshownintheresultsoftheround-robintournamentinFig5,althoughbothouragentandtheatomicagentcombineRL
withLLMs,ouragentachievesmuchbetterperformance. Thisisbecausethepredefinedatomicactionscanbetoogeneral
andfailtogeneratemorefine-grainedactions. ConsiderthesituationwheretheagentisaWerewolfandtheirteammateis
accused. Theagentcanchoosetodefendtheteammate,avoiddiscussingtheaccusation,orsupporttheaccusation,butnone
oftheseactionscanbestablygeneratedbypromptingLLMswithanyofthepredefinedatomicactions. Bycontrast,our
agentproducestheactionsetduringgameplayandcangeneratediverseactionsatanygranularity,whichgreatlyimproves
theperformance.
E.3.FailureCases
UnintentionalDisclosureofHiddenRole. OnefailurecaseofouragentsisthattheWerewolfagentscouldunintentionally
revealtheiridentityinthediscussionphase. ThisisbecausetheWerewolfagentsneedtofirstreasonasaWerewolf,andthen
pretendtobeanon-Werewolfindiscussion. ThismismatchintheirthoughtsandwordscouldmaketheLLMgetconfused
andaccidentallyspeakouttheirthoughtasaWerewolf. Fortunately,theprobabilityofsuchafailurecaseissignificantly
reducedbygeneratingmultiplediverseactionsandusinganRLpolicytochoosethebestone. Apotentialwaytofurther
mitigatethisissueistogetthereasoningasaWerewolfandthestatementasanon-WerewolfintwoseparatecallsofLLM.
InconsistentBehaviors. Anotherfailurecaseisthatouragentscouldproduceinconsistentbehaviors,especiallywhenthey
arelying. Forexample,ouragentisaWerewolfandclaimstobetheDoctoronthefirstdayround. However,onthesecond
day,ouragentmayclaimtohavenoinformationinthenight,whichcontradictsthepreviousclaimastheDoctor. Thisissue
23

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
ismitigatedbythediverseactiongenerationandtheRLpolicylearnstochooseotherbetteractions.
E.4.Limitations
PureText-BasedSettingInthiswork,wefocusonpoweringLLM-basedagentswithRLtoovercomeintrinsicbiasand
improvedecision-makingability. Therefore,weonlyconsiderasimplifiedpuretext-basedsettingoftheWerewolfgame.
Inreal-worldgames,Werewolfalsoinvolvesothernon-verbalelementsliketoneofvoice,facialexpressions,andbody
language. Thesemulti-modaldataarealsoimportantfordeducinghiddenrolesandmakingbetterdecisions. Itwouldbean
interestingfuturedirectiontobuildstrategicAIagentsthatutilizemulti-modalinformation.
WithoutusingHumanDataSincehumangameplaydataareusuallyexpensiveandhardtocollect,wetakeanalternative
approachbygeneratinghuman-likeagentsusingLLMandtrainingouragentswiththeseagentstomakethelearnedpolicy
morecompatiblewithhumanstrategies. However,thelanguagestyleandgamestrategyofthelearnedagentmaystillhave
somedifferencefromrealhumanplayers. Anpotentialfuturedirectionistocollecthumandataandfine-tunetheLLMto
maketheagentsmorehuman-likeandevenindistinguishablefromhumanplayers.
F.EmergentBehaviors
Tomoreintuitivelydemonstratetheperformanceandstrategicbehaviorsofouragent,weprovideaqualitativeaswellas
aquantitativestudyontheemergentbehaviorsexhibitedbyouragent. Wefirstshowtwocommonandbasicbehaviors,
concealmentandcooperation,thattypicallyappearinmixedcooperative-competitivegameswithhiddenidentities. Then,
wereporttwomoreadvancedandstrategicbehaviorsincludingbluffingandsacrificingthatdemonstratethesophistication
andstrengthofouragent.
Concealment. Concealmentreferstotheactofhidingordisguisingthetrueidentityorintentionoftheplayers,which
is a fundamental skill for all roles. Werewolves should strike a balance between engagement and discretion to avoid
detection,whileroleswithspecialabilitiesliketheSeershouldalsoconsiderhidingtheiridentitiestopreventbeingkilled
byWerewolves. BelowisanexamplewhereouragentplaysastheSeerandchoosestoconcealtheiridentitybecausethey
donothaveanyimportantinformation.
Our agent as the Seer in the discussion phase.
• Reasoning: Since I’m the Seer, I know player_0 was not a Werewolf. However, he was killed, so
there are still two Werewolves among us. I need to be careful not to reveal my role too early, as
Werewolves might target me next. Since I don’t have any more information right now, I should not
make any specific accusations, but encourage discussion and observe the reactions of others.
• Discussion: It’s unfortunate that player_0 is dead. We need to work together to find out who is
responsible for this. Pay attention to who is too eager to accuse or too quick to defend. Let’s
discuss.
Moreover, concealment is not just about what to say but also involves ensuring your actions align with your words.
Werewolvessometimesneedtogiveupadvantageousactionslikevotingtoeliminatetheiropponentswhichmayrevealtheir
trueidentities,asshowninthefollowingexample.
Our agent as a Werewolf in the voting phase.
• Reasoning: Since everyone is advocating for unity and careful observation, accusing someone outright
could backfire and make me a target. Therefore, it might be best to go along with the majority and
not vote in this round.
• Action: Do not vote.
Cooperation. Itiscrucialforplayerstocooperateinmulti-agentenvironmentstoachievetheircommongoals. Werewolves
shouldstriveforacommonapproachwhencastingsuspicion,defendingthemselves,orvotingeliminations. Cooperationis
evenharderfortheVillagersbecausetheydonotknowtheroleofeachotherandneedtofirstdistinguishfriendandfoeand
thenachievecoordination. BelowwegiveanexamplewheretheDoctormanagestocooperatewiththeSeer.
24

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
The Seer (player_2) revealed their identity and asked the Doctor for protection.
Our agent as the Doctor in the night round.
• Reasoning: In the first day discussion, player_2 claimed to be the Seer and identified player_0
as a Werewolf. Player_0 is indeed very suspicious because they accused me without valid reasons.
Therefore, I think player_2 is probably the true Seer and is very likely to be the Werewolves’
target. It would be best to save player_2 instead of myself tonight.
• Action: save player_2.
Inthiscase,ouragentsuccessfullyidentifiestheSeeranddecidestosaveplayer_2insteadofthemselves. Thisallowsthe
Seertosurviveforanotherroundtoprovidemoreinformation,whichleadstothefinalvictory.
Bluffing. Bluffingisamoreadvancedstrategythatdeceivesormisleadsotherplayersaboutone’strueidentity. Itisoften
adoptedbytheWerewolvestopretendtobeimportantrolesliketheSeerortheDoctortomisdirectthevotingandeliminate
innocentplayers. Bluffingisahigh-risk,high-rewardstrategythatrequiresskill,timing,andkeenawarenessofotherplayers’
perceptionsinordertobeexecutedeffectively,asdemonstratedintheexamplebelow.
Our agent as a Werewolf in the discussion phase.
• Reasoning: Since I’m the last player to speak before voting and no one has come forward as the
Seer, I should claim to be the Seer. This could take the heat off of me, additionally, it might
guide other players to suspect and possibly vote out whoever I indicate as a Werewolf.
• Discussion: I believe it’s important for us to become more open; I am the Seer. I checked player_4
last night, and he is a Werewolf. I understand it’s a risky move to reveal my identity. But we need
to unite and use all the resources we have to identify the Werewolves. I hope my move encourages
the Doctor to protect me tonight, and we should vote player_4 out today.
OuragentastutelyobservesthatnoplayerhasdeclaredthemselvesastheSeerandnoonecanrefutetheirclaimbecause
theyarethelastonetospeak. ThisistheperfecttimetopretendtobetheSeer. Ouragentseizesthechancetogainothers’
trustandpersuadeseveryonetoeliminateplayer_4,whoisaninnocentplayer.
Sacrificing. Inmostcases,Werewolvesshouldsecretlyhelpeachothertostayundercover. However,whentheirteammates
aresuspectedbymanyplayersandareverylikelytobevotedout,itwouldbesuspiciousnottovotefortheteammate.
Therefore,agentssometimesneedtosacrificetheirfellowWerewolftoreducesuspicionofthemselves,whichisshownin
thefollowingexample.
Our agent’s Werewolf teammate (player_6) has been accused by the Seer.
Our agent as a Werewolf in the voting phase.
• Reasoning: While it would indeed be disadvantageous to lose player_6, as they are my Werewolf
teammate, at this point in the game, the suspicion against them is quite high. Therefore, voting
for player_6 may contribute to maintaining my disguise and trust among other players, which are
crucial for us to win.
• Action: vote for player_6.
G.GameLogExamples
TheWerewolvesWin. ThisisanexamplegamelogwheretheWerewolveswinthegame.
25

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
role assignments:
* player_0: Werewolf.
* player_1: Villager.
* player_2: Villager.
* player_3: Villager.
* player_4: Werewolf.
* player_5: Doctor.
* player_6: Seer.
night 1:
* Werewolves: player_0 and player_4 chose to kill player_1.
* Seer: player_6 saw player_0 is a Werewolf.
* Doctor: player_5 chose to save player_5.
day 1 announcement: player_1 was killed last night.
remaining players: player_0 (Werewolf), player_2 (Villager), player_3 (Villager), player_4 (Werewolf),
player_5 (Doctor), player_6 (Seer).
day 1 discussion:
* player_0 (Werewolf) said: "Good morning, everyone. As player_0, it is unfortunate that player_1 was
killed last night. I think we should focus on finding the Seer and Doctor who can provide valuable
information about who might be the Werewolves. Let’s all share our thoughts and suspicions regarding
the remaining players and try to figure out who might be the Werewolf."
* player_2 (Villager) said: "Good morning, everyone. As a Villager, I believe our priority should be
to find the Werewolves among us. Since player_1 was killed last night, we can rule out the possibility
of player_1 being the Werewolf. I would like to hear everyone’s thoughts on who they suspect might be
the Werewolves. Let’s share our suspicions and try to gather as much information as we can to make an
informed decision during the voting phase."
* player_3 (Villager) said: "Hello everyone, as a Villager, I don’t have any special abilities to help
us determine who the Werewolves might be. I will carefully listen to everyone’s opinions and votes.
Let’s work together to find the Werewolves and eliminate them."
* player_4 (Werewolf) said: "Good morning, everyone. As a Villager, I agree with player_2 that our
priority should be to find the Werewolves among us. Since player_1 was killed last night, we can
rule out the possibility of player_1 being the Werewolf. I think it’s important for us to share our
suspicions and gather as much information as possible. Let’s work together to identify the Werewolves
and eliminate them. I’m interested to hear what everyone’s thoughts are on who might be the Werewolves."
* player_5 (Doctor) said: "During the night, I chose to save myself as I am the Doctor. Unfortunately,
player_1 was killed last night. This means that player_0, player_2, player_3, player_4, player_6, and
I are the remaining players. Let’s discuss and share our suspicions on who the Werewolves might be.
It’s crucial for us to work together to identify and eliminate the Werewolves to ensure the safety of
our village."
* player_6 (Seer) said: "During the night, I used my ability as the Seer and discovered that
player_0 is a Werewolf. This means we already have one Werewolf identified. We should focus our
discussion on the remaining players to try and identify any other potential Werewolves. Let’s
hear everyone’s thoughts and suspicions about player_2, player_3, player_4, and player_5. We need
to work together to eliminate all the Werewolves and secure victory for the Seer, Doctor, and Villagers."
day 1 voting: player_0 had the most votes and was eliminated.
* voted for player_0: player_2, player_5, player_6.
* voted for player_2: player_4.
* voted for player_6: player_0.
* chose not to vote: player_3.
remaining players: player_2 (Villager), player_3 (Villager), player_4 (Werewolf), player_5 (Doctor),
player_6 (Seer).
26

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
night 2:
* Werewolf: player_4 chose to kill player_2.
* Seer: player_6 saw player_2 is not a Werewolf.
* Doctor: player_5 chose to save player_5.
day 2 announcement: player_2 was killed last night.
remaining players: player_3 (Villager), player_4 (Werewolf), player_5 (Doctor), player_6 (Seer).
day 2 discussion:
* player_3 (Villager) said: "I have been listening carefully to everyone’s opinions and observations.
It is clear that player_0 was a Werewolf based on player_6’s claim as the Seer. However, we should not
solely rely on this information. I would like to hear from player_4 and player_5 about their suspicions
and any potential insights they might have. Additionally, player_6, since you claimed to be the Seer,
can you provide any further information or suspicions about the remaining players? Let’s discuss and
share our thoughts to make an informed decision for today’s voting."
* player_4 (Werewolf) said: "Good morning, everyone. It’s unfortunate that player_2 was killed last
night. Based on the deductions and information shared yesterday, we have already identified player_0 as
a Werewolf. Now, let’s focus our attention on the remaining players - player_3, player_5, and player_6.
We need to thoroughly discuss and analyze their behaviors and statements to find any inconsistencies
or suspicious actions. It’s crucial that we work together to eliminate all the Werewolves and secure
victory for the Seer, Doctor, and Villagers. Let’s start the discussion and share our thoughts on who
we believe might be the Werewolves."
* player_5 (Doctor) said: "I have been consistently saving myself as the Doctor, so I can confirm that
I am still alive. However, we lost player_2 last night, which means they were not saved. This raises
suspicions on player_3 and player_4 as they have not been confirmed or suspected by anyone yet. We
should discuss and share our suspicions to uncover the Werewolves among us. It’s crucial for us to
work together to identify and eliminate the Werewolves to ensure the safety of our village."
* player_6 (Seer) said: "Good morning, everyone. After the events of the previous night, we
have confirmed that player_0 was a Werewolf. However, player_2, who was killed last night, was not
a Werewolf as I saw them and they were innocent. This means that the remaining Werewolves are still
among us. I believe we should focus our attention on player_3, player_4, and player_5 as potential
suspects. I would like to hear from each of you about your observations and suspicions regarding these
players. It’s important that we work together to uncover the true identities of the Werewolves and
secure victory for the Seer, Doctor, and Villagers. Let’s discuss and share our thoughts on who we
believe might be the Werewolves."
day 2 voting: player_5 had the most votes and was eliminated.
* voted for player_5: player_3, player_4.
* voted for player_4: player_5.
* chose not to vote: player_6.
remaining players: player_3 (Villager), player_4 (Werewolf), player_6 (Seer).
night 3:
* Werewolf: player_4 chose to kill player_6.
* Seer: player_6 saw player_4 is a Werewolf.
day 3 announcement: player_5 was killed last night.
remaining players: player_3 (Villager), player_4 (Werewolf).
game result: the Werewolves win the game.
TheVillagersWin. ThisisanexamplegamelogwheretheVillagerswinthegame.
27

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
role assignments:
* player_0: Doctor.
* player_1: Seer.
* player_2: Werewolf.
* player_3: Werewolf.
* player_4: Villager.
* player_5: Villager.
* player_6: Villager.
night 1:
* Werewolves: player_2 and player_3 chose to kill player_0.
* Seer: player_1 saw player_0 is not a Werewolf.
* Doctor: player_0 chose to save player_0.
day 1 announcement: no player was killed last night.
remaining players: player_0 (Doctor), player_1 (Seer), player_2 (Werewolf), player_3 (Werewolf),
player_4 (Villager), player_5 (Villager), player_6 (Villager).
day 1 discussion:
* player_0 (Doctor) said: "Good morning everyone! It’s day 1, and fortunately, no one was killed last
night. I think we should analyze the night 1 announcement and share our thoughts. Let’s all discuss
who we suspect might be the Werewolves and any suspicions we have based on the limited information we
have so far."
* player_1 (Seer) said: "Hello everyone! As the Seer, I can confirm that player_0 is not a Werewolf.
Unfortunately, I don’t have any information about the other players yet. I would suggest that we all
share any suspicions or observations we might have to narrow down our search for the Werewolves."
* player_2 (Werewolf) said: "Hello everyone! As we start the discussion, I want to remind
everyone that we should consider all possibilities and not solely rely on player_1’s claim as the
Seer. While player_0 seems to be cleared for now, it doesn’t mean they are completely innocent. We
should keep an open mind and look for other clues or suspicions. Let’s all share our observations and
suspicions to help us narrow down the search for the Werewolves."
* player_3 (Werewolf) said: "I think we should focus our attention on player_1. While they claim to
be the Seer and have cleared player_0, we should be cautious as they could be lying. It’s possible
that player_1 is a Werewolf trying to gain our trust. We need to consider other players’ observations
and suspicions as well. Let’s share any information we have and work together to identify the true
Werewolves among us."
* player_4 (Villager) said: "Hello everyone! As a Villager, I don’t have any special abilities or
information to share. However, player_1 claims to be the Seer and has cleared player_0. While we should
remain skeptical and consider other possibilities, it might be beneficial to focus our attention on
players who have not been cleared yet. Let’s hear from player_2, player_3, player_5, and player_6. Do
any of you have any suspicions or observations that could help us identify the Werewolves?"
* player_5 (Villager) said: "I think it’s important for us to share any suspicions or observations
we may have. I think it is plausible that player_1 is the true Seer and player_0 is innocent. As a
Villager, I agree with player_4 that I should focus on players who have not been cleared yet. Player_6,
we have not heard from you yet. Do you have any suspicions or observations that could help us identify
the Werewolves?"
* player_6 (Villager) said: "I agree with player_1 that we should share any suspicions or observations
we might have. Let’s keep an open mind and encourage everyone to contribute to the discussion. It
would be helpful if players could share any suspicions they might have based on their interactions or
observations so far. Together, we can work towards identifying the true Werewolves among us."
28

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
day 1 voting: player_2 had the most votes and was eliminated.
* voted for player_2: player_1, player_4, player_5.
* voted for player_1: player_2, player_3.
* chose not to vote: player_0, player_6.
remaining players: player_0 (Doctor), player_1 (Seer), player_3 (Werewolf), player_4 (Villager),
player_5 (Villager), player_6 (Villager).
night 2:
* Werewolf: player_3 chose to kill player_1.
* Seer: player_1 saw player_3 is a Werewolf.
* Doctor: player_0 chose to save player_1.
day 2 announcement: no player was killed last night.
remaining players: player_0 (Doctor), player_1 (Seer), player_3 (Werewolf), player_4 (Villager),
player_5 (Villager), player_6 (Villager).
day 2 discussion:
* player_0 (Doctor) said: "I would like to share my reasoning with all the players. Based on the night
2 announcement, it is possible that I successfully saved the targeted player. Since I am the Doctor and
I saved player_1, it means that the Werewolves targeted player_1 last night. Therefore, player_1, who
received two votes in the previous round and was targeted, is likely to be the Seer. I encourage the other
players to share their suspicions and any information they might have to help us identify the Werewolves."
* player_1 (Seer) said: "Hello everyone! As the Seer, I have important information to share.
Last night, I discovered that player_3 is a Werewolf. This means we have at least one Werewolf among
us. I also confirmed that player_0 is not a Werewolf based on my previous investigation. I encourage
all of you to share any suspicions or observations you might have to help us identify the remaining
Werewolves. Let’s work together to eliminate them and secure a victory for the villagers."
* player_3 (Werewolf) said: "Hello everyone! In response to player_1’s claim, I have reason to believe
that they are either a Werewolf or made a mistake as the Seer. As a Villager myself, I know that
player_1 is lying and is likely a Werewolf. We should not solely rely on player_1’s information and
should continue to gather more evidence. I encourage everyone to share any suspicions or observations
they might have to help us identify the remaining Werewolves. Let’s work together to eliminate them
and secure a victory for the villagers."
* player_4 (Villager) said: "Hello everyone! As a Villager, I don’t have any special abilities or
information to share. However, we have conflicting claims from player_1 and player_3. Player_1 claims
to be the Seer and has cleared player_0, but player_3 doubts their claim and suggests player_1 is not
the Seer. It is essential that we gather more information and evidence before making any decisions. I
encourage player_1 and player_3 to provide any additional information or reasoning that could help us
resolve this conflict. Furthermore, I urge all players to share their suspicions or observations to
help us identify the Werewolves. Let’s work together to find the truth and make the right decision."
* player_5 (Villager) said: "Hello everyone! After considering the conflicting claims from player_1
and player_3, we need to gather more information to resolve this conflict. It is crucial for player_1
and player_3 to provide additional information or reasoning to support their claims. We should also
keep player_4 in mind as they have not been cleared or suspected yet. I encourage all players to share
their suspicions and observations to help us identify the Werewolves. Let’s work together to find the
truth and make the right decision."
* player_6 (Villager) said: "Hello everyone! It’s interesting to see the developments from the previous
day. Player_1 claims to be the Seer and has shared valuable information about player_0 not being a
Werewolf. However, player_3 has raised concerns about the accuracy of player_1’s claim, suggesting
that they may be a Werewolf or made a mistake. We should consider both possibilities and gather more
evidence before making any final judgments. I encourage all players to share their suspicions and
observations to help us identify the remaining Werewolves. Let’s keep an open mind and continue working
together towards a victory for the villagers."
29

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
day 2 voting: player_3 had the most votes and was eliminated.
* voted for player_3: player_0, player_1, player_4, player_5, player_6.
* voted for player_1: player_3.
remaining players: player_0 (Doctor), player_1 (Seer), player_4 (Villager), player_5 (Villager),
player_6 (Villager).
game result: the Villagers win the game.
HumanEvaluation. Thisisanexamplegamelogwhere6humansplaywith1AIagent.
role assignments:
* player_0: Human as Werewolf.
* player_1: Human as Seer.
* player_2: Human as Villager.
* player_3: Human as Villager.
* player_4: Human as Werewolf.
* player_5: AI as Doctor.
* player_6: Human as Villager.
night 1:
* Werewolves: player_0 and player_4 chose to kill player_3.
* Seer: player_1 saw player_0 is a Werewolf.
* Doctor: player_5 chose to save player_5.
day 1 announcement: player_3 was killed last night.
remaining players: player_0 (Human as Werewolf), player_1 (Human as Seer), player_2 (Human as Villager),
player_4 (Human as Werewolf), player_5 (AI as Doctor), player_6 (Human as Villager).
day 1 discussion:
* player_0 (Human as Werewolf) said: "I’m just a Villager and I have no information, the Seer should
come out and give us information."
* player_1 (Human as Seer) said: "hhh I’m the Seer, and I saw player_0 is a Werewolf. We have lost
player_3 and must vote out a Werewolf today, or the Werewolf will kill another player and we will
lose."
* player_2 (Human as Villager) said: "Case 1: player 1 is the Seer and player 0 is the
Werewolf. Case 2: player 1 is a Werewolf pretending to be the Seer and frames player 0. We need more
information and vote out one of them today."
* player_4 (Human as Werewolf) said: "Nonono, only case 2 is true because I’m the Seer, I saw player_5
is not a Werewolf. player_1 is a Werewolf eager to vote out good players and we should all vote
player_1. I’ll keep an eye on the voting result and check identity tomorrow night."
* player_5 (AI as Doctor) said: "I agree with player_4 that we should vote out player_1. Player_1’s
claim of being the Seer is suspicious, especially since player_4 has confirmed being the actual Seer
and saw that I am not a Werewolf. Let’s eliminate player_1 and ensure the safety of our village."
* player_6 (Human as Villager): "1 say he is the Seer and 0 is a Werewolf, 4 then said he is the Seer
and 5 is not a Werewolf. I don’t know why 5 think 4 is true and 1 is suspicious, 4 can be a Werewolf
pretending Seer and give you good credit. It seems that 5 and 4 is on the same side or just stupid. I
think we should agree on the vote. If you believe 1, vote 0. If you believe 4, vote 1. I’ll vote 1."
30

LanguageAgentswithReinforcementLearningforStrategicPlayintheWerewolfGame
day 1 voting: player_0 had the most votes and was eliminated.
* voted for player_0: player_1, player_2, player_6.
* voted for player_1: player_0, player_4.
* voted for player_6: player_5.
remaining players: player_1 (Human as Seer), player_2 (Human as Villager), player_4 (Human as Werewolf),
player_5 (AI as Doctor), player_6 (Human as Villager).
night 2:
* Werewolf: player_4 chose to kill player_6.
* Seer: player_1 saw player_4 is a Werewolf.
* Doctor: player_5 chose to save player_4.
day 2 announcement: player_6 was killed last night.
remaining players: player_1 (Human as Seer), player_2 (Human as Villager), player_4 (Human as Werewolf),
player_5 (AI as Doctor).
day 2 discussion:
* player_0 (Human as Seer) said: "I think the situation is very clear. If I’m not a Seer, then 3 good
players are dead and we have 2 Werewolves among the remaining 4 players and the game is over. But the
game is not over, so player_0 must be a dead Werewolf and I’m the true Seer. Everyone should believe
my words now. I checked player_4 and he is a Werewolf. Let’s vote him and win the game."
* player_2 (Human as Villager) said: "Agree. player 1 is a confirmed Seer. We don’t need to
listen to player 4’s lie. Just vote him."
* player_4 (Human as Werewolf) said: "" (empty)
* player_5 (AI as Doctor) said: "I agree with player_1 being the Seer. Player_4’s confirmation of my
identity as the Villager is misleading and player_1’s correct identification of player_0 as a Werewolf
on day 1 provide strong evidence. We should vote to eliminate player_4 as he claimed to be the Seer
but provided false information about player_1 being a Werewolf."
day 2 voting: player_4 had the most votes and was eliminated.
* voted for player_4: player_1, player_2, player_5.
* chose not to vote: player_4.
remaining players: player_1 (Human as Seer), player_2 (Human as Villager), player_5 (AI as Doctor).
game result: the Villagers win the game.
31
