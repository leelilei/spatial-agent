---
title: "UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large Language Models"
source_pdf: "01_urban_benchmarks\\05_UrbanPlanBench_Luo2025.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:31:26+00:00
page_count: 10
status: ok
text_char_count: 58690
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\01_urban_benchmarks\05_UrbanPlanBench_Luo2025.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:31:26+00:00
- Page count: 10
- Status: ok
- Text chars: 58690
- Quality flags: none

## Metadata

- Title: UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large Language Models
- Author: unknown
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

The advent of Large Language Models (LLMs) holds promise for revolutionizing various fields traditionally dominated by human expertise. Urban planning, a professional discipline that fundamentally shapes our daily surroundings, is one such field heavily relying on multifaceted domain knowledge and experience of human experts. The extent to which LLMs can assist human practitioners in urban planning remains largely unexplored. In this paper, we introduce a comprehensive benchmark, UrbanPlanBench, tailored to evaluate the efficacy of LLMs in urban planning, which encompasses fundamental principles, professional knowledge, and management and regulations, aligning closely with the qualifications expected of human planners. Through extensive evaluation, we reveal a significant imbalance in the acquisition of planning knowledge among LLMs, with even the most proficient models falling short of meeting professional standards. For instance, we observe that 70% of LLMs achieve subpar performance in understanding planning regulations compared to other aspects. Besides the benchmark, we present the largest-ever supervised fine-tuning (SFT) dataset, UrbanPlanText, comprising over 30,000 instruction pairs sourced from urban planning exams and textbooks. Our findings demonstrate that fine-tuned models exhibit enhanced performance in memorization tests and comprehension of urban planning knowledge, while there exists significant room for improvement, particularly in tasks requiring domain-specific terminology and reasoning. By making our benchmark, dataset, and associated evaluation and fine-tuning toolsets publicly available at https://github.com/tsinghua-fib-lab/PlanBench, we aim to catalyze the integration of LLMs into practical urban planning, fostering a symbiotic collaboration between human expertise and machine intelligence. 2 ]LC.sc[ 1v72012.4052:viXra

## Outline

- Abstract (page 1)
- 1 Introduction (page 1)
- 2 Benchmarking LLMs on Urban Planning (page 2)
  - 2.1 Construction of UrbanPlanBench (page 2)
  - 2.2 Evaluation Results (page 3)
  - 2.3 Prompting Techniques (page 5)
- 3 Fine-tuning LLMs with UrbanPlanText (page 5)
  - 3.1 Dataset Construction (page 5)
  - 3.2 SFT Data Quality (page 6)
  - 3.3 SFT Results (page 6)
- 4 Related Work (page 7)
- 5 Conclusion and Future Work (page 7)
- References (page 8)
- A Case Study (page 9)
- B Prompt for data generation (page 9)

## Markdown Content

UrbanPlanBench: A Comprehensive Urban Planning Benchmark
for Evaluating Large Language Models
Yu Zheng Longyi Liu Yuming Lin
y_zheng19@mails.tsinghua.edu.cn liulongyi22@mails.ucas.ac.cn linyuming9@foxmail.com
Tsinghua University University of Chinese Academy of Tsinghua University
Beijing, China Sciences Beijing, China
Beijing, China
Jie Feng Guozhen Zhang Depeng Jin
fengjie@tsinghua.edu.cn zhangguozhen@tsingroc.com jindp@tsinghua.edu.cn
Tsinghua University TsingRoc.ai Tsinghua University
Beijing, China Beijing, China Beijing, China
Yong Li
liyong07@tsinghua.edu.cn
Tsinghua University
Beijing, China
5202
rpA
32

Abstract
The advent of Large Language Models (LLMs) holds promise for
revolutionizing various fields traditionally dominated by human
expertise. Urban planning, a professional discipline that fundamentally shapes our daily surroundings, is one such field heavily relying on multifaceted domain knowledge and experience
of human experts. The extent to which LLMs can assist human
practitioners in urban planning remains largely unexplored. In
this paper, we introduce a comprehensive benchmark, UrbanPlanBench, tailored to evaluate the efficacy of LLMs in urban planning,
which encompasses fundamental principles, professional knowledge, and management and regulations, aligning closely with the
qualifications expected of human planners. Through extensive
evaluation, we reveal a significant imbalance in the acquisition
of planning knowledge among LLMs, with even the most proficient models falling short of meeting professional standards. For
instance, we observe that 70% of LLMs achieve subpar performance
in understanding planning regulations compared to other aspects.
Besides the benchmark, we present the largest-ever supervised
fine-tuning (SFT) dataset, UrbanPlanText, comprising over 30,000
instruction pairs sourced from urban planning exams and textbooks. Our findings demonstrate that fine-tuned models exhibit
enhanced performance in memorization tests and comprehension
of urban planning knowledge, while there exists significant room
for improvement, particularly in tasks requiring domain-specific
terminology and reasoning. By making our benchmark, dataset, and
associated evaluation and fine-tuning toolsets publicly available at
https://github.com/tsinghua-fib-lab/PlanBench, we aim to catalyze
the integration of LLMs into practical urban planning, fostering
a symbiotic collaboration between human expertise and machine
intelligence.
2
]LC.sc[
1v72012.4052:viXra

1 Introduction
Recent breakthroughs in Large Language Models (LLMs) [30, 39]
have showcased remarkable capabilities in generating text, reasoning, and knowledge QA, unlocking a plethora of applications
ranging from chatbots [22] to programming copilots [5]. Besides
general-purpose evaluation, assessing their capabilities in specialized domains is crucial for understanding the real-world impact of
LLMs [6, 8, 16, 20]. In this paper, we focus on one critical field, urban
planning, which stands as a cornerstone in shaping modern city
life, yielding profound influence on over 4 billion urban residents
worldwide. Urban planning is a complex endeavor that intertwines
various disciplines, demanding a deep understanding of domain
knowledge. Despite the advent of technological advancements, the
field continues to heavily rely on the expertise and experience of
human planners. For instance, human planners devote substantial
time to tasks such as planning text management, review, and assessment [47]. Moreover, the limitations inherent in human experience
often lead to errors and inefficiencies in planning outcomes [43].
Notably, the integration of LLMs in urban planning contexts
has emerged as a promising avenue, leveraging their pre-trained
world knowledge to tackle complex computational tasks [9, 18,
36, 46, 47]. However, the inherent challenges of hallucination and
vagueness present significant hurdles, particularly when addressing
specialized problems within urban planning [41]. While various
benchmarks such as SuperGLUE [31], BIG-BENCH [25] and CEval [14] have been proposed to evaluate LLM effectiveness in
understanding and solving intricate tasks, the absence of dedicated
benchmarks for urban planning restricts our ability to quantify
the extent to which LLMs acquire specialized knowledge and their
potential to enhance the productivity of human planners.
As a human-centered field, matching the performance of human
planners marks a milestone for LLMs and signifies their mastery of
urban planning capabilities. In alignment with the rigorous standards set by the certified urban planner qualification examination in
China, we introduce UrbanPlanBench, a comprehensive benchmark

KDD ’25, August 03–07, 2025, Toronto, ON, Canada
designed to evaluate LLMs across various perspectives of urban
planning, including fundamental principles, professional knowledge, and management and regulations. The benchmark mirrors
the latest available examination standards as of 2022, enabling a
comparative analysis between LLM and human planners, shedding lights on whether current general-purpose LLMs attain a
human-level understanding of urban planning. Leveraging this
benchmark, we scrutinize recent open-source LLMs, including
LLaMA1/2/3/3.1 [21, 30], Gemma1/2 [28, 29], ChatGLM3/4 [11],
Baichuan2 [3], Qwen1.5/2 [2, 37], and Yi [38], as well as commercial LLMs like ChatGPT 3.5/4o, to assess their acquisition of planning skills. Additionally, we also evaluate the effect of prompting
techniques for LLMs including chain of thought (COT) [35] and
retrieval augmented generation (RAG) [10, 17].
Supervised fine-tuning (SFT) stands as a prevalent method to
build domain-specific LLMs. However, to our knowledge, there are
currently no off-the-shelf resources for fine-tuning LLMs specifically for urban planning. This gap arises from the significant disparity between the distribution of urban planning knowledge in descriptive texts and the required form of SFT data, which necessitates
sample pairs comprising instructions and responses. To bridge this
gap, we further introduce UrbanPlanText, the largest-ever dataset
tailored for SFT of LLMs in urban planning. Comprising over 30,000
instruction pairs derived from textbooks and past exams, UrbanPlanText serves as a comprehensive collection of specialized urban
planning contents.
We conduct extensive experiments to assess current advanced
LLMs on UrbanPlanBench. While LLMs demonstrate significantly
better performance than random guessing, there remains large
room for improvement, indicating a limited mastery of urban planning skills. Notably, most of the current LLMs can not surpass the
certification bar of the urban planner qualification examination,
which roughly represents the top 10% proficiency level of human
planners. Additionally, our analysis highlights an imbalance in LLM
performance across three key urban planning perspectives: they exhibit greater proficiency in understanding planning principles and
knowledge but tend to falter in memorizing regulations, leading
to factual errors. Moreover, we find that finetuning LLMs with UrbanPlanText can effectively enhance their ability to answer urban
planning-related questions. By introducing both UrbanPlanBench
and UrbanPlanText, we aim to facilitate the seamless integration of
LLMs into practical urban planning workflows, thereby lowering
entry barriers for practitioners and enabling them to fully leverage
advanced AI tools in their work.
2 Benchmarking LLMs on Urban Planning
2.1 Construction of UrbanPlanBench
The motivation for UrbanPlanBench stems from the need to quantitatively assess the extent to which LLMs acquire expertise in urban
planning. Specifically, we aim to answer the fundamental question
of whether LLMs can match the proficiency of human planners,
given that urban planning is inherently a human-centered field. To
achieve this goal, we have constructed UrbanPlanBench based on
the latest available real-world urban planning qualification exam in
China, which serves as the standard for certifying registered urban

Zheng et al.
MCQ-S MCQ-M
The following is a multiple-choice question from the The following is a multiple-choice question from the
examination on fundamental principles of urban examination on professional knowledge of urban planning
planning in China, please select the only one single in China, please select the correct 2-4 options.
correct option. Which techniques can be used for urban 3D data collection?
W na h tu ic r h a l o r n e e se o r f v e th ? e followings is not part of the system of A. interferometric radar
A. forest part B. laser radar
B. ocean park C. Global Navigation Satellite System
C. geological park D. photogrammetry
D. country park E. virtual reality
Answer: D Answer: ABCD
Figure 1: Example questions of UrbanPlanBench. MCQ-S has
four options where only one option is correct. MCQ-M is
more challenging, featuring two to four correct options from
a total of five options. Contents are translated from Chinese
to English.
planners. This benchmark evaluates LLMs from the following three
critical perspectives (subjects) of urban planning:
• S1: Fundamental principles. This subject delves into topics
concerning cities and urban development, basic know-how of
urban planning, urban land use and spatial layout, as well as
practical implementation of urban planning. It reflects LLMs’
grasp of the foundational theories underlying urban development
and the discipline of urban planning.
• S2: Professional knowledge. This subject covers knowledge
from eight professional fields that are closely related to urban
planning, which include architecture, urban transportation, municipal public facilities, information technology application in
urban planning, urban economics, urban geography, urban sociology, and urban ecology and environment. It measures LLMs’
proficiency, familiarity, and comprehension across various disciplines relevant to urban planning.
• S3: Management and regulations. Management covers urban
planning formulation and approval management, implementation management, supervision and inspection, and professional
ethics. Regulations include foundational knowledge in administrative and urban planning laws, complementary regulations,
technical standards and specifications, and other relevant laws
and policies.
By incorporating the above diverse perspectives, UrbanPlanBench
forms a challenging testbed that comprehensively evaluates the
mastery of urban planning skills for LLMs, shedding light on their
capabilities in this complex domain.
In constructing UrbanPlanBench, we adopted the widely used
multiple-choice question (MCQ) format [12], due to its efficacy in
assessing LLMs’ understanding and reasoning capabilities, with
rigorously defined accuracy. For each of the three aforementioned
perspectives, we crafted 100 MCQs. In each category, the initial 80
MCQs feature four choices, with only one correct answer (MCS-S).
To further challenge the LLMs, the remaining 20 MCQs in each
perspective include five choices, with two to four correct options
(MCQ-M). It is worth noting that MCQ-M questions are much
more difficult than MCQ-S questions, as the accuracy of random
guess drops from 25% to 4%. All questions in UrbanPlanBench were
curated from PDF or Microsoft Word documents, and meticulously
transformed into a structured CSV format through careful parsing
and annotation by the authors. These questions were presented to
the LLMs through prompts, as demonstrated in Figure 1.

UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large
Table 1: Accuracy (%) of LLMs on three subjects of UrbanPlanB
multiple correct answers, respectively. Full represents the ov
S1
Model
S M
Random 25.0 4.0
LLaMA-7B 28.8 15.0
LLaMA-13B 25.0 15.0
LLaMA-30B 26.3 15.0
LLaMA2-13B 27.5 15.0
LLaMA3-8B-base 42.5 10.0
LLaMA3-8B-chat 46.3 15.0
LLaMA3.1-8B 56.3 10.0
LLaMA3.1-70B 42.5 10.0
LLaMA3.1-405B 48.8 5.0
Gemma-7B 26.3 5.0
Gemma2-9B 23.8 5.0
GPT-3.5-turbo 51.3 0.0
GPT-4o-mini 35.0 5.0
ChatGLM3-6B-base 47.5 5.0
ChatGLM3-6B-chat 38.8 5.0
ChatGLM4-9B 56.3 10.0
Baichuan2-7B-base 50.0 5.0
Baichuan2-7B-chat 36.3 5.0
Qwen1.5-7B-base 53.8 15.0
Qwen1.5-7B-chat 47.5 15.0
Qwen1.5-110B 60.0 15.0
Qwen2-7B 66.3 15.0
Qwen2-70B 70.0 30.0
Yi-6B-base 61.3 15.0
Yi-6B-chat 62.5 0.0
Cert. Bar (top 10% human) - -
In the context of the urban planner qualification exams, achieving
a score of 60 out of 100 MCQs correctly answered across all subjects
stands as a crucial criterion for certification. These exams pose a
significant challenge even for human participants, with only 10%
passing annually. Therefore, if LLMs can consistently answer 60
MCQs correctly across the three subjects, it suggests they have
attained a level of urban planning expertise comparable to that of
registered human planners, signifying the top 10% of human-level
proficiency. By adhering to the rigorous standards set by real-world
examinations, our constructed benchmark aims to offer tangible
insights into the capabilities of LLMs that can be directly compared
with those of human planners. Subsequently, we evaluate a diverse
array of advanced LLMs on this benchmark to comprehensively
scrutinize their urban planning abilities.
2.2 Evaluation Results
In our experimental evaluation, we prompted multiple advanced
LLMs to respond to all questions presented in the introduced UrbanPlanBench. For each question, we selected the option with the
highest output probability by each LLM as its final response [12],
and then calculated the average accuracy within different subjects.
Table 1 illustrates the benchmarking results of LLMs, detailing the

uage Models KDD ’25, August 03–07, 2025, Toronto, ON, Canada
ch. S and M indicate MCQs with one single correct answer and
l accuracy of both types of MCQs.
S2 S3
l S M Full S M Full
25.0 4.0 20.8 25.0 4.0 20.8
27.5 5.0 23.0 21.3 0.0 17.0
26.3 5.0 23.0 23.8 0.0 19.0
25.0 5.0 22.0 32.5 0.0 26.0
28.8 5.0 24.0 20.0 0.0 16.0
53.7 20.0 47.0 37.5 0.0 30.0
58.8 25.0 52.0 38.8 0.0 31.0
46.3 10.0 39.0 43.8 0.0 35.0
53.8 20.0 47.0 37.5 0.0 30.0
41.3 5.0 34.0 47.5 10.0 40.0
22.5 0.0 18.0 27.5 0.0 22.0
21.3 0.0 17.0 27.5 5.0 23.0
53.8 15.0 46.0 32.5 15.0 29.0
40.0 10.0 34.0 35.0 10.0 30.0
60.0 25.0 53.0 50.0 5.0 41.0
51.3 30.0 47.0 41.3 5.0 34.0
73.8 5.0 60.0 61.3 10.0 51.0
47.5 0.0 38.0 38.8 15.0 34.0
51.3 25.0 46.0 40.0 0.0 32.0
60.0 10.0 50.0 53.8 10.0 45.0
63.8 15.0 54.0 48.8 5.0 40.0
82.5 35.0 73.0 63.8 45.0 60.0
70.0 25.0 61.0 65.0 10.0 54.0
0 77.5 45.0 71.0 68.8 45.0 64.0
65.0 5.0 53.0 60.0 10.0 50.0
70.0 30.0 62.0 56.3 5.0 46.0
- - 60.0 - - 60.0
accuracy for both the 80 MCQ-S (single correct option) questions
and the 20 MCQ-M (multiple correct options) questions separately,
along with the accuracy for the entire set of 100 questions within
each subject.
2.2.1 Overall planning capabilities. We have the following empirical findings:
• We observe that current advanced LLMs demonstrate a substantial level of proficiency in urban planning expertise. Across all
three subjects, the accuracy rates of all LLMs notably surpass random guess predictions, indicating the effectiveness of large-scale
pretraining and supervised fine-tuning in equipping these models with urban planning memorization and reasoning abilities.
Specifically, the highest-performing LLM achieves approximately
2.98, 3.51, and 3.08 times higher accuracy than random guess predictions in fundamental principles, professional knowledge, and
management and regulations, respectively. Moreover, we observe
that 9 LLMs achieve at least 50.0% accuracy in at least one subject,
underscoring their mastery of urban planning expertise.
• Despite these promising results, LLMs still lag significantly behind professional human planners in terms of performance. All

KDD ’25, August 03–07, 2025, Toronto, ON, Canada
25 evaluated LLMs, except for Qwen2-70B, fail to exceed the certification bar for professional human planners, i.e. 60.0% accuracy
in all three subjects. Specifically, out of 75 cases comprising 25
different LLMs and 3 subjects, only 8 times does an LLM exceed
the 60% accuracy certification bar which roughly aligns with top
10% human proficiency levels. This indicates that most of the
LLMs evaluated in this study are not capable of passing the urban
planning qualification exam, highlighting their insufficient urban
planning capabilities compared to certified human planners.
• We find that LLMs perform notably worse on MCQ-M questions
compared to MCQ-S questions. This discrepancy is understandable, given the increased complexity of MCQ-M questions, which
feature a set of 25 potential answers, much larger than MCQ-S
questions that only have 4 potential answers. Specifically, we
observe zero accuracy in 15 out of 75 cases, indicating a performance level even below random guess predictions. These findings
suggest that, while most existing benchmarks for LLMs primarily focus on MCQ-S questions, it may be necessary to include
more challenging MCQ-M tests to comprehensively evaluate
the capabilities of LLMs in specialized domains such as urban
planning.
• Surprisingly, we find that Qwen2-70B achieved accuracy of 62.0%,
71.0%, and 64.0% on the three subjects, making it the first and
only LLM to surpass the 60% certification threshold of professional human planners. The inspiring results highlight the huge
potential of LLMs to assist human planners in practical urban
planning tasks.
2.2.2 Subject imbalance. The results in Table 1 reveal an obvious
imbalance in the performance of LLMs across the three distinct
subjects evaluated in UrbanPlanBench. Specifically, we find that
the average accuracy of the 25 LLMs on the three subjects is 38.24%,
44.16%, and 34.52%, respectively. Particularly, LLMs demonstrate
significantly better performance on S2 (professional knowledge)
compared to the other two subjects, S1 (fundamental principles)
and S3 (management and regulations). Moreover, 68% LLMs achieve
accuracy lower than 45.0% in both S1 and S3, and only 16% models
achieves over 50.0% accuracy in these two subjects.
Upon closer examination of the definitions of the three subjects,
we observe that S2 covers a broader range of general and diverse
topics, potentially overlapping with the pretraining and SFT data of
these LLMs. In contrast, S1 and S3 focus more on domain-specific
contents, emphasizing specialized urban planning concepts that
may be insufficiently represented in the training data. These findings underscore the need to develop a specialized SFT dataset tailored specifically to urban planning to enhance the performance of
LLMs in this critical domain.
2.2.3 Language bias. UrbanPlanBench is a Chinese benchmark
sourced from questions of urban planning exams in China, thus
most of the evaluated LLMs are also Chinese LLMs which are pretrained and finetuned with large-scale Chinese textual data. Still, we
include three English-primary LLM series for comparison, namely
LLaMA, Gemma, and GPT. The results highlight a notable difference between the performance of Chinese LLMs and two Englishprimary LLMs, particularly evident in S3 (management and regulations). The average accuracy of the three English-primary LLM
series in S3 is 26.77%, representing a significant 41.7% relative gap

Zheng et al.
S1 S2 S3
70
65
60
55
50
45
40
35
30
0.5B 1.8B 4B 7B 14B 32B
model size
ycarucca
S-QCM
S1 S2 S3
20
15
10
5
0
0.5B 1.8B 4B 7B 14B 32B
model size
ycarucca
M-QCM
Figure 2: Performance of different model sizes. The LLM
model Qwen1.5 is adopted. MCS-S and MCQ-M indicate MCQs
with one single correct answer and multiple correct answers,
respectively. (Left) Accuracy on MCQ-S questions. (Right)
Accuracy on MCQ-M questions.
compared to the other twelve Chinese LLMs, which exhibit an
average accuracy of 45.92%.
The disparity in performance between the English-primary LLMs
and other Chinese LLMs is less pronounced in S1 and S2, with gaps
of 8.9% and 1.8%, respectively. For example, the LLaMA3.1-8B and
LLaMA3-8B-chat model surpass 7 and 4 Chinese LLMs in terms of
accuracy in S1 and S2, respectively. These results suggest a potential
difference in the adaptability of English-primary LLMs compared
to their Chinese counterparts in comprehending and interpreting
the specific regulations and management aspects inherent in urban planning contexts, emphasizing the importance of considering
language-specific nuances in LLM performance evaluation and application.
2.2.4 Scaling effect. Researchers have consistently observed scaling laws of neural language models, particularly LLMs, where
scaling up models can lead to substantial performance improvements [15] and even emergent abilities [34]. From the results we
can observe that larger models generally achieve higher accuracy.
For instance, LLaMA3.1-405B improved the performance by 53.8%,
47.8%, and 135.3% on S1, S2, and S3, respectively, in comparison to
LLaMA-7B.
To further investigate this phenomenon, we evaluated Qwen1.5
models of varying parameter scales, ranging from 0.8B to 32B parameters, on UrbanPlanBench. We calculated accuracy across three
subjects, with MCQ-S and MCQ-M questions examined separately.
The results, depicted in Figure 2, showcase a notable scaling effect,
particularly evident in MCQ-S questions, aligning with previous
literature. Across all three subjects, we observed approximately a
100% increase in accuracy for MCQ-S questions by scaling up models, with the largest improvement of 108.0% seen in S1, followed by
96.3% and 89.7% improvements in S3 and S2, respectively. Remarkably, the Qwen1.5-14B and Qwen1.5-32B models achieved over 60%
accuracy in two of the three subjects, signaling their potential to
rival professional human planners.
These findings underscore the validity of scaling laws in LLMs
where larger models demonstrate enhanced understanding and
reasoning capabilities, as evidenced in our specialized benchmark.
However, we also observed that accuracy on MCQ-M questions
remained low despite increasing model sizes. Given the increasing
difficulty of MCQ-M tests, merely scaling up LLMs may prove
insufficient, necessitating advanced techniques such as retrieval
augmented generation (RAG) [17] to bolster the urban planning

UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large
expertise of LLMs for addressing intricate MCQ-M questions. We
show the benefits of advanced inference-time prompting techniques
in Section 2.3.
2.2.5 Longitudinal studies. To track the evolution of LLM performance over time, we compare different generations of LLMs. We
can observe that later generations of LLMs indeed achieve substantially better performance than their corrsponding earlier version in
most cases. For example, LLaMA3.1-8B improves the accuracy on
S1 by 105% against LLaMA-13B, Qwen2-7B improves the accuracy
on S2 by 17.3% against Qwen1.5-7B, and ChatGLM4-9B improves
the accuracy on S3 by 13.3% against ChatGLM3-6B. The longitudinal studies confirm that the progress made in data quality, model
structure, and training algorithm effectively enhances the ability of
LLMs to understand and deal with complex urban planning problems. Nevertheless, the enhanced model capabilities alone are still
not effective in dealing with MCQ-M questions, indicating the necessity of incorporating advanced techniques such as RAG [17] and
COT [35].
2.3 Prompting Techniques
Prompting techniques can significantly enhance LLMs in answering
complicated questions and improving their reasoning capabilities.
Here in UrbanPlanBench, we use GPT-4o-mini as the base model to
validate the effectiveness of RAG [17] and CoT [35] for knowledge
augmentation of LLMs, as well as to evaluate their enhancement of
LLMs’ competence in the field of urban planning. Table 2 illustrates
the results of different prompting techniques. Specifically, we utilize Self-RAG [1] to retrieve matches in RAG experiments, where
RAG_direct denotes that the relevant textbooks and previous years’
questions are directly used as the content of the knowledge base,
and RAG_qa denotes that these contents are first processed into
high-quality QA. With respect to COT, we adopt both few-shot-CoT
and zero-shot-CoT, denoted as CoT_fs and CoT_zs, respectively.
From the results, we have the following observations:
• RAG prompting. The introduction of RAG significantly improves
the performance on each subject. Specifically, RAG_direct and
RAG_qa improve the accuracy on S1 by 30.3% and 45.5%, respectively, compared to the GPT-4o-mini base model. In S2, RAG_direct
and RAG_qa achieve an overall average accuracy of 64% and 62%,
respectively, and both MCQ-S and MCQ-M are improved by more
than 52.9%, reaching the level of professional urban planners. In
MCQ-M of S3, the GPT-4o-mini base model performs better than
RAG_direct, but the accurate information retrieval still ensures a
high accuracy rate in MCQ-S for RAG models with about 32.5%
improvements against the base model.
• CoT prompting. The introduction of CoT technology leads to
stronger reasoning ability of LLMs and significantly improves
the performance of each subject. Specifically, CoT_fs and CoT_zs
improved the accuracy by 54.5% and 36.4% in S1, 70.3% and 75.7%
in S2, and 43.2% and 29.7% in S3, respectively. Notably, COT
substantially improves the performance of LLMs in answering
MCQ-M questions. For example, COT_zs increases the accuracy
on MCQ-M by 100%, 600%, and 133% in the three subjects. As
there exist more than one correct options in MCQ-M questions
which are much more complicated than MCQ-S ones, the above

uage Models KDD ’25, August 03–07, 2025, Toronto, ON, Canada
results confirm the effectiveness of COT in boosting the reasoning
ability of LLMs.
The above benchmarking results illustrate the large potential of
LLMs in urban planning. In practical urban planning scenarios,
LLMs can be smoothly integrated into planners’ workflow using
appropriate prompts, and we provide two example cases of urban
planning text polishment and proofreading in Appendix A.
3 Fine-tuning LLMs with UrbanPlanText
The inherent knowledge of LLMs proves insufficient when confronted with specialized urban planning queries, highlighting a
deficiency in domain-specific understanding. SFT emerges as a
widely adopted technique for tailoring LLMs towards specific domains by infusing them with related knowledge and data. Notably,
SFT datasets for LLMs typically consist of sample pairs comprising
instructions and corresponding responses. However, existing urban planning knowledge is scattered across unannotated textual
resources, presenting a challenge in sourcing relevant data for SFT.
Towards this end, we initially gathered materials from seven urban
planning textbooks, along with archives of urban planning exams
spanning the past eight years. Subsequently, we derive instruction
pairs from these materials, leading to the largest-ever SFT dataset
tailored for urban planning.
3.1 Dataset Construction
Data Sources. Our urban planning textual data collection primarily
focuses on two key sources: urban planning textbooks and past
urban planning exams, with the overview of the dataset’s statistics
shown in Table 3. Urban planning textbooks encompass a wide spectrum of general knowledge about urban planning, thus leveraging
data from textbooks enables LLMs to establish a foundational understanding of the specific domain, mirroring the approach taken by
human planners who frequently refer to textbooks as their primary
learning and training resources.
In addition, questions found in urban planning exams adhere to
specific formats and emphasize particular areas. Therefore, finetuning LLMs with data extracted from real exams serves to further
refine their abilities, enhancing their accuracy in addressing domainspecific exam questions. Particularly, as the introduced benchmark
UrbanPlanBench is sourced from the latest publicly available urban
planning exam in China held in 2022, we utilize exam questions
predating 2022 for the collection of SFT data, spanning eight years.
Data Processing. The collected original materials encompass a
variety of formats, predominantly stored as PDF or Microsoft Word
documents. To facilitate further processing, these materials are first
parsed into plain text format. In the case of urban planning exams
from previous years, an additional step is taken to transform these
MCQs into a structured CSV format before they are processed into
instruction pairs. These instruction pairs are designed to include
the system prompt, the question itself, and the provided options,
while the response comprises the correct answer accompanied by
explanations. Meanwhile, dialog-style instruction pairs are derived
from MCQs to further enrich the training materials, as depicted in
Figure 3.
For urban planning textbooks, which primarily contain descriptive text without readily available instruction pairs, more data

KDD ’25, August 03–07, 2025, Toronto, ON, Canada
Table 2: Accuracy (%) on three subjects of UrbanPlanBench u
single correct answer and multiple correct answers, respectiv
S1
Model
S M
GPT-4o-mini 40.0 5.0
RAG_direct 52.5 5.0
RAG_qa 58.8 5.0
COT_fs 60.0 15.0
COT_zs 53.8 10.0
Cert. Bar (top 10% human) - -
Table 3: Statistics of different sources for UrbanPlanText.
Category Name #Words #Samples
MCQ 619,810 2,397
Past Exams
dialog 350,080 4,139
Principles of
470,621 5,091
urban planning
Knowledge of
457,236 9,307
urban planning
Urban planning management
313,246 4,347
and regulations
Textbooks Urban planning practice 120,155 3,589
Detailed regulatory plan 174,626 246
History of urban
156,923 608
construction in China
Additional contents of
60,371 1,610
urban planning exams
Total 2,723,068 31,334
instruction:
MCQ T fu h n e d f a o m llo e w nt in al g p i r s i n a c m ip u le lt s i p o l f e u -c rb ho an ic e p l q a u n e n s in ti g o n in f r C o h m in a th , e p l e e x a a s m e i s n e a le ti c o t n t h o e n
correct option. Which statement is wrong? A.**, B.**, C.**, D.**.
Que A B C D Ans Exp response:
*** * * * * *** **** B. Explanation: ***
*** * * * * *** ****
Past Exams *** * * * * *** **** i W ns h t y r u ** c * t i i o s n w : rong? Extracted from question
dialog r * e ** s . ponse: Extracted from explanation
instruction:
The city is an integrated giant system, which Please briefly describe the components of the
includes economic subsystems, political urban system.
Textbooks s e s r u o r b e e u u n p v e l s b b e v a h p i s s r t a t r o l i y y h o a v o n s s i p e n n o t t d e e m s r w m m h s u t e . i i o r p t s s n b h , . t a a b e n e c a T s t e c s s u h w r h o y b e t e s c a r s o e t i e i y a e n t n s h l m t e e e t , h r x i m , s t e w e f s s u u n h e n b t a i l c c e s a t h t m y n o i s o d e t v i n v e n n e a m t r t t r e s o y f i s a r o g , t c t u w e h t s o t c a i h n r o t h e s e m u p m r m f a p a a l a t o l n n a k i e a w d d n e x l r T i s e s r c n e e u u o n h c l s b b n v e a l p u i s s t t r u i r o y y d o o i r s s b n i n n b n t t u s e e m s a g e t m m h n e e : e i p s s n s t c , . y o t o w s T s s n o t t h i u h e t o c e h b m e i m s a s e e o l y i i a c s s v s s c u t e u s a h e b u r b n m a s b o s l y i y l s s t n s h s y o t a t t s e e p e e n t r g m e e m , d r r m a s a a s f n , a t t s h d e i s , c o p a d t p t n o v a o o g e r t a g l i i i a f a n a t e l i l n o d t c c h t w a o e l s m r y s t p t h l e e e m x y ,
development of the city.
Figure 3: Data collection and process of UrbanPlanText. Past
exam questions are first annotated by the authors into structured CSV files and then transformed into MCQ-type instruction pairs and dialog-style instruction pairs. Textbooks are
first parsed into textual files, from which instruction pairs
are generated automatically by prompting OpenAI’s ChatGPT model. Contents are translated from Chinese to English.
process is needed. Here, we employ OpenAI’s ChatGPT to automatically generate instruction pairs from the descriptive text by
prompting, as demonstrated in Figure 3. This process ensures the
conversion of all collected materials into a standardized format suitable for subsequent SFT. The prompt template of data generation is
provided in Appendix B.

Zheng et al.
g RAG and CoT techniques. S and M indicate MCQs with one
Full represents the overall accuracy of both types of MCQs.
S2 S3
l S M Full S M Full
45.0 5.0 37.0 42.5 15.0 37.0
68.8 45.0 64.0 53.8 5.0 48.0
70.0 30.0 62.0 56.3 20.0 49.0
70.0 35.0 63.0 58.8 25.0 53.0
72.5 35.0 65.0 51.3 35.0 48.0
- - 60.0 - - 60.0
Table 4: Correctiveness and informativeness of the generated
SFT data by human experts.
Model
Expert Metric
ChatGPT Ernie Bonito
Correctiveness 9.6 9.6 7.2
1
Informativeness 9.4 8.8 5.8
Correctiveness 9.2 7.4 7.6
2
Informativeness 8.4 6.8 7.6
Correctiveness 6.2 6.0 5.2
3
Informativeness 6.2 6.2 4.6
Correctiveness 8.8 8.0 4.8
4
Informativeness 8.6 7.4 4.2
Correctiveness 7.6 7.4 6.4
5
Informativeness 7.6 7.6 5.2
3.2 SFT Data Quality
In our experiments, we tried different approaches to generate instruction pairs including OpenAI’s ChatGPT, Ernie, and the opensourced Bonito framework. Eventually we employed OpenAI’s
ChatGPT due to its better performance. It is worthwhile to notice
that using LLMs to generate training data has become a common
practice proven to be effective and widely adopted by related literature [4, 7]. To verify the data quality, we invited five domain experts
with graduated degree in urban planning to judge the generated
instruction pairs, comparing different approaches. Specifically, we
sample 100 instruction pairs generated by different approaches,
and asked the domain experts to score the generated data from the
perspective of both correctiveness and informativeness. The results
are demonstrated in Table 4.
3.3 SFT Results
We leveraged our constructed UrbanPlanText dataset to fine-tune
LLMs using LLaMA-Factory [45]. Employing lora [13] to accelerate
the SFT process, we fine-tuned all models for three epochs on one
single Nvidia A100 GPU, which takes about 4 hours. Subsequently,
we evaluated the fine-tuned LLMs again on UrbanPlanBench, with
the results detailed in Table 5. Notably, we observed a significant
enhancement in performance, particularly in S3 (management and
regulations). Specifically, 60% of LLMs exhibited improved accuracy
on full questions of S3, and 70% demonstrated enhanced accuracy
on the MCQ-S questions of S3, with the average accuracy of LLMs
improved by 2.1% compared to their pre-SFT counterparts. Given
that S3 was previously the weakest subject for LLMs according to

UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large
Table 5: Accuracy (%) of LLMs on three subjects of UrbanPlanBench after SFT on UrbanPlanText. S and M indicate
MCQs with one single correct answer and multiple correct
answers, respectively. Full represents the overall accuracy of
both types of MCQs. Bold numbers indicate that the performance improves against the corresponding pre-SFT model.
S1 S2 S3
Model
S M Full S M Full S M Full
LLaMA3-8B-base 40.0 5.0 33.0 57.5 25.0 51.0 41.3 0.0 33.0
LLaMA3-8B-chat 42.5 10.0 36.0 51.3 10.0 43.0 33.8 5.0 28.0
ChatGLM3-6B-base 50.0 5.0 41.0 58.8 35.0 54.0 55.0 5.0 45.0
ChatGLM3-6B-chat 35.0 5.0 29.0 52.5 25.0 47.0 42.5 5.0 35.0
Baichuan2-7B-base 46.3 5.0 38.0 56.3 5.0 46.0 43.8 15.0 38.0
Baichuan2-7B-chat 43.8 5.0 36.0 46.3 20.0 41.0 31.3 0.0 25.0
Qwen1.5-7B-base 50.0 10.0 42.0 63.8 5.0 52.0 53.8 10.0 45.0
Qwen1.5-7B-chat 48.8 15.0 42.0 63.8 5.0 52.0 50.0 10.0 42.0
Yi-6B-base 58.8 15.0 50.0 68.8 0.0 55.0 61.3 0.0 49.0
Yi-6B-chat 62.5 0.0 50.0 66.3 35.0 60.0 63.8 0.0 51.0
Table 1, these findings underscore the effectiveness of enhancing the
domain-specific capabilities of LLMs through SFT. Additionally, for
the previously strongest subject, S2 (professional knowledge), LLMs
maintained competitive performance, with an average accuracy of
50.1%, similar to the pre-SFT average accuracy of 50.2%.
Additionally, we conducted SFT experiments on LLMs of varying
sizes using UrbanPlanText and subsequently evaluated their performance on UrbanPlanBench. Aligning with previous benchmarking
experiments, we still employed the Qwen1.5 model across a spectrum of parameter sizes ranging from 0.8B to 32B. We illustrated
their post-SFT performance in Figure 4. Similar to previous observations, we can observe a clear scaling effect on the accuracy of
MCQ-S questions, with larger models demonstrating substantially
improved performance compared to their smaller counterparts.
Particularly, we noted that SFT yielded more substantial benefits
for smaller models. For instance, the average accuracy on MCQ-S
questions across all three subjects increased by 11.1%, 1.7%, and
6.0% for the smallest three models (0.5B, 1.8B, and 4B) compared to
previous results in Figure 2, respectively, while the improvement
was only 0.7% for the largest 32B model. These findings hold significant practical implications, particularly as smaller models are
more accessible to a broader user base at a considerably lower cost.
Similar to previous findings, the accuracy on MCQ-M questions
does not improve with growing model sizes, which again confirming the inherent difficulty of MCQ-M questions. The results in
Figure 4, in comparison to Section 2.3, suggest that combining SFT
and advanced prompting techniques can enhance performance on
challenging questions and lead to better overall accuracy.
4 Related Work
AI for urban planning. AI applications in urban planning offer
promising solutions to the challenges posed by rapid urbanization,
aiming to alleviate the burden on human planners [42]. Current
research predominantly focuses on urban design, generating layouts of various urban functionalities such as land use [43], transportation networks [27, 44], buildings [24], and points of interest
(POIs) [32]. These endeavors approach urban design as either a
generation problem, utilizing existing urban data and generative

uage Models KDD ’25, August 03–07, 2025, Toronto, ON, Canada
S1 S2 S3
70
65
60
55
50
45
40
35
30
0.5B 1.8B 4B 7B 14B 32B
model size
ycarucca
S-QCM
S1 S2 S3
20
15
10
5
0
0.5B 1.8B 4B 7B 14B 32B
model size
ycarucca
M-QCM
Figure 4: Performance of different model sizes after SFT on
UrbanPlanText. The LLM model Qwen1.5 is adopted. MCS-S
and MCQ-M indicate MCQs with one single correct answer
and multiple correct answers, respectively. (Left) Accuracy
on MCQ-S questions. (Right) Accuracy on MCQ-M questions.
models like diffusion models [24] and generative adversarial networks (GANs) [32], or as an optimization problem tackled through
methods such as reinforcement learning (RL) [26, 27, 43, 44] to find
more efficient layouts. Despite urban design, urban planners still
devote significant time to handling urban planning-related text.
The emergence of LLMs has led to the development of specialized
models tailored for urban planning tasks [33, 40, 47]. For instance,
TransGPT [33] fine-tunes LLMs with large-scale transportation
text to assist in transportation planning, while PlanGPT [47] equips
LLMs with external knowledge and web search capabilities for various text-related tasks in urban planning. However, these efforts
often rely on case studies to demonstrate the effectiveness of LLMs
in urban planning, underscoring the urgent need for a comprehensive benchmark to quantitatively assess the extent to which LLMs
masters urban planning knowledge.
Domain-specific benchmarks for LLMs. Benchmarks play a
pivotal role in shaping the trajectory of AI research, serving as foundational tools that drive progress within the field [23]. LLMs have
demonstrated exceptional understanding, reasoning, and memorization abilities, as evidenced by benchmarks such as SuperGLUE [31],
BIG-Bench [25], MMLU [12], and HELM [19], which cover diverse
Natural Language Processing (NLP) tasks. While general-purpose
NLP benchmarks have provided valuable insights into LLM capabilities, domain-specific benchmarks are indispensable to understand LLMs’ specialized expertise [6, 8, 16, 20]. Examples include
LawBench [8], which evaluates LLMs’ legal capabilities in memorization, understanding, and application of legal knowledge, and
BizBench [16], which assesses LLMs’ ability to reason about financial problems and synthesize code to accomplish Q&A tasks over
financial data. Additionally, MathBench [20] evaluates LLMs’ mathematical proficiency in answering theoretical questions and solving
application problems. However, within the realm of urban planning, there is a notable absence of publicly available benchmarks,
impeding the effective utilization of LLMs in this critical domain. In
response to this gap, this paper proposes the first urban planning
benchmark for LLMs, aiming to comprehensively evaluate their
capabilities and guide technological advancements in this field.
5 Conclusion and Future Work
This paper introduces UrbanPlanBench and UrbanPlanText, the first
urban planning benchmark and the largest-ever SFT dataset tailored

KDD ’25, August 03–07, 2025, Toronto, ON, Canada
for LLMs. These resources, along with open-sourced toolsets, provide comprehensive support for fine-tuning and evaluating LLMs
in the critical domain of urban planning. Through a series of experiments involving multiple advanced LLMs, we have showcased their
remarkable capabilities in mastering urban planning knowledge.
However, there remains substantial untapped potential to fully
leverage LLMs to enhance the productivity of human practitioners
in this field. We envision that our findings will foster interdisciplinary collaboration between human planners and AI practitioners,
paving the way for further exploration and the application of LLMs
in influential real-world urban planning scenarios. Moving forward,
our future work includes expanding both UrbanPlanBench and
UrbanPlanText to incorporate multi-linguistic urban planning materials, thereby enabling broader use cases of the benchmark and
dataset. Additionally, we aim to extend UrbanPlanBench into a
multi-modal benchmark, integrating both imagery of urban plans
and their corresponding descriptive text, further enriching the evaluation capabilities of LLMs in urban planning contexts.
References
[1] Akari Asai, Zeqiu Wu, Yizhong Wang, Avirup Sil, and Hannaneh Hajishirzi. 2023.
Self-rag: Learning to retrieve, generate, and critique through self-reflection. arXiv
preprint arXiv:2310.11511 (2023).
[2] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan,
Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji
Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men,
Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng
Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang,
Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng
Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang
Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. 2023. Qwen Technical
Report. arXiv preprint arXiv:2309.16609 (2023).
[3] Baichuan. 2023. Baichuan 2: Open Large-scale Language Models. arXiv preprint
arXiv:2309.10305 (2023). https://arxiv.org/abs/2309.10305
[4] James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long
Ouyang, Juntang Zhuang, Joyce Lee, Yufei Guo, et al. 2023. Improving image generation with better captions. Computer Science. https://cdn. openai.
com/papers/dall-e-3. pdf 2, 3 (2023), 8.
[5] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira
Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman,
et al. 2021. Evaluating large language models trained on code. arXiv preprint
arXiv:2107.03374 (2021).
[6] Qiyuan Chen and Cheng Deng. 2023. Bioinfo-Bench: A Simple Benchmark
Framework for LLM Bioinformatics Skills Evaluation. bioRxiv (2023), 2023–10.
[7] Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller,
Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, et al. 2024.
Scaling rectified flow transformers for high-resolution image synthesis. In Fortyfirst International Conference on Machine Learning.
[8] Zhiwei Fei, Xiaoyu Shen, Dawei Zhu, Fengzhe Zhou, Zhuo Han, Songyang Zhang,
Kai Chen, Zongwen Shen, and Jidong Ge. 2023. Lawbench: Benchmarking legal
knowledge of large language models. arXiv preprint arXiv:2309.16289 (2023).
[9] Jiayi Fu, Haoying Han, Xing Su, and Chao Fan. 2024. Towards human-AI collaborative urban science research enabled by pre-trained large language models.
Urban Informatics 3, 1 (2024), 8.
[10] Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai,
Jiawei Sun, and Haofen Wang. 2023. Retrieval-augmented generation for large
language models: A survey. arXiv preprint arXiv:2312.10997 (2023).
[11] Team GLM, Aohan Zeng, Bin Xu, Bowen Wang, Chenhui Zhang, Da Yin, Diego
Rojas, Guanyu Feng, Hanlin Zhao, Hanyu Lai, et al. 2024. ChatGLM: A Family
of Large Language Models from GLM-130B to GLM-4 All Tools. arXiv preprint
arXiv:2406.12793 (2024).
[12] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn
Song, and Jacob Steinhardt. 2020. Measuring Massive Multitask Language Understanding. In International Conference on Learning Representations.
[13] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean
Wang, Lu Wang, and Weizhu Chen. 2021. Lora: Low-rank adaptation of large
language models. arXiv preprint arXiv:2106.09685 (2021).
[14] Yuzhen Huang, Yuzhuo Bai, Zhihao Zhu, Junlei Zhang, Jinghan Zhang, Tangjun
Su, Junteng Liu, Chuancheng Lv, Yikai Zhang, Jiayi Lei, Yao Fu, Maosong Sun,

Zheng et al.
and Junxian He. 2023. C-Eval: A Multi-Level Multi-Discipline Chinese Evaluation Suite for Foundation Models. In Advances in Neural Information Processing
Systems.
[15] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess,
Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. 2020.
Scaling laws for neural language models. arXiv preprint arXiv:2001.08361 (2020).
[16] Rik Koncel-Kedziorski, Michael Krumdick, Viet Lai, Varshini Reddy, Charles
Lovering, and Chris Tanner. 2023. Bizbench: A quantitative reasoning benchmark
for business and finance. arXiv preprint arXiv:2311.06602 (2023).
[17] Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir Karpukhin,
Naman Goyal, Heinrich Küttler, Mike Lewis, Wen-tau Yih, Tim Rocktäschel,
et al. 2020. Retrieval-augmented generation for knowledge-intensive nlp tasks.
Advances in Neural Information Processing Systems 33 (2020), 9459–9474.
[18] Zhonghang Li, Lianghao Xia, Jiabin Tang, Yong Xu, Lei Shi, Long Xia, Dawei Yin,
and Chao Huang. 2024. Urbangpt: Spatio-temporal large language models. arXiv
preprint arXiv:2403.00813 (2024).
[19] Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al.
2022. Holistic evaluation of language models. arXiv preprint arXiv:2211.09110
(2022).
[20] Hongwei Liu, Zilong Zheng, Yuxuan Qiao, Haodong Duan, Zhiwei Fei, Fengzhe
Zhou, Wenwei Zhang, Songyang Zhang, Dahua Lin, and Kai Chen. 2024. MathBench: Evaluating the Theory and Application Proficiency of LLMs with a Hierarchical Mathematics Benchmark. arXiv preprint arXiv:2405.12209 (2024).
[21] Meta. 2024. Introducing Meta Llama 3: The most capable openly available LLM
to date. https://ai.meta.com/blog/meta-llama-3/.
[22] OpenAI. 2022. ChatGPT. https://chat.openai.com.
[23] David Patterson. 2012. For better or worse, benchmarks shape a field. Commun.
ACM 55 (2012).
[24] Yiming Qin, Nanxuan Zhao, Bin Sheng, and Rynson WH Lau. 2024. Text2City:
One-Stage Text-Driven Urban Layout Regeneration. In Proceedings of the AAAI
Conference on Artificial Intelligence, Vol. 38. 4578–4586.
[25] Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb,
Abubakar Abid, Adam Fisch, Adam R Brown, Adam Santoro, Aditya Gupta,
Adrià Garriga-Alonso, et al. 2022. Beyond the imitation game: Quantifying and
extrapolating the capabilities of language models. arXiv preprint arXiv:2206.04615
(2022).
[26] Hongyuan Su, Yu Zheng, Jingtao Ding, Depeng Jin, and Yong Li. 2024. Largescale Urban Facility Location Selection with Knowledge-informed Reinforcement
Learning. In Proceedings of the 32nd ACM International Conference on Advances
in Geographic Information Systems. 553–556.
[27] Hongyuan Su, Yu Zheng, Jingtao Ding, Depeng Jin, and Yong Li. 2024. MetroGNN: Metro Network Expansion with Reinforcement Learning. In Companion
Proceedings of the ACM on Web Conference 2024. 650–653.
[28] Gemma Team, Thomas Mesnard, Cassidy Hardin, Robert Dadashi, Surya Bhupatiraju, Shreya Pathak, Laurent Sifre, Morgane Rivière, Mihir Sanjay Kale, Juliette
Love, et al. 2024. Gemma: Open models based on gemini research and technology.
arXiv preprint arXiv:2403.08295 (2024).
[29] Gemma Team, Morgane Riviere, Shreya Pathak, Pier Giuseppe Sessa, Cassidy
Hardin, Surya Bhupatiraju, Léonard Hussenot, Thomas Mesnard, Bobak Shahriari,
Alexandre Ramé, et al. 2024. Gemma 2: Improving open language models at a
practical size. arXiv preprint arXiv:2408.00118 (2024).
[30] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, et al. 2023. Llama: Open and efficient foundation language models. arXiv
preprint arXiv:2302.13971 (2023).
[31] Alex Wang, Yada Pruksachatkun, Nikita Nangia, Amanpreet Singh, Julian Michael,
Felix Hill, Omer Levy, and Samuel Bowman. 2019. Superglue: A stickier benchmark for general-purpose language understanding systems. Advances in neural
information processing systems 32 (2019).
[32] Dongjie Wang, Yanjie Fu, Pengyang Wang, Bo Huang, and Chang-Tien Lu. 2020.
Reimagining city configuration: Automated urban planning via adversarial learning. In Proceedings of the 28th international conference on advances in geographic
information systems. 497–506.
[33] Peng Wang, Xiang Wei, Fangxu Hu, and Wenjuan Han. 2024. TransGPT: Multimodal Generative Pre-trained Transformer for Transportation. arXiv preprint
arXiv:2402.07233 (2024).
[34] Jason Wei, Yi Tay, Rishi Bommasani, Colin Raffel, Barret Zoph, Sebastian
Borgeaud, Dani Yogatama, Maarten Bosma, Denny Zhou, Donald Metzler, et al.
2022. Emergent abilities of large language models. arXiv preprint arXiv:2206.07682
(2022).
[35] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi,
Quoc V Le, Denny Zhou, et al. 2022. Chain-of-thought prompting elicits reasoning
in large language models. Advances in neural information processing systems 35
(2022), 24824–24837.
[36] Fengli Xu, Jun Zhang, Chen Gao, Jie Feng, and Yong Li. 2023. Urban generative intelligence (ugi): A foundational platform for agents in embodied city
environment. arXiv preprint arXiv:2312.11813 (2023).

UrbanPlanBench: A Comprehensive Urban Planning Benchmark for Evaluating Large
[37] An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, et al. 2024. Qwen2 technical
report. arXiv preprint arXiv:2407.10671 (2024).
[38] Alex Young, Bei Chen, Chao Li, Chengen Huang, Ge Zhang, Guanwei Zhang,
Heng Li, Jiangcheng Zhu, Jianqun Chen, Jing Chang, et al. 2024. Yi: Open
foundation models by 01. ai. arXiv preprint arXiv:2403.04652 (2024).
[39] Aohan Zeng, Xiao Liu, Zhengxiao Du, Zihan Wang, Hanyu Lai, Ming Ding,
Zhuoyi Yang, Yifan Xu, Wendi Zheng, Xiao Xia, Weng Lam Tam, Zixuan Ma,
Yufei Xue, Jidong Zhai, Wenguang Chen, Zhiyuan Liu, Peng Zhang, Yuxiao Dong,
and Jie Tang. 2023. GLM-130B: An Open Bilingual Pre-trained Model. In The
Eleventh International Conference on Learning Representations (ICLR). https:
//openreview.net/forum?id=-Aw0rrrPUF
[40] Siyao Zhang, Daocheng Fu, Wenzhe Liang, Zhao Zhang, Bin Yu, Pinlong Cai, and
Baozhen Yao. 2024. Trafficgpt: Viewing, processing and interacting with traffic
foundation models. Transport Policy 150 (2024), 95–105.
[41] Yue Zhang, Yafu Li, Leyang Cui, Deng Cai, Lemao Liu, Tingchen Fu, Xinting
Huang, Enbo Zhao, Yu Zhang, Yulong Chen, et al. 2023. Siren’s song in the
AI ocean: a survey on hallucination in large language models. arXiv preprint
arXiv:2309.01219 (2023).
[42] Yu Zheng, Qianyue Hao, Jingwei Wang, Changzheng Gao, Jinwei Chen, Depeng
Jin, and Yong Li. 2024. A Survey of Machine Learning for Urban Decision Making:
Applications in Planning, Transportation, and Healthcare. Comput. Surveys 57, 4
(2024), 1–41.
[43] Yu Zheng, Yuming Lin, Liang Zhao, Tinghai Wu, Depeng Jin, and Yong Li. 2023.
Spatial planning of urban communities via deep reinforcement learning. Nature
Computational Science 3, 9 (2023), 748–762.
[44] Yu Zheng, Hongyuan Su, Jingtao Ding, Depeng Jin, and Yong Li. 2023. Road
planning for slums via deep reinforcement learning. In Proceedings of the 29th
ACM SIGKDD Conference on Knowledge Discovery and Data Mining. 5695–5706.
[45] Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo, and
Yongqiang Ma. 2024. LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models. arXiv preprint arXiv:2403.13372 (2024). http://arxiv.org/abs/2403.
13372
[46] Zhilun Zhou, Yuming Lin, Depeng Jin, and Yong Li. 2024. Large Language Model
for Participatory Urban Planning. arXiv preprint arXiv:2402.17161 (2024).
[47] He Zhu, Wenjia Zhang, Nuoxian Huang, Boyang Li, Luyao Niu, Zipei Fan, Tianle
Lun, Yicheng Tao, Junyou Su, Zhaoya Gong, et al. 2024. PlanGPT: Enhancing
Urban Planning with Tailored Language Model and Efficient Retrieval. arXiv
preprint arXiv:2402.19273 (2024).
A Case Study
In real-world urban planning scenarios, human planners spend
much time dealing with textual data. We show two typical cases
about urban planning text polishment and proofreading, to demonstrate the effectiveness of our tool in practical applications.
Urban planning text polishment
#prompt# Assuming that you are a staff member who is good at
writing and proofreading China’s urban and rural planning texts,
could you please polish and proofread the #original text# according
to the #urban and rural planning text requirements#:
#urban and rural planning text requirements# The text
is coherent and complete. Standardized terminology, official and
rigorous content, no colloquial expressions, no English, pinyin,
internet terms, etc. In line with the style of government documents,
the content is full, and there is no concept stacking and repetition
of content. The content is reasonable and accurate, no misleading
expressions, ensure consistency and logic. Coorect in grammar and
spelling.
#original text# It is difficult to find a historical and cultural
district worthy of protection in a famous historical and cultural
city, and the focus now is on restoring the traditional appearance
of the historical city center as a whole.
#response# A famous historical and cultural city currently has
difficulty in finding a historical and cultural neighborhood worthy
of protection. In order to enhance the historical and cultural value
of the city, measures should be taken to enhance the protection of
the existing cultural heritage, to identify and discover historical and

uage Models KDD ’25, August 03–07, 2025, Toronto, ON, Canada
cultural districts that have yet to be protected, and to restore the
traditional appearance of the historical city center as a whole, so as
to preserve and continue the historical and cultural characteristics
of the city.
Urban planning text proofreading
#prompt# Assuming that you are a staff member who is good at
writing and proofreading Chinese town and country planning texts,
please touch up and proofread the #original text# according to the
#urban and rural planning text requirements#.
#urban and rural planning text requirements# The text
is coherent and complete. Standardised terminology, official and
rigorous content, no colloquial expressions, no English, pinyin,
internet terms, etc. In line with the style of government documents,
beautiful language, full of content, without concept stacking and
repetitive content. Whether the content is reasonable and accurate,
whether there are misleading expressions, to ensure consistency
and logic. Pay attention to grammar, spelling and fluency.
#original text# The layout of the city of Athens is a complete
embodiment of the Hippodrome layout pattern, the Miletus is a
layout pattern centred on the city square, with a grid of roads as the
backbone , the square or the marketplace is surrounded by a series
of public buildings, which are the core of urban life, the Acropolis
has a very typical unplanned layout of features
#response# The layout of the Athenian city does not fully reflect
the Hippodrome layout pattern, while the Miletus is a typical layout
pattern centred on the city square, with a grid of roads as the skeleton. A series of public buildings were constructed around the square
or marketplace, which became the core of urban life. In addition,
the Acropolis exhibits a typical unplanned layout characteristic,
reflecting the diversity of history and culture.
(The above contents are translated from Chinese)
B Prompt for data generation
The prompt template of data generation is as follows:
#prompt
#01 You are a Q&A pair dataset processing expert.
#02 Your task is to generate corresponding Q&A pairs based on
my questions and the content I give.
#03 The questions generated must be macro and value based,
don’t generate particularly detailed questions, and not too long.
#04 Answers must be comprehensive, use more of my information and be more informative.
#05 The text is coherent and the content is complete.
#06 Use standardised language, official and rigorous content, no
colloquial expressions, no English, pinyin, internet terms, etc.
#07 Beautiful language, rigorous content, no concepts and repetitive content.
#08 Must be generated according to the following sample format:
"instruction": “question”,
"output": "answer"
#09 The reference case is as follows:
"instruction": "How can town system planning contribute to the
sustainable development of a town system?" ,
"output": "Town system planning to promote the sustainable
development of the town system needs to consider comprehensively

KDD ’25, August 03–07, 2025, Toronto, ON, Canada Zheng et al.
from the aspects of resource utilisation, environmental protection, Generate 20 Q&A pairs, ending with the full JSON formatted
social and economic development." Q&A pair, discarding contexts that do not respond to completion.
(The above contents are translated from Chinese)
