---
telephone_index: 2
title: "Simulating Rumor Spreading in Social Networks using LLM Agents"
category: 05_misinformation_correction
venue: "arXiv"
year: 2025
doi: 
arxiv_id: 2502.01450
preferred_source_type: preprint_or_unresolved
publisher_url: https://arxiv.org/abs/2502.01450
quality_flags: ["abstract_may_include_layout_noise"]
---

# Citation Context

- Telephone index: 2
- Preferred source: arXiv
- DOI: none
- arXiv: 2502.01450
- PDF: `assets\papers\pdf\05_misinformation_correction\02_simulating-rumor-spreading-in-social-networks-using-llm-agents.pdf`

## Extracted Abstract

With the rise of social media, misinformation has become increasingly prevalent, fueled largely by the spread of rumors. This study explores the use of Large Language Model (LLM) agents within a novel framework to simulate and analyze the dynamics of rumor propagation across social networks. To this end, we design a variety of LLM-based agent types and construct four distinct network structures to conduct these simulations. Our framework assesses the effectiveness of different network constructions and agent behaviors in influencing the spread of rumors. Our results demonstrate that the framework can simulate rumor spreading across more than one hundred agents in various networks with thousands of edges. The evaluations indicate that network structure, personas, and spreading schemes can significantly influence rumor dissemination, ranging from no spread to affecting 83% of agents in iterations, thereby offering a realistic simulation of rumor spread in social networks. The code of this project is available at https://github.com/neerajas-group/rumors-inmulti-agent. Introduction Understanding human behaviors within social networks is critical across various domains in social sciences. In recent years, the rapid growth of Large Language Models (LLMs) has shown great potential for making LLMs act like humans and simulate social networks (Chen et al. 2024). LLMs demonstrate the ability to adapt to different backgrounds and personalities through in-context learning, effectively simulating human beings (Chuang et al. 2024). The traditional studies (Hamidian and Diab 2019; Kaligotla, Yu¨cesan, and Chick 2015) of social networks predominantly emphasize mathematical equations, statistical analyses, and simplistic agent models. However, these approaches often constrain their ability to accurately simulate the diverse personalities and complex dynamics inherent in real social networks, potentially leading to significant impacts on both the processes and outcomes of such studies. With the growing capabilities of LLMs (Radford et al. 2018), utilizing them as agents to facilitate communication within social networks presents a promising approach to studying human behavior under various conditions. Copyright © 2023, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved. 5202 beF 3 ]IS.sc[ 1v05410.2052:viXra In this study, we introduce a novel framework utilizing LLM-based agents to examine the spread of rumors and misinformation within social networks. Our approach enhances the traditional simulations of rumor dynamics by incorporating LLMs as dynamic agents, offering a more realistic exploration of information dissemination. To accurately simulate users in a social network, we employ an LLM to drive each agent with various personas and their preferences for accepting and spreading rumors, as defined by prompts. Each agent is associated with a post history that includes all posts from itself and its neighbors, along with a record of its beliefs about each rumor, based on the LLM’s output. Additionally, our dual-simulation framework accounts for both network properties and individual agent characteristics, providing a holistic view of how these factors jointly influence rumor dynamics. This research not only demonstrates the utility of LLMs in understanding rumor spreading but also provides significant insights into the behavioral simulation capabilities of LLM-based agent societies. Related Work Modeling rumor spreading In social network analysis, the spread of rumors is an important problem that has garnered extensive research and exploration. This is a network science topic where people tend to utilize statistical modeling and probabilistic analysis to formulate the network and define the spread of rumors. Common approaches include building statistical models with constraints (Zehmakan, Out, and Khelejan 2023) and defining multiple parameters that could affect the network (Chen and Wang 2020). However, these methods may not accurately reflect the individuals and the randomness in realworld societies. There are works that use traditional agentbased modeling (ABM) to simulate the spread of rumors in a bottom-up approach, including using NetLogo (Wilensky 1999) agents as nodes in a social network (Kaligotla, Yu¨cesan, and Chick 2015) and defining mathematical models for agents (Zehmakan, Out, and Khelejan 2023). However, these agents are still highly dependent on the definition of their mathematical properties. LLM-based Agents In recent years, we have seen the flourishing of LLM (OpenAI 2024) and its emergent abilities that perform well in various tasks. Recently, many studies have demonstrated the ability of LLMs to drive agents in ABM to simulate general human behavior (Park et al. 2023; Chuang et al. 2024). LLM-based agents also demonstrate strong language comprehension and perform well in tasks guided by natural language instructions (Chen et al. 2024). However, these studies primarily focus on utilizing LLMs as individual agents or basic agent communications, overlooking the potential for evaluating LLMs within a network graph to examine rumor propagation in complex social networks. Methods To demonstrate the capabilities of LLMs in simulating the spread of rumors and their mitigation within social networks, we aim to: (a) construct various social networks, (b) design and implement multiple LLM-based agents as part of an ABM framework operating within the networks, and (c) evaluate both the propagation of rumors and the effectiveness of potential mitigation strategies. Network Construction Network analysis represents individuals and their relationships as nodes and edges, respectively. In the context of rumor propagation, the social network models a social media environment where individuals interact with friends and share personal sentiments and rumors. To characterize this network, we propose that nodes represent users within the social network, while edges signify the friendship relationships between pairs of users (nodes). As friends can view each other’s messages, this network is defined as an undirected network. The structure of a network significantly influences behavior in simulations (Alam and Geller 2011). To investigate this, we construct various networks for simulation and analysis, employing two approaches: Synthetic Networks. We algorithmically generate networks with specific characteristics, including Erdo˝sRe´nyi networks (Erdo¨s and Re´nyi 1959), Scale-Free networks (Baraba´si and Bonabeau 2003), and Small-World networks (Watts and Strogatz 1998). These networks enable us to examine the relationship between rumor-spreading and network properties. Real-World Networks. To simulate more realistic scenarios, we utilize real-world social network data collected from Facebook to generate various networks (Leskovec and Mcauley 2012). Our objective is to evaluate the spread of rumors across all network types and to explore how network characteristics influence rumor propagation. LLM-based Agent In these networks, each node n represents an agent a i i driven by an LLM, as illustrated in Figure 1a and Algorithm 1. We use a consistent basic prompt structure and the ChatGPT-4o-mini (OpenAI 2024) for each agent a , but cusi tomize each prompt with unique information specific to each agent a . The prompt includes the following components: (a) i Task description and examples that instruct the LLM to generate responses in the correct syntax; (b) Agent personas p , i (a) Network with LLM-based (b) At each iteration, the agents; each agent maintains agent generates a post, apits own post history and ru- pends it to its own and its mor beliefs. neighbor’s history, and updates its rumor belief.
Title: 02_simulating-rumor-spreading-in-social-networks-using-llm-agents

Source PDF: D:\0-Research\5-Telephone\assets\papers\pdf\05_misinformation_correction\02_simulating-rumor-spreading-in-social-networks-using-llm-agents.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-06-20T12:38:44+00:00
- page_count: 7
- status: ok
- text_char_count: 27749

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- none

Markdown Content:

Simulating Rumor Spreading in Social Networks using LLM Agents
Tianrui Hu,1 † Dimitrios Liakopoulos,1 † Xiwen Wei,1 Radu Marculescu,1 Neeraja J. Yadwadkar1
1University of Texas at Austin, USA
tianrui@utexas.edu, dimliak@utexas.edu, xiwenwei@utexas.edu, radum@utexas.edu, neeraja@austin.utexas.edu
†These authors contributed equally to this work.

Abstract
With the rise of social media, misinformation has become increasingly prevalent, fueled largely by the spread of rumors.
This study explores the use of Large Language Model (LLM)
agents within a novel framework to simulate and analyze the
dynamics of rumor propagation across social networks. To
this end, we design a variety of LLM-based agent types and
construct four distinct network structures to conduct these
simulations. Our framework assesses the effectiveness of different network constructions and agent behaviors in influencing the spread of rumors. Our results demonstrate that the
framework can simulate rumor spreading across more than
one hundred agents in various networks with thousands of
edges. The evaluations indicate that network structure, personas, and spreading schemes can significantly influence rumor dissemination, ranging from no spread to affecting 83%
of agents in iterations, thereby offering a realistic simulation
of rumor spread in social networks. The code of this project
is available at https://github.com/neerajas-group/rumors-inmulti-agent.
Introduction
Understanding human behaviors within social networks is
critical across various domains in social sciences. In recent
years, the rapid growth of Large Language Models (LLMs)
has shown great potential for making LLMs act like humans and simulate social networks (Chen et al. 2024). LLMs
demonstrate the ability to adapt to different backgrounds and
personalities through in-context learning, effectively simulating human beings (Chuang et al. 2024). The traditional
studies (Hamidian and Diab 2019; Kaligotla, Yu¨cesan, and
Chick 2015) of social networks predominantly emphasize
mathematical equations, statistical analyses, and simplistic
agent models. However, these approaches often constrain
their ability to accurately simulate the diverse personalities
and complex dynamics inherent in real social networks, potentially leading to significant impacts on both the processes
and outcomes of such studies. With the growing capabilities
of LLMs (Radford et al. 2018), utilizing them as agents to
facilitate communication within social networks presents a
promising approach to studying human behavior under various conditions.
Copyright © 2023, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
5202
beF
3
]IS.sc[
1v05410.2052:viXra

In this study, we introduce a novel framework utilizing
LLM-based agents to examine the spread of rumors and
misinformation within social networks. Our approach enhances the traditional simulations of rumor dynamics by incorporating LLMs as dynamic agents, offering a more realistic exploration of information dissemination. To accurately
simulate users in a social network, we employ an LLM to
drive each agent with various personas and their preferences
for accepting and spreading rumors, as defined by prompts.
Each agent is associated with a post history that includes all
posts from itself and its neighbors, along with a record of its
beliefs about each rumor, based on the LLM’s output. Additionally, our dual-simulation framework accounts for both
network properties and individual agent characteristics, providing a holistic view of how these factors jointly influence
rumor dynamics. This research not only demonstrates the
utility of LLMs in understanding rumor spreading but also
provides significant insights into the behavioral simulation
capabilities of LLM-based agent societies.
Related Work
Modeling rumor spreading
In social network analysis, the spread of rumors is an important problem that has garnered extensive research and exploration. This is a network science topic where people tend to
utilize statistical modeling and probabilistic analysis to formulate the network and define the spread of rumors. Common approaches include building statistical models with
constraints (Zehmakan, Out, and Khelejan 2023) and defining multiple parameters that could affect the network (Chen
and Wang 2020). However, these methods may not accurately reflect the individuals and the randomness in realworld societies. There are works that use traditional agentbased modeling (ABM) to simulate the spread of rumors
in a bottom-up approach, including using NetLogo (Wilensky 1999) agents as nodes in a social network (Kaligotla,
Yu¨cesan, and Chick 2015) and defining mathematical models for agents (Zehmakan, Out, and Khelejan 2023). However, these agents are still highly dependent on the definition
of their mathematical properties.
LLM-based Agents
In recent years, we have seen the flourishing of LLM (OpenAI 2024) and its emergent abilities that perform well in

various tasks. Recently, many studies have demonstrated the
ability of LLMs to drive agents in ABM to simulate general human behavior (Park et al. 2023; Chuang et al. 2024).
LLM-based agents also demonstrate strong language comprehension and perform well in tasks guided by natural language instructions (Chen et al. 2024). However, these studies primarily focus on utilizing LLMs as individual agents or
basic agent communications, overlooking the potential for
evaluating LLMs within a network graph to examine rumor
propagation in complex social networks.
Methods
To demonstrate the capabilities of LLMs in simulating the
spread of rumors and their mitigation within social networks, we aim to: (a) construct various social networks, (b)
design and implement multiple LLM-based agents as part of
an ABM framework operating within the networks, and (c)
evaluate both the propagation of rumors and the effectiveness of potential mitigation strategies.
Network Construction
Network analysis represents individuals and their relationships as nodes and edges, respectively. In the context of
rumor propagation, the social network models a social media environment where individuals interact with friends and
share personal sentiments and rumors. To characterize this
network, we propose that nodes represent users within the
social network, while edges signify the friendship relationships between pairs of users (nodes). As friends can view
each other’s messages, this network is defined as an undirected network. The structure of a network significantly influences behavior in simulations (Alam and Geller 2011).
To investigate this, we construct various networks for simulation and analysis, employing two approaches:
Synthetic Networks. We algorithmically generate networks with specific characteristics, including Erdo˝sRe´nyi networks (Erdo¨s and Re´nyi 1959), Scale-Free networks (Baraba´si and Bonabeau 2003), and Small-World networks (Watts and Strogatz 1998). These networks enable us
to examine the relationship between rumor-spreading and
network properties.
Real-World Networks. To simulate more realistic scenarios, we utilize real-world social network data collected
from Facebook to generate various networks (Leskovec and
Mcauley 2012).
Our objective is to evaluate the spread of rumors across all
network types and to explore how network characteristics
influence rumor propagation.
LLM-based Agent
In these networks, each node n represents an agent a
i i
driven by an LLM, as illustrated in Figure 1a and Algorithm 1. We use a consistent basic prompt structure and the
ChatGPT-4o-mini (OpenAI 2024) for each agent a , but cusi
tomize each prompt with unique information specific to each
agent a . The prompt includes the following components: (a)
i
Task description and examples that instruct the LLM to generate responses in the correct syntax; (b) Agent personas p ,
i

(a) Network with LLM-based (b) At each iteration, the
agents; each agent maintains agent generates a post, apits own post history and ru- pends it to its own and its
mor beliefs. neighbor’s history, and updates its rumor belief.
Figure 1: Design of LLM-based multi-agent network.
Algorithm 1: Simulating Rumor Spread with LLM Agents
1: Input: G social network, N agent personas {p }N , L list of
i i=1
rumors {r }L , number of time steps T
j i=j
2: Output: B, the belief in rumors, where ⟨b ⟩ ∈ [0, 1] repreij
sents the belief of agent a in rumor r .
i j
3: for i = 1 to N do ▷ Agent Initialization
4: Assign node n of G to agent a
i i
5: Initialize agent a with persona p
i i
6: friend list = {}
i
7: for each edge e in G connecting n to n do
ix i x
8: Add a to friend list
x i
9: end for
10: end for
11: for j = 1 to L do ▷ Rumor Initialization
12: Select an agent a based on Initialization Strategy
i
13: Append r to a post history.
j i
14: end for
15: for t = 1 to T do ▷ Simulation
16: Select an agent a based on Activation Strategy
i
17: Agent a reads post history and makes a new post
i
18: for a in {a , friend list } do
x i i
19: Add the new post to post history of a
x
20: end for
21: for j = 1 to L do
22: Agent a updates opinion of r to ⟨b ⟩ in B
i j ij
23: end for
24: end for
including name, age, job, personality traits, and the agent’s
willingness to accept and spread rumors, tailored to each
agent; (c) Rumors previously believed by the agent; (d) Posts
visible to the agent; (e) A complete list of all rumors.
Component (a) directs the LLM to generate a new post
based on information from (b), (c), and (d), and to evaluate the agent’s belief in each rumor ⟨b ⟩ in the overall ruij
mor matrix B according to (e). This setup simulates a user
reading posts, creating a new post, and updating opinions on
various rumors. Initially, each agent is assigned some random messages, which include the rumors r to be tested.
j
The agents that have the rumors in their initial post histories are determined by the Initialization Strategy. This could
either be fully random or a degree-based selection, where
the rumors always start with the agents that have the highest
degrees (most number of friends).
As Figure 1b illustrates, in each iteration, an agent a is
i
selected in accordance with the Activation Strategy, where

the probability of an agent’s selection may be either fully
random or proportional to its degree. This models the realistic social dynamic wherein individuals with a larger number
of connections tend to disseminate more posts. The agent
a feeds the prompt to the LLM and generates a response
i
that contains a new post and its updated belief in each rumor, denoted as ⟨b ⟩. It then appends the new post to its
ij
own history as well as to the histories of connected nodes in
f riend list , while simultaneously updating its opinions on
i
all rumors in B.
Scalability
Recent work (Li et al. 2024) demonstrates that LLM-based
agents can be effectively scaled to enhance overall performance. This aligns with our observations when scaling our
design to a network comprising over 100 nodes and 1000
edges. The complexity of Algorithm 1 is O(T (N + B)),
where T is the number of iterations, N is the number of
agents, and B is the number of rumors. In each step, an inference request is sent to the LLM, and the response is appended as input for subsequent requests. Thus, further scaling the networks could significantly increase the length of
inputs and outputs for each LLM request, leading to a surge
in computational costs and potentially reducing accuracy in
managing long contexts. Future work could include implementing an efficient compression method for post history,
parallelizing the agents, and enhancing LLM serving optimizations (Zheng et al. 2023) to improve scalability.
Experiments
Experiment Setup. We implemented functions to generate
four network types: (a) an Erdo˝s-Re´nyi random network, (b)
a Scale-Free network, (c) a Small World network, and (d) a
real-world network using Facebook’s structure. Each structure has unique properties as shown in Table 1. Next, we
assigned characteristics and rumors to the agents and randomly mapped them to the nodes of the network. Each experiment consisted of 500 iterations, during which an agent
was selected in each iteration to make a post, as outlined in
the previous section. The LLM employed for the agents was
the latest version of ChatGPT-4o-mini.
We conducted a total of three experiments, each designed
to examine distinct facets of the problem under investigation: (1) the effect of network structure on the dynamics of
rumor propagation, (2) the impact of initial conditions and
spread schemes on the spread of rumors, and (3) the role of
agent characteristics in shaping the patterns of rumor spread.
For efficiency, the second and third experiments are evaluated on the Scale-Free network.
We tested, in total, the spread of 4 distinct rumors:
• Nicolae Ceausescu is not dead!
,
• A living dinosaur is found in Yellowstone National Park.
• Large Language Models are manned by real people acting as agents.
• Drinking 3 ales a day can heal cancer!

Table 1: Network Properties Comparison
Erdo˝s Scale Small Facebook
Re´nyi Free World #686
# Nodes 100 100 100 168
# Edges 396 390 200 1656
Avg Degree 7.92 7.80 4.00 19.71
Avg Path Len 2.42 2.37 3.88 2.43
Diameter 4 4 7 6
Avg CC 0.08 0.16 0.21 0.53
Figure 2: Maximum percentage of affected nodes across
all rumor-network combinations The small world network
demonstrates the greatest susceptibility to rumor spread.
Effect of Network Structure
Figure 2 depicts the maximum percentage of the network
influenced by each rumor. A notable observation is the differential spread of rumors across the network: rumors that
are less likely to be disproved tend to propagate more effectively, whereas intelligent agents predominantly reject those
easily identifiable as misinformation. This behavior can be
attributed to the agents’ ability to leverage knowledge from
the pretrained GPT model, allowing them to recognize and
dismiss misinformation (Liu et al. 2024). We argue that the
nature of a rumor plays a critical role in its propagation.
Rumors about history or engineering are often dismissed
by most agents, likely due to extensive coverage during
the model’s training. Conversely, rumors related to healthcare and nature exhibit a higher likelihood of spreading, potentially due to the agents’ limited domain-specific knowledge, which renders them more vulnerable to misinformation. However, the proprietary and non-transparent nature
of ChatGPT’s development and training processes prevents
concrete verification of this analysis. Future research focusing on the impact of specific knowledge domains or topics
on rumor propagation would provide valuable insights.
Moreover, the structure of the network plays a pivotal role
in influencing rumor propagation, with the connectivity and
clustering characteristics of nodes being particularly impactful. For instance, the Small-World network, characterized by
relatively sparse connectivity and moderate clustering, exhibits the highest susceptibility to rumor spread, with up to
50% of nodes being affected. In contrast, as network connectivity increases and clustering decreases—due to greater
randomization, as observed in Erdo˝s-Re´nyi and Scale-Free
networks—rumors propagate less effectively. In the case of
the real-world Facebook network, which is characterized
by high density and strong clustering, rumors are even less
likely to spread widely. This behavior can be attributed to

Figure 3: Propagation of Rumor #2. The Small-World network shows the greatest susceptibility to rumor spread.
Figure 4: All rumors are spread when they originate from
agents with more friends, and these agents are more active. Meanwhile, one particular rumor (rumor #2) is widely
spread using more random simulation strategies.
the increased connectivity in dense networks, which exposes
agents to a diverse array of information sources, thereby reducing the likelihood of rumor propagation. Additionally,
clustering plays a critical role; nodes within the same cluster often share similar beliefs, creating a form of collective
resistance to rumor.
Finally, we analyze the temporal dynamics of rumor propagation. Figure 3 illustrates the spread of Rumor #2 across
all networks over time. The results reveal an almost linear relationship between rumor spread and time. Notably,
an intriguing phenomenon emerges: as iterations progress,
some nodes that initially accepted the rumor later reject it.
This behavior can be attributed to interactions with other
agents, as each iteration exposes them to new posts and
perspectives. Furthermore, the agents’ decision-making processes—shaped by their ”intelligence,” derived from the pretrained GPT model—evolve with the influx of new information, prompting them to revise their stance. These findings
underscore the dynamic nature of rumor propagation and the
complex interplay of agent interactions within the network.
Effect of Initialization and Spreading Scheme
An additional critical factor influencing rumor propagation
is the choice of the Initialization Strategy, which determines the initial agents receiving the rumor, and the Activation Strategy, which specifies the selection of agents in
each iteration. In this experiment, conducted on a Scale-Free
network, the Initialization Strategy and Activation Strategy

were chosen either randomly or based on node degree, as
described in Section 3.
Figure 4 presents the matrix for the maximum percentage of nodes affected by each rumor under all combinations of Initialization Strategy and Activation Strategy. The
widespread dissemination of all rumors is observed when
both strategies target nodes with the highest degree. In this
scenario, these popular agents continually spread rumors.
The Activation Strategy significantly enhances the propagation of all rumors, thereby facilitating their spread throughout the network. This outcome can be attributed to the fact
that a highly connected Initialization Strategy accelerates the
rumor’s reach across a larger portion of the network. Meanwhile, if the posts are not initially presented to the popular
nodes, not all rumors can spread. Rumor #2, which is readily accepted by agents, is efficiently propagated to nearly
all agents, whereas other rumors are ignored. Furthermore,
when the popular nodes are no more active than others in all
random strategies, all rumors spread with limited impact.
Effect of Agent’s Personas
The final experiment aimed to examine the impact of agent
personas—specifically, the agents’ predisposition to accept
rumors—on rumor propagation. As in the previous experiment, this study was conducted exclusively on the ScaleFree network structure. We examined the maximum percentage of nodes affected under three distinct agent personality
configurations: (a) all agents are highly likely to accept a
rumor, (b) each agent’s likelihood of accepting a rumor is
assigned randomly, and (c) all agents are highly unlikely to
accept a rumor. As expected, the agents’ personality configurations significantly influence the spread of rumors. The
results (see Appendix) reveal a clear decline in rumor propagation as the agents’ likelihood of accepting rumors transitions from highly receptive to highly resistant. This underscores the critical role of agent characteristics in shaping the
dynamics of misinformation.
Conclusion
This study explores the use of LLMs as proxies for human
behavior in rumor dissemination across diverse network architectures. Our findings demonstrate their practicality and
scalability in network simulations. Moreover, we analyze the
impact of network attributes and prompt configurations on
rumor spread, contributing to the understanding of LLMs’
role in modeling social interactions and information flow.
For future work, we plan to analyze a wider range of rumors and develop advanced agent personas for more realistic
outcomes. We also aim to scale network sizes, explore mitigation strategies for rumor spread, and examine the role of
additional LLM-based agents in shaping outcomes.
Acknowledgment
We thank the anonymous reviewers for their helpful feedback. We thank the members of the UT-SysML research
group for their insightful discussions to improve this work.
This work was supported by the UT ECE junior faculty startup fund, UT iMAGiNE consortium and its industrial affili-

ates, an award from the UT Machine Learning Lab (MLL), Zheng, L.; Yin, L.; Xie, Z.; Huang, J.; Sun, C.; Yu, C.;
the AMD Chair Endowment, the Cisco Research Award, and Cao, S.; Kozyrakis, C.; Stoica, I.; Gonzalez, J. E.; et al.
the Amazon Research Award. 2023. Efficiently Programming Large Language Models using SGLang.
References
Alam, S. J.; and Geller, A. 2011. Networks in Agent-Based
Social Simulation. In Agent-Based Models of Geographical
Systems, 199–216. Springer.
Baraba´si, A.-L.; and Bonabeau, E. 2003. Scale-free networks. Scientific american, 288(5): 50–9.
Chen, X.; and Wang, N. 2020. Rumor spreading model considering rumor credibility, correlation and crowd classification based on personality. Scientific reports, 10(1): 5887.
Chen, Y.; Arkin, J.; Zhang, Y.; Roy, N.; and Fan, C.
2024. Scalable Multi-Robot Collaboration with Large
Language Models: Centralized or Decentralized Systems?
arXiv:2309.15943.
Chuang, Y.-S.; Goyal, A.; Harlalka, N.; Suresh, S.; Hawkins,
R.; Yang, S.; Shah, D.; Hu, J.; and Rogers, T. T. 2024. Simulating Opinion Dynamics with Networks of LLM-based
Agents. arXiv:2311.09618.
Erdo¨s, P.; and Re´nyi, A. 1959. On random graphs I. Publicationes Mathematicae (Debrecen), 6: 290–297. Dedicated
to O. Vargo on the occasion of his 50th birthday.
Hamidian, S.; and Diab, M. T. 2019. Rumor Detection and
Classification for Twitter Data. arXiv:1912.08926.
Kaligotla, C.; Yu¨cesan, E.; and Chick, S. E. 2015. An agent
based model of spread of competing rumors through online
interactions on social media. In 2015 winter simulation conference (WSC), 3985–3996. IEEE.
Leskovec, J.; and Mcauley, J. 2012. Learning to discover social circles in ego networks. Advances in neural information
processing systems, 25.
Li, J.; Zhang, Q.; Yu, Y.; Fu, Q.; and Ye, D. 2024. More
Agents Is All You Need. arXiv:2402.05120.
Liu, Q.; Tao, X.; Wu, J.; Wu, S.; and Wang, L. 2024. Can
Large Language Models Detect Rumors on Social Media?
arXiv:2402.03916.
OpenAI. 2024. ChatGPT. https://www.openai.com.
Park, J. S.; O’Brien, J.; Cai, C. J.; Morris, M. R.; Liang,
P.; and Bernstein, M. S. 2023. Generative Agents: Interactive Simulacra of Human Behavior. In Proceedings of the
36th Annual ACM Symposium on User Interface Software
and Technology. ISBN 9798400701320.
Radford, A.; Narasimhan, K.; Salimans, T.; and Sutskever,
I. 2018. Improving Language Understanding by Generative
Pre-Training. Available: OpenAI website.
Watts, D. J.; and Strogatz, S. H. 1998. Collective dynamics of ‘small-world’ networks. Nature, 393: 440–442. Published: 04 June 1998.
Wilensky, U. 1999. NetLogo. http://ccl.northwestern.edu/
netlogo.
Zehmakan, A. N.; Out, C.; and Khelejan, S. H. 2023. Why
Rumors Spread Fast in Social Networks, and How to Stop
It. arXiv:2305.08558.

Appendix id: 3
agent name: Leo
Synthetic Networks
agent age: 35
In Table 1, we present three synthetic networks with vari- agent job: Software Developer
ous properties. Below is the visualization of these networks, agent traits: Analytical, Persistent
where the name on each node denotes the agent associated agent rumors acc: 3
with that node. agent rumors spread: 3
id: 124
agent name: Olivia
agent age: 29
agent job: Data Scientist
agent traits: Curious, Logical
agent rumors acc: 4
agent rumors spread: 1
Prompt Template
In each iteration, for the selected agents, we use the ChatGPT API to submit prompts to the ChatGPT-4o-mini model.
Given an agent persona, a list of rumors, and post history, the
Figure 5: Visualization of Erdo˝s-Re´nyi random network. exact prompts we used are as follows:
role: system
content: You are a helpful
assistant.
role: user
content: Hi, {agent name}, you are
a {agent age}-year-old {agent job}
known for being {agent traits}.
Please follow the instructions
below. You are active on a social
network, receiving and sending
posts. You {likely to accept rumors
[agent rumors acc]}, and you
{likely to forward rumors
[agent rumors spread]}.
Read through the post history,
especially the new posts. It can
Figure 6: Visualization of Scale-Free network.
be something you’ve read in other
posts but you need to rephase it
your personality. You can criticize
the posts if you don’t agree with
them, you can also repeat them or
express in your own way. Your posts
can be seen by all your friends.
Here are your friends: {friend list}
You are about to send a new post
[POST] based on your personal
preferences.
After posting, you will review a
list of rumors and decide [CHECK]
whether to believe or reject each
one. Be honest: if your post
mentions a rumor, your response
Figure 7: Visualization of Small World network. must be consistent with what you
posted.
[Action Output Instruction] Start
with ’POST’, then on a new line,
Agent Personas
specify the content of your new
In all experiments, each agent’s personas are randomly gen- post. Then, on a new line, output
’CHECK’, followed by True or False
erated by ChatGPT-4, following this structure:
for each rumor.

Example#1:
POST
I just read that Donald Trump will
be president of Greece! OMG! That’s
interesting.
CHECK
False COVID-19 now named as
COVID-114514.
True Donald Trump will be president
of Greece.
Example#2:
POST
What a nice day! I enjoy my job as
a teacher.
CHECK
False COVID-19 now named as
COVID-114514.
False Donald Trump will be
president of Greece.
Before you reviewing the posts, you
used to believe:
You used to believe
{rumor list[str(i)]} is True
The previous post history is:
{post history}
Think step-by-step about the task.
Be careful not to let the rumor
list affect your judgment on post
history.
You CANNOT post the information
from the rumor list but NOT in your
post history.
The rumor list is: {rumor list}
Check whether you believe them
based on what you read and send.
Try not to exactly repeat what
others have said.
Propose exactly one action (POST
and CHECK) for yourself in the
current round.
Your response:
The dictionaries likely to accept rumors and
likely to forward rumors are defined below:
likely to accept rumors:
1: won’t easily accept any rumors or new information
unless they are confirmed or well-examined
2: may suspect rumors but will accept them once they
appear frequently in posts or generally make sense
3: will accept any new information unless there is significant controversy or criticism
4: will easily accept any rumors, even if there are
doubts or criticisms
likely to forward rumors:
1: prefer not to spread much of the new information

seen in others’ posts
2: may forward posts seen with comments and feelings, or may just share personal experiences
3: are willing to share and comment on rumors, posts,
and new things seen in posts
Supplementary Evaluation Results
The final experiment of the evaluation section investigated
the influence of agent predisposition on rumor propagation
within a Scale-Free network. Three distinct personality configurations—high, random, and low acceptance—were analyzed. Figure 8 shows the maximum percentage of nodes
affected under those three distinct agent personality configurations. Consistent with expectations, we observed a clear
decline in spread as receptivity decreased, highlighting the
impact of agent traits on misinformation dynamics.
Figure 8: As the personality of the agents shifts from being
more likely to accept rumors to being less likely to accept
them, we notice a decline in rumor spreading.
