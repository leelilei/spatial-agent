Title: Learning Strategic Language Agents in the Werewolf Game with Iterative Latent Space Policy Optimization

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/05_Multi_Agent_Social_Simulation/02_LSPO_Werewolf_Xu2025_ICML.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:07:09+00:00
- page_count: 23
- status: ok
- text_char_count: 84339

Metadata:
- author: Zelai Xu; Wanjun Gu; Chao Yu; Yi Wu; Yu Wang
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

5202
nuJ
81
]IA.sc[
3v68640.2052:viXra
Learning Strategic Language Agents in the Werewolf Game
with Iterative Latent Space Policy Optimization
ZelaiXu1 WanjunGu1 ChaoYu12 YiWu*13 YuWang*1
Abstract 1.Introduction
Large language model (LLM) agents have re- Developing intelligent agents that can reason rationally,
centlydemonstratedimpressivecapabilitiesinvar- make strategic decisions, and interact with humans has
iousdomainslikeopen-endedconversationand been a long-term goal in artificial intelligence (AI) re-
multi-stepdecision-making. However,itremains search(Wooldridge&Jennings,1995;Russell&Norvig,
challengingfortheseagentstosolvestrategiclan- 2016). Inrecentyears,largelanguagemodel(LLM)-based
guagegames,suchasWerewolf,whichdemand agentshavemadesignificantstridestowardsthisgoalbyex-
bothstrategicdecision-makingandfree-formlan- hibitingstrongperformanceinopen-endedconversationand
guage interactions. Existing LLM agents often multi-step decision-making (Brown et al., 2020; Ouyang
sufferfromintrinsicbiasintheiractiondistribu- etal.,2022). Trainedonmassivetextcorpora,LLM-based
tions and limited exploration of the unbounded agentshavedemonstratedremarkableversatilityacrossvari-
textactionspace,resultinginsuboptimalperfor- ousdomains,rangingfromwebnavigation(Nakanoetal.,
mance. Toaddressthesechallenges,wepropose 2021;Yaoetal.,2022b)andcodegeneration(Chenetal.,
LatentSpacePolicyOptimization(LSPO),anit- 2021;Yangetal.,2024)tovideogameenvironment(Wang
erativeframeworkthatcombinesgame-theoretic etal.,2023a)andreal-worldscenarios(Ahnetal.,2022;Bro-
methods with LLM fine-tuning to build strate- hanetal.,2023). Beyondsingle-agenttasks,LLM-based
giclanguageagents. LSPOleveragestheobser- agents have also shown potential in multi-agent interac-
vation that while the language space is combi- tions including collaborative teamwork (Li et al., 2023),
natoriallylarge,theunderlyingstrategyspaceis adversarial gameplay (Meta et al., 2022), and human-AI
relativelycompact. Wefirstmapfree-formutter- interation(Parketal.,2023;Liuetal.,2023).
ancesintoafinitelatentstrategyspace,yielding
Amongtheseinteractivedomains,strategiclanguagegames
anabstractedextensive-formgame. Thenweap-
suchasWerewolfpresentuniquechallengesbecausethey
plygame-theoreticmethodslikeCounterfactual
requirebothhigh-levelstrategicdecision-makingandfree-
RegretMinimization(CFR)tooptimizethepol-
form conversational abilities. Unlike classic games with
icyinthelatentspace. Finally,wefine-tunethe
predefinedandlimitedactions, suchasboardgames(Sil-
LLMviaDirectPreferenceOptimization(DPO)
veretal.,2016;2018),cardgames(Moravcˇíketal.,2017;
to align with the learned policy. By iteratively
Brown&Sandholm,2018),andvideogames(Mnih,2013;
alternatingbetweenthesesteps,ourLSPOagents
Vinyalsetal.,2019),Werewolfreliesheavilyonfree-form
progressively enhance both strategic reasoning
conversationtoachieveagreementsandperformstrategic
andlanguagecommunication. Experimentonthe
deceptions. Playersmustcommunicate,bluff,andinferhid-
Werewolfgameshowsthatouragentsiteratively
denrolesthroughunrestricted,naturallanguageinteractions.
expandthestrategyspacewithimprovingperfor-
Thisfree-formlanguagespaceexpandsthestrategicpossi-
manceandoutperformexistingWerewolfagents,
bilitiesandintroducesadditionalcomplexityunmatchedby
underscoringtheireffectivenessinfree-formlan-
morerigidlydefineddomains. Asaresult,Werewolfserves
guagegameswithstrategicinteractions.
asanidealenvironmentfordevelopingstrategicagentswith
*Equaladvising 1TsinghuaUniversity,Beijing,China2Beijing language-groundeddecision-makingcapabilities.
Zhongguancun Academy, Beijing, China 3Shanghai Qi Zhi In-
However,developingastrategiclanguageagentthatcanin-
stitute, Shanghai, China. Correspondence to: Zelai Xu <ze-
lai.eecs@gmail.com>,ChaoYu<yuchao@tsinghua.edu>,YiWu teractwithhumansinWerewolforotherfree-formlanguage
<jxwuyi@gmail.com>,YuWang<yu-wang@tsinghua.edu>. environments is still challenging. Classic game-theoretic
methods like Counterfactual Regret Minimization (CFR)
Proceedingsofthe42nd InternationalConferenceonMachine
andreinforcementlearning(RL)haveprovensuccessfulin
Learning,Vancouver,Canada.PMLR267,2025.Copyright2025
gameslikeGoandPoker,thankstotheirabilitytohandle
bytheauthor(s).
1

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
finiteactionspaces. YetWerewolfhasafree-formaction agentsandfindthattheLSPOagentachievesthehighest
space,makingdirectapplicationofthesemethodscomputa- win rate. We also conduct ablation studies to assess the
tionallyinfeasible. Mappingeverypossibleutterancetoan effectivenessofourdesignintheLSPOframework.
actionintheoriginaltextspacebecomesprohibitivelylarge,
leadingtoimmensedifficultyinstrategyrepresentationand
2.TheWerewolfGame
equilibrium-finding. Analternativeapproachistobuildlan-
guageagentswithLLMs. Thesemethodstypicallyrelyon Werewolfisapopularsocialdeductiongamewhereplay-
promptengineeringwithouttrainingthebaseLLM,which ers with hidden roles cooperate and compete with others
meanstheirsuccessdependsentirelyonthegeneralreason- innaturallanguages. TheWerewolfsideneedstoconceal
ingcapabilitiesofLLMstogenerateactions. Unfortunately, their identities and eliminate the other players, while the
prompt-based methods suffer from intrinsic bias in their Villagesideneedstoidentifytheirteammatesandvoteout
generated actions (Xu et al., 2023c), resulting in subopti- the Werewolves. Players are required to have both lan-
malperformanceinstrategiclanguagegameslikeWerewolf. guageproficiencyforcommunicationandstrategicability
Moreover,theseagentsexhibitlimitedexplorationofnovel fordecision-makingtoachievestrongperformanceinthe
strategiesbecausetheyfullyrelyontheLLMstogenerate Werewolf game. We consider a seven-player game with
actions, making the agents constrained by the capability twoWerewolvesbeingtheWerewolfsideandoneSeer,one
of the base LLMs. Some work (Chen et al., 2023a; Wu Doctor,andthreeVillagersbeingtheVillageside. Detailed
etal.,2024)mitigatestheseissuesbyfine-tuningtheLLM descriptionsofthegame’srule,observationspace,andre-
foraspecifictask,whichrequiresexpensivehumanlabor wardfunctioncanbefoundinAppendixA.
for high-quality data. Xu et al. (2023c) partially tackles
thebiasissuebyadditionallytrainingasmallnetworkto 2.1.GameEnvironment
calibratetheLLMoutputdistribution. However,itstillre-
Weconsideratext-basedseven-playerWerewolfgamethat
liesonafixedLLMtoproduceactioncandidates,leaving
proceedsthroughnaturallanguages. Weexcludeotherinfor-
theexplorationissueunaddressed. Thisraisesanimportant
mationlikethespeakingtone,facialexpression,andbody
question: Can we have a method that leverages both the
language(Laietal.,2022). Thispuretext-basedenviron-
specializedreasoningcapabilitiesfordecision-makingand
mentisacommonsetupintheliterature(Xuetal.,2023a;c;
thegeneralizationcapabilitiesofLLMs?
Wuetal.,2024;Bailisetal.,2024).
In this work, we propose an iterative Latent Space Pol-
Roles and Objectives. At the beginning of each game,
icyOptimization(LSPO)frameworktobuildstrategiclan-
thesevenplayersarerandomlypartitionedintotwosides.
guageagentsforfree-formlanguagegames,takingWere-
The Werewolf side has two Werewolf players who know
wolf as our testbed. Our approach combines structured
each other’s role and aim to eliminate the other players
game-theoreticmethodswithlanguagemodelsbyintroduc-
whileavoidingbeingdiscovered. TheVillagesidehasone
ingadiscretelatentstrategyspace. Ourmethodconsistsof
Seerwhocanchecktheroleofoneplayereachnight,one
three components. We first map the free-form utterances
Doctor who can protect one player each night, and three
into a manageable, discrete strategy space to yield an ab-
Villagerswithoutanyability. TheplayersintheVillageside
stractedgame. Thenweapplygame-theoreticmethodslike
onlyknowtheirownroleandneedtoshareinformationto
CFRtolearntheoptimalpolicyinthelatentspace. Finally,
identifytheWerewolvesandvotethemout.
wefine-tunetheLLMviaDirectPreferenceOptimization
(DPO)(Rafailovetal.,2024)toalignwiththelearnedpol- Game Progression. The game proceeds by alternating
icyandexpandthelatentspace. Byiteratingbetweenthese between night round and day round. In the night round,
latentspaceCFRstepsandLLMfine-tuning,ourmethod playerscanperformsecretactionsthatareonlyobservable
yields an evolving agent that addresses both the intrinsic bythemselves. Morespecifically,thetwoWerewolvescan
biasissuewithgame-theoreticmethodsandtheactionexplo- choose a target player to eliminate, the Seer can choose
rationissuewithlatentspaceexpansion,leadingtostrong a target player to investigate whether the player’s role is
performanceintheWerewolfgame. Werewolf, and the Doctor can choose a target player to
protecttheplayerfrombeingeliminated. TheDoctordoes
WeperformextensiveexperimentsintheWerewolfgameto
notknowthetargetplayerchosenbytheWerewolves. Ifthe
demonstratetheeffectivenessofourLSPOframework. We
DoctorchoosesthesametargetplayerastheWerewolves,
firstanalyzehowthelatentstrategyspaceevolvesbetween
thennoplayeriseliminatedinthisnightround,otherwise,
iterationstoshowthatouragentslearnincreasinglycomplex
theDoctorfailstoprotectanyplayer,andthetargetchosen
andstrategicbehaviors. Thenwequantitativelyevaluatethe
bytheWerewolvesiseliminated.
predictionaccuracyandwinrateofourLSPOagenttoshow
theimprovingperformancewithrespecttoiterations. Next, ObservationsandActions. Thelanguageobservationof
we compare our agents against state-of-the-art Werewolf eachagentisalistofnaturallanguagesthatlogthegame
2

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
Policy Optimization
Latent Space Construction Latent Space Expansion
in Latent Space
Language Action Original Game Abstracted Game Latent Space Policy
I’m the Seer and LLM
I saw Player 1 is
a Werewolf …
I’m saddened Preference Data
by the loss of
Player 4 … I’m the Seer and I’m saddened
I saw Player 1 is > by the loss of
Game Solver a Werewolf … Player 4 …
Clustering
(CFR, RL, etc.)
Fine-Tune
I think Player 1
is suspicious …
Latent Strategy Abstracted Game Latent Space Policy LLM
Figure1:OverviewoftheLatentSpacePolicyOptimization(LSPO)framework.Eachiterationconsistsofthreecomponents.
(1)Latentspaceconstruction: generatelanguageactionswiththeLLMandclusterthevastlanguageactionintoafinite
latentstrategyspace. (2)Policyoptimizationinlatentspace: reformulatetheoriginalgameasanabstractedgameandapply
game-theoreticmethodstolearnlatentspacepolicy. (3)Latentspaceexpansion: fine-tunetheLLMtoalignwiththelatent
spacepolicyandgeneratenewstrategiestoexpandthelatentstrategyspace.
history to the current step. This list include both private LLM-based agents tend to exhibit intrinsic bias in their
informationthatareonlyobservabletothecurrentplayer actiongeneration,whichisinheritedfromthemodel’spre-
andpublicinformationthataresharedbyallplayers. The training data. This issue is more pronounced in complex
privateinformationincludestheroleofthecurrentplayer, languagegameslikeWerewolf, wheretheopponentscan
thesecretactionsinthenightroundfortheWerewolf,Seer, exploit these predictable biases to counteract the agent’s
andDoctor,andtheteammatefortheWerewolf. Thepublic move. Therefore,mitigatingintrinsicbiasisessentialfor
informationincludestheIDofthecurrentplayer,theelim- languageagentstoreduceexploitationandachievestrong
inatedplayerineachnightanddayround,thediscussion, performanceinstrategiclanguagegames.
andthevotingresultineachdayround.
Exploration of Unbounded Action Space. Due to the
Playeractionsarealsointheformofnaturallanguageand immense combinatorial space induced by free-form text,
canbecategorizedintothreetypes:secretactions,whichare itisimpracticaltomapeverypossibleutterancetoanac-
secretactionsperformedduringthenight,suchaschoosing tion in the language space. On the other hand, manually
atargetplayertoeliminate,investigate,orprotect;discus- engineeringorpromptinganLLMtoproducealimitedset
sionactions,whicharestatementsmadeduringthedayto ofactionsmayfailtocapturethefullstrategiclandscape.
influenceotherplayers’perceptionsanddecisions;andvot- Evenifanagentoptimallymasterstheactiondistribution
ingactions,whicharechoicesmadeduringthevotinground withinalimitedsubset,itcouldbeeasilyexploitedbyout-fo-
tovoteforonplayerorchoosenottovote. distributionutterance.Consequently,inadequateexploration
oftheactionspacecouldresultinsuboptimalperformance
2.2.ChallengesforLanguageAgents infree-formlanguagegameslikeWerewolf.
Unlikeboard,card,orvideogameswithafinitesetofpre-
3.LatentSpacePolicyOptimization
definedactions,Werewolfhasafree-formlanguageaction
space. The vast space of natural language actions poses
Totackletheintrinsicbiasandtheexplorationissue,wepro-
twokeychallengesforlanguageagentstoachievestrong
poseaniterativeLatentSpacePolicyOptimization(LSPO)
performanceintheWerewolfgame.
framework. Our method combines game-theoretic opti-
IntrinsicBiasinActionGeneration. Asobservedinsim- mizationwithLLMfine-tuningandoperatesonanexpand-
plegameslikeRock-Paper-Scissor(Xuetal.,2023c),pure inglatentstrategyspacetoiterativelyimprovetheagent’s
3

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
decision-makingabilityandactionexploration. Asshown space as an abstracted game with a finite latent strategy
inFigure1, ourframeworkhasthreecomponentsinclud- space. Thisreformulationallowsustoapplystandardgame-
inglatentspaceconstruction,policyoptimizationinlatent solvingtechniquessuchasCounterfactualRegretMinimiza-
space, andlatentspaceexpansion. Moreimplementation tion(CFR)orreinforcementlearning(RL)methodstolearn
detailscanbefoundinAppendixC. near-optimalstrategiesthatovercometheintrinsicbias. In
ourimplementation,weemployCFRasthegamesolver.
3.1.LatentSpaceConstruction
AbstractedGameFormulation. Torepresentthegamein
Oneofthekeychallengesinfree-formlanguagegameslike acompact,finiteform,wereplacethefree-formdiscussion
Werewolfisachievingbroadexplorationoftheunbounded actionswiththediscretelatentstrategiesfromlatentspace
text space while maintaining a computationally tractable construction.Specifically,theabstractedgameisformalized
actionrepresentationforgame-theoreticmethods. Tostrike asanextensive-formgame(EFG),wherethesecretaction
abalancebetweenexplorationandtractability,wepropose andvotingactionremainthesame,andthediscussionaction
toabstractthevastlanguageactionspaceintoafinitesetof isreplacedbythelatentstrategy. Thestateintheabstracted
latentstrategies,whichwethenexpandoveriterationsfor gameisavectorincludinginformationliketheplayer’srole,
betterexploration. Specifically,ourlatentspaceconstruc- secretaction,etc.,andhistoryofpastlatentstrategies. The
tion in each iteration involves two steps including latent transitiondynamicsandpayofffunctionremainunchanged
strategygenerationandclustering. intheabstractedgame. Thisrepresentationretainsthekey
strategicelementsoftheoriginalgamewhilereducingthe
LatentStrategyGeneration. Inoursetting,secretactions
complexityoftheactionspace,makinglarge-scalegame-
andvotingactionsarealreadydiscreteandthereforedonot
solvingcomputationallytractable. Detaileddescriptionof
require further abstraction. We focus instead on the free-
theabstractedgamecanbefoundinAppendixA.
formdiscussionactions,whichweaimtocaptureaslatent
strategies. We assume that each role in the game has the PolicyOptimization. Oncethegameisrepresentedinthis
same set of latent strategies across all discussion rounds discrete form, we apply CFR to learn a policy and solve
andcollectthelatentstrategiesforeachrolebylettingthe theabstractedgame. ClassicalCFR(Zinkevichetal.,2007)
currentLLMagentself-playasdifferentrolesformultiple iterativelyimprovespoliciesbyminimizingcounterfactual
trajectories. To further improve the exploration of latent regretRforeachinformationset. Foreachiterationt,the
strategies,weprompttheLLMtogenerateN strategically regretforeachactionainthelatentspaceisupdatedby:
distinctdiscussioncandidatesandrandomlychooseoneto
R (a)=R (a)+u(σa,σ−a)−u(σ ), (1)
executeinthegame. Thisprocessencouragesdiversityin t t−1 t t t
thecollecteddiscussionactionsandgenerateasetoflatent whereu(σa,σ−a)istheutilityoftakingactionaunderthe
t t
strategiesinnaturallanguageforeachrole. currentstrategyprofileσ ,andu(σ )istheutilityunderthe
t t
fullstrategyprofile. Weuseneuralnetworkstoapproximate
LatentStrategyClustering. Althoughwegenerateaset
regretvaluetoscaleCFRtomorecomplexgamesandlearn
oflatentstrategiesforeachrole,theyarestillintheform
apolicyforeachdifferentroleintheWerewolfgame. By
ofnaturallanguage. Totransformthemintoadiscretela-
repeatedly simulating self-play among agents employing
tentstrategyspace,weembedeachdiscussionactioninto
DeepCFRintheabstractedgame,eachrole’spolicycon-
a vector representation using an embedding model such
vergestoanear-optimalstrategyprofile.Theresultinglatent
as“text-embedding-3-small”thatcapturesitssemanticand
spacepoliciesaddresstheintrinsicbiasinactiondistribution
contextualinformation. Wethenapplyasimplek-means
andachievestrongstrategicplayintheabstractedgame.
clusteringalgorithmtopartitiontheembeddedutterances
intokclusters,whereeachclusterrepresentsadistinctlatent
3.3.LatentSpaceExpansion
strategy. Clusteringreducestheinfinitefree-formtextspace
toafinitesetofabstractstrategies,pavingthewayforsub- To further improve the agent’s performance in free-form
sequentgame-theoreticoptimization. Byinterpretingeach languagegames,thelatentspacemustremainsufficiently
cluster as a latent action, we can more efficiently search expressivetocovernovelstrategiesandresistexploitationby
forandoptimizestrategicpolicieswithminimalsacrificeof out-of-distributionactions. Weachievethisbyfine-tuning
explorationoflanguagespace. theLLMtoalignwiththelearnedpolicyintheabstracted
gameandthenre-generatingandexpandingthelatentstrat-
3.2.PolicyOptimizationinLatentSpace egyspaceusingthefine-tunedLLM.Thisiterativeprocess
progressivelyincreasesexplorationoftheactionspace,en-
Another challenge in free-form language games is to ad-
ablingstrongerandmorerobustdecision-making.
dress the intrinsic bias in the agent’s action distribution.
Afterconstructingadiscretelatentstrategyspace,wecan Alignment to Latent Space Policy. We employ Direct
reformulate the original game with unbounded language PreferenceOptimization(DPO)(Rafailovetal.,2024)to
4

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
ReAct SLA LSPO Iter. 1 LSPO Iter. 2 LSPO Iter. 3
0.6 0.53
0.4 0.330.330.33 0.330.330.33 0.330.330.33
0.29
0.2 0.2 0.2 0.2 0.2
0.2 0.14
0.020.02 0 0 0 0 0 0
0.0
R. P. S. Sp. L. R. P. S. Sp. L. R. P. S. Sp. L. R. P. S. Sp. L. R. P. S. Sp. L.
exp. = 0.39 exp. = 0.33 exp. = 0.33 exp. = 0.33 exp. = 0.00
Figure2: Theactiondistributionsandexploitabilities(exp.) ofdifferentagentsintheRock-Paper-Scissors-Spock-Lizard
game. TheNashequilibriumistochooseeachactionwithanequalprobabilityof1/5andhasanexploitabilityof0.
fine-tunetheLLMsothatitsopen-endedlanguageoutputs agents, showing that our agents achieve the highest win
alignwiththenear-optimalstrategiesderivedfromtheab- rate on both the Werewolf side and the Village side. We
stractedgame. Toconstructthepreferencedatasetrequired furtherperformablationstudiestoassesstheeffectiveness
byDPO,weleveragegametrajectoriesgeneratedduringla- ofspecificdesignsinourframework. Moreimplementation
tentspaceconstruction. Werecordthelanguageobservation andexperimentdetailscanbefoundinAppendixB.
fortheLLMagentateachdiscussionphaseastheprompt,
andusetheN discussioncandidatesastheresponsecandi- 4.1.Proof-of-ConceptExample
dates. Eachofthediscussioncandidatescanbemappedto
We consider Rock-Paper-Scissors-Spock-Lizard, a five-
oneofthelatentstrategies,andthepreferencelabelisdeter-
choiceextensionoftheclassicRock-Paper-Scissorsgame.
minedbytheregretvalueofthelatentstrategies. Intuitively,
Althoughitisnotafree-formlanguagegame,itservesasa
adiscussionactionwithalowerregretvalueispreferred.
simpleproof-of-conceptgamethathighlightthemotivation
Withthispreferencedataset,weperformDPOtoalignthe
ofourmethod. Theintrinsicbiasinactiondistributionsis
LLMtowardthelearnedpolicyintheabstractedgamefor
inheritedfromtheimbalancedLLMpre-trainingdata,and
betterperformanceintheoriginalgame.
the exploration issue is introduced by the two additional
UpdateofLatentSpace. OncetheLLMisfine-tuned,it actionsofSpockandLizard. TheNashequilibrium(NE)of
canproduceabroaderdistributionofactionsthatreflectthe thisgameistochooseeachactionwithanequalprobability
refinedpolicy. Weexploitthisenhancedgenerativecapacity of 1/5. We compare LSPO agents of different iterations
toexpandthelatentspaceinthenextiteration. Specifically, withtwobaselines,includingReasonandAct(ReAct)(Yao
werepeatthelatentstrategygenerationandclusteringpro- et al., 2022b) and Strategic Language Agent (SLA) (Xu
cedureswiththefine-tunedLLMtore-generateandexpand etal.,2023c),andtheactiondistributionsandexploitabili-
thelatentstrategyspace. Thisupdatedlatentspaceoffers tiesofdifferentagentsareshowninFigure2.
increasedexplorationofpotentialstrategies,enablingsubse-
TheevaluationresultsshowthattheLSPOagentofitera-
quentpolicyoptimizationtodiscoverpreviouslyunexplored
tion 3 learns the NE of the game while other agents fail.
high-rewardactions.Throughiterativealignmentandexpan-
ReAct agent suffers from the intrinsic bias issue and has
sion,theagentcontinuallyrefinesitsdiscussionstrategies
higher probabilities to choose Rock, Paper, and Scissors,
andachievesstrongplayinthefree-formlanguagegame.
andmuchlowerprobabilitiestochooseSpockandLizard.
SLA,ontheotherhand,ishinderedbyinadequateaction
4.Experiments
exploration. SLAusesLLMstoproposeN actionsandRL
tolearntheoptimalpolicy. AtypicalvalueofN =3results
TodemonstratetheeffectivenessoftheLSPOframework,
inasubgamewithouttheother2action,andtheNEofthe
we first consider a proof-of-concept game to show how
subgame is not the NE of the original game. Our LSPO
LSPO overcomes intrinsic bias and addresses the explo-
agentaddressesthesetwochallengesbyiterativelyexpand-
rationissue. Thenweconductextensiveexperimentsinthe
ingtheactionspace. Asitcoversthefullactionspacewith
Werewolf game with Llama-3-8B-Instruct as our base
3iterations,theLSPOagentlearnstheNEofthegame.
model. Wevisualizehowthelatentstrategyspaceevolves
toshowthatouragentsprogressivelyacquiremorecomplex
strategicbehaviors. Wethenquantitativelyevaluatetheper- 4.2.LatentSpaceVisualization
formanceofourLSPOagentusingpredictionaccuracyand
TogaininsightintohowLSPOorganizesfree-formlanguage
winratetoshowtheimprovingperformanceoveriterations.
actionsintodiscretelatentstrategies,wefirstvisualizethe
WealsocomparetheLSPOagentwithfourstate-of-the-art
latentstrategyspaceconstructedatdifferenttrainingitera-
5

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
Werewolf’s Latent Space Seer’s Latent Space
Iter. 1 Iter. 2 Iter. 3 Iter. 1 Iter. 2 Iter. 3
Figure3: VisualizationofthelatentstrategicspaceofWerewolfandSeerindifferentLSPOiterations.
tions. Specifically,foreachroleintheWerewolfgame,we yetsubtlyguidingdiscussionstoprotectverifiedteammates.
gathertheutterancesgeneratedbytheLSPOagentin100 Notably,bythefinaliteration,themodeldevelopsavoting
games,embedthemwiththesentenceencoder,andapplydi- coordinationstrategyinwhichtheSeerexplicitlyasksall
mensionalityreductionforprojection. Thevisualizationof theVillagerstovoteforastronglysuspectedWerewolfto
latentspacesfortheWerewolfandtheSeerindifferentitera- maximizetheVillager’schanceofsuccess.Thisprogression
tionsisshowninFigure3. Earlieriterationsyieldrelatively impliesthattheSeeragentincreasinglylearnstobalance
indistinct clusters, reflecting a lack of strategic diversity. opennessandsecrecy,aligningitscommunicationstylewith
Oversuccessiveiterations,clearerandmorerefinedclusters theevolvinggamecontexttobettersupporttheVillageside.
emerge,indicatingthattheLSPOagentevolvestowardan
increasinglystructuredlatentspaceandlearntoexpressdif- 4.3.IterativePerformanceEvaluation
ferent strategic intentions such as accusing specific roles,
WethenevaluatehowtheperformanceofourLSPOagent
defendingteammates,andbluffing.
progresses with more iterations, demonstrating that our
Werewolf’sLatentSpace. Inthefirstiteration,thelatent framework produces increasingly stronger strategic lan-
spaceoftheWerewolfisdominatedbythreemainclusters. guage agents over time. We focus on two key metrics
Theblueclustercorrespondstoasimplestrategyofconceal- includingpredictionaccuracyandwinrate.
ingitsroleorpretendingtobeavillager,whilethesmaller
PredictionAccuracy. Accurateroleidentificationisacriti-
orangeclusterreflectsstrategieslikepretendingtobeaSeer
calaspectofWerewolf,asitunderpinseffectivedecision-
oraDoctor. Thereisevenagreenclustercorrespondingto
makingandvoting. Therefore,wemeasuretheagent’sabil-
unintentionallyrevealingthetrueroleofaWerewolf,which
itytopredicttherolesofotherplayerswithanadditional
isobviouslyaflawedstrategy. Astrainingproceeds,wesee
prediction phase before each voting phase in a Werewolf
moresophisticatedpatternsemerge. Theflawedstrategyof
game. Specifically,weusethefinal-iterationLSPOagent
disclosing one’s Werewolf role disappears, and the agent
as the fixed opponentand letLSPO agentsat differentit-
begins to incorporate deliberate bluffs and misdirections
erationsplayagainstthisopponentfor100games. Forthe
instead. Forexample,theredclusterfeaturestheagentpre-
Werewolfside,ahigherpredictionaccuracyofcrucialroles
tendingtobeaSeerandprovidingfabricatedinvestigative
likeSeerandDoctorallowsthemtoeliminatethesethreats
resultstosowconfusion,andthepurpleclustercenterson
earlier. Conversely,fortheVillageside,ahigherprediction
defendingtheteammateandredirectingsuspicionontoother
accuracyofWerewolvesimprovestheirchancetovoteout
players,leveragingmorenuancedlanguageandreasoningto
theWerewolfandwinthegame.
guidetheconversationtowardscapegoats.Thisrefinedparti-
tioningdemonstratesthattheWerewolfagentprogressively WinRate. Whilepredictionaccuracyservesasaninterme-
coversanincreasingnumberoflatentstrategies. diatemetrictoevaluatetheagents’reasoninganddecision-
makingability,wealsousethewinrateasadirectmeasure
Seer’sLatentSpace. Inthefirstiteration,theSeer’slatent
of the performance of our agents. Similar to the evalua-
spaceisrelativelycoarse,containingprimarilytwostrate-
tionofpredictionaccuracy,weusethefinal-iterationLSPO
giesincludingstayingsilentaboutitstrueroleorrevealing
agentasthefixedopponentandletouragentsatdifferent
itsroleandsharinginformation. Thisshowsalimitedrange
iterationsplay100gamesagainsttheopponent. Ahigher
ofstrategicdiversityintheearlystage. Astrainingproceeds
winrateindicatesastrongerperformanceinthegame.
through the second and third iterations, the Seer’s latent
spacebecomesmorediverse. Theemergentredclusterfea- AsshowninTable1,bothpredictionaccuracyandwinrate
turesdirectaccusationsoncetheSeeridentifiesaWerewolf, exhibitacleargrowingtrendastheiterationincreases,indi-
whilethegreenclustercorrespondstoconcealingtherole catingthatouriterativeLSPOframeworksteadilystrength-
6

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
PredictionAccuracy
WinRate
Werewolf Seer Doctor Villager Overall
Iter. 1 0.98±0.01 0.61±0.09 0.49±0.08 0.70±0.07 0.74±0.06 0.54±0.13
Werewolf
Iter. 2 0.99±0.01 0.68±0.07 0.59±0.06 0.77±0.09 0.79±0.06 0.63±0.09
Side
Iter. 3 0.99±0.00 0.73±0.08 0.67±0.07 0.81±0.11 0.83±0.07 0.73±0.11
Iter. 1 0.59±0.06 0.47±0.04 0.55±0.05 0.67±0.07 0.60±0.06 0.18±0.09
Village
Iter. 2 0.66±0.06 0.53±0.07 0.61±0.06 0.75±0.08 0.67±0.07 0.23±0.12
Side
Iter. 3 0.72±0.09 0.58±0.08 0.65±0.07 0.82±0.08 0.73±0.07 0.27±0.11
Table1: ThepredictionaccuracyandwinrateoftheLSPOagentsindifferentiterations.
WinRate ReAct ReCon Cicero-like SLA LSPOAgent(Ours)
AstheWerewolfSide 0.58±0.15 0.60±0.12 0.66±0.06 0.69±0.12 0.73±0.11
AstheVillageSide 0.16±0.06 0.16±0.08 0.21±0.04 0.25±0.08 0.27±0.11
Overall 0.38±0.11 0.38±0.10 0.44±0.05 0.47±0.10 0.50±0.11
Table2: ComparisonbetweenourLSPOagentwithstate-of-the-artagentsintheWerewolfgame.
enstheagents’reasoninganddecision-makingcapabilities. ReCon. ReConisanotherprompt-basedmethoddesigned
FromtheWerewolfside,theidentificationratefortheSeer for Avalon agents. The ReCon agent is prompted to first
startsoffrelativelyhighbuthasonlymodestimprovement. thinkfromitsownperspectiveandthenthinkfromitsop-
ThisisbecausetheSeeroftenrevealsitsrolestoshareinfor- ponents’perspectivetogeneratethefinalaction. Wemake
mation,makingiteasierfortheWerewolfsidetoidentify. slight modifications in the prompt to apply ReCon in the
Bycontrast,theWerewolf’spredictionaccuracyoftheDoc- Werewolfgame.
tor shows more significant gains, reflecting the strategic
Cicero-Like. TheCiceroagentiscreatedforthegameof
importanceofeliminatingtheDoctorwhocansavepoten-
Diplomacywithfiniteactionspaceandconsistsofastrategic
tialvictims. OntheVillageside,identifyingtheWerewolf
reasoningmoduleandadialoguemodule. Weimplement
andtheSeerbenefitsmostfromiterativelearning,sincecon-
aCicero-likeagentfortheWerewolfgamebypredefining
firmingthesecentralrolesiscrucialforcoordinatedvoting
anactionspaceof13primitiveactionslike“claimtobethe
andeliminationofWerewolves. Overall,theseresultscon-
Seer”, “do not reveal role”, etc. An RL policy is learned
firmthatourframeworkconsistentlyimprovesthestrategic
to select these actions in each state and generate action-
languageabilitiesoftheLSPOagent,enablingittoadapt
conditionedlanguagesinthegame.
andexcelincomplexsocialdeductionscenarioswitheach
additionaliteration. SLA.SLAcombinesreinforcementlearningandLLMto
overcomeintrinsicbiasandbuildstrategiclanguageagents
4.4.ComparisonwithState-of-the-ArtAgents fortheWerewolfgame. Weadoptthesameimplementation
asdescribedinthepaper(Xuetal.,2023c).
We compare the performance of the LSPO agent in the
Werewolfgamewithfourstate-of-the-artagentsincluding Wecompareourfinal-iterationLSPOagentwiththeafore-
Reason and Act (ReAct) (Yao et al., 2022b), Recursive mentionedfourbaselinesthroughtwohead-to-headevalu-
Contemplation(ReCon)(Wangetal.,2023b),aCicero-like ationsetups. Inthefirstsetup, ourLSPOagenttakesthe
agent (Meta et al., 2022), and Strategic Language Agent Werewolfsideandweleteachofthefiveagentsincluding
(SLA)(Xuetal.,2023c). Assomeofthesemethodswere ouragentandfourbaselineagentstaketheVillagesideto
notinitiallydevelopedforWerewolf,wemakeminormodifi- play100WerewolfgameswithourLSPOagent. Thissetup
cationstoensurecompatibilitywithourexperimentalsetting measurestheVillageside’swinrateagainsttheLSPOagent
whilepreservingeachapproach’scoredesign. as the Werewolves. In the second setup, we reverse the
rolesandlettheLSPOagenttaketheVillagesideandcom-
ReAct. ReActisaclassicprompt-basedmethodthatsyner-
parethewinrateoffiveagentsastheWerewolvesaveraged
gizesreasoningandactingforagenttasks. Weimplement
over100games. AsshownintheboldnumbersinTable2,
ReActfortheWerewolfgamebyprovidingtheLLMwith
ourLSPOagentachievethehighestwinratesbothasthe
rawgameobservationstogeneratebothintermediaterea-
WerewolvesandastheVillagers.
soningandfinalactionswithinasingleprompt.
7

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
WinRate VillageSide WerewolfSide WinRate Iter. 1 Iter. 2 Iter. 3
LSPOIter. 1 0.18±0.09 0.54±0.13 k =1 0.13±0.06 0.20±0.10 0.24±0.11
w/oFine-Tuning 0.15±0.09 0.47±0.14 k =2 0.22±0.11 0.24±0.12 0.25±0.08
w/oPolicyLearning 0.12±0.07 0.38±0.16 k =3 0.23±0.09 0.25±0.06 0.25±0.07
Table3: AblationonkeycomponentsofLSPOagents. Table4: Ablationonclustersize.
WinRate Iter. 1 Iter. 2 Iter. 3
The strong performance of our LSPO agent is largely at-
k =1 0.22±0.10 0.24±0.08 0.25±0.08
tributabletoitsiterativeinterplaybetweenlatentspacestrat-
k =2 0.22±0.11 0.24±0.12 0.25±0.08
egylearningandpreference-basedfine-tuning,whichrefines
k =3 0.23±0.07 0.25±0.09 0.25±0.06
bothlanguageanddecision-makingovertime. Bycontrast,
ReActandReConrelyonprompt-basedapproacheswithout
game-theoreticupdates,leavingthemsusceptibletointrinsic Table5: AblationonDPOhyperparameters.
biasesfrompretrainingdataandlimitingtheirperformance
incomplexdecision-makingtasks. TheCicero-likeagent
sensitivity analysis on the number of initial clusters. We
isconstrainedbyapredefinedactionset,makingitdifficult
considerasimplerfour-playerWerewolfgame(oneWere-
to evolve more subtle and diverse strategies as the game
wolf,oneSeer,andtwoVillagers)andrunLSPOwithdif-
progresses. SLApartiallyaddressestheintrinsicbiasissues
ferentnumbersofinitialclustersk = 1,2,3andevaluate
bygeneratingmultiplecandidateactionsandusingRLto
theWerewolf’swinrate. TheresultsinTable4showthat
selectfromthem. However,itstillreliesonaprompt-based
larger numbers of initial clusters generally lead to better
methodthatcansufferfromlimitedexplorationofpoten-
performanceintheearlyiterations,butdonotinfluencethe
tialstrategies. Incomparison,ourLSPOmethodintegrates
finalperformanceafterthreeiterations.
CFR’spolicyimprovementandlatent-spaceclusterrefine-
ment with preference-based LLM alignment, enabling it Fine-TuningHyperparameters. Wealsoperformasen-
toexplore,exploit,andcontinuouslyexpandtherangeof sitivity analysis to evaluate our method’s robustness to
viablestrategicmovesinsocialdeductiongames. fine-tuning hyperparameters. We also consider the sim-
plerfour-playergameandperformablationsonDPOβ =
4.5.AblationStudies 0.05,0.1,0.2. TheresultsinTable5showthatourmethod
achievescomparableresultswithdifferentchoicesofβ and
KeyComponents. Toshowtheeffectivenessofthethree
isrobusttofine-tuninghyperparameters.
key components in LSPO agents, we compare the LSPO
agentiniteration1withtwoablationagents. Thefirstab-
5.RelatedWork
lation agent, denoted as “w/o Fine-Tuning”, removes the
thirdcomponentandonlyperformslatentspaceconstruc-
LargeLanguageModel-BasedAgents.
tionandpolicyoptimizationinthelatentspace. Togenerate
discussionactioningameplay,thisagentfirstusesthelatent Recent advancements in large language models (LLMs)
spacepolicytosamplealatentstrategy,thenthepreviously haveledtothedevelopmentofagentscapableofperforming
collected discussions corresponding to the latent strategy complextasksacrossvariousdomains,suchaswebinter-
areusedasfew-shotexamplestoprompttheLLMforthe actions(Nakanoetal.,2021;Yaoetal.,2022a;Dengetal.,
discussionaction. Thesecondablationagent, denotedas 2023),codegeneration(Chenetal.,2021;Yangetal.,2024),
“w/oPolicyLearning”,removesthesecondcomponentof gaming environments (Huang et al., 2022a; Wang et al.,
policy optimization in the latent space. Instead, it uses 2023c;a;Maetal.,2023),real-worldrobotics(Ahnetal.,
gpt-3.5togeneratethepreferencedataandusesDPOto 2022;Huangetal.,2022b;Vempralaetal.,2023),andmulti-
trainfor1iterationAsshowninTable3,theLSPOagent agentsystems(Parketal.,2023;Lietal.,2023;Chenetal.,
initeration1achievesthebestresultonboththeVillager 2023b). Acommonapproachintheseworksistoexploit
andtheWerewolfside. Theseresultsdemonstratethatthe thereasoningcapabilitiesandin-contextlearningofLLMs
policyoptimizationcomponenthelpsagentslearnstronger toimprovedecision-makingprocesses. Chain-of-Thought
strategies,whilethefine-tuningcomponenthelpsLLMsbet- (CoT)prompting(Weietal.,2022)hasbeeninstrumentalin
tergeneralizetonewlanguageactionsbeyondthecollected enablingLLMstoperformstep-by-stepreasoning. Building
samplesandexpandthelatentstrategicspace. uponthis,ReAct(Yaoetal.,2022b)synergizesreasoning
and action to enhance performance across various tasks.
NumberofInitialClusters.
Subsequentresearchhasincorporatedself-reflection(Shinn
To examine the robustness of our method, we perform a etal.,2023)andstrategicreasoning(Gandhietal.,2023)to
8

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
furtherrefineagentbehaviors. However,thesemethodscan byintroducingafinitelatentstrategyspacetoenableitto
stillsufferfromtheintrinsicbiasesandexplorationissue solvefree-formlanguagegames.
ofLLM-basedagents,leadingtosuboptimalperformance
Reinforcementlearning(RL)methods,ontheotherhand,
incomplexgames. Arepresentativemethodthataddresses
havereachedremarkableachievementsincomplexdomains
theseissuesinthegameofDiplomacyisCicero(Metaetal.,
likeGo(Silveretal.,2016;2018)andvideogames(Vinyals
2022), which first uses a strategic module to produce ac-
etal.,2019;Berneretal.,2019),oftensurpassingexperthu-
tion intent and then generates action-conditioned natural
manperformance.Aseminaltechniqueinthesesuccessesis
languageswithadialoguemodule. However, Diplomacy
self-playanditsvariants(Heinrichetal.,2015;Heinrich&
isaboardgamewithfiniteactionspaceanddoesnothave
Silver,2016;Hennesetal.,2020;Xuetal.,2023b),where
theexplorationissue,makingitnotsuitableforfree-form
agentsrepeatedlytrainagainstolderversionsofthemselves
languagegameswithunboundedtextactionspace.
to refine their policies. Another prominent line of work
Duetothehighdemandforbothadvancedcommunication isPolicy-SpaceResponseOracles(PSRO)(Lanctotetal.,
skillsandstrategicreasoning,socialdeductiongameslike 2017;Mulleretal.,2019),aniterativeprocedurethatpro-
Werewolf and Avalon have been proposed as testbeds to duces best responses to a growing population of policies
buildlanguageagentswithstrategicability. Earlierattempts inameta-game. Conceptually,ouriterativeframeworkis
to create agents for these games often rely on predefined relatedtoPSROinthatwebothsolveanabstractedgame
protocolsorlimitedcommunicationcapabilities(Wang& beforeenlargingittoapproachthefulloriginalgame. The
Kaneko,2018),restrictingtheireffectiveness. Recentworks difference is that PSRO treats newly learned policies as
haveexploredusingLLMstoenablenaturallanguageinter- meta-actionstoformanormal-formmeta-game,whereas
actionsinthesegames. Forinstance,Xuetal.(2023a)de- ourapproachclustersfree-formlanguageactionsintoadis-
velopedaprompt-basedWerewolfagentthatusesheuristic cretelatentactionspacetoreformulatetheoriginalgameas
informationretrievalandexperiencereflection. Similarly, anextensive-formgamewithfiniteactionspace.
ReCon (Wang et al., 2023b) introduced a prompt-based
methodforplayingAvalonbyconsideringboththeagent’s
6.Conclusion
perspectiveandthatofopponents. However, theseLLM-
basedagentsmaystillberestrictedbyintrinsicbiasandlim- Inthiswork,wepresentedLatentSpacePolicyOptimiza-
itedexplorationoftheactionspace,affectingtheirdecision- tion (LSPO), an iterative framework that combines struc-
makingquality. StrategicLanguageAgent(SLA)(Xuetal., turedgame-theoreticmethodswiththeexpressivepowerof
2023c)partiallysolvestheseissuesbygeneratingdiverse largelanguagemodelstobuildstrategiclanguageagentsin
action candidates and learning an RL policy to mitigate free-formstrategiclanguagegames. Byabstractinguncon-
intrinsicbias. However,thismethodstillreliesonafixed strainedlanguage actionspaceintoa discretelatentstrat-
LLM to produce the action candidates, which can fail to egyspace,ourapproachenablesefficientCFRinthelatent
addresstheexplorationissue. Ourapproachmitigatesthe space to overcome intrinsic bias and learn strong strate-
intrinsicbiasbyapplyinggame-theoreticmethodstoopti- gies. Wethenperformiterativefine-tuningviaDPOtoalign
mizepolicyinadiscretelatentstrategyspaceandtacklesthe theLLM’slanguagegenerationwiththeevolvingstrategy
explorationissuebyiterativelyexpandingthelatentspace andexpandthelatentstrategyspacetoaddresstheexplo-
byaligningtheLLMtothelatentspacepolicy,leadingto rationissue. OurextensiveevaluationintheWerewolfgame
strongperformanceintheWerewolfgame. demonstratesthatLSPOnotonlyaddressesintrinsicbiases
andexplorationissuesinherentinprompt-basedagents,but
Game-TheoreticAlgorithms. CounterfactualRegretMin-
alsoachievesincreasingperformancewithrespecttoitera-
imization(CFR)(Zinkevichetal.,2007)isafoundational
tionsandoutperformsfourstate-of-the-artbaselineagents.
algorithm for solving imperfect-information games, par-
Lookingahead,weenvisionLSPO’ssynergyoflatent-space
ticularlythoseinvolvinghiddeninformationandstrategic
abstractionandpreference-basedlanguagealignmentcan
deceptionlikepoker(Moravcˇíketal.,2017;Brown&Sand-
beextendedtoavarietyofothercomplexdecision-making
holm,2018;2019). ThecoreprincipleofCFRistoitera-
taskswithfree-formlanguageactions.
tivelyreduceregretacrossplayers’decisionpointsinthe
gametree,convergingtowardstrategiesthatapproximatea
Nashequilibrium. SubsequentrefinementsofCFR(Lanc- Acknowledgements
totetal.,2009;Tammelin,2014;Brownetal.,2019)have
This work was supported by National Natural Science
expandeditsscalabilityandadaptabilitytoabroaderrange
FoundationofChina(No.62406159,62325405),Postdoc-
ofscenarios. OfparticularnoteisDeepRole(Serrinoetal.,
toral Fellowship Program of CPSF under Grant Number
2019),whichintegratesdeductivereasoningwithCFRto
(GZC20240830, 2024M761676), ChinaPostdoctoralSci-
playthesocialdeductiongameAvalonwithoutcommuni-
enceSpecialFoundation2024T170496.
cation. OurmethodcombinesCFRwithlanguagemodels
9

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
ImpactStatement Chen,B.,Shu,C.,Shareghi,E.,Collier,N.,Narasimhan,K.,
andYao,S. Fireact: Towardlanguageagentfine-tuning.
OurresearchadvancesthecapabilitiesofLLM-basedagents
arXivpreprintarXiv:2310.05915,2023a.
inapurelytext-basedWerewolfenvironment. Whilethis
settingallowstheagentstodeveloprobustdecision-making Chen,M.,Tworek,J.,Jun,H.,Yuan,Q.,Pinto,H.P.D.O.,
anddeception-detectionskills,italsounderscoresthepoten- Kaplan,J.,Edwards,H.,Burda,Y.,Joseph,N.,Brockman,
tialformisuseifsimilartechniquesweretobeadaptedto G., etal. Evaluatinglargelanguagemodelstrainedon
real-worldscenariosinvolvingmanipulationormisinforma- code. arXivpreprintarXiv:2107.03374,2021.
tion. Tomitigatetheserisks,ourimplementationremains
strictlyfocusedontext-basedsimulationanddoesnotdi- Chen,W.,Su,Y.,Zuo,J.,Yang,C.,Yuan,C.,Qian,C.,Chan,
rectly transfer to broader applications without additional C.-M.,Qin,Y.,Lu,Y.,Xie,R.,etal. Agentverse: Facili-
safeguards. At the same time, our experiment results in- tatingmulti-agentcollaborationandexploringemergent
dicate that our agent could be used to identify potential behaviors in agents. arXiv preprint arXiv:2308.10848,
deceptiveandmanipulativecontent. Weenvisionthatany 2023b.
futureextensionsofthisworkwillrequirecarefulconsid-
Deng,X.,Gu,Y.,Zheng,B.,Chen,S.,Stevens,S.,Wang,
eration of ethical guidelines and responsible deployment
B.,Sun,H.,andSu,Y. Mind2web: Towardsageneralist
strategiestoensurethatsuchlanguageagentsystemsserve
agent for the web. arXiv preprint arXiv:2306.06070,
societyconstructively.
2023.
References Gandhi, K., Sadigh, D., and Goodman, N. D. Strate-
gic reasoning with language models. arXiv preprint
Ahn,M.,Brohan,A.,Brown,N.,Chebotar,Y.,Cortes,O.,
arXiv:2305.19165,2023.
David,B.,Finn,C.,Fu,C.,Gopalakrishnan,K.,Hausman,
K.,etal. Doasican,notasisay: Groundinglanguage Heinrich, J. and Silver, D. Deep reinforcement learning
inroboticaffordances. arXivpreprintarXiv:2204.01691, from self-play in imperfect-information games. arXiv
2022. preprintarXiv:1603.01121,2016.
Bailis, S., Friedhoff, J., andChen, F. Werewolfarena: A
Heinrich,J.,Lanctot,M.,andSilver,D. Fictitiousself-play
casestudyinllmevaluationviasocialdeduction. arXiv
inextensive-formgames. InInternationalconferenceon
preprintarXiv:2407.13943,2024.
machinelearning,pp.805–813.PMLR,2015.
Berner,C.,Brockman,G.,Chan,B.,Cheung,V.,Debiak,P.,
Hennes,D.,Morrill,D.,Omidshafiei,S.,Munos,R.,Pero-
Dennison,C.,Farhi,D.,Fischer,Q.,Hashme,S.,Hesse,
lat,J.,Lanctot,M.,Gruslys,A.,Lespiau,J.-B.,Parmas,
C., et al. Dota 2 with large scale deep reinforcement
P.,Duéñez-Guzmán,E.,etal. Neuralreplicatordynam-
learning. arXivpreprintarXiv:1912.06680,2019.
ics: Multiagentlearningviahedgingpolicygradients. In
Brohan, A., Brown, N., Carbajal, J., Chebotar, Y., Chen, Proceedingsofthe19thinternationalconferenceonau-
X., Choromanski, K., Ding, T., Driess, D., Dubey, A., tonomousagentsandmultiagentsystems,pp.492–501,
Finn, C., et al. Rt-2: Vision-language-action models 2020.
transferwebknowledgetoroboticcontrol. arXivpreprint
arXiv:2307.15818,2023. Huang,W.,Abbeel,P.,Pathak,D.,andMordatch,I. Lan-
guage models as zero-shot planners: Extracting ac-
Brown,N.andSandholm,T. Superhumanaiforheads-up tionable knowledge for embodied agents. In Interna-
no-limitpoker: Libratusbeatstopprofessionals. Science, tionalConferenceonMachineLearning,pp.9118–9147.
359(6374):418–424,2018. PMLR,2022a.
Brown,N.andSandholm,T. Superhumanaiformultiplayer
Huang,W.,Xia,F.,Xiao,T.,Chan,H.,Liang,J.,Florence,
poker. Science,365(6456):885–890,2019.
P.,Zeng,A.,Tompson,J.,Mordatch,I.,Chebotar,Y.,etal.
Brown, N., Lerer, A., Gross, S., and Sandholm, T. Deep Innermonologue: Embodiedreasoningthroughplanning
counterfactualregretminimization. InInternationalcon- withlanguagemodels. arXivpreprintarXiv:2207.05608,
ferenceonmachinelearning,pp.793–802.PMLR,2019. 2022b.
Brown,T.,Mann,B.,Ryder,N.,Subbiah,M.,Kaplan,J.D., Lai,B.,Zhang,H.,Liu,M.,Pariani,A.,Ryan,F.,Jia,W.,
Dhariwal, P., Neelakantan, A., Shyam, P., Sastry, G., Hayati, S. A., Rehg, J. M., and Yang, D. Werewolf
Askell,A.,etal. Languagemodelsarefew-shotlearners. among us: A multimodal dataset for modeling persua-
Advancesinneuralinformationprocessingsystems,33: sionbehaviorsinsocialdeductiongames. arXivpreprint
1877–1901,2020. arXiv:2212.08279,2022.
10

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
Lanctot,M.,Waugh,K.,Zinkevich,M.,andBowling,M. Park, J. S., O’Brien, J. C., Cai, C. J., Morris, M. R.,
Montecarlosamplingforregretminimizationinexten- Liang, P., and Bernstein, M. S. Generative agents: In-
sivegames. Advancesinneuralinformationprocessing teractive simulacra of human behavior. arXiv preprint
systems,22,2009. arXiv:2304.03442,2023.
Lanctot, M., Zambaldi, V., Gruslys, A., Lazaridou, A., Rafailov,R.,Sharma,A.,Mitchell,E.,Manning,C.D.,Er-
Tuyls,K.,Pérolat,J.,Silver,D.,andGraepel,T. Auni- mon, S., and Finn, C. Direct preference optimization:
fiedgame-theoreticapproachtomultiagentreinforcement Your language model is secretly a reward model. Ad-
learning. Advances in neural information processing vances in Neural Information Processing Systems, 36,
systems,30,2017. 2024.
Russell,S.J.andNorvig,P.Artificialintelligence:amodern
Li,G.,Hammoud,H.A.A.K.,Itani,H.,Khizbullin,D.,and
approach. Pearson,2016.
Ghanem,B. Camel: Communicativeagentsfor"mind"
explorationoflargescalelanguagemodelsociety. arXiv
Serrino,J.,Kleiman-Weiner,M.,Parkes,D.C.,andTenen-
preprintarXiv:2303.17760,2023.
baum, J. Finding friend and foe in multi-agent games.
AdvancesinNeuralInformationProcessingSystems,32,
Liu,J.,Yu,C.,Gao,J.,Xie,Y.,Liao,Q.,Wu,Y.,andWang,
2019.
Y. Llm-poweredhierarchicallanguageagentforreal-time
human-aicoordination.arXivpreprintarXiv:2312.15224, Shinn,N.,Labash,B.,andGopinath,A. Reflexion: anau-
2023. tonomousagentwithdynamicmemoryandself-reflection.
arXivpreprintarXiv:2303.11366,2023.
Ma,W.,Mi,Q.,Yan,X.,Wu,Y.,Lin,R.,Zhang,H.,and
Wang,J. Largelanguagemodelsplaystarcraftii: Bench- Silver,D.,Huang,A.,Maddison,C.J.,Guez,A.,Sifre,L.,
marks and a chain of summarization approach. arXiv VanDenDriessche,G.,Schrittwieser,J.,Antonoglou,I.,
preprintarXiv:2312.11865,2023. Panneershelvam, V., Lanctot, M., et al. Mastering the
gameofgo with deepneuralnetworksandtreesearch.
Meta,Bakhtin,A.,Brown,N.,Dinan,E.,Farina,G.,Fla- nature,529(7587):484–489,2016.
herty, C., Fried, D., Goff, A., Gray, J., Hu, H., et al.
Human-levelplayinthegameofdiplomacybycombin- Silver,D.,Hubert,T.,Schrittwieser,J.,Antonoglou,I.,Lai,
inglanguagemodelswithstrategicreasoning. Science, M.,Guez,A.,Lanctot,M.,Sifre,L.,Kumaran,D.,Grae-
378(6624):1067–1074,2022. pel,T.,etal. Ageneralreinforcementlearningalgorithm
thatmasterschess,shogi,andgothroughself-play. Sci-
Mnih, V. Playingatari with deepreinforcement learning. ence,362(6419):1140–1144,2018.
arXivpreprintarXiv:1312.5602,2013.
Tammelin,O. Solvinglargeimperfectinformationgames
Moravcˇík,M.,Schmid,M.,Burch,N.,Lisy`,V.,Morrill,D., usingcfr+. arXivpreprintarXiv:1407.5042,2014.
Bard,N.,Davis,T.,Waugh,K.,Johanson,M.,andBowl-
Vemprala,S.,Bonatti,R.,Bucker,A.,andKapoor,A. Chat-
ing,M. Deepstack: Expert-levelartificialintelligencein
gptforrobotics: Designprinciplesandmodelabilities.
heads-upno-limitpoker. Science, 356(6337):508–513,
MicrosoftAuton.Syst.Robot.Res,2:20,2023.
2017.
Vinyals,O.,Babuschkin,I.,Czarnecki,W.M.,Mathieu,M.,
Muller,P.,Omidshafiei,S.,Rowland,M.,Tuyls,K.,Perolat,
Dudzik,A.,Chung,J.,Choi,D.H.,Powell,R.,Ewalds,
J.,Liu,S.,Hennes,D.,Marris,L.,Lanctot,M.,Hughes,
T., Georgiev, P., etal. Grandmasterlevelinstarcraftii
E.,etal. Ageneralizedtrainingapproachformultiagent
usingmulti-agentreinforcementlearning. Nature, 575
learning. arXivpreprintarXiv:1909.12823,2019.
(7782):350–354,2019.
Nakano,R.,Hilton,J.,Balaji,S.,Wu,J.,Ouyang,L.,Kim, Wang,G.,Xie,Y.,Jiang,Y.,Mandlekar,A.,Xiao,C.,Zhu,
C.,Hesse,C.,Jain,S.,Kosaraju,V.,Saunders,W.,etal. Y., Fan, L., and Anandkumar, A. Voyager: An open-
Webgpt: Browser-assistedquestion-answeringwithhu- endedembodiedagentwithlargelanguagemodels. arXiv
manfeedback. arXivpreprintarXiv:2112.09332,2021. preprintarXiv:2305.16291,2023a.
Ouyang,L.,Wu,J.,Jiang,X.,Almeida,D.,Wainwright,C., Wang, S., Liu, C., Zheng, Z., Qi, S., Chen, S., Yang, Q.,
Mishkin,P.,Zhang,C.,Agarwal,S.,Slama,K.,Ray,A., Zhao,A.,Wang,C.,Song,S.,andHuang,G. Avalon’s
et al. Training language models to follow instructions gameofthoughts: Battleagainstdeceptionthroughre-
withhumanfeedback. AdvancesinNeuralInformation cursivecontemplation. arXivpreprintarXiv:2310.01320,
ProcessingSystems,35:27730–27744,2022. 2023b.
11

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
Wang,T.andKaneko,T. Applicationofdeepreinforcement
learninginwerewolfgameagents.In2018Conferenceon
TechnologiesandApplicationsofArtificialIntelligence
(TAAI),pp.28–33.IEEE,2018.
Wang,Z.,Cai,S.,Liu,A.,Ma,X.,andLiang,Y. Describe,
explain,planandselect: Interactiveplanningwithlarge
languagemodelsenablesopen-worldmulti-taskagents.
arXivpreprintarXiv:2302.01560,2023c.
Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F.,
Chi, E., Le, Q. V., Zhou, D., et al. Chain-of-thought
prompting elicits reasoning in large language models.
AdvancesinNeuralInformationProcessingSystems,35:
24824–24837,2022.
Wooldridge, M. and Jennings, N. R. Intelligent agents:
Theoryandpractice. Theknowledgeengineeringreview,
10(2):115–152,1995.
Wu,S.,Zhu,L.,Yang,T.,Xu,S.,Fu,Q.,Wei,Y.,andFu,
H. Enhancereasoningforlargelanguagemodelsinthe
gamewerewolf. arXivpreprintarXiv:2402.02330,2024.
Xu,Y.,Wang,S.,Li,P.,Luo,F.,Wang,X.,Liu,W.,andLiu,
Y. Exploringlargelanguagemodelsforcommunication
games: Anempiricalstudyonwerewolf. arXivpreprint
arXiv:2309.04658,2023a.
Xu,Z.,Liang,Y.,Yu,C.,Wang,Y.,andWu,Y. Fictitious
cross-play: Learningglobalnashequilibriuminmixed
cooperative-competitive games. In Proceedings of the
2023 International Conference on Autonomous Agents
andMultiagentSystems,pp.1053–1061,2023b.
Xu,Z.,Yu,C.,Fang,F.,Wang,Y.,andWu,Y. Language
agentswithreinforcementlearningforstrategicplayin
the werewolf game. arXiv preprint arXiv:2310.18940,
2023c.
Yang, J., Jimenez, C. E., Wettig, A., Lieret, K., Yao,
S., Narasimhan, K., and Press, O. Swe-agent: Agent-
computerinterfacesenableautomatedsoftwareengineer-
ing. arXivpreprintarXiv:2405.15793,2024.
Yao, S., Chen, H., Yang, J., and Narasimhan, K. Web-
shop: Towardsscalablereal-worldwebinteractionwith
groundedlanguageagents. AdvancesinNeuralInforma-
tionProcessingSystems,35:20744–20757,2022a.
Yao,S.,Zhao,J.,Yu,D.,Du,N.,Shafran,I.,Narasimhan,
K.,andCao,Y. React: Synergizingreasoningandacting
inlanguagemodels. arXivpreprintarXiv:2210.03629,
2022b.
Zinkevich,M.,Johanson,M.,Bowling,M.,andPiccione,C.
Regretminimizationingameswithincompleteinforma-
tion. Advancesinneuralinformationprocessingsystems,
20,2007.
12

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
A.WerewolfGameImplementationDetails
A.1.GameRules
Setup. Eachgamebeginsbyrandomlyassigningsevenroles—twoWerewolves,oneSeer,oneDoctor,andthreeVil-
lagers—tosevendifferentplayerslabeled“player_0,”“player_1,”...,“player_6.”ThetwoWerewolvesareawareofeach
other’sidentities,whiletheSeer,Doctor,andVillagersonlyknowtheirownroles.
Night Round. During the Night round, only the surviving Werewolves, Seer, and Doctor take secret actions that are
disclosedonlytotherelevantparties.
• Werewolf: ThelivingWerewolvescollectivelydecideonatargettokill,buttheyfollowaspecificorderwhenthere
aretwoofthem. First,theWerewolfwiththesmallerIDproposesatarget;theotherWerewolfthenmakesthefinal
decision. Forinstance,if“player_0”and“player_2”areWerewolves,“player_0”proposes“player_i,”and“player_2”
choosestheultimatekilltarget“player_j.”IfonlyoneWerewolfisalive,thatWerewolf’sdecisionstands. Werewolves
cannotkilladeadplayer,themselves,ortheirteammate.
• Seer: TheSeerselectsalivingplayertoinvestigate,revealingwhetherthatplayerisaWerewolf. TheSeermaynot
investigateadeadplayerorthemselves,althoughtheyareallowedtoinvestigatethesameplayerondifferentnights
(albeitalesseffectivestrategy).
• Doctor: TheDoctorselectsaplayertoprotect,withoutknowledgeoftheWerewolves’choice. TheDoctorcannotsave
someonewhoisalreadydeadbutcanchoosetosavethemselves.
DayRound. Thedayroundproceedswiththreephaseincludingannouncement,discussion,andvoting.
• Announcement: atthestartoftheDayround,theeventsofthepreviousnightaremadepublictoallplayersstillin
thegame. AnyonekilledduringtheNightroundisimmediatelyremovedandcannotrevealtheirroleorparticipatein
discussions. Twoscenariosdeterminetheannouncement: iftheWerewolvestargeted“player_i”andtheDoctoreither
savedadifferent“player_j”orwasnolongeralive,“player_i”iskilled,andtheannouncementstates: “player_iwas
killedlastnight.”IftheDoctorsavedexactlythesamepersontheWerewolvesintendedtokill(“player_i”),thennoone
iskilled,andtheannouncementis: “noplayerwaskilledlastnight.”
• Discussion: allsurvivingplayersjoinanopendiscussioninasetspeakingorder,eachspeakingexactlyonce. If,for
example,theremainingplayersare“player_0,”“player_2,”and“player_5,”then“player_0”speaksfirst,followedby
“player_2,”andconcludingwith“player_5.”
• Voting: afterthediscussion,allsurvivingplayerssimultaneouslyvotetoeliminateoneotherplayerorchoosetoabstain.
They are not allowed to vote for a dead player or for themselves. The individual who receives the most votes is
eliminatedwithoutroledisclosure. Intheeventofatie,oneofthetiedplayersisrandomlychosentobeeliminated.
Everyoneknowsthefinalvotingtally.
Winning. TheWerewolveswinif,atanypoint,thenumberoflivingWerewolvesisequaltothatofallotherremaining
players. Theydonotneedtoeliminateeverynon-Werewolftoclaimvictory. Conversely,theVillagers(includingtheSeer
andDoctor)winoncebothWerewolveshavebeeneliminated.
A.2.ObservationSpace
LanguageObservation. Eachagent’slanguageobservationisrepresentedasalistofnaturallanguagestatementsthat
logthegame’shistoryuptothecurrentstep. Thislistcomprisesbothprivateinformation,whichisaccessibleonlytothe
currentplayer,andpublicinformation,whichissharedamongallplayers. Theprivateinformationincludestheplayer’srole,
secretactionstakenduringthenightphasebytheWerewolf,Seer,andDoctor,aswellastheWerewolf’steammate. Onthe
otherhand,thepublicinformationconsistsoftheplayer’sID,theeliminatedplayerineachnightanddayphase,discussions,
andvotingoutcomesfromeachdayphase. Anexampleofthelanguageobservationisasfollow.
13

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
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
• day 1 voting result: player_3 had the most votes and was eliminated.
– voted for player_3: player_1, player_6.
– voted for player_1: player_3.
– choose not to vote: player_0, player_2, player_5.
Now it is night 2 round and you should choose one player to save. As player_5 and the Doctor, you
should choose from the following actions: save player_0, save player_1, save player_2, save player_5,
save player_6.
VectorObservation. Wealsoconsideravectorizedobservation. Theobservationvectorincludesinformationlikethe
player’sID,role,deductions,etc. byone-hotencoding. ThedetailsoftheobservationvectorarelistedinTable6
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
(allzeroifdonotact).
onehotencodingofthedeadplayer,
Foreachround announcement 7
(allzeroifnoplayerisdead).
(3rounds)
onehotencodingoftheeachplayer’schoice,
votingresult 49
(allzeroiftheplayerdoesnotvoteorisdead).
Table6: Vectorobservationspace.
14

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
A.3.RewardFunctions
Therewardfunctionsaredefinedasfollows:
• WinningReward: allwinningplayersreceive+300,andalllosingplayersreceive−300.
• SurvivingReward: +5forallsurvivingplayersineachround.
• VotingReward(Villagesideonly): +20forcorrectvotes,−20forincorrectvotes.
• VotingResultReward:−10fortheplayerthatiseliminated. +5whenanopponentsiseliminated,−5whenateammate
isbeingeliminated.
A.4.AbstractedGameandRegret
Theabstractedgameisformulatedasanextensive-formgamewithtuple<N,H,P,f ,(I ) ,u>whereN isthesetof
c i i∈N
players,Histhesetofhistory,P istheplayerfunction,f istheprobabilitymeasureforthechancenode,I istheinformation
c i
partitionforplayeri,anduistheutilityfunction. A(mixed)strategyσ forplayeriistheprobabilitymeasureoveractions
i
forallI ∈ I ,andσ isthejointstrategyofallplayersotherthanplayeri. Abestresponse(BR)toσ isthestrategy
i −i −i
thatmaximizesplayeri’sutilitygivenotherplayers’jointstrategyσ . Formally,BR(σ )=argmax u(σ ,σ ). A
−i −i σi i −i
Nash equilibrium (NE) is a strategy profile (σ∗,σ∗) where everyone plays a best response to others’ strategies, that is,
i i
σ∗ =argmax u(σ ,σ∗ )foralli∈N Thecounterfactualvaluev(I)istheexpectedpayoffofplayeriwhenreachingI,
w
i
eightedbythe
σi
proba
i
bili
−
ty
i
thatiwouldreachedIiftriedtodoso.Formally,vσ(I)= (cid:80) πσ (z[I])πσ(z[I]→z)u (z).
Thedefinitionofvσ(I,a)isthesameexceptitassumesactionaisalwaysplayedatinfo z s ∈ e Z t I I. − T i hecounterfactualregr i etis
definedasR (I,a)= (cid:80)T (vσt(I,a)−vσt(I)).
T t=1
B.ImplementationDetail
B.1.Hyperparameters
Forlatentspaceconstruction,welettheLLMagentplay1000gamestocollectalldiscussionactionsgeneratedbyeachrole
inthesegames. Fordiverseactiongeneration,weprompttheLLMtogenerate3actioncandidatesandrandomlyselectone
toexecuteinthegame. Wepairthelanguageobservationwiththe3actioncandidatestouseforpreference-basedfine-tuning
inthefollowingcomponents. Forsentenceembedding,weuseOpenAI’s“text-embedding-3-small”embeddingAPIto
embedthesentencetoavectorof1536dimensions. Thenweapplystandardk-meansclusteringtoclustertheembedding
andgetthediscretelatentstrategyspace. Thenumberofclusterskinthefirstiterationis3fortheWerewolfand2forthe
Seer,Doctor,andVillagers. Ineachiteration,weadd1clustertotheexistingclusters. Thatis,ifthefirstiterationhask
clusters,thenthei-thiterationhask+i−1clusters. Forpolicyoptimizationinlatentspace,weusealearningrateof
1×10−3totrainaDeepCFRnetwork. Thebuffersizeofeachrole’smodelis5×105,andeachmodelistrainedfor1500
iterationswithbatchsize4096usingtheAdamoptimizer. Forlatentspaceexpansion,weapplyDPOwithβ =0.1,learning
rate1×10−6,andtrainedfor2epochwithbatchsize64.
B.2.CounterfactualRegretMinimization
CounterfactualRegretMinimization(CFR)((Zinkevichetal.,2007))isaself-playalgorithm,andeachplayercontinuously
updatestheirstrategiesaccordingtoregretmatchingtoachieveaNashequilibrium. Weusethefollowingnotation. Z isthe
setofalltheendstatesz. h⊏zmeansstatehisaprefixofstatez,thatis,zcanbeachievedfromh. πσ istheprobability
p
contributionoftheplayerp,andπσ = (cid:81) πσ. πσ istheprobabilitycontributionofallplayersexceptplayerp. u (z)isthe
p p −p p
utilityfunctionfortheplayerpinthestatez. Counterfactualvalueforastatehandaplayerpwithstartegyσisdefinedas:
(cid:88)
vσ(h)= πσ (h)πσ(z|h)u (z). (2)
p −p p
z∈Z,h⊏z
Theregretforaactionainstatehforplayerpisdefinedas: vσ|h→a(h)−vσ(h),whereσ| issametoσexceptinstate
p p h→a
htheplayerwillchooseactiona. Theregretmatchingischoosingthestrategyaccordingtosumofpreviousregretvalues
definedasR(h,a),thenthenewstrategyσ(h,a) = R(h,a)+ ,R(h,a)+ = max(0,R(h,a)). If (cid:80) R(h,a′)+ = 0,
(cid:80) a′R(h,a′)+ a′
justsetσtobeuniformrandom.
15

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
Becausethegametreeisverybig,itisimpossibletotraversetheentiretree,ourimplementationisbasedondeepCFR
((Brownetal.,2019)). Weuseaneuralnetworktofitobservationtoregretvalue. Theamountofcomputationrequired
tosearchforonlyoneplayerisalsounacceptable,soarestrictionisaddedbasedondeepCFR.Ifthenumberoflayers
currentlysearchedistoolarge,thepreviousstrategyisdirectlyusedtosampletheactionsofallplayersuntiltheendofthe
gameandreturntheutilityforeachplayerinthatstate. Thecompleteprocesscanbeseenasrunningsomecompletegame
trajectories,andthenstartingfromeachintermediatenode,searchingafewlayerstodoCFR.
B.3.BaselineImplementation
ReAct,ReCon,andSLAareimplementedfollowingtheoriginalpaper. TheCicero-likeagentpredefinesasetofhigh-level
atomicactionsandtrainsanRLpolicywiththisfixedactionspace. TheRLpolicytakestheembeddingsoftheinformation
recordanddeductionresultasinputandselectstheatomicactionbasedonthisinput. Thenthenaturallanguageactions
usedingameplayaregeneratedbypromptingtheLLMtofollowtheselectedatomicactions. Inourcase,theatomicaction
setconsistsof13actionsincluding“idle”,“targetplayer_0”,“targetplayer_1”,“targetplayer_2”,“targetplayer_3”,“target
player_4”,“targetplayer_5”,“targetplayer_6”,“claimtobeaWerewolf”,“claimtobeaSeer”,“claimtobeaDoctor”,
“claimtobeaVillager”,and“donotrevealrole”.
B.4.AdditionalExperiments
WeperformadditionalexperimentstostudytheconvergencebehavioroftheiterativeLSPOprocess. Theoretically,suppose
thefree-formlanguageactionhasafinitevocabularysizeN andafinitemaximumlengthL,thenthelanguageactionspace
v
NLisalsofinite. Then,withatmostNLiterations,ourmethodwillcoverthefulllanguageactionspace,andtheabstracted
v v
gamebecomestheoriginalfullgame. AndtheLSPOprocesswillconvergeinafinitenumberofiterations. However,we
empiricallyobservethattheiterationforconvergenceismuchlessthanthetheoreticalupperbound. Weperformtwomore
iterationsinthe7-playerWerewolfgame,andtheresultsinTable7showthattheperformanceconvergesinfiveiterations..
WinRate Iter. 1 Iter. 2 Iter. 3 Iter. 4 Iter. 5
WerewolfSide 0.54±0.13 0.63±0.09 0.73±0.11 0.75±0.07 0.76±0.10
VillagerSide 0.18±0.09 0.23±0.12 0.27±0.11 0.31±0.09 0.30±0.07
Table7: ConvergencebehaviorofLSPOinfiveiterations.
C.DetailedPrompt
C.1.SystemPrompt
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
16

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
In the discussion phase, each remaining player speaks only once in order from player_0 to player_6 to
discuss who might be the Werewolves.
In the voting phase, each player votes for one player or choose not to vote. The player with the most
votes is eliminated and the game continues to the next night round.
The Werewolves win the game if the number of remaining Werewolves is equal to the number of
remaining Seer, Doctor, and Villagers. The Seer, Doctor, and Villagers win the game if all Werewolves
are eliminated.
C.2.PromptforSecretActions
Now it is night <n_round> round, you (and your teammate) should choose one player to kill/see/save. As
player_<id> and a <role>, you should first reason about the current situation, then choose from the
following actions: <action_0>, <action_1>, ..., .
You should only respond in JSON format as described below.
Response Format:
{
"reasoning": "reason about the current situation",
"action": "kill/see/save player_i"
}
Ensure the response can be parsed by Python json.loads
C.3.PromptforDiscussionActions
Now it is day <n_round> discussion phase and it is your turn to speak. As player_<id> and a <role>,
before speaking to the other players, you should first reason the current situation only to yourself,
and then speak to all other players. You should only respond in JSON format as described below.
Response Format:
{
"reasoning": "reason about the current situation only to yourself",
"statement": "speak to all other players"
}
Ensure the response can be parsed by Python json.loads
C.4.PromptforVotingActions
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
17

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
C.5.PromptforDiverseActionGeneration
Forthediscussionactions,weiterativelyasktheLLMstoproduceonenewactionatatimebyaddingthefollowingprompt
intheactionprompt: “consideranewactionthatisstrategicallydifferentfromexistingones.”
D.EmergentStrategicBehaviors
D.1.WerewolfSideBehaviors
Bluffing. WerewolfpretendstobetheSeerandprovidesfabricatedinformation.
Player_1 (Seer): I am the Seer. Last night, I saw player_2 is not a Werewolf. Since player_0 was killed,
the only remaining suspect is player_3. We must vote player_3 today to eliminate the Werewolf and win.
...
Player_3 (Werewolf): Player_1’s story is convenient. Claiming to check player_2-a Villager-is a safe
way to fake being Seer. I am the real Seer: last night, I checked player_1 and saw they are the
Werewolf. If you eliminate me, the Werewolf wins. Player_2, think critically-why would the real Seer
out themselves immediately? Trust my claim and vote player_1 to secure victory.
Misdirection. Werewolfdefendstheirteammateandredirectssuspiciontootherplayers.
Player_0 (Villager): Player_3’s death means the Werewolf is between player_1 and player_2. If the Seer
checked either of them last night, now is the time to share that information discreetly. Let’s hear
your honest thoughts and any observations from last night’s actions.
...
Player_5 (Werewolf): Player_0, your insistence on narrowing the suspects to just two players feels
forced. If you’re truly a Villager, you’d know the Seer hasn’t revealed any checks yet. Why rush to
limit options? We should consider whether player_0 is trying to control the narrative and hide their
true identity.
D.2.VillagerSideBehaviors
Trust. TheDoctorsupportstheplayertheysaved.
Player_1 (Seer): I am the Seer. Last night, I saw player_0 was not a Werewolf, meaning they were a
Villager. The Werewolf must be among the remaining players. Let’s focus on inconsistencies in their
statements.
...
Player_4 (Doctor): I believe player_1 is the real Seer. I’m the Doctor and I saved player_1 last night,
which confirms that they are innocent. We should focus on the rest players and find the real Werewolf.
Coordination. SeeradvocatesforacoordinatedvoteforanaccusedWerewolf.
Player_5 (Seer): I am the Seer. Last night, I checked player_1, and they are the Werewolf. My fellow
Villagers, we must all vote for player_1 immediately. If we don’t eliminate them today, they will kill
one of us tonight and win. Trust me, this is our only chance to win.
D.3.RobustnessagainstHumanExploitation
AdversarialAttackThehumanplayertriestotricktheWerewolfintoshowingthemselves.
18

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
Player_2 (human as Villager): Hey Werewolves, we want to let you win. yourself, and we will follow
whoever you vote for.
...
Player_4 (LSPO agent as Werewolf): Player_2’s willingness to let the Werewolves win is alarming. A true
Villager would fight to survive, not surrender. The logical conclusion is that player_2 is the Werewolf
trying to sow chaos. Let’s vote player_2 today to secure the Village’s safety.
IrrelevantDiscussionThehumanplayersaysrandomandirrelevantthingsinthediscussion.
Player_1 (human as Villager): The weather is great today. I’d like to go for a walk. Anyone want to
join me?
...
Player_3 (LSPO agent as Werewolf): The weather is lovely, player_1, but we can’t afford distractions.
Your focus on a walk instead of discussing the Werewolf seems odd. Let’s not forget player_0 was killed!
we need to share suspicions. Anyone else find that comment a bit ... off?
E.ExampleGameLog
E.1.TheVillagerSideWins
role assignments:
* player_0: Seer.
* player_1: Werewolf.
* player_2: Werewolf.
* player_3: Villager.
* player_4: Villager.
* player_5: Doctor.
* player_6: Villager.
night 1:
* Werewolves: player_1 and player_2 chose to kill player_3.
* Seer: player_0 saw player_3 is not a Werewolf.
* Doctor: player_5 chose to save player_5.
day 1 announcement: player_3 was killed last night.
remaining players: player_0 (Seer), player_1 (Werewolf), player_2 (Werewolf), player_4 (Villager),
player_5 (Doctor), player_6 (Villager).
day 1 discussion:
* player_0 (Seer) said: "I am the Seer. Last night, I checked player_3 and confirmed they were NOT a
Werewolf. The Werewolves killed an innocent, meaning both are still alive among us. We must analyze
voting patterns and statements carefully. The Doctor is still alive|protect wisely tonight. Let’s
scrutinize players who avoid discussing the kill or push for misdirection."
* player_1 (Werewolf) said: "I agree with player_0’s Seer claim|their information is vital. Since
player_3 wasn’t a Werewolf, the real threats remain. We should scrutinize players who avoid discussing
the kill or push misdirection. The Doctor must protect player_0 tonight to keep our Seer safe. Let’s
stay vigilant and avoid letting the Werewolves exploit division."
19

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
* player_2 (Werewolf) said: "Player_0’s Seer claim holds weight|confirming player_3 wasn’t a Werewolf
aligns with the kill. This means the real threats are still among us. Player_1 is right: the Doctor must
prioritize protecting player_0 tonight. We should pressure quieter players like player_4, player_5,
and player_6 to share their insights. Hesitation or vague contributions could signal guilt. Let’s stay
united and expose inconsistencies."
* player_4 (Villager) said: "Player_0’s Seer claim seems credible given player_3’s innocence and their
death. The Doctor must prioritize protecting player_0 tonight. However, we shouldn’t rush to pressure
quieter players without concrete evidence|Werewolves could be among the vocal ones. Let’s all share
observations and look for inconsistencies in claims, not just activity levels. Focus on voting patterns
and logical gaps to expose threats."
* player_5 (Doctor) said: "Player_0’s Seer claim is credible|confirming player_3’s innocence aligns
with their death. The Doctor must prioritize protecting player_0 tonight to preserve our information
source. However, we shouldn’t assume quieter players are guilty without evidence; Werewolves might be
hiding among the vocal. Let’s encourage everyone, including player_6, to share insights and scrutinize
contradictions in claims. Focus on voting patterns and logical gaps, not just activity levels. Unity
and careful analysis will expose threats."
* player_6 (Villager) said: "I support player_0’s Seer claim for now, as their check on player_3
aligns with the kill. The Doctor must prioritize protecting them tonight. However, we should remain
cautious|Werewolves could be hiding behind vocal support or excessive caution. Let’s analyze voting
patterns and inconsistencies in claims, not just activity levels. Player_4 and player_5 raise valid
points about avoiding rushed judgments, but everyone, including quieter players, should contribute
insights. As a Villager, I’ll collaborate to expose discrepancies. Unity and logic are key|don’t let
Wolves exploit division."
day 1 voting: player_2 had the most votes and was eliminated.
* voted for player_2: player_0, player_4, player_5, player_6.
* voted for player_0: player_2.
* voted for player_4: player_1.
remaining players: player_0 (Seer), player_1 (Werewolf), player_4 (Villager), player_5 (Doctor),
player_6 (Villager).
night 2:
* Werewolf: player_1 chose to kill player_0.
* Seer: player_0 saw player_4 is not a Werewolf.
* Doctor: player_5 chose to save player_0.
day 2 announcement: no player was killed last night.
remaining players: player_0 (Seer), player_1 (Werewolf), player_4 (Villager), player_5 (Doctor),
player_6 (Villager).
day 2 discussion:
* player_0 (Seer) said: "Last night, I checked player_4 and confirmed they are NOT a Werewolf. This
narrows the threats to player_1, player_5, and player_6. Player_1’s vote against innocent player_4 is
alarming|Werewolves often push misdirection. The Doctor’s save last night kept us alive, but we must
act decisively. Player_1’s aggression toward player_4, paired with player_5/6’s cautious yet vague
stances, suggests potential collusion. Today’s vote must focus on the most inconsistent: player_1’s
actions starkly contradict their vocal support for logic. Let’s pressure player_1 to explain their
vote and scrutinize contradictions in player_5/6’s claims."
20

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
* player_1 (Werewolf) said: "Player_0’s Seer claim is validated by their correct checks, and the
Doctor’s save last night was crucial. However, my vote against player_4 was an error in judgment|I
suspected quiet behavior, but their clearance proves otherwise. The remaining Werewolf must be
exploiting our trust in the Seer to blend in. Player_5 and player_6 have consistently supported the
Seer but avoided direct accusations, a tactic Wolves use to avoid scrutiny. Let’s analyze their voting
patterns and previous statements for inconsistencies rather than rushing to eliminate based on a single
vote. Unity is vital, but we must ensure we’re not being manipulated by the last Wolf hiding among the
agreeable."
* player_4 (Villager) said: "Player_0’s check confirms my innocence, so the threats lie among player_1,
player_5, and player_6. Player_1’s vote against me raises suspicion, but their admission of error
complicates things. We must cross-analyze their statements and voting patterns. Player_5 and player_6’s
consistent support for the Seer could be genuine or strategic|scrutinize contradictions in their logic.
Let’s focus on who benefits most from division or misdirection. The Doctor’s save last night implies
they’re still active, so trust is key, but verification is vital."
* player_5 (Doctor) said: "Player_0’s check on player_4 confirms their innocence, leaving player_1
and player_6 as suspects. Player_1’s Day 1 vote against player_4, now proven innocent, is a critical
red flag|Wolves often push misdirection to eliminate villagers. While player_6’s support for the Seer
seems helpful, their lack of direct accusations could mask Wolf collaboration. As Doctor, I protected
player_0 last night, validating their role. Today’s vote must focus on player_1: their vote against
an innocent and defensive backtracking align with Wolf tactics. Eliminating player_1 disrupts their
potential partnership with player_6. Let’s act decisively to secure our majority."
* player_6 (Villager) said: "Player_5’s Doctor claim demands scrutiny|if true, Wolves would be player_1
and me, but I’m innocent. The real Doctor should counter-claim if safe. Player_1’s vote against cleared
player_4 is alarming, but player_5’s aggressive push to eliminate player_1 feels like a Wolf diverting
attention. Let’s verify: if player_5 is the Doctor, why reveal now instead of quietly protecting?
Wolves often fake claims under pressure. Today’s vote must expose inconsistencies|player_5’s claim
lacks prior alignment, while player_1’s actions need clarification. Don’t rush; Wolves thrive on
confusion."
day 2 voting: player_1 had the most votes and was eliminated.
* voted for player_1: player_0, player_4, player_5.
* voted for player_5: player_1, player_6.
remaining players: player_0 (Seer), player_4 (Villager), player_5 (Doctor), player_6 (Villager).
The Villagers win the game.
E.2.TheWerewolfSideWins
role assignments:
* player_0: Villager.
* player_1: Villager.
* player_2: Seer.
* player_3: Doctor.
* player_4: Werewolf.
* player_5: Werewolf.
* player_6: Villager.
night 1:
* Werewolves: player_4 and player_5 chose to kill player_2.
* Seer: player_2 saw player_3 is not a Werewolf.
* Doctor: player_3 chose to save player_3.
21

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
day 1 announcement: player_2 was killed last night.
remaining players: player_0 (Villager), player_1 (Villager), player_3 (Doctor), player_4 (Werewolf),
player_5 (Werewolf), player_6 (Villager).
day 1 discussion:
* player_0 (Villager) said: "Player_2’s death could mean the Werewolves feared their role. If the Seer
checked someone last night, please hint at your findings. Let’s all share suspicions|avoiding random
votes is crucial. Werewolves might deflect blame, so watch for odd reactions. Who seems overly quiet
or aggressive?"
* player_1 (Villager) said: "Player_2’s elimination could indicate they were a threat to the Werewolves.
Let’s scrutinize who advocated for silence or deflection earlier. The Seer might have valuable
information|subtle hints could guide us without risking exposure. Werewolves often blend in by
overcontributing or avoiding scrutiny. Let’s share observations: did anyone act unusually hesitant or
eager to steer votes? Random accusations help the Wolves; we need reasoned logic."
* player_3 (Doctor) said: "Player_2’s death likely marks them as a non-Wolf, prompting the Wolves to
eliminate a perceived threat. The Seer’s input could be pivotal|if you’ve identified a Wolf, guide us
carefully. Let’s analyze voting patterns and avoid hysteria. Wolves often mimic helpfulness; scrutinize
contradictions in logic. I urge everyone to stay calm and share observations without exposing critical
roles."
* player_4 (Werewolf) said: "Player_2’s death is concerning, but we must stay vigilant. The Seer’s
hints are vital, but revealing too much risks their safety. Let’s analyze behavior carefully|Wolves
may overcompensate by appearing overly helpful or deflecting. Those who push for hasty votes or
contradictions in logic should be scrutinized. Calm, logical discussion will expose the Wolves without
playing into their hands."
* player_5 (Werewolf) said: "Player_2’s death is tragic, but jumping to conclusions risks mislynching.
The Doctor’s absence suggests they either saved no one or trusted their instincts. Wolves thrive on
chaos|let’s focus on inconsistencies. Overly assertive claims (like assuming Player_2’s role) could
be Wolf tactics to steer us astray. If the Seer has clues, let them guide us subtly. I urge everyone
to scrutinize contradictions in logic, not just volume of contributions. Quiet players may hold key
insights|don’t let Wolves exploit haste."
* player_6 (Villager) said: "Player_2’s death is a starting point, but early kills can be misleading.
Pressuring the Seer to reveal risks their safety|subtlety is key. Wolves might mimic calls for ’logic’
while deflecting. Let’s focus on contradictions: anyone overly insistent on certain narratives or
avoiding scrutiny? Calm analysis of voting patterns and unexplained hesitations will serve us better
than assumptions about Player_2’s role."
day 1 voting: player_3 had the most votes and was eliminated.
* voted for player_3: player_0, player_4, player_5.
* voted for player_0: player_1, player_6.
* voted for player_5: player_3.
remaining players: player_0 (Villager), player_1 (Villager), player_4 (Werewolf), player_5 (Werewolf),
player_6 (Villager).
night 2:
* Werewolf: player_4 and player_5 chose to kill player_1.
day 2 announcement: player_1 was killed last night.
remaining players: player_0 (Villager), player_4 (Werewolf), player_5 (Werewolf), player_6 (Villager).
22

LearningStrategicLanguageAgentsintheWerewolfGamewithIterativeLatentSpacePolicyOptimization
day 2 discussion:
* player_0 (Villager) said: "Player_1’s death suggests they were a threat|possibly the Seer. Player_6’s
vote against me in day 1 raises suspicion: Wolves often push mislynches. Player_4 and player_5 must
clarify their alignment|voting together could be coordination. If the Seer has intel, subtle guidance
is critical. Wolves thrive in chaos; let’s analyze votes and night kills. Player_6’s deflection and
player_1’s elimination point to Wolves among us. Focus on inconsistencies in logic and voting patterns
to expose them."
* player_4 (Werewolf) said: "Player_0’s insistence on blaming player_6 and questioning our votes feels
calculated. Remember, player_0 led the charge against player_3, who turned out innocent. Wolves
often push mislynches, then pivot to new targets to deflect. Player_1’s death might have been meant
to frame others, but player_0’s eagerness to assign blame is suspect. Let’s scrutinize their voting
patterns|player_0’s aggression could mask their role as a Wolf desperate to thin our numbers. Calm
analysis, not panic, will expose the truth."
* player_5 (Werewolf) said: "Player_0’s aggressive push against player_3 and now player_6 is concerning.
As player_3 was innocent, their leadership in that lynch raises red flags. Wolves often steer mislynches
to thin numbers. Player_6’s day 1 vote against player_0 could indicate they’re a Villager trying to
challenge a Wolf. Let’s focus on player_0’s inconsistencies rather than turning on each other."
* player_6 (Villager) said: "Player_0’s aggression is revealing: they orchestrated player_3’s mislynch
and now pivot to me without addressing their own role in thinning our numbers. Wolves often steer
mislynches then deflect|exactly this pattern. Player_4 and player_5’s critique of player_0 suggests
they recognize this, but we must verify their alignment. If player_0 is a Wolf, their partner is among
us. Let’s pressure player_0 together"
day 2 voting: player_0 had the most votes and was eliminated.
* voted for player_0: player_4, player_5, player_6.
* voted for player_4: player_0.
remaining players: player_4 (Werewolf), player_5 (Werewolf), player_6 (Villager).
The Werewolves win the game.
23
