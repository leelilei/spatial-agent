---
title: "Introduction"
source_pdf: "01_urban_benchmarks\\03_STBench_Wang2024.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:31:15+00:00
page_count: 24
status: ok
text_char_count: 75045
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\01_urban_benchmarks\03_STBench_Wang2024.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:31:15+00:00
- Page count: 24
- Status: ok
- Text chars: 75045
- Quality flags: none

## Metadata

- Title: Introduction
- Author: unknown
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

The rapid evolution of large language models (LLMs) holds promise for reforming the methodology of spatio-temporal data mining. However, current works for evaluating the spatio-temporal understanding capability of LLMs are somewhat limited and biased. These works either fail to incorporate the latest language models or only focus on assessing the memorized spatio-temporal knowledge. To address this gap, this paper dissects LLMs’ capability of spatio-temporal data into four distinct dimensions: knowledge comprehension, spatio-temporal reasoning, accurate computation, and downstream applications. We curate several natural language question-answer tasks for each category and build the benchmark dataset, namely STBench, containing 13 distinct tasks and over 60,000 QA pairs. Moreover, we have assessed the capabilities of 13 LLMs, such as GPT-4o, Gemma and Mistral. Experimental results reveal that existing LLMs show remarkable performance on knowledge comprehension and spatio-temporal reasoning tasks, with potential for further enhancement on other tasks through in-context learning, chain-of-though prompting, and fine-tuning. The code and datasets of STBench are released on https://github.com/LwbXc/STBench.

## Outline

- Introduction (page 1)
- Related Work (page 3)
- Preliminary (page 3)
- Benchmark Construction (page 3)
  - Overview (page 4)
  - Knowledge comprehension (page 4)
  - Spatio-temporal reasoning (page 5)
  - Accurate computation (page 6)
  - Downstream Applications (page 6)
- Experiments (page 6)
  - Experimental setup (page 6)
  - Main results (page 7)
  - In-Context learning evaluation (page 8)
  - Chain-of-thought evaluation (page 9)
  - Fine-tuning Evaluation (page 9)
- Conclusion (page 9)
- Data Format (page 12)
  - Prompt template for chatting models (page 12)
  - Data Examples (page 12)
    - Knowledge comprehension (page 12)
    - Spatio-temporal reasoning (page 15)
    - Accurate computation (page 20)
    - Downstream Applications (page 20)
- Experimental Details (page 22)
  - Evaluated models (page 22)
  - Detailed results (page 22)
    - Basic prompt (page 22)
    - In-context learning (page 23)
    - Chain-of-thought (page 23)
    - Fine-tuning (page 24)

## Markdown Content

STBench: Assessing the Ability of Large Language
Models in Spatio-Temporal Analysis
Wenbin Li1,2, ∗Di Yao1, Ruibo Zhao1,2, Wenjie Chen1,2, Zijie Xu1,2, Chengxue Luo1,2,
Chang Gong1,2, Quanliang Jing1, Haining Tan1, ∗Jingping Bi1
1Institute of Computing Technology, Chinese Academy of Sciences, Beijing, China,
2University of Chinese Academy of Sciences,
{liwenbin20z,yaodi,zhaoruibao23s,chenwenjie23s,xuzijie22s}@ict.ac.cn
{gongchang21z,jingquanliang,tanhaining,bjp}@ict.ac.cn
Abstract
The rapid evolution of large language models (LLMs) holds promise for reforming
the methodology of spatio-temporal data mining. However, current works for
evaluating the spatio-temporal understanding capability of LLMs are somewhat
limited and biased. These works either fail to incorporate the latest language
models or only focus on assessing the memorized spatio-temporal knowledge. To
address this gap, this paper dissects LLMs’ capability of spatio-temporal data into
four distinct dimensions: knowledge comprehension, spatio-temporal reasoning,
accurate computation, and downstream applications. We curate several natural
language question-answer tasks for each category and build the benchmark dataset,
namely STBench, containing 13 distinct tasks and over 60,000 QA pairs. Moreover,
we have assessed the capabilities of 13 LLMs, such as GPT-4o, Gemma and Mistral.
Experimental results reveal that existing LLMs show remarkable performance on
knowledge comprehension and spatio-temporal reasoning tasks, with potential for
further enhancement on other tasks through in-context learning, chain-of-though
prompting, and fine-tuning. The code and datasets of STBench are released on
https://github.com/LwbXc/STBench.
1 Introduction
The rapid advancement of large language models (LLMs) has opened up new possibilities across
various domains [30, 28, 37]. One promising direction is enhancing spatio-temporal data analysis with
the ability of LLMs [18, 17, 19]. Spatio-temporal data, characterized by both spatial and temporal
dimensions, encompasses a variety of datasets crucial for many fields such as geography, meteorology,
transportation, and epidemiology. Despite LLMs’ remarkable proficiency in language-related tasks,
their applicability and effectiveness in handling spatio-temporal data remain relatively unexplored.
Existing evaluations of spatio-temporal data fall in two categorizes. The first category [27, 21, 16]
focus on evaluating the spatial analysis capability of LLMs and design QA pairs of spatial reasoning
such as asking "Is the yellow apple to the west of the yellow watermelon?". The QA pairs are
constructed in toy environments without temporal information, which is insufficient to assess the
ability of LLM on real spatio-temporal tasks. The second category [10, 32] aims to evaluate the
spatio-temporal analysis capability but only assess the abilities of LLMs’ in one specific dimension.
For example, the most recent work [10] tends to evaluate the memory ability of spatio-temporal
knowledge. For a comprehensive evaluation, we argue that the abilities of LLMs in spatio-temporal
analysis should contain not only the memory ability but also other dimensions, such as reasoning,
inference and knowledge comprehension.
∗Corresponding authors.
Preprint. Under review.
4202
nuJ
72
]LC.sc[
1v56091.6042:viXra

Figure 1: Overview of STBench. It consists of 13 distinct tasks covering four dimensions: knowledge
comprehension, spatio-temporal reasoning, accurate calculation and downstream applications.
To achieve this goal, we propose a framework, namely STBench, for evaluating the spatio-temporal
capabilities of LLMs. As shown in Figure 1, STBench dissects the LLMs’ capacity into four distinct
dimensions: knowledge comprehension, spatio-temporal reasoning, accurate computation, and
downstream applications. Knowledge Comprehension examines the model’s capacity to understand
and interpret the underlying meaning and context of spatio-temporal information. Spatio-Temporal
Reasoning evaluates the ability to understand and reason about the spatial and temporal relationships
between entities and events. Accurate Computation handles the precise and complex calculations of
spatio-temporal data. Moreover, we also employ some Downstream Applications such as trajectory
anomaly detection and trajectory prediction to assess the ability of LLMs on practical tasks.
For each evaluated dimension, we design several tasks and construct QA pairs to assess the ability of
LLMs qualitatively. We have curated a benchmark dataset, STBench, which contains over 60,000
QA pairs and 13 distinct tasks covering the four dimensions. Furthermore, we evaluated the latest 13
LLMs, including GPT-4o2, Gemma [20], Llama2 [29], and provide a detailed report that quantitatively
assesses the four dimensional abilities of LLMs. Our experimental results reveal that existing LLMs
show remarkable performance on knowledge comprehension and spatio-temporal reasoning tasks,
with the closed-source LLMs (GPT-4o and ChatGPT3) outperforming other models in many instances.
For example, ChatGPT achieved an accuracy of 79.26% on POI Category Recognition and 83.58%
on Administrative Region Determination, surpassing other evaluated open-source models by 34.6%
and 177.3%, respectively. For accurate computation tasks, performance across all models is generally
low. Moreover, we also reveal the potential of in-context learning and chain-of-thought prompting
in enhancing performance. For example, in-context learning improved ChatGPT’s accuracy on POI
Identification from 58.64% to 76.30%. Similarly, chain-of-thought prompting increased its accuracy
on Urban Region Function Recognition from 39.78% to 52.20%.
The contributions of this paper are summarized as following:
• This paper serves as a comprehensive evaluation of many LLMs on spatio-temporal analysis
and releases a benchmark dataset STBench. By systematically evaluating their performance
across diverse tasks and datasets, we have elucidated the strengths and limitations of LLMs
in the context of spatio-temporal analysis.
• Our findings highlight the remarkable performance of LLMs in knowledge comprehension
and spatio-temporal reasoning tasks, while also identifying areas for improvement in accurate computation and downstream applications. The in-context learning, chain-of-thought
prompting, and fine-tuning are verified to be potential techniques in developing more robust
and capable models.
2https://platform.openai.com/docs/models/gpt-4o
3https://openai.com/blog/chatgpt
2

• For transparency, we have made all the datasets, code, and evaluation methodologies of
STBench openly accessible. We believe that sharing our findings and resources will not
only facilitate reproducibility but also encourage broader engagement and innovation within
the research community.
2 Related Work
The rapid development of large-scale language models has attracted widespread interest from various
communities [36, 14, 35, 15]. Many researchers studied the capabilities of LLMs [4, 6, 5] and some
of them investigated the potential in spatio-temporal mining.
Spatial analysis capabilities. [22] proposed a question-answering (QA) benchmark for spatial
reasoning with natural language texts. [27] presented a QA dataset to evaluate language models’
capability of multi-hop spatial reasoning. [21] provided two datasets about spatial question answering
and spatial role labeling problems. [16] further improved a previous benchmark to provide a more
accurate assessment. However, these works only focus on spatial reasoning in toy environments. They
ignore the temporal dimension and are far from the real scenarios of spatio-temporal applications.
Spatio-temporal analysis capabilities. [12] evaluated the ability of LLMs to represent geometric
shapes and spatial relationships. [23] examines the performance of ChatGPT in a geographic
information systems exam to evaluate its spatial literacy. [25] investigates the geographic capabilities
of GPT-4 [24] through a series of qualitative and quantitative experiments. [10] analyzes the learned
representations of several spatial and temporal datasets by training linear regression probes. [32]
evaluates the ability of LLMs to represent and reason about spatial structures, such as squares and
hexagons. [11] assesses four closed-source LLMs on a set of tasks, primarily focusing on coding
capabilities, such as code interpretation and code generation. These works either only analyze a
specific model or only examine the capabilities of a specific aspect, failing to provide a comprehensive
evaluation of the latest closed-source and open-source LLMs. The most relevant work is [26] which
assesses the geographic and geospatial capabilities of multimodal LLMs. Their tasks are completely
designed for multimodal models and are not applicable to single-modal large language models. To
comprehensively assess the spatio-temporal ability of LLMs, in this paper, we classify the spatialtemporal abilities into four categories and propose a benchmark consisting of over 60,000 QA pairs
based on this. We benchmark 13 latest LLMs to assess their capabilities and to investigate their
potential in spatio-temporal mining.
3 Preliminary
In spatio-temporal data mining, the concepts of Point of Interest (POI), Trajectory, and Region
play a fundamental role in representing and analyzing spatio-temporal data. Before presenting the
construction methodology of our benchmark, we formally define these concepts in this section.
DEFINITION 1 (Point of Interest): A point of interest (POI) is a specific geographic location
p =< i , lat , lon , c , M >, where i is the ID number, lat is the latitude, lon is the longitude,
p p p p p p p p
c denotes the category of this POI and M = {m , m , · · · } is a set of comments about this POI.
p p 1 2
DEFINITION 2 (Trajectory): Each trajectory t =< t
1
, t
2
, · · · > is a sequence of points, where each
point t =< lat , lon , time > is a triplet of latitude, longitude and timestamp.
i i i i
DEFINITION 3 (Region): A region is a defined area that is distinct from its surroundings. Each
region r =< b , c , P > is characterized by its boundary lines b and the region function category
r r r r
c . The set P = {p , p , · · · } denotes the POIs that fall in this region.
r r 1 2
4 Benchmark Construction
In this section, we propose a benchmark, STBench, to assess the ability of LLMs in spatio-temporal
analysis. We will begin by presenting the considerations that guide the design of STBench. Subsequently, we will delve into a detailed exposition of the construction of STBench.
3

Table 1: A prompt template of the samples in STBench. The blue texts describe the question. The
brown texts are the options. The teal texts denote the guidance that constrains the output of LLMs.
Question: Below is the coordinate information and related comments of a point of interest: · · · .
Please answer the category of this point of interest.
Options: (1) xxxx, (2) xxxx, (3) xxxx, · · · .
Please answer one option.
Answer: The answer is option (
4.1 Overview
To construct a benchmark for assessing the ability of LLMs in spatio-temporal data, we should first
consider the evaluation tasks and the data format.
Ability Categories. Choosing or designing appropriate tasks is crucial for assessing the ability of
LLMs in spatio-temporal data mining. Although numerous spatio-temporal tasks, i.e., trajectory
anomaly detection and next POI prediction, already exist, they do not provide a comprehensive
evaluation of the capabilities in spatio-temporal analysis. We classify the requisite abilities into
four categories: knowledge comprehension, spatio-temporal reasoning, accurate computation, and
downstream applications. For each category, we design several tasks for assessment.
Data Format. Another important question is what data format we should adopt. If we directly ask
the model through dialogue and allow open-ended answers, it will bring some problems. Firstly, the
response of LLMs is uncontrolled. For instance, models may only apologize for not being able to
provide an accurate answer, rather than directly responding to our question. Moreover, open-ended
answers make it difficult to identify the final answer of LLMs, e.g., LLMs may reply with a lot of
explanation or even some unrelated content. Therefore, we have LLMs complete the input texts,
rather than asking LLMs through dialogue. As shown in Table 1, each data sample in STBench
consists of three parts: the question, the options and the guidance. The LLMs should continue the
guidance, i.e., they should generate an option number, thus the output is controllable. Note that some
LLMs are chat models and do not support text completion, thus we instruct these models to complete
the texts through system prompts. The details are in Appendix A in the supplementary material.
4.2 Knowledge comprehension
The model’s capacity to understand and interpret the underlying meaning and context of spatiotemporal information is important. This involves the ability to comprehend the semantic nuances
within the data and the knowledge of relevant spatio-temporal concepts and entities, e.g., understanding and distinguishing different POI categories. We provide valuable insights into LLMs’
spatio-temporal knowledge comprehension capabilities through four tasks: POI category recognition,
POI identification, urban region function recognition, and administrative region determination.
POI Category Recognition (PCR). The semantics of POI are crucial in various applications
such as POI recommendation, thus we design this task to evaluate LLM’s understanding of POI
semantics. Data samples of this task are generated based on the public Yelp dataset4. Specifically, we randomly sample some POIs from the Yelp dataset for data construction. For each POI
p =< i , lat , lon , c , M >, we randomly select two comments m , m from the comment
p p p p p i1 i2
set M . Then, LLMs are asked to predict the category c of the POI according to its coordinates
p p
< lat , lon > and the selected comments < m , m >. The POI category c and four other
p p i1 i2 p
randomly sampled POI categories are provided as options.
POI Identification (PI). In this task, the coordinates and comments of two POIs are provided and LLMs are asked to determine if they are the same POI or not. For a POI p =<
i , lat , lon , c , M > in the Yelp dataset, we construct a positive sample (i.e., the answer
p p p p p
is "Yes") and a negative sample based on it. For the positive sample, we ask the model if
< lat , lon , m , m > and < lat + ϵ , lon + ϵ , m , m > describe the same POI, where
p p i1 i2 p 1 p 2 i3 i4
m , 1 ≤ j ≤ 4 are comments sampled from the comment set M and ϵ , ϵ ∼ U (0.0004, 0.0008)
ij p 1 2
are minor disturbances to the coordinates. For negative samples, we construct a KD-Tree and sample
another POI p′ =< i , lat , lon , c , M > from the nearest five neighbors of p. Then, the
p′ p′ p′ p′ p′
4https://www.yelp.com/dataset.
4

negative sample is constructed based on < lat , lon , m , m > and < lat , lon , m , m >,
p p i1 i2 p′ p′ i5 i6
where m , m are comments sampled from the comment set M .
i5 i6 p′
Urban Region Function Recognition (URFR). This task requires LLMs to predict the urban region
function according to the boundary lines and the POIs located in the region, which evaluates LLMs’
understanding of urban regions. To construct data samples, we first match POIs in the Yelp dataset and
regions in the New Orleans region dataset5, removing POIs that do not fall in any region and regions
that contain no more than one POI. After that, for each region r =< b , c , P >, we randomly select
r r r
two POIs {p =< i , lat , lon , c , M > |k = i , i } from its POI set P . For each p , two
comments m k pk , mpk pk are sa p m k pled p f k rom pk the co p m k ment set M 1 2 , where k ∈ i , i . T r hen, we ask k LLMs
1 2 pk 1 2
to predict the region function c according to its boundary lines b , the coordinates and comments of
r r
the selected POIs, i.e., {< lat , lon , mpk , mpk > |k = i , i }. We provide the region function c
pk pk 1 2 1 2 r
and four other region function categories as options.
Administrative Region Determination (ARD). This task refers to determining which administrative
region a coordinate is located in, which involves relevant knowledge of the administrative regions and
the ability to associate it with geographical coordinates. For a POI p =< i , lat , lon , c , M > of
p p p p p
the Yelp dataset located in city , LLMs are asked to answer which city < lat , lon > is located in.
p p p
city along with other four cities in the same state are provided as options.
p
4.3 Spatio-temporal reasoning
Spatio-temporal reasoning encompasses the ability to understand and reason about the spatial and
temporal relationships between entities and events. For example, given a POI and some regions, LLMs
should determine which region the POI falls in according to their coordinates and boundary lines.
We design four tasks to assess the spatio-temporal reasoning ability of large language models: pointtrajectory relationship detection, point-region relationship detection, trajectory-region relationship
detection and trajectory identification.
Point-Trajectory Relationship Detection (PTRD). The task is to determine whether a trajectory
passes through a point. To generate a data sample, we downsample the trajectory in the public
Xi’an dataset6 into a shorter trajectory t = {t , · · · , t } and construct five points as options. We
1 n
take < (lat + lat )/2, (lon + lon )/2 > as the true option, where < lat , lon > and
i i+1 i i+1 i i
< lat , lon > are two adjacent points in the trajectory. To construct an error option, we sample
i+1 i+1
a point t =< lat , lon , time > from the trajectory and perturb its coordinates with Gaussian
j j j j
noise, i.e., the error option is < lat + ϵ , lon + ϵ >, where ϵ , ϵ ∼ N (0.01, 0.001).
j 1 j 2 1 2
Point-Region Relationship Detection (PRRD). Given a point and several regions, this task aims
to infer which region the point falls in. To generate a data sample, we select i regions {r , · · · , r }
1 i
located in the same city from the EULUC dataset [9]. Then, a region r is chosen from these i regions
j
and we randomly selected a point p in region r . The coordinates of point p and the boundary lines
j
of i regions are used to generate the question texts, and all i regions are provided as options. We
construct four sub-datasets by varying the value of i from 2 to 5.
Trajectory-Region Relationship Detection (TRRD). Given a trajectory and some regions, this task
aims to determine which regions the trajectory has passed through chronologically. To construct a
data sample, we randomly select five regions {r , · · · , r } located in the same city from the EULUC
1 5
dataset and generate a trajectory t by a random walk. The region sequence that t passes through and
four randomly generated region sequences are provided as options. We construct five sub-datasets by
setting the length of t to 2, 4, 6, 8 and 10, respectively.
Trajectory Identification (TI). In this task, we ask LLMs to determine if two point sequences
t′ and t′′ are sampled from the same trajectory. We propose two strategies to construct positive
samples (i.e., samples with the answer "Yes") and two strategies to construct negative samples.
Specifically, for a trajectory t =< t , t , · · · > in the Xi’an dataset, we construct two positive
1 2
samples through downsampling and staggered sampling. For instance, the downsampling strategy
use t′ =< t , t , t , · · · > and t′′ =< t , t , t , · · · > to generate the question, while the staggered
1 2 3 1 3 5
sampling strategy use t′ =< t , t , t , · · · > and t′′ =< t , t , t , · · · > to generate the question. To
1 3 5 2 4 6
5https://catalog.data.gov/dataset/zoning-district-9939c
6https://gaia.didichuxing.com/
5

construct negative samples, we downsample a tr
offsets to t′ to obtain t′′.
4.4 Accurate computation
In the context of handling spatial-temporal data,
on the model’s capability to perform precise an
data. We include two tasks that challenge the mo
assessment: direction determination and trajecto
Direction Determination (DD). This task is to
points. To create a data sample, two POIs are ran
is asked to calculate the corresponding azimut
on the calculation result. Eight options are pro
northeast, northwest, southeast and southwest.
Trajectory-Trajectory Relationship Analysi
times two trajectories encounter each other. To c
t =< t , · · · , t > and t′ =< t′ , · · · , t′ > thr
1 n 1 n
it as an encounter if t t and t′ t′ intersect i
i i+1 j j+1
We provided the ground truth and other four wr
4.5 Downstream Applications
Downstream tasks require the model to not on
apply this understanding to practical applicatio
downstream tasks: trajectory anomaly detection
Trajectory Anomaly Detection (TAD). In ord
infer the underlying route and shape from trajec
as normal and perform detours to generate an
t =< t , · · · , t >, we identify the direction p
1 n
move the middle one-third of the trajectory alon
Trajectory Classification (TC). This task req
coordinates, length, speed and other relevant in
construct dataset for this task based on the Geo
LLMs, we downsample each trajectory and ask
options are provided: bike, car and pedestrian.
Trajectory Prediction (TP). This task is to pred
trajectory involves the ability to model the traject
samples for this task based on the trajectories in
the each trajectory with a time interval of 30 seco
we ask LLMs to predict the coordinates of t a
j
where 3 ≤ j ≤ n. Note that we do not provide o
5 Experiments
We conduct extensive experiments on STBench
to investigate if in-context learning, chain-of-tho
5.1 Experimental setup
Evaluated models. We evaluate the perform
and GPT-4o, and a set of open-source mode
ChatGLM2, ChatGLM3, [8, 34], Mistral [13
More introduction to these models can be found
7https://www.microsoft.com/en-us/research/publi
8https://lmsys.org/blog/2023-03-30-vicuna/

tory t into t′ and add temporal offsets or spatial
urate computation plays a pivotal role. It focuses
omplex calculations related to spatial-temporal
’s accuracy in spatial-temporal computations for
rajectory relationship detection.
ermine the direction between two geographical
mly chosen from the Yelp dataset, and the model
nd to determinate their relative direction based
ed for all data samples: north, south, west, east,
TRA). This task is to calculate the number of
truct a data sample, we generate two trajectories
h random walks within a certain area. We count
ace and overlap in time, where 1 ≤ i, j ≤ n − 1.
answers as options.
nderstand the spatial-temporal context but also
We assess this aspect of LLMs through three
jectory classification and trajectory prediction.
to detect anomalous trajectories, LLMs should
y data. We consider trajectories in Xi’an dataset
alous samples. Specifically, given a trajectory
endicular to the line connecting t and t , and
1 n
is direction to generate an anomalous sample.
es the model to comprehensively consider the
mation to distinguish different trajectories. We
dataset7. Due to the input length limitation of
Ms to infer what generates the trajectory. Three
the next point based on the historical points of a
patterns and the moving speed. We construct data
Xi’an dataset. Specifically, we first downsample
Then, for each trajectory t =< t , t , · · · , t >,
1 2 n
rding to the historical points < t , · · · , t >,
1 j−1
ons in this task.
valuate the spatial-temporal ability of LLMs and
ht and fine-tuning can improve the performance.
e of two closed-source model, i.e., ChatGPT
Llama-2 [29], Vicuna8, Gemma [20], Phi-2,
alcon [1], Deepseek [3], Qwen [2] and Yi [33].
Appendix B in the supplementary material.
n/geolife-gps-trajectory-dataset-user-guide/

Table 2: The performance of ACC on knowledge comprehension and spatio-temporal reasoning tasks
(bold: best; underline: runner-up). ‘-’ denotes the model failed to answer most questions.
Knowledge Comprehension Spatio-temporal Reasoning
PCR PI URFR ARD PTRD PRRD TRRD TI
ChatGPT 0.7926 0.5864 0.3978 0.8358 0.7525 0.9240 0.0258 0.3342
GPT-4o 0.9588 0.7268 0.6026 0.9656 - 0.9188 0.1102 0.4416
ChatGLM2 0.2938 0.5004 0.2661 0.2176 0.2036 0.5216 0.2790 0.5000
ChatGLM3 0.4342 0.5272 0.2704 0.2872 0.3058 0.8244 0.1978 0.6842
Phi-2 - 0.5267 - 0.2988 - - - 0.5000
Llama-2-7B 0.2146 0.4790 0.2105 0.2198 0.2802 0.6606 0.2034 0.5486
Vicuna-7B 0.3858 0.5836 0.2063 0.2212 0.3470 0.7080 0.1968 0.5000
Gemma-2B 0.2116 0.5000 0.1989 0.1938 0.4688 0.5744 0.2014 0.5000
Gemma-7B 0.4462 0.5000 0.2258 0.2652 0.3782 0.9044 0.1992 0.5000
DeepSeek-7B 0.2160 0.4708 0.2071 0.1938 0.2142 0.6424 0.1173 0.4964
Falcon-7B 0.1888 0.5112 0.1929 0.1928 0.1918 0.4222 0.2061 0.7072
Mistral-7B 0.3526 0.4918 0.2168 0.3014 0.4476 0.7098 0.0702 0.4376
Qwen-7B 0.2504 0.6795 0.2569 0.2282 0.2272 0.5762 0.1661 0.4787
Yi-6B 0.3576 0.5052 0.2149 0.1880 0.5536 0.8264 0.1979 0.5722
Table 3: The performance of ACC and absolute error (in meters) on accurate computation and
downstream tasks (bold: best; underline: runner-up). ‘-’ denotes the model failed to directly answer
most questions.
Accurate Computation Downstream Applications
DD TTRA TAD TC TP
ChatGPT 0.1698 0.1048 0.5382 0.4475 -
GPT-4o 0.5434 0.3404 0.6016 - -
ChatGLM2 0.1182 0.1992 0.5000 0.3333 231.2
ChatGLM3 0.1156 0.1828 0.5000 0.3111 224.5
Phi-2 0.1182 0.0658 0.5000 0.3333 206.9
Llama-2-7B 0.1256 0.2062 0.5098 0.3333 189.3
Vicuna-7B 0.1106 0.1728 0.5000 0.2558 188.1
Gemma-2B 0.1972 0.2038 0.5000 0.3333 207.7
Gemma-7B 0.1182 0.1426 0.5000 0.3333 139.4
DeepSeek-7B 0.1972 0.1646 0.5000 0.3333 220.8
Falcon-7B 0.1365 0.2124 0.5000 0.3309 3572.8
Mistral-7B 0.1182 0.1094 0.5000 0.3333 156.8
Qwen-7B 0.1324 0.2424 0.5049 0.3477 205.2
Yi-6B 0.1284 0.2214 0.5000 0.3333 156.2
Metrics. We adopt accuracy for tasks other than trajectory prediction. For trajectory prediction, we
report absolute error, i.e., the distance in meters between the predicted coordinates and ground truth.
Experimental details. In our experiments, we adopt the precision of FP32 for all LLMs. For all tasks
except trajectory prediction, LLMs are expected to answer an option or "Yes"/"No", thus we set the
max_new_tokens to 15, i.e., the maximum length of the generated new tokens is 15. For trajectory
prediction, LLMs should predict the longitude and latitude, and we set the max_new_tokens to 50.
For other hyperparameters, we adopt the default value of each model. All experiments of open source
models are conducted on two NVIDIA H100.
5.2 Main results
To investigate the spatio-temporal ability of LLMs, we conduct experiments to evaluate the performance of all models on each task. The main results are shown in Table 2 and Table 3.
7

(a) (b) (c)
Figure 2: The performance of ACC and absolute error (in meters) in (a) in-context learning evaluation,
(b) chain-of-thought evaluation, (c) fine-tuning evaluation.
There are significant differences in the performance of different models. We observe ChatGPT
and GPT-4o outperform other models by a large margin on many tasks, e.g., point category recognition, administrative region determination, and point-trajectory relationship detection. There is
also a significant difference in performance between open-source models. For instance, Gemma-7B
outperforms Qwen-7B on point-region relationship detection with an improvement of 57.0%, while
Qwen-7B outperforms Gemma-7B on point-identification with an improvement of 35.9%. Although
LLMs have the potential to analyze spatio-temporal data, not all models have been adequately trained
on relevant corpora and learned corresponding spatio-temporal ability.
Model size is important for knowledge and semantic comprehension. For semantic comprehension, GPT-4o performs better than ChatGPT on all tasks, and ChatGPT outperforms other models on
most tasks. The possible reason is that LLMs rely on sufficient parameters to compress and store
knowledge, and ChatGPT/GPT-4o has more parameters than other evaluated open-source models. We
also observe that Gemma-2B performs poorly on all semantic comprehension tasks, while Gemma7B, with the same technology but more parameters, achieves higher performance. It supports our
conclusion that model size is important for knowledge and semantic comprehension.
The evaluated models have difficulty in multi-step reasoning. The performance of most models
on point-region relationship detection is much higher than trajectory-region detection. For instance,
the accuracy of ChatGPT is 92.40% on point-region relationship detection, with only 2.58% on
trajectory-region relationship detection. Note that trajectory-region relationship detection can be
achieved by performing point-region relationship detection for each point in the trajectory, thus it is
a multi-step reasoning task. The performance on this multi-step task is poor although models such
as ChatGPT, GPT-4o, and Gemma-7B can achieve high performance on each step. In conclusion,
multi-step spatio-temporal reasoning is difficult for LLMs.
Accurate computation and downstream tasks are more challenging. As shown in Table 3, the
accuracy of all models is below 35% on accurate computation tasks, which is because LLMs are
mainly trained on nature language corpus and are not good at computation. Moreover, the performance
of evaluated models is also poor on downstream tasks. For instance, the best performance on trajectory
anomaly is only 60.16%, indicating that most evaluated models can not distinguish between normal
and anomalous trajectories. The lack of expert knowledge on downstream tasks, e.g., the normal
trajectory patterns, leads to their unsatisfactory performance.
5.3 In-Context learning evaluation
Although some evaluated models can perform well on certain tasks, the results in many scenarios
are poor. Since LLMs show impressive in-context few-shot learning capacity in previous works, we
conduct experiments to investigate if in-context learning can improve the performance of LLMs on
STBench. Specifically, we select six tasks where the evaluated models performed poorly and we
adopt two-shot prompting. Due to the heavier computation cost caused by the longer context, we
only evaluate one closed-source model, ChatGPT, and two open-source models with different model
sizes, i.e., Gemma-2B and Llama-2-7B. The results are shown in Fig. 2(a).
For most tasks, the performance of ChatGPT has been greatly improved with in-context learning.
For instance, its performance on POI identification and direction determination has increased from
58.64% to 76.30%, and from 16.98% to 43.16%, respectively. Moreover, the two-shot prompting also
constrains the output, e.g., ChatGPT refuses to answer the questions of trajectory prediction in Table 3,
8

but its absolute error is only 119.4 with two-shot prompting. Although in-context learning is effective
for ChatGPT, it is useless on most tasks for Gemma-2B and Llama-2-7B, which is consistent with the
phenomenon in previous work that in-context learning is less effective for smaller LLMs [31].
5.4 Chain-of-thought evaluation
We further conduct experiments to verify if chain-of-thought (CoT) is effective on STBench. Specifically, we evaluate ChatGPT and Gemma-2B with chain-of-thought prompting on several tasks
that involve multi-step reasoning: urban region function recognition, trajectory-region relationship
detection, trajectory-trajectory relationship analysis and trajectory classification. For each task, we
add two samples with a detailed reasoning process in the context, i.e., we implement chain-of-thought
by two-shot prompting. For instance, in trajectory classification, we add two samples that contain the
reasoning process of calculating the length and average speed of the trajectory. The results are shown
in Fig. 2(b).
We observe the performance of ChatGPT increases significantly in all selected tasks. For instance, its
performance with CoT prompting is 52.20% on urban region function recognition and 61.04% on
trajectory classification, much better than 39.78% and 44.75% in Table 2 and Table 3. For Gemma-2B,
the performance on all selected tasks is also improved. For example, its accuracy increased from
19.89% to 22.55% on urban region function recognition and from 33.33% to 40.05% on trajectory
classification. The results demonstrate the effectiveness of CoT in spatio-temporal analysis.
5.5 Fine-tuning Evaluation
While in-context learning and chain-of-thought is less effective for smaller models, we conduct
experiments to investigate if fine-tuning can significantly improve the performance on STBench.
Specifically, we select several tasks and follow the construction strategies in Section 4 to generate
1,2000 samples as the training dataset for each task. We adopt QLoRA [7] to fine-tune the model on
the training dataset for each task, with the learning rate of 2e-4, the rank of 8 and NF4 quantization.
Due to the very high computational cost and memory usage, we only fine-tune a 2B model for
evaluation, i.e., Gemma-2B. The results are shown in Fig. 2(c).
The performance on all tasks is significantly improved after fine-tuning. For instance, the performance
on administrative region determination and direction determination increased from 19.89% to 91.98%,
and from 19.72% to 47.08%, respectively. For trajectory prediction, Gemma-2B achieves the absolute
error of 147.8 meters, which is better than all 7B models in Table 3. This confirms LLMs’ potential
in spatial-temporal analysis and the lack of training on relevant corpora.
6 Conclusion
In this work, we propose STBench to assess LLMs’ ability in spatio-temporal analysis. STBench
consists of 13 tasks and over 60,000 QA pairs, systematically evaluating four dimensions: knowledge
comprehension, spatio-temporal reasoning, accurate computation, and downstream applications.
We benchmark 13 latest LLMs and the results show their remarkable performance on knowledge
comprehension and spatio-temporal reasoning tasks. Our further experiments with in-context learning,
chain-of-thought prompting and fine-tuning also prove the great potential of LLMs on other tasks.
Limitations. Due to the rapid evolution of large language models and their enormous computational
costs, our assessment is difficult to cover the latest models. For instance, when we started benchmarking, Llama-2 and DeepSeek were the latest models, but now Llama-3 and DeepSeek-V2 have
appeared. We have already released our datasets and code, along with the experiments results. We
will maintain the project and benchmark more LLMs.
Acknowledgements
The data samples of STBench are constructed based on several open-source datasets, i.e., the Yelp
Dataset from Yelp Inc., the New Orleans Region Dataset from United States government, the Xi’an
Dataset from DiDi Chuxing Inc., the EULUC Dataset from Tsinghua University and the Geolife
Dataset from Microsoft Research.
9

References
[1] Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Alshamsi, et al. The falcon series of open
language models. CoRR, abs/2311.16867, 2023.
[2] Jinze Bai, Shuai Bai, Yunfei Chu, et al. Qwen technical report. CoRR, abs/2309.16609, 2023.
[3] Xiao Bi, Deli Chen, Guanting Chen, et al. Deepseek LLM: scaling open-source language
models with longtermism. CoRR, abs/2401.02954, 2024.
[4] Yupeng Chang, Xu Wang, Jindong Wang, et al. A survey on evaluation of large language
models. CoRR, abs/2307.03109, 2023.
[5] Jiawei Chen, Hongyu Lin, Xianpei Han, and Le Sun. Benchmarking large language models
in retrieval-augmented generation. In Conference on Artificial Intelligence, AAAI 2024, pages
17754–17762, 2024.
[6] Mark Chen, Jerry Tworek, Heewoo Jun, et al. Evaluating large language models trained on
code. CoRR, abs/2107.03374, 2021.
[7] Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, and Luke Zettlemoyer. Qlora: Efficient
finetuning of quantized llms. In Advances in Neural Information Processing Systems, NeurIPS
2023, 2023.
[8] Zhengxiao Du, Yujie Qian, Xiao Liu, et al. GLM: general language model pretraining with autoregressive blank infilling. In Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), ACL 2022, pages 320–335, 2022.
[9] Peng Gong, Bin Chen, Xuecao Li, et al. Mapping essential urban land use categories in china
(euluc-china): Preliminary results for 2018. Science Bulletin, 65(3):182–187, 2020.
[10] Wes Gurnee and Max Tegmark. Language models represent space and time. CoRR,
abs/2310.02207, 2023.
[11] Hartwig H. Hochmair, Levente Juhász, and Takoda Kemp. Correctness comparison of chatgpt-4,
bard, claude-2, and copilot for spatial tasks. CoRR, abs/2401.02404, 2024.
[12] Yuhan Ji and Song Gao. Evaluating the effectiveness of large language models in representing
textual descriptions of geometry and spatial relations (short paper). In International Conference
on Geographic Information Science, GIScience 2023, pages 43:1–43:6, 2023.
[13] Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, et al. Mistral 7b. CoRR,
abs/2310.06825, 2023.
[14] Ming Jin, Qingsong Wen, Yuxuan Liang, et al. Large models for time series and spatio-temporal
data: A survey and outlook. CoRR, abs/2310.10196, 2023.
[15] Enkelejda Kasneci, Kathrin Seßler, Stefan Küchemann, et al. Chatgpt for good? on opportunities
and challenges of large language models for education. Learning and individual differences,
103:102274, 2023.
[16] Fangjun Li, David C. Hogg, and Anthony G. Cohn. Advancing spatial reasoning in large
language models: An in-depth evaluation and enhancement using the stepgame benchmark. In
Conference on Artificial Intelligence, AAAI 2024, pages 18500–18507, 2024.
[17] Zhonghang Li, Lianghao Xia, Yong Xu, and Chao Huang. GPT-ST: generative pre-training of
spatio-temporal graph neural networks. In Advances in Neural Information Processing Systems,
NeurIPS 2023, 2023.
[18] Zhonghang Li, Lianghao Xia, Jiabin Tang, et al. Urbangpt: Spatio-temporal large language
models. CoRR, abs/2403.00813, 2024.
[19] Rohin Manvi, Samar Khanna, Gengchen Mai, et al. Geollm: Extracting geospatial knowledge
from large language models. CoRR, abs/2310.06213, 2023.
10

[20] Thomas Mesnard, Cassidy Hardin, Robert Dadashi, et al. Gemma: Open models based on
gemini research and technology. CoRR, abs/2403.08295, 2024.
[21] Roshanak Mirzaee and Parisa Kordjamshidi. Transfer learning with synthetic corpora for
spatial role labeling and reasoning. In Conference on Empirical Methods in Natural Language
Processing, EMNLP 2022, pages 6148–6165, 2022.
[22] Roshanak Mirzaee, Hossein Rajaby Faghihi, Qiang Ning, and Parisa Kordjamshidi. SPARTQA:
A textual question answering benchmark for spatial reasoning. In Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies,
NAACL-HLT 2021, pages 4582–4598, 2021.
[23] PETER MOONEY, WENCONG CUI, BOYUAN GUAN, and LEVENTE JUHÁSZ. Towards
understanding the spatial literacy of chatgpt. In ACM SIGSPATIAL International Conference,
2023.
[24] OpenAI. GPT-4 technical report. CoRR, abs/2303.08774, 2023.
[25] Jonathan Roberts, Timo Lüddecke, Sowmen Das, et al. GPT4GEO: how a language model sees
the world’s geography. CoRR, abs/2306.00020, 2023.
[26] Jonathan Roberts, Timo Lüddecke, Rehan Sheikh, et al. Charting new territories: Exploring the
geographic and geospatial capabilities of multimodal llms. CoRR, abs/2311.14656, 2023.
[27] Zhengxiang Shi, Qiang Zhang, and Aldo Lipani. Stepgame: A new benchmark for robust
multi-hop spatial reasoning in texts. In Conference on Artificial Intelligence, AAAI 2022, pages
11321–11329, 2022.
[28] Arun James Thirunavukarasu, Darren Shu Jeng Ting, Kabilan Elangovan, et al. Large language
models in medicine. Nature medicine, 29(8):1930–1940, 2023.
[29] Hugo Touvron, Louis Martin, Kevin Stone, et al. Llama 2: Open foundation and fine-tuned chat
models. CoRR, abs/2307.09288, 2023.
[30] Lei Wang, Chen Ma, Xueyang Feng, et al. A survey on large language model based autonomous
agents. Frontiers of Computer Science, 18(6):1–26, 2024.
[31] Jason Wei, Yi Tay, Rishi Bommasani, et al. Emergent abilities of large language models. Trans.
Mach. Learn. Res., 2022, 2022.
[32] Yutaro Yamada, Yihan Bao, Andrew K. Lampinen, et al. Evaluating spatial understanding of
large language models. CoRR, abs/2310.14540, 2023.
[33] Alex Young, Bei Chen, Chao Li, et al. Yi: Open foundation models by 01.ai. CoRR,
abs/2403.04652, 2024.
[34] Aohan Zeng, Xiao Liu, Zhengxiao Du, et al. GLM-130B: an open bilingual pre-trained model.
In International Conference on Learning Representations, ICLR 2023, 2023.
[35] Weijia Zhang, Jindong Han, Zhao Xu, et al. Towards urban general intelligence: A review and
outlook of urban foundation models. CoRR, abs/2402.01749, 2024.
[36] Xiyuan Zhang, Ranak Roy Chowdhury, Rajesh K. Gupta, and Jingbo Shang. Large language
models for time series: A survey. CoRR, abs/2402.01801, 2024.
[37] Wayne Xin Zhao, Kun Zhou, Junyi Li, et al. A survey of large language models. CoRR,
abs/2303.18223, 2023.
11

Appendix
A Data Format
A.1 Prompt template for chatting models
To make the responses of LLMs controllable and identification of the final answer easier, all data
samples in STBench are constructed in the form of text completion. However, there are some chatting
models that only support chat completion and do not support text completion, e.g., GPT-4o. For these
models, we instruct them to complete the text entered by the human via system prompt. The data
samples we constructed are inputted with the role of human, as shown in Table 4.
Table 4: A prompt template of models that only support chat completion. The blue texts describe
the question. The brown texts are the options. The teal texts denote the guidance that constrains the
output of LLMs.
System: "You are a helpful text completion assistant. Please continue writing the text entered by
the human."
Human: "Question: There is a trajectory, xxxx. Options: (1) xxxx, (2) xxxx, (3) xxxx, · · · . Please
answer one option. Answer: The answer is option ("
A.2 Data Examples
STBench consists of 13 distinct tasks, covering four dimensions: knowledge comprehension, spatiotemporal reasoning, accurate computation and downstream applications. We will provide data
samples to illustrate the design of each task.
A.2.1 Knowledge comprehension
There are four tasks to assess the knowledge comprehension ability of LLMs in spatio-temporal
analysis, i.e., Administrative Region Determination (ARD), POI Category Recognition (PCR),
POI Identification (PI) and Urban Region Function Recognition (URFR).
As shown in Table 5, for administrative region determination, we provide the coordinates of a location
and ask the model to answer which option the coordinates is located in. The options contain five
cities in the same state, which makes this task more challenging. The data sample of POI category
recognition is shown in Table 6. LLMs are asked to predict the category of the POI according to
its coordinates and two comments, where each comment contains the comment content and the
timestamp. We provide five options and each option is a list of tags such as shopping and skin care.
In POI identification, we ask the model if two POI are actually the same, where the description of
each POI consists of its coordinates and two comments, just as shown in Table 7. A data sample of
urban region function recognition is presented in Table 8, which asks the model to predict the urban
region function category according to its boundary lines and the POIs located within it.
12

Table 5: A data sample for ARD. The blue texts describe the question. The brown texts are the
options. The teal texts denote the guidance that constrains the output of LLMs.
Question: Below is the coordinate location information, and the options of the area
where the coordinate may be located:
{
"latitude": 36.104588,
"longitude": -86.81415,
Question
"options": "(0): Eaton, TN (1): Nashville, TN (2): Sewanee, TN (3): Memphis, TN
(4): Knoxville, TN"
}
Please answer which area the coordinate is located in. Please just answer the number
of your option with no other texts.
Answer: Option (
Answer 1): Nashville, TN
Table 6: A data sample for PCR. The blue texts describe the question. The brown texts are the options.
The teal texts denote the guidance that constrains the output of LLMs.
Question: Below is the coordinate location information and related comments of a
location, with the options of possible function for this location:
{
"latitude": 36.0423589,
"longitude": -86.7788876,
"comment1": {
"content": "BEST WAX CENTER. ZOIE AND ERIN ARE THE BEST. zoie
is calm and friendly makes me feel comfortable all the time erin kills the game with
my eyebrows every single time. Everyone asks about my eyebrows thanks to her.
Definitely recommend going to Erin and zoie.",
"time": "2021-06-02 00:37:48"
},
"comment2":{
Question "content": "I have done 2 sessions with Erin and LOVE HER! I was so incredibly
nervous my first time getting a full bikini wax, but she made me feel so comfortable.
She talked through what she was doing, asked me questions, and made the process
seem less painful overall. I highly recommend her!!",
"time": "2021-06-18 00:28:02"
},
"options": "(0): Computers, Shopping, Appliances, Furniture Stores, Home &
Garden (1): Waxing, Hair Removal, Skin Care, Beauty & Spas (2): Juice Bars &
Smoothies, Food, Vegan, Restaurants, Acai Bowls (3): Discount Store, Shopping,
Toy Stores, Food, Candy Stores, Specialty Food (4): Delis, Food, Coffee & Tea,
Sandwiches, Restaurants, Convenience Stores"
}
Please answer which function the location is. Please just answer the number of your
option with no other texts.
Answer: Option (
Answer 1): Waxing, Hair Removal, Skin Care, Beauty & Spas
13

Table 7: A data sample for PI. The blue texts describe the question. The brown texts are the options.
The teal texts denote the guidance that constrains the output of LLMs.
Question: Below are two Points of Interest (POI) and related comments.
POI 1:
{
"latitude": 34.4266787,
"longitude": -119.7111968,
"comment1": {
"content": "Abby Rappoport helped me achieve a long lost sense of health.
I was suffering from debilitating insomnia due to a very stressful job and family
requirements. She also was able to get me through a bad bout of bronchitis. She
is professional, thorough and clearly seasoned as a healthcare provider. I highly
recommend Abby if your situation needs caring attention.",
"time": "2012-08-09 20:43:27"
},
"comment2": {
"content": "Abby is an amazing practitioner. In a treatment she is really present
with me and my concerns. She is caring and thorough. I especially appreciate the
exercise, herbs and advice she sends me home with so that my healing can continue
outside her office. Abby has helped me with stress related problems and chronic low
back pain. Sadly, she moved out of my area but whenever I’m her neck of the woods I
take the opportunity to see her.",
"time": "2013-03-01 06:11:05"
}
}.
Question POI2:
{
"latitude": 34.4266621,
"longitude": -119.711207,
"comment1": {
"content": "Before buying I looked to see if they had a map off merchants to see
where they were located and found no map. If there is one there out is hard to find. I
won’t buy unless I can tell if members are near me by way of a seeing them onassis
map.",
"time": "2014-08-25 00:37:13"
},
"comment2": {
"content": "Buyer beware!.... I purchased this card last year and used the buy 1
get 1 free deal and was told it’s meant for two people. This was at McConnell’s fine
ice cream on state street. This guy who’s the manager or owner of the business said
this deal is meant for you to bring someone along and enjoy the ice cream together
and not for you to come in and walk away w/two ice cream cones and pay for one ice
cream cone. At the end he said come back w/a friend. He was annoyed.",
"time": "2020-10-09 16:54:26"
}
}.
Check whether the two POIs are the same place. Notice that due to the errors, the
latitude and longitude may be different although two POI represent the same place.
Please answer "Yes" or "No".
Answer: The answer is "
Answer No
14

Table 8: A data sample for URFR. The blue texts describe the question. The brown texts are the
options. The teal texts denote the guidance that constrains the output of LLMs.
Question: Below is the coordinate information and related comments of a region, with
the options of possible function for this region:
{
"region": [(-90.0877900, 29.9689360), (-90.0872427, 29.9689360), (-90.0872427,
29.9696428), (-90.0877900, 29.9696428), (-90.0877900, 29.9689360)]",
"pois": [
{
"latitude": 29.9694327,
"longitude": -90.0874047,
"comment1": {
"content": "I cannot day enough about how much I love this place. NOCB
popped up on my Instagram feed in 2017 with their Black Friday deals, signed up on
a whim and never looked back. The classes are fun and exciting and a great way to
get a feel for boxing and each of the trainers here. The gym has become my favorite
past time and I love taking my friends in to understand why I’m hooked.",
"time": "2019-12-05 01:43:01"
},
"comment2": {
"content": "The best boxing gym in the city! I started boxing a year ago
Question
wanting to both get in better shape and learn the skills associated with boxing. I’ve
tried a few places but ultimately settled at NOBC. The positive atmosphere is the first
thing you notice about this gym, regardless of if you are a professional or a first time
boxer everyone trains together and shares the same passion for boxing, wanting to
better themselves through the sport. The gym has everything you need from a weight
room, a full boxing ring/equipment, and a cardio/ab area. In a few short weeks training
with the owner Chase I have become a better boxer. The gym is clean, friendly, and
fun. I plan on training here for years to come.",
"time": "2016-10-29 02:02:17"
}
}
],
"options": "(0): Suburban Lake Area Neighborhood Park District (1): Suburban
Pedestrian Oriented Corridor Business District (2): Historic Urban Neighborhood
Business District (3): Greenway Open Space District (4): Historic Marigny Treme
Bywater Commercial District"
}
Please answer which function the location is. Please just answer the number of your
option with no other texts.
Answer: Option (
Answer 2): Historic Urban Neighborhood Business District
A.2.2 Spatio-temporal reasoning
The dimension of spatio-temporal reasoning consists of four tasks: Point-Trajectory Relationship
Detection (PTRD), Point-Region Relationship Detection (PRRD), Trajectory-Region Relationship Detection (TRRD) and Trajectory Identification (TI). The data sample of point-trajectory
relationship detection provides a trajectory and five points, then ask the model which point the trajectory passes through, as shown in Table 9. A sample of point-region relationship detection is given in
Table 10, which ask the model to determine which region a point falls in according to the boundary
lines of the regions and the coordinates of the point. As an enhancement to this task, trajectory-region
relationship detection further ask which regions a trajectory passes through chronologically, as shown
in Table 11. Trajectory identification aim to determine if two point sequences describe the same
trajectory, whose data samples are constructed by four strategies, i.e., downsampling, staggered
sampling, spatial offset and temporal offset. By setting different downsampling rate or sampling
different points, we can get two point sequences that describe the same trajectory, as shown in
15

Table 12. By adding spatial offset or temporal offset to the coordinates or timestamps of the trajectory,
we can get another different trajectory, as shown in Table 13.
Table 9: A data sample for PTRD. The blue texts describe the question. The brown texts are the
options. The teal texts denote the guidance that constrains the output of LLMs.
Question: The following is a sequence of points sampled from a trajectory and the meaning of each point is (longitude, latitude, timestamp):
[(108.91226, 34.25924, 1477967031), (108.92136, 34.25929, 1477967109),
(108.92268, 34.26271, 1477967184), (108.92247, 34.27329, 1477967274),
(108.92732, 34.27659, 1477967352), (108.93702, 34.27663, 1477967430), (108.9435,
Question 34.27682, 1477967505), (108.95271, 34.27686, 1477967586), (108.95937, 34.27675,
1477967662), (108.97203, 34.27726, 1477967767)].
The trajectory passes through one of the following points: (1) Point 1 (108.93244,
34.28307); (2) Point 2 (108.95336, 34.28628); (3) Point 3 (108.93661, 34.28624); (4)
Point 4 (108.91681, 34.259265); (5) Point 5 (108.92387, 34.26896);
Please answer which option the trajectory passes through.
Answer: The trajectory passes through Point
Answer 4
Table 10: A data sample for PRRD. The blue texts describe the question. The teal texts denote the
guidance that constrains the output of LLMs.
Question: There are several regions, and the boundary lines of each region are
presented in the form of a list of (longitude, latitude) below:
Region 1: [(104.2483, 33.2447), (104.2481, 33.2440), (104.2470, 33.2438),
(104.2466, 33.2440), (104.2464, 33.2443), (104.2463, 33.2446), (104.2477, 33.2456)]
Question Region 2: [(104.2446, 33.2471), (104.2453, 33.2460), (104.2456, 33.2450),
(104.2451, 33.2451), (104.2448, 33.2454), (104.2443, 33.2457), (104.2437, 33.2459),
(104.2432, 33.2462), (104.2431, 33.2465)]
Now there is a point with longitude 104.2444 and latitude 33.2460. Please directly
answer the number of the region that this point falls in.
Answer: The point falls in Region
Answer 2
16

Table 11: A data sample for TRRD. The blue texts describe the question. The brown texts are the
options. The teal texts denote the guidance that constrains the output of LLMs.
Question: There are several regions, and the boundary lines of each region are
presented in the form of a list of (longitude, latitude) below:
Region 1: [(104.2483209, 33.2446592), (104.2480514, 33.2440436), (104.2469734,
33.2437741), (104.2465616, 33.2440436), (104.2464345, 33.2443130),
(104.2462657, 33.2445689), (104.2477476, 33.2456337)]
Region 2: [(104.2446473, 33.2470611), (104.2452599, 33.2459617), (104.2456260,
33.2449552), (104.2450870, 33.2451215), (104.2448175, 33.2453910),
(104.2442785, 33.2456605), (104.2437395, 33.2459300), (104.2432005, 33.2461995),
(104.2430696, 33.2464690)]
Region 3: [(104.2476758, 33.2457578), (104.2459598, 33.2450870), (104.2454075,
33.2460224), (104.2447964, 33.2471191), (104.2465063, 33.2478088),
(104.2476758, 33.2457578)]
Question
Region 4: [(104.2445777, 33.2471861), (104.2427577, 33.2466877), (104.2423098,
33.2477300), (104.2424400, 33.2481779), (104.2433484, 33.2491652),
(104.2433517, 33.2491689), (104.2436447, 33.2488824), (104.2442290,
33.2478118)]
Region 5: [(104.2464353, 33.2479333), (104.2447267, 33.2472441), (104.2443780,
33.2478698), (104.2438019, 33.2489228), (104.2436336, 33.2494729),
(104.2451994, 33.2499855), (104.2458120, 33.2490264), (104.2464353,
33.2479333)]
Now there is a trajectory presented in the form of a list of (longitude, latitude): [(104.2453154, 33.2468798), (104.2431636, 33.2476642), (104.2448701,
33.2483024), (104.2427480, 33.2486476), (104.2466176, 33.2489308)]. Note that
although we only provide the coordinates of some discrete points, the trajectory is
actually continuous.
Please answer which regions it has passed through in chronological order: (1) [3, 2, 1,
5], (2) [3, 4], (3) [3, 4, 2, 3], (4) [3, 2, 4, 2, 1], (5) [3, 4, 5].
Answer only one option with no other texts. Answer: Option (
Answer 5): [3, 4, 5]
17

Table 12: Data samples constructed by downsampling and staggered sampling for TI. The blue
texts describe the question. The brown texts are the options. The teal texts denote the guidance that
constrains the output of LLMs.
Downsampling
Question: There are two point sequences and each sequence is sampled from a
trajectory. The meaning of each point is (longitude, latitude, time stamp). Please
answer whether these two sequences are sampled from the same trajectory.
Sequence 1: [(108.91226, 34.25924, 1477967031), (108.92136, 34.25929,
1477967106), (108.92277, 34.26197, 1477967178), (108.92248, 34.27254,
1477967265), (108.92586, 34.27659, 1477967340), (108.93587, 34.27662,
1477967415), (108.94108, 34.27671, 1477967487), (108.95088, 34.27682,
1477967564), (108.95635, 34.27691, 1477967638)],
Sequence 2: [(108.91226, 34.25924, 1477967031), (108.91715, 34.25925,
1477967067), (108.92136, 34.25929, 1477967106), (108.92275, 34.25931,
1477967142), (108.92277, 34.26197, 1477967178), (108.92257, 34.2661,
Question
1477967217), (108.92248, 34.27254, 1477967265), (108.92307, 34.27581,
1477967301), (108.92586, 34.27659, 1477967340), (108.93109, 34.2766,
1477967379), (108.93587, 34.27662, 1477967415), (108.93958, 34.27668,
1477967451), (108.94108, 34.27671, 1477967487), (108.94591, 34.27739,
1477967523), (108.95088, 34.27682, 1477967564), (108.95329, 34.27687,
1477967602), (108.95635, 34.27691, 1477967638)].
You can confirm if their routes are the same by checking if sequence 1 passes through
each point in sequence 2. Then, check if their timestamps are consistent. Finally,
answer whether they are sampled from the same trajectory.
Please answer "Yes" or "No".
Answer: The answer is "
Answer Yes
Staggered Sampling
Question: There are two point sequences and each sequence is sampled from a
trajectory. The meaning of each point is (longitude, latitude, time stamp). Please
answer whether these two sequences are sampled from the same trajectory.
Sequence 1: [(108.91267, 34.25924, 1477967034), (108.91758, 34.25925,
1477967070), (108.92136, 34.25929, 1477967109), (108.923, 34.25931,
1477967145), (108.92273, 34.26228, 1477967181), (108.92256, 34.26648,
1477967220), (108.92248, 34.27273, 1477967268), (108.92317, 34.27594,
1477967304), (108.92621, 34.27659, 1477967343), (108.93137, 34.27661,
1477967382), (108.93614, 34.27663, 1477967418), (108.93984, 34.27668,
1477967454), (108.94133, 34.27671, 1477967490), (108.94635, 34.27738,
1477967526), (108.95162, 34.27684, 1477967568), (108.95344, 34.27687,
Question
1477967605), (108.95665, 34.27689, 1477967641)],
Sequence 2: [(108.91226, 34.25924, 1477967031), (108.91715, 34.25925,
1477967067), (108.92136, 34.25929, 1477967106), (108.92275, 34.25931,
1477967142), (108.92277, 34.26197, 1477967178), (108.92257, 34.2661,
1477967217), (108.92248, 34.27254, 1477967265), (108.92307, 34.27581,
1477967301), (108.92586, 34.27659, 1477967340), (108.93109, 34.2766,
1477967379), (108.93587, 34.27662, 1477967415), (108.93958, 34.27668,
1477967451), (108.94108, 34.27671, 1477967487), (108.94591, 34.27739,
1477967523), (108.95088, 34.27682, 1477967564), (108.95329, 34.27687,
1477967602), (108.95635, 34.27691, 1477967638)].
You can confirm if their routes are the same by checking if sequence 1 passes through
each point in sequence 2. Then, check if their timestamps are consistent. Finally,
answer whether they are sampled from the same trajectory.
Please answer "Yes" or "No".
Answer: The answer is "
Answer Yes
18

Table 13: Data samples constructed through spatial or temporal offset for TI. The blue texts describe
the question. The brown texts are the options. The teal texts denote the guidance that constrains the
output of LLMs.
Spatial Offset
Question: There are two point sequences and each sequence is sampled from a
trajectory. The meaning of each point is (longitude, latitude, time stamp). Please
answer whether these two sequences are sampled from the same trajectory.
Sequence 1: [(108.91226, 34.25924, 1477967031), (108.91715, 34.25925,
1477967067), (108.92136, 34.25929, 1477967106), (108.92275, 34.25931,
1477967142), (108.92277, 34.26197, 1477967178), (108.92257, 34.2661,
1477967217), (108.94056, 34.28908, 1477967265), (108.94115, 34.29235,
1477967301), (108.94394, 34.29313, 1477967340), (108.94917, 34.29314,
1477967379), (108.95395, 34.29316, 1477967415), (108.95766, 34.29322,
1477967451), (108.95916, 34.29325, 1477967487), (108.96399, 34.29393,
1477967523), (108.96896, 34.29336, 1477967564), (108.97137, 34.29341,
Question
1477967602), (108.95635, 34.27691, 1477967638)],
Sequence 2: [(108.91226, 34.25924, 1477967031), (108.91715, 34.25925,
1477967067), (108.92136, 34.25929, 1477967106), (108.92275, 34.25931,
1477967142), (108.92277, 34.26197, 1477967178), (108.92257, 34.2661,
1477967217), (108.92248, 34.27254, 1477967265), (108.92307, 34.27581,
1477967301), (108.92586, 34.27659, 1477967340), (108.93109, 34.2766,
1477967379), (108.93587, 34.27662, 1477967415), (108.93958, 34.27668,
1477967451), (108.94108, 34.27671, 1477967487), (108.94591, 34.27739,
1477967523), (108.95088, 34.27682, 1477967564), (108.95329, 34.27687,
1477967602), (108.95635, 34.27691, 1477967638)].
You can confirm if their routes are the same by checking if sequence 1 passes through
each point in sequence 2. Then, check if their timestamps are consistent. Finally,
answer whether they are sampled from the same trajectory.
Please answer "Yes" or "No".
Answer: The answer is "
Answer No
Temporal Offset
Question: There are two point sequences and each sequence is sampled from a
trajectory. The meaning of each point is (longitude, latitude, time stamp). Please
answer whether these two sequences are sampled from the same trajectory.
Sequence 1: [(108.91226, 34.25924, 1477967031), (108.91715, 34.25925,
1477967067), (108.92136, 34.25929, 1477967106), (108.92275, 34.25931,
1477967142), (108.92277, 34.26197, 1477967178), (108.92257, 34.2661,
1477967217), (108.92248, 34.27254, 1477967265), (108.92307, 34.27581,
1477967301), (108.92586, 34.27659, 1477967340), (108.93109, 34.2766,
1477967379)],
Sequence 2: [(108.91226, 34.25924, 1478006153), (108.91715, 34.25925,
1478006189), (108.92136, 34.25929, 1478006228), (108.92275, 34.25931,
Question
1478006264), (108.92277, 34.26197, 1478006300), (108.92257, 34.2661,
1478006339), (108.92248, 34.27254, 1478006387), (108.92307, 34.27581,
1478006423), (108.92586, 34.27659, 1478006462), (108.93109, 34.2766,
1478006501)].
You can confirm if their routes are the same by checking if sequence 1 passes through
each point in sequence 2. Then, check if their timestamps are consistent. Finally,
answer whether they are sampled from the same trajectory.
Please answer "Yes" or "No".
Answer: The answer is "
Answer No
19

Table 14: A data sample for DD. The blue texts describe the question. The brown texts are the options.
The teal texts denote the guidance that constrains the output of LLMs.
Question: A has a longitude of 115.6249 and a latitude of 33.1811, while B has a
longitude of 114.3897 and a latitude of 36.085839. Therefore, B is in the () from A.
Please choose the correct answer from the following options and fill it in parentheses.
Question
(1) North, (2) Northeast, (3) East, (4) Southeast, (5) South, (6) Southwest, (7) West,
(8) Northwest.
Please directly give me the number of your option with no other texts.
Answer: Option (
Answer 1) North
Table 15: A data sample for TTRA. The blue texts describe the question. The brown texts are the
options. The teal texts denote the guidance that constrains the output of LLMs.
Question: There are two trajectories presented in the form of a list of (longitude,
latitude, timestamp) below:
trajectory A: [(104.24490, 33.24652, 1683618155), (104.24440, 33.24504,
1683619121), (104.24420, 33.24477, 1683620129), (104.24600, 33.24515,
1683621109), (104.24667, 33.24498, 1683622143)]
trajectory B: [(104.24458, 33.24707, 1683618164), (104.24242, 33.24675,
Question 1683619137), (104.24375, 33.24676, 1683620199), (104.24522, 33.24833,
1683621179), (104.24615, 33.24663, 1683622182)]
Please calculate the number of times these two trajectories intersect, and choose your
answer from following options:
(1) 2 times, (2) 3 times, (3) 4 times, (4) 0 times, (5) 1 times.
Note that two trajectories intersect if and only if they pass through the same point at
the same timestamp. Give me your option with no other texts.
Answer: Option (
Answer 4) 0 times
A.2.3 Accurate computation
The assessing of accurate computation involves two tasks: Direction Determination (DD) and
Trajectory-Trajectory Relationship Analaysis (TTRA). Direction determination aim to predict
the relative direction between two given coordinates, as shown in Table 14. For trajectory-trajectory
relationship analysis, two trajectories are given and the model is asked to count how many times they
intersect, as shown in Table 15.
A.2.4 Downstream Applications
We select three downstream applications for evaluation: Trajectory Anomaly Detection (TAD),
Trajectory Classification (TC) and Trajectory Prediction (TP). As shown in Table 16 and Table 17,
given a trajectory, trajectory anomaly detection and trajectory classification aims to infer if the
trajectory is anomalous and the source of the trajectory, respectively. For trajectory prediction, the
model is asked to predict the next point of a trajectory according to the historical points, as shown in
Table 18.
20

Table 16: A data sample for TAD. The blue texts describe the question. The brown texts are the
options. The teal texts denote the guidance that constrains the output of LLMs.
Question: Below is a trajectory generated by a taxi, and each point in this trajectory is
a tuple of (longitude, latitude, timestamp):
[(108.91226, 34.25924, 1477967031), (108.91715, 34.25925, 1477967067),
(108.92136, 34.25929, 1477967106), (108.92275, 34.25931, 1477967142),
(108.92277, 34.26197, 1477967178), (108.92257, 34.2661, 1477967217), (108.92248,
34.27254, 1477967265), (108.92307, 34.27581, 1477967301), (108.92586,
Question 34.27659, 1477967340), (108.93109, 34.2766, 1477967379), (108.93587,
34.27662, 1477967415), (108.93958, 34.27668, 1477967451), (108.94108,
34.27671, 1477967487), (108.94591, 34.27739, 1477967523), (108.95088,
34.27682, 1477967564), (108.95329, 34.27687, 1477967602), (108.95635,
34.27691, 1477967638), (108.96059, 34.27669, 1477967677), (108.96856,
34.277, 1477967737), (108.97323, 34.27733, 1477967776), (108.97674, 34.27742,
1477967812), (108.97917, 34.27868, 1477967854)].
The trajectory is anomalous if there is a detour, otherwise the trajectory is normal.
Please answer if this trajectory is anomalous or normal.
Please answer T¨ his trajectory is normalör T¨ his trajectory is anomalousw¨ ith no other
texts.
Answer: This trajectory is
Answer normal
Table 17: A data sample for TC. The blue texts describe the question. The brown texts are the options.
The teal texts denote the guidance that constrains the output of LLMs.
Question: The following is a sequence of points sampled from a trajectory, and the
meaning of each point is (longitude, latitude, timestamp):
[(116.3324016, 40.0743183, 1225573207), (116.3324566, 40.0743099, 1225573208),
(116.3326216, 40.0742966, 1225573212), (116.3328333, 40.0742683, 1225573216),
(116.3330533, 40.0742516, 1225573220), (116.3332683, 40.0742699, 1225573224),
(116.3334999, 40.0742583, 1225573228), (116.3337183, 40.0742583, 1225573232),
(116.3339750, 40.0742033, 1225573236), (116.3341916, 40.0742249, 1225573240),
(116.3343866, 40.0742749, 1225573244), (116.3345883, 40.0743099, 1225573248),
Question (116.3347933, 40.0742966, 1225573252), (116.3350016, 40.0743049, 1225573256),
(116.3352266, 40.0743299, 1225573260), (116.3354566, 40.0743183, 1225573264),
(116.3356466, 40.0743099, 1225573268), (116.3358816, 40.0743150, 1225573272)].
The trajectory is generated by one of the following option: (1) car, (2) bike, (3)
pedestrian.
Please calculate the length and the average speed of the trajectory, and answer which
option is most likely to generate this trajectory.
Answer: The trajectory is most likely to be generated by Option (
Answer 2
Table 18: A data sample for TP. The blue texts describe the question. The brown texts are the options.
The teal texts denote the guidance that constrains the output of LLMs.
Question: Below is an ongoing trajectory generated by a taxi, and each point in this
trajectory is a tuple of (longitude, latitude, timestamp):
Question [(108.92788, 34.23136, 1477956224), (108.92637, 34.23206, 1477956254),
(108.92599, 34.23226, 1477956284), (108.92527, 34.23263, 1477956314)].
Please predict the longitude and latitude of the next point.
Answer: The longitude and latitude of the next point is
Answer [108.92384, 34.23327]
21

Table 19: The performance of ACC on sub-datasets of point-region relationship detection and
trajectory-region relationship detection. r denotes the number of regions and l denotes the length of
the trajectory.
PRRD TRRD
r = 2 r = 3 r = 4 r = 5 l = 2 l = 4 l = 6 l = 8 l = 10
ChatGPT 0.9568 0.9176 0.8864 0.9352 0.0536 0.0312 0.0136 0.0160 0.0144
GPT-4o 0.9224 0.9160 0.9096 0.9272 0.2504 0.1088 0.0680 0.0624 0.0616
ChatGLM2 0.5624 0.6144 0.4216 0.4880 0.3104 0.2736 0.2536 0.2880 0.2696
ChatGLM3 0.9096 0.8400 0.7328 0.8152 0.2256 0.2144 0.2032 0.1784 0.1672
Phi-2 - - - - - - - - -
Llama-2-7B 0.5888 0.6504 0.6208 0.7824 0.2128 0.2088 0.1936 0.2072 0.1944
Vicuna-7B 0.7840 0.7160 0.5920 0.7400 0.1864 0.2032 0.1832 0.2008 0.2104
Gemma-2B 0.7024 0.5696 0.5408 0.4848 0.2096 0.1904 0.2168 0.1960 0.1944
Gemma-7B 0.9056 0.9072 0.8904 0.9144 0.2096 0.1856 0.2128 0.1952 0.1928
DeepSeek-7B 0.8544 0.5968 0.5184 0.6000 0.1504 0.1328 0.1001 0.1088 0.0944
Falcon-7B 0.5602 0.4344 0.3296 0.3647 0.1995 0.2110 0.2090 0.2062 0.2046
Mistral-7B 0.5336 0.7104 0.7256 0.8696 0.1896 0.0704 0.0320 0.0304 0.0288
Qwen-7B 0.6448 0.5752 0.5184 0.5662 0.2544 0.1544 0.1312 0.1496 0.1408
Yi-6B 0.9192 0.8008 0.7560 0.8296 0.2184 0.1816 0.1744 0.1672 0.1816
B Experimental Details
B.1 Evaluated models
We evaluate two closed-source models and a set of open-source models. The two closed-source models
are ChatGPT (gpt-3.5-turbo-1106) and GPT-4o (gpt-4o-2024-05-13), both developed by OpenAI.
For open-source models, we first select two models from the popular Llama family, i.e., Llama-2-7B
and Vicuna-7B, which are released by Meta and Large Model Systems Organization, respectively.
Then, we include Gemma-2B and Gemma-7B, which are developed by Google DeepMind, based
on Gemini research and technology. Phi-2, a model with only 2.7 billion parameters proposed by
Microsoft Research, is evaluated to investigate the performance of lightweight language models. We
also evaluate ChatGLM2 and ChatGLM3, two open bilingual language models with 6B parameters
based on General Language Model (GLM). Moreover, Mistral-7B, a large language model developed
by Mistral AI, is also included. Futhermore, other baselines includes textbfFalcon-7B, a LLM
developed by Technology Innovation Institute; Deepseek-7B, the language model presented by
Deepseek AI; Qwen-7B, the language model of Alibaba and Yi-6B, an open foundation model by
01.AI. All experiments about the open-source models are conducted on modelscope 9. The details
about the downloading of all open-source models, the code for reproducing our experiments, and the
benchmark datasets can be found at https://github.com/LwbXc/STBench.
B.2 Detailed results
There are some tasks that consists of several sub-datasets. Specifically, for the point-region relationship detection task, we vary the number of regions from 2 to 5 to obtain 4 sub-datasets. In the
trajectory-region relationship detection task, the trajectory length is set to 2, 4, 6, 8, 10 to construct
five sub-datasets. Moreover, we adopt four strategies to construct the data samples for trajectory
identification, resulting in four sub-datasets.
B.2.1 Basic prompt
The results on these sub-datasets with basic prompt are shown in Table 19 and Table 20. For
point-region relationship detection, we observe that most models achieve higher performance on
sub-datasets with fewer regions, which is in line with our intuition. But there are also exceptions,
e.g., Mistral-7B achieve higher performance with more regions. For the trajectory-region relationship
9https://github.com/modelscope/modelscope
22

Table 20: The performance of ACC on sub-datasets of trajectory identification.
Downsampling Staggered Temporal Spatial
ChatGPT 0.1784 0.0016 0.8464 0.3104
GPT-4o 0.1624 0.5840 0.0280 0.9920
ChatGLM2 0.0000 0.0000 1.0000 1.0000
ChatGLM3 0.9992 0.9368 0.8008 0.0000
Phi-2 1.0000 1.0000 0.0000 0.0000
Llama-2-7B 0.1952 0.9992 1.0000 0.0000
Vicuna-7B 0.0000 0.0000 1.0000 1.0000
Gemma-2B 0.0000 0.0000 1.0000 1.0000
Gemma-7B 1.0000 1.0000 0.0000 0.0000
DeepSeek-7B 1.0000 0.9856 0.0000 0.0000
Falcon-7B 0.8264 0.0024 1.0000 1.0000
Mistral-7B 0.0056 0.0000 1.0000 0.7448
Qwen-7B 0.3992 0.3395 0.6047 0.5714
Yi-6B 0.9888 0.8856 0.0000 0.4144
Table 21: The performance of ACC on sub-datasets of trajectory-region relationship detection with
in-context learning, chain-of-thought prompting and fine-tuning. l denotes the length of the trajectory.
l = 2 l = 4 l = 6 l = 8 l = 10
ChatGPT w/ ICL 0.1432 0.0408 0.0120 0.0080 0.0088
Llama-2-7B w/ ICL 0.2000 0.1688 0.1328 0.1232 0.1376
Gemma-2B w/ ICL 0.2088 0.2472 0.2376 0.2384 0.2200
ChatGPT w/ CoT 0.7504 0.2520 0.1584 0.1112 0.0872
Gemma-2B w/ CoT 0.2210 0.2564 0.2287 0.1910 0.2125
Gemma-2B w/ SFT 0.7560 0.8104 0.8072 0.7512 0.7640
detection, the performance of most models decreases with larger trajectory length, since longer
trajectory makes the task more challenging. For trajectory identification, we observe that some
models consistently answer "Yes" or "No", regardless of the question, e.g., ChatGLM2 and Phi-2.
We also observe that different models have different characteristics. For instance, GPT-4o can find
out spatial offset in trajectories, but it failed to identify the temporal offset. ChatGLM3 is good
at identifying downsampling, staggered sampling and temporal offset, but it did not recognize the
spatial offset. No evaluated model can achieve high performance on all four sub-datasets.
B.2.2 In-context learning
The results on sub-datasets of trajectory-region relationship detection with in-context learning are
shown in Table 21. We find that in-context learning significantly improve the performance of
ChatGPT on sub-datasets with the trajectory length of 2, but it is useless for sub-datasets with longer
trajectories. We also observe that in-context learing slightly improve the performance of Gemma-2B
on sub-datasets with trajectory length larger than 2, which is exactly opposite to ChatGPT.
B.2.3 Chain-of-thought
The results on sub-datasets of trajectory-region relationship detection with chain-of-though prompting
are shown in Table 21. We observe that CoT further significantly boost the performance of ChatGPT
on most sub-datasets. With the trajectory length increases, the performance of ChatGPT with CoT
decreases sharply. For Gemma-2B, CoT does not further improve its performance compared with
ICL.
23

B.2.4 Fine-tuning
The results on sub-datasets of trajectory-region relationship detection after fine-tuning are shown
in Table 21. We observe fine-tuning significantly improve the performace of Gemma-2B on all
sub-datasets. The performance after fine-tuning does not decreases with larger trajectory length.
24
