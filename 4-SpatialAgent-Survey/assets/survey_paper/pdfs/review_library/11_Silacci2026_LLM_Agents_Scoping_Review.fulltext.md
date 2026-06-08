Title: Large Language Model–Based Agents for Physical Activity and Cognitive Training: Scoping Review

Source PDF: /Users/mac/Documents/6-Research/4-SpatialAgent-Survey/assets/survey_paper/pdfs/review_library/11_Silacci2026_LLM_Agents_Scoping_Review.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-05-01T02:58:52+00:00
- page_count: 15
- status: ok
- text_char_count: 74962

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Large Language Model–Based Agents for Physical Activity and Cognitive Training: Scoping Review (page 1)
  - Introduction (page 2)
    - Background (page 2)
    - Objectives (page 2)
  - Methods (page 3)
    - Overview (page 3)
    - Search Strategy (page 3)
    - Keywords and Queries (page 3)
    - Study Selection (page 3)
    - Data Extraction (page 3)
    - Data Synthesis (page 3)
    - Ethical Considerations (page 4)
  - Results (page 4)
    - Search and Screening Results (page 4)
    - Domains of Use and Contextual Focus (page 5)
    - Social Roles and Interaction Patterns (page 5)
    - Technological Design and Functional Integration (page 5)
    - Prompting as Design: Framing Roles, Personalization, and Interaction (page 6)
    - Reported Outcomes: Perception, Behaviors, and Evaluation Gaps (page 7)
  - Discussion (page 8)
    - Principal Findings (page 8)
    - Limitations (page 10)
    - Future Works and Research Directions (page 11)
    - Conclusions (page 11)

Markdown Content:

JMIR AI Silacci et al
Review
Large Language Model–Based Agents for Physical Activity
and Cognitive Training: Scoping Review
Alessandro Silacci1,2, BSc, MSc, PhD; Benedetta Giachetti3,4, BSc, MSc; Leonardo Angelini2,3, BSc, MSc, PhD;
Nicola Francesco Lopomo5, MSc, PhD; Giuseppe Andreoni5,6, MSc, PhD; Elena Mugellini3, BSc, MSc, PhD;
Mauro Cherubini1, BA, MA, PhD; Maurizio Caon2, BSc, MSc, PhD
1Department of Information Systems, Faculty of Business and Economics, University of Lausanne, Lausanne, Switzerland
2Digital Business Center, School of Management Fribourg, HES-SO University of Applied Sciences and Arts Western Switzerland, Fribourg,
Switzerland
3HumanTech Institute, School of Engineering and Architecture Fribourg, HES-SO University of Applied Sciences and Arts Western Switzerland,
Fribourg, Switzerland, Fribourg, Switzerland
4Department of Informatics, Faculty of Science and Medicine, University of Fribourg, Fribourg, Switzerland
5Design Department, Politecnico di Milano, Milan, Italy
6Bioengineering Laboratory, Scientific Institute IRCCS E. Medea, Bosisio Parini, Italy
Corresponding Author:
Alessandro Silacci, BSc, MSc, PhD
Department of Information Systems
Faculty of Business and Economics, University of Lausanne
Quartier Centre
Lausanne 1015
Switzerland
Phone: 41 21 692 11 11
Email: alessandro.silacci@unil.ch
Abstract
Background: Large language model (LLM)–based conversational agents have been increasingly used in digital health
interventions. However, their specific application to physical activity (PA) and cognitive training—two critical well-being
domains—has not been systematically mapped. In fact, these domains share an important need for personalized, adaptive
support and conversational engagement, making them relevant targets for examining how LLM-based agents are currently
conceptualized and deployed.
Objective: This scoping review aimed to map the extent, characteristics, and design practices of LLM-based conversational
agents supporting PA or cognitive training, specifically analyzing their application contexts, social roles, and technological
features.
Methods: Following PRISMA-ScR (Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for
Scoping Reviews) guidelines, we searched Web of Science, Scopus, PubMed, ACM Digital Library, and IEEE Xplore
for studies published between January 2018 and December 2024. We included eligible studies that described LLM-based
conversational agents designed for PA or cognitive training. Two reviewers independently screened records and extracted
data. Descriptive synthesis and framework analysis were used to characterize intervention domains, agent roles, prompting
strategies, model types, and reported outcomes.
Results: Of 357 records screened, 10 studies met eligibility criteria (7 on PA and 3 on cognitive training). Applications
predominantly involved coaching roles for PA and companion or scaffolding roles in cognitive domains. The agent landscape
was dominated by proprietary LLMs (GPT-3.5, GPT-4, and Bard), with limited use of open-weight models. Prompt engineer-
ing emerged as a central yet inconsistently documented design mechanism. Reported outcomes mainly focused on perceived
usefulness, engagement, or content quality, with few quantitative behavioral outcomes.
Conclusions: LLM-based conversational agents have demonstrated early promise for supporting PA and emerging approaches
to cognitive training, yet the current evidence remains exploratory and methodologically limited. Key challenges persist,
including inconsistent reporting of prompts, reliance on proprietary models with limited reproducibility, and a lack of
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 1
(page number not for citation purposes)

JMIR AI Silacci et al
standardized outcome measures. More rigorous and transparently documented evaluations of these tools are required to
strengthen the evidence base and guide future development.
JMIR AI 2026;5:e80123; doi: 10.2196/80123
Keywords: cognitive training; conversational agents; large language models; physical activity; prompt engineering; reproduci-
bility; scoping review
Introduction adaptive tone, and flexible role construction. However,
current reviews do not account for the distinctive capabili-
Background ties, challenges, and design considerations introduced by this
new class of models. As LLMs continue to gain traction in
Conversational agents (CAs) have been increasingly both academic and commercial health technologies, a timely
integrated into digital health interventions, offering scala- synthesis is needed to chart the emerging landscape, identify
ble and personalized support for health-related behavioral key design patterns, and highlight open research questions.
change [1]. Within intervention domains such as physical
Despite being distinct domains, PA and cognitive training
activity (PA) promotion and cognitive health, CAs have
are frequently integrated and combined in the litera-
reported promising results in fostering user engagement,
ture, particularly within interactive and digitally mediated
supporting self-regulation, and enhancing adherence. These
interventions [23]. Indeed, PA produces well-established
agents often mimic human dialogue to educate [2], prompt
cognitive and neurobiological effects [24]. Moreover,
reflection [3], or guide users toward their behavior goals [4].
combined physical-cognitive training has been shown to yield
However, earlier conversational systems—particularly those
synergistic benefits compared to single-domain approaches,
based on prescripted or narrowly scoped interaction models—
although it remains subject to common challenges related
often failed to support the flexible, conversational interaction
to engagement, adherence, and intervention design. Recent
users expected, instead requiring command-like and highly
interactive and exergame-based systems further demonstrate
constrained input that many users experienced as frustrating
that physical and cognitive components are deeply inter-
or unnatural [5].
twined in user interaction and system design, rather than
The recent emergence of large language models (LLMs), implemented as isolated modalities [25]. Accordingly, this
such as OpenAI’s ChatGPT, introduces a fundamental shift in review considers both domains to examine how LLM-based
how CAs can be developed and deployed [6]. In fact, LLMs CAs are designed and evaluated in well-being interventions.
offer open-ended dialogue capabilities, context-sensitive The focus is on their shared interactional, motivational,
responses, and general-purpose reasoning [7-9]—qualities and personalization mechanisms, rather than on comparing
that may greatly enhance the reach and efficacy of behav- clinical outcomes across domains.
ioral interventions. Early research suggests that LLM-pow-
This review addresses that gap by systematically map-
ered agents can emulate counseling techniques, adapt their
ping how LLM-based CAs are conceptualized, applied,
tone and content dynamically, and even facilitate therapeutic
and evaluated in interventions addressing PA and cognitive
alliance-like interactions [10]. These affordances align with
training. Our contribution is 2-fold. First, we characterize the
long-standing human-computer interaction (HCI) priorities,
state of the art in this fast-moving field, including system
particularly the call for emotionally intelligent, adaptive,
features, use contexts, and intended outcomes. Second, and
and personalized systems to support human well-being [11].
more critically, we move beyond summary to dissect how
As such, LLM-based CAs are especially relevant in health
these systems are built and the scientific challenges this
domains where motivation, personalization, and sustained
creates. We specifically analyze the practice of prompt
engagement are critical.
engineering as an informal yet central design mechanism.
Despite the promise of LLMs, there is currently a lack of Furthermore, we highlight how the prevalent use of propriet-
systematic understanding of how LLM-based CAs are being ary “black box” models and inconsistent documentation pose
used, or could be used, in the context of PA and cogni- a fundamental threat to reproducibility, hindering the field’s
tive interventions. Existing literature reviews have examined cumulative scientific progress. By surfacing these methodo-
artificial intelligence (AI)–powered CAs across domains, logical risks, we provide a necessary critical perspective
such as PA [12,13], obesity treatment [14-17], and men- that complements and advances prior work on digital health
tal health [18]. These studies highlighted several recur- agents.
ring limitations, including conversational rigidity, shallow Objectives
personalization, limited contextual awareness, and repetitive
or unnatural dialogue patterns [1,19]. Such shortcomings can This scoping review explores the role of LLM-based CAs in
hinder user engagement and learning effectiveness, particu- supporting individuals’ PA and cognitive training, providing
larly in interventions that rely on sustained motivation and a comprehensive overview and critical evaluation of their
adaptive feedback, as is the case for both PA coaching impact. Specifically, it examines how these AI-driven agents
and cognitive training systems [20-22]. These weaknesses facilitate engagement, personalize interactions, and address
highlight a critical design gap that LLMs are poised to challenges in interventions aimed at enhancing both physical
address, thanks to their capacity for open-ended interaction, and cognitive well-being.
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 2
(page number not for citation purposes)

JMIR AI Silacci et al
To structure this analysis, we investigated 3 key research • Query 1: (K1 keywords) AND (K2 keywords) AND (K3
questions (RQs), focusing on their applications, social keywords)
dynamics, and integration with complementary technologies: • Query 2: (K1 keywords) AND (K2 keywords) AND (K4
• RQ1. In what ways have LLM-based CAs been applied keywords)
to support well-being, particularly in the contexts of PA
This structure was adapted to the specific syntax requirements
and cognitive training?
of WoS and Elsevier Scopus.
• RQ2. How does existing literature characterize the
Study Selection
social roles of LLM-based CAs in PA and cognitive
training interventions?
Inclusion criteria were established and adapted from previous
• RQ3. What additional technologies or design features
research on CAs for well-being [31]. Results from query 1
are integrated with LLM-based CAs to enhance their
and query 2 were uploaded to the Covidence [32] platform,
effectiveness in PA and cognitive training interven-
where all authors were invited to participate in the review
tions?
process.
Methods The first selection phase assessed studies based on their
title, abstract, and keywords, applying all inclusion and
exclusion criteria except full-text availability and, in some
Overview
instances, language. Following an initial pilot screening round
(14 papers of which 5 were selected and 9 were irrelevant,
This scoping review analyzes the landscape of LLM-based
~36% eligible, details available as supplementary materials
CAs for PA and cognitive training, following the PRISMA-
[27]), the inclusion and exclusion criteria were refined to
ScR (Preferred Reporting Items for Systematic Reviews and
improve clarity and consistency among reviewers. During
Meta-Analyses extension for Scoping Reviews) guidelines
the full-text screening phase, the complete set of eligibility
(Checklist 1) [26] to enhance the transparency and complete-
criteria was applied (cf, Supplementary Material [27]). In
ness of reporting.
both phases, each study was independently evaluated by at
Search Strategy
least two reviewers. In cases of disagreement, a third reviewer
was consulted, and discussions were held when necessary to
To identify relevant studies, keywords related to CAs, PA,
reach consensus.
cognition, and well-being were derived from a preliminary
Data Extraction
literature overview [27]. In parallel, LLM-specific keywords
were selected based on prior LLM reviews and the authors’
Key study characteristics were extracted, including biblio-
domain expertise. Searches were primarily performed using
graphic details (title, authors, year, outlet or conference),
combinations of these keyword groups (K1, K2, K3, ... Kn)
study type, and specific information outlined in the data
across Clarivate Web of Science (WoS) and Elsevier Scopus,
collection protocol available through our FAIR repository
2 databases recognized for their comprehensive coverage
[27]. These included the study aim, LLM model and
of peer-reviewed academic research [28,29]. To ensure
access modality, fine-tuning approach, characteristics of
comprehensive coverage, we further included PubMed, ACM
the CAs (name, form, role, purpose, and design), deploy-
Digital Library, and IEEE Xplore in our search based on their
ment context, interactional structure, software used, type of
frequent use in prior literature reviews [27].
physical or cognitive activity, and prompt features. All data
Keywords and Queries were independently reviewed by 2 authors. Discrepancies
were resolved through discussion to ensure consistency and
Keywords were collected based on other literature reviews’
accuracy.
requests involving agents used in PA and cognitive training.
Data Synthesis
Queries included papers from January 2018 to December
2024, as this marks the introduction of Bidirectional Encoder
To synthesize the collected data, we used both descriptive
Representations from Transformers, the first language model
and qualitative approaches. Descriptive statistics were used
to enable bidirectional language understanding, a founda-
to summarize key study characteristics, including publica-
tional feature for LLMs [30].
tion year, country of study, study type and design, interac-
For full transparency and reproducibility, the complete and tion modalities, and targeted domains (eg, PA and cognitive
exact search query strings used for each database are openly training). These metrics provided insights into the distribution
accessible in a findable, accessible, interoperable, reusable and focus areas of existing research involving LLM-based
(FAIR)–compliant repository [27]. As an example of our CAs in the context of PA and cognitive training.
search structure, we used two main queries: one combining
We used a framework analysis to synthesize findings
keywords from group K1 (agents), group K2 (technology),
from the included studies [33]. Two authors systematically
and group K3 (physical activity); and a second combining
extracted and charted textual data related to the design, use,
keywords from group K1 (agents), group K2 (technology),
and evaluation of the interventions. This charting focused on
and group K4 (cognition), all using Boolean operators. A
key domains, including the specific prompts used to guide the
simplified representation of the search logic for these two
CAs and the types of outcomes measured (both qualitative
distinct queries was as follows:
and quantitative). This systematic approach allowed us to
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 3
(page number not for citation purposes)

JMIR AI Silacci et al
identify recurring patterns and emerging themes within the 105 (12.6%) from PubMed, 22 (2.64%) from IEEE Xplore,
evidence base. and 8 (0.96%) from ACM DL. After removing 476 (57.14%)
duplicates using Covidence, 357 (42.86%) records remained
All conflicts or uncertainties in data interpretation were
for title and abstract screening. Of these, 330 (92.44%)
resolved collaboratively between at least two reviewers.
were excluded based on the inclusion criteria. The remain-
Ethical Considerations ing 27 (7.56%) full-text articles were assessed for eligibil-
ity, resulting in the exclusion of 17 (62.96%) studies due
To ensure the utmost transparency and facilitate reproducibil-
to reasons such as being out of scope (n=9, 52.94%),
ity, key research artifacts, specifically the full database search
wrong study design (n=3, 17.64%), or irrelevant outcomes,
queries, the raw and consolidated data extraction datasets, and
interventions, or indications. Ultimately, 10 (37.04%) studies
the R Markdown notebook used for quantitative analysis, as
met all eligibility criteria and were included in the final
well as our framework analysis results have been publicly
review (Figure 1). The dataset resulting from our analysis
archived, adhering to the FAIR principles and recommenda-
is available as supplementary material through our FAIR
tions provided by Niksirat et al [34]. The same supplementary
repository [27].
material content is also available in the Multimedia Appendix
1.
Results
Search and Screening Results
The initial database search yielded 833 records, with 386
(46.34%) from Scopus, 312 (37.45%) from Web of Science,
Figure 1. The PRISMA (Preferred Reporting Items for Systematic reviews and Meta-Analyses) flowchart, provided by Covidence, with the search
and the selection process of the studies included in our review. ACM: Association for Computing Machinery; IEEE: Institute of Electrical and
Electronics Engineers.
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 4
(page number not for citation purposes)

JMIR AI Silacci et al
Domains of Use and Contextual Focus reflecting a pragmatic emphasis on system development and
usability testing over theoretical modeling. However, only a
The 10 included studies explored a range of well-being
few studies offered robust outcome measures.
applications, with a strong emphasis on PA (n=7; [35-41]),
and fewer focusing on cognitive training (n=3; [42-44]). These findings comprehensively address RQ1 by
These interventions aimed to support behaviors such as illustrating the primary domains (PA and cognitive train-
exercise adherence, task planning, reminiscence, and memory ing) and specific intervention goals (eg, exercise adherence,
stimulation. Most were delivered via web platforms (n=7; memory stimulation) where LLM-based CAs are currently
[35-39,42,43]), followed by mobile apps (n=2; [40,43]), being applied.
messaging platforms (n=1; [41]), or robotic embodiments Social Roles and Interaction Patterns
(n=1; [44]).
LLM-based CAs were designed with varied social roles,
Several studies designed agents that adapted their
which ranged in both functionality and relational framing.
responses to user input, preferences, or contexts— such
The most common role was that of a personal coach [35-
as tailoring memory prompts, adjusting training plans, or
37,41], emphasizing directive and motivational engagement.
offering reminders. In cognitive domains, agents facilita-
Other roles included companions [43,44], assistants [40,44],
ted engagement by drawing on familiar content (eg, book
counselors [38], experts [42], and recommender systems [39]
discussions, life stories), whereas in PA, personalization was
(Table 1).
often linked to goal tracking or motivation cues.
Most studies followed an empirical (n=7; [35,37-39,41-
43]) or design-oriented (n=3; [36,40,44]) methodology,
Table 1. The distribution of the roles that were attributed to the large language model–based conversational agents in the reviewed studies,
demonstrating that these conversational agents were predominantly being used as coaches [35-37,41] but also involved as companions [43,44] and
other more specific roles such as assistants [40,44], counselor [38], expert [42], and recommender systems [39].
Role Reviewed articles
Personal coach [35-37,41]
Companion [43,44]
Scaffolding expert [42]
Recommender system [39]
Patient counselor [38]
Digital assistant [40,44]
Medical assistant [44]
Despite this diversity, dialogue patterns remained limited: Technological Design and Functional
most systems were user initiated (n=5; [35,36,41-43]), with Integration
only [44] and [40] supporting shared initiative. Communi-
cation was primarily text-based [35-38,42,43], although 4 Technological integration centered around popular LLMs
studies implemented voice interaction [40,42-44]. (Table 2), such as GPT-4.0 (n=5; [36,37,40,43]) and GPT-3.5
(n=4; [35,36,39,42]), with occasional use of alternatives such
Another consistent pattern across all studies was the use
as Google Bard [35,40], Mistral [35], and Llama [35,43].
of dyadic interaction models; indeed, the CA was always
These models were most commonly accessed via web-based
designed to interact with a single user at a time. No studies
interfaces, with several studies directly using web clients such
explored group dynamics, multiuser interfaces, or collabora-
as ChatGPT’s web platform [45], and some others integra-
tive scenarios involving multiple stakeholders. This highlights
ted the models into mobile applications. A smaller subset
a current boundary in the design space, where LLM-based
of studies incorporated multimodal features, such as voice
CAs are predominantly framed as personalized, one-to-one
interaction, embodied agents (eg, the EVA robot [46]), or
agents rather than social actors embedded in broader systems
context-aware elements such as memory recall cues, directly
or communities.
detailing the additional technologies and design features
specified in RQ3.
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 5
(page number not for citation purposes)

JMIR AI Silacci et al
Table 2. A reporting of the different large language models used in the reviewed studies with a main use of GPT-4.0 (n=5; [36,37,40,41,43]),
GPT-3.5 (n=4; [35,36,38,39]), and Google Bard [35,40] for the closed-source models, in addition to the mention of open-weight models, such as
Mistral [43] and Llama [35,43].
Developer, model, and variant Reviewed articles
OpenAI
ChatGPT
GPT-3.5 [35,36,38,39]
GPT-3.5-turbo [42]
GPT-4.0 [36,37,40,41,43]
NA [44]
Whisper [44]
Google
Bard
NA [35,40]
Meta
Llama
2 [35]
2-13B [43]
Mistral.ai
Mistral
7B [43]
A cross-cutting category was related to the use of engagement feasibility, few provided behavioral or cognitive metrics tied
and motivation strategies, including adaptive scaffolding, to intervention efficacy.
goal reminders, or user-personalized prompts. While some
Prompting as Design: Framing Roles,
studies integrated these intentionally, others relied on the
Personalization, and Interaction
natural language capabilities of LLMs to simulate engage-
ment (eg, responding conversationally or using humor). Only
In addition to model selection and platform deployment, the
a subset of studies reported evaluating these engagement-rela-
reviewed studies revealed a critical design layer in the form
ted elements in a structured way, while others did not include
of prompt engineering—that is, the crafting of textual inputs
specific assessments of these components.
that guide the behavior, tone, and identity of LLM-based
Finally, many studies highlighted technical or operational CAs. Although rarely emphasized as a formal methodology,
challenges. These included LLM response delays, platform prompt design emerged as a powerful mechanism through
limitations, and concerns over content appropriateness or which researchers shaped the agent’s functional logic, social
factuality. Several studies used semiautomated systems due role, and interpersonal dynamics. The resulting framework
to constraints in LLM access or stability. Moreover, the analysis of the prompt strategies observed across the included
lack of standardized outcome measures was a consistent studies highlights 4 key patterns in how prompts were used to
limitation: although most studies reported user satisfaction or construct agent behavior and interaction style (Table 3).
Table 3. A summary of the different categories that emerged when analyzing the provided prompts in the reviewed studies (7 papers provided
prompts out of the 10 analyzed).
Category Studies
Instructional and informational requests [36,37,39,42,44]
Role-based identity assignment [42-44]
Scenario-based personalization [36,42-44]
Task-oriented dialogue support [42,44]
Across the studies, prompts were not generic queries Prompting also played a decisive role in constructing the
but scripted scenarios or instructions that encoded interac- social identity of the agent. Multiple studies used explicit
tional intent. In many cases, this took the form of sce- role-based instructions, instructing the LLM: “You are a book
nario-based personalization. For instance, Favela et al [44] club host,” “You are a healthcare assistant,” or “You are a
framed interactions within dementia care routines, embedding caregiver.” These role assignments acted as social anchors,
the agent in emotionally significant and context-sensitive shaping how the CA would behave—more directive as a
dialogue. coach [36], more empathetic as a companion [44], or more
informative as a recommender system [39]. These framing
devices reflect a broader reliance on prompting to simulate
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 6
(page number not for citation purposes)

JMIR AI Silacci et al
relational presence, particularly in the absence of embodied or exercise: the LLM was given a user profile and asked to infer
affective sensing. likely future decisions from that perspective.
In terms of functionality, prompts often scaffolded Taken together, the analysis of prompt strategies highlights
task-oriented dialogues. For example, Hu et al [42] embed- that prompting is not just a technical necessity but a cen-
ded conditional logic into its prompt to simulate a grocery tral design practice. Whether used to construct social roles,
shopping task for cognitive assessment. Rather than scripting personalize content, or manage conversation flow, prompts
full interaction flows, these designs leveraged the LLM’s serve as the invisible scaffolding behind agent behavior. Yet,
interpretive flexibility, using natural language to create few studies evaluated or iterated on prompt effectiveness,
interactive, multistep tasks without formal programming and suggesting a need for more systematic approaches to prompt
prompting thus served as a low-code interface for designing design and testing in future work.
agent behavior.
The analysis of prompt strategies highlights that prompting
Some prompts explicitly addressed affective tone and is not just a technical necessity but a central design prac-
ethical conduct. Favela et al [44] instructed the CA not to tice. Whether used to construct social roles (RQ2), personal-
“talk like a child” when interacting with older adults and to ize content, or manage conversation flow (both enhancing
remain “patient and respectful.” Such affect-aware framing effectiveness, RQ3), prompts serve as the invisible scaffold-
suggests a growing awareness that prompts are not only ing behind agent behavior.
functional but also relational instruments, capable of shaping
Reported Outcomes: Perception,
the user’s emotional experience.
Behaviors, and Evaluation Gaps
Importantly, all studies used LLMs in dyadic contexts,
with prompts structured for one-on-one interaction. No study The included studies reported a range of qualitative and
designed prompts to support group conversation, multiuser quantitative outcomes, offering insights into both user
turn-taking, or collective memory tasks. This reflects a experience and the effectiveness of LLM-based CAs. A
current boundary in the field: despite LLMs’ flexible dialogue framework analysis of these outcomes revealed five dominant
capabilities, they are still being operationalized primarily as categories: perceived usefulness, user engagement, content
personalized single-user agents. quality, behavioral impact, and a notable lack of quantitative
evaluation. These categories illustrate how CAs are currently
Of the 10 reviewed studies, 3 did not provide the prompts
being evaluated and highlight where the evidence remains
in the text or the supplementary materials. One additional
limited or anecdotal (Table 4).
study [35] did not use prompting to shape the agent’s
behavior as a CA but instead framed the task as a reasoning
Table 4. A summary of the different categories that emerged from the outcomes’ analysis in the reviewed papers.
Category Studies
Behavioral impact [35,41]
Content quality [37-39]
Perceived usefulness [36,42]
User engagement [41,42,44]
Lack of quantitative evaluation [36,37,39,40,43]
Perceived usefulness was a recurring category in the reviewed and significant weaknesses. On the positive side, Washif et
papers. For instance, participants in the study by Hu et al [42] al [36] found that an agent’s exercise recommendations were
described the agent as helpful and easy to use, indicating a consistent with standard plans. Bak and Chin [35] reported
positive perception of its utility in their tasks. that LLMs could generate more stage-appropriate health
information when provided with user profiles that included
Similarly, user engagement was frequently reported as
clear goals. However, the same study noted limitations in
a key outcome. Several studies used interaction metrics
the recommendations for users in certain stages of behavior
as a proxy for engagement; Favela et al [44] noted that
change. Some studies reported several limitations related to
users sustained conversations lasting for over 10 minutes,
the accuracy, reliability, or personalization of the agents’
suggesting a naturalistic and engaging interaction. Hu et al
responses. Pugliese et al [38], for example, found that while
[42] documented consistent use of specific features, such as
responses were understandable, not all information provided
recommendations, while Sun et al [41] found that exposure
was reliable or sufficiently personalized.
to the agent was a significant predictor of engagement. The
latter study also identified specific design elements, such as A smaller subset of studies attempted to measure
humor, as potential enhancers of engagement, although their behavioral impact, although often with preliminary or indirect
direct motivational impact was not conclusively determined. indicators. Bak and Chin [35] evaluated the potential for
LLMs to address different stages of the transtheoretical
The content quality of the agent’s output emerged as a
model, highlighting that the models tended to favor certain
dual-focused category, with studies reporting both strengths
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 7
(page number not for citation purposes)

JMIR AI Silacci et al
strategies over others without providing clear reasons. While These findings highlight an underexplored opportunity
not finding significant changes in motivation, Sun et al [41] to use LLM-based agents for more structured cognitive
did demonstrate that the inclusion of humor had a measura- support. Future work should explore how these systems
ble effect on participants’ PA, pointing to a potential, albeit can be embedded in adaptive frameworks that respond to
subtle, behavioral influence. longitudinal user behavior, particularly in contexts such
as memory training or executive function support. Addi-
Finally, a critical finding was the widespread lack
tionally, the absence of evidence-based cognitive training
of quantitative evaluation. While a few studies reported
protocols underscores the need for interdisciplinary collab-
quantitative metrics such as conversation time [44] or feature
oration between HCI, cognitive neuroscience, and clinical
usage [42], these were the exception. Many papers explic-
design.
itly acknowledged that their evaluation was exploratory or
provided no quantitative data at all [36,37,39,40,43]. Our review shows that LLM-based CAs predominantly
rely on prompt-engineered instructions to instantiate social
Overall, the limited application of standardized outcome
roles such as “coach,” “companion,” or “caregiver.” This
measures suggests that the current evidence base remains
design choice enables rapid prototyping; however, it also
preliminary. While studies frequently reported positive user
exposes a deeper structural limitation. Indeed, LLMs do
perceptions, few included validated behavioral or cognitive
not maintain stable personas across extended interactions
assessments to substantiate claims of effectiveness. This
[48,49]. Recent empirical work demonstrates that persona
constrains the ability to draw firm conclusions regarding both
adherence degrades during multiturn dialogue, with models
the impact of these systems (RQ1) and the design choices that
gradually drifting away from assigned psychological profiles
shape their performance (RQ3).
or communicative styles. Bhandari et al [49] show that LLMs
frequently lose alignment with Big Five trait configurations
Discussion
over the course of dyadic conversations, even when such
traits are explicitly embedded at initialization, highlighting
Principal Findings inconsistencies in sustained personality expression. Similar
instability has been documented in emotional support settings,
This scoping review examined how LLM-based CAs have
where personas influence strategy use but undergo measura-
been applied to support well-being, with a focus on PA
ble shifts in emotionality and extraversion as conversations
and cognitive training. Through framework analysis, prompt
unfold [50]. Once a user diverges from the scripted inter-
categorization, and evaluation of reported outcomes, we
action, the role coherence can collapse, exposing the user
identified patterns in how these systems are designed,
to potential agent hallucinations [51]. This observation is
deployed, and assessed. In the following sections, we
consistent with findings in the LLM literature showing that
interpret the findings across three key areas: application
persona conditioning degrades over time without architectural
contexts, role construction, and design and evaluation
support (eg, memory, state tracking) [52].
strategies.
This fragility aligns with theoretical perspectives on
First, in terms of application contexts, our results show
role-play in LLMs, which conceptualize dialogue agents
that LLM-based CAs are primarily deployed in interventions
as enacting simulacra that lack internal persistence. Shana-
related to PA, where they function as digital coaches offering
han et al [53] argue that LLMs “role-play” characters by
motivational prompts, personalized planning, and behavio-
following statistical patterns rather than maintaining grounded
ral reinforcement [35,36]. These roles align with traditional
identities; consequently, persona continuity is inherently
coaching models that emphasize goal setting, encourage-
brittle in the absence of architectural mechanisms such as
ment, and self-monitoring [47]. In contrast, cognitive training
memory or state tracking. Our findings similarly reflect
applications remain limited and exploratory. The 2 studies in
that current well-being–oriented CAs rarely incorporate such
this domain focused on reminiscence [44] and task scaffold-
mechanisms, relying instead on static instructions that do not
ing [42] rather than delivering structured cognitive exercises
support evolving or contextually reinforced identities.
grounded in validated protocols.
Furthermore, research in HCI and communication science
This pattern suggests that PA interventions may present
indicates that personas—especially when used to guide social
a more immediate design fit for LLM-based agents, partic-
interaction—impact user perception, engagement, and trust.
ularly because motivational dialogue can be framed using
Controlled experiments with embodied LLM agents show that
general-purpose language generation without requiring deep
manipulating personality traits (eg, introversion vs extra-
domain modeling, thereby furthering our understanding of
version) significantly affects social evaluations, emotional
RQ1. Conversely, cognitive interventions—especially those
experience, and behavioral engagement [54]. However, these
targeting impairments—require higher precision, domain
effects depend on the consistency and credibility of the
knowledge, and ethical sensitivity, which current prompt-
persona. Complementary evidence reveals that AI-generated
based implementations may struggle to provide. Moreover,
personas often appear stereotypical or insufficiently nuanced
most applications in both domains rely on static personali-
compared to human-crafted ones, raising concerns about
zation, often configured during initial sessions, rather than
whether LLM personas authentically capture user diversity
dynamically adapting to user behavior or outcomes over time.
or complexity [55]. Similarly, work on demographic persona
prompting demonstrates that LLMs may reflect demographic
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 8
(page number not for citation purposes)

JMIR AI Silacci et al
biases or fail to accurately maintain demographic-specific frequently lack theoretical grounding or validation against
viewpoints unless tightly constrained [48]. established constructs.
This lack of continuity is critical because it undermines This lack of formalization extends directly to evaluation
the conditions under which users treat agents as social practices. Few studies attempted to link agent interaction
actors. Nass and Moon [56] demonstrated that humans apply with behavioral or cognitive outcomes, and fewer still used
social norms to computer agents when those agents main- validated instruments. Overall, the variability and limited
tain a coherent identity and consistent interpersonal behav- rigor of outcome measures across studies suggest that much
ior—qualities that foster deeper engagement and trust. These of the current work remains at a proof-of-concept level,
effects rely on interactional consistency and memory to with an emphasis on feasibility and system development
simulate “mindfulness” and sustained social presence, both rather than validated behavioral or cognitive outcomes. These
of which are often absent in current LLM-based implementa- observations are consistent with findings from Shool et al
tions. This challenge was also highlighted by Pataranutaporn [63], who reviewed more than 700 LLM studies in clinical
et al [57], who note that although AI-generated characters can medicine and found that most relied on ad hoc performance
simulate highly personalized roles (eg, mentor and therapist), indicators—such as accuracy or readability—while neglect-
their relational integrity is fragile unless backed by memory ing more robust, psychometrically validated tools. These
systems and contextual continuity mechanisms. observations echo broader concerns in recent LLM evalua-
tion scholarship regarding the limitations of current bench-
Taken together, these insights suggest that prompt-based
marks and metrics, which insufficiently capture meaningful,
social role construction is brittle and insufficient for sustained
real-world performance or safety [58].
engagement. To address this, future systems should incor-
porate persistent memory mechanisms, state awareness, or These combined observations on design and evalua-
hybrid logic layers to reinforce social cues across interactions. tion raise important concerns about the current maturity
Moreover, there is a clear need for empirical evaluation of of LLM-based CA research in well-being domains. To
persona coherence—an area that remains largely untested strengthen the evidentiary base, future work should adopt
despite its centrality to trust, compliance, and user satisfaction mixed methods designs with validated outcome measures and
in relational agents. comparative baselines. Furthermore, prompt design artifacts,
agent configurations, and transcripts should be published
The third major theme emerging from our findings
or shared where possible to support reproducibility and
concerns the profound challenge that current design practices
transparency in this rapidly evolving design space.
pose to scientific rigor. LLM-based CAs reflect a tension
between design flexibility and methodological fragmenta- Finally, beyond the challenges of prompt transparency,
tion. On the one hand, the ability to craft prompts as low- a deeper impediment to reproducibility in LLM-based
code design primitives allows for rapid customization and interventions lies in the widespread reliance on propriet-
iterative prototyping. Developers can create context-sensitive ary, continuously updated models. These systems—such as
interactions by embedding goals, roles, and emotional cues OpenAI’s GPT series and Google’s Gemini—are fundamen-
directly into natural language instructions. However, as recent tally nontransparent black boxes, a characteristic repeatedly
work has shown, this flexibility often comes at the cost of highlighted in the literature as a central obstacle to account-
consistency, transparency, and evaluative rigor. Large-scale ability and scientific verification. Existing literature emphasi-
methodological reviews increasingly describe LLM research zes that LLMs’ internal mechanisms remain opaque even to
ecosystems as fragmented and underspecified, noting that the expert users, complicating efforts to understand or trace how
lack of shared standards for documenting prompts, configura- outputs are generated (eg, their “algorithmic opacity”) and
tions, and evaluation pipelines produces substantial barriers to limiting the ability to contest or replicate results [64,65].
comparability and scientific accumulation [58,59].
A critical consequence of this opacity is model drift.
For instance, Hanauer et al [60] found that a large Indeed, proprietary LLMs are routinely updated without
proportion of LLM-driven clinical studies failed to report version-locking or archival access, meaning that the same
basic implementation details, such as model version, prompt issued weeks or months apart may yield measurably
parameter settings, or the timing of usage—critical factors different outputs. Such evolving behavior has been noted
that undermine reproducibility. Similarly, Zamfirescu-Pereira as incompatible with basic scientific principles of repeatabil-
et al [61] demonstrate that non-AI experts often struggle ity and falsifiability, as researchers cannot access, “freeze,”
to design effective prompts and rarely document prompt or independently inspect prior states of the model used in
rationale, iterations, or failures. These studies highlight their studies [66]. This challenge is distinct from issues of
that while prompt engineering lowers technical barriers, explainability; even perfect prompt documentation cannot
it introduces new challenges related to reproducibility, compensate for the fact that the underlying computational
replicability, and responsible design practice. Prompt design pathway is inaccessible and mutable.
is rarely subjected to empirical testing, and its impact
The inability to audit or update underlying training data
on system behavior is often undocumented or informally
compounds this problem. While transparency frameworks
evaluated—a concern echoed in psychological research,
increasingly stress the importance of auditability (ie, the
where Demszky et al [62] warn that LLM-based interventions
ability to identify what data or processes contributed to
an output), current proprietary LLMs rarely enable such
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 9
(page number not for citation purposes)

JMIR AI Silacci et al
inspection, creating structural barriers to verifying results studies or particular application contexts might not have been
or correcting errors [66]. Scholars further warn that focus- explored in exhaustive detail.
ing solely on explainability can obscure the more press-
Our search strategy, while comprehensive within its
ing practical issue: users lack sufficient clarity about how
defined parameters, was subject to certain constraints.
these systems operate and what their limitations are, further
Searches were limited to WoS and Elsevier Scopus; thus,
undermining reproducibility across contexts [67].
relevant studies published in other databases, gray literature,
Given these constraints, researchers using proprietary or conference proceedings not indexed in these sources might
LLMs should explicitly acknowledge the inherent limitations have been missed. The effectiveness of our search was
to reproducibility and document, at minimum, the date range also dependent on the chosen keyword combinations (K1,
of model access, application programming interface version K2, K3, and K4); although these were developed through
information (if any), and all implementation details that can preliminary scans and expert consultation, it is possible
feasibly be reported. Although such documentation cannot that alternative terminology or emerging concepts related to
fully compensate for the absence of model version stabil- LLM-based CAs, PA, or cognitive training were not fully
ity, it substantially improves transparency and allows future captured. Furthermore, our review was restricted to articles
researchers to contextualize observed outputs within the published in English, potentially excluding pertinent research
dynamic evolution of the model. published in other languages. While justified by the emer-
gence of LLMs, the time frame restriction to publications
In addition to transparency constraints, reproducibility
between January 2018 and December 2024 means that earlier
poses an even more fundamental challenge for LLM-based
foundational work or very recent developments (post-2024)
research. Recent evaluations across clinical and informa-
were not included. Finally, despite a comprehensive search,
tion-retrieval domains reveal that proprietary LLMs exhibit
the small sample size of only 10 studies meeting our stringent
intrinsic output instability: even when prompts, inputs, and
eligibility criteria reflects the nascent stage of research in
contexts are held constant, model responses vary in ways
these specific domains, inherently limiting the generalizabil-
that cannot be fully controlled or accounted for by research-
ity and robustness of our findings.
ers [68,69]. This instability reflects not simply stochastic
sampling, but deeper properties of opaque, continuously Our analysis was based solely on the information reported
optimized systems whose internal states and inference in the full-text articles, which means that insufficient
pathways are inaccessible. As a result, reproducibility failures reporting in original studies could lead to incomplete data
arise even before model drift is considered, compounding extraction or synthesis. Additionally, while our framework
the challenge introduced by unannounced backend updates. analysis of qualitative data, such as prompt strategies and
Together, these characteristics make LLMs fundamentally reported outcomes, was systematic, it inherently involved a
different from traditional research instruments: they cannot degree of subjective interpretation by the reviewers. Although
be frozen, independently audited, or deterministically rerun. consensus was reached through discussion to mitigate this,
Consequently, LLM-based studies must treat reproducibility individual biases cannot be entirely eliminated.
not as a procedural hurdle but as a structural limitation of
This review specifically identified challenges inherent
the technology, necessitating explicit acknowledgment and
to LLM research that also serve as limitations to its
meticulous reporting of model versions, access dates, prompt
own reproducibility. A significant proportion of the identi-
configurations, and variability observed during experimenta-
fied LLM-based CAs used proprietary models (eg, spe-
tion.
cific versions of GPT and Bard), which operate as “black
Limitations boxes” with undisclosed architectures, training data, and
update cycles. This means that replicating the exact behav-
While this scoping review provides a comprehensive mapping
ior or outputs of these agents is inherently challenging, if
of LLM-based CAs in PA and cognitive training, it is
not impossible, as the underlying model can change over
important to acknowledge several limitations that shape the
time (“model drift”) even with the same prompt, repre-
interpretation and generalizability of our findings.
senting a fundamental lack of version control and transpar-
As a scoping review, our primary aim was to map the ency within proprietary LLMs. Furthermore, while prompt
breadth of existing literature rather than to conduct a deep engineering emerged as a critical design practice, our review
synthesis or formal quality appraisal of individual studies. found that prompts were often inconsistently documented or
Consequently, we did not formally assess the methodolog- treated informally within the studies, impeding the ability of
ical quality or risk of bias of the included studies, mean- other researchers to precisely reproduce the designed agent
ing our review cannot make definitive statements about the behaviors or verify findings.
robustness of the evidence or the causal effectiveness of
In conclusion, while this scoping review provides valuable
the interventions. Similarly, we did not perform a meta-anal-
insights into the emerging field of LLM-based CAs for
ysis or other quantitative aggregation of outcomes due to
well-being, these limitations should be considered when
the inherent heterogeneity of study designs, interventions,
interpreting our findings and inform future research endeav-
and outcome measures, with our reported outcomes primar-
ors aiming for greater methodological rigor and transparency
ily consisting of qualitative summaries. While providing
in this rapidly evolving domain.
a comprehensive overview, the broad nature of a scoping
review also implies that specific nuances within individual
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 10
(page number not for citation purposes)

JMIR AI Silacci et al
Future Works and Research Directions documented, design practice. Future research should prioritize
developing and adopting standardized methodologies for
This scoping review has systematically mapped the current
prompt design, iteration, and evaluation. Furthermore, the
landscape of LLM-based CAs for PA and cognitive training,
systematic and open sharing of detailed prompt structures,
identifying several critical gaps and promising avenues for
including parameters such as temperature or top-p, is essential
future investigation. Building upon our findings, we propose
for enabling the reproducibility of LLM-based CA behav-
the following key directions for future research.
iors, as suggested by the LLM guidelines [70] project
initiated by Wagner et al [71]. Addressing reproducibility
Advancing LLM-Based CA Applications and
with proprietary LLMs is another fundamental challenge, as
Design
their inherent variability and black box nature (eg, model drift
Given the nascent and exploratory nature of LLM-based over time) present a significant impediment to replication.
CAs in cognitive training, future work should prioritize Future research must explicitly acknowledge these limita-
the development and rigorous evaluation of interventions tions, and when proprietary models are used, authors should
grounded in validated cognitive protocols. This includes meticulously document the exact model version, application
exploring their utility for specific cognitive functions programming interface details, and precise dates of interac-
beyond reminiscence and task scaffolding, such as execu- tion. The community should also explore and contribute to
tive functions or attention, potentially in clinical populations. research using open-source LLMs, where version control
Our review also highlighted a predominant focus on dyadic, and long-term reproducibility can be more readily ensured.
one-to-one interactions, with “coaching’' being a commonly Finally, while some studies share data, practices remain
adopted role. Future research should thus investigate more inconsistent. Future work should fully embrace comprehen-
diverse and complex social dynamics, explicitly exploring sive data sharing, adhering to FAIR principles. Specifically,
social setups such as companionship, alongside multiuser for LLM-based interventions, this mandates a focus on more
interfaces, group-based interventions, or integrating LLM- detailed and structured prompt documentation, enabling their
based CAs into broader community support systems for precise reproduction for verification and future research.
collective well-being. Furthermore, the observed fragility Conclusions
of LLM-based CA social roles underscores the need for
designing systems with persistent memory mechanisms, state This scoping review meticulously charted the nascent field of
awareness, and adaptive logical layers. Research should LLM-based CAs in PA and cognitive training. Our synthesis
explore how these structural reinforcements can enable more revealed a dynamic yet underexplored landscape, marked by
consistent, trustworthy, and long-term therapeutic alliances or a strong emphasis on PA coaching and a reliance on dyadic,
human-agent relationships. prompt-driven interactions. While these agents demonstrate
initial promise in engagement and perceived usefulness, a
Strengthening Methodological Rigor and
critical evaluation points to significant gaps in methodologi-
Transparency cal rigor and comprehensive outcome assessment. Crucially,
the unique challenges posed by proprietary LLMs and the
There is a critical need for more robust quantitative evalua-
current lack of structured prompt sharing emerge as funda-
tion of LLM-based CA effectiveness. Future studies should
mental impediments to reproducibility in this rapidly evolving
move beyond perceived usefulness and user satisfaction,
domain. Addressing these issues through rigorous evaluation
using validated behavioral and cognitive outcome measures.
and a strong commitment to open science will be paramount
This necessitates the adoption of mixed methods designs,
to advancing the scientific understanding and responsible
ideally with control groups and longitudinal follow-up, to
deployment of LLM-based CAs for well-being.
ascertain sustained impact. Our findings also underscore
that prompt engineering is a critical, yet inconsistently
Funding
Funding for this research was provided by two sources. The European Commission, through its Horizon research and
innovation program, DORIAN GRAY (grant 101156266), provided funding for some of the co-authors’ salaries and the
Covidence platform license. The Réseau de Compétence HES-SO Economie & Management provided funding that covered the
salary of one of the co-authors (project name SEP4PA).
Conflicts of Interest
None declared.
Multimedia Appendix 1
The comprehensive, open-access materials necessary to ensure the transparency, reproducibility, and verifiability of the
scoping review.
[ZIP File (ZIP archive File), 1202 KB-Multimedia Appendix 1]
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 11
(page number not for citation purposes)

JMIR AI Silacci et al
Checklist 1
PRISMA-ScR checklist.
[DOC File (Microsoft Word File), 122 KB-Checklist 1]
References
1. Li H, Zhang R, Lee YC, Kraut RE, Mohr DC. Systematic review and meta-analysis of AI-based conversational agents
for promoting mental health and well-being. NPJ Digit Med. Dec 19, 2023;6(1):236. [doi: 10.1038/s41746-023-00979-5]
[Medline: 38114588]
2. Maher CA, Davis CR, Curtis RG, Short CE, Murphy KJ. A physical activity and diet program delivered by artificially
intelligent virtual health coach: proof-of-concept study. JMIR mHealth uHealth. Jul 10, 2020;8(7):e17558. [doi: 10.2196/
17558] [Medline: 32673246]
3. Kocielnik R, Xiao L, Avrahami D, Hsieh G. Reflection companion: a conversational system for engaging users in
reflection on physical activity. Proceedings of the ACM Interactive Mobile Wearable and Ubiquitous Technologies.
2018;2(2):70. [doi: 10.1145/3214273]
4. Zhang J, Oh YJ, Lange P, Yu Z, Fukuoka Y. Artificial intelligence chatbot behavior change model for designing
artificial intelligence chatbots to promote physical activity and a healthy diet: viewpoint. J Med Internet Res. Sep 30,
2020;22(9):e22845. [doi: 10.2196/22845] [Medline: 32996892]
5. Cowan BR, Pantidi N, Coyle D, et al. What can I help you with?”: infrequent users’ experiences of intelligent personal
assistants. Presented at: Proceedings of the 19th International Conference on Human-Computer Interaction with Mobile
Devices and Services; Sep 4-7, 2017:1-12; Vienna, Austria. [doi: 10.1145/3098279.3098539]
6. Schöbel S, Schmitt A, Benner D, Saqr M, Janson A, Leimeister JM. Charting the evolution and future of conversational
agents: a research agenda along five waves and new frontiers. Inf Syst Front. Apr 2024;26(2):729-754. [doi: 10.1007/
s10796-023-10375-9]
7. Zhao WX, Zhou K, Li J, et al. A survey of large language models. arXiv. Preprint posted online on Mar 31, 2023. [doi:
10.48550/arXiv.2303.18223]
8. Huang J, Chang KCC. Towards reasoning in large language models: a survey. Presented at: Findings of the Association
for Computational Linguistics: ACL 2023; Jul 9-14, 2023; Toronto, Canada. [doi: 10.18653/v1/2023.findings-acl.67]
9. Chen J, Liu Z, Huang X, et al. When large language models meet personalization: perspectives of challenges and
opportunities. World Wide Web. Jul 2024;27(4):42. [doi: 10.1007/s11280-024-01276-1]
10. Lin B, Bouneffouf D, Landa Y, Jespersen R, Corcoran C, Cecchi G. COMPASS: computational mapping of patient-
therapist alliance strategies with language modeling. Transl Psychiatry. 2025;15:166. [doi: 10.1038/s41398-025-03379-
3]
11. Stephanidis C, Salvendy G, Antona M, et al. Seven HCI grand challenges. Int J Hum Comput Interact. Aug 27,
2019;35(14):1229-1269. [doi: 10.1080/10447318.2019.1619259]
12. Aldenaini N, Alslaity A, Sampalli S, Orji R. Persuasive strategies and their implementations in mobile interventions for
physical activity: a systematic review. Int J Hum Comput Interact. Jul 21, 2023;39(12):2292-2338. [doi: 10.1080/
10447318.2022.2075573]
13. Matthews J, Win KT, Oinas-Kukkonen H, Freeman M. Persuasive technology in mobile applications promoting physical
activity: a systematic review. J Med Syst. Mar 2016;40(3):72. [doi: 10.1007/s10916-015-0425-x] [Medline: 26748792]
14. Chew HSJ. The use of artificial intelligence–based conversational agents (chatbots) for weight loss: scoping review and
practical recommendations. JMIR Med Inform. Apr 13, 2022;10(4):e32578. [doi: 10.2196/32578] [Medline: 35416791]
15. Lyzwinski LN, Elgendi M, Menon C. Conversational agents and avatars for cardiometabolic risk factors and
lifestyle‑related behaviors: scoping review. JMIR mHealth uHealth. May 25, 2023;11:e39649. [doi: 10.2196/39649]
[Medline: 37227765]
16. Noh E, Won J, Jo S, Hahm DH, Lee H. Conversational agents for body weight management: systematic review. J Med
Internet Res. May 26, 2023;25:e42238. [doi: 10.2196/42238] [Medline: 37234029]
17. Oh YJ, Zhang J, Fang ML, Fukuoka Y. A systematic review of artificial intelligence chatbots for promoting physical
activity, healthy diet, and weight loss. Int J Behav Nutr Phys Act. Dec 11, 2021;18(1):160. [doi: 10.1186/s12966-021-
01224-6] [Medline: 34895247]
18. Dingler T, Kwasnicka D, Wei J, Gong E, Oldenburg B. The use and promise of conversational agents in digital health.
Yearb Med Inform. Aug 2021;30(1):191-199. [doi: 10.1055/s-0041-1726510] [Medline: 34479391]
19. Luo TC, Aguilera A, Lyles CR, Figueroa CA. Promoting physical activity through conversational agents: mixed methods
systematic review. J Med Internet Res. Sep 14, 2021;23(9):e25486. [doi: 10.2196/25486] [Medline: 34519653]
20. Fruitet J, Fouillen M, Facque V, Chainay H, De Chalvron S, Tarpin-Bernard F. Engaging with an embodied
conversational agent in a computerized cognitive training: an acceptability study with the elderly. Presented at:
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 12
(page number not for citation purposes)

JMIR AI Silacci et al
Proceedings of the ACM International Conference on Multimodal Interaction Companion (ICMI ’23 Companion); Oct
9-13, 2023:359-362; Paris, France. [doi: 10.1145/3610661.3616130]
21. Chan SWT, Sapkota S, Mathews R, Zhang H, Nanayakkara S. Prompto: investigating receptivity to prompts based on
cognitive load from memory training conversational agent. Proc ACM Interact Mob Wearable Ubiquitous Technol.
2020;4(4):121. [doi: 10.1145/3432190]
22. Kim Y, Kang Y, Kim B, Kim J, Kim GH. Exploring the role of engagement and adherence in chatbot-based cognitive
training for older adults: memory function and mental health outcomes. Behav Inf Technol. Jun 15,
2025;44(10):2405-2417. [doi: 10.1080/0144929X.2024.2362406]
23. Lauenroth A, Ioannidis AE, Teichmann B. Influence of combined physical and cognitive training on cognition: a
systematic review. BMC Geriatr. Jul 18, 2016;16(1):141. [doi: 10.1186/s12877-016-0315-1] [Medline: 27431673]
24. Bherer L, Erickson KI, Liu-Ambrose T. A review of the effects of physical activity and exercise on cognitive and brain
functions in older adults. J Aging Res. 2013;2013:657508. [doi: 10.1155/2013/657508] [Medline: 24102028]
25. Carrubba C, Torre MM, Langeard A, Temprado JJ. Enhancing cognition in older adults with interactive wall exergames.
Sci Rep. Oct 23, 2025;15(1):37104. [doi: 10.1038/s41598-025-21060-z] [Medline: 41131194]
26. Tricco AC, Lillie E, Zarin W, et al. PRISMA extension for scoping reviews (PRISMA‑ScR): checklist and explanation.
Ann Intern Med. Oct 2, 2018;169(7):467-473. [doi: 10.7326/M18-0850] [Medline: 30178033]
27. Silacci A, Giachetti B, Angelini L, et al. Large language model-based agents for physical activity and cognitive training:
a scoping review. JMIR Preprints. Preprint posted online on Jul 4, 2025. [Accessed 2026-02-20]
28. Singh VK, Singh P, Karmakar M, Leta J, Mayr P. The journal coverage of Web of Science, Scopus and Dimensions: a
comparative analysis. Scientometrics. Jun 2021;126(6):5113-5142. [doi: 10.1007/s11192-021-03948-5]
29. Gusenbauer M. Search where you will find most: comparing the disciplinary coverage of 56 bibliographic databases.
Scientometrics. 2022;127(5):2683-2745. [doi: 10.1007/s11192-022-04289-7] [Medline: 35571007]
30. Devlin J, Chang MW, Lee K, Toutanova K. BERT: pre-training of deep bidirectional transformers for language
understanding. arXiv. Preprint posted online on Oct 11, 2018. [doi: 10.48550/arXiv.1810.04805]
31. Guerreiro MP, Angelini L, Rafael Henriques H, et al. Conversational agents for health and well‑being across the life
course: protocol for an evidence map. JMIR Res Protoc. Sep 17, 2021;10(9):e26680. [doi: 10.2196/26680] [Medline:
34533460]
32. Covidence. URL: https://covidence.org [Accessed 2026-02-05]
33. Gale NK, Heath G, Cameron E, Rashid S, Redwood S. Using the framework method for the analysis of qualitative data
in multi-disciplinary health research. BMC Med Res Methodol. Sep 18, 2013;13(1):117. [doi: 10.1186/1471-2288-13-
117] [Medline: 24047204]
34. Salehzadeh Niksirat K, Goswami L, S. B. Rao P, et al. Changes in research ethics, openness, and transparency in
empirical studies between CHI 2017 and CHI 2022. Presented at: Proceedings of the 2023 CHI Conference on Human
Factors in Computing Systems; Apr 23-28, 2023:1-23; Hamburg, Germany. [doi: 10.1145/3544548.3580848]
35. Bak M, Chin J. The potential and limitations of large language models in identification of the states of motivations for
facilitating health behavior change. J Am Med Inform Assoc. Sep 1, 2024;31(9):2047-2053. [doi: 10.1093/jamia/
ocae057] [Medline: 38527272]
36. Washif JA, Pagaduan J, James C, Dergaa I, Beaven CM. Artificial intelligence in sport: exploring the potential of using
ChatGPT in resistance training prescription. Biol Sport. Mar 2024;41(2):209-220. [doi: 10.5114/biolsport.2024.132987]
[Medline: 38524820]
37. Dergaa I, Saad HB, El Omri A, et al. Using artificial intelligence for exercise prescription in personalised health
promotion: a critical evaluation of OpenAI’s GPT-4 model. Biol Sport. Mar 2024;41(2):221-241. [doi: 10.5114/
biolsport.2024.133661] [Medline: 38524814]
38. Pugliese N, Polverini D, Lombardi R, et al. Evaluation of ChatGPT as a counselling tool for Italian‑speaking MASLD
patients: assessment of accuracy, completeness and comprehensibility. J Pers Med. May 26, 2024;14(6):568. [doi: 10.
3390/jpm14060568] [Medline: 38929789]
39. Zaleski AL, Berkowsky R, Craig KJT, Pescatello LS. Comprehensiveness, accuracy, and readability of exercise
recommendations provided by an AI‑based chatbot: mixed methods study. JMIR Med Educ. Jan 11, 2024;10:e51308.
[doi: 10.2196/51308] [Medline: 38206661]
40. Vandelanotte C, Trost S, Hodgetts D, et al. Increasing physical activity using an just-in-time adaptive digital assistant
supported by machine learning: a novel approach for hyper-personalised mHealth interventions. J Biomed Inform. Aug
2023;144:104435. [doi: 10.1016/j.jbi.2023.104435] [Medline: 37394024]
41. Sun X, Teljeur I, Li Z, Bosch JA. Can a funny chatbot make a difference? Infusing humor into conversational agent for
behavioral intervention. Presented at: CUI ’24; Jul 8-10, 2024:1-19; Luxembourg, Luxembourg. Jul 8, 2024.[doi: 10.
1145/3640794.3665555]
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 13
(page number not for citation purposes)

JMIR AI Silacci et al
42. Hu J, Li J, Zeng Y, et al. Designing scaffolding strategies for conversational agents in dialog task of neurocognitive
disorders screening. Presented at: Proceedings of the 2024 CHI Conference on Human Factors in Computing Sytems;
May 11-16, 2024:1-21; Honolulu, HI. [doi: 10.1145/3613904.3642960]
43. Zhou H, Chen E, Wen S, Wang Y, Norel R. Large language models as a tool for cognitive stimulation: chatbot book
clubs for seniors. Presented at: 2024 IEEE International Conference on Digital Health (ICDH); Jul 7-13, 2024:123-125;
Shenzhen, China. [doi: 10.1109/ICDH62654.2024.00029]
44. Favela J, Cruz-Sandoval D, Parra MO. Conversational agents for dementia using large language models. Presented at:
2023 Mexican International Conference on Computer Science (ENC); Sep 11-13, 2023:1-7; Guanajuato, Guanajuato,
Mexico. [doi: 10.1109/ENC60556.2023.10508610]
45. ChatGPT. URL: https://chatgpt.com [Accessed 2026-02-05]
46. Cruz-Sandoval D, Favela J. Incorporating conversational strategies in a social robot to interact with people with
dementia. Dement Geriatr Cogn Disord. 2019;47(3):140-148. [doi: 10.1159/000497801] [Medline: 31247627]
47. Weimann TG, Schlieter H, Brendel AB. Virtual coaches: background, theories, and future research directions. Bus Inf
Syst Eng. 2022;64(4):515-528. [doi: 10.1007/s12599-022-00757-9]
48. Sun G, Zhan X, Such J. Building better AI agents: a provocation on the utilisation of persona in LLM-based
conversational agents. Presented at: Proceedings of the 6th Conference on ACM Conversational User Interfaces, CUI
2024; Jul 8-10, 2024:1-6; Luxembourg, Luxembourg. [doi: 10.1145/3640794.3665887]
49. Bhandari P, Fay N, Wise MJ, et al. Can LLM agents maintain a persona in discourse? Presented at: Proceedings of the
2025 Conference on Empirical Methods in Natural Language Processing; Nov 4-9, 2025:29201-29217; Suzhou, China.
[doi: 10.18653/v1/2025.emnlp-main.1487]
50. Wu S, Zhu Y, Hsu W, Lee ML, Deng Y. From personas to talks: revisiting the impact of personas on LLM-synthesized
emotional support conversations. Presented at: Proceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing; Nov 4-9, 2025:5439-5453; Suzhou, China. [doi: 10.18653/v1/2025.emnlp-main.277]
51. Ji Z, Lee N, Frieske R, et al. Survey of hallucination in natural language generation. ACM Comput Surv. Dec 31,
2023;55(12):1-38. [doi: 10.1145/3571730]
52. Zheng M, Pei J, Logeswaran L, Lee M, Jurgens D. When "a helpful assistant" is not really helpful: personas in system
prompts do not improve performances of large language models. Presented at: Findings of the Association for
Computational Linguistics: EMNLP 2024; Nov 12-16, 2024:15126-15154; Miami, FL. [doi: 10.18653/v1/2024.findings-
emnlp.888]
53. Shanahan M, McDonell K, Reynolds L. Role play with large language models. Nature New Biol. Nov
2023;623(7987):493-498. [doi: 10.1038/s41586-023-06647-8] [Medline: 37938776]
54. Kroczek LOH, May A, Hettenkofer S, Ruider A, Ludwig B, Mühlberger A. The influence of persona and conversational
task on social interactions with a LLM-controlled embodied conversational agent. Comput Human Behav. Nov
2025;172:108759. [doi: 10.1016/j.chb.2025.108759]
55. Lazik CK, Katins C, Kauter C, et al. The impostor is among us: can large language models capture the complexity of
human personas? Presented at: Proceedings of Mensch und Computer 2025 (MuC ’25); Aug 31 to Sep 3, 2025:434-451;
Chemnitz, Germany. [doi: 10.1145/3743049.3743057]
56. Nass C, Moon Y. Machines and mindlessness: social responses to computers. J Soc Issues. Jan 2000;56(1):81-103. [doi:
10.1111/0022-4537.00153]
57. Pataranutaporn P, Danry V, Leong J, et al. AI-generated characters for supporting personalized learning and well-being.
Nat Mach Intell. 2021;3(12):1013-1022. [doi: 10.1038/s42256-021-00417-9]
58. McIntosh TR, Susnjak T, Arachchilage N, et al. Inadequacies of large language model benchmarks in the era of
generative artificial intelligence. IEEE Trans Artif Intell. 2025;7(1):22-39. [doi: 10.1109/TAI.2025.3569516]
59. Chang Y, Wang X, Wang J, et al. A survey on evaluation of large language models. ACM Trans Intell Syst Technol. Jun
30, 2024;15(3):1-45. [doi: 10.1145/3641289]
60. Hanauer DA, Chen Y, Zheng K. Exploring reproducibility issues related to the use of large language models in the
clinical domain [Poster]. Presented at: AMIA 2025 Informatics Summit; Mar 10-13, 2025; Pittsburgh, PA. URL: https://
www.davidhanauer.com/CV/abstracts-presentations/2025/LLM_reproducibility_AMIA_abstract.pdf [Accessed
2026-02-17]
61. Zamfirescu-Pereira JD, Wong RY, Hartmann B, Yang Q. Why Johnny can’t prompt: how non-AI experts try (and fail) to
design LLM prompts. Presented at: Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems
(CHI ’23); Apr 23-28, 2023:1-21; Hamburg, Germany. [doi: 10.1145/3544548.3581388]
62. Demszky D, Yang D, Yeager DS, et al. Using large language models in psychology. Nat Rev Psychol.
2023;2(11):688-701. [doi: 10.1038/s44159-023-00241-5]
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 14
(page number not for citation purposes)

JMIR AI Silacci et al
63. Shool S, Adimi S, Saboori Amleshi R, Bitaraf E, Golpira R, Tara M. A systematic review of large language model
(LLM) evaluations in clinical medicine. BMC Med Inform Decis Mak. Mar 7, 2025;25(1):117. [doi: 10.1186/s12911-
025-02954-4] [Medline: 40055694]
64. Jiao J, Afroogh S, Xu Y, Phillips C. Navigating LLM ethics: advancements, challenges, and future directions. AI Ethics.
Dec 2025;5(6):5795-5819. [doi: 10.1007/s43681-025-00814-5]
65. Singh A. Evaluating the transparency and explainability of LLM-based educational systems. Social Science Research
Network (SSRN). Preprint posted online on Mar 31, 2025. URL: https://ssrn.com/abstract=5198565 [Accessed
2026-02-05]
66. Shanmugarasa Y, Pan S, Ding M, Zhao D, Rakotoarivelo T. Privacy meets explainability: managing confidential data
and transparency policies in LLM-empowered science. Presented at: Proceedings of the Extended Abstracts of the CHI
Conference on Human Factors in Computing Systems (CHI EA ’25); Apr 26 to May 1, 2025:1-8; Yokohama, Japan.
[doi: 10.1145/3706599.3720099]
67. Barman KG, Wood N, Pawlowski P. Beyond transparency and explainability: on the need for adequate and
contextualized user guidelines for LLM use. Ethics Inf Technol. Sep 2024;26(3):47. [doi: 10.1007/s10676-024-09778-2]
68. Franc JM, Cheng L, Hart A, Hata R, Hertelendy A. Repeatability, reproducibility, and diagnostic accuracy of a
commercial large language model (ChatGPT) to perform emergency department triage using the Canadian triage and
acuity scale. CJEM. Jan 2024;26(1):40-46. [doi: 10.1007/s43678-023-00616-w] [Medline: 38206515]
69. Staudinger M, Kusa W, Piroi F, Lipani A, Hanbury A. A reproducibility and generalizability study of large language
models for query generation. Presented at: Proceedings of the Annual International ACM SIGIR Conference on Research
and Development in Information Retrieval in the Asia Pacific Region (SIGIR‑AP ’24); Dec 9-12, 2024:186-196; Tokyo,
Japan. [doi: 10.1145/3673791.3698432]
70. Baltes S, Angermeir F, Arora C, et al. Guidelines for empirical studies in software engineering involving large language
models. arXiv. Preprint posted online on Aug 21, 2025. [doi: 10.48550/arXiv.2508.15503]
71. Wagner S, Barón MM, Falessi D, Baltes S. Towards evaluation guidelines for empirical studies involving llms.
Presented at: 2025 IEEE/ACM International Workshop on Methodological Issues with Empirical Studies in Software
Engineering (WSESE); May 3, 2025; Ottawa, ON. [doi: 10.1109/WSESE66602.2025.00011]
Abbreviations
AI: artificial intelligence
CA: conversational agent
FAIR: findable, accessible, interoperable, reusable
HCI: human-computer interaction
LLM: large language model
PA: physical activity
PRISMA-ScR: Preferred Reporting Items for Systematic Reviews and Meta-Analyses extension for Scoping Reviews
RQ: research question
WoS: Clarivate Web of Science
Edited by Khaled El Emam; peer-reviewed by Emre Sezgin, José Santos; submitted 04.Jul.2025; final revised version
received 15.Dec.2025; accepted 18.Jan.2026; published 12.Mar.2026
Please cite as:
Silacci A, Giachetti B, Angelini L, Lopomo NF, Andreoni G, Mugellini E, Cherubini M, Caon M
Large Language Model–Based Agents for Physical Activity and Cognitive Training: Scoping Review
JMIR AI 2026;5:e80123
URL: https://ai.jmir.org/2026/1/e80123
doi: 10.2196/80123
© Alessandro Silacci, Benedetta Giachetti, Leonardo Angelini, Nicola Francesco Lopomo, Giuseppe Andreoni, Elena
Mugellini, Mauro Cherubini, Maurizio Caon. Originally published in JMIR AI (https://ai.jmir.org), 12.Mar.2026. This
is an open-access article distributed under the terms of the Creative Commons Attribution License (https://creativecom-
mons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided the original
work, first published in JMIR AI, is properly cited. The complete bibliographic information, a link to the original publication
on https://www.ai.jmir.org/, as well as this copyright and license information must be included.
https://ai.jmir.org/2026/1/e80123 JMIR AI 2026 | vol. 5 | e80123 | p. 15
(page number not for citation purposes)
