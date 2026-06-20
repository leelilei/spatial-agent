---
telephone_index: 51
title: "Simulating Misinformation Vulnerabilities With Agent Personas"
category: 05_misinformation_correction
venue: "2025 Winter Simulation Conference (WSC)"
year: 2025
doi: 10.1109/wsc68292.2025.11338973
arxiv_id: 2511.04697
preferred_source_type: conference
publisher_url: https://doi.org/10.1109/wsc68292.2025.11338973
quality_flags: []
---

# Citation Context

- Telephone index: 51
- Preferred source: 2025 Winter Simulation Conference (WSC)
- DOI: 10.1109/wsc68292.2025.11338973
- arXiv: 2511.04697
- PDF: `assets\papers\pdf\05_misinformation_correction\51_simulating-misinformation-vulnerabilities-with-agent-personas.pdf`

## Extracted Abstract

Disinformation campaigns can distort public perce different populations respond to information is cruc experimentation is impractical and ethically chall simulation using Large Language Models (LLMs) agent personas spanning five professions and three headlines. Our findings show that LLM-generated a predictions, supporting their use as proxies for stu schemas, more than professional background, influ provides a validation of LLMs to be used as agen for analyzing trust, polarization, and susceptibility
Title: Simulating Misinformation Vulnerabilities With Agent Personas

Source PDF: D:\0-Research\5-Telephone\assets\papers\pdf\05_misinformation_correction\51_simulating-misinformation-vulnerabilities-with-agent-personas.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-06-20T12:44:52+00:00
- page_count: 12
- status: ok
- text_char_count: 43531

Metadata:
- author: David Farr; Lynnette Hui Xian Ng; Stephen Prochaska; Iain J. Cruickshank; Jevin West
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- INTRODUCTION (page 1)
- RELATED WORK (page 2)
  - Information Operations (page 2)
  - Simulation with AI agents (page 3)
- Methodology (page 3)
  - Agent Personas (page 3)
  - Misinfo Reaction Frames corpus (page 4)
  - LLM-Based Simulation (page 5)
- Results (page 5)
  - GPT Simulation (page 5)
  - LLaMA Simulation (page 6)
  - Propensity to Share (page 7)
- Discussion (page 7)
- Conclusion (page 9)
- APPENDICES (page 10)
  - Agent Prompts (page 10)

Markdown Content:

Proceedings of the 2025 Winter Simulation Conference
E. Azar, A. Djanatliev, A. Harper, C. Kogler, V. Ramamohan, A. Anagnostou, and S. J. E. Taylor, eds.
SIMULATING MISINFORMATION VULNERABILITIES WITH AGENT PERSONAS
David Farr1, Lynnette Hui Xian Ng2, Stephen Prochaska1, Iain J. Cruickshank2, and Jevin West1
1School of Information Science, University of Washington, Seattle, WA, USA
2School of Computer Science, Carnegie Mellon University, Pittsburgh, PA, USA
5

ABSTRACT
Disinformation campaigns can distort public perce
different populations respond to information is cruc
experimentation is impractical and ethically chall
simulation using Large Language Models (LLMs)
agent personas spanning five professions and three
headlines. Our findings show that LLM-generated a
predictions, supporting their use as proxies for stu
schemas, more than professional background, influ
provides a validation of LLMs to be used as agen
for analyzing trust, polarization, and susceptibility
1 INTRODUCTION
Protection against foreign information campaigns an
are critical to modern national security. In an era
battlefield, there is a need to maintain information ad
of information to achieve objectives more effectively
the Army 2023). Achieving and sustaining informati
compelling narratives but also to detect, counter, an
Foreign adversaries and non-state actors use in
to manipulate public perception, destabilize institu
2019; Bradshaw and Howard 2018). These campai
and shape operational environments before confli
Zhou, Wenqi and Carley, Kathleen M 2024). Altho
provide valuable information on population-based
the dynamic and adaptive nature of these operation
and policymakers.
Real-world experimentation on populations is e
based approaches a critical alternative for research an
ability to allow for exploration of diverse scenarios,
advancements in generative AI and agent-based mo
operations in a controlled and scalable manner. By e
ideological frames, and cognitive biases, we can si
competing narratives. Framing theory, which explo
based on preexisting beliefs, provides a robust foun
susceptibility, and counter-messaging strategies (K
able to produce believable simulations of human
5202
tcO
13
]IS.sc[
1v79640.1152:viXra

on and destabilize institutions. Understanding how
for designing effective interventions, yet real-world
ing. To address this, we develop an agent-based
model responses to misinformation. We construct
ental schemas, and evaluate their reactions to news
ts align closely with ground-truth labels and human
ng information responses. We also find that mental
ce how agents interpret misinformation. This work
n an agent-based model of an information network
deceptive content in complex social systems.
he ability to conduct effective information operations
ere the information domain can be leveraged as a
tage, defined as “the use, protection, and exploitation
an enemies and adversaries do" (U.S. Department of
advantage requires not only the ability to disseminate
mitigate adversarial information operations.
mation campaigns, which are sustained operations,
ns, and degrade military readiness (Starbird et al.
often exploit cognitive biases, fracture public trust
manifest kinetically (Ng, Lynnette Hui Xian and
case studies of previous disinformation operations
ctions (Reuter et al. 2019; Tandoc Jr et al. 2020),
resents a significant challenge for military planners
ally and strategically untenable, making simulationperational planning with an added advantage of their
ameters, and numerous trials (Epstein 2008). Recent
ing present new opportunities to study information
ding AI-driven agents with distinct mental schemas,
ate how different populations perceive and react to
how individuals process and interpret information
ion for modeling adversarial messaging, population
et al. 2007). LLM agents have been shown to be
ractions in social environments (Park et al. 2023;

Farr, Ng, Prochaska
Aher et al. 2023), and responses from LLM-based s
experiments (Filippas et al. 2024). Integrating AI
to test information environment scenarios, evaluate
engagement strategies.
This paper enables the systematic study of inform
techniques into Large Language Model (LLM)-b
simulate responses of different demographics towa
use LLM-agents as a proxy to simulate responses
examine population-based reactions to misinformat
misinformation-combating strategies.
2 RELATED WORK
2.1 Information Operations
Information operations take many forms, ranging
sophisticated, long-running campaigns that take adv
online social networks and amplify divisions (Sha
information operations are heavily participatory, in
often believe that content to be true or reliable, l
misleading narratives (Starbird et al. 2019). These
campaigns, making the boundaries of any given op
tactics have ripple effects outside of the direct cont
campaigns often includes a mix of true, false, and
make sense of novel or ambiguous events or inform
In order to better identify and understand inform
aspects of such operations, which are sometimes buc
content (François 2019). Each of these categories
paper, we focus primarily on content and actors.
strategic content is the difficulty in identifying the
pre-existing divisions within a target population (B
targeting these divisions, operations often seek to im
or expectations in order to appear more authentic (A
authentic and inauthentic activity such that detectio
authentic and inauthentic content being very simila
This type of participation has become an integ
seek to guide or interrupt audiences as they seek to m
2023; Starbird et al. 2025; Prochaska et al. 2025).
interpret the same facts differently, allowing online i
strategic content and interpretive frames (which h
Klein et al. 2007)) that align with a specific audie
this work, attempting to simulate members of partic
audiences might interpret the same facts different
misinformation that includes the complex milieu of
would actually interact with were they to come into
work has identified that common vectors for false
outlets and/or misleading headlines and stories (G
Although campaigns often combine such headlines
of a campaign for our simulation as we are focused
diverse audience interpretations of misleading cont

uickshank, and West
ulations have strong correlations with human subject
nts into disinformation simulations allows analysts
sinformation resilience, and optimize civil-military
on competition by incorporating cognitive modeling
d simulations. We use LLM-generated agents to
misinformation. We build on previous work and
m population groups. Through our simulation, we
, which enables better formulation and targeting of
om bot networks amplifying simple messages to
age of pre-existing prejudices and biases to infiltrate
t al. 2018; Arif et al. 2018; Rid 2020). Modern
t publics engaging with strategically seeded content
ing them to amplify it and further spread false or
nwitting agents” are key to the spread of influence
ion difficult to determine as the impacts of specific
of strategists (Rid 2020). Moreover, the content of
leading content to overwhelm audiences’ ability to
on (Bittman 1985; Rid 2020).
on operations, researchers have focused on different
ed into three primary groups: actors, behaviors, and
ssential to any given operation, but for the current
e of the primary challenges facing the detection of
oundaries of an operation due to their targeting of
man 1985; Ellul 1973; Rid 2020). In the process of
sonate or mimic people who fit particular stereotypes
et al. 2018). This muddies the distinction between
as to rely on multiple signals simultaneously due to
part of modern influence campaigns, as strategists
e sense of novel or ambiguous events (Starbird et al.
cent work has highlighted how different audiences
uencers to opportunistically engage with and amplify
also been referred to as schemas (Goffman 1974;
’s expectations (Starbird et al. 2025). We leverage
r audiences in order to better understand how those
In order to do so, we take a broad definition of
e, false, and misleading information that audiences
ntact with an online information operation. Previous
misleading information include unreliable media
berg et al. 2019) (see also (Bozarth et al. 2020)).
stories with other tactics, we focus on this aspect
imarily on testing the ability of models to simulate

Farr, Ng, Prochaska
2.2 Simulation with AI agents
Recent research has made notable strides in usin
of information on social systems. Agents construc
human-like behavior and social interactions, and can
et al. 2023). For example, LLMs can function as a
propagation of rumors (Hu, Tianrui and Liakopoulo
Yadwadkar, Neeraja J 2025). We extend this past w
behavior, and incorporate real-world misinformatio
with human perceptions of misinformation.
Our agent-based modeling approach draws fr
information processing done by individual humans
and environmental influences (Bandura 2009; Ng an
can significantly predict susceptibility to fake news (
our work incorporates human mental schemas that ca
rather than simply focusing on adjusting the model
Simulating more realistic agent characteristics
emergence of news spread and the effect of netw
and Xu, Yu and Zhang, Yongfeng and Malthouse,
misinformation sharing patterns. Researchers, for ex
a propensity to share false content (Mosleh et al.
with real-world misinformation reaction, we build
based on susceptibility to misinformation.
Further, role-based adjustments in ChatGPT
detection (Haupt et al. 2024), emphasizing the co
perspectives into LLMs. Such experiments help us
the nuanced ways in which biases in agent roles af
Much of the past research that uses LLMs as
network topology and prompt modifications. Some
to simulate diverse human perspectives on political
and Gui, Fred and Yang, Hongjia and Yu, Chenxia
Junlong Aaron and Shen, Bolin and others 2025), w
ideological spectrums. We bridge a research gap b
agents with the mental schemas that humans have,
information environments. To do so, we simulat
enabling a more interpretable comparison across di
3 METHODOLOGY
Figure 1 provides an overview of our simulation s
corpus is read by LLM-Agent Personas that are co
These personas respond to the headline with their
is a misinformation news. Their responses are com
provided by the corpus as well as other agents.
3.1 Agent Personas
To ensure a diverse range of perspectives in our sim
simulate these personas through LLMs. Each agent
or a relevant mental schema. The selection of the

uickshank, and West
anguage models as agents to simulate the spread
from generative AI models can simulate realistic
erefore be used for modeling information flow (Park
nts to assess the impact of network structure on the
imitrios and Wei, Xiwen and Marculescu, Radu and
k and compare the results of LLM-agents to human
eadlines, finding that LLM-agents can closely align
social cognitive theory, which suggests that the
n be shaped by personal factors, behavioral patterns
arley 2022). In fact, individual cognitive differences
nnycook and Rand 2019). Building on this literature,
ffect an individual’s susceptibility to misinformation,
behavior through instructions.
uch as job titles and personality traits, can show
topology on information dissemination (Li, Xinyi
dward C 2024). Social media users exhibit variant
ple, have shown that personality traits correlate with
1). To align the human decision-making processes
prior work and simulate mental schemas that vary
mpts can impact the accuracy of misinformation
lexities involved in integrating biases and multiple
entangle these complexities and provide insight into
misinformation detection performance.
ents for simulating information spread focuses on
ork indicate that LLMs can be effectively prompted
ourse (Li, Lincan and Li, Jiaqi and Chen, Catherine
nd Wang, Zhengguang and Cai, Jianing and Zhou,
ch allows the study of polarization dynamics across
imulating diverse humans to align LLM-generated
essential factor that is representative of real-world
LM-agents with mental schemas and professions,
ent sets of headlines and messages.
em. A headline from the Misinfo Reaction Frames
ucted of different professions and mental schemas.
ief in the headline, and the likelihood the headline
ed with the gold labels and human predicted labels
tion, we designed eight distinct agent personas. We
rsona represents a specific professional background
agents was driven by their potential susceptibility

Farr, Ng, Prochaska
Figure 1: Overview of simulating reactions
or targeting in adversarial information campaigns
professions and mental schemas.
Agent personas based on professions are: (1) m
of influence campaigns aimed at undermining mora
John D and Barash, Vlad and Howard, Philip N
have a historical role in political activism and the
demographic for grassroots and state-sponsored in
persons, representing the group of older adults that
a group that disproportionately engages and shares
industrial workers to present a blue-collar viewpoi
viewpoint, allowing how disinformation targeting l
In addition to profession-based roles, we introd
different cognitive responses to misinformation. Th
receptive to conspiracy narratives and amplify frin
susceptible agent that represents individuals who ar
prone to misinformation; (3) normal persons who
assess how an individual with no strong predisposi
By incorporating this combination of occupation
provides a robust framework for analyzing how
misinformation. We did not introduce explicit agent
interpretation. This was a deliberate design choice
approach enables us to assess not only the effecti
intervention strategies to mitigate their impact in di
for creating the agents are available in Appendix 2
3.2 Misinfo Reaction Frames corpus
We use the Misinfo Reaction Frames corpus to test
et al. 2022). This corpus captures both the factual ac
to misinformation. The test dataset consists of 2
discourse and national security concern, including C
Each headline was fact-checked by researchers and a
or trustworthy information.
Beyond factual classification, the dataset uniqu
ularly suited for simulating real-world information
headline was evaluated by 63 human annotators r
annotations on:

uickshank, and West
misinformation by different agent personas.
These personas are divided into two main groups:
ary personnel or soldiers, who are frequent targets
eadiness, or battlefield decision-making (Gallacher,
Kelly, John 2018); college students, a group that
rly adoption of emerging narratives, and are a key
ence efforts (Levine and Hirsch 1991); (3) retired
frequently identified in misinformation research as
sleading content (Brashier and Schacter 2020); (4)
(5) financial analysts for a contrasting white-collar
r or socioeconomic groups resonate differently.
d agent personas based on mental schemas to model
schemas are: (1) conspiracy-believer that is highly
heories into mainstream discourse; (2) conspiracyot fully embedded in conspiracy thinking but remain
ads the news as a neutral baseline, allowing us to
ns engages with the misinformation content.
oles and cognitive frames, our agent-based simulation
ferent demographics process, propagate, or resist
as in prompting and instead relied on implicit model
at could be altered or studied in future work. This
ess of disinformation campaigns but also possible
se populations. The full details of the prompts used
ent reactions towards misinformation news (Gabriel
racy of news content and human cognitive responses
2 news headlines covering key domains of public
VID-19, climate change, and cancer misinformation.
gned a binary classification as either misinformation
incorporates human reaction data, making it particironments, and therefore our simulation task. Each
uited via Amazon Mechanical Turk, who provided

Farr, Ng, Prochaska
• Perceived veracity – Whether they believed
• Emotional response – The dominant emotio
• Propensity to share – A Likert-scale rating
social media.
The cognitive and behavioral characteristics
emotional engagement, and likelihood of amplific
based simulations of digital influence operations.
solely on factual accuracy, this data set allows model
campaigns, which narratives are spread most effecti
demographic and ideological groups.
By incorporating these human-centered respon
complex social dynamics of digital information war
labels or probability based susceptibility, offering in
characteristics to spread disinformation.
3.3 LLM-Based Simulation
For each agent persona, we provided a headline fr
asked the agent two questions: (a) if the agent think
of the agent persona to share the information on a
(b) with human annotator predictions and ground t
In our experiments, we utilized the LLaMA
simulation performance across both models. GPT-4
(RLHF) model and LLaMA is a smaller, open-sour
represent different scales of model architecture. Bo
which minimizes randomness in token selection an
Temperature controls the level of randomness in the
choose the highest-probability token at each step, rat
For GPT-4, a logit bias of 10 was applied to each t
us to artificially increase the likelihood of selecting
before the final softmax step, effectively steering th
optimize GPT-4’s responses to the simulation task.
4 RESULTS
4.1 GPT Simulation
In our simulations using GPT, we consistently obs
across different professional domains. This finding e
significantly, such as financial workers and industr
and military personnel. However, there were nota
various mental schemas, which consist of personas
headlines or users that identify with conspiracy theo
in Figure 2 there is little agreement (0.53) between
less agreement (0.33) between agents that were con
the different mental states affect the difference in r
One interesting observation was that promptin
highest overlap in annotations with human annota
identifying misinformation. This suggests that a m

uickshank, and West
e headline to be real or fake.
licited by the headline (e.g., fear, anger, trust).
how likely they would be to share the headline on
he dataset that measures the perception of truth,
on, provide critical parameters for building agentlike traditional misinformation datasets that focus
of how different audiences respond to disinformation
y, and how misinformation resilience varies between
ariables, our simulation can better approximate the
than simulations purely based on alignment to gold
hts into how adversaries exploit different population
the Misinfo Reaction Frames Corpus dataset. We
e news headline is real, and (b) to rate the likelihood
Likert scale. We compare the results from (a) and
labels from the original data.
8B Instruct and GPT-4 models and compare the
larger reinforcement learning with human feedback
model suitable for local execution. The two models
models were run with a temperature setting of zero,
nsures more deterministic and reproducible outputs.
odel’s predictions; a value of zero makes the model
than sampling from the full probability distribution.
n in our constrained set of labels. Logit bias allows
ecific tokens by adding a fixed value to their logits
model toward those tokens. This adjustment helped
l prompts are used are shown in Table 2.
e an ability of the agents to detect misinformation
apolates to professions that can be assumed to differ
workers, or groups such as young college students
differences when agents were prompted with the
ere agents were more susceptible to alternative news
s. As shown in the GPT-Generated Agents heatmap
ents that were conspiracy and susceptible, and even
racy and normal. These observations suggests that
onse to misinformation more than professions do.
PT as a neutral news reader (normal) leads to the
, resulting in the best performance on the task of
e neutral, unbiased approach may better align with

Farr, Ng, Prochaska, Cruickshank, and West
Figure 2: Heatmap of annotation agreement between LLM-generated agents on identifying whether a news
headline constitutes misinformation.
human decision-making processes in misinformation detection and that GPT is relatively well aligned with
human perceptions of misinformation.
Out of the eight GPT generated agent annotators, six outperformed human annotators in identifying
misinformation, achieving over 63% accuracy (Figure 3). However, as shown in Figure 2 under GPTGenerated Agents, there were significant differences in agreement between agent annotators. In particular,
the conspiracy-driven and susceptible agents demonstrate a stronger tendency to classify misinformation
as true. Interestingly, even among agents who only differed in profession (e.g., financial workers versus
industrial workers), there were notable disagreements in their assessments of information truthfulness.
Although the overall precision of the identification of misinformation was similar, the agreement on
individual data points had a difference of 10% (Figure 2).
4.2 LLaMA Simulation
In contrast to GPT, the simulation using the LLaMA model for agent persona generation exhibited much
greater variance in performance. As with GPT, the neutral news reader (normal) agent yielded the highest
classification performance and most closely mirrored the human annotations. As shown in the LlaMaGenerated agent heatmap in Figure 3, five of the eight LLaMA agents outperformed human annotators in
identifying misinformation (more than 63% accuracy), although their performance was worse than that of
the GPT agents.
Additionally, the LLaMA agents did not align with human annotations as frequently as GPT agents did,
suggesting that LLaMA’s outputs are less consistent in terms of reflecting human annotation judgment. The
observed variance in responses among the LLaMA agents could be interpreted as a useful representation
of the diversity of perspectives that exist among individuals in the information environment, but additional
fine-tuning should be done in future work to better align agent behavior with human interpretation.
We compare the similarity of the responses of whether the LLM-generated agents think that the input
headline is real in two forms: the LLM-generated agents within each LLM-model, and the LLM-generated
responses against the gold labels and human annotator judgments.
Figure 2 shows the agreement heatmap of LLM-generated agents towards whether a news headline
constitutes misinformation. LLaMA-generated agents exhibit greater variance than GPT-generated agents
outcomes across both professions and mental schemas. Agents assigned different professions exhibited
largely similar interpretations of information (e.g., finance vs college), whereas altering the agents’ mental

Farr, Ng, Prochaska
Figure 3: Comparison of LLM-generated agent pred
LLM Model versus gold shows the comparison of
and GPT vs Pred shows the comparison of each in
schemas (e.g. conspiracy vs normal) led to signific
versus real information.
Figure 3 compares the LLM-generated agent pre
The gold labels and human judgments are provided i
agents align more closely with gold labels than wi
in identifying misinformation. The agents’ simila
agents can serve as effective proxies to simulate re
LLaMA-generated agents effectively identify misin
alignment with human predictions. Additional tuni
human perception, especially when using role prom
4.3 Propensity to Share
Figure 4 compares the Likert scale ratings of the l
agents and human annotators. Although most AI age
with significant schema adjustments, such as suscep
showing a higher propensity to share information,
their sharing likelihood into common response categ
with human annotators, whose Likert ratings are mo
most often choose a medium likelihood rating (i.e.,
human annotators would need to be categorized u
agents accurately mimic their representative human
agents and Likert responses, agent behavior appear
5 DISCUSSION
Our findings indicate that LLM-simulated agents l
annotated predictions in their interpretations of mis

uickshank, and West
ions to gold labels and human annotator judgments.
h individual LLM-based agent to gold annotations
dual LLM-based agent to human predictions.
variations in their classifications of misinformation
tions to gold labels and human annotator judgments.
e original Misinfo Reaction Corpus. GPT-generated
human annotators and demonstrate higher accuracy
to human predictions suggest that GPT-generated
onses to misinformation. On the other hand, while
mation based on gold labels, they exhibited limited
might be necessary to enhance their alignment with
ng to understand responses of diverse perspectives.
ihood to share news headlines between GPT-based
show general alignment with human ratings, agents
e and conspiracy agents, exhibit notable deviations,
uding misinformation. These agents tend to cluster
es, regardless of the specific headline. This contrasts
evenly distributed across the scale, though they still
oice three of five). For a more nuanced comparison,
g the same schema as the agents to assess whether
unterparts. Nonetheless, when averaging across all
resemble overall human patterns.
ely align with both ground truth labels and humanormation. However, most agent types deviated from

Farr, Ng, Prochaska, Cruickshank, and West
Figure 4: Bar plot comparing Likert scale ratings of the likelihood to share news headlines, as assessed by
LLM agents and human annotators with 1 being not at all likely and five being extremely likely. Agents
tend to cluster toward the middle of the Likert scale where humans seem to be more evenly distributed.
human norms when it came to sharing behavior. While human annotators exhibited a relatively even
distribution across the Likert scale for likelihood of sharing, simulated agents tended to cluster around
a moderate likelihood. The type of language model used to simulate agents significantly affected the
variance in misinformation labeling and the degree of agreement both among agents and between agents
and humans. Notably, GPT-based agents exhibited lower inter-agent variance and greater alignment with
human judgments, which we interpret as a strength, reflecting the diversity and complexity of real-world
information environments through variance in interpretation while preserving alignment. These results
suggest that LLM-simulated agents can serve as effective proxies for analyzing human responses to
misinformation. Table 1 provides sample responses indicating whether the simulated agent persona judged
a headline as real or as misinformation.
A key finding of our experiments is that an agent’s interpretation of information was more strongly
influenced by mental schemas than by professional background. While responses were relatively consistent
across different professions, significant differences emerged when agents were prompted with varying
cognitive predispositions, such as susceptibility to alternative news sources or belief in conspiracy theories.
In fact, compared to the normal agent persona, the conspiracy and susceptible persona performs worse in
detecting misinformation, showing that pre-existing beliefs can distort a person’s information processing.
This is in line with the phenomenon of confirmation bias or motivated reasoning. This insight underscores the
importance of tailoring misinformation intervention strategies to cognitive and ideological predispositions
rather than professional affiliations. This finding also has practical implications for misinformation mitigation
efforts. Rather than designing interventions that target individuals based on profession, strategies may want
to focus on addressing the underlying cognitive biases that contribute to susceptibility.
From a methodological perspective, our work establishes a pipeline for systematically creating agent
personas and simulating their responses towards misinformation news headlines. This simulation framework
creates a controlled environment that allows isolation of specific cognitive and profession-based characteristics that might affect susceptibility to misinformation. The framework also allows for rapid iteration
and large scale testing across population slices that will be difficult to implement with human studies like
surveys.

Farr, Ng, Prochaska
Table 1: GPT-Generated Agent responses towards
bold items means the responses agree with the Go
where there was large disagreement among agents
by the conspiracy agent correctly classifying many
Headline/Agent Ukrainian AP: Five years
Category schools will be on, Paris
closed as climate accord
lockdown working; CO2
measure emissions
dropped 17%
this year
Gold misinfo misinfo
Predicted real real
College misinfo real
Industrial misinfo real
Financial real real
Retired real real
Military real real
Standard real real
Susceptible real misinfo
Conspiracy misinfo misinfo
Beyond misinformation detection, our approach
for studying broader information dynamics. The a
searchers to analyze how different demographic and c
in digital spaces. This technique could extend to app
and susceptibility to other forms of deceptive conte
Further, from a national security perspective, unders
and sharing of population segments (i.e., professio
targeted counter-disinformation efforts such as edu
be tailored towards each mental schema for better
Limitations and Future Work Our study on
indicated good alignment with the gold label and
construction of agent personas with different LLM
tween the agent personas constructed from differe
mental schemas can be incorporated into the agent
personas. Nonetheless, this work offers a prelimina
misinformation of different personas and their alig
6 CONCLUSION
In this study, we constructed multiple agent persona
their responses to misinformation headlines. Our res
approximate human decision-making patterns in
susceptibility based on cognitive predisposition rat
Our study highlights the value of LLM-based
misinformation spread. By simulating diverse per
strategies, study information propagation dynamics,
efforts at scale.

uickshank, and West
o you think this is a real news headline?" question.
labels. This table was designed to show examples
d is not representative of agent accuracy, as shown
ficult headlines.
Siberian Envi- How climate CBS: Too
ronmentalist change could Many ’Thank
Detained for benefit Russia You’ Emails
Poaching Contribute to
World’s Largest Global
Sheep Warming
real real misinfo
real misinfo misinfo
misinfo misinfo misinfo
misinfo misinfo misinfo
misinfo misinfo misinfo
misinfo misinfo misinfo
misinfo misinfo misinfo
misinfo real misinfo
misinfo real real
real real real
hlights the potential of LLM-based agent simulations
ty to model and test different personas enables renitive groups interact with and propagate information
ations such as assessing polarization, trust in media,
including deepfakes and AI-generated propaganda.
ding the susceptibility towards misinformation belief
mental schemas) allows for more precise design of
onal materials. Specific interventions may need to
ctiveness.
nvestigated two LLMs, and while these two models
uman annotations, future work can investigate the
even comparing the similarity and differences beLLMs. Further, a larger range of professions and
sona construction to showcase a wider diversity of
investigation into measuring the responses towards
ent with human predictions.
sing Large Language Models (LLMs) and evaluated
s indicate that LLM-simulated agents can effectively
information detection, with a notable variance in
than professional backgrounds.
nts as a tool for understanding the mechanisms of
as, researchers can systematically test intervention
d assess the effectiveness of counter-misinformation

Farr, Ng, Prochaska, Cruickshank, and West
As the digital information landscape continues to evolve, the ability to simulate complex humanlike responses with multi-agent frameworks presents opportunities to create robust disinformation defense
strategies through a more realistic information environment than was previously possible. Future works
should explore additional model architectures, fine-tuning methods, and real-world behavioral comparisons
to refine accuracy and applicability of these simulations. Integrating LLM-based agent modeling into
misinformation research can provide insights into how misinformation spreads, what populations are
particularly vulnerable to specific messaging types, and how to counteract its effects in an increasingly AI
driven information environment.
A APPENDICES
A.1 Agent Prompts
Table 2 lists the agent prompts used for each profession and mental schema. The design decision was made
to not impose explicit biases in the prompt of profession traits and instead let the agent impose those traits
itself.
Table 2: Referenced agents and their system prompts.
Agent Name System Prompt
Soldier "You are a young enlisted soldier and read the following headline:
HEADLINE Did you believe the headline?""
College Student "You are a politically active college student and read the following
headline: HEADLINE Did you believe the headline?"
Retired "You are an older retired professional and read the following
headline: HEADLINE Did you believe the headline?""
Industrial Worker "You are an industrial worker and read the following headline:
HEADLINE Did you believe the headline?"
Financial Analyst "You are a financial analyst and read the following headline:
HEADLINE Did you believe the headline?"
Conspiracy-Believer "You are an individual who believes in many conspiracy theories
and read the following headline: HEADLINE Did you believe
the headline?""
Conspiracy-Susceptible "You are someone who is susceptible to conspiracy theories and
read the following headline: HEADLINE Did you believe the
headline?""
Standard News Reader "You are a standard news reader and read the following headline:
HEADLINE Did you believe the headline?""
REFERENCES
Aher, G. V., R. I. Arriaga, and A. T. Kalai. 2023. “Using Large Language Models to Simulate Multiple Humans and Replicate
Human Subject Studies”. In Proceedings of the 40th International Conference on Machine Learning, edited by A. Krause,
E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, and J. Scarlett, Volume 202 of Proceedings of Machine Learning Research.
July 23rd-29th, Honolulu, Hawaii, 337-371.
Arif, A., L. G. Stewart, and K. Starbird. 2018. “Acting the Part: Examining Information Operations Within #BlackLivesMatter
Discourse”. In Proceedings of the ACM on Human-Computer Interaction, Volume 2. New York, NY, USA: November
3rd-7th, Jersey City, New Jersey, 20:1-20:27.
Bandura, A. 2009. “Social Cognitive Theory of Mass Communication”. Media Psychology:265–299.
Bittman, L. 1985, October. The KGB and Soviet Disinformation: An Insider’s View. 1st Edition ed. Washington: Pergamon Pr.

Farr, Ng, Prochaska, Cruickshank, and West
Bozarth, L., A. Saraf, and C. Budak. 2020. “Higher Ground? How Groundtruth Labeling Impacts Our Understanding of Fake
News about the 2016 US Presidential Nominees”. In Proceedings of the International AAAI Conference on Web and Social
Media, Volume 14. February 7th-12th, New York, NY, 48-59.
Bradshaw, S., and P. N. Howard. 2018. “Challenging Truth and Trust: A Global Inventory of Organized Social Media
Manipulation”. The Computational Propaganda Project 1:1–26.
Brashier, N. M., and D. L. Schacter. 2020. “Aging in an Era of Fake News”. Current Directions in Psychological Science 29(3):316–
323.
Ellul, J. 1973, January. Propaganda: The Formation of Men’s Attitudes | Politics and Prose Bookstore. ISBN: 9780394718743.
Epstein, J. M. 2008. “Why Model?”. Journal of Artificial Societies and Social Simulation 11(4):12.
Filippas, A., J. J. Horton, and B. S. Manning. 2024. “Large Language Models as Simulated Economic Agents: What Can We
Learn from Homo Silicus?”. In Proceedings of the 25th ACM Conference on Economics and Computation. July 8th-11th,
New Haven, CT, 614-615.
François, C. 2019. “Actors, Behaviours, Content: A disinformation ABC (Transatlantic High Level Working Group on Content
Moderation Online and Freedom of Expression Series). Annenberg Public Policy Center, University of Pennsylvania;
Annenberg Foundation Trust, Sunnylands”. Institute for Information Law, University of Amsterdam.
Gabriel, S., S. Hallinan, M. Sap, P. Nguyen, F. Roesner, E. Choi et al. 2022, May. “Misinfo Reaction Frames: Reasoning about
Readers’ Reactions to News Headlines”. In Proceedings of the 60th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), edited by S. Muresan, P. Nakov, and A. Villavicencio. May 22nd-27th, Dublin,
Ireland, 3108-3127: Association for Computational Linguistics https://doi.org/10.18653/v1/2022.acl-long.222.
Gallacher, John D and Barash, Vlad and Howard, Philip N and Kelly, John 2018. “Junk News on Military Affairs and National
Security: Social Media Disinformation Campaigns against US Military Personnel and Veterans”. Last modified Feb 10,
2018. https://arxiv.org/abs/1802.03572.
Goffman, E. 1974. Frame analysis: An Essay on the Organization of Experience. Frame analysis: An Essay on the Organization
of Experience. Cambridge, MA, US: Harvard University Press. Pages: ix, 586.
Grinberg, N., K. Joseph, L. Friedland, B. Swire-Thompson, and D. Lazer. 2019, January. “Fake News on Twitter During the
2016 U.S. Presidential Election”. Science 363(6425):374–378.
Haupt, M. R., L. Yang, T. Purnat, and T. Mackey. 2024. “Evaluating the Influence of Role-Playing Prompts on ChatGPT’s
Misinformation Detection Accuracy: Quantitative Study”. JMIR infodemiology 4(1):e60678.
Hu, Tianrui and Liakopoulos, Dimitrios and Wei, Xiwen and Marculescu, Radu and Yadwadkar, Neeraja J 2025. “Simulating
Rumor Spreading in Social Networks using LLM Agents”. Last modified Feb 3, 2025. https://arxiv.org/abs/2502.01450.
Klein, G., J. K. Phillips, E. L. Rall, and D. A. Peluso. 2007. “A Data–Frame Theory of Sensemaking”. In Expertise out of
context, edited by R. R. Hoffman, 118–160. London: Psychology Press.
Levine, A., and D. Hirsch. 1991. “Undergraduates in Transition: A New Wave of Activism on American College Campus”.
Higher Education 22(2):119–128.
Li, Lincan and Li, Jiaqi and Chen, Catherine and Gui, Fred and Yang, Hongjia and Yu, Chenxiao and Wang, Zhengguang
and Cai, Jianing and Zhou, Junlong Aaron and Shen, Bolin and others 2025. “Political-llm: Large Language Models in
Political Science”. Last modified Dec 9, 2024. https://arxiv.org/abs/2412.06864.
Li, Xinyi and Xu, Yu and Zhang, Yongfeng and Malthouse, Edward C 2024. “Large Language Model-Driven Multi-Agent
Simulation for News Diffusion Under Different Network Structures”. Last modified Oct 16, 2024. https://arxiv.org/abs/
2410.13909.
Mosleh, M., G. Pennycook, A. A. Arechar, and D. G. Rand. 2021. “Cognitive Reflection Correlates with Behavior on Twitter”.
Nature Communications 12(1):921.
Ng, L. H. X., and K. M. Carley. 2022. “Pro or Anti? A Social Influence Model of Online Stance Flipping”. IEEE Transactions
on Network Science and Engineering 10(1):3–19.
Ng, Lynnette Hui Xian and Zhou, Wenqi and Carley, Kathleen M 2024. “Exploring Cognitive Bias Triggers in Covid-19
Misinformation Tweets: A Bot vs. Human Perspective”. Last modified June 11, 2024. https://arxiv.org/abs/2406.07293.
Park, J. S., J. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein. 2023. “Generative Agents: Interactive Simulacra
of Human Behavior”. In Proceedings of the 36th Annual ACM Symposium on User Interface Software and Technology.
October 29th-Novemeber 1st, San Fransisco, California, 1-22.
Pennycook, G., and D. G. Rand. 2019. “Lazy, Not Biased: Susceptibility to Partisan Fake News is Better Explained by Lack
of Reasoning Than by Motivated Reasoning”. Cognition 188:39–50.
Prochaska, S., J. Vera, D. Lew Tan, B. Yamron, S. Venuto, A. Kejriwal, et al. 2025. “Deep Storytelling: Collective Sensemaking
and Layers of Meaning in U.S. Elections”. Number CSCW1. Submitted for publication to Conference on Computer-Supported
Cooperative Work & Social Computing October 18th-22nd, Bergen, Norway.
Reuter, C., K. Hartwig, J. Kirchner, and N. Schlegel. 2019. “Fake News Perception in Germany: A Representative Study of
People’s Attitudes and Approaches to Counteract Disinformation”. Association for Information Systems AIS.

Farr, Ng, Prochaska
Rid, T. 2020, April. Active Measures : The Secret History
York: Farrar, Straus and Giroux. ISBN: 9780374287269
Shao, C., G. L. Ciampaglia, O. Varol, K.-C. Yang, A. Flammini
Content by Social Bots”. Nature Communications 9(1):4
Starbird, K., A. Arif, and T. Wilson. 2019. “Disinformatio
Strategic Information Operations”. In Proceedings of th
9th-13th, Austin, TX, 1-26.
Starbird, K., R. DiResta, and M. DeButts. 2023, June. “Influ
2020 US Election”. Social Media + Society.
Starbird, K., S. Prochaska, and B. Yamron. 2025. “What is G
Rumors About Election Integrity”. Submitted for public
Social Computing October 18th-22nd, Bergen, Norway.
Tandoc Jr, E. C., D. Lim, and R. Ling. 2020. “Diffusion of D
and Why”. Journalism 21(3):381–398.
U.S. Department of the Army 2023. Army Doctrine Public
Headquarters, Department of the Army.
AUTHOR BIOGRAPHIES
DAVID FARR is a PhD student at the University of Washin
of this work. He received his MSc in Operational Research
his Bachelor’s degree in Systems Engineering from the Unit
include multi-agent systems, network analysis, and data ann
https://davidthfarr.github.io/.
LYNNETTE HUI XIAN NG is a PhD student in Societal
Science and a co-first author of this work. She did her ba
Singapore. Her current work focuses around network and e
automated agents on social media. Her e-mail address is lyn
STEPHEN PROCHASKA is a PhD candidate in the Inform
current work focuses around sensemaking, framing theory, an
IAIN J. CRUICKSHANK is adjunct faculty at Carnegie-Me
Lecturer at Johns Hopkins University. His research interests i
the use of multi-modal data in understanding social phenom
JEVIN WEST is the co-founder of the new Center for an In
promoting an informed society and strengthening democrati
data and technology on science and society, with a focus o
jevinw@uw.edu and his website is https://www.jevinwest.or

uickshank, and West
Disinformation and Political Warfare. First edition. ed. New
d F. Menczer. 2018, November. “The Spread of Low-Credibility
Collaborative Work: Surfacing the Participatory Nature of
CM on Human-Computer Interaction, Volume 3. November
e and Improvisation: Participatory Disinformation during the
g On? An Evidence-Frame Framework for Analyzing Online
to Conference on Computer-Supported Cooperative Work &
nformation: How Social Media Users Respond to Fake News
n (ADP) 3-13: Information Operations. Washington, D.C.:
n in the School of Information Science and a co-first author
Data Science from the University of Edinburgh, and he did
tates Military Academy at West Point. His research interests
on. His e-mail address is dtfarr@uw.edu and his website is
mputing at Carnegie Mellon University, School of Computer
lor’s degree in Computer Science at National University of
ement impact of behavioral influence techniques applied by
eng@cmu.edu and his website is https://quarbby.github.io.
on Science Department at the University of Washington. His
ormation campaigns. His e-mail address is sprochas@uw.edu.
University’s Software and Societal Systems Department and
de applying data science to solve governmental problems and
. His e-mail address is icruicks@andrew.cmu.edu.
med Public at UW aimed at resisting strategic misinformation,
scourse. His research and teaching focus on the impact of
owing the spread of misinformation. His e-mail address is
