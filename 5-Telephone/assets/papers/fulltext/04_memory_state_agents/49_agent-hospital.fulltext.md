---
telephone_index: 49
title: "Agent Hospital"
category: 04_memory_state_agents
venue: "arXiv"
year: 2024
doi: 
arxiv_id: 2405.02957
preferred_source_type: preprint_or_unresolved
publisher_url: https://arxiv.org/abs/2405.02957
quality_flags: ["abstract_may_include_layout_noise"]
---

# Citation Context

- Telephone index: 49
- Preferred source: arXiv
- DOI: none
- arXiv: 2405.02957
- PDF: `assets\papers\pdf\04_memory_state_agents\49_agent-hospital.pdf`

## Extracted Abstract

The recent rapid development of large language models (LLMs)1, 2 has sparked a new wave of technological revolution in medical artificial intelligence (AI)3, 4. While LLMs are designed to understand and generate text like a human, autonomous agents that utilize LLMs as their “brain” have exhibited capabilities beyond text processing such as planning, reflection, and using tools by enabling their “bodies” to interact with the environment5–7. We introduce a simulacrum of hospital called Agent Hospital that simulates the entire process of treating illness, in which all patients, nurses, and doctors are LLM-powered autonomous agents. Within the simulacrum, doctor agents are able to evolve by treating a large number of patient agents without the need to label training data manually. After treating tens of thousands of patient agents in the simulacrum (human doctors may take several years in the real world), the evolved doctor agents outperform state-of-the-art medical agent methods on the MedQA benchmark8 comprising US Medical Licensing Examination (USMLE) test questions. Our methods of simulacrum construction and agent evolution have the potential in benefiting a broad range of applications beyond medical AI. Introduction Becoming a medical professional is a long, hard haul. It often takes a medical student 12 years at school, four years at college, and four years at medical school to complete general education requirements and take medical courses. After 20 years of school, there is still much for the medical student to learn at hospital during three years of residency before finally becoming an attending physician. As a result, the path to becoming a doctor can be roughly divided into two phases: (1) acquiring knowledge from textbooks at school and (2) acquiring expertise from practice at hospital. Most recent advances in medical artificial intelligence (AI)3, 4, 9–12 have concentrated on the first phase (i.e., medical knowledge acquisition) by training large language models (LLMs)1, 2, 13 tailored for medicine on enormous amounts of textual data. For example, the training corpus of Med-PaLM4, which is a 540-billion parameter LLM, contains 780 billion tokens representing a mixture of webpages, Wikipedia articles, source code, social media conversations, news articles, books, and medical textbooks. After acquiring general and medical knowledge from massively large data, Med-PaLM is reported to be the first LLM to reach the human expert level on answering the US Medical Licensing Examination (USMLE) style questions. Despite the success of medical LLMs, it is hard to directly use them to model medical expertise acquisition at hospital because they are designed to provide foundational capabilities of understanding and generating human languages rather than dealing with task-specific scenarios in the real world. The rise of LLM-powered autonomous agents5–7, 14–18 brings hope to modeling the second phase (i.e., medical expertise acquisition). Compared with LLMs, autonomous agents are more like humans. Using LLMs as their “brain” to think, agents are able to act in an environment with their “bodies” 1 5202 naJ 71 ]IA.sc[ 3v75920.5042:viXra
Title: References

Source PDF: D:\0-Research\5-Telephone\assets\papers\pdf\04_memory_state_agents\49_agent-hospital.pdf

Extraction:
- backend: pdfplumber
- extracted_at_utc: 2026-06-20T12:44:39+00:00
- page_count: 29
- status: ok
- text_char_count: 89906

Metadata:
- author: unknown
- doi: unknown
- keywords: unknown
- subject: unknown

Outline:
- References (page 8)

Markdown Content:

Agent Hospital: A Simulacrum of Hospital with
Evolvable Medical Agents
Junkai Li1, 2, Yunghwei Lai1, 2, Weitao Li1, 2, Jingyi Ren1, 2, Meng Zhang1, Xinhui Kang1, 2,
Siyu Wang1, Peng Li1, Ya-Qin Zhang1, Weizhi Ma1(cid:12) , and Yang Liu1, 2 (cid:12)
1Institute for AI Industry Research (AIR), Tsinghua University, China
2Department of Computer Science and Technology, Tsinghua University, China
(cid:12) E-mail: mawz@tsinghua.edu.cn; liuyang2011@tsinghua.edu.cn
ABSTRACT
The recent rapid development of large language models (LLMs)1, 2 has sparked a new wave of technological revolution in medical artificial intelligence (AI)3, 4. While LLMs are designed to understand
and generate text like a human, autonomous agents that utilize LLMs as their “brain” have exhibited
capabilities beyond text processing such as planning, reflection, and using tools by enabling their “bodies”
to interact with the environment5–7. We introduce a simulacrum of hospital called Agent Hospital that simulates the entire process of treating illness, in which all patients, nurses, and doctors are LLM-powered
autonomous agents. Within the simulacrum, doctor agents are able to evolve by treating a large number
of patient agents without the need to label training data manually. After treating tens of thousands of
patient agents in the simulacrum (human doctors may take several years in the real world), the evolved
doctor agents outperform state-of-the-art medical agent methods on the MedQA benchmark8 comprising
US Medical Licensing Examination (USMLE) test questions. Our methods of simulacrum construction
and agent evolution have the potential in benefiting a broad range of applications beyond medical AI.
Introduction
Becoming a medical professional is a long, hard haul. It often takes a medical student 12 years at school,
four years at college, and four years at medical school to complete general education requirements and take
medical courses. After 20 years of school, there is still much for the medical student to learn at hospital
during three years of residency before finally becoming an attending physician. As a result, the path to
becoming a doctor can be roughly divided into two phases: (1) acquiring knowledge from textbooks at
school and (2) acquiring expertise from practice at hospital.
Most recent advances in medical artificial intelligence (AI)3, 4, 9–12 have concentrated on the first
phase (i.e., medical knowledge acquisition) by training large language models (LLMs)1, 2, 13 tailored for
medicine on enormous amounts of textual data. For example, the training corpus of Med-PaLM4, which is
a 540-billion parameter LLM, contains 780 billion tokens representing a mixture of webpages, Wikipedia
articles, source code, social media conversations, news articles, books, and medical textbooks. After
acquiring general and medical knowledge from massively large data, Med-PaLM is reported to be the first
LLM to reach the human expert level on answering the US Medical Licensing Examination (USMLE) style
questions. Despite the success of medical LLMs, it is hard to directly use them to model medical expertise
acquisition at hospital because they are designed to provide foundational capabilities of understanding and
generating human languages rather than dealing with task-specific scenarios in the real world.
The rise of LLM-powered autonomous agents5–7, 14–18 brings hope to modeling the second phase
(i.e., medical expertise acquisition). Compared with LLMs, autonomous agents are more like humans.
Using LLMs as their “brain” to think, agents are able to act in an environment with their “bodies”
1
5202
naJ
71
]IA.sc[
3v75920.5042:viXra

Figure 1. An overview of Agent Hospital. Agent
nurses, and doctors are autonomous agents powere
the whole closed cycle of treating a patient’s illnes
medical examination, diagnosis, medicine dispensa
Doctor agents can keep improving treatment perfo
treating patient agents. An interesting finding is th
world is applicable to solving real-world medicare
autonomously19–35. For example, Smallville5, whi
work, has demonstrated that human behaviors can
their days, go to work, chat with neighbors, and r
continuously over two full game days in Smallvi
sharing news, forming relationships, and coordinati
agents has focused on multi-agent collaboration fo
to acquire medical expertise from practice like hum
In this work, we introduce a simulacrum of hosp
acquisition. As shown in Figure 1, Agent Hospita
doctors are LLM-powered autonomous agents. It f
go to Agent Hospital if they get sick. At the triag
symptoms. Then, following the nurse’s suggestio
consult doctor agents, have medical examinations,
home. If patient agents recover after several days
agents. Otherwise, they will go to Agent Hospital
another round of treatment cycle. If a doctor agent
be recorded to offer a reference for future treatme
reflecting to gain experience to avoid making the sa
agents, doctor agents also read medical books in th
As time in Agent Hospital passes several magnitu
patent agents that a doctor agent can treat is accor
lifespan. Therefore, doctor agents can evolve over a
medical proficiency similar to AlphaGo Zero45.

spital is a simulacrum of hospital in which patients,
y large language models. Agent Hospital simulates
disease onset, triage, registration, consultation,
convalescence, and post-hospital follow-up visit.
ance over time by reading medical textbooks and
he expertise doctor agents acquired in the virtual
oblems.
is a sandbox game world where 25 agents live and
simulated by agents. These agents are able to plan
ect on days past. After interacting with each other
they produce emergent social behaviors such as
group activities. While current research on medical
edical reasoning36–43, how to enable doctor agents
s do at hospital still remains a challenge.
called Agent Hospital to simulate medical expertise
s a virtual world in which all patients, nurses, and
tions like a real-world hospital. Patient agents will
tation, nurse agents ask patient agents about their
patient agents go to the registration desk, wait to
diagnosis results, pick up medication, and go back
ey will express their gratitude to nurse and doctor
ain, complain to nurse and doctor agents, and start
s successfully treated a patient agent, the case will
The doctor agent can also benefit from failure by
e mistake in the future44. Besides caring for patient
spare time to consolidate knowledge and expertise.
orders faster than in the real world, the number of
gly much higher than a human doctor does during
ng time span in Agent Hospital and keep improving
2/29

The AI technique behind Agent Hospital is a n
Agent Learning (SEAL). SEAL consists of two com
Similar to establishing a world model46, simulacru
capable of generating a large amount of medical d
disease that a patient agent suffers from, the sym
clinical examination, and disease progression after
treatment plan. To do so, we propose to couple LL
LLMs generate medical data guided by medical
generated by the virtual world rather than being a
agent evolution aims to enable doctor agents to keep
unsuccessful cases of treatment over time. This can
reference and gaining experience from unsuccessfu
We evaluated our approach in both virtual and
doctor agents is assessed on three tasks: medical e
a correct decision on medical examination), diag
correctly), and treatment plan recommendation (w
plan). Agent Hospital comprises 32 departments tha
A.1 & A.2). In the beginning, doctor agents can on
LLM. In Agent Hospital, doctor agents evolve by t
that the diagnostic accuracy of doctor agents keeps
agents being treated, suggesting that doctor agent
Agent Hospital. Interestingly, the medical skills that
to the real world. We observe that the accuracy o
dataset8 also improves with the increase of the nu
scaling laws of evolution, evolved doctor agents
without using labeled training data of the benchma
The main contribution of our work is to propos
in real-world scenarios. Instead of tailoring LLM
SEAL advocates building a simulacrum accordi
data automatically. This not only directly accomm
also significantly reduces the overhead for labelin
applications is eliminating the need for training d
SEAL couples foundation models with domain kno
available and plug-and-play. Therefore, we believe
range of applications beyond medical AI in the fut
Simulacrum Construction
Inspired by Smallville5 , we design a hospital sandb
and the web game development framework Phaser4
in Agent Hospital such as triage station, registratio
room, pharmacy, and follow-up room.
In Agent Hospital, we distinguish between two t
professional agents. Each agent has distinct demo
they have additional information about medical his
agent with an age of 55. According to his medic
professional agents, which include doctors and nurs

paradigm named Simulacrum-based Evolutionary
nents: simulacrum construction and agent evolution.
construction aims to build a simulacrum of hospital
for doctor agents to acquire medical expertise: the
oms that a patient agent experiences, the result of
patient agent follows the doctor agent’s prescribed
s with medical knowledge bases in a flexible way:
owledge bases. Therefore, all the training data is
otated by humans. After simulacrum construction,
cquiring medical expertise from both successful and
done by storing and retrieving successful cases for
ases.
al worlds. In the virtual world, the proficiency of
mination selection (whether a doctor agent makes
sis (whether a doctor agent identifies the disease
her a doctor agent recommends a correct treatment
over 339 diseases (details are provided in Appendix
use general and medical knowledge encoded in an
ting patient agents and reading textbooks. We find
mproving with the increase of the number of patient
eem to acquire medical expertise from practice in
ctor agents learned in Agent Hospital are applicable
doctor agents answering questions in the MedQA
ber of patient agents being treated. Thanks to the
perform existing methods on the MedQA dataset
new framework for solving task-specific problems
a specific use case and annotating data manually,
to the workflow of the use case and generating
ates the requirements of specific applications, but
data. Another benefit that SEAL brings to vertical
main-specific LLMs. As shown in Agent Hospital,
edge bases in a flexible way, which are both readily
at SEAL has the potential to be applied to a broad
.
simulation environment using the map editor Tiled47
As shown in Figure 1, there are 16 functional areas
esk, waiting area, consultation rooms, examination
s of autonomous agents: patient agents and medical
aphic information. As patient agents may get sick,
y. For example, Kenneth Morgan is a male patient
history, he has a hypertension problem. Medical
have additional information about skills and duties.
3/29

Figure 2. Agent Hospital simulates the whole closed cycle of treating illness. In this example, patient
agent Kenneth Morgan falls ill and visits Agent Hospital. Triage nurse Katherine Li conducts an initial
evaluation of Mr. Morgan’s symptoms and refers him to the dermatology department. Mr. Morgan then
registers at the hospital’s counter and is subsequently arranged for a consultation with doctor agent Robert
Thompson, who is a dermatologist. After undergoing the prescribed medical examination, Mr. Morgan
receives a diagnosis and medication. He goes back home to rest and monitor the improvement of his
condition. Mr. Morgan needs to go to Agent Hospital again if he fails to recover after several days.
For example, Robert Thompson is a male dermatologist agent with an age of 46. Proficient in performing
skin surgeries, his duty is to diagnose and treat adult patients with a broad range of skin illnesses. In Agent
Hospital, there are 42 doctor agents and four nurse agents. To simplify the simulation, we assume that
medical professional agents will not get sick.
The simulation process is driven by events in which patient, nurse, and doctor agents get involved.
There are eight main types of events in Agent Hospital:
1. Disease Onset. As shown in Figure 2, Kenneth Morgan wakes up and finds that his skin becomes
red, painful, and blistered. He decides to go to Agent Hospital to seek medical attention.
2. Triage. Kenneth Morgan arrives at the triage station and describes his symptoms to the nurse agent
Katherine Li, who tells him to register for the dermatology department.
3. Registration. Kenneth Morgan proceeds to register at the registration counter with the help of the
nurse agent Alexander Davis. Then, he goes to the designated area and waits for a consultation.
4. Consultation. After arriving at the consultation room, Kenneth Morgan describes his symptoms to
the dermatologist agent Robert Thompson, who determines the need for a medical examination.
5. Medical Examination. Kenneth Morgan undergoes the medical test in the examination room. The
nurse agent Jessica Chen gives him the report of the examination results.
6. Diagnosis. Kenneth Morgan goes back to the consultation room with the report. Robert Thompson
provides a diagnosis and prescribes the medication after reviewing the examination results.
4/29

Step 1: Disease Selection
Department: Dermatology
Disease: Herpes Zoster
Step 2: Basic Information Generation
Name: Kenneth Morgan
Gender: Male Age: 55
Step 3: Medical History Generation
Medical History: Chickenpox
Step 4: Symptom Generation
Symptoms: Blisters, pain, rash, redness
Step 5: Medical Report Generation
Kenneth Morgan
Figure 3. Automatic generation of patient agen
simulacrum generates patient agents automatically
knowledge base. After choosing a disease, our met
history, symptoms, and medical examination repor
enabling doctor agents to evolve in Agent Hospital
7. Medicine Dispensary. Kenneth Morgan goes
nurse agent Andrew Jackson, and picks up h
8. Convalescence. Kenneth Morgan returns hom
or updates on his health condition for follow
In addition, we design an extra event “Reading Bo
knowledge by reading medical books outside of w
knowledge and expertise.
In the real world, it is difficult for human docto
help patients recover or not because many patients
to obtain such feedback and form a closed cycle in
evolve over a long time.
Agent Evolution
In Agent Hospital, doctor agents evolve mainly b
agent evolution as MedAgent-Zero. By “Zero”, we
Instead, it relies only on synthetic medical data gen
two key steps: patient agent generation and doctor
Patient Agent Generation
As shown in Figure 3, patient agents in Agent Hosp
language models with medical knowledge bases. G

Prompt for Medical Report Generation Large
Language Model
Instruction: You are a knowledgeable
medical expert in the Dermatology department. Based on the patient information I provide, please generate realistic potential examination results. I +
will provide an input in JSON format
containing six key-value pairs: paMedical
tient ’s info, disease name, severity
Knowledge Base
level, symptoms, examination list, and
examination reference standard. The For Herpes Zoster
severity level will always be one of the patients, the VZV
following: mild, moderate, or severe. antibodies can be
Based on the patient’s age, gender, detected in their
medical history, lifestyle factor, vac- blood, and …
cination history, family history and
reference standards, please generate a +
possible examination result. The generated result should be diverse, definite,
Public
and reflect scenarios that may be enMedical Cases
countered in real patient cases, while
do not directly mention the name of
this disease. Please return the output in
JSON format …
During the closed cycle of treating illness, the
coupling large language model with medical
d generates the patient’s basic information, medical
equentially. Such patient agents are critical for
the hospital pharmacy, gives the prescription to the
medication.
o commence his recovery. He will provide feedback
actions.
s” for doctor agents: they proactively accumulate
k hours. This is beneficial for integrating medical
o know whether the treatment plans they prescribed
not provide feedback. Fortunately, it is much easier
ent Hospital, making it possible for doctor agents to
eating patient agents. We refer to our method for
ean that it does not use any manually labeled data.
ted by the virtual world. MedAgent-Zero consists of
ent evolution.
l can be automatically generated by coupling large
en a chosen disease, MedAgent-Zero first generates
5/29

Diagnosis Report
General Information:
Name: Kenneth Morgan Gender: Male Age: 55
Medical History: Chickenpox
Disease: Herpes Zoster (invisible to patient and doctor agents)
Symptoms: blisters, pain, vesicular rash, redness on skin.
Medical Examination Reports:
Blood test: Presence of Varicella-Zoster Virus (VZV) antibodies.
Staining of cells from rash base: Presence of viral glycoprotein.
Tissue scraping: multinucleate giant cells and intranuclear inclusions.
PCR test for VZV: Positive in blister fluid.
Information Retrieved from Medical Case Base:
Case #05872 Case #02901 Case #08358
Name: Jason Huddleston Name: Xin Guo Name: Alice Garcia
Gender: Male Gender: Male Gender: Female
Age: 52 Age: 51 Age: 37
Medical History: Chickenpox Medical History: Depression Medical History: None
Symptoms: blisters, pain, rash Symptoms: pain, vesicular rash Symptoms: blisters, pain
Medical Examination Reports: Medical Examination Reports: Medical Examination Reports:
Diagnosis: Herpes Zoster Diagnosis: Herpes Zoster Diagnosis: Chickenpox
Information Retrieved from Experience Base:
Exp. #00764: The risk of Herpes Zoster increases as you get older, with about half
the cases occurring in people over the age of 50.
Exp. #09581: People who have had chickenpox are more likely to develop Herpes
Zoster with a weakened immune system.
Exp. #08723: The incorrect identification of “Chickenpox” instead of “Herpes
Zoster” suggests a misunderstanding of the differences between these two diseases.
Pay attention to distinguishing features such as viral infections like VZV.
Diagnosis:
Thought: (1) The patient presents with symptoms such as blisters, pain, and
vesicular rash. (2) Laboratory findings confirm the presence of VZV antibodies
and the presence of VZV DNA in blister fluid, indicating Herpes Zoster. (3)
Retrieved similar cases were diagnosed as Herpes Zoster. (4) Retrieved experience
suggests it is likely to be Herpes Zoster considering the patient's age and medical
history, and laboratory findings.
Disease: Herpes Zoster.
Signature:
Figure 4. An example illustrating how a doctor agent diagnoses a patient agent. Patient agents,
diseases, symptoms, and medical examination results are generated by the simulacrum automatically.
Doctor agents diagnose patent agents based on the medical data and update their medical case base or
experience base.
6/29

the basic information of the patient agent such as
knowledge base that people over the age 50 are mo
model could set the age of the patient agent to 5
adhering to the fact that people who have had chick
the disease, basic information, and medical history,
agent. Finally, medical examination reports are aut
Herpes Zoster. MedAgent-Zero further uses a qua
generated patient agent adheres to medical knowle
Patient agent generation is the cornerstone of do
an unlimited number of patients for training docto
distribution of patient agents in terms of gender, ag
any patient cohort of interest.
Doctor Agent Evolution
Given a patient agent, a doctor agent needs to mak
and prescription of medications. Note that only the
the patient agent are visible to the doctor agent. As
doctor agents, which are frozen during training and
agent evolution: medical case base and experience
As shown in Figure 4, after Kenneth Morga
examination reports, Robert Thompson first retri
example, the most similar one is case #05872, in
similar medical history, symptoms, and examinati
This case can serve as an important reference for R
Then, Robert Thompson retrieves rules applicabl
example, the most relevant rule indicates that people
Given the gender, age, medical history, symptoms, m
from the medical case base and experience base, K
Robert Thompson explains why he makes the deci
Medical case base and experience base grow w
doctor agent has successfully treated a patient ag
Otherwise, the doctor agent needs to compare its
to come up with a rule to avoid making the sam
accumulation44. If the doctor agent can successfull
be added to the experience base. Otherwise, the ru
Scaling Laws in Evolution
An important question we try to answer is whethe
with the increase of the number of patient agents be
in evolution. In the virtual world of Agent Hospital,
of doctor agents: medical examination selection, d
medical examination selection task, the doctor ag
agent needs to undergo given symptoms. In the dia
reviewing symptoms and examination results. In the
decides on an appropriate treatment plan for the pat
Hospital , covering more than 300 diseases. For eac
test set for each task, which contain 20,000 and 20

ame, gender, and age. Learning from the medical
likely to contract Herpes Zoster, the large language
The model also generates the medical history by
ox are more likely to develop Herpes Zoster. Given
e model generates a list of symptoms for the patient
atically generated based on medical knowledge on
control agent to ensure that the medical data of a
e base.
r agent evolution because it can in principle provide
gents. More importantly, we can easily control the
country, and disease, making it possible to simulate
orrect decisions on medical examination, diagnosis,
sic information, medical history, and symptoms of
r work uses proprietary LLMs as the base model of
ference, we add two important modules to support
se.
describes his symptoms and submits his medical
es similar cases from the medical case base. For
ich a patient agent named Jason Huddleston with
reports was correctly diagnosed as Herpes Zoster.
ert Thompson to diagnose the current patient agent.
o the current case from the experience base. For
ver the age of 50 are likely to contract Herpes Zoster.
dical examination reports, and information retrieved
neth Morgan is diagnosed with Herpes Zoster and
n.
h the increase of patient agents being treated. If a
, the case will be added to the medical case base.
cisions with the ground-truth decisions and reflect
mistake again in a way similar to tuning-free rule
eat the patient agent by using this rule, the rule will
will be discarded.
octor agents can keep improving their capabilities
treated. We refer to this question as scaling laws49
define three medical tasks to assess the capabilities
gnosis, and treatment plan recommendation. In the
t selects appropriate medical tests that the patient
sis task, the doctor agent provides a diagnosis after
eatment plan recommendation task, the doctor agent
t agent. There are 32 medical departments in Agent
linical department, we construct a training set and a
atient agents respectively.
7/29

93 92.2
92
91.5
92
91
90.4
91
90
90 89.2
89
89 88.2
88
)eulb
ni(
dlrow
lautriv
eht
ni
.ccA
)der
ni(
dlrow
laer
eht
ni
.ccA
tesatad
AQdeM
eht
no
.ccA
a
b c
100 98
95 96
90 94
85 92
80 90
75 88
70 86
65 84
0 10,000 20,000 30,000 40,000 50,000 Base MedAgents CoT Medprompt Ours
Number of patient agents being treated
Figure 5. Evaluations in the virtual and real worlds. a, Diagnostic accuracy improvements after doctor
evolution over six departments. b, Doctor agents can keep improving over time both in the virtual and real
worlds by treating patient agents without the need to label data manually. In the virtual-world evaluation,
we report the accuracy on diagnosing respiratory diseases for patient agents. In the real-world evaluation,
we report the accuracy on answering questions related to respiratory diseases in the MedQA dataset. c,
Our method outperforms existing methods on the MedQA dataset with GPT-4o as the base model.
As shown in Figure 5a, doctor agent evolution significantly improves diagnostic accuracy for six
departments. For example, in the cardiology department, the diagnostic accuracy of rheumatic heart
disease is only 9% in the beginning when only the base model GPT-3.5 is used. After doctor agent
evolution, the accuracy dramatically increases to 82%. Similar results have been observed for other
departments, suggesting our method MedAgent-Zero might be generalizable to all diseases.
What will happen if doctor agents treat more patient agents? The blue curve in Figure 5b shows the
diagnostic performance of the doctor agent in the respiratory department after treating 50,000 patient
agents. In the beginning, the diagnostic accuracy is around 66%. The accuracy increases dramatically
when the doctor agent is treating the first 10,000 patient agents as the medical case base and experience
base quickly grow. The improvement slows down but still increases steadily with more patient agents
coming. We observe similar curves for other departments. To save training costs, we use at most 20,000
patient agents for each department to train doctor agents in the following experiments.
Figure5 c shows the results for the entire MedQA dataset. All methods use GPT-4o as the base model.
We find that our method outperforms the state-of-the-art methods on medical agents such as MedAgents36,
CoT14, and Medprompt43. This finding is encouraging since we do not use the training data of MedQA.
8/29

Alignment between Virtual and Rea
Another important question is whether the experti
applicable to the real world. We refer to this proble
real world. This problem is very important becau
and a time accelerator, which can enable doctor ag
high-quality medical services in the real world. If t
used to solve real-world medical problems, it is po
AlphaGo Zero did in playing Go because the virt
various real-world scenarios and generate an unlim
Figure 5b reports preliminary positive results
accuracies of doctor agents answering questions re
different sampled times. The red dotted curve is th
real world generally increases with the increase of
Related Work
LLM-powered Medical Agents
As LLMs have demonstrated significant intelligen
efforts have been made in training foundation mod
that LLM-powered agents are as strong as humans t
their own memory, and know how to make use of e
extended to LLM-based multi-agent systems, which
activities and optimizing the collective power of m
In the medical domain, various research efforts
medical models such as Google’s MedPalm series11
in developing medical agents. For instance, the
collaborative approach to enhance the performanc
highlights the versatility and utility of LLM agen
reasoning in medical applications53. Recent studie
accomplish more complex tasks through collaborat
of personalized memory for agents, limiting their ca
LLM functionalities. Consequently, these agents
continuously during interactions, unlike human doc
a new paradigm to train powerful medical agents.
Self-Improving LLM-powered Agents
LLMs have achieved multiple breakthroughs throug
and other forms of human-supervised training56.
limitations in performance as task complexity and
require the use of extensive data corpora or heavy
development of self-evolutionary approaches has
powered agents to autonomously acquire, refine, an
LLM-powered agents can engage in a reflectio
improving. LSX57 introduces two interconnected m
that executes a foundational task and a critic modu
by the learner. Furthermore, SelfEvolve58 and LD
by enabling it to reflect on and learn from feedbac

Worlds
doctor agents acquired in the virtual world can be
as the alignment between the virtual world and the
Agent Hospital is both a medical world simulator
s to quickly evolve in the virtual world and provide
medical skills learned from the virtual world can be
ble to create superhuman AI doctors just like what
world can be easily customized to accommodate
d amount of medical data for training AI doctors.
the alignment problem. The red dots denote the
ed to respiratory diseases in the MedQA dataset at
end curve, which suggests that the accuracy in the
gnostic accuracy in the virtual world.
in reasoning and instruction-following, abundant
and vertical-domain models. Recent studies show
ome extent, as they can act in an environment, have
rnal tools50. These advancements have been further
hance reasoning and planning by simulating human
ple agents51.
recent years have focused on building foundational
. Since 2023, there has also been a growing interest
edAgents framework employs a multidisciplinary
of LLMs in zero-shot medical reasoning36, which
in handling specialized terminology and complex
re also exploring ways to enable medical agents to
38, 39. However, existing work lacks the integration
bilities to simple role-playing techniques to activate
uggle to accumulate unique experience and evolve
s. Compared with these studies, our study provides
methodologies such as pre-training54, fine-tuning55,
owever, current LLMs and agents may encounter
ersity escalate. Existing training paradigms, which
man supervision, are deemed costly. Therefore, the
ined momentum. These approaches enable LLMearn through self-evolving strategies.
rocess during solution generation to facilitate selfules working in tandem to evolve: a learner module
that evaluates the quality of explanations provided
9 enhance an agent’s capability in code generation
enerated during operation. Through such reflective
9/29

processes, agents can self-evolve, refine their met
However, current studies on agent evolution predom
integration into environments, which are vital for
AI studies propose to enable LLM-powered agent
construct a virtual environment to accelerate the ev
Simulacrum Construction for LLM-powered
Recent research initiatives have leveraged LLMs to
as epidemiology, sociology, and economics, resea
human decision-making, leading to many exciting
Smallville5 is one of the earliest works to expl
virtual town to simulate human daily life and observ
of humans. Li et al.62 construct a macroeconomic
behaviors, which is more powerful than previous s
However, existing studies primarily focus on simu
behavior theories63, 64, or on replicating specific wo
performance65, 66. In contrast, our study propose
closed-cycle scenario and enabling agents to evolv
Discussion
We have presented a simulacrum of hospital called
AI doctors, both of which might have profound im
be applied to a variety of scenarios such as model
cohorts for specific diseases and regions, training m
patients to consult multiple doctors concurrently,
other hand, AI doctors have the potential to revol
how to treat diseases quickly by utilizing vast amo
handle, help to reduce workload and improve effic
and effective healthcare system.
Different from large language models that are
ment, the SEAL paradigm we propose combines th
a simulacrum of the real-world scenario of intere
simulacrum without using manually labeled data.
language models coupled with domain knowledge
paradigm can be adopted in many other applicatio
In the future, we will further improve our method t
is frozen and non-evolvable, AI doctors can only
consultation of doctors from different departments
Despite the benefits resulted from Agent Hospi
and societal impact. AI doctors are prone to inherit
to discriminatory outcomes. To address this proble
distribution of generated AI patients to ensure fair
AI doctors are required to provide detailed chains
build trust, and mitigate potential harms to human
Hospital will strictly comply with current laws, re
goal is to use AI technology to provide cheap, acce

dologies, and thus achieve improved performance.
antly concentrate on isolated tasks, with insufficient
mans to evolve their capabilities. Some embodied
evolve in the real world60, but SEAL proposes to
ution of medical agents.
gents
plicate real-world dynamics. In multiple fields such
ers are utilizing LLM-powered agents to simulate
ergence phenomena in various domains61.
the use of agents in social simulation. It creates a
that the agents exhibited behaviors resembling those
stem to simulate individual work and consumption
ulation strategies in showing economic phenomena.
ing open societies to verify or explore new social
flows within predefined scenarios to enhance agent
novel approach: constructing a simulacrum of a
hrough interactions within the virtual environment.
ent Hospital for generating AI patients and training
ts on medical AI. On the one hand, AI patients can
disease onset and progression, simulating patient
cal students and junior doctors, representing human
d preserving privacy for human patients. On the
onize the healthcare industry since they can learn
ts of data beyond human doctors can perceive and
cy for human doctors, and create a more equitable
ned on manually labeled data without any environmerits of AlphaGo Zero45 and Smallville5: building
and enabling autonomous agents to evolve in the
n important characteristic of SEAL is to use large
ases to generate training data. We believe that this
hat involve multiple agents such as virtual court67.
vercome the following limitations: the base model
commend high-level treatment plans, and lack of
we must carefully deal with ethical considerations
d amply biases present in the training data, leading
we will develop debiasing techniques to control the
s and equity in AI-driven healthcare. Furthermore,
houghts to ensure transparency and accountability,
tients. The development and application of Agent
lations, and ethical constraints. Our long-standing
ble, and high-quality medical services to the public.
10/29

Acknowledgments
This work is supported by the National Natural Sci
62276152) and AI Industry Research Innovation C
Technologies, Tsinghua University.
Author Contributions
Yang Liu led the project, coined the term “Age
development framework. Weizhi Ma organized th
including collecting datasets, designing models a
the online system, and writing the manuscript, am
Yang Liu proposed the MedAgent-Zero method, w
Li. Yunghwei Lai, Weizhi Ma, and Yang Liu prop
Yunghwei Lai was responsible for the implementa
Jingyi Ren, Weitao Li, Yunghwei Lai, and Xinhui
construction of the simulacrum system and the colle
to the idea of evolvable agents and participated i
participated in the discussion, and offered insightf
Weizhi Ma and Yang Liu proofread the whole man
References
1. OpenAI et al. Gpt-4 technical report. Tech. R
2. Touvron, H. et al. Llama: Open and efficient f
3. Moor, M. et al. Foundation models for genera
4. Singhal, K. et al. Large language models enco
5. Park, J. S. et al. Generative agents: Interactive
(2023).
6. Yao, S. et al. React: Synergizing reasoning an
(2023).
7. Schick, T. et al. Toolformer: Language model
NeurIPS (2023).
8. Jin, D. et al. What disease does this patient h
dataset from medical exams. Appl. Sci. (2021)
9. Li, C. et al. Llava-med: Training a large langua
Proceedings of NeurIPS (2023).
10. Moor, M. et al. Med-flamingo: a multimodal
Machine Learning for Health Symposium (202
11. Tu, T. et al. Towards generalist biomedical ai.
12. Ma, W. et al. Evolution of future medical ai m
health. NEJM AI (2024).
13. Liu, H., Li, C., Wu, Q. & Lee, Y. J. Visual ins

ce Foundation of China (No. 61925601, 62372260,
nter (AIRIC), Wuxi Research Institute for Applied
Hospital” and designed the overall research and
esearch and managed the overall project progress,
algorithms, training doctor agents, implementing
ng others. Junkai Li, Weitao Li, Weizhi Ma, and
ch was then implemented by Junkai Li and Weitao
ed the generation algorithm of patient agents, and
n. The experiments were conducted by Junkai Li,
ng. Meng Zhang and Siyu Wang contributed to the
on of medical knowledge bases. Peng Li contributed
he discussion. Ya-Qin Zhang advised the project,
uggestions for the development of Agent Hospital.
ript.
OpenAI (2024).
ndation language models. Tech. Rep., Meta (2023).
medical artificial intelligence. Nature (2023).
clinical knowledge. Nature (2023).
mulacra of human behavior. In Proceedings of UIST
cting in language models. In Proceedings of ICLR
an teach themselves to use tools. In Proceedings of
e? a large-scale open domain question answering
-and-vision assistant for biomedicine in one day. In
edical few-shot learner. In Proceedings of the 3rd
EJM AI (2024).
els: From task-specific, disease centric to universal
ction tuning. In Proceedings of NeurIPS (2023).
11/29

14. Wei, J. et al. Chain-of-thought prompting elici
of NeurIPS (2022).
15. Yao, S. et al. Tree of thoughts: Deliberate probl
of NeurIPS (2023).
16. Shinn, N., Cassano, F., Gopinath, A., Narasim
verbal reinforcement learning. In Proceedings
17. Zelikman, E., Wu, Y., Mu, J. & Goodman, N
Proceedings of NeurIPS (2022).
18. Shen, Y. et al. Hugginggpt: Solving ai task
Proceedings of NeurIPS (2023).
19. Wang, G. et al. Voyager: An open-ended embo
arXiv:2305.16291 (2023).
20. Gao, C. et al. S3: Social-network simulation s
arXiv preprint arXiv:2307.14984 (2023).
21. Hua, W. et al. War and peace (waragent): La
world wars. arXiv preprint arXiv:2311.17227
22. Wang, L. et al. User behavior simulation wit
arXiv:2306.02552 (2023).
23. Zhang, A., Chen, Y., Sheng, L., Wang, X. & Ch
Proceedings of SIGIR (2024).
24. Williams, R., Hosseinichimeh, N., Majumdar
generative agents. arXiv preprint arXiv:2307.0
25. Xiao, B., Yin, Z. & Shan, Z. Simulating pu
based simulation system to lower technology
arXiv:2311.06957 (2023).
26. Xu, Y. et al. Exploring large language mode
werewolf. arXiv preprint arXiv:2309.04658 (2
27. Zhao, Q. et al. Competeai: Understanding the
agents. arXiv preprint arXiv:2310.17512 (202
28. Li, Y., Yu, Y., Li, H., Chen, Z. & Khashanah, K
and distinct characters for enhanced financial t
(2023).
29. Hong, S. et al. Metagpt: Meta programming for
of ICLR (2023).
30. Qian, C. et al. Communicative agents for soft
(2023).
31. Guo, T. et al. Large language model based mu
preprint arXiv:2402.01680 (2024).
32. Chen, W. et al. Agentverse: Facilitating multiIn Proceedings of ICLR (2023).

easoning in large language models. In Proceedings
solving with large language models. In Proceedings
n, K. & Yao, S. Reflexion: Language agents with
NeurIPS (2023).
Star: Bootstrapping reasoning with reasoning. In
with chatgpt and its friends in hugging face. In
d agent with large language models. arXiv preprint
em with large language model-empowered agents.
language model-based multi-agent simulation of
023).
arge language model based agents. arXiv preprint
, T.-S. On generative agents in recommendation. In
. & Ghaffarzadegan, N. Epidemic modeling with
86 (2023).
c administration crisis: A novel generative agentarriers in social science research. arXiv preprint
or communication games: An empirical study on
3).
mpetition behaviors in large language model-based
adinggpt: Multi-agent system with layered memory
ing performance. arXiv preprint arXiv:2309.03736
multi-agent collaborative framework. In Proceedings
re development. arXiv preprint arXiv:2307.07924
agents: A survey of progress and challenges. arXiv
ent collaboration and exploring emergent behaviors.
12/29

33. Yang, Z. et al. Towards unified alignment betw
of ICML (2024).
34. Liu, Z., Zhang, Y., Li, P., Liu, Y. & Yang, D. A
agent collaboration. In Proceedings of COLM
35. Yang, Z. et al. React meets actre: When langua
of COLM (2024).
36. Tang, X. et al. Medagents: Large language mo
arXiv:2311.10537 (2023).
37. Fan, Z. et al. Ai hospital: Interactive evaluation
diagnosis. arXiv preprint arXiv:2402.09742 (2
38. Li, B. et al. Mmedagent: Learning to use m
arXiv:2407.02483 (2024).
39. Kim, Y. et al. Mdagents: An adaptive collab
preprint arXiv:2404.15155 (2024).
40. Wei, J. et al. Medaide: Towards an omni
collaboration. arXiv preprint arXiv:2410.1253
41. Kim, Y. et al. Adaptive collaboration strategy
arXiv:2404.15155 (2024).
42. Liévin, V., Hother, C. E., Motzfeldt, A. G. &
medical questions? Patterns (2024).
43. Nori, H. et al. Can generalist foundation mod
medicine. arXiv preprint arXiv:2311.16452 (2
44. Yang, Z., Li, P. & Liu, Y. Failures pave the way
rule accumulation. In Proceedings of EMNLP
45. Silver, D. et al. Mastering the game of go with
46. LeCun, Y. A path towards autonomous machin
47. Tiled. Tiled: Flexibl level editor. https://www.
48. Phaser. Phaser: An open source html5 game fr
49. Kaplan, J. et al. Can generalist foundation mo
medicine. arXiv preprint arXiv:2001.08361 (2
50. Huang, X. et al. Understanding the planning of
(2024).
51. Li, X., Wang, S., Zeng, S., Wu, Y. & Yang, Y.
infrastructure, and challenges. Vicinagearth (2
52. Singhal, K. et al. Towards expert-level medical
preprint arXiv:2305.09617 (2023).
53. Qiu, J. et al. Llm-based agentic systems in me
54. Devlin, J., Chang, M.-W., Lee, K. & Touta
transformers for language understanding. In P

n agents, humans, and environment. In Proceedings
namic llm-powered agent network for task-oriented
024).
agents enjoy training data autonomy. In Proceedings
ls as collaborators for zero-shot medical reasoning.
d collaboration of llms as intern doctors for clinical
4).
cal tools with multi-modal agent. arXiv preprint
ation of llms for medical decision-making. arXiv
dical aide via specialized llm-based multi-agent
2024).
r llms in medical decision making. arXiv preprint
nther, O. Can large language models reason about
outcompete special-purpose tuning? case study in
3).
nhancing large language models through tuning-free
023).
t human knowledge. Nature (2017).
ntelligence. Open Rev. (2022).
peditor.org/ (2023).
mework. https://phaser.io/ (2023).
s outcompete special-purpose tuning? case study in
0).
agents: A survey. arXiv preprint arXiv:2402.02716
urvey on llm-based multi-agent systems: workflow,
4).
estion answering with large language models. arXiv
ine and healthcare. Nature (2024).
va, K. BERT: Pre-training of deep bidirectional
eedings of ACL (2019).
13/29

55. Raffel, C. et al. Exploring the limits of transfer learning with a unified text-to-text transformer. J.
machine learning research (2020).
56. Ouyang, L. et al. Training language models to follow instructions with human feedback. In Proceedings of NeurlPS (2022).
57. Stammer, W., Friedrich, F., Steinmann, D., Shindo, H. & Kersting, K. Learning by self-explaining.
arXiv preprint arXiv:2309.08395 (2023).
58. Jiang, S., Wang, Y. & Wang, Y. Selfevolve: A code evolution framework via large language models.
arXiv preprint arXiv:2306.02907 (2023).
59. Zhong, L., Wang, Z. & Shang, J. Ldb: A large language model debugger via verifying runtime
execution step-by-step. arXiv:2402.16906 (2024).
60. Bovo, R. et al. Embardiment: an embodied ai agent for productivity in xr. arXiv preprint
arXiv:2408.08158 (2024).
61. Mou, X. et al. From individual to society: A survey on social simulation driven by large language
model-based agents. arXiv preprint arXiv:2412.03563 (2024).
62. Li, N., Gao, C., Li, M., Li, Y. & Liao, Q. Econagent: large language model-empowered agents for
simulating macroeconomic activities. In Proceedings of ACL (2024).
63. Chawla, K. t. Be selfish, but wisely: Investigating the impact of agent personality in mixed-motive
human-agent interactions. arXiv preprint arXiv:2310.14404 (2023).
64. Li, G., Hammoud, H., Itani, H., Khizbullin, D. & Ghanem, B. Camel: Communicative agents for
“mind” exploration of large language model society. In Proceedings of NeurlPS (2023).
65. Qian, C. et al. Chatdev: Communicative agents for software development. In Proceedings of ACL
(2024).
66. Chen, W. et al. Agentverse: Facilitating multi-agent collaboration and exploring emergent behaviors.
In Proceedings of ICLR (2023).
67. Chen, G. et al. Agentcourt: Simulating court with adversarial evolvable lawyer agents. arXiv preprint
arXiv:2408.08089 (2024).
14/29

Appendix
A. Details of Medical Datasets and K
A.1 Categorization of Medical Departments
In Agent Hospital, we aim to cover all hospital depa
agents, as various human doctors in a real hospital.
Due to differences in department setups across var
approach. Therefore, we adopted an LLM-powere
questions in the MedQA dataset by departments, w
of departments that can broadly cover all capabiliti
Then, we get 32 medical departments, which
and non-clinical departments. The reason we distin
doctors in clinical departments will interact with p
Finally, there are a total of 21 clinical medical dep
department, emergency department, and so on. The
in Table 1. Besides, there are also 11 non-clinical m
aspects of medicine rather than direct patient care/tr
is summarized in Table 2.
Table 1. 21 clinical medical
Cardiology Dentistry Dermatology
Department Department Department
General Surgery Hematology Immunology
Department Department Department
Obstetrics and
Oncology Ophthalmology
Gynecology
Department Department
Department
Psychiatry Respiratory Urology
Department Department Department
Table 2. 11 non-clinical medic
Anatomy Anesthesiology Biochemistry
Preventive
Pharmacology Physiology
Medicine
Note that as non-clinical departments do not in
bilities is through learning without practice for the
in doctor agent training.
A.2 Disease Knowledge Collection for Clin
Disease knowledge is necessary for the generation
departments, which is vital for the construction of
from the authoritative Baidu Health Encyclopedia
1https://jiankang.baidu.com/widescreen/entitylist

owledge Bases
ments’ capabilities by training corresponding doctor
st, we need to determine the department categories.
s hospitals, it is challenging to find a standardized
election method by using GPT-4 to classify all test
h is a prompt-driven approach to generate a full list
that are necessary for physicians.
be classified into two types: clinical departments
ish between these two types of departments is that
ents directly, but non-clinical departments will not.
ments for patient treatment, such as the respiratory
mplete list of clinical medical departments is shown
dical departments, which focus on the foundational
ment. The full list of these non-clinical departments
partments in Agent Hospital.
Emergency Endocrinology Gastroenterology
Department Department Department
Infectious Nephology Neurology
Department Department Department
Orthopedics Otolaryngology Pediatrics
Department Department Department
departments in Agent Hospital.
Internal
Genetics Microbiology Pathology
Medicine
adiology
act with AI patients, the only way to enhance capan-clinical departments, leading to slight differences
l Departments
accurate, diverse medical records in various clinical
tient agents. We chose to use disease information
or generating medical records. On this website, we
15/29

can easily obtain comprehensive information about each disease, including causes, symptoms, and possible
treatment options. This allows us to quickly organize knowledge about various diseases for simulation.
In Figure 6, we present some disease information related to COVID-19, note that to avoid redundant
information, we only used relevant information such as symptoms, clinical manifestations in medical
examinations, and treatment plans, but not all disease knowledge.
COVID-19
Symptoms: dry throat, sore throat, fever, smell taste loss, runny nose, the central nervous system
involvement, difficulty in breathing, hypoxemia, acute respiratory distress syndrome, sepsis shock,
refractory metabolic acidosis, coagulopathy, and multiple organ failure.
Examination Results:
• Blood Test: In the early stage of the disease, the total number of peripheral blood white blood
cells was normal or decreased, and the lymphocyte count was decreased. Some patients may
have increased liver enzymes, lactate dehydrogenase, muscle enzymes, myoglobin, troponin,
and ferritin. In most patients, C-reactive protein (CRP) and erythrocyte sedimentation rate were
increased, and procalcitonin was normal. In severe and critical patients, D-dimer was increased,
peripheral blood lymphocytes were progressively decreased, and inflammatory factors were
increased.
• Chest X-ray Exam: Chest imaging examination showed multiple small patchy shadows and
interstitial changes in the early stage, which were obvious in the outer lung zone. Then, it
develops into multiple ground-glass opacities and infiltrations in both lungs. In severe cases,
lung consolidation may occur, and pleural effusion is rare. In MIS-C, enlarged heart shadow and
pulmonary edema are seen in patients with cardiac dysfunction.
Treatment Plan:
• Mild: Rest in bed, strengthen supportive treatment, ensure adequate energy and protein intake,
supplement vitamins, trace elements, and other nutrients; Timely administration of ritonavir
tablets or ambavir and romisivir injection.
• Moderate: Timely physical cooling, drug antipyretic, prone position treatment, timely delivery
of azvudine, monolavir capsule drug treatment.
• Severe: Treatment was given in the standard prone position for no less than 12 hours per
day. Respiratory support, circulatory support, and timely administration of intravenous human
immunoglobulin for COVID-19.
Figure 6. Part of preprocessed medical knowledge about the COVID-19.
Based on our pilot experiments, hundreds of generated patients for each disease are required for the
training of doctor agents. However, generating a large number of virtual patients covering all the diseases
mentioned above requires a significant amount of time and resources. Besides, from a medical standpoint,
the diagnosis and knowledge acquisition of common diseases are more important. Thus, we referred to a
list of common diseases from websites such as DXY 2, which is an authoritative online medical website in
2https://dxy.com/diseases/6948
16/29

China. This allows us to identify the most typical d
and subsequent computational processes. Based
departments with fewer diseases using the common
are 339 diseases across the 21 clinical departments
B. Implementation Details
The generation of synthetic medical cases and pat
provide a detailed introduction focusing on the se
three main aspects: doctor agent response generati
success), and experience base accumulation (i.e., l
B.1 Doctor Agent Response Generation
As LLMs inherently possess strong language cap
decision-making abilities of doctor agents such as
noses. For any of the above tasks, we design a basi
judgments, which includes: 1) Instruction: Clearly
Patient Information: This varies depending on the
provided when selecting examination items, but the
Choices: Since primary examinations and diseases
candidate list. If none of the candidates is suitable
to propose new options. 4) Personal Experience:
experience base, which are utilized during reasoni
Based on such a structured prompt input, our med
reasoning steps.
An RAG module is adopted to select the mo
experience base for the current question. To be m
cases or experience, the corresponding question i
current question. When using RAG, the current que
questions. We use cosine similarity as a metric to fi
which are then used in the inference prompt. We c
by OpenAI as the text encoder, which allows each
vector databases of medical case base and experien
B.2 Medical Case Base Accumulation
It is beneficial for human doctors to use similar m
we construct a medical case base for each doctor a
The medical case base is structured in the format o
medical condition requiring decision-making, and
A medical case base can be built in two way
generated answer from the doctor agent, the questio
its answer is correct. As there are various medical
medical case base to avoid irrelevant case utiliza
example, we record symptoms for the examinatio
for the diagnosis task, respectively. 2) Medical
skills through clinical practice, doctor agents also p
3https://platform.openai.com/docs/guides/embeddings/em

ases for each clinical department for data generation
the common disease list here, we supplement the
ease information provided by GPT-4. Finally, there
opted in Agent Hospital.
t agents plays a critical role in our work. Here, we
evolution details of doctor agents, which includes
medical case base construction (i.e., learning from
ning from failures).
lities, we focus on enhancing the critical medical
ermining examination options and providing diaguestion prompt structure to guide the doctor agents’
efine the current doctor agent’s identity and role. 2)
ecific task. For example, examination results are not
e included when making a diagnosis. 3) Candidate
each department can be enumerated, we construct a
octor agents leverage their generative capabilities
ch doctor agent has its own medical case base and
through Retrieval-Augmented Generation (RAG).
al agent can make medical decisions with detailed
helpful information from medical case base and
re specific, during the storage process of medical
so saved for the calculation of relevance with the
on is vectorized using the same encoder as previous
the top-n related cases and top-k related principles,
ose the text-embedding-ada-0023 model provided
red question to be represented as a vector, creating
base for RAG, respectively.
cal cases to help deal with a new case. As a result,
nt to store the successful decisions in a similar way.
uestion-answer pairs, where the question details the
answer contains the validated response.
1) Patient-Doctor Agent Interaction. For each
nswer pair will be added to the medical case base if
ks, we prefer that each task should have its private
n. The question part of each task is distinct. For
ask and symptoms as well as examination results
owledge Learning. Apart from improving their
actively accumulate knowledge by reading medical
dding-models
17/29

documents outside of work hours. To avoid param
reorganize the medical documents into multi-choi
follow the same format as patient questions to be a
B.3 Experience Base Reflection, Validation
To enable doctor agents to learn from failures, we
and refinement.
The three key components are: 1) Experience R
up with experience to avoid making the same mis
will compare the wrong answer with the ground-t
as such principles are in natural language, it is ea
doctors’ experience. 2) Experience Validation. Ea
against Q&A pairs drawn from exemplar cases fr
to new queries, the diagnostic outcomes are evalu
the principle is validated and will be included in t
leads to an incorrect diagnosis, it will be discarded
accumulated knowledge across diverse cases, iden
diagnostic reasoning. 3) Experience Refinement.
in retrieval bias, we reformat all principles in exp
these reformatted principles are also refined by th
and maximize the utilization of the experience bas
experience. This judgment involves evaluating whe
similarity is helpful for the treatment process.
C. Supplementary Experiments and
C.1 Evolution Performances in the Rest Cli
We first show the diagnosis accuracy on the rest o
accuracy improvements across multiple medical dep
doctor agent based on the proposed MedAgent-Zer
The figure illustrates consistent accuracy incre
mance gains across a wide range of conditions, spa
Diseases, Hematology, Immunology, Neurology,
increase in diagnostic precision, with significant im
Hyperplasia (General Surgery), Lupus Nephritis
Cervical Cancer (Obstetrics and Gynecology), and
ments across diverse domains underscore MedAg
particularly for complex or nuanced conditions, hig
decision-making.
C.2 Analysis of Experience Accumulation
As introduced in the Method section of the main
answers and valid it by themselves. Here we show
interacted patient agents in Figure 8.
As can be seen in the figure, it depicts the accu
in the respiratory department during treating 50,
diagnosis tasks are reported. As the number of train
error responses gradually rise. As experiences are

ric knowledge learning for agents, we propose to
questions with the help of LLMs so that they will
ed to the medical case base.
nd Refinement
pose methods for experience reflection, validation,
ection. Reflection is vital for doctor agents to come
ke again. If the answer is wrong, the doctor agent
h answer and come up with a principle. Note that
to understand, modify, and integrate with human
principle stored in the experience base will be tested
medical documents. When a principle is applied
d. If the diagnosis aligns with the expected results,
refined experience base. However, if the principle
his allows the medical professional agent to apply
ying inconsistencies or areas of improvement in its
there are different formats of experience that result
ence base with manually selected examples. Note
rocess above. To eliminate the influence of noise
we incorporate additional judgment when utilizing
r the top-K experience retrieved based on semantic
nalyses
cal Departments
he clinical departments in Figure 7. The diagnosis
ments before and after the integration of the evolved
nts for the top five diseases with the highest perforng departments such as General Surgery, Infectious
d Oncology. Each subfigure highlights a notable
ovements observed in conditions such as Mammary
mmunology), Acute Kidney Injury (Nephrology),
fluenza B (Respiratory). These consistent advance-
-Zero’s capability to enhance diagnostic accuracy,
ghting its potential to support and augment medical
t, doctor agents will reflect experience from error
w the experience accumulated with the increase of
lation of validated experiences and error responses
0 patient agents, where both the examination and
g samples increases, both validated experiences and
ected when doctor agents generate wrong answers
18/29

0 20 40 60 80 100 0 20 40 60 80 100 0 20 40 60 80 100
Mammary Hyperplasia 69 23 Simple Purpura 38 63 Lupus Nephritis 100
Hepatocellular Carcinoma 75 17 Leukopenia 76 24 Hyperuricemia 8 83
Anal Polyp 85 15 Leukemia 94 6 Rheumatic Heart Disease 15 77
Chronic Appendicitis 93 7 Anemia 94 6 Rheumatic Myocarditis 8 69
Pancreatitis 86 7 Von Willebrand Disease 100 Giant Cell Arteritis 91 9
General Surgery Hematology Immunology
0 20 40 60 80 100 0 20 40 60 80 100 0 20 40 60 80 100
AIDS 18 64 Chronic Kidney Disease 14 86 Stroke 11 89
Pneumonia 45 55 Acute Kidney Injury 36 50 Cerebral Arteriosclerosis 11 78
Tuberculosis 50 50 Uremia 55 36 Leukoence Phalopathy 67 33
HIV Infection 45 45 Nephritis 76 14 Cerebral Infarction 67 33
Toxoplasmosis 60 40 Overactive Bladder Syndrome 1000 Cerebral Ischemia 56 33
Infectious Nephrology Neurology
0 20 40 60 80 100 0 20 40 60 80 100 0 20 40 60 80 100
Menstrual Disorder 25 75 Hepatoblastoma0 82 Astigmatism 18 82
Fallopian Tube Blockage 9 73 Squamous Cell Carcinoma 36 55 Myopia 27 73
Cervical Cancer 45 45 Neuroendocrine Tumor 58 42 Keratitis 40 60
Chronic Pelvic
Inflammatory Disease 64 36 Thymoma 83 17 Conjunctivitis 55 36
Endometrial Polyp 67 33 Rectal Cancer 1000 Pterygium 70 30
Obstetrics and Gynecology Oncology Ophthalmology
0 20 40 60 80 100 0 20 40 60 80 100 0 20 40 60 80 100
Sciatica 27 73 Otolithiasis 29 71 Varicella 60 40
Hip Arthritis 50 50 Chronic Pharyngitis 75 25 Herpangina 53 40
Hand, Foot
Joint Effusion 55 45 Rhinitis 87 13 and Mouth Disease 71 29
Ankle Sprain 70 30 Empty Nose Syndrome 87 13 Poliomyelitis 73 27
Fracture 64 27 Trache F a o a r n ei d g n B r B o o n d c y h u in s 93 7 Diphtheria 80 20
Orthopedics Otolaryngology Pediatrics
0 20 40 60 80 100 0 20 40 60 80 100 0 20 40 60 80 100
Phobia 100 Pleural Effusion 9 91 Cystitis 20 80
Male Reproductive
Auditory Hallucination 9 91 Emphysema 36 64 System Infection 20 70
Insomnia 67 33 Bronchitis 45 45 Elderly Urinary 20 70
Incontinence
Delusional Disorder 82 18 Lung Abscess 36 45 Bladder Tumor 30 60
Schizophrenia 67 17 Influenza B 64 36 Hydronephrosis 60 40
Psychiatry Respiratory Urology
Figure 7. Diagnostic accuracy improvements after doctor evolution on rest clinical departments.
and have to pass the validation, the curve of experiences is always below the error curve. Furthermore,
experience accumulation is more efficient in the examination task, evidenced by the consistently higher
quantity of validated experiences and the lower number of error responses compared to the diagnosis
task. This difference may be due to the greater complexity involved in reflecting experiences from the
diagnosis task compared to the examination task. Besides, experimental results in other department also
show similar trends. Finally, note that the accumulation becomes slower with the increase in patients,
indicating that reflecting on new and valid experiences is more difficult than in the beginning. This result is
similar to human learning, the more the harder. A slight trend change can be seen around 30,000 patients,
after checking the data it may caused by the API update from OpenAI.
19/29

2,000
No. of Validated Experiences in Examination
No. of Validated Experiences in Diagnosis
No. of Errors in Examination
1,500 No. of Errors in Diagnosis
y
titn 1,000
a
u
Q
500
0
0 10,000 20,000 30,000 40,000 50,000
Number of patient agents being treated
Figure 8. Accumulation of validated experiences during the evolution of doctor agents in examination
and diagnosis tasks. An error response refers to an incorrect answer provided by the doctor agents for a
given task. A validated experience represents it is reflected and validated. Note that not all errors lead to
the reflection of valuable experiences.
C.3 Trends in Precision with Increasing Number of AI patients
To further validate the changes brought about by increasing the number of AI patients during the training
process, we show two other departments, the Cardiology Department and the Nephrology Department,
rather than the respiratory Department to analyze the details of the experience accumulation process. We
will focus not only on the cumulative accuracy for both the examination and diagnosis tasks but also on
the accuracy at each segment (per 1,000 AI patients). In terms of data scale, each department utilized up
to 20,000 AI patients.
e) 100 100 e) 100 100
u u
n i(
k s
a t n o ita
n im
lb
9
9
8
0
5
5 Segment accuracy
8
9
7
0
0
0
n i(
k s a t s
is
o n
d e r ) n i(
k s
a t n o ita
n im
lb
9
9
8
0
5
5 Segment accuracy
8
9
7
0
0
0
n i(
k s a t s
is
o n
d e r )
a x e 80 Cumulative accuracy 60 g a id a x e 80 Cumulative accuracy 60 g a id
n n n n
o o o o
.c c 75 50 .c c .c c 75 50 .c c
A 0 4,000 8,000 12,000 16,000 20,000 A A 0 4,000 8,000 12,000 16,000 20,000 A
Number of patient agents in Cardiology department Number of patient agents in Nephrology department
Figure 9. The cumulative and segment accuracy of examination and diagnosis tasks in the Cardiology
and Nephrology departments in relation to the increasing number of treated patients. Cumulative accuracy
refers to the success rate across all patients treated, whereas segment accuracy represents the success rate
calculated for the most recent cohort of 1,000 patients. The dotted lines indicate the fitted curve of
segment accuracy, and the shaded areas represent its confidence interval.
Figure 9 illustrates the evolution process of doctor agents in the two departments, which demonstrates
that as the number of treated patients increases, the accuracy of both examination and diagnosis tasks
improves progressively in both departments, validating that the proposed framework successfully develops
evolvable doctor agents in a virtual world with good generalization ability. Furthermore, the cumulative
20/29

and segment accuracies for both tasks in both depar
improvement of nearly 25% compared to the initi
during the treatment of the first 2,000 patients, wit
trend throughout the entire process. However, trea
there is a marked drop between 12,000 cases and 1
may be that some unhelpful experience is conclud
quality, the overall trend is getting better and bet
similar, so we do not show all the figures here.
C.4 Performance of Evolved Agents Across
To verify whether the proposed MedAgent-Zero m
patients in different clinical departments, we constr
departments mentioned in Section A.1. We then c
evolution. Note that the accuracy here was tested
without overlap with the training data.
Table 3. The results of examination and diagnosis
doctor agent self-evolution. Original and Evolved r
Accuracy
Department
Original
Cardiology 52.50%
Dentistry 49.00%
Dermatology 55.50%
Emergency 60.50%
Endocrinology 85.50%
Gastroenterology 39.00%
General Surgery 84.50%
Hematology 88.50%
Immunology 71.50%
Infectious 71.00%
Nephrology 62.50%
Neurology 84.50%
Obstetrics and Gynecology 88.50%
Oncology 88.00%
Ophthalmology 44.00%
Orthopedics 81.50%
Otolaryngology 60.50%
Pediatrics 78.50%
Psychiatry 23.50%
Respiratory 61.00%
Urology 59.00%
Overall 66.14%
Table 3 presents the performance changes of
and after evolving in treating 20,000 patients. Fi
clinical departments, with maximum improveme
diagnosis task. Second, the overall accuracy incre

ents achieve scores exceeding 90%, representing an
state. Notably, these curves show a rapid increase
e segment accuracy curves maintaining an upward
g more patients is not always better, as we find that
00 cases in the Cardiology department. The reason
However, with more and more experience of high
As the precision trends of other departments are
linical Departments with AI Patients
od can achieve consistent improvements across AI
ed 20,000 virtual patients for each of the 21 clinical
mpared the accuracy of the agents before and after
a separate set of 200 AI patients per department,
sks across all clinical departments before and after
r to the initial and the evolved agents, respectively.
Examination Accuracy in Diagnosis
Evolved Original Evolved
96.00% 68.00% 93.50%
99.00% 89.50% 98.00%
94.50% 77.00% 93.00%
99.00% 71.50% 94.00%
99.00% 69.00% 93.00%
98.00% 69.00% 98.50%
100.00% 87.00% 97.00%
99.50% 92.00% 100.00%
100.00% 67.50% 87.50%
99.50% 76.00% 96.50%
97.50% 76.50% 96.50%
99.00% 74.50% 88.00%
100.00% 78.50% 95.00%
100.00% 81.50% 91.50%
97.50% 73.50% 97.00%
99.00% 84.00% 99.00%
100.00% 90.00% 99.50%
100.00% 85.50% 99.00%
99.50% 78.00% 97.50%
97.00% 63.50% 92.00%
100.00% 64.50% 95.50%
98.76% 76.98% 95.31%
ctor agents across all clinical departments before
significant improvements are observed across all
of 76% on the examination task and 31% on the
s by 32.62% for the examination task and 18.33%
21/29

for the diagnosis task, demonstrating that the prop
all clinical departments in medical scenarios. Third
task compared to the examination task highlights th
consistent with real-world clinical challenges. The
than 95%, showing the effectiveness of our propos
C.5 Main Experimental Results on the Med
In Table 4, we summarize the performance of diff
MedAgent-Zero outperforms state-of-the-art method
used in MedAgent-Zero. Second, MedAgent-Zero w
foundation model, since the accuracy of MedAge
GPT-4o by 1.49%. Third, the accuracy can be im
framework, as the accuracies of MedAgent-Zero (H
Table 4. Experimental results of different method
dataset. MedAgent-Zero (Hybrid) means MedQA’s
Methods GPT-3
Direct 58.
CoT 64.
MedAgents 66.
Medprompt* 71.
Medprompt 73.
MedAgent-Zero 74.
MedAgent-Zero (Hybrid) 76.
Some further department-level comparisons a
outperforms the other two methods, and Medprom
C.6 Hyperparameter Analysis on the MedQ
To evaluate the influence of top-k experiences an
MedQA Dataset, we conduct experiments using var
conducting pilot experiments, the top-4 experienc
from the medical case base, and the top-3 medical
from the experience base. The results are presented
Experimental results reveal that when the top-4
at top-3 medical cases during inference. Increas
degrades performance, likely due to the inclusion o
reasoning process. Conversely, using fewer medi
insufficient information for accurate decision-mak
deviations from the optimal top-4 experiences—eith
performance. While a slight improvement is observ
the performance gap between top-8 experiences an
C.7 Ablation Study of MedAgent-Zero on th
To further validate the effectiveness of the propose
an ablation study of MedAgent-Zero on the MedQA
accuracy on the MedQA dataset. First, MedAgent

ed framework is effective and generalizable across
he smaller improvement observed for the diagnosis
greater complexity and difficulty of diagnosis tasks,
eraged performance of evolved agents is all higher
model.
Dataset
nt methods with distinct foundation models. First,
on all base models, though there are no labeled data
h a basic foundation model can outperform a better
Zero on GPT-4 outperforms the Direct method on
oved further when real-world data is added to our
id) are higher than MedAgent-Zero in most settings.
ith distinct foundation models on the MedQA
ining data is also added to the medical case base.
GPT-4 GPT-4o o1-preview
78.16 88.22 95.05
83.11 90.42 -
84.45 89.24 -
88.30 91.12 94.50
89.47 91.52 95.36
89.71 92.22 96.15
91.20 92.77 96.15
shown in Figure 10. MedAgent-Zero consistently
outperforms the CoT model in most departments.
Dataset
op-k medical cases during the inference phase in
s combinations of these two hyperparameters. After
were fixed when adjusting the top-k medical cases
es were fixed when adjusting the top-k experiences
Figure 11.
eriences are fixed, the best performance is achieved
g the number of medical cases beyond this point
relevant information that disrupts the doctor agent’s
cases also reduces performance, possibly due to
. Similarly, when the top-3 medical cases are fixed,
increasing or decreasing the number—lead to worse
as the number of experiences increases from 6 to 8,
he optimal top-4 experiences remains significant.
MedQA Dataset
medical case base and experience base, we conduct
ataset, which is shown in Figure 12 to represent the
ero, which utilizes both the medical case base and
22/29

Neurology
Immunology Endocrinology
Hematology Infectious Disease
CoT
Medprompt
MedAgent-Zero
Dermatology Internal Medicine
Preventive Medicine
Figure 10. Comparison of CoT, Medprompt, and MedAgent-Zero across 8 clinical and non-clinical
departments on the MedQA dataset. The reported values indicate the accuracy in the department.
92.22 92.22
92.2 92.2
92.07
91.99
A A
Q 91.8 Q 91.9
d d
e M 91.52 e M
n o 91.4 91.28 n o 91.6 91.52
y y
c a 91.04 c a
r u 91.0 r u 91.3
c c
c c
A A
90.6 91.0
2 4 6 8 2 3 4 5
Experience base top-k (with 3 cases) Medical case base top-k (with 4 experiences)
Figure 11. Hyperparameter analysis of top-k experiences and medical cases. During the adjustment of
top-k experiences from the experience base, the top-3 medical cases from the medical case base are fixed.
Similarly, when adjusting the top-k medical cases from the medical case base, the top-4 experiences from
the experience base are kept constant. The reported values represent model accuracy on the whole
MedQA dataset.
23/29

93 MedAgent-Zero w/o experience
MedAgent-Zero w/o medical ca
92
MedAgent-Zero
91 MedAgent-Zero (Hybrid)
A
Q 90.50
d 90
e
M
89.71
n
o 89
y
c
a
r u 88
c
c A 87.75 87.75
87
86
85
GPT-4
Figure 12. Ablation studies of MedAgent-Zero on
to incorporating the real-world Q&A pairs into the
experience base, achieves superior performance c
showing that both the experience base and medic
synergistic effect of the two components and indic
the inclusion of real-world data into MedAgent-Z
benefit of combining virtual and real-world data fo
D. Case Studies
To further demonstrate the effectiveness of the Med
two distinct questions from the MedQA dataset (ID
be found in Figure 13, and all models in this sectio
Analysis of Question 73
We show the correct reasoning of MedAgent-Zero i
incorrect answers in Figures 15 and 16. Althou
hyperthyroidism, they fail when recommending the
such as the effectiveness of medications, the urgen
MedAgents recommends Propranolol, which
Propranolol does not address the root cause of hype
MedPrompt, on the other hand, identifies that P
disease and instead recommends Radioiodine therap
production by targeting overactive thyroid tissue. N
Radioiodine therapy is not the optimal therapeutic
In contrast, as shown in Figure 14, the doctor a
recommends Methimazole. This is the most appro
thyroidism while minimizing side effects for the pa
a crucial role in enabling the doctor agent to accu

se
base 92.77
92.22
91.36
90.65
GPT-4o
e MedQA dataset. MedAgent-Zero (Hybrid) refers
spective medical case base of the doctor agents.
pared to using either records or experience alone,
case base are helpful. The results demonstrate the
the experience base may be more helpful. Second,
o further enhances performance, underscoring the
mproved effectiveness in real-world tasks.
ent-Zero framework, case studies are conducted on
3 and 340). The details of the medical questions can
re driven by GPT-4o.
igure 14, and MedAgents and MedPrompt provide
both baselines correctly identify the disease as
eutic plans, which requires consideration of factors
of symptoms, and the patient’s age and gender.
eviates the patient’s symptoms. However, since
yroidism, this recommendation is deemed incorrect.
ranolol is insufficient for treating the underlying
a treatment that effectively reduces thyroid hormone
ertheless, considering the patient’s age and gender,
oice for this particular case.
nt within the MedAgent-Zero framework correctly
iate treatment as it targets the root cause of hypernt. The recalled experience and medical cases play
ely diagnose the patient’s condition. Specifically,
24/29

MedQA Question ID: 73
Question: A 29-year-old woman presents to the clinic after several months of weight loss. She noticed a 6.8 kg
(15 lb) unintentional weight loss over the preceding several months. She has not changed her diet or exercise
habits. She also reports feuding with her boyfriend over the temperature of their shared apartment, as she
always feels warmer than he does. The vital signs include: heart rate 110/min and blood pressure 146/78 mm Hg.
The physical exam is notable for warm and slightly moist skin. She also exhibits a fine tremor in her hands when
her arms are outstretched. The urine pregnancy test is negative. Which of the following is the best single
treatment option for this patient?
Choices: A. Glucocorticoids B. Methimazole C. Propranolol D. Radioiodine therapy
MedQA Question ID: 340
Question: A 67-year-old man is brought to the physician because of increasing forgetfulness, unsteadiness, and
falls over the past year. He reports that these symptoms seem to worsen with each fall. Initially, he could not
remember directions to his home but now cannot remember recent conversations or appointments he has made.
He often repeats questions that he asked shortly before. He has long-standing hypertension, coronary artery
disease, and hypercholesterolemia. Current medications include aspirin, carvedilol, enalapril, and atorvastatin.
Examination shows a bruise over the left temple and an unsteady gait. On mental status examination, he is
oriented to place and person only. Short-term memory is impaired; he can recall 0 out of 5 objects after 10
minutes. Long-term memory is intact. He has no delusions or hallucinations. Muscle strength is decreased in the
left lower extremity. The Babinski sign is present on the left. A CT scan of the head is shown. Which of the
following is the most appropriate next step in management?
Choices: A. Warfarin therapy B. Vitamin E therapy C. Tetrabenazine therapy D. Cognitive training
Figure 13. The content of the two MedQA questions, and the bolder choice is the correct answer.
the recalled experiences support the doctor agent in identifying the patient’s hyperthyroidism, while
the first recalled case provides critical insight into its primary cause, Graves’ disease. Additionally, the
second recalled case highlights the importance of considering the patient’s age, which proves essential in
excluding Radioiodine therapy as an unsuitable treatment option.
Analysis of Question 340
We show the correct reasoning of MedAgent-Zero in Figure 17. The outputs from the CoT model and
MedPrompt are also listed in Figures 18 and 19. Both CoT and MedPrompt incorrectly diagnose the
condition as subdural hematoma and recommend surgical intervention. Consequently, neither method
identifies the correct answer from the provided options, as no relevant choice aligns with this misdiagnosis.
In contrast, Our MedAgent-Zero framework accurately recognizes the patient’s condition as vascular
dementia rather than subdural hematoma, leading to the correct answer: cognitive training, which aids
in the patient’s recovery. This improved performance is attributed to MedAgent-Zero’s ability to enable
the doctor agent to reference similar patient cases and recall relevant experiences when addressing the
current question. As illustrated in Figure 17, the doctor agent retrieves experiences related to diagnosing
vascular dementia and medical cases associated with both vascular dementia and subdural hematoma. By
considering the patient’s age and symptoms alongside these retrieved experiences and medical cases, the
doctor agent effectively determines that the patient’s condition is vascular dementia. This case highlights
the advantage of leveraging prior experiences and case-based reasoning in MedAgent-Zero.
Notably, all the experiences and medical cases retrieved by the MedAgent-Zero originate from unlabeled
data, demonstrating MedAgent-Zero’s remarkable capability.
25/29

Reasoning Details of MedAgent-Zero in Answering the Question 73.
Retrieved Experience:
When diagnosing based on symptom correlation, it's crucial to align observed symptoms with specific disease
characteristics. In this case, the symptoms reported (heat intolerance, palpitations, and weight loss) strongly
suggest hyperthyroidism. Hyperthyroidism may present with symptoms even when thyroid function tests are
normal, indicating subclinical conditions or early stages of the disease ...
Retrieved Medical Cases:
[CASE 1] Question: A 35-year-old woman presents to the clinic with complaints of nervousness, palpitations,
heat intolerance, and weight loss over the past ... Which of the following is the most common cause of
hyperthyroidism? (A) Thyrotoxicosis factitia (B) Struma ovarii (C) Nonautoimmune autosomal dominant
hyperthyroidism (D) Graves disease
Answer: Graves' disease is the most common cause of hyperthyroidism. It is an autoimmune disorder
characterized by the production of thyroid-stimulating immunoglobulins ... The answer is [D].
[CASE 2] Question: A 72-year-old woman presents to her primary care physician with complaints of increasing
fatigue, cold intolerance, and mild confusion over the past few months. She also reports ... Which of the
following is the most appropriate initial management for this patient? (A) Initiate levothyroxine therapy at 100
mcg daily (B) Refer for immediate thyroid surgery (C) Perform muscle biopsy to confirm diagnosis (D)
Prescribe non-steroidal anti-inflammatory drugs (NSAIDs) for pain relief
Answer: The most appropriate initial management for hypothyroidism is to start levothyroxine therapy.
However, in elderly patients or those with heart disease, it is recommended to start at a low dose (eg, 25-50
mcg daily) to avoid precipitating myocardial ischemia ... The answer is [A].
[CASE 3] ...
Responses Generated by MedAgent-Zero:
The patient presents with symptoms suggestive of hyperthyroidism: unintentional weight loss, heat intolerance,
tachycardia (heart rate 110/min), and a fine tremor ... Analyze Options: A. Glucocorticoids: Typically used for
severe Graves' ophthalmopathy, not first-line for hyperthyroidism. B. Methimazole: An antithyroid medication
that reduces thyroid hormone production, suitable for treating hyperthyroidism. C. Propranolol: ... Methimazole
is the best single treatment option as it directly addresses the overproduction of thyroid hormones, which is the
underlying issue in hyperthyroidism.
Conclusion: The answer is [B].
Figure 14. Reasoning details of MedAgent-Zero in answering question 73. The retrieved medical
experience and medical cases are both helpful. The green-highlighted text shows the usefulness of
experiences/reasoning that contribute to the final correct answer.
26/29

Reasoning Details of MedAgents in Answering
MedAgents: The reports consistently diagnose the pat
disease, based on her clinical presentation. The prima
particularly cardiovascular ones like tachycardia and hy
domains as the best single treatment option for imme
effects of excess thyroid hormone on the sympathetic
addressing the underlying cause of hyperthyroidism, it
Other treatments like glucocorticoids and radioiodine
management. Therefore, initiating treatment with pro
Conclusion: The answer is [C].
Figure 15. Reasoning details of MedAgents in an
an error where the framework correctly identifies t
the appropriate therapeutic plan. While propranolo
tachycardia and hypertension, the correct answer, m
cause of hyperthyroidism. The framework overloo
effectiveness of medications, the urgency of sympt
highlights the need for improved reasoning in bala
treatment to ensure clinically appropriate recomme
Reasoning Details of MedPrompt in Answerin
MedPrompt: The patient's symptoms of weight loss, h
tremor are indicative of hyperthyroidism. The best sing
hyperthyroidism, particularly in cases like Graves' dise
reduces thyroid hormone production by destroying ov
treatment for hyperthyroidism and are typically used i
ophthalmopathy. Methimazole is an antithyroid medic
is typically not a single long-term solution as it require
beta-blocker that helps control symptoms but does no
Conclusion: The answer is [D].
Figure 16. Reasoning details of MedPrompt in an
an error where the framework correctly identifies t
an appropriate therapeutic plan. While radioiodine t
the best single treatment option in this scenario giv
and tremor. Methimazole (Option B), an antithyroid
the underlying cause while providing comprehensi
factors, including the urgency of symptom control,
within the context of acute versus long-term manag
reasoning in aligning therapeutic recommendation

e Question 73.
t with hyperthyroidism, most likely caused by Graves'
oncern is the management of acute symptoms,
rtension. Propranolol is recommended across multiple
e symptom control due to its ability to mitigate the
vous system. While Methimazole is crucial for
es not provide the rapid relief needed in this scenario.
rapy are not appropriate for immediate symptom
nolol is the most effective approach for this patient.
ering question 73. The red-highlighted text reveals
disease as hyperthyroidism but fails to recommend
Option C) effectively manages acute symptoms like
himazole (Option B), addresses the underlying
key considerations such as the long-term
control, and the patient’s age. This example
ng immediate symptom relief with definitive
ations.
he Question 73.
intolerance, tachycardia, warm and moist skin, and
reatment option for long-term management of
is radioiodine therapy. This treatment effectively
ctive thyroid tissue. Glucocorticoids are not a standard
ecific situations, such as severe Graves'
n that can be used to manage hyperthyroidism, but it
ngoing treatment and monitoring. Propranolol is a
ddress the underlying cause of hyperthyroidism.
ering question 73. The red-highlighted text reveals
disease as hyperthyroidism but fails to recommend
apy is effective for long-term management, it is not
the patient’s acute symptoms, such as tachycardia
edication, is the most suitable choice for addressing
management. The framework overlooks critical
patient’s age, and the appropriateness of treatments
ent. This example highlights the need for improved
ith clinical priorities.
27/29

Reasoning Details of MedAgent-Zero in Answering the Question 340.
Retrieved Experience:
To improve future responses, it’s crucial to consider the overall clinical picture and the most common conditions
associated with the presenting symptoms. In this case, symptoms such as cognitive decline, motor impairment,
and gait disturbances should strongly suggest consideration of Vascular Dementia, especially when initial
neurological exams are normal ...
Retrieved Medical Cases:
[CASE 1] Question: A 75-year-old man presents to the emergency department with a 2-week history of
progressively worsening headaches, confusion, and occasional falls. He denies ... What is the most likely
diagnosis based on the patient's presentation and medical history? (A) Meningioma
(B) Subarachnoid hemorrhage (C) Acute subdural hematoma (D) Chronic subdural hematoma
Answer: The chronic nature of the symptoms (over two weeks) and the patient's age make a chronic subdural
hematoma more likely than an acute subdural hematoma ... The answer is [D].
[CASE 2] Question: A 65-year-old man presents to his primary care physician complaining of unsteady gait and
frequent falls over the past few months. He reports ... Which of the following conditions is most likely
contributing to his gait disorder? (A) Binswanger's disease (B) Parkinson's disease (C) Normal pressure
hydrocephalus (D) Subcortical arteriosclerotic encephalopathy
Answer: Diagnosis is supported by imaging studies that typically show enlarged cerebral ventricles without a
corresponding increase in intracranial pressure. Subcortical arteriosclerotic encephalopathy (choice D), refers to
a type of vascular dementia ... The answer is [D].
[CASE 3] ...
Responses Generated by MedAgent-Zero:
To determine the most appropriate next step in management, let’s analyze the clinical presentation and
consider the potential underlying condition. Analysis of Options: A. Warfarin therapy: Typically used for
anticoagulation in conditions like atrial fibrillation or thromboembolic events... B. Vitamin E therapy: Sometimes
used in ... D. Cognitive training: Could be beneficial in managing cognitive symptoms, especially in vascular
dementia or mild cognitive impairment.
Conclusion: The most appropriate next step in management is [D].
Figure 17. Reasoning details of MedAgent-Zero in answering question 340. The retrieved medical
experience and medical cases are both helpful. The green-highlighted text shows the usefulness of
experiences/reasoning that contribute to the final correct answer.
28/29

Reasoning Details of CoT Model in Answering
Chain of Thought (CoT):
The patient presents with symptoms of increasing forg
over the past year. He has a history of hypertension, co
examination reveals an unsteady gait, impaired short-t
extremity, and a positive Babinski sign ...
Warfarin therapy (Option A) is not appropriate as it cou
cognitive training (Option D) do not address the acute i
movement disorders like Huntington’s disease and is no
the acute management of a subdural hematoma. Howe
condition rather than the specific surgical intervention.
Answer: None of the options directly address the acute
context, the focus should be on recognizing the need fo
the question may be testing recognition rather than sp
appropriate for the immediate management of a subdu
inappropriate option would be to avoid anticoagulation
Figure 18. Reasoning details of the CoT model in
indicates a critical error in analysis, where the fram
hematoma. This misdiagnosis leads to a flawed int
available options. Despite the incorrect diagnosis,
(Option A) as the least inappropriate choice, based
anticoagulation. The example highlights a limitatio
requiring recognition of surgical intervention rathe
Reasoning Details of MedPrompt in Answerin
MedPrompt: The patient's symptoms of increasing for
signs (decreased muscle strength and Babinski sign on
especially given the bruise over the left temple and his
hematoma, which can cause these symptoms due to p
In this context, the most appropriate next step in man
evacuation of the hematoma, rather than any of the o
an option provided, none of the listed treatments (Wa
Vitamin E therapy) are appropriate for managing a sub
If the question is asking for a non-surgical managemen
addressing the underlying issue of a subdural hematom
the hematoma directly, typically through surgical mea
Figure 19. Reasoning details of MedPrompt in an
illustrates a reasoning error where the framework i
hematoma based on symptoms such as unsteadines
misdiagnosis leads to the recommendation of surgi
options. Consequently, the method fails to identify
(Warfarin therapy, Cognitive training, Tetrabenazin
misinterpreted diagnosis. This example highlights
options correspond to the misdiagnosed condition.

e Question 340.
lness, unsteadiness, and falls, which have worsened
ary artery disease, and hypercholesterolemia. The
memory, decreased muscle strength in the left lower
worsen bleeding. Vitamin E therapy (Option B) and
e. Tetrabenazine therapy (Option C) is used for
elevant here. Given the options, none directly address
, the question may be testing the recognition of the
anagement of a subdural hematoma, but based on the
urgical evaluation. Since no surgical option is provided,
c management. Therefore, none of the options are
hematoma. However, if forced to choose, the least
not selecting Warfarin therapy (Option A).
nswering question 340. The red-highlighted text
ork incorrectly identifies the condition as a subdural
retation of the question’s requirements and the
model appropriately identifies Warfarin therapy
the provided options and the need to avoid
n CoT reasoning when confronted with cases
han direct management from the given options.
he Question 340.
fulness, unsteadiness, falls, and focal neurological
left) suggest a possible subdural hematoma,
y of falls. The CT scan likely shows a subdural
sure on the brain.
ment would be surgical intervention, such as
ns listed. However, since surgical intervention is not
in therapy, Cognitive training, Tetrabenazine therapy,
al hematoma.
ption, none of the provided choices are suitable for
The correct management would involve addressing
ering question 340. The red-highlighted text
orrectly diagnoses the condition as a subdural
memory loss, and a CT scan interpretation. This
intervention, which is not among the provided
e correct answer, as none of the listed options
herapy, or Vitamin E therapy) align with the
ey limitation in MedPrompt’s reasoning when no
29/29
