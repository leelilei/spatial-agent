Title: Introduction

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/review_library/09_Zhang2024_VLN_Foundation_Models_Survey.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:38+00:00
- page_count: 32
- status: ok
- text_char_count: 129501

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Background and Task Formulations (page 3)
  - Cognitive Underpinnings of VLN (page 3)
  - Relevant Tasks and Scope of the Survey (page 4)
  - VLN Task Formulations and Benchmarks (page 4)
  - Foundation Models (page 6)
- World Model: Learning and Representing the Visual Environments (page 6)
  - History and Memory (page 6)
  - Generalization across Environments (page 7)
- Human Model: Interpreting and Communicating with Humans (page 8)
  - Ambiguous Instructions (page 8)
  - Generalization of Grounded Instructions (page 9)
- VLN Agent: Learning an Embodied Agent for Reasoning and Planning (page 9)
  - Grounding and Reasoning (page 10)
  - Planning (page 10)
  - Foundation Models as VLN Agents (page 11)
- Challenges and Future Directions (page 12)
- Broader Impact (page 14)
- Acknowledgement (page 14)

Markdown Content:

Published in Transactions on Machine Learning Research (12/2024)
Vision-and-Language Navigation Today and Tomorrow:
A Survey in the Era of Foundation Models
Yue Zhang1∗ zhan1624@msu.edu
Ziqiao Ma2∗ marstin@umich.edu
Jialu Li3∗ jialuli@cs.unc.edu
Yanyuan Qiao4∗ yanyuan.qiao@adelaide.edu.au
Zun Wang3∗ zunwang@cs.unc.edu
Joyce Chai2† chaijy@umich.edu
Qi Wu4† qi.wu01@adelaide.edu.au
Mohit Bansal3† mbansal@cs.unc.edu
Parisa Kordjamshidi1† kordjams@msu.edu
1 Michigan State University 2 University of Michigan 3 UNC Chapel Hill 4 University of Adelaide
∗Equal Contribution † Equal Supervision
Reviewed on OpenReview: https://openreview.net/forum?id=yiqeh2ZYUh
Abstract
Vision-and-Language Navigation (VLN) has gained increasing attention over recent years
andmanyapproacheshaveemergedtoadvancetheirdevelopment. Theremarkableachieve-
ments of foundation models have shaped the challenges and methods for VLN research. In
thissurvey, weprovideatop-downreviewthatadoptsaprincipledframeworkforembodied
planningandreasoning,andemphasizesthecurrentmethodsandfutureopportunitieslever-
agingfoundationmodelstoaddressVLNchallenges. Wehopeourin-depthdiscussionscould
provide valuable resources and insights: on the one hand, to document the progress and ex-
ploreopportunitiesandpotentialrolesforfoundationmodelsinthisfield, andontheother,
to organize different challenges and solutions in VLN to foundation model researchers1.
1 Introduction
Developingembodiedagentsthatarecapableofinteractingwithhumansandtheirsurroundingenvironments
isoneofthelongstandinggoalsofArtificialIntelligence(AI)(Nguyenetal.,2021;Duanetal.,2022). These
AI systems hold immense potential for real-world applications to serve as multi-functional assistants in
daily life, such as household robots (Szot et al., 2021), self-driving cars (Hu et al., 2023), and personal
assistants (Chu et al., 2023). One formal problem setting to advance this research direction is Vision-and-
Language Navigation (VLN) (Anderson et al., 2018), a multimodal and cooperative task that requires the
agenttofollowhumaninstructions, explore3Denvironments, andengageinsituatedcommunicationsunder
variousformsofambiguity. Overtheyears,VLNhasbeenexploredinbothphotorealisticsimulators(Chang
etal.,2018;Savvaetal.,2019;Xiaetal.,2018)andrealenvironments(Mirowskietal.,2018;Banerjeeetal.,
1GitHubrepository: https://github.com/zhangyuejoslin/VLN-Survey-with-Foundation-Models
1
4202
ceD
92
]LC.sc[
2v53070.7042:viXra

Published in Transactions on Machine Learning Research (12/2024)
2021), leading to a number of benchmarks (Anderson et al., 2018; Ku et al., 2020; Krantz et al., 2020) that
each presents slightly different problem formulations.
Recently, foundation models (Bommasani et al.,
2021), ranging from early pre-trained models like
BERT (Kenton & Toutanova, 2019) to contem- World Model Grounding & Reasoning Human Model
porary large language models (LLMs) and vision- ✅ … enter the room.
l
f
a
o
n
rd
gu
e
a
t
g
a
e
l
m
.,
o
2
d
0
e
2
l
1
s
)
(
,
V
h
L
a
M
ve
s)
ex
(
h
A
i
c
b
h
it
ia
e
m
d e
e
x
t
c
a
e
l
p
.,
ti
2
o
0
n
2
a
3
l
;
a
R
b
a
il
d
i-
- ❎
Pl a n
ni ng D ia lo
gu e The room
L R
o
e i
n
g ft h ？
t
t
h
？
e
ties in multimodal comprehension, reasoning, and left or in the front?
VLN Agent Left.
cross-domain generalization. These models are pre-
Visual Navigation Language Language
trained on massive data, such as text, images, au- Perception Execution Response Instruction
Walk through the
dio, and video, and could further be adapted for The room on living room area
abroadrangeofspecificapplications,includingem- the left or in into the hallway.
the front? Turn right, then
bodiedAItasks(Xuetal.,2024b). Integratingthese Left. en tu t r e n r t r h ig e h r t o a o n m d .
foundation models into the VLN task marks a piv-
❓
otal recent advancement for embodied AI research,
demonstrated through significant performance im-
provements(Chenetal.,2021b;Wangetal.,2023h;
Zhou et al., 2024a). Foundation models have also Physical Environment Human
brought new opportunities to the VLN field, such
as expanding the research focus from multi-modal Figure 1: Organizing challenges and solutions in VLN
attention learning and strategy policy learning to using LAW framework (Hu & Shu, 2023).
pre-traininggenericvisionandlanguagerepresenta-
tions, hence enabling task planning, commonsense reasoning, as well as generalize to realistic environments.
Despite the recent impact of foundation models on VLN research, the previous surveys on VLN (Gu et al.,
2022; Park & Kim, 2023; Wu et al., 2024) are from the pre-foundation-model era and mainly focus on
the VLN benchmarks and conventional approaches, i.e., they are missing a comprehensive overview of the
existing methods and opportunities leveraging foundation models to address VLN challenges. Especially
with the emergence of LLMs, to the best of our knowledge, no review has yet discussed their applications in
VLNtasks. Moreover, unlikepreviouseffortsthatdiscusstheVLNtaskasanisolateddownstreamtask, the
objective of this survey is twofold: first, to milestone the progress and explore opportunities and potential
roles for foundation models in this field; second, to organize different challenges and solutions in VLN to
foundation model researchers within a systematic framework. To build this connection, we adopt the LAW
framework (Hu & Shu, 2023), where foundation models serve as backbones of world model and agent model.
This framework offers a general landscape of reasoning and planning in foundation models, and is closely
scoped with the core challenges in VLN.
Specifically, at each navigation step, the AI agents perceive the visual environment, receive language in-
structions from humans, and reason upon their representation of the world and humans to plan actions
and efficiently complete navigation tasks. As shown in Figure 1, a world model is an abstraction that
agents maintain to understand the external environment around them and how their actions change the
world state (Ha & Schmidhuber, 2018; Koh et al., 2021). This model is part of a broader agent model,
which also incorporates a human model that interprets the instructions of its human partner, thereby
informing the agent’s goals (Andreas, 2022; Ma et al., 2023). To review the growing body of work in VLN
and to understand the milestones achieved, we adopt a top-down approach to survey the field, focusing on
fundamental challenges from three perspectives:
• Learning a world model to represent the visual environment and generalize to unseen ones.
• Learning a human model to effectively interpret human intentions from grounded instructions.
• LearningaVLNagentthatleveragesitsworldandhumanmodeltogroundlanguage,communicate,
reason, and plan, enabling it to navigate environments as instructed.
2

Published in Transactions on Machine Learning Research (12/2024)
World Human VLN Agent Dataset
Name
Domain Environment Turn Format Gran. Type Act. Sp. Other Text Route
LANI/CHAI(2018) Indoors CHALET Single MultiInstr A - Disc Mani H H
R2R(2018) Indoors Matterport3D Single MultiInstr A Robot Graph H P
R4R(2019) Indoors Matterport3D Single MultiInstr A Robot Graph H P
RxR(2020) Indoors Matterport3D Single MultiInstr A Robot Graph H P
SOON(2021a) Indoors Matterport3D Single MultiInstr G Robot Graph H P
REVERIE(2020b) Indoors Matterport3D Single MultiInstr A,G Robot Graph Detect H P
VNLA(2019) Indoors Matterport3D Multi MultiInstr A,G Robot Graph T P
HANNA(2019) Indoors Matterport3D Multi MultiInstr A,G Robot Graph H P
CVDN(2020) Indoors Matterport3D Multi Restricted A Robot Graph H H
VLN-CE(2020) Indoors Habitat,Matterport3D Single MultiInstr A Robot Disc H P
Robo-VLN(2021) Indoors Habitat,Matterport3D Single MultiInstr A Robot Cont H P
RobotSlang(2021) Indoors Real Multi Freeform A Robot Disc H P
ALFRED(2020) Indoors AI2-THOR Single MultiInstr. A,G Robot Disc Mani H P
TEACh(2022) Indoors AI2-THOR Multi Freeform A,G Robot Disc Mani H H
DialFRED(2022) Indoors AI2-THOR Multi Restricted A,G Robot Disc Mani H,T P
TouchDown(2019) Outdoors GoogleStreetView Single MultiInstr A - Graph H P
StreetNav(2020) Outdoors GoogleStreetView Multi MultiInstr A - Disc T P
Talk2Nav(2021) Outdoors GoogleStreetView Single MultiInstr A,G - Disc H P
TtW(2018) Outdoors Real Multi Freeform A,G - Disc H H
LCSD(2019) Outdoors CARLA Single MultiInstr A Driving Disc H P
CDNLI(2020) Outdoors CARLA Multi MultiInstr A,G Driving Cont H,T H
SDN(2022) Outdoors CARLA Multi Freeform A,G Driving Disc,Cont H H
AerialVLN(2023b) Outdoors AirSim Single MultiInstr A,G Aerial Disc H H
ANDH(2023a) Outdoors xView Multi Freeform A,G Aerial Disc H H
Table 1: A summary of existing VLN benchmarks, taxonomized based on several key aspects: the world
in which navigation occurs, the type of human interaction involved, the action space and tasks assigned to
the VLN agent, and the methods of dataset collection. For the world, we consider their domain (either
indoors or outdoors) and the environment. For the human, we consider their turns of interaction
(either single or multiple turn), the format of communication (freeform dialogue, restricted dialogue, or
multiple instructions), and the language granularity (action-directed and goal-directed). For the VLN
agent, we consider their agent types (e.g., household robot, autonomous driving vehicles, or autonomous
aerial vehicles), their action space (graph-based, discrete or continuous), and other additional tasks
(manipulation and object detection). For dataset collection, we consider the text collection (by human
or templated) and the route demonstrations (by human or planner).
We present a hierarchical and fine-grained taxonomy in Figure 2 to discuss challenges, solutions, and future
directionsbasedonfoundationmodelsforeachmodel. Toorganizethissurvey,westartwithabriefoverview
of the background and related research efforts as well as the available benchmarks in this field (§2). We
structure the review around how the proposed methods have addressed the three key challenges described
above: worldmodel(§3), humanmodel(§4), andVLNagent(§5). Finally, wediscussthecurrentchallenges
and future research opportunities, particularly in light of the rise of foundation models (§6).
2 Background and Task Formulations
In this section, we discuss the background, clarify the scope of this survey, define the VLN problem, and
briefly overview the benchmarks.
2.1 Cognitive Underpinnings of VLN
Humansandothernavigationalanimalsdemonstrateearlyunderstandingandstrategiesfornavigatingtheir
environments (Rodrigo, 2002; Brand et al., 2015; Lingwood et al., 2018). For example, Gallistel (1990)
describes two basic mechanisms: piloting, which involves environmental landmarks and computes distances
andangles; andpath integration, whichcalculatesdisplacementandorientationchangesthroughself-motion
sensing. Central to understanding spatial navigation is the cognitive map hypothesis, suggesting that the
brain forms a unified spatial representation to support memory and guide navigation (Epstein et al., 2017;
Bellmund et al., 2018). For instance, Tolman (1948) observed that rats could adopt the correct novel path
when familiar paths are blocked and landmarks are absent. Neuroscientists also discovered hippocampal
3

Published in Transactions on Machine Learning Research (12/2024)
placecells, indicatingaspatialcoordinatesystemthatencodeslandmarksandgoalsallocentrically(O’Keefe
&Dostrovsky,1971;O’keefe&Nadel,1978). Recentstudiesalsoproposenon-Euclideanrepresentations,e.g.,
cognitivegraphs,whichillustratethecomplexityofhowwerepresentspatialknowledgeoftheworld(Warren,
2019;Ericson&Warren,2020). Whilevisualandauditoryperceptionsareobviouslyintegraltospatialrepre-
sentation(Klatzkyetal.,2006),ourlinguisticskillsandspatialcognitionarealsocloselyintertwined(Pruden
et al., 2011). For instance, researchers have shown that understanding different aspects of spatial language
canhelpwithspace-relatedtasks(Pyersetal.,2010),andthatlanguageinfluenceshowchildreninteractwith
spacebyassistingthemtorecognizetheimportanceoflandmarksinidentifyinglocations(Shustermanetal.,
2011). StudyingVLNnotonlyenhancesthedevelopmentofembodiedAIthatfollowshumaninstructionsin
visual environments, but also deepens our understanding of how cognitive agents develop navigation skills,
adapt to different environments, and how language use is connected to visual perceptions and actions.
2.2 Relevant Tasks and Scope of the Survey
Following natural language navigation instructions has traditionally been modeled using symbolic world
representations such as maps (Anderson et al., 1991; MacMahon et al., 2006; Paz-Argaman & Tsarfaty,
2019). However, our survey focuses on models that employ visual environments and address the challenges
of multimodal understanding and grounding. Likewise, we redirect readers to extensive surveys on visual
navigation (Zhu et al., 2021b; Zhang et al., 2022a; Zhu et al., 2022) and mobile robot navigation (Gul
et al., 2019; Crespo et al., 2020; Möller et al., 2021), which concentrate on visual perception and physical
embodiment. However,thesestudiesprovideminimaldiscussionsontheroleoflanguageinnavigationtasks.
While we inevitably extend our discussions of VLN to encompass areas beyond navigation, such as mobile
manipulationanddialogue,ourprimaryfocusremainsonnavigationaltasks,forwhichweprovideadetailed
literaturereview. Besides,unlikepreviousVLNsurveys(Guetal.,2022;Park&Kim,2023;Wuetal.,2024),
which offer a bottom-up summary focusing on benchmarks and modeling innovations, our survey adopts a
top-down approach, and uses the roles of foundation models to categorize the research efforts into three
fundamental challenges from the aspects of the world model, the human model, and the VLN agent. Note
that this survey concentrates on frontier methods associated with the rise of foundation models. Thus, we
point to the earlier generation of models (e.g., LSTM-based methods) very briefly at the beginning of each
section to motivate our discussions.
2.3 VLN Task Formulations and Benchmarks
VLN Task Definition. AtypicalVLNagentreceivesa(sequenceof)languageinstruction(s)fromhuman
instructorsatadesignatedposition. Theagentnavigatesthroughtheenvironmentusinganegocentricvisual
perspective. Byfollowingtheinstructions,itstaskistogenerateatrajectoryoverasequenceofdiscreteviews
orlower-levelactionsandcontrol(e.g.,FORWARD0.25meter)toreachthedestination,whichisconsidered
successful if the agent arrives within a specified distance (e.g., 3 meters) from the destination. Besides, the
agentmayexchangeinformationwiththeinstructorduringnavigation,eitherbyrequestinghelporengaging
infreeformlanguagecommunication. Additionally,therehasbeenanincreasingexpectationforVLNagents
to integrate additional tasks such as manipulation (Shridhar et al., 2020) and object detection (Qi et al.,
2020b), along with navigation.
Benchmarks. Unlike other multimodal tasks such as VQA, which have a relatively fixed task definition
and format, VLN encompasses a wide range of benchmarks and task formulations. These distinctions intro-
duce unique challenges in addressing the broader VLN task and must be clearly understood as prerequisites
for developing effective methods with appropriate foundation models. As is summarized in Table 1, exist-
ing VLN benchmarks can be taxonomized based on several key aspects in the LAW framework: (1) the
world where navigation occurs, including the domain (indoors or outdoors) and the specifics of the envi-
ronment. (2) the type of human interaction involved, including the interaction turns (single or multiple),
communication format (freeform dialogue, restricted dialogue, or multiple instructions), and language gran-
ularity (action-directed or goal-directed). (3) the VLN agent, including its types (e.g., household robots,
autonomous driving vehicles, or autonomous aerial vehicles), action space (graph-based, discrete, or contin-
uous), and additional tasks (manipulation and object detection). (4) the dataset collection, including text
4

Published in Transactions on Machine Learning Research (12/2024)
Environment
Augmentation
Instruction Synthesis
LLM Planner
sdohteM
noitagivaN
egaugnaL-dna-noisiV
History and History Encoding The Role of Foundation Models
Memory
Graph-based History destination Data and Knowledge Decision Making
encode
• preprocess, augment, • a navigation planner;
World edit existing data; • a dialogue manager to
Model • synthesize new data; seek information;
Generalization
P
R
re
e
-
p
t
r
r
e
a
s
in
en
ed
ta
V
ti
i
o
s
n
u
s
al generalize
unseen
•
c
k
o
n
le
m
o
v
w
m
er
le
o
a
d
n
g
g
e
s
e
e
t
n
h
in
s
e
e
t
a
h
c
e
q uired •
d e
a
c
g
is
e
i
n
o
e
n
r
-
a
m
l-
a
p
k
u
i
r
n
p
g
o
a
s
g
e
e nt.
Ability Pre-trained Text pre-training data.
Representations “Walk through the living room area
Human i t n u t r o n t r h i e g h h t a a ll n w d a e y n . t T e u r r t n h e r i r g o h o t m , t . h ” en “ b G at o h t r o o t o h m e .” Representation Task Learning
Model 👤 Walk through the living room area into the hallway. • generalizable text • embodied reasoning;
representations; • language grounding;
A In m st b r i u g c u t o io u n s I P a n n e fo r d r c m C ep o a t m t u io a m l n o C S n o e s n e e t k n e i s x n e t g 🤖 M W o h v e e re f o is r w th a e r h d a a ll n w d a l y o ? ok around. • r • e g l p e e a r n e r e n s r e , a n m l t iz a a a t i i n b o t l n e a s i v n ; i , s o u r a l • t le a l a s e r k a n s r i n b n i y g n , f g e i n e w m - - c s o b h n o o d t t e i x e t d
🤖 Forward process the history and learning or fine-tuning.
memory information.
Grounding and Explicit Grounding 👤 Turn right, then turn right. Challenges and Future Work
Reasoning VLN Pre-training F F o o r r w w a a r r d d . . F R o ig r h w t a . rd. F F o o r r w w a a r r d d . . Right. Benchmarks Limitations of Data and Task
Graph Planner Agent Model Adapting LLMs and VLMs
VLN Planning 👤 Enter the room.
Agent 🤖Which room? Human Model Instruction ⟶ Dialogue
The room on the left or in the front?
VLM Agents World Model 2D World ⟶ 3D World
Agent Models Left. 👤
LLM Agents 🤖 Left Deployment Simulation ⟶ Real Robots
Figure 2: VLN challenges and solutions within the framework of world model, human model, and VLN
agent. We discuss history and memory in the world model, ambiguous instructions in the human model,
generalization ability in them both. For the VLN agent, we discuss methods for grounding and reasoning,
planning,andadaptingfoundationmodelsasagents. Dependingontheroleservedbythefoundationmodels,
we categorize these methods into four types. Additionally, we discuss the potential future of the foundation
model for the VLN task.
collectionmethod(human-generatedortemplated)androutedemonstrations(human-performedorplanner-
generated). Representatively, Anderson et al. (2018) create the Room-to-Room (R2R) dataset based on the
Matterport3Dsimulator(Changetal.,2018),whereanagentneedstofollowfine-grainednavigationinstruc-
tions to reach the goal. Room-across-Room (RxR) (Ku et al., 2020) is a multilingual variation, including
English, Hindi, and Telugu instructions. It offers a larger sample size and provides time-aligned instructions
forvirtualposes,enrichingthetask’slinguisticandspatialinformation. Matterport3DallowsVLNagentsto
operate in a discrete environment and rely on pre-defined connectivity graphs for navigation, where agents
travelonthegraphbyteleportationbetweenadjacentnodes,referredtoasVLN-DE.Tomakethesimplified
setting more realistic, Krantz et al. (2020); Li et al. (2022c); Irshad et al. (2021) propose VLN in continu-
ous environments (VLN-CE) by transferring discrete R2R paths to continuous spaces (Savva et al., 2019).
Robo-VLN (Irshad et al., 2021) further narrows the sim-to-real gap by introducing VLN with continuous
action spaces that are more realistic in robotics settings. Recent VLN benchmarks have undergone several
design changes and expectations, which we discuss in § 6.
Evaluation Metrics. Three main metrics have been employed to evaluate navigation wayfinding perfor-
mance (Anderson et al., 2018): (1) Navigation Error (NE), the mean of the shortest path distance between
theagent’sfinalpositionandthegoaldestination;(2)Success Rate (SR),thepercentageofthefinalposition
beingcloseenoughtothegoaldestination;and(3)SuccessRateWeightedPathLength(SPL),whichnormal-
izessuccessratebytrajectorylengthtobalanceboththesuccessrateinreachingthecorrectdestinationand
the efficiency of the path. Some other metrics are used to measure the faithfulness of instruction following
and the fidelity between the predicted and the ground-truth trajectory, for example: (4) Coverage Weighted
by Length Score (CLS) (Jain et al., 2019) measures how closely an agent’s trajectory follows the reference
path. It balances two key aspects of the agent’s performance: the extent of coverage of the reference path
and the efficiency of the agent’s navigation by considering the length score; (5) Normalized Dynamic Time
Warping (nDTW) (Ilharco et al., 2019), which penalizes deviations from the ground-truth trajectories; and
(6) Normalized Dynamic Time Warping Weighted by Success Rate (sDTW) (Ilharco et al., 2019), which
penalizes deviations from the ground-truth trajectories and also considers the success rate.
5

Published in Transactions on Machine Learning Research (12/2024)
2.4 Foundation Models
Foundation models are trained on large-scale datasets, which show strong generalization capability for a
wide range of downstream applications. Text-only foundation models, such as pre-trained language models
like BERT (Kenton & Toutanova, 2019) and GPT-3 (Brown et al., 2020), have revolutionized the field of
NLP by setting new benchmarks for tasks like text generation, translation, and understanding. Building
on the success of these models, vision-language (VL) foundation models, like LXMERT (Tan & Bansal,
2019), CLIP (Radford et al., 2021) and GPT-4 (Achiam et al., 2023), have expanded the paradigm to
multimodal learning by integrating both visual and textual data, proving particularly impactful in various
VL applications (Li et al., 2019a; Ramesh et al., 2021; Alayrac et al., 2022; Hong et al., 2021; Zhang et al.,
2025; Cheng et al., 2024; Kamali & Kordjamshidi, 2023). For a more comprehensive overview of foundation
models and their applications, we encourage readers to refer to existing survey papers such as Bommasani
et al. (2021), Du et al. (2022), and Zhou et al. (2023).
3 World Model: Learning and Representing the Visual Environments
AworldmodelhelpstheVLNagenttounderstandtheirsurroundingenvironments,predicthowtheiractions
would change the world state, and align their perception and actions with language instructions. Two
challenges have been highlighted in existing work about learning a world model: encoding the visual history
of observations within the current episode as memory, and achieving generalization to unseen environments.
3.1 History and Memory
Differentfromothervision-languagetaskslikeVisualQuestionAnswering(VQA)(Antoletal.,2015),Visual
Entailment(Xieetal.,2019),theVLNagentneedstoincorporatethehistoryinformationofpastactionsand
observations into its current step’s input to determine the action rather than solely considering the image
and text in a single step. Prior to employing the foundation models in VLN, LSTM hidden states served
as an implicit memory supporting agents’ decision-making during navigation, and researchers further design
different attention mechanisms (Tan et al., 2019; Wang et al., 2019) or auxiliary tasks (Ma et al., 2019; Zhu
et al., 2020) to improve the alignment between the encoded history and instructions.
History Encoding. Different techniques have been proposed to encode navigation history using foun-
dation models. A multi-modal Transformer is built upon encoded instructions and navigation history for
decision-making, which is usually initialized from a model pre-trained on in-domain instruction-trajectory
datalikePrevalent(Haoetal.,2020). Someapproachesencodethenavigationhistoryinrecurrentlyupdated
state tokens. Hong et al. (2021) proposes to utilize a single [CLS] token from last step for encoding the
history information, while Lin et al. (2022a) introduces a variable-length memory framework that stores
multiple action activations from previous steps in a memory bank as the history encoding. Despite their
effectiveness, these methods are limited by the need for step-by-step token updates, making it challenging
to efficiently retrieve history encodings at arbitrary steps in the navigation trajectory, which can hinder
scalability in pre-training. Another line of work directly encodes navigation history as a sequence with
multi-modal Transformer. Among them, Pashevich et al. (2021) encodes single-view images for each step
in a trajectory. Chen et al. (2021b) further proposes a panorama encoder to encode the panoramic visual
observation at each time step, followed by a history encoder to encode all the past observations. This hier-
archicaldesignseparatelyprocessesthespatialrelationshipinapanoramicviewandthetemporaldynamics
across panoramas in the navigation history. Besides, this method eliminates the dependency on recurrently
updated state tokens for history encoding, facilitating efficient and large-scale pre-training on instruction-
path pairs. Follow-up research replaces the panorama encoder with mean pooling of images (Kamath et al.,
2023) or front-view image encoding (Qiao et al., 2022), both maintaining effective navigation performance.
With the advent of LLM-based navigation agents, some works (Zhou et al., 2024b) focus on converting the
visual environment into textual descriptions, and explaining the world with text became the trend. The
navigation history is then encoded as a sequence of these image descriptions, along with relative spatial
information such as heading, elevation, and distance. HELPER (Sarch et al., 2023) designs an external
6

Published in Transactions on Machine Learning Research (12/2024)
memory of language-program pairs that parses the free-form human-robot dialogue into action programs
through retrieval-augmented LLM prompting.
Graph-based History. Another line of research enhances the navigation history modeling with graph
information. For example, some of these techniques utilize a structured Transformer encoder to capture
the geometric cues in the environment (Chen et al., 2022c; Deng et al., 2020; Wang et al., 2023b; Zhou &
Mu, 2023; Su et al., 2023; Zheng et al., 2024b; Wang et al., 2021; Chen et al., 2021a; Zhu et al., 2021a).
In addition to the topological graph used in encoding, many works propose to include the top-down view
information(e.g.,gridmap(Wangetal.,2023g;Liuetal.,2023a),semanticmap(Hongetal.,2023a;Huang
et al., 2023a; Georgakis et al., 2022; Anderson et al., 2019; Chen et al., 2022a; Irshad et al., 2022), local
metrics map (An et al., 2023)), and local neighborhood map (Gopinathan et al., 2023) in modeling the
observation history during navigation. Recent advances in LLM-based navigation agents have introduced
innovative approaches to memory construction using maps. For instance, Chen et al. (2024a) proposes a
novel map-guided GPT-based agent that utilizes a linguistical-formed map to store and manage topological
graph information. MC-GPT (Zhan et al., 2024b) introduces a topological map as the memory structure to
record information about viewpoints, objects, and their spatial relationships.
3.2 Generalization across Environments
One main challenge in the VLN is learning from limited available environments and generalizing to new and
unseen environments. Many works demonstrate that learning from semantic segmentation features (Zhang
etal.,2021a),dropoutinformationintheenvironmentduringtraining(Tanetal.,2019),andmaximizingthe
similarity between semantically-aligned image pairs from different environments (Li et al., 2022a) improve
agents’ generalization performance to unseen environments. These observations suggest the need to learn
from large-scale environment data to avoid overfitting to training environments. Next, we discuss how
existing works collect new environment data, and utilize it in training.
Pre-trained Visual Representations. Most works obtain vision representations from ResNet pre-
trained on ImageNet (Anderson et al., 2018; Tan et al., 2019). Shen et al. (2022) replace ResNet with
the CLIP visual encoder (Radford et al., 2021), which is pre-trained with contrastive loss between image-
text pairs and naturally better aligns the image with the instructions, boosting the VLN performance.
Wang et al. (2022b) further explores transferring vision representation learned from video data for VLN
task, suggesting that temporal information learned from video is crucial for navigation.
Environment Augmentation. One main line of research focuses on augmenting the navigation environ-
ment with auto-generated synthetic data. EnvEdit (Li et al., 2022b), EnvMix (Liu et al., 2021), KED (Zhu
etal.,2023),andFDA(Heetal.,2024a)generatesyntheticdatabychangingtheexistingenvironmentsfrom
Matterport3D.Specifically,theymixuproomsfromdifferentenvironments,changetheappearanceandstyle
of the environments, and interpolate high-frequency features with the environments. Pathdreamer (Koh
et al., 2021) and SE3DS (Koh et al., 2023) further synthesize the environments in future steps given current
observations and explore utilizing the synthesis view as augmented data for VLN training.
Thelearningparadigmfromthecollectedenvironmentshaschangedwiththeadvancesinfoundationmodels.
Prior to the prevalence of pre-training in foundation models, most works directly augment the training
environment with the auto-collected new environments and fine-tune a LSTM-based VLN agent (Li et al.,
2022b; Liu et al., 2021; Koh et al., 2021; 2023; Zhu et al., 2023). As pre-training has been demonstrated
to be crucial for foundation models, it has also become a standard practice in VLN to learn from collected
environmentsduringthepre-trainingstage(Li&Bansal,2024;Kamathetal.,2023;Chenetal.,2022b;Wang
etal.,2023h;Linetal.,2023b;Guhuretal.,2021a;Heetal.,2024a). Large-scalepre-trainingwithaugmented
in-domain data has become crucial in bridging the gap between agents’ and humans’ performance. The in-
domain pre-trained multi-modal transformer has been proven to be more effective than the multi-modal
Transformer initialized from VLMs, like Oscar (Li et al., 2020) and LXMERT.
7

Published in Transactions on Machine Learning Research (12/2024)
4 Human Model: Interpreting and Communicating with Humans
Inadditiontolearningandmodelingtheworld,VLNagentsneedahumanmodelthatcomprehendshuman-
provided natural language instructions per situation to complete navigation tasks. There are two main
challenges: resolvingambiguityandgeneralizationofgroundedinstructionsindifferentvisualenvironments.
4.1 Ambiguous Instructions
Ambiguous instructions mainly arise in single-turn navigation scenarios, where the agent follows an initial
instruction without further human interaction for clarification. These instructions lack the flexibility to
traintheagenttoadaptitslanguageunderstandingandvisualperceptiontothedynamicenvironments. For
instance, instructions may contain landmarks invisible at the current view or indistinguishable landmarks
visible from multiple views (Zhang & Kordjamshidi, 2023). The issue of ambiguous instructions is barely
addressed before the application of foundational models to VLN. Although LEO (Xia et al., 2020) attempts
to aggregate multiple instructions to describe the same trajectory from different perspectives, it still relies
onhuman-annotatedinstructions. However,comprehensiveperceptualcontextandcommonsenseknowledge
from foundational models enable the agent to interpret ambiguous instructions using external knowledge, as
well as seek assistance from other human models.
Perceptual Context and Commonsense Knowledge. Large-scalecross-modalpre-trainedmodelslike
CLIParecapableofmatchingvisualsemanticswithtext. ThisenablestheVLNagenttoutilizeinformation
from the visual objects and their states in the current perception to resolve ambiguity, especially in single-
turn navigation scenarios. For example, VLN-Trans (Zhang & Kordjamshidi, 2023) constructs easy-to-
follow sub-instructions with visible and distinctive objects obtained from CLIP to pre-train a Translator
that converts original ambiguous instructions into easily understandable sub-instruction representations.
LANA+ (Wang et al., 2023f) leverages CLIP to query a text list of landmark semantic tags with the visual
panoramic observations, and selects the top-ranked retrieved textual cues as representations of the salient
landmarks to follow. KERM (Li et al., 2023a) proposes a knowledge-enhanced reasoning model to retrieve
facts where knowledge is described by language descriptions for the navigation views. NavHint (Zhang
etal.,2024b)constructsahintdataset, providingdetailedvisualdescriptionstohelptheVLNagentbuilda
comprehensiveunderstandingofthevisualenvironmentratherthanfocusingsolelyontheobjectsmentioned
intheinstructions. Ontheotherhand,thecommonsensereasoningabilityofLLMscanbeusedtoclarifyor
correctambiguouslandmarksintheinstructions,andbreakinstructionsintoactionableitems. Forexample,
Linetal.(2024b)useLLMstoprovidecommonsenseaboutopen-worldlandmarkco-occurrencesandconduct
CLIP-drivenlandmarkdiscoveryaccordingly. SayCan(Ahnetal.,2022)breaksaninstructionintoaranked
list of pre-defined admissible actions and combines them with an affordance function that assigns higher
weights to the objects appearing in the current scene.
Information Seeking. While ambiguous instructions can be resolved based on visual perception and
situational context, another more direct approach is to seek help from the communication partner, i.e.,
the human speakers who generate the instructions (Nguyen & Daumé III, 2019; Paul et al., 2022). There
are three key challenges in this line of work: (1) deciding when to ask for help (Chi et al., 2020); (2)
generating information-seeking questions, e.g., next action, objects, and directions (Roman et al., 2020;
Singhetal.,2022);(3)developinganoraclethatprovidesthequeriedinformation,whichcouldbeeitherreal
humans(Singhetal.,2022), rulesandtemplates(Gaoetal.,2022), orneuralmodels(Nguyen&DauméIII,
2019). LLMs and VLMs could potentially fit two roles in this framework, either as information-seeking
models, orasproxiesforhumanhelpersorinformation-providingmodels. Preliminaryresearchhasexplored
theuseofLLMsastheinformation-seekingmodel,addressingdeterminingbothwhenandwhattoask. This
is achieved with the help of techniques including conformal prediction (CP) (Ren et al., 2023) or in-context
learning(ICL)(Chenetal.,2023c). Forthelatter,foundationmodelsplaytheroleofahelperwhohasaccess
to oracle information, such as the location of the destination and a map of the environment, which is not
available to the task performer. Very recently, VLN-Copilot (Qiao et al., 2024) enables agents to actively
seek assistance when encountering confusion, with the LLM serving as a copilot to facilitate navigation.
Fan et al. (2023b) demonstrate that GPT-3 can decompose ground-truth responses in the training data
8

Published in Transactions on Machine Learning Research (12/2024)
step-by-step, which helps in training an oracle model using a pre-trained SwinBert (Lin et al., 2022b) video-
languagemodel. Theyalsodemonstratelargevision-languagemodelslikemPLUG-Owl(Yeetal.,2023)can
serve as strong zero-shot oracles off the shelf. In addition, self-motivated communication agents have been
developed (Zhu et al., 2021c) by learning the confidence of the oracle to produce a positive answer, which
enables a self-Q&A manner where the oracle can be removed at inference time.
4.2 Generalization of Grounded Instructions
The limited scale and diversity of navigation data is another significant issue affecting the VLN agent’s
abilitytocomprehendvariouslinguisticexpressionsandfollowinstructionseffectively,particularlyinunseen
navigation environments. Although the language style itself has good generalization capability across seen
andunseenenvironments(Zhangetal.,2021a),howtogroundtheinstructionswiththeunseenenvironments
is potentially a hard task given the limited scale of training instructions. Foundation models help address
these issues through both pre-trained representations and instruction generation for data augmentation.
Pre-trained Text Representations. Before the foundation models, many works rely on text encoders,
such as LSTM, to represent text instructions (Anderson et al., 2018; Tan et al., 2019). The foundation
models significantly enhance the VLN agent’s language generalization ability through pre-trained represen-
tations. For example, PRESS (Li et al., 2019b) fine-tunes the pre-trained language model BERT (Kenton &
Toutanova,2019)toobtaintextrepresentationsthatgeneralizebettertopreviouslyunseeninstructions. The
multi-modalTransformers(Tan&Bansal,2019;Luetal.,2019)boostmethods,suchasVLN-BERT(Majum-
daretal.,2020)andPREVALENT(Haoetal.,2020),toobtainmoregenericvision-linguisticrepresentations
by pre-training on large-scale text-image pairs collected from the web. Airbert (Guhur et al., 2021b) trains
ViLBERT-like architecture to learn text representations from image-caption pairs collected from the Inter-
net. CLEAR(Lietal.,2022a)learnscross-linguallanguagerepresentationsthatcapturethevisualconcepts
behind the instruction. ProbES (Liang et al., 2022) self-explores environments by sampling trajectories and
automatically constructs the corresponding instruction by filling the instruction templates with movements
and object phrases detected by CLIP. Additionally, it leverages prompt-based learning to facilitate fast
adaptation of language embeddings. NavGPT-2 (Zhou et al., 2025) explores leveraging vision-and-language
representations from pre-trained VLMs (InstructBLIP (Dai et al., 2024) with Flan-T5 (Chung et al., 2024)
or Vicuna (Zheng et al., 2023)) to enhance policy learning for navigation and navigational reasoning.
Instruction Synthesis. Another method to improve the agent’s generalization ability is to synthesize
more instructions. Early works employ the Speaker-Follower framework (Fried et al., 2018; Tan et al., 2019;
Kurita & Cho, 2020; Guhur et al., 2021a) to train an offline speaker (instruction generator) using human-
annotated instruction-trajectory pairs. It then generates new instructions based on sequences of panoramas
along a given trajectory. However, Zhao et al. (2021) observe that these generated instructions are low-
quality and show a poor performance in human wayfinding evaluation. Marky (Wang et al., 2022a; Kamath
et al., 2023) addresses this limitation using a multi-modal extension of the multilingual T5 model (Xue
et al., 2020) with text-aligned visual landmark correspondences, achieving near-human quality on R2R-style
paths in unseen environments. PASTS (Wang et al., 2023c) introduces a progress-aware spatial-temporal
Transformer speaker to better leverage the sequenced multiple vision and action features. SAS (Gopinathan
etal.,2024)generatesinstructionswithrichspatialinformationusingsemanticandstructuralcuesfromthe
environment. SRDF (Wang et al., 2024c) builds a strong instruction generator with iterative self-training.
Additionally, instead of training an offline instruction generator, some recent research (Liang et al., 2022;
Lin et al., 2023b; Zhang & Kordjamshidi, 2023; Wang et al., 2023e; Magassouba et al., 2021) generates
instructions while navigating. For instance, LANA (Wang et al., 2023e) introduces a language-capable
navigation agent that not only executes navigation instructions but also provides route descriptions.
5 VLN Agent: Learning an Embodied Agent for Reasoning and Planning
While the world and human models empower visual and language understanding abilities, VLN agents
need to develop embodied reasoning and planning capabilities to support their decision-making. From this
9

Published in Transactions on Machine Learning Research (12/2024)
perspective, wediscusstwochallenges: groundingandreasoning, andplanning. Wealsoexplorethemethod
of directly applying foundation models as the VLN agent backbone.
5.1 Grounding and Reasoning
DifferentfromotherVLtasks,suchasVQAandImageCaptioning,whichprimarilyfocusonstaticalignment
between images and corresponding textual descriptions, the VLN agent needs to reason about spatial and
temporal dynamics in the instructions and the environment based on its actions. Specifically, the agent
should consider previous actions, identify the part of the sub-instruction to execute, and ground the text
to the visual environment to execute the action accordingly. Previous methods primarily rely on explicit
semantic modeling or auxiliary task design to obtain such abilities. However, pre-training with specially
designed tasks has become the dominant approach with the advent of foundation models.
Explicit Semantic Grounding. The previous efforts enhance the agent’s grounding ability through ex-
plicit semantic modeling in both vision and language modalities, including modeling motions and land-
marks(Hongetal.,2020b;Heetal.,2021;Hongetal.,2020a;Zhangetal.,2021b;Qietal.,2020a),utilizing
syntacticinformationintheinstruction(Lietal.,2021), aswellasspatialrelations(Zhang&Kordjamshidi,
2022b; An et al., 2021). Very few works (Lin et al., 2023a; Zhan et al., 2024a; Wang et al., 2023b) ex-
plore explicit grounding in the VLN agent with the foundation models. Lin et al. (2023a) proposes actional
atomic-concept learning and map visual observations to faciliate multi-modal alignments.
Pre-training VLN Foundation Models. Except for explicit semantic modeling, the previous research
also enhances the agent’s grounding ability through auxiliary reasoning tasks (Ma et al., 2019; Wu et al.,
2021; Zhu et al., 2020; Raychaudhuri et al., 2021; Dou & Peng, 2022; Kim et al., 2021). Such methods
are less explored in VLN agents with foundation models, as their pre-training already provides a general
understanding of spatial and temporal semantics prior to navigation. Various pre-training methods with
speciallydesignedtaskshavebeenproposedtoimprovetheagent’sgroundingability. Linetal.(2021)intro-
ducepre-trainingtasksspecificallydesignedforsceneandobjectgrounding. LOViS(Zhang&Kordjamshidi,
2022a)formulatestwospecializedpre-trainingtaskstoenhanceorientationandvisualinformationseparately.
HOP(Qiao etal.,2022;2023a) introduces ahistory-and-orderaware pre-training paradigmthatemphasizes
historical information and trajectory orders. Li & Bansal (2023) suggests that enhancing the agent with the
ability to predict future view semantics helps the agent in longer path navigation performance. Dou et al.
(2023) design a masked path modeling objective to reconstruct the original path given a randomly masked
sub-path. Cui et al. (2023) propose entity-aware pre-training by predicting grounded entities and aligning
them to text.
5.2 Planning
DynamicplanningenablesVLNagentstoadapttoenvironmentalchangesandimprovenavigationstrategies
on the fly. Alongside the graph-based planners that utilize global graph information to enhance local action
spaces, the rise of foundational models, particularly LLMs, has brought LLM-based planners into the VLN
field. These planners use LLMs’ vast commonsense knowledge and advanced reasoning to create dynamic
plans that improve decision-making.
Graph-basedPlanner. RecentadvancementsinVLNemphasizeenhancingnavigationalagents’planning
capabilities through global graph information. Among them, Wang et al. (2021); Chen et al. (2022c); Deng
et al. (2020); Zheng et al. (2024b) enhance the local navigation action spaces with global action steps from
graph frontiers of visited nodes for better global planning. Gao et al. (2023) further enhances navigation
decision-making with high-level planning for zone selection and low-level planning for node selection. More-
over,Liuetal.(2023a)enrichesthegraph-frontier-basedglobalandlocalactionspaceswithgrid-levelactions
for more accurate action prediction. In continuous environments, Krantz et al. (2021); Hong et al. (2022);
Anderson et al. (2021) adopt a hierarchical planning approach utilizing high-level action spaces instead of
low-level ones by selecting a local waypoint from a predicted local navigability graph. CM2 (Georgakis
et al., 2022) facilitates trajectory planning by grounding instructions within a local map. Expanding on this
10

Published in Transactions on Machine Learning Research (12/2024)
strategy, An et al. (2024; 2023); Wang et al. (2023g); Chang et al. (2024); Wang et al. (2022c) construct
a global topological graph or grid maps to facilitate map-based global planning. Additionally, Wang et al.
(2023a; 2024a) predict multiple future waypoints using either a video prediction model or a neural radiance
representationmodeltoplanthebestactionbasedonthelong-termeffectsofpredictedcandidatewaypoints.
LLM-based Planner. Inparallel,somestudiesleveragecommon-senseknowledgefromLLMstogenerate
text-based plans (Huang et al., 2022; 2023b). LLM-Planner (Song et al., 2023) creates detailed plans com-
posed of sub-goals, dynamically adjusting these plans in real-time by integrating detected objects according
to predefined program patterns. Similarly, Mic (Qiao et al., 2023b) and A2Nav (Chen et al., 2023b) special-
ize in breaking down navigation tasks into detailed textual instructions, with Mic generating step-by-step
plans from both static and dynamic perspectives, while A2Nav uses GPT-3 to parse instructions into ac-
tionable sub-tasks. ThinkBot (Lu et al., 2023) employs thought chain reasoning to generate missing actions
with interactive objects. VL-Map (Huang et al., 2023a) decomposes navigation instructions into sequential,
goal-related functions in code format using code-written LLMs (following the Code-as-Policy (Liang et al.,
2023) framework) and utilizes a dynamically built, queryable map to guide the execution of these goals.
Additionally, SayNav (Rajvanshi et al., 2024) builds a 3D scene graph of the explored environment as input
to LLMs for generating feasible and contextually appropriate high-level plans for the navigator.
5.3 Foundation Models as VLN Agents
The architecture of VLN agents has undergone significant transformations with the advent of foundation
models. Initially conceptualized by Anderson et al. (2018), VLN agents were formulated within a Seq2Seq
framework, employing an LSTM and an attention mechanism to model the interaction between vision and
languagemodalities. Withtheadventoffoundationmodels,theagentbackendhastransitionedfromLSTM
to Transformer and, more recently, to these large-scale pre-trained systems.
VLMs as Agents. The mainstream methodology leverages single-stream VLMs as the core structure of
VLN agents (Hong et al., 2021; Qi et al., 2021; Moudgil et al., 2021; Zhao et al., 2022). These models
process inputs from language, vision, and historical tokens simultaneously at each time step. It performs
self-attentionoverthesecross-modaltokenstocapturethetextual-visualcorrespondence,whichisthenused
to infer the action probability. In the zero-shot VLN, CLIP-NAV (Dorbala et al., 2022) utilizes CLIP to
obtainnaturallanguagereferringexpressionsthatdescribethetargetobjectandmakesequentialnavigational
decisions. VLN-CEagents(Krantzetal.,2020)differentiatethemselvesfromtheVLN-DE(Andersonetal.,
2018) agents by their action space, executing low-level controls in the continuous environment instead of
graph-based high-level actions of view selection. Despite early works (Krantz et al., 2020; Raychaudhuri
et al., 2021) utilizing LSTM to infer low-level actions, the introduction of waypoint predictors has allowed
to transfer methods from DE to CE (Krantz et al., 2021; Krantz & Lee, 2022; Hong et al., 2022; Anderson
et al., 2021; An et al., 2022; Zhang & Kordjamshidi, 2024). All these methods use a waypoint predictor to
obtainalocalnavigabilitygraph,allowingfoundationmodelsinDEtoadapttothecontinuousenvironment.
In particular, the waypoint detection process primarily involves using visual observations (e.g., panoramic
RGBD images) to predict navigable candidate adjacent waypoints from the agent’s current position as
possible targets. Given the predicted waypoints, the agent selects one as the current destination.
LLMs as Agents. Since LLMs have powerful reasoning ability and semantic abstraction of the world,
and also show strong generalization ability in unknown large-scale environments, recent research in VLN
has started to directly employ LLMs as agents to complete navigation. Typically, visual observations are
converted into textual descriptions and fed into the LLM along with instructions, which then perform ac-
tion predictions. Innovations such as NavGPT (Zhou et al., 2024a) and MapGPT (Chen et al., 2024a)
demonstrate the feasibility of zero-shot navigation, with NavGPT autonomously generating actions using
GPT-4 and MapGPT converting topological maps into global exploration hints. DiscussNav (Long et al.,
2024b) extends this approach by deploying multiple domain-specific VLN experts to automate and reduce
humaninvolvementinnavigationtasks. ItincludesInstructionAnalysisExperts,VisionPerceptionExperts,
Completion Estimation Experts, and Decision Testing Experts. The use of multiple domain-specific VLN
experts distributes tasks among specialized agents, reducing the burden on a single model and allowing
11

Published in Transactions on Machine Learning Research (12/2024)
for optimized, task-specific processing. This multi-expert approach enhances robustness, transparency, and
overall performance by leveraging the collective strengths of multiple large models. MC-GPT (Zhan et al.,
2024b) employs memory topology maps and human navigation examples to diversify strategies, while In-
structNav (Long et al., 2024a) breaks navigation into sub-tasks with multi-sourced value maps for effective
execution. In contrast to zero-shot usage, some works (Zheng et al., 2024a; Zhang et al., 2024a; Pan et al.,
2024) fine-tune LLMs to address the embodied navigation tasks effectively. Some studies have incorporated
theChain-of-Thought(CoT)(Weietal.,2022)reasoningmechanismtoimprovethereasoningprocess. Nav-
CoT (Lin et al., 2024a) transforms LLMs into a world model and navigational reasoning agent, streamlining
decisions by simulating future environments. This demonstrates the flexibility and practical potential of
fine-tuned language models in both simulation and real-world scenarios, marking a significant advancement
over traditional applications.
6 Challenges and Future Directions
While foundation models have enabled novel solutions to VLN, several limitations remain under-explored,
and new challenges arise. In this section, we outline the challenges and future direction of VLN from the
perspectivesofbenchmarks,theworldmodel,thehumanmodel,theagentmodel,andrealrobotdeployment.
Benchmarks: Limitations of Data and Task. The current VLN datasets have limitations regarding
quality, diversity, bias, and scalability. For example, in the R2R dataset, the instruction-trajectory pairs are
biased to the shortest path, which may not accurately represent real-world navigation scenarios. We discuss
the trends and recommendations on how VLN benchmarks can be improved.
• Unified and Realistic Tasks and Platforms. Establishing robust benchmarks and ensuring reproducibil-
ity are crucial for evaluating VLN in real-world settings. Real-world variability necessitates compre-
hensive benchmarks reflecting navigation challenges. A universal sim-to-real evaluation platform, like
OVMM (Yenamandra et al., 2023), is needed for standardized testing across simulated and real-world
settings. In addition, the tasks and activities should be realistic and designed originated from human
needs. For instance, BEHAVIOR-1K (Li et al., 2024a) presents a benchmark of everyday household
activities in virtual, interactive, and ecological environment to address the demands for diversity and
realism.
• Dynamic Environment. Real-world environments are inherently complex and dynamic, with moving
objects, people, and variations like lighting and weather presenting unexpected situations (Ma et al.,
2022). These factors disrupt the visual perception of navigation systems and make maintaining reliable
performance difficult. Recent efforts like HAZARD (Zhou et al., 2024c), Habitat 3.0 (Puig et al., 2024),
and HA-VLN (Li et al., 2024b) consider dynamic environments and provide a good starting point.
• Indoors to Outdoors. VLN agents navigating in outdoor environments, e.g., autonomous driving and
aerial vehicles, also start to get more attention (Vasudevan et al., 2021; Li et al., 2024c), with various
language-guided datasets (Sriram et al., 2019; Ma et al., 2022) developed. Early studies have attempted
to involve LLMs in these tasks, either with prompt engineering (Shah et al., 2023; Sha et al., 2023; Wen
et al., 2023), or by fine-tuning LLMs to predict the next action or plan future trajectories (Chen et al.,
2024b; Mao et al., 2023). To adapt off-the-shelf VLMs to these outdoor navigation domains, real-world
driving videos (Xu et al., 2024a; Yuan et al., 2024), simulated driving data (Wang et al., 2023d; Shao
et al., 2024) and them both (Sima et al., 2023; Huang et al., 2024b) have been utilized for instruction
tuning so that these foundation models learn to predict future throttle and steering angles. Additional
reasoning and planning modules have also been integrated into foundation model driving agents (Huang
et al., 2024b; Tian et al., 2024). We refer the readers to surveys and position papers for a detailed
review (Li et al., 2023b; Cui et al., 2024; Gao et al., 2024; Yan et al., 2024).
World Model: From 2D to 3D. Building effective world representations is a central research theme in
embodied perception, reasoning, and planning. VLN is fundamentally a 3D task, where the agent perceives
thereal-worldenvironmentin3D.Althoughthecurrentresearchrepresentstheworldwithstrongandgeneric
2D representations, they fall short of spatial language understanding in the 3D world (Zhang et al., 2024d).
12

Published in Transactions on Machine Learning Research (12/2024)
Many explicit 3D representations are developed in prior work, including various semantic SLAMs and vol-
umetric representation (Chaplot et al., 2020; Min et al., 2021; Saha et al., 2022; Blukis et al., 2022; Zhang
etal.,2022b;Liuetal.,2024),depthinformation(Anetal.,2023),Bird’s-Eye-Viewrepresentationslikegrid
map (Wang et al., 2023g; Liu et al., 2023a), and local metrics map (An et al., 2023). These representations
are limited because they reduce the object set to a closed set, making them inadequate for open-vocabulary
settings with natural language. Several studies develop queryable map/scene representations by integrat-
ing multi-view image features captured from CLIP into 3D voxel grids (Jatavallabhula et al., 2023; Chang
et al., 2023) or top-down feature maps (Huang et al., 2023a; Chen et al., 2023a), as well as utilizing scene
graphs (Rana et al., 2023; Gu et al., 2024) to represent spatial relationships. However, adapting 3D repre-
sentations learned from large-scale data for VLN agents to better perceive the 3D environment is still under
exploration. The recent rise of 3D foundation models (Hong et al., 2023b; Huang et al., 2024a; Chen et al.,
2024d;e), including 3D reconstruction models (Hong et al., 2024) and 3D multimodal representations (Yang
et al., 2024; Zhang et al., 2024c;e), can be crucial for VLN.
HumanModel: FromInstructiontoDialogue. Previouseffortspredominantlyadopteitheraspeaker-
listener paradigm or restricted QA dialogue (Thomason et al., 2020; Gao et al., 2022) that only allows the
agent to ask for help. Recently, there has been a surge in new benchmarks featuring open-ended dialogue
instructions(DeVriesetal.,2018;Banerjeeetal.,2021;Padmakumaretal.,2022;Maetal.,2022;Fanetal.,
2023a), supporting fully free-form communication where agents can ask, propose, explain, suggest, clarify,
andnegotiateeveninambiguousorconfusingscenarios. Still,currentapproachesrelyonrule-baseddialogue
templates to tackle these complexities (Zhang et al., 2023; Parekh et al., 2023; Gu et al., 2023), though
they might feature a foundation model component. Huang et al. (2024b) perform conversational tuning
on a video-language model using human-human dialogue data paired with simulated navigation videos,
showcasing enhanced dialogue generation capabilities while navigation. Moving forward, it is imperative for
futureresearchtointegratefoundationmodelsforsituatedtask-orienteddialoguemanagement(Ulmeretal.,
2024), or explore existing foundation models for task-oriented dialogue (He et al., 2022).
Agent Model: Adapting Foundation Models for VLN. While foundation models show strong gen-
eralizability, incorporating them into navigation tasks remains challenging. LLMs fundamentally lack the
capability to visually perceive the actual environment and are prone to hallucinations. We als discuss capa-
bilities of LLMs in planning and reasoning.
• Lack of Embodied Experience. This limitation can lead to scenarios where LLMs rely solely on pre-
established commonsense for task planning and reasoning, which might not meet specific real-world
needs (Xiang et al., 2024). Some pipelines tackle this issue by captioning the visual observations to
textual descriptions as prompts for LLMs (Zheng et al., 2022), with a potential loss of essential visual
semantics. ComparedwithLLMs,VLMagentsdemonstratethepotentialtoperceivethevisualworldand
plan(Zhangetal.,2024a). Still,thesemodelsareprimarilydevelopedfrominternetdata,whichlackem-
bodied experiences (Mu et al., 2024) and need finetuning for robust agentic decision-making (Zhai et al.,
2024). Further research is needed to transfer the commonsense knowledge in foundation model agents
to generalize to embodied situations. Recently proposed embodied foundation models (such as Embod-
ieGPT(Muetal.,2024), PaLM-E(Driessetal.,2023)andOctopus(Yangetal.,2025))offerapromising
solution for enabling agents to operate more effectively in interactive environments. They fine-tune foun-
dation models across multiple embodied tasks to bridge the gap between an agent’s understanding of
vision, language, and embodied actions, enhancing the foundation model’s ability to comprehend and
execute based on multimodal input.
• Hallucination Issue. LLMsandVLMsmightgeneratenon-existentobjects,leadingtomisinformation(Li
et al., 2023c; Chen et al., 2024c). For example, when LLM performs task planning, it may generate
instructions such as “go forward and turn left at the sofa” even if there is no sofa in the room. This
inaccuracy may cause them to execute incorrect or impossible actions.
• LLMs in Planning and Reasoning. There are some literatures evaluating the zero-shot reasoning and
planning capabilities of LLMs, particularly in relation to PlanBench (Valmeekam et al., 2022) and Co-
gEval (Momennejad et al., 2023), which highlight LLMs’ limitations in more complex planning tasks.
These works assess LLMs in a variety of challenging settings, such as plan generation, optimality, robust-
13

Published in Transactions on Machine Learning Research (12/2024)
ness, and reasoning, and identify that LLMs sometimes struggle with hallucinations or fail to grasp the
relationalstructuresunderlyingcomplexplanningproblems. InthecontextofVLN,theactionspaceand
theplanningrequirementsarerelativelyconstrainedduetothefixedindoorenvironmentsandthelimited
setofnavigationalactions. ThisboundedsettingmakesitmorefeasibleforLLMstoprovidestep-by-step
instructions for coarse-grained directions, which has been demonstrated to be effective in previous works.
In VLN tasks, the LLM’s role is not to take over the entire planning process, but rather to assist by
offering a structured breakdown of instructions. The agent’s actual decision-making remains primarily
reliantonothercomponents, suchasperceptionandmotioncontrol. Therefore, inVLNtasks, theLLM’s
planning serves more as a supplementary guide rather than the sole decision-making factor.
Deployment: From Simulation to Real Robots. Simulated settings often lack the complexity and
variability of real-world environments, and lower-quality rendered images exacerbate this issue. First, the
perceptiongapresultsindecreasedperformanceandaccuracy,highlightingtheneedformorerobustpercep-
tion systems. Wang et al. (2024b) have started to explore the use of semantic maps and 3D feature fields to
provide monocular robots with panoramic perception shows improved performance. The embodiment gap
and the data scarcity are also bottlenecks. The rise of robot teleportation (He et al., 2024b) also provides
an alternative to scale up VLN data for foundation models in real human-robot communications.
7 Broader Impact
Foundation models hold great promise for advancing vision-language navigation. However, it is essential
to address their broader ethical, legal, and societal implications. Given that they are pre-trained on vast,
web-scale datasets, these models can carry inherent biases, which may result in fairness concerns, e.g., to
multilingual users. Some approaches involve continual model training, it is critical to acknowledge and
mitigate any potential risks to user privacy, especially when deployed in real-world applications such as
home robotics.
8 Acknowledgement
This work is supported in part by the ARO Award W911NF2110220, NSF grant IIS-1949634, and ONR
grant N00014-23-1-2417 & N00014-23-1-2356. Any opinions, findings, and conclusions or recommendations
expressed in this material are those of the authors and do not necessarily reflect the views of the funding
agencies.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo
Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv
preprint arXiv:2303.08774, 2023.
Michael Ahn, Anthony Brohan, Noah Brown, Yevgen Chebotar, Omar Cortes, Byron David, Chelsea Finn,
Chuyuan Fu, Keerthana Gopalakrishnan, Karol Hausman, et al. Do as i can, not as i say: Grounding
language in robotic affordances. arXiv preprint arXiv:2204.01691, 2022.
Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc,
Arthur Mensch, Katherine Millican, Malcolm Reynolds, et al. Flamingo: a visual language model for
few-shotlearning. InConference on Neural Information Processing Systems, volume35, pp.23716–23736,
2022.
DongAn,YuankaiQi,YanHuang,QiWu,LiangWang,andTieniuTan. Neighbor-viewenhancedmodelfor
visionandlanguagenavigation. InProceedings of the 29th ACM International Conference on Multimedia,
pp. 5101–5109, 2021.
Dong An, Zun Wang, Yangguang Li, Yi Wang, Yicong Hong, Yan Huang, Liang Wang, and Jing Shao. 1st
place solutions for rxr-habitat vision-and-language navigation competition (cvpr 2022). 2022.
14

Published in Transactions on Machine Learning Research (12/2024)
Dong An, Yuankai Qi, Yangguang Li, Yan Huang, Liang Wang, Tieniu Tan, and Jing Shao. Bevbert: Mul-
timodal map pre-training for language-guided navigation. In Proceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 2737–2748, 2023.
Dong An, Hanqing Wang, Wenguan Wang, Zun Wang, Yan Huang, Keji He, and Liang Wang. Etpnav:
Evolving topological planning for vision-language navigation in continuous environments. IEEE Transac-
tions on Pattern Analysis and Machine Intelligence, 2024.
Anne H Anderson, Miles Bader, Ellen Gurman Bard, Elizabeth Boyle, Gwyneth Doherty, Simon Garrod,
StephenIsard,JacquelineKowtko,JanMcAllister,JimMiller, etal. Thehcrcmaptaskcorpus. Language
and speech, 34(4):351–366, 1991.
Peter Anderson, Qi Wu, Damien Teney, Jake Bruce, Mark Johnson, Niko Sünderhauf, Ian Reid, Stephen
Gould, and Anton Van Den Hengel. Vision-and-language navigation: Interpreting visually-grounded nav-
igation instructions in real environments. In Proceedings of the IEEE conference on computer vision and
pattern recognition, pp. 3674–3683, 2018.
PeterAnderson,AyushShrivastava,DeviParikh,DhruvBatra,andStefanLee. Chasingghosts: Instruction
followingasbayesianstatetracking. InConference on Neural Information Processing Systems,volume32,
2019.
Peter Anderson, Ayush Shrivastava, Joanne Truong, Arjun Majumdar, Devi Parikh, Dhruv Batra, and
StefanLee. Sim-to-realtransferforvision-and-languagenavigation. InConference on Robot Learning, pp.
671–681. PMLR, 2021.
Jacob Andreas. Language models as agent models. In Findings of the Association for Computational
Linguistics: EMNLP 2022, pp. 5769–5779, 2022.
Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret Mitchell, Dhruv Batra, C. Lawrence Zitnick, and
DeviParikh. VQA:VisualQuestionAnswering. InInternationalConferenceonComputerVision(ICCV),
2015.
Shurjo Banerjee, Jesse Thomason, and Jason Corso. The robotslang benchmark: Dialog-guided robot local-
ization and navigation. In Conference on Robot Learning, pp. 1384–1393. PMLR, 2021.
Jacob LS Bellmund, Peter Gärdenfors, Edvard I Moser, and Christian F Doeller. Navigating cognition:
Spatial codes for human thinking. Science, 362(6415):eaat6766, 2018.
Valts Blukis, Chris Paxton, Dieter Fox, Animesh Garg, and Yoav Artzi. A persistent spatial semantic
representationforhigh-levelnaturallanguageinstructionexecution. InConference on Robot Learning,pp.
706–717. PMLR, 2022.
Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S
Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. On the opportunities and risks of
foundation models. arXiv preprint arXiv:2108.07258, 2021.
Rebecca J Brand, Kelly Escobar, Adrien Baranes, and Amanda Albu. Crawling predicts infants’ under-
standing of agents’ navigation of obstacles. Infancy, 20(4):405–415, 2015.
TomBrown,BenjaminMann,NickRyder,MelanieSubbiah,JaredDKaplan,PrafullaDhariwal,ArvindNee-
lakantan, Pranav Shyam, Girish Sastry, Amanda Askell, Sandhini Agarwal, Ariel Herbert-Voss, Gretchen
Krueger, Tom Henighan, Rewon Child, Aditya Ramesh, Daniel Ziegler, Jeffrey Wu, Clemens Winter,
Chris Hesse, Mark Chen, Eric Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess, Jack Clark, Christo-
pher Berner, Sam McCandlish, Alec Radford, Ilya Sutskever, and Dario Amodei. Language models are
few-shot learners. In H. Larochelle, M. Ranzato, R. Hadsell, M.F. Balcan, and H. Lin (eds.), Advances in
Neural Information Processing Systems, volume 33, pp. 1877–1901, 2020.
Angel Chang, Angela Dai, Thomas Funkhouser, Maciej Halber, Matthias Niebner, Manolis Savva, Shuran
Song, AndyZeng, andYindaZhang. Matterport3d: Learningfromrgb-ddatainindoorenvironments. In
7th IEEE International Conference on 3D Vision, 3DV 2017, pp. 667–676, 2018.
15

Published in Transactions on Machine Learning Research (12/2024)
HaonanChang,KowndinyaBoyalakuntla,ShiyangLu,SiweiCai,EricPuJing,ShreeshKeskar,ShijieGeng,
Adeeb Abbas, Lifeng Zhou, Kostas Bekris, et al. Context-aware entity grounding with open-vocabulary
3d scene graphs. In Proceedings of the 2023 Conference on Robot Learning (CORL). JMLR, 2023.
Matthew Chang, Theophile Gervet, Mukul Khanna, Sriram Yenamandra, Dhruv Shah, So Yeon Min, Kavit
Shah, Chris Paxton, Saurabh Gupta, Dhruv Batra, et al. Goat: Go to any thing. In Robotics: Science
and Systems 2024, 2024.
DevendraSinghChaplot,DhirajPrakashchandGandhi,AbhinavGupta,andRussRSalakhutdinov. Object
goalnavigationusinggoal-orientedsemanticexploration. InConference on Neural Information Processing
Systems, volume 33, pp. 4247–4258, 2020.
Boyuan Chen, Fei Xia, Brian Ichter, Kanishka Rao, Keerthana Gopalakrishnan, Michael S Ryoo, Austin
Stone, and Daniel Kappler. Open-vocabulary queryable scene representations for real world planning.
In 2023 IEEE International Conference on Robotics and Automation (ICRA), pp. 11509–11522. IEEE,
2023a.
Howard Chen, Alane Suhr, Dipendra Misra, Noah Snavely, and Yoav Artzi. Touchdown: Natural lan-
guage navigation and spatial reasoning in visual street environments. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pp. 12538–12547, 2019.
Jiaqi Chen, Bingqian Lin, Ran Xu, Zhenhua Chai, Xiaodan Liang, and Kwan-Yee K Wong. Mapgpt: Map-
guided prompting for unified vision-and-language navigation. arXiv preprint arXiv:2401.07314, 2024a.
Kevin Chen, Junshen K Chen, Jo Chuang, Marynel Vázquez, and Silvio Savarese. Topological planning
with transformers for vision-and-language navigation. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, pp. 11276–11286, 2021a.
LongChen, OlegSinavski, JanHünermann, AliceKarnsund, AndrewJamesWillmott, DannyBirch, Daniel
Maund, and Jamie Shotton. Driving with llms: Fusing object-level vector modality for explainable au-
tonomous driving. In 2024 IEEE International Conference on Robotics and Automation (ICRA), pp.
14093–14100. IEEE, 2024b.
Peihao Chen, Dongyu Ji, Kunyang Lin, Runhao Zeng, Thomas H. Li, Mingkui Tan, and Chuang Gan.
Weakly-supervised multi-granularity map learning for vision-and-language navigation. In Advances in
Neural Information Processing Systems, 2022a.
Peihao Chen, Xinyu Sun, Hongyan Zhi, Runhao Zeng, Thomas H Li, Gaowen Liu, Mingkui Tan, and
Chuang Gan. A2 nav: Action-aware zero-shot robot navigation by exploiting vision-and-language ability
of foundation models. 2023b.
ShizheChen,Pierre-LouisGuhur,CordeliaSchmid,andIvanLaptev. Historyawaremultimodaltransformer
forvision-and-languagenavigation. InAdvancesinNeuralInformationProcessingSystems,pp.5834–5847,
2021b.
Shizhe Chen, Pierre-Louis Guhur, Makarand Tapaswi, Cordelia Schmid, and Ivan Laptev. Learning from
unlabeled 3d environments for vision-and-language navigation. In European Conference on Computer
Vision, pp. 638–655. Springer, 2022b.
ShizheChen, Pierre-LouisGuhur, MakarandTapaswi, CordeliaSchmid, andIvanLaptev. Think global, act
local: Dual-scale graph transformer for vision-and-language navigation. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pp. 16537–16547, 2022c.
Xiaoyu Chen, Shenao Zhang, Pushi Zhang, Li Zhao, and Jianyu Chen. Asking before acting: Gather
information in embodied decision making with language models. arXiv preprint arXiv:2305.15695, 2023c.
Xuweiyi Chen, Ziqiao Ma, Xuejun Zhang, Sihan Xu, Shengyi Qian, Jianing Yang, David Fouhey, and Joyce
Chai. Multi-object hallucination in vision language models. In The Thirty-eighth Annual Conference on
Neural Information Processing Systems, 2024c.
16

Published in Transactions on Machine Learning Research (12/2024)
Zhimin Chen, Longlong Jing, Yingwei Li, and Bing Li. Bridging the domain gap: Self-supervised 3d scene
understanding with foundation models. Advances in Neural Information Processing Systems, 36, 2024d.
Zhimin Chen, Liang Yang, Yingwei Li, Longlong Jing, and Bing Li. Sam-guided masked token prediction
for 3d scene understanding. arXiv preprint arXiv:2410.12158, 2024e.
Zixu Cheng, Yujiang Pu, Shaogang Gong, Parisa Kordjamshidi, and Yu Kong. Shine: Saliency-aware hier-
archical negative ranking for compositional temporal grounding. arXiv preprint arXiv:2407.05118, 2024.
Ta-Chung Chi, Minmin Shen, Mihail Eric, Seokhwan Kim, and Dilek Hakkani-Tur. Just ask: An interactive
learningframeworkforvisionandlanguagenavigation. InProceedingsoftheAAAIconferenceonartificial
intelligence, volume 34, pp. 2459–2466, 2020.
Xiangxiang Chu, Limeng Qiao, Xinyang Lin, Shuang Xu, Yang Yang, Yiming Hu, Fei Wei, Xinyu Zhang,
Bo Zhang, Xiaolin Wei, et al. Mobilevlm: A fast, reproducible and strong vision language assistant for
mobile devices. arXiv preprint arXiv:2312.16886, 2023.
Hyung Won Chung, Le Hou, Shayne Longpre, Barret Zoph, Yi Tay, William Fedus, Yunxuan Li, Xuezhi
Wang, Mostafa Dehghani, Siddhartha Brahma, et al. Scaling instruction-finetuned language models.
Journal of Machine Learning Research, 25(70):1–53, 2024.
Jonathan Crespo, Jose Carlos Castillo, Oscar Martinez Mozos, and Ramon Barber. Semantic information
for robot navigation: A survey. Applied Sciences, 10(2):497, 2020.
CanCui,YunshengMa,XuCao,WenqianYe,YangZhou,KaizhaoLiang,JintaiChen,JuanwuLu,Zichong
Yang, Kuei-Da Liao, et al. A survey on multimodal large language models for autonomous driving. In
Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision,pp.958–979,2024.
Yibo Cui, Liang Xie, Yakun Zhang, Meishan Zhang, Ye Yan, and Erwei Yin. Grounded entity-landmark
adaptive pre-training for vision-and-language navigation. In Proceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 12043–12053, 2023.
Wenliang Dai, Junnan Li, DONGXU LI, Anthony Meng Huat Tiong, Junqi Zhao, Weisheng Wang, Boyang
Li, Pascale N Fung, and Steven Hoi. Instructblip: Towards general-purpose vision-language models with
instruction tuning. In Conference on Neural Information Processing Systems, volume 36, 2024.
Harm De Vries, Kurt Shuster, Dhruv Batra, Devi Parikh, Jason Weston, and Douwe Kiela. Talk the
walk: Navigating new york city through grounded dialogue. In Visual Learning and Embodied Agents in
Simulation Environments (VLEASE) Workshop at ECCV, 2018.
Zhiwei Deng, Karthik Narasimhan, and Olga Russakovsky. Evolving graphical planner: Contextual global
planning for vision-and-language navigation. In Conference on Neural Information Processing Systems,
volume 33, pp. 20660–20672, 2020.
Vishnu Sashank Dorbala, Gunnar Sigurdsson, Robinson Piramuthu, Jesse Thomason, and Gaurav S
Sukhatme. Clip-nav: Using clip for zero-shot vision-and-language navigation. In Workshop on Language
and Robotics at CoRL 2022, 2022.
Zi-Yi Dou and Nanyun Peng. Foam: A follower-aware speaker model for vision-and-language navigation. In
Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies, pp. 4332–4340, 2022.
Zi-Yi Dou, Feng Gao, and Nanyun Peng. Masked path modeling for vision-and-language navigation. In
Findings of the Association for Computational Linguistics: EMNLP, pp. 15255–15269, 2023.
DannyDriess,FeiXia,MehdiSMSajjadi,CoreyLynch,AakankshaChowdhery,BrianIchter,AyzaanWahid,
JonathanTompson, QuanVuong, TianheYu, etal. Palm-e: anembodiedmultimodallanguagemodel. In
Proceedings of the 40th International Conference on Machine Learning, pp. 8469–8488, 2023.
17

Published in Transactions on Machine Learning Research (12/2024)
YifanDu,ZikangLiu,JunyiLi,andWayneXinZhao. Asurveyofvision-languagepre-trainedmodels. arXiv
preprint arXiv:2202.10936, 2022.
Jiafei Duan, Samson Yu, Hui Li Tan, Hongyuan Zhu, and Cheston Tan. A survey of embodied ai: From
simulators to research tasks. IEEE Transactions on Emerging Topics in Computational Intelligence, 6(2):
230–244, 2022.
Russell A Epstein, Eva Zita Patai, Joshua B Julian, and Hugo J Spiers. The cognitive map in humans:
spatial navigation and beyond. Nature neuroscience, 20(11):1504–1513, 2017.
Jonathan D Ericson and William H Warren. Probing the invariant structure of spatial knowledge: Support
for the cognitive graph hypothesis. Cognition, 200:104276, 2020.
Yue Fan, Winson Chen, Tongzhou Jiang, Chun Zhou, Yi Zhang, and Xin Wang. Aerial vision-and-dialog
navigation. In Findings of the Association for Computational Linguistics: ACL 2023, pp. 3043–3061,
2023a.
YueFan,JingGu,KaizhiZheng,andXinWang. R2h: Buildingmultimodalnavigationhelpersthatrespond
to help requests. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language
Processing, pp. 14803–14819, 2023b.
Daniel Fried, Ronghang Hu, Volkan Cirik, Anna Rohrbach, Jacob Andreas, Louis-Philippe Morency, Taylor
Berg-Kirkpatrick, Kate Saenko, Dan Klein, and Trevor Darrell. Speaker-follower models for vision-and-
language navigation. In Conference on Neural Information Processing Systems, volume 31, 2018.
Charles R Gallistel. The organization of learning. The MIT Press, 1990.
Chen Gao, Xingyu Peng, Mi Yan, He Wang, Lirong Yang, Haibing Ren, Hongsheng Li, and Si Liu. Adap-
tive zone-aware hierarchical planner for vision-language navigation. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pp. 14911–14920, 2023.
Haoxiang Gao, Yaqian Li, Kaiwen Long, Ming Yang, and Yiqing Shen. A survey for foundation models in
autonomous driving. arXiv preprint arXiv:2402.01105, 2024.
Xiaofeng Gao, Qiaozi Gao, Ran Gong, Kaixiang Lin, Govind Thattai, and Gaurav S Sukhatme. Dialfred:
Dialogue-enabledagentsforembodiedinstructionfollowing. IEEE Robotics and Automation Letters (RA-
L), 2022.
Georgios Georgakis, Karl Schmeckpeper, Karan Wanchoo, Soham Dan, Eleni Miltsakaki, Dan Roth, and
Kostas Daniilidis. Cross-modal map learning for vision and language navigation. In Proceedings of the
IEEE/CVF conference on Computer Vision and Pattern Recognition, pp. 15439–15449, 2022.
Muraleekrishna Gopinathan, Jumana Abu-Khalaf, David Suter, Sidike Paheding, and Nathir A Rawashdeh.
What is near?: Room locality learning for enhanced robot vision-language-navigation in indoor living
environments. arXiv preprint arXiv:2309.05036, 2023.
MuraleekrishnaGopinathan, MartinMasek, JumanaAbu-Khalaf, andDavidSuter. Spatially-awarespeaker
for vision-and-language navigation instruction generation. In Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics (Volume 1: Long Papers), pp. 13601–13614, 2024.
JingGu,ElianaStefani,QiWu,JesseThomason,andXinWang. Vision-and-languagenavigation: Asurvey
of tasks, methods, and future directions. In Proceedings of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), pp. 7606–7623, 2022.
Jing Gu, Kaizhi Zheng, Kaiwen Zhou Yue Fan, Xuehai He Jialu Wang Zonglin Di, and Xin Eric Wang.
Slugjarvis: Multimodal commonsense knowledge-based embodied ai for simbot challenge. In Alexa Prize
SimBot Challenge Proceedings, 2023.
18

Published in Transactions on Machine Learning Research (12/2024)
Qiao Gu, Ali Kuwajerwala, Sacha Morin, Krishna Murthy Jatavallabhula, Bipasha Sen, Aditya Agarwal,
Corban Rivera, William Paul, Kirsty Ellis, Rama Chellappa, et al. Conceptgraphs: Open-vocabulary
3d scene graphs for perception and planning. In 2024 IEEE International Conference on Robotics and
Automation (ICRA), pp. 5021–5028. IEEE, 2024.
Pierre-Louis Guhur, Makarand Tapaswi, Shizhe Chen, Ivan Laptev, and Cordelia Schmid. Airbert: In-
domain pretraining for vision-and-language navigation. In Proceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 1634–1643, 2021a.
Pierre-Louis Guhur, Makarand Tapaswi, Shizhe Chen, Ivan Laptev, and Cordelia Schmid. Airbert: In-
domain pretraining for vision-and-language navigation. In Proceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 1634–1643, 2021b.
Faiza Gul, Wan Rahiman, and Syed Sahal Nazli Alhady. A comprehensive study for robot navigation
techniques. Cogent Engineering, 6(1):1632046, 2019.
David Ha and Jürgen Schmidhuber. Recurrent world models facilitate policy evolution. In Advances in
Neural Information Processing Systems 31, pp. 2451–2463. 2018.
Weituo Hao, Chunyuan Li, Xiujun Li, Lawrence Carin, and Jianfeng Gao. Towards learning a generic
agentforvision-and-languagenavigationviapre-training. InProceedings of the IEEE/CVF conference on
Computer Vision and Pattern Recognition, pp. 13134–13143, 2020.
Keji He, Yan Huang, Qi Wu, Jianhua Yang, Dong An, Shuanglin Sima, and Liang Wang. Landmark-rxr:
Solving vision-and-language navigation with fine-grained alignment supervision. In Conference on Neural
Information Processing Systems, volume 34, pp. 652–663, 2021.
Keji He, Chenyang Si, Zhihe Lu, Yan Huang, Liang Wang, and Xinchao Wang. Frequency-enhanced data
augmentation for vision-and-language navigation. In Conference on Neural Information Processing Sys-
tems, volume 36, 2024a.
Tairan He, Zhengyi Luo, Wenli Xiao, Chong Zhang, Kris Kitani, Changliu Liu, and Guanya Shi. Learning
human-to-humanoid real-time whole-body teleoperation. In 2024 IEEE/RSJ International Conference on
Intelligent Robots and Systems (IROS), 2024b.
Wanwei He, Yinpei Dai, Yinhe Zheng, Yuchuan Wu, Zheng Cao, Dermot Liu, Peng Jiang, Min Yang, Fei
Huang,LuoSi,etal. Galaxy: Agenerativepre-trainedmodelfortask-orienteddialogwithsemi-supervised
learning and explicit policy injection. In Proceedings of the AAAI conference on artificial intelligence,
volume 36, pp. 10749–10757, 2022.
Karl Moritz Hermann, Mateusz Malinowski, Piotr Mirowski, Andras Banki-Horvath, Keith Anderson, and
Raia Hadsell. Learning to follow directions in street view. In Proceedings of the AAAI Conference on
Artificial Intelligence, pp. 11773–11781, 2020.
YicongHong, CristianRodriguez, YuankaiQi, QiWu, andStephenGould. Languageandvisualentityrela-
tionshipgraphforagentnavigation. InConference on Neural Information Processing Systems,volume33,
pp. 7685–7696, 2020a.
Yicong Hong, Cristian Rodriguez, Qi Wu, and Stephen Gould. Sub-instruction aware vision-and-language
navigation. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing
(EMNLP), pp. 3360–3376, 2020b.
Yicong Hong, Qi Wu, Yuankai Qi, Cristian Rodriguez Opazo, and Stephen Gould. A recurrent vision-and-
language BERT for navigation. In Proceedings of the IEEE/CVF conference on Computer Vision and
Pattern Recognition, 2021.
Yicong Hong, Zun Wang, Qi Wu, and Stephen Gould. Bridging the gap between learning in discrete and
continuousenvironmentsforvision-and-languagenavigation. InProceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pp. 15439–15449, 2022.
19

Published in Transactions on Machine Learning Research (12/2024)
Yicong Hong, Yang Zhou, Ruiyi Zhang, Franck Dernoncourt, Trung Bui, Stephen Gould, and Hao Tan.
Learning navigational visual representations with semantic map supervision. In Proceedings of the
IEEE/CVF International Conference on Computer Vision, pp. 3055–3067, 2023a.
Yicong Hong, Kai Zhang, Jiuxiang Gu, Sai Bi, Yang Zhou, Difan Liu, Feng Liu, Kalyan Sunkavalli, Trung
Bui, andHaoTan. LRM:Largereconstructionmodelforsingleimageto3d. InThe Twelfth International
Conference on Learning Representations, 2024.
Yining Hong, Haoyu Zhen, Peihao Chen, Shuhong Zheng, Yilun Du, Zhenfang Chen, and Chuang Gan.
3d-llm: Injecting the 3d world into large language models. NeurIPS, 2023b.
Yihan Hu, Jiazhi Yang, Li Chen, Keyu Li, Chonghao Sima, Xizhou Zhu, Siqi Chai, Senyao Du, Tianwei
Lin, Wenhai Wang, Lewei Lu, Xiaosong Jia, Qiang Liu, Jifeng Dai, Yu Qiao, and Hongyang Li. Planning-
oriented autonomous driving. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, 2023.
Zhiting Hu and Tianmin Shu. Language models, agent models, and world models: The law for machine
reasoning and planning. NeurIPS 2023 Tutorial, 2023.
ChenguangHuang,OierMees,AndyZeng,andWolframBurgard.Visuallanguagemapsforrobotnavigation.
In IEEE International Conference on Robotics and Automation, pp. 10608–10615. IEEE, 2023a.
Jiangyong Huang, Silong Yong, Xiaojian Ma, Xiongkun Linghu, Puhao Li, Yan Wang, Qing Li, Song-Chun
Zhu, Baoxiong Jia, and Siyuan Huang. An embodied generalist agent in 3d world. In Proceedings of the
International Conference on Machine Learning (ICML), 2024a.
WenlongHuang,PieterAbbeel,DeepakPathak,andIgorMordatch. Languagemodelsaszero-shotplanners:
Extracting actionable knowledge for embodied agents. In International Conference on Machine Learning,
pp. 9118–9147. PMLR, 2022.
Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan Tomp-
son, Igor Mordatch, Yevgen Chebotar, et al. Inner monologue: Embodied reasoning through planning
with language models. In Conference on Robot Learning, pp. 1769–1782, 2023b.
Yidong Huang, Jacob Sansom, Ziqiao Ma, Felix Gervits, and Joyce Chai. Drivlme: Enhancing llm-based
autonomous driving agents with embodied and social experiences. In 2024 IEEE/RSJ International Con-
ference on Intelligent Robots and Systems (IROS), 2024b.
Gabriel Ilharco, Vihan Jain, Alexander Ku, Eugene Ie, and Jason Baldridge. General evaluation for instruc-
tion conditioned navigation using dynamic time warping. In Advances in neural information processing
systems, 2019.
MuhammadZubairIrshad,Chih-YaoMa,andZsoltKira. Hierarchicalcross-modalagentforroboticsvision-
and-language navigation. In 2021 IEEE International Conference on Robotics and Automation (ICRA),
pp. 13238–13246. IEEE, 2021.
MuhammadZubairIrshad, NiluthpolChowdhuryMithun, ZacharySeymour, Han-PangChiu, SupunSama-
rasekera,andRakeshKumar. Semantically-awarespatio-temporalreasoningagentforvision-and-language
navigation in continuous environments. In International Conference on Pattern Recognition, pp. 4065–
4071. IEEE, 2022.
Vihan Jain, Gabriel Magalhaes, Alexander Ku, Ashish Vaswani, Eugene Ie, and Jason Baldridge. Stay on
thepath: Instructionfidelityinvision-and-languagenavigation. InProceedingsofthe57thAnnualMeeting
of the Association for Computational Linguistics, pp. 1862–1872, 2019.
Krishna Murthy Jatavallabhula, Alihusein Kuwajerwala, Qiao Gu, Mohd Omama, Tao Chen, Alaa Maalouf,
Shuang Li, Ganesh Iyer, Soroush Saryazdi, Nikhil Keetha, et al. Conceptfusion: Open-set multimodal 3d
mapping. In ICRA2023 Workshop on Pretraining for Robotics (PT4R), 2023.
20

Published in Transactions on Machine Learning Research (12/2024)
Danial Kamali and Parisa Kordjamshidi. Syntax-guided transformers: Elevating compositional general-
ization and grounding in multimodal environments. In Proceedings of the 1st GenBench Workshop on
(Benchmarking) Generalisation in NLP, pp. 130–142, 2023.
Aishwarya Kamath, Peter Anderson, Su Wang, Jing Yu Koh, Alexander Ku, Austin Waters, Yinfei Yang,
Jason Baldridge, and Zarana Parekh. A new path: Scaling vision-and-language navigation with synthetic
instructions and imitation learning. In Proceedings of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition, pp. 10813–10823, 2023.
JacobDevlinMing-WeiChangKentonandLeeKristinaToutanova. Bert: Pre-trainingofdeepbidirectional
transformers for language understanding. pp. 4171–4186, 2019.
Hyounghun Kim, Jialu Li, and Mohit Bansal. Ndh-full: Learning and evaluating navigational agents on
full-length dialogue. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language
Processing, 2021.
Roberta L Klatzky, James R Marston, Nicholas A Giudice, Reginald G Golledge, and Jack M Loomis.
Cognitiveloadofnavigatingwithoutvisionwhenguidedbyvirtualsoundversusspatiallanguage. Journal
of experimental psychology: Applied, 12(4):223, 2006.
JingYuKoh,HonglakLee,YinfeiYang,JasonBaldridge,andPeterAnderson. Pathdreamer: Aworldmodel
for indoor navigation. In Proceedings of the IEEE/CVF International Conference on Computer Vision,
pp. 14738–14748, 2021.
Jing Yu Koh, Harsh Agrawal, Dhruv Batra, Richard Tucker, Austin Waters, Honglak Lee, Yinfei Yang,
Jason Baldridge, and Peter Anderson. Simple and effective synthesis of indoor 3d scenes. In Proceedings
of the AAAI Conference on Artificial Intelligence, volume 37, pp. 1169–1178, 2023.
Jacob Krantz and Stefan Lee. Sim-2-sim transfer for vision-and-language navigation in continuous environ-
ments. In European Conference on Computer Vision, pp. 588–603. Springer, 2022.
JacobKrantz,ErikWijmans,ArjunMajumdar,DhruvBatra,andStefanLee.Beyondthenav-graph: Vision-
and-language navigation in continuous environments. In European Conference on Computer Vision, pp.
104–120. Springer, 2020.
Jacob Krantz, Aaron Gokaslan, Dhruv Batra, Stefan Lee, and Oleksandr Maksymets. Waypoint models for
instruction-guidednavigationincontinuousenvironments. InProceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 15162–15171, 2021.
Alexander Ku, Peter Anderson, Roma Patel, Eugene Ie, and Jason Baldridge. Room-across-room: Multi-
lingual vision-and-language navigation with dense spatiotemporal grounding. In Proceedings of the 2020
Conference on Empirical Methods in Natural Language Processing (EMNLP), pp. 4392–4412, 2020.
ShuheiKuritaandKyunghyunCho. Generativelanguage-groundedpolicyinvision-and-languagenavigation
with bayes’ rule. In International Conference on Learning Representations, 2020.
ChengshuLi,RuohanZhang,JosiahWong,CemGokmen,SanjanaSrivastava,RobertoMartín-Martín,Chen
Wang, Gabrael Levine, Wensi Ai, Benjamin Martinez, et al. Behavior-1k: A human-centered, embodied
ai benchmark with 1, 000 everyday activities and realistic simulation. CoRR, 2024a.
HengLi, MinghanLi, Zhi-QiCheng, YifeiDong, YuxuanZhou, Jun-YanHe, QiDai, TerukoMitamura, and
Alexander G Hauptmann. Human-aware vision-and-language navigation: Bridging simulation to reality
with dynamic human interactions. In The Thirty-eight Conference on Neural Information Processing
Systems Datasets and Benchmarks Track, 2024b.
Jialu Li and Mohit Bansal. Improving vision-and-language navigation by generating future-view image
semantics. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
pp. 10803–10812, 2023.
21

Published in Transactions on Machine Learning Research (12/2024)
Jialu Li and Mohit Bansal. Panogen: Text-conditioned panoramic environment generation for vision-and-
language navigation. In Conference on Neural Information Processing Systems, volume 36, 2024.
Jialu Li, Hao Tan, and Mohit Bansal. Improving cross-modal alignment in vision language navigation
via syntactic information. In Proceedings of the 2021 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies, pp. 1041–1050, 2021.
Jialu Li, Hao Tan, and Mohit Bansal. Clear: Improving vision-language navigation with cross-lingual,
environment-agnostic representations. In Findings of the Association for Computational Linguistics:
NAACL 2022, pp. 633–649, 2022a.
Jialu Li, Hao Tan, and Mohit Bansal. Envedit: Environment editing for vision-and-language navigation. In
ProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,pp.15407–15417,
2022b.
Jialu Li, Aishwarya Padmakumar, Gaurav Sukhatme, and Mohit Bansal. Vln-video: Utilizing driving
videos for outdoor vision-and-language navigation. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 38, pp. 18517–18526, 2024c.
Liunian Harold Li, Mark Yatskar, Da Yin, Cho-Jui Hsieh, and Kai-Wei Chang. Visualbert: A simple and
performant baseline for vision and language. arXiv preprint arXiv:1908.03557, 2019a.
Xiangyang Li, Zihan Wang, Jiahao Yang, Yaowei Wang, and Shuqiang Jiang. Kerm: Knowledge enhanced
reasoning for vision-and-language navigation. In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pp. 2583–2592, 2023a.
Xin Li, Yeqi Bai, Pinlong Cai, Licheng Wen, Daocheng Fu, Bo Zhang, Xuemeng Yang, Xinyu Cai, Tao
Ma, Jianfei Guo, et al. Towards knowledge-driven autonomous driving. arXiv preprint arXiv:2312.04316,
2023b.
XinghangLi, DiGuo, HuapingLiu, andFuchunSun. Reve-ce: Remoteembodiedvisualreferringexpression
in continuous environment. IEEE Robotics and Automation Letters, 7(2):1494–1501, 2022c.
Xiujun Li, Chunyuan Li, Qiaolin Xia, Yonatan Bisk, Asli Çelikyilmaz, Jianfeng Gao, Noah A. Smith, and
Yejin Choi. Robust navigation with language pretraining and stochastic sampling. In Proceedings of the
2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint
Conference on Natural Language Processing, EMNLP-IJCNLP 2019, Hong Kong, China, November 3-7,
2019, pp. 1494–1499, 2019b.
Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang, Xiaowei Hu, Lei Zhang, Lijuan Wang, Houdong Hu,
LiDong,FuruWei,etal. Oscar: Object-semanticsalignedpre-trainingforvision-languagetasks. InCom-
puter Vision–ECCV 2020: 16th European Conference, Glasgow, UK, August 23–28, 2020, Proceedings,
Part XXX 16, pp. 121–137. Springer, 2020.
Yifan Li, Yifan Du, Kun Zhou, Jinpeng Wang, Wayne Xin Zhao, and Ji-Rong Wen. Evaluating object
hallucinationinlargevision-languagemodels. InProceedingsofthe2023ConferenceonEmpiricalMethods
in Natural Language Processing, 2023c.
Jacky Liang, Wenlong Huang, Fei Xia, Peng Xu, Karol Hausman, Brian Ichter, Pete Florence, and Andy
Zeng. Code as policies: Language model programs for embodied control. In 2023 IEEE International
Conference on Robotics and Automation (ICRA), pp. 9493–9500. IEEE, 2023.
Xiwen Liang, Fengda Zhu, Lingling Li, Hang Xu, and Xiaodan Liang. Visual-language navigation pretrain-
ing via prompt-based environmental self-exploration. In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long Papers), pp. 4837–4851, 2022.
Bingqian Lin, Yi Zhu, Xiaodan Liang, Liang Lin, and Jianzhuang Liu. Actional atomic-concept learning for
demystifyingvision-languagenavigation. InProceedingsoftheAAAIConferenceonArtificialIntelligence,
volume 37, pp. 1568–1576, 2023a.
22

Published in Transactions on Machine Learning Research (12/2024)
Bingqian Lin, Yunshuang Nie, Ziming Wei, Jiaqi Chen, Shikui Ma, Jianhua Han, Hang Xu, Xiaojun Chang,
andXiaodanLiang. Navcot: Boostingllm-basedvision-and-languagenavigationvialearningdisentangled
reasoning. arXiv preprint arXiv:2403.07376, 2024a.
BingqianLin,YunshuangNie,ZimingWei,YiZhu,HangXu,ShikuiMa,JianzhuangLiu,andXiaodanLiang.
Correctable landmark discovery via large models for vision-language navigation. IEEE Transactions on
Pattern Analysis and Machine Intelligence, 2024b.
Chuang Lin, Yi Jiang, Jianfei Cai, Lizhen Qu, Gholamreza Haffari, and Zehuan Yuan. Multimodal trans-
formerwithvariable-lengthmemoryforvision-and-languagenavigation. InEuropean Conference on Com-
puter Vision, volume 13696, pp. 380–397. Springer, 2022a.
Kevin Lin, Linjie Li, Chung-Ching Lin, Faisal Ahmed, Zhe Gan, Zicheng Liu, Yumao Lu, and Lijuan Wang.
Swinbert: End-to-end transformers with sparse attention for video captioning. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 17949–17958, 2022b.
Kunyang Lin, Peihao Chen, Diwei Huang, Thomas H Li, Mingkui Tan, and Chuang Gan. Learning vision-
and-languagenavigationfromyoutubevideos. InProceedings of the IEEE/CVF International Conference
on Computer Vision, pp. 8317–8326, 2023b.
Xiangru Lin, Guanbin Li, and Yizhou Yu. Scene-intuitive agent for remote embodied visual grounding.
In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pp. 7036–7045,
2021.
Jamie Lingwood, Mark Blades, Emily K Farran, Yannick Courbois, and Danielle Matthews. Using virtual
environments to investigate wayfinding in 8-to 12-year-olds and adults. Journal of experimental child
psychology, 166:178–189, 2018.
ChongLiu,FengdaZhu,XiaojunChang,XiaodanLiang,ZongyuanGe,andYi-DongShen. Vision-language
navigationwithrandomenvironmentalmixup. InProceedings of the IEEE/CVF International Conference
on Computer Vision, pp. 1644–1654, 2021.
Rui Liu, Xiaohan Wang, Wenguan Wang, and Yi Yang. Bird’s-eye-view scene graph for vision-language
navigation. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 10968–
10980, 2023a.
Rui Liu, Wenguan Wang, and Yi Yang. Volumetric environment representation for vision-language navi-
gation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp.
16317–16328, 2024.
Shubo Liu, Hongsheng Zhang, Yuankai Qi, Peng Wang, Yanning Zhang, and Qi Wu. Aerialvln: Vision-and-
language navigation for uavs. In Proceedings of the IEEE/CVF International Conference on Computer
Vision, pp. 15384–15394, 2023b.
Yuxing Long, Wenzhe Cai, Hongcheng Wang, Guanqi Zhan, and Hao Dong. Instructnav: Zero-shot system
forgenericinstructionnavigationinunexploredenvironment.In8thAnnualConferenceonRobotLearning,
2024a.
YuxingLong,XiaoqiLi,WenzheCai,andHaoDong. Discussbeforemoving: Visuallanguagenavigationvia
multi-expert discussions. In 2024 IEEE International Conference on Robotics and Automation (ICRA),
pp. 17380–17387. IEEE, 2024b.
Guanxing Lu, Ziwei Wang, Changliu Liu, Jiwen Lu, and Yansong Tang. Thinkbot: Embodied instruction
following with thought chain reasoning. arXiv preprint arXiv:2312.07062, 2023.
Jiasen Lu, Dhruv Batra, Devi Parikh, and Stefan Lee. Vilbert: Pretraining task-agnostic visiolinguistic
representations for vision-and-language tasks. In Conference on Neural Information Processing Systems,
volume 32, 2019.
23

Published in Transactions on Machine Learning Research (12/2024)
Chih-Yao Ma, Jiasen Lu, Zuxuan Wu, Ghassan AlRegib, Zsolt Kira, Richard Socher, and Caiming Xiong.
Self-monitoring navigation agent via auxiliary progress estimation. In The Seventh International Confer-
ence on Learning Representations, 2019.
ZiqiaoMa,BenjaminVanDerPloeg,Cristian-PaulBara,YidongHuang,Eui-InKim,FelixGervits,Matthew
Marge, and Joyce Chai. Dorothie: Spoken dialogue for handling unexpected situations in interactive
autonomous driving agents. In Findings of the Association for Computational Linguistics: EMNLP 2022,
pp. 4800–4822, 2022.
Ziqiao Ma, Jacob Sansom, Run Peng, and Joyce Chai. Towards a holistic landscape of situated theory of
mind in large language models. In Findings of the Association for Computational Linguistics: EMNLP
2023, pp. 1011–1031, 2023.
Matt MacMahon, Brian Stankiewicz, and Benjamin Kuipers. Walk the talk: Connecting language, knowl-
edge, and action in route instructions. Def, 2(6):4, 2006.
Aly Magassouba, Komei Sugiura, and Hisashi Kawai. Crossmap transformer: A crossmodal masked path
transformer using double back-translation for vision-and-language navigation. IEEE Robotics and Au-
tomation Letters, 6:6258–6265, 2021. URL https://api.semanticscholar.org/CorpusID:232075933.
ArjunMajumdar,AyushShrivastava,StefanLee,PeterAnderson,DeviParikh,andDhruvBatra. Improving
vision-and-languagenavigationwithimage-textpairsfromtheweb. InEuropean Conference on Computer
Vision, pp. 259–274, 2020.
Jiageng Mao, Yuxi Qian, Junjie Ye, Hang Zhao, and Yue Wang. Gpt-driver: Learning to drive with gpt. In
NeurIPS 2023 Foundation Models for Decision Making Workshop, 2023.
So Yeon Min, Devendra Singh Chaplot, Pradeep Kumar Ravikumar, Yonatan Bisk, and Ruslan Salakhut-
dinov. Film: Following instructions in language with modular methods. In International Conference on
Learning Representations, 2021.
Piotr Mirowski, Matt Grimes, Mateusz Malinowski, Karl Moritz Hermann, Keith Anderson, Denis
Teplyashin, Karen Simonyan, Andrew Zisserman, Raia Hadsell, et al. Learning to navigate in cities
without a map. In Conference on Neural Information Processing Systems, volume 31, 2018.
Dipendra Misra, Andrew Bennett, Valts Blukis, Eyvind Niklasson, Max Shatkhin, and Yoav Artzi. Map-
ping instructions to actions in 3d environments with visual goal prediction. In Proceedings of the 2018
Conference on Empirical Methods in Natural Language Processing, pp. 2667–2678, 2018.
Ronja Möller, Antonino Furnari, Sebastiano Battiato, Aki Härmä, and Giovanni Maria Farinella. A survey
on human-aware robot navigation. Robotics and Autonomous Systems, 145:103837, 2021.
Ida Momennejad, Hosein Hasanbeig, Felipe Vieira Frujeri, Hiteshi Sharma, Nebojsa Jojic, Hamid Palangi,
Robert Ness, and Jonathan Larson. Evaluating cognitive maps and planning in large language models
with cogeval. In Advances in Neural Information Processing Systems, volume 36, 2023.
Abhinav Moudgil, Arjun Majumdar, Harsh Agrawal, Stefan Lee, and Dhruv Batra. SOAT: A scene- and
object-awaretransformerforvision-and-languagenavigation. InAdvancesinneuralinformationprocessing
systems, pp. 7357–7367, 2021.
Yao Mu, Qinglong Zhang, Mengkang Hu, Wenhai Wang, Mingyu Ding, Jun Jin, Bin Wang, Jifeng Dai,
Yu Qiao, and Ping Luo. Embodiedgpt: Vision-language pre-training via embodied chain of thought. In
Conference on Neural Information Processing Systems, volume 36, 2024.
Khanh Nguyen and Hal Daumé III. Help, anna! visual navigation with natural multimodal assistance via
retrospectivecuriosity-encouragingimitationlearning. InProceedingsofthe2019ConferenceonEmpirical
Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language
Processing (EMNLP-IJCNLP), pp. 684–695, Hong Kong, China, November 2019.
24

Published in Transactions on Machine Learning Research (12/2024)
Khanh Nguyen, Debadeepta Dey, Chris Brockett, and Bill Dolan. Vision-based navigation with language-
based assistance via imitation learning with indirect intervention. In Proceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recognition, pp. 12527–12537, 2019.
Phuong DH Nguyen, Yasmin Kim Georgie, Ezgi Kayhan, Manfred Eppe, Verena Vanessa Hafner, and Ste-
fan Wermter. Sensorimotor representation learning for an “active self” in robots: a model survey. KI-
Künstliche Intelligenz, 35:9–35, 2021.
JohnO’KeefeandJonathanDostrovsky. Thehippocampusasaspatialmap: preliminaryevidencefromunit
activity in the freely-moving rat. Brain research, 1971.
John O’keefe and Lynn Nadel. The hippocampus as a cognitive map. Oxford university press, 1978.
Aishwarya Padmakumar, Jesse Thomason, Ayush Shrivastava, Patrick Lange, Anjali Narayan-Chen, Span-
dana Gella, Robinson Piramuthu, Gokhan Tur, and Dilek Hakkani-Tur. Teach: Task-driven embodied
agents that chat. In AAAI, 2022.
Bowen Pan, Rameswar Panda, SouYoung Jin, Rogerio Feris, Aude Oliva, Phillip Isola, and Yoon Kim.
Langnav: Language as a perceptual representation for navigation. In Findings of the Association for
Computational Linguistics: NAACL 2024, pp. 950–974, 2024.
Amit Parekh, Malvina Nikandrou, Georgios Pantazopoulos, Bhathiya Hemanthage, Arash Eshghi, Ioannis
Konstas, Oliver Lemon, and Alessandro Suglia. Emma: A foundation model for embodied, interactive,
multimodal task completion in 3d environments. In Alexa Prize SimBot Challenge Proceedings, 2023.
Sang-Min Park and Young-Gab Kim. Visual language navigation: A survey and open challenges. Artificial
Intelligence Review, 56(1):365–427, 2023.
Alexander Pashevich, Cordelia Schmid, and Chen Sun. Episodic transformer for vision-and-language navi-
gation. InProceedings of the IEEE/CVF International Conference on Computer Vision,pp.15922–15932.
IEEE, 2021.
Sudipta Paul, Amit Roy-Chowdhury, and Anoop Cherian. Avlen: Audio-visual-language embodied nav-
igation in 3d environments. In Conference on Neural Information Processing Systems, volume 35, pp.
6236–6249, 2022.
Tzuf Paz-Argaman and Reut Tsarfaty. RUN through the streets: A new dataset and baseline models for
realistic urban navigation. In Proceedings of the 2019 Conference on Empirical Methods in Natural Lan-
guage Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-
IJCNLP),pp.6449–6455, HongKong, China, November2019.AssociationforComputationalLinguistics.
doi: 10.18653/v1/D19-1681. URL https://aclanthology.org/D19-1681.
Shannon M Pruden, Susan C Levine, and Janellen Huttenlocher. Children’s spatial thinking: Does talk
about the spatial world matter? Developmental science, 14(6):1417–1430, 2011.
Xavier Puig, Eric Undersander, Andrew Szot, Mikael Dallaire Cote, Tsung-Yen Yang, Ruslan Partsey, Ruta
Desai,AlexanderClegg,MichalHlavac,SoYeonMin,etal. Habitat3.0: Aco-habitatforhumans,avatars,
and robots. In The Twelfth International Conference on Learning Representations, 2024.
Jennie E Pyers, Anna Shusterman, Ann Senghas, Elizabeth S Spelke, and Karen Emmorey. Evidence from
an emerging sign language reveals that language supports spatial cognition. Proceedings of the National
Academy of Sciences, 107(27):12116–12120, 2010.
Yuankai Qi, Zizheng Pan, Shengping Zhang, Anton van den Hengel, and Qi Wu. Object-and-action aware
modelforvisuallanguagenavigation. InEuropeanConferenceonComputerVision,pp.303–317.Springer,
2020a.
Yuankai Qi, Qi Wu, Peter Anderson, Xin Wang, William Yang Wang, Chunhua Shen, and Anton van den
Hengel. Reverie: Remoteembodiedvisualreferringexpressioninrealindoorenvironments. InProceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 9982–9991, 2020b.
25

Published in Transactions on Machine Learning Research (12/2024)
Yuankai Qi, Zizheng Pan, Yicong Hong, Ming-Hsuan Yang, Anton van den Hengel, and Qi Wu. The road
to know-where: An object-and-room informed sequential bert for indoor vision-language navigation. In
Proceedings of the IEEE/CVF International Conference on Computer Vision, pp. 1655–1664, 2021.
YanyuanQiao,YuankaiQi,YicongHong,ZhengYu,PengWang,andQiWu. HOP:history-and-orderaware
pre-trainingforvision-and-languagenavigation. InProceedingsoftheIEEE/CVFconferenceonComputer
Vision and Pattern Recognition, pp. 8524–8537, 2022.
YanyuanQiao,YuankaiQi,YicongHong,ZhengYu,PengWang,andQiWu. Hop+: History-enhancedand
order-aware pre-training for vision-and-language navigation. IEEE Transactions on Pattern Analysis and
Machine Intelligence, 2023a.
YanyuanQiao,YuankaiQi,ZhengYu,JingLiu,andQiWu. Marchinchat: Interactivepromptingforremote
embodied referring expression. In Proceedings of the IEEE/CVF International Conference on Computer
Vision, pp. 15758–15767, 2023b.
Yanyuan Qiao, Qianyi Liu, Jiajun Liu, Jing Liu, and Qi Wu. Llm as copilot for coarse-grained vision-and-
language navigation. In European Conference on Computer Vision, pp. 459–476, 2024.
Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish
Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. Learning
transferable visual models from natural language supervision. pp. 8748–8763, 2021.
Abhinav Rajvanshi, Karan Sikka, Xiao Lin, Bhoram Lee, Han-Pang Chiu, and Alvaro Velasquez. Saynav:
Groundinglargelanguagemodelsfordynamicplanningtonavigationinnewenvironments. InProceedings
of the International Conference on Automated Planning and Scheduling, volume 34, pp. 464–474, 2024.
Aditya Ramesh, Mikhail Pavlov, Gabriel Goh, Scott Gray, Chelsea Voss, Alec Radford, Mark Chen, and
Ilya Sutskever. Zero-shot text-to-image generation. In International conference on machine learning, pp.
8821–8831. Pmlr, 2021.
Krishan Rana, Jesse Haviland, Sourav Garg, Jad Abou-Chakra, Ian Reid, and Niko Suenderhauf. Sayplan:
Grounding large language models using 3d scene graphs for scalable robot task planning. In 7th Annual
Conference on Robot Learning, 2023.
Sonia Raychaudhuri, Saim Wani, Shivansh Patel, Unnat Jain, and Angel X. Chang. Language-aligned
waypoint (LAW) supervision for vision-and-language navigation in continuous environments. In EMNLP,
pp. 4018–4028, 2021.
Allen Z Ren, Anushri Dixit, Alexandra Bodrova, Sumeet Singh, Stephen Tu, Noah Brown, Peng Xu, Leila
Takayama, FeiXia, JakeVarley, etal. Robotsthataskforhelp: Uncertaintyalignmentforlargelanguage
model planners. Proceedings of Machine Learning Research, 229, 2023.
T Rodrigo. Navigational strategies and models. Psicológica, 23(1), 2002.
Junha Roh, Chris Paxton, Andrzej Pronobis, Ali Farhadi, and Dieter Fox. Conditional driving from natural
language instructions. In Proceedings of the Conference on Robot Learning, pp. 540–551, 2020.
HomeroRomanRoman,YonatanBisk,JesseThomason,AsliCelikyilmaz,andJianfengGao. Rmm: Arecur-
sive mental model for dialogue navigation. In Findings of the Association for Computational Linguistics:
EMNLP 2020, pp. 1732–1745, 2020.
Homagni Saha, Fateme Fotouhi, Qisai Liu, and Soumik Sarkar. A modular vision language navigation and
manipulationframeworkforlonghorizoncompositionaltasksinindoorenvironment. FrontiersinRobotics
and AI, 9, 2022.
Gabriel Sarch, Yue Wu, Michael Tarr, and Katerina Fragkiadaki. Open-ended instructable embodied agents
with memory-augmented large language models. In Findings of the Association for Computational Lin-
guistics: EMNLP 2023, pp. 3468–3500, 2023.
26

Published in Transactions on Machine Learning Research (12/2024)
Manolis Savva, Jitendra Malik, Devi Parikh, Dhruv Batra, Abhishek Kadian, Oleksandr Maksymets, Yili
Zhao, Erik Wijmans, Bhavana Jain, Julian Straub, Jia Liu, and Vladlen Koltun. Habitat: A platform for
embodied AI research. pp. 9338–9346, 2019.
HaoSha,YaoMu,YuxuanJiang,LiChen,ChenfengXu,PingLuo,ShengboEbenLi,MasayoshiTomizuka,
Wei Zhan, and Mingyu Ding. Languagempc: Large language models as decision makers for autonomous
driving. arXiv preprint arXiv:2310.03026, 2023.
DhruvShah,BłażejOsiński,SergeyLevine,etal. Lm-nav: Roboticnavigationwithlargepre-trainedmodels
of language, vision, and action. In Conference on robot learning, pp. 492–504. PMLR, 2023.
Hao Shao, Yuxuan Hu, Letian Wang, Guanglu Song, Steven L Waslander, Yu Liu, and Hongsheng Li.
Lmdrive: Closed-loop end-to-end driving with large language models. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition, pp. 15120–15130, 2024.
Sheng Shen, Liunian Harold Li, Hao Tan, Mohit Bansal, Anna Rohrbach, Kai-Wei Chang, Zhewei Yao, and
Kurt Keutzer. How much can clip benefit vision-and-language tasks? In International Conference on
Learning Representations, 2022.
Mohit Shridhar, Jesse Thomason, Daniel Gordon, Yonatan Bisk, Winson Han, Roozbeh Mottaghi, Luke
Zettlemoyer, and Dieter Fox. Alfred: A benchmark for interpreting grounded instructions for everyday
tasks. InProceedings of the IEEE/CVF conference on computer vision and pattern recognition,pp.10740–
10749, 2020.
AnnaShusterman,SangAhLee,andElizabethSSpelke. Cognitiveeffectsoflanguageonhumannavigation.
Cognition, 120(2):186–201, 2011.
Chonghao Sima, Katrin Renz, Kashyap Chitta, Li Chen, Hanxue Zhang, Chengen Xie, Ping Luo, Andreas
Geiger, and Hongyang Li. Drivelm: Driving with graph visual question answering. In First Vision and
Language for Autonomous Driving and Robotics Workshop, 2023.
KunalPratapSingh,LucaWeihs,AlvaroHerrasti,JonghyunChoi,AniruddhaKembhavi,andRoozbehMot-
taghi. Ask4help: Learningtoleverageanexpertforembodiedtasks. InConference on Neural Information
Processing Systems, volume 35, pp. 16221–16232, 2022.
Chan Hee Song, Jiaman Wu, Clayton Washington, Brian M Sadler, Wei-Lun Chao, and Yu Su. Llm-
planner: Few-shot grounded planning for embodied agents with large language models. In Proceedings of
the IEEE/CVF International Conference on Computer Vision, pp. 2998–3009, 2023.
NN Sriram, Tirth Maniar, Jayaganesh Kalyanasundaram, Vineet Gandhi, Brojeshwar Bhowmick, and
K Madhava Krishna. Talk to the vehicle: Language conditioned autonomous navigation of self driv-
ing cars. In 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp.
5284–5290. IEEE, 2019.
Yifei Su, Dong An, Yuan Xu, Kehan Chen, and Yan Huang. Target-grounded graph-aware transformer for
aerial vision-and-dialog navigation. arXiv preprint arXiv:2308.11561, 2023.
AndrewSzot,AlexanderClegg,EricUndersander,ErikWijmans,YiliZhao,JohnM.Turner,NoahMaestre,
MustafaMukadam,DevendraSinghChaplot,OleksandrMaksymets,AaronGokaslan,VladimirVondrus,
SameerDharur,FranziskaMeier,WojciechGaluba,AngelX.Chang,ZsoltKira,VladlenKoltun,Jitendra
Malik,ManolisSavva,andDhruvBatra. Habitat2.0: Traininghomeassistantstorearrangetheirhabitat.
In Advances in Neural Information Processing Systems, pp. 251–266, 2021.
Hao Tan and Mohit Bansal. Lxmert: Learning cross-modality encoder representations from transformers.
In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th
International Joint Conference on Natural Language Processing (EMNLP-IJCNLP),pp.5100–5111,2019.
27

Published in Transactions on Machine Learning Research (12/2024)
Hao Tan, Licheng Yu, and Mohit Bansal. Learning to navigate unseen environments: Back translation with
environmental dropout. In Proceedings of the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short
Papers), pp. 2610–2621, 2019.
Jesse Thomason, Michael Murray, Maya Cakmak, and Luke Zettlemoyer. Vision-and-dialog navigation. In
Conference on Robot Learning, pp. 394–406. PMLR, 2020.
Xiaoyu Tian, Junru Gu, Bailin Li, Yicheng Liu, Chenxu Hu, Yang Wang, Kun Zhan, Peng Jia, Xianpeng
Lang, and Hang Zhao. Drivevlm: The convergence of autonomous driving and large vision-language
models. In Conference on Robot Learning (CoRL), 2024.
Edward C Tolman. Cognitive maps in rats and men. Psychological review, 55(4):189, 1948.
Dennis Ulmer, Elman Mansimov, Kaixiang Lin, Justin Sun, Xibin Gao, and Yi Zhang. Bootstrapping
llm-based task-oriented dialogue agents via self-talk. arXiv preprint arXiv:2401.05033, 2024.
Karthik Valmeekam, Alberto Olmo, Sarath Sreedharan, and Subbarao Kambhampati. Planbench: An
extensible benchmark for evaluating large language models on planning and reasoning about change. In
Advances in Neural Information Processing Systems, 2022.
Arun Balajee Vasudevan, Dengxin Dai, and Luc Van Gool. Talk2nav: Long-range vision-and-language
navigation with dual attention and spatial memory. International Journal of Computer Vision, 129(1):
246–266, 2021.
Hanqing Wang, Wenguan Wang, Wei Liang, Caiming Xiong, and Jianbing Shen. Structured scene memory
for vision-language navigation. In Proceedings of the IEEE/CVF conference on Computer Vision and
Pattern Recognition, pp. 8455–8464, 2021.
HanqingWang, WeiLiang, LucVanGool, andWenguanWang. Dreamwalker: Mentalplanningforcontinu-
ous vision-language navigation. In Proceedings of the IEEE/CVF International Conference on Computer
Vision, pp. 10873–10883, 2023a.
Liuyi Wang, Zongtao He, Jiagui Tang, Ronghao Dang, Naijia Wang, Chengju Liu, and Qijun Chen. A dual
semantic-aware recurrent global-adaptive network for vision-and-language navigation. In Proceedings of
the Thirty-Second International Joint Conference on Artificial Intelligence, pp. 1479–1487, 2023b.
Liuyi Wang, Chengju Liu, Zongtao He, Shu Li, Qingqing Yan, Huiyi Chen, and Qi Chen. Pasts: Progress-
aware spatio-temporal transformer speaker for vision-and-language navigation. Eng. Appl. Artif. Intell.,
128:107487, 2023c. URL https://api.semanticscholar.org/CorpusID:258833536.
Su Wang, Ceslee Montgomery, Jordi Orbay, Vighnesh Birodkar, Aleksandra Faust, Izzeddin Gur, Natasha
Jaques, Austin Waters, Jason Baldridge, and Peter Anderson. Less is more: Generating grounded naviga-
tion instructions from landmarks. In Proceedings of the IEEE/CVF Conference on Computer Vision and
Pattern Recognition, pp. 15428–15438, 2022a.
WenhaiWang,JiangweiXie,ChuanYangHu,HaomingZou,JiananFan,WenwenTong,YangWen,SileiWu,
Hanming Deng, et al. Drivemlm: Aligning multi-modal large language models with behavioral planning
states for autonomous driving. arXiv preprint arXiv:2312.09245, 2023d.
XiaohanWang,WenguanWang,JiayiShao,andYiYang.Lana: Alanguage-capablenavigatorforinstruction
following and generation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 19048–19058, 2023e.
Xiaohan Wang, Wenguan Wang, Jiayi Shao, and Yi Yang. Learning to follow and generate instructions for
language-capable navigation. IEEE Transactions on Pattern Analysis and Machine Intelligence, 2023f.
XinWang,QiuyuanHuang,AsliCelikyilmaz,JianfengGao,DinghanShen,Yuan-FangWang,WilliamYang
Wang, and Lei Zhang. Reinforced cross-modal matching and self-supervised imitation learning for vision-
language navigation. In Proceedings of the IEEE/CVF conference on computer vision and pattern recog-
nition, pp. 6629–6638, 2019.
28

Published in Transactions on Machine Learning Research (12/2024)
YiWang,KunchangLi,YizhuoLi,YinanHe,BingkunHuang,ZhiyuZhao,HongjieZhang,JilanXu,YiLiu,
ZunWang,etal. Internvideo: Generalvideofoundationmodelsviagenerativeanddiscriminativelearning.
arXiv preprint arXiv:2212.03191, 2022b.
Zehao Wang, Mingxiao Li, Minye Wu, Marie-Francine Moens, and Tinne Tuytelaars. Find a way forward:
a language-guided semantic map navigator. arXiv preprint arXiv:2203.03183, 2022c.
Zihan Wang, Xiangyang Li, Jiahao Yang, Yeqi Liu, and Shuqiang Jiang. Gridmm: Grid memory map for
vision-and-language navigation. In Proceedings of the IEEE/CVF International Conference on Computer
Vision, pp. 15625–15636, 2023g.
Zihan Wang, Xiangyang Li, Jiahao Yang, Yeqi Liu, Junjie Hu, Ming Jiang, and Shuqiang Jiang. Lookahead
exploration with neural radiance representation for continuous vision-language navigation. In Proceedings
of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 13753–13762, 2024a.
Zihan Wang, Xiangyang Li, Jiahao Yang, Yeqi Liu, and Shuqiang Jiang. Sim-to-real transfer via 3d feature
fields for vision-and-language navigation. arXiv preprint arXiv:2406.09798, 2024b.
Zun Wang, Jialu Li, Yicong Hong, Yi Wang, Qi Wu, Mohit Bansal, Stephen Gould, Hao Tan, and Yu Qiao.
Scalingdatagenerationinvision-and-languagenavigation. InProceedings of the IEEE/CVF International
Conference on Computer Vision, pp. 12009–12020, 2023h.
Zun Wang, Jialu Li, Yicong Hong, Songze Li, Kunchang Li, Shoubin Yu, Yi Wang, Yu Qiao, Yali Wang,
Mohit Bansal, et al. Bootstrapping language-guided navigation learning with self-refining data flywheel.
arXiv preprint arXiv:2412.08467, 2024c.
William H Warren. Non-euclidean navigation. Journal of Experimental Biology, 222(Suppl_1):jeb187971,
2019.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le,
and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. In Advances in
Neural Information Processing Systems, 2022.
Licheng Wen, Daocheng Fu, Xin Li, Xinyu Cai, Tao Ma, Pinlong Cai, Min Dou, Botian Shi, Liang He, and
Yu Qiao. Dilu: A knowledge-driven approach to autonomous driving with large language models. In The
Twelfth International Conference on Learning Representations, 2023.
WansenWu, TaoChang, XinmengLi, QuanjunYin, andYueHu. Vision-languagenavigation: asurveyand
taxonomy. Neural Computing and Applications, 36(7):3291–3316, 2024.
Zongkai Wu, Zihan Liu, and Donglin Wang. Multi-grounding navigator for self-supervised vision-and-
language navigation. In 2021 International Joint Conference on Neural Networks (IJCNN), pp. 1–8.
IEEE, 2021.
Fei Xia, Amir R Zamir, Zhiyang He, Alexander Sax, Jitendra Malik, and Silvio Savarese. Gibson env: Real-
world perception for embodied agents. In Proceedings of the IEEE conference on computer vision and
pattern recognition, pp. 9068–9079, 2018.
Qiaolin Xia, Xiujun Li, Chunyuan Li, Yonatan Bisk, Zhifang Sui, Jianfeng Gao, Yejin Choi, and Noah A
Smith. Multi-view learning for vision-and-language navigation. arXiv preprint arXiv:2003.00857, 2020.
Jiannan Xiang, Tianhua Tao, Yi Gu, Tianmin Shu, Zirui Wang, Zichao Yang, and Zhiting Hu. Language
models meet world models: Embodied experiences enhance language models. In Conference on Neural
Information Processing Systems, volume 36, 2024.
NingXie,FarleyLai,DerekDoran,andAsimKadav. Visualentailment: Anoveltaskforfine-grainedimage
understanding. arXiv preprint arXiv:1901.06706, 2019.
29

Published in Transactions on Machine Learning Research (12/2024)
ZhenhuaXu,YujiaZhang,EnzeXie,ZhenZhao,YongGuo,Kwan-YeeKWong,ZhenguoLi,andHengshuang
Zhao. Drivegpt4: Interpretable end-to-end autonomous driving via large language model. IEEE Robotics
and Automation Letters, 2024a.
Zhiyuan Xu, Kun Wu, Junjie Wen, Jinming Li, Ning Liu, Zhengping Che, and Jian Tang. A survey on
robotics with foundation models: toward embodied ai. arXiv preprint arXiv:2402.02385, 2024b.
Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant, Aditya Barua,
and Colin Raffel. mt5: A massively multilingual pre-trained text-to-text transformer. arXiv preprint
arXiv:2010.11934, 2020.
Xu Yan, Haiming Zhang, Yingjie Cai, Jingming Guo, Weichao Qiu, Bin Gao, Kaiqiang Zhou, Yue Zhao,
Huan Jin, Jiantao Gao, et al. Forging vision foundation models for autonomous driving: Challenges,
methodologies, and opportunities. arXiv preprint arXiv:2401.08045, 2024.
JianingYang,XuweiyiChen,ShengyiQian,NikhilMadaan,MadhavanIyengar,DavidF.Fouhey,andJoyce
Chai. Llm-grounder: Open-vocabulary 3d visual grounding with large language model as an agent. In
Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), 2024.
Jingkang Yang, Yuhao Dong, Shuai Liu, Bo Li, Ziyue Wang, Haoran Tan, Chencheng Jiang, Jiamu Kang,
YuanhanZhang,KaiyangZhou,etal. Octopus: Embodiedvision-languageprogrammerfromenvironmen-
tal feedback. In European Conference on Computer Vision, pp. 20–38. Springer, 2025.
Qinghao Ye, Haiyang Xu, Guohai Xu, Jiabo Ye, Ming Yan, Yiyang Zhou, Junyang Wang, Anwen Hu,
Pengcheng Shi, Yaya Shi, et al. mplug-owl: Modularization empowers large language models with multi-
modality. arXiv preprint arXiv:2304.14178, 2023.
Sriram Yenamandra, Arun Ramachandran, Karmesh Yadav, Austin S Wang, Mukul Khanna, Theophile
Gervet, Tsung-Yen Yang, Vidhi Jain, Alexander Clegg, John M Turner, et al. Homerobot: Open-
vocabulary mobile manipulation. In Conference on Robot Learning, pp. 1975–2011, 2023.
JianhaoYuan,ShuyangSun,DanielOmeiza,BoZhao,PaulNewman,LarsKunze,andMatthewGadd. Rag-
driver: Generalisable driving explanations with retrieval-augmented in-context learning in multi-modal
large language model. arXiv preprint arXiv:2402.10828, 2024.
YuexiangZhai,HaoBai,ZipengLin,JiayiPan,ShengbangTong,YifeiZhou,AlaneSuhr,SainingXie,Yann
LeCun, Yi Ma, and Sergey Levine. Fine-tuning large vision-language models as decision-making agents
via reinforcement learning. In The Thirty-eighth Annual Conference on Neural Information Processing
Systems, 2024.
Zhaohuan Zhan, Jinghui Qin, Wei Zhuo, and Guang Tan. Enhancing vision and language navigation with
prompt-basedsceneknowledge. IEEE Transactions on Circuits and Systems for Video Technology, 2024a.
Zhaohuan Zhan, Lisha Yu, Sijie Yu, and Guang Tan. Mc-gpt: Empowering vision-and-language navigation
with memory map and reasoning chains. arXiv preprint arXiv:2405.10620, 2024b.
Jiazhao Zhang, Kunyu Wang, Rongtao Xu, Gengze Zhou, Yicong Hong, Xiaomeng Fang, Qi Wu, Zhizheng
Zhang, and Wang He. Navid: Video-based vlm plans the next step for vision-and-language navigation. In
Robotics: Science and Systems (RSS), 2024a.
TianyaoZhang,XiaoguangHu,JinXiao,andGuofengZhang. Asurveyofvisualnavigation: Fromgeometry
to embodied ai. Engineering Applications of Artificial Intelligence, 114:105036, 2022a.
Yichi Zhang, Jianing Yang, Jiayi Pan, Shane Storks, Nikhil Devraj, Ziqiao Ma, Keunwoo Peter Yu, Yuwei
Bao,andJoyceChai. Danli: Deliberativeagentforfollowingnaturallanguageinstructions. InProceedings
of the Conference on Empirical Methods in Natural Language Processing, 2022b.
Yichi Zhang, Jianing Yang, Keunwoo Yu, Yinpei Dai, Shane Storks, Yuwei Bao, Jiayi Pan, Nikhil Devraj,
ZiqiaoMa, andJoyceChai. Seagull: Anembodiedagentforinstructionfollowingthroughsituateddialog.
In Alexa Prize SimBot Challenge Proceedings, 2023.
30

Published in Transactions on Machine Learning Research (12/2024)
Yubo Zhang, Hao Tan, and Mohit Bansal. Diagnosing the environment bias in vision-and-language naviga-
tion. In Proceedings of the Twenty-Ninth International Conference on International Joint Conferences on
Artificial Intelligence, pp. 890–897, 2021a.
Yue Zhang and Parisa Kordjamshidi. Lovis: Learning orientation and visual signals for vision and language
navigation. In Proceedings of the 29th International Conference on Computational Linguistics, pp. 5745–
5754, 2022a.
Yue Zhang and Parisa Kordjamshidi. Explicit object relation alignment for vision and language navigation.
In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics: Student
Research Workshop, pp. 322–331, 2022b.
Yue Zhang and Parisa Kordjamshidi. VLN-Trans: Translator for the vision and language navigation agent.
In The 61st Annual Meeting Of The Association For Computational Linguistics, 2023.
Yue Zhang and Parisa Kordjamshidi. Narrowing the gap between vision and action in navigation. In
Proceedings of the 32nd ACM International Conference on Multimedia, pp. 856–865, 2024.
Yue Zhang, Quan Guo, and Parisa Kordjamshidi. Towards navigation by reasoning over spatial configu-
rations. In Proceedings of Second International Combined Workshop on Spatial Language Understanding
and Grounded Communication for Robotics, pp. 42–52, 2021b.
Yue Zhang, Quan Guo, and Parisa Kordjamshidi. NavHint: Vision and language navigation agent with a
hint generator. In Findings of the Association for Computational Linguistics: EACL 2024, pp. 92–103,
2024b.
Yue Zhang, Zhiyang Xu, Ying Shen, Parisa Kordjamshidi, and Lifu Huang. Spartun3d: Situated spatial
understanding of 3d world in large language models. arXiv preprint arXiv:2410.03878, 2024c.
Yue Zhang, Ben Colman, Xiao Guo, Ali Shahriyari, and Gaurav Bharaj. Common sense reasoning for
deepfake detection. In European Conference on Computer Vision, pp. 399–415. Springer, 2025.
Zheyuan Zhang, Fengyuan Hu, Jayjun Lee, Freda Shi, Parisa Kordjamshidi, Joyce Chai, and Ziqiao Ma. Do
vision-language models represent space and how? evaluating spatial frame of reference under ambiguities.
In Pluralistic Alignment Workshop at NeurIPS 2024, 2024d.
Zhihao Zhang, Shengcao Cao, and Yu-Xiong Wang. Tamm: Triadapter multi-modal learning for 3d shape
understanding.InProceedingsoftheIEEE/CVFConferenceonComputerVisionandPatternRecognition,
pp. 21413–21423, 2024e.
Ming Zhao, Peter Anderson, Vihan Jain, Su Wang, Alexander Ku, Jason Baldridge, and Eugene Ie. On the
evaluation of vision-and-language navigation instructions. In Proceedings of the 16th Conference of the
European Chapter of the Association for Computational Linguistics: Main Volume, pp. 1302–1316, 2021.
YushengZhao, JinyuChen, ChenGao, WenguanWang, LirongYang, HaibingRen, HuaxiaXia, andSiLiu.
Target-driven structured transformer planner for vision-language navigation. pp. 4194–4203, 2022.
Duo Zheng, Shijia Huang, Lin Zhao, Yiwu Zhong, and Liwei Wang. Towards learning a generalist model
for embodied navigation. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pp. 13624–13634, 2024a.
Kaizhi Zheng, Kaiwen Zhou, Jing Gu, Yue Fan, Jialu Wang, Zonglin Di, Xuehai He, and Xin Eric Wang.
Jarvis: A neuro-symbolic commonsense reasoning framework for conversational embodied agents. arXiv
preprint arXiv:2208.13266, 2022.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric. P Xing, Hao Zhang, Joseph E. Gonzalez, and Ion Stoica. Judging llm-as-
a-judge with mt-bench and chatbot arena, 2023.
31

Published in Transactions on Machine Learning Research (12/2024)
Qi Zheng, Daqing Liu, Chaoyue Wang, Jing Zhang, Dadong Wang, and Dacheng Tao. Esceme: Vision-and-
language navigation with episodic scene memory. International Journal of Computer Vision, pp. 1–21,
2024b.
Ce Zhou, Qian Li, Chen Li, Jun Yu, Yixin Liu, Guangjing Wang, Kai Zhang, Cheng Ji, Qiben Yan, Lifang
He,etal. Acomprehensivesurveyonpretrainedfoundationmodels: Ahistoryfromberttochatgpt. arXiv
preprint arXiv:2302.09419, 2023.
Gengze Zhou, Yicong Hong, and Qi Wu. Navgpt: Explicit reasoning in vision-and-language navigation
with large language models. pp. 7641–7649. AAAI Press, 2024a. doi: 10.1609/AAAI.V38I7.28597. URL
https://doi.org/10.1609/aaai.v38i7.28597.
Gengze Zhou, Yicong Hong, and Qi Wu. Navgpt: Explicit reasoning in vision-and-language navigation with
large language models. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pp.
7641–7649, 2024b.
Gengze Zhou, Yicong Hong, Zun Wang, Xin Eric Wang, and Qi Wu. Navgpt-2: Unleashing navigational
reasoning capability for large vision-language models. In European Conference on Computer Vision, pp.
260–278. Springer, 2025.
Qinhong Zhou, Sunli Chen, Yisong Wang, Haozhe Xu, Weihua Du, Hongxin Zhang, Yilun Du, Joshua B
Tenenbaum, and Chuang Gan. Hazard challenge: Embodied decision making in dynamically changing
environments. In The Twelfth International Conference on Learning Representations, 2024c.
Xinzhe Zhou and Yadong Mu. Tree-structured trajectory encoding for vision-and-language navigation. In
Proceedings of the AAAI Conference on Artificial Intelligence, volume 37, pp. 3814–3824, 2023.
ChenZhu,MichaelMeurer,andChristophGünther.Integrityofvisualnavigation—developments,challenges,
and prospects. NAVIGATION: Journal of the Institute of Navigation, 69(2), 2022.
Fengda Zhu, Yi Zhu, Xiaojun Chang, and Xiaodan Liang. Vision-language navigation with self-supervised
auxiliary reasoning tasks. In Proceedings of the IEEE/CVF conference on computer vision and pattern
recognition, pp. 10012–10022, 2020.
Fengda Zhu, Xiwen Liang, Yi Zhu, Qizhi Yu, Xiaojun Chang, and Xiaodan Liang. Soon: Scenario oriented
objectnavigationwithgraph-basedexploration.InProceedingsoftheIEEE/CVFConferenceonComputer
Vision and Pattern Recognition, pp. 12689–12699, 2021a.
Fengda Zhu, Yi Zhu, Vincent Lee, Xiaodan Liang, and Xiaojun Chang. Deep learning for embodied vision
navigation: A survey. arXiv preprint arXiv:2108.04097, 2021b.
Fengda Zhu, Vincent CS Lee, Xiaojun Chang, and Xiaodan Liang. Vision language navigation with
knowledge-driven environmental dreamer. In International Joint Conference on Artificial Intelligence
2023, pp. 1840–1848. Association for the Advancement of Artificial Intelligence (AAAI), 2023.
Yi Zhu, Yue Weng, Fengda Zhu, Xiaodan Liang, Qixiang Ye, Yutong Lu, and Jianbin Jiao. Self-motivated
communication agent for real-world vision-dialog navigation. In Proceedings of the IEEE/CVF Interna-
tional Conference on Computer Vision, pp. 1594–1603, 2021c.
32
