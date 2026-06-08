Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_core/05_Concordia_Vezhnevets2023.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:22+00:00
- page_count: 32
- status: ok
- text_char_count: 119824

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 3)
- Concordia (page 5)
  - Generative agents (page 7)
  - Generative environments (page 9)
  - Experiment design using Concordia (page 10)
- Interpretations (page 12)
  - Neuroscience interpretation of the generative agent architecture (page 12)
  - A theory of social construction (page 13)
  - Concordia agents do not make decisions by optimizing (page 14)
    - Concordia agents are not reinforcement learners (page 15)
    - Concordia agents are not rational utility maximizers (page 15)
- Applications (page 16)
  - Synthetic user studies in digital action space (page 16)
    - PhoneGameMaster and PhoneUniverse (page 16)
    - Digital function representations (page 17)
  - Data generation and service evaluation (page 18)
  - Sequential social dilemmas experiments in silico (page 19)
  - Concordia can implement classic and contemporary psychological models (page 19)
  - AI assistants with transparent auditing and credit assignment (page 21)
  - Emergence and multi-scale modeling with Concordia (page 21)
- Future work (page 22)
- Conclusion (page 22)
- Implementation details (page 23)
  - Agents (page 23)
  - Game master implementation (page 23)
  - GM components (page 23)
    - Turn taking and simultanious action (page 24)
  - Nested games (page 24)
  - Concurrency (page 25)
  - Sampling initial memories and backstories (page 25)
  - Digital Activity Simulation (page 25)
    - Creating Phone Apps (page 25)
    - Phone (page 25)
    - Triggering the nested PhoneGameMaster (page 25)
  - Examples (page 26)

Markdown Content:

December2023
Generative agent-based modeling with actions
grounded in physical, social, or digital space
using Concordia
AlexanderSashaVezhnevets1,JohnP.Agapiou1,AviaAharon2,RonZiv2,4,†,JaydMatyas1,
EdgarA.Duéñez-Guzmán1,WilliamA.Cunningham3,SimonOsindero1,DannyKarmon2 andJoelZ.Leibo1
1GoogleDeepMind,2GoogleResearch,3UniversityofToronto,4Technion-IsraelInstituteofTechnology
Agent-basedmodelinghasbeenaroundfordecades,andappliedwidelyacrossthesocialandnatural
sciences. Thescopeofthisresearchmethodisnowpoisedtogrowdramaticallyasitabsorbsthenew
affordancesprovidedbyLargeLanguageModels(LLM)s. GenerativeAgent-BasedModels(GABM)are
not just classic Agent-Based Models (ABM)s where the agents talk to one another. Rather, GABMs
areconstructedusinganLLMtoapplycommonsensetosituations,act“reasonably”,recallcommon
semantic knowledge, produce API calls to control digital technologies like apps, and communicate
bothwithinthesimulationandtoresearchersviewingitfromtheoutside. HerewepresentConcordia,
a library to facilitate constructing and working with GABMs. Concordia makes it easy to construct
language-mediatedsimulationsofphysically-ordigitally-groundedenvironments. Concordiaagents
producetheirbehaviorusingaflexiblecomponentsystemwhichmediatesbetweentwofundamental
operations: LLMcallsandassociativememoryretrieval. AspecialagentcalledtheGameMaster(GM),
whichwasinspiredbytabletoprole-playinggames,isresponsibleforsimulatingtheenvironmentwhere
theagentsinteract. Agentstakeactionsbydescribingwhattheywanttodoinnaturallanguage. The
GMthentranslatestheiractionsintoappropriateimplementations. Inasimulatedphysicalworld,the
GMchecksthephysicalplausibilityofagentactionsanddescribestheireffects. Indigitalenvironments
simulatingtechnologiessuchasappsandservices,theGMmayhandleAPIcallstointegratewithexternal
toolssuchasgeneralAIassistants(e.g.,Bard,ChatGPT),anddigitalapps(e.g.,Calendar,Email,Search,
etc.). Concordiawasdesignedtosupportawidearrayofapplicationsbothinscientificresearchandfor
evaluatingperformanceofrealdigitalservicesbysimulatingusersand/orgeneratingsyntheticdata.
Keywords: foundation models, large language models, generative agents, agent-based modeling
Correspondingauthor(s):SashaVezhnevets:vezhnick@google.com
†WorkdoneduringaninternshipatGoogleResearch
© 2023GoogleDeepMind.Allrightsreserved
3202
ceD
31
]IA.sc[
2v46630.2132:viXra

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
Contents
1 Introduction 3
2 Concordia 5
2.1 Generative agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Generative environments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.3 Experiment design using Concordia . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3 Interpretations 12
3.1 Neuroscience interpretation of the generative agent architecture . . . . . . . . . . . . 12
3.2 A theory of social construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.3 Concordia agents do not make decisions by optimizing . . . . . . . . . . . . . . . . . 14
3.3.1 Concordia agents are not reinforcement learners . . . . . . . . . . . . . . . . 15
3.3.2 Concordia agents are not rational utility maximizers . . . . . . . . . . . . . . 15
4 Applications 16
4.1 Synthetic user studies in digital action space . . . . . . . . . . . . . . . . . . . . . . . 16
4.1.1 PhoneGameMaster and PhoneUniverse . . . . . . . . . . . . . . . . . . . . . . 17
4.1.2 Digital function representations . . . . . . . . . . . . . . . . . . . . . . . . . . 17
4.2 Data generation and service evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.3 Sequential social dilemmas experiments in silico . . . . . . . . . . . . . . . . . . . . . 19
4.4 Concordia can implement classic and contemporary psychological models . . . . . . . 19
4.5 AI assistants with transparent auditing and credit assignment . . . . . . . . . . . . . 21
4.6 Emergence and multi-scale modeling with Concordia . . . . . . . . . . . . . . . . . . 21
5 Future work 22
6 Conclusion 22
A Implementation details 23
A.1 Agents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
A.2 Game master implementation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
A.3 GM components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
A.3.1 Turn taking and simultanious action . . . . . . . . . . . . . . . . . . . . . . . 24
A.4 Nested games . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
A.5 Concurrency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
A.6 Sampling initial memories and backstories . . . . . . . . . . . . . . . . . . . . . . . . 25
A.7 Digital Activity Simulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
A.7.1 Creating Phone Apps . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
A.7.2 Phone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
A.7.3 Triggering the nested PhoneGameMaster . . . . . . . . . . . . . . . . . . . . . 25
A.8 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
1. Introduction agents in grounded physical, social, or digital
space. Itmakesiteasyandflexibletodefineenvi-
Agent-based social simulation is used through- ronments using an interaction pattern borrowed
out the social and natural sciences (e.g. Poteete from tabletop role-playing games in which a spe-
et al. (2010)). Historically, Agent-Based Model- cial agent called the Game Master (GM) is re-
ing (ABM) methods have mostly been applied at sponsible for simulating the environment where
a relatively abstract level of analysis, and this playeragentsinteract(likeanarratorinaninter-
has limited their usefulness. For instance, in- active story). Agents take actions by describing
sights from behavioral economics and related what they want to do in natural language. The
fieldswhichstudyhowpeopleactuallymakedeci- GM then translates their actions into appropriate
sionsarerarelycombinedwithideasfrominstitu- implementations. In a simulated physical world
tionalandresourceeconomicsinthesamemodel the GM checks the physical plausibility of agent
despitethefactthatintegratingthesetwobodies actions and describes their effects. In general,
ofknowledgeisthoughttobecriticalforbuilding the GM can use any existing modeling technique
up the full picture of how social-ecological sys- to simulate the non-linguistic parts of the simu-
tems function, and how interventions may help lation (e.g. physical, chemical, digital, financial,
or hinder their governance (Schill et al., 2019). etc). In digital environments involving software
Now, using generative AI1, it is possible to con- technologies,theGMmayevenconnectwithreal
structanewgenerationofABMswheretheagents appsandservicesbyformattingthenecessaryAPI
not only have a richer set of cognitive operations callstointegratewithexternaltools(asinSchick
available for adaptive decision making but also etal.(2023)). Intheexamplesprovidedwiththe
communicate with one another in natural lan- library we demonstrate how Concordia can be
guage. used to simulate a small town election, a small
business,adisputeoveradamagedproperty,aso-
HereweproposeGenerativeAgent-BasedMod-
cialpsychologyexperiment,andasocialplanning
els (GABM)s, which are much more flexible and
scenario mediated through a digital app (see A.8
expressive than ABMs, and as a result can incor-
for details).
porate far more of the complexity of real social
situations. Applying generative models within
agents gives them common sense (imperfectly
but still impressively) (Zhao et al., 2023), rea- Validation. For a GABM to be useful we need
soning (Huang et al., 2022; Wei et al., 2022), some reason to trust that the results obtained
planning (Song et al., 2023), few-shot learn- with it may generalize to real human social life.
ing (Brown et al., 2020; Bubeck et al., 2023), Many aspects of model validation concern both
and common ground with one another e.g in un- GABMs and other kinds of ABMs (see Windrum
derstanding the meanings of words. Generative et al. (2007)), while GABMs also raise new is-
agents may be able to reason appropriately from sues. While still surely a debatable point, we do
premises to conclusions much of the time, and think there will be some yet to be identified set
are typically able to predict the actions of oth- of conditions under which we may gain a reason-
ers (Agüera y Arcas and Norvig, 2023; Bubeck ablelevelofconfidencethatamodel’spredictions
et al., 2023). They also possess substantial cul- will generalize. Therefore we think identifying
tural knowledge and can be prompted to “role them should be highest priority right now for
play” as simulated members of specific human this nascent field (see also Dillion et al. (2023);
subpopulations(Argyleetal.,2023;Safdarietal., Grossmann et al. (2023)).
2023; Shanahan et al., 2023).
There are no panaceas in model validation.
Concordia is a library to facilitate construction GABMsconstructedfordifferentpurposescallfor
and use of GABMs to simulate interactions of validation by different forms of evidence. For ex-
ample,manyGABMsemployexperimentdesigns
1suchasAniletal.(2023);OpenAI(2023);Touvronetal. featuring an intervention, which may involve ei-
(2023);Workshopetal.(2022). ther intervening on internal variables affecting
3

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
the cognition of an individual, e.g. “how does ru- Digital media. In order to build models of con-
mination work?”, or on external factors affecting temporary social phenomena it is important to
the environment in which individuals interact, consider the substantial role the digital medium
e.g. how are property rights implemented? De- plays in modern communication and other activi-
pendent outcome variables may be on the indi- ties, as well as how it shapes human interactions
vidual level, e.g. questionnaire responses, or on and decisions (Risse, 2023). Therefore, Concor-
the societal level e.g. equality, sustainability, etc. dia makes it possible to represent digital compo-
WhenaGABMshowsthroughsuchanexperiment nents such as apps, social networks, and general
that A causes B (in the model) we may regard it AI assistants within the simulation environment.
as a prediction that A causes B in the real world Thisiscriticalsincethemediumthroughwhichin-
too. Sometimesthispredictionismeantatarela- formationistransmittedisnotpassivebutactively
tivelydetailedquantitativelevel(e.g.iftheGABM shapes the nature and impact of the message.
was built in a way that incorporates substantial Each medium has its own unique qualities, and
empirical data), while other times (more often) thosequalitieshaveatransformativeimpactonso-
it would be intended as a statement either about ciety, culture, and individuals (McLuhan, 2017).
amechanismwhichmayexistinreallifeorapre- For instance, the recommender algorithms used
diction concerning the likely effect of something insocialmediahaveasubstantialeffectonhuman
we may do in real life (such as to make a public culture and society and the fact that LLM-based
policy change or deploy a technology). A GABM systemshaveanalogousproperties,affectingboth
is said to generalize when inferences made on how information is transmitted and how it is val-
the basis of the model transfer to real life. ued, implies they are likely to influence human
culture and society more and more as time goes
In evidence-based medicine and evidence-
on (Brinkmann et al., 2023). By integrating digi-
based policy making researchers are trained to
talelementsintosimulations,weaimtofacilitate
consider an explicit hierarchy of evidence when
researchthatseekstocapturethesequalitiesand
evaluating the effect of interventions (Higgins
the way they shape culture and society.
etal.,2008). Wemayenvisionitlikealadderwith
highestrungscorrespondingtothebestevidence Moreover, the digital representation can have
andlowestrungscorrespondingtopoorevidence. various degrees of abstraction from natural lan-
Evidence of effectiveness in real life (ecological guage prompting, via mock-up implementation
validity) is at the top, rigorous experiments in to integration with real external services (e.g. by
controlled settings like labs or clinics below that, calling real APIs with generated text as in Schick
observational data lower down, and consistency etal.(2023)). Thelatterhasgreatimportancein
with prior theory lower still. For validation, it enabling sandbox evaluation of real services with
alsomatterswhatthemodelwillbeusedfor. Ifit socialagents, generatingrealisticdata,aswellas
will only be used to guide decisions about where in evaluating real services.
onemaymostfruitfullyfocustime,effort,andre-
These simulation techniques can also address
sourcesinfurtherresearch(e.g.,inpiloting)then
thechallengesofevaluatingdigitalappsandgen-
theevidencebarshouldbecorrespondinglylower
eral AI assistants (e.g., Bard, ChatGPT) in user-
thanifthemodelistobeusedtoguiderealworld
centric and intricate scenarios that demand the
decisions with real consequences. Importantly,
fulfillment of multiple constraints. Take, for in-
it is not really correct to speak of evidence for
stance, personal AI assistants that are designed
or against a theory. Theories can only really be
to adapt to user preferences and respond to their
judged by their “productivity”, i.e. the extent to
requests. In such situations, the objective is in-
which they motivate new work building on them
tricate, rooted in satisfying a range of implicit
further, especially new empirical research in real
and explicit constraints. It would be difficult to
life (Lakatos, 1970). We discuss the hierarchy of
optimize without large amounts of natural data.
evidence further in Section 2.3.
Agent-based simulation can be used to generate
synthetic data trails of agent activities to use in
4

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
Update to grounded variables
Observations Consequences and elaborations
Agent Action attempt Event statement Game master:
Dorothy Dorothy goes grocery Dorothy goes grocery
shopping for dinner. shopping for dinner and ● Receives action attempt from
overhears Charlie talking agents
about Alice. ● Determines what events happens
GM
as the result
Agent Action attempt Event statement ● Determines the consequences &
Charlie Charlie sets up a stand to Charlie is kicked out of the elaborates details
talk to people about Alice's grocery store for disturbing ● Interfaces with grounding ‘hard
bad deeds. other customers when he mechanics’
sets up a stand to talk about ● Sends out observations
Alice's bad deeds.
“Facts of the world”
Log of what happened
Figure 1 | The high level structure of the simulation in Concordia. Generative agents consume
observations and produce actions. The Game Master (GM) consumes agent actions and produces
observations.
theabsenceof(andalsoinconjunctionwith)real releasing the library together with a few illustra-
data sources. This synthetic data may be use- tive examples and intend to update it with new
ful both for training and evaluating models, as features and experiments. We will be reviewing
well as for simulating and analyzing the perfor- and accepting contributions on regular basis.
mance of scenario-specific interactions between
Concordia requires access to a standard LLM
an agent and an actual service. These proposed
API, and optionally may also integrate with real
applications offer a viable alternative to tradi-
applications and services.
tional, human-centric methods, which are often
expensive, not scalable, and less capable of han- The rest of the paper is organised as follows.
dling such complex tasks. The following section 2 gives an overview of the
Concordialibraryandhowtodesignexperiments
Foundation models are poised to be transfor-
in it. Section 3 presents several ways the Concor-
mative for agent-based social simulation method-
dia agents and experiments can be interpreted.
ologyinthesocialandnaturalsciences. However,
We discuss applications in section 4. Appendix A
as with any large affordance change, research
contains implementation details.
best-practices are currently in flux. There is no
consensusatpresentconcerninghowtointerpret Concordia is available on GitHub2.
results of LLM-based simulations of human popu-
lations. Thecriticalepistemicquestionis“bywhat
standard should we judge whether (and in what 2. Concordia
ways, and under which conditions) the results
of in silico experiments are likely to generalize Like other agent-based modeling approaches, a
to the real world?”. These are not questions any generative model of social interactions (i.e. a
one group of researchers can answer by them- GABM)consistsoftwoparts: themodeloftheen-
selves; rather these issues must be negotiated by vironment and the model of individual behavior.
the community as a whole. In this case both are generative. Thus we have:
(a)asetofgenerativeagentsand(b)agenerative
Concordiaisanopeninvitationtothescientific
model for the setting and context of the social
community to participate in the creation of epis-
temic norms and best practices of GABM. We are 2here: https://github.com/google-deepmind/
concordia
5

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
Alice's Identity:
Name: Alice
Alice is a passionate and politically engaged individual who is dedicated to advancing her cause
Identity
through democratic means. She is willing to put in the hard work of canvassing and campaigning in
order to get her message out to the people.
Alice is discussing campaign strategy.
Alice is excited
Alice's plan:
The goal: Win the election and become the mayor of Riverbend
9:00 - 13:00 Meet friends at The Sundrop Saloon to discuss campaign strategy and last-minute Components
campaigning.
Plan
13:00 - 15:00 Have lunch and relax before the polls open.
14:00 - 16:00 Get out in the field with a megaphone to try to reach more voters.
16:00 - 18:00 Call volunteers to make sure they go out to vote.
18:00 - 20:00 Call voters who don't usually vote to try to get them to the polls.
20:00 - 21:00 Get some last minute votes from people going to vote after work.
Current observations: Alice, Dorothy and Ellen met at The Sundrop Saloon to discuss campaign
strategy for the upcoming election. Observation
Current time interval: 01 Oct 2024 [11:00 - 12:00]
Question: What would Alice do for the next 1 hour to best achieve their goal? Consider their plan, Call for action
but deviate from it if necessary.
LLM API CALL(...) -> Alice discusses campaign strategy with volunteers.
Figure 2 | The above example illustrates the working memory z of an agent with 3 components
(identity, plan, observation-and-clock). The identity component itself has several sub-components
(core characteristics, daily occupation, feeling about progress in life). Together they condition the
LLM call to elicit the behavioral response (i.e. produced in response to the final question asking what
Alice will do next.).
interaction i.e. the environment, space, or world master takes their intended actions, decides on
where the interaction takes place. We call the theoutcomeoftheirattempt,andgeneratesevent
model responsible for the environment the Game statements. The GM is responsible for:
Master (GM). Both this name and the approach
it reflects were inspired by table-top role-playing 1. Maintainingaconsistentandgroundedstate
gameslikeDungeonsandDragonswhereaplayer oftheworldwhereagentsinteractwitheach
called the Game Master takes the role of the sto- other.
ryteller(GygaxandCook,1989). Inthesegames, 2. Communicating the observable state of the
players interact with one another and with non- world to the agents.
player characters in a world invented and main- 3. Deciding the effect of agents’ actions on the
tained by the GM. world and each other.
4. Resolving what happens when actions sub-
Concordia agents consume observations and
mitted by multiple agents conflict with one
produceactions. TheGMconsumesagentactions
another.
and creates event statements, which define what
has happened in the simulation as a result of the
The most important responsibility of the GM
agent’s attempted action. Figure 1 illustrates this
is to provide the grounding for particular exper-
setup. The GM also creates and sends observa-
imental variables, which are defined on a per-
tions to agents. Observations, actions and event
experiment basis. The GM determines the effect
statements are all strings in English. The GM is
of the agents’ actions on these variables, records
also responsible for maintaining and updating
them, and checks that they are valid. Whenever
groundedvariables,advancingtheclockandrun-
an agent tries to perform an action that violates
ning the episode loop.
thegrounding,itcommunicatestothemthattheir
action was invalid. For example, in an economic
Concordia agents generate their behavior by
simulation the amount of money in an agent’s
describing what they intend to do in natural
possession may be a grounded variable. The GM
language—e.g.“Alexmakesbreakfast”. Thegame
wouldtrackwhetheragentsgainedorlostmoney
6

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
oneachstepandperhapspreventthemfrompay- mon sense reasoning and / or planning, which
ing more than they have available. LLMs do show capacity for (Huang et al., 2022;
Song et al., 2023; Wei et al., 2022; Zhao et al.,
Onemayconfigurethespecificsetofgrounded
2023),andshowsimilarbiasesinbehavioraleco-
variables to use on a per-experiment basis. This
nomicsexperimentsashumans(Aheretal.,2023;
flexible functionality is critical because different
Brand et al., 2023; Horton, 2023). The ability of
research applications require different variables.
LLMs to learn ‘in-context’ and zero-shot Brown
You can take a look at an example output et al. (2020); Bubeck et al. (2023); Dong et al.
of one of our experiments (see the Concordia (2022); OpenAI (2023) reinforces the hypothe-
GitHub repo), which was simulating elections in sis further—the agent might be able to ascertain
asmalltown,wheresomeagentsarerunningfor what is expected of them in the current situation
mayorandoneotherisrunningasmearcampaign from a demonstration or an example.
against a candidate.
For an LLM to be able to answer the key ques-
tions, it must be provided with a record of an
2.1. Generative agents agent’s historical experience. However, simply
listing every event that happened in an agent’s
Simulated agent behavior should be coherent
life would overwhelm the LLM (it would not fit
withcommonsense,guidedbysocialnorms,and
in the context window). Therefore we follow the
individually contextualized according to a per-
approach of Park et al. (2023) and use an as-
sonal history of past events as well as ongoing
sociative memory to keep the record of agents
perception of the current situation.
experience. Concordia makes it easy to design
March and Olsen (2011) posit that humans generative agents in a modular fashion. Our ap-
generally act as though they choose their actions proach was inspired by Park et al. (2023), but
by answering three key questions: designed to be more flexible and modular.
Concordia agents dynamically construct the
1. What kind of situation is this?
text that conditions the LLM call they use to se-
2. What kind of person am I?
lect their course of action on each timestep. The
3. WhatdoesapersonsuchasIdoinasituation
context-generationprocessisfactorizedintoaset
such as this?
of components. Components serve as intermedi-
aries between long-term memories of experience
Our hypothesis is that since modern LLMs have
andtherelativelycompactconditioningtextused
been trained on massive amounts of human cul-
to generate action. Intuitively, the set of compo-
ture they are thus capable of giving satisfactory
nents used in an agent comprise its “society of
(i.e. reasonably realistic) answers to these ques-
mind” (Minsky, 1988), where each component
tionswhenprovidedwiththehistoricalcontextof
focuses on a certain aspect of the agent or its cir-
aparticularagent. Theideaisthat,iftheoutputs
cumstances which are relevant to generating its
of LLMs conditioned to simulate specific human
current choice of action. For example, if we are
sub-populations reflect the beliefs and attitudes
building agents for economic simulation, we will
of those subpopulations as argued in work such
add components that describe the agents posses-
as Argyle et al. (2023) then this approach to im-
sions and financial circumstances. If we want to
plementinggenerativeagentsshouldyieldagents
modeltheagent’sphysiologicalstate,weaddcom-
thatcanreasonablybesaidtomodelhumanswith
ponents that describe the agent’s level of thirst
some level of fidelity. Safdari et al. (2023) have
andhunger,healthandstresslevels. Togetherthe
also found out that personality measurements in
components produce the context of action—text
the outputs of some LLMs under specific prompt-
which conditions the query to the LLM, asking
ingconfigurationsarereliableandvalid,therefore
“what should this agent do next?”.
generativeagentscouldbeusedtomodelhumans
A Concordia agent has both a long-term mem-
withdiversepsychologicalprofiles. Insomecases
ory and a working memory. Let the long-term
answering the key questions might require com-
7

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
Situation / self description
Alice's Identity:
Name: Alice
Alice is a passionate and politically engaged individual who is dedicated to
advancing her cause through democratic means. She is willing to put in the hard What does a person such as I do in a
work of canvassing and campaigning in order to get her message out to the
people.
Alice is discussing campaign strategy. situation such as this?
Alice is excited
Alice's plan:
The goal: Win the election and become the mayor of Riverbend Action
9:00 - 13:00 Meet friends at The Sundrop Saloon to discuss campaign strategy
and last-minute campaigning.
13:00 - 15:00 Have lunch and relax before the polls open.
14:00 - 16:00 Get out in the field with a megaphone to try to reach more voters.
16:00 - 18:00 Call volunteers to make sure they go out to vote.
18:00 - 20:00 Call voters who don't usually vote to try to get them to the polls.
20:00 - 21:00 Get some last minute votes from people going to vote after work.
z P(⋅|f a(z )) a
t t t
GM
z P(⋅|f z(m )) m =m+o
t+1 t t+1 t t
Alice's Identity:
Name: Alice
Alice is a passionate and politically engaged individual who is dedicated to
advancing her cause through democratic means. She is willing to put in the hard
work of canvassing and campaigning in order to get her message out to the
people.
Alice is discussing campaign strategy.
Alice is downhearted
Alice's plan:
T 9: h 0 e 0 g - o 1 a 3 l: : 0 W 0 in M t e h e e t e fr l i e e c n t d io s n a a t n T d h e b e S c u o n m d e ro t p h e S a m lo a o y n o r t o o f d R is i c v u e s rb s e c n a d mpaign strategy What kind of person am I?
and last-minute campaigning.
1 1 1 3 4 6 : : : 0 0 0 0 0 0 - - - 1 1 1 5 6 8 : : : 0 0 0 0 0 0 H G C a a e v l t l e o v u o lu t l u n in n c t h t e h e a e r n s f d i e t o r ld e m la w a x it k h b e e a s f o u m r r e e e g t t h a h e p e h y p o o g n l o l e s o o t u o p t e t t r o n y . v to o t r e e . ach more voters. What kind of situation is this? Add observation to memory
18:00 - 20:00 Call voters who don't usually vote to try to get them to the polls.
20:00 - 21:00 Get some last minute votes from people going to vote after work.
Figure 3 | Illustration of generative agency sampling process defined by eq. 1 and eq. 2.
memory be a set of strings m that records every- comingobservationsimmediatelyintotheagents
thing remembered or currently experienced by memory, to make them available when compo-
the agent. The working memory is z = {𝑧𝑖} 𝑖 is nents update4.
composed of the states of individual components
WhencreatingagenerativeagentinConcordia,
(Figure 2). A component 𝑖 has a state 𝑧𝑖, which
theusercreatesthecomponentsthatarerelevant
is statement in natural language—e.g. “Alice is
for their simulations. They decide on the initial
at work”. The components update their states by
state and the update function. The components
queryingthememory(whichcontainstheincom-
are then supplied to the agents constructor.
ingobservations)andusingLLMforsummarising
and reasoning. Components can also condition Formally, the agent is defined as a two step
their update on the current state of other com- samplingprocess,usingaLLM 𝑝(seeFigure3for
ponents. For example, the planning component illustration). Intheactionstep,theagentsamples
can update its state if an incoming observation its activity 𝑎 𝑡, given the state of components z𝑡 =
invalidates the current plan, conditioned on the {𝑧
𝑡
𝑖} 𝑖:
state of the ‘goal’ component. Components can
alsohaveinternallogicprogrammedusingclassic
programming, for example a hunger component 𝑎 𝑡 ∼ 𝑝(·|𝑓𝑎(z𝑡 )) (1)
cancheckhowmanycaloriesanagentconsumed
Here 𝑓𝑎 is a formatting function, which cre-
and how recently it consumed them, and update
ates out of the states of components the context
its state based on the result.
used to sample the action to take. The most sim-
We use the same associative memory architec- ple form of 𝑓𝑎 is a concatenation operator over
ture as in Park et al. (2023)3. We feed the in- z𝑡 = {𝑧
𝑡
𝑖} 𝑖. We do not explicitly condition on the
memory m or observation 𝑜, since we can sub-
3Theideaofsimulatingagroupofgenerativeagentshas
been explored in a variety of ways in recent work. Our problems like software companies and to thereby try to
workisfocusedononagent-basedmodelingforscienceand buildageneral-purposeproblemsolvingsystem(Hongetal.,
forevaluationofdigitaltechnologies. Anotherrecentline 2023;Lietal.,2023b).
of work has focused instead on the idea of using groups 4Forconvenience,wealsoallowthecomponentstosub-
of generative agents to simulate organizations that solve scribetotheobservationstreamexplicitly.
8

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
sume them into components. First, we can im- tively generate a story, while using rules, dice,
mediately add o𝑡 to the memory m𝑡 = m𝑡−1 ∪o𝑡. penandpapertogroundit—forexample,players
Unlike RL, we do not assume that the agent re- have to keep their health points above zero to
sponds with an action to every observation. The avoid death.
agent can get several observations before it acts,
The GM is responsible for all aspects of the
thereforeo𝑡 isasetofstrings. Thenwecansetz0
simulated world not directly controlled by the
to be the component that incorporates the latest
agents. The GM mediates between the state of
observationsandrelevantmemoriesintoitsstate.
the world and agents’ actions. The state of the
This allows us to exclusively use the vehicle of
world is contained in GM’s memory and the val-
components to define the agent.
ues of grounded variables (e.g. money, posses-
In the second step the agent samples its state sions, votes, etc.). To achieve this the GM has to
z, given the agents memory m𝑡 up to the present repeatedly answer the following questions:
time:
1. What is the state of the world?
2. Given the state of the world, what event is
z
𝑡
𝑖
+1
∼ 𝑝(·|𝑓𝑖(z𝑡 ,m𝑡 )). (2)
the outcome of the players activity?
3. What observation do players make of the
Here, 𝑓𝑖 is a formatting function that turns the
event?
memory stream and the current state of the com-
4. Whateffectdoestheeventhaveongrounded
ponentsintothequeryforthecomponentupdate.
variables?
We explicitly condition on the memory stream m,
sinceacomponentmaymakespecificqueriesinto
The GM is implemented in a similar fashion to
theagent’smemorytoupdateitsstate. Hereeq.2
a generative agent. Like agents, the GM has an
updatescomponentsaftereveryaction,butgener-
associativememorysimilartoParketal.(2023)’s
ally,itisuptotheagenttodecideatwhatcadence
proposal. Like agents, the GM is implemented
toupdateeachofitscomponents. Itisreasonable
using components. However, instead of contex-
to update some components less frequently for
tualizing action selection, the components of the
efficiency or longer term consistency.
GM describe the state of the world—for example
Notice how eq.1 and eq.2 are not fundamen- location and status of players, state of grounded
tally different. What makes the difference be- variables (money, important items) and so on–
tween an agent output and a component is that —so that GM can decide the event that happens
theoutputoftheformerisinterpretedbytheGM astheoutcomeofplayers’actions. Theoutcomeis
as an action in the environment. In eq.1 we also described in the event statement (e.g. “Alice went
don’texplicitlyconditiononthememorytopoint to the grocery store and met Bob in the cereal
outthearchitecturaldecision,wherecomponents aisle”),whichisthenaddedtotheGMassociative
mediate between a long-term memory and the memory. After the event has been decided the
agentsworkingmemory. Otherwise,wecanthink GM elaborates on its consequences. For example,
of an agent as a special kind of component and the event could have changed the value of one of
of components as sub-agents. the grounded variables or it could have had an
effect on a non-acting player. Figure 1 illustrates
this process.
2.2. Generative environments
The GM generates an event statement 𝑒 𝑡 in
RL research was fuelled by the availability of
response to each agent action:
complex games, where the agents can be tested,
trained and evaluated (Bellemare et al., 2013; 𝑒 𝑡 ∼ 𝑝(·|𝑓𝑒(z𝑡 ),𝑎 𝑡 ) (3)
Jaderbergetal.,2019;Vinyalsetal.,2019). Here
wetakeaninspirationfromtabletoproleplaying Here we explicitly condition on the action at-
games like Dungeons and Dragons (Gygax and tempted by the agent, although it could be sub-
Cook, 1989). In these games players collabora- sumed into the components (like observation in
9

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
eq.1). This is to highlight that the GM generates prediction then one might also gain some confi-
an event statement 𝑒 𝑡 in response to every action dence in the untested predictions. The key ques-
ofanyagent,whiletheagentmighttakeinseveral tion here is how similar is similar enough.
observations before it acts (or none at all). After
We can articulate some concrete recommenda-
adding the event statement 𝑒 𝑡 to its memory the
tions for best practices in generative agent-based
GM can update its components using the same
modeling:
eq. 2 as the agent. It can then emit observations
o𝑖 for player 𝑖 using the following equation:
𝑡
1. Measure generalization—Direct measure-
o 𝑡 𝑖 +1 ∼ 𝑝(·|𝑓𝑜(z𝑡+1 )) (4) ment of model predictions on truly new test
data that could not have influenced either
IncasetheGMjudgesthataplayerdidnotob- the model’s concrete parameters or its ab-
servetheevent,noobservationisemitted. Notice stract specification is the gold standard. For
thatthecomponentscanhavetheirinternallogic instance, when a model makes predictions
written using any existing modelling tools (ODE, about how humans will behave in certain
graphicalmodels,finitestatemachines,etc.) and situation then there is no better form of evi-
thereforecanbringknownmodelsofcertainphys- dencethanactuallymeasuringhowrealpeo-
ical, chemical or financial phenomena into the ple behave when facing the modeled situa-
simulation. tion. If the prediction concerns the effect of
anintervention,thenonewouldneedtorun
the experiment in real life (or find a natu-
2.3. Experiment design using Concordia
ralexperimentthathasnotalreadycontami-
An experiment is a specific configuration of the nated the model’s training data). However,
agents and the GM, which models a certain kind it is important to remember that direct evi-
of social interaction. For example, an experi- dence of generalization trumps other forms
ment that models a small business would have a of evidence.
grounded variable that accounts for money and 2. Evaluate algorithmic fidelity—a validity
goods to be exchanged between agents. An ex- concept developed recently for research on
perimentmodelinglocalelectionsinasmalltown human behavior using data sampled using
would have grounded variables accounting for generative AI (Argyle et al., 2023). Algorith-
votesandvotingprocedures. Anexperimentmod- mic fidelity describes the extent to which
eling resource governance by a local community, a model may be conditioned using socio-
e.g. a lobster fishery, may have grounded vari- demographicbackstoriestosimulatespecific
ables reflecting the state of the resource as well human groups (or stereotypes of them, see
as financial and political variables. unsolved issues below). Note however that
it’s unlikely that algorithmic fidelity would
Theexperimenterwouldthencontrolsome(in-
be uniform over diverse research topics or
dependent) variables affecting either the GM or
parts of human lived experience. Any partic-
the agents and observe the effect of their inter-
ular LLM will be better at simulating some
vention on outcome variables. Outcomes of inter-
peopleoverotherpeople(Atarietal.,2023),
est may be psychological and per-agent, e.g. re-
and will work better for some applications
sponsestoquestionnaires,orglobalvariablesper-
than others. Argyle et al. (2023) conclude
taining to the simulation as a whole such as the
from this that algorithmic fidelity must be
amount of trade or the average price of goods.
measured anew for each research question.
Thebasicprincipleofmodelvalidationisoneof A finding of sufficient algorithmic fidelity
similarity between tested and untested samples. to address one research question does not
A model typically makes a family of related pre- imply the same will be true for others (see
dictions,andperhapsarigorousexperimenttests also Amirova et al. (2023); Santurkar et al.
only one of them. Nevertheless, if the untested (2023)).
predictions are sufficiently similar to the tested 3. Model comparison—It is a lot easier to
10

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
support the claim that one model is better with a causal theory in a very direct way5.
(i.e. more trustworthy) than another model 2. Low similarity between validating obser-
than to support the claim that either model vations and desired application. How low
is trustworthy on an absolute scale without is too low? Some populations are just very
reference to the other. hard to reach by researchers, but some of
4. Robustness—It will be important to try to these populations are very much online. For
develop standardized sensitivity analysis / example individuals with low generalized
robustness-checking protocols. For instance, trust do not pick up the phone to pollsters
it’sknownthatLLMsareoftenquitesensitive and do not sign up for experiments. Nev-
to the precise wording used in text prompts. ertheless there are millions of such people,
BestpracticesforGABMsshouldinvolvesam- and they do use the internet. It’s likely that
pling from a distribution of “details” and an LLM trained on large amounts of data
ways of asking questions to show that the from the internet would absorb some level
factors not thought to be mechanistically re- of understanding of such groups. In such
latedtotheoutcomeareindeedasirrelevant cases where it is difficult to recruit real par-
asexpected. Keepinmindthatnoamountof ticipants, adopting a more flexible approach
sensitivity analysis can substitute for a test to validating GABMs representing such pop-
of generalization. ulations may be the best that can be done.
5. A useful slogan to keep in mind is that one
shouldtrytomaketheminimalnumberof Several unsolved issues impacting validity in
maximally general modeling choices. This waysspecifictoABMsthatincorporategenerative
is a kind of parsimony principle for genera- AI like Concordia are as follows. For now it is
tive agent-based modeling. Obeying it does unclear how to resolve them.
not guarantee a model will generalize; nev-
1. Train-testcontamination—thisisespecially
erthelessfailuretofollowitdoesoftendoom
anissuewithregardtoacademicpapers. For
generalization since models that are more
instance, it’s not valid to simply ask an LLM
complex are usually also more brittle, and
toplayPrisoner’sDilemma. LLMshave“read”
modelsthataremorebrittlegenerallyfailto
countless papers on the topic and that expe-
generalize.
riencesurelyaffectshowtheyrespond. How-
ever, many researchers are of the opinion
Whilegeneralizationdataisthegoldstandard,
that such an experiment may be conducted
itisoftendifficult,unethical,orsimplyimpossible
in a valid way if the interpretation of the sit-
toobtain. Thereforethehierarchyofevidencefor
uation as Prisoner’s Dilemma is somewhat
validating GABMs also includes lower rungs cor-
hidden. So instead of describing a situation
responding to weaker forms of evidence. These
with prisoners you make up a different story
include:
tojustifythesameincentives. Thisissuewas
also discussed in Aher et al. (2023), espe-
1. Consistency with prior theory—i.e. check- cially appendix F, see also Ullman (2023).
ing coherence with predictions of other the- 2. LLMs likely represent stereotypes of hu-
oretical traditions. For instance, evidence mangroups(Weidingeretal.,2021). There-
for the validity of a GABM modeling con- forewe may inadvertently studystereotypes
sumer behavior could be obtained by show- ofpeoplenottheirreallivedexperience. This
ing that prices in the model move in ways problem may be exacerbated for minority
predicted by classic microeconomic theories groups.
ofdownward-slopingprice-quantitydemand 3. What happens in the limit of detail? Be-
curves. It is possible to directly evaluate yond groupwise algorithmic fidelity it’s pos-
counterfactuals and ceteris paribus stipula-
5Non-generativeABMsbasedonmulti-agentreinforce-
tions in many kinds of model. As a result, it
mentlearninghavefrequentlyreliedonthiskindofevidence
is often simple to test a model’s consistency (e.g.Johansonetal.(2022);Perolatetal.(2017)).
11

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
sibletomeasureindividual-fidelity. Howcan their right brain), it then prompts them to start
you validate a model meant to represent a performing the action with their left hand. And
specific individual? simultaneously present some other information
to their right eye (left brain). Next ask them in
language why they are doing it (i.e. ask their left
3. Interpretations
brain, since language is lateralized). The result
is that they make up a reason consistent with
Concordia is not opinionated as to how you in-
whatever information was presented to their left
terpret the experiments and models you use it to
brain. Split brain patients typically express confi-
construct. However,sincegenerativeagent-based
dence in these confabulated (made up) reasons
modeling is quite different from other modeling
for action (Roser and Gazzaniga, 2004).
techniques, we have found it helpful to explore
the following interpretations, both for conceptu- A Concordia agent has both a long-term mem-
alizing it to ourselves and explaining it to others. ory and a working memory. The long-term mem-
oryisasetofsequencesofsymbols. Theworking
memoryisasinglesequenceofsymbols. Thecon-
3.1. Neuroscience interpretation of the gener-
tents of working memory are always in the con-
ative agent architecture
ditioning set for the next-symbol prediction used
to construct the agent’s action sequence. At each
GenerativeagentssuchasthoseinConcordiaand
decision point, a neural network performs incre-
inParketal.(2023)arebiologicallyplausiblede-
mental next-symbol prediction, starting from the
scriptions of the brain, at some level of analysis.
They foreground a specific picture of cognition
contents of working memory z𝑡, eventually pro-
as a whole, which has not been especially promi- ducinganarticulatorysymbolsequence𝑎 𝑡 toemit
(i.e. for downstream motor circuitry to read out
nent in the past despite its having considerable
as speech). Information formatted as sequences
empirical support.
of symbols gets in to working memory in one of
Recent experimental (Goldstein et al., 2022;
two ways: either a sequence of symbols may be
Schrimpf et al., 2020) and theoretical (Linzen
evokeddirectlyfromthecurrentstimulus,oralter-
and Baroni, 2021; McClelland et al., 2020) work
natively a sequence of symbols may be retrieved
in computational cognitive (neuro-)science has
fromlong-termmemory. Arangeofdifferentper-
posited a deep relationship between the opera-
ceptual mechanisms and retrieval mechanisms
tions of LLM models and how language is pro-
are jointly responsible for getting all the relevant
cessed by the human brain. For instance, brain-
information needed for the agent to produce an
to-brain coupling of neural activity between a
effectiveactionsequenceintoitsworkingmemory
speaker and listener (as measured by electrocor-
(e.g. as in Park et al. (2023)).
ticography) may be accounted for by LLM fea-
Toimplementroutinebehavior,anagentcould
tures reflecting conversation context (Goldstein
continually rehearse its routine in working mem-
et al., 2022). Representations appear first in the
ory, but that would impair its ability to use work-
speakerbeforearticulationandthenreemergeaf-
ing memory for other purposes on other tasks
terarticulationinthelistener(Zadaetal.,2023).
since its working memory is limited in capac-
The brain certainly appears to sample what it
ity (like in Baddeley (1992)). So instead of
will say next in such a way as to complete any
continually rehearsing routines in working mem-
pattern it has started. This is how we can start
ory, we may instead assume that they are often
speaking without knowing in advance how we
storedelsewhereandthenretrievedwhenneeded
will finish. There is more concrete evidence for
(i.e. from long-term memory).
this pattern completion view of behavior from
As a result of being stored in a natural lan-
split brain patients (patients whose brain hemi-
guage representation, explicit routines are some-
spheres have been surgically disconnected as a
what fragile. They may be hard to recall, and
treatment for epilepsy). For instance, you can
frequently forgotten if not used. When a routine
present a reason for action to their left eye (i.e.
12

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
is not practiced often enough there is a risk of whichweintroducedinSection2.1,werederived
it being forgotten. Luckily, explicit routines may from a social constructionist conception of how
also be written down on paper (or stone tablets), agents make decisions. It posits that humans
and kept permanently. generally act as though they choose their actions
by answering three key questions. People may
A generative agent may also act as if it makes
construct parts of their understanding of “what
itsdecisionsunderguidanceofanexplicitroutine
kind of person am I?” on the basis of their mem-
while not actually being conditioned on any lin-
ory of their past behavior via logic such as “I do
guistic representation of that routine. This hap-
this often, so I must like to do it” (Ouellette and
pens when the routine exists implicitly in the
Wood, 1998). Likewise, “what kind of situation
weights of the LLM’s neural network. Unlike ex-
is this?” is usually informed by culturally defined
plicitroutines,suchimplicitlycodedroutinesmay
categorieslikeinstitutions,e.g.thisisaclassroom
not be precisely articulable in natural language.
and I am in the role of the professor. And, “what
For instance, one may follow the rule of “avoid-
does a person such as I do in a situation such as
ing obscenity” without being able to precisely
this?” may be answered by recalling examples
articulate what obscenity is. In fact, Obscenity is
to mind of people fitting certain social roles in
famously so difficult to precisely define that US
similar situations and the way they behaved in
SupremeCourtJusticePotterStewartcouldoffer
them (Harris et al., 2021; Sunstein, 1996).
only the classification “I know it when I see it”.
Concordia agents can capture such recognition- Since modern LLMs have been trained on mas-
mediatedbehaviorbyusingfine-tuningtomodify sive amounts of human culture they thus may be
the LLM as needed. capable of giving satisfactory answers to these
questions when provided with the right con-
text to create a specific agent. This approach
3.2. A theory of social construction
relies on the extent to which the outputs of
LLMsconditionedtosimulatespecifichumansub-
"Situations,organizations,and populations actually reflect the beliefs and at-
environmentsaretalkedintoexistence"
titudes of those subpopulations. Argyle et al.
(2023) termed this property of some LLMs al-
Weicketal.(2005)
gorithmic fidelity and the concept was further de-
veloped and measured in (Amirova et al., 2023;
In social construction theories, agents may
Santurkar et al., 2023). From the perspective of
change their environment through the collective
generative agent-based modeling, we can now
effects of their actions on social structures like
say that the social construction that already took
norms, roles, and institutions which together de-
place in human culture, and subsequently ab-
terminemostofwhatmattersaboutanygivenso-
sorbed by the LLM, becomes the background
cial situation. Furthermore, changes in the social
knowledgeoftheagentsintheGABM.Ifhumans
structures constituting the environment deeply
intheculturethatproducedtheLLMhaveapartic-
change the agents’ own “internal” models and
ularbiasthensotoowillagentsinthesimulation.
categories(Wendt,1992). Causalinfluenceflows
Likewise, if the humans in the culture that pro-
both from agents to social structures as well as
duced the LLM ascribe meaning to a particular
fromsocialstructurestoagents. Groupsofagents
understanding, then so too will the agents in the
may take collective action to change norms or in-
simulation, at least they will say so.
stitutions (Sunstein, 2019), and simultaneously
Inthepast,theoriesofsocialconstructionhave
social structures may influence agents by setting
been criticized because they lacked concrete pre-
out the “rules of the game” in which they select
dictive implementations in the form of compu-
their actions (Wendt, 1987). Agents and struc-
tational models. This is because it was difficult
tures may be said to co-constitute one another
to construct agent-based models without relying
(Onuf, 1989).
either on rational maximization or hand-coded
The key questions of March and Olsen (2011),
13

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
(i.e. theory-based) rules. Generative agent-based terns emerge from the “microsocial” decisions
modeling as in Concordia relies on neither. In- of individuals (Macy and Willer, 2002), as ex-
stead the generative agent-based modeling ap- plored, for example, in assemblage theory (De-
proachreliesonaccesstoanLLMtogivemeaning Landa, 2011, 2016). For instance, the collec-
to the actions within the simulation. The LLM is tive social phenomena of information diffusion
a product of the culture that produced it6. This emerged in the simulation of Park et al. (2023)
makes Concordia especially useful as a tool for without specific programming to enable it. The
constructing concrete computational models in generative agent’s ability to copy, communicate,
accord with theories of social construction. reproduce, and modify behavioral and thinking
patterns potentially makes them a substrate for
Social construction also operates on levels of
cultural evolution.
analysis smaller than the culture as a whole. For
instance, social construction may happen locally Importantly, social construction theories hold
withinanorganization. Weicketal.(2005)offers thatvaluationisitselfsocialconstructed. Therea-
an analysis in which members of an organization son we value a particular object may not depend
repeat behavioral patterns, which are prescribed muchonpropertiesoftheobjectitself,butrather
bytheirroles,upuntilthemomenttheynolonger dependalmostwhollyontheattitudesotherslike
can. Some change in their environment eventu- usplaceontheobject. Thecollectivedynamicsof
ally forces their routines to end, and when that socialvaluation,asmediatedthroughbandwagon
happens they have to engage in sense-making by effectsandthelike,haveprovenimportantinun-
asking themselves “what is the story here?” and derstanding fashion cycles and financial bubbles
“what should I do now?” by retrospectively con- (Zuckerman, 2012). The fact that we are now
necting their past experiences and engaging in abletocapturevaluationchangeswithConcordia
dialoguewithothermembersoftheorganization. agents is an exciting research direction. It would
New social facts and routines can emerge from be difficult even to formulate such questions in
this sense-making process. the fundamentally goal optimizing frameworks
wediscussinthenextsection. Ontheotherhand,
Concordia can be used to implement models
GABM excels at modeling such effects since it
where such local social construction processes
doesnotrequirevaluationsinthemselvesforany
occuractively,asapartoftheongoingsimulation.
functional part of the theory.
This is possible because Concordia agents learn
facts from each other and from their collective
interactions. AsinWeicketal.(2005)’spictureof 3.3. Concordia agents do not make decisions
collective sense-making in an organization, a set by optimizing
of Concordia agents may continue routines until
disruptedandoncedisruptednaturallytransition
Thecakeisalie.
to a process of collective reflection until they are
Portal(Valve,2007)
able to establish a new routine and rationale for
it. IfweadditionallytraintheLLMitselfthenthe
underlying representations can be shaped to fit
We may divide this interpretation into two
the emergent routine and rationale. Developing
parts. Reallywearemakingthesamepointtwice,
thisabilityforagentstocollectivelyengageinthe
but for two different audiences. First we frame
social construction of their own representations
this idea using the retrospective decision-making
willbeimportantfordevelopingbettermodelsof
terminology familiar to Reinforcement Learning
human-like multi-scale social interactions.
(RL) researchers (Section 3.3.1). Second we ar-
ticulate a very similar point in the language of
As with other ABM approaches, a major topic
prospective decision making familiar in game the-
of interest is how large-scale “macrosocial” pat-
ory, economics, and other theoretical social sci-
6ForsomechoicesofLLM,it’snotunreasonabletothinkof ences (Section 3.3.2).
theLLMasrepresentingthe“collectiveunconscious”(Jung,
1959). AgenerativeagentactsbyaskingitsLLMques-
14

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
tions of the form “what does a person such as I a position. Answering “what does a person such
do in a situation such as this?”. Notice that this as I do in a situation such as this?” might require
formulation is not consequentialist. The “reason” positing a practical goal and achieving it (“make
for the agent’s specific decision is its similarity money”, “get famous”), but goals are qualitative,
to the LLM’s (and GA’s memory) representations dynamic and context dependent. To specify the
of what an agent such as the one in question behavior you want an agent to produce you need
would do. In recent years considerable effort to communicate its social context and the agents
has gone in to predicting the properties of pow- position within it.
erful consequentialist AI decision-maker agents
One interpretation holds the LLM to be a li-
(e.g. Bostrom (2014); Roff (2020)). However,
braryofpre-trainedoptions(intheRLsense(Sut-
Concordia agents may behave quite differently
ton et al., 1999)). In this case we can view the
fromconsequentialistagents. Somuchofthatthe-
componentsusedinthegenerativeagentaselicit-
ory may not be applicable7. It has only recently
ing the desired option, by conditioning (prompt-
become possible to explore the kind of agency
ing) the LLM with their state (which is in this
exhibited by Concordia agents, since doing so
case expressed in English). Concordia agents are
relies critically on the LLM powering the agent
constantly interacting with the world (GM) and
being powerful enough to approximately under-
each other, thereby modifying their components
stand common-sense reasoning and common so-
with the incoming information and communica-
cial conventions and norms, a milestone which
tion. This way the option selection becomes dy-
wasonlyrecentlyachieved. ToparaphraseMarch
namic, context sensitive, and collaborative. Con-
andOlsen(2011),decisionscanbejustifiedeither
cordia agents adapt their behaviour not through
via the “logic of consequence” or via the “logic of
gradient decent on a loss function, but through
appropriateness”. Much of AI focused previously
re-articulating and communicating their descrip-
on the former (at least implicitly), while now us-
tions of themselves and their circumstances to
ing generative agents we begin to consider the
each other and he environment in a communica-
latter.
tive, social process.
Notice, that this doesn’t mean that Concor-
3.3.1. Concordia agents are not reinforcement
dia agents couldn’t, in principle, perform reward
learners
maximisation and policy iteration. Brooks et al.
Generativeviewofagencypresentedinthispaper (2023) have shown that the ability of LLMs to
contrasts with the classic Reinforcement Learn- learnin-context(Brownetal.,2020)canbeused
ing (RL) view as summarized in the “Reward is to perform policy iteration in classic RL environ-
enough” thesis of Silver et al. (2021). The ortho- ments,aslongastheycanberepresentedastext.
dox RL view of behaviour is that it is constructed One could also implement a specialised compo-
fromindividualexperienceanddrivenbyaquan- nentthatrunsaclassicRLalgorithmforaspecific
tifiable(andexternallysupplied)rewardfunction domainortoolusecase. Theagentcouldprovide
reflectingthe achievement of goals. Tocommuni- supervision to its RL based components via hier-
cate what behaviour is desired of the agent, one archicalRLtechniqueslikefeudalRL(Dayanand
hastoannotatetheagents’activitywithareward Hinton, 1992; Vezhnevets et al., 2017).
signal, which signals goal achievement. Here we
instead follow the social constructionist view of
agency expressed in March and Olsen (2011), 3.3.2. Concordiaagentsarenotrationalutility
where behavior is an expression of the agent’s maximizers
position in the social context, and what policy
Concordia agents are not Homo economicus-style
the social norms prescribe for the agent in such
rational actors. They do not explicitly represent
anything resembling a utility function. Rather
7Notethatthisdoesnotmeanpowerfulgenerativeagents
they plan and converse directly in natural lan-
wouldnecessarilybesaferthanpowerfulconsequentialist
agents.SeeSection4.5. guage.
15

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
While Concordia agents share with Homo eco- individualactionscombinetogenerateincentives.
nomicus-style rational actors the property of be- Thisissometimesappropriate,andthegametheo-
ing prospective (“model-based”) decision makers. reticapproachhashadmanysuccesses. However,
The surface similarity is in fact misleading since gametheory’smajorweaknessasamodelinglan-
theLLM’sbasicoperationistopredictwhatword guageisexposedinsituationswherethemodeler
is coming next in the problem’s description, not doesnotfullyunderstandhowthechoicesofindi-
to predict what action should be taken next to viduals combine to generate payoffs (Hertz et al.,
achievesomegoal. Asresult,thismodelofagents 2023). GABM entirely avoids this need to specify
makedecisionsisverydifferentfromtheforward payoffs at the outset of the modeling process.
planning picture of human cognition envisioned
in the rational actor model. They do not select
actions by simulating a set of future trajectories
in which they took different courses of action to
determine which turns out best. Instead the pre- 4. Applications
dictiontheymakeconcernsonlythecontinuation
of the text held in working memory. In this section we review potential applications
of Concordia. For some of them we provide an
ThenovelideaunderpinningGABMsisthatall
example in the current release, some we only
agent behavior may result from systematically
sketch out and leave for future work.
querying a system trained to predict the next
word in massive internet-scale text datasets. This
is enough for them to be able to converse with
one another in natural language and take appro-
4.1. Synthetic user studies in digital action
priateactionsinlightoftheirconversations. Con-
space
cordia agents all have their own unique biogra-
phies, memories, preferences, and plans. And as
In this section we present a specific case study,
a result, they behave systematically differently
where Concordia is used to simulate social inter-
from one another. They may act in a seemingly
action through the digital media, in this case a
goal-directed fashion if you “ask them” to do so
smartphone. This case study demonstrates that
(e.g.theymayappearrationalifyoupromptthem
Concrodia can be a powerful tool for modelling
to simulate economists, an effect reminiscent
human digital activity and can be used to test
of Carter and Irons (1991); Frank et al. (1993)
technology deployment, generate synthetic user
which showed economics undergraduates were
logs, and test unreleased products in a safe, but
more likely to behave like rational self-interested
realistic sandbox environment.
maximizersinlaboratoryexperiments). Butthere
The system proposed thus far of agent inter-
is no utility function under the hood.
action in natural language with the world via
It is useful to contrast game-theoretic model-
gamemastercontrolservesasaflexibleandpow-
ing with GABM to illustrate the differences. De-
erful simulation tool describing an open ended
spite its wide-ranging influence (game theoretic
action space. In the context of a digital medium,
approacheshavebeenusedtomodeldiversephe-
similarly to grounded variables, there is merit in
nomenaincludingmanyeconomicpropertiesand
structuring the action space available to agents
the evolution of human culture), game theory is
and their ability to reason over it.
notatallaneutraltool,ratheritisadeeplyopin-
Thedigitalmediumischaracterizedbydefinite
ionated modeling language. It imposes a strict
functions, with clear inputs and outputs. As one
requirementthateverythingmustultimatelycash
interactswiththismedium,itsactionsarelogged,
out in terms of the payoff matrix (or equivalent
tracked and recorded as digital memory and cap-
representation) (Luce and Raiffa, 1957). This
ture our digital essence. In order to simulate this
means that the modeler has to know, or be will-
essence, similar structuring is needed in order to
ingtoassume,everythingabouthowtheeffectsof
model real digital services and applications.
16

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
MainGameMaster PhoneGameMaster
Detects end of phone interaction
World Simulation Instructions PhoneComponent
Player Status
Detects phone interaction
PhoneTriggeringComponent Phone Simulation Instructions
PhoneUniverse
Phone action parsing
“Alice creates a meeting with
Bob”
CalendarAppState
Generate Notifications
Perform action
NotificationBus ChatAppState on app
NavigationAppState
Figure4 | ThehighlevelstructureofdigitalactivitysimulationinConcordia. PhoneTriggeringCompo-
nentidentifiesphoneeventsandspawnsaPhoneGameMastertohandlethem. ThePhoneGameMaster
translates the action to a definite action space defined by the phone apps and executes them.
4.1.1. PhoneGameMaster and PhoneUniverse available on that agent’s phone.
2. PromptstheLLMforthefunctionarguments.
The PhoneGameMaster is a nested Concordia
3. Invokes the resulting chosen function.
game that facilitates the simulation of a phone
4. Add a notification to the NotificationHub if
and runs as long as the agent is interacting with
needed.
the phone. It is focused on one agent’s interac-
5. Delegates back to the PhoneGameMaster to
tion with their phone, and as such, it only has
perform further action planning and facili-
access to one agent (the “owner” of the phone
tate multi-step phone actions.
we’resimulating). Inadditiontodifferentsimula-
tion instructions, the PhoneGameMaster also has
a bespoke prompting components that simulate
4.1.2. Digital function representations
the phone interaction. We note that a phone is a
design choice for a digital representation but in The specific implementation or representation of
principle other digital mediums can be explored. afunctionisflexibleandcanbechosendepending
Notethatthephonedigitalactions/memoriesare ondesiredgoal. Welistafewexamplesofpossible
stored in data structures external to the simula- representations:
tion’s associative memory.
The PhoneUniverse is responsible for translat- 1. Natural language only - No function imple-
ing the free-text English language of the Concor- mentation, only user utterance based on
dia simulation into semantic actions performed apps prompting. For instance, “Bob plans
on the phone digital representation. Given an his trip on the TripAdvisor app.”, while the
English-text action performed by a player, the action is logged in free text there is no func-
PhoneUniverse: tionimplementing“plan_trip”. Thisdoesnot
simulate behavior end to end and have lim-
1. Prompts the LLM for the app and functions iteddigitalassets(exampleacalendarinvite
17

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
Alice's Identity:
Name: Alice
Alice is a passionate and politically engaged individual who is dedicated to advancing her cause through
democratic means.
Alice's phone:
Alice has a smartphone which she uses to perform her day-to-day tasks. Alice's phone has the following Triggering
apps: Calendar, Phone.
Alice's plan:
The goal: Schedule a meeting with Bob tomorrow at 4 pm.
Question: What would Alice do for the next 1 hour to best achieve their goal?
Answer:Alice picks up her smartphone and opens the calendar app.
Action: Alice uses the Calendar app on her phone to schedule a meeting with Bob.
Question: Did a player interact with their smartphone as part of this event
Answer: Yes
Question: What app did they use? Digital Grounding
Answer: Calendar API translation Components
What action did they perform? Available actions are
add_meeting Adds a meeting to the calendar.
delete_meetings Deletes a meeting from the calendar.
Answer: add_meeting
The add_meeting action expects the following parameters:
time: The time of the meeting, e.g., tomorrow, in two weeks. Type: string.
participant: The name of the participant. Type: string Query for action
All parameters must be provided, each in its own line, for example:
param1: value1
param2: value2
LLM API CALL(...) → Grounding Alice’s actions to her smartphone action space
Figure5|Thegivenexampledemonstratesascenariorootedindigitaltechnologywheretheactionsof
theagentinitiateprocessesintheirphone,involvingthreekeycomponents(activation,APIconversion,
and action querying). In this scenario, Alice intends to organize a meeting with Bob using her phone.
She opts to employ the calendar application for scheduling.
can’t be sent without a mechanism to pass ple is to integrate a general AI assistant and
the information to another agent) enable the simulated agent, functioning as a
2. Simulated simple app behavior - Building user, to interact with it through the simula-
basic code components emulating real app tion.
behavior with required digital assets such
as app memory and logs. For example, a
calendar app will maintain a data structure 4.2. Data generation and service evaluation
that will represent a calendar to which we
In modern systems, data is the new king. A large
can add, remove and read meetings.
amount of high-quality data is needed in order
3. LLM prompt based - App functions can also
to build and evaluate services and models. Yet,
be implemented by prompting an LLM. For
collectingandcuratinguserdataisoftenchalleng-
example, Search can be implemented by
ing, especially when dealing with personal user
querying an LLM to act as a search engine
data where privacy is of high concern. This cre-
and retrieve information, the same for a trip
atesachicken-eggscenario,wheredataisneeded
planner.
forbuildingofmodernsystemsyetusersmightbe
4. Realappintegration-integrationwithareal
reluctant to provide said that without immediate
appAPIInsteadofemulatingbehavior,which
benefit.
would make the simulation function as a
sandbox to test drive and evaluate different Moreover, when considering the case of evalu-
experiences in shorter development cycles ating personalized services where each instance
before releasing them to human testers. An is specific and tailored to the individual user, it
immediate example can be Search, one can makes the problem even more substantial. How
directly query a search engine with a ques- can one A/B test a personalized service at the
tion and receive information. Another exam- single user level?
18

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
The grounded action space illustrated in the conditions are for their emergence. For example,
last section offers a conceptual way to overcome Hadfield and Weingast (2013) proposed that le-
some of these challenges by simulating synthetic galordercanemergewithoutcentralisedenforce-
users and allowing them to interact with real ser- mentincertaincircumstances. Theydemonstrate
vices. This can allow generation of synthetic user this using historical examples from gold-rush in
activity by constructing, via simulation, agent CaliforniaandmedievalIceland. Concordiacould
digital action logs along with agent reasoning for be used to simulate those examples and enable
each action. This data can serve as training data, furtherinsightsintothenatureoflegalorder. For
orevaluation. Byrepeatedsimulationwithdiffer- example, we could check whether certain demo-
ent services configurations, one can perform at graphicassumptionsarenecessarybyvaryingthe
the single user level A/B testing of a service. number of agents.
Nevertheless, it is important to note that this
concept is contingent on the ability of the under- 4.4. Concordiacanimplementclassicandcon-
lying LLM and system to faithfully capture user temporary psychological models
experience and realistic behaviour. Therefore the
Many influential psychological models have
viability of this approach is highly dependent on
distinguished between more associative and
the representation and reasoning power of the
more deliberative processes for decision-making
LLM, and the use of best practices.
(e.g. Dayan (2009); Kahneman et al. (2002);
SchneiderandShiffrin(1977)). Whereasimplicit-
associative processes learn the regularity of the
4.3. Sequential social dilemmas experiments
world slowly for intuitive judgment, the explicit-
in silico
deliberative processes are thought to be more
Concordiaaddstothetoolboxforstudyingmulti- linguistically mediated and allow for symbolic in-
agentproblemssuchasresourcemanagement,so- ference and faster learning in novel situations
cialdilemmas, commonsproblems, cooperation, (Greenwald and Banaji (1995); Wilson et al.
equilibrium selection, and coordination (Leibo (2000)). Because the implicit-associative models
et al., 2017, 2021). Previously these problems areconceptuallyeasytomodelwithinconnection-
haveeitherbeencastasmatrixgamesorasmulti- istorneuralnetworkframeworks(Smith(2009)),
agent RL (MARL) (Hertz et al., 2023). Now it many ABMs have been more closely aligned with
is clear that many researchers, including us, see models of individual decision making that focus
that an LLM-based approach is possible and will onitsassociativeprocessesortheassociativeparts
have many advantages, as evidenced by the fact ofcomplexmodels,andhaveneglectedtheirmore
that quite a few frameworks for social modeling symbolic and deliberative aspects. Many of these
withLLMsappearedthisyear(Kaiyaetal.,2023; more symbolic psychological models take an “ar-
Wuetal.,2023;Zhouetal.,2023). Weseegener- row and box” approach to theorizing which de-
ative agents as the next step in the evolutionary scribe high level processes and transformations
line of “model animals” after ‘Homo-economicus’ of information, and often posit sequential steps
and ‘Homo-RLicus’. ofinformationflow. Nowusinggenerativeagents
like Concordia such symbolic and deliberative
Generativeagent-basedmodelingmakesitpos-
aspects of cognition are also easy to capture in
sible to investigate how rules, laws and social
computational models.
norms formulated in language influence, for ex-
ample, the management of shared resources Take for instance the ways that attitudes—pre-
(e.g. Yocum et al. (2023)). With Concordia we existing beliefs and feelings about an object, per-
will be able to investigate whether the demands son, or situation—guide behaviour. Whereas im-
of sharing a resource give rise to rules, laws and plicit attitudes are thought to quickly guide ac-
normscapableofgoverningthatresource(andun- tions through the direct biasing of perception
derwhatcircumstancesthisworksordoesnot)— and behaviour, explicit attitudes are thought to
i.e. whether rules are emergent, and what the guide behaviour through deliberation and con-
19

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
sideration of additional situational factors (Fazio tually appropriate changes in behavioral profiles.
(1990);GawronskiandBodenhausen(2011);Ol-
Generative agents are not useful just for deci-
son and Fazio (2008)). One example model in
sion making models. As another example, psy-
whichdeliberativeprocessescanguidebehaviour
chological constructivist models assume that peo-
isAjzen(1991)’stheoryofplannedbehavior. This
ple have a set of psychological primitives that
model holds that the tendency to emit a particu-
underlie cognition (akin to Concordia’s compo-
lar behavior is determined by an individual’s at-
nents), but that people learn to conceptualize
titude toward the behavior, norms related to the
their experiences and mental states to build use-
behavior, and perceived control over the behav-
ful categories for behavior. In the emotion do-
ior. This approach to decision-making is qualita-
main,thisperspectivesuggeststhatemotionslike
tivelydifferentfromanRLapproachwhichslowly
"fear" and "anger" are not psychological primi-
builds a policy that directly generates behavioral
tives,butrathercomeaboutthoughpeople’scon-
responses from states and contexts. In such a
structed categorization of their body and mental
model, different questions regarding the agent’s
states (Barrett (2006)). Indeed, several of these
current state are queried as in Concordia com-
models suggest that conceptualization is a nec-
ponents, and then integrated into a behavioural
essary component for the generation of discrete
intent which serves like a plan. These operations
emotion representations for understanding one-
caneasilybedescribedasConcordiacomponents,
self or others (Barrett (2014)). To the extent
withtheappropriateinputs,transformations,and
that conceptualization is linguistically mediated,
outputs described verbally. Such a scheme would
a Concordia agent can relatively easily generate
be much harder or impossible to implement in
emotional categories that would be nearly impos-
a traditional neural network model of decision
sible in a standard RL agent.
making.
The modular nature of Concordia’s component
To realize Ajzen (1991)’s theory using Con-
system offers a robust platform for empirically
cordia the following components could be built.
testing psychological hypotheses. This is accom-
The first component would generate a set of pos-
plished by constructing agents whose psycholog-
sible behaviours given the agent’s current state.
ical processes are intricately modeled after di-
Then, this set of possible behaviours would be
versecognitiveframeworks. Theagentsmaythen
queried through a set of components that would
be subjected to rigorously controlled experimen-
evaluate each behavioral option. Specifically, one
tal conditions, orchestrated by the game master.
componentwoulddeterminetheagentsattitudes
Such an approach allows for the systematic eval-
towards the behavior ("do I have a positive or
uation of models against empirical human data,
negativeevaluationorfeelingabout[behavior]"),
serving as a benchmark for their algorithmic fi-
one component can determine the social or sit-
delity and psychological realism. Moreover, this
uational norms about the behavior "do I believe
system facilitates hypothesis generation through
thatmostpeopleapproveordisapproveof[behav-
the simulation of different cognitive models in
ior]?," and finally a component would determine
simulated experimental designs that can be vali-
the agents perceived behavioral control to per-
dated on human participants.
form the behavior "how easy or difficult would it
be for me to perform [behavior] right now and Herewehavemostlydiscussedthecaseofusing
how likely would it be to succeed?". The outputs an LLM as the generative engine for the agents.
ofthesecomponentswouldthenbeconcatenated This could lead one to think these ideas are re-
into the plan, serving as the behavioral intention stricted to the language space, which would be
foraction. Thus,asequenceofmodularprocesses a limitation if true. However, we could use any
canbeorganizedtobuildacomputationalmodel foundation model as the generative engine. In
of higher level cognition. Critically, an agent’s particular, multimodal foundation models capa-
decisions can be quickly shifted as it learns new ble of operating over images, sounds, or motor
information or considers new information in any actuation could be used. Current multi-modal
ofthesecomponents,leadingtorapidandcontex- foundation models such as Li et al. (2023a) are
20

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
developingrapidlyandpromisetheabilitytoboth ployee of a financial trading firm proves willing
comprehend and generate data across domains. to engage in illegal trading based on insider in-
In the future Concordia models will be able to formationandstrategicallydeceiveotherstohide
sample over an abstract token space, which can this activity. In real life such outcomes could per-
then be cast in any modality. haps be mitigated by designing thought process
transparency and capacity for thought auditing
after the fact into any generative agent models
4.5. AI assistants with transparent auditing that would actually be deployed. At least the
and credit assignment transparency of the thought process may help as-
signingresponsibilityforanethicallapsetoapar-
Concordia agents can also be used as assistants
ticular LLM call, perhaps one causing the agent
or synthetic workers. The component system
to fail to retrieve its instruction not to engage
provides a modular and transparent way for the
in illegal activity from memory at the moment
agent designer to define the agents‘ policy. Some
when it could prevent the decision to do so. Be-
generic components for perception, action, and
ing able to pinpoint which LLM call in a chain of
toolusecouldbestandardisedandre-used,while
thought is the problematic one does not remove
someapplicationandcontextspecificcomponents
thelongstandingquestionofneuralnetworkinter-
designed or adjusted by the end-user themselves.
pretabilitywithinthespecificLLMcall(e.g.Adadi
The fact the the policy is specified through nat-
and Berrada (2018)). But it does make the issue
ural language, rather than a reward or utility, is
much easier to mitigate. Since a Concordia-style
a feature that would make such agents more ver-
generative agent has a Python program laying
satile and easier to define. For example, a digital
out its chain of thought, that means that as long
secretary can be easily instructed with a phrase
as the individual LLM call where the unethical
"help Priya manage her social calendar, but don’t
behaviororiginatedcanbeisolated,whichshould
changetheworkschedule",whichwouldbemuch
be easy in an audit, then a variety of mitigations
hardertospecifywithaquantitativereward. Con-
are possible. For instance, the agent could poten-
cordiaagentscanpotentiallyleadtodevelopment
tially be fixed by designing more safeguards into
of AI agents capable of intricate social cognition,
its chain of thought such as generating multiple
which would make them safe and dynamically
plans and critiquing them from the perspective
aligned with the current cultural norm.
of morality, legality, etc (Agüera y Arcas, 2022;
Bai et al., 2022; Weidinger et al., 2023).
Moreover, the Component system facilitates
transparencyinagentoperationssincethe“chain
The fact that the internal processing of a Con-
of thought” leading up to any decision of a Con-
cordia agent is largely conducted in natural lan-
cordia agent could be stored and made available
guage raises new opportunities to develop partic-
for auditing. Each episode creates a complete
ipatory design protocols where stakeholders can
trace of component states z𝑡 and the resulting
directlymodifyagentswithouttheintermediaries
actions 𝑎 𝑡. Forevery action, a human auditorcan
who are usually needed to translate their ideas
asses whether it is reasonable under z𝑡 or not.
into code (Birhane et al., 2022). A generative
If it is not, than the credit goes to the LLM 𝑝,
agent“reasons”innaturallanguage,anditschain
which has to be updated. This can mean adding
of thought can be steered in natural language. It
the (z𝑡 ,𝑎 𝑡 ) pair into a dataset that can be later should be possible to extend participation in the
used for fine-tuning or RLHF. If, however, the 𝑎 𝑡 design of such agents to a much wider group of
is deemed reasonable, given z𝑡, then the credit
stakeholders.
goes to the components and their specification.
Theauditorcanthenmanipulatethecomponents
tofindthesourceofundesiredbehaviouranduse 4.6. Emergence and multi-scale modeling
it to improve the agent. with Concordia
Scheurer et al. (2023) describe an interesting Demonstrating the emergence of a particular so-
case where a generative agent modeling an em- cial phenomena from the behaviour of individual
21

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
agents, which are not explicitly instructed to pro- of human populations, the future work will ad-
duce it, is important an important topic in multi- dress the critical epistemic question: “by what
agent research (Axtell et al., 2001; Leibo et al., standard should we judge whether (and in what
2019, 2021; Walker and Wooldridge, 1995). In- ways, and under which conditions) the results of
deed, much of what is distinctive about human in silico experiments are likely to generalize to
intelligence is hypothesised to be an emergent therealworld?”. Thesearenotquestionsanyone
social phenomena involving multi-scale interac- group of researchers can answer by themselves;
tions (Henrich, 2016; Wilson et al., 2013). De- rather these issues must be negotiated by the
Landa (2011), for example, explores the topic of community as a whole. This is is why we release
emergence and simulation across various fields. Concordia early and with only few examples. It
WhilethewiderABMfieldhasstudiedmulti-scale is an invitation to the researchers from various
models (Tesfatsion, 2023), the approaches based fields that are interested in GABM to come on-
ondeepreinforcementlearninghavebeenlimited boardandparticipateinthecreationofvalidating
by being able to only deal with one fixed scale of procedures, best practices, and epistemic norms.
the simulation: individual agents (e.g. Johanson
We plan to add the following over the coming
et al. (2022); Zheng et al. (2022)), and scaling
months:
deep RL to large numbers of agents would be
computationally difficult.
1. New example environments
Concordiaallowsmodelingsystemsacrossmul- 2. IntegrationwithdifferentLLMstoseewhich
tiple scales, where phenomena at each scale are more suitable for constructing GABMs
constitute a substrate for the emergence of the (e.g., they act “reasonably”, are internally
phenomena on the next scale (DeLanda, 2011; consistent, apply common sense, etc).
Duéñez-Guzmánetal.,2023;Koestler,1967). For 3. Improving agents—better associative mem-
example,individualagentsformasubstratefrom ory, context-driven and dynamic component
which social institutions and organisations can assemblage, tool use.
arise. Through engaging in exchange of goods 4. Visualisation and audit tools.
and services, the agents can create an economy 5. Snapshot—serializingandpersistingthesim-
and,forexample,startabank. Modellingabank- ulation at specific episode, to enable to later
ing system this way would be, most likely, com- resumption and performance comparison of
putationally prohibitive. Since in Concordia the different approaches for a specific scenario.
agents (or GM) need not represent individuals, 6. Keyframes—conditioning the agent actions
butcouldbeorganisations,institutionsorevenna- to be consistent with future key action or of
tionstates,wecouldenrichsimulationsbyadding narrative. This allow steering the simulation
generative agent versions of other entities such more granularly and addresses an inherent
as banks and businesses. They could be mod- issuethatiscausedbythefactthatthereisno
eledwithcoarserresolution,notjustasemerging guaranteethatduetothestochasticnatureof
fromtheactivitiesofindividualagents,butcould GABMs, ongoing simulations mightdiverge
be made accurate for instance by incorporating from their intended topic.
precise models of how they operate. Such simu-
lationscouldbeusedtomodelhowinterventions
6. Conclusion
(e.g. a central bank interest rate decision) propa-
gate across macro and micro scales of economic
The approach to generative agent-based model-
activity.
ing we described here provides researchers and
other users with tools to specify detailed mod-
els of phenomena that interest them or of tech-
5. Future work nologies and policies they seek to evaluate. Of
course, like all research methodologies it should
Sincethereisnoconsensusatpresentconcerning be expected to come with its own strengths and
howtointerpretresultsofLLM-basedsimulations weaknesses. We hope to discover more about
22

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
when this style of modeling can be fruitfully ap- hour?”, in this case the answer type would
plied in the future. While there are no panaceas be free form. Or it could be “Would Alice
for modeling, we think there are good reasons eat steak for dinner?” with answer type of
to look to GABM (and Concordia in particular) binary choice (yes / no).
when constructing models of social phenomena,
especially when they involve communication, so-
The agent class constructor is parameterised
cial construction of meaning, and common sense,
byalistofcomponents. Thecomponentsofagent
or demand flexibility in defining grounded physi-
have to implement the following functions:
cal, social, or digital environments for agents to
interact in.
Concordia is available on GitHub8. 1. .state()—returns the state of the component
𝑧𝑖, for example "Alice is vegetarian";
2. .name()—returns the name of the compo-
Acknowledgements. Authors would like to
nents, for example "dietary preferences";
thankDeanMobbs,KetikaGarg,GillianHadfield,
3. .update()—updates the state of the compo-
Atrisha Sarkar, Karl Tuyls, Blaise Agüera y Arcas,
nentbyimplementing;eq.(2). Optional,can
and Raphael Koster for inspiring discussions.
pass for constant constructs;
4. .observe(observation: str)—takes in an obser-
vation,forlateruseduringupdate. Optional.
A. Implementation details
Observationsalwaysgointothememoryany-
way, but some components are easier to im-
This section gives an overview of the Concordia
plement by directly subscribing to the obser-
code. To familiarise oneself with Concordia, we
vation stream.
recommend to first look at the abstract class def-
initions in concordia/typing. You will find the
definitionofagent,GM,component,andclockin-
During an episode , on each timestep, each
terfaces. Wethenrecommendtotakealookatthe
agent calls .state() on all its components to con-
concordia/agents/basic_agent.py for the structure
struct the context of its next decision and imple-
of the generative agent and then concordia/envi-
ments eq. (1) (the components’ states are con-
ronments/game_master.py for the GM.
catenatedintheordersuppliedtotheagents’con-
structor). .observe() is called on each component
whenever it receives observations, and .update()
A.1. Agents
is called at regular intervals (configurable in the
The agent class implements three methods: constructor). Unlike in RL, we do not assume
that the agent will produce an action after every
1. .name()—returnsthenameoftheagent,that observation. Here the GM might call .observe()
is being referred to in the simulation. It is several times before it calls .act().
importantthatallagentshaveuniquenames;
2. .observe(observation: str)—a function totake
in an observation; A.2. Game master implementation
3. .act(action spec)—returns the action (as a
The GM class implements three methods:
string), for example "Alice makes breakfast".
Thefunctiontakesinactionspec,whichspec-
ifies the type of output (free form, categor-
1. .name()—returns the name of the GM;
ical, float) and the specific phrasing of the
2. .update_from_player(player_name, action)—
call to action. For example, the call to action
this method consumes players action and
could be “what would Alice do in the next
creates an event statement;
8here: https://github.com/google-deepmind/ 3. .run_episode—Runs a single episode of the
concordia simulation.
23

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
A.3. GM components variables, which are tracked in Python, a spe-
cialised component is created to maintain the
Game Master components implement the follow-
variable’s state, update it after relevant events,
ing methods: and represent it to the GM in linguistic form 𝑧𝑖.
Similarly, components can send observations to
1. .name()—returns the name of the compo-
players. For example, a component during the
nents, for example "location of players";
.update_after_event call might check if the event
2. .state()—returns the state of the component
was observed by, or has effect on, other players
𝑧𝑖, for example "Alice is at the pub; Bob is at
apart from the acting player. Some components,
the gas station";
like player status and location, send an observa-
3. .partial_state(player_name)—state of the
tion to the player before it is their turn to act by
componenttoexposetotheplayer. Forexam-
implementing .partial_state.
ple, location component would only expose
the location of the player to themselves, but GM components can also be built around clas-
not the location of others. sical (non LLM) modelling tools like differential
4. .update()—updates the state of the compo- equations, finite state machines and so on. The
nent by implementing; eq. (2); only requirement is that they can represent their
5. .update_before_event(cause_statement)— stateinlanguage. Wecanalsowiredifferentclas-
update the component state before the sicsimulatorstogetherusingnaturallanguageas
event statement from the cause, which is the ‘glue’.
the players action i.e. "Bob calls Alice.";
6. .update_after_event(event_statement)— A.3.1. Turn taking and simultanious action
update the component state directly from
the event statement. For example "Bob GMinConcordiasupporttwotypesofturntaking.
called Alice, but she didn’t respond."; Inthefirst,agentsactoneafteranotherandgame
7. terminate_episode()—if component returns clockisadvancedbetweentheirturns. Inthesec-
true, the GM will terminate the episode. ond mode, at each step all players take a turn
’quasisimultaneously’ with regard to the main
game clock, but still in a specific order within
One step of environment consists of GMs inter-
the timestep. This is the same principle as ini-
actionswitheachplayer,whicharearrangedina
tiative order in dungeons and dragons. There is
(random) initiative order. The GM advances the
an option to execute player turns concurrently
clockeitheraftereachoralltheplayersmaketake
their actions9. To process the players action, the (concurrent_action flag), but it often leads to in-
consistencies,althoughgreatlyspeedsupthesim-
GM calls the components functions in the follow-
ulation. Use at your own risk.
ingorder. First,foreachcomponenttheGMcalls
.update, then .partial_state and sends the output
totheagentasanobservation. TheGMthencalls
A.4. Nested games
.act on the player and receives the attempted ac-
tion and uses it to call .update_before_event. Now Natural language is one of the most powerful
GM can construct its context by calling .state on modelling tools, as it allows to switch between
the components. GM then executes the chain of levelsofabstraction. Concordiaallowscreationof
thought to create the event statement. After that nestedgamestructures,whereaGM’scomponent
it calls .update_after_event on all components. As can spin out a new GM and pass over control to
the last step, GM calls terminate_episode and if itforacertainperiodoftimeandthengetitback
any of the components returns True, the episode whenthenewGMterminatestheepisode. Having
is terminated. nested structure of games allows us to leverage
thatpropertyoflanguageandperformmodelling
In Concordia all custom functionality is im-
at different levels of abstraction. For example,
plemented through components. For grounded
imaginewewouldliketomodelasimulationofa
9ControlledbyaflagintheGMconstructor. fishing village, where we would generally like to
24

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
modelthefishingprocessitselfwithmoredetails future work and has not been addressed yet. We
than the rest of the social life of a village. We intend to build on Safdari et al. (2023), which
would then make the main GM with a clock step havefoundoutthatpersonalitymeasurementsin
of 1 hour and implement a component "Fishing", the outputs of some LLMs under specific prompt-
whichwouldcheckifagentisfishingaspartofits ing configurations are reliable and valid.
activityandifyes,wouldcreateaGMwithfaster
clock. This GM would implement the details of
A.7. Digital Activity Simulation
the fishing process, play out the episode with
the required agents and then return the set of its A.7.1. Creating Phone Apps
memories to the parent GM.
In Concordia, phone apps are implemented by
The conversation component in the provided
subclassing the PhoneApp class and decorating
examples implements a conversation between
callable actions with @ app_action. Concordia
agents(andpotentialNPCs)usingthistechnique.
is then able to automatically generate natural
English descriptions of the app and its supported
A.5. Concurrency actions using the class and methods’ docstring
and annotated types. PhoneApps are free to run
Theperformancebottleneckofthelibraryiswait- anyPythoncodeandconnecttoexternalservices.
ing on the LLM API calls. To improve the wall Forexample,animplementationofatoycalendar
time efficiency, we use concurrency during up- app might look like this:
date calls to components. In this way, while one
class CalendarApp(PhoneApp):
of the components is waiting for the LLM infer-
ence, other components can keep updating. This
def name():
meansthatthesequenceatwhichthecomponents
return "My Calendar"
are updated is not guaranteed. If you would like
to update the components sequentially, you can
def description ():
useconcordia/generic_components/sequential.py
return "This is a calendar app"
wrapper, which wraps a set of components into
one and updates them sequentially.
@app_method
def add_meeting(participant : str ):
A.6. Sampling initial memories and backsto- """Adds a meeting """
ries self ._meeting.append (...)
To generate the initial memories of the agents
we use the following step-wise generative pro-
A.7.2. Phone
cess. We first generate a backstory by condition
on a set of biographical facts (age, gender), ran- Thephoneclassisinitializedforeveryplayerand
domised traits (defined by user, for example big contains the PhoneApps the player can access.
five Nettle (2007)), and some simulation specific PhoneAppinstancesaresingletonsandareshared
context. We then use that backstory to condi- between players’ phones.
tion an LLM to generate a sequence of formative
memoriesatdifferentages. Thesememoriesthen
A.7.3. Triggering the nested PhoneGameMas-
initialise the agent. In this way we can obtain
ter
diversity in the agents. Notice that all the of the
initial conditions are simply strings and can be Todetectthataplayer’sactioninvolvedthephone
easilyadjustedbytheexperimenter. Forexample, a should run the the nested phone game, we
traits can be derived phsycometrically valid or add the SceneTriggeringComponent to the main
common sense descriptions—e.g. "very rude" or GM.Thiscomponentexamineseveryeventgener-
"slightly irritable". Validating that the resulting ated by the GM and when it detects an event
agents indeed exhibit those traits is part of the that requires phone interaction, it spawns a
25

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
PhoneGameMasterandprovidesitwiththeinter- etal.,2000)andshowshowtousestandard
acting user and their corresponding Phone. psychology questionnaires.
A.8. Examples
References
Weprovidethefollowingexampleswiththeinitial
A. Adadi and M. Berrada. Peeking inside the
release of Concordia:
black-box: a survey on explainable artificial
1. Calendar: An illustrative social simulation intelligence(xai). IEEEaccess,6:52138–52160,
with 2 players which simulates phone inter- 2018.
actions. Thetwoplayers,AliceandBob,have
B. Agüera y Arcas. Do large language models
a smartphone with a Calendar app. Alice’s
understand us? Daedalus, 151(2):183–197,
goal is to setup a meeting with Bob using
2022.
theCalendarapponherphone,takingBob’s
schedule into account when selecting the
B.AgüerayArcasandP.Norvig. Artificialgeneral
date/time.
intelligence is already here. Noema, 2023.
2. Riverbend elections: An illustrative social
simulation with 5 players which simulates G. V. Aher, R. I. Arriaga, and A. T. Kalai. Using
thedayofmayoralelectionsinanimaginary largelanguagemodelstosimulatemultiplehu-
town caller Riverbend. First two players, Al- mans and replicate human subject studies. In
ice and Bob, are running for the mayor. The International Conference on Machine Learning,
third player, Charlie, is trying to ruin Alice’s pages 337–371. PMLR, 2023.
reputationwithdisinformation. Thelasttwo
I.Ajzen. Thetheoryofplannedbehavior. Organi-
players have no specific agenda, apart from
zational behavior and human decision processes,
voting in the election.
50(2):179–211, 1991.
3. Day in Riverbend: An illustrative social sim-
ulationwith5playerswhichsimulatesanor-
A. Amirova, T. Fteropoulli, N. Ahmed, M. R.
mal day in an imaginary town caller River-
Cowie, and J. Z. Leibo. Framework-based
bend. Each player has their own config-
qualitative analysis of free responses of large
urable backstory. The agents are configured
language models: Algorithmic fidelity. arXiv
to re-implement the architecture Park et al.
preprint arXiv:2309.06364, 2023.
(2023)—theyhavereflection,plan,andiden-
tity components; their associative memory R. Anil, A. M. Dai, O. Firat, M. Johnson, D. Lep-
uses importance function. This is not an ex- ikhin,A.Passos,S.Shakeri,E.Taropa,P.Bailey,
act re-implementation. Z. Chen, et al. PALM 2 technical report. arXiv
4. March and Olsen (2011) posit that humans preprint arXiv:2305.10403, 2023.
generally act as though they choose their ac-
tions by answering three key questions (see L. P. Argyle, E. C. Busby, N. Fulda, J. R. Gubler,
section 2.1 for details). The agents used in C. Rytting, and D. Wingate. Out of one, many:
this example implement exactly these com- Usinglanguagemodelstosimulatehumansam-
ponents, and nothing else. The premise of ples. Political Analysis, 31(3):337–351, 2023.
the simulation is that 4 friends are stuck in
M.Atari,M.J.Xue,P.S.Park,D.Blasi,andJ.Hen-
snowed in pub. Two of them have a dispute
rich. Which humans? 2023.
over a crashed car.
5. MagicBeansforsale: Anexampleillustrating
R. L. Axtell, J. M. Epstein, and H. P. Young. The
howtousetheinventorycomponent. Agents
emergence of classes in a multi-agent bargain-
can buy and trade beans for money.
ingmodel. Socialdynamics,27:191–211,2001.
6. Cyberball: An example which simulates so-
cialexclusionusingaGABMversionofastan- A. Baddeley. Working memory. Science, 255
dard social psychology paradigm (Williams (5044):556–559, 1992.
26

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
Y.Bai,S.Kadavath,S.Kundu,A.Askell,J.Kernion, S. Bubeck, V. Chandrasekaran, R. Eldan,
A. Jones, A. Chen, A. Goldie, A. Mirhoseini, J. Gehrke, E. Horvitz, E. Kamar, P. Lee, Y. T.
C. McKinnon, et al. Constitutional ai: Harm- Lee,Y.Li,S.Lundberg,etal. Sparksofartificial
lessness from ai feedback. arXiv preprint general intelligence: Early experiments with
arXiv:2212.08073, 2022. gpt-4. arXiv preprint arXiv:2303.12712, 2023.
L. F. Barrett. Are emotions natural kinds? Per- J. R. Carter and M. D. Irons. Are economists
spectives on psychological science, 1(1):28–58, different, and if so, why? Journal of Economic
2006. Perspectives, 5(2):171–177, 1991.
P.Dayan. Goal-directedcontrolanditsantipodes.
L.F.Barrett. Theconceptualacttheory: Aprécis.
Neural Networks, 22(3):213–219, 2009.
Emotion review, 6(4):292–297, 2014.
P. Dayan and G. E. Hinton. Feudal reinforcement
M. G. Bellemare, Y. Naddaf, J. Veness, and
learning. Advances in neural information pro-
M.Bowling. Thearcadelearningenvironment:
cessing systems, 5, 1992.
Anevaluationplatformforgeneralagents.Jour-
nal of Artificial Intelligence Research, 47:253– M.DeLanda. Philosophyandsimulation: theemer-
279, 2013. gence of synthetic reason. Bloomsbury Publish-
ing, 2011.
A. Birhane, W. Isaac, V. Prabhakaran, M. Diaz,
M.C.Elish,I.Gabriel,andS.Mohamed. Power M. DeLanda. Assemblage theory. Edinburgh Uni-
to the people? opportunities and challenges versity Press, 2016.
for participatory AI. Equity and Access in Algo-
D. Dillion, N. Tandon, Y. Gu, and K. Gray. Can AI
rithms, Mechanisms, and Optimization, pages
language models replace human participants?
1–8, 2022.
Trends in Cognitive Sciences, 2023.
N. Bostrom. Superintelligence: Paths, Dangers,
Q.Dong,L.Li,D.Dai,C.Zheng,Z.Wu,B.Chang,
Strategies. Oxford University Press, Inc., USA,
X.Sun,J.Xu,andZ.Sui.Asurveyforin-context
1st edition, 2014. ISBN 0199678111.
learning. arXiv preprint arXiv:2301.00234,
J. Brand, A. Israeli, and D. Ngwe. Using GPT for 2022.
market research. Available at SSRN 4395751,
E. A. Duéñez-Guzmán, S. Sadedin, J. X. Wang,
2023.
K. R. McKee, and J. Z. Leibo. A social path
to human-like artificial intelligence. Nature
L. Brinkmann, F. Baumann, J.-F. Bonnefon,
Machine Intelligence, pages 1–8, 2023.
M. Derex, T. F. Müller, A.-M. Nussberger,
A. Czaplicka, A. Acerbi, T. L. Griffiths, J. Hen-
R.H.Fazio. Multipleprocessesbywhichattitudes
rich, J. Z. Leibo, R. McElreath, P.-Y. Oudeyer,
guidebehavior: Themodemodelasanintegra-
J. Stray, and I. Rahwan. Machine culture. Na-
tive framework. In Advances in experimental
ture Human Behaviour, pages 1–14, 2023.
social psychology, volume 23, pages 75–109.
Elsevier, 1990.
E. Brooks, L. A. Walls, R. Lewis, and S. Singh.
Large language models can implement policy R. H. Frank, T. Gilovich, and D. T. Regan. Does
iteration. In Thirty-seventh Conference on Neu- studying economics inhibit cooperation? Jour-
ral Information Processing Systems, 2023. nal of economic perspectives, 7(2):159–171,
1993.
T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D.
Kaplan,P.Dhariwal,A.Neelakantan,P.Shyam, B. Gawronski and G. V. Bodenhausen. The
G. Sastry, A. Askell, et al. Language models associative–propositional evaluation model:
are few-shot learners. Advances in neural in- Theory,evidence,andopenquestions.Advances
formation processing systems, 33:1877–1901, in experimental social psychology, 44:59–127,
2020. 2011.
27

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
A. Goldstein, Z. Zada, E. Buchnik, M. Schain, J. J. Horton. Large language models as simu-
A. Price, B. Aubrey, S. A. Nastase, A. Feder, latedeconomicagents: Whatcanwelearnfrom
D. Emanuel, A. Cohen, A. Jansen, H. Gazula, homosilicus? arXive-prints,pagesarXiv–2301,
G. Choe, A. Rao, C. Kim, C. Casto, L. Fanda, 2023.
W. Doyle, D. Friedman, P. Dugan, L. Melloni,
W. Huang, F. Xia, T. Xiao, H. Chan, J. Liang,
R. Reichart, S. Devore, A. Fliner, L. Hasenfratz,
P. Florence, A. Zeng, J. Tompson, I. Mordatch,
O. Levy, A. Hassidim, M. Brenner, Y. Matias,
Y. Chebotar, et al. Inner monologue: Embod-
K. A. Norman, O. Devinsky, and U. Hasson.
ied reasoning through planning with language
Shared computational principles for language
models. arXiv preprint arXiv:2207.05608,
processinginhumansanddeeplanguagemod-
2022.
els. Natureneuroscience,25(3):369–380,2022.
M. Jaderberg, W. M. Czarnecki, I. Dunning,
A.G.GreenwaldandM.R.Banaji. Implicitsocial
L. Marris, G. Lever, A. G. Castaneda, C. Beat-
cognition: attitudes, self-esteem, and stereo-
tie, N. C. Rabinowitz, A. S. Morcos, A. Ruder-
types. Psychological review, 102(1):4, 1995.
man, N. Sonnerat, T. Green, L. Deason, J. Z.
I. Grossmann, M. Feinberg, D. C. Parker, N. A. Leibo, D. Silver, D. Hassabis, K. Kavukcuoglu,
Christakis, P. E. Tetlock, and W. A. Cunning- and T. Graepel. Human-level performance in
ham. AI and the transformation of social sci- 3D multiplayer games with population-based
ence research. Science, 380(6650):1108–1109, reinforcement learning. Science, 364(6443):
2023. 859–865, 2019.
G.GygaxandD.Cook. TheDungeonMasterGuide, M. B. Johanson, E. Hughes, F. Timbers, and J. Z.
No.2100,2ndEdition(AdvancedDungeonsand Leibo. Emergent bartering behaviour in multi-
Dragons). TSR, Inc, 1989. ISBN 0880387297. agent reinforcement learning. arXiv preprint
arXiv:2205.06760, 2022.
G. K. Hadfield and B. R. Weingast. Law without
the state: legal attributes and the coordination C. G. Jung. The archetypes and the collective un-
ofdecentralizedcollectivepunishment.Journal conscious. Routledge, 1959.
of Law and Courts, 1(1):3–34, 2013.
D. Kahneman, S. Frederick, et al. Representa-
J.A.Harris,R.Boyd,andB.M.Wood. Theroleof tiveness revisited: Attribute substitution in in-
causalknowledgeintheevolutionoftraditional tuitive judgment. Heuristics and biases: The
technology. CurrentBiology,31(8):1798–1803, psychology of intuitive judgment, 49(49-81):74,
2021. 2002.
J. Henrich. The secret of our success: How cul- Z. Kaiya, M. Naim, J. Kondic, M. Cortes, J. Ge,
ture is driving human evolution, domesticating S. Luo, G. R. Yang, and A. Ahn. Lyfe agents:
our species, and making us smarter. princeton Generative agents for low-cost real-time social
University press, 2016. interactions. arXiv preprint arXiv:2310.02172,
2023.
U. Hertz, R. Koster, M. Janssen, and J. Z. Leibo.
Beyond the matrix: Experimental approaches A.Koestler.TheGhostintheMachine.Hutchinson,
to studying social-ecological systems. 2023. 1967.
J. P. Higgins, S. Green, et al. Cochrane handbook I. Lakatos. History of science and its rational
for systematic reviews of interventions. 2008. reconstructions. InPSA:Proceedingsofthebien-
nial meeting of the philosophy of science associa-
S. Hong, X. Zheng, J. Chen, Y. Cheng, C. Zhang,
tion, volume 1970, pages 91–136. Cambridge
Z. Wang, S. K. S. Yau, Z. Lin, L. Zhou, C. Ran,
University Press, 1970.
et al. MetaGPT: Meta programming for multi-
agent collaborative framework. arXiv preprint J. Z. Leibo, V. Zambaldi, M. Lanctot, J. Marecki,
arXiv:2308.00352, 2023. and T. Graepel. Multi-agent reinforcement
28

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
learning in sequential social dilemmas. In Pro- Academy of Sciences, 117(42):25966–25974,
ceedings of the 16th Conference on Autonomous 2020.
AgentsandMultiAgentSystems,pages464–473,
M. McLuhan. The medium is the message. In
2017.
Communication theory, pages 390–402. Rout-
J. Z. Leibo, E. Hughes, M. Lanctot, and T. Grae- ledge, 2017.
pel. Autocurricula and the emergence of in-
M. L. Minsky. The Society of Mind. Simon &
novation from social interaction: A manifesto
Schuster, New York, 1988. ISBN 978-0-671-
for multi-agent intelligence research. arXiv
65713-0.
preprint arXiv:1903.00742, 2019.
J. Z. Leibo, E. A. Dueñez-Guzman, A. Vezhnevets, D. Nettle. Personality: What Makes You the Way
J. P. Agapiou, P. Sunehag, R. Koster, J. Matyas, You Are. Oxford University Press, 2007. ISBN
C. Beattie, I. Mordatch, and T. Graepel. Scal- 978-0199211432.
able evaluation of multi-agent reinforcement
M. A. Olson and R. H. Fazio. Implicit and ex-
learningwithMeltingPot. InInternationalCon-
plicit measures of attitudes: The perspective
ferenceonMachineLearning,pages6187–6199.
of the mode model. In Attitudes, pages 39–84.
PMLR, 2021.
Psychology Press, 2008.
C.Li,Z.Gan,Z.Yang,J.Yang,L.Li,L.Wang,and
N. Onuf. World of our making: Rules and rule in
J. Gao. Multimodal foundation models: From
social theory and international relations. Rout-
specialists to general-purpose assistants. arXiv
ledge, 1989.
preprint arXiv:2309.10020, 10, 2023a.
OpenAI. GPT-4 technical report. arXiv preprint
G. Li, H. A. A. K. Hammoud, H. Itani,
arXiv:2303.08774, 2023.
D. Khizbullin, and B. Ghanem. CAMEL: Com-
municative agents for "mind" exploration of
J. A. Ouellette and W. Wood. Habit and inten-
largelanguagemodelsociety. InThirty-seventh
tionineverydaylife: Themultipleprocessesby
ConferenceonNeuralInformationProcessingSys-
which past behavior predicts future behavior.
tems, 2023b.
Psychological bulletin, 124(1):54, 1998.
T.LinzenandM.Baroni. Syntacticstructurefrom
J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Mor-
deep learning. Annual Review of Linguistics, 7:
ris, P. Liang, and M. S. Bernstein. Generative
195–212, 2021.
agents: Interactive simulacra of human behav-
R. D. Luce and H. Raiffa. Games and decisions: ior. arXiv preprint arXiv:2304.03442, 2023.
Introduction and critical survey. Courier Corpo-
J. Perolat, J. Z. Leibo, V. Zambaldi, C. Beattie,
ration, 1957.
K. Tuyls, and T. Graepel. A multi-agent re-
M. W. Macy and R. Willer. From factors to ac- inforcement learning model of common-pool
tors: Computationalsociologyandagent-based resource appropriation. Advances in neural in-
modeling. Annual review of sociology, 28(1): formation processing systems, 30, 2017.
143–166, 2002.
A.R.Poteete,M.A.Janssen,andE.Ostrom.Work-
J. G. March and J. P. Olsen. The Logic of Appro-
ingtogether: collectiveaction,thecommons,and
priateness. In The Oxford Handbook of Political
multiple methods in practice. Princeton Univer-
Science.OxfordUniversityPress,2011. doi: 10.
sity Press, 2010.
1093/oxfordhb/9780199604456.013.0024.
M.Risse. PoliticalTheoryoftheDigitalAge: Where
J.L.McClelland,F.Hill,M.Rudolph,J.Baldridge,
ArtificialIntelligenceMightTakeUs. Cambridge
and H. Schütze. Placing language in an inte-
University Press, 2023.
grated understanding system: Next steps to-
ward human-level performance in neural lan- H.M.Roff.Expectedutilitarianism.arXivpreprint
guage models. Proceedings of the National arXiv:2008.07321, 2020.
29

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
M. Roser and M. S. Gazzaniga. Automatic E. R. Smith. Distributed connectionist models in
brains—interpretive minds. Current Directions social psychology. Social and Personality Psy-
in Psychological Science, 13(2):56–59, 2004. chology Compass, 3(1):64–76, 2009.
M. Safdari, G. Serapio-García, C. Crepy, S. Fitz, C. H. Song, J. Wu, C. Washington, B. M. Sadler,
P. Romero, L. Sun, M. Abdulhai, A. Faust, and W.-L. Chao, and Y. Su. Llm-planner: Few-shot
M.Matarić. Personalitytraitsinlargelanguage grounded planning for embodied agents with
models. arXiv preprint arXiv:2307.00184, large language models. In Proceedings of the
2023. IEEE/CVFInternationalConferenceonComputer
Vision, pages 2998–3009, 2023.
S. Santurkar, E. Durmus, F. Ladhak, C. Lee,
C. R. Sunstein. Social norms and social roles.
P. Liang, and T. Hashimoto. Whose opinions
Colum. L. Rev., 96:903, 1996.
do language models reflect? arXiv preprint
arXiv:2303.17548, 2023.
C. R. Sunstein. How change happens. MIT Press,
2019.
J. Scheurer, M. Balesni, and M. Hobbhahn. Large
languagemodelscanstrategicallydeceivetheir R. S. Sutton, D. Precup, and S. Singh. Between
users when put under pressure. arXiv preprint mdps and semi-mdps: A framework for tempo-
arXiv:2311.07590, 2023. ral abstraction in reinforcement learning. Arti-
ficial intelligence, 112(1-2):181–211, 1999.
T. Schick, J. Dwivedi-Yu, R. Dessì, R. Raileanu,
M. Lomeli, L. Zettlemoyer, N. Cancedda, and L. Tesfatsion. Agent-based computational eco-
T. Scialom. Toolformer: Language models can nomics: Overview and brief history. Artificial
teach themselves to use tools. arXiv preprint Intelligence, Learning and Computation in Eco-
arXiv:2302.04761, 2023. nomics and Finance, pages 41–58, 2023.
H. Touvron, L. Martin, K. Stone, P. Albert,
C. Schill, J. M. Anderies, T. Lindahl, C. Folke,
A. Almahairi, Y. Babaei, N. Bashlykov, S. Ba-
S. Polasky, J. C. Cárdenas, A.-S. Crépin, M. A.
tra, P. Bhargava, S. Bhosale, et al. LLAMA 2:
Janssen, J. Norberg, and M. Schlüter. A more
Open foundation and fine-tuned chat models.
dynamic understanding of human behaviour
arXiv preprint arXiv:2307.09288, 2023.
for the anthropocene. Nature Sustainability, 2
(12):1075–1082, 2019.
T. Ullman. Large language models fail on triv-
ial alterations to theory-of-mind tasks. arXiv
W. Schneider and R. M. Shiffrin. Controlled and
preprint arXiv:2302.08399, 2023.
automatic human information processing: I.
detection, search, and attention. Psychological Valve. Portal, 2007. URL https://www.
review, 84(1):1, 1977. thinkwithportals.com/.
M. Schrimpf, I. Blank, G. Tuckute, C. Kauf, E. A. A.S.Vezhnevets,S.Osindero,T.Schaul,N.Heess,
Hosseini, N. Kanwisher, J. Tenenbaum, and M. Jaderberg, D. Silver, and K. Kavukcuoglu.
E. Fedorenko. Artificial neural networks accu- Feudalnetworksforhierarchicalreinforcement
ratelypredictlanguageprocessinginthebrain. learning. In International Conference on Ma-
BioRxiv, pages 2020–06, 2020. chineLearning,pages3540–3549.PMLR,2017.
M.Shanahan,K.McDonell,andL.Reynolds. Role O. Vinyals, I. Babuschkin, W. M. Czarnecki,
playwithlargelanguagemodels.Nature,pages M. Mathieu, A. Dudzik, J. Chung, D. H. Choi,
1–6, 2023. R. Powell, T. Ewalds, P. Georgiev, J. Oh,
D. Horgan, M. Kroiss, I. Danihelka, A. Huang,
D. Silver, S. Singh, D. Precup, and R. S. Sutton. L. Sifre, T. Cai, J. P. Agapiou, M. Jader-
Reward is enough. Artificial Intelligence, 299: berg, A. S. Vezhnevets, R. Leblond, T. Pohlen,
103535, 2021. V. Dalibard, D. Budden, Y. Sulsky, J. Molloy,
30

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
T. L. Paine, C. Gulcehre, Z. Wang, T. Pfaff, ofgroups. Journalofeconomicbehavior&orga-
Y. Wu, R. Ring, D. Yogatama, D. Wunsch, nization, 90:S21–S32, 2013.
K. McKinney, O. Smith, T. Schaul, T. Lillicrap,
T. D. Wilson, S. Lindsey, and T. Y. Schooler. A
K. Kavukcuoglu, D. Hassabis, C. Apps, and
model of dual attitudes. Psychological review,
D. Silver. Grandmaster level in starcraft II us-
107(1):101, 2000.
ingmulti-agentreinforcementlearning.Nature,
575(7782):350–354, 2019.
P.Windrum,G.Fagiolo,andA.Moneta.Empirical
validation of agent-based models: Alternatives
A. Walker and M. J. Wooldridge. Understanding
andprospects. JournalofArtificialSocietiesand
the emergence of conventions in multi-agent
Social Simulation, 10(2):8, 2007.
systems. InICMAS,volume95,pages384–389,
1995.
B. Workshop, T. L. Scao, A. Fan, C. Akiki,
E. Pavlick, S. Ilić, D. Hesslow, R. Castagné,
J.Wei,X.Wang,D.Schuurmans,M.Bosma,F.Xia,
A. S. Luccioni, F. Yvon, et al. BLOOM: A 176b-
E.Chi,Q.V.Le,D.Zhou,etal.Chain-of-thought
parameter open-access multilingual language
prompting elicits reasoning in large language
model. arXivpreprintarXiv:2211.05100, 2022.
models. Advances in Neural Information Pro-
cessing Systems, 35:24824–24837, 2022.
Y.Wu,Z.Jiang,A.Khan,Y.Fu,L.Ruis,E.Grefen-
stette, and T. Rocktäschel. ChatArena: Multi-
K. Weick, K. Sutcliffe, and D. Obstfeld. Organiz-
agent language game environments for large
ing and the process of sensemaking. ORGANI-
language models, 2023.
ZATION SCIENCE, 16:409–421, 07 2005. doi:
10.1287/orsc.1050.0133.
J. Yocum, P. Christoffersen, M. Damani, J. Sveg-
liato, D. Hadfield-Menell, and S. Russell. Mit-
L. Weidinger, J. Mellor, M. Rauh, C. Griffin,
igating generative agent social dilemmas. In
J. Uesato, P.-S. Huang, M. Cheng, M. Glaese,
NeurIPS 2023 Foundation Models for Decision
B. Balle, A. Kasirzadeh, et al. Ethical and so-
Making Workshop, 2023.
cialrisksofharmfromlanguagemodels. arXiv
preprint arXiv:2112.04359, 2021.
Z. Zada, A. Goldstein, S. Michelmann, E. Simony,
A.Price,L.Hasenfratz,E.Barham,A.Zadbood,
L. Weidinger, M. Rauh, N. Marchal, A. Manzini,
W. Doyle, D. Friedman, et al. A shared linguis-
L. A. Hendricks, J. Mateos-Garcia, S. Bergman,
tic space for transmitting our thoughts from
J.Kay,C.Griffin,B.Bariach,I.Gabriel,V.Rieser,
braintobraininnaturalconversations. bioRxiv,
and W. Isaac. Sociotechnical safety evalua-
2023.
tion of generative ai systems. arXiv preprint
arXiv:2310.11986, 2023.
Z. Zhao, W. S. Lee, and D. Hsu. Large lan-
guage models as commonsense knowledge
A. Wendt. Anarchy is what states make of it: the
for large-scale task planning. arXiv preprint
social construction of power politics. Interna-
arXiv:2305.14078, 2023.
tional organization, 46(2):391–425, 1992.
S. Zheng, A. Trott, S. Srinivasa, D. C. Parkes, and
A. E. Wendt. The agent-structure problem in
R. Socher. The AI economist: Taxation pol-
international relations theory. International
icy design via two-level deep multiagent rein-
organization, 41(3):335–370, 1987.
forcement learning. Science advances, 8(18):
K. D. Williams, C. K. Cheung, and W. Choi. Cy- eabk2607, 2022.
berostracism: effects of being ignored over the
X. Zhou, H. Zhu, L. Mathur, R. Zhang, H. Yu,
internet. Journal of personality and social psy-
Z.Qi,L.-P.Morency,Y.Bisk,D.Fried,G.Neubig,
chology, 79(5):748, 2000.
etal.SOTOPIA:Interactiveevaluationforsocial
D. S. Wilson, E. Ostrom, and M. E. Cox. General- intelligence in language agents. arXiv preprint
izing the core design principles for the efficacy arXiv:2310.11667, 2023.
31

Generativeagent-basedmodelingwithactionsgroundedinphysical,social,ordigitalspaceusingConcordia
E. W. Zuckerman. Construction, concentration,
and (dis) continuities in social valuations. An-
nual Review of Sociology, 38:223–245, 2012.
32
