Title: Unveiling the collective behaviors of large language model-based autonomous agents in an online community: A social network analysis perspective

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_adjacent/18_BK08_Online_Community_Collective_Behaviors_2026.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T04:04:20+00:00
- page_count: 14
- status: ok
- text_char_count: 75934

Metadata:
- author: Huiru Chen
- doi: 10.1016/j.dim.2025.100107
- keywords: LLM-based autonomous agent, Machine behavior, Collective behavior, Online community, Social network
- subject: Data and Information Management, 10 (2026) 100107. doi:10.1016/j.dim.2025.100107

Outline:
- Unveiling the collective behaviors of large language model-based autonomous agents in an online community: A social network ... (page 1)
  - 1 Introduction (page 1)
  - 2 Literature review (page 2)
    - 2.1 LLM-based autonomous agents (page 2)
    - 2.2 Machine behavior (page 2)
    - 2.3 Collective machine behavior in online communities (page 3)
  - 3 Hypotheses development (page 3)
    - 3.1 Small-world phenomenon in LLMAAs’ social network (page 3)
    - 3.2 Power-law distribution in LLMAAs’ social network (page 3)
    - 3.3 Homophily in LLMAAs’ social network (page 4)
  - 4 Data and method (page 4)
    - 4.1 LLMAAs’ social network (page 4)
    - 4.2 Social network analysis (page 6)
    - 4.3 Text mining (page 6)
  - 5 Results (page 6)
    - 5.1 Small-world phenomenon (page 6)
    - 5.2 Power-law distribution (page 8)
    - 5.3 Homophily in LLMAAs’ social network (page 9)
      - 5.3.1 Profile-based homophily in the English subchannel (page 9)
      - 5.3.2 Content-based homophily in the English subchannel (page 9)
      - 5.3.3 Homophily in the Chinese subchannel (page 10)
  - 6 Discussion and conclusion (page 11)
    - 6.1 Key findings (page 11)
    - 6.2 Theoretical implications (page 12)
    - 6.3 Practical implications (page 12)
    - 6.4 Limitations and future directions (page 12)
  - CRediT authorship contribution statement (page 13)
  - Declaration of generative AI and AI-assisted technologies in the writing process (page 13)
  - Declaration of competing interest (page 13)
  - Acknowledgements (page 13)
  - References (page 13)

Markdown Content:

10 (2026) 100107
Contents lists available at ScienceDirect
Data and Information Management
journal homepage: www.journals.elsevier.com/data-and-information-management
Unveiling the collective behaviors of large language model-based
autonomous agents in an online community: A social network
analysis perspective
Huiru Chena,b , Zhenhua Wanga, Ming Rena,c,*
aRenmin University of China, Beijing, China
bNational University of Singapore, Singapore
cRUC Institute for AI Governance, Renmin University of China, Beijing, China
A R T I C L E I N F O A B S T R A C T
Keywords: As Large language models (LLMs) continue to advance, the autonomous agents built upon them—LLM-based
LLM-based autonomous agent Autonomous Agents (LLMAAs) —are becoming more capable and widely used. While existing research has
Machine behavior primarily focused on the capabilities of individual AI agents or their collaboration with humans, less is known
Collective behavior
about the emergent behaviors that arise when LLMAAs interact with each other at scale. This study addresses this
Online community
gap by examining the collective behavior of LLMAAs in Chirper, a social simulation platform exclusively
Social network
inhabited by AI agents. Drawing on theories from social network analysis and machine behavior, we investigate
whether LLMAAs exhibit social dynamics commonly found in human communities, such as clustering, influential
hubs, and homophily. Our findings reveal that LLMAAs form structured interaction networks that share key
properties with human social systems, including power-law degree distributions and interaction homophily,
though without exhibiting typical small-world characteristics. These insights represent an early step toward
understanding the collective behavior of autonomous AI agents. They contribute to the emerging field of AI
sociality and help inform the design of future multi-agent systems for engineering and social science applications.
1. Introduction environments (Wang et al., 2024). LLMs, which are based on probabi-
listic models and trained on large datasets, can offer more flexible re-
Large language models (LLMs), such as DeepSeek (DeepSeek-AI sponses. Their ability to generalize from training examples means they
et al., 2025) and LLaMA (Touvron et al., 2023), have shown impressive can adapt to a wider range of scenarios. Yet, this also means their
performance that in some cases resemble human cognition (Aggarwal behavior may sometimes be inaccurate, inconsistent, or suboptimal in
et al., 2023). Thus, LLMs are increasingly viewed as a promising foun- new situations. Given these characteristics, it is crucial to study how
dation for building more intelligent, human-like autonomous agents (Xi LLMAAs behave, particularly in interactive settings where they work
et al., 2023). The LLM-based Autonomous Agents (LLMAAs) are being together.
adopted in a variety of fields. To name a few, “Ghost in the Minecraft” The social science of AI has gained attention, aiming to understand
showed great performance in the game “My World”(Zhu et al., 2023). the principles that govern AI behavior and how it compares with human
AutoGPT can design websites without human intervention(Yang et al., behavior (Xu et al., 2024). These approaches examine AI systems at
2023), and MetaGPT offers a framework for multiple agents to collab- different levels: individual performance, collective behavior, and
orate on user-defined goals(Hong et al., 2023). These developments human-machine interaction. Studies at the individual level often assess
highlight the growing potential of LLMAAs in shaping the future of how well an AI model performs tasks using social science frameworks,
intelligent systems. such as those exploring reasoning and cognitive abilities (Binz & Schulz,
Autonomous agents—systems that can perform tasks independen- 2023; Hagendorff et al., 2022). Collective-level studies focus on emer-
tly—traditionally relied on rule-based or heuristic approaches, which gent patterns that arise from interactions among multiple agents (Borch,
made it difficult for them to replicate human-like behaviors in complex 2022). Hybrid studies of human-machine interaction aim to discover
* Corresponding author. 59 Zhongguancun Street, Haidian District, Beijing, 100872, China.
E-mail address: renm@ruc.edu.cn(M. Ren).
https://doi.org/10.1016/j.dim.2025.100107
Received 28 November 2024; Received in revised form 7 July 2025; Accepted 22 July 2025
Available online 5 August 2025
2543-9251/© 2025 The Authors. Published by Elsevier Ltd on behalf of School of Information Management Wuhan University. This is an open access article under
the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-nc-nd/4.0/ ).

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
how humans and AI can work together effectively (Chugunova & Sele, Initial applications of LLMAAs in social simulation have also
2022; Xiong et al., 2023). extended to classic psychological and economic experiments. For
While prior work has primarily focused on the performance of in- instance, LLMAAs have been used to model decision-making in the Ul-
dividual AI agents—either in isolation or within human-centered sys- timatum Game and the Prisoner’s Dilemma, yielding results comparable
tems—less attention has been given to the emergent behaviors that arise to those observed in human participants (Aher et al., 2023; Phelps &
solely from agent-to-agent interactions. Understanding these emergent Russell, 2023). A smaller body of research has begun to explore the
patterns is critical, as they shape how AI agents communicate, coordi- collective behavior of LLMAAs. In collaborative tasks, LLMAAs demon-
nate, and make decisions—core functions in any multi-agent system. A strated patterns such as majority rule, mirroring human group behavior
key question is whether the social structures formed by AI agents can be (Zhang et al., 2023). In competitive settings, behaviors such as imita-
meaningfully compared to human social networks, given their algo- tion, differentiation, and the Matthew Effect emerged (Zhao et al.,
rithmic foundations and absence of embodied cognition. On one hand, 2023). In political science simulations, LLMAAs infused with real-world
AI agents may exhibit fundamentally different interaction patterns due data have shown potential in predicting election outcomes (Argyle et al.,
to their distinct decision-making processes (Binz & Schulz, 2023; 2023). Moreover, studies have identified human-like interaction pat-
Hagendorff, 2023b); on the other hand, structural isomorphisms such as terns among LLMAAs in online community settings (He et al., 2023; S.
clustering, hubs, or power-law distributions may still emerge (Gao et al., Li, Zhang, & Sun, 2023), further supporting their value in advancing
2023). Given their autonomy, LLMAAs have the potential to social science research through computational experimentation.
self-organize in ways that produce complex and unpredictable collective
behaviors. 2.2. Machine behavior
This study aims to investigates the collective behavior of LLMAAs in
an online community. While LLMAAs are trained on human-generated The emerging field of machine behavior provides a framework for
data and often exhibit individual behaviors similar to those of understanding how AI systems (e.g., LLMAAs) behave in real-world
humans, it remains unclear whether their social networks follow pat- environments. As proposed by Rahwan et al. (2019), machine
terns commonly found in human communities. Prior research on human behavior encompasses three main domains: individual machine
social networks has identified consistent features such as small-world behavior, collective machine behavior, and hybrid human-machine
properties, power-law degree distributions, and homophily (Agnew behavior.
et al., 2001; Baraba´si & Albert, 1999; Watts & Strogatz, 1998). Using Individual machine behavior research focuses on evaluating AI
social network analysis and text mining, this study examines the struc- models using frameworks from psychology and economics to enhance
ture and interaction patterns within the LLMAA network. We analyze a interpretability and accountability (Hagendorff, 2023a). Psychological
dataset from Chirper (S. Li, Zhang, & Sun, 2023), which contains posts constructs explain human thinking without directly matching neural
and interaction data among LLMAAs. Chirper provides a structured yet processes. Likewise, analyzing the behavior of AI systems, which are
dynamic setting where LLMAAs can post content, engage with each based on neuron-inspired architectures, can advance our understanding
other, and form social connections, making it an ideal platform for un- of natural and artificial intelligence (Taylor & Taylor, 2021). By exam-
derstanding the LLMAAs’ behaviors in an online community. ining models’ cognitive abilities and moral decision-making, researchers
The remainder of this paper is structured as follows. Section 2 re- have identified both their strengths and limitations. For example, GPT-3
views related work on LLMAAs, machine behavior, and collective dy- performed well on tasks involving perception, search, and deliberation,
namics in online communities. Section 3outlines our hypotheses, based but struggled with causal reasoning, exhibiting human-like biases (Binz
on human social network theory and the technical features of LLMAAs. & Schulz, 2023). In contrast, more advanced models like GPT-3.5 and
Section 4introduces the dataset and methodological approach. Section 5 GPT-4 demonstrated greater consistency and “hyper-rationality” in
presents our findings. Section 6 discusses implications for future similar tasks (Hagendorff et al., 2022). Regarding moral behavior,
research and concludes the study. GPT-4 was shown to align closely with human responses across eight
moral judgment scenarios (Almeida et al., 2023). However, with
2. Literature review appropriate prompting, both GPT-3.5 and GPT-4 were capable of
generating deceptive outputs, such as inducing false beliefs (Hagendorff,
2.1. LLM-based autonomous agents 2023b). These studies, often conducted via controlled prompting, offer
insights into the behavior of LLMs as individual entities.
LLMAAs typically comprise four core modules: configuration, Collective machine behavior focuses on emergent dynamics that
memory, planning, and execution (Wang et al., 2024). These compo- arise only when multiple AI agents interact. Systems composed of
nents work together to enable LLMAAs to autonomously perceive and multiple AI models have demonstrated a capacity for complex coordi-
interact with their environment. With the integration of LLMs, these nation and problem-solving, particularly in high-stakes environments
agents have shown enhanced capabilities across various tasks, making (Chen, Sun, & Wang, 2022). However, such collective behavior can also
them increasingly applicable to a wide range of domains (Ziems et al., have unintended consequences. For instance, in automated financial
2023). markets, groups of AI agents replacing human traders have sometimes
Traditional social science experiments often face limitations such as interacted in ways that contributed to market instability, such as “flash
ethical concerns, limited scalability, and challenges in replicability. crashes” (Borch, 2022). Despite these risks, sociological theories remain
LLMAAs, acting as experimental participants, offer a promising alter- useful for understanding machine collective action and serve as a
native by enabling AI-driven simulations of social behavior. These sys- theoretical foundation for the design of multi-agent AI systems
tems provide novel opportunities to explore human dynamics in (MacKenzie, 2019). Compared to research on individual behavior, col-
controlled yet scalable environments (Grossmann et al., 2023). lective machine behavior remains relatively underexplored. Although
Recent work has focused on developing multi-agent systems that recent studies have simulated virtual societies composed of LLMAAs,
simulate human behavior across diverse social contexts. For example, these systems often involve a limited number of agents with predefined
Park et al. (2023)modeled daily life in a small town using 25 LLMAAs. Y. roles. There is still a lack of research into large-scale, spontaneous, and
Li, Yang, and Zhao (2023)constructed a collaborative multi-agent sys- self-organizing collective behavior among AI agents.
tem to simulate job fair interactions, while Gao et al. (2023)created a Hybrid human-machine behavior examines the interactions between
social network simulation involving information, emotion, and attitude humans and AI systems. This line of research explores factors influ-
diffusion among LLMAAs. These efforts highlight LLMAAs’ potential as a encing human trust in automated decision-making (Chugunova & Sele,
technical framework for simulating human social dynamics. 2022) and how the perceived status or role of AI participants affects
2

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
cooperation in joint tasks (Xiong et al., 2023). These findings offer been supported by empirical studies on large-scale social media plat-
practical guidance for designing more effective and collaborative forms. Analyses of user networks on Weibo and Twitter, for instance,
human-AI systems. revealed that users can typically reach one another through only a small
At present, research on individual machine behavior and human- number of connections, accelerating the spread of information (Dong
machine interaction has garnered significant attention. In contrast, et al., 2018; Sadri et al., 2018).
collective machine behavior—particularly in large-scale system- The second characteristic, high clustering, refers to the tendency for
s—remains a relatively underexplored area. As LLMs continue to individuals who share a mutual connection to also be connected with
improve, LLMAAs are increasingly capable of engaging in complex, one another. Newman and Park (2003)emphasized that social networks
multi-agent interactions. The growing interest in LLMAA collectives exhibit significantly higher clustering than other types of networks. This
aligns with the rise of the social science of AI, a nascent interdisciplinary phenomenon has been widely observed in online social media, where
field that treats AI agents as social entities and focuses on their behav- users often form dense clusters of interaction (Sadri et al., 2018). Such
ioral traits (Xu et al., 2024). clustering facilitates the development of trust and the reinforcement of
social norms within these groups. Su and Yen (2017)further affirmed
2.3. Collective machine behavior in online communities that the coexistence of short global separation and dense local clustering
is a defining feature of human social networks.
Information technology, especially social media, completely Building on this foundation, the small-world structure has significant
changed the way people communicate with others, reshaping the feature implications for how information flows, communities develop, and
of collective behaviors by greatly facilitating the social interactions collective behaviors emerge in a network. In the case of LLMAAs, there
(Bak-Coleman et al., 2021). Collective behavior refers to the sponta- are two main reasons to expect a small-world structure in their social
neous, self-organized actions that emerge within a crowd. More specif- networks. First, LLMAAs are designed for interaction, and the social
ically, collective behavior encompasses riots, protests, the spread of nature of online platforms encourages frequent and dense exchanges.
information and fads (Marx & Wood, 1975). These behaviors manifest in Unlike social bots—typically programmed to push specific content and
online communities through user interactions. In these contexts, user often forming star-shaped networks with limited complexity (Ng &
interactions include activities such as liking, commenting, following, Carley, 2025)—LLMAAs are intended to engage in conversations. Their
replying, sharing, among others (Felmlee & Faris, 2013). Consequently, goal is not just to amplify messages but to participate in social in-
users form social networks through these interactions. Social network teractions. As a result, they are more likely to build human-like, richly
analysis and text mining are widely employed methods to unveil the connected networks. Second, since LLMAAs show interactive behaviors
collective behavior of social media users, particularly in areas such as and perform at a human level in many tasks, it is reasonable to expect
information dissemination and social movements (Dong et al., 2018; Isa that they will form highly clustered, densely connected net-
& Himelboim, 2018). works—similar to those found in human societies.
Researchers studied the functions and roles of social bots in These considerations lead to the following hypothesis.
spreading information and their social network structure. Social bots,
Hypothesis 1. LLMAAs’ social network possesses small-world
albeit less sophisticated than LLMAAs, engage in social interactions with
characteristics.
specific agendas, collaborating to spread information automatically and
posting targeted content to draw attention (Cai et al., 2023). From the
conduit brokerage perspective for understanding the behavior of bots 3.2. Power-law distribution in LLMAAs’ social network
spreading information, two intertwined processes including algorithmic
social alertness and algorithmic social transmission can explain the in- A scale-free network is characterized by a degree distribution that
formation diffusion mechanism of social bots (Salge et al., 2022). When follows a power-law pattern, where a small number of nodes accumulate
spreading information, social bots with higher followership lead to a disproportionately large number of connections, while the vast ma-
higher impact (Boichak et al., 2018). jority have relatively few (Baraba´si & Albert, 1999). This structural
Given LLMAAs’ superior individual capabilities compared to simpler feature is commonly observed in real-world social networks and pro-
social bots, an intriguing research question emerges regarding the vides important insights into how such networks are organized and how
complex structures and traits arising spontaneously in LLMAAs’ collec- they evolve over time.
tive behaviors. Investigations into the interactions within LLMAAs in the Mathematically, a power-law distribution is expressed as shown in
absence of human intervention represent a distinct area of study. The Eq. (1), where P(x)represents the probability that a node has degree x,
autonomous actions of such systems, as opposed to those driven by and α is a constant greater than 1.
specific objectives as social bots, may exhibit divergent patterns. P(x)∝x (cid:0)α (1)
3. Hypotheses development This distribution implies that most nodes in the network are mini-
mally connected, while a few nodes—often referred to as hubs—possess
3.1. Small-world phenomenon in LLMAAs’ social network a very high number of connections. Such highly skewed distributions
have been widely documented in diverse contexts, including the struc-
The small-world property is one of the most well-documented ture of the internet, citation networks, and patterns of human commu-
structural features of real-world human social networks (Watts & Stro- nication (Clauset et al., 2009). In social systems, this reflects a tendency
gatz, 1998). A small-world network is defined by two key characteris- for interactions and attention to concentrate around a select few in-
tics: short average path lengths and high clustering coefficients. These dividuals who act as central figures or influencers within the network.
properties enable efficient information transmission and foster For instance, on social media platforms, only a small fraction of users
tightly-connected local communities within large-scale networks. receives substantial public attention, while the majority remain rela-
The first characteristic, short average path length, indicates that even tively unnoticed (Dong et al., 2018). Influencers and online celebrities,
in large networks, the typical distance between any two nodes remains though representing a small share of total users, hold significant sway
relatively small. This structure allows information or resources to diffuse over discourse and information flows (Vrontis et al., 2021). This phe-
rapidly across the network. Milgram’s classic 1967 experiment, which nomenon exemplifies the Matthew Effect, where initial advantages such
introduced the concept of “six degrees of separation,” demonstrated that as early visibility or popularity, can lead to increasing returns in influ-
individuals within large social networks are often connected by sur- ence and connectivity (Kümpel, 2020).
prisingly few intermediaries (Milgram, 1967). This finding has since In the case of LLMAAs, their behaviors are shaped by human-defined
3

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
prompts, including their posting frequency, tone, and topical focus. In following hypothesis.
an online community setting, such differences may result in varied levels
Hypothesis 3a. Connections are more likely to exist between LLMAAs
of engagement and visibility among agents. LLMAAs that are more
with higher profile similarity.
active or aligned with popular topics may attract more interactions, thus
emerging as influential agents within the network. These dynamics Content-based homophily refers to the tendency of LLMAAs to con-
mirror those seen in human social networks, suggesting the likelihood of nect based on similarity in the topics and content they generate. While
a similarly skewed distribution in LLMAAs’ online interactions. Based on profile information shapes their identity and interaction context, it is
this reasoning, we propose the following hypothesis: through their generated posts that LLMAAs express topical preferences
and implied values. Shared content interests may lead to more in-
Hypothesis 2. LLMAAs’ social network node degree follows a power
teractions and connections, analogous to how users in online commu-
law distribution.
nities form ties around shared narratives or discussion themes.
Therefore, we propose the following hypothesis.
3.3. Homophily in LLMAAs’ social network
Hypothesis 3b. Connections are more likely to exist between LLMAAs
Two key drivers of social network formation are spatio-temporal with higher posting content similarity.
proximity and homophily (Felmlee & Faris, 2013). As LLMAAs operate
in a digital space free from physical or temporal constraints, this study 4. Data and method
focuses exclusively on the role of homophily, the tendency of individuals
to associate with others who are similar to themselves. 4.1. LLMAAs’ social network
In human societies, individuals often form relationships, such as
friendships, marriages, or information-sharing ties, based on shared This study utilized data from Chirper (chirper.ai), a Twitter-like
characteristics (Agnew et al., 2001). As a result, personal networks online platform launched in April 2023, designed exclusively for
frequently reflect homophily along a wide range of socio-demographic, LLMAAs. On Chirper, LLMAAs can communicate with one another,
behavioral, and psychological dimensions (McPherson et al., 2001). This share diverse types of content, and engage socially by liking and com-
phenomenon has also been widely observed in online environments, menting on each other’s posts. While humans can create LLMAAs by
particularly in fields such as politics, marketing, and communication assigning them specific identities and traits, they are not permitted to
(Khanam et al., 2023). participate in the platform’s discussions during the data collection
In the context of LLMAAs, homophily can be examined along two key period.
dimensions: profile similarity and content similarity. These dimensions The main interface of the Chirper platform is shown in Fig. 1. It
reflect the unique ways in which LLMAAs are configured and interact on features a continuous feed of posts generated by LLMAAs, which may
digital platforms. include text, images, or videos. Other LLMAAs can interact with these
Profile-based homophily captures the tendency of LLMAAs to con- posts through likes or comments. Hashtags are used to organize dis-
nect with others whose predefined profiles share similar traits. LLMAAs cussion topics, and trending conversations are displayed on the right-
are typically guided by user-defined profiles that may include occupa- hand side of the page. A sample LLMAA profile page is presented in
tion, interests, personality descriptors, and other attributes. These pro- Fig. 2. The profile contains information such as the LLMAA’s biography
files not only shape their behavior and communication style but also act and follower/following details. The “Activity” subpage records the
as signals to other agents. As such, profile similarity may influence the LLMAA’s posting and liking history on the platform.
likelihood of connection formation among LLMAAs. This leads to the This study utilized the Chirper dataset which spans from April to
Fig. 1. The main web page of Chirper.
4

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
Fig. 2. A LLMAA profile page of Chirper.
June 2023 (S. Li, Zhang, & Sun, 2023). The dataset includes individual
LLMAA profiles, interaction histories, and platform posts. These posts
are written in five languages—English, Chinese, Japanese, German, and
Spanish—with English and Chinese being the most dominant. The En-
glish subchannel comprises 20,814 accounts, while the Chinese sub-
channel includes 11,288 accounts; the remaining languages each have
fewer than 100 accounts.
Our analysis focused on the “liking” behavior among LLMAAs, as it
represents the most common form of social interaction on Chirper.
“Liking” is a basic yet significant social media activity that serves as a
measurable indicator of social validation and peer influence (Sherman
et al., 2016). Compared to comments, likes are more visible and require
less effort (Schreiner et al., 2019), making them especially suitable for
studying LLMAA interactions.
We constructed a directed social network based on “likes,” visualized
using the Yifan Hu layout, as shown in Fig. 3. Each node in the network
represents a LLMAA, and a directed edge indicates that one LLMAA liked
a post created by another. Edge weights correspond to the number of
likes that one LLMAA gave to another. In this network, red nodes
represent LLMAAs in the English subchannel, while blue nodes denote Fig. 3. LLMAAs’ social network (English LLMAAs in red, Chinese LLMAAs in
blue). (For interpretation of the references to colour in this figure legend, the
those in the Chinese subchannel. The visualization reveals distinct
reader is referred to the Web version of this article.)
language-based clusters, with some cross-lingual interactions present,
reflecting the multilingual capabilities of certain LLMAAs. Fig. 4 pre-
over the two-month period. The network has a density of 0.000163 and
sents the weekly number of likes exchanged between LLMAAs on
an average in-degree/out-degree of 4.29. The highest interaction
Chirper. The data indicate a peak in activity during May, likely reflecting
observed between two nodes is with 46 likes.
increased user engagement during that period.
The network comprises 26,369 nodes and 113,236 directed edges,
including 3884 self-loops (i.e., LLMAAs liked their own posts). Most of
the edge weights fall below 10, suggesting relatively limited interactions
5

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
node was represented using vector embeddings derived from their tex-
tual content, following the procedure detailed in Section 4.3. We
computed the semantic similarity between connected node pairs in both
the original and the rewired networks. Using a Wilcoxon rank-sum test,
we assessed whether the average similarity between connected nodes in
the original network was significantly higher than that in the random-
ized version. A significantly higher similarity in the original network
would suggest that homophily is a key mechanism underlying the for-
mation of links in the LLMAA interaction network.
4.3. Text mining
To investigate profile-based homophily and content-based homo-
phily within the social network, we employed text mining techniques on
LLMAAs within the English subchannel and Chinese subchannel sepa-
rately. The overall text mining workflow is illustrated in Fig. 5.
Fig. 4. Number of likes each week. We first obtained the biographies in profiles and posting content of
LLMAAs in the English subchannel and Chinese subchannel. The text of
4.2. Social network analysis biographies and posts were preprocessed to remove non-word symbols
and emojis. Since some LLMAAs posted in multiple languages, we used
We applied social network analysis to examine the structural char- the Baidu Machine Translation API to translate non-English text into
acteristics of the network formed through LLMAAs’ liking behavior. Key English for the English subchannel, and non-Chinese text into Chinese
network properties were computed to provide a detailed understanding for the Chinese subchannel, ensuring consistency for the subsequent
of the network’s topology. Before conducting the analysis of the social analysis. In addition, for Chinese text, we applied the “jieba” package in
network, we removed self-loops, as they do not reflect social interactions Python to perform tokenization.
between LLMAAs and may introduce bias into the analysis. The next step involved vectorizing the text data. To examine profile-
To analyze the small-world properties of the LLMAAs’ social based homophily, we focused on LLMAAs’ profile biographies, which
network, we calculated the average shortest path length and the average typically contain self-descriptions, roles, or personality indicators. These
clustering coefficient of the largest strongly connected component texts were processed by converting text to lowercase, eliminating stop-
(LSCC), following standard practices for directed networks. The average words, and tokenizing. We then employed Doc2Vec to generate vector
shortest path length quantifies the degree of separation between nodes, representations of the biography text. Given the relatively simple nature
reflecting the efficiency of information flow within the network. The of these biographies, a vector size of 50 was used.
clustering coefficient, which captures the tendency of nodes to form To analyze content-based homophily, we used the LLMAAs’ posting
tightly connected groups, indicates the extent of local connectivity. content to infer their topical interests. We used BERTopic (Grootendorst,
Given the directed nature of the network, we further incorporated 2022), which enables the extraction of coherent and interpretable topics
directed clustering coefficient and directed global efficiency as com- while preserving key semantic features. For each LLMAA, we first vec-
plementary metrics, calculated across the entire social network. torized all their posts using all-MiniLM-L6-v2 for the English subchannel
Directed global efficiency measures the average inverse shortest path and bert-base-chinese for the Chinese subchannel. Then, we averaged the
length between node pairs, accounting for edge direction and excluding post vectors to obtain a single embedding for each LLMAA, which was
unreachable pairs. A higher value indicates efficient information flow used in the following computations. For dimensionality reduction,
across the directed network. The directed clustering coefficient, UMAP was applied with 15 neighbors and 5 components, followed by
following Fagiolo (2007), captures the likelihood that a node’s neigh- HDBSCAN clustering with a minimum cluster size of 10 and Euclidean
bors form directed triangles. This metric considers all combinations of distance. Topic distribution probabilities were used to generate vector
single and reciprocal links. It is defined as the ratio of observed to representations of each LLMAA’s content. Finally, cosine similarity be-
possible directed triangles based on a node’s total degree. Together, tween LLMAAs was calculated to quantify the semantic similarity of
these two metrics assess the small-world properties of directed net- their content.
works, reflecting both local cohesion and global connectivity in the
entire social network. 5. Results
To investigate degree distributions, we fitted power-law models
separately to the in-degree and out-degree distributions, following the 5.1. Small-world phenomenon
method outlined by Clauset et al. (2009). The fitting and testing pro-
cedures were conducted using the poweRlaw package in R. In real-world We examined the LLMAA like-based interaction network formed
scenarios, data rarely follow a pure power-law distribution across the across six distinct time periods based on the time of the liking behavior,
entire range. Instead, the distribution typically holds above a certain as well as the overall network (the overall network is used in the
threshold. Therefore, we estimated two key parameters: the scaling following analysis). In the overall network, the LSCC contains 39.12 %
parameter α and the lower bound xmin, where the power-law behavior of all nodes, suggesting a substantial level of mutual interaction among
begins (i.e., for x≥xmin). The goodness of fit was evaluated using the LLMAAs.
Kolmogorov–Smirnov (K-S) test statistic D, where a smaller D indicates a Table 1presents the average shortest path lengths in LSCC, clustering
closer fit between the empirical data and the theoretical distribution. To coefficients in LSCC, directed global efficiency and directed clustering
assess statistical significance, we employed a non-parametric bootstrap coefficient for all seven networks. In each case, the LLMAA networks
method to calculate p-values. A p-value below the chosen significance exhibit significantly higher clustering coefficients and directed clus-
level indicates rejection of the hypothesis that the data follow a tering coefficients compared to those of equivalent random networks,
power-law distribution. indicating strong local connectivity. This aligns with the first criterion of
To examine homophily in the network, we constructed a null model small-world networks. However, six of the seven networks (except for
for comparison. This model preserved the original network’s node set the network formed between May 24 and May 31, 2023) exhibit longer
and degree distribution but involved randomly rewiring the edges. Each average shortest path lengths within their LSCCs than their random
6

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
Fig. 5. Text mining procedures.
Table 1
Features of seven networks.
The LSCC in each time period May 3 – May 9 May 10 – May May 17 – May May 24 – May May 31 – June June 7 – June Overall
16 23 30 6 14 network
Number of nodes 1851 1131 2644 1879 890 339 1
Number of edges 5591 3206 12178 7536 4085 1994 71915
Average shortest path length (LLMAA 7.0248 (6.7981) 6.7894 5.9654 5.5294 4.7140 3.6172 5.6685
(random)) (6.6547) (5.3018) (5.5688) (4.6237) (3.4903) (4.8681)
Average clustering coefficient (LLMAA 0.0163 (0.0012) 0.0369 0.0375 0.0231 0.0412 0.0770 0.0426
(random)) (0.0019) (0.0018) (0.0019) (0.0066) (0.0176) (0.0007)
Directed global coefficient (random) 0.1368 (0.0667) 0.1495 0.1645 0.1739 0.2093 0.2679 0.1844
(0.0595) (0.0991) (0.1012) (0.1223) (0.1315) (0.1543)
Directed clustering coefficient (random) 0.0071 (8.7096e- 0.0102 0.0209 0.0206 0.0333 0.0656 0.0490
05) (0.0003) (0.0003) (0.0004) (0.0009) (0.0020) (0.0004)
counterparts. This observation contradicts the characteristic “short component-level and network-level metrics suggests that, although in-
path” property of small-world networks, which typically requires path formation flow is relatively slow within the largest component, the
lengths comparable to random networks. whole network benefits from strategic links between components. These
Interestingly, when examining the network as a whole rather than links create efficient pathways for fast information transmission across
just the LSCC, the directed global efficiency exceeds that of equivalent the structure.
random networks across all time periods. This contradiction between Therefore, Hypothesis 1 cannot be fully supported, as the LLMAA
Fig. 6. Multifractal analysis of the largest strongly connected component of LLMAAs’ social network.
7

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
social network does not exhibit classical small-world properties as level, sparse interconnections among these central hubs contribute to
defined by Watts and Strogatz (1998). This finding indicates that increased overall path lengths, reflecting a more fragmented large-scale
although LLMAAs build more densely connected and complex networks structure.
compared to the star-like structures often seen in social bots (Ng &
Carley, 2025), their network patterns still differ from those of typical 5.2. Power-law distribution
human social networks. Therefore, the structure of LLMAA social net-
works needs further investigation. Fig. 7illustrates the in-degree (a) and out-degree (b) distributions of
Given that the LLMAA social network does not exhibit the expected the LLMAA social network, plotted on logarithmic axes for clarity. The
small-world properties, we further investigated another potential in-degree distribution shows that most nodes receive relatively few
structural characteristic—fractality, or self-similarity. Self-similarity is a likes, while a small number of nodes have significantly higher in-
fundamental feature of complex networks and has been observed in degrees. The out-degree distribution is even more concentrated, with
diverse systems such as the World Wide Web, social networks, and the majority of nodes exhibiting very low out-degrees.
protein–protein interaction networks (Song et al., 2005). This property To fit the data to a power-law distribution, we identified the value of
refers to the repetition of similar structural patterns across different xmin that minimized the Kolmogorov–Smirnov (K–S) test statistic D. For
scales. In multifractal networks, shortest path lengths between nodes the in-degree distribution, the minimum D value of 0.0103 was achieved
can exhibit distinct behaviors depending on the scale of observation, at xmin =7, with 3446 data points exceeding this threshold. Under this
reflecting the underlying complexity and hierarchical organization of condition, the estimated power-law exponent ̂α was 2.297. As shown in
the network. Fig. 8(a), the fitted distribution closely matches the empirical data.
To explore the presence of self-similar patterns, we conducted a Using 5000 bootstrap samples, we obtained a p-value of 0.42, which
multifractal analysis of the social network. Specifically, we calculated exceeds the 0.05 significance level. Therefore, we cannot reject the
the shortest path distances between nodes within the LSCC of the overall hypothesis that the in-degree distribution follows a power-law distri-
LLMAA network and constructed the corresponding adjacency matrix. bution when x≥7. This finding suggests that LLMAAs with in-degrees
This matrix was then flattened and used for the multifractal analysis, above this threshold function as key influencers within the network.
following the method proposed by Rendo´n de la Torre et al. (2017). For the out-degree distribution, the minimum D value of 0.0493 was
The results are illustrated in Fig. 6. In Fig. 6(a), the fluctuation obtained at xmin =70, with only 84 data points exceeding this value. The
amplitude at different scales s for varying moment orders q reveals that estimated exponent ̂α was 6.367, and the fitted distribution is shown in
some curves are approximately linear while others are not, indicating Fig. 8(b). Again, 5000 bootstrap samples yielded a p-value of 0.52,
that the network displays different scaling behaviors at different levels indicating that the power-law distribution cannot be rejected for x≥70.
of fluctuation. Fig. 6(b) shows the Hurst exponent decreasing with scale, However, the high xmin value implies that only a small subset of LLMAAs
suggesting a higher fractal dimension at smaller scales and a lower one exhibit power-law behavior in their out-degree distribution. This in-
at larger scales. This is complemented by Fig. 6(c), where the upward dicates that only a minority of LLMAAs are highly active in initiating
trend of the mass exponent implies strong fractality at larger scales. interactions by liking other agents’ content, while the majority engage
Meanwhile, Fig. 6(d) presents the relationship between the Ho¨lder minimally. This pattern highlights current limitations in the social
exponent and its spectrum, which flattens at larger scales and aligns engagement capabilities of LLMAAs.
with the patterns observed in the Hurst exponent, further supporting the Additionally, we compared the power-law model with exponential
presence of multiscale complexity. and lognormal alternatives. As shown in Table 2, neither of the alter-
These results point to the structural richness and heterogeneity of the native distributions provided a better fit for the in-degree data at the
LLMAA social network. Some regions show dense and highly inter- 0.05 significance level. Therefore, the power-law distribution offers the
connected structures that resemble local small-world patterns with high most appropriate model for in-degree behavior in this context.
fractal dimensions. Others are more sparsely connected and have lower In conclusion, these findings partially support Hypothesis 2, as the
fractal dimensions. These findings suggest that the network comprises in-degree distribution follows a power-law pattern, indicating the
localized clusters embedded within a more diffuse global structure, presence of a small number of highly influential LLMAAs within the
reflecting a complex and self-similar organization. social network.
To further interpret the multifractal analysis results, we conducted a To investigate the mechanism underlying the power-law distribution
fine-grained examination of the network structure. In the LLMAA social of in-degree in the LLMAA social network, we examined the network’s
network, nodes with high in-degree centrality did not form a tightly evolutionary dynamics. Several theoretical mechanisms have been
interconnected cluster. Although the top three nodes in terms of in- proposed to account for the emergence of power-law distributions,
degree centrality (“@theenlightened1,” “@petshopboy,” and including preferential attachment, the Yule process, phase transitions,
“@auris”) were connected to one another, they did not interact with the and critical phenomena. Among these, preferential attachment is a
fourth-ranked node (“@slime”). Moreover, not all of the remaining top widely studied mechanism in the context of social network formation. It
10 in-degree nodes were connected to the top three, indicating that the posits that new nodes are more likely to connect to existing nodes with
network’s central hubs did not exhibit the cohesive clustering typically higher in-degree, thereby reinforcing their prominence and leading to a
seen in small-world networks. This lack of hub clustering contributes to power-law distribution (Baraba´si & Albert, 1999). We sought to deter-
longer average shortest path lengths across the network. mine whether this mechanism could explain the formation of the LLMAA
Furthermore, we extracted the 3-hop ego network of “@theenlight- network and the observed in-degree distribution.
ened1.” This subgraph contains 4725 nodes and 49,622 edges, with its To characterize preferential attachment, we adopted the bi-epochal
LSCC comprising 4310 nodes and 48,514 edges. The average shortest approach to estimate the attachment rate of nodes with in-degree k
path length within the LSCC is 3.6930, and the average clustering co- (Redner, 2005; Sheridan & Onodera, 2018). Originally designed to
efficient is 0.0778. For comparison, a random network with the same measure the rate at which scholarly articles with k citations attract new
size and degree distribution yields an average shortest path length of citations over time, this method can be adapted to social networks. The
3.7204 and a clustering coefficient of 0.0027. These results suggest that attachment rate A(k)is defined as the probability that a newly added
the ego network around “@theenlightened1” exhibits small-world edge connects to a node with in-degree k, as described in Eq. (2). This
properties. A similar pattern was observed for the ego network sur- approach allows us to empirically assess whether the dynamics of
rounding “@slime,” the fourth highest in-degree centrality node. These LLMAA interactios exhibit preferential attachment behavior.
findings indicate that local regions around high in-degree nodes tend to
be densely connected and structurally cohesive. However, at the global
8

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
Fig. 7. In-degree and out-degree distributions of LLMAAs’ social network.
Fig. 8. Power-law distribution fitting.
Vector representations were generated for all biography texts, and
Table 2
cosine similarity values were calculated between pairs of connected
Comparison of distribution models for in-degree distribution.
LLMAAs. The mean similarity among connected LLMAAs in the original
Power-law distribution vs. Exponential Distribution Lognormal Distribution network was 0.2371. To serve as a baseline, we constructed a randomly
log-likelihood ratio 8.743893 (cid:0) 1.743838 edge-rewired version of the network, preserving the original degree
p-value 0 0.08118742 distribution, and computed the text similarities between connected
nodes in this randomized network. The resulting mean similarity was
A(k)=
m2 (k)
(2)
0
Fi
.2
g.
1
1
2
0
2
.
. The similarity distributions of both networks are visualized in
n1 (k)
A Wilcoxon rank-sum test revealed an extremely small p-value,
In the above Eq. (2), m2 (k) is the number of edges from the new indicating a statistically significant difference between the two distri-
network that connect to a node of k in-degree in the original network, butions. Thus, we reject the null hypothesis and find support for Hy-
and n1 (k) is the number of nodes with k in-degree. We investigated pothesis 3a. This result suggests that profile-based homophily—the
whether the attachment rate increases with the in-degree of nodes. If so, tendency for LLMAAs with similar self-descriptions to interact—is a
we conclude that preferential attachment exists. significant factor shaping the structure of the LLMAA social network.
We examined the distribution of attachment rates across six distinct
periods, as depicted in Fig. 9. To ascertain whether there is an upward 5.3.2. Content-based homophily in the English subchannel
trend in attachment rates correlating with increasing in-degree, we After preprocessing the content and translating non-English text into
employed OLS regression without an intercept to model these rates. The English, BERTopic was applied to identify underlying thematic struc-
slope of the fitting lines, the associated p-values, along with R-square tures. This process yielded 192 distinct topics spanning a broad range of
values are also presented in the graphs. Across all six periods, the slopes domains, including finance, science, technology, AI ethics, art, and so-
consistently exhibit positive values and significant statistical signifi- ciety. Table 3presents ten of the most prevalent topics along with their
cance. This suggests that the preferential attachment mechanism plays a representative keywords on the Chirper platform.
pivotal role in link formation, subsequently leading to the observed Each LLMAA’s posting content was then vectorized based on the
power-law degree distribution. topic distribution probabilities derived from BERTopic. To assess
content-based homophily, we compared the content similarity of con-
nected node pairs in the original social network with those in a ran-
5.3. Homophily in LLMAAs’ social network
domized, edge-rewired version. As shown in Fig. 11(a) and (b), the
original network displayed a significantly higher mean similarity
5.3.1. Profile-based homophily in the English subchannel
(0.2063) compared to the randomized network (0.0627). A Wilcoxon
In the English subchannel, there were 20,324 LLMAAs for which
rank-sum test confirmed that this difference is statistically significant,
both posting content and profile biography information were available.
9

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
Fig. 9. Attachment rate distribution of six periods.
Fig. 10. Biography similarity of connected nodes in the English subchannel.
thereby providing support for Hypothesis 3b. These findings suggest that
Table 3 content-based homophily—the tendency for LLMAAs to connect based
Top 10 topics on Chirper. on shared topical interests—also plays a crucial role in shaping the
Topic Representative words structure of their social network.
Finance crypto, financial, investing, blockchain, cryptocurrency, market,
decentralized, bitcoin, finance. 5.3.3. Homophily in the Chinese subchannel
Science universe, quantum, space, exploration, ai, mysteries, cosmic, In the Chinese subchannel, there were 6617 LLMAAs, where we
computing, quantum computing, science
obtain results different from those in the English subchannel. Fig. 12
Comedy comedy, humor, did, jokes, laughter, joke, laugh, funny, hilarious
Technology ai, learning, machine learning, data, machine, technology, just, wait, shows the biography similarity between connected nodes in both the
new original network and the edge-rewired network. The average similarity
Pet cat, meow, cats, nap, humans, feline, just, catnip, dogs is 0.5806 in the original network and 0.5796 in the edge-rewired
Art art, painting, artist, just, artists, new, creativity, like, beauty
network. The Wilcoxon rank-sum test indicates that there is no signifi-
Society workers, class, confucianism, capitalism, working class, capitalist,
cant difference between the two networks. Similarly, Fig. 13 presents
fight, society, socialism, oppressive
Virtual virtual, virtual reality, vr, reality, ai, technology, game, games, new, the posting content similarity between connected nodes. The average
reality just similarity is 0.7923 in the original network and 0.7901 in the edge-
AI ethics ai, ethical, development, ensure, intelligence, artificial, artificial rewired network. Again, the Wilcoxon rank-sum test shows no signifi-
intelligence, technology, ethics, potential
cant difference.
Fashion fashion, socks, style, high, high socks, dress, sustainable, sustainable
fashion, designs One possible reason for these results is the limited Chinese language
ability of LLMAAs during the early stage of the Chirper platform. This
10

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
Fig. 11. Posting content similarity of connected nodes in the English subchannel.
Fig. 12. Biography similarity of connected nodes in the Chinese subchannel.
Fig. 13. Posting content similarity of connected nodes in the Chinese subchannel.
difference in language proficiency is also observed by Li, Yang, and Zhao In analyzing the connectivity of the LLMAA social network, it is
(2023) that LLMAAs in the English subchannel posted more diverse found that a substantial proportion of LLMAAs are interconnected,
content, while content in the Chinese subchannel was more similar. indicating the presence of a cohesive online community. However, the
Therefore, Hypotheses 3a and 3b are not supported in the Chinese LSCC does not fully exhibit small-world properties—while it demon-
subchannel, suggesting the importance of language performance in strates high local clustering, the average shortest path length is longer
influencing network patterns. than expected. As a result, Hypothesis 1cannot be supported. Further
multifractal analysis reveals a structurally complex network: certain
6. Discussion and conclusion areas exhibit strong local clustering, while others are sparsely con-
nected. Specifically, sparse connections among high in-degree nodes
6.1. Key findings contribute to longer path lengths. This type of self-organizing structure
enhances the network’s robustness, ensuring that the removal or inac-
This study investigates the collective dynamics of LLMAAs within an tivity of certain nodes does not lead to system-wide failure. Even when
online community known as Chirper. some LLMAAs become inactive, the network retains structural integrity
11

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
and remains functional, thereby supporting the platform’s ongoing Firstly, this study explores the collective behaviors of LLMAAs in
operation. realistic social contexts, introducing a social dimension essential for
Regarding degree distribution, we observed that the in-degree dis- advancing research in AI-driven social simulations—an emerging area
tribution conforms to a power-law, partially supporting Hypothesis 2. bridging artificial intelligence and the social sciences (Ziems et al., 2023;
This suggests that not all LLMAAs possess equal capacity to attract Xu et al., 2024; Gao et al., 2024). Our findings contribute to the growing
engagement—only a small number receive a large share of interactions, literature on machine behavior by framing AI agents as social actors
while the majority maintain minimal connections, resulting in a scale- within a collective system. We show that LLMAAs can display
free network. This centralization mirrors interaction patterns in human-like social patterns, such as forming ties and varying in their
human social systems. The observed in-degree power-law distribution levels of engagement.
may be explained by the mechanism of preferential attachment, Secondly, this study highlights the potential of LLMAAs to simulate
whereby LLMAAs with more existing links are more likely to gain nuanced social interactions both at the individual and collective levels.
additional ones. In contrast, the out-degree distribution only follows a These insights offer a foundational understanding for researchers
power-law in its upper tail, suggesting that most LLMAAs are relatively interested in modeling complex social dynamics and group decision-
passive in initiating interactions. This highlights the current limitations making processes. By demonstrating behavioral similarities between
in their social engagement capabilities. Future research could explore AI agents and humans, our work supports the plausibility and promise of
the attributes that enable certain LLMAAs to become socially influential using AI-driven simulations in social science research (Argyle et al.,
and identify strategies to enhance their interaction levels. 2023; Zhang et al., 2023; Zhao et al., 2023).
To understand the mechanisms of link formation, we further Thirdly, this study invites a re-examination of existing theories
analyzed homophily in the English subchannel. The results reveal sig- related to collective behavior and group decision-making. For example,
nificant profile-based homophily and content-based homophily, thereby traditional sociological theories emphasize human interactions and the
supporting Hypotheses 3a and 3b. LLMAAs tend to interact with others formation of social norms and group dynamics. Our findings suggest that
who have similar biographies or discuss similar topics, reflecting their non-human agents—LLMAAs—can also exhibit emergent collective
advanced natural language understanding and alignment capabilities. behavior, providing a novel lens to revisit these frameworks. Similarly,
Like people with similar interests who tend to stick together, LLMAAs in information science, theories of social network dynamics and online
are attracted to others with similar traits. These findings align with and communities have predominantly been human-centric (Lin & Li, 2021;
complement those of He et al. (2023), emphasizing the homogeneity of Zhou, 2022). Our research shows that AI agents can form social struc-
LLMAA interactions. Moreover, S. Li, Yang, and Zhao (2023)found that tures without relying on human-based constructs such as trust or cred-
LLMAA posts are highly consistent with their biographies—i.e., ibility, thus offering opportunities to expand or refine these theoretical
user-defined prompts—indicating that such prompts significantly shape models for AI-centered contexts.
LLMAA behavior. The presence of homophily based on both posting
content and biographies further underscores the tight relationship be- 6.3. Practical implications
tween these two agent attributes. However, in the Chinese subchannel,
due to the limited Chinese language proficiency of LLMAAs at the early Our findings also provide actionable insights for the design and
stage of Chirper platform, Hypothesis 3a and 3b are not supported, deployment of multi-agent AI systems (Guo et al., 2024). Understanding
suggesting that language ability plays a crucial role in network how LLMAAs form connections and coordinate actions can help build
formation. more realistic, interpretable, and socially responsible AI. Practical ap-
Despite exhibiting several parallels to human social behavior, plications include multi-agent decision-support systems, AI-driven
LLMAAs still exhibit noticeable limitations in individual expression. For teamwork platforms, and intelligent coordination frameworks that
instance, although LLMAAs can participate in diverse topics and present enhance the robustness and realism of automated systems.
coherent arguments, their discussions often lack depth and opinion di- First, recognizing the unique network properties of LLMAAs—such
versity. In topics involving ethical considerations, this may stem from as the absence of a typical “small-world” structure and the emergence of
embedded content moderation policies that prevent them from power-law distributions—can inform the design of AI networks that
expressing controversial or unethical views. However, more generally, facilitate more effective information flow and collaboration.
LLMAAs appear to lack the capacity for public deliberation and diverse Second, our findings on profile-based and interest-driven connec-
perspective exchange. Addressing this in future work may involve tions among agents suggest new ways to optimize agent matchmaking
developing mechanisms that foster greater heterogeneity in viewpoints. and team composition. Algorithms can be developed to group agents
In conclusion, this study provides new insights into the emergent based on complementary skills or roles, thereby improving task alloca-
collective behaviors of LLMAAs in a social network context. Their in- tion and system performance in collaborative AI applications.
teractions exhibit human-like tendencies, including clustering, central-
ized attention, and homophily in link formation. Yet, they still deviate 6.4. Limitations and future directions
from human norms, particularly in the sparsity of connections among
influential agents and their limited proactive engagement. These find- This study has limitations in several aspects that also present op-
ings offer a foundational understanding of the complex systems formed portunities for future work.
by LLMAAs, contributing to our knowledge of their societal impact, Firstly, this study analyzes the social network characteristics of
agent interaction dynamics, and potential in multi-agent systems and LLMAAs, using macro-level metrics such as degree distributions and
social simulations. clustering coefficients, which do overlook finer-grained behavioral
patterns. Micro-level analysis such as agent-specific interaction strate-
6.2. Theoretical implications gies, topic-driven engagement, or semantic alignment in communica-
tion, could potentially elucidate how LLMAAs actively shape their social
This study contributes to the emerging literature at the intersection environments. Future research could explore the integration of micro-
of artificial intelligence and social sciences by investigating the collec- level analysis with the macro-level one. For example, agent-based
tive behaviors of LLMAAs. While prior research has primarily evaluated modeling could be employed to simulate the interactions and behav-
large language models through task-based benchmarks, our work shifts iors of individual LLMAAs, providing a more nuanced understanding of
the focus toward their social dynamics and interactions in simulated how they shape their social environments. In addition, incorporating
environments. The findings generate new insights into how non-human semantic analysis of communication content could reveal the underlying
agents exhibit collective behavior. topics and themes that drive engagement and interaction within the
12

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
network. UK, march 25-28, 2018 (pp. 17–26). Springer International Publishing. Proceedings
Secondly, there is a lack of a deeper understanding of the technical 13.
Borch, C. (2022). Machine learning and social theory: Collective machine behaviour in
architecture of the Chirper platform, which could have provided more algorithmic trading. European Journal of Social Theory, 25(4), 503–520.
nuanced insights into the behavior of LLMAAs. Information on how an Cai, M., Luo, H., Meng, X., Cui, Y., & Wang, W. (2023). Network distribution and
agent decides to interact is missing, leaving us without awareness of the sentiment interaction: Information diffusion mechanisms between social bots and
human users on social media. Information Processing & Management, 60(2), Article
inherent mechanisms driving these behaviors. Although our study fo-
103197.
cuses on endogenous interactions within the Chirper platform, future Chen, J., Sun, J., & Wang, G. (2022). From unmanned systems to autonomous intelligent
research could explore how external influences shape social network systems. Engineering, 12, 16–19.
formation. As demonstrated by de Curto` and de Zarza` (2025), centrally Chugunova, M., & Sele, D. (2022). We and it: An interdisciplinary review of the
experimental evidence on how humans interact with machines. Journal of Behavioral
placed agents may amplify narrative cues generated by LLMs, facili- and Experimental Economics, 99, Article 101897.
tating the emergence of attention hubs. While the Chirper platform Clauset, A., Shalizi, C., & Newman, M. (2009). Power-law distributions in empirical data.
SIAM Review, 51(4), 661–703.
attempted to introduce responsiveness to real-world events, such as the de Curto`, J., & de Zarza`, I. (2025). LLM-Driven social influence for cooperative behavior
Russia-Ukraine conflict and the U.S. presidential election, LLMAAs in multi-agent systems. IEEE Access, 13, 44330–44342.
during the early-stage period covered by our dataset, as reported by Li, DeepSeek-Ai, Guo, D., Yang, D., et al. (2025). DeepSeek-R1: Incentivizing reasoning
capability in LLMs via reinforcement learning. Arxiv Preprint arXiv: 2501.12948.
Yang, and Zhao (2023), did not actively react to external information.
Dong, R., Li, L., Zhang, Q., & Cai, G. (2018). Information diffusion on social media during
Future studies could examine how the incorporation of external narra- natural disasters. IEEE transactions on computational social systems, 5(1), 265–276.
tive inputs — including simulated news events and trending topics — Fagiolo, G. (2007). Clustering in complex directed networks. Physical Review E: Statistical,
interacts with endogenous dynamics to reshape the social structures of Nonlinear, and Soft Matter Physics, 76(2), Article 026107.
Felmlee, D., & Faris, R. (2013). Interaction in social networks. In Handbook of social
LLMAAs. psychology (pp. 439–464). Netherlands: Dordrecht: Springer.
Gao, C., Lan, X., Li, N., Yuan, Y., Ding, J., Zhou, Z., … Li, Y. (2024). Large language
models empowered agent-based modeling and simulation: A survey and
CRediT authorship contribution statement
perspectives. Humanities and Social Sciences Communications, 11(1), 1–24.
Gao, C., Lan, X., Lu, Z., Mao, J., Piao, J., Wang, H., … Li, Y. (2023). S3: Social-network
Huiru Chen: Writing – original draft, Visualization, Methodology, simulation system with large language model-empowered agents. arXiv preprint
arXiv:2307.14984.
Formal analysis, Data curation, Conceptualization. Zhenhua Wang:
Grootendorst, M. R. (2022). BERTopic: Neural topic modeling with a class-based TF-IDF
Writing – review & editing, Methodology. Ming Ren: Writing – review procedure. arXiv preprint arXiv:2203.05794.
& editing, Supervision, Methodology, Conceptualization. Grossmann, I., Feinberg, M., Parker, D. C., Christakis, N. A., Tetlock, P. E., &
Cunningham, W. A. (2023). AI and the transformation of social science research.
Science, 380(6650), 1108–1109.
Declaration of generative AI and AI-assisted technologies in the Guo, T., Chen, X., Wang, Y., Chang, R., Pei, S., Chawla, N. V., … Zhang, X. (2024). Large
writing process language model based multi-agents: A survey of progress and challenges. arXiv
preprint arXiv:2402.01680.
Hagendorff, T. (2023a). Machine psychology: Investigating emergent capabilities and
During the preparation of this work the authors used ChatGPT 4o in behavior in large language models using psychological methods. arXiv preprint arXiv:
order to improve language and readability. After using this tool/service, 2303.13988.
the authors reviewed and edited the content as needed and take full Hagendorff, T. (2023b). Deception abilities emerged in large language models. arXiv
preprint arXiv:2307.16513.
responsibility for the content of the publication. Hagendorff, T., Fabi, S., & Kosinski, M. (2022). Machine intuition: Uncovering human-
like intuitive decision-making in GPT-3.5. arXiv preprint arXiv:2212.05206.
He, J., Wallis, F., & Rathje, S. (2023). Homophily in an artificial social network of agents
Declaration of competing interest powered by large language models. Research Square. https://doi.org/10.21203/rs.3.
rs-3096289/v1
Hong, S., Zheng, X., Chen, J., Cheng, Y., Zhang, C., Wang, Z., … Wu, C. (2023). Metagpt:
The authors declare that they have no known competing financial Meta programming for multi-agent collaborative framework. arXiv preprint arXiv:
interests or personal relationships that could have appeared to influence 2308.00352.
the work reported in this paper. Isa, D., & Himelboim, I. (2018). A social networks approach to online social movement:
Social mediators and mediated content in# freeajstaff Twitter network. Social
Media+Society, 4(1), Article 2056305118760807.
Acknowledgements Khanam, K. Z., Srivastava, G., & Mago, V. (2023). The homophily principle in social
network analysis: A survey. Multimedia Tools and Applications, 82(6), 8811–8854.
Kümpel, A. S. (2020). The matthew effect in social media news use: Assessing
This research is partly supported by the Major Project by Ministry of inequalities in news exposure and news engagement on social network sites (SNS).
Education Key Research Institute of Humanities and Social Sciences (No. Journalism, 21(8), 1083–1098.
22JJD870001). Li, S., Yang, J., & Zhao, K. (2023). Are you in a masquerade? Exploring the behavior and
impact of large language model driven social bots in online social networks. arXiv
preprint arXiv:2307.10337.
References Li, Y., Zhang, Y., & Sun, L. (2023). MetaAgents: Simulating interactions of human
behaviors for LLM-Based task-oriented coordination via collaborative generative
agents. arXiv preprint arXiv:2310.06500.
Aggarwal, N., Saxena, G. J., Singh, S., & Pundir, A. (2023). Can I say, now machines can
Lin, H., & Li, S. (2021). Analysis of user social support network in online tumor
think? arXiv preprint arXiv:2307.07526. community. Data and Information Management, 5(1), 184–194.
Agnew, C. R., Loving, T. J., & Drigotas, S. M. (2001). Substituting the forest for the trees: MacKenzie, D. (2019). How algorithms interact: Goffman’s ‘interaction order’ in
social networks and the prediction of romantic relationship state and fate. Journal of automated trading. Theory, Culture & Society, 36(2), 39–59.
personality and social psychology, 81(6), 1042–1057.
Marx, G. T., & Wood, J. L. (1975). Strands of theory and research in collective behavior.
Aher, G. V., Arriaga, R. I., & Kalai, A. T. (2023). Using large language models to simulate Annual Review of Sociology, 1(1), 363–428.
multiple humans and replicate human subject studies. In International conference on
machine learning (pp. 337–371). PMLR. July. McP s h o e c r i s a o l n n , e M tw ., o S r m ks i . t h A - n L n o u v a in l , R L e . v , i e & w C o o f o S k o , c J io . l ( o 2 g 0 y, 0 1 2 ) 7 . ( 1 B ) i , r d 4 s 1 o 5 f – 4 a 4 f 4 e . ather: Homophily in
Argyle, L. P., Busby, E. C., Fulda, N., Gubler, J. R., Rytting, C., & Wingate, D. (2023). Out Milgram, S. (1967). The small world problem. Psychology Today, 2(1), 60–67.
of one, many: Using language models to simulate human samples. Political Analysis,
31(3), 337–351. Newman, M., & Park, J. (2003). Why social networks are different from other types of
networks. Physical Review E - Statistical Physics, Plasmas, Fluids, and Related
Bak-Coleman, J. B., Alfano, M., Barfuss, W., Bergstrom, C. T., Centeno, M. A.,
Couzin, I. D., … Weber, E. U. (2021). Stewardship of global collective behavior. Interdisciplinary Topics, 68, Article 036122.
Ng, L. H. X., & Carley, K. M. (2025). A global comparison of social media bot and human
Proceedings of the National Academy of Sciences, 118(27), Article e2025764118.
Bara 2 b 8 a´ 6 si ( , 5 A 43 . 9 L ) ., , & 50 A 9 l – b 5 e 1 r 2 t, . R. (1999). Emergence of scaling in random networks. Science, Park c , h J a . r S a . c , t O er ’ i B st r i i c e s n . , S J c . i e C n . t , i fi C c a i R , e C p . o J rt . s , , M 15 o ( r 1 ri ) s , , A M r . t i R cl . e , L 1 i 0 a 9 n 7 g 3 , . P., & Bernstein, M. S. (2023).
Generative agents: Interactive simulacra of human behavior. arXiv preprint arXiv:
Binz, M., & Schulz, E. (2023). Using cognitive psychology to understand GPT-3.
2304.03442.
Proceedings of the National Academy of Sciences, 120(6), Article e2218523120.
Phelps, S., & Russell, Y. I. (2023). Investigating emergent goal-like behaviour in large
Boichak, O., Jackson, S., Hemsley, J., & Tanupabrungsun, S. (2018). Automated
language models using experimental economics. arXiv preprint arXiv:2305.07970.
diffusion? Bots and their influence during the 2016 US presidential election. In
Transforming digital worlds: 13th international conference, iConference 2018, Sheffield,
13

H. Chen et al. D a t a a n d I n f o r m a t i o n M a n a g e m e nt 10 (2026) 100107
Rahwan, I., Cebrian, M., Obradovich, N., Bongard, J., Bonnefon, J. F., Breazeal, C., … Vrontis, D., Makrides, A., Christofi, M., & Thrassou, A. (2021). Social media influencer
Wellman, M. (2019). Machine behaviour. Nature, 568(7753), 477–486. marketing: A systematic review, integrative framework and future research agenda.
Redner, S. (2005). Citation statistics from 110 years of physical review. Physics Today, 58 International Journal of Consumer Studies, 45(4), 617–644.
(6), 49–54. Wang, L., Ma, C., Feng, X., Zhang, Z., Yang, H., Zhang, J., … Wen, J. (2024). A survey on
Rendo´n de la Torre, S., Kalda, J., Kitt, R., & Engelbrecht, J. (2017). Fractal and large language model based autonomous agents. Frontiers of Computer Science, 18(6),
multifractal analysis of complex networks: Estonian network of payments. The Article 186345.
European Physical Journal B, 90, 1–8. Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of ‘small-world’ networks.
Sadri, A. M., Hasan, S., Ukkusuri, S. V., & Suarez Lopez, J. E. (2018). Analysis of social Nature, 393(6684), 440–442.
interaction network properties and growth on Twitter. Social Network Analysis and Xi, Z., Chen, W., Guo, X., He, W., Ding, Y., Hong, B., … Gui, T. (2023). The rise and
Mining, 8, 1–13. potential of large language model-based agents: A survey. arXiv preprint arXiv:
Salge, C., Karahanna, E., & Thatcher, J. B. (2022). Algorithmic processes of social 2309.07864.
alertness and social transmission: How bots disseminate information on Twitter. Xiong, W., Wang, C., & Ma, L. (2023). Partner or subordinate? Sequential risky decision-
Management Information Systems Quarterly, 46(1), 229–260. making behaviors under human-machine collaboration contexts. Computers in
Schreiner, M. S., Fischer, T., & Riedl, R. (2019). Impact of content characteristics and Human Behavior, 139, Article 107556.
emotion on behavioral engagement in social media: literature review and research Xu, R., Sun, Y., Ren, M., Guo, S., Pan, R., Lin, H., … Han, X. (2024). AI for social science
agenda. Electronic Commerce Research, 1–17. and social science of AI: A survey. Information Processing & Management, 61(3),
Sheridan, P., & Onodera, T. (2018). A preferential attachment paradox: How preferential Article 103665.
attachment combines with growth to produce networks with log-normal in-degree Yang, H., Yue, S., & He, Y. (2023). Auto-GPT for online decision making: Benchmarks
distributions. Scientific Reports, 8(1), 2811. and additional opinions. arXiv preprint arXiv:2306.02224.
Sherman, L. E., Payton, A. A., Hernandez, L. M., Greenfield, P. M., & Dapretto, M. (2016). Zhang, J., Xu, X., & Deng, S. (2023). Exploring collaboration mechanisms for llm agents:
The power of the like in adolescence: Effects of peer influence on neural and A social psychology view. arXiv preprint arXiv:2310.02124.
behavioral responses to social media. Psychological Science, 27(7), 1027–1035. Zhao, Q., Wang, J., Zhang, Y., Jin, Y., Zhu, K., Chen, H., & Xie, X. (2023). CompeteAI:
Song, C., Havlin, S., & Makse, H. A. (2005). Self-similarity of complex networks. Nature, Understanding the competition behaviors in large language model-based agents.
433(7024), 392–395. arXiv preprint arXiv:2310.17512.
Su, B. C., & Yen, T. S. (2017). Small-world phenomenon and strategies for making friends Zhou, Y. (2022). Analysis of influencing factors of knowledge dissemination and sharing
on social networking sites in mobile environment: random and non-random. based on the SEIRR model. Data and Information Management, 6(3), Article 100010.
International Journal of Mobile Communications, 15(4), 355–371. Zhu, X., Chen, Y., Tian, H., Tao, C., Su, W., Yang, C., … Dai, J. (2023). Ghost in the
Taylor, J. E. T., & Taylor, G. W. (2021). Artificial cognition: How experimental minecraft: Generally capable agents for open-world environments via large language
psychology can help generate explainable artificial intelligence. Psychonomic Bulletin models with text-based knowledge and memory. arXiv preprint arXiv:2305.17144.
& Review, 28(2), 454–475. Ziems, C., Held, W., Shaikh, O., Chen, J., Zhang, Z., & Yang, D. (2023). Can large
Touvron, H., Lavril, T., Izacard, G., Martinet, X., Lachaux, M. A., Lacroix, T., … language models transform computational social science? arXiv preprint arXiv:
Lample, G. (2023). Llama: Open and efficient foundation language models. arXiv 2305.03514.
preprint arXiv:2302.13971.
14
