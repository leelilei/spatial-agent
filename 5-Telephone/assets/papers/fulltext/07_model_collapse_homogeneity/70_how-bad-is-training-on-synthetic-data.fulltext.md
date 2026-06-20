---
telephone_index: 70
title: "How Bad is Training on Synthetic Data?"
category: 07_model_collapse_homogeneity
venue: "arXiv"
year: 2024
doi: 
arxiv_id: 2404.05090
preferred_source_type: preprint_or_unresolved
publisher_url: https://arxiv.org/abs/2404.05090
quality_flags: []
---

# Citation Context

- Telephone index: 70
- Preferred source: arXiv
- DOI: none
- arXiv: 2404.05090
- PDF: `assets\papers\pdf\07_model_collapse_homogeneity\70_how-bad-is-training-on-synthetic-data.pdf`

## Extracted Abstract

The phenomenon of model collapse, introduced in (Shumailov et al., 2023), refers to the deterioration in performance that occurs when new models are trained on synthetic data generated from previously trained models. This recursive training loop makes the tails of the original distribution disappear, thereby making future-generation models forget about the initial (real) distribution. With the aim of rigorously understanding model collapse in language models, we consider in this paper a statistical model that allows us to characterize the impact of various recursive training scenarios. Specifically, we demonstrate that model collapse cannot be avoided when training solely on synthetic data. However, when mixing both real and synthetic data, we provide an estimate of a maximal amount of synthetic data below which model collapse can eventually be avoided. Our theoretical conclusions are further supported by empirical validations.
Title: Introduction

Source PDF: D:\0-Research\5-Telephone\assets\papers\pdf\07_model_collapse_homogeneity\70_how-bad-is-training-on-synthetic-data.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-06-20T12:46:13+00:00
- page_count: 18
- status: ok
- text_char_count: 49121

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Theoretical Setup (page 3)
  - Statistical Language Model (page 3)
  - Recursive Training (page 4)
- Main Results (page 5)
  - Fully Synthetic: Training on synthetic data (page 5)
  - Partially Synthetic: Handling model collapse with real data (page 7)
- Experiments (page 9)
  - Transformer-based Models (page 9)
  - Additional Experiments with the Statistical Model (page 10)
- Discussions & Conclusion (page 11)
- Technical Lemma (page 13)
- General Results and Proofs (page 13)
  - Derivation of Formula (2) (page 13)
  - Proofs for the Fully Synthetic Case (page 14)
  - Proofs for the Partially Synthetic Case (page 15)
- Architecture & training parameters for GPT2 experiments (page 18)

Markdown Content:

How Bad is Training on Synthetic Data? A Statistical Analysis
of Language Model Collapse
Mohamed El Amine Seddik Suei-Wen Chen Soufiane Hayou
Technology Innovation Institute NYU Abu Dhabi Simons Institute
Abu Dhabi, UAE Abu Dhabi, UAE Berkeley, USA
mohamed.seddik@tii.ae swc435@nyu.edu hayou@berkeley.edu
Pierre Youssef Merouane Debbah
NYU Abu Dhabi Khalifa University of Science and Technology
Abu Dhabi, UAE Abu Dhabi, UAE
yp27@nyu.edu merouane.debbah@ku.ac.ae
Abstract
The phenomenon of model collapse, introduced in (Shumailov et al., 2023),
refers to the deterioration in performance that occurs when new models
are trained on synthetic data generated from previously trained models.
This recursive training loop makes the tails of the original distribution disappear, thereby making future-generation models forget about the initial
(real) distribution. With the aim of rigorously understanding model collapse in language models, we consider in this paper a statistical model that
allows us to characterize the impact of various recursive training scenarios.
Specifically, we demonstrate that model collapse cannot be avoided when
training solely on synthetic data. However, when mixing both real and synthetic data, we provide an estimate of a maximal amount of synthetic data
below which model collapse can eventually be avoided. Our theoretical
conclusions are further supported by empirical validations.
1 Introduction
The large-scale adoption of large language models (e.g. ChatGPT (OpenAI, 2024)) will
inevitably lead to enormous amounts of synthetic (generated) data “polluting” the original
human-created web data. Since language models are trained on web data, this raises some
concerns about the impact of this synthetic data on the next generations of LLMs. One
can think of a train-generate loop where models from the current generation generate
data that contaminate existing web data, and the next generation models are trained on
this contaminated data. This loop was studied in several works (Shumailov et al., 2023;
Alemohammad et al., 2023; Briesch et al., 2023) where the authors conclude that synthetic
data generally hurts performance as the number of generate-train increases, and that
(naturally) the impact on model performance is linked to the amount of real data in the
training set. A particular phenomenon, coined model collapse (Shumailov et al., 2023), refers
to the model’s tendency to produce limited or repetitive outputs making recursive training
on such outputs forget about the tails of the original underlying distribution of real data.
This was further studied in (Guo et al., 2023) where the authors show that recursive training
on synthetic data leads to a “self-consuming” loop that affects linguistic diversity.
Intuitively, model collapse is a result of the distribution shift that occurs when training generative models recursively on synthetic data from previous generation models. Shumailov
et al. (2023) have discussed two main sources of model collapse; 1) statistical approximation
error: which is inherently related to the fact that generative models are trained on a finite
number of samples, and therefore it is impossible that the learned model captures all the information about the original distribution. 2) functional approximation error: which results from
1
4202
rpA
7
]GL.sc[
1v09050.4042:viXra

the fact that the models are insufficiently expressive in real implementations, even if neural
networks are known to be universal functional approximators from a theoretical standpoint.
The authors provide further theoretical intuition to characterize the effect of these approximation errors, relying on simple mathematical models such as single-dimensional Gaussian
distribution.
In this paper, we aim to provide a rigorous theoretical framework to understand the effects of recursive training with synthetic data. In particular, we focus on the statistical
approximation error and introduce a simple next-token-prediction language model to characterize model collapse. Our model allows us to gain insights into the behaviour of the
self-consuming train-generate loop leading to model collapse. From a theoretical standpoint,
we consider two main recursive training scenarios:
• Fully Synthetic: Training with data sampled from the previous generation model.
• Partially Synthetic: Training with a mixture of data sampled from the previous
generation model and original data.
We demonstrate that model collapse always occurs in the first scenario and characterize
the rates at which it occurs. Furthermore, in the second scenario, we provide an upper
bound on the sample size of generated data below which model collapse can eventually be
attenuated. Our results are further confirmed through simulations of general scenarios with
the introduced statistical model, as well as with realistic GPT2-style language models on
real data. Our findings suggest that the amount of generated data should be considerably
smaller compared to the original data to avoid model collapse.
Related work: With the adoption of generative Large Language and Vision models, the
amount of synthetic data on the web is growing at an unprecedented rate – see for example
(del Rio-Chanona et al., 2023) where the authors conducted an empirical study of the amount
of synthetic data via activity monitoring on Stack Overflow, and (Alemohammad et al., 2023)
where the authors showed that a dataset used to train Stable Diffusion contains synthetic
data (Schuhmann et al., 2022). In fact, practitioners are willingly using synthetic data to
train next-generation models (Ben Allal et al., 2024; Gunasekar et al., 2023; Chen et al., 2024).
As we mentioned above, several works studied the recursive training loop where nextgeneration models are trained on synthetic data generated from previous-generation models.
Shumailov et al. (2023) studied model collapse, a phenomenon that occurs in recursive
training where the quality of model outputs tend to degrade by becoming e.g. repetitive.
Similar phenomena were studied in (Alemohammad et al., 2023) where the authors call it
Model Autophagy Disorder (MAD). Another empirical study by (Briesch et al., 2023) studied
this same Self-Consuming phenomenon and observed that the degeneracy rate (naturally)
depends on the number of fresh data in the training sample. In the same direction, several
works showed that incorporating synthetic data in the training can hurt the performance of
trained diffusion models (Bohacek & Farid, 2023; Mart´ınez et al., 2023a;b).
Only a few works have tackled this question from a theoretical perspective. Shumailov
et al. (2023) considered a simple recursive Gaussian distribution to provide an intuition as
to why model collapse occurs, but no training is considered in that work. In (Fu et al., 2024),
authors studied recursive training of diffusion models (generally used to learn distributions
over images) and obtained an upper bound on the total variation distance between the
distribution of the original data and that of the synthetic data after T generations. Dohmatob
et al. (2024b) studied the impact of synthetic data on scaling laws and, in a simple setting of
linear regression, Dohmatob et al. (2024a) studied the behaviour of the test error of different
generations and showed that a linear dependency of the degradation on generation number.
In this work, we are interested in characterizing the distribution shift in synthetic data
generated with a language model, as the number of generations increases. We consider a
linear Softmax classifier for next-token prediction and study the distribution of the learned
conditional probabilities as the number of generations increases. The closest work to ours is
(Fu et al., 2024) where the authors study the distribution of synthetic data generated by a
2

diffusion model instead, whereas the statistical model we are considering is closer in spirit
to the realm of language models.
The remainder of the paper is organized as follows. Section 2 presents our theoretical setup
where we introduce our statistical model and the considered recursive training scenarios.
Our main theoretical results are presented in Section 3. We further present some experiments
in Section 4.1 to support our findings. Finally, Section 5 concludes the paper.
2 Theoretical Setup
2.1 Statistical Language Model
We consider a language model of vocabulary size s, context length denoted by ℓ and we
further denote by c the number of possible contexts which is at most sℓ. We suppose that
the language data is generated from some unknown conditional probabilities given the
contexts. That is, the probability of the next token being k ∈ [s] := {1, ..., s} given some
context j = (j 1 , . . . , j ℓ ) ∈ [c] is denoted by
p := P{Y = k | X = j},
jk
where X and Y denote discrete random variables representing a context and the nexttoken respectively. In practice, we do not have access to the true conditional probabilities
p but rather a (large) corpus sampled according to p . In other words, we are given
jk jk
a dataset {(x , y )} of M samples of contexts and next-token pairs represented by
l l l∈[M]
x ∈ {e , . . . , e } and y ∈ {e , . . . , e } where e ’s denote the canonical vectors.
l 1 c l 1 s i
Given this dataset, we consider approximating the underlying conditional probabilities via
the Softmax classifier, which entails minimizing the categorical cross-entropy loss function:
arg min − 1 ∑ M y ⊤ log σ (cid:16) W ⊤ x (cid:17) , (1)
M l l
W=[w1,...,ws ]∈Rc×s l=1
where σ(v) =
exp(v)
is the Softmax function and the functions exp and log are applied
∑s
k=1
exp(vk )
entry-wise. Note that in current state-of-the-art language models, the x ’s are context
l
representations computed via transformer models, whereas, in our setting, we choose to
work with one-hot embeddings as representations for tractable theoretical analysis. Solving
the above objective (see Appendix B.1) yields the estimated conditional probability pˆ of
jk
p which expresses as the following empirical mean:
jk
pˆ = exp(wˆ k ⊤e j ) = 1 ∑ y with C = (cid:8) l ∈ [n] | x = e (cid:9) . (2)
jk ∑
i
s
=1
exp(wˆ
i
⊤e
j
) |C
j
|
l∈C j
lk j l j
The estimated conditional probabilities pˆ are the result of training on the original data.
jk
These conditional probabilities can be used to generate new synthetic data, which can be
used (with or without additional fresh data from the original dataset) to train the nextgeneration model. In this paper, we are interested in characterizing the behaviour of pˆ in
jk
this recursive training loop which we will formally define in the next section. Hereafter,
without loss of generality, we consider a fixed context j with N := |C | training samples
j
{(e , y )} of context-next-token pairs, where y ∈ Rs are independent multinomial random
j l l l
variables with one trial and parameter
p = (p , . . . , p ) := (p , . . . , p ) ∈ [0, 1]s. (3)
1 s j1 js
From (2), we notice that pˆ is an estimate of p and we further denote
jk jk
p (1) = (pˆ , . . . , pˆ ) := (pˆ , . . . , pˆ ) ∈ [0, 1]s. (4)
1 s j1 js
As such, p(0) := p corresponds to the ground-truth distribution whereas p(1) denotes the
first-generation model trained on the real data {(e j , y l )} l∈C j .
3

p(0)
p(10) p(20) p(30) p(40)
Figure 1: Evolution of p(m) in the Fully Synthetic setting for vocabulary size s = 3, context
length ℓ = 4, total contexts c = sℓ = 81 and sample size n = 1000. The initial distribution
p(0) is some random distribution over tokens. The trained conditional distributions converge
towards Dirac measures over generations illustrating total collapse in Definition 1.
2.2 Recursive Training
In this section, we introduce the notations for recursive training. At generation m ≥ 1, suppose that we have samples {y (t) } generated by some past models p(t) for t ∈ {0, . . . , m − 1}
l l
respectively. As such, similarly to (2), the model at generation m expresses as
p (m) := 1 m ∑ −1 n ∑
(
t
m)
y (t) . (5)
n(m) l
t=0 l=1
In other words, p(m) is obtained by training the model on a mixture of real and synthetic
(m)
data generated from previously trained models. Here, n stands for the number of
t
samples used to train the m-th generation model that are generated by model p(t), and
n(m) = n (m) + · · · + n (m) is the total number of training samples used to train p(m). Note
0 m−1
that we do not generate samples from p = p(0) but rather we are given a corpus {y (0) }
l l
which represent original data.
Note that by definition all the models p(m) are unbiased, i.e. Ep(m) = p, which means that
they recover the original distribution in case of infinite sample sizes. However, in practical
settings the sample sizes are finite, and therefore p(m) may deviate from p since its variance
(m)
can be large for small values of n . In the remainder of the paper, we present analytical
t
results to rigorously quantify the impact of sample sizes n (m) on the variance of p(m) and
t
how they affect the learned distribution to eventually cause model collapse (Shumailov et al.,
2023), a degenerative process affecting future generation models by either losing information
about the tails of the initial distribution or inducing distribution shifts over generations.
Specifically, we aim to quantify the rate of such deterioration, and to this end, we introduce
a stricter version of model collapse that we call total collapse and define as follows.
Definition 1 (Total Collapse). We say that total collapse occurs in the recursive training process if
p(m) converges to some Dirac mass δ for some token i ∈ [s] as m grows.
i
Total collapse refers to the case where, under recursive training, the trained model p(m)
completely loses information about the original distribution p over generations, leading
to poor linguistic diversity.1 This phenomenon is illustrated in Figure 1 where we see
convergence towards the vertices of the probability simplex, i.e. Dirac measures, over
generations. With this definition of total collapse, we provide a quantitative analysis of two
cases of recursive training:
1Note that here we define total collapse with respect to a single pre-fixed context. This can be
generalized to the event where total collapse occurs for all contexts. However, the theoretical analysis
in this case would require more refined treatment of several statistical quantities to obtain uniform
bounds over contexts. We leave this for future work.
4

• Fully Synthetic: Training with synthetic data from the last model. Each generation
p(m) is trained only on data generated by the previous model p(m−1). More precisely,
for some fixed n ∈ N we let n (m) = n · 1{t = m − 1} for all m ≥ 1 and 0 ≤ t < m.
t
• Partially Synthetic: Training with a mixture of real and synthetic data from the last
model. Each generation p(m) is trained on a mixture of real data and synthetic data
generated by the previous model p(m−1). More precisely, for some fixed n ∈ N we
let n
(m)
= N, n
(m)
= n and n
(m)
= 0 for all m ≥ 2 and 0 < t < m, and n
(1)
= N.
0 m−1 t 0
Fully Synthetic corresponds to the theoretical setting considered in (Shumailov et al., 2023).
However, in that paper, only Gaussian distribution was analyzed instead of discrete distributions over all possible tokens as language models entail. We point out that this setting is
unlikely to happen in real-world applications but serves as the worst-case scenario.
On the other hand, the Partially Synthetic setting is more realistic for future generation
models as it corresponds to training on a mixture of real and synthetic data. We consider
this setting to assess whether it is possible to avoid collapse by having a fraction of the
original data in the training mixture. We answer this question positively in the next section.
Moreover, we show through simulations in Section 4.1 that conclusions from our theoretical
analysis on both Fully Synthetic and Partially Synthetic hold beyond these simple settings,
such as training on a mixture of all generations or even using realistic transformer models.
3 Main Results
To investigate the model collapse phenomenon and the rate at which it occurs, we define
the following statistical quantities that capture the randomness of p(m):
∥p (m)∥∞ := max p
i
(m) , σ
m
:= ∥p (m)∥2
2
= ∑ s p
i
(m)2 and S
m
:= E[σ
m
].
i∈[s]
i=1
These quantities measure how far away p(m) is from some Dirac mass (Total Collapse,
Definition 1). Since the maximum value of all three quantities is 1, the closer they are to 1,
the closer p(m) is to some Dirac mass, and the less diverse p(m) is as a language model. As
such, ∥p(m)∥∞ or σ
m
being equal to 1 is equivalent to p(m) being a Dirac mass which reflects
total collapse. To quantify the distribution shift incurred by the aforementioned recursive
training scenarios, we further consider the 1-norm2 between two distributions µ, ν ∈ Rs
defined by ∥µ − ν∥ := ∑s |µ(i) − ν(i)|.
1 i=1
We assume that the initial distribution p(0) is nontrivial, specifically S
0
< 1 and ∥p(0)∥∞ < 1.
Under this assumption, we provide results on the rate of total collapse and further quantify
distribution shift under recursive training. All the proofs are presented in Appendix B.
3.1 Fully Synthetic: Training on synthetic data
We start by describing the recursive training process in which only synthetic data from the
last generation model are used. This process can be viewed as a Markov chain on the set of
probability measures ∆s−1 ∩ 1 Ns on [s] with denominator n, where
n
∆s−1 := {v ∈ Rs : v + v + · · · + v = 1, v ≥ 0 for all i}
1 2 s i
2We point out that the 1-norm is twice the total variation distance ∥µ − ν∥ , which is another
TV
commonly used metric for probability distributions and was considered by Fu et al. (2024) for studying
model collapse in the case of diffusion models.
5

is the probability simplex. Since the probability of reaching δ is positive provided p > 0,
i i
this random walk which starts at p(0) has absorbing states {δ : i ∈ [s] s.t. p > 0}. As a
i i
result, the random walk converges to one of the absorbing states almost surely (Kemeny
et al., 1969), which means that total collapse is bound to happen in the Fully Synthetic setting.
To characterize the rate at which total collapse occurs, let us denote by T := inf{t ∈ N :
∥p(t)∥∞ = 1} ≥ 1 the random time at which the model first becomes a Dirac mass, and let
(cid:16) (cid:17)
ρ
m
:= P ∥p(m)∥∞ = 1 denote the probability that the m-th generation has collapsed. Our
first result, presented in Theorem 1, provides the rate of convergence via S , ρ and E[T].
m m
Theorem 1 (Control on Total Collapse). Consider the Fully Synthetic setting and let s˜ :=
|supp(p)| denote the support size of p, namely s˜ := |{i ∈ [s] : p > 0}|.
i
1. The expected sum of squared probabilities S is given by
m
(cid:18) (cid:19)m
1
S = 1 − 1 − (1 − S ). (6)
m 0
n
2. The probability ρ that total collapse has occurred by generation m satisfies
m
1 − S
1 − n(1 − S )(1 − 1/n)m ≤ ρ ≤ 1 − 0 (1 − 1/n)m. (7)
0 m 1 − 1/s˜
3. The generation T at which total collapse happens satisfies
1 − S
1 + 0 (n − 1) ≤ E[T] ≤ 1 + (1 − S )n(n − 1). (8)
1 − 1/s˜ 0
In essence, Theorem 1 describes the behavior of p(m) as a function of the model generation
m, the sample size n, and the dispersion of the initial distribution S . Specifically, we draw
0
the following observations:
• Effect of the number of generations m: As m increases, S and ρ tend to 1 as per
m m
(6) and (7), making total collapse increasingly more likely. Note also that this
dependence is exponential in m, making total collapse in this case relatively fast.
• Effect of “synthetic” sample size n: The smaller n is, the more likely p(m) is to have
collapsed for a given generation m as per the bounds on ρ in (7), and the faster
m
total collapse is expected to happen as suggested by (8). The dependence in this
case is polynomial in n.
• Effect of S : Larger values of S correspond to faster collapse as suggested by (8);
0 0
namely, starting from an original distribution that is not diverse enough speeds up
total collapse. The upper and lower bounds on E[T] are both linear in (1 − S ).
0
We point out that when the number of contexts c is large, the number of samples n per
context would be fairly small, which suggests that total collapse, given a single context, is
expected to happen fairly quickly. The bounds on E[T] state that the expected collapse time
is at least of order n and at most of order n2, though experiments (see Figure 2) suggest
that the upper bound is not sharp and should be close to O(n) instead. On another note,
we characterize below in Proposition 1 the limiting distribution as m gets to infinity, which
demonstrates the direction of total collapse.
(cid:16) (cid:17)
Proposition 1. In the Fully Synthetic case, we have P lim p (m) = δ = p for all i ∈ [s].
m→∞ i i
Proposition 1 describes the limiting distribution when total collapse occurs in terms of
the initial probabilities p over tokens. Specifically, the resulting Dirac mass δ is likely to
i i
be supported on some token i with high initial probability p . This formally supports the
i
description of early and late model collapse in Shumailov et al. (2023): In the early phase of
recursive training, the tails of the original distribution disappear because the probability
6

Figure 2: Fully Synthetic case for different initial distribution p(0) . Total collapse time is
plotted as a function of the initial distribution p and the sample size n. (Top) The initial distribution p
with different values of S and support size s˜. The x-axis represents tokens i ∈ {1, 2, . . . , 600} while
0
the y-axis represents the probabilities in log scale. (Bottom) Each cross represents the average total
collapse time over 100 runs for a particular sample sizes n ∈ {10, 50, 100, 150, . . . , 400}. The red dashed
line depicts the lower bound on ET given by (8).
p (m) of outputting unlikely tokens j (those j’s for which p is small) will decrease as p(m)
j j
(m)
converges to some Dirac mass δ . After many generations, all but one p will go to 0,
i j
exhibiting late model collapse where all the randomness of the original distribution is lost.
3.2 Partially Synthetic: Handling model collapse with real data
As described in the previous section, total collapse is unavoidable when training solely
on synthetic data. In this section, we consider the case in which real data is incorporated
at each generation. In this case, p(m) can be simply seen as a weighted average of p(1)
and an estimate of p(m−1) with n samples. We also assume that p(1) is nontrivial, thereby
implying that, on average, p(m) will not be a Dirac mass. In what follows, we quantify the
variability in the data distribution across different generations, as well as the distribution
drift ∥p(m) − p(1)∥ from the first-generation model. We particularly show that collapse can
1
be avoided if enough real data is injected into the recursive training process.
Theorem 2 (Model Variation). Consider the Partially Synthetic setting. For m ≥ 1 we have
(cid:104) (cid:16) (cid:17) (cid:105)
S m+1 = N 1 1 + 1 + 2α ( − 1 + 1 1 − /N N 1 )α αβm + 1 + (1 (1 − + N 1 1 ) / S N 0 )α (cid:20) 1 + α − α N βm (cid:21) , (9)
(cid:104) (cid:105)
where α := n and β := α (1 + 1 )α − 1 .
N+n N N
Theorem 2 provides a control of the variance S in the Partially Synthetic setting. Essentially,
m
when n ≪ N, we have S ≈ 1 + (1 − 1 )S ≈ S , which is not surprising since the training
m N N 0 0
data for each generation model are dominated by real data in this case. However, even
when the number of synthetic data is much larger than the original dataset (i.e. n ≫ N),
we have α ≈ 1 ≈ β and hence S m+1 ≈ 1/N + (2 + 1/N)−1(1 − 1/N)(2 − 1/N)S 0 , which
approaches S for large N.
0
To further refine our analysis, we present a result that directly controls the deviation
E∥p(m) − p(1)∥ between the conditional distributions from first and m-th generations. This
1
allows us to have a quantitative control over the distribution shift. When n is sufficiently
small, we have a sharper control over this deviation by exploiting the concentration results
7

Figure 3: Partially Synthetic case with different sample sizes n. A hundred experiments
were run for 50 generations for N = 100 and different values of n. Each yellow line represents the
evolution of σm (top row) or ∥p(m) − p(1)∥
1
(bottom row) in one experiment, with the red line being
the empirical mean across 100 runs. The blue dashed lines plot the formula for Sm given by (9). The
initial distribution p satisfies s = 600, s˜ = 52, and S = 0.1.
0
from (Mardia et al., 2020). Essentially, this allows us to estimate the maximum number of
synthetic samples n to ensure that the distribution p(m) stays close to p(1).
Theorem 3 (Model Deviation). Consider the Partially Synthetic setting and define
  C 1 se
(cid:16)
C 2 0 e n
(cid:17)s/2
if C e 0 n + 2 ≤ s;
G n (s) := C s C0n if C0 n + 2 ≤ s < C0 n + 2; (10)
(2 1
s − 2
s
) if s
4
< C0 n + 2,
e
4
where C = e3 ≈ 3.19 and C = 6e ≈ 2.93, and s is the vocabulary size. Then, for m ≥ 2,
0 2π 1 π3/2
(cid:114)
1 πn
E∥p (m) − p (1)∥ < G (s).
1 n
N 2
We point out that the upper bound on the deviation E∥p(m) − p(1)∥ is independent of the
1
generation m. Since the deviation from p(0) to p(1) is inevitable and independent of n, we
give the result in E∥p(m) − p(1)∥ , from which E∥p(m) − p(0)∥ can be estimated by the
1 1
triangle inequality. Theorem 3 allows us to estimate the maximum number of synthetic
samples n that can be used if we want p(m) to stay ϵ-close to p(1) in L1 norm. For example,
when C n/e + 2 ≤ s, for any ϵ > 0 we can take
0
(cid:34) (cid:32) √ (cid:33)(cid:35)
2πNϵ
n ≤ 2πe −2 min s − 2, log (11)
6es
in order for E∥p(m) − p(1)∥ to be less than ϵ. In other words, to ensure small L1 deviation
1
n should be taken to be logarithmic in the ratio Nϵ/s, which highlights that the amount of
synthetic data should be exponentially smaller compared to real data in order to ensure
that p(m) remains close to p(1). We show through simulations the effect of the sample size
n and the initial distribution p. In Figure 3, we show that if we fix the initial distribution
and increase the amount of synthetic data n, the dispersion σ stays relatively constant
m
while the distribution drift ∥p(m) − p(1)∥ increases. In contrast, when we fix n and increase
1
the values of S , σ increases but ∥p(m) − p(1)∥ actually decreases as depicted in Figure
0 m 1
4. This behavior can be explained by Theorem 4 in Appendix B, which is more general
than Theorem 3 in the sense that it captures the dependence of E∥p(m) − p(1)∥ on the
1
randomness of p and hence provides a sharper bound on the expected deviation.
8

Figure 4: Partially Synthetic case with different initial distributions p. A hundred experiments were run for 50 generations for n = 10, N = 100 and different initial distributions p shown
in the top row. Notice that as S increases, the deviation ∥p(m) − p(1)∥ decreases, as suggest by the
0 1
inequality (19).
4 Experiments
4.1 Transformer-based Models
To support our findings in a realistic setting, we conduct experiments with a decoder-only
generative model for text generation. For this model, we consider the aforementioned Fully
Synthetic and Partially Synthetic settings using the model parameters in Appendix C. We
consider a simple character-level tokenizer using the tiny Shakespeare dataset3 yielding
a vocabulary of size s = 65. We first train a model for 2000 iterations on this dataset
and consider the trained model as the ground-truth distribution p(0). The next-generation
models are trained recursively using the exact same architecture and training parameters.
This setting allows us to reduce the effect of functional approximation error thereby focusing
only on the effect of statistical approximation error.
The results of these experiments are summarized in Figure 5. The top left plot therein depicts
the deviation ∥p(m) − p(1)∥ which is averaged over 300 random contexts generated by
1
the ground-truth generative model p(0). From this plot, we clearly see that ∥p(m) − p(1)∥
1
diverges over generations in the Fully Synthetic setting, while mixing with real data ensures
stability over generations.
The effect of synthetic data is further noticed in the validation loss of the next-generation
models where we see an overfitting effect in the Fully Synthetic setting. We point out that this
effect might also be associated with the functional approximation error and was rigorously
studied by Dohmatob et al. (2024a) in the case of linear regression, where the authors have
shown that synthetic data affect the usual scaling laws. We believe that similar conclusions
can be obtained with our statistical model by incorporating the functional approximation
error, this can be achieved for instance by supposing that the context embeddings e ’s are
i
3https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/
input.txt
9

0.8
0.7
0.6
0.5
0.4
1 2 3 4 5 6 7 8 9
generation m
)1(p
)m(p
1
synthetic 2.50
synthetic 50% - real 50% 2.25 synthetic 20% - real 80%
2.00
1.75
1.50
1.25
100 101
iterations
ssol
lav
synthetic
Gen 1 Gen 6
Gen 2 Gen 7
Gen 3 Gen 8
Gen 4 Gen 9
Gen 5 Gen 10
2.50
2.25
2.00
1.75
1.50
1.25
100 101
iterations
ssol
lav
synthetic 50% - real 50%
Gen 1 Gen 6 2.50
Gen 2 Gen 7 2.25
Gen 3 Gen 8
2.00
Gen 4 Gen 9
Gen 5 Gen 10 1.75
1.50
1.25
100 101
iterations
ssol
lav
synthetic 20% - real 80%
Gen 1 Gen 6
Gen 2 Gen 7
Gen 3 Gen 8
Gen 4 Gen 9
Gen 5 Gen 10
Figure 5: Experiments with a GPT2-type generative model. The top left plot depicts the
deviation ∥p(m) − p(1)∥ varying the generation model m for synthetic data and a mixture
1
of real and synthetic data. The three other plots show the behavior of the validation loss
over generations. Essentially, training solely on synthetic data causes model collapse and
affects the usual scaling laws (Dohmatob et al., 2024a).
high-dimensional Gaussian vectors instead of canonical vectors, thereby introducing the
embedding dimension as a parameter controlling model complexity.
4.2 Additional Experiments with the Statistical Model
To further investigate and demonstrate the generality of our theoretical findings, we present
empirical results on two more scenarios that better represent recursive training in real-world
settings, as follows:
• Most Recent Models: Each generation p(m) is trained on synthetic data from the most
recent K models for a fixed window size K. More precisely, for some fixed n ∈ N
we let n (m) = ⌊n/K⌋ · 1{max(0, m − K) ≤ t ≤ m − 1} for all m ≥ 1. When K = 1,
t
this case degenerates to the Fully Synthetic setting.
• Randomly Sampled Data: Each generation p(m) is trained on a mixture of synthetic
data from possibly all the previous models and the real data. More precisely, the
m-th generation model is trained on n = n
(m)
+ · · · + n
(m)
samples with
0 m−1
n
n (m) := ∑ 1{g = t}, (t = 0, · · · , m − 1),
t i
i=1
samples from the t-th generation, where {g } are independent and uniformly
i i∈[n]
distributed on {0, 1, . . . m − 1} indexing previous-generation models. This setting
describes the scenario where data generated by all past models are mixed in a pool
from which the training data for the next generation is collected.
Experiments for these two cases are shown in Figure 6. Column 1 corresponds to Fully
Synthetic, columns 2 and 3 for Most Recent Models, and column 4 shows the case of Randomly
Sampled Data. As we can see, when the window size K is increased, total collapse is delayed
but still eventually happens. Observe that there are multiple visible horizontal yellow lines
in the second row for window size 1. This is because p(m) can converge to any of the Dirac
10

Figure 6: Experiment for Most Recent Models and Randomly Sampled Data. A hundred
experiments were run for 500 generations for different window sizes and a fixed sample size n = 10.
In the first two rows, each yellow line represents the evolution of σm and ∥p(m) − p(1)∥
1
in one
experiment respectively, with the red line being the empirical mean across 100 runs. The bottom row
plots the histogram of total collapse time T with the red line being the empirical mean. The initial
distribution p satisfies s = 600, s˜ = 52 and S = 0.1.
0
masses δ provided p > 0 by Proposition 1. A similar phenomenon can be observed in
i i
the second and third columns. On the other hand, in column 4 the model does deteriorate
but the deviation plateaus very quickly. In particular, the 100 runs produce only one Dirac
mass over the span of 500 generations, suggesting that randomly sampling from all the
past models is qualitatively different from sampling from the most recent K models with
a fixed K. We remark that for K > 1, even if p(m) is some Dirac mass, p(m+1) could still
regain randomness from models before generation m, but with a fixed window size all the
randomness eventually disappears.
5 Discussions & Conclusion
In this paper, we studied model collapse in language models through a simple statistical
model. We provided theoretical analysis when training with only synthetic data and when
adding real data from the original distribution. Our results demonstrate that model collapse
always happens when the model is training solely on synthetic data, whereas controlling
deviation from the initial distribution requires careful choice of the amount of synthetic
data to inject in the training set. We also provided experiments showing that these findings
extend beyond the simple theoretical settings.
Our current results describe only the statistical approximation error since all generation
models are unbiased in our theoretical framework. However, as we discussed in the previous
section, this framework can be extended to account for the functional approximation error by
considering high-dimension Gaussian vectors as context embeddings instead of canonical
vectors. Another possible extension is to study the effect of in-context learning (Wu et al.,
2023) on model collapse, which is a key feature of transformer-based models.
Despite the simple setting of our current investigation, we believe that it lays the groundwork for better understanding and mitigation of model collapse in language models, thereby
opening the way for the development of more general theoretical frameworks to study
next-generation language models dynamics.
11

References
Sina Alemohammad, Josue Casco-Rodrigu
Hossein Babaei, Daniel LeJeune, Ali Siahk
generative models go mad, 2023.
Loubna Ben Allal, Anton Lozhkov, Guilhe
Werra. Cosmopedia, 2024. URL https:/
cosmopedia.
Matyas Bohacek and Hany Farid. Nepotistic
Martin Briesch, Dominik Sobania, and Fran
their own output: An analysis of the selfZixiang Chen, Yihe Deng, Huizhuo Yuan,
tuning converts weak language model
arXiv:2401.01335, 2024.
Maria del Rio-Chanona, Nadzeya Laurents
models a threat to digital public goods? e
Elvis Dohmatob, Yunzhen Feng, and Julia K
regression, 2024a.
Elvis Dohmatob, Yunzhen Feng, Pu Yang,
tails: Model collapse as a change of scalin
Shi Fu, Sen Zhang, Yingjie Wang, Xinmei
understandings of self-consuming genera
Suriya Gunasekar, Yi Zhang, Jyoti Aneja, C
Sivakanth Gopi, Mojan Javaheripi, Piero
et al. Textbooks are all you need. arXiv pr
Yanzhu Guo, Guokan Shang, Michalis Vazir
of linguistic diversity: Training language
John G Kemeny, J Laurie Snell, et al. Finite ma
NJ, 1969.
Jay Mardia, Jiantao Jiao, Ervin Ta´nczos, Ro
tration inequalities for the empirical dis
method of types. Information and Inference
Gonzalo Mart´ınez, Lauren Watson, Pedro R
and Rik Sarkar. Combining generative art
towards evolution or degradation?, 2023a
Gonzalo Mart´ınez, Lauren Watson, Pedro R
and Rik Sarkar. Towards understanding t
and the internet, 2023b.
OpenAI. Gpt-4 technical report, 2024.
Christoph Schuhmann, Romain Beaumon
man, Mehdi Cherti, Theo Coombes, Aar
Patrick Schramowski, Srivatsa Kundurthy
Kaczmarczyk, and Jenia Jitsev. Laion-5b
generation image-text models, 2022.
Ilia Shumailov, Zakhar Shumaylov, Yiren
Anderson. The curse of recursion: Trainin

, Lorenzo Luzi, Ahmed Imtiaz Humayun,
hi, and Richard G. Baraniuk. Self-consuming
e Penedo, Thomas Wolf, and Leandro von
uggingface.co/datasets/HuggingFaceTB/
y trained generative-ai models collapse, 2023.
othlauf. Large language models suffer from
suming training loop, 2023.
xuan Ji, and Quanquan Gu. Self-play finestrong language models. arXiv preprint
a, and Johannes Wachs. Are large language
ence from activity on stack overflow, 2023.
pe. Model collapse demystified: The case of
ncois Charton, and Julia Kempe. A tale of
aws, 2024b.
n, and Dacheng Tao. Towards theoretical
e models, 2024.
o Ce´sar Teodoro Mendes, Allie Del Giorno,
auffmann, Gustavo de Rosa, Olli Saarikivi,
int arXiv:2306.11644, 2023.
nnis, and Chloe´ Clavel. The curious decline
dels on synthetic text, 2023.
v chains, volume 26. van Nostrand Princeton,
D Nowak, and Tsachy Weissman. Concenution of discrete distributions: beyond the
Journal of the IMA, 9(4):813–850, 2020.
riego, Jose´ Alberto Herna´ndez, Marc Juarez,
al intelligence (ai) and the internet: Heading
riego, Jose´ Alberto Herna´ndez, Marc Juarez,
interplay of generative artificial intelligence
Richard Vencu, Cade Gordon, Ross WightKatta, Clayton Mullis, Mitchell Wortsman,
atherine Crowson, Ludwig Schmidt, Robert
n open large-scale dataset for training next
ao, Yarin Gal, Nicolas Papernot, and Ross
n generated data makes models forget, 2023.

Tsachy Weissman, Erik Ordentlich, Gadiel Seroussi, Sergio Verdu, and Marcelo J Weinberger.
Inequalities for the l1 deviation of the empirical distribution. Hewlett-Packard Labs, Tech.
Rep, 2003.
Jingfeng Wu, Difan Zou, Zixiang Chen, Vladimir Braverman, Quanquan Gu, and Peter L
Bartlett. How many pretraining tasks are needed for in-context learning of linear regression? arXiv preprint arXiv:2310.08391, 2023.
A Technical Lemma
For completeness, we include the concentration results from (Mardia et al., 2020) which we
used to prove Theorem 3. For a probability distribution p on [s] define
π := max min{p(A), 1 − p(A)} (12)
p
A⊆[s]
and notice that π ≤ 1 . Define the function φ : [0, 1/2) → R by
p 2
1 1 − x
φ(x) := log
1 − 2x x
and extend φ by continuity to φ(1/2) := 2. Observe that φ is strictly decreasing and
2 ≤ φ(x) < ∞. The following Lemma concerns the concentration of empirical distribution
which captures the dependence on the sample size n, dimension s as well as the structure of
the underlying probability distribution via φ(π ).
p
Lemma 1. Let p be a probability distribution on [s] and pˆ be the associated empirical distribution
obtained from n samples. Then for ϵ > 0 we have
(cid:32) (cid:33)
nφ(π )ϵ2
P (∥pˆ − p∥ ≥ ϵ) ≤ exp − p G (s),
1 n
4
where C = e3 , C = 6e and
0 2π 1 π3/2
 C s (C n/s)s/2 if C0n + 2 ≤ s ≤ C0n + 2;
 1 0 4 e
G n (s) =  C
(2
1
s
s
−
e C 2 0
2
e n
) i
i
f
f
s
C e 0
≤
n +
C0
2
n +
≤
2
s
.
; (13)
4
The upper bound
(cid:32) (cid:33)
nφ(π )ϵ2
P(∥pˆ − p∥ ) ≤ (2s − 2) exp − p
1
4
in fact holds for all values of s and n (Weissman et al., 2003), but this bound is very poor
when s/n is large, which is commonly the case for language models. Lemma 1 provides an
≲
improvement in the regime of small sample size n s.
B General Results and Proofs
B.1 Derivation of Formula (2)
Proof. The categorical cross-entropy loss reads as
(cid:32) (cid:33)
L(w , . . . , w ) = − 1 ∑ M ∑ s y log exp(w k ⊤x i ) .
1 s M ik ∑K exp(w⊤x )
i=1 k=1 j=1 j i
13

The gradient of the loss is expressed as
(cid:104) (cid:105)
∂ ∂ w L k = M 1 i ∑ = M 1 ℓ ∑ = s 1 y iℓ ∂w 1 ∂ k + ∑ ∑ j j ̸= ̸= ℓ ℓ e e x x p p ( ( ( ( w w j j − − w w ℓ ℓ ) ) ⊤ ⊤ x x i i ) ) ,
where
(cid:34) (cid:35) (cid:40)
∂w
∂
k j
∑
̸=ℓ
exp((w
j
− w
ℓ
)⊤ x
i
) =
e
−
xp
∑
(
j
(
̸=
w
k e
k
x
−
p(
w
(w
ℓ )⊤
j −
x i )
w k )
i
⊤
f
x i
k
)x
̸=
i
ℓ.
if k = ℓ,
Therefore,
∂L = 1 ∑ M (cid:40) y − ∑ j̸=k exp((w j − w k )⊤x i ) + ∑ y exp((w k − w ℓ )⊤x i ) (cid:41) x
∂w k M i=1 ik 1 + ∑ j̸=k exp((w j − w k )⊤x i ) ℓ̸=k iℓ 1 + ∑ j̸=ℓ exp((w j − w ℓ )⊤x i ) i
= 1 ∑ M (cid:40) ∑ y exp(w k ⊤x i ) − y ∑ j̸=k exp(w⊤ j x i ) (cid:41) x
M iℓ ∑s exp(w⊤x ) ik ∑s exp(w⊤x ) i
i=1 ℓ̸=k j=1 j i j=1 j i
(cid:40) (cid:32) (cid:33)(cid:41)
= M 1 ∑ M ∑ y iℓ ∑s exp e ( x w p( k ⊤ w x ⊤ i ) x ) − y ik 1 − ∑s exp e ( x w p( k ⊤ w x ⊤ i ) x ) x i
i=1 ℓ̸=k j=1 j i j=1 j i
 
= 1 ∑ M

∑ s y exp(w k ⊤x i ) − y

x
M i=1  ℓ
(cid:124)
=
(cid:123)
1
(cid:122)
i
(cid:125)
ℓ ∑s j=1 exp(w⊤ j x i ) ik  i
=1
(cid:40) (cid:41)
= 1 ∑ M exp(w k ⊤x i ) − y x
M ∑s exp(w⊤x ) ik i
i=1 j=1 j i
Finally, solving for ∂L = 0 yields (2).
∂wk
B.2 Proofs for the Fully Synthetic Case
Proof of Theorem 1. Write p
(m)
= X
(m)
/n where X
(m)
∼ B(n, p
(m−1)
) is binomial when
i i i i
conditioned on p(m−1). So we have
(cid:18) (cid:19)
E[p (m)2 | p (m−1)] = 1 p (m−1) + 1 − 1 p (m−1)2
i n i n i
∑ s E[p (m)2 | p (m−1)] = 1 + (cid:18) 1 − 1 (cid:19) ∑ s p (m−1)2
i n n i
i=1 i=1
and by the law of total expectation
(cid:18) (cid:19) (cid:18) (cid:19)m
1 1 1
S m = + 1 − S m−1 = 1 − 1 − (1 − S 0 ). (14)
n n n
Note that S ↗ 1 as m → ∞ and
m
(cid:34) (cid:35) (cid:34)(cid:32) (cid:33) (cid:35)
S
m
= E ∑ p
i
(m) p
i
(m) ≤ E ∑ p
i
(m) ∥p (m)∥∞ = E∥p (m)∥∞.
i i
(cid:16) (cid:17)
Recall that ρ
m
:= P ∥p(m)∥∞ = 1 and T := inf{m ∈ N : ∥p(m)∥∞ = 1} ≥ 1. Since
σ
m
≥ 1/s˜ and ∥p(m)∥∞ ∈ {
n
1 , . . . , n−
n
1 , 1}, we have
1
1 · ρ
m
+ (1 − ρ
m
) ≤ Eσ
m
= S
m
≤ E∥p (m)∥∞ ≤ 1 · ρ
m
+ (1 − 1/n)(1 − ρ
m
),
s˜
14

from which (7) follows thanks to (14).
For k = 1, 2, . . . we have P(T > k) = P(∥p(k)∥∞ < 1) = 1 − ρ
k
and thus
1 − S
0 (1 − 1/n)k ≤ P(T > k) ≤ n(1 − S )(1 − 1/n)k,
1 − 1/s˜ 0
which establishes (8) because E[T] = ∑∞ P(T > k).
k=0
Proof of Proposition 1. Fix i ∈ [s]. For m ≥ 1 consider the events E := {T ≤ m} and
m
F := {p
(m)
= 1}. Then p
(m)
∈ {0, 1} on E and F ⊆ E . Observe that
m i i m m m
E ↗ ∪ E and F ↗ ∪ F = { lim p (m) = δ },
m m m m m m m→∞ i
where P(∪ E ) = 1 by Theorem 1 and in particular P(E ) > 0 for m large. Thus
m m m
(cid:104) (cid:105)
p = lim E[p (m) ] = lim P(E )E[p (m) | E ] + P(Ec )E[p (m) | Ec ]
i m→∞ i m→∞ m i m m i m
= lim E[p (m) | E ] = lim P(p (m) = 1 | E ) = lim P(F m ∩ E m )
m→∞ i m m→∞ i m m→∞ P(E
m
)
P(F )
= lim m = lim P(F ) = P(∪ F ),
m→∞ P(E
m
) m→∞ m m m
which proves the assertion.
B.3 Proofs for the Partially Synthetic Case
(cid:20) (cid:21)
Proof of Theorem 2. Let ν (m) := E p (m)2 , N′ := N + n and y (m) = (y (m) , . . . , y (m) ). Then
i i i 1,i s,i
(cid:18) (cid:19)
ν (1) = p i + 1 − 1 p2
i N N i
and for m ≥ 2
(cid:32) (cid:33)2 (cid:32) (cid:33)2 
ν (m) = 1 E  ∑ N y (0) + ∑ n y (m−1) + 2 ∑ N ∑ n y (0) y (m−1) 
i N′2 i,k i,k i,k i,k
k=1 k=1 j=1 k=1
= 1 (cid:104) N p + (N2 − N)p2 + np + (n2 − n)ν (m−1) (cid:105) + 2 ∑ N ∑ n E (cid:104) y (0) y (m−1) (cid:105)
N′2 i i i i N′2 i,j i,k
j=1 k=1
= p i + N2 − N p2 + n2 − n ν (m−1) + 2 ∑ N ∑ n E (cid:104) y (0) y (m−1) (cid:105) . (15)
N′ N′2 i N′2 i N′2 i,j i,k
j=1 k=1
For m ≥ 2, since y
(m−1)
is conditionally independent of y
(0)
given p
(m−1)
, by conditioning
i,k i,j i
(0) (m−1)
on y and p we have
i,j i
(cid:104) (cid:105) (cid:104) (cid:105)
E y (0) y (m−1) = E y (0) p (m−1)
i,j i,k i,j i
and hence for m ≥ 2,
ν (m) = p i + N2 − N p2 + n2 − n ν (m−1) + 2n ∑ N E (cid:104) y (0) p (m−1) (cid:105) .
i N′ N′2 i N′2 i N′2 i,j i
j=1
15

By the definition of p
(m)
, for m ≥ 3
i
(cid:34) (cid:35) (cid:34) (cid:35)
E (cid:104) y (0) p (m−1) (cid:105) = 1 E y (0) ∑ N y (0) + 1 E y (0) ∑ n y (m−2)
i,j i N′ i,j i,k N′ i,j i,k
k=1 k=1
= p i + (N − 1)p2 i + n E (cid:104) y (0) p (m−2) (cid:105)
N′ N′ i,j i
and
E (cid:104) y (0) p (1) (cid:105) = 1 p + (cid:18) 1 − 1 (cid:19) p2 = p i + (N − 1)p2 i
i,j i N i N i N
which gives
E (cid:104) y (0) p (m−1) (cid:105) = 1 − (cid:0) N n ′ (cid:1)m−2 p i + (N − 1)p2 i + (cid:16) n (cid:17)m−2 E (cid:104) y (0) p (1) (cid:105) .
i,j i 1 − n N′ N′ i,j i
N′
Setting α := n/N′, we have N = (1 − α)N′ and hence
E (cid:104) y (0) p (m−1) (cid:105) = p i + (N − 1)p2 i
i,j i N
for all m ≥ 2. Plugging this back to the expression (15) for ν
(m)
gives
i
ν (m) = (1 − α)(1 + 2α) p + (cid:18) 1 − 1 (cid:19) (1 − α2)p2 + α (cid:20)(cid:18) 1 + 1 (cid:19) α − 1 (cid:21) ν (m−1) .
i N i N i N N i
(cid:104)(cid:16) (cid:17) (cid:105)
Let β := α 1 + 1 α − 1 . Then for m ≥ 1,
N N
ν
(m+1)
=
1 (cid:20) 1 − βm+1
− α(2 − α)
1 − βm (cid:21)
p
i N 1 − β 1 − β i
(cid:18) 1 (cid:19) (cid:20) 1 − βm+1 1 − βm (cid:21)
+ 1 − − α2 p2
N 1 − β 1 − β i
= N 1 p i (cid:20) 1 + 2α − (cid:18) 1 − 1 (cid:19) αβm (cid:21)
1 + (1 + 1/N)α N
(1 − 1 )p2 (cid:20) 1 (cid:21)
+ N i 1 + α − αβm
1 + (1 + 1/N)α N
and summing across i ∈ [s] gives the expression for S m+1 .
Note that 0 < β < α < 1, which gives both an upper bound and a lower bound on ν
(m)
. In
i
particular, for m ≥ 2
(cid:20) (cid:18) (cid:19) (cid:21)
ν (m) < 1 1 (1 + 2α)p + 1 − 1 (1 + α)p2
i 1 + (1 + 1/N)α N i N i
and therefore
(cid:20) (cid:18) (cid:19) (cid:21)
1 1 1
S < (1 + 2α) + 1 − (1 + α)S
m 1 + (1 + 1/N)α N N 0
(cid:16) (cid:17)
1 − 1 (1 + α)(1 − S )
N 0
= 1 − ,
1 + (1 + 1/N)α
where
(cid:16) (cid:17)
1 − N 1 (1 + α)(1 − S 0 ) (cid:20) 1 + α (cid:21)
γ := ∈ (1 − S ), 1 − S
1 + (1 + 1/N)α 2 + 3α 0 0
since 0 ≤ 1/N ≤ 1/2.
16

We state a more general result which implies Theorem 3.
Theorem 4. Let G (s) and φ be as in Lemma 1. Then for k ≥ 1 we have
n
(cid:114)
1 nπ
E∥p (k+1) − p (1)∥ < G (s), (16)
1 N φ(ζ) n
where
1
(cid:18)
1
(cid:20) (cid:21)(cid:19) (cid:18)
N
(cid:19)2
ζ = − − 2E max p (1)(A)p (1)([s] \ A) .
2 2 A⊆[s] N + n
Proof of Theorem 4. Since all generations share the same original data source, we can write
p (k+1) = N p (1) + n p(cid:100)(k), where p(cid:100)(k) = 1 ∑ n y (k) (17)
N + n N + n n i
i=1
and {y i (k) } i=1,...,n are i.i.d. multinomial with parameter p(k) and one trial (k ≥ 1). This gives
n (cid:104) (cid:105)
p (k+1) − p (1) = p(cid:100)(k) − p (1) ,
N + n
and applying the triangle inequality yields
n (cid:13) (cid:13) n (cid:13) (cid:13) n (cid:13) (cid:13)
∥p (k+1) − p (1)∥ = (cid:13)p(cid:100)(k) − p (1)(cid:13) ≤ (cid:13)p(cid:100)(k) − p (k)(cid:13) + (cid:13)p (k) − p (1)(cid:13) .
1 N + n (cid:13) (cid:13) 1 N + n (cid:13) (cid:13) 1 N + n (cid:13) (cid:13) 1
Taking the expectation and solving the recursion gives for k ≥ 1
E∥p (k+1) − p (1)∥ ≤ ∑ k (cid:18) n (cid:19)k+1−j E (cid:13) (cid:13)p(cid:100)(j) − p (j) (cid:13) (cid:13) . (18)
1 N + n (cid:13) (cid:13) 1
j=1
From Lemma 1, we have
(cid:32) (cid:12) (cid:33)
(cid:13) (cid:13) (cid:12)
P (cid:13)
(cid:13)
p(cid:100)(k) − p (k)(cid:13)
(cid:13)
≥ t (cid:12)
(cid:12)
p (k) ≤ G
n
(s)e −nφ(πk )t2/4
1 (cid:12)
where π := π . Integrating over t ∈ [0, ∞), we get
k p(k)
(cid:34) (cid:12) (cid:35)
(cid:13) (cid:13) (cid:12) (cid:114) π
E (cid:13)p(cid:100)(k) − p (k)(cid:13) (cid:12)p (k) ≤ G (s) ,
(cid:13) (cid:13) 1 (cid:12) (cid:12) n nφ(π k )
and by Jensen’s inequality and the concavity of x (cid:55)→ φ(x)−1/2,
(cid:13) (cid:13) (cid:114) π (cid:104) (cid:105) (cid:114) π
E (cid:13)p(cid:100)(k) − p (k)(cid:13) ≤ G (s)E φ(π )−1/2 ≤ G (s).
(cid:13) (cid:13) 1 n n k nφ(Eπ k ) n
Thus
E∥p (k+1) − p (1)∥ 1 ≤ (cid:114) π n G n (s) j ∑ = k 1 (cid:18) N n + n (cid:19)k+1−j (cid:113) φ( 1 Eπ j ) . (19)
It remains to upper upper bound Eπ since φ is decreasing. For A ⊆ [s] let Ac denote its
j
complement. Then by (17), for A ⊆ [s] we have
N2 n2
p (k+1)(A)p (k+1)(Ac) = p (1)(A)p (1)(Ac) + p(cid:100)(k)(A)p(cid:100)(k)(Ac)
(N + n)2 (N + n)2
Nn (cid:104) (cid:105)
+ p (1)(Ac)p(cid:100)(k)(A) + p (1)(A)p(cid:100)(k)(Ac)
(N + n)2
N2 n2 Nn
≤ p (1)(A)p (1)(Ac) + p(cid:100)(k)(A)p(cid:100)(k)(Ac) + .
(N + n)2 (N + n)2 (N + n)2
17

Let λ := max p(k)(A)p(k)(Ac), so the inequality above implies
k A⊆[s]
(cid:34) (cid:12) (cid:35)
N2 n2 (cid:12) Nn
E[λ k+1 | p (1) , p (k)] ≤ (N + n)2 λ 1 + (N + n)2 E A m ⊆ a [ x s] p(cid:100)(k)(A)p(cid:100)(k)(Ac)(cid:12) (cid:12) (cid:12) p (k) + (N + n)2
N2 n2 Nn
≤ λ + +
(N + n)2 1 4(N + n)2 (N + n)2
and thus
N2E[λ ] + Nn + n2/4 1 (cid:18) 1 (cid:19) (cid:18) N (cid:19)2
E[λ k+1 ] ≤ ( 1 N + n)2 = 4 − 4 − E[λ 1 ] N + n .
Observe that for 0 ≤ x ≤ 1 we have min(x, 1 − x) ≤ 2x(1 − x), so E[π ] ≤ 2E[λ ]. Writing
k k
1
(cid:18)
1
(cid:19) (cid:18)
N
(cid:19)2
ζ := − − 2E[λ ]
2 2 1 N + n
we have E[π ] ≤ ζ, so from (19) we see that
k
E∥p (k+1) − p (1)∥ ≤ (cid:114) π G (s) ∑ k (cid:18) n (cid:19)k+1−j < 1 (cid:114) nπ G (s). (20)
1 nφ(ζ) n N + n N φ(ζ) n
j=1
Proof of Theorem 3. Theorem 3 is an immediate consequence of Theorem 4 by replacing φ
with its minimum value 2.
C Architecture & training parameters for GPT2 experiments
We consider that all generation models have GPT2-type4 vanilla architecture which is a
decoder-only generative model with the configuration and training parameters as summarized in Table 1. These parameters were chosen to achieve the best validation loss when
training the first-generation model on data produced by ground-truth generative model
p(0) as defined in Section 4.1.
Context length 128
Embedding dimension 256
Number of layers 8
Number of self-attention heads 4
Vocabulary size 65
Dropout 0.2
Learning rate 10−3
Batch size 256
Max iterations 2000
Table 1: Architecture and training parameters in the setting of Section 4.1.
4https://github.com/karpathy/nanoGPT
18
