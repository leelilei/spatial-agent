---
title: "Introduction"
source_pdf: "05_mobility_realism\\01_MobiSim_Bench_Zhang2026_OpenReview.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-22T16:10:34+00:00
page_count: 16
status: ok
text_char_count: 64291
quality_flags: ["abstract_may_include_layout_noise"]
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\05_mobility_realism\01_MobiSim_Bench_Zhang2026_OpenReview.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-22T16:10:34+00:00
- Page count: 16
- Status: ok
- Text chars: 64291
- Quality flags: abstract_may_include_layout_noise

## Metadata

- Title: Introduction
- Author: unknown
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

011 012 With advances in large language models (LLMs) and agent technology, LLM 013 agents are transforming social science research on human behavior simulation with 014 their powerful role-playing capabilities. Among the simulation studies on complex 015 human behaviors, mobility behavior simulation has been receiving widespread 016 attention and has important implications for real-world applications. Unlike data017 driven statistical learning approaches, LLM agent-based simulation methods have 018 the potential to support all-day simulation and generation of human mobility be019 haviors or even simulation of adaptive changes in the environment in extraordinary 020 scenarios. To evaluate the performance of LLM agents for human mobility be021 havior simulation from multiple perspectives and in a holistic manner, we first 022 propose an evaluation framework, which contains three perspectives: Robustness, Realism, and Responsiveness. To implement the evaluation framework, 023 we construct and publish a multi-perspective benchmark named MobiSim-Bench 024 based on the AgentSociety simulation framework. The benchmark contains the 025 Daily Mobility Simulation mainly for evaluating realism and the Hurricane 026 Mobility Simulation mainly for evaluating responsiveness. Based on this bench027 mark, we organized a challenge with 18 teams to collect and evaluate LLM agents 028 designed by different researchers. In this challenge, 967 agents were deployed. 029 The agent design approach using LLM as the brain achieves the optimum in 030 terms of realism, while the LLM as an extra is more suitable for the responsive 031 scenario. The results show that our evaluation framework and benchmark do 032 examine the performance of LLM agent for simulating human behavior from 033 different perspectives, and on the other hand, they also reveal the shortcomings of the existing LLM agent designs, which will drive the research community to 034 further explore the LLM agent design approaches that can satisfy robustness, re035 alism and responsiveness simultaneously. The benchmark codes are available at 036 https://anonymous.4open.science/r/MobiSim-Bench-1077/. 037 038 039 1 INTRODUCTION 040 041 With the development of large language modeling (LLM) (Brown et al., 2020; Touvron et al., 2023; 042 Zhao et al.) and LLM agent technology (Wang et al., 2024b; Fang et al., 2025), LLM agents have 043 not only reshaped the way of working in fields such as programming (Hong et al., 2023a; Yang 044 et al., 2023; Qian et al., 2024), but also changed the paradigm of social science research about 045 the simulation of human behaviors (Park et al., 2023; Gao et al., 2023; Li et al., 2024) with their 046 powerful role-playing capabilities (Shao et al., 2023; Chen et al., 2024). LLM agents inherit the idea of agent-based modeling (ABM) (Schelling, 1971; Deffuant et al., 2000) and replace the agents from 047 manually formulated rules to LLMs that can simulate the logic of complex human behaviors (Gao 048 et al., 2024), which have been successful in the fields of mobility behavior simulation (Shao et al., 049 2024a; Feng et al., 2024; Yan et al., 2024), social simulation (Gao et al., 2023; Park et al., 2023), 050 economic simulation (Horton, 2023; Li et al., 2024), etc. 051 052 Among the simulation studies of complex human behaviors, mobility behavior simulation has been receiving extensive attention (WU et al.; Zhang et al., 2024b; Feng et al., 2024). Accurate simulation 053 of human mobility behavior patterns is of vital importance for urban planning (Neumann et al., 1 Under review as a conference paper at ICLR 2026 054 2019), traffic management (Zhang et al., 2024a), epidemic control (Han et al., 2025), business 055 decisions (Garcia-Gabilondo et al., 2024), etc. From a technical point of view, the LLM agent-based 056 human mobility behavior simulation approach models individual behaviors from the first principle in 057 a way that can overcome the shortcomings of data-driven statistical learning predictive models (Feng 058 et al., 2018; Chen et al., 2020) or generative models (Wang et al., 2021; Yuan et al., 2022) that can 059 only restore the macroscopic distribution. Unlike predictive or generative models, the step-by-step 060 simulation approach (Zhang et al., 2025b) not only embodies the interaction between humans and urban infrastructures, such as road networks, to reflect physical law constraints and thus ensures 061 realism from the microscopic perspective, but also captures the complex intentions and scenario 062 adaptations behind the behaviors through the LLM reasoning process in the simulation. However, 063 existing works (Wang et al., 2024a; Feng et al., 2024) on predicting or simulating human mobility 064 behaviors based on LLM agents still continue the research ideas of statistical learning models, with 065 next-location prediction or trajectory generation as the main research question. They fail to focus 066 on the fact that the LLM agent’s role-playing ability with human common sense understanding and 067 reasoning has the potential to support all-day simulation of human mobility behaviors as well as the 068 simulation of adaptive changes in the environment in extraordinary scenarios. Therefore, we believe 069 that long time scale simulation on the day level and different external environment effects are the key 070 to test whether the LLM agents are capable of performing the mobility simulation task and generating 071 highly realistic human mobility behaviors. At the same time, the evaluation of the simulation results should also go deeper from the macro-distribution statistics to the behavioral intention level. 072 073 To achieve this, we propose an evaluation framework for comprehensively evaluating the LLM agent’s 074 simulated human mobility behaviors from multiple perspectives as follows: 075 • Robustness: First of all, as the most basic requirement, the LLM agents should be able to 076 complete long time-scale mobility simulations for a day or even longer without errors. 077 • Realism: Second, simulation results based on LLM agents should approximate real-world human 078 data in terms of microscopic intentions and macroscopic statistical metrics. 079 • Responsiveness: Unlike data-driven modeling approaches, LLM agent-driven simulation ap080 proaches have advanced thinking and reasoning capabilities and should be able to show respon081 siveness to different external environmental changes. 082 Based on this evaluation framework, we construct and publish a multi-perspective benchmark named 083 MobiSim-Bench to advance the research related to the simulation of human mobility behaviors 084 using LLM agents. MobiSim-Bench consists of two day-level long time-scale simulation tasks, 085 Daily Mobility Simulation under normal conditions and Hurricane Mobility Simulation under 086 abnormal conditions. To build the two tasks, we collected real-world mobility data, constructed the 087 agent profiles and map data used for initializing agents for the simulation tasks. The real human 088 behaviors were extracted as ground truth for evaluation. In terms of evaluation methods, we not 089 only include common macroscopic statistical distribution metrics, but also further add individual 090 behavioral intention determination. For the hurricane scenario, we also design behavioral change 091 metrics to evaluate the adaptability of the agents. Overall, MobiSim-Bench fully evaluates the realism 092 of LLM-agent-based human mobility simulation in terms of microscopic intentions and macroscopic 093 statistical metrics from both normal and abnormal scenarios, and also examines the environmental adaptability under the impacts of external environmental changes, which realizes a multi-perspective 094 evaluation of long-scale human mobility simulation. 095 096 We organized a competition based on our benchmark and collected LLM agents constructed by human 097 experts. A total of 18 teams participated in the competition, submitting 967 agent implementations. 098 We systematically classified all submitted methods into three categories based on the role of LLMs in 099 the agent architecture: LLM as Brain, LLM as Glue, and LLM as Extra. These specially designed agents achieved peak scores of 66.38 in the Daily Mobility task and 85.63 in the Hurricane Mobility 100 task. These competitive outcomes confirm that MobiSim-Bench enables rigorous evaluation of diverse 101 agent design paradigms and validates our multi-dimensional framework for measuring robustness, 102 realism, and responsiveness in long-term mobility simulations. 103 104 Overall, the main contributions of this paper are listed as follows: 105 • We propose an evaluation framework for comprehensively evaluating the LLM agent’s simulated 106 human mobility behaviors from robustness, realism, and responsiveness. 107 2 Under review as a conference paper at ICLR 20 108 • We construct and publish a multi-perspective 109 Mobility Simulation task under normal cond 110 under abnormal conditions for benchmarkin 111 • We organized a competition to collect, qua 112 ferent teams with different design paradigm 113 corresponding baselines. 114 115 2 EVALUATION FRAMEWORK 116 117 Introducing LLM agents to simulate human b 118 role-playing, understanding, and reasoning cap 119 generative algorithms driven by data and statis 120 agents provide us with a window to simultaneo 121 outcomes, while also possessing the potential to 122 Given these differences, relying solely on statist 123 evaluate LLM agents has become inadequate. Th 124 comprising three key elements as shown in F 125 potential of LLM agents: Robustness, Realism 126 capabilities required for an LLM agent to simul 127 evaluation metrics. 128 129 2.1 ROBUSTNESS 130 131 Robustness is the most fundamental require132 ment for LLM agents. Unlike statistical learning 133 models that take fully standardized inputs and 134 also produce standardized output matrices, LLM agents directly handle diverse inputs. These in135 puts include predefined character profiles and 136 external commands, as well as callable functions 137 and even program errors encountered during ex138 ecution. LLM agents are required to correctly 139 handle all situations and continue simulation 140 with any inputs. This requires the agents to be 141 able to follow instructions to conduct simula142 tions, while also correctly utilizing functions 143 through structured output or function call capa144 bilities. Retry mechanisms and fallbacks will 145 prevent the program from crashing in the event of an LLM error. After ensuring the program 146 simulates normally, the agent’s ability to main147 tain context during day-level long-term simula148 tions will prevent absurd outcomes, such as contin 149 et al., 2025c) serves as the primary solution to t 150 151 Currently, with the advancement of LLM cap frameworks (Gao et al., 2025; Zhang et al., 2 152 mechanisms to build the aforementioned capabi 153 for LLM agents like mem0 (Chhikara et al., 2025 154 reduced the complexity of designing memory m 155 156 The evaluation of robustness is relatively straig 157 can complete the simulation without crashing. A 158 159 2.2 REALISM 160 Realism represents a further requirement that i 161 human mobility behavior. In human mobility be nchmark named MobiSim-Bench with the Daily ns and the Hurricane Mobility Simulation task atively evaluate, and compare agents from difn mobility simulation scenarios, and provided vior will release the high potential of LLMs’ ities in this research field. Unlike prediction or learning models, step-by-step simulated LLM observe behavioral motivations and behavioral pond to environmental changes. distributions of simulated mobility behaviors to we propose a hierarchical evaluation framework e 1 based on the technical characteristics and nd Responsiveness. Each element reflects the human mobility behavior and the corresponding Responsiveness Realism obustness gure 1: A hierarchical framework for evaluating LM agents that simulate human mobility behavrs. usly going out to eat. Memory mechanism (Zhang problem. ities and the maturation of agent development 5a), researchers can easily adopt their built-in s and create an agent program. Memory systems d A-MEM (Xu et al., 2025) have also significantly les. orward: it involves observing whether the agent agent that crashes will be vetoed outright. posed on LLM agents in the task of simulating or simulation tasks, LLM agents are tasked with Under review as a conference paper at ICLR 20 162 playing the role of individuals possessing speci 163 within a virtual city. This will evaluate the rol 164 whether they can perform travel behaviors cons 165 commuting to school or a white-collar worker he 166 ability to understand and apply human societal co 167 sleep schedules, commuting habits, and dining p 168 can realistically simulate human mobility. Plann long-duration simulations to ensure that moveme 169 reasonable. 170 171 The evaluation of realism can continue to utilize 172 from prediction and generation tasks (Feng et a 173 distribution and gyration radius distribution simi 174 cesses of LLM agents can be observed by resear recording and evaluation of micro-level behavio 175 whether LLM agents truly think and act like hum 176 177 178 2.3 RESPONSIVENESS 179 Responsiveness is the key to surpassing statis 180 simulate human mobility behavior. Statistical le 181 distributions to achieve generalization, renderin 182 scenarios. The powerful understanding provid 183 receive and process natural language descriptio 184 Leveraging the built-in knowledge and reason 185 transform these descriptions into adaptive actio 186 adaptation process, expert knowledge helps th environmental changes and implicitly suggests tr 187 the agent’s decision-making preferences, making 188 Reflective capabilities primarily focus on whethe 189 based on factors like external environmental shi 190 191 For the evaluation of adaptability, we suggest fo 192 before and after external environmental changes could involve computing the similarity in the dis 193 changes. 194 195 In summary, the proposed framework for assessin 196 a step-by-step standard for evaluating the perfo 197 human mobility behavior. This framework facili 198 simulation from statistical fitting toward unde 199 avenues for exploring human movement pattern 200 201 3 MOBISIM-BENCH 202 203 3.1 BENCHMARK OVERVIEW 204 205 To implement the proposed evaluation framew 206 siveness of LLM agents, we introduce a multi-p 207 benchmark consists of two tasks: Daily Mobilit 208 Both tasks are designed to evaluate LLM agent under different contextual conditions. The daily m 209 of Realism, as it focuses on capturing routine, ev 210 simulated outputs can approximate real-world hu 211 levels. In contrast, the hurricane mobility simula 212 it targets behavioral changes and adaptive respo 213 whether LLM agents can dynamically adjust to 214 As illustrated in Figure 2, the entire framework c 215 ground-truth trajectories and user profiles are i rofiles and self-determining their travel choices aying capabilities of LLM agents, specifically nt with a given profile, such as a student always ng to an office building. At the same time, LLMs’ mon sense and routine behavioral patterns, such as rences, will also determine whether LLM agents capabilities are also essential when dealing with ehaviors throughout the day remain relevant and mmon macro-level statistical distribution metrics 018; Yuan et al., 2022), such as check-in count y metrics. Furthermore, since the reasoning pros through natural language, we can introduce the ntentions. This will help researchers understand s. l learning models when using LLM agents to ng models rely entirely on the similarity of data em useless when facing rare out-of-distribution by LLMs to agents will enable these agents to f environmental changes in abnormal situations. capabilities of LLMs, they have the ability to n response to environmental shifts. During this gent fully comprehend the impacts of external plans. Emotions such as panic and fear reinforce m more aligned with real-world human behavior. e agent can re-plan and alter travel arrangements expert knowledge, and its own emotional state. ng on whether the differences in travel behavior gn with real-world conditions. For instance, this ution of travel time changes before and after the bustness, realism, and responsiveness establishes ance and potential of LLM agents in simulating s the transition of research paradigms in mobility nding-based behavior modeling, opening new thin complex dynamic environments. to evaluate the robustness, realism, and responective benchmark named MobiSim-Bench. The mulation and Hurricane Mobility Simulation. the domain of human mobility simulation, but ility simulation is primarily aligned with the goal day urban travel behaviors and assessing whether n mobility at both microscopic and macroscopic is closely tied to the goal of Responsiveness, as s during extreme weather events, thereby testing den environmental perturbations. ists of three stages: (i) Data Preparation, where rated with urban networks (for Daily Mobility) Under review as a conference paper at ICLR 2026 216 217 218 Daily Mobility GT 219 Ground Truth 220 Trajectories with Intentions Gen 221 Demographic 222 Profile, work and home Agent Init 223 Environment 224 Urban network of Beijing 225 Sim Init Environment 226 • Columbia Map Simulation Engine GT 227 Demographic Sunny Hurricane Cloudy Gen 228 Profile, work and home 229 230 Ground Truth Travel Statistics during HC 231 Time Sequence 232 Hurricane Mobility Evaluation 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255 256 257 258 259 260 261 262 263 264 265 266 267 268 269 tnuomAlevarT Step1 Preparation Step2 Simulation Step3 Evaluation Realism Robustness MICRO S In e t q e u n e ti n o c n e P I r n o t p en o t r i t o io n n MACRO G R y a r d at iu io s n L N o u c m at b io e n r Output Responsiveness • Weather Info Weather Change Change Rate Travel Distribution Figure 2: Overview of the MobiSim-Bench. or hurricane-related maps and census statistics (for Hurricane Mobility); (ii) Simulation, where agents are initialized with demographic and environmental inputs and executed within the built-in mobility engine of AgentSociety (Piao et al., 2025b; Zhang et al., 2025a); this engine performs first-principles simulations at a temporal resolution of 1 second, allowing agents to move through explicit function calls that translate intentions into concrete actions, thereby constructing complete mobility trajectories; (iii) Evaluation, where the generated behaviors are compared against real-world data, with Daily Mobility metrics (gyration radius, location number, intention sequence, intention proportion) assessing Realism, and Hurricane Mobility metrics (change rate, temporal distribution of travel) assessing Responsiveness. 3.2 DAILY MOBILITY SIMULATION Task Definition: The simulation requires each agent to generate temporally ordered intentions and corresponding actions that are consistent with user characteristics and the surrounding urban environment. The inputs include user demographic profiles, city-level geographic and transportation information, and daily time constraints. The outputs consist of each agent’s concrete mobility behaviors, including intention sequences, executed actions, and the resulting movement trajectories. Evaluation Metrics: To evaluate whether LLM-based mobility simulations approximate real-world human behavior, it is essential to quantify the similarity between the generated outcomes and empirical distributions. Similarity-based evaluation provides a principled way to measure how closely synthetic trajectories reproduce both individual-level behavioral intentions and population-level statistical regularities, thereby aligning directly with the Realism objective of our framework. We adopt the Jensen–Shannon Divergence (JSD) as the core similarity measure (see Appendix B). Lower JSD values indicate higher similarity between simulated and observed distributions. The benchmark evaluates four specific aspects, corresponding to different levels of behavioral realism: • Intention Sequences JSD: Consistency in the ordering of individual activity types, directly reflecting behavioral intentions. • Gyration Radius JSD: Similarity in spatial dispersion patterns, capturing the aggregate range of mobility. • Daily Location Numbers JSD: Alignment in the number of distinct places visited per day across the population. • Intention Proportions JSD: Balance among different activity categories at the population level. To provide a holistic assessment, these four metrics are aggregated into a single Final Score (Appendix B). The final score rescales similarity into the normalized range [0, 100], enabling direct comparison across models and tasks. 5 Under review as a conference paper at ICLR 2026 270 Data Preparation: This benchmark builds upon the processed dataset released in (Shao et al., 2024b), 271 which originates from large-scale mobility records provided by Tencent and China Mobile. The 272 dataset integrates two complementary sources of information: (i) fine-grained mobility trajectories of 273 Beijing users, capturing daily location visits and activity intentions, and (ii) user profile attributes 274 that enrich the contextual understanding of individual behavior. These data enable a comprehensive 275 representation of both movement patterns and demographic heterogeneity, forming the foundation for 276 evaluating LLM-based mobility simulations. 277 Overall, the Daily Mobility Simulation provides a principled framework for measuring the ability 278 of LLM agents to reproduce realistic urban mobility patterns. By aligning closely with the Realism 279 dimension of our evaluation framework, it assesses whether simulated trajectories approximate 280 real-world data at both microscopic (individual-level intentions) and macroscopic (population-level 281 statistics) scales, thereby supporting future research in mobility-aware AI systems. 282 283 3.3 HURRICANE MOBILITY SIMULATION 284 Task Definition: Agents are required to generate user-level mobility patterns that reflect behavioral 285 variations across three temporal phases: pre-hurricane, during-hurricane, and post-hurricane. The 286 inputs include hurricane-related contextual information, user demographic and behavioral features, 287 and explicit temporal phase indicators, while the outputs consist of each agent’s concrete mobility 288 behaviors in terms of travel time and location information. 289 Evaluation Metrics: Two major dimensions are used: 290 291 • Change Rate Accuracy (Change Rate Score): The accuracy of mobility change rates is 292 measured by mean absolute percentage error (MAPE) (see Appendix B). 293 • Distribution Similarity (Distribution Score): Hourly travel distributions are compared using 294 cosine similarity (see Appendix B). 295 The final score is a weighted combination of the two metrics (see Appendix B). The weighting 296 emphasizes change rate accuracy (60%) due to its direct reflection of hurricane impact, while 297 distribution similarity (40%) captures temporal mobility dynamics. 298 Data preparation: For the Hurricane Mobility Simulation, we use mobility records obtained from 299 SafeGraph, filtered to include users located in the city of Columbia during Hurricane Dorian. The 300 original SafeGraph data are provided at a weekly resolution, which we further processed into daily 301 trajectories to capture finer-grained temporal dynamics across the pre-hurricane, during-hurricane, and 302 post-hurricane phases. In addition to mobility traces, synthetic user profiles are constructed through a 303 CBG (Census Block Group)-based sampling procedure: (i) identifying the set of CBGs belonging to 304 Columbia, (ii) allocating population samples proportional to each CBG’s demographic weight, (iii) 305 assigning residential locations within the sampled CBGs, and (iv) sampling additional attributes such 306 as gender, race, and income level according to CBG-level statistics. This combination of processed 307 mobility trajectories and sampled profile attributes provides a realistic and demographically grounded 308 dataset for evaluating agent responsiveness under extreme conditions. 309 Overall, the Hurricane Mobility Simulation provides a rigorous and domain-specific framework 310 to evaluate whether LLM agents can replicate mobility adaptations under extreme weather. By 311 emphasizing both change rate fidelity and temporal distribution alignment, it directly reflects the 312 Responsiveness dimension of our evaluation framework, testing whether agents can dynamically 313 adjust their behaviors to sudden environmental perturbations and advancing the study of AI-driven 314 human mobility modeling in disaster scenarios. 315 316 4 EXPERIMENTS 317 318 Based on our MobiSim-Bench benchmark, we organized an open competition to evaluate LLM 319 agents under real-world mobility scenarios. A total of 18 teams participated in the competition, with 320 10 teams entering the daily mobility simulation task and 8 teams entering the hurricane mobility 321 simulation task. Across all submissions, a total of 967 agents were deployed, of which 933 passed the 322 robustness evaluation and obtained valid evaluation scores. Among these, 361 agents were submitted for the daily mobility task and 572 agents for the hurricane mobility task, reflecting both the scale 323 and diversity of approaches explored by the participating teams. 6 Under review as a conference paper at ICLR 2026 324 Table 1: Performance of all teams’ final submitted agents on the daily mobility task. Boldface 325 indicates best performance. 326 327 Team Role of LLM Base Model JSD JSD JSD JSD Final Score gyr loc seq prop 328 #01 Brain GLM-4-Flash 0.328 0.665 0.063 0.289 66.38 329 #02 Brain GLM-4-Flash 0.334 0.554 0.183 0.404 63.13 330 #03 Brain GLM-4-Flash 0.321 0.692 0.320 0.190 61.93 331 #04 Glue Qwen-plus 0.421 0.495 0.266 0.366 61.29 #05 Glue GLM-4-Flash 0.329 0.655 0.170 0.404 61.04 332 #06 Brain GLM-4-Flash 0.339 0.560 0.262 0.408 60.79 333 #07 Extra GLM-4-Flash 0.384 0.786 0.267 0.217 58.62 334 #08 Glue deepseek-chat 0.397 0.735 0.198 0.378 57.32 335 #09 Extra GPT-4 0.433 0.720 0.253 0.522 51.80 336 #10 Extra Qwen-plus 0.393 0.791 0.639 0.441 43.39 337 338 Table 2: Performance of all teams’ final submitted agents on the hurricane mobility task. GC repre339 sents the Generated Change (During/After vs Before), CE represents the Change Error (During/After 340 vs Before), CRS represents the Change Rate Score, DS represents the Distribution Score. The 341 ground-truth Real Change is -47.34 / -11.50 (During/After vs Before), which is used to compute the 342 Change Error from Generated Change. Boldface marks the best performance. 343 344 Team Role of LLM Base Model GC CE CRS DS Final Score 345 #11 Extra GLM-4-Flash -44.01 / -12.76 3.33 / 1.26 91.02 77.53 85.63 346 #12 Extra deepseek-chat -45.54 / -9.90 1.80 / 1.60 91.13 64.47 80.47 347 #13 Brain GLM-4-Flash -86.25 / -11.54 38.91 / 0.04 58.74 76.37 65.79 #14 Glue deepseek-chat -8.37 / -14.44 38.97 / 2.94 46.08 86.33 62.18 348 #15 Brain GLM-4-Flash -43.30 / -14.43 4.04 / 2.93 83.00 27.56 60.83 349 #16 Brain GLM-4-Flash -41.20 / -66.56 6.14 / 55.06 0.00 85.78 34.31 350 #17 Brain GLM-4-Flash -28.35 / -46.63 18.99 / 35.12 0.00 83.40 33.36 351 #18 Extra GLM-4-Flash -60.05 / -94.75 12.71 / 83.25 0.00 58.01 23.20 352 353 4.1 BASELINES 354 355 The participating teams adopted a wide range of strategies, and some teams even experimented with 356 multiple approaches. Across all these submissions, we identified three predominant design paradigms, 357 each with distinct roles for LLMs in the decision-making process. 358 LLM as Brain: In this paradigm, teams primarily leverage LLMs’ comprehensive reasoning and 359 creative generation capabilities to drive complete agent behavior. These approaches utilize the LLM’s 360 natural language processing and multi-step reasoning to produce complex behavioral decisions. 361 The best-performing LLM-dominated approach in the daily mobility task employs a narrative362 driven methodology. First, the LLM generates a detailed, first-person daily narrative describing the 363 character’s activities and thoughts throughout the day (An example can be found in Appendix A.3). 364 Second, another LLM call parses this narrative into structured activity plans. This two-step process ensures both narrative coherence and structural precision, allowing the agent to follow a pre-generated 365 plan throughout the task day. 366 367 LLM as Glue: In this paradigm, teams primarily utilize LLMs’ contextual adaptation and intelligent 368 bridging capabilities to enhance rule-based systems. These approaches leverage the LLM’s ability to 369 understand complex contexts and provide intelligent recommendations that connect different system 370 components. The best-performing LLM-as-Glue approach employs a multi-phase state manager with explicit normal, hurricane, and post-hurricane phases. The system maintains internal states (fatigue, 371 hunger, emotion, personality) and uses predefined behavioral templates, but the LLM provides 372 intelligent recommendations that consider the agent’s current subjective state, personality type, and 373 environmental context. When the primary rule-based system encounters complex situations, the LLM 374 bridges the gap between rigid templates and dynamic contextual needs. 375 376 LLM as Extra: In this paradigm, teams either minimally utilize LLM capabilities or completely avoid them, with core intelligence residing in well-designed rule systems. When present, teams only utilize 377 the LLM’s basic pattern recognition abilities as supplementary tools. The best-performing LLM-as7 Under review as a conference paper at ICLR 20 378 Extra approach in the hurricane mobility task e 379 system that adapts to different hurricane phases 380 fines three distinct phases with corresponding pr 381 for each hour of the day. The decision logic is e 382 that sophisticated agent behavior can be achiev 383 advanced LLM capabilities. 384 385 4.2 RESULTS 386 The performance results across the three desig 387 distinct trade-offs and characteristics that align 388 389 LLM as Brain: The LLM-as-Brain approach ac 390 task, demonstrating its strength in generating n 391 JSD scores for intention sequences and intention 392 at producing coherent and psychologically plau closely match real human behavior patterns at a 393 micro-behaviors such as morning commutes, lun 394 with the daily mobility benchmark’s focus on beh 395 activity transitions and maintain appropriate inte 396 other types of environmental changes, such as hu 397 struggles, producing unrealistic or overly comp 398 accurate human responses required during emer 399 LLM as Glue: The LLM-as-Glue approach 400 indicating its versatility in handling diverse sce 401 suggest that while state-driven agents can main 402 the complexity of parameter tuning and state sp 403 lower distribution score indicates challenges in a 404 weather events. 405 LLM as Extra: The LLM-as-Extra approach 406 mobility task, where predictability and reliabilit 407 change rate score demonstrates that rule-based sy 408 shifts during extreme weather events, which is e 409 phasis on change rate accuracy. However, the rel 410 that rigid rule structures may limit behavioral d 411 evidenced by higher JSD scores across all metri 412 413 4.3 DISCUSSION 414 415 Cross-task Performance Patterns: The perform 416 the quality of human behavior simulation across 417 evaluates the ability to simulate realistic daily hu 418 excel by leveraging the model’s comprehensive re appropriate behaviors. The superior JSD scores 419 that LLM-driven agents produce more coherent a 420 suggesting that complex behavioral modeling be 421 422 However, in the hurricane mobility task, which 423 during extreme weather events, LLM-as-Extra 424 perform those with greater LLM integration. T clear behavioral patterns and predictable huma 425 accurately model the expected changes in huma 426 struggle to represent the precise behavioral pat 427 emergency response simulation. 428 429 Cross-model Performance Patterns: In the h 430 rule-driven pipeline with different base models fitting the overall change rate and preserving h 431 Deepseek-chat(DeepSeek-AI et al., 2024) show oys a sophisticated hour-level probability table individual agent characteristics. The system debility matrices that specify movement likelihoods ely deterministic and rule-based, demonstrating hrough well-designed rule frameworks without aradigms as Table 1 and Table 2 shows reveal their underlying design philosophies. ved the highest performance in the daily mobility al and diverse behavioral patterns. The superior oportions indicate that LLM-driven agents excel e activity sequences. These sequences not only cro level but also effectively reconstruct specific breaks, and evening leisure activities. This aligns oral realism, where the ability to generate natural n distributions is crucial. However, when facing cane scenarios, the current LLM-as-Brain design behaviors that fail to replicate the simplified yet cies. eved balanced performance across both tasks, ios. The moderate JSD scores in daily mobility n behavioral coherence, they may struggle with management. In the hurricane mobility task, the ately modeling temporal patterns during extreme wed remarkable effectiveness in the hurricane e crucial for emergency scenarios. The excellent ms can accurately capture the expected behavioral ntial for the hurricane mobility benchmark’s emely lower performance in daily mobility suggests rsity and creativity in normal circumstances, as ce patterns reveal how different LLM roles affect erent scenarios. In the daily mobility task, which n movement patterns, LLM-as-Brain approaches ning capabilities to generate natural, contextually ntention sequences and proportions demonstrate ty patterns that better match real human behavior, fits from maximal LLM involvement. aluates the ability to simulate human responses roaches (with minimal LLM involvement) outreveals an important insight: for scenarios with esponses, well-designed rule systems can more mobility behavior, while current LLMs may still s and temporal dynamics required for accurate cane mobility task, one team applied the same vealing clear model-specific trade-offs between -level distribution patterns. (as Table 3 shows). e tightest alignment with targeted change rates, Under review as a conference paper at ICLR 2026 432 Table 3: Comparison of three base models from the same team using the same paradigm on the 433 hurricane mobility task. Boldface marks the best performance. 434 435 Model GC CE CRS DS Final Score 436 GLM-4-Flash-Free -44.01 / -12.76 3.33 / 1.26 91.02 77.53 85.63 437 Deepseek-chat -46.76 / -11.51 0.58 / 0.01 99.36 59.87 83.57 438 Qwen-plus -51.18 / -10.49 3.83 / 1.02 91.53 56.18 77.39 439 reflecting strong numerical discipline and instruction-following, but this comes at the cost of flatter, 440 less detailed hourly dynamics. GLM-4-Flash-Free achieves the most balanced performance, keeping 441 change errors low while maintaining richer diurnal structures, which supports its leading overall 442 score. Qwen-plus(Yang et al., 2025), by contrast, lags on both metrics, with larger deviations in 443 change rate and weaker reconstruction of hourly usage, indicating less stable phase calibration. These 444 outcomes suggest a practical guideline: choose numerically disciplined models when aggregate accuracy is critical, and balanced models when both accuracy and realistic hourly patterns matter, 445 avoiding models with inconsistent behaviors across metrics. 446 447 448 5 RELATED WORK 449 450 5.1 MOBILITY SIMULATION 451 Research on mobility behavior simulation can be broadly divided into two categories. The first cate452 gory follows traditional deep learning approaches, including classical Markov models (Rendle et al., 453 2010) and subsequent sequence-modeling techniques such as recurrent neural networks (RNNs) (Lai 454 et al., 2023; Feng et al., 2020) and attention-based architectures (Qin et al., 2022; Hong et al., 2023b). 455 More recent studies employ LLM-driven agents to conduct mobility simulations (Feng et al., 2025; 456 Shao et al., 2024b; Wang et al., 2024c), leveraging the agents’ extensive world knowledge, reasoning 457 capabilities, and adaptive decision-making to generate more realistic and dynamic movement patterns. 458 459 5.2 LLM AGENT SIMULATION BENCHMARK 460 461 The use of LLM agents for simulation has attracted growing attention in recent years. A number of 462 studies (Sukiennik et al., 2025; Zhao et al., 2024) have demonstrated the broad societal value of 463 deploying LLM agents in complex simulation settings. Meanwhile, platforms such as AgentSoci464 ety (Piao et al., 2025b) and YuLan-OneSim (Wang et al., 2025), along with recent efforts to optimize multi-agent simulation systems (Piao et al., 2025a; Zhang et al., 2025a), have further facilitated 465 large-scale agent-based simulation experiments. Despite these advances, most existing LLM-agent 466 benchmarks remain primarily focused on assessing ”tool-like” capabilities (Abdelnabi et al., 2024; 467 Zhu et al., 2025; Xu et al., 2024; Piatti et al., 2024), offering limited evaluation of agents’ ability 468 to simulate human behavioral patterns. Our work addresses this gap by introducing a benchmark 469 specifically designed to assess agents’ competence in modeling realistic human behaviors, thereby 470 contributing a novel and meaningful perspective to the field. 471 472 6 CONCLUSION 473 474 In this paper, to comprehensively evaluate the performance of LLM agent for human mobility 475 behavior simulation, we propose an evaluation framework containing three perspectives: robustness, 476 realism, and responsiveness. Guided by the evaluation framework, we construct a multi-perspective 477 benchmark named MobiSim-Bench powered by AgentSociety simulation framework, which contains 478 the daily mobility simulation and the hurricane mobility simulation. By organizing a challenge, we 479 evaluated the performance of multiple LLM agent design approaches under this evaluation framework 480 and benchmark. Unfortunately, none of the LLM agent designs can achieve robustness, realism and 481 responsiveness at the same time. This demonstrates the importance and value of MobiSim-Bench on 482 one hand, and reveals the inadequacy of current LLM agent designs for simulating human mobility 483 behavior on the other. We hope that MobiSim-Bench can help the research community to explore 484 and discover LLM agent designs that can effectively and comprehensively simulate human mobility behavior, and thus promote the development of social science research paradigms driven by LLM 485 agents. 9 Under review as a conference paper at ICLR 2026 486 ETHICS STATEMENT 487 488 This work fully complies with the ICLR Code of Ethics. All datasets used in MobiSim-Bench 489 have undergone strict anonymization and desensitization procedures to ensure that no personally 490 identifiable or sensitive information is retained. The benchmark is designed solely for research 491 purposes, emphasizing transparency, reproducibility, and responsible use. Dataset documentation, 492 simulation procedures, and evaluation guidelines are provided to facilitate safe adoption and avoid 493 potential misuse. No conflicts of interest or external sponsorship influenced the design or outcomes 494 of this work. 495 496 REPRODUCIBILITY STATEMENT 497 498 We prioritize reproducibility by releasing all necessary resources alongside the paper. The datasets 499 used in MobiSim-Bench, preprocessing scripts, simulation workflow, evaluation metrics, and baseline 500 implementations are included in an anonymized repository linked with the abstract. We provide 501 detailed descriptions of the two tasks in our benchmark framework, the Daily Mobility Simulation (in 502 Subsection 3.2) and the Hurricane Mobility Simulation (in Subsection 3.3). Each Subsection specifies 503 the task definition, the datasets employed, and the corresponding preprocessing steps. In addition, Appendix B lists the complete calculation formulas for all evaluation metrics. Considering the 504 inherent randomness of LLMs, in order to reduce the difficulty of reproduction, we release baseline 505 methods for both tasks, with Section 3 reporting extensive results across different LLM configurations. 506 Appendix A.2 further compiles all benchmark results for reference, while Appendix A.3 presents a 507 detailed output example of the best-performing LLM-driven agent in the Daily Mobility task. These 508 resources collectively ensure that independent researchers can reliably reproduce and extend our 509 findings. 510 511 REFERENCES 512 513 Sahar Abdelnabi, Amr Gomaa, Sarath Sivaprasad, Lea Scho¨nherr, and Mario Fritz. Cooperation, 514 competition, and maliciousness: Llm-stakeholders interactive negotiation. In A. Globerson, 515 L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang (eds.), Advances in Neural 516 Information Processing Systems, volume 37, pp. 83548–83599. Curran Associates, Inc., 2024. 517 URL https://proceedings.neurips.cc/paper_files/paper/2024/file/ 984dd3db213db2d1454a163b65b84d08-Paper-Datasets_and_Benchmarks_ 518 Track.pdf. 519 520 Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, 521 Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are 522 few-shot learners. Advances in neural information processing systems, 33:1877–1901, 2020. 523 Jiangjie Chen, Xintao Wang, Rui Xu, Siyu Yuan, Yikai Zhang, Wei Shi, Jian Xie, Shuang Li, Ruihan 524 Yang, Tinghui Zhu, et al. From persona to personalization: A survey on role-playing language 525 agents. arXiv preprint arXiv:2404.18231, 2024. 526 527 Yile Chen, Cheng Long, Gao Cong, and Chenliang Li. Context-aware Deep Model for Joint Mobility 528 and Time Prediction. In Proceedings of the 13th International Conference on Web Search and 529 Data Mining, pp. 106–114, Houston TX USA, January 2020. ACM. ISBN 978-1-4503-6822-3. 530 doi: 10.1145/3336191.3371837. URL https://dl.acm.org/doi/10.1145/3336191. 531 3371837. 532 Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. Mem0: Building 533 production-ready ai agents with scalable long-term memory. arXiv preprint arXiv:2504.19413, 534 2025. 535 536 DeepSeek-AI, :, Xiao Bi, Deli Chen, Guanting Chen, Shanhuang Chen, Damai Dai, Chengqi Deng, 537 Honghui Ding, Kai Dong, Qiushi Du, Zhe Fu, Huazuo Gao, Kaige Gao, Wenjun Gao, Ruiqi 538 Ge, Kang Guan, Daya Guo, Jianzhong Guo, Guangbo Hao, Zhewen Hao, Ying He, Wenjie Hu, Panpan Huang, Erhang Li, Guowei Li, Jiashi Li, Yao Li, Y. K. Li, Wenfeng Liang, Fangyun 539 Lin, A. X. Liu, Bo Liu, Wen Liu, Xiaodong Liu, Xin Liu, Yiyuan Liu, Haoyu Lu, Shanghao Lu, 10 Under review as a conference paper at ICLR 2026 540 Fuli Luo, Shirong Ma, Xiaotao Nie, Tian Pei, Yishi Piao, Junjie Qiu, Hui Qu, Tongzheng Ren, 541 Zehui Ren, Chong Ruan, Zhangli Sha, Zhihong Shao, Junxiao Song, Xuecheng Su, Jingxiang 542 Sun, Yaofeng Sun, Minghui Tang, Bingxuan Wang, Peiyi Wang, Shiyu Wang, Yaohui Wang, 543 Yongji Wang, Tong Wu, Y. Wu, Xin Xie, Zhenda Xie, Ziwei Xie, Yiliang Xiong, Hanwei Xu, 544 R. X. Xu, Yanhong Xu, Dejian Yang, Yuxiang You, Shuiping Yu, Xingkai Yu, B. Zhang, Haowei 545 Zhang, Lecong Zhang, Liyue Zhang, Mingchuan Zhang, Minghua Zhang, Wentao Zhang, Yichao 546 Zhang, Chenggang Zhao, Yao Zhao, Shangyan Zhou, Shunfeng Zhou, Qihao Zhu, and Yuheng Zou. Deepseek llm: Scaling open-source language models with longtermism, 2024. URL 547 https://arxiv.org/abs/2401.02954. 548 549 Guillaume Deffuant, David Neau, Frederic Amblard, and Ge´rard Weisbuch. Mixing beliefs among 550 interacting agents. Advances in Complex Systems, 3(01n04):87–98, 2000. 551 Jinyuan Fang, Yanwen Peng, Xi Zhang, Yingxu Wang, Xinhao Yi, Guibin Zhang, Yi Xu, Bin Wu, 552 Siwei Liu, Zihao Li, et al. A comprehensive survey of self-evolving ai agents: A new paradigm 553 bridging foundation models and lifelong agentic systems. arXiv preprint arXiv:2508.07407, 2025. 554 555 Jie Feng, Yong Li, Chao Zhang, Funing Sun, Fanchao Meng, Ang Guo, and Depeng Jin. DeepMove: 556 Predicting Human Mobility with Attentional Recurrent Networks. In Proceedings of the 2018 557 World Wide Web Conference on World Wide Web - WWW ’18, pp. 1459–1468, Lyon, France, 558 2018. ACM Press. ISBN 978-1-4503-5639-8. doi: 10.1145/3178876.3186058. URL http: //dl.acm.org/citation.cfm?doid=3178876.3186058. 559 560 Jie Feng, Can Rong, Funing Sun, Diansheng Guo, and Yong Li. Pmf: A privacy-preserving human 561 mobility prediction framework via federated learning. Proceedings of the ACM on Interactive, 562 Mobile, Wearable and Ubiquitous Technologies, 4(1):1–21, 2020. 563 Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. Agentmove: Predicting human mobility anywhere using 564 large language model based agentic framework. arXiv preprint arXiv:2408.13986, 2024. 565 566 Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. Agentmove: A large language model based agentic 567 framework for zero-shot next location prediction, 2025. URL https://arxiv.org/abs/ 568 2408.13986. 569 Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, 570 and Yong Li. S3: Social-network simulation system with large language model-empowered agents. 571 arXiv preprint arXiv:2307.14984, 2023. 572 573 Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and Yong 574 Li. Large language models empowered agent-based modeling and simulation: A survey and 575 perspectives. Humanities and Social Sciences Communications, 11(1):1–24, 2024. 576 Dawei Gao, Zitao Li, Yuexiang Xie, Weirui Kuang, Liuyi Yao, Bingchen Qian, Zhijian Ma, Yue 577 Cui, Haohao Luo, Shen Li, Lu Yi, Yi Yu, Shiqi He, Zhiling Luo, Wenmeng Zhou, Zhicheng 578 Zhang, Xuguang He, Ziqian Chen, Weikai Liao, Farruh Isakulovich Kushnazarov, Yaliang Li, 579 Bolin Ding, and Jingren Zhou. Agentscope 1.0: A developer-centric framework for building 580 agentic applications, 2025. URL https://arxiv.org/abs/2508.16279. 581 Santiago Garcia-Gabilondo, Yuya Shibuya, and Yoshihide Sekimoto. Enhancing geospatial retail 582 analysis by integrating synthetic human mobility simulations. Computers, Environment and Urban 583 Systems, 108:102058, 2024. 584 585 Zhenyu Han, Fengli Xu, Yong Li, Tao Jiang, and James Evans. Model predicted human mobility 586 explains covid-19 transmission in urban space without behavioral data. Scientific Reports, 15(1): 587 6365, 2025. 588 Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang, 589 Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. Metagpt: Meta programming for multi-agent 590 collaborative framework. arXiv preprint arXiv:2308.00352, 2023a. 591 592 Ye Hong, Yatao Zhang, Konrad Schindler, and Martin Raubal. Context-aware multi-head selfattentional neural network model for next location prediction. Transportation Research Part C: 593 Emerging Technologies, 156:104315, 2023b. 11 Under review as a conference paper at ICLR 20 594 John J Horton. Large language models as simula 595 silicus? Technical report, National Bureau of 596 Siqi Lai, Zhao Xu, Weijia Zhang, Hao Liu, and 597 control agents: Capacity and opportunity. arX 598 599 Nian Li, Chen Gao, Mingyu Li, Yong Li, and 600 empowered agents for simulating macroecon 601 Meeting of the Association for Computationa 602 15536, 2024. 603 Thorsten Neumann, Matthias Heinrichs, Michae 604 Biebl. Quantitative analysis of future scenario 605 case study. Transportation Research Procedi 606 607 Joon Sung Park, Joseph O’Brien, Carrie Jun Cai, 608 Bernstein. Generative agents: Interactive simu annual acm symposium on user interface soft 609 610 Jinghua Piao, Yuwei Yan, Nian Li, Jun Zhang, a 611 for piloting social experiments, 2025a. URL 612 Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li, 613 Zheng, Jing Yi Wang, Di Zhou, Chen Gao, Fe 614 Agentsociety: Large-scale simulation of llm615 human behaviors and society, 2025b. URL h 616 617 Giorgio Piatti, Zhijing Jin, Max Kleiman-Weine 618 Mihalcea. Cooperate or collapse: Emergen 619 agents. In The Thirty-eighth Annual Conferen URL https://openreview.net/foru 620 621 Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen 622 Yusheng Su, Xin Cong, et al. Chatdev: Co 623 Proceedings of the 62nd Annual Meeting of th 624 1: Long Papers), pp. 15174–15186, 2024. 625 Yanjun Qin, Yuchen Fang, Haiyong Luo, Fang 626 recommendation with auto-correlation enhanc 627 of the 45th International ACM SIGIR Confer 628 Retrieval, pp. 2612–2616, 2022. 629 630 Steffen Rendle, Christoph Freudenthaler, and Lar 631 chains for next-basket recommendation. In P World Wide Web, pp. 811–820, 2010. 632 633 Thomas C Schelling. Dynamic models of seg 634 143–186, 1971. 635 Chenyang Shao, Fengli Xu, Bingbing Fan, Jin 636 Beyond imitation: Generating human mobilit 637 models. arXiv preprint arXiv:2402.09836, 20 638 639 Chenyang Shao, Fengli Xu, Bingbing Fan, Jin 640 Chain-of-planned-behaviour workflow elicits 641 https://arxiv.org/abs/2402.098 642 Yunfan Shao, Linyang Li, Junqi Dai, and Xipe 643 playing. In Proceedings of the 2023 Confer 644 Processing, pp. 13153–13187, 2023. 645 646 Nicholas Sukiennik, Yichuan Xu, Yuqing Kan, The roots of international perceptions: Simu 647 agents, 2025. URL https://arxiv.org economic agents: What can we learn from homo onomic Research, 2023. Xiong. Large language models as traffic signal preprint arXiv:2312.16044, 2023. gmin Liao. Econagent: large language modelc activities. In Proceedings of the 62nd Annual nguistics (Volume 1: Long Papers), pp. 15523– ehrisch, Jakob Erdmann, and Anke Sauerla¨nderf urban mobility using agent-based simulation–a 1:295–308, 2019. redith Ringel Morris, Percy Liang, and Michael S a of human behavior. In Proceedings of the 36th e and technology, pp. 1–22, 2023. Yong Li. Exploring large language model agents tps://arxiv.org/abs/2508.08678. bo Yan, Xiaochong Lan, Zhihong Lu, Zhiheng Xu, Fang Zhang, Ke Rong, Jun Su, and Yong Li. en generative agents advances understanding of ps://arxiv.org/abs/2502.08691. ernhard Scho¨lkopf, Mrinmaya Sachan, and Rada f sustainable cooperation in a society of LLM n Neural Information Processing Systems, 2024. id=0zWzJj6lO3. ufan Dang, Jiahao Li, Cheng Yang, Weize Chen, unicative agents for software development. In sociation for Computational Linguistics (Volume ao, and Chenxing Wang. Next point-of-interest multi-modal transformer network. In Proceedings e on Research and Development in Information chmidt-Thieme. Factorizing personalized markov eedings of the 19th International Conference on tion. Journal of mathematical sociology, 1(2): o Ding, Yuan Yuan, Meng Wang, and Yong Li. om context-aware reasoning with large language . o Ding, Yuan Yuan, Meng Wang, and Yong Li. w-shot mobility generation in llms, 2024b. URL Qiu. Character-llm: A trainable agent for rolee on Empirical Methods in Natural Language ghua Piao, Yuwei Yan, Chen Gao, and Yong Li. ng us attitude changes towards china with llm bs/2508.08837. Under review as a conference paper at ICLR 20 648 Hugo Touvron, Thibaut Lavril, Gautier Izacard 649 Lacroix, Baptiste Rozie`re, Naman Goyal, E 650 efficient foundation language models. arXiv p 651 Jiawei Wang, Renhe Jiang, Chuang Yang, Zen 652 Noboru Koshizuka, and Chuan Xiao. Large 653 framework for personal mobility generation. A 654 37:124547–124574, 2024a. 655 656 Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhan Tang, Xu Chen, Yankai Lin, Wayne Xin Z 657 large language model based autonomous age 658 2024b. ISSN 2095-2236. doi: 10.1007/s117 659 10.1007/s11704-024-40231-1. 660 661 Lei Wang, Heyang Gao, Xiaohe Bo, Xu Chen, 662 generation of social simulator with large langu 663 abs/2505.07581. 664 Xinglei Wang, Meng Fang, Zichao Zeng, and Tao 665 els as human mobility predictors, 2024c. UR 666 Xingrui Wang, Xinyu Liu, Ziteng Lu, and Hanf 667 Using Map Based on Two Stage GAN. Jo 668 1680-743X, 1683-8602. doi: 10.6339/21-JDS1 669 10.6339/21-JDS1004. 670 671 Hao WU, Ziyang CHEN, Weiwei SUN, Baihu 672 with recurrent neural networks.(2017). In Pro 673 on Artificial Intelligence IJCAI-17, Melbourn 674 Lin Xu, Zhiyuan Hu, Daquan Zhou, Hongyu R 675 Jiashi Feng. MAgIC: Investigation of large 676 adaptability, rationality and collaboration. I 677 Chen (eds.), Proceedings of the 2024 Confe 678 Processing, Miami, Florida, USA, November 679 Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, 680 memory for llm agents. arXiv preprint arXiv: 681 682 Yuwei Yan, Qingbin Zeng, Zhiheng Zheng, Jing 683 Li. Opencity: A scalable platform to simula preprint arXiv:2410.21286, 2024. 684 685 An Yang, Anfeng Li, Baosong Yang, Beichen Z 686 Gao, Chengen Huang, Chenxu Lv, Chujie Zh 687 Hao Ge, Haoran Wei, Huan Lin, Jialong Tan 688 Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou, 689 Le Yu, Lianghao Deng, Mei Li, Mingfeng Xu 690 Men, Ruize Gao, Shixuan Liu, Shuang Luo, Ren, Xinyu Wang, Xinyu Zhang, Xuancheng 691 Zhang, Yu Wan, Yuqiong Liu, Zekun Wang, 692 Qiu. Qwen3 technical report, 2025. URL ht 693 694 Hui Yang, Sifu Yue, and Yunzhong He. Auto 695 additional opinions. arXiv preprint arXiv:230 696 Yuan Yuan, Jingtao Ding, Huandong Wang, Dep 697 via modeling spatiotemporal dynamics. In Pr 698 Knowledge Discovery and Data Mining, pp. 4 699 700 Jun Zhang, Wenxuan Ao, Junbo Yan, Depeng simulator for transportation system optimizati 701 2024a. avier Martinet, Marie-Anne Lachaux, Timothe´e Hambro, Faisal Azhar, et al. Llama: Open and rint arXiv:2302.13971, 2023. ng Wu, Makoto Onizuka, Ryosuke Shibasaki, guage models as urban residents: An llm agent ances in Neural Information Processing Systems, Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai , Zhewei Wei, and Jirong Wen. A survey on . Frontiers of Computer Science, 18(6), March 024-40231-1. URL http://dx.doi.org/ Ji-Rong Wen. Yulan-onesim: Towards the next models, 2025. URL https://arxiv.org/ eng. Where would i go next? large language modttps://arxiv.org/abs/2308.15197. Yang. Large Scale GPS Trajectory Generation al of Data Science, pp. 126–141, 2021. ISSN 4. URL https://jds-online.org/doi/ HENG, and Wei WANG. Modeling trajectories dings of the 26th International Joint Conference ustralia, August 19, volume 25, pp. 3083–3090. Zhen Dong, Kurt Keutzer, See-Kiong Ng, and guage model powered multi-agent in cognition, aser Al-Onaizan, Mohit Bansal, and Yun-Nung ce on Empirical Methods in Natural Language 24. Association for Computational Linguistics. ao Tan, and Yongfeng Zhang. A-mem: Agentic 2.12110, 2025. Yuan, Jie Feng, Jun Zhang, Fengli Xu, and Yong urban activities with massive llm agents. arXiv ng, Binyuan Hui, Bo Zheng, Bowen Yu, Chang , Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu, ian Yang, Jianhong Tu, Jianwei Zhang, Jianxin nyang Lin, Kai Dang, Keqin Bao, Kexin Yang, Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui nhao Li, Tianyi Tang, Wenbiao Yin, Xingzhang en, Yang Fan, Yang Su, Yichang Zhang, Yinger u Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan s://arxiv.org/abs/2505.09388. for online decision making: Benchmarks and 2224, 2023. Jin, and Yong Li. Activity trajectory generation edings of the 28th ACM SIGKDD Conference on 2–4762, 2022. , and Yong Li. A gpu-accelerated large-scale benchmarking. arXiv preprint arXiv:2406.10661, Under review as a conference paper at ICLR 2026 702 Jun Zhang, Wenxuan Ao, Junbo Yan, Can Rong, Depeng Jin, Wei Wu, and Yong Li. Moss: A 703 large-scale open microscopic traffic simulation system. arXiv preprint arXiv:2405.12520, 2024b. 704 705 Jun Zhang, Yuwei Yan, Junbo Yan, Zhiheng Zheng, Jinghua Piao, Depeng Jin, and Yong Li. A parallelized framework for simulating large-scale LLM agents with realistic environments and 706 interactions. In Georg Rehm and Yunyao Li (eds.), Proceedings of the 63rd Annual Meeting 707 of the Association for Computational Linguistics (Volume 6: Industry Track), pp. 1339–1349, 708 Vienna, Austria, July 2025a. Association for Computational Linguistics. ISBN 979-8-89176709 288-6. doi: 10.18653/v1/2025.acl-industry.94. URL https://aclanthology.org/2025. 710 acl-industry.94/. 711 712 Jun Zhang, Yuwei Yan, Junbo Yan, Zhiheng Zheng, Jinghua Piao, Depeng Jin, and Yong Li. A 713 parallelized framework for simulating large-scale llm agents with realistic environments and interactions. In Proceedings of the 63rd Annual Meeting of the Association for Computational 714 Linguistics (Volume 6: Industry Track), pp. 1339–1349, 2025b. 715 716 Zeyu Zhang, Quanyu Dai, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Jieming Zhu, Zhenhua Dong, and 717 Ji-Rong Wen. A survey on the memory mechanism of large language model-based agents. ACM 718 Transactions on Information Systems, 43(6):1–47, 2025c. 719 Qinlin Zhao, Jindong Wang, Yixuan Zhang, Yiqiao Jin, Kaijie Zhu, Hao Chen, and Xing Xie. 720 Competeai: Understanding the competition dynamics in large language model-based agents, 2024. 721 URL https://arxiv.org/abs/2310.17512. 722 723 Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min, 724 Beichen Zhang, Junjie Zhang, Zican Dong, et al. A survey of large language models. 725 Kunlun Zhu, Hongyi Du, Zhaochen Hong, Xiaocheng Yang, Shuyi Guo, Zhe Wang, Zhenhailong 726 Wang, Cheng Qian, Robert Tang, Heng Ji, and Jiaxuan You. MultiAgentBench : Evaluating 727 the collaboration and competition of LLM agents. In Wanxiang Che, Joyce Nabende, Ekaterina 728 Shutova, and Mohammad Taher Pilehvar (eds.), Proceedings of the 63rd Annual Meeting of the 729 Association for Computational Linguistics (Volume 1: Long Papers), Vienna, Austria, July 2025. 730 Association for Computational Linguistics. 731 732 733 734 735 736 737 738 739 740 741 742 743 744 745 746 747 748 749 750 751 752 753 754 755 14 Under review as a conference paper at ICLR 2026 756 A APPENDIX 757 758 A.1 THE USE OF LARGE LANGUAGE MODELS 759 760 In this work, the use of LLMs is limited to checking for grammatical errors and providing word 761 suggestions. 762 763 A.2 OVERALL SUBMISSION STATUS 764 765 Table 4: Summary of competition participation. 766 767 768 task # of Teams # of Agents Submitted # of Agents Evaluated 769 Daily mobility 10 362 361 770 Hurricane mobility 8 605 572 771 Total 18 967 933 772 773 774 775 A.3 AN EXAMPLE OF NARRATIVE GENERATED FROM THE BEST-PERFORMING 776 LLM-DOMINATED AGENT IN THE DAILY MOBILITY TASK 777 778 I woke up around 7:45 AM to the sound of my phone buzzing on the nightstand—same 779 old alarm, same tired feeling. My apartment in Haidian (that’s location ID 500063798 for 780 whatever system needs that) is cozy but nothing fancy: IKEA furniture, a desk buried under 781 cables and old coffee mugs, and a window that looks out onto a row of elm trees and the 782 back of a convenience store. I lay there for a few minutes scrolling through WeChat—family 783 group messages from my mom asking if I’ve eaten properly, a couple memes from my college 784 buddies, and a work Slack ping reminding me about today’s sprint review. 785 By 8:10, I dragged myself out of bed. Quick shower, face wash, toothbrush dance—I keep it 786 simple. Breakfast was instant oatmeal with a banana and black tea, all while half-watching a 787 tech podcast on my laptop. I hate mornings, but at least Beijing’s autumn air is finally cooling 788 down. No more sweltering subway rides. 789 790 Left the house at 8:50, walked five minutes to Wudaokou Station. Took Line 13 toward Zhichunlu, then switched to Line 10. The commute’s predictable—packed cars, people 791 reading novels or napping standing up, someone always blasting music by accident. Got off at 792 Suzhoujie Station (close enough to office ID 500059965), then a ten-minute walk through that 793 narrow street lined with bubble tea shops and repair stalls. 794 795 Reached the office around 9:25. Clock in, hang up my jacket, refill my thermos with hot water. 796 Team meeting started at 9:30—we’re wrapping up this backend migration, so I gave a quick 797 update on the API refactoring I’ve been grinding on. Then it was heads-down coding until 798 lunch. Debugged a race condition in the user auth module—stupid typo in a timeout config. Felt dumb, but hey, at least it wasn’t in production. 799 800 Lunch was at 12:30. Me and three other guys from the team hit that hand-pulled noodle 801 place across the street—*Lanzhou Lamian*, yellow signs, cheap and filling. Beef soup, 802 extra cilantro, chili oil on the side. We talked about everything except work: someone’s new 803 apartment, the PS5 price hike, whether China will ever get decent sci-fi movies outside of 804 *The Wandering Earth*. Back to the office by 1:15. 805 Afternoon was lighter—code review for a junior dev, updated some documentation (ugh), and 806 fixed a minor UI glitch on the internal dashboard. Took a 20-minute break around 4:00 to walk 807 around the block and grab a soy milk and steamed bun from the old lady’s cart near the park 808 entrance. Autumn sunlight felt good on my face. 809 15 Under review as a conference paper at ICLR 2026 810 811 Wrapped up around 6:45. Manager didn’t push for overtime, which I appreciated—we’re not 812 crunching yet. Left the office by 7:00. Instead of going straight home, swung by the Carrefour 813 Express near Wudaokou Square. Picked up tofu, bok choy, instant ramen (for emergencies), a 814 bottle of soy sauce, and a liter of beer—just one, because I’m not trying to become “that guy” 815 with a fridge full of empties. 816 Got home around 7:45. Changed into sweatpants, put on some lo-fi beats. Cooked a quick 817 stir-fry with what I had—garlic, tofu, greens—and poured the beer into a glass. Ate while 818 watching an episode of *Line of Duty* dubbed in Mandarin. Not the same without the accents, 819 but it passes the time. 820 Around 9:30, I opened my notebook and sketched out some ideas for a personal project—a 821 habit-tracking app with minimalist design. Nothing serious, just something to tinker with on 822 weekends. Then browsed Zhihu for half an hour, reading rants about AI replacing programmers 823 (again). 824 825 Showered again—sweat from the commute still clinging—and brushed my teeth. Checked my 826 phone one last time: no urgent messages, weather says tomorrow will be partly cloudy. Set the 827 alarm for 7:50. Lights out by 11:20. 828 As I drifted off, I thought: *Another day, another thousand lines of code nobody will ever see.* 829 But hey—at least the noodles were good. 830 831 832 B FORMULAS FOR EVALUATION METRICS 833 834 B.1 DAILY MOBILITY SIMULATION METRICS 835 836 The Jensen–Shannon Divergence (JSD) is defined as: 837 JSD(P ∥ Q) = 1 KL(P ∥ M ) + 1 KL(Q ∥ M ), M = 1 (P + Q), 838 2 2 2 839 where P and Q denote the probability distributions of generated and real-world data, respectively, 840 and KL(· ∥ ·) is the Kullback–Leibler divergence. 841 The aggregated Final Score is defined as: 842 843 (cid:18) (1 − JSD ) + (1 − JSD ) + (1 − JSD ) + (1 − JSD ) (cid:19) Final Score = gyr loc seq prop × 100. 844 4 845 846 B.2 HURRICANE MOBILITY SIMULATION METRICS 847 848 The mean absolute percentage error (MAPE) and the Change Rate Score are given by: 849 |Real Change Rate − Generated Change Rate| 850 MAPE = × 100%, |Real Change Rate| 851 852 Change Rate Score = max (cid:0) 0, 100 − Average MAPE (cid:1) . 853 854 The cosine similarity and the Distribution Score are defined as: 855 A · B 856 Cosine Similarity(A, B) = , ∥A∥ × ∥B∥ 857 (cid:0) (cid:1) 858 Distribution Score = max 0, Average Cosine Similarity × 100 . 859 860 The weighted final score is: 861 Final Score = 0.6 × Change Rate Score + 0.4 × Distribution Score. 862 863 16

## Outline

- Introduction (page 1)
- Evaluation Framework (page 3)
  - Robustness (page 3)
  - Realism (page 3)
  - Responsiveness (page 4)
- MobiSim-Bench (page 4)
  - Benchmark Overview (page 4)
  - Daily Mobility Simulation (page 5)
  - Hurricane Mobility Simulation (page 6)
- Experiments (page 6)
  - Baselines (page 7)
  - Results (page 8)
  - Discussion (page 8)
- Related Work (page 9)
  - Mobility Simulation (page 9)
  - LLM Agent Simulation Benchmark (page 9)
- Conclusion (page 9)
- Appendix (page 15)
  - The Use of Large Language Models (page 15)
  - Overall submission status (page 15)
  - An example of narrative generated from the best-performing LLM-dominated agent in the Daily Mobility task (page 15)
- Formulas for Evaluation Metrics (page 16)
  - Daily Mobility Simulation Metrics (page 16)
  - Hurricane Mobility Simulation Metrics (page 16)

## Markdown Content

Under review as a conference paper at ICLR 2026
000 MOBISIM-BENCH: A MULTI-PERSPECTIVE BENCH001
002 MARK FOR EVALUATING LLM-AGENT-BASED HUMAN
003
MOBILITY SIMULATION
004
005
006
Anonymous authors
007
Paper under double-blind review
008
009
010
ABSTRACT
011
012
With advances in large language models (LLMs) and agent technology, LLM
013
agents are transforming social science research on human behavior simulation with
014
their powerful role-playing capabilities. Among the simulation studies on complex
015
human behaviors, mobility behavior simulation has been receiving widespread
016
attention and has important implications for real-world applications. Unlike data017 driven statistical learning approaches, LLM agent-based simulation methods have
018 the potential to support all-day simulation and generation of human mobility be019 haviors or even simulation of adaptive changes in the environment in extraordinary
020 scenarios. To evaluate the performance of LLM agents for human mobility be021 havior simulation from multiple perspectives and in a holistic manner, we first
022 propose an evaluation framework, which contains three perspectives: Robustness, Realism, and Responsiveness. To implement the evaluation framework,
023
we construct and publish a multi-perspective benchmark named MobiSim-Bench
024
based on the AgentSociety simulation framework. The benchmark contains the
025
Daily Mobility Simulation mainly for evaluating realism and the Hurricane
026
Mobility Simulation mainly for evaluating responsiveness. Based on this bench027
mark, we organized a challenge with 18 teams to collect and evaluate LLM agents
028 designed by different researchers. In this challenge, 967 agents were deployed.
029 The agent design approach using LLM as the brain achieves the optimum in
030 terms of realism, while the LLM as an extra is more suitable for the responsive
031 scenario. The results show that our evaluation framework and benchmark do
032 examine the performance of LLM agent for simulating human behavior from
033 different perspectives, and on the other hand, they also reveal the shortcomings
of the existing LLM agent designs, which will drive the research community to
034
further explore the LLM agent design approaches that can satisfy robustness, re035
alism and responsiveness simultaneously. The benchmark codes are available at
036
https://anonymous.4open.science/r/MobiSim-Bench-1077/.
037
038
039 1 INTRODUCTION
040
041 With the development of large language modeling (LLM) (Brown et al., 2020; Touvron et al., 2023;
042 Zhao et al.) and LLM agent technology (Wang et al., 2024b; Fang et al., 2025), LLM agents have
043 not only reshaped the way of working in fields such as programming (Hong et al., 2023a; Yang
044 et al., 2023; Qian et al., 2024), but also changed the paradigm of social science research about
045 the simulation of human behaviors (Park et al., 2023; Gao et al., 2023; Li et al., 2024) with their
046 powerful role-playing capabilities (Shao et al., 2023; Chen et al., 2024). LLM agents inherit the idea
of agent-based modeling (ABM) (Schelling, 1971; Deffuant et al., 2000) and replace the agents from
047
manually formulated rules to LLMs that can simulate the logic of complex human behaviors (Gao
048
et al., 2024), which have been successful in the fields of mobility behavior simulation (Shao et al.,
049
2024a; Feng et al., 2024; Yan et al., 2024), social simulation (Gao et al., 2023; Park et al., 2023),
050
economic simulation (Horton, 2023; Li et al., 2024), etc.
051
052 Among the simulation studies of complex human behaviors, mobility behavior simulation has been
receiving extensive attention (WU et al.; Zhang et al., 2024b; Feng et al., 2024). Accurate simulation
053
of human mobility behavior patterns is of vital importance for urban planning (Neumann et al.,
1

Under review as a conference paper at ICLR 2026
054
2019), traffic management (Zhang et al., 2024a), epidemic control (Han et al., 2025), business
055 decisions (Garcia-Gabilondo et al., 2024), etc. From a technical point of view, the LLM agent-based
056 human mobility behavior simulation approach models individual behaviors from the first principle in
057 a way that can overcome the shortcomings of data-driven statistical learning predictive models (Feng
058 et al., 2018; Chen et al., 2020) or generative models (Wang et al., 2021; Yuan et al., 2022) that can
059 only restore the macroscopic distribution. Unlike predictive or generative models, the step-by-step
060 simulation approach (Zhang et al., 2025b) not only embodies the interaction between humans and
urban infrastructures, such as road networks, to reflect physical law constraints and thus ensures
061
realism from the microscopic perspective, but also captures the complex intentions and scenario
062
adaptations behind the behaviors through the LLM reasoning process in the simulation. However,
063
existing works (Wang et al., 2024a; Feng et al., 2024) on predicting or simulating human mobility
064
behaviors based on LLM agents still continue the research ideas of statistical learning models, with
065
next-location prediction or trajectory generation as the main research question. They fail to focus
066 on the fact that the LLM agent’s role-playing ability with human common sense understanding and
067 reasoning has the potential to support all-day simulation of human mobility behaviors as well as the
068 simulation of adaptive changes in the environment in extraordinary scenarios. Therefore, we believe
069 that long time scale simulation on the day level and different external environment effects are the key
070 to test whether the LLM agents are capable of performing the mobility simulation task and generating
071 highly realistic human mobility behaviors. At the same time, the evaluation of the simulation results
should also go deeper from the macro-distribution statistics to the behavioral intention level.
072
073 To achieve this, we propose an evaluation framework for comprehensively evaluating the LLM agent’s
074 simulated human mobility behaviors from multiple perspectives as follows:
075
• Robustness: First of all, as the most basic requirement, the LLM agents should be able to
076
complete long time-scale mobility simulations for a day or even longer without errors.
077
• Realism: Second, simulation results based on LLM agents should approximate real-world human
078
data in terms of microscopic intentions and macroscopic statistical metrics.
079
• Responsiveness: Unlike data-driven modeling approaches, LLM agent-driven simulation ap080
proaches have advanced thinking and reasoning capabilities and should be able to show respon081
siveness to different external environmental changes.
082
Based on this evaluation framework, we construct and publish a multi-perspective benchmark named
083
MobiSim-Bench to advance the research related to the simulation of human mobility behaviors
084
using LLM agents. MobiSim-Bench consists of two day-level long time-scale simulation tasks,
085
Daily Mobility Simulation under normal conditions and Hurricane Mobility Simulation under
086
abnormal conditions. To build the two tasks, we collected real-world mobility data, constructed the
087
agent profiles and map data used for initializing agents for the simulation tasks. The real human
088 behaviors were extracted as ground truth for evaluation. In terms of evaluation methods, we not
089 only include common macroscopic statistical distribution metrics, but also further add individual
090 behavioral intention determination. For the hurricane scenario, we also design behavioral change
091 metrics to evaluate the adaptability of the agents. Overall, MobiSim-Bench fully evaluates the realism
092 of LLM-agent-based human mobility simulation in terms of microscopic intentions and macroscopic
093 statistical metrics from both normal and abnormal scenarios, and also examines the environmental
adaptability under the impacts of external environmental changes, which realizes a multi-perspective
094
evaluation of long-scale human mobility simulation.
095
096 We organized a competition based on our benchmark and collected LLM agents constructed by human
097 experts. A total of 18 teams participated in the competition, submitting 967 agent implementations.
098 We systematically classified all submitted methods into three categories based on the role of LLMs in
099 the agent architecture: LLM as Brain, LLM as Glue, and LLM as Extra. These specially designed
agents achieved peak scores of 66.38 in the Daily Mobility task and 85.63 in the Hurricane Mobility
100
task. These competitive outcomes confirm that MobiSim-Bench enables rigorous evaluation of diverse
101
agent design paradigms and validates our multi-dimensional framework for measuring robustness,
102
realism, and responsiveness in long-term mobility simulations.
103
104 Overall, the main contributions of this paper are listed as follows:
105
• We propose an evaluation framework for comprehensively evaluating the LLM agent’s simulated
106 human mobility behaviors from robustness, realism, and responsiveness.
107
2

Under review as a conference paper at ICLR 20
108
• We construct and publish a multi-perspective
109 Mobility Simulation task under normal cond
110 under abnormal conditions for benchmarkin
111 • We organized a competition to collect, qua
112 ferent teams with different design paradigm
113 corresponding baselines.
114
115
2 EVALUATION FRAMEWORK
116
117
Introducing LLM agents to simulate human b
118
role-playing, understanding, and reasoning cap
119
generative algorithms driven by data and statis
120 agents provide us with a window to simultaneo
121 outcomes, while also possessing the potential to
122
Given these differences, relying solely on statist
123
evaluate LLM agents has become inadequate. Th
124
comprising three key elements as shown in F
125
potential of LLM agents: Robustness, Realism
126 capabilities required for an LLM agent to simul
127 evaluation metrics.
128
129
2.1 ROBUSTNESS
130
131 Robustness is the most fundamental require132 ment for LLM agents. Unlike statistical learning
133 models that take fully standardized inputs and
134 also produce standardized output matrices, LLM
agents directly handle diverse inputs. These in135
puts include predefined character profiles and
136
external commands, as well as callable functions
137
and even program errors encountered during ex138
ecution. LLM agents are required to correctly
139
handle all situations and continue simulation
140 with any inputs. This requires the agents to be
141 able to follow instructions to conduct simula142 tions, while also correctly utilizing functions
143 through structured output or function call capa144 bilities. Retry mechanisms and fallbacks will
145 prevent the program from crashing in the event
of an LLM error. After ensuring the program
146
simulates normally, the agent’s ability to main147
tain context during day-level long-term simula148
tions will prevent absurd outcomes, such as contin
149
et al., 2025c) serves as the primary solution to t
150
151 Currently, with the advancement of LLM cap
frameworks (Gao et al., 2025; Zhang et al., 2
152
mechanisms to build the aforementioned capabi
153
for LLM agents like mem0 (Chhikara et al., 2025
154
reduced the complexity of designing memory m
155
156 The evaluation of robustness is relatively straig
157 can complete the simulation without crashing. A
158
159 2.2 REALISM
160
Realism represents a further requirement that i
161
human mobility behavior. In human mobility be

nchmark named MobiSim-Bench with the Daily
ns and the Hurricane Mobility Simulation task
atively evaluate, and compare agents from difn mobility simulation scenarios, and provided
vior will release the high potential of LLMs’
ities in this research field. Unlike prediction or
learning models, step-by-step simulated LLM
observe behavioral motivations and behavioral
pond to environmental changes.
distributions of simulated mobility behaviors to
we propose a hierarchical evaluation framework
e 1 based on the technical characteristics and
nd Responsiveness. Each element reflects the
human mobility behavior and the corresponding
Responsiveness
Realism
obustness
gure 1: A hierarchical framework for evaluating
LM agents that simulate human mobility behavrs.
usly going out to eat. Memory mechanism (Zhang
problem.
ities and the maturation of agent development
5a), researchers can easily adopt their built-in
s and create an agent program. Memory systems
d A-MEM (Xu et al., 2025) have also significantly
les.
orward: it involves observing whether the agent
agent that crashes will be vetoed outright.
posed on LLM agents in the task of simulating
or simulation tasks, LLM agents are tasked with

Under review as a conference paper at ICLR 20
162
playing the role of individuals possessing speci
163 within a virtual city. This will evaluate the rol
164 whether they can perform travel behaviors cons
165 commuting to school or a white-collar worker he
166 ability to understand and apply human societal co
167 sleep schedules, commuting habits, and dining p
168 can realistically simulate human mobility. Plann
long-duration simulations to ensure that moveme
169
reasonable.
170
171 The evaluation of realism can continue to utilize
172 from prediction and generation tasks (Feng et a
173 distribution and gyration radius distribution simi
174 cesses of LLM agents can be observed by resear
recording and evaluation of micro-level behavio
175
whether LLM agents truly think and act like hum
176
177
178
2.3 RESPONSIVENESS
179
Responsiveness is the key to surpassing statis
180
simulate human mobility behavior. Statistical le
181 distributions to achieve generalization, renderin
182 scenarios. The powerful understanding provid
183 receive and process natural language descriptio
184 Leveraging the built-in knowledge and reason
185 transform these descriptions into adaptive actio
186 adaptation process, expert knowledge helps th
environmental changes and implicitly suggests tr
187
the agent’s decision-making preferences, making
188
Reflective capabilities primarily focus on whethe
189
based on factors like external environmental shi
190
191 For the evaluation of adaptability, we suggest fo
192 before and after external environmental changes
could involve computing the similarity in the dis
193
changes.
194
195
In summary, the proposed framework for assessin
196
a step-by-step standard for evaluating the perfo
197 human mobility behavior. This framework facili
198 simulation from statistical fitting toward unde
199 avenues for exploring human movement pattern
200
201
3 MOBISIM-BENCH
202
203
3.1 BENCHMARK OVERVIEW
204
205 To implement the proposed evaluation framew
206 siveness of LLM agents, we introduce a multi-p
207 benchmark consists of two tasks: Daily Mobilit
208 Both tasks are designed to evaluate LLM agent
under different contextual conditions. The daily m
209
of Realism, as it focuses on capturing routine, ev
210
simulated outputs can approximate real-world hu
211
levels. In contrast, the hurricane mobility simula
212
it targets behavioral changes and adaptive respo
213
whether LLM agents can dynamically adjust to
214
As illustrated in Figure 2, the entire framework c
215
ground-truth trajectories and user profiles are i

rofiles and self-determining their travel choices
aying capabilities of LLM agents, specifically
nt with a given profile, such as a student always
ng to an office building. At the same time, LLMs’
mon sense and routine behavioral patterns, such as
rences, will also determine whether LLM agents
capabilities are also essential when dealing with
ehaviors throughout the day remain relevant and
mmon macro-level statistical distribution metrics
018; Yuan et al., 2022), such as check-in count
y metrics. Furthermore, since the reasoning pros through natural language, we can introduce the
ntentions. This will help researchers understand
s.
l learning models when using LLM agents to
ng models rely entirely on the similarity of data
em useless when facing rare out-of-distribution
by LLMs to agents will enable these agents to
f environmental changes in abnormal situations.
capabilities of LLMs, they have the ability to
n response to environmental shifts. During this
gent fully comprehend the impacts of external
plans. Emotions such as panic and fear reinforce
m more aligned with real-world human behavior.
e agent can re-plan and alter travel arrangements
expert knowledge, and its own emotional state.
ng on whether the differences in travel behavior
gn with real-world conditions. For instance, this
ution of travel time changes before and after the
bustness, realism, and responsiveness establishes
ance and potential of LLM agents in simulating
s the transition of research paradigms in mobility
nding-based behavior modeling, opening new
thin complex dynamic environments.
to evaluate the robustness, realism, and responective benchmark named MobiSim-Bench. The
mulation and Hurricane Mobility Simulation.
the domain of human mobility simulation, but
ility simulation is primarily aligned with the goal
day urban travel behaviors and assessing whether
n mobility at both microscopic and macroscopic
is closely tied to the goal of Responsiveness, as
s during extreme weather events, thereby testing
den environmental perturbations.
ists of three stages: (i) Data Preparation, where
rated with urban networks (for Daily Mobility)

Under review as a conference paper at ICLR 2026
216
217
218 Daily Mobility
GT
219 Ground Truth
220 Trajectories with Intentions Gen
221 Demographic
222 Profile, work and home
Agent Init
223 Environment
224 Urban network of Beijing
225 Sim Init
Environment
226
• Columbia Map Simulation Engine GT
227 Demographic Sunny Hurricane Cloudy Gen
228
Profile, work and home
229
230 Ground Truth
Travel Statistics during HC
231
Time Sequence
232 Hurricane Mobility Evaluation
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
269
tnuomAlevarT
Step1 Preparation Step2 Simulation Step3 Evaluation
Realism
Robustness
MICRO S In e t q e u n e ti n o c n e P I r n o t p en o t r i t o io n n
MACRO G R y a r d at iu io s n L N o u c m at b io e n r
Output
Responsiveness
• Weather Info
Weather Change
Change Rate Travel Distribution
Figure 2: Overview of the MobiSim-Bench.
or hurricane-related maps and census statistics (for Hurricane Mobility); (ii) Simulation, where
agents are initialized with demographic and environmental inputs and executed within the built-in
mobility engine of AgentSociety (Piao et al., 2025b; Zhang et al., 2025a); this engine performs
first-principles simulations at a temporal resolution of 1 second, allowing agents to move through
explicit function calls that translate intentions into concrete actions, thereby constructing complete
mobility trajectories; (iii) Evaluation, where the generated behaviors are compared against real-world
data, with Daily Mobility metrics (gyration radius, location number, intention sequence, intention
proportion) assessing Realism, and Hurricane Mobility metrics (change rate, temporal distribution of
travel) assessing Responsiveness.
3.2 DAILY MOBILITY SIMULATION
Task Definition: The simulation requires each agent to generate temporally ordered intentions
and corresponding actions that are consistent with user characteristics and the surrounding urban
environment. The inputs include user demographic profiles, city-level geographic and transportation
information, and daily time constraints. The outputs consist of each agent’s concrete mobility
behaviors, including intention sequences, executed actions, and the resulting movement trajectories.
Evaluation Metrics: To evaluate whether LLM-based mobility simulations approximate real-world
human behavior, it is essential to quantify the similarity between the generated outcomes and empirical
distributions. Similarity-based evaluation provides a principled way to measure how closely synthetic
trajectories reproduce both individual-level behavioral intentions and population-level statistical
regularities, thereby aligning directly with the Realism objective of our framework. We adopt the
Jensen–Shannon Divergence (JSD) as the core similarity measure (see Appendix B). Lower JSD
values indicate higher similarity between simulated and observed distributions.
The benchmark evaluates four specific aspects, corresponding to different levels of behavioral realism:
• Intention Sequences JSD: Consistency in the ordering of individual activity types, directly
reflecting behavioral intentions.
• Gyration Radius JSD: Similarity in spatial dispersion patterns, capturing the aggregate range of
mobility.
• Daily Location Numbers JSD: Alignment in the number of distinct places visited per day across
the population.
• Intention Proportions JSD: Balance among different activity categories at the population level.
To provide a holistic assessment, these four metrics are aggregated into a single Final Score (Appendix B). The final score rescales similarity into the normalized range [0, 100], enabling direct
comparison across models and tasks.
5

Under review as a conference paper at ICLR 2026
270 Data Preparation: This benchmark builds upon the processed dataset released in (Shao et al., 2024b),
271 which originates from large-scale mobility records provided by Tencent and China Mobile. The
272 dataset integrates two complementary sources of information: (i) fine-grained mobility trajectories of
273 Beijing users, capturing daily location visits and activity intentions, and (ii) user profile attributes
274 that enrich the contextual understanding of individual behavior. These data enable a comprehensive
275 representation of both movement patterns and demographic heterogeneity, forming the foundation for
276 evaluating LLM-based mobility simulations.
277 Overall, the Daily Mobility Simulation provides a principled framework for measuring the ability
278 of LLM agents to reproduce realistic urban mobility patterns. By aligning closely with the Realism
279 dimension of our evaluation framework, it assesses whether simulated trajectories approximate
280 real-world data at both microscopic (individual-level intentions) and macroscopic (population-level
281 statistics) scales, thereby supporting future research in mobility-aware AI systems.
282
283 3.3 HURRICANE MOBILITY SIMULATION
284
Task Definition: Agents are required to generate user-level mobility patterns that reflect behavioral
285
variations across three temporal phases: pre-hurricane, during-hurricane, and post-hurricane. The
286
inputs include hurricane-related contextual information, user demographic and behavioral features,
287
and explicit temporal phase indicators, while the outputs consist of each agent’s concrete mobility
288
behaviors in terms of travel time and location information.
289
Evaluation Metrics: Two major dimensions are used:
290
291 • Change Rate Accuracy (Change Rate Score): The accuracy of mobility change rates is
292 measured by mean absolute percentage error (MAPE) (see Appendix B).
293 • Distribution Similarity (Distribution Score): Hourly travel distributions are compared using
294 cosine similarity (see Appendix B).
295
The final score is a weighted combination of the two metrics (see Appendix B). The weighting
296
emphasizes change rate accuracy (60%) due to its direct reflection of hurricane impact, while
297
distribution similarity (40%) captures temporal mobility dynamics.
298
Data preparation: For the Hurricane Mobility Simulation, we use mobility records obtained from
299
SafeGraph, filtered to include users located in the city of Columbia during Hurricane Dorian. The
300
original SafeGraph data are provided at a weekly resolution, which we further processed into daily
301
trajectories to capture finer-grained temporal dynamics across the pre-hurricane, during-hurricane, and
302
post-hurricane phases. In addition to mobility traces, synthetic user profiles are constructed through a
303
CBG (Census Block Group)-based sampling procedure: (i) identifying the set of CBGs belonging to
304 Columbia, (ii) allocating population samples proportional to each CBG’s demographic weight, (iii)
305 assigning residential locations within the sampled CBGs, and (iv) sampling additional attributes such
306 as gender, race, and income level according to CBG-level statistics. This combination of processed
307 mobility trajectories and sampled profile attributes provides a realistic and demographically grounded
308 dataset for evaluating agent responsiveness under extreme conditions.
309
Overall, the Hurricane Mobility Simulation provides a rigorous and domain-specific framework
310 to evaluate whether LLM agents can replicate mobility adaptations under extreme weather. By
311 emphasizing both change rate fidelity and temporal distribution alignment, it directly reflects the
312 Responsiveness dimension of our evaluation framework, testing whether agents can dynamically
313 adjust their behaviors to sudden environmental perturbations and advancing the study of AI-driven
314 human mobility modeling in disaster scenarios.
315
316 4 EXPERIMENTS
317
318 Based on our MobiSim-Bench benchmark, we organized an open competition to evaluate LLM
319 agents under real-world mobility scenarios. A total of 18 teams participated in the competition, with
320 10 teams entering the daily mobility simulation task and 8 teams entering the hurricane mobility
321 simulation task. Across all submissions, a total of 967 agents were deployed, of which 933 passed the
322 robustness evaluation and obtained valid evaluation scores. Among these, 361 agents were submitted
for the daily mobility task and 572 agents for the hurricane mobility task, reflecting both the scale
323
and diversity of approaches explored by the participating teams.
6

Under review as a conference paper at ICLR 2026
324 Table 1: Performance of all teams’ final submitted agents on the daily mobility task. Boldface
325 indicates best performance.
326
327 Team Role of LLM Base Model JSD JSD JSD JSD Final Score
gyr loc seq prop
328
#01 Brain GLM-4-Flash 0.328 0.665 0.063 0.289 66.38
329 #02 Brain GLM-4-Flash 0.334 0.554 0.183 0.404 63.13
330 #03 Brain GLM-4-Flash 0.321 0.692 0.320 0.190 61.93
331 #04 Glue Qwen-plus 0.421 0.495 0.266 0.366 61.29
#05 Glue GLM-4-Flash 0.329 0.655 0.170 0.404 61.04
332
#06 Brain GLM-4-Flash 0.339 0.560 0.262 0.408 60.79
333
#07 Extra GLM-4-Flash 0.384 0.786 0.267 0.217 58.62
334 #08 Glue deepseek-chat 0.397 0.735 0.198 0.378 57.32
335 #09 Extra GPT-4 0.433 0.720 0.253 0.522 51.80
336 #10 Extra Qwen-plus 0.393 0.791 0.639 0.441 43.39
337
338 Table 2: Performance of all teams’ final submitted agents on the hurricane mobility task. GC repre339 sents the Generated Change (During/After vs Before), CE represents the Change Error (During/After
340 vs Before), CRS represents the Change Rate Score, DS represents the Distribution Score. The
341 ground-truth Real Change is -47.34 / -11.50 (During/After vs Before), which is used to compute the
342 Change Error from Generated Change. Boldface marks the best performance.
343
344 Team Role of LLM Base Model GC CE CRS DS Final Score
345 #11 Extra GLM-4-Flash -44.01 / -12.76 3.33 / 1.26 91.02 77.53 85.63
346 #12 Extra deepseek-chat -45.54 / -9.90 1.80 / 1.60 91.13 64.47 80.47
347 #13 Brain GLM-4-Flash -86.25 / -11.54 38.91 / 0.04 58.74 76.37 65.79
#14 Glue deepseek-chat -8.37 / -14.44 38.97 / 2.94 46.08 86.33 62.18
348
#15 Brain GLM-4-Flash -43.30 / -14.43 4.04 / 2.93 83.00 27.56 60.83
349
#16 Brain GLM-4-Flash -41.20 / -66.56 6.14 / 55.06 0.00 85.78 34.31
350 #17 Brain GLM-4-Flash -28.35 / -46.63 18.99 / 35.12 0.00 83.40 33.36
351 #18 Extra GLM-4-Flash -60.05 / -94.75 12.71 / 83.25 0.00 58.01 23.20
352
353 4.1 BASELINES
354
355 The participating teams adopted a wide range of strategies, and some teams even experimented with
356 multiple approaches. Across all these submissions, we identified three predominant design paradigms,
357 each with distinct roles for LLMs in the decision-making process.
358
LLM as Brain: In this paradigm, teams primarily leverage LLMs’ comprehensive reasoning and
359 creative generation capabilities to drive complete agent behavior. These approaches utilize the LLM’s
360 natural language processing and multi-step reasoning to produce complex behavioral decisions.
361 The best-performing LLM-dominated approach in the daily mobility task employs a narrative362 driven methodology. First, the LLM generates a detailed, first-person daily narrative describing the
363 character’s activities and thoughts throughout the day (An example can be found in Appendix A.3).
364 Second, another LLM call parses this narrative into structured activity plans. This two-step process
ensures both narrative coherence and structural precision, allowing the agent to follow a pre-generated
365
plan throughout the task day.
366
367 LLM as Glue: In this paradigm, teams primarily utilize LLMs’ contextual adaptation and intelligent
368 bridging capabilities to enhance rule-based systems. These approaches leverage the LLM’s ability to
369 understand complex contexts and provide intelligent recommendations that connect different system
370 components. The best-performing LLM-as-Glue approach employs a multi-phase state manager with
explicit normal, hurricane, and post-hurricane phases. The system maintains internal states (fatigue,
371
hunger, emotion, personality) and uses predefined behavioral templates, but the LLM provides
372
intelligent recommendations that consider the agent’s current subjective state, personality type, and
373
environmental context. When the primary rule-based system encounters complex situations, the LLM
374
bridges the gap between rigid templates and dynamic contextual needs.
375
376 LLM as Extra: In this paradigm, teams either minimally utilize LLM capabilities or completely avoid
them, with core intelligence residing in well-designed rule systems. When present, teams only utilize
377
the LLM’s basic pattern recognition abilities as supplementary tools. The best-performing LLM-as7

Under review as a conference paper at ICLR 20
378
Extra approach in the hurricane mobility task e
379 system that adapts to different hurricane phases
380 fines three distinct phases with corresponding pr
381 for each hour of the day. The decision logic is e
382 that sophisticated agent behavior can be achiev
383 advanced LLM capabilities.
384
385 4.2 RESULTS
386
The performance results across the three desig
387
distinct trade-offs and characteristics that align
388
389 LLM as Brain: The LLM-as-Brain approach ac
390 task, demonstrating its strength in generating n
391 JSD scores for intention sequences and intention
392 at producing coherent and psychologically plau
closely match real human behavior patterns at a
393
micro-behaviors such as morning commutes, lun
394
with the daily mobility benchmark’s focus on beh
395
activity transitions and maintain appropriate inte
396
other types of environmental changes, such as hu
397
struggles, producing unrealistic or overly comp
398 accurate human responses required during emer
399
LLM as Glue: The LLM-as-Glue approach
400
indicating its versatility in handling diverse sce
401
suggest that while state-driven agents can main
402
the complexity of parameter tuning and state sp
403
lower distribution score indicates challenges in a
404 weather events.
405
LLM as Extra: The LLM-as-Extra approach
406
mobility task, where predictability and reliabilit
407
change rate score demonstrates that rule-based sy
408
shifts during extreme weather events, which is e
409
phasis on change rate accuracy. However, the rel
410 that rigid rule structures may limit behavioral d
411 evidenced by higher JSD scores across all metri
412
413
4.3 DISCUSSION
414
415 Cross-task Performance Patterns: The perform
416 the quality of human behavior simulation across
417 evaluates the ability to simulate realistic daily hu
418 excel by leveraging the model’s comprehensive re
appropriate behaviors. The superior JSD scores
419
that LLM-driven agents produce more coherent a
420
suggesting that complex behavioral modeling be
421
422 However, in the hurricane mobility task, which
423 during extreme weather events, LLM-as-Extra
424 perform those with greater LLM integration. T
clear behavioral patterns and predictable huma
425
accurately model the expected changes in huma
426
struggle to represent the precise behavioral pat
427
emergency response simulation.
428
429 Cross-model Performance Patterns: In the h
430 rule-driven pipeline with different base models
fitting the overall change rate and preserving h
431
Deepseek-chat(DeepSeek-AI et al., 2024) show

oys a sophisticated hour-level probability table
individual agent characteristics. The system debility matrices that specify movement likelihoods
ely deterministic and rule-based, demonstrating
hrough well-designed rule frameworks without
aradigms as Table 1 and Table 2 shows reveal
their underlying design philosophies.
ved the highest performance in the daily mobility
al and diverse behavioral patterns. The superior
oportions indicate that LLM-driven agents excel
e activity sequences. These sequences not only
cro level but also effectively reconstruct specific
breaks, and evening leisure activities. This aligns
oral realism, where the ability to generate natural
n distributions is crucial. However, when facing
cane scenarios, the current LLM-as-Brain design
behaviors that fail to replicate the simplified yet
cies.
eved balanced performance across both tasks,
ios. The moderate JSD scores in daily mobility
n behavioral coherence, they may struggle with
management. In the hurricane mobility task, the
ately modeling temporal patterns during extreme
wed remarkable effectiveness in the hurricane
e crucial for emergency scenarios. The excellent
ms can accurately capture the expected behavioral
ntial for the hurricane mobility benchmark’s emely lower performance in daily mobility suggests
rsity and creativity in normal circumstances, as
ce patterns reveal how different LLM roles affect
erent scenarios. In the daily mobility task, which
n movement patterns, LLM-as-Brain approaches
ning capabilities to generate natural, contextually
ntention sequences and proportions demonstrate
ty patterns that better match real human behavior,
fits from maximal LLM involvement.
aluates the ability to simulate human responses
roaches (with minimal LLM involvement) outreveals an important insight: for scenarios with
esponses, well-designed rule systems can more
mobility behavior, while current LLMs may still
s and temporal dynamics required for accurate
cane mobility task, one team applied the same
vealing clear model-specific trade-offs between
-level distribution patterns. (as Table 3 shows).
e tightest alignment with targeted change rates,

Under review as a conference paper at ICLR 2026
432 Table 3: Comparison of three base models from the same team using the same paradigm on the
433 hurricane mobility task. Boldface marks the best performance.
434
435 Model GC CE CRS DS Final Score
436
GLM-4-Flash-Free -44.01 / -12.76 3.33 / 1.26 91.02 77.53 85.63
437 Deepseek-chat -46.76 / -11.51 0.58 / 0.01 99.36 59.87 83.57
438 Qwen-plus -51.18 / -10.49 3.83 / 1.02 91.53 56.18 77.39
439 reflecting strong numerical discipline and instruction-following, but this comes at the cost of flatter,
440 less detailed hourly dynamics. GLM-4-Flash-Free achieves the most balanced performance, keeping
441 change errors low while maintaining richer diurnal structures, which supports its leading overall
442 score. Qwen-plus(Yang et al., 2025), by contrast, lags on both metrics, with larger deviations in
443 change rate and weaker reconstruction of hourly usage, indicating less stable phase calibration. These
444 outcomes suggest a practical guideline: choose numerically disciplined models when aggregate
accuracy is critical, and balanced models when both accuracy and realistic hourly patterns matter,
445
avoiding models with inconsistent behaviors across metrics.
446
447
448 5 RELATED WORK
449
450 5.1 MOBILITY SIMULATION
451
Research on mobility behavior simulation can be broadly divided into two categories. The first cate452
gory follows traditional deep learning approaches, including classical Markov models (Rendle et al.,
453
2010) and subsequent sequence-modeling techniques such as recurrent neural networks (RNNs) (Lai
454
et al., 2023; Feng et al., 2020) and attention-based architectures (Qin et al., 2022; Hong et al., 2023b).
455
More recent studies employ LLM-driven agents to conduct mobility simulations (Feng et al., 2025;
456
Shao et al., 2024b; Wang et al., 2024c), leveraging the agents’ extensive world knowledge, reasoning
457 capabilities, and adaptive decision-making to generate more realistic and dynamic movement patterns.
458
459
5.2 LLM AGENT SIMULATION BENCHMARK
460
461 The use of LLM agents for simulation has attracted growing attention in recent years. A number of
462 studies (Sukiennik et al., 2025; Zhao et al., 2024) have demonstrated the broad societal value of
463 deploying LLM agents in complex simulation settings. Meanwhile, platforms such as AgentSoci464 ety (Piao et al., 2025b) and YuLan-OneSim (Wang et al., 2025), along with recent efforts to optimize
multi-agent simulation systems (Piao et al., 2025a; Zhang et al., 2025a), have further facilitated
465
large-scale agent-based simulation experiments. Despite these advances, most existing LLM-agent
466
benchmarks remain primarily focused on assessing ”tool-like” capabilities (Abdelnabi et al., 2024;
467
Zhu et al., 2025; Xu et al., 2024; Piatti et al., 2024), offering limited evaluation of agents’ ability
468
to simulate human behavioral patterns. Our work addresses this gap by introducing a benchmark
469
specifically designed to assess agents’ competence in modeling realistic human behaviors, thereby
470 contributing a novel and meaningful perspective to the field.
471
472
6 CONCLUSION
473
474
In this paper, to comprehensively evaluate the performance of LLM agent for human mobility
475
behavior simulation, we propose an evaluation framework containing three perspectives: robustness,
476
realism, and responsiveness. Guided by the evaluation framework, we construct a multi-perspective
477
benchmark named MobiSim-Bench powered by AgentSociety simulation framework, which contains
478
the daily mobility simulation and the hurricane mobility simulation. By organizing a challenge, we
479 evaluated the performance of multiple LLM agent design approaches under this evaluation framework
480 and benchmark. Unfortunately, none of the LLM agent designs can achieve robustness, realism and
481 responsiveness at the same time. This demonstrates the importance and value of MobiSim-Bench on
482 one hand, and reveals the inadequacy of current LLM agent designs for simulating human mobility
483 behavior on the other. We hope that MobiSim-Bench can help the research community to explore
484 and discover LLM agent designs that can effectively and comprehensively simulate human mobility
behavior, and thus promote the development of social science research paradigms driven by LLM
485
agents.
9

Under review as a conference paper at ICLR 2026
486 ETHICS STATEMENT
487
488
This work fully complies with the ICLR Code of Ethics. All datasets used in MobiSim-Bench
489 have undergone strict anonymization and desensitization procedures to ensure that no personally
490 identifiable or sensitive information is retained. The benchmark is designed solely for research
491 purposes, emphasizing transparency, reproducibility, and responsible use. Dataset documentation,
492 simulation procedures, and evaluation guidelines are provided to facilitate safe adoption and avoid
493 potential misuse. No conflicts of interest or external sponsorship influenced the design or outcomes
494 of this work.
495
496 REPRODUCIBILITY STATEMENT
497
498 We prioritize reproducibility by releasing all necessary resources alongside the paper. The datasets
499 used in MobiSim-Bench, preprocessing scripts, simulation workflow, evaluation metrics, and baseline
500 implementations are included in an anonymized repository linked with the abstract. We provide
501 detailed descriptions of the two tasks in our benchmark framework, the Daily Mobility Simulation (in
502 Subsection 3.2) and the Hurricane Mobility Simulation (in Subsection 3.3). Each Subsection specifies
503 the task definition, the datasets employed, and the corresponding preprocessing steps. In addition,
Appendix B lists the complete calculation formulas for all evaluation metrics. Considering the
504
inherent randomness of LLMs, in order to reduce the difficulty of reproduction, we release baseline
505
methods for both tasks, with Section 3 reporting extensive results across different LLM configurations.
506
Appendix A.2 further compiles all benchmark results for reference, while Appendix A.3 presents a
507
detailed output example of the best-performing LLM-driven agent in the Daily Mobility task. These
508
resources collectively ensure that independent researchers can reliably reproduce and extend our
509 findings.
510
511
REFERENCES
512
513 Sahar Abdelnabi, Amr Gomaa, Sarath Sivaprasad, Lea Scho¨nherr, and Mario Fritz. Cooperation,
514 competition, and maliciousness: Llm-stakeholders interactive negotiation. In A. Globerson,
515 L. Mackey, D. Belgrave, A. Fan, U. Paquet, J. Tomczak, and C. Zhang (eds.), Advances in Neural
516 Information Processing Systems, volume 37, pp. 83548–83599. Curran Associates, Inc., 2024.
517 URL https://proceedings.neurips.cc/paper_files/paper/2024/file/
984dd3db213db2d1454a163b65b84d08-Paper-Datasets_and_Benchmarks_
518
Track.pdf.
519
520
Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal,
521 Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are
522 few-shot learners. Advances in neural information processing systems, 33:1877–1901, 2020.
523
Jiangjie Chen, Xintao Wang, Rui Xu, Siyu Yuan, Yikai Zhang, Wei Shi, Jian Xie, Shuang Li, Ruihan
524
Yang, Tinghui Zhu, et al. From persona to personalization: A survey on role-playing language
525
agents. arXiv preprint arXiv:2404.18231, 2024.
526
527 Yile Chen, Cheng Long, Gao Cong, and Chenliang Li. Context-aware Deep Model for Joint Mobility
528 and Time Prediction. In Proceedings of the 13th International Conference on Web Search and
529 Data Mining, pp. 106–114, Houston TX USA, January 2020. ACM. ISBN 978-1-4503-6822-3.
530 doi: 10.1145/3336191.3371837. URL https://dl.acm.org/doi/10.1145/3336191.
531 3371837.
532
Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. Mem0: Building
533
production-ready ai agents with scalable long-term memory. arXiv preprint arXiv:2504.19413,
534
2025.
535
536 DeepSeek-AI, :, Xiao Bi, Deli Chen, Guanting Chen, Shanhuang Chen, Damai Dai, Chengqi Deng,
537 Honghui Ding, Kai Dong, Qiushi Du, Zhe Fu, Huazuo Gao, Kaige Gao, Wenjun Gao, Ruiqi
538 Ge, Kang Guan, Daya Guo, Jianzhong Guo, Guangbo Hao, Zhewen Hao, Ying He, Wenjie Hu,
Panpan Huang, Erhang Li, Guowei Li, Jiashi Li, Yao Li, Y. K. Li, Wenfeng Liang, Fangyun
539
Lin, A. X. Liu, Bo Liu, Wen Liu, Xiaodong Liu, Xin Liu, Yiyuan Liu, Haoyu Lu, Shanghao Lu,
10

Under review as a conference paper at ICLR 2026
540
Fuli Luo, Shirong Ma, Xiaotao Nie, Tian Pei, Yishi Piao, Junjie Qiu, Hui Qu, Tongzheng Ren,
541 Zehui Ren, Chong Ruan, Zhangli Sha, Zhihong Shao, Junxiao Song, Xuecheng Su, Jingxiang
542 Sun, Yaofeng Sun, Minghui Tang, Bingxuan Wang, Peiyi Wang, Shiyu Wang, Yaohui Wang,
543 Yongji Wang, Tong Wu, Y. Wu, Xin Xie, Zhenda Xie, Ziwei Xie, Yiliang Xiong, Hanwei Xu,
544 R. X. Xu, Yanhong Xu, Dejian Yang, Yuxiang You, Shuiping Yu, Xingkai Yu, B. Zhang, Haowei
545 Zhang, Lecong Zhang, Liyue Zhang, Mingchuan Zhang, Minghua Zhang, Wentao Zhang, Yichao
546 Zhang, Chenggang Zhao, Yao Zhao, Shangyan Zhou, Shunfeng Zhou, Qihao Zhu, and Yuheng
Zou. Deepseek llm: Scaling open-source language models with longtermism, 2024. URL
547
https://arxiv.org/abs/2401.02954.
548
549 Guillaume Deffuant, David Neau, Frederic Amblard, and Ge´rard Weisbuch. Mixing beliefs among
550 interacting agents. Advances in Complex Systems, 3(01n04):87–98, 2000.
551
Jinyuan Fang, Yanwen Peng, Xi Zhang, Yingxu Wang, Xinhao Yi, Guibin Zhang, Yi Xu, Bin Wu,
552
Siwei Liu, Zihao Li, et al. A comprehensive survey of self-evolving ai agents: A new paradigm
553
bridging foundation models and lifelong agentic systems. arXiv preprint arXiv:2508.07407, 2025.
554
555 Jie Feng, Yong Li, Chao Zhang, Funing Sun, Fanchao Meng, Ang Guo, and Depeng Jin. DeepMove:
556 Predicting Human Mobility with Attentional Recurrent Networks. In Proceedings of the 2018
557 World Wide Web Conference on World Wide Web - WWW ’18, pp. 1459–1468, Lyon, France,
558 2018. ACM Press. ISBN 978-1-4503-5639-8. doi: 10.1145/3178876.3186058. URL http:
//dl.acm.org/citation.cfm?doid=3178876.3186058.
559
560
Jie Feng, Can Rong, Funing Sun, Diansheng Guo, and Yong Li. Pmf: A privacy-preserving human
561 mobility prediction framework via federated learning. Proceedings of the ACM on Interactive,
562 Mobile, Wearable and Ubiquitous Technologies, 4(1):1–21, 2020.
563
Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. Agentmove: Predicting human mobility anywhere using
564
large language model based agentic framework. arXiv preprint arXiv:2408.13986, 2024.
565
566 Jie Feng, Yuwei Du, Jie Zhao, and Yong Li. Agentmove: A large language model based agentic
567 framework for zero-shot next location prediction, 2025. URL https://arxiv.org/abs/
568 2408.13986.
569
Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin,
570
and Yong Li. S3: Social-network simulation system with large language model-empowered agents.
571
arXiv preprint arXiv:2307.14984, 2023.
572
573 Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and Yong
574 Li. Large language models empowered agent-based modeling and simulation: A survey and
575 perspectives. Humanities and Social Sciences Communications, 11(1):1–24, 2024.
576
Dawei Gao, Zitao Li, Yuexiang Xie, Weirui Kuang, Liuyi Yao, Bingchen Qian, Zhijian Ma, Yue
577
Cui, Haohao Luo, Shen Li, Lu Yi, Yi Yu, Shiqi He, Zhiling Luo, Wenmeng Zhou, Zhicheng
578 Zhang, Xuguang He, Ziqian Chen, Weikai Liao, Farruh Isakulovich Kushnazarov, Yaliang Li,
579 Bolin Ding, and Jingren Zhou. Agentscope 1.0: A developer-centric framework for building
580 agentic applications, 2025. URL https://arxiv.org/abs/2508.16279.
581
Santiago Garcia-Gabilondo, Yuya Shibuya, and Yoshihide Sekimoto. Enhancing geospatial retail
582
analysis by integrating synthetic human mobility simulations. Computers, Environment and Urban
583
Systems, 108:102058, 2024.
584
585 Zhenyu Han, Fengli Xu, Yong Li, Tao Jiang, and James Evans. Model predicted human mobility
586 explains covid-19 transmission in urban space without behavioral data. Scientific Reports, 15(1):
587 6365, 2025.
588
Sirui Hong, Xiawu Zheng, Jonathan Chen, Yuheng Cheng, Jinlin Wang, Ceyao Zhang, Zili Wang,
589
Steven Ka Shing Yau, Zijuan Lin, Liyang Zhou, et al. Metagpt: Meta programming for multi-agent
590 collaborative framework. arXiv preprint arXiv:2308.00352, 2023a.
591
592 Ye Hong, Yatao Zhang, Konrad Schindler, and Martin Raubal. Context-aware multi-head selfattentional neural network model for next location prediction. Transportation Research Part C:
593
Emerging Technologies, 156:104315, 2023b.
11

Under review as a conference paper at ICLR 20
594
John J Horton. Large language models as simula
595 silicus? Technical report, National Bureau of
596
Siqi Lai, Zhao Xu, Weijia Zhang, Hao Liu, and
597
control agents: Capacity and opportunity. arX
598
599 Nian Li, Chen Gao, Mingyu Li, Yong Li, and
600 empowered agents for simulating macroecon
601 Meeting of the Association for Computationa
602 15536, 2024.
603
Thorsten Neumann, Matthias Heinrichs, Michae
604
Biebl. Quantitative analysis of future scenario
605
case study. Transportation Research Procedi
606
607 Joon Sung Park, Joseph O’Brien, Carrie Jun Cai,
608 Bernstein. Generative agents: Interactive simu
annual acm symposium on user interface soft
609
610 Jinghua Piao, Yuwei Yan, Nian Li, Jun Zhang, a
611 for piloting social experiments, 2025a. URL
612
Jinghua Piao, Yuwei Yan, Jun Zhang, Nian Li,
613
Zheng, Jing Yi Wang, Di Zhou, Chen Gao, Fe
614
Agentsociety: Large-scale simulation of llm615
human behaviors and society, 2025b. URL h
616
617 Giorgio Piatti, Zhijing Jin, Max Kleiman-Weine
618 Mihalcea. Cooperate or collapse: Emergen
619 agents. In The Thirty-eighth Annual Conferen
URL https://openreview.net/foru
620
621
Chen Qian, Wei Liu, Hongzhang Liu, Nuo Chen
622 Yusheng Su, Xin Cong, et al. Chatdev: Co
623 Proceedings of the 62nd Annual Meeting of th
624 1: Long Papers), pp. 15174–15186, 2024.
625
Yanjun Qin, Yuchen Fang, Haiyong Luo, Fang
626
recommendation with auto-correlation enhanc
627
of the 45th International ACM SIGIR Confer
628
Retrieval, pp. 2612–2616, 2022.
629
630 Steffen Rendle, Christoph Freudenthaler, and Lar
631 chains for next-basket recommendation. In P
World Wide Web, pp. 811–820, 2010.
632
633 Thomas C Schelling. Dynamic models of seg
634 143–186, 1971.
635
Chenyang Shao, Fengli Xu, Bingbing Fan, Jin
636
Beyond imitation: Generating human mobilit
637
models. arXiv preprint arXiv:2402.09836, 20
638
639 Chenyang Shao, Fengli Xu, Bingbing Fan, Jin
640 Chain-of-planned-behaviour workflow elicits
641 https://arxiv.org/abs/2402.098
642
Yunfan Shao, Linyang Li, Junqi Dai, and Xipe
643
playing. In Proceedings of the 2023 Confer
644 Processing, pp. 13153–13187, 2023.
645
646 Nicholas Sukiennik, Yichuan Xu, Yuqing Kan,
The roots of international perceptions: Simu
647
agents, 2025. URL https://arxiv.org

economic agents: What can we learn from homo
onomic Research, 2023.
Xiong. Large language models as traffic signal
preprint arXiv:2312.16044, 2023.
gmin Liao. Econagent: large language modelc activities. In Proceedings of the 62nd Annual
nguistics (Volume 1: Long Papers), pp. 15523–
ehrisch, Jakob Erdmann, and Anke Sauerla¨nderf urban mobility using agent-based simulation–a
1:295–308, 2019.
redith Ringel Morris, Percy Liang, and Michael S
a of human behavior. In Proceedings of the 36th
e and technology, pp. 1–22, 2023.
Yong Li. Exploring large language model agents
tps://arxiv.org/abs/2508.08678.
bo Yan, Xiaochong Lan, Zhihong Lu, Zhiheng
Xu, Fang Zhang, Ke Rong, Jun Su, and Yong Li.
en generative agents advances understanding of
ps://arxiv.org/abs/2502.08691.
ernhard Scho¨lkopf, Mrinmaya Sachan, and Rada
f sustainable cooperation in a society of LLM
n Neural Information Processing Systems, 2024.
id=0zWzJj6lO3.
ufan Dang, Jiahao Li, Cheng Yang, Weize Chen,
unicative agents for software development. In
sociation for Computational Linguistics (Volume
ao, and Chenxing Wang. Next point-of-interest
multi-modal transformer network. In Proceedings
e on Research and Development in Information
chmidt-Thieme. Factorizing personalized markov
eedings of the 19th International Conference on
tion. Journal of mathematical sociology, 1(2):
o Ding, Yuan Yuan, Meng Wang, and Yong Li.
om context-aware reasoning with large language
.
o Ding, Yuan Yuan, Meng Wang, and Yong Li.
w-shot mobility generation in llms, 2024b. URL
Qiu. Character-llm: A trainable agent for rolee on Empirical Methods in Natural Language
ghua Piao, Yuwei Yan, Chen Gao, and Yong Li.
ng us attitude changes towards china with llm
bs/2508.08837.

Under review as a conference paper at ICLR 20
648
Hugo Touvron, Thibaut Lavril, Gautier Izacard
649 Lacroix, Baptiste Rozie`re, Naman Goyal, E
650 efficient foundation language models. arXiv p
651
Jiawei Wang, Renhe Jiang, Chuang Yang, Zen
652
Noboru Koshizuka, and Chuan Xiao. Large
653
framework for personal mobility generation. A
654
37:124547–124574, 2024a.
655
656 Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhan
Tang, Xu Chen, Yankai Lin, Wayne Xin Z
657
large language model based autonomous age
658
2024b. ISSN 2095-2236. doi: 10.1007/s117
659
10.1007/s11704-024-40231-1.
660
661 Lei Wang, Heyang Gao, Xiaohe Bo, Xu Chen,
662 generation of social simulator with large langu
663 abs/2505.07581.
664
Xinglei Wang, Meng Fang, Zichao Zeng, and Tao
665 els as human mobility predictors, 2024c. UR
666
Xingrui Wang, Xinyu Liu, Ziteng Lu, and Hanf
667
Using Map Based on Two Stage GAN. Jo
668
1680-743X, 1683-8602. doi: 10.6339/21-JDS1
669
10.6339/21-JDS1004.
670
671 Hao WU, Ziyang CHEN, Weiwei SUN, Baihu
672 with recurrent neural networks.(2017). In Pro
673 on Artificial Intelligence IJCAI-17, Melbourn
674
Lin Xu, Zhiyuan Hu, Daquan Zhou, Hongyu R
675 Jiashi Feng. MAgIC: Investigation of large
676 adaptability, rationality and collaboration. I
677 Chen (eds.), Proceedings of the 2024 Confe
678 Processing, Miami, Florida, USA, November
679
Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao,
680
memory for llm agents. arXiv preprint arXiv:
681
682 Yuwei Yan, Qingbin Zeng, Zhiheng Zheng, Jing
683 Li. Opencity: A scalable platform to simula
preprint arXiv:2410.21286, 2024.
684
685 An Yang, Anfeng Li, Baosong Yang, Beichen Z
686 Gao, Chengen Huang, Chenxu Lv, Chujie Zh
687 Hao Ge, Haoran Wei, Huan Lin, Jialong Tan
688 Yang, Jiaxi Yang, Jing Zhou, Jingren Zhou,
689 Le Yu, Lianghao Deng, Mei Li, Mingfeng Xu
690 Men, Ruize Gao, Shixuan Liu, Shuang Luo,
Ren, Xinyu Wang, Xinyu Zhang, Xuancheng
691
Zhang, Yu Wan, Yuqiong Liu, Zekun Wang,
692
Qiu. Qwen3 technical report, 2025. URL ht
693
694 Hui Yang, Sifu Yue, and Yunzhong He. Auto
695 additional opinions. arXiv preprint arXiv:230
696
Yuan Yuan, Jingtao Ding, Huandong Wang, Dep
697
via modeling spatiotemporal dynamics. In Pr
698
Knowledge Discovery and Data Mining, pp. 4
699
700 Jun Zhang, Wenxuan Ao, Junbo Yan, Depeng
simulator for transportation system optimizati
701
2024a.

avier Martinet, Marie-Anne Lachaux, Timothe´e
Hambro, Faisal Azhar, et al. Llama: Open and
rint arXiv:2302.13971, 2023.
ng Wu, Makoto Onizuka, Ryosuke Shibasaki,
guage models as urban residents: An llm agent
ances in Neural Information Processing Systems,
Hao Yang, Jingsen Zhang, Zhiyuan Chen, Jiakai
, Zhewei Wei, and Jirong Wen. A survey on
. Frontiers of Computer Science, 18(6), March
024-40231-1. URL http://dx.doi.org/
Ji-Rong Wen. Yulan-onesim: Towards the next
models, 2025. URL https://arxiv.org/
eng. Where would i go next? large language modttps://arxiv.org/abs/2308.15197.
Yang. Large Scale GPS Trajectory Generation
al of Data Science, pp. 126–141, 2021. ISSN
4. URL https://jds-online.org/doi/
HENG, and Wei WANG. Modeling trajectories
dings of the 26th International Joint Conference
ustralia, August 19, volume 25, pp. 3083–3090.
Zhen Dong, Kurt Keutzer, See-Kiong Ng, and
guage model powered multi-agent in cognition,
aser Al-Onaizan, Mohit Bansal, and Yun-Nung
ce on Empirical Methods in Natural Language
24. Association for Computational Linguistics.
ao Tan, and Yongfeng Zhang. A-mem: Agentic
2.12110, 2025.
Yuan, Jie Feng, Jun Zhang, Fengli Xu, and Yong
urban activities with massive llm agents. arXiv
ng, Binyuan Hui, Bo Zheng, Bowen Yu, Chang
, Dayiheng Liu, Fan Zhou, Fei Huang, Feng Hu,
ian Yang, Jianhong Tu, Jianwei Zhang, Jianxin
nyang Lin, Kai Dang, Keqin Bao, Kexin Yang,
Mingze Li, Pei Zhang, Peng Wang, Qin Zhu, Rui
nhao Li, Tianyi Tang, Wenbiao Yin, Xingzhang
en, Yang Fan, Yang Su, Yichang Zhang, Yinger
u Cui, Zhenru Zhang, Zhipeng Zhou, and Zihan
s://arxiv.org/abs/2505.09388.
for online decision making: Benchmarks and
2224, 2023.
Jin, and Yong Li. Activity trajectory generation
edings of the 28th ACM SIGKDD Conference on
2–4762, 2022.
, and Yong Li. A gpu-accelerated large-scale
benchmarking. arXiv preprint arXiv:2406.10661,

Under review as a conference paper at ICLR 2026
702
Jun Zhang, Wenxuan Ao, Junbo Yan, Can Rong, Depeng Jin, Wei Wu, and Yong Li. Moss: A
703 large-scale open microscopic traffic simulation system. arXiv preprint arXiv:2405.12520, 2024b.
704
705 Jun Zhang, Yuwei Yan, Junbo Yan, Zhiheng Zheng, Jinghua Piao, Depeng Jin, and Yong Li. A
parallelized framework for simulating large-scale LLM agents with realistic environments and
706
interactions. In Georg Rehm and Yunyao Li (eds.), Proceedings of the 63rd Annual Meeting
707
of the Association for Computational Linguistics (Volume 6: Industry Track), pp. 1339–1349,
708
Vienna, Austria, July 2025a. Association for Computational Linguistics. ISBN 979-8-89176709
288-6. doi: 10.18653/v1/2025.acl-industry.94. URL https://aclanthology.org/2025.
710 acl-industry.94/.
711
712 Jun Zhang, Yuwei Yan, Junbo Yan, Zhiheng Zheng, Jinghua Piao, Depeng Jin, and Yong Li. A
713 parallelized framework for simulating large-scale llm agents with realistic environments and
interactions. In Proceedings of the 63rd Annual Meeting of the Association for Computational
714
Linguistics (Volume 6: Industry Track), pp. 1339–1349, 2025b.
715
716 Zeyu Zhang, Quanyu Dai, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Jieming Zhu, Zhenhua Dong, and
717 Ji-Rong Wen. A survey on the memory mechanism of large language model-based agents. ACM
718 Transactions on Information Systems, 43(6):1–47, 2025c.
719
Qinlin Zhao, Jindong Wang, Yixuan Zhang, Yiqiao Jin, Kaijie Zhu, Hao Chen, and Xing Xie.
720
Competeai: Understanding the competition dynamics in large language model-based agents, 2024.
721
URL https://arxiv.org/abs/2310.17512.
722
723 Wayne Xin Zhao, Kun Zhou, Junyi Li, Tianyi Tang, Xiaolei Wang, Yupeng Hou, Yingqian Min,
724 Beichen Zhang, Junjie Zhang, Zican Dong, et al. A survey of large language models.
725
Kunlun Zhu, Hongyi Du, Zhaochen Hong, Xiaocheng Yang, Shuyi Guo, Zhe Wang, Zhenhailong
726
Wang, Cheng Qian, Robert Tang, Heng Ji, and Jiaxuan You. MultiAgentBench : Evaluating
727
the collaboration and competition of LLM agents. In Wanxiang Che, Joyce Nabende, Ekaterina
728 Shutova, and Mohammad Taher Pilehvar (eds.), Proceedings of the 63rd Annual Meeting of the
729 Association for Computational Linguistics (Volume 1: Long Papers), Vienna, Austria, July 2025.
730 Association for Computational Linguistics.
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
14

Under review as a conference paper at ICLR 2026
756 A APPENDIX
757
758
A.1 THE USE OF LARGE LANGUAGE MODELS
759
760 In this work, the use of LLMs is limited to checking for grammatical errors and providing word
761 suggestions.
762
763 A.2 OVERALL SUBMISSION STATUS
764
765
Table 4: Summary of competition participation.
766
767
768 task # of Teams # of Agents Submitted # of Agents Evaluated
769 Daily mobility 10 362 361
770 Hurricane mobility 8 605 572
771 Total 18 967 933
772
773
774
775 A.3 AN EXAMPLE OF NARRATIVE GENERATED FROM THE BEST-PERFORMING
776 LLM-DOMINATED AGENT IN THE DAILY MOBILITY TASK
777
778
I woke up around 7:45 AM to the sound of my phone buzzing on the nightstand—same
779
old alarm, same tired feeling. My apartment in Haidian (that’s location ID 500063798 for
780 whatever system needs that) is cozy but nothing fancy: IKEA furniture, a desk buried under
781 cables and old coffee mugs, and a window that looks out onto a row of elm trees and the
782 back of a convenience store. I lay there for a few minutes scrolling through WeChat—family
783 group messages from my mom asking if I’ve eaten properly, a couple memes from my college
784 buddies, and a work Slack ping reminding me about today’s sprint review.
785
By 8:10, I dragged myself out of bed. Quick shower, face wash, toothbrush dance—I keep it
786
simple. Breakfast was instant oatmeal with a banana and black tea, all while half-watching a
787
tech podcast on my laptop. I hate mornings, but at least Beijing’s autumn air is finally cooling
788 down. No more sweltering subway rides.
789
790 Left the house at 8:50, walked five minutes to Wudaokou Station. Took Line 13 toward
Zhichunlu, then switched to Line 10. The commute’s predictable—packed cars, people
791
reading novels or napping standing up, someone always blasting music by accident. Got off at
792
Suzhoujie Station (close enough to office ID 500059965), then a ten-minute walk through that
793
narrow street lined with bubble tea shops and repair stalls.
794
795 Reached the office around 9:25. Clock in, hang up my jacket, refill my thermos with hot water.
796 Team meeting started at 9:30—we’re wrapping up this backend migration, so I gave a quick
797 update on the API refactoring I’ve been grinding on. Then it was heads-down coding until
798 lunch. Debugged a race condition in the user auth module—stupid typo in a timeout config.
Felt dumb, but hey, at least it wasn’t in production.
799
800
Lunch was at 12:30. Me and three other guys from the team hit that hand-pulled noodle
801 place across the street—*Lanzhou Lamian*, yellow signs, cheap and filling. Beef soup,
802 extra cilantro, chili oil on the side. We talked about everything except work: someone’s new
803 apartment, the PS5 price hike, whether China will ever get decent sci-fi movies outside of
804 *The Wandering Earth*. Back to the office by 1:15.
805
Afternoon was lighter—code review for a junior dev, updated some documentation (ugh), and
806
fixed a minor UI glitch on the internal dashboard. Took a 20-minute break around 4:00 to walk
807
around the block and grab a soy milk and steamed bun from the old lady’s cart near the park
808
entrance. Autumn sunlight felt good on my face.
809
15

Under review as a conference paper at ICLR 2026
810
811 Wrapped up around 6:45. Manager didn’t push for overtime, which I appreciated—we’re not
812 crunching yet. Left the office by 7:00. Instead of going straight home, swung by the Carrefour
813 Express near Wudaokou Square. Picked up tofu, bok choy, instant ramen (for emergencies), a
814 bottle of soy sauce, and a liter of beer—just one, because I’m not trying to become “that guy”
815 with a fridge full of empties.
816
Got home around 7:45. Changed into sweatpants, put on some lo-fi beats. Cooked a quick
817
stir-fry with what I had—garlic, tofu, greens—and poured the beer into a glass. Ate while
818 watching an episode of *Line of Duty* dubbed in Mandarin. Not the same without the accents,
819 but it passes the time.
820
Around 9:30, I opened my notebook and sketched out some ideas for a personal project—a
821
habit-tracking app with minimalist design. Nothing serious, just something to tinker with on
822
weekends. Then browsed Zhihu for half an hour, reading rants about AI replacing programmers
823
(again).
824
825 Showered again—sweat from the commute still clinging—and brushed my teeth. Checked my
826 phone one last time: no urgent messages, weather says tomorrow will be partly cloudy. Set the
827 alarm for 7:50. Lights out by 11:20.
828
As I drifted off, I thought: *Another day, another thousand lines of code nobody will ever see.*
829
But hey—at least the noodles were good.
830
831
832
B FORMULAS FOR EVALUATION METRICS
833
834
B.1 DAILY MOBILITY SIMULATION METRICS
835
836
The Jensen–Shannon Divergence (JSD) is defined as:
837
JSD(P ∥ Q) = 1 KL(P ∥ M ) + 1 KL(Q ∥ M ), M = 1 (P + Q),
838 2 2 2
839 where P and Q denote the probability distributions of generated and real-world data, respectively,
840 and KL(· ∥ ·) is the Kullback–Leibler divergence.
841
The aggregated Final Score is defined as:
842
843 (cid:18) (1 − JSD ) + (1 − JSD ) + (1 − JSD ) + (1 − JSD ) (cid:19)
Final Score = gyr loc seq prop × 100.
844 4
845
846
B.2 HURRICANE MOBILITY SIMULATION METRICS
847
848 The mean absolute percentage error (MAPE) and the Change Rate Score are given by:
849
|Real Change Rate − Generated Change Rate|
850 MAPE = × 100%,
|Real Change Rate|
851
852 Change Rate Score = max (cid:0) 0, 100 − Average MAPE (cid:1) .
853
854 The cosine similarity and the Distribution Score are defined as:
855
A · B
856 Cosine Similarity(A, B) = ,
∥A∥ × ∥B∥
857
(cid:0) (cid:1)
858 Distribution Score = max 0, Average Cosine Similarity × 100 .
859
860 The weighted final score is:
861
Final Score = 0.6 × Change Rate Score + 0.4 × Distribution Score.
862
863
16
