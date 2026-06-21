---
title: "CityGPT: Empowering Urban Spatial Cognition of Large Language Models"
source_pdf: "01_urban_benchmarks\\02_CityGPT_CityEval_Feng2024.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:31:10+00:00
page_count: 12
status: ok
text_char_count: 69615
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\01_urban_benchmarks\02_CityGPT_CityEval_Feng2024.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:31:10+00:00
- Page count: 12
- Status: ok
- Text chars: 69615
- Quality flags: none

## Metadata

- Title: CityGPT: Empowering Urban Spatial Cognition of Large Language Models
- Author: Jie Feng; Tianhui Liu; Yuwei Du; Siqi Guo; Yuming Lin; Yong Li
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

Large language models(LLMs), with their powerful language generation and reasoning capabilities, have already achieved notable success in many domains, e.g., math and code generation. However, they often fall short when tackling real-life geospatial tasks within urban environments. This limitation stems from a lack of physical world knowledge and relevant data during training. To address this gap, we propose CityGPT, a systematic framework designed to enhance LLMs’ understanding of urban space and improve their ability to solve the related urban tasks by integrating a city-scale ‘world model’ into the model. Firstly, we construct a diverse instruction tuning dataset, CityInstruction, for injecting urban knowledge into LLMs and effectively boosting their spatial reasoning capabilities. Using a combination of CityInstruction and open source general instruction data, we introduce a novel and easy-to-use self-weighted fine-tuning method (SWFT) to train various LLMs (including ChatGLM3-6B, Llama3-8B, and Qwen2.5-7B) to enhance their urban spatial capabilities without compromising, or even improving, their general abilities. Finally, to validate the effectiveness of our proposed framework, we develop a comprehensive text-based spatial benchmark CityEval for evaluating the performance of LLMs across a wide range of urban scenarios and geospatial tasks. Extensive evaluation results demonstrate that smaller LLMs trained with CityInstruction by SWFT method can achieve performance that is competitive with, and in some cases superior to, proprietary LLMs when assessed using CityEval. Our work highlights the potential for integrating spatial knowledge into LLMs, thereby expanding their spatial cognition abilities and applicability to the real-world physical environments. The dataset, benchmark, and source code are open-sourced and can be accessed through https://github.com/tsinghua-fib-lab/CityGPT.

## Outline

- Abstract (page 1)
- 1 Introduction (page 1)
- 2 Methods (page 2)
  - 2.1 CityInstruction Construction (page 3)
  - 2.2 SWFT: Self-Weighted Fine-Tuning (page 4)
  - 2.3 CityEval Benchmark (page 4)
- 3 Experiments (page 5)
  - 3.1 Settings (page 5)
  - 3.2 Overall Performance on CityEval (page 5)
  - 3.3 General Capabilities and Self-Weighted Fine-Tuning of CityGPT (page 6)
  - 3.4 Spatial Transferability and Downstream Task Applicability (page 7)
  - 3.5 Instruction Training Data Ablation Study (page 7)
- 4 Related Work (page 8)
- 5 Conclusion (page 9)
- References (page 9)
- A Appendix (page 10)
  - A.1 Comparison of CityEval with other Benchmarks (page 10)
  - A.2 SWFT Validation in Other Cities (page 10)
  - A.3 Effects of the LLM Size (page 10)
  - A.4 Additional Results of SimpleData (page 11)
  - A.5 Extended Results of Spatial Transferability (page 11)
  - A.6 Data Statistics (page 11)
  - A.7 Description of Urban Composite Tasks (page 11)
  - A.8 Hyper-parameter Settings (page 12)

## Markdown Content

5202
yaM
CityGPT: Empowering Urban Spatial Cognition of Large
Language Models
Jie Feng* Tianhui Liu* Yuwei Du
Department of Electronic School of Electronic and Information Department of Electronic
Engineering, BNRist, Engineering, Engineering, BNRist,
Tsinghua University Beijing Jiaotong University Tsinghua University
Beijing, China Beijing, China Beijing, China
fengj12ee@hotmail.com 21211125@bjtu.edu.cn duyw23@mails.tsinghua.edu.cn
Siqi Guo Yuming Lin Yong Li†
Department of Electronic Department of Urban Planning, Department of Electronic
Engineering, Tsinghua University Engineering, BNRist,
Tsinghua University Beijing, China Tsinghua University
Beijing, China linyuming9@mail.tsinghua.edu.cn Beijing, China
guosq21@mails.tsinghua.edu.cn liyong07@tsinghua.edu.cn

M
13
]IA.sc[
2v84931.6042:viXra
ABSTRACT
Large language models(LLMs), with their powerful language generation and reasoning capabilities, have already achieved notable
success in many domains, e.g., math and code generation. However, they often fall short when tackling real-life geospatial tasks
within urban environments. This limitation stems from a lack of
physical world knowledge and relevant data during training. To
address this gap, we propose CityGPT, a systematic framework
designed to enhance LLMs’ understanding of urban space and improve their ability to solve the related urban tasks by integrating
a city-scale ‘world model’ into the model. Firstly, we construct
a diverse instruction tuning dataset, CityInstruction, for injecting
urban knowledge into LLMs and effectively boosting their spatial
reasoning capabilities. Using a combination of CityInstruction and
open source general instruction data, we introduce a novel and
easy-to-use self-weighted fine-tuning method (SWFT) to train various LLMs (including ChatGLM3-6B, Llama3-8B, and Qwen2.5-7B)
to enhance their urban spatial capabilities without compromising, or even improving, their general abilities. Finally, to validate
the effectiveness of our proposed framework, we develop a comprehensive text-based spatial benchmark CityEval for evaluating
the performance of LLMs across a wide range of urban scenarios
and geospatial tasks. Extensive evaluation results demonstrate that
smaller LLMs trained with CityInstruction by SWFT method can
achieve performance that is competitive with, and in some cases
superior to, proprietary LLMs when assessed using CityEval. Our
work highlights the potential for integrating spatial knowledge
into LLMs, thereby expanding their spatial cognition abilities and

applicability to the real-world physical environments. The dataset,
benchmark, and source code are open-sourced and can be accessed
through https://github.com/tsinghua-fib-lab/CityGPT.
ACM Reference Format:
Jie Feng*, Tianhui Liu*, Yuwei Du, Siqi Guo, Yuming Lin, and Yong Li†. 2018.
CityGPT: Empowering Urban Spatial Cognition of Large Language Models.
In Proceedings of Make sure to enter the correct conference title from your
rights confirmation emai (Conference acronym ’XX). ACM, New York, NY,
USA, 12 pages. https://doi.org/XXXXXXX.XXXXXXX
1 INTRODUCTION
In recent years, large language models(LLMs) have made rapid
advancements across various language-based scenarios, such as
chat [6] and code generation [1]. Multiple studies [52] have shown
that LLMs exhibit powerful generalization across a wide range of
tasks and demonstrate impressive reasoning ability over complex
tasks. These developments have significantly contributed to the
progress of general artificial intelligence and have encouraged the
broader application of LLMs across diverse domains. Consequently,
various domain-specific LLMs like BloombergGPT [53] for finance,
Med-PaLM [44] for medicine and Llemma [2] for math have been
proposed and have achieved promising results.
In geography and urban science field, researchers also investigate the potential of LLMs in domain-specific tasks like geospatial
understanding and prediction tasks [5, 19, 21, 32, 34, 35, 41]. For
example, Gurnee et al. [21] investigate weather Llama2 [49] really
learns the map of the world by training linear regression probes
to predict the real location and Manvi et al. [35] design prompts
to extract geospatial knowledge from LLM for downstream prediction tasks. In the global scale or national scale, researchers find
that LLMs are good at representing the coarse location and related
geospatial knowledge like demographic indicators. However, they
also find that LLMs become struggling when the geospatial task
breaks down to the city scale, e.g., the location coordinates prediction accuracy dropped from more than 70% for cities in USA to
∗These authors contributed equally.
†Corresponding author, email: liyong07@tsinghua.edu.cn

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
general LLMs CityInstruction training Self-Weighted
Human Behavior CityInstruction Self-W
Simulation
turn left
walk 100m Base
along A road Domain
go straight Specific
Training SFT
Data
−
CityQA CityWalk CityReasoning
General
Q: Where is the Q: How to go to Q: What is the
nearest shop locaiton Y? direction of X to Y? Training
around here? A: You need to first A: While you need Data General M
A: There is a walk 100m along X to go south first, .... ,
grocery store 100 road, where you can thus X is to the Self-W
merters ahead, ... observe .... north of Y
Templates LLM Augmented lower loss weights
Figure 1: An overview of CityGPT, including CityInstructi
benchmark. CityInstruction comprises CityQA, CityWalk a
Semantics, Spatial Reasoning and Composite Tasks.
less than 30% for Point of Interests (PoIs) in New York [21]. The
results indicate that after training on the online web text, LLMs
may lack the detailed geospatial knowledge of the offline physical
world in the city. Besides, existing evaluations have deficiencies in
two aspects which greatly limits understanding the utility of LLMs
in urban space. On the one hand, most of the evaluation tasks are
based on the simple location coordinates which is just a small part
of the space, more concepts and tasks need to be validate, e.g., fundamental elements in the image of the city [31]. On the other hand,
most of the evaluation are conducted in the global scale or national
scale, limited results in the city scale are available. The question of
whether LLMs can truly be applied to solve the geospatial task in
the city scale and whether they own similar spatial cognition like
human remains unknown.
In this paper, we propose CityGPT, a systematic framework for
evaluating and enhancing the capability of LLMs on understanding
the urban space and solving the urban geospatial tasks. As the first
component of CityGPT, we construct a instruction tuning dataset
CityInstruction, which is diverse and effective for enhancing the
capability of general LLMs on understanding the urban space. We
follow the similar experience of human exploring and perceiving
the urban space in the daily life via a mobility simulator with real
map to build the dataset. Furthermore, we extend the experience
dataset by generating explicit intermediary spatial reasoning steps
for high level urban tasks which encourage the model to learn the
general reasoning paradigms in urban space. As the second component of CityGPT, we propose a robust self-weighted fine-tuning
method SWFT that automatically assesses the quality of domain
data, reweights the loss accordingly, and effectively enhances the
spatial skills of LLMs, while minimizing negative impact on their
general performance. We first train a warm-up LLM using standard
SFT with the entire CityInstruction dataset. Then, we assess the
quality of each example based on the evaluation losses of both
the base LLM and the warm-up LLM. Based on observations of
high-quality data and loss variations, we propose self-weighted
fine-tuning method, which assigns smaller learning weights in the

Jie Feng et al.
ng evaluating CityEval Benchmark CityGPT
d Tuning CityEval Benchmark
G1: City Image G2: Urban Semantics G3: Spatial Reasoning

G4: Urban Composite Tasks
Mobility Prediction Trajectory Generation Spatial Navigation
Domain Model
ed Tuning
w-quality” data
1  2  3  4 ?
1  2  3  4  5
dataset, self-weighted tuning SWFT method, and CityEval
CityReasoning, while CityEval includes City Image, Urban
loss function to ’low-quality’ data, ensuring more robust and effective knowledge learning. As the third component of CityGPT, we
build a comprehensive evaluation benchmark, CityEval, to evaluate
the capability of LLMs on various urban scenarios and downstream
tasks. Follow the experience from urban planning [31], neurocognitive science [15] and geoscience [32], the evaluation task in CityEval
is divided into four groups: City Image task group for measuring
the intuitive understanding of urban fundamental elements, Urban Semantics task group for understanding the effects of human
activities on urban environment, Spatial Reasoning task group for
high level spatial cognitive capability evaluation, Composite Task
group for evaluating the integrated capability of LLMs, which includes mobility prediction [50], behavior generation [42] and street
navigation [9] with more complicated context and instructions. In
summary, our contributions are as follows,
• To our best knowledge, CityGPT is the first systematic framework to evaluate and enhance the spatial cognition abilities of
general LLMs in the urban environment.
• We propose a mobility behavior simulation based instruction
tuning data synthesis method which could prepare high-quality
data CityInstruction for injecting urban knowledge into LLMs.
• We propose an effective fine-tuning method, self-weighted finetuning (SWFT), to enable robust and easy-to-use domain-specific
model training without compromising general capabilities.
• We propose CityEval, a comprehensive urban spatial evaluation
benchmark to accessing the performance of LLMs on urban
spatial knowledge and reasoning abilities.
• Extensive experiments on CityEval show that our method effectively enhance the spatial knowledge and capabilities of general
LLMs. After training, smaller models achieve performance comparable to or even better than top proprietary LLMs.
2 METHODS
In this paper, we propose a systematic framework to evaluate and
enhance the capability of LLMs on urban tasks and applications.
The whole framework is shown in Fig. 1, which comprises three

CityGPT: Empowering Urban Spatial Cognition of Large Language Models
central components: CityInstruction, Self-weighted Fine-Tuning, and
CityEval. We first introduce CityInstruction in Section 2.1, a dataset
designed to inject urban knowledge into general LLMs, enhancing
their ability to handle urban-related tasks. Next, in Section 2.2, we
introduce self-weighted fine-tuning, an effective and user-friendly
instruction-tuning method that enables CityGPT to be trained efficiently and robustly across diverse LLMs using mixed domain
specific data. Finally, in Section 2.3, we introduce CityEval, a benchmark designed to comprehensively evaluate LLMs on their understanding of urban spaces and ability to solve urban tasks.
2.1 CityInstruction Construction
As mentioned before, general LLMs struggle to solve the task in the
city scale due the lack of offline urban knowledge which is rare in
the online web text. A naive approach to compensate for the shortcoming is to learn the urban knowledge directly, e.g., raw map data.
However the raw map data which is designed for efficient storage
and computing is not friendly for learning. Some studies have been
done to solve this problem and efficiently ground the geospatial
information and natural language. For example, Huang et al. [23]
propose to utilize online user logs to construct heterogeneous graph
and sample random walk to construct the sequence data to train a
BERT model. However, the online user log is not public available
which make the former method disabled for the public. Besides,
GeoLM [29] use geospatial entity from the Wikipedia to align with
the same entity in open street map and validate the effectiveness
in several downstream knowledge graph task like toponym linking
and relation extraction. However, the entity recorded in the online
Wikipedia is very limited which restricts the application of this
method in the real world.
To solve this problem, we revisit the mechanisms of spatial cognition in humans. Actually, human beings perceive and recognize
the physical world through embodied experiences, often in the
form of multi-view data, during daily activities such as commuting
and wandering. Thus, we propose to simulate the human mobility
behaviors in the daily life to collect multi-view data simultaneously
as the embodied experience data for model tuning. For example, the
embodied experience data can be, "What can I observe at the current
location?", the answer may include the information of PoI, road, AoI
and so on. Based on the collected simple experience data, we first
manually design templates for each kind of data and then utilize
ChatGPT [1] with carefully designed prompts to extend these templates with more diverse formats. In this way, we obtain the diverse
multi-view experience data in the forms of instructions, including
the CityQA and CityWalk. Finally, we construct the CityReasoning dataset with intermediary steps by solving spatial reasoning
problems with manually designed solutions and ChatGPT assisted
solutions. For example, the spatial reasoning problem can be inferring the spatial orientation and distance relationships between
locations based on the navigation routing as input.
2.1.1 CityQA-Single Step Exploration. In CityQA, we define simple questions for all kinds of single entity in the urban space. The
entities considered in the dataset are PoI, AoI, road and junction of
roads. For example, we construct question about the basic information of PoI, including its category, address and coordinates, and also
relations with other nearby entities. The question of AoI is similar

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
20
15
10
5
0
1 0 1 2 3 4 5 6
Loss-WarmUp
esaB-ssoL
Figure 2: The loss of data samples before and after training,
where the dashed trend line represents the average learning
ratio, and red pentagrams highlight the anomalous region.
to the PoI. For the road and junction, only relation base questions
are considered. As mentioned before, each kind of question have at
least 3 templates which are manually defined and rewriting with
the help of ChatGPT for diversity. It is noted that due to a large
portion of addresses of entities being absent, we reconstruct the
address of them based on the road network. In this way, we can
directly link the major entities in the same urban space with the
same address representation via road network. To some extent,
this alignment method via road network based address is similar
to the entity alignment methods from [29] when LLMs are highly
skilled at recognizing and aligning similar entity [55]. Meanwhile,
proposed alignment method are easy to implement and can be
widely-used for any regions around the world.
2.1.2 CityWalk-Multi Step Exploration. CityQA covers the single
entity and its nearby relations, which can be regarded as a single
step CityWalk with random explored positions. CityWalk with a
long-term temporal and spatial window can provide us more similar
and diverse embodied experiences of urban space than human
beings. Here, following the practices from embodied agents for
house-holding [27, 54], we design two work modes to drive a data
collection agent to construct the CityWalk dataset by exploring the
urban space in the simulator. In the first mode, given a starting
point and a goal, the agent freely explores the urban space until
the goal is reached. For examples, when the agent is required to
start from its predefined home to buy some vegetables back, it can
collect potential experience data by interacting with the simulator
with APIs like search, walk, and so on. While this mode is intuitive,
it requires much more carefully designed post-processing efforts.
In second mode, we directly assign task with predefined origin and
destination to the agent which only needs to follow the fixed path
to collect multi-step data including the routing between locations
and other observations during the trip. We choose the second mode
as the default data collection mechanism when this mode works
controllably and efficiently. The first mode is only used to generate
small portion data for diversity.
2.1.3 CityReasoning-Exploration with Explicit Spatial Reasoning
Steps. Spatial reasoning problem in the urban space are not widely
studied in the existing works when most of them mainly focus on

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
the reasoning based on geographic coordinates [5, 19]. However,
geographic coordinates based reasoning is not consistent with the
mechanism of spatial cognition in humans, who usually engage in
spatial reasoning by integrating the approximate memories of visited path with rough calculations. Thus, we construct CityReasoning
dataset whose reasoning mechanism is aligned with human cognitive habits to effectively enhance the spatial reasoning capability of
LLMs. Here, we focus on most basic direction and distance based
spatial reasoning problems. Most topology related problems in our
setting can be transferred to these two questions. To construct
CityReasoning, we first random select two locations and obtain
their navigation path as context. Based on the navigation path, we
can generate the explicit reasoning steps of inferring direction and
distance and translate them with predefined templates into the
format of instruction data. For the distance reasoning problem, the
intermediate reasoning process is to perform a rough summation of
the traversed path step by step. For the direction reasoning problem,
the intermediate reasoning process is to group the movement by
the direction and then compare their values to obtain the results.
2.2 SWFT : Self-Weighted Fine-Tuning
2.2.1 General Instruction Data. Following the practice of previous works [13, 58], we mix the CityInstruction with the diverse
general instruction data during the instruction tuning stage for
reducing the risk of catastrophic forgetting of general capability.
We introduce four general datasets in our experiments, ShareGPT 1,
UltralChat [12], Open-Platypus [25] and AgentTuning [58]. Besides, we introduce geographical datasets GeoGLUE [26] to enhance
the geographical language understanding capability and language
based spatial reasoning dataset StepGame [43] and ReSQ [37] for
enhancing the qualitative spatial reasoning capability of CityGPT
via language. While GeoGLUE does not follow the instruction format, we design simple templates to convert the data. We also utilize
GPT-4 as the automatic data annotator and data quality evaluator
to generate intermediate reasoning steps of StepGame and ReSQ to
reduce the learning difficulty of small LLMs.
2.2.2 Self-Weighted Fine-Tuning. Even when mixed with general
data, the trained model still performs poorly to some extent, exhibiting a decline in general capabilities and a degradation in domainspecific performance. To investigate this issue, as shown in Figure 2,
we analyzed the loss of CityInstruction data samples before and after
training and identified a subset of anomalous data points, highlighted as red pentagrams in the figure. These data points have an
exceptionally high loss on the base model (e.g., Llama3-8B, 𝑀 𝑏𝑎𝑠𝑒 ),
indicating that they are either of poor quality or introduce entirely
new knowledge that significantly deviates from the base model’s
prior distribution. Furthermore, after training, the loss reduction
for these data points remains smaller than the average reduction
observed across the entire dataset (as indicated by the dashed trend
line). This confirms that these data points are indeed of ’low quality’
and difficult for the model to learn from, potentially harming overall performance. Thus, based on these observations, we propose the
self-weighted fine-tuning (SWFT) method, which leverages learning
dynamics to generate personalized weights for each data sample
1https://huggingface.co/datasets/shareAI/ShareGPT-Chinese-English-90k

Jie Feng et al.
P
50
G eneration
re
d
ic
tio
n
50
1
5 0 0 8
B o u n d a r y
4 0 D i r e c t i o n 4
0 5 1
404
urrounding
200
S
5 0 5 0
0
0 1
5 0 1 0 0
e
d
o N ark
ask
L
andm
N avigation p o site T C ity R oad
C
o m Im
a
S g
p a C i t y E v a l e
tia l R
e
a
D
istance
s o
n in g U rb a n S e
F
m a n tic s
T
ype
D istrict
u n
c
tio
n
Figure 3: Composition of CityEval.
using a function 𝑓 , thereby adaptively adjusting sample-specific
weights 𝑤 in the loss function. Specifically, the loss function L𝑠𝑤𝑓 𝑡
of proposed SWFT for model 𝑀 is formulated as follows,
𝑁 𝑇
1 ∑︁ ∑︁
L swft (𝑀) = − 𝑁 𝑤 𝑖 log 𝑃 𝑀 (𝑦 𝑡 |𝑥, 𝑦 <𝑡 ),
𝑖=1 𝑡=1
𝑤 𝑖 = 𝑓 (L𝑖 (𝑀 base ), L𝑖 (𝑀 warm )),
|L(𝑀 ) − L(𝑀 )|
𝑓 𝑒𝑥𝑝 = warm base ,
∥L(𝑀 )∥
base 2
where 𝑓 𝑒𝑥𝑝 denotes an representative function 𝑓 by considering the
trend in the observation, 𝑥 is the input token, 𝑇 is the token length
of data instance 𝑖, 𝑦 𝑡 is the next token, 𝑁 is the number of data
samples, L denotes the normal cross entropy loss. According to the
above formula, "low-quality" data—characterized by a large initial
loss and minimal loss reduction—will automatically be assigned
lower weights during tuning, as determined by the base LLM 𝑀 𝑏𝑎𝑠𝑒
and the warm-up trained LLMs 𝑀 𝑤𝑎𝑟𝑚. This allows the model to
effectively focus more on well-matched, high-quality data, leading
to improved and more robust performance. We believe 𝑓 𝑒𝑥𝑝 is not
the only possible weighting function. Here, we define 𝑓 𝑒𝑥𝑝 in the
simplest form due to the limitation of computation.
2.3 CityEval Benchmark
Different form existing works [21, 32, 41] which mainly focus on
evaluation on the global scale or national scale, we propose a systematic evaluation benchmark CityEval to testify the capability
of LLMs in urban space. Following the common experiences from
different fields [15, 31, 32], as Fig. 3 shows, our benchmark contains
four sub-modules with emphasizing different aspects of spatial cognition of human and applications of urban science, including City
Image, Urban Semantics, Spatial Reasoning and Composite Tasks.

CityGPT: Empowering Urban Spatial Cognition of Large Language Models
2.3.1 City Image-Fundamental Elements of The City In the Mind.
Lynch [31] explored the mechanism of human perceiving and remembering the urban environments and found that human usually
deconstruct urban space into a combination of five fundamental elements: paths, edges, districts, nodes, and landmarks in their mind.
Similar concepts and mechanism are also verified by the neurocognitive science [15]. Based on these observations, we propose the
City Image task group to evaluate whether LLMs can understand
these concepts and solve the related questions. In City Image, we
manually design various questions for each element, e.g., attributes
and underlying relations. For example, while people use path in the
mind to remember how to arrive different locations, one typical
question for it is "Do you know the origin and destination junction
of Nanyuan road?" It is noted that this question dose not exist in
the instruction tuning data directly, model needs to learn from the
experiences in CityWalk and answer this question by organizing its
memory about all the possible junctions of Nanyuan road. Another
example is about the concept of boundary. While roads usually play
the role of separating different areas in the city, we design the question like "Which of the following roads serve as the boundaries of
region X?" to confirm weather the model understands the concept
of boundary in the urban space. In summary, we design 12 types of
questions for 5 fundamental elements to construct the City Image.
2.3.2 Urban Semantics-Human Activities and Urban Environment.
Different from the City Image, Urban Semantics pay attention to the
human activities happened in the urban environment and evaluate
the capacity of understanding the urban functions. The understanding and prediction of urban functions is the fundamental task of
geoscience [32] and urban science [57]. In simple terms, we define
the task of Urban Semantics as inferring the functions of areas with
knowing the PoI distribution and the most likely missing PoIs in
the environment. For example, the question about inferring the
functions of areas can be "There are PoI A, PoI B, ..., PoI G in the
area Y, what is the potential function of area Y?". In summary, we
design 6 types of questions to construct the Urban Semantics.
2.3.3 Spatial Reasoning-Reasoning in Urban Space. Compared with
the former two tasks which require more about the capacity of
memorization and association analysis, we introduce Space Reasoning task group to evaluate the capacity of quantitative reasoning
and spatial cognition which is more challenging for LLMs. The design of Spatial Reasoning is similar to the methods in Section 2.1.3
CityReasoning. Here, we set two testing scenarios for the spatial
reasoning evaluation. The first testing scenario is whether the question contains the necessary context for spatial reasoning. When no
necessary context is provided, model needs to reasoning over its
memory which is a more challenging process. The second testing
scenario is whether the urban space of reasoning has been saw by
the model in the training. Besides, when evaluating models trained
by CityReasoning introduced before, we carefully check the evaluation data to prevent the potential data leakage. In summary, we
design 20 types of questions for Spatial Reasoning.
2.3.4 Urban Composite Tasks-Solving Realistic Urban Tasks. Finally,
we introduce the Composite Tasks group which consists of mobility
prediction [50], trajectory generation [42] and spatial navigation [9]
for assessing the integration capability of LLMs in urban space. All

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
60
40
20
0
City Image Urban Semantics Spatial Reasoning
Task
)%(
ycaruccA
ChatGLM3-6B
CityGPT-6B
Qwen2.5-7B
CityGPT-7B
LLama3-8B
CityGPT-8B
Figure 4: The performance of CityGPT@Beijing consistently
exceeds that of the baseline across various base models on
CityEval benchmark.
these tasks require diverse capability of LLMs to understand the
urban environments and human behavior to complete. Detailed
introduction of these tasks can refer to the appendix.
3 EXPERIMENTS
3.1 Settings
3.1.1 General Evaluation Tasks. In addition to the proposed CityEval benchmark, we also evaluate our model using general benchmarks, including MMLU [22] to assess general knowledge abilities,
GSM8K [7] to evaluate mathematical abilities, and BBH [45] to
evaluate common sense reasoning abilities.
3.1.2 Evaluation Metrics. For general evaluation tasks including
MMLU, BBH and GSM8K, we use opencompass [8] with default
generation settings as the evaluation tool to calculate the score. For
the first three types of tasks in CityEval, the questions are organized
as single-choice questions with at least 4 choices (up to 10 choices )
and accuracy is chosen as metric. For the last composite application
tasks in CityEval, we provide all the models with 1-shot example
and use their common practices to define metrics.
3.1.3 Evaluation Cities. We choose Beijing, London, NewYork and
Paris and perform the experiments across the entire geographical
areas of these cities. To conduct the out-of-domain validation, SanFrancisco does not participate in the evaluation but only generates
task instruction data for other cities.
3.1.4 LLM Baselines. We consider the following baselines and divide them into 3 groups: small open source LLMs group with about
7B parameters including ChatGLM3-6B [59], Qwen2.5-7B [48],
Llama3-8B [36] and Gemma2-9B [46], large open source LLMs
group with about 100B parameters including Mistral-Small-24B [47],
Gemma2-27B [46], Qwen2.5-32B [48], LLama3.1-70B [14], Qwen2.572B [48] and LLama3.1-405B [14], and commercial APIs group including GPT-3.5 and GPT-4omini [1]. For open source LLMs, we
deploy them with the help of vllm [24]. The max output token are
set to 500, the repetition penalty is set to 1.0, the temperature is set
as 0, and it is changed to 1.0 when needing sample answers.
3.2 Overall Performance on CityEval
The main results of CityGPT on four cities are presented in Table 1.
Here, we use Qwen2.5-7B as the start point and use the proposed
CityInstruction to obtain the final model CityGPT-7B. It is noted
that we only report the performance of top 3 tasks in CityEval

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Table 1: Main results on CityEval. CityGPT-7B significantly o
‘US’ denotes urban semantics, and ‘SR’ denotes spatial reason
City Beijing Lond
Tasks CI↑ US↑ SR↑ CI↑ US
ChatGLM3-6B 0.300 0.477 0.248 0.269 0.45
Qwen2.5-7B 0.325 0.587 0.164 0.303 0.48
LLama3-8B 0.286 0.520 0.285 0.312 0.49
Gemma2-9B 0.097 0.207 0.159 0.168 0.22
Mistral-Small-24B 0.288 0.587 0.293 0.315 0.54
Gemma2-27B 0.326 0.573 0.225 0.363 0.52
Qwen2.5-32B 0.400 0.627 0.405 0.360 0.54
LLama3.1-70B 0.357 0.570 0.338 0.372 0.54
Qwen2.5-72B 0.408 0.607 0.293 0.345 0.55
LLama3.1-405B 0.417 0.587 0.414 0.451 0.59
GPT-3.5 0.269 0.553 0.249 0.297 0.51
GPT-4omini 0.319 0.533 0.246 0.386 0.51
CityGPT-Qwen2.5-7B 0.502 0.620 0.552 0.525 0.59
vs. Qwen2.5-7B +54.50% +5.68% +236.59% +73.08% +24.3
vs. Best Baseline +20.29% -1.07% +33.33% +16.37% +0.57
whose metrics is the accuracy. Results on the final composite task
are presented in section 3.4.
We first analyze the results from Beijing. In the first 7B parameter group, we find that more advanced LLMs can achieve better
performance in all the tasks, e.g., LLama3-8B outperforms the older
ChatGLM3-6B around 23% in City Image task. It is worth noting
that the newer Gemma2-9B unexpectedly shows the weakest performance. We speculate that this is due to the distribution of its
training data, which makes it unsuitable for urban-related tasks.
Performance of larger parameter group (about 100B) continues to
outperforms than small parameter group about 0.69%-330%, with
the largest open source model LLama3.1-405B achieving the best
performance in 2 tasks, even surpassing the GPT series. The results
demonstrate the effectiveness of proposed evaluation benchmark
CityEval. Meanwhile, we notice that there is great potential for
overall improvement in the benchmark when the best performance
among all the task is only 0.627. Overall, CityGPT-Qwen2.5-7B
exhibits significant improvement over all baselines in most of tasks.
Compared with the best baseline, the performance gain of CityGPT7B is 33.33% in the challenging Spatial Reasoning task. And it outperforms its original version Qwen2.5-7B with at least 5.68% in
the urban semantic task and 236.59% in the spatial reasoning tasks.
These results present the effectiveness of proposed instruction tuning dataset CityInstruction which successfully teach the small LLMs
with various capabilities in the urban space and achieve outstanding performance than all the powerful general LLMs including the
commercial API.
The results from London, New York, and Paris are similar to those
from Beijing. LLama3.1-405B is generally the best-performing baseline and even surpasses CityGPT-7B in the City Image task in Paris.
However, apart from this, our CityGPT-7B outperforms all other
models across all tasks. As shown in the Figure 4, this illustrates
the performance of different base models(including ChatGLM3-6B,
Qwen2.5-7B and LLama3-8B) on CityEval after being trained with
CityInstruction in Beijing. All CityGPT models outperform the base

Jie Feng et al.
erforms than baselines in most tasks. ‘CI’ denotes city image,
in CityEval benchmark.
NewYork Paris
SR↑ CI↑ US↑ SR↑ CI↑ US↑ SR↑
0.241 0.315 0.430 0.254 0.291 0.383 0.263
0.256 0.311 0.503 0.256 0.277 0.483 0.232
0.282 0.331 0.503 0.277 0.265 0.463 0.281
0.214 0.168 0.197 0.209 0.162 0.197 0.191
0.339 0.332 0.580 0.317 0.342 0.493 0.320
0.245 0.346 0.557 0.238 0.372 0.490 0.235
0.419 0.383 0.543 0.390 0.337 0.503 0.391
0.393 0.412 0.597 0.377 0.388 0.473 0.377
0.363 0.417 0.577 0.319 0.346 0.453 0.336
0.484 0.400 0.580 0.424 0.457 0.513 0.467
0.272 0.354 0.490 0.239 0.299 0.473 0.275
0.308 0.369 0.523 0.291 0.369 0.503 0.293
0.603 0.485 0.607 0.585 0.439 0.527 0.619
+135.55% +55.92% +20.54% +128.52% +58.36% +8.98% +166.81%
+24.59% +16.24% +1.68% +37.97% -4.03% +2.61% +32.55%
models across all tasks. This performance gap is particularly evident
in the most challenging Spatial Reasoning Task, where CityGPT
achieves 148% to 237% higher accuracy compared to the base models.
In summary, proposed evaluation benchmark CityEval effectively
distinguishes the diverse capabilities of different LLMs in understanding urban space, and CityInstruction can be used to effectively
improve the performance of smaller LLMs in urban capabilities.
3.3 General Capabilities and Self-Weighted
Fine-Tuning of CityGPT
In this section, we first evaluate the performance of CityGPT in
general benchmark. Table 2 presents the performance of CityGPT
trained on different base models, which indicates that CityGPT
models are generally comparable to the base models in terms of
general capabilities. CityGPT-Qwen2.5-7B shows improvements on
MMLU and BBH, while maintaining similar performance on GSM8K.
However, there are notable decreases on MMLU and GSM8K with
CityGPT-LLama3-8B, a decline is also observed on BBH with CityGPTChatGLM-6B. Therefore, we propose a Self-Weighted Fine-Tuning
approach to address these issues.
Table 2: The performance of CityGPT@Beijing on general
benchmarks is comparable to that of the baseline.
General Benchmark MMLU GSM8K BBH
Qwen2.5-7B 74.15 80.21 66.01
CityGPT-Qwen2.5-7B 74.72↑ 77.18≈ 70.03↑
LLama3-8B 68.33 79.38 52.88
CityGPT-LLama3-8B 56.89 60.58 53.92↑
ChatGLM3-6B 51.97 57.47 34.35
CityGPT-ChatGLM3-6B 52.03↑ 56.79≈ 27.51
We conduct exploratory experiments on SWFT using LLama3-8B,
which experiences the largest decline in general capabilities. As

CityGPT: Empowering Urban Spatial Cognition of Large Language Models
1.2
1.0
0.8
0.6
0.4
0.2
0.0
0 5 10 15
Loss
ytisneD
Base-LLama3 80
SFT-CityGPT
SWFT-CityGPT 70
60
50
40
30
CI US SR MMLU GSM8K BBH
(a) Loss on the training data.
)%(
)erocS(
ycaruccA
Base-LLama3
SFT-CityGPT
SWFT-CityGPT
(b) Performance of models@London.
Figure 5: Effectiveness of proposed self-weighted tuning.
Figure 5(a) shows, the loss range of SFT-CityGPT is significantly
narrower than that of the base model, indicating the effectiveness
of the fine-tuning process. Notably, the loss for SWFT-CityGPT
is larger due to the application of the weighted 𝑓 𝑒𝑥𝑝 function in
the loss calculation. From Figure 5(b), we can observe that SWFTCityGPT significantly improves performance over CityGPT-SFT on
both CityEval and general benchmark, with gains ranging from 0.8%
to 27%, demonstrating the effectiveness of the proposed SWFT approach. However, it is also evident that CityGPT-SWFT still shows a
decrease on the GSM8K task compared to the Base-LLama3 model.
This result indicates that while our training strategy helps the
model retain its general capabilities on simpler tasks, further improvements are needed for it to sustain comparable performance
on more challenging benchmarks.
In summary, after tuning on CityInstruction with SWFT method,
CityGPT demonstrates stronger urban knowledge and task-solving
ability while preserving general capabilities.
3.4 Spatial Transferability and Downstream
Task Applicability
In this section, we evaluate the transferability of the spatial knowledge and reasoning ability of CityGPT. As Table 3 shows, we divide the results of spatial reasoning into with-context and withoutcontext two groups where each group has 20 questions. Regardless
of the base model used, CityGPT@Beijing trained by data from
Beijing outperforms the base model significantly in the CityEval
of other three different cities. The outstanding performance of
CityGPT in out-of-domain regions demonstrate that CityGPT indeed learns the general spatial cognition knowledge of urban space
which can be transferred between cities. For all models, the performance in the without-context setting is worse than that in the
with-context setting, indicating that while CityInstruction has enhanced the model’s urban space capabilities, there is still room for
improvement in handling reasoning tasks.
The result of downstream Urban Composite Tasks group is presented in Table 4. CityGPT, acquiring urban spatial knowledge and
the skill of spatial reasoning after tuning with CityInstruction, outperforms ChatGLM3-6B significantly in all three tasks, including
the mobility prediction, trajectory generation and street navigation.
It is noted that no task related instruction data is collected and used
to train the model during the whole experiment. In the mobility
prediction task, the performance of Llama3-70B is competitive with

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
70
60
50
40
30
20
10
0
0% 20% 40% 60% 80% 100%
)%(
ycaruccA
City Image Spatial Reasoning(with context)
Urban Semantics Spatial Reasoning(w/o context)
Figure 6: The performance of CityGPT improves as the volume of the instruction dataset increases.
CityGPT. Due to the periodical characteristics of human mobility, Llama3-70B with powerful reasoning capability can observe
this regularity and give proper location prediction results by only
considering the locations exists in the past trajectory. The results
demonstrate that when the model is trained with knowledge-based
QA and navigation tasks, it learns the local knowledge of the urban
space from the QA and the mobility patterns of the population
from navigation instructions. Both of these are valuable for various downstream tasks. While this may not directly enhance the
model’s personalized capabilities for tasks like mobility prediction
and trajectory generation, a deeper understanding of urban spaces
and context can still improve its performance on these tasks.
3.5 Instruction Training Data Ablation Study
In this section, we study the influence of the data composition in
CityInstruction in Figure 6, Figure 7, and Table 5. To study the effects
of data size, we split the whole CityInstruction into five equal parts
and fine-tune Qwen2.5-7B with data from only 1 part to all the 5
parts. As Figure 6 shows, the performance of all the tasks increase
with more data are utilized. We find that Urban Semantics task
group requires only a modest amount of data to achieve a relatively
high level of performance, whereas the more challenging Spatial
Reasoning task necessitates significantly larger quantities of data
to attain a comparable high level of performance.
Besides, we compare our CityInstruction with the simple tuning data to demonstrate the effectiveness of data construction in
our framework. As shown in Table 5, without carefully designed
instruction-tuning data, simple fine-tuning on naive static urban
knowledge does not enable LLMs to effectively understand the urban space. In the table, all the models utilize standard SFT, with
the only difference being the training data. "SimpleData" refers to
the direct conversion of geospatial data into conversational format
for training the LLM, while "SimpleData2" indicates the mixing
of SimpleData with the same general text instruction data used in
CityGPT. Our findings show that CityGPT, when trained with carefully designed instruction data, outperforms LLMs trained solely
on simple geospatial data. Although learning from the simple data
provides some performance improvements in certain cases, it can
also negatively impact the LLM in others.
Furthermore, we discuss the effects of different types of data in
CityInstruction and present the results in Figure 7. All Data’ yields
the best performance, showing that single datasets are insufficient
and mixing multiple datasets is key to superior results.

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Table 3: The performance of CityGPT, trained using data fr
‘with context’ denotes spatial reasoning with context, ‘w/o co
Testing@London
Model
CI↑ US↑ with context↑ w/o context↑ CI↑ U
Qwen2.5-7B 0.303 0.480 0.270 0.242 0.311 0.
Training@Beijing 0.511 0.633 0.752 0.324 0.483 0.
LLama3-8B 0.312 0.490 0.362 0.202 0.331 0.
Training@Beijing 0.565 0.653 0.828 0.598 0.543 0.
ChatGLM3-6B 0.269 0.450 0.246 0.236 0.315 0.
Training@Beijing 0.531 0.647 0.814 0.536 0.486 0.
Table 4: CityGPT-ChatGLM3-6B performs well on Composite
bold denotes the best results, underline denotes the second b
Tasks@Beijing-Wudaokou Mobility Prediction
Acc(multi) ↑ Acc(gen) ↑
ChatGLM3-6B 0.25 0.12
CityGPT-ChatGLM3-6B 0.52 0.46
Llama3-70B 0.45 0.50
Table 5: Comparison of our data with SimpleData.
Model@Beijing CI US SR
LLama3-8B 0.286 0.520 0.285
LLama3-8B-SimpleData 0.219 0.480 0.191
LLama3-8B-SimpleData2 0.259 0.467 0.260
CityGPT-8B-OurData 0.554 0.680 0.708
80
60
40
20
0
City Image Urban Semantics Spatial Reasoning Spatial Reasoning
(with context) (w/o context)
)%(
ycaruccA
Base +QA+Task +QA+Task+Reasoning+Walk
+QA +QA+Task+Reasoning All Data
Figure 7: The performance of CityGPT increases when different sub-datasets are added, where ‘base’ denotes the base
model, ‘+’ denotes the model is trained on added dataset,
‘Task’ denotes task instruction data.
Finally, we present the in-context learning (5-shot) results for
three representative baselines—LLama3.1-405B and LLama3-8B—in
Beijing in the Table 6. As shown in the table, compared to the zeroshot setting, the performance of the baselines in the 5-shot setting
exhibits varying degrees of improvement, ranging from 8% to 15%.
This highlights the importance of providing examples to help LLMs
become familiar with the task paradigm and instructions. However,
despite the performance gains in the 5-shot setting, these baselines

Jie Feng et al.
Beijing, in three another cities: London, NewYork and Paris.
xt’ denotes spatial reasoning without context in CityEval.
sting@NewYork Testing@Paris
with context↑ w/o context↑ CI↑ US↑ with context↑ w/o context↑
0.262 0.250 0.277 0.483 0.254 0.210
0.780 0.354 0.468 0.650 0.764 0.374
0.358 0.196 0.265 0.463 0.366 0.196
0.788 0.570 0.534 0.650 0.836 0.608
0.258 0.250 0.291 0.383 0.264 0.262
0.784 0.532 0.509 0.563 0.782 0.548
sk without any further task-related fine-tuning. In the table,
results.
Trajectory Generation Spatial Navigation
dius(JSD) ↓ Distance(JSD) ↓ Steps ↓ Success Rate ↑
0.473 0.416 20.83 0.35
0.451 0.380 15.32 0.55
0.455 0.389 18.95 0.44
Table 6: Performance of CityGPT with zero-shot settings and
general LLMs with few-shot settings in CityEval.
Model@Beijing CI US SR
LLama3.1-405B-zeroshot 0.417 0.587 0.414
LLama3.1-405B-5shot 0.451 0.663 0.468
LLama3-8B-zeroshot 0.286 0.520 0.285
LLama3-8B-5shot 0.330 0.566 0.262
CityGPT-8B 0.554 0.680 0.708
still lag behind CityGPT in the zero-shot setting in the vast majority
of cases. We also provide the results of Qwen in appendix.
4 RELATED WORK
Large Language Models. Since the publication of ChatGPT [39],
LLMs [61] presents impressive language generation and reasoning
capabilities in many challenging tasks [1, 18]. While LLMs [49, 59]
are trained on the massive online web text data, they usually underperform in many specialized fields of real-life. Thus, researchers
design various mechanisms to enhance the capability of general
LLMs in specific domains, like BloombergGPT [53] , Med-Plam [44],
and Llemma [2]. In the geospatial field, K2 [10] is designed to answer geographical knowledge questions after learning scientific
literature. Similar to K2, Wang et al. [51] finetune ChatGLM to answer questions about urban renewal. Different from these domain
specific QA models for text based literature, our method is designed
for understanding physical urban space whose original format is
not text and conducting spatial reasoning to solve real urban tasks.
Language and Urban Space. While urban space is usually described by the accurate digital map, researchers have explored
various methods [4, 11, 17, 18, 23, 28–30] to grounding the natural
language with the geospatial entity. Huang et al. [23] propose utilize

CityGPT: Empowering Urban Spatial Cognition of Large Language Models
online user searching logs to construct heterogeneous graph and
sample random walks to construct the sequence data with geospatial entity. Li et al. [28, 29] use geospatial entity from the Wikipedia
to align with the same entity in map. However, the former relies
on the large scale private user logs and the latter can only cover
limited entities mentioned in the Wikipedia. Recently, Balsebre et
al. [4] propose LAMP to injecting PoIs into LLMs with RAG for
better PoI recommendation, which is similar to part of the questions
about PoIs in our CityQA. Unlike LAMP, our method considers a
broader range of questions and entities by drawing inspiration from
GeoQA [33, 40] and we introduce routing based instruction data
and spatial reasoning instructions as new ways to grounding the
urban spatial knowledge with language.
Spatial Cognition and Reasoning. With explicit function zones
in the brain like place cells and border cells, human build a cognitive map [15, 16] in the mind to recognize the physical world and
navigate in it. Following this concept, researchers try to evaluate
the spatial reasoning and navigation capability of LLMs in abstract
environments [38, 56, 60]. However, their experiment are conducted
in the idealized and non-realistic environments like grids which is
far from the real-life urban space. Besides, many studies [21, 41]
propose to evaluate the spatial knowledge of LLMs. However, most
of them pay attention to the coordinates based problems and only
conduct national scale evaluations. In this paper, we follow the
concept of the image of the city [31] and spatial cognitive map to
construct the CityEval benchmark. As the first systematic evaluation benchmark for urban spatial capability of LLMs, it covers
diverse aspects of urban space and sheds light for effectively evaluating the intelligence and utility of LLMs for urban system.
5 CONCLUSION
In this paper, we propose a systematic framework for evaluating
and enhancing the capability of LLMs on understanding urban
space and solving related urban tasks. For effectively evaluating the
capability of LLMs, we construct CityEval which comprehensively
considering various aspects of urban space. To enhance the capability of smaller LLMs, we construct a diverse instruction tuning
dataset CityInstruction with human-like spatial experience data and
enhanced spatial reasoning problem data via simulation. Finally, we
propose a self-weighted fine-tuning method that incorporates data
quality into the loss function to mitigate the forgetting problem
while enhancing the domain-specific capabilities of LLMs. This
approach enables robust and stable learning using ordinary data
without the need for costly, meticulous filtering, ensuring resilience
against the influence of noisy data. In the future, we plan to validate
the framework in more cities around the world to further demonstrate its effectiveness. We will also explore adding data from other
modalities, such as remote sensing and street view images, to further enhance the capability of foundation models.
REFERENCES
[1] Josh Achiam, Steven Adler, Sandhini Agarwal, and et al. 2023. Gpt-4 technical
report. arXiv preprint arXiv:2303.08774 (2023).
[2] Zhangir Azerbayev, Hailey Schoelkopf, Keiran Paster, and et al. 2023. Llemma:
An open language model for mathematics. arXiv preprint arXiv:2310.10631 (2023).
[3] Jinze Bai, Shuai Bai, Yunfei Chu, and et al. 2023. Qwen Technical Report. arXiv
preprint arXiv:2309.16609 (2023).
[4] Pasquale Balsebre, Weiming Huang, and Gao Cong. 2024. LAMP: A Language
Model on the Map. arXiv preprint arXiv:2403.09059 (2024).

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
[5] Prabin Bhandari, Antonios Anastasopoulos, and Dieter Pfoser. 2023. Are large
language models geospatially knowledgeable?. In Proceedings of the 31st ACM
International Conference on Advances in Geographic Information Systems. 1–4.
[6] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan,
Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. 2020. Language models are few-shot learners. Advances in neural
information processing systems 33 (2020), 1877–1901.
[7] Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian, Mark Chen, Heewoo Jun,
Lukasz Kaiser, Matthias Plappert, Jerry Tworek, Jacob Hilton, Reiichiro Nakano,
et al. 2021. Training verifiers to solve math word problems. arXiv preprint
arXiv:2110.14168 (2021).
[8] OpenCompass Contributors. 2023. OpenCompass: A Universal Evaluation Platform for Foundation Models. https://github.com/open-compass/opencompass.
[9] Antoine Coutrot, Ed Manley, Sarah Goodroe, Christoffer Gahnstrom, Gabriele
Filomena, Demet Yesiltepe, Ruth Conroy Dalton, Jan M Wiener, Christoph
Hölscher, Michael Hornberger, et al. 2022. Entropy of city street networks
linked to future spatial navigation ability. Nature 604, 7904 (2022), 104–110.
[10] Cheng Deng, Tianhang Zhang, Zhongmou He, Qiyuan Chen, Yuanyuan Shi, Yi
Xu, Luoyi Fu, Weinan Zhang, Xinbing Wang, Chenghu Zhou, et al. 2024. K2:
A foundation language model for geoscience knowledge understanding and
utilization. In Proceedings of the 17th ACM International Conference on Web Search
and Data Mining. 161–170.
[11] Jingtao Ding, Yunke Zhang, Yu Shang, Yuheng Zhang, Zefang Zong, Jie Feng,
Yuan Yuan, Hongyuan Su, Nian Li, Nicholas Sukiennik, et al. 2024. Understanding
World or Predicting Future? A Comprehensive Survey of World Models. arXiv
preprint arXiv:2411.14499 (2024).
[12] Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan
Liu, Maosong Sun, and Bowen Zhou. 2023. Enhancing chat language models by
scaling high-quality instructional conversations. arXiv:2305.14233 (2023).
[13] Guanting Dong, Hongyi Yuan, Keming Lu, Chengpeng Li, Mingfeng Xue, Dayiheng Liu, Wei Wang, Zheng Yuan, Chang Zhou, and Jingren Zhou. 2023. How
abilities in large language models are affected by supervised fine-tuning data
composition. arXiv preprint arXiv:2310.05492 (2023).
[14] Abhimanyu Dubey, Abhinav Jauhri, et al. 2024. The Llama 3 Herd of Models. ArXiv abs/2407.21783 (2024). https://api.semanticscholar.org/CorpusID:
271571434
[15] Russell A Epstein, Eva Zita Patai, Joshua B Julian, and Hugo J Spiers. 2017. The
cognitive map in humans: spatial navigation and beyond. Nature neuroscience 20,
11 (2017), 1504–1513.
[16] Delaram Farzanfar, Hugo J Spiers, Morris Moscovitch, and R Shayna Rosenbaum.
2023. From cognitive maps to spatial schemas. Nature Reviews Neuroscience 24, 2
(2023), 63–79.
[17] Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. 2025. AgentMove: A large language
model based agentic framework for zero-shot next location prediction. In NAACL.
[18] Jie Feng, Jinwei Zeng, Qingyue Long, Hongyi Chen, Jie Zhao, Yanxin Xi, Zhilun
Zhou, Yuan Yuan, Shengyuan Wang, Qingbin Zeng, et al. 2025. A Survey of
Large Language Model-Powered Spatial Intelligence Across Scales: Advances in
Embodied Agents, Smart Cities, and Earth Science. arXiv:2504.09848 (2025).
[19] Nathan Godey, Éric de la Clergerie, and Benoît Sagot. 2024. On the Scaling Laws
of Geographical Representation in Language Models. arXiv:2402.19406 (2024).
[20] Sylvain Gugger, Lysandre Debut, Thomas Wolf, Philipp Schmid, Zachary Mueller,
Sourab Mangrulkar, Marc Sun, and Benjamin Bossan. 2022. Accelerate: Training
and inference at scale made simple, efficient and adaptable. https://github.com/
huggingface/accelerate.
[21] Wes Gurnee and Max Tegmark. 2023. Language models represent space and time.
arXiv preprint arXiv:2310.02207 (2023).
[22] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn
Song, and Jacob Steinhardt. 2020. Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300 (2020).
[23] Jizhou Huang, Haifeng Wang, Yibo Sun, Yunsheng Shi, Zhengjie Huang, An
Zhuo, and Shikun Feng. 2022. ERNIE-GeoL: A Geography-and-Language Pretrained Model and its Applications in Baidu Maps. In Proceedings of the 28th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining. 3029–3039.
[24] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng,
Cody Hao Yu, Joseph Gonzalez, Hao Zhang, and Ion Stoica. 2023. Efficient
memory management for large language model serving with pagedattention. In
Proceedings of the 29th Symposium on Operating Systems Principles. 611–626.
[25] Ariel N Lee, Cole J Hunter, and Nataniel Ruiz. 2023. Platypus: Quick, cheap, and
powerful refinement of llms. arXiv preprint arXiv:2308.07317 (2023).
[26] Dongyang Li, Ruixue Ding, Qiang Zhang, Zheng Li, Boli Chen, Pengjun Xie, Yao
Xu, Xin Li, Ning Guo, Fei Huang, et al. 2023. Geoglue: A geographic language
understanding evaluation benchmark. arXiv preprint arXiv:2305.06545 (2023).
[27] Shuang Li, Xavier Puig, Chris Paxton, Yilun Du, Clinton Wang, Linxi Fan, Tao
Chen, De-An Huang, Ekin Akyürek, Anima Anandkumar, et al. 2022. Pre-trained
language models for interactive decision-making. Advances in Neural Information
Processing Systems 35 (2022), 31199–31212.
[28] Zekun Li, Jina Kim, Yao-Yi Chiang, and Muhao Chen. 2022. SpaBERT: A Pretrained
Language Model from Geographic Data for Geo-Entity Representation. arXiv

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
preprint arXiv:2210.12213 (2022).
[29] Zekun Li, Wenxuan Zhou, Yao-Yi Chiang, and Muhao Chen. 2023. Geolm: Empowering language models for geospatially grounded language understanding.
arXiv preprint arXiv:2310.14478 (2023).
[30] Yu Liu, Jingtao Ding, Yanjie Fu, and Yong Li. 2023. Urbankg: An urban knowledge
graph system. ACM Transactions on Intelligent Systems and Technology 14, 4
(2023), 1–25.
[31] Kevin Lynch. 1964. The image of the city. MIT press.
[32] Gengchen Mai, Weiming Huang, Jin Sun, Suhang Song, Deepak Mishra, Ninghao
Liu, Song Gao, Tianming Liu, Gao Cong, Yingjie Hu, et al. 2023. On the opportunities and challenges of foundation models for geospatial artificial intelligence.
arXiv preprint arXiv:2304.06798 (2023).
[33] Gengchen Mai, Krzysztof Janowicz, Rui Zhu, Ling Cai, and Ni Lao. 2021. Geographic question answering: challenges, uniqueness, classification, and future
directions. AGILE: GIScience series 2 (2021), 8.
[34] Rohin Manvi, Samar Khanna, Marshall Burke, David Lobell, and Stefano Ermon. 2024. Large language models are geographically biased. arXiv preprint
arXiv:2402.02680 (2024).
[35] Rohin Manvi, Samar Khanna, Gengchen Mai, Marshall Burke, David Lobell,
and Stefano Ermon. 2023. Geollm: Extracting geospatial knowledge from large
language models. arXiv preprint arXiv:2310.06213 (2023).
[36] Meta. 2024. Introducing Meta Llama 3: The most capable openly available LLM
to date. https://ai.meta.com/blog/meta-llama-3/.
[37] Roshanak Mirzaee and Parisa Kordjamshidi. 2022. Transfer learning with
synthetic corpora for spatial role labeling and reasoning. arXiv preprint
arXiv:2210.16952 (2022).
[38] Ida Momennejad, Hosein Hasanbeig, Felipe Vieira Frujeri, Hiteshi Sharma, Nebojsa Jojic, Hamid Palangi, Robert Ness, and Jonathan Larson. 2024. Evaluating
cognitive maps and planning in large language models with CogEval. Advances
in Neural Information Processing Systems 36 (2024).
[39] OpenAI. 2022. Introducing ChatGPT. https://openai.com/blog/chatgpt/.
[40] Dharmen Punjani, Kuldeep Singh, Andreas Both, Manolis Koubarakis, Iosif Angelidis, Konstantina Bereta, Themis Beris, Dimitris Bilidas, Theofilos Ioannidis,
Nikolaos Karalis, et al. 2018. Template-based question answering over linked
geospatial data. In Proceedings of the 12th workshop on geographic information
retrieval. 1–10.
[41] Jonathan Roberts, Timo Lüddecke, Sowmen Das, Kai Han, and Samuel Albanie.
2023. GPT4GEO: How a Language Model Sees the World’s Geography. arXiv
preprint arXiv:2306.00020 (2023).
[42] Chenyang Shao, Fengli Xu, Bingbing Fan, Jingtao Ding, Yuan Yuan, Meng Wang,
and Yong Li. 2024. Beyond Imitation: Generating Human Mobility from Contextaware Reasoning with Large Language Models. arXiv preprint arXiv:2402.09836
(2024).
[43] Zhengxiang Shi, Qiang Zhang, and Aldo Lipani. 2022. Stepgame: A new benchmark for robust multi-hop spatial reasoning in texts. In Proceedings of the AAAI
conference on artificial intelligence, Vol. 36. 11321–11329.
[44] Karan Singhal, Shekoofeh Azizi, Tao Tu, S Sara Mahdavi, Jason Wei, Hyung Won
Chung, Nathan Scales, Ajay Tanwani, Heather Cole-Lewis, Stephen Pfohl, et al.
2023. Large language models encode clinical knowledge. Nature 620, 7972 (2023),
172–180.
[45] Mirac Suzgun, Nathan Scales, Nathanael Schärli, Sebastian Gehrmann, Yi Tay,
Hyung Won Chung, Aakanksha Chowdhery, Quoc V Le, Ed H Chi, Denny Zhou,
et al. 2022. Challenging big-bench tasks and whether chain-of-thought can solve
them. arXiv preprint arXiv:2210.09261 (2022).
[46] Gemma Team. 2024. Gemma. (2024). doi:10.34740/KAGGLE/M/3301
[47] Mistral AI team. 2025. Mistral Small 3. https://mistral.ai/news/mistral-small-3/.
[48] Qwen Team. 2024. Qwen2.5: A Party of Foundation Models. https://qwenlm.
github.io/blog/qwen2.5/
[49] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. 2023. Llama 2: Open foundation and fine-tuned chat models. arXiv
preprint arXiv:2307.09288 (2023).
[50] Xinglei Wang, Meng Fang, Zichao Zeng, and Tao Cheng. 2023. Where would i
go next? large language models as human mobility predictors. arXiv preprint
arXiv:2308.15197 (2023).
[51] Xi Wang, Xianyao Ling, Tom Zhang, Xuecao Li, Shaolan Wang, Zhixing Li, Liang
Zhang, and Peng Gong. 2023. Optimizing and Fine-tuning Large Language Model
for Urban Renewal. arXiv preprint arXiv:2311.15490 (2023).
[52] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian
Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al.
2022. Emergent abilities of large language models. arXiv preprint arXiv:2206.07682
(2022).
[53] Shijie Wu, Ozan Irsoy, Steven Lu, Vadim Dabravolski, Mark Dredze, Sebastian Gehrmann, Prabhanjan Kambadur, David Rosenberg, and Gideon Mann.
2023. Bloomberggpt: A large language model for finance. arXiv preprint
arXiv:2303.17564 (2023).

Jie Feng et al.
[54] Jiannan Xiang, Tianhua Tao, Yi Gu, Tianmin Shu, Zirui Wang, Zichao Yang, and
Zhiting Hu. 2024. Language models meet world models: Embodied experiences
enhance language models. Advances in neural information processing systems 36
(2024).
[55] Derong Xu, Wei Chen, Wenjun Peng, Chao Zhang, Tong Xu, Xiangyu Zhao,
Xian Wu, Yefeng Zheng, and Enhong Chen. 2023. Large language models for
generative information extraction: A survey. arXiv preprint arXiv:2312.17617
(2023).
[56] Yutaro Yamada, Yihan Bao, Andrew K Lampinen, Jungo Kasai, and Ilker Yildirim.
2023. Evaluating Spatial Understanding of Large Language Models. arXiv preprint
arXiv:2310.14540 (2023).
[57] Jing Yuan, Yu Zheng, and Xing Xie. 2012. Discovering regions of different
functions in a city using human mobility and POIs. In Proceedings of the 18th
ACM SIGKDD international conference on Knowledge discovery and data mining.
186–194.
[58] Aohan Zeng, Mingdao Liu, Rui Lu, Bowen Wang, Xiao Liu, Yuxiao Dong, and
Jie Tang. 2023. Agenttuning: Enabling generalized agent abilities for llms. arXiv
preprint arXiv:2310.12823 (2023).
[59] Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding,
Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, et al. 2022. Glm-130b: An open
bilingual pre-trained model. arXiv preprint arXiv:2210.02414 (2022).
[60] Jirong Zha, Yuxuan Fan, Xiao Yang, Chen Gao, and Xinlei Chen. 2025. How to
Enable LLM with 3D Capacity? A Survey of Spatial Reasoning in LLM. IJCAI
(2025).
[61] Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou,
Yingqian Min, Beichen Zhang, Junjie Zhang, Zican Dong, et al. 2023. A survey
of large language models. arXiv preprint arXiv:2303.18223 (2023).
A APPENDIX
A.1 Comparison of CityEval with other
Benchmarks
Table 7 presents a comparison of our CityEval with several related
benchmarks on geospatial and urban knowledge. As shown in the
table, CityEval covers a wider range of task types and provides detailed evaluations for three cities. Most existing benchmarks focus
solely on assessing the spatial knowledge of LLMs, which is only
one aspect of CityEval. In contrast, CityEval includes high-level reasoning questions and multiple real-world downstream application
tasks. Detailed content of four modules in CityEval are introduced
as follows. Detailed statistic information for CityEval in Beijing can
refer to Table 8.
A.2 SWFT Validation in Other Cities
This section presents comparative results for models trained using
different methods in Beijing and NewYork. From the Table 9, we
observe that models trained using SWFT outperform those obtained
through standard SFT training.
A.3 Effects of the LLM Size
In this section, we study the effects of model in Figure 8. We select
the Qwen1.5 with 0.5B-14B models to investigate the influence
of the model size. Due to limited computing resources in our experiments, all Qwen1.5 models were trained with full fine-tuning
settings, except for Qwen1.5-14B, which was trained using LoRA
settings. As Figure 8 shows, we can observe that the challenging
Spatial Reasoning task require LLMs with larger parameters while
the Urban Semantics task group can be handled well with smaller
LLMs. Furthermore, CityGPT-Qwen1.5-14B outperforms CityGPTChatGLM3-6B with more than 20% in the Spatial Reasoning task.
Although Qwen1.5-14B shows only minimal performance gains
and even declines in certain tasks compared to smaller models, we
believe this may be due to the LoRA training mechanism.

CityGPT: Empowering Urban Spatial Cognition of Large Language Models
Table 7: Comparison of our CityEval with several re
Types Content Inst
GeoBench [10] 2 task GeoScience Exam ~
GPT4GEO [41] 19 tasks limited task for city ~
Space&Time [21] 1 task POI coodinates ~
CityImage, UrbanSemantics,
CityEval-Ours 39 tasks ~
Spatial Reasoning
Table 10: Comparison of our data with SimpleData on
Qwen2.5-7B.
Model@Beijing CI US SR
Qwen2.5-7B 0.325 0.587 0.164
Qwen2.5-7B-SimpleData 0.320 0.583 0.252
Qwen2.5-7B-SimpleData2 0.312 0.573 0.191
CityGPT-7B-OurData 0.502 0.620 0.552
Table 11: Performance of CityGPT with zero-shot settings
and Qwen2.5-7B with few-shot settings in CityEval.
Model@Beijing CI US SR
Qwen2.5-7B-zeroshot 0.325 0.587 0.164
Qwen2.5-7B-5shot 0.368 0.596 0.279
CityGPT-7B 0.502 0.620 0.552
Table 12: The performance of CityGPT-7B, trained using data
from CityA, evaluated using data from CityB.
Task Training@London Training@NewYork Training@Paris
Beijing CI 0.482 0.460 0.437
US 0.543 0.563 0.530
SR 0.584 0.598 0.588
London CI / 0.506 0.434
US / 0.567 0.567
SR / 0.596 0.605
NewYork CI 0.465 / 0.486
US 0.573 / 0.590
SR 0.576 / 0.626
Table 8: Statistics of different task groups of CityEval in
Beijing, where Composite Tasks are conducted in BeijingWudaokou, and Acc. denotes accuracy, SR. denotes success
rate.
Task Group #Insts. #Tasks Metrics
City Image 650 13 Acc
Urban Semantics 300 6 Acc
Spatial Reasoning 1000 20 Acc
Composite Tasks 321 3 SR, etc.
Table 9: The performance of Models using different tuning
method on CityEval and general benchmarks.
City Model CI US SR MMLU GSM8K BBH
Beijing Base-LLama3 0.286 0.520 0.285 68.33 79.38 52.88
SFT-CityGPT 0.554 0.680 0.708 56.89 60.58 53.92
SWFT-CityGPT 0.605↑ 0.670≈ 0.709≈ 60.51↑ 57.92≈ 55.76↑
NewYork Base-LLama3 0.331 0.503 0.277 68.33 79.38 52.88
SFT-CityGPT 0.574 0.650 0.712 55.12 59.44 53.37
SWFT-CityGPT 0.654↑ 0.673↑ 0.704≈ 63.72↑ 61.56↑ 56.29↑

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
ed benchmarks on geospatial and urban knowledge.
es Source Scale Format
NPEE, APTest - multi-choice
GeoNames, Google Map World generate
NYC OpenData POI NYC regression
Beijing, Paris,
Open Street Map multi-choice
NewYork, London
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0.0
0.5B 1.8B 4B 7B 14B
ycaruccA
City Image Spatial Reasoning(with context)
Urban Semantics Spatial Reasoning(w/o context)
Figure 8: The performance of CityGPT improves as the parameters of Qwen1.5 increase, from 0.5B to 14B.
A.4 Additional Results of SimpleData
Extending our exploration from Section 3.5, this section includes
the SimpleData and 5-shot results for Qwen2.5-7B in Table 10 and
Table 11, which are identical to those for LLama3-8B. Our CityGPT
significantly outperforms models trained with simple urban geographic data and baseline with 5-shot setting.
A.5 Extended Results of Spatial Transferability
Following up on the results in Section 3.4, we also conduct urban
transferability assessments for CityGPT-7B, trained with data from
different cities. The results can be viewed in Table 12. Models trained
with data from CityA have achieve excellent results in evaluation
of CityB.
A.6 Data Statistics
We present the spatial range of the four evaluated regions in Figure 9
and the constructed CityInstruction data for each city in Table 13.
A.7 Description of Urban Composite Tasks
Mobility Prediction: The model is required to predict the next
PoI of a person based on his/her previous trajectory. Information
provided include: 1) previous trajectory of the person (a series
of trajectory items formatted as [poi name, visiting time]), 2) the
visiting time of the PoI that requires prediction, 3) 9 candidate
prediction PoIs. Note that the trajectory data used in this experiment

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Figure 9: Spatial range of eva
Table 13: Basic statistical information of CityInstruction.
CityReasoning data for the four cities are the same which
are generated from SanFrancisco.
City Dataset Instance Length/Token Rounds
General Spatial 3488 283 1
Instruction Data Chat 41866 745 2.32
CityWalk 30000 593 1
CityInstruction@Beijing CityQA 48551 105 1
CityReasoning 7992 688 1.13
CityWalk 30000 537 1
CityInstruction@London CityQA 48691 88 1
CityReasoning 7992 688 1.13
CityWalk 30000 607 1
CityInstruction@NewYork CityQA 48484 95 1
CityReasoning 7992 688 1.13
CityWalk 29128 645 1
CityInstruction@Paris CityQA 41546 108 1
CityReasoning 7992 688 1.13
are all from real world users. Ground truth of each question is
extracted from the trajectory dataset.
Trajectory Generation: The model generates a trajectory based
on a virtual agenda generated by GPT-3.5-turbo-1106. First, 250
templates of virtual agenda, formatted as a series of [time, action]
items, is generated with GPT-3.5. Then, the model is required to
assign a possible poi to each [time, action] item, which creates a
trajectory with each point in time assigned with a corresponding
PoI. The performance of the model is evaluated by comparing the
virtually generated trajectories with the real-word ones. Specifically,
we use JSD to measure the similarity between the mobility pattern
distributions of generated trajectory and real trajectory data.
Spatial Navigation: The model is required to make step by step
navigation from one AoI to another. At each step, the model is
provided with: 1) hint about its current position(denoted by the two
PoIs closest to its current position), 2) name of the destination AoI
B, 3) candidate choices of navigation lanes (extracted from the map
simulating platform and formatted as [road name, direction]). The
choice of the model among the candidates will lead to a position
update towards the next crossroad along the chosen road and its
corresponding direction. The task is deemed successful if the model
is able to navigate itself to a position that is within a threshold

Jie Feng et al.
ted cities in the experiments.
distance( 500m in our experiment) to the destination AoI B in 30
steps. For evaluation, the models are tested on 21 navigation tasks
designed to be finished within a minimum of 1,3,6 steps and an
average of 4.5 steps. Metrics are introduced as below.
• Acc(multi): prediction accuracy when N candidate PoIs are
provided.
• Acc(gen): prediction accuracy when no candidate PoIs are
given.
• Radius(JSD): radius of gyration, which represents the spatial
range of the user’s daily activities.
• DailyLoc(JSD): daily visited locations, which is calculated as
the number of visited locations per day for user.
• Steps: average step that the model took to finish the navigation
task. Note that the step is counted as 30 (maximum rounds of
navigation) for cases where the model failed to navigate to the
destination.
• Success Rate: probability that the model successfully navigates
to the specified location.
A.8 Hyper-parameter Settings
Table 14: Hyper-parameters for fine-tuning.
Hyper-parameter Value Hyper-parameter Value
Learning Rate 1e-5 Max Sequence Length 4096
Batch Size Per Device 1 Epoch 1
Gradient Acc Steps 16 LR Scheduler cosine
To reduce the training cost, we choose to fine-tune the chat
version of general LLMs. We utilize accelerate [20] with the full
training mode to fine-tune the LLMs in a server with 4 A800 GPUs.
We try to train ChatGLM3-6B [59], Qwen series [3], and LLama38B [49] in our experiments. During the experiments, we find that
the influence of parameter settings is far less than the influence of
data quality. Thus, we fix the training parameters in most of the
experiments and leave the work of best parameter search in the
future. The core training parameters settings are shown in Table 14.
