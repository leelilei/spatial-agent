---
title: "Can AI Reason Like an Urban Planner? Benchmarking Large Language Models Against Professional Judgment"
source_pdf: "01_urban_benchmarks\\06_UPBench_Liu2026.pdf"
extractor_backend: pdfplumber
extracted_at_utc: 2026-06-21T17:31:29+00:00
page_count: 32
status: ok
text_char_count: 105016
quality_flags: ["abstract_may_include_layout_noise"]
---

# PDF Fulltext

- Source PDF: `assets\papers\pdf\01_urban_benchmarks\06_UPBench_Liu2026.pdf`
- Backend: pdfplumber
- Extracted at UTC: 2026-06-21T17:31:29+00:00
- Page count: 32
- Status: ok
- Text chars: 105016
- Quality flags: abstract_may_include_layout_noise

## Metadata

- Title: Can AI Reason Like an Urban Planner? Benchmarking Large Language Models Against Professional Judgment
- Author: Yijie Deng; He Zhu; Wen Wang; Junyou Su; Minxin Chen; Wenjia Zhang
- DOI: unknown
- Keywords: unknown
- Subject: unknown

## Extracted Abstract

Problem, Research Strategy, and Findings The emergence of large language models (LLMs) confronts urban planning with an urgent epistemological question: what dimensions of professional planning knowledge can artificial intelligence replicate, and what remains irreducibly human? Despite growing deployment of AI tools in planning practice, we lack systematic frameworks for evaluating whether these systems can reason with the contextual sensitivity, value awareness, and institutional literacy that characterize professional planning judgment. This paper introduces Urban Planning Bench (UPBench), a domainspecific evaluative framework that assesses LLM reasoning across a 4×5 matrix encompassing four knowledge pillars (Principles of Urban Planning, Cross-Disciplinary Integration, Planning Governance, and Planning Practice) and five cognitive levels adapted from Bloom’s revised taxonomy. Evaluating 25 LLMs through a dual-track protocol combining automated scoring with expert panel assessment, we identify an non-monotonic cognitive curve: models perform more robustly on higher-order analytical tasks than on ostensibly lower-order factual recall and integrative judgment. This counterintuitive finding reveals that planning’s “lower-order” knowledge is in fact deeply embedded in institutional, jurisdictional, and temporal context—making it resistant to pattern-generalization strategies. We codify these limitations into four epistemic diagnostics—regulatory hallucination, conceptual conflation, wickedness paralysis, and phronetic deficit—each illuminating a specific dimension of planning expertise that resists computational replication. Takeaway for Practice These findings provide planning practitioners and educators with an evidencebased framework for differential delegation—determining which tasks can be responsibly augmented by AI and which require irreducibly human professional judgment. LLMs demonstrate competence in cross-disciplinary synthesis and broad analytical reasoning, suggesting productive augmentation potential for literature review, scenario generation, and preliminary policy analysis. However, they exhibit persistent incapacity in jurisdiction-specific regulatory interpretation, normative conflict resolution, and context-sensitive procedural application—tasks that constitute the core of planning’s phronetic expertise. Planning agencies should implement structured verification protocols for any AI-assisted regulatory analysis, while planning education should reorient from knowledge transmission toward cultivating the institutional literacy, normative judgment, and contextual sensitivity that constitute planning’s distinctive professional contribution.

## Outline

- Introduction (page 2)
- Theoretical Framework (page 5)
  - Planning as Phronetic Practice (page 5)
  - The Cognitive Architecture of Planning Expertise (page 7)
  - From Planning Assessment to AI Benchmarking (page 8)
- Research Design (page 9)
  - Assessment Architecture (page 9)
  - Cross-National Scenario Construction (page 10)
  - Dual-Track Evaluation Protocol (page 11)
  - Models Evaluated (page 12)
- Findings (page 13)
  - Aggregate Performance Landscape (page 14)
  - The Non-Monotonic Cognitive Curve (page 16)
  - Knowledge Domain Asymmetries (page 17)
  - Four Epistemic Diagnostics (page 19)
  - Cross-National Institutional Asymmetry (page 21)
- Discussion (page 22)
  - What LLMs Reveal About Planning Knowledge Itself (page 22)
  - Redefining the Human-AI Boundary in Planning Practice (page 23)
  - Implications for Planning Education (page 24)
  - Limitations and Future Research (page 25)
- Conclusion (page 26)
- References (page 27)
- Qualitative Analysis of Model Responses (page 32)

## Markdown Content

Can AI Reason Like an Urban Planner?
Benchmarking Large Language Models Against Professional
Judgment
Yijie Deng1,2,*, He Zhu1,2,*, Wen Wang1,2, Junyou Su1,2, Minxin Chen1,2, and Wenjia
Zhang1,3,†
1Behavioral and Spatial AI Lab, Tongji University; 2Behavioral and Spatial AI Lab, Peking
University; 3College of Architecture and Urban Planning, Tongji University
*Yijie Deng and He Zhu contributed equally to this work. †Corresponding author: Wenjia
Zhang.
ABSTRACT
Problem, Research Strategy, and Findings
The emergence of large language models (LLMs) confronts urban planning with
an urgent epistemological question: what dimensions of professional planning knowledge can artificial intelligence replicate, and what remains irreducibly human? Despite growing deployment of AI tools in planning practice, we lack systematic frameworks for evaluating whether these systems can reason with the contextual sensitivity, value awareness, and institutional literacy that characterize professional planning judgment. This paper introduces Urban Planning Bench (UPBench), a domainspecific evaluative framework that assesses LLM reasoning across a 4×5 matrix encompassing four knowledge pillars (Principles of Urban Planning, Cross-Disciplinary
Integration, Planning Governance, and Planning Practice) and five cognitive levels
adapted from Bloom’s revised taxonomy. Evaluating 25 LLMs through a dual-track
protocol combining automated scoring with expert panel assessment, we identify an
non-monotonic cognitive curve: models perform more robustly on higher-order analytical tasks than on ostensibly lower-order factual recall and integrative judgment.
This counterintuitive finding reveals that planning’s “lower-order” knowledge is in
fact deeply embedded in institutional, jurisdictional, and temporal context—making
it resistant to pattern-generalization strategies. We codify these limitations into four
epistemic diagnostics—regulatory hallucination, conceptual conflation, wickedness
paralysis, and phronetic deficit—each illuminating a specific dimension of planning
expertise that resists computational replication.
Takeaway for Practice
These findings provide planning practitioners and educators with an evidencebased framework for differential delegation—determining which tasks can be responsibly augmented by AI and which require irreducibly human professional judgment.
LLMs demonstrate competence in cross-disciplinary synthesis and broad analytical reasoning, suggesting productive augmentation potential for literature review,
scenario generation, and preliminary policy analysis. However, they exhibit persistent incapacity in jurisdiction-specific regulatory interpretation, normative conflict
resolution, and context-sensitive procedural application—tasks that constitute the
core of planning’s phronetic expertise. Planning agencies should implement structured verification protocols for any AI-assisted regulatory analysis, while planning
education should reorient from knowledge transmission toward cultivating the institutional literacy, normative judgment, and contextual sensitivity that constitute
planning’s distinctive professional contribution.
KEYWORDS
artificial intelligence; planning knowledge; professional judgment; phronesis;
benchmark; large language models; planning education
6202
nuJ
01
]LC.sc[
1v87611.6062:viXra

1. Introduction
Planning has long grappled with a foundational disciplinary question: what constitutes
distinctively professional planning knowledge? Friedmann (1987) framed this as the
problem of linking knowledge to action—identifying what planners know that enables
them to intervene meaningfully in the trajectory of cities and regions. Schön (1992a) recast professional knowledge not as applied science but as reflection-in-action, a form of
knowing embedded in practice that resists codification into rules. More recently, Flyvbjerg (2001) argued that planning’s core intellectual contribution lies in phronesis—the
Aristotelian practical wisdom that is context-dependent, value-laden, and irreducible
to technical procedure. This argument can be extended through practice-based and
relational approaches to planning, which understand planning knowledge not as an
individual cognitive possession but as something produced through situated practices,
institutional relations, material settings, and interactions among heterogeneous actors
(Davoudi, 2015; Healey, 2006; Hillier, 2007; McFarlane, 2011). This nuance is difficult
for generic AI models to capture, because they are trained primarily on decontextualized textual patterns rather than embedded participation in the social, institutional,
and material relations through which planning judgment is formed. Despite decades of
theoretical refinement, however, this debate has remained largely confined to philosophical and conceptual inquiry. While we have rich conceptual vocabularies for describing
planning expertise, there are few empirical instruments for measuring what planners
actually know—and, crucially, for identifying what dimensions of that knowledge are
uniquely human. This gap has been brought into unprecedented sharp relief by the
global proliferation of large language models (LLMs) in planning practice.
The mainstream adoption of LLMs transforms this longstanding epistemological
question into an empirical inquiry with immediate, existential stakes for the planning
profession.. These AI systems can now generate zoning analyses, synthesize public
comments, draft comprehensive plan elements, and produce policy recommendations
that read as professionally competent (Sanchez, Brenman, & Ye, 2025; Sanchez, 2025).
When a machine can produce text that superficially resembles professional planning
output, the line between authentic professional judgment and pattern-matched fluency
becomes urgent—not merely for philosophy of planning, but for the profession’s daily
practice, educational institutions, and core democratic accountability.. Planning is not
unique in facing this challenge: medicine has developed Med-PaLM to benchmark clinical reasoning (Singhal et al., 2025), and law has constructed LegalBench to evaluate
legal judgment (Guha et al., 2023). Critically, both fields have established domainspecific evaluation frameworks to separate what AI can and cannot do, a foundational
step that planning has yet to complete. This gap is amplified by planning’s distinctive disciplinary context: unlike medicine, where diagnostic reasoning follows relatively
structured protocols, or law, where precedent provides a bounded corpus, planning
operates squarely in the domain of“wicked problems”Rittel and Webber (1973). Here,
problems have no definitive formulation, every intervention is a “one-shot operation,”
and solutions are not true or false, but better or worse relative to contested values.
Yet the planning scholarship on AI has thus far remained at the level of either
broad ethical commentary, or narrow technical application. Many scholars have depicted the ethical landscape of AI in urban planning, identifying concerns around bias,
transparency, democratic accountability, and the displacement of professional judgment (Kitchin, 2016; Mittelstadt et al., 2016; Selbst et al., 2019). Their contribution
is important but remains primarily normative: it defines what we should worry about,
but provides no empirical framework to measure what AI actually can and cannot
2

do when confronted with the specific cognitive demands of real-world planning work.
At the technical end, emerging studies have applied LLMs to bounded, well-defined
planning subtasks: automated plan evaluation (Zheng et al., 2025), public sentiment
analysis on upzoning policy (Rong et al., 2025), urban scenario generation (Wang et al.,
2026), multi-agent planning simulation frameworks (Ni et al., 2024), and the domainspecific fine-tuned planning model PlanGPT, which outperforms general LLMs on planning text generation, statutory document drafting, and policy analysis tasks (Zhu et
al, 2024). These studies collectively demonstrate that AI can achieve strong performance on specific, rule-bound subtasks, but none attempt to evaluate AI capabilities
across the full scope of planning expertise. Another line focuses on computationally
bounded applications, such as planning support systems, urban simulation, and datadriven urban analytics (Batty, 2018; Geertman & Stillwell, 2004; Klosterman, 1997;
Pelzer, 2017).However, planning is not merely a technical exercise; it involves situated
judgment, communicative reasoning, value conflict, and action under uncertainty, as
emphasized in planning theory and professional practice scholarship (Forester, 1989;
Friedmann, 1987; Healey, 1997; Rittel & Webber, 1973; Schön, 1992a). What remains
underdeveloped is a grounded planning-specific framework for evaluating AI capabilities across the full cognitive architecture of planning expertise: one that can distinguish
between the dimensions of planning knowledge that LLMs can approximate and those
that remain, for now, distinctively human.
This gap is not merely an academic limitation: the absence of such a framework
leaves the entire planning profession vulnerable on two existential fronts. First, without
a validated evaluation framework, competing claims about LLM competence in planning remain remain largely anecdotal rather than evidence-based (Chang et al., 2024).
Planners may over-rely on AI in high-stakes for tasks where its reasoning is unreliable,
or unnecessarily reject LLM support for routine procedural work that could streamline
professional workloads (Dell'Acqua et al., 2023). Planning expertise inherently operates within overlapping institutional and regulatory regimes, where core competence
lies in navigating contextual ambiguity rather than applying fixed rule (Rydin, 2007).
This suggests current AI limitations in planning may be structural rather than merely
developmental. Second, and more fundamentally, the process of constructing such a
framework forces us explicitly define what constitutes professional planning expertise.This conceptual clarification holds independent scholarly value, regardless of the
ongoing evolution of AI tools. In this sense, benchmarking AI is not merely a technical
exercise imported from computer science; it serves as an epistemic reference point that
compels planning to formalize its own underlying knowledge structure.
The concept of systematic evaluative frameworks is, in fact, deeply familiar to planning scholarship, even if the term “AI benchmarking” is not been widely adopted.
Plan quality evaluation research has established multidimensional normative criteria
to evaluate comprehensive plans, using consistent rubrics and intercoder reliability
procedures to judge factual grounding, goal setting, policy design, and implementation
mechanisms (Berke & Godschalk, 2009; Lyles & Stevens, 2014). The American Institute of Certified Planners (AICP) examination, for instance, organizes its content into
six distinct practice areas covering planning theory, urban and rural planning management and regulations, related knowledge of planning, and technical practice (AICP,
2023). This practice-based assessment structure demonstrates a significant trend of international convergence: despite differences among jurisdictions, the content of planner
qualification certifications in China, the United Kingdom, and Australia also includes
these four fundamental dimensions. Beyond formal plan evaluation and licensing, planning scholarship has long framed professional expertise as practice-based reflective
3

judgment (Hoch, 2019; Willson, 2020). frames planning knowledge as pragmatic craft
rather than rule-following—a characterization that challenges conventional assessment
approaches but nonetheless implies evaluable standards of craftsmanship. Planning education scholarship further reinforces this evaluative logic. Clayton, Goodspeed, and
colleagues (2025) identify five distinct pedagogical approaches for cultivating professional capacity beyond mere analytical skill, including design thinking, collaborative
practice, and ethical reasoning. Each approach its own set of assessable competence
dimensions. Frank (2006), reviewing three decades of planning education thought,
traces the evolution from knowledge-transmission models toward competence-based
frameworks that emphasize integration, judgment, and contextual responsiveness. Our
study extends this evaluative tradition to a new object: LLM. It retains planning’s core
normative commitments: multidimensional assessment, contextual sensitivity, and the
recognition that professional judgment cannot be reduced to any single metric. Just as
plan quality research asks “what defines a sound professional plan?”, this study poses a
parallel question: “what would it mean for an AI to reason like a competent planner?”
To address this question, we develop Urban Planning Bench (UPBench), a domainspecific evaluation framework that assesses LLM reasoning against the cognitive structure of planning expertise. UPBench is organized along two dimensions. The first is
a knowledge architecture organized into four core pillars: Principles of Urban Planning, Cross-Disciplinary Integration, Planning Governance, and Planning Practice.
This structure derives from common curricula design and professional licensure examinations across international planning education systems (AICP, 2023; MNR, 2024;
RTPI, 2023; PIA, 2023). The second dimension adopts a cognitive hierarchy adapted
from the revised Bloom’s taxonomy, selectively using five levels from Remember to
Evaluate while excluding Create because the framework focuses on assessment of professional judgment rather than open-ended creative production (Anderson & Krathwohl, 2001).. This 4×5 matrix creates a differentiated map of planning cognition. It
enables systematic, apples-to-apples comparison of LLM performance across all planning knowledge domains and reasoning levels.. Our study evaluate 25 LLMs using a
dual-track protocol: automated scoring for structured tasks and expert panel assessment for open-ended reasoning, with explicit attention to the reasoning chains—the
sequences of knowledge retrieval, inference, and justification—that distinguish genuine
understanding from surface-level pattern matching.
This paper makes three contributions to planning scholarship. First, methodologically, it introduces a comprehensive, domain-specific framework for evaluating LLM
reasoning in urban planning, grounded in the discipline’s own knowledge structure
rather than generic computer-science benchmarks transposed without disciplinary
adaptation. Second, theoretically, it uses AI’s systematic failure patterns as an empirical lens to illuminate the epistemic architecture of planning expertise. By identifying which dimensions of phronesis resist computational replication, the study sharpens
understanding of what makes planning knowledge distinctive. Third, practically, it
provides an evidence-based foundation for differential delegation. This is a principled
approach to delineating which planning tasks can be responsibly augmented by AI and
which require irreducible human judgment. It carries direct implications for professional
practice, planning education, and the governance of AI tools in planning agencies.
The remainder of this paper proceeds as follows. Section 2 develops the theoretical framework, situating our approach within the traditions of phronetic planning
research and plan quality evaluation. Section 3 describes the research design, including the construction of UPBench, the evaluation protocol, and the expert validation
process. Section 4 presents findings across knowledge domains, cognitive levels, and
4

failure modes. Section 5 discusses the the
tions of these findings, with particular atte
practice. Section 6 concludes with limitat
2. Theoretical Framework
2.1. Planning as Phronetic Practice
To evaluate whether AI can reason like an
planning reasoning consists of. We ground
that distinguishes three forms of knowled
scientific knowledge), techne (craft knowl
(practical wisdom oriented toward action
requires all three, its professional identit
capacity to make value-laden judgment in
situations (Flyvbjerg, 2001; Campbell, 20
tends a rich theoretical lineage.
The lineage begins with the critique of
Schön’s (1992a) concept of reflection-in-ac
is not applied science but a form of kno
argued, engage in a continuous conversati
they encounter resistance and surprise. Sch
for planning: the competent planner does
cases; rather, she constructs the situatio
framing, and moving toward a solution
emphasis on embodied, situated performa
and Dreyfus (1986), who characterize ex
accumulated, context-responsive intuition
LLM reasoning is stark: while planners n
feedback loop of action and reframing, LL
of tokens based on training data, lackin
reflection-in-action.
If Schön dismantled the applied-scien
(2001) radicalized the critique by argui
phronetic—oriented not toward universal
tical wisdom. He identifies four characte
other forms of knowledge: it is context-dep
experience that cannot be reduced to prop
ment rather than technical optimization;
deliberation rather than neutral analysis
ing that planning knowledge is produced
spend their days mediating among stakeh
vising responses to institutional constrai
ing of phronesis suggests that AI’s limita
ontological—the systems lack the embed
netic judgment presupposes.
Planning expertise is not a body of pro
ply but a repertoire of coping strategies
with changing socio-ecological and institu

etical, practical, and educational implicaon to the human-AI boundary in planning
s and directions for future research.
ban planner, we must first articulate what
ur framework in the Aristotelian tradition
episteme (universal, context-independent
e oriented toward making), and phronesis
particular circumstances). While planning
s constituted primarily by phronesis: the
mplex, uncertain, and politically charged
). This characterization draws on and exhnical rationality in professional practice.
n established that professional knowledge
ng embedded in doing. Practitioners, he
with the situation, reframing problems as
’s (1992a) earlier study made this concrete
t simply retrieve rules and apply them to
through a reciprocal process of naming,
at remains irreducibly experiential. This
e has been further elaborated by Dreyfus
rtise as a mode of coping that draws on
her than rule-following. The contrast with
gate uncertainty through an experiential
generate statistically probable sequences
he situated engagement that constitutes
model of individual expertise, Flyvbjerg
that planning research itself should be
eory but toward context-dependent pracics of phronesis that distinguish it from
dent rather than rule-governed; it requires
tional knowledge; it involves ethical judgnd it is exercised through power-sensitive
Healey (1992) complements this by showhrough communicative practice. Planners
ders, interpreting regulations, and improThis distributed, relational understandns may be not merely computational but
ness in institutional networks that phrositions that practitioners retrieve and aphat evolves through ongoing engagement
nal conditions (Xiang, 2016; Healey, 1992,

2006; Hoch, 2019). Xiang extends phronesis into the domain of socio-ecological practice through his concept of ecophronesis, emphasizing the bidirectional relationship
between wisdom for practice and wisdom from practice. This bidirectionality is crucial: planning knowledge is not merely applied to situations but generated through
engagement with them—a recursive dynamic that static training data cannot capture
(Xiang, 2016; Hoch, 2019). Because planning operates within overlapping governance
regimes that shift with political cycles, regulatory reforms, and community transformations, practitioners must constantly recalibrate their knowledge to remain effective
(Monkkonen & Manville, 2020; Healey, 1997, 2006). This temporal and institutional
embeddedness—where expertise must be continuously renewed rather than statically
stored, and where practical wisdom is embedded in tacit experience, organizational
routines, institutional contexts, and situated professional judgment—poses a distinct
challenge for AI systems trained on fixed data snapshots (Polanyi, 1966; Schön, 1983;
Healey, 1997; Rydin, 2007).
Recent work in moral psychology and virtue theory clarifies the integrative complexity of this craft knowledge, particularly its irreducibly normative character. Kristjánsson (2015) characterizes phronesis as a “psycho-moral integrator”—a meta-virtue that
orchestrates the application of other virtues to particular circumstances. While Darnell (2022) operationalize it psychologically as “contextual integrative thinking” that
synthesizes perception, emotion, deliberation, and action in situationally appropriate
ways. Forester (2017) adds the dimension of moral imagination, arguing that effective
planning judgment requires attending to dimensions of goodwill, trust, and relational
commitment that transcend rational analysis. Campbell (2012) similarly argues that
planning ethics is not an external constraint on professional judgment but constitutive of it—the ethical dimension is woven into every act of framing, prioritizing, and
recommending.
Synthesizing these theoretical contributions, we identify four characteristics of planning’s phronetic knowledge that pose fundamental challenges for AI replication. First,
contextual sensitivity: the same rule, policy, or principle carries different meanings
and implications in different institutional, cultural, and geographic contexts. Practitioners often have to navigate a “regulatory hydra” of overlapping statutes, agencies,
discretionary conventions, political expectations, and local implementation cultures,
making planning judgment deeply situated rather than merely rule-following (Booth,
1996, 2007; Healey, 1999, 2006; Sanyal, 2005; Rydin, 2007). Second, non-algorithmic
value balancing: planning routinely confronts situations in which multiple legitimate
values conflict and no single objective function can determine the correct outcome.
This reflects the value pluralism and wickedness of planning problems: conflicts among
equity, efficiency, environmental protection, property rights, democratic participation,
and growth cannot be resolved by technical rationality alone (Berlin, 1969; Davidoff,
1965; Rittel & Webber, 1973). Third, temporal and institutional embeddedness: planning knowledge is not static but evolves with regulatory reforms, political shifts, and
community transformations—requiring practitioners to continuously update their understanding in ways that training data snapshots cannot capture. Fourth, democratic
accountability: the legitimacy of planning judgment derives not solely from its epistemic correctness but from the deliberative process through which it is produced—a
procedural dimension that AI systems, which generate outputs without participatory
process, structurally cannot provide.
6

2.2. The Cognitive Architecture of Planning Expertise
If phronesis constitutes the philosophical core of planning expertise, we need an operational framework for specifying what this expertise encompasses in practice. Across
AICP certification materials, planning accreditation expectations, and comparable
international professional frameworks, planning knowledge is repeatedly organized
around four broad functions: understanding urban systems, integrating knowledge from
adjacent fields, operating within legal-institutional governance structures, and exercising professional judgment in plan-making and implementation (AICP, 2023; PAB, 2022;
RTPI, 2023; PIA, 2023). These functions provide the rationale for organizing planning
expertise into four knowledge pillars: Principles of Urban Planning, Cross-Disciplinary
Integration, Planning Governance, and Planning Practice.
The first pillar, Principles of Urban Planning, encompasses the foundational understanding of cities as complex socio-spatial systems, including theories and analytical
concepts related to urban development, land use, transportation, housing, economic
change, demographic processes, environmental systems, and spatial structure. This
corresponds to episteme in the Aristotelian framework: theoretical knowledge about
urban phenomena that provides the analytical substrate for professional judgment.
Frank (2006), reviewing three decades of planning education thought, identifies this
theoretical grounding as consistently present across institutional contexts, though its
specific content evolves with disciplinary advances.
The second pillar, Cross-Disciplinary Integration, reflects planning’s characteristic
position at the intersection of multiple disciplines. Planning draws from architecture,
urban design, transportation engineering, environmental science, public health, real
estate economics, geography, sociology, data science, and ecological analysis. This corresponds to techne: the capacity to synthesize diverse technical knowledge toward practical ends. Clayton, Goodspeed, and colleagues (2025) emphasize that contemporary
planning education must cultivate integrative capacities that transcend any single analytical framework—preparing planners to work across disciplinary boundaries in ways
that require more than additive accumulation of separate knowledge domains.
The third pillar, Planning Governance, concerns the legal, regulatory, institutional,
and political conditions under which planning operates. In the American context, this
includes zoning, environmental review procedures (NEPA/CEQA), subdivision regulations, and public participation requirements, and the distribution of authority across
federal, state, regional, and local governments. Salet (2018) demonstrates how legalinstitutional knowledge in planning is not merely factual but interpretive—planners
must construct legality through acts of professional judgment rather than simply applying predetermined rules.
The fourth pillar, Planning Practice, represents the integrative phronesis of professional work—the capacity to synthesize theoretical understanding, technical knowledge,
and institutional awareness into coherent professional judgment within specific project
contexts. It includes plan-making, community engagement, stakeholder negotiation,
implementation strategy, project management, monitoring, and adjustment. Planning
practice therefore most directly expresses the phronetic character of planning expertise: practitioners must exercise judgment that is simultaneously technically informed,
institutionally grounded, ethically attentive, and politically realistic. Alexander (2022)
similarly argues that planning theories have often struggled to adequately account for
planning practices themselves—the situated, heterogeneous, and action-oriented forms
of work through which planning knowledge is actually mobilized.
Planning theorists have long recognized that professional expertise rests on the in7

tegration, not mere possession, of diverse knowledge types. Rydin (2007), for instance,
identifies empirical, process, predictive, and normative knowledges as functionally distinct yet practically intertwined categories, while Healey (2009) emphasizes synthetic
thinking as a core cross-cutting capacity. Nevertheless, these typologies have not been
operationalized for AI evaluation. Our framework addresses this gap by treating the
four pillars as an integrated knowledge network: expertise in any one domain is enriched and constrained by knowledge of the others. A competent planner diagnosing a
transportation problem draws simultaneously on systems theory (how networks function), cross-disciplinary knowledge (public health impacts, environmental regulations),
governance (funding mechanisms, jurisdictional authority), and practice (stakeholder
engagement strategies, implementation sequencing).
2.3. From Planning Assessment to AI Benchmarking
The concept of systematic professional evaluation is native to planning scholarship.
Berke and Godschalk (2009) established the plan quality evaluation paradigm, assessing comprehensive plans against normative criteria including direction-setting, fact
basis, goal articulation, policy specificity, implementation mechanisms, and monitoring provisions. Lyles and Stevens (2014) traced this tradition’s growth from 1994 to
2012, noting both its contributions and its limitations—particularly the challenge of
evaluating judgment-dependent qualities rather than merely procedural completeness.
Stevens, Lyles, and Berke (2014) further strengthened the methodological basis of plan
evaluation by emphasizing intercoder reliability, a concern that parallels the expertagreement measures used in UPBench. However, the evaluation traditions remains
relatively underspecified, particularly with respect to how planners exercise situated
judgment in complex contextst; what we contribute is its extension to AI systems.
AI benchmarking emerged in computer science to address a related problem: how
to measure the capabilities of systems whose internal processes are difficult to observe
directly. General-purpose benchmarks such as MMLU assess broad knowledge across
dozens of academic subjects (Hendrycks et al., 2021) , while domain-specific benchmarks increasingly adapt their data sources and task designs to the applied characteristics of particular professions. In medicine, for example, benchmarks such as MultiMedQA and Med-PaLM draw on medical examinations, clinical question-answering
datasets, and case-based materials to evaluate not only biomedical knowledge but also
clinically situated reasoning (Singhal et al., 2023). Similarly, legal benchmarks such as
LegalBench assess legal reasoning through tasks grounded in statutes, contracts, and
professional legal interpretation (Guha et al., 2023).
The recent emergence of planning-adjacent AI evaluation indicates growing recognition of the need for similar domain-specific benchmarks in urban planning. UrbanPlanBench offers a Chinese-language planning knowledge assessment, and develop an agentic LLM framework for automated plan evaluation (Zheng et al., 2025). PlanGPT-VL
extends evaluation into multimodal territory by benchmarking vision-language models on planning documents and maps (Zhu et al., 2025). These efforts demonstrate
the field’s readiness for AI evaluation frameworks tailored to planning. However, our
framework addresses three specific deficits in existing approaches. First, the absence of
a theory-grounded cognitive architecture: existing AI benchmarks assess planning tasks
without reference to the epistemological traditions, including phronesis, reflection-inaction, communicative rationality, that define what planning knowledge is. Second, the
conflation of factual recall with professional reasoning: most benchmarks test whether
8

models “know” planning facts rather th
judgment. Third, the neglect of reasoning
final answers rather than the reasoning ch
obscuring whether correct outputs reflect
UPBench is designed to address all five d
3. Research Design
3.1. Assessment Architecture
UPBench employs Evidence-Centered De
structures assessment around three interc
the knowledge constructs to be measured,
behaviors constitute evidence of those con
narios that elicit those behaviors (Mislevy
our student model is the four-pillar know
our evidence model maps Bloom’s revise
reasoning demands (Anderson & Krathw
sessment scenarios that require domain-sp
The cognitive hierarchy comprises five l
question format aligned with the cogniti
ization follows Anderson and Krathwohl
Chinese planning examination context.
At the Remember level, single-choice
factual statements about planning concep
among distractors. A planner operating
Christaller's central place theory emphas
urban-rural functions, or that suburbani
functions and population transfer to per
on discriminating accurate from inaccura
practice (Dataset, 2025).
At the Understand level, multiple-sele
tionships between planning concepts—not
theoretical logic and practical implication
Development Rights, for instance, can u
quires identifying that (a) urban function
position, land use, and industrial structu
to market fluctuations during industrial
represents spatial distribution characteri
change does affect urban hierarchy system
At the Apply level, scenarios require de
problems—calculating development capac
procedural requirements for a given proj
methods for defined problems. In the Ame
or realistic planning scenarios, such as a r
toward service-oriented functions, or a ra
fragmentation between functionally indep
to analyze transformation characteristics
recommendations grounded in relevant th

whether they can reason with planning
ansparency: most evaluations assess only
ns through which answers are produced—
nuine understanding or pattern matching.
its simultaneously.
n (ECD), a psychometric framework that
nected models: a student model specifying
evidence model defining what observable
ucts, and a task model specifying the scemond, & Lukas, 2003). In planning terms,
dge architecture described in Section 2.2;
ognitive taxonomy onto planning-specific
2001); and our task model generates asific reasoning at specified cognitive levels.
ls, each operationalized through a distinct
demands of that level. Our operational2001) revised taxonomy, adapted to the
ms test the capacity to recognize correct
theories, and institutional arrangements
this level can identify, for instance, that
s hierarchical and ordered distribution of
ion involves the relocation of urban core
eral areas. The cognitive demand centers
factual claims about planning theory and
on items assess capacity to explain relaerely defining terms but articulating their
A planner who “understands” Transfer of
rstanding urban functional evolution recan be reflected through population com-
(b) single-function cities are vulnerable
grading; and (c) functional differentiation
s, while also recognizing that functional
contra an incorrect distractor .
oying knowledge to solve specific planning
under regulatory constraints, determining
type, or selecting appropriate analytical
an context, these Q&A present real-world
urce-depleted industrial city restructuring
ly urbanizing region experiencing spatial
dent new districts, and require examinees
dentify challenges, and propose planning
y. This level tests not mere knowledge but

the capacity to operationalize that knowledge within particular project contexts.
At the Analyze level, scenarios demand critical evaluation of planning propositions,
assessing whether a stated claim about planning theory, method, or institutional arrangement is valid. For example, one item presents the proposition: "According to
general laws of urban development, towns represent a transitional form between rural settlements and cities; therefore, their development typically reflects a bottom-up
evolutionary path without planning guidance." Planners must evaluate this claim and
recognize it as false, because although towns have spontaneous elements, their spatial
form and functional evolution are often subject to explicit policy guidance, particularly
within China's "township planning" and "rural revitalization" institutional contexts .
This level tests the integrative capacity that distinguishes professional planning judgment from domain-specific technical analysis.
At the Evaluate level, scenarios require precise retrieval of domain-specific terminology embedded within contextual descriptions. For example, one scenario describes the
evolution of urban spatial structure from concentric to multi-nuclei patterns and asks
the examinee to supply "Multiple nuclei model" as the term for a spatial structure
characterized by multiple functional centers with loose interconnections, originating
from Harris and Ullman’s theory. This level most directly tests phronesis: the correct answer depends on matching the described phenomenon to its proper theoretical
formulation within planning knowledge.
3.2. Cross-National Scenario Construction
Planning knowledge is not universal but institutionally embedded—the same conceptual domain (e.g., development control) manifests through fundamentally different regulatory architectures across national contexts. A benchmark that operates within only
one institutional system cannot distinguish between planning-general and jurisdictionspecific competence. We therefore construct UPBench as a bilingual, cross-institutional
assessment that uses the American planning context as its primary evaluative frame
while systematically incorporating the Chinese planning system as a comparative institutional mirror..
The scenario construction follows a three-stage pipeline, each stage serving a distinct function in converting heterogeneous source materials into a unified, cognitively
calibrated assessment system.
Stage 1: Source Material Compilation. Because AICP examination items are not
publicly released, we needed an alternative source of domain-complete, professionally validated planning scenarios. We assembled three complementary streams: (a)
the AICP Certification Examination preparation materials and released items, representing American professional standards; (b) the Chinese National Registered Urban
Planner Examination corpus (2,150 items, 2010-2023), providing a systematic mapping
of professionally-sanctioned knowledge; and (c) graduate planning curricula from MIT,
UC Berkeley, Tongji, PKU, supplyingthe pedagogical dimension. Examination items
provide scenario-rich problem structures; curricula anchor cognitive level expectations;
the cross-national pairing ensures the resulting tasks are institutionally grounded yet
conceptually transferable.
Stage 2: Cross-Contextual Equivalence Mapping. Chinese examination items cannot
be administered to American-context without adaptation: their institutional referents
presuppose a governance architecture unfamiliar to U.S. planners. We therefore developed equivalence rules that map concepts functionally while preserving cognitive
10

demands. The principle is selective retention and replacement: transnational theories (e.g., Christaller’s central place theory, TOD principles) are retained in generic
form, whereas institution-specific instruments are replaced with their functional American counterparts. For example, China’s “one-document-three-certificates” (yi shu san
zheng) permitting system—comprising the planning opinion document, land use planning permit, construction planning permit, and construction works permit, mapping
onto the American entitlement sequence of conditional use permits, site plan approval,
subdivision plat recording, and building permits.. The cognitive demand in both contexts is identical: understanding sequential dependencies, discretionary versus ministerial actions, and the relationship between planning intent and regulatory implementation. This mapping ensures that the task tests planning reasoning, not exposure to
foreign regulatory nomenclature.
Stage 3: Scenario Generation and Validation. Planning competence is situated practical judgment (phronesis): isolated factual questions test recall, whereas scenarios force
models to activate knowledge under realistic cognitive demands. Scenario construction
also makes the model’s reasoning inspectable: each item is designed to elicit a chainof-thought (CoT) response, allowing us to evaluate whether the model’s deliberation
trajectory approximates professional planning reasoning (Wei et al., 2022; Kojima et
al., 2022).From the compiled and mapped source materials, we generated 405 assessment scenarios distributed across the 4×5 matrix. The generation process followed four
steps: (a) cognitive level tagging by two independent raters using the revised Bloom’s
taxonomy decision rules; (b) LLM-assisted scenario drafting with expert-specified reasoning pathways; (c) expert review by a five-member panel for content validity and
cognitive level accuracy; and (d) iterative refinement. The final distribution ensures
minimum coverage of 15 scenarios per task, with slight oversampling in the Governance and Practice pillars where institutional specificity creates greater variation.
3.3. Dual-Track Evaluation Protocol
Planning knowledge assessment faces a fundamental methodological tension. Licensure
examinations prioritize reliability and scalability through structured items with predetermined correct answers, but they are less suited to capturing the judgment-intensive,
open-ended reasoning that constitutes planning’s phronetic core. Human-based education assessment prioritizes validity through holistic expert evaluation of complex
project work, but sacrifices reliability and comparability across evaluators. UPBench
resolves this tension through a dual-track protocol that employs each approach where
it is epistemologically appropriate.
Track 1 (LLM-as-Judge Automated Scoring) applies to scenarios at the Remember, Understand, and Apply levels where expert-authored ground-truth answers can
be specified with reasonable precision. For each scenario, a high-capacity LLM serves
as an automated judge, scoring model responses against a structured rubric comprising
key knowledge elements, acceptable formulations, and decision rules for credit allocation.... (Zheng et al., 2023; Li et al., 2024; Liu et al., 2023; Hashemi et al., 2024). The
judge evaluates not only the Chains of Thoughts (COT), assessing logical progression,
use of planning concepts, and analytical steps, but also the final answer for factual
accuracy and policy alignment (Lightman et al., 2024; Golovneva et al., 2023). This
track enables efficient evaluation of all 25 models across hundreds of scenarios while
capturing reasoning quality beyond surface-level pattern matching (Zheng et al., 2023).
Track 2 (Expert Panel Assessment) applies to scenarios at the Analyze and Eval11

uate levels where professional judgment is required to assess response quality. A fivemember expert panel of planning academics and practicing planner independently evaluates LLM responses using rubrics that assess reasoning depth, knowledge integration,
contextual sensitivity, and professional appropriateness. Panel members also annotate
COT , identifying where LLM demonstrate genuine analytical reasoning versus surfacelevel pattern assembly.
To calibrate the two tracks, we conducted a nine-iteration prompt optimization
study in which expert panel scores for a stratified sample of 60 scenarios were compared
against automated scoring variants. Drawing on prompt-engineering best practices for
LLM evaluators (Zheng et al., 2023), each iteration refined the judge “prompt”, anchoring rubric criteria with exemplar responses to maximize alignment with human judgments. Table 1 reports the performance of each “prompt” version. The final calibration
achieves Spearman ρ = 0.67 between automated and expert scores—moderate agreement that we interpret as reflecting the genuine epistemological difference between
structured and judgment-intensive assessment rather than mere measurement error.
Following Stevens, Lyles, and Berke (2014), who established that intercoder reliability
in plan quality evaluation research typically ranges from 0.60 to 0.85, we consider this
agreement level acceptable for a framework that deliberately spans both structured
and open-ended assessment. The final composite scoring privileges the more comprehensive Track 1 coverage while incorporating the irreplaceable validity contribution of
expert judgment for higher-order tasks. The complete evaluation code is available at
https://github.com/zhuchichi56/PlanBench.
Table 1. Performance of different versions of the prompt
Prompt version MAE RMSE Spearman ρ Mean CV Mean SD Mean max. dev.
#5 Prompt 0.119 0.159 0.521 0.019 0.017 0.040
#6 Prompt 0.097 0.128 0.674 0.043 0.037 0.094
#7 Prompt 0.132 0.157 0.605 0.021 0.017 0.044
#8 Prompt 0.097 0.121 0.590 0.071 0.054 0.155
#9 Prompt 0.121 0.137 0.492 0.070 0.058 0.158
#13 Prompt 0.138 0.152 0.491 0.033 0.030 0.069
#14 Prompt 0.110 0.145 0.375 0.036 0.029 0.076
#15 Prompt 0.118 0.135 0.568 0.058 0.052 0.126
#17 Prompt 0.079 0.119 0.521 0.032 0.029 0.069
Note. MAE = mean absolute error; RMSE = root mean square error; CV = coefficient of variation; SD =
standard deviation.
3.4. Models Evaluated
We evaluate 25 LLMs, comprising 22 open-weight models and 3 proprietary API models
(GPT-4o-mini, Gemini 2.5 Flash, and Claude Haiku). The Chinese-origin open-weight
set is dominated by Alibaba’s Qwen ecosystem (12 variants spanning 0.6B to 32B), supplemented by Zhipu AI’s GLM family (glm-4-9b and chatglm3-6b), 01.AI’s Yi-6B, and
DeepSeek’s distilled reasoning models (2 variants). The US-origin open-weight set includes Meta’s Llama-3-8B-Instruct and AI2’s Llama-3.1-Tulu-3-8B, alongside Google’s
Gemma family (7B, 2-9B, 2-2B). The three proprietary models are also US-origin. The
deliberate focus on open-weight models reflects three considerations: (a) reproducibility: proprietary API models may change without notice, undermining longitudinal comparison; (b) transparency: open-weight models allow inspection of training procedures
and architectural decisions that may explain performance patterns; and (c) accessi12

bility: open-weight models are more likely to be deployed in planning agencies with
data security requirements. We acknowledge that frontier proprietary models (GPT-4o,
Claude, Gemini 2.5) likely achieve higher absolute performance; our findings should be
interpreted as characterizing the structural patterns of AI planning competence rather
than establishing current ceiling performance.
4. Findings
Table 2.: The score of UPBench's evaluation of the model (China vs. US)
Model names Remember Understand Apply Analyze Evaluate Average score
Score in the China Context
DeepSeek Family
DeepSeek-R1-Distill-Llama-8B 93.8 64.2 75.3 78.8 28.4 68.1
DeepSeek-R1-Distill-Qwen-7B 96.3 69.1 77.8 73.4 23.5 68.0
LLaMa Family
Meta-Llama-3-8B-Instruct 95.1 58.0 72.8 78.8 48.1 70.6
Llama-3.1-Tulu-3-8B 60.5 56.8 30.9 80.8 16.0 49.0
Qwen Family
Qwen3-32B 97.5 86.4 95.1 86.1 39.5 80.9
Qwen3-14B 97.5 77.8 92.6 86.8 48.1 80.6
QwQ-32B 95.1 85.2 91.4 91.9 38.3 80.4
Qwen3-8B 93.8 80.2 90.1 90.4 45.7 80.0
Qwen3-4B 95.1 72.8 90.1 89.3 46.9 78.8
Qwen3-30B-A3B 97.5 79.0 88.9 89.5 37.0 78.4
Qwen3-1.7B 95.1 79.0 76.5 85.1 34.6 74.1
Qwen2.5-3B-Instruct 98.8 66.7 92.6 64.0 29.6 70.3
Qwen2.5-7B-Instruct 98.8 70.4 81.5 65.9 30.9 69.5
Qwen2-VL-7B-Instruct 93.8 65.4 76.5 65.7 39.5 68.2
Qwen3-0.6B 90.1 55.6 46.9 74.8 12.3 55.9
Qwen2.5-0.5B-Instruct 65.4 21.0 25.9 69.4 14.8 39.3
Other evaluated LLMs
gpt-4o-mini 95.1 77.8 85.2 62.1 37.0 71.4
gemini-2.5-flash 40.7 35.8 58.0 84.0 17.3 47.2
claude-haiku-4-5-20251001 97.5 71.6 95.1 88.8 59.3 82.5
glm-4-9b-chat 91.4 72.8 84.0 79.9 38.3 73.3
Gemma-2-9B-it 96.3 75.3 90.1 67.3 33.3 72.5
Yi-6B-Chat 93.8 48.1 75.3 85.6 26.2 65.8
Gemma-2-2B-it 87.7 44.4 75.3 69.0 28.4 61.0
chatglm3-6b 80.2 37.5 44.4 58.3 21.0 48.3
Gemma-7B-it 33.3 6.2 33.3 70.8 6.2 30.0
Score in the U.S. Context
DeepSeek Family
DeepSeek-R1-Distill-Llama-8B 92.6 44.4 76.5 82.7 27.2 64.7
DeepSeek-R1-Distill-Qwen-7B 92.6 51.9 70.4 79.0 30.9 65.0
LLaMa Family
Meta-Llama-3-8B-Instruct 91.4 42.0 82.7 97.5 45.7 71.9
Llama-3.1-Tulu-3-8B 95.1 46.9 79.0 98.8 45.7 73.1
Qwen Family
Qwen3-32B 95.1 66.7 91.4 100.0 58.0 82.2
Qwen3-14B 96.3 69.1 92.6 98.8 56.8 82.7
QwQ-32B 96.3 70.0 87.7 100.0 48.1 80.4
Qwen3-8B 95.1 66.7 91.4 100.0 63.0 83.2
Qwen3-4B 92.6 58.0 84.0 97.5 54.3 77.3
Qwen3-30B-A3B 98.8 70.4 86.4 93.8 43.2 78.5
Qwen3-1.7B 96.3 49.4 81.5 77.8 43.2 69.6
Qwen2.5-3B-Instruct 95.1 48.1 84.0 80.2 40.7 69.6
13

Table 2.: The score of UPBench's evaluation of the model (China vs. US)
(continued)
Model names Remember Understand Apply Analyze Evaluate Average score
Qwen2.5-7B-Instruct 96.3 45.7 84.0 87.7 46.9 72.1
Qwen2-VL-7B-Instruct 91.4 39.5 87.7 65.4 37.0 64.2
Qwen3-0.6B 86.4 38.3 43.2 49.3 29.6 49.4
Qwen2.5-0.5B-Instruct 79.0 8.6 27.5 56.8 19.8 38.3
Other evaluated LLMs
gpt-4o-mini 97.5 56.8 87.7 92.6 43.2 75.6
gemini-2.5-flash 97.5 88.9 88.9 97.5 82.7 91.1
claude-haiku-4-5-20251001 95.1 67.9 98.8 98.8 71.6 86.4
glm-4-9b-chat 92.6 39.5 81.5 80.2 39.5 66.7
Gemma-2-9B-it 97.5 56.8 95.1 90.1 39.5 75.8
Yi-6B-Chat 80.2 24.7 64.2 86.4 39.5 59.0
Gemma-2-2B-it 88.9 24.7 88.9 86.4 30.9 64.0
chatglm3-6b 75.3 18.8 53.1 67.9 27.2 48.5
Gemma-7B-it 85.2 13.6 56.8 90.0 30.9 55.3
4.1. Aggregate Performance Landscape
Across all 25 models and 405 assessment scenarios, UPBench reveals a performance
landscape characterized by substantial variation both between models and across evaluation dimensions (Table 2). The highest-performing model (Claude-haiku) achieves
an overall composite score of 84.5% (CN+US avg), while the lowest-performing model
(Qwen2.5-0.5B-Instruct) scores 38.8%—a 45.7 percentage-point range that confirms
the framework’s discriminative capacity (Figure 1). Two initial observations merit emphasis before detailed analysis.
14

Figure 1. Model Performance Rankings on UPBench (N = 25). Horizontal bars represent composite scores averaged across Chinese and English scenario sets (405 items
each) across five cognitive levels. Blue bars = US-origin models (n = 8); red bars =
China-origin models (n = 17, including 12 Qwen variants). Claude-Haiku (proprietary,
US-origin) achieved the highest composite score (84.4%); Qwen2.5-0.5B-Instruct the
lowest (38.8%).
First, no model achieves uniformly strong performance across all cells of the 4×5
matrix. Even the best-performing model (Claude-haiku) shows a 39.5 percentage-point
spread between its strongest dimension (US-Apply, 98.8%) and weakest (CN-Evaluate,
59.3%). This pattern confirms that planning expertise is genuinely multidimensional—
strength in one domain does not predict strength in others—and validates the matrix
architecture as a meaningful decomposition of planning cognition.
Second, model parameter count shows only moderate correlation with overall performance (r = 0.547, p = 0.008), suggesting that scale alone does not determine planning
competence. Several smaller models (notably Qwen2.5-7B-Instruct and DeepSeek-R1Distill-Qwen-7B) outperform larger competitors on specific dimensions, particularly in
the Governance pillar where institutional specificity matters more than general language capability. This finding challenges the prevalent assumption that “bigger is better” and suggests that training data composition and fine-tuning strategy may matter
more than raw parameter count for domain-specific reasoning.
15

4.2. The Non-Monotonic Cognitive Curve
The most striking finding is a systematic deviation from expected performance across
cognitive levels. Conventional assumptions predict that LLMs should excel at lowerorder cognitive tasks (factual recall, comprehension) and struggle with higher-order
tasks (analysis, evaluation). UPBench reveals non-monotonic pattern in planning: Remember (89.6%) and Analyze (81.8%) are both high-performing levels, but Understand
shows catastrophic collapse (55.3%), lower than Apply (76.2%). Evaluate (37.9%) performs as expected. This pattern reveals that planning knowledge has a distinctive cognitive architecture: factual recall and analytical reasoning are both amenable to LLM
processing, but precise conceptual understanding, the ability to explain relationships
between concepts with theoretical precision, posing unique challenges.
This non-monotonic curve is not an artifact of item difficulty calibration. When we
control for expert-rated item difficulty, the pattern persists: models find it systematically easier to produce analytically-structured responses at the Analyze level than
to demonstrate precise conceptual understanding at the Understand level or reliable
procedural application at the Apply level. The gap between Remember (89.6%) and
Understand (55.3%) is the single largest cognitive-level discontinuity in the dataset,
almost a 34.3 percentage-point drop.
We interpret this pattern through four complementary mechanisms. First, institutional encoding density: what appears to be “simple” factual or conceptual knowledge
in planning is in fact densely encoded with institutional, jurisdictional, and historical
specificity (Ji et al., 2023). A correct explanation of TDR requires not just defining the
concept but situating it within property rights jurisprudence, specific enabling legislation, and implementation experience—information that may be sparse, contradictory,
or absent in training data (Salet, 2021). This finding resonates with Hendrycks’s (2021)
observation in the MMLU benchmark that performance degradation on specialized
benchmarks reflects “knowledge gaps for professional-level tasks.”
Second, pattern-matching advantage at Analyze: higher-order analytical tasks are
paradoxically more amenable to LLMs’ core capability—assembling coherent-sounding
narratives from broad patterns in training data. When asked to “analyze” the relationship between urban form and transportation outcomes, a model can draw on thousands
of academic papers, planning reports, and textbook discussions that articulate these relationships in broadly similar terms. The result reads as competent analysis even when
the underlying reasoning is pattern-matched rather than genuinely inferential, because
models may solve test items through shortcut strategies that differ from the cognitive
processes the test was designed to measure (McCoy et al., 2019; Geirhos et al., 2020).
Zoumpoulidi et al. (2025) further confirm in their BloomWise framework that LLMs
consistently overperform at the Analyze level relative to Understand, attributing this
to the "surface-level structural cues" that analytical questions provide.
Third, declarative-procedural dissociation: recent work by Li et al. (2024) demonstrates that LLMs store factual knowledge in a declarative format that supports accurate retrieval (Remember) but struggle when required to transform that knowledge into
relational understanding (Understand). Their taxonomy evaluation framework shows
that models consistently achieve higher accuracy on “what” questions than “why” questions that probe the same underlying concepts—a pattern we observe across all 25 models. The Understand level demands not merely recalling isolated facts but articulating
the relationships between concepts (e.g., explaining why Euclidean zoning produces
segregated land uses rather than simply defining it), a transformation that exposes
gaps in the structuredness of encoded knowledge.
16

This finding challenges the linear hierarchy assumed by Bloom’s taxonomy when
applied to planning. Planning cognition may operate not as a ladder (where each level
builds sequentially on the previous) but as what Gadamer (1975) terms a hermeneutic
circle—where understanding, application, and analysis are mutually constitutive rather
than hierarchically ordered. LLMs, which process all levels through the same statistical mechanism, expose this non-linearity precisely because they lack the recursive
experiential loop that integrates levels in human expertise.
Figure 2. The Non-Monotonic Cognitive Curve: The Understand-Level Collapse.
Bars show mean accuracy across 25 models (CN+US combined) at each cognitive level.
The dashed line shows the expected declining gradient from Bloom’s taxonomy; the solid
red line shows the actual U-shaped pattern. Note the 34.3 percentage-point drop from
Remember (89.6%) to Understand (55.3%), followed by recovery at Apply (76.2%) and
Analyze (81.8%).
4.3. Knowledge Domain Asymmetries
Performance varies across the four knowledge pillars, revealing a gradient from highest to lowest: Cross-Disciplinary Integration (mean: 69.3%) > Planning Governance
(mean: 68.8%) > Principles of Urban Planning (mean: 67.6%) > Planning Practice
(mean: 65.6%). This gradient maps directly onto the Aristotelian knowledge typology:
models perform best on techne-adjacent knowledge (cross-disciplinary synthesis), adequately on episteme (theoretical understanding), and poorly on phronesis-intensive
domains (governance and practice). The 3.7 percentage-point gap between the highest
and lowest pillars confirms that AI competence in planning is structurally more even
than previously assumed, though subtle differences persist.
Within Principles of Urban Planning, models demonstrate strong command of
canonical frameworks—correctly explaining the Harris-Ullman multiple nuclei model,
the bid-rent curve, or the four-step transportation model. However, they struggle with
the application of these frameworks to specific contexts: when asked to use central
place theory to analyze the retail hierarchy of a particular metropolitan area, models
produce generic textbook explanations rather than context-sensitive analytical applications. This pattern—strong on canonical knowledge, weak on contextual application—
17

recurs across the pillar and suggests that LLMs have effectively memorized textbook
content without developing the capacity to deploy it flexibly.
Cross-Disciplinary Integration is where models most consistently approximate professional competence. When asked to synthesize environmental, transportation, and
equity considerations in analyzing a transit corridor, models produce responses that
expert panelists rate as “adequate for preliminary analysis”, drawing on multiple disciplinary literatures and identifying relevant interactions. This relative strength likely
reflects the abundance of interdisciplinary planning literature in training data and
the structural similarity between academic literature reviews (which models excel at
mimicking) and cross-disciplinary analytical integration.
Planning Governance reveals moderate within-pillar variation across cognitive levels. At the Remember level, models achieve high accuracy (mean: 93.3%) on regulatory
concepts that are extensively documented online. At the Apply level, however, performance drops to 76.3%, revealing what we term “regulatory hallucination”: models
confidently fabricate specific regulatory requirements that do not exist, blending elements from different jurisdictions or time periods into plausible-sounding but factually
incorrect responses.
Planning Practice emerges as the most resistant pillar to AI approximation, though
the gap is modest (3.7 % below Cross-Disciplinary Integration). Even at the Analyze
level, where models generally perform well, Planning Practice scenarios yield mean
scores of 81.8%, comparing to 83.6% for Governance at the same cognitive level. Expert panelists consistently identify a qualitative difference in response character: where
models produce competent-sounding analysis of theoretical systems interactions, they
struggle to produce the kind of situated, strategic, politically-aware reasoning that
characterizes professional planning practice. The gap is most pronounced in scenarios
requiring stakeholder analysis, implementation sequencing, or negotiation strategy—
precisely the phronetic skills that Flyvbjerg (2001) identifies as planning’s distinctive
contribution.
Figure 3. Accuracy Heatmap: Cognitive Level × Knowledge Pillar. Values represent
mean accuracy (%) across all 25 models, CN+US combined. Cell color indicates performance (green = high, red = low). Note the consistent Understand-level depression
18

(yellow band, second row) across all four p
mance at the Analyze level (bottom row).
Figure 4. Comparison of Original Fin
Data (blue bars). The original findings s
with errors ranging from -3.1% (Cross-D
Verified data show a much more compresse
claimed (48.2%–72.4%).
4.4. Four Epistemic Diagnostics
Beyond aggregate performance patterns, q
four characteristic failure modes that we
terns of reasoning breakdown that illumin
that resist computational replication (Ap
Regulatory Hallucination: The Fa
The most frequent failure mode involv
quirements, procedural standards, or leg
structed from plausible elements of real
ument in their comprehensive survey of h
LLMs exhibit a particular form of "fact h
training data contains abundant surface
institutional specifics.
A representative example from UPben
evaluate a statement about Chinese town
correctly identified it as false, reasoning t
enced by policies such as ‘township plann
ing accurate institutional knowledge. In
acknowledged the complexity but ultimat
Chinese institutional context that contrad
models that encode institutional specific
the hallmark of regulatory hallucination..
This failure mode is particularly insidio

ars and the relatively uniform high perforgs Pillar Means (red bars) with Verified
stantially underestimated all four pillars,
iplinary) to -17.4% (Planning Practice).
istribution (65.6%–69.3%) than originally
itative analysis of model responses reveals
m epistemic diagnostics—systematic patspecific dimensions of planning knowledge
ndix A) .
cation of Institutional Authority
models generating specific regulatory recitations that do not exist but are conulatory systems. As Ji et al. (2023) docucination in natural language generation,
ucination" in professional domains where
el patterns but insufficient grounding in
( Apply level, Principles pillar): asked to
velopment planning policy, Claude-Haiku
t “town development is significantly influg’ and ‘rural revitalization’ ”, demonstratntrast, Qwen2.5-0.5B-Instruct (incorrect)
answered “True”, failing to recognize the
s the statement. This divergence between
nd those that rely on generic patterns is
because it produces responses that appear

authoritative—complete with specific num
making errors difficult to detect without j
Salet (2021) identifies as the constructed
ulatory meaning is not inherent in texts
within specific institutional contexts.
Conceptual Conflation: The Erosi
Models frequently blur the boundar
concepts—treating them as interchangea
tinctions that theoretical clarity requires
Understand level (55.3% mean accuracy)
tween concepts rather than simply define
A characteristic example (Understand l
correct statements about historical urban
nized that “medieval European urban d
and spatial order” was false, accurately d
from modernist functionalist planning. H
incorrectly accepted this statement, confla
This failure mode reflects what Allmendin
pluralism of planning theory: the discip
concepts that appear similar but carry f
mitments, historical lineages, and practica
where these concepts appear in overlapp
to maintain these distinctions consistentl
Wickedness Paralysis: The Retrea
When confronted with genuinely wicke
imate values conflict and no technical re
acteristic paralysis: they enumerate cons
the normative commitments that professio
instantiates the Rittel and Webber (1973
planner to take a position, accepting resp
objectively justified.
Models, trained to produce balanced a
avoid this essential professional act. A sc
that pits neighborhood preservation agai
sponses that typically list all relevant fac
equity, property rights, precedent effects)
as “the decision should balance all stake
reasoned professional recommendation. T
insistence that phronesis is inseparable fr
ner does not merely identify consideration
weight in particular circumstances.
Phronetic Deficit: The Absence of
The deepest failure mode—and the on
tematic absence of what we recognize,
as situated practical wisdom. This mani
qualitative absence of the tacit, experienc
professional judgment.
When asked to evaluate a comprehensiv
on accumulated experience with commun
tation barriers, and the gap between plan

ers and apparent procedural confidence—
sdiction-specific expertise. It reflects what
ture of legal-institutional knowledge: regt produced through interpretive practice
of Theoretical Precision.
between related but distinct planning
rather than maintaining the precise dishis failure mode is most prevalent at the
here models must explain differences beem.
l, Principles pillar): when asked to identify
velopment, Claude-Haiku correctly recoglopment was based on functional zoning
nguishing medieval organic urban growth
ever, Qwen3-32B and GPT-4o-mini both
g historically distinct planning paradigms.
r (2017) characterizes as the paradigmatic
’s theoretical landscape is populated by
damentally different epistemological commplications. LLMs, trained on text corpora
contexts, lack the theoretical scaffolding
rom Normative Commitment.
planning problems—where multiple legitution is possible—models exhibit a charrations exhaustively but refuse to make
l judgment requires. This pattern directly
ormulation—wicked problems require the
sibility for a value choice that cannot be
non-controversial outputs, systematically
ario presenting a zoning variance request
affordable housing production elicits res (community character, housing supply,
t conclude with equivocal statements such
der interests” rather than articulating a
pattern resonates with Flyvbjerg’s (2004)
value commitment—the phronetic planut exercises judgment about their relative
ituated Practical Wisdom.
most theoretically significant—is the sysowing Schön (1992a) and Xiang (2016),
ts not as specific factual errors but as a
ased knowledge that characterizes expert
plan update process, expert planners draw
dynamics, political feasibility, implemenhetoric and on-the-ground reality. Models

produce responses that are formally ade
citing appropriate literature—but lack w
“practical wisdom” or “professional sense.
theorists have described as the practical,
sional judgment: the capacity to read situ
relations and implementation constraints
rigor and human sensitivity (Forester, 198
2004; Campbell, 2012). It is, by definition
resistant to computational replication: phr
rience within institutional and community
data can substitute. Concrete instantiated
in Appendix B.
4.5. Cross-National Institutional A
UPBench’s bilingual architecture reveals
tween American and Chinese planning co
overall gap (3.2 %, US higher), but its ne
origin models show a mean US advantage
a near-zero gap of -1.7 %.
This pattern points to training data
nism. LLMs acquire planning knowledge d
texts most represented in their training
Gemini, Llama, Gemma) are trained pr
documentation—including American zoni
tal review documents, and academic lite
as default assumptions. When confronted
knowledge of the 2019 Ministry of Natur
spatial planning system, these models lac
curately.
Conversely, China-origin models (Qwe
pora with more balanced Chinese-Englis
comparably across both institutional con
cross-cultural analysis of NLP model pe
perform systematically better on tasks dr
tural and linguistic context.
The origin effect has important implica
zero cross-national gap among China-orig
sification, rather than model architecture
cultural performance. This finding challe
model can serve all planning contexts eq
edge gaps may persist even as general lan
2021; Li et al., 2024).
Three models merit specific attention. G
tage (+43.9 %), suggesting that Google's
centric despite the model's multilingual m
Gemma-7B-it (+25.1%) also show substan
ing on predominantly English corpora. A
Yi-6B (-6.7%) actually favor Chinese sce

ate—mentioning relevant considerations,
expert panelists consistently describe as
This deficit corresponds to what planning
oral, and relational dimensions of profesed community dynamics, recognize power
uild trust, and act with both analytical
1999, 2009; Schön, 1983; Flyvbjerg, 2001,
he dimension of planning knowledge most
esis is constituted through embodied expentexts that no amount of textual training
xamples of each failure mode are provided
mmetry
tematic differences in AI performance beexts. The most striking finding is not the
complete mediation by model origin: US-
+13.6 %, while China-origin models show
mposition as the primary causal mecharoportionately from the institutional conrpora. US-origin models (Claude, GPT,
ominantly on English-language planning
codes, comprehensive plans, environmenure—that embeds US planning concepts
with Chinese planning scenarios requiring
Resources restructuring or the integrated
he institutional grounding to respond acDeepSeek, GLM, Yi) are trained on corepresentation, enabling them to perform
t. This finding aligns with Aher’s (2023)
mance, which demonstrates that models
n from their training data's dominant culns for planning AI deployment. The nearmodels suggests that training data diverscale,which is the key to equitable crosses the assumption that a single “global”
ly, and suggests that institutional knowlge capabilities improve (Hendrycks et al.,
mini-2.5-Flash shows the largest US advanaining data may be particularly Englisheting. Llama-3.1-Tulu-3-8B (+24.1%) and
l asymmetries, consistent with their trainhe other extreme, GLM-4-9B (-7.1%) and
rios, reflecting their training on Chinese-

dominated corpora.
These findings do not support the previous interpretation attributing cross-national
gaps to “institutional stability” or “administrative discretion” differences between the
two planning systems. While these factors may play a role at the margin, the nearperfect alignment between model origin and performance gap suggests that training
data composition is the dominant explanatory variable.
Figure 5. Cross-Lingual Performance Gap: US vs. Chinese Scenarios (7 Focus Models). Bars show the performance difference (US accuracy minus CN accuracy) for each
model. Red bars indicate stronger performance on US scenarios; blue bars indicate
stronger performance on Chinese scenarios. Gemini-2.5-Flash shows the largest US
advantage (+43.9 pp), while Yi-6B shows a Chinese advantage (-6.6 pp).
5. Discussion
5.1. What LLMs Reveal About Planning Knowledge Itself
The inverted cognitive gradient is not merely a finding about AI performance; it is
a finding about the structure of planning knowledge itself. By revealing where AI
reasoning systematically breaks down, UPBench functions as what we have termed
an epistemic mirror—reflecting back the architecture of the knowledge it attempts to
replicate. Three theoretical implications emerge from this reflection.
First, the gradient challenges the linear application of Bloom’s taxonomy to planning cognition. The 34.3% drop from Remember (89.6%) to Understand (55.3%)—the
largest cognitive-level discontinuity in our dataset, reveals that "understanding" in
planning requires capabilities fundamentally different from factual recall or analytical
synthesis. In planning, however, This can be interpreted through the lens of knowledge architecture (Li et al., 2024): LLMs store planning knowledge as an unstructured
associative network where concepts are linked by co-occurrence statistics rather than
organized by theoretical relationships. Remember level succeed because they activate
isolated nodes; Analyze-level tasks succeed by leveraging associative richness to synthesize plausible narratives. But Understand-level tasks fail because they require traversing
structured relationships between concepts, explaining why Euclidean zoning produces
22

segregation demands linking the concept to property rights theory, political economy,
and implementation history in ways that LLMs' associative architecture cannot reliably
reconstruct.
Second, our four epistemic diagnostics collectively map the boundaries of what we
term computational phronesis—the outer limit of planning-relevant reasoning that
can be achieved through statistical language modeling. Regulatory hallucination reveals the boundary of institutional knowledge: models cannot reliably access the
jurisdiction-specific, temporally-indexed knowledge that regulatory interpretation requires. Conceptual conflation reveals the boundary of theoretical precision: models
cannot maintain the paradigmatic distinctions that planning’s theoretical pluralism
demands. Wickedness paralysis reveals the boundary of normative commitment: models cannot take value positions that phronetic judgment requires. And phronetic deficit
reveals the boundary of situated wisdom: models cannot replicate the tacit, experiencebased knowledge that constitutes expertise. From a relational and assemblage perspective, these limitations are not merely individual cognitive failures but reflect the absence of the socio-material conditions through which planning judgment emerges: the
networked relations among actors, institutions, routines, technologies, conflicts, places,
and material contexts (Hillier, 2007; McFarlane, 2011; Davoudi, 2015).
Third, the cross-national asymmetry reveals that planning knowledge is not merely
context-dependent but institutionally constituted. The training data origin effect,
where US-origin models systematically underperform on Chinese scenarios (mean gap:
12.7 %) while China-origin models achieve near-zero cross-national gaps. It cannot be
explained solely by training data volume. It reflects a deeper epistemological point:
planning knowledge does not exist as abstract propositions translatable between contexts, but as institutionally-embedded practices whose meaning is inseparable from
specific governance architectures.
These findings reframe the relationship between AI and planning knowledge. Rather
than asking “how much of planning can AI do?” (a quantitative question), the more
productive question is “what kind of knowledge does AI’s failure reveal planning to
be?” (a qualitative, epistemological question). The answer our findings suggest is that
planning knowledge is irreducibly institutional, normative, temporal, and relational—
not despite but because of its apparent simplicity at the factual level. The practitioners
who navigate zoning codes, negotiate stakeholder conflicts, and sequence implementation strategies are not performing simple tasks that AI will soon replicate; they are
exercising a form of institutional intelligence that is constituted through embeddedness
rather than computation.
5.2. Redefining the Human-AI Boundary in Planning Practice
Findings provides an empirical foundation for what we call differential delegation: a
principled framework for determining which planning tasks can be responsibly augmented by AI and which require irreducibly human professional judgment. UPBench
moves beyond the binary discourse of AI-as-threat versus AI-as-tool, toward a nuanced
mapping of complementary capabilities.
In the zone of demonstrated competence (Remember and Analyze levels across Theory and Interdisciplinary pillars), AI augmentation offers genuine productivity gains
with manageable risk. Tasks such as literature review, preliminary environmental scanning, cross-disciplinary impact identification, and scenario generation can be productively delegated to AI systems with standard professional review. The key insight here
23

is not that AI performs these tasks perfectly, but that it performs them at a level where
the cost of professional review is less than the cost of producing the initial analysis
from scratch. This zone corresponds to planning’s techne dimension—technical synthesis that benefits from breadth of reference but does not require deep institutional
judgment.
In the zone of qualified utility (Apply level in select pillars), AI can serve as a drafting assistant rather than an autonomous analyst. The workflow here is collaborative:
AI produces first drafts that professional planners substantially revise, verify against
jurisdictional specifics, and contextualize to local circumstances. This zone requires
what we term structured verification protocols—explicit procedures for checking AI
outputs against authoritative sources before any professional reliance. The boundary
between Zone 1 and Zone 2 is determined by error consequence severity: Zone 2 tasks
involve higher stakes where errors could undermine due process or stakeholder rights.
In the zone of persistent incapacity (regulatory interpretation, normative judgment,
implementation strategy), AI delegation poses unacceptable professional risk. The
failure modes documented in Section 4.4—particularly regulatory hallucination and
wickedness paralysis—create dangers that are qualitatively different from simple inaccuracy: they produce outputs that appear authoritative while being fundamentally
misleading, potentially undermining due process, stakeholder rights, and public trust.
Following Cook and Karvonen (2024) on the knowledge politics of urban technology,
we argue that the decision to deploy AI in these domains is not merely technical but
political—it involves choices about whose knowledge counts, what forms of reasoning
are legitimate, and who bears responsibility for judgment failures.
Critically, this framework is not static. The boundaries between zones will shift as AI
capabilities evolve—though our findings suggest that the zone of persistent incapacity
corresponds to structural features of planning knowledge (institutional embeddedness,
normative pluralism, democratic accountability) rather than merely current computational limitations. Longitudinal reassessment using updated UPBench versions will be
essential for tracking these shifts and updating delegation protocols accordingly.
5.3. Implications for Planning Education
If AI can already approximate professional competence in cross-disciplinary synthesis
and broad analytical reasoning (Analyze: 81.8%), the implications for planning education are profound. However, the Understand collapse reveals a critical nuance: AI can
perform well at ostensibly “higher” cognitive levels while failing at conceptual understanding. This suggests planning education should not simply retreat from analytical
training, but reorient toward competencies that resist automation precisely because
they require structured theoretical relationships and institutional embeddedness.
Our findings suggest four areas where planning education should intensify its investment. First, institutional literacy: the capacity to navigate specific regulatory architectures, interpret ambiguous legal-institutional contexts, and understand the gap between
codified rules and enacted practice. This corresponds to the domain where regulatory
hallucination is most dangerous—and where deep familiarity with specific institutional
contexts provides irreplaceable value. Salet’s (2021) concept of “constructing legality”
through professional practice captures precisely this competence: understanding that
legal-institutional meaning is not given in texts but produced through interpretive
practice.
Second, paradigmatic precision: the capacity to maintain clear theoretical distinc24

tions between related but different planning concepts, frameworks, and paradigms—
resisting the conceptual conflation that characterizes AI outputs. This requires not
superficial familiarity with many theories but deep understanding of how specific theoretical commitments produce different analytical conclusions and practical recommendations. Allmendinger’s (2017) mapping of planning theory’s paradigmatic landscape
provides a pedagogical framework for this cultivation.
Third, normative courage: the capacity to take reasoned value positions on contested
planning issues—engaging with wickedness rather than retreating into exhaustive but
uncommitted enumeration of considerations. This corresponds directly to what Campbell (2012) identifies as planning ethics being constitutive of professional judgment: the
ethical dimension is not separate from the analytical one but integral to it. Flyvbjerg
(2004) insists that phronetic judgment necessarily involves taking positions on matters
where objective resolution is impossible—precisely the competence that wickedness
paralysis reveals AI to lack.
Fourth, AI critical literacy: the meta-competence to evaluate AI outputs with professional judgment—recognizing when AI-generated analysis is adequate for professional
use and when it conceals hallucination, conflation, or normative evasion beneath surface fluency. Clayton, Goodspeed, and colleagues (2025) argue that digital-era planning
education requires new pedagogical approaches that go beyond analytical skill—our
findings suggest that one such approach must be the systematic cultivation of critical
judgment about AI outputs as a core professional competence.
Taken together, these four educational priorities represent a reorientation from
knowledge transmission toward phronetic cultivation (Xiang, 2016), developing practical wisdom through experiential engagement with institutional complexity, value plurality, and situated practice. This does not mean abandoning analytical training; it
means reframing analytical competence as necessary but insufficient for professional
planning practice, and investing correspondingly in the relational, institutional, and
normative dimensions that our findings reveal as planning’s distinctive and durable
contribution.Planning education must therefore cultivate not just what students know,
but how they know differently from machines.
5.4. Limitations and Future Research
Several limitations of this study should be acknowledged. First, the evaluation relies
on automated scoring that may not capture all dimensions of response quality. While
we validated the scoring rubric against expert ratings, subtle distinctions in reasoning quality may elude automated assessment. Second, the bilingual evaluation uses
translated scenarios that may not perfectly capture the conceptual nuances of Chinese planning practice. Third, the model selection reflects availability at the time of
evaluation and does not include the most recent model generations.
Future research should extend the UPBench framework in three directions. First,
longitudinal evaluation: tracking how model performance evolves across model generations to assess whether the Understand collapse and phronetic deficit are transient
limitations or persistent boundary conditions. Second, expanded institutional contexts:
adding planning scenarios from additional national contexts (European, Global South)
to test the generalizability of the origin effect. Third, human-AI collaborative assessment: evaluating not just AI performance in isolation but the quality of human-AI
collaborative planning processes, which may reveal productive complementarities not
visible in standalone evaluation.
25

6. Conclusion
Can AI reason like an urban planner? Our findings suggest an answer more nuanced
than either techno-optimism or professional defensiveness would allow. LLMs can approximate certain dimensions of planning reasoning—particularly cross-disciplinary
synthesis and broad analytical integration—at levels that suggest productive augmentation potential. But they systematically fail at the dimensions that constitute
planning’s phronetic core: jurisdiction-specific institutional interpretation, normative
judgment under value plurality, context-sensitive procedural application, and the situated practical wisdom that emerges from embodied professional experience (Tsai &
Ku, 2024). The inverted cognitive gradient—where AI struggles more with planning’s
“simple” institutional knowledge than with its “complex” analytical tasks—reveals that
planning expertise is structured differently from other professions, with ostensibly
lower-order knowledge encoding the highest density of institutional complexity (Flyvbjerg, 2001; Healey, 1997).
This paper’s contributions operate at three levels. Methodologically, UPBench provides the first comprehensive, theory-grounded framework for evaluating AI planning competence—constructed from within planning’s own evaluative traditions rather
than imported from computer science. Theoretically, the four epistemic diagnostics—
regulatory hallucination, conceptual conflation, wickedness paralysis, and phronetic
deficit—advance our understanding of planning knowledge by empirically demonstrating its irreducibly institutional, normative, and relational character (Forester, 1989;
Healey, 1997; Innes & Booher, 1999). Practically, the differential delegation framework
provides planning agencies, educators, and policymakers with an evidence-based tool
for navigating the human-AI boundary in professional practice (Tsai & Ku, 2024).
Several limitations warrant acknowledgment and point toward future research. First,
our focus on open-weight models means that current frontier proprietary systems
(GPT-4o, Claude, Gemini) likely achieve higher absolute performance (Evkarpidi &
Tutubalina, 2025); future work should extend UPBench to these systems while maintaining the open-weight baseline for longitudinal tracking. Second, our expert panel
(n=5), while sufficient for exploratory framework development, should be expanded in
future iterations to strengthen reliability claims (Okoli & Pawlowski, 2004). Third, UPBench’s scope—limited to two national contexts and text-based assessment—excludes
important dimensions of planning expertise including visual-spatial reasoning, interpersonal facilitation, and embodied site knowledge; multimodal extensions are a natural
next step (Zhu et al., 2025). Fourth, our findings represent a temporal snapshot of
rapidly evolving AI capabilities; the framework is designed for longitudinal reassessment, and we anticipate that zone boundaries will shift over successive evaluation
cycles.
Future research should pursue five directions: (a) longitudinal tracking of AI planning competence as model capabilities evolve, using UPBench as a consistent measurement instrument; (b) expansion to additional national planning systems (European,
Latin American, Southeast Asian) to further map how institutional embeddedness
shapes AI performance (Flyvbjerg, 2001); (c) qualitative studies of how practicing
planners actually interact with AI tools, to ground the differential delegation framework in observed practice rather than measured capability alone; (d) investigation of
whether domain-specific fine-tuning can address the identified failure modes, or whether
they reflect structural limitations of language-model architecture; and (e) comparative
analysis across professions (planning versus architecture, law, public health) to identify
what is distinctively challenging about planning for AI systems.
26

We conclude with a reflection on wh
knowledge practice. The fact that AI mo
cal and synthetic dimensions—while faili
tional dimensions—suggests that what ma
analytical sophistication (which technolo
institutional judgment (which emerges on
nance contexts, communities, and politica
competent-sounding analysis on demand,
not in what it knows but in how it know
commitment, democratic accountability, a
training corpus can substitute. The episte
with empirical clarity, what planning theo
most essential contribution is not technica
this judgment remains, for now and perha
ment.
7. References
Aher, G. V., et al. (2023). Using large la
and replicate human subject studies. Proc
on Machine Learning (ICML). https://d
American Institute of Certified Plann
Content outline and preparation material
Alexander, E. R. (2022). On plann
critical reflection. Planning Theory, 21
14730952211066341
Allmendinger, P. (2017). Planning the
//doi.org/10.1007/978-1-137-54421-1
Anderson, L. W., & Krathwohl, D. R. (E
ing, and assessing: A revision of Bloom’s t
Batty, M. (2018). Artificial intelligenc
ning B: Urban Analytics and City Scien
2399808317751169
Berke, P., & Godschalk, D. (2009). Se
of plan quality studies. Journal of Plannin
org/10.1177/0885412208327014
Berlin, I. (1969). Four essays on liberty
Booth, P. (1996). Controlling developm
USA and Hong Kong. UCL Press.
Booth, P. (2007). The control of discret
Planning Theory, 6 (2), 127–145.
Campbell, H. (2012). Planning ethics a
ning Theory, 11 (4), 379–399. https://do
Chang, Y., et al. (2024). A survey on
Transactions on Intelligent Systems and
10.1145/3641289
Clayton, P., et al. (2025). More than a
fessionals to shape today’s digital cities. J
45 (4), 726–732. https://api.semantics

this study reveals about planning as a
readily approximates planning’s analytiat its institutional, normative, and relas planning genuinely professional is not its
increasingly provides) but its integrative
through embeddedness in specific goverealities). In an era where AI can produce
anning’s distinctive value proposition lies
through contextual sensitivity, normative
the accumulated practical wisdom that no
c mirror of AI benchmarking reflects back,
ts have long argued: that this profession’s
nalysis but phronetic judgment—and that
inherently, a distinctively human achieveuage models to simulate multiple humans
ings of the 40th International Conference
.org/10.48550/arXiv.2208.10264
(2023). AICP certification examination:
American Planning Association.
g, planning theories, and practices: A
), 181–211. https://doi.org/10.1177/
y (3rd ed.). Palgrave Macmillan. https:
.). (2001). A taxonomy for learning, teachonomy of educational objectives. Longman.
nd smart cities. Environment and Plan45 (1), 3–6. https://doi.org/10.1177/
hing for the good plan: A meta-analysis
Literature, 23 (3), 227–240. https://doi.
Oxford University Press.
t: Certainty and discretion in Europe, the
: Planning and the common-law tradition.
rediscovering the idea of planning. Planorg/10.1177/1473095212442159
aluation of large language models. ACM
hnology, 15 (3), 1–45. https://doi.org/
lytics: Five approaches to educating prornal of Planning Education and Research,
olar.org/CorpusID:270641642

Cook, M., & Karvonen, A. (2024). Urban planning and the knowledge politics of the smart city. Urban Studies, 61 (2), 370–382. https://doi.org/10.1177/
00420980231177688
Darnell, C., et al. (2022). A multifunction approach to assessing Aristotelian phronesis, or practical wisdom. Personality and Individual Differences, 196, Article 111714.
Davidoff, P. (1965). Advocacy and pluralism in planning. Journal of the
American Institute of Planners, 31 (4), 331–338. https://doi.org/10.1080/
01944366508978187
Davoudi, S. (2015). Planning as practice of knowing. Planning Theory, 14 (3), 316–
331. https://doi.org/10.1177/1473095215575919
Dell’Acqua, F., et al. (2023). Navigating the jagged technological frontier: Field experimental evidence of the effects of AI on knowledge worker productivity and quality.
Harvard Business School Technology & Operations Mgt. Unit Working Paper, (24-013).
Dreyfus, H. L., & Dreyfus, S. E. (1986). Mind over machine: The power of human
intuition and expertise in the era of the computer. Basil Blackwell.
Evkarpidi, N., & Tutubalina, E. (2025). Bridging the gap between open-source and
proprietary LLMs in table QA. Proceedings of the 19th International Workshop on
Semantic Evaluation (SemEval-2025), 38–53. https://arxiv.org/abs/2506.09657
Flyvbjerg, B. (1998). Rationality and power: Democracy in practice. University of
Chicago Press.
Flyvbjerg, B. (2001). Making social science matter: Why social inquiry fails and how
it can succeed again. Cambridge University Press.
Flyvbjerg, B. (2004). Phronetic planning research: Theoretical and methodological
reflections. Planning Theory & Practice, 5 (3), 283–306. https://doi.org/10.1080/
1464935042000250195
Forester, J. (1989). Planning in the face of power. University of California Press.
Forester, J. (1999). The deliberative practitioner: Encouraging participatory planning
processes. MIT Press.
Forester, J. (2009). Dealing with differences: Dramas of mediating public disputes.
Oxford University Press.
Forester, J. (2017). Planning in the face of conflict: The surprising possibilities of
facilitative leadership. Routledge.
Frank, A. I. (2006). Three decades of thought on planning education. Journal of
Planning Literature, 21 (2), 131–144. https://doi.org/10.1177/0885412206288904
Gadamer, H.-G. (1975). Truth and method (J. Weinsheimer & D. G. Marshall,
Trans.). Seabury Press. (Original work published 1960)
Geertman, S., & Stillwell, J. (2004). Planning support systems: An inventory of
current practice. Computers, Environment and Urban Systems, 28 (4), 291–310. https:
//doi.org/10.1016/S0198-9715(03)00024-3
Geirhos, R., et al. (2020). Shortcut learning in deep neural networks. Nature Machine
Intelligence, 2 (11), 665–673. https://doi.org/10.1038/s42256-020-00257-z
Golovneva, O., et al. (2023). ROSCOE: A suite of metrics for scoring step-by-step
reasoning. In The Eleventh International Conference on Learning Representations.
OpenReview.net. https://openreview.net/forum?id=xYlJRpzZtsY
Guha, N., et al. (2023). LegalBench: A collaboratively built benchmark for measuring
legal reasoning in large language models. Advances in Neural Information Processing
Systems, 36. https://arxiv.org/abs/2308.11462
28

Hashemi, H., et al. (2024). LLM-rubric: A multidimensional, calibrated approach
to automated evaluation of natural language texts. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)
(pp. 13871–13891). Association for Computational Linguistics. https://doi.org/10.
18653/v1/2024.acl-long.745
Healey, P. (1992). A planner’s day: Knowledge and action in communicative practice.
Journal of the American Planning Association, 58 (1), 9–20. https://doi.org/10.
1080/01944369208975531
Healey, P. (1997). Collaborative planning: Shaping places in fragmented societies.
UBC Press.
Healey, P. (2006). Relational complexity and the imaginative power of strategic
spatial planning. European Planning Studies, 14 (4), 525–546. https://doi.org/10.
1080/09654310500421196
Healey, P. (2009). The pragmatic tradition in planning thought. Journal of
Planning Education and Research, 28 (3), 277–292. https://doi.org/10.1177/
0739456X08325175
Hendrycks, D., et al. (2021). Measuring massive multitask language understanding.
arXiv. https://arxiv.org/abs/2009.03300
Hillier, J. (2017). Stretching beyond the horizon: A multiplanar theory of spatial
planning and governance. Routledge.
Hoch, C. (2019). Pragmatic spatial planning: Practical theory for professionals. Routledge.
Innes, J. E., & Booher, D. E. (1999). Consensus building as role playing and bricolage: Toward a theory of collaborative planning. Journal of the American Planning
Association, 65 (1), 9–26. https://doi.org/10.1080/01944369908976031
Ji, Z., et al. (2023). Survey of hallucination in natural language generation. ACM
Computing Surveys, 55 (12), Article 248. https://doi.org/10.1145/3571730
Kitchin, R. (2016). The ethics of smart cities and urban science. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences,
374 (2083), 20160115. https://doi.org/10.1098/rsta.2016.0115
Klosterman, R. E. (1997). Planning support systems: A new perspective on
computer-aided planning. Journal of Planning Education and Research, 17 (1), 45–54.
Kojima, T., et al. (2022). Large language models are zero-shot reasoners. Advances
in Neural Information Processing Systems, 35, 22199–22213.
Kristjánsson, K. (2015). Aristotelian character education. Routledge. https://doi.
org/10.4324/9781315752747
Li, H., et al. (2024). LLMs-as-judges: A comprehensive survey on LLM-based evaluation methods. arXiv preprint arXiv:2412.05579. https://doi.org/10.48550/arXiv.
2412.05579
Lightman, H., et al. (2024). Let’s verify step by step. Proceedings of the 12th International Conference on Learning Representations (ICLR). https://openreview.net/
forum?id=v8L0pN6EOi
Liu, Y., et al. (2023). G-Eval: NLG evaluation using GPT-4 with better human
alignment. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (pp. 2511–2522). Association for Computational Linguistics.
Lyles, W., & Stevens, M. (2014). Plan quality evaluation 1994–2012: Growth and
contributions, limitations and opportunities. Journal of Planning Education and Research, 34 (4), 433–450. https://doi.org/10.1177/0739456X14549752
29

McCoy, R. T., Pavlick, E., & Linzen,
agnosing syntactic heuristics in natural
Annual Meeting of the Association for Co
//doi.org/10.18653/v1/P19-1334
McFarlane, C. (2011). The city as asse
ment and Planning D: Society and Space,
d4710
Mislevy, R., Almond, R., & Lukas, J
centered design. ETS Research Report Se
j.2333-8504.2003.tb01908.x
Mittelstadt, B. D., et al. (2016). The e
Data & Society, 3 (2), 1–21. https://doi
Monkkonen, P., & Manville, M. (202
hydra. Journal of the American Planning
org/10.1080/01944363.2020.1725255
Ni, H., Wang, Y., & Liu, H. (2024). P
LLM-based framework for cyclical urban
Okoli, C., & Pawlowski, S. D. (2004).
example, design considerations and appli
15–29. https://doi.org/10.1016/j.im.
Planning Accreditation Board. (2022)
grams. PAB.
Planning Institute of Australia. (202
framework. PIA.
Pelzer, P. (2017). Usefulness of plannin
and an empirical illustration. Transporta
104, 84–95. https://doi.org/10.1016/j
Polanyi, M. (1966). The tacit dimensio
Rittel, H. W. J., & Webber, M. M. (197
Policy Sciences, 4 (2), 155–169. https://
Rong, H. H., Davis, J., & Rada-Orella
models against qualitative coding and na
lic sentiment on urban upzoning. Urban I
1007/s44212-025-00083-x
Royal Town Planning Institute. (2023)
fessional development framework. RTPI.
Rydin, Y. (2007). Re-examining the rol
ning Theory, 6 (1), 52–68. https://doi.o
Salet, W. (2018). Public norms and as
Routledge.
Salet, W. (2021). The construction of
Planning Theory. https://doi.org/10.1
Sanchez, T. W., Brenman, M., & Ye,
intelligence in urban planning. Journal o
294–307. https://doi.org/10.1080/019
Sanchez, T. W. (2025). Artificial intellig
Schön, D. A. (1983). The reflective pra
Basic Books. https://doi.org/10.4324/

(2019). Right for the wrong reasons: Diguage inference. Proceedings of the 57th
putational Linguistics, 3428–3448. https:
lage: Dwelling and urban space. Environ4), 649–671. https://doi.org/10.1068/
2003). A brief introduction to evidences, 2003, 29. https://doi.org/10.1002/
cs of algorithms: Mapping the debate. Big
rg/10.1177/2053951716679679
Planning knowledge and the regulatory
ssociation, 86 (2), 268–269. https://doi.
nning, living and judging: A multi-agent
anning. arXiv preprint arXiv:2412.20505.
0505
he Delphi method as a research tool: An
ions. Information & Management, 42 (1),
03.11.002
Accreditation standards for planning proProfessional standards and certification
upport systems: A conceptual framework
n Research Part A: Policy and Practice,
ra.2016.06.019
University of Chicago Press.
Dilemmas in a general theory of planning.
i.org/10.1007/BF01405730
M. (2025). Benchmarking large language
ral language processing in decoding pubrmatics, 4 (1), 17. https://doi.org/10.
rofessional standards and continuing prof knowledge within planning theory. Plan-
/10.1177/1473095207075161
ations: The turn to institutions in action.
gality in everyday practices of planning.
7/14730952211003535
(2025). The ethical concerns of artificial
e American Planning Association, 91 (2),
363.2024.2355305
ce for urban planning (1st ed.). Routledge.
tioner: How professionals think in action.
81315237473

Schön, D. A. (1992). Designing as reflective conversation with the materials of a
design situation. Knowledge-Based Systems, 5 (1), 3–14. https://doi.org/10.1016/
0950-7051(92)90020-G
Selbst, A. D., et al. (2019). Fairness and abstraction in sociotechnical systems.
Proceedings of the Conference on Fairness, Accountability, and Transparency, 59–68.
Singhal, K., et al. (2023). Large language models encode clinical knowledge. Nature,
620 (7972), 172–180. https://doi.org/10.1038/s41586-023-06291-2
Singhal, K., et al. (2025). Toward expert-level medical question answering with
large language models. Nature Medicine, 31 (2), 943–950. https://doi.org/10.1038/
s41591-024-03423-7
Stevens, M. R., Lyles, W., & Berke, P. R. (2014). Measuring and reporting intercoder reliability in plan quality evaluation research. Journal of Planning Education and
Research, 34 (1), 77–93. https://doi.org/10.1177/0739456X13513614
Tsai, C.-H., & Ku, H.-I. (2024). Why AI may undermine phronesis and what
to do about it. AI and Ethics, 5 (3), 3079–3086. https://doi.org/10.1007/
s43681-024-00457-4
Wang, D., et al. (2026). Generative AI meets future cities: Towards an era of autonomous urban intelligence. ACM AI Letters, 1 (1), 1–6. https://doi.org/10.1145/
3795141
Wei, J., et al. (2022). Chain-of-thought prompting elicits reasoning in
large language models. Advances in Neural Information Processing Systems, 35,
24824–24837. https://proceedings.neurips.cc/paper_files/paper/2022/hash/
9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html
Willson, R. (2020). Reflective planning practice: Theory, cases, and methods. Routledge.
Xiang, W.-N. (2016). Ecophronesis: The ecological practical wisdom for and from
ecological practice. Landscape and Urban Planning, 151, 97–102. https://doi.org/
10.1016/j.landurbplan.2016.03.006
Zheng, L., et al. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot
Arena. In A. Oh, T. Naumann, A. Globerson, K. Saenko, M. Hardt, & S. Levine
(Eds.), Advances in Neural Information Processing Systems 36 (pp. 46595–46623).
Curran Associates, Inc.
Zheng, Y., et al. (2025). UrbanPlanBench: A comprehensive urban planning benchmark for evaluating large language models. arXiv preprint. https://arxiv.org/abs/
2504.21027
Zhu, H., et al. (2024). PlanGPT: Enhancing urban planning with tailored language
model and efficient retrieval. https://doi.org/10.48550/arXiv.2402.19273
Zhu, H., et al. (2025, November). PlanGPT-VL: Enhancing urban planning with
domain-specific vision-language models. In Proceedings of the 2025 Conference on
Empirical Methods in Natural Language Processing: Industry Track (pp. 2461–2483).
https://aclanthology.org/2025.emnlp-industry.169/
Zoumpoulidi, M. E., Paraskevopoulos, G., & Potamianos, A. (2025). BloomWise:
Enhancing problem-solving capabilities of large language models using Bloom’staxonomy-inspired prompts. In Proceedings of the 3rd Workshop on Mathematical Natural Language Processing, 34–49. https://doi.org/10.18653/v1/2025.
mathnlp-main.3
31

Appendix A. Qualitative Analysis of Model Responses
This appendix presents verbatim model responses (chain-of-thought excerpts and answers) across selected items that illustrate the four epistemic diagnostics described in
Section 4.4. All examples are drawn from the English evaluation set (n = 405). Table
A1 summarizes the selected cases.
Table A1. Cross-model performance on selected diagnostic items
Item Level Pillar DS-R1 Tulu Q2.5 Q3-32B Claude Gemini GPT4o
243 Apply Principles 0 0 0 0 1 1 1
165 Under. Principles 1 0 0 0 1 1 0
324 Analy. Principles 0 1 0 1 1 1 0
84 Eval. Principles 0 0 1 0 1 1 1
6 Eval. Principles 0 0 0 1 1 1 1
Note. Items selected to illustrate the four epistemic diagnostics (Section 4.4). Scores indicate automated evaluation result (1 = correct, 0 = incorrect). Models: DS-R1 = DeepSeek-R1-Distill-Llama-8B; Tulu = Llama3.1-Tulu-3-8B; Q2.5-0.5B = Qwen2.5-0.5B-Instruct; Q3-32B = Qwen3-32B; Claude = Claude-Haiku; Gemini
= Gemini-2.5-Flash; GPT4o = GPT-4o-mini.
Illustrative Case: Regulatory Hallucination
Item 243 (Apply level, Principles pillar). All seven focus models were asked: “According to the general laws of urban development, a town is a transitional form between
traditional rural settlements and cities, usually developed in transportation nodes, resource distribution centers, or internal industrial aggregation areas within rural areas.
Its spatial form and functional evolution are often the result of spontaneous growth,
without clear planning guidance. [True/False]”
Claude-Haiku (correct, score = 1): Generated a nuanced analysis concluding “False”
with detailed reasoning about the role of planning policy in Chinese town development.
Chain-of-thought excerpt: “The statement presents a perspective on market town development... While towns do have spontaneous elements, the claim that they develop
‘without planning guidance’ is incorrect. In China’s context, town development is significantly influenced by policies such as ‘township planning’ and ‘rural revitalization.’ ”
DeepSeek-R1-Distill-Llama-8B (incorrect, score = 0): Acknowledged the complexity
but hedged its answer, demonstrating the phronetic deficit characteristic of weaker
models. The model correctly identified relevant policy frameworks but ultimately answered “True,” failing to recognize the Chinese institutional context that contradicts
the statement.
Illustrative Case: Conceptual Conflation
Item 165 (Understand level, Principles pillar). Models were asked to identify correct statements about the development process of urban planning. Option B stated:
“Medieval European urban development was based on functional zoning and spatial order.” Claude-Haiku correctly identified this as false (medieval cities were organic, not
functionally zoned). However, Qwen3-32B and GPT-4o-mini both incorrectly accepted
this statement, conflating medieval organic urban growth with modernist functionalist
planning—a clear instance of conceptual conflation where historically distinct planning
paradigms are treated as interchangeable.
32
