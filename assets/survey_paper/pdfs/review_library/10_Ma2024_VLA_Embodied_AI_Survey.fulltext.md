Title: A Survey on Vision-Language-Action Models for Embodied AI

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/survey_paper/pdfs/review_library/10_Ma2024_VLA_Embodied_AI_Survey.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:41+00:00
- page_count: 54
- status: ok
- text_char_count: 340835

Metadata:
- author: Yueen Ma; Zixing Song; Yuzheng Zhuang; Jianye Hao; Irwin King
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Background (page 2)
- Vision-Language-Action Models (page 3)
  - Components of VLA (page 3)
    - Reinforcement Learning (page 3)
    - Pretrained Visual Representations (page 3)
    - Video Representations (page 4)
    - Dynamics Learning (page 4)
    - World Models (page 5)
    - LLM-induced World Models (page 5)
    - Visual World Models (page 6)
    - Reasoning (page 6)
    - Policy Steering (page 6)
  - Low-level Control Policies (page 6)
    - Non-Transformer Control Policies (page 7)
    - Transformer-based Control Policies (page 7)
    - Control Policies for Multimodal Instructions (page 9)
    - Control Policies with 3D Vision (page 9)
    - Diffusion-based Control Policies (page 10)
    - Diffusion-based Control Policies with 3D Vision (page 10)
    - Control Policies for Motion Planning (page 10)
    - Control Policies with Point-based Action (page 10)
    - Large VLA (page 10)
- Task Planners (page 12)
  - Monolithic Task Planners (page 12)
    - End-to-end Task Planners (page 12)
    - End-to-end Task Planners with 3D Vision (page 13)
    - Grounded Task Planners (page 13)
  - Modular Task Planners (page 13)
    - Language-based Task Planners (page 13)
    - Code-based Task Planners (page 14)
- Datasets and Benchmarks (page 14)
  - Real-world Robot Datasets & Benchmarks (page 14)
  - Simulators, Simulated Robot Datasets & Benchmarks (page 14)
  - Automated Dataset Collection (page 15)
  - Human Datasets (page 15)
  - Task Planning Benchmarks (page 15)
  - Embodied Question Answering Benchmarks (page 15)
- Challenges and Future Directions (page 15)
- Conclusion (page 16)
- References (page 17)
- Appendix (page 37)
  - Background (page 37)
    - Unimodal Models (page 37)
    - Vision-Language Models (page 37)
  - Background (Extended Version): Unimodal Models (page 37)
    - Computer Vision (page 38)
    - Natural Language Processing (page 38)
    - Reinforcement Learning (page 40)
    - Graph (page 40)
  - Background (Extended Version): Vision-Language Models (page 41)
    - Self-supervised pretraining (page 41)
    - Contrastive pretraining (page 41)
    - Large multi-modal model (page 43)
  - Supplementary Related Work (page 43)
  - Additional VLA-Related Work (page 44)
    - Components of VLA: Pretraining (page 44)
    - Components of VLA: World Models (page 44)
    - Components of VLA: Imitation Learning (page 44)
    - Subsequent Surveys on VLA (page 45)
    - Latest Developments of VLA (page 45)
    - Beyond VLA (page 50)

Markdown Content:

1
A Survey on Vision-Language-Action Models for
Embodied AI
Yueen Ma, Zixing Song, Yuzheng Zhuang, Jianye Hao, Irwin King, Fellow, IEEE
Abstract—Embodied AI is widely recognized as a cornerstone Action
of artificial general intelligence because it involves controlling
embodiedagentstoperformtasksinthephysicalworld.Building World Reasoning Policy
Model Steering
on the success of large language models and vision-language
models, a new category of multimodal models—referred to as
vision-language-action models (VLAs)—has emerged to address Reinforcement Action Decoder Dynamics
language-conditionedrobotictasksinembodiedAIbyleveraging Learning Learning
theirdistinctabilitytogenerateactions.Therecentproliferation
of VLAs necessitates a comprehensive survey to capture the
rapidly evolving landscape. To this end, we present the first Pretrained Vision Language Pretrained
Visual Repr. Encoder Encoder Lang. Model
surveyonVLAsforembodiedAI.Thisworkprovidesadetailed
taxonomyofVLAs,organizedintothreemajorlinesofresearch.
State Instruction
The first line focuses on individual components of VLAs. The
secondlineisdedicatedtodevelopingVLA-basedcontrolpolicies Figure 1: The general architecture of vision-language-action
adept at predicting low-level actions. The third line comprises models.Threerepresentativemethodsforactionpredictionare
high-level task planners capable of decomposing long-horizon
shown. Related components are presented in dashed boxes.
tasks into a sequence of subtasks, thereby guiding VLAs to
follow more general user instructions. Furthermore, we provide
an extensive summary of relevant resources, including datasets, AlexNet [2] showcased the potential of artificial neural net-
simulators, and benchmarks. Finally, we discuss the challenges works (ANNs). Recurrent neural networks laid the ground-
facingVLAsandoutlinepromisingfuturedirectionsinembodied workfornumerousnaturallanguageprocessing(NLP)models,
AI. A curated repository associated with this survey is available
but have seen a transition in recent years, with Transformers
at: https://github.com/yueen-ma/Awesome-VLA.
[3] taking precedence. The Deep Q-network [4] demonstrated
Index Terms—Vision-Language-Action Model, Embodied AI, that ANNs can successfully tackle reinforcement learning
Robotics, Multimodality, Large Language Model, World Model
(RL)problems.Leveragingadvancementsofunimodalmodels
across diverse machine learning fields, multimodal models
I. INTRODUCTION now address a wide range of tasks, such as visual question
answering, image captioning, and text-to-video generation.
Vision-language-action models (VLAs) are a class of mul-
Conventionalrobotpoliciesbasedonreinforcementlearning
timodal models within the field of embodied AI, designed
have largely focused on addressing a limited set of tasks
to process information from three modalities: vision, lan-
within controlled environments, such as item grasping [5].
guage, and action. Unlike conversational AI, embodied AI
However, there is a growing need for more versatile multi-
requires controlling physical embodiments that interact with
task policies, akin to recent trends in large language models
the environment, and robotics is the most prominent domain
(LLMs) and vision-language models (VLMs). Developing a
of embodied AI. In language-conditioned robotic tasks, the
multi-task policy is challenging, as it requires learning a
policy must possess the capability to understand language
broader set of skills and adapting to diverse environments.
instructions, visually perceive the environment, and generate
Furthermore, specifying tasks via language instructions offers
appropriate actions, necessitating the multimodal capabilities
a more intuitive user-robot interface, which necessitates the
ofVLAs.ThetermwasrecentlycoinedbyRT-2[1].Compared
development of language-conditioned robot policies.
toearlierdeepreinforcementlearningapproaches,VLAsoffer
Built upon the success of large VLMs, vision-language-
superior versatility, dexterity, and generalizability in complex
action models have demonstrated their potential in addressing
environments. As a result, they are well-suited not only for
these challenges, as illustrated in Figure 1. Similar to VLMs,
controlled settings like factories but also for everyday tasks in
VLAs utilize vision foundation models as vision encoders to
household environments.
obtainpretrainedvisualrepresentationsofthecurrentenviron-
Early developments in deep learning primarily consist of
mental state, such as object class, pose, and geometry. VLAs
unimodal models. In computer vision (CV), models like
encodeinstructionsusingthetokenembeddingsoftheirLLMs
and employ various strategies to align vision and language
Y. Ma and I. King are with the Chinese University of Hong Kong, Hong
Kong,China(Email:{yema21, king}@cse.cuhk.edu.hk) embeddings,includingapproacheslikeBLIP-2[6]andLLaVA
Z. Song is with University of Bristol, Bristol, UK (Email: [7]. By finetuning on robot data, the LLM can function as a
zixing.song@bristol.ac.uk)
decoder to predict actions and perform language-conditioned
Y.ZhuangandJ.HaoarewithHuaweiNoah’sArkLab,Shenzhen,China
(Email:{zhuangyuzheng, haojianye}@huawei.com) robotic tasks. These cross-disciplinary innovations drive the
6202
beF
4
]OR.sc[
7v39041.5042:viXra

2
Embodied AI ResNet SENet ViT SAM Dreamer R3M MVP VC-1 TWM SMART Genie
Task Planner 2015 2017 2020 2023 2020 2022 2022 2023 2023 2023 2024
Input: user instruction Computer Vision Components of VLA
Output: subtask ViLBERT CLIP LLaVA w P o i r o l n d e m er o in d g e l Time le c a o r n n t in ra g stive A r d o a b p o t t i M c A PV E R to ex A is t s i t n u g d y P V of R s bas T e r d a n w s o fo rl r d m m er o - del inve F r o s r e w d a y r n d a & m ics f F ro o m un u d n a s ti u o p n e w rv o is r e ld d m vi o d d e e o l s
Control Policy GRU Transformer 2019 2021 2023 CLIPort BC-Z RT-1 VIMA RT-2 OpenVLA ECoT
Input: state
Output: action 2014 2017 VLA 2021 2021 2022 2022 2023 2024 2024
G In e p n u O t e : u r s t t a p a u t l e t i , : z i a n e c s t d t i r o u n V cti L on A Natural Language Process B ing 2 E 0 R 19 T Cha 20 t 2 G 2 PT w C it o h m C T b o r i a n n n e t s r C p o o L l r I t P P e r olicy ge Z ne e r r a o l - i s z h a o ti t o n c T o r n a t n ro sf l o p r o m li e c r y Mu p l r t o i- m m p o t dal LL co M in -b ed as t e h d e c t o e n rm tro , " l V p L ol A ic " y, O l p a e r n ge -s V ou L r A ce E T m ho b u o g d h ie t d R C ea h s a o in n - in o g f-
Large VLA DQN PPO DPO SayCan Inner Monologue CaP ProgPrompt PaLM-E EAI
Adapted from a large 2015 2017 2023 2022 2022 2022 2022 2023 2024
VLM to predict actions Reinforcement Learning Task Planner
Alp 2 h 01 a 6 GO D 2 a 0 c 1 t 8 yl DT 202 T 1 T Gr in o u r n ea d l i - n w g o L rl L d M Lang la u n a g g u e a -b g a e s f e u d s i v o i n sion- Co la d n e g -b u a a s g e e d f u v s is io io n n- P p ro ro gr m a p m t m st a r t u i c c t L u L re M m L u a lt r i g - e m e o m da b l o m di o e d d e l In E te m rf b ac o e d i B e e d n A ch ge m n a t rk
(a) Concepts (b) Timelines
Figure 2: (a) A Venn diagram that outlines the main concepts in embodied AI discussed in this paper. (b) Timelines that trace
the evolution from unimodal models to vision-language-action models.
advancement of VLAs in embodied AI—a critical building the first comprehensive survey of emerging vision-language-
block for artificial general intelligence (AGI). action (VLA) models in the field of embodied AI.
VLAs are closely related to three lines of work, as de- • Comprehensive Review. We present a thorough review
picted by the timelines in Figure 2b and the taxonomy in ofemergingVLAmodelsinembodiedAI,coveringvari-
Figure 3. Some approaches focus on individual components ous aspects including components, architectures, training
of VLAs (§III-A), such as pretrained visual representations, objectives, robotic tasks, etc.
dynamics learning, world models, and reasoning. Meanwhile, • Taxonomy. We introduce a taxonomy of VLAs based
asubstantialbodyofresearchisdedicatedtolow-levelcontrol onthehierarchicalframeworkofcurrentroboticsystems,
policies (§III-B). In this category, language instructions and comprisingtwohierarchies:alow-levelcontrolpolicyand
visual perceptions are fed into the control policy, which then a high-level task planner. Control policies execute low-
generateslow-levelactions—suchastranslationandrotation— level actions based on specified language commands and
thereby rendering VLAs an ideal choice for control policies. the perceived environment. Task planners provide guid-
In contrast, another category of models serves as high-level ance to control policies by decomposing long-horizon
task planners responsible for task decomposition (§IV). These tasks into subtasks. We also discuss various essential
models break down long-horizon tasks into a sequence of components of VLAs.
subtasks that, in turn, guide VLAs toward the overall goal, • Resources. We summarize the necessary resources for
as illustrated in Figure 4. Most current robotic systems adopt training and evaluating VLAs, including recent datasets
such a hierarchical framework [8]–[10] because the high-level andbenchmarksinreal-worldorsimulatedenvironments.
task planner can leverage models with high capacity while We also discuss various approaches to address current
the low-level control policy can focus on speed and precision, challenges, such as data scarcity and inconsistency.
similar to hierarchical reinforcement learning. • Future Directions. We outline current challenges and
To provide a more comprehensive overview of current promisingfutureopportunitiesinthefield,suchassafety,
progress in embodied AI, we propose a generalized definition foundation models, and real-world deployment.
of“VLA,”asillustratedbytheVenndiagraminFigure2a.We
define a VLA as any model capable of processing multimodal II. BACKGROUND
inputs from vision and language to produce robot actions that
Embodied AI is a unique form of artificial intelligence that
accomplish embodied tasks, typically following the architec-
actively interacts with the physical environment. This sets
ture in Figure 1. The original concept of VLA referred to a
it apart from other AI models, such as conversational AI,
modelthatadaptsVLMstorobotictasks[1].Analogoustothe
which primarily handles textual conversations, or generative
distinctionbetweenLLMsandmoregenerallanguagemodels,
AI models that focus on tasks like text-to-video generation.
we designate the original VLAs as “Large VLAs” (LVLAs)
EmbodiedAIencompassesabroadspectrumofembodiments,
because they are based on LLMs or large VLMs.
including smart appliances, smart glasses, autonomous vehi-
Related Work. To the best of our knowledge, this survey cles, and more. Among them all, robots stand out as one of
is the first to review the recent progress of VLA models, the most prominent embodiments.
a rapidly emerging research area. Previous surveys have in- Robot learning is also usually framed as a reinforcement
vestigated other facets of embodied AI. [11] comprehensively learning problem, represented as a Markov Decision Process
summarized foundation models in robotics up to 2023, while (MDP)consistingofstates(s),actions(a),andrewards(r).A
[12] focused on LLMs in robotics. [13] examined more MDPtrajectoryisdenotedasτ =(s ,a ,r ,...,s ,a ,r ).
1 1 1 T T T
recent vision, language, and robotic foundation models for In certain scenarios, robotic tasks may also be viewed as
general-purpose robots. [14] concentrates on real-world robot Partially Observable Markov Decision Processes (POMDPs)
applications. In contrast, our work emphasizes VLA models, due to incomplete observations. The primary objective of
thereby complementing and extending the existing literature reinforcement learning is to train a policy capable of gen-
on embodied AI. erating optimal actions for the current state π(a |s ,a ).
t ≤t <t
Contributions. To the best of our knowledge, this paper is Various methods, such as TD learning, policy gradients, etc.,

3
VLA§III
ComponentsofVLA§III-A ControlPolicies§III-B TaskPlanners§IV Datasets&Benchmarks§V
ReinforcementLearning§III-A1 Non-Transformer§III-B1
Monolithic§IV-A Real-world§V-A
PretrainedVisualRepr.§III-A2 Transformer-based§III-B2
End-to-end§IV-A1 Simulation§V-B
VideoRepr.§III-A3 MultimodalInstructions§III-B3
DynamicsLearning§III-A4 3DVision§III-B4 3DVision§IV-A2 Simulators
WorldModels§III-A5 3DVision+Diffusion§III-B6 Grounded§IV-A3 AutoDataCollection§V-C
LLM-induced§III-A6 Diffusion§III-B5
Modular§IV-B HumanData§V-D
Visual§III-A7 MotionPlanning§III-B7
Language-based§IV-B1 TaskPlanningBench.§V-E
Reasoning§III-A8 Point-basedAction§III-B8
PolicySteering§III-A9 LargeVLA§III-B9 Code-based§IV-B2 EmbodiedQA§V-F
Figure 3: The taxonomy of VLA models. The organization of this survey follows this taxonomy.
can be employed to achieve this. However, in cases where design reward functions for embodied agents that outperform
defining the reward function proves challenging, imitation expert human-engineered ones. As LLMs evolve, this synergy
learning is utilized to directly model the action distribution accelerates progress in RL and embodied AI.
withintrajectoriesdevoidofrewardsτ =(s ,a ,...,s ,a ). 2) Pretrained Visual Representations: The effectiveness of
1 1 T T
Furthermore, many multi-task robot models employ language the vision encoder directly influences the performance of
as instructions p to determine which task or skill to execute, VLAs,asitprovidescrucialinformationregardingthecurrent
leading to the development of language-conditioned robot state s , such as object categories, positions, and affordance.
t
policies π(a |p,s ,a ). Consequently, numerous methods are devoted to improving
t ≤t <t
the quality of pretrained visual representations (PVRs). Their
technical details are compared in Table I.
III. VISION-LANGUAGE-ACTIONMODELS
CLIP [22] has gained widespread adoption as a vision
A. Components of VLA
encoderinroboticmodels.ThetrainingobjectiveofCLIPisto
A body of work focuses on individual components of VLA identify the correct text-image pair among all possible combi-
models, drawing on successes in CV, NLP, and RL. We nationsinagivenbatch. CLIPundergoestrainingontheWIT
introduce them through the lens of embodied AI. dataset, comprising 400 million image-text pairs. This large-
1) Reinforcement Learning: Reinforcement learning (RL) scale training allows CLIP to develop a rich understanding of
laid the foundation for embodied AI and continues to help the relationship between visual and textual information.
advance VLAs. Deep Q-Network (DQN) first demonstrated R3M [23] proposes two main pretraining objectives: time
learning policies directly from high-dimensional pixel inputs, contrastivelearningandvideo-languagealignment.Theobjec-
underscoring the need for greater model capacity in end-to- tive of time contrastive learning is to minimize the distance
end RL. RL trajectories—sequences of states, actions, and between temporally proximal video frames while simultane-
rewards—naturally align with sequence modeling problems, ously increasing the separation between temporally distant
making them well-suited to transformer architectures. Pio- ones. This objective aims to create PVRs that capture the
neering efforts in this direction include Decision Transformer temporal relationship within the video sequence. On the other
(DT) [15] and Trajectory Transformer (TT) [16]. Gato [17] hand, video-language alignment is to learn whether a video
further extended this paradigm to a multimodal, multitask, corresponds to a language instruction. This objective enriches
multi-embodiment setting. π∗ [18] employs RL for VLAs the semantic relevance embedded in the PVRs. VIP [24] also
0.6
to learn from experience. capitalizes on the video temporal relationship.
Furthermore, a synergy has emerged between RL and MVP [25] adopts masked autoencoder (MAE) from com-
LLMs, benefiting embodied AI in multiple ways. Reinforce- puter vision to robotic datasets. The MAE involves masking
ment learning from human feedback (RLHF) aligns LLMs out a portion of input patches to a ViT model and training
with human preferences and has also been applied to robot it to reconstruct the corrupted patches. This approach closely
learning. SEED [19] utilizes RLHF alongside skill-based RL resembles the masked language modeling technique used in
to address the sparse reward issue and to improve safety BERT [26] and falls within the purview of self-supervised
via human evaluation. Conversely, LLMs also enable novel training.RPT[27]undergoespretrainingwithafocusnotonly
RL methods. Reflexion [20] proposes a novel verbal rein- onreconstructingvisualinputsbutalsoonroboticactionsand
forcement learning framework that replaces weight updates proprioceptive states.
in RL models with linguistic feedback, which is naturally Voltron [32] introduces a pretraining objective by incor-
applicable to embodied decision-making, where planning also porating language conditioning and language generation into
occurs in language form. Eureka [21] shows that LLMs can the MAE objective. Employing an encoder-decoder Trans-

4
Table I: Pretrained visual representations. V: Vision. L: Language. CL: contrastive learning. TFM: Transformer. Sim/Real:
simulated/real-world.Mani/Navi:manipulation/navigation.Forsimplicity,weonlyshowthemainpartoftheobjectiveequation,
omitting elements such as temperature, auxiliary loss, etc. S(·) denotes a similarity measure.
Model Network Type Objective Notations RoboticTasks
CLIP[22] ViT-B VL-CL (cid:80)N
i=1
−log(cid:80)N
j=
ex
1
p
e
(
x
S
p
(
(
x
S
i
(
,y
x
i
i
)
,
)
yj))
(xi,yi):image-textpair
a
(U
nd
se
C
d
o
b
W
yC
[3
L
0
I
]
P
)
ort[28],EmbCLIP[29],
R3M[23] ResNet-50 Time-CL (cid:80)T
i=1
−log
exp(S(x
e
i
x
,x
p
j
(
)
S
)
(
+
x
e
i
x
,x
p
j
(
)
S
)
(xi,xk))
xi:i-thvideoframe,i<j<k S
A
i
d
m
ro
-M
it
ani:Meta-World,FrankaKitchen,
MVP[25] ViT-B/L MAE (cid:80)N
i=1
−logP(cid:0)xi|x̸=i (cid:1) xi:imagepatch Real-Mani(xArm7):pick,reachblock,
pushcube,closefridge
VIP[24] ResNet-50 Time-CL (cid:80)T
i=1
−log
exp(S(x
e
0
x
,x
p
j
(S
))
(
+
x0
ex
,x
p
j
(
)
S
)
(xi,xj))
xi:i-thvideoframe,0<i<j R
dr
e
a
a
w
l-
e
M
r,
a
p
n
u
i
sh
(F
b
r
o
a
t
n
t
k
le
a
,
):
fo
p
l
i
d
ck
to
a
w
n
e
d
l
place,close
VC-1[31] ViT-L MAE,CL (Acombinationofpreviousworks,including Sim-Mani:Meta-World,Adroit,DMC,
CLIP,R3M,MVP,andVIP.) TriFinger,Habitat2.0;Sim-Navi:Habitat
Voltron[32] TFM MAE, (cid:80)N
i=1
−logP(cid:0)xi|x̸=i,y(cid:1); xi:imagepatch; Sim-Mani:FrankaKitchen;
RPT[27] ViT L M a A ng E -Gen (cid:80) (cid:80) N i N i = = ′ 1 1 − − l l o o g g P P (cid:0) (y x i i | | x x , ̸= y i < ,y i) ,z,...(cid:1) x y: ,y la , n z g : u t a h g r e ee in d s i t s r t u in c c ti t o m n odalities R R e e a a l l - - M M a a n n i i ( ( F F r r a a n n k k a a ) ) : : s c t u a s c t k o , m pi s c t k u , dy pic d k esk
frombin
DINOv2 ResNet,ViT Self- (cid:80) x (cid:80) x′̸=x H(Pt(x),Px(x′)) x,x′:imageviews;H():cross-entropy; (UsedbyOpenVLA[34],ReKep[35])
[33] distillation Pt,Ps:teacher,student
I-JEPA[36] ViT JEPA
M
1 (cid:80)M
i=1
(cid:80)
j
∥xj(i)−yj(i)∥2
2
xj(i):j-thmaskedpatchembeddingof
blocki;yj(i):unmaskedpatchembedding
Theia[37] ViT-T/S/B Distillation (Distillationofvisionfoundationmodels: Sim-Mani&Navi:CortexBench(VC-1);
ViT,CLIP,SAM,DINOv2,Depth-Anything.) Real-Mani:pick,place,opendoor/drawer
former structure, the pretraining alternates between language- [42] surpasses NeRF in visual quality and rendering speed.
conditioned masked image reconstruction and language gen- Additionally, many videos contain audio, which can provide
eration from masked images. This enhances the alignment important cues for robot policies [43].
between language and vision modalities. 4) Dynamics Learning: Dynamics learning encompasses
VC-1 [31] conducts an in-depth examination of prior PVRs objectives aimed at endowing the model f(·) with an under-
and introduces an enhanced PVR model by systematically standing of forward or inverse dynamics. Forward dynamics
exploring optimal ViT configurations across diverse datasets. involves predicting the subsequent state resulting from a
Additionally,theyperformacomprehensivecomparativeanal- given action, whereas inverse dynamics entails determining
ysis of their model against previous methods on various the action required to transition from a previous state to a
manipulation and navigation datasets, shedding light on the known subsequent state:
critical factors that contribute to the improvement of PVR.
Forward dynamics: sˆ ←f (s ,a ),
Another study [38] also compares previous PVRs obtained t+1 fwd t t (1)
under supervised learning or self-supervised learning. Inverse dynamics: aˆ t ←f inv (s t ,s t+1 ).
DINOv2 [33] proposes a new self-supervised training Some approaches also frame these objectives as reordering
paradigm for PVRs that achieves performance beyond that problems for shuffled state sequences. Some forward dynam-
of MAE. It employs a self-distillation framework in which ics methods closely resemble the image or video prediction
the teacher and student networks receive different views of pretraining used in PVRs. We compare them in Table II.
the same image and match their encoded representations. The
Vi-PRoM[44]presentsthreedistinctpretrainingobjectives.
student network is updated using SGD, while the teacher
The first involves a contrastive self-supervised learning ob-
network is maintained as the EMA of the student network.
jective designed to distinguish between different videos. The
I-JEPA [36] is motivated by the joint-embedding predictive remainingtwoobjectivesarecenteredaroundsupervisedlearn-
architectures proposed by [39]. It constructs a “primitive” ing tasks: temporal dynamics learning, aimed at recovering
internalworldmodelbycomparingtheembeddingsofpatches. shuffled video frames, and image classification employing
Unlike DINO, which uses cropped images, I-JEPA employs pseudo labels. Through a comprehensive comparison with
masked patches. Moreover, it differs from MAE because it is preceding pretraining methods, Vi-PRoM demonstrates its
a non-generative approach. effectiveness for behavior cloning and PPO.
Theia [37] proposes distilling various vision foundation MIDAS [46] introduces an inverse dynamics prediction
models into a single model. By fusing their information from task as part of its pretraining. The objective is to train the
segmentation, depth, semantics, etc., it outperforms previous model to predict actions from observations, formulated as a
PVRs while requiring less data and a smaller model size. motion-following task. This approach enhances the model’s
3) Video Representations: Videos are simple sequences of understanding of the transition dynamics of the environment.
images and can be represented by concatenating the usual SMART [47] presents a pretraining scheme encompassing
PVRsofeachframe.However,theirmulti-viewnatureenables three distinct objectives: forward dynamics prediction, inverse
a variety of unique representation techniques beyond those dynamics prediction, and randomly masked hindsight control.
mentionedabove,suchastimecontrastivelearningandMAE. The forward dynamics prediction task involves predicting the
NeRF can be extracted from videos and contains rich 3D next latent state, while the inverse dynamics prediction task
information for robot learning, as exemplified by F3RM [40] entails predicting the last action. In the case of hindsight
and3D-LLM[41].Therecent3DGaussianSplatting(3D-GS) control, the entire control sequence is provided as input, with

5
Table II: Dynamics learning methods for VLAs. f(·) is the dynamic model. Fwd, inv: forward & inverse dynamics.
Model VisionEncoder Type Objective Notations RoboticTasks
Vi-PRoM[44] ResNet Temporaldynamics (cid:80)T
i=1
CE(i,f(xi|x′)) f(·):predictsframe Sim-Mani:Meta-World,Franka
indexinrawseq.xgiven Kitchen;Real-Mani:open&close
shuffledseq.x′ drawer/door
MaskDP[45] ViT(MAE) MAE(implicitfwd (cid:80)T
i=1
−logP(cid:0)xi|x̸=i,y(cid:1) xi:stateoractiontoken; Sim:DeepMindControlSuite
&invdynamics) y:theothermodality
M SM ID A A R S T [ [ 4 4 6 7 ] ] V C i N T N ,MaskR-CNN d I F n y o v n r e w a r m s a e r i d c d s & yna in m v i e c r s se (cid:80) (cid:80) T i T i = = 1 1 + M (cid:0)M M SE S S E E (a ( ( t s a , t t f + , i f n 1 v i , n ( f v s ( f t w s , d t s ( , t s s + t t , + 1 a ) 1 ) t ) ) ) ) (cid:1) s s t t , , a a t t : : s s t t a a t t e e , , a ac ct t i i o o n n S Si im m : -M D a e n ep i: M V in IM d A C - o B n e tr n o c l h Suite
PACT[48] ResNet-18,PointNet Forwarddynamics (cid:80)T
i=1
MSE(st+1,ffwd(st,at)) st,at:state,action Sim-Navi:Habitat;Real-Navi
(MuSHRvehicle)
VPT[49] ResNet Inversedynamics (cid:80)T
i=1
MSE(at,finv(st,st+1)) st,at:state,action Sim:Minecraft
GR-1[50] ViT(MAE) Forwarddynamics (cid:80)T
i=1
MSE(st+1,ffwd(st,at)) st,at:state,action Sim-Mani:CALVIN
some actions masked, and the model is trained to recover pled from visual world models that explicitly generate images
these masked actions. The incorporation of the first two or videos of future states.
dynamicspredictiontasksfacilitatescapturinglocalandshort- Dreamer[51]employsthreeprimarymodulestoconstructa
term dynamics, while the third task is designed to capture latentdynamicsmodel:arepresentationmodel,responsiblefor
global and long-term temporal dependencies. encoding images into latent states; a transition model, which
MaskDP [45] features the masked decision prediction task, capturestransitionsbetweenlatentstates;andarewardmodel,
wherein both state and action tokens are masked for recon- predicting the reward associated with a given state. Under
struction. This masked modeling task is specifically crafted to the actor-critic framework, Dreamer utilizes an action model
equip the model with an understanding of both forward and and a value model to learn behavior through imagination by
inverse dynamics. Notably, in contrast to preceding masked propagating analytic gradients through the learned dynamics.
modeling approaches like BERT or MAE, MaskDP is applied Building upon this foundation, DreamerV2 [52] introduces a
directly to downstream tasks discrete latent state space along with an improved objective.
PACT[48]introducesapretrainingobjectiveaimedatmod- DreamerV3 [53] extends its focus to a broader range of
eling state-action transitions. It receives sequences of states domainswithfixedhyperparameters.DayDreamer[54]applies
and actions as input, and predicts each state and action token this method to physical robots performing real-world tasks.
autoregressively. This pretrained model serves as a dynamics IRIS [55] employs a GPT-like autoregressive Transformer
model, which can then be finetuned for various downstream as the foundation of its world model, with a VQ-VAE serving
tasks such as localization, mapping, and navigation. as the vision encoder. Subsequently, a policy is trained using
VPT [49] proposes a video pretraining method that har- imagined trajectories, which are unrolled from a real obser-
nessesunlabeledinternetdatatopretrainafoundationalmodel vation by the world model. TWM [56] also investigates the
for the game of Minecraft. The approach begins by training application of Transformers in building world models.
an inverse dynamics model using a limited amount of labeled 6) LLM-inducedWorldModels: LLMsencompassawealth
data, which is then utilized to label internet videos. Subse- ofcommonsenseknowledgeabouttheworld,promptingmany
quently, this newly auto-labeled data is employed to train approaches to leverage that knowledge for improving VLAs.
the VPT foundation model through behavior cloning. This DECKARD [57] prompts LLM to generate abstract world
methodology follows semi-supervised imitation learning. As models (AWMs) represented as directed acyclic graphs [58],
a result of this process, the model demonstrates human-level [59], specifically tailored for the task of item crafting in
performance across a multitude of tasks. Minecraft. DECKARD iterates between two phases: in the
GR-1 [50] introduces video prediction pretraining tailored Dream phase, it samples a subgoal guided by the AWM; in
for a GPT-style model. The ability to anticipate future frames theWakephase,DECKARDexecutesthesubgoalandupdates
aligns with forward dynamics learning, contributing to more the AWM through interactions with the game. This guided
accurate action prediction. approach enables DECKARD to achieve markedly faster item
5) World Models: A world model P(·) encodes common- crafting compared to baselines lacking such guidance.
sense knowledge about the world and predicts the future state LLM-DM [60] uses an LLM to construct world models
for a given action [39]: in planning domain definition language (PDDL)—a capability
that LLM+P [61] did not achieve, as its PDDL world model
sˆ ∼P(sˆ |s ,a ). (2) was hand-crafted. The LLM also acts as an interface, mediat-
t+1 t+1 t t
ing between the generated PDDL model and corrective feed-
It enables model-based control and planning for embodied backfromsyntacticvalidatorsandhumanexperts.Finally,the
agents, as they can search for an optimal action sequence in PDDL world model serves as a symbolic simulator, assisting
imaginary space before executing any real actions. Although the LLM planner in generating plans.
forward dynamics learning also attempts to predict the next RAP [62] repurposes an LLM to act as both a policy that
state, it is usually treated as a pretraining task or an auxiliary predictsactionsandaworldmodelthatprovidesthestatetran-
loss to enhance the RL-Transformer-based action decoder for sition distribution. Unlike previous chain-of-thought prompt-
the primary robotics tasks, rather than serving as a standalone ing methods, RAP incorporates Monte Carlo Tree Search
module. Additionally, new embodied experiences can be sam- (MCTS) to enable structured planning, allowing the LLM to

6
build a reasoning tree incrementally. This reasoning strategy features, before predicting low-level actions. By relying on
helps RAP find a high-reward path that balances exploration this multi-step reasoning rather than the “muscle memory” of
and exploitation. Tree-Planner [63] improves efficiency by VLAs,itimprovessuccessratesonchallenginggeneralization
promptingtheLLMonlyoncetogeneratediversepathswithin tasks without requiring additional robot data. CoT-VLA [77]
an action tree. introduces visual CoT reasoning for VLAs.
LLM-MCTS[64]buildsuponRAPbutextendstheproblem 9) Policy Steering: Policy steering can enhance VLA per-
setting to POMDPs. As a world model, the LLM generates formance at test-time without the need for expensive retrain-
the initial belief of the current state; as a policy, it serves ing.V-GPS[78]re-ranksgeneratedactionsbasedonalearned
as a heuristic to guide action selection. By leveraging its value function, while RoboMonkey [79] employs a VLM-
commonsense knowledge, the LLM reduces the search space based verifier to select the optimal action from a sampled set.
of MCTS, thereby improving search efficiency.
7) VisualWorldModels: UnlikeLLM-inducedworldmod- Strengths and Limitations.
els, which are in textual form, visual world models generate a) PVRs: Althoughtimecontrastivelearningwithvideos
images, videos, or 3D scenes of future states—aligning more and text-guided pretraining methods, such as CLIP, provide
closely with the physical world. They can further be utilized image-level information, they lack the pixel-level details of-
to generate new trajectories. This direction has been gaining fered by MAE-based self-supervised learning methods. Pixel-
increasingattentionsinceSorademonstratedworld-simulation level information contains rich details—including segmenta-
capabilities [65], as investigated by a dedicated survey [66]. tion masks, object positions, and depth estimation—that are
Genie [67] introduces a new class of generative models, generally more useful for robot manipulation tasks requiring
termed Generative Interactive Environments. It consists of high precision, as demonstrated by VC-1’s comparison [31].
three main components: a spatiotemporal video tokenizer, an DINOv2 learns both pixel- and image-level features by com-
autoregressive dynamics model, and a latent action model. bining masked image modeling with a momentum encoder
After being trained on unlabeled videos in an unsupervised and multi-crop augmentation, with benefits on downstream
manner, Genie allows users to interact with the generative robotictasksevidencedbyOpenVLA[34].I-JEPAfocuseson
environment on a frame-by-frame basis. Consequently, Genie patches in the representation space and, as a result, captures
establishes a foundation world model. low-levelimagefeaturesmoreeffectivelythanview-invariance
3D-VLA [68] proposes a 3D world model capable of goal methods such as DINO. Theia distills various off-the-shelf
generation. It processes visual inputs, such as images, depth vision foundation models into a single model that surpasses
maps, and point clouds, and then generates a goal state— isolatedindividualmodels,asdemonstratedbycomprehensive
either as an image or a point cloud—using diffusion models evaluationsagainstmostexistingPVRsinrobotlearning[37].
in response to the user’s query. The generated goal state can b) Forward & inverse dynamics: Forward dynamics
subsequently be used to guide robot control. learning is generally more challenging than inverse dynamics
UniSim [69] builds a generative model based on real-world learningbecausepredictingfuturestatesismorecomplexthan
interaction videos. It is capable of simulating visual outcomes predictingpastactions.Consequently,thedifficultyofforward
for both high-level and low-level actions, which can then be dynamicsoftenleadstogreaterperformanceimprovements,as
leveraged as new experiences for training embodied agents. demonstrated in SMART. However, inverse dynamics models
E2WM [70] even treats existing simulators as world models can be used to generate action labels for datasets that contain
to collect embodied experiences via MCTS. only states, such as raw robot manipulation videos.
8) Reasoning: Reasoning has become a key capability of c) World Models & Reasoning: Although both world
LLMs, as demonstrated by chain-of-thought (CoT) methods models and reasoning methods can be applied to low-level
[71], [72]. In embodied AI, researchers are exploring how to control policies and high-level task planners, current ap-
leverageCoTreasoningtorefinethedecision-makingprocess. proaches remain distinct. World models are predominantly
Reasoningisnaturallycompatiblewithhigh-leveltaskplan- used to interact with control policies because they excel at
ning, as both often occur in the language domain. ThinkBot generatingtheimmediatenextstategivenlow-levelactions.In
[73] applies CoT to recover missing action descriptions in contrast,CoT-basedreasoningmethodsfocusontaskplanning
sparse human instructions, thereby enhancing instruction co- since they express thought chains in text, making them well-
herence and boosting success rates in difficult tasks. ReAct suited for refining text-based task plans.
[74] interleaves reasoning traces and actions, where CoT can
help create action plans, inject commonsense knowledge, and
B. Low-level Control Policies
handle exceptions, ultimately improving embodied decision-
Through the integration of an action decoder with percep-
making. RAT [75] integrates CoT with retrieval-augmented
tion modules, such as vision encoders and language encoders,
generation (RAG) to mitigate hallucinations and thus improve
a VLA model π with parameters θ is formed as a control
embodied planning. Tree-Planner [63] employs a tree-of- θ
policy to execute language instructions p:
thoughts approach for task planning.
Another paradigm involves equipping low-level control
aˆ ∼π (aˆ |p,s ,a ). (3)
t θ t ≤t <t
policies with reasoning capabilities, as pioneered by ECoT
[76]. This method trains OpenVLA [34] to conduct embodied It can also be referred to as a low-level policy, low-level
CoT reasoning about plans, sub-tasks, motions, and visual controller, or action primitive. The diversity among VLAs

7
Clean up the room
High-level LLM
S₀ Task Plan High-level Task Planner VLM S₃
1. Pick up the toy car 2. Move to the coffee table 3. Put near the camera
Low-level Control Policy VLA
S₁ S₂
Initial State: a toy Low-level Control Robot holds Action: Robot near the Action: Goal State: the room
car on the floor Trajectory the toy car Rotation coffee table Translation has been cleaned up
Figure 4: Illustration of a hierarchical robot policy. The high-level task planner decomposes the user instruction into subtasks,
which are then executed step by step by the low-level control policy.
arises from individual modules and overall architectures. The andactionsareextractedfromtheframesofthevideothrough
generalarchitectureisshowninFigure1.Thissectionexplores inversedynamics.Thisinnovativepolicy-as-videoformulation
various approaches to designing low-level control policies. offers several advantages, including enhanced generalization
Table III summarizes their technical details. across diverse robot tasks and the potential for knowledge
1) Non-TransformerControlPolicies: Priortotheadoption transfer from internet videos to real robots.
of Transformer models, early control policies for language- 2) Transformer-based Control Policies: Since the intro-
conditioned robotic tasks varied significantly in architecture. duction of Transformers, control policies have converged to
CLIPort[28]integratesCLIPwiththeTransporternetwork, similar Transformer-based architectures.
creating a two-stream architecture. The CLIP vision encoder InteractiveLanguage[86]presentsaroboticsystemwherein
extracts “semantic” information from the RGB image, while the low-level control policy can be guided in real-time by
the Transporter network extracts “spatial” information from human instructions conveyed through language, enabling the
the RGB-D image. The CLIP sentence encoder encodes the completion of long-horizon rearrangement tasks. The efficacy
language instruction and guides the output SE(2) action, of such language-based guidance is primarily attributed to the
consisting of paired pick and place end-effector poses. It utilization of a meticulously collected dataset containing di-
represents an early demonstration of language-conditioned verselanguageinstructions,whichsurpassespreviousdatasets
pick-and-place capabilities. by an order of magnitude in scale.
BC-Z [80] processes two types of task instructions: a Hiveformer [87] places significant emphasis on leveraging
language instruction or a human demonstration video. The multi-view scene observations and maintaining the full ob-
environment is presented to the model in the form of an servation history for a language-conditioned policy. This ap-
RGB image. Then the instruction embedding and the image proachrepresentsanadvancementoverprevioussystems,such
embeddingarecombinedthroughtheFiLMlayer,culminating as CLIPort and BC-Z, that only use the current observation.
inthegenerationofactions.Thisconditionalpolicyisasserted Notably, Hiveformer stands out as one of the early adopters
to exhibit zero-shot task generalization to unseen tasks. of Transformer architecture as its policy backbone.
MCIL [81] represents a pioneering robot policy that in- Gato [17] proposes a model that can play Atari games,
tegrates free-form natural language conditioning. This is in caption images, and stack blocks, all with a single set of
contrast to earlier approaches that typically rely on conditions modelparameters.Thisachievementisfacilitatedbyaunified
in the form of task IDs or goal images. MCIL introduces the tokenization scheme, harmonizing the input and output across
capability to leverage unlabeled and unstructured demonstra- diverse tasks and domains. Consequently, Gato enables the
tion data. This is achieved by training the policy to follow simultaneoustrainingofdifferenttasks.Astra[126]optimizes
either image or language goals, with a small fraction of the this architecture via trajectory attention.
trainingdatasetconsistingofpairedimageandlanguagegoals. RoboCat [93] proposes a self-improvement process de-
HULC [82] introduces several techniques aimed at enhanc- signed to enable an agent to rapidly adapt to new tasks
ing robot learning architectures. These include a hierarchical with as few as 100 demonstrations. This self-improvement
decomposition of robot learning, a multimodal Transformer, process iteratively finetunes the model and self-generates new
and discrete latent plans. The Transformer learns high-level data with the finetuned model. Built upon the Gato model,
behaviors, hierarchically dividing low-level local policies and RoboCat incorporates the VQ-GAN image encoder. During
the global plan. Additionally, HULC incorporates a visuo- training, RoboCat predicts not only the next action but also
lingual semantic alignment loss based on contrastive learning futureobservations.Theeffectivenessoftheself-improvement
toalignVLmodalities.HULC++[83]furtherintegratesaself- process is demonstrated through comprehensive experiments
supervisedaffordancemodel.ThismodelguidesHULCtothe conducted in both simulated and real-world environments
actionableregionspecifiedbyalanguageinstruction,enabling under multi-task, multi-embodiment settings.
it to fulfill tasks within this designated area. RT-1 [95], developed by the same team as BC-Z, shares
UniPi [84] treats the decision-making problem as a text- similarities with BC-Z but introduces some key distinctions.
conditioned video generation problem. To predict actions, Notably, RT-1 employs a vision encoder based on the more
UniPi generates a video based on a given text instruction, efficient EfficientNet, departing from BC-Z’s use of ResNet.

8
TableIII:VLAsthatserveaslow-levelcontrolpolicies.♢indicateslargeVLAs.Closelyrelated(non-VLAmodels)areincluded
in brackets. The remaining are generalized VLAs. BC: behavior cloning (cont/disc: continuous/discrete action). Xattn: cross-
attention. Concat: concatenation. Quant.: quantization. p/s: prompt/state vision encoder. [SC]: self-collect data.
Model Vision Language ActionDe- Architecture Training Training Environments,Embodiments,Tasks,and
Encoder Encoder/VLM coder/Head Objectives Datasets Skills
CLIPort[28] CLIP-ResNet50, CLIP-GPT LingUNet Hadamard BC(SE(2)) [SC] Sim:Ravens
Transporter-ResNet
MCIL[81] Custom-CNN USE RNN LMP MCIL Play-LMP,[SC] Sim:3DPlayroomenvironment
HULC[82],[83] MCILCNN Sentence-BERT RNN LMP MCIL CALVINdata Sim:CALVIN
Languagecosts[85] CLIP-ViT,UNet CLIP-GPT STORM Concat MLE(costmap) [SC] Sim&Real(Franka):pick,place
InteractiveLanguage ResNet CLIP-GPT TFM Xattn BC(cont) [SC:Language- Sim&Real(xArm6):rearrangement
[86] Table]
Hiveformer[87] UNet CLIP-GPT TFM,UNet Concat BC(cont) RLBenchdata Sim:RLBench
PerAct[88] 3DCNN CLIP-GPT PerceiverIO Concat 3Daffordance RLBenchdata, Sim:RLBench;Real(Franka):pick,place,
[SC] stack,opendrawer,sweep,insertpeg,etc.
Act3D[89] CLIP-ResNet50 CLIP-GPT TFM Xattn 3Daffordance RLBenchdata, Sim:RLBench;Real(Franka):reachtarget,
(voxel) [SC] wipe,stack,etc.
RVT[90], CLIP-ResNet50 CLIP-GPT TFM Concat 2Daffordance RLBenchdata, Sim:RLBench;Real(Franka):stack,press,
RVT-2[91] (projectto3D) [SC] place
RoboPoint[92] ViT-L/14 Vicuna-V1.5 Concat 2Daffordance [SC] Real(Franka):pick,place
13B (projectto3D)
Gato[17] ViT Sent.Piece TFM Concat BC(cont&disc) [SC] Sim&Real(Sawyer):RGB-stacking
(RoboCat)[93] VQ-GAN(p,s) TFM Quant. BC,observation Self- Sim&Real(Sawyer,Franka,KUKA):
prediction improvement stacking,building,lifting,insertion,removal
VIMA[94] ViT,MaskR-CNN T5 TFM Xattn BC(SE(2)) [SC:VIMA-Data] Sim(Ravens):VIMA-Bench
BC-Z[80] ResNet18(p,s) USE MLP FiLM BC(cont) [SC] Real(EDR):pick-place/wipe/drag,grasp,push
RT-1[95] EfficientNet USE TFM FiLM BC(disc) [SC:Fractal] Real(EDR):pick-place,move,knock
MOO[94] OWL-ViT(p), USE TFM FiLM BC(disc) [SC] Real(EDR):pick,movenear,knock,place
EfficientNet(s) upright,placeinto
Q-Transformer[96] EfficientNet USE TFM FiLM TDerror Fractal,Auto- Sim:pick;Real(EDR):pick,place,open/close
collect drawer,movenear
(RT-Trajectory)[97] EfficientNet TFM BC(disc) [SC] Real(EDR):pick,place,foldtowel,swivel
chair,etc.
(ACT)[98] ResNet18 CVAE-TFM BC(cont,action [SC]with Sim:transfercube,bimanualinsertion;Real
chunking) ALOHA (ViperX,WidowX):slotbattery,opencup,etc
RoboAgent/MT- CNN CVAE-TFM FiLM BC(cont,action RoboSet Real(Franka):pick,place,open/closedrawers,
ACT[99] chunking) pour,push,drag,etc.
RoboFlamingo[100] CLIP-ViT-L/14 LLaMA,MPT, LSTM, Xattn BC(cont) CALVINdata Sim:CALVIN
GPT-NeoX TFM
RoboUniView[101] UVFormer (ModeldesignfollowsRoboFlamingo) BC(cont) CALVINdata Sim:CALVIN
DeeR-VLA[102] (ModeldesignfollowsRoboFlamingo++) BC(cont) CALVINdata Sim:CALVIN
Instruct2Act[103] CLIP,SAM ChatGPT RobotAPIs Tool-Use Sim(Ravens):VIMA-Bench
VoxPoser[104] ViLD,MDETR, GPT-4 MPC Tool-Use Sim:Sapien;Real(Franka):move&avoid,set
OWL-ViT,SAM table,closedrawer,openbottle,sweeptrash
UniPi[84] Imagenvideo T5-XXL CNN Xattn Inversedynamics [SC:PF],Ravens, Sim:PaintingFactory(PF),Ravens
BridgeV1
(DiffusionPolicy) ResNet18 UNet,TFM DDPM [SC] Sim:Robomimic,FrankaKitchen,etc;Real
[105] (UR5,Franka):push-T,flipmug,poursauce
(DP3)[106] DP3Encoder (ModeldesignfollowsDiffusionPolicy) DDIM [SC] Sim:(72tasks);Real(Franka,Allegrohand):
roll-up,dumpling,drill,pour
SUDD[107] ResNet18 CLIP-GPT UNet,TFM Concat DDPM Lang-guided Sim:MuJoCo;Real(UR5e):pick,place
datageneration
Octo[108] CNN T5-base TFM Concat DDPM OXE Real:BridgeV2,CMUBaking,Stanford
Coffee,BerkeleyPegInsert,etc.
3DDiffuserActor (ModeldesignfollowsAct3D) DDPM RLBench, Sim:RLBench,CALVIN;Real(Franka):put,
[109] CALVIN,[SC] open,close,stack,etc.
MDT[110] CLIP-ViT-B/16(p), CLIP-GPT DiT Concat DDIM CALVIN, Sim:CALVIN,LIBERO;Real(Franka):pick,
Voltron/ResNet18(s) LIBERO,[SC] push,open,close,etc.
RDT-1B[111] SigLIP T5-XXL DiT Xattn DDPM (Aggregated Real(ALOHAdual-arm):wash,pour,fold,
Datasets) etc.
RT-2[1]♢ ViT-4B,ViT-22B PaLI-X,PaLM-E Symbol- Concat BC(disc),Co- Fractal,VQA Sim:Language-Table;Real:RT-1evaluation
tuning fine-tuning tasks
RT-H[112]♢ (ModeldesignfollowsRT-2) BC(disc) Diverse+Kitchen Real:Diverse+Kitchenevaltasks
RT-X[113]♢ (ModelsfromRT-1andRT-2) BC(disc) [SC:OXE] Real:BridgeV2,RT-1evaluationtasks,etc.
OpenVLA[34]♢ DINOv2,SigLIP Prismatic-7B Symbol- Concat BC(disc) OXE,DROID Real:BridgeV2,RT-1evaluationtasks,
tuning Franka-Tabletop,DROID,etc.
OpenVLA-OFT (ImprovesOpenVLAwithOFTrecipe) BC(cont,parallel LIBERO,[SC] Sim:LIBERO;Real(ALOHAsetup):fold,
[114]♢ decodew/chunk.) scoop,put
TraceVLA[115]♢ (ModeldesignfollowsOpenVLA,addingvisualtraceprompting) BC(disc) BridgeV2, Sim:SimplerEnv;Real(WidowX):pick,push,
Fractal,[SC] fold,swipe
π0[116]♢ SigLIP PaliGemma Action Concat Flowmatching OXE,[SC:π- Real(generalrobotcontrol):sweep,open,
expert cross-embod.] pack,etc.
RoboMamba[117] CLIP-ViT Mamba MLP Concat BC(cont) [SC] Sim:Sapien;Real(Franka):opendoor/box,
♢ staple
SpatialVLA[118]♢ SigLIP,Ego3D PaliGemma2 MLP Concat BC(Adaptive OXE,BridgeV2, Sim:SimplerEnv,LIBERO;Real(WidowX):
PositionEncoding ActionGrids) Fractal,RH20T pick,place,close,push
TinyVLA[119]♢ ViT Pythia Diffusion Concat DDPM OXE,[SC] Sim:MetaWorld;Real(Franka,UR5):place,
Policy stack,flipmug,closedrawer,openbox
CogACT[120]♢ DINOv2,SigLIP LLaMA2 DiT Concat DDIM OXE,[SC] Sim:SimplerEnv;Real(Realman,Franka):
pick,place,stack,open/closeoven
DexVLA[121]♢ ViT,ResNet-50 Qwen2-VL2B, ScaleDP Concat DDPM [SC] Real(Franka,UR5e,AgileX):pick,foldshirt,
DistilBERT, bustable,pour
HybridVLA[122]♢ DINOv2,SigLIP, LLaMA2,Phi-2 MLP Concat DDIM OXE,DROID Sim:RLBench;Real(Franka,AgileX):pick-
CLIP place,pour,opendrawer,fold,etc.
LAPA[123]♢ C-ViViT,VQ-GAN LWM-Chat-1M MLP Concat LAPA OXE,BridgeV2, Sim:Language-Table,SimplerEnv;Real
SomethingV2 (Franka):pick,coverwithtowel,knockover
WorldVLA[124]♢ VQ-GAN Chameleon TFM Quant. BC(disc,chunk.), LIBERO, Sim:LIBERO
worldmodel OpenVLAdata
UniVLA[125]♢ MoVQ Emu3 TFM Quant. BC(disc,chunk.), (Simbenchmark Sim:CALVIN,LIBERO,SimplerEnv
worldmodel data)

Action
Key,
Value Action
Decoder
Vision Language
Encoder Encoder
State Instr.
9
⊙
Action Action
Action Decoder Action
VLM Expert (VLM) VLM
(Standard Large VLA) Vision Language
Encoder Encoder (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. State Instr.
Action Action AStcattioen Action
Key,
Action Action DeVc.alueVisAiocnti Done c. Action Decoder
Decoder Decoder (System 1) VLM
Language Vision ( V VL i A s i + o W n o rld MLodaenl)guage VLM Encoder Encoder Vis. En E c. nc T o o d k e e r nizer En T c ok o e d n e iz r er (System 2) Robot
Instruction State State StatIenstr. InAscttri.on State Instr. State
(a) FiLM
Action Action State Action
Action Dec. De-Tokenizer Action Tool Action Decoder API (Transformer) VLM (VLA + World Model) LLM
Unified Vocabulary
Vision Language API Encoder Encoder Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
⊙
Action
Key,
Value Action
Decoder
Vision Language
Encoder Encoder
State Instr.
Action Action
Action Decoder Action
VLM Expert (VLM) VLM
(Standard Large VLA) Vision Language Encoder Encoder (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. State Instr.
(b) Cross-attention
Action Action State Action
Action Dec. Vision Dec. Action Action Decoder Decoder (System 1) VLM
(VLA + World Model)
Language Vision VLM Encoder Encoder Vis. Enc. Tokenizer Tokenizer (System 2)
Robot
Instruction State State Instr. Action State Instr. State
Action Action State Action
Action Dec. De-Tokenizer Action Tool Action Decoder API (Transformer) VLM (VLA + World Model)
LLM
Unified Vocabulary
Vision Language API
Encoder Encoder
Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
⊙
Action Action Action
Key,
Value Action Action Decoder Action
Decoder VLM Expert
(VLM) VLM
Vision Language (Standard Large VLA) Vision Language
Encoder Encoder Encoder Encoder (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. State Instr. State Instr.
Action Action State Action
Action Dec. Vision Dec. Action Action Decoder
Decoder (System 1) VLM
(VLA + World Model) Language Vision VLM
Encoder Encoder Vis. Enc. Tokenizer Tokenizer (System 2) Robot
Instruction State State Instr. Action State Instr. State
Action Action State Action
Action Dec. De-Tokenizer Action Tool Action Decoder
API (Transformer) VLM (VLA + World Model) LLM
Unified Vocabulary Vision Language API Encoder Encoder Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
(c) Concatenation
⊙
Action Action
Action Decoder Action
VLM Expert
(VLM) VLM
(Standard Large VLA) Vision Language
Encoder Encoder (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. State Instr.
Action Action State Action
Action Dec. Vision Dec. Action Action Decoder
Decoder (System 1) VLM
(VLA + World Model) Language Vision VLM
Encoder Encoder Vis. Enc. Tokenizer Tokenizer (System 2) Robot
Instruction State State Instr. Action State Instr. State
Action Action State Action
Action Dec. De-Tokenizer Action Tool Action Decoder
API (Transformer) VLM (VLA + World Model) LLM
Unified Vocabulary Vision Language API Encoder Encoder Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
(d) Tool Use
Action
Key,
Value Action
Decoder
Vision Language Encoder Encoder
State Instr.
⊙
Action Action Action
Key,
Value Action Action Decoder Action
Decoder VLM Expert (VLM) VLM
Vision Language (Standard Large VLA) Vision Language Encoder Encoder Encoder Encoder (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. State Instr. State Instr.
(e) Standard LVLA
Action Action State Action
Action Dec. Vision Dec.
Action Action Decoder
Decoder (System 1) VLM
(VLA + World Model) Language Vision VLM Encoder Encoder Vis. Enc. Tokenizer Tokenizer (System 2)
Robot
Instruction State State Instr. Action State Instr. State
Action Action State Action
Action Dec. De-Tokenizer Action Tool Action Decoder
API
(Transformer) VLM (VLA + World Model)
LLM
Unified Vocabulary
Vision Language API
Encoder Encoder
Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
⊙
Action
Key,
Value Action
Decoder
Vision Language
Encoder Encoder
State Instr.
Action Action
Action Decoder Action
VLM Expert (VLM) VLM
(Standard Large VLA) Vision Language Encoder Encoder (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. State Instr.
(f) Action Expert
Action Action State Action
Action Dec. Vision Dec.
Action Action Decoder
Decoder (System 1) VLM
(VLA + World Model) Language Vision VLM Encoder Encoder Vis. Enc. Tokenizer Tokenizer (System 2)
Robot
Instruction State State Instr. Action State Instr. State
Action Action State Action
Action Dec. De-Tokenizer Action Tool Action Decoder
API
(Transformer) VLM (VLA + World Model)
LLM
Unified Vocabulary
Vision Language API
Encoder Encoder
Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
⊙
Action AcAticotnion
Key,
Action Decoder Value AcAticotnio n
VLM DecEoxdpeerrt (VLM) VLM
(Standard Large VLA) VVisiisoino n LaLnagnugaugaeg e
EEncnocdoedrer EEncnocdoedrer (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. StSattaete InIsntsrt.r.
Action Action State Action
Action Dec. Vision Dec. Action Action Decoder
Decoder (System 1) VLM
(VLA + World Model) Language Vision VLM Encoder Encoder Vis. Enc. Tokenizer Tokenizer (System 2) Robot
Instruction State State Instr. Action State Instr. State
(g) Dual-System
Action Action State Action
Action Dec. De-Tokenizer Action Tool
Action Decoder
API (Transformer) VLM (VLA + World Model)
LLM
Unified Vocabulary Vision Language API Encoder Encoder Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
⊙
Action
Key,
Value Action
Decoder
Vision Language
Encoder Encoder
State Instr.
Action Action
Action Decoder Action
VLM Expert (VLM) VLM
(Standard Large VLA) Vision Language
Encoder Encoder (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. State Instr.
Action Action State Action
Action Dec. Vision Dec. Action Action Decoder
Decoder (System 1) VLM
(VLA + World Model) Language Vision VLM Encoder Encoder Vis. Enc. Tokenizer Tokenizer (System 2) Robot
Instruction State State Instr. Action State Instr. State
(h) VLA + World Model
Action Action State Action
Action Dec. De-Tokenizer Action Tool
Action Decoder
API (Transformer) VLM (VLA + World Model)
LLM
Unified Vocabulary Vision Language API Encoder Encoder Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
⊙
Action Action
Action Decoder Action
VLM Expert
(VLM) VLM
(Standard Large VLA) Vision Language
Encoder Encoder (Tokenizer) Vis. Enc. Tokenizer (Tokenizer)
State Instr. State Instr.
Action Action State Action
Action Dec. Vision Dec. Action Action Decoder
Decoder (System 1) VLM
(VLA + World Model) Language Vision VLM
Encoder Encoder Vis. Enc. Tokenizer Tokenizer (System 2) Robot
Instruction State State Instr. Action State Instr. State
Action Action State Action
Action Dec. De-Tokenizer Action Tool Action Decoder
API (Transformer) VLM (VLA + World Model)
LLM
Unified Vocabulary Vision Language API Encoder Encoder Quantizer Tokenizer Tokenizer Vision Tool
State Instr. State Instr. Action State Instruction
(i) Quantization
Figure5:RepresentativearchitecturesofVLAmodels.Somecorrespondtothe“Architecture”columninTableIII.⊙:Hadamard
product. ⊕: Concatenation.
However, RT-1 does not use video as a task instruction. and action tools, enabling LLMs to perform robotic tasks.
Additionally, RT-1 replaces the MLP action decoder in BC- 3) Control Policies for Multimodal Instructions: Multi-
Z with a Transformer decoder, producing discretized actions. modal instruction enables new ways to specify tasks, such
This modification enables RT-1 to attend to past images, as through demonstrations, by naming novel objects, or by
enhancing its performance compared to BC-Z. pointing with a finger or mouse click.
Q-Transformer [96] extends RT-1 by introducing autore- VIMA [128] places a significant emphasis on multimodal
gressive Q-functions. In contrast to RT-1, which learns expert prompts and the generalization capabilities of models. By
trajectories through imitation learning, Q-Transformer adopts incorporating multimodal prompts, more specific and intricate
Q-learning methods. Alongside the TD error objective of Q- taskscanbeformulatedcomparedtopuretextprompts.VIMA
learning, a conservative regularizer is incorporated to ensure introduces four main types of tasks: object manipulation,
that the maximum value action remains in-distribution. This visualgoalreaching,novelconceptgrounding,one-shotvideo
approachallowsQ-Transformertoleveragenotonlysuccessful imitation, visual constraint satisfaction, and visual reasoning.
demonstrations but also failed trajectories for learning. Thesetasksareoftenchallengingoreveninfeasibletoexpress
RT-Trajectory [97] adopts trajectory sketches as policy using only language prompts. VIMA-Bench has been devel-
conditions instead of relying on language conditions or goal opedtoevaluateacrossfourgeneralizabilitylevels:placement,
conditions. These trajectory sketches consist of curves that novel combinatorial, novel object, and novel task.
delineate the intended trajectory for the robot end-effector to MOO [94] extends RT-1 to handle multimodal prompts.
follow. They can be manually specified through a graphical Leveraging the backbone of RT-1, it incorporates OWL-ViT
user interface, extracted from human demonstration videos, to encode images within the prompt. By expanding the RT-1
or generated by foundation models. RT-Trajectory’s policy is dataset with new objects and additional prompt images, MOO
built upon the backbone of RT-1 and trained to control the enhances the generalization capabilities of RT-1. This exten-
robot arm to accurately follow the trajectory sketches. This sion also facilitates new methods of specifying target objects,
approach facilitates generalization to novel objects, tasks, and such as pointing with a finger and clicking on graphical user
skills, as trajectories from various tasks are transferable. interfaces.
ACT [98] builds a conditional VAE policy with action 4) Control Policies with 3D Vision: In our 3D world,
chunking,requiringthepolicytopredictasequenceofactions it is reasonable to assume that 3D vision provides richer
ratherthanasingleone.Duringinference,theactionsequence information than 2D images.
is averaged using a method called temporal ensembling. Point clouds are a common representation for 3D visual
RoboAgent [99] extends ACT via MT-ACT, demonstrating inputsduetotheirstraightforwardderivationfromRGB-Din-
that action chunking improves temporal consistency. It also puts,asdemonstratedbybothDP3[106]and3DDiffuserAc-
introducesaninpainting-basedsemanticaugmentationmethod. tor[109].Voxelshavelikewisebeenextensivelystudied.VER
RoboFlamingo [100] adapts the existing Flamingo VLM to [129] proposes voxelizing multi-view images into 3D cells
a robot policy by attaching an LSTM-based policy head. This in a coarse-to-fine manner, enhancing performance in vision-
demonstrates that pretrained VLMs can be effectively trans- languagenavigationtasks.PerAct[88]facilitatesefficienttask
ferred to language-conditioned robotic manipulation tasks. learning with only a few demonstrations by leveraging voxel
A recent trend in LLMs is equipping them with tool-use representations in both the observation and action spaces.
capabilitiesbygeneratingcodethatcallstoolsviaAPIs[127]. The input comprises voxel maps reconstructed from multi-
Instruct2Act[103]followsthisparadigmbyintegratingvision viewRGB-Dimages,whiletheoutputcorrespondstothebest

10
voxelforguidingthegripper’smovement.RoboUniView[101] 7) Control Policies for Motion Planning: Motion planning
improvesperformancebyinjecting3Dinformationfrommulti- involvesdecomposingmovementtasksintodiscretewaypoints
perspectiveimagesthroughanovelUVFormervisionencoder, while satisfying constraints such as obstacle avoidance and
which is pretrained on a 3D occupancy task. kinematic limits.
In contrast, Act3D [89] introduces a continuous resolution Language costs [85] presents a novel approach to robot
3Dfeaturefield,withadaptiveresolutionsbasedonthecurrent correction using natural language for human-in-the-loop robot
task, addressing the computational cost of voxelization. RVT, control systems. This method leverages predicted cost maps
RVT-2 [90], [91] propose re-rendering images from virtual generated from human instructions, which are then utilized
views of the scene point cloud and using these images as by the motion planner to compute the optimal action. This
inputs, rather than directly relying on 3D inputs. framework enables users to correct goals, specify preferences,
or recover from errors through intuitive language commands.
5) Diffusion-basedControlPolicies: Diffusion-basedaction
VoxPoser [104] employs LLM and VLM to create two 3D
generation leverages the success of diffusion models in the
voxel maps that represent affordance and constraint. It lever-
field of computer vision.
ages the programming capability of LLMs and the perception
Diffusion Policy [105] formulates a robot policy as a
capabilityofVLMs.LLMtranslateslanguageinstructionsinto
DDPM. This approach incorporates a variety of techniques,
executable code, invoking VLM to obtain object coordinates.
including receding horizon control, visual conditioning, and
Based on the composed affordance and constraint maps, Vox-
thetime-seriesdiffusionTransformer.Theeffectivenessofthis
Poser employs model predictive control to generate a feasible
diffusion-based visuomotor policy is underscored by its pro-
trajectory for the robot arm’s end-effector. Notably, VoxPoser
ficiency in multimodal action distributions, high-dimensional
doesnotrequireanytraining,asitdirectlyconnectsLLMand
action spaces, and training stability.
VLM for motion planning.
SUDD [107] presents a framework where an LLM guides
RoboTAP [131] breaks down demonstrations into stages
data generation, and subsequently, the filtered dataset is
marked by the opening and closing of the gripper. In each
distilled into a visuo-linguo-motor policy. This framework
stage, RoboTAP uses the TAPIR algorithm to detect active
achieves language-guided data generation by composing an
points that track the relevant object from the source to the
LLM with a suite of primitive robot utilities, such as grasp
target pose. The path can then be used by visual servoing
samplersandmotionplanners.ItthenextendsDiffusionPolicy
to control the robot. A motion plan is created by stringing
by incorporating language-based conditioning for multi-task
together these stages, enabling few-shot visual imitation.
learning and facilitates the distillation of the filtered dataset.
8) Control Policies with Point-based Action: Recent re-
Octo [108] introduces a Transformer-based diffusion policy
search has explored leveraging the capabilities of VLMs to
characterized by a modular open-framework design, allowing
select or predict point-based actions—a cost-effective alterna-
forflexibleconnectionsfromdifferenttaskdefinitionencoders,
tive to building full VLAs.
observation encoders, and action decoders to the Octo Trans-
PIVOT[132]castsroboticstasksasvisualquestionanswer-
former.BeingamongthefirsttoutilizetheOXEdataset[113],
ing,leveragingVLMstoselectthebestrobotactionfromaset
Octodemonstratespositivetransferandgeneralizabilityacross
ofvisualproposals.Visualproposalsareannotatedintheform
diverse robots and tasks.
of keypoints on images. The VLM is iteratively prompted to
MDT [110] adapts the newly introduced DiT model from
refine them until the best option is identified.
computer vision to the action prediction head. DiT, originally
RoboPoint [92] finetunes VLM using the task of spatial
proposed as a Transformer-based diffusion model, replaces
affordance prediction, which is to point at where to act on
the classical U-Net architecture for video generation. Coupled
the image. These affordance points on 2D images are subse-
with two auxiliary objectives—masked generative foresight
quently projected into 3D space using depth maps, forming
and contrastive latent alignment—MDT demonstrates better
the predicted robot action.
performance than the U-Net-based diffusion model, SUDD.
ReKep[35]isaconstraintfunctionthatmaps3Dkeypoints
RDT-1B [111] is a diffusion-based foundation model for in the scene to a numerical cost. Robotics manipulation
bimanual manipulation, also built on DiT. It addresses data tasks can be represented as a sequence of ReKep constraints,
scarcity by introducing a unified action format across vari- which are produced with large vision models and VLMs.
ous robots, enabling pretraining on heterogeneous multi-robot Consequently, robot actions can be obtained by solving the
datasets with over 6K trajectories. As a result, RDT scales up constrained optimization problem.
to1.2Bparametersanddemonstrateszero-shotgeneralization. 9) Large VLA: Large VLA is equivalent to the origi-
6) Diffusion-basedControlPolicieswith3DVision: Several nal VLA definition proposed by RT-2 [1], as illustrated in
works have proposed combining 3D Vision with diffusion- Figure 2a. This terminology is analogous to the distinction
based policies. DP3 [106] introduces 3D inputs to a diffu- betweenLLMsandgenerallanguagemodels,orbetweenlarge
sion policy, resulting in improved performance. Similarly, 3D VLMs and general VLMs.
Diffuser Actor [109] shares the core idea of DP3 but differs RT-2 [1] endeavors to harness the capabilities of large
in model architecture by combining Act3D with Diffusion multimodalmodelsinroboticstasks,drawinginspirationfrom
Policy.3D-MoE[130]exploresanefficientmixture-of-experts models like PaLI-X and PaLM-E (see the architecture in
architecture with DiT-based action diffusion using a rectified Fig. 5e). The approach introduces co-fine-tuning, aiming to
flow scheduler. fit the model to both Internet-scale visual question answering

11
(VQA) data and robot data. This training scheme enhances NORA-1.5[134]unifiesaVLAwithaworldmodelthrough
generalizability and brings about emergent capabilities. reward-guidedpost-training.GenieEnvisioner[135]isaworld
RT-H [112] introduces an action hierarchy that includes an foundation platform that integrates a world model and a VLA
intermediatepredictionlayeroflanguagemotions,situatedbe- within a single video-generative framework. See the general
tween language instructions and low-level actions (translation architecture in Fig. 5h.
and rotation). This additional layer facilitates improved data Visualautoregressivemodeling(VAR)[136]withquantized
sharing across different tasks. For example, both the language visual tokens demonstrates improved performance over diffu-
instructions “pick” and “pour” may involve the language sion models in image generation. This suggests that the three
motion “move the arm up”. Moreover, this action hierarchy modalities of VLAs can be unified under the autoregressive
enables users to specify corrections to recover from failures, paradigm[137].WorldVLA[124]andUniVLA[125]advance
which the model can then learn from. this direction by integrating VLAs with world models (see
RT-X[113]buildsuponthepreviousRT-1andRT-2models. the architecture in Fig. 5i). It quantizes multimodal data into
These models are retrained using the newly introduced open- discretetokens,formingasharedvocabularyofquantizedmul-
source large dataset, named Open X-Embodiment (OXE), timodal tokens. Consequently, all modalities can be modeled
which is orders of magnitude larger than previous datasets. autoregressively, enabling not only action and text generation
The resulting models, RT-1-X and RT-2-X, both outperform butalsoimagegeneration,therebyconstitutingaworldmodel.
their original versions.
OpenVLA [34] was later developed as an open-source Strengths and Limitations.
counterpart to RT-2-X. They additionally explored efficient a) Architectures: Representative VLA architectures are
fine-tuning methods, including LoRA and model quanti- illustrated in Figure 5. FiLM is used in RT-1, and thus
zation. OpenVLA-OFT [114] applies an Optimized Fine- its follow-up models inherit this mechanism. While cross-
Tuning(OFT)recipeforimprovedefficiencyandperformance. attention may offer superior performance with smaller model
TraceVLA [115] finetunes OpenVLA to enable visual trace sizes, concatenation is simpler to implement and can achieve
prompting, enhancing spatial-temporal awareness. comparable results with larger models [128]. Quantization
π [116] proposes a flow-matching architecture for trans- unifies multimodal tokens into a shared vocabulary, thus
0
forming VLMs into VLAs. By incorporating an additional enablingintegrationwithworldmodels.Thetool-useparadigm
action expert based on the mixture-of-experts framework (see of LLMs can also be applied to robotic tasks.
the architecture in Fig. 5f), it effectively inherits the Internet- b) Action types and their training objectives: Most low-
scale knowledge in the VLM while extending its capabilities level control policies predict actions for the end-effector pose
to address robotic tasks. while abstracting away the motion planning module that
RoboMamba [117] replaces the costly Transformer with a produces more fine-grained motions. While this abstraction
Mambastatespacemodelthathaslinearinferencecomplexity, facilitates better generalization to different embodiments, it
achieving efficient robotic reasoning and action capabilities. also imposes limitations on dexterity.
SpatialVLA [118] introduces Ego3D Position Encoding for The behavior cloning (BC) objective is used in imitation-
injecting3DinformationandrepresentsactionswithAdaptive learning,withdifferentvariantsfordifferentactiontypes.The
Action Grids for enhanced generalizability and robustness. BC objective for continuous action can be written as:
LAPA [123] devises the first unsupervised pretraining (cid:88)
L = MSE(a ,aˆ ), (4)
method for VLAs based on latent actions [67]. This approach Cont t t
t
employs a three-stage process to learn from internet-scale
where MSE(·) stands for mean squared error. a is the action
unlabeledvideos.First,aVQ-VAEframeworkispretrainedto t
annotation from expert demonstrations.
extract quantized latent actions between image frames. Next,
Discrete action is achieved by dividing the action value
a VLA model is pretrained to predict these latent actions.
range into a fixed number of bins. Its BC objective is:
Finally, the model is finetuned using only a small robotic
dataset to map the latent actions to actual robot actions. (cid:88)
L = CE(a ,aˆ ), (5)
Disc t t
The integration of large VLAs with diffusion has also been
t
gaining popularity. TinyVLA [119] leverages the Diffusion
where CE(·) stands for cross-entropy loss.
Policy, while CogACT [120] utilizes a DiT action diffusion
The BC objective of SE(2) action is:
module. DexVLA [121] proposes embodied curriculum learn-
ing to progressively train a diffusion action expert, incorpo- L =CE(a ,aˆ )+CE(a ,aˆ ). (6)
SE(2) pick pick place place
ratingsub-stepreasoningfordecomposinglong-horizontasks.
HybridVLA [122] integrates diffusion with the autoregression The DDPM objective in diffusion-based control policies is:
paradigm to fully leverage VLMs’ reasoning capabilities. L =MSE (cid:0) εk,ε (a +εk,k) (cid:1) , (7)
GR00T N1 [133] introduces a dual-system architecture to DDPM θ t
build a robot foundation model for humanoid robots (see the where εk is a random noise for iteration k; ε is the noise
θ
architecture in Fig. 5g). Its VLM-based System 2 processes prediction network, i.e., the VLA model.
image observations and language instructions at 10 Hz, while While discrete action has demonstrated superior perfor-
System 1 is a diffusion module that generates closed-loop mance in RT-1 [95], Octo [108] argues that it leads to early
motor actions in real time (120 Hz). grasping issues. SE(2) actions require the model to predict

12
Table IV: High-level task planners.
Model Vision LanguageModel/ Low-levelControl Architecture Require Environments,Embodiments,Tasks,and
Model VLM Policy Training Skills
PaLM-E[10] ViT,OSRT PaLM InteractiveLanguage, Concat ✓ Sim:TAMP;Sim&Real-Mani:Language-
RT-1 Table;Real:SayCansetup
EmbodiedGPT[138] EVAViT-G/14 LLaMA-7B MLP Xattn ✓ Sim-Mani:FrankaKitchen,Meta-World
LEO[139] ConvNeXt,PointNet++ Vicuna-7B MLP Concat ✓ Sim-Mani:CLIPorttasksubset;Sim-Navi:
Habitat-web
3D-LLM[41] CLIP,3D-CLR, Flamingo,BLIP-2 DD-PPO Concat ✓ Sim-Navi:Habitat
ConceptFusion
ShapeLLM[140] ReCon++ LLaMA Concat ✓ 3DMM-VetBenchmark
SayCan[9] PaLM,FLAN BC-Z,MT-Opt ✗ Real-Navi&Mani(EDR):officekitchen
Translated⟨LM⟩[141] GPT-3,Codex ✗ Sim:VirtualHome
(SL)3[142] T5-small seq2seq ✓ Sim-Navi:ALFRED
InnerMonologue[8] MDETR,CLIP InstructGPT,PaLM CLIPort,heuristics, Language ✗ Sim&Real-Mani:TabletopRearrangement;
SayCanpolicies Real-Navi&Mani:KitchenMobileMani.
LLM-Planner[143] HLSMobjectdetector GPT-3 HLSM Language ✓ Sim-Navi:ALFRED
LID[144] CNN GPT-2 Lang.,Embed ✓ Sim:VirtualHome
SMs[145] CLIP,ViLD GPT-3,RoBERTa CLIPort Lang.,Code ✗ Sim-Mani:pick,place
ProgPrompt[146] ViLD GPT-3 API Code ✗ Sim:VirtualHome
ChatGPTforRobotics YOLOv8 ChatGPT API Code ✗ Real-Navi:droneflight;Sim-Navi:AirSim,
[147] Habitat
CaP[148] ViLD,MDETR GPT-3,Codex API Code ✗ Sim-Mani&Sim-Navi:pick,place,etc.
DEPS[149] CLIP ChatGPT MC-Controller,Steve-1 Code ✗ Sim:Minecraft
ConceptGraphs[150] SAM,CLIP,LLaVA GPT-4 API Code(JSON) ✗ Sim:AI2-THOR;Real(SpotArm):pick-place
only the pick and place end-effector poses, which is sufficient IV. TASKPLANNERS
formanytabletopmanipulationtasks.However,morecomplex A high-level task planner π aims to divide a complex task
ϕ
tasks—such as “pouring water into a cup”—may require ℓ into a sequence of subtasks p (i.e., task plan), each serving
i
additional DoFs, thereby necessitating SE(3) actions [35]. as an instruction to low-level control policies π :
θ
Although point-based actions can be coarse-grained, they are
[p ,p ,...,p ]∼π (ℓ,s ). (8)
more easily obtained from VLMs in a zero-shot manner. 1 2 N ϕ t
This process is sometimes referred to as task or subgoal
c) RT series: RT-1 [95] inspired a series of “Robotic decomposition and is closely related to task and motion plan-
Transformer” models. The Transformer backbone surpasses ning(TAMP)andembodieddecisionmaking.Whenequipped
previous RNN backbones by harnessing the higher capacity with task planners, VLAs can complete more complex, long-
of Transformers to absorb larger robot datasets. Preceding horizon tasks, as illustrated in Figure 4. Details are summa-
RT-1 was BC-Z, which solely utilized MLP layers for action rized in Table IV. Ideally, task plans should also incorporate
prediction. Subsequent to RT-1, several works emerged, each optimal scheduling for these subtasks.
introducing new capabilities. MOO adapted RT-1 to accom-
modate multimodal prompts. RT-Trajectory enabled RT-1 to A. Monolithic Task Planners
processtrajectorysketchesasprompts.Q-Transformerutilized A single LLM or multimodal LLM (MLLM) can typically
Q-learning to train RT-1. RT-2, based on ViT and LLM, generate task plans by employing a tailored framework or
introduced a completely different architecture from RT-1. RT- through finetuning on embodied datasets. We refer to these
X retrained RT-1 and RT-2 with a significantly larger dataset, as monolithic models.
resulting in improved performance. Based on RT-2, RT-H 1) End-to-endTaskPlanners: SimilartoLVLAs,taskplan-
[112] introduces action hierarchies for better data sharing. ners can be implemented as end-to-end multimodal LLMs,
leveraging their Internet-scale knowledge for task planning.
d) LVLA vs generalized VLA: While LVLAs can greatly PaLM-E [10] integrates ViT and PaLM to create a large
enhanceinstruction-followingabilitiesbecausetheycanbetter embodied multimodal language model capable of performing
parse user intentions, concerns arise regarding their train- high-level embodied reasoning tasks. Based on perceived im-
ing cost and deployment speed. Slow inference speed, in ages and high-level language instructions, PaLM-E generates
particular, can significantly impact performance in dynamic a text plan that serves as instructions for low-level robotic
environments,aschangesintheenvironmentmayoccurduring policies. In a mobile manipulation environment, they map
inference. Therefore, several methods have been proposed to the generated plan to executable low-level instructions with
improveefficiency.TinyVLA[119]focusedoninferencespeed SayCan [9]. As the low-level policy executes actions, PaLM-
anddataefficiencythroughasmallerVLManddiffusionhead E can also replan based on changes in the environment. With
for robot action. DeeR-VLA [102] proposes only partially PaLMasitsbackbone,PaLM-Ecanhandlebothnormalvisual
activating the model with dynamic inference with early-exit. question answering (VQA) tasks, along with the additional
embodied VQA tasks.
e) Scaling Law: Similar to LLMs, scaling laws have EmbodiedGPT [138] introduces the embodied-former,
also been observed in robotics [151], [152], revealing the which outputs task-relevant instance-level features. This is
importance of model size, dataset size, and the diversity achieved by incorporating information from vision encoder
of environments and objects. Further research in this area embeddings and embodied planning information provided by
can guide the development of VLAs with robust in-the-wild LLM. The instance feature serves to inform the low-level
generalization capabilities. policy about the immediate next action to take.

Task: Clean the room
Object
Objects: Toy car, camera...
Detector
Next steps?
LLM
1. Pick up the toy car Control
2. Move to the coffee table Policy
... ...
13
2) End-to-end Task Planners with 3D Vision: Some task
planners also explore the use of 3D vision. Because the Task: Clean the room Task: Clean the room
Object
majorityofcurrentMLLMsdealwithimagesasvisualinputs, Objects: Toy car, camera... Detector APIs: detect_objects(), pick_up()...
Next steps?
they require architectural changes to incorporate 3D visual LLM
inputs, and therefore, they are usually end-to-end models. LLM Object
objects =detect_objects() Detector
LEO [139] uses a two-stage training strategy to integrate a 1. Pick up the toy car Control for obj in objects:
point cloud encoder with an LLM: the first stage focuses on 2. Move to t . h .. e . . c . offee table Policy . p . i . c . k . _ . up(obj) C P o o n l t ic r y ol
3D vision-language alignment, followed by the second stage,
(a) Language-based (b) Code-based
which involves 3D vision-language-action instruction tuning.
LEO performs well not only in 3D question-answering tasks Figure6:DifferentapproachestoconnectLLMtomulti-modal
but also in manipulation, navigation, and task planning. modules in modular task planners.
Task: Clean the room
3D-LLM [41] injects 3D information into LLMs and em- APIs: detect_objects(), pick_up()...
B. Modular Task Planners
powers them to perform 3D tasks, such as 3D-assisted dialog
LLM
and navigation, using features from point cloud, gradSLAM, Finetuning end-to-end models on embodied data can be
Object
andneuralvoxelfield.MultiPLY[153]isanobject-centricem- exobpjeecntss i=vdee,tecatn_odbjesctosm()e aDpetpecrtooraches adopt a modular design by
bodiedLLMthatincorporatesevenmoremodalities,including asfsore mobjb ilni nobgjeoctfsf:-the-shelCfonLtrLol Ms and VLMs into task planners.
audio, tactile, and thermal. T h e s. p e. i . c . k a. _ p. up p (o r b o j) achescanaPlsoloicybeviewedasfollowingthetool-use
architecture [127].
ShapeLLM [140] is built on the novel 3D vision en-
1) Language-based Task Planners: Language-based ap-
coder ReCon++, which distills knowledge from multi-view
proaches use natural language descriptions as the medium for
image and text teachers, along with a point cloud MAE.
exchanging multimodal information, as shown in Figure 6a.
By integrating ReCon++ with LLaMA, ShapeLLM improves
Inner Monologue [8] sits between high-level command and
embodiedinteractionperformanceontheirnewlyproposed3D
low-level policy to enable closed-loop control planning. It
benchmark, 3D MM-Vet.
employs LLM to generate language instructions for low-level
3) Grounded Task Planners: Grounded task planning in-
policies and dynamically updates these instructions based
volvesgeneratinghigh-levelactionswhileconsideringwhether
on feedback received from them. The feedback encompasses
they can be executed by low-level control policies.
various sources: success feedback, object and scene feedback,
SayCan [9] is a framework designed to integrate high-
andhumanfeedback.Asthefeedbackiscommunicatedtothe
level LLM planners with low-level control policies. In this
LLM in textual format, no additional training is required for
framework, the LLM planner accepts users’ high-level in-
the LLM. A similar approach is used in ReAct [74].
struction and “says” what the most probable next low-level
LLM-Planner [143] introduces a novel approach to con-
skillis,aconceptreferredtoastask-grounding.Thelow-level
structingahierarchicalpolicycomprisingahigh-levelplanner
policy provides the value function as the affordance function,
and a low-level planner. The high-level planner harnesses the
determining the possibility that the policy “can” complete the
capabilities of LLM to generate natural language plans, while
skill, known as world-grounding. By considering both LLM’s
the low-level planner translates each subgoal within the plan
plan and affordance, the framework selects the optimal skill
intoprimitiveactions.Whilesharingsimilaritieswithprevious
for the current state.
methodsinitsoverallarchitecture,LLM-Plannerdistinguishes
Translated⟨LM⟩[141]employsatwo-stepprocesstotrans- itself by incorporating a re-planning mechanism, aiding the
late high-level instructions into executable actions. Initially, a robot to “get unstuck”.
pretrainedcausalLLMisutilizedforplangeneration,breaking LID [144] introduces a novel data collection procedure
down the high-level instruction into the next action expressed termed Active Data Gathering (ADG). A key aspect of ADG
in free-form language phrases. Then, as these phrases may is hindsight relabeling, which reassigns labels to unsuccessful
not directly map to VirtualHome actions, a pretrained masked trajectories, effectively maximizing the utilization of data
LLM is then employed for action translation. This step in- irrespective of their success. By converting all environmental
volves calculating the similarity between the generated action inputs into textual descriptions, their language-model-based
phrases and the VirtualHome action. The translated action is policy demonstrates enhanced combinatorial generalization.
appended to the plan, and the updated plan is read by the Socratic Models (SMs) [145] present a unique framework
LLMtogeneratethenextactionphrase.Thetwo-stepprocess wherein diverse pretrained models are effectively composed
isrepeateduntilacompleteplanisformed.A“Re-prompting” without the need for finetuning. The framework is based on
strategy[154]isfurtherproposedtogeneratecorrectiveactions the key component, named multimodal-informed prompting,
when the agent encounters precondition errors. facilitating information exchange among models with varied
(SL)3 [142] is a learning algorithm that alternates between multimodal capabilities. The idea is to utilize multimodal
three steps: segmentation, labeling, and parameter update. In models to convert non-language inputs into language de-
the segmentation step, high-level subtasks are aligned with scriptions, effectively unifying different modalities within the
low-level actions, subtask descriptions are then inferred in language space. Beyond excelling in conventional multimodal
the labeling step, and finally, the network parameters are up- tasks, SMs showcase their versatility in robot perception and
dated. This approach enables a hierarchical policy to discover planning.Inadditiontonaturallanguageplans,taskplanscan
reusable skills with sparse natural language annotations. also be represented in the form of pseudocode.

14
2) Code-based Task Planners: Code-based task planners Table V: Embodied Datasets. Per RT-X, skills correspond
leverage the coding ability of LLMs to generate task plans in to verbs, and tasks are different combinations of verbs and
the form of a program. Object detectors, VLMs, and control objects. ∗ Dataset collected in simulation rather than the real
policies can be invoked via APIs, as shown in Figure 6b. world. Some datasets are continually updated, and we include
ProgPrompt [146] introduces a novel task-planning ap- only the original version. Table adapted from [156], [157].
proach by prompting LLMs with program-like specifications Dataset Skills TasksScenesEpisodes Collection Obs. Instruction Robots
MIME[158] 12 20 1 8.3K Humanteleop. RGBD Demo Baxter
detailing available actions and objects. This enables LLMs to ∗RoboTurk[159] 2 1 2.1K Humanteleop. RGB Sawyer
generate high-level plans for household tasks in a few-shot RoboNet[160] 10 162K Script RGB Goalimage (7robots)
MT-Opt[161] 2 12 1 800K Script RGB Lang (7robots)
manner. Environmental feedback can be incorporated through BC-Z[80] 3 100 1 25.9K Humanteleop. RGB Lang,demo EDR
Fractal[95] 12 700+ 2 130K Humanteleop. RGB Lang EDR
assertions within the program. MOO[94] 5 59.1K Humanteleop. RGB Multimodal EDR
∗VIMA[128] 17 1 650K Script RGB Multimodal UR5
ChatGPT for Robotics [147] takes advantage of the pro- RoboSet[162] 12 38 11 98.5K Human,script RGBD Lang Franka
BridgeV2[163] 13 24 60.1K Human,script RGBD Lang WidowX
gramming ability of ChatGPT to facilitate “user on the loop” RH20T[156] 42 147 7 110K+ Humanteleop. RGBD Lang (4robots)
DROID[157] 86 564 76K Humanteleop. RGBD Lang Franka
control, a departure from the conventional “engineer in the OXE[113] 527 160K 311 1M+ Aggregatedata RGBD Lang (22robots)
loop” methodology. The procedure includes several steps:
concern. In contrast, modular task planners are more readily
firstly, a list of APIs is defined, such as an object-detection
deployable because they leverage off-the-shelf LLMs and
API, a grasp API, a move API; secondly, a prompt is then
VLMs. Language-based task planners offer the advantage
constructed for ChatGPT, specifying the environment, API
of seamless integration of LLMs and VLMs, as they are
functionality, task goal, etc.; thirdly, iteratively prompting
designed to operate in the natural language space. However,
ChatGPTtowritecodewiththedefinedAPIsthatcanexecute
theyoften requireextrasteps toalignthegenerated taskplans
the task, provided the access to simulation and user feedback
with language instructions that are admissible to low-level
forevaluatingthecodequalityandsafety;finally,executingthe
control policies. Conversely, while code-based task planners
ChatGPT generated code. In this procedure, ChatGPT serves
may require manually wrapping VLMs and control policies
asahigh-leveltaskplanner,andactionsaregeneratedthrough
in APIs and preparing clear documentation in advance, they
function calls to corresponding low-level APIs.
enable code debugging and provide greater controllability.
Code as policies (CaP) [148] also leverages the code-
Nevertheless, their performance can be constrained by the
writing capability of LLMs. It employs GPT-3 or Codex
programming capabilities of existing models.
to generate policy code, which, in turn, invokes perception
modulesandcontrolAPIs.CaPexhibitsproficiencyinspatial-
geometric reasoning, generalization to new instructions, and V. DATASETSANDBENCHMARKS
parameterization for low-level control primitives. By lever- A. Real-world Robot Datasets & Benchmarks
aging the multimodal capabilities of GPT-4V, COME-robot
Embodied AI faces significant data scarcity issues because
[155]eliminatestheneedforperceptionAPIsinCaP.Thisalso
real-world robot data is not as readily available as language
opens up possibilities for open-ended reasoning and adaptive
data. Collecting real-world robot datasets poses multiple chal-
planningwithinaclosed-loopframework,enablingcapabilities
lenges. Firstly, it is impeded by the cost and time required
such as failure recovery and free-form instruction following.
toprocureroboticequipment,setupenvironments,andgather
DEPS [149] stands for “Describe, Explain, Plan, and Se-
expertdatathroughdedicatedpoliciesorhumanteleoperation.
lect”. This approach employs an LLM to generate plans and
Secondly,thediversetypesandconfigurationsofrobotsintro-
explainfailuresbasedonfeedbackdescriptionscollectedfrom
duce inconsistencies in sensory data, control modes, gripper
the environment—a process referred to as “self-explanation”,
types, etc. Lastly, accurately capturing object 6D poses and
aiding in re-planning. Additionally, DEPS introduces a train-
reproducing setups remains elusive. We summarize recent
able goal selector to choose among parallel candidate sub-
robot datasets in Table V. In addition, real-world benchmarks
goals based on how easily they can be achieved, a crucial
are further complicated by the need for human evaluation.
aspect often overlooked by other high-level task planners.
ConceptGraphs [150] introduces a method to convert ob-
B. Simulators, Simulated Robot Datasets & Benchmarks
servation sequences into open-vocabulary 3D scene graphs.
Objects are extracted from RGB images using 2D segmenta- Many researchers resort to simulated environments to cir-
tion models, and VLMs are employed to caption objects and cumvent real-world obstacles and scale the data collection
establish inter-object relations, resulting in the formation of process. We compare simulators and simulated benchmarks
the 3D scene graph. This graph can then be translated into in Table VI. Nevertheless, this strategy presents its own
a text description (JSON), offering rich semantic and spatial challenges, chief among which is the sim-to-real gap. This
relationships between entities to LLMs for task planning. discrepancy arises when models trained on simulated data
exhibit poor performance during real-world deployment. The
Strengths and Limitations. causes of this gap are multifaceted, encompassing unrealistic
Monolithictaskplannersthatutilizegroundedtaskplanning rendering quality, inaccuracies in physics simulations, and
focusongeneratingexecutableplans.End-to-endmodelsshare domain shifts characterized by object properties and robot
an architecture similar to most LVLAs and can be finetuned motion planners. For instance, simulating non-rigid objects
on specialized embodied data to achieve better performance. such as deformable objects or liquids presents significant
However, the training costs of such large models can be a difficulties. Moreover, importing new objects into simulators

15
Table VI: Simulators and simulated benchmarks. Control: continuous control tasks. D, S, A, N: depth, segmentation, audio,
normal. Force: simulated contact force between end-effector and item. PD: pre-defined. Table adapted from [164], [165].
Name Scenes Objects UI Physics Task Observation Action Agent Description Related
/Rooms /Cat Engine
Gibson[166] 572/- Pybullet Navi RGB,D,N,S Navionly
iGibson[165],[167], 15/108 152/5 Mouse, Pybullet Navi,Mani RGB,D,S,N, Force TurtleBotv2, VR,ContinuousExtendedStates. Benchmarks:BEHAVIOR-100
[168] VR Flow,LiDAR LoCoBot,etc. Versions:0.5,1.0,2.0 [164],BEHAVIOR-1K[169]
SAPIEN[170] 2346/- Code PhysX Navi,Mani RGB,D,S Force Franka Articulation,RayTracing VoxPoser.Benchmark:SIMPLER
[171]
AI2-THOR[172] -/120 118/118 Mouse Unity Navi,Mani RGB,D,S,A Force,PD ManipulaTHOR, ObjectStates,TaskPlanning. Benchmarks:ALFRED,RoPOR
LoCoBot,etc. Versions:[173],[174] [175]
VirtualHome[176] 7/- -/509 Lang Unity Navi,Mani RGB,D,S Force,PD Human ObjectStates,TaskPlanning LID,Translated〈LM〉,ProgPrompt
TDW[177] 15/120 112/50 VR Unity, Navi,Mani RGB,D,S,A Force Fetch,Sawyer, Audio,Fluids
Flex Baxter
RLBench[178] 1/- 28/28 Code Bullet Mani RGB,D,S Force Franka TieredTaskDifficulty Hiveformer,PerAct
Meta-World[179] 1/- 80/7 Code MuJoCo Mani Pose Force Sawyer Meta-RL R3M,VC-1,Vi-PRoM,
EmbodiedGPT
CALVIN[180] 4/- 7/5 Pybullet Mani RGB,D Force Franka Long-horizonLang-condtasks GR-1,HULC,RoboFlamingo
FrankaKitchen[181] 1/- 10/6 VR MuJoCo Mani Pose Force Franka ExtendedbyR3MwithRGB R3M,Voltron,Vi-PRoM,
DiffusionPolicy,EmbodiedGPT
Habitat[182],[183] (Matterport+Gibson) Mouse Bullet Navi RGB,D,S,A Force Fetch,Franka, Fast,Navionly.Versions:1.0, VC-1,PACT;Benchmark:
AlienGO 2.0,Rearrangement[184] OVMM[185]
ALFRED[186] -/120 84/84 Unity Navi,Mani RGB,D,S PD Human Diverselong-horizontasks (SL)3,LLM-Planner
DMC[187] 1/- 4/4 Code MuJoCo Control RGB,D Force ContinuousRL VC-1,SMART
OpenAIGym[188] 1/- 4/4 Code MuJoCo Control RGB Force SingleagentRLenvironments
Genesis[189] (Rigid, deformable, Code (Propri- Navi,Mani RGB,D,S,N Force Franka,Unitree, High-speedcomprehensive
liquid,etc.) etary) etc. physicssimulation
requires considerable effort, often involving techniques such E. Task Planning Benchmarks
as 3D scanning and mesh editing. Despite these hurdles,
EgoPlan-Bench [196] focuses on benchmarking real-world
simulated environments provide automated evaluation metrics
taskplanningwithhumanannotations.PlanBench[197],[198]
that aid researchers in consistently evaluating robotic models.
comprehensively assesses various aspects of task planning
Many benchmarks are based on simulators because they can
ability, such as cost optimality, plan verification, and replan-
precisely reproduce the experimental setup and yield fair
ning. LoTa-Bench [199] directly evaluates task planning by
comparisons of different models. Another technique, known
executing the generated plans in simulators and calculating
asreal-to-sim,canimprovesimulationfidelity,recreatefailure
success rates. Embodied Agent Interface (EAI) [200] argues
cases, or facilitate digital twins.
that this approach fails to pinpoint issues in LLMs. By for-
malizingtheinput-outputofLLM-basedmodulesfordecision-
C. Automated Dataset Collection making tasks, EAI enables more fine-grained metrics beyond
Several approaches advocate for automated dataset col- success rates.
lection. RoboGen [190] employs a generative simulation
paradigm that proposes interesting skills, simulates corre-
F. Embodied Question Answering Benchmarks
sponding environments, and selects optimal learning ap-
Embodied question answering (EQA) benchmarks, as sum-
proaches to train policies for acquiring those skills. AutoRT
marized in Table VII, do not directly evaluate robotic tasks
[191] functions as a robot orchestrator driven by LLMs, gen-
like manipulation and navigation, but they are aimed at other
erating tasks, filtering them by affordance, and utilizing either
relevant abilities for embodied AI, such as spatial reasoning,
autonomous policies or human teleoperators to collect and
physics understanding, as well as world knowledge. EQA is
evaluate data. DIAL [192] focuses on augmenting language
akin to previous visual question answering benchmarks, but
instructions in existing datasets using VLMs. RoboPoint [92]
differs in that the agent can actively explore the environment
generates scenes procedurally with randomized 3D layouts,
before providing an answer. EmbodiedQA [201] and IQUAD
objects, and camera viewpoints.
[202] were among the first works to introduce this type of
benchmark. MT-EQA [203] focuses on complex questions in-
D. Human Datasets
volving multiple targets. MP3D-EQA [204] converts previous
Analternativestrategytoaddressdatascarcityinreal-world
RGBinputstopointclouds,testing3Dperceptioncapabilities.
settings is to leverage human data. Human behavior offers
Active exploration requires access to a simulator, limiting
plentifulguidanceforrobotpoliciesduetoitsdexterityanddi-
the types of data that can be used, such as real-world videos.
versity [193]. However, this strategy also comes with inherent
EgoVQA [205] shifts the focus of VQA to egocentric videos.
drawbacks. Capturing and transferring human hand/body mo-
EgoTaskQA[206]emphasizesspatial,temporal,andcausalre-
tions to robot embodiments is inherently difficult. Moreover,
lationship reasoning. EQA-MX [207] investigates multimodal
the inconsistency in human data poses a hurdle, as some data
expressions (MX), including regular verbal utterances and
maybeegocentricwhileothersarecapturedfromthird-person
nonverbal gestures like eye gaze and pointing. OpenEQA
perspectives. Additionally, filtering human data to extract
[208] evaluates seven main categories, including functional
useful information can be labor-intensive. These obstacles
reasoning and world knowledge.
underscore the complexities involved in incorporating human
data into robot learning processes. UMI [194] proposes a
method to mitigate these issues using hand-held grippers. For
VI. CHALLENGESANDFUTUREDIRECTIONS
amorecomprehensivecomparisonofhumandatasets,werefer a) Safetyfirst: Safetyisparamountinrobotics,asrobots
interested readers to [195]. interact directly with the physical world. Ensuring the safety

16
Table VII: Embodied question answering benchmarks. Explore: active exploration.
Benchmark QAPairs Scenes Source AnswerType Collection Explore Metrics
EQA[201] 5K 750envs House3Dsimulator Answerset(172answers) Template ✓ Accuracy
IQUAD[202] 75K 30rooms AI2-THOR Multiplechoice Template ✓ Accuracy
MT-EQA[203] 19.3K 588envs House3Dsimulator Binaryanswer Template ✓ Accuracy
MP3D-EQA[204] 1,136 83envs MatterPort3D Answerset(53answers) Template ✓ Accuracy
EgoVQA[205] 600 16videos IUMulti-view Multiplechoice(1outof5) Humanannotators ✗ Accuracy
EgoTaskQA[206] 40K 2Kvideos LEMMAdataset Openanswer,binaryverification Humanannotators&template ✗ Accuracy
EQA-MX[207] 8.2M 750Kimages CAESARsimulator Answerset Questiontemplates,answerset ✗ Accuracy
OpenEQA[208] 557+1079 180envs HM3D+ScanNet Openanswer Humanannotators ✗ LLMScore
of robotic systems requires the integration of real-world com- redundant and may hinder scalability. Additionally, although
monsense. This involves the incorporation of robust safety modular task planners typically do not require training, they
guardrails, risk assessment frameworks, and human-robot in- are not plug-and-play: language-based models may generate
teraction protocols. RLHF and“evaluation without execution” subtasks that control policies cannot execute, whereas code-
can also significantly lower safety risks [19]. Interpretability based models require modules to be pre-wrapped in APIs
andexpandability ofVLAdecision-making processes arealso manually. Therefore, developing a unified framework that
crucial for enhancing robot safety through error diagnosis and directly translates long-horizon tasks into low-level control
troubleshooting. signals in an end-to-end fashion is worth exploring.
b) Datasets & Benchmarks: In addition to the issues f) Real-Time Responsiveness: Unlike conversational AI,
discussed in §V, comprehensive benchmarks that cover a many robotic applications require real-time decision-making
wide range of skills, objects, embodiments, and environments to respond to dynamic environments. If inference time can-
remaintobedeveloped.Moreover,metricsbeyondthesuccess not keep pace with environmental changes, the model may
rate are needed for a fine-grained diagnosis of issues in VLA generate obsolete actions repeatedly. However, current VLA
models, as highlighted by EAI [200] for LLMs. models—especially LVLAs and task planners—face a trade-
c) Foundation Models & Generalization: VLA founda- off between speed and capacity. Novel mechanisms are thus
tionmodelsorroboticfoundationmodels(RFM)forembodied needed to strike an optimal balance.
AIremainanopenresearchtopicprimarilyduetothediversity g) Multi-agent Systems: Cooperative multi-agent sys-
in embodiments, environments, and tasks. Many have made tems offer benefits such as distributed perception and collab-
significant progress [111], [116], but still lack generalization orative fault recovery. However, they also face challenges, in-
capability on par with LLMs in NLP. Attaining such a level cludingeffectivecommunication,coordinateddispatching,and
of generalization is very challenging, as it requires the devel- fleetheterogeneity.Incertainscenarios,individualagentsmay
opment of many core AGI capabilities. have conflicting goals, which further increases complexity.
d) Multimodality: VLAsinheritmanychallengesassoci- h) Ethical and Societal Implications: Robotics has al-
atedwithmultimodalmodels,suchasobtainingusefulembed- waysraisedvariousethical,societal,andlegalconcerns.These
dings and aligning different modalities. Current approaches, include risks related to privacy, job displacement, decision-
like ImageBind [209] and LanguageBind [210], align differ- making bias, and the impact on social norms and human
ent modalities to the image or language embedding space, relationships.
respectively. Within a unified embedding space, MLLMs can i) Applications: Most current VLAs focus on house-
accommodate diverse modalities and become more general. hold or industrial settings, but a wider range of applications
However, whether focusing on embeddings alone is sufficient is possible, such as virtual assistants, autonomous vehicles,
remains under debate. Although beyond the scope of VLAs, and agricultural robots. Various embodiments may also call
other modalities—such as audio [43], haptics [211], and gaze for specialized VLAs, including dexterous hands, drones,
[212]—have proven useful for certain embodied AI applica- quadruped robots, and humanoid robots. One particularly
tions. For instance, modeling human gaze data using an addi- important field is healthcare, encompassing surgical robots
tional gaze network [213] or incorporating it via an auxiliary [216],carerobots[217].Healthcaredemandshighersafetyand
loss [214] has been shown to enhance the performance of the privacy standards and may necessitate novel techniques such
primary policy network. These approaches demonstrate that as human-in-the-loop (HITL) control and federated learning.
RL policies can benefit from human-like visual attention, as Moreover,duetothesignificantdomaingap,specializedvision
human gaze often reveals the most salient locations in the models might be needed for medical images.
environment [215]. While incorporating additional modalities
isoftenadvantageous,itinevitablyintroducesextracomplexity
VII. CONCLUSION
into the model design.
e) Framework for Long-Horizon Tasks: The hierarchical Vision-language-action models hold immense promise for
framework is currently the most practical approach for long- enabling embodied agents to interact with the physical world
horizon tasks. However, it increases system complexity and and fulfill users’ instructions. This paper is the first survey
potential points of failure. Frequent task execution failures to review large VLAs alongside generalized VLAs. Our tax-
can trigger re-planning, which can cause significant latency. onomy provides a high-level overview of three main lines of
Moreover, monolithic task planners share similar architec- research: key components, control policies, and task planners.
tures with LVLAs, so employing two large models can be We meticulously analyze and compare their technical details,

17
including model architectures, training strategies, and individ- [12] J.Wang,Z.Wu,Y.Li,H.Jiang,P.Shu,E.Shi,H.Hu,C.Ma,Y.Liu,
ualmodules.Additionally,wehighlightessentialresourcesfor X. Wang, Y. Yao, X. Liu, H. Zhao, Z. Liu, H. Dai, L. Zhao, B. Ge,
X.Li,T.Liu,andS.Zhang,“Largelanguagemodelsforrobotics:Op-
trainingandevaluatingVLAs,suchasdatasets,simulators,and
portunities,challenges,andperspectives,”CoRR,vol.abs/2401.04334,
benchmarks.Wehopethissurveycapturestherapidlyevolving 2024.
landscape of embodied AI and inspires future research. [13] Y. Hu, Q. Xie, V. Jain, J. Francis, J. Patrikar, N. V. Keetha, S. Kim,
Y. Xie, T. Zhang, S. Zhao, Y. Q. Chong, C. Wang, K. P. Sycara,
M. Johnson-Roberson, D. Batra, X. Wang, S. A. Scherer, Z. Kira,
F. Xia, and Y. Bisk, “Toward general-purpose robots via foundation
ACKNOWLEDGMENTS
models: A survey and meta-analysis,” CoRR, vol. abs/2312.08782,
Theresearchpresentedinthispaperwaspartiallysupported 2023.
[14] K.Kawaharazuka,T.Matsushima,A.Gambardella,J.Guo,C.Paxton,
by the Research Grants Council of the Hong Kong Special
andA.Zeng,“Real-worldrobotapplicationsoffoundationmodels:a
AdministrativeRegion,China(CUHK2410072,RGCR1015- review,”Adv.Robotics,vol.38,no.18,pp.1232–1254,2024.
23) and CUHK 7010870. [15] L. Chen, K. Lu, A. Rajeswaran, K. Lee, A. Grover, M. Laskin,
P. Abbeel, A. Srinivas, and I. Mordatch, “Decision transformer: Re-
inforcement learning via sequence modeling,” in NeurIPS, 2021, pp.
15084–15097.
REFERENCES
[16] M.Janner,Q.Li,andS.Levine,“Offlinereinforcementlearningasone
bigsequencemodelingproblem,”inNeurIPS,2021,pp.1273–1286.
[1] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choro-
[17] S. E. Reed, K. Zolna, E. Parisotto, S. G. Colmenarejo, A. Novikov,
manski, T. Ding, D. Driess, A. Dubey, C. Finn, P. Florence, C. Fu,
G. Barth-Maron, M. Gimenez, Y. Sulsky, J. Kay, J. T. Springenberg,
M. G. Arenas, K. Gopalakrishnan, K. Han, K. Hausman, A. Herzog,
T. Eccles, J. Bruce, A. Razavi, A. Edwards, N. Heess, Y. Chen,
J. Hsu, B. Ichter, A. Irpan, N. J. Joshi, R. Julian, D. Kalashnikov,
R. Hadsell, O. Vinyals, M. Bordbar, and N. de Freitas, “A generalist
Y.Kuang,I.Leal,L.Lee,T.E.Lee,S.Levine,Y.Lu,H.Michalewski,
agent,”Trans.Mach.Learn.Res.,vol.2022,2022.
I.Mordatch,K.Pertsch,K.Rao,K.Reymann,M.S.Ryoo,G.Salazar,
[18] A.A.PhysicalIntelligenceand,R.Aniceto,A.Balakrishna,K.Black,
P. Sanketi, P. Sermanet, J. Singh, A. Singh, R. Soricut, H. T. Tran,
K. Conley, G. Connors, J. Darpinian, K. Dhabalia, J. DiCarlo,
V. Vanhoucke, Q. Vuong, A. Wahid, S. Welker, P. Wohlhart, J. Wu,
D.Driess,M.Equi,A.Esmail,Y.Fang,C.Finn,C.Glossop,T.God-
F.Xia,T.Xiao,P.Xu,S.Xu,T.Yu,andB.Zitkovich,“RT-2:vision-
den,I.Goryachev,L.Groom,H.Hancock,K.Hausman,G.Hussein,
language-action models transfer web knowledge to robotic control,”
B. Ichter, S. Jakubczak, R. Jen, T. Jones, B. Katz, L. Ke, C. Kuchi,
CoRR,vol.abs/2307.15818,2023.
M. Lamb, D. LeBlanc, S. Levine, A. Li-Bell, Y. Lu, V. Mano,
[2] A.Krizhevsky,I.Sutskever,andG.E.Hinton,“Imagenetclassification
M.Mothukuri,S.Nair,K.Pertsch,A.Z.Ren,C.Sharma,L.X.Shi,
with deep convolutional neural networks,” in NIPS, 2012, pp. 1106–
L.Smith,J.T.Springenberg,K.Stachowicz,W.Stoeckle,A.Swerdlow,
1114.
J. Tanner, M. Torne, Q. Vuong, A. Walling, H. Wang, B. Williams,
[3]
G
A
o
.
m
V
e
a
z
s
,
w
L
an
.
i
K
,
a
N
is
.
er
S
,
h
a
a
n
z
d
ee
I
r
.
,
P
N
o
.
lo
P
s
a
u
r
k
m
h
a
in
r,
, “
J
A
.
t
U
te
s
n
z
t
k
io
o
n
rei
i
t
s
,
a
L
ll
.
y
J
o
o
u
ne
n
s,
ee
A
d,
.
”
N
in
. S.Yoo,L.Yu,U.Zhilinsky,andZ.Zhou,“π* 0.6:aVLAthatlearns,
fromexperience,”CoRR,vol.abs/2511.14759,2025.
NIPS,2017,pp.5998–6008.
[19] A. Hiranaka, M. Hwang, S. Lee, C. Wang, L. Fei-Fei, J. Wu, and
[4] V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G.
R.Zhang,“Primitiveskill-basedrobotlearningfromhumanevaluative
Bellemare, A. Graves, M. A. Riedmiller, A. Fidjeland, G. Ostrovski,
feedback,”inIROS,2023,pp.7817–7824.
S.Petersen,C.Beattie,A.Sadik,I.Antonoglou,H.King,D.Kumaran,
D.Wierstra,S.Legg,andD.Hassabis,“Human-levelcontrolthrough [20] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao,
deep reinforcement learning,” Nat., vol. 518, no. 7540, pp. 529–533, “Reflexion: language agents with verbal reinforcement learning,” in
2015.
NeurIPS,2023.
[5] S. Levine, P. Pastor, A. Krizhevsky, and D. Quillen, “Learning hand- [21] Y. J. Ma, W. Liang, G. Wang, D. Huang, O. Bastani, D. Jayaraman,
eyecoordinationforroboticgraspingwithlarge-scaledatacollection,” Y. Zhu, L. Fan, and A. Anandkumar, “Eureka: Human-level reward
in ISER, ser. Springer Proceedings in Advanced Robotics, vol. 1. designviacodinglargelanguagemodels,”inICLR,2024.
Springer,2016,pp.173–184. [22] A.Radford,J.W.Kim,C.Hallacy,A.Ramesh,G.Goh,S.Agarwal,
[6] J. Li, D. Li, S. Savarese, and S. C. H. Hoi, “BLIP-2: bootstrapping G.Sastry,A.Askell,P.Mishkin,J.Clark,G.Krueger,andI.Sutskever,
language-image pre-training with frozen image encoders and large “Learning transferable visual models from natural language supervi-
language models,” in ICML, vol. 202. PMLR, 2023, pp. 19730– sion,”inICML,vol.139. PMLR,2021,pp.8748–8763.
19742. [23] S. Nair, A. Rajeswaran, V. Kumar, C. Finn, and A. Gupta, “R3M: A
[7] H.Liu,C.Li,Q.Wu,andY.J.Lee,“Visualinstructiontuning,”CoRR, universalvisualrepresentationforrobotmanipulation,”inCoRL,vol.
vol.abs/2304.08485,2023. 205. PMLR,2022,pp.892–909.
[8] W. Huang, F. Xia, T. Xiao, H. Chan, J. Liang, P. Florence, A. Zeng, [24] Y. J. Ma, S. Sodhani, D. Jayaraman, O. Bastani, V. Kumar, and
J. Tompson, I. Mordatch, Y. Chebotar, P. Sermanet, T. Jackson, A. Zhang, “VIP: towards universal visual reward and representation
N.Brown,L.Luu,S.Levine,K.Hausman,andB.Ichter,“Innermono- viavalue-implicitpre-training,”inICLR,2023.
logue: Embodied reasoning through planning with language models,” [25] I.Radosavovic,T.Xiao,S.James,P.Abbeel,J.Malik,andT.Darrell,
inCoRL,vol.205. PMLR,2022,pp.1769–1782. “Real-worldrobotlearningwithmaskedvisualpre-training,”inCoRL,
[9] B. Ichter, A. Brohan, Y. Chebotar, C. Finn, K. Hausman, A. Herzog, vol.205. PMLR,2022,pp.416–426.
D.Ho,J.Ibarz,A.Irpan,E.Jang,R.Julian,D.Kalashnikov,S.Levine, [26] J.Devlin,M.Chang,K.Lee,andK.Toutanova,“BERT:pre-training
Y.Lu,C.Parada,K.Rao,P.Sermanet,A.Toshev,V.Vanhoucke,F.Xia, of deep bidirectional transformers for language understanding,” in
T. Xiao, P. Xu, M. Yan, N. Brown, M. Ahn, O. Cortes, N. Sievers, NAACL-HLT (1). Association for Computational Linguistics, 2019,
C. Tan, S. Xu, D. Reyes, J. Rettinghouse, J. Quiambao, P. Pastor, pp.4171–4186.
L. Luu, K. Lee, Y. Kuang, S. Jesmonth, N. J. Joshi, K. Jeffrey, R. J. [27] I. Radosavovic, B. Shi, L. Fu, K. Goldberg, T. Darrell, and J. Malik,
Ruano,J.Hsu,K.Gopalakrishnan,B.David,A.Zeng,andC.K.Fu, “Robot learning with sensorimotor pre-training,” in CoRL, vol. 229.
“DoasIcan,notasIsay:Groundinglanguageinroboticaffordances,” PMLR,2023,pp.683–693.
inCoRL,vol.205. PMLR,2022,pp.287–318. [28] M. Shridhar, L. Manuelli, and D. Fox, “Cliport: What and where
[10] D.Driess,F.Xia,M.S.M.Sajjadi,C.Lynch,A.Chowdhery,B.Ichter, pathwaysforroboticmanipulation,”inCoRL,vol.164. PMLR,2021,
A. Wahid, J. Tompson, Q. Vuong, T. Yu, W. Huang, Y. Chebotar, pp.894–906.
P. Sermanet, D. Duckworth, S. Levine, V. Vanhoucke, K. Hausman, [29] A.Khandelwal,L.Weihs,R.Mottaghi,andA.Kembhavi,“Simplebut
M.Toussaint,K.Greff,A.Zeng,I.Mordatch,andP.Florence,“Palm-e: effective:CLIPembeddingsforembodiedAI,”inCVPR. IEEE,2022,
Anembodiedmultimodallanguagemodel,”inICML,vol.202. PMLR, pp.14809–14818.
2023,pp.8469–8488. [30] S.Y.Gadre,M.Wortsman,G.Ilharco,L.Schmidt,andS.Song,“Cows
[11] R. Firoozi, J. Tucker, S. Tian, A. Majumdar, J. Sun, W. Liu, Y. Zhu, on pasture: Baselines and benchmarks for language-driven zero-shot
S. Song, A. Kapoor, K. Hausman, B. Ichter, D. Driess, J. Wu, objectnavigation,”inCVPR. IEEE,2023,pp.23171–23181.
C.Lu,andM.Schwager,“Foundationmodelsinrobotics:Applications, [31] A. Majumdar, K. Yadav, S. Arnaud, Y. J. Ma, C. Chen, S. Silwal,
challenges,andthefuture,”CoRR,vol.abs/2312.07843,2023. A. Jain, V. Berges, T. Wu, J. Vakil, P. Abbeel, J. Malik, D. Batra,

18
Y. Lin, O. Maksymets, A. Rajeswaran, and F. Meier, “Where are we [55] V. Micheli, E. Alonso, and F. Fleuret, “Transformers are sample-
inthesearchforanartificialvisualcortexforembodiedintelligence?” efficientworldmodels,”inICLR,2023.
inNeurIPS,2023. [56] J.Robine,M.Ho¨ftmann,T.Uelwer,andS.Harmeling,“Transformer-
[32] S. Karamcheti, S. Nair, A. S. Chen, T. Kollar, C. Finn, D. Sadigh, basedworldmodelsarehappywith100kinteractions,”inICLR,2023.
and P. Liang, “Language-driven representation learning for robotics,” [57] K. Nottingham, P. Ammanabrolu, A. Suhr, Y. Choi, H. Hajishirzi,
inRSS,2023. S.Singh,andR.Fox,“Doembodiedagentsdreamofpixelatedsheep:
[33] M.Oquab,T.Darcet,T.Moutakanni,H.V.Vo,M.Szafraniec,V.Khali- Embodied decision making using language guided world modelling,”
dov, P. Fernandez, D. Haziza, F. Massa, A. El-Nouby, M. Assran, inICML,vol.202. PMLR,2023,pp.26311–26325.
N.Ballas,W.Galuba,R.Howes,P.Huang,S.Li,I.Misra,M.Rabbat, [58] Z. Song, Y. Zhang, and I. King, “No change, no gain: Empowering
V. Sharma, G. Synnaeve, H. Xu, H. Je´gou, J. Mairal, P. Labatut, graphneuralnetworkswithexpectedmodelchangemaximizationfor
A.Joulin,andP.Bojanowski,“Dinov2:Learningrobustvisualfeatures activelearning,”inNeurIPS,2023.
withoutsupervision,”Trans.Mach.Learn.Res.,vol.2024,2024. [59] Y. Ma, Z. Song, X. Hu, J. Li, Y. Zhang, and I. King, “Graph
[34] M.J.Kim,K.Pertsch,S.Karamcheti,T.Xiao,A.Balakrishna,S.Nair, componentcontrastivelearningforconceptrelatednessestimation,”in
R. Rafailov, E. P. Foster, G. Lam, P. Sanketi, Q. Vuong, T. Kollar, AAAI. AAAIPress,2023,pp.13362–13370.
B.Burchfiel,R.Tedrake,D.Sadigh,S.Levine,P.Liang,andC.Finn, [60] L.Guan,K.Valmeekam,S.Sreedharan,andS.Kambhampati,“Lever-
“Openvla:Anopen-sourcevision-language-actionmodel,”CoRR,vol. agingpre-trainedlargelanguagemodelstoconstructandutilizeworld
abs/2406.09246,2024. modelsformodel-basedtaskplanning,”inNeurIPS,2023.
[35] W. Huang, C. Wang, Y. Li, R. Zhang, and L. Fei-Fei, “Rekep:
[61] B.Liu,Y.Jiang,X.Zhang,Q.Liu,S.Zhang,J.Biswas,andP.Stone,
Spatio-temporalreasoningofrelationalkeypointconstraintsforrobotic
“LLM+P: empowering large language models with optimal planning
manipulation,”CoRR,vol.abs/2409.01652,2024.
proficiency,”CoRR,vol.abs/2304.11477,2023.
[36] M.Assran,Q.Duval,I.Misra,P.Bojanowski,P.Vincent,M.G.Rabbat,
[62] S.Hao,Y.Gu,H.Ma,J.J.Hong,Z.Wang,D.Z.Wang,andZ.Hu,
Y.LeCun,andN.Ballas,“Self-supervisedlearningfromimageswith
“Reasoning with language model is planning with world model,” in
ajoint-embeddingpredictivearchitecture,”inCVPR. IEEE,2023,pp.
EMNLP,2023,pp.8154–8173.
15619–15629.
[63] M.Hu,Y.Mu,X.Yu,M.Ding,S.Wu,W.Shao,Q.Chen,B.Wang,
[37] J.Shang,K.Schmeckpeper,B.B.May,M.V.Minniti,T.Kelestemur,
Y.Qiao,andP.Luo,“Tree-planner:Efficientclose-looptaskplanning
D.Watkins,andL.Herlant,“Theia:Distillingdiversevisionfoundation
withlargelanguagemodels,”inICLR,2024.
models for robot learning,” in CoRL, ser. Proceedings of Machine
[64] Z.Zhao,W.S.Lee,andD.Hsu,“Largelanguagemodelsascommon-
LearningResearch,vol.270. PMLR,2024,pp.724–748.
senseknowledgeforlarge-scaletaskplanning,”inNeurIPS,2023.
[38] S. Parisi, A. Rajeswaran, S. Purushwalkam, and A. Gupta, “The
[65] OpenAI. (2024) Video generation models as world
unsurprising effectiveness of pre-trained vision models for control,”
simulators. [Online]. Available: https://openai.com/index/
inICML,vol.162. PMLR,2022,pp.17359–17371.
video-generation-models-as-world-simulators/
[39] Y. LeCun and Courant, “A path towards autonomous machine
[66] Z.Zhu,X.Wang,W.Zhao,C.Min,N.Deng,M.Dou,Y.Wang,B.Shi,
intelligence version 0.9.2, 2022-06-27,” 2022. [Online]. Available:
K.Wang,C.Zhang,Y.You,Z.Zhang,D.Zhao,L.Xiao,J.Zhao,J.Lu,
https://api.semanticscholar.org/CorpusID:251881108
andG.Huang,“Issoraaworldsimulator?Acomprehensivesurveyon
[40] W.Shen,G.Yang,A.Yu,J.Wong,L.P.Kaelbling,andP.Isola,“Dis-
generalworldmodelsandbeyond,”CoRR,vol.abs/2405.03520,2024.
tilledfeaturefieldsenablefew-shotlanguage-guidedmanipulation,”in
CoRL,vol.229. PMLR,2023,pp.405–424. [67] J. Bruce, M. D. Dennis, A. Edwards, J. Parker-Holder, Y. Shi,
E.Hughes,M.Lai,A.Mavalankar,R.Steigerwald,C.Apps,Y.Aytar,
[41] Y.Hong,H.Zhen,P.Chen,S.Zheng,Y.Du,Z.Chen,andC.Gan,“3d-
S.Bechtle,F.M.P.Behbahani,S.C.Y.Chan,N.Heess,L.Gonzalez,
llm: Injecting the 3d world into large language models,” in NeurIPS,
S. Osindero, S. Ozair, S. E. Reed, J. Zhang, K. Zolna, J. Clune,
2023.
N. de Freitas, S. Singh, and T. Rockta¨schel, “Genie: Generative
[42] B.Kerbl,G.Kopanas,T.Leimku¨hler,andG.Drettakis,“3dgaussian
interactiveenvironments,”inICML,2024.
splatting for real-time radiance field rendering,” ACM Trans. Graph.,
[68] H. Zhen, X. Qiu, P. Chen, J. Yang, X. Yan, Y. Du, Y. Hong, and
vol.42,no.4,pp.139:1–139:14,2023.
C.Gan,“3d-vla:A3dvision-language-actiongenerativeworldmodel,”
[43] A. Thankaraj and L. Pinto, “That sounds right: Auditory self-
inICML,2024.
supervision for dynamic robot manipulation,” in CoRL, vol. 229.
PMLR,2023,pp.1036–1049. [69] S. Yang, Y. Du, S. K. S. Ghasemipour, J. Tompson, L. P. Kaelbling,
D.Schuurmans,andP.Abbeel,“Learninginteractivereal-worldsimu-
[44] Y. Jing, X. Zhu, X. Liu, Q. Sima, T. Yang, Y. Feng, and T. Kong,
lators,”inICLR,2024.
“Exploringvisualpre-trainingforrobotmanipulation:Datasets,models
andmethods,”inIROS,2023,pp.11390–11395. [70] J. Xiang, T. Tao, Y. Gu, T. Shu, Z. Wang, Z. Yang, and Z. Hu,
[45] F. Liu, H. Liu, A. Grover, and P. Abbeel, “Masked autoencoding for “Languagemodelsmeetworldmodels:Embodiedexperiencesenhance
scalableandgeneralizabledecisionmaking,”inNeurIPS,2022. languagemodels,”inNeurIPS,2023.
[46] J. Li, Q. Gao, M. Johnston, X. Gao, X. He, H. Shi, S. Shakiah, [71] T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa, “Large
R. Ghanadan, and W. Y. Wang, “Mastering robot manipulation with languagemodelsarezero-shotreasoners,”inNeurIPS,2022.
multimodalpromptsthroughpretrainingandmulti-taskfine-tuning,”in [72] J.Wei,X.Wang,D.Schuurmans,M.Bosma,B.Ichter,F.Xia,E.H.
ICML,2024. Chi, Q. V. Le, and D. Zhou, “Chain-of-thought prompting elicits
[47] Y. Sun, S. Ma, R. Madaan, R. Bonatti, F. Huang, and A. Kapoor, reasoninginlargelanguagemodels,”inNeurIPS,2022.
“SMART: self-supervised multi-task pretraining with control trans- [73] G. Lu, Z. Wang, C. Liu, J. Lu, and Y. Tang, “Thinkbot: Embod-
formers,”inICLR,2023. ied instruction following with thought chain reasoning,” CoRR, vol.
[48] R. Bonatti, S. Vemprala, S. Ma, F. Frujeri, S. Chen, and abs/2312.07062,2023.
A. Kapoor, “PACT: perception-action causal transformer for autore- [74] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. R. Narasimhan, and
gressiveroboticspre-training,”inIROS,2023,pp.3621–3627. Y.Cao,“React:Synergizingreasoningandactinginlanguagemodels,”
[49] B. Baker, I. Akkaya, P. Zhokhov, J. Huizinga, J. Tang, A. Ecoffet, inICLR,2023.
B. Houghton, R. Sampedro, and J. Clune, “Video pretraining (VPT): [75] Z.Wang,A.Liu,H.Lin,J.Li,X.Ma,andY.Liang,“RAT:retrieval
learningtoactbywatchingunlabeledonlinevideos,”inNeurIPS,2022. augmented thoughts elicit context-aware reasoning in long-horizon
[50] H. Wu, Y. Jing, C. Cheang, G. Chen, J. Xu, X. Li, M. Liu, H. Li, generation,”CoRR,vol.abs/2403.05313,2024.
andT.Kong,“Unleashinglarge-scalevideogenerativepre-trainingfor [76] M.Zawalski,W.Chen,K.Pertsch,O.Mees,C.Finn,andS.Levine,
visualrobotmanipulation,”inICLR,2024. “Roboticcontrolviaembodiedchain-of-thoughtreasoning,”CoRR,vol.
[51] D.Hafner,T.P.Lillicrap,J.Ba,andM.Norouzi,“Dreamtocontrol: abs/2407.08693,2024.
Learningbehaviorsbylatentimagination,”inICLR,2020. [77] Q. Zhao, Y. Lu, M. J. Kim, Z. Fu, Z. Zhang, Y. Wu, Z. Li, Q. Ma,
[52] D.Hafner,T.P.Lillicrap,M.Norouzi,andJ.Ba,“Masteringatariwith S.Han,C.Finn,A.Handa,T.Lin,G.Wetzstein,M.Liu,andD.Xiang,
discreteworldmodels,”inICLR,2021. “Cot-vla:Visualchain-of-thoughtreasoningforvision-language-action
[53] D.Hafner,J.Pasukonis,J.Ba,andT.P.Lillicrap,“Masteringdiverse models,”inCVPR,2025,pp.1702–1713.
domainsthroughworldmodels,”CoRR,vol.abs/2301.04104,2023. [78] M. Nakamoto, O. Mees, A. Kumar, and S. Levine, “Steering your
[54] P. Wu, A. Escontrela, D. Hafner, P. Abbeel, and K. Goldberg, “Day- generalists:Improvingroboticfoundationmodelsviavalueguidance,”
dreamer:Worldmodelsforphysicalrobotlearning,”inCoRL,vol.205. in CoRL, ser. Proceedings of Machine Learning Research, vol. 270.
PMLR,2022,pp.2226–2240. PMLR,2024,pp.4996–5013.

19
[79] J.Kwok,C.Agia,R.Sinha,M.Foutter,S.Li,I.Stoica,A.Mirhoseini, Robotic task generalization via hindsight trajectory sketches,” CoRR,
andM.Pavone,“Robomonkey:Scalingtest-timesamplingandverifi- vol.abs/2311.01977,2023.
cationforvision-language-actionmodels,”CoRR,vol.abs/2506.17811, [98] T.Z.Zhao,V.Kumar,S.Levine,andC.Finn,“Learningfine-grained
2025. bimanualmanipulationwithlow-costhardware,”inRSS,2023.
[80] E. Jang, A. Irpan, M. Khansari, D. Kappler, F. Ebert, C. Lynch, [99] H.Bharadhwaj,J.Vakil,M.Sharma,A.Gupta,S.Tulsiani,andV.Ku-
S. Levine, and C. Finn, “BC-Z: zero-shot task generalization with mar,“Roboagent:Generalizationandefficiencyinrobotmanipulation
robotic imitation learning,” in CoRL, vol. 164. PMLR, 2021, pp. via semantic augmentations and action chunking,” in ICRA. IEEE,
991–1002. 2024,pp.4788–4795.
[81] C. Lynch and P. Sermanet, “Language conditioned imitation learning [100] X. Li, M. Liu, H. Zhang, C. Yu, J. Xu, H. Wu, C. Cheang, Y. Jing,
overunstructureddata,”inRSS,2021. W. Zhang, H. Liu, H. Li, and T. Kong, “Vision-language foundation
[82] O. Mees, L. Hermann, and W. Burgard, “What matters in language modelsaseffectiverobotimitators,”CoRR,vol.abs/2311.01378,2023.
conditioned robotic imitation learning over unstructured data,” IEEE [101] F.Liu,F.Yan,L.Zheng,C.Feng,Y.Huang,andL.Ma,“Robouniview:
RoboticsAutom.Lett.,vol.7,no.4,pp.11205–11212,2022. Visual-language model with unified view representation for robotic
[83] O. Mees, J. Borja-Diaz, and W. Burgard, “Grounding language with manipulaiton,”CoRR,vol.abs/2406.18977,2024.
visualaffordancesoverunstructureddata,”inICRA. IEEE,2023,pp. [102] Y. Yue, Y. Wang, B. Kang, Y. Han, S. Wang, S. Song, J. Feng, and
11576–11582. G.Huang,“Deer-vla:Dynamicinferenceofmultimodallargelanguage
[84] Y.Du,S.Yang,B.Dai,H.Dai,O.Nachum,J.Tenenbaum,D.Schu- modelsforefficientrobotexecution,”inNeurIPS,2024.
urmans, and P. Abbeel, “Learning universal policies via text-guided [103] S.Huang,Z.Jiang,H.Dong,Y.Qiao,P.Gao,andH.Li,“Instruct2act:
videogeneration,”inNeurIPS,2023. Mapping multi-modality instructions to robotic actions with large
[85] P. Sharma, B. Sundaralingam, V. Blukis, C. Paxton, T. Hermans, languagemodel,”CoRR,vol.abs/2305.11176,2023.
A. Torralba, J. Andreas, and D. Fox, “Correcting robot plans with [104] W.Huang,C.Wang,R.Zhang,Y.Li,J.Wu,andL.Fei-Fei,“Voxposer:
naturallanguagefeedback,”inRSS,2022. Composable 3d value maps for robotic manipulation with language
[86] C. Lynch, A. Wahid, J. Tompson, T. Ding, J. Betker, R. Baruch, models,”CoRR,vol.abs/2307.05973,2023.
T.Armstrong,andP.Florence,“Interactivelanguage:Talkingtorobots [105] C.Chi,S.Feng,Y.Du,Z.Xu,E.Cousineau,B.Burchfiel,andS.Song,
inrealtime,”CoRR,vol.abs/2210.06407,2022. “Diffusionpolicy:Visuomotorpolicylearningviaactiondiffusion,”in
[87] P.Guhur,S.Chen,R.G.Pinel,M.Tapaswi,I.Laptev,andC.Schmid, RSS,2023.
“Instruction-driven history-aware policies for robotic manipulations,” [106] Y. Ze, G. Zhang, K. Zhang, C. Hu, M. Wang, and H. Xu, “3d
inCoRL,vol.205. PMLR,2022,pp.175–187. diffusionpolicy:Generalizablevisuomotorpolicylearningviasimple
[88] M. Shridhar, L. Manuelli, and D. Fox, “Perceiver-actor: A multi-task 3drepresentations,”inRSS,2024.
transformer for robotic manipulation,” in CoRL, vol. 205. PMLR, [107] H. Ha, P. Florence, and S. Song, “Scaling up and distilling down:
2022,pp.785–799. Language-guidedrobotskillacquisition,”inCoRL,vol.229. PMLR,
[89] T. Gervet, Z. Xian, N. Gkanatsios, and K. Fragkiadaki, “Act3d: 3d 2023,pp.3766–3777.
feature field transformers for multi-task robotic manipulation,” in [108] D. Ghosh, H. R. Walke, K. Pertsch, K. Black, O. Mees, S. Dasari,
CoRL,vol.229. PMLR,2023,pp.3949–3965. J.Hejna,T.Kreiman,C.Xu,J.Luo,Y.L.Tan,L.Y.Chen,Q.Vuong,
[90] A. Goyal, J. Xu, Y. Guo, V. Blukis, Y. Chao, and D. Fox, “RVT: T.Xiao,P.R.Sanketi,D.Sadigh,C.Finn,andS.Levine,“Octo:An
robotic view transformer for 3d object manipulation,” in CoRL, vol. open-sourcegeneralistrobotpolicy,”inRSS,2024.
229. PMLR,2023,pp.694–710. [109] T. Ke, N. Gkanatsios, and K. Fragkiadaki, “3d diffuser actor: Policy
[91] A. Goyal, V. Blukis, J. Xu, Y. Guo, Y. Chao, and D. Fox, “RVT-2: diffusion with 3d scene representations,” CoRR, vol. abs/2402.10885,
learning precise manipulation from few demonstrations,” CoRR, vol. 2024.
abs/2406.08545,2024. [110] M.Reuss,O¨.E.Yagmurlu,F.Wenzel,andR.Lioutikov,“Multimodal
[92] W. Yuan, J. Duan, V. Blukis, W. Pumacay, R. Krishna, A. Murali, diffusion transformer: Learning versatile behavior from multimodal
A.Mousavian,andD.Fox,“Robopoint:Avision-languagemodelfor goals,”CoRR,vol.abs/2407.05996,2024.
spatialaffordancepredictionforrobotics,”CoRR,vol.abs/2406.10721, [111] S. Liu, L. Wu, B. Li, H. Tan, H. Chen, Z. Wang, K. Xu, H. Su,
2024. and J. Zhu, “Rdt-1b: a diffusion foundation model for bimanual
[93] K. Bousmalis, G. Vezzani, D. Rao, C. Devin, A. X. Lee, M. Bauza´, manipulation,”arXivpreprintarXiv:2410.07864,2024.
T. Davchev, Y. Zhou, A. Gupta, A. Raju, A. Laurens, C. Fantacci, [112] S. Belkhale, T. Ding, T. Xiao, P. Sermanet, Q. Vuong, J. Tompson,
V.Dalibard,M.Zambelli,M.F.Martins,R.Pevceviciute,M.Blokzijl, Y. Chebotar, D. Dwibedi, and D. Sadigh, “RT-H: action hierarchies
M. Denil, N. Batchelor, T. Lampe, E. Parisotto, K. Zolna, S. E. usinglanguage,”CoRR,vol.abs/2403.01823,2024.
Reed, S. G. Colmenarejo, J. Scholz, A. Abdolmaleki, O. Groth, [113] O. X. Collaboration, A. Padalkar, A. Pooley, A. Jain, A. Bewley,
J. Regli, O. Sushkov, T. Rotho¨rl, J. E. Chen, Y. Aytar, D. Barker, A. Herzog, A. Irpan, A. Khazatsky, A. Raj, A. Singh, A. Brohan,
J. Ortiz, M. A. Riedmiller, J. T. Springenberg, R. Hadsell, F. Nori, A. Raffin, A. Wahid, B. Burgess-Limerick, B. Kim, B. Scho¨lkopf,
andN.Heess,“Robocat:Aself-improvingfoundationagentforrobotic B.Ichter,C.Lu,C.Xu,C.Finn,C.Xu,C.Chi,C.Huang,C.Chan,
manipulation,”CoRR,vol.abs/2306.11706,2023. C. Pan, C. Fu, C. Devin, D. Driess, D. Pathak, D. Shah, D. Bu¨chler,
[94] A. Stone, T. Xiao, Y. Lu, K. Gopalakrishnan, K. Lee, Q. Vuong, D. Kalashnikov, D. Sadigh, E. Johns, F. Ceola, F. Xia, F. Stulp,
P. Wohlhart, B. Zitkovich, F. Xia, C. Finn, and K. Hausman, “Open- G.Zhou,G.S.Sukhatme,G.Salhotra,G.Yan,G.Schiavi,G.Kahn,
worldobjectmanipulationusingpre-trainedvision-languagemodels,” H. Su, H. Fang, H. Shi, H. B. Amor, H. I. Christensen, H. Furuta,
CoRR,vol.abs/2303.00905,2023. H.Walke,H.Fang,I.Mordatch,I.Radosavovic,andetal.,“Openx-
[95] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, embodiment:RoboticlearningdatasetsandRT-Xmodels,”CoRR,vol.
K.Gopalakrishnan,K.Hausman,A.Herzog,J.Hsu,J.Ibarz,B.Ichter, abs/2310.08864,2023.
A. Irpan, T. Jackson, S. Jesmonth, N. J. Joshi, R. Julian, D. Kalash- [114] M.J.Kim,C.Finn,andP.Liang,“Fine-tuningvision-language-action
nikov, Y. Kuang, I. Leal, K. Lee, S. Levine, Y. Lu, U. Malla, models: Optimizing speed and success,” CoRR, vol. abs/2502.19645,
D.Manjunath,I.Mordatch,O.Nachum,C.Parada,J.Peralta,E.Perez, 2025.
K. Pertsch, J. Quiambao, K. Rao, M. S. Ryoo, G. Salazar, P. R. [115] R.Zheng,Y.Liang,S.Huang,J.Gao,H.D.III,A.Kolobov,F.Huang,
Sanketi,K.Sayed,J.Singh,S.Sontakke,A.Stone,C.Tan,H.T.Tran, and J. Yang, “Tracevla: Visual trace prompting enhances spatial-
V.Vanhoucke,S.Vega,Q.Vuong,F.Xia,T.Xiao,P.Xu,S.Xu,T.Yu, temporalawarenessforgeneralistroboticpolicies,”inICLR,2025.
andB.Zitkovich,“RT-1:roboticstransformerforreal-worldcontrolat [116] K.Black,N.Brown,D.Driess,A.Esmail,M.Equi,C.Finn,N.Fusai,
scale,”inRSS,2023. L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones, L. Ke,
[96] Y.Chebotar,Q.Vuong,A.Irpan,K.Hausman,F.Xia,Y.Lu,A.Kumar, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch, L. X. Shi,
T.Yu,A.Herzog,K.Pertsch,K.Gopalakrishnan,J.Ibarz,O.Nachum, J.Tanner,Q.Vuong,A.Walling,H.Wang,andU.Zhilinsky,“π0:A
S.Sontakke,G.Salazar,H.T.Tran,J.Peralta,C.Tan,D.Manjunath, vision-language-action flow model for general robot control,” CoRR,
J.Singh,B.Zitkovich,T.Jackson,K.Rao,C.Finn,andS.Levine,“Q- vol.abs/2410.24164,2024.
transformer:Scalableofflinereinforcementlearningviaautoregressive [117] J. Liu, M. Liu, Z. Wang, P. An, X. Li, K. Zhou, S. Yang, R. Zhang,
q-functions,”CoRR,vol.abs/2309.10150,2023. Y.Guo,andS.Zhang,“Robomamba:Efficientvision-language-action
[97] J. Gu, S. Kirmani, P. Wohlhart, Y. Lu, M. G. Arenas, K. Rao, modelforroboticreasoningandmanipulation,”inNeurIPS,2024.
W. Yu, C. Fu, K. Gopalakrishnan, Z. Xu, P. Sundaresan, P. Xu, [118] D. Qu, H. Song, Q. Chen, Y. Yao, X. Ye, Y. Ding, Z. Wang, J. Gu,
H. Su, K. Hausman, C. Finn, Q. Vuong, and T. Xiao, “Rt-trajectory: B.Zhao,D.Wang,andX.Li,“Spatialvla:Exploringspatialrepresen-

20
tationsforvisual-language-actionmodel,”CoRR,vol.abs/2501.15830, [138] Y.Mu,Q.Zhang,M.Hu,W.Wang,M.Ding,J.Jin,B.Wang,J.Dai,
2025. Y. Qiao, and P. Luo, “Embodiedgpt: Vision-language pre-training via
[119] J.Wen,Y.Zhu,J.Li,M.Zhu,K.Wu,Z.Xu,N.Liu,R.Cheng,C.Shen, embodiedchainofthought,”CoRR,vol.abs/2305.15021,2023.
Y. Peng, F. Feng, and J. Tang, “Tinyvla: Towards fast, data-efficient [139] J.Huang,S.Yong,X.Ma,X.Linghu,P.Li,Y.Wang,Q.Li,S.Zhu,
vision-language-action models for robotic manipulation,” CoRR, vol. B.Jia,andS.Huang,“Anembodiedgeneralistagentin3dworld,”in
abs/2409.12514,2024. ICML,2024.
[120] Q.Li,Y.Liang,Z.Wang,L.Luo,X.Chen,M.Liao,F.Wei,Y.Deng, [140] Z. Qi, R. Dong, S. Zhang, H. Geng, C. Han, Z. Ge, L. Yi, and
S. Xu, Y. Zhang, X. Wang, B. Liu, J. Fu, J. Bao, D. Chen, Y. Shi, K. Ma, “Shapellm: Universal 3d object understanding for embodied
J.Yang,andB.Guo,“Cogact:Afoundationalvision-language-action interaction,” in ECCV (43), ser. Lecture Notes in Computer Science,
model for synergizing cognition and action in robotic manipulation,” vol.15101. Springer,2024,pp.214–238.
CoRR,vol.abs/2411.19650,2024. [141] W.Huang,P.Abbeel,D.Pathak,andI.Mordatch,“Languagemodels
[121] J.Wen,Y.Zhu,J.Li,Z.Tang,C.Shen,andF.Feng,“Dexvla:Vision- as zero-shot planners: Extracting actionable knowledge for embodied
languagemodelwithplug-indiffusionexpertforgeneralrobotcontrol,” agents,”inICML,vol.162. PMLR,2022,pp.9118–9147.
CoRR,vol.abs/2502.05855,2025. [142] P.Sharma,A.Torralba,andJ.Andreas,“Skillinductionandplanning
[122] J. Liu, H. Chen, P. An, Z. Liu, R. Zhang, C. Gu, X. Li, Z. Guo, withlatentlanguage,”inACL(1),2022,pp.1713–1726.
S. Chen, M. Liu, C. Hou, M. Zhao, K. alex Zhou, P. Heng, and [143] C.H.Song,B.M.Sadler,J.Wu,W.Chao,C.Washington,andY.Su,
S. Zhang, “Hybridvla: Collaborative diffusion and autoregression in “Llm-planner:Few-shotgroundedplanningforembodiedagentswith
a unified vision-language-action model,” CoRR, vol. abs/2503.10631, largelanguagemodels,”inICCV. IEEE,2023,pp.2986–2997.
2025. [144] S.Li,X.Puig,C.Paxton,Y.Du,C.Wang,L.Fan,T.Chen,D.Huang,
[123] S. Ye, J. Jang, B. Jeon, S. J. Joo, J. Yang, B. Peng, A. Mandlekar, E.Akyu¨rek,A.Anandkumar,J.Andreas,I.Mordatch,A.Torralba,and
R.Tan,Y.Chao,B.Y.Lin,L.Liden,K.Lee,J.Gao,L.Zettlemoyer, Y.Zhu,“Pre-trainedlanguagemodelsforinteractivedecision-making,”
D.Fox,andM.Seo,“Latentactionpretrainingfromvideos,”inICLR, inNeurIPS,2022.
2025. [145] A. Zeng, M. Attarian, B. Ichter, K. M. Choromanski, A. Wong,
[124] J. Cen, C. Yu, H. Yuan, Y. Jiang, S. Huang, J. Guo, X. Li, Y. Song, S.Welker,F.Tombari,A.Purohit,M.S.Ryoo,V.Sindhwani,J.Lee,
H.Luo,F.Wang,D.Zhao,andH.Chen,“Worldvla:Towardsautore- V.Vanhoucke,andP.Florence,“Socraticmodels:Composingzero-shot
gressiveactionworldmodel,”CoRR,vol.abs/2506.21539,2025. multimodalreasoningwithlanguage,”inICLR,2023.
[125] Y. Wang, X. Li, W. Wang, J. Zhang, Y. Li, Y. Chen, X. Wang,
[146] I. Singh, V. Blukis, A. Mousavian, A. Goyal, D. Xu, J. Tremblay,
and Z. Zhang, “Unified vision-language-action model,” CoRR, vol.
D.Fox,J.Thomason,andA.Garg,“Progprompt:Generatingsituated
abs/2506.19850,2025.
robottaskplansusinglargelanguagemodels,”inICRA. IEEE,2023,
[126] Y. Ma, D. Chi, S. Wu, Y. Liu, Y. Zhuang, and I. King, “Astra:
pp.11523–11530.
Efficienttransformerarchitectureandcontrastivedynamicslearningfor
[147] S. Vemprala, R. Bonatti, A. Bucker, and A. Kapoor, “Chatgpt
embodiedinstructionfollowing,”inEMNLP,2025.
for robotics: Design principles and model abilities,” CoRR, vol.
[127] C. Qu, S. Dai, X. Wei, H. Cai, S. Wang, D. Yin, J. Xu, and
abs/2306.17582,2023.
J.Wen,“Toollearningwithlargelanguagemodels:asurvey,”Frontiers
[148] J. Liang, W. Huang, F. Xia, P. Xu, K. Hausman, B. Ichter, P. Flo-
Comput.Sci.,vol.19,no.8,p.198343,2025.
rence,andA.Zeng,“Codeaspolicies:Languagemodelprogramsfor
[128] Y. Jiang, A. Gupta, Z. Zhang, G. Wang, Y. Dou, Y. Chen, L. Fei-
embodiedcontrol,”inICRA. IEEE,2023,pp.9493–9500.
Fei, A. Anandkumar, Y. Zhu, and L. Fan, “VIMA: general robot
[149] Z.Wang,S.Cai,A.Liu,X.Ma,andY.Liang,“Describe,explain,plan
manipulation with multimodal prompts,” CoRR, vol. abs/2210.03094,
and select: Interactive planning with large language models enables
2022.
open-worldmulti-taskagents,”CoRR,vol.abs/2302.01560,2023.
[129] R.Liu,W.Wang,andY.Yang,“Volumetricenvironmentrepresentation
[150] Q. Gu, A. Kuwajerwala, S. Morin, K. M. Jatavallabhula, B. Sen,
for vision-language navigation,”in CVPR. IEEE,2024, pp.16317–
A.Agarwal,C.Rivera,W.Paul,K.Ellis,R.Chellappa,C.Gan,C.M.
16328.
de Melo, J. B. Tenenbaum, A. Torralba, F. Shkurti, and L. Paull,
[130] Y.MaandI.King,“3d-moe:Amixture-of-expertsmulti-modalLLM
“Conceptgraphs:Open-vocabulary3dscenegraphsforperceptionand
for 3d vision and pose diffusion via rectified flow,” CoRR, vol.
planning,”CoRR,vol.abs/2309.16650,2023.
abs/2501.16698,2025.
[151] F. Lin, Y. Hu, P. Sheng, C. Wen, J. You, and Y. Gao, “Data scaling
[131] M. Vecer´ık, C. Doersch, Y. Yang, T. Davchev, Y. Aytar, G. Zhou,
lawsinimitationlearningforroboticmanipulation,”inICLR,2025.
R. Hadsell, L. Agapito, and J. Scholz, “Robotap: Tracking arbitrary
pointsforfew-shotvisualimitation,”inICRA. IEEE,2024,pp.5397– [152] T. Pearce, T. Rashid, D. Bignell, R. Georgescu, S. Devlin, and
5403. K.Hofmann,“Scalinglawsforpre-trainingagentsandworldmodels,”
[132] S. Nasiriany, F. Xia, W. Yu, T. Xiao, J. Liang, I. Dasgupta, A. Xie,
inICML,2025.
D.Driess,A.Wahid,Z.Xu,Q.Vuong,T.Zhang,T.E.Lee,K.Lee, [153] Y. Hong, Z. Zheng, P. Chen, Y. Wang, J. Li, and C. Gan, “Multiply:
P.Xu,S.Kirmani,Y.Zhu,A.Zeng,K.Hausman,N.Heess,C.Finn, A multisensory object-centric embodied large language model in 3d
S. Levine, and B. Ichter, “PIVOT: iterative visual prompting elicits world,”inCVPR. IEEE,2024,pp.26396–26406.
actionableknowledgeforvlms,”inICML,2024. [154] S.S.Raman,V.Cohen,E.Rosen,I.Idrees,D.Paulius,andS.Tellex,
[133] J.Bjorck,F.Castan˜eda,N.Cherniadev,X.Da,R.Ding,Linxi,Y.Fang, “Planning with large language models via corrective re-prompting,”
D. Fox, F. Hu, S. Huang, J. Jang, Z. Jiang, J. Kautz, K. Kundalia, CoRR,vol.abs/2211.09935,2022.
L. Lao, Z. Li, Z. Lin, K. Lin, G. Liu, E. LLontop, L. Magne, [155] P. Zhi, Z. Zhang, M. Han, Z. Zhang, Z. Li, Z. Jiao, B. Jia, and
A.Mandlekar,A.Narayan,S.Nasiriany,S.Reed,Y.L.Tan,G.Wang, S. Huang, “Closed-loop open-vocabulary mobile manipulation with
Z. Wang, J. Wang, Q. Wang, J. Xiang, Y. Xie, Y. Xu, Z. Xu, S. Ye, GPT-4V,”CoRR,vol.abs/2404.10220,2024.
Z.Yu,A.Zhang,H.Zhang,Y.Zhao,R.Zheng,andY.Zhu,“GR00T [156] H. Fang, H. Fang, Z. Tang, J. Liu, C. Wang, J. Wang, H. Zhu, and
N1:anopenfoundationmodelforgeneralisthumanoidrobots,”CoRR, C.Lu,“RH20T:Acomprehensiveroboticdatasetforlearningdiverse
vol.abs/2503.14734,2025. skillsinone-shot,”inICRA. IEEE,2024,pp.653–660.
[134] N. M. Chia-Yu Hung and, H. Deng, L. Renhang, Y. Ang, A. Zadeh, [157] A.Khazatsky,K.Pertsch,S.Nair,A.Balakrishna,S.Dasari,S.Karam-
C. Li, D. Herremans, Z. Wang, and S. Poria, “NORA-1.5: A vision- cheti,S.Nasiriany,M.K.Srirama,L.Y.Chen,K.Ellis,P.D.Fagan,
language-action model trained using world model-, and action-based J.Hejna,M.Itkina,M.Lepert,Y.J.Ma,P.T.Miller,J.Wu,S.Belkhale,
preferencerewards,”CoRR,vol.abs/2511.14659,2025. S.Dass,H.Ha,A.Jain,A.Lee,Y.Lee,M.Memmel,S.Park,I.Ra-
[135] P. Z. Yue Liao and, S. Huang, D. Yang, S. Chen, Y. Jiang, H. Yue, dosavovic,K.Wang,A.Zhan,K.Black,C.Chi,K.B.Hatch,S.Lin,
J. Cai, S. Liu, J. Luo, L. Chen, S. Yan, M. Yao, and G. Ren, J. Lu, J. Mercat, A. Rehman, P. R. Sanketi, A. Sharma, C. Simpson,
“Genie envisioner: A unified world foundation platform for robotic, Q.Vuong,H.R.Walke,B.Wulfe,T.Xiao,J.H.Yang,A.Yavary,T.Z.
manipulation,”CoRR,vol.abs/2508.05635,2025. Zhao,C.Agia,R.Baijal,M.G.Castro,D.Chen,Q.Chen,T.Chung,
[136] K.Tian,Y.Jiang,Z.Yuan,B.Peng,andL.Wang,“Visualautoregres- J. Drake, E. P. Foster, and et al., “DROID: A large-scale in-the-wild
sivemodeling:Scalableimagegenerationvianext-scaleprediction,”in robotmanipulationdataset,”CoRR,vol.abs/2403.12945,2024.
NeurIPS,2024. [158] P. Sharma, L. Mohan, L. Pinto, and A. Gupta, “Multiple interactions
[137] X. Zhuang, Y. Xie, Y. Deng, L. Liang, J. Ru, Y. Yin, and Y. Zou, madeeasy(MIME):largescaledemonstrationsdataforimitation,”in
“VARGPT:unifiedunderstandingandgenerationinavisualautoregres- CoRL,vol.87. PMLR,2018,pp.906–915.
sive multimodal large language model,” CoRR, vol. abs/2501.12327, [159] A. Mandlekar, Y. Zhu, A. Garg, J. Booher, M. Spero, A. Tung,
2025. J.Gao,J.Emmons,A.Gupta,E.Orbay,S.Savarese,andL.Fei-Fei,

21
“ROBOTURK: A crowdsourcing platform for robotic skill learning [178] S.James,Z.Ma,D.R.Arrojo,andA.J.Davison,“Rlbench:Therobot
throughimitation,”inCoRL,vol.87. PMLR,2018,pp.879–893. learning benchmark & learning environment,” IEEE Robotics Autom.
[160] S. Dasari, F. Ebert, S. Tian, S. Nair, B. Bucher, K. Schmeckpeper, Lett.,vol.5,no.2,pp.3019–3026,2020.
S. Singh, S. Levine, and C. Finn, “Robonet: Large-scale multi-robot [179] T.Yu,D.Quillen,Z.He,R.Julian,K.Hausman,C.Finn,andS.Levine,
learning,”inCoRL,vol.100. PMLR,2019,pp.885–897. “Meta-world: A benchmark and evaluation for multi-task and meta
[161] D.Kalashnikov,J.Varley,Y.Chebotar,B.Swanson,R.Jonschkowski, reinforcementlearning,”inCoRL,vol.100. PMLR,2019,pp.1094–
C.Finn,S.Levine,andK.Hausman,“Mt-opt:Continuousmulti-task 1100.
robotic reinforcement learning at scale,” CoRR, vol. abs/2104.08212, [180] O.Mees,L.Hermann,E.Rosete-Beas,andW.Burgard,“CALVIN:A
2021. benchmark for language-conditioned policy learning for long-horizon
[162] V.Kumar,R.M.Shah,G.Zhou,V.Moens,V.Caggiano,A.Gupta,and robot manipulation tasks,” IEEE Robotics Autom. Lett., vol. 7, no. 3,
A. Rajeswaran, “Robohive: A unified framework for robot learning,” pp.7327–7334,2022.
inNeurIPS,2023. [181] A. Gupta, V. Kumar, C. Lynch, S. Levine, and K. Hausman, “Relay
[163] F.Ebert,Y.Yang,K.Schmeckpeper,B.Bucher,G.Georgakis,K.Dani- policylearning:Solvinglong-horizontasksviaimitationandreinforce-
ilidis,C.Finn,andS.Levine,“Bridgedata:Boostinggeneralizationof mentlearning,”inCoRL,vol.100. PMLR,2019,pp.1025–1037.
roboticskillswithcross-domaindatasets,”inRSS,2022. [182] M. Savva, J. Malik, D. Parikh, D. Batra, A. Kadian, O. Maksymets,
[164] S. Srivastava, C. Li, M. Lingelbach, R. Mart´ın-Mart´ın, F. Xia, K. E. Y.Zhao,E.Wijmans,B.Jain,J.Straub,J.Liu,andV.Koltun,“Habitat:
Vainio, Z. Lian, C. Gokmen, S. Buch, C. K. Liu, S. Savarese, A platform for embodied AI research,” in ICCV. IEEE, 2019, pp.
H. Gweon, J. Wu, and L. Fei-Fei, “BEHAVIOR: benchmark for 9338–9346.
everyday household activities in virtual, interactive, and ecological [183] A.Szot,A.Clegg,E.Undersander,E.Wijmans,Y.Zhao,J.M.Turner,
environments,”inCoRL,vol.164. PMLR,2021,pp.477–490. N.Maestre,M.Mukadam,D.S.Chaplot,O.Maksymets,A.Gokaslan,
[165] C.Li,F.Xia,R.Mart´ın-Mart´ın,M.Lingelbach,S.Srivastava,B.Shen, V. Vondrus, S. Dharur, F. Meier, W. Galuba, A. X. Chang, Z. Kira,
K.E.Vainio,C.Gokmen,G.Dharan,T.Jain,A.Kurenkov,C.K.Liu, V. Koltun, J. Malik, M. Savva, and D. Batra, “Habitat 2.0: Training
H. Gweon, J. Wu, L. Fei-Fei, and S. Savarese, “igibson 2.0: Object- homeassistantstorearrangetheirhabitat,”inNeurIPS,2021,pp.251–
centricsimulationforrobotlearningofeverydayhouseholdtasks,”in 266.
CoRL,vol.164. PMLR,2021,pp.455–465. [184] D. Batra, A. X. Chang, S. Chernova, A. J. Davison, J. Deng,
[166] F.Xia,A.R.Zamir,Z.He,A.Sax,J.Malik,andS.Savarese,“Gibson V. Koltun, S. Levine, J. Malik, I. Mordatch, R. Mottaghi, M. Savva,
env:Real-worldperceptionforembodiedagents,”inCVPR. Computer andH.Su,“Rearrangement:AchallengeforembodiedAI,”CoRR,vol.
VisionFoundation/IEEEComputerSociety,2018,pp.9068–9079. abs/2011.01975,2020.
[167] F. Xia, W. B. Shen, C. Li, P. Kasimbeg, M. Tchapmi, A. Toshev,
[185] S.Yenamandra,A.Ramachandran,K.Yadav,A.S.Wang,M.Khanna,
R.Mart´ın-Mart´ın,andS.Savarese,“Interactivegibsonbenchmark:A
T.Gervet,T.Yang,V.Jain,A.Clegg,J.M.Turner,Z.Kira,M.Savva,
benchmarkforinteractivenavigationinclutteredenvironments,”IEEE
A. X. Chang, D. S. Chaplot, D. Batra, R. Mottaghi, Y. Bisk, and
RoboticsAutom.Lett.,vol.5,no.2,pp.713–720,2020.
C. Paxton, “Homerobot: Open-vocabulary mobile manipulation,” in
[168] B.Shen,F.Xia,C.Li,R.Mart´ın-Mart´ın,L.Fan,G.Wang,C.Pe´rez-
CoRL,vol.229. PMLR,2023,pp.1975–2011.
D’Arpino,S.Buch,S.Srivastava,L.Tchapmi,M.Tchapmi,K.Vainio,
[186] M.Shridhar,J.Thomason,D.Gordon,Y.Bisk,W.Han,R.Mottaghi,
J. Wong, L. Fei-Fei, and S. Savarese, “igibson 1.0: A simulation
L.Zettlemoyer,andD.Fox,“ALFRED:Abenchmarkforinterpreting
environment for interactive tasks in large realistic scenes,” in IROS.
groundedinstructionsforeverydaytasks,”inCVPR. ComputerVision
IEEE,2021,pp.7520–7527.
Foundation/IEEE,2020,pp.10737–10746.
[169] C.Li,R.Zhang,J.Wong,C.Gokmen,S.Srivastava,R.Mart´ın-Mart´ın,
[187] Y.Tassa,Y.Doron,A.Muldal,T.Erez,Y.Li,D.deLasCasas,D.Bud-
C. Wang, G. Levine, W. Ai, B. Martinez, H. Yin, M. Lingelbach,
den,A.Abdolmaleki,J.Merel,A.Lefrancq,T.P.Lillicrap,andM.A.
M. Hwang, A. Hiranaka, S. Garlanka, A. Aydin, S. Lee, J. Sun,
Riedmiller, “Deepmind control suite,” CoRR, vol. abs/1801.00690,
M. Anvari, M. Sharma, D. Bansal, S. Hunter, K. Kim, A. Lou,
2018.
C.R.Matthews,I.Villa-Renteria,J.H.Tang,C.Tang,F.Xia,Y.Li,
[188] G. Brockman, V. Cheung, L. Pettersson, J. Schneider, J. Schulman,
S.Savarese,H.Gweon,C.K.Liu,J.Wu,andL.Fei-Fei,“BEHAVIOR-
J.Tang,andW.Zaremba,“Openaigym,”CoRR,vol.abs/1606.01540,
1K:Ahuman-centered,embodiedAIbenchmarkwith1,000everyday
2016.
activitiesandrealisticsimulation,”CoRR,vol.abs/2403.09227,2024.
[189] G. Authors, “Genesis: A universal and generative physics engine
[170] F. Xiang, Y. Qin, K. Mo, Y. Xia, H. Zhu, F. Liu, M. Liu, H. Jiang,
for robotics and beyond,” December 2024. [Online]. Available:
Y. Yuan, H. Wang, L. Yi, A. X. Chang, L. J. Guibas, and H. Su,
https://github.com/Genesis-Embodied-AI/Genesis
“SAPIEN:Asimulatedpart-basedinteractiveenvironment,”inCVPR.
[190] Y. Wang, Z. Xian, F. Chen, T. Wang, Y. Wang, K. Fragkiadaki,
ComputerVisionFoundation/IEEE,2020,pp.11094–11104.
Z. Erickson, D. Held, and C. Gan, “Robogen: Towards unleashing
[171] X. Li, K. Hsu, J. Gu, K. Pertsch, O. Mees, H. R. Walke, C. Fu,
infinite data for automated robot learning via generative simulation,”
I. Lunawat, I. Sieh, S. Kirmani, S. Levine, J. Wu, C. Finn, H. Su,
inICML,2024.
Q. Vuong, and T. Xiao, “Evaluating real-world robot manipulation
policiesinsimulation,”CoRR,vol.abs/2405.05941,2024. [191] M. Ahn, D. Dwibedi, C. Finn, M. G. Arenas, K. Gopalakrishnan,
[172] E.Kolve,R.Mottaghi,D.Gordon,Y.Zhu,A.Gupta,andA.Farhadi, K. Hausman, B. Ichter, A. Irpan, N. J. Joshi, R. Julian, S. Kirmani,
“AI2-THOR:aninteractive3denvironmentforvisualAI,”CoRR,vol. I.Leal,T.E.Lee,S.Levine,Y.Lu,S.Maddineni,K.Rao,D.Sadigh,
abs/1712.05474,2017. P.Sanketi,P.Sermanet,Q.Vuong,S.Welker,F.Xia,T.Xiao,P.Xu,
[173] K. Ehsani, W. Han, A. Herrasti, E. VanderBilt, L. Weihs, E. Kolve, S.Xu,andZ.Xu,“Autort:Embodiedfoundationmodelsforlargescale
A.Kembhavi,andR.Mottaghi,“Manipulathor:Aframeworkforvisual
orchestrationofroboticagents,”CoRR,vol.abs/2401.12963,2024.
objectmanipulation,”inCVPR. ComputerVisionFoundation/IEEE, [192] T. Xiao, H. Chan, P. Sermanet, A. Wahid, A. Brohan, K. Hausman,
2021,pp.4497–4506. S. Levine, and J. Tompson, “Robotic skill acquisition via instruction
[174] L. Weihs, M. Deitke, A. Kembhavi, and R. Mottaghi, “Visual room augmentationwithvision-languagemodels,”inRSS,2023.
rearrangement,”inCVPR. ComputerVisionFoundation/IEEE,2021, [193] Y. Ma, D. Chi, J. Li, K. Song, Y. Zhuang, and I. King, “VOLTA:
pp.5922–5931. improvinggenerativediversitybyvariationalmutualinformationmax-
[175] K.Mirakhor,S.Ghosh,D.Das,andB.Bhowmick,“Taskplanningfor imizingautoencoder,”inNAACL-HLT(Findings),2024.
visualroomrearrangementunderpartialobservability,”inICLR,2024. [194] C.Chi,Z.Xu,C.Pan,E.Cousineau,B.Burchfiel,S.Feng,R.Tedrake,
[176] X.Puig,K.Ra,M.Boben,J.Li,T.Wang,S.Fidler,andA.Torralba, and S. Song, “Universal manipulation interface: In-the-wild robot
“Virtualhome:Simulatinghouseholdactivitiesviaprograms,”in2018 teachingwithoutin-the-wildrobots,”inRSS,2024.
IEEEConferenceonComputerVisionandPatternRecognition,CVPR [195] G.Moon,S.Saito,W.Xu,R.Joshi,J.Buffalini,H.Bellan,N.Rosen,
2018,SaltLakeCity,UT,USA,June18-22,2018. ComputerVision J. Richardson, M. Mize, P. de Bree, T. Simon, B. Peng, S. Garg,
Foundation/IEEEComputerSociety,2018,pp.8494–8502. K. McPhail, and T. Shiratori, “A dataset of relighted 3d interacting
[177] C. Gan, J. Schwartz, S. Alter, D. Mrowca, M. Schrimpf, J. Traer, hands,”inNeurIPS,2023.
J. D. Freitas, J. Kubilius, A. Bhandwaldar, N. Haber, M. Sano, [196] Y.Chen,Y.Ge,Y.Ge,M.Ding,B.Li,R.Wang,R.Xu,Y.Shan,and
K.Kim,E.Wang,M.Lingelbach,A.Curtis,K.T.Feigelis,D.Bear, X.Liu,“Egoplan-bench:Benchmarkingegocentricembodiedplanning
D. Gutfreund, D. D. Cox, A. Torralba, J. J. DiCarlo, J. Tenenbaum, withmultimodallargelanguagemodels,”CoRR,vol.abs/2312.06722,
J. H. McDermott, and D. Yamins, “Threedworld: A platform for 2023.
interactivemulti-modalphysicalsimulation,”inNeurIPSDatasetsand [197] K. Valmeekam, M. Marquez, A. O. Hernandez, S. Sreedharan, and
Benchmarks,2021. S.Kambhampati,“Planbench:Anextensiblebenchmarkforevaluating

22
large language models on planning and reasoning about change,” in [220] A. Kirillov, E. Mintun, N. Ravi, H. Mao, C. Rolland, L. Gustafson,
NeurIPS,2023. T.Xiao,S.Whitehead,A.C.Berg,W.Lo,P.Dolla´r,andR.B.Girshick,
[198] K. Valmeekam, M. Marquez, S. Sreedharan, and S. Kambhampati, “Segmentanything,”CoRR,vol.abs/2304.02643,2023.
“On the planning abilities of large language models - A critical [221] S.HochreiterandJ.Schmidhuber,“Longshort-termmemory,”Neural
investigation,”inNeurIPS,2023. Comput.,vol.9,no.8,pp.1735–1780,1997.
[199] J.Choi,Y.Yoon,H.Ong,J.Kim,andM.Jang,“Lota-bench:Bench- [222] K.Cho,B.vanMerrienboer,C¸.Gu¨lc¸ehre,D.Bahdanau,F.Bougares,
markinglanguage-orientedtaskplannersforembodiedagents,”CoRR, H. Schwenk, and Y. Bengio, “Learning phrase representations using
vol.abs/2402.08178,2024. RNNencoder-decoderforstatisticalmachinetranslation,”inEMNLP.
[200] M.Li,S.Zhao,Q.Wang,K.Wang,Y.Zhou,S.Srivastava,C.Gokmen, ACL,2014,pp.1724–1734.
T.Lee,L.E.Li,R.Zhang,W.Liu,P.Liang,L.Fei-Fei,J.Mao,and [223] OpenAI. (2023) Introducing chatgpt. [Online]. Available: https:
J. Wu, “Embodied agent interface: Benchmarking llms for embodied //openai.com/blog/chatgpt
decisionmaking,”inNeurIPS,2024. [224] D. Silver, A. Huang, C. J. Maddison, A. Guez, L. Sifre, G. van den
[201] A.Das,S.Datta,G.Gkioxari,S.Lee,D.Parikh,andD.Batra,“Em- Driessche, J. Schrittwieser, I. Antonoglou, V. Panneershelvam,
bodiedquestionanswering,”inCVPR. ComputerVisionFoundation M. Lanctot, S. Dieleman, D. Grewe, J. Nham, N. Kalchbrenner,
/IEEEComputerSociety,2018,pp.1–10. I. Sutskever, T. P. Lillicrap, M. Leach, K. Kavukcuoglu, T. Graepel,
[202] D. Gordon, A. Kembhavi, M. Rastegari, J. Redmon, D. Fox, and andD.Hassabis,“Masteringthegameofgowithdeepneuralnetworks
A. Farhadi, “IQA: visual question answering in interactive environ- andtreesearch,”Nat.,vol.529,no.7587,pp.484–489,2016.
ments,” in CVPR. Computer Vision Foundation / IEEE Computer [225] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov,
Society,2018,pp.4089–4098. “Proximalpolicyoptimizationalgorithms,”CoRR,vol.abs/1707.06347,
[203] L. Yu, X. Chen, G. Gkioxari, M. Bansal, T. L. Berg, and D. Batra, 2017.
“Multi-target embodied question answering,” in CVPR. Computer [226] OpenAI, M. Andrychowicz, B. Baker, M. Chociej, R. Jo´zefowicz,
VisionFoundation/IEEE,2019,pp.6309–6318. B. McGrew, J. Pachocki, A. Petron, M. Plappert, G. Powell,
A. Ray, J. Schneider, S. Sidor, J. Tobin, P. Welinder, L. Weng, and
[204] E. Wijmans, S. Datta, O. Maksymets, A. Das, G. Gkioxari, S. Lee,
W. Zaremba, “Learning dexterous in-hand manipulation,” CoRR, vol.
I. Essa, D. Parikh, and D. Batra, “Embodied question answering in
abs/1808.00177,2018.
photorealistic environments with point cloud perception,” in CVPR.
ComputerVisionFoundation/IEEE,2019,pp.6659–6668. [227] R. Rafailov, A. Sharma, E. Mitchell, C. D. Manning, S. Ermon, and
C. Finn, “Direct preference optimization: Your language model is
[205] C.Fan,“Egovqa-anegocentricvideoquestionansweringbenchmark
secretlyarewardmodel,”inNeurIPS,2023.
dataset,”inICCVWorkshops. IEEE,2019,pp.4359–4366.
[228] X.Chen,H.Fang,T.Lin,R.Vedantam,S.Gupta,P.Dolla´r,andC.L.
[206] B.Jia,T.Lei,S.Zhu,andS.Huang,“Egotaskqa:Understandinghuman
Zitnick, “Microsoft COCO captions: Data collection and evaluation
tasksinegocentricvideos,”inNeurIPS,2022.
server,”CoRR,vol.abs/1504.00325,2015.
[207] M. M. Islam, A. Gladstone, R. Islam, and T. Iqbal, “EQA-MX:
[229] S. Antol, A. Agrawal, J. Lu, M. Mitchell, D. Batra, C. L. Zitnick,
embodiedquestionansweringusingmultimodalexpression,”inICLR,
and D. Parikh, “VQA: visual question answering,” in ICCV. IEEE
2024.
ComputerSociety,2015,pp.2425–2433.
[208] A.Majumdar,A.Ajay,X.Zhang,P.Putta,S.Yenamandra,M.Henaff,
[230] L. Yu, P. Poirson, S. Yang, A. C. Berg, and T. L. Berg, “Modeling
S. Silwal, P. Mcvay, O. Maksymets, S. Arnaud, K. Yadav, Q. Li,
context in referring expressions,” in ECCV (2), ser. Lecture Notes in
B. Newman, M. Sharma, V. Berges, S. Zhang, P. Agrawal, Y. Bisk,
ComputerScience,vol.9906. Springer,2016,pp.69–85.
D. Batra, M. Kalakrishnan, F. Meier, C. Paxton, S. Sax, and A. Ra-
[231] O. Vinyals, A. Toshev, S. Bengio, and D. Erhan, “Show and tell: A
jeswaran, “OpenEQA: Embodied Question Answering in the Era of
neuralimagecaptiongenerator,”inCVPR. IEEEComputerSociety,
FoundationModels,”inCVPR,2024.
2015,pp.3156–3164.
[209] R. Girdhar, A. El-Nouby, Z. Liu, M. Singh, K. V. Alwala, A. Joulin,
[232] A.Radford,K.Narasimhan,T.Salimans,andI.Sutskever,“Improving
and I. Misra, “Imagebind one embedding space to bind them all,” in
language understanding by generative pre-training,” OpenAI blog,
CVPR. IEEE,2023,pp.15180–15190.
2018.
[210] B.Zhu,B.Lin,M.Ning,Y.Yan,J.Cui,H.Wang,Y.Pang,W.Jiang,
[233] J. Lu, D. Batra, D. Parikh, and S. Lee, “Vilbert: Pretraining task-
J.Zhang,Z.Li,C.Zhang,Z.Li,W.Liu,andL.Yuan,“Languagebind:
agnosticvisiolinguisticrepresentationsforvision-and-languagetasks,”
Extendingvideo-languagepretrainington-modalitybylanguage-based
inNeurIPS,2019,pp.13–23.
semanticalignment,”inICLR,2024.
[234] J.Alayrac,J.Donahue,P.Luc,A.Miech,I.Barr,Y.Hasson,K.Lenc,
[211] I.Gu¨zey,B.Evans,S.Chintala,andL.Pinto,“Dexterityfromtouch:
A. Mensch, K. Millican, M. Reynolds, R. Ring, E. Rutherford,
Self-supervised pre-training of tactile representations with robotic
S.Cabi,T.Han,Z.Gong,S.Samangooei,M.Monteiro,J.L.Menick,
play,”inCoRL,vol.229. PMLR,2023,pp.3142–3166.
S.Borgeaud,A.Brock,A.Nematzadeh,S.Sharifzadeh,M.Binkowski,
[212] R.Zhang,A.Saran,B.Liu,Y.Zhu,S.Guo,S.Niekum,D.Ballard,and R.Barreira,O.Vinyals,A.Zisserman,andK.Simonyan,“Flamingo:
M.Hayhoe,“Humangazeassistedartificialintelligence:Areview,”in avisuallanguagemodelforfew-shotlearning,”inNeurIPS,2022.
IJCAI-20,72020,pp.4951–4958,surveytrack.
[235] A. Khan, A. Sohail, U. Zahoora, and A. S. Qureshi, “A survey of
[213] R. Zhang, Z. Liu, L. Zhang, J. A. Whritner, K. S. Muller, M. M. therecentarchitecturesofdeepconvolutionalneuralnetworks,”Artif.
Hayhoe,andD.H.Ballard,“AGIL:learningattentionfromhumanfor Intell.Rev.,vol.53,no.8,pp.5455–5516,2020.
visuomotor tasks,” in ECCV (11), vol. 11215. Springer, 2018, pp. [236] S. H. Khan, M. Naseer, M. Hayat, S. W. Zamir, F. S. Khan, and
692–707. M. Shah, “Transformers in vision: A survey,” ACM Comput. Surv.,
[214] A.Saran,R.Zhang,E.S.Short,andS.Niekum,“Efficientlyguiding vol.54,no.10s,pp.200:1–200:41,2022.
imitationlearningagentswithhumangaze,”inAAMAS. ACM,2021, [237] Y.LeCun,B.E.Boser,J.S.Denker,D.Henderson,R.E.Howard,W.E.
pp.1109–1117. Hubbard, and L. D. Jackel, “Backpropagation applied to handwritten
[215] S. Guo, R. Zhang, B. Liu, Y. Zhu, D. H. Ballard, M. M. Hayhoe, zip code recognition,” Neural Comput., vol. 1, no. 4, pp. 541–551,
andP.Stone,“Machineversushumanattentionindeepreinforcement 1989.
learningtasks,”inNeurIPS,2021,pp.25370–25385. [238] K. Simonyan and A. Zisserman, “Very deep convolutional networks
[216] H. M. Le, T. N. Do, and S. J. Phee, “A survey on actuators-driven forlarge-scaleimagerecognition,”inICLR,2015.
surgicalrobots,”SensorsandActuatorsA-physical,vol.247,pp.323– [239] C. Szegedy, W. Liu, Y. Jia, P. Sermanet, S. E. Reed, D. Anguelov,
354,2016. D. Erhan, V. Vanhoucke, and A. Rabinovich, “Going deeper with
[217] M. S. Laursen, J. S. Pedersen, S. A. Just, T. R. Savarimuthu, convolutions,”inCVPR. IEEEComputerSociety,2015,pp.1–9.
B.Blomholt,J.K.H.Andersen,andP.J.Vinholt,“Factorsfacilitating [240] C. Szegedy, S. Ioffe, V. Vanhoucke, and A. A. Alemi, “Inception-v4,
theacceptanceofdiagnosticrobotsinhealthcare:Asurvey,”inICHI. inception-resnet and the impact of residual connections on learning,”
IEEE,2022,pp.442–448. inAAAI. AAAIPress,2017,pp.4278–4284.
[218] K.He,X.Zhang,S.Ren,andJ.Sun,“Deepresiduallearningforimage [241] S.Xie,R.B.Girshick,P.Dolla´r,Z.Tu,andK.He,“Aggregatedresidual
recognition,”inCVPR. IEEEComputerSociety,2016,pp.770–778. transformationsfordeepneuralnetworks,”inCVPR. IEEEComputer
[219] A. Dosovitskiy, L. Beyer, A. Kolesnikov, D. Weissenborn, X. Zhai, Society,2017,pp.5987–5995.
T. Unterthiner, M. Dehghani, M. Minderer, G. Heigold, S. Gelly, [242] J. Hu, L. Shen, and G. Sun, “Squeeze-and-excitation networks,” in
J. Uszkoreit, and N. Houlsby, “An image is worth 16x16 words: CVPR. ComputerVisionFoundation/IEEEComputerSociety,2018,
Transformersforimagerecognitionatscale,”inICLR,2021. pp.7132–7141.

23
[243] M. Tan and Q. V. Le, “Efficientnet: Rethinking model scaling for [268] J.L.Elman,“Findingstructureintime,”Cogn.Sci.,vol.14,no.2,pp.
convolutionalneuralnetworks,”inICML,vol.97. PMLR,2019,pp. 179–211,1990.
6105–6114. [269] D.Bahdanau,K.Cho,andY.Bengio,“Neuralmachinetranslationby
[244] R. B. Girshick, J. Donahue, T. Darrell, and J. Malik, “Rich feature jointlylearningtoalignandtranslate,”inICLR,2015.
hierarchies for accurate object detection and semantic segmentation,” [270] Z. Huang, W. Xu, and K. Yu, “Bidirectional LSTM-CRF models for
inCVPR. IEEEComputerSociety,2014,pp.580–587. sequencetagging,”CoRR,vol.abs/1508.01991,2015.
[245] R. B. Girshick, “Fast R-CNN,” in ICCV. IEEE Computer Society, [271] M. E. Peters, M. Neumann, M. Iyyer, M. Gardner, C. Clark, K. Lee,
2015,pp.1440–1448. and L. Zettlemoyer, “Deep contextualized word representations,” in
[246] S. Ren, K. He, R. B. Girshick, and J. Sun, “Faster R-CNN: towards NAACL-HLT. Association for Computational Linguistics, 2018, pp.
real-time object detection with region proposal networks,” in NIPS, 2227–2237.
2015,pp.91–99. [272] J.HowardandS.Ruder,“Universallanguagemodelfine-tuningfortext
[247] K.He,G.Gkioxari,P.Dolla´r,andR.B.Girshick,“MaskR-CNN,”in classification,”inACL(1). AssociationforComputationalLinguistics,
ICCV. IEEEComputerSociety,2017,pp.2980–2988. 2018,pp.328–339.
[248] J. Redmon, S. K. Divvala, R. B. Girshick, and A. Farhadi, “You [273] Y.Kim,“Convolutionalneuralnetworksforsentenceclassification,”in
onlylookonce:Unified,real-timeobjectdetection,”inCVPR. IEEE EMNLP. ACL,2014,pp.1746–1751.
ComputerSociety,2016,pp.779–788. [274] X. Zhang, J. J. Zhao, and Y. LeCun, “Character-level convolutional
[249] T. Lin, P. Dolla´r, R. B. Girshick, K. He, B. Hariharan, and S. J. networksfortextclassification,”inNIPS,2015,pp.649–657.
Belongie,“Featurepyramidnetworksforobjectdetection,”inCVPR. [275] X. Ma and E. H. Hovy, “End-to-end sequence labeling via bi-
IEEEComputerSociety,2017,pp.936–944. directionallstm-cnns-crf,”inACL(1). TheAssociationforComputer
[250] T.Lin,P.Goyal,R.B.Girshick,K.He,andP.Dolla´r,“Focallossfor Linguistics,2016.
denseobjectdetection,”inICCV. IEEEComputerSociety,2017,pp. [276] A.Radford,J.Wu,R.Child,D.Luan,D.Amodei,I.Sutskeveretal.,
2999–3007. “Languagemodelsareunsupervisedmultitasklearners,”OpenAIblog,
[251] P.Anderson,X.He,C.Buehler,D.Teney,M.Johnson,S.Gould,and vol.1,no.8,p.9,2019.
L.Zhang,“Bottom-upandtop-downattentionforimagecaptioningand [277] T.B.Brown,B.Mann,N.Ryder,M.Subbiah,J.Kaplan,P.Dhariwal,
visualquestionanswering,”inCVPR. ComputerVisionFoundation/ A. Neelakantan, P. Shyam, G. Sastry, A. Askell et al., “Language
IEEEComputerSociety,2018,pp.6077–6086. modelsarefew-shotlearners,”arXivpreprintarXiv:2005.14165,2020.
[252] J. Long, E. Shelhamer, and T. Darrell, “Fully convolutional networks [278] OpenAI,“GPT-4technicalreport,”CoRR,vol.abs/2303.08774,2023.
forsemanticsegmentation,”inCVPR. IEEEComputerSociety,2015, [279] Y.Liu,M.Ott,N.Goyal,J.Du,M.Joshi,D.Chen,O.Levy,M.Lewis,
pp.3431–3440. L.Zettlemoyer,andV.Stoyanov,“Roberta:ArobustlyoptimizedBERT
[253] V. Badrinarayanan, A. Kendall, and R. Cipolla, “Segnet: A deep pretrainingapproach,”CoRR,vol.abs/1907.11692,2019.
convolutional encoder-decoder architecture for image segmentation,” [280] Z.Lan,M.Chen,S.Goodman,K.Gimpel,P.Sharma,andR.Soricut,
IEEE Trans. Pattern Anal. Mach. Intell., vol. 39, no. 12, pp. 2481– “ALBERT: A lite BERT for self-supervised learning of language
2495,2017. representations,”inICLR,2020.
[254] O. Ronneberger, P. Fischer, and T. Brox, “U-net: Convolutional net- [281] K. Clark, M. Luong, Q. V. Le, and C. D. Manning, “ELECTRA:
worksforbiomedicalimagesegmentation,”inMICCAI(3),ser.Lecture pre-trainingtextencodersasdiscriminatorsratherthangenerators,”in
NotesinComputerScience,vol.9351. Springer,2015,pp.234–241. ICLR,2020.
[255] N. Carion, F. Massa, G. Synnaeve, N. Usunier, A. Kirillov, and [282] Z. Yang, Z. Dai, Y. Yang, J. G. Carbonell, R. Salakhutdinov, and
S. Zagoruyko, “End-to-end object detection with transformers,” in Q.V.Le,“Xlnet:Generalizedautoregressivepretrainingforlanguage
ECCV (1), ser. Lecture Notes in Computer Science, vol. 12346. understanding,”inNeurIPS,2019,pp.5754–5764.
Springer,2020,pp.213–229. [283] S. Zhang, S. Roller, N. Goyal, M. Artetxe, M. Chen, S. Chen,
[256] R. Strudel, R. G. Pinel, I. Laptev, and C. Schmid, “Segmenter: C. Dewan, M. T. Diab, X. Li, X. V. Lin, T. Mihaylov, M. Ott,
Transformer for semantic segmentation,” in ICCV. IEEE, 2021, pp. S.Shleifer,K.Shuster,D.Simig,P.S.Koura,A.Sridhar,T.Wang,and
7242–7252. L.Zettlemoyer,“OPT:openpre-trainedtransformerlanguagemodels,”
[257] A. Ioannidou, E. Chatzilari, S. Nikolopoulos, and I. Kompatsiaris, CoRR,vol.abs/2205.01068,2022.
“Deeplearningadvancesincomputervisionwith3ddata:Asurvey,” [284] M.Lewis,Y.Liu,N.Goyal,M.Ghazvininejad,A.Mohamed,O.Levy,
ACMComput.Surv.,vol.50,no.2,pp.20:1–20:38,2017. V. Stoyanov, and L. Zettlemoyer, “BART: denoising sequence-to-
[258] E.Ahmed,A.Saint,A.E.R.Shabayek,K.Cherenkova,R.Das,G.Gu- sequencepre-trainingfornaturallanguagegeneration,translation,and
sev,D.Aouada,andB.E.Ottersten,“Deeplearningadvancesondif- comprehension,”inACL. AssociationforComputationalLinguistics,
ferent3ddatarepresentations:Asurvey,”CoRR,vol.abs/1808.01462, 2020,pp.7871–7880.
2018. [285] C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena,
[259] Y.Guo,H.Wang,Q.Hu,H.Liu,L.Liu,andM.Bennamoun,“Deep Y.Zhou,W.Li,andP.J.Liu,“Exploringthelimitsoftransferlearning
learning for 3d point clouds: A survey,” IEEE Trans. Pattern Anal. withaunifiedtext-to-texttransformer,”J.Mach.Learn.Res.,vol.21,
Mach.Intell.,vol.43,no.12,pp.4338–4364,2021. pp.140:1–140:67,2020.
[260] C. R. Qi, H. Su, M. Nießner, A. Dai, M. Yan, and L. J. Guibas, [286] A.Chowdhery,S.Narang,J.Devlin,M.Bosma,G.Mishra,A.Roberts,
“Volumetricandmulti-viewcnnsforobjectclassificationon3ddata,” P. Barham, H. W. Chung, C. Sutton, S. Gehrmann, P. Schuh, K. Shi,
inCVPR. IEEEComputerSociety,2016,pp.5648–5656. S.Tsvyashchenko,J.Maynez,A.Rao,P.Barnes,Y.Tay,N.Shazeer,
[261] Y.Feng,Y.Feng,H.You,X.Zhao,andY.Gao,“Meshnet:Meshneural V.Prabhakaran,E.Reif,N.Du,B.Hutchinson,R.Pope,J.Bradbury,
network for 3d shape representation,” in AAAI. AAAI Press, 2019, J. Austin, M. Isard, G. Gur-Ari, P. Yin, T. Duke, A. Levskaya,
pp.8279–8286. S.Ghemawat,S.Dev,H.Michalewski,X.Garcia,V.Misra,K.Robin-
[262] D. W. Otter, J. R. Medina, and J. K. Kalita, “A survey of the usages son, L. Fedus, D. Zhou, D. Ippolito, D. Luan, H. Lim, B. Zoph,
ofdeeplearningfornaturallanguageprocessing,”IEEETrans.Neural A.Spiridonov,R.Sepassi,D.Dohan,S.Agrawal,M.Omernick,A.M.
NetworksLearn.Syst.,vol.32,no.2,pp.604–624,2021. Dai, T. S. Pillai, M. Pellat, A. Lewkowycz, E. Moreira, R. Child,
[263] P. Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi, and G. Neubig, “Pre- O. Polozov, K. Lee, Z. Zhou, X. Wang, B. Saeta, M. Diaz, O. Firat,
train,prompt,andpredict:Asystematicsurveyofpromptingmethods M.Catasta,J.Wei,K.Meier-Hellstern,D.Eck,J.Dean,S.Petrov,and
in natural language processing,” ACM Comput. Surv., vol. 55, no. 9, N.Fiedel,“Palm:Scalinglanguagemodelingwithpathways,”J.Mach.
pp.195:1–195:35,2023. Learn.Res.,vol.24,pp.240:1–240:113,2023.
[264] Y. Bengio, R. Ducharme, and P. Vincent, “A neural probabilistic [287] R. Anil, A. M. Dai, O. Firat, M. Johnson, D. Lepikhin, A. Passos,
languagemodel,”inNIPS. MITPress,2000,pp.932–938. S. Shakeri, E. Taropa, P. Bailey, Z. Chen, E. Chu, J. H. Clark,
[265] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean, L. E. Shafey, Y. Huang, K. Meier-Hellstern, G. Mishra, E. Moreira,
“Distributed representations of words and phrases and their compo- M.Omernick,K.Robinson,S.Ruder,Y.Tay,K.Xiao,Y.Xu,Y.Zhang,
sitionality,”inNIPS,2013,pp.3111–3119. G.H.A´brego,J.Ahn,J.Austin,P.Barham,J.A.Botha,J.Bradbury,
[266] T. Mikolov, K. Chen, G. Corrado, and J. Dean, “Efficient estimation S. Brahma, K. Brooks, M. Catasta, Y. Cheng, C. Cherry, C. A.
ofwordrepresentationsinvectorspace,”inICLR(WorkshopPoster), Choquette-Choo, A. Chowdhery, C. Crepy, S. Dave, M. Dehghani,
2013. S. Dev, J. Devlin, M. D´ıaz, N. Du, E. Dyer, V. Feinberg, F. Feng,
[267] J.Pennington,R.Socher,andC.D.Manning,“Glove:Globalvectors V. Fienber, M. Freitag, X. Garcia, S. Gehrmann, L. Gonzalez, and
forwordrepresentation,”inEMNLP. ACL,2014,pp.1532–1543. etal.,“Palm2technicalreport,”CoRR,vol.abs/2305.10403,2023.

24
[288] H.Touvron,T.Lavril,G.Izacard,X.Martinet,M.Lachaux,T.Lacroix, inforcementlearning,”inICML,ser.JMLRWorkshopandConference
B.Rozie`re,N.Goyal,E.Hambro,F.Azhar,A.Rodriguez,A.Joulin, Proceedings,vol.48. JMLR.org,2016,pp.1928–1937.
E. Grave, and G. Lample, “Llama: Open and efficient foundation [308] S. Gu, T. P. Lillicrap, I. Sutskever, and S. Levine, “Continuous
languagemodels,”CoRR,vol.abs/2302.13971,2023. deep q-learning with model-based acceleration,” in ICML, ser. JMLR
[289] H. Touvron,L. Martin, K.Stone, P. Albert, A. Almahairi,Y. Babaei, WorkshopandConferenceProceedings,vol.48. JMLR.org,2016,pp.
N.Bashlykov,S.Batra,P.Bhargava,S.Bhosale,D.Bikel,L.Blecher, 2829–2838.
C. Canton-Ferrer, M. Chen, G. Cucurull, D. Esiobu, J. Fernandes, [309] T.Haarnoja,A.Zhou,P.Abbeel,andS.Levine,“Softactor-critic:Off-
J.Fu,W.Fu,B.Fuller,C.Gao,V.Goswami,N.Goyal,A.Hartshorn, policymaximumentropydeepreinforcementlearningwithastochastic
S. Hosseini, R. Hou, H. Inan, M. Kardas, V. Kerkez, M. Khabsa, actor,”inICML,vol.80. PMLR,2018,pp.1856–1865.
I.Kloumann,A.Korenev,P.S.Koura,M.Lachaux,T.Lavril,J.Lee, [310] J. Schulman, S. Levine, P. Abbeel, M. I. Jordan, and P. Moritz,
D. Liskovich, Y. Lu, Y. Mao, X. Martinet, T. Mihaylov, P. Mishra, “Trustregionpolicyoptimization,”inICML,ser.JMLRWorkshopand
I.Molybog,Y.Nie,A.Poulton,J.Reizenstein,R.Rungta,K.Saladi, ConferenceProceedings,vol.37. JMLR.org,2015,pp.1889–1897.
A. Schelten, R. Silva, E. M. Smith, R. Subramanian, X. E. Tan, [311] J. Schulman, P. Moritz, S. Levine, M. I. Jordan, and P. Abbeel,
B.Tang,R.Taylor,A.Williams,J.X.Kuan,P.Xu,Z.Yan,I.Zarov, “High-dimensional continuous control using generalized advantage
Y.Zhang,A.Fan,M.Kambadur,S.Narang,A.Rodriguez,R.Stojnic, estimation,”inICLR(Poster),2016.
S.Edunov,andT.Scialom,“Llama2:Openfoundationandfine-tuned [312] J. Ho and S. Ermon, “Generative adversarial imitation learning,” in
chatmodels,”CoRR,vol.abs/2307.09288,2023. NIPS,2016,pp.4565–4573.
[290] Baidu. (2023) Introducing ernie 3.5: Baidu’s knowledge-enhanced [313] L.Pinto,J.Davidson,R.Sukthankar,andA.Gupta,“Robustadversarial
foundation model takes a giant leap forward. [Online]. Available: reinforcementlearning,”inICML,vol.70. PMLR,2017,pp.2817–
http://research.baidu.com/Blog/index-view?id=185 2826.
[291] L.Ouyang,J.Wu,X.Jiang,D.Almeida,C.L.Wainwright,P.Mishkin, [314] P. F. Christiano, J. Leike, T. B. Brown, M. Martic, S. Legg, and
C. Zhang, S. Agarwal, K. Slama, A. Ray, J. Schulman, J. Hilton, D. Amodei, “Deep reinforcement learning from human preferences,”
F.Kelton,L.Miller,M.Simens,A.Askell,P.Welinder,P.F.Christiano, inNIPS,2017,pp.4299–4307.
J.Leike,andR.Lowe,“Traininglanguagemodelstofollowinstructions [315] A. S. Vezhnevets, S. Osindero, T. Schaul, N. Heess, M. Jaderberg,
withhumanfeedback,”inNeurIPS,2022. D. Silver, and K. Kavukcuoglu, “Feudal networks for hierarchical
[292] J.Wei,M.Bosma,V.Y.Zhao,K.Guu,A.W.Yu,B.Lester,N.Du, reinforcementlearning,”inICML,vol.70. PMLR,2017,pp.3540–
A. M. Dai, and Q. V. Le, “Finetuned language models are zero-shot 3549.
learners,”inICLR,2022. [316] S.Levine,C.Finn,T.Darrell,andP.Abbeel,“End-to-endtrainingof
[293] H.W.Chung,L.Hou,S.Longpre,B.Zoph,Y.Tay,W.Fedus,E.Li, deep visuomotor policies,” J. Mach. Learn. Res., vol. 17, pp. 39:1–
X. Wang, M. Dehghani, S. Brahma, A. Webson, S. S. Gu, Z. Dai, 39:40,2016.
M. Suzgun, X. Chen, A. Chowdhery, S. Narang, G. Mishra, A. Yu, [317] D. Kalashnikov, A. Irpan, P. Pastor, J. Ibarz, A. Herzog, E. Jang,
V. Y. Zhao, Y. Huang, A. M. Dai, H. Yu, S. Petrov, E. H. Chi, D.Quillen,E.Holly,M.Kalakrishnan,V.Vanhoucke,andS.Levine,
J.Dean,J.Devlin,A.Roberts,D.Zhou,Q.V.Le,andJ.Wei,“Scaling “Qt-opt:Scalabledeepreinforcementlearningforvision-basedrobotic
instruction-finetuned language models,” CoRR, vol. abs/2210.11416, manipulation,”CoRR,vol.abs/1806.10293,2018.
2022. [318] OpenAI,I.Akkaya,M.Andrychowicz,M.Chociej,M.Litwin,B.Mc-
[294] R.Taori,I.Gulrajani,T.Zhang,Y.Dubois,X.Li,C.Guestrin,P.Liang, Grew,A.Petron,A.Paino,M.Plappert,G.Powell,R.Ribas,J.Schnei-
andT.B.Hashimoto,“Stanfordalpaca:Aninstruction-followingllama der,N.Tezak,J.Tworek,P.Welinder,L.Weng,Q.Yuan,W.Zaremba,
model,”https://github.com/tatsu-lab/stanford alpaca,2023. and L. Zhang, “Solving rubik’s cube with a robot hand,” CoRR, vol.
abs/1910.07113,2019.
[295] W.-L. Chiang, Z. Li, Z. Lin, Y. Sheng, Z. Wu, H. Zhang,
[319] F.Scarselli,M.Gori,A.C.Tsoi,M.Hagenbuchner,andG.Monfardini,
L. Zheng, S. Zhuang, Y. Zhuang, J. E. Gonzalez, I. Stoica, and
“The graph neural network model,” IEEE Trans. Neural Networks,
E. P. Xing, “Vicuna: An open-source chatbot impressing gpt-4
vol.20,no.1,pp.61–80,2009.
with 90%* chatgpt quality,” March 2023. [Online]. Available:
[320] Z. Wu, S. Pan, F. Chen, G. Long, C. Zhang, and P. S. Yu, “A
https://lmsys.org/blog/2023-03-30-vicuna/
comprehensivesurveyongraphneuralnetworks,”IEEETrans.Neural
[296] Y. Li, “Deep reinforcement learning: An overview,” CoRR, vol.
NetworksLearn.Syst.,vol.32,no.1,pp.4–24,2021.
abs/1701.07274,2017.
[321] J. Bruna, W. Zaremba, A. Szlam, and Y. LeCun, “Spectral networks
[297] K. Arulkumaran, M. P. Deisenroth, M. Brundage, and A. A.
andlocallyconnectednetworksongraphs,”inICLR,2014.
Bharath,“Abriefsurveyofdeepreinforcementlearning,”CoRR,vol.
[322] M. Defferrard, X. Bresson, and P. Vandergheynst, “Convolutional
abs/1708.05866,2017.
neural networks on graphs with fast localized spectral filtering,” in
[298] W. Li, H. Luo, Z. Lin, C. Zhang, Z. Lu, and D. Ye, “A survey on
NIPS,2016,pp.3837–3845.
transformers in reinforcement learning,” CoRR, vol. abs/2301.03044,
[323] T.N.KipfandM.Welling,“Semi-supervisedclassificationwithgraph
2023.
convolutionalnetworks,”inICLR(Poster),2017.
[299] H.vanHasselt,A.Guez,andD.Silver,“Deepreinforcementlearning
[324] A. Micheli, “Neural network for graphs: A contextual constructive
withdoubleq-learning,”inAAAI. AAAIPress,2016,pp.2094–2100.
approach,”IEEETrans.NeuralNetworks,vol.20,no.3,pp.498–511,
[300] M.Andrychowicz,D.Crow,A.Ray,J.Schneider,R.Fong,P.Welin-
2009.
der, B. McGrew, J. Tobin, P. Abbeel, and W. Zaremba, “Hindsight
[325] J. Gilmer, S. S. Schoenholz, P. F. Riley, O. Vinyals, and G. E. Dahl,
experiencereplay,”inNIPS,2017,pp.5048–5058.
“Neural message passing for quantum chemistry,” in ICML, vol. 70.
[301] S.Fujimoto,D.Meger,andD.Precup,“Off-policydeepreinforcement PMLR,2017,pp.1263–1272.
learning without exploration,” in ICML, vol. 97. PMLR, 2019, pp. [326] K.Xu,W.Hu,J.Leskovec,andS.Jegelka,“Howpowerfularegraph
2052–2062. neuralnetworks?”inICLR,2019.
[302] A.Kumar,J.Fu,M.Soh,G.Tucker,andS.Levine,“Stabilizingoff- [327] W. L. Hamilton, Z. Ying, and J. Leskovec, “Inductive representation
policyq-learningviabootstrappingerrorreduction,”inNeurIPS,2019, learningonlargegraphs,”inNIPS,2017,pp.1024–1034.
pp.11761–11771. [328] P. Velickovic, G. Cucurull, A. Casanova, A. Romero, P. Lio`, and
[303] A.Kumar,A.Zhou,G.Tucker,andS.Levine,“Conservativeq-learning Y.Bengio,“Graphattentionnetworks,”inICLR(Poster),2018.
forofflinereinforcementlearning,”inNeurIPS,2020. [329] S.Cao,W.Lu,andQ.Xu,“Deepneuralnetworksforlearninggraph
[304] S. Levine and V. Koltun, “Guided policy search,” in ICML (3), ser. representations,”inAAAI. AAAIPress,2016,pp.1145–1152.
JMLR Workshop and Conference Proceedings, vol. 28. JMLR.org, [330] T.N.KipfandM.Welling,“Variationalgraphauto-encoders,”CoRR,
2013,pp.1–9. vol.abs/1611.07308,2016.
[305] D. Silver, G. Lever, N. Heess, T. Degris, D. Wierstra, and M. A. [331] Y.Seo,M.Defferrard,P.Vandergheynst,andX.Bresson,“Structured
Riedmiller, “Deterministic policy gradient algorithms,” in ICML, ser. sequence modeling with graph convolutional recurrent networks,” in
JMLR Workshop and Conference Proceedings, vol. 32. JMLR.org, ICONIP (1), ser. Lecture Notes in Computer Science, vol. 11301.
2014,pp.387–395. Springer,2018,pp.362–373.
[306] T. P. Lillicrap, J. J. Hunt, A. Pritzel, N. Heess, T. Erez, Y. Tassa, [332] W.Du,H.Zhang,Y.Du,Q.Meng,W.Chen,N.Zheng,B.Shao,and
D. Silver, and D. Wierstra, “Continuous control with deep reinforce- T.Liu,“SE(3)equivariantgraphneuralnetworkswithcompletelocal
mentlearning,”inICLR(Poster),2016. frames,”inICML,vol.162. PMLR,2022,pp.5583–5608.
[307] V.Mnih,A.P.Badia,M.Mirza,A.Graves,T.P.Lillicrap,T.Harley, [333] V.G.Satorras,E.Hoogeboom,andM.Welling,“E(n)equivariantgraph
D. Silver, and K. Kavukcuoglu, “Asynchronous methods for deep re- neuralnetworks,”inICML,vol.139. PMLR,2021,pp.9323–9332.

25
[334] Y. Rong, Y. Bian, T. Xu, W. Xie, Y. Wei, W. Huang, and J. Huang, [357] Z. Liu, Y. Lin, Y. Cao, H. Hu, Y. Wei, Z. Zhang, S. Lin, and
“Self-supervised graph transformer on large-scale molecular data,” in B. Guo, “Swin transformer: Hierarchical vision transformer using
NeurIPS,2020. shiftedwindows,”inICCV. IEEE,2021,pp.9992–10002.
[335] F. Fuchs, D. E. Worrall, V. Fischer, and M. Welling, “Se(3)- [358] H.Wu,B.Xiao,N.Codella,M.Liu,X.Dai,L.Yuan,andL.Zhang,
transformers: 3d roto-translation equivariant attention networks,” in “Cvt: Introducing convolutions to vision transformers,” in ICCV.
NeurIPS,2020. IEEE,2021,pp.22–31.
[336] R.Krishna,Y.Zhu,O.Groth,J.Johnson,K.Hata,J.Kravitz,S.Chen, [359] A. Brock, S. De, S. L. Smith, and K. Simonyan, “High-performance
Y.Kalantidis,L.Li,D.A.Shamma,M.S.Bernstein,andL.Fei-Fei, large-scale image recognition without normalization,” in ICML, vol.
“Visualgenome:Connectinglanguageandvisionusingcrowdsourced 139. PMLR,2021,pp.1059–1071.
dense image annotations,” Int. J. Comput. Vis., vol. 123, no. 1, pp. [360] J. Hoffmann, S. Borgeaud, A. Mensch, E. Buchatskaya, T. Cai,
32–73,2017. E.Rutherford,D.deLasCasas,L.A.Hendricks,J.Welbl,A.Clark,
[337] L.Wu,Y.Chen,K.Shen,X.Guo,H.Gao,S.Li,J.Pei,andB.Long, T.Hennigan,E.Noland,K.Millican,G.vandenDriessche,B.Damoc,
“Graph neural networks for natural language processing: A survey,” A.Guy,S.Osindero,K.Simonyan,E.Elsen,J.W.Rae,O.Vinyals,and
Found.TrendsMach.Learn.,vol.16,no.2,pp.119–328,2023. L. Sifre, “Training compute-optimal large language models,” CoRR,
[338] D. Ghosal, N. Majumder, S. Poria, N. Chhaya, and A. F. Gelbukh, vol.abs/2203.15556,2022.
“Dialoguegcn: A graph convolutional neural network for emotion [361] Y. Fang, W. Wang, B. Xie, Q. Sun, L. Wu, X. Wang, T. Huang,
recognition in conversation,” in EMNLP/IJCNLP (1). Association X. Wang, and Y. Cao, “EVA: exploring the limits of masked visual
forComputationalLinguistics,2019,pp.154–164. representationlearningatscale,”inCVPR. IEEE,2023,pp.19358–
[339] W. Zhong, J. Xu, D. Tang, Z. Xu, N. Duan, M. Zhou, J. Wang, and 19369.
J. Yin, “Reasoning over semantic-level graph for fact checking,” in [362] X. Chen, X. Wang, S. Changpinyo, A. J. Piergiovanni, P. Padlewski,
ACL. Association for Computational Linguistics, 2020, pp. 6170– D.Salz,S.Goodman,A.Grycner,B.Mustafa,L.Beyer,A.Kolesnikov,
6180. J.Puigcerver,N.Ding,K.Rong,H.Akbari,G.Mishra,L.Xue,A.V.
[340] L.Wang,Y.Li,O¨.Aslan,andO.Vinyals,“Wikigraphs:Awikipedia Thapliyal,J.Bradbury,andW.Kuo,“Pali:Ajointly-scaledmultilingual
text - knowledge graph paired dataset,” CoRR, vol. abs/2107.09556, language-imagemodel,”inICLR,2023.
2021. [363] L. Xue, N. Constant, A. Roberts, M. Kale, R. Al-Rfou, A. Siddhant,
[341] J. Tang, J. Zhang, L. Yao, J. Li, L. Zhang, and Z. Su, “Arnetminer: A. Barua, and C. Raffel, “mt5: A massively multilingual pre-trained
extractionandminingofacademicsocialnetworks,”inKDD. ACM, text-to-texttransformer,”inNAACL-HLT. AssociationforComputa-
2008,pp.990–998. tionalLinguistics,2021,pp.483–498.
[342] H. Tan and M. Bansal, “LXMERT: learning cross-modality encoder [364] X.Chen,J.Djolonga,P.Padlewski,B.Mustafa,S.Changpinyo,J.Wu,
representationsfromtransformers,”inEMNLP/IJCNLP(1). Associ- C.R.Ruiz,S.Goodman,X.Wang,Y.Tay,S.Shakeri,M.Dehghani,
ationforComputationalLinguistics,2019,pp.5099–5110. D. Salz, M. Lucic, M. Tschannen, A. Nagrani, H. Hu, M. Joshi,
[343] L.H.Li,M.Yatskar,D.Yin,C.Hsieh,andK.Chang,“Visualbert:A B. Pang, C. Montgomery, P. Pietrzyk, M. Ritter, A. J. Piergiovanni,
simple and performant baseline for vision and language,” CoRR, vol. M.Minderer,F.Pavetic,A.Waters,G.Li,I.Alabdulmohsin,L.Beyer,
abs/1908.03557,2019. J.Amelot,K.Lee,A.P.Steiner,Y.Li,D.Keysers,A.Arnab,Y.Xu,
[344] W.Su,X.Zhu,Y.Cao,B.Li,L.Lu,F.Wei,andJ.Dai,“VL-BERT: K. Rong, A. Kolesnikov, M. Seyedhosseini, A. Angelova, X. Zhai,
pre-trainingofgenericvisual-linguisticrepresentations,”inICLR,2020. N.Houlsby,andR.Soricut,“Pali-x:Onscalingupamultilingualvision
[345] Y. Chen, L. Li, L. Yu, A. E. Kholy, F. Ahmed, Z. Gan, Y. Cheng, andlanguagemodel,”CoRR,vol.abs/2305.18565,2023.
and J. Liu, “UNITER: universal image-text representation learning,” [365] M.Dehghani,J.Djolonga,B.Mustafa,P.Padlewski,J.Heek,J.Gilmer,
in ECCV (30), ser. Lecture Notes in Computer Science, vol. 12375. A. Steiner, M. Caron, R. Geirhos, I. Alabdulmohsin, R. Jenatton,
Springer,2020,pp.104–120. L.Beyer,M.Tschannen,A.Arnab,X.Wang,C.Riquelme,M.Min-
[346] W. Kim, B. Son, and I. Kim, “Vilt: Vision-and-language transformer derer, J. Puigcerver, U. Evci, M. Kumar, S. van Steenkiste, G. F.
withoutconvolutionorregionsupervision,”inICML,vol.139. PMLR, Elsayed, A. Mahendran, F. Yu, A. Oliver, F. Huot, J. Bastings,
2021,pp.5583–5594. M. P. Collier, A. A. Gritsenko, V. Birodkar, C. Vasconcelos, Y. Tay,
[347] Z.Wang,J.Yu,A.W.Yu,Z.Dai,Y.Tsvetkov,andY.Cao,“Simvlm: T. Mensink, A. Kolesnikov, F. Pavetic, D. Tran, T. Kipf, M. Lucic,
Simple visual language model pretraining with weak supervision,” in X. Zhai, D. Keysers, J. Harmsen, and N. Houlsby, “Scaling vision
ICLR,2022. transformers to 22 billion parameters,” CoRR, vol. abs/2302.05442,
[348] Z.Dai,H.Liu,Q.V.Le,andM.Tan,“Coatnet:Marryingconvolution 2023.
andattentionforalldatasizes,”inNeurIPS,2021,pp.3965–3977. [366] Y.Tay,M.Dehghani,V.Q.Tran,X.Garcia,J.Wei,X.Wang,H.W.
[349] J.Wang,Z.Yang,X.Hu,L.Li,K.Lin,Z.Gan,Z.Liu,C.Liu,and Chung,D.Bahri,T.Schuster,H.S.Zheng,D.Zhou,N.Houlsby,and
L.Wang,“GIT:Agenerativeimage-to-texttransformerforvisionand D. Metzler, “UL2: unifying language learning paradigms,” in ICLR,
language,”Trans.Mach.Learn.Res.,vol.2022,2022. 2023.
[350] L. Yuan, D. Chen, Y. Chen, N. Codella, X. Dai, J. Gao, H. Hu, [367] R.Zhang,J.Han,A.Zhou,X.Hu,S.Yan,P.Lu,H.Li,P.Gao,and
X.Huang,B.Li,C.Li,C.Liu,M.Liu,Z.Liu,Y.Lu,Y.Shi,L.Wang, Y.Qiao,“Llama-adapter:Efficientfine-tuningoflanguagemodelswith
J.Wang,B.Xiao,Z.Xiao,J.Yang,M.Zeng,L.Zhou,andP.Zhang, zero-initattention,”CoRR,vol.abs/2303.16199,2023.
“Florence:Anewfoundationmodelforcomputervision,”CoRR,vol. [368] P.Gao,J.Han,R.Zhang,Z.Lin,S.Geng,A.Zhou,W.Zhang,P.Lu,
abs/2111.11432,2021. C. He, X. Yue, H. Li, and Y. Qiao, “Llama-adapter V2: parameter-
[351] W.Wang,H.Bao,L.Dong,J.Bjorck,Z.Peng,Q.Liu,K.Aggarwal, efficientvisualinstructionmodel,”CoRR,vol.abs/2304.15010,2023.
O.K.Mohammed,S.Singhal,S.Som,andF.Wei,“Imageasaforeign [369] S. Huang, L. Dong, W. Wang, Y. Hao, S. Singhal, S. Ma, T. Lv,
language: BEIT pretraining for vision and vision-language tasks,” in L. Cui, O. K. Mohammed, B. Patra, Q. Liu, K. Aggarwal, Z. Chi,
CVPR. IEEE,2023,pp.19175–19186. J.Bjorck,V.Chaudhary,S.Som,X.Song,andF.Wei,“Languageis
[352] L. Yao, R. Huang, L. Hou, G. Lu, M. Niu, H. Xu, X. Liang, Z. Li, not all you need: Aligning perception with language models,” CoRR,
X. Jiang, and C. Xu, “FILIP: fine-grained interactive language-image vol.abs/2302.14045,2023.
pre-training,”inICLR,2022. [370] Z. Peng, W. Wang, L. Dong, Y. Hao, S. Huang, S. Ma, and F. Wei,
[353] C. Jia, Y. Yang, Y. Xia, Y. Chen, Z. Parekh, H. Pham, Q. V. Le, “Kosmos-2: Grounding multimodal large language models to the
Y.Sung,Z.Li,andT.Duerig,“Scalingupvisualandvision-language world,”CoRR,vol.abs/2306.14824,2023.
representationlearningwithnoisytextsupervision,”inICML,vol.139. [371] H.Wang,S.Ma,S.Huang,L.Dong,W.Wang,Z.Peng,Y.Wu,P.Ba-
PMLR,2021,pp.4904–4916. jaj,S.Singhal,A.Benhaim,B.Patra,Z.Liu,V.Chaudhary,X.Song,
[354] Q.Xie,M.Luong,E.H.Hovy,andQ.V.Le,“Self-trainingwithnoisy and F. Wei, “Foundation transformers,” CoRR, vol. abs/2210.06423,
studentimprovesimagenetclassification,”inCVPR. ComputerVision 2022.
Foundation/IEEE,2020,pp.10684–10695. [372] W.Dai,J.Li,D.Li,A.M.H.Tiong,J.Zhao,W.Wang,B.Li,P.Fung,
[355] J. Li, R. R. Selvaraju, A. Gotmare, S. R. Joty, C. Xiong, and S. C. and S. C. H. Hoi, “Instructblip: Towards general-purpose vision-
Hoi, “Align before fuse: Vision and language representation learning languagemodelswithinstructiontuning,”CoRR,vol.abs/2305.06500,
withmomentumdistillation,”inNeurIPS,2021,pp.9694–9705. 2023.
[356] A.Singh,R.Hu,V.Goswami,G.Couairon,W.Galuba,M.Rohrbach, [373] D. Zhu, J. Chen, X. Shen, X. Li, and M. Elhoseiny, “Minigpt-4: En-
andD.Kiela,“FLAVA:Afoundationallanguageandvisionalignment hancing vision-language understanding with advanced large language
model,”inCVPR. IEEE,2022,pp.15617–15629. models,”CoRR,vol.abs/2304.10592,2023.

26
[374] H. Zhang, X. Li, and L. Bing, “Video-llama: An instruction-tuned [399] X.Zhai,B.Mustafa,A.Kolesnikov,andL.Beyer,“Sigmoidlossfor
audio-visual language model for video understanding,” CoRR, vol. language image pre-training,” in ICCV. IEEE, 2023, pp. 11941–
abs/2306.02858,2023. 11952.
[375] Y.Su,T.Lan,H.Li,J.Xu,Y.Wang,andD.Cai,“Pandagpt:Onemodel [400] X.Gu,T.Lin,W.Kuo,andY.Cui,“Open-vocabularyobjectdetection
toinstruction-followthemall,”CoRR,vol.abs/2305.16355,2023. viavisionandlanguageknowledgedistillation,”inICLR,2022.
[376] K. Li, Y. He, Y. Wang, Y. Li, W. Wang, P. Luo, Y. Wang, L. Wang, [401] A.Kamath,M.Singh,Y.LeCun,G.Synnaeve,I.Misra,andN.Carion,
and Y. Qiao, “Videochat: Chat-centric video understanding,” CoRR, “MDETR - modulated detection for end-to-end multi-modal under-
vol.abs/2305.06355,2023. standing,”inICCV. IEEE,2021,pp.1760–1770.
[377] S. contributors. (2023) Stablelm: Stability ai language models. [402] V.Blukis,C.Paxton,D.Fox,A.Garg,andY.Artzi,“Apersistentspa-
[Online].Available:https://github.com/stability-AI/stableLM tialsemanticrepresentationforhigh-levelnaturallanguageinstruction
[378] L. Zhao, E. Yu, Z. Ge, J. Yang, H. Wei, H. Zhou, J. Sun, Y. Peng, execution,”inCoRL,vol.164. PMLR,2021,pp.706–717.
R. Dong, C. Han, and X. Zhang, “Chatspot: Bootstrapping mul- [403] K.He,X.Chen,S.Xie,Y.Li,P.Dolla´r,andR.B.Girshick,“Masked
timodal llms via precise referring instruction tuning,” CoRR, vol. autoencodersarescalablevisionlearners,”inCVPR. IEEE,2022,pp.
abs/2307.09474,2023. 15979–15988.
[379] Q.Ye,H.Xu,G.Xu,J.Ye,M.Yan,Y.Zhou,J.Wang,A.Hu,P.Shi, [404] M.Minderer,A.A.Gritsenko,A.Stone,M.Neumann,D.Weissenborn,
Y.Shi,C.Li,Y.Xu,H.Chen,J.Tian,Q.Qi,J.Zhang,andF.Huang, A. Dosovitskiy, A. Mahendran, A. Arnab, M. Dehghani, Z. Shen,
“mplug-owl: Modularization empowers large language models with X.Wang,X.Zhai,T.Kipf,andN.Houlsby,“Simpleopen-vocabulary
multimodality,”CoRR,vol.abs/2304.14178,2023. objectdetectionwithvisiontransformers,”CoRR,vol.abs/2205.06230,
[380] Q. Ye, H. Xu, J. Ye, M. Yan, A. Hu, H. Liu, Q. Qian, J. Zhang, 2022.
F. Huang, and J. Zhou, “mplug-owl2: Revolutionizing multi-modal [405] Z. Liu, H. Mao, C. Wu, C. Feichtenhofer, T. Darrell, and S. Xie, “A
large language model with modality collaboration,” CoRR, vol. convnetforthe2020s,”inCVPR. IEEE,2022,pp.11966–11976.
abs/2311.04257,2023. [406] J.Ho,W.Chan,C.Saharia,J.Whang,R.Gao,A.A.Gritsenko,D.P.
[381] C. Xu, D. Guo, N. Duan, and J. J. McAuley, “Baize: An open- Kingma,B.Poole,M.Norouzi,D.J.Fleet,andT.Salimans,“Imagen
source chat model with parameter-efficient tuning on self-chat data,” video:Highdefinitionvideogenerationwithdiffusionmodels,”CoRR,
in EMNLP. Association for Computational Linguistics, 2023, pp. vol.abs/2210.02303,2022.
6268–6278. [407] R. Villegas, M. Babaeizadeh, P. Kindermans, H. Moraldo, H. Zhang,
[382] C.Wu,S.Yin,W.Qi,X.Wang,Z.Tang,andN.Duan,“Visualchatgpt: M. T. Saffar, S. Castro, J. Kunze, and D. Erhan, “Phenaki: Variable
Talking, drawing and editing with visual foundation models,” CoRR, length video generation from open domain textual descriptions,” in
vol.abs/2303.04671,2023. ICLR. OpenReview.net,2023.
[383] F. Chen, M. Han, H. Zhao, Q. Zhang, J. Shi, S. Xu, and B. Xu, “X- [408] M. S. M. Sajjadi, D. Duckworth, A. Mahendran, S. van Steenkiste,
LLM:bootstrappingadvancedlargelanguagemodelsbytreatingmulti- F. Pavetic, M. Lucic, L. J. Guibas, K. Greff, and T. Kipf, “Object
modalitiesasforeignlanguages,”CoRR,vol.abs/2305.04160,2023. scenerepresentationtransformer,”inNeurIPS,2022.
[384] X. Zhai, A. Kolesnikov, N. Houlsby, and L. Beyer, “Scaling vision [409] C. R. Qi, H. Su, K. Mo, and L. J. Guibas, “Pointnet: Deep learning
transformers,”inCVPR. IEEE,2022,pp.1204–1213. onpointsetsfor3dclassificationandsegmentation,”inCVPR. IEEE
[385] Z.Du,Y.Qian,X.Liu,M.Ding,J.Qiu,Z.Yang,andJ.Tang,“GLM: ComputerSociety,2017,pp.77–85.
generallanguagemodelpretrainingwithautoregressiveblankinfilling,” [410] C.R.Qi,L.Yi,H.Su,andL.J.Guibas,“Pointnet++:Deephierarchical
inACL(1). AssociationforComputationalLinguistics,2022,pp.320– feature learning on point sets in a metric space,” in NIPS, 2017, pp.
335. 5099–5108.
[386] F.Chen,D.Zhang,M.Han,X.Chen,J.Shi,S.Xu,andB.Xu,“VLP: [411] Y.Hong,C.Lin,Y.Du,Z.Chen,J.B.Tenenbaum,andC.Gan,“3d
A survey on vision-language pre-training,” Int. J. Autom. Comput., concept learning and reasoning from multi-view images,” in CVPR.
vol.20,no.1,pp.38–56,2023. IEEE,2023,pp.9202–9212.
[387] P. Xu, X. Zhu, and D. A. Clifton, “Multimodal learning with trans- [412] K. M. Jatavallabhula, A. Kuwajerwala, Q. Gu, M. Omama, G. Iyer,
formers: A survey,” IEEE Trans. Pattern Anal. Mach. Intell., vol. 45, S. Saryazdi, T. Chen, A. Maalouf, S. Li, N. V. Keetha, A. Tewari,
no.10,pp.12113–12132,2023. J.B.Tenenbaum,C.M.deMelo,K.M.Krishna,L.Paull,F.Shkurti,
[388] X. Wang, G. Chen, G. Qian, P. Gao, X. Wei, Y. Wang, Y. Tian, and and A. Torralba, “Conceptfusion: Open-set multimodal 3d mapping,”
W.Gao,“Large-scalemulti-modalpre-trainedmodels:Acomprehen- inRSS,2023.
sivesurvey,”Mach.Intell.Res.,vol.20,no.4,pp.447–482,2023. [413] N. Reimers and I. Gurevych, “Sentence-bert: Sentence embeddings
[389] J. Zhang, J. Huang, S. Jin, and S. Lu, “Vision-language models for using siamese bert-networks,” in EMNLP/IJCNLP (1). Association
visiontasks:Asurvey,”CoRR,vol.abs/2304.00685,2023. forComputationalLinguistics,2019,pp.3980–3990.
[390] C.Sun,A.Myers,C.Vondrick,K.Murphy,andC.Schmid,“Videobert: [414] V. Sanh, L. Debut, J. Chaumond, and T. Wolf, “Distilbert, a distilled
Ajointmodelforvideoandlanguagerepresentationlearning,”inICCV. version of BERT: smaller, faster, cheaper and lighter,” CoRR, vol.
IEEE,2019,pp.7463–7472. abs/1910.01108,2019.
[391] H.Bao,W.Wang,L.Dong,Q.Liu,O.K.Mohammed,K.Aggarwal, [415] M. N. Team. (2023) Introducing mpt-7b: A new standard for open-
S. Som, S. Piao, and F. Wei, “Vlmo: Unified vision-language pre- source, commercially usable llms. Accessed: 2023-05-05. [Online].
trainingwithmixture-of-modality-experts,”inNeurIPS,2022. Available:www.mosaicml.com/blog/mpt-7b
[392] X.Zhai,X.Wang,B.Mustafa,A.Steiner,D.Keysers,A.Kolesnikov, [416] A. Awadalla, I. Gao, J. Gardner, J. Hessel, Y. Hanafy, W. Zhu,
andL.Beyer,“Lit:Zero-shottransferwithlocked-imagetexttuning,” K.Marathe,Y.Bitton,S.Y.Gadre,S.Sagawa,J.Jitsev,S.Kornblith,
inCVPR. IEEE,2022,pp.18102–18112. P.W.Koh,G.Ilharco,M.Wortsman,andL.Schmidt,“Openflamingo:
[393] M.Tsimpoukelli,J.Menick,S.Cabi,S.M.A.Eslami,O.Vinyals,and An open-source framework for training large autoregressive vision-
F.Hill,“Multimodalfew-shotlearningwithfrozenlanguagemodels,” languagemodels,”CoRR,vol.abs/2308.01390,2023.
inNeurIPS,2021,pp.200–212. [417] S.Biderman,H.Schoelkopf,Q.G.Anthony,H.Bradley,K.O’Brien,
[394] J. Yu, Z. Wang, V. Vasudevan, L. Yeung, M. Seyedhosseini, and E. Hallahan, M. A. Khan, S. Purohit, U. S. Prashanth, E. Raff,
Y.Wu,“Coca:Contrastivecaptionersareimage-textfoundationmod- A. Skowron, L. Sutawika, and O. van der Wal, “Pythia: A suite for
els,”Trans.Mach.Learn.Res.,vol.2022,2022. analyzinglargelanguagemodelsacrosstrainingandscaling,”inICML,
[395] P.Wang,A.Yang,R.Men,J.Lin,S.Bai,Z.Li,J.Ma,C.Zhou,J.Zhou, vol.202. PMLR,2023,pp.2397–2430.
and H. Yang, “OFA: unifying architectures, tasks, and modalities [418] M. Javaheripi, S. Bubeck, M. Abdin, J. Aneja, S. Bubeck, C. C. T.
throughasimplesequence-to-sequencelearningframework,”inICML, Mendes, W. Chen, A. Del Giorno, R. Eldan, S. Gopi et al., “Phi-2:
vol.162. PMLR,2022,pp.23318–23340. The surprising power of small language models,” Microsoft Research
[396] E.J.Hu,Y.Shen,P.Wallis,Z.Allen-Zhu,Y.Li,S.Wang,L.Wang, Blog,2023.
andW.Chen,“Lora:Low-rankadaptationoflargelanguagemodels,” [419] S.Black,S.Biderman,E.Hallahan,Q.Anthony,L.Gao,L.Golding,
inICLR,2022. H.He,C.Leahy,K.McDonell,J.Phang,M.Pieler,U.S.Prashanth,
[397] P.Esser,R.Rombach,andB.Ommer,“Tamingtransformersforhigh- S. Purohit, L. Reynolds, J. Tow, B. Wang, and S. Weinbach, “Gpt-
resolutionimagesynthesis,”inCVPR. ComputerVisionFoundation neox-20b:Anopen-sourceautoregressivelanguagemodel,”CoRR,vol.
/IEEE,2021,pp.12873–12883. abs/2204.06745,2022.
[398] C. Zheng, T. Vuong, J. Cai, and D. Phung, “Movq: Modulating [420] M.Chen,J.Tworek,H.Jun,Q.Yuan,H.P.deOliveiraPinto,J.Kaplan,
quantized vectors for high-fidelity image generation,” in NeurIPS, H. Edwards, Y. Burda, N. Joseph, G. Brockman, A. Ray, R. Puri,
2022. G. Krueger, M. Petrov, H. Khlaaf, G. Sastry, P. Mishkin, B. Chan,

27
S. Gray, N. Ryder, M. Pavlov, A. Power, L. Kaiser, M. Bavarian, [439] X. Lin, J. So, S. Mahalingam, F. Liu, and P. Abbeel, “Spawnnet:
C.Winter,P.Tillet,F.P.Such,D.Cummings,M.Plappert,F.Chantzis, Learning generalizable visuomotor skills from pre-trained networks,”
E.Barnes,A.Herbert-Voss,W.H.Guss,A.Nichol,A.Paino,N.Tezak, CoRR,vol.abs/2307.03567,2023.
J. Tang, I. Babuschkin, S. Balaji, S. Jain, W. Saunders, C. Hesse, [440] S. P. Arunachalam, I. Gu¨zey, S. Chintala, and L. Pinto, “Holo-dex:
A. N. Carr, J. Leike, J. Achiam, V. Misra, E. Morikawa, A. Rad- Teaching dexterity with immersive mixed reality,” in ICRA. IEEE,
ford, M. Knight, M. Brundage, M. Murati, K. Mayer, P. Welinder, 2023,pp.5962–5969.
B.McGrew,D.Amodei,S.McCandlish,I.Sutskever,andW.Zaremba, [441] N.M.M.Shafiullah,A.Rai,H.Etukuru,Y.Liu,I.Misra,S.Chintala,
“Evaluating large language models trained on code,” CoRR, vol. andL.Pinto,“Onbringingrobotshome,”CoRR,vol.abs/2311.16098,
abs/2107.03374,2021. 2023.
[421] S. Karamcheti, S. Nair, A. Balakrishna, P. Liang, T. Kollar, and [442] Y. Seo, D. Hafner, H. Liu, F. Liu, S. James, K. Lee, and P. Abbeel,
D.Sadigh,“Prismaticvlms:Investigatingthedesignspaceofvisually- “Maskedworldmodelsforvisualcontrol,”inCoRL,vol.205. PMLR,
conditionedlanguagemodels,”inICML,2024. 2022,pp.1332–1344.
[422] L. Beyer, A. Steiner, A. S. Pinto, A. Kolesnikov, X. Wang, D. Salz, [443] R.Mendonca,S.Bahl,andD.Pathak,“Structuredworldmodelsfrom
M.Neumann,I.Alabdulmohsin,M.Tschannen,E.Bugliarello,T.Un- humanvideos,”inRSS,2023.
terthiner, D. Keysers, S. Koppula, F. Liu, A. Grycner, A. A. Grit- [444] M.Pan,X.Zhu,Y.Wang,andX.Yang,“Iso-dream:Isolatingandlever-
senko, N. Houlsby, M. Kumar, K. Rong, J. Eisenschlos, R. Kabra, agingnoncontrollablevisualdynamicsinworldmodels,”inNeurIPS,
M.Bauer,M.Bosnjak,X.Chen,M.Minderer,P.Voigtlaender,I.Bica, 2022.
I. Balazevic, J. Puigcerver, P. Papalampidi, O. J. He´naff, X. Xiong, [445] Z.Dai,Z.Yang,Y.Yang,J.G.Carbonell,Q.V.Le,andR.Salakhutdi-
R.Soricut,J.Harmsen,andX.Zhai,“Paligemma:Aversatile3bVLM nov,“Transformer-xl:Attentivelanguagemodelsbeyondafixed-length
fortransfer,”CoRR,vol.abs/2407.07726,2024. context,”inACL(1). AssociationforComputationalLinguistics,2019,
[423] A.Steiner,A.S.Pinto,M.Tschannen,D.Keysers,X.Wang,Y.Bitton, pp.2978–2988.
A.A.Gritsenko,M.Minderer,A.Sherbondy,S.Long,S.Qin,R.R. [446] A. Avetisyan, C. Xie, H. Howard-Jenkins, T. Yang, S. Aroudj,
Ingle, E. Bugliarello, S. Kazemzadeh, T. Mesnard, I. Alabdulmohsin, S. Patra, F. Zhang, D. P. Frost, L. Holland, C. Orme, J. Engel,
L.Beyer,andX.Zhai,“Paligemma2:Afamilyofversatilevlmsfor E.Miller,R.A.Newcombe,andV.Balntas,“Scenescript:Reconstruct-
transfer,”CoRR,vol.abs/2412.03555,2024. ingsceneswithanautoregressivestructuredlanguagemodel,”CoRR,
[424] Chameleon-Team,“Chameleon:Mixed-modalearly-fusionfoundation vol.abs/2403.13064,2024.
models,”CoRR,vol.abs/2405.09818,2024. [447] N. M. Shafiullah, Z. J. Cui, A. Altanzaya, and L. Pinto, “Behavior
[425] X. Wang, X. Zhang, Z. Luo, Q. Sun, Y. Cui, J. Wang, F. Zhang, transformers:Cloning$k$modeswithonestone,”inNeurIPS,2022.
Y.Wang,Z.Li,Q.Yu,Y.Zhao,Y.Ao,X.Min,T.Li,B.Wu,B.Zhao, [448] Z.J.Cui,Y.Wang,N.M.M.Shafiullah,andL.Pinto,“Fromplayto
B.Zhang,L.Wang,G.Liu,Z.He,X.Yang,J.Liu,Y.Lin,T.Huang, policy:Conditionalbehaviorgenerationfromuncuratedrobotdata,”in
and Z. Wang, “Emu3: Next-token prediction is all you need,” CoRR, ICLR,2023.
vol.abs/2409.18869,2024. [449] S. Lee, Y. Wang, H. Etukuru, H. J. Kim, N. M. M. Shafiullah, and
[426] H.Liu,W.Yan,M.Zaharia,andP.Abbeel,“Worldmodelonmillion- L.Pinto,“Behaviorgenerationwithlatentactions,”inICML,2024.
length video and language with blockwise ringattention,” in ICLR. [450] R. Sapkota, Y. Cao, K. I. Roumeliotis, and M. Karkee, “Vision-
OpenReview.net,2025. language-action models: Concepts, progress, applications and chal-
[427] D. K. Misra, A. Bennett, V. Blukis, E. Niklasson, M. Shatkhin, and lenges,”CoRR,vol.abs/2505.04769,2025.
Y. Artzi, “Mapping instructions to actions in 3d environments with [451] Y. Zhong, F. Bai, S. Cai, X. Huang, Z. Chen, X. Zhang, Y. Wang,
visualgoalprediction,”inEMNLP,2018,pp.2667–2678. S. Guo, T. Guan, K. N. Lui, Z. Qi, Y. Liang, Y. Chen, and Y. Yang,
[428] C. Lynch, M. Khansari, T. Xiao, V. Kumar, J. Tompson, S. Levine, “A survey on vision-language-action models: An action tokenization
andP.Sermanet,“Learninglatentplansfromplay,”inCoRL,vol.100. perspective,”CoRR,vol.abs/2507.01925,2025.
PMLR,2019,pp.1113–1132. [452] M.U.Din,W.Akram,L.S.Saoud,J.Rosell,andI.Hussain,“Vision
[429] M.Bhardwaj,B.Sundaralingam,A.Mousavian,N.D.Ratliff,D.Fox, languageactionmodelsinroboticmanipulation:Asystematicreview,”
F. Ramos, and B. Boots, “STORM: an integrated framework for CoRR,vol.abs/2507.10672,2025.
fastjoint-spacemodel-predictivecontrolforreactivemanipulation,”in [453] D. Zhang, J. Sun, C. Hu, X. Wu, Z. Yuan, R. Zhou, F. Shen, and
CoRL,vol.164. PMLR,2021,pp.750–759. Q.Zhou,“Purevisionlanguageaction(VLA)models:Acomprehen-
[430] A.Jaegle,S.Borgeaud,J.Alayrac,C.Doersch,C.Ionescu,D.Ding, sivesurvey,”CoRR,vol.abs/2509.19012,2025.
S. Koppula, D. Zoran, A. Brock, E. Shelhamer, O. J. He´naff, M. M. [454] S.Li,Y.Chen,L.Dong,S.Liu,D.Lan,L.Yu,andZ.Pang,“Transfer-
Botvinick,A.Zisserman,O.Vinyals,andJ.Carreira,“PerceiverIO:A ringvision-language-actionmodelstoindustryapplications:Architec-
generalarchitectureforstructuredinputs&outputs,”inICLR,2022. tures,performance,andchallenges,”CoRR,vol.abs/2509.23121,2025.
[431] E. Wijmans, A. Kadian, A. Morcos, S. Lee, I. Essa, D. Parikh, [455] K. Kawaharazuka, J. Oh, J. Yamada, I. Posner, and Y. Zhu, “Vision-
M. Savva, and D. Batra, “DD-PPO: learning near-perfect pointgoal language-action models for robotics: A review towards real-world
navigatorsfrom2.5billionframes,”inICLR,2020. applications,”IEEEAccess,vol.13,pp.162467–162504,2025.
[432] M. Zhu, Y. Zhu, J. Li, J. Wen, Z. Xu, N. Liu, R. Cheng, C. Shen, [456] Z.Yu,B.Wang,P.Zeng,H.Zhang,J.Zhang,L.Gao,J.Song,N.Sebe,
Y. Peng, F. Feng, and J. Tang, “Scaling diffusion policy in trans- andH.T.Shen,“Asurveyonefficientvision-language-actionmodels,”
former to 1 billion parameters for robotic manipulation,” CoRR, vol. CoRR,vol.abs/2510.24795,2025.
abs/2409.14411,2024. [457] S.Poria,N.Majumder,C.Hung,A.A.Bagherzadeh,C.Li,K.Kwok,
[433] J. W. Wei, L. Hou, A. K. Lampinen, X. Chen, D. Huang, Y. Tay, Z.Wang,C.Tan,J.Wu,andD.Hsu,“10openchallengessteeringthe
X. Chen, Y. Lu, D. Zhou, T. Ma, and Q. V. Le, “Symbol tun- futureofvision-language-actionmodels,”CoRR,vol.abs/2511.05936,
ing improves in-context learning in language models,” CoRR, vol. 2025.
abs/2305.08298,2023. [458] C. Xu, S. Zhang, Y. Liu, B. Sun, W. Chen, B. Xu, Q. Liu, J. Wang,
[434] W.PeeblesandS.Xie,“Scalablediffusionmodelswithtransformers,” S.Wang,S.Luo,J.Peters,A.V.Vasilakos,S.Zafeiriou,andJ.Deng,
inICCV. IEEE,2023,pp.4172–4182. “An anatomy of vision-language-action models: From modules to
[435] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic milestonesandchallenges,”CoRR,vol.abs/2512.11362,2025.
models,”inNeurIPS,2020. [459] H.Deng,Z.Wu,H.Liu,W.Guo,Y.Xue,Z.Shan,C.Zhang,B.Jia,
[436] Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, Y. Ling, G. Lu, and Z. Wang, “A survey on reinforcement learning
and B. Poole, “Score-based generative modeling through stochastic ofvision-language-actionmodelsforroboticmanipulation,”TechRxiv,
differentialequations,”inICLR,2021. 2025,preprint.
[437] A. Zeng, P. Florence, J. Tompson, S. Welker, J. Chien, M. Attarian, [460] T. Hu, X. Liu, S. Wang, Y. Zhu, A. Liang, L. Kong, G. Zhao,
T.Armstrong,I.Krasin,D.Duong,V.Sindhwani,andJ.Lee,“Trans- Z. Gong, J. Cen, Z. Huang, X. Hao, L. Li, H. Song, X. Li, J. Ma,
porter networks: Rearranging the visual world for robotic manipula- S.Shen,J.Zhu,D.Tao,Z.Liu,andJ.Liang,“Vision-language-action
tion,”inCoRL,vol.155. PMLR,2020,pp.726–747. modelsforautonomousdriving:Past,present,andfuture,”CoRR,vol.
[438] R. Goyal, S. E. Kahou, V. Michalski, J. Materzynska, S. Westphal, abs/2512.16760,2025.
H.Kim,V.Haenel,I.Fru¨nd,P.Yianilos,M.Mueller-Freitag,F.Hoppe, [461] X. Li, C. Mata, J. Park, K. Kahatapitiya, Y. S. Jang, J. Shang,
C. Thurau, I. Bax, and R. Memisevic, “The ”something something” K. Ranasinghe, R. D. Burgert, M. Cai, Y. J. Lee, and M. S. Ryoo,
video database for learning and evaluating visual common sense,” in “Llara:Superchargingrobotlearningdataforvision-languagepolicy,”
ICCV. IEEEComputerSociety,2017,pp.5843–5851. inICLR. OpenReview.net,2025.

28
[462] K. Pertsch, K. Stachowicz, B. Ichter, D. Driess, S. Nair, Q. Vuong, model,”inCoRL,ser.ProceedingsofMachineLearningResearch,vol.
O.Mees,C.Finn,andS.Levine,“FAST:efficientactiontokenization 270. PMLR,2024,pp.1675–1690.
forvision-language-actionmodels,”CoRR,vol.abs/2501.09747,2025. [482] K. K. Minho Park and, J. Hyung, H. Jang, H. Jin, J. Yun, H. Lee,
[463] P. Intelligence, K. Black, N. Brown, J. Darpinian, K. Dhabalia, and J. Choo, “ACG: action coherence guidance for flow-based VLA
D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, M. Y. Galliker, models,”CoRR,vol.abs/2510.22201,2025.
D.Ghosh,L.Groom,K.Hausman,B.Ichter,S.Jakubczak,T.Jones, [483] T.W.WenchengYeand,L.Zhu,F.Li,andG.Yang,“Actdistill:General
L. Ke, D. LeBlanc, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, action-guided self-derived distillation for efficient, vision-language-
K. Pertsch, A. Z. Ren, L. X. Shi, L. M. Smith, J. T. Springenberg, actionmodels,”CoRR,vol.abs/2511.18082,2025.
K.Stachowicz,J.Tanner,Q.Vuong,H.Walke,A.Walling,H.Wang, [484] H.G.YuntaoDaiand,T.Wang,Q.Cheng,Y.Zheng,Z.Qiu,L.Gong,
L. Yu, and U. Zhilinsky, “π0.5: a vision-language-action model with W.Lou,andX.Zhou,“Actionflow:Apipelinedactionaccelerationfor
open-worldgeneralization,”CoRR,vol.abs/2504.16054,2025. visionlanguage,modelsonedge,”CoRR,vol.abs/2512.20276,2025.
[464] Z. Xu, H. L. Chiang, Z. Fu, M. G. Jacob, T. Zhang, T. E. Lee, [485] Y. L. Weijie Shen and, Y. Wu, Z. Liang, S. Gu, D. Wang, T. Nian,
W.Yu,C.Schenck,D.Rendleman,D.Shah,F.Xia,J.Hsu,J.Hoech, L. Xu, Y. Qin, J. Pang, X. Guan, X. Yang, and Y. Mu, “Expertise
P. Florence, S. Kirmani, S. Singh, V. Sindhwani, C. Parada, C. Finn, neednotmonopolize:Action-specializedmixtureofexperts,forvision-
P.Xu,S.Levine,andJ.Tan,“MobilityVLA:multimodalinstruction language-actionlearning,”CoRR,vol.abs/2510.14300,2025.
navigation with long-context vlms and topological graphs,” in CoRL, [486] Y. C. Xiaohuan Pei and, S. Xu, Y. Wang, Y. Shi, and C. Xu,
ser. Proceedings of Machine Learning Research, vol. 270. PMLR, “Action-aware dynamic pruning for efficient vision-language-action,
2024,pp.3866–3887. manipulation,”CoRR,vol.abs/2509.22093,2025.
[465] P. Ding, J. Ma, X. Tong, B. Zou, X. Luo, Y. Fan, T. Wang, H. Lu, [487] Z.W.SiyuXuand,Y.Wang,C.Xia,T.Huang,andC.Xu,“Affordance
P. Mo, J. Liu, Y. Wang, H. Zhou, W. Feng, J. Liu, S. Huang, and field intervention: Enabling vlas to escape memory traps, in robotic
D. Wang, “Humanoid-vla: Towards universal humanoid control with manipulation,”CoRR,vol.abs/2512.07472,2025.
visualintegration,”CoRR,vol.abs/2502.14795,2025. [488] Z. Y. Yizheng Zhang and, J. Lai, C. Lu, and L. Han, “Agentworld:
[466] P. Ding, H. Zhao, W. Zhang, W. Song, M. Zhang, S. Huang, Aninteractivesimulationplatformforsceneconstruction,andmobile
N. Yang, and D. Wang, “QUAR-VLA: vision-language-action model roboticmanipulation,”CoRR,vol.abs/2508.07770,2025.
for quadruped robots,” in ECCV (5), ser. Lecture Notes in Computer [489] H. Q. Irmak Guzey and, J. Urain, C. Wang, J. Yin, K. Bodduluri,
Science,vol.15063. Springer,2024,pp.352–367. M. Lambeta, L. Pinto, A. Rai, J. Malik, T. Wu, A. Sharma, and
[467] X.Tong,P.Ding,D.Wang,W.Zhang,C.Cui,M.Sun,Y.Fan,H.Zhao, H. Bharadhwaj, “Dexterity from smart lenses: Multi-fingered robot
H.Zhang,Y.Dang,S.Huang,andS.Lyu,“Quart-online:Latency-free manipulation with, in-the-wild human demonstrations,” CoRR, vol.
largemultimodallanguagemodelforquadrupedrobotlearning,”CoRR,
abs/2511.16661,2025.
vol.abs/2412.15576,2024.
[490] B. L. Wenxin Zheng and, B. Xu, E. Feng, J. Gu, and H. Chen,
[468] H.Zhao,W.Song,D.Wang,X.Tong,P.Ding,X.Cheng,andZ.Ge,
“Leveragingos-levelprimitivesforroboticactionmanagement,”CoRR,
“More:Unlockingscalabilityinreinforcementlearningforquadruped
vol.abs/2508.10259,2025.
vision-language-actionmodels,”CoRR,vol.abs/2503.08007,2025.
[491] Z.W.YiyangHuangand,Z.Wan,Y.Tian,H.Xu,Y.Han,andY.Gan,
[469] Y.Zhong,X.Huang,R.Li,C.Zhang,Y.Liang,Y.Yang,andY.Chen,
“ANNIE:becarefulofyourrobots,”CoRR,vol.abs/2509.03383,2025.
“Dexgraspvla: A vision-language-action framework towards general
[492] S.C.YuhuaJiangand,Y.Ding,F.Gao,andB.Qi,“Asyncvla:Asyn-
dexterousgrasping,”CoRR,vol.abs/2502.20900,2025.
chronous flow matching for vision-language-action models,” CoRR,
[470] Y.Cui,Y.Zhang,L.Tao,Y.Li,X.Yi,andZ.Li,“End-to-enddexterous
vol.abs/2511.14148,2025.
arm-hand VLA policies via shared autonomy: VR teleoperation aug-
[493] C.W.YangZhangand,O.Lu,Y.Zhao,Y.Ge,Z.S.0001,X.L.0001,
mentedbyautonomoushandVLApolicyforefficientdatacollection,”
C. Z. 0012, C. Bai, and X. L. 0001, “Align-then-steer: Adapting the
CoRR,vol.abs/2511.00139,2025.
vision-languageactionmodelsthroughunifiedlatentguidance,”2025.
[471] NVIDIA, “Alpamayo-r1: Bridging reasoning and action prediction
[Online].Available:https://dblp.org/rec/journals/corr/abs-2509-02055
for generalizable autonomous driving in the long tail,” CoRR, vol.
[494] J.T.ZhenlongYuanand,J.Luo,R.Chen,C.Qian,L.Sun,X.Chu,
abs/2511.00088,2025. Y. Cai, D. Zhang, and S. Li, “Autodrive-r2: Incentivizing reasoning
[472] H.Arai,K.Miwa,K.Sasaki,K.Watanabe,Y.Yamaguchi,S.Aoki,and
and self-reflection, capacity for VLA model in autonomous driving,”
I. Yamamoto, “Covla: Comprehensive vision-language-action dataset
CoRR,vol.abs/2509.01944,2025.
forautonomousdriving,”inWACV. IEEE,2025,pp.1933–1943.
[473] Y.Li,S.Shang,W.Liu,B.Zhan,H.Wang,Y.Wang,Y.Chen,X.Wang, [495] Y.X.HanshiWangand,Z.Xu,J.Gao,Y.Liu,W.Hu,K.Wang,and
Y. An, C. Tang, L. Hou, L. Fan, and Z. Zhang, “Drivevla-w0: World Z. Zhang, “Autoprune: Each complexity deserves a pruning policy,”
models amplify data scaling law in autonomous driving,” CoRR, vol. CoRR,vol.abs/2509.23931,2025.
abs/2510.12796,2025. [496] T. C. Zewei Zhou and, S. Z. Zhao, Y. Zhang, Z. Huang, B. Zhou,
[474] J.Hwang,R.Xu,H.Lin,W.Hung,J.Ji,K.Choi,D.Huang,T.He, and J. Ma, “Autovla: A vision-language-action model for end-to-end
P. Covington, B. Sapp, Y. Zhou, J. Guo, D. Anguelov, and M. Tan, autonomous, driving with adaptive reasoning and reinforcement fine-
“EMMA: end-to-end multimodal model for autonomous driving,” tuning,”CoRR,vol.abs/2506.13757,2025.
Trans.Mach.Learn.Res.,vol.2025,2025. [497] J. L. Lei Xiao and, J. Gao, F. Ye, Y. Jin, J. Qian, J. Zhang,
[475] P. Chen, P. Bu, Y. Wang, X. Wang, Z. Wang, J. Guo, Y. Zhao, Y. Wu, and X. Yu, “Ava-vla: Improving vision-language-action
Q. Zhu, J. Song, S. Yang, J. Wang, and B. Zheng, “Combatvla: An models with active visual attention,” 2025. [Online]. Available:
efficient vision-language-action model for combat tasks in 3d action https://dblp.org/rec/journals/corr/abs-2511-18960
role-playinggames,”CoRR,vol.abs/2503.09527,2025. [498] L.L.HarrisSongand,“Avi:Actionfromvolumetricinference,”CoRR,
[476] M. Li, Z. Wang, K. He, X. Ma, and Y. Liang, “JARVIS-VLA: post- vol.abs/2510.21746,2025.
training large-scale vision language models to play visual games [499] G. T. Xueyang Zhou and, G. Zhang, H. Wang, P. Zhou, and L. Sun,
with keyboards and mouse,” in ACL (Findings). Association for “Badvla:Towardsbackdoorattacksonvision-language-actionmodels,
ComputationalLinguistics,2025,pp.17878–17899. via objective-decoupled optimization,” CoRR, vol. abs/2505.16640,
[477] N.G.Tsung-WeiKeandandK.Fragkiadaki,“3ddiffuseractor:Policy 2025.
diffusionwith3dscenerepresentations,”inCoRL,ser.Proceedingsof [500] Z.Z.KechunXuand,A.Chen,S.Zhao,Q.Huang,Y.Yang,H.Lu,
MachineLearningResearch,vol.270. PMLR,2024,pp.1949–1974. R. Xiong, M. Tomizuka, and Y. Wang, “Seeing to act, prompting to
[478] X. Li, L. Heng, J. Liu, Y. Shen, C. Gu, Z. Liu, H. Chen, N. Han, specify: A bayesian factorization of, vision language action policy,”
R.Zhang,H.Tang,S.Zhang,andH.Dong,“3ds-vla,”arXivpreprint, CoRR,vol.abs/2512.11218,2025.
2025. [501] Y. F. Hao Luo and, W. Zhang, S. Zheng, Y. Wang, H. Yuan, J. Liu,
[479] Y.C.JiahuiZhangand,Y.Xu,Z.Huang,Y.Zhou,Y.Yuan,X.Cai, C.Xu,Q.Jin,andZ.Lu,“Being-h0:Vision-language-actionpretraining
G. Huang, X. Quan, H. Xu, and L. Zhang, “4d-vla: Spatiotempo- fromlarge-scalehuman,videos,”CoRR,vol.abs/2507.15597,2025.
ral vision-language-action pretraining with cross-scene, calibration,” [502] J.F.YanboMaoand,R.Zhang,H.Xie,andM.Yao,“Beyondsuccess:
CoRR,vol.abs/2506.22242,2025. Refiningelegantrobotmanipulationfrommixed-quality,dataviajust-
[480] M.A.KoheiSendaiand,T.Matsushima,Y.Matsuo,andY.Iwasawa, in-timeintervention,”CoRR,vol.abs/2511.22555,2025.
“Leave no observation behind: Real-time correction for VLA action, [503] M.A.C.KoffiviFide`leGbagbeand,A.Alabbas,O.Alyunes,A.Lykov,
chunks,”CoRR,vol.abs/2509.23224,2025. andD.Tsetserukou,“Bi-vla:Vision-language-actionmodel-basedsys-
[481] H.C.SiyuanHuangand,Y.Liu,Y.Zhu,H.Dong,A.Boularias,P.Gao, temforbimanualrobotic,dexterousmanipulations,”inSMC. IEEE,
and H. Li, “A3VLM: actionable articulation-aware vision language 2024,pp.2864–2869.

29
[504] T.B.MasatoKobayashiand,“Bi-vla:Bilateralcontrol-basedimitation [527] Y. L. Tianyuan Yuan and, C. Lu, Z. Chen, T. Jiang, and H. Zhao,
learningviavision-language,fusionforactiongeneration,”CoRR,vol. “Depthvla: Enhancing vision-language-action models with depth-
abs/2509.18865,2025. aware,spatialreasoning,”CoRR,vol.abs/2510.13375,2025.
[505] Y. C. Peiyan Li and, H. Wu, X. Ma, X. Wu, Y. Huang, L. Wang, [528] E.Z.BinXieand,F.Jia,H.Shi,H.Fan,H.Zhang,H.Li,J.Sun,J.Bin,
T. Kong, and T. Tan, “Bridgevla: Input-output alignment for efficient J.Huang,K.Liu,K.Liu,K.Gu,L.Sun,M.Zhang,P.Han,R.Hao,
3d manipulation learning, with vision-language models,” CoRR, vol. R.Zhang,S.Huang,S.Xie,T.Wang,T.Liu,W.Tang,W.Zhu,Y.Chen,
abs/2506.07961,2025. Y. Liu, Y. Zhou, Y. Liu, Y. Zhao, Y. Ma, Y. Wei, Y. Chen, Z. Chen,
[506] A.Z.R.AsherJ.HancockandandA.Majumdar,“Run-timeobserva- Z.Li,Z.Wu,Z.Zhang,Z.Liu,Z.Yan,andZ.Zhang,“Dexbotic:Open-
tion interventions make vision-language-action models, more visually source vision-language-action toolbox,” CoRR, vol. abs/2510.23511,
robust,”inICRA. IEEE,2025,pp.9499–9506. 2025.
[507] Y.Y.XiuxiuQiand,J.Cao,L.Bai,C.Fan,C.Cao,andH.Wang,“Con- [529] Z. X. Cheng Chi and, S. Feng, E. Cousineau, Y. Du, B. Burchfiel,
tinuous vision-language-action co-learning with semantic-physical, R.Tedrake,andS.Song,“Diffusionpolicy:Visuomotorpolicylearning
alignmentforbehavioralcloning,”CoRR,vol.abs/2511.14396,2025. viaactiondiffusion,”Int.J.RoboticsRes.,vol.44,no.10-11,pp.1684–
[508] Y. Z. Zhongyi Zhou and, J. Wen, C. Shen, and Y. Xu, “Chatvla-2: 1704,2025.
Vision-language-action model with open-world embodied reasoning, [530] M. Z. Junjie Wen and, Y. Zhu, Z. Tang, J. Li, Z. Zhou, C. Li,
frompretrainedknowledge,”CoRR,vol.abs/2505.21906,2025. X. Liu, Y. Peng, C. Shen, and F. Feng, “Diffusion-vla: Scaling robot
[509] R. Y. Zijian An and, Y. Feng, and L. Zhou, “CLAW: A vision- foundation models via unified diffusion, and autoregression,” CoRR,
language-actionframeworkforweight-awarerobotic,grasping,”CoRR, vol.abs/2412.03293,2024.
vol.abs/2509.14143,2025. [531] A. J. Yu Gao and, Y. Wang, J. Wang, H. Jiang, Z. Sun, Y. Heng,
[510] J.K.Gi-CheonKangand,K.Shim,J.K.Lee,andB.Zhang,“CLIP-RT: W.Shuo,H.Zhao,andH.Sun,“Diffvla++:Bridgingcognitivereason-
learninglanguage-conditionedroboticpoliciesfromnatural,language ingandend-to-enddrivingthrough,metric-guidedalignment,”CoRR,
supervision,”CoRR,vol.abs/2411.00508,2024. vol.abs/2510.17148,2025.
[511] Q. Y. Zeyuan Chen and, Y. Chen, T. Wu, J. Zhang, Z. Ding, [532] R.Liang,Y.Zheng,K.Zheng,T.Tan,J.Li,L.Mao,Z.Wang,G.Chen,
J. Li, Y. Yang, and H. Dong, “Clutterdexgrasp: A sim-to-real sys- H. Ye, J. Liu, J. Wang, and X. Zhan, “Dichotomous diffusion policy
tem for general dexterous grasping, in cluttered scenes,” CoRR, vol. optimization,”arXivpreprint,2025.
abs/2506.14317,2025. [533] Z.F.RushuaiYangand,T.Zhang,K.Wang,C.Zhang,L.Zhao,X.Su,
Y.Chen,andJ.Bian,“Discover,learn,andreinforce:Scalingvision-
[512] F. S. Dapeng Zhang and, R. Zhao, Y. Chen, P. Zhi, C. Li, R. Zhou,
language-action pretraining, with diverse rl-generated trajectories,”
andQ.Zhou,“Coc-vla:Delvingintoadversarialdomaintransferforex-
CoRR,vol.abs/2511.19528,2025.
plainable, autonomous driving via chain-of-causality visual-language-
[534] M. K. Nikita Kachaev and, D. Zelezetsky, A. K. Kovalev, and A. I.
actionmodel,”CoRR,vol.abs/2511.19914,2025.
Panov, “Don’t blind your VLA: aligning visual representations for
[513] R. Z. Wei Li and, R. Shao, J. He, and L. Nie, “Cogvla: Cognition-
OOD,generalization,”CoRR,vol.abs/2510.25616,2025.
alignedvision-language-actionmodelviainstruction-driven,routing&
[535] J. K. ByungOk Han and and J. Jang, “A dual process VLA: efficient
sparsification,”CoRR,vol.abs/2508.21046,2025.
robotic manipulation leveraging VLM,” CoRR, vol. abs/2410.15549,
[514] X.C.QihangPengand,C.Yang,S.Shi,andH.Li,“Colavla:Lever-
2024.
aging cognitive latent reasoning for hierarchical parallel, trajectory
[536] Z.Z.GuoYeand,X.Zhao,S.Wu,H.Lu,S.Lu,andH.Liu,“Learning
planninginautonomousdriving,”CoRR,vol.abs/2512.22939,2025.
tofeelthefuture:Dreamtacvlaforcontact-richmanipulation,”CoRR,
[515] S.T.YuhuiChenand,S.Liu,Y.Zhou,H.Li,andD.Zhao,“Conrft:A
vol.abs/2512.23864,2025.
reinforcedfine-tuningmethodforVLAmodelsviaconsistency,policy,”
[537] H.L.WenyaoZhangand,Z.Qi,Y.Wang,X.Yu,J.Zhang,R.Dong,
CoRR,vol.abs/2502.05450,2025.
J. He, H. Wang, Z. Zhang, L. Yi, W. Zeng, and X. Jin, “Dreamvla:
[516] Y. W. Puhao Li and, Z. Xi, W. Li, Y. Huang, Z. Zhang, Y. Chen,
A vision-language-action model dreamed with comprehensive, world
J.Wang,S.Zhu,T.Liu,andS.Huang,“Controlvla:Few-shotobject-
knowledge,”CoRR,vol.abs/2507.04447,2025.
centric adaptation for pre-trained vision-language-action, models,”
[538] S. G. Jiacheng Ye and, J. Gao, J. Fan, S. Wu, W. Bi, H. Bai,
CoRR,vol.abs/2506.16211,2025.
L.Shang,andL.Kong,“Dream-vl&dream-vla:Openvision-language
[517] W. K. Tian Nian and, Y. Mu, T. Chen, S. Zhu, and B. Hu, “Control
and vision-language-action, models with diffusion language model
yourrobot:Aunifiedsystemforrobotcontrolandpolicy,deployment,”
backbone,”CoRR,vol.abs/2512.22615,2025.
CoRR,vol.abs/2509.23823,2025.
[539] Z. L. Zhen Fang and, J. Liu, H. Chen, Y. Zeng, S. Huang, Z. Chen,
[518] Y.C.ShiyuFangand,H.Liang,C.Lv,P.Hang,andJ.Sun,“Corevla:
L. Chen, S. Zhang, and F. Zhao, “Dualvla: Building a generalizable
A dual-stage end-to-end autonomous driving framework for, long-tail
embodiedagentviapartialdecoupling,ofreasoningandaction,”CoRR,
scenariosviacollect-and-refine,”CoRR,vol.abs/2509.15968,2025.
vol.abs/2511.22134,2025.
[519] T. Y. Zhaohui Wang and and H. Tang, “Cot4ad: A vision-language- [540] H.Z.TeqiangZouand,Y.Nong,Y.Li,K.Liu,H.Yang,X.Ling,X.Li,
actionmodelwithexplicitchain-of-thought,reasoningforautonomous and L. Ma, “Asynchronous fast-slow vision-language-action policies
driving,”CoRR,vol.abs/2511.22532,2025. for whole-body, robotic manipulation,” CoRR, vol. abs/2512.20188,
[520] W.D.Zhenghao”Mark”Pengand,Y.You,Y.Chen,W.Luo,T.Tian, 2025.
Y. Cao, A. Sharma, D. Xu, B. Ivanovic, B. Li, B. Zhou, Y. Wang, [541] M. Z. Junjie Wen and, J. Liu, Z. Liu, Y. Yang, L. Zhang, S. Zhang,
andM.Pavone,“CounterfactualVLA:self-reflectivevision-language- Y.Zhu,andY.Xu,“dvla:Diffusionvision-language-actionmodelwith
action model, with adaptive reasoning,” CoRR, vol. abs/2512.24426, multimodalchain-of-thought,”CoRR,vol.abs/2509.25681,2025.
2025. [542] Y.H.TravisDaviesand,A.Gladstone,Y.Liu,X.Chen,H.Ji,H.Liu,
[521] O. H. Daniel San Jose´ Pro and, R. Ro¨mer, M. Do¨sch, M. Schuck, and L. Hu, “Ebt-policy: Energy unlocks emergent physical reasoning
and A. P. Schoellig, “CRISP - compliant ROS2 controllers for capabilities,”CoRR,vol.abs/2510.27545,2025.
learning-based manipulation, policies and teleoperation,” CoRR, vol. [543] W. C. Michal Zawalski and, K. Pertsch, O. Mees, C. Finn, and
abs/2509.06819,2025. S.Levine,“Roboticcontrolviaembodiedchain-of-thoughtreasoning,”
[522] H.L.Yi-LinWeiand,Y.Lin,P.Wang,Z.Liang,G.Liu,andW.Zheng, in CoRL, ser. Proceedings of Machine Learning Research, vol. 270.
“Cyclemanip:Enablingcyclictaskmanipulationviaeffectivehistorical, PMLR,2024,pp.3157–3181.
perceptionandunderstanding,”CoRR,vol.abs/2512.01022,2025. [544] S. B. William Chen and, S. Mirchandani, O. Mees, D. Driess,
[523] H. L. Changyeon Kim and, Y. Seo, K. Lee, and Y. Zhu, “DEAS: K.Pertsch,andS.Levine,“Trainingstrategiesforefficientembodied
detachedvaluelearningwithactionsequenceforscalable,offlineRL,” reasoning,”CoRR,vol.abs/2505.08243,2025.
CoRR,vol.abs/2510.07730,2025. [545] Y. W. Yantai Yang and, Z. Wen, L. Zhongwei, C. Zou, Z. Zhang,
[524] L.H.HaiboHuand,N.Guan,andC.J.Xue,“Deead:Dynamicearly C. Wen, and L. Zhang, “Efficientvla: Training-free acceleration
exitofvision-languageactionforefficient,autonomousdriving,”CoRR, and compression for vision-language-action, models,” CoRR, vol.
vol.abs/2511.20720,2025. abs/2506.10100,2025.
[525] Y. L. Cheng Yin and, W. Xu, S. Tam, X. Zeng, Z. Liu, and Z. Yin, [546] M.Z.S.BinjieZhangand,“Ego-centricpredictivemodelconditioned
“Deepthinkvla: Enhancing reasoning capability of vision-language- onhandtrajectories,”CoRR,vol.abs/2508.19852,2025.
action,models,”CoRR,vol.abs/2511.15669,2025. [547] R. C. Zefu Lin and, C. Hanning, X. Wang, J. Xu, X. Jin, C. Wenbo,
[526] S.Wu,Y.Ji,Q.Li,Z.Zhang,Q.He,W.Xie,G.Zhang,B.Bayramli, H.Zhou,L.Fan,W.Li,andZ.Zhang,“Embodiedcoder:Parameterized
Y. Ding, and H. Lu, “Dejavu: Towards experience feedback learning embodiedmobilemanipulationviamodern,codingmodel,”CoRR,vol.
forembodiedintelligence,”arXivpreprint,2025. abs/2510.06207,2025.

30
[548] T. H. Nhat Chung and, T. Nguyen, H. Le, F. Bumgarner, D. M. H. [569] Z.D.YifanYangand,T.Xie,F.Cao,P.Shen,P.Song,P.Jin,G.Sun,
Nguyen,K.Vo,K.Yamazaki,C.Rainwater,T.Kieu,A.Nguyen,and S. Xu, Y. You, and J. Liu, “FPC-VLA: A vision-language-action
N.Le,“Rethinkingprogressionofmemorystateinroboticmanipula- framework with a supervisor, for failure prediction and correction,”
tion:An,object-centricperspective,”CoRR,vol.abs/2511.11478,2025. CoRR,vol.abs/2509.04018,2025.
[549] X. W. Zhehao Dong and, Z. Zhu, Y. Wang, Y. Wang, Y. Zhou, [570] J. L. Xin Wang and, Z. Weng, Y. Wang, Y. Gao, T. Pang, C. Du,
B.Wang,C.Ni,R.Ouyang,W.Qin,X.Chen,Y.Ye,andG.Huang, Y. Teng, Y. Wang, Z. Wu, X. Ma, and Y. Jiang, “Freezevla: Action-
“EMMA: generalizing real-world robot manipulation via generative, freezing attacks against vision-language-action, models,” CoRR, vol.
visualtransfer,”CoRR,vol.abs/2509.22407,2025. abs/2509.19870,2025.
[550] P.H.QiSunand,P.T.Deep,V.Toh,U.Tan,D.Ghosal,andS.Poria, [571] Q. Z. Weiqi Li and, R. Zhai, L. Lin, and G. Wang, “VLA models
“Emma-x:Anembodiedmultimodalactionmodelwithgroundedchain aremoregeneralizablethanyouthink:Revisitingphysical,andspatial
of,thoughtandlook-aheadspatialreasoning,”inACL(1). Association modeling,”CoRR,vol.abs/2512.02902,2025.
forComputationalLinguistics,2025,pp.14199–14214. [572] T.Y.TaoJiangand,Y.Liu,C.Lu,J.Cui,X.Liu,S.Cheng,J.Gao,
[551] L. B. Chikit Ng and, G. Wang, Y. Wang, H. Gao, K. Yuan, H.Xu,andH.Zhao,“Galaxeaopen-worlddatasetandG0dual-system
C. Jin, T. Zeng, and H. Ren, “Endovla: Dual-phase vision-language- VLAmodel,”CoRR,vol.abs/2509.00576,2025.
action model for autonomous tracking, in endoscopy,” CoRR, vol. [573] H. N. Arjun Vaithilingam Sudhakar and, M. Reymond, M. Liu,
abs/2505.15206,2025. J. Rajendran, and S. Chandar, “A generalist hanabi agent,” in ICLR.
[552] H.S.DelinQuand,Q.Chen,Z.Chen,X.Gao,X.Ye,Q.Lv,M.Shi, OpenReview.net,2025.
G.Ren,C.Ruan,M.Yao,H.Yang,J.Bao,B.Zhao,andD.Wang,“Em- [574] G. A. Team, “Gen-0: Embodied foundation models that scale with
bodiedonevision:Interleavedvision-text-actionpretrainingfor,general physicalinteraction,”arXivpreprint,2025.
robotcontrol,”CoRR,vol.abs/2508.21112,2025. [575] M. M. Ali Abouzeid and, Z. Sun, and D. Song, “Geoaware-vla:
[553] S.W.YiLiuand,D.Wei,X.Cai,L.Zhong,J.Yang,G.Ren,J.Zhang, Implicit geometry aware vision-language-action model,” CoRR, vol.
M. Yao, C. Li, X. He, L. Chen, and J. Luo, “Unified embodied abs/2509.14117,2025.
VLMreasoningwithroboticactionviaautoregressive,discretizedpre- [576] H. Z. Wenxuan Song and, P. Ding, C. Cui, S. Lyu, Y. Fan, and
training,”CoRR,vol.abs/2512.24125,2025. D.Wang,“Germ:Ageneralistroboticmodelwithmixture-of-experts
[554] G. W. Chang Nie and, Z. Lie, and H. Wang, “ERMV: editing 4d forquadruped,robot,”inIROS. IEEE,2024,pp.11879–11886.
robotic multi-view images to enhance embodied agents,” CoRR, vol. [577] P.D.HongyinZhangand,S.Lyu,Y.Peng,andD.Wang,“GEVRM:
abs/2507.17462,2025. goal-expressive video generation model for robust visual, manipula-
[555] Y. P. Chengmeng Li and, “Embodiment transfer learning for vision- tion,”inICLR. OpenReview.net,2025.
language-actionmodels,”CoRR,vol.abs/2511.01224,2025. [578] L. G. Shunlei Li and, J. Wang, C. Che, X. Xiao, J. Cao, Y. Hu,
[556] A.M.SamarthChopraand,B.Carnovale,E.Sokolson,R.Kubendran, and H. R. Karimi, “Information-theoretic graph fusion with vision-
and S. Dickerson, “Everydayvla: A vision-language-action model for language-actionmodel,forpolicyreasoninganddualroboticcontrol,”
affordablerobotic,manipulation,”CoRR,vol.abs/2511.05397,2025. CoRR,vol.abs/2508.05342,2025.
[557] Y. Z. Tao Lin and, Y. Du, J. Zhang, J. Liu, Y. Chen, E. Gu, Z. Liu, [579] M.C.MinghaoGuoand,J.Tao,R.Xu,Y.Yan,X.Liang,I.Laptev,
H. Cai, Y. Zou, L. Zou, Z. Zhou, G. Li, and B. Zhao, “Evo-1: andX.Chang,“Glad:Geometriclatentdistillationforvision-language-
Lightweight vision-language-action model with preserved semantic, actionmodels,”CoRR,vol.abs/2512.09619,2025.
alignment,”CoRR,vol.abs/2511.04555,2025. [580] J. Jabbour, D.-K. Kim, M. Smith, J. Patrikar, R. Ghosal, Y. Wang,
[558] Y. A. Shahram Najam Syed and, A. Jakobsson, and J. Ichnowski, A. Agha, V. J. Reddi, and S. Omidshafiei, “Dont run with scissors,”
“Expres-vla: Specializing vision-language-action models through ex- arXivpreprint,2025.
perience,replayandretrieval,”CoRR,vol.abs/2511.06202,2025. [581] A.A.GeminiRoboticsTeamand,S.Abeyruwan,J.Ainslie,J.Alayrac,
[559] Y. H. Jiashu Yang and, Y. Xie, N. Guo, and W. Lian, “Look, zoom, M.G.Arenas,A.Balakrishna,N.Batchelor,A.Bewley,J.T.Bingham,
understand:Theroboticeyeballforembodiedperception,”CoRR,vol. M. Bloesch, K. Bousmalis, P. Brakel, A. Brohan, T. Buschmann,
abs/2511.15279,2025. A.Byravan,S.Cabi,K.Caluwaerts,F.Casarini,C.Chan,O.Chang,
[560] W. K. Qi Lv and, H. Li, J. Zeng, Z. Qiu, D. Qu, H. Song, Q. Chen, L.Chappellet-Volpini,J.E.Chen,X.Chen,H.L.Chiang,K.Choro-
X. Deng, and J. Pang, “F1: A vision-language-action model bridging manski,A.Collister,D.B.D’Ambrosio,S.Dasari,T.Davchev,M.K.
understandingand,generationtoactions,”CoRR,vol.abs/2509.06951, Dave, C. Devin, N. D. Palo, T. Ding, C. Doersch, A. Dostmohamed,
2025. Y. Du, D. Dwibedi, S. T. Egambaram, M. Elabd, T. Erez, X. Fang,
[561] J.D.ZijunLinand,H.Fang,D.Fox,R.Krishna,C.Tan,andB.Wen, C.Fantacci,C.Fong,E.Frey,C.Fu,R.Gao,M.Giustina,K.Gopalakr-
“Failsafe: Reasoning and recovery from failures in vision-language- ishnan, L. Graesser, O. Groth, A. Gupta, R. Hafner, S. Hansen,
action,models,”CoRR,vol.abs/2510.01642,2025. L. Hasenclever, S. Haves, N. Heess, B. Hernaez, A. Hofer, J. Hsu,
[562] Q. Z. Jiajun Cao and, P. Jia, X. Zhao, B. Lan, X. Zhang, X. Wei, L.Huang,S.H.Huang,A.Iscen,M.G.Jacob,D.Jain,S.Jesmonth,
S.Chen,Z.Li,Y.Wang,L.Li,X.Liu,M.Lu,andS.Zhang,“Fast- A. Jindal, R. Julian, D. Kalashnikov, M. E. Karagozler, S. Karp,
drivevla:Efficientend-to-enddrivingviaplug-and-playreconstruction- M.Kecman,J.C.Kew,D.Kim,F.Kim,J.Kim,T.Kipf,S.Kirmani,
based,tokenpruning,”CoRR,vol.abs/2507.23318,2025. K. Konyushkova, L. Y. Ku, Y. Kuang, T. Lampe, A. Laurens, T. A.
[563] H.Chen,J.Liu,C.Gu,Z.Liu,R.Zhang,X.Li,andX.He,“Fast-in- Le, I. Leal, A. X. Lee, T. E. Lee, G. Lever, J. Liang, L. Lin, F. Liu,
slow:Adual-systemvlamodelunifyingfastmanipulationwithinslow S.Long,C.Lu,S.Maddineni,A.Majumdar,K.Maninis,A.Marmon,
reasoning,”arXivpreprint,2025. S.Martinez,A.H.Michaely,andN.Milonopoulos,“Geminirobotics
[564] J. W. Ruijie Zheng and, S. Reed, J. Bjorck, Y. Fang, F. Hu, J. Jang, 1.5:Pushingthefrontierofgeneralistrobotswith,advancedembodied
K. Kundalia, Z. Lin, L. Magne, A. Narayan, Y. L. Tan, G. Wang, reasoning,thinking,andmotiontransfer,”CoRR,vol.abs/2510.03342,
Q. Wang, J. Xiang, Y. Xu, S. Ye, J. Kautz, F. Huang, Y. Zhu, and 2025.
L.Fan,“FLARE:robotlearningwithimplicitworldmodeling,”CoRR, [582] K. Z. Zijian Zhang and, Z. Chen, J. Jang, Y. Li, C. Wang, M. Ding,
vol.abs/2505.15659,2025. D.Fox,andH.Yao,“GRAPE:generalizingrobotpolicyviapreference
[565] H. Z. Moritz Reuss and, M. Ru¨hle, O¨. E. Yagmurlu, F. Otto, alignment,”CoRR,vol.abs/2411.19309,2024.
and R. Lioutikov, “FLOWER: democratizing generalist robot poli- [583] M.C.HelongHuangand,K.Tan,X.Quan,G.Huang,andH.Zhang,
cies with efficient vision-language-action, flow policies,” CoRR, vol. “Graphcot-vla: A 3d spatial-aware reasoning vision-language-action,
abs/2509.04996,2025. model for robotic manipulation with ambiguous instructions,” CoRR,
[566] Z.Zhong,H.Yan,J.Li,X.Liu,X.Gong,T.Zhang,W.Song,J.Chen, vol.abs/2508.07650,2025.
X.Zheng,H.Wang,andH.Li,“Flowvla:Visualchainofthought-based [584] M.Y.ShengliangDengand,S.Wei,H.Ma,Y.Yang,J.Chen,Z.Zhang,
motion reasoning for vision-language-action models,” arXiv preprint, T. Yang, X. Zhang, H. Cui, Z. Zhang, and H. Wang, “Graspvla: a
2025. graspingfoundationmodelpre-trainedonbillion-scale,syntheticaction
[567] H. L. Jiawen Yu and, Q. Yu, J. Ren, C. Hao, H. Ding, G. Huang, data,”CoRR,vol.abs/2505.03233,2025.
G.Huang,Y.Song,P.Cai,C.Lu,andW.Zhang,“Forcevla:Enhancing [585] Z.F.Mae¨licNeauand,P.E.Santos,A.Bosser,andC.Buche,“Grasp-
VLAmodelswithaforce-awaremoeforcontact-rich,manipulation,” vla: Graph-based symbolic action representation for long-horizon,
CoRR,vol.abs/2505.22159,2025. planningwithVLApolicies,”CoRR,vol.abs/2511.04357,2025.
[568] S. L. Yanjia Huang and, S. Liu, Q. Xu, M. Wu, X. Gao, and [586] G. C. Ruoshi Wen and, Z. Cui, M. Du, Y. Gou, Z. Han, L. Huang,
Z.Tu,“Forge-tree:Diffusion-forcingtreesearchforlong-horizonrobot M.Lei,Y.Li,Z.Li,W.Liu,Y.Liu,X.Ma,H.Niu,Y.Ouyang,Z.Ren,
manipulation,”CoRR,vol.abs/2510.21744,2025. H. Shi, W. Xu, H. Zhang, J. Zhang, X. Zhang, L. Zheng, W. Zhong,

31
Y. Zhou, Z. Zhu, and H. Li, “Gr-dexter technical report,” CoRR, vol. [608] Y. N. Bahey Tharwat and, A. Abouzeid, and I. Reid, “Latent action
abs/2512.24210,2025. pretraining through world modeling,” CoRR, vol. abs/2509.18428,
[587] X.M.YunfeiLiand,J.Xu,Y.Cui,Z.Cui,Z.Han,L.Huang,T.Kong, 2025.
Y. Liu, H. Niu, W. Peng, J. Qiao, Z. Ren, H. Shi, Z. Su, J. Tian, [609] K. C. Shuhan Tan and, Y. Chen, R. Tian, Y. You, Y. Wang,
Y. Xiao, S. Zhang, L. Zheng, H. Li, and Y. Wu, “GR-RL: going W.Luo,Y.Cao,P.Kra¨henbu¨hl,M.Pavone,andB.Ivanovic,“Latent
dexterous and precise for long-horizon robotic manipulation,” CoRR, chain-of-thought world modeling for end-to-end driving,” CoRR, vol.
vol.abs/2512.01801,2025. abs/2512.10226,2025.
[588] Y. D. Yi Li and, J. Zhang, J. Jang, M. Memmel, C. R. Garrett, [610] W. C. Ameesh Shah and, A. Godbole, F. Mora, S. A. Seshia, and
F. Ramos, D. Fox, A. Li, A. Gupta, and A. Goyal, “HAMSTER: S.Levine,“Learningaffordancesatinference-timeforvision-language-
hierarchical action models for open-world robot manipulation,” in action,models,”CoRR,vol.abs/2510.19752,2025.
ICLR. OpenReview.net,2025. [611] K.D.G.JustinWilliamsand,R.George,andM.Sarkar,“LiteVLA:
[589] FIGURE, “Helix: A vision-language-action model for generalist hu- efficient vision-language-action control on cpu-bound, edge robots,”
manoidcontrol,”arXivpreprint,2025. CoRR,vol.abs/2511.05642,2025.
[590] P.D.MinghuiLinand,S.Wang,Z.Zhuang,Y.Liu,X.Tong,W.Song, [612] J. S. Yi Yang and, S. Kou, Y. Wang, and Z. Deng, “Lohovla:
S. Lyu, S. Huang, and D. Wang, “Hif-vla: Hindsight, insight and A unified vision-language-action model for long-horizon, embodied
foresight through motion representation, for vision-language-action tasks,”CoRR,vol.abs/2506.00411,2025.
models,”CoRR,vol.abs/2512.09928,2025. [613] X. G. Xiaofan Wang and, J. Fu, Z. Li, D. Fortier, G. Mullins,
[591] B.L.ZhiyingDuand,Y.Liang,Y.Shen,H.Cao,X.Zheng,Z.Feng, A. Kolobov, and B. Guo, “Lola: Long horizon latent action learning
Z. Wu, J. Yang, and Y. Jiang, “Himoe-vla: Hierarchical mixture-of- forgeneralrobotmanipulation,”CoRR,vol.abs/2512.20166,2025.
experts for generalist vision-language-action, policies,” CoRR, vol. [614] P. D. Yiguo Fan and, S. Bai, X. Tong, Y. Zhu, H. Lu, F. Dai,
abs/2512.05693,2025. W.Zhao,Y.Liu,S.Huang,Z.Fan,B.Chen,andD.Wang,“Long-vla:
[592] R.Z.GuanxingLuand,H.Lin,H.Zhang,andY.Tang,“Human-in- Unleashing long-horizon capability of vision language action, model
the-loop online rejection sampling for robotic manipulation,” CoRR, forrobotmanipulation,”CoRR,vol.abs/2508.19958,2025.
vol.abs/2510.26406,2025. [615] T. Z. Boyuan Chen and, H. Geng, K. Song, C. Zhang, P. Li, W. T.
[593] B.I.LucyXiaoyangShiand,M.R.Equi,L.Ke,K.Pertsch,Q.Vuong, Freeman, J. Malik, P. Abbeel, R. Tedrake, V. Sitzmann, and Y. Du,
J. Tanner, A. Walling, H. Wang, N. Fusai, A. Li-Bell, D. Driess, “Largevideoplannerenablesgeneralizablerobotcontrol,”CoRR,vol.
L.Groom,S.Levine,andC.Finn,“Hirobot:Open-endedinstruction abs/2512.15840,2025.
followingwithhierarchicalvision-language-action,models,”inICML. [616] K. G. Yi Yang and, Y. Wen, H. Li, Y. Zhao, T. Wang, and X. Liu,
OpenReview.net,2025. “Maniagent:Anagenticframeworkforgeneralroboticmanipulation,”
[594] Y.G.JiankeZhangand,X.Chen,Y.Wang,Y.Hu,C.Shi,andJ.Chen, CoRR,vol.abs/2510.11660,2025.
“Hirt:Enhancingroboticcontrolwithhierarchicalrobottransformers,” [617] X. L. Yi Yang and, Y. Chen, J. Song, Y. Wang, Z. Xiao, J. Su,
in CoRL, ser. Proceedings of Machine Learning Research, vol. 270. Y. Qiaoben, P. Liu, and Z. Deng, “Mantis: A versatile vision-
PMLR,2024,pp.933–946. language-actionmodelwithdisentangled,visualforesight,”CoRR,vol.
[595] Y.Z.Xinyu Xuand,Y.Li, L.Han,andC. Lu,“Humanvla:Towards abs/2511.16175,2025.
vision-languagedirectedobjectrearrangementby,physicalhumanoid,” [618] J. L. Chenyang Gu and, H. Chen, R. Huang, Q. Wuwu, Z. Liu,
inNeurIPS,2024. X. Li, Y. Li, R. Zhang, P. Jia, P. Heng, and S. Zhang, “Manualvla:
[596] C. X. Yuan Zhang and, W. Xu, C. Ji, J. Wu, and J. Pan, “iflybot-vla A unified VLA model for chain-of-thought manual generation, and
technicalreport,”CoRR,vol.abs/2511.01914,2025. roboticmanipulation,”CoRR,vol.abs/2512.02013,2025.
[597] W.G.DekunLuandandK.Jia,“Imaginationpolicy:Towardsgener- [619] W. G. Runhao Li and, Z. Wu, C. Wang, H. Deng, Z. Weng,
alizable,preciseandreliableend-to-end,policyforroboticmanipula- Y.Tan,andZ.Wang,“MAP-VLA:memory-augmentedpromptingfor
tion,”CoRR,vol.abs/2509.20841,2025. vision-language-action model, in robotic manipulation,” CoRR, vol.
[598] H.G.HaohanChiand,Z.Liu,J.Liu,C.Liu,J.Li,K.Yang,Y.Yu, abs/2511.09516,2025.
Z. Wang, W. Li, L. Wang, X. Hu, H. Sun, H. Zhao, and H. Zhao, [620] J. Z. Zhihao Zhan and, L. Zhang, Q. Lv, H. Liu, J. Zhang, W. Li,
“Impromptu VLA: open weights and open data for driving vision- Z. Chen, T. Chen, K. Wang, L. Lin, and G. Wang, “E 0: Enhancing
language-action,models,”CoRR,vol.abs/2505.23757,2025. generalizationandfine-grained,controlinVLAmodelsviacontinuized
[599] Z.S.UlasBerkKarliandandT.Fitzgerald,“INSIGHT:inference-time discretediffusion,”CoRR,vol.abs/2511.21542,2025.
sequenceintrospectionforgeneratinghelp,triggersinvision-language- [621] O¨.E.Y.MoritzReussand,F.Wenzel,andR.Lioutikov,“Multimodal
actionmodels,”CoRR,vol.abs/2510.01389,2025. diffusion transformer: Learning versatile behavior from, multimodal
[600] H.L.ShuaiYangand,Y.Chen,B.Wang,Y.Tian,T.Wang,H.Wang, goals,”inRobotics:ScienceandSystems,2024.
F. Zhao, Y. Liao, and J. Pang, “Instructvla: Vision-language-action [622] J. P. Ajay Sridhar and, S. Sharma, and C. Finn, “Memer: Scaling
instruction tuning from understanding, to manipulation,” CoRR, vol. up memory for robot control via experience retrieval,” CoRR, vol.
abs/2507.17520,2025. abs/2510.20328,2025.
[601] K.G.YanduChenand,Y.Wen,Y.Zhao,T.Wang,andL.Nie,“Inten- [623] B.X.HaoShiand,Y.Liu,L.Sun,F.Liu,T.Wang,E.Zhou,H.Fan,
tionvla: Generalizable and efficient embodied intention reasoning, for X.Zhang,andG.Huang,“Memoryvla:Perceptual-cognitivememoryin
human-robotinteraction,”CoRR,vol.abs/2510.07778,2025. vision-language-action models, for robotic manipulation,” CoRR, vol.
[602] B.M.NanSunand,Y.Li,C.Wang,D.Guo,andH.Liu,“Transforming abs/2508.19236,2025.
monolithicfoundationmodelsintoembodiedmulti-agent,architectures [624] Z. Y. Chen Li and, H. Zhang, F. Chen, C. Zhu, A. Bolimera, and
forhuman-robotcollaboration,”CoRR,vol.abs/2512.00797,2025. M.Savvides,“Metavla:Unifiedmetaco-trainingforefficientembodied
[603] Y. C. Xinyi Chen and, Y. Fu, N. Gao, J. Jia, W. Jin, H. Li, Y. Mu, adaption,”CoRR,vol.abs/2510.05580,2025.
J. Pang, Y. Qiao, Y. Tian, B. Wang, B. Wang, F. Wang, H. Wang, [625] D. K. Suhyeok Jang and, C. Kim, Y. Kim, and J. Shin, “Verifier-
T. Wang, Z. Wang, X. Wei, C. Wu, S. Yang, J. Ye, J. Yu, J. Zeng, freetest-timesamplingforvisionlanguageactionmodels,”CoRR,vol.
J. Zhang, J. Zhang, S. Zhang, F. Zheng, B. Zhou, and Y. Zhu, abs/2510.05681,2025.
“Internvla-m1: A spatially guided vision-language-action framework, [626] I.Z.HaoyunLiand,R.Ouyang,X.Wang,Z.Zhu,Z.Yang,Z.Zhang,
forgeneralistrobotpolicy,”CoRR,vol.abs/2510.13778,2025. B. Wang, C. Ni, W. Qin, X. Chen, Y. Ye, G. Huang, Z. Song, and
[604] J.Z.YanjiangGuoand,X.Chen,X.Ji,Y.Wang,Y.Hu,andJ.Chen, X.Wang,“Mimicdreamer:Aligninghumanandrobotdemonstrations
“Improving vision-language-action model with online reinforcement forscalable,VLAtraining,”CoRR,vol.abs/2509.22199,2025.
learning,”inICRA. IEEE,2025,pp.15665–15672. [627] D. Z. Haoyu Fu and, Z. Zhao, J. Cui, H. Xie, B. Wang, G. Chen,
[605] Y.G.AnqingJiangand,Y.Wang,Z.Sun,S.Wang,Y.Heng,H.Sun, D.Liang,andX.Bai,“Minddrive:Avision-language-actionmodelfor
S. Tang, L. Zhu, J. Chai, J. Wang, Z. Gu, H. Jiang, and L. Sun, autonomous driving, via online reinforcement learning,” CoRR, vol.
“IRL-VLA:traininganvision-language-actionpolicyviarewardworld, abs/2512.13636,2025.
model,”CoRR,vol.abs/2508.06571,2025. [628] S. X. Peijun Tang and, B. Sun, B. Huang, K. Luo, H. Yang, W. Jin,
[606] W.Xu,L.Zhuang,andL.Shan,“Kv-efficientvla:Amethodtospeed andJ.Wang,“Mindtohand:Purposefulroboticcontrolviaembodied
up vision language models with rnn-gated chunked kv cache,” arXiv reasoning,”CoRR,vol.abs/2512.08580,2025.
preprint,2025. [629] X. W. Zhenhan Yin and, J. Jiang, K. Deng, P. Chen, S. Li, C. Liu,
[607] X. G. Zuolei Li and, X. Wang, and J. Fu, “Latbot: Distilling uni- X.Xu,J.Song,L.Gao,andH.T.Shen,“Mivla:Towardsgeneralizable
versal latent actions for vision-language-action, models,” CoRR, vol. vision-language-actionmodelwithhuman-robot,mutualimitationpre-
abs/2511.23034,2025. training,”CoRR,vol.abs/2512.15411,2025.

32
[630] J. L. Zhuoyang Liu and, J. Xu, N. Han, C. Gu, H. Chen, K. Zhou, [650] S.Y.JulongWeiand,P.Li,Q.Hu,Z.Gan,andW.Ding,“Occllama:An
R. Zhang, K. Hsieh, K. Wu, Z. Che, J. Tang, and S. Zhang, “MLA: occupancy-language-action generative world model for, autonomous
Amultisensorylanguage-actionmodelformultimodalunderstanding, driving,”CoRR,vol.abs/2409.03272,2024.
andforecastinginroboticmanipulation,”CoRR,vol.abs/2509.26642, [651] L.K.RuixunLiuand,D.Li,andH.Zhao,“Occvla:Vision-language-
2025. action model with implicit 3d occupancy supervision,” CoRR, vol.
[631] X.C.HaotianLiangand,B.Wang,M.Chen,Y.Liu,Y.Zhang,Z.Chen, abs/2509.05578,2025.
T.Yang,Y.Chen,J.Pang,D.Liu,X.Yang,Y.Mu,W.Shao,andP.Luo, [652] H.D.TianyiZhangand,H.Hao,Y.Qiao,J.Dai,andZ.Hou,“Ground-
“MM-ACT:learnfrommultimodalparallelgenerationtoact,”CoRR, ing actions in camera space: Observation-centric vision-language-
vol.abs/2512.00975,2025. action,policy,”CoRR,vol.abs/2508.13103,2025.
[632] G.W.DongJingand,J.Liu,W.Tang,Z.Sun,Y.Yao,Z.Wei,Y.Liu, [653] S. C. Zihao Wang and, Z. Mu, H. Lin, C. Zhang, X. Liu, Q. Li,
Z.Lu,andM.Ding,“Mixtureofhorizonsinactionchunking,”CoRR, A.Liu,X.S.Ma,andY.Liang,“Omnijarvis:Unifiedvision-language-
vol.abs/2511.19433,2025. actiontokenizationenablesopen-world,instructionfollowingagents,”
[633] N. S. Dmytro Kuzmenko and, “Moira: Modular instruction routing inNeurIPS,2024.
architectureformulti-taskrobotics,”CoRR,vol.abs/2507.01843,2025. [654] Q. N. Pei Liu and, X. Lu, H. Liu, W. Ma, D. She, P. Jia, X. Lang,
[634] M. X. Chengshu Li and, A. Bahety, H. Yin, Y. Jiang, H. Huang, and J. Ma, “Omnireason: A temporal-guided vision-language-action
J.Wong,S.Garlanka,C.Gokmen,R.Zhang,W.Liu,J.Wu,R.Mart´ın- framework for, autonomous driving,” CoRR, vol. abs/2509.00789,
Mart´ın, and L. Fei-Fei, “Momagen: Generating demonstrations under 2025.
soft and hard constraints, for multi-step bimanual mobile manipula- [655] C.C.HuaihaiLyuand,S.Xie,P.Wang,X.Chen,S.Zhang,andC.Xu,
tion,”CoRR,vol.abs/2510.18316,2025. “Omnisat: Compact action token, faster auto regression,” CoRR, vol.
[635] Y. Z. Zhenyu Wu and, X. Xu, Z. Wang, and H. Yan, “Momanipvla: abs/2510.09667,2025.
Transferringvision-language-actionmodelsforgeneral,mobilemanip- [656] C.G.NoriakiHiroseand,D.Shah,andS.Levine,“Omnivla:Anomni-
ulation,” in CVPR. Computer Vision Foundation / IEEE, 2025, pp. modalvision-language-actionmodelforrobotnavigation,”CoRR,vol.
1714–1723. abs/2509.19480,2025.
[636] Y. W. Shuo Wang and, W. Li, Y. Wang, M. Chen, K. Wang, [657] R.N.FanqiLinand,Y.Hu,J.You,J.Zhao,andY.Gao,“Onetwovla:A
Z. Su, X. Cai, Y. Jin, D. Li, and Z. Fan, “Monodream: Monocular unifiedvision-language-actionmodelwithadaptive,reasoning,”CoRR,
vision-language navigation with panoramic dreaming,” CoRR, vol. vol.abs/2505.11917,2025.
abs/2508.02549,2025. [658] M. L. Zihao Wang and, K. He, X. Wang, Z. Mu, A. Liu, and
Y.Liang,“Openha:Aseriesofopen-sourcehierarchicalagenticmodels
[637] T.X.AustinStoneand,Y.Lu,K.Gopalakrishnan,K.Lee,Q.Vuong,
inminecraft,”CoRR,vol.abs/2509.13347,2025.
P.Wohlhart,S.Kirmani,B.Zitkovich,F.Xia,C.Finn,andK.Hausman,
“Open-world object manipulation using pre-trained vision-language [659] K. P. Moo Jin Kim and, S. Karamcheti, T. Xiao, A. Balakrishna,
models,” in CoRL, ser. Proceedings of Machine Learning Research, S. Nair, R. Rafailov, E. P. Foster, P. R. Sanketi, Q. Vuong, T. Kollar,
vol.229. PMLR,2023,pp.3397–3417. B.Burchfiel,R.Tedrake,D.Sadigh,S.Levine,P.Liang,andC.Finn,
“Openvla: An open-source vision-language-action model,” in CoRL,
[638] W.S.HanZhaoand,D.Wang,X.Tong,P.Ding,X.Cheng,andZ.Ge,
ser. Proceedings of Machine Learning Research, vol. 270. PMLR,
“More:Unlockingscalabilityinreinforcementlearningforquadruped,
2024,pp.2679–2713.
vision-language-action models,” in ICRA. IEEE, 2025, pp. 11212–
[660] F. L. Huang Huang and, L. Fu, T. Wu, M. Mukadam, J. Malik,
11218.
K.Goldberg,andP.Abbeel,“OTTER:Avision-language-actionmodel
[639] R. Z. Chengbo Yuan and, M. Liu, Y. Hu, S. Wang, L. Yi, C. Wen,
withtext-awarevisualfeature,extraction,”inICML. OpenReview.net,
S. Zhang, and Y. Gao, “Motiontrans: Human VR data enable
2025.
motion-level learning for robotic, manipulation policies,” CoRR, vol.
[661] S.L.XiaopengLinand,B.Yu,R.Yang,C.Wu,Y.Miao,Y.Jin,Y.Shi,
abs/2509.17759,2025.
C.Huang,B.Cheng,andK.Chen,“Physbrain:Humanegocentricdata
[640] A.M.ZhenyuWuand,X.Xu,H.Yin,Y.Liang,Z.Wang,J.Lu,and
as a bridge from vision language, models to physical intelligence,”
H. Yan, “Moto: A zero-shot plug-in interaction-aware navigation for
CoRR,vol.abs/2512.16793,2025.
general,mobilemanipulation,”CoRR,vol.abs/2509.01658,2025.
[662] J.L.ZhihaoWangand,J.Zheng,W.Zhang,D.Liu,Y.Zheng,H.Niu,
[641] J. Z. Alexander Spiridonov and, N. Nikolov, L. V. Gool, and D. P.
J. Yu, and X. Zhan, “Physiagent: An embodied agent framework in
Paudel, “Generalist robot manipulation beyond action labeled data,”
physicalworld,”CoRR,vol.abs/2509.24524,2025.
CoRR,vol.abs/2509.19958,2025.
[663] K.Chen,Z.Liu,T.Zhang,Z.Guo,S.Xu,H.Lin,H.Zang,Q.Zhang,
[642] H.T.HongzheBiand,S.Xie,Z.Wang,S.Huang,H.Liu,R.Zhao,
Z. Yu, G. Fan, T. Huang, Y. Wang, and C. Yu, “πrl: Online RL
Y. Feng, C. Xiang, Y. Rong, H. Zhao, H. Liu, Z. Su, L. Ma, H. Su,
fine-tuningforflow-basedvision-language-actionmodels,”CoRR,vol.
andJ.Zhu,“Motus:Aunifiedlatentactionworldmodel,”CoRR,vol.
abs/2510.25889,2025.
abs/2512.13030,2025.
[664] G.S.WenqiLiangand,Y.He,J.Dong,S.Dai,I.Laptev,S.H.Khan,
[643] X. S. Pu Zhao and, Z. Kong, Y. Shen, S. Chang, A. Akbari, T. Rup- andY.Cong,“Pixelvla:Advancingpixel-levelunderstandinginvision-
precht, L. Lu, E. Nan, C. Yang, Y. He, W. Shi, X. Xu, Y. Huang, language-action,model,”CoRR,vol.abs/2511.01571,2025.
W. Jiang, W. Wang, Y. Chen, Y. He, and Y. Wang, “Open-source
[665] E. L. H. Yi Zhang and, K. Chao, N. Petrovic, Y. Song, C. Wu,
multimodalmoxinmodelswithmoxin-vlmandmoxin-vla,”CoRR,vol.
and A. Knoll, “A unified perception-language-action framework for
abs/2512.22208,2025. adaptiveautonomous,driving,”CoRR,vol.abs/2507.23540,2025.
[644] F.J.PeilongHanand,M.Zhang,Y.Qiu,H.Tang,Y.Zheng,T.Wang, [666] J.Z.HangYuand,Y.Liu,K.Li,C.Ma,D.Zhang,Y.Hu,G.Chen,
andJ.Hao,“MUVLA:learningtoexploreobjectnavigationviamap J.Xie,J.Guo,J.Zhao,andY.Gao,“Pointwhatyoumean:Visually
understanding,”CoRR,vol.abs/2509.25966,2025. groundedinstructionpolicy,”CoRR,vol.abs/2512.18933,2025.
[645] Y.J.An-ChiehChengand,Z.Yang,X.Zou,J.Kautz,E.Biyik,H.Yin, [667] X. W. Ziwen Li and, H. Zhang, R. Chen, R. Lin, X. He, H. Huang,
S. Liu, and X. Wang, “Navila: Legged robot vision-language-action Y. Guo, F. Karray, T. Liu, and M. Gong, “Posa-vla: Enhancing
modelfornavigation,”CoRR,vol.abs/2412.04453,2024. action generation via pose-conditioned anchor, attention,” CoRR, vol.
[646] M. P. Sajjad Pakdamansavoji and, A. Sigal, Z. Li, R. H. Yang, and abs/2512.03724,2025.
A. Rasouli, “Improving robotic manipulation robustness via NICE [668] Z. H. Jiahui Zhang and, C. Gu, Z. Ma, and L. Zhang, “Reinforcing
scenesurgery,”CoRR,vol.abs/2511.22777,2025. actionpoliciesbyprophesying,”CoRR,vol.abs/2511.20633,2025.
[647] L.Magne,A.Awadalla,G.Wang,Y.Xu,J.Belofsky,F.Hu,J.Kim, [669] H. K. Seongmin Park and, W. Jeon, J. Yang, B. Jeon, Y. Oh, and
L. Schmidt, G. Gkioxari, J. Kautz, Y. Yue, Y. Choi, Y. Zhu, and J. Choi, “Quantization-aware imitation-learning for resource-efficient
L.J.Fan,“Nitrogen:Anopenfoundationmodelforgeneralistgaming robotic,control,”CoRR,vol.abs/2412.01034,2024.
agents,”arXivpreprint,2026. [670] Y. C. Yixuan Li and, M. Zhou, and H. Li, “Qdepth-vla: Quantized
[648] D. D. Rokas Bendikas and, M. Peschl, S. Haresh, and P. Mazzaglia, depth prediction as auxiliary supervision for, vision-language-action
“Focusing on what matters: Object-agent-centric tokenization for vi- models,”CoRR,vol.abs/2510.14836,2025.
sion,languageactionmodels,”CoRR,vol.abs/2509.23655,2025. [671] Q. V. Yevgen Chebotar and, K. Hausman, F. Xia, Y. Lu, A. Irpan,
[649] T.H.KhoaVoand,Y.Ikebe,T.Pham,N.Chung,M.N.Vu,D.N.H. A.Kumar,T.Yu,A.Herzog,K.Pertsch,K.Gopalakrishnan,J.Ibarz,
Minh,A.Nguyen,A.Gunderman,C.Rainwater,andN.Le,“Clutter- O.Nachum,S.A.Sontakke,G.Salazar,H.T.Tran,J.Peralta,C.Tan,
resistant vision-language-action models through object-centric, and D. Manjunath, J. Singh, B. Zitkovich, T. Jackson, K. Rao, C. Finn,
geometrygrounding,”CoRR,vol.abs/2512.22519,2025. andS.Levine,“Q-transformer:Scalableofflinereinforcementlearning

33
viaautoregressive,q-functions,”inCoRL,ser.ProceedingsofMachine lifelong, scalable, and robust multi-robot collaboration,” CoRR, vol.
LearningResearch,vol.229. PMLR,2023,pp.3909–3928. abs/2510.26536,2025.
[672] P.D.XinyangTongand,Y.Fan,D.Wang,W.Zhang,C.Cui,M.Sun, [692] J.D.WentaoYuanand,V.Blukis,W.Pumacay,R.Krishna,A.Murali,
H. Zhao, H. Zhang, Y. Dang, S. Huang, and S. Lyu, “Quart-online: A.Mousavian,andD.Fox,“Robopoint:Avision-languagemodelfor
Latency-free multimodal large language model for quadruped, robot spatialaffordanceprediction,inrobotics,”inCoRL,ser.Proceedingsof
learning,”inICRA. IEEE,2025,pp.9533–9539. MachineLearningResearch,vol.270. PMLR,2024,pp.4005–4020.
[673] L.F.JustinYuand,H.Huang,K.El-Refai,R.A.Ambrus,R.Cheng, [693] C. Y. Boshi An and and R. K. Katzschmann, “Robotic assistant:
M. Z. Irshad, and K. Goldberg, “Real2render2real: Scaling robot Completingcollaborativetaskswithdexterousvision-language-action,
data without dynamics simulation or, robot hardware,” CoRR, vol. models,”CoRR,vol.abs/2510.25713,2025.
abs/2505.09601,2025. [694] P. L. Xinghang Li and, M. Liu, D. Wang, J. Liu, B. Kang, X. Ma,
[674] L. W. Songming Liu and, B. Li, H. Tan, H. Chen, Z. Wang, K. Xu, T. Kong, H. Zhang, and H. Liu, “Towards generalist robot policies:
H.Su,andJ.Zhu,“RDT-1B:adiffusionfoundationmodelforbimanual Whatmattersinbuildingvision-language-action,models,”CoRR,vol.
manipulation,”inICLR. OpenReview.net,2025. abs/2412.14058,2024.
[675] Z.Y.DapengZhangand,Z.Chen,C.Liao,Y.Chen,F.Shen,Q.Zhou, [695] Z.W.JianingGuoand,C.Tu,Y.Ma,X.Kong,Z.Liu,J.Ji,S.Zhang,
andT.Chua,“Reasoning-vla:Afastandgeneralvision-language-action Y.Chen,K.Chen,Q.Dou,Y.Yang,X.Liu,H.Zhao,W.Lv,andS.Li,
reasoning,modelforautonomousdriving,”CoRR,vol.abs/2511.19912, “On robustness of vision-language-action model against multi-modal,
2025. perturbations,”CoRR,vol.abs/2510.00037,2025.
[676] Y. Z. Pengxiang Li and, Y. Wang, H. Wang, H. Zhao, J. Liu, [696] L. L. Mingtong Dai and, Y. Bai, Y. Liu, Z. Wang, R. SU, C. Chen,
X. Zhan, K. Zhan, and X. Lang, “Discrete diffusion for reflective L.Lin,andX.Wu,“Rover:Robotrewardmodelastest-timeverifier
vision-language-action models in, autonomous driving,” CoRR, vol. forvision-language-action,model,”CoRR,vol.abs/2510.10975,2025.
abs/2509.20109,2025. [697] W.B.TobiasJu¨lgandandF.Walter,“Refinedpolicydistillation:From
[677] S. D. Kaustubh Sridhar and, D. Jayaraman, and I. Lee, “REGENT: VLA generalists to RL experts,” in IROS. IEEE, 2025, pp. 11677–
Aretrieval-augmentedgeneralistagentthatcanactin-context,innew 11684.
environments,”inICLR. OpenReview.net,2025. [698] J.L.TaeyoungKimand,M.Koo,D.Kim,K.Lee,C.Kim,Y.Seo,and
[678] C.W.WenlongHuangand,Y.Li,R.Zhang,andL.Fei-Fei,“Rekep: J.Shin,“Contrastiverepresentationregularizationforvision-language-
Spatio-temporalreasoningofrelationalkeypointconstraints,forrobotic action,models,”CoRR,vol.abs/2510.01711,2025.
manipulation,” in CoRL, ser. Proceedings of Machine Learning Re- [699] T. Y. Brianna Zitkovich and, S. Xu, P. Xu, T. Xiao, F. Xia, J. Wu,
search,vol.270. PMLR,2024,pp.4573–4602. P. Wohlhart, S. Welker, A. Wahid, Q. Vuong, V. Vanhoucke, H. T.
[679] Z.Z.YajatYadavand,A.Wagenmaker,K.Pertsch,andS.Levine,“Ro- Tran, R. Soricut, A. Singh, J. Singh, P. Sermanet, P. R. Sanketi,
bustfinetuningofvision-language-actionrobotpoliciesviaparameter, G.Salazar,M.S.Ryoo,K.Reymann,K.Rao,K.Pertsch,I.Mordatch,
merging,”CoRR,vol.abs/2512.08333,2025. H.Michalewski,Y.Lu,S.Levine,L.Lee,T.E.Lee,I.Leal,Y.Kuang,
[680] T.C.JiyeonKooand,H.Kang,E.Pyo,T.G.Oh,T.Kim,andA.J. D. Kalashnikov, R. Julian, N. J. Joshi, A. Irpan, B. Ichter, J. Hsu,
Choi,“Retovla:Reusingregistertokensforspatialreasoninginvision- A. Herzog, K. Hausman, K. Gopalakrishnan, C. Fu, P. Florence,
language-action,models,”CoRR,vol.abs/2509.21243,2025. C.Finn,K.A.Dubey,D.Driess,T.Ding,K.M.Choromanski,X.Chen,
[681] J.Z.SombitDeyand,N.Nikolov,L.V.Gool,andD.P.Paudel,“Revla: Y. Chebotar, J. Carbajal, N. Brown, A. Brohan, M. G. Arenas, and
Reverting visual domain limitation of robotic foundation models,” in K.Han,“RT-2:vision-language-actionmodelstransferwebknowledge
ICRA. IEEE,2025,pp.8679–8686. to robotic, control,” in CoRL, ser. Proceedings of Machine Learning
[682] S.D.KaustubhSridharand,D.Jayaraman,andI.Lee,“RICL:adding Research,vol.229. PMLR,2023,pp.2165–2183.
in-contextadaptabilitytopre-trainedvision-language-action,models,” [700] S. K. Soroush Nasiriany and, T. Ding, L. Smith, Y. Zhu, D. Driess,
CoRR,vol.abs/2508.02062,2025. D. Sadigh, and T. Xiao, “Rt-affordance: Affordances are versatile
[683] G.V.KonstantinosBousmalisand,D.Rao,C.M.Devin,A.X.Lee, intermediaterepresentations,forrobotmanipulation,”inICRA. IEEE,
M.B.Villalonga,T.Davchev,Y.Zhou,A.Gupta,A.Raju,A.Laurens, 2025,pp.8249–8257.
C.Fantacci,V.Dalibard,M.Zambelli,M.F.Martins,R.Pevceviciute, [701] T.D.SuneelBelkhaleand,T.Xiao,P.Sermanet,Q.Vuong,J.Tompson,
M.Blokzijl,M.Denil,N.Batchelor,T.Lampe,E.Parisotto,K.Zolna, Y. Chebotar, D. Dwibedi, and D. Sadigh, “RT-H: action hierarchies
S.E.Reed,S.G.Colmenarejo,J.Scholz,A.Abdolmaleki,O.Groth, usinglanguage,”inRobotics:ScienceandSystems,2024.
J. Regli, O. Sushkov, T. Rotho¨rl, J. E. Chen, Y. Aytar, D. Barker, [702] J. W. K. Samuel Schmidgall and, A. Kuntz, A. E. Ghazi, and
J. Ortiz, M. A. Riedmiller, J. T. Springenberg, R. Hadsell, F. Nori, A. Krieger, “General-purpose foundation models for increased auton-
andN.Heess,“Robocat:Aself-improvinggeneralistagentforrobotic omy in robot-assisted, surgery,” Nat. Mac. Intell., vol. 6, no. 11, pp.
manipulation,”Trans.Mach.Learn.Res.,vol.2024,2024. 1275–1283,2024.
[684] C.Y.ZongzhengZhangand,H.Xu,M.Liao,X.Qi,H.Gao,Z.Wang, [703] S. K. Jiayuan Gu and, P. Wohlhart, Y. Lu, M. G. Arenas, K. Rao,
and H. Zhao, “Robochemist: Long-horizon and safety-compliant W. Yu, C. Fu, K. Gopalakrishnan, Z. Xu, P. Sundaresan, P. Xu,
roboticchemicalexperimentation,”CoRR,vol.abs/2509.08820,2025. H. Su, K. Hausman, C. Finn, Q. Vuong, and T. Xiao, “Rt-trajectory:
[685] H.L.QingwenBuand,L.Chen,J.Cai,J.Zeng,H.Cui,M.Yao,and Robotictaskgeneralizationviahindsighttrajectory,sketches,”inICLR.
Y. Qiao, “Towards synergistic, generalized, and efficient dual-system OpenReview.net,2024.
forrobotic,manipulation,”CoRR,vol.abs/2410.08001,2024. [704] A.R.AbbyO’Neilland,A.Maddukuri,A.Gupta,A.Padalkar,A.Lee,
[686] M.L.XinghangLiand,H.Zhang,C.Yu,J.Xu,H.Wu,C.Cheang, A. Pooley, A. Gupta, A. Mandlekar, A. Jain, A. Tung, A. Bewley,
Y.Jing,W.Zhang,H.Liu,H.Li,andT.Kong,“Vision-languagefoun- A. Herzog, A. Irpan, A. Khazatsky, A. Rai, A. Gupta, A. E. Wang,
dationmodelsaseffectiverobotimitators,”inICLR. OpenReview.net, A. Singh, A. Garg, A. Kembhavi, A. Xie, A. Brohan, A. Raffin,
2024. A.Sharma,A.Yavary,A.Jain,A.Balakrishna,A.Wahid,B.Burgess-
[687] W. Z. Weixin Mao and, Z. Jiang, D. Fang, Z. Zhang, Z. Lan, Limerick, B. Kim, B. Scho¨lkopf, B. Wulfe, B. Ichter, C. Lu, C. Xu,
F. Jia, T. Wang, H. Fan, and O. Yoshie, “Robomatrix: A skill-centric C.Le,C.Finn,C.Wang,C.Xu,C.Chi,C.Huang,C.Chan,C.Agia,
hierarchicalframeworkforscalable,robottaskplanningandexecution C. Pan, C. Fu, C. Devin, D. Xu, D. Morton, D. Driess, D. Chen,
inopen-world,”CoRR,vol.abs/2412.00171,2024. D. Pathak, D. Shah, D. Bu¨chler, D. Jayaraman, D. Kalashnikov,
[688] H. X. Weifan Guan and, C. Zhang, A. Li, Q. Hu, and J. Cheng, D. Sadigh, E. Johns, E. P. Foster, F. Liu, F. Ceola, F. Xia, F. Zhao,
“Roboneuron: A modular framework linking foundation models and F. Stulp, G. Zhou, G. S. Sukhatme, G. Salhotra, G. Yan, G. Feng,
ROS,forembodiedAI,”CoRR,vol.abs/2512.10394,2025. G. Schiavi, G. Berseth, G. Kahn, G. Wang, H. Su, H. Fang, H. Shi,
[689] J. W. Shunlei Li and, R. Dai, W. Ma, W. Y. Ng, Y. Hu, and Z. Li, H.Bao,H.B.Amor,H.I.Christensen,H.Furuta,H.Walke,H.Fang,
“Robonurse-vla:Roboticscrubnursesystembasedonvision-language- H.Ha,I.Mordatch,I.Radosavovic,I.Leal,J.Liang,J.Abou-Chakra,
action,model,”inIROS. IEEE,2025,pp.3986–3993. J.Kim,J.Drake,J.Peters,J.Schneider,J.Hsu,J.Bohg,J.T.Bingham,
[690] J.F.SiyinWangand,F.Liu,X.He,H.Wu,J.Shi,K.Huang,Z.Fei, J. Wu, J. Gao, J. Hu, J. Wu, J. Wu, J. Sun, J. Luo, J. Gu, J. Tan,
J. Gong, Z. Wu, Y. Jiang, S. Ng, T. Chua, and X. Qiu, “Roboomni: J.Oh,J.Wu,J.Lu,J.Yang,J.Malik,J.Silve´rio,J.Hejna,J.Booher,
Proactive robot manipulation in omni-modal context,” CoRR, vol. J.Tompson,J.Yang,J.Salvador,J.J.Lim,J.Han,K.Wang,K.Rao,
abs/2510.23763,2025. K. Pertsch, K. Hausman, K. Go, K. Gopalakrishnan, K. Goldberg,
[691] C. C. Huajie Tan and, X. Chen, Y. Ji, Z. Zhao, X. Hao, Y. Lyu, K.Byrne,K.Oslund,K.Kawaharazuka,K.Black,K.Lin,K.Zhang,
M.Cao,J.Zhao,H.Lyu,E.Zhou,N.Chen,Y.Fu,C.Peng,W.Guo, K.Ehsani,K.Lekkala,K.Ellis,K.Rana,K.Srinivasan,K.Fang,K.P.
D.Liang,Z.Chen,M.Lyu,C.He,Y.Ao,Y.Lin,P.Wang,Z.Wang, Singh,K.Zeng,K.Hatch,K.Hsu,L.Itti,L.Y.Chen,L.Pinto,L.Fei-
andS.Zhang,“Roboos-next:Aunifiedmemory-basedframeworkfor Fei,L.Tan,L.J.Fan,L.Ott,L.Lee,L.Weihs,M.Chen,M.Lepert,

34
M.Memmel,M.Tomizuka,M.Itkina,M.G.Castro,M.Spero,M.Du, action model for affordable and efficient, robotics,” CoRR, vol.
M. Ahn, M. C. Yip, M. Zhang, M. Ding, M. Heo, M. K. Srirama, abs/2506.01844,2025.
M. Sharma, M. J. Kim, N. Kanazawa, N. Hansen, N. Heess, N. J. [720] W.X.JianpingJiangand,Z.Lin,H.Zhang,T.Ren,Y.Gao,Z.Lin,
Joshi, N. Su¨nderhauf, N. Liu, N. D. Palo, N. M. M. Shafiullah, Z.Cai,L.Yang,andZ.Liu,“SOLAMI:socialvision-language-action
O. Mees, O. Kroemer, O. Bastani, P. R. Sanketi, P. T. Miller, P. Yin, modeling for immersive interaction, with 3d autonomous characters,”
P. Wohlhart, P. Xu, P. D. Fagan, P. Mitrano, P. Sermanet, P. Abbeel, in CVPR. Computer Vision Foundation / IEEE, 2025, pp. 26887–
P. Sundaresan, Q. Chen, Q. Vuong, R. Rafailov, R. Tian, R. Doshi, 26898.
R.Mart´ın-Mart´ın,R.Baijal,R.Scalise,R.Hendrix,R.Lin,R.Qian, [721] W. S. Fuhao Li and, H. Zhao, J. Wang, P. Ding, D. Wang, L. Zeng,
R.Zhang,R.Mendonca,R.Shah,R.Hoque,R.Julian,S.Bustamante- and H. Li, “Spatial forcing: Implicit spatial representation alignment
Gomez, S. Kirmani, S. Levine, S. Lin, S. Moore, S. Bahl, S. Dass, forvision-language-action,model,”CoRR,vol.abs/2510.12276,2025.
S.D.Sonawani,S.Song,S.Xu,S.Haldar,S.Karamcheti,S.Adebola, [722] J. X. Hanzhen Wang and, J. Pan, Y. Zhou, and G. Dai, “Specprune-
S.Guist,S.Nasiriany,S.Schaal,S.Welker,S.Tian,S.Ramamoorthy, vla:Acceleratingvision-language-actionmodelsviaaction-aware,self-
S. Dasari, S. Belkhale, S. Park, S. Nair, S. Mirchandani, T. Osa, speculativepruning,”CoRR,vol.abs/2509.05614,2025.
T.Gupta,T.Harada,T.Matsushima,T.Xiao,T.Kollar,T.Yu,T.Ding, [723] R. Y. Songsheng Wang and, Z. Yuan, C. Yu, F. Gao, Y. Wang, and
T. Davchev, T. Z. Zhao, T. Armstrong, T. Darrell, T. Chung, V. Jain, D. F. Wong, “Spec-vla: Speculative decoding for vision-language-
V. Vanhoucke, W. Zhan, W. Zhou, W. Burgard, X. Chen, X. Wang, action models with, relaxed acceptance,” CoRR, vol. abs/2507.22424,
X. Zhu, X. Geng, X. Liu, L. Xu, X. Li, Y. Lu, Y. J. Ma, Y. Kim, 2025.
Y.Chebotar,Y.Zhou,Y.Zhu,Y.Wu,Y.Xu,Y.Wang,Y.Bisk,Y.Cho, [724] Y. L. Hengyu Fang and, Y. Du, L. Du, and H. Yang,
Y. Lee, Y. Cui, Y. Cao, Y. Wu, Y. Tang, Y. Zhu, Y. Zhang, Y. Jiang, “SQAP-VLA: A synergistic quantization-aware pruning framework
Y.Li,Y.Li,Y.Iwasawa,Y.Matsuo,Z.Ma,Z.Xu,Z.J.Cui,Z.Zhang, for, high-performance vision-language-action models,” CoRR, vol.
andZ.Lin,“Openx-embodiment:RoboticlearningdatasetsandRT-X abs/2509.09090,2025.
models:Open,x-embodimentcollaboration,”inICRA. IEEE,2024, [725] Y.Y.ZhejiaCaiand,X.Chang,S.Liang,R.Chen,F.Xiong,M.Xu,
pp.6892–6903. andR.Huang,“Seeingspaceandmotion:Enhancinglatentactionswith
[705] V.B.AnkitGoyaland,J.Xu,Y.Guo,Y.Chao,andD.Fox,“RVT-2: spatialand,dynamicawarenessforVLA,”CoRR,vol.abs/2509.26251,
learningprecisemanipulationfromfewdemonstrations,”inRobotics: 2025.
ScienceandSystems,2024. [726] G. Z. Feng Xu and, X. Kong, T. Fu, D. F. N. Gordon, X. An,
[706] S. H. Yuming Jiang and, S. Xue, Y. Zhao, J. Cen, S. Leng, K. Li, and B. Busam, “STARE-VLA: progressive stage-aware reinforce-
J.Guo,K.Wang,M.Chen,F.Wang,D.Zhao,andX.Li,“Rynnvla-001: ment for fine-tuning, vision-language-action models,” CoRR, vol.
Using human demonstrations to improve robot manipulation,” CoRR, abs/2512.05107,2025.
vol.abs/2509.15212,2025. [727] M. Y. Shengliang Deng and, Y. Zheng, J. Su, W. Zhang,
[707] S.H.JunCenand,Y.Yuan,K.Li,H.Yuan,C.Yu,Y.Jiang,J.Guo, X. Zhao, H. Cui, Z. Zhang, and H. Wang, “Stereovla: Enhanc-
X.Li,H.Luo,F.Wang,D.Zhao,andH.Chen,“Rynnvla-002:Aunified ing vision-language-action models with stereo vision,” CoRR, vol.
vision-language-actionandworldmodel,”CoRR,vol.abs/2511.17502, abs/2512.21970,2025.
2025. [728] J. Z. Wenjun Lin and, K. Cai, and K. Wang, “STORM: search-
[708] B. Zhang, Y. Zhang, J. Ji, Y. Lei, J. Dai, Y. Chen, and Y. Yang, guidedgenerativeworldmodelsforroboticmanipulation,”CoRR,vol.
“Safevla: Towards safety alignment of vision-language-action model abs/2512.18477,2025.
viaconstrainedlearning,”arXivpreprint,2025. [729] P.G.YufanHeand,M.Xu,Z.Li,A.Myronenko,D.Imans,B.Liu,
[709] K.C.IsabelLealand,D.Jain,A.Dubey,J.Varley,M.S.Ryoo,Y.Lu, D.Yang,M.Gu,Y.Ji,Y.Jin,R.Zhao,B.Shen,andD.Xu,“Surgworld:
F. Liu, V. Sindhwani, Q. Vuong, T. Sarlo´s, K. Oslund, K. Hausman, Learning surgical robot policies from videos via world, modeling,”
and K. Rao, “SARA-RT: scaling up robotics transformers with self- CoRR,vol.abs/2512.23162,2025.
adaptiverobust,attention,”inICRA. IEEE,2024,pp.6920–6927. [730] C.C.ChaojunNiand,X.Wang,Z.Zhu,W.Zheng,B.Wang,T.Chen,
[710] Y.Z.MinjieZhuand,J.Li,J.Wen,Z.Xu,N.Liu,R.Cheng,C.Shen, G. Zhao, H. Li, Z. Dong, Q. Zhang, Y. Ye, Y. Wang, G. Huang, and
Y.Peng,F.Feng,andJ.Tang,“Scalingdiffusionpolicyintransformer W.Mei,“Swiftvla:Unlockingspatiotemporaldynamicsforlightweight
to 1 billion parameters for, robotic manipulation,” in ICRA. IEEE, VLA,modelsatminimaloverhead,”CoRR,vol.abs/2512.00903,2025.
2025,pp.10838–10845. [731] X. Z. Zonghuan Xu and, X. Ma, and Y. Jiang, “Tabvla: Tar-
[711] C. Li, J. Liu, G. Wang, X. Li, S. Chen, L. Heng, C. Xiong, J. Ge, getedbackdoorattacksonvision-language-actionmodels,”CoRR,vol.
R.Zhang,K.Zhou,andS.Zhang,“Aself-correctingvision-language- abs/2510.10932,2025.
action model for fast and slow system manipulation,” arXiv preprint, [732] S. M. Jonas Geiping and, N. Jain, J. Kirchenbauer, S. Singh, B. R.
2024. Bartoldson, B. Kailkhura, A. Bhatele, and T. Goldstein, “Scaling up
[712] A.L.YilinWuand,T.Hermans,F.Ramos,A.Bajcsy,andC.Pe´rez- test-timecomputewithlatentreasoning:Arecurrent,depthapproach,”
D’Arpino, “Do what you say: Steering vision-language-action mod- CoRR,vol.abs/2502.05171,2025.
els via runtime, reasoning-action alignment verification,” CoRR, vol. [733] H.Z.ShuaijunWangand,D.Xiang,andY.You,“Tacrefinenet:Tactile-
abs/2510.16281,2025. onlygrasprefinementbetweenarbitraryin-hand,objectposes,”CoRR,
[713] J. Z. Beichen Wang and, S. Dong, I. Fang, and C. Feng, “VLM see, vol.abs/2509.25746,2025.
robotdo:Humandemovideotorobotactionplanviavision,language [734] S.W.JialeiHuangand,F.Lin,Y.Hu,C.Wen,andY.Gao,“Tactile-
model,”inIROS. IEEE,2025,pp.17215–17222. vla:Unlockingvision-language-actionmodel’sphysicalknowledge,for
[714] Z. A. Ran Yang and, L. Zhou, and Y. Feng, “Seqvla: Sequential tactilegeneralization,”CoRR,vol.abs/2507.09160,2025.
task execution for long-horizon manipulation with, completion-aware [735] H.X.ZongzhengZhangand,Z.Yang,C.Yue,Z.Lin,H.Gao,Z.Wang,
vision-language-actionmodel,”CoRR,vol.abs/2509.14138,2025. andH.Zhao,“TA-VLA:elucidatingthedesignspaceoftorque-aware
[715] L.L.KevinQinghongLinand,D.Gao,Z.Yang,S.Wu,Z.Bai,S.W. vision-language-action,models,”CoRR,vol.abs/2509.07962,2025.
Lei,L.Wang,andM.Z.Shou,“Showui:Onevision-language-action [736] C.Huang,Y.Wu,M.Chen,Y.F.Wang,andF.Yang,“Thinkact:Vision-
modelforGUIvisualagent,”inCVPR. ComputerVisionFoundation language-actionreasoningviareinforcedvisuallatentplanning,”CoRR,
/IEEE,2025,pp.19498–19508. vol.abs/2507.16815,2025.
[716] L. Wang, “Sigma: The key for vision-language-action models toward [737] Z. W. Guanxing Lu and, C. Liu, J. Lu, and Y. Tang, “Thinkbot:
telepathic,alignment,”CoRR,vol.abs/2512.00783,2025. Embodied instruction following with thought chain reasoning,” in
[717] Y. Z. Haozhan Li and, J. Yu, Y. Zhang, Z. Yang, K. Zhang, X. Zhu, ICLR. OpenReview.net,2025.
Y.Zhang,T.Chen,G.Cui,D.Wang,D.Luo,Y.Fan,Y.Sun,J.Zeng, [738] J.Z.ShaoanWangand,M.Li,J.Liu,A.Li,K.Wu,F.Zhong,J.Yu,
J.Pang,S.Zhang,Y.Wang,Y.Mu,B.Zhou,andN.Ding,“Simplevla- Z. Zhang, and H. Wang, “Trackvla: Embodied visual tracking in the
rl: Scaling VLA training via reinforcement learning,” CoRR, vol. wild,”CoRR,vol.abs/2505.23189,2025.
abs/2509.09674,2025. [739] P.D.JiachengLiuand,Q.Zhou,Y.Wu,D.Huang,Z.Peng,W.Xiao,
[718] H. S. Ayudh Saxena and, S. Routray, R. R. Shah, and E. Pahwa, W. Zhang, L. Yang, C. Lu, and D. Wang, “Trajbooster: Boosting
“SITCOM: scaling inference-time compute for vlas,” CoRR, vol. humanoid whole-body manipulation via trajectory-centric, learning,”
abs/2510.04041,2025. CoRR,vol.abs/2509.11839,2025.
[719] D. A. Mustafa Shukor and, F. Capuano, P. Kooijmans, S. Palma, [740] Y. G. Zhenyang Liu and, S. Zheng, X. Xue, and Y. Fu, “Trivla: A
A.Zouitine,M.Aractingi,C.Pascal,M.Russi,A.Marafioti,S.Alibert, triple-system-based unified vision-language-action model, for general
M. Cord, T. Wolf, and R. Cade`ne, “Smolvla: A vision-language- robotcontrol,”CoRR,vol.abs/2507.01424,2025.

35
[741] Y.Bai,Z.Wang,Y.Liu,K.Luo,Y.Wen,M.Dai,W.Chen,Z.Chen, [763] Y.X.YupingYanand,Y.Zhang,L.Lyu,H.Wang,andY.Jin,“When
L.Liu,G.Li,andL.Lin,“Learningtoseeandact:Task-awarevirtual alignment fails: Multimodal adversarial attacks on vision-language-
viewexplorationforroboticmanipulation,”arXivpreprint,2025. action,models,”CoRR,vol.abs/2511.16203,2025.
[742] W.S.JiayiChenand,P.Ding,Z.Zhou,H.Zhao,F.Tang,D.Wang, [764] Z.L.ChongkaiGaoand,Z.Chi,J.Huang,X.Fei,Y.Hou,Y.Zhang,
andH.Li,“UnifieddiffusionVLA:vision-language-actionmodelvia Y. Lin, Z. Fang, Z. Jiang, and L. Shao, “VLA-OS: structuring and
jointdiscrete,denoisingdiffusionprocess,”CoRR,vol.abs/2511.01718, dissectingplanningrepresentationsand,paradigmsinvision-language-
2025. actionmodels,”CoRR,vol.abs/2506.17561,2025.
[743] Y. Z. Zhangyuan Wang and, Y. Yan, X. Tian, X. Shao, M. Li, [765] J. L. Zhuo Li and, Z. Dong, T. Teng, Q. Rouxel, D. G. Caldwell,
W.Li,G.Su,W.Cui,andD.Fan,“Underwatervla:Dual-brainvision- andF.Chen,“TowardsdeployingVLAwithoutfine-tuning:Plug-and-
language-action architecture for, autonomous underwater navigation,” play inference-time, VLA policy steering via embodied evolutionary
CoRR,vol.abs/2509.22441,2025. diffusion,”CoRR,vol.abs/2511.14178,2025.
[744] Y.H.JiankeZhangand,Y.Guo,X.Chen,Y.Liu,W.Chen,C.Lu,and [766] Y.C.ZiyanLiuand,H.Cai,T.Lin,S.Yang,Z.Liu,andB.Zhao,“Vla-
J.Chen,“Unicod:Enhancingrobotpolicyviaunifiedcontinuousand pruner: Temporal-aware dual-level visual token pruning for efficient,
discrete,representationlearning,”CoRR,vol.abs/2510.10642,2025. vision-language-actioninference,”CoRR,vol.abs/2511.16449,2025.
[745] C.C.JiasenLuand,S.Lee,Z.Zhang,S.Khosla,R.Marten,D.Hoiem, [767] O.G.Y.CyrusNearyand,A.Kuramshin,O.Aslan,andG.Berseth,
and A. Kembhavi, “Unified-io 2: Scaling autoregressive multimodal “Improving pre-trained vision-language-action policies with model-
models with vision, language, audio, and action,” in CVPR. IEEE, based,search,”CoRR,vol.abs/2508.12211,2025.
2024,pp.26429–26445. [768] S. M. Hyunki Seong and, H. Ahn, J. Kang, and D. H.
[746] K.W.JiazhaoZhangand,S.Wang,M.Li,H.Liu,S.Wei,Z.Wang, Shim, “Vla-r: Vision-language action retrieval toward open-world
Z. Zhang, and H. Wang, “Uni-navid: A video-based vision-language- end-to-end autonomous driving,” 2025. [Online]. Available: https:
action model for unifying, embodied navigation tasks,” CoRR, vol. //dblp.org/rec/journals/corr/abs-2511-12405
abs/2412.06224,2024. [769] Z.Z.AngenYeand,B.Wang,X.Wang,D.Zhang,andZ.Zhu,“Vla-
[747] Z.L.HaoLuand,G.Jiang,Y.Luo,S.Chen,Y.Zhang,andY.Chen, r1: Enhancing reasoning in vision-language-action models,” 2025.
“Uniugp:Unifyingunderstanding,generation,andplaningforend-to- [Online].Available:https://dblp.org/rec/journals/corr/abs-2510-01623
end,autonomousdriving,”CoRR,vol.abs/2512.09864,2025.
[770] L.Z.YongshengZhaoand,B.Cheng,G.Yao,X.Wen,andH.Gao,
[748] Y.Y.HuiLuand,Y.Yang,C.Yi,Q.Zhang,B.Shen,A.C.Kot,and “VLA-RAIL: A real-time asynchronous inference linker for VLA,
X.Jiang,“Whenrobotsobeythepatch:Universaltransferablepatchat- modelsandrobots,”CoRR,vol.abs/2512.24673,2025.
tackson,vision-language-actionmodels,”CoRR,vol.abs/2511.21192,
[771] P.D.HengtaoLiand,R.Suo,Y.Wang,Z.Ge,D.Zang,K.Yu,M.Sun,
2025.
H. Zhang, D. Wang, and W. Su, “VLA-RFT: vision-language-action
[749] Y.G.JiankeZhangand,Y.Hu,X.Chen,X.Zhu,andJ.Chen,“UP-
reinforcementfine-tuningwithverified,rewardsinworldsimulators,”
VLA: A unified understanding and prediction model for embodied,
CoRR,vol.abs/2510.00406,2025.
agent,”inICML. OpenReview.net,2025.
[772] P.D.WeiZhaoand,M.Zhang,Z.Gong,S.Bai,H.Zhao,andD.Wang,
[750] Z. W. Anqi Li and, J. Zhang, M. Li, Y. Qi, Z. Chen, Z. Zhang,
“VLAS: vision-language-action model with speech instructions for,
and H. Wang, “Urbanvla: A vision-language-action model for urban
customizedrobotmanipulation,”inICLR. OpenReview.net,2025.
micromobility,”CoRR,vol.abs/2510.23576,2025.
[773] T.Z.GanlinYangand,H.Hao,W.Wang,Y.Liu,D.Wang,G.Chen,
[751] Z.W.JunwenGuand,P.Si,S.Qiu,Y.Feng,L.Sun,L.Luo,L.Yu,
Z. Cai, J. Chen, W. Su, W. Zhou, Y. Qiao, J. Dai, J. Pang, G. Luo,
J.Wang,andZ.Wu,“USIMandU0:Avision-language-actiondataset
W.Wang,Y.Mu,andZ.Hou,“Vlaser:Vision-language-actionmodel
andmodelfor,generalunderwaterrobots,”CoRR,vol.abs/2510.07869,
with synergistic embodied reasoning,” CoRR, vol. abs/2510.11027,
2025.
2025.
[752] R.Y.ChuningZhuand,S.Feng,B.Burchfiel,P.Shah,andA.Gupta,
[774] Y.S.JiamingTangand,Y.Zhao,S.Yang,Y.Lin,Z.Zhang,J.Hou,
“Unified world models: Coupling video and action diffusion for pre-
Y. Lu, Z. Liu, and S. Han, “VLASH: real-time vlas via future-state-
training,onlargeroboticdatasets,”CoRR,vol.abs/2504.02792,2025.
awareasynchronousinference,”CoRR,vol.abs/2512.01031,2025.
[753] L.A.JonasPaiand,V.Montesinos,B.Forrai,O.Mees,andE.Nava,
[775] X. W. Asher J. Hancock and, L. Zha, O. Russakovsky, and A. Ma-
“mimic-video: Video-action models for generalizable robot control
jumdar, “Actions as language: Fine-tuning vlms into vlas without
beyond,vlas,”CoRR,vol.abs/2512.15692,2025.
catastrophic,forgetting,”CoRR,vol.abs/2509.22195,2025.
[754] J.L.YueruJiaand,S.Liu,R.Zhou,W.Yu,Y.Yan,X.Chi,Y.Guo,
[776] M.W.GuangyanChenand,T.Cui,Y.Mu,H.Lu,T.Zhou,Z.Peng,
B.Shi,andS.Zhang,“Video2act:Adual-systemvideodiffusionpolicy
M. Hu, H. Li, L. Yuan, Y. Yang, and Y. Yue, “Vlmimic: Vision
with robotic spatio-motional, modeling,” CoRR, vol. abs/2512.03044,
languagemodelsarevisualimitationlearnerforfine-grained,actions,”
2025.
inNeurIPS,2024.
[755] F. W. Yichao Shen and, Z. Du, Y. Liang, Y. Lu, J. Yang, N. Zheng,
and B. Guo, “Videovla: Video generators can be generalizable robot [777] C. W. Wenlong Huang and, R. Zhang, Y. Li, J. Wu, and L. Fei-Fei,
manipulators,”CoRR,vol.abs/2512.06963,2025. “Voxposer:Composable3dvaluemapsforroboticmanipulationwith
[756] J. Y. Jeongeun Park and, B. Jeon, J. Park, J. Shin, N. Cho, K. Lee, language, models,” in CoRL, ser. Proceedings of Machine Learning
S.Yun,andS.Choi,“Hierarchicalvisionlanguageactionmodelusing Research,vol.229. PMLR,2023,pp.540–562.
successandfailure,demonstrations,”CoRR,vol.abs/2512.03913,2025. [778] M. W. Mingjie Xu and, Y. Zhao, J. C. L. Li, and W. Ou, “Llava-
[757] M.W.GuangyanChenand,Q.Shao,Z.Zhou,W.Mao,T.Cui,M.Zhu, spacesgg: Visual instruct tuning for open-vocabulary scene graph,
Y.Deng,L.Yang,Z.Zhang,Y.Yang,H.Chen,andY.Yue,“Seeonce, generation with enhanced spatial relations,” in WACV. IEEE, 2025,
then act: Vision-language-action model with task learning, from one- pp.6362–6372.
shotvideodemonstrations,”CoRR,vol.abs/2512.07582,2025. [779] J. C. Yifang Xu and, F. Cai, Z. Zhu, H. Shang, S. Luan, M. Xu,
[758] H. H. Ankit Goyal and, X. Yang, V. Blukis, and F. Ramos, “VLA- N.Zhang,Y.Li,J.Cai,andS.Zhu,“Wam-flow:Parallelcoarse-to-fine
0: building state-of-the-art vlas with zero modification,” CoRR, vol. motionplanningviadiscreteflow,matchingforautonomousdriving,”
abs/2510.13054,2025. CoRR,vol.abs/2512.06112,2025.
[759] C. M. Hanyu Zhou and and G. H. Lee, “VLA-4D: embedding 4d [780] J. C. Haoran Jiang and, Q. Bu, L. Chen, M. Shi, Y. Zhang, D. Li,
awareness into vision-language-action models, for spatiotemporally C.Suo,C.Wang,Z.Peng,andH.Li,“Wholebodyvla:Towardsunified
coherentroboticmanipulation,”CoRR,vol.abs/2511.17199,2025. latent VLA for whole-body loco-manipulation, control,” CoRR, vol.
[760] P.D.YihaoWangand,L.Li,C.Cui,Z.Ge,X.Tong,W.Song,H.Zhao, abs/2512.11047,2025.
W.Zhao,P.Hou,S.Huang,Y.Tang,W.Wang,R.Zhang,J.Liu,and [781] Z. Y. Fangqi Zhu and, Z. Hong, Q. Shou, X. Ma, and S. Guo,
D. Wang, “Vla-adapter: An effective paradigm for tiny-scale vision- “WMPO:worldmodel-basedpolicyoptimizationforvision-language-
language-action,model,”CoRR,vol.abs/2509.09372,2025. action,models,”CoRR,vol.abs/2511.09515,2025.
[761] M. Z. Yuze Wu and, X. Li, Y. Du, Y. Fan, W. Li, Z. Han, X. Zhou, [782] X.C.ZezhongQianand,Y.Li,S.Wang,Z.Qin,X.Ju,S.Han,and
andF.Gao,“VLA-AN:anefficientandonboardvision-language-action S. Zhang, “Wristworld: Generating wrist-views via 4d world models
framework,foraerialnavigationincomplexenvironments,”CoRR,vol. forrobotic,manipulation,”CoRR,vol.abs/2510.07313,2025.
abs/2512.15258,2025. [783] H.C.PeiYangand,Y.Song,andM.Z.Shou,“X-humanoid:Robotize
[762] Y. W. Siyu Xu and, C. Xia, D. Zhu, T. Huang, and C. Xu, “Vla- human videos to generate humanoid videos at scale,” CoRR, vol.
cache: Towards efficient vision-language-action model via adaptive, abs/2512.04537,2025.
token caching in robotic manipulation,” CoRR, vol. abs/2502.02175, [784] K. W. Shichao Fan and, Z. Che, X. Wang, D. Wu, F. Liao, N. Liu,
2025. Y. Zhang, Z. Zhao, Z. Xu, M. Li, Q. Liu, S. Zhang, M. Wan,

36
and J. Tang, “XR-1: towards versatile vision-language-action mod-
els via learning, unified vision-motion representations,” CoRR, vol.
abs/2511.02776,2025.
[785] J. L. Jinliang Zheng and, Z. Wang, D. Liu, X. Kang, Y. Feng,
Y. Zheng, J. Zou, Y. Chen, J. Zeng, Y. Zhang, J. Pang, J. Liu,
T. Wang, and X. Zhan, “X-VLA: soft-prompted transformer as scal-
able cross-embodiment vision-language-action, model,” CoRR, vol.
abs/2510.10274,2025.

37
APPENDIX 1) ComputerVision: Computervisionwitnessedtheincep-
A. Background tion of modern neural networks. In robotics, object classifica-
tionmodelscanbeusedtoinformapolicyaboutwhichobjects
1) Unimodal Models: Vision-language-action models in-
are of interest, and models for object detection or image
tegrate three modalities, often relying on existing unimodal
segmentation can help precisely locate objects. Therefore, we
models. The transition from convolutional neural networks
mainly summarize approaches for these tasks, but numerous
(e.g., ResNet [218]) to visual Transformers (e.g., ViT [219],
excellentsurveysonvisualmodels,rangingfromconvolutional
SAM[220])incomputervisionhasfacilitatedthedevelopment
neural networks (CNNs) [235] to Transformers [236], offer
of vision foundation models (VFMs). In natural language
more detailed insights. Interested readers are directed to these
processing,theevolutionfromrecurrentneuralnetworks(e.g.,
surveys for a more comprehensive introduction. Here, we will
LSTM [221], GRU [222]) to Transformers [3] initially led
briefly touch upon some of the key developments in the field
to the pretrain-finetune paradigm (e.g., BERT [26], ChatGPT
of computer vision.
[223]), followed by the recent success of prompt tuning
a) Convolutionalneuralnetwork: Earlydevelopmentsin
drivenbylargelanguagemodels.Reinforcementlearning(e.g.,
computer vision (CV) were primarily focused on the image
DQN [4], AlphaGo [224], PPO [225], Dactyl [226]) has also
classification task. LeNet [237] was among the first convolu-
witnessed a shift towards employing Transformers to model
tional neural networks, designed for identifying handwritten
the Markov Decision Process as autoregressive sequential
digits in zip codes. In 2012, AlexNet [2] emerged as a
data. DPO [227] directly trains LLMs on human preferences,
breakthroughbywinningtheImageNetchallenge,showcasing
simplifying RLHF.
the potential of neural networks. VGG [238] demonstrated
2) Vision-Language Models: Vision-language tasks, en-
the benefits of increasing the depth of CNNs. GoogLeNet
compassingimagecaptioning[228],visualquestionanswering
[239], also known as Inception-V1, introduced the concept of
[229], visual grounding [230], require the fusion of com-
blocks. ResNet [218] introduced skip connections or residual
puter vision and natural language processing models. Early
connections. Inception-ResNet [240], as the name suggests,
efforts, such as Show and Tell [231], leveraged the success
combines residual connects and inception blocks. ResNeXt
of early CNNs and RNNs. The advent of high-capacity lan-
[241] explored the concept of split, transform, and merge.
guage models, including BERT [26] and GPT [232], ush-
SENet [242] introduces the squeeze-and-excitation blocks,
ered in a new era of Transformer-based VLMs. One of the
utilizing a type of attention mechanism. EfficientNet [243]
pioneering self-supervised pretraining methods is ViLBERT
studied the width, depth, and resolution of CNN models
[233], while CLIP [22] popularized contrastive pretraining
with “compound scaling,” highlighting the trade-off between
approaches for multimodal alignment. The recent emergence
efficiency and performance.
oflargelanguagemodelshasdriventhedevelopmentofmulti-
Alongside image classification, object detection became an
modal LLMs (MLLMs) or large multimodal models (LMMs),
integral component in many applications. Building upon the
which achieve state-of-the-art performance on multimodal
successof image classificationbackbonenetworks, aseriesof
instruction-following tasks. Representative MLLMs include
works optimized region-based methods: R-CNN [244], Fast
Flamingo [234], BLIP-2 [6], and LLaVA [7]. VLMs share a
R-CNN [245], Faster R-CNN [246], and Mask R-CNN [247].
close relationship with VLAs, as the multimodal architectures
Grid-basedmethodslikeYOLO[248]arealsowidelyadopted.
of VLMs can be readily adopted for VLAs. Additionally,
Bottom-up, top-down is also a popular strategy, employed by
VLMscanfunctionashigh-leveltaskplannersiftheypossess
FPN [249], RetinaNet [250], BUTD [251], etc. In scenarios
sufficient reasoning capabilities.
requiring more detailed and precise object detection, image
segmentation aims to determine the exact outline of objects.
B. Background (Extended Version): Unimodal Models
Many popular models adopt an “encoder-decoder” architec-
Vision-language-actionmodelsinvolvethreemodalities,and ture, where the encoder understands both the global and local
consequently, many VLAs depend on existing unimodal mod- contextoftheimage,andthedecoderproducesasegmentation
els for processing inputs from different modalities. Therefore, map based on this context information. Representative works
it is crucial to summarize representative developments in following this idea include FCN [252], SegNet [253], Mask
unimodal models, as they often serve as integral components R-CNN [247], and U-Net [254].
in VLAs. Specifically, for the vision modality, we collect b) Vision Transformer: Convolutional neural networks
modelsdesignedforimageclassification,objectdetection,and (CNNs) have historically been the foundation of computer
image segmentation, as these tasks are particularly relevant vision models. However, the landscape shifted with the intro-
for robotic learning. Natural language processing models play duction of the Transformer architecture in the seminal work
a crucial role in enabling VLAs to understand language by [3]. This paradigm shift was initiated by ViT [219]. It
instructions or generate language responses. Reinforcement revolutionizesimageprocessingbybreakingdownimagesinto
learning is a foundational component for obtaining optimal 16-by-16 pixel patches, treating each as a token akin to those
policies, facilitating the generation of appropriate actions in in NLP; leveraging a BERT-like model, ViT encodes these
a given environment and condition. A brief timeline of the patches and has exhibited superior performance over many
development of unimodal models is depicted in Figure 7. traditional CNN models in image classification tasks.
Additionally, Figure 8 highlights the progressive increase in The transformative power of the Transformer extends be-
model size within these fields. yond classification. DETR [255] employs an encoder-decoder

38
Computer Vision Natural Language Processing Reinforcement Learning
Classification Detection, CNN RNN Value, etc. Policy Robotics
Segmentation
... LeNet LSTM BiRNN TD-Learning Policy
Gradient
2012 AlexNet
22001133 word2vec GPS
VGG R-CNN GloVe GRU
2014 WordCNN DPG
GoogLeNet FCN Enc-Dec RNN
2013 Fast R-CNNU-Net RNNsearch DQN
2015 ResNet CharCNN TRPO
Faster R-CNN LSTM-CRF AlphaGo
Inception- BiLSTM-CNNs-CRF D-DQN DDPG GAE E2E-DVP
2016 YOLO
ResNet GAIL A3C NAF Hand-eye
Transformer
2013 RetinaNet FPN HER RLHF
2017 ResNeXt Transformer PPO
Mask R-CNN RARL FuN
ELMo Soft AC QT-Opt
2018 SENet BUTD GPT
ULMFiT Dactyl
2013 GPT-2 BCQ
2019 EfficientNet ADR
BERT BEAR
2020 ViT DETR GPT-3 T5 CQL Dreamer
22002131 DINO Segmenter InstructGPT DT TT
2022 ChatGPT Gato
2023 EVA SAM LLaMA GPT-4
Figure 7: A brief timeline of pivotal unimodal models leading to the development of vision-language-action models, organized
by their publication years. Details can be found in Appendix:B.
Transformer architecture to tackle object detection. The en- maps and is suitable for representing rigid objects. Despite
coder processes the input image, and its output embeddings the widespread use of 3D meshes as the default data format
are fed into the decoder through cross-attention. Notably, in computer graphics, their irregular nature poses challenges
DETR introduces learnable object queries to the decoder, for neural networks [261].
facilitating the extraction of crucial object-wise information 2) Natural Language Processing: Natural Language Pro-
fromtheencoder’soutput.Venturingintoimagesegmentation, cessing (NLP) plays a pivotal role in VLA, serving as a
Segmenter [256] was the first to utilize Transformer on this vital component for understanding user instructions or even
task. The Segment Anything model (SAM) [220] achieves generating appropriate textual responses. The recent surge in
remarkable milestones in promptable segmentation, zero-shot NLP owes much to the success of Transformer models [3]. In
performance,andversatilearchitecture,furtherunderliningthe thelandscapeofcontemporaryNLP,thereisanoticeableshift
transformativeimpactofVisionTransformermodelsinvarious towards implicit learning of language syntax and semantics,
computer vision domains. a departure from the previous paradigms. To provide context,
c) Vision in 3D: Aside from the most common RGB this subsection will commence with a concise overview of
data,othertypesofvisualinputsarewidelyused[257],[258]. fundamental yet enduring concepts before delving into the
Inrobotics,depthmapsareusefulsincetheyprovideessential noteworthy advancements in contemporary NLP. For an in-
3D information that is not explicitly stored in RGB images. depth exploration of the progress in the NLP domain, readers
Depth maps can be captured with Microsoft Kinect 1 or Intel are directed to comprehensive surveys by [262] and [263],
RealSense2 orrecoveredfrompureRGBimages.Pointclouds which meticulously review the trajectory of advancements in
[259]arealsopopularvisualinputtypesduetothewidespread NLP.
adoption of LiDARs and 3D scanners; depth maps can be
a) Early developments: The field of NLP, which was
easilyconvertedtopointclouds.Volumetricdata[260],suchas
morefrequentlyreferredtoasComputationalLinguistics(CL)
voxels or octrees, is usually more information-rich than depth
intheearlydays,triestosolvevarioustasksregardingtonatu-
1https://azure.microsoft.com/en-us/products/kinect-dk/ rallanguage.InCL,naturallanguagesusedtobeprocessedin
2https://www.intelrealsense.com ahierarchicalway:word,syntax,andsemantics.Firstly,onthe

39
107
106
105
104
103
102
101
100
10 1
10 2
10 3
2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023
Release Year
)snoilliM
ni
,elacs
gol(
sretemaraP
*GPT-4
PaLM
GPT-3 175B
LLaMA-65B
LLaMA-33B
T5-11B LLaMA-13B
LLaMA-7B
T5-3B
GPT-2 ChatGPT
T5-Large Gato
BERT-Large ViT-Huge
Transformer SENet ViT-Large
VGG BERT-BaseGPT T5-Base ViT-Base
AlexNet Inception-ResNet ResNet-152 ELMo-Original T5-Small
Inception-V In 4 ception-ResNet-v2 EfficientNet-B7
Inception-V3 ResNet-50 ELMo-Medium
GoogLeNet ELMo-Small
BiLSTM-CNN-CRF
QT-Opt TT
DT
DDPG
DQN PPO Computer Vision
Natural Language Processing
Reinforcement Learning
Figure 8: The growing scale of unimodal models over the years. ∗GPT-4’s model size is estimated since it has not been
officially disclosed.
word level, many aspects need to be accounted for, including withword2vecfeaturesservingasinputtotheCNNs.Another
morphology, lexicology, phonology, etc. This leads to prob- approach, CharCNN [274], focused on modeling language
lems like tokenization, lemmatization, stemming, semantic at the character level with CNN. Subsequent research [275]
relations,wordsensedisambiguation,andZipf’sLawproblem. highlighted that character-level CNNs excel at capturing word
Then, in terms of syntax, natural language, in contrast to morphology, and their combination with a word-level LSTM
formallanguage,hasmuchlessrestrictedgrammarandthusis backbone can significantly enhance performance.
more challenging to parse: in the Chomsky hierarchy, natural
c) Transformer & large language model: The ground-
language is generally considered to follow context-sensitive
breaking Transformer model, introduced by [3], revolution-
grammar, while programming languages are covered under
ized natural language processing through the introduction of
context-free grammar. Syntactic parsing includes tasks such
the self-attention mechanism, inspiring a cascade of subse-
as part-of-speech tagging, constituency parsing, dependency
quent works. BERT [26] leverages the Transformer encoder
parsing, and named entity recognition. Finally, to understand
stack, excelling in natural language understanding. On the
thesemanticsofasentenceinwrittenlanguageoranutterance
other hand, the GPT family [232], [276]–[278] is built upon
inspokenlanguage,thefollowingtaskswerestudied:semantic
Transformer decoder blocks, showcasing prowess in natural
role labeling, frame semantic parsing, abstract meaning repre-
language generation tasks. A line of work strives to refine the
sentation, logical form parsing, etc.
original BERT, including RoBERTa [279], ALBERT [280],
b) Recurrentneuralnetwork&convolutionalneuralnet- ELECTRA [281]. Simultaneously, a parallel line of research
work: In the initial stages of NLP, rudimentary models relied following the GPT paradigm has given rise to models like
on simple feed-forward neural networks to tackle various XLNet [282], OPT [283]. BART [284], an encoder-decoder
tasks [264]. After the introduction of word embeddings like Transformer, distinguishes itself through pretraining using the
word2vec [265], [266] and GloVe [267], NLP techniques em- denoising sequence-to-sequence task. Meanwhile, T5 [285]
bracedrecurrentneuralnetworks(RNNs)[268],suchasLSTM introducesmodificationstotheoriginalTransformer,maintain-
[221], GRU [222], RNNsearch [269], LSTM-CRF [270], etc. ing the encoder-decoder architecture. T5 unifies various NLP
ExamplesofrepresentativeRNNsinNLPincludeELMo[271] tasksthroughasharedtext-to-textformat,exhibitingenhanced
and ULMFiT [272]. While RNNs played a significant role, performanceintransferlearning.Thesediversemodelscollec-
alternativemodelsutilizingconvolutionalneuralnetworksalso tively showcase the versatility and ongoing evolution within
emerged. WordCNN [273] employed CNNs at the word level, the NLP landscape.

40
Over the past few years, there has been a remarkable actor-critic techniques. These approaches aim to combat per-
expansion in the size of language models, driven by the sistentchallenges,includinginstability,slowconvergence,and
scalability of the Transformer architecture. This trend has data inefficiency. Guided policy search (GPS) [304] learns a
given rise to a series of large language models (LLMs) that policy with importance sampling guided by another controller
have demonstrated breakthrough performance and capabilities toward a local optimum. Deterministic policy gradient (DPG)
not achievable with smaller models. A landmark model in [305], deep deterministic policy gradient (DDPG) [306], and
this evolution is ChatGPT [223], which has sparked consid- asynchronousadvantageactor-critic(A3C)[307]improveeffi-
erable interest and inspired a series of works in this domain, ciency without compromising stability. Normalized advantage
such as GPT-4 [278], PaLM [286], PaLM-2 [287], LLaMA functions (NAF) [308] are a continuous variant of Q-learning,
[288], LLaMA 2 [289], ERNIE 3.5 [290]. Notably, LLaMA allowing for Q-learning with experience replay. Soft actor-
stands out as one of the few open-source LLMs, fostering critic (Soft AC) [309] takes advantage of the maximum
interesting developments. The introduction of “instruction- entropy RL framework to lower sample complexity and im-
tuning” has allowed efficient fine-tuning of a pretrained LLM proveconvergenceproperties.Trustregionpolicyoptimization
to become an instruction-following model. This technique is (TRPO) [310] and proximal policy optimization (PPO) [225]
popularized by InstructGPT [291] and FLAN [292], [293]. utilize trust region methods to stabilize policy gradients,
Recent advancements in instruction-following models include with PPO additionally incorporating a truncated generalized
Alpaca [294], employing self-instruction, and Vicuna [295], advantage estimation (GAE) [311].
leveraging conversations from ShareGPT. As LLMs grow in Beyond these, various other RL methodologies exist, such
scale and power, there is a shift away from the need for fine- as imitation learning and hierarchical reinforcement learning.
tuningondownstreamtasks.Withappropriateprompts,LLMs Generative adversarial imitation learning (GAIL) [312] is an
can produce accurate outputs without task-specific training, imitation learning method that uses a generative adversarial
a paradigm known as prompt engineering. This approach framework to discriminate expert trajectories against gener-
differs from the traditional pretrain-finetune paradigm. DPO ated trajectories. Robust adversarial reinforcement learning
[227] introduces a method to train LLMs directly on hu- (RARL)[313]incorporatesadversarialagentstoenhancegen-
man preferences without requiring explicit reward modeling eralization. RLHF [314] utilizes human preferences without
or reinforcement learning, simplifying upon previous RLHF access to the reward function. FeUdal Networks (FuN) [315]
methods. introduce a hierarchical reinforcement learning architecture
3) Reinforcement Learning: Reinforcement learning (RL) featuring a Manager module and a Worker module.
seeks to acquire a policy capable of taking optimal actions b) Robotics: InthefieldofRL,roboticsstandsoutasone
based on observations of the environment. Numerous vision- ofthemostprevalentandimpactfulapplications.Anoteworthy
language-action models are constructed based on paradigms contribution to this field is E2E-DVP [316]. This pioneering
such asimitation learning orTemporal Difference (TD)learn- model represents one of the first end-to-end solutions for
ing within RL. Many challenges faced in the development of robotic control. Its neural network is designed to take raw
robotic policies can be effectively addressed through insights images as input and generate motor torques as output. [5]
gained from the field of RL. Consequently, delving into RL curated a substantial real-world dataset and developed a CNN
methods presents a valuable avenue for enhancing robotic that predicts grasps based on monocular input images. Build-
learning.ForadeeperexplorationofRLmethods,readerscan ing upon these foundations, QT-Opt [317] further expands
refertomorecomprehensivereviewsprovidedby[296],[297], the dataset and model scale, introducing closed-loop control
and [298]. capabilitiestoenhanceroboticcontrolsystems.ThenDreamer
a) Deep reinforcement learning: The advent of deep [51] addresses long-horizon tasks. OpenAI also developed a
reinforcement learning can be attributed to the success of dexterous robot hand that can solve the Rubik’s cube [226],
pioneering models, Deep Q-Network [4] and AlphaGo [224]. [318].
Deep learning, with its ability to provide low-dimensional 4) Graph: Graph is ubiquitous in many scenarios, such
representations, proved instrumental in overcoming traditional as social networks, molecule structures, 3D object meshes,
computational and memory complexity challenges in rein- etc. Even images and text can be modeled as a 2D grid and
forcement learning. In recent years, a multitude of value- a linear graph (path graph), respectively. To process graph-
function-based approaches have surfaced. Double DQN (D- structured data, recurrent graph neural networks [319] were
DQN) [299] addresses the action value overestimation issue first introduced, which were later optimized by convolutional
ofDQN.Hindsightexperiencereplay(HER)[300]focuseson graph neural networks. The review of graph neural networks
the sparse reward issue. Batch-Constrained deep Q-learning (GNN) [320] can be referred to for more in-depth details.
(BCQ) [301] presents an approach aimed at enhancing off- Convolutional graph neural networks can be generally di-
policy learning by constraining the action space. BEAR [302] vided into two categories: spectral-based and spatial-based.
endeavors to alleviate instability arising from bootstrapping Spectral-based convolutional GNNs draw inspiration from
errors in off-policy RL. [303] introduces conservative Q- graphsignalprocessing,whichprovidestheoreticalsupportfor
learning (CQL) to address the overestimation of values by the design of the networks. However, spatial-based convolu-
standard off-policy RL methods. tionalGNNshaveanadvantageintermsoftheirefficiencyand
Another paradigm within reinforcement learning is policy flexibility.SpectralCNN[321]isoneofthefirstconvolutional
search, encompassing methods such as policy gradient and GNNs, but it is not robust to changes in graph structure and

41
hasahighcomputationalcost.ChebNet[322]andGCN[323] given rise to robust multi-modal Transformer models. Initial
significantlyreducedthecost:ChebNetusedanapproximation VLMs based on BERT can be broadly categorized into two
based on Chebyshev polynomials, and GCN is its first-order types: single-stream and multi-stream [386]. Single-stream
approximation. Neural Network for Graphs (NN4G) [324] is models employ a single stack of Transformer blocks to pro-
the first spatial network. MPNN [325] introduced a general cess both visual and linguistic inputs, whereas multi-stream
framework of spatial-based networks under which most exist- modelsutilizeaseparateTransformerstackforeachmodality,
ingGNNscanbecovered.ButthedrawbackofMPNNisthat with Transformer cross-attention layers exchanging multi-
it does not embed graph structure information, which is later modal information. To enhance alignment among modalities,
solved by GIN [326]. GraphSage [327] improves efficiency these models incorporate various pretraining tasks aimed at
by sampling a fixed number of neighbors. Graph Attention absorbing knowledge from out-of-domain data. ViLBERT
Network (GAT) [328] incorporates the attention mechanism. [233] stands as the pioneer in this line of work, featuring a
Besides recurrent and convolutional graph neural networks, multi-stream Transformer architecture. Text input undergoes
therearegraphautoencoders[329],[330]andspatial-temporal standard processing in the language Transformer; image in-
graph neural networks [331]. Equivariant message passing put is first processed using Faster R-CNN, and the output
networksare recently introducedtohandle 3Dgraphs,includ- embeddings of all objects are then passed into the vision
ing E(n)- and SE(3)- Equivariant GNN [332], [333]. Graph stream. The two Transformer outputs—language embeddings
Transformer models make use of the power of transformers and vision embeddings—are combined using a novel co-
to process graph data. There are already over 20 such graph attention transformer layer. VL-BERT [344] adopts a single-
Transformer models, such as GROVER [334] and SE(3)- stream multi-modal Transformer, simply concatenating vision
Transformers [335]. andlanguagetokensintoasingleinputsequence.VideoBERT
a) Graphandvision: Graphstructuresalsoexistinsome [390] adapts mulitmodal Transformer models to video inputs.
computer vision tasks. Scene graph [336] can be used to UNITER [345] proposes the word-region alignment loss to
express object relationships in most visual inputs. In addition explicitlyalignwordwithimageregions.ViLT[346]usesViT-
to detecting objects in an image, scene graph generation style[219]imagepatchprojectiontoembedimages,deviating
necessitates the understanding of the relationships between from previous region or grid features.
detected objects. For example, a model needs to detect a SimVLM [347] opts for a streamlined approach, relying
person and a cup, and then understand that the person is solelyonasingleprefixlanguagemodelingobjectivetoreduce
holding the cup, which is the relationship between the two training costs. VLMo [391] and BEiT-3 [351] both introduce
objects. Knowledge graphs often contain visual illustrations, mixture-of-modality-experts Transformers to effectively han-
suchasWikiData.Thosegraphscanbehelpfulindownstream dle multi-modal inputs.
computer vision tasks. 2) Contrastive pretraining: Vision-language pretraining in
b) Graphandlanguage: Graphstructuresareubiquitous the initial series of BERT-based VLMs has evolved, with
inlanguagedata[337].Word-levelgraphsincludedependency refinements such as curating larger-scale pretraining datasets,
graphs, constituency graphs, AMR graphs, etc. Word-level leveraging multi-modal contrastive learning, and exploring
means each node of those graphs corresponds to a word in specialized multi-modal architectures. CLIP [22] is one of
the original text. These graphs can be used to explicitly rep- theearliestattemptsinvision-languagecontrastivepretraining.
resent the syntax or semantics of the raw sentence. Sentence- By contrastive pretraining on a large-scale image-text pair
level graphs can be useful in dialog tracking [338], fact dataset, CLIP exhibits the capability to be transferred to
checking[339],etc.Document-levelgraphsincludeknowledge downstream tasks in a zero-shot fashion. In the same line
graphs [340], citation graphs [341], etc. They can be used in of work, other few-/zero-shot learners have emerged. FILIP
document-level tasks, such as document retrieval, document [352] concentrates on finer-grained multi-modal interactions
clustering, etc. Different types of language graphs are often withatoken-wisecontrastiveobjective.ALIGN[353]focuses
processed using the aforementioned GNNs to facilitate down- onlearningfromnoisydatasetscollectedwithoutfilteringand
stream tasks. post-processing. “Locked-image Tuning” (LiT) [392] posits
that only training the text model while freezing the image
model yields the best results on new tasks. In Frozen [393],
C. Background (Extended Version): Vision-Language Models
the pretrained language model is frozen and a vision encoder
Comprehensive surveys on VLMs exist, covering early is trained to produce image embeddings as a part of language
BERT-based VLMs [386], [387] (Section C1), as well as model prompts, exemplifying an instance of prompt tuning.
more recent VLMs with contrastive pretraining [388], [389] Unlike the two-tower frameworks of CLIP, FILIP, and
(Section C2). Given the rapid evolution of this field and the ALIGN,whichsolelytrainunimodalencoders(imageencoder
emergence of new VLMs based on large language models, and text encoder), ALBEF [355] additionally incorporates
commonly known as large multi-modal models (LMMs), we training a multimodal encoder on top of the unimodal en-
also compile the latest developments of LMMs (Section C3). coders, with FLAVA [356] sharing a similar idea. In con-
To compare the most representative VLMs, we include their trast to contrastive pretraining methods, CoCa [394] seeks to
specifications in Table VIII. amalgamate the strengths of CLIP’s contrastive learning and
1) Self-supervised pretraining: The evolution of the Trans- SimVLM’s generative objective. Florence [350] generalizes
former architecture to accommodate various modalities has representations from coarse, scene-level to fine, object-level,

42
Table VIII: Vision-language models. In the “Objective” column: “MLM”: masked language modeling. “MVM”: masked vision
modeling, reconstructing masked image regions. “VLM”: binary classification of whether vision and language inputs are a
match.“LM”:autoregressivelanguagemodeling.“VLCL”:vision-languagecontrastivelearning.Weonlyincluderepresentative
multi-modal datasets due to limited space. “MM” includes multi-modal tasks such as visual question answering, image
captioning, and vision-language retrieval. “Vision” represents computer vision tasks, like image classification. “Language”
represents natural language processing tasks.
VisionEncoder LanguageEncoder
Model Name Params Name Params VL-Fusion Objectives Datasets Tasks
desivrepus-fleS
ViLBERT[233] FasterR-CNN[246], 44M Dual-stream 221M Dual-stream MLM,MVM, COCO,VG MM
[251] BERT-base[26] VLM
LXMERT[342] FasterR-CNN[246], 44M Dual-stream 183M Dual-stream MLM,MVM, COCO,VG,VQA,GQA,VGQA MM
[251] BERT-base[26] VLM,VQA
VisualBERT[343] FasterR-CNN[246], 60M BERT-base[26] 110M Single-stream MLM,VLM COCO MM
[251]
VL-BERT[344] FasterR-CNN[246], 44M BERT-base[26] 110M Single-stream MLM,MVM CC MM
[251]
UNITER[345] FasterR-CNN[246], 44M BERT-base/ 86M/ Single-stream MLM,VLM, COCO,VG,SBU,CC MM
[251] BERT-large[26] 303M MVM,WRA
ViLT[346] Linearprojection[219] 2.4M BERT-base[26] 85M Single-stream MLM,VLM COCO,VG,SBU,CC MM
SimVLM[347] ViT/CoAtNet-huge 632M Sharedencoder 632M Single-stream PrefixLM ALIGNdataset MM
(sharedencoder)[348]
GIT[349] Florence[350] 637M Transformer[3] 60M Single-stream LM COCO,VG,SBU,CC,etc. MM
BEiT-3[351] V-FFN 692M L-FFN 692M Modalityexperts MLM,VLM COCO,VG,SBU,CC MM,Vision
(+SharedAttn) (+317M) (+SharedAttn) (+317M)
evitsartnoC
CLIP[22] ViT[219] 428M GPT-2[276] 63M Two-tower VLCL WTI Vision
FILIP[352] ViT-L/14[219] 428M GPT[276] 117M Two-tower VLCL FILIP300M(Self-collect) MM,Vision
ALIGN[353] EfficientNet-L2[354] 480M BERT-large[26] 336M Two-tower VLCL ALIGNdataset(Self-collect) MM,Vision
ALBEF[355] ViT-B/16[219] 87M BERT-base[26] 85M Dual-stream MLM,VLM, COCO,VG,CC,SBU MM
VLCL
FLAVA[356] ViT-B/16[219] 87M RoBERTa-base 125M Dual-stream MLM,MVM, COCO,VG,CC,SBU,etc. MM,Vision,
[279] VLM,VLCL (PMD) Language
Florence[350] HierarchicalVision 637M RoBERTa[279] 125M Two-tower VLCL FLD-900M(Self-collect) Vision
Transformers[357],[358]
ledoMladom-itluMegraL
Flamingo[234] NFNet-F6[359] 438M Chinchilla[360] 70B Dual-stream LM M3W,ALIGNdataset,LTIP,VTP MM
BLIP-2[6] CLIPViT-L/14[22], 428M, OPT[283] 6.7B Single-stream BLIP,LM COCO,VG,CC,SBU,LAION MM
EVAViT-G/14[361] 1B Flan-T5[293] 3B/11B
+Q-Former
PaLI[362] ViT-e[362] 4B mT5-XXL[363] 13B Single-stream Mixed WebLI,etc MM
PaLI-X[364] ViT-22B[365] 22B UL2[366] 32B Single-stream Mixed WebLI,etc MM
LLaMA-Adapter CLIPViT-B/16[22] 87M LLaMA[288] 7B Single-stream LM Self-instruct Instruction-
[367] following
LLaMA-Adapter-V2 CLIPViT-L/14[22] 428M LLaMA[288] 7B Single-stream LM GPT-4-LLM,COCO,ShareGPT Instruction-
[368] following
Kosmos-1[369], CLIPViT-L/14[22] 428M Magneto[371] 1.3B Single-stream LM LAION,COYO,CC;Unnatural Instruction-
Kosmos-2[370] Instructions,FLANv2 following
(Kosmos-2
w/grounding,
referring)
InstructBLIP[372] EVAViT-G/14[361] 1B Flan-T5[293] 3B/11B Single-stream BLIP,LM COCO,VQA,LLaVA-Instruct- Instruction-
Vicuna[295] 7B/13B 150K,etc.(26datasets) following
LLaVA[7] CLIPViT-L/14[22] 428M LLaMA[288] 13B Single-stream LM CC,(FT:GPT-assistedVisual Instruction-
InstructionDataGeneration) following
MiniGPT-4[373] EVAViT-G/14[361] 1B Vicuna[295] 7B/13B Single-stream LM CC,SBU,LAION(FT:SC) Instruction-
+Q-Former[6] LLaMA2[289] 7B following
Video-LLaMA[374] EVAViT-G/14[361] 1B LLaMA[288] 7B/13B Single-stream BLIP,LM CC595k Instruction-
+Q-Former[6] following
PandaGPT[375] ImageBindViT-H[209] 632M Vicuna[295] 13B Single-stream LM (FT:LLaVAdata,MiniGPT-4 Instruction-
data) following
VideoChat[376] EVAViT-G/14[361] 1B StableVicuna 13B Single-stream LM COCO,VG,CC,SBU(FT:SC, Instruction-
+Q-Former[6] [377] MiniGPT-4,LLaVAdata) following
ChatSpot[378] CLIPViT-L/14[22] 428M Vicuna[295] 7B Single-stream LM MGVLID,RegionChat Instruction-
following,Vision
mPLUG-Owl[379], CLIPViT-L/14[22] 428M LLaMA[288] 7B Single-stream LM LAION,COYO,CC,COCO(FT: Instruction-
mPLUG-Owl2[380] +VisualAbstractor Alpaca,Vicuna,Baize[381]data) following
VisualChatGPT (22differentmodels) - ChatGPT[223] - PromptManager - AddimageunderstandingandgenerationtoChatGPT
[382]
X-LLM[383] ViT-G[384]+Q-Former 1.8B ChatGLM[385] 6B Single-stream Three-stage MiniGPT-4data,AISHELL-2, Instruction-
[6]+Adapter training ActivityNet,VSDial-CN(SC) following

43
expands from images to videos, and encompasses modalities Q-Former [6]. PandaGPT [375] leverages ImageBind [209]
beyond RGB channels. OFA [395] draws inspiration from T5 to encode vision/text/audio/depth/thermal/IMU data, feeding
[285]andproposesunifyingdiverseunimodalandmulti-modal them to the Vicuna model [295] also through a linear layer.
tasks under a sequence-to-sequence learning framework. PandaGPT diverges from MiniGPT-4 by using LoRA [396] to
3) Large multi-modal model: Large language models train Vicuna alongside the linear layer.
(LLMs) encapsulate extensive knowledge, and efforts have
been made to transfer this knowledge to multimodal tasks.
D. Supplementary Related Work
Giventheresource-intensivenatureoffine-tuningentireLLMs
Due to page limitations, we were unable to provide
onmulti-modaltasksduetotheirlargesize,varioustechniques
citations for all the mentioned models in the main text. Here
have been explored to effectively connect frozen LLMs with
is a list of supplementary related works:
vision encoders, enabling the combined model to acquire
multi-modalcapabilities.Flamingo[234]connectsapretrained
Computer Vision:
vision encoder, NFNet [359], and a large language model,
Chinchilla [360], by inserting trainable gated cross-attention • Mask R-CNN [247]
layers while keeping the rest of the model frozen. BLIP-2 • YOLOv8 [248]
[6] introduces Q-Former, bootstrapping vision-language rep- • EfficientNet [243]
resentation learning first from a frozen CLIP ViT [22] and • UNet [254]
then from a frozen LLM, OPT [283] or Flan-T5 [293]. PaLI • VQ-GAN [397]
[362] and PaLI-X [364] investigate the advantages of jointly • MoVQ [398]
scaling up the vision and language components using large- • SigLIP [399]
scale multilingual image-text data. • ViLD [400]
Similar to developments in NLP, instruction-following has • MDETR [401]
become a crucial aspect of VLMs, prompting the exploration • HLSM object detector [402]
of various multimodal instruction-tuning methods. LLaMA- • ResNet [218]
Adapter [367], [368] employs a parameter-efficient finetun- • ViT, ViT-B, ViT-L [25], [219]
ing (PEFT) technique, enabling LLaMA [288] to process • MAE [403]
visual inputs. Kosmos-1 [369] introduces a less restrictive • ViT-22B [365]
input format that accommodates interleaved image and text. • EVA ViT-G/14 [361]
Its Magneto LLM [371] serves as a “general-purpose inter- • OWL-ViT [404]
face” for docking with perception modules [22]. Kosmos-2 • ConvNeXt [405]
[370] adds additional grounding and referring capabilities. • SAM [220]
InstructBLIP [372] achieves instruction-following using an • Imagen video [406]
instruction-aware Q-Former based on BLIP-2’s Q-Former [6]. • C-ViViT [407]
Comparable to Kosmos-2, ChatSpot [378] excels at following • OSRT [408]
precise referring instructions, utilizing CLIP ViT [22] and • PointNet [409]
Vicuna[295].X-LLM[383]convertsmulti-modalitydatainto • PointNet++ [410]
LLM inputs using X2L interfaces and treats them as foreign • 3D-CLR [411]
languages, where the X2L interface is inspired by the Q- • ConceptFusion [412]
FormerfromBLIP-2[6].mPLUG-Owl[379],[380]introduces
a two-stage training paradigm that establishes a connection Natural Language Processing, LLM, VLM:
between a pretrained LLM with a visual encoder and a • Long Short-Term Memory (LSTM) [221]
visualabstractor,therebyendowingLLMswithmulti-modality • Transformer [3]
abilities. Visual ChatGPT [382] proposes a prompt manager • Sentence-BERT / Sent.-BERT [413]
that manages the interaction between ChatGPT and 22 visual • DistilBERT [414]
foundation models, with the goal of equipping ChatGPT with • T5-small, T5-base, T5-XXL [285]
the capability to understand and generate images. • LLaMA [288]
Rather than employing intricate mechanisms to connect • LLaMA 2 [289]
components for different modalities, both LLaVA [7] and • Vicuna-V1.5 13B [295]
MiniGPT-4 [373] propose connecting vision encoders with • MPT [415]
LLMsthroughasinglelinearlayer.LLaVAadoptsatwo-stage • FLAN [292]
instruction-tuning approach, pretraining the CLIP ViT vision • Flamingo [234], [416]
encoder [22] in the first stage and finetuning the linear layer • Pythia [417]
and the LLaMA LLM [288] in the second stage. In contrast, • Phi-2 [418]
MiniGPT-4 freezes both the vision encoder (BLIP-2’s ViT + • GPT-NeoX [419]
Q-Former [6]) and the Vicuna LLM [295], only training the • Codex [420]
linear layer. Following MiniGPT-4, Video-LLaMA [374] han- • InstructGPT [375]
dlesvideosbyincorporatingtwobranchesforvideoandaudio, • ChatGPT [223]
each comprising a video/audio encoder and a BLIP-2-style • GPT-2 [276]

44
• GPT-3 [277] (SSL). In Dobb·E [441], SSL is also explored for 3D visual
• GPT-4 [278] inputs, through a method termed “Home Pretrained Represen-
• PaLI-X [364] tations,” using data collected from 22 homes in NYC. The
• Prismatic-7B VLM [421] authors extend SSL-pretrained representations beyond visual
• PaliGemma [422] inputs.AuRL[43]introduceslearningdynamicbehaviorsfrom
• PaliGemma 2 [423] audio, an often-overlooked yet important information source.
• Chameleon [424] Additionally, visual inputs were found to be insufficient for
• Emu3 [425] multi-fingeredrobotichands,leadingtoT-Dex[211],atactile-
• LWM-Chat-1M [426] based dexterous policy.
• LLaMA-Adapter [367] 2) Components of VLA: World Models: Masked World
Model (MWM) [442] innovates by modifying the vision en-
Action Modules: coderofDreamerV2toahybridcompositionofconvolutional
• LingUNet [427] neural network and vision Transformer. In training this novel
• Latent Motor Plans (LMP) [428] Convolutional-ViT vision encoder, MWM draws inspiration
• STORM [429] from the approach proposed in MAE [403]. Through the in-
• PerceiverIO [430] corporationofanauxiliaryrewardpredictionloss,theresulting
• DD-PPO [431] learnedlatent dynamicsmodelexhibitsa notableperformance
• ScaleDP [432] improvement across various visual robotic tasks.
• Symbol-tuning [433] SWIM [443] advocates for the use of human videos in
• DiT [434] training a world model due to the availability of large-scale
human-centric data. However, acknowledging the substantial
Others:
gap between human and robot data, SWIM addresses this
• DDPM [435]
disparity by grounding actions in visual affordance maps.
• DDIM [436]
This approach involves inferring target poses based on the
• Ravens [437]
affordancemaps,facilitatinganeffectivetransferofknowledge
• RLBench [178]
from human data to enhance robot control.
• Something V2: Something-something V2 [438]
Iso-Dream [444] introduces two key enhancements to the
Dreamer framework. The first enhancement focuses on op-
Abbreviations:
timizing inverse dynamics by decoupling controllable and
• TFM: transformer
noncontrollable dynamics. The second enhancement involves
• MCIL: multicontext imitation learning
optimizing agent behavior based on the decoupled latent
• MLE: maximum likelihood estimation
imaginations. This approach is particularly advantageous, as
• MPC: model predictive control
the noncontrollable state transition branch can be rolled out
• CVAE: conditional variational autoencoder
independently of actions, yielding benefits for long-horizon
• EDR: Everyday Robots
decision-making processes.
Transformer-based World Model (TWM) [56] shares the
E. Additional VLA-Related Work
same motivation as Dreamer but adopts a different approach
We include additional VLA-related work that could not be by constructing a world model based on the Transformer-XL
included in the main text due to the page limit. architecture[445].ThisTransformer-basedworldmodeltrains
1) Components of VLA: Pretraining: Value-Implicit Pre- a model-free agent in latent imagination by generating new
training (VIP) [24] capitalizes on the temporal sequences trajectories.Additionally,TWMsuggestsamodificationtothe
present in videos, distinguishing itself from R3M [23] by balanced KL divergence loss from DreamerV2 and introduces
attracting both the initial and target frames while simul- a novel thresholded entropy loss tailored for the advantage
taneously repelling successive frames. This objective aims actor-critic framework.
to capture long-range temporal relationships and uphold lo- SceneScript [446] introduces a set of structured language
cal smoothness. While their own experiments demonstrate commands that can define an entire scene, specifying the
superior performance compared to R3M in specific tasks, layout and objects. This language-based scene representation
subsequentresearchpresentsconflictingfindingsthroughmore distinguishes itself from previous methods—such as meshes,
comprehensive evaluations [31]. voxel grids, point clouds, or radiance fields—by generating
SpawnNet [439] utilizes a two-stream architecture incorpo- scenes in an autoregressive, token-based fashion. It achieves
rating adapter layers to fuse features from both a pretrained competitive results against state-of-the-art methods in layout
vision encoder and features learned from scratch. This inno- estimation and object detection.
vative approach eliminates the necessity of training the pre- 3) Components of VLA: Imitation Learning: BeT [447],
trained vision encoders while surpassing the performance of an imitation learning variant of the Trajectory Transformer,
parameter-efficient finetuning (PEFT) methods, as evidenced addresses the noisy and multimodal nature of non-expert
by experimental results in robot manipulation tasks. humandemonstrationdatabyusingk-means-basedactiondis-
Holo-Dex [440] proposes learning low-dimensional repre- cretization coupled with continuous action correction. C-BeT
sentations for visual policies using self-supervised learning [448] extends BeT by adding a target frame or demonstration

45
as the goal specification. VQ-BeT [449] further improves “robotics”. This pipeline yielded approximately 400 VLA-
BeT by incorporating vector quantization instead of k-means, related papers. Acknowledging the potential for automated
enabling better modeling of long-range actions. errors, we welcome feedback and requests for corrections
4) Subsequent Surveys on VLA: Since the initial release of regarding the included data.
this survey was made public, the field of embodied AI has
experienced a proliferation of VLA models, leading to the Abbreviations of institutes appearing in Figure 9:
emergence of several related surveys [450]–[460]. • AI2: Allen Institute for AI
5) Latest Developments of VLA: LLaRA [461] introduces • AIBD: Advanced Institute of Big Data
a data-centric method that uses a Vision-Language Model • ANU: Australian National University
to automatically relabel existing robot demonstration videos • AgiBot: AgiBot Research
with rich, descriptive language, significantly boosting the • Alexandria Univ.: Alexandria University
performance of downstream vision-language policies. • Alibaba: Alibaba Group, DAMO Academy
π 0 [116] undergoes further enhancements, including FAST • Anyverse: Anyverse Intelligence
[462]andπ 0.5 [463].FASTisanovelrobotactiontokenization • BAAI: Beijing Academy of Artificial Intelligence
methoddesignedtoprioritizedexterousskills.π 0.5 pushesthe • BACFBC: Innovation Center for Future Blockchain and
boundaries of in-the-wild generalization by incorporating co- Privacy Computing, Beijing
training with diverse data sources. • BIGAI: State Key Lab of General Artificial Intelligence
Mobility VLA [464] proposes a hierarchical policy that • BIT: Beijing Institute of Technology
integrates the commonsense reasoning capabilities of VLMs • BJUT: Beijing University of Technology
with a topological-graph-based low-level navigation policy. • BKLSISMI:BeijingKeyLaboratoryofSuperIntelligent
While many VLAs focus primarily on robotic arms, recent Security of Multi-Modal Information
advancements have extended their application to more com- • BNU: Beijing Normal University
plexembodiments,includinghumanoidandquadrupedrobots. • BUAA: Beihang University
• BUPT: Beijing University of Posts and Telecommunica-
Humanoid Robot: tions
• GR00T N1 [133] • Bosch: Bosch Center for Artificial Intelligence, Bosch
Corporate Research, Bosch Mobility Solutions, Bosch
• Humanoid-VLA [465]
Research
Quadruped Robot:
• Bretagne: Bretagne INP - ENIB
• QUAR-VLA [466] • ByteDance: ByteDance Research, ByteDance Seed
• QUART-Online [467] • CAS: Chinese Academy of Sciences
• MoRE [468] • CAU: Clark Atlanta University
Dexterous Hand: • CMU: Carnegie Mellon University
• DexGraspVLA [469] • CNRS: CNRS IRL 2010 CROSSING
• DexGrasp-VLA [470] • CSU: Central South University
Autonomous Vehicle: • CUHK: The Chinese University of Hong Kong
• CUHK(SZ): The Chinese University of Hong Kong
• Alpamayo-R1 [471] (Shenzhen)
• CoVLA [472] • CWRU: Case Western Reserve University
• DriveVLA-W0 [473] • Caltech: California Institute of Technology
• EMMA [474] • Cambridge: Cambridge University
• China Mobile: China Mobile Information Technology
Additionally,someVLAsaredesignedtofunctionasvirtual
Co., Ltd.,
assistants capable of taking actions within operating systems,
• China Telecom: China Telecom
video games, and other environments. Notable examples in-
• CityU: City University of Hong Kong
clude:
• Cognitive AI: Cognitive AI Lab
• CombatVLA [475] • Columbia: Columbia University
• JARVIS-VLA [476] • DSO: DSO National Laboratories
• DUT: Dalian University of Technology
We utilize various charts to visualize key aspects of VLA • Didi Chuxing: Didi Chuxing
developments from 2020 to 2025, including Figure 9, Fig- • Drexel: Drexel University
ure10,Figure11,andFigure12.TosupplementtheVLAsdis- • Duke: Duke University
cussedinthemaintext,weemployedahybridapproachcom- • ECNU: East China Normal University
bining automated scripting and manual searching to retrieve • EIT: Eastern Institute of Technology
VLA-related papers published between January 2020 and • EKUT: University of Tu¨bingen
December 2025. We queried the keywords “VLA”, “Vision- • ENS: E´cole Normale Supe´rieure
language-action”, and “Vision language action”, filtering false • ER: Everyday Robots
positives based on their relevance to “embodied AI” and • ETH: ETH Zurich

46
• EdUHK: The Education University of Hong Kong • NJU: Nanjing University
• Fudan: Fudan University • NJUPT: Nanjing University of Posts and Telecommuni-
• GDUT: Guangdong University of Technology cations
• Gachon Univ.: Gachon University • NKU: Nankai University
• Galaxea: Galaxea AI • NPU: Northwestern Polytechnical University
• Georgia Tech: Georgia Institute of Technology • NTU: Nanyang Technological University
• Google:Google,GoogleDeepMind,RoboticsatGoogle, • NUS: National University of Singapore
Google Research, Brain Team, Gemini Robotics Team • NVIDIA: NVIDIA Research
• HBUT: Hebei University of Technology • NWU: Northwestern University
• HIT: Harbin Institute of Technology • NYU: New York University
• HIT(SZ): Harbin Institute of Technology (Shenzhen) • NaUKMA: National University of Kyiv-Mohyla
• HKU: The University of Hong Kong Academy
• HKUST:HongKongUniversityofScienceandTechnol- • Noematrix: Noematrix Intelligence
ogy • OXE Team: Open X-Embodiment Collaboration
• HKUST(GZ): Hong Kong University of Science and • OpenHelix: OpenHelix Team
Technology (Guangzhou) • PCL: Peng Cheng Laboratory
• HUST:HuazhongUniversityofScienceandTechnology • PI: Physical Intelligence
• Hanyang Univ.: Hanyang University • PKU: Peking University
• Harvard: Harvard University • PSL: PSL Research University
• Horizon: Horizon Robotics • Penn State: Pennsylvania State University
• Huawei: Huawei Technologies, Huawei Noah’s Ark Lab • Pitt: University of Pittsburgh
• HuggingFace: Hugging Face • PolyU: The Hong Kong Polytechnic University
• Hyundai: Hyundai Motor Company • Princeton: Princeton University
• IC: Imperial College London • QMUL: Queen Mary University of London
• IEIT: IEIT SYSTEMS Co., Ltd. • Qi Zhi: Shanghai Qi Zhi Institute, Shanghai Qizhi Insti-
• IIIT-H: IIIT Hyderabad tute
• IIT: Istituto Italiano di Tecnologia • Qualcomm: Qualcomm AI Research
• IMT: IMT Atlantique • RU: Rutgers University
• Infinigence: Infinigence AI • RUC: Renmin University of China
• JHU: Johns Hopkins University • SBU: Stony Brook University
• JLU: Jilin University • SCUT: South China University of Technology
• KAIST: KAIST AI • SH AI Lab: Shanghai AI Laboratory
• KIT: Karlsruhe Institute of Technology • SHU: Shanghai University
• Kobe Univ.: Kobe University • SII: Shanghai Innovation Institute
• Korea Univ.: Korea University • SJTU: Shanghai Jiao Tong University
• LZU: Lanzhou University • SKKU: Sungkyunkwan University
• Lehigh Univ.: Lehigh University • SNU: Seoul National University
• LiAuto: LiAuto Inc. • STU: ShanghaiTech University
• LimX: LimX Dynamics • SUST: Southern University of Science and Technology
• Logos: Logos Robotics • SUTD: Singapore University of Technology and Design
• Lumina: Lumina Group • SYSU: Sun Yat-sen University
• Lumos: Lumos Robotics • SZU: Shenzhen University
• MBZUAI: Mohamed bin Zayed University of Artificial • Sea AI: Sea AI Lab
Intelligence • SenseTime: SenseTime Research
• MEGVII: MEGVII Technology • Siemens: Siemens Corporation
• MIPT: IAI MIPT • Simplexity: Simplexity Robotics
• MIT: Massachusetts Institute of Technology • Sofia Univ.: Sofia University “St. Kliment Ohridski”
• MMLab: MMLab @ CUHK, MMLab @ HKU • Sony: Sony Interactive Entertainment, Sony Research
• Macalester: Macalester College • Sorbonne Univ.: Sorbonne University
• Meta: Meta AI, FAIR-MetaAI, Meta Reality Labs • Spirit: Spirit AI
• Microsoft:MicrosoftResearch,MicrosoftResearchAsia, • Stanford: Stanford University
Microsoft Zurich • Syracuse: Syracuse University
• Midea: Midea Group • T-Stone: T-Stone Robotics Institute
• Mila: Mila — Quebec AI Institute • TJU: Tianjin University
• Monash Univ.: Monash University • TUM: Technical University of Munich
• Moxin: Moxin (Huzhou) Technology Co., Ltd. • Taiwan Univ.: National Taiwan University
• NAVER: NAVER AI Lab • Tencent: Tencent Inc., Tencent Robotics X, Wechat AI
• NEU: Northeastern University • Tongji: Tongji University

47
• Toyota: Toyota Research Institute Xiaomi EV, Xiaomi Robotics
• Tsinghua: Tsinghua University • Yale: Yale University
• Turing: Turing Inc. • Yinwang: Yinwang Intelligent Technology Co., Ltd.
• U of U: University of Utah • Yuandao: Yuandao AI
• UATX: The University of Austin at Texas • ZGCA: Zhongguancun Academy
• UAlberta: University of Alberta • ZGCI: Zhongguancun Institute of Artificial Intelligence
• UArizona: University of Arizona • ZJU: Zhejiang University
• UArkansas: University of Arkansas • ZZU: Zhengzhou University
• UBC: The University of British Columbia • ZhiCheng: ZhiCheng AI
• UCAS: University of Chinese Academy of Sciences • ZhongkeHuiling:BeijingZhongkeHuilingRobotTech-
• UCB: University of California, Berkeley nology Co
• UCL: University College London • iFlyTek: iFlyTek Research and Development Group
• UCLA: University of California, Los Angeles • mimic: mimic robotics
• UCSD: University of California San Diego • valeo: valeo.ai
• UCSI: UCSI University
• UCSP: Universidad Cato´lica San Pablo List of VLAs appearing in Figure 9:
• UChicago: University of Chicago • 3D Diffuser Actor [477]
• UESTC: University of Electronic Science and Technol- • 3DS-VLA [478]
ogy of China • 4D-VLA [479]
• UIC: University of Illinois Chicago • A2C2 [480]
• UIUC: University of Illinois Urbana-Champaign • A3VLM [481]
• UM: University of Macau • ACG [482]
• UMD: University of Maryland, College Park • ACT [98]
• UMU: Umea˚ University • Act3D [89]
• UNSW: University of New South Wales • ActDistill [483]
• UOsaka: The University of Osaka • ActionFlow [484]
• UPenn: University of Pennsylvania • AdaMoE [485]
• UQ: University of Queensland • ADP [486]
• USC: University of Southern California • AFI [487]
• USST: University of Shanghai for Science and Technol- • AgentWorld [488]
ogy • AINA [489]
• USTC: University of Science and Technology of China • Alpamayo-R1 [471]
• USYD: The University of Sydney • AMS [490]
• UT Austin: The University of Texas at Austin • ANNIE [491]
• UT Dallas: University of Texas at Dallas • AsyncVLA [492]
• UTN: University of Technology Nuremberg • ATE [493]
• UTS: University of Technology Sydney • AutoDrive-R2 [494]
• UTokyo: The University of Tokyo • AutoPrune [495]
• UW: University of Washington • AutoVLA [496]
• UWarsaw: University of Warsaw • AVA-VLA [497]
• UW–Madison: University of Wisconsin-Madison • Avi [498]
• UdeM: Universite´ de Montre´al • BadVLA [499]
• Uni Freiburg: University of Freiburg • BayesVLA [500]
• UofT: University of Toronto • BC-Z [80]
• VT: Virginia Tech • Being-H0 [501]
• VinUni: VinUniversity • Beyond Success [502]
• WHU: Wuhan University • Bi-VLA [503]
• WMU: Wenzhou Medical University • Bi-VLA 2025 [504]
• Waseda: Waseda University • BridgeVLA [505]
• Westlake Univ.: Westlake University • BYOVLA [506]
• X-Era: X-Era AI Lab • CCoL [507]
• X-Humanoid: Beijing Innovation Center of Humanoid • ChatVLA-2 [508]
Robotics • CLAW [509]
• XDU: Xidian University • CLIPort [28]
• XJTU: Xi’an Jiaotong University • CLIP-RT [510]
• XMU: Xiamen University Malaysia • ClutterDexGrasp [511]
• XPeng: XPeng Motors • CoC-VLA [512]
• Xiaomi: Beijing Xiaomi Robot Technology Co., Ltd., • CogACT [120]

48
• CogVLA [513] • FAST [462]
• ColaVLA [514] • FastDriveVLA [562]
• CombatVLA [475] • Fast-in-Slow [563]
• ConRFT [515] • FLARE [564]
• ControlVLA [516] • FLOWER [565]
• Control Your Robot [517] • FlowVLA [566]
• CoReVLA [518] • ForceVLA [567]
• CoT4AD [519] • FORGE-Tree [568]
• CoT-VLA [77] • FPC-VLA [569]
• Counterfactual VLA [520] • FreezeVLA [570]
• CoVLA [472] • FTM, FLA [571]
• CRISP [521] • G0 [572]
• CycleManip [522] • Gato [573]
• DEAS [523] • GEN-0 [574]
• DeeAD [524] • Genie Envisioner [135]
• DeepThinkVLA [525] • GeoAware-VLA [575]
• DeeR-VLA [102] • GeRM [576]
• Dejavu [526] • GEVRM [577]
• DepthVLA [527] • GF-VLA [578]
• Dexbotic [528] • GLaD [579]
• DexGrasp-VLA [470] • GLUESTICK [580]
• DexGraspVLA [469] • GR00T N1 [133]
• DexVLA [121] • GR 1.5 [581]
• Diffusion Policy [529] • GRAPE [582]
• Diffusion-VLA [530] • GraphCoT-VLA [583]
• DiffVLA [531] • GraspVLA [584]
• DIPOLE [532] • GraSP-VLA [585]
• DLR [533] • GR-Dexter [586]
• Don’t Blind Your VLA [534] • GR-RL [587]
• DP3 [106] • HAMSTER [588]
• DP-VLA [535] • Helix [589]
• DreamTacVLA [536] • HiF-VLA [590]
• DreamVLA [537] • HiMoE-VLA [591]
• Dream-VLA [538] • Hi-ORS [592]
• DriveVLA-W0 [473] • Hi Robot [593]
• DualVLA [539] • HiRT [594]
• DuoCore-FS [540] • Hiveformer [87]
• dVLA [541] • HULC [82]
• EBT-Policy [542] • HULC++ [83]
• ECoT [543] • Humanoid-VLA [465]
• ECoT-Lite [544] • HumanVLA [595]
• EfficientVLA [545] • HybridVLA [122]
• Ego-PM [546] • iFlyBot-VLA [596]
• EmbodiedCoder [547] • ImaginationPolicy [597]
• Embodied-SlotSSM [548] • Impromptu VLA [598]
• EMMA [549] • INSIGHT [599]
• Emma-X [550] • Instruct2Act [103]
• EndoVLA [551] • InstructVLA [600]
• EO-1 [552] • IntentionVLA [601]
• ERIQ [553] • InteractGen [602]
• ERMV [554] • Interactive Language [86]
• ET-VLA [555] • InternVLA-M1 [603]
• EveryDayVLA [556] • iRe-VLA [604]
• Evo-1 [557] • IRL-VLA [605]
• ExpReS-VLA [558] • JARVIS-VLA [476]
• EyeVLA [559] • KV-Efficient VLA [606]
• F1 [560] • Language costs [85]
• FailSafe [561] • LAPA [123]

49
• LatBot [607] • OpenVLA [659]
• LAWM [608] • OpenVLA-OFT [114]
• LCDrive [609] • OTTER [660]
• LITEN [610] • PerAct [88]
• Lite VLA [611] • PhysBrain [661]
• LLaRA [461] • PhysiAgent [662]
• LoHoVLA [612] • π 0 [116]
• LoLA [613] • π 0.5 [463]
• Long-VLA [614] • π 0 ∗ .6 [18]
• LVP [615] • π RL [663]
• ManiAgent [616] • PIVOT [132]
• Mantis [617] • PixelVLA [664]
• ManualVLA [618] • PLA [665]
• MAP-VLA [619] • Point-VLA [666]
• E 0 [620] • PosA-VLA [667]
• MCIL [82] • Prophet [668]
• MDT [621] • QAIL+QBC [669]
• MemER [622] • QDepth-VLA [670]
• MemoryVLA [623] • Q-Transformer [671]
• MetaVLA [624] • QUART-Online [672]
• MG-Select [625] • QUAR-VLA [466]
• MimicDreamer [626] • R2R2R [673]
• MindDrive [627] • RDT-1B [674]
• Mind to Hand [628] • Reasoning-VLA [675]
• MiVLA [629] • ReflectDrive [676]
• MLA [630] • REGENT [677]
• MM-ACT [631] • ReKep [678]
• Mobility VLA [464] • RETAIN [679]
• MoH [632] • RetoVLA [680]
• MoIRA [633] • ReVLA [681]
• MoMaGen [634] • RICL [682]
• MoManipVLA [635] • RoboCat [683]
• MonoDream [636] • RoboChemist [684]
• MOO [637] • RoboDual [685]
• MoRE [638] • RoboFlamingo [686]
• MotionTrans [639] • RoboMamba [117]
• MoTo [640] • RoboMatrix [687]
• MotoVLA [641] • RoboMonkey [79]
• Motus [642] • RoboNeuron [688]
• Moxin-VLA [643] • RoboNurse-VLA [689]
• MT-ACT [99] • RoboOmni [690]
• MUVLA [644] • RoboOS-NeXT [691]
• NaVILA [645] • RoboPoint [692]
• NICE [646] • RoboTAP [131]
• NitroGen [647] • Robotic Assistant [693]
• NORA-1.5 [134] • RoboUniView [101]
• Oat-VLA [648] • RoboVLMs [694]
• OBEYED-VLA [649] • RobustVLA [695]
• OccLLaMA [650] • RoVer [696]
• OccVLA [651] • RPD [697]
• Octo [108] • RS-CL [698]
• OC-VLA [652] • RT-1 [95]
• OmniJARVIS [653] • RT-2 [699]
• OmniReason [654] • RT-A [700]
• OmniSAT [655] • RT-H [701]
• OmniVLA [656] • RT-RAS [702]
• OneTwoVLA [657] • RT-Trajectory [703]
• OpenHA [658] • RT-X [704]

50
• RVT [90] • V-GPS [78]
• RVT-2 [705] • Video2Act [754]
• RynnVLA-001 [706] • VideoVLA [755]
• RynnVLA-002 [707] • VIMA [128]
• SafeVLA [708] • VINE [756]
• SARA-RT [709] • ViVLA [757]
• ScaleDP [710] • VLA-0 [758]
• SC-VLA [711] • VLA-4D [759]
• SEAL [712] • VLA-Adapter [760]
• SeeDo [713] • VLA-AN [761]
• SeqVLA [714] • VLA-Cache [762]
• ShowUI [715] • VLA-Fool [763]
• Sigma [716] • VLA-OS [764]
• SimpleVLA-RL [717] • VLA-Pilot [765]
• SITCOM [718] • VLA-Pruner [766]
• SmolVLA [719] • VLAPS [767]
• SOLAMI [720] • VLA-R [768]
• Spatial Forcing [721] • VLA-R1 [769]
• SpatialVLA [118] • VLA-RAIL [770]
• SpecPrune-VLA [722] • VLA-RFT [771]
• Spec-VLA [723] • VLAS [772]
• SQAP-VLA [724] • Vlaser [773]
• SSM-VLA [725] • VLASH [774]
• STARE-VLA [726] • VLM2VLA [775]
• StereoVLA [727] • VLMimic [776]
• STORM [728] • VoxPoser [777]
• SUDD [107] • VST [778]
• SurgWorld [729] • WAM-Flow [779]
• SwiftVLA [730] • WholeBodyVLA [780]
• TabVLA [731] • WMPO [781]
• TACO [732] • WorldVLA [124]
• TacRefineNet [733] • WristWorld [782]
• Tactile-VLA [734] • X-Humanoid [783]
• TA-VLA [735] • XR-1 [784]
• ThinkAct [736] • X-VLA [785]
• ThinkBot [737]
• TinyVLA [119] 6) Beyond VLA: Recent research has expanded beyond
• TraceVLA [115] standard VLA architectures in several key directions:
• TrackVLA [738] • VLA + World Model: Architectures that unify VLAs
• TrajBooster [739] with world models.
• Transporter Networks [437] – WorldVLA [124]
• TriVLA [740] – UniVLA [125]
• TVVE [741] – NORA-1.5 [134]
• UD-VLA [742] – RynnVLA-002 [707]
• UnderwaterVLA [743] – Motus [642]
• UniCoD [744]
• PLA, MLA:Modelsincorporatingperceptionmodalities
• Unified-IO 2 [745]
beyond vision.
• Uni-NaVid [746]
– Perception-Language-Action framework (PLA)
• UniPi [84]
[665]
• UniUGP [747]
– Multisensory Language–Action model (MLA) [630]
• UniVLA [125]
• UPA-RFAS [748] • VAM: Video-Action Models that jointly capture seman-
• UP-VLA [749] tics and dynamics during video pretraining, enabling
• UrbanVLA [750] more efficient post-training for low-level robot control.
• USIM & U0 [751] – mimic-video (VAM) [753]
• UWM [752]
• VAM [753]
• VER [129]

51
2020-2021 (4) 2022 (9) 2023 (21) 2024 (55) 2025 (276)
htnoM
- - Generalized VLA [41] Meta (5) [84] IIT (3) [1 W 3][ h 2 o 2 le ][ B 3 o 4 d ][ y 6 V 3 L ][ A 73] X-Hu [1 m 4 a ] noid
— Large VLA [42] UT Austin (5) [85] GigaAI (3) ViVLA Video2Act VideoVLA WAM-Flow
[57]LimX [19][2][40][70][74] [13][15][1][28] [108][13]
[1] Tsinghua (71) [43] ECNU (5) [86] Harvard (3)
VINE VLA-AN VLA-RAIL
[2] PKU (54) [44] Midea (5) [87] Xiaomi (3) [31][79] Korea Univ. NAVER [7] Differential... China Mobile
[3] SJTU (39) [45] Alibaba (5) [88] CityU (3) [12][14] S [3 u ] rg [9 W ]S or K ld KUWMU [10][1 T 2 A 3 C ][ O 1][40] U [2 n 0 iU ][2 G 5 P ] [15][62 V ][ A 6 M ]mimic
[4] CAS (30) [46] X-Era (5) [89] UM (3) RoboNeuron STARE-VLA STORM StereoVLA
[5] Google (24) [47] MBZUAI (5) [90] Uni Freiburg (2) [1][4]MICRO [111][39][49] [19] [16][22][2][37][4]XMU
[6] UCB (22) [48] HIT (5) [91] UCSD (2) [25][48][58][ P 8 h 2 y ] s D B e ra e i p n CyboZGCI [11 P 6 o ][ i 1 n ] t- [ V 3 L ] A [50] Pos [ A 59 -V ] LA RE [ T 6 A ] IN
[7] ZJU (22) [49] Huawei (5) [92] ENS (2) Motus Moxin-VLA OBEYED-VLA
[105][1][2][38] [86] [120]
[8] Stanford (21) [50] Tongji (5) [93] CNRS (2)
LoLA ManualVLA MiVLA Mind to Hand MindDrive
[9] NVIDIA (19) [51] Caltech (4) [94] UCL (2) [15][4] [12][2] Simplexity [50][78] [83] [58][87]
[10] USTC (19) [52] Toyota (4) [95] Hupan Lab (2) [17][25][35][7] HiF- W VL e A stlake Rob... [1 H 3] iM [1 o 5 E ][ - 1 V ] L [2 A 8] L E C K D U ri T ve [24] L [ V 6] P [86]
[11] SH AI Lab (18) [53] UIUC (4) [96] OpenHelix (2) FTM, FLA GLaD GR-Dexter GR-RL
[12] CUHK (18) [54] UPenn (4) [97] NYU (2) [19][46] [47]UIC [20] [20]
[13] Fudan (18) [55] Dexmal (4) [98] MEGVII (2) DIP [1 O ] LE Drea [2 m 2 - ] VLA Drea N m W Ta U cVLA DuoC [8 o 3 r ] e-FS [3 E 4 R ][ I 6 Q 3]
[14] NUS (15) [57] BIT (4) [99] TJU (2) ActionFlow BayesVLA ColaVLA Counterfactual VLA
[10]IEIT [6][7] [12][1] Didi Chuxing [77][8][9]
[15] Microsoft (12) [58] HUST (4) [100] StepFun (2)
VLASH VST WMPO XR-1 iFlyBot-VLA AFI
[16] BAAI (12) [59] USYD (4) [101] UChicago (2) [24] [1][20][22] [20][40] [2][33][36] LindenBot iFlyTek [3][59]
[17] Westlake Univ. (12) [61] Tencent (4) [102] Galaxea (2) [17] Penn V S L t A a - t F e ool SonyXDU [12][ V 84 L ] A- T P - i S lo t t one [1 V 0 L ][ A 1 - 6 P ] r [3 u ] n [ e 4 r 8] V [ L 3 A 1 - ] R
[18] CMU (11) [62] ETH (4) [103] Anyverse (2) UD-VLA UPA-RFAS VLA-4D
[19] SYSU (11) [63] AgiBot (4) [104] SenseTime (2) [17][25][7] Monash Univ. [23]DSO [14][58]
[20] ByteDance (10) [64] UTN (3) [105] Horizon (2) [10 R ][ e 1 a 4 s ] o [1 n ] in [7 g 6 - ] V U L N A SW R [ y 4 n 5 n ] V [7 L ] A [9 -0 5 0 ] 2 S U ig C m S a I [1][2][ S 3 w 6] if [ t 8 V 5 L ] A Moxin
[22] HKU (10) [65] Georgia Tech (3) [106] INSAIT (2) Mantis MoH NICE PixelVLA Prophet
[13][34][35][38][3] [12][72]UNC [49] [113][47][4][75] [13][34]Logos
[23] NTU (10) [66] KIT (3) [107] Sofia Univ. (2) Lite VLA MAP-VLA MM-ACT
[24] MIT (9) [67] Columbia (3) [108] Yinwang (2) CAUSiemens [1][23][32][75]VinUni [10][11][13][22][3][7]
[25] HKUST(GZ) (9) [68] U of U (3) [109] NaUKMA (2) [93]Bretagne IM G T raSP P -V ri L o A riAnalytica UMU Inte [1 ra ][ c 3 t 2 G ] en [ L 1 a 5 t ] B [4 o ] t
[ [ 2 2 6 7 ] ] U Q W i Z h (8 i ) (8) [ [ 6 7 9 0 ] ] A A I I 2 2 R (3 o ) botics (3) [ [ 1 1 1 1 0 1 ] ] P IC C ( L 2 ) (2) Ever [ y 1 D 2 a 2 y ] VLA E [1 v 1 o 1 -1 ] ExpR [1 e 8 S ] -VLA [3 E ] y [4 e ] V D L U A T Gen G e E ra N l - is 0 t AI
[28] XJTU (8) [71] STU (3) [112] Princeton (2) [15][1][ D 40 L ] R [74]CSU [ D 4 e 7 e ][ A 88 D ] [1 D 0 u ] a [1 lV 2] L [ A 2] ET [2 -V 9 L ] A Embo [ d 1 i 2 e 0 d ] - [ S 18 lo ] tSSM
[29] SHU (7) [72] RUC (3) [113] ANU (2) [118][88]E C d C U o H L KPolyU [1 C 0 o ][ C 1 - 4 V ] L [7 A 6] CoT [2 4 ] AD Cy [1 cl 2 e ] M [1 a 9 n ] ip
[30] PI (7) [73] MMLab (3) [114] Drexel (2) AVA-VLA ActDistill AsyncVLA Beyond Success
[31] KAIST (7) [74] WHU (3) [115] VT (2) [119][12]LiAuto [50]AIBDUTS [11][1][7]Lumos [15]JLU
[32] BUPT (7) [75] SCUT (3) [116] Spirit (2) [14 W ] r [ i 2 s ] tW [36 o ] r [ ld 40] [1 X 1] -V [1 L ] A [2] [19][460]GDUT π [30* 0.6] [4 A 1 I ] N [9 A 7]
[33] BUAA (7) [76] LZU (3) [117] RLWRLD (2) VLA-RFT Vlaser
[34] SII (7) [77] UCLA (3) [118] NKU (2) [13][17][32][7][96]HBUTZZU [10][11][121][13][14][1][35][3][7]SZU
[35] NJU (7) [78] UESTC (3) [119] BJUT (2) T [1 a 3 b ] V [8 L 8 A ] [11 U ][ n 1 i ] C [2 o 7 D ][2] [10 U ] r [1 b 6 a ] n [ V 2 L ][ A 37] VL [9 A ] -0 [1 V ] L [ A 4] -R [8 1 5]
[36] X-Humanoid (6) [79] SNU (3) [120] UArkansas (2) Rob [1 o 3 O ] mni Rob [2 o 4 ti ] c [ 6 A 2 s ] s [ i 8 s ] tant [ S 68 E ] A [9 L ] SIT [1 C 8 O ] M [1 S 7 p ][ a 1 t ] ia [2 l F 5] o [ r 7 c 5 in ] g [7]
[ [ 3 3 7 8 ] ] G Bo a s lb c o h t ( ( 6 6 ) ) [ [ 8 8 0 1 ] ] S In U fin T i D ge ( n 3 c ) e (3) [ [ 1 1 2 2 1 2 ] ] N Pi E tt U (2 ( ) 2) [4] ZQhDoenpgtkhe-V HLuAiling [11 R 7 S ][3 -C 1] L [6] [110][11] R [1 o 9 V ][ e 2 r 3][46][4] R [1 o 6 b ] o [2 O ] S [3 -N 3] e [ X 4] T
[39] TUM (6) [82] ZGCA (3) [123] China Telecom (2) [1 M 1 G 7] - [ S 31 e ] le [7 c 9 t ] [1 M 0 a ][ n 1 i 1 A 9 g ] e [3 n 5 t ] Me [ m 8] ER M [1 e 8 ta ][ V 4 L 1 A ] M [ o 4 M 2] a [ G 8] en Om [1 n 0 iS ] AT
[40] HKUST (6) [83] Astribot (3) INSIGHT IntentionVLA InternVLA-M1 LITEN
Yale [10][35][48][55] [11] Intern Robotics [30][6]
EmbodiedCoder FORGE-Tree FailSafe GR 1.5 Hi-ORS
[12][33][4] [66] [26] [5] [1][61]
Don't Blind Your VLA DriveVLA-W0 EBT-Policy
Cognitive AI MIPT [108][4] [1][2][53]ZhiCheng
DeepT [6 h 1 in ] kVLA De [3 ja ] vu D [ e 1 p 0 t 2 h ] V [1 L ] A DexG [ r 2 a 0 s ] p-VLA [ D 1 e 0 x 0 b ][ o 5 t 5 ic ]
AdaMoE Alpamayo-R1 Avi DEAS
[1][22][3][50] D-Robotics [14] [54][77] [31][42][6][9]
UnderwaterVLA VLA-Adapter VLM2VLA dVLA ACG
[113][17][7] [17][25][32][7][96] [112] [2][3] [31]
Sp [ e 3 c 4 P ] r [ u 3 n ][ e 8 - 1 V ] LA [1 T 6 A ][ - 1 V ] L [2 A 3] TacR [ e 8 f 7 in ] eNet [1 T 7 r ] a [3 jB 4 o ] o [3 s ] te [7 r ]
[35 S ] Q U A A P r - i V zo L n A a [1][ S 28 S ] M [4 - 5 V ] L A A map [1 S 1 e 4 q ][ V 1 L 1 A 5] Simp [ l 1 e ] V [2 L ] A-RL
RetoVLA RoboChemist RobustVLA RynnVLA-001
Gachon Univ. [1] [12][1][2][33] [2]
OccVLA OmniVLA OpenHA PhysiAgent ReflectDrive
[13][1][27][28][3] [6] [2] [1][2][6] [1]
MoTo MotionTrans MotoVLA Oat-VLA
[1][23][32] [1][27][2][3][74] [106][107][62] [94]Qualcomm
LAWM MLA MUVLA MimicDreamer
[47] Alexandria U... [12][2][36] [55][57][99] [1][4][85]NJUST
GeoAw [4 a 7 r ] e-VLA ImaginationPolicy KV-E [1 f ] fic U ie o n fT t VLA
F1 FLOWER FPC-VLA FreezeVLA GLUESTICK
[11][48] [15][66] [118][121][87][89] [11][13]Sea AI [86] FieldAI
Uni-NaVid CLAW CRISP CoReVLA Control Your Robot EMMA
[16][2][37] [114][115] [39] [50] [3]Lumina ScaleLabUSST [5][80]
RoboVLMs TraceVLA AutoPrune Bi-VLA 2025
[14][1][20][3][4] [15] Capital One UMD [103][3][4][71]AutoLab BKLSISMI KargoBot Kobe Univ. UOsaka
QUART-Online REGENT VLAPS A2C2 ADP ANNIE ATE
[7] [54] MilaUBCUdeM UTokyo [59] [4][65] UT Dallas [123][12][1]NPU
NaVILA QAIL+QBC OC-VLA OmniReason RICL TVVE
[91][9]USC Hanyang Univ. Hyundai [104][11][1][35][7] [25][40] [54] [110][19][23][46][4]
SOLAMI ShowUI Emma-X IRL-VLA Long-VLA MemoryVLA MonoDream
[104][23]S-Lab [15] [5][80] [1][29][38][3] [7] [100][1][48][55][98][99] [105][14][72]BACFBC
[5 R ]U T A -A TX [12][4] R [5 o 7 b ] o [ M 98 a ] t W rix aseda [1 G 0 0 2] Un G ive F r - s V it L y A o... Geni [ e 1 4 E ] n [3 vi 3 s ] ioner Grap [1 h 0 C ][ o 4 T 9 - ] VLA
CogACT DeeR-VLA GRAPE AMS AgentWorld CogVLA EO-1 Ego-PM FlowVLA
[10][15][1][4] [1][20] [101] [3]SUST [3][61] [48] [48] [14]Show Lab [25][3]
V [1 - 8 G ] P [6 S ] [2 V 2 L ] M [2 i ] m [5 ic 7] CL [ I 7 P 9 - ] RT M [1 o 0 IR 9] A [1 P ] L [3 A 9] [1] S [8 p 1 e ] c [ - 8 V 2 L ] A [89] T [ a 1 c ] t [ i 3 le ] - [ V 7 L 8 A ] [9] T T a h iw in a k n A c U t niv.
DP-VLA LAPA RDT-1B DreamVLA ERMV FastDriveVLA InstructVLA
ETRI [15][26][31][69][9] [1] [10][1][2][37][3][53]EIT [3]Cambridge [2]XPeng [10][11][7]
TinyVLA BYOVLA UniVLA VLA-OS WorldVLA Being-H0
[29][36][43][44]Syracuse [112] [16][1][4] [10][14][1][23] [45][7][95] [2][72]BeingBeyond
ReVLA RoboNurse-VLA ScaleDP SeeDo SmolVLA USIM & U0
[106][107] [12][84] [29][36][43][44] [97] [92]HuggingFace Sorbonne Univ. valeo [4]
CoVLA HiRT OccLLaMA ReKep EfficientVLA Fast-in-Slow NORA-1.5 R2R2R RoboMonkey
Turing [1][27][6] [13][1] [67][8] [103][28][3][48][78] [12][16][2][70] [23][80]QMUL [52][65] [6][8][9]
[6][8] E U C W oT arsaw M [6 D 6 T ] Mobil [ i 5 ty ] VLA [20][35 B ] r [ i 4 d ] ge F V i L ve A Ages ClutteDrDuekxeGrasp [1] C [2 o ] n [8 tr 3 o ] lV B L I A GAI [1][ D 38 if ] fV [3 L ] A RIX
[26] R [6 o 9 b ] o [9 P ] o U in C t SP Ro M bo e U it n u i a V n iew [18][1][2 π ]R[L4][81][82] 3 [ D 1 S 2] -V [2 L ] A 4 [1 D 3 - ] V [4 L 9 A ] [45 A ] u [7 to 6 D ]C r W ive R -R UU 2 Q Au [ t 7 o 7 V ] LA
U [2 n 6 i ] fi [ e 5 d 3 - ] I [ O 69 2 ] RV [9 T ] -2 [11 R ][ o 2 b 2 o ] D [3 u ] a [6 l 3] R [ o 1 b 6 o ][ M 2] a [ m 70 b ] a [ L 1 o 3 H ][ o 3 V ][ L 7 A 1] [116 O ][ n 1 e 1 T ][ w 13 o ] V [ L 1 A ][27] [16][2 T ] r [ a 3 c 3 k ] V [3 L 7 A ]BNU π [300.5]
QU [1 A 7 R ][ - 7 V ] LA SAR [5 A ] -RT T [ h 1 i 8 n ] k [ B 1 o ] t Om [ n 1 i 2 J ] A [2 R ] VIS [24][3 O 0] p [5 e 2 n ] V[5L]A [6][8] [11][13][14][28] F [2 o 9 rc ] e [3 V 4 L ] A [3] Noematrix [16 G ][ r 2 a 2 s ] p [ V 2 L ][ A 37] Impro [1 m ][ p 3 t 8 u ] VLA
RT-Trajectory RoboFlamingo HumanVLA LLaRA ChatVLA-2 ECoT-Lite EndoVLA FLARE
[5][8][91] Intrinsic [14][1][20][3] [3][61] SBUUW–Madison [29][43][44] [8] [12][39] [51]
MT-ACT Q-Transformer RT-X A3VLM Diffusion-VLA MoRE OTTER RPD SafeVLA UWM BadVLA
[18][1] [5] OXE Team [11][12][2][3]RUYuandao [29][43][44] [19][46] [41][6] [64] [2] [26][52] [58] Lehigh Univ.
[1][42][51][8] V [ I 9 M ] A Macalester [ R 5] T E -1 R R [ T 5 - ] 2 [ S 5 U ][ D 6 D 7] V [ o 5 x 3 P ] o [8 s ] er Ro [5 b ] o [9 T 4 A ] P SC [ - 2 V ] LA [ π 300] Com [ b 4 a 5 t ] VLA GR0 [5 0 1 T ] N1 [ H 1 y 2 b ][ r 1 id 6 V ] L [2 A ] JARV [ I 2 S ] -VLA M [ o 1 M ][ a 2 n 3 i ] p [3 V 2 L ] A
H [6 U 4 L ][ C 9 + 0 + ] Interactive [5 L ] anguage [11 I ] n [ s 1 t 2 ru ][ c 2 t ] 2A [3 c ] t [4] A [ c 1 t 8 3 ] D R [9 V ] T Rob [5 o ] Cat [7]CC V A E I R ReLER S B k i o -V lte L c A h [18 O ][ c 6 t ] o [8] Human [7 o ] id-VLA OpenV [8 L ] A-OFT VL [ A 3 - ] C [5 a 9 c ] he V [ L 2 A 8] S [ C 24 o ] T [ - 8 V ] L [9 A ]
C [2 L 6 I ] P [ o 9 r ] t [ B 6 C ][ - 8 Z ] [92][93] H III i T ve -H forme In r ria PSL [ P 2 e 6 r ] A [9 c ] t Di [ f 2 fu 4 s ] i [ o 5 n 2 ] P [6 o 7 li ] cy M [ O 5] O [41 A ][ C 6 T ][8] [11][1 D ] P [2 3 7][3] G [ e 1 R 7] M R [ T 5 - ] H De [2 x 5 G ] r [ a 2 s ][p5V4L]A D [4 e 3 x ] V [4 L 4 A ] G [1 E 7 V ] R [7 M ] HA [2 M 4 S ][ T 9 E ] R FI H G e U li R x E [3 H 0 i ] R [6 o ] b [ o 8 t ]
M [ C 5] IL Transport [ e 5 r ] Networks [6 H 4 U ][ L 9 C 0] L [2 a 4 n ] g [ u 2 a 6 g ][ e 6 8 c ] o [ s 9 t ] s G [ a 5 t ] o [24][5][65] U [6 n ] iPi UAlberta [ R 6 T 8] -R JH A U S 3D Diff [ u 1 s 8 e ] r Actor [4 P 2] IV [5 O ] T [8] [30 F ] A [6 S ] T [8] [11 S ][ p 7 a 1 t ] iaTlVeLleAAI U [1 P ] - [ V 2 L 7 A ] [ i 1 R ] e [2 -V 7] L [ A 6] Con [4 R ] FT
Figure 9: Timeline of Vision-Language-Action models from 2020 to 2025. Bracketed numbers indicate the publication count
for the corresponding year or institute.

52
Google MC T IL ransporter Networks Gat I o nteractive La R n T g - u 1 ag M e OO Q R - T T - r 2 a R n T s - f T o r r a m je e c r t P o I r V yR O T T -H Mobility VLA RT-A GR 1.5 Venue R G ob r o o t u ic p s
Columbia Diffusion Policy (CoRL, ICRA,
SUDD
IROS, RSS, ...)
OpenVLA-OFT
Stanford ACT VoxPoser OpenVL R A eKep ECoT-Lite Vision
PI π0 F H π A0 i S. R 5T obot π0 * .6 ( E C C V C P V R , , . . I . C ) CV,
UW CLIPort PerAct RoboPoint UWM ML
(NIPS, ICLR,
OXE Team RT-X ICML, AAAI,
V-GPS IJCAI, TMLR, ...)
UCB BC-Z Octo OTTER
ECoT
Preprint
Qi Zhi DP3 OccVLA (Cited by > 5)
MIT UniPi HAMSTER Other
Tsinghua ThinkBot RD C R T o o - g 1 b A B o C V T LMsOneT T w a M o c V e til L m e A - o V ry L V A LA
VIMA ThinkAct
NVIDIA Language costs RVT-2 CoT-VLA
RVT
ByteDance RoboFlamingo BridgeVLA
FLARE
Caltech GR00T N1
AI2 Unified-IO 2
CMU Act3D 3D Diffuser Actor
MT-ACT
SHU TinyVLA
A3VLM DreamVLA
SJTU Instruct2Act HumanVLA EfficientVLA
RoboDual SpecPrune-VLA Citations
Uni Freiburg HULC
HULC++
SH AI Lab SpatialVLA F1 500
ForceVLA
Inria Hiveformer
1000
KAIST LAPA
UMD TraceVLA 1500
Microsoft ShowUI
KIT MDT FLOWER 2000
HuggingFace SmolVLA
Midea DexVLA
RoboMamba MotionTrans
PKU SC-VLA HybridVLA
OmniJARVIS
ChatVLA-2
ECNU Diffusion-VLA
ScaleDP
ReLER VER
UCSD NaVILA
CAS ConRFT
GeRM
Westlake Univ. QUAR-VLA VLA-RFT
CombatVLA
Alibaba
WorldVLA
LoHoVLA
Fudan OccLLaMA
4D-VLA
Galbot GraspVLA
UChicago GRAPE
SBU LLaRA
UCLA AutoVLA
Turing CoVLA
NYU SeeDo
GEVRM
ZJU Long-VLA
Humanoid-VLA
XJTU VLAS
Skoltech Bi-VLA
Meituan RoboUniView
BUPT MoManipVLAVLA-Adapter
NUS VLA-OS
Genie Envisioner
SUTD Emma-X
CUHK RoboNurse-VLA
JHU RT-RAS
INSAIT ReVLA
VLMimic
Other BYOVLA Instruc G tV 0 LA
DP-VLA
2020 Apr Jul Oct 2021 Apr Jul Oct 2022 Apr Jul Oct 2023 Apr Jul Oct 2024 Apr Jul Oct 2025 Apr Jul Oct 2026
Figure 10: Visualization of the VLA research landscape.

53
295
Preprint NIPS ICLR ICML
290 Others RSS CVPR IROS CoRL ICRA 280 237
270
70 63
60
15 3
50 3
40 3 3 5 5 3 3 3
30 5 16
22 6
20 3 9
3
10 9 5 5 21 2 2 7 9
0
2020 2021 2022 2023 2024 2025
srepaP
fo
rebmuN
1000
100
10
0
2020 2021 2022 2023 2024 2025
(a) Papers per Year
repaP
rep
snoitatiC
Max:933
Q M 3 : : 8 8 6 9 6 9 Max:1432 Q1:833 M Q a 3 x: : 6 5 2 4 1 5 Avg:866 Min:800 Q3:758
M:470 Avg:604 Max:392
Avg:470 Q1:395 Avg:452 Q3:376
Min:320 M:314
M:223 Max:247
Q1:165
Min:137 Avg:124 Q3:122 Q1:89
M:48
Min:17 Q1:16 Max:17 Avg:11 Q3:7
Average (Avg)
Top-cited Papers
M: Median Value M:1
Q1: 25th Percentile Q3: 75th Percentile Min:0 M Q in 1 : : 0 0 Min/Max: Whiskers (1.5x IQR)
(b) Individual Paper Citations per Year
200
150
100
50
0
2020 2021 2022 2023 2024 2025
setutitsnI
tnereffiD
fo
rebmuN
243
10000
8000
6000
4000 83
2000
28
18
4
0
2020 2021 2022 2023 2024 2025
(c) Institutes per Year
snoitatiC
fo
rebmuN
9952
7869
5437
3513
1733
941
(d) Total Citations per Year
Tsinghua
SJTU 12
PKU 135 12
CAS 7 3 4
SH AI Lab 8 7 5 2
ZJU 5 3 1 1 6
Fudan 5 6 5 3 10
USTC 6 4 3 1 3 3 2
UCB 4 1 1
NUS 5 5 1 1 2 1 2 4
Stanford 1 8
NVIDIA 1 1 2 1 5 8
CUHK 1 2 8 2 1 1 1 1
BAAI 2 1 9 3 2 2
UCAS 2 1 9 2 2
Westlake Univ. 1 1 9 1
Microsoft 3 3 2 1 1 1 2 6
HKU 2 3 3 1 2 1 2 1 2
NTU 5 2 1 1 1 1 1
SII 5 1 1 5 1 1 1
NJU 2 1 1 2 3 1 3 1 1 1 4
MIT 5 3 3
Qi Zhi 9 3 2 3 2 3
HKUST(GZ) 1 1 1 4 4 1
XJTU 3 3 1 4 1 2 1 1
Galbot 1 1 6 1 2 5 2 2
SHU 1 2 1 1 1 1 1
Google 2 3 2
BUPT 4 2 1 2 3 1
SYSU 1 2 1 1 2
0
Tsinghua SJTU PK S U H C A A S I Lab ZJ F U udan USTC UCB S N t U a S nfo N r V d IDI C A UH
W
K B es A t A l U a I C ke A S M Un ic i r v o . soft HKU NTUSII NJUM H Q I K T U i Z S h T i (GZ) XJT G U albot S G HU oogle BUPT SYSU
srepaP
derahS
fo
rebmuN
(e) Collaboration Heatmap
Figure 11: Quantitative analysis of VLA development trends.

54
60
50
40
30
20
10
0
Tsinghua PK S U JTU UCB CAS Z G JU o S o t g a S le n H fo A rd I La F b ud N a V n ID U IA STC NU C S UHK BAA M C IM i W cr U e o s s t o la ft k M e I T Un U iv C . B A y S N te T D U anc Q e H i Z K h U H i S K T U ( G S Z) YS K U AISTPISII U B W UA X A JTU S X H -H U u N m JU ano B id UP G T alb B o G o t e H s o c K r h g U ia S T Tech Met X a M -E B ra ZU A A lib I ab T a o D ng e j x i m M al ide E U a C T N A U us U ti P n e M n M n La H b U X S i T ao mi H B I I T T (SZ) H T I o T yota TU M Cit C y U U U S H Y K D ( C SZ al ) te O ch ther U s I H U u C C a o w lu e m i T b e i n a cent
srepaP
fo
rebmuN
46
35
8
2 1
44
63
7 1
73
03
5 2
62
81
5 2 1
52
12
4
42
91
3 2
22
6
9
3 2
12
11
5
3 11
91
41
4 1
81
71
81
9
4
1 3 1
71
61
51
31
1
51
21
2 1
21
01
2
21
6
3 3
21
8
4
11
7
2 1
11
9
1
01
9 1
01
9
01
7
2 1
9
7 2
9
7 2
9
9
8
8
8
7
8
6 2
8
8
8
2 1 2 1
7
7
7
7
7
4 3
7
7
6
4 2
6
6
6
5
6
5
6
6
5
4 1
5
2
5
5
5
5
5
5
5
5
5
5
5
3
5
3
5
1 4 4 2 4 4 4 4 4 2 4 4 4 4 4 1 4 4 4 4 4 4 4 4 1 4 2 4 2 4 4 4 2 4
2020
2021
2022
2023
2024
2025
(a) Number of Papers per Institute
10000
8000
6000
4000
2000
0
Goo S g ta le nford UCB M N I V T ID T IA oyota Tsi P ng I hua C U ol W u mbiaER Meta C MU SJTU S U H IU O A C I X L E a T b ea m PKU Qi C Zh a i ltech M A ic I2 r U o T so B A f y t u t s e t D in ance NUS ZJ E U CN M U G id e e o a r C gi A a S T U e A ch lberta U U T n N i S F H r M e U i a b c u a rg leste C r UHK BAA U I C X A - S H E u N m S anoi U d U S W TC a S rs y a r w acus G e albot ST U U CS F D uda T W n e e le s A U tl I a C k S e P Uni U v. of C U NRS PSL IIIT-H Inr K ia AIST K C I a T U p M ita D l One HKU
snoitatiC
fo
rebmuN
79201
9291
2573
6563
149
9617
518
1792
3222
008
0765
1462
2661 008
1683
3641
1991
5723
5521 339
3113
3641
9951
2182
6242
7952
4431
5742
598 339
6702
8281
0191
0191
7251
7841
4151
1311
6931
176
9711
3311
7011
995 309 309 578 297 486 806 985 065 725 394 154 844 844 244 414 293 973 773 863 063 653 033 713 072 562 652 722 912 991 881 781 871 771 171 261 061 951 851 851 851 251 431 721 721 321
2020
2021
2022
2023
2024
2025
(b) Number of Citations per Institute
Figure 12: VLA research output and impact by institution.
