---
telephone_index: 71
title: "Trustworthy LLM-Mediated Communication: LAAC"
category: 07_model_collapse_homogeneity
venue: "arXiv"
year: 2025
doi: 
arxiv_id: 2511.04184
preferred_source_type: preprint_or_unresolved
publisher_url: https://arxiv.org/abs/2511.04184
quality_flags: []
---

# Citation Context

- Telephone index: 71
- Preferred source: arXiv
- DOI: none
- arXiv: 2511.04184
- PDF: `assets\papers\pdf\07_model_collapse_homogeneity\71_trustworthy-llm-mediated-communication-laac.pdf`

## Extracted Abstract

The proliferation of AI-generated content has created an absurd communication theater where senders use LLMs to inflate simple ideas into verbose content, recipients use LLMs to compress them back into summaries, and as a consequence neither party engage with authentic content. LAAC (LLM as a Communicator) proposes a paradigm shift—positioning LLMs as intelligent communication intermediaries that capture the sender’s intent through structured dialogue and facilitate genuine knowledge exchange with recipients. Rather than perpetuating cycles of AI-generated inflation and compression, LAAC enables authentic communication across diverse contexts including academic papers, proposals, professional emails, and cross-platform content generation. However, deploying LLMs as trusted communication intermediaries raises critical questions about information fidelity, consistency, and reliability. This position paper systematically evaluates the trustworthiness requirements for LAAC’s deployment across multiple communication domains. We investigate three fundamental dimensions: (1) Information Capture Fidelity—accuracy of intent extraction during sender interviews across different communication types, (2) Reproducibility—consistency of structured knowledge across multiple interaction instances, and (3) Query Response Integrity—reliability of recipient-facing responses without hallucination, source conflation, or fabrication. Through controlled experiments spanning multiple LAAC use cases, we assess these trust dimensions using LAAC’s multi-agent architecture. Preliminary findings reveal measurable trust gaps that must be addressed before LAAC can be reliably deployed in high-stakes communication scenarios.
Title: Trustworthy LLM-Mediated Communication: Evaluating Information Fidelity in LLM as a Communicator (LAAC) Framework in Multiple Application Domains

Source PDF: D:\0-Research\5-Telephone\assets\papers\pdf\07_model_collapse_homogeneity\71_trustworthy-llm-mediated-communication-laac.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-06-20T12:46:17+00:00
- page_count: 17
- status: ok
- text_char_count: 37216

Metadata:
- author: Mohammed Musthafa Rafi; Adarsh Krishnamurthy; Aditya Balu
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- Introduction (page 1)
- Related Work (page 2)
  - LLM-Mediated Communication (page 2)
  - Information Fidelity and Hallucination (page 3)
  - Multi-Agent LLM Systems (page 3)
  - Trustworthy AI and Verification (page 3)
- LAAC Framework Architecture (page 3)
  - Three-Agent Architecture (page 4)
    - Interview Agent (page 4)
    - Extraction Agent (page 4)
    - Query Agent (page 4)
  - Information Flow (page 4)
  - Domain Adaptability (page 5)
- Trustworthiness Evaluation Methodology (page 5)
  - Dimension 1: Information Capture Fidelity (page 6)
    - Evaluation Protocol (page 6)
    - Metrics (page 6)
  - Dimension 2: Reproducibility (page 6)
    - Evaluation Protocol (page 6)
    - Metrics (page 7)
  - Dimension 3: Query Response Integrity (page 7)
    - Evaluation Protocol (page 7)
    - Metrics (page 7)
  - Experimental Design Considerations (page 8)
- Implementation: Academic Paper Development (page 8)
  - System Architecture (page 8)
  - Author Interface (page 8)
  - Reviewer Interface (page 11)
  - Technical Implementation (page 12)
- Preliminary Findings and Discussion (page 12)
  - Information Capture Fidelity Observations (page 12)
  - Reproducibility Challenges (page 13)
  - Query Response Integrity Findings (page 13)
  - Cross-Cutting Observations (page 13)
  - Implications for LAAC Deployment (page 14)
- Limitations and Future Work (page 14)
  - Current Limitations (page 14)
  - Future Research Directions (page 15)
- Conclusion (page 15)

Markdown Content:

Trustworthy LLM-Mediated Communication: Evaluating
Information Fidelity in LLM as a Communicator (LAAC)
Framework in Multiple Application Domains
Mohammed Musthafa Rafi, Adarsh Krishnamurthy, Aditya Balu
Iowa State University
Ames, IA, USA
{mohd7, adarsh, baditya}@iastate.edu
Abstract
The proliferation of AI-generated content has created an absurd communication theater
where senders use LLMs to inflate simple ideas into verbose content, recipients use LLMs to
compress them back into summaries, and as a consequence neither party engage with authentic
content. LAAC (LLM as a Communicator) proposes a paradigm shift—positioning LLMs as
intelligent communication intermediaries that capture the sender’s intent through structured
dialogue and facilitate genuine knowledge exchange with recipients. Rather than perpetuating
cycles of AI-generated inflation and compression, LAAC enables authentic communication across
diverse contexts including academic papers, proposals, professional emails, and cross-platform
content generation. However, deploying LLMs as trusted communication intermediaries raises
critical questions about information fidelity, consistency, and reliability. This position paper
systematically evaluates the trustworthiness requirements for LAAC’s deployment across multiple communication domains. We investigate three fundamental dimensions: (1) Information
Capture Fidelity—accuracy of intent extraction during sender interviews across different communication types, (2) Reproducibility—consistency of structured knowledge across multiple interaction instances, and (3) Query Response Integrity—reliability of recipient-facing responses
without hallucination, source conflation, or fabrication. Through controlled experiments spanning multiple LAAC use cases, we assess these trust dimensions using LAAC’s multi-agent
architecture. Preliminary findings reveal measurable trust gaps that must be addressed before
LAAC can be reliably deployed in high-stakes communication scenarios.
Keywords: Large Language Models, Human-AI Communication, Information Fidelity, Trustworthy AI, Academic Writing, Multi-Agent Systems
1 Introduction
The rapid adoption of Large Language Models (LLMs) has fundamentally transformed how people
create and consume written content. However, this transformation has produced an unexpected and
inefficient phenomenon: a communication theater where authenticity is systematically eliminated at
both ends of the exchange. Senders prompt LLMs to expand terse bullet points into elaborate prose,
adding formality and verbosity that obscures rather than clarifies their original intent. Recipients,
overwhelmed by this inflated content, immediately prompt their own LLMs to compress these
expansive texts back into bullet-point summaries. The result is a complete cycle of artificial inflation
and deflation where genuine human thought is lost in translation, computational resources are
wasted, and neither party engages meaningfully with the actual content.
1
5202
voN
6
]LC.sc[
1v48140.1152:viXra

This wasteful cycle affects nearly every domain of written communication—from academic papers artificially expanded with filler text to business emails that say in five paragraphs what could
be expressed in two sentences. The fundamental problem is not the LLM technology itself, but
rather its misapplication as a content generator rather than as an intelligent intermediary. We argue
that LLMs should not replace human communication but rather facilitate it—serving as trusted
mediators that faithfully capture sender intent and enable recipient comprehension.
We propose LAAC (LLM as a Communicator), a paradigm that repositions LLMs from content
generators to communication intermediaries. Rather than producing verbose expansions of simple
ideas, LAAC systems engage senders in structured dialogue to extract and formalize their authentic
intent, then enable recipients to interact directly with this structured knowledge through natural
language queries. This approach promises to restore authenticity to LLM-mediated communication while leveraging the genuine strengths of these systems—their ability to facilitate knowledge
structuring, semantic understanding, and interactive question-answering.
However, deploying LLMs as communication intermediaries introduces critical trustworthiness
challenges. If an LLM misrepresents a sender’s intent, produces inconsistent knowledge structures
from identical inputs, or fabricates information when responding to recipient queries, the entire
communication exchange becomes unreliable. Unlike traditional LLM applications where errors
might be caught and corrected by human review, LAAC systems operate as autonomous intermediaries where trust is essential for adoption.
This position paper makes the following contributions:
• We identify and formalize three fundamental trust dimensions for LAAC systems: Information
Capture Fidelity, Reproducibility, and Query Response Integrity
• We present a systematic evaluation methodology for assessing these trust dimensions across
diverse communication domains
• We describe a concrete implementation of LAAC for academic paper development and review,
demonstrating the framework’s applicability to high-stakes communication scenarios
• We report preliminary findings from controlled experiments that reveal measurable gaps in
current LLM trustworthiness for communication intermediary roles
• We propose future research directions for improving LAAC system reliability and establishing
verifiable trust metrics
The remainder of this paper is structured as follows. Section 2 reviews related work in LLMmediated communication and trustworthy AI systems. Section 3 details the LAAC framework
architecture and its three-agent design. Section 4 presents our evaluation methodology for measuring trustworthiness across the three critical dimensions. Section 5 describes our implementation
in the academic paper domain. Section 6 discusses preliminary findings and their implications.
Section 8 concludes with future research directions.
2 Related Work
2.1 LLM-Mediated Communication
The use of LLMs to assist in various forms of written communication has become widespread, with
applications ranging from email composition [19] to academic writing support [11]. However, most
existing systems focus on content generation rather than communication mediation. Tools like
2

GPT-4 [15], Claude [3], and specialized writing
manner—transforming user inputs into polished
enabling recipient interaction with the underlyi
Recent work has explored more interactive
writing systems [12] enable iterative refinement
co-author rather than a faithful intermediary. S
to ask questions about existing documents, but
than capturing intent during document creation
2.2 Information Fidelity and Hallucin
A critical challenge for deploying LLMs in high
plausible but factually incorrect information—a
research has documented LLM hallucinations ac
[14], mathematical reasoning [5], and citation g
Efforts to mitigate hallucination include r
mechanisms [16], and uncertainty quantification
factual accuracy in external knowledge domai
tion—the core requirement for communication
2.3 Multi-Agent LLM Systems
Recent advances in multi-agent LLM architectur
task decomposition and specialized agent roles
employ multiple agents with distinct responsibi
tures inspire LAAC’s design, but existing multicommunication mediation.
2.4 Trustworthy AI and Verification
The broader field of trustworthy AI has establ
cluding transparency, explainability, fairness, a
systems [10] provide formal guarantees for spec
extensively applied to communication fidelity sc
Our work bridges these research areas by
LLM-mediated communication, proposing concr
an evaluation methodology suitable for commun
3 LAAC Framework Architectu
The LAAC (LLM as a Communicator) framew
to maintain information fidelity throughout the
applications where a single model attempts to se
cation mediation task into three specialized age
function.

istants [6] typically operate in a one-directional
utputs without maintaining semantic fidelity or
intent.
proaches to AI-assisted writing. Collaborative
rough dialogue, but still position the LLM as a
larly, document querying systems [4] allow users
hese systems analyze pre-written content rather
ion
akes applications is their tendency to generate
enomenon known as hallucination [9]. Extensive
ss domains including factual question-answering
ration [1].
ieval-augmented generation [13], fact-checking
]. However, these approaches primarily address
rather than fidelity to user-provided informarmediary systems.
have demonstrated improved performance through
. Systems like AutoGPT [17] and MetaGPT [8]
es to accomplish complex tasks. These architecnt systems focus on task completion rather than
ed principles for reliable system deployment inrobustness [2]. Verification methods for neural
properties, but these techniques have not been
arios.
plying trustworthiness principles specifically to
metrics for information fidelity, and presenting
ation intermediary systems.
e
k employs a multi-agent architecture designed
mmunication pipeline. Unlike traditional LLM
all functions, LAAC decomposes the communiroles, each optimized for a specific trust-critical

3.1 Three-Agent Architecture
3.1.1 Interview Agent
The Interview Agent serves as the primary inter
role is to extract comprehensive information abo
Rather than accepting free-form text and attemp
questions that elicit specific details about the s
For academic paper development, the Inter
findings, theoretical contributions, and related w
for objectives, action items, stakeholders, and
domain-specific and designed to capture all in
resentation.
Critical to trustworthiness, the Interview A
tent generation. It should ask questions rather
sender responses are ambiguous, and explicitly
filling them with inferred content.
3.1.2 Extraction Agent
The Extraction Agent processes the complete int
edge representation of the sender’s intent. Th
truth for all subsequent interactions—it is what
The knowledge structure varies by domain
explicit relationships between concepts, support
about certainty levels. For academic papers, th
(introduction, methodology, results, discussion)
may be appropriate.
The Extraction Agent’s trustworthiness depe
content without introducing new information,
details. Its output must be a faithful transformat
format.
3.1.3 Query Agent
The Query Agent provides the recipient interfac
natural language questions about any aspect of t
based solely on the extracted knowledge struc
relevant information without reading verbose
intent.
The Query Agent faces perhaps the most cr
strong LLM tendency to hallucinate. When fa
the structured knowledge, it must explicitly a
plausible but unfounded responses. It must also
or misrepresenting the certainty of claims.
3.2 Information Flow
The complete LAAC communication flow proce

e between the sender and the LAAC system. Its
the sender’s intent through structured dialogue.
g to expand it, the Interview Agent asks targeted
er’s message.
w Agent asks about research methodology, key
k. For business communications, it might probe
eadlines. The Interview Agent’s prompts are
mation necessary for complete knowledge rept’s objective is information extraction, not conn make assumptions, request clarification when
cknowledge gaps in understanding rather than
iew transcript and generates a structured knowlepresentation serves as the canonical source of
e sender actually meant to communicate.
ut generally includes hierarchical organization,
evidence or reasoning for claims, and metadata
might be organized by standard paper sections
or other communications, alternative structures
s on its ability to accurately reflect the interview
srepresenting relationships, or omitting critical
n of the sender’s expressed intent into a queryable
o the structured knowledge. Recipients can ask
sender’s message, and the Query Agent responds
e. This enables recipients to efficiently access
tent while maintaining fidelity to the sender’s
cal trustworthiness challenge: it must resist the
with questions that cannot be answered from
owledge this limitation rather than generating
oid conflating information from different sections
as follows:

1. The sender initiates communication by en
2. The Interview Agent conducts a structu
extract comprehensive information about
3. The complete interview transcript is proc
structured knowledge representation
4. The sender reviews and potentially refines
5. Recipients interact with the Query Agent
structured knowledge
6. The Query Agent responds to recipient qu
mation from the knowledge structure
This architecture ensures that the sender’s
accessed consistently by all recipients. No conten
extraction, structuring, and retrieval.
3.3 Domain Adaptability
While this paper focuses primarily on academic
LAAC architecture is designed for adaptability
structure remains constant, but agent prompts
customized for each domain:
• Academic Papers: Interview about met
sections; enable detailed technical queries
• Business Proposals: Interview about ob
components; enable stakeholder-specific q
• Professional Emails: Interview about
topic hierarchy; enable quick information
• Technical Documentation: Interview a
as technical reference; enable developer qu
This domain adaptability is essential for L
trustworthiness evaluation challenge—each dom
domain-specific trust metrics.
4 Trustworthiness Evaluation M
We propose a systematic methodology for eval
mental dimensions. Each dimension addresses a
role and requires distinct evaluation approaches

ging with the Interview Agent
dialogue, asking domain-specific questions to
sender’s intent
ed by the Extraction Agent, which generates a
e extracted knowledge structure
sking questions that are answered based on the
ions by retrieving and presenting relevant inforent is captured once, represented faithfully, and
nflation or compression occurs—only information
per development as a demonstration domain, the
ross communication contexts. The three-agent
nowledge schemas, and interaction patterns are
dology, results, contributions; structure as paper
tives, solutions, timelines; structure as proposal
ies
ntext, action items, dependencies; structure as
kup
ut system architecture, APIs, use cases; structure
es
AC’s practical utility, but it also multiplies the
may exhibit different failure modes and require
ethodology
ting LAAC trustworthiness across three fundatical aspect of the communication intermediary

4.1 Dimension 1: Information Capture Fidelity
Information Capture Fidelity measures how accurately the Interview Agent extracts information
from the sender and how faithfully the Extraction Agent represents this information in the knowledge structure. This dimension addresses the fundamental question: Does the structured knowledge
accurately reflect what the sender intended to communicate?
4.1.1 Evaluation Protocol
We employ a ground-truth comparison methodology:
1. Select representative content samples from the target domain (e.g., existing academic papers,
business proposals)
2. For each sample, conduct an Interview Agent session where a domain expert role-plays as the
author, providing information based on the original document
3. Generate the extracted knowledge structure
4. Compare the knowledge structure against the original document using both automated metrics and human evaluation
4.1.2 Metrics
We assess fidelity across multiple dimensions:
• Content Coverage: Percentage of key concepts from the original appearing in the structured
knowledge
• Semantic Accuracy: Correctness of relationships and claims in the knowledge structure
(human-evaluated)
• Information Addition: Percentage of concepts in the structured knowledge that do not
appear in the interview or original (false positives)
• Information Omission: Percentage of key concepts from the interview that do not appear
in the structured knowledge (false negatives)
4.2 Dimension 2: Reproducibility
Reproducibility measures the consistency of the LAAC system when processing the same sender
intent multiple times. Given identical or near-identical interview inputs, does the system produce
equivalent knowledge structures? This dimension is critical for establishing LAAC as a reliable
communication medium.
4.2.1 Evaluation Protocol
We employ a repeated-extraction methodology:
1. Conduct an Interview Agent session on a specific topic
2. Process the same interview transcript through the Extraction Agent multiple times (varying
random seeds, temperature parameters)
6

3. Compare the resulting knowledge structures for consistency
4. Alternatively, conduct multiple interview sessions with the same information and compare
extracted structures
4.2.2 Metrics
We measure consistency using:
• Structural Similarity: Overlap in hierarchical organization and section structure
• Semantic Equivalence: Agreement on core claims and relationships (evaluated via semantic
similarity metrics)
• Detail Consistency: Stability of specific facts, numbers, and citations across extractions
• Variability Analysis: Quantification of differences and identification of factors causing
inconsistency
4.3 Dimension 3: Query Response Integrity
Query Response Integrity assesses the trustworthiness of the Query Agent’s responses to recipient
questions. This dimension addresses whether recipients can rely on the information provided by the
system, focusing specifically on hallucination avoidance, source fidelity, and appropriate uncertainty
acknowledgment.
4.3.1 Evaluation Protocol
We employ a question-answer verification methodology:
1. Generate a knowledge structure from a known ground-truth document
2. Create a test set of questions spanning multiple categories: directly answerable from the
structure, requiring inference, and unanswerable
3. Collect Query Agent responses
4. Evaluate responses for accuracy, groundedness, and appropriate uncertainty expression
4.3.2 Metrics
We assess query integrity using:
• Answer Accuracy: Correctness of responses to answerable questions
• Hallucination Rate: Frequency of fabricated information in responses
• Citation Accuracy: Correctness of attributions and references in responses
• Uncertainty Calibration: Appropriateness of confidence expressions and acknowledgment
of knowledge gaps
• Source Conflation: Frequency of incorrectly combining information from distinct sources
7

4.4 Experimental Design Considerati
Our evaluation methodology addresses several i
Domain Diversity: We evaluate across mu
ability. Initial experiments focus on academic
ground truth, but we extend to business commu
Complexity Variation: We include comm
emails) to complex (multi-section research pape
information complexity.
LLM Model Comparison: We evaluate m
understand whether trustworthiness challenges a
Human Expert Validation: All automate
uation, particularly for semantic fidelity and ha
is challenging.
5 Implementation: Academic P
To demonstrate the LAAC framework and ena
plemented a complete system for academic pap
an ideal testbed: academic papers have well-defi
stakes for information fidelity.
5.1 System Architecture
Figure 1 shows the landing page of our implem
authors who develop papers through AI-guide
informed decision-making.
Figure 2 presents the authentication interf
reviewer accounts. The system maintains separ
the underlying knowledge representation.
5.2 Author Interface
The author workflow guides researchers through
dialogue. Figure 3 shows the author dashboard
The Interview Agent asks domain-specific q
• Research motivation and problem stateme
• Related work and theoretical positioning
• Methodology and experimental design
• Results and key findings
• Discussion and implications
• Limitations and future work

s
ortant experimental design considerations:
ple communication domains to assess generalizers due to well-defined structure and verifiable
cations and technical documentation.
cation samples ranging from simple (single-topic
to understand how trustworthiness scales with
tiple LLM backends (GPT-4, Claude, Llama) to
model-specific or systematic across architectures.
metrics are complemented by human expert evalcination detection where automated assessment
per Development
systematic trustworthiness evaluation, we imdevelopment and review. This domain provides
d structure, verifiable factual content, and high
ntation, which supports two distinct user roles:
nterviews, and reviewers who query papers for
, providing access control for both author and
workflows optimized for each role while sharing
uctured paper development via Interview Agent
ere researchers manage their papers.
tions spanning:

Figure 1: LAAC landing page showing dual interfaces for authors and reviewers. The system
emphasizes intelligent paper development and AI-powered content analysis to facilitate authentic
academic communication.
9

Figure 2: Login interface supporting both author and reviewer account types. Role-based access
control ensures appropriate permissions for paper development versus review activities.
10

Figure 3: Author dashboard for managing pape
pers and resume work on existing drafts, with a
from AI-guided interviews.
Authors provide information conversational
while maintaining an interview transcript. Th
remaining natural and efficient compared to tra
Once the interview is complete, the Extracti
ture organized by paper sections. Authors revi
provide additional information through follow-u
5.3 Reviewer Interface
Reviewers interact with submitted papers throu
dashboard displaying available papers.
Figure 4: Reviewer dashboard showing papers av
engage with the Query Agent to examine meth
reading verbose manuscript text.
Rather than reading a traditional manuscrip

under development. Authors can create new paapers backed by structured knowledge extracted
and the system extracts structured knowledge
pproach ensures comprehensive coverage while
ional paper writing.
Agent generates a hierarchical knowledge structhis structure and can request modifications or
dialogue.
the Query Agent. Figure 4 shows the reviewer
able for review. Reviewers can select papers and
ology, results, and other paper aspects without
reviewers ask questions about the research:

• What methodology did the authors use?
• What were the primary results?
• How does this work compare to existing a
• What are the limitations of the study?
• Are the claims adequately supported?
The Query Agent responds based on the
providing direct answers. This enables efficie
access to all relevant information.
5.4 Technical Implementation
The system is implemented as a web applicatio
Frontend: React-based interface with separ
chat interface for Interview Agent and Query A
Backend: Node.js API server managing us
tration. PostgreSQL database for user accounts
LLM Integration: API integration with
cialized prompts for each agent optimized for th
as JSON with hierarchical organization.
Evaluation Infrastructure: Logging sys
knowledge structures, and query interactions. A
interface for trustworthiness assessment.
6 Preliminary Findings and Di
We conducted initial experiments evaluating th
demic paper implementation. While comprehens
these preliminary findings reveal important cha
6.1 Information Capture Fidelity Obs
Testing with five published computer science pa
Strengths: The Interview Agent successfull
questions, methodology, results). When author
the Extraction Agent generally represented it a
Weaknesses: We identified concerning gap
• Quantitative Results: Numerical findin
author stating ”we achieved 94.3% accu
achieved” with the specific number lost.
• Technical Details: Fine-grained method
level of abstraction, potentially losing crit
• Citation Context: When authors menti
knowledge sometimes misrepresented the
versus work being contrasted against).

roaches?
uctured knowledge, citing specific sections and
focused review while ensuring reviewers have
ith the following components:
workflows for authors and reviewers. Real-time
nt interactions.
authentication, paper storage, and LLM orchesd paper metadata.
ude (Anthropic) for all three agent roles. Spespecific functions. Structured knowledge stored
m capturing all interview transcripts, extracted
mated metrics calculation and human evaluation
ussion
hree trustworthiness dimensions using our acaresults require extensive testing across domains,
nges and patterns.
vations
rs, we observed:
xtracted most major paper components (research
provided explicit information during interviews,
rately in the knowledge structure.
n specific areas:
were sometimes approximated or omitted. An
y” might be extracted as ”high accuracy was
gical specifics were often summarized at a higher
l reproducibility information.
d related work during interviews, the extracted
tionship (e.g., conflating work being built upon

Variable Extraction Accuracy: Differen
Abstracts and high-level contributions were capt
(human-evaluated), while detailed methodology
6.2 Reproducibility Challenges
We processed the same interview transcript th
temperature parameters:
Structural Variability: Knowledge struc
While major sections (Introduction, Methodolog
varied considerably. One extraction might gro
distribute them across multiple sections.
Detail Inconsistency: Specific claims app
tions. For example, a limitation mentioned in t
in 7 out of 10 runs—an unacceptable inconsiste
Implicit Information Generation: We ob
implicit connections or implications not explicit
inferences were reasonable, they represent a dep
ients.
Temperature Sensitivity: Reproducibili
rameter. Lower temperatures (0.1-0.3) produce
nuanced information. Higher temperatures (0.7variability across runs.
6.3 Query Response Integrity Findin
Testing with 50 questions across answerable, in
vealed:
Answerable Questions: For questions dire
ture, the Query Agent provided accurate respon
minor inaccuracies or omissions.
Hallucination Rate: Critically, when ask
knowledge structure), the Query Agent fabricat
acknowledging the knowledge gap. This rate is
Citation Fabrication: When the knowled
sometimes invented specific page numbers, pub
vided in the original information—a particula
communication.
Source Conflation: In papers discussing m
attributed findings from one paper to another
answering comparative questions.
Overconfidence: The Query Agent rarely
beyond the explicit knowledge structure. Thi
recipients trying to assess information reliability
6.4 Cross-Cutting Observations
Several patterns emerged across all three trustw

paper sections exhibited different fidelity levels.
d with approximately 85-90% semantic accuracy
d statistical results showed 60-70% fidelity.
gh the Extraction Agent ten times with varied
es showed significant organizational differences.
Results) were consistent, subsection organization
related concepts together, while another might
ed, disappeared, or were reworded across extracinterview appeared in the extracted knowledge
y level for a communication intermediary.
ved instances where the Extraction Agent added
stated in the interview. While sometimes these
ure from strict fidelity that could mislead recipstrongly correlated with LLM temperature pamore consistent structures but sometimes missed
) captured more detail but showed unacceptable
ence-requiring, and unanswerable categories rey addressing information in the knowledge strucs 82% of the time. The remaining 18% included
unanswerable questions (information not in the
plausible responses 31% of the time rather than
acceptably high for a trusted intermediary.
structure contained citations, the Query Agent
tion years, or author names that were not proconcerning form of hallucination for academic
iple related works, the Query Agent occasionally
r combined results from multiple studies when
ressed uncertainty even when making inferences
ack of calibrated confidence is problematic for
thiness dimensions:

Information Loss at Agent Boundaries: Each agent transition (Interview to Extraction,
Extraction to Query) introduced information loss or distortion. The cumulative effect across the
pipeline means recipient-facing information may diverge significantly from sender intent.
Abstraction Tendency: The system consistently pushed toward higher levels of abstraction,
losing specific details. This may reflect LLM training on summarization tasks, but it conflicts with
LAAC’s goal of maintaining full information fidelity.
Domain Formality Bias: The system showed bias toward formal academic language patterns
even when authors provided information conversationally. This could obscure author intent behind
generic academic phrasing.
Lack of Uncertainty Tracking: The knowledge structure format did not adequately distinguish between explicitly stated facts, reasonable inferences, and uncertain claims. All information
was presented with equal confidence in query responses.
6.5 Implications for LAAC Deployment
These preliminary findings suggest that current LLM technology, while powerful, exhibits systematic trustworthiness gaps that must be addressed before LAAC systems can be deployed as reliable
communication intermediaries:
1. Fidelity Verification Mechanisms: Systems need explicit verification steps where senders
confirm the accuracy of extracted knowledge before recipients access it.
2. Provenance Tracking: Knowledge structures should maintain direct links to specific interview statements, enabling recipients to verify information sources.
3. Uncertainty Quantification: Systems must explicitly represent and communicate confidence levels for different pieces of information.
4. Hallucination Detection: Query Agents require robust mechanisms for detecting when
questions cannot be answered from available knowledge and refusing to speculate.
5. Human-in-the-Loop Validation: For high-stakes communication domains, automated extraction should be complemented by human review and approval.
7 Limitations and Future Work
This position paper presents preliminary work with several important limitations that motivate
future research directions.
7.1 Current Limitations
Limited Experimental Scope: Our evaluation focused primarily on academic papers with a small
sample size. Comprehensive assessment requires larger datasets spanning diverse communication
domains, complexity levels, and LLM models.
Single Implementation: We evaluated one specific implementation of the LAAC architecture. Different design choices (agent prompts, knowledge schemas, interaction patterns) may yield
different trustworthiness profiles.
Preliminary Metrics: Our evaluation metrics, while systematically defined, have not been
validated against user trust perceptions or real-world deployment outcomes. The relationship between measured fidelity and perceived trustworthiness requires investigation.
14

Controlled Experiments: We evaluated u
inputs. Real-world usage with diverse users m
controlled settings.
7.2 Future Research Directions
Advanced Trustworthiness Mechanisms: W
proving LAAC trustworthiness including retrie
structures in interview transcripts, uncertaintyknowledge boundaries, multi-model consensus w
edge and their outputs are reconciled, and for
about information fidelity for specific properties
User Studies: Comprehensive evaluation
LAAC system trustworthiness. We plan contro
cation to traditional methods, investigating use
trustworthiness requirements from practitioners
Domain Expansion: We will extend LA
communication domains including business prop
policy briefs, and cross-cultural communication
Standardized Benchmarks: The broader
ized benchmarks for evaluating communication i
across approaches and tracking progress over ti
Regulatory and Ethical Consideration
important questions arise about liability when
sure requirements for AI-mediated communicat
levels in different domains.
8 Conclusion
The proliferation of LLMs has created a parado
used to inflate and then compress information,
authentic human communication. The LAAC fr
ing LLMs as trusted intermediaries that faithf
understanding through structured knowledge an
However, our systematic evaluation reveals
mediary role faces critical trustworthiness chal
in information capture fidelity, reproducibility
achieve variable extraction accuracy, Extraction
from identical inputs, and Query Agents show
citation fabrication.
These findings should not be interpreted as f
rather as empirical validation that trustworthin
evaluated and engineered. The path forward re
uncertainty quantification, and hallucination pre
loop validation for high-stakes communication d
As LLMs continue to evolve, their potential
more authentic and efficient application than co
requires the AI research community to prioriti

g structured protocols with researcher-controlled
reveal additional failure modes not captured in
plan to investigate technical approaches for im-
-augmented extraction that grounds knowledge
are query responses that explicitly acknowledge
re multiple LLMs independently extract knowll verification methods that provide guarantees
equires understanding how real users perceive
d studies comparing LAAC-mediated communirust calibration, and identifying domain-specific
C implementation and evaluation to additional
als, technical documentation, grant applications,
enarios.
search community would benefit from standardrmediary systems, enabling rigorous comparison
As LAAC-style systems become more prevalent,
intermediaries misrepresent information, disclon, and standards for acceptable trustworthiness
al situation where these powerful tools are being
sting computational resources while eliminating
mework offers an alternative paradigm: positiony capture sender intent and facilitate recipient
nteractive querying.
t deploying LLMs in this communication interges. Current systems exhibit measurable gaps
nd query response integrity. Interview Agents
gents produce inconsistent knowledge structures
oncerning tendencies toward hallucination and
damental limitations of the LAAC approach, but
cannot be assumed—it must be systematically
res technical innovations in fidelity verification,
ntion, combined with appropriate human-in-themains.
e as communication intermediaries represents a
nt generation. However, realizing this potential
trustworthiness alongside capability, developing

systems that users can rely on to faithfully repre
for understanding and measuring that trustwort
a path toward reliable LLM-mediated communi
References
[1] A. Alkaissi and S. I. McFarlane. Artificial
writing. Cureus, 15(2), 2023.
[2] D. Amodei et al. Concrete problems in ai s
[3] Anthropic. Claude: Constitutional ai and h
[4] Y. Chen et al. Document question answerin
ings of the 2022 Conference on Empirical M
pages 5621–5634. Association for Computa
[5] H. Frieder et al. Mathematical capabilities
[6] Grammarly. Ai-powered writing assistant.
[7] J. He et al. Quantifying uncertainty in large
2023.
[8] S. Hong et al. Metagpt: Meta programmi
preprint arXiv:2308.00352, 2023.
[9] Z. Ji et al. Survey of hallucination in natur
55(12):1–38, 2023.
[10] M. Katz et al. Verifying neural networks:
Methods in System Design, 57:261–296, 202
[11] S. Kumar and J. Rodriguez. Large languag
challenges. Nature Human Behaviour, 7(8)
[12] R. Lee et al. Collaborative writing with a
Transactions on Computer-Human Interac
[13] P. Lewis et al. Retrieval-augmented genera
in Neural Information Processing Systems
[14] S. Maynez et al. On faithfulness and factu
of the 58th Annual Meeting of the Associa
1906–1919. Association for Computational
[15] OpenAI. Gpt-4 technical report. arXiv pre
[16] N. Rashkin et al. Fact-checking meets f
Proceedings of the 2021 Conference on E
(EMNLP), pages 2374–2390. Association fo
[17] T. Richards. Autogpt: An autonomous gp

nt their intent. This paper provides a framework
ess, establishes preliminary baselines, and charts
ion.
lucinations in chatgpt: Implications in scientific
ty. arXiv preprint arXiv:1606.06565, 2016.
mlessness. https://www.anthropic.com, 2023.
with contextualized language models. In Proceedhods in Natural Language Processing (EMNLP),
nal Linguistics, 2022.
chatgpt. arXiv preprint arXiv:2301.13867, 2023.
tps://www.grammarly.com, 2024.
guage models. arXiv preprint arXiv:2302.09664,
for multi-agent collaborative framework. arXiv
language generation. ACM Computing Surveys,
urrent methods and future challenges. Formal
models for academic writing: Opportunities and
34–1245, 2023.
Understanding the human-ai partnership. ACM
n, 30(4):1–28, 2023.
n for knowledge-intensive nlp tasks. In Advances
eurIPS), volume 33, pages 9459–9474, 2020.
y in abstractive summarization. In Proceedings
n for Computational Linguistics (ACL), pages
nguistics, 2020.
nt arXiv:2303.08774, 2023.
tography: Verifying claims about images. In
rical Methods in Natural Language Processing
Computational Linguistics, 2021.
experiment. GitHub repository, 2023.

[18] Q. Wu et al. Autogen: Enabling next-gen llm applications via multi-agent conversation. arXiv
preprint arXiv:2308.08155, 2023.
[19] M. Zhang et al. Ai-assisted email composition: Usage patterns and user satisfaction. In
Proceedings of the CHI Conference on Human Factors in Computing Systems, pages 1–14.
ACM, 2023.
17
