---
title: "Mechanism Plausibility in Generative Agent-Based Modeling"
source_pdf: "09_surveys\\04_Mechanism_Plausibility_Zhao2026.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-07-03T12:08:40+00:00
page_count: 26
status: ok
text_char_count: 97730
quality_flags: ["abstract_may_include_layout_noise"]
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\09_surveys\04_Mechanism_Plausibility_Zhao2026.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-07-03T12:08:40+00:00
- Page count: 26
- Status: ok
- Text chars: 97730
- Quality flags: abstract_may_include_layout_noise

## Metadata

- Title: Mechanism Plausibility in Generative Agent-Based Modeling
- Author: Patrick Zhao; David Huu Pham; Nicholas Vincent
- DOI: unknown
- Keywords: Agent-Based Modeling, Mechanisms, Generative Agents, Large Language Models, Philosophy of Science
- Subject: -  Computing methodologies  ->  Simulation evaluation.Model development and analysis.Modeling and simulation.Natural language processing.-  Human-centered computing  ->  Collaborative and social computing design and evaluation methods.

## Extracted Abstract

constructs within the bounds of the experiment, for the sake of falsifiable detection and experimental reproducibility [13]. The process of FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. creating an operational definition for a particular concept is called the “operationalization” of the concept, and determining whether this operational definition measures what it is intended to measure, is called construct validity [20, 28]. Operationalization involves not only translating abstract constructs into measurable patterns, but also assigning interpretations to the formal components of a model. From the modeling and cognitive representation literature [22, 83], we recognize the distinction between a model’s formal functions and the interpretation assigned by the modeler to connect the functions to the domain of interest. Egan distinguishes between what she calls the “theory proper” of a computational model and an “intentional gloss” that accompanies it [22]. The theory proper specifies the mathematical function(s) computed, the algorithms, the structures maintained, and their physical realization. For LLM Agents within a simulation, this would be the next-token probability distribution over a vocabulary, given an input sequence. The intentional gloss is what connects the computation to the modeler’s interpretation, which could be some target persona the modeler says the agent is representing. But as Egan argues, the validity of an intentional gloss is not guaranteed by its computations and requires independent justification, typically grounded in the theorist’s explanatory goals. In our scale interpretation takes the form of an Intent 𝐼 , which we will return to in Section 3.3. Since our focus is on simulation models created by researchers, most researchers have particular phenomena that they would like the simulation to produce [32]. We refer to these phenomena of interest as 𝑇 , the target phenomena, and we expand on this definition in Section 2.2. In our review we find gaps in the operationalization of target phenomena used in the evaluation of recent LLM-based social simulations, further discussed in 5.1. 2.2 Phenomenal Models and Generative Sufficiency The term phenomenal comes from established usage in the scientific modeling field [42, 56], where it is used to describe models that aim to produce the patterns describing a target phenomenon 𝑇 , but do not contain information about the mechanism behind it. They may produce an accurate output without describing the relevant internal structure, therefore limiting their explanatory power. One can imagine that it is not always simple or practical to produce the target phenomenon; In the modeling field, the term generative sufficiency describes the level to which a model is able to accurately produce 𝑇 [32]. Due to the black-box nature of deep neural networks and other practicality reasons, much of the emphasis in the traditional machine learning field is put on the generative sufficiency of different ML models–how accurately they are able to produce a target behavior. At the time of writing, the primary ways to evaluate LLMs are to measure scores they achieve on some benchmark centered around human evaluation or fact-checking. This mentality may have spread to the LLM social simulation area, as initial projects in the space used similar evaluations to benchmark the realism of their simulation. For example, projects using ‘believability’ as a metric for their sufficiency in producing a target behavior [40, 47, 61, 62, 69, 78]. While generative sufficiency could be appropriate for exploratory or illustrative settings, the goals of a model may not be limited to just reproducing the target behavior; One may want to test unknown counterfactual scenarios or interventions. Problematically, these simulations are evaluated based off of their generative sufficiency and then used to test interventions as if there are plausible mechanisms [26, 37]. Phenomenal models cannot be used to test counterfactual scenarios because they lack the relevant internal causal structure. In order to move past being purely phenomenal, the model needs to suggest how 𝑇 is produced: the mechanisms behind it. 2.3 Mechanisms Mechanisms literature has seen a rise in discussion in the past two decades, primarily in the philosophy-of-science and neuroscience fields [17, 30, 53]. Glennan gives a minimal definition for mechanisms in his text, The New Mechanical Philosophy: Mechanism Plausibility in Generative Agent-Based Modeling FAccT ’26, June 25–28, 2026, Montreal, QC, Canada “A mechanism for a phenomenon consists of entities (or parts) whose activities and interactions are organized so as to be responsible for the phenomenon.” [30] Pragmatically, in our discussion of agent-based models and computer simulation, this might include how the agents, environment, and update rules function to produce 𝑇 . A mechanism is involved in the causal process of 𝑇 , not just correlated, and hypothesizing about them is the first step towards explaining a phenomenon. This hypothesis can take the form of a mapping which details what parts of the simulation correspond to mechanisms behind 𝑇 . In our scale the addition of this mapping is what distinguishes a purely phenomenal model from one that presents the plausible candidate mechanisms behind 𝑇 . To explain the mechanisms behind a phenomenon is to explain how the phenomenon is produced (falsifiably). Once some level of description of the mechanisms behind𝑇 are produced, the model is beyond a purely phenomenal account. Kaplan and Craver have summarized these demands into an account called the 3M requirement: “In successful explanatory models in cognitive and systems neuroscience (a) the variables in the model correspond to components, activities, properties, and organizational features of the target mechanism that produces, maintains or underlies the phenomenon, and (b) the (perhaps mathematical) dependencies posited among these variables in the model correspond to the (perhaps quantifiable) causal relations among the components of the target mechanism.” [41] To be clear, an explanation does not need to constitute every detail down to the atomic level; it can use an adequate level of abstraction or idealization to fit the use case of the modeler [18, 74]. For example, in Figure 1, lower-level mechanisms beyond the ‘Agent-level’ could be further explored and abstracted, but may be stubbed at the modeler’s adequate level of abstraction. We note that mechanisms cannot be identified in isolation, and therefore the target phenomena need to be operationalized before identifying any mechanisms. Craver suggests, “mechanistic explanations can fail because one has tried to explain a fictitious phenomenon, because one has mischaracterized the phenomenon, and because one has characterized the phenomenon to be explained only partially.” [19] Mechanisms are not just ‘static’ concepts, they are functions that are defined relative to a phenomenon. Its identity, boundaries, and relevance are all defined by the specific outcome it is supposed to explain [17, 31]. Therefore, as we will see later, in our Mechanism Plausibility Scale the operationalization precedes the hypothesis. 2.4 Mechanisms vs Prediction The focus on the productive process of a phenomenon distinguishes mechanisms from predictivism or correlation. One can use a barometer reading to predict weather, but the changing air pressure it measures is not the mechanism that produces it. In causal inference, this is the difference between observational and interventional questions [65, 66]. A predictive model is appropriate for questions such as “given these initial conditions, what outcomes are likely?” Without plausible mechanisms, however, a model’s predictive outputs are usually only appropriate to the extent that they can be validated against observed outcomes. For scenarios that have been or can be empirically tested, this validation may suffice [71]. But for novel interventions, mechanisms provide the basis for reasoning about whether the model’s outputs are acceptable. This distinction between explanation and prediction is well established and known to be easily conflated [71]. The two goals require different criteria for model evaluation, different relationships to the underlying data-generating process, etc. An explanatory model aims to test causal hypotheses about the process producing 𝑇 ; a predictive model aims to produce accurate forecasts of new observations, and may do so using variables that have no/weak causal relationship to the outcome. Conflating the two is a category error that appears in both classical statistics and, as we argue, in early LLM-ABM work. FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Fig. 1. An adapted Craver diagram [19] showing a simulati ABM, the agents/entities {𝑥 1 , . . . , 𝑥 𝑚} (circles) and activities are further and reciprocally constituted by lower-level mech tractability, but are also why simulations can never be fully 2.5 Plausibility The definition of plausibility can be vague, subjective definition from the Stanford Encyclopedia of Philosop has epistemic support: we have some reason to believe it In this paper, we operationalize plausibility in ABMs 3), which encapsulates factors such as how a simulatio used to justify its parameters, the model’s relationship we are interested in if a model is a faithful represen scholars recently publishing in the LLM-ABM space annotation to support their simulations. We find tha provide support for is elusive for even seasoned and c giving us the primary motivation for developing our s 3 A Mechanism Plausibility Scale Now that we have distinguished explanatory models f for models as plausible explanations. Craver: “For those interested in building plausible to reproduce the input–output mapping of target what is known about the internal machinery by possible, for example, to simulate human skills at m scales; but that is not how most humans multiply Zhao et al. roducing 𝑇 with higher and lower-level mechanisms. In the . . . , 𝜙 𝑛} (arrows) work to produce 𝑇 . The agents in the ABM ms, which are generally abstracted away for the purposes of dated (see Level Ω in Section 3.5). d is often treated as a qualitative property. A general “To say that a hypothesis is plausible is to convey that it en prior to testing.” [9] ed off of its standing on our scale (presented in Section components are operationalized, the type of evidence hypotheses the modeler is presenting, etc. In particular, on of the modeler’s intent. As mentioned previously, ve used believability/plausibility metrics like human e task of identifying what these evaluations actually able researchers when it is applied to LLM simulation, e. m predictive and illustrative ones, we introduce an axis ulations, it will not suffice for simulation 𝑆 simply enomenon 𝑇 . The model is further constrained by ich the inputs are transformed into outputs. It is iplication with two sticks marked with logarithmic 8] Mechanism Plausibility in Generative Agent-Based Modeling If we want a simulation to be a plausible representati 𝑇 – the simulation mechanisms must be adequately cl [41, 83]. We formalize a model as a four-tuple 𝑀 = (𝑆,𝑇 , Intent (𝐼 ), and Evidence (𝐸) (these terms will be fu corresponding four-level Mechanism Plausibility become falsifiable and relevant in explaining its mechan the modeler’s intentions. To make the scale concrete, w (hypothetical) LLM-based simulation of opinion dyna 3.1 Level 0 A Level 0 model is a ‘toy’ simulation or sandbox with which is set of procedures, code, and update rules that to explain. Since mechanisms are defined relative to [17, 31], a model without a target cannot have mechan of a target 𝑇 unintentionally in level 0 as well. 3.1.1 Example. A research team builds a sandbox wh and allowed to post, reply, and share content freely technique. The researcher documents the system and to reproduce or explain. 3.2 Level 1 To reach Level 1, a model must add an operationaliz Models that do not convey anything about the unde being pattern reproduction rather than creating hypo phenomenal; They have an operationally defined 𝑇 a 𝑆 can produce the operationalized patterns of 𝑇 . Ho produce 𝑇 in any way. To put it another way, they are which match a pattern operationalized as 𝑇 . Recently, Level 1 models using LLM agents have b models in cooperation, games, and other environment benchmark how different LLMs perform in those abstr work on placing LLMs in game-theoretic scenarios to The research questions of these simulations often fo {𝑥 0 , 𝑥 1 , . . . , 𝑥 𝑚 }” and are questions of generative suffic More generally, a lot of work uses multi-agent LLM s such as their capacity for cooperation or their inherent LLM agents’ capabilities, not to necessarily explain a generative ABM literature by Larooij et al. [45], we s evaluation metric in this way, which we argue is an as power. The existence of a level 1 bucket also helps to flag if a to produce LLM agents that return the outputs whic behaviors of agents can be heavily influenced by pro desired behavior is perfectly acceptable for a level 1 FAccT ’26, June 25–28, 2026, Montreal, QC, Canada or how 𝑇 is created, it is not sufficient to just reproduce to being a proxy for how 𝑇 may actually be generated : Simulation (𝑆), Target phenomenon (𝑇 ), modeler er defined below). We use this four-tuple to create a le. Models climb our scale as more components of 𝑀 ms, as well as being overall more faithful in representing will revisit at each level a high-level running example: a s on a social media platform. specified modeling goal. It consists of a Simulation 𝑆, nerate outputs but lacks a clearly defined phenomenon enomenon (sometimes referred to as Glennan’s Law) s. We place models that lack explicit operationalization LLM agents are placed on a simulated social network e purpose is to demo and explore a new simulation erves what happens, but has no specified phenomenon arget 𝑇 . ng mechanism are said to be phenomenal, their purpose es with their simulation [17, 18]. Models at level 1 are re considered generatively sufficient if its simulation er, it makes no claims about explanation. 𝑆 exists to rd-coded’ simulations that produce a set of data points used to explore the capabilities of different language he goal is not to accurately model the scenario, but to environments. For example, there exists a multitude of how they act or perform [2, 16, 35, 43, 50]. w the lines of “can some LLM agents produce behaviors y, rather than related to why a behavior was produced. ulations to probe the capabilities of LLMs themselves, ses. The goal of these simulations is to characterize the ific real-world social dynamic. In the survey of recent that many projects use believability as their primary ment of generative sufficiency rather than explanatory LM-based simulation is ‘cheating’. It is entirely feasible roduce 𝑇 through the manipulation of prompts. The t engineering; an engineered prompt that produces a nomenal model. However, if an explanatory claim is FAccT ’26, June 25–28, 2026, Montreal, QC, Canada being made, it can become important to clarify in the forces the correct output, or an intentional abstractio model may be phenomenally ambiguous. 3.2.1 Example. Following our social media model ex produce recognizable polarization patterns, operationa They audit the simulation and report that the LLM ag rate as believable. At this stage, the simulation can serve two purpose LLM agents interacting on a simulated platform. Secon with similar features. Given these agents on this netw expect it to do so again under similar conditions. However, the polarization could be driven by the ag algorithm, or some interaction among them. Therefore behind the phenomenon. 3.3 Level 2 Simulations with a plausibility of level 2 move beyo could possibly be generated. This is achieved when mo and mapping (sometimes called a ‘model key’ [32]) proposed mechanisms responsible for generating 𝑇 . By mechanisms of 𝑇 are related to the simulation code. E Craver’s 3M requirement [41] in Section 2.3. Modeling literature often refers to these post-phenom or ‘logical possibilities’ [5]. One distinguishment of le for reasoning about counterfactual scenarios, given a example, one could reason about how 𝑇 might change Later on in Level 3, when one tries to validate a mod or wrong. It is worth being precise about what the ma 2.1, we distinguish between a model’s computations an mapping is an interpretation that proposes how certa standing in for certain real-world entities and activiti simulation 𝑆 and target 𝑇 and propose different mapp To tie this to LLM-ABM, suppose an agent is initi describing a specific profile; we can imagine the map behavioral patterns of a ‘person’ matching that profile text prediction conditioned on a token sequence, which processes of the described persona, we need the mappin data encodes the relevant distributions about human b empirical question that is scoped to each particular d assumption is reasonable is an open problem that wou 3.3.1 Example. At Level 2, our example researchers emerges in their simulation because agents engage wit the simulated feed algorithm amplifies this by surfaci researchers propose that the LLM agents stand in for Zhao et al. odel’s intent 𝐼 whether the prompt is an ‘artifact’ that a real-world mechanism. Without this clarification, a le, at Level 1, the researchers tweak the simulation to d as some clustering of sentiment scores over time (𝑇 ). s produce polarized discourse that human annotators rst, it demonstrates that polarization can emerge from , it could be used to forecast polarization on platforms structure, polarization reliably emerges, and we might ’ prompts, the network topology, the recommendation model does not serve to identify causal responsibilities eproducing 𝑇 to proposing a hypothesis for how it er specifies their Intent 𝐼 , which includes a hypothesis t connects the components and activities in 𝑆 to the ng this, one states a hypothesis about how the possible er, we discussed and summarized this into Kaplan and al simulations as ‘how-possibly’ simulations [11, 32, 89] 2 from level 1 simulations is that they provide a basis othesis about 𝑇 ’s mechanisms encoded through 𝐼 . For hose mechanisms were different. is what determines if the simulation behavior is right ng in 𝐼 involves epistemically; As discussed in Section he interpretation the modeler assigns to it [22, 83]. The computational components of 𝑆 can be understood as This means that two modelers could look at the same s in 𝐼 . ed through persona prompts or steering vectors [14] g in 𝐼 interpreting the LLM’s outputs as reflecting the nsidering the LLM’s “theory proper” is autoregressive rs questionable structural resemblance to the cognitive o state: the modeler is assuming that the LLM’s training vior. Whether this assumption holds for a given 𝑇 is an ain. As this is a developing field, discerning when this benefit from community discussion. opose a hypothesis and mapping 𝐼 : that polarization ontent that aligns with their initialized viewpoints, and high-engagement content. As part of the mapping, the users on the social media platform, as the affordances Mechanism Plausibility in Generative Agent-Based Modeling FAccT ’26, June 25–28, 2026, Montreal, QC, Canada made on the simulated platform (posting, replying, sharing, and receiving algorithmically ranked content) mirror the same that are available to real users. With this, future interventional questions become answerable relative to the hypothesis. For instance, “what happens if we ablate on the recommendation algorithm?” is now a meaningful experiment to add to evidence 𝐸, because the modeler has specified components they believe to be causally responsible, and exposes the hypothesis and its details to falsification. Level 𝑆 𝑇 𝐼 𝐸 0 ✓ ∅ ∅ ∅ 1 ✓ ✓ ∅ ∅ 2 ✓ ✓ ✓ ∅ 3 ✓ ✓ ✓ ✓ Table 1. Plausibility levels and their relationship to the existence/falsifiability of a model’s components. 3.4 Level 3 A simulation with plausibility level 3 attempts to ground its components in evidence 𝐸, which is used to support or constrain the model’s construction, parameterization, or validation. Since the addition of each previous term in 𝑆,𝑇 , 𝐼 is what makes them falsifiable, this evidence could inform the design of the simulation 𝑆, the operationalization of the target 𝑇 , or the justification for the mapping in 𝐼 . 𝐸 could also come in the form of further constrained experiments, for example, ablations or sensitivity analyses that reinforce the prescribed hypotheses contained in the mapping. A modeler might select initial parameters based off of some observed values from census data, survey results, or prior empirical studies. For example, initializing an agent’s political beliefs based on real-world polling data from a specific region might constitute a piece of evidence 𝐸. Prior work suggests that how-possibly and how-actually explanations may exist on a continuum rather than as a strict dichotomy [12]. Metaphorically, as more evidence is gathered for the conditions postulated in an explanation, the explanation moves along the continuum until it is counted as how-actually. Adopting this viewpoint to our scale, Level 3 can be thought of not as a binary threshold like levels 0 through 2, but a gradient progressing further as the quality, quantity, and directness of that evidence increases towards an unreachable Ω. We return to the question of why evidence can only asymptotically approach a definitive confirmation in Section 3.5. In our discussion in Section 5, we elaborate on the confusion creators of LLM-based social simulations face in gathering relevant evidence 𝐸, particularly when much of the research effort is focused on validating the agent’s internal architecture rather than the emergent social phenomenon. 3.4.1 Example. Continuing the social media polarization example, at Level 3 the researchers ground the simulation by presenting varying evidence 𝐸. They show how agent viewpoint distributions are initialized from real survey data on political attitudes in a specific region and the recommendation algorithm mirrors a documented platform’s ranking function. They run ablation studies showing that reducing the algorithmic amplification component significantly reduces polarization, consistent with prior empirical findings. Whether this evidence is appropriate is a judgment for the standards of their research domain. The model becomes more plausible as more of its components are supported, but the question of “plausible enough” is not one the scale answers, just makes explicit. 3.5 Interpreting the Plausibility Scale Given these levels in their increasing order, it is not to say that simulations of a lower plausibility level are worse. It is of general agreement among scientists and philosophers that idealizations are useful, if not, necessary in FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. Fig. 2. The Plausibility scale classifies models based on their epistemic contribution. Level Ω is considered the unreachable simulation that we can approach along level 3 continuously. building models [8, 23, 63]. Our scale clarifies the kind of epistemic contribution each simulation can provide. Some simulations demonstrate that a pattern can be generated, others propose and test explanations for how it can arise. Morgan and Morrison aptly describe that models can function as partially autonomous instruments that mediate between theory and data without being fully derived from either [59]; they can serve as tools for exploration even when they are known to be incomplete or idealized. For example, level 0 simulations like cellular automata can demonstrate that emergent behavior can arise from simple rules, which sets the ground for new simulation paradigms. Level 2 simulations can be used to generate “how-possibly” hypotheses which are falsifiable at the mechanisms level. What increases as we move up the scale is the number of commitments the model has made that can, in principle, be shown to be wrong, and scope of the claims it can support. At Level 1, only the reproduction of 𝑇 is at stake. At Level 2, the mapping 𝐼 becomes an additional falsifiable commitment. At Level 3, the empirical grounding 𝐸 opens further points of potential failure. In addition, the confidence that the operationalized components of 𝑆 faithfully capture the abstract constructs and hypotheses the modeler intends them to represent, becomes increasingly examinable as more of the model’s structure is made explicit and subject to evidence. We file all of this under the umbrella term of ‘plausibility’. It is also of note that each term in 𝑀 = (𝑆,𝑇 , 𝐼, 𝐸) is sequentially dependent on the previous terms for moving up plausibility levels. Consider a counterexample where a simulation 𝑆 only has component 𝐸. If there is no 𝑇 and 𝐼 , the pair of 𝑆 and 𝐸 stands as a pairing of simulation outputs and arbitrary ‘facts’, with no clear mapping between them. Thus, 𝑇 and 𝐼 are necessary relational structures that, when composed in sequence as (𝑆,𝑇 , 𝐼, 𝐸), turn sets of unrelated facts into points of evidence which support a hypothesis. This is also why Table 1 can be helpful, as it shows each level depends on the inclusion of all previous terms. 3.5.1 The unreachable Ω simulation. Finally, we describe the theoretical unreachable model where every mechanism for a target phenomenon is described and leaves no doubt as to whether 𝑆 is a faithful representation of 𝑇 . In the mechanist’s view, to fully describe the mechanisms of a phenomenon is to explain it. We refer to this as a Level Ω simulation and note that it is a fiction we may never reach. As Brandon [12] argues, how-possibly explanations can be thought of as a continuum toward how-actually, as more evidence is accumulated for their postulated conditions. In our scale, Level Ω (see Figure 2) represents the (fictional) endpoint of this continuum where all postulated conditions are fully confirmed and we are sure that the mechanisms in 𝑆 are the mechanisms responsible for producing 𝑇 in actuality. However, Bokulich [11] suggests that as evidence confirms a mechanism at one level of abstraction, attempts to specify that mechanism open new branches of how-possibly explanation, each requiring their own evidence. Following this, the approach toward Ω may be better thought of as a “branching” process in which settling one question reveals further open ones that are implicitly abstracted away when unanswered. Moreover, a related limitation arises from the more general relationship between evidence and theory. The Duhem-Quine thesis, loosely, holds that hypotheses are never tested in isolation, therefore the unambiguous falsification of a scientific hypothesis is impossible [21, 68]. Another reason why we can never reach the Ω Level Mechanism Plausibility in Generative Agent-Based Modeling is that when a model is tested against empirical obse attributed to particular components. It is important to characterize the Ω level both beca and because it makes explicit that one cannot confir behind a phenomenon. 4 The Mechanism Plausibility Scale Heuristic We draw on existing frameworks for reporting on mac and present a checklist for using the Mechanism Plausib are long-standing, established problems in science, th with putting out artifacts that are epistemically cohesi evidence are aligned and appropriately scoped to one an A we follow examples using historical ABMs, one for 5 Discussion In the following section we review some popular ways we engage with broader ethical and epistemic conside over historical examples and issues where the unders 5.1 Reflections on the State of LLM Social Simu “How can we use LLM social simulation practically?” G behind a phenomenon (as discussed in Section 3.5) th are LLM-ABMs adequate for a given purpose?” The current state of affairs for LLM social simulatio producing a target phenomenon. On the surface, the further up the “generative sufficiency scale”, allowin new work in the area. This focus on generative suffi al., where 22 out of 35 surveyed LLM social simulatio metric [45]. Here, the believability of an agent actio (experimentally as part of a study, or simply by inspe (Level 1) may be adequate for demonstrating that a ph such as brainstorming and prototyping. However, if a m that have not been observed – for example, how a pol implicitly making a claim about which components claim, whether or not the modeler frames it as such. The field of machine learning revolves around lear observed examples. The primary goal for many pape workings are often considered a separate topic from is the goal. However, there are a couple of caveats w the evaluation of a functioning/believable LLM agent simulation in exploring unknown scenarios, where p for producing relevant counterfactuals. We observe that LLM-based simulation is prone to co validation. What do we mean by this? From the age presupposed mechanism – they are generally not the FAccT ’26, June 25–28, 2026, Montreal, QC, Canada tions, a failure (or success) cannot unambiguously be of the inevitable idealizations introduced into models, hat a simulation has fully described the mechanisms e learning datasets and model deployments [29, 58, 85] y Scale. While hypothesis testing and operationalization ovelty of LLM-ABMs may lead researchers to struggle where the target phenomenon, claims, and supporting er. In Figure 3 we present the heuristic and in Appendix h level in the scale. Ms are currently being used in simulation. Later in 5.3, ons for using LLM in simulation. In Section 5.4, we go fication of models may have caused real-world harms. ion n that no simulation can fully exhaust the mechanisms uestion is best interpreted as, “Under what conditions ve a focus on demonstrating a simulation is capable of ition of LLMs in social simulation seemed to move us ents to access a larger action space, which prompted cy is reflected in the systematic review by Larooij et apers used ‘believability’ as their primary validation r simulation outcome is judged by humans or LLMs n). A simulation validated only through believability omenon can be generated, or for exploratory purposes ler wishes to test what would happen under conditions intervention might alter the dynamics of 𝑇 – they are are causally responsible for 𝑇 . This is a mechanistic g unknown functions or distributions from real-world may be predictive accuracy, and the model’s internal mpirical evaluations. This is no problem if prediction LLM social simulation: many LLM-ABM projects use enerative sufficiency to justify the usefulness of their ible mechanisms instead would be the relevant factor tion of agent-level validation for ABM/simulation-level based modeling perspective, a functioning agent is a et phenomena of interest. An agent’s behaviors would FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. Mechanism Plausibility Scale Heuristic (𝑆,𝑇 , 𝐼, 𝐸) This scale grades the model’s contribution as a plausible explanation for a target phenomenon. While not every model’s goal is to be explanatory, it is important to clarify when it is appropriate. Level 0: Simulation (𝑆) – Sandbox/Toy Model □ Simulation. Is the simulation (S) defined, including environments, agents, and update rules? The requirements for Level 0 are relatively minimal; It essentially shares the same requirements for something to be considered an ABM or simulation, and mainly exists to distinguish it from the other levels. Level 0 simulations are often toys or demonstrations of new simulation paradigms (e.g., Conway’s Game of Life, a demo for a new simulation framework/technique). Level 1: Target Phenomenon (𝑇 ) – Phenomenal Model □ Defined Target Phenomenon. Is a target phenomenon (𝑇 ) operationalized (e.g. as statistical patterns, human annotations/observations, etc.)? □ Generative Sufficiency. Can the simulation (𝑆) successfully generate the patterns described in (𝑇 )? □ Reproducibility. Does the reproducibility of the simulation (seeds, API versions, consideration of proprietary prompt injections or version changes, inherent stochasticity, etc.) match the reproducibility goals of the modeler or the field they are working in (sensitivity analysis requirements, etc.)? The Level 1 requirement checks if there are explicit conditions that determine if the phenomena have happened and if the model produces the specified phenomena. Level 1 simulations often show that something (𝑇 ) is possible or achievable using the entities and activities of the simulation (e.g. Can LLM agents solve games, pass theory of mind, benchmarks, etc.). Level 2: Intent & Mapping (𝐼) – How-Possibly Model □ Simulation Contribution. Is the simulation’s use case understood (e.g., predictive, exploratory, illustrative, explanatory, etc.)? □ Falsifiable Hypotheses. Does there exist a hypothesis for how the target phenomenon 𝑇 arises from components in the model? □ Mechanism Mapping. Is there an Intent 𝐼 (implicit or explicit mapping) which connects components of the simulation (𝑆) to the hypothesized ‘real-world’ mechanisms of (𝑇 )? Level 2 is a check for if the modelers have explicitly proposed how the phenomena (or parts of the phenomena) of interest are produced using the components of their simulation. This is important to make the model falsifiable. Level 3: Evidence (𝐸) – Plausible Model (if validated) □ Evidence Exists. Is the model supported by some evidence 𝐸? □ Relevance. Is 𝐸 directed towards the claims made in 𝐼? Could 𝐸, in principle, disconfirm the hypotheses in 𝐼? Adding any 𝐸 to get a simulation to Level 3 is straightforward; The difficulty lies in the model to remain valid, as the 𝐸 becomes additional falsifiable parts of the model. What is considered acceptable 𝐸 is bounded by the standards of the domain the model is in. Conclusion: Based on the checklist, the model is classified as a Level [X] model. Fig. 3. The Mechanism Plausibility Scale in checklist form. have been manually programmed in classic agent-based models, and a non-functioning agent would have meant that the programmer made a bug. In our own attempts to review ABM papers that employ LLM-driven agents, Mechanism Plausibility in Generative Agent-Based Modeling we found that works tended to focus heavily on justif given that LLM-driven agents are a relatively new s intentional gloss is not guaranteed by the theory prop the agent architecture (e.g., showing the agent can rem 𝐼 concerning a higher-level social phenomenon 𝑇 . A 𝑆, but its functionality alone does not validate the m simulation-level mechanisms, we refer to the visual m [19] showing how the overall phenomena 𝑇 is produc An open question is how current LLM simulation given the discussed limitations so far. While we do no practitioners already reason about simulations in w ran a year-long human co-design of simulations wit 2024-2025 [49]. The policymakers seemed to show sk the agents exhibited believable behavior. Instead, the s tool. For example, when a simulation’s dynamics we tacit knowledge and allowed them to list out importan settings. This has echoes in work done by Park et al. [ designers identify and prototype solutions to potentia The preparedness team began to trust the simulations scenarios, when the authors tested it against their in Once the policymakers saw that the simulations gen experience and intuition, they were willing to entertain higher-level, abstracted mechanisms. 5.2 Proprietary LLM APIs and Reproducibility LLM API services have been known to introduce pro the end user. These features are added for safety, regu detrimental to experimental validity. For example, hid an agent’s behavior or prevent agents from exhibiting r proprietary LLMs are often subject to unannounced ve behavior between runs. This problem is solvable with to entry for many researchers because of things like G Concerning ethical considerations of proprietary m practices that fall below disciplinary ethical standa practices involving underpaid workers, the inclusion methodological and epistemic side, closed-process (tra the community’s ability to inspect training data, att rigorous control over their scientific methodology. There are growing movements toward addressing t have demonstrated that competitive language mode and intermediate checkpoints, with the goal of enabli Network advocates for treating AI as public infrastru produce permanent public goods [38]. However, at the both commercial deployment and research usage. 1See https://github.com/asgeirtj/system_prompts_leaks and similar FAccT ’26, June 25–28, 2026, Montreal, QC, Canada g their design of LLM-driven agents; this makes sense lation technique. However, just as the validity of an Section 2.1), evidence supporting the functionality of er facts) is not sufficient as evidence 𝐸 for the mapping nctioning agent is a necessary part of the simulation el’s explanation of 𝑇 . To distinguish agent-level and phor in Figure 1, which is a modified Craver diagram by agents {𝑥 1 , . . . , 𝑥 𝑚 } and activities {𝜙 1 , . . . , 𝜙 𝑛 }. an be made useful for policy or sociological settings tempt to answer this fully, recent work suggests that that align with the distinctions in our scale. Li et al. heir university’s emergency preparedness team from cism towards any models’ predictive abilities, even if ulations seemed to help them more as a brainstorming dentified to be wrong, it resurfaced the policymakers’ oncerns, for example, wheelchair ramps in evacuation where ‘false’ simulated social media platforms helped oblems before they came up in a real deployed setting. e once the simulations started to align with real-world ution’s real-world graduation commencement setting. ted behavior that matched outcomes based on their ‘how-possibly’ outcomes generated by the simulation’s injections, guardrails, or system prompts invisible to on, or other proprietary purposes but can be actively prompts could unknowingly change the trajectory of vant behavior the modeler is interested in. Furthermore, on or system prompt1 updates, which could alter agent n-sourced locally hosted models, but raises the barrier and technical constraints. ls, LLM training data is frequently assembled through for example, mass scraping without consent, labor rivate data, and environmental harms [34, 80]. On the ng sources and methods, weights) models compromise ute model behavior to appropriate sources, and have concerns. Initiatives such as AI2’s OLMo project [33] an be developed with fully open training data, code, he scientific study of language models. The Public AI re – publicly accessible, accountable, and designed to e of writing, proprietary models continue to dominate n-the-wild examples. FAccT ’26, June 25–28, 2026, Montreal, QC, Canada 5.3 Broader Ethical and Epistemic Concerns The problems related to reproducibility, proprietary mechanistic plausibility are largely methodological. H about the use of LLMs in social simulation that warra Regarding whether LLMs should serve as proxies for proposals to substitute human research participants w with values relating to representation, inclusion, and with LLMs may disregard the relationship between research. When an LLM generates text that resembl from the experience of a live, present individual. Furth referenced by Weidinger et al. [81]. LLMs encode th particular point in time. Related empirical work suppo time periods not represented in their training corpus 5.4 Historical Issues and Harms of Poor ABM s While the Mechanism Plausibility Scale was motivate not specific to ABMs with LLMs; The literature surro long-standing discussion [6, 45, 60, 72, 74, 76]. Importa is not only important to the modeler herself, but also Squazzoni et al. [72] note that during the COVID reported that results from their model projected “a h policy measures were taken”. The results of their mode by the UK government, and advised governments of cou the damages caused by the virus. However, because of u model erroneously affected the policies of many count further peer analysis of the model showed it may onl the simulation code was not made public, even later a Axelrod’s iterated Prisoner’s Dilemma (PD) simu adapted script on “The Evolution of Cooperation” [7] arms races, nuclear proliferation, and crisis bargaining advice to players of the game theoretic scenario might and Alexandrova [60] observe that despite the enormo 1960), it has largely failed to explain phenomena of so Arnold (sharply) observes a broader pattern in the simulations produced practically no successful empir He identifies, firstly, the “justificatory narratives” mod the model is merely heuristic or exploratory without sp arguing that all models rely on simplification, a defens a model isolates are empirically discernible from the o not, the simplification cannot be tested. We felt it appropriate to reiterate these issues unde growing interest in simulation using LLMs. Zhao et al. Is, and the conflation of generative sufficiency with ever, there are broader ethical and epistemic concerns onsideration. man subjects in the first place, Agnew et al. [1] examine LLM surrogates and find that such proposals conflict erstanding of human subjects. Replacing participants earcher and subject existing in prior human subject urvey responses or social behavior, it is not directly more, they identify the problem of “value lock-in”, also orms and attitudes present in their training data at a his; language models exhibit degraded performance in . ification y recent challenges posed by LLM-ABM, the ideas are ing well-motivated, sound ABM design in general is a y, we demonstrate how understanding a model’s limits s end users. pandemic, a team at the Imperial College of London number of people would die in Britain unless severe d interventions were quickly adopted and implemented ies like the US and France in their attempts to minimize erspecification on what the model was adequate for, the , namely, being used in counterfactual scenarios when ave been adequate for illustrative purposes. Moreover, e time of Squazzoni et al.’s publication. ons are another well-known problematic case. In an xelrod asserts that many real-world scenarios such as instances of the iterated Prisoner’s Dilemma, and that ve as advice to national leaders. In response, Northcott attention devoted to the PD (over 16,000 articles since scientific interest. deling tradition [6]: over thirty years of Repeated PD applications, yet this failure has been largely ignored. rs use after scrutiny, which is retreating to claims that fying the limits of that exploration. Secondly, modelers at, as Arnold notes, only holds when the causal factors r factors at work in the target system. When they are ur scale and point to related work, especially with the Mechanism Plausibility in Generative Agent-Based Modeling 6 Conclusion and Limitations In this paper we connect contemporary mechanisms, literature with agent-based modeling and LLM social s heuristic that classifies simulations into levels based and offer a practical checklist. Through a review of rec category errors between Agent-level and ABM-level these problems with existing issues in ABM and highlig happened in high-stakes scenarios. While our scale p refined to differentiate the quality and extent of eviden be said about a separate axis for predictive models, as of the paper, ultimately, remains grounding multiple d to attention. Generative AI Usage Statement This document was produced with the assistance of G checklists, figures, proofreading, and typographical lay authors also used AI-augmented paper search engines References [1] William Agnew, A. Stevie Bergman, Jennifer Chien, Mark D McKee. 2024. The illusion of artificial inclusion. In Proceedin doi:10.1145/3613904.3642703 arXiv:2401.08572 [cs]. [2] Elif Akata, Lion Schulz, Julian Coda-Forno, Seong Joon Oh, Ma Language Models. Nature Human Behaviour (May 2025). doi: [3] Altera AL, Andrew Ahn, Nic Becker, Stephanie Carroll, Nico Luo, Peter Y. Wang, Mathew Willows, Feitong Yang, and Guan civilization. doi:10.48550/arXiv.2411.00114 arXiv:2411.00114 [ [4] Jacy Reese Anthis, Ryan Liu, Sean M. Richardson, Austin C. K Bernstein. 2025. LLM Social Simulations Are a Promising Res [5] Eckhart Arnold. 2013. Simulation Models of the Evolution of C E Politica 15, 2 (2013), 101–138. https://philarchive.org/rec/AR [6] Eckhart Arnold. 2015. How Models Fail: A Critical Look at th Collective Agency and Cooperation in Natural and Artificial Sy 261–279. doi:10.1007/978-3-319-15515-9_14 [7] Robert Axelrod. [n. d.]. The Evolution of Cooperation*. ([n. d.] [8] N. Emrah Aydinonat. 2024. The puzzle of model-based explan ed.). Routledge, London, 177–192. doi:10.4324/9781003205647 [9] Paul Bartha. 2024. Analogy and Analogical Reasoning. In The S Nodelman (Eds.). Metaphysics Research Lab, Stanford Universit [10] James Bogen and James Woodward. 1988. Saving the Phen doi:10.2307/2185445 [11] Alisa Bokulich. 2014. How the Tiger Bush Got its Stripes: ‘How 2014), 321–338. doi:10.5840/monist201497321 [12] Robert N. Brandon and Robert N. Brandon. 2014. Adaptat 10.1515/9781400860661 [13] P. W. (Percy Williams) Bridgman. 1927. The Logic of Modern P [14] Runjin Chen, Andy Arditi, Henry Sleight, Owain Evans, and Ja Traits in Language Models. doi:10.48550/arXiv.2507.21509 arX 2https://asta.allen.ai/chat FAccT ’26, June 25–28, 2026, Montreal, QC, Canada nitive representation, and other philosophy of science lation. We present the Mechanism Plausibility Scale, a he falsifiability and existence of components 𝑆,𝑇 , 𝐼, 𝐸 LLM-ABM papers we confirm the existence of common ponents and underspecified models. We also connect he historical harms that occurred when these mistakes des a useful heuristic, the criteria for Level 3 could be 𝐸 for a more practical setting. Additionally, more could osed to our plausible explanation axis. The main focus plines in common language and bringing these issues erative AI, which assisted in the formatting of tables, of the paper. It was also used to generate critique; the ch as Asta2, for paper discovery. Seliem El-Sayed, Jaylen Pittman, Shakir Mohamed, and Kevin R. the CHI Conference on Human Factors in Computing Systems. 1–12. s Bethge, and Eric Schulz. 2025. Playing repeated games with Large 38/s41562-025-02172-y arXiv:2305.16867 [cs]. tie, Manuel Cortes, Arda Demirci, Melissa Du, Frankie Li, Shuying Robert Yang. 2024. Project Sid: Many-agent simulations toward AI owski, Bernard Koch, James Evans, Erik Brynjolfsson, and Michael Method. doi:10.48550/arXiv.2504.02234 arXiv:2504.02234 [cs]. ration as Proofs of Logical Possibilities. How Useful Are They? Etica MO Publisher: University of Trieste, Department of Philosophy. story of Computer Simulations of the Evolution of Cooperation. In , Catrin Misselhorn (Ed.). Springer International Publishing, Cham, tps://ee.stanford.edu/~hellman/Breakthrough/book/pdfs/axelrod.pdf n. In The Routledge Handbook of Philosophy of Scientific Modeling (1 rd Encyclopedia of Philosophy (fall 2024 ed.), Edward N. Zalta and Uri ps://plato.stanford.edu/archives/fall2024/entries/reasoning-analogy/ na. The Philosophical Review 97, 3 (1988), 303–352. jstor:2185445 sibly’ vs. ‘How Actually’ Model Explanations. The Monist 97, 3 (July nd environment. Princeton University Press, Princeton. doi:doi: s. The Macmillan Company. ndsey. 2025. Persona Vectors: Monitoring and Controlling Character 507.21509 [cs]. FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. [15] Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu, Yaxi Lu, Yi-Hsin Hung, Chen Qian, Yujia Qin, Xin Cong, Ruobing Xie, Zhiyuan Liu, Maosong Sun, and Jie Zhou. 2023. AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors. doi:10.48550/arXiv.2308.10848 arXiv:2308.10848 [cs]. [16] Anthony Costarelli, Mat Allen, Roman Hauksson, Grace Sodunke, Suhas Hariharan, Carlson Cheng, Wenjie Li, and Arjun Yadav. 2024. GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents. doi:10.48550/arXiv.2406.06613 arXiv:2406.06613 [cs] version: 1. [17] Carl Craver, James Tabery, and Phyllis Illari. 2024. Mechanisms in Science. In The Stanford Encyclopedia of Philosophy (fall 2024 ed.), Edward N. Zalta and Uri Nodelman (Eds.). Metaphysics Research Lab, Stanford University. https://plato.stanford.edu/archives/fall2024/ entries/science-mechanisms/ [18] Carl F. Craver. 2006. When mechanistic models explain. Synthese 153, 3 (Dec. 2006), 355–376. doi:10.1007/s11229-006-9097-x [19] Carl F. Craver. 2009. Explaining the Brain. Oxford University Press. [20] Lee J. Cronbach and Paul E. Meehl. 1955. Construct validity in psychological tests. Psychological Bulletin 52, 4 (1955), 281–302. doi:10.1037/h0040957 Place: US Publisher: American Psychological Association. [21] Pierre Maurice Marie Duhem. 1954. The aim and structure of physical theory. Vol. 1. Princeton University Press. Pages: 85-87. [22] Frances Egan. 2025. Deflating Mental Representation (The Jean Nicod Lectures). MIT Press (open access). [23] Catherine Z. Elgin. 2004. True Enough. Philosophical Issues 14 (2004), 113–131. https://www.jstor.org/stable/3050623 Publisher: [Wiley, Ridgeview Publishing Company]. [24] Joshua M. Epstein. 2006. Generative Social Science: Studies in Agent-Based Computational Modeling (stu - student edition ed.). Princeton University Press. http://www.jstor.org/stable/j.ctt7rxj1 [25] Ronald Aylmer Fisher. 1999. The genetical theory of natural selection: by R.A. Fisher ; edited with a foreword and notes by J.H. Bennett (a complete variorum ed ed.). Oxford University Press, Oxford. [26] Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, and Yong Li. 2025. S$^3$: Social-network Simulation System with Large Language Model-Empowered Agents. arXiv:2307.14984 [cs] doi:10.48550/arXiv.2307.14984 [27] Martin Gardner. 1970. Mathematical Games. Scientific American 223, 4 (1970), 120–123. https://www.jstor.org/stable/24927642 Publisher: Scientific American, a division of Nature America, Inc.. [28] Edward G.Carmines and Richard A.Zeller. 1979. Reliability and Validity Assessment. SAGE Publications, Inc. doi:10.4135/9781412985642 [29] Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, and Kate Crawford. 2021. Datasheets for Datasets. doi:10.48550/arXiv.1803.09010 arXiv:1803.09010 [cs]. [30] Stuart Glennan. 2017. The New Mechanical Philosophy. Oxford University Press, Oxford. [31] Stuart S. Glennan. 1996. Mechanisms and the nature of causation. Erkenntnis 44, 1 (Jan. 1996), 49–71. doi:10.1007/BF00172853 [32] Claudius Graebner. 2018. How to Relate Models to Reality? An Epistemological Framework for the Validation and Verification of Computational Models. Journal of Artificial Societies and Social Simulation 21, 3 (2018), 8. [33] Dirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord, Ananya Harsh Jha, Hamish Ivison, Ian Magnusson, Yizhong Wang, Shane Arora, David Atkinson, Russell Authur, Khyathi Raghavi Chandu, Arman Cohan, Jennifer Dumas, Yanai Elazar, Yuling Gu, Jack Hessel, Tushar Khot, William Merrill, Jacob Morrison, Niklas Muennighoff, Aakanksha Naik, Crystal Nam, Matthew E. Peters, Valentina Pyatkin, Abhilasha Ravichander, Dustin Schwenk, Saurabh Shah, Will Smith, Emma Strubell, Nishant Subramani, Mitchell Wortsman, Pradeep Dasigi, Nathan Lambert, Kyle Richardson, Luke Zettlemoyer, Jesse Dodge, Kyle Lo, Luca Soldaini, Noah A. Smith, and Hannaneh Hajishirzi. 2024. OLMo: Accelerating the Science of Language Models. doi:10.48550/arXiv.2402.00838 arXiv:2402.00838 [cs]. [34] Olivia Guest and Iris van Rooij. 2025. Critical Artificial Intelligence Literacy for Psychologists. doi:10.31234/osf.io/dkrgj_v1 [35] Fulin Guo. 2023. GPT in Game Theory Experiments. doi:10.48550/arXiv.2305.05516 arXiv:2305.05516 [econ]. [36] John J. Horton. 2023. Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? doi:10.48550/ arXiv.2301.07543 arXiv:2301.07543 [econ]. [37] Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jianchao Ji, Yingqiang Ge, Libby Hemphill, and Yongfeng Zhang. 2024. War and Peace (WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars. doi:10.48550/arXiv.2311.17227 arXiv:2311.17227 [cs]. [38] Brandon Jackson, B Cavello, Flynn Devine, Nick Garcia, Samuel J. Klein, Alex Krasodomski, Joshua Tan, and Eleanor Tursman. 2024. Public AI: Infrastructure for the common good. doi:10.5281/zenodo.13914560 [39] Frank Jackson. 1982. Epiphenomenal Qualia. The Philosophical Quarterly 32, 127 (April 1982), 127–136. doi:10.2307/2960077 [40] Zhao Kaiya, Michelangelo Naim, Jovana Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo, Guangyu Robert Yang, and Andrew Ahn. 2023. Lyfe Agents: Generative Agents for Low-Cost Real-Time Social Interactions. arXiv:2310.02172 [cs] doi:10.48550/arXiv.2310.02172 [41] David Michael Kaplan and Carl F. Craver. 2011. The Explanatory Force of Dynamical and Mathematical Models in Neuroscience: A Mechanistic Perspective*. Philosophy of Science 78, 4 (2011), 601–627. doi:10.1086/661755 Publisher: [The University of Chicago Press, Philosophy of Science Association]. [42] Kendrick N. Kay. 2018. Principles for models of neural information processing. NeuroImage 180 (Oct. 2018), 101–109. doi:10.1016/j. neuroimage.2017.08.016 Mechanism Plausibility in Generative Agent-Based Modeling [43] Benjamin Kempinski, Ian Gemp, Kate Larson, Marc Lanctot, Reasoning in Game-Theoretic Domains with Large Language M Agents and Multiagent Systems (AAMAS ’25). International Fou 1088–1097. [44] J. R. Landis and G. G. Koch. 1977. The measurement of observe [45] Maik Larooij and Petter Törnberg. 2025. Do Large Language M Generative Social Simulations. doi:10.48550/arXiv.2504.03274 [46] Angeliki Lazaridou, Adhiguna Kuncoro, Elena Gribovskaya de Masson d’Autume, Tomas Kocisky, Sebastian Ruder, Dani Y Gap: Assessing Temporal Generalization in Neural Language [47] Huao Li, Yu Quan Chong, Simon Stepputtis, Joseph Campbell, Multi-Agent Collaboration via Large Language Models. In Proc Processing. 180–192. doi:10.18653/v1/2023.emnlp-main.13 arX [48] Xinyi Li, Yu Xu, Yongfeng Zhang, and Edward C. Malthouse. Diffusion Under Different Network Structures. doi:10.48550/a [49] Yuxuan Li, Sauvik Das, and Hirokazu Shirado. 2025. What Ma Design Engagement in Emergency Preparedness. doi:10.48550 [50] Yuxuan Li and Hirokazu Shirado. 2025. Spontaneous Giving a arXiv:2502.17720 [cs]. [51] Yuhan Liu, Xiuying Chen, Xiaoqing Zhang, Xing Gao, Ji Zha Attitude Dynamics Toward Fake News. In Proceedings of the Thi doi:10.24963/ijcai.2024/873 arXiv:2403.09498 [cs]. [52] Kenneth MacCorquodale and Paul E. Meehl. 1948. On a Di Psychological Review 55, 2 (1948), 95–107. doi:10.1037/h00560 [53] Peter Machamer, Lindley Darden, and Carl F. Craver. 2000. https://www.jstor.org/stable/188611 Publisher: [The Universit [54] Giordano De Marzo, Luciano Pietronero, and David Garcia. 202 Language Models. doi:10.48550/arXiv.2312.06619 arXiv:2312.0 [55] Michela Massimi. 2022. Perspectival Ontology: Between Situ 214–228. doi:10.1093/monist/onab032 [56] Michael D. Mauk. 2000. The potential effectiveness of simula 2000), 649–651. doi:10.1038/76606 Publisher: Nature Publishin [57] James W. McAllister. 1997. Phenomena and Patterns in Data Se 1005387021520 [58] Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barne and Timnit Gebru. 2019. Model Cards for Model Reporting. In P 220–229. doi:10.1145/3287560.3287596 arXiv:1810.03993 [cs]. [59] Mary S. Morgan and Margaret Morrison (Eds.). 1999. Mode University Press, Cambridge. doi:10.1017/CBO9780511660108 [60] Robert Northcott and Anna Alexandrova. 2015. Prisoner’s philosophical arguments., Martin Peterson (Ed.). Cambridge Un [61] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith R Agents: Interactive Simulacra of Human Behavior. doi:10.4855 [62] Joon Sung Park, Lindsay Popowski, Carrie Cai, Meredith Ring Creating Populated Prototypes for Social Computing Systems. and Technology (Oct. 2022), 1–18. doi:10.1145/3526113.3545616 Interface Software and Technology ISBN: 9781450393201 Plac [63] Wendy S. Parker. 2020. Model Evaluation: An Adequacy-for-Pu 708691 [64] Debjit Paul, Robert West, Antoine Bosselut, and Boi Faltings. 2 Chain-of-Thought Reasoning. arXiv. doi:10.48550/ARXIV.2402 [65] Judea Pearl. 2009. Causality (2 ed.). Cambridge University Pre [66] Judea Pearl and Dana Mackenzie. 2018. The book of why: The [67] Axel Pichler and Nils Reiter. 2022. From Concepts to Texts a Journal of Cultural Analytics 7, 4 (Dec. 2022). doi:10.22148/001 FAccT ’26, June 25–28, 2026, Montreal, QC, Canada m Bachrach, and Tal Kachman. 2025. Game of Thoughts: Iterative ls. In Proceedings of the 24th International Conference on Autonomous tion for Autonomous Agents and Multiagent Systems, Richland, SC, eement for categorical data. Biometrics 33, 1 (March 1977), 159–174. s Solve the Problems of Agent-Based Modeling? A Critical Review of v:2504.03274 [cs]. vang Agrawal, Adam Liska, Tayfun Terzi, Mai Gimenez, Cyprien ama, Kris Cao, Susannah Young, and Phil Blunsom. 2021. Mind the els. doi:10.48550/arXiv.2102.01951 arXiv:2102.01951 [cs]. Hughes, Michael Lewis, and Katia Sycara. 2023. Theory of Mind for ngs of the 2023 Conference on Empirical Methods in Natural Language 10.10701 [cs]. . Large Language Model-driven Multi-Agent Simulation for News 2410.13909 arXiv:2410.13909 [cs]. LM Agent Simulations Useful for Policy? Insights From an Iterative iv.2509.21868 arXiv:2509.21868 [cs]. alculated Greed in Language Models. doi:10.48550/arXiv.2502.17720 nd Rui Yan. 2024. From Skepticism to Acceptance: Simulating the hirdInternational Joint Conference on Artificial Intelligence. 7849–7857. tion between Hypothetical Constructs and Intervening Variables. king about Mechanisms. Philosophy of Science 67, 1 (2000), 1–25. Chicago Press, Philosophy of Science Association]. mergence of Scale-Free Networks in Social Interactions among Large [physics]. Knowledge and Multiculturalism. The Monist 105, 2 (March 2022), s versus phenomenological models. Nature Neuroscience 3, 7 (July oup. rkenntnis (1975-) 47, 2 (1997), 217–228. jstor:20012798 doi:10.1023/A: cy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, edings of the Conference on Fairness, Accountability, and Transparency. Mediators: Perspectives on Natural and Social Science. Cambridge mma Doesn’t Explain Much. In The Prisoner?s Dilemma. Classic sity Press, 64–84. https://philarchive.org/rec/NORPDD l Morris, Percy Liang, and Michael S. Bernstein. 2023. Generative Xiv.2304.03442 arXiv:2304.03442 [cs]. orris, Percy Liang, and Michael S. Bernstein. 2022. Social Simulacra: edings of the 35th Annual ACM Symposium on User Interface Software ference Name: UIST ’22: The 35th Annual ACM Symposium on User nd OR USA Publisher: ACM. e View. Philosophy of Science 87, 3 (July 2020), 457–477. doi:10.1086/ Making Reasoning Matter: Measuring and Improving Faithfulness of 50 Version Number: 4. ambridge. doi:10.1017/CBO9780511803161 cience of cause and effect (1 ed.). Basic Books, Inc., USA. Back: Operationalization as a Core Activity of Digital Humanities. 195 FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. [68] Willard Van Orman Quine. 1953. From a Logical Point of View. Harvard University Press, Cambridge. [69] Siyue Ren, Zhiyao Cui, Ruiqi Song, Zhen Wang, and Shuyue Hu. 2024. Emergence of Social Norms in Generative Agent Societies: Principles and Architecture. doi:10.48550/arXiv.2403.08251 arXiv:2403.08251 [cs]. [70] Thomas C. Schelling. 1969. Models of Segregation. The American Economic Review 59, 2 (1969), 488–493. https://www.jstor.org/stable/ 1823701 Publisher: American Economic Association. [71] Galit Shmueli. 2010. To Explain or to Predict? Statist. Sci. 25, 3 (Aug. 2010). doi:10.1214/10-STS330 [72] Flaminio Squazzoni, J. Gareth Polhill, Bruce Edmonds, Petra Ahrweiler, Patrycja Antosz, Geeske Scholz, Emile Chappin, Melania Borit, Harko Verhagen, Francesca Giardini, and Nigel Gilbert. 2020. Computational Models That Matter During a Global Pandemic Outbreak: A Call to Action. JASSS - The Journal of Artificial Societies and Social Simulation 23, 2 (March 2020). doi:10.18564/jasss.4298 [73] S. S. Stevens. 1935. The Operational Definition of Psychological Concepts. Psychological Review 42, 6 (1935), 517–527. doi:10.1037/h0056973 [74] Samarth Swarup. 2019. Adequacy: What Makes a Simulation Good Enough?. In 2019 Spring Simulation Conference (SpringSim). 1–12. doi:10.23919/SpringSim.2019.8732895 [75] Edward Bradford Titchener. 1910. A Text-Book of Psychology. MacMillan Co, New York, NY, US. xx, 565 pages. doi:10.1037/10907-000 [76] Loïs Vanhée, Melania Borit, Peer-Olaf Siebers, Roger Cremades, Christopher Frantz, Önder Gürcan, František Kalvas, Denisa Reshef Kera, Vivek Nallur, Kavin Narasimhan, and Martin Neumann. 2025. Large Language Models for Agent-Based Modelling: Current and possible uses across the modelling cycle. doi:10.48550/arXiv.2507.05723 arXiv:2507.05723 [cs] version: 1. [77] Elina Vessonen. 2021. Conceptual engineering and operationalism in psychology. Synthese 199, 3 (Dec. 2021), 10615–10637. doi:10.1007/ s11229-021-03261-x [78] Lei Wang, Jingsen Zhang, Hao Yang, Zhi-Yuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Hao Sun, Ruihua Song, Xin Zhao, Jun Xu, Zhicheng Dou, Jun Wang, and Ji-Rong Wen. 2025. User Behavior Simulation with Large Language Model-based Agents. ACM Trans. Inf. Syst. 43, 2 (Jan. 2025), 55:1–55:37. doi:10.1145/3708985 [79] Zhilin Wang, Yu Ying Chiu, and Yu Cheung Chiu. 2023. Humanoid Agents: Platform for Simulating Human-like Generative Agents. doi:10.48550/arXiv.2310.05418 arXiv:2310.05418 [cs]. [80] Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato, Po-Sen Huang, Myra Cheng, Mia Glaese, Borja Balle, Atoosa Kasirzadeh, Zac Kenton, Sasha Brown, Will Hawkins, Tom Stepleton, Courtney Biles, Abeba Birhane, Julia Haas, Laura Rimell, Lisa Anne Hendricks, William Isaac, Sean Legassick, Geoffrey Irving, and Iason Gabriel. 2021. Ethical and social risks of harm from Language Models. doi:10.48550/arXiv.2112.04359 arXiv:2112.04359 [cs]. [81] Laura Weidinger, Jonathan Uesato, Maribeth Rauh, Conor Griffin, Po-Sen Huang, John Mellor, Amelia Glaese, Myra Cheng, Borja Balle, Atoosa Kasirzadeh, Courtney Biles, Sasha Brown, Zac Kenton, Will Hawkins, Tom Stepleton, Abeba Birhane, Lisa Anne Hendricks, Laura Rimell, William Isaac, Julia Haas, Sean Legassick, Geoffrey Irving, and Iason Gabriel. 2022. Taxonomy of Risks posed by Language Models. In 2022 ACM Conference on Fairness Accountability and Transparency. ACM, Seoul Republic of Korea, 214–229. doi:10.1145/3531146.3533088 [82] Michael Weisberg. 2007. Who Is a Modeler? The British Journal for the Philosophy of Science 58, 2 (2007), 207–233. https://www.jstor. org/stable/30115224 Publisher: [Oxford University Press, The British Society for the Philosophy of Science]. [83] Michael Weisberg. 2013. Simulation and Similarity: Using Models to Understand the World. Oxford University Press. [84] Ross Williams, Niyousha Hosseinichimeh, Aritra Majumdar, and Navid Ghaffarzadegan. 2023. Epidemic Modeling with Generative Agents. doi:10.48550/arXiv.2307.04986 arXiv:2307.04986 [cs]. [85] Michael Winikoff, John Thangarajah, and Sebastian Rodriguez. 2025. A Scoresheet for Explainable AI. doi:10.48550/arXiv.2502.09861 arXiv:2502.09861 [cs]. [86] Gal Yona, Roee Aharoni, and Mor Geva. 2024. Can Large Language Models Faithfully Express Their Intrinsic Uncertainty in Words? (2024). doi:10.48550/ARXIV.2405.16908 Publisher: arXiv Version Number: 2. [87] Dong Zhang, Zhaowei Li, Pengyu Wang, Xin Zhang, Yaqian Zhou, and Xipeng Qiu. 2024. SpeechAgents: Human-Communication Simulation with Multi-Modal Multi-Agent Systems. doi:10.48550/arXiv.2401.03945 arXiv:2401.03945 [cs]. [88] Jintian Zhang, Xin Xu, Ningyu Zhang, Ruibo Liu, Bryan Hooi, and Shumin Deng. 2024. Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View. doi:10.48550/arXiv.2310.02124 arXiv:2310.02124 [cs]. [89] Dunja Šešelja. 2023. Agent-Based Modeling in the Philosophy of Science. In The Stanford Encyclopedia of Philosophy (winter 2023 ed.), Edward N. Zalta and Uri Nodelman (Eds.). Metaphysics Research Lab, Stanford University. https://plato.stanford.edu/archives/win2023/ entries/agent-modeling-philscience/ Mechanism Plausibility in Generative Agent-Based Modeling A Examples In this section we step through Figures 4-7, which con Conway’s Game of Life This scale grades the model’s potential as a plausible exp goal is to be explanatory, it is important to clarify when Level 0: Simulation (𝑆) – Sandbox/Toy Model □✓ Simulation. Is the simulation (S) defined, including The rules of the game are detailed: At each timestep, “1. for the next generation. 2. Each counter with four or more with one neighbor or none dies from isolation. Each empty birth cell. A counter is placed on it at the next move.” Level 1: Target Phenomenon (𝑇 ) – Phenomenal Mo □ Defined Target Phenomenon. Is a target phenom annotations/observations, etc.)? □ Generative Sufficiency. Can the simulation (𝑆) suc □✓ Reproducibility. Does the reproducibility of the si prompt injections or version changes, inherent stoch or the field they are working in (sensitivity analysis While Conway selected his rules to try and make the be there is no operationalized pattern that the simulation is i [27]. Level 2: Intent & Mapping (𝐼) – How-Possibly Mode □ Simulation Contribution. Is the simulation’s use explanatory, etc.)? □ Falsifiable Hypotheses. Does there exist a hypothe in the model? □ Mechanism Mapping. Is there an Intent 𝐼 (implic simulation (𝑆) to the hypothesized ‘real-world’ mec Due to the lack of 𝑇 , the simulation does not describ phenomenon (see ‘Glennan’s Law’ [17, 31]). Level 3: Evidence (𝐸) – Plausible Model (if validate □ Evidence Exists. Is the model supported by some e □ Relevance. Is 𝐸 directed towards the claims made i Since 𝐸 requires 𝑇 and 𝐼, the model does not pass the Le Conclusion: Based on the checklist, the model is cla Fig. 4. Example for Level 0: The Mechanism Plausibility Sca FAccT ’26, June 25–28, 2026, Montreal, QC, Canada n example checklists filled out for each level. tion for the target phenomenon. While not every model’s s appropriate. vironments, agents, and update rules? y counter with two or three neighboring counters survives hbors dies (is removed) from overpopulation. Every counter adjacent to exactly three neighbors–no more, no fewer–is a n (𝑇 ) operationalized (e.g. as statistical patterns, human fully generate the patterns described in (𝑇 )? ation (seeds, API versions, consideration of proprietary city, etc.) match the reproducibility goals of the modeler uirements, etc.)? or of populations in his sim unpredictable, for the reader nded to reproduce, his simulation described as a “solitaire” e understood (e.g., predictive, exploratory, illustrative, or how the target phenomenon 𝑇 arises from components r explicit mapping) which connects components of the sms of (𝑇 )? ny mechanisms. Mechanisms are defined relative to a nce 𝐸? Could 𝐸, in principle, disconfirm the hypotheses in 𝐼? 3 requirement. fied as a Level 0 Toy model. pplied to an implementation of Conway’s Game of Life [27]. FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. Game Theory LLM Benchmarking Sim This scale grades the model’s potential as a plausible explanation for the target phenomenon. While not every model’s goal is to be explanatory, it is important to clarify when it is appropriate. Level 0: Simulation (𝑆) – Sandbox/Toy Model □✓ Simulation. Is the simulation (S) defined, including environments, agents, and update rules? 𝑆 includes the codebase for the simulation, which is an implementation of games such as Prisoner’s Dilemma, Texas Hold’em, Staghunt, etc. played by different LLM Agents against each other. Level 1: Target Phenomenon (𝑇 ) – Phenomenal Model □✓ Defined Target Phenomenon. Is a target phenomenon (𝑇 ) operationalized (e.g. as statistical patterns, human annotations/observations, etc.)? □✓ Generative Sufficiency. Can the simulation (𝑆) successfully generate the patterns described in (𝑇 )? □✓ Reproducibility. Does the reproducibility of the simulation (e.g. seeds, API versions, consideration of proprietary prompt injections or version changes, inherent stochasticity) match the reproducibility goals of the modeler or the field they are working in (sensitivity analysis requirements, etc.)? We aim to benchmark the behavior of different LLMs to see if they will solve game-theoretic scenarios, and if they produce optimal or well-known game-theoretic behavior (e.g., Tit-for-Tat, Nash Equilibrium); their execution of these strategies we will consider 𝑇 . After running the simulation, we find that models with a larger parameter space tend to exhibit more aggressive behavior. Level 2: Intent & Mapping (𝐼) – How-Possibly Model □ Simulation Contribution. Is the simulation’s use case understood (e.g., predictive, exploratory, illustrative, explanatory, etc.)? □ Falsifiable Hypotheses. Does there exist a hypothesis for how the target phenomenon 𝑇 arises from components in the model? □ Mechanism Mapping. Is there an Intent 𝐼 (implicit or explicit mapping) which connects components of the simulation (𝑆) to the hypothesized ‘real-world’ mechanisms of (𝑇 )? We do not suggest the mechanisms behind why some models play different styles of games than others. However, our findings do find a correlation between the aggressiveness of players and their parameter count. Level 3: Evidence (𝐸) – Plausible Model (if validated) □ Evidence Exists. Is the model supported by some evidence 𝐸? □ Relevance. Is 𝐸 directed towards the claims made in 𝐼? Could 𝐸, in principle, disconfirm the hypotheses in 𝐼? Since 𝐸 requires 𝐼, the model does not pass the Level 3 requirement. Conclusion: Based on the checklist, the model is classified as a Level 1 Phenomenal model. Fig. 5. Example for Level 1: The Mechanism Plausibility Scale applied to a fabricated game theory paper. Mechanism Plausibility in Generative Agent-Based Modeling Example Schelling’s Model of Segregation This scale grades the model’s potential as a plausible exp goal is to be explanatory, it is important to clarify when Level 0: Simulation (𝑆) – Sandbox/Toy Model □✓ Simulation. Is the simulation (S) defined, including 𝑆 is defined as a grid of agents who move to adjacent em below a certain threshold (formalized in full paper). Level 1: Target Phenomenon (𝑇 ) – Phenomenal Mo □✓ Defined Target Phenomenon. Is a target phenom annotations/observations, etc.)? □✓ Generative Sufficiency. Can the simulation (𝑆) suc □✓ Reproducibility. Is the simulation reproducible? The target 𝑇 is the emergence of macro-level clustering generatively sufficient as it always produces segregated Level 2: Intent & Mapping (𝐼) – How-Possibly Mode □✓ Simulation Contribution. Is the simulation’s use explanatory, etc.)? □✓ Falsifiable Hypotheses. Does there exist a hypothe in the model? □✓ Mechanism Mapping. Is there an Intent 𝐼 (implic simulation (𝑆) to the hypothesized ‘real-world’ mec Our Intent 𝐼 is to demonstrate the feasibility of the hypo macro-segregation to occur. Mild preferences for similar rules map to a simplification of the real-world mechanism Level 3: Evidence (𝐸) – Plausible Model (if validate □ Evidence Exists. Is the model supported by some e □ Relevance. Is 𝐸 directed towards the claims made i The threshold parameters in our model are abstract and It proposes a “how-possibly” mechanism. Conclusion: Based on the checklist, the model is cla Fig. 6. Example for Level 2: The Mechanism Plausibil FAccT ’26, June 25–28, 2026, Montreal, QC, Canada tion for the target phenomenon. While not every model’s s appropriate. vironments, agents, and update rules? spots if the percentage of their own color neighbors falls n (𝑇 ) operationalized (e.g. as statistical patterns, human fully generate the patterns described in (𝑇 )? ich represents residential segregation. The simulation is ghborhoods. e understood (e.g., predictive, exploratory, illustrative, or how the target phenomenon 𝑇 arises from components r explicit mapping) which connects components of the sms of (𝑇 )? is that extreme individual prejudice is not necessary for hbors are a sufficient mechanism. The agents’ movement residents relocating based on neighborhood composition. nce 𝐸? Could 𝐸, in principle, disconfirm the hypotheses in 𝐼? derived from specific empirical data (e.g. census surveys). fied as a Level 2 How-Possibly model. cale applied to Schelling’s Model of Segregation [70] FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. Example Anasazi Model (Epstein et al.) This scale grades the model’s potential as a plausible explanation for the target phenomenon. While not every model’s goal is to be explanatory, it is important to clarify when it is appropriate. Level 0: Simulation (𝑆) – Sandbox/Toy Model □✓ Simulation. Is the simulation (S) defined, including environments, agents, and update rules? 𝑆 is an agent-based model that simulates the Long House Valley environment using rules for annual agricultural productivity, and defines agent behaviors based on specific rules for nutritional needs, household size, and reproduction rates. The details of these parameters, as well as the simulation code, can be found in our GitHub repository. Level 1: Target Phenomenon (𝑇 ) – Phenomenal Model □✓ Defined Target Phenomenon. Is a target phenomenon (𝑇 ) operationalized (e.g. as statistical patterns, human annotations/observations, etc.)? □✓ Generative Sufficiency. Can the simulation (𝑆) successfully generate the patterns described in (𝑇 )? □✓ Reproducibility. Is the simulation reproducible? The target 𝑇 is the historical population dynamics and settlement patterns of the Long House Valley from 800 AD to 1350 AD. The simulation reproduces the population crash and abandonment of the valley. Level 2: Intent & Mapping (𝐼) – How-Possibly Model □✓ Simulation Contribution. Is the simulation’s use case understood (e.g., predictive, exploratory, illustrative, explanatory, etc.)? □✓ Falsifiable Hypotheses. Does there exist a hypothesis for how 𝑇 arises? □✓ Mechanism Mapping. Is there an Intent 𝐼 (implicit or explicit mapping) which connects components of the simulation (𝑆) to the hypothesized ‘real-world’ mechanisms of (𝑇 )? The intent (𝐼) maps the simulation’s rules (agricultural yield vs. caloric needs) to the real-world mechanisms of the environmental factors affecting population growth. Therefore it hypothesizes that environmental shifts were the primary driver. Level 3: Evidence (𝐸) – Plausible Model (if validated) □✓ Evidence Exists. Is the model supported by some evidence 𝐸? □✓ Relevance. Is 𝐸 directed towards the claims made in 𝐼? Could 𝐸, in principle, disconfirm the hypotheses in 𝐼? The model is constrained by empirical Evidence 𝐸, which includes agricultural productivity reconstructed using paleoenvironmental data from tree rings, soil analysis, and geology. Each agent’s nutritional needs and household sizes are derived from anthropological studies of Puebloan peoples. Conclusion: Based on the checklist, the model is classified as a Level 3 Plausible model. Fig. 7. Example for Level 3: The Mechanism Plausibility Scale applied to the Artificial Anasazi Model [24] Mechanism Plausibility in Generative Agent-Based Modeling B Calibrating the Mechanism Plausibility Scale This section goes through the process of how we itera B.1 Calibration The Mechanism Plausibility Scale was refined through from a systematic review of LLM-based social simulat evaluated by two reviewers who assigned scores bef two rounds of calibration, multiple ambiguities still r to further rework where we decided it would be mor format. B.2 Round 1 Calibration B.2.1 Paper Selection and Review Process. We tested from Larooij et al.’s systematic review [45]. We chos we found that their inclusion criteria was heavily al requirements that the ABM uses an LLM as the bas and that the LLMs were seen to be simulating human LLM-ABM social simulation. A copy of the exact quer Each paper was reviewed and evaluated by two revie period, and (2) the reconciliation period. During the assign it a score before moving onto the next paper. T the other reviewer until the reconciliation period beg B.2.2 Inter-Rater Reliability. To assess the reliability inter-rater reliability using a weighted kappa (𝑘 𝑤) w mentioned before, the first structured round of apply it was challenging for even two researchers to apply guidelines and confusion with the nested nature of th FAccT ’26, June 25–28, 2026, Montreal, QC, Canada on the scale. uble-blinded review processes involving papers drawn s by Larooij et al. [45]. Each paper was independently entering a reconciliation phase. After going through ained about how the scale should be applied. This led propriate to reframe the scale as a practical checklist y versions of the scale on the first 15 out of 35 papers evaluate papers from Larooij et al.’s review because ed with our own research interests. In particular, the r their agents, there are multiple interacting agents, havior, were all aligned with our own conceptions of they used can be found in our Appendix at B.4. s; their task comprised of two phases: (1) the evaluation uation period, each reviewer would read a paper and eviewers were blinded to the scores and sentiments of the Mechanism Plausibility Scale, we calculated the quadratic weights, suitable for our ordinal scale. As the scale to a focused body of literature revealed that scale consistently; we found ambiguities in the rating mulations through the reconciliation process. FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. Round 1 Reviewer Scores Shortened Title A B Generative Agents [61] 3 1 WarAgent [37] 3 1 Social Simulacra [62] 3 1 S3 [26] 0 1 Scale-Free Networks [54] 3 2 Humanoid Agents [79] 3 2 LyfeAgents [40] 3 0 Collaboration [88] 3 2 AgentVerse [15] 3 0 Epidemic Modeling [84] 3 2 Project Sid [3] 3 1 Theory of Mind [47] 3 1 News Diffusion [48] 0 1 SpeechAgents [87] 1 1 Fake News Propagation [51] 1 1 Table 2. Levels of the Mechanism Plausibility Scale assigned to each paper by Reviewers A and B during the blinded first round of evaluation, along with its assigned level after unblinding and reconciliation. B.2.3 Round 1 results of the applied review. The results of the first round are shown in Table 2. Through the reconciliation process, we found that our scale’s rating guidelines and definitions were too ambiguous to handle the operationalization gaps discussed in Section 5.1. Notably, we also found that many papers conflated Agent-level functionality with ABM-level plausibility. A paper might have provided high-quality experimental evidence for its Agent-level social simulation (the lowest level in Figure 1), but then they implicitly treated that as sufficient evidence for the claims made about the emergent social phenomenon (𝑇 ) observed at the ABM-level, which is a category error. Work that shows the mechanism plausibility of Agent-level phenomena does not necessarily translate to the mechanism plausibility of ABM-level phenomena. This remains to be shown and must be argued for in the modeler’s Intent, with further Evidence provided at the ABM-level. Papers had this problem to varying degrees, but the ones that we flagged particularly were: • S3 [26], which conflated (the LLM agent’s capacity to simulate the social media posts of an individual, with matching estimated emotions and attitudes) with (their ABM’s ability to simulate realistic social media phenomena, like opinion dynamics or information cascades). • News Diffusion [48], which conflated their (LLM agent’s ability to share news based on personality traits and friend connections), with their (ABM’s capacity to produce realistic fake news diffusion patterns). • SpeechAgents [87], which conflated (their LLM agent’s ability to generate text-to-speech outputs, which was successfully transcribed back into similar text) with (their ABM’s ability to simulate realistic, emergent human communication dynamics and social interaction patterns at the group level). • Fake News Propagation [51], which conflated (an LLM agent’s capability to reason about, reflect on, and share fake news) with (their ABM’s ability to mechanistically explain realistic fake news propagation dynamics and the emergence of collective opinion patterns). Mechanism Plausibility in Generative Agent-Based Modeling The presence of these nested simulations was particu identify the target phenomenon 𝑇 , and also difficult to between Agent and ABM phenomena led to a split bet quadratic weighted kappa score of 0.207. B.3 Round 2 Calibration After uncovering the gaps in operationalization (also d were to assign two scores: one for the ABM-level target In addition to the clarified scoring guidelines, the sa increase in reliability may be partially attributable to As shown in Table 4, the quadratic weighted kapp Agent ratings reached 0.503. We posit that the score di from the literature review operationalizing the Agent the ABM-level. These results are shown in Table 3. Ro Shortened Title Generative Agents [61] WarAgent [37] Social Simulacra [62] S3 [26] Scale-Free Networks [54] Humanoid Agents [79] LyfeAgents [40] Collaboration [88] AgentVerse [15] Epidemic Modeling [84] Project Sid [3] Theory of Mind [47] News Diffusion [48] SpeechAgents [87] Fake News Propagation [ Table 3. Levels of the Mechanism Plausibility Scale assign round of the literature review, along with its assigned level In the second round of evaluations, we found that o too broad, allowing for many papers to reach a Level Difficulties in ignoring a paper’s perceived evidence q the ABM-level. B.4 Queries for LLM ABM-related papers The 15 papers from our applied study are from Larooi FAccT ’26, June 25–28, 2026, Montreal, QC, Canada y difficult to evaluate with our scale, as it was difficult to ntify its operationalization. The ambiguous evaluations en the reviewer’s perceptions and resulted in an initial ssed in Section 5.1), in the second round the reviewers nomena, and one for the Agent-level target phenomena. reviewers were also used in both rounds. and so the training received as part of the first round. r the ABM ratings rose to 0.255, and the score for the ence between Agent and ABM also comes from papers el phenomena (implicitly) more in-depth compared to d 2 Reviewer Scores ABM Agent A B R A B R 3 1 3 3 3 3 3 1 3 3 1 3 1 1 1 3 3 3 0 0 0 1 2 1 3 3 3 1 1 1 1 0 1 3 3 3 1 1 1 3 1 3 3 2 3 3 3 3 3 2 3 3 1 3 3 2 3 3 2 3 3 2 3 3 1 3 1 2 2 3 2 3 3 2 3 2 1 2 1 0 1 3 3 3 3 2 3 3 2 3 o each paper by Reviewers A and B in the blinded second r unblinding and reconciliation. efinition of the Evidence (as stated in Section 3.4) was n our scale, regardless of the quality of their Evidence. ty led to large differences between reviewer scores at al. [45]: FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al. Dataset Weighted Kappa (𝑘 𝑤) Interpretation Round 1 0.207 Fair Agreement Round 2 (Agent) 0.503 Moderate Agreement Round 2 (ABM) 0.255 Fair Agreement Table 4. Summary of weighted kappa (𝑘 𝑤) scores using quadratic weights. The ordinal measure was used because the plausibility scale has ordered categories. The interpretation comes from Landis and Koch [44]. TITLE-ABS-KEY ( ( "generative social simulation" ) OR ( "generative agent-based model*" ) OR ( "agent-based simulation" AND "generative AI" ) OR ( "LLM*" AND "agent-based model*" ) OR ( "large language model*" AND "ABM" ) OR ( "foundation model*" AND "ABM" ) OR ( "multiagent system*" AND "generative AI" ) OR ( "generative agent*" ) OR ( "social simulation" AND "LLM*" ) OR ( "large language model-based agents" ) ) We also used Asta3, an AI research paper search engine built on Semantic Scholar, for paper discovery. Other LLM-ABM papers were from previous knowledge of the authors or related work. C Additional Philosophy of Science Background C.1 Clarification of Model Targets 𝑇 According to a description by Weisberg, 𝑇 does not have to be a particular or ‘real’ phenomenon, and some models might not even have a 𝑇 ; the target could be particular, generic, or even hypothetical [83]. As an example, Graebner gives an account of how the target of Schelling’s segregation model [70] is a generalized target, where it represents an abstract city and its arguments can be applied generically rather than to a particular city [32, 83]. 𝑇 can also be hypothetical; for example, Fisher’s three-sex population simulation [25] shows how a population with three sexes comes with large costs compared to those with only two and is a possible explanation for why three-sex populations do not exist in reality [32, 82]. 3https://asta.allen.ai/chat

## Outline

- Abstract (page 1)
- 1 Introduction (page 2)
- 2 Motivation and Related Work (page 3)
  - 2.1 Operationalization (page 3)
  - 2.2 Phenomenal Models and Generative Sufficiency (page 4)
  - 2.3 Mechanisms (page 4)
  - 2.4 Mechanisms vs Prediction (page 5)
  - 2.5 Plausibility (page 6)
- 3 A Mechanism Plausibility Scale (page 6)
  - 3.1 Level 0 (page 7)
  - 3.2 Level 1 (page 7)
  - 3.3 Level 2 (page 8)
  - 3.4 Level 3 (page 9)
  - 3.5 Interpreting the Plausibility Scale (page 9)
- 4 The Mechanism Plausibility Scale Heuristic (page 11)
- 5 Discussion (page 11)
  - 5.1 Reflections on the State of LLM Social Simulation (page 11)
  - 5.2 Proprietary LLM APIs and Reproducibility (page 13)
  - 5.3 Broader Ethical and Epistemic Concerns (page 14)
  - 5.4 Historical Issues and Harms of Poor ABM specification (page 14)
- 6 Conclusion and Limitations (page 15)
- References (page 15)
- A Examples (page 19)
- B Calibrating the Mechanism Plausibility Scale (page 23)
  - B.1 Calibration (page 23)
  - B.2 Round 1 Calibration (page 23)
  - B.3 Round 2 Calibration (page 25)
  - B.4 Queries for LLM ABM-related papers (page 25)
- C Additional Philosophy of Science Background (page 26)
  - C.1 Clarification of Model Targets T (page 26)

## Markdown Content

Mechanism Plausibility in Genera
PATRICK ZHAO, Simon Fraser University, Canada
DAVID HUU PHAM, Simon Fraser University, Ca
NICHOLAS VINCENT, Simon Fraser University,
Large language models (LLMs) can generate high-level d
capability has led to their adoption within different agent-ba
to test whether they are capable of generating different phen
platforms or performance in game-theoretic scenarios.
However, capability, prediction, and explanation are diffe
literature, explanation requires showing, to some degree, ho
activities. For modelers, describing the characteristics of an ex
(or explanation), can be difficult without being grounded in
We integrate recent work on LLM-ABMs with contempo
butions. First, we gather insights from modeling and mech
‘plausibility’ in a four-level scale. Our scale separates the eva
phenomenon) from its mechanistic plausibility (how the ph
different models, such as predictive and explanatory ones.
we discuss the early wave of LLM-ABM research and find t
with claims about emergent ABM-level phenomenon, relyin
Our discussion section speaks on how these findings echo lo
by these issues, and broader ethical and epistemic concern
review, we offer the scale as a practical heuristic in the for
levels of plausibility may be useful. We hope the activity of fi
contribution of their simulations.
CCS Concepts: • Computing methodologies → Simulati
and simulation; Natural language processing; • Human-ce
and evaluation methods.
Additional Key Words and Phrases: Agent-Based Modelin
Philosophy of Science
ACM Reference Format:
Patrick Zhao, David Huu Pham, and Nicholas Vincent. 2026.
The 2026 ACM Conference on Fairness, Accountability, and Tr
ACM, New York, NY, USA, 26 pages. https://doi.org/10.1145
Authors’ Contact Information: Patrick Zhao, patrick_zhao@sfu.c
dhpham@sfu.ca, Simon Fraser University, Burnaby, BC, Canada; Ni
Canada.
This work is licensed under a Creative Commons Attribution 4.0 In
FAccT ’26, Montreal, QC, Canada
6202
yaM
71
]AM.sc[
2v42821.5062:viXra

ve Agent-Based Modeling
a
nada
se phenomena without explicitly programmed rules. This
models (ABMs) and social simulations. Recent research aim
ena of interest, for example, human behavior on social media
– drawing from the philosophy of science and mechanisms
phenomenon is produced by related organized entities and
ment or whether a simulation provides progress in capability
entially distant research areas.
philosophy of science literature and make two main contrims literature and use them to operationalize a definition of
on of a model’s generative sufficiency (ability to reproduce a
menon could be produced), and clarifies the distinct roles of
introduce this as the Mechanism Plausibility Scale. Second,
papers often conflate evidence of Agent-level functionality
n ‘believability’ metrics that focus on generative sufficiency.
standing problems in classical ABM, historical harms caused
bout using LLMs in modeling. Using the findings from our
a checklist which can clarify how simulations at different
g out the scale will help new modelers ground the epistemic
valuation; Model development and analysis; Modeling
ed computing → Collaborative and social computing design
Mechanisms, Generative Agents, Large Language Models,
hanism Plausibility in Generative Agent-Based Modeling. In
parency (FAccT ’26), June 25–28, 2026, Montreal, QC, Canada.
5689.3812388
mon Fraser University, Burnaby, BC, Canada; David Huu Pham,
as Vincent, nvincent@sfu.ca, Simon Fraser University, Burnaby, BC,
ational License.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
1 Introduction
Developments in natural language processing have s
social simulations [4, 36, 61], for example, extending th
seems increasingly possible that product decisions, p
by the outcome of such simulations [4, 49]. Today, a
of reproducing higher-level phenomena without exp
In a canonical agent-based model (ABM), the mechan
programmed by the modeler (e.g., for an economic
requirement 𝐵 is at a threshold 𝑌 , then buy some am
some combination of assumptions, scientific theory, a
several social science papers to determine a particular
represent their preferences and attributes. Using LLMs
and biases obtained by training on social data may c
behavior, allowing for richer representations of hum
also formed around models failing to capture the com
[1], which leaves us with questions about if this is tie
should be used at all.
When using LLMs in modeling social phenomena
did the results emerge from some correctly retrieved
agents model the human behavior we are interested
on data describing real, human decision-making. Wit
interpretability and data attribution, it could be the c
information that is irrelevant to the modeler’s intent
‘faithfulness’ [64, 86]). In other words, we might pro
science phenomenon, but is just generating it through s
that there are many ways in which a phenomenon ca
A recent review by Larooij et al. from April 2025 [4
ABMs with LLMs (LLM-ABM) fail to acknowledge es
even have proper operational validity. One particular s
believability, where human annotators are tasked wit
dialogues are produced by a human. On top of this, m
LLM agents are capable of producing a specific pheno
These problems leave us with further questions: Is
of LLMs to produce useful simulations? What does ‘
facilitate the discussion we connect work from the phil
computer models, such as ABMs.
Let us consider a target phenomenon 𝑇 a modeler is
agent-based modeling it is mostly accepted that by g
how 𝑇 is created, sometimes called generative suffic
modeler has created an input-output mapping and d
how 𝑇 might arise [24].
Now suppose the modeler wants to explain, to some
relationship between the simulation’s mechanisms and
are the theoretical organization of entities and activ
and neuroscience literature a simulation that produce

Zhao et al.
red interest in using large language models (LLMs) in
ction space of agents in agent-based models (ABMs). It
ymaking, and even research itself may be influenced
deler [82] creating simulations with LLMs is capable
ly programming the mechanisms that produce them.
ms underlying a phenomenon are operationalized and
nt, “if the price of resource 𝐴 is 𝑋 and my internal
nt of resource 𝐴”). These rules are typically based on
mpirical data. For instance, a programmer might read
ribution from which their agents will draw values that
simulations offers the tantalizing promise that weights
ain relevant distributional information about human
ubjects [4, 61, 76]. On the other hand, critiques have
te experiences of the human subjects they substitute
the nature of LLMs, and if so, the question of if LLMs
e are left with a few puzzles: For a given simulation,
al knowledge encoded in the LLM’s weights? Do our
This could be the case, given that LLMs are trained
t improvements in the field of machine learning (ML)
that simulations incorporating LLMs are drawing on
metimes referred to in the machine learning space as
e a simulation that looks like it is explaining a social
e other means, regardless of the ‘how’. One can imagine
cur, and we are only interested in a particular one.
urveyed and found that a number of studies involving
ished work in the traditional simulation literature, or
mary is that recent evaluations rest on some variant of
beling whether or not they think the outputs of agent
h work focuses on whether or not a simulation or its
non.
ecessary to completely understand the inner workings
ul’ mean anyways, in the context of simulations? To
phy of science about what can be learned from idealized
empting to produce using a simulation 𝑆. In traditional
rating 𝑇 using 𝑆, they realize a possible candidate for
y [24]. By ‘growing’ 𝑇 through their simulation, the
nstrated a sufficient, but not necessary condition for
el, how 𝑇 arises in actuality–they need to describe the
“real” mechanisms that produce the target. Mechanisms
s behind a phenomenon [17, 53]. In the mechanisms
without a connection to the “how-actually” is called a

Mechanism Plausibility in Generative Agent-Based Modeling FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
phenomenal model [42, 56]. Connecting this to ABMs, a modeler might use a simulation to deduce or intuit parts
of the mechanisms behind 𝑇 ; however, since a simulation of 𝑇 is only a single possible candidate, one could say
that generative success is not sufficient to show the mechanisms in 𝑆 correspond to the mechanisms responsible
for 𝑇 . A modeler could generate 𝑇 in many possible ways, perhaps completely unrelated to any hypothesis about
its real causes. If a modeler is interested in creating a simulation that helps in explaining the target phenomenon,
it needs to convey some level of information about the underlying mechanism and propose how it is mapped to
the simulation; that is, they need to show the mechanisms in 𝑆 are plausible mechanisms for 𝑇 .
In this paper we explain how simulations can vary in their level of plausibility and introduce a set of criteria
for categorizing simulations along our axis of interest. This is not to say that the value of a simulation is dictated
purely by plausibility or the mechanistic understanding of a model; it is of general agreement that idealizations
and abstractions are common, if not, necessary in building accepted models, or science may never move forward
[8, 23, 63]. Simulations can vary in their level and type of claim, whether they claim to be predictive, illustrative,
exploratory, explanatory, etc. However, if a modeler wants to use their simulation to make any level of claim
about how 𝑇 might arise in actuality (explanatory), they must move beyond a purely phenomenal account. We
present a checklist version of the scale in Section 4, motivated by dataset and model information checklists in
past work [29, 58, 85]. We believe the scale will guide researchers in developing their own models, especially
those integrating LLMs.
In Section 2 we operationalize and elaborate on terms used across the paper such as mechanism, phenomenal,
plausibility, and explanation. We aim to show how these concepts can be directly related to existing simulation
work in various fields of computing, especially the use of LLM simulation across human computer interaction
and computational social science. In Section 3 we introduce a “mechanism plausibility scale” that aims to capture
core ideas from the diverse literatures discussed in the preceding section and provide a practical approach for
classifying simulations and their contributions. In Section 4 we present the more pragmatic, checklist version of
the scale and discuss the reviews involved in its development. Finally, in Section 5 we further discuss contemporary
problems of LLM-enabled simulation and how it relates to their placement on these scales.
2 Motivation and Related Work
2.1 Operationalization
In the philosophy of science, phenomena are defined to be stable patterns, regularities, or events that can be
reliably inferred from data, and are the targets of explanation for scientific communities [10]. The patterns that
qualify as ‘phenomena’ are scoped to the particular domain of inquiry [55], and may vary depending on the
modeler’s methodological choices or research question [57].
Consider a subject who displays the phenomena of eye contact avoidance and shaking limbs. The phenomena
of ‘eye contact avoidance’ is something that is inferred by patterns in the data pertaining to the subject’s average
length of eye contact and their direction of gaze. Although behavioral, psychological, or social phenomena may
be inferred from aggregated, third-person observational data, the mental experience of, and the cause of these
phenomena may only be accessible to the subject experiencing them [39, 75], where outside observers can only
agree upon a subject’s apparent reactions to their own internal experience [73]. Third-person observers may
posit that the phenomena displayed by the subject are indicative of the hypothetical construct of anxiety [20, 52].
Originating from psychometric evaluation, hypothetical constructs are a theoretical attribute postulated to
explain observed behavioral patterns, but are not directly observable themselves [20, 52]. We often work with
hypothetical constructs in order to characterize and reason about mental and social phenomena [67, 77]. To allow
empirical measurements of these constructs, we create operational definitions: these are an explicit, unambiguous
set of operations, protocols, or rules that are treated as equivalent to these abstract constructs within the bounds
of the experiment, for the sake of falsifiable detection and experimental reproducibility [13]. The process of

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
creating an operational definition for a particular concept is called the “operationalization” of the concept, and
determining whether this operational definition measures what it is intended to measure, is called construct
validity [20, 28].
Operationalization involves not only translating abstract constructs into measurable patterns, but also assigning
interpretations to the formal components of a model. From the modeling and cognitive representation literature
[22, 83], we recognize the distinction between a model’s formal functions and the interpretation assigned by the
modeler to connect the functions to the domain of interest. Egan distinguishes between what she calls the “theory
proper” of a computational model and an “intentional gloss” that accompanies it [22]. The theory proper specifies
the mathematical function(s) computed, the algorithms, the structures maintained, and their physical realization.
For LLM Agents within a simulation, this would be the next-token probability distribution over a vocabulary,
given an input sequence. The intentional gloss is what connects the computation to the modeler’s interpretation,
which could be some target persona the modeler says the agent is representing. But as Egan argues, the validity
of an intentional gloss is not guaranteed by its computations and requires independent justification, typically
grounded in the theorist’s explanatory goals. In our scale interpretation takes the form of an Intent 𝐼 , which we
will return to in Section 3.3.
Since our focus is on simulation models created by researchers, most researchers have particular phenomena
that they would like the simulation to produce [32]. We refer to these phenomena of interest as 𝑇 , the target
phenomena, and we expand on this definition in Section 2.2. In our review we find gaps in the operationalization
of target phenomena used in the evaluation of recent LLM-based social simulations, further discussed in 5.1.
2.2 Phenomenal Models and Generative Sufficiency
The term phenomenal comes from established usage in the scientific modeling field [42, 56], where it is used
to describe models that aim to produce the patterns describing a target phenomenon 𝑇 , but do not contain
information about the mechanism behind it. They may produce an accurate output without describing the
relevant internal structure, therefore limiting their explanatory power.
One can imagine that it is not always simple or practical to produce the target phenomenon; In the modeling
field, the term generative sufficiency describes the level to which a model is able to accurately produce 𝑇 [32].
Due to the black-box nature of deep neural networks and other practicality reasons, much of the emphasis in the
traditional machine learning field is put on the generative sufficiency of different ML models–how accurately they
are able to produce a target behavior. At the time of writing, the primary ways to evaluate LLMs are to measure
scores they achieve on some benchmark centered around human evaluation or fact-checking. This mentality
may have spread to the LLM social simulation area, as initial projects in the space used similar evaluations
to benchmark the realism of their simulation. For example, projects using ‘believability’ as a metric for their
sufficiency in producing a target behavior [40, 47, 61, 62, 69, 78].
While generative sufficiency could be appropriate for exploratory or illustrative settings, the goals of a model
may not be limited to just reproducing the target behavior; One may want to test unknown counterfactual scenarios
or interventions. Problematically, these simulations are evaluated based off of their generative sufficiency and
then used to test interventions as if there are plausible mechanisms [26, 37]. Phenomenal models cannot be used
to test counterfactual scenarios because they lack the relevant internal causal structure. In order to move past
being purely phenomenal, the model needs to suggest how 𝑇 is produced: the mechanisms behind it.
2.3 Mechanisms
Mechanisms literature has seen a rise in discussion in the past two decades, primarily in the philosophy-of-science
and neuroscience fields [17, 30, 53]. Glennan gives a minimal definition for mechanisms in his text, The New
Mechanical Philosophy:

Mechanism Plausibility in Generative Agent-Based Modeling FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
“A mechanism for a phenomenon consists of entities (or parts) whose activities and interactions are
organized so as to be responsible for the phenomenon.” [30]
Pragmatically, in our discussion of agent-based models and computer simulation, this might include how the
agents, environment, and update rules function to produce 𝑇 . A mechanism is involved in the causal process of
𝑇 , not just correlated, and hypothesizing about them is the first step towards explaining a phenomenon. This
hypothesis can take the form of a mapping which details what parts of the simulation correspond to mechanisms
behind 𝑇 . In our scale the addition of this mapping is what distinguishes a purely phenomenal model from one
that presents the plausible candidate mechanisms behind 𝑇 .
To explain the mechanisms behind a phenomenon is to explain how the phenomenon is produced (falsifiably).
Once some level of description of the mechanisms behind𝑇 are produced, the model is beyond a purely phenomenal
account. Kaplan and Craver have summarized these demands into an account called the 3M requirement:
“In successful explanatory models in cognitive and systems neuroscience (a) the variables in the model
correspond to components, activities, properties, and organizational features of the target mechanism
that produces, maintains or underlies the phenomenon, and (b) the (perhaps mathematical) dependencies
posited among these variables in the model correspond to the (perhaps quantifiable) causal relations
among the components of the target mechanism.” [41]
To be clear, an explanation does not need to constitute every detail down to the atomic level; it can use an
adequate level of abstraction or idealization to fit the use case of the modeler [18, 74]. For example, in Figure 1,
lower-level mechanisms beyond the ‘Agent-level’ could be further explored and abstracted, but may be stubbed
at the modeler’s adequate level of abstraction.
We note that mechanisms cannot be identified in isolation, and therefore the target phenomena need to be
operationalized before identifying any mechanisms. Craver suggests, “mechanistic explanations can fail because
one has tried to explain a fictitious phenomenon, because one has mischaracterized the phenomenon, and because
one has characterized the phenomenon to be explained only partially.” [19] Mechanisms are not just ‘static’
concepts, they are functions that are defined relative to a phenomenon. Its identity, boundaries, and relevance
are all defined by the specific outcome it is supposed to explain [17, 31]. Therefore, as we will see later, in our
Mechanism Plausibility Scale the operationalization precedes the hypothesis.
2.4 Mechanisms vs Prediction
The focus on the productive process of a phenomenon distinguishes mechanisms from predictivism or correlation.
One can use a barometer reading to predict weather, but the changing air pressure it measures is not the
mechanism that produces it. In causal inference, this is the difference between observational and interventional
questions [65, 66]. A predictive model is appropriate for questions such as “given these initial conditions, what
outcomes are likely?” Without plausible mechanisms, however, a model’s predictive outputs are usually only
appropriate to the extent that they can be validated against observed outcomes. For scenarios that have been or
can be empirically tested, this validation may suffice [71]. But for novel interventions, mechanisms provide the
basis for reasoning about whether the model’s outputs are acceptable.
This distinction between explanation and prediction is well established and known to be easily conflated
[71]. The two goals require different criteria for model evaluation, different relationships to the underlying
data-generating process, etc. An explanatory model aims to test causal hypotheses about the process producing
𝑇 ; a predictive model aims to produce accurate forecasts of new observations, and may do so using variables that
have no/weak causal relationship to the outcome. Conflating the two is a category error that appears in both
classical statistics and, as we argue, in early LLM-ABM work.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
Fig. 1. An adapted Craver diagram [19] showing a simulati
ABM, the agents/entities {𝑥
1
, . . . , 𝑥 𝑚} (circles) and activities
are further and reciprocally constituted by lower-level mech
tractability, but are also why simulations can never be fully
2.5 Plausibility
The definition of plausibility can be vague, subjective
definition from the Stanford Encyclopedia of Philosop
has epistemic support: we have some reason to believe it
In this paper, we operationalize plausibility in ABMs
3), which encapsulates factors such as how a simulatio
used to justify its parameters, the model’s relationship
we are interested in if a model is a faithful represen
scholars recently publishing in the LLM-ABM space
annotation to support their simulations. We find tha
provide support for is elusive for even seasoned and c
giving us the primary motivation for developing our s
3 A Mechanism Plausibility Scale
Now that we have distinguished explanatory models f
for models as plausible explanations.
Craver: “For those interested in building plausible
to reproduce the input–output mapping of target
what is known about the internal machinery by
possible, for example, to simulate human skills at m
scales; but that is not how most humans multiply

Zhao et al.
roducing 𝑇 with higher and lower-level mechanisms. In the
. . . , 𝜙 𝑛} (arrows) work to produce 𝑇 . The agents in the ABM
ms, which are generally abstracted away for the purposes of
dated (see Level Ω in Section 3.5).
d is often treated as a qualitative property. A general
“To say that a hypothesis is plausible is to convey that it
en prior to testing.” [9]
ed off of its standing on our scale (presented in Section
components are operationalized, the type of evidence
hypotheses the modeler is presenting, etc. In particular,
on of the modeler’s intent. As mentioned previously,
ve used believability/plausibility metrics like human
e task of identifying what these evaluations actually
able researchers when it is applied to LLM simulation,
e.
m predictive and illustrative ones, we introduce an axis
ulations, it will not suffice for simulation 𝑆 simply
enomenon 𝑇 . The model is further constrained by
ich the inputs are transformed into outputs. It is
iplication with two sticks marked with logarithmic
8]

Mechanism Plausibility in Generative Agent-Based Modeling
If we want a simulation to be a plausible representati
𝑇 – the simulation mechanisms must be adequately cl
[41, 83].
We formalize a model as a four-tuple 𝑀 = (𝑆,𝑇 ,
Intent (𝐼 ), and Evidence (𝐸) (these terms will be fu
corresponding four-level Mechanism Plausibility
become falsifiable and relevant in explaining its mechan
the modeler’s intentions. To make the scale concrete, w
(hypothetical) LLM-based simulation of opinion dyna
3.1 Level 0
A Level 0 model is a ‘toy’ simulation or sandbox with
which is set of procedures, code, and update rules that
to explain. Since mechanisms are defined relative to
[17, 31], a model without a target cannot have mechan
of a target 𝑇 unintentionally in level 0 as well.
3.1.1 Example. A research team builds a sandbox wh
and allowed to post, reply, and share content freely
technique. The researcher documents the system and
to reproduce or explain.
3.2 Level 1
To reach Level 1, a model must add an operationaliz
Models that do not convey anything about the unde
being pattern reproduction rather than creating hypo
phenomenal; They have an operationally defined 𝑇 a
𝑆 can produce the operationalized patterns of 𝑇 . Ho
produce 𝑇 in any way. To put it another way, they are
which match a pattern operationalized as 𝑇 .
Recently, Level 1 models using LLM agents have b
models in cooperation, games, and other environment
benchmark how different LLMs perform in those abstr
work on placing LLMs in game-theoretic scenarios to
The research questions of these simulations often fo
{𝑥 0 , 𝑥 1 , . . . , 𝑥 𝑚 }” and are questions of generative suffic
More generally, a lot of work uses multi-agent LLM s
such as their capacity for cooperation or their inherent
LLM agents’ capabilities, not to necessarily explain a
generative ABM literature by Larooij et al. [45], we s
evaluation metric in this way, which we argue is an as
power.
The existence of a level 1 bucket also helps to flag if a
to produce LLM agents that return the outputs whic
behaviors of agents can be heavily influenced by pro
desired behavior is perfectly acceptable for a level 1

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
or how 𝑇 is created, it is not sufficient to just reproduce
to being a proxy for how 𝑇 may actually be generated
: Simulation (𝑆), Target phenomenon (𝑇 ), modeler
er defined below). We use this four-tuple to create a
le. Models climb our scale as more components of 𝑀
ms, as well as being overall more faithful in representing
will revisit at each level a high-level running example: a
s on a social media platform.
specified modeling goal. It consists of a Simulation 𝑆,
nerate outputs but lacks a clearly defined phenomenon
enomenon (sometimes referred to as Glennan’s Law)
s. We place models that lack explicit operationalization
LLM agents are placed on a simulated social network
e purpose is to demo and explore a new simulation
erves what happens, but has no specified phenomenon
arget 𝑇 .
ng mechanism are said to be phenomenal, their purpose
es with their simulation [17, 18]. Models at level 1 are
re considered generatively sufficient if its simulation
er, it makes no claims about explanation. 𝑆 exists to
rd-coded’ simulations that produce a set of data points
used to explore the capabilities of different language
he goal is not to accurately model the scenario, but to
environments. For example, there exists a multitude of
how they act or perform [2, 16, 35, 43, 50].
w the lines of “can some LLM agents produce behaviors
y, rather than related to why a behavior was produced.
ulations to probe the capabilities of LLMs themselves,
ses. The goal of these simulations is to characterize the
ific real-world social dynamic. In the survey of recent
that many projects use believability as their primary
ment of generative sufficiency rather than explanatory
LM-based simulation is ‘cheating’. It is entirely feasible
roduce 𝑇 through the manipulation of prompts. The
t engineering; an engineered prompt that produces a
nomenal model. However, if an explanatory claim is

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
being made, it can become important to clarify in the
forces the correct output, or an intentional abstractio
model may be phenomenally ambiguous.
3.2.1 Example. Following our social media model ex
produce recognizable polarization patterns, operationa
They audit the simulation and report that the LLM ag
rate as believable.
At this stage, the simulation can serve two purpose
LLM agents interacting on a simulated platform. Secon
with similar features. Given these agents on this netw
expect it to do so again under similar conditions.
However, the polarization could be driven by the ag
algorithm, or some interaction among them. Therefore
behind the phenomenon.
3.3 Level 2
Simulations with a plausibility of level 2 move beyo
could possibly be generated. This is achieved when mo
and mapping (sometimes called a ‘model key’ [32])
proposed mechanisms responsible for generating 𝑇 . By
mechanisms of 𝑇 are related to the simulation code. E
Craver’s 3M requirement [41] in Section 2.3.
Modeling literature often refers to these post-phenom
or ‘logical possibilities’ [5]. One distinguishment of le
for reasoning about counterfactual scenarios, given a
example, one could reason about how 𝑇 might change
Later on in Level 3, when one tries to validate a mod
or wrong. It is worth being precise about what the ma
2.1, we distinguish between a model’s computations an
mapping is an interpretation that proposes how certa
standing in for certain real-world entities and activiti
simulation 𝑆 and target 𝑇 and propose different mapp
To tie this to LLM-ABM, suppose an agent is initi
describing a specific profile; we can imagine the map
behavioral patterns of a ‘person’ matching that profile
text prediction conditioned on a token sequence, which
processes of the described persona, we need the mappin
data encodes the relevant distributions about human b
empirical question that is scoped to each particular d
assumption is reasonable is an open problem that wou
3.3.1 Example. At Level 2, our example researchers
emerges in their simulation because agents engage wit
the simulated feed algorithm amplifies this by surfaci
researchers propose that the LLM agents stand in for

Zhao et al.
odel’s intent 𝐼 whether the prompt is an ‘artifact’ that
a real-world mechanism. Without this clarification, a
le, at Level 1, the researchers tweak the simulation to
d as some clustering of sentiment scores over time (𝑇 ).
s produce polarized discourse that human annotators
rst, it demonstrates that polarization can emerge from
, it could be used to forecast polarization on platforms
structure, polarization reliably emerges, and we might
’ prompts, the network topology, the recommendation
model does not serve to identify causal responsibilities
eproducing 𝑇 to proposing a hypothesis for how it
er specifies their Intent 𝐼 , which includes a hypothesis
t connects the components and activities in 𝑆 to the
ng this, one states a hypothesis about how the possible
er, we discussed and summarized this into Kaplan and
al simulations as ‘how-possibly’ simulations [11, 32, 89]
2 from level 1 simulations is that they provide a basis
othesis about 𝑇 ’s mechanisms encoded through 𝐼 . For
hose mechanisms were different.
is what determines if the simulation behavior is right
ng in 𝐼 involves epistemically; As discussed in Section
he interpretation the modeler assigns to it [22, 83]. The
computational components of 𝑆 can be understood as
This means that two modelers could look at the same
s in 𝐼 .
ed through persona prompts or steering vectors [14]
g in 𝐼 interpreting the LLM’s outputs as reflecting the
nsidering the LLM’s “theory proper” is autoregressive
rs questionable structural resemblance to the cognitive
o state: the modeler is assuming that the LLM’s training
vior. Whether this assumption holds for a given 𝑇 is an
ain. As this is a developing field, discerning when this
benefit from community discussion.
opose a hypothesis and mapping 𝐼 : that polarization
ontent that aligns with their initialized viewpoints, and
high-engagement content. As part of the mapping, the
users on the social media platform, as the affordances

Mechanism Plausibility in Generative Agent-Based Modeling FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
made on the simulated platform (posting, replying, sharing, and receiving algorithmically ranked content) mirror
the same that are available to real users. With this, future interventional questions become answerable relative to
the hypothesis. For instance, “what happens if we ablate on the recommendation algorithm?” is now a meaningful
experiment to add to evidence 𝐸, because the modeler has specified components they believe to be causally
responsible, and exposes the hypothesis and its details to falsification.
Level 𝑆 𝑇 𝐼 𝐸
0 ✓ ∅ ∅ ∅
1 ✓ ✓ ∅ ∅
2 ✓ ✓ ✓ ∅
3 ✓ ✓ ✓ ✓
Table 1. Plausibility levels and their relationship to the existence/falsifiability of a model’s components.
3.4 Level 3
A simulation with plausibility level 3 attempts to ground its components in evidence 𝐸, which is used to support
or constrain the model’s construction, parameterization, or validation. Since the addition of each previous
term in 𝑆,𝑇 , 𝐼 is what makes them falsifiable, this evidence could inform the design of the simulation 𝑆, the
operationalization of the target 𝑇 , or the justification for the mapping in 𝐼 . 𝐸 could also come in the form of
further constrained experiments, for example, ablations or sensitivity analyses that reinforce the prescribed
hypotheses contained in the mapping. A modeler might select initial parameters based off of some observed
values from census data, survey results, or prior empirical studies. For example, initializing an agent’s political
beliefs based on real-world polling data from a specific region might constitute a piece of evidence 𝐸.
Prior work suggests that how-possibly and how-actually explanations may exist on a continuum rather than
as a strict dichotomy [12]. Metaphorically, as more evidence is gathered for the conditions postulated in an
explanation, the explanation moves along the continuum until it is counted as how-actually. Adopting this
viewpoint to our scale, Level 3 can be thought of not as a binary threshold like levels 0 through 2, but a gradient
progressing further as the quality, quantity, and directness of that evidence increases towards an unreachable Ω.
We return to the question of why evidence can only asymptotically approach a definitive confirmation in Section
3.5.
In our discussion in Section 5, we elaborate on the confusion creators of LLM-based social simulations face in
gathering relevant evidence 𝐸, particularly when much of the research effort is focused on validating the agent’s
internal architecture rather than the emergent social phenomenon.
3.4.1 Example. Continuing the social media polarization example, at Level 3 the researchers ground the simulation by presenting varying evidence 𝐸. They show how agent viewpoint distributions are initialized from real
survey data on political attitudes in a specific region and the recommendation algorithm mirrors a documented
platform’s ranking function. They run ablation studies showing that reducing the algorithmic amplification
component significantly reduces polarization, consistent with prior empirical findings. Whether this evidence is
appropriate is a judgment for the standards of their research domain. The model becomes more plausible as more
of its components are supported, but the question of “plausible enough” is not one the scale answers, just makes
explicit.
3.5 Interpreting the Plausibility Scale
Given these levels in their increasing order, it is not to say that simulations of a lower plausibility level are worse.
It is of general agreement among scientists and philosophers that idealizations are useful, if not, necessary in

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
Fig. 2. The Plausibility scale classifies models based on their epistemic contribution. Level Ω is considered the unreachable
simulation that we can approach along level 3 continuously.
building models [8, 23, 63]. Our scale clarifies the kind of epistemic contribution each simulation can provide.
Some simulations demonstrate that a pattern can be generated, others propose and test explanations for how it
can arise. Morgan and Morrison aptly describe that models can function as partially autonomous instruments
that mediate between theory and data without being fully derived from either [59]; they can serve as tools
for exploration even when they are known to be incomplete or idealized. For example, level 0 simulations like
cellular automata can demonstrate that emergent behavior can arise from simple rules, which sets the ground for
new simulation paradigms. Level 2 simulations can be used to generate “how-possibly” hypotheses which are
falsifiable at the mechanisms level.
What increases as we move up the scale is the number of commitments the model has made that can, in
principle, be shown to be wrong, and scope of the claims it can support. At Level 1, only the reproduction of 𝑇 is at
stake. At Level 2, the mapping 𝐼 becomes an additional falsifiable commitment. At Level 3, the empirical grounding
𝐸 opens further points of potential failure. In addition, the confidence that the operationalized components of
𝑆 faithfully capture the abstract constructs and hypotheses the modeler intends them to represent, becomes
increasingly examinable as more of the model’s structure is made explicit and subject to evidence. We file all of
this under the umbrella term of ‘plausibility’.
It is also of note that each term in 𝑀 = (𝑆,𝑇 , 𝐼, 𝐸) is sequentially dependent on the previous terms for moving
up plausibility levels. Consider a counterexample where a simulation 𝑆 only has component 𝐸. If there is no 𝑇
and 𝐼 , the pair of 𝑆 and 𝐸 stands as a pairing of simulation outputs and arbitrary ‘facts’, with no clear mapping
between them. Thus, 𝑇 and 𝐼 are necessary relational structures that, when composed in sequence as (𝑆,𝑇 , 𝐼, 𝐸),
turn sets of unrelated facts into points of evidence which support a hypothesis. This is also why Table 1 can be
helpful, as it shows each level depends on the inclusion of all previous terms.
3.5.1 The unreachable Ω simulation. Finally, we describe the theoretical unreachable model where every mechanism for a target phenomenon is described and leaves no doubt as to whether 𝑆 is a faithful representation of
𝑇 . In the mechanist’s view, to fully describe the mechanisms of a phenomenon is to explain it. We refer to this
as a Level Ω simulation and note that it is a fiction we may never reach. As Brandon [12] argues, how-possibly
explanations can be thought of as a continuum toward how-actually, as more evidence is accumulated for their
postulated conditions. In our scale, Level Ω (see Figure 2) represents the (fictional) endpoint of this continuum
where all postulated conditions are fully confirmed and we are sure that the mechanisms in 𝑆 are the mechanisms
responsible for producing 𝑇 in actuality. However, Bokulich [11] suggests that as evidence confirms a mechanism
at one level of abstraction, attempts to specify that mechanism open new branches of how-possibly explanation,
each requiring their own evidence. Following this, the approach toward Ω may be better thought of as a “branching” process in which settling one question reveals further open ones that are implicitly abstracted away when
unanswered.
Moreover, a related limitation arises from the more general relationship between evidence and theory. The
Duhem-Quine thesis, loosely, holds that hypotheses are never tested in isolation, therefore the unambiguous
falsification of a scientific hypothesis is impossible [21, 68]. Another reason why we can never reach the Ω Level

Mechanism Plausibility in Generative Agent-Based Modeling
is that when a model is tested against empirical obse
attributed to particular components.
It is important to characterize the Ω level both beca
and because it makes explicit that one cannot confir
behind a phenomenon.
4 The Mechanism Plausibility Scale Heuristic
We draw on existing frameworks for reporting on mac
and present a checklist for using the Mechanism Plausib
are long-standing, established problems in science, th
with putting out artifacts that are epistemically cohesi
evidence are aligned and appropriately scoped to one an
A we follow examples using historical ABMs, one for
5 Discussion
In the following section we review some popular ways
we engage with broader ethical and epistemic conside
over historical examples and issues where the unders
5.1 Reflections on the State of LLM Social Simu
“How can we use LLM social simulation practically?” G
behind a phenomenon (as discussed in Section 3.5) th
are LLM-ABMs adequate for a given purpose?”
The current state of affairs for LLM social simulatio
producing a target phenomenon. On the surface, the
further up the “generative sufficiency scale”, allowin
new work in the area. This focus on generative suffi
al., where 22 out of 35 surveyed LLM social simulatio
metric [45]. Here, the believability of an agent actio
(experimentally as part of a study, or simply by inspe
(Level 1) may be adequate for demonstrating that a ph
such as brainstorming and prototyping. However, if a m
that have not been observed – for example, how a pol
implicitly making a claim about which components
claim, whether or not the modeler frames it as such.
The field of machine learning revolves around lear
observed examples. The primary goal for many pape
workings are often considered a separate topic from
is the goal. However, there are a couple of caveats w
the evaluation of a functioning/believable LLM agent
simulation in exploring unknown scenarios, where p
for producing relevant counterfactuals.
We observe that LLM-based simulation is prone to co
validation. What do we mean by this? From the age
presupposed mechanism – they are generally not the

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
tions, a failure (or success) cannot unambiguously be
of the inevitable idealizations introduced into models,
hat a simulation has fully described the mechanisms
e learning datasets and model deployments [29, 58, 85]
y Scale. While hypothesis testing and operationalization
ovelty of LLM-ABMs may lead researchers to struggle
where the target phenomenon, claims, and supporting
er. In Figure 3 we present the heuristic and in Appendix
h level in the scale.
Ms are currently being used in simulation. Later in 5.3,
ons for using LLM in simulation. In Section 5.4, we go
fication of models may have caused real-world harms.
ion
n that no simulation can fully exhaust the mechanisms
uestion is best interpreted as, “Under what conditions
ve a focus on demonstrating a simulation is capable of
ition of LLMs in social simulation seemed to move us
ents to access a larger action space, which prompted
cy is reflected in the systematic review by Larooij et
apers used ‘believability’ as their primary validation
r simulation outcome is judged by humans or LLMs
n). A simulation validated only through believability
omenon can be generated, or for exploratory purposes
ler wishes to test what would happen under conditions
intervention might alter the dynamics of 𝑇 – they are
are causally responsible for 𝑇 . This is a mechanistic
g unknown functions or distributions from real-world
may be predictive accuracy, and the model’s internal
mpirical evaluations. This is no problem if prediction
LLM social simulation: many LLM-ABM projects use
enerative sufficiency to justify the usefulness of their
ible mechanisms instead would be the relevant factor
tion of agent-level validation for ABM/simulation-level
based modeling perspective, a functioning agent is a
et phenomena of interest. An agent’s behaviors would

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
Mechanism Plausibility Scale Heuristic (𝑆,𝑇 , 𝐼, 𝐸)
This scale grades the model’s contribution as a plausible explanation for a target phenomenon. While not every
model’s goal is to be explanatory, it is important to clarify when it is appropriate.
Level 0: Simulation (𝑆) – Sandbox/Toy Model
□ Simulation. Is the simulation (S) defined, including environments, agents, and update rules?
The requirements for Level 0 are relatively minimal; It essentially shares the same requirements for something to be
considered an ABM or simulation, and mainly exists to distinguish it from the other levels. Level 0 simulations are
often toys or demonstrations of new simulation paradigms (e.g., Conway’s Game of Life, a demo for a new simulation
framework/technique).
Level 1: Target Phenomenon (𝑇 ) – Phenomenal Model
□ Defined Target Phenomenon. Is a target phenomenon (𝑇 ) operationalized (e.g. as statistical patterns, human
annotations/observations, etc.)?
□ Generative Sufficiency. Can the simulation (𝑆) successfully generate the patterns described in (𝑇 )?
□ Reproducibility. Does the reproducibility of the simulation (seeds, API versions, consideration of proprietary
prompt injections or version changes, inherent stochasticity, etc.) match the reproducibility goals of the modeler
or the field they are working in (sensitivity analysis requirements, etc.)?
The Level 1 requirement checks if there are explicit conditions that determine if the phenomena have happened and if the
model produces the specified phenomena. Level 1 simulations often show that something (𝑇 ) is possible or achievable using
the entities and activities of the simulation (e.g. Can LLM agents solve games, pass theory of mind, benchmarks, etc.).
Level 2: Intent & Mapping (𝐼) – How-Possibly Model
□ Simulation Contribution. Is the simulation’s use case understood (e.g., predictive, exploratory, illustrative,
explanatory, etc.)?
□ Falsifiable Hypotheses. Does there exist a hypothesis for how the target phenomenon 𝑇 arises from components
in the model?
□ Mechanism Mapping. Is there an Intent 𝐼 (implicit or explicit mapping) which connects components of the
simulation (𝑆) to the hypothesized ‘real-world’ mechanisms of (𝑇 )?
Level 2 is a check for if the modelers have explicitly proposed how the phenomena (or parts of the phenomena) of interest
are produced using the components of their simulation. This is important to make the model falsifiable.
Level 3: Evidence (𝐸) – Plausible Model (if validated)
□ Evidence Exists. Is the model supported by some evidence 𝐸?
□ Relevance. Is 𝐸 directed towards the claims made in 𝐼? Could 𝐸, in principle, disconfirm the hypotheses in 𝐼?
Adding any 𝐸 to get a simulation to Level 3 is straightforward; The difficulty lies in the model to remain valid, as the 𝐸
becomes additional falsifiable parts of the model. What is considered acceptable 𝐸 is bounded by the standards of the
domain the model is in.
Conclusion: Based on the checklist, the model is classified as a Level [X] model.
Fig. 3. The Mechanism Plausibility Scale in checklist form.
have been manually programmed in classic agent-based models, and a non-functioning agent would have meant
that the programmer made a bug. In our own attempts to review ABM papers that employ LLM-driven agents,

Mechanism Plausibility in Generative Agent-Based Modeling
we found that works tended to focus heavily on justif
given that LLM-driven agents are a relatively new s
intentional gloss is not guaranteed by the theory prop
the agent architecture (e.g., showing the agent can rem
𝐼 concerning a higher-level social phenomenon 𝑇 . A
𝑆, but its functionality alone does not validate the m
simulation-level mechanisms, we refer to the visual m
[19] showing how the overall phenomena 𝑇 is produc
An open question is how current LLM simulation
given the discussed limitations so far. While we do no
practitioners already reason about simulations in w
ran a year-long human co-design of simulations wit
2024-2025 [49]. The policymakers seemed to show sk
the agents exhibited believable behavior. Instead, the s
tool. For example, when a simulation’s dynamics we
tacit knowledge and allowed them to list out importan
settings. This has echoes in work done by Park et al. [
designers identify and prototype solutions to potentia
The preparedness team began to trust the simulations
scenarios, when the authors tested it against their in
Once the policymakers saw that the simulations gen
experience and intuition, they were willing to entertain
higher-level, abstracted mechanisms.
5.2 Proprietary LLM APIs and Reproducibility
LLM API services have been known to introduce pro
the end user. These features are added for safety, regu
detrimental to experimental validity. For example, hid
an agent’s behavior or prevent agents from exhibiting r
proprietary LLMs are often subject to unannounced ve
behavior between runs. This problem is solvable with
to entry for many researchers because of things like G
Concerning ethical considerations of proprietary m
practices that fall below disciplinary ethical standa
practices involving underpaid workers, the inclusion
methodological and epistemic side, closed-process (tra
the community’s ability to inspect training data, att
rigorous control over their scientific methodology.
There are growing movements toward addressing t
have demonstrated that competitive language mode
and intermediate checkpoints, with the goal of enabli
Network advocates for treating AI as public infrastru
produce permanent public goods [38]. However, at the
both commercial deployment and research usage.
1See https://github.com/asgeirtj/system_prompts_leaks and similar

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
g their design of LLM-driven agents; this makes sense
lation technique. However, just as the validity of an
Section 2.1), evidence supporting the functionality of
er facts) is not sufficient as evidence 𝐸 for the mapping
nctioning agent is a necessary part of the simulation
el’s explanation of 𝑇 . To distinguish agent-level and
phor in Figure 1, which is a modified Craver diagram
by agents {𝑥 1 , . . . , 𝑥 𝑚 } and activities {𝜙 1 , . . . , 𝜙 𝑛 }.
an be made useful for policy or sociological settings
tempt to answer this fully, recent work suggests that
that align with the distinctions in our scale. Li et al.
heir university’s emergency preparedness team from
cism towards any models’ predictive abilities, even if
ulations seemed to help them more as a brainstorming
dentified to be wrong, it resurfaced the policymakers’
oncerns, for example, wheelchair ramps in evacuation
where ‘false’ simulated social media platforms helped
oblems before they came up in a real deployed setting.
e once the simulations started to align with real-world
ution’s real-world graduation commencement setting.
ted behavior that matched outcomes based on their
‘how-possibly’ outcomes generated by the simulation’s
injections, guardrails, or system prompts invisible to
on, or other proprietary purposes but can be actively
prompts could unknowingly change the trajectory of
vant behavior the modeler is interested in. Furthermore,
on or system prompt1 updates, which could alter agent
n-sourced locally hosted models, but raises the barrier
and technical constraints.
ls, LLM training data is frequently assembled through
for example, mass scraping without consent, labor
rivate data, and environmental harms [34, 80]. On the
ng sources and methods, weights) models compromise
ute model behavior to appropriate sources, and have
concerns. Initiatives such as AI2’s OLMo project [33]
an be developed with fully open training data, code,
he scientific study of language models. The Public AI
re – publicly accessible, accountable, and designed to
e of writing, proprietary models continue to dominate
n-the-wild examples.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
5.3 Broader Ethical and Epistemic Concerns
The problems related to reproducibility, proprietary
mechanistic plausibility are largely methodological. H
about the use of LLMs in social simulation that warra
Regarding whether LLMs should serve as proxies for
proposals to substitute human research participants w
with values relating to representation, inclusion, and
with LLMs may disregard the relationship between
research. When an LLM generates text that resembl
from the experience of a live, present individual. Furth
referenced by Weidinger et al. [81]. LLMs encode th
particular point in time. Related empirical work suppo
time periods not represented in their training corpus
5.4 Historical Issues and Harms of Poor ABM s
While the Mechanism Plausibility Scale was motivate
not specific to ABMs with LLMs; The literature surro
long-standing discussion [6, 45, 60, 72, 74, 76]. Importa
is not only important to the modeler herself, but also
Squazzoni et al. [72] note that during the COVID
reported that results from their model projected “a h
policy measures were taken”. The results of their mode
by the UK government, and advised governments of cou
the damages caused by the virus. However, because of u
model erroneously affected the policies of many count
further peer analysis of the model showed it may onl
the simulation code was not made public, even later a
Axelrod’s iterated Prisoner’s Dilemma (PD) simu
adapted script on “The Evolution of Cooperation” [7]
arms races, nuclear proliferation, and crisis bargaining
advice to players of the game theoretic scenario might
and Alexandrova [60] observe that despite the enormo
1960), it has largely failed to explain phenomena of so
Arnold (sharply) observes a broader pattern in the
simulations produced practically no successful empir
He identifies, firstly, the “justificatory narratives” mod
the model is merely heuristic or exploratory without sp
arguing that all models rely on simplification, a defens
a model isolates are empirically discernible from the o
not, the simplification cannot be tested.
We felt it appropriate to reiterate these issues unde
growing interest in simulation using LLMs.

Zhao et al.
Is, and the conflation of generative sufficiency with
ever, there are broader ethical and epistemic concerns
onsideration.
man subjects in the first place, Agnew et al. [1] examine
LLM surrogates and find that such proposals conflict
erstanding of human subjects. Replacing participants
earcher and subject existing in prior human subject
urvey responses or social behavior, it is not directly
more, they identify the problem of “value lock-in”, also
orms and attitudes present in their training data at a
his; language models exhibit degraded performance in
.
ification
y recent challenges posed by LLM-ABM, the ideas are
ing well-motivated, sound ABM design in general is a
y, we demonstrate how understanding a model’s limits
s end users.
pandemic, a team at the Imperial College of London
number of people would die in Britain unless severe
d interventions were quickly adopted and implemented
ies like the US and France in their attempts to minimize
erspecification on what the model was adequate for, the
, namely, being used in counterfactual scenarios when
ave been adequate for illustrative purposes. Moreover,
e time of Squazzoni et al.’s publication.
ons are another well-known problematic case. In an
xelrod asserts that many real-world scenarios such as
instances of the iterated Prisoner’s Dilemma, and that
ve as advice to national leaders. In response, Northcott
attention devoted to the PD (over 16,000 articles since
scientific interest.
deling tradition [6]: over thirty years of Repeated PD
applications, yet this failure has been largely ignored.
rs use after scrutiny, which is retreating to claims that
fying the limits of that exploration. Secondly, modelers
at, as Arnold notes, only holds when the causal factors
r factors at work in the target system. When they are
ur scale and point to related work, especially with the

Mechanism Plausibility in Generative Agent-Based Modeling
6 Conclusion and Limitations
In this paper we connect contemporary mechanisms,
literature with agent-based modeling and LLM social s
heuristic that classifies simulations into levels based
and offer a practical checklist. Through a review of rec
category errors between Agent-level and ABM-level
these problems with existing issues in ABM and highlig
happened in high-stakes scenarios. While our scale p
refined to differentiate the quality and extent of eviden
be said about a separate axis for predictive models, as
of the paper, ultimately, remains grounding multiple d
to attention.
Generative AI Usage Statement
This document was produced with the assistance of G
checklists, figures, proofreading, and typographical lay
authors also used AI-augmented paper search engines
References
[1] William Agnew, A. Stevie Bergman, Jennifer Chien, Mark D
McKee. 2024. The illusion of artificial inclusion. In Proceedin
doi:10.1145/3613904.3642703 arXiv:2401.08572 [cs].
[2] Elif Akata, Lion Schulz, Julian Coda-Forno, Seong Joon Oh, Ma
Language Models. Nature Human Behaviour (May 2025). doi:
[3] Altera AL, Andrew Ahn, Nic Becker, Stephanie Carroll, Nico
Luo, Peter Y. Wang, Mathew Willows, Feitong Yang, and Guan
civilization. doi:10.48550/arXiv.2411.00114 arXiv:2411.00114 [
[4] Jacy Reese Anthis, Ryan Liu, Sean M. Richardson, Austin C. K
Bernstein. 2025. LLM Social Simulations Are a Promising Res
[5] Eckhart Arnold. 2013. Simulation Models of the Evolution of C
E Politica 15, 2 (2013), 101–138. https://philarchive.org/rec/AR
[6] Eckhart Arnold. 2015. How Models Fail: A Critical Look at th
Collective Agency and Cooperation in Natural and Artificial Sy
261–279. doi:10.1007/978-3-319-15515-9_14
[7] Robert Axelrod. [n. d.]. The Evolution of Cooperation*. ([n. d.]
[8] N. Emrah Aydinonat. 2024. The puzzle of model-based explan
ed.). Routledge, London, 177–192. doi:10.4324/9781003205647
[9] Paul Bartha. 2024. Analogy and Analogical Reasoning. In The S
Nodelman (Eds.). Metaphysics Research Lab, Stanford Universit
[10] James Bogen and James Woodward. 1988. Saving the Phen
doi:10.2307/2185445
[11] Alisa Bokulich. 2014. How the Tiger Bush Got its Stripes: ‘How
2014), 321–338. doi:10.5840/monist201497321
[12] Robert N. Brandon and Robert N. Brandon. 2014. Adaptat
10.1515/9781400860661
[13] P. W. (Percy Williams) Bridgman. 1927. The Logic of Modern P
[14] Runjin Chen, Andy Arditi, Henry Sleight, Owain Evans, and Ja
Traits in Language Models. doi:10.48550/arXiv.2507.21509 arX
2https://asta.allen.ai/chat

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
nitive representation, and other philosophy of science
lation. We present the Mechanism Plausibility Scale, a
he falsifiability and existence of components 𝑆,𝑇 , 𝐼, 𝐸
LLM-ABM papers we confirm the existence of common
ponents and underspecified models. We also connect
he historical harms that occurred when these mistakes
des a useful heuristic, the criteria for Level 3 could be
𝐸 for a more practical setting. Additionally, more could
osed to our plausible explanation axis. The main focus
plines in common language and bringing these issues
erative AI, which assisted in the formatting of tables,
of the paper. It was also used to generate critique; the
ch as Asta2, for paper discovery.
Seliem El-Sayed, Jaylen Pittman, Shakir Mohamed, and Kevin R.
the CHI Conference on Human Factors in Computing Systems. 1–12.
s Bethge, and Eric Schulz. 2025. Playing repeated games with Large
38/s41562-025-02172-y arXiv:2305.16867 [cs].
tie, Manuel Cortes, Arda Demirci, Melissa Du, Frankie Li, Shuying
Robert Yang. 2024. Project Sid: Many-agent simulations toward AI
owski, Bernard Koch, James Evans, Erik Brynjolfsson, and Michael
Method. doi:10.48550/arXiv.2504.02234 arXiv:2504.02234 [cs].
ration as Proofs of Logical Possibilities. How Useful Are They? Etica
MO Publisher: University of Trieste, Department of Philosophy.
story of Computer Simulations of the Evolution of Cooperation. In
, Catrin Misselhorn (Ed.). Springer International Publishing, Cham,
tps://ee.stanford.edu/~hellman/Breakthrough/book/pdfs/axelrod.pdf
n. In The Routledge Handbook of Philosophy of Scientific Modeling (1
rd Encyclopedia of Philosophy (fall 2024 ed.), Edward N. Zalta and Uri
ps://plato.stanford.edu/archives/fall2024/entries/reasoning-analogy/
na. The Philosophical Review 97, 3 (1988), 303–352. jstor:2185445
sibly’ vs. ‘How Actually’ Model Explanations. The Monist 97, 3 (July
nd environment. Princeton University Press, Princeton. doi:doi:
s. The Macmillan Company.
ndsey. 2025. Persona Vectors: Monitoring and Controlling Character
507.21509 [cs].

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
[15] Weize Chen, Yusheng Su, Jingwei Zuo, Cheng Yang, Chenfei Yuan, Chi-Min Chan, Heyang Yu, Yaxi Lu, Yi-Hsin Hung, Chen Qian, Yujia
Qin, Xin Cong, Ruobing Xie, Zhiyuan Liu, Maosong Sun, and Jie Zhou. 2023. AgentVerse: Facilitating Multi-Agent Collaboration and
Exploring Emergent Behaviors. doi:10.48550/arXiv.2308.10848 arXiv:2308.10848 [cs].
[16] Anthony Costarelli, Mat Allen, Roman Hauksson, Grace Sodunke, Suhas Hariharan, Carlson Cheng, Wenjie Li, and Arjun Yadav. 2024.
GameBench: Evaluating Strategic Reasoning Abilities of LLM Agents. doi:10.48550/arXiv.2406.06613 arXiv:2406.06613 [cs] version: 1.
[17] Carl Craver, James Tabery, and Phyllis Illari. 2024. Mechanisms in Science. In The Stanford Encyclopedia of Philosophy (fall 2024 ed.),
Edward N. Zalta and Uri Nodelman (Eds.). Metaphysics Research Lab, Stanford University. https://plato.stanford.edu/archives/fall2024/
entries/science-mechanisms/
[18] Carl F. Craver. 2006. When mechanistic models explain. Synthese 153, 3 (Dec. 2006), 355–376. doi:10.1007/s11229-006-9097-x
[19] Carl F. Craver. 2009. Explaining the Brain. Oxford University Press.
[20] Lee J. Cronbach and Paul E. Meehl. 1955. Construct validity in psychological tests. Psychological Bulletin 52, 4 (1955), 281–302.
doi:10.1037/h0040957 Place: US Publisher: American Psychological Association.
[21] Pierre Maurice Marie Duhem. 1954. The aim and structure of physical theory. Vol. 1. Princeton University Press. Pages: 85-87.
[22] Frances Egan. 2025. Deflating Mental Representation (The Jean Nicod Lectures). MIT Press (open access).
[23] Catherine Z. Elgin. 2004. True Enough. Philosophical Issues 14 (2004), 113–131. https://www.jstor.org/stable/3050623 Publisher: [Wiley,
Ridgeview Publishing Company].
[24] Joshua M. Epstein. 2006. Generative Social Science: Studies in Agent-Based Computational Modeling (stu - student edition ed.). Princeton
University Press. http://www.jstor.org/stable/j.ctt7rxj1
[25] Ronald Aylmer Fisher. 1999. The genetical theory of natural selection: by R.A. Fisher ; edited with a foreword and notes by J.H. Bennett (a
complete variorum ed ed.). Oxford University Press, Oxford.
[26] Chen Gao, Xiaochong Lan, Zhihong Lu, Jinzhu Mao, Jinghua Piao, Huandong Wang, Depeng Jin, and Yong Li. 2025. S$^3$: Social-network
Simulation System with Large Language Model-Empowered Agents. arXiv:2307.14984 [cs] doi:10.48550/arXiv.2307.14984
[27] Martin Gardner. 1970. Mathematical Games. Scientific American 223, 4 (1970), 120–123. https://www.jstor.org/stable/24927642 Publisher:
Scientific American, a division of Nature America, Inc..
[28] Edward G.Carmines and Richard A.Zeller. 1979. Reliability and Validity Assessment. SAGE Publications, Inc. doi:10.4135/9781412985642
[29] Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach, Hal Daumé III, and Kate Crawford.
2021. Datasheets for Datasets. doi:10.48550/arXiv.1803.09010 arXiv:1803.09010 [cs].
[30] Stuart Glennan. 2017. The New Mechanical Philosophy. Oxford University Press, Oxford.
[31] Stuart S. Glennan. 1996. Mechanisms and the nature of causation. Erkenntnis 44, 1 (Jan. 1996), 49–71. doi:10.1007/BF00172853
[32] Claudius Graebner. 2018. How to Relate Models to Reality? An Epistemological Framework for the Validation and Verification of
Computational Models. Journal of Artificial Societies and Social Simulation 21, 3 (2018), 8.
[33] Dirk Groeneveld, Iz Beltagy, Pete Walsh, Akshita Bhagia, Rodney Kinney, Oyvind Tafjord, Ananya Harsh Jha, Hamish Ivison, Ian
Magnusson, Yizhong Wang, Shane Arora, David Atkinson, Russell Authur, Khyathi Raghavi Chandu, Arman Cohan, Jennifer Dumas,
Yanai Elazar, Yuling Gu, Jack Hessel, Tushar Khot, William Merrill, Jacob Morrison, Niklas Muennighoff, Aakanksha Naik, Crystal Nam,
Matthew E. Peters, Valentina Pyatkin, Abhilasha Ravichander, Dustin Schwenk, Saurabh Shah, Will Smith, Emma Strubell, Nishant
Subramani, Mitchell Wortsman, Pradeep Dasigi, Nathan Lambert, Kyle Richardson, Luke Zettlemoyer, Jesse Dodge, Kyle Lo, Luca Soldaini,
Noah A. Smith, and Hannaneh Hajishirzi. 2024. OLMo: Accelerating the Science of Language Models. doi:10.48550/arXiv.2402.00838
arXiv:2402.00838 [cs].
[34] Olivia Guest and Iris van Rooij. 2025. Critical Artificial Intelligence Literacy for Psychologists. doi:10.31234/osf.io/dkrgj_v1
[35] Fulin Guo. 2023. GPT in Game Theory Experiments. doi:10.48550/arXiv.2305.05516 arXiv:2305.05516 [econ].
[36] John J. Horton. 2023. Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? doi:10.48550/
arXiv.2301.07543 arXiv:2301.07543 [econ].
[37] Wenyue Hua, Lizhou Fan, Lingyao Li, Kai Mei, Jianchao Ji, Yingqiang Ge, Libby Hemphill, and Yongfeng Zhang. 2024. War and Peace
(WarAgent): Large Language Model-based Multi-Agent Simulation of World Wars. doi:10.48550/arXiv.2311.17227 arXiv:2311.17227 [cs].
[38] Brandon Jackson, B Cavello, Flynn Devine, Nick Garcia, Samuel J. Klein, Alex Krasodomski, Joshua Tan, and Eleanor Tursman. 2024.
Public AI: Infrastructure for the common good. doi:10.5281/zenodo.13914560
[39] Frank Jackson. 1982. Epiphenomenal Qualia. The Philosophical Quarterly 32, 127 (April 1982), 127–136. doi:10.2307/2960077
[40] Zhao Kaiya, Michelangelo Naim, Jovana Kondic, Manuel Cortes, Jiaxin Ge, Shuying Luo, Guangyu Robert Yang, and Andrew Ahn. 2023.
Lyfe Agents: Generative Agents for Low-Cost Real-Time Social Interactions. arXiv:2310.02172 [cs] doi:10.48550/arXiv.2310.02172
[41] David Michael Kaplan and Carl F. Craver. 2011. The Explanatory Force of Dynamical and Mathematical Models in Neuroscience: A
Mechanistic Perspective*. Philosophy of Science 78, 4 (2011), 601–627. doi:10.1086/661755 Publisher: [The University of Chicago Press,
Philosophy of Science Association].
[42] Kendrick N. Kay. 2018. Principles for models of neural information processing. NeuroImage 180 (Oct. 2018), 101–109. doi:10.1016/j.
neuroimage.2017.08.016

Mechanism Plausibility in Generative Agent-Based Modeling
[43] Benjamin Kempinski, Ian Gemp, Kate Larson, Marc Lanctot,
Reasoning in Game-Theoretic Domains with Large Language M
Agents and Multiagent Systems (AAMAS ’25). International Fou
1088–1097.
[44] J. R. Landis and G. G. Koch. 1977. The measurement of observe
[45] Maik Larooij and Petter Törnberg. 2025. Do Large Language M
Generative Social Simulations. doi:10.48550/arXiv.2504.03274
[46] Angeliki Lazaridou, Adhiguna Kuncoro, Elena Gribovskaya
de Masson d’Autume, Tomas Kocisky, Sebastian Ruder, Dani Y
Gap: Assessing Temporal Generalization in Neural Language
[47] Huao Li, Yu Quan Chong, Simon Stepputtis, Joseph Campbell,
Multi-Agent Collaboration via Large Language Models. In Proc
Processing. 180–192. doi:10.18653/v1/2023.emnlp-main.13 arX
[48] Xinyi Li, Yu Xu, Yongfeng Zhang, and Edward C. Malthouse.
Diffusion Under Different Network Structures. doi:10.48550/a
[49] Yuxuan Li, Sauvik Das, and Hirokazu Shirado. 2025. What Ma
Design Engagement in Emergency Preparedness. doi:10.48550
[50] Yuxuan Li and Hirokazu Shirado. 2025. Spontaneous Giving a
arXiv:2502.17720 [cs].
[51] Yuhan Liu, Xiuying Chen, Xiaoqing Zhang, Xing Gao, Ji Zha
Attitude Dynamics Toward Fake News. In Proceedings of the Thi
doi:10.24963/ijcai.2024/873 arXiv:2403.09498 [cs].
[52] Kenneth MacCorquodale and Paul E. Meehl. 1948. On a Di
Psychological Review 55, 2 (1948), 95–107. doi:10.1037/h00560
[53] Peter Machamer, Lindley Darden, and Carl F. Craver. 2000.
https://www.jstor.org/stable/188611 Publisher: [The Universit
[54] Giordano De Marzo, Luciano Pietronero, and David Garcia. 202
Language Models. doi:10.48550/arXiv.2312.06619 arXiv:2312.0
[55] Michela Massimi. 2022. Perspectival Ontology: Between Situ
214–228. doi:10.1093/monist/onab032
[56] Michael D. Mauk. 2000. The potential effectiveness of simula
2000), 649–651. doi:10.1038/76606 Publisher: Nature Publishin
[57] James W. McAllister. 1997. Phenomena and Patterns in Data Se
1005387021520
[58] Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barne
and Timnit Gebru. 2019. Model Cards for Model Reporting. In P
220–229. doi:10.1145/3287560.3287596 arXiv:1810.03993 [cs].
[59] Mary S. Morgan and Margaret Morrison (Eds.). 1999. Mode
University Press, Cambridge. doi:10.1017/CBO9780511660108
[60] Robert Northcott and Anna Alexandrova. 2015. Prisoner’s
philosophical arguments., Martin Peterson (Ed.). Cambridge Un
[61] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith R
Agents: Interactive Simulacra of Human Behavior. doi:10.4855
[62] Joon Sung Park, Lindsay Popowski, Carrie Cai, Meredith Ring
Creating Populated Prototypes for Social Computing Systems.
and Technology (Oct. 2022), 1–18. doi:10.1145/3526113.3545616
Interface Software and Technology ISBN: 9781450393201 Plac
[63] Wendy S. Parker. 2020. Model Evaluation: An Adequacy-for-Pu
708691
[64] Debjit Paul, Robert West, Antoine Bosselut, and Boi Faltings. 2
Chain-of-Thought Reasoning. arXiv. doi:10.48550/ARXIV.2402
[65] Judea Pearl. 2009. Causality (2 ed.). Cambridge University Pre
[66] Judea Pearl and Dana Mackenzie. 2018. The book of why: The
[67] Axel Pichler and Nils Reiter. 2022. From Concepts to Texts a
Journal of Cultural Analytics 7, 4 (Dec. 2022). doi:10.22148/001

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
m Bachrach, and Tal Kachman. 2025. Game of Thoughts: Iterative
ls. In Proceedings of the 24th International Conference on Autonomous
tion for Autonomous Agents and Multiagent Systems, Richland, SC,
eement for categorical data. Biometrics 33, 1 (March 1977), 159–174.
s Solve the Problems of Agent-Based Modeling? A Critical Review of
v:2504.03274 [cs].
vang Agrawal, Adam Liska, Tayfun Terzi, Mai Gimenez, Cyprien
ama, Kris Cao, Susannah Young, and Phil Blunsom. 2021. Mind the
els. doi:10.48550/arXiv.2102.01951 arXiv:2102.01951 [cs].
Hughes, Michael Lewis, and Katia Sycara. 2023. Theory of Mind for
ngs of the 2023 Conference on Empirical Methods in Natural Language
10.10701 [cs].
. Large Language Model-driven Multi-Agent Simulation for News
2410.13909 arXiv:2410.13909 [cs].
LM Agent Simulations Useful for Policy? Insights From an Iterative
iv.2509.21868 arXiv:2509.21868 [cs].
alculated Greed in Language Models. doi:10.48550/arXiv.2502.17720
nd Rui Yan. 2024. From Skepticism to Acceptance: Simulating the
hirdInternational Joint Conference on Artificial Intelligence. 7849–7857.
tion between Hypothetical Constructs and Intervening Variables.
king about Mechanisms. Philosophy of Science 67, 1 (2000), 1–25.
Chicago Press, Philosophy of Science Association].
mergence of Scale-Free Networks in Social Interactions among Large
[physics].
Knowledge and Multiculturalism. The Monist 105, 2 (March 2022),
s versus phenomenological models. Nature Neuroscience 3, 7 (July
oup.
rkenntnis (1975-) 47, 2 (1997), 217–228. jstor:20012798 doi:10.1023/A:
cy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji,
edings of the Conference on Fairness, Accountability, and Transparency.
Mediators: Perspectives on Natural and Social Science. Cambridge
mma Doesn’t Explain Much. In The Prisoner?s Dilemma. Classic
sity Press, 64–84. https://philarchive.org/rec/NORPDD
l Morris, Percy Liang, and Michael S. Bernstein. 2023. Generative
Xiv.2304.03442 arXiv:2304.03442 [cs].
orris, Percy Liang, and Michael S. Bernstein. 2022. Social Simulacra:
edings of the 35th Annual ACM Symposium on User Interface Software
ference Name: UIST ’22: The 35th Annual ACM Symposium on User
nd OR USA Publisher: ACM.
e View. Philosophy of Science 87, 3 (July 2020), 457–477. doi:10.1086/
Making Reasoning Matter: Measuring and Improving Faithfulness of
50 Version Number: 4.
ambridge. doi:10.1017/CBO9780511803161
cience of cause and effect (1 ed.). Basic Books, Inc., USA.
Back: Operationalization as a Core Activity of Digital Humanities.
195

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
[68] Willard Van Orman Quine. 1953. From a Logical Point of View. Harvard University Press, Cambridge.
[69] Siyue Ren, Zhiyao Cui, Ruiqi Song, Zhen Wang, and Shuyue Hu. 2024. Emergence of Social Norms in Generative Agent Societies:
Principles and Architecture. doi:10.48550/arXiv.2403.08251 arXiv:2403.08251 [cs].
[70] Thomas C. Schelling. 1969. Models of Segregation. The American Economic Review 59, 2 (1969), 488–493. https://www.jstor.org/stable/
1823701 Publisher: American Economic Association.
[71] Galit Shmueli. 2010. To Explain or to Predict? Statist. Sci. 25, 3 (Aug. 2010). doi:10.1214/10-STS330
[72] Flaminio Squazzoni, J. Gareth Polhill, Bruce Edmonds, Petra Ahrweiler, Patrycja Antosz, Geeske Scholz, Emile Chappin, Melania Borit,
Harko Verhagen, Francesca Giardini, and Nigel Gilbert. 2020. Computational Models That Matter During a Global Pandemic Outbreak:
A Call to Action. JASSS - The Journal of Artificial Societies and Social Simulation 23, 2 (March 2020). doi:10.18564/jasss.4298
[73] S. S. Stevens. 1935. The Operational Definition of Psychological Concepts. Psychological Review 42, 6 (1935), 517–527. doi:10.1037/h0056973
[74] Samarth Swarup. 2019. Adequacy: What Makes a Simulation Good Enough?. In 2019 Spring Simulation Conference (SpringSim). 1–12.
doi:10.23919/SpringSim.2019.8732895
[75] Edward Bradford Titchener. 1910. A Text-Book of Psychology. MacMillan Co, New York, NY, US. xx, 565 pages. doi:10.1037/10907-000
[76] Loïs Vanhée, Melania Borit, Peer-Olaf Siebers, Roger Cremades, Christopher Frantz, Önder Gürcan, František Kalvas, Denisa Reshef
Kera, Vivek Nallur, Kavin Narasimhan, and Martin Neumann. 2025. Large Language Models for Agent-Based Modelling: Current and
possible uses across the modelling cycle. doi:10.48550/arXiv.2507.05723 arXiv:2507.05723 [cs] version: 1.
[77] Elina Vessonen. 2021. Conceptual engineering and operationalism in psychology. Synthese 199, 3 (Dec. 2021), 10615–10637. doi:10.1007/
s11229-021-03261-x
[78] Lei Wang, Jingsen Zhang, Hao Yang, Zhi-Yuan Chen, Jiakai Tang, Zeyu Zhang, Xu Chen, Yankai Lin, Hao Sun, Ruihua Song, Xin Zhao,
Jun Xu, Zhicheng Dou, Jun Wang, and Ji-Rong Wen. 2025. User Behavior Simulation with Large Language Model-based Agents. ACM
Trans. Inf. Syst. 43, 2 (Jan. 2025), 55:1–55:37. doi:10.1145/3708985
[79] Zhilin Wang, Yu Ying Chiu, and Yu Cheung Chiu. 2023. Humanoid Agents: Platform for Simulating Human-like Generative Agents.
doi:10.48550/arXiv.2310.05418 arXiv:2310.05418 [cs].
[80] Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato, Po-Sen Huang, Myra Cheng, Mia Glaese, Borja Balle,
Atoosa Kasirzadeh, Zac Kenton, Sasha Brown, Will Hawkins, Tom Stepleton, Courtney Biles, Abeba Birhane, Julia Haas, Laura Rimell,
Lisa Anne Hendricks, William Isaac, Sean Legassick, Geoffrey Irving, and Iason Gabriel. 2021. Ethical and social risks of harm from
Language Models. doi:10.48550/arXiv.2112.04359 arXiv:2112.04359 [cs].
[81] Laura Weidinger, Jonathan Uesato, Maribeth Rauh, Conor Griffin, Po-Sen Huang, John Mellor, Amelia Glaese, Myra Cheng, Borja Balle,
Atoosa Kasirzadeh, Courtney Biles, Sasha Brown, Zac Kenton, Will Hawkins, Tom Stepleton, Abeba Birhane, Lisa Anne Hendricks,
Laura Rimell, William Isaac, Julia Haas, Sean Legassick, Geoffrey Irving, and Iason Gabriel. 2022. Taxonomy of Risks posed by
Language Models. In 2022 ACM Conference on Fairness Accountability and Transparency. ACM, Seoul Republic of Korea, 214–229.
doi:10.1145/3531146.3533088
[82] Michael Weisberg. 2007. Who Is a Modeler? The British Journal for the Philosophy of Science 58, 2 (2007), 207–233. https://www.jstor.
org/stable/30115224 Publisher: [Oxford University Press, The British Society for the Philosophy of Science].
[83] Michael Weisberg. 2013. Simulation and Similarity: Using Models to Understand the World. Oxford University Press.
[84] Ross Williams, Niyousha Hosseinichimeh, Aritra Majumdar, and Navid Ghaffarzadegan. 2023. Epidemic Modeling with Generative
Agents. doi:10.48550/arXiv.2307.04986 arXiv:2307.04986 [cs].
[85] Michael Winikoff, John Thangarajah, and Sebastian Rodriguez. 2025. A Scoresheet for Explainable AI. doi:10.48550/arXiv.2502.09861
arXiv:2502.09861 [cs].
[86] Gal Yona, Roee Aharoni, and Mor Geva. 2024. Can Large Language Models Faithfully Express Their Intrinsic Uncertainty in Words?
(2024). doi:10.48550/ARXIV.2405.16908 Publisher: arXiv Version Number: 2.
[87] Dong Zhang, Zhaowei Li, Pengyu Wang, Xin Zhang, Yaqian Zhou, and Xipeng Qiu. 2024. SpeechAgents: Human-Communication
Simulation with Multi-Modal Multi-Agent Systems. doi:10.48550/arXiv.2401.03945 arXiv:2401.03945 [cs].
[88] Jintian Zhang, Xin Xu, Ningyu Zhang, Ruibo Liu, Bryan Hooi, and Shumin Deng. 2024. Exploring Collaboration Mechanisms for LLM
Agents: A Social Psychology View. doi:10.48550/arXiv.2310.02124 arXiv:2310.02124 [cs].
[89] Dunja Šešelja. 2023. Agent-Based Modeling in the Philosophy of Science. In The Stanford Encyclopedia of Philosophy (winter 2023 ed.),
Edward N. Zalta and Uri Nodelman (Eds.). Metaphysics Research Lab, Stanford University. https://plato.stanford.edu/archives/win2023/
entries/agent-modeling-philscience/

Mechanism Plausibility in Generative Agent-Based Modeling
A Examples
In this section we step through Figures 4-7, which con
Conway’s Game of Life
This scale grades the model’s potential as a plausible exp
goal is to be explanatory, it is important to clarify when
Level 0: Simulation (𝑆) – Sandbox/Toy Model
□✓ Simulation. Is the simulation (S) defined, including
The rules of the game are detailed: At each timestep, “1.
for the next generation. 2. Each counter with four or more
with one neighbor or none dies from isolation. Each empty
birth cell. A counter is placed on it at the next move.”
Level 1: Target Phenomenon (𝑇 ) – Phenomenal Mo
□ Defined Target Phenomenon. Is a target phenom
annotations/observations, etc.)?
□ Generative Sufficiency. Can the simulation (𝑆) suc
□✓ Reproducibility. Does the reproducibility of the si
prompt injections or version changes, inherent stoch
or the field they are working in (sensitivity analysis
While Conway selected his rules to try and make the be
there is no operationalized pattern that the simulation is i
[27].
Level 2: Intent & Mapping (𝐼) – How-Possibly Mode
□ Simulation Contribution. Is the simulation’s use
explanatory, etc.)?
□ Falsifiable Hypotheses. Does there exist a hypothe
in the model?
□ Mechanism Mapping. Is there an Intent 𝐼 (implic
simulation (𝑆) to the hypothesized ‘real-world’ mec
Due to the lack of 𝑇 , the simulation does not describ
phenomenon (see ‘Glennan’s Law’ [17, 31]).
Level 3: Evidence (𝐸) – Plausible Model (if validate
□ Evidence Exists. Is the model supported by some e
□ Relevance. Is 𝐸 directed towards the claims made i
Since 𝐸 requires 𝑇 and 𝐼, the model does not pass the Le
Conclusion: Based on the checklist, the model is cla
Fig. 4. Example for Level 0: The Mechanism Plausibility Sca

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
n example checklists filled out for each level.
tion for the target phenomenon. While not every model’s
s appropriate.
vironments, agents, and update rules?
y counter with two or three neighboring counters survives
hbors dies (is removed) from overpopulation. Every counter
adjacent to exactly three neighbors–no more, no fewer–is a
n (𝑇 ) operationalized (e.g. as statistical patterns, human
fully generate the patterns described in (𝑇 )?
ation (seeds, API versions, consideration of proprietary
city, etc.) match the reproducibility goals of the modeler
uirements, etc.)?
or of populations in his sim unpredictable, for the reader
nded to reproduce, his simulation described as a “solitaire”
e understood (e.g., predictive, exploratory, illustrative,
or how the target phenomenon 𝑇 arises from components
r explicit mapping) which connects components of the
sms of (𝑇 )?
ny mechanisms. Mechanisms are defined relative to a
nce 𝐸?
Could 𝐸, in principle, disconfirm the hypotheses in 𝐼?
3 requirement.
fied as a Level 0 Toy model.
pplied to an implementation of Conway’s Game of Life [27].

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
Game Theory LLM Benchmarking Sim
This scale grades the model’s potential as a plausible explanation for the target phenomenon. While not every model’s
goal is to be explanatory, it is important to clarify when it is appropriate.
Level 0: Simulation (𝑆) – Sandbox/Toy Model
□✓ Simulation. Is the simulation (S) defined, including environments, agents, and update rules?
𝑆 includes the codebase for the simulation, which is an implementation of games such as Prisoner’s Dilemma, Texas
Hold’em, Staghunt, etc. played by different LLM Agents against each other.
Level 1: Target Phenomenon (𝑇 ) – Phenomenal Model
□✓ Defined Target Phenomenon. Is a target phenomenon (𝑇 ) operationalized (e.g. as statistical patterns, human
annotations/observations, etc.)?
□✓ Generative Sufficiency. Can the simulation (𝑆) successfully generate the patterns described in (𝑇 )?
□✓ Reproducibility. Does the reproducibility of the simulation (e.g. seeds, API versions, consideration of proprietary
prompt injections or version changes, inherent stochasticity) match the reproducibility goals of the modeler or
the field they are working in (sensitivity analysis requirements, etc.)?
We aim to benchmark the behavior of different LLMs to see if they will solve game-theoretic scenarios, and if they
produce optimal or well-known game-theoretic behavior (e.g., Tit-for-Tat, Nash Equilibrium); their execution of these
strategies we will consider 𝑇 . After running the simulation, we find that models with a larger parameter space tend
to exhibit more aggressive behavior.
Level 2: Intent & Mapping (𝐼) – How-Possibly Model
□ Simulation Contribution. Is the simulation’s use case understood (e.g., predictive, exploratory, illustrative,
explanatory, etc.)?
□ Falsifiable Hypotheses. Does there exist a hypothesis for how the target phenomenon 𝑇 arises from components
in the model?
□ Mechanism Mapping. Is there an Intent 𝐼 (implicit or explicit mapping) which connects components of the
simulation (𝑆) to the hypothesized ‘real-world’ mechanisms of (𝑇 )?
We do not suggest the mechanisms behind why some models play different styles of games than others. However,
our findings do find a correlation between the aggressiveness of players and their parameter count.
Level 3: Evidence (𝐸) – Plausible Model (if validated)
□ Evidence Exists. Is the model supported by some evidence 𝐸?
□ Relevance. Is 𝐸 directed towards the claims made in 𝐼? Could 𝐸, in principle, disconfirm the hypotheses in 𝐼?
Since 𝐸 requires 𝐼, the model does not pass the Level 3 requirement.
Conclusion: Based on the checklist, the model is classified as a Level 1 Phenomenal model.
Fig. 5. Example for Level 1: The Mechanism Plausibility Scale applied to a fabricated game theory paper.

Mechanism Plausibility in Generative Agent-Based Modeling
Example Schelling’s Model of Segregation
This scale grades the model’s potential as a plausible exp
goal is to be explanatory, it is important to clarify when
Level 0: Simulation (𝑆) – Sandbox/Toy Model
□✓ Simulation. Is the simulation (S) defined, including
𝑆 is defined as a grid of agents who move to adjacent em
below a certain threshold (formalized in full paper).
Level 1: Target Phenomenon (𝑇 ) – Phenomenal Mo
□✓ Defined Target Phenomenon. Is a target phenom
annotations/observations, etc.)?
□✓ Generative Sufficiency. Can the simulation (𝑆) suc
□✓ Reproducibility. Is the simulation reproducible?
The target 𝑇 is the emergence of macro-level clustering
generatively sufficient as it always produces segregated
Level 2: Intent & Mapping (𝐼) – How-Possibly Mode
□✓ Simulation Contribution. Is the simulation’s use
explanatory, etc.)?
□✓ Falsifiable Hypotheses. Does there exist a hypothe
in the model?
□✓ Mechanism Mapping. Is there an Intent 𝐼 (implic
simulation (𝑆) to the hypothesized ‘real-world’ mec
Our Intent 𝐼 is to demonstrate the feasibility of the hypo
macro-segregation to occur. Mild preferences for similar
rules map to a simplification of the real-world mechanism
Level 3: Evidence (𝐸) – Plausible Model (if validate
□ Evidence Exists. Is the model supported by some e
□ Relevance. Is 𝐸 directed towards the claims made i
The threshold parameters in our model are abstract and
It proposes a “how-possibly” mechanism.
Conclusion: Based on the checklist, the model is cla
Fig. 6. Example for Level 2: The Mechanism Plausibil

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
tion for the target phenomenon. While not every model’s
s appropriate.
vironments, agents, and update rules?
spots if the percentage of their own color neighbors falls
n (𝑇 ) operationalized (e.g. as statistical patterns, human
fully generate the patterns described in (𝑇 )?
ich represents residential segregation. The simulation is
ghborhoods.
e understood (e.g., predictive, exploratory, illustrative,
or how the target phenomenon 𝑇 arises from components
r explicit mapping) which connects components of the
sms of (𝑇 )?
is that extreme individual prejudice is not necessary for
hbors are a sufficient mechanism. The agents’ movement
residents relocating based on neighborhood composition.
nce 𝐸?
Could 𝐸, in principle, disconfirm the hypotheses in 𝐼?
derived from specific empirical data (e.g. census surveys).
fied as a Level 2 How-Possibly model.
cale applied to Schelling’s Model of Segregation [70]

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
Example Anasazi Model (Epstein et al.)
This scale grades the model’s potential as a plausible explanation for the target phenomenon. While not every model’s
goal is to be explanatory, it is important to clarify when it is appropriate.
Level 0: Simulation (𝑆) – Sandbox/Toy Model
□✓ Simulation. Is the simulation (S) defined, including environments, agents, and update rules?
𝑆 is an agent-based model that simulates the Long House Valley environment using rules for annual agricultural
productivity, and defines agent behaviors based on specific rules for nutritional needs, household size, and reproduction
rates. The details of these parameters, as well as the simulation code, can be found in our GitHub repository.
Level 1: Target Phenomenon (𝑇 ) – Phenomenal Model
□✓ Defined Target Phenomenon. Is a target phenomenon (𝑇 ) operationalized (e.g. as statistical patterns, human
annotations/observations, etc.)?
□✓ Generative Sufficiency. Can the simulation (𝑆) successfully generate the patterns described in (𝑇 )?
□✓ Reproducibility. Is the simulation reproducible?
The target 𝑇 is the historical population dynamics and settlement patterns of the Long House Valley from 800 AD to
1350 AD. The simulation reproduces the population crash and abandonment of the valley.
Level 2: Intent & Mapping (𝐼) – How-Possibly Model
□✓ Simulation Contribution. Is the simulation’s use case understood (e.g., predictive, exploratory, illustrative,
explanatory, etc.)?
□✓ Falsifiable Hypotheses. Does there exist a hypothesis for how 𝑇 arises?
□✓ Mechanism Mapping. Is there an Intent 𝐼 (implicit or explicit mapping) which connects components of the
simulation (𝑆) to the hypothesized ‘real-world’ mechanisms of (𝑇 )?
The intent (𝐼) maps the simulation’s rules (agricultural yield vs. caloric needs) to the real-world mechanisms of the
environmental factors affecting population growth. Therefore it hypothesizes that environmental shifts were the
primary driver.
Level 3: Evidence (𝐸) – Plausible Model (if validated)
□✓ Evidence Exists. Is the model supported by some evidence 𝐸?
□✓ Relevance. Is 𝐸 directed towards the claims made in 𝐼? Could 𝐸, in principle, disconfirm the hypotheses in 𝐼?
The model is constrained by empirical Evidence 𝐸, which includes agricultural productivity reconstructed using
paleoenvironmental data from tree rings, soil analysis, and geology. Each agent’s nutritional needs and household
sizes are derived from anthropological studies of Puebloan peoples.
Conclusion: Based on the checklist, the model is classified as a Level 3 Plausible model.
Fig. 7. Example for Level 3: The Mechanism Plausibility Scale applied to the Artificial Anasazi Model [24]

Mechanism Plausibility in Generative Agent-Based Modeling
B Calibrating the Mechanism Plausibility Scale
This section goes through the process of how we itera
B.1 Calibration
The Mechanism Plausibility Scale was refined through
from a systematic review of LLM-based social simulat
evaluated by two reviewers who assigned scores bef
two rounds of calibration, multiple ambiguities still r
to further rework where we decided it would be mor
format.
B.2 Round 1 Calibration
B.2.1 Paper Selection and Review Process. We tested
from Larooij et al.’s systematic review [45]. We chos
we found that their inclusion criteria was heavily al
requirements that the ABM uses an LLM as the bas
and that the LLMs were seen to be simulating human
LLM-ABM social simulation. A copy of the exact quer
Each paper was reviewed and evaluated by two revie
period, and (2) the reconciliation period. During the
assign it a score before moving onto the next paper. T
the other reviewer until the reconciliation period beg
B.2.2 Inter-Rater Reliability. To assess the reliability
inter-rater reliability using a weighted kappa (𝑘 𝑤) w
mentioned before, the first structured round of apply
it was challenging for even two researchers to apply
guidelines and confusion with the nested nature of th

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
on the scale.
uble-blinded review processes involving papers drawn
s by Larooij et al. [45]. Each paper was independently
entering a reconciliation phase. After going through
ained about how the scale should be applied. This led
propriate to reframe the scale as a practical checklist
y versions of the scale on the first 15 out of 35 papers
evaluate papers from Larooij et al.’s review because
ed with our own research interests. In particular, the
r their agents, there are multiple interacting agents,
havior, were all aligned with our own conceptions of
they used can be found in our Appendix at B.4.
s; their task comprised of two phases: (1) the evaluation
uation period, each reviewer would read a paper and
eviewers were blinded to the scores and sentiments of
the Mechanism Plausibility Scale, we calculated the
quadratic weights, suitable for our ordinal scale. As
the scale to a focused body of literature revealed that
scale consistently; we found ambiguities in the rating
mulations through the reconciliation process.

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
Round 1
Reviewer Scores
Shortened Title A B
Generative Agents [61] 3 1
WarAgent [37] 3 1
Social Simulacra [62] 3 1
S3 [26] 0 1
Scale-Free Networks [54] 3 2
Humanoid Agents [79] 3 2
LyfeAgents [40] 3 0
Collaboration [88] 3 2
AgentVerse [15] 3 0
Epidemic Modeling [84] 3 2
Project Sid [3] 3 1
Theory of Mind [47] 3 1
News Diffusion [48] 0 1
SpeechAgents [87] 1 1
Fake News Propagation [51] 1 1
Table 2. Levels of the Mechanism Plausibility Scale assigned to each paper by Reviewers A and B during the blinded first
round of evaluation, along with its assigned level after unblinding and reconciliation.
B.2.3 Round 1 results of the applied review. The results of the first round are shown in Table 2. Through the
reconciliation process, we found that our scale’s rating guidelines and definitions were too ambiguous to handle
the operationalization gaps discussed in Section 5.1.
Notably, we also found that many papers conflated Agent-level functionality with ABM-level plausibility. A
paper might have provided high-quality experimental evidence for its Agent-level social simulation (the lowest
level in Figure 1), but then they implicitly treated that as sufficient evidence for the claims made about the
emergent social phenomenon (𝑇 ) observed at the ABM-level, which is a category error. Work that shows the
mechanism plausibility of Agent-level phenomena does not necessarily translate to the mechanism plausibility of
ABM-level phenomena. This remains to be shown and must be argued for in the modeler’s Intent, with further
Evidence provided at the ABM-level.
Papers had this problem to varying degrees, but the ones that we flagged particularly were:
• S3 [26], which conflated (the LLM agent’s capacity to simulate the social media posts of an individual, with
matching estimated emotions and attitudes) with (their ABM’s ability to simulate realistic social media
phenomena, like opinion dynamics or information cascades).
• News Diffusion [48], which conflated their (LLM agent’s ability to share news based on personality traits
and friend connections), with their (ABM’s capacity to produce realistic fake news diffusion patterns).
• SpeechAgents [87], which conflated (their LLM agent’s ability to generate text-to-speech outputs, which
was successfully transcribed back into similar text) with (their ABM’s ability to simulate realistic, emergent
human communication dynamics and social interaction patterns at the group level).
• Fake News Propagation [51], which conflated (an LLM agent’s capability to reason about, reflect on, and
share fake news) with (their ABM’s ability to mechanistically explain realistic fake news propagation
dynamics and the emergence of collective opinion patterns).

Mechanism Plausibility in Generative Agent-Based Modeling
The presence of these nested simulations was particu
identify the target phenomenon 𝑇 , and also difficult to
between Agent and ABM phenomena led to a split bet
quadratic weighted kappa score of 0.207.
B.3 Round 2 Calibration
After uncovering the gaps in operationalization (also d
were to assign two scores: one for the ABM-level target
In addition to the clarified scoring guidelines, the sa
increase in reliability may be partially attributable to
As shown in Table 4, the quadratic weighted kapp
Agent ratings reached 0.503. We posit that the score di
from the literature review operationalizing the Agent
the ABM-level. These results are shown in Table 3.
Ro
Shortened Title
Generative Agents [61]
WarAgent [37]
Social Simulacra [62]
S3 [26]
Scale-Free Networks [54]
Humanoid Agents [79]
LyfeAgents [40]
Collaboration [88]
AgentVerse [15]
Epidemic Modeling [84]
Project Sid [3]
Theory of Mind [47]
News Diffusion [48]
SpeechAgents [87]
Fake News Propagation [
Table 3. Levels of the Mechanism Plausibility Scale assign
round of the literature review, along with its assigned level
In the second round of evaluations, we found that o
too broad, allowing for many papers to reach a Level
Difficulties in ignoring a paper’s perceived evidence q
the ABM-level.
B.4 Queries for LLM ABM-related papers
The 15 papers from our applied study are from Larooi

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada
y difficult to evaluate with our scale, as it was difficult to
ntify its operationalization. The ambiguous evaluations
en the reviewer’s perceptions and resulted in an initial
ssed in Section 5.1), in the second round the reviewers
nomena, and one for the Agent-level target phenomena.
reviewers were also used in both rounds. and so the
training received as part of the first round.
r the ABM ratings rose to 0.255, and the score for the
ence between Agent and ABM also comes from papers
el phenomena (implicitly) more in-depth compared to
d 2
Reviewer Scores
ABM Agent
A B R A B R
3 1 3 3 3 3
3 1 3 3 1 3
1 1 1 3 3 3
0 0 0 1 2 1
3 3 3 1 1 1
1 0 1 3 3 3
1 1 1 3 1 3
3 2 3 3 3 3
3 2 3 3 1 3
3 2 3 3 2 3
3 2 3 3 1 3
1 2 2 3 2 3
3 2 3 2 1 2
1 0 1 3 3 3
3 2 3 3 2 3
o each paper by Reviewers A and B in the blinded second
r unblinding and reconciliation.
efinition of the Evidence (as stated in Section 3.4) was
n our scale, regardless of the quality of their Evidence.
ty led to large differences between reviewer scores at
al. [45]:

FAccT ’26, June 25–28, 2026, Montreal, QC, Canada Zhao et al.
Dataset Weighted Kappa (𝑘 𝑤) Interpretation
Round 1 0.207 Fair Agreement
Round 2 (Agent) 0.503 Moderate Agreement
Round 2 (ABM) 0.255 Fair Agreement
Table 4. Summary of weighted kappa (𝑘 𝑤) scores using quadratic weights. The ordinal measure was used because the
plausibility scale has ordered categories. The interpretation comes from Landis and Koch [44].
TITLE-ABS-KEY ( ( "generative social simulation" ) OR ( "generative agent-based
model*" ) OR ( "agent-based simulation" AND "generative AI" ) OR ( "LLM*" AND
"agent-based model*" ) OR ( "large language model*" AND "ABM" ) OR ( "foundation
model*" AND "ABM" ) OR ( "multiagent system*" AND "generative AI" ) OR ( "generative
agent*" ) OR ( "social simulation" AND "LLM*" ) OR ( "large language model-based
agents" ) )
We also used Asta3, an AI research paper search engine built on Semantic Scholar, for paper discovery. Other
LLM-ABM papers were from previous knowledge of the authors or related work.
C Additional Philosophy of Science Background
C.1 Clarification of Model Targets 𝑇
According to a description by Weisberg, 𝑇 does not have to be a particular or ‘real’ phenomenon, and some
models might not even have a 𝑇 ; the target could be particular, generic, or even hypothetical [83]. As an example,
Graebner gives an account of how the target of Schelling’s segregation model [70] is a generalized target, where
it represents an abstract city and its arguments can be applied generically rather than to a particular city [32, 83].
𝑇 can also be hypothetical; for example, Fisher’s three-sex population simulation [25] shows how a population
with three sexes comes with large costs compared to those with only two and is a possible explanation for why
three-sex populations do not exist in reality [32, 82].
3https://asta.allen.ai/chat
