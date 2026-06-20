---
telephone_index: 27
title: "CortexDebate"
category: 02_debate_consensus
venue: "arXiv"
year: 2025
doi: 
arxiv_id: 2507.03928
preferred_source_type: preprint_or_unresolved
publisher_url: https://arxiv.org/abs/2507.03928
quality_flags: []
---

# Citation Context

- Telephone index: 27
- Preferred source: arXiv
- DOI: none
- arXiv: 2507.03928
- PDF: `assets\papers\pdf\02_debate_consensus\27_cortexdebate.pdf`

## Extracted Abstract

Nowadays, single Large Language Model (LLM) struggles with critical issues such as hallucination and inadequate reasoning abilities. To mitigate these issues, Multi-Agent Debate (MAD) has emerged as an effective strategy, where LLM agents engage in in-depth debates with others on tasks. However, existing MAD methods face two major issues: (a) too lengthy input contexts, which causes LLM agents to get lost in plenty of input information and experiences performance drop; and (b) the overconfidence dilemma, where self-assured LLM agents dominate the debate, leading to low debating effectiveness. To address these limitations, we propose a novel MAD method called “CortexDebate”. Inspired by the human brain’s tendency to establish a sparse and dynamically optimized network among cortical areas governed by white matter, CortexDebate constructs a sparse debating graph among LLM agents, where each LLM agent only debates with the ones that are helpful to it. To optimize the graph, we propose a module named McKinseybased Debate Matter (MDM), which acts as an artificial analog to white matter. By integrating the McKinsey Trust Formula, a wellestablished measure of trustworthiness from sociology, MDM enables credible evaluations that guide graph optimization. The effectiveness of our CortexDebate has been well demonstrated by extensive experimental results across eight datasets from four task types.
Title: CortexDebate: Debating Sparsely and Equally for Multi-Agent Debate

Source PDF: D:\0-Research\5-Telephone\assets\papers\pdf\02_debate_consensus\27_cortexdebate.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-06-20T12:42:03+00:00
- page_count: 21
- status: ok
- text_char_count: 72582

Metadata:
- author: Yiliu Sun; Zicheng Zhao; Sheng Wan; Chen Gong
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Related Work (page 3)
- Preliminaries (page 3)
  - Problem Definition (page 3)
  - McKinsey Trust Formula (page 3)
- Methodology (page 4)
  - Phase 1: Initial Answer Generation (page 4)
  - Phase 2: Multi-round Debate (page 4)
  - Phase 3: Final Answer Generation (page 5)
- Experiments (page 6)
  - Experimental Setup (page 6)
  - Main Results (page 6)
  - Performance Investigation (page 8)
- Conclusion (page 9)
- Dataset Details (page 12)
- Supplementary Experimental Results (page 12)
- Additional Experiments (page 12)
- Performance Investigation (page 14)
  - Average-based Edge Pruning (page 14)
  - Text Similarity Calculation (page 14)
  - Confidence Recalibration (page 15)
- Introduction of Evaluation Strategies (page 15)
- Prompts in CortexDebate (page 15)
- Introduction of Baseline Methods (page 15)
- CortexDebate Algorithm (page 16)

Markdown Content:

CortexDebate: Debating Sparsely and Equally for Multi-Agent Debate
Yiliu Sun1, Zicheng Zhao1, Sheng Wan2*, Chen Gong3*
1School of Computer Science and Engineering, Nanjing University of Science and
Technology, Nanjing, China.
2College of Artificial Intelligence, Nanjing Agricultural University, Nanjing, China.
3School of Automation and Intelligent Sensing, Shanghai Jiao Tong University,
Shanghai, China.
Correspondence: wansheng315@hotmail.com; chen.gong@sjtu.edu.cn.

5202
luJ
5
]IA.sc[
1v82930.7052:viXra
Abstract
Nowadays, single Large Language Model
(LLM) struggles with critical issues such as hallucination and inadequate reasoning abilities.
To mitigate these issues, Multi-Agent Debate
(MAD) has emerged as an effective strategy,
where LLM agents engage in in-depth debates
with others on tasks. However, existing MAD
methods face two major issues: (a) too lengthy
input contexts, which causes LLM agents to
get lost in plenty of input information and experiences performance drop; and (b) the overconfidence dilemma, where self-assured LLM
agents dominate the debate, leading to low debating effectiveness. To address these limitations, we propose a novel MAD method called
“CortexDebate”. Inspired by the human brain’s
tendency to establish a sparse and dynamically
optimized network among cortical areas governed by white matter, CortexDebate constructs
a sparse debating graph among LLM agents,
where each LLM agent only debates with the
ones that are helpful to it. To optimize the
graph, we propose a module named McKinseybased Debate Matter (MDM), which acts as
an artificial analog to white matter. By integrating the McKinsey Trust Formula, a wellestablished measure of trustworthiness from
sociology, MDM enables credible evaluations
that guide graph optimization. The effectiveness of our CortexDebate has been well demonstrated by extensive experimental results across
eight datasets from four task types.
1 Introduction
Recently, inspired by human cooperation, many
multi-agent interaction methods (Wan et al., 2024;
Xu et al., 2023a; Tu et al., 2023; Hu et al., 2024)
have been proposed to further improve the reasoning results of LLMs. These methods aim to address
critical issues faced by single LLM agent, such as
hallucination and poor reasoning ability. Among
these methods, Multi-Agent Debate (MAD) (Zhang
et al., 2024a; Du et al., 2023) has emerged as one of

the most promising strategies, as it can effectively
improve the performance of LLM agents through
the debating process among them.
Although previous MAD methods have achieved
promising results, they still suffer from two major
shortcomings. As shown in Figure 1, firstly, in
these methods, each LLM agent is often required
to debate with all other LLM agents, which causes
its input context to expand significantly as the number of agents and debating rounds increase. Consequently, since single LLM agent usually struggles
to handle lengthy input contexts (Liu et al., 2024a;
Luo et al., 2024), it may get lost in the vast amount
of input information, leading to a significant performance drop. Secondly, prior MAD methods determine the debating influence of each LLM agent
simply according to its own confidence, which may
lead to the overconfident LLM agents gradually
dominating the entire debating process. As a result,
the potential useful information provided by other
“weak” LLM agents may be ignored. Such unequal
debate is harmful to debating effectiveness, as also
confirmed by (Xiong et al., 2023; Xu et al., 2023b).
Therefore, inspired by the human cognition theory (Thiebaut de Schotten and Forkel, 2022), this
paper proposes a new MAD approach named CortexDebate, which mimics the working mode of the
human brain cortex. As revealed by (Thiebaut de
Schotten and Forkel, 2022), given a problem, the
human brain tends to establish a dynamic and
sparse network among different cortical areas, and
this network is gradually optimized by a specialized module named white matter. During the optimization process, the white matter focuses more
on the influence between paired areas rather than
the performance of a single cortical area.
By treating LLM agents as cortical areas in human brain, our proposed CortexDebate establishes
a sparse and directed debating graph, where the
nodes represent participated LLM agents and the
edges carry information transmission between two

3 4 Task
8
7 2
5
Think it step by step
1 Provide your answe
6 and its explanation.
Input Context
1
W ex e p lc e o r m ti e s e to i n th e s u d c e c b i a n te c ! t Y ly o u a n ar d e p a e d r e s b u a a te s r i v w e i l t y h 2 1 ) C A o n n sw fid er e : n 2 c 3 e: 0.9
expressing your viewpoints. You will engage in 3 2) Answer: 25
d T i a s s c k u : s 2 si 7 o 4 n - s 2 w 0 i t × h 1 o 3 th - e r 5 s . + 2 × 8 = ( ) 4 3 ) C A o n n sw fid er e : n 2 ce 5 : 0.5
5 Confidence: 0.6
O U t s h in e g r L th L e M op a i g n e io n n t s s o c l a u r t e i f o u n l s ly : as additional advice, 6 Generate your answ
can you provide an updated answer? Examine 7
your solution.
<Output Format> 8 Sinc
Figure 1: Shortcomings of the existing MAD methods:
to LLM agents. They may get lost in the vast amou
Determining the debating impact of LLM agents simply
ones dominating the debate. This situation is harmful t
LLM agents. Each directed graph edge is assigned
a weight that reflects how much the performance
of the tail LLM agent is expected to be improved
by debating with the head LLM agent. Therefore,
each tail LLM agent will not debate with the head
LLM agents which do not help improve its performance. It means that the edges with small weights
in the debating graph will be removed, resulting
in a sparse graph. As a result, the length of context input to such tail LLM agent will also be reduced. To optimize the edge weights of the debating graph, akin to the white matter dynamically
governing the optimization of sparse graph among
different cortical areas in human brain, our CortexDebate introduces a module named McKinseybased Debate Matter (MDM) that serves as the
artificial white matter. To alleviate the overconfidence dilemma present in prior works, MDM considers both the performance of head LLM agent and
the performance improvement expectation of tail
LLM agent in deciding each edge weight. Specifically, MDM innovatively introduces McKinsey
Trust Formula (Lamarre et al., 2012) to calculate
edge weights, which has been widely used in sociology to evaluate the level of trustworthiness of a
person through four aspects, including credibility,
reliability, intimacy, and self-orientation. Among
them, the first two evaluate individual abilities,
while the last two evaluate the collaboration effectiveness with others. Therefore, this formula may
suppress overconfident LLM agents, and also balance individual competence with teamwork ability

at is the result of 274 - 20 × 13 - 5 + 2 × 8? 25
Answer: 23 Answer: 25 Answer: 25
Process: 2 × 8 =16, Process: 2 × 8 =16, Process: 20 × 13 =
20 × 13 =260, 274 20 × 13 =260, 274 260, 274 - 260 - 5 =
- 260 - 5 + 16 = 23 - 260 - 5 + 16 = 25 9, 9 + 2 × 8 = 25
Confidence: 0.9 Confidence: 0.5 Confidence: 0.6
Answer: 23 Answer: 23 Answer: 23
Process: 20 × 13 = Process: 23 is Process: 274 - 260
260, 2 × 8 = 16, right, with high - 5 + 16 = 14 - 5 +
274 - 260 - 5 + 16 confidence. 274 - 16 = 9 + 16 = 25
= 23. The answer 260 - 5 + 16 = 23, (not 23, I may
of the task is 23. not 25. make a mistake)
Confidence: 1.0 Confidence: 0.8 Confidence: 0.6
ee LLM agents reach a consensus, the final answer is 23.
Debating with all others causes lengthy contexts input
of input information and perform unsatisfactorily; (b)
ed on their self-confidence may lead to the overconfident
e debating performance.
of LLM agents in MAD.
The effectiveness of our CortexDebate has been
well confirmed by the experiments on diverse tasks,
including math, world knowledge question answering, reasoning, and long-context understanding.
For instance, when compared with the state-of-theart methods, in math task, CortexDebate increases
Result Accuracy (RA) by up to 9.00% on GSM-IC
dataset and 10.00% on MATH dataset, respectively.
In reasoning task, CortexDebate increases RA by
up to 9.00% on GPQA dataset and 12.33% on ARCC dataset, respectively. Besides, apart from achieving high performance, our CortexDebate significantly reduces the length of context input to each
LLM agent, with a maximum reduction of 70.79%.
The main contributions of this paper are summarized as follows:
1) We propose a new MAD method named CortexDebate, which can improve the performance of
LLM agents by establishing a sparse and dynamic
debating graph and reducing the burden of lengthy
input context during the debate.
2) We propose a new module named MDM,
which introduces McKinsey Trust Formula to evaluate both the confidence of each LLM agent and
the usefulness to its debating component, thereby
alleviating the overconfidence of LLM agents.
3) We conduct extensive experiments to show
that our proposed CortexDebate outperforms representative baseline methods across multiple tasks
such as math, world knowledge question answering, reasoning, and long-context understanding.

2 Related Work
In a MAD system, each LLM agent presents its
viewpoint and scrutinizes the viewpoints of other
LLM agents across multiple rounds of debate (Sun
et al., 2024a). In summary, the existing MAD methods can be categorized as two types, namely sequential debate and parallel debate.
Sequential Debate. In these methods (Hu et al.,
2025; Brown-Cohen et al., 2023; Michael et al.,
2023; Wang et al., 2025; He et al., 2024), LLM
agents generate their viewpoints in turn. Each LLM
agent can only obtain the viewpoints of its preceding LLM agents. For example, Liang et al. (2023)
require two LLMs to refute each other in turn. In
addition to debaters, Guan et al. (2025) add extra
roles, such as judge and critic. The judge speaks
before debaters to explain the task, and the critic
speaks last to summarize debates. However, in a
sequential debate system, each LLM agent must
wait for previous LLM agents to finish reasoning
before it starts. This makes debating time increase
linearly with the number of LLM agents, leading
to low efficiency which limits the scalability.
Parallel Debate. In these methods (Pham et al.,
2023; Yin et al., 2023; Chern et al., 2024; Khan
et al., 2024; Liang et al., 2024; Li et al., 2024a;
Hegazy, 2024; Zhang et al., 2024b), all LLM agents
simultaneously generate their viewpoints based on
the viewpoints of other LLM agents in the last
debating round. For example, Chan et al. (2023) require LLM agents to critique all answers generated
in the last debating round and update its answer
in each debating round simultaneously. In addition to the answers generated in the last round, Sun
et al. (2024b) also provide each LLM agent with
task-related information retrieved from the web.
Besides, some methods (Duan and Wang, 2024;
Yoffe et al., 2024) try to adjust the debating influence of each LLM agent to improve the debating
effectiveness. For example, Chen et al. (2023) require each LLM agent to generate the confidence
score for its own answer, and then inputs the score
to other LLM agents along with the answer.
Since sequential debate systems face the lowefficiency issue mentioned above, our proposed
CortexDebate follows the parallel debate framework. Compared with existing parallel debating
methods which require each LLM agent to debate
with all others in each round, our CortexDebate
dynamically decides the necessary debating agents
by establishing a sparse debating graph among all

involved LLM agents, so that the input context to
each agent can be shortened. This is also in contrary to (Liu et al., 2024b; Li et al., 2024b) in which
the debating opponents are fixed. Furthermore, different from prior methods which determine the
debating impact of each LLM agent simply based
on its own confidence, we introduce the McKinsey Trust Formula so that both the confidence of
each LLM agent and the usefulness to its debating
component can be evaluated.
3 Preliminaries
In this section, we provide the problem definition
for our CortexDebate, and introduce the McKinsey
Trust Formula which plays an important role in our
proposed CortexDebate.
3.1 Problem Definition
Our CortexDebate establishes a directed debating
graph among n LLM agents, G = (A, E), where
A = {A }n is the vertex set representing partici i=1
ipating LLM agents and E = {E }
i→j i,j∈[1,2,...,n]
is the directed edge set representing information
transmission. Here, each directed edge E is asi→j
signed a weight W that indicates the expected
i→j
improvement in the performance of agent A by
j
debating with A . All the weights {W } are
i i→j
dynamically optimized during the debate process.
Given a problem Q, the agents {A }n engage in
i i=1
D rounds of debate. In the d-th debate round, each
LLM agent A scrutinizes the outputs of the LLM
i
agents connected to it, and then generates its own
output Od along with a self-confidence score Hd.
i i
Afterwards, the final answer of this debate round,
i.e., F , is obtained by majority voting.
d
3.2 McKinsey Trust Formula
The McKinsey Trust Formula (Lamarre et al., 2012)
is widely used in sociology to evaluate the level of
trustworthiness of a person within a group. This
formula can be expressed as:
C × R × I
T = , (1)
S
where C, R, I, and S denote credibility, reliability, intimacy, and self-orientation, respectively.
Among them, credibility measures professional
competence, reliability measures the stability of
task performance, intimacy measures the relationship with the evaluated person, and self-orientation
measures the self-orientation level of the evaluated
person within a group.

Question: What is the
Phase 1: Initial Answe
Answer: 23
Process: 2 × 8 =16, 20
× 13 = 260 ...
Confidence: 0.9
Answer: 25
Process: 20 × 13 =
260, 274 - 260 = 14 ...
Confidence: 0.5
Answer: 25
Process: 20 × 13 =
260, 274 - 260 = 14 ...
Confidence: 0.7
Step
3:
Answer
Regeneration
McKinsey-based Debate Matter
Mc  K=ins  ey× Tr  us×t F  o÷rm  ula
1
W: 0
Step 1: Edge Weight Optimization
Step 2: Sparse Graph Establishment
<
≥
[0, 1] Fully-connected → 0/1 Sparse:
connect
disconnect
Phase 3: Final Answe
Input Context: not lengthy
Other LLM agent solutions:
Using they as additional advice, can you provide Majority Voting:
an updated answer? <Output Format>
Figure 2: Overview of our proposed CortexDebate, wh
and consists of three phases: (a) Initial Answer Genera
and its confidence score. (b) Multi-round Debate: Parti
debating graph which is dynamically optimized by MD
debates, the final answer is generated by majority votin
In our MDM module, we adapt these four factors
to the context of MAD. Specifically, for directed
edge E connecting agent A to A , credibility
i→j i j
evaluates the professional competence of A . Relii
ability is the average confidence score of A to its
i
own answers in history debates, which represents
the performance reliability on the current question.
Intimacy represents the average degree of difference in viewpoints between A and A in history
i j
debates, as the collision of different viewpoints can
enhance the debating effectiveness (Xiong et al.,
2023). Self-orientation represents the participation
level of A in the debate (a lower participation level
i
indicates higher self-orientation).
4 Methodology
In this section, we introduce the overall framework
of our CortexDebate. As shown in Figure 2 and Algorithm 1, CortexDebate operates in three phases,
including initial answer generation, multi-round
debate, and final answer generation. Unlike existing MAD methods that establish fully-connected
and fixed graphs among LLM agents, our CortexDebate establishes a sparse and dynamic graph,
where each LLM agent selectively debates with
those that can contribute to its improvement. Be-

t of 274 - 20 × 13 - 5 + 2 × 8? Correct Answer: 25
Invovled Agents: Large Language Models
eneration
wer: 25 Answer: 29
cess: 20 × 13 = Process: 2 + 8 =10, 20
, 2 × 8 = 16 ... × 13 = 260 ...
nfidence: 0.7 Confidence: 0.5
Phase 2: Multi-round Debate
er: 25 Answer: 23 Step 4: Debate Termination
ss: 20 × 13 = Process: 2 × 8 =16,
× 8 = 16 ... 20 × 13 = 260 ... Answer: 25 No consensus
dence: 0.9 Confidence: 0.3 23 25
er: 25 Answer: 25 Step 4: Debate Termination
ss: 20 × 13 = Process: 2 × 8 =16,
× 8 = 16 ... 20 × 13 = 260 ... Answer: 25
A consensus
dence: 0.9 Confidence: 0.6 other 25
neration
Therefore, the final answer to the task is 25.
Process: 20 × 13 = 260, 2 × 8 = 16, 274 - 260
= 14, 14 - 5 = 9, 9 + 16 = 25
=argm  ax  (   =  )

Step
1
Output Components:
1) Answer: a numerical number
2) Process: an answer explanation
3) Confidence: answer confidence [0, 1]
is inspired by the working mode of human brain cortex
: Each LLM agent generates an answer, an explanation,
ating LLM agents engage in debates guided by a sparse
module. (c) Final Answer Generation: After multi-round
sides, CortexDebate evaluates the performance of
LLM agents and their usefulness to their debating
components, enabling credible graph optimization.
4.1 Phase 1: Initial Answer Generation
When given a problem Q, CortexDebate allows
each LLM agent A to independently generate an
i
initial output O0 and a self-confidence score H0
i i
(see Appendix F for the specific prompt). To mitigate overconfidence, CortexDebate adopts a recalibration strategy, which has been proven to be
effective in prior works (Chen et al., 2023). Our
strategy can be expressed as:
 0.8, H0 ≥ 0.8
 i

0.6, 0.6 ≤ H0 < 0.8
H0 = i . (2)
i H0, 0.3 ≤ H0 < 0.6
  i i
0.3, H0 < 0.3
i
4.2 Phase 2: Multi-round Debate
CortexDebate then comes into a debate phase,
where the set of agents {A } engage in D rounds
i
of debate. In the d-th debating round, CortexDebate comprises four steps, including edge weight
optimization, sparse graph establishment, answer
regeneration, and debate termination.
Step 1: Edge Weight Optimization. As the

description of Equation (1), MDM calculates the
edge weights based on four aspects, including credibility, reliability, intimacy, and self-orientation.
Following the definition for each aspect in the context of MAD in Section 3.2, the specific calculation
of each aspect will be given next.
For E , since the scaling law for LLM
i→j
agents (Hoffmann et al., 2022) can evaluate abilities of one LLM agent, we use it to calculate credibility C , which can be expressed as:
d
406.4 410.7
L (N, M ) = + + 1.69, (3)
N 0.34 M 0.28
where N , M , and L denote the parameter number,
the token number of pre-training data, and the pretraining loss of one model, respectively. A smaller
loss value indicates better model abilities, and thus
C is expressed as:
d
1
C = . (4)
d
L (N, M )
For reliability R which represents the average
d
confidence score of A in its own answers in the
i
preceding d − 1 rounds, its calculation can be expressed as:
R × (d − 1) + Hd−1
R = d−1 i . (5)
d
d
For intimacy I , which represents the average
d
degree of difference in viewpoints between A and
i
A in the preceding d − 1 rounds, MDM first uses
j
cosine similarity to calculate the textual similarity
between Od−1 and Od−1. Subsequently, CortexDei j
bate calculates the average viewpoint similarity
between A and A in the preceding d − 1 rounds,
i j
i.e., Sim , as:
d
Sim ×(d−1)+cos(Od−1,Od−1)
d−1 i j
Sim = , (6)
d
d
where cos(a, b) calculates cosine similarity between a and b. Since I represents the average
d
degree of difference, it is calculated as:
I = 1 − Sim . (7)
d d
For self-orientation S , based on the fact that
d
less group participation indicates that one is more
selfish, the MDM module uses the number of times
that A has debated with other LLM agents in the
i
preceding d − 1 rounds, denoted as P , to indid
rectly reflect self-orientation. The calculation can
be expressed as:
S = (d − 1) × (n − 1) − P , (8)
d d
where (d − 1) × (n − 1) denotes the maximum
number of times that one LLM agent can debate
with others in the preceding d − 1 rounds.

Therefore, following Equation (1), the weight of
edge E can be calculated as:
i→j
C × R × I
W d = d d d . (9)
i→j S
d
Step 2: Sparse Graph Establishment. For A ,
j
it can debate with the other n − 1 LLM agents. In
other words, there are n−1 directed edges pointing
to it, with A as the tail node. CortexDebate deterj
mines the set of debating opponents for A accordj
(cid:110) (cid:111)n
ing to the weights of these edges W d .
i→j
i=1, i̸=j
Firstly, the average weight of these edges, i.e.,
d
W , is calculated as:
j
1
W d = (cid:80) W d . (10)
j n − 1 i(i̸=j) i→j
Secondly, the edges with weights below W d are
j
removed, resulting in a sparse debating graph. The
process can be expressed as:
(cid:40)
d
1, W ≥ W
W d = i→j j . (11)
i→j d
0, W < W
i→j j
Therefore, the debating opponents for A , denoted
j
as Deb , can be expressed as:
j
(cid:110) (cid:111)
Debd = A | W d = 1, i ̸= j . (12)
j i i→j
Step 3: Answer Regeneration. For LLM agent
A , it receives the answers of the LLM agents in
j
Debd, which are generated in the (d − 1)-th dej
bating round. Afterwards, A needs to read and
j
scrutinize these answers, and generate its new answer Od and self-confidence score Hd. The input
j j
prompt can be expressed as:
(cid:104) (cid:110) (cid:111)(cid:105)
P romptd = Ins, Q, Od−1 , (13)
j k
where Ins denotes the instruction that stimulates
(cid:110) (cid:111)
A to regenerate its answer and Od−1 denotes
j k
the set of answers that A receives. The specific
j
prompt is shown in Appendix F.
Step 4: Debate Termination. After all the LLM
agents have generated their answers, CortexDebate
checks whether all the LLM agents reach a consensus (i.e., all the LLM agents agree on the same
answer) or the debate reaches the maximum rounds.
If so, the whole debating process concludes immediately.
4.3 Phase 3: Final Answer Generation
Once the entire debating process concludes, CortexDebate generates the final answer to the question
by majority voting among all the answers generated
in the last debating round, which can be expressed

as:
(cid:88)
O = arg max 1 (O = o) , (14)
final i
o
i
where o denotes a distinct answer generated by any
of the LLM agents. If all the generated answers are
different after debates, we treat the final result as
incorrect. By excluding fallback strategies, we can
clearly attribute the observed performance solely
to the debate mechanism itself.
5 Experiments
This section introduces the experimental setup, experimental results, and analysis of our experiments.
5.1 Experimental Setup
In this part, we introduce the details of the experimental setup.
Tasks. In our experiments, we consider four
typical tasks, namely: (a) math task, (b) world
knowledge question answering task, (c) reasoning
task, and (d) long-context understanding task. For
the math task, we use GSM-IC (Shi et al., 2023)
and MATH (Hendrycks et al., 2021) datasets. For
the world knowledge question answering task, we
use MMLU (Hendrycks et al., 2020) and MMLUpro (Wang et al., 2024) datasets. For the reasoning
task, we use GPQA (Rein et al., 2023) and ARCC (Clark et al., 2018) dataset. For the long-context
understanding task, we use LongBench (Bai et al.,
2023) and SQuAD (Rajpurkar, 2016) datasets.
More details on the employed datasets for experiments can be found in Appendix A.
Evaluation Metrics. For LongBench dataset,
we follow (Bai et al., 2023) and utilize the MacroAverage (M-Avg), which calculates the average
score over major sub-task categories. For SQuAD
dataset, we follow (Rajpurkar, 2016) and utilize
the Exact Match (EM), which calculates the percentage of outputs containing correct answers. For
the remaining six datasets, we follow (Shi et al.,
2023; Hendrycks et al., 2021, 2020; Wang et al.,
2024; Rein et al., 2023; Clark et al., 2018; Sun
et al., 2025) and utilize the Result Accuracy (RA),
which calculates the percentage of correct results.
Baseline Methods. Our proposed CortexDebate
is compared with the three categories of methods:
1) No debate: Multi-agent Voting (MaV) (Wang
et al., 2022), 2) Full debate: Multi-LLM Debate
(MLD) (Du et al., 2023), RECONCILE (Chen et al.,
2023), ChatEval (Chan et al., 2023), and Peer Review Debate (PRD) (Xu et al., 2023b), 3) Part

debate: GroupDebate (GD) (Liu et al., 2024b) and
Neighbor Debate (ND) (Li et al., 2024b). Among
them, no debate methods are the multi-agent methods without using debating strategies, full debate
methods are the MAD methods where each LLM
agents are required to debate with all others, and
part debate methods are the MAD methods where
each LLM agents only debates with part of the others. Detailed introduction of these baseline methods can be found in Appendix G.
For fairness, the maximum number of debating
rounds is set to 5 for all debating methods.
Backbone Models. The backbone models involved in the debating system for our experiments
are Qwen-2.5-7B-Instruct-Turbo (Team, 2024),
Mistral-7B-Instruct (Jiang et al., 2023), Typhoon1.5-8B-Instruct (Pipatanakul et al., 2023), Llama3.1-8B-Instruct-Turbo (Dubey et al., 2024), and
Gemma-2-9B-Instruct (Yang et al., 2024). For simplicity, we refer to them as Qwen, Mistral, Typhoon, Llama, and Gemma, respectively.
Implementation Details. We follow prior
works (Du et al., 2023; Chen et al., 2023; Besta
et al., 2024) to experiment on a subset of 100 examples for each dataset. For each experiment, we
conduct three runs on the same examples with the
same setups and report average results along with
their variances. We also conduct large-scale experiments on the more challenging datasets from
each task (i.e. MATH, MMLU-pro, GPQA, and
LongBench) and observe similar results, which are
detailed in Appendix C.
5.2 Main Results
In this part, we present the experimental results and
detailed analysis to highlight the effectiveness of
our proposed CortexDebate.
CortexDebate outperforms baseline methods.
Table 1 reports the accuracy of our CortexDebate
and baseline methods on eight datasets. Compared with the baseline methods, our CortexDebate achieves the highest accuracy and performs
stably on all adopted datasets. Besides, we can
find that the effectiveness and stability of the full
debate methods (i.e., MLD, RECONCILE, ChatEval, and PRD) drops on complex reasoning and
long-context tasks (i.e., GPQA, LongBench, and
SQuAD). It is because the reasoning process increases with the complexity of the task, leading to
the lengthy context issue mentioned in Section 1.
However, our CortexDebate still performs well
and stably due to its sparse debating graph which

GSM-IC MATH MMLU MMLU-pro GPQA ARC-C LongBench SQuAD
Type Method
RA ↑ M-Avg ↑ EM ↑
No Debate MaV 70.33±1.56 46.00±2.67 69.33±0.22 46.00±4.67 27.33±2.89 76.00±0.67 45.11±1.09 85.33±1.56
MLD 72.67±0.22 47.33±0.89 71.33±1.56 47.33±0.89 28.33±2.89 79.33±0.22 48.87±2.21 86.33±0.22
Full Debate
RECONCILE 75.67±0.22 50.33±4.22 75.00±2.67 53.67±2.89 31.00±0.67 83.67±2.89 52.55±2.68 88.33±6.89
ChatEval 74.33±0.89 49.00±0.67 73.00±0.67 49.33±0.89 31.33±0.89 82.67±1.56 53.56±6.16 87.33±6.22
PRD 77.00±0.67 51.33±0.89 77.33±1.56 54.00±0.67 32.00±2.00 84.33±0.89 50.21±6.09 87.67±4.22
GD 76.00±2.67 49.67±1.56 74.00±2.67 51.67±0.89 32.67±0.22 82.00±2.00 55.97±0.59 90.33±0.89
Part Debate ND 73.67±1.56 49.00±0.67 71.67±2.89 48.67±1.56 32.33±1.56 81.33±2.89 54.55±6.18 88.33±1.56
Ours 79.33±0.22 56.00±0.67 82.33±0.22 59.33±0.22 36.33±1.56 88.33±0.89 60.31±0.32 93.33±0.89
Table 1: Comparison results on the four different types of tasks. The unit of all the results is “%”. The format of
the results is “(average result)±(variance)”. “↑” means that higher values are better. The best records under each
metric are highlighted in bold.
MaV MLD RECONCILE ChatEval PRD GD ND Ours
8000 80% 9000 60% 12000 84% 16000 70%
6000 75% 6750 55% 9000 78% 12000 60%
4000 70% 4500 50% 6000 72% 8000 50%
2000 65% 2250 45% 3000 66% 4000 40%
0 60% 0 40% 0 60% 0 30%
GSM-IC MATH MMLU MMLU-pro
20000 40% 12000 90% 800000 80% 25000 95%
15000 35% 9000 85% 600000 60% 18750 90%
10000 30% 6000 80% 400000 40% 12500 85%
5000 25% 3000 75% 200000 20% 6250 80%
0 20% 0 70% 0 0% 0 75%
GPQA ARC-C LongBench SQuAD
Figure 3: Comparison results of average length of context input to the LLM agents on eight datasets. We reflect the
length of one input context through its token number. In each combined chart, the left vertical axis (representing
token number) corresponds to the bar chart, while the right vertical axis (representing task accuracy) corresponds to
the line chart.
reduces input context length and MDM module on eight adopted datasets after each debating round,
which makes each LLM agent debate with those respectively. From Figure 4a, we have two importhat are helpful to it. tant observations: (a) As the debate proceeds, the
CortexDebate significantly reduces input con- performance of our CortexDebate continues to imtext length. For each adopted dataset, we calculate prove. (b) Compared with the baseline methods,
our CortexDebate maintains superior performance
the average token number of context input to a sinand achieves the highest score of 69.41%. From
gle LLM agent in each method and present the reFigure 4b, our observations are likewise twofold:
sults in Figure 3. Compared with MaV, MAD meth-
(a) In the initial rounds, since CortexDebate encourods generally incur long context input to each LLM
ages the equal collision of different viewpoints, its
agent, indicating a significant challenge in reducing
consensus proportion is relatively low. However,
input context length while maintaining superior acas the debate proceeds, a high consensus proporcuracy in MAD methods. Our proposed CortexDetion is achieved. (b) Compared with other methbate takes a further step, as it achieves both shorter
ods, RECONCILE maintains the highest consensus
input context length and higher task performance
proportion while its score fluctuates as shown in
compared with other MAD baseline methods. The
Figure 4a. This is due to the overconfidence-caused
specific numerical values of the results shown in
unequal debate, where the debate is dominated by
Figure 3 are presented in Appendix B.
a few LLM agents and others tend to surrender.
CortexDebate debates effectively and equally.
Differently, our CortexDebate alleviates this issue
Engaging in more effective debates is what MAD
and maintains equally debates among LLM agents,
systems strive for. To study this, in Figures 4a
thereby achieving consistent growth in score and
and 4b, we plot the average scores and proportion
consensus proportion. The numerical results are
of examples achieving consensus on the answers

70
67
64
61
58
55
1 2 3 4 5
)%(
erocS
egarevA
MLD RECONCILE ChatEval PRD GD ND Ours
Debate Round
(a) Average scores of our CortexDebate and baseline methods after each debating round.
100
90
80
70
60
50
40
1 2 3 4 5
)%(
susnesnoC
MLD RECONCILE ChatEval PRD GD ND Ours
Debate Round
(b) Proportion of examples achieving answer consensus.
Figure 4: Results of average task scores and consensus
proportions for MAD methods after each round.
Method Score ↑
Fully-connected Graph 60.49
+ MDM 63.76
Sparse Graph 62.72
+ Self-evaluation (RECONCILE) 62.13
+ Peer Evaluation (PRD) 66.71
+ MDM (w/o I and S in Equation (9)) 66.69
d d
+ MDM (Ours) 69.41
Table 2: Ablation study on our proposed CortexDebate.
“↑” means that higher values are better. The best record
is highlighted in bold.
presented in Appendix B.
5.3 Performance Investigation
In this section, we conduct in-depth investigation
on our CortexDebate to analyze its effectiveness.
For each method, we use its average score on eight
adopted datasets to represent its performance.
Each component of CortexDebate is indispensable. To show that every component of CortexDebate (i.e., sparse debating graph and MDM
module) is indispensable, we conduct an ablation
study. For the fully-connected graph, we follow
the basic MAD framework where each LLM agent
debates with all others. For the sparse graph, we
use different evaluation strategies to optimize the

Method (CortexDebate) DVC CVR CVR/DVC
without I and S factors 3.71 1.26 33.96
with I and S factors 8.44 4.83 64.92
Table 3: Comparison results of our CortexDebate
with and without considering intimacy (I) and selforientation (S) factors.
         
 / / 0  $ J H Q W  1 X P E H U
 G Q X R 5  H W D E H '
 
 
 
 
 
  
        
                        
    
                             
    
                      
            
    
                          
        
    
        
        
 
         
   
    
Figure 5: Task performance of CortexDebate under
different LLM agent numbers and debating rounds.
edge weights of the debating graph, including selfevaluation (Chen et al., 2023), peer evaluation (Xu
et al., 2023b), MDM (w/o I and S in Equad d
tion (9)), and MDM (see Appendix E for detailed
introduction). As shown in Table 2, compared with
“fully-connected graph + MDM”, “sparse graph +
MDM” increases the average score by 5.65%. It
is because sparse debating graph structure alleviates lengthy input context issue and allows LLM
agents to make full use of their input information.
For different optimization strategies, the average
task score of self-evaluation is only 62.13%. It is
due to the overconfidence dilemma mentioned in
Section 1. Peer evaluation and MDM (w/o I and
d
S in Equation (9)) alleviate this issue, achieving
d
better performance compared with self-evaluation.
Moreover, MDM further improves the task performance, since it considers both the performance of
each LLM agent and the usefulness to its debating components, thereby conducting more credible evaluations compared with Peer evaluation and
MDM (w/o I and S in Equation (9)) which only
d d
evaluate individual performance.
Considering cooperation performance among
agents is essential. On MATH dataset, we compare the average numbers of different viewpoint
collisions (DVC) and correct viewpoint revision
(CVR) per question of our CortexDebate with and
without using intimacy (I) and self-orientation (S)

FcG CortexDebate
Agent
RA ↑ Avg-DN ↓ RA ↑ Avg-DN ↓
Qwen 54.00 13.58 58.00 11.53
Mistral 49.00 13.58 56.00 6.24
Typhoon 47.00 13.58 53.00 8.83
Llama 51.00 13.58 56.00 11.37
Gemma 45.00 13.58 51.00 5.46
Table 4: Task performance of every participated LLM
agent under the fully-connected debating graph and our
proposed CortexDebate. “↑” means that higher values
are better, and “↓” means that lower values are better.
factors. As shown in Table 3, we can find that incorporating I and S increases both the frequency
and quality of viewpoint interactions. This confirms that considering interactions among agents
is essential for enhancing collective reasoning in
LLM-based systems.
CortexDebate excels in large-scale debates. To
explore the influence of LLM agent number and debating rounds on our CortexDebate, we evaluate the
task performance of CortexDebate under different
numbers of participating LLM agents and debating
rounds. We present the results in Figure 5. We
can see that as the number of LLM agents and the
debating rounds increase, the task performance of
our CortexDebate continues to improve. Moreover,
compared with debating rounds, the increase in the
number of LLM agents contributes more to the performance improvement of CortexDebate. These
results demonstrate the potential of CortexDebate
for application in large-scale debates.
CortexDebate retains helpful debates. To further show the effectiveness of the retained edges
and corresponding nodes in our CortexDebate, we
conduct a detailed analysis. On MATH dataset, we
calculate the average debating number (Avg-DN)
and RA of every participated LLM agent under
the fully-connected graph (FcG) and our proposed
debating graph. As shown in Table 4, our proposed CortexDebate reduces debates among the
LLM agents, while improving the performance of
every LLM agent. It suggests that our CortexDebate retains helpful debates while pruning harmful
ones.
6 Conclusion
In this paper, we propose a new MAD method
termed “CortexDebate” to improve the reasoning

abilities of multi-agent interaction systems. Specifically, our CortexDebate establishes a sparse debating graph among participating LLM agents, which
reduces input information burdens of LLM agents.
Besides, by integrating the McKinsey Trust Formula, our proposed MDM module conducts credible evaluations to gradually optimize the debating graph, making the debating process equal, indepth, and effective. Due to the above designs,
our method alleviates two major issues faced by
existing MAD systems (i.e., too lengthy input contexts and overconfidence-caused unequal debates),
and shows superior performance to various stateof-the-art MAD methods on various typical tasks.
In the future, we plan to continue exploring the
potential of CortexDebate in large-scale debates
and complex tasks (i.e., domain expert systems).
Limitations
Despite the impressive performance of our proposed CortexDebate, we acknowledge that it has
two main limitations. Firstly, as a multi-agent debate method, compared with single-agent methods,
it is inevitable that there will be a decrease in efficiency and an increase in cost when solving tasks.
Secondly, despite the success, the reasoning ability
of LLM agents remains an important factor that
limits the performance of CortexDebate. Although
our proposed CortexDebate improves the debate
strategy among LLM agents, mistakes may still
occur due to the poor reasoning ability of LLM
agents.
Acknowledgments
This research is supported by NSF of China (Nos:
62336003, 12371510) and NSF of Jiangsu Province
(No: BK20241469).
References
Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu,
Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao
Liu, Aohan Zeng, Lei Hou, et al. 2023. Longbench:
A bilingual, multitask benchmark for long context
understanding. In Annual Meeting of the Association
for Computational Linguistics.
Maciej Besta, Nils Blach, Ales Kubicek, Robert Gerstenberger, Michal Podstawski, Lukas Gianinazzi,
Joanna Gajda, Tomasz Lehmann, Hubert Niewiadomski, Piotr Nyczyk, et al. 2024. Graph of thoughts:
Solving elaborate problems with large language models. In AAAI Conference on Artificial Intelligence.

Jonah Brown-Cohen, Geoffrey Irving, and Georgios Piliouras. 2023. Scalable ai safety via doubly-efficient
debate. In International Conference on Machine
Learning.
Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu,
Wei Xue, Shanghang Zhang, Jie Fu, and Zhiyuan
Liu. 2023. Chateval: Towards better llm-based evaluators through multi-agent debate. In International
Conference on Learning Representations.
Justin Chih-Yao Chen, Swarnadeep Saha, and Mohit
Bansal. 2023. Reconcile: Round-table conference
improves reasoning via consensus among diverse
llms. arXiv preprint arXiv:2309.13007.
Steffi Chern, Ethan Chern, Graham Neubig, and Pengfei
Liu. 2024. Can large language models be trusted
for evaluation? scalable meta-evaluation of llms
as evaluators via agent debate. arXiv preprint
arXiv:2401.16788.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018. Think you have solved question answering? try arc, the ai2 reasoning challenge. arXiv
preprint arXiv:1803.05457.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, et al. 2021. Training verifiers to solve math
word problems. arXiv preprint arXiv:2110.14168.
Yilun Du, Shuang Li, Antonio Torralba, Joshua B Tenenbaum, and Igor Mordatch. 2023. Improving factuality and reasoning in language models through multiagent debate. In International Conference on Machine
Learning.
Zhihua Duan and Jialin Wang. 2024. Enhancing multiagent consensus through third-party llm integration: Analyzing uncertainty and mitigating hallucinations in large language models. arXiv preprint
arXiv:2411.16189.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, et al. 2024. The llama 3 herd of models. arXiv
preprint arXiv:2407.21783.
Yong Guan, Hao Peng, Lei Hou, and Juanzi Li. 2025.
Mmd-ere: Multi-agent multi-sided debate for event
relation extraction. In Proceedings of the 31st International Conference on Computational Linguistics.
Zhitao He, Pengfei Cao, Chenhao Wang, Zhuoran Jin,
Yubo Chen, Jiexin Xu, Huaijun Li, Kang Liu, and Jun
Zhao. 2024. Agentscourt: Building judicial decisionmaking agents with court debate simulation and legal
knowledge augmentation. In Findings of the Association for Computational Linguistics: EMNLP 2024.
Mahmood Hegazy. 2024. Diversity of thought elicits
stronger reasoning capabilities in multi-agent debate
frameworks. arXiv preprint arXiv:2410.12853.

Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language understanding. In International Conference on Learning
Representations.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and
Jacob Steinhardt. 2021. Measuring mathematical
problem solving with the math dataset. Advances in
Neural Information Processing Systems.
Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch,
Elena Buchatskaya, Trevor Cai, Eliza Rutherford,
Diego de Las Casas, Lisa Anne Hendricks, Johannes
Welbl, Aidan Clark, et al. 2022. Training computeoptimal large language models. Advances in Neural
Information Processing Systems.
Qitian Jason Hu, Jacob Bieker, Xiuyu Li, Nan Jiang,
Benjamin Keigwin, Gaurav Ranganath, Kurt Keutzer,
and Shriyash Kaustubh Upadhyay. 2024. Routerbench: A benchmark for multi-llm routing system.
arXiv preprint arXiv:2403.12031.
Zhe Hu, Hou Pong Chan, Jing Li, and Yu Yin.
2025. Debate-to-write: A persona-driven multi-agent
framework for diverse argument generation. In International Conference on Computational Linguistics.
Albert Q Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guillaume Lample, Lucile Saulnier, et al. 2023. Mistral
7b. arXiv preprint arXiv:2310.06825.
Akbir Khan, John Hughes, Dan Valentine, Laura
Ruis, Kshitij Sachan, Ansh Radhakrishnan, Edward
Grefenstette, Samuel R Bowman, Tim Rocktäschel,
and Ethan Perez. 2024. Debating with more persuasive llms leads to more truthful answers. In International Conference on Machine Learning.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yutaka Matsuo, and Yusuke Iwasawa. 2022. Large language models are zero-shot reasoners. Advances in
Neural Information Processing Systems.
Eric Lamarre, T Mansour, and J Tetrault. 2012. Mckinsey on cooperatives.
Renhao Li, Minghuan Tan, Derek F Wong, and Min
Yang. 2024a. Coevol: Constructing better responses
for instruction finetuning through multi-agent cooperation. In Conference on Empirical Methods in
Natural Language Processing.
Yunxuan Li, Yibing Du, Jiageng Zhang, Le Hou, Peter Grabowski, Yeqing Li, and Eugene Ie. 2024b.
Improving multi-agent debate with sparse communication topology. In Findings of the Association for
Computational Linguistics: EMNLP 2024.
Jingcong Liang, Rong Ye, Meng Han, Ruofei Lai, Xinyu
Zhang, Xuanjing Huang, and Zhongyu Wei. 2024.

Debatrix: Multi-dimensinal debate judge with iterative chronological analysis based on llm. In Findings of the Association for Computational Linguistics:
ACL 2024.
Tian Liang, Zhiwei He, Wenxiang Jiao, Xing Wang,
Yan Wang, Rui Wang, Yujiu Yang, Zhaopeng Tu, and
Shuming Shi. 2023. Encouraging divergent thinking in large language models through multi-agent
debate. In Annual Meeting Of The Association For
Computational Linguistics.
Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy
Liang. 2024a. Lost in the middle: How language
models use long contexts. Transactions of the Association for Computational Linguistics, 12:157–173.
Tongxuan Liu, Xingyu Wang, Weizhe Huang, Wenjiang
Xu, Yuting Zeng, Lei Jiang, Hailong Yang, and Jing
Li. 2024b. Groupdebate: Enhancing the efficiency
of multi-agent debate using group discussion. arXiv
preprint arXiv:2409.14051.
Linhao Luo, Zicheng Zhao, Chen Gong, Gholamreza Haffari, and Shirui Pan. 2024. Graphconstrained reasoning: Faithful reasoning on knowledge graphs with large language models. arXiv
preprint arXiv:2410.13080.
Julian Michael, Salsabila Mahdi, David Rein, Jackson Petty, Julien Dirani, Vishakh Padmakumar, and
Samuel R Bowman. 2023. Debate helps supervise
unreliable experts. arXiv preprint arXiv:2311.08702.
Chau Pham, Boyi Liu, Yingxiang Yang, Zhengyu Chen,
Tianyi Liu, Jianbo Yuan, Bryan A Plummer, Zhaoran
Wang, and Hongxia Yang. 2023. Let models speak
ciphers: Multiagent debate through embeddings. In
International Conference on Learning Representations.
Kunat Pipatanakul, Phatrasek Jirabovonvisut, Potsawee
Manakul, Sittipong Sripaisarnmongkol, Ruangsak
Patomwong, Pathomporn Chokchainant, and Kasima
Tharnpipitchai. 2023. Typhoon: Thai large language
models. arXiv preprint arXiv:2312.13951.
P Rajpurkar. 2016. Squad: 100,000+ questions for
machine comprehension of text. In Conference on
Empirical Methods in Natural Language Processing.
David Rein, Betty Li Hou, Asa Cooper Stickland, Jackson Petty, Richard Yuanzhe Pang, Julien Dirani, Julian Michael, and Samuel R Bowman. 2023. Gpqa: A
graduate-level google-proof q&a benchmark. arXiv
preprint arXiv:2311.12022.
Freda Shi, Xinyun Chen, Kanishka Misra, Nathan
Scales, David Dohan, Ed H Chi, Nathanael Schärli,
and Denny Zhou. 2023. Large language models can
be easily distracted by irrelevant context. In International Conference on Machine Learning.

Qiushi Sun, Zhangyue Yin, Xiang Li, Zhiyong Wu,
Xipeng Qiu, and Lingpeng Kong. 2024a. Corex:
Pushing the boundaries of complex reasoning
through multi-model collaboration. In ICLR 2024
Workshop on Large Language Model (LLM) Agents.
Xiaoxi Sun, Jinpeng Li, Yan Zhong, Dongyan Zhao,
and Rui Yan. 2024b. Towards detecting llms hallucination via markov chain-based multi-agent debate
framework. arXiv preprint arXiv:2406.03075.
Yiliu Sun, Yanfang Zhang, Zicheng Zhao, Sheng Wan,
Dacheng Tao, and Chen Gong. 2025. Fast-slowthinking: Complex task solving with large language
models. arXiv preprint arXiv:2504.08690.
Qwen Team. 2024. Qwen2.5: A party of foundation
models.
Michel Thiebaut de Schotten and Stephanie J Forkel.
2022. The emergent properties of the connected
brain. Science, 378(6619):505–510.
Lifu Tu, Semih Yavuz, Jin Qu, Jiacheng Xu, Rui Meng,
Caiming Xiong, and Yingbo Zhou. 2023. Unlocking
anticipatory text generation: A constrained approach
for faithful decoding with large language models. In
Conference on Empirical Methods in Natural Language Processing.
Fanqi Wan, Longguang Zhong, Ziyi Yang, Ruijun Chen, and Xiaojun Quan. 2024. Fusechat:
Knowledge fusion of chat models. arXiv preprint
arXiv:2408.07990.
Haotian Wang, Xiyuan Du, Weijiang Yu, Qianglong
Chen, Kun Zhu, Zheng Chu, Lian Yan, and Yi Guan.
2025. Learning to break: Knowledge-enhanced reasoning in multi-agent debate system. Neurocomputing, 618:129063.
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le,
Ed H Chi, Sharan Narang, Aakanksha Chowdhery,
and Denny Zhou. 2022. Self-consistency improves
chain of thought reasoning in language models. In
International Conference on Learning Representations.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni,
Abhranil Chandra, Shiguang Guo, Weiming Ren,
Aaran Arulraj, Xuan He, Ziyan Jiang, et al. 2024.
Mmlu-pro: A more robust and challenging multi-task
language understanding benchmark. Advances in
Neural Information Processing Systems.
Kai Xiong, Xiao Ding, Yixin Cao, Ting Liu, and Bing
Qin. 2023. Examining inter-consistency of large language models collaboration: An in-depth analysis via
debate. In Findings of the Association for Computational Linguistics: EMNLP 2023.
Fangyuan Xu, Weijia Shi, and Eunsol Choi. 2023a. Recomp: Improving retrieval-augmented lms with compression and selective augmentation. In International
Conference on Learning Representations.

Zhenran Xu, Senbao Shi, Baotian Hu, Jindi Yu, Dongfang Li, Min Zhang, and Yuxiang Wu. 2023b. Towards reasoning in large language models via multiagent peer review collaboration. arXiv preprint
arXiv:2311.08152.
Ziyi Yang, Fanqi Wan, Longguang Zhong, Tianyuan
Shi, and Xiaojun Quan. 2024. Weighted-reward preference optimization for implicit model fusion. arXiv
preprint arXiv:2412.03187.
Zhangyue Yin, Qiushi Sun, Cheng Chang, Qipeng
Guo, Junqi Dai, Xuanjing Huang, and Xipeng Qiu.
2023. Exchange-of-thought: Enhancing large language model capabilities through cross-model communication. In Conference on Empirical Methods in
Natural Language Processing.
Luke Yoffe, Alfonso Amayuelas, and William Yang
Wang. 2024. Debunc: mitigating hallucinations in large language model agent communication with uncertainty estimations. arXiv preprint
arXiv:2407.06426.
Jintian Zhang, Xin Xu, Ningyu Zhang, Ruibo Liu,
Bryan Hooi, and Shumin Deng. 2024a. Exploring
collaboration mechanisms for llm agents: A social
psychology view. In ICLR 2024 Workshop on Large
Language Model (LLM) Agents.
Mingqing Zhang, Haisong Gong, Qiang Liu, Shu Wu,
and Liang Wang. 2024b. Breaking event rumor detection via stance-separated multi-agent debate. arXiv
preprint arXiv:2412.04859.
A Dataset Details
The eight datasets used in our experiments are classic datasets that are widely employed to evaluate
the performance of agent-based methods. Here, we
provide an introduction to the eight datasets used
in our experiments.
GSM-IC. It is a grade-school math problem
dataset derived from GSM8K (Cobbe et al., 2021).
For each problem in GSM8K, GSM-IC keeps the
base problem description and adds to it one irrelevant sentence that does not affect the solution of
the problem.
MATH. It is a math dataset containing challenging competition mathematics problems. Each of
them has a full step-by-step solution.
MMLU. It contains 57 types of multiple-choice
problems, such as elementary mathematics, US
history, computer science, and so on. To acquire
high performance on the MMLU datasset, models must possess extensive world knowledge and
strong problem-solving ability.
MMLU-pro. It contains questions sourced from
multiple origins, such as MMLU, TheoremQA, and

SciBench. Moreover, it expands the option number
of each problem from 4 to 10.
GPQA. It contains 448 graduate-level questionanswering problems, covering knowledge in various fields such as biology, physics, and chemistry.
ARC-C. It contains complex questions on natural science, presented in the form of multiplechoice options.
LongBench. It is a dataset designed to evaluate
the long-context understanding capabilities of models. It encompasses six major categories of tasks,
including single-document QA, multi-document
QA, summarization, few-shot learning, code completion, and synthetic tasks.
SQuAD. It is a dataset used to evaluate the reading comprehension ability of models. The dataset
requires models to answer different questions from
given long texts.
B Supplementary Experimental Results
In this section, we provide the experimental result
data involved in the charts which are presented in
Sections 5.2 and 5.3.
For Figure 3, we provide the data in Table 7.
Compared with the full debate methods (i.e., MLD,
RECONCILE, ChatEval, and MPRC), our CortexDebate significantly reduces the length of the
contextual input for each LLM agent, with a maximum reduction of 70.79%. Moreover, compared
with the part debate methods (i.e., GD and ND), our
CortexDebate can reduce the input context length
by at least 17.62%.
For Figure 4, we provide the data in Table 8. After each debating round, our CortexDebate achieves
the highest average score compared with the baseline methods, with a global maximal score of
69.41% (67.30% for the baseline methods).
C Additional Experiments
In this section, we present large-scale experiments
of our CortexDebate and baseline methods to further demonstrate the superiority of CortexDebate.
Experimental Setup. For each task (i.e., math,
world knowledge question answering, reasoning,
and long-context understanding), we conduct experiments on the more challenging one of the two
datasets (i.e., MATH, MMLU-pro, GPQA, and
LongBench). For each adopted dataset, we experiment on a subset of 1000 examples. Besides,
the backbone models and evaluation metrics used

MATH
Type Method
No Debate MaV 47.40
MLD 49.20
RECONCILE 50.70
Full Debate
ChatEval 49.90
PRD 51.20
GD 50.30
Part Debate ND 49.50
Ours 56.30
Table 5: Comparison results on the four datasets. The
are better. The best records under each metric are highl
Type Method MATH
No Debate MaV 1316.85
MLD 6408.39
RECONCILE 6723.84
Full Debate
ChatEval 5571.07
PRD 8849.70
GD 4217.23
Part Debate ND 4175.27
Ours 3355.20
Table 6: Comparison results of average input context le
token number of input context. The results in gray ind
their corresponding method (MaV) is not MAD method.
are highlighted in bold.
Type Method GSM-IC MATH MMLU
No Debate MaV 1161.18 1277.73 1670.48
MLD 6287.39 6397.97 7905.84
RECONCILE 6196.09 6574.29 8409.61
Full Debate
ChatEval 5600.22 5394.71 7325.20
PRD 7651.62 8652.23 11691.8
GD 3828.95 4139.04 6156.13
Part Debate ND 3149.04 4207.18 4740.46
Ours 2413.35 3262.79 3727.65
Table 7: Comparison results of average input context l
token number of input context. The results in gray ind
their corresponding method (MaV) is not MAD method.
are highlighted in bold.

MMLU-pro GPQA LongBench
RA ↑ M-Avg ↑
46.30 29.10 43.35
48.40 30.60 46.26
53.10 30.80 48.33
49.30 31.10 51.23
54.20 32.40 47.67
51.30 34.20 54.58
49.10 32.80 54.14
58.90 36.60 59.63
t of all the results is “%”. “↑” means that higher values
ed in bold.
MMLU-pro GPQA LongBench
2268.10 2567.90 125034.39
11412.75 12868.37 585365.43
11334.12 14061.76 605688.14
9219.88 12369.62 553114.66
14946.31 18851.29 815449.95
7265.23 8817.46 447987.68
6673.75 7971.60 394905.47
6001.33 6503.76 321109.57
h on adopted datasets. Each result represents the average
e that they are not included in result comparison, since
e best records among the MAD methods on each dataset
MMLU-pro GPQA ARC-C LongBench SQuAD
2144.39 2653.92 1582.67 105020.51 4724.95
11213.07 12947.80 7605.01 525177.19 23185.66
11260.15 14107.64 8770.85 525765.69 24112.64
9160.49 12252.56 6918.96 473070.19 20781.94
14829.46 18837.51 11232.72 735370.99 33350.02
7159.45 8906.51 5381.72 367835.88 16073.50
6647.27 8016.54 4311.26 314993.80 14218.49
5897.94 6340.26 3280.71 230956.05 11965.81
th on eight datasets. Each result represents the average
e that they are not included in result comparison, since
e best records among the MAD methods on each dataset

Score (%
Type Method
1 2 3
MLD 55.99 58.76 60.32
RECONCILE 58.95 60.71 67.30
Full Debate
ChatEval 58.13 63.86 61.74
PRD 60.22 65.05 66.66
GD 56.94 59.04 64.19
Part Debate ND 56.21 58.65 57.52
Ours 60.31 65.65 67.63
Table 8: Experimental results of average task scores and
round.
Edge Pruning Strategy RA ↑
Top-3 54.00
Bot-3 56.00
AMT 52.00
AAT (Ours) 57.00
Table 9: Task performance of CortexDebate with different edge pruning strategies. “↑” means that higher
values are better. The best record is highlighted in bold.
in the experiments are the same as mentioned in
Section 5.1.
Results. The experimental results are presented
in Table 5. Consistent with the experimental results
reported in Table 1, our proposed CortexDebate
achieves the best performance on all the datasets
compared with baseline methods. For instance,
CortexDebate achieves a maximal RA of 56.30%
on MATH dataset, 58.90% on MMLU-pro dataset,
36.60% on GPQA dataset, and 59.63% on LongBench dataset, respectively. Moreover, for each
method, we calculate the average token numbers
of the contexts input to one LLM agent on each
dataset and present the results in Table 6. Compared with the full debate methods (i.e., MLD,
RECONCILE, ChatEval, and MPRC), our CortexDebate significantly reduces the length of the
contextual input for each LLM agent, with a maximum reduction of 65.50%. Moreover, compared
with the part debate methods (i.e., GD and ND), our
CortexDebate can reduce the input context length
by at least 17.40%.
D Performance Investigation
In this section, we present additional in-depth investigations on our CortexDebate to further analyze

Consensus (%)
4 5 1 2 3 4 5
.63 59.82 52.88 66.88 82.00 87.88 86.50
.64 63.65 73.63 79.25 94.00 95.75 98.63
.01 62.32 55.75 72.13 67.63 78.63 88.50
.50 64.11 64.50 72.75 79.50 86.38 87.88
.87 63.91 48.13 54.75 74.00 78.88 81.75
.65 62.19 43.38 56.63 66.13 73.00 77.75
.10 69.41 51.75 62.13 76.75 89.63 95.50
nsensus proportion for all the methods after each debate
Text Similarity Calculation M-Avg ↑
DeTS 57.57
±0.69
R1-P 56.91
±3.10
Ours 60.31
±0.32
Table 10: Task performance of CortexDebate with different calculation strategies of text similarity. The format of the results is “(average result)±(variance)”. “↑”
means that higher values are better. The best record is
highlighted in bold.
its effectiveness.
D.1 Average-based Edge Pruning
As present in Equation (11), our CortexDebate uses
the average value as the threshold to prune the
edges. To evaluate the effectiveness of adopting
the average-based threshold, we conduct experiments on MATH dataset. Specifically, we compare the strategy of debating with the agents above
the average threshold (AAT) with three alternatives, namely Top-3 (debating with the top three
agents), Bot-3 (excluding the bottom three agents),
and AMT (debating with agents above the median
threshold). As shown in Table 9, AAT achieves
superior performance than the others, which validates the effectiveness of the average-based edge
pruning.
D.2 Text Similarity Calculation
In the experiments, we use the text-embedding-3large model released by OpenAI as the embedding
model. For calculation of text similarity, we use
cosine similarity which is widely used due to its efficiency and robustness to varying input length, and
strong empirical performance. To confirm this, on
LongBench dataset, we compare our strategy with

Threshold Configurations Average Score ↑
w/o recalibration 68.62
[0.9, 0.7, 0.2] 68.96
[0.9, 0.6, 0.3] 69.03
[0.8, 0.6, 0.2] 69.15
[0.8, 0.5, 0.1] 68.84
[0.7, 0.5, 0.2] 68.72
[0.8, 0.6, 0.3] (Ours) 69.41
Table 11: Task performance of CortexDebate with different threshold configurations of the recalibration strategy. “↑” means that higher values are better. The best
record is highlighted in bold.
ag-nli-DeTS-sentence-similarity-v4 model (DeTS)
that is trained on six natural language inference
datasets and “DeepSeek R1 + prompt” (R1-P).
The average task scores and variances over three
runs are reported in Table 10. We can find that
our method outperforms the two baseline methods.
Moreover, we observe that large language models
tend to perform unstably when used for text similarity estimation, which is reflected by the higher
variance across different runs.
D.3 Confidence Recalibration
As present in Equation (2), our CortexDebate
adopts a recalibration strategy to mitigate overconfidence issue of LLM agents. Following the practice
of (Chen et al., 2023), we conduct experiments on
different combinations of thresholds. We present
the average scores on eight adopted datasets in Table 11. According to the results, this recalibration
strategy leads to the improved performance, and
the parameter setting in our paper leads to the best
performance. Moreover, our method is generally insensitive to different threshold configurations. This
demonstrates the effectiveness and robustness of
the proposed confidence recalibration strategy.
E Introduction of Evaluation Strategies
Here we introduce the details of the evaluation
strategies (i.e., self-evaluation, peer evaluation, part
MDM) mentioned in Section 5.3.
Self-evaluation. In this strategy, each LLM
agent is required to generate a confidence score for
its generated answer. Each LLM agent will only debate with the LLM agents whose confidence scores
are above the average of the entire graph.
Peer Evaluation. For each LLM agent, its
answer is scored by other LLM agents, and the final

score of the answer is the average of the received
scores. Each LLM agent will only debate with the
LLM agents whose scores are above the average of
the entire graph.
MDM (w/o I and S in Equation (9)). For
d d
McKinsey Trust Formula used in MDM module,
this strategy only considers the first two aspects
(i.e., credibility and reliability) which evaluate individual abilities, neglecting the last two aspects (i.e.,
intimacy and self-orientation) which evaluate the
debate effectiveness between two LLM agents.
F Prompts in CortexDebate
We provide the specific prompts of our proposed
CortexDebate in Table 12. For initial answer generation, CortexDebate follows (Kojima et al., 2022)
and prompts each LLM agent to solve the problem
step by step. For answer regeneration, the prompt
contains three parts: (a) An instruction that stimulates LLM agents to generate their new answers
and self-confidence scores after scrutinizing other
answers. (b) A description of the problem. (c)
Some answers generated by other LLM agents.
G Introduction of Baseline Methods
Here we introduce the details of the baseline methods (i.e., Multi-agent Voting, ChatEval, MultiLLM Debate, RECONCILE, Peer Review Debate,
GroupDebate, and Neighbor Debate) in our experiments.
Multi-agent Voting. This method adopts a majority voting strategy to aggregate responses from
multiple LLM agents. Specifically, each LLM
agent independently generates a response to the
given question. The final prediction is then determined through majority voting.
ChatEval. ChatEval uses an extra LLM agent
to summarize the debating results in each round of
debate. The specific prompt of debating summary
used in the experiments is shown in Figure 7. The
summary text generated in the current round of
debate will be input to each LLM agent as supplementary information in the next round of debate.
Multi-LLM Debate. Firstly, each LLM generates an answer to the question. Then, each LLM
reads and critiques the answers generated by other
LLM agents, and generates its new answer. This
step is repeated multiple times. After that, the final
answer is obtained through majority voting among
the answers generated by all the LLM agents in the
last round of debate. The specific prompt used in

Type
Question: {the descr
Please think it step
explanation for your
Also, evaluate how c
Initial Answer
Your confidence sco
Generation
The format of your a
Answer: (...)
Explanation: (
Confidence Sc
Question: {the descr
There are some answ
One LLM agent ans
One LLM agent ans
... ...
Answer Using these answers
Regeneration a new answer and an
Also, evaluate how c
Your confidence sco
The format of your a
Answer: (...)
Explanation: (
Confidence Sc
Table 12: Prompts of our proposed
the experiments is shown in Figure 6.
RECONCILE. Given a problem, each LLM
first generates an answer and its uncertainty for the
answer. Then all LLM agents enter a multi-round
debate. Each debating round consists of each LLM
generating a revised answer and its new uncertainty
based on the answers generated by all other LLM
agents from the previous round. After the multiround debate, RECONCILE obtains the final answer through majority voting. The specific prompt
used in the experiments is shown in Figure 8.
Peer Review Debate. Similar to RECONCILE,
this method also evaluates all the answers in each
round of debate. However, this method employs a
peer review strategy where the answer generated
by each LLM agent is evaluated by other LLM
agents. The specific prompt used in the experiments is shown in Figure 9.
GroupDebate. This method divides the LLM
agents into several debate groups, with each group
conducting internal debates. After the internal debates, the result of each debate group is summarized and placed into a shared pool. After that, each

Prompt
on of the question}
step and generate an answer and an
swer.
dent you are that your answer is correct.
hould between 0 and 1.
wer must be:
: (...)
on of the question}
generated by other LLM agents:
: {answer}
: {answer}
additional information, please generate
planation for your answer.
dent you are that your answer is correct.
hould between 0 and 1.
wer must be:
: (...)
rtexDebate used in the experiments.
group retrieves the debate summaries of all groups
from the pool, which serve as the input for all the
LLM agents in the next round. The specific prompt
used in the experiments is shown in Figure 10.
Neighbor Debate. In this method, LLMs only
debate with their neighbors. The specific prompt
used in the experiments is shown in Figure 11.
H CortexDebate Algorithm
In this section, we provide the detailed algorithm
of our proposed CortexDebate. As present in Algorithm 1, we strictly follow Sections 3 and 4, and
provide the whole execution process of our proposed CortexDebate.

Debating Prompt for Each LLM Agent
These are the solutions to the problem from other agents: [other answers]
Using the opinion of other LLM agents as additional advice, can you give an updated
response ...
Figure 6: Prompt of Multi-LLM Debate used in the experiments.
Debate Summary
[Question]
{source_text}
[The Start of Assistant 1's Answer]
{compared_text_one}
[The End of Assistant 1's Answer]
[The Start of Assistant 2's Answer]
{compared_text_two}
[The End of Assistant 2's Answer]
[The Start of Assistant 3's Answer]
{compared_text_one}
[The End of Assistant 3's Answer]
[The Start of Assistant 4's Answer]
{compared_text_one}
[The End of Assistant 4's Answer]
[System]
We would like to request your feedback on the performance of four Al assistants in
response to the user question displayed above.
Please consider the helpfulness, relevance, accuracy, and level of detail of their
responses.
Each assistant receives an overall score on a scale of 1 to 10, where a higher score
indicates better overall performance.
There are a few other referees assigned the same task, it's your responsibility to discuss
with them and think critically before you make your final judgment.
Here is your discussion history:
{chat_history}
{role_description}
Now it's your time to talk, please make your talk short and clear, {agent_name} !
Figure 7: Debating summary prompt of ChatEval used in the experiments.

Initial Answer Generation
{convincing_samples}
Q: {test_question}
Please answer the question with step-by-step reasoning.
Also, evaluate your confidence level (between 0.0 and 1.0) to indicate the possibility of
your answer being right.
Debate
{convincing_samples}
{initial_prompt}
Carefully review the following solutions from other agents as additional information, and
provide your own answer and step-by-step reasoning to the question.
Clearly state which point of view you agree or disagree with and why.
There are {majority_num} agents think the answer is {majority_ans}.
One agent solution: {agent_reasoning} {agent_ans} {agent_confidence}
One agent solution: {agent_reasoning} {agent_ans} {agent_confidence}
There are {minority_num}agents think the answer is {minority_ans}.
One agent solution: {agent_reasoning} {agent_ans} {agent_confidence}
Figure 8: Prompt of RECONCILE used in the experiments.
Initial Answer Generation
Can you solve the following problem? {Question}
Explain your reasoning. Your final answer should be in the form \boxed{answer}, at the
end of your response.
Peer Review
Here is a solution from another agent: {Answer B}
Please examine this agent's reasoning process step by step and offer feedback on its
reasoning.
You can rate your confidence in your feedback on a scale from 1-10, where 10 indicates
the highest level of confidence.
Answer Revise
Here are the feedbacks for your solution from other agents:
One agent feedback: {Feedback B → A}
One agent feedback: {Feedback C → A}
One agent feedback: {Feedback D → A}
One agent feedback: {Feedback E → A}
Using other agents’ solutions and feedbacks as additional information, can you provide
your answer to the math problem?
The original math problem is {Question}
Your final answer should be a single numerical number, in the form \boxed{answer}, at
the end of your response.
Figure 9: Prompt of Peer Review Debate used in the experiments.

System
Welcome to the debate! You are a seasoned debater with expertise in succinctly and
persuasively expressing your viewpoints. You will be assigned to debate groups,
where you will engage in discussions with fellow participants. The outcomes of each
group's deliberations will be shared among all members. It is crucial for you to
leverage this information effectively in order to critically analyze the question at hand
and ultimately arrive at the correct answer: Best of luck!
Starting
Can you solve the following problem? <Problem>
Explain your reasoning. <Output format>.
Intra-group Debate
These are the recent opinions from other agents: <other agent responses>
Using the opinions carefully as additional advice, can you provide an updated answer?
Examine your solution and that other agents step by step. <Output format>.
Summary
These are the recent/updated opinions from all agents: <all agent responses>
Summarize these opinions carefully and completly in no more than 80 words.
Aggregate and put your final answers in parentheses at the end of your response.
Inter-group Debate
These are the recent opinions from all groups: Your group response:
<group summary>, Other group responses: <other group summary>.
Using the reasoning from all groups as additional advice, can you give an updated
answer? Examine your solution and that all groups step by step. <Output format>.
Figure 10: Prompt of GroupDebate Debate used in the experiments.

System
You are a helpful assistant. Your task is to assist in solving a problem by providing a
clear and detailed solution. Your final answer should be in the form of {{answer}}, at
the end of your response.
Initial Answer Generation
Can you solve the following problem? {question}
Explain your reasoning. Your final answer should be in the form of {{answer}}, at the
end of your response.
Debate
These are the solutions to the problem from other agents:
One agent solution: {reference solution}
One agent solution: {reference solution}
One agent solution: {reference solution}
One agent solution: {reference solution}
Using the solutions from other agents as additional information, can you provide your
answer to the problem? The original problem is {question}. Your final answer should be
in the form of {{answer}}, at the end of your response.
Figure 11: Prompt of Neighbor Debate used in the experiments.

Algorithm 1 CortexDebate Method
Input: Number of LLM agents n, set of LLM agents {A }n , set of directed edges {E } , test question Q,
i i=1 i→j i,j∈[1,2,...,n]
maximum debating rounds D, answer extraction ans (·)
Output: Final answer O
final
1: for i = 1 to n do
2: O0, H0 ← A (Q) ▷ Phase 1: Initial Answer Generation
i i i
3: Recalibration H0 based on Equation (2)
i
4: Calculate Ci based on Equations (3) and (4)
5: P i ← 0
0
6: end for
7: O ←
(cid:8) O0(cid:9)n
▷ Phase 2: Multi-round Debate
i i=1
8: for d = 1 to D do
9: for i = 1 to n do
10: Calculate Ri and Si based on Equations (5) and (8), respectively
d d
11: for j = 1 to n do
12: if i ̸= j then
13: Calculate Sim and Ii based on Equations (6) and (7), respectively
d d
14: Calculate W d based on Equation (9) ▷ Phase 2, Step 1: Edge Weight Optimization
i→j
15: end if
16: end for
17: end for
18: for j = 1 to n do
19: Debd, Othersd ← ∅ ▷ Phase 2, Step 2: Sparse Graph Establishment
j j
d
20: Calculate W based on Equation (10)
j
21: for i = 1 to n do
22: if i ̸= j then
23: Calculate W d based on Equation (11)
i→j
24: if W d = 1 then
i→j
25: Debd ← Debd ∪ {A }
j j i
26: Othersd ← Othersd ∪ (cid:8) Od−1(cid:9)
j j i
27: end if
28: end if
29: end for
30: Od, Hd ← A (cid:0) Q, Othersd(cid:1) ▷ Phase 2, Step 3: Answer Regeneration
i i j j
31: Recalibration Hd based on Equation (2)
i
32: end for
33: is_end ← True ▷ Phase 2, Step 4: Debate Termination
34: for i = 2 to n do
35: if ans
(cid:0) Od(cid:1)
̸= ans
(cid:0) Od(cid:1)
then
1 i
36: is_end ← False
37: break
38: end if
39: end for
40: O ←
(cid:8) Od(cid:9)n
i i=1
41: if is_end = True then
42: break
43: end if
44: end for
45: o ←set(O , O , · · · , O )
1 2 n
46: Get O based on Equation (14) ▷ Phase 3: Final Answer Generation
final
47: return O
final
