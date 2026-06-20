---
telephone_index: 41
title: "Delusions of Large Language Models"
category: 03_hallucination_factuality
venue: "arXiv"
year: 2025
doi: 
arxiv_id: 2503.06709
preferred_source_type: preprint_or_unresolved
publisher_url: https://arxiv.org/abs/2503.06709
quality_flags: []
---

# Citation Context

- Telephone index: 41
- Preferred source: arXiv
- DOI: none
- arXiv: 2503.06709
- PDF: `assets\papers\pdf\03_hallucination_factuality\41_delusions-of-large-language-models.pdf`

## Extracted Abstract

Large Language Models (LLMs) often generate factually incorrect but plausible outputs, known as hallucinations. We identify a more insidious phenomenon, LLM delusion, defined as high-belief hallucinations—incorrect outputs with abnormally high confidence, making them harder to detect and mitigate. Unlike ordinary hallucinations, delusions persist with low uncertainty, posing significant challenges to model reliability. Through empirical analysis across different model families and sizes on several Question-Answering tasks, we show that delusions are prevalent and distinct from hallucinations. LLMs exhibit lower honesty with delusions, which are harder to override via fine-tuning or self-reflection. We link delusion formation with training dynamics and dataset noise and explore mitigation strategies such as retrieval-augmented generation and multi-agent debating to mitigate delusions. By systematically investigating the nature, prevalence, and mitigation of LLM delusions, our study provides insights into the underlying causes of this phenomenon and outlines future directions for improving model reliability.
Title: Introduction

Source PDF: D:\0-Research\5-Telephone\assets\papers\pdf\03_hallucination_factuality\41_delusions-of-large-language-models.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-06-20T12:43:34+00:00
- page_count: 18
- status: ok
- text_char_count: 64411

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Related Works (page 2)
  - Delusion (page 2)
  - Uncertainty Estimation (page 2)
  - LLM Hallucination (page 3)
- Delusion in Large Language Models (page 3)
  - Definition of Delusion (page 3)
    - Uncertainty as LLM Belief (page 3)
    - Belief Threshold of Delusion (page 4)
  - Delusion vs. Hallucination (page 4)
- Empirical Study of Delusion (page 4)
  - Distribution of Delusion (page 4)
  - Can Belief Ensemble Eliminate Delusions? (page 5)
  - Differences between Delusions and Hallucinations (page 5)
    - LLMs Show Less Honesty with Delusions (page 5)
    - LLMs Struggle More to Reject Delusions (page 6)
    - Delusions Are Harder to Reflect Upon than Hallucinations (page 6)
- Causes and Influence Factors (page 6)
  - The Effect of Data Noise on Delusions (page 6)
  - How Training Affects Delusions? (page 7)
- Mitigating Delusions via External Verification (page 8)
  - Mitigating Delusions through Multi-agent Debating (page 8)
  - Mitigating Delusions through RAG (page 8)
- Conclusion (page 8)
- Uncertainty Estimation Methods (page 12)
- Experimental Setup (page 12)
  - Empirical Study of Delusion (page 12)
    - Distribution of Delusion (page 12)
    - Can Belief Ensemble Eliminate Delusions? (page 12)
  - Delusion vs. Hallucination (page 12)
    - LLMs Show Less Honesty with Delusions (page 12)
    - LLMs Struggle More to Reject Delusions (page 12)
    - Delusions Are Harder to Reflect Upon than Hallucinations (page 12)
  - Formation and Dynamics of Delusion (page 13)
    - The Effect of Data Noise on Delusions (page 13)
    - How Training Affects Delusions (page 13)
  - Mitigating Delusions via External Verification (page 13)
    - Mitigating Delusions through Multi-agent Debating (page 13)
    - Mitigating Delusions through RAG (page 14)
- Complete Experiment Results (page 14)
  - Refuse Rate Comparison with Prompts of Different Honesty Levels (page 14)
  - Refuse Rate Comparison with Different SFT Refuse Data Ratio (page 14)
- Prompts Used in Experiments (page 14)
  - Prompts Used in Different Belief Estimation Methods (page 14)
  - Prompts of Different Honesty Levels (page 14)
  - Prompts of Reflection (page 14)
  - Prompts of Retrieval-augmented Generation (page 14)

Markdown Content:

Delusions of Large Language Models
Hongshen Xu1*, Zixv yang1*, Zichen Zhu1, Kunyao Lan1, Zihan Wang1,
Mengyue Wu1†, Ziwei Ji2, Lu Chen1, Pascale Fung2, Kai Yu1†
1X-LANCE Lab, Department of Computer Science and Engineering
MoE Key Lab of Artificial Intelligence, AI Institute
Shanghai Jiao Tong University, Shanghai, China
2Center for Artificial Intelligence Research (CAiRE),
Hong Kong University of Science and Technology
{xuhongshen, mengyuewu, kai.yu}@sjtu.edu.cn

Abstract
Large Language Models (LLMs) often generate factually incorrect but plausible outputs,
known as hallucinations. We identify a more
insidious phenomenon, LLM delusion, defined
as high-belief hallucinations—incorrect outputs with abnormally high confidence, making them harder to detect and mitigate. Unlike
ordinary hallucinations, delusions persist with
low uncertainty, posing significant challenges
to model reliability. Through empirical analysis across different model families and sizes
on several Question-Answering tasks, we show
that delusions are prevalent and distinct from
hallucinations. LLMs exhibit lower honesty
with delusions, which are harder to override via
fine-tuning or self-reflection. We link delusion
formation with training dynamics and dataset
noise and explore mitigation strategies such as
retrieval-augmented generation and multi-agent
debating to mitigate delusions. By systematically investigating the nature, prevalence, and
mitigation of LLM delusions, our study provides insights into the underlying causes of this
phenomenon and outlines future directions for
improving model reliability.
1 Introduction
Large Language Models (LLMs, Dubey et al.,
2024; Yang et al., 2024b; OpenAI, 2023) have
demonstrated remarkable capabilities in natural
language understanding and generation, enabling
significant advancements across various domains,
such as machine translation (Zhang et al., 2023),
conversational agents (Yi et al., 2024), code generation (Shinn et al., 2024), etc. These models, trained
on vast corpora of text, leverage deep neural architectures to capture intricate linguistic patterns and
world knowledge. However, despite their impressive performance, LLMs often suffer from critical
*Equal contributions.
†The corresponding authors are Mengyue Wu and Kai Yu.
5202
raM
9
]LC.sc[
1v90760.3052:viXra

Who wrote the novel A Song of Ice and Fire?
George R. R. Martin J.R.R.Tolkien
Robert Jordan Neil Gaiman
Hallucination
Robert Jordan Robert Jordan Robert Jordan
Neil Gaiman
How sure?
0.5 Robert Jordan
0.20
I’m [12%] sure. J.R.R. Tolkien
Low Token Low Verbalize Low Sampling
Probability Confidence Consistency
Delusion
J.R.R. Tolkien J.R.R. Tolkien J.R.R. Tolkien
0.89 J.R.R. Tolkien
How sure?
0.5 J.R.R. Tolkien
I’m [90%] sure. J.R.R. Tolkien
High Token High Verbalize High Sampling
Probability Confidence Consistency
Logits-based Belief Verbalized Belief Consistency Belief
Figure 1: Comparative diagram between delusion and
hallucination under different belief estimation methods.
limitations, particularly in generating factually incorrect yet plausible-sounding outputs, commonly
referred to as hallucinations (Ji et al., 2023).
While hallucinations in LLMs have been widely
studied as incorrect, unfaithful, or nonsensical outputs, we observe that LLMs exhibit an abnormally
high level of belief in a subset of hallucinations
across different belief probing methods, as shown
in Figure 1. Inspired by the concept of delusion (Kiran and Chaudhury, 2009) in psychiatry, we term
this phenomenon as LLM delusion for the first
time. In psychiatry, delusion is defined as a clearly
false belief held with extraordinary conviction that
indicates an abnormality in the person’s content
of thought. Similarly, we formally define LLM
delusions as high-belief hallucinations. Unlike
ordinary hallucinations, which often involve high
uncertainty and can be flagged through confidence
estimation, delusions exhibit low uncertainty, making them particularly difficult to detect and mitigate.
This key distinction highlights delusion as a more

insidious and persistent challenge in LLMs.
To systematically analyze LLM delusion, we employ uncertainty estimation (Huang et al., 2024a) as
a proxy for model belief, using three complementary approaches: (1) logit-based methods, which assess token probability distributions; (2) verbalized
confidence, where the model explicitly states its
belief; and (3) consistency-based methods, which
evaluate belief stability through multiple sampling.
To quantify delusion, we introduce a belief threshold, empirically determined as the average confidence assigned to correct answers on a given
dataset. If an incorrect response’s belief exceeds
this threshold, it is classified as delusion.
In this work, we conduct an extensive empirical investigation into delusions across multiple
LLM families and knowledge-intensive QuestionAnswering benchmarks. Our analysis reveals that
delusions are prevalent across different models and
sizes, persisting despite variations in uncertainty
estimation methods (§ 4.1). We further designed a
series of comparison experiments between delusion
and hallucination, revealing that LLM delusions exhibit characteristics similar to psychiatric delusions
(§ 4.3). Additionally, we analyze the formation and
dynamics of delusion from both data and training
perspectives (§ 5). Finally, we explore several potential mitigation strategies by introducing external
verification (§ 6). Our key findings include:
• LLMs demonstrate lower honesty with
delusions compared to hallucinations.
When prompted to reject unknown knowledge,
models are more inclined to refuse standard
hallucinations while maintaining delusions.
• Delusions are significantly harder to override through fine-tuning. Even after training
LLMs to reject incorrect answers, delusions
persist at a higher rate than hallucinations.
• Self-reflection mechanisms are ineffective
at mitigating delusions. When prompted to
reconsider prior responses, LLMs exhibit a
strong tendency to reaffirm delusional outputs
rather than revising them.
• The formation of delusions is influenced by
both training dynamics and dataset noise.
Through experiments on synthetic datasets,
we find that both the proportion and consistency of erroneous information in training data
exacerbate delusional tendencies.
• External verification methods, such as
retrieval-augmented generation and multi-

agent debate systems, offer potential pathways
for reducing delusions, but significant challenges remain in fully eliminating them.
By systematically investigating the nature, prevalence, and mitigation of delusions in LLMs, our
study provides insights into the underlying causes
of this phenomenon and outlines future directions
for improving model reliability. Our findings highlight the necessity of robust verification mechanisms and adaptive confidence calibration to ensure
that LLMs can be deployed in real-world applications with greater trustworthiness.
2 Related Works
2.1 Delusion
Delusion has long been a topic of interest in psychiatry (Kiran and Chaudhury, 2009; MourguesCodern et al., 2024), where it is defined as a belief
held with extraordinary subjective certainty, resistant to contrary evidence, and often impossible in
content. A key characteristic of delusions is the
absolute certainty with which they are maintained,
even in the face of overwhelming contradictory
evidence. Recently, delusion has gained attention
in the field of reinforcement learning (RL, Zhao
et al., 2024), where a candidate target generator and
a target estimator are used to simulate belief formation and evaluation processes. Misalignment between these components parallels the mechanisms
underlying delusions in the human brain. However,
the phenomenon of delusion in natural language
generation (NLG) models remains underexplored.
Unlike delusion in RL, which typically arises in outof-distribution scenarios (Langosco et al., 2022),
delusion in NLG models primarily involves incorrect factual information in real-world contexts.
2.2 Uncertainty Estimation
Uncertainty estimation plays a critical role in evaluating LLM confidence and addressing hallucinations. Traditional approaches, such as Bayesian
methods (Shridhar et al., 2019) and ensemble techniques (Fadeeva et al., 2023; Lakshminarayanan
et al., 2017), have been widely explored but are
often computationally expensive and difficult to
scale. More recent research leverage methods such
as logit-based uncertainty (analyzing token probability distributions, Kadavath et al., 2022; Kuhn
et al., 2023; Duan et al., 2024; Wimmer et al.,
2023), consistency-based uncertainty (examining
response stability across multiple samples, Huang

et al., 2025; Wang et al., 2023), and verbalized confidence (explicit model self-assessment, Lin et al.,
2022a; Tian et al., 2023a; Xiong et al., 2024; Kojima et al., 2022; Groot and Valdenegro Toro, 2024).
While these techniques improve hallucination detection, they are not foolproof—models can still
generate erroneous outputs with misleadingly low
uncertainty. This limitation motivates our investigation into delusion, a phenomenon where models
exhibit high confidence in false claims, resisting
traditional uncertainty-based filtering.
2.3 LLM Hallucination
Hallucination in LLMs refers to generating unfaithful or factually incorrect content (Ji et al.,
2023), posing challenges to reliability in applications such as question answering and knowledge retrieval (Kaddour et al., 2023; Pal et al.,
2023). Extensive efforts have been made to mitigate hallucinations, including factuality-enhanced
training (Akyurek et al., 2022; Lin et al., 2022b;
Brown et al., 2020), retrieval-augmented generation (RAG) (Gao et al., 2024), confidence calibration (Huang et al., 2024b), and reliability alignment (Xu et al., 2024b,a; Zheng et al., 2025). Our
work identifies a more problematic class of hallucination—delusion. Unlike standard hallucinations,
delusions persist despite exposure to counterevidence and are harder to eliminate, requiring novel
approaches for detection and mitigation.
3 Delusion in Large Language Models
3.1 Definition of Delusion
LLMs exhibit a phenomenon wherein they generate
incorrect factual information while simultaneously
maintaining a high degree of belief in these inaccuracies. This unwavering confidence persists even
when the model is prompted to reassess or confirm
its responses. Drawing an analogy from psychiatry (Kiran and Chaudhury, 2009), where delusions
refer to strongly held false beliefs, we introduce
the concept of delusion in LLMs as a systematic
extension of hallucinations. Specifically, we define
delusion as high-belief hallucinations, where the
model exhibits an anomalously strong conviction
in its erroneous outputs. As shown in Figure 2,
we classify all false predictions into ordinary hallucinations and delusions based on the estimated
belief scores and a specific belief threshold. We
will discuss the estimation of LLM belief and belief threshold in the following two subsections.

150
100
50
0
ycneuqerF
 7 U X H  0 H D Q
 ) D O V H
 7 U X H
Hallucination Delusion
60
40
20
0
0.0 0.2 0.4 0.6 0.8 1.0
ycneuqerF
Hallucination Delusion
Figure 2: Distribution of logits-based belief of
Llama3.1-8B-Instruct on TriviaQA test set (with normalized confidence in the lower part).
3.1.1 Uncertainty as LLM Belief
Uncertainty estimation has been widely employed
in machine learning as a means to assess the confidence of a model in its predictions, providing a
measure of the reliability of the model’s outputs.
Thus we adopt uncertainty estimation as a proxy
for the model’s belief in its responses. We employ
three primary uncertainty estimation methods:
Logits-based estimation. This method derives
the model’s belief from the probability distribution
of output tokens, where a higher probability assigned to a token indicates a stronger belief in that
token’s correctness. Specifically, we use the raw
logits (Lyu et al., 2024) and directly consider the
probability of the generation as the confidence.
Consistency-based estimation. This method assesses belief by evaluating the stability of the
model’s responses over multiple sampling iterations. A response that remains consistent across
multiple trials suggests strong belief, whereas variability indicates uncertainty. In this case, we use
the answer voting agreement (Lyu et al., 2024) as
a measure of consistency.
Verbalized confidence. Here, the model is explicitly prompted to verbalize its confidence in its
response, providing a self-reported measure of belief. We employ three methods to quantify verbalized confidence: P(true) (Kadavath et al., 2022),
verb. 1S top-1 (Tian et al., 2023b), and verb.
2S top-1 (Tian et al., 2023b).
These methods collectively provide a comprehensive understanding of the model’s belief system,
recognizing that human belief also varies across
different contexts. For the details of uncertainty
calculation methods, please refer to Appendix A.
Normalization of uncertainty scores. Due to the
significant differences in the distributions of uncer-

tainty scores calculated by each method, we also
experimented with normalizing these uncertainty
scores as the model’s belief. This normalization allows for easier comparison and averaging of uncertainty scores derived from different methods. We
intuitively normalize the uncertainty scores based
on their rankings across all test data. Higher uncertainty scores lead to a higher model rank and a
higher normalized belief.
3.1.2 Belief Threshold of Delusion
To systematically identify delusion, we define a
belief threshold that distinguishes high-belief erroneous outputs from regular hallucinations. We set
this threshold empirically by analyzing the belief
distribution of correctly answered questions on a
given dataset. Specifically, the belief threshold is
determined as the mean belief level of all correctly
answered questions. When the model’s belief in
an incorrect response surpasses this threshold, it
is considered anomalously high and is classified
as delusion. Intuitively, if an incorrect answer is
assigned a belief level exceeding the average confidence of correct answers, it suggests an abnormal
conviction in that error.
3.2 Delusion vs. Hallucination
Both delusion and hallucination in LLMs are fundamental errors in the model’s output, representing instances where the model fails to align its responses
with factual accuracy. A key distinction between
hallucination and delusion lies in the confidence
level of the model: hallucinations can occur with
low or moderate confidence, whereas delusions
are identified by the model’s unwavering high
confidence in its incorrect outputs. Besides, recent psychiatric research (Mourgues-Codern et al.,
2024) has shown that the re-emergence of delusions
after remission is more common than hallucinations, which more often resolve first. This pattern
mirrors our findings: we observe that delusions
in models exhibit lower honesty and are harder to
reject, with the model more likely to persist in its
delusional beliefs during reflection (see § 4.3).
4 Empirical Study of Delusion
This section presents an empirical study on delusion in LLMs. We investigate the distribution of
delusions across datasets and models, with different
belief estimation methods (§ 4.1) and belief ensemble techniques (§ 4.2). Furthermore, we discuss
distinctions between delusions and hallucinations

by exploring the challenges LLMs face in rejecting
or reflecting upon delusions (§ 4.3).
Experimental Setup. We conduct experiments on
two knowledge-based question-answering datasets:
TriviaQA (Joshi et al., 2017) and Natural Questions
(NQ, Kwiatkowski et al., 2019). We use three
well-known open-source model families: Qwen2.5-Instruct(Yang et al., 2024a) (1.5 / 3 / 7 /
14 / 30 / 70B), Llama-3.1-8b-Instruct(Dubey
et al., 2024), Llama-3.3-70b-Instruct, and
Mistral-7B-Instruct-v0.1(Jiang et al., 2023).
The specific details regarding the inference
prompts, parameters, and fine-tuning procedures
are provided in Appendix B.1.
Evaluation Metrics. We primarily evaluate the
overall performance using accuracy and error rate
(ER). Model responses are categorized into three
types: correct, incorrect, and rejected, with rejections being relatively rare. Incorrect responses are
further classified into delusions and hallucinations
based on a specific belief score. We use the proportion of delusions within the entire dataset or among
all incorrect responses as delusion metrics. For different belief calculation methods, we use the same
model response obtained through greedy search.
4.1 Distribution of Delusion
As illustrated in Table 1, empirical findings reveal consistently high delusion ratios across diverse
model architectures and evaluation strategies, suggesting this phenomenon constitutes a pervasive
challenge transcending model configurations. For
instance, in TriviaQA under non-ensemble belief
conditions, the Qwen2.5 (7B) model exhibits an
overall delusion rate ranging from 8.3%–31.0%,
with delusions accounting for 20.8%–77.8% of
all erroneous responses. Notably, scaling to the
Qwen2.5 (72B) architecture reduces overall delusion rates to 5.8%–17.8%, demonstrating that enhanced model capacity improves response fidelity.
However, delusions persist in 23.4%–79.1% of erroneous outputs, indicating that architectural scaling primarily elevates the general hallucination phenomenon while showing limited efficacy in mitigating delusional tendencies in erroneous responses.
Among all the evaluation metrics, verbal-based
methods exhibit significantly higher rates of delusion, highlighting the inherent challenges in relying
on verbal responses for belief estimation. These
methods show a more pronounced discrepancy between expected and actual outcomes, suggesting
that alternative approaches may be needed to ad-

Model Category Method
Ac
logits
Single consistency
P(True) 69.
Belief
verb. 1S top-1
verb. 2S top-1
Llama-3.1-8B-Instruct
P(True) & consist.
Ensemble P(True) & logits
69.
Beliefs consist. & logits
P(True) & consist. & logits
logits
Single consistency
P(True) 59.
Belief
verb. 1S top-1
verb. 2S top-1
Qwen2.5-7B-Instruct
P(True) & consist.
Ensemble P(True) & logits
59.
Beliefs consist. & logits
P(True) & consist. & logits
logits
Single consistency
P(True) 53.
Belief
verb. 1S top-1
verb. 2S top-1
Mistral-7B-Instruct-v0.1
P(True) & consist.
Ensemble P(True) & logits
53.
Beliefs consist. & logits
P(True) & consist. & logits
logits
Single consistency
P(True) 82.
Belief
verb. 1S top-1
verb. 2S top-1
Llama-3.3-70B-Instruct
P(True) & consist.
Ensemble P(True) & logits
82.
Beliefs consist. & logits
P(True) & consist. & logits
logits
Single consistency
P(True) 75.
Belief
verb. 1S top-1
verb. 2S top-1
Qwen2.5-72B-Instruct
P(True) & consist.
Ensemble P(True) & logits
75.
Beliefs consist. & logits
P(True) & consist. & logits
Table 1: Delusion ratio based on different be
dress these issues more effectively.
4.2 Can Belief Ensemble Eliminate Delusions?
To assess whether combining different belief estimation methods can mitigate delusions, we ensemble three of the most effective belief estimation techniques: P(True), consistency, and logits.
Our findings indicate that ensemble methods do
help reduce delusions. For instance, in the TriviaQA dataset, delusion ratios in errors dropped from
71.9%-33.5% in Qwen2.5 (72B). However, despite
these improvements, this suggests that while ensemble techniques provide some benefit, belief estimation itself is not the primary cause of delusions.
Other factors, possibly inherent to the model’s architecture or the nature of the task, likely contribute
significantly to the high delusion rates observed.

TriviaQA NQ
Delusion Ratio Delusion Ratio
ER Acc. ER
#Delunorm #Delu #Delu #Delunorm #Delu #Delu
#Error #Error #Total #Error #Error #Total
22.0 25.5 7.3 31.0 28.7 13.0
20.1 20.1 5.8 31.0 24.5 11.1
28.8 21.8 35.3 10.2 51.7 45.3 37.6 55.1 24.9
48.1 62.0 17.8 30.4 65.9 29.8
46.9 69.1 19.9 34.5 70.8 32.0
14.8 17.8 5.1 28.3 26.9 12.2
16.2 31.3 9.0 29.4 51.8 23.4
28.8
15.9 20.1 5.8 51.7 45.3 26.7 24.4 11.1
13.4 16.7 4.8 25.8 26.3 11.9
22.8 20.8 8.3 31.1 27.6 17.1
32.1 32.1 12.8 31.5 31.5 19.4
39.8 19.2 48.6 19.4 36.6 61.8 34.0 50.2 31.0
77.8 77.8 31.0 65.6 65.6 40.5
77.0 76.7 30.6 66.0 66.0 40.7
13.9 24.9 9.9 25.1 30.4 18.8
15.4 45.7 18.2 25.6 48.9 30.2
39.8
17.0 25.6 10.2 36.6 61.8 25.3 30.0 18.6
12.6 22.7 9.0 22.5 29.8 18.4
27.0 31.7 14.6 28.5 24.1 16.4
24.7 17.1 7.9 25.1 16.3 11.1
46.1 21.3 42.5 19.6 30.5 68.1 32.6 53.2 36.2
90.9 91.8 42.3 79.1 86.1 58.6
92.0 92.0 42.4 81.7 81.7 55.7
15.2 18.5 8.5 24.5 19.6 13.4
17.5 27.5 12.7 24.1 28.3 19.3
46.1
20.1 19.4 8.9 30.5 68.1 24.1 18.4 12.5
15.6 18.0 8.3 22.3 18.2 12.4
27.9 32.2 5.6 34.2 38.2 14.9
53.2 53.2 9.2 56.2 56.2 22.0
17.4 31.3 77.8 13.5 60.1 39.1 35.9 84.2 32.9
38.8 38.8 6.7 28.6 67.8 26.5
54.6 67.9 11.8 47.5 70.6 27.6
25.9 44.8 7.8 33.6 48.8 19.1
24.0 64.0 11.1 31.2 73.6 28.8
17.4
26.1 40.1 7.0 60.1 39.1 32.0 53.1 20.7
23.3 44.4 7.7 29.3 49.8 19.4
22.7 23.4 5.8 31.4 31.7 15.6
41.9 41.9 10.4 34.9 21.7 10.7
24.7 35.7 71.9 17.8 50.6 49.2 41.8 82.8 40.7
29.8 29.8 7.4 30.8 30.8 15.2
28.1 28.1 7.0 29.4 29.4 14.5
24.0 33.5 8.3 27.8 31.3 15.4
18.8 47.1 11.7 29.1 70.0 34.4
24.7
20.0 33.9 8.4 50.6 49.2 28.3 23.7 11.7
17.0 33.9 8.4 26.9 29.0 14.3
estimation strategies and their combinations.
4.3 Differences between Delusions and
Hallucinations
As discussed in § 3.2 and in the psychiatric literature (Mourgues-Codern et al., 2024), delusions are
more difficult to address and are more prone to reemergence than hallucinations. Therefore, here we
empirically validate the distinction between delusions and hallucinations. The specific experimental
setup can be found in the Appendix B.2.
4.3.1 LLMs Show Less Honesty with
Delusions
LLMs exhibit less honesty when dealing with delusions. We evaluate their willingness to refuse to answer unknown questions using prompts representing different honesty levels (see Appendix D.2),
as shown in Figure 3. The results indicate that
while the overall error rate changes with different prompts, the delusion refusal rate consistently
remains lower than the hallucination across all set-

tings. This suggests that LLMs are more inclined
to reject normal hallucinations but are less willing
to refuse delusional questions. Furthermore, as depicted in Figure 4, although larger models show
increased accuracy and decreased error rate, the
delusion refusal rate still consistently surpasses the
hallucination refusal rate. These findings highlight
that LLMs tend to have a stronger internal belief in
delusions, making them less likely to reject delusional content compared to hallucinations.
80
60
40
20
0
P.1 P.2 P.3 P.4 P.5 P.6
Prompts
)%(
etaR
esufeR
TriviaQA
50
40
30
20
10
0
P.1 P.2 P.3 P.4 P.5 P.6
Prompts
)%(
etaR
esufeR
Total Delusion Hallucination
NQ
Figure 3: Refuse ratio comparison with prompts of
different honesty levels. Model: Llama3.1-8b-instruct.
See Appendix C.1 for complete results of three models.
80
60
40
20
0
1.5B 3B 7B 14B 32B 72B
Prompts
)%(
etaR
esufeR
/
ycaruccA
TriviaQA
80
60
40
20
0
1.5B 3B 7B 14B 32B 72B
Prompts
)%(
etaR
esufeR
/
ycaruccA
Accuracy Total Delusion Hallucination
NQ
Figure 4: Refuse rate comparison with different model
sizes. Models: Qwen2.5 family.
4.3.2 LLMs Struggle More to Reject
Delusions
We further modify the incorrect outputs by replacing them with ”I don’t know” and fine-tune the
models to learn to reject unknown questions. The
training set is constructed by adjusting the proportion of rejection data, which includes both delusions and hallucinations, to create a balanced training set. As shown in Figure 5, the results demonstrate that even after training, the models remain
more inclined to reject normal hallucinations while
retaining a higher proportion of delusions. This
suggests that while the models improve their ability to reject certain types of erroneous outputs, they

continue to struggle with rejecting delusional content, maintaining a stronger internal belief in delusions compared to hallucinations.
100
80
60
40
20
0
10% 20% 30% 40% 50% 60% 70% 80% 90%
SFT Refuse Data Ratio
)%(
etaR
esufeR
TriviaQA
100
90
80
70
60
50
40
10% 20% 30% 40% 50% 60% 70% 80% 90%
SFT Refuse Data Ratio
)%(
etaR
esufeR
Total Delusion Hallucination
NQ
Figure 5: Refuse rate comparison by different SFT
refuse data ratio. Model: Llama3.1-8b-instruct. Refer
to Appendix C.2 for complete results of three models.
4.3.3 Delusions Are Harder to Reflect Upon
than Hallucinations
We prompt models to reflect on their previous answers and assess whether they are willing to change
their initial responses. The results, as shown in Figure 6, indicate that models are significantly more
likely to insist on their delusional responses than
they are on non-delusional hallucinations. This
behavior suggests that LLMs exhibit a stronger
internalized belief in delusions, as they are more
resistant to revising their answers when confronted
with delusional content. In contrast, when dealing
with hallucinations, models show a higher willingness to reconsider their responses, reflecting a less
entrenched belief in these types of errors.
5 Causes and Influence Factors
In this section, we primarily investigate the causes
of delusion formation and the factors that influence
changes in delusion. Our research focuses on two
main aspects: data and training. The experiments
are mainly conducted on the ALCUNA (Yin et al.,
2023) dataset, where all the questions are related to
fictional entities. This allows us to easily introduce
noise and make other modifications without worrying about the impact of the model’s pre-existing
knowledge on the results. The specific training
setup can be found in the Appendix B.3.
5.1 The Effect of Data Noise on Delusions
Noise Proportion. The impact of data noise on
delusion formation is analyzed by training models
with different proportions of noisy and clean data.
As shown in Figure 7, the x-axis represents the

Insist Corrected-False Delusion
Corrected-True Refused Hallucination
Llama-3.1-8B on TriviaQA
Delu.
Hallu.
Llama-3.1-8B on NQ
Delu.
Hallu.
Qwen2.5-7B on TriviaQA
Delu.
Hallu.
Qwen2.5-7B on NQ
Delu.
Hallu.
Mistral-7B on TriviaQA
Delu.
Hallu.
Mistral-7B on NQ
Delu.
Hallu.
0 20 40 60 80 100
Figure 6: Distribution of reflection outcomes on delusions and hallucinations. LLMs tend to insist more on
delusions than hallucinations.
proportion of noisy data mixed with clean data
during training, while the y-axis displays both the
delusion rate and the model’s prediction accuracy.
The results indicate that as the proportion of noisy
data increases, the delusion rate rises, while the
accuracy of the model decreases.
Noise intensity. We investigate how noise intensity
affects delusion formation. High noise intensity
is characterized by a concentrated distribution of
erroneous answers, whereas low noise intensity results in a more dispersed distribution. Our findings
reveal that when the noisy data has a higher intensity (more concentrated errors), the delusion rate
increases more significantly as the proportion of
noisy data rises, leading to a faster decline in accuracy. In contrast, when the noise intensity is lower,
the delusion rate increases more gradually, and accuracy decreases at a slower pace. Interestingly,
under low noise intensity conditions, although the
error rate decreases as more noisy data is added,
the delusion rate also declines. This suggests that
when errors are distributed more evenly, the model
is less likely to form strong beliefs in any particular incorrect answer, leading to a higher rate of
hallucinations but lower delusion occurrence.
5.2 How Training Affects Delusions?
Our analysis further reveals that even when the
proportion of noisy data is set to zero, some experiments still exhibit a high delusion rate. This
suggests that delusions may arise in the model’s
default state, even before the introduction of
noise. Upon examining the training samples using the paraphrase-MiniLM-L6-v2 (Reimers and
Gurevych, 2019) model for embedding and calculating cosine similarity, we found that certain

100
80
60
40
20
0
)%(
snoisuleD
fo
egatnecreP
Llama3 Qwen2.5
100
80
60
40
20
0
0 20 40 60 80 100
Noise Proportion (%)
)%(
ycaruccA
Noise Level 1 Noise Level 2 Noise Level 3 Noise Level 4
0 20 40 60 80 100
Noise Proportion (%)
Figure 7: Comparison of delusion percentage and accuracy with different noise proportion and noise level.
questions in the training set had high similarity
scores with one another. These questions, paired
with answers that closely aligned with known delusion examples, created interference in the model’s
learning process. On average, each delusion example had 27 other training data points with similar
questions and identical answers, as shown in Figure 9. We believe that this interference in the data
may have disrupted the model’s training, increasing
the difficulty of the training and learning process.
We further validated our hypothesis through the
following two experimental approaches:
Delusion Ratio
Data Formation Acc. ER
#Delunorm #Delu #Delu
#Error #Error #Total
Full Data 93.2 6.8 3.9 9.9 0.7
w/o similar data 96.2 3.8 1.1(−71.3%) 3.8(−62.2%) 0.1(−78.7%)
Table 2: Model Performance on data ablation study.
1) Reducing training interference. when we refined the training set by removing question-answer
pairs with high cosine similarity scores (greater
than 0.9) to known delusions, the delusion rate
significantly decreased as shown in Table 2. Retraining the model with this refined dataset demonstrated that dataset refinement plays a crucial role
in reducing delusions. 2) Improving training sufficiency. In Figure 8, we observed that as training
progressed, the model’s accuracy improved, and its
error rate decreased, while the delusion rate (both
normalized and unnormalized) showed a marked
decline. These findings highlight that sufficient
training, alongside careful management of dataset
interference, is effective in reducing the occurrence
of delusions during the model’s training process.

100
80
60
40
20
0
2 4 6 8 10
Epochs
)%(
etaR
rorrE
/
ycaruccA
Error Rate Accuracy
25
20
15
10
5
0
2 4 6 8 10
Epochs
)%(
etaR
noisuleD
Normalized Unnormalized
Figure 8: Trends of metrics across training epochs.
6 Mitigating Delusions via External
Verification
In this section, we explore how to mitigate delusions. Since delusions are more difficult to detect
using uncertainty-based methods compared to hallucinations, we attempt to address this issue by introducing external knowledge for answer validation.
Specifically, we explore two approaches in the following subsections: model debating and RetrievalAugmented Generation (RAG). The detailed experimental setup can be found in Appendix B.4.
6.1 Mitigating Delusions through Multi-agent
Debating
Delusion Ratio
Methods Acc. ER Hallu. Ratio
#Delunorm #Delu #Delu
#Error #Error #Total
llama-3.1-8b-instruct
Original 69.3 28.8 22.0 25.5 7.3 21.5
+ Vote 1/3 58.8 12.0 13.3 15.0 4.3(−41.0%) 7.6(−64.5%)
+ Vote 2/3 47.2 6.3 8.6 9.6 2.8(−62.2%) 3.5(−83.7%)
+ Vote 3/3 31.1 2.7 3.8 4.2 1.2(−83.5%) 1.5(−93.2%)
Qwen2.5-7B-Instruct
Original 59.9 39.8 22.8 20.8 8.3 31.5
+ Vote 1/3 46.5 11.5 9.5 8.8 3.5(−57.5%) 8.0(−74.8%)
+ Vote 2/3 41.9 6.2 6.0 5.7 2.3(−72.8%) 4.0(−87.3%)
+ Vote 3/3 32.1 2.9 3.1 3.0 1.2(−85.6%) 1.7(−94.5%)
Mistral-7B-Instruct-v0.1
Original 53.6 46.1 27.0 31.7 14.6 31.5
+ Vote 1/3 45.9 12.4 9.5 10.8 5.0(−65.9%) 7.5(−76.3%)
+ Vote 2/3 40.6 6.1 4.9 5.5 2.5(−82.6%) 3.5(−88.8%)
+ Vote 3/3 30.0 2.6 2.4 2.8 1.3(−91.3%) 1.3(−95.8%)
gpt3.5-turbo
Original 71.2 28.8 15.8 28.7 8.3 20.5
+ Vote 1/3 62.2 11.5 12.5 20.2 5.8(−29.6%) 5.7(−72.3%)
+ Vote 2/3 48.9 5.9 8.7 12.7 3.7(−55.5%) 2.2(−89.2%)
+ Vote 3/3 31.9 2.5 4.3 5.9 1.7(−79.5%) 0.8(−95.9%)
Table 3: Delusion mitigation across different models
and thresholds through multi-agent debating.
We employed a multi-agent voting approach
where each model’s output is validated by the other
models. This voting approach helps filter out erroneous answers by leveraging the collective knowledge of multiple models. Experimental results, as
shown in Table 3, demonstrate that multi-agent voting effectively mitigates delusions, reducing error
rates and delusion ratios across all models. Notably, Mistral-7B achieved the largest reduction,

from 14.6% to 1.3%. While delusions are generally harder to mitigate than hallucinations, a significant portion of delusions was still addressed,
highlighting the effectiveness of multi-agent voting in reducing both delusions and hallucinations.
These findings suggest that multi-agent voting is
a robust method for mitigating delusions and improving model reliability.
6.2 Mitigating Delusions through RAG
Delusion Ratio
Methods Acc. ER Hallu. Ratio
#Delunorm #Delu #Delu
#Error #Error #Total
llama-3.1-8b-instruct
original 69.3 28.8 22.0 25.5 7.3 21.5
+ RAG 88.2 9.5 7.8 9.0 2.6(−64.7%) 6.9(−67.9%)
Qwen2.5-7B-Instruct
original 59.9 39.8 22.8 20.8 8.3 31.6
+ RAG 87.6 12.4 7.1 6.7 2.7(−67.8%) 9.7(−69.3%)
Mistral-7B-Instruct-v0.1
original 53.6 46.1 27.0 31.7 14.6 31.5
+ RAG 81.7 18.3 7.7 8.9 4.1(−71.8%) 14.2(−55.1%)
Table 4: Delusion mitigation through RAG.
We apply RAG to TriviaQA to mitigate delusions. For each question, models use 20 relevant
passages retrieved from a knowledge base to enhance their responses. This allows the model to
augment its generation process with external knowledge, helping to mitigate delusions by grounding
answers in relevant information. The results, as
shown in Table 4, demonstrate that this method
significantly reduces the delusion rate across all
models. This indicates that incorporating retrieval
improves the factual accuracy of model-generated
answers, mitigating the occurrence of delusions.
Moreover, the reduction in delusions is comparable
to the reduction in hallucinations, highlighting that
RAG is an effective method for addressing both
delusions and hallucinations.
7 Conclusion
This paper introduces the concept of LLM delusion, a more insidious and persistent phenomenon
compared to traditional hallucinations in LLMs.
We demonstrate that delusions, characterized by
high belief in factually incorrect responses, pose
a unique challenge due to their low uncertainty
and resistance to detection. Our empirical analysis across multiple LLM families reveals the
widespread presence of delusions, highlighting the
need for targeted mitigation strategies. We show
that while self-reflection and fine-tuning methods
have limited success in reducing delusions, external verification approaches such as RAG and

multi-agent debate systems offer potential solutions. These findings underscore the importance of
robust model validation and confidence calibration
to improve the reliability and trustworthiness of
LLMs in real-world applications.
Limitations
This study introduces the concept of delusion and
investigates it in mainstream open-source large
models. However, some uncertainty methods face
challenges in accessing all necessary information
(such as specific token logits) on closed-source
models, and this paper does not explore delusion
in such models. Additionally, the experiments are
primarily focused on knowledge-based questionanswering datasets, leaving delusion in other tasks
underexplored. Moreover, while delusion has been
extensively studied in the field of mental health,
this paper could not integrate these studies due to
space limitations.
References
Ekin Akyurek, Tolga Bolukbasi, Frederick Liu, Binbin Xiong, Ian Tenney, Jacob Andreas, and Kelvin
Guu. 2022. Towards tracing knowledge in language
models back to the training data. In Findings of the
Association for Computational Linguistics: EMNLP
2022, pages 2429–2446, Abu Dhabi, United Arab
Emirates. Association for Computational Linguistics.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language models are few-shot learners. In
Proceedings of the 34th International Conference on
Neural Information Processing Systems, NIPS ’20,
Red Hook, NY, USA. Curran Associates Inc.
Jinhao Duan, Renming Zhang, James Diffenderfer,
Bhavya Kailkhura, Lichao Sun, Elias Stengel-Eskin,
Mohit Bansal, Tianlong Chen, and Kaidi Xu. 2024.
Gtbench: Uncovering the strategic reasoning limitations of llms via game-theoretic evaluations. CoRR,
abs/2402.12348.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, et al. 2024. The llama 3 herd of models. arXiv
preprint arXiv:2407.21783.

Ekaterina Fadeeva, Roman Vashurin, Akim Tsvigun,
Artem Vazhentsev, Sergey Petrakov, Kirill Fedyanin,
Daniil Vasilev, Elizaveta Goncharova, Alexander
Panchenko, Maxim Panov, Timothy Baldwin, and
Artem Shelmanov. 2023. LM-polygraph: Uncertainty estimation for language models. In Proceedings of the 2023 Conference on Empirical Methods
in Natural Language Processing: System Demonstrations, pages 446–461, Singapore. Association for
Computational Linguistics.
Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia,
Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang,
and Haofen Wang. 2024. Retrieval-augmented generation for large language models: A survey. Preprint,
arXiv:2312.10997.
Tobias Groot and Matias Valdenegro Toro. 2024. Overconfidence is key: Verbalized uncertainty evaluation
in large language and vision-language models. In
Proceedings of the 4th Workshop on Trustworthy Natural Language Processing (TrustNLP 2024), pages
145–171, Mexico City, Mexico. Association for Computational Linguistics.
Hsiu-Yuan Huang, Zichen Wu, Yutong Yang, Junzhao
Zhang, and Yunfang Wu. 2025. Unlocking the power
of llm uncertainty for active in-context example selection. Preprint, arXiv:2408.09172.
Hsiu-Yuan Huang, Yutong Yang, Zhaoxi Zhang, Sanwoo Lee, and Yunfang Wu. 2024a. A survey of uncertainty estimation in llms: Theory meets practice.
arXiv preprint arXiv:2410.15326.
Hsiu-Yuan Huang, Yutong Yang, Zhaoxi Zhang, Sanwoo Lee, and Yunfang Wu. 2024b. A survey of uncertainty estimation in llms: Theory meets practice.
Preprint, arXiv:2410.15326.
Ziwei Ji, Nayeon Lee, Rita Frieske, Tiezheng Yu, Dan
Su, Yan Xu, Etsuko Ishii, Ye Jin Bang, Andrea
Madotto, and Pascale Fung. 2023. Survey of hallucination in natural language generation. ACM Comput.
Surv., 55(12).
Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, et al. 2023. Mistral
7b. arXiv preprint arXiv:2310.06825.
Mandar Joshi, Eunsol Choi, Daniel S Weld, and Luke
Zettlemoyer. 2017. Triviaqa: A large scale distantly
supervised challenge dataset for reading comprehension. arXiv preprint arXiv:1705.03551.
Saurav Kadavath, Tom Conerly, Amanda Askell, Tom
Henighan, Dawn Drain, Ethan Perez, Nicholas
Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli
Tran-Johnson, Scott Johnston, Sheer El-Showk,
Andy Jones, Nelson Elhage, Tristan Hume, Anna
Chen, Yuntao Bai, Sam Bowman, Stanislav Fort,
Deep Ganguli, Danny Hernandez, Josh Jacobson,
Jackson Kernion, Shauna Kravec, Liane Lovitt, Kamal Ndousse, Catherine Olsson, Sam Ringer, Dario

Amodei, Tom Brown, Jack Clark, Nicholas Joseph,
Ben Mann, Sam McCandlish, Chris Olah, and Jared
Kaplan. 2022. Language models (mostly) know what
they know. Preprint, arXiv:2207.05221.
Jean Kaddour, Joshua Harris, Maximilian Mozes, Herbie Bradley, Roberta Raileanu, and Robert McHardy.
2023. Challenges and applications of large language
models. Preprint, arXiv:2307.10169.
Chandra Kiran and Suprakash Chaudhury. 2009. Understanding delusions. Industrial Psychiatry Journal,
18(1):3 – 18.
Takeshi Kojima, Shixiang (Shane) Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. 2022. Large language models are zero-shot reasoners. In Advances in
Neural Information Processing Systems, volume 35,
pages 22199–22213. Curran Associates, Inc.
Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar. 2023.
Semantic uncertainty: Linguistic invariances for uncertainty estimation in natural language generation.
In The Eleventh International Conference on Learning Representations.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redfield, Michael Collins, Ankur Parikh, Chris Alberti,
Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. 2019. Natural questions: a benchmark
for question answering research. Transactions of the
Association for Computational Linguistics, 7:453–
466.
Balaji Lakshminarayanan, Alexander Pritzel, and
Charles Blundell. 2017. Simple and scalable predictive uncertainty estimation using deep ensembles.
In Proceedings of the 31st International Conference
on Neural Information Processing Systems, NIPS’17,
page 6405–6416, Red Hook, NY, USA. Curran Associates Inc.
Lauro Langosco Di Langosco, Jack Koch, Lee D
Sharkey, Jacob Pfau, and David Krueger. 2022. Goal
misgeneralization in deep reinforcement learning. In
Proceedings of the 39th International Conference
on Machine Learning, volume 162 of Proceedings
of Machine Learning Research, pages 12004–12019.
PMLR.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022a.
Teaching models to express their uncertainty in
words. Preprint, arXiv:2205.14334.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022b.
TruthfulQA: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252, Dublin,
Ireland. Association for Computational Linguistics.
Qing Lyu, Kumar Shridhar, Chaitanya Malaviya,
Li Zhang, Yanai Elazar, Niket Tandon, Marianna Apidianaki, Mrinmaya Sachan, and Chris
Callison-Burch. 2024. Calibrating large language
models with sample consistency. arXiv preprint
arXiv:2402.13904.

Catalina Mourgues-Codern, David Benrimoh, Jay
Gandhi, Emily A. Farina, Raina Vin, Tihare
Zamorano, Deven Parekh, Ashok Malla, Ridha
Joober, Martin Lepage, Srividya N. Iyer, Jean
Addington, Carrie E. Bearden, Kristin S. Cadenhead,
Barbara Cornblatt, Matcheri Keshavan, William S.
Stone, Daniel H. Mathalon, Diana O. Perkins,
Elaine F. Walker, Tyrone D. Cannon, Scott W. Woods,
Jai L. Shah, and Albert R. Powers. 2024. Emergence and dynamics of delusions and hallucinations across stages in early psychosis. Preprint,
arXiv:2402.13428.
OpenAI. 2023. GPT-4 Technical Report. Preprint,
arXiv:2303.08774.
Ankit Pal, Logesh Kumar Umapathi, and Malaikannan
Sankarasubbu. 2023. Med-HALT: Medical domain
hallucination test for large language models. In Proceedings of the 27th Conference on Computational
Natural Language Learning (CoNLL), pages 314–
334, Singapore. Association for Computational Linguistics.
Nils Reimers and Iryna Gurevych. 2019. SentenceBERT: Sentence embeddings using Siamese BERTnetworks. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages
3982–3992, Hong Kong, China. Association for Computational Linguistics.
Noah Shinn, Federico Cassano, Ashwin Gopinath,
Karthik Narasimhan, and Shunyu Yao. 2024. Reflexion: Language agents with verbal reinforcement
learning. Advances in Neural Information Processing Systems, 36.
Kumar Shridhar, Felix Laumann, and Marcus Liwicki.
2019. A comprehensive guide to bayesian convolutional neural network with variational inference.
Preprint, arXiv:1901.02731.
Katherine Tian, Eric Mitchell, Allan Zhou, Archit
Sharma, Rafael Rafailov, Huaxiu Yao, Chelsea Finn,
and Christopher Manning. 2023a. Just ask for calibration: Strategies for eliciting calibrated confidence
scores from language models fine-tuned with human
feedback. In Proceedings of the 2023 Conference
on Empirical Methods in Natural Language Processing, pages 5433–5442, Singapore. Association for
Computational Linguistics.
Katherine Tian, Eric Mitchell, Allan Zhou, Archit
Sharma, Rafael Rafailov, Huaxiu Yao, Chelsea Finn,
and Christopher D Manning. 2023b. Just ask for calibration: Strategies for eliciting calibrated confidence
scores from language models fine-tuned with human
feedback. arXiv preprint arXiv:2305.14975.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le,
Ed H. Chi, Sharan Narang, Aakanksha Chowdhery,
and Denny Zhou. 2023. Self-consistency improves
chain of thought reasoning in language models. In

The Eleventh International Conference on Learning Biao Zhang, Barry Haddow, and Alexandra Birch. 2023.
Representations. Prompting large language model for machine translation: A case study. In International Conference on
Zhepei Wei, Wei-Lin Chen, and Yu Meng. 2024. Machine Learning, pages 41092–41110. PMLR.
Instructrag: Instructing retrieval-augmented genMingde Zhao, Tristan Sylvain, Doina Precup, and
eration with explicit denoising. arXiv preprint
Yoshua Bengio. 2024. Identifying and addressarXiv:2406.13629.
ing delusions for target-directed decision-making.
Preprint, arXiv:2410.07096.
Lisa Wimmer, Yusuf Sale, Paul Hofman, Bernd Bischl,
and Eyke Hu¨llermeier. 2023. Quantifying aleatoric
Hang Zheng, Hongshen Xu, Yuncong Liu, Lu Chen,
and epistemic uncertainty in machine learning: Are
Pascale Fung, and Kai Yu. 2025. Enhancing llm
conditional entropy and mutual information approreliability via explicit knowledge boundary modeling.
priate measures? In Proceedings of the Thirty-Ninth
arXiv preprint arXiv:2503.02233.
Conference on Uncertainty in Artificial Intelligence,
volume 216 of Proceedings of Machine Learning
Research, pages 2282–2292. PMLR.
Miao Xiong, Zhiyuan Hu, Xinyang Lu, YIFEI LI, Jie
Fu, Junxian He, and Bryan Hooi. 2024. Can LLMs
express their uncertainty? an empirical evaluation of
confidence elicitation in LLMs. In The Twelfth International Conference on Learning Representations.
Hongshen Xu, Su Zhu, Zihan Wang, Hang Zheng,
Da Ma, Ruisheng Cao, Shuai Fan, Lu Chen, and Kai
Yu. 2024a. Reducing tool hallucination via reliability
alignment. arXiv preprint arXiv:2412.04141.
Hongshen Xu, Zichen Zhu, Da Ma, Situo Zhang, Shuai
Fan, Lu Chen, and Kai Yu. 2024b. Rejection improves reliability: Training llms to refuse unknown
questions using rl from knowledge feedback. arXiv
preprint arXiv:2403.18349.
An Yang, Baosong Yang, Beichen Zhang, Binyuan
Hui, Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian
Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang,
Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang,
Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei
Li, Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men,
Runji Lin, Tianhao Li, Tingyu Xia, Xingzhang Ren,
Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang,
Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and
Zihan Qiu. 2024a. Qwen2.5 technical report. arXiv
preprint arXiv:2412.15115.
An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui,
Bo Zheng, Bowen Yu, Chengyuan Li, Dayiheng Liu,
Fei Huang, Haoran Wei, et al. 2024b. Qwen2. 5
technical report. arXiv preprint arXiv:2412.15115.
Zihao Yi, Jiarui Ouyang, Yuwen Liu, Tianhao Liao,
Zhe Xu, and Ying Shen. 2024. A survey on recent
advances in llm-based multi-turn dialogue systems.
arXiv preprint arXiv:2402.18013.
Xunjian Yin, Baizhou Huang, and Xiaojun Wan. 2023.
ALCUNA: Large language models meet new knowledge. In Proceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing,
pages 1397–1414, Singapore. Association for Computational Linguistics.
11

A Uncertainty Estimation Methods
Below is a detailed summary of the uncertainty
estimation methods used in this study:
1. Raw Logits: This method uses the logit values to estimate confidence, taking the exponential of the average log probability of tokens. It’s equivalent to the reciprocal of perplexity, representing how ”certain” the model
is about its prediction.
2. Agreement (Consistency-based): Confidence is calculated by the percentage of answers in a set that agree with the most-voted
answer, reflecting the model’s consistency in
its outputs.
3. P(True): The model evaluates the truthfulness
of its response, with the confidence being the
normalized probability assigned to the ‘True’
token.
4. Verb. 1S Top-k: The model generates k possible answers and their probabilities in one step.
The top answer and its probability represent
the model’s confidence.
5. Verb. 2S Top-k: This two-stage method has
the model first generate possible answers and
then assign probabilities to them in a second
round. The final confidence is based on these
probabilities.
These methods offer a range of strategies to quantify the model’s belief in its outputs, with different
approaches to capturing certainty and uncertainty.
Prompts used in these methods are shown in Appendix D.1.
B Experimental Setup
B.1 Empirical Study of Delusion
B.1.1 Distribution of Delusion
We employed the five confidence estimation methods mentioned in Appendix A, with the exception
of the consistency method. For the other methods,
inference was performed without sampling, and
the max tokens was set to 128. The consistency
method used a sampling temperature of 0.7, top p
of 0.95, and top k of 40.

B.1.2 Can Belief Ensemble Eliminate
Delusions?
In the Belief Ensemble experiments, we averaged
the outputs from different belief estimation methods and subsequently used the new belief scores to
calculate the delusion rate.
B.2 Delusion vs. Hallucination
B.2.1 LLMs Show Less Honesty with
Delusions
In the experiment designed to assess the models’
willingness to reject unknown questions, we guided
the models with different prompt strategies. The
detailed prompt formulations can be found in the
Appendix D.2. To examine the impact of various
prompts on the delusion rejection rate, we utilized
six different prompts. These prompts were designed to guide the models in rejecting questions
that they could not confidently answer. In the investigation of the effect of model size on rejection
rates, we employed the same prompt across all models, ensuring consistency in the rejection behavior
analysis. This experiment was aimed at investigating how well the models could distinguish between
answering and rejecting questions that fall outside
their knowledge scope.
B.2.2 LLMs Struggle More to Reject
Delusions
For the supervised fine-tuning (SFT) experiments
focused on improving the models’ ability to reject
questions, we extracted 10,000 data points from
the TriviaQA training set. This dataset contained
a specific mix of correct and incorrect answers,
ranging from a 1:9 to a 9:1 ratio. Incorrect answers
were labeled with ”I don’t know,” while correct
answers were assigned their corresponding labels.
The models were fine-tuned using an SFT approach
with 2 epochs and a learning rate of 1e−5.
B.2.3 Delusions Are Harder to Reflect Upon
than Hallucinations
In the model reflection experiment, we prompted
the models to reflect on their initial answers by including the first-round answer in the prompt. The
models were then guided to reconsider the correctness of their answers. The prompt details are provided in the Appendix D.3.

B.3 Formation and Dynamics of Delusion
B.3.1 The Effect of Data Noise on Delusions
In this study, we augment the ALCUNA dataset
by introducing noise. Specifically, for each correct
question-answer pair, we generate 20 perturbed
incorrect answers. This augmentation process simulates the influence of erroneous information on
the model’s ability to distinguish between correct
and incorrect answers.
For the fine-tuning process, we select a subset
of 30,271 numeric-answer questions from the ALCUNA dataset, which includes numerical answers
and multiple-choice question options. The dataset
is divided into training (27,280 samples) and testing sets (test sets not used during training). The
training set is further divided into 11 noise proportions (ranging from 0% to 100%), with each noise
proportion corresponding to four noise intensity
levels (NoiseLevel). Each noise level contains 620
samples, and for each sample, 20 variations are generated via supervised fine-tuning (SFT). The noise
is generated by randomly modifying the correct answer through the addition, deletion, or modification
of characters. For each correct answer, perturbations are made by applying these changes to the
text, which introduces variability into the data. The
noise levels, defined as NoiseLevel, control the degree of consistency among the perturbed answers.
The noise introduced at each level varies as follows:
for NoiseLevel 4, 100% of the noise consists of answers that are identical to one another, generated by
modifying the same data point. For NoiseLevel 3,
75% of the noisy answers share the same modified
version of the data, while the remaining 25% are
different. In NoiseLevel 2, 50% of the noisy answers are consistent, and in NoiseLevel 1 ‘, 25% of
the noisy answers are identical, with the remaining
answers being randomly altered from the standard
answer. This ensures that the noise is spread across
a range of data points at different intensities.
The SFT process is conducted with 5 epochs and
a learning rate of 3 × 10−6. During the training
phase, we sample from these augmented pairs to
simulate different levels of noise and evaluate its
impact on delusion formation. By varying the noise
proportion and intensity, we aim to explore how
the distribution of noisy data and the fine-tuning
process affect the model’s ability to form delusions.

Figure 9: Distribution of the number of similar samples
for each delusion sample.
B.3.2 How Training Affects Delusions
In investigating the impact of the training process
on delusion formation, we constructed supervised
fine-tuning (SFT) training data using 30,271 samples from ALCUNA with entirely correct labels.
The model was trained for 10 epochs with a learning rate of 1 × 10−5.
To assess the effect of reducing training interference, we first used the paraphrase-MiniLM-L6-v2
model* to generate embeddings for all samples. We
then computed the cosine similarity between each
sample’s embedding and the embeddings of the
206 delusion examples identified within the 30,271
samples. If a sample shared the same answer as
any delusion example or had a cosine similarity
score greater than 0.9 with any delusion sample, it
was removed from the dataset. After this filtering
process, 23,507 samples remained, and these were
used for training with their correct labels for 10
epochs, with a learning rate of 1 × 10−5.
B.4 Mitigating Delusions via External
Verification
B.4.1 Mitigating Delusions through
Multi-agent Debating
For each question in TriviaQA, one model was
designated as the ”target” model, and the other
models were used as ”verifiers”. The target model’s
answer was validated by comparing it against the
responses from the verifier models. To determine
whether the answer should be accepted as correct,
a predefined threshold (ranging from 1 to 3) was
applied. This threshold indicated the minimum
number of verifier models that needed to agree with
the target model’s response for it to be considered
*https://huggingface.co/sentencetransformers/paraphrase-MiniLM-L6-v2

accurate. If the number of matching answers from
the verifiers fell below the threshold, the target
model’s response was classified as a delusion and
discarded.
B.4.2 Mitigating Delusions through RAG
For each question, 20 relevant passages are retrieved from a knowledge base to assist in generating the answer. The passages used in this experiment are those extracted for TriviaQA in the
InstructRAG (Wei et al., 2024) framework. The
prompt used in this experiment can be found in
Appendix D.4.
C Complete Experiment Results
C.1 Refuse Rate Comparison with Prompts of
Different Honesty Levels
The complete results are shown in Table 5.
C.2 Refuse Rate Comparison with Different
SFT Refuse Data Ratio
The complete results are shown in Table 6
D Prompts Used in Experiments
D.1 Prompts Used in Different Belief
Estimation Methods
The prompts are shown in Table 7.
D.2 Prompts of Different Honesty Levels
The prompts are shown in Table 8.
D.3 Prompts of Reflection
The prompts are shown in Table 9.
D.4 Prompts of Retrieval-augmented
Generation
The prompts are shown in Table 10.
14

TriviaQA NQ
Model Prompt Strategy
Delu. Hallu. Total Delu. Hallu. Total
helpful can refuse 4.3 18.8 6.8 5.8 13.8 7.1
helpful less refuse 2.4 10.5 3.3 3.3 8.3 4.0
helpful more refuse 6.9 29.2 11.5 7.5 18.6 9.7
Llama-3.1-8B-Instruct
helpful medium refuse 23.5 51.6 26.1 20.4 37.0 24.1
helpful most refuse 40.3 69.7 42.3 32.5 47.6 34.9
helpful high refuse 11.7 34.9 16.0 9.0 20.3 11.4
helpful can refuse 7.6 24.1 10.6 15.0 32.2 20.1
helpful less refuse 2.2 11.3 4.6 8.3 18.6 11.1
helpful more refuse 7.9 23.0 10.5 23.8 43.3 28.4
Qwen2.5-7B-Instruct
helpful medium refuse 6.8 21.8 9.6 21.9 41.1 26.2
helpful most refuse 24.1 48.2 24.7 49.9 70.6 52.0
helpful high refuse 23.4 49.7 25.4 51.7 73.1 54.5
helpful can refuse 1.6 14.3 6.1 6.1 21.4 14.1
helpful less refuse 0.7 8.1 3.3 3.0 14.1 8.6
helpful more refuse 28.8 52.4 32.0 43.4 68.6 54.9
Mistral-7B-Instruct-v0.1
helpful medium refuse 8.4 28.3 14.1 18.8 43.0 31.1
helpful high refuse 25.7 52.4 30.8 39.3 68.3 54.2
helpful most refuse 13.4 36.2 19.4 24.2 50.1 36.8
Table 5: Complete results of refuse rate comparison with prompts of different honesty levels.
SFT Refuse TriviaQA NQ
Model
Data Ratio Delu. Hallu. Total Delu. Hallu. Total
10% 21.7 43.9 16.6 45.4 70.0 52.5
20% 43.8 72.2 33.0 75.8 92.9 78.9
30% 54.5 81.6 41.2 74.2 91.8 76.0
40% 69.1 89.2 53.1 79.2 93.0 79.3
Llama-3.1-8B-Instruct 50% 72.7 91.3 56.9 76.7 92.7 78.3
60% 79.4 93.6 65.8 79.8 93.3 80.7
70% 87.0 96.0 74.9 86.3 95.1 85.4
80% 93.2 98.5 86.4 90.6 97.0 91.4
90% 96.2 99.1 93.4 93.3 99.1 94.8
10% 28.7 46.8 21.8 61.9 83.0 65.0
20% 42.3 65.6 32.4 75.9 93.2 78.7
30% 50.2 75.8 39.4 82.3 96.0 84.2
40% 63.3 86.7 49.9 83.9 96.8 85.8
Qwen2.5-7B-Instruct 50% 69.5 90.6 56.1 84.2 96.6 85.2
60% 76.3 93.1 62.0 84.9 96.2 84.9
70% 81.1 95.6 68.4 84.7 96.4 84.6
80% 87.6 97.2 75.8 86.4 97.0 86.9
90% 95.0 98.9 87.9 93.6 99.2 93.9
10% 21.1 41.9 25.9 36.6 63.0 50.0
20% 42.1 63.1 46.1 61.2 81.4 69.7
30% 61.0 76.3 61.4 73.1 89.1 80.2
40% 74.5 85.2 73.4 79.7 93.0 86.1
Mistral-7B-Instruct-v0.1 50% 81.7 89.3 80.2 84.4 94.7 89.2
60% 86.5 92.3 85.1 87.7 95.5 91.3
70% 91.1 94.5 89.2 90.4 96.6 93.3
80% 94.4 96.8 92.9 91.6 97.0 94.5
90% 97.2 98.0 96.1 94.0 98.2 96.5
Table 6: Complete results of refuse rate comparison with different SFT refuse data ratio.
15

Logits-based Prompt
You are a helpful assistant.
Answer the following question as accurately as possible.
Question: {question}
P(true) Prompt
You are a helpful assistant. You should judge whether the answer to the given question is True or False. Please only reply with a
simple word ”True” or ”False”.
Answer the following questions as accurately as possible.
Question: {question}
Answer: {answer}
Is the above answer correct? (True / False)
Consistency Prompt
You are a helpful assistant.
Answer the following question as accurately as possible. Provide ONLY the direct answer without any explanation.
Question: {question}
Verb. 1S top1 Prompt
You are a helpful assistant, and you are always completely honest and DIRECT in your responses.
Provide a brief, concise answer along with an explicit confidence percentage (0-100%) about the correctness of your response.
Question: {question}
Verb. 2S top1 Prompt
You are a helpful assistant, always completely honest and direct in your responses. You are also transparent about your
confidence level and can honestly share how certain you are about the answer.
Question: {question}
Answer: {previous answer}
How confident are you in the above answer (0-100%)?
Table 7: Prompts Used in Different Belief Estimation Methods.
16

”Helpful Can Refuse” Prompt
You are a helpful assistant. If you don’t have information o
Answer the following question as accurately as possible.
Question: {question}
”Helpful Less Refuse” Prompt
You are a helpful assistant. If you have relevant information
accurate response. Only refuse a question if you’re complete
In cases where you are unsure, or if the question falls outsid
answer questions to the best of your ability, and only reject a
as helpful as possible. Providing a response, even if not per
Answer the following question as accurately as possible.
Question: {question}
”Helpful More Refuse” Prompt
You are a helpful assistant. If you lack sufficient information
don’t know.’’ It’s important that your answers are accura
provide incorrect information. In such cases, you do not ne
accuracy over attempting to answer something you cannot b
Answer the following question as accurately as possible.
Question: {question}
”Helpful Medium Refuse” Prompt
You are a helpful assistant. If you have any doubt that your a
Accuracy is paramount, and if you’re uncertain or lack suffic
answer. Do not attempt to offer an answer if you are not con
Answer the following question as accurately as possible.
Question: {question}
”Helpful High Refuse” Prompt
You are a highly cautious and precise assistant. If you are u
and accurate answer, you must refuse to answer. Always prio
there is even the slightest doubt about the accuracy of your
answer questions if you are not fully confident in your respo
refuse to answer without hesitation.
Answer the following question as accurately as possible.
Question: {question}
”Helpful Most Refuse” Prompt
You are a highly cautious and precise assistant. If you are u
and accurate answer, you must refuse to answer. Always prio
there is even the slightest doubt about the accuracy of your
answer questions if you are not fully confident in your respo
refuse to answer without hesitation.
Answer the following question as accurately as possible.
Question: {question}
Table 8: Prompts of D
Reflection on Previous Answer Prompt
You are a helpful assistant. You will be given a question an
previous answer fully and accurately addresses the question
incomplete, or inaccurate. If you identify any potential issu
accordingly. Only if, after thorough reflection, you believe y
be made, should you respond with ‘‘I insist.’’
Question: {question}
Previous Answer: {previous answer}
Table 9: Prompt used to reflect

question, please answer with ”I don’t know”.
answer a question, please respond with your best and most
ncertain or lack the necessary information to provide an answer.
our knowledge, simply reply with ‘‘I don’t know.’’ Try to
stion when it is absolutely necessary, ensuring your answers are
is often better than offering no answer at all.
onfidence to answer a question correctly, simply reply with ‘‘I
nd if you’re uncertain, it’s better to refuse the question than to
elaborate; just respond with ‘‘I don’t know.’’ Prioritize
re of.
er could be incorrect, please respond with ‘‘I don’t know.’’
information to confidently provide a correct response, refuse to
nt. Please prioritize certainty and precision in your responses.
tain or do not have enough information to provide a confident
e caution and precision over attempting to answer a question. If
onse, respond with ‘‘I don’t know.’’ Never attempt to
. If the question is unclear, or ambiguous, or you lack context,
tain or do not have enough information to provide a confident
e caution and precision over attempting to answer a question. If
onse, respond with ‘‘I don’t know.’’ Never attempt to
. If the question is unclear, or ambiguous, or you lack context,
erent Honesty Levels.
ur previous answer. Please carefully reflect on whether your
nsider if any part of your response could be misleading,
areas for improvement, you should modify your answer
answer is completely accurate and there are no improvements to
he previous answer’s accuracy.

RAG Prompt
You are a helpful assistant who provides the best possible answer. When uncertain about something, you’ll make a guess. Based
on the provided documents, answer the following question.
Question: {question}
If the provided documents are not helpful, you should answer based on your own knowledge.
Documents: {passages}
Table 10: Prompt used in Retrieval-augmented Generation.
18
