---
title: "Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent"
source_pdf: "08_route_planning_agents\\04_AgentMob_Chen2026.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-07-03T12:08:29+00:00
page_count: 15
status: ok
text_char_count: 60877
quality_flags: []
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\08_route_planning_agents\04_AgentMob_Chen2026.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-07-03T12:08:29+00:00
- Page count: 15
- Status: ok
- Text chars: 60877
- Quality flags: none

## Metadata

- Title: Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent
- Author: Linyao Chen; Qinlao Zhao; Zechen Li; Mingming Li; Likun Ni; Jinyu Chen; Yuhao Yao; Xuan Song; Noboru Koshizuka; Hiroki Kobayashi
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

Individual-level mobility prediction is central to urban simulation, transportation planning, and policy analysis. Supervised sequence models achieve strong accuracy but require taskspecific training and offer limited decisionlevel transparency. Recent LLM-based methods improve interpretability, yet mostly rely on static prompts and single-pass inference, limiting their ability to seek additional evidence when mobility signals are weak or conflicting. We propose AgentMob, a training-free LLM-driven agent framework that formulates next-location prediction as adaptive evidencecontrolled decision making. AgentMob resolves routine cases through a fast path based on historical regularity, while ambiguous cases trigger iterative tool use over recent trajectories, historical behavior, stay-move likelihood, and geographical evidence. Across three mobility datasets, AgentMob achieves the strongest overall performance among training-free LLMbased methods, with GPT-5.4 reaching 71.42% Acc@1 on BW, 33.14% on YJMob100K, and 33.50% on Shanghai ISP. On BW non-fast-path cases, the LLM controller improves Acc@1 from 30.65% to 48.62% over a same-tool statistical baseline, showing that its main benefit lies in resolving ambiguous predictions through adaptive evidence gathering. Our code is available at AgentMob.

## Outline

- Introduction (page 1)
- Related Work (page 2)
- Methodology (page 3)
  - Pipeline of LLM-based Tool Agent for Next Location Prediction (page 3)
  - Mobility Analysis Toolbox (page 3)
- Experiment (page 4)
  - Experimental Setup (page 4)
  - Main Results (page 5)
  - Ablations (page 7)
- Conclusion and Future Work (page 8)
- Limitations (page 8)
- Risk Statement (page 9)
- Qualitative Trajectory Visualization (page 11)
- Location Description prediction (page 11)
- Ablation Case Examples (page 12)
- Inference Case Studies (page 13)
  - Baseline-by-Dataset Comparison Cases (page 13)

## Markdown Content

Towards Efficient and Evidence-grounded Mobility Prediction
with LLM-Driven Agents
Linyao Chen1 Qinlao Zhao2 Zechen Li3 Mingming Li1
Likun Ni5 Jinyu Chen1,† Yuhao Yao4,†
Xuan Song7 Noboru Koshizuka1 Hiroki H. Kobayashi1
1The University of Tokyo 2Huazhong University of Science and Technology
3University of New South Wales, Sydney 4LocationMind Inc.
5Southern University of Science and Technology
7Jilin University †Corresponding authors

Abstract
Individual-level mobility prediction is central
to urban simulation, transportation planning,
and policy analysis. Supervised sequence models achieve strong accuracy but require taskspecific training and offer limited decisionlevel transparency. Recent LLM-based methods improve interpretability, yet mostly rely on
static prompts and single-pass inference, limiting their ability to seek additional evidence
when mobility signals are weak or conflicting. We propose AgentMob, a training-free
LLM-driven agent framework that formulates
next-location prediction as adaptive evidencecontrolled decision making. AgentMob resolves routine cases through a fast path based
on historical regularity, while ambiguous cases
trigger iterative tool use over recent trajectories, historical behavior, stay-move likelihood,
and geographical evidence. Across three mobility datasets, AgentMob achieves the strongest
overall performance among training-free LLMbased methods, with GPT-5.4 reaching 71.42%
Acc@1 on BW, 33.14% on YJMob100K, and
33.50% on Shanghai ISP. On BW non-fast-path
cases, the LLM controller improves Acc@1
from 30.65% to 48.62% over a same-tool statistical baseline, showing that its main benefit
lies in resolving ambiguous predictions through
adaptive evidence gathering. Our code is available at AgentMob.
1 Introduction
Accurate human mobility prediction is fundamental
to urban planning (Zheng et al., 2014), transportation management (Luca et al., 2021), and public
health analysis (Barbosa et al., 2020). At the individual level, next-location prediction supports
location-based services (Zheng, 2015), demandaware transportation systems, and targeted public
health interventions (Oliver et al., 2020). The core
challenge is to infer a user’s next spatial state from
historical trajectories, recent movement context,
6202
nuJ
3
]GL.sc[
1v03150.6062:viXra

a Deep Neural Network (DNN) Drawbacks
1. Blackbox Model
Train Predict H wh a y rd a t o lo i c n a te ti r o p n r e is t
predicted.
2. Data Deficiency
Tra G je P c S tory DNN Model T P r r a e j d e i c c t t o e r d y R la e b q e u le ir d e d s a la ta rg a e n -s d c c a o le stly
retraining.
b LLM (Prompt Engineering) Drawbacks
1. Irreversible Inference
Textualize Convert Predict S w i i n th g l n e o -p c a h s a s n p c r e e d to iction
revise.
Tra G je P c S tory T t e r x a t je u c a t l o iz r e y d (Co C M m o e n p m t r e o e x s r t y s ) ed LLM Te lo x c tu a a ti l o iz n ed 2 A co . l l m I e n p v f r o id e r e s m n s c e a e d ti i o i s n n to B a ottleneck
bounded prompt.
c Our Method: Agentic Framework Our Advantages
1) Individual mobility knowledge Predict 1. Adaptive Planning
Textualize Refine Retrieve F de a e st p - p r a ea th s o fo n r i n ro g u o ti n n l e y w ca h s e e n s;
signals are weak/conflicting.
Tra G je P c S tory T T e r x a t j u e a c l t i o z r e y d Mo k b n ili o ty w b le e d h g a e vior Te lo x c tu a a ti l o iz n ed 2. Grounded Inference
2) Tool Box Leverages multi-source
mobility & geographic
evidence for reliable
... predictions.
r Mceot o rni b etei v lixt e ytr GIenR ofoe grt rmr a ie pav hteiior cnal SEtsatyim-Maotover Invoke LLM-based 3. Iterative Refinement
Agent I c t r e o r s a s ti - v c e h l e y c g k a s t h e e v r id s e a n n c d e,
enabling self-correction
and better decisions.
3) Urban
Geographical Knowledge Retrieve
(POIs,Regions Descriptions, etc.)
From static prediction to adaptive, evidence-grounded, and Iterative inference.
Figure 1: Comparison between different mobility prediction paradigms. Our method proposes adaptive,
evidance-grounded and iterative prediction in a trainingfree manner, provides effecient and reliable predictions.
and the geographical semantics of candidate locations.
Existing approaches largely follow two
paradigms. Supervised sequence models,
including RNNs (Feng et al., 2018), Transformers (Vaswani et al., 2017), and their variants, learn
mobility regularities from large-scale trajectory
data and can achieve strong predictive accuracy.
However, they require task-specific training, are
costly to adapt to new cities or spatial granularities,
and typically provide limited insight into why a
particular location is predicted. Recent LLM-based
methods (Zhao et al., 2026; Zhang et al., 2024)
offer a more interpretable alternative by converting

trajectories into text and leveraging languagemodel reasoning. Fine-tuning approaches (Feng
et al., 2024; Li et al., 2024a) still inherit substantial
training cost, while prompt-based methods (Wang
et al., 2024b; Calderón et al., 2025) avoid retraining
but compress all available evidence into a static
prompt. Agent-like mobility frameworks (Feng
et al., 2025; Li et al., 2025) introduce structured
memory or reasoning modules, but often rely on
pre-scripted workflows with limited ability to
adapt the amount and type of evidence used for
each prediction.
This static prediction paradigm is problematic
since mobility instances are not equally difficult.
Many cases are routine: a user repeatedly visits
the same location at a similar weekday and hour,
so historical regularity may be sufficient. Other
cases are ambiguous: recent movement, long-term
routines, stay–move tendencies, and geographical
plausibility may point to different candidate locations. In such cases, a reliable predictor should
not commit after a single forward pass. It should
retrieve targeted evidence, cross-check conflicting
signals, and stop once the evidence is sufficient.
Existing prompt-only LLM methods lack this capability since prediction is performed through a fixed
context and a single generation step, with no structured mechanism to verify or revise the decision.
To address this limitation, we propose AgentMob, a training-free agentic framework that formulates next-location prediction as adaptive evidencecontrolled decision making. Instead of treating the
LLM as a direct trajectory predictor, AgentMob
uses it as a controller that decides how much evidence is needed for each instance. Routine cases
exit through a fast path based on strong historical
regularity, while ambiguous cases trigger iterative
tool use over recent trajectory context, historical behavioral statistics, stay–move likelihood, geographical distance, and location semantics. The final
prediction is thus grounded in explicit tool outputs
rather than opaque prompt-only generation.
As illustrated in Figure 1, AgentMob differs
from supervised DNNs and prompt-based LLM
methods in both computation and reasoning. It
does not require task-specific model training, and it
avoids forcing all samples through the same fixed
inference procedure. Instead, it allocates reasoning effort according to prediction difficulty and
records timestamp-bounded tool outputs for auditability. We evaluate AgentMob with both opensource and closed-source LLM backbones on three

mobility datasets with different spatial granularities. Experiments show that AgentMob achieves
the strongest overall performance among trainingfree LLM-based methods, while additional analyses demonstrate that the LLM controller is most
beneficial when deterministic mobility statistics are
insufficient or conflicting. In summary, our contributions are as follows:
• Adaptive evidence-control formulation. We
recast next-location prediction as an instancelevel decision process, where an LLM agent
chooses between a fast historical-regularity
path and additional evidence gathering for ambiguous cases.
• Training-free tool-augmented mobility
agent. We develop AgentMob, which
selectively invokes mobility tools over recent
context, historical behavior, stay–move
likelihood, and geographical evidence to
produce auditable prediction traces.
• Strong and explainable training-free performance. Across three mobility datasets
and multiple LLM backbones, AgentMob
achieves the strongest overall results among
training-free LLM-based methods, with analyses showing that adaptive evidence gathering
is most useful when mobility signals conflict.
2 Related Work
Individual Next-Location Prediction. Nextlocation prediction has evolved from Markov-chain
and factorization-based methods (Rendle et al.,
2010; Gambs et al., 2012) to deep sequence models
based on RNNs (Feng et al., 2018; Liu et al., 2016),
Transformers (Lian et al., 2020; Luo et al., 2021;
Qin et al., 2022; Sun et al., 2024), and GNNs (Wang
et al., 2024c; Wu et al., 2024). These methods
learn complex spatiotemporal dependencies from
large-scale mobility data, but typically require taskspecific training and provide limited decision-level
transparency. Recent LLM-based methods convert trajectories into textual inputs for mobility prediction or generation (Wang et al., 2023, 2024a;
Liang et al., 2024); some fine-tune LLMs for pointof-interest recommendation or trajectory generation (Li et al., 2024a,b), while others integrate
memory, urban knowledge, or structured reasoning modules (Feng et al., 2025; Ju et al., 2025;
Zhong et al., 2025; Liu et al., 2025). However,
most existing LLM-based mobility methods still

follow a fixed inference procedure, where history
or knowledge is retrieved in advance, compressed
into a prompt or scripted workflow, and then used
to produce a prediction. Closely related agentic mobility frameworks, such as AgentMove (Feng et al.,
2025) and ARMove (Wang et al., 2026), introduce
structured memory, user profiling, feature management, or feature optimization. In contrast, AgentMob treats next-location prediction as an instancelevel evidence-control problem: the agent decides
whether a sample can exit through a fast historicalregularity path, which tools to invoke for ambiguous cases, and how to resolve conflicts among recent context, historical behavior, stay–move likelihood, and geographical plausibility.
LLM-Driven Agents and Evidence-Grounded
Tool Use. LLM-driven agents extend LMs from
passive text generation to interactive reasoning
and action. Prior work has explored instructionfollowing (Ouyang et al., 2022), multi-agent collaboration (Li et al., 2023; Wu et al., 2023; Li
et al., 2026), general task automation (Hu et al.,
2025; Tang et al., 2025), social simulation (Park
et al., 2023), and tool-augmented problem solving (Nakano et al., 2021; Qin et al., 2023). These
studies suggest that LLMs can coordinate intermediate evidence and external tools, but they are not
directly designed for next-location prediction under
spatiotemporal uncertainty. AgentMob instantiates
evidence-grounded tool use for mobility prediction,
where tool invocation is controlled by prediction
difficulty and each decision is traceable through
timestamp-bounded behavioral and geographical
evidence.
3 Methodology
3.1 Pipeline of LLM-based Tool Agent for
Next Location Prediction
Figure 2 illustrates the overall workflow of AgentMob. We formulate next-location prediction as an
adaptive evidence-control process, where an LLM
agent decides whether a test instance can be solved
from historical regularity or requires additional evidence from mobility-analysis tools. The framework
is implemented with smolagents (Roucher et al.,
2025), but the key design is independent of a specific agent library: the LLM acts as a controller that
selects tools, interprets their outputs, and produces
a ranked prediction over candidate spatial units.
Given raw GPS records, we first discretize coordinates into spatial units, either administrative

polygons or uniform grid cells depending on the
dataset. Each spatial unit is paired with a concise
textual description of its urban function, allowing
the LLM to reason over both trajectory statistics
and location semantics. The prediction task is then
defined as selecting the spatial unit that the user
will visit next, given the user ID, target timestamp,
historical trajectory records, and the observed context before the target time.
Fast-path Prediction. AgentMob first performs
a lightweight regularity check before invoking
the full tool-calling loop. If the user’s historical
records show a dominant location for the same
weekday and hour, the agent returns this location
directly as the prediction. This fast path resolves
routine cases efficiently and prevents unnecessary
LLM/tool computation when the historical signal
is already strong.
Adaptive Tool-calling Prediction. When strong
historical regularity is absent, AgentMob enters
the tool-calling mode. The agent invokes tools
from the mobility-analysis toolbox described in
Section 3.2. These tools provide two complementary types of evidence: behavioral evidence, such
as recent trajectory context, same-time visitation
statistics, stay–move likelihood, and historical transitions under similar conditions; and geographical
evidence, such as distance to candidate locations
and textual descriptions of their urban functions.
Based on the evidence collected so far, the agent
may request additional tool outputs, compare competing candidates, or proceed to a final decision.
The loop is capped at ten iterations to bound inference cost.
Prediction and Auditability. After evidence
gathering, the agent outputs a final top-1 prediction together with a ranked top-K candidate list
for rank-based evaluation. All tool invocations are
constrained to the training split and to observations available before the target timestamp, ensuring chronological validity. For auditability, each
prediction trace stores the user ID, target timestamp, allowed history range, invoked tools, serialized tool outputs, LLM reasoning steps, and final
ranked prediction.
3.2 Mobility Analysis Toolbox
The toolbox exposes compact, timestamp-bounded
evidence that the agent can selectively query, with
each tool summarizing a distinct mobility signal

Toolbox
Mobility Recent Trajectory
Context
Retriever Historical visitation
(Too To l o in l v A o g a e c n t t ion) G In e R f o o e g r t r m r a ie p a v h t e i i o c r n a l G Ge eo o g gr ra a p p h h i i c c a a l l D De is s t c a r
S E t s a t y im -m a o to v r e Probability of Movem
Historical
Behavior Behavioral statistics
Retriever
No Iteratio
Timestamp Strong
historical
User ID regularity? Yes
Figure 2: AgentMob The workflow of Agentmob. Th
regular cases 2. adaptive tool use for ambiguous cases,
The primary tool retrieves multi-dimensional informati
instead of passing raw trajectories directly to the
LLM. Together, these tools cover four complementary aspects of next-location prediction: recent context, geographical plausibility, stay–move uncertainty, and historical behavior under comparable
conditions.
Mobility Context Retriever. Given a target
timestamp, this tool summarizes the user’s shortterm movement context and routine temporal patterns. It returns the recent sequence of visited locations over the past several hours, together with
visitation statistics for the same weekday and hour
in the user’s historical records. This evidence helps
the agent distinguish immediate movement continuity from long-term temporal regularity.
Geographical Information Retriever. This tool
provides spatial and semantic evidence for candidate locations. It returns the distance from the
current location to each candidate, as well as a concise textual description of the candidate’s urban
function. This allows the agent to check whether a
candidate is geographically plausible and semantically consistent with the user’s mobility context.
Stay–Move Estimator. This tool estimates
whether the user is more likely to remain at the current location or move elsewhere. It compares the
current stay duration with historical stay-duration
statistics at the same location and returns a movement likelihood derived from past behavior. This

cs
Need Yes
more
context?
No Tool Agent
(LLM Inference)
Yes
Enough
tion
context?
aximally 10
No
Predicted location
ey faeture includes: 1. fast-path prediction for highly
evidence-controlled stopping before final prediction 3.
or reliable evidence-grounded inference.
evidence is especially useful when recent continuity conflicts with transition-based predictions.
Historical Behavior Retriever. This tool retrieves behavioral evidence from past visits to the
same or nearby locations under comparable temporal contexts, such as similar time of day or day of
week. It summarizes typical dwell times, frequent
next destinations, transition tendencies, and visit
regularity. The agent uses this evidence to verify
uncertain candidates and resolve conflicts among
competing mobility signals.
4 Experiment
4.1 Experimental Setup
Datasets. We evaluate AgentMob on three mobility datasets with different spatial granularities
and observation mechanisms. BW (Blogwatcher,
Inc., 2024) is a mobile-phone GPS dataset from the
Tokyo metropolitan area, where raw GPS records
are mapped to third-level administrative polygons
annotated with hierarchical region names and functional descriptions. YJMob100K (Yabe et al., 2024)
is a large-scale mobile-phone GPS dataset discretized into anonymized 500 m×500 m grid cells;
since cells do not have real place names, we generate textual descriptions from the provided POI category distributions using LLM-based POI summarization (Appendix B). For BW and YJMob100K,
we select the 100 most active users and convert

Statistic BW YJMob100K Shanghai ISP
Records 427,248 310,546 4,944
Region Tokyo Anonymized Shanghai
Spatial unit Admin. polygons 500 m grids 500 m grids
Eval. setting Top-100 users Top-100 users 200 first-test users
Visited locations 4,188 polygons 12,430 cells 1,385 cells
Move / stay transitions 28.6 / 71.4% 74.7 / 25.3% 90.0 / 10.0%
Avg. unique locations 104.8 413.7 10.7
Table 1: Dataset statistics and evaluation settings.
continuous trajectories into spatial-unit sequences
with location descriptions (Table 1). Shanghai
ISP (Feng et al., 2019) is an anonymized mobilenetwork trajectory benchmark collected from mobile network logs in Shanghai, containing 325,215
records from April 19 to 26, 2016; following recent
LLM-based next-location prediction work (Feng
et al., 2025), we discretize base-station coordinates
into 500 m×500 m grid cells and generate textual
descriptions for each cell.
Baselines. We compare AgentMob with two supervised sequence models and four LLM-based
mobility prediction methods. The supervised
baselines include DeepMove (Feng et al., 2018),
an attentional RNN designed to capture periodic mobility patterns and long-term user preferences, and a vanilla Transformer (Vaswani et al.,
2017). The LLM-based baselines include AgentMove (Feng et al., 2025), which decomposes
zero-shot prediction into spatial-temporal memory,
world knowledge, and collective pattern modules;
LLM-Mob (Wang et al., 2023), which formulates
prediction as in-context learning over structured trajectory prompts; TrajLLM (Ju et al., 2025), which
converts mobility sequences into textual representations for sequential reasoning; and LLM Urban
Residents (Wang et al., 2024a), which models individuals as LLM agents conditioned on activity
patterns and retrieved daily motivations. For LLMbased methods, we evaluate Qwen3-8B (Yang et al.,
2025), GPT-4.1-mini (OpenAI, 2025), and GPT5.4 (OpenAI, 2026) as backbones. All methods are
evaluated under the same chronological train/test
split for each dataset. DeepMove and Transformer
are trained only on the training split, while LLMbased baselines and AgentMob can access the same
training-history records and only the observed context before each target timestamp during inference.
Evaluation Metrics. For each test instance, the
model outputs a ranked list of candidate locations.
We report three metrics: Acc@1, which measures
whether the top-ranked prediction matches the
ground-truth location; MRR@5, which computes

the reciprocal rank of the ground truth within the
top five predictions and assigns zero if it is absent;
and mean top-1 geographic distance, which measures the Haversine distance in kilometers between
the predicted and ground-truth locations.
4.2 Main Results
Performance against Baselines. Table 2 reports
the main comparison on BW, YJMob100K, and the
Shanghai ISP first-test-point setting. The Shanghai
ISP evaluation follows the same 200-user first-test
sample used in prior work (Feng et al., 2025), and
all methods are evaluated under the same chronological split within each dataset. Overall, AgentMob achieves the strongest performance among
training-free LLM-based methods. With GPT5.4, AgentMob obtains 71.42% Acc@1, 78.84%
MRR@5, and 2.20 km distance on BW; 33.14%,
46.55%, and 4.29 km on YJMob100K; and 33.50%,
47.44%, and 4.23 km on Shanghai ISP. These results show that adaptive evidence gathering improves LLM-based mobility prediction across different spatial granularities and observation settings.
Compared with supervised baselines, AgentMob does not always dominate task-specific sequence models. On BW, Transformer achieves
the best overall Acc@1 and MRR@5, suggesting
that supervised training remains highly effective
when sufficient regular mobility data are available.
However, AgentMob with GPT-5.4 outperforms
supervised baselines on YJMob100K and Shanghai ISP, where the location space is denser or the
available history is shorter. This suggests that
evidence-grounded LLM reasoning can be competitive with task-specific training when calibrated
mobility statistics, recent context, and location semantics provide useful decision evidence.
Among LLM-based baselines, GPT-5.4 generally improves performance, but the gains vary by
method and dataset. LLM Urban Residents remains
a strong baseline on BW, likely because its activitypattern modeling aligns with the stronger temporal
regularity of this dataset. AgentMove is competitive on YJMob100K, while AgentMob achieves
better overall ranking and/or spatial accuracy by
explicitly cross-checking behavioral and geographical evidence. The distance metric is particularly
informative: on YJMob100K and Shanghai ISP,
AgentMob avoids the larger spatial drift observed
in several prompt-based or scripted LLM baselines.
Appendix D.1 provides one case for each dataset–
baseline pair, showing how these aggregate differ-

Table 2: Main performance comparison under chronolog
first-test-point setting. Bold marks the best result amon
training-free LLM-based methods.
BW
Method Backbone
Acc@1↑ MRR@5↑ D
DeepMove 72.13% 78.92% 2
Deep Neural Network
Transformer 73.04% 79.67% 2
GPT-4.1-mini 58.52% 70.16% 3
AgentMove Qwen3-8B 52.58% 64.09% 4
GPT-5.4 64.20% 74.02% 3
GPT-4.1-mini 55.08% 66.10% 3
LLM-Mob Qwen3-8B 56.19% 65.53% 3
GPT-5.4 66.48% 74.84% 2
GPT-4.1-mini 53.08% 64.33% 6
TrajLLM Qwen3-8B 52.58% 64.04% 4
GPT-5.4 62.23% 72.54% 3
GPT-4.1-mini 64.38% 72.89% 2
LLM Urban Res. Qwen3-8B 58.93% 68.00% 3
GPT-5.4 68.40% 76.36% 2
GPT-4.1-mini 66.30% 76.33% 2
Ours Qwen3-8B 62.65% 74.30% 2
GPT-5.4 71.42% 78.84% 2
Figure 3: Effect of the LLM controller. AGENTMOBSTATISTICS uses the same tool evidence as AgentMob
but replaces the LLM controller with a deterministic
decision rule. Full AgentMob uses GPT-5.4.
ences appear at the prediction level.
Shanghai ISP reveals a metric-specific exception.
LLM-Mob with GPT-4.1-mini achieves the highest
MRR@5, while AgentMob achieves higher Acc@1
and lower geographic distance. Since Shanghai
ISP contains only eight days of trajectories, several
nearby grids can remain plausible for a given user,
making top-K ranking easier than selecting the exact top-1 location. AgentMob is optimized for the
final evidence-grounded decision, which improves
top-1 accuracy and spatial error, but does not always yield the most favorable ordering among the
remaining plausible candidates. Qualitative trajectory visualizations are provided in Appendix A.
Reasoning Process Analysis. To isolate the contribution of the LLM controller from the underlying mobility statistics, we introduce AGENTMOBSTATISTICS, a non-LLM baseline that uses the
same tool evidence as AgentMob but replaces the
LLM controller with a deterministic decision rule.

l evaluation on BW, YJMob100K, and the Shanghai ISP
l methods, and underlining marks the best result among
YJMob100K Shanghai ISP
Acc@1↑ MRR@5↑ Dist.↓ Acc@1↑ MRR@5↑ Dist.↓
31.52% 44.86% 4.86 20.50% 30.00% 6.95
33.12% 46.12% 4.81 22.00% 32.25% 9.26
29.25% 41.33% 4.77 26.50% 39.26% 4.78
29.41% 41.84% 5.36 28.00% 38.48% 5.75
33.09% 46.51% 4.46 27.00% 39.28% 5.35
21.38% 35.42% 5.98 33.00% 47.61% 5.22
23.57% 36.50% 5.84 26.50% 40.67% 6.87
26.20% 39.15% 5.20 29.50% 45.38% 6.44
24.25% 37.21% 11.57 22.50% 36.30% 7.18
28.12% 42.23% 5.16 22.00% 35.00% 6.54
29.35% 43.20% 4.68 25.00% 39.46% 19.74
26.59% 40.02% 5.21 32.00% 47.28% 4.23
25.89% 39.51% 5.90 19.5% 24.74% 7.37
29.36% 42.91% 4.62 31.50% 46.96% 4.45
31.81% 45.97% 4.25 33.00% 45.48% 4.23
30.56% 45.27% 4.39 32.00% 46.78% 4.30
33.14% 46.55% 4.29 33.50% 47.44% 4.23
As shown in Figure 3, structured mobility statistics already provide a strong baseline, but the LLM
controller further improves decision quality when
evidence needs to be reconciled. On BW, AgentMob improves Acc@1 from 60.05% to 71.42%,
MRR@5 from 70.48% to 78.84%, and reduces distance from 3.44 km to 2.20 km. On Shanghai ISP,
Acc@1 increases from 25.50% to 33.50%, with
distance reduced from 5.86 km to 4.23 km.
The gain is smaller on YJMob100K, where
AGENTMOB-STATISTICS and AgentMob are
nearly tied in Acc@1. This is likely because YJMob100K uses anonymized grid cells with limited
semantic cues, and the structured mobility statistics already capture much of the predictable routine. Nevertheless, AgentMob slightly improves
MRR@5 and reduces spatial error, suggesting that
the controller mainly helps avoid worse off-target
predictions rather than changing many exact top-1
decisions.
The benefit of the controller becomes clearer
on difficult cases. On the BW non-fast-path
subset, where strong historical regularity is absent, AgentMob improves Acc@1 from 30.65%
to 48.62% and MRR@5 from 46.67% to 60.66%
over AGENTMOB-STATISTICS. This supports our
central hypothesis: the LLM controller is most
useful when deterministic mobility statistics are
insufficient and multiple evidence sources must be
cross-checked.
Appendix D.1 provides representative traces.
The BW fast-path case is resolved directly by a per-

Figure 4: Difficulty-stratified gains of AgentMob over
AGENTMOB-STATISTICS on BW and YJMob100K.
The sample size N is shown under each subset.
fectly repeated target-hour pattern, while the other
cases show AgentMob correcting tempting baseline
choices by checking hour-specific transitions, local
movement evidence, or candidate-ranking signals.
These examples support the same mechanism as
the aggregate controller results: the agent is most
useful when it can cross-check a plausible but weak
cue before committing to the final top-1 prediction.
Difficulty-stratified analysis. Figure 4 compares
AgentMob with AGENTMOB-STATISTICS across
fast-path and harder cases. AgentMob improves
the accuracy of all cases, but the gains are larger
when deterministic evidence is weaker. The least
gain of +6.58% Acc@1 and +4.39% MRR@5 appears on non-fast-path cases, the most is +13.09%
Acc@1 and +9.87% MRR@5 under high conflict
cases. This indicates the role of the LLM controller in the system. Highly regular cases can
often be resolved by structured statistics, whereas
difficult cases benefit from the evidence analysis
and inference by the LLM controller. When deterministic regularity is weak, candidate scores are
close, or historical routines are unreliable, the LLM
controller can compare temporal, transition, staymove, and spatial evidence before making the final
prediction. The effect is also dataset-dependent.
On YJMob100K and Shanghai ISP, where location
information is anonymized grid cell and semantic
evidence is limited, the LLM has lesser semantic
information beyond the statistics. As a result, the
metric improvement of AgentMob is not so significant as AGENTMOB-STATISTICS.
Efficiency and Cost Analysis. Table 3 reports
trace-derived efficiency statistics for GPT-5.4 runs.
For each dataset, we compare AgentMob with the
strongest GPT-5.4 LLM-based baseline in Table 2.
The efficiency behavior reflects the adaptive allocation strategy of AgentMob: routine cases can

Dataset Method Fast path Tools Tokens Wall
/sample /sample (s/sample)
BW LLM Urban Res. – – 4.15k 2.32
BW AgentMob 62.54% 1.16 6.02k 0.57
YJMob100K AgentMove – – 1.84k 1.53
YJMob100K AgentMob 12.74% 2.66 12.96k 0.77
Shanghai ISP LLM Urban Res. – – 81.40k 68.77
Shanghai ISP AgentMob 0.00% 1.00 4.82k 2.87
Table 3: Efficiency statistics for GPT-5.4 runs. For
each dataset, the baseline is the strongest GPT-5.4 LLM
baseline in Table 2. Tools denote evidence-tool calls in
AgentMob excluding final answer submission; tokens
include prompts and responses; wall-clock time is measured in seconds per sample under the recorded worker
parallelism.
exit through the fast path, while ambiguous cases
receive additional tool calls and LLM reasoning.
On BW, 62.54% of samples are resolved by the
fast path, leading to only 1.16 evidence-tool calls
per sample and a lower wall-clock time than the
strongest LLM baseline. YJMob100K has weaker
routine regularity, so more samples enter the toolcalling mode and the average token usage increases.
Shanghai ISP has no fast-path exits because each
user contributes only one sparse first-test instance,
but AgentMob still reduces token usage by 94.1%
compared with the strongest GPT-5.4 baseline by
replacing long history-heavy prompts with compact
structured evidence.
These results show that AgentMob is not designed to minimize token usage uniformly across
all datasets. Instead, it allocates computation according to prediction difficulty. Even when some
non-fast-path samples require more tool reasoning, AgentMob achieves lower observed wall-clock
time on all three benchmarks under the recorded
worker parallelism. Appendix D.1 provides a fastpath example where a strong target-hour pattern
allows the agent to return a prediction without unnecessary tool loops.
4.3 Ablations
Figure 5 reports the effect of removing each evidence source from AgentMob. Overall, no single
tool dominates all metrics, which is expected because the tools target different types of uncertainty.
The full model achieves the most stable overall
performance, especially in rank-based accuracy
and spatial error. Some ablations can slightly improve Acc@1 on a specific dataset, but they usually
worsen MRR@5 or geographic distance, indicating
that the removed evidence helps prevent spatially
poor alternatives even when the exact top-1 label

Figure 5: Tool ablation results with GPT-5.4 on BW and
YJMob100K, reported before deterministic calibration
to isolate the effect of each evidence source. Bars show
Acc@1, and lines show geographic distance.
changes little.
Effect of the Stay–Move Estimator. Removing
the Stay–Move Estimator consistently weakens performance. On BW, Acc@1 drops from 67.57% to
66.41%, MRR@5 from 76.90% to 76.27%, and
distance increases from 2.39 km to 2.61 km. On
YJMob100K, Acc@1 decreases from 32.88% to
32.47%, with distance increasing from 4.25 km to
4.36 km. This shows that stay–move evidence is
useful for boundary cases where recent continuity
and historical departure patterns disagree. A paired
trace is provided in Appendix C.
Effect of the Historical Behavior Retriever.
The Historical Behavior Retriever provides
location-specific evidence such as visit frequency,
dwell time, and frequent next destinations. Removing it reduces BW Acc@1 from 67.57% to
66.67% and increases distance from 2.39 km to
2.47 km. On YJMob100K, Acc@1 slightly increases from 32.88% to 33.12%, but distance worsens from 4.25 km to 4.50 km. This suggests that
historical behavior evidence is especially useful for
spatial grounding: even when exact top-1 accuracy
changes little, it helps avoid farther off-target predictions in dense grid settings. Additional cases are
shown in Appendix C.
Effect of the Mobility Context Retriever. The
Mobility Context Retriever supplies recent trajectory context and same-time historical visitation
statistics. Removing it causes smaller but consistent degradation: BW Acc@1 decreases from
67.57% to 67.18%, and YJMob100K Acc@1 decreases from 32.88% to 32.69%, with distance also
increasing on both datasets. This indicates that
long-term regularity already solves many routine
cases, but recent context remains useful when the
user has just departed, returned, or stayed unusually
long. A paired trace is provided in Appendix C.

Effect of the Location Profiler. The Location
Profiler serves as an optional verification tool for
candidate locations. Removing it causes only a
small drop on BW, from 67.57% to 67.51% Acc@1,
but a clearer drop on YJMob100K, from 32.88% to
32.48%. This matches its role in ambiguous cases:
it helps check whether a candidate is spatially plausible and semantically consistent before the agent
changes its decision. A paired trace is provided in
Appendix C.
Sensitivity to the backbone LLM. AgentMob
also depends on the backbone model’s tool-use
ability. Compared with GPT-4.1-mini, Qwen3-8B
shows weaker multi-tool coordination: after entering tool-calling mode, 29.1% of cases fail to invoke
the Stay–Move Estimator as prescribed. Since reliable tool use requires instruction following, API
selection, and multi-step planning (Qin et al., 2023),
smaller or less aligned models may require stricter
tool-call validation, simplified orchestration, or distillation of tool-use behavior. This is consistent
with reported model-scale variation in Qwen3 instruction following (Yang et al., 2025).
5 Conclusion and Future Work
We presented AgentMob, a training-free LLMagent that formulates next-location prediction as
adaptive evidence-controlled decision making. Instead of relying on static prompt-only inference,
AgentMob allocates reasoning effort according to
prediction difficulty. Routine cases are resolved
through a fast path, while ambiguous cases trigger
selective tool use over recent context, historical
behavior, stay–move likelihood, and geographical
evidence. Experiments on different datasets show
AgentMob achieves strong training-free performance while producing auditable prediction traces.
Further analyses demonstrate that the LLM controller is most useful when deterministic mobility statistics are insufficient or conflicting. Future
work includes stronger uncertainty estimation, riskaware mobility planning, and broader multi-city
transfer.
6 Limitations
We discuss several scope boundaries of the current
study and how they motivate future extensions.
First, AgentMob relies on the backbone LLM’s
ability to follow tool-use instructions and coordinate multi-step reasoning. This is inherent to

tool-augmented agent frameworks rather than specific to mobility prediction. Our backbone analysis shows that stronger instruction-following models can better exploit the evidence-control protocol, while smaller models may require additional
safeguards. Future work could improve robustness
through stricter tool-call validation, simplified orchestration, or distillation of successful tool-use
traces into smaller models.
Second, our evaluation focuses on automatically
collected mobility trajectories, including continuous GPS datasets and a sparse mobile-network
benchmark. This choice matches our goal of studying next-location prediction under chronological
constraints from passively sensed trajectories. We
therefore do not directly evaluate on social checkin datasets such as Foursquare, where locations
are actively reported events and follow a different
observation mechanism from continuous sensing.
Extending AgentMob to bridge check-in data, continuous GPS traces, and mobile-network records is
an important direction for broader generalization.
Finally, the current toolbox is designed around
general evidence categories for mobility prediction:
recent context, historical behavior, stay–move likelihood, and geographical plausibility. Although
these tools are effective across the studied datasets,
their boundaries and invocation policy are manually specified. More systematic optimization of tool
design and orchestration could further improve performance, for example through automated prompt
tuning, learned tool-selection policies, or dynamic
tool composition. These extensions are complementary to our core contribution of formulating
mobility prediction as adaptive evidence-controlled
decision making.
7 Risk Statement
The current tool design is based on the capabilities
of existing LLMs and may become less effective
as LLM capabilities evolve.
References
Hugo Barbosa, Fernando B. de Lima-Neto, Alexandre
Evsukoff, and Ronaldo Menezes. 2020. The scales
of human mobility. Nature, 586(7831):402–407.
Blogwatcher, Inc. 2024. Blogwatcher. https://www.
blogwatcher.co.jp/. (Japanese only).
Christian Calderón, Pasqual Martí, Jaume Jordán, Javier
Palanca, and Vicente Julian. 2025. Cognitive agents

in urban mobility: Integrating llm reasoning into
multi-agent simulations. Sensors, 25(18):5688.
Jie Feng, Yuwei Du, and Yong Li. 2024. Limp: Large
language model enhanced intent-aware mobility prediction. arXiv preprint arXiv:2408.12832.
Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. 2025.
AgentMove: A large language model-based agentic framework for zero-shot next location prediction.
Jie Feng, Yong Li, Chao Zhang, Funing Sun, Fanchao
Meng, Ang Guo, and Depeng Jin. 2018. Deepmove:
Predicting human mobility with attentional recurrent
networks. In Proceedings of the 2018 world wide
web conference, pages 1459–1468.
Jie Feng, Mingyang Zhang, Huandong Wang, Zeyu
Yang, Chao Zhang, Yong Li, and Depeng Jin. 2019.
DPLink: User identity linkage via deep neural network from heterogeneous mobility data. In Proceedings of the 2019 World Wide Web Conference, pages
459–469.
Sébastien Gambs, Marc-Olivier Killijian, and Miguel
Núñez del Prado Cortez. 2012. Next place prediction
using mobility markov chains. In Proceedings of the
First Workshop on Measurement, Privacy, and Mobility, MPM ’12, New York, NY, USA. Association
for Computing Machinery.
Mengkang Hu, Yuhang Zhou, Wendong Fan, Yuzhou
Nie, Bowei Xia, Tao Sun, Ziyu Ye, Zhaoxuan Jin,
Yingru Li, Qiguang Chen, and 1 others. 2025. Owl:
Optimized workforce learning for general multiagent assistance in real-world task automation. arXiv
preprint arXiv:2505.23885.
Chenlu Ju, Jiaxin Liu, Shobhit Sinha, Hao Xue, and
Flora Salim. 2025. TrajLLM: A modular LLMenhanced agent-based framework for realistic human
trajectory simulation.
Guohao Li and 1 others. 2023. Camel: Communicative agents for “mind” exploration of large language
model society. arXiv preprint arXiv:2303.17760.
Peibo Li, Maarten de Rijke, Hao Xue, Shuang Ao, Yang
Song, and Flora D. Salim. 2024a. Large language
models for next point-of-interest recommendation.
In Proceedings of the 47th International ACM SIGIR
Conference on Research and Development in Information Retrieval, SIGIR 2024, pages 1463–1472.
ACM.
Qiumeng Li, Chunhou Ji, and Xinyue Liu. 2025. From
narrative to action: A hierarchical llm-agent framework for human mobility generation. Preprint,
arXiv:2510.24802.
Siyu Li, Toan Tran, Haowen Lin, John Krumm, Cyrus
Shahabi, Lingyi Zhao, Khurram Shafique, and
Li Xiong. 2024b. Geo-llama: Leveraging llms for
human mobility trajectory generation with spatiotemporal constraints. arXiv preprint arXiv:2408.13918.

Zechen Li, Baiyu Chen, Hao Xue, and Flora D. Salim.
2026. Zara: Training-free motion time-series reasoning via evidence-grounded llm agents. arXiv preprint
arXiv:2508.04038.
Defu Lian, Yongji Wu, Yong Ge, Xing Xie, and Enhong
Chen. 2020. Geography-aware sequential location
recommendation. In Proceedings of the 26th ACM
SIGKDD international conference on knowledge discovery & data mining, pages 2009–2019.
Yuebing Liang, Yichao Liu, Xiaohan Wang, and
Zhan Zhao. 2024. Exploring large language models for human mobility prediction under public
events. Computers, Environment and Urban Systems,
112:102153.
Qi Liu, Can Li, and Wanjing Ma. 2025. Gatsim: Urban
mobility simulation with generative agents. arXiv
preprint arXiv:2506.23306.
Qiang Liu, Shu Wu, Liang Wang, and Tieniu Tan. 2016.
Predicting the next location: a recurrent model with
spatial and temporal contexts. In Proceedings of the
Thirtieth AAAI Conference on Artificial Intelligence,
AAAI’16, pages 194–200. AAAI Press.
Massimiliano Luca, Gianni Barlacchi, Bruno Lepri, and
Luca Pappalardo. 2021. A survey on deep learning for human mobility. ACM Computing Surveys,
55(1):1–44.
Yingtao Luo, Qiang Liu, and Zhaocheng Liu. 2021.
Stan: Spatio-temporal attention network for next location recommendation. In Proceedings of the web
conference 2021, pages 2177–2185.
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Karl
Cobbe, Liane Dao, Matthew Jones, Nicholas Kornis,
Vlad Malaya, Kathryn Millican, Pamela Mishkin, and
1 others. 2021. Webgpt: Browser-assisted questionanswering with human feedback. arXiv preprint
arXiv:2112.09332.
Nuria Oliver, Bruno Lepri, Harald Sterly, and 1 others.
2020. Mobile phone data for informing public health
actions across the COVID-19 pandemic life cycle.
Science Advances, 6(23):eabc0764.
OpenAI. 2025. Gpt-4.1-mini: A compact and efficient
large language model. https://openai.com/. Accessed: 2026-03-16.
OpenAI. 2026. Introducing GPT-5.4. https://
openai.com/index/introducing-gpt-5-4/. Accessed: 2026-05-24.
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, and
1 others. 2022. Training language models to follow
instructions with human feedback. arXiv preprint
arXiv:2203.02155.

Joon Sung Park, Carrie O’Brien, Carrie Jun Cai, Meredith Ringel Morris, Percy Liang, and Michael S
Bernstein. 2023. Generative agents: Interactive
simulacra of human behavior. arXiv preprint
arXiv:2304.03442.
Canwen Qin, Aston Zhang, Zhuosheng Chen, Heng Ji,
Xiang Ren, Yizhou Sun, and 1 others. 2023. Toolllm:
Facilitating large language models to master 16,000+
real-world apis. arXiv preprint arXiv:2307.16789.
Yanjun Qin, Yuchen Fang, Haiyong Luo, Fang Zhao,
and Chenxing Wang. 2022. Next point-of-interest
recommendation with auto-correlation enhanced
multi-modal transformer network. In Proceedings
of the 45th International ACM SIGIR Conference on
Research and Development in Information Retrieval,
pages 2612–2616.
Steffen Rendle, Christoph Freudenthaler, and Lars
Schmidt-Thieme. 2010. Factorizing personalized
markov chains for next-basket recommendation. In
Proceedings of the 19th international conference on
World wide web, pages 811–820.
Aymeric Roucher, Albert Villanova del Moral, Thomas
Wolf, Leandro von Werra, and Erik Kaunismäki.
2025. ‘smolagents‘: a smol library to build
great agentic systems. https://github.com/
huggingface/smolagents.
Tianao Sun, Ke Fu, Weiming Huang, Kai Zhao, Yongshun Gong, and Meng Chen. 2024. Going where, by
whom, and at what time: Next location prediction
considering user preference and temporal regularity. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
pages 2784–2793.
Y. Tang and 1 others. 2025. Agent-kb: Knowledge base
enhanced multi-agent collaboration for complex task
solving. arXiv preprint arXiv:2507.06229.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob
Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz
Kaiser, and Illia Polosukhin. 2017. Attention is all
you need. In Advances in Neural Information Processing Systems (NeurIPS), volume 30.
Chuyue Wang, Jie Feng, Yuxi Wu, Shenglin Yi, and
Hang Zhang. 2026. ARMove: Learning to predict
human mobility through agentic reasoning. Preprint,
arXiv:2604.17419.
Jiawei Wang, Renhe Jiang, Chuang Yang, Zengqing
Wu, Makoto Onizuka, Ryosuke Shibasaki, Noboru
Koshizuka, and Chuan Xiao. 2024a. Large language
models as urban residents: An llm agent framework
for personal mobility generation. Advances in Neural
Information Processing Systems, 37:124547–124574.
Xinglei Wang, Meng Fang, Zichao Zeng, and Tao
Cheng. 2023. Where would i go next? large language models as human mobility predictors. arXiv
preprint arXiv:2308.15197.

Xinglei Wang, Meng Fang, Zichao Zeng, and Tao
Cheng. 2024b. Where would i go next? large language models as human mobility predictors. arXiv
preprint arXiv:2308.15197.
Yu Wang, Tongya Zheng, Shunyu Liu, Zunlei Feng,
Kaixuan Chen, Yunzhi Hao, and Mingli Song. 2024c.
Spatiotemporal-augmented graph neural networks
for human mobility simulation. IEEE Transactions
on Knowledge and Data Engineering, 36(11):7074–
7086.
Jiaman Wu, Shangqing Cao, Giuseppe Perona, and
Marta C Gonzalez. 2024. Imitate the right data: Citywide mobility generation with graph learning. In
Proceedings of the 32nd ACM International Conference on Advances in Geographic Information Systems, pages 609–612.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran
Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang, Shaokun Zhang, Jiale Liu, and 1 others.
2023. Autogen: Enabling next-gen llm applications via multi-agent conversation. arXiv preprint
arXiv:2308.08155.
Takahiro Yabe, Kota Tsubouchi, Toru Shimizu, Yoshihide Sekimoto, Kaoru Sezaki, Esteban Moro, and
Alex Pentland. 2024. Yjmob100k: City-scale and
longitudinal dataset of anonymized human mobility
trajectories. Scientific Data, 11(1):397.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, and Others. 2025. Qwen3
technical report. Preprint, arXiv:2505.09388.
Peiyuan Zhang, Guangtao Zeng, Tianduo Wang, and
Wei Lu. 2024. Tinyllama: An open-source small
language model. Preprint, arXiv:2401.02385.
Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang,
Xiaolei Wang, Yupeng Hou, Yingqian Min, Beichen
Zhang, Junjie Zhang, Zican Dong, Yifan Du, Chen
Yang, Yushuo Chen, Zhipeng Chen, Jinhao Jiang,
Ruiyang Ren, Yifan Li, Xinyu Tang, Zikang Liu, and
3 others. 2026. A survey of large language models.
Preprint, arXiv:2303.18223.
Yu Zheng. 2015. Trajectory data mining: An overview.
ACM Transactions on Intelligent Systems and Technology, 6(3):1–41.
Yu Zheng, Licia Capra, Ouri Wolfson, and Hai Yang.
2014. Urban computing: concepts, methodologies,
and applications. ACM Transactions on Intelligent
Systems and Technology, 5(3):1–55.
Lin Zhong, Lingzhi Wang, Xu Yang, and Qing Liao.
2025. Comapoi: A collaborative multi-agent framework for next poi prediction bridging the gap between
trajectory and language. In Proceedings of the 48th
International ACM SIGIR Conference on Research
and Development in Information Retrieval, pages
1768–1778.

Toolbox
R MCeoo trnb ite ilev itxe ytr R H e is c t e o n ri t c T a r l a v je is c it t a o t r i y on Statistics
(TooTol oinlv Aogaecnttion) GIne Rfooe grt rmr a
ie
pav hteiioc rna l G
Ge
eo
o
g
gr
ra
a
p
p
h
h
i
i
c
c
a
a
l
l
D
De
is
s
t
c
a
r
n
ip
ce
tion co
N m
n
e o
t
e
e
r d e
xt ?
Yes
SEtsatyim-maotovre Probability of Movement No (LLTMoo Inl Afegreenntce)
H RBi ees tht r oaie rvi v cioe arr l Behavioral statistics on location c E o n n o t u e g xt h ? Yes
No Iteration: Maximally 10 No
Timestamp hi S s t t r o o r n ic g a l
User ID regularity? Yes
Predicted location
Figure 6: Part of predictions for a sample user. (a)
Ground truth (b) Our method (c-e) Baselines.
A Qualitative Trajectory Visualization
B Location Description prediction
Since raw GPS coordinates and anonymous cell
IDs carry no semantic information, we design a
description-prediction step that converts each spatial unit into a concise textual characterization, enabling the LLM to reason about locations based
on their functional roles. All descriptions are generated once with GPT-4o and shared across every
LLM-based method evaluated in this paper.
BW. Each polygon corresponds to a third-level
administrative unit and is identified by a hierarchical place name (prefecture / municipality / district,
e.g., To¯ kyo¯ -to, Itabashi-ku, Hasune). We retrieve
publicly available geographic information for each
place name and prompt GPT-4o to produce a onesentence functional summary. For example, the
polygon To¯kyo¯-to, Itabashi-ku, Hasune yields:
“It functions primarily as a quiet residential neighborhood, where the area is characterized by apartment complexes, small parks, and local convenience stores, with nearby transit access via Hasune Station on the Mita Line.”
YJMob100K. Cells are anonymized
500 m × 500 m grid squares with no place
names. We leverage the POI category vectors (85
categories) provided by the dataset authors (Yabe
et al., 2024), and prompt GPT-4o to summarize
each cell’s top POI categories and their relative
proportions into a one-sentence description. For
example, a cell whose top categories are Hair
Salon (8.3%), Transit Station (7.4%), and Hospital
(7.0%) yields:
“It functions primarily as a diverse mixed-use service area, where the mapped profile is led by many
hair salons alongside many transit stations and
many hospitals, with adjacent cells indicating a
more active, service-rich amenity landscape and
no single activity clearly dominating the amenity
mix.”

C Ablation Case Examples
Stay-move Estimator. For user
fef58e6c6288Bad60f5629111c489116 at
2023-06-16 07:00 in BW, the no-stay-move
ablation predicts 76620, while the full method
predicts the ground-truth location 17833. The
paired traces show why the Stay-move Estimator
matters.
No-stay-move ablation trace
“The user has stayed at 76620 for the
last five hours, transition continuation
from the current location strongly favors
remaining at 76620 (88.4%), and the top
composite score is also 76620. Although
the Friday 07:00 historical signal points
to 17833, it is based on only one prior
instance and is weaker than the strong
current stay/transition evidence.”
Full-method trace
“Average stay: 8.6h. Current stay:
5h (0.58x average). Typical departure
hours: 7:00. Current hour 7:00 matches
a typical departure hour. Transitions
at 07:00 from Location 76620: 17833:
64%; 76620 (stay): 24%.”
“Although 76620 is the top raw candidate,
multiple stronger move signals point to
17833: 07:00 is a typical departure hour
from 76620, hour-specific transitions
from 76620 go to 17833 64% vs only
24% stay, and the only past Friday 07:00
example is also 17833. These aligned
commute-time signals justify overriding
the rank-1 stay candidate.”
This case supports the aggregate ablation result:
without the Stay-move Estimator, the agent overweights recent continuity; with the estimator, it can
identify departure-boundary cases where the user
is likely to move despite several recent hours at the
same location.
Mobility Context Retriever. For user
ed1fedcdf0c95e6748f68ee552aba4d2 at
2023-05-25 07:00 in BW, the no-recent-trajectory
ablation predicts 35995, while the full method
predicts the ground-truth location 60203. The
paired traces show that recent context prevents the
agent from overreacting to a sparse weekday-hour
pattern.
No-recent-trajectory ablation trace

“Although the current-location stay signal is strong, the strongest Tier-1 evidence is the past same Thursday 07:00
example and the weekly 07:00 pattern,
both pointing to 35995. Because this
is a commute window and the dominant
day+hour location differs from the current location, I override the rank-1 candidate and predict 35995.”
Full-method trace
“Recent Trajectory (last 6): 2023-0525T01:00:00: ID 60203 ... 2023-0525T06:00:00: ID 60203. Last 4 hours:
ID 60203 → 60203 → 60203 → 60203
(stable).”
“Although past Thursday 07:00 examples
favor 35995, the user has been settled at
60203 for 7 hours, current stay matches
the historical average, and both overall
and 07:00-specific transitions strongly
favor remaining at 60203. Given the stable overnight trajectory and 78% selftransition at 07:00, staying at 60203 is
the most likely outcome.”
This case supports the ablation result: without recent trajectory, the agent follows the same weekdayhour memory; with the Mobility Context Retriever,
it sees that the user is in a stable local continuation
state.
Historical Behavior Retriever. For user
b1774dafe8Ba1caac3e7aeb1b2b001d4 at 202306-21 13:00 in BW, the no-retriever ablation
predicts 33524, while the full method predicts the
ground-truth location 96817. The paired traces
show that the Historical Behavior Retriever helps
the agent audit whether a sparse historical signal
corresponds to a truly visited location.
No-retriever ablation trace
“The strongest signal is the Wednesday
13:00 historical pattern, where ID 33524
accounts for 50.0% of past instances and
also receives the strongest initial support.
Current-location stay evidence is weak
with no transition or duration history for
96817, so the dominant same-day/hour
pattern should override staying nearby.”
Full-method trace

“Location Details: 96818. Visit frequency: 0.00% (0 visits).”
“The strong Wednesday 13:00 historical
signal points to 96818, but that location
is not in the candidate list and shows no
visit history in the details lookup. With
no transition data from 96817 and the
user only having stayed there 1 hour after local movement, I choose the only
plausible nearby visited continuation
among candidates: remaining at current
location 96817, though with low confidence.”
This case supports the ablation result: without the retriever, the agent follows a coarse sameday/hour pattern; with the retriever, it can check the
visitation evidence behind that pattern and avoid
trusting an unsupported historical candidate.
Location Profiler. For user
5c6fe37f6005d3aeb4e3062f44bb32d3 at
2023-06-01 12:00 in BW, the no-optional-tools
ablation predicts 55472, while the full method
predicts the ground-truth location 37601. The
paired traces show that the Location Profiler helps
the agent reject an unsupported historical override
before leaving a stable current location.
No-optional-tools ablation trace
“The user has been stationary at 37601
for 24 hours, but this far exceeds the historical average stay and matches typical departure timing, so move signals
are strong. Among plausible move destinations, 55472 has the highest composite score and is strongly supported
by hourly and overall visitation patterns,
while the Thursday-12:00 historical signal for 66619 is based on only one instance and is not in the candidate set.”
Full-method trace
“Location Details: 66619. Visit frequency: 0.00% (0 visits).”
“Despite the top composite score for
55472, the user has remained at 37601
for 24 hours with a settled pattern and
all recent hours unchanged. The strong
Thursday-12:00 signal points to 66619,
but that location has 0 recorded visits and is not a valid candidate, so

continuation/self-transition to 37601 is
the safest prediction.”
This case supports the ablation result: optional
profiling is not needed for every sample, but it helps
in ambiguous cases by checking whether a tempting alternative is supported by concrete locationlevel evidence.
D Inference Case Studies
D.1 Baseline-by-Dataset Comparison Cases
This section gives one representative comparison
for each dataset-baseline pair. Each case reports the
ground truth, AgentMob’s prediction, and the baseline’s top-ranked prediction, followed by a short
explanation of the decision difference.
BW–AgentMove.
Dataset: BW
Ground truth: 36166
Ours: correct
AgentMove: wrong (17844 ranked first)
Ours inference
The prediction is made directly through the fastpath mechanism. The temporal evidence shows
a perfectly repeated pattern: on Friday at 09:00,
the user was at location 36166 in 18 out of 18
historical instances. Since the day-hour pattern is
fully consistent, the model can confidently rely on
this structured temporal signal without invoking
additional tools.
AgentMove inference
The user’s most visited location is 17844 with
a high overall visit rate and a significant presence in their long-term history, indicating a strong
likelihood to return especially during weekday
mornings.
... 36166 ... is ranked third.
BW–LLM-Mob.
Dataset: BW
Ground truth: 84174
Ours: correct
LLM-Mob: wrong (60263 ranked first)
Ours inference
The candidate ranking step corrected the initial
prediction and selected 84174. Although several overnight locations were plausible, the final evidence-supported candidate was the groundtruth location.
LLM-Mob inference
LLM-Mob emphasized the Wednesday 01:00 historical pattern and the immediately preceding trajectory, ranking 60263 first because it appeared
to match overnight behavior. It treated 84174 as a
later early-morning location and ranked it below
the top candidates.

BW–LLM Urban Residents.
Dataset: BW
Ground truth: 4419
Ours: correct
LLM Urban Residents: wrong (76623 ranked
first)
Ours inference
AgentMob used the hour-specific transition evidence to move away from the initial candidate
and selected 4419. The decision follows the local
early-morning evidence rather than the broader
persona-level routine.
LLM Urban Residents inference
LLM Urban Residents emphasized a weekend overnight movement pattern and the user’s
broader activity persona, ranking 76623 first as a
likely early-morning return location. The groundtruth location 4419 was kept as a lower-ranked
recent stop.
YJMob100K–AgentMove.
Dataset: YJMob100K
Ground truth: (134,83)
Ours: correct
AgentMove: wrong ((155,106) ranked first)
Ours inference
The candidate ranking step selected (134,83) after comparing the immediate candidate evidence.
This prevents the prediction from collapsing to a
distant long-term anchor when the current sample
favors a different location.
AgentMove inference
AgentMove prioritized the user’s dominant longterm anchor (155,106), which accounts for a large
share of visits and has strong self-transition behavior. This broad routine signal outweighed the
sample-specific evidence for (134,83).
YJMob100K–LLM-Mob.
Dataset: YJMob100K
Ground truth: (107,75)
Ours: correct
LLM-Mob: wrong ((98,78) ranked first)
Ours inference
AgentMob corrected the initial nearby candidate
and selected (107,75). The final decision stays
within the current local movement corridor rather
than following a repeated afternoon pattern from
another grid cluster.
LLM-Mob inference
LLM-Mob emphasized a repeated historical pattern around (98,78), ranking that location first. It
considered the 107-cluster plausible but placed it
below the stronger routine signal.

YJMob100K–LLM Urban Residents.
Dataset: YJMob100K
Ground truth: (169,126)
Ours: correct
LLM Urban Residents: wrong ((138,89) ranked
first)
Ours inference
The candidate ranking step selected (169,126),
preserving the evidence for the current workrelated location rather than extrapolating from
the latest movement cluster.
LLM Urban Residents inference
LLM Urban Residents relied on the recent movement within the (138,88)–(139,88) cluster and a
factory-worker persona, ranking (138,89) first as
a likely continuation. The ground-truth location
was included only as a lower-ranked alternative.
Shanghai ISP–AgentMove.
Dataset: Shanghai ISP
Ground truth: (138,114)
Ours: correct
AgentMove: wrong ((129,121) ranked first)
Ours inference
AgentMob kept the base prediction (138,114), indicating that the available evidence did not justify
moving to a farther historical anchor in this sparse
first-test setting.
AgentMove inference
AgentMove emphasized the user’s overall preference for (129,121) and frequent transitions around
that area. This long-term anchor dominated its
prediction, even though the target remained at
(138,114).
Shanghai ISP–LLM-Mob.
Dataset: Shanghai ISP
Ground truth: (92,105)
Ours: correct
LLM-Mob: wrong ((71,91) ranked first)
Ours inference
AgentMob used hour-transition calibration to revise the base prediction from (71,91) to (92,105).
The final answer favors the target-time evidence
over a repeated but less reliable recent morning
pattern.
LLM-Mob inference
LLM-Mob ranked (71,91) first because the user
appeared there at 08:00 on two recent days. It still
ranked (92,105) second, but did not elevate it to
the final top-1 prediction.

Shanghai ISP–LLM Urban Residents.
Dataset: Shanghai ISP
Ground truth: (125,108)
Ours: correct
LLM Urban Residents: wrong ((126,107) ranked
first)
Ours inference
AgentMob used hour-transition calibration to select (125,108) instead of the neighboring morning
anchor (126,107). The correction is small spatially but changes the exact top-1 label.
LLM Urban Residents inference
LLM Urban Residents ranked (126,107) first because it was a regular 08:00 location across recent
similar days. It placed (125,108) second, showing
that the baseline identified the right local area but
missed the exact grid.
15
