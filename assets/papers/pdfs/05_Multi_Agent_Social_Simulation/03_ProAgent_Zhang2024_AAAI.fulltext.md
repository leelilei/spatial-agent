Title: 03_ProAgent_Zhang2024_AAAI

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/05_Multi_Agent_Social_Simulation/03_ProAgent_Zhang2024_AAAI.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:07:12+00:00
- page_count: 9
- status: ok
- text_char_count: 45160

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

ProAgent: Building Proactive Cooperative Agents with Large Language Models
CeyaoZhang1,2*†,KaijieYang3*,SiyiHu4*,ZihaoWang2,5,GuangheLi2,YihangSun2,
ChengZhang2,ZhaoweiZhang2,5,AnjiLiu2,Song-ChunZhu5,XiaojunChang4,JungeZhang3,
FengYin1,YitaoLiang2,YaodongYang2‡
1SSE,TheChineseUniversityofHongKong,Shenzhen
2InstituteforArtificialIntelligence,PekingUniversity
3InstituteofAutomation,ChineseAcademyofSciences
4ReLER,AAII,UniversityofTechnologySydney
5NationalKeyLaboratoryofGeneralArtificialIntelligence,BeijingInstituteforGeneralArtificialIntelligence(BIGAI)
ceyaozhang2@link.cuhk.edu.cn,yaodong.yang@pku.edu.cn
Abstract amount of training data, can capture and embody a signifi-
cant amount of common sense knowledge. Notable LLM-
Buildingagentswithadaptivebehaviorincooperativetasks
based agents like SayCan (Ahn et al. 2022), ReAct (Yao
standsasaparamountgoalintherealmofmulti-agentsys-
et al. 2023), DEPS (Wang et al. 2023b), RAP (Hao et al.
tems. Current approaches to developing cooperative agents
2023),Reflexion(Shinnetal.2023),andJARVIS-1(Wang
relyprimarilyonlearning-basedmethods,whosepolicygen-
et al. 2023c) have demonstrated the ability to make deci-
eralization depends heavily on the diversity of teammates
they interact with during the training phase. Such reliance, sionsinteractivelythroughappropriatepromptsorfeedback.
however, constrains the agents’ capacity for strategic adap- However, these works have primarily focused on explor-
tation when cooperating with unfamiliar teammates, which ing the potential of LLMs as individual agents, whether in
becomes a significant challenge in zero-shot coordination gamesorrobotics.Theuntappedpotentialliesininvestigat-
scenarios.Toaddressthischallenge,weproposeProAgent, ing how LLM-based agents can effectively cooperate with
a novel framework that harnesses large language models otherAIagentsorhumans.
(LLMs) to create proactive agents capable of dynamically
adapting their behavior to enhance cooperation with team- This research delves into the capabilities of LLMs in
mates. ProAgent can analyze the present state, and infer tackling the intricate challenges of multi-agent coordina-
the intentions of teammates from observations. It then up- tion (Yang and Wang 2021; Zhang, Yang, and Bas¸ar 2021;
dates its beliefs in alignment with the teammates’ subse- Gronauer and Diepold 2022), particularly in the realm of
quentactualbehaviors.Moreover,ProAgentexhibitsahigh policygeneralization(Strouseetal.2021;Zhaoetal.2023;
degreeofmodularityandinterpretability,makingiteasilyin- Li et al. 2023b, 2024). Current approaches (Carroll et al.
tegrated into various of coordination scenarios. Experimen-
2019;Jaderbergetal.2017;Strouseetal.2021;Zhaoetal.
tal evaluations conducted within the Overcooked-AI envi-
2023; Li et al. 2023b, 2024) to developing cooperative
ronment unveil the remarkable performance superiority of
agentsrelyprimarilyonlearning-basedmethods,whosepol-
ProAgent,outperformingfivemethodsbasedonself-playand
icygeneralizationdependsheavilyonthediversityofteam-
population-basedtrainingwhencooperatingwithAIagents.
Furthermore,inpartneredwithhumanproxymodels,itsper- matestheyinteractwithduringthetrainingphase.Suchre-
formance exhibits an average improvement exceeding 10% liance, however, constrains the agents’ capacity for strate-
comparedtothecurrentstate-of-the-artmethod.Formorein- gicadaptationwhencooperatingwithunfamiliarteammates,
formationaboutourproject,pleasevisithttps://pku-proagent. which becomes a significant challenge in zero-shot coordi-
github.io. nation scenarios. We present ProAgent, an innovative and
adaptableframeworkspecificallydesignedtoexcelincoor-
Introduction dination scenarios alongside novel agents. ProAgent com-
prises four essential modules: Planner, Verificator,
Large Language Models (LLMs) have rapidly emerged as
Controller and Memory, along with the mechanism
powerful tools, achieving remarkable advancements across
ofBelief Correction.Thesemodulessynergistically
various domains, including long conversations (Ouyang
enable ProAgent to actively predict teammates’ intentions
etal.2022),reasoning(Bubecketal.2023),andtextgenera-
and achieve adaptive cooperative reasoning and planning
tion(Brownetal.2020).Thesemodels,byleveragingavast
without the need for prior training or finetuning. To assess
the adaptive cooperative capabilities of ProAgent, we con-
*Theseauthorscontributedequally.
†WorkdonewhenCeyaoZhangvisitedPekingUniversity. ducted performance evaluations using the well-established
‡Correspondingauthor multi-agentcoordinationtestingsuite,Overcooked-AI (Car-
Copyright©2024,AssociationfortheAdvancementofArtificial rolletal.2019).Inthisenvironment,twoplayersmustwork
Intelligence(www.aaai.org).Allrightsreserved. together to maximize their score. The empirical findings
4202
naJ
11
]IA.sc[
3v93311.8032:viXra

memory
Reflection Loop
state Target: cook soup and deliver…
Skill pool: pickup(onion), cook
soup…
You(Alice): hand hold nothing.
Bob: hand holds nothing.
Kitchen states: pot empty
Bobwill choose to pickup(onion).
action
environment
ProAgent
knowledge
language state state
PlanValidation Path
Planner
Fail?
belief belief Achieved!
plan
verificator
verificator
controller
ProAgent
loop store
rellortnoc
knowledge
teammate
feedback
feedback
Prompt
Error message: xxx
Please analysis again and
replanthe skill based on I succeeded at pickup(onion)
the current scene.
Plan of you: “pickup(onion)”
Analysis: The pot is empty. Both
Youand Bob have empty hands.
Intention of Bob: “pickup(dish)”
Real behavior of Bob: “pickup(onion)” Belief Correction
memory Bob
Figure 1: Overview of our proposed ProAgent framework including the coordination task workflow (left) and inner details
of ProAgent pipeline (right). The teammate agent’s decision-making loop is formed by the blue solid arrows in the outer
circle, while the decision process of the ProAgent is formed by the middle gray dotted box and the outer gray solid arrows.
ProAgentcommencesitsoperationbytranslatingtheinitialstateintonaturallanguage.ThenthePlanneradeptlyanalyzes
theprovidedlanguagestateinconjunctionwithhistoricalinformationstoredintheMemory.Thisanalyticalprocessallowsthe
modeltodiscerntheintentionsoftheteammateanddeviseahigh-levelskillfortheagentaccordingly.Thebeliefaboutpredicted
intentionwillbeupdatedthroughtheBelief Correctionmechanism,whichinvolvescomparingitwiththesubsequent
actual behavior of the teammate agent. As to the planned skill, the Verificator validates whether it can be performed
underthecurrentstate.Incaseofskillfailure,theVerificatorwillassesstheskill’spreconditionsandprovideadetailed
explanation for the encountered issue. Should the need arise, ProAgent enters into a re-plan loop, initiating a recalibration
process.Ontheotherhand,iftheskillisdeemedviable,theControllerfurtherdissectsitintoseveralexecutivelow-level
actions,tobeexecutedwithintheenvironment.
from our evaluations reveal the following key insights: 1) riorityoverotheragentswhenengagingincooperationwith
ProAgentdemonstratesremarkableproficiencyincoordinat- diversetypesofteammates.
ing with various types of AI teammates across diverse sce-
narios.2)ProAgentexhibitsanotablepreferenceforcollab- RelatedWorks
orating with rational teammates, such as the human proxy,
Reasoning and Planning with Large Language Models.
which showcases human-like behavior and suggests its ac-
IntherealmofLLMs(HuangandChang2023;Mialonetal.
tive effort to understand teammates’ intentions to enhance
2023; Bubeck et al. 2023), reasoning often entails decom-
cooperation. These results collectively highlight the effec-
posing intricate queries into sequential intermediate steps,
tiveness of ProAgent as a cooperative agent across a wide
referredtoasChain-of-Thought(CoT;Weietal.2022;Ko-
rangeofscenarios.
jima et al. 2022), to attain a final solution. Some research
In summary, our work makes three key contributions: focuses on minimizing errors as the number of steps in-
Firstly, we successfully integrate LLMs into the field of creases (Wang et al. 2023a), while others explore decom-
cooperative multi-agents and propose the ProAgent frame- positiontechniquesthatbreakdowncomplexproblemsinto
work,whichservesasacomprehensiveguidelineforlever- simpler subproblems (Zhou et al. 2023). Recent endeavors
aging the powerful reasoning and planning capabilities of have translated LLMs’ reasoning capability into planning
LLMs in cooperative settings. Secondly, we demonstrate byconstructingamonologuewithfeedback(Wellecketal.
the remarkable capability of our ProAgent to interpretably 2023; Shinn et al. 2023; Paul et al. 2023) to facilitate the
analyzethecurrentscene,explicitlyinferteammates’inten- reasoning and planning process. Notably, the challenge of
tions,anddynamicallyadaptitsbehavioraccordingly.This open-ended long-term planning in the MineDojo environ-
proactivenatureempowersProAgenttoactivelycollaborate ment(Fanetal.2022)hasbeenaddressedbyutilizingLLMs
with teammates, enabling more efficient cooperative sce- as central planners (Wang et al. 2023b,c), thereby demon-
narios. Thirdly, through a comprehensive series of experi- strating the extensive capabilities of LLMs-based agents
ments,weprovidecompellingevidenceofProAgent’ssupe- in overcoming complex decision-making tasks. As of the

camera-readyversionofourpaper,theapplicationofLLM- task or environment. The controller can be rule-based, or
based agents in cooperative games remains little explored. RL-basedmethods.
Lietal.(2023a)employsacentralizedLLM-basedplanner Memory Storage. Throughout the pipeline, all relevant
forbothtwoplayers.Incontrast,ourframeworkadoptsade- information involved in the prompt, planning process, val-
centralizedplanningparadigmandusesoneplannerforone idation process, and belief correction process is stored in
player. While Zhang et al. (2023) also decentralized plan- the Memory module. This accumulated knowledge helps
ning, their method facilitates cooperation through explicit in making informed decisions and adjusting behavior over
communication.Ourwork,ontheotherhand,fosterscoop- time.
eration by observing and inferring the intentions of team- We offer a pipeline outlined in pseudocode, available
mates. in the appendix, which delineates the procedural stages of
ProAgent’s cooperative reasoning and planning through-
Multi-agentCoordination. Thegoalofmulti-agentcoor-
out the execution of a cooperative task. By following this
dinationistoenablemultipleautonomousagentstocollabo-
pipeline,ProAgenteffectivelyincorporatesaknowledgeli-
rateeffectivelytowardsasharedgoal(Rashidetal.2018;Hu
brary,performslanguage-basedplanning,andadaptsitsbe-
and Foerster 2020; Hu et al. 2021a; Yu et al. 2022; Zhong
haviorthroughcontinuousinteractionandmemoryupdates.
et al. 2023). However, traditional approaches have limita-
tions in fixed task settings and struggle to handle multiple
PromptConstruction
tasksorunseenscenarios.Oneapproachtoaddressthischal-
lenge is to enable an agent to learn multiple tasks concur- Knowledge library The planning ability of LLMs is
rently(Huetal.2021b;Mengetal.2022;Wenetal.2022). closely related to the prompt at the beginning, which is
However, these methods may still limit the agent’s coop- alsothestandardpracticeinautomatedplanning.ProAgent
eration ability in familiar tasks and fail to handle unseen is no exception, and the knowledge library should be fed
tasksornewagentinteractions.Anotherlineofresearchfo- into LLMs at the initial stage before the cooperation task
cusesonzero-shotcoordination(ZSC),utilizingPopulation- begins. The main difficulty lies in how to build structured
BasedTraining(PBT;Strouseetal.2021;Zhaoetal.2023; knowledge.Inpractice,wefindthatthebestcombinationof
Lupu et al. 2021; Lucas and Allen 2022; Li et al. 2023b, knowledgelibraryneedstobedescribedfromthreeperspec-
2024)andTheoryofMind(ToM;Huetal.2021a;Wuetal. tives, including Task, Rules, and Demos. We provide a
2021; Wang et al. 2021) to facilitate adaptive policy devel- templatetoconstructtheknowledgelibrary:
opment for coordinating with various counterparts without ### Task:
priorcoordinationexperience.However,theseZSCmethods − The task requires two players player0 and player1 to
demandsignificantcomputationalresourcesfordatacollec- work together as a team ...
− To get the points , the team needs to ...
tionandmodeloptimization,andtheresultingpoliciesoften
...
lackinterpretability.
### Rules:
In this task , each player can ONLY perform the
Method following skills: [skill 1], [skill 2], ...
def skill 1(obj):
TheoverviewofourProAgentframework,asisdepictedin
[function detail]
Fig.1,involvesconstantinteractionbetweenagentsandthe
def skill 2(obj, obj):
environment. The inference pipeline of ProAgent is a hier-
[function detail]
archicalprocessthatinvolvesmultipleinteractionsbetween
...
theLLMsandthetaskathand.Webreakdownthepipeline Suppose you are an assistant who is proficient in the
intofivekeystages: task. Your goal is to control player0 and
Knowledge Library and State Grouding. The pipeline cooperate with player1 who is controlled by a
startswithacquiringKnowledgeLibraryspecifictothecur- certain strategy to get a high score and should
rent task and transforming the raw tensor state information follow:
intoLanguage-basedStatedescriptionthattheLLMcanef- − [Rule 1].
− [Rule 2].
fectivelycomprehend.
...
High-level Skill Planning. Receiving the aligned
− Based on the current scene, you need to achieve
language-based state, the LLM-based Planner then ana-
− [Target 1].
lyzesthecurrentscene,inferstheintentinoabouttheteam-
− [Target 2].
mate agent’s intentions, and plans a skill for the current ...
agent. Your response should be in the following format:
BeliefCorrection.Thebeliefintheteammateagent’sin- − Analysis:[your analysis of the current scene]
tentionisfurthercorrectedbytheBelief Correction − Plan for Player 0: [one skill in [skill 1, skill
mechanism. 2...]]
...
Skill Validation and Action Execution. The selected
### Demos:
skill will be validated by the Verificator and a replan
Scene 0: [Player0 state 0]. [Player1 state 0]. [Other
isneededifthecurrentskillfails.Ifavalidskillisselected,
task information]
andtheControllermoduledecomposesitintolow-level
Analysis: Both Player0 and Player1 are [State
actions, allowing ProAgent to effectively interact with the description]. I guess two players will [Some

CooperativeReasoningandPlanning
skill].
[Target 1]: [Some skill].
ProAgent is a specialized system tailored for cooperative
[Target 2]: [Some skill].
tasks,whereinformationfromteammateagentsplaysapiv-
...
otalroleinthecoordinationprocess.Existingworksmainly
Scene 39: [Player0 state 39]. [Player1 state 39]. [
utilizeinformationintwoways:firstly,throughexplicitin-
Other task information]
Analysis: Player0 is [State description]. Player1 is [ corporation, involving communication and exchange of in-
State description]. I guess ... formation before decision-making; secondly, through im-
... plicitmodelingofteammateagentstofacilitatecooperative
TaskisforLLMstounderstandtheobjectiveofthetask learning. Each approach comes with its own set of advan-
and information about other cooperative agents. Rules is tages and disadvantages concerning cooperative reasoning
designedtoregulatetheplanningpatternoftheLLM,defin- andplanning:Theintegrationofteammateinformationcan
ingwhichskillsarelegalandwhicharenot.InRules,we beachievedefficientlybysendingteammateagentinforma-
can also enforce the format of LLMs’ responses to follow tion to LLMs. However, this approach may jeopardize the
theCoT:outputanalysisandthenplanaccordingtotheanal- overallgeneralizationofProAgent’sreasoningcapabilities.
ysis instead of directly outputting a plan. Demos is an op- On the other hand, modeling the teammate agent offers a
tional component of the three. Its main functionality is to more flexible approach, while the modeling process is in-
provide real cases for LLMs to strengthen their memories herentlyunstableastheteammateagent’sstrategymaycon-
and behave following the regulations set by Rules. Nor- tinuouslyevolve,demandingadditionalresourcesformain-
mally, Demos should contain a scene description followed tenance.
byananalysisandthedesiredbehavior,suchastheselected In order to strike a balance between the generalization
skill.Withthesethreeparts,LLMscanunderstandthetask ability of built agents and the efficiency of incorporating
andwhatisexpectedoftheminthesubsequentplanningand teammate information, particularly for LLMs that possess
reasoningstages. excellent reasoning capabilities but face challenges in fine-
Grounding tensor state to language-based state To fa- tuningorlearningextrabeliefmodules,ProAgentintroduces
cilitateinteractionbetweenLLMsandtheenvironment,itis three core components along with a cooperative reasoning
essentialtoestablishabridgebetweentheoriginalsymbolic and planning mechanism. The three modules encompass:
state provided by the environment and the language-based 1) The Memory module, which stores information about
state for LLMs. In most scenarios, the raw state is not di- task trajectory and general knowledge in the task domain.
rectly applicable to LLMs’ usage. Hence, finding an effec- 2) The Verificator module, consisting of one compo-
tive alignment between the original symbolic state and the nent for skill failure analysis and another for transforming
language-based state is crucial to enhancing LLMs’ accu- skills into atomic actions. 3) The Controller module,
rateunderstandingofthecurrentsituation.Toillustratethis, dedicatedtothetransformationofskillsintoatomicactions.
we present a simplified example based on the Overcooked- To further align the LLMs’ belief regarding the teammate
AI environment, demonstrating how the state can be trans- agent’s intentions with actual behavior, and thereby con-
formedintolanguagewithinourProAgentframework.With tinuallyenhancepredictionaccuracy,ProAgentimplements
theknowledgelibraryandinitialstateinformationprepared, the Belief Correction mechanism. This process ef-
ProAgent is equipped to tackle the cooperative task along- fectivelystrengthenstheLLMs’beliefs,leadingtoimproved
side its teammates. This marks the transition to the subse- cooperativereasoningandplanning.
quentstage,whereProAgentengagesinreasoningandplan-
Memory Module: Leveraging History for Cooper-
ning,progressingstepbysteptoachieveitsobjectives.Here
ative Behavior In ProAgent, the Memory module
isanillustrativeinstanceofthealignmentbetweenstaterep-
plays a crucial role in supporting information stor-
resentationandnaturallanguage:
age and retrieval processes. It consists of two compo-
### Original State
nents: Knowledge Library and Trajectory. The
|X X P X X|
Knowledge Libraryactsasapersistentrepository,re-
| | taining a comprehensive record of the task, including its
|O ←0o ←1o O| layout,rules,anddemonstrationsthroughoutgameplayses-
| | sions. On the other hand, the Trajectory component
|X X| serves as a temporary buffer with a fixed length, following
| | aFirst-In,First-Out(FIFO)approach.Itstoresessentialin-
|X D X S X| formation,suchasthelatestLanguage-based State,
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Analysis, Belief of teammates’ intentions, and the
### Language State (Layout)
Skillused,whilediscardingthemostoutdateddata.When
Above is the layout of the kitchen: onion dispenser at
needed, only specific parts of the Memory are retrieved,
(0, 1), onion dispenser at (4, 1), dish
depending on the chosen strategy, such as the recent-K
dispenser at (1, 3), pot at (2, 0), serving loc
at (3, 3). strategy1. This strategy focuses on the immediate context,
### Language State (Task state) facilitating efficient decision-making and planning during
State: Player 0 holds one onion. Player 1 holds one
onion. Kitchen states: Pot (2, 0) is empty. 1onlyretrievetheKmostrecenttrajectories.

ongoing interactions. Overall, the Memory module signif- tions of each skill can be expressed either in natural lan-
icantlyenhancesProAgent’scapacitytoaccesspertinentin- guageorinpseudo-codeform,whichcanbemoreeffective
formation and cooperate efficiently with teammate agents. asproposedinpreviousworks(Liangetal.2023;Singhetal.
Byleveragingpastexperiencesandlearningfromhistorical 2023).
data,theMemorymoduleempowersProAgenttomakein-
BeliefCorrection:RectifyingBeliefonTeammateAgents
formeddecisionsduringcooperationtasks.
The Belief Correction mechanism plays a pivotal
Planner Module: Reasoning with Chain of Thought role in rectifying any incorrect beliefs during cooperation.
With the history information and current state descrip- ProAgent makes predictions about their teammates’ future
tion ready, ProAgent utilizes the strong reasoning ability behavior and stores relevant analyses in their memory. In
of LLMs to make decisions in the current situation. The subsequent steps, ProAgent verifies the accuracy of their
Planner module, which follows the Chain of Thought predictionsandcorrectsanyerroneousbeliefs.Specifically,
(CoT) approach commonly used in LLMs’ reasoning and iftheobservedbehavioroftheteammateagentdeviatesfrom
planningwork(Yaoetal.2023;Haoetal.2023;Shinnetal. the assumed intentions recorded in Memory, the Belief
2023). Instead of directly outputting a plan, the Planner Correctionmechanismcantaketwoapproaches:1)Re-
modulemakesthefinaldecisionstepbystep.Theprovided placethepredictedintentionwiththeactualbehaviorofthe
informationisfirstthoroughlyanalyzed,andtheintentionof teammate. 2) Provide an annotation alongside the original
the teammate agent’s plan for the current step is predicted. prediction to flag it as incorrect. The replacement method
BasedonthisAnalysisandtheBeliefabouttheteam- enforces ProAgent to learn from ground truth, while the
mateagent,LLMsformulateaplanthatensuresitisthemost annotation method allows ProAgent to reason about the
reasonable and effective strategy for the given situation. In cause of the wrong belief, thereby avoiding similar mis-
theexperimentpart,weconductanablationstudytoassess takes in the future. Additionally, the replan loop within the
how this design enhances ProAgent’s performance in a co- Verificator module serves as an indirect method for
operativescenario. rectifying beliefs. With each query to the LLMs, ProA-
gentoutputsnewintentionsontheirteammateagent,which
Verificator Module: Analyzing Skill Failures With
contributes to improving the accuracy of their predictions.
Multi-rounds Prompts In the cooperative setting, the
ThisiterativeprocessallowsProAgenttorefinetheirbeliefs
Verificatormoduleplaysacrucialroleinscrutinizing
over time and enhance their ability to make accurate pre-
andidentifyinganyunreasonableorflawedplanninggener-
dictionsabouttheirteammate’sintentions.Insummary,the
ated by the LLMs. Its primary function involves analyzing
Belief CorrectionmechanismensuresthatProAgent
theunderlyingreasonsfortheseinadequaciesandproviding
maintains accurate and up-to-date information about their
valuable insights and suggestions for improvement. In the
teammateagent’srealbehavior.ByreferencingtheBelief
ProAgentframework,thisprocessentailsconductingathor-
partofMemorybeforemakingdecisions,ProAgentcontin-
ough investigation through multiple rounds of prompt and
ually improves the accuracy of their beliefs regarding their
responsebetweentheagentandtheLLMs.
teammate’sfuturebehavior.
Toillustratethisprocess,wepresentanexamplebasedon
Overcooked-AI,whereweemployathree-roundpromptand Controller Module: Grounding High-Level Skills to
response approach, including Preconditions Check, Low-Level Actions Based on the modules and mecha-
Double-check, and Error Conclusion. It’s impor- nismsdiscussedabove,ProAgenteffectivelyengagesinco-
tant to note that the number of rounds or the specific inter- operativereasoningandplansahigh-levelskill.However,it
action style is not restricted, and the core idea behind the is worth noting that there is a gap between the skill space
Verificator module remains focused on decomposing andtheenvironment’sactionspace.Therefore,wealsoneed
howtoreplanforthecurrentagentwhenreceivingnegative aControllermodulewhichisimperative,aimingtocon-
feedback from external environments by checking and de- vertlanguage-basedskillsintolow-levelactionsthatcanbe
termination. executed in the environment. Although this transformation
Preconditions Check: The Preconditions Check process is closely tied to the specific task at hand, mak-
involvessignalingtheLLMsifthecurrentplanisillegaldue ingtheControllermodulehighlyflexible,itnecessitates
to internal checks before its actual execution. A robust in- theestablishmentoffixedrulescapableofdecomposingthe
ternal checking mechanism can prevent failures when the skillintomultiplestepsoflow-levelactionsandprovidinga
LLMs haven’t fully understood the consequences of their feedbacksignaltothereasoningcomponentoncetheaction
chosen skill under the current state. In the Overcooked-AI is fully executed. The controller can be a rule-based path
example, we design the condition check prompt by lever- search algorithm or a policy trained by language-grounded
aging both the current scene and the failed skill as inputs. reinforcement learning (Hanjie, Zhong, and Narasimhan
We employ a trigger prompt to enable the LLMs to indi- 2021;Dingetal.2023;HuandSadigh2023;Duetal.2023)
vidually verify each precondition of the skill and pinpoint methods.Consideringthatthecontrollerisnotourmaincon-
the specific one that led to the failure. To aid in solving cern,wechoosethebuilt-incontrollerintheOvercooked-AI
multi-step reasoning problems, prompting techniques like environment based on Best-First Search and a better con-
CoT are also adopted. An instance of the trigger prompt in trollercandefinitelyreachbetterperformance.Anexample
Overcooked-AIcouldbe:”AnalysisofwhyIcannotexecute of how the skill fill dish with soup() is executed
this skill in the current scene step by step.” The precondi- and completed in three timesteps can be found in the ap-

BaselineAIAgents
Layout ProAgent(ours)
SP PBT FCP MEP COLE
168.5±15.2 178.8±16.5 196.3±16.8 185±15 163.8±24.1 197.3±6.1
CrampedRoom
172.8±16.1 179.8±26.8 196±11.9 178.2±15.6 169.2±16.8 194.2±10.5
183.3±27.5 182.2±27.9 185.7±22.7 155.7±63.9 201.3±34.5 228.7±23
AsymmetricAdvantages
177.8±24.6 152.3±64.5 167.8±21.3 184±41.8 165.5±33.3 229.8±21.9
122±17.2 141.3±28 148.8±19.4 167.2±22.4 168.8±26.1 175.3±29
CoordinationRing
133.3±23.7 141.3±27.5 145.7±17.1 159.3±25.3 158.3±27.1 183±31.7
6.7±6.7 15.3±17.1 44.7±36.4 23.3±19.8 24±21.8 49.7±33.1
ForcedCoordination
30.2±21.9 61.7±46 32.2±30.2 39.3±16.9 57.3±36.4 31±33.9
64.7±45.8 64.7±45.9 58.3±37.5 74.3±39.1 95.5±25.2 126.3±32.3
CounterCircuit
60.7±40.8 54.3±49.1 60±38.3 81.5±27.5 100.8±31.1 128.5±28.1
Table 1: Performance for all AI agent pairs. Each column represents the average reward and standard error of one algorithm
playing with all others. For each layout, the first row represents the scenario where the agent takes the role of Player 0, and
theAIpartnertakestheroleofPlayer1.Thesecondrowdepictsthevice-versascenario.Thebestresultsforeachlayoutare
highlightedinbold.
pendix. CollaboratingwithAIAgents
Quantitative Results Table 1 illustrates the average per-
formance of SP, PBT, FCP, MEP, COLE, and ProAgent
Experiments
when paired with all the others. For each layout, the first
rowrepresentsthescenariowheretheagenttakestheroleof
ExperimentalSettings Player0,andtheAIpartnertakestheroleofPlayer1.The
secondrowdepictsthevice-versascenario.Theresultsindi-
cate that ProAgent outperforms the baselines in all layouts
Following previous works on cooperative AI and human-
when acting as Playe 0. Taking the role of Player 1, ProA-
AI cooperation, we choose Overcooked-AI as our test en-
gentonlyslightlyunderperformsFCPincrampedroomlay-
vironment, in which two agents swiftly prepare and serve
outandlosestoPBTinforcedcoordinationlayout.Wewill
soups by placing up to three ingredients in a pot, cook-
examine this failure further in the appendix. In previous
ing the soup, filling the soup with the dish, and delivering
studies, it is rare to compare different AI agent combina-
thesoup.Agentsmustdynamicallyallocatetasksandcoop-
tions with each other, and our experimental results also re-
erate effectively. Five classical layouts are used: Cramped
vealthatnoneoftheotherZSCmethodsisconsistentlybet-
Room, Asymmetric Advantages, Forced Coordination, Co-
terthanothermethods.ConsideringthatProAgentrequires
ordinationRing,andCounterCircuit.Adetaileddescription
no specific training with distinct teammates and in distinct
ofeachlayoutcanbefoundintheappendix.
layouts,itpresentsastrongeradaptiveabilitythantheother
Our primary concern behind this work is how well the AIagents.TheseresultsshowourLLM-basedagentisabet-
agentsdevelopedsofarbasedonZSCmethodscancooper- tercooperator.
atewithdiverseteammates,rangingfromdifferentAIagents
tohumans.InpreviousworksonOvercooked-AI,thecoop- QualitativeResults Togaindeeperinsightsintothefun-
erativeperformanceofanagentisoftenevaluatedwithtwo damentalcomponentsofeffectivecooperation,weperforma
held-outpopulations:self-play(SP)agentandhumanproxy qualitativeexaminationofourProAgent’sbehaviorsexhib-
model.Weconductacomparativeanalysisbetweenourpro- ited during our experiments, leading us to identify several
posedProAgentandfivealternativesprevalentinthefieldin- cooperativebehaviors.
cludingSP(Tesauro1994;Carrolletal.2019),PBT(Jader- ProAgent excels in making strategic plans. For example,
bergetal.2017),FCP(Strouseetal.2021),MEP(Zhaoetal. when pot one is cooking and pot two lacks an onion, we
2023),andCOLE(Lietal.2023b,2024).Wecombinedthe observed that ProAgent would prioritize putting one onion
above six algorithms in pairs to construct 36 pairs. For ex- into pot two. After this, the agent will fetch the plate. At
ample,wechoosetheSPalgorithmasplayer0andthePBT the same time, cooking can be completed in the first pot,
algorithmasplayer1,andthesetwoalgorithmscanforman and this agent with a plate can directly fill the plate with
agentpair(SP,PBT).Sincethetwoplayersarenotallhomo- soup.Thisprocessisveryeffective.Besides,aftermakinga
geneous,wewillalsoforma(PBT,SP)algorithmpair.For failure plan, ProAgent can promptly recognize this failure,
each algorithm pair, we ran five episodes and collected the andmakeanewandoftenbetterplan.
meanandstandardvariationoftheepisodereturns.Besides, ProAgent demonstrates a remarkable capacity to dy-
we also select the human proxy model proposed by (Car- namically adjust low-level actions while executing high-
rolletal.2019)totesttheagent’sabilitytocooperatewith levelplans.Forinstance,whenProAgentintendstodeposit
humans. an onion into a pot, it’s underlying Controller identi-

Figure 2: Performance with human proxy partners. In each layout, the reward bar represents the average performance of one
algorithm collaborating with the unseen human proxy partners over 400 timesteps on five BC models, and the error lines
representthestandarderror.Thehashedbarsindicatetherewardsobtainedwherethestartingpositionsareswitched.
fies a blocked path caused by its teammate. Swiftly, the theCrampedRoomlayout.Theexperimentconsideredthree
Controller will identify an alternative interconnected distinct conditions and their respective scores were: 1) 204
route, skillfully bypassing any potential obstructions. This forwithbothanalysisandbelief,2)184withoutbelief,and
adaptive strategy enables ProAgent to discover unhindered 3) 100 for no analysis and belief, and making a skill plan
pathways.Moreover,whenPlannerhasnocleargoal,the directly. We believe that the significance of analysis in the
Controllerwillmoverandomly.Thisdynamicoperation PlannerModuleliesinitsprovisionofin-contextforfinal
helps ProAgent to break the deadlock caused by other AI planning just as CoT will improve the effect of reasoning.
agentsduetoconventionsformedduringthetrainingphase. Additionally,inferringteammateintentionsprovidesfurther
improvements.
CollaboratingwithHumans
Apart from cooperation with AI agents, our concern also Is Verificator effective in feedback-based reasoning?
involves the generalization to human partners. Due to the Upon removing the Verificator Module and allowing
limitation of collecting human interaction data, we follow ProAgenttoengageinplanningwithoutfeedback,wecom-
the previous work (Carroll et al. 2019) that uses a behav- putedsuccessratesover100steps.Notably,thesuccessrate
ior cloning (BC) model trained on human data as a proxy droppedsignificantlyto20%,underscoringthecriticalrole
of humans. Fig. 2 presents the average cumulative rewards ofourVerificatorModuleinfurnishingfeedbackwhen
achieved for 400 timesteps by ProAgent when engaged in thePlannerModulegeneratesinaccurateplans.
collaboration with BC. The reported outcomes encompass
both the mean value and standard error across five distinct
BC models. Analysis of the experimental findings reveals Conclusion
thatacrossthefiveenvironments,ProAgentoutperformsthe
baseline in four environments, exhibiting particularly note-
Inthiswork,weproposeProAgent,aproactiveLLM-based
worthysuperioritywhenfunctioningasPlayer0inthecon-
agent framework, with the primary objective of address-
text of Forced Coordination. Notably, the positioning dis-
ing the multi-agent coordination predicament. By leverag-
crepancybetweentheleftandrightstartingpositionshada
ing the inherent faculties of LLMs encompassing common
negligibleimpactonProAgent’sperformance.However,this
sensecomprehensionandlanguage-centrictaskunderstand-
differenceledtosubstantialperformancedisparitiesamong
ing, coupled with explicit mechanisms for reasoning and
thebaselines,particularlyinasymmetriclayouts,wherethe
planning, ProAgent demonstrates remarkable performance
cumulativerewardsachievedbyallbaselinesweresuperior
within various coordination scenarios. Experiments on co-
intheleftpositioncomparedtotherightposition,consistent
operating with both AI agents and human proxies in the
withthefindingsinCOLE(Lietal.2023b,2024).
Overcooked-AI demonstrate the effectiveness of ProAgent
overstate-of-the-artmethods.Moreover,ProAgent’sreason-
Discussion
ing and planning are based on natural language, which is
Does analysis and belief help in better planning? To interpretableandfriendlytohumans.Theseencouragingre-
gauge the influence of analysis and belief on the accuracy sults pave the way for further advancements in both coop-
and efficiency of decisions made by the Planner Mod- erativemulti-agentandhuman-compatibleAIsystemsbuilt
ule, we conducted an ablation study within the context of uponLLMs.

Acknowledgement Gronauer,S.;andDiepold,K.2022. Multi-AgentDeepRe-
inforcementLearning:Asurvey. ArtificialIntelligenceRe-
This work is sponsored by the National Natural Science
view,1–49.
Foundation of China (62376013), by the Basic Research
Project No. HZQB-KCZYZ-2021067 of Hetao Shenzhen- Hanjie, A. W.; Zhong, V. Y.; and Narasimhan, K. 2021.
HK S&T Cooperation Zone, Beijing Municipal Science Grounding Language to Entities and Dynamics for Gener-
& Technology Commission (Z231100007423015), by the alizationinReinforcementLearning. InInternationalCon-
Shenzhen Outstanding Talents Training Fund 202002, by ferenceonMachineLearning,4051–4062.PMLR.
the Guangdong Research Projects No. 2017ZT07X152 Hao,S.;Gu,Y.;Ma,H.;Hong,J.J.;Wang,Z.;Wang,D.Z.;
and No. 2019CX01X104, by the Guangdong Provincial andHu,Z.2023. ReasoningwithLanguageModelisPlan-
Key Laboratory of Future Networks of Intelligence (Grant ningwithWorldModel. arXiv:2305.14992.
No. 2022B1212010001), by the Shenzhen Key Labora- Hu,H.;andFoerster,J.N.2020. SimplifiedActionDecoder
tory of Big Data and Artificial Intelligence (Grant No. forDeepMulti-AgentReinforcementLearning. InInterna-
ZDSYS201707251409055), by the NSFC under Grant No. tionalConferenceonLearningRepresentations.
62271433, and by Shenzhen Science and Technology Pro-
Hu,H.;Lerer,A.;Cui,B.;Pineda,L.;Brown,N.;andFoer-
gram under Grant No. JCYJ20220530143806016 and No.
ster,J.2021a. Off-BeliefLearning. InInternationalConfer-
RCJC20210609104448114.
enceonMachineLearning,4369–4379.PMLR.
Hu, H.; and Sadigh, D. 2023. Language Instructed Rein-
References
forcement Learning for Human-AI Coordination. In Pro-
Ahn, M.; Brohan, A.; Brown, N.; Chebotar, Y.; Cortes, O.; ceedings of the 40th International Conference on Machine
David, B.; Finn, C.; Fu, C.; Gopalakrishnan, K.; Hausman, Learning.PMLR.
K.; Herzog, A.; Ho, D.; Hsu, J.; Ibarz, J.; Ichter, B.; Irpan, Hu, S.; Zhu, F.; Chang, X.; and Liang, X. 2021b. UPDeT:
A.; Jang, E.; Ruano, R. J.; Jeffrey, K.; Jesmonth, S.; Joshi, Universal Multi-agent Reinforcement Learning via Policy
N. J.; Julian, R.; Kalashnikov, D.; Kuang, Y.; Lee, K.-H.; DecouplingwithTransformers. arXiv:2101.08001.
Levine,S.;Lu,Y.;Luu,L.;Parada,C.;Pastor,P.;Quiambao,
Huang, J.; and Chang, K. C.-C. 2023. Towards Reasoning
J.;Rao,K.;Rettinghouse,J.;Reyes,D.;Sermanet,P.;Siev-
inLargeLanguageModels:ASurvey. arXiv:2212.10403.
ers,N.;Tan,C.;Toshev,A.;Vanhoucke,V.;Xia,F.;Xiao,T.;
Jaderberg,M.;Dalibard,V.;Osindero,S.;Czarnecki,W.M.;
Xu, P.; Xu, S.; Yan, M.; and Zeng, A. 2022. Do As I Can,
Donahue, J.; Razavi, A.; Vinyals, O.; Green, T.; Dun-
NotAsISay:GroundingLanguageinRoboticAffordances.
ning, I.; Simonyan, K.; Fernando, C.; and Kavukcuoglu,
arXiv:2204.01691.
K. 2017. Population Based Training of Neural Networks.
Brown,T.;Mann,B.;Ryder,N.;Subbiah,M.;Kaplan,J.D.; arXiv:1711.09846.
Dhariwal,P.;Neelakantan,A.;Shyam,P.;Sastry,G.;Askell,
Kojima, T.; Gu, S. S.; Reid, M.; Matsuo, Y.; and Iwasawa,
A.; et al. 2020. Language Models are Few-Shot Learners.
Y.2022. LargeLanguageModelsareZero-ShotReasoners.
InAdvancesinneuralinformationprocessingsystems,vol-
InAdvancesinneuralinformationprocessingsystems,vol-
ume33,1877–1901.
ume35,22199–22213.
Bubeck, S.; Chandrasekaran, V.; Eldan, R.; Gehrke, J.;
Li,W.;Qiao,D.;Wang,B.;Wang,X.;Jin,B.;andZha,H.
Horvitz,E.;Kamar,E.;Lee,P.;Lee,Y.T.;Li,Y.;Lundberg,
2023a. SemanticallyAlignedTaskDecompositioninMulti-
S.;Nori,H.;Palangi,H.;Ribeiro,M.T.;andZhang,Y.2023.
AgentReinforcementLearning. arXiv:2305.10865.
SparksofArtificialGeneralIntelligence:EarlyExperiments
Li, Y.; Zhang, S.; Sun, J.; Du, Y.; Wen, Y.; Wang, X.; and
withGPT-4. arXiv:2303.12712.
Pan, W. 2023b. Cooperative Open-ended Learning Frame-
Carroll, M.; Shah, R.; Ho, M. K.; Griffiths, T.; Seshia, S.; workforZero-shotCoordination.InProceedingsofthe40th
Abbeel,P.;andDragan,A.2019. OntheUtilityofLearning InternationalConferenceonMachineLearning.PMLR.
aboutHumansforHuman-AICoordination. InAdvancesin
Li,Y.;Zhang,S.;Sun,J.;Zhang,W.;Du,Y.;Wen,Y.;Wang,
neuralinformationprocessingsystems,volume32.
X.;andPan,W.2024. TacklingCooperativeIncompatibility
Ding,Z.;Zhang,W.;Yue,J.;Wang,X.;Huang,T.;andLu, forZero-ShotHuman-AICoordination. arXiv:2306.03034.
Z.2023. EntityDividerwithLanguageGroundinginMulti- Liang, J.; Huang, W.; Xia, F.; Xu, P.; Hausman, K.; Ichter,
AgentReinforcementLearning.InInternationalConference
B.;Florence,P.;andZeng,A.2023. CodeasPolicies:Lan-
onMachineLearning,8103–8119.PMLR. guage Model Programs for Embodied Control. In 2023
Du, Y.; Watkins, O.; Wang, Z.; Colas, C.; Darrell, T.; IEEEInternationalConferenceonRoboticsandAutomation
Abbeel, P.; Gupta, A.; and Andreas, J. 2023. Guiding Pre- (ICRA),9493–9500.IEEE.
training in Reinforcement Learning with Large Language Lucas, K.; and Allen, R. E. 2022. Any-Play: An Intrinsic
Models. arXiv:2302.06692. AugmentationforZero-ShotCoordination. InInternational
Fan,L.;Wang,G.;Jiang,Y.;Mandlekar,A.;Yang,Y.;Zhu, FoundationforAutonomousAgentsandMultiagentSystems,
H.; Tang, A.; Huang, D.-A.; Zhu, Y.; and Anandkumar, A. 853–861.
2022. MineDojo: Building Open-Ended Embodied Agents Lupu, A.; Cui, B.; Hu, H.; and Foerster, J. 2021. Trajec-
withInternet-ScaleKnowledge.InNIPSProcessingSystems toryDiversityforZero-ShotCoordination. InInternational
DatasetsandBenchmarksTrack. conferenceonmachinelearning,7204–7213.PMLR.

Meng, L.; Wen, M.; Yang, Y.; Le, C.; Li, X.; Zhang, W.; Wang, Z.; Cai, S.; Liu, A.; Jin, Y.; Hou, J.; Zhang, B.;
Wen, Y.; Zhang, H.; Wang, J.; and Xu, B. 2022. Offline Lin, H.; He, Z.; Zheng, Z.; Yang, Y.; Ma, X.; and Liang,
Pre-trainedMulti-AgentDecisionTransformer:OneBigSe- Y. 2023c. JARVIS-1: Open-World Multi-Task Agents
quenceModelTacklesAllSMACTasks.arXiv:2112.02845. with Memory-Augmented Multimodal Language Models.
arXiv:2311.05997.
Mialon, G.; Dess`ı, R.; Lomeli, M.; Nalmpantis, C.; Pa-
sunuru, R.; Raileanu, R.; Rozie`re, B.; Schick, T.; Dwivedi- Wei,J.;Wang,X.;Schuurmans,D.;Bosma,M.;brianichter;
Yu,J.;Celikyilmaz,A.;Grave,E.;LeCun,Y.;andScialom, Xia, F.; Chi, E. H.; Le, Q. V.; and Zhou, D. 2022. Chain
T. 2023. Augmented Language Models: a Survey. ofThoughtPromptingElicitsReasoninginLargeLanguage
arXiv:2302.07842. Models. InAdvancesinNeuralInformationProcessingSys-
tems,volume35,24824–24837.
Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright,
C.; Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, Welleck, S.; Lu, X.; West, P.; Brahman, F.; Shen, T.;
A.; Schulman, J.; Hilton, J.; Kelton, F.; Miller, L.; Simens, Khashabi, D.; and Choi, Y. 2023. Generating Sequences
M.;Askell,A.;Welinder,P.;Christiano,P.F.;Leike,J.;and byLearningtoSelf-Correct. InTheEleventhInternational
Lowe, R. 2022. Training Language Models to Follow In- ConferenceonLearningRepresentations.
structions with Human Feedback. In Advances in Neural Wen, M.; Kuba, J.; Lin, R.; Zhang, W.; Wen, Y.; Wang, J.;
InformationProcessingSystems,volume35,27730–27744. and Yang, Y. 2022. Multi-Agent Reinforcement Learning
Paul, D.; Ismayilzada, M.; Peyrard, M.; Borges, B.; is a Sequence Modeling Problem. In Advances in Neural
Bosselut, A.; West, R.; and Faltings, B. 2023. RE- InformationProcessingSystems,volume35,16509–16521.
FINER: Reasoning Feedback on Intermediate Representa- Wu, S. A.; Wang, R. E.; Evans, J. A.; Tenenbaum, J. B.;
tions. arXiv:2304.01904. Parkes, D. C.; and Kleiman-Weiner, M. 2021. Too Many
Rashid,T.;Samvelyan,M.;Schroeder,C.;Farquhar,G.;Fo- Cooks: Bayesian Inference for Coordinating Multi-Agent
erster,J.;andWhiteson,S.2018. QMIX:MonotonicValue Collaboration. TopicsinCognitiveScience,13(2):414–432.
FunctionFactorisationforDeepMulti-AgentReinforcement Yang,Y.;andWang,J.2021. AnOverviewofMulti-Agent
Learning. In International Conference on Machine Learn- Reinforcement Learning from Game Theoretical Perspec-
ing,4295–4304.PMLR. tive. arXiv:2011.00583.
Shinn, N.; Cassano, F.; Gopinath, A.; Narasimhan, K. R.; Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan,
andYao,S.2023. Reflexion:LanguageAgentswithVerbal K.R.;andCao,Y.2023.ReAct:SynergizingReasoningand
Reinforcement Learning. In Thirty-seventh Conference on ActinginLanguageModels. InTheEleventhInternational
NeuralInformationProcessingSystems. ConferenceonLearningRepresentations.
Singh, I.; Blukis, V.; Mousavian, A.; Goyal, A.; Xu, D.; Yu,C.;Velu,A.;Vinitsky,E.;Gao,J.;Wang,Y.;Bayen,A.;
Tremblay, J.; Fox, D.; Thomason, J.; and Garg, A. 2023. and Wu, Y. 2022. The Surprising Effectiveness of PPO in
ProgPrompt: Generating Situated Robot Task Plans using CooperativeMulti-AgentGames. InAdvancesinNeuralIn-
LargeLanguageModels. In2023IEEEInternationalCon- formationProcessingSystems,volume35,24611–24624.
ferenceonRoboticsandAutomation(ICRA),11523–11530. Zhang,H.;Du,W.;Shan,J.;Zhou,Q.;Du,Y.;Tenenbaum,
IEEE. J. B.; Shu, T.; and Gan, C. 2023. Building Cooperative
Strouse,D.;McKee,K.;Botvinick,M.;Hughes,E.;andEv- EmbodiedAgentsModularlywithLargeLanguageModels.
erett,R.2021. CollaboratingwithHumanswithoutHuman arXiv:2307.02485.
Data. In Advances in Neural Information Processing Sys- Zhang,K.;Yang,Z.;andBas¸ar,T.2021. Multi-AgentRein-
tems,volume34,14502–14515. forcementLearning:ASelectiveOverviewofTheoriesand
Algorithms. Handbookofreinforcementlearningandcon-
Tesauro, G. 1994. TD-Gammon, a self-teaching backgam-
trol,321–384.
monprogram,achievesmaster-levelplay. Neuralcomputa-
tion,6(2):215–219. Zhao, R.; Song, J.; Yuan, Y.; Hu, H.; Gao, Y.; Wu, Y.;
Sun, Z.; and Yang, W. 2023. Maximum Entropy Popula-
Wang, X.; Wei, J.; Schuurmans, D.; Le, Q. V.; Chi, E. H.;
tionBasedTrainingforZero-ShotHuman-AICoordination.
Narang, S.; Chowdhery, A.; and Zhou, D. 2023a. Self-
InProceedingsoftheAAAIConferenceonArtificialIntelli-
ConsistencyImprovesChainofThoughtReasoninginLan-
gence,5,6145–6153.
guageModels.InTheEleventhInternationalConferenceon
LearningRepresentations. Zhong, Y.; Kuba, J. G.; Feng, X.; Hu, S.; Ji, J.; and Yang,
Y. 2023. Heterogeneous-Agent Reinforcement Learning.
Wang, Y.; Zhong, F.; Xu, J.; and Wang, Y. 2021. ToM2C:
arXiv:2304.09870.
Target-oriented Multi-agent Communication and Coopera-
tion with Theory of Mind. In International Conference on Zhou, D.; Scha¨rli, N.; Hou, L.; Wei, J.; Scales, N.; Wang,
LearningRepresentations. X.; Schuurmans, D.; Cui, C.; Bousquet, O.; Le, Q. V.; and
Chi, E. H. 2023. Least-to-Most Prompting Enables Com-
Wang,Z.;Cai,S.;Chen,G.;Liu,A.;Ma,X.;andLiang,Y.
plexReasoninginLargeLanguageModels. InTheEleventh
2023b. Describe,Explain,PlanandSelect:InteractivePlan-
InternationalConferenceonLearningRepresentations.
ningwithLLMsEnablesOpen-WorldMulti-TaskAgents.In
Thirty-seventh Conference on Neural Information Process-
ingSystems.
