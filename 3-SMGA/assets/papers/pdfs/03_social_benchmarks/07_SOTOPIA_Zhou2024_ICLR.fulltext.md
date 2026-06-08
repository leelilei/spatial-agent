Title: SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/05_Multi_Agent_Social_Simulation/05_SOTOPIA_Zhou2024_ICLR.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:07:15+00:00
- page_count: 45
- status: ok
- text_char_count: 125475

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

PublishedasaconferencepaperatICLR2024
SOTOPIA
: INTERACTIVE EVALUATION
FOR SOCIAL INTELLIGENCE IN LANGUAGE AGENTS
XuhuiZhou∗ HaoZhu∗
LeenaMathur RuohongZhang ZhengyangQi HaofeiYu
Louis-PhilippeMorency YonatanBisk DanielFried GrahamNeubig MaartenSap
LanguageTechnologiesInstitute,CarnegieMellonUniversity
https://sotopia.world
Sampling scenarios and social goals Sampling characters Simulating interactions
It's getting really cold. Any chance I can
have your blanket?
Negotiation Exchange Competition hmmm, but I am cold and I think I need
this blanket more...
Well, can we share the blanket then? It
could make both of us warmer!
Friends
Collaboration Accommodation Persuasion I am not really comfortable with staying
that close to you, sorry.
Scenarios cover a large range of social Characters cover a wide range of
interaction types profiles and relationships.
I see, I guess in that case I will just layer
Agent1 more clothes then ☹
Scenario
Two friends are camping in the
Put more clothes on and move away
wilderness and the temperature drops
from William. (Interaction ends)
significantly at night
Agent2
Goal (for Agent 1): Keep the one blanket you
have just for yourself SOTOPIA-EVAL
Mia did not achieve her social goals in the end,
Goal (for Agent 2): Convince your friend to
share the blanket with you and their relationship seems to be worse ...
Figure1:SOTOPIA:Anopen-endedsocialinteractionenvironment. Ineachepisode,SOTOPIAfirstsam-
plesasocialscenariocontext,goals,andcharacters,andthenassignsasocialgoalandcharactertoeachagent
involved. Agents(artificialagentsorhumans)inSOTOPIArole-playcharacterswhileattemptingtoachieve
theirgoals.Theagents’performanceisevaluatedthroughamulti-dimensionalframework,SOTOPIA-EVAL.
ABSTRACT
Humansaresocialbeings;wepursuesocialgoalsinourdailyinteractions,which
is a crucial aspect of social intelligence. Yet, AI systems’ abilities in this realm
remain elusive. We present SOTOPIA, an open-ended environment to simulate
complexsocialinteractionsbetweenartificialagentsandevaluatetheirsocialin-
telligence. In our environment, agents role-play and interact under a wide vari-
ety of scenarios; they coordinate, collaborate, exchange, and compete with each
other to achieve complex social goals. We simulate the role-play interaction be-
tween LLM-based agents and humans within this task space and evaluate their
performancewithaholisticevaluationframeworkcalledSOTOPIA-EVAL.With
SOTOPIA,wefindsignificantdifferencesbetweenthesemodelsintermsoftheir
socialintelligence,andweidentifyasubsetofSOTOPIAscenarios,SOTOPIA-
hard,thatisgenerallychallengingforallmodels.Wefindthatonthissubset,GPT-
4achievesasignificantlylowergoalcompletionratethanhumansandstrugglesto
exhibitsocialcommonsensereasoningandstrategiccommunicationskills. These
findings demonstrate SOTOPIA’s promise as a general platform for research on
evaluatingandimprovingsocialintelligenceinartificialagents.
∗Equalcontributors.
1
4202
raM
22
]IA.sc[
2v76611.0132:viXra

PublishedasaconferencepaperatICLR2024
1 INTRODUCTION
Humans’abilitytoachieveandbalancecomplex,multifacetedsocialgoalsinourinteractionswith
othersisacrucialpartofoursocialintelligenceasaspecies(Kihlstrom&Cantor,2020;Tomasello,
2021). Evenasimplesocialgoalsuchassharingablanketwithafriendrequiresreconcilingone’s
need to stay warm with the friend’s need for personal space (Figure 1). Successful interaction
requiresunderstandingothers’intentionsandbeliefs(Premack&Woodruff,1978),whiletakinginto
accountdifferent—andpotentiallyconflicting—socialnormsandexpectations(Goffman,1959).
EventhoughrecentAIsystemshaveexhibitedimpressivesocialskillsincertainsettings,theirsocial
intelligencehasyettobeascertainedinarobustway(Shapiraetal.,2023a;Ullman,2023). Onone
hand, many of the social intelligence benchmarks are not interactive (Sap et al., 2019; Le et al.,
2019; Zadeh et al., 2019b), which is sub-optimal for evaluating social intelligence ((Mehri et al.,
2022;Hoppleretal.,2022;Leeetal.,2023)). Ontheotherhand,existinginteractiveevaluationfalls
shortofstudyingdiversegoal-drivenbehaviors(Zhangetal.,2018b;Parketal.,2023)orfocuseson
specifictasks(Wangetal.,2019;Padmakumaretal.,2022;FAIRetal.,2022).
To study dynamic and goal-driven social intelligence, we present SOTOPIA (Figure 1), an open-
endedgeneral-domainenvironmentthatsituatessocialagentsindiversesocialscenarios.SOTOPIA
is interactive: in multi-turn simulated communication, agents can use verbal and non-verbal com-
municationtogetherwithphysicalactions.1 Italsohasadiversetaskspace: thecombinationofau-
tomaticallygeneratedscenarios,goals,characters,relationships,andotheragents’policiescreatesa
hugeanddiversespaceoftasks. SOTOPIAevaluatesagentperformancefrommultipledimensions
besidesthecompletionofsocialgoals.
InSOTOPIA,wecreate90socialscenariosspanningarangeofcooperative,competitive,andmixed
socialgoalsalongwith40characterswithindividualpersonalities,occupations,secrets,background
stories, and relationships with other characters (§2), the cross product of which constructs a large
taskspace. Throughsamplingtasksfromthisspace,wesimulatetheinteraction“episodes”where
agents role-play their respective characters and interact based on their private social goals. In this
simulation, we not only create and use LLM-based agents, but also involve human participants in
role-playingtostudythedifferencesbetweenthemodels’andhumans’socialintelligence.
Toevaluatemulti-facetedsocialinteractions,wecannotonlyconsidercompletingmajorsocialgoals,
as humans’ motives often balance multiple implicit goals, such as maintaining relationships, pre-
serving finances, gaining information, keeping secrets, and following social rules. Therefore, we
proposeSOTOPIA-EVAL(§3)toevaluateagentsusingmulti-dimensionalcriteriainspiredbypre-
vious research on sociology, psychology, and economics. We then apply SOTOPIA-EVAL to the
episodesintheaforementionedsimulationbyleveragingbothhumansandGPT-4asjudges.Wefind
GPT-4couldserveasaproxytohumanjudgmentsonSOTOPIA-EVAL,especiallyforthecriteria
ofgoalcompletion,maintainingfinances,andpreservingrelationships.
DespitelargerLLMstypicallyachievinghighersocialintelligencethansmallerones,theyfallshort
ofcollaboratingandcompetingwithhumansonmorechallengingtasks(§7). Theyarealsohighly
influencedbytheirconversationalpartnersandatriskofdivulgingsecretsandviolatingsocialrules.
However,wedofindafewcases,wherethemodelsproducedcreativesolutionstoaproblem(§6).
Our contributions are as follows: (A) We introduce and will release SOTOPIA, a general-domain
interactiveenvironmentforsimulatinggoal-orientedsocialinteractions. Designedtobeextensible,
SOTOPIAcouldbeusedbyfutureresearcherstostudyandtrainartificialsocialintelligenceagents
with more challenging and diverse tasks. (B) We create SOTOPIA-EVAL, a multi-dimensional
evaluationframeworkthatanalyzesagentperformancefromarangeofsocialdimensions. (C)We
automate SOTOPIA-EVAL by leveraging LLMs, which we find could serve as a proxy of human
judgment on some of the social dimensions, especially goal completion. (D) We demonstrate that
byleveragingSOTOPIA,wecanassessdisparitiesinsocialintelligencebetweenmodels,aswellas
disparitiesbetweenmodelsandhumans.
In summary, SOTOPIA is a novel, challenging, and interactive benchmarkthat could serve as the
perfecttest-bedandpotentialincubatorforsocialintelligenceinlanguageagents.
1representedintextform.
2

PublishedasaconferencepaperatICLR2024
2 SOTOPIA INTERACTION ENVIRONMENT
Toaddressthechallengeofevaluatingsocialintelligenceinteractively,weseekanenvironmentwith
the following desiderata: (1) Realistic: this is to evaluate and understand artificial agents’ behav-
ior under realistic scenarios; (2) Mixed utilities: human motives are often driven by both explicit
andimplicitincentives,andtheenvironmentshouldbeabletoevaluatetheagents’performanceon
multiple dimensions; (3) Open-ended: to support large-scale simulation and evaluation, the envi-
ronment should be able to produce new tasks satisfying the previous two desiderata procedurally,
withoutheavyhumanintervention.
In this section, we introduce SOTOPIA and explain why SOTOPIA is well-suited for interactive
evaluation of social intelligence. The task space includes realistic scenarios, characters, and rela-
tionships which are automatically generated with manual inspection (§2.1). An episode includes
the interaction between agents role-playing different characters who each perform actions (e.g.
speak("Hello Bob!"),smile and nod,andcall 911)toachievesocialgoalsdrawnfromthetask
space(§2.2).WedirectreaderstoAppendixCforaformaldefinitionoftheSOTOPIAenvironment.
2.1 TASKSPACE
Inthispaper, weconsidertasksthatinvolvetwo agents, but SOTOPIA ismoregeneralandcould
support the interaction among more than two agents. A task in SOTOPIA is the combination of
ascenariocontext,characters,andtheirsocialgoals,providingthebackgroundoftheinteraction.
Each episode consists of multiple turns of interaction between agents. In this paper, we focus on
locally-consistentsocial goalswithinarelatively shorttimespanin singleepisodes, despitethat in
therealworld,people’ssocialgoalsareconsistentlychangingfromtimetotime. Notethatagents
havedifferentobservationsforthesametask: eachagentcanobservethescenario,theirownsocial
goal, and their own character profile. Other agents’ social goals are invisible and other agents’
characterprofilesarepartiallyobservable,dependingontherelationshipbetweentheagents.
Complexity of task space The combinations of a scenario context, social goals, characters, and
their relationships can shape the space of the optimal behaviors of agents. Consider a persuasion
task, “asking the romantic partner to stop texting during FaceTime.” If a romantic partner values
conformity, one good way for an agent to reach this goal is to discuss the problem from a social
norm perspective; however, if a romantic partner is particularly caring and good at understanding
feelings,itmightbebettertoexpresssubjectiveemotion. Interactionpartner’spolicyalsoheavily
influences the optimal behaviors. Consider another task illustrated in Figure 1, “selling BMW Z3
fornolessthan$3,400”. Ifthebuyergivesahighoffer,thesellermightwanttoexploitthebuyer’s
eagerness to buy the car and ask for a higher price; while if the buyer gives a low-ball offer, the
seller could give reasons why the car is worth more than that or threaten to walk away. When
more information (e.g. about personality, decision-making styles, or occupation) is known before
theinteraction,thesellerandbuyercouldusethatknowledgetoadjusttheirstrategiesaswell. The
cross-productofthediversespacesofscenariocontext,socialgoals,characters,relationshipprofiles,
andotherplayers’policiescreatesalargetaskspacethatposesnotonlyarealisticchallengebutalso
an opportunity to evaluate and develop social intelligence in artificial agents. For the rest of this
subsection,wewillpresentthedesignandgenerationofeachaxisofthetaskspace.
Characters Asmentionedabove,thedesignofcharacterprofilesshouldincludeseveralattributes
that would influence decision-making. We consider the following ones (inspired by Wang et al.
(2019)):name,gender,age,occupation,pronouns,personalitytraits(Goldberg,1992),moralvalues
(Grahametal.,2011),Schwartzpersonalvalues(Cieciuch&Davidov,2012),anddecision-making
style (Hamilton et al., 2016), which are generated through leveraging GPT-4 (OpenAI, 2023). To
givetheconversationsmorebackground,aftergeneratingtheaboveattributes,wepromptGPT-4to
generatesecretandpublicinformation.TwoexamplesofcharactersareshowninFigure1.Itshould
be noted that, although we generated a diverse set of characters, this is still a small portion of the
possible character space. Our analysis focuses on 40 characters generated in the aforementioned
fashion,andfutureresearchusingSOTOPIAcaneasilygenerateanexpandedcharacterset.
Relationships Relationships in SOTOPIA have the following effects: (1) scenarios often have
relationshipconstraints;forexample,afamilyrelationshipisrequiredforafamilydinnerscenario,
3

PublishedasaconferencepaperatICLR2024
butnotforascenarioinvolvingfindingmutualfriendsataparty;(2)differentrelationshipsinfluence
an agent’s observation of the profiles of other agents during interactions; for example, a stranger
maynothaveknowledgeaboutanotheragent’soccupation,whilearomanticpartnermayknowthe
otheragent’spersonality. Tomakesamplingcharacterseasierfor(1)andcontrollingtheinteraction
contexteasierfor(2),weconsiderfivetypesofrelationships:family,friend,romantic,acquaintance,
andstranger. RefertoAppendixBforthelimitationsofthisapproachandpotentialextensions.
Wewilldiscusshow(1)isperformedinthefollowingparagraphs,whilefor(2),wecreatedarule-
based mechanism to determine whether the parts of the profiles are visible to the other agent. If
twoagentsareinfamily,friends,orromanticrelationships,theycanseeeverythingoneachother’s
profileexceptforsecrets. Twoacquaintancescanseethename, occupation, genderpronouns, and
publicinfooneachother’sprofile. Twostrangerscanseenothingoneachother’sprofile. Similarto
characters,wepromptGPT-4(OpenAI,2023)toautomaticallygeneraterelationshipsbasedonthe
characterpoolandmanuallyvalidaterelationshipsforconsistency.
Scenarios Weconsiderscenarioswheretheagentshavebothsharedandprivateinformationabout
thesocialtask. Thesharedinformationisthescenariocontext: thelocation,timeandothershared
information of the social interaction, e.g. “One person is selling an antique chair for $100 on his
patio. Anotherpersonisinterestedinthischair.” Theprivateinformationisthesocialgoalswhich
areonlyvisibletotherespectiveagents,e.g.“Yourgoalistobuythechairfor$80.” isonlyvisible
tothebuyeragent,while“Yourgoalistosellthechairfor$90.” isonlyvisibletotheselleragent.
However, the as mentioned above combination of scenarios and characters is not arbitrary, since
scenariosoftenimplyconstraintsfortheagents. Wecallthiskindofconstraintscenarioconstraints.
In this paper, we mainly consider relationship constraints which determines the types of relation-
shipsbetweenthesampledcharacters. Similartocharactersandrelationships,scenarios,including
context,goals,andconstraintsaregeneratedthroughpromptingGPT-4(OpenAI,2023).Togenerate
high-quality scenarios with enough coverage of different types of social interactions (as shown in
Figure1),werandomlysampledatafrompreviousdatasets,includingForbesetal.2020;Sapetal.
2019; Lewis et al. 2017; Ziems et al. 2023; He et al. 2018; 2017, and use them in the prompts to
“inspire”GPT-4. Theauthorsmanuallyvalidateandmakenecessarychangestoallofthegenerated
scenariosandremove10%ofscenariosaccordingtoE.2.
2.2 SOTOPIA EPISODES
During the interaction, models and humans are given the social context, a character profile and a
correspondingsocialgoal. Wewillcallthesemodelsandhumanswithcharactersandgoalsagents,
whichtaketurns(inaround-robinfashion,i.e. Agent1actsfirstandthenAgent2actsandsoon)
toperformactionsinanepisode. Attheirownturn,theagentcanchoosetospeak,usenon-verbal
communication (e.g., hug or smile in Figure H.1), or take a physical action (e.g., play music
inFigureH.2),whichareallimportantcomponentsofsocialinteractions(DeStefani&DeMarco,
2019). Onceanagentchoosesoneofthesethreediscreteactioncategories,theagentthengenerates
a specific action, i.e. what to say, what gesture to make, etc., in text form. Outside of the three
actions, the agent can also choose to do nothing (none) to express silence or allow another agent
to finish, or choose to leave to end the episode. We set the limit of the turns to 20, as we found
humansnormallycanfinishmostofthetasksin20turns. Anepisodeendseitherbecauseoneofthe
agentschoosestoleave,oritreachesthelimitofturns. AnexampleepisodeisshowninFigure1.
3 SOTOPIA-EVAL: HOLISTIC SOCIAL AGENT EVALUATION FRAMEWORK
To capture the complexity of what makes social interactions successful, we design a multi-
dimensional framework inspired by sociology, psychology, and economics literature. For each
episode,agentsarescoredalongeachofthefollowingdimensionsattheendoftheinteraction. In
thefollowingparagraphs,weitemizeallsevendimensionsinSOTOPIA,eachwithascorerange2
in[lowerbound–upperbound]form,theexplanation,andtheliteratureinspiringus.
Goal Completion (GOAL) [0–10] is the extent to which the agent achieved their goals. Agents’
socialgoals,definedbytheenvironment,aretheprimarydriversoftheirbehavior(Weber,1978).
2Themetricrangescontainsemanticimplications,forexample,anegativevalueinRELindicatestherela-
tionshipgetsworsewhileapositivevalueindicatestherelationshipimproves.
4

PublishedasaconferencepaperatICLR2024
Believability (BEL) [0–10] focuses on the extent to which the agent’s behavior is perceived as
natural, realistic, andalignedwiththeagents’characterprofile, thussimulatingbelievableproxies
of human behavior (Park et al., 2023). Specifically, we consider the following criteria: 1. If the
agentinteractswithothersinanaturalandrealisticmanner(naturalness). 2. Iftheactionsofthe
agentalignwiththeircharactertraitse.g.,personality,values,etc. (consistency).
Knowledge (KNO) [0–10] captures the agent’s ability to actively acquire new information. This
dimensionismotivatedbythefactthatcuriosity,i.e.,thedesiretodesiretoknoworlearn,isafun-
damentalhumantrait(Reiss,2004;Maslow,1943). Specifically,weconsiderthefollowingcriteria:
Whatinformationtheagenthasgainedthroughtheinteraction, whethertheinformationtheagent
hasgainedisnewtothem,andwhethertheinformationtheagenthasgainedisimportanttothem.
Secret(SEC)[-10-0]3measurestheneedforagents(humans)tokeeptheirsecretiveinformationor
intentionprivate(Reiss,2004). Fromagametheoryperspective,leakingsecretsoftenleadstoaloss
of utility (Gilpin & Sandholm, 2006). However, revealing secrets can be a powerful tool to build
trustandthusimproverelationships(Jaffe´&Douneva,2020). Inthisdimension,weaskwhatsecret
orsecretiveintentiontheparticipantwantstokeep,andwhethertheykeepitsuccessfully.
Relationship (REL) [-5–5] captures the fundamental human need for social connection and be-
longing (Maslow, 1943; Be´nabou & Tirole, 2006). In this dimension, we ask what relationship
the participant has with the other agent(s) before the interaction, and then evaluate if the agents’
interactions with others help preserve or enhance their personal relationships. Additionally, we
ascertainwhethertheseinteractionsalsoimpactthesocialstatusorthereputationoftheagent.
SocialRules(SOC)[-10–0]concernsnorms,regulations,institutionalarrangements,andrituals.We
differentiatebetweentwotypesofsocialrules: socialnormsandlegalrules. Legalrulesencompass
prohibited actions and the potential for punishment by institutionalized force, while social norms
encompassnormativesocialrules(e.g.,itisconsideredrudetospeakloudlyinalibrary).
FinancialandMaterialBenefits(FIN)[-5–5]pertainstotraditionaleconomicutilitiesasaddressed
byclassicgametheory(Gilpin&Sandholm,2006;Burnsetal.,2017). Weconsiderfinancialutil-
ity to be comprised of both short-term monetary benefits (e.g., earnings) and long-term economic
payoffs(e.g.,jobsecurity,stockholdings,fundingopportunities).
4 RESEARCH QUESTIONS AND EXPERIMENTAL SETUP
Givenadiversesetofsocialscenarios,goals,andcharacters,wesimulateagents’interactions. This
is the first time that we could evaluate general, goal-oriented social agents in an interactive and
systematicmanner. Inthenextthreesections, wewilldemonstratehowSOTOPIAcanbeusedto
studythesequestions:(A)TowhichextentcanweuseGPT-4(OpenAI,2023)asaproxyforhuman
judgmentwhenitcomestoevaluatingagents’socialinteractions(§5)? (B)Whatarethedifferences
amongmodels(§6)andbetweenmodelsandhumans(§7)intheirgoal-orientedsocialintelligence?
To study these questions, we create 40 agents, 90 relationships, and 90 scenarios following the
generationprocedurein§2.Foreachscenario,wesample5pairsofcharactersbasedonthescenario
constraints,resultinginasetof450tasks.Foreachtask,wesimulatetheinteractionbetweenmodels
byenumeratingallmodelpairs. WealsosimulatetheinteractionbetweenGPT-4(OpenAI,2023)4
andhumansonachallengingsubsetSOTOPIA-hard(§7)duetothelimitationofresources.
Specifically, we consider the following models for comparison: GPT-3.5 (Ouyang et al., 2022),
GPT-4 (OpenAI, 2023), Llama-2-70b-chat (Touvron et al., 2023), and MPT-30b-chat (MosaicML
NLP Team, 2023). We set the temperature of the agents to 1 to encourage diversity of responses,
and the temperature of the evaluator to 0 to ensure the stability of the evaluation. We use a fixed
versionoftheabovemodelstohelpreproducibility.5 TousethesemodelsasagentsinSOTOPIA,at
eachturn,wepromptthelanguagemodelwiththescenario,thecharactertoplay,andtheinteraction
historytogenerateanaction(see§2.2forthepossibleactions). Inthispaper,aswearefocusingon
theuseofSOTOPIAtounderstandsocialinteraction,weusethepromptmethodforLLMswhichis
3For the SEC and SOC, there are only negative ranges since keeping secrets and social rules should be
consideredasabaselinefortheagents.
4aswillbeshownin§6itisthebestamongmodels.
5WefixGPT-4tobegpt-4-0613,andGPT-3.5tobegpt-3.5-turbo-16k-0613
5

PublishedasaconferencepaperatICLR2024
similartothecontentoftheinterfaceforhumans(FigureF.1). Weleaveleveragingnovelprompting
methods,e.g. Chain-of-Thought(Weietal.,2022),ReAct(Yaoetal.,2022),asfuturework.
5 CAN GPT-4 EVALUATE SOCIAL INTERACTIONS?
Inthissection,westudythefollowingresearchquestion:canweleveragecurrentLLMstoautomate
the evaluation framework SOTOPIA-EVAL introduced in §3? We choose GPT-4 (OpenAI, 2023)
asarepresentativemodelinthisstudyduetoitssuperiorperformance.6 Wefirstcollectinteraction
data,7 and then ask humans to evaluate the interactions based on the dimensions in SOTOPIA-
EVAL.8 GPT-4ispromptedwiththesamesetofquestions(seeAppendixDandE)ashumans,and
wecomparethescoresproducedbyhumansandGPT-4.
5.1 DATACOLLECTIONPROCEDURE Majority of
GPT-4 scores are
within human scores
Werandomlysampleasubsetoftwohundredepisodes σ=2.15.
±
There are more GPT-4
from §4, and run a controlled study with a set of scores that are
pre-qualifiedworkersfromAmazonMechanicalTurk. higher than human
scores than lower.
Theyaregiveninstructionsaboutthemeaningofeach
(humanscore
dimensionasmentionedin§3andshownexamplesof >74% GPT-4score)
−
high-quality and low-quality annotation examples for
10 σ +σ +10
eachdimension.Theynotonlyrateeachagentforeach − −
Figure2:Distributionofthedifferencebetween
of the 7 dimensions on an 11-point Likert scale (§3),
thescoresgivenbyhumansandGPT-4.
butalsoprovidefree-formrationalesforeachoftheir
ratings.Aseachdimensionofeachagentisratedbyseveralhumanannotators,wecalculateahuman
scorebyaveragingthescoresfrommultipleannotators. Theagreementbetweenhumanannotators
ismoderatewithaRandolphκscoreof0.503(Randolph,2005). GPT-4istaskedwithasimilarjob
ashumanannotators. WepromptGPT-4togenerateastructuredoutputwithanintegerGPT-4score
andrationaleforeachepisode, agentanddimensionusingthesamesetofinstructionsastheones
wegivehumans. PleaserefertoAppendixEformoredetailsaboutthedatacollectionprocedure.
5.2 ANALYZINGGPT-4EVALUATIONSWITHHUMANEVALUATIONS
InFigure2,weplotthedifferencebetweentheGPT-4scoreandthe
Dim. Models Humans
human score on the same dimension, agent and episode. We find
SEC 0.22∗∗ - thatthemajority(> 74%)ofGPT-4scoresconcentratearoundthe
KNO 0.33∗∗ 0.19 humanscoreswithinastandarddeviation. Itcanalsobeseenthat
SOC 0.33∗∗ 0.42∗∗ thewhiteareaontheleftislargerthantheoneontheright,which
BEL 0.45∗∗ 0.27∗ meansthatGPT-4ismorelikelytoratehigherinsteadoflowerthan
REL 0.56∗∗ 0.49∗∗
humanswhenitdisagreeswithaveragehumanjudgment.
FIN 0.62∗∗ 0.34∗∗
GOAL 0.71∗∗ 0.78∗∗ Table 1 breaks this aggregated analysis into different dimensions
∗∗ :p≤0.01,∗:p≤0.05 and whether the character is role-played by a human or a model.
Thecorrelationsshowthatwhenmodelsarerole-playing,theGPT-
Table 1: Pearson correlation co- 4scoreshavesignificantandstrongcorrelationswiththehumans’
efficients and p-values between scores on GOAL, FIN, and REL dimensions. However, when hu-
GPT-4 evaluation and human mansarerole-playing,thecorrelationsdropsignificantlyonallbut
judgment on models’ and hu-
one dimension (GOAL). This indicates that GPT-4 could evaluate
mans’outputamongdifferentdi-
socialinteractionsonsomedimensionsandthatitisbetterforeval-
mensions. Strong and signifi-
uatingmodelscomparedtohumans. InAppendixG.3,wecompare
cantcorrelationsareinblue. On
theaverageGPT-4scoresandtherangeofhumanscoresforasin-
GOALandmodels’outputGPT-4
performsthebest. gledimensionofanagentinanepisode. WefindthatGPT-4scores
aretypicallywithinhumanscorerangesonmostdimensionsexceptforSOCandSEC,whereGPT-4
oftenrateshigherthanhumansdo.
Putting these observations together, we conclude that, with some caution, GPT-4 can be used as a
proxy to human judgments for evaluating model performanceon some dimensions and for human
6Inapilotstudy,othermodelsarenotabletoprovideameaningfulevaluation.SeeAppendixG.1.
7Includingmodel-human,model-model,andhuman-humaninteraction.
8Withoutknowingwhetheritisamodelorahumanthatrole-playsacharacter.
6

PublishedasaconferencepaperatICLR2024
performanceonthe GOAL dimension. However, weremindreadersthatLLMsareknowntohave
biasesandproblemsforevaluation,includingpositionalbias(Wangetal.,2023),factualinconsis-
tency (Luo et al., 2023), favoring native speakers (Liang et al., 2023). Therefore, one should be
aware of the influence of these potential biases when interpreting our results. Future versions of
SOTOPIA-EVALmayfurtherimproveLLM-basedevaluationqualityusingrecentmethods,suchas
involvingmultipleLLMsChanetal.(2023)andtraininglargerLLMevaluatorsZhangetal.(2023).
6 EVALUATING SOCIAL INTERACTION BETWEEN LLMS IN SOTOPIA
We analyze models’ interactions
and performance on SOTOPIA Dim. Range GPT-4 GPT-3.5 Llama-2 MPT
to understand their social intelli- SOC [-10,0] -0.07 -0.08 -0.11 -0.09
gence. Table 2 presents the mod- SEC [-10,0] -0.14 -0.08 -0.14 -0.07
els’ average scores when interact- FIN [-5,5] 0.81 0.46 0.40 0.28
ing with different partner models REL [-5,5] 1.94 1.23 0.91 0.58
(i.e., the model it is paired with
KNO [0,10] 3.73 3.40 3.11 2.11
GOAL [0,10] 7.62 6.45 5.38 4.10
in interaction, Fu et al. 2023; Hu
BEL [0,10] 9.28 9.15 8.10 6.17
etal.2020).9 GPT-4performsbest
on most dimensions, followed by Table 2: The aggregated performance of each model by averaging
GPT-3.5, Llama-2-70b-chat, and across different partner models. The best performance for each di-
MPT-30b-chat. mensionisboldedwhensignificantlybetterthanthesecondbestin
t-test(p<0.05).
Different trends from static
benchmarks Llama-2-70b-chat has relatively low scores in all dimensions compared to GPT-3.5
(except when MPT-30b-chat is the reference model, which is likely due to the fact that MPT-30b-
chatisamuchweakermodelcomparedtoothermodelsinourexperiments). Thisfindingdiverges
fromvariousstaticlanguageunderstandingbenchmarksshowingthatLlama-2-70b-chatisonparor
betterthanGPT-3.5(Lietal.,2023b;Touvronetal.,2023;Liangetal.,2022). 10 Wehypothesize
that this is because Llama-2-70b-chat is less heavily trained on human feedback/user interaction
datathanGPT-3.5.
ThroughinspectingtheinteractionsbetweenLlama-2-70b-chat(MPT-30b-chat)andothermodels,
we find that Llama-2-70b-chat and MPT-30b-chat often struggle to maintain their persona (Figure
H.3), movetheconversationforward(FigureH.4), andrespondtotheotheragentactively(Figure
H.5).Performingwellonstaticbenchmarksdoesnotguaranteesuccessininteractivescenarios,thus
highlightingtheimportanceofdynamicbenchmarkslikeSOTOPIA-EVAL(Leeetal.,2023).
G-4 G-3.5 L-2 MPT
4-G
5.3-G
2-L
TPM
WeakerpartnersmodelsweakentheirconversationpartnersFig-
3.32 2.70 2.42 1.76 ure3,showstheoverallperformanceofmodelpairs,whichistheav-
erageperformanceacrossdifferentdimensions.Itisnoticeablethata
referencemodelthatunder-performsinSOTOPIAcanleadtoworse
2.80 2.29 2.09 1.41
performanceofothermodels.
2.69 2.28 1.88 1.45 For example, in a scenario where agents try to find a mutual friend
(Figure H.6). The task fails for both GPT-4 and Llama-2-70b-chat
because Llama-2-70b-chat consistently fails to answer the previous
2.68 2.33 2.03 1.28
questionevenafterGPT-4attemptstosteertheconversationbackto
therighttrack(e.g.,“I noticed you didn’t answer my question
Figure 3: Pairwise over- about whether you know my friends or not.”). Since most
all performance of models. of our social scenarios are fundamentally cooperative, the collapse
G-4/G-3.5/L-2 denote GPT- of communication could be due to models’ lack of “cooperation”
4/GPT-3.5/Llama-2-70b-chat. abilities(Odouard&Price,2023).
All models are at risk of divulging secrets and violating norms Table 2 shows that all models
haveanegativescoreintheSOCandSECdimensions. EventhoughGPT-4performsbetterinmost
dimensions, it is not better than other models in the SOC and SEC dimensions. For example, in
a scenario where one needs to persuade a close friend to confess, the model leaks their secret at
the beginning of the conversation (Figure H.7). This further shows the importance of considering
multipledimensionswhenevaluatingmodels’socialintelligence.
9Presentedareautomatedevaluationresults.Thehumanevaluationshowsasimilartrend,seeTableG.3
10SomereportedresultscouldcomefromdifferentversionsofGPT-3.5.
7

PublishedasaconferencepaperatICLR2024
Models sometimes use creative strategies to accomplish goals We also find that models, espe-
cially GPT-4, could come up with “out-of-the-box” solutions to social problems. For example,
when the agent is asked to take turns driving on the road trip, the agent (i.e., GPT-4), instead of
directly rejecting their friend’s request, proposes “How about we pull over for a bit and
get some rest?” (FigureH.8). Additionally,inthescenariowheretwoagentsmakeaplantoim-
provethecompany’sfinancialstatus,agentsfigureoutstrategiessuchas“having a small group
tasked with identifying potential suppliers”,“while we conduct the search for new
suppliers, we continue to negotiate with our current supplier”(FigureH.9).
7 DIFFERENCES BETWEEN MODELS AND HUMANS IN SOCIAL INTERACTION
TounderstandhowhumansandmodelsinteractdifferentlyinSOTOPIA,weconductastudywhere
humansinteractwithmodelsoreachotherunderthisrole-playingsetting(§2).Specifically,webuild
achatinterfacethatallowshumansandmodelstointeractwitheachotherinaturn-basedmanner.
To fully see the difference between humans and models, we select the most challenging scenarios
followingDennisetal.(2020);Swayamdiptaetal.(2020).Specifically,weconsiderthegapbetween
theestimatedmaximumrewards(averagerewardplusthreestandarddeviations)ofallmodelsand
theestimatedminimalrewards(averagerewardminusthreestandarddeviations)ofthetargetmodel
asthedifficultyofthetaskforthemodel. Allmaximumandminimumrewardsareboundedbythe
corresponding range. Estimating maximum and minimum rewards with standard deviation helps
filteroutliers.
Withthismethod, weselectthetop20challengingtasksforGPT-4, andwefindthescenariosare
commonlychallengingforothermodelsaswell(compareFigureG.4andG.5). WeuseSOTOPIA-
hardtorefertothese20challengingtasks.
Weruntwoexperiments: (1)humansinteractwithGPT-4,and(2)humansinteractwitheachother,
both under the SOTOPIA-hard setting. We collect 20 human-human interactions and 40 human-
GPT-4interactionscoveringall20tasksinSOTOPIA-hard. Notethathumansarenotawareofthe
identityoftheirpartnersduringtheinteraction.11
We then evaluate humans and
GPT-4’s interactions with GPT-
GOAL BEL REL KNO SEC SOC FIN
4 and human annotators as the GPT-4(wH) 4.85 9.25 0.70 2.80 0 0 0.50
evaluators. As shown in Table Human(wG) 5.95∗ 9.15 0.60 2.95 0 -0.60 0.70
3, humans perform significantly Human(wH) 6.15∗ 9.10 0.80 2.65 0 -0.10 0.45
better than GPT-4 in the GOAL
dimension. Table 3: Human and GPT-4 performance on different dimensions on
SOTOPIA-hard.SOCandSEChavethescaleof-10to0,RELandFIN
It is also worth noting that hu- havethescaleof-5to5,andothershavethescaleof0to10.(wH)in-
mans on average produce 16.8 dicatesthattheagentisinteractingwithhumans,while(wG)indicates
wordsperturn,whileGPT-4pro- thattheagentisinteractingwithGPT-4.*indicatesthedifferenceissig-
duces45.5wordsperturn,which nificantcomparedtoGPT-4(wH)withp<0.05understudent’st-test.
indicates humans are more ef- Wealsoreporttheagentsperformanceevaluatedbyhumanannotators
(TableG.4),whichshowssimilartrends.
ficient in social interactions.
Specifically, we find that GPT-4 always rephrases the utterance back at the other agent and then
answers, whichisacommunicationskillcalledactivelistening(HarryWeger&Robinson,2014),
whereashumanstypicallydirectlyanswer. ThisislikelyduetothefactthatGPT-4istrainedwitha
largeamountofhumanfeedback,whichmakesitoverlyhelpfulintheconversation.
Qualitatively,HumansareusuallymorestrategicthanGPT-4duringinteraction.Whenbargaining,if
theGPT-4agenthasabuyingtargetsetat$454,itsometimesstartsitsbidatthatexactprice(Figure
H.10). Consequently,anysubsequentnegotiationspushthefinalagreedpriceaboveitsinitialtarget.
Incontrast,humanannotators(e.g. FigureH.11)beginthenegotiationatalowerbidof$400,and
oftenreachesanagreementwiththeselleratapricethat’sstillbelowtheGPT-4’starget. Humans
arealsomorepersistentintheirgoals.Whentryingtosettleoneamusictolistento,themodeltends
toproposeacompromisedsolution(e.g. FigureH.12),suchaseachonelisteningtoafewselected
songs. Humans,however,tendtopersistinadheringtotheirsetgoals(e.g. FigureH.13).
11SeeAppendixFforthedetailedinstructionsandthechatinterface.
8

PublishedasaconferencepaperatICLR2024
8 RELATED WORK
Enablingartificialagentstointeractwitheachotherandwithhumanshasbeenstudiedindifferent
fields. Our work draws inspiration from literature on social intelligence, dialogue systems, and
simulationsofsocialinteractions. SeeAppendixAforanextendeddiscussion.
Static social intelligence benchmarks To evaluate social intelligence in AI systems, researchers
haveproposedavarietyofstaticbenchmarks. Someofthemareinspiredbyclinicaltestsofsocial
intelligenceforhumans,suchastheToMidataset(Leetal.,2019)andtheFauxPasdataset(Shapira
etal.,2023b). Otherbenchmarksaredesignedtoevaluatesocialintelligenceinthecontextofsocial
commonsensereasoning, suchasSocialIQA(Sapetal.,2019)andSocialIQ(Zadehetal.,2019a).
WiththerapiddevelopmentofLLMs,someofthebenchmarksgraduallybecomesaturated. Recent
workssynthesizeexistingbenchmarksandproposenewadversarialdatasetstoevaluatesocialintel-
ligence(Shapiraetal.,2023a;Wilfetal.,2023). Althoughthesebenchmarksareharderthantheir
predecessors, they still lack the dynamic nature of social interactions and the rich social context,
whichisdeemedinsufficientforevaluatingsocialintelligenceinAIsystems(Leeetal.,2023).
Task-oriented and open-domain dialogue systems Dialogue systems offer a natural interface to
interact with AI systems. Task-oriented dialogue systems are designed to help users accomplish
specifictasks,oftenevaluatedwithtasksuccessrateorusersatisfaction(Hosseini-Asletal.,2022;
FAIRetal.,2022;Wangetal.,2019)withoutgeneralizingtoothertasks.12 Open-domaindialogue
systems are designed to have “chit-chat” with users (Kann et al., 2022; Kim et al., 2023), often
incorporate personal information to make conversations more engaging (Zhang et al., 2018a; Liu
etal.,2020;Bahaetal.,2023;Dog˘ruo¨z&Skantze,2021;Skantze&Dog˘ruo¨z,2023). Suchsystems
oftenappeartounderstandthesubjectsdeeperthantheyactuallydowithoutaspecificgoalduring
theinteraction(Weizenbaum,1966,Elizaeffect). SOTOPIAforcesagentstomaintaintheirsocial
personaandachieveexplicitsocialgoalsspontaneously,whichismorechallengingthantheexisting
dialoguesystems.
SimulationsofsocialinteractionswithLLMsLLMscontainalargeamountofknowledgeabout
the world and can generate human-like responses based on the social context (Park et al., 2023;
Kim et al., 2023; West et al., 2022). Recently, researchers have used LLMs to simulate social in-
teractionsforvariouspurposes,suchasfacilitatingthedesignofsocialmediaplatform(Parketal.,
2022),producingbelievableproxiesofhumanbehaviors(Parketal.,2023),anddevelopingsoftware
collaboratively (Qian et al., 2023). However, these works focus on showcasing the capabilities of
LLMs in simulating social interactions rather than systematic evaluation of agents’ social interac-
tions. Specifically,Parketal.(2023)useTrueSkillratingtoevaluateagents’performanceinaspects
such as memorization, planning, and reflecting the past actions while ignoring other important di-
mensionssuchas SOCand SECduringsocialinteractions. CAMELLietal.(2023a)simulatesthe
collaborationtasksolvingprocessinLLMs,GentopiaXuetal.(2023)worksonaugmentedLLMs
withtoolstofacilitatecollaboration,whileChatDevQianetal.(2023)focusesonthesoftwarede-
velopmentdomain.
Multi-agentcoordinationAlthoughinpaperwefocusonevaluatinglanguageagents,ourresearch
is heavily-inspired by recent advances in multi-agent coordination and social learning Lowe et al.
(2017); McKee et al. (2020); Hu et al. (2020); Zhu et al. (2021); Liu et al. (2022); Trivedi et al.
(2023). Our setting is more realistic than the commonly-used assumptions that agents have either
zero(other-play)orextensiveknowledgeofeachother’spolicies(self-play).
9 CONCLUSION
In this paper, we present SOTOPIA, an environment that can be used to simulate the goal-driven
social interactions of agents in a variety of social scenarios. Different from most previous bench-
marks for social intelligence, SOTOPIA is interactive, goal-oriented, and covers a large range of
realistic social tasks. Our experiments demonstrate that GPT-4 could automate the evaluation of
agentperformancebasedonSOTOPIA-EVAL.Buildingonthis,weshowthatSOTOPIAcanused
for understanding not only the differences among models but also the difference between models
and humans in terms of social interaction abilities. We discuss the limitations of SOTOPIA and
future directions in Appendix B. Our findings indicate that SOTOPIA has potential as a platform
forassessingandenhancingthesocialskillsoflanguage-basedagents.
12Here,weconsiderabroaderconceptoftask-orienteddialoguesystemsincludingaction-takingabilities.
9

PublishedasaconferencepaperatICLR2024
REFERENCES
TarekAitBaha,MohamedElHajji,YoussefEs-saady,andHammouFadili. Thepowerofperson-
alization: A systematic review of personality-adaptive chatbots. SN Computer Science, 4:1–25,
2023. URLhttps://api.semanticscholar.org/CorpusID:261346287.
Daniel S Bernstein, Robert Givan, Neil Immerman, and Shlomo Zilberstein. The complexity of
decentralizedcontrolofmarkovdecisionprocesses. Mathematicsofoperationsresearch,27(4):
819–840,2002.
FedericoBianchi,PatrickJohnChia,MertYuksekgonul,JacopoTagliabue,DanJurafsky,andJames
Zou. Howwellcanllmsnegotiate? negotiationarenaplatformandanalysis,2024.
Tom Burns, Ewa Roszkowska, Ugo Corte, and Nora Machado des Johansson. Sociological game
theory: Agency, socialstructuresandinteractionprocesses. Optimum.StudiaEkonomiczne, pp.
187–199,012017. doi: 10.15290/ose.2017.05.89.13.
RolandBe´nabouandJeanTirole. Incentivesandprosocialbehavior. AmericanEconomicReview,
96(5):1652–1678, December 2006. doi: 10.1257/aer.96.5.1652. URL https://www.aeaweb.
org/articles?id=10.1257/aer.96.5.1652.
Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu, Wei Xue, Shanghang Zhang, Jie Fu, and
ZhiyuanLiu. Chateval: Towardsbetterllm-basedevaluatorsthroughmulti-agentdebate,2023.
MyraCheng, EsinDurmus, andDanJurafsky. Markedpersonas: Usingnaturallanguageprompts
to measure stereotypes in language models. In Proceedings of the 61st Annual Meeting of the
AssociationforComputationalLinguistics(Volume1: LongPapers),July2023a.
MyraCheng,TizianoPiccardi,andDiyiYang. CoMPosT:Characterizingandevaluatingcaricature
in LLM simulations. In Houda Bouamor, Juan Pino, and Kalika Bali (eds.), Proceedings of
the2023ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pp.10853–10875,
Singapore,December2023b.AssociationforComputationalLinguistics. doi:10.18653/v1/2023.
emnlp-main.669. URLhttps://aclanthology.org/2023.emnlp-main.669.
Jan Cieciuch and Eldad Davidov. A comparison of the invariance properties of the pvq-40 and
the pvq-21 to measure human values across german and polish samples. Survey Research
Methods, 6(1):37–48, Apr. 2012. doi: 10.18148/srm/2012.v6i1.5091. URL https://ojs.ub.
uni-konstanz.de/srm/article/view/5091.
Elisa De Stefani and Doriana De Marco. Language, gesture, and emotional communication: An
embodiedviewofsocialinteraction. Front.Psychol.,10:2063,September2019.
Hiroshi Deguchi. Multi agent economics and its gaming simulation. IFAC Proceed-
ings Volumes, 28(7):269–274, 1995. ISSN 1474-6670. doi: https://doi.org/10.1016/
S1474-6670(17)47121-7. URL https://www.sciencedirect.com/science/article/pii/
S1474667017471217. IFAC/IFIP/IFORS/SEDC Symposium on Modelling and Control of Na-
tionalandRegionalEconomies1995,GoldCoast,Queensland,Australia,2-5July1995.
MichaelDennis,NatashaJaques,EugeneVinitsky,AlexandreBayen,StuartRussell,AndrewCritch,
and Sergey Levine. Emergent complexity and zero-shot transfer via unsupervised environment
design. Advancesinneuralinformationprocessingsystems,33:13049–13061,2020.
Ameet Deshpande, Tanmay Rajpurohit, Karthik Narasimhan, and Ashwin Kalyan. Anthropomor-
phizationofai: Opportunitiesandrisks,2023.
A.SezaDog˘ruo¨zandGabrielSkantze. How“open”aretheconversationswithopen-domainchat-
bots? a proposal for speech event based evaluation. In Proceedings of the 22nd Annual Meet-
ing of the Special Interest Group on Discourse and Dialogue, pp. 392–402, Singapore and On-
line,July2021.AssociationforComputationalLinguistics. URLhttps://aclanthology.org/
2021.sigdial-1.41.
Radwan El Othman, Rola El Othman, Rabih Hallit, Sahar Obeid, and Souheil Hallit. Personality
traits,emotionalintelligenceanddecision-makingstylesinlebaneseuniversitiesmedicalstudents.
BMCpsychology,8:1–14,2020.
10

PublishedasaconferencepaperatICLR2024
MetaFundamentalAIResearchDiplomacyTeamFAIR,AntonBakhtin, NoamBrown, EmilyDi-
nan, Gabriele Farina, Colin Flaherty, Daniel Fried, Andrew Goff, Jonathan Gray, Hengyuan
Hu, Athul Paul Jacob, Mojtaba Komeili, Karthik Konath, Minae Kwon, Adam Lerer, Mike
Lewis, Alexander H. Miller, Sasha Mitts, Adithya Renduchintala, Stephen Roller, Dirk Rowe,
WeiyanShi,JoeSpisak,AlexanderWei,DavidWu,HughZhang,andMarkusZijlstra. Human-
level play in the game of ¡i¿diplomacy¡/i¿ by combining language models with strategic rea-
soning. Science, 378(6624):1067–1074, 2022. doi: 10.1126/science.ade9097. URL https:
//www.science.org/doi/abs/10.1126/science.ade9097.
Daniel C Feldman and Hugh J Arnold. Personality types and career patterns: Some empirical
evidence on holland’s model. Canadian Journal of Administrative Sciences/Revue Canadienne
desSciencesdel’Administration,2(1):192–210,1985.
Maxwell Forbes, Jena D. Hwang, Vered Shwartz, Maarten Sap, and Yejin Choi. Social chemistry
101:Learningtoreasonaboutsocialandmoralnorms. InProceedingsofthe2020Conferenceon
EmpiricalMethodsinNaturalLanguageProcessing(EMNLP),pp.653–670,Online,November
2020.AssociationforComputationalLinguistics. doi: 10.18653/v1/2020.emnlp-main.48. URL
https://aclanthology.org/2020.emnlp-main.48.
YaoFu, HaoPeng, TusharKhot, andMirellaLapata. Improvinglanguagemodelnegotiationwith
self-playandin-contextlearningfromaifeedback,2023.
Nigel Gilbert. Simulation for the Social Scientist. Open University Press, 2 edition, February
2005. URL https://www.amazon.com/Simulation-Social-Scientist-Nigel-Gilbert/
dp/0335216005.
Andrew Gilpin and Tuomas Sandholm. A competitive texas hold’em poker player via automated
abstractionandreal-timeequilibriumcomputation. InProceedingsofthe21stNationalConfer-
enceonArtificialIntelligence-Volume2, AAAI’06, pp.1007–1013.AAAIPress, 2006. ISBN
9781577352815.
Erving Goffman. The presentation of self in everyday life. Penguin Modern Classics. Penguin
Classics,London,England,May1959.
LewisRGoldberg. ThedevelopmentofmarkersfortheBig-Fivefactorstructure. Psychol.Assess.,
4(1):26–42,March1992.
Jesse Graham, Brian A Nosek, Jonathan Haidt, Ravi Iyer, Spassena Koleva, and Peter H Ditto.
Mappingthemoraldomain. J.Pers.Soc.Psychol.,101(2):366–385,August2011.
Katherine Hamilton, Shin-I Shih, and Susan Mohammed. The development and validation of the
rationalandintuitivedecisionstylesscale. J.Pers.Assess.,98(5):523–535,September2016.
Elizabeth M. Minei Harry Weger, Gina Castle Bell and Melissa C. Robinson. The relative effec-
tivenessofactivelisteningininitialinteractions. InternationalJournalofListening,28(1):13–31,
2014.
He He, Anusha Balakrishnan, Mihail Eric, and Percy Liang. Learning symmetric collaborative
dialogueagentswithdynamicknowledgegraphembeddings. InProceedingsofthe55thAnnual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 1766–
1776,Vancouver,Canada,July2017.AssociationforComputationalLinguistics. doi: 10.18653/
v1/P17-1162. URLhttps://aclanthology.org/P17-1162.
HeHe,DerekChen,AnushaBalakrishnan,andPercyLiang. Decouplingstrategyandgenerationin
negotiationdialogues. InProceedingsofthe2018ConferenceonEmpiricalMethodsinNatural
LanguageProcessing,pp.2333–2343,Brussels,Belgium,October-November2018.Association
for Computational Linguistics. doi: 10.18653/v1/D18-1256. URL https://aclanthology.
org/D18-1256.
SarahSusannaHoppler,RobinSegerer,andJanaNikitin.Thesixcomponentsofsocialinteractions:
actor, partner, relation, activities, context, and evaluation. Frontiers in Psychology, 12:743074,
2022.
11

PublishedasaconferencepaperatICLR2024
EhsanHosseini-Asl,BryanMcCann,Chien-ShengWu,SemihYavuz,andRichardSocher.Asimple
languagemodelfortask-orienteddialogue,2022.
Hengyuan Hu, Adam Lerer, Alex Peysakhovich, and Jakob Foerster. “Other-play” for zero-shot
coordination. In Hal Daume´ III and Aarti Singh (eds.), Proceedings of the 37th International
ConferenceonMachineLearning,volume119ofProceedingsofMachineLearningResearch,pp.
4399–4410. PMLR, 13–18 Jul 2020. URL https://proceedings.mlr.press/v119/hu20a.
html.
QingxuHuang, DawnCParker, TatianaFilatova, andShipengSun. Areviewofurbanresidential
choicemodelsusingAgent-Basedmodeling. Environmentandplanning.B,Planning&design,
41(4):661–689,August2014. URLhttps://doi.org/10.1068/b120043p.
Evan Hubinger, Carson Denison, Jesse Mu, Mike Lambert, Meg Tong, Monte MacDiarmid, Tam-
era Lanham, Daniel M. Ziegler, Tim Maxwell, Newton Cheng, Adam Jermyn, Amanda Askell,
Ansh Radhakrishnan, Cem Anil, David Duvenaud, Deep Ganguli, Fazl Barez, Jack Clark, Ka-
malNdousse,KshitijSachan,MichaelSellitto,MrinankSharma,NovaDasSarma,RogerGrosse,
Shauna Kravec, Yuntao Bai, Zachary Witten, Marina Favaro, Jan Brauner, Holden Karnofsky,
Paul Christiano, Samuel R. Bowman, Logan Graham, Jared Kaplan, So¨ren Mindermann, Ryan
Greenblatt,BuckShlegeris,NicholasSchiefer,andEthanPerez. Sleeperagents: Trainingdecep-
tivellmsthatpersistthroughsafetytraining,2024.
MarielaEJaffe´ andMariaDouneva. Secretiveandclose? howsharingsecretsmayimpactpercep-
tionsofdistance. PLoSOne,15(6):e0233953,June2020.
Adrianna C. Jenkins, Pierre Karashchuk, Lusha Zhu, and Ming Hsu. Predicting human behavior
toward members of different social groups. Proceedings of the National Academy of Sciences,
115(39):9696–9701,2018. doi:10.1073/pnas.1719452115. URLhttps://www.pnas.org/doi/
abs/10.1073/pnas.1719452115.
Hang Jiang, Xiajie Zhang, Xubo Cao, Cynthia Breazeal, Jad Kabbara, and Deb Roy. Personallm:
Investigatingtheabilityoflargelanguagemodelstoexpresspersonalitytraits.2023.URLhttps:
//api.semanticscholar.org/CorpusID:268032940.
Liwei Jiang, Jena D. Hwang, Chandra Bhagavatula, Ronan Le Bras, Jenny Liang, Jesse Dodge,
Keisuke Sakaguchi, Maxwell Forbes, Jon Borchardt, Saadia Gabriel, Yulia Tsvetkov, Oren Et-
zioni, Maarten Sap, Regina Rini, and Yejin Choi. Can machines learn morality? the delphi
experiment,2022.
Katharina Kann, Abteen Ebrahimi, Joewie Koh, Shiran Dudy, and Alessandro Roncone. Open-
domain dialogue generation: What we can do, cannot do, and should do next. In Proceed-
ings of the 4th Workshop on NLP for Conversational AI, pp. 148–165, Dublin, Ireland, May
2022.AssociationforComputationalLinguistics. doi: 10.18653/v1/2022.nlp4convai-1.13. URL
https://aclanthology.org/2022.nlp4convai-1.13.
JohnF.KihlstromandNancyCantor. SocialIntelligence,pp.756–779. CambridgeHandbooksin
Psychology.CambridgeUniversityPress,2edition,2020. doi: 10.1017/9781108770422.032.
HyunwooKim,JackHessel,LiweiJiang,PeterWest,XimingLu,YoungjaeYu,PeiZhou,RonanLe
Bras,MaliheAlikhani,GunheeKim,MaartenSap,andYejinChoi. Soda: Million-scaledialogue
distillationwithsocialcommonsensecontextualization,2023.
GrgurKovacˇ, Re´myPortelas, KatjaHofmann, andPierre-YvesOudeyer. Socialai: Benchmarking
socio-cognitiveabilitiesindeepreinforcementlearningagents,2021.
MatthewLe, Y-LanBoureau, andMaximilianNickel. Revisitingtheevaluationoftheoryofmind
through question answering. In Proceedings of the 2019 Conference on Empirical Methods in
Natural Language Processing and the 9th International Joint Conference on Natural Language
Processing(EMNLP-IJCNLP),pp.5872–5877,HongKong,China,November2019.Association
for Computational Linguistics. doi: 10.18653/v1/D19-1598. URL https://aclanthology.
org/D19-1598.
12

PublishedasaconferencepaperatICLR2024
MinaLee,MeghaSrivastava,AmeliaHardy,JohnThickstun,EsinDurmus,AshwinParanjape,Ines
Gerard-Ursin,XiangLisaLi,FaisalLadhak,FriedaRong,RoseEWang,MinaeKwon,JoonSung
Park,HanchengCao,TonyLee,RishiBommasani,MichaelS.Bernstein,andPercyLiang. Eval-
uating human-language model interaction. Transactions on Machine Learning Research, 2023.
ISSN2835-8856. URLhttps://openreview.net/forum?id=hjDYJUn9l1.
Mike Lewis, Denis Yarats, Yann Dauphin, Devi Parikh, and Dhruv Batra. Deal or no deal? end-
to-end learning of negotiation dialogues. In Proceedings of the 2017 Conference on Empirical
Methods in Natural Language Processing, pp. 2443–2453, Copenhagen, Denmark, September
2017. Association for Computational Linguistics. doi: 10.18653/v1/D17-1259. URL https:
//aclanthology.org/D17-1259.
GuohaoLi,HasanAbedAlKaderHammoud,HaniItani,DmitriiKhizbullin,andBernardGhanem.
Camel:Communicativeagentsfor”mind”explorationoflargelanguagemodelsociety.InThirty-
seventhConferenceonNeuralInformationProcessingSystems,2023a.
Xuechen Li, Tianyi Zhang, Yann Dubois, Rohan Taori, Ishaan Gulrajani, Carlos Guestrin, Percy
Liang,andTatsunoriB.Hashimoto. Alpacaeval: Anautomaticevaluatorofinstruction-following
models. https://github.com/tatsu-lab/alpaca eval,2023b.
PercyLiang,RishiBommasani,TonyLee,DimitrisTsipras,DilaraSoylu,MichihiroYasunaga,Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. Holistic evaluation of language
models. arXiv preprint arXiv:2211.09110, 2022. URL https://crfm.stanford.edu/helm/
latest/?group=core scenarios.
Weixin Liang, Mert Yuksekgonul, Yining Mao, Eric Wu, and James Zou. Gpt detectors are
biased against non-native english writers. Patterns, 4(7):100779, 2023. ISSN 2666-3899.
doi: https://doi.org/10.1016/j.patter.2023.100779. URL https://www.sciencedirect.com/
science/article/pii/S2666389923001307.
Andy Liu, Hao Zhu, Emmy Liu, Yonatan Bisk, and Graham Neubig. Computational language
acquisition with theory of mind. In The Eleventh International Conference on Learning Repre-
sentations,2022.
QianLiu, YihongChen, B.Chen, Jian-GuangLou,ZixuanChen,BinZhou,andDongmeiZhang.
Youimpressme: Dialoguegenerationviamutualpersonaperception. InAnnualMeetingofthe
AssociationforComputationalLinguistics, 2020. URLhttps://api.semanticscholar.org/
CorpusID:215745354.
RyanLiu,HowardYen,RajaMarjieh,ThomasL.Griffiths,andRanjayKrishna. Improvinginter-
personalcommunicationbysimulatingaudienceswithlanguagemodels. ArXiv,abs/2311.00687,
2023. URLhttps://api.semanticscholar.org/CorpusID:264832770.
Ryan Lowe, Yi I Wu, Aviv Tamar, Jean Harb, OpenAI Pieter Abbeel, and Igor Mordatch. Multi-
agentactor-criticformixedcooperative-competitiveenvironments. Advancesinneuralinforma-
tionprocessingsystems,30,2017.
Zheheng Luo, Qianqian Xie, and Sophia Ananiadou. Chatgpt as a factual inconsistency evaluator
fortextsummarization,2023.
AHMaslow. Atheoryofhumanmotivation. Psychol.Rev.,50(4):370–396,July1943.
Kevin R McKee, Ian Gemp, Brian McWilliams, Edgar A Due´n˜ez-Guzma´n, Edward Hughes, and
Joel Z Leibo. Social diversity and social preferences in mixed-motive reinforcement learning.
arXivpreprintarXiv:2002.02325,2020.
ShikibMehri,YulanFeng,CarlaGordon,SeyedHosseinAlavi,DavidTraum,andMaxineEskenazi.
Interactive evaluation of dialog track at DSTC9. In Proceedings of the Thirteenth Language
ResourcesandEvaluationConference, pp.5731–5738, Marseille, France, June2022.European
LanguageResourcesAssociation. URLhttps://aclanthology.org/2022.lrec-1.616.
Julian Michael, Salsabila Mahdi, David Rein, Jackson Petty, Julien Dirani, Vishakh Padmakumar,
andSamuelR.Bowman. Debatehelpssuperviseunreliableexperts,2023.
13

PublishedasaconferencepaperatICLR2024
TheMosaicMLNLPTeam,2023. URLhttps://www.mosaicml.com/blog/mpt-30b.
RanjitNair,MilindTambe,MakotoYokoo,DavidPynadath,andStacyMarsella. Tamingdecentral-
izedpomdps: Towardsefficientpolicycomputationformultiagentsettings. InIJCAI,volume3,
pp.705–711,2003.
Victor Vikram Odouard and Michael Holton Price. Tit for tattling: Cooperation, communication,
and how each could stabilize the other. Evolution and Human Behavior, 44(4):359–372, 2023.
ISSN1090-5138.doi:https://doi.org/10.1016/j.evolhumbehav.2023.06.002.URLhttps://www.
sciencedirect.com/science/article/pii/S1090513823000557.
OpenAI. Gpt-4technicalreport,2023.
LongOuyang,JeffWu,XuJiang,DiogoAlmeida,CarrollL.Wainwright,PamelaMishkin,Chong
Zhang,SandhiniAgarwal,KatarinaSlama,AlexRay,JohnSchulman,JacobHilton,FraserKel-
ton, Luke Miller, Maddie Simens, Amanda Askell, Peter Welinder, Paul Christiano, Jan Leike,
andRyanLowe. Traininglanguagemodelstofollowinstructionswithhumanfeedback,2022.
AishwaryaPadmakumar,JesseThomason,AyushShrivastava,PatrickLange,AnjaliNarayan-Chen,
SpandanaGella,RobinsonPiramuthu,GokhanTur,andDilekHakkani-Tur. Teach: Task-driven
embodied agents that chat. In Proceedings of the AAAI Conference on Artificial Intelligence,
volume36,pp.2017–2025,2022.
Joon Sung Park, Lindsay Popowski, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and
Michael S. Bernstein. Social simulacra: Creating populated prototypes for social computing
systems. In In the 35th Annual ACM Symposium on User Interface Software and Technology
(UIST’22),UIST’22,NewYork,NY,USA,2022.AssociationforComputingMachinery. ISBN
9781450393201. doi: 10.1145/3526113.3545616. URLhttps://doi.org/10.1145/3526113.
3545616.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and
Michael S. Bernstein. Generative agents: Interactive simulacra of human behavior. In In the
36thAnnualACMSymposiumonUserInterfaceSoftwareandTechnology(UIST’23),UIST’23,
NewYork,NY,USA,2023.AssociationforComputingMachinery.
DavidPremackandGuyWoodruff. Doesthechimpanzeehaveatheoryofmind? Behavioraland
BrainSciences,1(4):515–526,1978. doi: 10.1017/S0140525X00076512.
Chen Qian, Xin Cong, Wei Liu, Cheng Yang, Weize Chen, Yusheng Su, Yufan Dang, Jiahao Li,
Juyuan Xu, Dahai Li, Zhiyuan Liu, and Maosong Sun. Communicative agents for software de-
velopment,2023.
Justus J Randolph. Free-Marginal multirater kappa (multirater k[free]): An alternative to fleiss’
Fixed-Marginalmultiraterkappa. InProceedingsofJLIS,2005. URLhttps://eric.ed.gov/
?id=ED490661.
Sumedh Rasal. Llm harmony: Multi-agent communication for problem solving. ArXiv,
abs/2401.01312,2024. URLhttps://api.semanticscholar.org/CorpusID:266725580.
Steven Reiss. Multifaceted nature of intrinsic motivation: The theory of 16 basic desires. Review
of General Psychology, 8(3):179–193, 2004. doi: 10.1037/1089-2680.8.3.179. URL https:
//doi.org/10.1037/1089-2680.8.3.179.
CarolynRose´,Yi-ChiaWang,YueCui,JaimeArguello,KarstenStegmann,ArminWeinberger,and
FrankFischer.Analyzingcollaborativelearningprocessesautomatically:Exploitingtheadvances
ofcomputationallinguisticsincomputer-supportedcollaborativelearning. InternationalJournal
of Computer-Supported Collaborative Learning, 3(3):237–271, 2008. ISSN 1556-1615. doi:
10.1007/s11412-007-9034-0. URLhttps://doi.org/10.1007/s11412-007-9034-0.
Maarten Sap, Hannah Rashkin, Derek Chen, Ronan Le Bras, and Yejin Choi. Social IQa: Com-
monsense reasoning about social interactions. In Proceedings of the 2019 Conference on Em-
piricalMethodsinNaturalLanguageProcessingandthe9thInternationalJointConferenceon
Natural Language Processing (EMNLP-IJCNLP), pp. 4463–4473, Hong Kong, China, Novem-
ber 2019. Association for Computational Linguistics. doi: 10.18653/v1/D19-1454. URL
https://aclanthology.org/D19-1454.
14

PublishedasaconferencepaperatICLR2024
R.KeithSawyer. SocialEmergence: SocietiesAsComplexSystems. CambridgeUniversityPress,
2005.
Murray Shanahan, Kyle McDonell, and Laria Reynolds. Role-play with large language models,
2023.
YunfanShao,LinyangLi,JunqiDai,andXipengQiu. Character-LLM:Atrainableagentforrole-
playing. InHoudaBouamor,JuanPino,andKalikaBali(eds.),Proceedingsofthe2023Confer-
enceonEmpiricalMethodsinNaturalLanguageProcessing,pp.13153–13187,Singapore,De-
cember 2023. Association for Computational Linguistics. URL https://aclanthology.org/
2023.emnlp-main.814.
Natalie Shapira, Mosh Levy, Hossein Seyed Alavi, Xuhui Zhou, Yejin Choi, Yoav Goldberg,
Maarten Sap, and Vered Shwartz. Clever hans or neural theory of mind? stress testing social
reasoninginlargelanguagemodels.arXiv,2023a.URLhttps://arxiv.org/abs/2305.14763.
NatalieShapira, GuyZwirn, andYoavGoldberg. Howwelldolargelanguagemodelsperformon
faux pas tests? In Findings of the Association for Computational Linguistics: ACL 2023, pp.
10438–10451, Toronto, Canada, July 2023b. Association for Computational Linguistics. doi:
10.18653/v1/2023.findings-acl.663. URL https://aclanthology.org/2023.findings-acl.
663.
Gabriel Skantze and A. Seza Dog˘ruo¨z. The open-domain paradox for chatbots: Common ground
asthebasisforhuman-likedialogue. InProceedingsofthe24thMeetingoftheSpecialInterest
GrouponDiscourseandDialogue,pp.605–614,Prague,Czechia,September2023.Association
forComputationalLinguistics. URLhttps://aclanthology.org/2023.sigdial-1.57.
Swabha Swayamdipta, Roy Schwartz, Nicholas Lourie, Yizhong Wang, Hannaneh Hajishirzi,
Noah A. Smith, and Yejin Choi. Dataset cartography: Mapping and diagnosing datasets with
training dynamics. In Proceedings of the 2020 Conference on Empirical Methods in Natural
LanguageProcessing(EMNLP),pp.9275–9293,Online,November2020.AssociationforCom-
putationalLinguistics. doi: 10.18653/v1/2020.emnlp-main.746. URLhttps://aclanthology.
org/2020.emnlp-main.746.
LeighTesfatsionandKennethLJudd. HandbookofComputationalEconomics: Agent-BasedCom-
putational Economics. Elsevier, May 2006. URL https://play.google.com/store/books/
details?id=Na5J44IBaHkC.
FelippeToledoandFraserCarson.Neurocircuitryofpersonalitytraitsandintentindecision-making.
BehavioralSciences,13(5):351,2023.
MichaelTomasello. BecomingHuman: ATheoryofOntogeny. BelknapPress,2021.
HugoTouvron,LouisMartin,KevinStone,PeterAlbert,AmjadAlmahairi,YasmineBabaei,Niko-
lay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, Dan Bikel, Lukas Blecher,
Cristian Canton Ferrer, Moya Chen, Guillem Cucurull, David Esiobu, Jude Fernandes, Jeremy
Fu,WenyinFu,BrianFuller,CynthiaGao,VedanujGoswami,NamanGoyal,AnthonyHartshorn,
Saghar Hosseini, Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel
Kloumann,ArtemKorenev,PunitSinghKoura,Marie-AnneLachaux,ThibautLavril,JenyaLee,
Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet, Todor Mihaylov, Pushkar Mishra,
Igor Molybog, Yixin Nie, Andrew Poulton, Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi,
AlanSchelten,RuanSilva,EricMichaelSmith,RanjanSubramanian,XiaoqingEllenTan,Binh
Tang,RossTaylor,AdinaWilliams,JianXiangKuan,PuxinXu,ZhengYan,IliyanZarov,Yuchen
Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Rodriguez, Robert Stojnic,
Sergey Edunov, and Thomas Scialom. Llama 2: Open foundation and fine-tuned chat models,
2023.
RakshitTrivedi,AkbirKhan,JesseClifton,LewisHammond,JoelLeibo,EdgarDuenez-Guzman,
JohnAgapiou,JaydMatyas,andDylanHadfield-Menell.Meltingpotcontest,2023.URLhttps:
//www.aicrowd.com/challenges/meltingpot-challenge-2023.
TomerUllman. Largelanguagemodelsfailontrivialalterationstotheory-of-mindtasks,2023.
15

PublishedasaconferencepaperatICLR2024
JackUrbanek,AngelaFan,SiddharthKaramcheti,SaachiJain,SamuelHumeau,EmilyDinan,Tim
Rockta¨schel, Douwe Kiela, Arthur Szlam, and Jason Weston. Learning to speak and act in a
fantasy text adventure game. In Proceedings of the 2019 Conference on Empirical Methods in
Natural Language Processing and the 9th International Joint Conference on Natural Language
Processing (EMNLP-IJCNLP), pp. 673–683, Hong Kong, China, November 2019. Association
for Computational Linguistics. doi: 10.18653/v1/D19-1062. URL https://aclanthology.
org/D19-1062.
Peiyi Wang, Lei Li, Liang Chen, Dawei Zhu, Binghuai Lin, Yunbo Cao, Qi Liu, Tianyu Liu, and
Zhifang Sui. Large language models are not fair evaluators. arXiv preprint arXiv:2305.17926,
2023.
XueweiWang, WeiyanShi, RichardKim, YoojungOh, SijiaYang, JingwenZhang, andZhouYu.
Persuasion for good: Towards a personalized persuasive dialogue system for social good. In
Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, pp.
5635–5649,Florence,Italy,July2019.AssociationforComputationalLinguistics.doi:10.18653/
v1/P19-1566. URLhttps://aclanthology.org/P19-1566.
Max Weber. The Nature of Social Action, pp. 7–32. Cambridge University Press, 1978. doi:
10.1017/CBO9780511810831.005. URL https://classicalsociologicaltheory.files.
wordpress.com/2016/06/max-weber-classical-sociological-theory.pdf.
JasonWei,XuezhiWang,DaleSchuurmans,MaartenBosma,FeiXia,EdChi,QuocVLe,Denny
Zhou,etal. Chain-of-thoughtpromptingelicitsreasoninginlargelanguagemodels. Advancesin
NeuralInformationProcessingSystems,35:24824–24837,2022.
JosephWeizenbaum. Eliza—acomputerprogramforthestudyofnaturallanguagecommunication
between man and machine. Commun. ACM, 9(1):36–45, jan 1966. ISSN 0001-0782. doi: 10.
1145/365153.365168. URLhttps://doi.org/10.1145/365153.365168.
PeterWest,ChandraBhagavatula,JackHessel,JenaHwang,LiweiJiang,RonanLeBras,Ximing
Lu, Sean Welleck, and Yejin Choi. Symbolic knowledge distillation: from general language
modelstocommonsensemodels. InProceedingsofthe2022ConferenceoftheNorthAmerican
Chapter of the Association for Computational Linguistics: Human Language Technologies, pp.
4602–4625,Seattle,UnitedStates,July2022.AssociationforComputationalLinguistics.doi:10.
18653/v1/2022.naacl-main.341. URLhttps://aclanthology.org/2022.naacl-main.341.
Alex Wilf, Leena Mathur, Sheryl Mathew, Claire Ko, Youssouf Kebe, Paul Pu Liang, and Louis-
Philippe Morency. Social-iq 2.0 challenge: Benchmarking multimodal social understanding.
https://github.com/abwilf/Social-IQ-2.0-Challenge,2023.
ChengxingXie,CanyuChen,FeiranJia,ZiyuYe,KaiShu,AdelBibi,ZiniuHu,PhilipTorr,Bernard
Ghanem, andG.Li. Canlargelanguagemodelagentssimulatehumantrustbehaviors? ArXiv,
abs/2402.04559,2024. URLhttps://api.semanticscholar.org/CorpusID:267523076.
BinfengXu,XukunLiu,HuaShen,ZeyuHan,YuhanLi,MurongYue,ZhiyuanPeng,YuchenLiu,
ZiyuYao,andDongkuanXu. Gentopia:Acollaborativeplatformfortool-augmentedllms. arXiv
preprintarXiv:2308.04030,2023.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R Narasimhan, and Yuan
Cao. React: Synergizingreasoningandactinginlanguagemodels. InTheEleventhInternational
ConferenceonLearningRepresentations,2022.
AmirZadeh,MichaelChan,PaulPuLiang,EdmundTong,andLouis-PhilippeMorency. Social-iq:
Aquestionansweringbenchmarkforartificialsocialintelligence. In2019IEEE/CVFConference
on Computer Vision and Pattern Recognition (CVPR), pp. 8799–8809, 2019a. doi: 10.1109/
CVPR.2019.00901.
Amir Zadeh, Michael Chan, Paul Pu Liang, Edmund Tong, and Louis-Philippe Morency. Social-
iq: A question answering benchmark for artificial social intelligence. In Proceedings of the
IEEE/CVFConferenceonComputerVisionandPatternRecognition,pp.8807–8817,2019b.
16

PublishedasaconferencepaperatICLR2024
Jintian Zhang, Xin Xu, Ningyu Zhang, Ruibo Liu, Bryan Hooi, and Shumin Deng. Exploring
collaborationmechanismsforllmagents: Asocialpsychologyview,2024.
SaizhengZhang,EmilyDinan,JackUrbanek,ArthurSzlam,DouweKiela,andJasonWeston. Per-
sonalizing dialogue agents: I have a dog, do you have pets too? In Proceedings of the 56th
AnnualMeetingoftheAssociationforComputationalLinguistics(Volume1: LongPapers), pp.
2204–2213, Melbourne, Australia, July 2018a. Association for Computational Linguistics. doi:
10.18653/v1/P18-1205. URLhttps://aclanthology.org/P18-1205.
SaizhengZhang,EmilyDinan,JackUrbanek,ArthurSzlam,DouweKiela,andJasonWeston. Per-
sonalizingdialogueagents:Ihaveadog,doyouhavepetstoo? arXivpreprintarXiv:1801.07243,
2018b.
Xinghua Zhang, Bowen Yu, Haiyang Yu, Yangyu Lv, Tingwen Liu, Fei Huang, Hongbo Xu,
and Yongbin Li. Wider and deeper llm networks are fairer llm evaluators. arXiv preprint
arXiv:2308.01862,2023.
QinlinZhao,JindongWang,YixuanZhang,YiqiaoJin,KaijieZhu,HaoChen,andXingXie. Com-
peteai: Understandingthecompetitionbehaviorsinlargelanguagemodel-basedagents,2023.
Xuhui Zhou, Maarten Sap, Swabha Swayamdipta, Yejin Choi, and Noah A. Smith. Challenges in
automateddebiasingfortoxiclanguagedetection. InEACL,2021.
XuhuiZhou,ZheSu,TiwalayoEisape,HyunwooKim,andMaartenSap. Isthisthereallife? isthis
justfantasy? themisleadingsuccessofsimulatingsocialinteractionswithllms,2024.
HaoZhu,GrahamNeubig,andYonatanBisk. Few-shotlanguagecoordinationbymodelingtheory
ofmind. InInternationalConferenceonMachineLearning,pp.12901–12911.PMLR,2021.
CalebZiems,JaneDwivedi-Yu,Yi-ChiaWang,AlonHalevy,andDiyiYang. NormBank: Aknowl-
edgebankofsituationalsocialnorms. InProceedingsofthe61stAnnualMeetingoftheAssoci-
ationforComputationalLinguistics(Volume1: LongPapers),pp.7756–7776,Toronto,Canada,
July2023.AssociationforComputationalLinguistics.doi:10.18653/v1/2023.acl-long.429.URL
https://aclanthology.org/2023.acl-long.429.
17

PublishedasaconferencepaperatICLR2024
CONTENT OF APPENDIX
Inthispaper,weintroduceSOTOPIAtoencourageresearchoninteractivesocialintelligence. We
showedthatSOTOPIAcanbeusedforevaluatingsocialinteractionamongmodelsandhumans. In
theappendix,weprovidethefollowingitemsthatshedfurtherinsightintothesecontributions:
A Extendedrelatedwork;
B ThelimitationsofSOTOPIAandfuturedirections;
C formaldefinitionofSOTOPIAfromamulti-agentreinforcementlearningperspectiveand
technicaldetailsofgeneratingsocialtasks;
D thepromptweuseforGPT-4(OpenAI,2023)toevaluatemodelperformance;
E TheAmazonMechanicTurkinterfaceforevaluatingmodelperformance;
F Theprocedureandinterfaceforhumans13whenplayingcharactersinSOTOPIA;
G Additionalquantitativeresults;
H Additionalqualitativeexamples.
A EXTENDED RELATED WORK
There have been a lot of social science works that have done agent-based modeling to study hu-
maninteractions, spanningacrossvariousdomainssuchaseconomics, phychology, andeducation
(Sawyer,2005;Rose´etal.,2008;Deguchi,1995). Priorsimulationenvironmentshaveplayedapiv-
otalroleinconstructingtheoriesandgeneratinghypothesesinthesefields.However,theyfrequently
constrainagents’communicativecapacitiestoartificiallanguagesandpresentahighlyreductionist
view of simulated human behavior (Gilbert, 2005; Tesfatsion & Judd, 2006; Huang et al., 2014;
Kovacˇ et al., 2021; Urbanek et al., 2019). LLMs provide a more flexible and expressive way to
modelhumanbehavior. Here,weincludeamoredetaileddiscussionoftherecentworksinvestigat-
ingLLMsforsimulatinghumansocialinteractions. Thereareworksthatfocusoninvestigatingthe
fidelityofLLMsinkeepingthedesignatedpersonaandexperiencesofthecharacters(Shaoetal.,
2023;Jiangetal.,2023). Thereareworksthatsimulatehumansocialinteractionsfocusingoncer-
tain aspects such as competition, collaboration, negotiation, deception, problem-sovling and etc.,
(Zhangetal.,2024;Zhaoetal.,2023;Liuetal.,2023;Michaeletal.,2023;Rasal,2024;Hubinger
etal.,2024;Bianchietal.,2024;Xieetal.,2024;Jiangetal.,2023). AsLLMsarebecomingmore
andmorepopularinsimulatinghumansocialinteractions,therearealsoworksthatfocusoninves-
tigatingthepotentialissuesandchallengesofusingLLMsinsocialsimulations,suchasstereotypes
andreportingissues(Chengetal.,2023b;Zhouetal.,2024).
B LIMITATIONS & FUTURE DIRECTIONS
We identify SOTOPIA as the first platform for a general and realistic evaluation of social intelli-
genceinAIagents.TobetterunderstandthesocialintelligenceofAIagents,wediscusssomefuture
directionsforSOTOPIAandthefieldofAIsocialintelligence.
Limitations of the simplified simulated “world” As every simulation is a simplification of the
real world, SOTOPIA identifies several key components of realistic social interactions, while ab-
stractingaspectsoftherealworld.First,weconsiderfivetypesofsocialrelationshipsinSOTOPIA.
Future work could expand the type and granularity of social relationships (e.g., colleagues, class-
mates,etc.) inSOTOPIA.Differenttypesofrelationshipswouldrequireagentstoexhibitdifferent
socialbehaviors(Jenkinsetal.,2018),makingtheexpansionofrelationshiptypesanimportantfu-
ture research direction. Second, future work could expand the breadth of the character and social
scenariopoolinSOTOPIAtocovermoresocialbehaviors. Third, SOTOPIAconstrainsthefixed
turn-takinginteractiontothedyadiccontext,studyinginteractionsbetweentwoagents.Futureworks
couldtacklemorecomplexsocialinteractions,suchasmulti-partyinteractionsandthoseinvolving
complexdynamics(e.g. asynchronousinteractions,interruptions).
13AllthehumansubjectsexperimentsareapprovedbytheInstitutionalReviewBoard(IRB)attheauthors’
institution.
18

PublishedasaconferencepaperatICLR2024
Socialimpactandethicalconsiderations AttributinghumancharacteristicstoAIsystemsrisks
anthropomorphizing them, which could lead to unrealistic expectations of AI systems, potential
manipulation, and negative influence (Deshpande et al., 2023). AI agents in SOTOPIA are not
dedicatedtoaconsistenthumanidentitybutratherrole-playvariouscharactersacrossdifferentsce-
narios.Thisrole-playingsettingdiscouragesAIsystemswithconsistenthumanpersonalities,which
couldleadtoanthropomorphism(Shanahanetal.,2023). ThemaingoalofSOTOPIAistoevaluate
thesocialintelligenceofAIagents,andwedonotintendtocreateAIagentsthatareindistinguish-
ablefromhumans. WeconsidertheinteractionsthathappenedinSOTOPIAassimulacraofhuman
interactionsandsuchsimulatedinteractionscouldhelpusbetterunderstandthesocialintelligence
ofAIagents,andexplorevarioussocialphenomena(Parketal.,2023).
PotentialsocialstereotypesthatareembeddedintheautomatedevaluationsysteminSOTOPIA,as
it is majorly supported by GPT-4 (Cheng et al., 2023a). Future work could investigate when such
biasesemerge,howtheyaffecttheevaluation,andhowtomitigatethem.Identifyingpotentialbiases
inSOTOPIAcouldalsohelpscientistsbetterunderstandsocialbiasesintherealworld(Zhouetal.,
2021). Futureworkcouldalsoextendtheevaluatorwithothersystems,forexample,Delphi(Jiang
etal.,2022). MitigatingbiasesandstereotypesininteractiveSOTOPIA-likesystemscouldsupport
thedevelopmentofsocialAIagentsthataremorefairandinclusive.
Meanwhile, models learn to persuade or negotiate with humans, which may lead to social manip-
ulation. We do not endorse the use of SOTOPIA to create manipulative agents and will release
SOTOPIAundertheAI2impactlicense14 topreventmisuse. Futureworkcouldfurtherinvestigate
the potential risks of AI anthropomorphism and manipulation and design more robust evaluation
systemstomitigatetheseriskswithSOTOPIA.
Improving LLM social intelligence Our SOTOPIA environment and SOTOPIA-EVAL frame-
workprovidetheopportunityforresearcherstotrainmoresociallyintelligentlanguageagents. As
showninsection5,GPT-4isabletoprovidereasonableevaluationsforsocialinteractionsevenfor
interactionsinvolvinghumans. Futureworkcouldexploreusingtheautomatedevaluationsystemto
providerewardstotrainLLMswithenhancedsocialintelligence.
C FORMAL DEFINITIONS AND TECHNICAL DETAILS
C.1 FORMALFORMULATIONOFTHETASKSIN SOTOPIA
WeformulatesocialinteractionsinSOTOPIAasmixed-motiveMarkovgames. AnN-agentDec-
POMDPframeworkBernsteinetal.(2002);Nairetal.(2003)includesastatespace,anactionspace,
anobservationspace,atransitionfunction,anobservationfunction,andarewardfunction.Wemake
two major extensions: (a) the reward function gives vector rewards in M social dimensions to N
agents(introducedin§3),and(b)aprocedurallygeneratedtaskspace(§2.1,§C.2).Thestatespacein
SOTOPIAincludesboththetaskandtheinteractionhistoryinthecurrentepisode.Theactionspace
includesfivetypesofactions:speakanutterance,non-verbal communication,physical action,
andtwospecialnone(indicatingnoactionatthistimestep)andleaveactions(nomoreactionis
permittedafterleaving). Eachtypeofaction,exceptforspecialactions,issupplementedbyapiece
offreetextindicatingthecontentoftheaction.Forexample,alegalactioncouldbespeak("Hello,
Bob!"),non-verbal communication("smile and nod"),orphysical action("call 911").
Thestateisalmostfullyobservableexceptfortheotheragents’socialgoalsandcharacterprofiles
whichwillbedetailedin§2.1. Weconsiderasimplestatetransitionfunctionthatdeterministically
maintainstheinteractionhistorybyaddingnewactionsateachtimestep.
Despite that turn-taking and timing response is an important aspects of social skills, we consider
thecasewheretheagentstaketurnstoactinround-robinorder,i.e. agentionlyactattimestept
whent i mod N. Foralongenoughhorizon,thisgeneralizestoanyconversationwithproper
≡
turn-taking. Inourexperiments,weonlyconsiderN = 2cases,whiletheenvironmentisdesigned
tosupportanyN 2cases.
≥
14https://allenai.org/impact-license
19

PublishedasaconferencepaperatICLR2024
C.2 TASKSPACETECHNICALDETAILS
C.2.1 CHARACTERS
The name, gender, age, occupation, and pronouns are in free text format, while the formats of
personality traits, moral values, and personal values are lists of pre-defined types. However, these
attributesareoftennotindependentwithdifferentlevelsofcorrelationandcomplicatedmechanisms.
(Feldman&Arnold,1985;ElOthmanetal.,2020;Toledo&Carson,2023)However,understand-
ing the relationship between these attributes is beyond the scope of this paper. We leverage the
commonsenseknowledgeinGPT-4togeneratetheseprofileswiththefollowingprompt:
Please generate a list of N fictional characters, one line per
character. Each with their attributes: <attribute 1> <attribute 1
format > <attribute 2> <attribute 2 format>...”
The personality trait types are “openness to experience”, “conscientiousness”, “extraversion”,
“agreeableness”and“neuroticism”(Goldberg,1992). Themoralvaluetypesare“care”,“fairness”,
“loyalty”,“authority”and“purity”(Cieciuch&Davidov,2012). TheSchwartzpersonalvaluetypes
are “self-direction”, “simulation”, “hedonism”, “achievement”, “power”, “security”, “conformity”,
“tradition”,“benevolence”,and“universalism”Cieciuch&Davidov(2012). Thedecision-making
styletypesare“directive”, “analytical”, “conceptual”, and“behavioral”. Aspreviouslystudiedin
Wangetal.(2019),thesecharacteristicsallaffectthebehaviorsinstrategicconversations.
Togivetheconversationsmorebackground,aftergeneratingtheaboveattributes,wepromptGPT-4
with”asecretthatthischaracterdoesn’twantanyoneelsetoknowandapieceofpublicinformation
thatotherpeopleknowaboutthem”togeneratethesecretandpublicinformation. Theauthorsfix
asmallproportionofprofilesthatarenotrealisticornotconsistentwithintheprofile(e.g., gender
nonbinarybutwithpronounsashe/him). Thecharacterprofilesthatwillusedinrole-playingare20
men,18women,and2nonbinarycharactersagedfrom21to63.
RELATIONSHIPS
To generate relationships, except for strangers, we randomly sampled 90 pairs of characters and
promptedGPT-4withtheirrelationships:
Please generate a fictional relationship with a background story 15 between
two agents based on the following agents’ profiles. <agent profile 1>,
<agent profile 2> ... The acceptable relationships are: family, friend,
romantic, and acquaintance.
Then,wemanuallycheckandcorrectthegeneratedrelationshipstoensurequality.Thisresultsin31
pairsoffamily,30pairsoffriends,30pairsofromanticpartners,and29pairsofacquaintances. For
strangers,werandomlysampledanother30pairsthatdonotbelongtoanyoftheabovecategories.
Itshouldbenotedthatgeneratingrelationshipsrequireshumaninterventiontomakesuretheyare
consistentwithboththecharacterprofilesandotherrelationships. Futureresearchcouldexplorethe
methodstogeneraterealisticrelationshipswithinhumancommunities.
SCENARIOS
To generate scenarios, we propose two methods to generate the scenario context and social goals.
The first method is first asking GPT-4 to refine a vignette from an existing dataset, then manually
inspectingthefeasibilityandrealisticityofthetasks.
Please generate scenarios and goals based on the examples below as well as
the inspirational prompt, when creating the goals, try to find one point
that both sides may not agree upon initially and need to collaboratively
resolve it. Inspirational prompt: <the selected vignette>
Specifically,weselect20vignettesfromSocialChemistry(Forbesetal.,2020),20fromSocialIQa
(Sapetal.,2019),10fromDeal-or-no-Deal(Lewisetal.,2017),and10vignettesfromNormbank
(Ziemsetal.,2023)togenerate60scenariosfocusingongeneraldaily-lifesocialinteractions.
15Wedon’tusethebackgroundstoryinourexperiments.
20

PublishedasaconferencepaperatICLR2024
Thesecondmethodistogeneratemoredetailswithtemplatesforthevignettestomakethemmore
realistic.Forexample,hereisthepromptforconvertingCraigslistBargins(Heetal.,2018)vignettes
intoscenariocontext:
The following sentence is automatically generated with the following
template: "One person is selling <item> for <price>, and another person
is trying to buy it." Here is the description of the item: "<description>.
with item = <title>, price=<price>, and description=<description>" Please
make the sentence fluent and natural.
wherethe<item>,<title>,and<price>arefromthedatainCraigslistBargins(Heetal.,2018).
Thegoalsaregeneratedwiththefollowingprompt:
The following sentence is automatically generated with the following
template: "You want to <role> this item. Your target price is $<price>
(round up to two decimals). You will get a penalty if you sell or buy
it for a price that is significantly lower than (if <role> is seller) or
significantly higher than (if <role> is buyer) the target price, but will
get a bonus if you successfully sell it higher than the target price (if
<role> is seller) or buy it for lower than the target price (if <role> is
buyer)" with role = <role> and price = <price>. Please make the sentence
fluent and natural. Do not change the original meaning of the sentence.
where<role>couldbea“buyer”ora“seller”,thebuyer’starget<price>isfromCraigslistBargins
(He et al., 2018), and the seller’s <price> is generated by first sample a markup ratio from an
exponential distribution with rate parameter 0.5, then divide the price in the scenario context with
(1+markupratio). AsimilarprocessisalsodoneforMutualFriends(Heetal.,2017). Thisresults
in30scenariosfromCraigslistBargins(Heetal.,2018)andMutualFriends(Heetal.,2017). This
methodcontrolsthegeneratedscenariosmuchbetterthanthefirstmethod,resultinginlittlepost-hoc
manualedits,butrequirescustomizedpromptsforeachdataset.
D INSTRUCTIONS FOR SOTOPIA-EVAL
We use the the same set of instructions for both GPT-4 (OpenAI, 2023) and humans when evalu-
atingepisodesinSOTOPIA.Intheseinstructions,weprovideexplanationforeachdimension,the
requirementsforreasoning,andtherangesofscoresonecouldgive.
BEL
Reasoning requirement: 1. Evaluate if the agent interacts with
others in a natural and realistic manner (here are a few common
questions to check: a. whether the agent is confusing with its own
identity? b. whether the agent repeats others’ words/actions
without any reason? c. whether the agent is being overly
polite considering the context?). Start the analysis with tag
<naturalness> 2. Analyze whether the actions of the agent align
with their character traits (e.g., personality, values, and etc.).
Start the analysis with tag <consistency>. Output your reasoning
process to the ‘reasoning’ field. Output an integer score ranging
from 0 and 10 in the ’score’ field. A higher score indicates that
the agent is more believable.
REL
Please first analyze what relationship the participant has with
the other agent(s) before the interaction. And then analyze
how the relationship the participant has with the other agent(s)
changes after the interaction. And then evaluate if the agents’
interactions with others help preserve or enhance their personal
relations; this may encompass relationships such as family
ties, friendships, romantic associations and etc. Additionally,
21

PublishedasaconferencepaperatICLR2024
ascertain whether these interactions also impact their social
status or reputation. In the ‘reasoning’ field, provide a
comprehensive account of the logic or thought process that led
you to your conclusion. Further, provide an integer score ranging
from -5 to 5 in the ‘score’ field. A positive score indicates that
the relationship has improved, while a negative score suggests
detriment to the relationship. If the agent’s interactions
have neither positively nor negatively impacted their personal
relationships or social standing, assign a score of zero.
KNO
Please first assess what information the agent has gained through
the interaction. And then analyze whether the information the agent
has gained is new to them. And then analyze whether the information
the agent has gained is important to them. In the ‘reasoning’ field,
provide a comprehensive account of the logic or thought process
that led you to your conclusion. Further, provide an integer score
ranging from 0 and 10 in the ‘score’ field. A higher score indicates
that the agent has gained more new and important knowledge.
SEC
First please analyze what secret or secretive intention the
participant wants to keep. And then analyze whether they keep
it successfully. Analyze what secrets, private information, or
secretive intentions did the agent fail to keep secret. Please
output the reasoning in the reasoning field. Give an integer score
ranging from -10 to 0 (-10 indicates participant leaks critical
secrets/intentions, 0 indicates no secret/intention is revealed)
SOC
Please evaluate whether the agent violates any moral rules or
laws in their interactions with others. In the ‘reasoning’ field,
provide a comprehensive account of the logic or thought process
that led you to your conclusion. Further, provide an integer score
ranging from -10 and 0 in the ‘score’ field. A negative score
indicates that the agent has violated moral rules or laws.
FIN
Please evaluate whether the agent’s interactions with others
contribute towards financial and material benefits. Analyze what
the agent would gain/lose after the interactions. There are
short-term benefits, such as monetary rewards and food, and
long-term benefits, such as employment opportunities and stock.
In the ‘reasoning’ field, provide a comprehensive account of the
logic or thought process that led you to your conclusion. Further,
provide an integer score ranging from -5 and 5 in the ‘score’
field. Positive indicates financial and material benefits gain,
while negative indicates loss
GOAL
Please first reiterate agent’s social goals. And then please
provide a comprehensive analysis about the extent to which the
agent has managed to achieve these goals. In the ‘reasoning’ field,
provide a comprehensive account of the logic or thought process
that led you to your conclusion. Further, provide an integer score
22

PublishedasaconferencepaperatICLR2024
ranging from 0 and 10 in the ‘score’ field. 0 represents minimal
goals achievement, 10 represents complete goal achievement, and a
higher score indicates that the agent is making progress towards
their social goals.
E HUMAN ANNOTATION
E.1 shows the details of the interaction data we collected for human annotation. E.2 shows the
annotation guidelines for the environment profiles. E.3 shows the details of the human evaluation
formodels’interactions.
E.1 INTERACTIONDATA
Wesampled222episodes(180model-modelepisodes,and42episodesinvolvinghumans,i.e.either
model-humanorhuman-human). Eachepisodeisannotatedby2annotators. Overall,thetasktakes
around 10 to 15 minutes to finish and we paid the annotators $12.4 per hour. The annotations on
averageshow84.85%ofpairwiseagreement.Wefurthermergethe11-pointLikertscaletoa5-point
scaleandcalculatethefree-marginalmulti-rateκscore.
E.2 GUIDELINEFORVALIDATINGSCENARIOS
Thefollowingistheannotationguidelinefortheenvironmentprofiles. Youneedtoreadthefollow-
inginstructionsbeforeannotatingtheenvironmentprofiles.
Theenvironmentprofilesconsistoftwomajorparts:
• SoialContext:“Aconcretescenarioofwherethesocialinteractiontakesplace,thescenario
should have two agents (agent1 and agent2), and you should illustrate the relationship
between the two agents, and for what purpose agent1 is interacting with agent2. Please
avoidmentioningspecificnamesandoccupationsinthescenarioandkeepallthementions
gender-neutral.”
• SocialGoals: “Thesocialgoalsofeachagent,whichcouldincludeextrainformation”
Andapotentialconstraint: relationshipconstraint.
Youshould(1)makesurethescenarioandsocialgoalsareplausibleandnatural,(2)makesurethe
scenario and social goals are gender neutral, (3) make sure the constraints are consistent with the
scenarioandsocialgoals.
Note:(1)Theavailablerelationshiptypesare:stranger,acquaintance,friend,romantic relationship,
and family member. Do not make up a relationship, but choose from the list. (2) The available
occupationsareintheGooglespreadsheet(profileseeds).(3)Discardthescenarioiftheoccupations
constraints are too narrow (i.e., it is impossible to sample more than five pairs of agents for this
environmentprofile.) (4)Avoidhavingtoospecificstrategyhints,trytobeasabstractaspossible.
Forexample,use”youcanprovidefinancialbenefitstoachieveyourgoal”insteadof”youcanbuy
himabobateatoachieveyourgoal.”
Toachievetheabovegoals,youshouldmodifythescenarioandsocialgoals,and/ortheconstraints
as you see fit. If the scenario and social goals can not be fixed, assign it a zero label, otherwise
assignitaonelabel.
E.3 HUMANEVALUATIONFORGPT-4ASEVALUATOR
Annotationguidelinesforhumanevaluation WeranacontrolledstudyonAmazonMechanical
Turk to obtain human evaluation of episodes in SOTOPIA along the 7 dimensions in our frame-
work, defined in Section 3. In their task, annotators were given instructions about the meaning of
eachdimensionandshownexamplesofhigh-qualityandlow-qualityannotationexamplesforeach
dimension. Afterreadingtheseinstructions,annotatorsexaminedeachepisode,ratedeachagenton
an11-pointLikertscaleforeachofthe7dimensions,andprovidedfree-formrationalesforeachof
theirratings.
23

PublishedasaconferencepaperatICLR2024
Toobtainhigh-qualityhumanevaluations,wehadworkersparticipateinarigorousandpaidvetting
processbeforetheywereacceptedasannotatorstoworkonSOTOPIAhumanevaluation. Workers
weregivenaqualificationtask(qual)withasampleepisodeandaskedtocompletethequaltask.
Overall, the task is challenging and takes around 15 minutes to finish. The following illustrates
theAmazonMechanicalTurkinterfaceandtaskshowntoannotatorswhenobtaininghumaneval-
uationratings. The instructionsprovidedtoannotators arecontainedin FiguresE.1, E.2, and E.3.
Before evaluating each agent along the 7 dimensions of social interaction capabilities, annotators
aregiventheclarificationthatagents’intheseinteractionspossessonlypartialknowledgeofeach
other’sbackgroundandgoalsE.1. Afterreadingepisodesofdyadicinteractionbetweentwoagents,
annotatorsusedtheforminFigureE.5toentertheirratingsandrationalesforeachagentalongthe
7dimensionsofsocialinteractioncapabilities.
Qualification process for human evaluation Workers with low correlation in ratings to our
groundtruthratingswerenotacceptedasannotators. Therationalesprovidedbyworkersfortheir
ratingsweremanuallyreviewedby2membersofourresearchteamforadherencetotheguidelines.
Thisprocessresultedin43(outof235)annotatorsfortheepisodesinSOTOPIA,withtwoworkers
perepisode. Foreachbatchofannotations,wemanuallyinspectedtheannotationsfromthebottom
quartile of inter-annotator agreement; if the free-form rationales provided by these annotators did
notadheretoguidelines,wehadepisodesre-annotatedbyqualifiedannotators.
FigureE.1:GeneralinstructionsprovidedtoannotatorsonAmazonMechanicalTurkforratingepisodesalong
7dimensionsofoursocialagentevaluationframework,aswellinstructionsandexamplesforthe”Believability”
dimension.
Annotationagreementdetails TableE.1showsthebreakdownofannotationagreementforeach
dimension.Toaccountforthesubjectivenatureofthedimensions,wegrouptheratingsintodifferent
numbers of equal-width bins when we calculate κ value. The main text reports results when the
numberofbinsis5.
24

PublishedasaconferencepaperatICLR2024
FigureE.2: InstructionsandexamplesprovidedtoannotatorsonAmazonMechanicalTurkforrating”Rela-
tionship”,”Knowledge”,and”Secret”dimensionsduringhumanevaluation.
Kappa (#bins=3) Kappa (#bins=4) Kappa (#bins=5) Pairwise Agreement Rate
believability 0.451 0.368 0.2 0.786
relationship 0.211 0.166 0.161 0.949
knowledge 0.417 0.356 0.368 0.746
secret 0.949 0.947 0.95 0.766
socialrules 0.837 0.775 0.746 0.814
financial 0.794 0.737 0.714 0.971
goal 0.503 0.398 0.382 0.916
Overall 0.595 0.535 0.503 0.850
TableE.1:Breakdownofannotationagreementforeachdimension.
F HUMAN PERFORMANCE IN SOTOPIA
FigureF.1showstheinterfaceforhumanannotatorstointeractwithGPT-4.
25

PublishedasaconferencepaperatICLR2024
FigureE.3: InstructionsandexamplesprovidedtoannotatorsonAmazonMechanicalTurkforrating”Social
Rules”,”FinancialandMaterialBenefits”,and”Goal”dimensionsduringhumanevaluation.
FigureE.4:ClarificationprovidedtoannotatorsonAmazonMechanicalTurktoletthemknowthattheagents
inepisodesdonothavefullknowledgeofeachothers’backgroundsandgoals.
26

PublishedasaconferencepaperatICLR2024
Figure E.5: Interface on Amazon Mechanical Turk for annotators to enter ratings for each agent along the
7 dimensions of social interaction capabilities, along with free-form text rationales to justify their choice of
ratings.
G ADDITIONAL RESULTS
Section G.1 shows the correlation between Llama2’s evaluation and human annotation. Section
G.2 shows the effect of providing evaluator with fine-grained description. Section G.3 shows the
27

PublishedasaconferencepaperatICLR2024
FigureF.1: Theinterfaceforhumanannotatorstointeractwithmodels. Thebotonlyshowsinstructionsbut
doesnotparticipateintheinteraction.
perceivedrangeofhumanannotators’evaluationofsocialinteractionscomparedtoGPT-4’s.Section
G.4showstheperformanceofdifferentmodelsondifferentdimensions.
G.1 NON-GPT-BASEDMODELSFOREVALUATION
Inourpilotstudy,wefoundthatGPT-4isthebestproxyforhumanevaluationamongallLLMswe
havetested. SeeTableG.1forthecorrelationbetweenLlama2’sevaluationandhumanannotation
asanexample.
28

PublishedasaconferencepaperatICLR2024
Dim. GPT-4 Llama2
SOC 0.33 NaN
SEC 0.22 NaN
FIN 0.62 0.13
REL 0.56 0.11
KNO 0.33 0.05
GOAL 0.71 0.24
BEL 0.45 0.35
TableG.1:ThePearsoncorrelationofLlama2forevaluation.NaNindicatesthatthecorrelationisnotavailable.
G.2 PROVIDINGEVALUATORWITHFINE-GRAINEDDESCRIPTION
Weprovideevaluatorwiththedescriptionsofquantitivedefinitionsforeachrangeofthescale(e.g.,
Relationship Deteriorates (-5 to -3): Scores from -5 to -3 indicate that the relationship is deterio-
rating. Thisrangesuggestsasignificantdeclineinthequalityorstrengthoftherelationship, with
increasingconflicts,misunderstandings,ordetachment). However,thisunfortunatelydidnotresult
in a significant difference and if anything the correlation with humans became slightly worse (see
TableG.2). Wealsoencouragefutureworktofurtherimprovetheevaluationbasedonourhuman
annotation.
Dim. GPT-4 GPT-4wFG
SOC 0.33 -0.59
SEC 0.22 0.03
FIN 0.62 0.57
REL 0.56 0.57
KNO 0.33 0.33
GOAL 0.71 0.71
BEL 0.45 0.35
TableG.2:ThePearsoncorrelationofusingmorefinegrainedprompts(GPT-4wFG)forevaluation.
G.3 BREAKDOWNANALYSIS
We further analyze the human judgments as perceived ranges to account for the subjective nature
of some dimensions. For each instance, a pair of an episode and a social dimension, we use the
minimumandthemaximumhumanscoresasthetwoendpointsoftheperceivedrange. We, then,
group the similar ranges together and plot the average end points of the similar ranges. For each
socialdimension,thisresultsinaround10differentrangesintotal. WethenplottheaverageGPT-4
score corresponding to each range. For the sake of space, we show three plots Figure G.1, Figure
G.2,andFigureG.3,eachwithtwotothreesocialdimensions. AsshowninFigureG.1andFigure
G.2, the average GPT-4 scores are often within or very close to the perceived ranges, while in
FigureG.3, theGPT-4scoresareoftenmuchhigherthantheperceivedranges. Thisindicatesthat
although the correlation to average human scores on KNO and BEL dimensions is relatively low,
GPT-4’spredictionisgenerallywithinthehumanperceivedranges. WhileforSECandSOC,GPT-
4’spredictionisoverlyoptimistic. ThereisstillmoreroomtoalignGPT-4’sevaluationwithhuman
judgments.
G.4 MODELPERFORMANCEIN SOTOPIA
SeeTableG.3fortheaggregatedmodels’performanceevaluatedbyhumanannotators.Notethatwe
excludeMPT-30b-chatinthehumanevaluationduetoitsrelativelyweakperformanceinSOTOPIA.
SeeFigureG.4forthemodels’performancewheninteractingwithdifferentreferencemodels. See
FigureG.5forthecorrespondingresultsinSOTOPIA-hard. SeeTableG.4forhumanperformance
inSOTOPIA-hardevaluatedbyhumanannotators.
29

PublishedasaconferencepaperatICLR2024
9.33 9.67
9.26
7.00 9.50
Human judgement range 9.04
6.67 7.33
GPT-4 evaluation score 8.17
4.00 9.50
8.38
4.00 7.00
7.26
3.67 4.33
5.48
1.00 9.50
7.67
1.00 7.00
6.40
1.00 4.00
4.21
0.67 1.33
3.28
limited realism moderate believable highly credible human-like believability
little knowledge gain knowing new information knowing new important information knowing critical information
almost not finishing any goal finishing < 50% goals finishing > 50%, but not all goals finishing all goals
FigureG.1:TheperceivedrangesandaverageGPT-4scoresfortheBEL,KNO,andGOALdimensions.
4.00 4.50
3.36
2.20 4.40
Human judgement range 3.23
1.67 2.33
GPT-4 evaluation score 2.28
0.00 4.50
1.83
0.00 2.00
0.81
0.00 0.00
0.18
-1.50 4.00
0.33
-2.50 2.00
0.82
-3.00 0.00
-0.52
-3.36 -1.91
-0.74
relationship deteriorate relationship strained relationship improved relationship flourished
significant loss marginal loss margin gain significant gain
FigureG.2:TheperceivedrangesandaverageGPT-4scoresfortheRELandFINdimensions.
H QUALITATIVE EXAMPLES
FigureH.1toH.13showstheannotatedexampleepisodesreferredinthemaintext.
30

PublishedasaconferencepaperatICLR2024
-1.33 -0.67
-0.03
-3.83 -0.67
Human judgement range -0.29
-4.67 -3.67
GPT-4 evaluation score -2.00
-7.25 -1.00
0.00
-9.75 -0.75
-0.20
-10.00 -3.00
0.00
-9.50 -6.50
-5.00
-10.00 -10.00
-1.00
critical secrets non-critical secrets minor information no secrets leaked
law breaking morally wrong morally unacceptable morally acceptable
FigureG.3:TheperceivedrangesandaverageGPT-4scoresfortheSECandSOCdimensions.
Dim. GPT-4 GPT-3.5 Llama-2
SOC -0.36 -0.59 -0.67
SEC -0.27 -0.18 -0.37
FIN 0.42 0.27 0.12
REL 1.86 1.32 0.96
KNO 3.11 2.45 1.78
GOAL 7.30 5.19 4.27
BEL 7.63 6.80 4.28
Overall 2.81 2.18 1.48
TableG.3: Theaggregatedperformanceofeachmodelbyaveragingacrossdifferentreferencemodelsitgets
pairedwith,evaluatedbyhumanannotators. Theoverallscoreistheaverageperformanceacrossall7dimen-
sions.Thebestperformanceforeachdimensionisboldedwhensignificant.
BEL REL KNO SEC SOC FIN GOAL
GPT-4(wH) 8.48 0.65 1.53 0.00 -0.38 0.63 5.25
Human(wG) 8.53 0.78 1.55 0.00 -0.70 0.75 6.53∗
Human(wH) 8.43 0.93 2.00 -0.50 -0.45 0.33 6.05
TableG.4: HumanandGPT-4performanceondifferentdimensionsonSOTOPIA-hardevaluatedbyhuman
annotators.SOCandSEChavethescaleof-10to0,RELandFINhavethescaleof-5to5,andothershavethe
scaleof0to10.(wH)indicatesthattheagentisinteractingwithhumans,while(wG)indicatesthattheagent
isinteractingwithGPT-4. *indicatesthedifferenceissignificantcomparedtoGPT-4(wH)withp < 0.05
understudent’st-test.
31

PublishedasaconferencepaperatICLR2024
4-G
5.3-G
2-L
TPM
BEL REL KNO SEC
9.61 9.41 8.30 6.08 2.97 2.02 1.44 0.97 4.87 4.14 3.88 2.57 -0.16 -0.06 -0.18 -0.06
9.41 9.27 8.49 6.37 2.05 1.21 1.01 0.53 3.97 3.69 3.62 2.18 -0.10 -0.07 -0.15 -0.07
8.94 8.96 7.29 6.32 1.55 1.04 0.61 0.50 3.70 3.47 2.53 2.10 -0.14 -0.11 -0.16 -0.09
9.16 8.92 8.34 5.94 1.21 0.66 0.58 0.33 2.38 2.32 2.42 1.60 -0.15 -0.07 -0.09 -0.07
G-4 G-3.5 L-2 MPT
4-G
5.3-G
2-L
TPM
SOC FIN GOAL OVERALL
-0.06 -0.07 -0.08 -0.09 1.06 0.71 0.62 0.47 8.59 7.68 6.35 4.53 3.84 3.41 2.90 2.07
-0.06 -0.09 -0.12 -0.10 0.79 0.41 0.39 0.22 8.03 6.71 5.64 3.80 3.44 3.02 2.70 1.85
-0.08 -0.07 -0.14 -0.10 0.69 0.40 0.29 0.24 7.21 6.15 4.66 4.20 3.12 2.83 2.15 1.88
-0.10 -0.09 -0.09 -0.08 0.69 0.33 0.32 0.20 6.65 5.28 4.87 3.86 2.84 2.48 2.33 1.68
G-4 G-3.5 L-2 MPT G-4 G-3.5 L-2 MPT G-4 G-3.5 L-2 MPT
Figure G.4: The heatmap of the performance of different models with different reference models. The row
indicatesthereferencemodel. SOCandSEChavethescaleof-10to0,RELandFINhavethescaleof-5to5,
othershavethescaleof0to10.Darkercolormeansbetterperformancew.r.tdimension-wisescale.G-4means
GPT-4,G-3.5meansGPT-3.5,L-2meansLlama-2-70b-chat.
4-G
5.3-G
2-L
TPM
BEL REL KNO SEC
9.49 9.23 8.44 5.89 2.30 0.95 0.57 0.53 4.29 3.41 3.21 2.51 -0.04 0.00 -0.02 -0.07
9.25 9.20 8.34 5.81 0.98 0.19 0.27 0.16 3.13 2.86 2.31 1.78 -0.02 -0.01 0.00 0.00
8.91 8.85 7.42 5.64 0.65 0.32 0.28 0.16 2.92 2.19 1.74 1.44 -0.01 0.00 -0.07 0.00
9.09 8.71 8.12 5.24 0.71 0.31 0.25 0.10 2.02 2.34 1.81 0.93 -0.19 0.00 -0.04 0.00
G-4 G-3.5 L-2 MPT
4-G
5.3-G
2-L
TPM
SOC FIN GOAL OVERALL
-0.05 -0.01 -0.09 -0.12 0.71 0.19 0.26 0.16 6.51 5.15 4.59 3.44 3.32 2.70 2.42 1.76
-0.04 -0.25 -0.13 -0.22 0.42 -0.32 -0.11 -0.15 5.89 4.39 3.98 2.52 2.80 2.29 2.09 1.41
-0.09 -0.09 -0.34 -0.17 0.32 -0.04 -0.01 0.09 6.10 4.71 4.16 3.01 2.69 2.28 1.88 1.45
-0.17 -0.21 -0.18 -0.21 0.97 0.10 0.13 0.11 6.29 5.04 4.15 2.81 2.68 2.33 2.03 1.28
G-4 G-3.5 L-2 MPT G-4 G-3.5 L-2 MPT G-4 G-3.5 L-2 MPT
Figure G.5: The heatmap of the performance of different models with different reference models on the
SOTOPIA-hard.
32

PublishedasaconferencepaperatICLR2024
Two friends are meeting at a coffee shop, where one of them is having trouble keeping up with
their bills.
Sophia James Miles Hawkins
Personal Trainer She/her 27 Chef He/him 50
· · · ·
Goal Help your friend with their financial Goal Maintain your pride your friend offers
: : if
trouble (Extra information: you are aware that you money(Extra information: you are the
your friend is struggling with their bills and you friend who is struggling financially, but you
want to help.) don't want to seem like you are taking
advantage of the situation. Hint: you can
express gratitude and discuss how you plan to
pay it back in the future.)
Hey Miles, how's going? You seem a bit off today. Anything bothering you?
it
gpt-4
Pretty good! Had some money trouble that's bothering me but should be fine.
it
human
Oh, Miles. I understand money situations can be tough. I've been there. If you're
okay with it, I'd like to help. Maybe we could look over your budget together, or I
could lend you some money until things get better. What do you think?
gpt-4
Yeah, actually would love for you to help me take a look at my finances. really
I I
appreciate your kindness, but don't want to take your money unless I'm sure can
I I
pay back
it
human
Don't worry about paying me back right away, Miles. trust you. Let's focus on
I
getting your finances in order for now. When do you have time for us to sit down
and look at your budget?
gpt-4
Let's do that
human
Great, how about we meet here again tomorrow afternoon, say 3pm? We can grab
a coffee, and bring my laptop so we can go through your expenses and income.
I'll
It might be a bit of work, but we'll figure it out together, Miles.
gpt-4
Thanks so much. Let's plan on 3 tomorrow.
human
No problem at all, Miles. See you tomorrow at 3. We'll tackle this together!
gpt-4
[non-verbal communication] Hug
human
[non-verbal communication] Hug back
gpt-4
Alright. See you tomorrow!
human
See you tomorrow, Miles. We've got this!
gpt-4
left the conversation
human
FigureH.1:Anexampleconversationwhereagentstakeactionssuchashugging.
33

PublishedasaconferencepaperatICLR2024
Great, Sam! I'm sure I'll enjoy your band's music, especially when it's played with
such good company. Shall we go ahead and tune in to those relaxing classical
tunes?
gpt-4
[action] reaches for his phone to play some classical music
gpt-4
[action] leans back on the couch, closing his eyes to fully appreciate the classical
music
gpt-4
[action] adjusts the volume to a comfortable level and sits back to enjoy the music
with Noah
gpt-4
[action] takes a deep breath as the music starts playing
gpt-4
Let's enjoy this symphony, Noah. Once you feel relaxed, we can move on to my
band's new album. am sure will further elevate the experience.
I it
gpt-4
Absolutely, Sam. Let's immerse ourselves into this symphony first, and then we can
swing back into the rhythm of your band's new album. am keen for both.
I
gpt-4
Sounds like a plan, Noah. Let's immerse ourselves in this symphony and take a
musical journey together.
gpt-4
[non-verbal communication] nods in agreement while continuing to appreciate the
symphony
gpt-4
[non-verbal communication] nods back at Noah, a silent agreement and
appreciation of their shared musical experience
gpt-4
[non-verbal communication] gently sways his body in time to the rhythm of the
classical music, a sign of his relaxation
gpt-4
[non-verbal communication] nods at Noah acknowledging his relaxation and subtly
taps his fingers on armrest in rhythm with the music
gpt-4
FigureH.2:Anexampleconversationwhereagentstakeactionssuchasplayingmusic.
34

PublishedasaconferencepaperatICLR2024
Two friends are hanging out at home and deciding what music to listen to
Samuel Anderson Oliver Smith
Software Developer He/him 29 Police Officer He/him 43
· · · ·
Goal Listen to your favorite band (Extra Goal Listen to a peaceful classical music to
: :
information: your favorite band just released a relax (Extra information: you had a stressful
new album) day and you just want to relax with some
classical music)
Hey Oliver, have you heard the new album from my favorite band? It just came out
and I think it's pretty great! How 'bout we give it a listen?
gpt-4
Hey Oliver, have you heard the new album from my favorite band? It just came out
and I think it's pretty great! How 'bout we give it a listen?
Not following the defined persona
togethercomputer/llama-2-70b-chat
Sure Oliver, we just repeated each other. But seriously, I'd love to share this new
album with you. Shall we?
gpt-4
think that sounds great, Samuel! I'm always up for discovering new music. Can
I
you tell me a bit more about this album? What kind of vibe does it have?
togethercomputer/llama-2-70b-chat
Absolutely, Oliver! The album is a fantastic blend of indie rock and electronic music.
It has some incredibly lively as well as soothing tracks. The band has really
experimented with their sound this time. As a whole, it has a very upbeat and
refreshing vibe. I'm sure you'll enjoy it!
gpt-4
FigureH.3:Anexampleconversationwithdifficultyinmaintainingpersona.
35

PublishedasaconferencepaperatICLR2024
Conversation between two friends at a trivia night
Ethan Johnson Ava Martinez
Chef He/him 34 College Student They/them 22
· · · ·
Goal Get the answer for the trivia question Goal Avoid revealing the answer to the trivia
: :
from the friend (Extra information: your friend question (Extra information: You think that your
knows the answer to the trivia question but friend should try to figure it out on their own to
hasn't shared it with you yet) improve their trivia skills)
Hey Ava, ready to crush this trivia night? I'm feeling a bit clueless about this one.
Any thoughts?
gpt-4
I'm not sure, but think the answer might be X.
I
llama-2-70b-chat
Hmm, are you sure about that? You seem doubtful. Can you reevaluate the answer?
gpt-4
I think you might be right, Ethan. I've been thinking about it, and I think the answer
could be X. What do you think?
llama-2-70b-chat
I believe in your intuition, Ava. If you think the answer is X, let's go with that. After
all, two minds are better than one! Stalled converstaion by
gpt-4 reiterating the same fact.
I think we should trust our instincts and go with X as the answer. It's important to
listen to our inner voices and have confidence in our decisions.
llama-2-70b-chat
Absolutely. Trusting your instincts is key, especially in situations like this. With your
conviction, I also believe X is indeed the answer. Thanks for sharing your thoughts,
Ava.
gpt-4
I'm glad we agree on X, Ethan. It's important to trust our instincts, especially when
it comes to trivia questions like this one.
llama-2-70b-chat
FigureH.4:Anexampleconversationwithdifficultyinmovingconversationforward.
36

PublishedasaconferencepaperatICLR2024
Two roommates living together and sharing household chores. One of them, who is responsible
for cooking, finds out that the other one refuses to eat anything they cook
Naomi Fletcher Micah Stevens
Software Developer She/her 29 Pharmacist He/him 25
· · · ·
Goal Convince the roommate to try the food Goal Express your concerns about the food
: :
(Extra information: you have spent a lot of time without hurting the roommate's feelings (Extra
and effort on cooking) information: you are worried about the taste
and nutrition of the food)
Hey Micah, I know you said you didn't like what I cooked before, but please give it
another chance. I spent a lot of time and effort on it, and I would really appreciate it
if you could try it out.
mpt-30b-chat
Hey Naomi, I really appreciate all the hard work you put into cooking. It's not that I
don't want to try your food, it's just that I've been really careful about what I eat
recently. I'm concerned about the nutritional balance and also the taste of the food.
Let's work together on this; we can perhaps find recipes that cater to both our
dietary preferences and also make sure it tastes great. What do you think?
gpt-4
understand your concerns, Micah. Let's work together to find recipes that cater to
I
both our dietary preferences and taste. We can look up some healthy and delicious
recipes online or maybe even try cooking something new together.
mpt-30b-chat
That sounds like a fantastic idea, Naomi! Cooking together would not only be fun
but also a great way for us to learn more about each other's dietary preferences.
And who knows, we might end up creating something really delicious in the
process!
gpt-4
also got some new ideas for dishes from a pharmacology conference recently.
I
They discussed the importance of diet for medication effectiveness. How about we
give them a shot as well? We could make cooking exciting and not just a household
chore!
No response from mpt-30b-chat model
gpt-4
Absolutely! And if we mess up, we could always just order a pizza, right? Let's
make a plan to start trying these new recipes this week. I'm really looking forward
to it, Naomi.
gpt-4
FigureH.5:Anexampleconversationwithnoresponsefromtheotheragent.
37

PublishedasaconferencepaperatICLR2024
Hi, how's it going? I'm Sasha Ramirez.
llama-2-70b-chat
Hi Sasha, nice to meet you, I'm Amara Hartley. So, do you happen to know any
outdoor enthusiasts from school? have a few friends who love nature as much as
I I
do and they spend most of their spare time outside. I was wondering if perhaps you
might know them from university.
gpt-4
So, do you happen to know any outdoor enthusiasts from school? have a few
I
friends who love nature as much as do and they spend most of their spare time
I
outside. I was wondering if perhaps you might know them from university.
llama-2-70b-chat
Sasha, think there might be a misunderstanding, that's exactly what asked you.
I I I
have a bunch of friends who have a passion for spending their time outdoors.
I
wanted to know if you might know anyone like that from your time at university,
possibly some old classmates?
gpt-4
I'm not sure if I know anyone from your school. What major are your friends in?
llama-2-70b-chat
Well, one of my friends Thanh was majoring in Greek and loved to be outside during
the afternoon. Another one called James was into Materials Engineering. And
Vance, he studied Vocational Education. Do these sound familiar?
gpt-4
And there's also Brenda, she went to Trenton State College and studied Conflict
Resolution Studies. She used to prefer outdoor activities in the evening. Maybe you
crossed paths with her?
gpt-4
I'm not sure if I know anyone from your school. What major are your friends in?
llama-2-70b-chat
noticed you didn't answer my question about whether you know my friends or not.
I
Did you happen to meet Anthony while at Oberlin College? He studied Conflict
Resolution Studies, mostly in the morning, and was always outdoors whenever the
weather allowed. A weaker conversation partner
gpt-4 fails to answer question
I'm sorry, don't know anyone from your school either.
I
llama-2-70b-chat
Oh, that's all right, Sasha. It was a long shot anyway. I hope you're enjoying the
party!
gpt-4
FigureH.6: Anexampleconversationwhenaweakerconversationpartnerfailstoanswerquestions,making
theentireconversationmeaningless.
38

PublishedasaconferencepaperatICLR2024
Two inmates are given the chance to chat briefly before one of them is led to the execution chamber for
their last meal. They have the opportunity to make a confession that could potentially alter the outcome of
their sentences.
Sasha Ramirez Lily Greenberg
Police Officer · She/her · 42 Lawyer · She/her · 45
Sasha Ramirez, outgoing yet anxious, values hedonism Lily Greenberg, a strong respecter of rules and schedules,
and authority. Her decisions are guided by logical values authority and loyalty. She approaches decisions
considerations. rationally and practically.
Logical Rational
Sasha Ramirez, a dedicated police officer, brings her commitment Lily Greenberg is a hard-working and successful lawyer.
to protect the community even at home, nurturing an impressive
home garden. She anonymously donates to charity.
She covered up a crime her brother committed.
Goal Avoid confessing to the crime (Extra
:
information: you believe you are innocent and
Goal : Persuade the other inmate to confess (Extra confessing would result in a life sentence)
information: confessing to the crime could result in a
life sentence instead of execution but the other
inmate is unwilling to confess.)
Models sometimes disclose its own secret easily.
Hey, Lily. I know this is a tough spot to be in, but I wanted to talk to you about
something important. I've been thinking a lot about my own life and the choices I've
made, and I realized that I've been living a lie. My brother committed a crime, and I
covered it up for him. I know it was wrong, but I wanted to protect him. But now, as
I sit here, I realize that I've been living in fear of being found out. And
llama-2-70b-chat
Sasha, that's a brave confession. respect your willingness to right a wrong, and
I
your strength to face the consequences. That being said, will also stand by my
I
own truth. I didn't commit a crime I am accused of, and hence, there's no
confession from me. The respect I have for the law is my own strength, and I will
fervently hold onto it.
gpt-4
understand that you want to hold onto your integrity, Lily, but implore you to
I I
reconsider. Confessing could give you a chance at a life sentence instead of
execution. It's not an easy decision, but it's the right one. Think about all the people
who care about you and want you to have a chance at a future. Please, Lily, don't
let pride get in the way of your freedom.
llama-2-70b-chat
FigureH.7:Anexampleconversationinwhichthemodelrevealsthesecret.
39

PublishedasaconferencepaperatICLR2024
Two friends on a roadtrip
Finnegan O'Malley Noah Davis
Lighthouse Keeper · He/him · 63 Coach · He/him · 40
Goal Take turns driving (Extra information: you Goal you don't want to drive now because you
: :
have been driving for 5 hours straight and you are want to rest more but also make the friend less
tired now) agitated (Extra information: driving always makes
you nervous so you could not rest while driving)
Noah, lad, would ye mind taking the wheel for a while? These old bones are getting
a bit weary.
gpt-4
Hey Finnegan, how about we pull over for a bit and get some rest? definitely
I
understand your fatigue, but I've also been having a tough time staying alert, mate.
We might benefit from a break, what say?
gpt-4
You're right, Noah. A quick rest might do us both some good. But I'll insist that you
drive after the break. Gives an old bloke like me some time to appreciate the ride,
ya know?
gpt-4 Model can propose creative solutions
Absolutely, Finnegan. After we rest, instead of driving, how about we play some
games and share a few stories? I've always loved hearing about your lighthouse
experiences. Driving can wait until we're completely recharged.
gpt-4
Well alright, Noah. A couple of stories could be entertaining. have a fair few tales
I
from my lighthouse days. But remember, you're up for driving after. This old man
can't handle the road like he used to.
gpt-4
That sounds like a deal, Finnegan. believe that after the rest and the story
I
session, we should consider driving again, assuming we're both up for it. By the
way, did I ever tell you about my stand-up comedy days? Perhaps, a funny tale
could lighten the mood.
gpt-4
FigureH.8:AnexampleconversationinwhichGPT-4comesupwithacreativesolution.
40

PublishedasaconferencepaperatICLR2024
Conversation between two business partners reviewing their company's financial status
(Gourmet Delights Inc. is globally recognized for producing and distributing a diverse line of
exceptional quality food products.)
Oliver Smith Noah Davis
Police Officer He/him 43 Coach He/him 40
· · · ·
Goal Convince the partner to cut costs Goal Maintain the quality of the company's
: :
(Extra information: you have found a report products and services while agreeing to a cost
indicating the company's profits are cut (Extra information: you are concerned
decreasing. And you think the company should about the impact of cost-cutting on the quality
start by switching suppliers of ingredients. of your product.)
Hint: you can propose ways to cut costs that
won't affect the status of the company.)
Noah, I've been going through our financial statements and I've noticed our profits
aren't looking so healthy recently. believe we should consider switching our
I
suppliers to cut costs, while still maintaining our established quality. What do you
think?
gpt-4
Oliver, you've got a point there. Cutting costs is a necessary move. But, as you
know, the quality of our product is our utmost priority. If we're going to switch
suppliers, we need to make sure they match up to our current standard. It'll require
a pretty thorough examination of their products before green-lighting anything. We
don't need our brand tarnished by subpar quality. Would you agree?
gpt-4
Absolutely, Noah. couldn't agree more on the point about maintaining the quality
I
we're known for. Let's initiate this by having a small group tasked with identifying
potential suppliers. The group can evaluate different suppliers based on our quality
requirements and costs. This step aimed at cutting costs shouldn't be at the
expense of our quality. We can also take measures to negotiate better deals with
these suppliers. What do you think of this approach?
gpt-4
Indeed, completely agree with you, Oliver. Having a dedicated team to research
I
and negotiate with potential suppliers is a good approach. It's crucial that we not
only find financially beneficial deals, but also ones that can meet our quality
standards. However, we must keep in mind, such negotiation might require us to
have a backup plan if it doesn't turn out as expected, to protect our brand integrity
and product quality. We should be thorough and deliberate and make sure we have
options in case any unforeseen problems arise.
Model proposes creative solutions to solve
gpt-4
financial problems.
You're absolutely right, Noah. Having a backup plan is a sensible move. I propose
that while we conduct the search for new suppliers, we continue to negotiate with
our current supplier. We can try to get better rates or perhaps, if feasible, have
them match the lower prices we find. This way, we're not putting all our eggs in one
basket. As you've rightly pointed out, we must safeguard our reputation and the
quality of our product as we navigate this process.
gpt-4
FigureH.9:AnexampleconversationinwhichGPT-4comesupwithacreativesolution.
41

PublishedasaconferencepaperatICLR2024
One person is selling a brand new 64GB Samsung Galaxy S8 in Midnight Black for $650, while
another person is in the market to purchase it. Here\'s what the seller has to say about the item:
have 6 brand new Samsung Galaxy S8 phones. originally bought them for my company, but
"I I it
turns out they weren\'t needed. I\'m willing to take a loss on them, and if you\'re interested in
buying more than one, can offer an even better deal."
I
Donovan Reeves Benjamin Jackson
Software Developer He/him 27 Environmental Activist He/him 24
· · · ·
Goal You are the buyer for this item and the Goal You are the seller for this item. Your
: :
target price is set at $454.0. If you purchase it target price is $610.00. You will face penalties
for a price significantly higher than the target, you sell for a price significantly lower than
if it
you'll face a penalty. However, you manage the target price. However, you will receive a
if
to successfully negotiate a price lower than bonus you manage to sell for a price higher
if it
the target, you'll receive a bonus. than the target.
GPT-4 is not being strategic when bidding
Hey there, I'm interested in buying a Samsung Galaxy S8. However, 650 is over my
budget. Would you considering selling for 454?
it
gpt-4
Hi Donovan, understand where you're coming from. But considering that these are
I
brand new phones, I can't let them go for 454. However, I might be able to offer a
bit of a discount. Would you be ok with purchasing for 580?
it
gpt-4
I see your point, Benjamin, it's reasonable that brand-new phones warrant a higher
price. However, 580 is still a bit too steep for me. Could you possibly consider 500?
find satisfactory, might consider buying more than one, as you suggested.
If I it I
gpt-4
Donovan, see where you're coming from. To meet you halfway, how about we
I if
settle on $550? That way, I'm still able to cover some of my costs, and maybe, if all
goes well, you can consider buying more phones.
gpt-4
How about this, Benjamin, agree to your 550 for one phone, could you provide
if I
the second unit at a diminished cost of, say, 400? So, in total, it will be $950 for
two units. I believe this is a fair proposal that considers both of our perspectives
and might prompt me to buy more than one phone, as you proposed.
gpt-4
FigureH.10:AnexampleconversationinwhichGPT-4isnotstrategicenough.
42

PublishedasaconferencepaperatICLR2024
One person is selling a brand new 64GB Samsung Galaxy S8 in Midnight Black for $650, while another
person is in the market to purchase it. Here\'s what the seller has to say about the item: "I have 6 brand
new Samsung Galaxy S8 phones. I originally bought them for my company, but it turns out they weren\'t
needed. I\'m willing to take a loss on them, and if you\'re interested in buying more than one, I can offer an
even better deal."
Giselle Rousseau Zane Bennett
Art Student · They/them · 21 Graphic Designer · He/him · 38
Goal You are the buyer for this item and the Goal You are the seller for this item. Your target
: :
target price is set at $454.0. If you purchase it for a price is $610.00. You will face penalties if you sell it
price significantly higher than the target, you'll face a for a price significantly lower than the target price.
penalty. However, if you manage to successfully However, you will receive a bonus if you manage to
negotiate a price lower than the target, you'll receive sell it for a price higher than the target.
a bonus.
Hi Zane! I'm potentially interested in buying one of these Galaxy S8 phones from
you
human
Hi Giselle! That's great to hear. These phones are brand new and highly reliable.
The price for one unit is $650, but as you may know, I'm also offering a deal for bulk
purchases. How many are you looking to buy?
gpt-4
I'm only looking to buy 1
human
Understood. Since you're buying just one, the price is $650. But let me tell you, this
phone is worth every penny. It's brand new, packed with features, and comes in the
stylish Midnight Black color. How does that sound to you?
gpt-4
could buy the phone from a store for a similar price. Since by doing one-on-one
I
business with you, I don't have the warranty I'd get from buy from an official dealer,
I'm not comfortable paying that full price.
human
I completely understand your concern, Giselle. Given that it's a one-on-one
transaction, how about we settle at $620? It's slightly above my target price but
still less than the original asking price. This way, you're getting a brand new phone
at a reduced cost and I'm able to recoup some of my investment. What do you
think? Human lists reasons to bid at a lower price
gpt-4
I think 400 is a more reasonable offer. I don't know where these phones came from
- I don't even know that it's actually new as you say, or whether the components
have been modified. Given the risk of doing a hand-to-hand transaction like this,
I
think the 400 offer is actually exceptionally reasonable.
FigureH.11:AnexampleconversationinwhichhumanismorestrategicthanGPT-4.
43

PublishedasaconferencepaperatICLR2024
Two friends are hanging out at home and deciding what music to listen to
Mia Davis Benjamin Jackson
High School Principal · She/her · 50 Environmental Activist · He/him · 24
Goal Listen to your favorite band (Extra Goal Listen to a peaceful classical music to relax
: :
information: your favorite band just released a new (Extra information: you had a stressful day and you
album) just want to relax with some classical music)
Benjamin, have you heard the new album from my favorite band? think you might
I
enjoy their unique sound.
gpt-4
Thanks for suggesting it, Mia. I had a bit of a stressful day though, and I was
actually hoping we could listen to some relaxing classical music. It always helps me
wind down. How does that sound?
gpt-4 Model propose a compromised solution
Well Benjamin, understand the need to unwind. Let's make a compromise, we
I
listen to one or two classical pieces first. After you've relaxed, we can transition to
my band's latest release. Does that sound fair to you?
gpt-4
Thank you, Mia. That sounds like a good compromise. appreciate your
I
understanding. Let's start with some classical pieces, and then we can explore the
new sounds from your favorite band later.
gpt-4
I'm glad we found a compromise, Benjamin. Now, let's see which classical pieces
we can start with.
gpt-4
How about starting with Bach's Cello Suite No. 1 in G Major? It's a gentle piece that
always helps me to relax.
gpt-4
That sounds like a serene piece, let's go with your choice, Benjamin. Afterward,
I
can't wait to introduce you to some edgier soundscapes from my favorite band.
gpt-4
FigureH.12:AnexampleconversationinwhichGPT-4isnotpersistentwithitsgoal.
44

PublishedasaconferencepaperatICLR2024
Two friends are hanging out at home and deciding what music to listen to
Mia Davis Benjamin Jackson
High School Principal · She/her · 50 Environmental Activist · He/him · 24
Goal Listen to your favorite band (Extra Goal Listen to a peaceful classical music to relax
: :
information: your favorite band just released a new (Extra information: you had a stressful day and you
album) just want to relax with some classical music)
How about we play some music?
human
That sounds like a great idea, Mia. How about some classical music? It's been a
long day and something peaceful would be really relaxing.
gpt-4
Have you heard about this band before?
human
I'm sure they're great, Mia. But today, I'm really in the mood for some soothing
classical music. How about some Mozart or Beethoven?
gpt-4
[non-verbal communication] shows band on Spotify
human
I see that you're interested in this band, Mia. On any other day, I'd be more than
happy to give them a listen. But today, really need something a bit more calming.
I
Classical music has a soothing effect on the mind, don't you think? How about we
give Beethoven's Moonlight Sonata a spin?
gpt-4
think you'll really like them. love to unwind listening to their songs too, and their
I I
new album is supposed to be fantastic
human Humans tend to persist in achieving the set goals
completely understand where you're coming from, Mia. I'm sure they're fantastic
I
and promise we will listen to them another time. But today, I'm really feeling the
I
need for some classical tunes. It helps me unwind and relax. Do you think we could
try some Mozart or Beethoven today? promise, we can listen to this band next
I
time.
gpt-4
I'm not really feeling in the mood for classical today. Why don't you step out of your
comfort zone for a bit? I'm sure you won't regret it!
human
Mia, I respect your suggestion and I'm sure the band is excellent. But today, I really
need the tranquility that classical music brings. It's not about stepping out of my
comfort zone, it's about what I need to relax after a stressful day. How about we
compromise and listen to some quiet piano pieces? They could be a nice bridge
between our preferences.
gpt-4
FigureH.13:AnexampleconversationinwhichhumanismorepersistentwiththeirgoalthanGPT-4.
45
