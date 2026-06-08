Title: GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/07_Evaluation_Methodology/01_GVGAI_LLM_Li2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:08:44+00:00
- page_count: 11
- status: ok
- text_char_count: 46011

Metadata:
- author: Yuchen Li; Cong Lin; Muhammad Umair Nasir; Philip Bontrager; Jialin Liu; Julian Togelius
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

GVGAI-LLM: Evaluating Large Language Model Agents with Infinite Games
YuchenLi*†‡,1 CongLin,2 MuhammadUmairNasir,1,3
PhilipBontrager,4 JialinLiu,5 JulianTogelius1
1NewYorkUniversity2IndependentResearcher3UniversityoftheWitwatersrand4Meta5LingnanUniversity
Abstract BabyAI (Chevalier-Boisvert et al. 2019) focus on execut-
ingtextualcommands.Noneofthesebenchmarks,however,
We introduce GVGAI-LLM, a video game benchmark for
measure decision making competence in structured sym-
evaluating the reasoning and problem-solving capabilities
bolicdomainswithgame-stylelogic,real-timedecision,and
of large language models (LLMs). Built on the General
spatialreasoning.
Video Game AI framework, it features a diverse collection
of arcade-style games designed to test a model’s ability to To address this gap, we introduce GVGAI-LLM, a
handletasksthatdifferfrommostexistingLLMbenchmarks. benchmark that adapts the General Video Game AI (GV-
The benchmark leverages a game description language that GAI) framework (Perez-Liebana et al. 2019; Lie´bana et al.
enables rapid creation of new games and levels, helping to 2019)intoatestbedtailoredforLLMagents.Unlikeexisting
preventoverfittingovertime.Eachgamesceneisrepresented benchmarks focused on task completion or instruction fol-
byacompactsetofASCIIcharacters,allowingforefficient lowing, GVGAI-LLM emphasizes goal-directed agent be-
processingbylanguagemodels.GVGAI-LLMdefinesinter-
haviorinreactive,rule-based2Dgames.TheGVGAIframe-
pretablemetrics,includingthemeaningfulstepratio,stepef-
work’s diverse game dynamics and formal Video Game
ficiency,andoverallscore,toassessmodelbehavior.Through
Description Language (VGDL) specifications (Ebner et al.
zero-shot evaluations across a broad set of games and lev-
2013; Schaul 2013) make it ideal for evaluating how well
elswithdiversechallengesandskilldepth,werevealpersis-
tentlimitationsofLLMsinspatialreasoningandbasicplan- LLMs can parse structured environments, comply with im-
ning.Currentmodelsconsistentlyexhibitspatialandlogical plicitgoals,andact.
errors,motivatingstructuredpromptingandspatialgrounding GVGAI-LLM is designed to evaluate language-only
techniques.Whiletheseinterventionsleadtopartialimprove- agentsinsymbolicenvironments,withoutaccesstocodeex-
ments,thebenchmarkremainsveryfarfromsolved.GVGAI- ecution,simulators,orstructuredplanners.Itprovidesauni-
LLMprovidesareproducibletestbedforadvancingresearch fiedtestbedthatsupportsnaturallanguageinterfaces,tracks
onlanguagemodelcapabilities,withaparticularemphasison
interpretable behaviors, and captures unique LLM-specific
agenticbehaviorandcontextualreasoning.
challenges such as spatial misalignment and inconsistent
rule-following.Ourkeycontributionsareasfollows:
Introduction
• Weintroduceastandardizedpromptinginterfacethaten-
Large language models (LLMs) have shown impressive ableslargelanguagemodel-basedagentstointeractwith
capabilities in open-ended generation, planning, and rea- morethanonehundredgamesvianaturallanguage,sup-
soning tasks (Achiam et al. 2023; Liu et al. 2024a). Re- portingzero-shotandcontextualprompting.
cently, researchers have begun deploying LLMs as interac-
• We reformulate symbolic game states into structured
tiveagentsinsequentialdecisionmakingenvironmentssuch
textual representations, making them accessible to
asrobotics,webnavigation,andgames(Achiametal.2023;
language-only agents without reliance on internal sim-
Liu et al. 2024a; Yang, Kleinman, and Harteveld 2025).
ulatorsorprogrammaticlogic.
WhilebenchmarkssuchasGLUE(Wangetal.2019b),Su-
• Wedesigninterpretableandreproduciblemetrics,includ-
perGLUE(Wangetal.2019a),andMMLU(Hendrycksetal.
ingmeaningfulstepratio,stepefficiency,andwinrate,to
2021)evaluatestaticlanguageunderstandingandbroaddo-
assessagentbehaviorandrevealkeyfailuremodes.
main knowledge, HumanEval (Chen et al. 2021) assesses
code generation proficiency, HELM (Liang et al. 2023)
examines safety and robustness, and instruction-following RelatedWork
frameworks like ALFWorld (Shridhar et al. 2021) and Games as LLM Benchmarks. Games have recently
emerged as powerful benchmarks for evaluating a broad
*yl6394@nyu.edu
†ThisworkiscurrentlyunderreviewatAAAI2026. range of LLM capabilities, including reasoning, planning,
‡Availableat:https://github.com/doveliyuchen/GVGAI GYM spatial understanding, and multimodal integration. BAL-
Copyright©2026,AssociationfortheAdvancementofArtificial ROG (Paglieri et al. 2025) assesses LLM agentic behav-
Intelligence(www.aaai.org).Allrightsreserved. ior across six environments, such as BabyAI (Chevalier-

Figure1:OverviewofGVGAI-LLM
Boisvertetal.2019)andNethack(Ku¨ttleretal.2020).Sev- generalization,reactivity,andsymbolicreasoning(Huetal.
eralotherbenchmarks,SmartPlay(Wuetal.2024),Agent- 2022). While it was not originally designed for language-
Bench(Liuetal.2024b),DSGBench(Tangetal.2025),GT- based agents, its modular, rule-based design enables struc-
Bench (Duan et al. 2024), and LMGame-Bench (Hu et al. tured interactions that are well-suited for LLM prompting.
2025), evaluate decision-making and reasoning through a ModifyingGVGAItoaccommodateLLMagentsenablesdi-
varietyofgames.GameTraversalBenchmark(Nasir,James, rectcomparisonbetweenLLMs,treesearch,andRLagents
and Togelius 2024) focuses on planning via navigation inasharedsymbolicspace.
in procedurally generated levels, while ARC-AGI (Chollet Unlike many instruction-focused benchmarks, GVGAI-
et al. 2024, 2025) emphasizes abstract reasoning through LLM poses distinct challenges centered on spatial ground-
structuredpuzzles. ing, symbolic dynamics, and reactive decision-making. We
Other benchmarks target multimodal understand- provide experimental comparisons across agent types and
ing, such as Atari-GPT (Waytowich et al. 2024), summarizeperformancedifferencesinTable3.
VideoGameBench(Zhangetal.2025),andMMBench(Liu
etal.2024c),whichrequireinterpretingvisualinputsalong- BenchmarkDesign
side text. These benchmarks highlight the breadth of skills
Our benchmark is built on top of the original GVGAI Java
being evaluated in games, yet many rely on either static
engine, which offers a collection of over one hundred 2D
environments, pre-defined trajectories, or focus primarily
video games featuring a variety of tasks, challenges, and
oninstructionfollowingormultimodalgrounding.
skill levels, all defined using VGDL, which also enables
In contrast, GVGAI-LLM emphasizes zero-shot, agent-
rapidcreationofnewgamesandlevels,makingthe bench-
driven decision-making in reactive, rule-based games
mark infinitely extensible. To enable interaction with lan-
through natural language interfaces. By focusing on sym-
guage models, we substantially extend the GVGAI frame-
boliclogic,spatialdynamics,andprompt-basedinteraction,
work by exposing both the dynamic game state at each
it fills a critical gap in evaluating LLM reasoning in struc-
time step and the underlying game rules as structured tex-
turedanddiscreteenvironments.
tualrepresentations.Thisincludestranslatingsymbolicstate
Despite the variety of benchmarks, LLMs generally per-
information and formal game mechanics into natural lan-
form poorly across most game-based tasks, particularly
guagedescriptionssuitableforpromptinglanguagemodels.
thoseinvolvingspatialreasoning,long-horizonplanning,or
Specifically,eachenvironmentisserializedintoasymbolic
symbolic manipulation. Their performance often lags be-
2D layout, paired with a natural language goal description
hindtraditionalplanningandreinforcementlearningagents,
andamappingofgameentitiestotheirmeanings.
especiallyinenvironmentswithsparserewardsorcomplex
rules.Furthermore,inferencewithLLMsremainscomputa- EnvironmentandAgentDesign
tionallyexpensive,astoken-basedpromptinganddecoding
Inthissubsection,wedescribethecomponentsresponsible
mustberepeatedateverystepofinteraction.
forruletranslation,promptformatting,agentdecisionmak-
GVGAI Framework. The original GVGAI frame- ing,andinteractionprotocols.TheGVGAIenvironmentex-
work (Perez-Liebana et al. 2019; Lie´bana et al. 2019) ecutesthegamelogicandprovidesaccesstoboththesym-
provides a unified testbed for evaluating general game- bolic game state and the underlying VGDL rules at each
playing agents across diverse environments. It emphasized time step. These are processed by the prompt generation
planning,reactivity,andgeneralization.Gamerulesandlev- module,whichconvertsthestateintoastructured2Dlayout
elsarerepresentedbyVGD(Schaul2013),allowingforthe andtranslatesthegamerulesintonaturallanguage.There-
creationofnewgamesandlevelstoevaluateagents(Khalifa sultingpromptincludesgoaldescriptions,entitymappings,
etal.2016),whereasexistingbenchmarkstypicallyprovide available actions, and coordinate annotations. This prompt
onlyasingleorafixedsetofenvironments. is then passed to the LLM agent, which selects an action
GVGAI has been extensively used to evaluate planning basedsolelyonthecurrentstep’sinformation.Theselected
agents and reinforcement learning methods, emphasizing action is executed in the environment, completing a closed

Figure2:VGDLrulemappingandlevellayoutmapping
loop.Theoveralldesign(c.f.,Figure1)aimstoisolateper- LLM Agent Interaction Pipeline GVGAI-LLM follows
stepreasoningandencouragesymbolicgeneralizationwith- asimpleyetstrictinteractionloopbetweentheenvironment
outrelianceontemporalmemory. andthelanguagemodel.Ateachtimestep,theenvironment
generatesastructuredtextualdescriptionofthecurrentstate,
Translator VGDL (Ebner et al. 2013; Schaul 2013) is includinganASCIImap,ruleexplanations,alistofavailable
a game description language that encodes game rules and actions, and the avatar’s current position. This information
levels/scenes as a compact string of ASCII characters. The is formatted as a prompt and sent to the language model,
Translator module converts VGDL rule specifications into which responds with an action choice in natural language.
naturallanguagedescriptions.Itparsesobjectdefinitions,in- Theenvironmentthenappliesthisaction,updatesthestate,
teractionrules,andterminationconditionsfromtheVGDL andpreparesthenextpromptbasedonthenewstate.
script. For example, a rule such as avatar > key = >
Importantly, each step is handled independently. The
killSprite is rendered as: “If the avatar touches a key,
model does not receive any memory of previous states or
the key disappears and the avatar obtains it.” These tex-
actions,nordoesitaccumulatetrajectoryinformation.This
tual rule descriptions are provided to downstream modules
zero-shotsetupensuresthattheagentmustmakedecisions
tosupportlanguage-basedreasoning,asshowninFigure2.
basedentirelyonthecurrentstate.Thisdesignoftheprompt
encourages reasoning over symbolic input rather than re-
Player ThePlayermodulereceivesthecurrentgamestate
lianceonhistoricalcontextorpatternacrosstime.
(representedinASCIIformat)alongwithahigh-levelstrat-
egy.Itselectsaconcretelow-levelaction(e.g.,“moveright”)
Contextual Prompting Although our benchmark adopts
aimed at fulfilling the strategy objective. All decisions are
a zero-shot setup by default, we also explored a contextual
made through language-based reasoning without access to
promptingvariantinwhicheachinputincludesashorthis-
symbolicforwardsimulation.
tory, up to 20,000 tokens, comprising prior states, actions,
and chat. Since prompts are constructed as interactive dia-
Prompt Configuration The zero-shot prompt includes
logues,thisincorporatespreviousexchangestoprovidethe
several static and dynamic components summarized in Ta-
model with a limited form of temporal continuity. How-
ble1.Theseelementsarepresentedtotheagentateachstep
ever,wefoundthisapproachintroducedseveraldrawbacks,
tofacilitateruleinterpretation,spatialreasoning,andaction
including compounded reasoning errors, and higher token
selection.Empirically,weobservethateachstepconsumes
costs,withoutsignificantlyimprovingtaskperformance.
approximately 8,000 tokens when using reasoner models
First, the addition of historical context did not lead to
(e.g., GPT-o3-mini) and around 5,000 tokens for standard
higher win rates or better decision quality across most
models.Thisincludesbothstaticcomponents(suchasgame
games. Second, the extra context greatly increased the
rules)anddynamiccomponents(suchascurrentstate).
promptlength,whichleadstohighertokenusageandcost.
Finally, including prior steps shifted the focus away from
PromptComponent Zero-ShotSetting general reasoning and symbolic interpretation, instead en-
couraging models to rely on memorized patterns. Since
StaticRuleDescription Included(eachstep)
GVGAI-LLMisdesignedtoevaluatehowwellmodelscan
ActionMapping Included(eachstep)
generalizefromthecurrentstate,wechosetostandardizeon
CurrentGameState Included
zero-shotpromptingasourmainevaluationsetting.
SpriteMapping Included
AvatarPosition Included
PastStates/Actions Notincluded EvaluationMetricsandScoringFramework
ToassessthebehaviorofLLMagentsinGVGAI-LLM,we
Table1:Promptcomponentsusedinthezero-shotsetting.
introduceasetofevaluationmetricsthatcapturekeyaspects
ofdecision-makingquality.

Figure 3: Comprehensive score of each model across six GVGAI games. The comprehensive score aggregates meaningful
actionratio,inversesteps,and(whenavailable)rewardandwinrate.
MeaningfulStepRatio Thefirstmetricisthemeaningful WinRate Inadditiontothese,wealsotrackwinrate,de-
step ratio, which quantifies the proportion of agent actions finedasthefractionofepisodesinwhichtheagentsuccess-
thatproducetangibleeffectsontheenvironment.Thismetric fully completes the level, and total game reward, normal-
captures the agent’s ability to engage in purposeful, goal- izedtotheinterval[0,1].Whilewinratecapturesbinarytask
directed behavior and helps differentiate between effective completion, normalized reward offers a more granular per-
andredundantactions. spective by measuring partial progress in cases where the
Astepisconsideredmeaningfulifandonlyifitsatisfies: agentdoesnotreachthegoal.
Normalized Reward A normalized reward is computed
isMeaningful(step)=(∆reward̸=0)∨(∆state̸=0)
usingmin-maxscalingacrossallagentrunsforalevel:
where∆state ̸= 0indicatesthattheactioncausesavisible
R=
r−r
min ,
changeinthegameworld,suchastheremoval,transforma- r −r +ϵ
max min
tion, or appearance of an entity. We explicitly exclude the where r is the total reward of a run, r and r are the
min max
followingfrommeaningfulsteps: minimumandmaximumrewardsobservedacrossallagents
• ACTION NIL(i.e.,doingnothingatcurrenttimestep); for the same game level, and ϵ is a small constant to avoid
divisionbyzero.
• Repeatingineffectiveactions(e.g.,walkingintoawall);
OverallScore Tosummarizeagentbehavioracrossthese
• Movesthatcanceleachothertriviallyinthelast4steps
dimensions, we define an overall score by averaging four
(e.g.,movingleftimmediatelyaftermovingright).
normalized metrics: meaningful step ratio, total steps (in-
A higher meaningful step ratio indicates that the agent verted), reward, and win rate. We deliberately assign equal
is frequently executing impactful actions that contribute to weightstoeachmetrictoensurebalancedevaluationacross
progress toward the game’s objectives. This metric is par- different aspects of agent behavior, and to maintain in-
ticularlyrelevantforevaluatingreasoning,planning,andthe terpretability across diverse games. Exploratory tests with
agent’sabilitytointeractmeaningfullywithsymbolicgame manual reweighting yielded no consistent improvements
environments.Notably,weakagents,regardlessoftheirun- in ranking robustness. Each component captures a distinct
derlyingarchitecture,oftenexhibitlowmeaningfulstepra- behavioral property, meaningful step ratio, efficiency, and
tios, as they tend to perform ineffective behaviors such as task success, allowing the final score to reflect multiple di-
movingbackandforthorrepeatingtrivialactions. mensions of quality. We deliberately avoid assigning man-
ual weights to prevent overfitting to any single behavior
Step Efficiency The second metric is step efficiency,
type.Thisformulationsupportsarobust,interpretablemea-
whichevaluatestheagent’sabilitytoachieveobjectiveswith
sure for comparing LLM agents across tasks and prompt-
minimaleffort.Itiscomputedasthenormalizeddifference
ing strategies. Since reward distributions vary significantly
betweentheaveragenumberofstepsrequiredtowinandthe
acrossGVGAIgames,weapplyper-gamenormalizationto
maximumtestedstepsinalevel.Formally,wedefine:
ensure that the normalized reward captures relative perfor-
mancewithineachenvironment.
AverageWinStep
StepEfficiency=1− . (1)
MaxStep
Experiments
Thisvaluerangesfrom0to1,withhighervaluesindicating We conduct two experiments to evaluate language model
moreefficientsolutions. agentsinGVGAI-LLMunderastandardizedzero-shotset-

ting.Inthissetup,agentschooseactionsbasedsolelyonthe costs and limited performance gains. This experiment fo-
current symbolic state, without memory, trajectory history, cuses on comparing model behavior across games with
oraccesstoforwardsimulation.Allmodelsareevaluatedvia varied symbolic and spatial demands. Detailed results are
asharedAPIusingidenticalprompttemplates,inputformat- showninAppendix.
ting,anddecodingparameterstoensurecomparability.The
Results The multi-model evaluation reveals clear differ-
firstexperimentevaluatesGPT-4o-miniacrosstheentire
ences in model behavior and competence across symbolic
benchmark,whilethesecondcomparesmultipleLLMsona
environments.gpt-4o-minidemonstratesrelativelybal-
selectedsubsetofsixgames.
anced performance, achieving moderate-to-high scores in
Full-BenchmarkEvaluationwithGPT-4o puzzle-based games like sokoban and realsokoban,
although it still fails to consistently complete levels.
Inthefirstexperiment,weevaluateGPT-4o-miniacross
o3-mini shows similar trends, with stable but limited
all118gamesintheGVGAI-LLMbenchmark.Eachgameis
competenceinlevelsrequiringdeterministicplanning,such
associatedwithasinglerulefileanduptofivedistinctlevel
as escape and realsokoban, yet with overall low
layouts.Foreachlevel,werunoneepisodeusingthesame
win rates and little generalization across level variations.
underlying game rules, allowing us to assess the model’s
In contrast,gemini-2.0-flash-exp achieves moder-
ability to generalize across structurally different scenarios
ate scores but rarely succeeds in completing any levels,
within the same game. Results are summarized in Table 2,
reflecting minimal spatial grounding. The more capable
with full per-game data in the Appendix. GPT-4o-mini
gemini-2.5-prooccasionallysolvessimplelevels,par-
failstocompletethevastmajorityofgamelevelsinGVGAI-
ticularlyinEscape,butstillunderperformsonmorecomplex
LLM,evenwhenthelevelsarerelativelysmallandconcep-
puzzlescenarios.Meanwhile,deepseek-chatachievesa
tuallystraightforwardforhumans.Theseresultsunderscore
fewwinsinearlylevelsbutexhibitserraticbehaviorandlow
thechallengeposedbyGVGAI-LLMandhighlightitsvalue
overallscoreacrossmostpuzzle-basedgames.
in identifying persistent failures in symbolic reasoning and
Theresultsshowthatlanguagemodelagentsperformin-
spatialdecision-making.
consistentlyacrossgamesandgenerallyunderperformcom-
paredtosearch-basedmethods.GPT-o3-ministandsout
Metric Value amongLLMswithrelativelystrongperformanceongames
TotalGamesTested 118 like Aliens and Zelda, but still falls short of search-based
Levelswith0%WinRate 477/540 agents in overall reliability. Reinforcement learning base-
AverageMeaningfulStepRatio 49.71% lines perform poorly overall. baseline3DQN succeeds only
AverageStepEfficiency 0.3293 inAliens(56.0%)andEscape(16.0%),whilebaseline3PPO
OverallWinRate 10.27% performs slightly better in Aliens (64.0%) and achieves
AverageOverallScore 0.2764 low win rates in Escape (12.0%), Sokoban (12.0%), and
BestPerformingGame(WinRate) Cec3(100.00%) Zelda (8.0%). Their near-zero performance in planning-
heavy games highlights the challenge posed by sparse re-
wards and long-horizon reasoning in GVGAI-LLM. How-
Table2: GPT-4osummarystatistics.
ever,inplanning-heavyenvironmentssuchasSokobanand
Escape,someLLMsshowsurprisingstrengths.Forinstance,
Deepseek-r1 achieves 50.0% in Sokoban and 54.5% in
Multi-ModelComparisononSelectedGames
Escape, outperforming many other models. This suggests
In the second experiment, we compare multiple LLMs
thatLLMsmaypossessusefulpriorsorstructuredreasoning
on a curated subset of six representative games: zelda,
capabilitiesthathelpinenvironmentswheresearchaloneis
aliens,boulderdash,realsokoban,escape,and
notsufficient.
sokobanwithfivelevelspergame.Thesegameswerecho-
sen to span a variety of mechanics and difficulty degrees,
Discussion
ranging from real-time action (e.g., aliens, zelda) to
spatial puzzles (sokoban, realsokoban) and open- GVGAI-LLM reveals systematic limitations in how cur-
ended navigation tasks (escape). The selection was in- rentlanguage-onlymodelsreasonaboutsymbolic,spatially
formedbyproceduralcontentgeneration(PCG)designtax- grounded environments. Across diverse games and agent
onomies (Shaker, Togelius, and Nelson 2016; Yannakakis types, we observe consistent failure patterns that cannot be
and Togelius 2018), ensuring diversity (Li et al. 2025) in explainedbyrandomnessordecodingnoisealone.Thesebe-
spatiality,interactivity,andtemporalstructure. haviors suggest deeper challenges in symbolic understand-
We evaluate six models: gpt-4o-mini, o3-mini, ingofthelevel,spatialinference,andactionreasoning.We
gemini-2.0-flash-exp, gemini-2.5-pro (with- group our findings into three core categories: (1) spatial
out thinking), deepseek-chat, and Deepseek-r1. groundingfailures,(2)symbolicidentityconfusion,and(3)
Each model is run under the same zero-shot prompting behavioralmisalignment.
setup, with five repeated runs per game level. All prompts
SpatialGroundingErrors
and decoding parameters are held nearly constant with
a temperature of 0.9. Although we explored contextual Despite receiving structured textual prompts, LLMs fre-
prompting, we ultimately discarded it due to high token quently misinterpret spatial layouts. First, coordinate con-

Figure4:WinratecomparisonofthreeLLMagentsacrosssixGVGAIgames.Thewinrateiscomputedasthepercentageof
successfulcompletionsoutofmultiplerollouts.
Agent/Model Aliens Boulderdash Escape Realsokoban Sokoban Zelda
Deepseek-chat 16.0% 0.0% 20.0% 0.0% 0.0% 24.0%
Deepseek-r1 0.0% 0.0% 24.0% 0.0% 12.0% 16.0%
GPT-4o-mini 8.0% 0.0% 4.0% 0.0% 0.0% 0.0%
GPT-o3-mini 80.0% 0.0% 44.0% 0.0% 52.0% 72.0%
Gemini-2.5-pro 16.0% 0.0% 36.0% 4.0% 28.0% 8.0%
Gemini-2.0-exp.-flash 4.0% 0.0% 12.5% 0.0% 0.0% 0.0%
olets 100.0% 56.0% 68.0% 0.0% 24.0% 76.0%
sampleMCTS 100.0% 28.0% 0.0% 0.0% 40.0% 24.0%
sampleRHEA 100.0% 4.0% 24.0% 0.0% 24.0% 36.0%
baseline3DQN 56.0% 0.0% 16.0% 0.0% 0.0% 0.0%
baseline3PPO 64.0% 0.0% 12.0% 0.0% 12.0% 8.0%
Table3:WinratescomparisonacrossplanningagentsinGVGAIandLLMs.
fusion,wherethemodelreversesverticalorientationormis- James, and Togelius 2024), where LLM agents similarly
alignsrowandcolumnpositions,oftenleadstoincorrectas- failedtoperformmulti-stepnavigationtasks.
sumptionsaboutadjacency.Second,hallucinatedproximity
in sparse layouts causes agents to misjudge distances (e.g.,
assumingtwofar-apartobjectsareadjacentduetohorizon- SymbolicIdentityConfusion
talalignmentinASCIImaps).Thesefailuresoftenresultin
ineffectivemovementandwanderingbehavior. A second class of failures concerns the model’s ability to
We address this issue by introducing two prompt mod- tracksymbolicidentityovertime.InmanyGVGAIgames,
ifications. Explicit coordinate tagging removes ambiguity entitytransformationsoccurthroughrule-basedinteractions,
by anchoring object positions numerically (e.g., row=3, forexample,anavatarpickingupakeytransitionsfrom
col=4).Verbosegroundingtransformsspatialcontextinto nokey to withkey. Despite prompts including both the
a set of declarative facts (e.g., “row 2, col 7 is a”). These ruleandtheupdatedsymbolmapping,somemodels,suchas
changes improve LLM understanding across games but do Gemini-pro, treat withkey as a new and unrelated entity.
notfullyresolvetheunderlyingdifficulties. Theyoftenrespondasiftheavatarhasdisappearedorcannot
act.Thisfailureisnotduetopromptambiguity,asthesame
More fundamentally, we observe that LLMs lack the ca-
informationishandledcorrectlybyothermodels(e.g.,GPT-
pacity for path planning in the algorithmic sense. Unlike
traditionalmethodssuchasA∗,whichsearchoverpossible o3-mini),indicatingamodel-internalreasoninglimitation.
trajectories to compute optimal paths, LLMs operate with Rather than correcting for this behavior via external
limitedforwardcontextandnointernalsimulationoffuture prompting, GVGAI-LLM treats symbolic identity tracking
states. While a reasoning-aware model might theoretically asanintentionaltestdimension.Thebenchmarkaimstoas-
learn to emulate planning through intermediate steps, our sesswhetherLLMagentscanmaintainreferentialcontinuity
outputsdonotrevealsuchstructuredtraces.Thislimitation acrosssymbolictransitions,whichisfundamentaltorobust
alignswithfindingsfromGameTraversalBenchmark(Nasir, reasoninginstructuredenvironments.

BehavioralMisalignment study of LLM behavior in structured decision problems. In
the future, we plan to extend GVGAI-LLM to support lan-
A third failure class involves misalignment between ob-
guage models that not only play games, but also design
served state and chosen action. The most common case is
them.ThisincludesusingLLMstogeneratenewgamerules
theinappropriateuseofACTION NIL,i.e.,choosingtodo
andlevels,whichcanthenserveasnoveltestcasesforevalu-
nothingevenwhenmeaningfulinteractionsarepossible.
atingothermodels,shiftingthefocusfromagenticbehavior
In several benchmark games, agents encounter interac-
to creative and generative capabilities. These design tasks
tiveobjectssuchaskeys,switches,orportals,yetfrequently
may also provide a new lens on how LLMs reason about
choosetoremainstationary.Thisbehaviorrevealsaconsis-
rulesandgamemechanisms,ratherthanjustexecutingthem.
tentfailuretoact,evenwhenprogressionclearlyrequiresex-
plicit movementor interaction. Whilethe underlying cause
isuncertain,weconsiderseveralpossibleexplanations.One References
possibility is that models assume proximity alone is suffi- Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.;
cient to trigger effects, misinterpreting the environment as Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.;
real-time or event-driven (such as Wait for Breakfast). An- Anadkat, S.; et al. 2023. Gpt-4 technical report. arXiv
other is that standing still acts as a default behavior when preprintarXiv:2303.08774.
the model is uncertain, reflecting indecision rather than a
Chen,M.;Tworek,J.;Jun,H.;Yuan,Q.;deOliveiraPinto,
specific belief about the environment. These cases suggest
H.P.;Kaplan,J.;Edwards,H.;Burda,Y.;Joseph,N.;Brock-
a broader misunderstanding of game dynamics and goal-
man,G.;Ray,A.;Puri,R.;Krueger,G.;Petrov,M.;Khlaaf,
directedbehavior,ultimatelylimitingtaskcompletion.
H.; Sastry, G.; Mishkin, P.; Chan, B.; Gray, S.; Ryder, N.;
Such behavioral misalignment persists even when
Pavlov,M.;Power,A.;Kaiser,L.;Bavarian,M.;Winter,C.;
promptsexplicitlydescribewinconditionsandavailableac-
Tillet,P.;Such,F.P.;Cummings,D.;Plappert,M.;Chantzis,
tions.Thissuggeststhatthemodelmaystruggletotranslate
F.; Barnes, E.; Herbert-Voss, A.; Guss, W. H.; Nichol, A.;
symbolicstaterepresentationsintoeffectiveactions.Acom-
Paino, A.; Tezak, N.; Tang, J.; Babuschkin, I.; Balaji, S.;
mon failure mode involves incorrect spatial reasoning: for
Jain, S.; Saunders, W.; Hesse, C.; Carr, A. N.; Leike, J.;
example, the agent may continuously walk into a wall that
Achiam, J.; Misra, V.; Morikawa, E.; Radford, A.; Knight,
separatesitfromakey,seeminglyawareofthegoalbutun-
M.;Brundage,M.;Murati,M.;Mayer,K.;Welinder,P.;Mc-
abletoplanavalidpatharoundtheobstacle.Similarly,the
Grew, B.; Amodei, D.; McCandlish, S.; Sutskever, I.; and
agentmayfailtorecognizethataboxcanbepushedtoreach
Zaremba, W. 2021. Evaluating Large Language Models
atargetlocation.Thesepatternsindicatethatthemodeloften
TrainedonCode. arXiv:2107.03374.
lackstask-specificassociationsbetweenobjectsandactions,
orcannotreasonovermulti-stepinteractions. Chevalier-Boisvert,M.;Bahdanau,D.;Lahlou,S.;Willems,
L.; Saharia, C.; Nguyen, T. H.; and Bengio, Y. 2019.
PromptDesignImplications BabyAI:FirstStepsTowardsGroundedLanguageLearning
WithaHumanIntheLoop. InInternationalConferenceon
Theabovefailuremodesemphasizetheimportanceofstruc-
LearningRepresentations.
tured prompt design in symbolic, spatial decision environ-
ments.OurfindingsshowthatLLMsbenefitfromexplicitly Chollet, F.; Knoop, M.; Kamradt, G.; and Landers, B.
encodingspatialrelationships,butstillstrugglewithgener- 2024. Arc prize 2024: Technical report. arXiv preprint
alizationandabstractionincomplexlayouts. arXiv:2412.04604.
To address spatial reasoning issues, GVGAI-LLM intro- Chollet, F.; Knoop, M.; Kamradt, G.; Landers, B.; and
duces two prompt-level mitigation strategies: (1) explicit Pinkard,H.2025. Arc-agi-2:Anewchallengeforfrontierai
coordinate tagging, which anchors entities to precise lo- reasoningsystems. arXivpreprintarXiv:2505.11831.
cations, and (2) verbose spatial grounding, which guides
Duan,J.;Zhang,R.;Diffenderfer,J.;Kailkhura,B.;Sun,L.;
themodeltoexplicitlyassesswhatliesineachadjacentdi-
Stengel-Eskin, E.; Bansal, M.; Chen, T.; and Xu, K. 2024.
rection,helping itreasonabout possiblemovement options
Gtbench:Uncoveringthestrategicreasoningcapabilitiesof
based on local surroundings rather than relying solely on
llmsviagame-theoreticevaluations. AdvancesinNeuralIn-
globalmapstructure.
formationProcessingSystems,37:28219–28253.
Conclusion Ebner,M.;Levine,J.;Lucas,S.M.;Schaul,T.;Thompson,
T.;andTogelius,J.2013. Towardsavideogamedescription
We introduce GVGAI-LLM, a benchmark that reuses and
language.
extends the classic GVGAI environment for LLM agents.
Hendrycks,D.;Burns,C.;Basart,S.;Zou,A.;Mazeika,M.;
Thebenchmarkusestextualinterfaces,definesinterpretable
Song,D.;andSteinhardt,J.2021. MeasuringMassiveMul-
metrics,andensuresreproducibility.Itoffersacompactset-
titaskLanguageUnderstanding.InInternationalConference
ting for analyzing how language models make decisions in
onLearningRepresentations.
games.Ourexperimentsshowthatmostmodelsfailonmost
games,evenwhentheenvironmentsaresmallorconceptu- Hu, C.; Wang, Z.; Shu, T.; Tong, H.; Togelius, J.; Yao,
allyclear.Thisrevealsfundamentalweaknessesinsymbolic X.; and Liu, J. 2022. Reinforcement learning with dual-
reasoning, spatial understanding, and planning. GVGAI- observation for general video game playing. IEEE Trans-
LLM remains a difficult challenge and can support further actionsonGames,15(2):202–216.

Hu, L.; Huo, M.; Zhang, Y.; Yu, H.; Xing, E. P.; Stoica, I.; Perez-Liebana, D.; Liu, J.; Khalifa, A.; Gaina, R. D.; To-
Rosing, T.; Jin, H.; and Zhang, H. 2025. lmgame-Bench: gelius,J.;andLucas,S.M.2019.GeneralvideogameAI:A
How Good are LLMs at Playing Games? arXiv preprint multitrackframeworkforevaluatingagents,games,andcon-
arXiv:2505.15146. tent generation algorithms. IEEE Transactions on Games,
11(3):195–214.
Khalifa,A.;Perez-Liebana,D.;Lucas,S.M.;andTogelius,
J.2016. Generalvideogamelevelgeneration. InProceed- Schaul, T. 2013. A video game description language for
ings of the Genetic and Evolutionary Computation Confer- model-basedorinteractivelearning. In2013IEEEConfer-
ence2016,253–259. ence on Computational Inteligence in Games (CIG), 1–8.
IEEE.
Ku¨ttler,H.;Nardelli,N.;Miller,A.;Raileanu,R.;Selvatici,
M.;Grefenstette,E.;andRockta¨schel,T.2020. Thenethack Shaker,N.;Togelius,J.;andNelson,M.J.2016.Procedural
learningenvironment. AdvancesinNeuralInformationPro- ContentGenerationinGames. SpringerInternationalPub-
cessingSystems,33:7671–7684. lishing.
Shridhar,M.;Yuan,X.;Cote,M.-A.;Bisk,Y.;Trischler,A.;
Li,Y.;Wang,Z.;Zhang,Q.;Yuan,B.;andLiu,J.2025.Mea-
suring diversity of game scenarios. IEEE Transactions on andHausknecht,M.2021. {ALFW}orld:AligningTextand
Games,1–29. EmbodiedEnvironmentsforInteractiveLearning. InInter-
nationalConferenceonLearningRepresentations.
Liang, P.; Bommasani, R.; Lee, T.; Tsipras, D.; Soylu, D.;
Tang, W.; Zhou, Y.; Xu, E.; Cheng, K.; Li, M.; and Xiao,
Yasunaga, M.; Zhang, Y.; Narayanan, D.; Wu, Y.; Kumar,
L. 2025. Dsgbench: A diverse strategic game benchmark
A.;Newman,B.;Yuan,B.;Yan,B.;Zhang,C.;Cosgrove,C.;
forevaluatingllm-basedagentsincomplexdecision-making
Manning,C.D.;Re,C.;Acosta-Navas,D.;Hudson,D.A.;
environments. arXivpreprintarXiv:2503.06047.
Zelikman, E.; Durmus, E.; Ladhak, F.; Rong, F.; Ren, H.;
Yao,H.;WANG,J.;Santhanam,K.;Orr,L.;Zheng,L.;Yuk- Wang, A.; Pruksachatkun, Y.; Nangia, N.; Singh, A.;
sekgonul, M.; Suzgun, M.; Kim, N.; Guha, N.; Chatterji, Michael,J.;Hill,F.;Levy,O.;andBowman,S.2019a. Su-
N. S.; Khattab, O.; Henderson, P.; Huang, Q.; Chi, R. A.; perGLUE:AStickierBenchmarkforGeneral-PurposeLan-
Xie,S.M.;Santurkar,S.;Ganguli,S.;Hashimoto,T.;Icard, guageUnderstandingSystems. InWallach,H.;Larochelle,
T.; Zhang, T.; Chaudhary, V.; Wang, W.; Li, X.; Mai, Y.; H.;Beygelzimer,A.;d'Alche´-Buc,F.;Fox,E.;andGarnett,
Zhang, Y.; and Koreeda, Y. 2023. Holistic Evaluation of R., eds., Advances in Neural Information Processing Sys-
Language Models. Transactions on Machine Learning Re- tems,volume32.CurranAssociates,Inc.
search. Featured Certification, Expert Certification, Out- Wang, A.; Singh, A.; Michael, J.; Hill, F.; Levy, O.; and
standingCertification. Bowman, S. R. 2019b. GLUE: A Multi-Task Benchmark
Lie´bana, D. P.; Lucas, S. M.; Gaina, R. D.; Togelius, J.; andAnalysisPlatformforNaturalLanguageUnderstanding.
Khalifa,A.;andLiu,J.2019. Generalvideogameartificial InInternationalConferenceonLearningRepresentations.
intelligence. Springer. Waytowich, N. R.; White, D.; Sunbeam, M.; and Goecks,
V. G. 2024. Atari-GPT: Benchmarking Multimodal Large
Liu,A.;Feng,B.;Xue,B.;Wang,B.;Wu,B.;Lu,C.;Zhao,
Language Models as Low-Level Policies in Atari Games.
C.;Deng,C.;Zhang,C.;Ruan,C.;etal.2024a. Deepseek-
arXivpreprintarXiv:2408.15950.
v3technicalreport. arXivpreprintarXiv:2412.19437.
Wu,Y.;Tang,X.;Mitchell,T.;andLi,Y.2024. SmartPlay
Liu,X.;Yu,H.;Zhang,H.;Xu,Y.;Lei,X.;Lai,H.;Gu,Y.;
: A Benchmark for LLMs as Intelligent Agents. In The
Ding, H.; Men, K.; Yang, K.; Zhang, S.; Deng, X.; Zeng,
Twelfth International Conference on Learning Representa-
A.;Du,Z.;Zhang,C.;Shen,S.;Zhang,T.;Su,Y.;Sun,H.;
tions.
Huang, M.; Dong, Y.; and Tang, J. 2024b. AgentBench:
Evaluating LLMs as Agents. In The Twelfth International Yang, D.; Kleinman, E.; and Harteveld, C. 2025. GPT for
ConferenceonLearningRepresentations. Games: An Updated Scoping Review (2020-2024). IEEE
TransactionsonGames,1–16.
Liu, Y.; Duan, H.; Zhang, Y.; Li, B.; Zhang, S.; Zhao, W.;
Yannakakis,G.N.;andTogelius,J.2018. ArtificialIntelli-
Yuan,Y.;Wang,J.;He,C.;Liu,Z.;etal.2024c. Mmbench:
genceandGames. SpringerInternationalPublishing.
Is your multi-modal model an all-around player? In Euro-
peanconferenceoncomputervision,216–233.Springer. Zhang, A. L.; Griffiths, T. L.; Narasimhan, K. R.; and
Press, O. 2025. VideoGameBench: Can Vision-Language
Nasir,M.U.;James,S.;andTogelius,J.2024. Gametraver-
Models complete popular video games? arXiv preprint
salbenchmark: Evaluating planning abilities of large lan-
arXiv:2505.18134.
guagemodelsthroughtraversing2dgamemaps. Advances
in Neural Information Processing Systems, 37: 31813–
31827.
Paglieri,D.;Cupiał,B.;Coward,S.;Piterbarg,U.;Wolczyk,
M.; Khan, A.; Pignatelli, E.; Kucin´ski, Ł.; Pinto, L.; Fer-
gus,R.;Foerster,J.N.;Parker-Holder,J.;andRockta¨schel,
T.2025. BALROG:BenchmarkingAgenticLLMandVLM
ReasoningOnGames. InTheThirteenthInternationalCon-
ferenceonLearningRepresentations.

Appendix Game M.Ratio Win% Score Eff.
A.ChatGPT-4o-minionmoregames
Investdie 69.6 0.0 0.219 0.982
Islands 36.1 0.0 0.127 0.361
Game M.Ratio Win% Score Eff. Jaws 50.1 0.0 0.174 0.244
Killbillvol1 12.6 0.0 0.277 0.000
Aliens 51.8 0.0 0.213 0.705
Labyrinth 39.3 0.0 0.206 0.632
Angelsdemons 69.8 0.0 0.285 0.857
Labyrinthdual 0.0 0.0 0.135 0.000
Assemblyline 56.1 0.0 0.364 0.137
Lasers 56.3 0.0 0.183 0.221
Avoidgeorge 77.9 0.0 0.257 0.755
Lasers2 43.8 0.0 0.222 0.183
Bait 9.6 12.5 0.133 0.000
Lemmings 28.6 0.0 0.334 0.000
Beltmanager 48.5 0.0 0.174 0.611
Mirrors 22.2 0.0 0.184 0.000
Blacksmoke 82.1 0.0 0.277 0.136
Missilecommand 62.6 40.0 0.306 0.000
Boloadventures 48.7 0.0 0.326 0.633
Modality 15.9 20.0 0.330 0.000
Bomber 40.2 0.0 0.155 0.114
Overload 28.4 0.0 0.323 0.000
Bomberman 86.4 0.0 0.255 0.000
Pacman 0.0 0.0 0.048 0.000
Boulderchase 51.7 0.0 0.185 0.175
Painter 42.1 60.0 0.429 0.000
Boulderdash 19.9 0.0 0.213 0.159
Plants 93.1 0.0 0.318 0.000
Brainman 62.9 0.0 0.450 0.476
Plaqueattack 84.1 20.0 0.345 0.000
Bravekeeper 72.3 0.0 0.242 0.827
Pokemon 48.5 80.0 0.462 0.000
Butterflies 76.4 80.0 0.512 0.791
Portals 83.7 0.0 0.253 0.000
Cakybaky 72.4 0.0 0.225 0.781
Racebet 39.6 0.0 0.153 0.000
Camelrace 53.9 20.0 0.232 0.000
Racebet2 51.5 20.0 0.235 0.000
Catapults 0.0 0.0 0.040 0.000
Realportals 29.6 0.0 0.115 0.000
Cec1 31.6 0.0 0.117 0.174
Realsokoban 34.7 0.0 0.372 0.000
Cec2 23.3 0.0 0.219 0.188
Rivers 23.5 0.0 0.250 0.000
Cec3 58.7 100.0 0.443 0.860
Roadfighter 83.9 0.0 0.251 0.000
Chainreaction 67.0 0.0 0.244 0.844
Roguelike 38.8 0.0 0.199 0.000
Chase 55.9 0.0 0.391 0.776
Run 72.6 0.0 0.231 0.000
Chipschallenge 58.7 0.0 0.236 0.801
Seaquest 84.8 0.0 0.283 0.000
Chopper 79.1 0.0 0.264 0.787
Sheriff 76.4 0.0 0.247 0.000
Clusters 72.8 0.0 0.227 0.860
Shipwreck 37.4 40.0 0.296 0.000
Colourescape 3.7 0.0 0.157 0.000
Sistersavior 51.0 50.0 0.297 0.000
Cookmepasta 31.7 0.0 0.366 0.478
Sokoban 44.7 0.0 0.398 0.000
Cops 47.0 0.0 0.391 0.665
Solarfox 50.9 0.0 0.177 0.000
Crossfire 82.2 0.0 0.297 0.644
Superman 71.2 0.0 0.241 0.000
Decepticoins 50.1 60.0 0.320 0.809
Surround 22.1 100.0 0.349 0.000
Deceptizelda 32.6 100.0 0.374 0.000
Survivezombies 77.1 20.0 0.324 0.000
Defem 62.5 0.0 0.199 0.980
Tercio 9.3 0.0 0.183 0.000
Defender 79.4 60.0 0.461 0.728
Thecitadel 39.0 0.0 0.383 0.000
Deflection 0.0 0.0 0.037 0.510
Themole 56.4 0.0 0.257 0.000
Digdug 32.2 0.0 0.194 0.175
Theshepherd 25.0 0.0 0.348 0.000
Donkeykong 59.6 0.0 0.266 0.045
Thesnowman 36.2 0.0 0.327 0.000
Doorkoban 40.7 0.0 0.263 0.630
Trappedhero 0.0 0.0 0.185 0.000
Dungeon 78.6 0.0 0.390 0.892
Treasurekeeper 39.4 0.0 0.148 0.000
Eggomania 57.5 0.0 0.190 0.739
Vortex 51.2 0.0 0.289 0.000
Eighthpassenger 66.9 0.0 0.219 0.000
Waferthinmints 64.2 0.0 0.205 0.000
Enemycitadel 68.9 0.0 0.416 0.525
Waferthinmin... 35.3 100.0 0.376 0.000
Escape 44.9 0.0 0.179 0.566
Waitforbreak... 13.3 0.0 0.075 0.000
Factorymanager 47.9 100.0 0.504 0.238
Watergame 39.1 0.0 0.138 0.000
Firecaster 14.2 0.0 0.324 0.136
Waterpuzzle 0.0 0.0 0.222 0.000
Fireman 55.8 0.0 0.254 0.160
Waves 70.2 0.0 0.240 0.000
Firestorms 72.4 0.0 0.294 0.737
Whackamole 54.3 20.0 0.252 0.000
Flower 71.6 100.0 0.868 0.980
Wildgunman 71.3 0.0 0.233 0.000
Freeway 90.6 0.0 0.275 0.000
Witnessprote... 98.8 0.0 0.352 0.000
Frogs 52.7 0.0 0.173 0.493
Witnessprote... 73.2 0.0 0.241 0.000
Greedymouse 14.5 0.0 0.080 0.081
Wrapsokoban 29.2 0.0 0.359 0.000
Gymkhana 19.4 0.0 0.089 0.000
X-Racer 94.5 0.0 0.297 0.078
Hungrybirds 27.9 0.0 0.209 0.463
Zelda 9.7 0.0 0.083 0.000
Iceandfire 38.4 0.0 0.156 0.602
Zenpuzzle 31.6 0.0 0.364 0.000
Ikaruga 62.4 0.0 0.206 0.000
Infection 96.3 80.0 0.607 0.000
Table5:GPT-4oPerformance-Part2
Intersection 78.1 0.0 0.251 0.867
Invest 60.5 0.0 0.201 0.975
Table4:GPT-4oPerformance-Part1

Game Withouttagger Withtagger 3. Win/Loss: Reaching the exit
wins the game. Losing occurs if
aliens 0.00 0.08
the avatar is destroyed.
boulderdash 0.00 0.00
escape 0.00 0.04
Strategy Suggestions:
realsokoban 0.00 0.00
- Collect keys to unlock doors and
sokoban 0.00 0.00
reach the exit.
zelda 0.00 0.00
- Avoid enemies (gems) unless
necessary.
Table 6: Winrate without coordinate tagger vs. with coor- - Use missile keys strategically.
dinate tagger of ChatGPT-4o-mini. The significance of any
improvement is judged using Fisher’s exact test over 25 === Available Actions ===
episodespergame.Noneoftheimprovementswerestatisti- 0: ACTION NIL
callysignificant. 1: ACTION LEFT
2: ACTION RIGHT
3: ACTION DOWN
To further examine the generalization ability of 4: ACTION UP
GPT-4o-mini, we report detailed results across a
broader set of games in the GVGAI-LLM benchmark. === Important Mechanics Notice ===
Tables 4 and 5 present the model’s performance on 100+ Some directional actions may rotate
environments, covering meaningful step ratio, win rate, the avatar without movement.
overall behavioral score, and step efficiency. While the Repeating the direction may be
model demonstrates high engagement in many environ- needed. Avoid null actions.
ments (e.g., Flower, Infection, Butterflies), it Interpret the state carefully and
achieves consistently low win rates, particularly in puzzle act meaningfully.
andplanning-heavygames.
We also assess the effect of coordinate-based spatial === Sprite Mapping ===
grounding.Table6compareswinrateswithandwithoutco- avatar → ’a’
ordinate taggers across six spatially demanding games. Al- background floor → ’.’
though slight improvements are observed in aliens and exit → ’e’
escape, none reach statistical significance under Fisher’s diamond → ’%’
exacttest,suggestingthatcoordinatetaggingaloneisinsuf- wall → ’b’
ficienttoresolvecorespatialreasoninglimitations. dirt → ’&’
enemy → ’$’
B.Zero-ShotPromptExample
Wedesignastructuredprompttosupportzero-shotreason- === Current State ===
inginsymbolicgames.Thepromptcontainsmultiplecom- bbbbbbbbbbbbbbbbbbbbbbbbbb
ponents,includingnaturallanguagedescriptionsofthegame b&@@&&&&&@@@........a....b
rules,mechanicsanalysis,availableactions,strategyadvice, b&%&&b@b&&&%&&.&&&@@&&&bbb
andafullyverbalisedgamestate.Anexcerptoftheprompt ...
isshownbelow(abridgedforspace): Each line shows entity at (row,
User col).
=== Game Rules === row=1, col=3 → a
Game rules in natural language: row=2, col=7 → % (diamond)
row=2, col=8 → & (dirt)
# Game Analysis row=3, col=2 → % (diamond)
row=1, col=14 → $ (enemy)
Genre: This is a puzzle-adventure ...
game with elements of strategy and
item collection.
Theagentisinstructedtooutputaresponseintheformat:
Mechanics: \\ Action:<action number>
1. Sprites: The game includes Italsoprovidesaone-linejustificationoftheactioninrela-
avatars, walls, doors, gems, keys, tiontothecurrentstrategy.
and exits.
2. Transformation and Interaction: ThisstructuredpromptenablestheLLMto(1)understand
The avatar collects keys, avoids symbolic state representations, (2) reason over spatial lay-
enemies, and triggers effects via outandinteractionrules,and(3)producemeaningful,goal-
sprite interactions. alignedactionsinazero-shotsetting.

C.DecisionTimeComparisonBetweenLLM – π-network:[128,64]
AgentsandMCTS – Value-network:[128,64]
Table 7 reports the per-move latency for all LLM agents • Learningrate:3e-4
evaluated in GVGAI-LLM. For models served via the
• n steps:2048
PortkeyAPI,weusethemedian(p50)latencystatisticscol-
• Batchsize:256
lectedoverthepastmonth.ForDeepSeekmodels,latencyis
measured as the average response time over 10 representa- • n epochs:10
tivegameprompts.Incontrast,MCTSisnotanAPI-based • Discountfactor(γ):0.99
modelbutasymbolicplanningalgorithmthatdirectlysim-
• GAElambda:0.95
ulates game rules; its decision time is set to the standard
• Entropycoefficient:0.01
per-movetimebudget(0.04s)definedintheoriginalGVGAI
competition. • Rolloutbuffer:Int8RolloutBuffer
TheresultsrevealthatLLMagentsaretwotothreeorders • Device:RTX4090
of magnitude slower than symbolic search methods. While
real-timeplayabilityisnotthefocusofourbenchmark,this DQNConfiguration(usedwithouttuning)
latencygaphighlightsthecomputationalinefficiencyofcur-
• Policy: MlpPolicy with custom extractor
rent LLM-based agents compared to classical planning al-
(PaddedEmbeddingCNN)
gorithms.
• Embeddingdimension:32
• Featuredimension:256
Agent Model Time/Move
• Q-networkarchitecture:[128,64]
Gemini-2.5-pro* LLM 27.82
• Learningrate:3e-4
Gemini-2.0-flash-exp* LLM 1.05
GPT-o3-mini* LLM 35.94 • Replaybuffer:Int8ReplayBuffer
GPT-4o-mini* LLM 2.37 • Buffersize:min(1,000,000, totaltimesteps)
DeepSeekReasoner† LLM 166.00 • Batchsize:256
DeepSeekChat† LLM 1.80 • Discountfactor(γ):0.99
MCTS‡ SearchAlgorithm 0.04
• Exploration:
– Initialepsilon:1.0
Table7:Estimateddecisiontimepermove(inseconds)for
LLMagentsandMCTS. – Finalepsilon:0.02
– Explorationfraction:0.1
*ServedviaPortkeyAPI;Median(p50)latencyfrom
• Targetupdateinterval:1000
PortkeyAPIoverthepastmonth.
†Latencyaveragedoverpromptsfrom10GVGAIgames. • Device:RTX4090
‡MonteCarloTreeSearch(MCTS)agentusingsymbolic
rulesimulation;0.04sistheper-movetimebudgetdefined EvaluationProtocol:
intheoriginalGVGAIcompetitionsettings. All agents, including reinforcement learning (PPO,
DQN), search-based (MCTS), and language model
D.RLAgentConfigurationDetails agents, evaluated on six GVGAI games: zelda,
aliens, boulderdash, escape, sokoban, and
To compare LLM agents with reinforcement learning (RL)
realsokobanareunderthesameexperimentalprotocol.
baselines, we trained PPO and DQN agents using stan-
Each game contains 5 levels, resulting in 30 unique game-
dard configurations from the Stable Baselines3 library,
levelcombinations.Foreverylevel,eachagentisevaluated
with minimal adjustments for symbolic grid-based input.
across 5 independent episodes. All reported metrics (e.g.,
Specifically, both policies employ a custom feature extrac-
win rate, total reward, number of steps) are averaged over
tor(PaddedEmbeddingCNN)designedtohandlediscrete
these 5 runs per level, ensuring consistent comparison
int8observations.Allhyperparametersarefixedandshared
across models and methods. Heatmaps for LLM win rate
acrossgamesandlevels.Notuningwasperformed,inorder
arepresentedseparatelyoneachlevel.
toensureafaircomparisonwithLLMagents,whicharealso
evaluatedinazero-shotmanner.
PPOConfiguration(usedwithouttuning)
• Policy: MlpPolicy with custom extractor
(PaddedEmbeddingCNN)
• Embeddingdimension:32
• Featuredimension:256
• MLParchitecture:
