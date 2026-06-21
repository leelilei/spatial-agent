---
title: "UrbanLLaVA: A Multi-modal Large Language Model for Urban Intelligence with Spatial Reasoning and Understanding"
source_pdf: "03_embodied_city\\02_UrbanLLaVA_Feng2025.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:32:34+00:00
page_count: 29
status: ok
text_char_count: 94653
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\03_embodied_city\02_UrbanLLaVA_Feng2025.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:32:34+00:00
- Page count: 29
- Status: ok
- Text chars: 94653
- Quality flags: none

## Metadata

- Title: UrbanLLaVA: A Multi-modal Large Language Model for Urban Intelligence with Spatial Reasoning and Understanding
- Author: Jie Feng; Shengyuan Wang; Tianhui Liu; Yanxin Xi; Yong Li
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

Urban research involves a wide range of scenarios and Satellite Image Street View Image tasks that require the understanding of multi-modal data. Current methods often focus on specific data types and lack a unified framework in urban field for processing them comprehensively. The recent success of multi-modal large language models (MLLMs) presents a promising opportunity to overcome this limitation. In this paper, we introduce UrbanGeLoLSpaaVtiAal, Daatamulti-modal largeTrlaajencgtourya gDeatamodel designed to process these four types of data simultaneously and achieve strong performance across diverse urban tasks compared with general MLLMs. In UrbanLLaVA, we first curate a diverse urban instruction dataset encompassing both singlemodal and cross-modal urban data, spanning from location view to global view of urban environment. Additionally, we propose a multi-stage training framework that decouples spatial reasoning enhancement from domain knowledge learning, thereby improving the compatibility and downstream performance of UrbanLLaVA across diverse urban tasks. Finally, we also extend existing benchmark for urban research to assess the performance of MLLMs across a wide range of urban tasks. Experimental results from three cities demonstrate that UrbanLLaVA outperforms open-source and proprietary MLLMs in both singlemodal tasks and complex cross-modal tasks and shows robust generalization abilities across cities. Source codes and data are openly accessible to the research community via https://github.com/tsinghua- fiblab/UrbanLLaVA.

## Outline

- Introduction (page 1)
- Methods (page 3)
  - UData: Constructing Urban Instruction Data from a Multi-View Perspective of Urban Space (page 3)
    - Location View Data (page 3)
    - Trajectory View Data (page 3)
    - Global View Data (page 4)
  - UTrain: A Multi-Stage Training Pipeline for Decoupling Reasoning and Knowledge Learning (page 4)
  - UBench: An Enhanced Multimodal Benchmark for Urban Intelligence Tasks (page 5)
- Experiments (page 5)
  - Settings (page 5)
  - Main Results (page 5)
  - Effects of Training Strategies (page 6)
  - Model Generalization Study (page 6)
  - Data Ablation Study (page 7)
  - Case Study (page 7)
- Related Work (page 8)
  - Multi-modal Large Language Model (page 8)
  - Multi-modal Model for Urban Study (page 9)
- Conclusion (page 9)
- Limitation and Future Work (page 9)
- Data Example for Three Stages (page 12)
- Comparing with models for single-modality urban tasks (page 12)
- Additional Detailed Results of Three Cities (page 12)
- Additional Results for Training Strategies (page 12)
- Effects of Training Data Size (page 12)
- Effects of Base Model (page 12)
- Effects of Model Size (page 12)
- Additional Case Study (page 13)
- Urban Instruction Data (page 14)

## Markdown Content

5202
n
UrbanLLaVA: A Multi-modal Large Language Model for Urban Intelligence
with Spatial Reasoning and Understanding
Jie Feng†, Shengyuan Wang‡, Tianhui Liu§, Yanxin Xi¶, Yong Li†
†Department of Electronic Engineering, BNRist, Tsinghua University, Beijing, China
‡Department of Computer Science and Technology, Tsinghua University, Beijing, China
§School of Electronic and Information Engineering, Beijing Jiaotong University, China
¶University of Helsinki, Finland
{fengjie, liyong07}@tsinghua.edu.cn

nuJ
92
]VC.sc[
1v91232.6052:viXra
Abstract
Urban research involves a wide range of scenarios and Satellite Image
Street View Image
tasks that require the understanding of multi-modal data.
Current methods often focus on specific data types and lack
a unified framework in urban field for processing them comprehensively. The recent success of multi-modal large language models (MLLMs) presents a promising opportunity to
overcome this limitation. In this paper, we introduce UrbanGeLoLSpaaVtiAal, Daatamulti-modal largeTrlaajencgtourya gDeatamodel designed to
process these four types of data simultaneously and achieve
strong performance across diverse urban tasks compared
with general MLLMs. In UrbanLLaVA, we first curate a diverse urban instruction dataset encompassing both singlemodal and cross-modal urban data, spanning from location
view to global view of urban environment. Additionally,
we propose a multi-stage training framework that decouples spatial reasoning enhancement from domain knowledge learning, thereby improving the compatibility and
downstream performance of UrbanLLaVA across diverse
urban tasks. Finally, we also extend existing benchmark
for urban research to assess the performance of MLLMs
across a wide range of urban tasks. Experimental results
from three cities demonstrate that UrbanLLaVA outperforms open-source and proprietary MLLMs in both singlemodal tasks and complex cross-modal tasks and shows robust generalization abilities across cities. Source codes
and data are openly accessible to the research community via https://github.com/tsinghua- fiblab/UrbanLLaVA.
1. Introduction
Urban science [53, 57] and geographic science research[35]
highlight that urban data spans multiple modalities, including urban visual data [14], geo-text [45], structured geospa-

General Multi-Modal Large Lanauge Models (LLaVA, ......)
Satellite Image GeoSpatial Data Satellite Image
Trajectory
Street
View
GeoChat CityGPT Image
GeoSpatial Data
Street View Trajectory Data
Urban Instruction Data
UrbanVLP Mobility-LLM UrbanLLaVA
Existing Works Our Work
Figure 1. Existing works vs. our UrbanLLaVA in urban research.
tial data [1, 2], and spatiotemporal series data [20, 28]. Together, these data types capture the multi-faceted nature of
urban environments, representing a wide range of spatial
information and urban knowledge [35, 46, 57]. Integrating these multi-modal data into a cohesive framework is
essential for developing a systematic understanding of urban spaces and advancing complex modeling architectures
in urban research. However, the inherent heterogeneity of
these diverse urban data presents substantial challenges for
the integration. While numerous deep learning based methods have been proposed to fuse various cross-domain urban data [57], they are often designed for specific urban
tasks, limiting their ability to achieve a comprehensive understanding of urban environment and advanced reasoning
for real-world urban applications [46, 53].
Recently, multi-modal large language models
(MLLMs) [49] have made notable advancements by
leveraging large language models (LLMs) [38] with

UUDDaattaa:: D Daattaa P Piippeelliinnee xxxxxx
LLM
projector tokenizer&emb
Training vision encoder converter
STV-QA STV-Addr
Q: <image>\n Q: <image>\nPlease tell me detailed
Please find the address of this street view image.
landmark in this A: Shuguang, xx, Haidian District,
street view image Beijing, 100080, China
and possible
surrounding POIs. STV-Disc
Q: <image>\nPlease describe the
STV-Geo street view image and possible
Q: Where is this surrounding POIs.
image located? Navigati
A: It is in XX road Q: <image>\n Please provide
500m, where xxxxx Reason and next Action('forw
'right', or 'stop') based on the
and the route navigation instr
GeoSpatial Data Trajectory-Vision Traject
Q a A m r : : o e r W u T t n e h h d r e s e h r r a e e e h r i i e e s s a ? a t d h , g e . r . o n . c e e a r r y es s t t s o h re o p 1 00 Q A n s a c o n : : e t d Y … n ic e o w i h n u f a e g e a n a a r < t d t e u i i t m n o r p i g o n a t r s g g f a i r e t v x o i > e o x m , l n x t t e n h o … d o e V r r a e t e t h l i C v s to e a a t f s e s L o t R r u o e t u o e h n m t g a e. Q t A t o o : : … K s Y o O o u tr u t a h B 'r v , e u e w r l a g i i t n t e h L g r. a S 3 v t 0 a a 0 , r b a m u n e c d t k e y s r o s o u n f r n o t e h
GeoSpatial Data (Geo) Street View Image (STV) Trajectory Data (Tr
Location View Trajectory View
Figure 2. The framework of UrbanLLa
build-in common sense and reasoning abilities as a central component for unifying the processing data across
various modalities, such as images [31], speech [19], and
time series [25]. For example, Ma et al. [34] develop a
vision-language model as a conversational assistant for
autonomous driving, Brohan et al. [4] introduce RT-2,
a vision language model based end-to-end model for
flexible robotics control, Li et al. [27] train LLaVA-Med
for answering open-ended questions related to biomedicine
images. Building on this trend, researchers have begun
to explore the potential of MLLMs in urban studies [53].
As shown in the left part of Figure 1, notable examples
include GeoChat [26], an early effort in creating MLLMs
for remote sensing tasks; Mobility-LLM [20], which
extends LLM with capabilities for trajectory modeling; and
CityGPT [16], designed to process structured geospatial
data with LLMs. In contrast to earlier urban data fusion
methods developing in the deep learning era [53, 57], these
recent studies incorporate various unimodal urban data into
LLMs to create obtain MLLMs that maintain the powerful
reasoning abilities and address diverse urban tasks within a
single modality.
However, these recent works focus solely on processing unimodal urban data and fall short of achieving a comprehensive understanding and modeling of urban system
across diverse tasks involving multi-modal urban data. Unified modeling of multi-modal urban data poses significant

ain: Training Pipeline UBench: Evaluation Benchmark
LLM Proj.
3: Mixture Tuning Single View Multi View
Trajectory Trajectory + STV
2: Knowledge Learning GeoSpatial Geo + SAT
Evaluation Satellite Image Geo + STV
: Task Alignment Street View Image Geo + SAT +STV
Understanding Reasoning
SAT-Disc GeoQA Satellite Image
Q: <image>\nPlease
tell me the address and
layout of the amenities Q: Which of the
in the satellite image. following roads is not
connected to Victoria
Embankment Gardens?
Q: In the provided four
Street View Image satellite images in urban area,
which image probably
n shows most POIs (For
Q: You are given a SAT i S m A a T ge & STV Q po : s S si e b le le c t n in e g ar t b h y e P m O o I s s t or e 'b x a a k m er p y l s e ' , , [ 'f 'r o e o s d ta s u ', r ' a fa n s ts t_ ', foods'])?
<image> and a STV image <image>, landmarks description
and please predict which quadrant the in the region of a street
STV image lies in the SAT image. view image.
t A: Bottom left
Trajectory-Prediction
Q: <history>: xxx, <context>: xxx,
<target_stay>: xxx
Your task is to predict a user's next
location based on his/her activity
Satellite Image (SAT) pattern <history> and <context>.
Please infer what the
<next_place_id> might be from
<target_stay>.
Trajectory-Visual Consistency
Q: You are given one reference image <image>\n and four
options. Which option image is taken most close to the
reference?
Global View
including UData, UTrain and UBench.
challenges. The first challenge is the scarcity of highquality data for cross-modality alignment. While previous
works [16, 26] propose various methods for constructing
instruction tuning dataset for different types of unimodal
urban data integrated with language, these efforts are insufficient for unified modeling across multiple modalities.
A second challenge lies in the potential conflicts among
diverse urban tasks across different modalities, which can
lead to unstable training and inconsistent performance.
In this paper, we introduce UrbanLLaVA, a multi-modal
large language model designed to build comprehensive urban cognition and addressing a wide range of urban tasks,
which is shown in the right part of Figure 1. In UrbanLLaVA, we first design UData, a systematic urban instruction data pipeline that enables the generation of highquality synthetic data. In UData, data generation is meticulously structured to span multiple perspectives—from a
localized view for single modality data to trajectory and
global view for cross-modality data—capturing the inherently multi-faceted nature of urban system. To improve the
training stability and model performance, we conduct extensive experiments to identify key factors impacting the
training process and develop an effective three-stage training pipeline UTrain, based on these insights. In fact, the
proposed multi-stage training framework can be viewed as
a promising practice that explicitly decouples the learning
of reasoning capabilities from domain-specific knowledge

W
alk
R
andom
V
isual
D ata
V
iew
C rossR easoning M od
1
ality
4
C r
9
oss
7 7 1 9 2 7
C
ityQ
1
A
Locatio
d
n
dress
Co S m A M p T a u r l i t s i o p n le 10114 & 7 S 7 T 2 ( V S 0
)
A 4 T I m age M s ulti T ex t
V
D ata
L o c
932
S
46
in g
A
le
51130 La D nd et m ai a l r s k
I L n a f e n r d e u n s c e e 3 6 4 2
G
lo b a l ie w D a
ta
U D a t a
ie w
D a ta
a tio
n
S
V
tr
I
e
i m e
e
w
t
ag e 2 8 7 9 8 I D m e a s g c e r ip tio n
L A oc d a d t r io es n s 2 7
I
7
m
7
a C g o e n
I
te
n
n 9
d
t
S
3
i
1
I a v
5
m t i e d a l u l g i a t e e l
30
V
00 V isio n - A u g m en
T V
ta
r
ted
a ie je w c t D o r a y ta B
ase 9 d
T
8
ext9001 W al R k and
2
o
0 0
m
0 R M e C a o s r d o o a n s l s i i n ty g
V
ision- Languag
N
e avigation
8 9 3 6
T rajector
W
y
orld
R ealFigure 3. The thorough composition of UData in Beijing.
in MLLMs. Finally, we extend existing urban benchmarks
to build a systematic urban benchmark UBench for evaluating the capabilities of MLLMs in tackling diverse urban
tasks. In summary, our contributions are as follows,
• UrbanLLaVA is the first MLLM designed for the unified
modeling of four major types of urban data, with the
goal of fostering comprehensive understanding and effective task-solving for urban environments, to the best
of our knowledge.
• We conduct extensive experiments to identify the key
factors influencing training and propose a three-stage
training pipeline that ensures stable performance of UrbanLLaVA across a wide range of urban tasks involving
multiple data modalities.
• UrbanLLaVA demonstrates effective integration of
multi-modal data, establishing comprehensive spatial
cognition and outperforming general MLLMs across
various urban tasks based on results from an enhanced
urban task benchmark.
2. Methods
As illustrated in Figure 2, UrbanLLaVA comprises three
key components: 1) the data pipeline, UData, designed
for generating diverse and high-quality urban instruction
data across various urban scenarios; 2) the training pipeline,
UTrain, which facilitates efficient and stable training across
a wide range of urban tasks; 3) the evaluation benchmark,
UBench, for evaluating the capabilities of MLLMs in multimodal urban tasks.

2.1. UData: Constructing Urban Instruction Data
from a Multi-View Perspective of Urban Space
Over the past decade, effectively integrating multi-modal
urban data has emerged as a key research question in urban
studies [57]. Building on the successes of MLLMs in various fields [49, 53], we extend the modelling of four types
of urban data into a unified model, UrbanLLaVA, by constructing a diverse urban instruction data from a systematic view on the urban environment. Specifically, we organize the urban instruction data in a sequence that move
from location view to a trajectory view, and finally to a
global view. This approach ensures both broad spatial
coverage and the integrity of relationships between different modalities in the final data. UData builds upon four
kinds of original urban data: 1) the structured geospatial
data from OpenStreetMap 1; 2) public trajectory data, e.g.,
Foursquare-checkins [48] and OpenStreetMap traces 2; 3)
satellite images from GoogleEarth 3; 4) street view images
from GoogleMap 4 and BaiduMap 5. Before experiments,
we collect original data from above platforms and using the
following data pipeline to build instruction data. We follow the license of these platforms and ensure that the data
is used only for academic research.
2.1.1. Location View Data
In the location view data construction stage, we focus on
structured geospatial data and single street view images.
Following the recent practices [1, 16] for structured geospatial knowledge learning, we create geospatial instruction
data by designing question templates that transform basic
geospatial data into natural language question and answers.
For single street view image, we synthesize three types
of questions: 1) two types based on predefined templates
populated with information from structured geospatial data,
such as, location addresses and landmark details; 2) one
general MLLM generated detailed description of the image
content, following the common practice for image captioning [6]. Throughout the data construction, we maintain a
core principle of integrating street view image content with
structured geographical knowledge, such as consistency in
location addresses and landmark descriptions.
2.1.2. Trajectory View Data
Here, we construct the trajectory view data, which includes
the geospatial data, trajectory data, and street view images.
We start by creating two types of text-based trajectory data.
The first type is generated by randomly sampling origin and
destination points for routing, while the second type uses
the real-world trajectory data collected from the public web
1https://www.openstreetmap.org
2https://www.openstreetmap.org/traces
3https://earth.google.com/
4https://www.google.com/maps
5https://map.baidu.com/

source, including Foursquare-checkins and OpenStreetMap
traces. To enhance geospatial context of trajectory data, we
align the GPS coordinates from these original data sources
with the structured geospatial data, using the textual addresses to represent locations within the trajectory. Additionally, we integrate street view images to enrich trajectory data, resulting two types of vision-augmented trajectory data. The first data extends the text-based trajectory
data by incorporating street view images captured along the
route (excluding intersections). We organize this data with
the similar interleaved image-text format in VILA [29]. The
second data builds on the navigation instruction format akin
to the classic vision-language navigation task [5]. In this
data, multiple street view images are presented at intersection during the trajectory, and the correct image is selected
to guide the continuation of the journey.
2.1.3. Global View Data
Here, we present the construction of global view data designed to capture relationships among diverse data types
over long distances, with street view images and satellite
images as primary components and geospatial data serving
as auxiliary support. Initially, we create a basic form of
global view data by generating captions for single satellite
image data enriched with structured geospatial data. Specifically, we define three types of data: 1) prompting general MLLM to produce detailed content description for individual satellite image; 2) sampling location address within
satellite image and using a general LLM to summarize the
spatial coverage of it based on these location address; 3)
prompting general MLLM with land use ground-truth label
to generate land use inference results with reason.
Furthermore, we introduce the multiple satellite images
for more complex instruction data. The first task is to compare the building densities across multiple satellite images.
The second task focuses on identifying functional point of
interest within these images. For these tasks, we provide
manually crafted reasoning steps in a chain-of-thoughts format, supported by structured geospatial data, to improve the
alignment between satellite images and geospatial data. Finally, we design two tasks to strengthen the alignment between the street view images and satellite images. The first
task is to select the correct satellite image from a set when
given a street view image, requiring the model to understand and match content or address across both image types.
The second, more challenging task involves pinpointing the
location of the street view image within a specific satellite
image, such as identifying it as located in the top-left region
of satellite image.
Based on the data generation steps described before, we
perform data quality checks and filtering on the synthesized
data to ensure its quality.

2.2. UTrain: A Multi-Stage Training Pipeline for Decoupling Reasoning and Knowledge Learning
Answer: .... UTrain
LLM
Stage3: Mixture Tuning
Stage2: Knowledge Learning
Stage1: Task Alignment
Figure 4. UTrain: three-stage training pipeline.
Training UrbanLLaVA presents significant challenges
due to the heterogeneity of multi-modal urban instruction
data and the diversity of urban tasks. Achieving stable training and balancing performance across various tasks is notably difficult. We chose VILA[29] as the base model for
our experiments and conduct extensive studies to identify
key factors affecting training. We examine the impact of the
training order of multi-modal data and trained components,
observing minimal effects. However, we find that learning
rate has significant effects on training stability and performance. Detailed results of them are provided in the section 3.3. Additionally, inspired by Dong et al. [12], we explore and propose an effective multi-stage training pipeline
which is shown in the Figure 4.
We first introduce three kinds of learning procedures:
knowledge learning, task alignment and mixture learning. The knowledge learning procedure refers to the training process which UrbanLLaVA acquires foundational urban knowledge from various urban data, such as the information of geospatial data, pure textual trajectory, and
detailed description of street view and satellite images.
The task alignment learning focuses on equipping UrbanLLaVA with task-specific skills for urban applications, including vision-language navigation, trajectory prediction,
chain-of-thoughts reasoning across multiple satellite and
street view images. Finally, mixture learning represents
the standard training method used by most MLLMs, which
training by directly mixing all types of instruction data.
During our experiments, we observe that different combination of various learning procedures significantly impact
the training. Based on the observations, we propose a threestage tuning pipeline to improve the training stability and
performance on diverse urban tasks. This pipeline consists of three sequential stages:task alignment, knowledge
learning, and finally mixture learning. Starting with a welltrained general MLLM as our base model, we first introduce the task alignment learning procedure, fine-tuning the
model with diverse urban task related instructions to prepare it for various urban tasks. Through this phase, the
model become familiar with a variety of urban tasks, lever-

aging its pre-existing general knowledge to complete them.
However, familiarity with general knowledge alone is insufficient for effectively addressing diverse urban tasks, so
we incorporate the second stage, knowledge learning procedure. This stage imparts specialized urban knowledge
from multi-modal urban data that is essential for task resolution. Finally, we introduce the mixture learning stage
to enhance the model’s awareness of combining knowledge
and skills for solving diverse urban tasks. Here, we resample 1/3 domain specific data from the first two stages and
1/3 general textual instruction data, e.g. ShareGPT 6 and
UltralChat [11], for final tuning.
2.3. UBench: An Enhanced Multimodal Benchmark
for Urban Intelligence Tasks
To assess the potential of MLLMs in urban studies, CityBench [18] and Urbench [56] have been recently introduced. Drawing from the diverse evaluation tasks in these
two benchmarks, we reorganize and expand them to create
the urban evaluation benchmark UBench, which includes
12 tasks for our experiments. All the evaluation tasks are
presented in Table1. We select 6 of these tasks based on
the utility of the evaluation data and their relevance to urban scenarios involving UrbanLLaVA’s urban data. For
structured geospatial data and trajectory modelling, we incorporate the GeoQA, trajectory prediction and navigation
task from CityBench. For cross-view urban tasks involving
both street view and satellite images, we adopt the image
retrieval, camera localization, and scene comparison task
from UrBench. In addition, we introduce 6 new tasks in
UBench. Four of these tasks are designed for single street
view and satellite images, including address inference for
both image types, landmark recognition for street view images, and land use inference for satellite images. These
single-image tasks are aligned with the urban instruction
data, and we partition the original dataset into training and
validation sets to prevent potential data leakage. Moreover,
we build 2 additional tasks involving multiple images: 1)
STV-Outlier, is a spatial consistency task for street view
image, where multiple images from a single trajectory are
compared to identify an outlier image not part of the trajectory; 2) SceneFunc, extends the scene comparison task from
UrBench, challenging model to select the correct satellite
image that fulfills specific functional requirements.
3. Experiments
3.1. Settings
We select Beijing, London and New York to conduct experiments. Due to the large volume of data, we select a region
6https://huggingface.co/datasets/shareAI/ShareGPT-Chinese-English90k

Table 1. Detailed information about UBench for Beijing, ‘STV’
refers to street view image, and ‘SAT’ refers to satellite image.
Tasks Data Category Metrics Samples Source
GeoQA Geospatial Data GeoQA Avg. Accuracy 1450 CityBench
TrajPredict Trajectory Data Geo+Traj Top-1 500 CityBench
Navigation Single STV Geo+Traj Success Rate 50 CityBench
SceneComp Multi SAT Geo+SAT Accuracy 200 UrBench
ImgRetrieval Multi STV & SAT Geo+SS Accuracy 200 UrBench
CameraLoc Multi STV & SAT Geo+SS Accuracy 200 UrBench
STV-Address Single STV Geo+STV Accuracy 200 UBench
STV-Landmark Single STV Geo+STV Accuracy 200 UBench
SAT-Address Single SAT Geo+SAT Accuracy 200 UBench
SAT-Landuse Single SAT Geo+SAT Accuracy 200 UBench
STV-Outlier Multi STV Geo+STV Accuracy 200 UBench
SceneFunc Multi SAT Geo+SAT Accuracy 200 UBench
from each cities to conduct experiments. The spatial coverage of each region is shown in supplementary material.
MLLMs We consider the following MLLMs as baselines: Qwen2VL-7B/72B [41], InternVL2-8B/26B [7, 8],
VILA1.5-3B/8B/13B [29], LLama3.2-11B/90B [36], and
GPT4o and GPT4o-mini [40]. For open source MLLMs,
we deploy them through VLMEvalKit [13]. The max output tokens are set to 1000, and the temperature is set as 0.
Metrics Table 1 contains all the metrics for UBench.
For general evaluation tasks including LLaVA-Bench(Inthe-Wild) [30], RealWorldQA [44], and MM-Vet [50], RealWorldQA uses accuracy as the metric, while LLaVABench(In-the-Wild) and MM-Vet use rating score form
GPT4o as the judgement.
Implementation We use codes from official repository 7
of VILA [29] for fine-tuning on a single 8xA100 node. The
training parameters are set as follows: a learning rate of 1e5, a maximum sequence length of 2048, a batch size of 8
per GPU, and one training epoch. Training UrbanLLaVA
for Beijing on 4xA100 took a total of 10.7 hours.
3.2. Main Results
The main results of UrbanLLaVA on three cities are presented in Table 2, more detailed information can be accessed in 9. We use VILA1.5-8B as the default base model
in most experiments and use UData with UTrain methods
to fine-tune it to obtain the final model UrbanLLaVA.
We analyze the results in Beijing first. One point to
note is that, since LLama3.2 series models currently do
not support multi-image input, the results for evaluation
tasks involving multiple images in the UBench are left
blank. For models within the same series, the general
trend is that larger parameter models tend to perform better, e.g., VILA1.5-13b significantly outperforms VILA1.53b on 5 out of 6 tasks, including both single modal and cross
modal tasks. Additionally, we observe that the latest released Qwen2VL series models outperform the GPT4o se7https://github.com/NVlabs/VILA

Table 2. Results on UBench at Beijing, London, and New York. Urb
cities. Here, ‘STV’ denotes street view images related tasks, ‘Geo
denotes satellite images related tasks, and ‘SS’ denotes street view
City Beijing
Task Group GeoQA Geo+Traj Geo+STV Geo+SAT Geo+SS GeoQA
VILA1.5-3B 0.3873 0.0200 0.3967 0.3200 0.2575 0.4362
VILA1.5-8B 0.4322 0.0589 0.4300 0.3488 0.2425 0.4841
VILA1.5-13B 0.4410 0.1156 0.5167 0.3638 0.2400 0.4592
InternVL2-8B 0.4709 0.1578 0.4667 0.3313 0.2325 0.4973
InternVL2-26B 0.4877 0.1478 0.4550 0.3825 0.2275 0.5168
Qwen2VL-7B 0.4950 0.1389 0.4383 0.3638 0.2675 0.4991
Qwen2VL-72B 0.5491 0.1611 0.5817 0.3588 0.2975 0.5802
LLaMA3.2-11B 0.4229 0.0756 0.4375 0.3075 / 0.4804
LLaMA3.2-90B 0.4502 0.1056 0.5325 0.2925 / 0.5659
GPT4o-mini 0.4542 0.1622 0.4350 0.3800 0.2475 0.5357
GPT4o 0.5479 0.1522 0.4300 0.4125 0.3025 0.6446
UrbanLLaVA-VILA1.5-8B 0.5682 0.2800 0.8650 0.6663 0.7025 0.6399
vs. VILA1.5-8B +31.47% +375.38% +101.16% +91.03% +189.69% +32.18%
vs. Best Baseline +3.48% +72.63% +48.70% +61.53% +132.23% -0.73%
ries models on 2 tasks. These results demonstrate the validity and usability of our UBench. Our UrbanLLaVA shows
marked improvements over all baselines across all tasks in
UBench. Against the best baselines, UrbanLLaVA achieves
performance gains ranging from 3.48% to 132.23% for
each task. When compared to the base model VILA1.58B, the minimum increase is 31.47% on the GeoQA task,
while the maximum reaches an impressive 375.38% on the
Geo+Traj task. These results highlight the effectiveness of
the proposed multi modal dataset, UData, which successfully equips smaller MLLMs with a variety of capabilities
within urban space, achieving superior performance over all
advanced general MLLMs.
The results in New York and London are similar to those
in Beijing. Out of 5 tasks, UrbanLLaVA@London and UrbanLLaVA@NewYork both perform best in 4 tasks. However, in GeoQA task, their performance is slightly inferior to GPT4o, with reductions of -0.73% and -7.37%, respectively. For UrbanLLaVA’s performance falling short
of expectations on certain task, we speculate two possible reasons: first, the quality of relevant data in the two
cities may be lower than that in Beijing, preventing the
model from acquiring urban capabilities through learning
in the training stage; second, the base model VILA1.58B may have comparatively weaker capabilities than commercial API GPT4o, e.g., for the GeoQA task, UrbanLLaVA@London outperforms VILA1.5-8B by 32.18% but
falls short of GPT4o by 0.73%.
Overall, the proposed UrbanLLaVA sucessfully enhance
the performance of small MLLMs on diverse urban tasks.
3.3. Effects of Training Strategies
Since UrbanLLaVA is trained with multi-modal urban instruction data, we conduct various experiments to explore a

LLaVA significantly outperforms other baselines in most task across
notes geospatial data, ‘Traj’ denotes trajectory related task, ‘SAT’
tellite images. Detailed subtask and metrics can refer to Table 1.
London New York
+Traj Geo+STV Geo+SAT Geo+SS GeoQA Geo+Traj Geo+STV Geo+SAT Geo+SS
400 0.2557 0.2850 0.2725 0.3954 0.0400 0.4400 0.2713 0.2425
884 0.4495 0.4575 0.2575 0.4575 0.1200 0.4983 0.3763 0.2525
298 0.4991 0.4538 0.2625 0.4501 0.2350 0.5583 0.4025 0.2825
347 0.4477 0.4763 0.2400 0.4632 0.1830 0.4917 0.4175 0.2400
288 0.4923 0.5138 0.2425 0.4766 0.2240 0.5217 0.4738 0.2375
560 0.4381 0.4863 0.2775 0.4567 0.1700 0.5117 0.5100 0.2950
322 0.6375 0.4375 0.3250 0.5273 0.2540 0.6333 0.3788 0.3275
180 0.4000 0.3800 / 0.4127 0.1100 0.5200 0.2225 /
010 0.5450 0.4700 / 0.5234 0.1570 0.6825 0.3400 /
278 0.4752 0.5388 0.2675 0.5075 0.2320 0.5633 0.4775 0.2350
300 0.5469 0.6050 0.2850 0.6232 0.2340 0.5767 0.5400 0.2900
680 0.7500 0.7100 0.4325 0.5773 0.3060 0.8500 0.7725 0.5825
.17% +66.85% +55.19% +67.96% +26.19% +155.00% +70.57% +105.32% +130.69%
42% +17.65% +17.36% +33.08% -7.37% +20.47% +24.54% +43.06% +77.86%
stable and well-performing training strategies. Due to the
limitation of space, we only report the multi-stage results
here, more results on learning rate, modality and trained
components can refer the supplementary material.
We divide the training dataset into two categories: basic knowledge data and task format aligned data, aiming to
develop a training pipeline that enables the model to perform stably and effectively on diverse urban tasks. As Figure 5a shows, ‘Three stage: TA→K→Mix’ performs best in
most tasks and maintains reliable performance, surpassing
the default tuning method for MLLMs. We also probe the
effects of the order between knowledge learning and task
alignment in Figure 5b and Figure 5c. We find that in twostage training, K→TA slightly outperforms TA→K. However, when the third mixture learning is added in a twostage training model, having task alignment first achieves
better results, surpassing the models in two-stage training.
We hypothesize that this is because in the two-stage training, the model first learns the foundational knowledge and
then learns how to solve specific tasks. In the three-stage
training, the two-stage model that knowledge learning first
and then task alignment already possesses considerable capabilities, so the impact of mixture training is not significant. However, for two-stage model that completes task
alignment before knowledge learning, mixture learning can
enhance its abilities, allowing it to recall how to solve urban
tasks learned previously.
On the whole, the proposed three-stage training pipeline
UTrain integrates cross-modal data to achieve stable training and balanced performance across various urban tasks.
3.4. Model Generalization Study
Here, we show that UrbanLLaVA can be generalized to different data distributions and tasks, which are crucial for

0.8
0.6
0.4
0.2
0.0
TrajPredic
N
t avigatio
S
n AT-Addre
S
ss ceneFun
C
c ameraLoc Others
)%(
ycaruccA
0.8
0.6
0.4
0.2
0.0
TrajPredict Navigatio
S
n
AT-A
One stage: K Three stage: TA K Mix
Two stage: TA K One stage: K + TA
(a) The performance of three-stage tuning, gray
part is the default tuning method for MLLMs.
)%(
ycaruccA
Two stage: K
Two stage: TA
(b) The effects of the
learning and task align
Figure 5. Performance of different training strategies. ‘K’ refers to
mixture learning. ‘One stage: K + TA’ means knowledge learning
means task alignment first then knowledge learning in the second st
learning. The tasks detailed in the table are those with significant
other tasks in UBench with smaller differences.
general urban intelligence. As Table 3 shows, while our
UrbanLLaVA performs well in diverse urban tasks, it also
maintains the original stability in general scenarios, including LLaVA-Bench [30], RealWorldQA [44], and MMVet [50]. The results demonstrate that UrbanLLaVA is competitive in the dimension of various daily-life visual tasks,
real-world spatial understanding and integrated capabilities
which is the base for general urban intelligence.
Table 3. General benchmark results. Rating Score refers to result from the LLM-as-a-judge method with GPT4o. For LLaVABench, scores range from 0 to 100, for MM-Vet, scores range from
0.0 to 1.0. Higher scores indicate better performance.
LLaVA-Bench
Test@General RealWorldQA MM-Vet
(In-the-Wild)
Metric Rating Score ACC Rating Score
VILA1.5-8B 60.75 0.3765 0.3518
Ours-8B 58.95 0.4052 0.3239
Different cities exhibit various natural and artificial features. Thus, the transferability of urban model is important for its application. As Figure 6 shows, apart from
in-domain capabilities empowering and performance improvement after learning, UrbanLLaVA can generalize to
out-of-domain tasks in various cities. Here, we examined
our model trained in the Beijing training set and it exhibits
competitive capabilities when tested on London and New
York benchmarks. We can see from Figure 6, performance
improvements are observed across all tasks in London and
New York. Notably, for challenging aspects such as trajectory and regional tasks, the enhancements are significant,
indicating the presence of similarity structures across cities
that go beyond simple, naive differences.
3.5. Data Ablation Study
Here, we investigate the influences of different data compositions, with results shown in Table 4. As outlined in Sec-

0.8
0.6
0.4
0.2
0.0
s SceneFunc CameraLoc Others TrajPredic
N
t avigatio
S
n AT-Addre
S
ss ceneFun
C
c ameraLoc Others
One stage: K + TA
r between knowledge
in two-stage tuning.
)%(
ycaruccA
Three stage: K TA Mix One stage: K + TA
Three stage: TA K Mix
(c) The effects of the order between knowledge
learning and task alignment in three-stage tuning.
wledge learning, ‘TA’ refers to task alignment, and ‘Mix’ refers to
task alignment are merged in the same stage. ‘Two stage: TA→K’
‘Three stage: TA→K→Mix’ adds a step in the third stage: mixture
erences across different training strategies, while ‘Others’ refers to
tion 2.1, the urban instruction data is divided into three different subsets: local view, trajectory view, and global view.
We remove each subset individually and observe the resulting performance differences. Local view: It consists of textual urban geography denoted as CityQA and street view related data denoted as STV. Local view data is important for
different tasks requiring intelligence about a local part of
cities. Noticeable deterioration is observed in both singlemodal and multi-modal tasks, indicating the importance of
locality knowledge for overall urban understanding. Trajectory view: It describes the knowledge about continuous spaces in urban areas. It contains text-trajectory (random walk routing and real-world trajectories) and visualtrajectory( visual-language navigation instructions and random walk with visual input). Both text and multi-modal
trajectory view datasets are essential for navigation task. It
is also shown that trajectory view data is helpful for different tasks like SceneFunc and GeoQA. Global view: It includes a subset of single satellite images that focus on urban
knowledge from a specific area, as well as a subset of multiple satellite images that highlight the correlations between
different regions and cross alignment between satellite and
street view images. Results show that they are essential to
empower MLLM to handle urban tasks from a global view,
e.g, ImgRetrieval and CameraLoc, while local capabilities
are already competitive.
3.6. Case Study
Here, we show two typical examples of urban task instances
to demonstrate that UrbanLLaVA can handle challenging
urban tasks. Due to space limits, other cases can refer to
supplementary materials.
SceneFunc. This task challenges the model to identify
which satellite image contains the highest concentration of
a specified category of places of interest (POIs). Involving multiple image inputs and text prompts, SceneFunc task
demands the model to understand and compare the differ-

0.8
0.6
0.4
0.2
0.0 GeoQA TrajPredict STV-Address STV-Landmark SAT-Address SAT-Land
erocS
ecnamrofreP
Beijing (Baseline) Beijing (Ours) London (Basel
Figure 6. Learning from one city (Beijing) can be directly general
VILA1.5-8b, and our UrbanLLaVA is only trained with the urban i
Table 4. Ablation results on different urban instruction data compo
significant differences are denoted. For TrajPredict task, the thresh
using the one-stage strategy to optimize experimental efficiency.
Task Data View GeoQA TrajPredict Address Landmark Address
Metric Avg. Acc Acc@1 Acc Acc Acc
Ours - 0.5741 0.0711 0.8550 0.8750 0.7450
w/o CityQA Local 0.5409 0.0822 ↑ 0.8700 0.8900 0.7150
w/o STV Local 0.5192 ↓ 0.0622 0.4300 ↓ 0.7300 ↓ 0.4700 ↓
w/o Traj-Text&Nav Trajectory 0.4769 ↓ 0.0644 0.8100 0.8800 0.6350 ↓
w/o Traj-Vision Trajectory 0.5590 0.0690 0.8350 0.9050 0.7300
w/o SAT-Single Global 0.5345 0.0778 0.8600 0.9100 0.5550 ↓
w/o SAT-Multi Global 0.5420 0.0778 0.8500 0.8700 0.6200 ↓
SceneFunc
Image Inputs:
Prompt: In the provided four satellite images in urban area, which image probably
shows most POIs (For example, ['restaurants', 'bakerys', 'foods', 'fast_foods',
'beveragess', 'food_courts', 'bars', 'cafes', 'coffees', 'vending_machines', 'nightclubs’])?
A. The first image <image> B. The second image <image>
C. The third image <image> D. The fourth image <image>
Only provide one letter as the answer and please select your answer from A, B, C, or D.
Reference: C VILA1.5-8B: A Explanation: The third image depicts a commercial area.
In contrast to residential or sparse offices, it is likely to
Ours: C GPT-4o mini : C
have a higher concentration of food-related businesses.
Figure 7. An example of the SceneFunc task, where correct answers are in green, wrong ones in red.
ences between different images. As shown in Figure 7,
while VILA1.5-8B fails to answer the question, our UrbanLLaVA succeeds in giving the correct answer. Our model
exhibits strong capabilities like multiple image understanding and comparison in this example, and is competitive with
the successful closed-source model.
STV-Outlier. This task requires model to compare between multiple street views and point out the closest one to
a reference. Figure 8 shows an instance of this task, where
VILA1.5-8B does not successfully identify the scene of the
reference image. GPT-4o-mini is closer, but it is still confused by another wrong option. Our model shows its capabilities of understanding multiple images and conducting
high-level implicit logical reasoning in an urban context,
outperforming these general MLLMs.

London (Ours) New York (Baseline) New York (Ours)
vigation STV-Outlier SceneComp SceneFunc ImgRetrieval CameraLoc
to other cities (London and New York). In this figure, Baseline is
uction data from Beijing.
ns. The arrows indicate corresponding comparison with ours. Only
is 1%, for other tasks, the threshold is 5%. All models are trained
dUse Navigation STV-Outlier SceneComp SceneFunc ImgRetrieval CameraLoc
cc Success Rate Acc Acc Acc Acc Acc
850 0.3600 0.7800 0.5500 0.5050 0.7300 0.5100
50 ↓ 0.4000 0.8050 0.5400 0.5200 0.7750 0.5200
00 ↓ 0.4200 ↑ 0.6700 ↓ 0.4900 ↓ 0.4550 ↓ 0.6250 ↓ 0.4250 ↓
50 ↓ 0.0000 ↓ 0.7600 0.4950 ↓ 0.4300 ↓ 0.6800 ↓ 0.4600 ↓
00 ↓ 0.3000 ↓ 0.8000 0.5150 0.4650 0.7150 0.4950
50 ↓ 0.3800 0.7800 0.5150 0.4100 ↓ 0.7200 0.4800
00 ↓ 0.3400 0.6450 ↓ 0.3500 ↓ 0.3400 ↓ 0.3950 ↓ 0.2600 ↓
STV-Outlier
Image Inputs:
Prompt: You are given one reference image <image>\n and four options. Which option
image is taken most close to the reference?
A.The First image <image> B.The Second image <image>
C.The Third image <image> D.The fourth image <image>
Only provide one letter as the answer and please select your answer from A, B, C, or D.
Reference: D Explanation: The reference displays a city
Ours: D VILA1.5-8B: B road image with a bike lane. The fourth
image shows a similar scene while the others
GPT-4o mini: A lack features like bike lane or sidewalks.
Figure 8. An example of the STV-Outlier task.
4. Related Work
4.1. Multi-modal Large Language Model
Since the success of GPT4-V [39], MLLM [49] have become a major area of focus in research community, exemplified by the development of models like the LLaVA [30, 31],
VILA [29], QwenVL [41] and InternVL [7, 8]. One of
the most promising solution to develop advanced MLLM
is constructing diverse and high-quality instruction dataset.
For example, LLaVA [31] use GPT4-V to create visual instruction tuning data, leading to the training of the first open
source MLLM. Following LLaVA, VILA [29] explore the
effects of training pipelines and data formats during the pretraining stage. ShareGPT4v [6] further expand data scale by
developing a superb caption model trained on high-quality
caption data from GPT4-V. While general MLLM demonstrate strong visual understanding and reasoning capabili-

ties [9, 21, 43, 47] in common scenarios, they often face
challenges in many specialized fields such as medical applications and remote sensing tasks. Thus, domain-specific
multi-modal large language models [42] are proposed, such
as, Dolphins [34] for autonomous driving, GeoChat [26] for
remote sensing tasks, and various models for medical application [23]. In this paper, we propose the first MLLM for
urban intelligence which can handle various data and diverse tasks in urban field.
4.2. Multi-modal Model for Urban Study
Urban research is an interdisciplinary field that exists multimodal data sources [10, 17, 35, 53, 57], including structured
geospatial data [2], spatiotemporal series data [57], remote
sensing data [35, 55] and street view data [3, 14, 54]. Inspired by the recent advances of MLLMs, researchers explore their potential in urban studies. For structured geospatial data, Balsebre et al. [1] and Feng et al. [16] propose
various methods to convert structured geospatial data into
a language-compatible format to enhance the geospatial
knowledge of large language models. For remote sensing
data [24, 33, 37, 51], Kuckreja et al. [26] and Zhang et
al. [52] design various remote sensing instruction data to
fine-tune general MLLMs for various downstream remote
sensing tasks. For street view data, Hao et al. [22] finetune CLIP model for improved urban indicator prediction
by integrating street view data and remote sensing data. Liu
et al. [32] evaluate the potential of multi-modal language
model for urban socioeconomic sensing. For spatiotemporal series data, Li et al. [28] and Gong et al. [20] introduce
domain-specific encoders to enhance LLM capabilities for
spatiotemporal series modeling. Feng et al. [15] propose
agentic framework to unleash the power of LLM for zeroshot mobility prediction. Unlike these works that focus on
limited data types and specific tasks, our method is designed
to process all these data types and address a wide range of
urban tasks.
5. Conclusion
In this paper, we propose UrbanLLaVA, a MLLM with enhanced urban spatial cognition by integrating four types of
urban data and supporting a wide range of urban tasks. Our
approach begin with the development of diverse and highquality urban instruction data, spanning from local view to
global view of urban environment. We then design a threestage training pipeline to ensure the stable training and improved performance of model on diverse urban tasks. Experimental results from three cities on an extended urban
benchmark highlight the effectiveness of UrbanLLaVA for
integrating multi-modal urban data and solving urban tasks.
In summary, UrbanLLaVA sheds lights for building the unified foundation model with powerful perception and reasoning abilities for general urban intelligence.

6. Limitation and Future Work
While we have made every effort to explore UrbanLLaVA and present our findings clearly, several limitations
remain. Our experiments have focused on the 8B model;
the full potential of UData and UTrain on larger models
has yet to be realized. In addition, UBench can still be
improved by refining the design of tasks, testing MLLMs’
overall multi-modal capabilities from a more fine-grained
perspective. Lastly, more modalities could be included like
video, time series data, etc., which are also important in
urban intelligence. In the future, we plan to extend UrbanLLaVA to incorporate more diverse data types in urban research and tackle more advanced urban tasks from various
interdisciplinary fields.
References
[1] Pasquale Balsebre, Weiming Huang, and Gao Cong.
Lamp: A language model on the map. arXiv preprint
arXiv:2403.09059, 2024. 1, 3, 9
[2] Pasquale Balsebre, Weiming Huang, Gao Cong, and Yi Li.
City foundation models for learning general purpose representations from openstreetmap. In Proceedings of the
33rd ACM International Conference on Information and
Knowledge Management, pages 87–97, 2024. 1, 9
[3] Filip Biljecki and Koichi Ito. Street view imagery in urban
analytics and gis: A review. Landscape and Urban Planning,
215:104217, 2021. 9
[4] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen
Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding,
Danny Driess, Avinava Dubey, Chelsea Finn, et al. Rt-2:
Vision-language-action models transfer web knowledge to
robotic control. arXiv preprint arXiv:2307.15818, 2023. 2
[5] Howard Chen, Alane Suhr, Dipendra Misra, Noah Snavely,
and Yoav Artzi. Touchdown: Natural language navigation and spatial reasoning in visual street environments.
In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 12538–12547, 2019.
4
[6] Lin Chen, Jinsong Li, Xiaoyi Dong, Pan Zhang, Conghui
He, Jiaqi Wang, Feng Zhao, and Dahua Lin. Sharegpt4v:
Improving large multi-modal models with better captions.
arXiv preprint arXiv:2311.12793, 2023. 3, 8
[7] Zhe Chen, Weiyun Wang, Hao Tian, Shenglong Ye, Zhangwei Gao, Erfei Cui, Wenwen Tong, Kongzhi Hu, Jiapeng
Luo, Zheng Ma, et al. How far are we to gpt-4v? closing
the gap to commercial multimodal models with open-source
suites. arXiv preprint arXiv:2404.16821, 2024. 5, 8
[8] Zhe Chen, Jiannan Wu, Wenhai Wang, Weijie Su, Guo
Chen, Sen Xing, Muyan Zhong, Qinglong Zhang, Xizhou
Zhu, Lewei Lu, et al. Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks.
In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 24185–24198, 2024.
5, 8

[9] An-Chieh Cheng, Hongxu Yin, Yang Fu, Qiushan Guo, Ruihan Yang, Jan Kautz, Xiaolong Wang, and Sifei Liu. Spatialrgpt: Grounded spatial reasoning in vision language model.
arXiv preprint arXiv:2406.01584, 2024. 9
[10] Jingtao Ding, Yunke Zhang, Yu Shang, Yuheng Zhang, Zefang Zong, Jie Feng, Yuan Yuan, Hongyuan Su, Nian Li,
Nicholas Sukiennik, et al. Understanding world or predicting future? a comprehensive survey of world models. arXiv
preprint arXiv:2411.14499, 2024. 9
[11] Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi
Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, and
Bowen Zhou. Enhancing chat language models by scaling high-quality instructional conversations. arXiv preprint
arXiv:2305.14233, 2023. 5
[12] Guanting Dong, Hongyi Yuan, Keming Lu, Chengpeng Li,
Mingfeng Xue, Dayiheng Liu, Wei Wang, Zheng Yuan,
Chang Zhou, and Jingren Zhou. How abilities in large language models are affected by supervised fine-tuning data
composition. arXiv preprint arXiv:2310.05492, 2023. 4
[13] Haodong Duan, Junming Yang, Yuxuan Qiao, Xinyu Fang,
Lin Chen, Yuan Liu, Xiaoyi Dong, Yuhang Zang, Pan Zhang,
Jiaqi Wang, Dahua Lin, and Kai Chen. Vlmevalkit: An opensource toolkit for evaluating large multi-modality models,
2024. 5
[14] Zhuangyuan Fan, Fan Zhang, Becky PY Loo, and Carlo
Ratti. Urban visual intelligence: Uncovering hidden city profiles with street view images. Proceedings of the National
Academy of Sciences, 120(27):e2220417120, 2023. 1, 9
[15] Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. Agentmove: A large language model based agentic framework for
zero-shot next location prediction. In Proceedings of the
2025 Conference of the Nations of the Americas Chapter
of the Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers), pages
1322–1338, 2025. 9
[16] Jie Feng, Tianhui Liu, Yuwei Du, Siqi Guo, Yuming Lin,
and Yong Li. Citygpt: Empowering urban spatial cognition
of large language models. In Proceedings of the 31th ACM
SIGKDD International Conference on Knowledge Discovery
and Data Mining, 2025. 2, 3, 9
[17] Jie Feng, Jinwei Zeng, Qingyue Long, Hongyi Chen, Jie
Zhao, Yanxin Xi, Zhilun Zhou, Yuan Yuan, Shengyuan
Wang, Qingbin Zeng, et al. A survey of large language
model-powered spatial intelligence across scales: Advances
in embodied agents, smart cities, and earth science. arXiv
preprint arXiv:2504.09848, 2025. 9
[18] Jie Feng, Jun Zhang, Tianhui Liu, Xin Zhang, Tianjian
Ouyang, Junbo Yan, Yuwei Du, Siqi Guo, and Yong Li. Citybench: Evaluating the capabilities of large language models
for urban tasks. In Proceedings of the 31th ACM SIGKDD
International Conference on Knowledge Discovery and Data
Mining, 2025. 5
[19] Rohit Girdhar, Alaaeldin El-Nouby, Zhuang Liu, Mannat
Singh, Kalyan Vasudev Alwala, Armand Joulin, and Ishan
Misra. Imagebind: One embedding space to bind them all.
In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 15180–15190, 2023.
2

[20] Letian Gong, Yan Lin, Xinyue Zhang, Yiwen Lu, Xuedi Han,
Yichen Liu, Shengnan Guo, Youfang Lin, and Huaiyu Wan.
Mobility-llm: Learning visiting intentions and travel preferences from human mobility data with large language models.
arXiv preprint arXiv:2411.00823, 2024. 1, 2, 9
[21] Qiushan Guo, Shalini De Mello, Hongxu Yin, Wonmin
Byeon, Ka Chun Cheung, Yizhou Yu, Ping Luo, and Sifei
Liu. Regiongpt: Towards region understanding vision language model. In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition, pages 13796–
13806, 2024. 9
[22] Xixuan Hao, Wei Chen, Yibo Yan, Siru Zhong, Kun Wang,
Qingsong Wen, and Yuxuan Liang. Urbanvlp: A multigranularity vision-language pre-trained foundation model for
urban indicator prediction. arXiv preprint arXiv:2403.16831,
2024. 9
[23] Iryna Hartsock and Ghulam Rasool. Vision-language models
for medical report generation and visual question answering:
A review, 2024. 9
[24] Yuan Hu, Jianlong Yuan, Congcong Wen, Xiaonan Lu, and
Xiang Li. Rsgpt: A remote sensing vision language model
and benchmark. arXiv preprint arXiv:2307.15266, 2023. 9
[25] Ming Jin, Shiyu Wang, Lintao Ma, Zhixuan Chu, James Y
Zhang, Xiaoming Shi, Pin-Yu Chen, Yuxuan Liang, YuanFang Li, Shirui Pan, et al. Time-llm: Time series forecasting
by reprogramming large language models. arXiv preprint
arXiv:2310.01728, 2023. 2
[26] Kartik Kuckreja, Muhammad Sohail Danish, Muzammal
Naseer, Abhijit Das, Salman Khan, and Fahad Shahbaz
Khan. Geochat: Grounded large vision-language model
for remote sensing. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition,
pages 27831–27840, 2024. 2, 9
[27] Chunyuan Li, Cliff Wong, Sheng Zhang, Naoto Usuyama,
Haotian Liu, Jianwei Yang, Tristan Naumann, Hoifung Poon,
and Jianfeng Gao. Llava-med: Training a large languageand-vision assistant for biomedicine in one day. Advances in
Neural Information Processing Systems, 36, 2024. 2
[28] Zhonghang Li, Lianghao Xia, Jiabin Tang, Yong Xu, Lei Shi,
Long Xia, Dawei Yin, and Chao Huang. Urbangpt: Spatiotemporal large language models. In Proceedings of the 30th
ACM SIGKDD Conference on Knowledge Discovery and
Data Mining, pages 5351–5362, 2024. 1, 9
[29] Ji Lin, Hongxu Yin, Wei Ping, Pavlo Molchanov, Mohammad Shoeybi, and Song Han. Vila: On pre-training for
visual language models. In Proceedings of the IEEE/CVF
Conference on Computer Vision and Pattern Recognition,
pages 26689–26699, 2024. 4, 5, 8
[30] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae
Lee. Improved baselines with visual instruction tuning.
In Proceedings of the IEEE/CVF Conference on Computer
Vision and Pattern Recognition, pages 26296–26306, 2024.
5, 7, 8
[31] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee.
Visual instruction tuning. Advances in neural information
processing systems, 36, 2024. 2, 8
[32] Tianhui Liu, Jie Feng, Hetian Pang, Xin Zhang, Tianjian
Ouyang, Zhiyuan Zhang, and Yong Li. Citylens: Bench-

marking large language-vision models for urban socioeconomic sensing. arXiv preprint arXiv:2506.00530, 2025. 9
[33] Junwei Luo, Zhen Pang, Yongjun Zhang, Tingzhu Wang,
Linlin Wang, Bo Dang, Jiangwei Lao, Jian Wang, Jingdong
Chen, Yihua Tan, et al. Skysensegpt: A fine-grained instruction tuning dataset and model for remote sensing visionlanguage understanding. arXiv preprint arXiv:2406.10100,
2024. 9
[34] Yingzi Ma, Yulong Cao, Jiachen Sun, Marco Pavone, and
Chaowei Xiao. Dolphins: Multimodal language model for
driving. arXiv preprint arXiv:2312.00438, 2023. 2, 9
[35] Gengchen Mai, Weiming Huang, Jin Sun, Suhang Song,
Deepak Mishra, Ninghao Liu, Song Gao, Tianming Liu, Gao
Cong, Yingjie Hu, et al. On the opportunities and challenges of foundation models for geoai (vision paper). ACM
Transactions on Spatial Algorithms and Systems, 2024. 1, 9
[36] Meta AI. LLaMA 3.2: Advancing Vision, Edge, and Mobile Devices. https://ai.meta.com/blog/llama3 - 2 - connect - 2024 - vision - edge - mobile -
devices/, 2024. Accessed: 2024-11-01. 5
[37] Dilxat Muhtar, Zhenshi Li, Feng Gu, Xueliang Zhang, and
Pengfeng Xiao. Lhrs-bot: Empowering remote sensing
with vgi-enhanced large multimodal language model. arXiv
preprint arXiv:2402.02544, 2024. 9
[38] OpenAI. Introducing chatgpt. https://openai.com/
blog/chatgpt/, 2022. 1
[39] OpenAI. Gpt-4v(ision) system card. 2023. 8
[40] OpenAI. Hello GPT-4. https : / / openai . com /
index/hello-gpt-4o/, 2024. 5
[41] Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan,
Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin
Ge, et al. Qwen2-vl: Enhancing vision-language model’s
perception of the world at any resolution. arXiv preprint
arXiv:2409.12191, 2024. 5, 8
[42] Jiannan Wu, Muyan Zhong, Sen Xing, Zeqiang Lai,
Zhaoyang Liu, Wenhai Wang, Zhe Chen, Xizhou Zhu, Lewei
Lu, Tong Lu, et al. Visionllm v2: An end-to-end generalist multimodal large language model for hundreds of visionlanguage tasks. arXiv preprint arXiv:2406.08394, 2024. 9
[43] Penghao Wu and Saining Xie. V*: Guided visual search as
a core mechanism in multimodal llms. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, pages 13084–13094, 2024. 9
[44] XAI Organization. RealworldQA Dataset.
https : / / huggingface . co / datasets / xai -
org/RealworldQA, 2024. Accessed: 2024-10-01. 5, 7
[45] Zhaomin Xiao, Eduardo Blanco, and Yan Huang. Analyzing large language models’ capability in location prediction.
In Proceedings of the 2024 Joint International Conference
on Computational Linguistics, Language Resources and
Evaluation (LREC-COLING 2024), pages 951–958, 2024.
1
[46] Fengli Xu, Jun Zhang, Chen Gao, Jie Feng, and Yong Li. Urban generative intelligence (ugi): A foundational platform
for agents in embodied city environment. arXiv preprint
arXiv:2312.11813, 2023. 1

[47] Fengli Xu, Qianyue Hao, Zefang Zong, Jingwei Wang,
Yunke Zhang, Jingyi Wang, Xiaochong Lan, Jiahui Gong,
Tianjian Ouyang, Fanjin Meng, et al. Towards large reasoning models: A survey of reinforced reasoning with large
language models. arXiv preprint arXiv:2501.09686, 2025. 9
[48] Dingqi Yang, Daqing Zhang, and Bingqing Qu. Participatory cultural mapping based on collective behavior
data in location-based social networks. ACM Transactions
on Intelligent Systems and Technology (TIST), 7(3):1–23,
2016. 3
[49] Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun,
Tong Xu, and Enhong Chen. A survey on multimodal large
language models. arXiv preprint arXiv:2306.13549, 2023. 1,
3, 8
[50] Weihao Yu, Zhengyuan Yang, Linjie Li, Jianfeng Wang,
Kevin Lin, Zicheng Liu, Xinchao Wang, and Lijuan Wang.
Mm-vet: Evaluating large multimodal models for integrated capabilities. In International conference on machine
learning. PMLR, 2024. 5, 7
[51] Yang Zhan, Zhitong Xiong, and Yuan Yuan. Skyeyegpt:
Unifying remote sensing vision-language tasks via instruction tuning with large language model. arXiv preprint
arXiv:2401.09712, 2024. 9
[52] Wei Zhang, Miaoxin Cai, Tong Zhang, Yin Zhuang, and
Xuerui Mao. Earthgpt: A universal multi-modal large language model for multi-sensor image comprehension in remote sensing domain. IEEE Transactions on Geoscience and
Remote Sensing, 2024. 9
[53] Weijia Zhang, Jindong Han, Zhao Xu, Hang Ni, Hao Liu,
and Hui Xiong. Urban foundation models: A survey.
In Proceedings of the 30th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, pages 6633–6643,
2024. 1, 2, 3, 9
[54] Xin Zhang, Tianjian Ouyang, Yu Shang, Qingmin Liao, and
Yong Li. UrbanMLLM: Joint learning of cross-view imagery
for urban understanding, 2025. 9
[55] Yunke Zhang, Ruolong Ma, Xin Zhang, and Yong Li. Perceiving urban inequality from imagery using visual language
models with chain-of-thought reasoning. In Proceedings of
the ACM on Web Conference 2025, pages 5342–5351, 2025.
9
[56] Baichuan Zhou, Haote Yang, Dairong Chen, Junyan Ye,
Tianyi Bai, Jinhua Yu, Songyang Zhang, Dahua Lin, Conghui He, and Weijia Li. Urbench: A comprehensive benchmark for evaluating large multimodal models in multi-view
urban scenarios. In Proceedings of the AAAI Conference on
Artificial Intelligence, pages 10707–10715, 2025. 5
[57] Xingchen Zou, Yibo Yan, Xixuan Hao, Yuehong Hu,
Haomin Wen, Erdong Liu, Junbo Zhang, Yong Li, Tianrui
Li, Yu Zheng, et al. Deep learning for cross-domain data fusion in urban computing: Taxonomy, advances, and outlook.
Information Fusion, 113:102606, 2025. 1, 2, 3, 9

UrbanLLaVA: A Multi-modal Large L
with Spatial Reasoni
Supplemen
7. Data Example for Three Stages
Below, we provide examples for each stage.
Figure 9. Input data examples for three-stage training.
8. Comparing with models for single-modality
urban tasks
We focus on comparing our approach with these modalityspecific models to better showcase its effectiveness, which
are presented in following Table 5.
Table 5. Comparing with models for single-modality urban tasks.
GeoQA STV-Address STV-Landmark SAT-Address SAT-Landuse
GeoChat 0.3746 0.3100 0.2050 0.2872 0.4650
CityGPT 0.5238 - - - -
UrbanCLIP - - - - 0.3750
Ours 0.5741 0.8550 0.8750 0.7450 0.7850
9. Additional Detailed Results of Three Cities
The detailed results of UBench on three cities are presented
in Table 6, Table 7 and Table 8. Table 2 in Section 3.2
is the aggregated results of these three tables. UrbanLLaVA@Beijing surpasses the baselines in all tasks, showcasing exceptional performance. UrbanLLaVA@London
delivers top results in 9 out of 12 tasks, achieving gains over
the best baseline ranging from 5.17% to 49.38%. Meanwhile, UrbanLLaVA@NewYork performs best in 9 tasks as

nguage Model for Urban Intelligence
g and Understanding
ry Material
well, with improvements over the best baseline spanning
from 6.25% to 122.78%.
10. Additional Results for Training Strategies
As a supplement to results in Section 3.3, we report results
on learning rate, modality and trained components here.
We first adjusted some experimental parameters to explore their effects, and ultimately found that the learning
rate is the key parameter influencing training stability and
model performance. As shown in Figure 10a, we conduct
experiments on the same data with different training parameters, and compared to a learning rate of 1e-4 (the default
choice of VILA), the curve is smoother and lower with a
learning rate of 1e-5. We think training with mixed domainspecific structured instruction data, a lower learning rate
(1e-5) enables the model to handle features from different
modalities more robustly.
Then we consider whether to separate text data and vision data during training to explore the influence of text
data and vision data on training. But as shown in Figure
10b, training with text and vision data in one stage yields
better results compared to the other two experiments and
base model VILA1.5-8B. We also investigated the impact
of training components. As Figure 10c presents, using different components to train the same data shows little difference.
11. Effects of Training Data Size
Fig. 11 presents training results with different amounts, exhibiting the high quality of UData.
12. Effects of Base Model
Our method is model-agnostic and can be generalized to
different MLLMs, e.g., Qwen2.5-VL-7B in Table 9.
13. Effects of Model Size
As Figure 12 shows, performance generally improves with
increasing parameter size for VILA 1.5 (from 3B to 13B).
However, for certain tasks, models of different sizes exhibit
similar capabilities. This occurs either because the tasks are
inherently challenging (e.g., trajectory prediction) or relatively easy (e.g., SAT-Landuse). Compared to VILA1.58B, the performance improvement of VILA1.5-13B is minimal, likely due to the capabilities of the LLaMA3-8B and
LLaMA2-13B models utilized by VILA1.5. However, due

3.0
2.5
2.0
1.5
1.0
0.5
0 500 1000 1500 2000 2500
Training iteration
ssoL
0.8
1e-4
0.6
1e-5
0.4
0.2
0.0
GeoQA SAT-Address
(a) The changes in training loss under the settings
of learning rates 1e − 4 and 1e − 5.
erocS
ecnamrofreP
VILA1.5-8B
One stage: text
(b) Results on UBenc
into text data and visio
Figure 10. (a) illustrates that the training loss is smoother and lowe
‘One stage: text’ means training with text data, ‘Two stage: text→v
the second stage, ‘One stage: text+vision’ means training with tex
(c) ‘T’ refers to Text data, ‘V’ refers to Vision data and ‘T-LLM-P
the first stage, later vision data with LLM and Projector.
Table 6. Main results on UBench at Beijing. UrbanLLa
GeoQA Geo+Traj Geo+STV
Tasks@Beijing
GeoQA TrajPredict Navigation STV-Address STV-Landma
Qwen2VL-7B 0.4950 0.0978 0.18 0.440 0.755
Qwen2VL-72B 0.5491 0.0822 0.24 0.410 0.785
InternVL2-8B 0.4709 0.0957 0.22 0.420 0.755
InternVL2-26B 0.4877 0.0756 0.22 0.440 0.755
VILA1.5-3B 0.3873 0.0000 0.04 0.270 0.655
VILA1.5-8B 0.4322 0.0578 0.06 0.270 0.650
VILA1.5-13B 0.4410 0.0511 0.18 0.305 0.715
LLaMA3.2-11B 0.4229 0.0711 0.08 0.280 0.595
LLaMA3.2-90B 0.4502 0.0711 0.14 0.295 0.770
GPT4o-mini 0.4542 0.0844 0.24 0.280 0.765
GPT4o 0.5479 0.0844 0.22 0.405 0.775
UrbanLLaVA-VILA1.5-8B 0.5682 0.1000 0.46 0.91 0.870
vs. VILA1.5-8B +31.47% +73.10% +666.67% +237.04% +33.85%
vs. Best Baseline +3.48% +2.28% +91.67% +106.82% +10.83%
0.8
0.6
0.4
0.2
10 50 100
Training Data Used (%)
erocS
GeoQA
Geo+Traj
Geo+STV
Geo+SAT
Geo+SS
MMScore
Figure 11. Scaling law from training data size to performance.
to limited computing resources, we were unable to provide
results for VILA1.5-40B, which could potentially achieve
significantly better performance than VILA1.5-8B.
14. Additional Case Study
SAT-LandUse. This task needs a model to speculate the
land use type (commercial, residential, agricultural, etc.)
based on a satellite image. One example is shown in Figure 13. Our UrbanLLaVA can respond to this task precisely,
showing the capability of correctly perceiving the given im-

0.8
0.6
0.4
0.2
0.0
anduse SceneFunc CameraLoc GeoQA Geo+Traj Geo+STV Geo+SAT Geo+SS
Two stage: text vision
One stage: text + vision
hen UData is divided
a.
erocS
ecnamrofreP
T-LLM-Proj V-LLM-Proj T-LLM V-LLM
T-LLM V-LLM-Proj
(c) Results on UBench from experiments using
different training components.
en the learning rate is 1e − 5 (ours) compared to 1e − 4(VILA). (b)
n’ means training with text data in the first stage then vision data in
visual data in one stage. ‘Others’ refers to other tasks in UBench.
→V-LLM-Proj’ means training text data with LLM and Projector in
significantly outperforms other baselines in every task.
Geo+SAT Geo+SS
V-Outlier SAT-Address SAT-Landuse SceneComp SceneFunc ImgRetrieval CameraLoc
0.1200 0.295 0.405 0.400 0.355 0.275 0.260
0.5500 0.395 0.395 0.335 0.310 0.290 0.305
0.2250 0.295 0.300 0.390 0.340 0.210 0.255
0.1700 0.360 0.375 0.440 0.355 0.230 0.225
0.2650 0.275 0.475 0.295 0.235 0.250 0.265
0.3700 0.225 0.405 0.420 0.345 0.195 0.290
0.5300 0.320 0.320 0.425 0.390 0.270 0.210
/ 0.290 0.325 / / / /
/ 0.295 0.290 / / / /
0.2600 0.350 0.360 0.465 0.345 0.205 0.290
0.1100 0.390 0.420 0.450 0.390 0.315 0.290
0.8150 0.780 0.72 0.585 0.58 0.785 0.62
120.27% +246.67% +77.78% +39.29% +68.12% +302.56% +113.79%
+48.18% +97.47% +51.58% +25.81% +48.72% +149.21% +103.28%
0.8
0.6
0.4
3B 8B 13B
erocS
ecnamrofreP
GeoQA
STV
SAT
Geo + STV
Geo + SAT
Geo + SAT + STV
Figure 12. Results on UrbanLLaVA with different model sizes.
age, satisfactory instruction following, and urban knowledge mastering.
STV-Landmark. A representative example is in Figure 14. In this task, models are required to find out
the closest landmark feature to a given street view, which
needs implicit logical reasoning capability to answer. By
correctly answering a STV-Landmark question, UrbanLLaVA presents its ability to conduct logical reasoning in
a multi-modal context.
SAT-Address. This task needs a model to speculate the
most probable address description based on a satellite image. One example is shown in Figure 15

Table 7. Main results on UBench at London. UrbanLLaVA achie
GeoQA Geo+Traj Geo+STV
Tasks@Beijing
GeoQA TrajPredict Navigation STV-Address STV-Landma
Qwen2VL-7B 0.4991 0.1920 0.12 0.405 0.760
Qwen2VL-72B 0.5802 0.2245 0.24 0.485 0.875
InternVL2-8B 0.4973 0.1694 0.10 0.290 0.810
InternVL2-26B 0.5168 0.1776 0.08 0.380 0.865
VILA1.5-3B 0.4362 0.0000 0.08 0.230 0.305
VILA1.5-8B 0.4841 0.1367 0.04 0.330 0.560
VILA1.5-13B 0.4592 0.1796 0.08 0.430 0.570
LLama3.2-11B 0.4804 0.1959 0.04 0.360 0.440
LLama3.2-90B 0.5659 0.2020 0.20 0.375 0.715
GPT4o-mini 0.5357 0.1755 0.08 0.375 0.835
GPT4o 0.6446 0.2000 0.06 0.580 0.895
UrbanLLaVA-VILA1.5-8B 0.6399 0.1959 0.34 0.610 0.955
vs. VILA1.5-8B +32.20% +43.28% +750.00% +84.85% +70.54%
vs. Best Baseline -0.72% -12.73% +41.67% +5.17% +6.70%
Table 8. Main results on UBench at NewYork. UrbanLLaV
GeoQA Geo+Traj Geo+STV
Tasks@Beijing
GeoQA TrajPredict Navigation STV-Address STV-Landmar
Qwen2VL-7B 0.4567 0.1200 0.22 0.585 0.805
Qwen2VL-72B 0.5273 0.1480 0.36 0.550 0.795
InternVL2-8B 0.4632 0.1260 0.24 0.440 0.780
InternVL2-26B 0.4766 0.1080 0.34 0.490 0.805
VILA1.5-3B 0.3954 0.0000 0.08 0.330 0.745
VILA1.5-8B 0.4575 0.1000 0.14 0.345 0.680
VILA1.5-13B 0.4501 0.1100 0.36 0.375 0.765
LLama3.2-11B 0.4127 0.1000 0.12 0.395 0.645
LLama3.2-90B 0.5234 0.1140 0.20 0.575 0.790
GPT4o-mini 0.5075 0.1240 0.34 0.550 0.880
GPT4o 0.6232 0.1080 0.36 0.740 0.830
CityGPT-V-VILA1.5-8B 0.5773 0.1120 0.50 0.920 0.935
vs. VILA1.5-8B +26.19% +12.00% +257.14% +166.67% +37.50%
vs. Best Baseline -7.36% -24.32% +38.89% +24.32% +6.25%
Table 9. Evaluating generalizability of methods on Qwen2.5VL.
Task Group @ Beijing GeoQA Geo+Traj Geo+STV Geo+SAT Geo+SS
Qwen2.5-VL-7B-Instruct 0.4324 0.2192 0.4467 0.2850 0.2225
+ Finetuned with UData 0.5720↑ 0.1876 0.6833↑ 0.4800↑ 0.3800↑
STV-Address. This task provides a street view image
and needs a model to speculate the most probable address
this image was taken. Figure 16 is an example.
SceneComp. This task provides four satellite remote
sensing images and prompts the model to choose the one
with the most number of buildings. An instance is shown in
Figure 17.
ImgRetrieval. It evaluates capability to map a given
street view image to the corresponding satellite image. An
example is displayed in Figure 18.
CameraLoc. It requires the model to infer which quadrant of a satellite image corresponds to the location where a
given street view image was captured. An example is shown
in Figure 19.

better performance than other baselines in the majority of tasks.
Geo+SAT Geo+SS
V-Outlier SAT-Address SAT-Landuse SceneComp SceneFunc ImgRetrieval CameraLoc
0.1492 0.305 0.550 0.870 0.220 0.270 0.285
0.5525 0.530 0.535 0.420 0.265 0.405 0.245
0.2431 0.315 0.490 0.785 0.315 0.215 0.265
0.2320 0.355 0.490 0.905 0.305 0.215 0.270
0.2320 0.200 0.445 0.295 0.200 0.290 0.255
0.4586 0.305 0.485 0.705 0.335 0.250 0.265
0.4972 0.275 0.350 0.800 0.390 0.275 0.250
/ 0.260 0.500 / / / /
/ 0.385 0.555 / / / /
0.2155 0.390 0.570 0.855 0.340 0.290 0.245
0.1657 0.480 0.610 0.900 0.430 0.320 0.250
0.6851 0.575 0.750 0.955 0.560 0.605 0.260
+49.40% +88.52% +54.64% +35.46% +67.16% +142.00% -1.89%
+24.00% +8.49% +22.95% +5.52% +30.23% +49.38% -8.77%
hieves better performance than other models in most tasks.
Geo+SAT Geo+SS
V-Outlier SAT-Address SAT-Landuse SceneComp SceneFunc ImgRetrieval CameraLoc
.1450 0.455 0.395 0.875 0.315 0.275 0.315
.5550 0.520 0.235 0.470 0.290 0.335 0.320
.2550 0.395 0.135 0.835 0.305 0.245 0.235
.2700 0.495 0.225 0.885 0.290 0.230 0.245
.2450 0.310 0.250 0.280 0.245 0.255 0.230
.4700 0.235 0.160 0.795 0.315 0.260 0.245
.5350 0.325 0.175 0.820 0.290 0.285 0.280
/ 0.295 0.150 / / / /
/ 0.460 0.220 / / / /
.2600 0.415 0.265 0.880 0.350 0.255 0.215
.1600 0.610 0.215 0.930 0.405 0.305 0.275
.6950 0.885 0.880 0.835 0.490 0.645 0.520
47.87% +276.60% +450.00% +5.03% +55.56% +148.08% +112.24%
25.23% +45.08% +122.78% -10.22% +20.99% +92.54% +62.50%
SAT-LandUse
Image Inputs: Prompt: The following is a multiple-choice
question about selecting the most possible
landuse type in the region of a satellite image.
A. Grass B. Residential
C. Garages D. Retail
Please choose the most suitable one among A,
B, C and D as the answer to this question.
Please output the option directly. No need for
explanation.
Reference: B VILA1.5-8B: B Explanation: Dense residential buildings in the
remote sensing image denote the most possible
Ours: B GPT-4o mini: B
land-use type of this area is residential.
Figure 13. An example of the SAT-LandUse task. The correct
answers from model are denoted with green color. The response
from ours is in bold. Explanation is written by human for this
question and answer.
15. Urban Instruction Data
Table 10 provides detailed statistics of UData across three
cities, while Table 11 presents the detailed statistics of the
raw data used to construct UData. Additionally, we present

STV-Landmark
Image Inputs: Prompt: The following is a multiple-choice
question about selecting the most possible nearby
POIs(Place of Interests) or landmarks description
in the region of a street view image.
A. Residential building area.
B. Overpass near commercial buildings.
C. Power transmission lines.
Reference: A VILA1.5-8B: A D. Wudaokou Shopping Center
Ours: A GPT-4o mini: A Please choose the most suitable one among A, B,
C and D as the answer to this question.
Explanation: The sidewalk Please output the option directly. No need for
and apartment building explanation.
indicate that there is a
residential building area nearby.
Figure 14. An example of the STV-Landmark task. The correct
answers from model are denoted with green color. The response
from ours is in bold. Explanation is written by human for this
question and answer.
SAT-Address
Image Inputs: Prompt: The following is a multiple-choice question about selecting
the most appropriate address for a satellite image.
A. The area is characterized by a well-defined square layout…
B. …The eastern side features Zhongguin Village East Road,
which is lined with residential communities…
C. The area is a well-defined square located in Wudaokou, a
vibrant neighborhood in Haidian District, Beijing…
D. …To the north, you will find the prominent Zhongguancun
Hospital, situated along Zhongguancun South Road, which runs
through the area…
Please choose the most suitable one among A, B, C and D as the
answer to this question.
Reference: B Please output the option directly. No need for explanation.
CityGPT-V: B Explanation: The right part of this remote sensing image can
be identify to be a residential community, which echoes with
description of option B.
Figure 15. Example of a SAT-Address task.
STV-Address
Image Inputs:
Prompt: The following is a multiple-choice question about selecting the most appropriate address
for a street view image.
A. Bajiajiayuan, Xisanqi, Houbajia, Haidian District, Beijing, 100192, China
B. Beichen West Road, Chaoyang District, Beijing, 100101, China
C. Building A of Beichen Century Center, 8, Beichen West Road, Chaoyang District, Beijing,
100020, China
D. Nanyitiao of Zhongguancun, Keyu Community, Zhongguancun, Dongsheng, Haidian District,
Beijing, 100190, China
Please choose the most suitable one among A, B, C and D as the answer to this question.
Please output the option directly. No need for explanation.
Reference: B CityGPT-V: B
Figure 16. Example of a STV-Address task.
representative examples of our urban instruction data, as
shown in Figure 20 to Figure 35.

SceneComp
Image Inputs:
Prompt: In the provided four satellite images in urban area, which image shows most buildings?
A. The first image <image> B. The second image <image>
C. The third image <image> D. The fourth image <image>
Only provide one letter as the answer and please select your answer from A, B, C, or D.
Explanation: The reference displays a city road
Reference: A image with a bike lane. The fourth image shows a
CityGPT-V: A similar scene while the others lack features like bike
lane.
Figure 17. An example of a SceneComp task.
ImgRetrieval
Image Inputs:
Prompt: You are given one street view image <image>and four satellite images. Which satellite image
contains the street view image?
A. The first image <image> B. The second image <image>
C. The third image <image> D. The fourth image <image>
Only provide one letter as the answer and please select your answer from A, B, C, or D.
Explanation: The street view image shows several
Reference: C large yet short building, indicating an industrial or
CityGPT-V: C business area. So the third RS image most probably
contains its location.
Figure 18. An example of an ImagRetrieval task.
CameraLoc
Image Inputs:
Prompt: You are given a satellite image <image> and a street view image <image> .You are given a
satellite image and a street view image, and please predict which quadrant the street view image lies in
the satellite image.
A. Top left B. Top right
C. Bottom left D. Bottom right
Only provide one letter as the answer and please select your answer from A, B, C, or D.
Reference: B Explanation: The street view image shows a broad
road with no tall building in view. Thus it is not
CityGPT-V: B likely to be taken in the left or bottom part of this
area.
Figure 19. An example of a CameraLoc task.

User: <image >\n Could you provide a description of the content shown in the arial image.
Assistant: In the 256x256 pixel area, the road network is primarily composed of two main roads: the trunk road
North Roud of Landianchang, which runs from [179, 249] to [178, 247] in a southward direction, and the service
road Road of Kunminghu, extending from [127, 124] to [84, 16], which travels in a generally southwest direction.
Additionally, there is a tertiary road Road of Kunminghu that connects [131, 123] to [127, 124], running parallel to
the service road, and a secondary road North Roud of Landianchang that stretches from [176, 250] to [172, 248],
also heading southward. The area features notable points of interest (POIs), including tickets located at [137, 175]
and attractions at [88, 140]. The distribution of roads indicates a concentration of infrastructure towards the southern
part of the region, particularly along North Roud of Landianchang, which is flanked by various POIs, while Road of
Kunminghu serves as a key access route with a notable presence of attractions nearby, suggesting a vibrant area for
visitors.
Figure 20. An example of global view training instances of Image Content.
5

User: <image >\n You are provided a 256*256 satellite image. What is the landuse type in region [[32, 136], [33,
167], [39, 167], [101, 133], [99, 127], [90, 131], [86, 121], [88, 114], [74, 111], [32, 136]]?
Assistant: Residential
Figure 21. An example of global view training instances of Landuse Inference.
User: <image >\n What is the detailed address of the provided street view image?
Assistant: Tsinghuayuan, Xueyuan Road, Dongsheng, Haidian District, Beijing, 100190, China
Figure 22. An example of local view training instances of Location Address.
6

User: <image >\n What is shown in this street view image? And what related pois could be estimated nearby
Assistant: The image depicts a building partially obscured by lush greenery. The structure appears to be a
single-story building with a flat roof, characterized by a light-colored exterior that suggests a concrete or stucco
material. The roof is lined with a blue trim, which adds a subtle contrast to the overall appearance.
Surrounding the building, dense foliage and various plants create a vibrant green backdrop, indicating a
well-established natural environment. The vegetation is thick, with a mix of taller trees and lower shrubs, suggesting
a sense of seclusion. The building is positioned towards the center of the image, with trees flanking its sides, while a
pathway or road runs along the left side, leading towards the viewer.
The spatial relationship between the building and the surrounding greenery is notable; the building is somewhat
hidden by the dense plants, which extend close to its walls, creating a harmonious blend of man-made and natural
elements. The sunlight filters through the leaves, casting dappled shadows on the ground, enhancing the tranquil
atmosphere of the scene. Overall, the image conveys a sense of quietude and integration with nature.
Figure 23. An example of local view training instances of Image Description.
User: <image >\n What is the landmark in this image? If there is no landmark, please say ’None’.
Assistant: In the street view image, a notable landmark is visible in the background: a pagoda, which is likely part
of the nearby Changchun Garden. The pagoda stands tall among the trees, providing a distinctive silhouette against
the sky, and serves as a navigational reference point for the surrounding area. The road curves gently around the
landmark, with vehicles traveling in both directions, while the nearby buildings, including educational institutions
like the Medical College and Pharmacy College, create a backdrop that emphasizes the pagoda’s prominence in the
landscape. This combination of natural and architectural features highlights the cultural significance of the pagoda
within the urban environment
Figure 24. An example of local view training instances of Landmark Details.
7

User: You are given a satellite image <image>and a st
the street view image lies in the satellite image?
A. Top left
B. Top right
C. Bottom left
D. Bottom right
Please provide a detailed reasoning for your answer. An
Assistant: Step 1: Identify the satellite view image’s ad
of Beijing, featuring a well-organized 5x5 grid of notabl
Park, a central site surrounded by various establishments
Museum of China, enhancing the area’s scientific theme
key telecommunications provider, and the vibrant The R
connects these points, facilitating easy navigation. This
establishments, all within close proximity.
Step 2: Identify the street view image’s address: The stre
50, Datun Road, Chaoyang District, Beijing, 100101, Ch
Step 3: Determine the quadrant where the street view im
located in quadrant C of the satellite view image.”
Figure 25. An example of local view trai

view image <image>, can you predict which quadrant
ve me one letter as your answer in the last sentence.
s: The satellite image is taken in the Chaoyang District
cations. To the north is the Olympic Village Science
irectly east along Datun Road is the National Zoological
oving south on Datun Road, you’ll find China Unicom, a
Parrot Image Agency, adding cultural flair. Datun Road
blends educational, cultural, and commercial
view image is taken at The Red Parrot Image Agency, #
lies in the satellite view image: The street view image is
instances of Cross Modality Reasoning.

Assistant: You are given one street view image <image>and four satellite images. Which satellite image shows the
surroundings of the street view image?
A. The first image <image>
B. The second image <image>
C. The third image <image>
D. The fourth image <image>
Please provide a detailed reasoning for your answer. And give me one letter as your answer in the last sentence.”
Assistant: Step 1: Describe the street view image: The image shows a parking area with various vehicles parked in
a semi-organized manner. In the foreground, cars of different colors, including silver, black, and white, are parked
closely on a paved surface made of large rectangular tiles, indicating moderate occupancy. To the right, a prominent
blue fence encloses a structure, likely a building or series of buildings, contrasting with nearby lush trees. The
background features multi-storied buildings made of brick and concrete, with visible windows, suggesting
residential or commercial use. The parking area is in front of these buildings, with cars facing the blue enclosure.
The short distance between the cars and the fence creates a compact environment. The clear sky suggests a bright
day, enhancing visibility.
Step 2: Recall the address of the street view image: The image is taken at the School of Medicine, Jinchun Road,
Qinghuayuan, Xiwacun, Haidian District, Beijing, 100084, China.
Step 3: Recall the addresses of each possible satellite view image:
...
Step 4: Reason the corresponding satellite view image: The satellite view image corresponding to the street view
image is B
Figure 26. An example of global view training instances of Cross Modality Reasoning.
9

User: <image >\n What is the address of this location?
Assistant: Step 1: Identify the city name. According to
Step 2: Extract the location’s features. From the image,
area, the roads are primarily oriented in a north-south an
facilitating access to various points of interest (POIs). N
institutes and universities, indicating a concentration of e
are strategically located alongside the main north-south
for students and researchers alike. The distribution of ro
thoroughfares connecting key locations. The concentrati
suggests that this area serves as a hub for academic and
placement of POIs create a vibrant environment conduci
Step 3: Identify the location’s address. Based on my obs
Haidian District, Beijing, characterized by a 5x5 layout
Institute of Semiconductors, Chinese Academy of Scien
presence in the region. Directly to the south, Beijing For
backdrop to the area. The main thoroughfare, Beilin Gin
institutions and facilitating easy access. The Xueyuanlu
accessibility of the institutions, with Bajia Village nearb
these educational and research institutions fosters a colla
and scientific endeavors.
Figure 27. An example of global vi

ease think step by step and provide a detailed reasoning.
satellite view image, this image was taken in Beijing.
n observe the following features: In the 256x256 pixel
st-west direction, with significant intersections
bly, the coordinates [116, 40] host both research
cational and research facilities in this region. These POIs
that runs through the area, enhancing their accessibility
in this region is fairly balanced, with a few major
of specific POIs, particularly educational institutions,
arch activities. Overall, the layout of roads and the
o learning and innovation.
ation and knowledge of this region, the area is situated in
features several prominent institutions. To the north, the
occupies multiple locations, creating a significant
y University is also located, providing an educational
Avenue, runs through the region, connecting these
district, where this area is found, enhances the
urther enriching the local community. The proximity of
ative environment, making this area a hub for academic
raining instances of Image Content.

User: <image >\n Please count the number of buildings in this satellite image and provide a detailed reasoning for
your answer.
Assistant: Step 1: Identify the city name: According to the satellite view image, this image was likely taken in
Beijing.
Step 2: Describe the location’s features: From the image, I can observe the following features: In the 256x256 pixel
area, the roads are arranged to facilitate access to various points of interest (POIs) and ensure smooth traffic flow.
The tertiary road, Tianchen West Road, runs vertically from [137, 188] to [137, 171], providing a north-south route
that connects to nearby POIs, including cars located at [47, 155]. The secondary road, Datun Road, extends
horizontally from [174, 211] to [221, 209], serving as a major thoroughfare likely supporting higher traffic volumes
and is near cafes located at [55, 148] and [61, 142]. Additionally, another segment of the tertiary road, Datun Road,
stretches from [162, 187] to [0, 193], indicating a more extensive network that enhances connectivity across the
region. The concentration of cafes near the secondary road suggests a vibrant social scene, while the presence of
cars indicates active transportation throughout the area, particularly along these key roads. Overall, the layout of the
roads and the distribution of POIs create a dynamic environment that caters to both vehicular movement and local
amenities.
Step 3: Provide the location’s address: Based on my observation and knowledge of this region, the area described is
located in the Chaoyang District of Beijing, characterized by a well-organized 5x5 layout. To the north, you will
find Beichen West Road, a prominent thoroughfare, while to the south, Datun North Road runs parallel, providing
easy access to the surrounding locations. The eastern section is defined by Tianchen West Road, which intersects
with various points of interest, including the Beichen Century Center, situated at the northwest corner. This center is
flanked by additional buildings along Beichen West Road, creating a bustling environment. Adjacent to these
landmarks, Datun Road runs through the area, connecting several establishments and enhancing the region’s
accessibility. The overall layout ensures that each location is conveniently reachable, fostering a vibrant community
atmosphere.
Step 4: Count the number of buildings or POIs: There are 5 buildings in this image.”
Figure 28. An example of global view training instances of Cross Modality Reasoning.
11

User: <image >\n What is the address of this location? Please think step by step and provide a detailed reasoning.
Assistant: Step 1: Describe the street view image: This is a street view image depicting a city street scene with a
wide, well-maintained road extending into the distance. On the left side, a prominent orange guardrail runs parallel
to the road, suggesting a separation from a lower area, possibly a sidewalk or a bus stop. The road is dark asphalt,
reflecting the bright sunlight, indicating a clear day. To the right, a series of buildings are visible, showcasing a mix
of architectural styles. The building closest to the viewer is painted in a muted red hue and features several air
conditioning units mounted on its exterior walls. This building appears to be several stories tall, with large windows
that allow for natural light. Further along, a taller, modern glass building stands out, its reflective surface capturing
the sunlight and contrasting with the surrounding structures. This building is flanked by additional high-rise
buildings in the background, creating a skyline that suggests a bustling urban environment. In the distance, road
signs are visible, indicating directions or information for drivers, while the road continues to stretch ahead, leading
towards the horizon. The overall scene conveys a sense of an active city, with a combination of modern architecture
and well-maintained infrastructure. The clear blue sky above enhances the vibrant atmosphere of the setting.
Step 2: Tell the city name: According to the street view image, this is probably in Beijing.
Step 3: Extract the location’s features around: The street view image is taken in a region with the following features:
Beijing Haidian District Vocational School, Haidian District Vocational Technical School East Campus, Hongyun
Laobeiping, Khan Baba, Mi Da Wan, and the Affiliated High School of China University of Geosciences.
Step 4: Tell the location’s address: Based on my observation and knowledge about this region, the address is
Xueyuanlu Subdistrict, Dongsheng, Haidian District, Beijing, 100083, China.”
Figure 29. An example of local view training instances of Cross Modality Reasoning.
12

User: <image >\n The following is a multiple-choice question about selecting the most appropriate address for a
satellite image.
A. The area is characterized by a well-organized layout, featuring a 5x5 grid that offers a variety of attractions and
roadways. To the north, the prominent Yuan Dynasty Capital City Wall Ruins Park serves as a significant landmark,
providing a historical backdrop and recreational space. Adjacent to this park, Beitou City West Road runs east to
west, connecting various points of interest within the vicinity. To the east ...
B. The area is situated in the Huayuanlu Subdistrict of Haidian District, Beijing, characterized by a well-defined
square layout divided into a 5x5 arrangement. To the north, the region is bordered by a series of residential complexes,
including the prominent Beiji Temple Residential Area, which occupies several positions within the grid. To the south
...
C. The area is characterized by a well-organized 5x5 layout, with the northern section primarily featuring Wanquanhe
Road, which runs through the heart of the neighborhood, providing easy access to various points of interest. To the
east, ...
D. The area is located in the Huayuanlu Subdistrict of Haidian District, Beijing, characterized by a well-defined
square layout that is predominantly residential. To the north, you will find a cluster of residential buildings known as
Beiji Temple Residential Area, which extends down the western side of the area. Moving eastward, ...
Please choose the most suitable one among A, B, C and D as the answer to this question.
Please output the option directly. No need for explaination
Assistant: A
Figure 30. An example of global view training instances of Location Address.
13

User: <image >\n The following is a multiple-choice question about selecting the most possible landuse type in the
region of a satellite image.
A. Industrial
B. Residential
C. Meadow
D. Forest
Please choose the most suitable one among A, B, C and D as the answer to this question.
Please output the option directly. No need for explaination.
Assistant: B
Figure 31. An example of global view training instances of Landuse Inference.
14

User: <image >\n The following is a multiple-choice question about selecting the most appropriate address for a
street view image.
A. G6 Auxiliary Road, Chaoyang District, Beijing, 100000, China
B. Old Summer Palace Park, 28, Qinghua West Road, Yanyuan, Haidian Town, Haidian District, Beijing, 100084,
China
C. Piaoliang Sunshine Plaza, Datun, Chaoyang District, Beijing, 100012, China
D. G6 Auxiliary Road, Xueyuanlu Subdistrict, Tayuan Village, Haidian District, Beijing, 100191, China
Please choose the most suitable one among A, B, C and D as the answer to this question.
Please output the option directly. No need for explaination.
Assistant: B
Figure 32. An example of local view training instances of Location Address.
User: <image >\n The following is a multiple-choice question about selecting the most possible nearby POIs(Place
of Interests) or landmarks description in the region of a street view image.
A. Unpaved rural road.
B. Metal fence or wall.
C. Not identifiable.
D. Residential apartment complex.
Please choose the most suitable one among A, B, C and D as the answer to this question.
Please output the option directly. No need for explaination.
Assistant: D
Figure 33. An example of local view training instances of Landmark Details.
15

User: You are given a satellite image <image>and a street view image <image>, and please predict which quadrant
the street view image lies in the satellite image.
A. Top left
B. Top right
C. Bottom left
D. Bottom right
Only provide one letter as the answer and please select your answer from A, B, C, or D.”
ASSITANT: D
Figure 34. An example of global view training instances of Cross View Data.
16

User: You are given one street view image <image>and four satellite images. Which satellite image shows the
surroundings of the street view image?
A. The first image <image>
B. The second image <image>
C. The third image <image>
D. The fourth image <image>
Only provide one letter as the answer and please select your answer from A, B, C, or D.
Assistant: C
Figure 35. An example of global view training instances of Multiple SAT Comparison.
(a) Beijing (b) London (c) New York
Figure 36. Maps for Beijing, London and New York.
17

Table 10. Basic information of UData on three cities.
City Category Dataset Instance Rounds
/ General ShareGPT,UltraChat,Open-Platypus 19866 3.7
Beijing Location View Data CityQA 19271 1
Location Address 93246 1
Landmark Details 51130 1
Image Description 28798 1
Cross Modality Reasoning 2000 1
Trajectory View Data Random Walk 9001 1
Real-World Trajectory 98 1
Visual Random Walk 8936 1
Vision-Language Navigation 3000 1
Global View Data Image Content 9315 1
Location Address 2777 1
Landuse Inference 3642 1
Multiple SAT Comparison 10114 1
Cross-View Data 77204 1
Cross Modality Reasoning 14977 1
London Location View Data CityQA 28934 1
Location Address 2172 1
Landmark Details 2372 1
Image Description 716 1
Cross Modality Reasoning 1286 1
Trajectory View Data Random Walk 16524 1
Real-World Trajectory 98 1
Visual Random Walk 13412 1
Vision-Language Navigation 3000 1
Global View Data Image Content 3853 1
Location Address 882 1
Landuse Inference 4332 1
Multiple SAT Comparison 4500 1
Cross-View Data 2172 1
Cross Modality Reasoning 5758 1
New York Location View Data CityQA 25413 1
Location Address 94886 1
Landmark Details 50404 1
Image Description 24529 1
Cross Modality Reasoning 2012 1
Trajectory View Data Random Walk 12277 1
Real-World Trajectory 98 1
Visual Random Walk 12229 1
Vision-Language Navigation 3000 1
Global View Data Image Content 18368 1
Location Address 5113 1
Landuse Inference 17899 1
Multiple SAT Comparison 22020 1
Cross-View Data 94886 1
Cross Modality Reasoning 23603 1
Table 11. The raw data of the selected region in three cities.
City AoIs PoIs Roads Trajectory Street View Image Satellite Image
Beijing 4647 1882 2320 21015 28798 1533
London 13705 11715 1322 173268 3125 556
New York 19541 11112 522 390934 24444 2738
18
