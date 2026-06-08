# BK05 - Mixed-Initiative Dialogue Management for Human-Virtual Agents Interaction in Forum Theatre Inspired Training

## Stable Widened-Core Snapshot

- core_layer: `bridge_core`
- admission_status: `promote_now`
- corpus_tier: `core`
- system_family: `BK05`
- paper_refs: `BK05`
- year: ``
- agent_count: `2-10`
- environment_side_representation: `3D_engine`
- agent_accessible_representation: `L2`
- behavioral_scale: `interaction`
- behavior_type: `dialogue; cooperation; other`
- evidence_status: `designed_affordance_only`
- spatial_behavior_coupling: `implicit`
- evaluation_method: `mixed`
- space_syntax_construct: `none`
- source_basis: `local_pdf_archived`
- artifact_class: `local_pdf`

## Representation Gap Note

Downloaded PDF confirms a VR training tool with virtual agents and reflection/replay; bridge because it is training interaction rather than social simulation.

## Original Artifact Pointer

- local_artifact_path: `assets/survey_paper/pdfs/phase1_adjacent/08_BK05_Forum_Theatre_Training.pdf`

## Source Content

Title: Mixed-Initiative Dialogue Management for Human-Virtual Agents Interaction in Forum Theatre Inspired Training

Source PDF: D:\0-AI相关研究\1-spatialagent\spatial-agent\assets\survey_paper\pdfs\phase1_adjacent\08_BK05_Forum_Theatre_Training.pdf

Extraction:
- backend: pypdf
- extracted_at_utc: 2026-04-28T16:33:00+00:00
- page_count: 5
- status: ok
- text_char_count: 18356

Metadata:
- author: Samuel Otofa ; Yacine Zerenini ; Frederic Bechet ; Benoit Favre ; Jean-Marie Pergandi ; Magalie Ochs
- doi: unknown
- keywords: unknown
- subject: IWSDS2026 2026

Outline:
- Introduction (page 1)
- The Forum Theatre approach (page 1)
- System overview (page 2)
- Dialogue Management and Interaction Strategy (page 2)
  - General Architecture (page 2)
  - Dialogue Controller (page 3)
- Use Case: Ordinary Sexism in Professional Situations (page 4)
- Conclusion (page 4)

Markdown Content:

Proceedings of the 16th International Workshop on Spoken Dialogue Systems Technology , pages 109–113
February 26–March 1, 2026. ©2026 Association for Computational Linguistics
109
Mixed-Initiative Dialogue Management for Human-Virtual Agents
Interaction in Forum Theatre Inspired Training
Samuel Otofa1, Yacine Zerenini2, Frederic Bechet 1, Benoit Favre1,
Jean-Marie Pergandi2,Magalie Ochs 1
1LIS - Aix Marseille University - CNRS - France,
2CRVM - Aix Marseille University - CNRS - France
Correspondence:magalie.ochs@lis-lab.fr
Abstract
This work presents a virtual reality (VR) train-
ing tool designed to raise awareness of social
discrimination (ethnic and gender-based) and
to train individuals to respond effectively when
witnessing such situations. Inspired by Au-
gusto Boal’s forum theatre, the system recre-
ates interactive scenarios of discrimination us-
ing autonomous virtual agents. From a di-
alogue system perspective, the project intro-
duces a hybrid dialogue management architec-
ture combining state-based control with Large
Language Model (LLM)-driven open dialogue.
This mixed-initiative approach allows the sys-
tem to manage structured training sequences
while supporting flexible, context-aware inter-
actions on sensitive topics. The demonstrator
illustrates this approach through a case of ordi-
nary sexism in a professional setting, highlight-
ing the potential of spoken dialogue systems in
VR for experiential learning and social behav-
ior training.
1 Introduction
In the field of training, increasing attention has
been directed towardsimulation-based learningus-
ing virtual environments. Numerous studies have
examined systems that simulate social interactions
withSocially Interactive Agents(SIAs) to foster the
development of social skills (Bruijnes et al., 2019),
applied to the medical domain (Prange et al., 2017;
Campillos-Llanos et al., 2015) or in the context of
teacher training (Pautler et al., 2018). These stud-
ies have shown that SIAs can effectively enhance
individuals’ interpersonal abilities, for instance, in
job interview preparation or intercultural commu-
nication training (Anderson et al., 2013; Hall et al.,
2011). However, several application domains re-
main underexplored, notably the use of SIAs for
training to prevent social discrimination, which is
the focus of the present study.
In this context, the demonstration system we
describe in this study is a virtual reality (VR) train-
ing tool designed to raise awareness of ethnic and
gender discrimination and to train users to react
appropriately as witnesses. Inspired by Augusto
Boal’s forum theatre, the system stages interactive
discrimination scenarios with autonomous virtual
agents. Users observe, analyze, and reenact these
situations to explore alternative responses.
Technically, the project introduces a hybrid dia-
logue architecture combining state-based control
with Large Language Model (LLM)-driven open
dialogue. This approach supports both structured
training and flexible, context-sensitive interactions.
The demonstrator we describe in the next sections
showcases the potential of VR dialogue systems for
experiential learning and social behavior training
in the context of workplace sexism.
2 The Forum Theatre approach
We aim to design and deploy avirtual reality(VR)
training tool intended to raise awareness of social
discrimination (both ethnic and gender-based) and
to train individuals to respond appropriately when
witnessing such situations. The tool draws inspi-
ration from theforum theatre technique, an inter-
active theatre method developed by Augusto Boal
in the 1960s (Boal, 1972). Originally conceived as
a form of popular education, forum theatre is now
widely used to promote awareness of social issues
such as discrimination and violence. It involves the
dramatization of a problematic situation performed
by actors, followed by active audience participa-
tion: spectators are invited to take the place of a
character and explore alternative actions to change
the course of events. This method not only raises
awareness but also enables participants todevelop
and practice concrete strategiesthey can later ap-
ply in real-life contexts.

110
Figure 1: Screenshot of a VR scene depicting a discrim-
inatory situation enacted by two autonomous virtual
characters
Figure 2: Screenshot of a VR scene in which the user
has the task to identify the different discriminatory be-
haviors observed in the previous scene through natural
langage dialog with a virtual character.
3 System overview
Within this framework, our demonstrator consists
of three main stages. In a first step, the user is
immersed, via a VR headset, in a simulated scene
depicting a discriminatory situation enacted by two
autonomous virtual characters (Figure 1). This cor-
responds to theWitness Stage. In a second step, the
user interacts with in natural langage with avirtual
characterto identify and analyze the different prob-
lematic behaviors observed in the scene. Through
dialogue, the character helps the user identify situ-
ations of discrimination that he may have observed
in the scene played out by the two virtual actors,
reminding him of different moments in the scene
and pointing out problematic behaviours (Figure
2). This is theDiscussion Stage. In a final step,
the user replays the same scene in VR simulated by
the two virtual actors, but in the step, the user em-
bodying the discriminated character, and attempts
to respond to the discriminatory behavior of the
virtual actor in order to resolve or transform the
situation. This is theConfrontation Stage.
Various interactive scenarios can be simulated,
encompassing different forms of social discrimi-
nation. In the proposed demonstration, we focus
onordinary sexismoccurring in diverse social con-
texts (e.g., hierarchical relationships, mixed-gender
interactions) and expressed through varying socio-
emotional behaviors of virtual agents (e.g., concil-
iatory vs. aggressive attitudes).Ordinary sexismis
defined as “stereotypes and collective representa-
tions that translate into words, gestures, behaviors
or actions that exclude, marginalise or inferiorize
women” (Grésy, 2009); for example, sexist remarks
and jokes or devious seduction.
The virtual actors are integrated into a VR plat-
form that simulates social interactions. As an initial
step, we use a collectedcorpus of forum theatre
performances on discriminationdescribed in (Ochs
et al., 2023). Motion capture was used in this cor-
pus to recreate realistic scenes with virtual charac-
ters and to model the behavior of discriminatory
agents (Figure 4). This behavioral modeling en-
ables the virtual actors to reproduce discriminatory
attitudes dynamically during interaction with the
user.
4 Dialogue Management and Interaction
Strategy
Our system adopts amixed-initiative dialogue man-
agement strategycombining predefined sequences
with open-ended interaction via aLarge Language
Model(LLM) API. Predefined sequences include
replayed discrimination scenes, system explana-
tions, and recovery mechanisms for sensitive user
inputs. During open-ended dialogue, adialogue
state representationtracks discussion topics, scene
progression, and critical events.
4.1 General Architecture
As shown in Figure 3, the system integrates an
Automatic Speech Recognition(ASR) module, a
dialogue controller, atext-to-speech synthesizer, a
VR animation manager, and anLLM-based chatbot.
We use theGoogle Speech APIfor ASR,inworld-
tts-1-max1 for speech synthesis, theUnity VR en-
gine2 for animation, and theGemini-2.5-flashLLM
for dialog turn generation.
Thedialogue controllercombines state-based
management with open conversational capabilities,
1https://inworld.ai/
2https://unity.com/solutions/vr

111
Speech
Recognition
Dialog State
Script
Sequences
Contextual Spoken
Language
Understanding
Warning
detection
?
Dialog State
Update
Chatbot LLM
Speech
Synthesis
+
VR animation
Script
detection
?
Prompt
Generation
Answer
Generation
speech
text
dialog history
+ dialog state
dialog history
+ dialog state
no
no
yes
yes
Script (text+VR)
Script ID
End
dialog ?
no
STOP
yes
Script ID
text+dialog state+
warning+script labels
dialog

controller
text prompt
text + metadata
Figure 3: Architecture of the dialogue controller.
ensuring both robustness and flexibility in handling
sensitive social interactions.
4.2 Dialogue Controller
LLM-based agents face two main challenges: main-
taining long-term coherence and preventing harm-
ful or inappropriate behavior. Previous studies have
addressed these issues through memory abstraction
techniques (Lee et al., 2023; Seo et al., 2025) and
output constraints (Rebedea et al., 2023). Our ap-
proach integrates both through a dynamicprompt
chaining mechanismand an explicitdialogue state
representationguiding conversation flow and goal
completion.
Our approach draws inspiration from these
works by integrating both a dynamicprompt chain-
ing mechanism, which continuously updates the
LLM prompt history to guide the conversation, and
an explicitdialogue state representationthat su-
pervises dialogue flow and ensures all goals are
fulfilled before the conversation ends.
In addition to these enhanced memory methods,
we implemented aproblematic situation detector
and acontextual scripted dialogue router, which
can temporarily override LLM control when neces-
sary. These modules are described below.
Dialogue State -This data structure maintains
both the dialogue history and the set of goals
achieved during the interaction. The active goal set
depends on the current stage (Witness, Discussion,
Confrontation) and consists of references to spe-
cific situations that must be addressed before the
dialogue can be concluded. For instance, during
the Discussion stage, the user is expected to com-
ment on each discriminatory situation identified in
the Witness stage. Each situation is represented
by a unique label, and the dialogue state structure
tracks which labels have already been discussed
and which remain pending.
Contextual Spoken Language Understanding
(CSLU) -This module analyzes the automatic
transcription of user speech in relation to the cur-
rent dialogue state. It provides four primary func-
tions: (1) detecting discriminatory situations based
on the current dialogue stage and updating the di-
alogue state to reflect newly discussed situations;
(2) triggering predefined scripted sequences in re-
sponse to the dialogue state and user input; (3)
detecting the completion of a dialogue stage and
returning control to the main VR menu system; and
(4) identifying problematic situations originating
from either the user or the LLM, and initiating cor-
rective scripted sequences or safely terminating the
interaction.
Scripted Sequences -This database contains pre-
defined VR sequences associated with each stage.
For instance, during theWitness Stage, the se-
quence is fully scripted, as will be described in
the next section. In theDiscussion Stage, scripted
sequences correspond to explanatory interventions
about specific discrimination situations, including
legal implications or contextual clarifications.

112
Prompt Generation -When the CSLU module
allows the LLM to generate the next system utter-
ance, this module constructs the prompt contain-
ing instructions for the LLM API. The LLM is
expected to return a JSON structure with two fields:
(1) a text output corresponding to the avatar’s
speech; and (2) an array, possibly empty, contain-
ing dialogue state labels identified in the current
conversational step. The prompt itself consists of
four parts: (1) a description of the persona played
by the LLM; (2) a description of the current dia-
logue stage, including the set of possible dialogue
states, their labels, and examples; (3) general be-
havioral guidelines for the persona; and (4) stage-
specific instructions summarizing the dialogue his-
tory and directing the next conversational goal
based on the dialogue state representation.
Answer Generation -Whether the response orig-
inates from a scripted sequence or an LLM output,
this module generates the corresponding VR in-
structions for speech synthesis and avatar move-
ment.
Dialogue State Update -At each interaction step,
the dialogue state representation is updated based
on the selected scripted sequence or the processed
LLM output.
5 Use Case: Ordinary Sexism in
Professional Situations
The developed training tool is illustrated through
a scenario depictingordinary sexismin the work-
place. The scene involves a conversation between a
male supervisor and his female employee regarding
an important assignment. Although the supervisor
intends to entrust her with the task, he expresses
doubts about her ability to lead a team. The sce-
nario was designed based on descriptions of ordi-
nary sexism in professional settings (Grésy, 2009,
2015), incorporating common behaviors such as:
condescension and paternalism(e.g., “my sweet-
heart”),denigration(e.g., “you don’t have the ca-
pacity for this job”),indirect seduction(encour-
aging stereotypical femininity),maternity offence
(e.g., “it’s not the right time for another child”),
part-time bias(e.g., “you’re lucky you’re not do-
ing anything tomorrow, Wednesday”), andsexist
remarks or jokes.
Two professional actors from the company
NextLevel performed the scene (Figure 4). Both
have extensive experience in forum theatre, a tech-
Figure 4: Extract from the recorded corpus showing
face-to-face interaction with discriminatory behaviors.
nique frequently used for corporate training on dis-
crimination awareness.
Based on motion capture data from the recorded
corpus, body animations were created usingiClone
and integrated intoUnity. Facial expressions were
extracted from the videos usingOpenFace(Amos
et al., 2016). In Unity, we developed two main
animation libraries,talkingandlistening, and de-
signed additionalidlemovements. These behaviors
were derived from the corpus, enhanced with Mix-
amo assets, and informed by our previous work
on virtual character animation. In total, we imple-
mented 8 idle, 10 listening, 9 talking, 19 facial, and
16 head movement animations.
Animations are layered (body, face, and head) to
generate varied full-body behaviors. Their selec-
tion (talking, listening, or idle) depends onanima-
tion statevariables in Unity, automatically updated
by thedialogue controller. A lightweight algorithm
ensures animation variability, while lip movements
are synchronized with speech using theSALSA lip-
synctool.
6 Conclusion
We present a VR training system that combines a
Large Language Model–driven dialogue controller
with realistic virtual characters to address everyday
sexism in professional contexts. The system re-
lies on a hybrid architecture that integrates scripted
sequences with open-ended dialogue, balancing
interaction flexibility with control in sensitive ex-
changes.
The proposed use case depicts a workplace sce-
nario inspired by real instances of ordinary sex-
ism. Future work will extend the approach to other
forms of social bias and include initial evaluations
of user engagement and learning outcomes based
on post-interaction surveys.

113
References
Brandon Amos, Bartosz Ludwiczuk, Mahadev Satya-
narayanan, et al. 2016. Openface: A general-purpose
face recognition library with mobile applications.
CMU School of Computer Science, 6(2):20.
Keith Anderson, Elisabeth André, Tobias Baur, Sara
Bernardini, Mathieu Chollet, Evi Chryssafidou, Ionut
Damian, Cathy Ennis, Arjan Egges, Patrick Gebhard,
et al. 2013. The tardis framework: intelligent vir-
tual agents for social coaching in job interviews. In
International Conference on Advances in Computer
Entertainment Technology, pages 476–491. Springer.
Augusto Boal. 1972. Catégories du théâtre populaire.
Travail théâtral, 6:3–26.
Merijn Bruijnes, Jeroen Linssen, and Dirk Heylen. 2019.
Special issue editorial: Virtual agents for social skills
training.
Leonardo Campillos-Llanos, D. Bouamor, Éric Bilin-
ski, Anne-Laure Ligozat, Pierre Zweigenbaum, and
S. Rosset. 2015. Description of the patientgenesys
dialogue system. InSIGDIAL Conference.
Brigitte Grésy. 2009.Petit traité contre le sexisme ordi-
naire. Albin Michel.
Brigitte Grésy. 2015. Le sexisme dans le monde du
travail, entre déni et réalité. Technical report, Rap-
port du Conseil supérieur de l’égalité professionnelle
entre les femmes et les hommes solidaire.
Lynne Hall, Susan J Jones, Ruth Aylett, Elisabeth An-
dre, Ana Paiva, Gert Jan Hofstede, Arvid Kappas,
Yukiko Nakano, and Toyoaki Nishida. 2011. Foster-
ing empathic behaviour in children and young people:
interaction with intelligent characters embodying cul-
turally specific behaviour in virtual world simulations.
INTED2011 Proceedings, pages 2804–2814.
Gibbeum Lee, V olker Hartmann, Jongho Park, Dimitris
Papailiopoulos, and Kangwook Lee. 2023. Prompted
LLMs as chatbot modules for long open-domain con-
versation. InFindings of the Association for Compu-
tational Linguistics: ACL 2023, pages 4536–4554,
Toronto, Canada. Association for Computational Lin-
guistics.
Magalie Ochs, Jean-Marie Pergandi, Alain Ghio, Carine
André, Patrick Sainton, Emmanuel Ayad, Auriane
Boudin, and Roxane Bertrand. 2023. A forum theater
corpus for discrimination awareness.Frontiers in
Computer Science, 5:1081586.
D. Pautler, Vikram Ramanarayanan, Kirby Cofino,
P. Lange, and D. Suendermann-Oeft. 2018. Leverag-
ing multimodal dialog technology for the design of
automated and interactive student agents for teacher
training. InSIGDIAL Conference.
Alexander Prange, Margarita Chikobava, P. Poller,
Michael Barz, and Daniel Sonntag. 2017. A multi-
modal dialogue system for medical decision support
inside virtual reality. InSIGDIAL Conference.
Traian Rebedea, Razvan Dinu, Makesh Narsimhan
Sreedhar, Christopher Parisien, and Jonathan Cohen.
2023. NeMo guardrails: A toolkit for controllable
and safe LLM applications with programmable rails.
InProceedings of the 2023 Conference on Empirical
Methods in Natural Language Processing: System
Demonstrations, pages 431–445, Singapore. Associa-
tion for Computational Linguistics.
Seongbum Seo, Sangbong Yoo, and Yun Jang. 2025. A
prompt chaining framework for long-term recall in
llm-powered intelligent assistant. InProceedings of
the 30th International Conference on Intelligent User
Interfaces, pages 89–105.
