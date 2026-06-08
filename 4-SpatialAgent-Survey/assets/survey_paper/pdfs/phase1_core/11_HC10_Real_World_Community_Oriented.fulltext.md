Title: Real world community oriented high-definition social simulation: Combining reinforcement learning and large language models

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/phase1_core/11_HC10_Real_World_Community_Oriented.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:56:43+00:00
- page_count: 16
- status: ok
- text_char_count: 82873

Metadata:
- author: Peng Lu
- doi: 10.1016/j.cities.2025.106468
- keywords: Artificial generative intelligence, Large language model, Social simulation, Reinforcement learning, Machine learning, Dual rewards
- subject: Cities, 168 (2026) 106468. doi:10.1016/j.cities.2025.106468

Outline:
- Real world community oriented high-definition social simulation: Combining reinforcement learning and large language models (page 1)
  - 1 Introduction (page 1)
  - 2 Results (page 3)
    - 2.1 Real data to align with (page 3)
    - 2.2 Statistical consistency in the week scale (page 3)
    - 2.3 Statistical consistency in the daily scale (page 3)
    - 2.4 Inner consistency for two datasets (page 4)
    - 2.5 Performance evaluation metrics (page 5)
    - 2.6 Matched sleep patterns for weekdays and weekends (page 6)
    - 2.7 Simulations supported by social common senses (page 7)
  - 3 Discussion (page 9)
  - 4 Materials and methods (page 10)
    - 4.1 Constructing high-definition virtual community (page 10)
    - 4.2 Generative modeling of AI agents (page 10)
    - 4.3 Reinforcement learning algorithm (page 11)
    - 4.4 The application and improvement of LLM (page 12)
    - 4.5 The combined framework of RL and LLM (page 13)
    - 4.6 Observations of agents and actions (page 14)
    - 4.7 Comprehensive design of rewards (page 15)
    - 4.8 Computing resource used for training and simulation (page 15)
    - 4.9 Training and validating procedure (page 15)
  - CRediT authorship contribution statement (page 16)
  - Code availability (page 16)
  - Declaration of competing interest (page 16)
  - Acknowledgement (page 16)
  - Data availability (page 16)
  - References (page 16)

Markdown Content:

Cities 168 (2026) 106468
Contents lists available at ScienceDirect
Cities
journal homepage: www.elsevier.com/locate/cities
Real world community oriented high-definition social simulation:
Combining reinforcement learning and large language models
Peng Lua,b,c, Mengdi Lia,c, Yuhao Keb,c,*, Siyang Liaoc,*
aSchool of Public Administration, Central South University, China
bSchool of Automation, Central South University, China
cPeking University Wuhan Institution for Artificial Intelligence, China
A R T I C L E I N F O A B S T R A C T
Keywords: Current social simulation approaches face critical limitations in terms of the scale of agents, environmental
Artificial generative intelligence complexity, and behavioral reliability. This study presents a novel framework combining reinforcement learning
Large language model (RL) and large language models (LLM) to simulate community-level social dynamics with a large scale and the
Social simulation
fidelity. We construct a high-definition virtual replica of Yisheng Garden Community (in Unreal Engine),
Reinforcement learning
populated with 3000 AI agents representing diverse demographic profiles derived from real community data.
Machine learning
Dual rewards Our dual-reward system integrates micro-level LLM evaluations of individual behavioral appropriateness with
macro-level statistical alignment to real smartphone usage patterns. The trained agents demonstrate remarkable
behavioral consistency with real residents across multiple validation metrics: smartphone usage patterns achieve
over 90 % correlation with real data throughout a week-long simulation, sleep patterns align with established
research findings across different demographic groups, and daily activity distributions well reflect authentic
social norms. Time-series analysis using Seasonal Auto Regressive Integrated Moving Average (SARIMA) models
confirms internal consistency between simulated and real behavioral data. This framework has well addressed
the problems about the agent scale limitation, environmental simplicity, and algorithmic bias that constrain
existing approaches. Our validated framework establishes a foundation for city-scale social simulation and
evidence-based social policy testing in virtual environments.
1. Introduction can exchange information about daily life and the environment through
encounters and random dialogue. In this way, AI agents can recognize
Real world social experiment is one of the most challenging area in the current environment and decide what to do next. In addition, AI
computational social science. Traditional empirical studies face ethical agents can also introspect, form new insights and make long-term plans
constraints, resource limitations, and the impossibility of controlled (Park et al., 2023). This work has primarily shown the potential of using
experimentation on real-world communities (Dunn et al., 2012). AI agents to simulate social interaction. Other than the AI town, there
Generative AI agent is emerging as a critical methodology for social also exist many other related researches. Zhao et al. designed the Lyfe
experiment and policy (interventions) test, which enables us to better Agent utilizing the inferencing ability of LLM to simulate the process of
understand emergent social phenomena and social changes, in order to crime solving (Zhao et al., n.d.). Tang et al. proposed GenSim, a platform
achieve better social governance. In this direction, the Stanford Uni- simulating AI agents interacting on-line (Tang et al., 2024). Zheng et al.
versity team created an AI town with the concept and architecture of AI built AI Economist to simulate human economic activities in a simplified
agents on April 13, 2023. They used the large language model (LLM) to environment (Zheng et al., 2021).
generate 25 AI agents, which primarily realizes the simulation of human After that, many studies have attempted to simulate human behavior
behavior with high reliability, thus showing realistic individual and using large language models (Aher et al., 2023; Gao et al., 2023; Park
group behaviors in various interactive applications. These AI agents et al., 2023). However, studies have shown that LLM may have value
have different personalities and can start spontaneous actions in the biases, and it is challenging to ensure each generated behavior meets the
virtual world, including getting up, sleeping, working and playing. They expected standards (Tabone & De Winter, 2023). With the development
* Corresponding authors.
E-mail addresses: 254601004@csu.edu.cn(Y. Ke), liaosiyang@whai.pku.edu.cn(S. Liao).
https://doi.org/10.1016/j.cities.2025.106468
Received 17 January 2025; Received in revised form 23 August 2025; Accepted 6 September 2025
Available online 23 September 2025
0264-2751/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

P. Lu et al. C i t i e s 168 (2026) 106468
of computational social science, RL was more and more used to model decide to combine the RL and LLM to avoid the uncontrollability
and analyze decision-making processes within complex, dynamic envi- of LLM and take advantage of its general inferencing.
ronments (Sutton, 2018). The core components of RL include an agent, a (d) ABM combined with RL þ LLM can be a possible solution.
set of actions, a state space representing the environment, a reward ABM powered by RL and LLM are revolutionizing social simula-
signal, and the decision-making policy that the agent follows (Ding tion. ABM framework based on the RL and LLM has achieved a
et al., 2020). The agent learns to make decisions by acting in an envi- breakthrough, transitioning from simple task execution to com-
ronment to achieve cumulative rewards by RL (Moussaoui & Ben- plex social behavior simulation by integrating the three core
slimane, 2023). By learning a value model and using the rewards components of planning, memory, and tool use. This enables AI
generated by the RL, it can be expected that the agent tend to behave agents to exhibit human-like independent planning, collaborative
more human-like (Al Nahian et al., 2024). However, there exist some interaction, and creative behavior (Park et al., 2025). ABM
problems unsolved in the field of social simulation, and we are trying to powered by RL and LLM architectures successfully integrate
provide possible solutions to them: LLM/RL with ABM to create transformational frameworks for
understanding complex social systems. Through systematic
(a) The scale remains the most obvious barrier. AI Town of development of LLM-augmented social simulations, this archi-
Stanford University has only 25 AI agents, Lyfe Agents only tecture achieves unprecedented capabilities in modeling human
supports simulation of 9 agents and there are only 10 AI Econo- behavior and social dynamics. The integration delivers powerful
mists simulated in the platform of AI Economist. GenSim enables research toolsets that enable more nuanced, realistic, and
a large number of agents but it has no visualizing method and has comprehensive representations of complex systems, revolution-
the simplest virtual environment overall. In a real community, izing how researchers' study and predict social phenomena
people's behaviors and reactions are highly varied, but the through sophisticated computational approaches (Gürcan, 2024).
limited number of agents in AI Town restricts the diversity of For example, ABM with LLM systems have demonstrated the ca-
interactive scenes and modes for AI agents. This makes it quite pabilities in simulating human-like behavior and replicating
difficult to accurately represent real-world communities' complex human prosocial behavior in public goods games across multiple
behaviors (Hutson & Ratican, 2023). This scale mismatch pre- experimental treatments. Beyond reproducing lab results, they
vents researchers from studying the very social processes that predicted responses to novel conditions and exhibited real-world
matter most for real-world applications. In our framework, we “unbounded actions” like collaboration and cheating (Sreedhar
provide simulation of 3000 AI agents which is larger than AI et al., 2025). LLM-powered ABM creates generative agents with
town, Lyfe Agents, and AI Economist. Only GenSim supports human-like cognitive, memory, and decision-making capabilities
more agents than ours with the cost of simplest environment that interact through natural language, enabling accessible and
among all the researches mentioned; interpretable social science research by simulating complex
(b) Environmental authenticity presents the second constraint. public administration scenarios like crisis response without
The AI Town of Stanford University uses simple pixel blocks requiring extensive technical expertise (Xiao et al., 2023). It also
(patches) to model the community environment. Lyfe Agents uses can create large-scale social simulators by constructing human-
the graph engine Utility to build an animated 3d-world. GenSim like agents with cognition, emotions, and needs that interact in
does not have a virtual physical environment and it shows the realistic urban environments, enabling low-cost policy experi-
simulation via a simple web interface. AI Economist constructs a mentation and social phenomenon prediction through digital
two-dimensional grid world for the agents to interact with. The twin societies that can simulate complex behaviors like opinion
built environment influences social interactions, mobility pat- polarization, crisis response, and economic dynamics (Piao et al.,
terns, and daily routines. Without environmental fidelity, 2025).
behavioral realism becomes impossible to achieve or validate
against real-world data. Our framework, on the other hand, Thus, we propose the RL +LLM framework. According to real GIS
construct the virtual environment exactly the same as a real and BIM data of the real community (named Yisheng Garden Commu-
community. We use Unreal Engine to develop the virtual physical nity), we construct a High-Definition 3D virtual community, as the
world so that it can simulate the real interaction of the agents training environment of RL. According to real demographic data of this
with the physical world; community, we have generated 3000 AI agents. We design the obser-
(c) Algorithmic reliability poses the deepest challenge. AI Town vation capability and action spaces, to simulate 3000 AI agents living in
of Stanford, Lyfe Agents, and GenSim all rely on LLM as the main the virtual community. We design a reward system combining both
reasoning engine, while AI Economist solely deploy RL. The macro and micro level to guide action choices of AI agents. The micro-
complete reliance on LLM leads to potential inconsistencies in the level LLM reward is based on instant responses from LLM grading. It
actions across different contexts. It is challenging for LLM to provides the influence of large social laws on each individual AI agent.
ensure the behaviors generated each time meet expected stan- The macro-level statistical reward is based on the comparison between
dards and thus poses the risk of uncontrollability. Meanwhile, real data and simulations. It provides the behavioral pattern of group
standard RL is suitable for tasks in specific fields, like AI Econo- (macro) level. For the real data, we use the smartphone usage data for
mist did with economy, but it is difficult to design the reward 3000 real residents, and the data is updated by each 1/12 h (5 min).
system for a much more general case, like human activities in Once the model is well trained, we generate community simulation of
community. Pure LLM-based approaches suffer from inconsis- one week and evaluate the performance based on comparison with real
tency, potential bias, and uncontrollable outputs that undermine data and social common senses. This study will address these constraints
scientific reproducibility. The complete reliance on language through a novel integration (RL +LLM). By combining the consistency
models leads to potential inconsistencies in actions across of RL optimization with the behavioral sophistication of LLMs, we create
different contexts, making it challenging to ensure behaviors a framework that maintains both scientific rigor and behavioral
meet expected standards. Conversely, traditional RL frameworks authenticity. Our approach scales to community-relevant populations
excel at optimization but struggle with the open-ended nature of while grounding simulations in real demographic data and validating
human social behavior. Neither approach alone can balance the outcomes against empirical behavioral patterns. The framework's
flexibility needed for realistic behavior with the control required effectiveness is demonstrated through simulation of a real community
for scientific analysis. In order to solve the bias of algorithm, we with comprehensive validation against multiple behavioral metrics,
ensuring that our contributions extend beyond algorithmic novelty to
2

P. Lu et al. C i t i e s 168 (2026) 106468
practical utility for researchers, planners, and policymakers who require 2.2. Statistical consistency in the week scale
evidence-based tools for understanding community dynamics at scale
(Table 1). In the one-week simulation, we count the number of people using
Key differentiators emerge from this comparison. While GenSim smartphone inside the virtual community at each time step (t) and then
achieves comparable agent numbers, it sacrifices environmental fidelity compare it with the Real Phone Usage. In our model, we assume the AI
and uses pure LLM control. AI Town and Lyfe Agents provide sophisti- agents use smartphone while they are reading, relaxing, shopping or
cated behavioral modeling but cannot scale beyond dozens of agents. AI exercising. In Fig. 1, the blue line shows the trends of Real Phone Usage
Economist demonstrates RL effectiveness but only in narrow economic while the orange one represents the Simulated Phone Usage as we have
domains. Our framework uniquely combines large-scale capability with defined them in Section 2.1. Both Real Phone Usage and Simulated
environmental realism and algorithmic control, validated against real Phone Usage can well present synthetic periods of one day. Simulated
community data rather than expert judgment. This combination ad- Phone Usage has seven peaks from Monday to Sunday (Monday 92.38
dresses the fundamental limitations that prevent existing approaches %, Tuesday 97.66 %, Wednesday 78.13 %, Thursday 94.53 %, Friday
from supporting policy-relevant social simulation. With this proposed 88.67 %, Saturday 96.48 % and Sunday 91.80 %), which coincides with
framework, we can even achieve the simulation of the whole city by seven peaks around similar times in the trend of Real Phone Usage. We
integrating the simulations of all communities in the city. The results of also compare the timing of peaks between the Real and Simulated Phone
such city simulation are able to advise urban policy and planning, such Usage. As Fig. 1shows, From Monday to Sunday, it reaches the peak at
as traffic planning and garbage recycling. Our framework also supports 21:15, 21:15, 20:20, 21:10, 21:25, 20:45 and 20:40 for Real Phone
multiple fine-tuning methods to be adopted in other cities or countries. Usage, while it also takes the maximum at 22:10, 21:30, 22:10, 22:10,
22:00, 23:00, and 21:40 for the Simulated Phone Usage. The differences
2. Results in peaks' timing are less than 1 h. There are also 7 concaves in the Real
Phone Usage (Monday 6.52 %, Tuesday 6.46 %, Wednesday 6.57 %,
We deploy the trained model and generate the community simula- Thursday 5.62 %, Friday 5.33 %, Saturday 8.25 %, Sunday 8.17 %)
tion of one week (7 days). It suggests that our framework (RL +LLM) can while the Simulated Phone Usage takes its minimum at the similar times
yield outcomes that match real data very well, and the action patterns of (Monday 8.40 %, Tuesday 7.42 %, Wednesday 9.37 %, Thursday 8.40 %,
AI agents are quite close to real residents in this community, in terms of Friday 7.81 %, Saturday 7.23 %, Sunday 10.74 %). Therefore, the
social common sense. overall statistical outcome suggests that the smartphone usage of the
virtual community simulated by the model matches with Real Phone
2.1. Real data to align with Usage well.
In order to verify the effectiveness of our simulation, we need to 2.3. Statistical consistency in the daily scale
compute and compare the similarities between virtual 3D community
and the real one (Stonedahl et al., 2011). The smartphone usage data of Fig. 2shows the trends and basic statistical information of both Real
this community is obtained at group (macro) level, provided by the Phone Usage and Simulated Phone Usage in each day for a week. Sub-
Tencent Company who is one of the biggest Internet Company in China. plots A-G represent the comparison between the Real Phone Usage and
It provides popular mobile applications for Chinese people, such as the Simulated Phone Usage. In these subplots, blue lines represent Real
WeChat, QQ, Tencent Video, and Tencent Meeting. In China, there are Phone Usage, and orange lines represent Simulated Phone Usage.
more than 1.2 billion people using the services and products provided by Table H of Fig. 2shows the mean and SD for Real and Simulated Phone
Tencent Company. Therefore, smartphone usage data from Tencent Usage for each day. Like the observation made in the scale of one week,
Company can largely reflect the real residents. In the rest of this paper, the daily result suggests that the trend of Simulated Phone Usage in each
we define the smartphone usage data gathered from Tencent Company day is also consistent with the daily trend of Real Phone Usage. Fig. 2A
as the dataset of “Real Phone Usage”, and simulated phone usage in the represents the Real and Simulated Phone Usage on Monday. The blue
virtual community as the dataset of “Simulated Phone Usage”. The dif- line represents Real Phone Usage, and it shows that the phone usage
ference between two datasets is a key indicator to evaluate the matching continues to decline (78.55 %–9.65 %) between 0: 00 and 6: 00. After 6:
degree between the 3D virtual and real community behaviors. There also 00, it begins to rise slowly until 8: 00. Then, the usage of smartphones is
exist rich amount of research about the sleep times and durations of overall stabilized and shows a gradual upward trend until 18:00 when it
residents. In this section, we also compare the sleep pattern of AI agents begins to rise rapidly again. Real Phone Usage reaches the peak (100 %)
with real residents. at 21:15 and then declines immediately. The orange line representing
We understand that citizens in other countries present different Simulated Phone Usage shares the exact same pattern as the Real Phone
phone usage habits. For a country where smartphones are not involved Usage through the whole day in the perspective of both critical points
in daily life as much as China, other sources of data would be more and extreme values. The statistical information also shows trivial dif-
appropriate. Nevertheless, our proposed framework supports the ference in each day. The difference in mean value takes its minimum of
replacement of phone usage data with any kind of community-related 0.02 on Saturday and the difference in standard deviation (SD) takes its
data while remaining effective. minimum of 0.002 on Sunday as it shows in Fig. 2H.
Table 1
Systematic comparison with existing approaches.
Approach Agent Scale Environment Algorithm Validation Method
AI Town (Stanford) 25 Pixel-based 2D Pure LLM Qualitative observation
Lyfe Agents 9 3D game engine Pure LLM Expert evaluation
GenSim 1000+ Web interface Pure LLM Limited metrics
AI Economist 10 2D grid world Pure RL Economic indicators
Our Framework 3000 Photorealistic 3D RL þLLM hybrid Multi-level real data
Time Series Validation
Four Levels Similarity Validation
3

P. Lu et al. C i t i e s 168 (2026) 106468
Fig. 1. The trend of Real Phone Usage and Simulated Phone Usage through a whole week. The x-axis coordinates represent time, and the y-axis represents the
proportion of Phone Usages.
Fig. 2. Detail of Real Phone Usage and Simulated Phone Usage for each day in the week with basic statistical information. In subplots A-G, the blue line represents
the percentage in phone usages of Real Phone Usage, and the orange line represent the percentage in phone usages of Simulated Phone Usage. The dotted red lines
indicate the maximum and minimum of Real Phone Usage for each day. H is the table showing the mean and SD for Real and Simulated Phone Usage in each day. (For
interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)
2.4. Inner consistency for two datasets Sunday (validation set).
We have run multiple experiments and found out the optimal pa-
Other than statistical analysis, we also apply machine learning (ML) rameters for both sets, such as (p ¼1, d ¼0, q ¼1) for seasonal parts
to prove (recheck) the well matchiness between Real Phone Usage and and (p ¼1, d ¼0, q ¼1) for non-seasonal part. For Real Phone Usage
Simulated Phone Usage. We use time series analysis to validate the unity data, Fig. 3A shows the target and predicted trend from Friday to Sunday
of trends and periods. Seasonal Auto Regressive Integrated Moving by the SARIMA model, with 95 % confidence interval (CI). The red line
Average (SARIMA) is broadly used model, in the field of broadcasting represents the Real Phone Usage trend. The blue dots are the predicted
features highly related to the time. It is made of two parts, seasonal and values from Friday to Sunday. The shaded band represents the CI range.
non-seasonal, and each part combines differencing with autoregression All predicted points (values) fall into the 95 % CI, and our SARIMA
and a moving average model. For seasonal parameters and non-seasonal model can predict the smartphone usage of real residents, which in-
parameters, we set two sets. In each set, there are three major param- dicates that real data has inner consistency at the week scale.
eters: p stands for the order of the autoregressive part; d stands for the For Simulated Phone Usage, we apply the same SARIMA model with
degree of first differencing involved; q stands for the order of the moving the same parameter values, to check the inner consistency at the same
average part (Sinuany-Stern, 2021). We divide the Real Phone Usage time scale (week). We divide the Simulated Phone Usage into two sets,
dataset into two parts, Monday to Thursday (training set) and Friday to such as the training set (Monday to Thursday) and validation set (Friday
4

P. Lu et al. C i t i e s 168 (2026) 106468
Fig. 3. Validation of matched patterns using the method of time series. Take the data from Monday to Thursday as training set, fit a time series model and use the
data from Friday to Sunday to validate it. The red line indicates the data value from Friday to Sunday, the blue dots represent the predictions, and the shaded area
represents the confidence interval. A shows the result for Real Phone Usage and B shows the result for Simulated Phone Usage. (For interpretation of the references to
color in this figure legend, the reader is referred to the web version of this article.)
to Sunday). Like Fig. 3A, Fig. 3B shows the target trends, predicted value a time-domain signal into its constituent frequency components,
points, and 95 % CI range. Most predicted points are included in the 95 revealing both amplitude and phase information across the frequency
% CI, which indicates that the same SARIMA model can predict simu- spectrum (Bracewell, 1989). In this paper, FT was applied to detect
lated smartphone usage behaviors of AI agents. Therefore, for either timing discrepancies between real and simulated data, leveraging its
Real or Simulated Phone Usage, the validation set can be well predicted ability to decouple overlapping periodic behaviors. We compute the
by the training set. Hence, the outcome of our simulation can largely phase difference between the real and simulated data under two main
reflect the inner consistency of real-world social actions of real residents. frequencies: one-day and half-day. The phase difference is (cid:0) 1.48 h
under the frequency of one day and (cid:0) 0.06 h under the frequency of half
day. If we assume the period of phone usage is one day, then the apex of
2.5. Performance evaluation metrics
simulated phone usage is 1.48 h earlier than the real ones. Likewise, if
we assume the period of phone usage is half a day, then the apex of
In this paper, we bring up 4 metrics to evaluate the performance of
simulated phone usage is only 0.06 h earlier than the real ones.
simulation. In order to evaluate, we smooth the real data simulated data
Kullback-Leibler Divergence (KL-Divergence) is a non-symmetric
by taking the hourly summation and evaluate the performance based on
measure quantifying the difference between two probability distribu-
these smoothed data (Table 2).
tions (Biglieri, 2022). Th(e divergence of distribution P from distribution
Structural image similarity (SSIM) index is one of the most popular ∑
measurements for the similarity between images. It evaluates lumi- Q is computed as DKL P∣|Q) = P(x)log Q P( ( x x ) ). In our research, we
nance, contrast, and structure of two compared images in the set of
normalize the real and simulated data to convert them into the form of
corresponding windows around image pixels (Starovoytov et al., 2020).
distribution. Their value can be then considered as the probability of
In our research, we construct two images – “real image” and “simulated
using mobile phone at a certain timestep. This approach and metric is
image” using smoothed real data and simulated data. We first reshape
suitable for assessing distributional alignment in phone usage data
the smoothed data into arrays with 24 rows and 7 columns representing
because it focuses on relative entropy rather than absolute values. The
24 h and 7 days. We multiply the values inside the arrays by 255 to
value of KL-Divergence of the simulated data from the real data is 0.071.
transform them into standard form of images. Then, we compute the
The range of KL-Divergence is from zero to infinity and value below 0.1
SSIM index for these two images. The value of SSIM index represents the
is an indication of similar distribution in the field of statistics. The value
similarity in absolute value, trends within days and trends through the
0.071 indicates that the simulated data only has minor deviation from
whole week between real and simulated phone usage. The range of SSIM
the real data.
index is between 0 and 1, and our simulation achieved an outstanding
Dynamic Time Warping (DTW) is a robust algorithm designed to
score as 0.79.
measure similarity between two temporal sequences that may vary in
Fourier Transform (FT) is a mathematical operation that decomposes
speed or length, by computing an optimal alignment path that mini-
mizes the cumulative distance between them through nonlinear warping
Table 2 of the time axis (Müller, 2007). The optimal warping path identified in
Summary of the metrics used and their values used for
the analysis of real versus simulated data signifies the sequence of point-
performance evaluation.
to-point matches that minimizes the total cumulative distance between
Metric Value these two temporal sequences. After we compute the optimal wrapping
SSIM 0.79 path, we let the time indices of real data in the point-to-point matches be
Phase Shift (cid:0) 1.48 h/(cid:0) 0.06 h the independent variable (x) and the time indices of simulated data as
KL-Divergence 0.071 dependent variable (y). If the linear equation y =x can fit the point-to-
DTW-R2 0.99
5

P. Lu et al. C i t i e s 168 (2026) 106468
point matches well, we can conclude that these two temporal sequences research, to further verify the effectiveness of our simulation. Fig. 5B & C
are quite similar. We calculate the predicted values using the equation y show the distributions of sleeping duration in a weekday and on
= x and then compute R2. The value of R2 is 0.99, which means the weekends. Fig. 5D & E show the difference in sleep duration distribution
optimal path is very close to the equation y =x, thus indicating the real among different life stage groups. As Fig. 5B shows, 52.78 % of AI agents
data and simulated data are very similar. We visualize the pairs of time sleep 7–10 h at weekday. Researchers conducted questionnaire surveys
indices and the desired regression line with 10 units y-intercept shifted at the Boston Science Museum from February to May 2009, distributing
¨
region in Fig. 4. All the points fall inside the shifted region, which in- 48-question surveys to adult visitors that included the Horne-Ostberg
dicates that all the pairs of time indices have difference less than 10 MEQ, the Pittsburgh Sleep Quality Index (PSQI), the Epworth Sleepiness
units. Scale (ESS), the Munich Chronotype Questionnaire, as well as 12 addi-
Overall, we evaluate the performance of simulation with four tional questions addressing general sleep habits. Results showed most
different metrics. SSIM evaluate the structural similarity between the participants reported approximately 7.55 ± 1.22 h of weekday sleep
real and simulated data, FT enables us to measure the phase shift of (Roepke & Duffy, 2010), which is consistent with our study. Only 22.62
simulated data from real data, KL-Divergence evaluate the simulation by % of them sleeping for more than 10 h during the weekdays. Through
transforming the data into the form of distribution and DTW yields an large-scale cohort studies and objective measurement technologies,
optimal wrapping path that indicates the similarity between real and including wearable devices (such as Fitbit), activity recorders, stan-
simulated data. With all of the four metrics, the simulation of the phone dardized questionnaires, and systematic reviews with meta-analysis,
usage can be evaluated as sound and valid. scientists analyzed 50 million nights of sleep data from 73,513 partici-
pants in the British Biobank study, 38,015 participants in the Swedish
2.6. Matched sleep patterns for weekdays and weekends national cohort study, and more than 220,000 total participants. The
research found that participants slept more than 10 h on weekends,
Fig. 5A shows the number of AI agents sleeping at each timestep which also matches the empirical finding that some people sleeping for
through a weekday. AI agents go to bed and wake up at different timings, more than 10 h (Gallicchio & Kalesan, 2009).
but during the same time interval, which is close to real people. The Existing research indicates that sleep duration shows significant
number of AI agents sleeping starts relatively high at 0:00 and it in- differences between weekdays and weekends. During the weekdays,
creases for approximately 5 h. Then it drops rapidly between 6:00 and people who accumulate considerable sleep debt compensate on week-
8:00, indicating that most AI agents get up during this period. This end by lengthening their sleep by several hours (Roenneberg et al.,
pattern matches social natural norms of real residents. The number stays 2003). Fig. 5C & E represent the sleep pattern of AI agents during the
low during the daytime and begins to increase after 20:00. The gradual weekend. The values of sleep duration in these two subplots stand for the
rising from22:00 to midnight indicates that most people go to bed in this average of Saturday and Sunday. We found that during weekdays,
time interval. The line continues going up smoothly after 0:00, indi- considerable amount of AI agents sleep less than 6 h, and most AI agents
cating some people staying up late at night and therefore, go to bed at (20.24 %) sleep for 8–9 h. However, Fig. 5C indicates no AI agents sleep
various times. less than 6 h, and most of them (26.19 %) sleep for 11–12 h in average
Besides the start time of the sleep, we also investigate the sleep and retired seniors sleep for 6.50 h in average during the weekday. This
duration of AI agents in the same day and compare it with existing sleep pattern differences fit with the previous research that seniors tend
Fig. 4. DWT-R2 and corresponding regression performance. We let the time indices of real data in the point-to-point matches be the independent variable (x) and the
time indices of simulated data as dependent variable (y). We test if the line y =x is an appropriate regression for the data points. The blue dots in this figure represent
the pairs of indices and the pink line represents the regression line y =x. The shaded area represents the shift with 10 units of y intercepts. (For interpretation of the
references to color in this figure legend, the reader is referred to the web version of this article.)
6

P. Lu et al. C i t i e s 168 (2026) 106468
Fig. 5. The sleep patterns for different life stage groups in a weekday and on weekend. Panel A shows the number of AI agents sleeping at each timestep through a
weekday. The x-axis coordinates represent time, and the y-axis represents the number of different people taking each action through a weekday. B and C show the
distributions of sleeping duration in a weekday and on weekends. The x-axis coordinates represent sleep duration, and the y-axis represents the number of people. D
and E shows the difference in sleep duration distribution among different life stage groups. The x-axis coordinates represent sleep duration, and the y-axis represents t
different life stages.
to sleep for less time than students and adults (Hirshkowitz et al., 2015). compare the action patterns of two groups (employed adults and stu-
For the weekend, Fig. 5E shows that unemployed adults and retired dents) by the difference in action curves (working and studying). The
seniors sleep for 4 to 5 h, while the employed adults and students sleep trends of working and studying fit the observations of these actions in
for 8 to 9 h in the simulation. For our simulation of all life stage groups, real community well. These two actions (working and studying) both
AI agents sleep more during weekdays than during weekdays but rise rapidly in the morning, stay unchanged for the daytime, and then
employed adults and students still sleep for more hours than unem- fall in the afternoon. The difference is that the curve for working starts to
ployed adults and retired seniors. This pattern can be explained and can rise earlier than studying, and it declines later than studying. It also
reflect the behaviors of real residents. As employed people and students shows that the curve for working grows and drops more smoothly. In
sleep less on weekdays, they tend to sleep more on the weekends. real society, people's day shifts start at various timings. Some start their
work at 7:00, while some others start at 10:00 (Soldatos et al., 2005).
Respectively, some people's shifts end at 16:00 while some others end at
2.7. Simulations supported by social common senses
20:00. For students, the period of school time is much more regular and
stable. Most of the schools start and end at similar times, therefore
Fig. 6A shows the trend (number) of AI agents doing each activity
students tend to start and end the action of studying at similar times
through a weekday (we take Monday as example). Based on this, we
7

P. Lu et al. C i t i e s 168 (2026) 106468
Fig. 6. Trend of AI agents taking each action through a weekday. The x-axis coordinates represent time, and the y-axis represents the number of people. A shows the
trend for all the AI agents, B shows the trend for employed adults, C shows the trend for students, D shows the trend for retired seniors and E shows the trend for
unemployed adults.
(Kelley et al., 2017). Therefore, the curves of these two simulated ac- trends (numbers) of AI agents (unemployed adults and retired seniors)
tions can largely reflect the social common sense that also affects real taking each action during a weekday. The curve of AI agents (retired
residents. seniors) exercising and the curve of AI agents (unemployed adults)
We then focus on the difference among four typical life stage groups shopping both grow in the morning, reach the peak in the noon, and
to further check whether simulated behaviors of AI agents can be vali- start to drop in the afternoon. The AI agents (retired seniors) start to
dated by social laws and regulations (social common sense). Fig. 6B, C, exercise at different times in the morning, during 6:00 and 12:00. The
D&E represent the trend (number) of AI agents in each Life Stage doing number of AI agents (retired seniors) exercising takes its maximum at
each activity through the same week day. Generally, in the society, 12:00. This maximum stays for an hour and then it keeps decreasing in
students and employed adults leave home for school or work in the the afternoon, indicating that they return home at various times in the
morning and return home in the evening, showing strict regularities in afternoon. This action pattern of AI agents (retired seniors) is consistent
their daytime schedules, which can be reflected by the stable and flat with the real-world retired seniors that they tend to exercise inside the
surface found in the curves of studying and working. However, most community during the daytime.
students would go to a school near home, while most of the employed AI agents of unemployed adults start to go shopping at different
adults have to endure commuting time over 30 min (Koslowsky et al., times in the morning from 10:00 to 12:00. The number of them shopping
2013), which leads to the timing difference in commuting. This pattern takes its maximum at 13:00 and then decreases gradually in the after-
difference can be reflected by comparing the curve slopes of employed noon, indicating they return home at various times. This action pattern
adults in Fig. 6B and students in Fig. 6C. It suggests that the curve slope of AI agents (unemployed adults) is consistent with real-world unem-
of employed adults is much shallower than the students. The steeper ployed adults in this community that they tend to go shopping during
slope for the students indicates that they would spend less commuting the daytime (because they do not have to work). Generally, in real so-
time than employed adults. Hence, the action pattern of AI agents ciety, unemployed adults and retired seniors are free from strict daily
(employed adults and students) can be largely supported by social working schedules and take their actions more casually than students
common sense. The verification from social common sense can be also and employed adults. By our simulation, the curves for trends (numbers)
found in the other two groups. For the retired seniors, existing research of them exercising and shopping have narrow peaks at their maximums,
shows that they tend to exercise inside the community while unem- unlike the stable surfaces presented by the curves of employed adults
ployed adults tend to go shopping during the daytime and they would and students in Fig. 6B & C. This indicates that the AI agents of retired
take these actions casually (Simek et al., 2015). Fig. 6D & E show the seniors and unemployed adults follow less strict daily routine than
8

P. Lu et al. C i t i e s 168 (2026) 106468
students and employed adults, which is consistent with real-world pat- social common sense in China or worldwide.
terns of retired seniors and unemployed adults. Hence, the simulation of
AI agents (retired seniors and unemployed adults) can be largely sup- 3. Discussion
ported by the social common sense.
Fig. 6illustrates the crowd behavior from the perspective of actions, In this paper, we have proposed a combined social simulation
and Fig. 7provides another independent proof source, by investigating framework of AI agents, which has been applied to simulate the social
typical locations of them at various timings for the same weekday as actions of residents in the community level society. We have found that
Figs. 5 & 6. Fig. 7presents the location dynamics (distribution) of AI this framework is effective in community-level social simulation. The
agents through a weekday. The curve of AI agents located at working combined design of dual rewards in both micro-level and macro-level
place has the same shape of AI agents (employed adults) working in has also shown effectiveness for the training process. The macro-level
Fig. 6A. Similarly, the curve of AI agents located at school in Fig. 7A has statistical rewards are gained based on the difference between Real
the same shape of related AI agents (students) studying in Fig. 6A. This and Simulated Phone Usage, and the consistency between two datasets
pattern consistent reflects social common senses that only students can validate the reasonability and effectiveness of macro-level statistical
would go to school and employed adults go to workplaces (In our reward. The micro-level LLM reward is calculated based on the grades of
framework, we mark the school as working place for adults who works LLM. It rates the normality degree of social actions for individual AI
there). The curve of AI agents located at community public area in agents. In other words, the grade of LLM can train them to take appro-
Fig. 7A has the same shape of AI agents (retired seniors) exercising in priate (normal) actions at different times. The matched behavior pat-
Fig. 6D, and the curve of AI agents located at shops in Fig. 7A has the terns between AI agents and real residents suggest that the micro-level
same shape of AI agents (unemployed adults) shopping in Fig. 6E. These LLM reward also largely supports our social simulation. Overall, our
shared patterns can also be supported by social regulations in China that framework adopts mature and robust training methodology (RL) and it
retired seniors would exercise in public area inside the community while has been proven to be valid. It successfully trained a feasible and flexible
the unemployed adults tend to go shopping nearby during the daytime. policy via the comprehensive reward system containing two layers such
Fig. 7B, C & D provide the location distribution of AI agents at three as the macro-level (statistical data) and micro-level (LLM grading).
different timings. At 8:00, most AI agents are still at home, some This social simulation framework yields promising results, and most
(employed adults and students) are already located in their working of them are close to real social system. Simulated Phone Usage (simu-
places or schools, and there is no AI agent located in the community lation results) is consistent with Real Phone Usage (real community level
public area or shops in Fig. 7B. Obviously, this pattern satisfies real- data). The inner consistency between them has also been proved by the
world social common sense in China that, in the morning, most stu- ML method (time series analysis). The sleep patterns of AI agents agree
dents and employed adults would leave home earlier than unemployed with previous social research, for different life stage groups and for
adults or retired seniors. At 14:00, the AI agents are located more evenly different timing (weekdays and weekends). The trends (numbers) of AI
in Fig. 7C. Most AI agents located in working place, which reflects the agents taking each action are well supported by the social common
social fact worldwide that employed adults take the majority proportion senses and the behavioral patterns of the 4 different life stage groups are
in the society. At 19:00, most AI agents are located at home, but there well matched with real residents. The dynamical location distributions
are still some AI agents located at working places in Fig. 7D. This is also of AI agents share same patterns as real resident actions. This consis-
consistent with real social phenomenon in China that some employed tency is also supported by the social laws and regularities in China or
adults would end their shifts later in the night and return home quite worldwide.
later than others. Hence, the location dynamics of AI agents can be In our research, we found general community rules by investigating
largely supported by related social phenomena, social regulations and the action and location history records and all of these records are open
Fig. 7. The dynamical location distribution of AI agents at different timing during a weekday. A shows the overall dynamical location distribution of AI agents. The
x-axis represents time, and the y-axis represents the number of people in different location. B, C and D indicate the location distribution of AI agents in three specific
timings: 8:00, 14:00 and 19:00.
9

P. Lu et al. C i t i e s 168 (2026) 106468
sourced to all scholars. These community rules can be further validated 4. Materials and methods
by scholars from other perspectives using data from other sources. For
example, social organizations may be interested in the action histories of 4.1. Constructing high-definition virtual community
the elders. If they already gathered such data from real elders, our
community rule about elders' action patterns can be further validated by We initiate the modeling of movement within a specified community
them. We also look forward to new interpretations of our results from region using virtual simulations. This virtual modeling is accomplished
other filed of studies. For example, social activists may be interested in with Unreal Engine (UE), which is a software development tool designed
the number of people gathered in the public area inside the community. for creating interactive applications, which includes components such as
In this case, the location history record can provide the accurate data for a graphics engine, animation tools, physics engine, sound engine, and
them. Economists may be interested in the population flow through scripting capabilities. It is a versatile tool in the field of video games.
different gates of the community. The action history records the exact Many famous games like PUBG, FIFA and Black Myth Wukong are built
gate agents go through when going out or into the community. The with it. With the support of UE, we can visualize the virtual community
accurate population flow through all directions can thus be computed. vividly.
Our framework also provides considerable portability to be per- Fig. 8 shows the details of virtual community (Yisheng Garden
formed in different cities. The most resource expensive way is to train an Community). Consisting of 1848 households, it is an accommodation-
entirely new model based on different cities and citizens. The second business mixed complex and is located at Wuhan City in China. Fig. 7J
way is to fine tune the base model we already have using the data of new & K show the real GPS image of this real community and the upper view
cities and citizens, which is a more economical method. The most for the virtual community we constructed. All the buildings and path-
resource friendly way is to adjust action masks in the configuration file ways in the real community are included in this virtual community. As it
representing specific rules or legislation of different countries or cities. shows in Fig. 8A & C, we construct the virtual main entrances situated
By either method, our framework is able to achieve valid community between Buildings 3 and 6 on the eastern side and between Buildings 7
simulation. and 11 on the southern side with all the details matched with the real
In the future, we will construct a city simulation system based on our community. These entrances are decorated by tall, orderly placed tree
proposed community simulation framework. Modern city is a complex arrays, pedestrian pathways, and recreational green plazas. In total,
system composed of communities; therefore, city simulation can be 38.15 % of the community is covered by green land, enhancing the
made by integrating the simulation of multiple communities. The results urban streetscape and creating a warm and vibrant community
of such city simulation can be used for urban policy and planning. Traffic atmosphere.
planning is an important work of urban governance. With our simulation Other than the main buildings and public area, we also model high-
framework, we are able to simulate the commuting destination and resolution details inside the buildings as shown in Fig. 8G & H & I. Our
commuting method of each resident in each community, providing community-level social simulator provides users all the details of the
valuable reference for traffic planning of a city. Other than traffic resident in the community from bargains in the markets to evening
planning, public resource distribution has also been a delicate and walks in the park. Users can explore every corner of this virtual com-
important task for urban governance. Once we build valid simulations munity, keeping track of any resident of interest via a friendly interface.
for all the communities in the city, we are able to observe the difference
in the needs of various resources among communities. For example, our 4.2. Generative modeling of AI agents
simulation framework can provide information to infer the amounts of
different types of garbage produced in each community. Decision maker Under real-world limitations, we cannot obtain detailed information
of the city can adjust the resource for garbage recycling instructed by (data) of individuals or residents in the community, which hinders the
this simulation result. development of traditional social research. However, we can largely
Although the current framework can well simulate residents' be- simulate real-world people using generative AI agents. Based on group-
haviors in specific community, we need to point out potential limitations level features of the real residents, we generate following features for AI
and future improvements. The first is the variance of environment and agents: Gender, Age, Marital Status, Educational Level, Life Stage, Car
actions. We have not constructed nearby environment of the commu- Ownership, Commuting Distance, Commuting Methods, Career, Routine
nity, such as the spaces like schools and companies. And we have not Action, Action Time, and Go Home Time.
constructed the visualization for the actions in these spaces yet. In the Table 3shows the list of group features that we have collected from
future, we plan to expand the environment with more buildings and social surveys in this community. The features of Gender, Age and
more complicated spaces, to enlarge our action space so that the AI Commuting Method are generated independently with the ratio pre-
agents can take more detailed actions such as sporting and napping. The sented in Table 3. The distribution of marital status in Table 3indicates
second limitation is the lack of AI agents' inner motivation. Our frame- the married/single ratio among the eligible populations, which is
work now only simulates physical behaviors, which is not enough. The composed of male no younger than 22 years old and female no younger
motivations of AI agents should be included. Peng et al. claim that than 20 years old (according to Civil Code of the People's Republic of
evaluation of AGI should be rooted in dynamic embodied physical and China). Thus, we mark all the ineligible agents as single and then
social interactions (Peng et al., 2024), hence the construction of physical generate the Marital Status for the remaining individuals according to
and emotional needs is necessary. In the future, we will introduce the the distribution. We apply similar approaches to generate other features.
element of motivations when we design the action policy model for AI There exist age bounds for each level of education. Residents need to be
agents to choose so that their behavior would also reflect how the at least 12 years old to graduate from primary schools, at least 15 years
motivation drives the actions of real residents. The third limitation is the old to finish middle school, at least 18 years old to graduate from high
portability of algorithm. The environment we built now is based on one schools and at least 22 years old to graduate from colleges. Thus, we set
specific community in Wuhan. We have not verified if the algorithm we the potential Educational Level for the agents according to their ages
developed is also applicable for other communities. In the future, we and then allocate the value according to the distribution. The law reg-
would deploy the same framework for other communities to verify the ulates that people under 18 years old are not allowed to drive, so we
portability of our algorithm. mark all the ineligible agents as “No” for the feature of Car Ownership;
the feature of the Life Stage is bounded by the value of Age and Gender
as only male older than 60 or female older than 55 could be retired and
only agents older than 18 could be employed/unemployed adults; the
feature of the Commuting Duration is dependent on the Age and Life
10

P. Lu et al. C i t i e s 168 (2026) 106468
Fig. 8. This is a set of screenshots taken from the virtual community and a GPS image (J) showing the boundaries of the real community. A and C show the main
entrances located in the southern and eastern side of the virtual community. B presents an overview of the whole virtual community. D shows the detail of the
pathway inside the virtual community. E shows an overview of the exercise park in the virtual community and F gives a closer look with two residents in it. G, H and I
shows the details inside the apartments of the virtual community.
Stage since retired agents and agents under 3 years old does not need to According to the data from Wuhan Municipal Education Bureau, the
commute regularly. Besides, the feature Career for AI agents is generated Class Release Time for primary school students is 16:30, and 17:30 for
from the statistical data collected in the Seventh National Census in middle school students. The feature of Go Home Time for students is set
2021. The specific proportion is listed in Table 4. the same as the Class Release Time. For employed adults, we draw the
(cid:0) )
Routine Action is the feature representing the daily action taken by value of the working duration from the normal distribution N 9,12 ,
the agent. It usually starts in the morning and is decided by the agent's and add it to the timing of going to work to generate the Go Home Time
Life Stage. In the real society, students spend most of their time studying for employed agents.
and employed adults spend most time working. Thus, we assign “Go to
School” and “Go to Workplace” for the agents of these two life stages.
Unemployed adults and retired seniors, on the other hand, do not follow 4.3. Reinforcement learning algorithm
strict daily routine like students and employed adults. Therefore, we
assign None to Routine Action of agents experiencing these two life In a general RL framework, there exist an environment and agents
stages. can interact with the environment including other agents. We define the
The feature Action Time indicates the usual time of Routine Action. set of environment and agent as state space, which is denoted as S. Then,
For students, we assume the start time of first class is normally distrib- we define the action space set containing all possible actions for agents,
uted. According to previous social surveys, the mean value of start time denoted as A. After an action is taken, the state will somehow change.
is 7:35 and the standard deviation (SD) is 30 min (Karan et al., 2021). We define the reward from s to s′ under action a as Ra (s,s ʹ). At time step
We draw the start time from this distribution and subtract t, the agent observes the state St and receive the reward Rt. Then, it takes
Commuting Duration from it to generate Action Time. For the employed the action At and interact with the environment. The environment
adults, we set the Action Time as 9:00 subtracted by the agent's moves to a new state St+1, and then presents Stþ1 and Rtþ1 to the agent,
Commuting Duration. at next time step (t +1). In this process, our goal is to find the relation,
called policy function π:S×A→[0,1], which represents the probability
11

P. Lu et al. C i t i e s 168 (2026) 106468
Table 3 Table 4
The features and according distributions of the virtual residents from survey The features and according distributions of the virtual residents from statistical
data. data.
Survey data National census data in 2021
Gender Career
Male 51.17 % Agriculture 0.47 %
Female 48.83 % Mining 2.04 %
Manufacture 22.40 %
Resource 2.25 %
Marital status
Construction 11.00 %
Married 72.72 %
Retailing 4.71 %
Single 27.28 %
Transportation 4.65 %
Food and Accommodation 1.53 %
Age Information Technology 3.17 %
0–17 21.11 % Finance 4.43 %
18–24 7.34 % Real Estate 3.07 %
25–30 8.36 % Rental Service 4.42 %
31–35 8.36 % Scientific Research 2.73 %
36–40 6.87 % Public Service Management 1.52 %
41–45 6.79 % Resident Service 0.54 %
46–60 23.36 % Education 11.69 %
>61 17.81 % Health Industry 6.68 %
Entertainment 0.88 %
Social Benefits 11.82 %
Educational level
Primary school 12.78 % Data source: The seventh National Census in 2021.
Middle school 17.80 %
High school 7.75 %
time step 0 to infinity.
Community college 4.10 %
B
M
a
a
c
s
h
te
e
r
lo
d
r
e
d
g
e
r
g
e
r
e
ee 3
0
.
.
4
3
4
5
%
%
Vπ (s)=Eπ [Gt |St =s]=Eπ [Rt +γG t+1 |St =s] (2)
PhD and higher 0.47 % Equation 2: The Bellman Equation defines the value function as the
expected long-term return since timestep t given state s. It is also equal to
Life stage the reward at timestep t plus the discounted return at timestep t +1.
Students 21.11 %
Employed adults 52.5 % Aπ (s,a)=Qπ (s,a)(cid:0) Vπ (s) (3)
Unemployed adults 8.90 %
Retired seniors 14.10 % Equation 3: The advantage function defines how much better the
action a is than other actions at state s. Qπ (s,a)stands for the long-term
return if the agent choose action a at this timestep and then perform
Car ownership
Yes 41.67 % under policy π. Vπ (s)stands for the standard Value under policy π.
No 58.33 % Mnih et al. (2015)introduced neural network to represent the policy
function and successfully trained the agent to play video games properly
Commuting method (Mnih et al., 2015). It decides the agent's action and is then called policy
Walk 2.60 % network and the reward of each time step (t) is used for the training
Bike 5.30 % (Fig. 9). There are multiple state-of-the-art methods to optimize the
Car 59.6 %
policy network, and we decide to implement Proximal Policy Optimi-
Public transportation 29.1 %
Other 3.4 % zation Algorithms (PPO). The main reason is that agents we created can
be considered as players whose goal is to achieve the highest rate in
“behaving normal” and PPO can achieve promising performance for
Commuting duration
<15 min 36.40 % various games (Yu et al., 2022). It constructs the surrogate loss for the
15 min–30 min 35.80 % policy network that restricts the update in a certain level and encourages
30 min–60 min 19.9 % the increase of entropy (Schulman et al., 2017).
>60 min 7.9 %
Class release time 4.4. The application and improvement of LLM
Primary school 16:30
Middle school 17:30 As large language model shows the potential to simulate human
actions, we apply it to our RL framework. In earlier times, the language
models are often small and aimed to do specific finite tasks. Then,
of each action under a specific state, in order to maximize the long-term
Google researchers (2017 NeurIPS conference) introduced the trans-
return defined in Eq. (1) (Sutton, 2018). Furthermore, the expected
long-term return at the state s with the policy π is given by the Bellman former architecture in their landmark paper “Attention Is All You Need”
(Vaswani, 2017). This architecture eventually became a milestone for
Equation in Eq. (2). At state s, we would also want to know whether a
the technology of language models. The models inspired by the trans-
specific action a would yield better return than other actions on average,
under the policy π. This difference is defined by Advantage Function as former architecture could have enormous number of parameters, which
brought up the concept of “Large” Language Model (LLM). By the time of
shown in Eq. (3).
September 2024, the most famous and probably the most powerful LLM
∑∞
G= γtRt+1 =R1 +γR2 +… (1) is the model o1 published by OpenAI (Wang et al., 2024). It achieves to
t=0 establish the long-term thinking ability for the model and can beat
human experts in various academic competence. Despite the capability
Equation 1: The Bellman Function representing the long-term return
of o1, OpenAI does not provide the source code for users to set up
G as the sum of discounted instant reward with discount rate of γ from
locally. On the other hand, there also exist some other models available
12

P. Lu et al. C i t i e s 168 (2026) 106468
Fig. 9. Examples of prompts sent to LLM for the grades of behaving normal. The first one is graded 0 because the agent got up and down repeatedly during the night.
The second one is graded 50 because even though the agent got up earlier than normal, they still follow their daily routine. The last one is graded 100 because the
agent follows the routine and behave as normal as a real person.
for download and customization such as Gemma and LLaMA. They are
Table 5
both leading models according to the LMSYS Chatbot Arena Leader-
Performance of Different original LLMs and fine-tuned LLM.
board (Dunlap et al., 2024).
Before we decided to introduce LLM in the reward system, we had Model Avg difference
already trained the policy model purely using the phone usage data. We llama3.1_8b_chinese_chat_q4_k_m 28.15
recorded the action history for all the agents and found out that the AI qwen1_5-7b-chat-q8_0 62.70
agents failed to show any tendency to relocate themselves. For instance, Yi-1.5-9B-Chat.Q8_0 31.22
Mistral-7B-v0.3-Chinese-Chat-f16 34.35
the number of AI agents in their homes declines dramatically in the early
Fine-tuned llama3.1_8b_chinese_chat_q4_k_m 11.35
morning but stays stable for the rest of whole day. We believe this sit-
uation is due to the lack of reward source. The reward is only related to
the phone usage inside the community. Thus, the change of location tuned model achieves a low average difference as 11.35, which largely
would not help or undermine the achievement of reward. To simulate outperformed all original LLMs we selected. Thus, we use this fine-tuned
the location dynamics or more detailed actions other than those model to generate grade for agents' actions.
involved with phone usage, another source of reward is needed. We
introduce another source of reward given by LLM regarding AI agents'
4.5. The combined framework of RL and LLM
action history. We present some examples of prompts and responses in
Fig. 8. Double sources of reward make sure of the simulation of phone
Fig. 10shows the combined framework of RL and LLM we build. We
usage, as well as location dynamics and detailed actions.
construct the RL framework with five major parts: Agent, Environment,
In order to find the suitable LLM for the task of grading agents' ac-
Observation, Action, and Reward. We first initialize six categories of
tions, we construct a dataset from human responses. We generate 2123
locations, such as home, on the way, workplace, school, supermarket,
prompts asking if the action history regarding and ask human volunteers and public area. The location “home”, “workplace” and “school”
to answer them. In this way, we collect 2123 “prompt-response” pairs as
represent the locations where the agent lives, works or studies. Location
a fine-tuning dataset. We split the dataset into training set and testing set “on the way” indicates that the agent is moving to another location.
with the ratio 8:2. As it shows in Table 5, we first evaluate some open Location “Supermarket” represents the supermarkets and other smaller
source LLMs and evaluate their performances with the average differ- retailing stores inside the community. Location “public area” represents
ence between the grades they generate and the grades given by humans.
the public area inside the community, such as gyms, playground,
Then, we use the training set to fine tune the model “llama3.1_8b_chi-
swimming pool and garden etc. With UE, we construct the virtual
nese_chat_q4_k_m”. We choose this model because it has the best original
community containing all the apartments for agents, all the retailing
performance among the LLMs we tried. As it shows in Table 5, the fine-
stores in interest, all the other public area inside the community and a
13

P. Lu et al. C i t i e s 168 (2026) 106468
Fig. 10. The combined framework of Reinforcement Learning and Large Language Model.
road system to connect them together. Then, we generate 3000 virtual movement contains the actions of moving to other places. Group of non-
agents according to Section 4.2. We build the reward system based on movement contains actions not involving movement to another place.
the real phone usage data and the fine-tuned LLM. Once the environ-
ment and agents are reset or initialized, the time for the environment is • Movement actions:
set to be 0:00 on Monday and all the agents are set to be sleeping at
home. 1. Go Home: Each agent has been assigned to their own apartment once
the experiment begins. This action will instruct the agent to go to
their own apartment.
4.6. Observations of agents and actions
2. Go to Workplace: This action will instruct the agent to go to work.
Since we have only constructed the environment for the community
There are 10 kinds of observations in total. We divide them into 2
by now, once the agent takes this action, we would set the agent's
major groups: environment based, as well as agent based.
destination as the gate of the community, let them wait for their
corresponding commuting time and then mark them as working. This
• Environment Based Observations:
action is restricted to the employed adults. Agents in other life stages
cannot take this action.
1. Day of the Week: This observation provides information about the
3. Go to School: This action will instruct the agent to go to school. For
day of the week.
the same reason as the action to go to work, we apply the same
2. Holiday: This observation indicates whether it is a holiday.
approach to simulate the commuting process. This action is exclusive
3. Hours: This observation indicates which hour the current simulation
to students.
is at.
4. Go to Public Area: The agent taking this action will go to a random
4. Minutes: This observation indicates which minute the current
public area inside the community. There are several places available
simulation is at.
such as gym, park, swimming pool etc. as described in Section 4.1.
5. Go to Stores: The agent taking this action will go to a random store
• Agent Based Observations:
inside the community.
1. Action: This observation indicates the action the agent is taking at • Non-movement actions listed by the restrictions from locations:
current timestep.
2. Last Action: This observation indicates the action the agent was
1. Home: There are 4 actions available at home: sleep, relax, eat, and
taking at the last timestep.
read.
3. Location: This observation indicates where the agent is located at
2. Public Area: At the public area inside the community, agents can take
current timestep.
the actions of exercise.
4. Last Location: This observation indicates where the agent was
3. Stores: Agents can only take the action of shopping at the stores in-
located at the last timestep.
side the community.
5. Phone Usage: This observation indicates whether the agent is using
4. Workplace: Agent can only take the action of working at their
their phone at current timestep.
workplace.
6. Age: This observation indicates the age of the agent.
5. School: Agent can only take the action of studying at their school
In total, there are 13 actions available in the action space. We can
categorize them into 2 groups: movement and non-movement. Group of
14

P. Lu et al. C i t i e s 168 (2026) 106468
4.7. Comprehensive design of rewards widespread attention and concerns, any responsible algorithm model
must ensure that its algorithms are free from gender discrimination and
The environment generates reward for each agent based on their bias. The reward system is the only part of the whole framework where
action and current state. In our framework, we construct rewards in the gender discrimination and bias may be produced and we have
combined layers of micro-level and macro-level. Micro-level LLM eliminated this potentiality. The macro-level statistical reward is
reward is gained from the gradings by LLM, and the macro-level sta- computed purely based on the phone usage, the feature of gender is
tistical reward is computed from the difference between Simulated and entirely excluded from this type of reward. As for the micro-level reward
Real Phone Usage. Then, we take the average value of these two layers of generated from the grades generated by LLMs, the way we fine-tuned the
rewards and use this value for model training. LLM is a process of the LLM learning from human feedback. The training
In each timestep, a prompt containing the agent's information, cur- data for fine tuning is generated by volunteers containing half males and
rent time and agent's action histories is sent to the LLM engine and wait half females. In this way, we have eliminated the potential gender
for the model to grade it. If the agent is a student or employed adult, the discrimination or bias of LLM.
content would also contain the features of Routine Action and Go Home
Time. These pieces of information would help the LLM grade the agent's 4.8. Computing resource used for training and simulation
behavior more precisely. Fig. 9shows a few prompts and their corre-
sponding grade given by the LLM. Through the process of training, we use two computer machines and
For each timestep, all the agents' histories of actions by this step an additional “A30” GPU chip in total. Both computer machines are
would be rated by the LLM. Once the grades of all agents are collected, installed with “AMD Ryzen 9 7950X” CPU and “NVIDIA GeForce RTX
they would be normalized to fall in the interval of (cid:0) 1 and 1 as the final 4080” GPU. We start the UE environment in one machine and run the
reward from LLM in this timestep, for which they are referred as “LLM training process for 3000 AI agents in the other one. The large language
Rewards”. model used for grading is deployed in the “A30” chip. It takes 20 h to
Another reward is computed based on the difference between Real train each epoch.
and Simulated Phone Usage. This reward reflects how the AI agents For the simulation process of 3000 AI agents, only one computer
behave in the group (macro) level, for which it is called macro-level machine with the same computing power mentioned above is required.
statistical reward. It takes less than 1 min to simulate one step (10 min) through the
In each timestep, if the AI agent is taking the action of read, relax, simulation process.
shop, and exercise, we mark this agent using phone at this time (t). We
compute the proportion of phone users among the AI agents and denote
4.9. Training and validating procedure
it as PSim,t. We denote the proportion of phone users derived from the
Real Phone Usage as PReal,t. We take the difference between them as
In each episode, we simulate for a whole week, which is 10,080 min
Dt =PSim,t (cid:0) PStat,t. We use the variable Ui,t to denote whether the agent
in total. We collect data from the environment every 10 min, so there are
i is using their smartphone at timestep t. Ui,t =1 if the agent is using the T =1008 timesteps in total for a complete episode. Each of N =512
phone and Ui,t =0 if the agent is not. Then, we assign the macro-level agent collects q =4 timesteps of data and then we construct the loss L on
statistical reward for agent i at timestep t as Eq. (4). these Nq pieces of data with clipping factor ϵ and entropy factor β. Then,
⎧
⎨ 0,if∣Dt ∣≤0.1 we update the parameter θ for policy network at the learning rate α with
ri,t =
⎩
(cid:0) 0.5,ifDt >0.1whileUi,t =1orDt <(cid:0) 0.1whileUi,t =0 the loss constructed. We provide the procedure of one complete episode
0.5,ifDt <(cid:0) 0.1whileUi,t =1orDt >0.1whileUi,t =0 code as the following.
(4) Algorithm. Virtual community and resident.
Equation 4: If the difference between the Simulated and Real Phone
Usage is less than 0.1, we consider it trivial and don't assign reward to After 4 iterations of training, we deploy the policy model and
any agents. If the Simulated Phone Usage is significantly larger than Real generate the simulation of one week as presented in Section 2. Unlike
Phone Usage (Dt >0.1), we assign positive reward for the AI agents not the evaluation of testing sets in supervised training, comparison with
using phones and negative to those using. Similarly, when the Real human experts is commonly used to evaluate RL. Since we constructed
Phone Usage is significantly higher, we assign positive reward to AI our own virtual environment and action space, there is no previous
agents using phones and negative to AI agents not using. human expert performance to compare with. Therefore, we need to
In the current context where AI ethics and moral issues have sparked validate our model in new ways. The comparison between Simulated
15

P. Lu et al. C i t i e s 168 (2026) 106468
and Real Phone Usage data can reflect the performance of our simulation Hirshkowitz, M., Whiton, K., Albert, S. M., Alessi, C., Bruni, O., DonCarlos, L., …
in group (macro) level, and the investigation of action patterns can Kheirandish-Gozal, L. (2015). National Sleep Foundation’s sleep time duration
recommendations: Methodology and results summary. Sleep Health, 1(1), 40–43.
validate the simulation in individual (micro) level. Therefore, we pro- Hutson, J., & Ratican, J. (2023). Leveraging generative agents: Autonomous AI with
vide the results of validation in Section 2in such ways. simulated personas for interactive simulacra and collaborative research. Journal of
Innovation and Technology, 2023(15).
Karan, M., Rahal, D., Almeida, D. M., et al. (2021). School commute time, chronotype,
CRediT authorship contribution statement
and altered HPA axis functioning during adolescence. Psychoneuroendocrinology, 133,
Article 105371.
Peng Lu: Investigation, Formal analysis, Conceptualization. Mengdi Kelley, P., Lockley, S. W., Kelley, J., & Evans, M. D. (2017). Is 8: 30 am still too early to
start school? A 10: 00 am school start time improves health and performance of
Li: Data curation. Yuhao Ke: Formal analysis. Siyang Liao: Supervision, students aged 13–16. Frontiers in Human Neuroscience, 11, Article 306422.
Software. Koslowsky, M., Kluger, A. N., & Reich, M. (2013). Commuting stress: Causes, effects, and
methods of coping. Springer Science & Business Media.
Mnih, V., Kavukcuoglu, K., Silver, D., Rusu, A. A., Veness, J., Bellemare, M. G., …
Code availability
Ostrovski, G. (2015). Human-level control through deep reinforcement learning.
Nature, 518(7540), 529–533.
The trained policy model, the instruction to deploy the simulation Moussaoui, H., & Benslimane, M. (2023). Reinforcement learning: A review. International
Journal of Computing and Digital Systems, 13(1), 1.
process and code to reproduce the images shown in the paper are
Müller, M. (2007). Dynamic time warping. Information Retrieval for Music and Motion,
available at this GitHub repository: https://github.com/WhaiPkuKeyuh 69–84.
ao/RL_LLM_Social_Simulation.git. The fine-tuned LLM used for grading Park, B.-J., Yong, S.-J., Hwang, H.-S., & Moon, I.-Y. (2025). Optimizing agent behavior in
is available at ModelScope: https://www.modelscope.cn/models the MiniGrid environment using reinforcement learning based on large language
models. Applied Sciences, 15(4), Article 1860.
/PkuWhAIKyh/HumanActionGrader. Please contact the corresponding Park, J. S., O’Brien, J., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023).
author for the access to the UE environment via email: keyuhao@whai. Generative agents: Interactive simulacra of human behavior. In Proceedings of the
pku.edu.cn. 36th annual ACM symposium on user interface software and technology.
Peng, Y., Han, J., Zhang, Z., Fan, L., Liu, T., Qi, S., Feng, X., Ma, Y., Wang, Y., & Zhu, S.-C.
(2024). The tong test: Evaluating artificial general intelligence through dynamic
Declaration of competing interest embodied physical and social interactions. Engineering, 34, 12–22.
Piao, J., Yan, Y., Zhang, J., Li, N., Yan, J., Lan, X., … Zhou, D. (2025). AgentSociety: Large-
scale simulation of LLM-driven generative agents advances understanding of human
The authors declare no competing interests.
behaviors and society. arXiv preprint arXiv:2502.08691.
Roenneberg, T., Wirz-Justice, A., & Merrow, M. (2003). Life between clocks: Daily
Acknowledgement temporal patterns of human chronotypes. Journal of Biological Rhythms, 18(1), 80.
Roepke, S. E., & Duffy, J. F. (2010). Differential impact of chronotype on weekday and
weekend sleep timing and duration. Nature and Science of Sleep, 213–220.
This work was supported by the National Social Science Foundation Schulman, J., Wolski, F., Dhariwal, P., Radford, A., & Klimov, O. (2017). Proximal policy
of China (Grant No. 23&ZD090), Wuhan East Lake High-Tech Devel- optimization algorithms. arXiv preprint arXiv:1707.06347.
Simek, E. M., McPhate, L., Hill, K. D., Finch, C. F., Day, L., & Haines, T. P. (2015). What
opment Zone (also known as the Optics Valley of China, or OVC) Na-
are the characteristics of home exercise programs that older adults prefer?: A cross-
tional Comprehensive Experimental Base for Intelligent Social sectional study. American Journal of Physical Medicine & Rehabilitation, 94(7),
Governance, and the Fundamental Research Funds for the Central Uni- 508–521.
versities of Central South University (Grant No. 2023ZZTS0826 & No. Sinuany-Stern, Z. (2021). Forecasting methods in higher education: An overview.
Handbook of Operations Research and Management Science in Higher Education,
CX20230127 & No. 2023ZZTS0526). 131–157.
Soldatos, C. R., Allaert, F. A., Ohta, T., & Dikeos, D. G. (2005). How do individuals sleep
Data availability around the world? Results from a single-day survey in ten countries. Sleep Medicine, 6
(1), 5–13.
Sreedhar, K., Cai, A., Ma, J., Nickerson, J. V., & Chilton, L. B. (2025). Simulating
All the raw data and data generated during the current study are cooperative prosocial behavior with multi-agent LLMs: Evidence and mechanisms
available from the corresponding authors upon request. Please contact for AI agents to inform policy decisions. In Proceedings of the 30th international
conference on intelligent user interfaces.
the authors via email: keyuhao@whai.pku.edu.cn.
Starovoytov, V., Eldarova, E., & Iskakov, K. T. (2020). Comparative analysis of the SSIM
index and the Pearson coefficient as a criterion for image similarity. Eurasian Journal
References Of Mathematical And Computer Applications, 8(1), 76–90.
Stonedahl, F., Anderson, D., & Rand, W. (2011). When does simulated data match real
data?. In Proceedings of the 13th annual conference companion on Genetic and
Aher, G. V., Arriaga, R. I., & Kalai, A. T. (2023). Using large language models to simulate
evolutionary computation.
multiple humans and replicate human subject studies. International Conference on
Sutton, R. S. (2018). Reinforcement learning: An introduction. A Bradford Book.
Machine Learning. PMLR, 337–371. Tabone, W., & De Winter, J. (2023). Using ChatGPT for human–computer interaction
Al Nahian, M. S., Frazier, S., Riedl, M., & Harrison, B. (2024). Training value-aligned
research: A primer. Royal Society Open Science, 10(9), Article 231053.
reinforcement learning agents using a normative prior. IEEE Transactions on Artificial Tang, J., Gao, H., Pan, X., Wang, L., Tan, H., Gao, D., … Li, Y. (2024). GenSim: A general
Intelligence, 5(7), 3350–3361.
social simulation platform with large language model based agents. arXiv preprint arXiv:
Biglieri, E. (2022). Dimensions of uncertainty in communication engineering. Academic
2410.04360.
Press.
Vaswani, A. (2017). Attention is all you need. Advances in Neural Information Processing
Bracewell, R. N. (1989). The fourier transform. Scientific American, 260(6), 86–95.
Systems, 30.
Ding, Z., Huang, Y., Yuan, H., & Dong, H. (2020). Introduction to reinforcement learning.
Wang, S., Wei, Z., Choi, Y., & Ren, X. (2024). Can LLMs reason with rules? Logic scaffolding
Deep Reinforcement Learning: Fundamentals, Research and Applications, 47–123.
for stress-testing and improving LLMs. arXiv preprint arXiv:2402.11442.
Dunlap, L., Mandal, K., Darrell, T., Steinhardt, J., & Gonzalez, J. E. (2024). VibeCheck:
Xiao, B., Yin, Z., & Shan, Z. (2023). Simulating public administration crisis: A novel
Discover and quantify qualitative differences in large language models. arXiv preprint
generative agent-based simulation system to lower technology barriers in social science
arXiv:2410.12851.
research. arXiv preprint arXiv:2311.06957.
Dunn, M., Sheehan, M., Hope, T., & Parker, M. (2012). Toward methodological
Yu, C., Velu, A., Vinitsky, E., Wang, Y., Bayen, A., & Wu, Y. (2022). The surprising
innovation in empirical ethics research. Cambridge Quarterly of Healthcare Ethics, 21 effectiveness of PPO in cooperative, multi-agent games. arXiv, 24611–24624. arXiv
(4), 466–480.
preprint arXiv:2103.01955.35.
Gallicchio, L., & Kalesan, B. (2009). Sleep duration and mortality: A systematic review Zhao, K. I., Naim, M., Kondic, J., Cortes, M. E., Ge, J., Luo, S., Yang, G. R., & Ahn, A. Lyfe
and meta-analysis. Journal of Sleep Research, 18(2), 148–158.
Agents: generative agents for low-cost real-time social interactions.
Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y., Sun, J., & Wang, H. (2023).
Zheng S, Trott A, Srinivasa S, et al. The ai economist: Improving equality and
Retrieval-augmented generation for large language models: A survey. arXiv preprint
productivity with ai-driven tax policies[J]. arXiv preprint arXiv:2004.13332, 2020.
arXiv:2312.10997.
¨
Gürcan, O. (2024). Llm-augmented agent-based modelling for social simulations: Challenges
and opportunities. HHAI 2024: Hybrid Human AI Systems for the Social Good (pp.
134–144).
16
