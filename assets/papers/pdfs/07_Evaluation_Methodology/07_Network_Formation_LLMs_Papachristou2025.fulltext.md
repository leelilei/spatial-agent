Title: Network Formation and Dynamics Among Multi-LLMs

Source PDF: /Users/mac/Documents/6-Research/1-SpatialAgent/assets/papers/pdfs/07_Evaluation_Methodology/07_Network_Formation_LLMs_Papachristou2025.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T03:08:56+00:00
- page_count: 48
- status: ok
- text_char_count: 117884

Metadata:
- author: Marios Papachristou; Yuan Yuan
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Methods and Materials (page 25)
  - Experimental Procedure (page 25)
    - Network Formation Process (page 25)
    - Prompts (page 25)
    - Feature Representations for Prompts (page 27)
    - Robustness Checks and Prompt Sensitivity (page 28)
  - Details for Small-World Experiments (page 28)
  - Real-World Network Experiments (page 29)
    - The Discrete Choice Model in Real-World Network Experiments (page 29)
    - Estimating the Parameters of the Discrete Choice Model (page 29)
    - Candidate Set Construction for Network Decisions (page 30)
    - Measuring Alignment Between Models (page 30)
  - Human Baseline (page 31)
    - Survey (page 31)
    - Sample Size Construction on Prolific (page 31)
    - Measuring Alignment between models and Humans (page 31)
    - Robustness Checks and Prompt Sensitivity (page 32)
  - Data and Code Availability (page 34)
- Real-World Datasets (page 35)
  - Statistics of Real-World Datasets (page 35)
  - Robustness of Results to Sampling Strategies (page 36)
    - Recommendation System Parameters (page 36)
    - Change in Graph Statistics due to Different Sampling Strategies (page 37)
    - Average Marginal Effects (page 38)
  - Robustness of Results to Temperature (page 39)
    - Regression Coefficients (page 39)
    - Change in Graph Statistics due to Different Temperatures (page 40)
  - Robustness of Results to Large Context Windows (page 41)
- Network Evolution and Omitted Simulations (page 42)
  - Principle 1: Preferential Attachment (page 42)
  - Principle 2: Triadic Closure (page 42)
  - Principle 5: Small-World Phenomenon (page 44)
- Chain-of-Thought Experiments (page 45)

Markdown Content:

∗
Network Formation and Dynamics among Multi-LLMs
Marios Papachristou† Yuan Yuan‡
Abstract
Social networks profoundly influence how humans form opinions, exchange information, and orga-
nize collectively. As large language models (LLMs) are increasingly embedded into social and pro-
fessional environments, it is critical to understand whether their interactions approximate human-like
networkdynamics. WedevelopaframeworktostudythenetworkformationbehaviorsofmultipleLLM
agentsandbenchmarkthemagainsthumandecisions. Acrosssyntheticandreal-worldsettings,includ-
ing friendship, telecommunication, and employment networks, we find that LLMs consistently repro-
ducefundamentalmicro-levelprinciplessuchaspreferentialattachment,triadicclosure,andhomophily,
as well as macro-level properties including community structure and small-world effects. Importantly,
the relative emphasis of these principles adapts to context: for example, LLMs favor homophily in
friendship networks but heterophily in organizational settings, mirroring patterns of social mobility.
A controlled human-subject survey confirms strong alignment between LLMs and human participants
in link-formation decisions. These results establish that LLMs can serve as powerful tools for social
simulation and synthetic data generation, while also raising critical questions about bias, fairness, and
the design of AI systems that participate in human networks.
Keywords: social networks, network formation, large language models, computational social science
Code: https://doi.org/10.5281/zenodo.16969696
Data: https://doi.org/10.5281/zenodo.17196412
∗Accepted at PNAS Nexus. Corresponding author: Marios Papachristou (mpapachr@asu.edu).
†Department of Information Systems, W.P. Carey School of Business, Arizona State University, Tempe, AZ, USA and
Department of Computer Science, Cornell University, Ithaca, NY, USA.
Supported by a scholarship from the Onassis Foundation (Scholarship ID: F ZT 056-1/2023-2024), and in part by a Simons
Investigator Award, a Vannevar Bush Faculty Fellowship, AFOSR grant FA9550-19-1-0183, a Simons Collaboration grant,
and a grant from the MacArthur Foundation.
‡Graduate School of Management, University of California Davis, Davis, CA, USA.
1
5202
tcO
5
]IS.sc[
7v95601.2042:viXra

Introduction
Recent progress in large language models (LLMs), such as GPT [42], Claude [3], and Llama [54], have
shown promising developments in AI techniques and their integration into real-life applications. It is thus
crucial to comprehend AI actions to ensure they align with human expectations, mitigate potential risks,
and maximize their benefits. Misaligned AI actions may lead to unintended consequences, such as biased
decision-making, fairness issues, and the miscoordinative or non-cooperative behavior [50]. Recently,
researchers have started to apply social science methodologies, such as methods analogous to laboratory
experiments [20, 1, 57, 35], agent-based modeling [48, 22, 24, 17, 18, 49], and qualitative methods [13],
to study LLMs. These methods not only reveal the capabilities and interpretability of LLMs but also
suggest their potential for applications in social science [20, 47, 12, 30].
In human societies, social networks play a crucial role in shaping individual behaviors, preferences,
and connections, as well as influencing the diffusion of information and norms across communities [51, 5,
21, 6, 61]. LLMs have shown great potential in social contexts, notably as intelligent personal assistants
that facilitate social and prosocial interactions (see, e.g., [46, 14, 57]). However, less is known about
how LLMs’ behaviors and preferences align with human network formation principles [25, 62, 47]. This
is particularly crucial, as it sheds light on the potential of these models to shape and be shaped by the
networks of human relationships, which is a fundamental aspect of social systems.
Recently, there has been an emerging body of work regarding LLM-based agent-based models, where
theresearchcommunityhasdevisedframeworksforsocialsimulation[62,48,52,19], andhaveshownthat
collectives of LLMs exhibit linguistic collective biases [4, 19], and the friendship paradox [43], showing
that LLMs are promising at simulating real-world social networks.
Our study complements these works, and explores LLMs’ behaviors and preferences in the context of
network formation with both synthetic and real-world social networks, and answers the question “Which
complex phenomena emerge by interactions between multiple LLMs?” beyond merely focusing on the
modeling and simulation aspect. By analyzing such interactions, we aim to understand the implications
of LLMs representing humans in social and professional settings.
Specifically, we examine micro-level social network properties including preferential attachment [7],
triadic closure [23], and homophily [37], as well as macro-level properties including community structure
[41], and the small-world phenomenon [28, 59].
By analyzing LLM agents interacting dynamically in several different contexts and environments,
with a variety of models (both closed and open-weight), and variations of the prompts, we find that in
synthetic network simulations, LLMs displayed preferential attachment, homophily, and triadic closure,
resultingintheformationofcommunitystructuresandsmall-worlddynamics. Morenotably,inreal-world
social network simulations, we find that LLMs prioritize triadic closure and homophily over preferential
attachment when forming new links, indicating a strong preference for connecting with similar nodes or
sharedacquaintances. Additionally,inatelecommunicationnetwork,LLMstendedtoprioritizehomophily
and preferential attachment over triadic closure, and in a company network, the agents who corresponded
to employees formed links frequently with managers, which showcases behavior that is consistent with
human social mobility principles.
Generally, LLMs not only exhibit fundamental social network formation principles in synthetic sim-
ulations but also adapt their strategies based on the context of real-world networks, mirroring human
social behaviors specific to each setting.
As LLM technology continues to evolve, our study serves as an early exploration of their potential in
social network studies, with several significant implications for future studies. First, our study demon-
strates the potential of LLMs for agent-based modeling. By simulating decision-making processes that
approximate human-like behavior across various network settings, LLMs can provide valuable insights
into the emergence of social phenomena. Although these models are still in early stages of development,
they offer an intriguing framework for studying and designing systems that can mimic key aspects of
real-world dynamics. This opens up possibilities for applying LLMs to explore and understand complex
2

behaviors in social, professional, and collaborative environments. Second, our work highlights the poten-
tial of LLMs for synthetic dataset generation, a critical area in network science. Although the accuracy of
LLM-based predictions is not yet perfect, like all other link prediction models, this approach is particu-
larly valuable in scenarios where privacy concerns limit access to real-world data. By simulating realistic
datasets that capture important network properties, LLMs can facilitate research and experimentation
without compromising sensitive information.
Results
In this study, we investigated whether LLMs exhibit fundamental principles of network formation ob-
served in human social networks. By simulating multiple LLM agents acting independently within sepa-
rate conversational threads, we examined their behaviors in decision-making scenarios involving network
connections. Wefocusedonthreemicro-levelnetworkprinciples–preferentialattachment, triadicclosure,
and homophily – and two macro-level phenomena–community structure and the small-world effect. To
assess the robustness of our findings, we varied the temperature settings of different LLM models, includ-
ing GPT-3.5-turbo, GPT-4o Mini, Llama 3 (70b-instruct), and Claude 3.5 Sonnet. We also experimented
with different environmental prompts (e.g., friendship, collaboration, community) to test prompt sensi-
tivity. Additionally, we employed an interview-like method to probe the LLMs’ decision-making rationale
andconductedexperimentsusingChain-of-Thought(CoT)reasoning[60](theexperimentsaredeferredto
Section D). Finally, we extended our analysis to real-world networks, including a social media friendship
network, a telecommunication network, and a company collaboration network, to compare the network
formation preferences between LLMs and humans.
More information about the experimental procedure, methods, and materials can be found in the
Section A.
Micro-Level Properties
Principle 1: Preferential Attachment
Preferential attachment is a fundamental concept in network science, illustrating how nodes in a network
gain connections over time, leading to a scale-free degree distribution characterized by a few highly
connected nodes [7, 8].
To test if LLM agents exhibit preferential attachment, we simulated network growth by sequentially
addingnodestoaninitiallyemptynetwork. Eachnewnodewaspromptedwithinformationaboutexisting
nodes,andthepersontoconnectwithwasdecided. Wegeneratednetworkswithn = 200nodestoobserve
meaningful degree distributions1.
On a micro-scale, Figure 1 illustrates the probability of connecting to a top-k node as a function of
its degree percentile (k/n). To demonstrate the tendency toward preferential attachment, we compare
these probabilities to a null model assuming random connections (represented by dashed lines), where
the likelihood of connecting to a top-k node is simply k/n. Our findings reveal that all models prefer
connecting to higher-degree nodes. Notably, GPT-3.5 exhibits a weaker preference, while other, arguably
more capable models, show an even stronger inclination toward preferential attachment. Using GPT-3.5
as an example, we examine the effect of temperature – a parameter controlling the variability of model
output – on this tendency. At lower temperatures, the model makes fewer stochastic choices and, as a
result, is more likely to connect to high-degree nodes. We also vary the prompt to explore the influence of
“environment”-contextual settings such as school, work, or community. The results show slight variations
comparedtothebaseline(GPT-3.5withtemperature=1.5), yetthetendencyforpreferentialattachment
1Notethatweprovidethefullnetworkstructureintheprompt,somodelsarenotinherentlybiasedtowardforminglinks
with the highest-degree nodes.
3

(a)
(b)
(b)
(c)
(d)
Figure1: ResultsforPrinciple1(preferentialattachment)Themulti-LLMsetupwasgivenneighborhoodinformation
{N :j ∈V }. (a, b): Probability of connecting to top-k-degree nodes for varying model (temperature is fixed to 1.0 and
j,t t
environmenttobaseline),temperature(modelfixedtoGPT-3.5andenvironmenttobaseline)andenvironment(modelfixed
to GPT-3.5 and environment temperature to 1.5) for networks generated according to Principle 1 with n = 200 nodes.
(a) shows the whole range of k, and (b) shows the top 1−2.5% nodes. (c): Power Law exponents and standard errors
for varying model, temperature, and environment. (d): Simulated networks. Power-law degree distributions are evident
(P >0.5, K-S test), with the networks at a temperature of 1.5 closely resembling the Baraba´si-Albert model (P >0.1, K-S
test) for GPT-3.5 agents.
persists across environments. In all cases, the observed curves lie above the null model, underscoring the
presence of preferential attachment.
4

Next,weinvestigatethedegreedistributionoftheresultinggraphs. AsshowninFigure1,theresulting
networks display a pattern where a few nodes have many connections while most have few, indicative of
a scale-free distribution, with form:
π(d) ∝ d−γ, where γ > 1. (1)
We estimated the exponent γ for different models and temperatures. Our analysis reveals several notable
patterns in the networks generated by LLM agents under different conditions. First, models newer than
GPT-3.5 exhibit a slightly larger γˆ than GPT-3.5. This implies that these models display a stronger ten-
dency toward preferential attachment and the formation of hubs. Second, as the temperature increases
the power-law exponent γˆ generally becomes larger. This indicates that higher temperatures introduce
more variance in node connectivity, leading to degree distributions with heavier tails. Third, the envi-
ronmental context significantly affects the value of γˆ. For example, when the network is framed within a
“school” environment, the exponent increases, suggesting a more uniform distribution of connections and
fewer highly central nodes.
Finally, while the prompts we have utilized thus far have provided the model with the complete
existing network structure, we also explore an alternative scenario: what happens if agents are supplied
solely with the degree of other alternatives, without access to the network’s full structure? As detailed
in Section C, our findings reveal that limiting agents to degree information alone also leads to notable
structural differences in the networks that emerge (cf Figure SI.3). Thus, degree information alone
yields more restrictive structures than providing the agents with the full topological information (i.e., the
neighbors).
The findings highlight the practical potential of LLMs in modeling complex networks, such as social,
economic, or biological systems, by leveraging their ability to simulate preferential attachment and scale-
free distributions. These models can be used to study real-world phenomena like information diffusion,
hub formation, or connectivity patterns under varying conditions. Additionally, the sensitivity of network
structures to parameters like temperature and context underscores the importance of prompt design in
steering outcomes, making LLMs versatile tools for tailored simulations.
Principle 2: Triadic Closure
The second micro-level principle we examine is triadic closure, which posits that individuals are more
likely to form connections with friends of friends, thus creating closed triads in the network. This process
strengthens network structure and cohesion, grounded in the idea that two nodes are more likely to
connect if they share a common neighbor [23, 38].
To investigate triadic closure, we employ an assortative stochastic block model (SBM) [39] to create
an initial network G with n nodes divided into two equal-sized clusters A and B. Connections within
1
each cluster are formed with a probability of 0.5, while inter-cluster connections occur with a probability
of0.1. Thissetupmirrorsourassumptionthatnodeswithinthesameclusteraremore inclinedtoconnect
due to a higher number of shared neighbors. In subsequent time steps, we then examine each node i,
considering the intersection of neighborhoods of i’s non-neighbors2.
We conducted ten simulations with n = 50 nodes to facilitate clear visualization and ensure statistical
significance3.
On a micro-scale, Figure 2 illustrates the probability of connecting to a top-k-percentile node as a
functionofthenumberofcommonneighbors. Thedashedlinesrepresenttheresultsofnullmodels, where
connections arechosenrandomly; whichcorresponds tothe probability ofconnecting to a top-k percentile
node in terms of the common neighbors being k/n. Our findings reveal that, across all models, there is
a consistently higher probability of forming links with nodes that share more common neighbors. Unlike
the behavior observed in preferential attachment, temperature does not appear to severely impact this
2Similar outcomes arise when providing neighbors instead of common neighbors.
3Choosing n=50 instead of a larger number like n=200 aids in visualization and maintains statistical significance.
5

Stochastic block model initialization (a-d)
(a)
(b)
(c)
(d)
Erdős–Rényi model initialization (e-f)
(e) (f)
Figure 2: Results for Principle 2 (triadic closure). (a, b): Probability of connecting to top-k nodes (in terms of
common neighbors) for varying model (temperature is fixed to 1.0 and environment to baseline), temperature (model fixed
toGPT-4Miniandenvironmenttobaseline)andenvironment(modelfixedtoGPT-4Miniandenvironmenttemperatureto
0.5)fornetworksgeneratedaccordingtoPrinciple2(n=50,10simulationsforeachmodel,environmentandtemperature).
The dotted diagonal line corresponds to the null model, where connections are made at random. Panel (a) shows top-k
for k for k in the range 10−50%, and Panel (b) shows top-k for k in the range of 10−100%. (c): Marginal transitivity
(D) and probability of an edge within a community (pˆ) for networks generated according to Principle 2 in different models,
temperatures,andenvironments. Thedottedlinecorrespondstotherandomnullmodel. (d): Thefigureshowstheresulting
networkscreatedbyGPT-4Mini,accordingtoPrinciple2whentheintersectionoftheneighborhoodsofthequerynodeand
eachalternativeisprovidedandcomparisonofthemetricsDandpˆwiththerandomnullmodel. Thenodecolorscorrespond
tothegroupstowhicheachnodebelongs. Theboldedges(redorblue)correspondtothenewlycreatedinter-clusteredges,
and the orange edges correspond to the new intra-cluster edges. (e, f): Marginal transitivity (D) and network instances
when the initial network is an Erdo¨s-R´enyi graph with n=50 and p=0.1.
probability. Thistendencytoformlinkswithnodesthathavemorecommonneighborsisconsistentacross
various contexts, including school, work, and community environments. These results suggest that the
triadicclosuretendencyisarobustphenomenon,persistingacrossdifferentmodelfamilies,configurations,
6

and environments.
Then, for evaluating triadic closure on the network (macroscopic) level, we utilize two metrics:
marginal transitivity and probability of edge formation within the same community. Marginal transi-
tivity (D) represents the change in the ratio of closed triangles to all triads, transitioning from the
SBM-generated network G to the final network G after T = 50 iterations:
1 T
# triangles(G ) # triangles(G )
T 1
D = 3× −3× .
# triads(G ) # triads(G )
T 1
where a large positive D indicates a strong triadic closure tendency.
As we investigate under SBM, the same community membership indicates more open triads being
closed.
Marginaltransitivity(D),presentedinFigure2,demonstratesastatisticallysignificantincreaseacross
all models, temperatures, and environments, underscoring the robust nature of triadic closure.
In Figure 2, sample networks from GPT-3.5 are displayed, with the upper panel showing networks
where the entire structure is provided and the lower panel showing those with only common neighbor
numbers provided. Nodes are color-coded to indicate their cluster memberships in the SBM, with red and
blue edges within clusters and orange edges between clusters. Newly formed edges are highlighted with
thicker lines.
Finally, toeliminatethepossibilitythattheresultsareduetostructuralbiasfromtheinitialstructure
(SBM), we note that we can obtain the same results when we start from a more “neutral” initial topology.
Specifically, we get the same results and an even stronger effect for the marginal transitivity (D) by
starting from a sparse Erd¨os-R´enyi graph with n = 50 nodes and p = 0.1. We find that, across or models,
temperatures and variations of the prompts, the resulting network exhibits higher marginal transitivity
(D) compared to the random null model, which makes connections at random starting from the same
Erd¨os-R´enyi graph, and the results are statistically significant (cf. Figure 2; P < 0.001; t-test comparing
the marginal transitivity of the resulting LLM-generated networks and the random null model).
In summary, these findings show that most LLMs exhibit a consistent tendency for triadic closure
across various configurations, temperatures, and environments. This behavior mirrors human network
dynamics, highlighting the models’ ability to simulate realistic social and structural networks and rein-
forcing their alignment with social principles observed in real-world communities.
Principle 3: Homophily
Homophily reflects the tendency for nodes with similar characteristics or attributes to form connections
and associate with each other. This phenomenon is based on the principle that individuals in a network
are more likely to connect with others who share similar traits, interests, or demographics [37].
To test whether LLM agents exhibit homophily, we perform the following experiment: We generate
nodes with randomly generated attributes regarding a hobby (randomly chosen among three hobbies),
a favorite color (randomly chosen among three colors), and a location within the US (randomly chosen
among three US locations) and provide the attributes of the other nodes and the node’s own attributes,
and each node is tasked to form up to δ = 5 links with others. For each node i, we provide it with the
features x of all non-neighbors j of i. The seed network is taken to be the empty graph. We run ten
j
simulations for networks with n = 50 nodes and δ = 5.
To evaluate homophily, we calculate the attribute assortativity coefficient for each of the features. For
each property P which takes K distinct values P ,...,P (indexed by k or l), its assortativity coefficient
1 K
R is defined as
(cid:80)K
M −
(cid:80)K
a b
R = k=1 kk k=1 k k .
1−
(cid:80)K
a b
k=1 k k
7

(a)
(b)
(c)
Figure3: ResultsforPrinciple3(Homophily)andPrinciple4(Communitystructureduetohomophily). (a):
Assortativity and Louvain modularity by Principle 3 (n=50, 5 runs per row) across school, work, and community settings.
Allcomparisonstotherandomnullmodel(R=0)arestatisticallysignificant(P <0.0003,t-testswithBonferronicorrection
for three tests). Modularity is also significantly greater than 0 (P < 0.001). (b): Network examples and communities for
GPT-3.5 agents. Compared to a null model where agents connect randomly (R = 0). (c): Influence of distractor features
(favorite color, lucky number) on homophily. Compared to a random null model with R = 0. All results are statistically
significant (P <0.00025), with Bonferroni correction over 3 tests (location, favorite color, hobby).
Here, M representsthemixingmatrix. ItselementsM reflecttheproportionofedgesconnectingtwo
kl
nodes with values P and P , respectively. We define a =
(cid:80)K
M and b =
(cid:80)K
M . Assortativity
k l k l=1 kl k l=1 lk
ranges from −1 to +1. A positive assortativity indicates nodes preferentially connect to similar ones,
forming a homophilous network. Conversely, a negative assortativity suggests connections primarily
occur between dissimilar nodes, indicating heterophily.
From Figure 3, we observe that different attributes exhibit varying levels of assortativity. First,
homophily is present across all LLMs, regardless of the specific model or configuration (e.g., temperature
settings), all show positive assortativity for all four attributes, where they obtain statistically significant
results P < 0.0003 (t-test with 0, Bonferroni correction across three tests across the three features). This
aligns with human societies, where homophily is a primary driver of network formation [37]4.
4Asanadditionalrobustnesscheck,wealsotestedmutualagreementconnections. Inthatsetting,afteranodej ischosen
bynodei,j hastoconfirmthecreationofthelinkfromitselftoi(j →i). Weranseveralexperimentswithdifferentmodels
and temperatures and we found the results not to be affected, namely, the proposed connections were always bilateral.
8

Moreover,totesttheeffectofthefeaturesonhomophilyasindicatedbytheassortativitycoefficientfor
each attribute, we introduce a distractor feature, which corresponds to a lucky number that is randomly
chosen between 0 and 9. We repeat the simulations for all models and measure the effect of each feature
on Figure 3. We still observe strong homophily effects with high statistical significance after applying
Bonferroni correction for four tests (P < 0.00025, t-test with the random null model where connections
are done at random which has assortativity R = 0).
However,weshowthatluckynumbersconsistentlyshowlowerassortativitycoefficients,indicatingthey
are less considered when forming homophilous connections. This is consistent with our prior expectation
that humans typically do not prioritize shared lucky numbers when establishing relationships.
Surprisingly, even though the lucky number does not seem to impact homophily much, the favorite
color exhibits a similar level of homophily as hobbies. One might expect that hobbies, being substantive
interests, would have a stronger influence on social connections than favorite colors, which are more
arbitrary preferences. However, this finding aligns with the social identity theory and the minimal group
paradigm [53]. According to this paradigm, even minimal and arbitrary group distinctions – such as
a preference for certain colors – can lead to in-group favoritism and influence social connections. This
suggests that LLM agents, akin to humans, may form connections based on even trivial shared attributes,
reflecting inherent tendencies toward group formation based on minimal commonalities.
Allinall, LLMscancaptureandreproducesubtlehumansocialbehaviors, notjustlinguisticpatterns.
This underscores their potential as powerful tools for social simulation. However, these findings may also
raiseimportantconsiderationsregardingbias,fairness,andtheethicaldesignofAIsystems(cf. Discussion
Section).
Macro-Level Principles
Principle 4: Community Structure
The community structure of networks refers to the organization of nodes or individuals within a network
intodistinctanddenselyinterconnectedgroupsorclusters[41,40,9,16]. Identifyingcommunitystructures
is crucial for understanding the overall dynamics of a network, as it reveals patterns of relationships and
interactions that might not be apparent at the global level.5
Both triadic closure and homophily contribute to the formation of community structures. By exam-
ining how these two factors contribute to network formation, we aim to gain insights into the underlying
mechanisms driving community dynamics in LLM-generated networks. We employ the simulation results
presented in the synthetic networks to determine whether community structure in networks generated by
LLMs emerges from triadic closure or homophily.
First,weconsiderthenetworksgeneratedinFigure2. WeexaminehowLLMagents’choicesstrengthen
thenetwork’scommunitystructure. Specifically,weleveragethefactthattheSBMgraphhasapreexisting
communitystructureandmeasurehowthenewlyformedlinksreinforcesuchastructure. Visualinspection
shows that the newly added links, represented by the bold edges, happen mostly within each cluster,
reinforcing the community structure.
To measure the emergence of communities in the triadic closure case, we initially examine the prob-
ability of forming an edge within the same community (pˆ). The quantity pˆ is calculated by the ratio of
edges in G \G (newly formed edges) connecting nodes within the same cluster:
T 1
|{{i,j} ∈ E(G )\E(G ) : y = y }|
T 1 i j
pˆ= ,
|E(G )\E(G )|
T 1
where y ,y ∈ A,B denote the community memberships of nodes i and j, respectively. A value of pˆ
i j
exceeding 0.5 suggests a triadic closure tendency and community structure.
5Asanexample,wepresentonlytheresultsfromGPT-3.5forPrinciple4(CommunityStructure)andPrinciple5(Small-
World).
9

Figure 2 shows that pˆ is significantly higher than 0.5 (P < 0.001, t-test compared to 0.5), and is
significantly bigger compared to a random null model where connections are made at random. All in all,
this indicates that most edges are within the same community, strengthening the community structure.
Next, we investigate the community structure resulting from homophily using modularity maximiza-
tion [9]. Modularity quantifies the discrepancy between the actual number of edges within communities
and the expected number in a random network with identical node count and degree distribution, fol-
lowing the Chung-Lu model [15]. This model presumes that nodes maintain their weighted degree, with
edges randomly distributed. The weighted modularity Q [16] for a graph with edge weights w and C
ij
communities is defined as
(cid:88)
C (cid:34)
L c
(cid:18)
k c
(cid:19)2 (cid:35)
Q = −r .
W 2W
c=1
Here W represents the total edge weights, L the intra-community link weights for community c, k
c c
the total weighted degree within community c, and r the resolution parameter, set to 1 for our analysis.
High modularity values (e.g., greater than 0.5) indicate significant community structuring, diverging from
the random model.6
Firstly, we note that when the experimental setting for Principle 2 (cf. Figure 2) is initialized with
an SBM or an Erd¨os-Renyi network, we obtain positive modularity Q > 0 (P < 0.001; t-test comparing
with 0).
Secondly, regarding the homophily experiment (cf. Figure 3), for the network’s weights, we use the
(cid:12)(cid:110) (cid:111)(cid:12)
number of common attributes shared between each pair of nodes: w = (cid:12) k : x (k) = x (k) (cid:12) for each link
ij (cid:12) i j (cid:12)
(k) (k)
(i,j) in the final network. Here, x and x correspond to the k-th features of x and x , respectively.
i j i j
In Figure 3, various colors represent the communities identified by the Louvain algorithm at different
temperatures for GPT-3.5. Notably, communities appear more distinct at lower temperatures, likely due
to reduced randomness in decision-making at these temperatures.
Figure 3 presents the distribution of Louvain modularity values across simulations accross different
LLM models and different environments, indicating consistent community structure with positive mod-
ularity at all temperatures, confirmed by a t-test against a modularity of Q = 0 for a random graph
(P < 0.001).
Our results demonstrate that community structures manifest in networks generated by LLMs, driven
by both triadic closure and homophily.
Principle 5: Small-World
The small-world phenomenon is characterized by networks where nodes are interconnected in tight clus-
ters, yet the average distance between any two nodes remains relatively short, typically scaling loga-
rithmically with the network size [59, 28]. This balance between high clustering and short path lengths
characterizes small-world networks.
A small-world network is defined by its average shortest path length L, which grows logarithmically
with the size of the network n,7 expressed as
L ∼ log(n).
Our analysis utilizes the Watts-Strogatz model [59] as a benchmark to investigate whether LLMs
can generate networks exhibiting small-world characteristics. This model has a delicate balance between
6Given the NP-Hard nature of maximizing Q, we employ the Louvain algorithm [9] to approximate the highest possible
modularity.
7As per the definition in [26].
10

(a1) 𝛽=0.25 (a2) (a3)
(b1) 𝛽=0.50 (b2) (b3)
(c1) 𝛽=0.75 (c2) (c3)
(d)
Figure 4: Fitted results for Principle 5 (small world) for β = 0.25,k = 5 (a1-a3), β = 0.5,k = 5 (b1-b3), and
β = 0.75,k = 5 (c1-c3). (a1-c1): Average clustering coefficient C the average shortest path length L. The comparison is
made with respect to a Watts-Strogatz graph with n = 50,k = 5,β ∈ {0.25,0.5,0.75}. The error bars correspond to 95%
confidence intervals. The results are compared against the Watts-Strogatz model with the same parameters k and β as a
null model. The t-test comparing L and C for the LLM-generated networks and Watts-Strogatz networks yields P > 0.05
(Bonferroni correction for two tests). (a2-c2): Regression plots relating average shortest path length (L) and average
clustering coefficient (C) with n. The value a in legends represents the effect size (slope of the regression lines). (a3-c3):
Estimatedvaluesβˆofβ ∈{0.25,0.5,0.75}forLLM-generatednetworksbasedonmatchingtheaverageclusteringcoefficient
and difference in the average shortest path between LLM-generated networks and Watts-Strogatz with the estimated
rewiring probability βˆ for GPT-3.5 agents. We report the P-values of the t-test comparing the average shortest path
length of the LLM-generated networks and the average shortest path length of the Watts-Strogatz graphs with rewiring
probability βˆ. (d): Regression plot for the relation L ∼ log(n) for different LLM models and environments (school, work,
community)forβ =0.25andk=5. Thelegendshowstheeffectsize(a)andtheP-value. Theresultsarecomparedagainst
the Watts-Strogatz model with the same parameters k and β as a null model. (*: P < 0.025; **: P < 0.005, and ***:
P <0.0005, Bonferroni correction for two tests; L and C.).
local clustering and short average path lengths: Nodes tend to form clusters or groups (triadic closure),
exhibiting a high level of interconnectedness within these local neighborhoods, whereas at the same time,
the existence of a few long-range connections ensures that the entire network is reachable with relatively
few steps [48, 34, 27].
We employ a modified version of the model, where edge rewiring is informed by LLM queries, based
on the current network structure. The generation process is parametrized by the number of nodes (n),
average degree (k), and the rewiring probability (β). See details in Section A.2
We generated networks of various sizes, ranging from n = 10 to n = 100, to explore the relationship
between the network size (n) and two key metrics: the average shortest path length (L) and the average
clustering coefficient (C). For this analysis, we considered values of β set at 0.25, 0.5, and 0.75, with a
11

fixed k = 5 to serve as a consistent parameter.
However,whendirectlycomparedwiththeWatts-Strogatzmodel,thenetworksgeneratedbytheLLMs
do not precisely replicate the characteristics of Watts-Strogatz networks for the corresponding rewiring
probabilities (β). As illustrated in panels (a1-c1) of Figure 4, we fail to reject the null hypothesis at level
0.05 that the LLM-generated networks have the same average shortest path length as the Watts-Strogatz
model for the rewiring probabilities (β) of 0.25, 0.5, and 0.75 (t-test comparing the average shortest path
lengths, Bonferroni correction for two tests). Additionally, LLM-generated networks also fail to reject the
nullhypothesisatlevel0.05thattheLLM-generatednetworkshavethesameaverageclusteringcoefficient
as the Watts-Strogatz model for the same rewiring probabilities β (Bonferroni correction for two tests).
These results may suggest similarities in the network structure and connectivity patterns between the
LLM-generated networks and the classical Watts-Strogatz model.
We also provide regression analysis by examining the correlation between the average shortest path
length and average clustering coefficient versus log(n) (refer to Figure 4). We found that across all tested
temperatures, the relationships were statistically significant, with most regressions yielding statistically
significant results after applying Bonferroni correction for two tests (P < 0.0005). This indicates that the
average shortest path length increases proportionally with log(n). Similarly, for the average clustering
coefficient,wedemonstratedthatitinverselyscaleswith1/log(n),withthemajorityofregressionanalyses
also showing high statistical significance after Bonferroni correction for the two tests (P < 0.0005). These
findings align with the small-world properties of organizational networks as documented in the study
by [26], suggesting that these characteristics are not only prevalent but also predictable across different
network sizes.
To quantify how LLM-generated networks resemble Watts-Strogatz networks, we fit the estimated βˆ
valuesforeachLLM-generatednetwork.8 InFigure4,weplottheestimatedvaluesforβˆforeachvalueofβ
andeachtemperature. Here,P-valuesresultfromat-testcomparingwiththeaverageshortestpathlength
of Watts-Strogatz with rewiring probability βˆ. These results show that while the average shortest path
lengths are not identical, they are sufficiently close, with the differences not being statistically significant
at the 0.1 level for most temperature settings. Finally, as Figure 4 shows, the relation L ∼ log(n) holds
for different LLM models and environments.
In conclusion, our analysis demonstrates that LLM-generated networks exhibit key small-world prop-
erties, with logarithmic scaling of average shortest path lengths and inverse logarithmic scaling of average
clustering coefficients. While these networks do not perfectly align with the Watts-Strogatz model, they
exhibit similar structural characteristics.
Decisions on Real-World Networks with Heterogeneous Agents
We investigate the behavior of LLMs in real-world network formation contexts with four datasets in
two differing real-world domains. Despite the significant advancements in social network analysis over
recent years, the availability of fully complete and comprehensive network datasets remains exceptionally
rare [61]. We employ three datasets from the Facebook100 collection [56] and the telecommunication
(Andorra) and the employment (MobileD) datasets from [61]. The Facebook100 data correspond to
“friendship”networksfromonehundredAmericancollegesanduniversities,capturedataspecificmoment
from Facebook’s online social network. The Andorra dataset contains nationwide call records in Andorra
fromJuly2015toJune2016,wherecallscorrespondtomutualcallsbetweenAndorranresidentscontaining
information about the caller’s and the callee’s location, phone type, and usage. Finally, the MobileD
dataset corresponds to a company network where relations correspond to call or text communication, and
each employee is either a manager or a subordinate.
For all network datasets, the agents have heterogeneous profiles (i.e., profiles with different features)
8We conducted a binary search to identify the βˆvalues for which the Watts-Strogatz networks’ average clustering coeffi-
cients match those of the LLM-generated networks.
12

whose statistics (degree distribution, clustering coefficient distribution, assortativity) we report in Fig-
ure SI.1.
To infer the models’ tendencies, we employ a discrete choice modeling framework [44, 36]. Specifically,
we model the network formation process as a discrete choice process, wherein nodes are sequentially
prompted to form connections from a set of available alternatives (see Section A.3.1).
Candidate Set Construction for Network Decisions
At each decision step t, a query node i selects a link from a set of candidate nodes A with size |A | = A.
t t t
Given the limited context window of LLMs, we consider two alternative strategies for constructing the
candidate set A :
t
Uniform Sampling. WeuniformlysampleAnon-neighbornodesfromthegraph. Thisapproachserves
asaneutralbaseline, ensuringthatthealternativespresentedtothemodelareselectedwithoutstructural
or feature-based bias. Uniform sampling reflects a scenario where the agent has no a priori ranking or
filtering of candidates and evaluates all choices purely based on the features provided in the prompt.
Recommendation-Based Sampling. We also consider a more realistic and structured candidate se-
lection method that mimics the behavior of recommender systems. In this approach, we use a supervised
link prediction model based on logistic regression to compute the likelihood of a link between each candi-
date pair (u,v) (cf. [32]). The model takes as input common structural features known to be predictive
of link formation, such as similarity, the number of common neighbors between u and v, the preferential
attachment score between u and v, the Jaccard similarity between the neighborhoods of u and v, and the
Adamic-Adar index (see Section A.3.3 for a description of the recommendation system and Section B.2.1
for the effect sizes and AUC of the recommendation system). We then select the top-A highest-scoring
nodes as the candidate set A for each query node i . This method mirrors how real-world systems
t t
(e.g., social media friend suggestions, hiring portals, content feeds) narrow down decision spaces through
algorithmic filtering based on network and user features.
Hyperparameters. For the three datasets from Facebook100 are Caltech36 (n = 769) Swarthmore42
(n = 1,659), and UChicago30 (n = 6,591), we set the number of alternatives to be A = 15 and randomly
sampled from the existing network. For the UChicago30 dataset, we consider a randomly sampled subset
ofN = 2,000nodesbecauseofthelimitedcontextwindowoftheLLMmodels. ForAndorra(n = 32,812)
and MobileD (n = 1,982), we set the number of alternatives to A = 5 and consider a randomly sampled
subset of N = 1,000 nodes.
Regression Coefficients and Model Alignment
Uniform Sampling. Weregressnetworkformationdecisionsonstandardizedscoresreflectingthethree
micro-level principles. We present the regression results in Table 1.9 First, we observe a dominant effect
of homophily across all datasets and models. The coefficients for homophily (θˆ ) are consistently the
H
largest and highly significant (P < 0.05) in almost all cases. For instance, in the Caltech36 dataset,
the homophily coefficients for GPT-3.5, GPT-4, and Llama 3 70b Instruct are 0.65, 1.95, and 2.43,
respectively (P < 0.001). The emphasis on homophily suggests that LLMs, much like humans, prioritize
forming connections based on shared characteristics.
Second, wefindthatpreferentialattachmentplaysasecondaryroleinthenetworkformationdecisions
of LLMs. While the coefficients for preferential attachment (θˆ ) are generally positive and statistically
PA
significant across most models and datasets, they are notably smaller than those for homophily. For
example, in the Swarthmore42 dataset, GPT-3.5 and Llama 3 70b Instruct have preferential attachment
9More detailed results can be found in Section B.3.1.
13

Model PreferentialAttachment(θˆ PA) Homophily(θˆ H) TriadicClosure(θˆ TC) LogLikelihood AIC
Caltech36(n=769nodes,m=33,312edges,N=769samples,A=15alternativeseach)
GPT-3.5+Uniform 0.20***(0.002) 0.65***(0.005) -0.06(0.006) -2,088.21 4,184.41
GPT-4oMini+Uniform 0.34***(0.006) 2.13***(0.03) 0.44***(0.02) -1,201.27 2,410.55
Claude3.5+Uniform 0.46***(0.005) 0.55***(0.01) 0.55***(0.007) -1,748.19 3,504.38
Llama370b+Uniform 0.28***(0.006) 2.43***(0.02) 0.84***(0.01) -809.57 1,627.15
GPT-3.5+RecSys 0.15**(0.002) 0.08(0.007) -0.60***(0.02) -2,114.41 4,236.82
GPT-4oMini+RecSys 0.21***(0.004) 2.32***(0.005) 0.33**(0.005) -1,611.38 3,230.77
Claude3.5+RecSys 0.65***(0.002) 1.86***(0.01) 0.20(0.01) -1,852.96 3,713.91
Llama370b+RecSys 0.23***(0.003) 4.13***(0.01) 0.68***(0.01) -919.15 1,846.30
Swarthmore42(n=1,659nodes,m=122,100edges,N=1,659samples,A=15alternativeseach)
GPT-3.5+Uniform 0.19***(0.008) 0.47***(0.01) 0.00(0.009) -4,484.45 8,976.90
GPT-4oMini+Uniform 0.27***(0.21) 2.22***(0.78) 0.57***(0.43) -1,899.09 3,806.19
Claude3.5+Uniform 0.36***(0.002) 0.75***(0.006) 0.55***(0.004) -3,563.02 7,134.03
Llama370b+Uniform 0.39***(0.003) 2.31***(0.005) 0.62***(0.004) -1,820.26 3,648.52
GPT-3.5+RecSys 0.14**(0.001) 0.11(0.002) -0.08(0.002) -4,564.89 9,137.78
GPT-4oMini+RecSys 0.33***(0.007) 2.94***(0.01) 0.45***(0.006) -2,723.78 5,455.57
Claude3.5+RecSys 1.26***(0.004) 1.22***(0.007) 0.95***(0.006) -2,281.61 4,571.22
LLama370b+RecSys 0.09(0.007) 2.58***(0.02) 1.18***(0.009) -610.00 1,228.00
UChicago30(n=6,951nodes,m=416,206edges,N=2,000samples,A=15alternativeseach)
GPT-3.5+Uniform 0.22***(0.001) 0.48***(0.004) -0.02(0.0005) -8,157.38 16,322.77
GPT-4oMini+Uniform 0.27***(0.005) 2.22***(0.019) 0.57***(0.011) -1,899.09 3,806.19
Claude3.5+Uniform 0.43***(0.003) 0.78***(0.005) 0.39***(0.002) -6,604.77 13,217.54
Llama370b+Uniform 0.43***(0.007) 2.57***(0.014) 0.32***(0.005) -3,689.00 7,386.00
GPT-3.5+RecSys 0.14***(0.002) -0.08(0.006) 0.18**(0.007) -4,459.64 8,927.28
GPT-4oMini+RecSys 0.32***(0.001) 3.44***(0.01) -0.74***(0.005) -3,154.27 6,316.53
Claude3.5+RecSys 0.75***(0.002) 1.68***(0.005) 0.17*(0.003) -2,386.04 4,780.09
LLama370b+RecSys 0.27***(0.004) 2.81***(0.02) 0.53**(0.01) -661.75 1,331.50
Andorra(n=32,812nodes,m=513,931edges,N=1,000samples,A=5alternativeseach)
GPT-3.5+Uniform 0.53***(0.001) 0.21*(0.01) -0.24***(0.002) -1,712.91 3,433.83
GPT-4oMini+Uniform 0.54***(0.004) 3.47***(0.06) -0.09*(0.01) -1,002.11 2,012.22
Claude3.5+Uniform 0.54***(0.003) 1.94***(0.009) -0.15***(0.003) -1,541.77 3,091.55
Llama370b+Uniform 0.38***(0.003) 3.92***(0.02) -0.04(0.01) -985.95 1,979.91
GPT-3.5+RecSys 0.31***(0.03) -0.07(0.009) -0.43***(0.007) -1,722.42 3,452.84
GPT-4oMini+RecSys 0.11(0.003) 3.68***(0.008) -0.64***(0.006) -938.74 1,885.47
Claude3.5+RecSys 0.38***(0.003) 1.78***(0.01) -0.41***(0.005) -1,651.67 3,311.33
Llama370b+RecSys 0.53***(0.002) 3.63***(0.01) -0.12*(0.003) -1,238.22 2,484.45
MobileD(n=1,982nodes,m=25,470edges,N=1,000samples,A=5alternativeseach)
GPT-3.5+Uniform 1.06***(0.003) -0.94***(0.009) -0.02(0.001) -1,663.42 3,334.84
GPT-4oMini+Uniform 1.38***(0.02) -0.85***(0.02) 0.87***(0.01) -880.39 1,768.78
Claude3.5+Uniform 0.71***(0.009) -2.44***(0.02) 1.13***(0.005) -1,197.92 2,403.83
Llama370b+Uniform 1.04***(0.005) -0.36**(0.01) 0.71***(0.002) -1,269.42 2,546.83
GPT3.5+RecSys 1.68***(0.006) -0.35**(0.008) -0.91***(0.006) -1,613.85 3,235.69
GPT-4oMini+RecSys 3.16***(0.01) -0.49*(0.02) 0.67***(0.01) -681.39 1,370.78
Claude3.5+RecSys 1.85***(0.01) -0.87***(0.006) 0.16**(0.007) -1,542.90 3,093.80
Llama370b+RecSys 1.43***(0.01) 1.05***(0.007) 0.36***(0.005) -1,468.61 2,945.22
Note: *: P <0.05,**: P <0.01,***: P <0.001
Table 1: Effect sizes for real-world networks from Facebook100 [56], the Andorra dataset [61], and the MobileD dataset
[61] for several LLMs for temperature set to 0.5. We test two sampling strategies: a uniform strategy where A is sampled
t
uniformly from the set of nodes, and a recommender system (RecSys) based on logistic regression and trained on pairwise
nodesimilaritiesandnetworkcharacteristics(numberofcommonneighbors,Jaccardsimilarity,preferentialattachmentscore,
and the Adamic-Adar index). See Section A.3.3 for more information on the sampling strategies. Average marginal effects
(cf. Section B.2.3) show that homophily is the strongest driver of link formation, with recommendation-based sampling
amplifying the dominant mechanism in each dataset while preserving the overall ranking of behavioral factors.
14

(a)
(b)
(c)
Figure 5: Comparison between the network formation decisions among different models for the uniform
and the recommendation system sampling strategies. We report the Spearman correlation between the effects
correspondingtothefitsaswellasthetotalvariation(TV)distancebetweenthecorrespondingfittedmodels(cf. SectionA.3.4
for a detailed description of the metrics).
coefficients of 0.19 and 0.39, respectively (P < 0.001). This suggests that while LLMs do consider the
degree of potential connection nodes–favoring connections to well-connected nodes–the influence of this
factor is less evident compared to homophily.
15

The influence of triadic closure appears to vary across different datasets and models. In most cases,
the coefficients for triadic closure (θˆ ) are positive and significant, indicating that LLMs consider the
TC
numberofmutualconnectionswhenformingnewlinks. However,insomeinstances,suchaswithGPT-3.5
on the Andorra dataset, the triadic closure coefficient is negative (−0.24) and significant, suggesting a
structure-dependent role of this principle as shown by the low clustering coefficient of the network, which
is dominated by preferential attachment (cf. Section B.1). This variability implies that while triadic
closure is a factor in LLMs’ decision-making, its impact may be influenced by the specific characteristics
of the dataset or the model used.
Additionally, in Section B.4 we report the results for larger context windows (A ∈ {50,100}), and find
that our results are robust to larger context windows.
Thus, our analysis demonstrates that while homophily, triadic closure, and preferential attachment
are integral to the network formation behaviors of LLMs, homophily is the dominant factor.
Recommendation-Based Sampling and Model Alignment. In Figure 5, we present both the
Spearman correlations of these effects and the total variation (TV) distances between the distributions of
agent decisions under the fitted discrete choice models (see Section A.3.3 for details on the comparison
metrics).
Our analysis reveals that the key behavioral patterns of LLM agents, namely, the relative strength
of their preferences for homophily, triadic closure, and preferential attachment, are largely consistent
across different candidate selection strategies. Specifically, we observe high Spearman correlations and
low TV distances in the majority of comparisons, both when using the same sampling strategy and when
comparingtheuniformsamplingmethodtotherecommendation-basedapproach. Homophilystillremains
the dominant factor in the agent’s decisions and is context-dependent even when the agents interact with
the recommendation system.
These results suggest that the observed LLM behaviors are, in the majority, robust to variations in
how the candidate set A is constructed.
t
Average Marginal Effects. Due to space constraints, we report the average marginal effects (AMEs)
in Section B.2.3. The AMEs provide a complementary view of the regression results by quantifying the
expected change in choice probability associated with a one-unit change in each standardized feature.
Consistent with the coefficient estimates, homophily exhibits the largest AMEs in most datasets, often
exceeding 1.0 and reaching above 2.5 under the recommendation-based strategy (e.g., GPT-4 Mini on
UChicago30). Preferential attachment also shows consistently positive AMEs, though typically smaller
in magnitude than those for homophily, indicating a weaker, yet still significant, propensity to connect
to high-degree nodes. Triadic closure effects are more variable: in several Facebook100 networks they are
positive, reinforcing local clustering, while in datasets such as Andorra and MobileD they are frequently
negative, indicating a tendency to form cross-community links rather than closing triangles. Across
datasets, the recommendation-based strategy tends to amplify the dominant mechanism, i.e., most often
homophily in Facebook100 networks and preferential attachment in MobileD, highlighting that sampling
strategy can strengthen the prevailing behavioral bias while leaving the relative ranking of mechanisms
broadly consistent.
Change of Graph Statistics. Finally, the networks resulting from the newly added links preserve
the graph statistics (cf. [31]), such as the degree distribution, the adjacency matrix spectrum, and the
distribution of the sizes of the connected components (see Section B.2.2 and Section B.3.2). KS test
results show that adding these new edges (≤ 5% new edges) minimally affects global metrics – degree
distribution, spectrum, and component sizes remain largely unchanged – while significant shifts occur
mainly in local clustering, especially under the Uniform strategy. The Recommendation System produces
even fewer local changes, indicating that LLM-driven edge additions at this scale largely preserve overall
16

network structure, with strategy choice shaping only localized patterns. The results are also robust to
temperature changes (cf. Section B.3.2)
(a) (c)
(b)
(d)
Figure 6: Measurement of LLM-Human alignment for two contexts: Social network (n=100), and company
network (n = 103). (a) TV distance between fitted models and Spearman correlation between estimated effects. (b)
Effects and average marginal effects with standard errors to measure alignment between how different models and humans
rankpreferentialattachment,homophily,andtriadicclosure. (c)SpearmancorrelationandL distancebetweentheaverage
2
Bordacountvectorstomeasurealignmentbetweenhowdifferentmodelsandhumansrankpreferentialattachment,homophily,
andtriadicclosure. (d)Within-modelSpearmancorrelationsbetweenthedecisionswithineachmodeltomeasurealignment
within the decisions of one model. Section A.4 contains detailed information on the construction of the baseline.
Human Baseline
Survey. To assess how closely the network formation preferences of LLM agents align with human
decision-making, we conducted a controlled survey-based experiment involving both human participants
and LLMs. The experiment was designed to elicit link formation choices in two distinct social contexts:
(i) a social network where participants assumed the role of a student forming friendships within a college
social network, and (ii) a company network where participants assumed the role of an employee making
professional connections within a company network.
17

Foreachscenario,theparticipantwaspresentedwithafocalnode(representingthemselves)andA = 3
candidate profiles containing a value indicating similarity as well as relevant network statistics (degree,
common neighbors) with the focal profile. The participant was then asked to select exactly one candidate
with whom to form a connection and rate the criteria – among similarity, degree, and common neighbors
– that they considered when choosing the specific profile. Section A.4 contains more information about
the experimental setup.
We recruited human participants via the Prolific platform, ensuring diversity in demographic back-
grounds. We obtain n = 100 and n = 103 responses for the social and company network contexts,
respectively. To compare with LLM models, we administered the same dynamically-generated survey
inputs that we gave to each participant to an LLM – preserving the wording, structure, and candidate
attributes – for the five LLM models.
This experimental design allows for a direct, context-controlled comparison between human and LLM
decisionpatterns. Bypresentinganidenticalsetofalternatives, wecanmeasurealignmentintwocomple-
mentary ways: (i) at the principle level, by estimating discrete choice models for both humans and LLMs
and comparing the inferred effect sizes for homophily, triadic closure, and preferential attachment, and
(ii) at the choice level, by comparing the Borda count vectors between how the participants ranked each
criterion in their choices. Furthermore, the two scenarios are chosen to reflect socially and professionally
relevant settings as in the case of the real-world datasets.
LLM-HumanAlignmentinNetworkFormationContexts. Figure6summarizestheresultsofour
alignment study. Across all scenarios, the rankings of network formation principles based on effect sizes
are perfectly correlated between humans and LLMs, and the Borda vector averages are likewise almost
perfectly correlated (with the exception of Claude 3.5). The total variation (TV) distances between
the discrete choice models inferred from human and LLM choices are consistently small – below 0.32
in all cases and typically below 0.10 – indicating high distributional similarity (cf. panels (a)-(c)). In
the vast majority of cases, the signs of the estimated effects also match between humans and LLMs.
Consistent with our earlier observations in Table 1, we find strong homophily in the social network
context (θˆ > 0;P < 0.001) and strong heterophily in the company network context (θˆ < 0;P < 0.001).
H H
Additionally, the ranking of the effects is consistent with our findings in Table 1.
While aggregate-level alignment between human and LLM decisions is high across models (cf. Fig-
ure 6a-c), notable differences emerge in within-model agreement. Specifically, LLMs exhibit substantially
higherinternalconsistencyintheirdecisionrankingsthanhumans, whodisplaygreatervariabilityintheir
within-model rankings (cf. Figure 6d).
Discussion
Summary of Findings and Broader Impact
In this study, we conducted a comprehensive evaluation of LLMs’ network formation preferences, examin-
ing both micro-level network principles–such as preferential attachment, triadic closure, and homophily–
and macro-level network properties like community structure and the small-world phenomenon. Our
findings indicate that networks generated by multiple LLMs exhibit these properties, particularly when
themodelsareprimedwithnetworkstatisticslikethenumberofmutualfriendsorthedegreesofpotential
connections. Furthermore, using discrete choice modeling, we explored the emergence of these proper-
ties in simulations based on real-world networks. Our results reveal that the LLM agents’ selections are
predominantly driven by homophily, followed by triadic closure and preferential attachment.
On the one hand, our study enhances our understanding of how multiple LLMs behave in networked
settings. Specifically, our findings reveal varying strengths in network formation properties among LLMs,
suggesting that when these models are employed to coordinate social networks in social or work envi-
ronments, they may exhibit human-like behaviors. This has important implications for applications like
18

agent-based modeling, where a realistic simulation of human behavior is crucial. Traditionally, agent-
based models rely on “formalized” rules or heuristics to represent individual behaviors, which may not
adequately capture the complexity of human decision-making. Given the abilities of LLMs to solve com-
plex tasks that require extensive reasoning, which may be beyond the scope of a traditional agent-based
modeling framework, LLM agents provide the potential to simulate more nuanced and context-aware in-
teractionsthatcanpotentiallyresemblehumansocialbehaviorcloselywithouttheneedtospecifydecision
rules or heuristics rigidly.
In addition, our work expands and provides several novel results to the existing literature of findings
on LLM-based network simulations [4, 19, 43], and is the first, to the best of our knowledge, to include
a human baseline to verify the findings. Specifically, in our work, we show the emergence of several
topological collective biases, which are complementary to the linguistic social conventions found in [4] and
[19], and the emergence of the friendship paradox on LLM-generated networks, as shown in [43].
Limitations and Boundary Conditions
On the other hand, our results suggest that we should exercise caution when leveraging LLMs in net-
working scenarios. The model family, configuration, and prompts can subtly affect the models’ behavior,
resulting in qualitatively similar but quantitatively different outcomes.
For example, newer models such as GPT-4 and Claude 3.5 exhibit stronger biases compared to prior
models such as GPT-3.5. For instance, in the preferential attachment principle, newer models such
as GPT-4 and Claude 3.5 have stronger biases – i.e., connect to highest-degree-nodes yielding star-like
networks – compared to GPT-3.5 and LLama 3, which had weaker biases – i.e., connect to high-degree-
nodes. Similar results can be found in homophily, as larger biases towards homophily and triadic closure.
Thus, even though LLMs exhibit these principles, we should be cautious of such biases when designing
simulations.
Similarly, in our experiments with real-world data, we find an interesting phase transition from ho-
mophily to heterophily: In the Facebook100 data, the LLMs generally exhibited positive biases toward
homophily (θˆ > 0). However, in employment networks, agents were either managers or subordinates,
H
and we discovered that LLM agents were heterophilous in such a case (θˆ < 0), which aligns with ca-
H
reer advancement dynamics (i.e., employees want to form links with managers because of better career
prospects).
Additionally,eventhoughonaggregateLLMandhumanresponsesarealigned,thefine-grainedpicture
on the individual level is different: When compared to human responses, the responses given by LLMs
are significantly more correlated than the responses obtained by humans (cf. Figure 6).
The above underscores the need for researchers to provide oversight and ensure that LLM behaviors
align with human expectations when employing them in scientific research methods, such as agent-based
modeling and even prototypical human subject research with LLMs.
Thus, although we find that LLMs resemble human network formation behaviors, we should consider
whether these models should exhibit such behaviors when serving as assistants to humans in work and so-
ciallives. Biaseslikehomophily,triadicclosure,orpreferentialattachmentmayleadtonetworkstructures
that overemphasize certain individuals or fragment information flow.
Therefore, whenusedassocialassistants, LLMsmaynotnecessarilyneedtomirrorhumannetworking
behaviors and could be personalized to promote more equitable and efficient information dissemination.
Our study highlights the need for more deliberate efforts to align LLM behavior in this domain.
Future Research Directions
Looking ahead, we identify three promising directions for future research: First, investigating LLM be-
havior in more complex interactions, such as simulated dialogues, could provide deeper insights. By
examining the specific dialogues of LLMs during interactions, we can better understand their network
formation preferences and how they adapt to different social dynamics. Second, we could explore how
19

LLMscanbeintegratedintoreal-worldsettings, suchassocialmediaplatforms. LLM-assistedbotsmight
be employed to facilitate interactions, break echo chambers, and moderate democratic discussions (see,
for example, [46, 2]).
An important direction for future work is to more explicitly integrate the synthetic and empirical
analyses. While our current study shows that the same micro-level principles (homophily, triadic closure,
preferential attachment) emerge across both settings, a systematic structural comparison would further
validate external robustness. For instance, one can quantify the similarity of LLM-generated synthetic
graphs and empirical benchmarks using metrics such as degree distribution, clustering coefficient, assor-
tativity, modularity, or spectral properties. Moreover, causal inference techniques (e.g., counterfactual
link removal or intervention-based analyses) could help identify whether the same underlying mechanisms
explain network growth in both idealized and real-world scenarios. Such approaches would not only im-
proveinterpretabilitybutalsoestablishstrongerguaranteesthatLLM-drivenbehaviorsgeneralizebeyond
controlled synthetic environments.
Finally, we can use our methods to create realistic synthetic networks. These synthetic datasets can
serve as benchmarks for evaluating graph learning methods, thereby addressing the scarcity of existing
graph benchmarks (cf. [45]). By adjusting parameters like temperature and environmental settings or
selecting different models, we can generate diverse networks to test graph neural network performance
under various conditions. Importantly, our approach allows for the generation of artificial data that
resembles real-world data while adhering to privacy regulations.
Acknowledgements
The authors would like to thank Nikhil Garg, Jon Kleinberg, Yanbang Wang, Yuanqi Du, the attendees
of the Learning on Graphs NYC meetup, and the participants of the Cornell AI, Policy, and Practice
working group for their valuable feedback on the current version of the paper.
References
[1] G. V. Aher, R. I. Arriaga, and A. T. Kalai. Using large language models to simulate multiple
humans and replicate human subject studies. In International Conference on Machine Learning,
pages 337–371. PMLR, 2023.
[2] J. R. Anthis, R. Liu, S. M. Richardson, A. C. Kozlowski, B. Koch, E. Brynjolfsson, J. Evans, and
M. S. Bernstein. Position: LLM Social Simulations Are a Promising Research Method. In Forty-
second International Conference on Machine Learning Position Paper Track, 2025.
[3] Anthropic. Claude: Large Language Model by Anthropic, 2024. Accessed: 2024-09-18.
[4] A. F. Ashery, L. M. Aiello, and A. Baronchelli. Emergent Social Conventions and Collective Bias in
LLM Populations. Science Advances, 11(20):eadu9368, 2025.
[5] E. Bakshy, I. Rosenn, C. Marlow, and L. Adamic. The Role of Social Networks in Information
diffusion. In Proceedings of the 21st International Conference on World Wide Web, pages 519–528,
2012.
[6] A. Banerjee, A. G. Chandrasekhar, E. Duflo, and M. O. Jackson. The Diffusion of Microfinance.
Science, 341(6144):1236498, 2013.
[7] A.-L. Barab´asi and R. Albert. Emergence of Scaling in Random Networks. Science, 286(5439):509–
512, 1999.
[8] G. Bianconi and A.-L. Barab´asi. Competition and Multiscaling in Evolving networks. Europhysics
letters, 54(4):436, 2001.
20

[9] V. D. Blondel, J.-L. Guillaume, R. Lambiotte, and E. Lefebvre. Fast unfolding of communities in
large networks. Journal of statistical mechanics: theory and experiment, 2008(10):P10008, 2008.
[10] S. Bordia and S. Bowman. Identifying and Reducing Gender Bias in Word-Level Language Mod-
els. In Proceedings of the 2019 Conference of the North American Chapter of the Association for
Computational Linguistics: Student Research Workshop, pages 7–15, 2019.
[11] P. Brookins and J. M. DeBacker. Playing Games with GPT: What can we learn about a Large
Language Model from Canonical Strategic Games? Available at SSRN 4493398, 2023.
[12] Y. Chen, T. X. Liu, Y. Shan, and S. Zhong. The Emergence of Economic Rationality of GPT.
Proceedings of the National Academy of Sciences, 120(51):e2316205120, 2023.
[13] R. Chew, J. Bollenbacher, M. Wenger, J. Speer, and A. Kim. LLM-assisted content analysis: Using
large language models to support deductive coding. arXiv preprint arXiv:2306.14924, 2023.
[14] F. Chopra and I. Haaland. Conducting qualitative interviews with AI. CESifo Working Paper, 2023.
[15] F. Chung and L. Lu. The Average Distance in a Random Graph with given Expected Degrees.
Internet Mathematics, 1(1):91–113, 2004.
[16] A. Clauset, M. E. Newman, and C. Moore. Finding community structure in very large networks.
Physical review E, 70(6):066111, 2004.
[17] G. De Marzo, L. Pietronero, and D. Garcia. Emergence of Scale-Free Networks in Social Interactions
among Large Language Models. arXiv preprint arXiv:2312.06619, 2023.
[18] B. Fatemi, J. Halcrow, and B. Perozzi. Talk like a Graph: Encoding Graphs for Large Language
Models. In The Twelfth International Conference on Learning Representations, 2024.
[19] A. Ferraro, A. Galli, V. La Gatta, M. Postiglione, G. M. Orlando, D. Russo, G. Riccio, A. Ro-
mano, and V. Moscato. Agent-based Modelling meets Generative AI in Social Network Simulations.
In International Conference on Advances in Social Networks Analysis and Mining, pages 155–170.
Springer, 2024.
[20] A. Filippas, J. J. Horton, and B. S. Manning. Large language models as simulated economic agents:
What can we learn from homo silicus? In Proceedings of the 25th ACM Conference on Economics
and Computation, pages 614–615, 2024.
[21] J. H. Fowler and N. A. Christakis. Dynamic Spread of Happiness in a Large Social Network: Lon-
gitudinal Analysis over 20 years in the Framingham Heart Study. British Medical Journal, 337,
2008.
[22] C.Gao,F.Xu,X.Chen,X.Wang,X.He,andY.Li. SimulatingHumanSocietywithLargeLanguage
Model Agents: City, Social Media, and Economic System. In Companion Proceedings of the ACM
Web Conference 2024, pages 1290–1293, 2024.
[23] M. S. Granovetter. The Strength of Weak Ties. American Journal of Sociology, 78(6):1360–1380,
1973.
[24] J. He, F. Wallis, and S. Rathje. Homophily in An Artificial Social Network of Agents Powered by
Large Language Models. OSF, 2023.
[25] M. O. Jackson. Social and economic networks, volume 3. Princeton university press Princeton, 2008.
21

[26] A. Z. Jacobs and D. J. Watts. A large-scale comparative study of informal social networks in firms.
Management Science, 67(9):5489–5509, 2021.
[27] E. Jahani, S. P. Fraiberger, M. Bailey, and D. Eckles. Long ties, disruptive life events, and economic
prosperity. Proceedings of the National Academy of Sciences, 120(28):e2211062120, 2023.
[28] J. Kleinberg. The Small-world Phenomenon: An Algorithmic Perspective. In Proceedings of the
Thirty-second Annual ACM Symposium on Theory of Computing, pages 163–170, 2000.
[29] H. Kotek, R. Dockum, and D. Sun. Gender Bias and Stereotypes in Large Language Models. In
Proceedings of The ACM Collective Intelligence Conference, pages 12–24, 2023.
[30] Y. Leng, T. Sowrirajan, Y. Zhai, and A. Pentland. Interpretable Stochastic Block Influence Model:
Measuring Social Influence among Homophilous Communities. IEEE Transactions on Knowledge
and Data Engineering, 2023.
[31] J.LeskovecandC.Faloutsos. SamplingfromLargeGraphs. InProceedingsofthe12thACMSIGKDD
International Conference on Knowledge Discovery and Data Mining, pages 631–636, 2006.
[32] D. Liben-Nowell and J. Kleinberg. The Link Prediction Problem for Social Networks. In Proceedings
of the Twelfth International Conference on Information and Knowledge Management, pages556–559,
2003.
[33] D. C. Liu and J. Nocedal. On the Limited Memory BFGS method for Large Scale Optimization.
Mathematical Programming, 45(1):503–528, 1989.
[34] D. Lyu, Y. Yuan, L. Wang, X. Wang, and A. Pentland. Investigating and modeling the dynamics of
long ties. Communications Physics, 5(1):87, 2022.
[35] B. S. Manning, K. Zhu, and J. J. Horton. Automated Social Science: A Structural Causal Model-
Based Approach. SSRN, 2024.
[36] D. McFadden. Conditional Logit Analysis of Qualitative Choice Behavior. Working Paper, 1972.
[37] M. McPherson, L. Smith-Lovin, and J. M. Cook. Birds of a Feather: Homophily in Social Networks.
Annual Review of Sociology, 27(1):415–444, 2001.
[38] M. Mosleh, D. Eckles, and D. G. Rand. Tendencies Toward Triadic Closure: Field Experimental
Evidence. Proceedings of the National Academy of Sciences, 122(27):e2404590122, 2025.
[39] M. E. Newman. Mixing patterns in networks. Physical review E, 67(2):026126, 2003.
[40] M. E. Newman. Modularity and community structure in networks. Proceedings of the national
academy of sciences, 103(23):8577–8582, 2006.
[41] M. E. Newman and M. Girvan. Finding and evaluating community structure in networks. Physical
review E, 69(2):026113, 2004.
[42] OpenAI. GPT-4 technical report. arXiv, pages 2303–08774, 2023.
[43] G. M. Orlando, V. La Gatta, D. Russo, and V. Moscato. Can Generative Agent-Based Modeling
ReplicatetheFriendshipParadoxinSocialMediaSimulations? InProceedings of the 17th ACM Web
Science Conference 2025, pages 510–515, 2025.
[44] J. Overgoor, A. Benson, and J. Ugander. Choosing to Grow a Graph: Modeling Network Formation
as Discrete Choice. In The World Wide Web Conference, pages 1409–1420, 2019.
22

[45] J. Palowitch, A. Tsitsulin, B. Mayer, and B. Perozzi. Graphworld: Fake graphs bring real insights
for gnns. In Proceedings of the 28th ACM SIGKDD Conference on Knowledge Discovery and Data
Mining, pages 3691–3701, 2022.
[46] M.Papachristou,L.Yang,andC.-C.Hsu. LeveragingLargeLanguageModelsforCollectiveDecision-
Making. In Proceedings of the 28th ACM Conference on Computer-Supported Cooperative Work (to
appear), 2023.
[47] J. S. Park, J. C. O’Brien, C. J. Cai, M. R. Morris, P. Liang, and M. S. Bernstein. Generative Agents:
Interactive Simulacra of Human Behavior. In Proceedings of the 36th Annual ACM Symposium on
User Interface Software and Technology, pages 1–22, 2023.
[48] P. S. Park, J. E. Blumenstock, and M. W. Macy. The strength of long-range ties in population-scale
social networks. Science, 362(6421):1410–1413, 2018.
[49] B.Perozzi,B.Fatemi,D.Zelle,A.Tsitsulin,M.Kazemi,R.Al-Rfou,andJ.Halcrow. LetYourGraph
Do the Talking: Encoding Structured Data for LLMs. arXiv preprint arXiv:2402.05862, 2024.
[50] I. Rahwan, M. Cebrian, N. Obradovich, J. Bongard, J.-F. Bonnefon, C. Breazeal, J. W. Crandall,
N. A. Christakis, I. D. Couzin, M. O. Jackson, et al. Machine Behaviour. Nature, 568(7753):477–486,
2019.
[51] E. M. Rogers. Diffusion of Innovations. Simon and Schuster, 5th edition, 2003.
[52] G. Rossetti, M. Stella, R. Cazabet, K. Abramski, E. Cau, S. Citraro, A. Failla, R. Improta,
V. Morini, and V. Pansanella. Y social: an llm-powered social media digital twin. arXiv preprint
arXiv:2408.00818, 2024.
[53] H.Tajfel,M.G.Billig,R.P.Bundy,andC.Flament. SocialCategorizationandIntergroupBehaviour.
European Journal of Social Psychology, 1(2):149–178, 1971.
[54] H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra,
P. Bhargava, S. Bhosale, D. Bikel, L. Blecher, C. Canton Ferrer, M. Chen, G. Cucurull, D. Esiobu,
J. Fernandes, J. Fu, W. Fu, B. Fuller, C. Gao, V. Goswami, N. Goyal, A. Hartshorn, S. Hosseini,
R. Hou, H. Inan, M. Kardas, V. Kerkez, M. Khabsa, I. Kloumann, A. Korenev, P. S. Koura, M.-A.
Lachaux,T.Lavril,J.Lee,D.Liskovich,Y.Lu,Y.Mao,X.Martinet,T.Mihaylov,P.Mishra,I.Moly-
bog, Y. Nie, A. Poulton, J. Reizenstein, R. Rungta, K. Saladi, A. Schelten, S. Ruan, S. E. Michael,
S. Ranjan, T. X. Ellen, T. Binh, T. Ross, W. Adina, X. Jian, X. K. Puxin, Y. Zheng, Z. Iliyan,
Z. Yuchen, F. Angela, K. Melanie, N. Sharan, R. Aurelien, S. Robert, E. Sergey, and S. Thomas.
Llama 2: Open Foundation and Fine-Tuned Chat Models. arXiv preprint arXiv:2310.12345, 2023.
[55] K. E. Train. Discrete Choice Methods with Simulation. Cambridge university press, 2009.
[56] A. L. Traud, P. J. Mucha, and M. A. Porter. Social Structure of Facebook Networks. Physica A:
Statistical Mechanics and its Applications, 391(16):4165–4180, 2012.
[57] V.Veselovsky, M.H.Ribeiro, andR.West. ArtificialArtificialArtificialIntelligence: CrowdWorkers
Widely use Large Language Models for Text Production Tasks. arXiv preprint arXiv:2306.07899,
2023.
[58] J. Vig, S. Gehrmann, Y. Belinkov, S. Qian, D. Nevo, Y. Singer, and S. Shieber. Investigating
Gender Bias in Language Models using Causal Mediation Analysis. Advances in Neural Information
Processing Systems, 33:12388–12401, 2020.
23

[59] D. J. Watts and S. H. Strogatz. Collective Dynamics of “Small-world” Networks. Nature,
393(6684):440–442, 1998.
[60] J.Wei,X.Wang,D.Schuurmans,M.Bosma,E.Chi,Q.Le,andD.Zhou. Chainofthoughtprompting
elicits reasoning in large language models. arXiv preprint arXiv:2201.11903, 2022.
[61] Y. Yuan, A. Alabdulkareem, and A. Pentland. An Interpretable Approach for Social Network For-
mation among Heterogeneous Agents. Nature Communications, 9(1):4704, 2018.
[62] X. Zhou, H. Zhu, L. Mathur, R. Zhang, H. Yu, Z. Qi, L.-P. Morency, Y. Bisk, D. Fried, G. Neubig,
and M. Sap. SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents. In The
Twelfth International Conference on Learning Representations, 2024.
24

Supplementary Material for
“Network Formation and Dynamics among
Multi-LLMs
Marios Papachristou10, Yuan Yuan
A Methods and Materials
A.1 Experimental Procedure
In our study, we performed experiments to assess whether key network principles at both the micro-
level (such as preferential attachment, triadic closure, and homophily) and the macro-level (including
community structure and weak ties) align with classical network models. Subsequently, we utilized real-
world networks to determine the factors that are most heavily weighted by LLMs.
A.1.1 Network Formation Process
Our experiments span a time series of T steps, with a sequence of network structures denoted as
G ,G ,...,G with vertex sets V ,...,V . The initial network, G , is referred to as the seed network.
1 2 T 1 T 1
At each step t, we select a query node i (which may either be a new arrival or an existing node in
t
the graph) and assign it the task of forming new links. This is accomplished by selecting nodes from
a set of alternatives A (meaning potential candidates for link formation) and initiating a query call
t
Q(A ,i ,δ) to the LLM (as outlined in Algorithm SI.2) to create up to δ new links. The edge set selection
t t
process involves presenting the LLMs with personal or network features of the alternatives, denoted as
F(A ) = {f : a ∈ A }, which may include information such as the neighbors of the nodes, node degrees,
t a t
common connections with i , and community memberships, formatted in JSON. We adopt a zero-shot
t
learning approach, avoiding the provision of examples to the model to prevent bias, in line with relevant
studies such as [11]. This approach allows for the exploration of the innate preferences of LLMs.
We employ multiple temperatures to account for the variability in response generation by LLM sys-
tems, which is also observed in classical statistical models of network formation [25]. Our study conducts
experiments using three temperatures for all models except Claude 3.5: 0.5, 1.0, and 1.5. For Claude 3.5
the temperature range is between 0 and 1, and we run experiments with two temperatures: 0.5, and 1.0.
Moreover, the model is tasked with outputting a JSON object indicating the node chosen for link
formationandtherationalebehindthechoice. ThisapproachisadoptedbecauseLLMshavedemonstrated
proficiency in processing code-like structures, such as HTML and JSON.
A.1.2 Prompts
The general prompt we use is given in Algorithm SI.2. An example of this prompt is given at Algo-
rithm SI.1.
10Correspondence to: mpapachr@asu.edu
1

Algorithm SI.1 Example prompt regarding social network data.
# Task
You are located in a school. Your task is to select a set of people to be friends
with.
# Profile
Your profile is given below after chevrons:
<PROFILE>
{
"name" : "Person 0",
"favorite subject" : "Chemistry",
"neighbors" : ["Person 3", "Person 432", "Person 4", "Person 3", "Person
32"]
}
</PROFILE>
# Candidate Profiles
The candidate profiles to be friends with are given below after chevrons:
<PROFILES>
[
{
"name" : "Person 1",
"favorite subject" : "Mathematics",
"neighbors" : ["Person 3", "Person 4", "Person 23", "Person 65"]
},
{
"name" : "Person 33",
"favorite subject" : "History",
"neighbors" : ["Person 342", "Person 2", "Person 12"]
}, ...
]
</PROFILES>
# Output
The output should be given a list of JSON objects with the following structure
[
{{
"name" : name of the person you selected,
"reason" : reason for selecting the person
}}, ...
]
# Notes
- The output must be a list of JSON objects ranked in the order of preference.
- You can make at most 1 selection.
2

Algorithm SI.2 General Prompt used to implement Q(A ,i ,δ).
t t
# Task
Your task is to select a set of people to be friends with.
# Profile
Your profile is given below after chevrons:
<PROFILE>F({i })</PROFILE>
t
# Candidate Profiles
The candidate profiles to be friends with are given below after chevrons:
<PROFILES>F(A )</PROFILES>
t
# Output
The output should be given a list of JSON objects with the following structure
[
{{
"name" : name of the person you selected,
"reason" : reason for selecting the person
}}, ...
]
# Notes
- The output must be a list of JSON objects ranked in the order of preference.
- You can make at most δ selections.
A.1.3 Feature Representations for Prompts
Below, we give examples of the features used in the prompt presented in Algorithm SI.2. The features
are formatted as a list of JSON objects which are provided to the prompt.
Principle 1: Preferential Attachment. We have the following features:
[
{
"name" : 0,
"neighbors" : [5, 7, 1, 6]
},
...
]
Principle 2: Triadic Closure. We have the following features:
[
{
"name" : 0,
"common_neighbors" : [5, 7, 1, 6]
},
...
]
Principle 3: Homophily. We have the following features:
[
{
"name" : 0,
"favorite_color" : "red",
"hobby" : "hiking",
"location" : "Boston"
},
3

...
]
Principle 5: Small-World. We have the following features:
[
{
"name" : 0,
"neighbors" : [5, 7, 1, 6]
},
...
]
Real-World Data. We have the following features:
[
{
"name" : 0,
"status" : "student",
"major" : 10,
"second major" : 93,
"accommodation" : "house",
"high_school" : 5,
"graduation_year" : 2008
},
...
]
We note that the initial Facebook100 dataset included gender information as a feature. We chose not
to include gender as one of the features, as it has been shown that language models exhibit gender bias
[58, 29, 10]. An example of the prompt using real-world social network data is given at Algorithm SI.1.
A.1.4 Robustness Checks and Prompt Sensitivity
We tried the following LLM models:
• GPT-3.5 (gpt-3.5-turbo)
• GPT-4o Mini (gpt-4o-mini)
• Llama 3 (llama-3-70b-instruct)
• Claude 3.5 Sonnet (claude-3-5-sonnet-20240620).
For each of the models except Claude 3.5 we used three temperatures: 0.5, 1.0, 1.5. For the Claude
3.5 model we used temperatures 0.5 and 1.0 (since the model does not allow temperatures above 1.0). Fi-
nally, we experimented with different contexts (e.g., friendship, collaboration, community) to test prompt
sensitivity.
A.2 Details for Small-World Experiments
The algorithm for the altered Watts-Strogatz model is described as follows:
1. Similarly to Watts-Strogatz, we first create a ring network with n nodes. After that, for each node
[n], we create k edges where k/2 edges connect to its rightmost neighbors and k/2 edges connect to
its leftmost neighbors.
2. TocreateG ,foreachnode[n],wetakeitsk/2rightmostneighborsandrewirethemwithprobability
t
β. For each of the k/2 rightmost neighbors that are to be rewired, we make one query to the LLM,
which indicates how the edge will be rewired. The choice is made by providing the LLM with all
the network nodes and each node’s neighbors (i.e., the network structure).
4

ThemodelcloselyresemblestheWatts-Strogatzmodel,withtheprimarydistinctionbeingthemethod
of edge rewiring. Instead of randomly selecting edges for rewiring, as in the Watts-Strogatz model, we
determine the rewiring of an edge by inquiring about the LLM and providing it with the current network
structure.
A.3 Real-World Network Experiments
A.3.1 The Discrete Choice Model in Real-World Network Experiments
For each node i that we consider at time t, we randomly remove one of its current friends from the
t
real-world network. After we remove a neighbor for each of i ,...,i , we end up with the network G ,
1 T 1
which we use as a seed network for the LLM agents.
Subsequently, during the link formation process, we present each node i with a set of candidate nodes
t
(denoted by A ), comprising one of the previously removed friends and other nodes that are not their
t
friends. We then instruct the LLM to form a link with one of the candidates, providing the attributes
of the candidates and the social network structure to aid its decision-making. These choices are made
sequentially.
We use the utility of the model for each node for each sequential decision of network formation:
U = θ logd +θ logw +θ logc +ϵ .
ij,t PA j,t H ij TC ij,t ij,t
Inthisequation, θ measuresthestrengthofpreferentialattachmentbasedonthedegreed ofj atstep
PA j,t
t, θ measures the strength of homophily based on the similarity w (i.e. number of common attributes)
H ij
between i and j, and θ measures the strength of triadic closure, based on the number of common
TC
neighbors c between i and j at step t. The error term ϵ is distributed as i.i.d. standard Gumbel.11
ij,t ij,t
All variables are first normalized based on their range, and then the log transformation is taken.
The multinomial logit model (MNL) indicates that the probability that i links to j at step t is given
by
dθPAwθHcθTC
p =Pr (cid:2) argmax U =j (cid:3) = j,t ij ij,t . (2)
ij,t r∈At ir,t (cid:80) dθPAwθHcθTC
r∈At r,t ir ir,t
Given a sequence of nodes i ,...,i ∈ V and choices (denoted by subscripted j) j ∈ A ,...,j ∈ A ,
1 T 1 1 T T
the parameters can be found by maximizing the log-likelihood function. To get the standard errors of the
coefficients and the corresponding P-values, we follow the process outlined in [44].
A.3.2 Estimating the Parameters of the Discrete Choice Model
Toestimatetheparametersofthediscretechoicemodel, weoptimizethefollowinglog-likelihoodfunction:
T (cid:18) (cid:19)
(θˆ ,θˆ ,θˆ )= argmax (cid:88) θ logd +θ logw +θ logc −log (cid:0) (cid:88) dθPAwθHcθTC (cid:1) , (3)
PA TC H PA jt,t H itjt TC itjt,t r,t itr itr,t
(θPA,θTC,θH)∈R3
t=1 r∈At
where i ,...,i are the chooser nodes (i.e., the LLM agents who want to form a link), and j ,...,j are
1 T 1 T
the nodes which are chosen from the alternative sets A ,...,A . The likelihood function is convex, and
1 T
we optimize it with the L-BFGS-B method [33]. The standard errors of the coefficients are approximated
as (cid:112) −H−1/N where H is the Hessian matrix of the log-likelihood at (θˆ ,θˆ ,θˆ ) and N is the number
PA TC H
of data points (cf. [44, 55]).
11The standard Gumbel distribution has CDF ee−x .
5

A.3.3 Candidate Set Construction for Network Decisions
At each decision step t, a query node i selects a link from a set of candidate nodes A . Given the limited
t t
context window of LLMs, we consider two alternative strategies for constructing the candidate set A :
t
• Uniform Sampling. We uniformly sample A non-neighbor nodes from the graph. This approach
serves as a neutral baseline, ensuring that the alternatives presented to the model are selected
without structural or feature-based bias. Uniform sampling reflects a scenario where the agent has
no a priori ranking or filtering of candidates and evaluates all choices purely based on the features
provided in the prompt.
• Recommendation-Based Sampling. Weuseasupervisedlinkpredictionmodelbasedonlogistic
regressiontocomputethelikelihoodofalinkbetweeneachcandidatepair{i,j}followingtheworkof
[32]. Theprobabilityof{i,j}beinganedgeequalsσ (cid:0) ψTz (cid:1) whereσ(·)isthesigmoidfunction, ψ is
ij
(cid:16) (cid:17)
a vector of trainable parameters, and z = w ,c ,d ·d , (cid:80) 1 , |Nt(i)∩Nt(j)|
ij,t ij ij,t i,t j,t k∈Nt(i)∩Nt(j) log|d
k,t
| |Nt(i)∪Nt(j)|
is the feature vector for the pair {i,j} with the following entries:
– Similarity between node attributes w .
ij
– Number of common neighbors c .
ij,t
– Preferential attachment score d ·d .
i,t j,t
– Adamic-Adar index (cid:80) 1 .
k∈Nt(i)∩Nt(j) log|d
k,t
|
– Jaccard Similaririty between node neighborhoods
|Nt(i)∩Nt(j)|
.
|Nt(i)∪Nt(j)|
To avoid structural bias due to the LLM agents, the logistic regression model is trained at t = 1,
i.e., prior to any link formation by the LLM agents, as:
 
ψˆ= argmax  (cid:88) logσ (cid:0) ψTz (cid:1) + (cid:88) log (cid:0) 1−σ(ψTz ) (cid:1)  ,
ij,1 ij,1
ψ∈R5  
{i,j}∈E+ {i,j}∈E−
where E and E are equally sized sets of positive and negative edges sampled from G . For each
+ − 1
t, the set A , which is presented to the LLM agent, is constructed as the top-A highest-scoring
t
nodes concerning node i , where the scores are computed as yˆ = σ(ψˆTz ). To train the logistic
t it,j itj,t
regression model, we use the statsmodels Python package. Information about the parameters of
the link prediction algorithms can be found in Section B.2.1.
A.3.4 Measuring Alignment Between Models
The plots of Figure 5 are constructed by measuring similarity between models. Specifically, for two LLM
models M and M′, we fit two discrete choice models θˆM and θˆM′ respectively according to Equations (2)
and (3) and measure the following:
(cid:16) (cid:17)
• Spearman correlation Between Effects. We measure Spearman θˆM,θˆM′ , which measures
thedifferenceinhowthedifferentLLMmodelsrankpreferentialattachment, homophily, andtriadic
closure.
• TV Distance Between Fitted Models. We measure the total variation distance between the
probabilities that each LLM model assigns to nodes parametrized by the MNL model. Specifically,
6

the TV distance is calculated by sampling a time index t uniformly in {1,...,T} and a pair of a
node u and an alternative set A from G as follows:
t t t
d TV (M,M′)= 1 2 E t∼U({1,...,T}) E (ut,At)∼Gt   (cid:88) (cid:12) (cid:12) (cid:12) (cid:12) (cid:12)(cid:80) d θ v ˆ P M ,t Aw θˆM u θˆ H M v c θˆ θ u ˆ M T M v C ,t θˆM − (cid:80) d θ u ˆ P j ,t A θ w ˆM u θˆ H ′ M v ′ θ c ˆM θ u ˆ T M v ′ C ,t ′ θˆM′ (cid:12) (cid:12) (cid:12) (cid:12) (cid:12)  . (4)
v∈At (cid:12) r∈A d r, P t Aw uHr c u T r, C t r∈A d r, P t Aw uHv c u T v C ,t(cid:12)
In our implementation, we report the Monte-Carlo estimate of Equation (4).
A.4 Human Baseline
A.4.1 Survey
We construct the survey by presenting three alternatives (A = 3) to each participant in two different con-
texts (social network, company network). For each participant i, and each context ω ∈ {Social Network,
Company}, we generate a dynamic survey with alternative set A . For each alternative j ∈ A we
i,ω i,ω
generate:
1. Number of friends (degree) d . Uniformly sampled integer between 0 and 1000.
j,ω
2. Number of common friends (common neighbors) c . Uniformly sampled integer between
ij,ω
0 and the number of friends (degree).
3. Similarity w . Uniformly sampled integer between 0 and 10 for the social network context,
ij,ω
indicating the number of common interests. Uniformly sampled binary variable determining the
role of the person (0 for co-worker, 1 for manager).
Forthesocialnetworkcontext,weasktheparticipant(focusprofile)topretendtobeacollegestudent.
For the company network context, we ask the participant to pretend to be an employee (non-manager).
The participants are asked how they ranked – from 1 to 3 (1 = worst, 3 = best) – the three attributes
when forming their decision and optionally give the reasoning behind their decisions.
IRB Approval. The study protocol was approved by the Institutional Review Board of Cornell Uni-
versity (Protocol #IRB0150009), and all participants provided informed consent prior to participation.
A.4.2 Sample Size Construction on Prolific
We distribute the survey on the Prolific platform on participants located in the United States, who are
at least 18 years old and speak English as their primary language. We obtain n = 100 responses for the
social network context, and n = 103 responses for the company context. We use the standard sampling
settings for prolific. Participants are allowed to submit the survey only once.
A.4.3 Measuring Alignment between models and Humans
For each participant i, context ω ∈ {Social Network,Company} and alternative set A we construct
i,ω
z = (d ,c ,w ) for each j ∈ A . We let yM ∈ A to be the decision of model/human M abd
ij,ω j,ω ij,ω ij,ω i,ω i,ω i,ω
hM to be the vector of Borda counts for the choice yM. For instance, if a human participant ranked
i,ω i,ω
homophily over triadic closure over preferential attachment, their Borda score vector is hHuman = (1,2,3)
i,ω
assuming that the first dimension corresponds to preferential attachment (number of friends), the second
dimensioncorrespondstotriadicclosure(numberofcommonfriends),andthethirddimensioncorresponds
to homophily (similarity).
7

Between-Model Agreement. For each model M we fit a discrete choice model θˆM similarly to
Section A.3.1. We also calculate the average Borda Score vector as h¯M = 1 (cid:80)n hM
ω n i=1 i,ω
To measure between-model agreement we compare the pairs of models according to the following
criteria:
(cid:16) (cid:17)
1. Principle-Level. For each pair of models we measure Spearman θˆM,θˆM′ and d (M,M′)
TV
similarly to Equation (4).
(cid:16) (cid:17) (cid:13) (cid:13)
2. Choice-Level. ForeachpairofmodelswemeasureSpearman h¯M,h¯M′ andthedistance(cid:13)h¯M−h¯M′(cid:13)
ω ω (cid:13) ω ω (cid:13)
2
Within-Model Agreement. To measure the within-model agreement for model M we measure the
average Spearman correlation of the Borda count vectors between pairs of participants, i.e.
1 (cid:88)
Spearman
(cid:0) hM,hM(cid:1)
.
(cid:0)n(cid:1) i,ω j,ω
2 i,j:i<j
Survey Prompt. We use the prompt described in Algorithm SI.3 for the survey data.
A.4.4 Robustness Checks and Prompt Sensitivity
Models. We tried the following LLM models:
• GPT-3.5 (gpt-3.5-turbo)
• GPT-4o Mini (gpt-4o-mini)
• Llama 3 (llama-3-70b-instruct)
• Claude 3.5 Sonnet (claude-3-5-sonnet-20240620).
Additionally, to measure alignment with humans we use data collected from humans through the
Prolific platform
Temperatures. For each of the models except Claude 3.5 we used three temperatures: 0.5, 1.0, 1.5.
For the Claude 3.5 model we used temperatures 0.5 and 1.0 (since the model does not allow temperatures
above 1.0). In the main paper we report results with temperature equal to 0.5. The results are robust to
temperature change (see Table SI.4 for results with other temperatures).
Context Window Length. We perform robustness checks regarding the size of the context window.
Weusethelargecontextwindowmodelgpt-4.1-miniandcontextwindowsA ∈ {50,100}(seeSectionB.4).
Sampling Strategies. We perform robustness checks with two policies for generating the alternative
sets A : (i) uniform sampling and (ii) sampling based on a recommendation system based on logistic
t
regression.
Prompt Sensitivity. We perform prompt sensitivity experiments based on the different contexts and
the type of experiment: (i) decisions in real-world networks with real-world data, where we use Algo-
rithm SI.2, (ii) survey data, where we use Algorithm SI.3. Our findings are robust to different prompts.
8

Algorithm SI.3 Prompt used to implement the survey. When the context ω is a social network the
profile textvariableissettobe’You are an undergraduate student at a university. You are
looking for friends to connect with on a social network.’. When the context is the company
networktheprofile textvariableissetto’You are an employee at a company. You are looking
for colleagues to connect with on a company network.’
# Task
Your task is to select a set of people to be friends with.
# Profile
{profile_text}
# Candidate Profiles
The candidate profiles to be friends with are given below after chevrons:
<PROFILES>F(A )</PROFILES>
i,ω
# Output
The output should be as a JSON object with the following structure
{{
"name" : name of the person you selected (integer format),
"reason" : reason for selecting the person,
"ranking_degree" : ranking of how much you based your decision on the degree of
the person (1 = most important, 2 = average important, 3 = least important),
"ranking_similarity" : ranking of how much you based your decision on the
similarity of the person (1 = most important, 2 = average important, 3 = least
important),
"ranking_common_friends" : ranking of how much you based your decision on the
number of common friends with the person (1 = most important, 2 = average
important, 3 = least important)
}}
# Notes
* The output must be a single JSON object ranked in the order of preference.
* You can make at most 1 selection.
* Your output must be contained within the json markdown cue.
* Rankings must be mutually exclusive, i.e. you cannot have the same ranking for two
different attributes.
9

A.5 Data and Code Availability
Data and code are openly available on GitHub at the following link:
https://github.com/papachristoumarios/llm-network-formation
The real-world social network data have been taken from the sources of [56] and [61].
10

B Real-World Datasets
B.1 Statistics of Real-World Datasets
Figure SI.1: Distributions of real-world datasets analyzed in our study, including degree, clustering coefficients, and the
assortativities of the attributes included in the datasets.
11

B.2 Robustness of Results to Sampling Strategies
B.2.1 Recommendation System Parameters
Constant Similarity CommonNeighbors Jaccard Adamic-Adar PAScore AUCScore
Caltech36 -2.9861∗∗∗ 0.5103∗∗∗ -0.9384∗∗∗ 9.9513∗∗∗ 4.9751∗∗∗ -4.28×10−5∗∗∗ 95.2
Swarthmore42 -3.0713∗∗∗ 0.3323∗∗∗ -0.8603∗∗∗ 29.0475∗∗∗ 4.5827∗∗∗ -4.596×10−6 94.8
UChicago30 -3.1467∗∗∗ 0.5493∗∗∗ -1.5431∗∗∗ 59.5934∗∗∗ 8.3355∗∗∗ 3.575×10−5∗∗∗ 97.05
Andorra -2.1337∗∗∗ 0.2247∗∗∗ -2.0713∗∗∗ 96.1618∗∗∗ 13.2652∗∗∗ 3.00×10−4∗∗∗ 92.4
MobileD -4.6000∗∗∗ 0.4075∗ -1.9072∗∗∗ 24.7593∗∗ 14.6024∗∗∗ -0.0058∗∗∗ 98.9
Note ∗:P <0.05, ∗∗:P <0.01, ∗∗∗:P <0.001
Table SI.1: Recommendation System Parameters.
TableSI.1showstheeffectsandtheAUCscorefortherecommendersystembasedonlogisticregression
(cf. Section A.3.3).
12

B.2.2 Change in Graph Statistics due to Different Sampling Strategies
Across all datasets and models, the Kolmogorov–Smirnov statistics indicate that adding a small fraction
of new edges (≤ 5%) produces only minor shifts in the degree distribution, spectrum, and sizes of con-
nected components, with most p-values far above the 0.05 threshold. Significant changes arise primarily
in the local clustering coefficient—particularly under the Uniform strategy—suggesting localized struc-
tural effects without major disruption to global network properties. In contrast, the Recommendation
System strategy yields even fewer significant differences, with most metrics remaining statistically indis-
tinguishable from the original graphs. These results indicate that, at this perturbation scale, LLM-driven
edge additions preserve the overall network structure, with strategy choice influencing the extent of local
structural change.
Name Model Degrees(KS) P-value SizesofCCs(KS) P-value Spectrum(KS) P-value LCC(KS) P-value %NewEdges
Uniform
Caltech36 GPT-4Mini 0.05 0.3 0.1 1 0.06 0.2 0.04 0.6 5
Swarthmore42 GPT-4Mini 0.02 0.8 0.2 1 0.02 1 0.02 1 3
UChicago30 GPT-4Mini 0.02 0.3 0.06 1 0.02 0.2 0.006 1 1
Caltech36 GPT-3.5 0.06 0.1 0.5 0.6 0.07 0.04 0.1 0.0005 5
Swarthmore42 GPT-3.5 0.02 0.8 0.4 0.5 0.02 0.9 0.07 0.0008 3
UChicago30 GPT-3.5 0.02 0.2 0.1 1 0.02 0.1 0.03 0.003 1
Caltech36 LLAMA-3 0.06 0.1 0.08 1 0.07 0.04 0.02 1 5
Swarthmore42 LLAMA-3 0.02 0.9 0.09 1 0.02 0.9 0.02 1 3
UChicago30 LLAMA-3 0.02 0.2 0.02 1 0.02 0.07 0.007 1 1
Caltech36 Claude3.5 0.05 0.3 0.1 1 0.05 0.2 0.03 0.9 5
Swarthmore42 Claude3.5 0.02 0.9 0.3 0.9 0.01 1 0.02 0.9 3
UChicago30 Claude3.5 0.02 0.2 0.2 0.3 0.02 0.2 0.01 0.9 1
Andorra GPT-4Mini 0.002 1 0 1 0.1 1 0.001 1 0.2
MobileD GPT-4Mini 0.03 0.3 0 1 0.08 3e-06 0.06 0.002 3
Andorra GPT-3.5 0.002 1 0 1 0.1 1 0.002 1 0.2
MobileD GPT-3.5 0.04 0.06 0 1 0.05 0.02 0.2 6e-29 4
Andorra LLAMA-3 0.002 1 0 1 0.1 1 0.0009 1 0.2
MobileD LLAMA-3 0.04 0.08 0 1 0.09 8e-07 0.04 0.06 4
Andorra Claude3.5 0.002 1 0 1 0.1 1 0.001 1 0.2
MobileD Claude3.5 0.04 0.04 0 1 0.2 5e-39 0.1 9e-19 4
RecommendationSystem
Caltech36 GPT-4Mini 0.05 0.2 0.1 1 0.06 0.2 0.05 0.2 5
Swarthmore42 GPT-4Mini 0.02 0.9 0.1 1 0.02 0.9 0.04 0.1 2
UChicago30 GPT-4Mini 0.01 0.6 0.3 0.03 0.01 0.7 0.02 0.4 0.7
Caltech36 GPT-3.5 0.05 0.2 0.5 0.6 0.06 0.1 0.07 0.03 5
Swarthmore42 GPT-3.5 0.02 0.8 0.3 0.9 0.02 1 0.07 0.0005 3
UChicago30 GPT-3.5 0.01 0.5 0.5 0.002 0.01 0.6 0.02 0.08 0.9
Caltech36 LLAMA-3 0.06 0.2 0.1 1 0.07 0.06 0.03 0.9 5
Swarthmore42 LLAMA-3 0.01 1 0.2 1 0.01 1 0.02 1 1
UChicago30 LLAMA-3 0.006 1 0.2 0.4 0.007 1 0.005 1 0.3
Caltech36 Claude3.5 0.05 0.2 0.2 1 0.04 0.4 0.08 0.02 5
Swarthmore42 Claude3.5 0.01 1 0.2 1 0.008 1 0.05 0.02 2
UChicago30 Claude3.5 0.006 1 0.4 0.02 0.006 1 0.01 0.6 0.5
Andorra GPT-4Mini 0.002 1 0 1 0.1 1 0.003 1 0.1
MobileD GPT-4Mini 0.03 0.6 0 1 0.07 0.0003 0.08 2e-05 2
Andorra GPT-3.5 0.002 1 0 1 0.1 1 0.004 0.9 0.2
MobileD GPT-3.5 0.05 0.01 0 1 0.04 0.08 0.07 0.0004 4
Andorra LLAMA-3 0.002 1 0 1 0.1 1 0.003 1 0.2
MobileD LLAMA-3 0.04 0.05 0 1 0.07 6e-05 0.08 9e-06 4
Andorra Claude3.5 0.002 1 0 1 0.1 1 0.005 0.7 0.2
MobileD Claude3.5 0.04 0.06 0 1 0.1 2e-17 0.1 6e-14 4
Table SI.2: Change in Graph Statistics for the experiments of Table 1. We report the KS statistic and the
P-valuesforthefollowingquantities(see[31]formoreinformationonthestatistics): (i)degreedistribution,(ii)distribution
of the sizes of strongly connected components, (iii) adjacency matrix spectrum, (iv) local clustering coefficient. The last
column reports the percentage of new edges added. Adding ≤ 5% of edges based on LLM decisions leaves global graph
properties largely unchanged, with only occasional local clustering increases—more frequent under the Uniform strategy
than the Recommendation System.
13

B.2.3 Average Marginal Effects
In Table SI.3 we report the average marginal effects (AMEs) per feature for the experiments of Table 1.
Our analysis reveals that LLM-driven edge formation is consistently shaped by preferential attachment
and homophily, with homophily often exhibiting the largest marginal effects – frequently exceeding 1.0
and reaching above 2.5 under the Recommendation System strategy. Preferential attachment is positive
across all datasets and models, indicating a systematic tendency to link to high-degree nodes. Triadic
closure effects are more variable, sometimes reinforcing local clustering and sometimes favoring cross-
community connections, particularly under the Recommendation System. Compared to Uniform edge
additions, the Recommendation System generally amplifies both preferential attachment and homophily,
suggesting that recommendation-driven link formation intensifies these social-network-like biases.
θˆ
PA
θˆ
H
θˆ
TC
Algorithm Uniform RecSys Uniform RecSys Uniform RecSys
Name Model
Caltech36 Claude3.5 0.39***(0.00) 0.57***(0.00) 0.47***(0.01) 1.62***(0.01) 0.47***(0.01) 0.18***(0.01)
GPT-3.5 0.18***(0.00) 0.14***(0.00) 0.61***(0.00) 0.07***(0.01) -0.05***(0.01) -0.56***(0.01)
GPT-4Mini 0.21***(0.00) 0.17***(0.00) 1.30***(0.02) 1.85***(0.00) 0.27***(0.01) 0.27***(0.00)
LLAMA-3 0.11***(0.00) 0.10***(0.00) 0.96***(0.01) 1.82***(0.01) 0.33***(0.00) 0.30***(0.01)
Swarthmore42 Claude3.5 0.29***(0.00) 1.07***(0.00) 0.60***(0.01) 1.03***(0.01) 0.44***(0.00) 0.80***(0.01)
GPT-3.5 0.18***(0.01) 0.13***(0.00) 0.44***(0.01) 0.10***(0.00) 0.00(0.01) -0.08***(0.00)
GPT-4Mini 0.12***(0.00) 0.23***(0.01) 1.01***(0.01) 2.03***(0.01) 0.26***(0.00) 0.31***(0.00)
LLAMA-3 0.17***(0.00) 0.05***(0.00) 0.99***(0.00) 1.52***(0.01) 0.26***(0.00) 0.69***(0.01)
Uchicago30 Claude3.5 0.35***(0.00) 0.66***(0.00) 0.64***(0.00) 1.47***(0.00) 0.32***(0.00) 0.15***(0.00)
GPT-3.5 0.21***(0.00) 0.13***(0.00) 0.45***(0.00) -0.08***(0.01) -0.02***(0.00) 0.17***(0.01)
GPT-4Mini 0.13***(0.00) 0.27***(0.00) 1.03***(0.01) 2.82***(0.01) 0.24***(0.00) -0.60***(0.00)
LLAMA-3 0.21***(0.00) 0.19***(0.00) 1.27***(0.01) 1.97***(0.01) 0.16***(0.00) 0.37***(0.01)
MobileD Claude3.5 0.43***(0.01) 1.39***(0.01) -1.47***(0.01) -0.66***(0.00) 0.68***(0.00) 0.12***(0.01)
GPT-3.5 0.83***(0.00) 1.30***(0.00) -0.74***(0.01) -0.27***(0.01) -0.02***(0.00) -0.70***(0.01)
GPT-4Mini 0.89***(0.01) 2.06***(0.01) -0.55***(0.01) -0.32***(0.01) 0.56***(0.01) 0.44***(0.01)
LLAMA-3 0.66***(0.00) 1.02***(0.01) 0.23***(0.01) 0.75***(0.01) 0.45***(0.00) 0.26***(0.00)
Andorra Claude3.5 0.40***(0.00) 0.30***(0.00) 1.45***(0.01) 1.40***(0.01) -0.11***(0.00) -0.32***(0.00)
GPT-3.5 0.43***(0.00) 0.25***(0.02) 0.17***(0.01) -0.06***(0.01) -0.19***(0.00) -0.35***(0.01)
GPT-4Mini 0.31***(0.00) 0.08***(0.00) 2.00***(0.03) 2.54***(0.01) -0.05***(0.01) -0.45***(0.00)
LLAMA-3 0.19***(0.00) 0.33***(0.00) 1.92***(0.01) 2.24***(0.01) -0.02*(0.01) -0.08***(0.00)
Note: *: P <0.05,**: P <0.01,***: P <0.001
Table SI.3: AMEs for the discrete choice models of Table 1.
14

B.3 Robustness of Results to Temperature
B.3.1 Regression Coefficients
In Table SI.4, we report the regression coefficient for the regression in the real-world network data for
all temperatures and GPT-4 (gpt-4-1106-preview). The first column corresponds to the temperature, the
next three columns correspond to the fitted coefficients from the regression model of Section 1.C (also
shown in Figure 5) accompanied by the standard errors (in parentheses) and the P-values indicated by
stars (the null hypothesis corresponds to the parameters being set to 0). Next, LL corresponds to the
log-likelihood of the fitted model, and AIC corresponds to the Akaike Information Criterion. Finally,
we report the percent change in the accuracy compared to random guessing, the percent change in the
average path length (as a measure of the small-world phenomenon), and the clustering coefficient (as a
measure of the small-world phenomenon and the triadic closure), as well as the t-statistic for the change
in modularity (Q) between the ground truth network dataset (before the edge deletions) and the network
after the network formation process.
We observe that θˆ > θˆ > θˆ > 0 accross all settings. LLM agents do better than random
H TC PA
guessing, reinforce the small-world phenomenon, and weaken the triadic closure, though the changes are
very small, 0-1% change for the average path length and up to 10% change for the clustering coefficient.
Finally, the community structure is strengthened after new links are formed.
Temp. θˆ PA θˆ H θˆ TC LL AIC %Change %Change %Change ∆Q(t-stat)
Acc. L C
Caltech36(769nodes,33,312edges)
0.5 0.41***(0.01) 1.95***(0.02) 0.59***(0.01) -1,377.47 2,762.94 171.8 -0.008 -9.94 3.45**
1.0 0.36***(0.005) 1.85***(0.02) 0.58***(0.01) -1,435.07 2,878.13 179.6 -0.18 -11.08 3.49**
1.5 0.36***(0.006) 1.72***(0.01) 0.55***(0.007) -1,522.47 3,052.94 127.6 -0.06 -11.46 3.37**
Swarthmore42(1,659nodes,12,2100edges)
0.5 0.18***(0.003) 1.62***(0.006) 0.65***(0.002) -2,838.33 5,684.66 124.2 0.01 -11.46 7.42***
11.0 0.26***(0.002) 1.70***(0.008) 0.58***(0.003) -2,927.99 5,863.97 91.6 -0.10 -4.25 1.96*
1.5 0.19***(0.004) 1.50***(0.008) 0.59***(0.002) -3,139.42 6,286.83 87.39 -0.20 -4.52 4.03***
UChicago30(6,591nodes,416,206edges)
0.5 0.23***(0.001) 2.00***(0.005) 0.41***(0.002) -3,444.33 6,896.67 217.2 -0.24 -2.52 7.46***[0.34]
1.0 0.23***(0.002) 1.98***(0.004) 0.38***(0.001) -3,578.18 7,164.36 219.2 -0.12 -2.66 9.56***[1.05]
1.5 0.22***(0.004) 1.78***(0.008) 0.41***(0.002) -2,033.49 4,074.98 222.4 -0.17 -2.42 10.19***[0.24]
Notes θˆ PA=Coefficientoflogdegree,θˆ H=Coefficientoflog#ofcommonattributes,θˆ TC=Coefficientoflog#commonneighbors
LL=Log-likelihood,AIC=AkaikeInformationCriterion
Acc. =Accuracy,L=AveragePathLength,C=AverageClusteringCoefficient,∆Q(t-stat)=Modularitychanget-statistic
∗:P <0.05, ∗∗:P <0.01, ∗∗∗:P <0.001
TableSI.4: MultinomiallogitcoefficientsforthreenetworksfromtheFacebook100datasetandGPT-4(gpt-4-1106-preview).
Thestandarderrorsoftheestimatesareshowninparentheses. Thenullhypothesiscorrespondstotherespectiveparameter
beingequalto0. Wereportthepercentchangeinaccuracy,averagepathlength,andaverageclusteringcoefficientcompared
to the initial network (before the deletion of edges). For the change in modularity, we run the Louvain algorithm ten times
and perform a t-test with the resulting modularities. For the UChicago30 dataset, we report the t-statistic value in the
subgraph induced by the 2,000 sampled nodes, since the newly added edges would have a very small effect on the change in
the community structure if we were to measure it in the whole network. We also report the modularity change (t-statistic)
of the whole graph inside brackets.
15

B.3.2 Change in Graph Statistics due to Different Temperatures
Further, to measure the changes in the network statistics, we use the metrics presented in [31] to quantify
the changes. Specifically, we measure the Kolmogorov-Smirnov statistic and the corresponding P-value
for the degree distribution, the distribution of the sizes of the connected components, the distribution
of the singular values of the adjacency matrix, and the distribution of the local clustering coefficient,
(CC) for the real-world Facebook100 networks and the gpt-4-1106-preview model (the results are similar
for the other networks and models we examined). Except the changes on the distribution of the sizes
of the connected components for UChicago30, we find that most KS statistics are negligible and the
corresponding P-values are large (e.g. P ≫ 0.5), indicating that most network statistics are not affected.
Table SI.5 summarizes the results:
Name Temp Degrees(KS) (P-value) SizesofCCs(KS) (P-value) Spectrum(KS) (P-value) LocalCC(KS) (P-value)
Caltech36 0.5 0.0481 0.336 0.125 0.999 0.0546 0.202 0.0234 0.984
1.0 0.0481 0.336 0.176 0.926 0.0559 0.181 0.0325 0.811
1.5 0.0481 0.336 0.111 1 0.0559 0.181 0.0351 0.731
Swarthmore42 0.5 0.0229 0.777 0.2 0.987 0.0151 0.992 0.0127 0.999
1.0 0.0217 0.83 0.2 0.987 0.0133 0.999 0.0133 0.999
1.5 0.0211 0.854 0.2 0.987 0.0157 0.987 0.0175 0.962
UChicago30 0.5 0.00228 1 0.81 3.4e-08(***) 0.00303 1 0.0188 0.194
1.0 0.00228 1 0.805 4.62e-08(***) 0.00288 1 0.0184 0.217
1.5 0.00789(***) 0.986 0.873 3.86e-11(***) 0.00819 0.98 0.0188 0.194
Table SI.5: ChangeingraphstatisticsfortheGPT-4model(gpt-4-1106-preview)andtheFacebook100databythemetrics
outlined in [31]. The results for the other datasets, models, and temperatures are similar. (***) denotes P <0.001.
16

B.4 Robustness of Results to Large Context Windows
We perform experiments with the large-context model gpt-4.1-mini. We set the temperature to 0.5. Ta-
bleSI.6showstheeffectsizes. Weobservethatforsocialnetworks(Caltech36,Swarthmore42,UChicago30)
homophily still remains the dominant force for large context windows and that in most cases θˆ > θˆ >
H TC
θˆ > 0, agreeing with the results of Table 1. Additionally, for the MobileD network we observe het-
PA
erophily (θˆ < 0). On the other hand, we observe that for the Andorra dataset, for larger contexts,
H
the triadic closure has a positive effect (θˆ > 0; P < 0.001) compared to negative weight in Table 1
TC
(P < 0.001).
Dataset PreferentialAttachment(θˆ PA) Homophily(θˆ H) TriadicClosure(θˆ TC) LogLikelihood AIC
A=50
Caltech36 0.30***(0.002) 2.74***(0.01) 0.25***(0.006) -2,080.91 4,169.83
Swarthmore42 0.17***(0.002) 2.23***(0.004) 0.40***(0.002) -2,708.70 5,425.41
UChicago30 0.16***(0.004) 2.04***(0.005) 0.49***(0.002) -2,553.28 5,114.57
Andorra 0.27***(0.01) 6.32***(0.02) 0.30***(0.01) -1,762.45 3,532.89
MobileD 0.27**(0.005) -0.84***(0.02) 1.53***(0.002) -2,359.88 4,727.77
A=100
Caltech36 0.35***(0.003) 3.23***(0.02) 0.26***(0.002) -2,450.46 4,908.91
Swarthmore42 0.15**(0.005) 2.51***(0.004) 0.33***(0.002) -3,522.14 7,052.27
UChicago30 0.16***(0.003) 2.66***(0.004) 0.40***(0.003) -3,100.58 6,209.16
Andorra 0.23***(0.006) 6.72***(0.04) 0.56***(0.002) -1,838.66 3,685.33
MobileD 0.32***(0.004) -0.23(0.008) 1.58***(0.004) -2,848.65 5,705.30
Note: *: P <0.05,**: P <0.01,***: P <0.001
Table SI.6: Robustness of results to large contexts. Experiments have been performed with gpt-4.1-mini with context
windows A∈{50,100}. The temperature has been set to 0.5.
17

C Network Evolution and Omitted Simulations
HerewedepicttheevolutionofthenetworksgeneratedbytheLLMagents, aswellasomittedsimulations.
C.1 Principle 1: Preferential Attachment
Network Evolution
We plot the evolution of the LLM-based preferential attachment networks at three timesteps, together
with the degree distribution alongside the degree distribution of a BA graph with the same number of
nodes. We observe that for the temperature being 0.5 we have a core-periphery-like formation which
diverges from the BA model, whereas for the temperature being 1.5 the network has the same degree
distribution as the BA model.
Figure SI.2: Dynamic evolution of networks created based on Principle 1.
Simulations with Degree Information
In Figure SI.3 we provide the results with degree-information only. We observe that the agents form
connections around high-degree nodes only (see Figure SI.3). The same result (star-like networks) holds
for the other LLM models and temperatures.
C.2 Principle 2: Triadic Closure
Network Evolution
We plot the evolution of the LLM-generated networks based on the triadic closure principle, together
with the transitivity measure and the algebraic connectivity (which corresponds to the second-smallest
18

FigureSI.3: ResultsforPrinciple1(preferentialattachment): Wedisplaysimulatednetworkscomprising200nodes
acrossdifferenttemperatures. Forthedegree-basedsimulations,nodedegreedata{d :j ∈V }wasprovided(V corresponds
j,t t t
to the vertex set of the network G at round t). With degree information only, the networks form more unrealistic star-like
t
structures, diverging from scale-free configurations and more closely mirroring a core-periphery network structure.
eigenvalue of the graph Laplacian). We observe that the algebraic connectivity gradually increases as
new edges between the clusters are created. Specifically, the algebraic connectivity reaches a higher value
for higher temperatures, indicating the more frequent creation of new intra-cluster edges. Moreover, we
observe that the transitivity initially increases and then decreases until it reaches its final value.
Figure SI.4: Dynamic evolution of networks created based on Principle 2.
Simulations with the Number of Common Neighbors
Instead of giving the neighborhood information, the simulations presented in Figure SI.5 use the number
of common neighbors. We observe behavior similar to Figure 2.
19

Figure SI.5: Results for Principle 2 (triadic closure). The figure shows the same networks as in Figure 2 with the
only change that instead of the intersection of neighborhoods between the query node and each alternative, we provide the
number of common neighbors (i.e., the size of the intersection) between the query node and each alternative. Similarly, we
observe that the probability of forming an edge within the same community and the marginal transitivity, which indicate
triadic closure, is significantly larger than randomly creating links (P < 0.001, t-test). The error bars correspond to 95%
confidence intervals.
C.3 Principle 5: Small-World Phenomenon
Figure SI.6 shows LLM-generated small-world networks for β ∈ {0.25,0.5,0.75} and compares them with
the Watts-Strogatz networks with the same parameters.
(a) β =0.25
(b) β =0.5
(c) β =0.75
Figure SI.6: Simulation results for Principle 5 (small world). Networkinstancesforthenetworkscreatedaccording
to Principle 5 using the altered Watts-Strogatz Model for node count n = 50, average degree k = 5, rewriting probability
β ∈{0.25,0.5,0.75},togetherwithplotsoftheaverage clustering coefficientC andtheaverage shortest path length
L. The comparison is made with respect to a Watts-Strogatz graph with n = 50,k = 5,β ∈ {0.25,0.5,0.75}. The error
bars correspond to 95% confidence intervals. The results are compared against the Watts-Strogatz model with the same
parameters k and β as a null model. The t-test comparing L and C for the LLM-generated networks and Watts-Strogatz
networks yields P >0.05 (Bonferroni correction for two tests).
20

D Chain-of-Thought Experiments
We experiment with Chain-of-Thought (CoT) reasoning [60]. To induce CoT reasoning we ask the
LLM agents to output the reason and then their choice (i.e. by reversing the order of reason and name
in Algorithm SI.2). The resulting prompt can be found at Algorithm SI.4. In the following figures, we
show the results from the same experiments as the ones we of the main text with the different that CoT
is used.
(a) Probability of connecting to top-k nodes for different models, temper-
atures, and environments
(b) Power law fits (γˆ) and standard errors for different models, tempera-
tures, and environments
Figure SI.7: Results for Principle 1 with CoT reasoning (preferential attachment) The multi-LLM setup was
given neighborhood information {N : j ∈ V }. Top: Probability of connecting to top-k-degree nodes for varying model
j,t t
(temperatureisfixedto1.0andenvironmenttobaseline),temperature(modelfixedtoGPT-3.5andenvironmenttobaseline)
andenvironment(modelfixedtoGPT-3.5andenvironmenttemperatureto1.5)fornetworksgeneratedaccordingtoPrinciple
1withn=200nodes. Bottom: PowerLawexponentsandstandarderrorsforvaryingmodel,temperature,andenvironment.
21

(a) Probability of connecting to top-k for different models, temperatures, and envi-
ronments
(b) Marginal transitivity (D) and probability of an edge within a community (pˆ) for
different models, temperatures, and environments
Figure SI.8: Results for Principle 2 with CoT reasoning (triadic closure). Top: Probability of connecting to
top-k nodes (in terms of common neighbors) for varying model (temperature is fixed to 1.0 and environment to baseline),
temperature (model fixed to GPT-4 Mini and environment to baseline) and environment (model fixed to GPT-4 Mini and
environment temperature to 0.5) for networks generated according to Principle 2 (n = 50, 10 simulations for each model,
environment and temperature). Bottom: Marginal transitivity (D) and probability of an edge within a community (pˆ) for
networks generated according to Principle 2 in different models, temperatures, and environments.
22

Algorithm SI.4 Example prompt regarding social network data with Chain-of-Thought reasoning. Note
that compared to Algorithm SI.1 the order of the fields name and reason in the output format is reversed.
# Task
You are located in a school. Your task is to select a set of people to be friends
with.
# Profile
Your profile is given below after chevrons:
<PROFILE>
{
"name" : "Person 0",
"favorite subject" : "Chemistry",
"neighbors" : ["Person 3", "Person 432", "Person 4", "Person 3", "Person
32"]
}
</PROFILE>
# Candidate Profiles
The candidate profiles to be friends with are given below after chevrons:
<PROFILES>
[
{
"name" : "Person 1",
"favorite subject" : "Mathematics",
"neighbors" : ["Person 3", "Person 4", "Person 23", "Person 65"]
},
{
"name" : "Person 33",
"favorite subject" : "History",
"neighbors" : ["Person 342", "Person 2", "Person 12"]
}, ...
]
</PROFILES>
# Output
The output should be given a list of JSON objects with the following structure
[
{{
"reason" : reason for selecting the person,
"name" : name of the person you selected
}}, ...
]
# Notes
- The output must be a list of JSON objects ranked in the order of preference.
- You can make at most 1 selection.
23

(a) Assortativity and Louvain Modularity with different LLM models and environments
Figure SI.9: Results for Principle 3 (Homophily) and Principle 4 (Community structure due to homophily)
withCoTreasoning. Top: AssortativitiesandLouvainmodularityaccordingtoPrinciple3(n=50,5simulationsforeach
row) in different environments (school, work, community) using different models. The statistical significance is P <0.0003
for all t-tests (comparing with 0, Bonferroni correction for three tests).
(a) Regressionplotfordifferentmodelsandenvironmentsforβ =0.25and
k=5.
Figure SI.10: Fitted results for Principle 5 with CoT reasoning (small world). Regression plot for the relation
L ∼ log(n) for different LLM models for β = 0.25 and k = 5. The legend shows the effect size (a) and the P-value. (*:
P <0.0025; **: P <0.005, and ***: P <0.0005, Bonferroni correction for two tests).
24
